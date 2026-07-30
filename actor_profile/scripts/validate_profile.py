#!/usr/bin/env python3
"""Validate actor profile, IOC dataset, artifacts CSV, and generated STIX."""

from __future__ import annotations

import argparse
import csv
import ipaddress
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from common import (
    CONFIDENCE,
    TIME_PRECISIONS,
    TIME_STATUSES,
    load_json,
    parse_json_array_cell,
)
from ingest_observables import (
    IANA_TLDS,
    SPECIAL_USE_TLDS,
    host_of,
    reference_host,
)

PUBLICATION_BASIS = re.compile(
    r"(?:publication|published|report(?:ed)?[-_ ]?date|daily-news-file-date)",
    re.IGNORECASE,
)


@dataclass
class Issue:
    severity: str
    location: str
    message: str


def issue(
    issues: list[Issue], severity: str, location: str, message: str
) -> None:
    issues.append(Issue(severity, location, message))


def validate_time(
    value: Any, location: str, issues: list[Issue], *, warn_unknown: bool = False
) -> None:
    if not isinstance(value, dict):
        issue(issues, "error", location, "time point must be an object")
        return
    for key in ("value", "precision", "status", "basis"):
        if key not in value:
            issue(issues, "error", location, f"missing time field: {key}")
    if value.get("precision") not in TIME_PRECISIONS:
        issue(issues, "error", location, "invalid time precision")
    if value.get("status") not in TIME_STATUSES:
        issue(issues, "error", location, "invalid time status")
    if value.get("status") == "unknown" and value.get("value") is not None:
        issue(issues, "error", location, "unknown time must have null value")
    if value.get("status") in {"known", "inferred"} and not value.get("value"):
        issue(issues, "error", location, "known/inferred time requires value")
    if value.get("value"):
        try:
            normalized = str(value["value"]).replace("Z", "+00:00")
            from datetime import datetime

            datetime.fromisoformat(normalized)
        except ValueError:
            issue(issues, "error", location, "invalid ISO 8601 time")
    if warn_unknown and value.get("status") == "unknown":
        issue(issues, "warning", location, "observation time is unknown")


def validate_observation_time(
    value: Any,
    location: str,
    issues: list[Issue],
    *,
    warn_unknown: bool = False,
) -> None:
    validate_time(value, location, issues, warn_unknown=warn_unknown)
    if (
        isinstance(value, dict)
        and value.get("value")
        and PUBLICATION_BASIS.search(str(value.get("basis", "")))
    ):
        issue(
            issues,
            "error",
            location,
            "publication/report date cannot be used as an observation date",
        )


def check_unique_ids(
    items: Iterable[dict[str, Any]],
    key: str,
    location: str,
    issues: list[Issue],
) -> set[str]:
    values: set[str] = set()
    for index, item in enumerate(items):
        value = item.get(key)
        if not isinstance(value, str) or not value:
            issue(issues, "error", f"{location}[{index}]", f"missing {key}")
            continue
        if value in values:
            issue(issues, "error", f"{location}[{index}].{key}", f"duplicate ID: {value}")
        values.add(value)
    return values


def check_evidence_refs(
    item: dict[str, Any],
    location: str,
    source_ids: set[str],
    issues: list[Issue],
) -> None:
    refs = item.get("evidence_refs")
    if refs is None:
        issue(issues, "error", location, "missing evidence_refs")
        return
    if not refs:
        issue(issues, "warning", location, "no evidence references")
    for ref in refs:
        if ref not in source_ids:
            issue(issues, "error", location, f"dangling evidence reference: {ref}")


def validate_profile(profile: dict[str, Any], issues: list[Issue]) -> dict[str, set[str]]:
    required = {
        "schema_version", "profile_id", "name", "status", "created_at", "updated_at",
        "actor", "attribution", "motivations", "relationships", "diamond_model",
        "capabilities", "activities", "victim_cases", "targets", "ttps", "sources",
        "assessment", "free_text",
    }
    missing = required - set(profile)
    for key in sorted(missing):
        issue(issues, "error", "$", f"missing top-level field: {key}")
    if profile.get("schema_version") != "1.1.0":
        issue(issues, "error", "$.schema_version", "expected 1.1.0")
    if not re.match(r"^actor--[a-z0-9][a-z0-9-]*$", profile.get("profile_id", "")):
        issue(issues, "error", "$.profile_id", "invalid profile ID")

    sources = profile.get("sources", [])
    source_ids = check_unique_ids(sources, "source_id", "$.sources", issues)
    for index, source in enumerate(sources):
        validate_time(source.get("published_at"), f"$.sources[{index}].published_at", issues)
        if source.get("reliability") not in CONFIDENCE:
            issue(issues, "error", f"$.sources[{index}].reliability", "invalid confidence")
        if not source.get("path"):
            issue(issues, "warning", f"$.sources[{index}].path", "source path is empty")

    actor = profile.get("actor", {})
    validate_time(actor.get("first_seen"), "$.actor.first_seen", issues)
    validate_time(actor.get("last_seen"), "$.actor.last_seen", issues)
    alias_names: set[str] = set()
    for index, alias in enumerate(actor.get("aliases", [])):
        lowered = alias.get("name", "").lower()
        if lowered in alias_names:
            issue(issues, "error", f"$.actor.aliases[{index}]", "duplicate alias")
        alias_names.add(lowered)
        if alias.get("scope") == "unknown":
            issue(issues, "warning", f"$.actor.aliases[{index}]", "alias scope is unknown")
        check_evidence_refs(alias, f"$.actor.aliases[{index}]", source_ids, issues)

    attribution = profile.get("attribution", {})
    if attribution.get("confidence") not in CONFIDENCE:
        issue(issues, "error", "$.attribution.confidence", "invalid confidence")
    check_evidence_refs(attribution, "$.attribution", source_ids, issues)

    for index, motivation in enumerate(profile.get("motivations", [])):
        check_evidence_refs(motivation, f"$.motivations[{index}]", source_ids, issues)

    relationships = profile.get("relationships", [])
    relationship_ids = check_unique_ids(
        relationships, "relationship_id", "$.relationships", issues
    )
    for index, relationship in enumerate(relationships):
        check_evidence_refs(
            relationship, f"$.relationships[{index}]", source_ids, issues
        )
        for key in ("first_observed", "last_observed"):
            if key in relationship:
                validate_observation_time(
                    relationship[key],
                    f"$.relationships[{index}].{key}",
                    issues,
                )

    capabilities = profile.get("capabilities", {})
    capability_ids: dict[str, set[str]] = {}
    all_capability_ids: set[str] = set()
    for category in (
        "malware", "tools", "infrastructure", "delivery_formats",
        "vulnerabilities", "operational_capabilities",
    ):
        items = capabilities.get(category, [])
        ids = check_unique_ids(items, "id", f"$.capabilities.{category}", issues)
        overlap = all_capability_ids & ids
        for duplicate in sorted(overlap):
            issue(issues, "error", f"$.capabilities.{category}", f"ID reused across capability categories: {duplicate}")
        all_capability_ids |= ids
        capability_ids[category] = ids
        for index, item in enumerate(items):
            validate_observation_time(item.get("first_observed"), f"$.capabilities.{category}[{index}].first_observed", issues)
            validate_observation_time(item.get("last_observed"), f"$.capabilities.{category}[{index}].last_observed", issues)
            check_evidence_refs(item, f"$.capabilities.{category}[{index}]", source_ids, issues)

    activities = profile.get("activities", [])
    activity_ids = check_unique_ids(activities, "activity_id", "$.activities", issues)
    victim_cases = profile.get("victim_cases", [])
    victim_ids = check_unique_ids(
        victim_cases, "victim_case_id", "$.victim_cases", issues
    )
    target_items = []
    for category in ("countries", "regions", "sectors", "roles"):
        target_items.extend(profile.get("targets", {}).get(category, []))
    target_ids = check_unique_ids(target_items, "id", "$.targets.*", issues)

    for index, activity in enumerate(activities):
        validate_observation_time(activity.get("first_observed"), f"$.activities[{index}].first_observed", issues)
        validate_observation_time(activity.get("last_observed"), f"$.activities[{index}].last_observed", issues)
        validate_time(activity.get("reported_at"), f"$.activities[{index}].reported_at", issues)
        check_evidence_refs(activity, f"$.activities[{index}]", source_ids, issues)
        for ref in activity.get("target_refs", []):
            if ref not in target_ids:
                issue(issues, "error", f"$.activities[{index}].target_refs", f"dangling target reference: {ref}")
        for ref in activity.get("malware_refs", []):
            if ref not in capability_ids.get("malware", set()):
                issue(issues, "error", f"$.activities[{index}].malware_refs", f"dangling malware reference: {ref}")
        for ref in activity.get("infrastructure_refs", []):
            if ref not in capability_ids.get("infrastructure", set()):
                issue(issues, "error", f"$.activities[{index}].infrastructure_refs", f"dangling infrastructure reference: {ref}")
        for ref in activity.get("victim_refs", []):
            if ref not in victim_ids:
                issue(issues, "error", f"$.activities[{index}].victim_refs", f"dangling victim reference: {ref}")

    for index, victim in enumerate(victim_cases):
        location = f"$.victim_cases[{index}]"
        for key in ("first_observed", "last_observed"):
            validate_observation_time(victim.get(key), f"{location}.{key}", issues)
        validate_time(victim.get("reported_at"), f"{location}.reported_at", issues)
        check_evidence_refs(victim, location, source_ids, issues)
        for ref in victim.get("activity_refs", []):
            if ref not in activity_ids:
                issue(issues, "error", f"{location}.activity_refs", f"dangling activity reference: {ref}")
        for ref in victim.get("target_refs", []):
            if ref not in target_ids:
                issue(issues, "error", f"{location}.target_refs", f"dangling target reference: {ref}")
        for ref in victim.get("malware_refs", []):
            if ref not in capability_ids.get("malware", set()):
                issue(issues, "error", f"{location}.malware_refs", f"dangling malware reference: {ref}")

    for category in ("countries", "regions", "sectors", "roles"):
        for index, target in enumerate(profile.get("targets", {}).get(category, [])):
            validate_observation_time(target.get("first_observed"), f"$.targets.{category}[{index}].first_observed", issues)
            validate_observation_time(target.get("last_observed"), f"$.targets.{category}[{index}].last_observed", issues)
            check_evidence_refs(target, f"$.targets.{category}[{index}]", source_ids, issues)

    ttps = profile.get("ttps", [])
    ttp_ids = check_unique_ids(ttps, "ttp_id", "$.ttps", issues)
    for index, ttp in enumerate(ttps):
        if not re.match(r"^T\d{4}(?:\.\d{3})?$", ttp.get("technique_id", "")):
            issue(issues, "error", f"$.ttps[{index}].technique_id", "invalid ATT&CK technique ID")
        if not ttp.get("observed_behavior"):
            issue(issues, "warning", f"$.ttps[{index}].observed_behavior", "observed behavior is empty")
        validate_observation_time(ttp.get("first_observed"), f"$.ttps[{index}].first_observed", issues)
        validate_observation_time(ttp.get("last_observed"), f"$.ttps[{index}].last_observed", issues)
        check_evidence_refs(ttp, f"$.ttps[{index}]", source_ids, issues)
        for ref in ttp.get("activity_refs", []):
            if ref not in activity_ids:
                issue(issues, "error", f"$.ttps[{index}].activity_refs", f"dangling activity reference: {ref}")
        for ref in ttp.get("malware_refs", []):
            if ref not in capability_ids.get("malware", set()):
                issue(issues, "error", f"$.ttps[{index}].malware_refs", f"dangling malware reference: {ref}")
        for ref in ttp.get("infrastructure_refs", []):
            if ref not in capability_ids.get("infrastructure", set()):
                issue(issues, "error", f"$.ttps[{index}].infrastructure_refs", f"dangling infrastructure reference: {ref}")
        if ttp.get("activity_refs") and not (
            ttp.get("first_observed", {}).get("value")
            or ttp.get("last_observed", {}).get("value")
        ):
            issue(
                issues,
                "warning",
                f"$.ttps[{index}]",
                "activity-linked TTP has no observation date",
            )

    activity_by_id = {item["activity_id"]: item for item in activities}
    ttp_by_id = {item["ttp_id"]: item for item in ttps}
    victim_by_id = {item["victim_case_id"]: item for item in victim_cases}
    for index, activity in enumerate(activities):
        activity_id = activity["activity_id"]
        for ref in activity.get("ttp_refs", []):
            ttp = ttp_by_id.get(ref)
            if ttp is None:
                issue(issues, "error", f"$.activities[{index}].ttp_refs", f"dangling TTP reference: {ref}")
            elif activity_id not in ttp.get("activity_refs", []):
                issue(issues, "error", f"$.activities[{index}].ttp_refs", f"TTP backlink is missing: {ref}")
        for ref in activity.get("victim_refs", []):
            victim = victim_by_id.get(ref)
            if victim is not None and activity_id not in victim.get("activity_refs", []):
                issue(issues, "error", f"$.activities[{index}].victim_refs", f"victim backlink is missing: {ref}")
    for index, ttp in enumerate(ttps):
        for ref in ttp.get("activity_refs", []):
            activity = activity_by_id.get(ref)
            if activity is not None and ttp["ttp_id"] not in activity.get("ttp_refs", []):
                issue(issues, "error", f"$.ttps[{index}].activity_refs", f"activity backlink is missing: {ref}")
    for index, victim in enumerate(victim_cases):
        for ref in victim.get("activity_refs", []):
            activity = activity_by_id.get(ref)
            if activity is not None and victim["victim_case_id"] not in activity.get("victim_refs", []):
                issue(issues, "error", f"$.victim_cases[{index}].activity_refs", f"activity backlink is missing: {ref}")
        for ref in victim.get("ttp_refs", []):
            if ref not in ttp_ids:
                issue(issues, "error", f"$.victim_cases[{index}].ttp_refs", f"dangling TTP reference: {ref}")

    for index, judgment in enumerate(profile.get("assessment", {}).get("key_judgments", [])):
        check_evidence_refs(judgment, f"$.assessment.key_judgments[{index}]", source_ids, issues)

    if not profile.get("free_text", {}).get("executive_summary"):
        issue(issues, "warning", "$.free_text.executive_summary", "executive summary is empty")

    return {
        "source_ids": source_ids,
        "activity_ids": activity_ids,
        "malware_ids": capability_ids.get("malware", set()),
        "infrastructure_ids": capability_ids.get("infrastructure", set()),
        "target_ids": target_ids,
        "victim_ids": victim_ids,
        "relationship_ids": relationship_ids,
        "ttp_ids": ttp_ids,
    }


def check_indicator_is_observable(
    indicator: dict[str, Any], location: str, issues: list[Issue]
) -> None:
    """指標として成立しない値がIOCへ混入していないか検査する。

    出典レポート自身の参考リンク（ベンダーブログ、CERT、報道）と、実在しない
    TLDを持つ抽出失敗値を検出する。詳細は RULES.md 8. IOCモデルを参照。
    """
    ioc_type = indicator.get("type")
    if ioc_type not in {"url", "domain", "email"}:
        return
    value = indicator.get("normalized_value") or indicator.get("value") or ""
    host = host_of(value)
    if not host:
        issue(issues, "error", location, f"ホストを取り出せない値: {value!r}")
        return
    try:
        # http://203.0.113.10/path のようにホストがIPアドレスのURLは指標として正当。
        ipaddress.ip_address(host.strip("[]").split("%", 1)[0])
    except ValueError:
        pass
    else:
        return
    if reference_host(value):
        issue(
            issues,
            "error",
            location,
            f"出典の参考リンクはIOCにしない (RULES.md 8.): {host}",
        )
        return
    if "." not in host:
        issue(issues, "error", location, f"ホストとして成立しない値: {host}")
        return
    tld = host.rsplit(".", 1)[-1]
    if IANA_TLDS and tld not in IANA_TLDS and tld not in SPECIAL_USE_TLDS:
        issue(issues, "error", location, f"実在しないTLD: .{tld}")


def validate_iocs(
    dataset: dict[str, Any],
    profile: dict[str, Any],
    refs: dict[str, set[str]],
    issues: list[Issue],
) -> None:
    if dataset.get("schema_version") != "1.0.0":
        issue(issues, "error", "iocs.schema_version", "expected 1.0.0")
    if dataset.get("actor_ref") != profile.get("profile_id"):
        issue(issues, "error", "iocs.actor_ref", "does not match profile_id")
    dataset_source_ids = check_unique_ids(
        dataset.get("sources", []), "source_id", "iocs.sources", issues
    )
    valid_source_ids = refs["source_ids"] | dataset_source_ids
    for index, source in enumerate(dataset.get("sources", [])):
        validate_time(
            source.get("published_at"),
            f"iocs.sources[{index}].published_at",
            issues,
        )
    indicator_ids: set[str] = set()
    observation_ids: set[str] = set()
    for index, indicator in enumerate(dataset.get("indicators", [])):
        location = f"iocs.indicators[{index}]"
        indicator_id = indicator.get("indicator_id")
        if indicator_id in indicator_ids:
            issue(issues, "error", location, f"duplicate indicator ID: {indicator_id}")
        indicator_ids.add(indicator_id)
        observations = indicator.get("observations", [])
        if indicator.get("observation_count") != len(observations):
            issue(issues, "error", location, "observation_count does not match observations")
        campaigns = sorted(
            {ref for obs in observations for ref in obs.get("campaign_refs", [])}
        )
        if indicator.get("campaign_count") != len(campaigns):
            issue(issues, "error", location, "campaign_count does not match observations")
        if indicator.get("seen_in_multiple_campaigns") != (len(campaigns) > 1):
            issue(issues, "error", location, "seen_in_multiple_campaigns is inconsistent")
        if sorted(indicator.get("campaign_refs", [])) != campaigns:
            issue(issues, "error", location, "campaign_refs aggregate is inconsistent")
        validate_time(indicator.get("first_observed"), f"{location}.first_observed", issues)
        validate_time(indicator.get("last_observed"), f"{location}.last_observed", issues)
        if indicator.get("disposition") == "candidate":
            issue(issues, "warning", location, "candidate IOC requires analyst review")
        check_indicator_is_observable(indicator, location, issues)
        for obs_index, observation in enumerate(observations):
            obs_location = f"{location}.observations[{obs_index}]"
            obs_id = observation.get("observation_id")
            if obs_id in observation_ids:
                issue(issues, "error", obs_location, f"duplicate observation ID: {obs_id}")
            observation_ids.add(obs_id)
            validate_time(observation.get("observed_at"), f"{obs_location}.observed_at", issues, warn_unknown=True)
            validate_time(observation.get("source_published_at"), f"{obs_location}.source_published_at", issues)
            if observation.get("source_id") not in valid_source_ids:
                issue(issues, "error", obs_location, f"unknown source_id: {observation.get('source_id')}")
            for ref in observation.get("campaign_refs", []):
                if ref not in refs["activity_ids"]:
                    issue(issues, "error", obs_location, f"unknown campaign_ref: {ref}")
            for ref in observation.get("malware_refs", []):
                if ref not in refs["malware_ids"]:
                    issue(issues, "error", obs_location, f"unknown malware_ref: {ref}")
            for ref in observation.get("infrastructure_refs", []):
                if ref not in refs["infrastructure_ids"]:
                    issue(issues, "error", obs_location, f"unknown infrastructure_ref: {ref}")
    ingestion = dataset.get("ingestion", {})
    if ingestion.get("error_source_count", 0):
        issue(issues, "warning", "iocs.ingestion", f"{ingestion['error_source_count']} sources failed ingestion")


def validate_artifacts(
    path: Path,
    profile: dict[str, Any],
    refs: dict[str, set[str]],
    issues: list[Issue],
) -> None:
    spec = load_json(
        Path(__file__).resolve().parent.parent
        / "schemas"
        / "artifacts-csv-columns.json"
    )
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != spec["columns"]:
            issue(issues, "error", "artifacts.header", "CSV columns/order do not match canonical specification")
        rows = list(reader)
    observation_ids: set[str] = set()
    campaigns_by_artifact: dict[str, set[str]] = {}
    for row in rows:
        try:
            campaigns = set(parse_json_array_cell(row["campaign_refs"]))
            malware = set(parse_json_array_cell(row["malware_refs"]))
            infrastructure = set(parse_json_array_cell(row["infrastructure_refs"]))
            parse_json_array_cell(row["roles"])
        except (ValueError, json.JSONDecodeError) as exc:
            issue(issues, "error", f"artifacts:{row.get('observation_id')}", f"invalid JSON array cell: {exc}")
            continue
        campaigns_by_artifact.setdefault(row["artifact_id"], set()).update(campaigns)
        location = f"artifacts:{row['observation_id']}"
        if row["schema_version"] != spec["schema_version"]:
            issue(issues, "error", location, "unexpected schema_version")
        if row["actor_ref"] != profile.get("profile_id"):
            issue(issues, "error", location, "actor_ref does not match profile")
        if not row["artifact_id"] or not row["value"] or not row["normalized_value"]:
            issue(issues, "error", location, "artifact ID/value fields must be non-empty")
        if row["artifact_type"] not in spec["artifact_types"]:
            issue(issues, "error", location, "invalid artifact_type")
        if row["disposition"] not in {"confirmed", "candidate", "rejected"}:
            issue(issues, "error", location, "invalid disposition")
        if row["confidence"] not in CONFIDENCE:
            issue(issues, "error", location, "invalid confidence")
        if row["source_id"] not in refs["source_ids"]:
            issue(issues, "error", location, f"unknown source_id: {row['source_id']}")
        if row["observation_id"] in observation_ids:
            issue(issues, "error", location, "duplicate observation_id")
        observation_ids.add(row["observation_id"])
        if row["observed_at_status"] == "unknown":
            issue(issues, "warning", f"artifacts:{row['observation_id']}", "observation time is unknown")
        else:
            validate_time(
                {
                    "value": row["observed_at"],
                    "precision": row["observed_at_precision"],
                    "status": row["observed_at_status"],
                    "basis": row["observed_at_basis"],
                },
                f"artifacts:{row['observation_id']}.observed_at",
                issues,
            )
        if row["source_published_at"]:
            validate_time(
                {
                    "value": row["source_published_at"],
                    "precision": "second",
                    "status": "known",
                    "basis": "source-publication",
                },
                f"artifacts:{row['observation_id']}.source_published_at",
                issues,
            )
        if row["disposition"] == "candidate":
            issue(issues, "warning", f"artifacts:{row['observation_id']}", "candidate artifact requires analyst review")
        for ref in campaigns:
            if ref not in refs["activity_ids"]:
                issue(issues, "error", f"artifacts:{row['observation_id']}", f"unknown campaign_ref: {ref}")
        for ref in malware:
            if ref not in refs["malware_ids"]:
                issue(issues, "error", f"artifacts:{row['observation_id']}", f"unknown malware_ref: {ref}")
        for ref in infrastructure:
            if ref not in refs["infrastructure_ids"]:
                issue(issues, "error", f"artifacts:{row['observation_id']}", f"unknown infrastructure_ref: {ref}")
    for row in rows:
        expected = len(campaigns_by_artifact.get(row["artifact_id"], set()))
        if int(row["campaign_count"] or 0) != expected:
            issue(issues, "error", f"artifacts:{row['observation_id']}", "campaign_count is inconsistent")
        expected_multiple = "true" if expected > 1 else "false"
        if row["seen_in_multiple_campaigns"].lower() != expected_multiple:
            issue(issues, "error", f"artifacts:{row['observation_id']}", "seen_in_multiple_campaigns is inconsistent")


def validate_stix(bundle: dict[str, Any], issues: list[Issue]) -> None:
    if bundle.get("type") != "bundle":
        issue(issues, "error", "stix.type", "expected STIX bundle")
    objects = bundle.get("objects", [])
    ids: set[str] = set()
    for index, obj in enumerate(objects):
        obj_id = obj.get("id")
        if not isinstance(obj_id, str) or not obj_id.startswith(f"{obj.get('type')}--"):
            issue(issues, "error", f"stix.objects[{index}].id", "invalid STIX ID prefix")
        if obj_id in ids:
            issue(issues, "error", f"stix.objects[{index}].id", "duplicate STIX ID")
        ids.add(obj_id)
    external_refs = {"marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487"}
    for index, obj in enumerate(objects):
        for key in ("source_ref", "target_ref"):
            if obj.get(key) and obj[key] not in ids:
                issue(issues, "error", f"stix.objects[{index}].{key}", f"dangling STIX reference: {obj[key]}")
        for key in ("object_refs", "object_marking_refs"):
            for ref in obj.get(key, []):
                if ref not in ids and ref not in external_refs:
                    issue(issues, "error", f"stix.objects[{index}].{key}", f"dangling STIX reference: {ref}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", type=Path)
    parser.add_argument("--iocs", type=Path)
    parser.add_argument("--artifacts", type=Path)
    parser.add_argument("--stix", type=Path)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--json-output", action="store_true")
    parser.add_argument(
        "--max-findings",
        type=int,
        default=100,
        help="maximum text findings to print; 0 prints all (default: 100)",
    )
    args = parser.parse_args()

    issues: list[Issue] = []
    profile = load_json(args.profile)
    refs = validate_profile(profile, issues)
    ioc_dataset = None
    if args.iocs:
        ioc_dataset = load_json(args.iocs)
        validate_iocs(ioc_dataset, profile, refs, issues)
    if args.artifacts:
        artifact_refs = dict(refs)
        artifact_refs["source_ids"] = set(refs["source_ids"])
        if ioc_dataset:
            artifact_refs["source_ids"].update(
                item.get("source_id")
                for item in ioc_dataset.get("sources", [])
                if item.get("source_id")
            )
        validate_artifacts(args.artifacts, profile, artifact_refs, issues)
    if args.stix:
        validate_stix(load_json(args.stix), issues)

    counts = {
        severity: sum(item.severity == severity for item in issues)
        for severity in ("error", "warning", "info")
    }
    shown = issues if args.max_findings == 0 else issues[: max(args.max_findings, 0)]
    if args.json_output:
        print(
            json.dumps(
                {
                    "valid": counts["error"] == 0
                    and (not args.strict or counts["warning"] == 0),
                    "counts": counts,
                    "issues": [item.__dict__ for item in shown],
                    "omitted_issue_count": len(issues) - len(shown),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        for item in shown:
            print(f"{item.severity.upper()}\t{item.location}\t{item.message}")
        if len(shown) < len(issues):
            print(f"NOTICE\toutput\t{len(issues) - len(shown)} additional findings omitted")
        print(
            f"SUMMARY\terrors={counts['error']} warnings={counts['warning']} "
            f"info={counts['info']}"
        )
    return 1 if counts["error"] or (args.strict and counts["warning"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
