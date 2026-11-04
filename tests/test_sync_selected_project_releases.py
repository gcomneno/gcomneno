from __future__ import annotations

import importlib.util
import io
import json
import sys
import traceback
import unittest
from contextlib import redirect_stderr, redirect_stdout
from http.client import BadStatusLine, HTTPException, IncompleteRead
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.error import HTTPError, URLError
from unittest.mock import patch

from scripts import bilingual_write as writer

SCRIPT_PATH = (
    Path(__file__).parents[1]
    / "scripts"
    / "sync_selected_project_releases.py"
)
SPEC = importlib.util.spec_from_file_location(
    "sync_selected_project_releases",
    SCRIPT_PATH,
)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class SelectedRepositoryContractTests(unittest.TestCase):
    def test_selected_repositories_match_canonical_table_composition(self) -> None:
        self.assertEqual(
            MODULE.SELECTED_REPOSITORIES,
            (
                "atelier-kit",
                "smart-file-organizer",
                "lele-manager",
                "giadaware-ui-components",
                "gyte",
                "ubuntu-system-tools",
                "giadaware-ai",
                "gyte-ai-learning-pipeline",
            ),
        )


def profile_fixture(*, omit: str | None = None) -> str:
    rows = []
    for repository in MODULE.SELECTED_REPOSITORIES:
        if repository == omit:
            continue
        rows.append(
            f"| [{repository}](https://github.com/gcomneno/{repository}) "
            "| [v0.0.1](https://example.test/old) | Description | Signal |"
        )
    return "\n".join(rows) + "\n"


def repository_metadata(repository: str = "example") -> dict:
    return {
        "name": repository,
        "full_name": f"gcomneno/{repository}",
        "owner": {"login": "gcomneno"},
        "private": False,
        "archived": False,
        "disabled": False,
        "visibility": "public",
    }


def release_metadata(repository: str = "example") -> dict:
    return {
        "tag_name": "v2.0.0",
        "html_url": f"https://github.com/gcomneno/{repository}/releases/tag/v2.0.0",
        "draft": False,
        "prerelease": False,
    }


def json_response(payload: object) -> io.BytesIO:
    return io.BytesIO(json.dumps(payload).encode("utf-8"))


def api_error(status: int) -> HTTPError:
    return HTTPError(
        "https://example.test/private-metadata-sentinel",
        status,
        "private-metadata-sentinel",
        hdrs=None,
        fp=None,
    )


class ReleaseLookupTests(unittest.TestCase):
    def assert_sync_aborts(self, responses: list) -> None:
        """Fail a later lookup after an earlier project has a pending update."""
        with TemporaryDirectory() as directory:
            paths = {
                "en": Path(directory) / "README.md",
                "it": Path(directory) / "README.it.md",
            }
            for locale, path in paths.items():
                path.write_text(f"{locale}\n{profile_fixture()}", encoding="utf-8")
            originals = {path: path.read_bytes() for path in paths.values()}
            first = MODULE.SELECTED_REPOSITORIES[0]
            responses = [
                json_response(repository_metadata(first)),
                json_response(release_metadata(first)),
                *responses,
            ]
            stdout, stderr = io.StringIO(), io.StringIO()
            with (
                patch.object(MODULE, "README_PATHS", paths),
                patch.object(MODULE, "urlopen", side_effect=responses) as open_url,
                patch.object(MODULE, "write_bilingual") as write,
                redirect_stdout(stdout), redirect_stderr(stderr),
            ):
                self.assertEqual(MODULE.main(), 1)
            self.assertEqual(open_url.call_count, len(responses))
            self.assertEqual(
                open_url.call_args_list[2].args[0].full_url,
                "https://api.github.com/repos/gcomneno/"
                + MODULE.SELECTED_REPOSITORIES[1],
            )
            write.assert_not_called()
            for path, original in originals.items():
                self.assertEqual(path.read_bytes(), original)
            self.assertEqual(list(Path(directory).glob(".*")), [])
            self.assertEqual(stdout.getvalue(), "")
            self.assertIn("Release sync aborted", stderr.getvalue())
            self.assertIn("READMEs left unchanged", stderr.getvalue())
            self.assertNotIn("private-metadata-sentinel", stderr.getvalue())

    def test_eligible_repository_and_official_release(self) -> None:
        with patch.object(MODULE, "urlopen", side_effect=[
            json_response(repository_metadata()),
            json_response(release_metadata()),
        ]) as open_url:
            release = MODULE.fetch_latest_release("example")
        self.assertEqual(
            release,
            MODULE.OfficialRelease(
                tag_name="v2.0.0",
                html_url=release_metadata()["html_url"],
            ),
        )
        self.assertEqual(
            [call.args[0].full_url for call in open_url.call_args_list],
            [
                "https://api.github.com/repos/gcomneno/example",
                "https://api.github.com/repos/gcomneno/example/releases/latest",
            ],
        )
        for call in open_url.call_args_list:
            self.assertEqual(call.kwargs, {"timeout": 20})
            self.assertEqual(
                call.args[0].get_header("Accept"), "application/vnd.github+json"
            )

    def test_identity_comparison_is_case_insensitive(self) -> None:
        metadata = repository_metadata("EXAMPLE")
        metadata["owner"] = {"login": "GComneno"}
        metadata["full_name"] = "GComneno/EXAMPLE"
        with patch.object(MODULE, "urlopen", side_effect=[
            json_response(metadata), json_response(release_metadata()),
        ]):
            self.assertIsNotNone(MODULE.fetch_latest_release("example"))

    def test_repository_flags_require_explicit_false(self) -> None:
        for flag in ("private", "archived", "disabled"):
            for value in (True, None, 0, 1, "false", "", [], {}):
                with self.subTest(flag=flag, value=value):
                    metadata = repository_metadata(MODULE.SELECTED_REPOSITORIES[1])
                    metadata[flag] = value
                    self.assert_sync_aborts([json_response(metadata)])
            with self.subTest(flag=flag, missing=True):
                metadata = repository_metadata(MODULE.SELECTED_REPOSITORIES[1])
                del metadata[flag]
                self.assert_sync_aborts([json_response(metadata)])

    def test_visibility_must_be_explicitly_public(self) -> None:
        for value in ("private", "internal", "unknown", "PUBLIC", "", None, False, 0, []):
            with self.subTest(visibility=value):
                metadata = repository_metadata(MODULE.SELECTED_REPOSITORIES[1])
                metadata["visibility"] = value
                self.assert_sync_aborts([json_response(metadata)])
        metadata = repository_metadata(MODULE.SELECTED_REPOSITORIES[1])
        del metadata["visibility"]
        self.assert_sync_aborts([json_response(metadata)])

    def test_missing_or_mismatched_repository_identity(self) -> None:
        for field in ("name", "full_name", "owner"):
            for value in (None, False, 42, [], {}, "private-metadata-sentinel"):
                with self.subTest(field=field, value=value):
                    metadata = repository_metadata(MODULE.SELECTED_REPOSITORIES[1])
                    metadata[field] = value
                    self.assert_sync_aborts([json_response(metadata)])
            with self.subTest(field=field, missing=True):
                metadata = repository_metadata(MODULE.SELECTED_REPOSITORIES[1])
                del metadata[field]
                self.assert_sync_aborts([json_response(metadata)])

        second = MODULE.SELECTED_REPOSITORIES[1]
        for changes in (
            {"owner": {"login": "private-metadata-sentinel"}},
            {"owner": {"login": False}},
            {"full_name": f"private-metadata-sentinel/{second}"},
            {"name": "private-metadata-sentinel"},
            {
                "name": "private-metadata-sentinel",
                "full_name": "gcomneno/private-metadata-sentinel",
            },
        ):
            with self.subTest(changes=changes):
                metadata = repository_metadata(second)
                metadata.update(changes)
                self.assert_sync_aborts([json_response(metadata)])

    def test_metadata_errors_abort_before_release_lookup(self) -> None:
        for error in (
            api_error(404), api_error(403), api_error(500),
            URLError("private-metadata-sentinel"),
            TimeoutError("private-metadata-sentinel"),
            OSError("private-metadata-sentinel"),
        ):
            with self.subTest(error=type(error).__name__):
                self.assert_sync_aborts([error])

    def test_malformed_metadata_aborts_before_release_lookup(self) -> None:
        for payload in (None, [], "private-metadata-sentinel", 0, False):
            with self.subTest(payload=payload):
                self.assert_sync_aborts([json_response(payload)])
        for raw in (b"{private-metadata-sentinel", b"\xff"):
            with self.subTest(raw=raw):
                self.assert_sync_aborts([io.BytesIO(raw)])

    def test_protocol_errors_abort_without_writes_at_either_lookup(self) -> None:
        for lookup in ("metadata", "release"):
            for error in (
                HTTPException("private-metadata-sentinel"),
                BadStatusLine("private-metadata-sentinel"),
                IncompleteRead(b"private-metadata-sentinel"),
            ):
                with self.subTest(lookup=lookup, error=type(error).__name__):
                    response = io.BytesIO()
                    responses = [response]
                    if lookup == "release":
                        responses.insert(0, json_response(repository_metadata(
                            MODULE.SELECTED_REPOSITORIES[1]
                        )))
                    with patch.object(response, "read", side_effect=error):
                        self.assert_sync_aborts(responses)

    def test_lookup_tracebacks_do_not_disclose_exception_details(self) -> None:
        for responses in (
            [api_error(404)],
            [URLError("private-metadata-sentinel")],
            [BadStatusLine("private-metadata-sentinel")],
            [json_response(repository_metadata()), api_error(500)],
            [json_response(repository_metadata()), URLError("private-metadata-sentinel")],
            [json_response(repository_metadata()), BadStatusLine("private-metadata-sentinel")],
        ):
            with self.subTest(response_count=len(responses)):
                with patch.object(MODULE, "urlopen", side_effect=responses):
                    try:
                        MODULE.fetch_latest_release("example")
                    except MODULE.ReleaseSyncError as exc:
                        diagnostic = "".join(traceback.format_exception(exc))
                    else:
                        self.fail("Lookup should fail closed")
                self.assertNotIn("private-metadata-sentinel", diagnostic)

    def test_404_means_no_official_release_after_confirmed_eligibility(self) -> None:
        with patch.object(MODULE, "urlopen", side_effect=[
            json_response(repository_metadata()), api_error(404),
        ]) as open_url:
            release = MODULE.fetch_latest_release("example")
        self.assertIsNone(release)
        self.assertEqual(MODULE.render_release_cell(release), "—")
        self.assertEqual(open_url.call_count, 2)
        self.assertTrue(
            open_url.call_args.args[0].full_url.endswith("/releases/latest")
        )

    def test_non_404_api_error_fails_closed(self) -> None:
        for error in (
            api_error(403), api_error(500),
            URLError("private-metadata-sentinel"),
            TimeoutError("private-metadata-sentinel"),
        ):
            with self.subTest(error=type(error).__name__):
                self.assert_sync_aborts([
                    json_response(repository_metadata(MODULE.SELECTED_REPOSITORIES[1])),
                    error,
                ])

    def test_release_status_flags_require_explicit_false(self) -> None:
        second = MODULE.SELECTED_REPOSITORIES[1]
        for flag in ("draft", "prerelease"):
            for value in (True, None, 0, 1, "false", "", [], {}):
                with self.subTest(flag=flag, value=value):
                    release = release_metadata(second)
                    release[flag] = value
                    self.assert_sync_aborts([
                        json_response(repository_metadata(second)),
                        json_response(release),
                    ])
            with self.subTest(flag=flag, missing=True):
                release = release_metadata(second)
                del release[flag]
                self.assert_sync_aborts([
                    json_response(repository_metadata(second)),
                    json_response(release),
                ])

    def test_malformed_release_fails_closed(self) -> None:
        for payload in (None, [], "private-metadata-sentinel", {}, False):
            with self.subTest(payload=payload):
                self.assert_sync_aborts([
                    json_response(repository_metadata(MODULE.SELECTED_REPOSITORIES[1])),
                    json_response(payload),
                ])
        for raw in (b"{private-metadata-sentinel", b"\xff"):
            with self.subTest(raw=raw):
                self.assert_sync_aborts([
                    json_response(repository_metadata(MODULE.SELECTED_REPOSITORIES[1])),
                    io.BytesIO(raw),
                ])

    def test_main_verifies_each_repository_and_preserves_bilingual_rows(self) -> None:
        with TemporaryDirectory() as directory:
            paths = {
                "en": Path(directory) / "README.md",
                "it": Path(directory) / "README.it.md",
            }
            for locale, path in paths.items():
                path.write_text(f"{locale}\n{profile_fixture()}", encoding="utf-8")
            no_release = "giadaware-ui-components"
            responses = []
            expected_urls = []
            expected_rows = []
            for repository in MODULE.SELECTED_REPOSITORIES:
                base = f"https://api.github.com/repos/gcomneno/{repository}"
                expected_urls.extend((base, f"{base}/releases/latest"))
                responses.append(json_response(repository_metadata(repository)))
                if repository == no_release:
                    responses.append(api_error(404))
                    cell = "—"
                else:
                    responses.append(json_response(release_metadata(repository)))
                    cell = (
                        f"[v2.0.0](https://github.com/gcomneno/{repository}"
                        "/releases/tag/v2.0.0)"
                    )
                expected_rows.append(
                    f"| [{repository}](https://github.com/gcomneno/{repository}) "
                    f"| {cell} | Description | Signal |"
                )
            with (
                patch.object(MODULE, "README_PATHS", paths),
                patch.object(MODULE, "urlopen", side_effect=responses) as open_url,
                redirect_stdout(io.StringIO()),
            ):
                self.assertEqual(MODULE.main(), 0)
            self.assertEqual(
                [call.args[0].full_url for call in open_url.call_args_list],
                expected_urls,
            )
            for locale, path in paths.items():
                self.assertEqual(
                    path.read_text(encoding="utf-8"),
                    f"{locale}\n" + "\n".join(expected_rows) + "\n",
                )


class ReleaseRenderingTests(unittest.TestCase):
    def test_no_release_renders_dash(self) -> None:
        self.assertEqual(MODULE.render_release_cell(None), "—")

    def test_replaces_only_release_cell(self) -> None:
        original = (
            "| [Example](https://github.com/gcomneno/example) | old | "
            "Description | Signal |\n"
        )
        current = MODULE.OfficialRelease(
            tag_name="v2.0.0",
            html_url=(
                "https://github.com/gcomneno/example/releases/tag/v2.0.0"
            ),
        )
        updated = MODULE.replace_release_cell(
            original,
            "example",
            current,
            source="README.md",
        )
        self.assertEqual(
            updated,
            "| [Example](https://github.com/gcomneno/example) | "
            "[v2.0.0](https://github.com/gcomneno/example/releases/tag/v2.0.0) "
            "| Description | Signal |\n",
        )

    def test_missing_row_fails(self) -> None:
        with self.assertRaises(MODULE.ReleaseSyncError):
            MODULE.replace_release_cell(
                "No table here\n",
                "example",
                None,
                source="README.md",
            )

    def test_duplicate_row_fails(self) -> None:
        row = (
            "| [Example](https://github.com/gcomneno/example) | old | "
            "Description | Signal |\n"
        )
        with self.assertRaises(MODULE.ReleaseSyncError):
            MODULE.replace_release_cell(
                row + row,
                "example",
                None,
                source="README.md",
            )


class AtomicBilingualTests(unittest.TestCase):
    def test_main_propagates_bilingual_write_failures(self) -> None:
        for failure in ("staging", "replacement", "rollback"):
            with self.subTest(failure=failure), TemporaryDirectory() as directory:
                root = Path(directory)
                paths = {"en": root / "README.md", "it": root / "README.it.md"}
                for path in paths.values():
                    path.write_text(profile_fixture(), encoding="utf-8")
                originals = {path: path.read_bytes() for path in paths.values()}
                real_replace = writer.os.replace

                def replace(source, destination):
                    if destination == paths["it"] or (
                        failure == "rollback" and source.suffix == ".restore"
                    ):
                        raise OSError("injected replacement failure")
                    real_replace(source, destination)

                stdout, stderr = io.StringIO(), io.StringIO()
                with (
                    patch.object(MODULE, "README_PATHS", paths),
                    patch.object(MODULE, "fetch_latest_release", return_value=None),
                    patch.object(writer.os, "replace", side_effect=replace),
                    patch.object(
                        writer.os, "fsync",
                        side_effect=OSError("staging failure") if failure == "staging" else None,
                    ),
                    redirect_stdout(stdout), redirect_stderr(stderr),
                ):
                    self.assertEqual(MODULE.main(), 1)
                self.assertNotIn("Synchronized", stdout.getvalue())
                self.assertNotIn("already up to date", stdout.getvalue())
                self.assertIn("Release sync aborted", stderr.getvalue())
                if failure == "rollback":
                    self.assertIn("Recovery required", stderr.getvalue())
                    self.assertNotIn("READMEs left unchanged", stderr.getvalue())
                    backups = list(root.glob(".*.original"))
                    self.assertEqual(len(backups), 2)
                    for path, data in originals.items():
                        backup = next(root.glob(f".{path.name}.*.original"))
                        self.assertEqual(backup.read_bytes(), data)
                        self.assertIn(str(backup), stderr.getvalue())
                else:
                    for path, data in originals.items():
                        self.assertEqual(path.read_bytes(), data)
                    self.assertEqual(list(root.glob(".*")), [])

    def test_main_validation_failure_never_calls_writer(self) -> None:
        with TemporaryDirectory() as directory:
            paths = {
                "en": Path(directory) / "README.md",
                "it": Path(directory) / "README.it.md",
            }
            paths["en"].write_text(profile_fixture(), encoding="utf-8")
            paths["it"].write_text(profile_fixture(omit="gyte"), encoding="utf-8")
            with (
                patch.object(MODULE, "README_PATHS", paths),
                patch.object(MODULE, "fetch_latest_release", return_value=None),
                patch.object(MODULE, "write_bilingual") as write,
                redirect_stderr(io.StringIO()),
            ):
                self.assertEqual(MODULE.main(), 1)
                write.assert_not_called()

    def test_edit_after_rendering_is_not_overwritten(self) -> None:
        with TemporaryDirectory() as directory:
            paths = {
                "en": Path(directory) / "README.md",
                "it": Path(directory) / "README.it.md",
            }
            for path in paths.values():
                path.write_text(profile_fixture(), encoding="utf-8")

            def edit_then_write(originals, outputs):
                paths["it"].write_bytes(b"Concurrent edit\n")
                return writer.write_bilingual(originals, outputs)

            with (
                patch.object(MODULE, "README_PATHS", paths),
                patch.object(MODULE, "fetch_latest_release", return_value=None),
                patch.object(MODULE, "write_bilingual", side_effect=edit_then_write),
                redirect_stderr(io.StringIO()),
            ):
                self.assertEqual(MODULE.main(), 1)
            self.assertEqual(paths["it"].read_bytes(), b"Concurrent edit\n")
            self.assertEqual(paths["en"].read_text(encoding="utf-8"), profile_fixture())

    def test_structure_failure_prevents_partial_write(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            en = root / "README.md"
            it = root / "README.it.md"
            en_original = profile_fixture()
            it_original = profile_fixture(omit="atelier-kit")
            en.write_text(en_original, encoding="utf-8")
            it.write_text(it_original, encoding="utf-8")
            paths = {"en": en, "it": it}
            releases = {
                repository: None
                for repository in MODULE.SELECTED_REPOSITORIES
            }

            with self.assertRaises(MODULE.ReleaseSyncError):
                MODULE.build_updated_readmes(releases, paths)

            self.assertEqual(en.read_text(encoding="utf-8"), en_original)
            self.assertEqual(it.read_text(encoding="utf-8"), it_original)

    def test_main_updates_both_languages_after_complete_lookup(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            paths = {
                "en": root / "README.md",
                "it": root / "README.it.md",
            }
            for path in paths.values():
                path.write_text(profile_fixture(), encoding="utf-8")

            def lookup(repository: str):
                if repository == "giadaware-ui-components":
                    return None
                return MODULE.OfficialRelease(
                    tag_name="v9.9.9",
                    html_url=(
                        f"https://github.com/gcomneno/{repository}"
                        "/releases/tag/v9.9.9"
                    ),
                )

            with (
                patch.object(MODULE, "README_PATHS", paths),
                patch.object(
                    MODULE,
                    "fetch_latest_release",
                    side_effect=lookup,
                ),
            ):
                self.assertEqual(MODULE.main(), 0)

            for path in paths.values():
                content = path.read_text(encoding="utf-8")
                self.assertIn(
                    "[v9.9.9](https://github.com/gcomneno/lele-manager"
                    "/releases/tag/v9.9.9)",
                    content,
                )

    def test_api_failure_prevents_all_writes(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            paths = {
                "en": root / "README.md",
                "it": root / "README.it.md",
            }
            original = profile_fixture()
            for path in paths.values():
                path.write_text(original, encoding="utf-8")

            def lookup(repository: str):
                if repository == "gyte":
                    raise MODULE.ReleaseSyncError("boom")
                return None

            with (
                patch.object(MODULE, "README_PATHS", paths),
                patch.object(
                    MODULE,
                    "fetch_latest_release",
                    side_effect=lookup,
                ),
            ):
                self.assertEqual(MODULE.main(), 1)

            for path in paths.values():
                self.assertEqual(
                    path.read_text(encoding="utf-8"),
                    original,
                )


if __name__ == "__main__":
    unittest.main()
