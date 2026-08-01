#!/usr/bin/env python3
"""Apply reviewed attribution corrections and Meta 2021 campaign evidence."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from common import normalize_time, stable_id, unknown_time, utc_now, write_json_atomic
from activity_diamond import materialize_profile_diamonds


PROFILES_ROOT = Path("profiles")
META_SOURCE_ID = "source--meta-syria-hackers-2021"
META_URL = (
    "https://about.fb.com/news/2021/11/"
    "taking-action-against-hackers-in-pakistan-and-syria/"
)


def source(
    source_id: str,
    url: str,
    title: str,
    publisher: str,
    published_at: str,
    notes: str,
    *,
    source_type: str = "vendor-research",
) -> dict[str, Any]:
    return {
        "source_id": source_id,
        "path": url,
        "url": url,
        "title": title,
        "publisher": publisher,
        "published_at": normalize_time(published_at, basis="document"),
        "accessed_at": "2026-07-25T00:00:00Z",
        "language": "en",
        "source_type": source_type,
        "tlp": "TLP:CLEAR",
        "reliability": "high",
        "sha256": None,
        "actor_scope": "overlapping",
        "claims_supported": [
            "attribution",
            "relationship",
            "activity",
            "malware",
            "infrastructure",
            "targeting",
            "ioc",
        ],
        "analyst_notes": notes,
    }


META_SOURCE = source(
    META_SOURCE_ID,
    META_URL,
    "Taking Action Against Hackers in Pakistan and Syria",
    "Meta",
    "2021-11-16",
    (
        "Meta directly observed and disrupted separate Syrian networks. It maps "
        "SEA/APT-C-27 and APT-C-37 to different units linked to Syria's Air "
        "Force Intelligence and publishes campaign indicators."
    ),
)

CFR_SOURCE_ID = "source--cfr-taiwan-offensive-cyber-2022"
CFR_SOURCE = source(
    CFR_SOURCE_ID,
    (
        "https://www.cfr.org/articles/"
        "taiwans-offensive-cyber-capabilities-and-ramifications-taiwan-china-conflict"
    ),
    "Taiwan's Offensive Cyber Capabilities and Ramifications for a Taiwan-China Conflict",
    "Council on Foreign Relations",
    "2022-12-07",
    (
        "CFR summarizes public reporting that attributes Green Spot / "
        "PoisonVine / APT-C-01 to Taiwan. The underlying attribution originated "
        "with Chinese security vendors and therefore remains estimative."
    ),
    source_type="policy-research",
)


def append_unique(items: list[Any], value: Any, key: str) -> None:
    identity = str(value.get(key))
    for index, item in enumerate(items):
        if isinstance(item, dict) and str(item.get(key)) == identity:
            items[index] = value
            return
    items.append(value)


def capability(
    item_id: str,
    name: str,
    types: list[str],
    description: str,
    source_id: str,
    *,
    aliases: list[str] | None = None,
    first: str | None = None,
    last: str | None = None,
) -> dict[str, Any]:
    return {
        "id": item_id,
        "name": name,
        "aliases": aliases or [],
        "types": types,
        "description": description,
        "first_observed": (
            normalize_time(first, basis="source-stated") if first else unknown_time()
        ),
        "last_observed": (
            normalize_time(last, basis="source-stated") if last else unknown_time()
        ),
        "confidence": "high",
        "evidence_refs": [source_id],
        "analyst_notes": "",
    }


def target(
    item_id: str,
    name: str,
    description: str,
    source_id: str,
    *,
    first: str | None = None,
    last: str | None = None,
    confidence: str = "high",
) -> dict[str, Any]:
    return {
        "id": item_id,
        "name": name,
        "description": description,
        "first_observed": (
            normalize_time(first, basis="source-stated") if first else unknown_time()
        ),
        "last_observed": (
            normalize_time(last, basis="source-stated") if last else unknown_time()
        ),
        "confidence": confidence,
        "evidence_refs": [source_id],
        "analyst_notes": "",
    }


def meta_activity(actor_name: str, description: str, target_refs: list[str]) -> dict[str, Any]:
    return {
        "activity_id": "activity--meta-syria-disruption-2021",
        "name": "Meta Syrian network disruption (October 2021)",
        "activity_type": "cyber-espionage",
        "first_observed": normalize_time("2021-10", basis="source-stated"),
        "last_observed": normalize_time("2021-10", basis="source-stated"),
        "reported_at": normalize_time("2021-11-16", basis="document"),
        "description": f"{actor_name}: {description}",
        "target_refs": target_refs,
        "malware_refs": [],
        "infrastructure_refs": [],
        "ttp_refs": [],
        "victim_refs": [],
        "confidence": "high",
        "evidence_refs": [META_SOURCE_ID],
        "analyst_notes": (
            "The date is the disruption month stated by Meta, not a first-seen "
            "date for the actor or every listed indicator."
        ),
    }


def add_meta_manifest(slug: str, malware_refs: list[str]) -> None:
    path = PROFILES_ROOT / slug / "ioc-sources.json"
    manifest = json.loads(path.read_text(encoding="utf-8"))
    excerpt = f"actor_profile/osint/excerpts/meta-2021-{slug}-iocs.csv"
    source_item = {
        "source_id": META_SOURCE_ID,
        "path": excerpt,
        "published_at": normalize_time("2021-11-16", basis="document"),
        "campaign_refs": ["activity--meta-syria-disruption-2021"],
        "malware_refs": malware_refs,
        "infrastructure_refs": [],
        "roles": [],
        "confidence": "high",
        "tlp": "TLP:CLEAR",
        "allow_plain_domains": True,
        "field_map": {
            "type": "type",
            "value": "value",
            "observed_at": "observed_at",
            "campaign_refs": "campaign_refs",
            "malware_refs": "malware_refs",
            "infrastructure_refs": "infrastructure_refs",
            "roles": "roles",
        },
        "analyst_notes": (
            "Actor-scoped transcription of the indicator table in the Meta "
            "report. Observation month is the stated disruption month unless "
            "the row identifies an earlier year."
        ),
    }
    existing = {item["source_id"] for item in manifest["sources"]}
    if META_SOURCE_ID not in existing:
        manifest["sources"].append(source_item)
    else:
        manifest["sources"] = [
            source_item if item["source_id"] == META_SOURCE_ID else item
            for item in manifest["sources"]
        ]
    write_json_atomic(path, manifest)


def correct_apt_c_01() -> None:
    path = PROFILES_ROOT / "apt-c-01" / "actor-profile.json"
    profile = json.loads(path.read_text(encoding="utf-8"))
    append_unique(profile["sources"], CFR_SOURCE, "source_id")
    local_report_ref = "source--apt-c-01--c225ad868f45dc7c"
    profile["attribution"] = {
        "countries": ["Taiwan"],
        "sponsor_type": "state",
        "organizations": [
            {
                "id": "org--taiwan-icefcom",
                "name": "Information Communication Electronic Force Command",
                "relationship": "claimed-subordinate-to",
                "confidence": "medium",
                "evidence_refs": [CFR_SOURCE_ID, local_report_ref],
                "analyst_notes": (
                    "This organizational link is asserted in Chinese public "
                    "reporting and has not been publicly confirmed by Taiwan."
                ),
            }
        ],
        "assessment": (
            "Public reporting places Green Spot / PoisonVine / APT-C-01 in "
            "Taiwan and describes targeting of Chinese government, military, "
            "aviation, research, and maritime entities. Exact state command is "
            "not independently confirmed."
        ),
        "confidence": "medium",
        "evidence_refs": [CFR_SOURCE_ID, local_report_ref],
        "analyst_notes": (
            "Supersedes the workbook-only China attribution. The principal "
            "technical attribution claims originate with Chinese vendors and "
            "government-linked reporting, so geopolitical source bias is material."
        ),
    }
    judgment = {
        "statement": (
            "The previous China attribution was a worksheet-placement artifact; "
            "available OSINT instead associates APT-C-01 with Taiwan."
        ),
        "confidence": "medium",
        "evidence_refs": [CFR_SOURCE_ID, local_report_ref],
        "analyst_notes": (
            "Counterevidence review: no independent source supporting a China-"
            "sponsored APT-C-01 cluster was found in the fixed datasets."
        ),
    }
    append_unique(profile["assessment"]["key_judgments"], judgment, "statement")
    uncertainty = (
        "Taiwan/ICEF command claims rely substantially on sources from the PRC; "
        "treat sponsor and unit-level attribution as estimative."
    )
    if uncertainty not in profile["assessment"]["uncertainties"]:
        profile["assessment"]["uncertainties"].append(uncertainty)
    append_unique(
        profile["targets"]["countries"],
        target(
            "target--country--china",
            "China",
            "Primary geographic target in the reviewed public reporting.",
            CFR_SOURCE_ID,
            confidence="medium",
        ),
        "id",
    )
    for sector_name in (
        "Government",
        "Defense",
        "Aviation",
        "Education and Research",
        "Maritime",
    ):
        sector_id = "target--sector--" + sector_name.lower().replace(" ", "-")
        append_unique(
            profile["targets"]["sectors"],
            target(
                sector_id,
                sector_name,
                f"Public reporting identifies {sector_name} entities as targets.",
                CFR_SOURCE_ID,
                confidence="medium",
            ),
            "id",
        )
    profile["targets"]["selection_logic"] = (
        "Entities holding Chinese government, defense, aviation, maritime, and "
        "cross-Strait policy information."
    )
    profile["updated_at"] = utc_now()
    write_json_atomic(path, profile)


def correct_syrian_actor(slug: str) -> None:
    path = PROFILES_ROOT / slug / "actor-profile.json"
    profile = json.loads(path.read_text(encoding="utf-8"))
    append_unique(profile["sources"], META_SOURCE, "source_id")
    actor_name = profile["name"]
    is_27 = slug == "apt-c-27"
    relationship = (
        "subsumed-into"
        if is_27
        else "linked-to-separate-unit-within"
    )
    profile["attribution"] = {
        "countries": ["Syria"],
        "sponsor_type": "state",
        "organizations": [
            {
                "id": "org--syria-air-force-intelligence",
                "name": "Syrian Air Force Intelligence",
                "relationship": relationship,
                "confidence": "high",
                "evidence_refs": [META_SOURCE_ID],
                "analyst_notes": (
                    "Meta observed the 2021 activity and distinguishes the units "
                    "associated with APT-C-27 and APT-C-37."
                ),
            }
        ],
        "assessment": (
            "Meta linked the observed 2021 network to Syria's Air Force "
            "Intelligence."
        ),
        "confidence": "high",
        "evidence_refs": [META_SOURCE_ID],
        "analyst_notes": (
            "Supersedes the workbook-only China attribution. Meta distinguishes "
            "APT-C-27/SEA from APT-C-37 as separate Syrian networks."
        ),
    }
    judgment = {
        "statement": (
            f"The previous China attribution for {actor_name} is contradicted by "
            "direct Meta observations linking the activity to Syrian Air Force "
            "Intelligence."
        ),
        "confidence": "high",
        "evidence_refs": [META_SOURCE_ID],
        "analyst_notes": (
            "The old assertion depended only on worksheet placement and is "
            "retained as superseded counterevidence in the claim audit."
        ),
    }
    append_unique(profile["assessment"]["key_judgments"], judgment, "statement")
    role_names = {
        "humanitarian organizations",
        "journalists",
        "activists",
        "military opposition",
    }
    if not is_27:
        role_names = {"Free Syrian Army-linked persons", "former military personnel"}
    append_unique(
        profile["targets"]["countries"],
        target(
            "target--country--syria",
            "Syria",
            "Meta observed targeting of people and organizations in Syria.",
            META_SOURCE_ID,
            first="2021-10",
            last="2021-10",
        ),
        "id",
    )
    for sector_name in ("Government", "Defense", "Civil Society"):
        append_unique(
            profile["targets"]["sectors"],
            target(
                "target--sector--" + sector_name.lower().replace(" ", "-"),
                sector_name,
                f"Meta's observed victim set included {sector_name} targets.",
                META_SOURCE_ID,
                first="2021-10",
                last="2021-10",
            ),
            "id",
        )
    for role_name in sorted(role_names):
        role_id = "target--role--" + re.sub(r"[^a-z0-9]+", "-", role_name.lower()).strip("-")
        append_unique(
            profile["targets"]["roles"],
            target(
                role_id,
                role_name,
                f"Meta identified {role_name} in the observed victim set.",
                META_SOURCE_ID,
                first="2021-10",
                last="2021-10",
            ),
            "id",
        )
    profile["targets"]["selection_logic"] = (
        "Syrian civil-society, media, humanitarian, opposition, and former "
        "military targets holding politically or militarily relevant information."
    )

    if is_27:
        append_unique(
            profile["capabilities"]["malware"],
            capability(
                "malware--silverhawk",
                "SilverHawk",
                ["android-spyware"],
                "Custom Android malware also called HmzaRAT.",
                META_SOURCE_ID,
                aliases=["HmzaRAT"],
                last="2021-10",
            ),
            "id",
        )
        append_unique(
            profile["capabilities"]["malware"],
            capability(
                "malware--meta-unnamed-android-2021",
                "Unnamed Android family (Meta 2021)",
                ["android-spyware"],
                "Previously unnamed Android malware distributed in trojanized Telegram and Syrian news applications.",
                META_SOURCE_ID,
                last="2021-10",
            ),
            "id",
        )
        activity_description = (
            "Meta disrupted SEA/APT-C-27 accounts and infrastructure linked to "
            "Syrian Air Force Intelligence. The actor used credential phishing "
            "and trojanized Android applications."
        )
        malware_refs = [
            "malware--silverhawk",
            "malware--meta-unnamed-android-2021",
        ]
    else:
        append_unique(
            profile["capabilities"]["malware"],
            capability(
                "malware--sslove",
                "SSLove",
                ["android-spyware"],
                "Likely in-house Android malware distributed as a fake WhatsApp application.",
                META_SOURCE_ID,
                last="2021-10",
            ),
            "id",
        )
        append_unique(
            profile["capabilities"]["malware"],
            capability(
                "malware--sandrorat",
                "SandroRAT",
                ["android-rat"],
                "Commodity Android remote-access malware used in the observed campaign.",
                META_SOURCE_ID,
                last="2021-10",
            ),
            "id",
        )
        activity_description = (
            "Meta disrupted APT-C-37 infrastructure linked to a separate Syrian "
            "Air Force Intelligence unit. The actor used credential phishing, "
            "SandroRAT, and SSLove against opposition-linked targets."
        )
        malware_refs = ["malware--sslove", "malware--sandrorat"]
    activity = meta_activity(
        actor_name,
        activity_description,
        ["target--country--syria"],
    )
    activity["malware_refs"] = malware_refs
    if is_27:
        infrastructure_items = [
            capability(
                "infra--meta-apt-c-27-phishing",
                "APT-C-27 credential phishing infrastructure",
                ["phishing-infrastructure"],
                "Blogspot-hosted credential phishing pages reported by Meta.",
                META_SOURCE_ID,
                last="2021-10",
            ),
            capability(
                "infra--meta-apt-c-27-delivery",
                "APT-C-27 Android malware delivery infrastructure",
                ["malware-distribution"],
                "Compromised and cloud-hosted sites used to distribute Android malware.",
                META_SOURCE_ID,
                first="2020",
                last="2021-10",
            ),
            capability(
                "infra--meta-apt-c-27-c2",
                "APT-C-27 command-and-control infrastructure",
                ["command-and-control"],
                "Server used for C2 and Android malware distribution.",
                META_SOURCE_ID,
                last="2021-10",
            ),
        ]
    else:
        infrastructure_items = [
            capability(
                "infra--meta-apt-c-37-c2",
                "APT-C-37 command-and-control infrastructure",
                ["command-and-control"],
                "Long-running C2 server reported by Meta.",
                META_SOURCE_ID,
                last="2021-10",
            )
        ]
    for infrastructure in infrastructure_items:
        append_unique(
            profile["capabilities"]["infrastructure"],
            infrastructure,
            "id",
        )
    activity["infrastructure_refs"] = [
        item["id"] for item in infrastructure_items
    ]
    append_unique(profile["activities"], activity, "activity_id")
    relation = {
        "relationship_id": stable_id(
            "relationship", slug, "distinct-from", "apt-c-37" if is_27 else "apt-c-27"
        ),
        "target_actor": "APT-C-37" if is_27 else "APT-C-27",
        "relationship_type": "distinct-from",
        "description": (
            "Meta reported the two clusters as separate Syrian networks linked "
            "to different units within Syria's Air Force Intelligence."
        ),
        "confidence": "high",
        "first_observed": normalize_time("2021-10", basis="source-stated"),
        "last_observed": normalize_time("2021-10", basis="source-stated"),
        "evidence_refs": [META_SOURCE_ID],
        "analyst_notes": (
            "Shared national sponsor and similar targeting do not establish "
            "actor identity."
        ),
    }
    append_unique(profile["relationships"], relation, "relationship_id")
    materialize_profile_diamonds(profile)
    profile["updated_at"] = utc_now()
    write_json_atomic(path, profile)
    add_meta_manifest(slug, malware_refs)


def main() -> int:
    correct_apt_c_01()
    correct_syrian_actor("apt-c-27")
    correct_syrian_actor("apt-c-37")
    tracker_path = PROFILES_ROOT / "osint-progress.json"
    tracker = json.loads(tracker_path.read_text(encoding="utf-8"))
    for item in tracker["actors"]:
        if item["slug"] not in {"apt-c-01", "apt-c-27", "apt-c-37"}:
            continue
        item["status"] = "integrated"
        claim_id = f"attribution-correction--{item['slug']}"
        if claim_id not in item["claims_integrated"]:
            item["claims_integrated"].append(claim_id)
        item["last_searched_at"] = utc_now()
    tracker["updated_at"] = utc_now()
    write_json_atomic(tracker_path, tracker)
    print(
        json.dumps(
            {
                "updated_profiles": ["apt-c-01", "apt-c-27", "apt-c-37"],
                "meta_ioc_manifests": ["apt-c-27", "apt-c-37"],
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
