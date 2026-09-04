from __future__ import annotations

import importlib.util
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch


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


def item(
    *,
    hour: int,
    kind: str,
    text: str,
    url: str,
    priority: int | None = None,
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
        repo="example",
        kind=kind,
        text=text,
        url=url,
        priority=(
            MODULE.COMMIT_PRIORITY_BY_KIND[kind]
            if priority is None
            else priority
        ),
    )


class RepositoryEligibilityPolicyTests(unittest.TestCase):
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
        self.assertIn(
            "gcomneno/grocery-deal-intelligence",
            MODULE.CURATED_REPOSITORIES,
        )
        self.assertIn(
            "gcomneno/linux-container-lab",
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
            },
            {
                "full_name": "gcomneno/atelier-kit",
                "owner": {"login": "gcomneno"},
                "private": False,
                "archived": False,
                "disabled": False,
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
    def test_keeps_only_most_recent_hundred_items(
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
                repo="example",
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
            "[update-99]",
            rendered,
        )
        self.assertNotIn(
            "[update-100]",
            rendered,
        )
        self.assertIn(
            "5 older update(s) omitted",
            rendered,
        )
        self.assertIn(
            "More recent meaningful updates",
            rendered,
        )

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

    def test_renders_italian_details_summary(
        self,
    ) -> None:
        updates = [
            item(
                hour=10 - index,
                kind="development",
                text=f"update-{index}",
                url=f"https://example.test/{index}",
            )
            for index in range(5)
        ]

        rendered = MODULE.render_updates(
            updates,
            locale="it",
        )

        self.assertIn(
            "Altri aggiornamenti recenti e significativi",
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
                    return_value=[update],
                ),
                patch.object(
                    MODULE,
                    "API_HAD_FAILURE",
                    True,
                ),
            ):
                result = MODULE.main()

            self.assertEqual(result, 0)

            for path in paths.values():
                self.assertEqual(
                    path.read_text(
                        encoding="utf-8",
                    ),
                    original,
                )


if __name__ == "__main__":
    unittest.main()
