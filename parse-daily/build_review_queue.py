#!/usr/bin/env python3
"""Parse tech-memo daily news/IOCs and build an actor-linked review queue."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any

from daily_common import (
    ActorRegistry,
    assess_activity_claim,
    date_from_path,
    extract_artifacts,
    is_file_like,
    is_safe_structured_match,
    load_json,
    name_candidates,
    parse_news_file,
    qualifier_confidence,
    read_ioc_csv,
    stable_digest,
    utc_now,
    write_json_atomic,
)


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent

# 名前候補ごとに保持する記事コンテキストの上限。queueの肥大化を防ぐ。
NAME_CANDIDATE_CONTEXT_LIMIT = 5


def git_commit(source_root: Path) -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=source_root,
        text=True,
        capture_output=True,
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else "unknown"


def git_commit_timestamp(source_root: Path) -> str | None:
    result = subprocess.run(
        ["git", "show", "-s", "--format=%cI", "HEAD"],
        cwd=source_root,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        return None
    return result.stdout.strip().replace("+00:00", "Z") or None


def in_range(value: str | None, since: str | None, until: str | None) -> bool:
    if not value:
        return not since and not until
    return (not since or value >= since) and (not until or value <= until)


def article_lookup(articles: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for article in articles:
        for value in (article["url"], article["primary_url"]):
            result.setdefault(value.rstrip("/"), article)
    return result


def record_id(slug: str, activity_reference: str) -> str:
    return f"daily-record--{stable_digest(slug, activity_reference)[:24]}"


def source_entry(url: str, source_path: str, source_type: str) -> dict[str, str]:
    return {
        "url": url,
        "source_path": source_path,
        "source_type": source_type,
    }


def add_unique_source(record: dict[str, Any], source: dict[str, str]) -> None:
    existing = {
        item["url"] for item in record.setdefault("sources", [])
    }
    if source["url"] not in existing:
        record["sources"].append(source)


def add_capability_candidate(record: dict[str, Any], raw_value: str) -> None:
    existing = {
        item["name"].casefold() for item in record.setdefault("capability_decisions", [])
    }
    for name in re.split(r"[,;|]", raw_value):
        name = name.strip()
        key = name.casefold()
        if key in {"", "unknown", "n/a", "na", "none", "知られていない"}:
            continue
        file_match = re.search(
            r"([^/\\\s]+\.(?:exe|dll|sys|ps1|bat|cmd|js|jse|vbs|hta|lnk|"
            r"docm?|xlsm?|pptm?|pdf|zip|rar|7z|apk|dmg|pkg|sh|py))$",
            name,
            flags=re.IGNORECASE,
        )
        if is_file_like(name) or file_match:
            file_name = file_match.group(1) if file_match else name
            artifact_key = ("file-name", file_name)
            artifact_existing = {
                (item["artifact_type"], item["value"])
                for item in record.setdefault("artifacts", [])
            }
            if artifact_key not in artifact_existing:
                record["artifacts"].append(
                    {
                        "artifact_type": "file-name",
                        "value": file_name,
                        "context": f"malware列: {raw_value}",
                        "review_status": "pending",
                    }
                )
            continue
        if key not in existing:
            record["capability_decisions"].append(
                {
                    "name": name,
                    "status": "pending",
                    "reason": "malware列の値。一次資料で直接利用を確認する必要がある。",
                }
            )
            existing.add(key)


def apply_decision(record: dict[str, Any], decisions: dict[str, Any]) -> None:
    key = f"{record['actor']['slug']}|{record['activity']['activity_reference']}"
    decision = decisions.get(key)
    if not decision:
        return
    for field in ("review_status", "confidence", "review_notes", "activity_type"):
        if field in decision:
            record[field] = decision[field]
    if "activity_period" in decision:
        record["activity_period"] = decision["activity_period"]
    capability_overrides = {
        item["name"].casefold(): item
        for item in decision.get("capability_decisions", [])
    }
    matched_capabilities: set[str] = set()
    for item in record.get("capability_decisions", []):
        override = capability_overrides.get(item["name"].casefold())
        if override:
            item.update(override)
            matched_capabilities.add(item["name"].casefold())
    for name in sorted(capability_overrides.keys() - matched_capabilities):
        record.setdefault("decision_issues", []).append(
            f"Capability判断の対象が入力に存在しない: {name}"
        )
    approved_artifacts = {
        (item["artifact_type"], item["value"])
        for item in decision.get("approved_artifacts", [])
    }
    matched_artifacts: set[tuple[str, str]] = set()
    for item in record.get("artifacts", []):
        artifact_key = (item["artifact_type"], item["value"])
        if artifact_key in approved_artifacts:
            item["review_status"] = "approved"
            matched_artifacts.add(artifact_key)
        else:
            item["review_status"] = item.get("review_status", "pending")
    for artifact_type, value in sorted(approved_artifacts - matched_artifacts):
        record.setdefault("decision_issues", []).append(
            f"artifact判断の対象が入力に存在しない: {artifact_type}={value}"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=HERE / "config.json")
    parser.add_argument("--source-root", type=Path, default=HERE / ".cache" / "tech-memo")
    parser.add_argument("--profiles-root", type=Path, default=REPO_ROOT / "profiles")
    parser.add_argument("--output", type=Path, default=HERE / "output" / "review-queue.json")
    parser.add_argument("--since", help="include dates on/after YYYY-MM-DD")
    parser.add_argument("--until", help="include dates on/before YYYY-MM-DD")
    parser.add_argument(
        "--decisions",
        type=Path,
        default=HERE / "review-decisions.json",
        help="curated review decisions keyed by actor slug and activity reference",
    )
    parser.add_argument(
        "--approve-structured",
        action="store_true",
        help="approve only unique exact actor matches from structured IOC actor fields",
    )
    args = parser.parse_args()

    config = load_json(args.config)
    decisions = load_json(args.decisions) if args.decisions.exists() else {}
    reference_aliases = config.get("activity_reference_aliases", {})
    source_root = args.source_root.resolve()
    profiles_root = args.profiles_root.resolve()
    news_root = source_root / config["source"]["news_path"]
    iocs_root = source_root / config["source"]["iocs_path"]
    if not news_root.is_dir() or not iocs_root.is_dir():
        raise SystemExit("Source data is missing. Run sync_daily.py or pass --source-root.")

    registry = ActorRegistry(profiles_root, config)
    articles: list[dict[str, Any]] = []
    parse_errors: list[dict[str, str]] = []
    for path in sorted(news_root.rglob("*.md")):
        date = date_from_path(path)
        if not in_range(date, args.since, args.until):
            continue
        relative = path.relative_to(source_root).as_posix()
        try:
            articles.extend(parse_news_file(path, relative))
        except Exception as exc:
            parse_errors.append({"path": relative, "error": f"{type(exc).__name__}: {exc}"})
    by_url = article_lookup(articles)

    records: dict[tuple[str, str], dict[str, Any]] = {}
    unmatched_actor_values: Counter[str] = Counter()
    ignored = {
        value.casefold() for value in config["matching"].get("ignored_actor_values", [])
    }

    # IOCを伴わない記事はIOC CSVのactor列に現れず unmatched_actor_values で検知できない。
    # 発見用途の第2チャンネルとして、本文から未登録のアクター名候補を収集する。
    ignored_names = config["matching"].get("ignored_name_candidates", [])
    name_candidate_counts: Counter[str] = Counter()
    name_candidate_articles: dict[str, list[dict[str, str]]] = {}
    for article in articles:
        for value in name_candidates(article, registry, ignored_names):
            name_candidate_counts[value] += 1
            context = name_candidate_articles.setdefault(value, [])
            if len(context) < NAME_CANDIDATE_CONTEXT_LIMIT:
                context.append(
                    {
                        "news_date": article.get("news_date") or "",
                        "news_path": article.get("news_path") or "",
                        "title": article.get("title") or "",
                        "primary_url": article.get("primary_url") or "",
                    }
                )

    for path in sorted(iocs_root.rglob("*.csv")):
        file_date = date_from_path(path)
        if not in_range(file_date, args.since, args.until):
            continue
        relative = path.relative_to(source_root).as_posix()
        try:
            rows = read_ioc_csv(path, config)
        except Exception as exc:
            parse_errors.append({"path": relative, "error": f"{type(exc).__name__}: {exc}"})
            continue
        for row in rows:
            if not row["type"] or not row["value"]:
                parse_errors.append(
                    {"path": relative, "error": f"row {row['row']}: unsupported/empty IOC"}
                )
                continue
            matches = registry.exact(row["actor"], "ioc-actor-field")
            if not matches:
                if row["actor"].casefold() not in ignored:
                    unmatched_actor_values[row["actor"]] += 1
                continue
            match = matches[0]
            reference = row["reference"] or f"tech-memo:{relative}"
            activity_reference = reference_aliases.get(reference, reference)
            article = by_url.get(activity_reference.rstrip("/"))
            news_path = article["news_path"] if article else relative
            key = (match.slug, activity_reference)
            if key not in records:
                safe = is_safe_structured_match(row["actor"], match)
                records[key] = {
                    "record_id": record_id(*key),
                    "review_status": "approved" if args.approve_structured and safe else "pending",
                    "suggested_action": "approve" if safe else "review",
                    "actor": {
                        "slug": match.slug,
                        "canonical_name": match.name,
                        "matched_term": match.term,
                        "scope": match.scope,
                        "match_confidence": match.confidence,
                        "reason": match.reason,
                        "raw_value": row["actor"],
                    },
                    "activity": {
                        "title": article["title"] if article else f"{match.name}の日次IOC観測",
                        "summary": article["summary"] if article else row["description"],
                        "news_date": article["news_date"] if article else file_date,
                        "news_url": article["url"] if article else "",
                        "primary_url": activity_reference,
                        "activity_reference": activity_reference,
                        "news_path": news_path,
                    },
                    "confidence": qualifier_confidence(row["actor"], row["confidence"]),
                    "iocs": [],
                    "artifacts": extract_artifacts(article["body"]) if article else [],
                    "sources": [],
                    "capability_decisions": [],
                    "review_notes": "",
                    "activity_claim": {
                        "assessment": "structured-actor-field",
                        "actor_role": "operator",
                        "match_location": "ioc-actor-field",
                        "evidence_text": row["actor"],
                        "reasons": [
                            "tech-memo IOC CSVの構造化actor列に記載されている"
                        ],
                        "suggested_confidence": qualifier_confidence(
                            row["actor"], row["confidence"]
                        ),
                    },
                }
                add_unique_source(
                    records[key],
                    source_entry(
                        activity_reference,
                        news_path,
                        "primary-report" if article else "ioc-reference",
                    ),
                )
            add_unique_source(
                records[key],
                source_entry(reference, relative, "ioc-reference"),
            )
            item = dict(row)
            item["source_path"] = relative
            item["malware_refs"] = registry.malware_refs(match.slug, [row["malware"]])
            records[key]["iocs"].append(item)
            add_capability_candidate(records[key], row["malware"])

    structured_keys = {
        (record["actor"]["slug"], record["activity"]["activity_reference"].rstrip("/"))
        for record in records.values()
    }
    for article in articles:
        for match in registry.mentions(article["title"], article["body"]):
            primary = reference_aliases.get(article["primary_url"], article["primary_url"])
            if (match.slug, primary.rstrip("/")) in structured_keys:
                continue
            key = (match.slug, primary)
            if key in records:
                continue
            records[key] = {
                "record_id": record_id(*key),
                "review_status": "pending",
                "suggested_action": "review",
                "actor": {
                    "slug": match.slug,
                    "canonical_name": match.name,
                    "matched_term": match.term,
                    "scope": match.scope,
                    "match_confidence": match.confidence,
                    "reason": match.reason,
                    "raw_value": match.term,
                },
                "activity": {
                    "title": article["title"],
                    "summary": article["summary"],
                    "news_date": article["news_date"],
                    "news_url": article["url"],
                    "primary_url": primary,
                    "activity_reference": primary,
                    "news_path": article["news_path"],
                },
                "confidence": "medium" if match.reason == "news-title" else "low",
                "iocs": [],
                "artifacts": extract_artifacts(article["body"]),
                "sources": [
                    source_entry(primary, article["news_path"], "primary-report")
                ],
                "capability_decisions": [],
                "review_notes": "",
                "activity_claim": assess_activity_claim(
                    match,
                    article["title"],
                    article["body"],
                    config,
                ),
            }

    for record in records.values():
        apply_decision(record, decisions)
        record["sources"].sort(key=lambda item: (item["url"], item["source_path"]))
        record["capability_decisions"].sort(key=lambda item: item["name"].casefold())
    record_decision_keys = {
        f"{record['actor']['slug']}|{record['activity']['activity_reference']}"
        for record in records.values()
    }
    decision_issues = (
        [
            f"入力に対応する活動がないreview decision: {key}"
            for key in sorted(set(decisions) - record_decision_keys)
        ]
        if not args.since and not args.until
        else []
    )

    ordered = sorted(
        records.values(),
        key=lambda item: (
            item["activity"].get("news_date") or "",
            item["actor"]["slug"],
            item["record_id"],
        ),
    )
    status_counts = Counter(item["review_status"] for item in ordered)
    decision_issue_count = len(decision_issues) + sum(
        len(item.get("decision_issues", [])) for item in ordered
    )
    queue = {
        "schema_version": "2.0.0",
        "generated_at": git_commit_timestamp(source_root) or utc_now(),
        "source": {
            "repository": config["source"]["repository_full_name"],
            "branch": config["source"]["branch"],
            "commit": git_commit(source_root),
            "root": str(source_root),
            "since": args.since,
            "until": args.until,
        },
        "statistics": {
            "news_files": len(
                [
                    path
                    for path in news_root.rglob("*.md")
                    if in_range(date_from_path(path), args.since, args.until)
                ]
            ),
            "articles": len(articles),
            "records": len(ordered),
            "approved": status_counts["approved"],
            "pending": status_counts["pending"],
            "ioc_observations": sum(len(item["iocs"]) for item in ordered),
            "artifact_candidates": sum(len(item["artifacts"]) for item in ordered),
            "unmatched_actor_values": sum(unmatched_actor_values.values()),
            "unmatched_name_candidates": len(name_candidate_counts),
            "parse_errors": len(parse_errors),
            "decision_issues": decision_issue_count,
        },
        "unmatched_actor_values": [
            {"value": value, "observations": count}
            for value, count in unmatched_actor_values.most_common()
        ],
        "unmatched_name_candidates": [
            {
                "value": value,
                "articles": count,
                "detected_via": "news-body",
                "sources": name_candidate_articles.get(value, []),
            }
            for value, count in name_candidate_counts.most_common()
        ],
        "parse_errors": parse_errors,
        "decision_issues": decision_issues,
        "records": ordered,
    }
    write_json_atomic(args.output, queue)
    print(json.dumps(queue["statistics"], ensure_ascii=False, indent=2))
    return 1 if parse_errors or decision_issue_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
