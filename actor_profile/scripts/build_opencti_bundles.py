#!/usr/bin/env python3
"""Build self-contained OpenCTI import bundles by actor and modeled activity.

The canonical actor profile remains the source of truth.  This exporter consumes
the already-rendered STIX bundle and rewrites it into smaller, self-contained
STIX 2.1 bundles that can be uploaded through OpenCTI's ImportFileStix connector.
"""

from __future__ import annotations

import argparse
import copy
import json
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

from common import load_json, write_json_atomic
from render_profile import (
    TLP_CLEAR,
    actor_alias_evidence_refs,
    external_refs,
    opencti_identity_aliases,
    relationship_time_properties,
    stix_base,
    stix_id,
)
from stix_modeling import activity_stix_object_type
from standalone_activity_stix import (
    build_standalone_activity_bundle,
    validate_curation as validate_standalone_curation,
)


CONFIDENCE_SCORE = {
    "high": 85,
    "medium": 60,
    "low": 30,
    "unknown": 0,
}
PRODUCER_KEY = "opencti-export:proshiba/threatactor-intel-analysis"
REPOSITORY_URL = "https://github.com/proshiba/threatactor-intel-analysis"
# These timestamps version the producer Identity itself, not the newest item in
# the exported corpus. Bump PRODUCER_MODIFIED only when the Identity metadata
# below changes. Deriving it from max(profile.updated_at) rewrites every bundle
# after an unrelated actor update and can produce conflicting versions during a
# partial import.
PRODUCER_CREATED = "2026-07-25T00:00:00Z"
PRODUCER_MODIFIED = "2026-09-21T13:20:00Z"
# Version the OpenCTI export model independently from canonical intelligence.
# A representation-only change (for example adding an explicit based-on SRO)
# must advance modified on affected generated objects without pretending that
# every source profile received new OSINT on the same day.
OPENCTI_MODEL_MODIFIED = "2026-09-24T14:03:24Z"
DEFAULT_OPENCTI_COUNTRY_INDEX = Path(
    "actor_profile/reference/opencti-country-index.json"
)
DEFAULT_STANDALONE_CURATION = Path(
    "actor_profile/standalone-activity-curation.json"
)
DEFAULT_UNKNOWN_CLUSTER_LEDGER = Path("parse-daily/unknown-clusters.json")
OPENCTI_SAFE_ACTOR_RELATIONSHIPS = {"part-of", "related-to"}
REFERENCE_FIELDS = ("source_ref", "target_ref", "created_by_ref")
REFERENCE_LIST_FIELDS = ("object_refs", "object_marking_refs")
IOC_OBSERVABLE_TYPES = {
    "domain": "domain-name",
    "email": "email-addr",
    "ipv4": "ipv4-addr",
    "ipv6": "ipv6-addr",
    "url": "url",
    "certificate-fingerprint": "x509-certificate",
    "md5": "file",
    "sha1": "file",
    "sha256": "file",
    "sha512": "file",
}
HASH_ALGORITHMS = {
    "md5": "MD5",
    "sha1": "SHA-1",
    "sha256": "SHA-256",
    "sha512": "SHA-512",
}
OPENCTI_MAIN_OBSERVABLE_TYPES = {
    "domain-name": "Domain-Name",
    "email-addr": "Email-Addr",
    "file": "StixFile",
    "ipv4-addr": "IPv4-Addr",
    "ipv6-addr": "IPv6-Addr",
    "url": "Url",
    "x509-certificate": "X509-Certificate",
}
ATOMIC_OBSERVABLE_TYPES = set(OPENCTI_MAIN_OBSERVABLE_TYPES)
UNVERSIONED_OBSERVABLE_ROLE_FIELDS = {
    "x_opencti_labels",
    "x_ioc_roles",
    "x_ioc_role_scope",
}
PATTERN_VALUE_IOC_TYPES = {
    "domain-name": "domain",
    "email-addr": "email",
    "ipv4-addr": "ipv4",
    "ipv6-addr": "ipv6",
    "url": "url",
}
PATTERN_HASH_IOC_TYPES = {
    "MD5": "md5",
    "SHA-1": "sha1",
    "SHA-256": "sha256",
    "SHA-512": "sha512",
}
PATTERN_VALUE_TERM = re.compile(
    r"(?P<type>domain-name|email-addr|ipv4-addr|ipv6-addr|url):value"
    r"\s*=\s*'(?P<value>(?:\\.|[^'])*)'"
)
PATTERN_HASH_TERM = re.compile(
    r"(?P<type>file|x509-certificate):hashes\."
    r"'(?P<algorithm>MD5|SHA-1|SHA-256|SHA-512)'"
    r"\s*=\s*'(?P<value>(?:\\.|[^'])*)'"
)
PATTERN_X509_SERIAL_TERM = re.compile(
    r"x509-certificate:serial_number\s*=\s*"
    r"'(?P<value>(?:\\.|[^'])*)'"
)
IOC_ROLE_LABEL = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def normalized_actor_key(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value or "").casefold()
    return "".join(character for character in normalized if character.isalnum())


def confidence_score(value: Any) -> int:
    return CONFIDENCE_SCORE.get(str(value or "unknown").lower(), 0)


def opencti_modified(profile: dict[str, Any]) -> str:
    """Return the later of intelligence and exporter-model modification."""

    return max(profile["updated_at"], OPENCTI_MODEL_MODIFIED)


def source_reference(
    source_id: str, source: dict[str, Any] | None
) -> dict[str, Any]:
    source = source or {}
    path = str(source.get("url") or source.get("path") or "")
    result: dict[str, Any] = {
        "source_name": source.get("publisher") or source.get("title") or "local-source",
        "external_id": source_id,
    }
    if path.startswith(("https://", "http://")):
        result["url"] = path
    elif path:
        result["description"] = f"Repository source: {path}"
    else:
        result["description"] = "Source metadata retained in the actor profile."
    return result


def merge_external_references(
    current: list[dict[str, Any]], additions: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()
    for item in [*current, *additions]:
        key = (
            str(item.get("source_name", "")),
            str(item.get("external_id", "")),
            str(item.get("url", "")),
        )
        if key in seen:
            continue
        seen.add(key)
        result.append(item)
    return result


def producer_identity(created: str, modified: str) -> dict[str, Any]:
    return {
        "type": "identity",
        "spec_version": "2.1",
        "id": stix_id("identity", PRODUCER_KEY),
        "created": created,
        "modified": modified,
        "name": "Threat Actor Intelligence Profiles",
        "description": (
            "Open-source threat actor intelligence exported by "
            "proshiba/threatactor-intel-analysis."
        ),
        "identity_class": "organization",
        "confidence": 100,
        "external_references": [
            {"source_name": "GitHub", "url": REPOSITORY_URL}
        ],
        "object_marking_refs": [TLP_CLEAR],
    }


def repository_producer_identity() -> dict[str, Any]:
    """Return the corpus-wide producer at its own pinned object version."""

    return producer_identity(PRODUCER_CREATED, PRODUCER_MODIFIED)


def ioc_role_labels(roles: Any) -> list[str]:
    """Return evidence-backed IOC roles that are safe as OpenCTI labels.

    Roles are deliberately not guessed from the Observable type, actor, or
    surrounding Campaign.  Only the structured ``roles`` values carried by an
    IOC observation are eligible.  Free text is rejected rather than silently
    turned into a broad or misleading label.
    """

    if not isinstance(roles, list):
        return []
    result: set[str] = set()
    for raw in roles:
        value = unicodedata.normalize("NFKC", str(raw)).strip().casefold()
        if len(value) <= 64 and IOC_ROLE_LABEL.fullmatch(value):
            result.add(value)
    return sorted(result)


def apply_observable_roles(
    observable: dict[str, Any], roles: Any
) -> dict[str, Any]:
    """Attach corpus-scoped, evidence-backed role labels to an Observable."""

    role_labels = ioc_role_labels(roles)
    if role_labels:
        # SCOs do not have a standard STIX ``labels`` property. OpenCTI's
        # importer supports this explicit extension on Observables.
        observable["x_opencti_labels"] = role_labels
        observable["x_ioc_roles"] = role_labels
        observable["x_ioc_role_scope"] = "corpus-observed-uses"
    return observable


def observable_object(
    indicator: dict[str, Any],
    *,
    roles: list[str] | None = None,
) -> dict[str, Any] | None:
    """Create one stable atomic SCO represented by a canonical IOC."""

    indicator_type = indicator.get("type")
    stix_type = IOC_OBSERVABLE_TYPES.get(indicator_type)
    if not stix_type:
        return None
    value = indicator.get("normalized_value") or indicator.get("value")
    if not value:
        return None
    key = f"observable:{indicator_type}:{value}"
    result: dict[str, Any] = {
        "type": stix_type,
        "spec_version": "2.1",
        "id": stix_id(stix_type, key),
        "object_marking_refs": [TLP_CLEAR],
    }
    if stix_type == "file":
        algorithm = HASH_ALGORITHMS[indicator_type]
        result["hashes"] = {algorithm: value}
    elif stix_type == "x509-certificate":
        algorithm = HASH_ALGORITHMS.get(indicator.get("hash_algorithm"))
        if not algorithm:
            return None
        result["hashes"] = {algorithm: value}
    else:
        result["value"] = value
    return apply_observable_roles(
        result,
        indicator.get("roles", []) if roles is None else roles,
    )


def _unescape_stix_pattern_value(value: str) -> str:
    return value.replace("\\'", "'").replace("\\\\", "\\")


def observable_objects_from_indicator_pattern(
    indicator: dict[str, Any],
    observable_role_index: dict[str, list[str]] | None = None,
) -> list[dict[str, Any]]:
    """Extract exact atomic SCOs from a reviewed Hunting Pivot pattern.

    Only an OR-list of exact equality terms is accepted. ``MATCHES``, compound
    predicates and other non-atomic patterns intentionally remain Indicator +
    Note only, because materializing a concrete SCO would invent an observed
    value.
    """

    if not indicator.get("x_hunting_pivot"):
        return []
    pattern = str(indicator.get("pattern") or "").strip()
    if not pattern.startswith("[") or not pattern.endswith("]"):
        return []
    terms = re.split(r"\s+OR\s+", pattern[1:-1].strip())
    observables: dict[str, dict[str, Any]] = {}
    for term in terms:
        value_match = PATTERN_VALUE_TERM.fullmatch(term.strip())
        if value_match:
            stix_type = value_match.group("type")
            value = _unescape_stix_pattern_value(
                value_match.group("value")
            )
            if stix_type in {"domain-name", "email-addr"}:
                value = value.lower()
            observable = observable_object(
                {
                    "type": PATTERN_VALUE_IOC_TYPES[stix_type],
                    "normalized_value": value,
                }
            )
        else:
            hash_match = PATTERN_HASH_TERM.fullmatch(term.strip())
            if hash_match:
                stix_type = hash_match.group("type")
                algorithm = hash_match.group("algorithm")
                value = _unescape_stix_pattern_value(
                    hash_match.group("value")
                ).lower()
                observable = observable_object(
                    {
                        "type": (
                            PATTERN_HASH_IOC_TYPES[algorithm]
                            if stix_type == "file"
                            else "certificate-fingerprint"
                        ),
                        "normalized_value": value,
                        "hash_algorithm": PATTERN_HASH_IOC_TYPES[algorithm],
                    }
                )
            else:
                serial_match = PATTERN_X509_SERIAL_TERM.fullmatch(
                    term.strip()
                )
                if not serial_match:
                    return []
                value = _unescape_stix_pattern_value(
                    serial_match.group("value")
                ).lower()
                observable = {
                    "type": "x509-certificate",
                    "spec_version": "2.1",
                    "id": stix_id(
                        "x509-certificate",
                        f"observable:x509-serial:{value}",
                    ),
                    "serial_number": value,
                    "object_marking_refs": [TLP_CLEAR],
                }
        if not observable:
            return []
        if observable_role_index and observable["id"] in observable_role_index:
            apply_observable_roles(
                observable, observable_role_index[observable["id"]]
            )
        observables[observable["id"]] = observable
    return [observables[object_id] for object_id in sorted(observables)]


def build_observable_role_index(
    records: list[dict[str, Any]],
    standalone_bundles: list[dict[str, Any]] | None = None,
) -> dict[str, list[str]]:
    """Aggregate roles for shared atomic SCOs across the complete corpus.

    Atomic SCO IDs are intentionally reused between actor and Activity
    bundles.  Their label sets must therefore be corpus-wide and byte-identical
    rather than depending on whichever profile happened to be imported first.
    """

    roles_by_id: dict[str, set[str]] = defaultdict(set)
    for record in records:
        for indicator in record.get("iocs", {}).get("indicators", []):
            if indicator.get("disposition") == "rejected":
                continue
            observable = observable_object(indicator, roles=[])
            if observable:
                roles_by_id[observable["id"]].update(
                    ioc_role_labels(indicator.get("roles", []))
                )
    for bundle in standalone_bundles or []:
        for observable in bundle.get("objects", []):
            if observable.get("type") not in ATOMIC_OBSERVABLE_TYPES:
                continue
            roles_by_id[observable["id"]].update(
                ioc_role_labels(observable.get("x_ioc_roles", []))
            )
    return {
        object_id: sorted(roles)
        for object_id, roles in roles_by_id.items()
        if roles
    }


PROFILE_SCOPED_OBJECT_TYPES = {
    "attack-pattern",
    "campaign",
    "grouping",
    "incident",
    "indicator",
    "infrastructure",
    "malware",
    "note",
    "relationship",
    "tool",
}


def profile_scoped_stix_id(profile_id: str, kind: str, object_id: str) -> str:
    """Return a stable ID for knowledge whose semantics belong to one profile.

    Canonical profile IDs such as ``ttp--T1059.003`` and
    ``malware--powershell`` are intentionally human-readable and can occur in
    more than one actor profile.  Their rendered descriptions, evidence and
    observation metadata are actor-specific, so reusing a bare STIX ID would
    make OpenCTI overwrite one profile's SDO with another profile's content.
    """

    return stix_id(kind, f"{profile_id}:{object_id}")


def scope_profile_owned_objects(
    profile: dict[str, Any], objects: list[dict[str, Any]]
) -> None:
    """Namespace profile-owned SDO/SRO IDs and rewrite their references.

    Globally reusable objects (the canonical Intrusion Set, associated legal
    entities, verified Locations and atomic SCOs) keep their shared IDs.  TTP
    rows, capabilities, activities, Indicators and evidence containers remain
    actor-scoped because the canonical model stores profile-specific claims in
    those objects.
    """

    target_and_victim_refs = {
        item["id"]
        for category in ("countries", "regions", "sectors", "roles")
        for item in profile.get("targets", {}).get(category, [])
    } | {
        item["victim_case_id"] for item in profile.get("victim_cases", [])
    }
    rewrites: dict[str, str] = {}
    for obj in objects:
        kind = obj.get("type", "")
        profile_object_id = obj.get("x_profile_object_id")
        is_profile_identity = (
            kind == "identity"
            and profile_object_id in target_and_victim_refs
        )
        if kind not in PROFILE_SCOPED_OBJECT_TYPES and not is_profile_identity:
            continue
        old_id = obj["id"]
        rewrites[old_id] = profile_scoped_stix_id(
            profile["profile_id"], kind, old_id
        )

    for obj in objects:
        obj["id"] = rewrites.get(obj["id"], obj["id"])
        for key in REFERENCE_FIELDS:
            if obj.get(key) in rewrites:
                obj[key] = rewrites[obj[key]]
        for key in REFERENCE_LIST_FIELDS:
            if key in obj:
                obj[key] = [rewrites.get(ref, ref) for ref in obj[key]]


def normalize_shared_object_versions(records: list[dict[str, Any]]) -> None:
    """Make every deliberately shared object byte-identical across profiles.

    ``created`` and ``modified`` are version metadata, not a reason to emit
    conflicting definitions for one STIX ID.  Profile-owned objects have
    already been namespaced; any remaining semantic disagreement is therefore
    a generator error and is rejected rather than resolved by arbitrary
    first-wins behavior.
    """

    by_id: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        for obj in record["objects"]:
            by_id[obj["id"]].append(obj)
    for object_id, objects in by_id.items():
        if len(objects) < 2:
            continue
        semantic_versions = {
            json.dumps(
                {
                    key: value
                    for key, value in obj.items()
                    if key not in {"created", "modified"}
                },
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            )
            for obj in objects
        }
        if len(semantic_versions) != 1:
            raise ValueError(
                "shared STIX ID has conflicting semantics after profile "
                f"scoping: {object_id}"
            )
        created_values = [obj["created"] for obj in objects if obj.get("created")]
        modified_values = [
            obj["modified"] for obj in objects if obj.get("modified")
        ]
        for obj in objects:
            if created_values:
                obj["created"] = min(created_values)
            if modified_values:
                obj["modified"] = max(modified_values)


def indicator_temporal_properties(
    indicator: dict[str, Any],
) -> dict[str, Any]:
    """Separate actual observation time from report-publication fallback."""

    observations = indicator.get("observations", [])
    observed = [
        item["observed_at"]
        for item in observations
        if item.get("observed_at", {}).get("value")
    ]
    publications = sorted(
        (
            {
                "source_id": item.get("source_id", ""),
                **item["source_published_at"],
            }
            for item in observations
            if item.get("source_published_at", {}).get("value")
        ),
        key=lambda item: (item.get("value", ""), item.get("source_id", "")),
    )
    extra: dict[str, Any] = {
        "x_temporal_basis": (
            "observed-at"
            if observed
            else "report-published-fallback"
            if publications
            else "unknown"
        ),
        "x_time_correlation_eligible": bool(observed),
        "x_report_published_fallback": publications,
    }
    if observed:
        first = min(observed, key=lambda item: item["value"])
        last = max(observed, key=lambda item: item["value"])
        extra["x_first_observed"] = first
        extra["x_last_observed"] = last
        extra["start_time"] = first["value"]
        if last["value"] > first["value"]:
            extra["stop_time"] = last["value"]
    return extra


def target_metadata(profile: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for category in ("countries", "regions", "sectors", "roles"):
        for target in profile.get("targets", {}).get(category, []):
            old_id = stix_id("identity", target["id"])
            result[old_id] = {"category": category, "target": target}
    return result


def prepare_profile_objects(
    profile: dict[str, Any],
    iocs: dict[str, Any],
    full_bundle: dict[str, Any],
    producer_ref: str,
    country_index: dict[str, dict[str, Any]] | None = None,
    observable_role_index: dict[str, list[str]] | None = None,
) -> tuple[list[dict[str, Any]], dict[str, str]]:
    """Normalize rendered objects for OpenCTI and return rewritten target IDs."""

    targets = target_metadata(profile)
    activities = {
        stix_id(activity_stix_object_type(item), item["activity_id"]): item
        for item in profile.get("activities", [])
    }
    id_rewrites: dict[str, str] = {}
    for old_id, metadata in targets.items():
        category = metadata["category"]
        if category in {"countries", "regions"}:
            id_rewrites[old_id] = stix_id(
                "location", metadata["target"]["id"]
            )

    source_by_id = {
        item["source_id"]: item
        for item in [*profile.get("sources", []), *iocs.get("sources", [])]
        if item.get("source_id")
    }
    prepared: list[dict[str, Any]] = []
    target_relationship_evidence: dict[str, dict[str, Any]] = {}
    for original in full_bundle.get("objects", []):
        if original.get("type") == "report":
            continue
        obj = copy.deepcopy(original)
        old_id = obj.get("id", "")
        metadata = targets.get(old_id)
        if metadata:
            category = metadata["category"]
            target = metadata["target"]
            obj["x_profile_object_id"] = target["id"]
            obj["confidence"] = confidence_score(target.get("confidence"))
            if category in {"countries", "regions"}:
                obj["type"] = "location"
                obj["id"] = id_rewrites[old_id]
                obj.pop("identity_class", None)
                obj["x_opencti_location_type"] = (
                    "Country" if category == "countries" else "Region"
                )
                if category == "countries" and country_index:
                    country = country_index.get(target["name"])
                else:
                    country = None
                if country:
                    # Match OpenCTI's built-in Country contributing properties
                    # while retaining the upstream ID as a traceable reference.
                    # Actor-specific target evidence belongs to the relationship,
                    # not to the shared Country entity that OpenCTI deduplicates.
                    target_relationship_evidence[obj["id"]] = {
                        "description": obj.pop("description", ""),
                        "external_references": obj.pop(
                            "external_references", []
                        ),
                    }
                    obj["name"] = country["name"]
                    obj["country"] = country["country"]
                    obj["x_opencti_reference_id"] = country["id"]
                    aliases = {
                        target["name"],
                        *country.get("aliases", []),
                    }
                    obj["x_opencti_aliases"] = sorted(aliases)
                    for coordinate in ("latitude", "longitude"):
                        if coordinate in country:
                            obj[coordinate] = country[coordinate]
                    obj.pop("x_confidence", None)
                    obj["confidence"] = 100
                else:
                    # STIX 2.1 requires every Location to contain country,
                    # region, or coordinates.  Never invent a code when the
                    # pinned OpenCTI reference data has no verified match.
                    obj[
                        "country" if category == "countries" else "region"
                    ] = target["name"]
            else:
                obj["identity_class"] = "class"

        if obj.get("type") == "intrusion-set":
            # The complete cross-check remains in osint-crosscheck.json.  It is
            # too large and too repository-specific to be an OpenCTI property.
            crosscheck = obj.pop("x_osint_crosscheck", None)
            if crosscheck:
                obj["x_osint_crosscheck_assessment"] = crosscheck.get(
                    "overall_assessment", "unknown"
                )

        if obj.get("type") in {"campaign", "incident", "grouping"} and old_id in activities:
            obj["x_activity_type"] = activities[old_id].get(
                "activity_type", "unknown"
            )

        if "x_confidence" in obj and "confidence" not in obj:
            obj["confidence"] = confidence_score(obj["x_confidence"])

        if obj.get("type") == "indicator":
            observations = obj.pop("x_observations", [])
            source_ids = sorted(
                {
                    item.get("source_id")
                    for item in observations
                    if item.get("source_id")
                }
            )
            obj["x_observation_source_refs"] = source_ids
            obj["external_references"] = merge_external_references(
                obj.get("external_references", []),
                [
                    source_reference(source_id, source_by_id.get(source_id))
                    for source_id in source_ids
                ],
            )
            disposition = obj.get("x_disposition", "unknown")
            obj["confidence"] = {
                "confirmed": 80,
                "candidate": 40,
                "rejected": 0,
            }.get(disposition, 0)

        enhanced_refs: list[dict[str, Any]] = []
        for ref in obj.get("external_references", []):
            source_id = ref.get("external_id")
            if not source_id or source_id not in source_by_id:
                enhanced_refs.append(ref)
                continue
            merged = dict(ref)
            source = source_by_id[source_id]
            path = str(source.get("url") or source.get("path") or "")
            if path.startswith(("https://", "http://")):
                merged["url"] = path
            enhanced_refs.append(merged)
        if enhanced_refs:
            obj["external_references"] = enhanced_refs

        if obj.get("type") not in {"marking-definition"}:
            obj["created_by_ref"] = producer_ref
        prepared.append(obj)

    for obj in prepared:
        for key in REFERENCE_FIELDS:
            if obj.get(key) in id_rewrites:
                obj[key] = id_rewrites[obj[key]]
        for key in REFERENCE_LIST_FIELDS:
            if key in obj:
                obj[key] = [id_rewrites.get(ref, ref) for ref in obj[key]]
        if obj.get("type") == "relationship":
            evidence = target_relationship_evidence.get(
                obj.get("target_ref", "")
            )
            if evidence:
                evidence_description = evidence.get("description", "")
                if evidence_description:
                    existing_description = obj.get("description", "")
                    obj["description"] = (
                        f"{existing_description}\n\nEvidence: "
                        f"{evidence_description}"
                    ).strip()
                obj["external_references"] = merge_external_references(
                    obj.get("external_references", []),
                    evidence.get("external_references", []),
                )

    profile_object_ids = {
        obj.get("x_profile_object_id"): obj["id"]
        for obj in prepared
        if obj.get("x_profile_object_id")
    }
    prepared_by_id = {obj["id"]: obj for obj in prepared}
    observable_by_id: dict[str, dict[str, Any]] = {}
    indicator_relations: dict[str, dict[str, Any]] = {}
    infrastructure_relations: dict[str, dict[str, Any]] = {}
    for indicator in iocs.get("indicators", []):
        if indicator.get("disposition") == "rejected":
            continue
        base_observable = observable_object(indicator, roles=[])
        if not base_observable:
            continue
        observable = observable_object(
            indicator,
            roles=(
                observable_role_index.get(base_observable["id"], [])
                if observable_role_index is not None
                else indicator.get("roles", [])
            ),
        )
        if not observable:
            continue
        indicator_ref = stix_id("indicator", indicator["indicator_id"])
        rendered_indicator = prepared_by_id.get(indicator_ref)
        if (
            not rendered_indicator
            or rendered_indicator.get("type") != "indicator"
        ):
            raise ValueError(
                "canonical IOC has no rendered Indicator: "
                f"{profile['profile_id']}/{indicator['indicator_id']}"
            )
        rendered_indicator["x_opencti_main_observable_type"] = (
            OPENCTI_MAIN_OBSERVABLE_TYPES[observable["type"]]
        )
        local_roles = ioc_role_labels(indicator.get("roles", []))
        if local_roles:
            rendered_indicator["labels"] = sorted(
                set(rendered_indicator.get("labels", [])) | set(local_roles)
            )
        rendered_indicator["modified"] = opencti_modified(profile)
        observable_by_id[observable["id"]] = observable
        observation_source_ids = sorted(
            {
                item.get("source_id")
                for item in indicator.get("observations", [])
                if item.get("source_id")
            }
        )
        indicator_relation = make_relationship(
            key=(
                f"{indicator_ref}:based-on:{observable['id']}:"
                f"{indicator['indicator_id']}"
            ),
            now=opencti_modified(profile),
            producer_ref=producer_ref,
            source_ref=indicator_ref,
            relationship_type="based-on",
            target_ref=observable["id"],
            description=(
                f"{indicator['indicator_id']} directly represents the atomic "
                f"{observable['type']} observable derived from the same "
                "canonical IOC record."
            ),
            confidence=confidence_score(
                "high"
                if indicator.get("disposition") == "confirmed"
                else "low"
            ),
        )
        indicator_relation["external_references"] = [
            source_reference(source_id, source_by_id.get(source_id))
            for source_id in observation_source_ids
        ]
        indicator_relation["x_profile_indicator_id"] = indicator[
            "indicator_id"
        ]
        indicator_relation["x_observation_source_refs"] = (
            observation_source_ids
        )
        if local_roles:
            role_source_ids = sorted(
                {
                    item.get("source_id")
                    for item in indicator.get("observations", [])
                    if ioc_role_labels(item.get("roles", []))
                    and item.get("source_id")
                }
            )
            indicator_relation["x_ioc_roles"] = local_roles
            indicator_relation["x_ioc_role_source_refs"] = role_source_ids
        indicator_relations[indicator_relation["id"]] = indicator_relation
        for infrastructure_ref in indicator.get("infrastructure_refs", []):
            source_ref = profile_object_ids.get(infrastructure_ref)
            if not source_ref:
                continue
            relation = make_relationship(
                key=(
                    f"{source_ref}:consists-of:{observable['id']}:"
                    f"{indicator['indicator_id']}"
                ),
                now=profile["updated_at"],
                producer_ref=producer_ref,
                source_ref=source_ref,
                relationship_type="consists-of",
                target_ref=observable["id"],
                description=(
                    f"{infrastructure_ref} explicitly contains the observable "
                    f"represented by {indicator['indicator_id']}."
                ),
                confidence=confidence_score(
                    "high" if indicator.get("disposition") == "confirmed" else "low"
                ),
            )
            relation.update(indicator_temporal_properties(indicator))
            relation["external_references"] = [
                source_reference(source_id, source_by_id.get(source_id))
                for source_id in observation_source_ids
            ]
            relation["x_profile_indicator_id"] = indicator["indicator_id"]
            relation["x_observation_source_refs"] = observation_source_ids
            infrastructure_relations[relation["id"]] = relation
    for rendered_indicator in prepared:
        if (
            rendered_indicator.get("type") != "indicator"
            or not rendered_indicator.get("x_hunting_pivot")
        ):
            continue
        observables = observable_objects_from_indicator_pattern(
            rendered_indicator, observable_role_index
        )
        if not observables:
            continue
        observable_types = {
            OPENCTI_MAIN_OBSERVABLE_TYPES[item["type"]]
            for item in observables
        }
        if len(observable_types) == 1:
            rendered_indicator["x_opencti_main_observable_type"] = next(
                iter(observable_types)
            )
        rendered_indicator["modified"] = opencti_modified(profile)
        source_ids = sorted(
            {
                item.get("external_id")
                for item in rendered_indicator.get(
                    "external_references", []
                )
                if item.get("external_id")
            }
        )
        for observable in observables:
            observable_by_id[observable["id"]] = observable
            relation = make_relationship(
                key=(
                    f"{rendered_indicator['id']}:based-on:"
                    f"{observable['id']}:hunting-pivot"
                ),
                now=opencti_modified(profile),
                producer_ref=producer_ref,
                source_ref=rendered_indicator["id"],
                relationship_type="based-on",
                target_ref=observable["id"],
                description=(
                    "This reviewed Hunting Pivot Indicator directly represents "
                    "the exact atomic Observable in its STIX pattern."
                ),
                confidence=confidence_score(
                    rendered_indicator.get("x_confidence")
                ),
            )
            relation["external_references"] = copy.deepcopy(
                rendered_indicator.get("external_references", [])
            )
            relation["x_profile_hunting_pivot_id"] = (
                rendered_indicator.get("x_profile_object_id", "")
            )
            relation["x_observation_source_refs"] = source_ids
            indicator_relations[relation["id"]] = relation
    prepared.extend(observable_by_id.values())
    prepared.extend(indicator_relations.values())
    prepared.extend(infrastructure_relations.values())
    scope_profile_owned_objects(profile, prepared)
    return prepared, id_rewrites


def actor_stub(
    profile: dict[str, Any], producer_ref: str
) -> dict[str, Any]:
    actor = profile["actor"]
    source_by_id = {
        item["source_id"]: item for item in profile.get("sources", [])
    }
    evidence_refs = list(
        dict.fromkeys(
            [
                *profile.get("attribution", {}).get("evidence_refs", []),
                *actor_alias_evidence_refs(actor),
            ]
        )
    )
    extra: dict[str, Any] = {
        "name": actor["canonical_name"],
        "aliases": opencti_identity_aliases(actor),
        "description": actor.get("description") or profile["free_text"].get(
            "executive_summary", ""
        ),
        "external_references": external_refs(
            evidence_refs, source_by_id
        ),
        "x_profile_id": profile["profile_id"],
        "x_profile_status": profile["status"],
        "x_alias_assessments": actor.get("aliases", []),
        "created_by_ref": producer_ref,
    }
    for output_key, source_key in (
        ("first_seen", "first_seen"),
        ("last_seen", "last_seen"),
    ):
        value = actor.get(source_key, {}).get("value")
        if value:
            extra[output_key] = value
    if profile["status"] == "deprecated":
        extra["revoked"] = True
    obj = stix_base(
        "intrusion-set", profile["profile_id"], profile["updated_at"], extra
    )
    obj["created"] = profile.get("created_at") or profile["updated_at"]
    return obj


def build_actor_index(
    records: list[dict[str, Any]],
) -> tuple[dict[str, dict[str, Any]], dict[str, list[dict[str, Any]]]]:
    by_profile_id = {item["profile"]["profile_id"]: item for item in records}
    by_name: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        profile = record["profile"]
        actor = profile["actor"]
        by_name[normalized_actor_key(actor["canonical_name"])].append(record)
        for alias in opencti_identity_aliases(actor):
            by_name[normalized_actor_key(alias)].append(record)
    return by_profile_id, by_name


def validate_actor_identity_keys(
    records: list[dict[str, Any]],
) -> list[str]:
    """Reject OpenCTI identity keys shared by multiple active profiles."""

    owners: dict[str, dict[str, set[str]]] = defaultdict(
        lambda: {"profiles": set(), "names": set()}
    )
    for record in records:
        profile = record["profile"]
        if profile.get("status") == "deprecated":
            continue
        actor = profile["actor"]
        for name in [
            actor["canonical_name"],
            *opencti_identity_aliases(actor),
        ]:
            key = normalized_actor_key(name)
            owners[key]["profiles"].add(profile["profile_id"])
            owners[key]["names"].add(name)
    return [
        (
            "OpenCTI actor identity key is shared across profiles: "
            f"{', '.join(sorted(item['names']))} -> "
            f"{', '.join(sorted(item['profiles']))}"
        )
        for item in owners.values()
        if len(item["profiles"]) > 1
    ]


def resolve_actor(
    target: str,
    by_profile_id: dict[str, dict[str, Any]],
    by_name: dict[str, list[dict[str, Any]]],
) -> dict[str, Any] | None:
    if target in by_profile_id:
        return by_profile_id[target]
    candidates = {
        item["profile"]["profile_id"]: item
        for item in by_name.get(normalized_actor_key(target), [])
    }
    if len(candidates) == 1:
        return next(iter(candidates.values()))
    return None


def actor_relationship_objects(
    profile: dict[str, Any],
    producer_ref: str,
    by_profile_id: dict[str, dict[str, Any]],
    by_name: dict[str, list[dict[str, Any]]],
) -> tuple[list[dict[str, Any]], list[str]]:
    source_by_id = {
        item["source_id"]: item for item in profile.get("sources", [])
    }
    source_ref = stix_id("intrusion-set", profile["profile_id"])
    objects: list[dict[str, Any]] = []
    stubs: dict[str, dict[str, Any]] = {}
    unresolved: list[str] = []
    for item in profile.get("relationships", []):
        target_record = resolve_actor(
            item.get("target_actor", ""), by_profile_id, by_name
        )
        if not target_record:
            unresolved.append(item["relationship_id"])
            objects.append(
                stix_base(
                    "note",
                    f"unresolved-actor-relationship:{item['relationship_id']}",
                    profile["updated_at"],
                    {
                        "abstract": (
                            "Unresolved actor relationship: "
                            f"{item.get('target_actor', 'unknown')}"
                        ),
                        "content": item.get("description", ""),
                        "object_refs": [source_ref],
                        "external_references": external_refs(
                            item.get("evidence_refs", []), source_by_id
                        ),
                        "x_profile_relationship_id": item["relationship_id"],
                        "x_profile_relationship_type": item.get(
                            "relationship_type", "related-to"
                        ),
                        "x_unresolved_target_actor": item.get(
                            "target_actor", ""
                        ),
                        "x_confidence": item.get("confidence", "unknown"),
                        "x_analyst_notes": item.get("analyst_notes", ""),
                        "created_by_ref": producer_ref,
                    },
                )
            )
            continue
        target_profile = target_record["profile"]
        target_ref = stix_id("intrusion-set", target_profile["profile_id"])
        if target_ref == source_ref:
            unresolved.append(item["relationship_id"])
            continue
        target_actor = next(
            (
                obj
                for obj in target_record.get("objects", [])
                if obj.get("id") == target_ref
            ),
            None,
        )
        # Reuse the canonical, fully prepared actor object so the same STIX ID
        # has byte-identical content in the target's own Actor/Activity bundles
        # and in bundles that merely need it as a relationship endpoint.
        stubs[target_ref] = copy.deepcopy(
            target_actor or actor_stub(target_profile, producer_ref)
        )
        original_type = item.get("relationship_type") or "related-to"
        relationship_type = (
            original_type
            if original_type in OPENCTI_SAFE_ACTOR_RELATIONSHIPS
            else "related-to"
        )
        extra: dict[str, Any] = {
            "relationship_type": relationship_type,
            "source_ref": source_ref,
            "target_ref": target_ref,
            "description": item.get("description", ""),
            "confidence": confidence_score(item.get("confidence")),
            "external_references": external_refs(
                item.get("evidence_refs", []), source_by_id
            ),
            "x_profile_relationship_id": item["relationship_id"],
            "x_profile_relationship_type": original_type,
            "x_confidence": item.get("confidence", "unknown"),
            "x_analyst_notes": item.get("analyst_notes", ""),
            "created_by_ref": producer_ref,
        }
        extra.update(
            relationship_time_properties(
                item.get("first_observed"), item.get("last_observed")
            )
        )
        relationship = stix_base(
            "relationship",
            item["relationship_id"],
            profile["updated_at"],
            extra,
        )
        relationship["created"] = profile.get("created_at") or profile["updated_at"]
        objects.append(relationship)
    return [*stubs.values(), *objects], unresolved


def profile_object_index(
    profile: dict[str, Any], objects: list[dict[str, Any]]
) -> dict[str, str]:
    result = {
        profile["profile_id"]: stix_id("intrusion-set", profile["profile_id"])
    }
    for obj in objects:
        profile_object_id = obj.get("x_profile_object_id")
        if profile_object_id:
            result[profile_object_id] = obj["id"]
    return result


def make_relationship(
    key: str,
    now: str,
    producer_ref: str,
    source_ref: str,
    relationship_type: str,
    target_ref: str,
    description: str,
    confidence: int,
) -> dict[str, Any]:
    return stix_base(
        "relationship",
        key,
        now,
        {
            "relationship_type": relationship_type,
            "source_ref": source_ref,
            "target_ref": target_ref,
            "description": description,
            "confidence": confidence,
            "created_by_ref": producer_ref,
        },
    )


def make_report(
    *,
    key: str,
    now: str,
    producer_ref: str,
    name: str,
    description: str,
    report_type: str,
    object_refs: list[str],
    scope: str,
    profile_id: str,
    activity_id: str | None = None,
    modified: str | None = None,
) -> dict[str, Any]:
    extra: dict[str, Any] = {
        "name": name,
        "description": description,
        "report_types": [report_type],
        "published": now,
        "object_refs": sorted(set(object_refs)),
        "created_by_ref": producer_ref,
        "x_opencti_bundle_scope": scope,
        "x_profile_id": profile_id,
    }
    if activity_id:
        extra["x_activity_id"] = activity_id
    report = stix_base("report", key, now, extra)
    if modified:
        report["modified"] = modified
    return report


def source_report_objects(
    *,
    profile: dict[str, Any],
    iocs: dict[str, Any],
    objects: list[dict[str, Any]],
    producer_ref: str,
    scope_key: str,
) -> list[dict[str, Any]]:
    """Materialize dated source Reports around only the objects they support."""

    source_by_id = {
        item["source_id"]: item
        for item in [*profile.get("sources", []), *iocs.get("sources", [])]
        if item.get("source_id")
    }
    object_refs_by_source: dict[str, set[str]] = defaultdict(set)
    for obj in objects:
        source_ids = {
            ref.get("external_id")
            for ref in obj.get("external_references", [])
            if ref.get("external_id") in source_by_id
        }
        source_ids.update(
            source_id
            for source_id in obj.get("x_observation_source_refs", [])
            if source_id in source_by_id
        )
        for source_id in source_ids:
            object_refs_by_source[source_id].add(obj["id"])

    result: list[dict[str, Any]] = []
    for source_id, object_refs in sorted(object_refs_by_source.items()):
        source = source_by_id[source_id]
        published = source.get("published_at", {})
        if not published.get("value"):
            # STIX Report requires ``published``. Unknown publication remains
            # an External Reference and must never be fabricated from access,
            # repository, or profile modification time.
            continue
        report = stix_base(
            "report",
            f"source-report:{scope_key}:{source_id}",
            opencti_modified(profile),
            {
                "name": source.get("title") or source.get("path") or source_id,
                "description": (
                    "Source report represented from canonical provenance. Its "
                    "publication time is not an observation or relationship time."
                ),
                "report_types": ["threat-report"],
                "published": published["value"],
                "object_refs": sorted(object_refs),
                "created_by_ref": producer_ref,
                "external_references": [source_reference(source_id, source)],
                "x_opencti_source_report": True,
                "x_source_id": source_id,
                "x_evidence_slice_scope": scope_key,
                "x_source_publisher": source.get("publisher", ""),
                "x_source_type": source.get("source_type", "unknown"),
                "x_published_precision": published.get("precision", "unknown"),
                "x_published_status": published.get("status", "unknown"),
                "x_published_basis": published.get("basis", "not-stated"),
                "x_temporal_role": "publication-only",
            },
        )
        result.append(report)
    return result


def finalize_bundle(
    key: str,
    producer: dict[str, Any],
    objects: list[dict[str, Any]],
    report: dict[str, Any],
) -> dict[str, Any]:
    unique: dict[str, dict[str, Any]] = {producer["id"]: producer}
    for obj in objects:
        complete_opencti_relationship_time_range(obj)
        unique[obj["id"]] = obj
    unique[report["id"]] = report
    ordered = [unique[producer["id"]]]
    ordered.extend(
        unique[obj_id]
        for obj_id in sorted(unique)
        if obj_id not in {producer["id"], report["id"]}
    )
    ordered.append(unique[report["id"]])
    return {
        "type": "bundle",
        "id": stix_id("bundle", key),
        "objects": ordered,
    }


def complete_opencti_relationship_time_range(obj: dict[str, Any]) -> bool:
    """Complete a Relationship time pair required by OpenCTI imports.

    Canonical temporal provenance remains in ``x_first_observed`` and
    ``x_last_observed``.  When an actual last observation is unavailable, the
    duplicated stop time is explicitly marked as an OpenCTI compatibility
    fallback and must not be interpreted as an observed relationship end.
    """

    if obj.get("type") != "relationship":
        return False
    start_time = obj.get("start_time")
    if not start_time or obj.get("stop_time"):
        return False

    last_observed = obj.get("x_last_observed")
    last_value = (
        last_observed.get("value")
        if isinstance(last_observed, dict)
        else None
    )
    if last_value and last_value < start_time:
        raise ValueError(
            f"{obj.get('id', 'relationship')} has last_observed before "
            "start_time"
        )
    if last_value:
        obj["stop_time"] = last_value
    else:
        obj["stop_time"] = start_time
        obj["x_stop_time_is_fallback"] = True
        obj["x_stop_time_basis"] = "opencti-required-start-time-fallback"

    obj["modified"] = max(
        str(obj.get("modified", "")), OPENCTI_MODEL_MODIFIED
    )
    return True


def preserve_object_versions(
    bundle: dict[str, Any],
    previous_bundle: dict[str, Any] | None,
) -> None:
    """Preserve STIX creation metadata and reject invalid version updates.

    OpenCTI bundles are tracked release artifacts and therefore also serve as
    the version baseline for stable object IDs. Rebuilding a bundle must not
    rewrite ``created`` merely because the owning profile was updated. When
    the semantic content is unchanged, ``modified`` is retained as well. A
    semantic change with a non-increasing ``modified`` value is rejected so a
    generator-policy change cannot silently produce two definitions for the
    same STIX version.
    """

    if not previous_bundle:
        return
    previous_by_id = {
        item["id"]: item
        for item in previous_bundle.get("objects", [])
        if isinstance(item, dict) and item.get("id")
    }
    for item in bundle.get("objects", []):
        previous = previous_by_id.get(item.get("id"))
        if not previous:
            continue
        if previous.get("created"):
            item["created"] = previous["created"]
        current_semantic = {
            key: value
            for key, value in item.items()
            if key not in {"created", "modified"}
        }
        previous_semantic = {
            key: value
            for key, value in previous.items()
            if key not in {"created", "modified"}
        }
        if current_semantic == previous_semantic:
            if previous.get("modified"):
                item["modified"] = previous["modified"]
            continue
        previous_modified = previous.get("modified")
        current_modified = item.get("modified")
        if not previous_modified or not current_modified:
            current_without_roles = {
                key: value
                for key, value in current_semantic.items()
                if key not in UNVERSIONED_OBSERVABLE_ROLE_FIELDS
            }
            previous_without_roles = {
                key: value
                for key, value in previous_semantic.items()
                if key not in UNVERSIONED_OBSERVABLE_ROLE_FIELDS
            }
            if (
                item.get("type") in ATOMIC_OBSERVABLE_TYPES
                and previous.get("type") == item.get("type")
                and current_without_roles == previous_without_roles
            ):
                # SCOs have no created/modified version properties. A controlled
                # OpenCTI representation migration may add or update only the
                # non-contributing role-label metadata while preserving the
                # observable value/hash and deterministic ID. Any other
                # unversioned semantic change still fails closed below.
                continue
            raise ValueError(
                "stable unversioned STIX object changed semantic content: "
                f"{item.get('id', 'unknown')}"
            )
        previous_time = datetime.fromisoformat(
            previous_modified.replace("Z", "+00:00")
        )
        current_time = datetime.fromisoformat(
            current_modified.replace("Z", "+00:00")
        )
        if current_time <= previous_time:
            raise ValueError(
                "STIX object semantic content changed without a newer "
                f"modified value: {item.get('id', 'unknown')} "
                f"({previous_modified} -> {current_modified})"
            )


def load_previous_opencti_objects(
    output_root: Path,
) -> dict[str, dict[str, Any]]:
    """Load one byte-identical prior definition for every exported object."""

    previous_by_id: dict[str, dict[str, Any]] = {}
    serialized_by_id: dict[str, str] = {}
    for section in ("actors", "campaigns", "activities"):
        directory = output_root / section
        if not directory.exists():
            continue
        for path in sorted(directory.rglob("*.stix2.json")):
            for obj in load_json(path).get("objects", []):
                serialized = json.dumps(
                    obj,
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                )
                previous = serialized_by_id.setdefault(obj["id"], serialized)
                if previous != serialized:
                    raise ValueError(
                        "previous OpenCTI corpus has conflicting definitions "
                        f"for shared STIX ID: {obj['id']}"
                    )
                previous_by_id.setdefault(obj["id"], obj)
    return previous_by_id


def preserve_prepared_object_versions(
    records: list[dict[str, Any]],
    previous_by_id: dict[str, dict[str, Any]],
) -> None:
    """Apply prior shared-object versions before any bundle is sliced.

    An object newly added to an earlier Activity slice may already exist in a
    later slice. Restoring its corpus-wide version here prevents traversal
    order from making the two bundles disagree on ``created`` or ``modified``.
    """

    for record in records:
        for obj in record["objects"]:
            previous = previous_by_id.get(obj["id"])
            if not previous:
                continue
            if previous.get("created"):
                obj["created"] = previous["created"]
            current_semantic = {
                key: value
                for key, value in obj.items()
                if key not in {"created", "modified"}
            }
            previous_semantic = {
                key: value
                for key, value in previous.items()
                if key not in {"created", "modified"}
            }
            if current_semantic == previous_semantic and previous.get(
                "modified"
            ):
                obj["modified"] = previous["modified"]


def build_actor_bundle(
    record: dict[str, Any],
    producer: dict[str, Any],
    by_profile_id: dict[str, dict[str, Any]],
    by_name: dict[str, list[dict[str, Any]]],
) -> tuple[dict[str, Any], list[str]]:
    profile = record["profile"]
    objects = record["objects"]
    profile_ids = profile_object_index(profile, objects)
    activity_ids = {
        profile_ids[item["activity_id"]]
        for item in profile.get("activities", [])
        if item["activity_id"] in profile_ids
    }
    victim_ids = {
        profile_ids[item["victim_case_id"]]
        for item in profile.get("victim_cases", [])
        if item["victim_case_id"] in profile_ids
    }
    actor_observable_ids = {
        observable["id"]
        for indicator in record.get("iocs", {}).get("indicators", [])
        if indicator.get("disposition") != "rejected"
        and not indicator.get("campaign_refs")
        and (observable := observable_object(indicator)) is not None
    }
    actor_hunting_indicator_ids = {
        obj["id"]
        for obj in objects
        if obj.get("type") == "indicator" and obj.get("x_hunting_pivot")
    }
    actor_observable_ids.update(
        obj["target_ref"]
        for obj in objects
        if obj.get("type") == "relationship"
        and obj.get("relationship_type") == "based-on"
        and obj.get("source_ref") in actor_hunting_indicator_ids
    )
    selected: list[dict[str, Any]] = []
    selected_ids: set[str] = set()
    relationships: list[dict[str, Any]] = []
    for obj in objects:
        obj_type = obj.get("type")
        if obj_type == "relationship":
            relationships.append(obj)
            continue
        if obj["id"] in activity_ids or obj["id"] in victim_ids:
            continue
        if obj_type == "indicator" and obj.get("x_campaign_refs"):
            continue
        if (
            obj_type in ATOMIC_OBSERVABLE_TYPES
            and obj["id"] not in actor_observable_ids
        ):
            continue
        selected.append(obj)
        selected_ids.add(obj["id"])

    # Notes can legitimately connect an actor-wide hunting pivot to a modeled
    # activity.  Activities are exported in their own bundles, however, so an
    # actor bundle must retain only the Note references that are present in
    # that actor bundle.  Work on copies because the same prepared objects are
    # reused when the per-activity bundles are built later.
    scoped_selected: list[dict[str, Any]] = []
    for obj in selected:
        scoped = copy.deepcopy(obj)
        if "object_refs" in scoped:
            original_refs = scoped["object_refs"]
            scoped["object_refs"] = [
                ref for ref in scoped["object_refs"] if ref in selected_ids
            ]
            if (
                scoped.get("type") == "note"
                and scoped["object_refs"] != original_refs
            ):
                scoped["id"] = stix_id(
                    scoped["type"], f"{obj['id']}:slice:actor"
                )
        scoped_selected.append(scoped)
    selected = scoped_selected
    selected.extend(
        obj
        for obj in relationships
        if obj.get("source_ref") in selected_ids
        and obj.get("target_ref") in selected_ids
        and obj.get("source_ref") not in activity_ids
        and obj.get("target_ref") not in activity_ids
    )
    actor_links, unresolved = actor_relationship_objects(
        profile, producer["id"], by_profile_id, by_name
    )
    selected.extend(actor_links)
    selected.extend(
        source_report_objects(
            profile=profile,
            iocs=record["iocs"],
            objects=selected,
            producer_ref=producer["id"],
            scope_key=f"actor:{profile['profile_id']}",
        )
    )
    report = make_report(
        key=f"opencti-actor-report:{profile['profile_id']}",
        now=profile["updated_at"],
        producer_ref=producer["id"],
        name=f"{profile['name']} OpenCTI Actor Profile",
        description=profile["free_text"].get("executive_summary", ""),
        report_type="threat-actor",
        object_refs=[obj["id"] for obj in selected],
        scope="actor",
        profile_id=profile["profile_id"],
        modified=opencti_modified(profile),
    )
    return (
        finalize_bundle(
            f"opencti-actor:{profile['profile_id']}", producer, selected, report
        ),
        unresolved,
    )


def campaign_dependency_profile_ids(
    profile: dict[str, Any], activity: dict[str, Any]
) -> set[str]:
    """Return the cycle-safe transitive dependency closure for an Activity.

    Parent Campaigns may explicitly contain child Incident/Grouping records.
    The child Activity and all objects that the child explicitly references
    must travel together; otherwise object_refs on the child would be sliced
    differently between its own bundle and the parent bundle.
    """

    activities = {
        item["activity_id"]: item for item in profile.get("activities", [])
    }
    result: set[str] = set()
    pending = [activity]
    visited_activities: set[str] = set()
    dependency_fields = (
        "activity_refs",
        "malware_refs",
        "tool_refs",
        "infrastructure_refs",
        "target_refs",
        "ttp_refs",
        "victim_refs",
    )
    while pending:
        current = pending.pop()
        current_id = current.get("activity_id")
        if current_id in visited_activities:
            continue
        if current_id:
            visited_activities.add(current_id)
        for field in dependency_fields:
            refs = current.get(field, [])
            result.update(refs)
            if field == "activity_refs":
                pending.extend(
                    activities[ref]
                    for ref in refs
                    if ref in activities and ref not in visited_activities
                )

    victims = {
        item["victim_case_id"]: item for item in profile.get("victim_cases", [])
    }
    ttps = {item["ttp_id"]: item for item in profile.get("ttps", [])}
    expanded: set[str] = set()
    while True:
        pending_refs = result - expanded
        if not pending_refs:
            break
        expanded.update(pending_refs)
        for ref in pending_refs:
            victim = victims.get(ref, {})
            result.update(victim.get("target_refs", []))
            result.update(victim.get("malware_refs", []))
            result.update(victim.get("ttp_refs", []))
            ttp = ttps.get(ref, {})
            result.update(ttp.get("malware_refs", []))
            result.update(ttp.get("infrastructure_refs", []))
    return result


def build_activity_bundle(
    record: dict[str, Any],
    activity: dict[str, Any],
    producer: dict[str, Any],
) -> dict[str, Any]:
    profile = record["profile"]
    objects = record["objects"]
    primary_type = activity_stix_object_type(activity)
    profile_ids = profile_object_index(profile, objects)
    dependency_ids = campaign_dependency_profile_ids(profile, activity)
    activity_ref = profile_ids[activity["activity_id"]]
    all_activity_ids = {
        profile_ids[item["activity_id"]]
        for item in profile.get("activities", [])
        if item["activity_id"] in profile_ids
    }
    activity_profile_ids = {
        item["activity_id"]
        for item in profile.get("activities", [])
    }
    slice_activity_profile_ids = {
        activity["activity_id"],
        *(dependency_ids & activity_profile_ids),
    }
    slice_activity_refs = {
        profile_ids[item]
        for item in slice_activity_profile_ids
        if item in profile_ids
    }
    wanted_ids = {
        stix_id("intrusion-set", profile["profile_id"]),
        activity_ref,
        *(
            profile_ids[item]
            for item in dependency_ids
            if item in profile_ids
        ),
    }
    # Hunting Notes are shared evidence containers. Include a Note and its
    # Indicator/dependency references in the activity slice when the Note
    # explicitly names this activity, while excluding references to any other
    # activity that the same cross-campaign pivot may also cover.
    activity_hunting_notes = [
        obj
        for obj in objects
        if obj.get("type") == "note"
        and obj.get("x_profile_hunting_pivot_id")
        and slice_activity_refs.intersection(obj.get("object_refs", []))
    ]
    for note in activity_hunting_notes:
        wanted_ids.add(note["id"])
        wanted_ids.update(
            ref
            for ref in note.get("object_refs", [])
            if ref == activity_ref or ref not in all_activity_ids
        )
    campaign_indicators = [
        obj
        for obj in objects
        if obj.get("type") == "indicator"
        and slice_activity_profile_ids.intersection(
            obj.get("x_campaign_refs", [])
        )
    ]
    for indicator in campaign_indicators:
        wanted_ids.add(indicator["id"])
        for profile_ref in (
            indicator.get("x_malware_refs", [])
            + indicator.get("x_infrastructure_refs", [])
        ):
            if profile_ref in profile_ids:
                wanted_ids.add(profile_ids[profile_ref])

    # Atomic SCOs are deliberately profile-neutral. Reconstruct their stable
    # IDs from the selected canonical IOC records rather than storing actor or
    # campaign metadata on the shared SCO itself.
    for indicator in record.get("iocs", {}).get("indicators", []):
        if indicator.get("disposition") == "rejected":
            continue
        if not slice_activity_profile_ids.intersection(
            indicator.get("campaign_refs", [])
        ):
            continue
        observable = observable_object(indicator)
        if observable:
            wanted_ids.add(observable["id"])
    wanted_ids.update(
        obj["target_ref"]
        for obj in objects
        if obj.get("type") == "relationship"
        and obj.get("relationship_type") == "based-on"
        and obj.get("source_ref") in wanted_ids
    )

    selected = [
        obj
        for obj in objects
        if obj.get("type") != "relationship" and obj.get("id") in wanted_ids
    ]
    selected_ids = {obj["id"] for obj in selected}
    selected = [
        {
            **copy.deepcopy(obj),
            **(
                {
                    "object_refs": [
                        ref
                        for ref in obj.get("object_refs", [])
                        if ref in selected_ids
                    ]
                }
                if "object_refs" in obj
                else {}
            ),
        }
        for obj in selected
    ]
    original_by_id = {obj["id"]: obj for obj in objects}
    for obj in selected:
        original = original_by_id[obj["id"]]
        if (
            obj.get("type") == "note"
            and obj.get("object_refs") != original.get("object_refs")
        ):
            obj["id"] = stix_id(
                obj["type"],
                f"{original['id']}:slice:{primary_type}:{activity['activity_id']}",
            )
    # A Grouping is an evidence container, not a claim that every co-contained
    # object is directly related.  The only SROs retained for a Grouping are
    # explicit Indicator ``based-on`` Observable and Infrastructure
    # ``consists-of`` Observable bindings generated from the same canonical
    # IOC record; no relation is inferred from co-containment.
    selected.extend(
        obj
        for obj in objects
        if obj.get("type") == "relationship"
        and obj.get("source_ref") in wanted_ids
        and obj.get("target_ref") in wanted_ids
        and (
            primary_type != "grouping"
            or obj.get("relationship_type") in {"based-on", "consists-of"}
        )
    )

    existing_relationship_ids = {obj["id"] for obj in selected}
    for indicator in campaign_indicators:
        if primary_type == "grouping":
            continue
        if activity["activity_id"] not in indicator.get("x_campaign_refs", []):
            # The Indicator belongs to an explicitly contained child Activity,
            # not automatically to the parent Campaign.
            continue
        relation = make_relationship(
            key=f"{indicator['id']}:indicates:{activity_ref}",
            now=profile["updated_at"],
            producer_ref=producer["id"],
            source_ref=indicator["id"],
            relationship_type="indicates",
            target_ref=activity_ref,
            description=(
                f"{indicator.get('name', indicator['id'])} is explicitly "
                f"scoped to {primary_type} {activity['name']} in the "
                "repository dataset."
            ),
            confidence=indicator.get("confidence", 0),
        )
        if relation["id"] not in existing_relationship_ids:
            selected.append(relation)
            existing_relationship_ids.add(relation["id"])
        for key in ("x_malware_refs", "x_infrastructure_refs"):
            for profile_ref in indicator.get(key, []):
                target_ref = profile_ids.get(profile_ref)
                if not target_ref or target_ref not in wanted_ids:
                    continue
                relation = make_relationship(
                    key=f"{indicator['id']}:indicates:{target_ref}",
                    now=profile["updated_at"],
                    producer_ref=producer["id"],
                    source_ref=indicator["id"],
                    relationship_type="indicates",
                    target_ref=target_ref,
                    description=(
                        f"{indicator.get('name', indicator['id'])} is explicitly "
                        f"linked to {profile_ref} in the repository dataset."
                    ),
                    confidence=indicator.get("confidence", 0),
                )
                if relation["id"] not in existing_relationship_ids:
                    selected.append(relation)
                    existing_relationship_ids.add(relation["id"])

    # A child Grouping embedded in a parent Campaign must remain byte-identical
    # to that Grouping in its own bundle. Build containment from the child's
    # transitive dependency closure, never from every object in the parent
    # slice. Cross-activity hunting Notes are excluded from Grouping containment
    # because their bundle-specific sliced IDs are intentionally different.
    selected_ids = {obj["id"] for obj in selected}
    activities_by_id = {
        item["activity_id"]: item for item in profile.get("activities", [])
    }
    for index, obj in enumerate(selected):
        if obj.get("type") != "grouping":
            continue
        grouping_activity_id = obj.get("x_profile_object_id")
        grouping_activity = activities_by_id.get(grouping_activity_id)
        if not grouping_activity:
            continue
        grouping_activity_ref = profile_ids.get(grouping_activity_id)
        grouping_dependencies = campaign_dependency_profile_ids(
            profile, grouping_activity
        )
        grouping_refs = {
            stix_id("intrusion-set", profile["profile_id"]),
            *(
                profile_ids[item]
                for item in grouping_dependencies
                if item in profile_ids
            ),
        }
        for contained in selected:
            if contained.get("type") == "indicator" and grouping_activity_id in contained.get(
                "x_campaign_refs", []
            ):
                grouping_refs.add(contained["id"])
            if contained.get("type") == "note" and grouping_activity_ref in contained.get(
                "object_refs", []
            ):
                original = original_by_id.get(contained.get("id"))
                if original is None:
                    # This is a bundle-specific sliced Note ID. A Note that was
                    # cross-activity in the canonical object must not become a
                    # child-Grouping member only because another activity ref
                    # was removed for this slice.
                    continue
                original_activity_refs = set(original.get("object_refs", [])) & all_activity_ids
                if original_activity_refs <= {grouping_activity_ref}:
                    grouping_refs.add(contained["id"])
        for indicator in record.get("iocs", {}).get("indicators", []):
            if grouping_activity_id not in indicator.get("campaign_refs", []):
                continue
            observable = observable_object(indicator)
            if observable and observable["id"] in selected_ids:
                grouping_refs.add(observable["id"])
        grouping = copy.deepcopy(obj)
        grouping["object_refs"] = sorted(
            ref
            for ref in grouping_refs
            if ref in selected_ids and ref != grouping_activity_ref
        )
        grouping["modified"] = opencti_modified(profile)
        selected[index] = grouping

    selected.extend(
        source_report_objects(
            profile=profile,
            iocs=record["iocs"],
            objects=selected,
            producer_ref=producer["id"],
            scope_key=(
                f"{primary_type}:{profile['profile_id']}:"
                f"{activity['activity_id']}"
            ),
        )
    )
    report = make_report(
        key=(
            f"opencti-campaign-report:{profile['profile_id']}:"
            f"{activity['activity_id']}"
        ),
        now=profile["updated_at"],
        producer_ref=producer["id"],
        name=f"{profile['name']} / {activity['name']}",
        description=activity.get("description", ""),
        report_type="campaign" if primary_type == "campaign" else "threat-report",
        object_refs=[obj["id"] for obj in selected],
        scope=primary_type,
        profile_id=profile["profile_id"],
        activity_id=activity["activity_id"],
        modified=opencti_modified(profile),
    )
    return finalize_bundle(
        f"opencti-{primary_type}:{profile['profile_id']}:{activity['activity_id']}",
        producer,
        selected,
        report,
    )


def build_campaign_bundle(
    record: dict[str, Any],
    activity: dict[str, Any],
    producer: dict[str, Any],
) -> dict[str, Any]:
    """Backward-compatible wrapper for callers with an explicit Campaign."""

    return build_activity_bundle(record, activity, producer)


def validate_bundle(
    bundle: dict[str, Any],
    *,
    expected_scope: str | None = None,
) -> list[str]:
    errors: list[str] = []
    if bundle.get("type") != "bundle":
        errors.append("top-level type is not bundle")
    if not str(bundle.get("id", "")).startswith("bundle--"):
        errors.append("bundle id is missing or invalid")
    objects = bundle.get("objects")
    if not isinstance(objects, list) or not objects:
        return [*errors, "bundle objects must be a non-empty list"]
    ids: set[str] = set()
    objects_by_id: dict[str, dict[str, Any]] = {}
    reports: list[dict[str, Any]] = []
    activity_counts = {"campaign": 0, "incident": 0, "grouping": 0}
    for index, obj in enumerate(objects):
        obj_id = obj.get("id")
        if not isinstance(obj_id, str) or not obj_id.startswith(
            f"{obj.get('type')}--"
        ):
            errors.append(f"objects[{index}] has an invalid type/id pair")
            continue
        if obj_id in ids:
            errors.append(f"duplicate object id: {obj_id}")
        ids.add(obj_id)
        objects_by_id[obj_id] = obj
        if obj.get("type") != "marking-definition" and obj.get(
            "spec_version"
        ) != "2.1":
            errors.append(f"{obj_id} does not declare STIX 2.1")
        if obj.get("type") == "report":
            reports.append(obj)
        if obj.get("type") == "relationship":
            start_time = obj.get("start_time")
            stop_time = obj.get("stop_time")
            if start_time and not stop_time:
                errors.append(
                    f"{obj_id} has start_time without required stop_time"
                )
            if obj.get("x_stop_time_is_fallback") is True:
                if not start_time or stop_time != start_time:
                    errors.append(
                        f"{obj_id} fallback stop_time must equal start_time"
                    )
                if obj.get("x_stop_time_basis") != (
                    "opencti-required-start-time-fallback"
                ):
                    errors.append(
                        f"{obj_id} has an invalid stop_time fallback basis"
                    )
                last_observed = obj.get("x_last_observed")
                if (
                    isinstance(last_observed, dict)
                    and last_observed.get("value")
                ):
                    errors.append(
                        f"{obj_id} marks stop_time as fallback despite a "
                        "known last observation"
                    )
        if (
            obj.get("type") == "intrusion-set"
            and "x_alias_assessments" in obj
        ):
            expected_aliases = opencti_identity_aliases(
                {"aliases": obj.get("x_alias_assessments", [])}
            )
            if obj.get("aliases", []) != expected_aliases:
                errors.append(
                    f"{obj_id}.aliases contains a non-identity alias or "
                    "omits an exact/high alias"
                )
        if obj.get("type") in activity_counts and obj.get("x_profile_object_id"):
            activity_counts[obj["type"]] += 1
    external_ids = {TLP_CLEAR}
    for obj in objects:
        for key in REFERENCE_FIELDS:
            ref = obj.get(key)
            if ref and ref not in ids and ref not in external_ids:
                errors.append(f"{obj['id']}.{key} is dangling: {ref}")
        for key in REFERENCE_LIST_FIELDS:
            for ref in obj.get(key, []):
                if ref not in ids and ref not in external_ids:
                    errors.append(f"{obj['id']}.{key} is dangling: {ref}")
    generated_based_on_by_indicator: dict[str, list[dict[str, Any]]] = (
        defaultdict(list)
    )
    for obj in objects:
        if (
            obj.get("type") != "relationship"
            or obj.get("relationship_type") != "based-on"
            or not (
                obj.get("x_profile_indicator_id")
                or obj.get("x_profile_hunting_pivot_id")
                or obj.get("x_standalone_indicator_id")
            )
        ):
            continue
        source = objects_by_id.get(obj.get("source_ref"))
        target = objects_by_id.get(obj.get("target_ref"))
        if not source or source.get("type") != "indicator":
            errors.append(
                f"{obj['id']} generated based-on source is not an Indicator"
            )
            continue
        if not target or target.get("type") not in ATOMIC_OBSERVABLE_TYPES:
            errors.append(
                f"{obj['id']} generated based-on target is not a supported "
                "atomic Observable"
            )
            continue
        target_roles = ioc_role_labels(target.get("x_ioc_roles", []))
        if target.get("x_opencti_labels", []) != target_roles:
            errors.append(
                f"{target['id']} OpenCTI labels do not match its IOC roles"
            )
        if target_roles and target.get("x_ioc_role_scope") != (
            "corpus-observed-uses"
        ):
            errors.append(
                f"{target['id']} has IOC roles without corpus role scope"
            )
        source_roles = ioc_role_labels(
            source.get("x_ioc_roles", source.get("x_roles", []))
        )
        if source_roles:
            if not set(source_roles).issubset(set(source.get("labels", []))):
                errors.append(
                    f"{source['id']} labels omit structured IOC roles"
                )
            if obj.get("x_ioc_roles") != source_roles:
                errors.append(
                    f"{obj['id']} does not preserve Indicator IOC roles"
                )
            if not obj.get("x_ioc_role_source_refs"):
                errors.append(
                    f"{obj['id']} has IOC roles without role evidence refs"
                )
            if not set(source_roles).issubset(set(target_roles)):
                errors.append(
                    f"{target['id']} labels omit a directly asserted IOC role"
                )
        generated_based_on_by_indicator[source["id"]].append(obj)
    for obj in objects:
        declared_type = obj.get("x_opencti_main_observable_type")
        if obj.get("type") != "indicator" or not declared_type:
            continue
        relations = generated_based_on_by_indicator.get(obj["id"], [])
        expected_minimum = 1
        expected_maximum = None if obj.get("x_hunting_pivot") else 1
        if len(relations) < expected_minimum or (
            expected_maximum is not None
            and len(relations) > expected_maximum
        ):
            expected_count = (
                "at least one"
                if expected_maximum is None
                else "exactly one"
            )
            errors.append(
                f"{obj['id']} must have {expected_count} generated based-on "
                f"Observable relationship; found {len(relations)}"
            )
            continue
        expected_types = {
            OPENCTI_MAIN_OBSERVABLE_TYPES[
                objects_by_id[relation["target_ref"]]["type"]
            ]
            for relation in relations
        }
        if expected_types != {declared_type}:
            errors.append(
                f"{obj['id']}.x_opencti_main_observable_type is "
                f"{declared_type}, expected one of "
                f"{', '.join(sorted(expected_types))}"
            )
    container_reports = [
        item for item in reports if item.get("x_opencti_bundle_scope")
    ]
    if len(container_reports) != 1:
        errors.append(
            "expected exactly one generated container report, found "
            f"{len(container_reports)}"
        )
    else:
        report = container_reports[0]
        if report.get("x_opencti_bundle_scope") != expected_scope:
            errors.append("report scope does not match bundle scope")
        expected_report_refs = ids - {
            report["id"],
            report.get("created_by_ref", ""),
        }
        missing_report_refs = expected_report_refs - set(
            report.get("object_refs", [])
        )
        if missing_report_refs:
            errors.append(
                "report does not contain every knowledge object: "
                + ", ".join(sorted(missing_report_refs)[:5])
            )
    for report in reports:
        if report.get("x_opencti_source_report") and not report.get("published"):
            errors.append(f"source report has no published time: {report['id']}")
    total_activities = sum(activity_counts.values())
    if expected_scope == "actor" and total_activities:
        errors.append(
            f"actor bundle contains {total_activities} activity objects"
        )
    if expected_scope in activity_counts:
        primary_activity_id = (
            container_reports[0].get("x_activity_id")
            if len(container_reports) == 1
            else None
        )
        primary_matches = [
            obj
            for obj in objects
            if obj.get("type") == expected_scope
            and obj.get("x_profile_object_id") == primary_activity_id
        ]
        if len(primary_matches) != 1:
            errors.append(
                f"{expected_scope} bundle must contain its one declared primary "
                f"activity; found {len(primary_matches)}"
            )
    return errors


def validate_shared_object_definitions(
    bundle: dict[str, Any], definitions: dict[str, str]
) -> list[str]:
    """Reject two different definitions of one STIX ID across bundles."""

    errors: list[str] = []
    for obj in bundle.get("objects", []):
        serialized = json.dumps(
            obj,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        previous = definitions.setdefault(obj["id"], serialized)
        if previous != serialized:
            errors.append(
                f"shared STIX ID has conflicting bundle definitions: {obj['id']}"
            )
    return errors


def safe_activity_filename(activity_id: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9._-]+", "-", activity_id).strip("-.")
    return f"{value or 'activity'}.stix2.json"


def load_records(
    catalog_path: Path,
    profiles_root: Path,
    wanted: set[str],
) -> list[dict[str, Any]]:
    catalog = load_json(catalog_path)
    records: list[dict[str, Any]] = []
    for actor in catalog["actors"]:
        slug = actor["slug"]
        if wanted and slug not in wanted:
            continue
        actor_dir = profiles_root / slug
        profile_path = actor_dir / "actor-profile.json"
        bundle_path = actor_dir / "generated" / "profile.stix2.json"
        iocs_path = actor_dir / "iocs.json"
        if not profile_path.exists() or not bundle_path.exists():
            raise FileNotFoundError(
                f"missing canonical profile or rendered STIX for {slug}"
            )
        records.append(
            {
                "slug": slug,
                "profile": load_json(profile_path),
                "full_bundle": load_json(bundle_path),
                "iocs": load_json(iocs_path) if iocs_path.exists() else {},
            }
        )
    return records


def prune_stale(output_root: Path, expected: set[Path]) -> int:
    removed = 0
    for directory in (
        output_root / "actors",
        output_root / "campaigns",
        output_root / "activities",
    ):
        if not directory.exists():
            continue
        for path in directory.rglob("*.stix2.json"):
            if path.resolve() in expected:
                continue
            path.unlink()
            removed += 1
    return removed


def load_standalone_records(
    curation_path: Path, ledger_path: Path
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Load the explicit standalone allowlist; never export the ledger wholesale."""

    curation = load_json(curation_path)
    ledger = load_json(ledger_path)
    return curation, validate_standalone_curation(curation, ledger)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--catalog",
        type=Path,
        default=Path("actor_profile/corpus-catalog.json"),
    )
    parser.add_argument("--profiles-root", type=Path, default=Path("profiles"))
    parser.add_argument("--output-root", type=Path, default=Path("opencti"))
    parser.add_argument(
        "--opencti-country-index",
        type=Path,
        default=DEFAULT_OPENCTI_COUNTRY_INDEX,
        help="pinned OpenCTI Country metadata used for entity deduplication",
    )
    parser.add_argument(
        "--standalone-activity-curation",
        type=Path,
        default=DEFAULT_STANDALONE_CURATION,
        help="explicit allowlist for actor-free Campaign/Incident/Grouping bundles",
    )
    parser.add_argument(
        "--unknown-cluster-ledger",
        type=Path,
        default=DEFAULT_UNKNOWN_CLUSTER_LEDGER,
        help="reviewed ledger referenced by the standalone allowlist",
    )
    parser.add_argument("--actor", action="append", help="only export this slug")
    parser.add_argument(
        "--prune",
        action="store_true",
        help="remove stale generated .stix2.json files below the output root",
    )
    parser.add_argument(
        "--max-bundle-bytes",
        type=int,
        default=45 * 1024 * 1024,
        help="fail when a bundle exceeds this size (default: 45 MiB)",
    )
    args = parser.parse_args()

    repository_root = Path.cwd().resolve()
    catalog_path = (repository_root / args.catalog).resolve()
    profiles_root = (repository_root / args.profiles_root).resolve()
    output_root = (repository_root / args.output_root).resolve()
    country_index_path = (
        repository_root / args.opencti_country_index
    ).resolve()
    standalone_curation_path = (
        repository_root / args.standalone_activity_curation
    ).resolve()
    unknown_cluster_ledger_path = (
        repository_root / args.unknown_cluster_ledger
    ).resolve()
    output_root.relative_to(repository_root)

    country_index_document = load_json(country_index_path)
    country_index = country_index_document.get("countries", {})
    if not isinstance(country_index, dict) or not country_index:
        raise ValueError(
            f"invalid or empty OpenCTI country index: {country_index_path}"
        )

    wanted = set(args.actor or [])
    # Always prepare the complete corpus. Shared Locations/entities and the
    # producer object must not acquire different versions merely because a
    # targeted ``--actor`` export was requested.
    records = load_records(catalog_path, profiles_root, set())
    if not records:
        raise SystemExit("no actor profiles selected")
    identity_key_errors = validate_actor_identity_keys(records)
    if identity_key_errors:
        raise ValueError(identity_key_errors[0])
    modified = max(
        OPENCTI_MODEL_MODIFIED,
        *(record["profile"]["updated_at"] for record in records),
    )
    producer = repository_producer_identity()
    # Standalone Activities are part of the same Observable namespace even
    # during a targeted actor rebuild. Build a read-only preview first so role
    # labels on a shared SCO are the corpus-wide union in every bundle.
    standalone_curation, standalone_records = load_standalone_records(
        standalone_curation_path, unknown_cluster_ledger_path
    )
    standalone_updated_at = standalone_curation["updated_at"]
    standalone_previews = [
        build_standalone_activity_bundle(
            record=standalone_record,
            updated_at=standalone_updated_at,
            producer=producer,
            model_modified_at=OPENCTI_MODEL_MODIFIED,
        )[0]
        for standalone_record in standalone_records
    ]
    observable_role_index = build_observable_role_index(
        records, standalone_previews
    )
    for record in records:
        objects, rewrites = prepare_profile_objects(
            record["profile"],
            record["iocs"],
            record["full_bundle"],
            producer["id"],
            country_index,
            observable_role_index,
        )
        record["objects"] = objects
        record["id_rewrites"] = rewrites
    normalize_shared_object_versions(records)
    preserve_prepared_object_versions(
        records,
        load_previous_opencti_objects(output_root),
    )

    by_profile_id, by_name = build_actor_index(records)
    selected_records = [
        record for record in records if not wanted or record["slug"] in wanted
    ]
    if not selected_records:
        raise SystemExit("no actor profiles selected")
    expected_paths: set[Path] = set()
    actor_entries: list[dict[str, Any]] = []
    campaign_entries: list[dict[str, Any]] = []
    activity_entries: list[dict[str, Any]] = []
    standalone_entries: list[dict[str, Any]] = []
    unresolved_relationships: list[dict[str, str]] = []
    shared_object_definitions: dict[str, str] = {}
    max_size = 0
    for record in selected_records:
        profile = record["profile"]
        slug = record["slug"]
        actor_bundle, unresolved = build_actor_bundle(
            record, producer, by_profile_id, by_name
        )
        actor_path = output_root / "actors" / f"{slug}.stix2.json"
        preserve_object_versions(
            actor_bundle,
            load_json(actor_path) if actor_path.exists() else None,
        )
        actor_errors = validate_bundle(actor_bundle, expected_scope="actor")
        actor_errors.extend(
            validate_shared_object_definitions(
                actor_bundle, shared_object_definitions
            )
        )
        if actor_errors:
            raise ValueError(f"invalid actor bundle {slug}: {actor_errors[:10]}")
        write_json_atomic(actor_path, actor_bundle)
        actor_size = actor_path.stat().st_size
        if actor_size > args.max_bundle_bytes:
            raise ValueError(f"actor bundle exceeds size limit: {actor_path}")
        max_size = max(max_size, actor_size)
        expected_paths.add(actor_path.resolve())
        actor_entries.append(
            {
                "slug": slug,
                "profile_id": profile["profile_id"],
                "name": profile["name"],
                "path": actor_path.relative_to(repository_root).as_posix(),
                "object_count": len(actor_bundle["objects"]),
                "campaign_bundle_count": sum(
                    activity_stix_object_type(item) == "campaign"
                    for item in profile.get("activities", [])
                ),
                "activity_bundle_count": len(profile.get("activities", [])),
                "size_bytes": actor_size,
            }
        )
        unresolved_relationships.extend(
            {"slug": slug, "relationship_id": relation_id}
            for relation_id in unresolved
        )

        for activity in profile.get("activities", []):
            primary_type = activity_stix_object_type(activity)
            activity_bundle = build_activity_bundle(record, activity, producer)
            output_section = (
                "campaigns" if primary_type == "campaign" else "activities"
            )
            activity_path = (
                output_root
                / output_section
                / slug
                / safe_activity_filename(activity["activity_id"])
            )
            preserve_object_versions(
                activity_bundle,
                load_json(activity_path) if activity_path.exists() else None,
            )
            activity_errors = validate_bundle(
                activity_bundle, expected_scope=primary_type
            )
            activity_errors.extend(
                validate_shared_object_definitions(
                    activity_bundle, shared_object_definitions
                )
            )
            if activity_errors:
                raise ValueError(
                    f"invalid {primary_type} bundle "
                    f"{slug}/{activity['activity_id']}: "
                    f"{activity_errors[:10]}"
                )
            write_json_atomic(activity_path, activity_bundle)
            activity_size = activity_path.stat().st_size
            if activity_size > args.max_bundle_bytes:
                raise ValueError(
                    f"activity bundle exceeds size limit: {activity_path}"
                )
            max_size = max(max_size, activity_size)
            expected_paths.add(activity_path.resolve())
            entry = {
                "slug": slug,
                "profile_id": profile["profile_id"],
                "activity_id": activity["activity_id"],
                "name": activity["name"],
                "stix_object_type": primary_type,
                "path": activity_path.relative_to(repository_root).as_posix(),
                "object_count": len(activity_bundle["objects"]),
                "size_bytes": activity_size,
            }
            if primary_type == "campaign":
                campaign_entries.append(entry)
            else:
                activity_entries.append(entry)

    # Standalone activities are exported only for a full run. ``--actor`` is
    # an actor-profile selector and must not accidentally imply selection of a
    # heterogeneous ledger entry. The curation file is an explicit allowlist;
    # unknown-clusters.json is never traversed as an export queue.
    if not wanted:
        for standalone_record in standalone_records:
            bundle, entry = build_standalone_activity_bundle(
                record=standalone_record,
                updated_at=standalone_updated_at,
                producer=producer,
                model_modified_at=OPENCTI_MODEL_MODIFIED,
                observable_role_index=observable_role_index,
            )
            for obj in bundle.get("objects", []):
                complete_opencti_relationship_time_range(obj)
            primary_type = entry["stix_object_type"]
            output_section = (
                "campaigns" if primary_type == "campaign" else "activities"
            )
            activity_path = (
                output_root
                / output_section
                / "unattributed"
                / safe_activity_filename(entry["activity_id"])
            )
            preserve_object_versions(
                bundle,
                load_json(activity_path) if activity_path.exists() else None,
            )
            bundle_errors = validate_bundle(bundle, expected_scope=primary_type)
            bundle_errors.extend(
                validate_shared_object_definitions(bundle, shared_object_definitions)
            )
            if bundle_errors:
                raise ValueError(
                    f"invalid standalone {primary_type} bundle "
                    f"{entry['activity_id']}: {bundle_errors[:10]}"
                )
            write_json_atomic(activity_path, bundle)
            activity_size = activity_path.stat().st_size
            if activity_size > args.max_bundle_bytes:
                raise ValueError(
                    f"standalone activity bundle exceeds size limit: {activity_path}"
                )
            max_size = max(max_size, activity_size)
            expected_paths.add(activity_path.resolve())
            entry.update(
                {
                    "slug": "unattributed",
                    "profile_id": None,
                    "standalone_activity": True,
                    "path": activity_path.relative_to(repository_root).as_posix(),
                    "object_count": len(bundle["objects"]),
                    "size_bytes": activity_size,
                }
            )
            standalone_entries.append(entry)
            if primary_type == "campaign":
                campaign_entries.append(entry)
            else:
                activity_entries.append(entry)

    removed = prune_stale(output_root, expected_paths) if args.prune else 0
    manifest = {
        "schema_version": "1.1.0",
        "format": "STIX 2.1 bundles for OpenCTI ImportFileStix",
        "generated_at": modified,
        "producer_identity": producer["id"],
        "object_marking": "TLP:CLEAR",
        "import_order": ["actors", "campaigns", "activities"],
        "actor_bundle_count": len(actor_entries),
        "campaign_bundle_count": len(campaign_entries),
        "activity_bundle_count": len(activity_entries),
        "standalone_activity_bundle_count": len(standalone_entries),
        "activity_type_counts": dict(
            sorted(
                Counter(
                    item["stix_object_type"] for item in activity_entries
                ).items()
            )
        ),
        "max_bundle_size_bytes": max_size,
        "unresolved_actor_relationships": unresolved_relationships,
        "actors": actor_entries,
        "campaigns": campaign_entries,
        "activities": activity_entries,
        "standalone_activities": standalone_entries,
    }
    write_json_atomic(output_root / "manifest.json", manifest)
    print(
        json.dumps(
            {
                "actor_bundles": len(actor_entries),
                "campaign_bundles": len(campaign_entries),
                "activity_bundles": len(activity_entries),
                "standalone_activity_bundles": len(standalone_entries),
                "unresolved_actor_relationships": len(unresolved_relationships),
                "max_bundle_size_bytes": max_size,
                "pruned_files": removed,
                "manifest": str((output_root / "manifest.json").relative_to(repository_root)),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
