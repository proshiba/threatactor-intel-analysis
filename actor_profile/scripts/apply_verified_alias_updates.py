#!/usr/bin/env python3
"""Apply primary-source-verified actor aliases and entity boundaries.

The mappings in this migration intentionally distinguish vendor renames from
cross-vendor overlap. Aggregation-only names are not promoted here.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from bootstrap_all_profiles import normalized_name
from common import load_json, normalize_time, stable_digest, unknown_time, utc_now, write_json_atomic


GTIG_URL = "https://cloud.google.com/blog/topics/threat-intelligence/updated-cyber-threat-actor-naming-system"
GTIG_SOURCE_ID = "source--gtig-unified-actor-naming-2026"
MICROSOFT_SOURCE_ID = "source--osint-microsoft-threat-actor-mapping"

# (profile slug, previous GTIG names). The new GTIG name is the dictionary key.
GTIG_MAPPINGS: dict[str, tuple[str, list[str]]] = {
    "RAZOR COMET": ("fin11", ["FIN11"]),
    "SQUID COMET": ("fin6", ["FIN6"]),
    "WILD COMET": ("fin7", ["FIN7"]),
    "PUNCH COMET": ("fin8", ["FIN8"]),
    "BLEAK ION": ("apt33", ["APT33"]),
    "SOLAR ION": ("apt34", ["APT34"]),
    "RICH ION": ("charming-kitten", ["APT35"]),
    "CINDER ION": ("apt39", ["APT39"]),
    "CALANQUE ION": ("apt42", ["APT42", "CALANQUE"]),
    "MUDDY ION": ("muddywater", ["TEMP.Zagros", "MUDDYCOAST"]),
    "PLAIN NEPTUNE": ("apt37", ["APT37"]),
    "GRASS NEPTUNE": ("apt45", ["APT45"]),
    "MIDNIGHT NEPTUNE": ("unc1069", ["UNC1069", "MASAN"]),
    "HERMIT NEPTUNE": ("temp-hermit", ["TEMP.Hermit"]),
    "RIVER CASTLE": ("ke3chang", ["APT15"]),
    "RIDGE CASTLE": ("violin-panda", ["APT20"]),
    "RAVINE CASTLE": ("apt24", ["UNC1088"]),
    "SHORE CASTLE": ("threat-group-3390", ["APT27"]),
    "ISTHMUS CASTLE": ("apt30", ["APT30"]),
    "TIDE CASTLE": ("zirconium", ["APT31"]),
    "ISLAND CASTLE": ("leviathan", ["APT40"]),
    "SPIRE CASTLE": ("apt41", ["APT41"]),
    "BASALT CASTLE": ("apt5", ["APT5"]),
    "LONE CASTLE": ("tonto-team", ["Tonto Team"]),
    "TICK CASTLE": ("tick", ["TEMP.Tick"]),
    "DARK CASTLE": ("unc2814", ["UNC2814"]),
    "NAIKON CASTLE": ("naikon", ["Naikon Team"]),
    "BASIN CASTLE": ("mustang-panda", ["TEMP.Hex"]),
    "CAVERN CASTLE": ("blacktech", ["TEMP.Overboard"]),
    "LAKE RELIC": ("apt28", ["APT28", "FROZENLAKE"]),
    "ICE RELIC": ("apt29", ["APT29", "ICECAP"]),
    "SANDWORM RELIC": ("sandworm", ["APT44", "FROZENBARENTS"]),
    "COLD RELIC": ("callisto", ["UNC4057", "COLDRIVER"]),
    "VERMIN RELIC": ("uac-0020", ["TEMP.Vermin"]),
    "TURLA RELIC": ("turla", ["Turla Team"]),
}

BOUNDARY_REMOVALS = {
    "ta505": {
        "DEV-0950",
        "Evil Corp",
        "FIN11",
        "Indrik Spider",
        "Lace Tempest",
        "TA505 (merged w/Indrik Spider)",
    },
    "lace-tempest": {"FIN11", "TA505"},
    "apt38": {"TEMP.Hermit"},
    "naikon": {"APT30"},
    "dragonfly": {"ALLANITE"},
}

MICROSOFT_MAPPINGS = {
    "unc5792": ["Frontier Blizzard"],
    "unc6040": ["Storm-2581"],
    "unc6240": ["Storm-3127"],
}

MITRE_19_2_MAPPINGS = {
    "teampcp": ("G1056", ["DeadCatx3", "PCPCat", "SHADOW-WATER-058", "ShellForce", "UNC6780"]),
    "unc6240": ("G1057", ["Bling Libra", "ShinyHunters"]),
}

CYBERAV3NGERS_ALIASES = [
    "APT Iran",
    "Bauxite",
    "Hydro Kitten",
    "Mr. Soul",
    "Shahid Kaveh Group",
    "Soldiers of Soloman",
    "Soldiers of Solomon",
    "Storm-0784",
    "UNC5691",
]

BLACKTECH_ALIASES = ["Circuit Panda", "Palmerworm", "Radio Panda", "TEMP.Overboard"]


def time_value(value: str | None) -> dict[str, Any]:
    return normalize_time(value, basis="source-publication") if value else unknown_time()


SOURCES: dict[str, dict[str, Any]] = {
    GTIG_SOURCE_ID: {
        "source_id": GTIG_SOURCE_ID,
        "path": GTIG_URL,
        "url": GTIG_URL,
        "title": "Updated Cyber Threat Actor Naming System",
        "publisher": "Google Threat Intelligence Group",
        "published_at": time_value("2026-07-24"),
        "language": "en",
        "source_type": "official-vendor-actor-mapping",
        "tlp": "TLP:CLEAR",
        "reliability": "high",
        "sha256": None,
        "actor_scope": "exact",
        "claims_supported": ["identity", "alias"],
        "analyst_notes": "GTIG's July 30 update supplies the explicit previous-name to new-name table. Exactness applies inside GTIG's taxonomy; other vendors may draw different cluster boundaries.",
    },
    "source--mandiant-fin11-ta505-boundary-2020": {
        "source_id": "source--mandiant-fin11-ta505-boundary-2020",
        "path": "https://cloud.google.com/blog/topics/threat-intelligence/fin11-email-campaigns-precursor-for-ransomware-data-theft",
        "url": "https://cloud.google.com/blog/topics/threat-intelligence/fin11-email-campaigns-precursor-for-ransomware-data-theft",
        "title": "FIN11: Widespread Email Campaigns as Precursor for Ransomware and Data Theft",
        "publisher": "Mandiant",
        "published_at": time_value("2020-10-14"),
        "language": "en",
        "source_type": "vendor-threat-research",
        "tlp": "TLP:CLEAR",
        "reliability": "high",
        "sha256": None,
        "actor_scope": "overlapping",
        "claims_supported": ["identity-boundary", "relationship"],
        "analyst_notes": "Mandiant says FIN11 includes a subset of activity called TA505, excludes early TA505 operations, and cautions against interchangeable use.",
    },
    "source--mandiant-apt38-temp-hermit-boundary-2018": {
        "source_id": "source--mandiant-apt38-temp-hermit-boundary-2018",
        "path": "https://cloud.google.com/blog/topics/threat-intelligence/apt38-details-on-new-north-korean-regime-backed-threat-group/",
        "url": "https://cloud.google.com/blog/topics/threat-intelligence/apt38-details-on-new-north-korean-regime-backed-threat-group/",
        "title": "APT38: Details on New North Korean Regime-Backed Threat Group",
        "publisher": "Mandiant",
        "published_at": time_value("2018-10-03"),
        "language": "en",
        "source_type": "vendor-threat-research",
        "tlp": "TLP:CLEAR",
        "reliability": "high",
        "sha256": None,
        "actor_scope": "overlapping",
        "claims_supported": ["identity-boundary", "relationship"],
        "analyst_notes": "Mandiant describes APT38 activity as disparate from TEMP.Hermit despite shared resources.",
    },
    "source--mitre-attack-ics-19-2": {
        "source_id": "source--mitre-attack-ics-19-2",
        "path": "actor_profile/reference/attack-ics-index.json",
        "url": "https://attack.mitre.org/groups/G1000/",
        "title": "MITRE ICS ATT&CK 19.2 compact local index",
        "publisher": "MITRE",
        "published_at": time_value("2026-08-05"),
        "language": "en",
        "source_type": "structured-knowledge-base",
        "tlp": "TLP:CLEAR",
        "reliability": "high",
        "sha256": None,
        "actor_scope": "exact",
        "claims_supported": ["identity", "alias", "relationship", "ttp"],
        "analyst_notes": "Official MITRE ICS ATT&CK release 19.2 local compact index.",
    },
    "source--cisa-aa23-335a": {
        "source_id": "source--cisa-aa23-335a",
        "path": "International Strategic/Iran/Iranian-Affiliated Cyber Actors Exploit Programmable Logic Controllers Across US Critical Infrastructure.pdf",
        "url": "https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a",
        "title": "IRGC-Affiliated Cyber Actors Exploit PLCs in Multiple Sectors",
        "publisher": "CISA, FBI, NSA, EPA, INCD and NCSC-IL",
        "published_at": time_value("2023-12-01"),
        "language": "en",
        "source_type": "government-advisory",
        "tlp": "TLP:CLEAR",
        "reliability": "high",
        "sha256": None,
        "actor_scope": "exact",
        "claims_supported": ["identity", "alias", "activity", "targeting"],
        "analyst_notes": "The advisory explicitly says private industry and open sources also refer to CyberAv3ngers by the listed names.",
    },
    "source--mitre-attack-g1056": {
        "source_id": "source--mitre-attack-g1056",
        "path": "https://attack.mitre.org/groups/G1056/",
        "url": "https://attack.mitre.org/groups/G1056/",
        "title": "TeamPCP, Group G1056",
        "publisher": "MITRE ATT&CK",
        "published_at": time_value("2026-07-31"),
        "language": "en",
        "source_type": "structured-knowledge-base",
        "tlp": "TLP:CLEAR",
        "reliability": "high",
        "sha256": None,
        "actor_scope": "overlapping",
        "claims_supported": ["identity", "alias"],
        "analyst_notes": "Official ATT&CK Group G1056 associated-group names.",
    },
    "source--mitre-attack-g1057": {
        "source_id": "source--mitre-attack-g1057",
        "path": "https://attack.mitre.org/groups/G1057/",
        "url": "https://attack.mitre.org/groups/G1057/",
        "title": "ShinyHunters, Group G1057",
        "publisher": "MITRE ATT&CK",
        "published_at": time_value("2026-07-31"),
        "language": "en",
        "source_type": "structured-knowledge-base",
        "tlp": "TLP:CLEAR",
        "reliability": "high",
        "sha256": None,
        "actor_scope": "overlapping",
        "claims_supported": ["identity", "alias"],
        "analyst_notes": "Official ATT&CK Group G1057 associated-group names.",
    },
    "source--nsa-blacktech-2023": {
        "source_id": "source--nsa-blacktech-2023",
        "path": "https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/article/3539209/us-and-japanese-agencies-issue-advisory-about-china-linked-actors-hiding-in-rou/",
        "url": "https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/article/3539209/us-and-japanese-agencies-issue-advisory-about-china-linked-actors-hiding-in-rou/",
        "title": "U.S. and Japanese Agencies Issue Advisory about BlackTech",
        "publisher": "NSA",
        "published_at": time_value("2023-09-27"),
        "language": "en",
        "source_type": "government-advisory",
        "tlp": "TLP:CLEAR",
        "reliability": "high",
        "sha256": None,
        "actor_scope": "exact",
        "claims_supported": ["identity", "alias"],
        "analyst_notes": "The joint advisory identifies BlackTech as Palmerworm, TEMP.Overboard, Circuit Panda, and Radio Panda.",
    },
    "source--cert-ua-uac0020-index": {
        "source_id": "source--cert-ua-uac0020-index",
        "path": "actor_profile/reference/osint/cert-ua-uac-index.json",
        "url": "https://cert.gov.ua/article/6281111",
        "title": "CERT-UA UAC-0020 (Vermin) reporting",
        "publisher": "CERT-UA",
        "published_at": unknown_time(),
        "language": "uk",
        "source_type": "government-cert-article-index",
        "tlp": "TLP:CLEAR",
        "reliability": "high",
        "sha256": None,
        "actor_scope": "overlapping",
        "claims_supported": ["identity", "alias"],
        "analyst_notes": "CERT-UA titles identify UAC-0020 as Vermin; GTIG separately tracks TEMP.Vermin and renamed it VERMIN RELIC. The cross-vendor mapping remains overlapping, not exact.",
    },
}


def merge_source(profile: dict[str, Any], source_id: str) -> None:
    source = SOURCES[source_id]
    for index, existing in enumerate(profile["sources"]):
        if existing["source_id"] == source_id:
            profile["sources"][index] = source
            return
    profile["sources"].append(source)


def merge_alias(
    profile: dict[str, Any],
    *,
    name: str,
    vendor: str,
    scope: str,
    confidence: str,
    source_id: str,
    note: str,
) -> None:
    if normalized_name(name) == normalized_name(profile["actor"]["canonical_name"]):
        return
    aliases = profile["actor"]["aliases"]
    existing = next(
        (item for item in aliases if normalized_name(item["name"]) == normalized_name(name)),
        None,
    )
    if existing is None:
        aliases.append(
            {
                "name": name,
                "vendor": vendor,
                "scope": scope,
                "confidence": confidence,
                "evidence_refs": [source_id],
                "analyst_notes": note,
            }
        )
        return
    existing["evidence_refs"] = list(
        dict.fromkeys([*existing.get("evidence_refs", []), source_id])
    )
    if confidence == "high":
        existing["confidence"] = "high"
    if scope == "exact":
        existing["scope"] = "exact"
    if vendor and vendor not in existing.get("vendor", ""):
        existing["vendor"] = " / ".join(x for x in (existing.get("vendor"), vendor) if x)
    if note and note not in existing.get("analyst_notes", ""):
        existing["analyst_notes"] = " ".join(
            x for x in (existing.get("analyst_notes", ""), note) if x
        )


def remove_aliases(profile: dict[str, Any], names: set[str]) -> None:
    blocked = {normalized_name(name) for name in names}
    profile["actor"]["aliases"] = [
        item
        for item in profile["actor"]["aliases"]
        if normalized_name(item["name"]) not in blocked
    ]


def add_relationship(
    left: dict[str, Any],
    right: dict[str, Any],
    *,
    left_slug: str,
    right_slug: str,
    description: str,
    source_id: str,
) -> None:
    relationship_id = (
        f"relationship--{left_slug}--verified-overlap--"
        + stable_digest(left_slug, right_slug, source_id)[:16]
    )
    record = {
        "relationship_id": relationship_id,
        "target_actor": right["actor"]["canonical_name"],
        "relationship_type": "overlaps-with",
        "description": description,
        "confidence": "high",
        "first_observed": unknown_time(),
        "last_observed": unknown_time(),
        "evidence_refs": [source_id],
        "analyst_notes": "Primary-source-verified taxonomy boundary; this relationship must not be converted into an exact alias.",
    }
    left["relationships"] = [
        item
        for item in left.get("relationships", [])
        if item["relationship_id"] != relationship_id
    ] + [record]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=Path("actor_profile/corpus-catalog.json"))
    parser.add_argument("--profiles-root", type=Path, default=Path("profiles"))
    args = parser.parse_args()

    catalog = load_json(args.catalog)
    catalog_by_slug = {item["slug"]: item for item in catalog["actors"]}
    profiles: dict[str, dict[str, Any]] = {}

    def profile(slug: str) -> dict[str, Any]:
        if slug not in profiles:
            profiles[slug] = load_json(args.profiles_root / slug / "actor-profile.json")
        return profiles[slug]

    def catalog_alias(slug: str, name: str) -> None:
        actor = catalog_by_slug[slug]
        if normalized_name(name) == normalized_name(actor["name"]):
            return
        existing = {normalized_name(item) for item in actor.get("aliases", [])}
        if normalized_name(name) not in existing:
            actor.setdefault("aliases", []).append(name)

    gtig_note = (
        "GTIG's July 2026 table explicitly maps the previous name to this new "
        "unified name. Exactness is within GTIG's taxonomy; other vendors may "
        "use different collection boundaries."
    )
    for new_name, (slug, previous_names) in GTIG_MAPPINGS.items():
        current = profile(slug)
        merge_source(current, GTIG_SOURCE_ID)
        scope = "overlapping" if slug == "uac-0020" else "exact"
        alias_source = (
            "source--cert-ua-uac0020-index" if slug == "uac-0020" else GTIG_SOURCE_ID
        )
        if slug == "uac-0020":
            merge_source(current, alias_source)
        merge_alias(
            current,
            name=new_name,
            vendor="Google Threat Intelligence Group",
            scope=scope,
            confidence="high",
            source_id=GTIG_SOURCE_ID,
            note=gtig_note if scope == "exact" else SOURCES[alias_source]["analyst_notes"],
        )
        if slug == "uac-0020":
            merge_alias(
                current,
                name=new_name,
                vendor="CERT-UA / Google Threat Intelligence Group",
                scope="overlapping",
                confidence="high",
                source_id=alias_source,
                note=SOURCES[alias_source]["analyst_notes"],
            )
        catalog_alias(slug, new_name)
        for old_name in previous_names:
            merge_alias(
                current,
                name=old_name,
                vendor="Google Threat Intelligence Group",
                scope=scope,
                confidence="high",
                source_id=alias_source,
                note=gtig_note if scope == "exact" else SOURCES[alias_source]["analyst_notes"],
            )
            catalog_alias(slug, old_name)

    for slug, aliases in MICROSOFT_MAPPINGS.items():
        current = profile(slug)
        for name in aliases:
            merge_alias(
                current,
                name=name,
                vendor="Microsoft",
                scope="overlapping",
                confidence="high",
                source_id=MICROSOFT_SOURCE_ID,
                note="Microsoft's official mapping links this name to the profile identifier; cross-vendor collection boundaries may differ.",
            )
            catalog_alias(slug, name)

    for slug, (group_id, aliases) in MITRE_19_2_MAPPINGS.items():
        current = profile(slug)
        source_id = f"source--mitre-attack-{group_id.casefold()}"
        merge_source(current, source_id)
        catalog_by_slug[slug]["mitre_group_id"] = group_id
        for name in aliases:
            merge_alias(
                current,
                name=name,
                vendor="MITRE ATT&CK",
                scope="overlapping",
                confidence="high",
                source_id=source_id,
                note=f"Official MITRE ATT&CK associated-group name for {group_id}.",
            )
            catalog_alias(slug, name)

    cyber = profile("cyberav3ngers")
    merge_source(cyber, "source--cisa-aa23-335a")
    for name in CYBERAV3NGERS_ALIASES:
        merge_alias(
            cyber,
            name=name,
            vendor="CISA / joint government advisory",
            scope="exact",
            confidence="high",
            source_id="source--cisa-aa23-335a",
            note="The joint advisory explicitly lists this as another name used for CyberAv3ngers.",
        )
        catalog_alias("cyberav3ngers", name)

    blacktech = profile("blacktech")
    merge_source(blacktech, "source--nsa-blacktech-2023")
    for name in BLACKTECH_ALIASES:
        merge_alias(
            blacktech,
            name=name,
            vendor="NSA / joint government advisory",
            scope="exact",
            confidence="high",
            source_id="source--nsa-blacktech-2023",
            note="The joint U.S.-Japan advisory explicitly identifies this name with BlackTech.",
        )
        catalog_alias("blacktech", name)

    white_company = profile("white-company")
    merge_alias(
        white_company,
        name="White Company",
        vendor="MITRE ATT&CK / corpus curation",
        scope="exact",
        confidence="high",
        source_id="source--mitre-attack-19-1",
        note=(
            "The corpus name without the leading article refers to the same "
            "Operation Shaheen actor canonicalized by MITRE as The White Company."
        ),
    )
    catalog_alias("white-company", "White Company")

    for slug, names in BOUNDARY_REMOVALS.items():
        current = profile(slug)
        remove_aliases(current, names)
        blocked = {normalized_name(name) for name in names}
        catalog_by_slug[slug]["aliases"] = [
            name
            for name in catalog_by_slug[slug].get("aliases", [])
            if normalized_name(name) not in blocked
        ]

    boundaries = [
        (
            "fin11",
            "ta505",
            "FIN11 includes a subset of activity publicly called TA505, but early TA505 operations are not attributed to FIN11 and the names are not interchangeable.",
            "source--mandiant-fin11-ta505-boundary-2020",
        ),
        (
            "temp-hermit",
            "apt38",
            "APT38 and TEMP.Hermit have shared resources, but Mandiant describes their activity as disparate and tracks them separately.",
            "source--mandiant-apt38-temp-hermit-boundary-2018",
        ),
        (
            "allanite",
            "dragonfly",
            "ALLANITE has tactics and techniques similar to Dragonfly, but MITRE ATT&CK tracks it as separate Group G1000 with a distinct observed capability boundary.",
            "source--mitre-attack-ics-19-2",
        ),
    ]
    for left_slug, right_slug, description, source_id in boundaries:
        left = profile(left_slug)
        right = profile(right_slug)
        merge_source(left, source_id)
        merge_source(right, source_id)
        for current, target_name in ((left, right["actor"]["canonical_name"]), (right, left["actor"]["canonical_name"])):
            current["relationships"] = [
                item
                for item in current.get("relationships", [])
                if not (
                    normalized_name(item.get("target_actor", "")) == normalized_name(target_name)
                    and "alias-overlap" in item.get("relationship_id", "")
                )
            ]
        add_relationship(left, right, left_slug=left_slug, right_slug=right_slug, description=description, source_id=source_id)
        add_relationship(right, left, left_slug=right_slug, right_slug=left_slug, description=description, source_id=source_id)

    # Remove stale alias-overlap assertions between APT30 and Naikon; the
    # existing ATT&CK narrative relationship remains the authoritative record.
    for slug, target in (("apt30", "Naikon"), ("naikon", "APT30")):
        current = profile(slug)
        current["relationships"] = [
            item
            for item in current.get("relationships", [])
            if not (
                normalized_name(item.get("target_actor", "")) == normalized_name(target)
                and "alias-overlap" in item.get("relationship_id", "")
            )
        ]

    for slug, current in profiles.items():
        current["actor"]["aliases"].sort(key=lambda item: normalized_name(item["name"]))
        current["updated_at"] = utc_now()
        write_json_atomic(args.profiles_root / slug / "actor-profile.json", current)
    for actor in catalog["actors"]:
        actor["aliases"] = sorted(
            dict.fromkeys(actor.get("aliases", [])), key=lambda name: normalized_name(name)
        )
    catalog["actors"].sort(key=lambda item: item["slug"])
    write_json_atomic(args.catalog, catalog)
    print(json.dumps({"profiles_updated": len(profiles), "gtig_mappings": len(GTIG_MAPPINGS), "catalog_actors": len(catalog["actors"])}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
