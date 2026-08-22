from __future__ import annotations

import unittest
from pathlib import Path


README_PATHS = (Path("README.md"), Path("README.it.md"))

ATELIER_KIT_DEMO_URL = "https://atelier-kit-public-demo.vercel.app/"
ATELIER_KIT_SOURCE_URL = "https://github.com/gcomneno/atelier-kit"
ATELIER_KIT_SOURCE_BADGE = "https://img.shields.io/badge/SOURCE%20CODE-GITHUB-24292F?style=for-the-badge&logo=github&logoColor=white"

FEATURED_DEMO_MARKERS = {
    "README.md": (
        "These projects best represent my current work",
        "<strong>Featured live demo — Atelier-Kit</strong>",
        "| Project | Official release | What it does | What it demonstrates |",
    ),
    "README.it.md": (
        "Questi progetti rappresentano meglio il mio lavoro attuale",
        "<strong>Demo live in evidenza — Atelier-Kit</strong>",
        "| Progetto | Release ufficiale | Cosa fa | Cosa dimostra |",
    ),
}

SELECTED_PROJECTS = (
    "atelier-kit",
    "smart-file-organizer",
    "lele-manager",
    "giadaware-ui-components",
    "gyte",
    "ubuntu-system-tools",
)

OPERATIONAL_PROJECTS = (
    "semantic-mail-archivist",
    "gyte-study-tools",
    "lele-quizzer",
)

PRIMARY_RESEARCH = (
    "system-log-dynamics",
    "lotto-digit-coverage-dynamics",
    "digit-probe",
    "oeis-probe",
)

SECONDARY_RESEARCH = (
    "midas",
    "turbo-bucketizer",
    "integer-structural-search",
    "huffman-compressor",
    "prime-tower-clocks",
    "lasagna-v2",
    "crystal-codec-gcc-v1",
)

PRIMARY_LEARNING = (
    "yocto-qemu-mini-lab",
    "distributed-systems-study",
    "system-design-study",
    "kleis-corso-sviluppo-software",
    "physics-study",
)

SUPPORTING_LEARNING = (
    "oop-in-c-lab",
    "js-lab-didattico",
    "boardlab",
    "web",
)

FORBIDDEN_PROFILE_LINKS = (
    "https://github.com/gcomneno/reference-engine",
    "https://github.com/gcomneno/cyse-lab",
    "https://github.com/gcomneno/testflinger",
    "https://github.com/canonical/testflinger",
)

YOCTO_PULL_REQUESTS = (
    538,
    543,
    545,
    544,
    513,
    518,
    510,
    533,
    532,
    535,
    524,
    526,
)

CANONICAL_CRAFT_PULL_REQUESTS = (
    ("craft-parts", 1600),
    ("craft-parts", 1598),
    ("craft-parts", 1562),
    ("craft-parts", 1533),
    ("craft-application", 1068),
    ("craft-providers", 966),
    ("craft-cli", 425),
    ("rockcraft", 1148),
)

CANONICAL_OPERATOR_PULL_REQUESTS = (
    ("operator", 2454),
)

LEGACY_FORK_HEADINGS = {
    "README.md": (
        "Previously contributed — Canonical Craft ecosystem",
        "Other public upstream forks",
    ),
    "README.it.md": (
        "Contributi precedenti — ecosistema Canonical Craft",
        "Altri fork upstream pubblici",
    ),
}


def assert_tokens_in_order(
    testcase: unittest.TestCase,
    text: str,
    tokens: tuple[str, ...],
    *,
    label: str,
) -> None:
    positions = []
    for token in tokens:
        position = text.find(token)
        testcase.assertNotEqual(position, -1, f"{label}: missing {token}")
        positions.append(position)

    testcase.assertEqual(
        positions,
        sorted(positions),
        f"{label}: entries are not ordered by descending portfolio priority",
    )


class ProfilePriorityOrderingTests(unittest.TestCase):
    def test_atelier_kit_featured_demo_is_prominent_and_bilingual(self) -> None:
        for path in README_PATHS:
            text = path.read_text(encoding="utf-8")
            intro, demo_heading, table_heading = FEATURED_DEMO_MARKERS[path.name]

            self.assertEqual(
                text.count(ATELIER_KIT_DEMO_URL),
                1,
                f"{path}: Atelier-Kit demo URL must appear exactly once",
            )
            self.assertIn(
                ATELIER_KIT_SOURCE_URL,
                text,
                f"{path}: Atelier-Kit source link missing",
            )
            self.assertEqual(
                text.count(ATELIER_KIT_SOURCE_BADGE),
                1,
                f"{path}: Atelier-Kit source badge must appear exactly once",
            )
            self.assertNotIn(
                "&nbsp;·&nbsp;",
                text[
                    text.find(demo_heading):
                    text.find(table_heading)
                ],
                f"{path}: demo actions must not use a dangling text separator",
            )

            intro_position = text.find(intro)
            demo_position = text.find(demo_heading)
            table_position = text.find(table_heading)

            self.assertNotEqual(
                intro_position,
                -1,
                f"{path}: Selected Projects intro missing",
            )
            self.assertNotEqual(
                demo_position,
                -1,
                f"{path}: featured Atelier-Kit demo missing",
            )
            self.assertNotEqual(
                table_position,
                -1,
                f"{path}: Selected Projects table missing",
            )
            self.assertLess(
                intro_position,
                demo_position,
                f"{path}: demo must follow the Selected Projects intro",
            )
            self.assertLess(
                demo_position,
                table_position,
                f"{path}: demo must precede the Selected Projects table",
            )

    def test_curated_repository_lists_follow_priority_order(self) -> None:
        for path in README_PATHS:
            text = path.read_text(encoding="utf-8")

            with self.subTest(path=path, section="selected"):
                assert_tokens_in_order(
                    self,
                    text,
                    tuple(
                        f"https://github.com/gcomneno/{repo}) |"
                        for repo in SELECTED_PROJECTS
                    ),
                    label=f"{path}: Selected Projects",
                )

            with self.subTest(path=path, section="operational"):
                assert_tokens_in_order(
                    self,
                    text,
                    tuple(
                        f"https://github.com/gcomneno/{repo}) |"
                        for repo in OPERATIONAL_PROJECTS
                    ),
                    label=f"{path}: operational projects",
                )

            with self.subTest(path=path, section="primary-research"):
                assert_tokens_in_order(
                    self,
                    text,
                    tuple(
                        f"https://github.com/gcomneno/{repo}) |"
                        for repo in PRIMARY_RESEARCH
                    ),
                    label=f"{path}: primary research",
                )

            with self.subTest(path=path, section="secondary-research"):
                assert_tokens_in_order(
                    self,
                    text,
                    tuple(
                        f"https://github.com/gcomneno/{repo}) |"
                        for repo in SECONDARY_RESEARCH
                    ),
                    label=f"{path}: secondary research",
                )

            with self.subTest(path=path, section="primary-learning"):
                assert_tokens_in_order(
                    self,
                    text,
                    tuple(
                        f"https://github.com/gcomneno/{repo}) |"
                        for repo in PRIMARY_LEARNING
                    ),
                    label=f"{path}: primary learning",
                )

            with self.subTest(path=path, section="supporting-learning"):
                assert_tokens_in_order(
                    self,
                    text,
                    tuple(
                        f"https://github.com/gcomneno/{repo})"
                        for repo in SUPPORTING_LEARNING
                    ),
                    label=f"{path}: supporting learning",
                )

    def test_forbidden_showcase_links_are_absent(self) -> None:
        for path in README_PATHS:
            text = path.read_text(encoding="utf-8")
            for link in FORBIDDEN_PROFILE_LINKS:
                self.assertNotIn(
                    link,
                    text,
                    f"{path}: forbidden showcase link still present: {link}",
                )

    def test_legacy_fork_sections_are_absent(self) -> None:
        for path in README_PATHS:
            text = path.read_text(encoding="utf-8")
            for heading in LEGACY_FORK_HEADINGS[path.name]:
                self.assertNotIn(
                    heading,
                    text,
                    f"{path}: legacy fork-centric heading still present",
                )

    def test_selected_yocto_prs_follow_signal_priority(self) -> None:
        for path in README_PATHS:
            text = path.read_text(encoding="utf-8")
            assert_tokens_in_order(
                self,
                text,
                tuple(
                    "https://github.com/yoctoproject/"
                    f"vscode-bitbake/pull/{number})"
                    for number in YOCTO_PULL_REQUESTS
                ),
                label=f"{path}: selected Yocto pull requests",
            )

    def test_selected_canonical_prs_follow_signal_priority(self) -> None:
        for path in README_PATHS:
            text = path.read_text(encoding="utf-8")

            assert_tokens_in_order(
                self,
                text,
                tuple(
                    f"https://github.com/canonical/{repo}/pull/{number})"
                    for repo, number in CANONICAL_CRAFT_PULL_REQUESTS
                ),
                label=f"{path}: selected Canonical Craft pull requests",
            )

            assert_tokens_in_order(
                self,
                text,
                tuple(
                    f"https://github.com/canonical/{repo}/pull/{number})"
                    for repo, number in CANONICAL_OPERATOR_PULL_REQUESTS
                ),
                label=f"{path}: selected Canonical Operator pull requests",
            )


if __name__ == "__main__":
    unittest.main()
