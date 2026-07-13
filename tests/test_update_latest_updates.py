from __future__ import annotations

import importlib.util
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path


SCRIPT_PATH = Path(__file__).parents[1] / "scripts" / "update_latest_updates.py"
SPEC = importlib.util.spec_from_file_location("update_latest_updates", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class UpdateTagTests(unittest.TestCase):
    def test_parse_docs_tag(self) -> None:
        self.assertEqual(
            MODULE.parse_update_message("docs: explain why and when to use Yocto"),
            ("docs", "explain why and when to use Yocto"),
        )

    def test_parse_docs_tag_is_case_insensitive(self) -> None:
        self.assertEqual(
            MODULE.parse_update_message("DOCS: Pin Wrynose release notes link"),
            ("docs", "Pin Wrynose release notes link"),
        )

    def test_render_docs_label(self) -> None:
        item = MODULE.UpdateItem(
            date=datetime(2026, 7, 13, 9, 0, tzinfo=timezone.utc),
            repo="yocto-qemu-mini-lab",
            kind="docs",
            text="explain why and when to use Yocto",
            url="https://example.test/commit/123",
            priority=MODULE.COMMIT_PRIORITY_BY_KIND["docs"],
        )

        self.assertEqual(
            MODULE.render_update_item(item),
            "- **2026-07-13** · `yocto-qemu-mini-lab` · **Docs:** "
            "[explain why and when to use Yocto](https://example.test/commit/123)",
        )

    def test_news_wins_over_docs_for_same_repo_and_day(self) -> None:
        docs = MODULE.UpdateItem(
            date=datetime(2026, 7, 13, 9, 0, tzinfo=timezone.utc),
            repo="example",
            kind="docs",
            text="documentation",
            url="https://example.test/docs",
            priority=MODULE.COMMIT_PRIORITY_BY_KIND["docs"],
        )
        news = MODULE.UpdateItem(
            date=datetime(2026, 7, 13, 8, 0, tzinfo=timezone.utc),
            repo="example",
            kind="news",
            text="important news",
            url="https://example.test/news",
            priority=MODULE.COMMIT_PRIORITY_BY_KIND["news"],
        )

        self.assertEqual(MODULE.dedupe_updates([docs, news]), [news])

    def test_parse_update_tag(self) -> None:
        self.assertEqual(
            MODULE.parse_update_message("update: align Scimmietta Operativa profile"),
            ("update", "align Scimmietta Operativa profile"),
        )

    def test_parse_update_tag_is_case_insensitive(self) -> None:
        self.assertEqual(
            MODULE.parse_update_message("UPDATE: Refresh profile"),
            ("update", "Refresh profile"),
        )

    def test_render_update_label(self) -> None:
        item = MODULE.UpdateItem(
            date=datetime(2026, 7, 11, 9, 0, tzinfo=timezone.utc),
            repo="ai-operating-profiles",
            kind="update",
            text="align Scimmietta Operativa profile",
            url="https://example.test/commit/123",
            priority=MODULE.COMMIT_PRIORITY_BY_KIND["update"],
        )

        self.assertEqual(
            MODULE.render_update_item(item),
            "- **2026-07-11** · `ai-operating-profiles` · **Update:** "
            "[align Scimmietta Operativa profile](https://example.test/commit/123)",
        )

    def test_update_wins_over_news_for_same_repo_and_day(self) -> None:
        news = MODULE.UpdateItem(
            date=datetime(2026, 7, 11, 8, 0, tzinfo=timezone.utc),
            repo="example",
            kind="news",
            text="older news",
            url="https://example.test/news",
            priority=MODULE.COMMIT_PRIORITY_BY_KIND["news"],
        )
        update = MODULE.UpdateItem(
            date=datetime(2026, 7, 11, 7, 0, tzinfo=timezone.utc),
            repo="example",
            kind="update",
            text="important update",
            url="https://example.test/update",
            priority=MODULE.COMMIT_PRIORITY_BY_KIND["update"],
        )

        self.assertEqual(MODULE.dedupe_updates([news, update]), [update])

    def test_release_still_wins_over_update(self) -> None:
        update = MODULE.UpdateItem(
            date=datetime(2026, 7, 11, 9, 0, tzinfo=timezone.utc),
            repo="example",
            kind="update",
            text="update",
            url="https://example.test/update",
            priority=MODULE.COMMIT_PRIORITY_BY_KIND["update"],
        )
        release = MODULE.UpdateItem(
            date=datetime(2026, 7, 11, 8, 0, tzinfo=timezone.utc),
            repo="example",
            kind="release",
            text="v1.0.0",
            url="https://example.test/release",
            priority=MODULE.PRIORITY_RELEASE_API,
        )

        self.assertEqual(MODULE.dedupe_updates([update, release]), [release])


if __name__ == "__main__":
    unittest.main()
