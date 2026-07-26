#!/usr/bin/env python3
"""Apply approved daily review records to profiles and observable datasets."""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

from daily_common import (
    UNKNOWN_TIME,
    load_json,
    source_publisher,
    stable_digest,
    time_point,
    utc_now,
    write_json_atomic,
)


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
sys.path.insert(0, str(REPO_ROOT / "actor_profile" / "scripts"))
from common import (  # noqa: E402
    json_array_cell,
    normalize_observable,
    stable_id,
    stix_pattern,
)

FILE_LIKE_RE = re.compile(
    r"(?:^|\s)([^/\\\s]+\.(?:exe|dll|sys|ps1|bat|cmd|js|jse|vbs|hta|lnk|"
    r"docm?|xlsm?|pptm?|pdf|zip|rar|7z|apk|dmg|pkg|sh|py))$",
    re.IGNORECASE,
)


def source_id_for(record: dict[str, Any]) -> str:
    activity = record["activity"]
    identity = activity.get("primary_url") or activity["news_path"]
    return f"source--daily-{stable_digest(identity)[:20]}"


def activity_id_for(record: dict[str, Any]) -> str:
    return f"activity--daily-{stable_digest(record['record_id'])[:20]}"


def source_path_for(record: dict[str, Any], queue: dict[str, Any]) -> str:
    path = record["activity"].get("primary_url")
    if path:
        return path
    repository = queue["source"]["repository"]
    commit = queue["source"]["commit"]
    return f"https://github.com/{repository}/blob/{commit}/{record['activity']['news_path']}"


def profile_source(record: dict[str, Any], queue: dict[str, Any]) -> dict[str, Any]:
    activity = record["activity"]
    primary = source_path_for(record, queue)
    news_url = activity.get("news_url") or ""
    notes = (
        f"tech-memo日次収集から取込。元ファイル: {activity['news_path']}; "
        f"source commit: {queue['source']['commit']}"
    )
    if news_url and news_url != primary:
        notes += f"; 参照記事: {news_url}"
    return {
        "source_id": source_id_for(record),
        "path": primary,
        "title": activity["title"],
        "publisher": source_publisher(primary),
        "published_at": time_point(activity.get("news_date"), "daily-news-file-date"),
        "language": "unknown",
        "source_type": "osint-report",
        "tlp": "TLP:CLEAR",
        "reliability": record.get("confidence", "medium"),
        "sha256": None,
        "analyst_notes": notes,
    }


def observed_bounds(record: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    dates = sorted(
        {
            row.get("observed_date")
            for row in record.get("iocs", [])
            if time_point(row.get("observed_date"), "daily-ioc-date")["status"] == "known"
        }
    )
    if not dates:
        return dict(UNKNOWN_TIME), dict(UNKNOWN_TIME)
    return (
        time_point(dates[0], "daily-ioc-date"),
        time_point(dates[-1], "daily-ioc-date"),
    )


def activity_entry(record: dict[str, Any]) -> dict[str, Any]:
    first, last = observed_bounds(record)
    malware_refs = sorted(
        {
            ref
            for row in record.get("iocs", [])
            for ref in row.get("malware_refs", [])
        }
    )
    notes = (
        f"日次収集レコード {record['record_id']} から取込。"
        "日付はIOC観測日がある場合のみ活動の観測期間として使用し、"
        "ニュースファイルの日付とは分離した。"
    )
    return {
        "activity_id": activity_id_for(record),
        "name": record["activity"]["title"],
        "activity_type": "reported-activity",
        "first_observed": first,
        "last_observed": last,
        "description": record["activity"].get("summary") or "日次OSINTで報告された活動。",
        "target_refs": [],
        "malware_refs": malware_refs,
        "infrastructure_refs": [],
        "confidence": record.get("confidence", "medium"),
        "evidence_refs": [source_id_for(record)],
        "analyst_notes": notes,
    }


def ensure_malware_capabilities(
    profile: dict[str, Any],
    record: dict[str, Any],
) -> None:
    malware = profile["capabilities"]["malware"]
    lookup: dict[str, dict[str, Any]] = {}
    for item in malware:
        lookup[normalize_observable("artifact", item.get("name", "")).casefold()] = item
        for alias in item.get("aliases", []):
            lookup[normalize_observable("artifact", alias).casefold()] = item
    source_id = source_id_for(record)
    record_first, record_last = observed_bounds(record)
    for row in record.get("iocs", []):
        refs = set(row.get("malware_refs", []))
        raw_malware = row.get("malware", "").strip()
        if raw_malware.casefold() in {"", "unknown", "n/a", "na", "none", "知られていない"}:
            row["malware_refs"] = sorted(refs)
            continue
        for name in re.split(r"[,;|]", raw_malware):
            name = name.strip()
            key = normalize_observable("artifact", name).casefold()
            if (
                len(key) < 3
                or key in {"unknown", "n/a", "na", "none", "知られていない"}
            ):
                continue
            file_match = FILE_LIKE_RE.search(name)
            if file_match:
                artifact = {
                    "artifact_type": "file-name",
                    "value": file_match.group(1),
                    "context": f"daily IOC malware field: {raw_malware}",
                    "review_status": "approved",
                }
                if not any(
                    item.get("artifact_type") == "file-name"
                    and item.get("value") == artifact["value"]
                    for item in record.setdefault("artifacts", [])
                ):
                    record["artifacts"].append(artifact)
                continue
            item = lookup.get(key)
            if item is None:
                malware_type = row.get("malware_type", "").strip()
                types = (
                    [malware_type]
                    if malware_type.casefold() not in {"", "unknown", "n/a", "na", "none"}
                    else []
                )
                item = {
                    "id": f"malware--daily-{stable_digest(name)[:20]}",
                    "name": name,
                    "aliases": [],
                    "types": types,
                    "description": (
                        f"tech-memo日次IOCで{profile['actor']['canonical_name']}による"
                        f"使用が報告されたマルウェア。"
                    ),
                    "first_observed": record_first,
                    "last_observed": record_last,
                    "confidence": record.get("confidence", "medium"),
                    "evidence_refs": [source_id],
                    "analyst_notes": f"日次収集レコード {record['record_id']} から追加。",
                }
                malware.append(item)
                lookup[key] = item
            elif source_id not in item.get("evidence_refs", []):
                item.setdefault("evidence_refs", []).append(source_id)
                item["evidence_refs"].sort()
            refs.add(item["id"])
        row["malware_refs"] = sorted(refs)


def prune_invalid_daily_malware(profile: dict[str, Any]) -> None:
    malware = profile["capabilities"]["malware"]
    invalid_ids = {
        item["id"]
        for item in malware
        if item["id"].startswith("malware--daily-")
        and (
            len(normalize_observable("artifact", item.get("name", "")).strip()) < 3
            or bool(FILE_LIKE_RE.search(item.get("name", "")))
        )
    }
    if not invalid_ids:
        return
    profile["capabilities"]["malware"] = [
        item for item in malware if item["id"] not in invalid_ids
    ]
    for activity in profile.get("activities", []):
        activity["malware_refs"] = [
            ref for ref in activity.get("malware_refs", []) if ref not in invalid_ids
        ]


def minmax_time(observations: list[dict[str, Any]], latest: bool) -> dict[str, Any]:
    known = [item["observed_at"] for item in observations if item["observed_at"].get("value")]
    if not known:
        return dict(UNKNOWN_TIME)
    return (max if latest else min)(known, key=lambda item: item["value"])


def merge_ioc_record(
    dataset: dict[str, Any],
    record: dict[str, Any],
    queue: dict[str, Any],
) -> None:
    source_id = source_id_for(record)
    source_path = (
        f"https://github.com/{queue['source']['repository']}/blob/"
        f"{queue['source']['commit']}/{record['activity']['news_path']}"
    )
    published = time_point(record["activity"].get("news_date"), "daily-news-file-date")
    if source_id not in {item["source_id"] for item in dataset["sources"]}:
        dataset["sources"].append(
            {
                "source_id": source_id,
                "path": source_path,
                "published_at": published,
                "confidence": record.get("confidence", "medium"),
                "tlp": "TLP:CLEAR",
                "analyst_notes": f"Primary reference: {source_path_for(record, queue)}",
            }
        )

    by_key = {
        (item["type"], item["normalized_value"]): item
        for item in dataset["indicators"]
    }
    activity_id = activity_id_for(record)
    actor_ref = dataset["actor_ref"]
    for row in record.get("iocs", []):
        kind = row["type"]
        normalized = normalize_observable(kind, row["value"])
        if not normalized:
            continue
        key = (kind, normalized)
        observation = {
            "observation_id": stable_id(
                "observation",
                actor_ref,
                kind,
                normalized,
                source_id,
                str(row.get("row", "")),
                row.get("observed_date", ""),
            ),
            "observed_at": time_point(row.get("observed_date"), "daily-ioc-date"),
            "source_published_at": published,
            "source_id": source_id,
            "source_path": source_path,
            "source_location": {
                "repository": queue["source"]["repository"],
                "commit": queue["source"]["commit"],
                "path": row.get("source_path", record["activity"]["news_path"]),
                "row": row.get("row"),
            },
            "campaign_refs": [activity_id],
            "malware_refs": row.get("malware_refs", []),
            "infrastructure_refs": [],
            "roles": row.get("roles", []),
            "confidence": row.get("confidence", record.get("confidence", "medium")),
            "tlp": "TLP:CLEAR",
            "extraction_method": "tech-memo-structured-csv",
            "raw_value": row["value"],
            "context_excerpt": row.get("description", "")[:500],
            "analyst_notes": (
                f"actor field: {row.get('actor', '')}; "
                f"actor_attribute: {row.get('actor_attribute', '')}; "
                f"reference: {row.get('reference', '')}"
            ),
        }
        if key not in by_key:
            indicator = {
                "indicator_id": stable_id("indicator", actor_ref, kind, normalized),
                "type": kind,
                "value": row["value"],
                "normalized_value": normalized,
                "stix_pattern": stix_pattern(kind, normalized),
                "disposition": "confirmed",
                "first_observed": observation["observed_at"],
                "last_observed": observation["observed_at"],
                "observation_count": 1,
                "campaign_count": 1,
                "seen_in_multiple_campaigns": False,
                "campaign_refs": [activity_id],
                "malware_refs": row.get("malware_refs", []),
                "infrastructure_refs": [],
                "roles": row.get("roles", []),
                "observations": [observation],
            }
            dataset["indicators"].append(indicator)
            by_key[key] = indicator
            continue

        indicator = by_key[key]
        observation_ids = {
            item["observation_id"]: index
            for index, item in enumerate(indicator["observations"])
        }
        if observation["observation_id"] not in observation_ids:
            indicator["observations"].append(observation)
        else:
            indicator["observations"][observation_ids[observation["observation_id"]]] = observation
        observations = indicator["observations"]
        indicator["observation_count"] = len(observations)
        for field in ("campaign_refs", "malware_refs", "infrastructure_refs", "roles"):
            indicator[field] = sorted(
                {
                    ref
                    for item in observations
                    for ref in item.get(field, [])
                }
            )
        indicator["campaign_count"] = len(indicator["campaign_refs"])
        indicator["seen_in_multiple_campaigns"] = indicator["campaign_count"] > 1
        indicator["first_observed"] = minmax_time(observations, latest=False)
        indicator["last_observed"] = minmax_time(observations, latest=True)
        if indicator.get("disposition") == "candidate":
            indicator["disposition"] = "confirmed"

    ingestion = dataset.setdefault("ingestion", {})
    ingestion["source_count"] = len(dataset["sources"])
    ingestion["processed_source_count"] = max(
        ingestion.get("processed_source_count", 0), len(dataset["sources"])
    )
    ingestion["candidate_count"] = sum(
        item.get("disposition") == "candidate" for item in dataset["indicators"]
    )
    dataset["generated_at"] = utc_now()


def merge_artifacts(
    path: Path,
    record: dict[str, Any],
    queue: dict[str, Any],
    actor_ref: str,
) -> None:
    approved = [
        item for item in record.get("artifacts", [])
        if item.get("review_status") == "approved"
    ]
    if not approved:
        return
    columns = load_json(
        REPO_ROOT / "actor_profile" / "schemas" / "artifacts-csv-columns.json"
    )["columns"]
    rows: list[dict[str, Any]] = []
    if path.exists():
        with path.open("r", encoding="utf-8-sig", newline="") as stream:
            rows = list(csv.DictReader(stream))
    existing = {row["observation_id"] for row in rows}
    source_id = source_id_for(record)
    activity_id = activity_id_for(record)
    observed = observed_bounds(record)[0]
    published = time_point(record["activity"].get("news_date"), "daily-news-file-date")
    source_path = (
        f"https://github.com/{queue['source']['repository']}/blob/"
        f"{queue['source']['commit']}/{record['activity']['news_path']}"
    )
    for item in approved:
        normalized = normalize_observable("artifact", item["value"])
        observation_id = stable_id(
            "observation", actor_ref, item["artifact_type"], normalized, source_id
        )
        if observation_id in existing:
            continue
        rows.append(
            {
                "schema_version": "1.0.0",
                "actor_ref": actor_ref,
                "artifact_id": stable_id("artifact", item["artifact_type"], normalized),
                "observation_id": observation_id,
                "artifact_type": item["artifact_type"],
                "value": item["value"],
                "normalized_value": normalized,
                "disposition": "confirmed",
                "observed_at": observed.get("value") or "",
                "observed_at_precision": observed["precision"],
                "observed_at_status": observed["status"],
                "observed_at_basis": observed["basis"],
                "source_published_at": published.get("value") or "",
                "source_id": source_id,
                "source_path": source_path,
                "source_location": json.dumps(
                    {
                        "repository": queue["source"]["repository"],
                        "commit": queue["source"]["commit"],
                        "path": record["activity"]["news_path"],
                    },
                    ensure_ascii=False,
                    sort_keys=True,
                ),
                "campaign_refs": json_array_cell([activity_id]),
                "malware_refs": json_array_cell([]),
                "infrastructure_refs": json_array_cell([]),
                "roles": json_array_cell([]),
                "campaign_count": "1",
                "seen_in_multiple_campaigns": "false",
                "confidence": record.get("confidence", "medium"),
                "tlp": "TLP:CLEAR",
                "extraction_method": "tech-memo-reviewed-artifact",
                "context_excerpt": item.get("context", "")[:500],
                "analyst_notes": f"daily record: {record['record_id']}",
            }
        )
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def process_profile(profile_dir: Path) -> dict[str, Any]:
    profile = profile_dir / "actor-profile.json"
    iocs = profile_dir / "iocs.json"
    artifacts = profile_dir / "artifacts.csv"
    commands = [
        [
            sys.executable,
            str(REPO_ROOT / "actor_profile" / "scripts" / "render_profile.py"),
            str(profile),
            "--iocs", str(iocs),
            "--artifacts", str(artifacts),
        ],
        [
            sys.executable,
            str(REPO_ROOT / "actor_profile" / "scripts" / "validate_profile.py"),
            str(profile),
            "--iocs", str(iocs),
            "--artifacts", str(artifacts),
            "--stix", str(profile_dir / "generated" / "profile.stix2.json"),
            "--json-output",
        ],
    ]
    result: dict[str, Any] = {"render": 0, "validate": 0, "validation": {}}
    for index, command in enumerate(commands):
        completed = subprocess.run(
            command,
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        key = "render" if index == 0 else "validate"
        result[key] = completed.returncode
        if index == 1:
            try:
                validation = json.loads(completed.stdout)
                result["validation"] = {
                    "valid": validation.get("valid", False),
                    "counts": validation.get("counts", {}),
                    "errors": [
                        item for item in validation.get("issues", [])
                        if item.get("severity") == "error"
                    ][:20],
                }
            except json.JSONDecodeError:
                result["validation"] = {"stderr": completed.stderr}
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("queue", type=Path)
    parser.add_argument("--profiles-root", type=Path, default=REPO_ROOT / "profiles")
    parser.add_argument("--apply", action="store_true", help="write changes; default is dry-run")
    parser.add_argument("--actor", action="append", help="limit to actor slug; repeatable")
    parser.add_argument("--no-render", action="store_true")
    args = parser.parse_args()

    queue = load_json(args.queue.resolve())
    wanted = set(args.actor or [])
    approved = [
        item for item in queue["records"]
        if item.get("review_status") == "approved"
        and (not wanted or item["actor"]["slug"] in wanted)
    ]
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in approved:
        grouped[record["actor"]["slug"]].append(record)
    summary: dict[str, Any] = {
        "mode": "apply" if args.apply else "dry-run",
        "approved_records": len(approved),
        "actors": {},
    }
    if not args.apply:
        for slug, records in sorted(grouped.items()):
            summary["actors"][slug] = {
                "records": len(records),
                "ioc_observations": sum(len(item.get("iocs", [])) for item in records),
                "approved_artifacts": sum(
                    artifact.get("review_status") == "approved"
                    for item in records
                    for artifact in item.get("artifacts", [])
                ),
            }
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0

    failures = 0
    for slug, records in sorted(grouped.items()):
        profile_dir = args.profiles_root.resolve() / slug
        profile_path = profile_dir / "actor-profile.json"
        iocs_path = profile_dir / "iocs.json"
        artifacts_path = profile_dir / "artifacts.csv"
        if not profile_path.exists() or not iocs_path.exists() or not artifacts_path.exists():
            summary["actors"][slug] = {"error": "required profile outputs are missing"}
            failures += 1
            continue
        profile = load_json(profile_path)
        dataset = load_json(iocs_path)
        ledger_path = profile_dir / "daily-observations.json"
        ledger = (
            load_json(ledger_path)
            if ledger_path.exists()
            else {
                "schema_version": "1.0.0",
                "actor_ref": profile["profile_id"],
                "updated_at": utc_now(),
                "records": [],
            }
        )
        ledger_ids = {item["record_id"] for item in ledger["records"]}
        source_ids = {item["source_id"] for item in profile["sources"]}
        activity_indexes = {
            item["activity_id"]: index for index, item in enumerate(profile["activities"])
        }
        ledger_indexes = {
            item["record_id"]: index for index, item in enumerate(ledger["records"])
        }
        prune_invalid_daily_malware(profile)
        added = 0
        for record in records:
            source = profile_source(record, queue)
            if source["source_id"] not in source_ids:
                profile["sources"].append(source)
                source_ids.add(source["source_id"])
            ensure_malware_capabilities(profile, record)
            activity = activity_entry(record)
            if activity["activity_id"] not in activity_indexes:
                profile["activities"].append(activity)
                activity_indexes[activity["activity_id"]] = len(profile["activities"]) - 1
            else:
                profile["activities"][activity_indexes[activity["activity_id"]]] = activity
            merge_ioc_record(dataset, record, queue)
            merge_artifacts(artifacts_path, record, queue, profile["profile_id"])
            if record["record_id"] not in ledger_ids:
                ledger["records"].append(
                    {
                        **record,
                        "applied_at": utc_now(),
                        "source_commit": queue["source"]["commit"],
                    }
                )
                ledger_ids.add(record["record_id"])
                added += 1
            else:
                previous = ledger["records"][ledger_indexes[record["record_id"]]]
                ledger["records"][ledger_indexes[record["record_id"]]] = {
                    **record,
                    "applied_at": previous.get("applied_at", utc_now()),
                    "source_commit": queue["source"]["commit"],
                }
        profile["sources"].sort(key=lambda item: item["source_id"])
        profile["activities"].sort(
            key=lambda item: (
                item.get("first_observed", {}).get("value") or "",
                item["activity_id"],
            )
        )
        profile["capabilities"]["malware"].sort(key=lambda item: item["id"])
        profile["updated_at"] = utc_now()
        ledger["updated_at"] = utc_now()
        ledger["records"].sort(key=lambda item: item["record_id"])
        write_json_atomic(profile_path, profile)
        write_json_atomic(iocs_path, dataset)
        write_json_atomic(ledger_path, ledger)
        result = {"records_added_to_ledger": added}
        if not args.no_render:
            result["processing"] = process_profile(profile_dir)
            counts = result["processing"].get("validation", {}).get("counts", {})
            if result["processing"]["render"] or counts.get("error", 1):
                failures += 1
        summary["actors"][slug] = result
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
