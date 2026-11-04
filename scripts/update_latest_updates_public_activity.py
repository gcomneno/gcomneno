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
        if head != ZERO_SHA:
            core.record_api_failure("malformed push head metadata.")
        return []

    if before is not None and not isinstance(before, str):
        core.record_api_failure("malformed push comparison base metadata.")
        return []

    if not before or before == ZERO_SHA:
        url = (
            f"https://api.github.com/repos/{full_name}/commits/"
            f"{quote(head, safe='')}"
        )
        commit = core.github_get_json(url)
        if core.API_HAD_FAILURE:
            return []
        if not isinstance(commit, dict):
            core.record_api_failure("malformed push commit response.")
            return []
        return [commit]

    url = (
        f"https://api.github.com/repos/{full_name}/compare/"
        f"{quote(before, safe='')}...{quote(head, safe='')}"
    )
    comparison = core.github_get_json(url)
    if core.API_HAD_FAILURE:
        return []
    if not isinstance(comparison, dict):
        core.record_api_failure("malformed push comparison response.")
        return []

    commits = comparison.get("commits")
    if not isinstance(commits, list) or any(
        not isinstance(commit, dict) for commit in commits
    ):
        core.record_api_failure("malformed push comparison commits.")
        return []

    return commits


def update_item_from_commit(
    full_name: str,
    commit_obj: dict,
) -> core.UpdateItem | None:
    return core.update_item_from_commit(full_name, commit_obj)


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

        if core.API_HAD_FAILURE:
            return []
        if not isinstance(events, list):
            core.record_api_failure("malformed public activity page.")
            return []
        if not events:
            break

        reached_cutoff = False
        for event in events:
            if not isinstance(event, dict):
                core.record_api_failure("malformed public activity record.")
                return []
            stats["events"] += 1

            created_at = event.get("created_at")
            try:
                event_date = core.parse_github_datetime(created_at)
            except ValueError:
                core.record_api_failure("malformed public activity timestamp.")
                return []

            if event_date < cutoff:
                reached_cutoff = True
                break

            if not isinstance(event.get("type"), str):
                core.record_api_failure("malformed public activity type.")
                return []
            if event["type"] != "PushEvent":
                continue
            stats["push_events"] += 1

            actor = event.get("actor")
            repo = event.get("repo")
            payload = event.get("payload")
            if (
                not isinstance(actor, dict)
                or not isinstance(actor.get("login"), str)
                or not isinstance(repo, dict)
                or not isinstance(repo.get("name"), str)
                or not isinstance(payload, dict)
            ):
                core.record_api_failure("malformed public push metadata.")
                return []
            if actor.get("login") != core.OWNER_LOGIN:
                continue

            full_name = repo.get("name")
            if (
                not isinstance(full_name, str)
                or full_name not in eligible_repositories
            ):
                continue

            ref = payload.get("ref")
            if not isinstance(ref, str):
                core.record_api_failure("malformed public push reference.")
                return []
            if not ref.startswith("refs/heads/"):
                continue
            stats["eligible_push_events"] += 1

            commits = fetch_push_event_commits(full_name, payload)
            if core.API_HAD_FAILURE:
                return []
            stats["resolved_commits"] += len(commits)

            for commit_obj in commits:
                item = update_item_from_commit(full_name, commit_obj)
                if core.API_HAD_FAILURE:
                    return []
                if core.is_own_commit(commit_obj):
                    stats["owner_commits"] += 1

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
    if core.API_HAD_FAILURE:
        return []
    print(
        f"Discovered {len(repos)} recently updated public repository/repositories.",
        file=sys.stderr,
    )

    items: list[core.UpdateItem] = []
    for repo in repos:
        items.extend(core.fetch_repo_releases(repo))
        if core.API_HAD_FAILURE:
            return []
        items.extend(core.fetch_repo_commit_updates(repo))
        if core.API_HAD_FAILURE:
            return []

    stable_urls = {item.url for item in items}
    activity_items = fetch_public_push_activity(set(repos))
    if core.API_HAD_FAILURE:
        return []
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
