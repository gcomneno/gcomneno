#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

OWNER_LOGIN = "gcomneno"
README_PATHS = {
    "en": Path("README.md"),
    "it": Path("README.it.md"),
}
SELECTED_REPOSITORIES = (
    "atelier-kit",
    "smart-file-organizer",
    "lele-manager",
    "giadaware-ui-components",
    "gyte",
    "reference-engine",
    "ubuntu-system-tools",
)


class ReleaseSyncError(RuntimeError):
    pass


@dataclass(frozen=True)
class OfficialRelease:
    tag_name: str
    html_url: str


def github_headers() -> dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "gcomneno-profile-release-sync",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def fetch_latest_release(repository: str) -> OfficialRelease | None:
    url = (
        f"https://api.github.com/repos/{OWNER_LOGIN}/{repository}"
        "/releases/latest"
    )
    request = Request(url, headers=github_headers())

    try:
        with urlopen(request, timeout=20) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        if exc.code == 404:
            return None
        raise ReleaseSyncError(
            f"GitHub API returned {exc.code} for {repository}."
        ) from exc
    except (URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise ReleaseSyncError(
            f"GitHub API failed for {repository}: {exc}"
        ) from exc

    if not isinstance(payload, dict):
        raise ReleaseSyncError(
            f"Malformed latest-release response for {repository}."
        )

    tag_name = payload.get("tag_name")
    html_url = payload.get("html_url")
    if (
        not isinstance(tag_name, str)
        or not tag_name.strip()
        or not isinstance(html_url, str)
        or not html_url.startswith("https://github.com/")
        or payload.get("draft") is True
        or payload.get("prerelease") is True
    ):
        raise ReleaseSyncError(
            f"Invalid latest-release payload for {repository}."
        )

    return OfficialRelease(tag_name=tag_name.strip(), html_url=html_url)


def render_release_cell(release: OfficialRelease | None) -> str:
    if release is None:
        return "—"
    return f"[{release.tag_name}]({release.html_url})"


def replace_release_cell(
    readme: str,
    repository: str,
    release: OfficialRelease | None,
    *,
    source: str,
) -> str:
    repo_url = f"https://github.com/{OWNER_LOGIN}/{repository}"
    pattern = re.compile(
        rf"^(?P<prefix>\| \[[^\]]+\]\({re.escape(repo_url)}\) \| )"
        rf"(?P<cell>[^|]*?)"
        rf"(?P<suffix> \| .*)$",
        re.MULTILINE,
    )
    matches = list(pattern.finditer(readme))
    if len(matches) != 1:
        raise ReleaseSyncError(
            f"{source}: expected exactly one Selected Projects row for "
            f"{repository}, found {len(matches)}."
        )

    cell = render_release_cell(release)
    return pattern.sub(
        lambda match: f"{match.group('prefix')}{cell}{match.group('suffix')}",
        readme,
        count=1,
    )


def build_updated_readmes(
    releases: dict[str, OfficialRelease | None],
    paths: dict[str, Path] | None = None,
) -> dict[Path, str]:
    resolved_paths = README_PATHS if paths is None else paths
    originals: dict[Path, str] = {}

    for locale, path in resolved_paths.items():
        if not path.is_file():
            raise ReleaseSyncError(
                f"Profile README missing for locale {locale}: {path}"
            )
        originals[path] = path.read_text(encoding="utf-8")

    updated: dict[Path, str] = {}
    for path, original in originals.items():
        text = original
        for repository in SELECTED_REPOSITORIES:
            if repository not in releases:
                raise ReleaseSyncError(
                    f"Missing release lookup result for {repository}."
                )
            text = replace_release_cell(
                text,
                repository,
                releases[repository],
                source=str(path),
            )
        updated[path] = text

    return updated


def main() -> int:
    try:
        releases = {
            repository: fetch_latest_release(repository)
            for repository in SELECTED_REPOSITORIES
        }
        updated = build_updated_readmes(releases)
    except ReleaseSyncError as exc:
        print(f"Release sync aborted: {exc}", file=sys.stderr)
        print("Profile READMEs left unchanged.", file=sys.stderr)
        return 1

    changed_paths = [
        path
        for path, content in updated.items()
        if content != path.read_text(encoding="utf-8")
    ]
    if not changed_paths:
        print("Selected Projects releases already up to date.")
        return 0

    for path in changed_paths:
        path.write_text(updated[path], encoding="utf-8")

    changed = ", ".join(str(path) for path in changed_paths)
    print(f"Synchronized official Selected Projects releases in {changed}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
