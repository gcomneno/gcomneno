#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass
from http.client import HTTPException
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

try:
    from scripts.bilingual_write import (
        BilingualWriteError, FileSnapshot, read_snapshot, write_bilingual,
    )
except ModuleNotFoundError:  # Direct execution: python scripts/<generator>.py
    from bilingual_write import (
        BilingualWriteError, FileSnapshot, read_snapshot, write_bilingual,
    )

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
    "ubuntu-system-tools",
    "giadaware-ai",
    "gyte-ai-learning-pipeline",
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


def verify_repository_eligibility(repository: str) -> None:
    request = Request(
        f"https://api.github.com/repos/{OWNER_LOGIN}/{repository}",
        headers=github_headers(),
    )
    try:
        with urlopen(request, timeout=20) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except (OSError, HTTPException, UnicodeError, json.JSONDecodeError):
        # Neither response bodies nor exception details are safe to disclose.
        raise ReleaseSyncError("GitHub repository metadata lookup failed.") from None

    if not isinstance(payload, dict):
        raise ReleaseSyncError("Malformed repository metadata response.")

    owner = payload.get("owner")
    owner_login = owner.get("login") if isinstance(owner, dict) else None
    name = payload.get("name")
    full_name = payload.get("full_name")
    if (
        not isinstance(owner_login, str)
        or owner_login.casefold() != OWNER_LOGIN.casefold()
        or not isinstance(name, str)
        or name.casefold() != repository.casefold()
        or not isinstance(full_name, str)
        or full_name.casefold() != f"{OWNER_LOGIN}/{repository}".casefold()
        or any(
            payload.get(flag) is not False
            for flag in ("private", "archived", "disabled")
        )
        or payload.get("visibility") != "public"
    ):
        raise ReleaseSyncError("Repository eligibility could not be verified.")


def fetch_latest_release(repository: str) -> OfficialRelease | None:
    verify_repository_eligibility(repository)
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
        ) from None
    except (OSError, HTTPException, UnicodeError, json.JSONDecodeError):
        raise ReleaseSyncError(
            f"GitHub release lookup failed for {repository}."
        ) from None

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
        or payload.get("draft") is not False
        or payload.get("prerelease") is not False
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
    *,
    originals: dict[Path, FileSnapshot] | None = None,
) -> dict[Path, str]:
    resolved_paths = README_PATHS if paths is None else paths
    snapshots = {} if originals is None else originals

    for locale, path in resolved_paths.items():
        if not path.is_file():
            raise ReleaseSyncError(
                f"Profile README missing for locale {locale}: {path}"
            )
        if path not in snapshots:
            snapshots[path] = read_snapshot(path)

    updated: dict[Path, str] = {}
    for path in resolved_paths.values():
        text = snapshots[path].text
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
        originals: dict[Path, FileSnapshot] = {}
        updated = build_updated_readmes(releases, originals=originals)
    except (ReleaseSyncError, BilingualWriteError, OSError, UnicodeError) as exc:
        print(f"Release sync aborted: {exc}", file=sys.stderr)
        print("Profile READMEs left unchanged.", file=sys.stderr)
        return 1

    try:
        changed_paths = write_bilingual(originals, updated)
    except (BilingualWriteError, OSError, UnicodeError) as exc:
        print(f"Release sync aborted: {exc}", file=sys.stderr)
        return 1
    if not changed_paths:
        print("Selected Projects releases already up to date.")
        return 0

    changed = ", ".join(str(path) for path in changed_paths)
    print(f"Synchronized official Selected Projects releases in {changed}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
