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

MAX_ITEMS = 5
SINCE_DAYS = 14
MAX_REPOS = 100

NEWS_PATTERN = re.compile(r"^(news|release):\s*(.+)$", re.IGNORECASE)


@dataclass(frozen=True)
class UpdateItem:
    date: datetime
    repo: str
    kind: str
    text: str
    url: str


def github_get_json(url: str) -> object | None:
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
        if exc.code == 404:
            print(f"info: skipping unavailable endpoint: {url}", file=sys.stderr)
        else:
            print(f"warning: GitHub API returned {exc.code} for {url}", file=sys.stderr)
        return None
    except URLError as exc:
        print(f"warning: GitHub API failed for {url}: {exc}", file=sys.stderr)
        return None


def discover_public_repositories() -> list[str]:
    repos: list[str] = []
    page = 1

    while len(repos) < MAX_REPOS:
        url = (
            f"https://api.github.com/users/{OWNER_LOGIN}/repos"
            f"?type=owner&sort=pushed&direction=desc&per_page=100&page={page}"
        )

        payload = github_get_json(url)
        if not isinstance(payload, list):
            break

        if not payload:
            break

        for repo in payload:
            if not isinstance(repo, dict):
                continue

            full_name = repo.get("full_name")
            owner = repo.get("owner", {})
            owner_login = owner.get("login") if isinstance(owner, dict) else None

            if not isinstance(full_name, str):
                continue

            if owner_login != OWNER_LOGIN:
                continue

            if full_name == PROFILE_REPO:
                continue

            if repo.get("private") is True:
                continue

            if repo.get("archived") is True:
                continue

            if repo.get("disabled") is True:
                continue

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
    if isinstance(committer, dict) and committer.get("login") == OWNER_LOGIN:
        return True

    return False


def fetch_repo_updates(repo: str) -> list[UpdateItem]:
    since = (datetime.now(timezone.utc) - timedelta(days=SINCE_DAYS)).isoformat()
    url = f"https://api.github.com/repos/{repo}/commits?since={since}&per_page=50"

    commits = github_get_json(url)
    if not isinstance(commits, list):
        return []

    items: list[UpdateItem] = []

    for commit_obj in commits:
        if not isinstance(commit_obj, dict):
            continue

        if not is_own_commit(commit_obj):
            continue

        try:
            commit = commit_obj["commit"]
            message = commit["message"].splitlines()[0].strip()
            match = NEWS_PATTERN.match(message)
            if not match:
                continue

            kind = match.group(1).lower()
            text = match.group(2).strip()
            date_raw = commit["committer"]["date"]
            html_url = commit_obj["html_url"]

            date = datetime.fromisoformat(date_raw.replace("Z", "+00:00"))

            items.append(
                UpdateItem(
                    date=date,
                    repo=repo.split("/", 1)[1],
                    kind=kind,
                    text=text,
                    url=html_url,
                )
            )
        except (KeyError, TypeError, ValueError):
            continue

    return items


def collect_updates() -> list[UpdateItem]:
    repos = discover_public_repositories()

    print(f"Discovered {len(repos)} public repository/repositories.", file=sys.stderr)

    items: list[UpdateItem] = []

    for repo in repos:
        items.extend(fetch_repo_updates(repo))

    deduped: dict[tuple[str, str], UpdateItem] = {}

    for item in items:
        key = (item.repo, item.text.lower())
        if key not in deduped or item.date > deduped[key].date:
            deduped[key] = item

    return sorted(deduped.values(), key=lambda item: item.date, reverse=True)[:MAX_ITEMS]


def render_updates(items: list[UpdateItem]) -> str:
    lines = []

    for item in items:
        date = item.date.strftime("%Y-%m-%d")
        label = "Release" if item.kind == "release" else "News"
        lines.append(
            f"- **{date}** · `{item.repo}` · **{label}:** "
            f"[{item.text}]({item.url})"
        )

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

    if not items:
        print("No tagged news/release commits found. README.md left unchanged.")
        return 0

    readme = README_PATH.read_text(encoding="utf-8")
    updates_markdown = render_updates(items)
    updated = replace_updates_block(readme, updates_markdown)

    if updated == readme:
        print("Latest Updates already up to date.")
        return 0

    README_PATH.write_text(updated, encoding="utf-8")
    print(f"Updated README.md with {len(items)} item(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
