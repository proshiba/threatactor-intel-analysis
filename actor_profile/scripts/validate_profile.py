#!/usr/bin/env python3
"""Validate actor profile, IOC dataset, artifacts CSV, and generated STIX."""

from __future__ import annotations

import argparse
import csv
import ipaddress
import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from common import (
    CONFIDENCE,
    TIME_PRECISIONS,
    TIME_STATUSES,
    load_json,
    parse_json_array_cell,
)
from activity_diamond import build_activity_diamond
from ingest_observables import (
    IANA_TLDS,
    SPECIAL_USE_TLDS,
    analyst_marked_indicator,
    host_of,
    reference_host,
)

PUBLICATION_BASIS = re.compile(
    r"(?:publication|published|report(?:ed)?[-_ ]?date|daily-news-file-date)",
    re.IGNORECASE,
)
NON_ACTIVITY_OBSERVATION_BASIS = re.compile(
    r"(?:"
    r"(?:vt|virustotal)[-_ ]?first[-_ ]?seen"
    r"|certificate[-_ ]?(?:validity|not[-_ ]?before|not[-_ ]?after)"
    r")",
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
            datetime.fromisoformat(normalized)
        except ValueError:
            issue(issues, "error", location, "invalid ISO 8601 time")
    if warn_unknown and value.get("status") == "unknown":
        issue(issues, "warning", location, "observation time is unknown")


def validate_time_order(
    first: Any,
    last: Any,
    location: str,
    issues: list[Issue],
) -> None:
    """Reject a known first timestamp that is later than the known last one."""

    if not isinstance(first, dict) or not isinstance(last, dict):
        return
    first_value = first.get("value")
    last_value = last.get("value")
    if not first_value or not last_value:
        return

    def normalized_datetime(value: Any) -> datetime:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)

    try:
        first_datetime = normalized_datetime(first_value)
        last_datetime = normalized_datetime(last_value)
    except (TypeError, ValueError):
        # validate_time reports malformed values at their precise locations.
        return
    if first_datetime > last_datetime:
        issue(
            issues,
            "error",
            location,
            "first observation time cannot be later than last observation time",
        )


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
    if (
        isinstance(value, dict)
        and value.get("value")
        and NON_ACTIVITY_OBSERVATION_BASIS.search(
            str(value.get("basis", ""))
        )
    ):
        issue(
            issues,
            "error",
            location,
            "repository first-seen or certificate-validity metadata cannot "
            "be used as an activity observation date",
        )


def validate_legal_action_time(
    value: Any,
    location: str,
    issues: list[Issue],
) -> None:
    """Validate a legal event date without substituting source publication."""

    validate_time(value, location, issues)
    if (
        isinstance(value, dict)
        and value.get("value")
        and PUBLICATION_BASIS.search(str(value.get("basis", "")))
    ):
        issue(
            issues,
            "error",
            location,
            "source publication date cannot be used as a legal action date",
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
        "actor", "attribution", "motivations", "relationships",
        "associated_entities", "entity_relationships", "hunting_pivots", "diamond_model",
        "capabilities", "activities", "victim_cases", "targets", "ttps", "sources",
        "assessment", "free_text",
    }
    missing = required - set(profile)
    for key in sorted(missing):
        issue(issues, "error", "$", f"missing top-level field: {key}")
    if profile.get("schema_version") != "1.4.0":
        issue(issues, "error", "$.schema_version", "expected 1.4.0")
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
    validate_observation_time(
        actor.get("first_seen"), "$.actor.first_seen", issues
    )
    validate_observation_time(
        actor.get("last_seen"), "$.actor.last_seen", issues
    )
    validate_time_order(
        actor.get("first_seen"), actor.get("last_seen"), "$.actor", issues
    )
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
        validate_time_order(
            relationship.get("first_observed"),
            relationship.get("last_observed"),
            f"$.relationships[{index}]",
            issues,
        )

    associated_entities = profile.get("associated_entities", [])
    entity_ids = check_unique_ids(
        associated_entities, "entity_id", "$.associated_entities", issues
    )
    for index, entity in enumerate(associated_entities):
        location = f"$.associated_entities[{index}]"
        entity_id = entity.get("entity_id", "")
        entity_type = entity.get("entity_type")
        expected_prefix = {
            "organization": "organization--",
            "threat-actor-individual": "threat-actor-individual--",
            "threat-actor-group": "threat-actor-group--",
        }.get(entity_type)
        if expected_prefix and not entity_id.startswith(expected_prefix):
            issue(
                issues,
                "error",
                f"{location}.entity_id",
                f"{entity_type} ID must start with {expected_prefix}",
            )
        if entity_type == "organization" and entity.get("threat_actor_types"):
            issue(
                issues,
                "error",
                f"{location}.threat_actor_types",
                "organization cannot have threat_actor_types",
            )
        validate_observation_time(
            entity.get("first_observed"), f"{location}.first_observed", issues
        )
        validate_observation_time(
            entity.get("last_observed"), f"{location}.last_observed", issues
        )
        validate_time_order(
            entity.get("first_observed"),
            entity.get("last_observed"),
            location,
            issues,
        )
        check_evidence_refs(entity, location, source_ids, issues)
        legal_actions = entity.get("legal_actions", [])
        check_unique_ids(
            legal_actions, "action_id", f"{location}.legal_actions", issues
        )
        for action_index, action in enumerate(legal_actions):
            action_location = f"{location}.legal_actions[{action_index}]"
            validate_legal_action_time(
                action.get("action_date"),
                f"{action_location}.action_date",
                issues,
            )
            check_evidence_refs(action, action_location, source_ids, issues)

    entity_relationships = profile.get("entity_relationships", [])
    entity_relationship_ids = check_unique_ids(
        entity_relationships,
        "relationship_id",
        "$.entity_relationships",
        issues,
    )
    valid_entity_refs = {profile.get("profile_id", ""), *entity_ids}
    for index, relationship in enumerate(entity_relationships):
        location = f"$.entity_relationships[{index}]"
        for ref_key in ("source_ref", "target_ref"):
            if relationship.get(ref_key) not in valid_entity_refs:
                issue(
                    issues,
                    "error",
                    f"{location}.{ref_key}",
                    f"dangling entity reference: {relationship.get(ref_key)}",
                )
        if relationship.get("source_ref") == relationship.get("target_ref"):
            issue(issues, "error", location, "entity relationship cannot be self-referential")
        validate_observation_time(
            relationship.get("first_observed"),
            f"{location}.first_observed",
            issues,
        )
        validate_observation_time(
            relationship.get("last_observed"),
            f"{location}.last_observed",
            issues,
        )
        validate_time_order(
            relationship.get("first_observed"),
            relationship.get("last_observed"),
            location,
            issues,
        )
        check_evidence_refs(relationship, location, source_ids, issues)

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
            validate_time_order(
                item.get("first_observed"),
                item.get("last_observed"),
                f"$.capabilities.{category}[{index}]",
                issues,
            )
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

    hunting_pivots = profile.get("hunting_pivots", [])
    hunting_pivot_ids = check_unique_ids(
        hunting_pivots, "pivot_id", "$.hunting_pivots", issues
    )
    indicator_ref_pattern = re.compile(r"^indicator--")
    for index, pivot in enumerate(hunting_pivots):
        location = f"$.hunting_pivots[{index}]"
        validate_observation_time(
            pivot.get("first_observed"), f"{location}.first_observed", issues
        )
        validate_observation_time(
            pivot.get("last_observed"), f"{location}.last_observed", issues
        )
        validate_time_order(
            pivot.get("first_observed"),
            pivot.get("last_observed"),
            location,
            issues,
        )
        check_evidence_refs(pivot, location, source_ids, issues)
        for ref in pivot.get("malware_refs", []):
            if ref not in capability_ids.get("malware", set()):
                issue(issues, "error", f"{location}.malware_refs", f"dangling malware reference: {ref}")
        for ref in pivot.get("infrastructure_refs", []):
            if ref not in capability_ids.get("infrastructure", set()):
                issue(issues, "error", f"{location}.infrastructure_refs", f"dangling infrastructure reference: {ref}")
        for ref in pivot.get("activity_refs", []):
            if ref not in activity_ids:
                issue(issues, "error", f"{location}.activity_refs", f"dangling activity reference: {ref}")
        for ref in pivot.get("indicator_refs", []):
            if not indicator_ref_pattern.match(ref):
                issue(issues, "error", f"{location}.indicator_refs", f"invalid indicator reference: {ref}")

        observations = pivot.get("observations", [])
        check_unique_ids(
            observations, "observation_id", f"{location}.observations", issues
        )
        observation_total = 0
        observation_sources: set[str] = set()
        observation_activities: set[str] = set()
        for observation_index, observation in enumerate(observations):
            observation_location = (
                f"{location}.observations[{observation_index}]"
            )
            validate_observation_time(
                observation.get("observed_at"),
                f"{observation_location}.observed_at",
                issues,
            )
            source_ref = observation.get("source_ref")
            if source_ref not in source_ids:
                issue(
                    issues,
                    "error",
                    f"{observation_location}.source_ref",
                    f"dangling source reference: {source_ref}",
                )
            elif source_ref:
                observation_sources.add(source_ref)
            activity_ref = observation.get("activity_ref")
            if activity_ref is not None:
                if activity_ref not in activity_ids:
                    issue(
                        issues,
                        "error",
                        f"{observation_location}.activity_ref",
                        f"dangling activity reference: {activity_ref}",
                    )
                else:
                    observation_activities.add(activity_ref)
            observation_total += observation.get("count", 0)
        missing_evidence_sources = observation_sources - set(
            pivot.get("evidence_refs", [])
        )
        if missing_evidence_sources:
            issue(
                issues,
                "error",
                f"{location}.evidence_refs",
                "pivot evidence_refs must include every observation source: "
                + ", ".join(sorted(missing_evidence_sources)),
            )
        missing_activity_refs = observation_activities - set(
            pivot.get("activity_refs", [])
        )
        if missing_activity_refs:
            issue(
                issues,
                "error",
                f"{location}.activity_refs",
                "pivot activity_refs must include every observation activity: "
                + ", ".join(sorted(missing_activity_refs)),
            )
        expected_counts = {
            "observation_count": observation_total,
            "source_count": len(observation_sources),
            "activity_count": len(observation_activities),
        }
        for count_key, expected in expected_counts.items():
            if pivot.get(count_key) != expected:
                issue(
                    issues,
                    "error",
                    f"{location}.{count_key}",
                    f"expected {expected} from observation records",
                )
        continuity = pivot.get("continuity", {})
        assessment = continuity.get("assessment")
        if assessment == "single-observation" and len(observations) != 1:
            issue(
                issues,
                "error",
                f"{location}.continuity",
                "single-observation requires exactly one observation record; "
                "that record may count multiple samples or observables",
            )
        if assessment in {"reused", "reobserved"} and observation_total < 2:
            issue(issues, "error", f"{location}.continuity", f"{assessment} requires at least two documented observations")
        checks = continuity.get("checks", [])
        check_unique_ids(
            checks, "check_id", f"{location}.continuity.checks", issues
        )
        for check_index, check in enumerate(checks):
            check_location = (
                f"{location}.continuity.checks[{check_index}]"
            )
            try:
                datetime.fromisoformat(
                    str(check.get("evaluated_at", "")).replace("Z", "+00:00")
                )
            except ValueError:
                issue(
                    issues,
                    "error",
                    f"{check_location}.evaluated_at",
                    "invalid ISO 8601 evaluation time",
                )
            for source_ref in check.get("evidence_refs", []):
                if source_ref not in source_ids:
                    issue(
                        issues,
                        "error",
                        f"{check_location}.evidence_refs",
                        f"dangling source reference: {source_ref}",
                    )
        passive_scan_performed = continuity.get("passive_scan_performed")
        if passive_scan_performed is True and not checks:
            issue(
                issues,
                "error",
                f"{location}.continuity.checks",
                "a performed passive scan requires a structured check record",
            )
        if checks and passive_scan_performed is not True:
            issue(
                issues,
                "error",
                f"{location}.continuity.passive_scan_performed",
                "structured continuity checks require passive_scan_performed=true",
            )
        if continuity.get("active_status") in {"active", "inactive"} and not any(
            check.get("analyst_validated")
            and check.get("evidence_refs")
            for check in checks
        ):
            issue(
                issues,
                "error",
                f"{location}.continuity.active_status",
                "active/inactive status requires a validated, evidenced continuity check",
            )
        for query_index, query in enumerate(pivot.get("hunt_queries", [])):
            query_location = f"{location}.hunt_queries[{query_index}]"
            if query.get("requires_validation") is not True:
                issue(
                    issues,
                    "error",
                    f"{query_location}.requires_validation",
                    "hunt results must require analyst validation",
                )
            if not str(query.get("false_positive_notes", "")).strip():
                issue(
                    issues,
                    "error",
                    f"{query_location}.false_positive_notes",
                    "hunt query must document false-positive conditions",
                )

    for index, activity in enumerate(activities):
        stix_type = activity.get("stix_object_type")
        if stix_type not in {"campaign", "incident", "grouping"}:
            issue(
                issues,
                "error",
                f"$.activities[{index}].stix_object_type",
                "must explicitly be campaign, incident, or grouping",
            )
        grouping_context = activity.get("grouping_context")
        if stix_type == "grouping" and grouping_context not in {
            "suspicious-activity", "malware-analysis", "unspecified"
        }:
            issue(
                issues,
                "error",
                f"$.activities[{index}].grouping_context",
                "Grouping requires an explicit STIX grouping context",
            )
        if stix_type != "grouping" and grouping_context is not None:
            issue(
                issues,
                "error",
                f"$.activities[{index}].grouping_context",
                "non-Grouping activity must use null grouping_context",
            )
        validate_observation_time(activity.get("first_observed"), f"$.activities[{index}].first_observed", issues)
        validate_observation_time(activity.get("last_observed"), f"$.activities[{index}].last_observed", issues)
        validate_time_order(
            activity.get("first_observed"),
            activity.get("last_observed"),
            f"$.activities[{index}]",
            issues,
        )
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
        for ref in activity.get("activity_refs", []):
            if ref not in activity_ids:
                issue(issues, "error", f"$.activities[{index}].activity_refs", f"dangling activity reference: {ref}")
            if ref == activity.get("activity_id"):
                issue(issues, "error", f"$.activities[{index}].activity_refs", "activity cannot contain itself")
        if not isinstance(activity.get("diamond_model"), dict):
            issue(
                issues,
                "error",
                f"$.activities[{index}].diamond_model",
                "activity Diamond Model is missing",
            )

    for index, victim in enumerate(victim_cases):
        location = f"$.victim_cases[{index}]"
        for key in ("first_observed", "last_observed"):
            validate_observation_time(victim.get(key), f"{location}.{key}", issues)
        validate_time_order(
            victim.get("first_observed"),
            victim.get("last_observed"),
            location,
            issues,
        )
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
            validate_time_order(
                target.get("first_observed"),
                target.get("last_observed"),
                f"$.targets.{category}[{index}]",
                issues,
            )
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
        validate_time_order(
            ttp.get("first_observed"),
            ttp.get("last_observed"),
            f"$.ttps[{index}]",
            issues,
        )
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

    for index, activity in enumerate(activities):
        expected_diamond = build_activity_diamond(profile, activity)
        if activity.get("diamond_model") != expected_diamond:
            issue(
                issues,
                "error",
                f"$.activities[{index}].diamond_model",
                "activity Diamond Model is stale or inconsistent; run materialize_activity_diamonds.py --apply",
            )

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
        "entity_ids": entity_ids,
        "entity_relationship_ids": entity_relationship_ids,
        "hunting_pivot_ids": hunting_pivot_ids,
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
    if ioc_type == "certificate-fingerprint":
        algorithm = indicator.get("hash_algorithm")
        expected_names = {
            "md5": "MD5",
            "sha1": "SHA-1",
            "sha256": "SHA-256",
            "sha512": "SHA-512",
        }
        if algorithm not in expected_names:
            issue(
                issues,
                "error",
                location,
                "certificate-fingerprint requires an explicit hash_algorithm",
            )
            return
        expected_length = {
            "md5": 32,
            "sha1": 40,
            "sha256": 64,
            "sha512": 128,
        }[algorithm]
        normalized_value = indicator.get("normalized_value", "")
        if len(normalized_value) != expected_length:
            issue(
                issues,
                "error",
                location,
                f"certificate fingerprint {algorithm} requires "
                f"{expected_length} hex characters",
            )
        marker = f"hashes.'{expected_names[algorithm]}'"
        if marker not in indicator.get("stix_pattern", ""):
            issue(
                issues,
                "error",
                location,
                "certificate fingerprint STIX pattern does not match hash_algorithm",
            )
        return
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
    if reference_host(value) and not analyst_marked_indicator(indicator):
        # 8.0の例外: 構造化IOC表由来・難読化済みの値はアナリストが指標として
        # 明示したものなので、参考ホスト(攻撃者が悪用した正規サービスを含む)でも残す。
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
        validate_observation_time(
            indicator.get("first_observed"),
            f"{location}.first_observed",
            issues,
        )
        validate_observation_time(
            indicator.get("last_observed"),
            f"{location}.last_observed",
            issues,
        )
        validate_time_order(
            indicator.get("first_observed"),
            indicator.get("last_observed"),
            location,
            issues,
        )
        if indicator.get("disposition") == "candidate":
            issue(issues, "warning", location, "candidate IOC requires analyst review")
        check_indicator_is_observable(indicator, location, issues)
        for obs_index, observation in enumerate(observations):
            obs_location = f"{location}.observations[{obs_index}]"
            obs_id = observation.get("observation_id")
            if obs_id in observation_ids:
                issue(issues, "error", obs_location, f"duplicate observation ID: {obs_id}")
            observation_ids.add(obs_id)
            validate_observation_time(
                observation.get("observed_at"),
                f"{obs_location}.observed_at",
                issues,
                warn_unknown=True,
            )
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
            validate_observation_time(
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
