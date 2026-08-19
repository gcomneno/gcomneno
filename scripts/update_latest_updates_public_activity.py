#!/usr/bin/env python3
from __future__ import annotations

import sys
from datetime import datetime, timedelta, timezone

import update_latest_updates as core


PUBLIC_ACTIVITY_LOOKBACK_DAYS = 14
MAX_PUBLIC_ACTIVITY_PAGES = 3
PUBLIC_ACTIVITY_PER_PAGE = 100


def event_commit_belongs_to_owner(commit: dict, actor: dict) -> bool:
    if actor.get("login") != core.OWNER_LOGIN:
        return False

    author = commit.get("author")
    if not isinstance(author, dict):
        return False

    email = author.get("email")
    if not isinstance(email, str):
        return False

    login = core.OWNER_LOGIN.lower()
    actor_id = actor.get("id")
    accepted = {f"{login}@users.noreply.github.com"}
    if isinstance(actor_id, int):
        accepted.add(f"{actor_id}+{login}@users.noreply.github.com")

    return email.strip().lower() in accepted


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
        "commits": 0,
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
                date = core.parse_github_datetime(created_at)
            except ValueError:
                continue

            if date < cutoff:
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

            commits = payload.get("commits")
            if not isinstance(commits, list):
                continue

            repo_name = full_name.split("/", 1)[1]
            for commit in commits:
                if not isinstance(commit, dict):
                    continue
                stats["commits"] += 1
                if not event_commit_belongs_to_owner(commit, actor):
                    continue
                stats["owner_commits"] += 1

                sha = commit.get("sha")
                message = commit.get("message")
                if not isinstance(sha, str) or not sha:
                    continue
                if not isinstance(message, str):
                    continue

                parsed = core.parse_update_message(message)
                if not parsed:
                    continue
                stats["meaningful"] += 1

                kind, text = parsed
                items.append(
                    core.UpdateItem(
                        date=date,
                        repo=repo_name,
                        kind=kind,
                        text=text,
                        url=f"https://github.com/{full_name}/commit/{sha}",
                        priority=core.COMMIT_PRIORITY_BY_KIND[kind],
                    )
                )

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
