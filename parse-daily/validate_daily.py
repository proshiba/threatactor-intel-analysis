#!/usr/bin/env python3
"""Validate a daily review queue and, optionally, its applied profile state."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from daily_common import is_file_like, load_json
from daily_materializer import (
    activity_id_for,
    source_id_for_value,
    source_items,
)


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
VALID_STATUS = {"pending", "approved", "rejected"}
VALID_CAPABILITY_STATUS = {"pending", "approved", "rejected", "related-only"}
VALID_IOC_TYPES = {
    "md5", "sha1", "sha256", "sha512", "ipv4", "ipv6",
    "domain", "url", "email", "certificate-fingerprint",
}


def finding(level: str, code: str, message: str, record_id: str = "") -> dict[str, str]:
    result = {"level": level, "code": code, "message": message}
    if record_id:
        result["record_id"] = record_id
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("queue", type=Path)
    parser.add_argument("--profiles-root", type=Path, default=REPO_ROOT / "profiles")
    parser.add_argument("--check-applied", action="store_true")
    args = parser.parse_args()

    queue = load_json(args.queue.resolve())
    issues: list[dict[str, str]] = []
    if queue.get("schema_version") != "2.0.0":
        issues.append(finding("error", "schema-version", "schema_version must be 2.0.0"))
    records = queue.get("records")
    if not isinstance(records, list):
        issues.append(finding("error", "records-type", "records must be an array"))
        records = []
    for message in queue.get("decision_issues", []):
        issues.append(finding("error", "unused-review-decision", message))
    seen: set[str] = set()
    approved_by_actor: Counter[str] = Counter()
    for record in records:
        record_id = record.get("record_id", "")
        for message in record.get("decision_issues", []):
            issues.append(
                finding("error", "review-decision-mismatch", message, record_id)
            )
        if not record_id or record_id in seen:
            issues.append(finding("error", "record-id", "missing or duplicate record_id", record_id))
        seen.add(record_id)
        status = record.get("review_status")
        if status not in VALID_STATUS:
            issues.append(finding("error", "review-status", f"invalid status: {status}", record_id))
        actor = record.get("actor", {})
        slug = actor.get("slug", "")
        if not (args.profiles_root / slug / "actor-profile.json").exists():
            issues.append(finding("error", "actor-missing", f"profile not found: {slug}", record_id))
        if status == "approved":
            approved_by_actor[slug] += 1
            if actor.get("scope") != "exact":
                issues.append(
                    finding(
                        "warning",
                        "non-exact-approved",
                        f"approved actor match has scope={actor.get('scope')}",
                        record_id,
                    )
                )
        activity = record.get("activity", {})
        if (
            not activity.get("title")
            or not activity.get("news_path")
            or not activity.get("activity_reference")
        ):
            issues.append(finding("error", "activity-required", "activity title/path missing", record_id))
        date = activity.get("news_date")
        if date and not re.fullmatch(r"20\d{2}-\d{2}-\d{2}", date):
            issues.append(finding("error", "news-date", f"invalid news date: {date}", record_id))
        for row in record.get("iocs", []):
            if row.get("type") not in VALID_IOC_TYPES:
                issues.append(
                    finding("error", "ioc-type", f"invalid IOC type: {row.get('type')}", record_id)
                )
            if not row.get("value"):
                issues.append(finding("error", "ioc-value", "empty IOC value", record_id))
            observed = row.get("observed_date")
            if observed and not re.fullmatch(r"20\d{2}-\d{2}-\d{2}", observed):
                issues.append(
                    finding("error", "ioc-date", f"invalid IOC date: {observed}", record_id)
                )
        for artifact in record.get("artifacts", []):
            if artifact.get("review_status") == "approved" and not artifact.get("value"):
                issues.append(
                    finding("error", "artifact-value", "approved artifact has no value", record_id)
                )
        decisions = record.get("capability_decisions", [])
        seen_capabilities: set[str] = set()
        for decision in decisions:
            name = decision.get("name", "")
            if not name or name.casefold() in seen_capabilities:
                issues.append(
                    finding(
                        "error",
                        "capability-name",
                        "missing or duplicate capability decision",
                        record_id,
                    )
                )
            seen_capabilities.add(name.casefold())
            capability_status = decision.get("status")
            if capability_status not in VALID_CAPABILITY_STATUS:
                issues.append(
                    finding(
                        "error",
                        "capability-status",
                        f"invalid capability status: {capability_status}",
                        record_id,
                    )
                )
            if capability_status != "pending" and not decision.get("reason"):
                issues.append(
                    finding(
                        "error",
                        "capability-reason",
                        f"reviewed capability lacks reason: {name}",
                        record_id,
                    )
                )
            if is_file_like(name):
                issues.append(
                    finding(
                        "error",
                        "file-as-capability",
                        f"file-like value must be an artifact: {name}",
                        record_id,
                    )
                )
        if status == "approved" and any(
            item.get("status") == "pending" for item in decisions
        ):
            issues.append(
                finding(
                    "error",
                    "capability-review-pending",
                    "approved record contains pending capability decisions",
                    record_id,
                )
            )

    if args.check_applied:
        for slug, expected in approved_by_actor.items():
            ledger_path = args.profiles_root / slug / "daily-observations.json"
            if not ledger_path.exists():
                issues.append(finding("error", "ledger-missing", f"missing ledger for {slug}"))
                continue
            ledger = load_json(ledger_path)
            ledger_ids = {item.get("record_id") for item in ledger.get("records", [])}
            queue_ids = {
                item["record_id"]
                for item in records
                if item.get("review_status") == "approved" and item["actor"]["slug"] == slug
            }
            missing = sorted(queue_ids - ledger_ids)
            if missing:
                issues.append(
                    finding("error", "ledger-incomplete", f"{slug}: {len(missing)} approved records missing")
                )
            profile = load_json(args.profiles_root / slug / "actor-profile.json")
            profile_source_ids = {item["source_id"] for item in profile.get("sources", [])}
            profile_activity_ids = {
                item["activity_id"] for item in profile.get("activities", [])
            }
            dataset = load_json(args.profiles_root / slug / "iocs.json")
            ioc_source_ids = {item["source_id"] for item in dataset.get("sources", [])}
            observation_source_ids = {
                observation["source_id"]
                for indicator in dataset.get("indicators", [])
                for observation in indicator.get("observations", [])
            }
            for item in records:
                if item.get("review_status") != "approved" or item["actor"]["slug"] != slug:
                    continue
                expected_source_ids = {
                    source_id_for_value(source["url"])
                    for source in source_items(item, queue)
                }
                activity_id = activity_id_for(item)
                for source_id in sorted(expected_source_ids - profile_source_ids):
                    issues.append(
                        finding(
                            "error",
                            "profile-source-missing",
                            source_id,
                            item["record_id"],
                        )
                    )
                if activity_id not in profile_activity_ids:
                    issues.append(
                        finding("error", "profile-activity-missing", activity_id, item["record_id"])
                    )
                if item.get("iocs"):
                    missing_ioc_sources = expected_source_ids - (
                        ioc_source_ids & observation_source_ids
                    )
                    for source_id in sorted(missing_ioc_sources):
                        issues.append(
                            finding(
                                "error",
                                "ioc-source-missing",
                                source_id,
                                item["record_id"],
                            )
                        )

    counts = Counter(item["level"] for item in issues)
    result: dict[str, Any] = {
        "valid": counts["error"] == 0,
        "counts": {
            "error": counts["error"],
            "warning": counts["warning"],
            "records": len(records),
            "approved": sum(approved_by_actor.values()),
        },
        "issues": issues,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if counts["error"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
