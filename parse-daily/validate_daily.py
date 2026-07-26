#!/usr/bin/env python3
"""Validate a daily review queue and, optionally, its applied profile state."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from daily_common import load_json, stable_digest


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
VALID_STATUS = {"pending", "approved", "rejected"}
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
    if queue.get("schema_version") != "1.0.0":
        issues.append(finding("error", "schema-version", "schema_version must be 1.0.0"))
    records = queue.get("records")
    if not isinstance(records, list):
        issues.append(finding("error", "records-type", "records must be an array"))
        records = []
    seen: set[str] = set()
    approved_by_actor: Counter[str] = Counter()
    for record in records:
        record_id = record.get("record_id", "")
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
        if not activity.get("title") or not activity.get("news_path"):
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
                identity = (
                    item["activity"].get("primary_url")
                    or item["activity"]["news_path"]
                )
                source_id = f"source--daily-{stable_digest(identity)[:20]}"
                activity_id = (
                    f"activity--daily-{stable_digest(item['record_id'])[:20]}"
                )
                if source_id not in profile_source_ids:
                    issues.append(
                        finding("error", "profile-source-missing", source_id, item["record_id"])
                    )
                if activity_id not in profile_activity_ids:
                    issues.append(
                        finding("error", "profile-activity-missing", activity_id, item["record_id"])
                    )
                if item.get("iocs") and (
                    source_id not in ioc_source_ids
                    or source_id not in observation_source_ids
                ):
                    issues.append(
                        finding("error", "ioc-source-missing", source_id, item["record_id"])
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
