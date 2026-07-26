"""Pure modeling helpers for approved daily intelligence records."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any

from daily_common import (
    UNKNOWN_TIME,
    is_file_like,
    load_json,
    source_publisher,
    source_reliability,
    stable_digest,
    time_point,
)


REPO_ROOT = Path(__file__).resolve().parent.parent
FILE_NAME_SEARCH = re.compile(
    r"([^/\\\s]+\.(?:exe|dll|sys|ps1|bat|cmd|js|jse|vbs|hta|lnk|"
    r"docm?|xlsm?|pptm?|pdf|zip|rar|7z|apk|dmg|pkg|sh|py))",
    re.IGNORECASE,
)


def source_id_for_value(value: str) -> str:
    return f"source--daily-{stable_digest(value)[:20]}"


def activity_reference(record: dict[str, Any]) -> str:
    activity = record["activity"]
    return (
        activity.get("activity_reference")
        or activity.get("primary_url")
        or activity["news_path"]
    )


def activity_id_for(record: dict[str, Any]) -> str:
    return (
        f"activity--daily-"
        f"{stable_digest(record['actor']['slug'], activity_reference(record))[:20]}"
    )


def repository_url(queue: dict[str, Any], path: str) -> str:
    return (
        f"https://github.com/{queue['source']['repository']}/blob/"
        f"{queue['source']['commit']}/{path}"
    )


def source_items(record: dict[str, Any], queue: dict[str, Any]) -> list[dict[str, str]]:
    values = record.get("sources", [])
    if not values:
        activity = record["activity"]
        values = [
            {
                "url": activity.get("primary_url") or "",
                "source_path": activity["news_path"],
                "source_type": "primary-report",
            }
        ]
    result: list[dict[str, str]] = []
    seen: set[str] = set()
    for item in values:
        path = item.get("source_path") or record["activity"]["news_path"]
        url = item.get("url") or repository_url(queue, path)
        if url in seen:
            continue
        seen.add(url)
        result.append(
            {
                "url": url,
                "source_path": path,
                "source_type": item.get("source_type", "osint-report"),
            }
        )
    return sorted(result, key=lambda item: item["url"])


def source_for_row(
    record: dict[str, Any], row: dict[str, Any], queue: dict[str, Any]
) -> dict[str, str]:
    reference = row.get("reference", "").strip()
    if reference:
        return {
            "url": reference,
            "source_path": row.get("source_path") or record["activity"]["news_path"],
            "source_type": (
                "primary-report"
                if reference == activity_reference(record)
                else "ioc-reference"
            ),
        }
    return source_items(record, queue)[0]


def primary_source(
    record: dict[str, Any], queue: dict[str, Any]
) -> dict[str, str]:
    sources = source_items(record, queue)
    reference = activity_reference(record)
    return next(
        (
            item
            for item in sources
            if item["url"] == reference or item["source_type"] == "primary-report"
        ),
        sources[0],
    )


def profile_source(
    record: dict[str, Any], source: dict[str, str], queue: dict[str, Any]
) -> dict[str, Any]:
    activity = record["activity"]
    primary = source["url"]
    published = (
        time_point(activity.get("news_date"), "daily-news-file-date")
        if source["source_type"] == "primary-report"
        else dict(UNKNOWN_TIME)
    )
    return {
        "source_id": source_id_for_value(primary),
        "path": primary,
        "title": (
            activity["title"]
            if source["source_type"] == "primary-report"
            else f"{activity['title']} — IOC補助資料"
        ),
        "publisher": source_publisher(primary),
        "published_at": published,
        "language": "unknown",
        "source_type": "osint-report",
        "tlp": "TLP:CLEAR",
        "reliability": source_reliability(primary),
        "sha256": None,
        "analyst_notes": (
            f"tech-memo日次収集から取込。元ファイル: {source['source_path']}; "
            f"source commit: {queue['source']['commit']}; "
            "出典信頼性はアクター帰属確度と分離して評価。"
        ),
    }


def activity_bounds(record: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    reviewed = record.get("activity_period", {})
    if reviewed:
        return (
            dict(reviewed.get("first_observed") or UNKNOWN_TIME),
            dict(reviewed.get("last_observed") or UNKNOWN_TIME),
        )
    return dict(UNKNOWN_TIME), dict(UNKNOWN_TIME)


def activity_entry(
    record: dict[str, Any], evidence_refs: list[str]
) -> dict[str, Any]:
    first, last = activity_bounds(record)
    malware_refs = sorted(
        {
            ref
            for row in record.get("iocs", [])
            for ref in row.get("malware_refs", [])
        }
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
        "confidence": record.get("confidence", "unknown"),
        "evidence_refs": sorted(evidence_refs),
        "analyst_notes": (
            f"日次収集レコード {record['record_id']} から取込。"
            "活動期間はレビュー済みの一次資料記載がある場合だけ設定し、"
            "ニュース公開日やIOC収集日からは推定しない。"
            f" レビュー: {record.get('review_notes') or '記載なし'}"
        ),
    }


def capability_decision(record: dict[str, Any], name: str) -> dict[str, str]:
    for item in record.get("capability_decisions", []):
        if item.get("name", "").casefold() == name.casefold():
            return item
    return {
        "name": name,
        "status": "pending",
        "reason": "Capabilityレビューが未実施。",
    }


def _malware_lookup(profile: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for item in profile["capabilities"]["malware"]:
        result[item.get("name", "").casefold()] = item
        for alias in item.get("aliases", []):
            result[alias.casefold()] = item
    return result


def ensure_malware_capabilities(
    profile: dict[str, Any],
    record: dict[str, Any],
    evidence_refs: list[str],
) -> None:
    malware = profile["capabilities"]["malware"]
    lookup = _malware_lookup(profile)
    record_first, record_last = activity_bounds(record)
    for row in record.get("iocs", []):
        refs: set[str] = set()
        raw_malware = row.get("malware", "").strip()
        for raw_name in re.split(r"[,;|]", raw_malware):
            name = raw_name.strip()
            if name.casefold() in {"", "unknown", "n/a", "na", "none", "知られていない"}:
                continue
            match = FILE_NAME_SEARCH.search(name)
            if is_file_like(name) or match:
                continue
            decision = capability_decision(record, name)
            if decision.get("status") != "approved":
                continue
            item = lookup.get(name.casefold())
            if item is None:
                malware_type = row.get("malware_type", "").strip()
                types = (
                    [malware_type]
                    if malware_type.casefold()
                    not in {"", "unknown", "n/a", "na", "none"}
                    else []
                )
                item = {
                    "id": f"malware--daily-{stable_digest(name)[:20]}",
                    "name": name,
                    "aliases": [],
                    "types": types,
                    "description": (
                        f"{profile['actor']['canonical_name']}との直接的な利用関係が"
                        "一次資料レビューで確認されたマルウェア。"
                    ),
                    "first_observed": record_first,
                    "last_observed": record_last,
                    "confidence": record.get("confidence", "unknown"),
                    "evidence_refs": sorted(evidence_refs),
                    "analyst_notes": decision.get("reason", ""),
                }
                malware.append(item)
                lookup[name.casefold()] = item
            elif item["id"].startswith("malware--daily-"):
                malware_type = row.get("malware_type", "").strip()
                confidence_rank = {
                    "unknown": 0,
                    "low": 1,
                    "medium": 2,
                    "high": 3,
                }
                confidence_values = {
                    item.get("confidence", "unknown"),
                    record.get("confidence", "unknown"),
                }
                item.update(
                    {
                        "types": sorted(
                            set(item.get("types", []))
                            | (
                                {malware_type}
                                if malware_type.casefold()
                                not in {"", "unknown", "n/a", "na", "none"}
                                else set()
                            )
                        ),
                        "description": (
                            f"{profile['actor']['canonical_name']}との直接的な利用関係が"
                            "一次資料レビューで確認されたマルウェア。"
                        ),
                        "first_observed": _merge_time_point(
                            item.get("first_observed", UNKNOWN_TIME),
                            record_first,
                            latest=False,
                        ),
                        "last_observed": _merge_time_point(
                            item.get("last_observed", UNKNOWN_TIME),
                            record_last,
                            latest=True,
                        ),
                        "confidence": min(
                            confidence_values,
                            key=lambda value: confidence_rank.get(value, 0),
                        ),
                        "evidence_refs": sorted(
                            set(item.get("evidence_refs", [])) | set(evidence_refs)
                        ),
                        "analyst_notes": " | ".join(
                            sorted(
                                {
                                    value
                                    for value in (
                                        item.get("analyst_notes", ""),
                                        decision.get("reason", ""),
                                    )
                                    if value
                                }
                            )
                        ),
                    }
                )
            else:
                item["evidence_refs"] = sorted(
                    set(item.get("evidence_refs", [])) | set(evidence_refs)
                )
            refs.add(item["id"])
        row["malware_refs"] = sorted(refs)


def minmax_time(observations: list[dict[str, Any]], latest: bool) -> dict[str, Any]:
    known = [
        item["observed_at"] for item in observations if item["observed_at"].get("value")
    ]
    if not known:
        return dict(UNKNOWN_TIME)
    return (max if latest else min)(known, key=lambda item: item["value"])


def _merge_time_point(
    left: dict[str, Any], right: dict[str, Any], *, latest: bool
) -> dict[str, Any]:
    known = [item for item in (left, right) if item.get("value")]
    if not known:
        return dict(UNKNOWN_TIME)
    return dict((max if latest else min)(known, key=lambda item: item["value"]))


def add_dataset_source(
    dataset: dict[str, Any],
    record: dict[str, Any],
    source: dict[str, str],
) -> str:
    source_id = source_id_for_value(source["url"])
    published = (
        time_point(record["activity"].get("news_date"), "daily-news-file-date")
        if source["source_type"] == "primary-report"
        else dict(UNKNOWN_TIME)
    )
    modeled = {
        "source_id": source_id,
        "path": source["url"],
        "published_at": published,
        "confidence": source_reliability(source["url"]),
        "tlp": "TLP:CLEAR",
        "analyst_notes": (
            "source confidenceは出典信頼性であり、アクター帰属確度ではない。"
        ),
    }
    source_indexes = {
        item["source_id"]: index
        for index, item in enumerate(dataset["sources"])
    }
    if source_id in source_indexes:
        dataset["sources"][source_indexes[source_id]] = modeled
    else:
        dataset["sources"].append(modeled)
    return source_id


def merge_ioc_record(
    dataset: dict[str, Any],
    record: dict[str, Any],
    queue: dict[str, Any],
    common: Any,
) -> None:
    by_key = {
        (item["type"], item["normalized_value"]): item
        for item in dataset["indicators"]
    }
    activity_id = activity_id_for(record)
    actor_ref = dataset["actor_ref"]
    for row in record.get("iocs", []):
        kind = row["type"]
        normalized = common.normalize_observable(kind, row["value"])
        if not normalized:
            continue
        source = source_for_row(record, row, queue)
        source_id = add_dataset_source(dataset, record, source)
        key = (kind, normalized)
        observation = {
            "observation_id": common.stable_id(
                "observation",
                actor_ref,
                kind,
                normalized,
                source_id,
                row.get("source_path", ""),
                str(row.get("row", "")),
                row.get("observed_date", ""),
            ),
            "observed_at": time_point(row.get("observed_date"), "daily-ioc-date"),
            "source_published_at": (
                time_point(record["activity"].get("news_date"), "daily-news-file-date")
                if source["source_type"] == "primary-report"
                else dict(UNKNOWN_TIME)
            ),
            "source_id": source_id,
            "source_path": source["url"],
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
            "confidence": row.get("confidence", record.get("confidence", "unknown")),
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
                "indicator_id": common.stable_id(
                    "indicator", actor_ref, kind, normalized
                ),
                "type": kind,
                "value": row["value"],
                "normalized_value": normalized,
                "stix_pattern": common.stix_pattern(kind, normalized),
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
        indexes = {
            item["observation_id"]: index
            for index, item in enumerate(indicator["observations"])
        }
        if observation["observation_id"] in indexes:
            indicator["observations"][indexes[observation["observation_id"]]] = observation
        else:
            indicator["observations"].append(observation)
        refresh_indicator(indicator)


def refresh_indicator(indicator: dict[str, Any]) -> None:
    observations = indicator["observations"]
    indicator["observation_count"] = len(observations)
    for field in ("campaign_refs", "malware_refs", "infrastructure_refs", "roles"):
        indicator[field] = sorted(
            {
                ref
                for observation in observations
                for ref in observation.get(field, [])
            }
        )
    indicator["campaign_count"] = len(indicator["campaign_refs"])
    indicator["seen_in_multiple_campaigns"] = indicator["campaign_count"] > 1
    indicator["first_observed"] = minmax_time(observations, latest=False)
    indicator["last_observed"] = minmax_time(observations, latest=True)


def load_artifact_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def merge_artifacts(
    rows: list[dict[str, str]],
    record: dict[str, Any],
    queue: dict[str, Any],
    actor_ref: str,
    common: Any,
) -> list[dict[str, str]]:
    approved = [
        item
        for item in record.get("artifacts", [])
        if item.get("review_status") == "approved"
    ]
    existing = {row["observation_id"] for row in rows}
    source = primary_source(record, queue)
    source_id = source_id_for_value(source["url"])
    activity_id = activity_id_for(record)
    first, _ = activity_bounds(record)
    published = time_point(
        record["activity"].get("news_date"), "daily-news-file-date"
    )
    for item in approved:
        normalized = common.normalize_observable("artifact", item["value"])
        observation_id = common.stable_id(
            "observation",
            actor_ref,
            item["artifact_type"],
            normalized,
            source_id,
            record["record_id"],
        )
        if observation_id in existing:
            continue
        rows.append(
            {
                "schema_version": "1.0.0",
                "actor_ref": actor_ref,
                "artifact_id": common.stable_id(
                    "artifact", item["artifact_type"], normalized
                ),
                "observation_id": observation_id,
                "artifact_type": item["artifact_type"],
                "value": item["value"],
                "normalized_value": normalized,
                "disposition": "confirmed",
                "observed_at": first.get("value") or "",
                "observed_at_precision": first["precision"],
                "observed_at_status": first["status"],
                "observed_at_basis": first["basis"],
                "source_published_at": published.get("value") or "",
                "source_id": source_id,
                "source_path": source["url"],
                "source_location": json.dumps(
                    {
                        "repository": queue["source"]["repository"],
                        "commit": queue["source"]["commit"],
                        "path": record["activity"]["news_path"],
                    },
                    ensure_ascii=False,
                    sort_keys=True,
                ),
                "campaign_refs": common.json_array_cell([activity_id]),
                "malware_refs": common.json_array_cell([]),
                "infrastructure_refs": common.json_array_cell([]),
                "roles": common.json_array_cell([]),
                "campaign_count": "1",
                "seen_in_multiple_campaigns": "false",
                "confidence": record.get("confidence", "unknown"),
                "tlp": "TLP:CLEAR",
                "extraction_method": "tech-memo-reviewed-artifact",
                "context_excerpt": item.get("context", "")[:500],
                "analyst_notes": f"daily record: {record['record_id']}",
            }
        )
        existing.add(observation_id)
    return rows


def remove_daily_materialization(
    profile: dict[str, Any],
    dataset: dict[str, Any],
    artifact_rows: list[dict[str, str]],
) -> list[dict[str, str]]:
    profile["sources"] = [
        item
        for item in profile.get("sources", [])
        if not item["source_id"].startswith("source--daily-")
    ]
    profile["activities"] = [
        item
        for item in profile.get("activities", [])
        if not item["activity_id"].startswith("activity--daily-")
    ]
    profile["capabilities"]["malware"] = [
        item
        for item in profile["capabilities"]["malware"]
        if not item["id"].startswith("malware--daily-")
    ]
    _remove_daily_refs(profile)

    dataset["sources"] = [
        item
        for item in dataset.get("sources", [])
        if not item["source_id"].startswith("source--daily-")
    ]
    indicators = []
    for indicator in dataset.get("indicators", []):
        existing_observations = indicator.get("observations", [])
        retained_observations = [
            item
            for item in existing_observations
            if not item.get("extraction_method", "").startswith("tech-memo-")
        ]
        if len(retained_observations) != len(existing_observations):
            indicator["observations"] = retained_observations
            if retained_observations:
                refresh_indicator(indicator)
        indicators.append(indicator)
    dataset["indicators"] = indicators
    return [
        row
        for row in artifact_rows
        if not row.get("extraction_method", "").startswith("tech-memo-")
    ]


def _remove_daily_refs(value: Any) -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            if isinstance(item, list) and key.endswith("_refs"):
                value[key] = [
                    ref
                    for ref in item
                    if not (
                        isinstance(ref, str)
                        and ref.startswith(
                            ("source--daily-", "activity--daily-", "malware--daily-")
                        )
                    )
                ]
            else:
                _remove_daily_refs(item)
    elif isinstance(value, list):
        for item in value:
            _remove_daily_refs(item)


def finalize_dataset(dataset: dict[str, Any]) -> None:
    dataset["indicators"] = [
        item for item in dataset["indicators"] if item.get("observations")
    ]
    ingestion = dataset.setdefault("ingestion", {})
    ingestion["source_count"] = len(dataset["sources"])
    ingestion["processed_source_count"] = len(dataset["sources"])
    ingestion["candidate_count"] = sum(
        item.get("disposition") == "candidate" for item in dataset["indicators"]
    )


def artifact_columns() -> list[str]:
    return load_json(
        REPO_ROOT / "actor_profile" / "schemas" / "artifacts-csv-columns.json"
    )["columns"]


def build_ledger(
    existing: dict[str, Any] | None,
    actor_ref: str,
    records: list[dict[str, Any]],
    source_commit: str,
    updated_at: str,
    *,
    rebuild: bool,
) -> dict[str, Any]:
    retained = {} if rebuild else {
        item["record_id"]: item
        for item in (existing or {}).get("records", [])
    }
    for record in records:
        retained[record["record_id"]] = {
            **record,
            "source_commit": source_commit,
        }
    return {
        "schema_version": "2.0.0",
        "actor_ref": actor_ref,
        "updated_at": updated_at,
        "records": sorted(retained.values(), key=lambda item: item["record_id"]),
    }
