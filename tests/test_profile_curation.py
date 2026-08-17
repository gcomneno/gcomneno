from __future__ import annotations

import unittest
from pathlib import Path


README_PATHS = (Path("README.md"), Path("README.it.md"))

SELECTED_PROJECTS = (
    "atelier-kit",
    "smart-file-organizer",
    "lele-manager",
    "giadaware-ui-components",
    "gyte",
    "reference-engine",
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

CANONICAL_FORKS = (
    "rockcraft",
    "snapcraft",
    "craft-parts",
    "craft-providers",
    "craft-application",
    "craft-cli",
)

YOCTO_PULL_REQUESTS = (
    538,
    543,
    545,
    544,
    533,
    532,
    535,
    524,
    526,
    541,
    521,
    527,
)


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
            with self.subTest(path=path, section="canonical-forks"):
                assert_tokens_in_order(
                    self,
                    text,
                    tuple(
                        f"https://github.com/gcomneno/{repo})"
                        for repo in CANONICAL_FORKS
                    ),
                    label=f"{path}: Canonical forks",
                )

    def test_selected_yocto_prs_follow_signal_priority(self) -> None:
        for path in README_PATHS:
            text = path.read_text(encoding="utf-8")
            assert_tokens_in_order(
                self,
                text,
                tuple(
                    f"https://github.com/yoctoproject/vscode-bitbake/pull/{number})"
                    for number in YOCTO_PULL_REQUESTS
                ),
                label=f"{path}: selected Yocto pull requests",
            )


if __name__ == "__main__":
    unittest.main()
