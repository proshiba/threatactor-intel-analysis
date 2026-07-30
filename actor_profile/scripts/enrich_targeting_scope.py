#!/usr/bin/env python3
"""Audit and enrich target-country and target-region scope for every profile.

Inputs are intentionally evidence preserving:

* reviewed profile activities and ATT&CK group summaries;
* high-confidence actor matches in the existing OSINT cross-check files;
* structured victim-geography fields from MISP/ETDA datasets;
* actor-specific primary-source curation.

Attribution countries, infrastructure locations, and countries that merely
issued attribution statements are not treated as victim countries.
"""

from __future__ import annotations

import argparse
import copy
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

from common import load_json, stable_digest, unknown_time, utc_now, write_json_atomic
from enrich_activity_intelligence import (
    actor_attribution_context,
    compile_rules,
    contextual_match,
    excerpt_for,
    mitre_target_match,
)


HERE = Path(__file__).resolve().parent
FRAMEWORK_ROOT = HERE.parent
REPO_ROOT = FRAMEWORK_ROOT.parent
DEFAULT_PROFILES = REPO_ROOT / "profiles"
DEFAULT_CATALOG = FRAMEWORK_ROOT / "corpus-catalog.json"
DEFAULT_ATTACK = FRAMEWORK_ROOT / "reference" / "attack-index.json"
DEFAULT_ACTIVITY_RULES = FRAMEWORK_ROOT / "activity-observation-rules.json"
DEFAULT_GEOGRAPHY = FRAMEWORK_ROOT / "target-geography.json"
DEFAULT_CURATION = FRAMEWORK_ROOT / "targeting-curation.json"
DEFAULT_REPORT = DEFAULT_PROFILES / "targeting-audit.json"

GENERATED_PREFIX = "target--targeting-audit--"
DERIVATION_NOTE = "[targeting-scope-audit-v1]"
TARGETING_LINE_PREFIX = "構造化ターゲット監査:"

CONFIDENCE_RANK = {"unknown": 0, "low": 1, "medium": 2, "high": 3}
AMBIGUOUS_TEXT_ALIASES = {"korea", "korean"}

DATASETS = {
    "misp-threat-actor": {
        "path": FRAMEWORK_ROOT / "reference" / "osint" / "misp-threat-actor.json",
        "source_id": "source--target-audit-misp-threat-actor",
        "value_path": ("meta", "cfr-suspected-victims"),
        "source": {
            "source_id": "source--target-audit-misp-threat-actor",
            "path": "actor_profile/reference/osint/misp-threat-actor.json",
            "url": "https://github.com/MISP/misp-galaxy/blob/main/clusters/threat-actor.json",
            "title": "MISP Galaxy Threat Actor victim geography fields",
            "publisher": "MISP Project / Council on Foreign Relations",
            "published_at": unknown_time(),
            "accessed_at": "2026-07-25T13:35:12Z",
            "language": "en",
            "source_type": "structured-osint-aggregation",
            "tlp": "TLP:CLEAR",
            "reliability": "medium",
            "sha256": None,
            "actor_scope": "overlapping",
            "claims_supported": ["targeting-lead", "victim-geography"],
            "analyst_notes": (
                "High-confidence actor-name matches only. Victim fields are "
                "aggregation leads and may inherit vendor collection-boundary "
                "differences; profile entries therefore use medium confidence."
            ),
        },
    },
    "etda-threat-group-cards": {
        "path": FRAMEWORK_ROOT / "reference" / "osint" / "etda-threat-group-cards.json",
        "source_id": "source--target-audit-etda-threat-group-cards",
        "value_path": ("observed-countries",),
        "source": {
            "source_id": "source--target-audit-etda-threat-group-cards",
            "path": "actor_profile/reference/osint/etda-threat-group-cards.json",
            "url": "https://apt.etda.or.th/cgi-bin/listgroups.cgi",
            "title": "ETDA Threat Group Cards observed-country fields",
            "publisher": "ETDA / ThaiCERT",
            "published_at": unknown_time(),
            "accessed_at": "2026-07-25T13:52:47Z",
            "language": "en",
            "source_type": "government-threat-actor-encyclopedia",
            "tlp": "TLP:CLEAR",
            "reliability": "medium",
            "sha256": None,
            "actor_scope": "overlapping",
            "claims_supported": ["targeting-lead", "victim-geography"],
            "analyst_notes": (
                "High-confidence actor-name matches only. ETDA aggregates "
                "vendor reporting; observed-country entries are retained as "
                "medium-confidence targeting evidence with scope caveats."
            ),
        },
    },
    "misp-360net": {
        "path": FRAMEWORK_ROOT / "reference" / "osint" / "misp-360net.json",
        "source_id": "source--target-audit-misp-360net",
        "value_path": ("meta", "suspected-victims"),
        "source": {
            "source_id": "source--target-audit-misp-360net",
            "path": "actor_profile/reference/osint/misp-360net.json",
            "url": "https://github.com/MISP/misp-galaxy/blob/main/clusters/360net.json",
            "title": "MISP 360.net suspected-victim fields",
            "publisher": "MISP Project / 360.net",
            "published_at": unknown_time(),
            "accessed_at": "2026-07-25T13:35:12Z",
            "language": "zh",
            "source_type": "structured-osint-aggregation",
            "tlp": "TLP:CLEAR",
            "reliability": "medium",
            "sha256": None,
            "actor_scope": "overlapping",
            "claims_supported": ["targeting-lead", "victim-geography"],
            "analyst_notes": (
                "High-confidence actor-name matches only. Suspected-victim "
                "fields are vendor assessments and may reflect geopolitical "
                "source bias; entries use medium confidence."
            ),
        },
    },
}


def normalize_key(value: str) -> str:
    return re.sub(
        r"[^a-z0-9\u3040-\u30ff\u3400-\u9fff]+",
        "",
        value.casefold(),
    )


def confidence_max(left: str, right: str) -> str:
    return max((left, right), key=lambda item: CONFIDENCE_RANK.get(item, 0))


def known_time(point: dict[str, Any] | None) -> bool:
    return bool(point and point.get("status") in {"known", "inferred"} and point.get("value"))


def time_min(
    left: dict[str, Any] | None,
    right: dict[str, Any] | None,
) -> dict[str, Any]:
    if not known_time(left):
        return copy.deepcopy(right) if known_time(right) else unknown_time()
    if not known_time(right):
        return copy.deepcopy(left)
    return copy.deepcopy(left if left["value"] <= right["value"] else right)


def time_max(
    left: dict[str, Any] | None,
    right: dict[str, Any] | None,
) -> dict[str, Any]:
    if not known_time(left):
        return copy.deepcopy(right) if known_time(right) else unknown_time()
    if not known_time(right):
        return copy.deepcopy(left)
    return copy.deepcopy(left if left["value"] >= right["value"] else right)


def compile_literal(alias: str) -> re.Pattern[str]:
    escaped = re.escape(alias)
    if re.search(r"[A-Za-z0-9]", alias):
        return re.compile(rf"(?<![A-Za-z0-9]){escaped}(?![A-Za-z0-9])", re.IGNORECASE)
    return re.compile(escaped)


class Geography:
    def __init__(self, raw: dict[str, Any]) -> None:
        self.countries = raw["countries"]
        self.regions = raw["regions"]
        self.country_by_key: dict[str, dict[str, Any]] = {}
        self.region_by_key: dict[str, dict[str, Any]] = {}
        for item in self.countries:
            for value in [item["name"], *item.get("aliases", [])]:
                self.country_by_key[normalize_key(value)] = item
            item["_patterns"] = [
                compile_literal(value)
                for value in [item["name"], *item.get("aliases", [])]
                if normalize_key(value) not in AMBIGUOUS_TEXT_ALIASES
            ]
        for item in self.regions:
            for value in [item["name"], *item.get("aliases", [])]:
                self.region_by_key[normalize_key(value)] = item
            item["_patterns"] = [
                compile_literal(value)
                for value in [item["name"], *item.get("aliases", [])]
            ]

    def exact_country(self, value: str) -> dict[str, Any] | None:
        return self.country_by_key.get(normalize_key(value))

    def exact_region(self, value: str) -> dict[str, Any] | None:
        return self.region_by_key.get(normalize_key(value))

    @staticmethod
    def _mentions(
        text: str,
        entries: Iterable[dict[str, Any]],
    ) -> list[tuple[dict[str, Any], re.Match[str]]]:
        candidates: list[tuple[int, int, dict[str, Any], re.Match[str]]] = []
        for entry in entries:
            for pattern in entry["_patterns"]:
                for match in pattern.finditer(text):
                    candidates.append(
                        (match.start(), -(match.end() - match.start()), entry, match)
                    )
        candidates.sort(key=lambda row: (row[0], row[1]))
        accepted: list[tuple[dict[str, Any], re.Match[str]]] = []
        occupied: list[tuple[int, int]] = []
        for _, _, entry, match in candidates:
            span = match.span()
            if any(span[0] < end and start < span[1] for start, end in occupied):
                continue
            occupied.append(span)
            accepted.append((entry, match))
        return accepted

    def classify_value(self, value: str) -> tuple[set[str], set[str]]:
        exact_country = self.exact_country(value)
        if exact_country:
            return {exact_country["name"]}, set()
        exact_region = self.exact_region(value)
        if exact_region:
            return set(), {exact_region["name"]}
        countries = {
            entry["name"] for entry, _ in self._mentions(value, self.countries)
        }
        regions = {
            entry["name"] for entry, _ in self._mentions(value, self.regions)
        }
        return countries, regions

    def target_mentions(
        self,
        text: str,
        *,
        target_context_patterns: list[re.Pattern[str]],
        actor_pattern: re.Pattern[str] | None,
        mitre: bool,
    ) -> tuple[set[str], set[str]]:
        countries: set[str] = set()
        regions: set[str] = set()
        for entry in self.countries:
            match = (
                mitre_target_match(
                    text,
                    entry["_patterns"],
                    country=True,
                    actor_pattern=actor_pattern,
                )
                if mitre
                else contextual_match(
                    text,
                    entry["_patterns"],
                    target_context_patterns,
                    country=True,
                    actor_pattern=actor_pattern,
                )
            )
            if match is not None:
                countries.add(entry["name"])
        for entry in self.regions:
            match = (
                mitre_target_match(
                    text,
                    entry["_patterns"],
                    country=True,
                    actor_pattern=actor_pattern,
                )
                if mitre
                else contextual_match(
                    text,
                    entry["_patterns"],
                    target_context_patterns,
                    country=True,
                    actor_pattern=actor_pattern,
                )
            )
            if match is not None:
                regions.add(entry["name"])
        return countries, regions

    def regions_for_country(self, name: str) -> set[str]:
        item = self.exact_country(name)
        return set(item.get("regions", [])) if item else set()


def nested_values(item: dict[str, Any], path: tuple[str, ...]) -> list[str]:
    value: Any = item
    for key in path:
        if not isinstance(value, dict):
            return []
        value = value.get(key)
    if not isinstance(value, list):
        return []
    return [str(entry).strip() for entry in value if str(entry).strip()]


def candidate() -> dict[str, Any]:
    return {
        "evidence_refs": set(),
        "confidence": "unknown",
        "first_observed": unknown_time(),
        "last_observed": unknown_time(),
        "description": "",
        "description_priority": -1,
        "notes": set(),
        "origins": set(),
    }


def add_candidate(
    candidates: dict[str, dict[str, Any]],
    name: str,
    *,
    evidence_refs: Iterable[str],
    confidence: str,
    description: str,
    description_priority: int,
    note: str,
    origin: str,
    first_observed: dict[str, Any] | None = None,
    last_observed: dict[str, Any] | None = None,
) -> None:
    item = candidates.setdefault(name, candidate())
    item["evidence_refs"].update(evidence_refs)
    item["confidence"] = confidence_max(item["confidence"], confidence)
    if description_priority > item["description_priority"]:
        item["description"] = description
        item["description_priority"] = description_priority
    if note:
        item["notes"].add(note)
    item["origins"].add(origin)
    item["first_observed"] = time_min(
        item["first_observed"], first_observed or unknown_time()
    )
    item["last_observed"] = time_max(
        item["last_observed"], last_observed or unknown_time()
    )


def cleanup_generated(profile: dict[str, Any]) -> None:
    removed = {
        item["id"]
        for category in ("countries", "regions")
        for item in profile["targets"].get(category, [])
        if item.get("id", "").startswith(GENERATED_PREFIX)
    }
    for category in ("countries", "regions"):
        profile["targets"][category] = [
            item
            for item in profile["targets"].get(category, [])
            if item.get("id") not in removed
        ]
    replace_refs(profile, {item: None for item in removed})


def replace_refs(
    profile: dict[str, Any],
    replacements: dict[str, str | None],
) -> None:
    for collection in ("activities", "victim_cases"):
        for item in profile.get(collection, []):
            refs = item.get("target_refs", [])
            updated: list[str] = []
            for ref in refs:
                replacement = replacements.get(ref, ref)
                if replacement and replacement not in updated:
                    updated.append(replacement)
            item["target_refs"] = updated


def merge_target_objects(keeper: dict[str, Any], other: dict[str, Any]) -> None:
    keeper["evidence_refs"] = sorted(
        set(keeper.get("evidence_refs", [])) | set(other.get("evidence_refs", []))
    )
    keeper["first_observed"] = time_min(
        keeper.get("first_observed"), other.get("first_observed")
    )
    keeper["last_observed"] = time_max(
        keeper.get("last_observed"), other.get("last_observed")
    )
    keeper["confidence"] = confidence_max(
        keeper.get("confidence", "unknown"),
        other.get("confidence", "unknown"),
    )
    notes = [keeper.get("analyst_notes", ""), other.get("analyst_notes", "")]
    keeper["analyst_notes"] = " ".join(
        dict.fromkeys(value.strip() for value in notes if value.strip())
    )


def target_priority(item: dict[str, Any]) -> int:
    item_id = item.get("id", "")
    if item_id.startswith("target--osint--"):
        return 5
    if not item_id.startswith(
        ("target--activity-rule--", "target--mitre-group--", GENERATED_PREFIX)
    ):
        return 4
    if item_id.startswith(GENERATED_PREFIX):
        return 3
    if item_id.startswith("target--mitre-group--"):
        return 2
    return 1


def canonicalize_existing(profile: dict[str, Any], geography: Geography) -> None:
    moved_to_regions: list[dict[str, Any]] = []
    kept_countries: list[dict[str, Any]] = []
    for item in profile["targets"].get("countries", []):
        country = geography.exact_country(item.get("name", ""))
        region = geography.exact_region(item.get("name", ""))
        if country:
            item["name"] = country["name"]
            kept_countries.append(item)
        elif region:
            item["name"] = region["name"]
            moved_to_regions.append(item)
        else:
            kept_countries.append(item)
    profile["targets"]["countries"] = kept_countries
    for item in profile["targets"].get("regions", []):
        region = geography.exact_region(item.get("name", ""))
        if region:
            item["name"] = region["name"]
    profile["targets"]["regions"].extend(moved_to_regions)
    dedupe_targets(profile, "countries")
    dedupe_targets(profile, "regions")


def dedupe_targets(profile: dict[str, Any], category: str) -> None:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in profile["targets"].get(category, []):
        grouped[normalize_key(item.get("name", ""))].append(item)
    result: list[dict[str, Any]] = []
    replacements: dict[str, str] = {}
    for items in grouped.values():
        items.sort(key=target_priority, reverse=True)
        keeper = items[0]
        result.append(keeper)
        for other in items[1:]:
            merge_target_objects(keeper, other)
            replacements[other["id"]] = keeper["id"]
    profile["targets"][category] = result
    replace_refs(profile, replacements)


def upsert_target(
    profile: dict[str, Any],
    category: str,
    name: str,
    item: dict[str, Any],
) -> dict[str, Any]:
    existing = next(
        (
            target
            for target in profile["targets"][category]
            if normalize_key(target.get("name", "")) == normalize_key(name)
        ),
        None,
    )
    if existing is None:
        kind = "country" if category == "countries" else "region"
        digest = stable_digest(profile["profile_id"], kind, name)[:20]
        existing = {
            "id": f"{GENERATED_PREFIX}{kind}--{digest}",
            "name": name,
            "description": item["description"],
            "first_observed": copy.deepcopy(item["first_observed"]),
            "last_observed": copy.deepcopy(item["last_observed"]),
            "confidence": item["confidence"],
            "evidence_refs": sorted(item["evidence_refs"]),
            "analyst_notes": (
                f"{DERIVATION_NOTE} "
                + " ".join(sorted(item["notes"]))
            ).strip(),
        }
        profile["targets"][category].append(existing)
        return existing
    existing["evidence_refs"] = sorted(
        set(existing.get("evidence_refs", [])) | set(item["evidence_refs"])
    )
    existing["first_observed"] = time_min(
        existing.get("first_observed"), item["first_observed"]
    )
    existing["last_observed"] = time_max(
        existing.get("last_observed"), item["last_observed"]
    )
    existing["confidence"] = confidence_max(
        existing.get("confidence", "unknown"), item["confidence"]
    )
    if item["description_priority"] >= 3:
        existing["description"] = item["description"]
    note = f"{DERIVATION_NOTE} " + " ".join(sorted(item["notes"]))
    if DERIVATION_NOTE not in existing.get("analyst_notes", ""):
        existing["analyst_notes"] = (
            existing.get("analyst_notes", "").rstrip() + " " + note
        ).strip()
    return existing


def ensure_source(profile: dict[str, Any], source: dict[str, Any]) -> None:
    for index, existing in enumerate(profile["sources"]):
        if existing.get("source_id") == source["source_id"]:
            profile["sources"][index] = copy.deepcopy(source)
            return
    profile["sources"].append(copy.deepcopy(source))


def catalog_group_map(catalog: dict[str, Any]) -> dict[str, str]:
    return {
        item["slug"]: item["mitre_group_id"]
        for item in catalog["actors"]
        if item.get("mitre_group_id")
    }


def actor_names(profile: dict[str, Any]) -> set[str]:
    return {
        value
        for value in [
            profile.get("name", ""),
            profile.get("actor", {}).get("canonical_name", ""),
            *[
                alias.get("name", "")
                for alias in profile.get("actor", {}).get("aliases", [])
            ],
        ]
        if value
    }


def collect_mitre(
    profile: dict[str, Any],
    group: dict[str, Any] | None,
    geography: Geography,
    compiled_rules: dict[str, Any],
    countries: dict[str, dict[str, Any]],
    regions: dict[str, dict[str, Any]],
) -> None:
    if not group:
        return
    description = group.get("description", "")
    country_names, region_names = geography.target_mentions(
        description,
        target_context_patterns=compiled_rules["_target_context_patterns"],
        actor_pattern=compiled_rules.get("_actor_pattern"),
        mitre=True,
    )
    for name in country_names:
        add_candidate(
            countries,
            name,
            evidence_refs=["source--mitre-attack-19-1"],
            confidence="high",
            description=(
                f"MITRE ATT&CKのGroup概要で{profile['name']}の標的国として"
                "明示されている。"
            ),
            description_priority=2,
            note="公式ATT&CKのGroup概要から構造化。",
            origin="mitre-group",
        )
    for name in region_names:
        add_candidate(
            regions,
            name,
            evidence_refs=["source--mitre-attack-19-1"],
            confidence="high",
            description=(
                f"MITRE ATT&CKのGroup概要で{profile['name']}の標的範囲として"
                f"{name}が明示されている。"
            ),
            description_priority=2,
            note="公式ATT&CKのGroup概要から構造化。",
            origin="mitre-group",
        )


def collect_activities(
    profile: dict[str, Any],
    geography: Geography,
    compiled_rules: dict[str, Any],
    countries: dict[str, dict[str, Any]],
    regions: dict[str, dict[str, Any]],
) -> None:
    for activity in profile.get("activities", []):
        text = " ".join(
            value
            for value in [activity.get("name", ""), activity.get("description", "")]
            if value
        )
        country_names, region_names = geography.target_mentions(
            text,
            target_context_patterns=compiled_rules["_target_context_patterns"],
            actor_pattern=compiled_rules.get("_actor_pattern"),
            mitre=False,
        )
        for name in country_names:
            add_candidate(
                countries,
                name,
                evidence_refs=activity.get("evidence_refs", []),
                confidence=(
                    "medium"
                    if activity.get("confidence") in {"high", "medium"}
                    else "low"
                ),
                description=(
                    f"活動「{activity['name']}」の記述で標的・被害国として"
                    "明示されている。"
                ),
                description_priority=2,
                note="活動記述の標的文脈から構造化。",
                origin="activity",
                first_observed=activity.get("first_observed"),
                last_observed=activity.get("last_observed"),
            )
        for name in region_names:
            add_candidate(
                regions,
                name,
                evidence_refs=activity.get("evidence_refs", []),
                confidence=(
                    "medium"
                    if activity.get("confidence") in {"high", "medium"}
                    else "low"
                ),
                description=(
                    f"活動「{activity['name']}」の記述で標的地域として{name}が"
                    "明示されている。"
                ),
                description_priority=2,
                note="活動記述の標的文脈から構造化。",
                origin="activity",
                first_observed=activity.get("first_observed"),
                last_observed=activity.get("last_observed"),
            )


def collect_reviewed_targeting_text(
    profile: dict[str, Any],
    geography: Geography,
    countries: dict[str, dict[str, Any]],
    regions: dict[str, dict[str, Any]],
) -> None:
    """Structure geography already preserved in the dedicated target notes.

    Historical bootstrap profiles copied this field from the reviewed actor
    mapping workbook but did not always materialize its countries and regions.
    The generated audit summary is excluded so repeated runs cannot feed their
    own output back into the profile.
    """

    source_id = "source--actor-mapping-workbook"
    if not any(
        item.get("source_id") == source_id for item in profile.get("sources", [])
    ):
        return
    text = "\n".join(
        line
        for line in profile.get("free_text", {})
        .get("targeting_details", "")
        .splitlines()
        if not line.startswith(TARGETING_LINE_PREFIX)
    ).strip()
    if not text:
        return
    country_names = {
        entry["name"] for entry, _ in geography._mentions(text, geography.countries)
    }
    # "US" is intentionally not a global case-insensitive country alias:
    # doing so would confuse the English pronoun "us" in arbitrary prose.
    if re.search(r"(?<![A-Za-z0-9])US(?![A-Za-z0-9])", text):
        country_names.add("米国")
    region_names = {
        entry["name"] for entry, _ in geography._mentions(text, geography.regions)
    }
    for name in country_names:
        add_candidate(
            countries,
            name,
            evidence_refs=[source_id],
            confidence="medium",
            description=(
                "レビュー済みアクターマッピングの標的欄に記録された"
                f"{name}を構造化した。"
            ),
            description_priority=1,
            note="既存の標的専用自由記述から構造化。",
            origin="reviewed-targeting-text",
        )
    for name in region_names:
        add_candidate(
            regions,
            name,
            evidence_refs=[source_id],
            confidence="medium",
            description=(
                "レビュー済みアクターマッピングの標的欄に記録された"
                f"{name}を構造化した。"
            ),
            description_priority=1,
            note="既存の標的専用自由記述から構造化。",
            origin="reviewed-targeting-text",
        )


def load_dataset_indexes() -> dict[str, dict[str, dict[str, Any]]]:
    indexes: dict[str, dict[str, dict[str, Any]]] = {}
    for dataset_id, spec in DATASETS.items():
        if not spec["path"].exists():
            indexes[dataset_id] = {}
            continue
        data = load_json(spec["path"])
        indexes[dataset_id] = {
            item["uuid"]: item
            for item in data.get("values", [])
            if item.get("uuid")
        }
    return indexes


def collect_crosscheck(
    profile: dict[str, Any],
    crosscheck: dict[str, Any] | None,
    dataset_indexes: dict[str, dict[str, dict[str, Any]]],
    geography: Geography,
    countries: dict[str, dict[str, Any]],
    regions: dict[str, dict[str, Any]],
) -> tuple[set[str], set[str], set[str]]:
    used_sources: set[str] = set()
    unresolved: set[str] = set()
    raw_values: set[str] = set()
    if not crosscheck:
        return used_sources, unresolved, raw_values
    for dataset_id, spec in DATASETS.items():
        for match in crosscheck.get("actor_matches", {}).get(dataset_id, []):
            if match.get("match_confidence") != "high":
                continue
            if match.get("match_basis") not in {
                "canonical-name",
                "mitre-external-id",
                "multiple-name-intersection",
            }:
                continue
            entry = dataset_indexes.get(dataset_id, {}).get(match.get("entry_uuid"))
            if not entry:
                continue
            for raw_value in nested_values(entry, spec["value_path"]):
                raw_values.add(raw_value)
                country_names, region_names = geography.classify_value(raw_value)
                if not country_names and not region_names:
                    unresolved.add(raw_value)
                    continue
                used_sources.add(spec["source_id"])
                for name in country_names:
                    add_candidate(
                        countries,
                        name,
                        evidence_refs=[spec["source_id"]],
                        confidence="medium",
                        description=(
                            f"構造化OSINTの被害国フィールドで{profile['name']}の"
                            f"標的・被害国として{name}が記録されている。"
                        ),
                        description_priority=1,
                        note=(
                            "集約データの追跡範囲はベンダーごとに異なるため、"
                            "中確度の標的地理情報として扱う。"
                        ),
                        origin=dataset_id,
                    )
                for name in region_names:
                    add_candidate(
                        regions,
                        name,
                        evidence_refs=[spec["source_id"]],
                        confidence="medium",
                        description=(
                            f"構造化OSINTの被害地域フィールドで{profile['name']}の"
                            f"標的範囲として{name}が記録されている。"
                        ),
                        description_priority=1,
                        note=(
                            "集約データの追跡範囲はベンダーごとに異なるため、"
                            "中確度の標的地理情報として扱う。"
                        ),
                        origin=dataset_id,
                    )
    return used_sources, unresolved, raw_values


def collect_curation(
    profile: dict[str, Any],
    curation: dict[str, Any] | None,
    countries: dict[str, dict[str, Any]],
    regions: dict[str, dict[str, Any]],
) -> set[str]:
    if not curation:
        return set()
    country_refs = curation.get("country_source_refs", [])
    region_refs = curation.get("region_source_refs", [])
    for name in curation.get("countries", []):
        add_candidate(
            countries,
            name,
            evidence_refs=country_refs,
            confidence="high",
            description=curation.get("description", ""),
            description_priority=3,
            note=curation.get("analyst_notes", ""),
            origin="reviewed-curation",
        )
    for name in curation.get("regions", []):
        add_candidate(
            regions,
            name,
            evidence_refs=region_refs,
            confidence="high",
            description=curation.get("description", ""),
            description_priority=3,
            note=curation.get("analyst_notes", ""),
            origin="reviewed-curation",
        )
    for source in curation.get("sources", []):
        ensure_source(profile, source)
    return {
        source["source_id"] for source in curation.get("sources", [])
    }


def derive_regions(
    profile: dict[str, Any],
    geography: Geography,
    regions: dict[str, dict[str, Any]],
) -> None:
    by_region: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for target in profile["targets"].get("countries", []):
        for region in geography.regions_for_country(target.get("name", "")):
            by_region[region].append(target)
    for region, targets in by_region.items():
        distinct = {item["name"] for item in targets}
        if len(distinct) < 2:
            continue
        evidence_refs = {
            ref for item in targets for ref in item.get("evidence_refs", [])
        }
        add_candidate(
            regions,
            region,
            evidence_refs=evidence_refs,
            confidence="medium",
            description=(
                f"{'、'.join(sorted(distinct))}で確認された標的・被害事例を"
                f"{region}として集約した地域表示。"
            ),
            description_priority=0,
            note=(
                "複数の個別国から導出した地域表示。域内の全国家・組織が"
                "標的だったことを意味しない。"
            ),
            origin="derived-from-countries",
        )


def update_targeting_text(profile: dict[str, Any]) -> None:
    countries = [item["name"] for item in profile["targets"].get("countries", [])]
    regions = [item["name"] for item in profile["targets"].get("regions", [])]
    if not countries and not regions:
        line = (
            f"{TARGETING_LINE_PREFIX} 現時点で根拠付きの標的国・地域を"
            "構造化できていない。追加収集が必要。"
        )
    else:
        country_text = "、".join(countries[:24]) or "個別国なし"
        if len(countries) > 24:
            country_text += f"ほか{len(countries) - 24}か国"
        region_text = "、".join(regions) or "広域情報なし"
        line = (
            f"{TARGETING_LINE_PREFIX} 標的国={country_text}。"
            f"標的地域={region_text}。日本は確認時に個別国として保持する。"
        )
    current = profile["free_text"].get("targeting_details", "")
    lines = [
        existing
        for existing in current.splitlines()
        if not existing.startswith(TARGETING_LINE_PREFIX)
    ]
    profile["free_text"]["targeting_details"] = "\n\n".join(
        [line, *[existing for existing in lines if existing.strip()]]
    ).strip()


def append_audit_notes(profile: dict[str, Any]) -> None:
    logic = (
        "標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした"
        "個別補正、および高確度でアクター照合できた構造化OSINTの被害地理"
        "フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、"
        "日本は確認できた場合に地域表示とは別に個別保持する。"
    )
    if not profile["targets"].get("selection_logic"):
        profile["targets"]["selection_logic"] = logic
    elif logic not in profile["targets"]["selection_logic"]:
        profile["targets"]["selection_logic"] = (
            profile["targets"]["selection_logic"].rstrip() + " " + logic
        )
    note = (
        f"{DERIVATION_NOTE} 地域は明示記述または複数の個別国から導出する。"
        "導出地域は域内全体への攻撃を意味しない。OSINT集約値は中確度とし、"
        "ベンダー間のアクター集合境界差を保持する。"
    )
    if DERIVATION_NOTE not in profile["targets"].get("analyst_notes", ""):
        profile["targets"]["analyst_notes"] = (
            profile["targets"].get("analyst_notes", "").rstrip() + " " + note
        ).strip()


def process_profile(
    profile: dict[str, Any],
    *,
    slug: str,
    geography: Geography,
    compiled_rules: dict[str, Any],
    group: dict[str, Any] | None,
    crosscheck: dict[str, Any] | None,
    dataset_indexes: dict[str, dict[str, dict[str, Any]]],
    curation: dict[str, Any] | None,
) -> dict[str, Any]:
    before_countries = [
        item.get("name") for item in profile["targets"].get("countries", [])
    ]
    before_regions = [
        item.get("name") for item in profile["targets"].get("regions", [])
    ]
    cleanup_generated(profile)
    canonicalize_existing(profile, geography)
    countries: dict[str, dict[str, Any]] = {}
    regions: dict[str, dict[str, Any]] = {}
    collect_mitre(profile, group, geography, compiled_rules, countries, regions)
    collect_activities(profile, geography, compiled_rules, countries, regions)
    collect_reviewed_targeting_text(profile, geography, countries, regions)
    used_sources, unresolved, raw_values = collect_crosscheck(
        profile,
        crosscheck,
        dataset_indexes,
        geography,
        countries,
        regions,
    )
    used_sources |= collect_curation(profile, curation, countries, regions)
    for source_id in used_sources:
        for spec in DATASETS.values():
            if spec["source_id"] == source_id:
                ensure_source(profile, spec["source"])
                break
    for name, item in countries.items():
        upsert_target(profile, "countries", name, item)
    derive_regions(profile, geography, regions)
    for name, item in regions.items():
        upsert_target(profile, "regions", name, item)
    dedupe_targets(profile, "countries")
    dedupe_targets(profile, "regions")
    profile["targets"]["countries"].sort(key=lambda item: item["name"])
    profile["targets"]["regions"].sort(key=lambda item: item["name"])
    append_audit_notes(profile)
    update_targeting_text(profile)
    after_countries = [
        item.get("name") for item in profile["targets"].get("countries", [])
    ]
    after_regions = [
        item.get("name") for item in profile["targets"].get("regions", [])
    ]
    flags: list[str] = []
    if not after_countries and not after_regions:
        flags.append("no-structured-geography")
    if len(after_countries) == 1 and not after_regions:
        flags.append("single-country-no-region")
    if after_countries == ["日本"] and not after_regions:
        flags.append("japan-only")
    if unresolved:
        flags.append("unresolved-osint-values")
    return {
        "slug": slug,
        "name": profile["name"],
        "before_country_count": len(before_countries),
        "after_country_count": len(after_countries),
        "before_region_count": len(before_regions),
        "after_region_count": len(after_regions),
        "countries_added": sorted(set(after_countries) - set(before_countries)),
        "regions_added": sorted(set(after_regions) - set(before_regions)),
        "sources_used": sorted(used_sources),
        "raw_osint_value_count": len(raw_values),
        "unresolved_osint_values": sorted(unresolved),
        "flags": flags,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profiles_root", nargs="?", type=Path, default=DEFAULT_PROFILES)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--attack-index", type=Path, default=DEFAULT_ATTACK)
    parser.add_argument("--activity-rules", type=Path, default=DEFAULT_ACTIVITY_RULES)
    parser.add_argument("--geography", type=Path, default=DEFAULT_GEOGRAPHY)
    parser.add_argument("--curation", type=Path, default=DEFAULT_CURATION)
    parser.add_argument("--actor", action="append", default=[])
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    catalog = load_json(args.catalog)
    attack = load_json(args.attack_index)
    geography = Geography(load_json(args.geography))
    compiled_rules = compile_rules(load_json(args.activity_rules), catalog)
    group_ids = catalog_group_map(catalog)
    curation = load_json(args.curation).get("actors", {}) if args.curation.exists() else {}
    dataset_indexes = load_dataset_indexes()
    actor_filter = set(args.actor)
    rows: list[dict[str, Any]] = []
    changed = 0

    for path in sorted(args.profiles_root.glob("*/actor-profile.json")):
        slug = path.parent.name
        if actor_filter and slug not in actor_filter:
            continue
        profile = load_json(path)
        before = json.dumps(profile, ensure_ascii=False, sort_keys=True)
        crosscheck_path = path.parent / "osint-crosscheck.json"
        crosscheck = load_json(crosscheck_path) if crosscheck_path.exists() else None
        group = attack.get("groups", {}).get(group_ids.get(slug, ""))
        row = process_profile(
            profile,
            slug=slug,
            geography=geography,
            compiled_rules=compiled_rules,
            group=group,
            crosscheck=crosscheck,
            dataset_indexes=dataset_indexes,
            curation=curation.get(slug),
        )
        after = json.dumps(profile, ensure_ascii=False, sort_keys=True)
        row["changed"] = before != after
        if row["changed"]:
            changed += 1
            if args.apply:
                profile["updated_at"] = utc_now()
                write_json_atomic(path, profile)
        rows.append(row)

    summary = {
        "mode": "apply" if args.apply else "dry-run",
        "profiles_scanned": len(rows),
        "profiles_changed": changed,
        "profiles_with_countries": sum(row["after_country_count"] > 0 for row in rows),
        "profiles_with_regions": sum(row["after_region_count"] > 0 for row in rows),
        "profiles_without_geography": sum(
            "no-structured-geography" in row["flags"] for row in rows
        ),
        "single_country_without_region": sum(
            "single-country-no-region" in row["flags"] for row in rows
        ),
        "japan_only": sum("japan-only" in row["flags"] for row in rows),
        "country_targets": sum(row["after_country_count"] for row in rows),
        "region_targets": sum(row["after_region_count"] for row in rows),
        "profiles_with_unresolved_osint_values": sum(
            bool(row["unresolved_osint_values"]) for row in rows
        ),
        "unresolved_osint_value_count": sum(
            len(row["unresolved_osint_values"]) for row in rows
        ),
    }
    report = {
        "schema_version": "1.0.0",
        "generated_at": utc_now(),
        "summary": summary,
        "profiles": rows,
    }
    if args.report:
        write_json_atomic(args.report, report)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
