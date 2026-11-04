from __future__ import annotations

import importlib.util
import io
import json
import sys
import unittest
from copy import deepcopy
from contextlib import redirect_stderr, redirect_stdout
from datetime import datetime, timedelta, timezone
from http.client import IncompleteRead, RemoteDisconnected
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError, URLError

from scripts import bilingual_write as writer


SCRIPT_PATH = (
    Path(__file__).parents[1]
    / "scripts"
    / "update_latest_updates.py"
)
SPEC = importlib.util.spec_from_file_location(
    "update_latest_updates",
    SCRIPT_PATH,
)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def repository(**overrides) -> dict:
    return {
        "full_name": "gcomneno/atelier-kit",
        "owner": {"login": "gcomneno"},
        "private": False, "archived": False, "disabled": False,
        "pushed_at": datetime.now(timezone.utc).isoformat(),
        **overrides,
    }


def release(**overrides) -> dict:
    return {
        "draft": False, "prerelease": False,
        "published_at": datetime.now(timezone.utc).isoformat(),
        "tag_name": "v1.0.0", "name": None,
        "html_url": "https://github.com/gcomneno/atelier-kit/releases/tag/v1.0.0",
        **overrides,
    }


def commit_data() -> dict:
    return {
        "author": {"login": "gcomneno"},
        "committer": {"login": "gcomneno"},
        "html_url": "https://github.com/gcomneno/atelier-kit/commit/abc",
        "commit": {
            "message": "feat: add public capability",
            "committer": {"date": datetime.now(timezone.utc).isoformat()},
        },
    }


class IsolatedApiTests(unittest.TestCase):
    def setUp(self) -> None:
        failure = patch.object(MODULE, "API_HAD_FAILURE", False)
        failure.start()
        self.addCleanup(failure.stop)


def item(
    *,
    hour: int,
    kind: str,
    text: str,
    url: str,
    priority: int | None = None,
    repo: str = "example",
) -> MODULE.UpdateItem:
    return MODULE.UpdateItem(
        date=datetime(
            2026,
            8,
            2,
            hour,
            0,
            tzinfo=timezone.utc,
        ),
        repo=repo,
        kind=kind,
        text=text,
        url=url,
        priority=(
            MODULE.COMMIT_PRIORITY_BY_KIND[kind]
            if priority is None
            else priority
        ),
    )


class RepositoryEligibilityPolicyTests(IsolatedApiTests):
    def test_repository_policy_is_positive_and_fail_closed(self) -> None:
        self.assertIn(
            "gcomneno/atelier-kit",
            MODULE.ALLOWED_REPOSITORIES,
        )
        self.assertIn(
            "gcomneno/vscode-bitbake",
            MODULE.ALLOWED_REPOSITORIES,
        )
        self.assertIn(
            "gcomneno/craft-parts",
            MODULE.ALLOWED_REPOSITORIES,
        )
        self.assertIn(
            "gcomneno/gyte-ai-learning-pipeline",
            MODULE.CURATED_REPOSITORIES,
        )
        self.assertIn(
            "gcomneno/giadaware-ai",
            MODULE.CURATED_REPOSITORIES,
        )
        self.assertNotIn(
            "gcomneno/grocery-deal-intelligence",
            MODULE.CURATED_REPOSITORIES,
        )
        self.assertNotIn(
            "gcomneno/semantic-mail-archivist",
            MODULE.CURATED_REPOSITORIES,
        )
        self.assertIn(
            "gcomneno/system-log-dynamics",
            MODULE.CURATED_REPOSITORIES,
        )
        self.assertIn(
            "gcomneno/bmaptool",
            MODULE.UPSTREAM_WORK_REPOSITORIES,
        )
        self.assertIn(
            "gcomneno/tree-sitter-bitbake",
            MODULE.UPSTREAM_WORK_REPOSITORIES,
        )
        self.assertNotIn(
            "gcomneno/gyte-study-tools",
            MODULE.ALLOWED_REPOSITORIES,
        )
        self.assertNotIn(
            MODULE.PROFILE_REPO,
            MODULE.ALLOWED_REPOSITORIES,
        )
        self.assertNotIn(
            "gcomneno/unlisted-public-repository",
            MODULE.ALLOWED_REPOSITORIES,
        )

    def test_discovery_skips_unlisted_public_repositories(self) -> None:
        payload = [
            {
                "full_name": "gcomneno/unlisted-public-repository",
                "owner": {"login": "gcomneno"},
                "private": False,
                "archived": False,
                "disabled": False,
                "pushed_at": datetime.now(timezone.utc).isoformat(),
            },
            {
                "full_name": "gcomneno/atelier-kit",
                "owner": {"login": "gcomneno"},
                "private": False,
                "archived": False,
                "disabled": False,
                "pushed_at": datetime.now(timezone.utc).isoformat(),
            },
        ]

        with patch.object(
            MODULE,
            "github_get_json",
            side_effect=[payload, []],
        ):
            self.assertEqual(
                MODULE.discover_public_repositories(),
                ["gcomneno/atelier-kit"],
            )

    def test_eligibility_fields_require_explicit_booleans(self) -> None:
        missing = object()
        for field in ("private", "archived", "disabled"):
            for value in (missing, None, 0, 1, "false", "true", [], {}):
                with self.subTest(field=field, value=value):
                    repo = repository()
                    if value is missing:
                        del repo[field]
                    else:
                        repo[field] = value
                    MODULE.API_HAD_FAILURE = False
                    with (
                        patch.object(MODULE, "github_get_json", return_value=[repo]),
                        redirect_stderr(io.StringIO()),
                    ):
                        self.assertEqual(MODULE.discover_public_repositories(), [])
                    self.assertTrue(MODULE.API_HAD_FAILURE)

    def test_explicit_ineligible_repositories_are_successfully_excluded(self) -> None:
        for overrides in (
            {"private": True}, {"archived": True}, {"disabled": True},
            {"full_name": MODULE.PROFILE_REPO},
            {"full_name": "other/atelier-kit", "owner": {"login": "other"}},
            {"pushed_at": (datetime.now(timezone.utc) - timedelta(
                days=MODULE.LOOKBACK_DAYS + 1
            )).isoformat()},
            {"pushed_at": None},
        ):
            with self.subTest(overrides=overrides), patch.object(
                MODULE, "github_get_json", return_value=[repository(**overrides)]
            ):
                self.assertEqual(MODULE.discover_public_repositories(), [])
                self.assertFalse(MODULE.API_HAD_FAILURE)

    def test_empty_discovery_page_is_success(self) -> None:
        with patch.object(MODULE, "github_get_json", return_value=[]):
            self.assertEqual(MODULE.discover_public_repositories(), [])
        self.assertFalse(MODULE.API_HAD_FAILURE)

    def test_malformed_discovery_pages_and_records_are_failures(self) -> None:
        for payload in (
            None, {}, {"message": "synthetic-private-payload"}, "", 0, False,
            [None], [[]], ["synthetic-private-payload"], [{}],
            [repository(owner=None)], [repository(owner={})],
            [repository(owner={"login": "other"})],
            [repository(full_name=123)], [repository(full_name="gcomneno/")],
            [repository(full_name="gcomneno/atelier-kit/extra")],
        ):
            with self.subTest(payload=payload):
                MODULE.API_HAD_FAILURE = False
                diagnostic = io.StringIO()
                with (
                    patch.object(MODULE, "github_get_json", return_value=payload),
                    redirect_stderr(diagnostic),
                ):
                    self.assertEqual(MODULE.discover_public_repositories(), [])
                self.assertTrue(MODULE.API_HAD_FAILURE)
                self.assertNotIn("synthetic-private-payload", diagnostic.getvalue())

    def test_discovery_failure_discards_previously_valid_page(self) -> None:
        page = [repository()] + [repository(
            full_name="gcomneno/unlisted-public-repository"
        ) for _ in range(99)]
        for failed_page in (None, {}, [None], [repository(private=None)]):
            with self.subTest(failed_page=failed_page):
                MODULE.API_HAD_FAILURE = False
                with (
                    patch.object(MODULE, "github_get_json", side_effect=[
                        page, failed_page
                    ]) as get,
                    redirect_stderr(io.StringIO()),
                ):
                    self.assertEqual(MODULE.discover_public_repositories(), [])
                self.assertEqual(get.call_count, 2)
                self.assertTrue(MODULE.API_HAD_FAILURE)

    def test_unknown_or_malformed_push_time_is_a_discovery_failure(self) -> None:
        missing = object()
        for value in (missing, "invalid", "", 123, False, [], {},
                      "2026-11-04", "2026-11-04T12:00:00"):
            with self.subTest(value=value):
                repo = repository(pushed_at=value)
                if value is missing:
                    del repo["pushed_at"]
                MODULE.API_HAD_FAILURE = False
                with (
                    patch.object(MODULE, "github_get_json", return_value=[repo]),
                    redirect_stderr(io.StringIO()),
                ):
                    self.assertEqual(MODULE.discover_public_repositories(), [])
                self.assertTrue(MODULE.API_HAD_FAILURE)


class ApiFailureTests(IsolatedApiTests):
    def test_http_transport_timeout_decoding_and_json_failures_are_private(self) -> None:
        secret = "synthetic-private-sentinel"
        url = f"https://api.github.com/{secret}"
        failures = (
            (HTTPError(url, 503, secret, {}, None), "HTTP failure (status 503)"),
            (URLError(secret), "transport or timeout"),
            (TimeoutError(secret), "transport or timeout"),
            (ConnectionResetError(secret), "transport or timeout"),
            (RemoteDisconnected(secret), "transport or timeout"),
            (IncompleteRead(secret.encode()), "transport or timeout"),
            (UnicodeDecodeError("utf-8", b"\xff", 0, 1, secret), "decoding failure"),
            (json.JSONDecodeError(secret, secret, 0), "JSON decoding failure"),
        )
        for failure, expected in failures:
            for phase in ("open", "read"):
                with self.subTest(failure=type(failure).__name__, phase=phase):
                    MODULE.API_HAD_FAILURE = False
                    response = MagicMock()
                    response.__enter__.return_value = response
                    if phase == "read":
                        response.read.side_effect = failure
                    diagnostic = io.StringIO()
                    with (
                        patch.object(MODULE, "urlopen", return_value=response,
                                     side_effect=failure if phase == "open" else None),
                        patch.dict(MODULE.os.environ, {
                            MODULE.PROFILE_BLOCK_TERMS_ENV: secret,
                            "GH_TOKEN": secret,
                        }),
                        redirect_stderr(diagnostic),
                    ):
                        self.assertIsNone(MODULE.github_get_json(url))
                    self.assertTrue(MODULE.API_HAD_FAILURE)
                    self.assertIn(expected, diagnostic.getvalue())
                    self.assertNotIn(secret, diagnostic.getvalue())
                    self.assertNotIn(url, diagnostic.getvalue())

    def test_invalid_response_bytes_are_reported(self) -> None:
        for body, expected in ((b"\xff", "decoding failure"),
                               (b"not-json", "JSON decoding failure")):
            with self.subTest(body=body):
                MODULE.API_HAD_FAILURE = False
                response = MagicMock()
                response.__enter__.return_value.read.return_value = body
                diagnostic = io.StringIO()
                with (
                    patch.object(MODULE, "urlopen", return_value=response),
                    redirect_stderr(diagnostic),
                ):
                    self.assertIsNone(MODULE.github_get_json("https://api.github.com/"))
                self.assertTrue(MODULE.API_HAD_FAILURE)
                self.assertIn(expected, diagnostic.getvalue())

    def test_activity_pages_distinguish_empty_from_malformed(self) -> None:
        for fetch in (MODULE.fetch_repo_releases, MODULE.fetch_repo_commit_updates):
            for payload in ([], None, {}, "invalid", [None], [{}]):
                with self.subTest(fetch=fetch.__name__, payload=payload):
                    MODULE.API_HAD_FAILURE = False
                    with (
                        patch.object(MODULE, "github_get_json", return_value=payload),
                        redirect_stderr(io.StringIO()),
                    ):
                        self.assertEqual(fetch("gcomneno/atelier-kit"), [])
                    self.assertEqual(MODULE.API_HAD_FAILURE, payload != [])

    def test_activity_page_failure_discards_partial_items(self) -> None:
        for fetch, record in (
            (MODULE.fetch_repo_releases, release()),
            (MODULE.fetch_repo_commit_updates, commit_data()),
        ):
            with self.subTest(fetch=fetch.__name__):
                MODULE.API_HAD_FAILURE = False
                with (
                    patch.object(MODULE, "github_get_json", side_effect=[
                        [record] * 100, {}
                    ]) as get,
                    redirect_stderr(io.StringIO()),
                ):
                    self.assertEqual(fetch("gcomneno/atelier-kit"), [])
                self.assertEqual(get.call_count, 2)
                self.assertTrue(MODULE.API_HAD_FAILURE)

    def test_malformed_commit_metadata_is_a_failure(self) -> None:
        for key_path, value in (
            (("commit",), None), (("commit", "message"), 42),
            (("commit", "committer"), []),
            (("commit", "committer", "date"), "invalid"),
            (("commit", "committer", "date"), "2026-11-04"),
            (("html_url",), None), (("author",), "invalid"),
        ):
            with self.subTest(key_path=key_path, value=value):
                MODULE.API_HAD_FAILURE = False
                commit = deepcopy(commit_data())
                target = commit
                for key in key_path[:-1]:
                    target = target[key]
                target[key_path[-1]] = value
                with (
                    patch.object(MODULE, "github_get_json", return_value=[commit]),
                    redirect_stderr(io.StringIO()),
                ):
                    self.assertEqual(MODULE.fetch_repo_commit_updates(
                        "gcomneno/atelier-kit"
                    ), [])
                self.assertTrue(MODULE.API_HAD_FAILURE)

    def test_malformed_release_metadata_is_a_failure(self) -> None:
        for overrides in (
            {"draft": None}, {"draft": 0}, {"tag_name": None}, {"name": []},
            {"published_at": "invalid"}, {"published_at": None},
            {"published_at": "2026-11-04"}, {"html_url": False},
        ):
            with self.subTest(overrides=overrides):
                MODULE.API_HAD_FAILURE = False
                with (
                    patch.object(MODULE, "github_get_json", return_value=[
                        release(**overrides)
                    ]), redirect_stderr(io.StringIO()),
                ):
                    self.assertEqual(MODULE.fetch_repo_releases("gcomneno/atelier-kit"), [])
                self.assertTrue(MODULE.API_HAD_FAILURE)

    def test_prereleases_remain_latest_updates_activity(self) -> None:
        with patch.object(MODULE, "github_get_json", return_value=[
            release(prerelease=True, tag_name="v2.0.0-rc.1"), release(draft=True),
        ]):
            items = MODULE.fetch_repo_releases("gcomneno/atelier-kit")
        self.assertEqual([entry.text for entry in items], ["v2.0.0-rc.1"])
        self.assertFalse(MODULE.API_HAD_FAILURE)


class UpdateMessageTests(unittest.TestCase):
    def test_parses_explicit_docs_tag(
        self,
    ) -> None:
        self.assertEqual(
            MODULE.parse_update_message(
                "docs(api): explain the contract"
            ),
            ("docs", "explain the contract"),
        )

    def test_parses_explicit_update_tag_case_insensitively(
        self,
    ) -> None:
        self.assertEqual(
            MODULE.parse_update_message(
                "UPDATE: Refresh profile"
            ),
            ("update", "Refresh profile"),
        )

    def test_excludes_empty_commit_message(self) -> None:
        self.assertIsNone(
            MODULE.parse_update_message("")
        )

    def test_parses_conventional_feature(
        self,
    ) -> None:
        self.assertEqual(
            MODULE.parse_update_message(
                "feat(cli): add sortable reports"
            ),
            ("feature", "add sortable reports"),
        )

    def test_parses_conventional_fix(
        self,
    ) -> None:
        self.assertEqual(
            MODULE.parse_update_message(
                "fix: reject malformed input"
            ),
            ("fix", "reject malformed input"),
        )

    def test_excludes_plain_placeholder_messages(self) -> None:
        for message in (
            "noop",
            "TMP",
            "temp",
            "probe",
            "wip",
            "debug",
            "x",
            "X",
            "7",
            "!",
            "??",
        ):
            with self.subTest(message=message):
                self.assertIsNone(
                    MODULE.parse_update_message(message)
                )

    def test_excludes_tagged_low_information_messages(self) -> None:
        for message in (
            "docs: x",
            "feat: x",
            "fix(ui): !",
            "UPDATE: ??",
        ):
            with self.subTest(message=message):
                self.assertIsNone(
                    MODULE.parse_update_message(message)
                )

    def test_runtime_block_terms_are_private_editorial_filter(self) -> None:
        with patch.dict(
            MODULE.os.environ,
            {
                MODULE.PROFILE_BLOCK_TERMS_ENV:
                    "Client Alpha,internal showcase"
            },
            clear=False,
        ):
            self.assertIsNone(
                MODULE.parse_update_message(
                    "docs: document Client Alpha operator runbook"
                )
            )
            self.assertIsNone(
                MODULE.parse_update_message(
                    "Add INTERNAL SHOWCASE recovery notes"
                )
            )
            self.assertEqual(
                MODULE.parse_update_message(
                    "fix: preserve unrelated public behavior"
                ),
                ("fix", "preserve unrelated public behavior"),
            )

    def test_accepts_plain_meaningful_commit(
        self,
    ) -> None:
        self.assertEqual(
            MODULE.parse_update_message(
                "Add sortable coverage hit reports"
            ),
            (
                "development",
                "Add sortable coverage hit reports",
            ),
        )

    def test_excludes_maintenance_commit_types(
        self,
    ) -> None:
        messages = (
            "chore: update generated files",
            "chore(deps): update dependency",
            "ci: refresh workflow",
            "build: refresh package metadata",
            "style: reformat source",
            "test: adjust fixture",
            "deps: bump library",
            "maintenance: clean repository",
        )

        for message in messages:
            with self.subTest(message=message):
                self.assertIsNone(
                    MODULE.parse_update_message(
                        message
                    )
                )

    def test_excludes_merge_bump_and_automatic_updates(
        self,
    ) -> None:
        messages = (
            "Merge branch 'main'",
            "Bump actions/checkout from 4 to 5",
            "Automatic update of generated references",
            "Auto update references",
        )

        for message in messages:
            with self.subTest(message=message):
                self.assertIsNone(
                    MODULE.parse_update_message(
                        message
                    )
                )

    def test_keeps_chore_release_as_release(
        self,
    ) -> None:
        self.assertEqual(
            MODULE.parse_update_message(
                "chore(release): v2.0.0"
            ),
            ("release", "v2.0.0"),
        )
        self.assertEqual(
            MODULE.parse_update_message(
                "chore: release v2.0.0"
            ),
            ("release", "v2.0.0"),
        )


class UpdateRenderingTests(unittest.TestCase):
    def test_renders_development_label(
        self,
    ) -> None:
        update = item(
            hour=10,
            kind="development",
            text="Add sortable reports",
            url="https://example.test/commit/123",
        )

        self.assertEqual(
            MODULE.render_update_item(update),
            (
                "- **2026-08-02** · `example` · "
                "**Development:** "
                "[Add sortable reports]"
                "(https://example.test/commit/123)"
            ),
        )


class UpdateDeduplicationTests(unittest.TestCase):
    def test_preserves_multiple_meaningful_commits_same_day(
        self,
    ) -> None:
        feature = item(
            hour=10,
            kind="feature",
            text="feature",
            url="https://example.test/feature",
        )
        docs = item(
            hour=9,
            kind="docs",
            text="documentation",
            url="https://example.test/docs",
        )

        self.assertEqual(
            MODULE.dedupe_updates(
                [docs, feature]
            ),
            [feature, docs],
        )

    def test_removes_exact_url_duplicates(
        self,
    ) -> None:
        older = item(
            hour=8,
            kind="development",
            text="older",
            url="https://example.test/same",
        )
        newer = item(
            hour=10,
            kind="development",
            text="newer",
            url="https://example.test/same",
        )

        self.assertEqual(
            MODULE.dedupe_updates(
                [older, newer]
            ),
            [newer],
        )

    def test_collapses_same_day_repeated_editorial_title(self) -> None:
        older = item(
            hour=8,
            kind="development",
            text="studio: update hero banner",
            url="https://example.test/older",
        )
        newer = item(
            hour=10,
            kind="development",
            text="studio: update hero banner",
            url="https://example.test/newer",
        )

        self.assertEqual(
            MODULE.dedupe_updates([older, newer]),
            [newer],
        )

    def test_keeps_same_title_on_different_days(self) -> None:
        older = MODULE.UpdateItem(
            date=datetime(
                2026,
                8,
                1,
                10,
                0,
                tzinfo=timezone.utc,
            ),
            repo="example",
            kind="development",
            text="studio: update hero banner",
            url="https://example.test/day-1",
            priority=MODULE.COMMIT_PRIORITY_BY_KIND[
                "development"
            ],
        )
        newer = MODULE.UpdateItem(
            date=datetime(
                2026,
                8,
                2,
                10,
                0,
                tzinfo=timezone.utc,
            ),
            repo="example",
            kind="development",
            text="studio: update hero banner",
            url="https://example.test/day-2",
            priority=MODULE.COMMIT_PRIORITY_BY_KIND[
                "development"
            ],
        )

        self.assertEqual(
            MODULE.dedupe_updates([older, newer]),
            [newer, older],
        )

    def test_api_release_replaces_release_commit_only(
        self,
    ) -> None:
        api_release = item(
            hour=11,
            kind="release",
            text="v1.0.0",
            url="https://example.test/release",
            priority=MODULE.PRIORITY_RELEASE_API,
        )
        release_commit = item(
            hour=10,
            kind="release",
            text="v1.0.0",
            url="https://example.test/release-commit",
        )
        feature = item(
            hour=9,
            kind="feature",
            text="new feature",
            url="https://example.test/feature",
        )

        self.assertEqual(
            MODULE.dedupe_updates(
                [
                    release_commit,
                    feature,
                    api_release,
                ]
            ),
            [api_release, feature],
        )


class UpdateRenderLimitTests(unittest.TestCase):
    def test_keeps_twenty_items_with_repository_cap(
        self,
    ) -> None:
        updates = [
            MODULE.UpdateItem(
                date=datetime(
                    2026,
                    8,
                    2,
                    10,
                    0,
                    tzinfo=timezone.utc,
                ),
                repo=f"example-{index // 3}",
                kind="development",
                text=f"update-{index}",
                url=(
                    "https://example.test/commit/"
                    f"{index}"
                ),
                priority=(
                    MODULE.COMMIT_PRIORITY_BY_KIND[
                        "development"
                    ]
                ),
            )
            for index in range(105)
        ]

        rendered = MODULE.render_updates(updates)

        self.assertEqual(
            rendered.count("- **"),
            MODULE.MAX_RENDERED_ITEMS,
        )
        self.assertIn(
            "[update-0]",
            rendered,
        )
        self.assertIn(
            "[update-19]",
            rendered,
        )
        self.assertNotIn(
            "[update-20]",
            rendered,
        )
        self.assertIn(
            "85 additional update(s) not displayed",
            rendered,
        )
        self.assertIn(
            "<summary>More recent meaningful updates</summary>",
            rendered,
        )
        self.assertIn(
            "<details>",
            rendered,
        )
        self.assertIn(
            "</details>",
            rendered,
        )

    def test_caps_updates_per_repository(self) -> None:
        updates = [
            item(
                hour=10 - index,
                kind="development",
                text=f"same-repo-{index}",
                url=f"https://example.test/{index}",
            )
            for index in range(6)
        ]
        rendered = MODULE.render_updates(updates)
        self.assertEqual(rendered.count("- **"), 3)
        self.assertIn("[same-repo-2]", rendered)
        self.assertNotIn("[same-repo-3]", rendered)

    def test_does_not_show_omission_note_below_limit(
        self,
    ) -> None:
        updates = [
            item(
                hour=10,
                kind="development",
                text="first",
                url="https://example.test/first",
            ),
            item(
                hour=9,
                kind="feature",
                text="second",
                url="https://example.test/second",
            ),
        ]

        rendered = MODULE.render_updates(updates)

        self.assertNotIn(
            "older update(s) omitted",
            rendered,
        )


class LocalizedUpdateRenderingTests(unittest.TestCase):
    def test_renders_italian_label_without_translating_title(
        self,
    ) -> None:
        update = item(
            hour=10,
            kind="feature",
            text="Add stable public API",
            url="https://example.test/feature",
        )

        rendered = MODULE.render_update_item(
            update,
            locale="it",
        )

        self.assertIn(
            "**Funzionalità:**",
            rendered,
        )
        self.assertIn(
            "[Add stable public API]",
            rendered,
        )

    def test_uses_italian_fallback(
        self,
    ) -> None:
        self.assertEqual(
            MODULE.render_updates([], locale="it"),
            (
                "- Al momento non sono disponibili "
                "aggiornamenti automatici."
            ),
        )

    def test_renders_italian_more_updates_disclosure(
        self,
    ) -> None:
        updates = [
            item(
                hour=10 - index,
                kind="development",
                text=f"update-{index}",
                url=f"https://example.test/{index}",
                repo=f"example-{index}",
            )
            for index in range(5)
        ]

        rendered = MODULE.render_updates(
            updates,
            locale="it",
        )

        self.assertIn(
            "<summary>Altri aggiornamenti recenti e significativi</summary>",
            rendered,
        )
        self.assertIn(
            "<details>",
            rendered,
        )
        self.assertIn(
            "</details>",
            rendered,
        )
        self.assertIn(
            "**Sviluppo:**",
            rendered,
        )

    def test_rejects_unknown_locale(
        self,
    ) -> None:
        update = item(
            hour=10,
            kind="fix",
            text="Fix example",
            url="https://example.test/fix",
        )

        with self.assertRaises(ValueError):
            MODULE.render_update_item(
                update,
                locale="xx",
            )

    def test_tracks_both_profile_readmes(
        self,
    ) -> None:
        self.assertEqual(
            MODULE.README_PATHS,
            {
                "en": Path("README.md"),
                "it": Path("README.it.md"),
            },
        )


class BilingualMainIntegrationTests(unittest.TestCase):
    def test_failed_refreshes_preserve_both_files_and_return_failure(self) -> None:
        for payloads in (
            [{}],
            [[repository(private=None)]],
            [[repository()], {}],
            [[repository()], [release()], {"message": "synthetic-private-payload"}],
            [[repository()], [], [commit_data(), {}]],
        ):
            with self.subTest(payloads=payloads), TemporaryDirectory() as directory:
                paths = {"en": Path(directory) / "README.md",
                         "it": Path(directory) / "README.it.md"}
                for path in paths.values():
                    path.write_bytes(self.readme_fixture().replace("\n", "\r\n").encode())
                originals = {path: path.read_bytes() for path in paths.values()}
                diagnostic = io.StringIO()
                with (
                    patch.object(MODULE, "README_PATHS", paths),
                    patch.object(MODULE, "github_get_json", side_effect=payloads),
                    patch.object(MODULE, "write_bilingual") as write,
                    redirect_stderr(diagnostic), redirect_stdout(io.StringIO()),
                ):
                    self.assertEqual(MODULE.main(), 1)
                    write.assert_not_called()
                self.assertIn("READMEs left unchanged", diagnostic.getvalue())
                self.assertNotIn("synthetic-private-payload", diagnostic.getvalue())
                for path, original in originals.items():
                    self.assertEqual(path.read_bytes(), original)

    def test_wire_failures_return_failure_without_writes(self) -> None:
        for failure in (
            HTTPError("https://api.github.com/", 403, "private", {}, None),
            URLError("private"), TimeoutError("private"),
            json.JSONDecodeError("private", "private", 0),
            UnicodeDecodeError("utf-8", b"\xff", 0, 1, "private"),
        ):
            with self.subTest(failure=type(failure).__name__), TemporaryDirectory() as directory:
                paths = {"en": Path(directory) / "README.md",
                         "it": Path(directory) / "README.it.md"}
                for path in paths.values():
                    path.write_text(self.readme_fixture(), encoding="utf-8")
                originals = {path: path.read_bytes() for path in paths.values()}
                with (
                    patch.object(MODULE, "README_PATHS", paths),
                    patch.object(MODULE, "urlopen", side_effect=failure),
                    patch.object(MODULE, "write_bilingual") as write,
                    redirect_stderr(io.StringIO()),
                ):
                    self.assertEqual(MODULE.main(), 1)
                    write.assert_not_called()
                for path, original in originals.items():
                    self.assertEqual(path.read_bytes(), original)

    def test_failure_then_clean_empty_refresh_then_no_change(self) -> None:
        with TemporaryDirectory() as directory:
            paths = {"en": Path(directory) / "README.md",
                     "it": Path(directory) / "README.it.md"}
            for path in paths.values():
                path.write_text(self.readme_fixture(), encoding="utf-8")
            with (
                patch.object(MODULE, "README_PATHS", paths),
                patch.object(MODULE, "github_get_json", side_effect=[{}, [], []]),
                redirect_stderr(io.StringIO()), redirect_stdout(io.StringIO()) as stdout,
            ):
                self.assertEqual(MODULE.main(), 1)
                self.assertTrue(MODULE.API_HAD_FAILURE)
                self.assertEqual(MODULE.main(), 0)
                self.assertFalse(MODULE.API_HAD_FAILURE)
                after_empty = {path: path.read_bytes() for path in paths.values()}
                for locale, path in paths.items():
                    self.assertIn(MODULE.UI_BY_LOCALE[locale]["fallback"],
                                  path.read_text(encoding="utf-8"))
                self.assertEqual(MODULE.main(), 0)
                self.assertFalse(MODULE.API_HAD_FAILURE)
                self.assertIn("already up to date", stdout.getvalue())
                for path, original in after_empty.items():
                    self.assertEqual(path.read_bytes(), original)

    def test_main_propagates_bilingual_write_failures(self) -> None:
        for failure in ("staging", "replacement", "rollback"):
            with self.subTest(failure=failure), TemporaryDirectory() as directory:
                root = Path(directory)
                paths = {"en": root / "README.md", "it": root / "README.it.md"}
                for path in paths.values():
                    path.write_text(self.readme_fixture(), encoding="utf-8")
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
                    patch.object(MODULE, "collect_updates", return_value=[]),
                    patch.object(MODULE, "API_HAD_FAILURE", False),
                    patch.object(writer.os, "replace", side_effect=replace),
                    patch.object(
                        writer.os, "fsync",
                        side_effect=OSError("staging failure") if failure == "staging" else None,
                    ),
                    redirect_stdout(stdout), redirect_stderr(stderr),
                ):
                    self.assertEqual(MODULE.main(), 1)
                self.assertNotIn("fallback written", stdout.getvalue())
                self.assertNotIn("already up to date", stdout.getvalue())
                self.assertIn("Latest Updates aborted", stderr.getvalue())
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

    def test_second_readme_validation_failure_never_calls_writer(self) -> None:
        with TemporaryDirectory() as directory:
            paths = {
                "en": Path(directory) / "README.md",
                "it": Path(directory) / "README.it.md",
            }
            paths["en"].write_text(self.readme_fixture(), encoding="utf-8")
            paths["it"].write_text("Missing markers\n", encoding="utf-8")
            with (
                patch.object(MODULE, "README_PATHS", paths),
                patch.object(MODULE, "collect_updates", return_value=[]),
                patch.object(MODULE, "API_HAD_FAILURE", False),
                patch.object(MODULE, "write_bilingual") as write,
            ):
                with self.assertRaises(SystemExit):
                    MODULE.main()
                write.assert_not_called()
            self.assertEqual(
                paths["en"].read_text(encoding="utf-8"), self.readme_fixture()
            )

    def test_edit_after_rendering_is_not_overwritten(self) -> None:
        with TemporaryDirectory() as directory:
            paths = {
                "en": Path(directory) / "README.md",
                "it": Path(directory) / "README.it.md",
            }
            for path in paths.values():
                path.write_text(self.readme_fixture(), encoding="utf-8")

            def edit_then_write(originals, outputs):
                paths["it"].write_bytes(b"Concurrent edit\n")
                return writer.write_bilingual(originals, outputs)

            with (
                patch.object(MODULE, "README_PATHS", paths),
                patch.object(MODULE, "collect_updates", return_value=[]),
                patch.object(MODULE, "API_HAD_FAILURE", False),
                patch.object(MODULE, "write_bilingual", side_effect=edit_then_write),
                redirect_stderr(io.StringIO()),
            ):
                self.assertEqual(MODULE.main(), 1)
            self.assertEqual(paths["it"].read_bytes(), b"Concurrent edit\n")
            self.assertEqual(
                paths["en"].read_text(encoding="utf-8"), self.readme_fixture()
            )

    @staticmethod
    def readme_fixture() -> str:
        return (
            "Static introduction\n"
            "<!-- updates:start -->\n\n"
            "- Previous generated content\n\n"
            "<!-- updates:end -->\n"
            "Static conclusion\n"
        )

    def test_main_updates_both_profile_readmes(
        self,
    ) -> None:
        update = item(
            hour=10,
            kind="feature",
            text="Add stable public API",
            url="https://example.test/feature",
        )

        with TemporaryDirectory() as directory:
            root = Path(directory)
            paths = {
                "en": root / "README.md",
                "it": root / "README.it.md",
            }

            for path in paths.values():
                path.write_text(
                    self.readme_fixture(),
                    encoding="utf-8",
                )

            with (
                patch.object(
                    MODULE,
                    "README_PATHS",
                    paths,
                ),
                patch.object(
                    MODULE,
                    "collect_updates",
                    return_value=[update],
                ),
                patch.object(
                    MODULE,
                    "API_HAD_FAILURE",
                    False,
                ),
            ):
                result = MODULE.main()

            english = paths["en"].read_text(
                encoding="utf-8",
            )
            italian = paths["it"].read_text(
                encoding="utf-8",
            )

            self.assertEqual(result, 0)
            self.assertIn(
                "**Feature:**",
                english,
            )
            self.assertIn(
                "**Funzionalità:**",
                italian,
            )
            self.assertIn(
                "[Add stable public API]",
                english,
            )
            self.assertIn(
                "[Add stable public API]",
                italian,
            )
            self.assertNotIn(
                "Previous generated content",
                english,
            )
            self.assertNotIn(
                "Previous generated content",
                italian,
            )

    def test_main_writes_more_updates_disclosure(
        self,
    ) -> None:
        updates = [
            item(
                hour=10 - index,
                kind="development",
                text=f"update-{index}",
                url=f"https://example.test/{index}",
                repo=f"example-{index}",
            )
            for index in range(5)
        ]

        with TemporaryDirectory() as directory:
            root = Path(directory)
            paths = {
                "en": root / "README.md",
                "it": root / "README.it.md",
            }

            for path in paths.values():
                path.write_text(
                    self.readme_fixture(),
                    encoding="utf-8",
                )

            with (
                patch.object(
                    MODULE,
                    "README_PATHS",
                    paths,
                ),
                patch.object(
                    MODULE,
                    "collect_updates",
                    return_value=updates,
                ),
                patch.object(
                    MODULE,
                    "API_HAD_FAILURE",
                    False,
                ),
            ):
                result = MODULE.main()

            english = paths["en"].read_text(
                encoding="utf-8",
            )
            italian = paths["it"].read_text(
                encoding="utf-8",
            )

            self.assertEqual(result, 0)
            self.assertIn(
                "<summary>More recent meaningful updates</summary>",
                english,
            )
            self.assertIn(
                "<summary>Altri aggiornamenti recenti e significativi</summary>",
                italian,
            )

            for text in (english, italian):
                self.assertIn(
                    "<details>",
                    text,
                )
                self.assertIn(
                    "</details>",
                    text,
                )

    def test_missing_translation_prevents_partial_write(
        self,
    ) -> None:
        update = item(
            hour=10,
            kind="fix",
            text="Reject malformed input",
            url="https://example.test/fix",
        )

        with TemporaryDirectory() as directory:
            root = Path(directory)
            english_path = root / "README.md"
            italian_path = root / "README.it.md"
            original = self.readme_fixture()

            english_path.write_text(
                original,
                encoding="utf-8",
            )

            paths = {
                "en": english_path,
                "it": italian_path,
            }

            with (
                patch.object(
                    MODULE,
                    "README_PATHS",
                    paths,
                ),
                patch.object(
                    MODULE,
                    "collect_updates",
                    return_value=[update],
                ),
                patch.object(
                    MODULE,
                    "API_HAD_FAILURE",
                    False,
                ),
            ):
                with self.assertRaises(SystemExit):
                    MODULE.main()

            self.assertEqual(
                english_path.read_text(
                    encoding="utf-8",
                ),
                original,
            )

    def test_api_failure_leaves_both_readmes_unchanged(
        self,
    ) -> None:
        update = item(
            hour=10,
            kind="development",
            text="Add experiment",
            url="https://example.test/development",
        )

        def failed_collection():
            MODULE.record_api_failure("injected collection failure.")
            return [update]

        with TemporaryDirectory() as directory:
            root = Path(directory)
            paths = {
                "en": root / "README.md",
                "it": root / "README.it.md",
            }
            original = self.readme_fixture()

            for path in paths.values():
                path.write_text(
                    original,
                    encoding="utf-8",
                )

            with (
                patch.object(
                    MODULE,
                    "README_PATHS",
                    paths,
                ),
                patch.object(
                    MODULE,
                    "collect_updates",
                    side_effect=failed_collection,
                ),
                patch.object(
                    MODULE,
                    "API_HAD_FAILURE",
                    True,
                ),
            ):
                result = MODULE.main()

            self.assertEqual(result, 1)

            for path in paths.values():
                self.assertEqual(
                    path.read_text(
                        encoding="utf-8",
                    ),
                    original,
                )


if __name__ == "__main__":
    unittest.main()
