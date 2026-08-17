from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.error import HTTPError
from unittest.mock import patch

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


class ReleaseLookupTests(unittest.TestCase):
    def test_404_means_no_official_release(self) -> None:
        error = HTTPError(
            "https://example.test",
            404,
            "Not Found",
            hdrs=None,
            fp=None,
        )
        with patch.object(MODULE, "urlopen", side_effect=error):
            self.assertIsNone(MODULE.fetch_latest_release("example"))

    def test_non_404_api_error_fails_closed(self) -> None:
        error = HTTPError(
            "https://example.test",
            500,
            "Server Error",
            hdrs=None,
            fp=None,
        )
        with patch.object(MODULE, "urlopen", side_effect=error):
            with self.assertRaises(MODULE.ReleaseSyncError):
                MODULE.fetch_latest_release("example")


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
