#!/usr/bin/env python3
"""Build explicitly curated, actor-free Activity bundles for OpenCTI.

The daily unknown-cluster ledger is intentionally heterogeneous and is never
exported wholesale.  Only entries allowlisted in
``standalone-activity-curation.json`` reach this module.  The resulting bundle
contains Campaign/Incident/Grouping evidence, source Reports and (for the two
reviewed structured tables) Indicators, but never an Intrusion Set, Threat
Actor, or an Activity-to-Actor relationship.
"""

from __future__ import annotations

import copy
import ipaddress
import json
import re
from collections import defaultdict
from datetime import datetime
from typing import Any

from render_profile import TLP_CLEAR, stix_base, stix_id


CONFIDENCE = {"high": 85, "medium": 60, "low": 30, "unknown": 0}
ALLOWED_ACTIVITY_TYPES = {"campaign", "incident", "grouping"}
ALLOWED_GROUPING_CONTEXTS = {"suspicious-activity", "malware-analysis", "unspecified"}
ALLOWED_PRECISIONS = {"second", "day", "month", "year", "range", "unknown"}
ALLOWED_TIME_STATUSES = {"known", "inferred", "unknown"}
STANDALONE_OBSERVABLE_TYPES = {
    "domain": "domain-name",
    "ipv4": "ipv4-addr",
    "sha256": "file",
    "url": "url",
}
OPENCTI_MAIN_OBSERVABLE_TYPES = {
    "domain": "Domain-Name",
    "ipv4": "IPv4-Addr",
    "sha256": "StixFile",
    "url": "Url",
}
IOC_ROLE_LABEL = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def _source_id(activity_id: str, index: int, suffix: str = "") -> str:
    tail = f"-{suffix}" if suffix else ""
    return f"source--standalone-{activity_id.removeprefix('activity--')}-{index}{tail}"


def _external_reference(source_id: str, source: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {
        "source_name": source.get("publisher") or "source",
        "external_id": source_id,
    }
    if source.get("url"):
        result["url"] = source["url"]
    return result


def _validate_point(point: Any, field: str) -> None:
    if not isinstance(point, dict):
        raise ValueError(f"{field} must be an object")
    if point.get("precision") not in ALLOWED_PRECISIONS:
        raise ValueError(f"{field}.precision is invalid")
    if point.get("status") not in ALLOWED_TIME_STATUSES:
        raise ValueError(f"{field}.status is invalid")
    if not isinstance(point.get("basis"), str) or not point["basis"].strip():
        raise ValueError(f"{field}.basis must be a non-empty string")
    if point.get("status") == "unknown" and point.get("value") is not None:
        raise ValueError(f"{field} unknown status must have null value")
    if point.get("status") == "unknown" and point.get("precision") != "unknown":
        raise ValueError(f"{field} unknown status must use unknown precision")
    if point.get("status") != "unknown" and not point.get("value"):
        raise ValueError(f"{field} known/inferred status requires value")
    if point.get("status") != "unknown" and point.get("precision") == "unknown":
        raise ValueError(f"{field} known/inferred status cannot use unknown precision")
    if point.get("value"):
        _parse_timestamp(point["value"], field)


def _parse_timestamp(value: Any, field: str) -> datetime:
    if not isinstance(value, str):
        raise ValueError(f"{field} must be an ISO 8601 string")
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        return datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise ValueError(f"{field} is not valid ISO 8601: {value}") from exc


def _published_timestamp(value: Any, field: str) -> str | None:
    """Validate source publication time without converting it to observation time."""

    if value in (None, "", "unknown"):
        return None
    if not isinstance(value, str):
        raise ValueError(f"{field} must be an ISO 8601 date/time string")
    result = f"{value}T00:00:00Z" if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value) else value
    _parse_timestamp(result, field)
    return result


def validate_curation(
    curation: dict[str, Any], ledger: dict[str, Any]
) -> list[dict[str, Any]]:
    """Validate the explicit allowlist and return ledger-backed records."""

    _parse_timestamp(curation.get("updated_at"), "updated_at")
    clusters = {item["cluster_id"]: item for item in ledger.get("clusters", [])}
    seen_activity_ids: set[str] = set()
    seen_clusters: set[str] = set()
    records: list[dict[str, Any]] = []
    for index, item in enumerate(curation.get("activities", [])):
        prefix = f"activities[{index}]"
        activity_id = item.get("activity_id", "")
        if not activity_id.startswith("activity--") or activity_id in seen_activity_ids:
            raise ValueError(f"{prefix}.activity_id is missing, invalid, or duplicated")
        seen_activity_ids.add(activity_id)
        cluster_id = item.get("ledger_cluster_id")
        if cluster_id in seen_clusters:
            raise ValueError(f"{prefix}.ledger_cluster_id is duplicated")
        seen_clusters.add(cluster_id)
        if cluster_id not in clusters:
            raise ValueError(f"{prefix} references missing ledger cluster {cluster_id}")
        object_type = item.get("stix_object_type")
        if object_type not in ALLOWED_ACTIVITY_TYPES:
            raise ValueError(f"{prefix}.stix_object_type is invalid")
        context = item.get("grouping_context")
        if object_type == "grouping" and context not in ALLOWED_GROUPING_CONTEXTS:
            raise ValueError(f"{prefix}.grouping_context is invalid")
        if object_type != "grouping" and context is not None:
            raise ValueError(f"{prefix}.grouping_context must be null")
        _validate_point(item.get("first_observed"), f"{prefix}.first_observed")
        _validate_point(item.get("last_observed"), f"{prefix}.last_observed")
        observation_indexes = item.get("observation_indexes")
        if not isinstance(observation_indexes, list) or not observation_indexes:
            raise ValueError(f"{prefix}.observation_indexes must be non-empty")
        observations = clusters[cluster_id].get("observations", [])
        if any(not isinstance(value, int) or value < 0 or value >= len(observations) for value in observation_indexes):
            raise ValueError(f"{prefix}.observation_indexes contains an invalid index")
        for observation_index in observation_indexes:
            observation = observations[observation_index]
            _published_timestamp(
                observation.get("published_at"),
                f"{prefix}.observations[{observation_index}].published_at",
            )
            for corroborating_index, corroborating in enumerate(
                observation.get("corroborating_sources", [])
            ):
                _published_timestamp(
                    corroborating.get("published_at"),
                    f"{prefix}.observations[{observation_index}]."
                    f"corroborating_sources[{corroborating_index}].published_at",
                )
        if item.get("confidence") not in CONFIDENCE:
            raise ValueError(f"{prefix}.confidence is invalid")
        if item.get("ioc_policy") not in {
            "none", "bigbear-primary-table", "secflow-primary-tables"
        }:
            raise ValueError(f"{prefix}.ioc_policy is invalid")
        records.append({"curation": item, "cluster": clusters[cluster_id]})
    return records


def _deobfuscate(value: str) -> str:
    return value.replace("[.]", ".").replace("[://]", "://")


def _drop_nulls(value: Any) -> Any:
    """Keep custom STIX evidence JSON null-free without inventing values."""

    if isinstance(value, dict):
        return {
            key: _drop_nulls(item)
            for key, item in value.items()
            if item is not None
        }
    if isinstance(value, list):
        return [_drop_nulls(item) for item in value if item is not None]
    return value


def _pattern(kind: str, value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace("'", "\\'")
    if kind == "ipv4":
        return f"[ipv4-addr:value = '{escaped}']"
    if kind == "domain":
        return f"[domain-name:value = '{escaped}']"
    if kind == "url":
        return f"[url:value = '{escaped}']"
    if kind == "sha256":
        return f"[file:hashes.'SHA-256' = '{escaped}']"
    raise ValueError(f"unsupported standalone indicator type: {kind}")


def _indicator_key(activity_id: str, kind: str, value: str) -> str:
    # Indicator is an Activity-scoped assertion. The same atomic value may be
    # reused by unrelated campaigns without sharing confidence/evidence.
    return f"standalone-indicator:{activity_id}:{kind}:{value}"


def _role_labels(roles: Any) -> list[str]:
    if not isinstance(roles, list):
        return []
    return sorted(
        {
            str(role).strip().casefold()
            for role in roles
            if len(str(role).strip()) <= 64
            and IOC_ROLE_LABEL.fullmatch(str(role).strip().casefold())
        }
    )


def _observable(
    kind: str, value: str, roles: list[str] | None = None
) -> dict[str, Any]:
    """Create the stable atomic SCO represented by a standalone Indicator."""

    stix_type = STANDALONE_OBSERVABLE_TYPES[kind]
    result: dict[str, Any] = {
        "type": stix_type,
        "spec_version": "2.1",
        "id": stix_id(stix_type, f"observable:{kind}:{value}"),
        "object_marking_refs": [TLP_CLEAR],
    }
    if kind == "sha256":
        result["hashes"] = {"SHA-256": value}
    else:
        result["value"] = value
    role_labels = _role_labels(roles or [])
    if role_labels:
        result["x_opencti_labels"] = role_labels
        result["x_ioc_roles"] = role_labels
        result["x_ioc_role_scope"] = "corpus-observed-uses"
    return result


def _indicator(
    *,
    kind: str,
    value: str,
    activity: dict[str, Any],
    updated_at: str,
    producer_ref: str,
    source_id: str,
    role: str,
    role_labels: list[str],
    observed_at: dict[str, Any] | None,
    source_row_count: int = 1,
) -> dict[str, Any]:
    point = observed_at or {
        "value": None,
        "precision": "unknown",
        "status": "unknown",
        "basis": "not-stated-for-individual-observable",
    }
    valid_from = point.get("value") or updated_at
    normalized_roles = _role_labels(role_labels)
    result = stix_base(
        "indicator",
        _indicator_key(activity["activity_id"], kind, value),
        updated_at,
        {
            "name": f"{kind}: {value}",
            "description": (
                "Source-scoped observable from an explicitly reviewed standalone "
                "Activity. It does not identify an actor and current validity was "
                "not inferred."
            ),
            "indicator_types": ["malicious-activity"],
            "pattern": _pattern(kind, value),
            "pattern_type": "stix",
            "valid_from": valid_from,
            "confidence": CONFIDENCE[activity["confidence"]],
            "created_by_ref": producer_ref,
            "external_references": [
                {"source_name": "standalone-activity-source", "external_id": source_id}
            ],
            "x_standalone_activity_id": activity["activity_id"],
            "x_indicator_type": kind,
            "x_indicator_value": value,
            "x_indicator_role": role,
            "x_ioc_roles": normalized_roles,
            "x_source_id": source_id,
            "x_source_scoped_observation_count": source_row_count,
            "x_first_observed": point,
            "x_temporal_basis": (
                "observed-at" if point.get("value") else "unknown"
            ),
            "x_time_correlation_eligible": bool(point.get("value")),
            "x_valid_from_basis": (
                point.get("basis")
                if point.get("value")
                else "schema-generation-time-not-observation"
            ),
        },
    )
    if normalized_roles:
        result["labels"] = normalized_roles
    return result


def _bigbear_indicators(
    observation: dict[str, Any], activity: dict[str, Any], updated_at: str,
    producer_ref: str, source_id: str,
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    table = observation.get("indicators", {})
    groups = {
        "vps_nodes": "vps-node",
        "historical_vps_nodes": "historical-vps-node",
        "phishing_domains": "phishing-domain",
        "historical_phishing_domains": "historical-phishing-domain",
    }
    result: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    observations = 0
    for field, role in groups.items():
        for raw in table.get(field, []):
            observations += 1
            value = _deobfuscate(str(raw).strip()).lower()
            kind = "ipv4" if field.endswith("vps_nodes") else "domain"
            if kind == "ipv4":
                ipaddress.IPv4Address(value)
            elif not re.fullmatch(r"(?=.{1,253}$)[a-z0-9.-]+\.[a-z]{2,63}", value):
                raise ValueError(f"invalid BigBear domain: {value}")
            key = (kind, value)
            if key in seen:
                raise ValueError(f"duplicate BigBear structured IOC: {key}")
            seen.add(key)
            result.append(
                _indicator(
                    kind=kind, value=value, activity=activity,
                    updated_at=updated_at, producer_ref=producer_ref,
                    source_id=source_id, role=role,
                    role_labels=[role], observed_at=None,
                )
            )
    if observations != 48 or len(result) != 48:
        raise ValueError(
            f"BigBear reviewed table must contain 48 unique IOCs, got {observations}/{len(result)}"
        )
    return result, {
        "indicator_count": len(result),
        "source_observation_count": observations,
        "non_promoted_feature_count": 0,
    }


def _secflow_observation_dates(observation: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    rows = observation.get("indicators", {}).get("dated_workspace_observations", [])
    for row in rows:
        match = re.match(r"^(\d{4}-\d{2}-\d{2})\s+(\d+(?:\.\d+){3})", _deobfuscate(row))
        if match:
            result[match.group(2)] = {
                "value": f"{match.group(1)}T00:00:00Z",
                "precision": "day", "status": "known", "basis": "source-stated",
            }
    return result


def _secflow_indicators(
    observation: dict[str, Any], activity: dict[str, Any], updated_at: str,
    producer_ref: str, source_id: str,
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    table = observation.get("indicators", {})
    date_by_ip = _secflow_observation_dates(observation)
    accumulated: dict[tuple[str, str], dict[str, Any]] = {}
    promoted_observations = 0
    non_promoted = 0

    for raw in table.get("operator_and_support_infrastructure", []):
        token = _deobfuscate(str(raw).split(" ", 1)[0]).lower()
        if token.startswith("*."):
            # A wildcard family is a hunting clue, not an exact IOC. It remains
            # in the source Note via x_ledger_observation.
            non_promoted += 1
            continue
        if token.startswith(("tcp://", "wss://")):
            kind, value = "url", token
        else:
            match = re.match(r"^(\d+(?:\.\d+){3})", token)
            if not match:
                raise ValueError(f"unhandled SecFlow infrastructure row: {raw}")
            kind, value = "ipv4", match.group(1)
            ipaddress.IPv4Address(value)
        promoted_observations += 1
        key = (kind, value)
        current = accumulated.setdefault(
            key,
            {
                "count": 0,
                "roles": [],
                "role_labels": {"infrastructure"},
                "observed_at": date_by_ip.get(value),
            },
        )
        current["count"] += 1
        current["roles"].append(str(raw))

    for raw in table.get("payload_sha256", []):
        value = str(raw).split(" ", 1)[0].lower()
        if not re.fullmatch(r"[0-9a-f]{64}", value):
            raise ValueError(f"invalid SecFlow SHA-256 row: {raw}")
        promoted_observations += 1
        key = ("sha256", value)
        if key in accumulated:
            raise ValueError(f"duplicate SecFlow SHA-256: {value}")
        accumulated[key] = {
            "count": 1,
            "roles": [str(raw)],
            "role_labels": {"payload"},
            "observed_at": None,
        }

    result = [
        _indicator(
            kind=kind,
            value=value,
            activity=activity,
            updated_at=updated_at,
            producer_ref=producer_ref,
            source_id=source_id,
            role=" | ".join(metadata["roles"]),
            role_labels=sorted(metadata["role_labels"]),
            observed_at=metadata["observed_at"],
            source_row_count=metadata["count"],
        )
        for (kind, value), metadata in sorted(accumulated.items())
    ]
    if len(result) != 38 or promoted_observations != 40 or non_promoted != 1:
        raise ValueError(
            "SecFlow reviewed tables must produce 38 unique exact Indicators "
            f"from 40 rows with 1 non-promoted wildcard; got {len(result)}, "
            f"{promoted_observations}, {non_promoted}"
        )
    return result, {
        "indicator_count": len(result),
        "source_observation_count": promoted_observations,
        "non_promoted_feature_count": non_promoted,
    }


def _source_records(
    activity: dict[str, Any], cluster: dict[str, Any]
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for position, observation_index in enumerate(activity["observation_indexes"]):
        observation = copy.deepcopy(cluster["observations"][observation_index])
        records.append(
            {
                "source_id": _source_id(activity["activity_id"], position),
                "observation_index": observation_index,
                "observation": observation,
            }
        )
        for corroborating_index, source in enumerate(
            observation.get("corroborating_sources", [])
        ):
            records.append(
                {
                    "source_id": _source_id(
                        activity["activity_id"], position, f"corroborating-{corroborating_index}"
                    ),
                    "observation_index": observation_index,
                    "observation": copy.deepcopy(source),
                    "corroborating": True,
                }
            )
    return records


def _note_content(cluster: dict[str, Any], observation: dict[str, Any]) -> str:
    parts = [
        str(observation.get("summary") or observation.get("claim") or "Source evidence."),
        f"Activity period: {observation.get('activity_period') or 'unknown'}",
        f"Targets: {observation.get('targets') or 'unknown'}",
        f"Attribution caveat: {cluster.get('attribution', {}).get('notes', 'unknown')}",
    ]
    return "\n\n".join(parts)


def build_standalone_activity_bundle(
    *,
    record: dict[str, Any],
    updated_at: str,
    producer: dict[str, Any],
    model_modified_at: str | None = None,
    observable_role_index: dict[str, list[str]] | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Build one actor-free and reference-complete standalone bundle."""

    activity = record["curation"]
    cluster = record["cluster"]
    generated_modified = max(updated_at, model_modified_at or updated_at)
    source_records = _source_records(activity, cluster)
    sources_by_id = {item["source_id"]: item["observation"] for item in source_records}
    activity_ref = stix_id(activity["stix_object_type"], activity["activity_id"])
    external_references = [
        _external_reference(source_id, source)
        for source_id, source in sources_by_id.items()
    ]
    primary_extra: dict[str, Any] = {
        "name": activity["name"],
        "description": cluster.get("analyst_notes") or activity["decision"],
        "confidence": CONFIDENCE[activity["confidence"]],
        "created_by_ref": producer["id"],
        "external_references": external_references,
        "x_profile_object_id": activity["activity_id"],
        "x_standalone_activity": True,
        "x_ledger_cluster_id": activity["ledger_cluster_id"],
        "x_curation_decision": activity["decision"],
        "x_ioc_promotion_policy": activity["ioc_policy"],
        "x_unstructured_observables_promoted": False,
        "x_attribution": cluster.get("attribution", {}),
        "x_first_observed": activity["first_observed"],
        "x_last_observed": activity["last_observed"],
        "x_time_basis": cluster.get("time_basis") or "unknown",
    }
    if activity["stix_object_type"] == "campaign":
        if activity["first_observed"].get("value"):
            primary_extra["first_seen"] = activity["first_observed"]["value"]
        if activity["last_observed"].get("value"):
            primary_extra["last_seen"] = activity["last_observed"]["value"]
    elif activity["stix_object_type"] == "grouping":
        primary_extra["context"] = activity["grouping_context"]
        primary_extra["object_refs"] = []
    primary = stix_base(
        activity["stix_object_type"], activity["activity_id"], updated_at, primary_extra
    )

    notes: list[dict[str, Any]] = []
    source_note_ids: dict[str, str] = {}
    for source_record in source_records:
        source_id = source_record["source_id"]
        source = source_record["observation"]
        note = stix_base(
            "note",
            f"standalone-source-note:{activity['activity_id']}:{source_id}",
            updated_at,
            {
                "abstract": source.get("title") or f"Evidence for {activity['name']}",
                "content": _note_content(cluster, source),
                "object_refs": [activity_ref],
                "created_by_ref": producer["id"],
                "external_references": [_external_reference(source_id, source)],
                "x_standalone_activity_id": activity["activity_id"],
                "x_source_id": source_id,
                "x_source_publication_only": source.get("published_at") or "unknown",
                "x_ledger_observation": _drop_nulls(source),
                "x_unresolved_questions": cluster.get("unresolved_questions", []),
                "x_related_profiles_are_unpromoted": cluster.get("related_profiles", []),
            },
        )
        notes.append(note)
        source_note_ids[source_id] = note["id"]

    indicators: list[dict[str, Any]] = []
    ioc_counts = {
        "indicator_count": 0,
        "source_observation_count": 0,
        "non_promoted_feature_count": 0,
    }
    primary_source = source_records[0]
    if activity["ioc_policy"] == "bigbear-primary-table":
        indicators, ioc_counts = _bigbear_indicators(
            primary_source["observation"], activity, updated_at,
            producer["id"], primary_source["source_id"],
        )
    elif activity["ioc_policy"] == "secflow-primary-tables":
        indicators, ioc_counts = _secflow_indicators(
            primary_source["observation"], activity, updated_at,
            producer["id"], primary_source["source_id"],
        )
    observables_by_id: dict[str, dict[str, Any]] = {}
    based_on_relationships: list[dict[str, Any]] = []
    for indicator in indicators:
        kind = indicator["x_indicator_type"]
        unlabelled = _observable(kind, indicator["x_indicator_value"])
        roles = indicator.get("x_ioc_roles", [])
        if observable_role_index is not None:
            roles = observable_role_index.get(unlabelled["id"], roles)
        observable = _observable(
            kind, indicator["x_indicator_value"], roles
        )
        observables_by_id[observable["id"]] = observable
        indicator["x_opencti_main_observable_type"] = (
            OPENCTI_MAIN_OBSERVABLE_TYPES[kind]
        )
        indicator["modified"] = generated_modified
        based_on_relationships.append(
            stix_base(
                "relationship",
                f"{indicator['id']}:based-on:{observable['id']}",
                generated_modified,
                {
                    "relationship_type": "based-on",
                    "source_ref": indicator["id"],
                    "target_ref": observable["id"],
                    "description": (
                        "The Indicator directly represents this atomic "
                        "Observable from the same reviewed standalone source row."
                    ),
                    "confidence": indicator["confidence"],
                    "created_by_ref": producer["id"],
                    "external_references": indicator[
                        "external_references"
                    ],
                    "x_standalone_indicator_id": indicator["id"],
                    "x_standalone_activity_id": activity["activity_id"],
                    "x_source_id": indicator["x_source_id"],
                    "x_ioc_roles": indicator.get("x_ioc_roles", []),
                    "x_ioc_role_source_refs": [indicator["x_source_id"]],
                },
            )
        )
    primary["x_structured_ioc_indicator_count"] = ioc_counts["indicator_count"]
    primary["x_structured_ioc_source_observation_count"] = ioc_counts[
        "source_observation_count"
    ]
    primary["x_non_promoted_feature_count"] = ioc_counts[
        "non_promoted_feature_count"
    ]

    relationships: list[dict[str, Any]] = [*based_on_relationships]
    if activity["stix_object_type"] in {"campaign", "incident"}:
        for indicator in indicators:
            relationships.append(
                stix_base(
                    "relationship",
                    f"{indicator['id']}:indicates:{activity_ref}",
                    updated_at,
                    {
                        "relationship_type": "indicates",
                        "source_ref": indicator["id"],
                        "target_ref": activity_ref,
                        "description": (
                            "The reviewed source explicitly scopes this observable "
                            "to the standalone Activity; it does not attribute an actor."
                        ),
                        "confidence": indicator["confidence"],
                        "created_by_ref": producer["id"],
                        "external_references": indicator["external_references"],
                        "x_temporal_basis": "unknown",
                        "x_time_correlation_eligible": False,
                    },
                )
            )

    observables = list(observables_by_id.values())
    knowledge: list[dict[str, Any]] = [
        primary,
        *notes,
        *observables,
        *indicators,
        *relationships,
    ]
    if activity["stix_object_type"] == "grouping":
        primary["object_refs"] = sorted(
            obj["id"] for obj in knowledge if obj["id"] != primary["id"]
        )

    source_reports: list[dict[str, Any]] = []
    indicators_by_source: dict[str, list[dict[str, Any]]] = defaultdict(list)
    relationships_by_source: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for indicator in indicators:
        indicators_by_source[indicator["x_source_id"]].append(indicator)
    for relationship in relationships:
        source_id = relationship.get("external_references", [{}])[0].get("external_id")
        if source_id:
            relationships_by_source[source_id].append(relationship)
    for source_id, source in sources_by_id.items():
        published = _published_timestamp(
            source.get("published_at"), f"source {source_id}.published_at"
        )
        if not published:
            continue
        refs = {
            activity_ref,
            source_note_ids[source_id],
            *(obj["id"] for obj in indicators_by_source[source_id]),
            *(obj["id"] for obj in relationships_by_source[source_id]),
            *(
                obj["target_ref"]
                for obj in relationships_by_source[source_id]
                if obj.get("relationship_type") == "based-on"
            ),
        }
        source_report = stix_base(
            "report",
            f"standalone-source-report:{activity['activity_id']}:{source_id}",
            updated_at,
            {
                "name": source.get("title") or source_id,
                "description": (
                    "Source publication container. Its published time is not an "
                    "Activity observation or Relationship validity time."
                ),
                "report_types": ["threat-report"],
                "published": published,
                "object_refs": sorted(refs),
                "created_by_ref": producer["id"],
                "external_references": [_external_reference(source_id, source)],
                "x_opencti_source_report": True,
                "x_source_id": source_id,
                "x_source_publisher": source.get("publisher") or "unknown",
                "x_source_type": source.get("source_type") or "unknown",
                "x_source_reliability": source.get("reliability") or "unknown",
                "x_published_precision": "day",
                "x_published_status": "known",
                "x_published_basis": "source-stated",
                "x_temporal_role": "publication-only",
                "x_standalone_activity_id": activity["activity_id"],
            },
        )
        source_report["modified"] = generated_modified
        source_reports.append(source_report)
    knowledge.extend(source_reports)

    container = stix_base(
        "report",
        f"opencti-standalone-report:{activity['activity_id']}",
        updated_at,
        {
            "name": f"Standalone Activity / {activity['name']}",
            "description": activity["decision"],
            "report_types": [
                "campaign" if activity["stix_object_type"] == "campaign" else "threat-report"
            ],
            "published": updated_at,
            "object_refs": sorted(obj["id"] for obj in knowledge),
            "created_by_ref": producer["id"],
            "x_opencti_bundle_scope": activity["stix_object_type"],
            "x_activity_id": activity["activity_id"],
            "x_standalone_activity": True,
            "x_temporal_role": "bundle-generation-time",
            "x_generated_at": updated_at,
        },
    )
    container["modified"] = generated_modified
    objects_by_id = {producer["id"]: producer}
    objects_by_id.update({obj["id"]: obj for obj in knowledge})
    objects_by_id[container["id"]] = container
    ordered = [objects_by_id[producer["id"]]]
    ordered.extend(
        objects_by_id[obj_id]
        for obj_id in sorted(objects_by_id)
        if obj_id not in {producer["id"], container["id"]}
    )
    ordered.append(container)
    bundle = {
        "type": "bundle",
        "id": stix_id("bundle", f"opencti-standalone:{activity['activity_id']}"),
        "objects": ordered,
    }
    metadata = {
        "activity_id": activity["activity_id"],
        "ledger_cluster_id": activity["ledger_cluster_id"],
        "name": activity["name"],
        "stix_object_type": activity["stix_object_type"],
        "structured_ioc_indicator_count": ioc_counts["indicator_count"],
        "structured_ioc_observable_count": len(observables),
        "structured_ioc_based_on_count": len(based_on_relationships),
        "structured_ioc_source_observation_count": ioc_counts[
            "source_observation_count"
        ],
        "non_promoted_feature_count": ioc_counts["non_promoted_feature_count"],
    }
    return bundle, metadata
