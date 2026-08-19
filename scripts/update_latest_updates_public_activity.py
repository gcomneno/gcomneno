#!/usr/bin/env python3
from __future__ import annotations

import sys
from datetime import datetime, timedelta, timezone
from urllib.parse import quote

import update_latest_updates as core


PUBLIC_ACTIVITY_LOOKBACK_DAYS = 14
MAX_PUBLIC_ACTIVITY_PAGES = 3
PUBLIC_ACTIVITY_PER_PAGE = 100
ZERO_SHA = "0" * 40


def fetch_push_event_commits(
    full_name: str,
    payload: dict,
) -> list[dict]:
    head = payload.get("head")
    before = payload.get("before")

    if not isinstance(head, str) or not head or head == ZERO_SHA:
        return []

    if not isinstance(before, str) or not before or before == ZERO_SHA:
        url = (
            f"https://api.github.com/repos/{full_name}/commits/"
            f"{quote(head, safe='')}"
        )
        commit = core.github_get_json(url)
        return [commit] if isinstance(commit, dict) else []

    url = (
        f"https://api.github.com/repos/{full_name}/compare/"
        f"{quote(before, safe='')}...{quote(head, safe='')}"
    )
    comparison = core.github_get_json(url)
    if not isinstance(comparison, dict):
        return []

    commits = comparison.get("commits")
    if not isinstance(commits, list):
        return []

    return [commit for commit in commits if isinstance(commit, dict)]


def update_item_from_commit(
    full_name: str,
    commit_obj: dict,
) -> core.UpdateItem | None:
    if not core.is_own_commit(commit_obj):
        return None

    try:
        commit = commit_obj["commit"]
        parsed = core.parse_update_message(commit["message"])
        if not parsed:
            return None

        kind, text = parsed
        date = core.parse_github_datetime(commit["committer"]["date"])
        html_url = commit_obj["html_url"]
    except (KeyError, TypeError, ValueError):
        return None

    if not isinstance(html_url, str):
        return None

    return core.UpdateItem(
        date=date,
        repo=full_name.split("/", 1)[1],
        kind=kind,
        text=text,
        url=html_url,
        priority=core.COMMIT_PRIORITY_BY_KIND[kind],
    )


def fetch_public_push_activity(
    eligible_repositories: set[str],
) -> list[core.UpdateItem]:
    cutoff = datetime.now(timezone.utc) - timedelta(
        days=PUBLIC_ACTIVITY_LOOKBACK_DAYS
    )
    items: list[core.UpdateItem] = []
    stats = {
        "events": 0,
        "push_events": 0,
        "eligible_push_events": 0,
        "resolved_commits": 0,
        "owner_commits": 0,
        "meaningful": 0,
    }

    for page in range(1, MAX_PUBLIC_ACTIVITY_PAGES + 1):
        url = (
            f"https://api.github.com/users/{core.OWNER_LOGIN}/events/public"
            f"?per_page={PUBLIC_ACTIVITY_PER_PAGE}&page={page}"
        )
        events = core.github_get_json(url)

        if not isinstance(events, list):
            break
        if not events:
            break

        reached_cutoff = False
        for event in events:
            if not isinstance(event, dict):
                continue
            stats["events"] += 1

            created_at = event.get("created_at")
            if not isinstance(created_at, str):
                continue

            try:
                event_date = core.parse_github_datetime(created_at)
            except ValueError:
                continue

            if event_date < cutoff:
                reached_cutoff = True
                break

            if event.get("type") != "PushEvent":
                continue
            stats["push_events"] += 1

            actor = event.get("actor")
            repo = event.get("repo")
            payload = event.get("payload")
            if not isinstance(actor, dict):
                continue
            if not isinstance(repo, dict):
                continue
            if not isinstance(payload, dict):
                continue
            if actor.get("login") != core.OWNER_LOGIN:
                continue

            full_name = repo.get("name")
            if (
                not isinstance(full_name, str)
                or full_name not in eligible_repositories
            ):
                continue

            ref = payload.get("ref")
            if not isinstance(ref, str) or not ref.startswith("refs/heads/"):
                continue
            stats["eligible_push_events"] += 1

            commits = fetch_push_event_commits(full_name, payload)
            stats["resolved_commits"] += len(commits)

            for commit_obj in commits:
                if core.is_own_commit(commit_obj):
                    stats["owner_commits"] += 1

                item = update_item_from_commit(full_name, commit_obj)
                if item is None:
                    continue

                stats["meaningful"] += 1
                items.append(item)

        if reached_cutoff or len(events) < PUBLIC_ACTIVITY_PER_PAGE:
            break

    print(
        "Public activity scan: "
        + ", ".join(f"{name}={value}" for name, value in stats.items()),
        file=sys.stderr,
    )
    return items


def collect_updates() -> list[core.UpdateItem]:
    repos = core.discover_public_repositories()
    print(
        f"Discovered {len(repos)} recently updated public repository/repositories.",
        file=sys.stderr,
    )

    items: list[core.UpdateItem] = []
    for repo in repos:
        items.extend(core.fetch_repo_releases(repo))
        items.extend(core.fetch_repo_commit_updates(repo))

    stable_urls = {item.url for item in items}
    activity_items = fetch_public_push_activity(set(repos))
    supplemental = [
        item for item in activity_items if item.url not in stable_urls
    ]
    items.extend(supplemental)

    merged = core.dedupe_updates(items)
    counts = {
        kind: sum(1 for item in merged if item.kind == kind)
        for kind in core.KIND_LABELS_BY_LOCALE[core.DEFAULT_LOCALE]
    }
    count_summary = ", ".join(
        f"{count} {kind}"
        for kind, count in counts.items()
        if count
    )

    print(
        "Collected "
        f"{len(merged)} meaningful update(s) after deduplication "
        f"({count_summary}); "
        f"{len(supplemental)} supplemental public branch item(s).",
        file=sys.stderr,
    )
    return merged


def main() -> int:
    original_collect_updates = core.collect_updates
    core.collect_updates = collect_updates
    try:
        return core.main()
    finally:
        core.collect_updates = original_collect_updates


if __name__ == "__main__":
    raise SystemExit(main())
