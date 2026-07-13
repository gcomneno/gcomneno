#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


README_PATH = Path("README.md")

OWNER_LOGIN = "gcomneno"
PROFILE_REPO = f"{OWNER_LOGIN}/{OWNER_LOGIN}"

VISIBLE_ITEMS = 4
LOOKBACK_DAYS = 183
MAX_REPOS = 100

FALLBACK_UPDATE = "- No automatic updates available at the moment."

UPDATE_PATTERNS: tuple[tuple[re.Pattern[str], str], ...] = (
    (re.compile(r"^docs:\s*(.+)$", re.IGNORECASE), "docs"),
    (re.compile(r"^news:\s*(.+)$", re.IGNORECASE), "news"),
    (re.compile(r"^update:\s*(.+)$", re.IGNORECASE), "update"),
    (re.compile(r"^release:\s*(.+)$", re.IGNORECASE), "release"),
    (re.compile(r"^chore\(release\):\s*(.+)$", re.IGNORECASE), "release"),
    (re.compile(r"^chore:\s*release\s+(.+)$", re.IGNORECASE), "release"),
)

# Higher priority wins when multiple updates share repo + day.
PRIORITY_RELEASE_API = 4
COMMIT_PRIORITY_BY_KIND = {
    "release": 3,
    "update": 2,
    "news": 1,
    "docs": 0,
}

LABEL_BY_KIND = {
    "release": "Release",
    "update": "Update",
    "news": "News",
    "docs": "Docs",
}

API_HAD_FAILURE = False


@dataclass(frozen=True)
class UpdateItem:
    date: datetime
    repo: str
    kind: str
    text: str
    url: str
    priority: int = 0


def parse_github_datetime(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def github_get_json(url: str) -> object | None:
    global API_HAD_FAILURE

    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "gcomneno-profile-updates",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = Request(url, headers=headers)

    try:
        with urlopen(request, timeout=20) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        API_HAD_FAILURE = True
        print(f"warning: GitHub API returned {exc.code} for {url}", file=sys.stderr)
        return None
    except URLError as exc:
        API_HAD_FAILURE = True
        print(f"warning: GitHub API failed for {url}: {exc}", file=sys.stderr)
        return None


def parse_update_message(message: str) -> tuple[str, str] | None:
    first_line = message.splitlines()[0].strip()

    for pattern, kind in UPDATE_PATTERNS:
        match = pattern.match(first_line)
        if match:
            return kind, match.group(1).strip()

    return None


def discover_public_repositories() -> list[str]:
    repos: list[str] = []
    page = 1
    cutoff = datetime.now(timezone.utc) - timedelta(days=LOOKBACK_DAYS)

    while len(repos) < MAX_REPOS:
        url = (
            f"https://api.github.com/users/{OWNER_LOGIN}/repos"
            f"?type=owner&sort=pushed&direction=desc&per_page=100&page={page}"
        )
        payload = github_get_json(url)
        if not isinstance(payload, list) or not payload:
            break

        for repo in payload:
            if not isinstance(repo, dict):
                continue

            full_name = repo.get("full_name")
            owner = repo.get("owner", {})
            owner_login = owner.get("login") if isinstance(owner, dict) else None

            if not isinstance(full_name, str) or owner_login != OWNER_LOGIN:
                continue
            if full_name == PROFILE_REPO:
                continue
            if repo.get("private") is True:
                continue
            if repo.get("archived") is True:
                continue
            if repo.get("disabled") is True:
                continue

            pushed_at = repo.get("pushed_at")
            if isinstance(pushed_at, str):
                try:
                    if parse_github_datetime(pushed_at) < cutoff:
                        continue
                except ValueError:
                    pass

            repos.append(full_name)
            if len(repos) >= MAX_REPOS:
                break

        if len(payload) < 100:
            break
        page += 1

    return repos


def is_own_commit(commit_obj: dict) -> bool:
    author = commit_obj.get("author")
    if isinstance(author, dict) and author.get("login") == OWNER_LOGIN:
        return True

    committer = commit_obj.get("committer")
    return isinstance(committer, dict) and committer.get("login") == OWNER_LOGIN


def release_label(tag_name: str, name: str | None) -> str:
    cleaned_name = (name or "").strip()
    cleaned_tag = tag_name.strip()

    if cleaned_name and cleaned_name != cleaned_tag:
        return cleaned_name

    return cleaned_tag


def fetch_repo_releases(repo: str) -> list[UpdateItem]:
    cutoff = datetime.now(timezone.utc) - timedelta(days=LOOKBACK_DAYS)
    items: list[UpdateItem] = []
    page = 1
    repo_name = repo.split("/", 1)[1]

    while True:
        url = f"https://api.github.com/repos/{repo}/releases?per_page=100&page={page}"
        releases = github_get_json(url)

        if not isinstance(releases, list):
            return items
        if not releases:
            break

        for release in releases:
            if not isinstance(release, dict) or release.get("draft") is True:
                continue

            published_at = release.get("published_at")
            tag_name = release.get("tag_name")
            html_url = release.get("html_url")

            if not isinstance(published_at, str) or not isinstance(tag_name, str):
                continue
            if not isinstance(html_url, str):
                continue

            try:
                date = parse_github_datetime(published_at)
            except ValueError:
                continue

            if date < cutoff:
                continue

            name = release.get("name")
            items.append(
                UpdateItem(
                    date=date,
                    repo=repo_name,
                    kind="release",
                    text=release_label(tag_name, name if isinstance(name, str) else None),
                    url=html_url,
                    priority=PRIORITY_RELEASE_API,
                )
            )

        if len(releases) < 100:
            break
        page += 1

    return items


def fetch_repo_commit_updates(repo: str) -> list[UpdateItem]:
    since = (datetime.now(timezone.utc) - timedelta(days=LOOKBACK_DAYS)).isoformat()
    items: list[UpdateItem] = []
    page = 1
    repo_name = repo.split("/", 1)[1]

    while True:
        url = (
            f"https://api.github.com/repos/{repo}/commits"
            f"?since={since}&per_page=100&page={page}"
        )
        commits = github_get_json(url)

        if not isinstance(commits, list):
            return items
        if not commits:
            break

        for commit_obj in commits:
            if not isinstance(commit_obj, dict) or not is_own_commit(commit_obj):
                continue

            try:
                commit = commit_obj["commit"]
                parsed = parse_update_message(commit["message"])
                if not parsed:
                    continue

                kind, text = parsed
                date = parse_github_datetime(commit["committer"]["date"])
                html_url = commit_obj["html_url"]
                priority = COMMIT_PRIORITY_BY_KIND[kind]

                items.append(
                    UpdateItem(
                        date=date,
                        repo=repo_name,
                        kind=kind,
                        text=text,
                        url=html_url,
                        priority=priority,
                    )
                )
            except (KeyError, TypeError, ValueError):
                continue

        if len(commits) < 100:
            break
        page += 1

    return items


def dedupe_updates(items: list[UpdateItem]) -> list[UpdateItem]:
    deduped: dict[tuple[str, str], UpdateItem] = {}

    for item in items:
        key = (item.repo, item.date.strftime("%Y-%m-%d"))
        existing = deduped.get(key)

        if existing is None:
            deduped[key] = item
            continue

        if item.priority > existing.priority:
            deduped[key] = item
            continue

        if item.priority == existing.priority and item.date > existing.date:
            deduped[key] = item

    return sorted(deduped.values(), key=lambda item: item.date, reverse=True)


def collect_updates() -> list[UpdateItem]:
    repos = discover_public_repositories()
    print(f"Discovered {len(repos)} recently updated public repository/repositories.", file=sys.stderr)

    items: list[UpdateItem] = []
    for repo in repos:
        items.extend(fetch_repo_releases(repo))
        items.extend(fetch_repo_commit_updates(repo))

    merged = dedupe_updates(items)
    counts = {kind: sum(1 for item in merged if item.kind == kind) for kind in LABEL_BY_KIND}
    print(
        "Collected "
        f"{len(merged)} update(s) after merge "
        f"({counts['release']} release, {counts['update']} update, "
        f"{counts['news']} news, {counts['docs']} docs).",
        file=sys.stderr,
    )

    return merged


def render_update_item(item: UpdateItem) -> str:
    date = item.date.strftime("%Y-%m-%d")
    label = LABEL_BY_KIND[item.kind]

    return (
        f"- **{date}** · `{item.repo}` · **{label}:** "
        f"[{item.text}]({item.url})"
    )


def render_updates(items: list[UpdateItem]) -> str:
    if not items:
        return FALLBACK_UPDATE

    visible_items = items[:VISIBLE_ITEMS]
    hidden_items = items[VISIBLE_ITEMS:]
    lines = [render_update_item(item) for item in visible_items]

    if hidden_items:
        lines.extend(
            [
                "",
                "<details>",
                "<summary>More updates from the last 6 months</summary>",
                "",
            ]
        )
        lines.extend(render_update_item(item) for item in hidden_items)
        lines.extend(["", "</details>"])

    return "\n".join(lines)


def replace_updates_block(readme: str, updates_markdown: str) -> str:
    start_marker = "<!-- updates:start -->"
    end_marker = "<!-- updates:end -->"

    if start_marker not in readme or end_marker not in readme:
        raise SystemExit("README.md non contiene i marker updates:start / updates:end.")

    start = readme.index(start_marker) + len(start_marker)
    end = readme.index(end_marker, start)
    return readme[:start] + "\n\n" + updates_markdown + "\n\n" + readme[end:]


def main() -> int:
    items = collect_updates()

    if API_HAD_FAILURE:
        print("GitHub API failure detected. README.md left unchanged.")
        return 0

    readme = README_PATH.read_text(encoding="utf-8")
    updates_markdown = render_updates(items)
    updated = replace_updates_block(readme, updates_markdown)

    if updated == readme:
        print("Latest Updates already up to date.")
        return 0

    README_PATH.write_text(updated, encoding="utf-8")

    if items:
        visible = min(len(items), VISIBLE_ITEMS)
        print(f"Updated README.md with {len(items)} item(s), {visible} visible.")
    else:
        print("No tagged news/update/release updates found. Fallback written to README.md.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
