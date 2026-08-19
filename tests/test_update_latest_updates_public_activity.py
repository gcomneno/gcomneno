from __future__ import annotations

import importlib.util
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path
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


def push_event(
    *,
    repo: str = "gcomneno/vscode-bitbake",
    sha: str = "abc123",
    message: str = "feat: add branch capability",
    email: str = "126195429+gcomneno@users.noreply.github.com",
) -> dict:
    return {
        "type": "PushEvent",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "actor": {"login": "gcomneno", "id": 126195429},
        "repo": {"name": repo},
        "payload": {
            "ref": "refs/heads/contrib/issue-example",
            "commits": [
                {
                    "sha": sha,
                    "message": message,
                    "author": {
                        "name": "Giancarlo",
                        "email": email,
                    },
                }
            ],
        },
    }


class PublicPushActivityTests(unittest.TestCase):
    def test_collects_meaningful_commit_from_public_branch(self) -> None:
        with patch.object(
            MODULE.core,
            "github_get_json",
            return_value=[push_event()],
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
            return_value=[
                push_event(email="someone@example.com")
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
            return_value=[
                push_event(message="test: adjust flaky fixture")
            ],
        ):
            items = MODULE.fetch_public_push_activity(
                {"gcomneno/vscode-bitbake"}
            )

        self.assertEqual(items, [])


class SupplementalCollectionTests(unittest.TestCase):
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
