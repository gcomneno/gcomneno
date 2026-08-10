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


README_PATHS = {
    "en": Path("README.md"),
    "it": Path("README.it.md"),
}
DEFAULT_LOCALE = "en"

OWNER_LOGIN = "gcomneno"
PROFILE_REPO = f"{OWNER_LOGIN}/{OWNER_LOGIN}"

VISIBLE_ITEMS = 4
MAX_RENDERED_ITEMS = 100
LOOKBACK_DAYS = 183
MAX_REPOS = 100

UI_BY_LOCALE = {
    "en": {
        "fallback": "- No automatic updates available at the moment.",
        "details_summary": "More recent meaningful updates",
        "omitted": (
            "_Showing the {limit} most recent meaningful updates; "
            "{count} older update(s) omitted._"
        ),
    },
    "it": {
        "fallback": (
            "- Al momento non sono disponibili aggiornamenti automatici."
        ),
        "details_summary": (
            "Altri aggiornamenti recenti e significativi"
        ),
        "omitted": (
            "_Sono mostrati i {limit} aggiornamenti significativi "
            "più recenti; {count} aggiornamenti precedenti "
            "sono stati omessi._"
        ),
    },
}

UPDATE_PATTERNS: tuple[tuple[re.Pattern[str], str], ...] = (
    (
        re.compile(
            r"^docs(?:\([^)]+\))?!?:\s*(.+)$",
            re.IGNORECASE,
        ),
        "docs",
    ),
    (
        re.compile(
            r"^news(?:\([^)]+\))?!?:\s*(.+)$",
            re.IGNORECASE,
        ),
        "news",
    ),
    (
        re.compile(
            r"^update(?:\([^)]+\))?!?:\s*(.+)$",
            re.IGNORECASE,
        ),
        "update",
    ),
    (
        re.compile(
            r"^release(?:\([^)]+\))?!?:\s*(.+)$",
            re.IGNORECASE,
        ),
        "release",
    ),
    (
        re.compile(
            r"^chore\(release\)!?:\s*(.+)$",
            re.IGNORECASE,
        ),
        "release",
    ),
    (
        re.compile(
            r"^chore!?:\s*release\s+(.+)$",
            re.IGNORECASE,
        ),
        "release",
    ),
)

CONVENTIONAL_UPDATE_PATTERN = re.compile(
    (
        r"^(?P<type>"
        r"feat|fix|refactor|perf|security"
        r")"
        r"(?:\([^)]+\))?!?:\s*"
        r"(?P<text>.+)$"
    ),
    re.IGNORECASE,
)

CONVENTIONAL_KIND_BY_TYPE = {
    "feat": "feature",
    "fix": "fix",
    "refactor": "refactor",
    "perf": "performance",
    "security": "security",
}

IGNORED_COMMIT_PATTERN = re.compile(
    (
        r"^(?:"
        r"chore|ci|build|style|test|tests|deps|"
        r"maintenance|housekeeping"
        r")"
        r"(?:\([^)]+\))?"
        r"(?:!?:|\b)"
    ),
    re.IGNORECASE,
)

IGNORED_MESSAGE_PATTERNS = (
    re.compile(r"^merge(?:\s|:)", re.IGNORECASE),
    re.compile(r"^bump(?:\s|:)", re.IGNORECASE),
    re.compile(
        r"^auto(?:matic)? update(?:\s|:)",
        re.IGNORECASE,
    ),
)

PRIORITY_RELEASE_API = 10

COMMIT_PRIORITY_BY_KIND = {
    "release": 9,
    "security": 8,
    "feature": 7,
    "fix": 6,
    "performance": 5,
    "refactor": 4,
    "update": 3,
    "news": 2,
    "development": 1,
    "docs": 0,
}

KIND_LABELS_BY_LOCALE = {
    "en": {
        "release": "Release",
        "security": "Security",
        "feature": "Feature",
        "fix": "Fix",
        "performance": "Performance",
        "refactor": "Refactor",
        "update": "Update",
        "news": "News",
        "development": "Development",
        "docs": "Docs",
    },
    "it": {
        "release": "Release",
        "security": "Sicurezza",
        "feature": "Funzionalità",
        "fix": "Correzione",
        "performance": "Prestazioni",
        "refactor": "Refactoring",
        "update": "Aggiornamento",
        "news": "Novità",
        "development": "Sviluppo",
        "docs": "Documentazione",
    },
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
    """Classifica un commit significativo per la vetrina."""

    lines = message.splitlines()

    if not lines:
        return None

    first_line = lines[0].strip()

    if not first_line:
        return None

    # Le release dichiarate come chore restano eventi
    # pubblicabili e vengono riconosciute prima del filtro.
    for pattern, kind in UPDATE_PATTERNS:
        match = pattern.match(first_line)
        if match:
            return kind, match.group(1).strip()

    if IGNORED_COMMIT_PATTERN.match(first_line):
        return None

    if any(
        pattern.match(first_line)
        for pattern in IGNORED_MESSAGE_PATTERNS
    ):
        return None

    conventional = CONVENTIONAL_UPDATE_PATTERN.match(
        first_line
    )

    if conventional:
        commit_type = conventional.group(
            "type"
        ).lower()
        return (
            CONVENTIONAL_KIND_BY_TYPE[commit_type],
            conventional.group("text").strip(),
        )

    # I messaggi non convenzionali sono significativi
    # per impostazione predefinita.
    return "development", first_line


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


def dedupe_updates(
    items: list[UpdateItem],
) -> list[UpdateItem]:
    """
    Elimina soltanto duplicati reali.

    Tutti i commit significativi restano visibili, anche
    quando appartengono allo stesso repository e giorno.
    Una release ottenuta dall'API sostituisce soltanto
    l'eventuale commit di annuncio della stessa giornata.
    """

    release_api_days = {
        (
            item.repo,
            item.date.strftime("%Y-%m-%d"),
        )
        for item in items
        if (
            item.kind == "release"
            and item.priority == PRIORITY_RELEASE_API
        )
    }

    seen_urls: set[str] = set()
    deduped: list[UpdateItem] = []

    ordered = sorted(
        items,
        key=lambda item: (
            item.date,
            item.priority,
        ),
        reverse=True,
    )

    for item in ordered:
        if item.url in seen_urls:
            continue

        day_key = (
            item.repo,
            item.date.strftime("%Y-%m-%d"),
        )

        if (
            item.kind == "release"
            and item.priority < PRIORITY_RELEASE_API
            and day_key in release_api_days
        ):
            continue

        seen_urls.add(item.url)
        deduped.append(item)

    return deduped


def collect_updates() -> list[UpdateItem]:
    repos = discover_public_repositories()
    print(f"Discovered {len(repos)} recently updated public repository/repositories.", file=sys.stderr)

    items: list[UpdateItem] = []
    for repo in repos:
        items.extend(fetch_repo_releases(repo))
        items.extend(fetch_repo_commit_updates(repo))

    merged = dedupe_updates(items)
    counts = {
        kind: sum(
            1
            for item in merged
            if item.kind == kind
        )
        for kind in KIND_LABELS_BY_LOCALE[DEFAULT_LOCALE]
    }
    count_summary = ", ".join(
        f"{count} {kind}"
        for kind, count in counts.items()
        if count
    )

    print(
        "Collected "
        f"{len(merged)} meaningful update(s) "
        f"after deduplication ({count_summary}).",
        file=sys.stderr,
    )

    return merged


def locale_ui(locale: str) -> dict[str, str]:
    try:
        return UI_BY_LOCALE[locale]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported profile locale: {locale}"
        ) from exc


def locale_labels(locale: str) -> dict[str, str]:
    try:
        return KIND_LABELS_BY_LOCALE[locale]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported profile locale: {locale}"
        ) from exc


def render_update_item(
    item: UpdateItem,
    locale: str = DEFAULT_LOCALE,
) -> str:
    date = item.date.strftime("%Y-%m-%d")
    label = locale_labels(locale)[item.kind]

    return (
        f"- **{date}** · `{item.repo}` · **{label}:** "
        f"[{item.text}]({item.url})"
    )


def render_updates(
    items: list[UpdateItem],
    locale: str = DEFAULT_LOCALE,
) -> str:
    """
    Renderizza una vetrina localizzata e limitata agli
    aggiornamenti significativi più recenti.

    I titoli originali di commit e release restano invariati.
    Cambiano soltanto etichette e testo dell'interfaccia.
    """

    ui = locale_ui(locale)

    if not items:
        return ui["fallback"]

    rendered_items = items[:MAX_RENDERED_ITEMS]
    visible_items = rendered_items[:VISIBLE_ITEMS]
    hidden_items = rendered_items[VISIBLE_ITEMS:]
    omitted_count = len(items) - len(rendered_items)

    lines = [
        render_update_item(item, locale)
        for item in visible_items
    ]

    if hidden_items:
        lines.extend(
            [
                "",
                "<details>",
                (
                    "<summary>"
                    f"{ui['details_summary']}"
                    "</summary>"
                ),
                "",
            ]
        )
        lines.extend(
            render_update_item(item, locale)
            for item in hidden_items
        )

        if omitted_count:
            lines.extend(
                [
                    "",
                    ui["omitted"].format(
                        limit=MAX_RENDERED_ITEMS,
                        count=omitted_count,
                    ),
                ]
            )

        lines.extend(["", "</details>"])

    return "\n".join(lines)


def replace_updates_block(
    readme: str,
    updates_markdown: str,
    path: Path | None = None,
) -> str:
    start_marker = "<!-- updates:start -->"
    end_marker = "<!-- updates:end -->"
    source = str(path) if path is not None else "README"

    if start_marker not in readme or end_marker not in readme:
        raise SystemExit(
            f"{source} non contiene i marker "
            "updates:start / updates:end."
        )

    start = readme.index(start_marker) + len(start_marker)
    end = readme.index(end_marker, start)
    return (
        readme[:start]
        + "\n\n"
        + updates_markdown
        + "\n\n"
        + readme[end:]
    )


def main() -> int:
    items = collect_updates()

    if API_HAD_FAILURE:
        print(
            "GitHub API failure detected. "
            "Profile READMEs left unchanged."
        )
        return 0

    updated_by_path: dict[Path, str] = {}
    changed_paths: list[Path] = []

    for locale, path in README_PATHS.items():
        if not path.is_file():
            raise SystemExit(
                f"Profile README missing for locale {locale}: {path}"
            )

        readme = path.read_text(encoding="utf-8")
        updates_markdown = render_updates(
            items,
            locale=locale,
        )
        updated = replace_updates_block(
            readme,
            updates_markdown,
            path=path,
        )
        updated_by_path[path] = updated

        if updated != readme:
            changed_paths.append(path)

    if not changed_paths:
        print(
            "Latest Updates already up to date "
            "in both profile READMEs."
        )
        return 0

    for path in changed_paths:
        path.write_text(
            updated_by_path[path],
            encoding="utf-8",
        )

    changed = ", ".join(str(path) for path in changed_paths)

    if items:
        rendered = min(
            len(items),
            MAX_RENDERED_ITEMS,
        )
        visible = min(
            rendered,
            VISIBLE_ITEMS,
        )
        print(
            f"Updated {changed} with "
            f"{rendered} of {len(items)} "
            "meaningful item(s), "
            f"{visible} visible."
        )
    else:
        print(
            "No meaningful updates found. "
            f"Localized fallback written to {changed}."
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
