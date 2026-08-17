#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    target = Path(path)
    text = target.read_text(encoding="utf-8")
    count = text.count(old)
    if count == 1:
        target.write_text(text.replace(old, new, 1), encoding="utf-8")
        return
    if count == 0 and new and new in text:
        return
    if count == 0 and not new:
        return
    raise RuntimeError(f"{path}: expected exactly one migration target, found {count}")


def require_absent(path: str, tokens: tuple[str, ...]) -> None:
    text = Path(path).read_text(encoding="utf-8")
    present = [token for token in tokens if token in text]
    if present:
        raise RuntimeError(f"{path}: retired profile references remain: {present}")


def main() -> int:
    reference_row_en = (
        "| [GiadaWare Reference Engine](https://github.com/gcomneno/reference-engine) | — | "
        "Extracts, validates, traces provenance and queries information from personal reference documents | "
        "Deterministic extraction, validation, provenance, querying and durable repository boundaries |\n"
    )
    reference_row_it = (
        "| [GiadaWare Reference Engine](https://github.com/gcomneno/reference-engine) | — | "
        "Estrae, valida, traccia la provenienza e rende interrogabili informazioni da documenti personali di riferimento | "
        "Estrazione deterministica, validazione, provenienza, interrogazione e confini persistenti del repository |\n"
    )
    replace_once("README.md", reference_row_en, "")
    replace_once("README.it.md", reference_row_it, "")

    replace_once(
        "scripts/sync_selected_project_releases.py",
        '    "gyte",\n    "reference-engine",\n    "ubuntu-system-tools",\n',
        '    "gyte",\n    "ubuntu-system-tools",\n',
    )
    replace_once(
        "tests/test_profile_curation.py",
        '    "gyte",\n    "reference-engine",\n    "ubuntu-system-tools",\n',
        '    "gyte",\n    "ubuntu-system-tools",\n',
    )

    replace_once(
        "tests/test_sync_selected_project_releases.py",
        '                if repository in {\n                    "reference-engine",\n                    "giadaware-ui-components",\n                }:\n',
        '                if repository == "giadaware-ui-components":\n',
    )
    replace_once(
        "tests/test_sync_selected_project_releases.py",
        '                self.assertIn(\n                    "| [reference-engine](https://github.com/gcomneno/"\n                    "reference-engine) | — |",\n                    content,\n                )\n',
        "",
    )

    replace_once(
        "scripts/update_latest_updates.py",
        'PROFILE_REPO = f"{OWNER_LOGIN}/{OWNER_LOGIN}"\n\nVISIBLE_ITEMS = 4\n',
        'PROFILE_REPO = f"{OWNER_LOGIN}/{OWNER_LOGIN}"\nEXCLUDED_REPOSITORIES = {\n    f"{OWNER_LOGIN}/reference-engine",\n    f"{OWNER_LOGIN}/cyse-lab",\n}\n\nVISIBLE_ITEMS = 4\n',
    )
    replace_once(
        "scripts/update_latest_updates.py",
        '            if full_name == PROFILE_REPO:\n                continue\n            if repo.get("private") is True:\n',
        '            if full_name == PROFILE_REPO:\n                continue\n            if full_name in EXCLUDED_REPOSITORIES:\n                continue\n            if repo.get("private") is True:\n',
    )

    replace_once(
        "tests/test_update_latest_updates.py",
        'class UpdateMessageTests(unittest.TestCase):\n',
        '''class RepositoryExclusionPolicyTests(unittest.TestCase):\n    def test_retired_repositories_are_explicitly_excluded(self) -> None:\n        self.assertEqual(\n            MODULE.EXCLUDED_REPOSITORIES,\n            {\n                "gcomneno/reference-engine",\n                "gcomneno/cyse-lab",\n            },\n        )\n\n    def test_discovery_skips_retired_repositories(self) -> None:\n        payload = [\n            {\n                "full_name": "gcomneno/reference-engine",\n                "owner": {"login": "gcomneno"},\n                "private": False,\n                "archived": False,\n                "disabled": False,\n            },\n            {\n                "full_name": "gcomneno/cyse-lab",\n                "owner": {"login": "gcomneno"},\n                "private": False,\n                "archived": False,\n                "disabled": False,\n            },\n            {\n                "full_name": "gcomneno/atelier-kit",\n                "owner": {"login": "gcomneno"},\n                "private": False,\n                "archived": False,\n                "disabled": False,\n            },\n        ]\n        with patch.object(MODULE, "github_get_json", side_effect=[payload, []]):\n            self.assertEqual(\n                MODULE.discover_public_repositories(),\n                ["gcomneno/atelier-kit"],\n            )\n\n\nclass UpdateMessageTests(unittest.TestCase):\n''',
    )

    replace_once(
        "tests/test_profile_curation.py",
        'YOCTO_PULL_REQUESTS = (\n',
        'RETIRED_PROFILE_REPOSITORIES = (\n    "reference-engine",\n    "cyse-lab",\n)\n\nYOCTO_PULL_REQUESTS = (\n',
    )
    replace_once(
        "tests/test_profile_curation.py",
        '    def test_selected_yocto_prs_follow_signal_priority(self) -> None:\n',
        '''    def test_retired_repositories_are_absent_from_curated_profile(self) -> None:\n        for path in README_PATHS:\n            text = path.read_text(encoding="utf-8")\n            for repository in RETIRED_PROFILE_REPOSITORIES:\n                self.assertNotIn(\n                    f"https://github.com/gcomneno/{repository}",\n                    text,\n                    f"{path}: retired repository still exposed: {repository}",\n                )\n\n    def test_selected_yocto_prs_follow_signal_priority(self) -> None:\n''',
    )

    require_absent("README.md", ("gcomneno/reference-engine", "gcomneno/cyse-lab"))
    require_absent("README.it.md", ("gcomneno/reference-engine", "gcomneno/cyse-lab"))
    print("Retired profile repositories removed and exclusion policy installed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
