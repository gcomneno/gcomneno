from __future__ import annotations

import importlib.util
import io
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch


SCRIPTS_DIR = Path(__file__).parents[1] / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

SCRIPT_PATH = SCRIPTS_DIR / "update_latest_updates_public_activity.py"
SPEC = importlib.util.spec_from_file_location(
    "update_latest_updates_public_activity",
    SCRIPT_PATH,
)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class IsolatedApiTests(unittest.TestCase):
    def setUp(self) -> None:
        failure = patch.object(MODULE.core, "API_HAD_FAILURE", False)
        failure.start()
        self.addCleanup(failure.stop)


def push_event(
    *,
    repo: str = "gcomneno/vscode-bitbake",
    head: str = "abc123",
    before: str = "def456",
) -> dict:
    return {
        "type": "PushEvent",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "actor": {"login": "gcomneno", "id": 126195429},
        "repo": {"name": repo},
        "payload": {
            "ref": "refs/heads/contrib/issue-example",
            "head": head,
            "before": before,
        },
    }


def commit_obj(
    *,
    sha: str = "abc123",
    message: str = "feat: add branch capability",
    login: str = "gcomneno",
) -> dict:
    return {
        "sha": sha,
        "html_url": (
            "https://github.com/gcomneno/vscode-bitbake/commit/"
            f"{sha}"
        ),
        "author": {"login": login},
        "committer": {"login": login},
        "commit": {
            "message": message,
            "committer": {
                "date": datetime.now(timezone.utc).isoformat(),
            },
        },
    }


class PublicPushActivityTests(IsolatedApiTests):
    def test_malformed_push_metadata_fails_before_any_commit_request(self) -> None:
        for overrides in ({"head": None}, {"head": 42}, {"head": ""},
                          {"before": 42}, {"before": False}, {"before": []}):
            with self.subTest(overrides=overrides):
                MODULE.core.API_HAD_FAILURE = False
                event = push_event()
                event["payload"].update(overrides)
                with (
                    patch.object(MODULE.core, "github_get_json", return_value=[event]) as get,
                    redirect_stderr(io.StringIO()),
                ):
                    self.assertEqual(MODULE.fetch_public_push_activity(
                        {"gcomneno/vscode-bitbake"}
                    ), [])
                self.assertTrue(MODULE.core.API_HAD_FAILURE)
                self.assertEqual(get.call_count, 1)

    def test_branch_deletion_and_empty_comparison_are_valid_empty_activity(self) -> None:
        for responses in (
            [[push_event(head=MODULE.ZERO_SHA)]],
            [[push_event()], {"commits": []}],
        ):
            with self.subTest(responses=responses):
                with (
                    patch.object(MODULE.core, "github_get_json", side_effect=responses),
                    redirect_stderr(io.StringIO()),
                ):
                    self.assertEqual(MODULE.fetch_public_push_activity(
                        {"gcomneno/vscode-bitbake"}
                    ), [])
                self.assertFalse(MODULE.core.API_HAD_FAILURE)

    def test_empty_events_are_success_but_malformed_responses_fail(self) -> None:
        for payload in ([], None, {}, "invalid", [None], [{}],
                        [push_event() | {"created_at": "invalid"}],
                        [push_event() | {"created_at": "2026-11-04"}],
                        [push_event() | {"payload": None}]):
            with self.subTest(payload=payload):
                MODULE.core.API_HAD_FAILURE = False
                with (
                    patch.object(MODULE.core, "github_get_json", return_value=payload),
                    redirect_stderr(io.StringIO()),
                ):
                    self.assertEqual(MODULE.fetch_public_push_activity(
                        {"gcomneno/vscode-bitbake"}
                    ), [])
                self.assertEqual(MODULE.core.API_HAD_FAILURE, payload != [])

    def test_malformed_compare_and_head_responses_fail(self) -> None:
        for before, response in (
            ("def456", None), ("def456", []), ("def456", {}),
            ("def456", {"commits": None}), ("def456", {"commits": [None]}),
            ("def456", {"commits": [{}]}),
            (MODULE.ZERO_SHA, []), (MODULE.ZERO_SHA, None), (MODULE.ZERO_SHA, {}),
        ):
            with self.subTest(before=before, response=response):
                MODULE.core.API_HAD_FAILURE = False
                with (
                    patch.object(MODULE.core, "github_get_json", side_effect=[
                        [push_event(before=before)], response
                    ]), redirect_stderr(io.StringIO()),
                ):
                    self.assertEqual(MODULE.fetch_public_push_activity(
                        {"gcomneno/vscode-bitbake"}
                    ), [])
                self.assertTrue(MODULE.core.API_HAD_FAILURE)

    def test_later_event_page_failure_discards_partial_activity(self) -> None:
        page = [push_event()] + [push_event(
            repo="gcomneno/unlisted-public-repository"
        ) for _ in range(99)]
        with (
            patch.object(MODULE.core, "github_get_json", side_effect=[
                page, {"commits": [commit_obj()]}, {}
            ]) as get, redirect_stderr(io.StringIO()),
        ):
            self.assertEqual(MODULE.fetch_public_push_activity(
                {"gcomneno/vscode-bitbake"}
            ), [])
        self.assertEqual(get.call_count, 3)
        self.assertTrue(MODULE.core.API_HAD_FAILURE)

    def test_collects_meaningful_commit_from_public_branch(self) -> None:
        with patch.object(
            MODULE.core,
            "github_get_json",
            side_effect=[
                [push_event()],
                {"commits": [commit_obj()]},
            ],
        ):
            items = MODULE.fetch_public_push_activity(
                {"gcomneno/vscode-bitbake"}
            )

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].repo, "vscode-bitbake")
        self.assertEqual(items[0].kind, "feature")
        self.assertEqual(items[0].text, "add branch capability")
        self.assertEqual(
            items[0].url,
            "https://github.com/gcomneno/vscode-bitbake/commit/abc123",
        )

    def test_branch_creation_fetches_head_commit(self) -> None:
        with patch.object(
            MODULE.core,
            "github_get_json",
            side_effect=[
                [push_event(before=MODULE.ZERO_SHA)],
                commit_obj(),
            ],
        ):
            items = MODULE.fetch_public_push_activity(
                {"gcomneno/vscode-bitbake"}
            )

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].text, "add branch capability")

    def test_skips_repository_not_in_public_eligibility_set(self) -> None:
        with patch.object(
            MODULE.core,
            "github_get_json",
            return_value=[push_event(repo="gcomneno/cyse-lab")],
        ):
            items = MODULE.fetch_public_push_activity(
                {"gcomneno/vscode-bitbake"}
            )

        self.assertEqual(items, [])

    def test_skips_commit_not_attributable_to_owner(self) -> None:
        with patch.object(
            MODULE.core,
            "github_get_json",
            side_effect=[
                [push_event()],
                {"commits": [commit_obj(login="someone-else")]},
            ],
        ):
            items = MODULE.fetch_public_push_activity(
                {"gcomneno/vscode-bitbake"}
            )

        self.assertEqual(items, [])

    def test_skips_maintenance_commit_on_branch(self) -> None:
        with patch.object(
            MODULE.core,
            "github_get_json",
            side_effect=[
                [push_event()],
                {
                    "commits": [
                        commit_obj(message="test: adjust flaky fixture")
                    ]
                },
            ],
        ):
            items = MODULE.fetch_public_push_activity(
                {"gcomneno/vscode-bitbake"}
            )

        self.assertEqual(items, [])


class SupplementalCollectionTests(IsolatedApiTests):
    def test_discovery_failure_never_starts_activity_collection(self) -> None:
        with (
            patch.object(MODULE.core, "github_get_json", return_value={}),
            patch.object(MODULE.core, "fetch_repo_releases") as releases,
            patch.object(MODULE.core, "fetch_repo_commit_updates") as commits,
            patch.object(MODULE, "fetch_public_push_activity") as supplemental,
            redirect_stderr(io.StringIO()),
        ):
            self.assertEqual(MODULE.collect_updates(), [])
            self.assertTrue(MODULE.core.API_HAD_FAILURE)
            releases.assert_not_called()
            commits.assert_not_called()
            supplemental.assert_not_called()

    def test_main_failure_preserves_readmes_then_clean_invocation_succeeds(self) -> None:
        repo = {
            "full_name": "gcomneno/vscode-bitbake",
            "owner": {"login": "gcomneno"},
            "private": False, "archived": False, "disabled": False,
            "pushed_at": datetime.now(timezone.utc).isoformat(),
        }
        failures = (
            [{}],  # Discovery must not proceed to the public event API.
            [[repo], [], [], {}],
            [[repo], [], [], [push_event()], {}],
        )
        for responses in failures:
            with self.subTest(responses=responses), TemporaryDirectory() as directory:
                paths = {"en": Path(directory) / "README.md",
                         "it": Path(directory) / "README.it.md"}
                original = b"Intro\r\n<!-- updates:start -->\r\nold\r\n<!-- updates:end -->\r\n"
                for path in paths.values():
                    path.write_bytes(original)
                collector = MODULE.core.collect_updates
                with (
                    patch.object(MODULE.core, "README_PATHS", paths),
                    patch.object(MODULE.core, "github_get_json", side_effect=responses),
                    patch.object(MODULE.core, "write_bilingual") as write,
                    redirect_stderr(io.StringIO()), redirect_stdout(io.StringIO()),
                ):
                    self.assertEqual(MODULE.main(), 1)
                    self.assertTrue(MODULE.core.API_HAD_FAILURE)
                    write.assert_not_called()
                self.assertIs(MODULE.core.collect_updates, collector)
                for path in paths.values():
                    self.assertEqual(path.read_bytes(), original)
                # No manual clearing of the failure flag between invocations.
                with (
                    patch.object(MODULE.core, "README_PATHS", paths),
                    patch.object(MODULE.core, "github_get_json", return_value=[]),
                    redirect_stderr(io.StringIO()), redirect_stdout(io.StringIO()),
                ):
                    self.assertEqual(MODULE.main(), 0)
                    self.assertFalse(MODULE.core.API_HAD_FAILURE)
                self.assertIs(MODULE.core.collect_updates, collector)
                for locale, path in paths.items():
                    self.assertIn(MODULE.core.UI_BY_LOCALE[locale]["fallback"],
                                  path.read_text(encoding="utf-8"))

    @staticmethod
    def update(url: str, text: str) -> MODULE.core.UpdateItem:
        return MODULE.core.UpdateItem(
            date=datetime(2026, 8, 18, 12, 0, tzinfo=timezone.utc),
            repo="vscode-bitbake",
            kind="feature",
            text=text,
            url=url,
            priority=MODULE.core.COMMIT_PRIORITY_BY_KIND["feature"],
        )

    def test_keeps_branch_item_but_not_duplicate_default_commit(self) -> None:
        stable_url = (
            "https://github.com/gcomneno/vscode-bitbake/commit/stable"
        )
        branch_url = (
            "https://github.com/gcomneno/vscode-bitbake/commit/branch"
        )
        stable = self.update(stable_url, "stable")
        duplicate = self.update(stable_url, "duplicate")
        branch = self.update(branch_url, "branch")

        with (
            patch.object(
                MODULE.core,
                "discover_public_repositories",
                return_value=["gcomneno/vscode-bitbake"],
            ),
            patch.object(
                MODULE.core,
                "fetch_repo_releases",
                return_value=[],
            ),
            patch.object(
                MODULE.core,
                "fetch_repo_commit_updates",
                return_value=[stable],
            ),
            patch.object(
                MODULE,
                "fetch_public_push_activity",
                return_value=[duplicate, branch],
            ),
        ):
            items = MODULE.collect_updates()

        self.assertEqual(
            [item.url for item in items],
            [stable_url, branch_url],
        )


if __name__ == "__main__":
    unittest.main()
