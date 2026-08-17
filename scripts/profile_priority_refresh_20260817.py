#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


README_PATHS = (Path("README.md"), Path("README.it.md"))

ORDERED_GROUPS = (
    (
        "Selected Projects",
        (
            "https://github.com/gcomneno/atelier-kit)",
            "https://github.com/gcomneno/smart-file-organizer)",
            "https://github.com/gcomneno/lele-manager)",
            "https://github.com/gcomneno/giadaware-ui-components)",
            "https://github.com/gcomneno/gyte)",
            "https://github.com/gcomneno/reference-engine)",
            "https://github.com/gcomneno/ubuntu-system-tools)",
        ),
    ),
    (
        "operational projects",
        (
            "https://github.com/gcomneno/semantic-mail-archivist)",
            "https://github.com/gcomneno/gyte-study-tools)",
            "https://github.com/gcomneno/lele-quizzer)",
        ),
    ),
    (
        "Canonical forks",
        (
            "https://github.com/gcomneno/rockcraft)",
            "https://github.com/gcomneno/snapcraft)",
            "https://github.com/gcomneno/craft-parts)",
            "https://github.com/gcomneno/craft-providers)",
            "https://github.com/gcomneno/craft-application)",
            "https://github.com/gcomneno/craft-cli)",
        ),
    ),
    (
        "primary research",
        (
            "https://github.com/gcomneno/system-log-dynamics)",
            "https://github.com/gcomneno/lotto-digit-coverage-dynamics)",
            "https://github.com/gcomneno/digit-probe)",
            "https://github.com/gcomneno/oeis-probe)",
        ),
    ),
    (
        "secondary research",
        (
            "https://github.com/gcomneno/midas)",
            "https://github.com/gcomneno/turbo-bucketizer)",
            "https://github.com/gcomneno/integer-structural-search)",
            "https://github.com/gcomneno/huffman-compressor)",
            "https://github.com/gcomneno/prime-tower-clocks)",
            "https://github.com/gcomneno/lasagna-v2)",
            "https://github.com/gcomneno/crystal-codec-gcc-v1)",
        ),
    ),
    (
        "primary learning",
        (
            "https://github.com/gcomneno/yocto-qemu-mini-lab)",
            "https://github.com/gcomneno/distributed-systems-study)",
            "https://github.com/gcomneno/system-design-study)",
            "https://github.com/gcomneno/kleis-corso-sviluppo-software)",
            "https://github.com/gcomneno/physics-study)",
        ),
    ),
    (
        "supporting learning",
        (
            "https://github.com/gcomneno/oop-in-c-lab)",
            "https://github.com/gcomneno/js-lab-didattico)",
            "https://github.com/gcomneno/boardlab)",
            "https://github.com/gcomneno/web)",
        ),
    ),
    (
        "selected Yocto PRs",
        tuple(
            f"https://github.com/yoctoproject/vscode-bitbake/pull/{number})"
            for number in (538, 543, 545, 544, 533, 532, 535, 524, 526, 541, 521, 527)
        ),
    ),
)


def reorder_group(lines: list[str], label: str, tokens: tuple[str, ...], source: str) -> None:
    indexed: list[tuple[int, str]] = []
    for token in tokens:
        matches = [index for index, line in enumerate(lines) if token in line]
        if len(matches) != 1:
            raise RuntimeError(
                f"{source}: {label}: expected exactly one line for {token}, found {len(matches)}"
            )
        indexed.append((matches[0], lines[matches[0]]))

    positions = sorted(index for index, _line in indexed)
    expected = list(range(positions[0], positions[0] + len(positions)))
    if positions != expected:
        raise RuntimeError(
            f"{source}: {label}: target lines are not contiguous; refusing to reorder"
        )

    line_by_token = {
        token: next(line for _index, line in indexed if token in line)
        for token in tokens
    }
    for position, token in zip(positions, tokens, strict=True):
        lines[position] = line_by_token[token]


def build_updated(path: Path) -> str:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines(keepends=True)
    for label, tokens in ORDERED_GROUPS:
        reorder_group(lines, label, tokens, str(path))
    return "".join(lines)


def main() -> int:
    originals = {path: path.read_text(encoding="utf-8") for path in README_PATHS}
    updated = {path: build_updated(path) for path in README_PATHS}

    for path in README_PATHS:
        if updated[path] != originals[path]:
            path.write_text(updated[path], encoding="utf-8")

    changed = [str(path) for path in README_PATHS if updated[path] != originals[path]]
    if changed:
        print("Reordered curated profile entries by descending portfolio priority: " + ", ".join(changed))
    else:
        print("Curated profile entries already follow portfolio priority order.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
