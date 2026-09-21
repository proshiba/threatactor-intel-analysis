#!/usr/bin/env python3
"""Remove contradicted or lead-only claims from canonical actor profiles.

This is a deterministic migration for the 2026-09 evidence-boundary audit.  It
keeps aggregation/workbook assertions in ``manual-research-leads.json``, fixes
the reviewed APT28/APT29/Calypso records, clears unsupported legacy top-level
Diamond prose, and makes unknown OSINT source metadata explicit.
"""

from __future__ import annotations

import argparse
import copy
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from activity_diamond import materialize_profile_diamonds
from common import load_json, utc_now, write_json_atomic
from enrich_targeting_scope import DATASETS


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
DEFAULT_CATALOG = ROOT / "actor_profile" / "corpus-catalog.json"
DEFAULT_PROFILES = ROOT / "profiles"
DEFAULT_LEADS = ROOT / "actor_profile" / "manual-research-leads.json"

WEAK_PREFIXES = (
    "source--actor-mapping-workbook",
    "source--osint-etda",
    "source--osint-misp",
    "source--target-audit-",
)
LEGACY_DIAMOND_FIELDS = (
    "adversary",
    "capability",
    "infrastructure",
    "victim",
    "socio_political",
)
APT28_BAD_ACTIVITY = "activity--daily-7f3a9417fcc5fd34f701"
APT28_BAD_VICTIM = "victim--activity-rule--00277baa4211a83e77d8"
APT28_BAD_SOURCE = "source--daily-7ba97251f8ecb9b8c790"
APT29_REVERSE_RELATIONSHIPS = {
    "relationship--apt29-unc6293-subcluster",
    "relationship--apt29-unc7005-subcluster",
}
PWC_SOURCE_ID = "source--pwc-red-lamassu-jfmbackdoor-2026"
LUMEN_SOURCE_ID = "source--daily-350d930382dd3ed9f923"
AKAMAI_SOURCE_ID = "source--akamai-apt28-cve-2026-21510"
MICROSOFT_CAPTIVECRUNCH_SOURCE_ID = "source--microsoft-captivecrunch-2026"
REVIEWED_ALIAS_SCOPES = {
    ("teampcp", "PCPCat"): {
        "scope": "overlapping",
        "note": (
            "MITRE ATT&CK lists PCPCat as an Associated Group for G1056. "
            "ATT&CK explicitly treats associated names as overlap signals rather "
            "than exact equivalence, so this alias remains overlapping."
        ),
    },
    ("carberb", "Carberb"): {
        "scope": "exact",
        "note": (
            "Legacy repository spelling retained as an exact lookup variant of "
            "the reviewed canonical name Carberp; confidence remains low because "
            "the misspelling is corpus-local."
        ),
    },
}


def fix_promethium_identity(profile: dict[str, Any]) -> None:
    """Keep the G0056 actor distinct from its same-named StrongPity malware."""
    profile["name"] = "PROMETHIUM"
    actor = profile["actor"]
    actor["canonical_name"] = "PROMETHIUM"
    aliases = [
        item
        for item in actor.get("aliases", [])
        if item.get("name", "").casefold() not in {"promethium", "strongpity"}
    ]
    aliases.append(
        {
            "name": "StrongPity",
            "vendor": "MITRE ATT&CK",
            "scope": "overlapping",
            "confidence": "high",
            "evidence_refs": ["source--mitre-attack-19-2"],
            "analyst_notes": (
                "MITRE ATT&CK lists StrongPity as an Associated Group for G0056, "
                "but also states that the name has been used for both the group and "
                "its malware. It is therefore retained as an overlapping actor name, "
                "not as an exact software-to-actor identity assertion."
            ),
        }
    )
    actor["aliases"] = aliases
    boundary_note = (
        "2026-09 entity-boundary review: G0056 uses PROMETHIUM as the canonical "
        "actor name. StrongPity remains an overlapping historical actor label and "
        "a separate malware entity (S0491)."
    )
    if boundary_note not in actor.get("analyst_notes", ""):
        actor["analyst_notes"] = (
            actor.get("analyst_notes", "").rstrip() + " " + boundary_note
        ).strip()

    for target in profile.get("targets", {}).get("regions", []):
        if isinstance(target.get("description"), str):
            target["description"] = target["description"].replace(
                "StrongPityの標的範囲", "PROMETHIUMの標的範囲"
            )
    summary = profile.get("free_text", {}).get("executive_summary", "")
    if summary.startswith("StrongPityの標準化プロファイル"):
        profile["free_text"]["executive_summary"] = summary.replace(
            "StrongPityの標準化プロファイル",
            "PROMETHIUMの標準化プロファイル",
            1,
        )


def fix_unc7005_relationship(profile: dict[str, Any]) -> None:
    """Record both vendors' stated boundaries for UNC7005/STORM-2945."""
    sources = {item["source_id"]: item for item in profile.get("sources", [])}
    sources[MICROSOFT_CAPTIVECRUNCH_SOURCE_ID] = {
        "source_id": MICROSOFT_CAPTIVECRUNCH_SOURCE_ID,
        "path": (
            "https://www.microsoft.com/en-us/security/blog/2026/07/31/"
            "captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-"
            "malware-delivery-and-credential-theft/"
        ),
        "url": (
            "https://www.microsoft.com/en-us/security/blog/2026/07/31/"
            "captivecrunch-midnight-blizzard-targets-travelers-worldwide-for-"
            "malware-delivery-and-credential-theft/"
        ),
        "title": (
            "CaptiveCrunch: Midnight Blizzard targets travelers worldwide for "
            "malware delivery and credential theft"
        ),
        "publisher": "Microsoft Threat Intelligence",
        "published_at": time_point(
            "2026-07-31T00:00:00Z", "day", "known", "source-stated"
        ),
        "accessed_at": "2026-09-21T00:00:00Z",
        "language": "en",
        "source_type": "vendor-research",
        "tlp": "TLP:CLEAR",
        "reliability": "high",
        "sha256": None,
        "actor_scope": "direct",
        "claims_supported": [
            "identity",
            "relationship",
            "attribution",
            "activity",
            "malware",
            "infrastructure",
            "targeting",
            "ioc",
        ],
        "analyst_notes": (
            "Microsoft directly identifies Storm-2945 as an operational subcluster "
            "of Midnight Blizzard. GTIG separately states that UNC7005 is also known "
            "as STORM-2945, allowing the vendor-scoped relationship evidence to be "
            "joined without collapsing GTIG's distinct cluster boundary."
        ),
    }
    profile["sources"] = list(sources.values())

    relationship = next(
        (
            item
            for item in profile.get("relationships", [])
            if item.get("relationship_id")
            == "relationship--unc7005-ice-relic-connection"
        ),
        None,
    )
    if relationship is None:
        return
    if "MicrosoftはStorm-2945を" not in relationship.get("description", ""):
        relationship["description"] = (
            relationship.get("description", "").rstrip()
            + " MicrosoftはStorm-2945をMidnight Blizzardの運用サブクラスタと"
            "明記している。"
        )
    relationship["evidence_refs"] = list(
        dict.fromkeys(
            [
                *relationship.get("evidence_refs", []),
                MICROSOFT_CAPTIVECRUNCH_SOURCE_ID,
            ]
        )
    )
    relationship["analyst_notes"] = (
        "GTIGはUNC7005をICE RELICに接続する初期アクセスクラスタとしてmoderate "
        "confidenceで評価し、Microsoftは対応するStorm-2945をMidnight Blizzardの"
        "運用サブクラスタと明記する。ベンダー間でクラスタ境界と確度が異なるため、"
        "UNC7005はAPT29へ統合せず、part-of関係に両方の根拠を保持する。"
    )


def replace_record(
    records: list[dict[str, Any]], key: str, record: dict[str, Any]
) -> None:
    existing = next(
        (item for item in records if item.get(key) == record[key]),
        None,
    )
    if key == "activity_id" and existing is not None:
        for generated_key in (
            "target_refs",
            "infrastructure_refs",
            "ttp_refs",
            "victim_refs",
            "diamond_model",
        ):
            if generated_key in existing:
                record[generated_key] = existing[generated_key]
    records[:] = [item for item in records if item.get(key) != record[key]]
    records.append(record)


def add_primary_source(profile: dict[str, Any], source: dict[str, Any]) -> None:
    sources = {item["source_id"]: item for item in profile.get("sources", [])}
    sources[source["source_id"]] = source
    profile["sources"] = list(sources.values())


def fix_invisimole_primary_evidence(profile: dict[str, Any]) -> None:
    source_id = "source--eset-invisimole-hidden-arsenal-2020"
    add_primary_source(
        profile,
        {
            "source_id": source_id,
            "path": "https://www.welivesecurity.com/2020/06/18/digging-up-invisimole-hidden-arsenal/",
            "url": "https://www.welivesecurity.com/2020/06/18/digging-up-invisimole-hidden-arsenal/",
            "archive_url": None,
            "title": "Digging up InvisiMole's hidden arsenal",
            "publisher": "ESET Research",
            "published_at": time_point(
                "2020-06-18T00:00:00Z", "day", "known", "document"
            ),
            "accessed_at": "2026-09-21T00:00:00Z",
            "language": "en",
            "source_type": "vendor-research",
            "tlp": "TLP:CLEAR",
            "reliability": "high",
            "sha256": None,
            "actor_scope": "direct",
            "claims_supported": [
                "identity",
                "activity",
                "relationship",
                "malware",
                "targeting",
                "motivation",
                "ttp",
            ],
            "analyst_notes": (
                "ESET directly distinguishes the InvisiMole group from its "
                "same-named malware and from Gamaredon, based on victim-side "
                "investigation and telemetry."
            ),
        },
    )
    actor = profile["actor"]
    actor["first_seen"] = time_point(
        "2013-01-01T00:00:00Z", "year", "known", "source-stated"
    )
    actor["last_seen"] = time_point(
        "2020-06-18T00:00:00Z", "day", "known", "source-observed"
    )
    actor["description"] = (
        "InvisiMoleはESETが追跡するサイバースパイ活動グループで、少なくとも2013年から"
        "活動している。同名のInvisiMoleマルウェアは同グループのツールであり、"
        "アクター自体と同一のソフトウェア実体ではない。"
    )
    note = (
        "2026-09 entity-boundary review: ESET explicitly treats InvisiMole as a "
        "group and its same-named espionage toolkit as malware."
    )
    if note not in actor.get("analyst_notes", ""):
        actor["analyst_notes"] = (actor.get("analyst_notes", "").rstrip() + " " + note).strip()
    profile["attribution"]["analyst_notes"] = (
        "The reviewed ESET source does not identify a sponsoring state or operator "
        "organization; attribution remains unknown."
    )
    replace_record(
        profile["motivations"],
        "type",
        {
            "type": "espionage",
            "description": (
                "ESET explicitly describes InvisiMole as a cyber-espionage group "
                "and documents extensive spying capabilities."
            ),
            "confidence": "high",
            "evidence_refs": [source_id],
            "analyst_notes": "Motivation is source-stated, not inferred from geography.",
        },
    )
    replace_record(
        profile["capabilities"]["malware"],
        "id",
        {
            "id": "malware--invisimole",
            "name": "InvisiMole",
            "aliases": [],
            "types": ["Windows", "modular-spyware"],
            "description": (
                "同名グループが使用するモジュール型スパイウェア。RC2CLとRC2FMの"
                "バックドア、更新版のTCP/DNSダウンローダーを含む。"
            ),
            "first_observed": time_point(
                "2013-01-01T00:00:00Z", "year", "known", "source-stated"
            ),
            "last_observed": time_point(
                "2020-06-18T00:00:00Z", "day", "known", "source-observed"
            ),
            "confidence": "high",
            "evidence_refs": [source_id],
            "analyst_notes": (
                "The software label is intentionally separate from actor--invisimole."
            ),
        },
    )
    activity_id = "activity--invisimole-eastern-europe-2019-2020"
    replace_record(
        profile["activities"],
        "activity_id",
        {
            "activity_id": activity_id,
            "name": "InvisiMoleによる東欧の軍事・外交組織へのスパイ活動",
            "activity_type": "cyber-espionage",
            "stix_object_type": "campaign",
            "grouping_context": None,
            "activity_refs": [],
            "first_observed": time_point(
                "2019-10-01T00:00:00Z", "month", "known", "source-stated"
            ),
            "last_observed": time_point(
                "2020-06-18T00:00:00Z", "day", "known", "source-observed"
            ),
            "reported_at": time_point(
                "2020-06-18T00:00:00Z", "day", "known", "document"
            ),
            "description": (
                "ESETは2019年後半から2020年6月18日の報告時点まで、東欧の少数の"
                "高位組織、特に軍事部門と政府・行政に属する外交使節団を標的とする攻撃を観測した。"
                "Gamaredonが先に侵入した端末の一部へ、より選別的にInvisiMoleを配布した。"
            ),
            "target_refs": [],
            "malware_refs": ["malware--invisimole"],
            "infrastructure_refs": [],
            "ttp_refs": [],
            "victim_refs": [],
            "confidence": "high",
            "evidence_refs": [source_id],
            "analyst_notes": (
                "The October start is a month-precision proxy for the source "
                "phrase 'late 2019'; it is not an exact start date."
            ),
        },
    )
    replace_record(
        profile["relationships"],
        "relationship_id",
        {
            "relationship_id": "relationship--invisimole--gamaredon-delivery",
            "target_actor": "actor--gamaredon",
            "relationship_type": "cooperates-with",
            "description": (
                "ESET observed Gamaredon malware establishing initial access and "
                "delivering InvisiMole to a small, selected subset of targets. "
                "ESET explicitly treats the two as distinct groups with different TTPs."
            ),
            "confidence": "high",
            "first_observed": time_point(
                "2019-10-01T00:00:00Z", "month", "known", "source-stated"
            ),
            "last_observed": time_point(
                "2020-06-18T00:00:00Z", "day", "known", "source-observed"
            ),
            "evidence_refs": [source_id],
            "analyst_notes": (
                "Delivery cooperation does not establish exact identity or a part-of relationship."
            ),
        },
    )
    profile["free_text"]["executive_summary"] = (
        "InvisiMoleは少なくとも2013年から活動するサイバースパイ集団で、2019年後半から"
        "2020年に東欧の軍事・外交組織を標的化した。Gamaredonによる初期侵入後に"
        "同名のモジュール型スパイウェアを選別配布する協力関係が確認されている。"
    )


def fix_konni_primary_evidence(profile: dict[str, Any]) -> None:
    source_id = "source--unit42-fractured-statue-2020"
    add_primary_source(
        profile,
        {
            "source_id": source_id,
            "path": "https://unit42.paloaltonetworks.com/the-fractured-statue-campaign-u-s-government-targeted-in-spear-phishing-attacks/",
            "url": "https://unit42.paloaltonetworks.com/the-fractured-statue-campaign-u-s-government-targeted-in-spear-phishing-attacks/",
            "archive_url": None,
            "title": "The Fractured Statue Campaign: U.S. Government Agency Targeted in Spear-Phishing Attacks",
            "publisher": "Palo Alto Networks Unit 42",
            "published_at": time_point(
                "2020-01-23T00:00:00Z", "day", "known", "document"
            ),
            "accessed_at": "2026-09-21T00:00:00Z",
            "language": "en",
            "source_type": "vendor-research",
            "tlp": "TLP:CLEAR",
            "reliability": "high",
            "sha256": None,
            "actor_scope": "direct",
            "claims_supported": [
                "identity",
                "activity",
                "malware",
                "targeting",
                "motivation",
                "attribution",
            ],
            "analyst_notes": (
                "Unit 42 explicitly explains the overloaded Konni label: it began "
                "as a RAT name and is also used for a broader activity group."
            ),
        },
    )
    actor = profile["actor"]
    actor["first_seen"] = time_point(
        "2014-01-01T00:00:00Z", "year", "known", "source-stated"
    )
    actor["description"] = (
        "Konni Groupは、同名のKONNI RATを使用した活動から命名された活動集合である。"
        "Unit 42は、KONNI RATを使わないもののTTPが強く重なる作戦も含め、"
        "アクター側をKonni Groupとして追跡している。"
    )
    note = (
        "2026-09 entity-boundary review: Konni is retained as an actor label, while "
        "KONNI is separately modeled as malware. Unit 42 cautions that public TTP "
        "reporting creates copycat and false-flag attribution risk."
    )
    if note not in actor.get("analyst_notes", ""):
        actor["analyst_notes"] = (actor.get("analyst_notes", "").rstrip() + " " + note).strip()
    profile["attribution"]["analyst_notes"] = (
        "North Korea-themed targeting and links to North Korean interests do not by "
        "themselves establish a sponsoring state; sponsor attribution remains unknown."
    )
    replace_record(
        profile["motivations"],
        "type",
        {
            "type": "espionage",
            "description": (
                "Unit 42 describes sustained information-stealing campaigns and "
                "targeting of government and North Korea-linked individuals."
            ),
            "confidence": "medium",
            "evidence_refs": [source_id],
            "analyst_notes": "The operational objective is explicit; state sponsorship is not inferred.",
        },
    )
    malware_records = [
        ("malware--konni", "KONNI", "2014-01-01T00:00:00Z", "2017-12-31T00:00:00Z", "remote-access-trojan"),
        ("malware--nokki", "NOKKI", "2018-01-01T00:00:00Z", None, "malware"),
        ("malware--carrotbat", "CARROTBAT", "2018-01-01T00:00:00Z", "2019-10-31T00:00:00Z", "downloader"),
        ("malware--carrotball", "CARROTBALL", "2019-10-01T00:00:00Z", "2019-10-31T00:00:00Z", "downloader"),
        ("malware--syscon", "SYSCON", "2019-07-01T00:00:00Z", "2019-10-31T00:00:00Z", "remote-access-trojan"),
    ]
    for malware_id, name, first, last, kind in malware_records:
        replace_record(
            profile["capabilities"]["malware"],
            "id",
            {
                "id": malware_id,
                "name": name,
                "aliases": [],
                "types": ["Windows", kind],
                "description": (
                    f"Unit 42がKonni Groupの活動で確認した{name}マルウェア。"
                ),
                "first_observed": time_point(
                    first, "year" if first.endswith("01-01T00:00:00Z") else "month", "known", "source-stated"
                ),
                "last_observed": time_point(
                    last,
                    (
                        "unknown"
                        if last is None
                        else "year"
                        if last.endswith("12-31T00:00:00Z")
                        else "month"
                    ),
                    "known" if last else "unknown",
                    "source-stated" if last else "not-stated",
                ),
                "confidence": "medium" if name in {"KONNI", "NOKKI"} else "high",
                "evidence_refs": [source_id],
                "analyst_notes": (
                    "The malware entity is distinct from the Konni Group actor label."
                    if name == "KONNI"
                    else "Observation dates are limited to the periods stated in this source."
                ),
            },
        )
    profile["capabilities"]["malware"].sort(
        key=lambda item: item.get("name", "").casefold()
    )
    replace_record(
        profile["activities"],
        "activity_id",
        {
            "activity_id": "activity--konni-fractured-statue-2019",
            "name": "Fractured Statueキャンペーン",
            "activity_type": "phishing-campaign",
            "stix_object_type": "campaign",
            "grouping_context": None,
            "activity_refs": [],
            "first_observed": time_point(
                "2019-07-01T00:00:00Z", "month", "known", "source-stated"
            ),
            "last_observed": time_point(
                "2019-10-31T00:00:00Z", "month", "known", "source-stated"
            ),
            "reported_at": time_point(
                "2020-01-23T00:00:00Z", "day", "known", "document"
            ),
            "description": (
                "Unit 42は2019年7月から10月、米国政府機関と朝鮮半島情勢に職業上関係する"
                "米国外の外国人を標的としたスピアフィッシングを観測した。ロシア語の朝鮮半島情勢"
                "を題材に、CARROTBATまたはCARROTBALLからSYSCONを配布した。"
            ),
            "target_refs": [],
            "malware_refs": [
                "malware--carrotbat",
                "malware--carrotball",
                "malware--syscon",
            ],
            "infrastructure_refs": [],
            "ttp_refs": [],
            "victim_refs": [],
            "confidence": "medium",
            "evidence_refs": [source_id],
            "analyst_notes": (
                "Unit 42 assesses the Konni Group link with moderate confidence "
                "because public TTP details could enable copycat or false-flag activity."
            ),
        },
    )
    profile["free_text"]["executive_summary"] = (
        "Konni Groupは同名RATに由来する活動集合で、2014年以降の情報窃取作戦と、"
        "KONNI、NOKKI、CARROTBAT、CARROTBALL、SYSCON等の利用が報告されている。"
        "アクター名とマルウェア名を分離し、個別作戦の帰属確度を保持する。"
    )


def fix_nettraveler_primary_evidence(profile: dict[str, Any]) -> None:
    source_id = "source--kaspersky-nettraveler-2013"
    relation_source_id = "source--kaspersky-q2-2016-danti"
    add_primary_source(
        profile,
        {
            "source_id": source_id,
            "path": "https://securelist.com/nettraveler-is-running-red-star-apt-attacks-compromise-high-profile-victims/35936/",
            "url": "https://securelist.com/nettraveler-is-running-red-star-apt-attacks-compromise-high-profile-victims/35936/",
            "archive_url": None,
            "title": "NetTraveler is Running! - Red Star APT Attacks Compromise High-Profile Victims",
            "publisher": "Kaspersky Global Research and Analysis Team",
            "published_at": time_point(
                "2013-06-04T00:00:00Z", "day", "known", "document"
            ),
            "accessed_at": "2026-09-21T00:00:00Z",
            "language": "en",
            "source_type": "vendor-research",
            "tlp": "TLP:CLEAR",
            "reliability": "high",
            "sha256": None,
            "actor_scope": "direct",
            "claims_supported": [
                "identity",
                "activity",
                "malware",
                "targeting",
                "motivation",
                "attribution",
                "ttp",
            ],
            "analyst_notes": (
                "Kaspersky uses NetTraveler for both the operator group/campaign and "
                "the principal malware/toolkit; the two entities are modeled separately."
            ),
        },
    )
    add_primary_source(
        profile,
        {
            "source_id": relation_source_id,
            "path": "https://securelist.com/it-threat-evolution-in-q2-2016-overview/75615/",
            "url": "https://securelist.com/it-threat-evolution-in-q2-2016-overview/75615/",
            "archive_url": None,
            "title": "IT threat evolution in Q2 2016. Overview",
            "publisher": "Kaspersky",
            "published_at": time_point(
                "2016-08-11T00:00:00Z", "day", "known", "document"
            ),
            "accessed_at": "2026-09-21T00:00:00Z",
            "language": "en",
            "source_type": "vendor-research",
            "tlp": "TLP:CLEAR",
            "reliability": "high",
            "sha256": None,
            "actor_scope": "overlapping",
            "claims_supported": ["relationship", "attribution"],
            "analyst_notes": (
                "Kaspersky expresses only a suspected connection between Danti and "
                "the separately tracked NetTraveler and DragonOK groups."
            ),
        },
    )
    actor = profile["actor"]
    actor["first_seen"] = time_point(
        "2004-01-01T00:00:00Z", "year", "known", "source-stated"
    )
    actor["last_seen"] = time_point(
        "2013-06-04T00:00:00Z", "day", "known", "source-observed"
    )
    actor["description"] = (
        "NetTravelerはKasperskyが追跡した大規模サイバースパイ活動集合で、少なくとも"
        "2004年から活動し、40か国で350件超の高位標的を侵害した。同名のNetTraveler"
        "ツールキットは主要マルウェアであり、アクター実体とは分離して記録する。"
    )
    note = (
        "2026-09 entity-boundary review: public reporting overloads NetTraveler as "
        "both a group/campaign label and a malware/toolkit name; this profile models "
        "the operator cluster and keeps malware--nettraveler separate."
    )
    if note not in actor.get("analyst_notes", ""):
        actor["analyst_notes"] = (actor.get("analyst_notes", "").rstrip() + " " + note).strip()
    profile["attribution"]["analyst_notes"] = (
        "Kaspersky observed that most operators appeared to be native Chinese speakers, "
        "but language does not establish country of origin, state control, or sponsorship."
    )
    replace_record(
        profile["motivations"],
        "type",
        {
            "type": "espionage",
            "description": (
                "Kaspersky explicitly describes the activity as cyber espionage and "
                "documents theft of sensitive technical and government information."
            ),
            "confidence": "high",
            "evidence_refs": [source_id],
            "analyst_notes": "Motivation is source-stated; sponsorship remains unknown.",
        },
    )
    replace_record(
        profile["capabilities"]["malware"],
        "id",
        {
            "id": "malware--nettraveler",
            "name": "NetTraveler",
            "aliases": ["Travnet", "Netfile"],
            "types": ["Windows", "information-stealer", "backdoor"],
            "description": (
                "NetTravelerグループが監視、キーロギング、ファイル窃取、追加マルウェア"
                "導入に使用した同名ツールキット。"
            ),
            "first_observed": time_point(
                "2005-01-01T00:00:00Z", "year", "known", "sample-timestamp"
            ),
            "last_observed": time_point(
                "2013-06-04T00:00:00Z", "day", "known", "source-observed"
            ),
            "confidence": "high",
            "evidence_refs": [source_id],
            "analyst_notes": (
                "The source notes references to 2004 activity but the earliest known "
                "sample timestamps are from 2005."
            ),
        },
    )
    for cve in ("CVE-2010-3333", "CVE-2012-0158"):
        replace_record(
            profile["capabilities"]["vulnerabilities"],
            "id",
            {
                "id": f"vulnerability--{cve.casefold()}",
                "name": cve,
                "description": (
                    "Patched Microsoft Office vulnerability used in malicious "
                    "spearphishing attachments during NetTraveler operations."
                ),
                "first_observed": time_point(
                    None, "unknown", "unknown", "not-stated"
                ),
                "last_observed": time_point(
                    "2013-06-04T00:00:00Z", "day", "known", "source-observed"
                ),
                "confidence": "high",
                "evidence_refs": [source_id],
                "analyst_notes": "The source does not state the first use date.",
            },
        )
    replace_record(
        profile["activities"],
        "activity_id",
        {
            "activity_id": "activity--nettraveler-red-star-2004-2013",
            "name": "NetTraveler／Red Starサイバースパイ活動",
            "activity_type": "cyber-espionage",
            "stix_object_type": "campaign",
            "grouping_context": None,
            "activity_refs": [],
            "first_observed": time_point(
                "2004-01-01T00:00:00Z", "year", "known", "source-stated"
            ),
            "last_observed": time_point(
                "2013-06-04T00:00:00Z", "day", "known", "source-observed"
            ),
            "reported_at": time_point(
                "2013-06-04T00:00:00Z", "day", "known", "document"
            ),
            "description": (
                "Kasperskyは、モンゴル、ロシア、インド、カザフスタン、キルギス、中国、"
                "タジキスタン、韓国、スペイン、ドイツ、米国、カナダ、英国、チリ、"
                "モロッコ、ギリシャ、ベルギー、オーストリア、ウクライナ、リトアニア、"
                "ベラルーシ、オーストラリア、香港、日本、イラン、トルコ、パキスタン、"
                "タイ、カタール、ヨルダンを含む40か国で侵害を確認した。標的は政府機関、"
                "大使館、石油・ガス、研究機関、大学、防衛・軍事請負企業、活動家等で、"
                "NetTravelerマルウェアを用いて機微情報を窃取した。"
            ),
            "target_refs": [],
            "malware_refs": ["malware--nettraveler"],
            "infrastructure_refs": [],
            "ttp_refs": [],
            "victim_refs": [],
            "confidence": "high",
            "evidence_refs": [source_id],
            "analyst_notes": (
                "Country names are explicit victim locations in the source; the list "
                "does not imply attribution or sponsorship."
            ),
        },
    )
    replace_record(
        profile["relationships"],
        "relationship_id",
        {
            "relationship_id": "relationship--nettraveler--danti-suspected",
            "target_actor": "actor--danti",
            "relationship_type": "related-to",
            "description": (
                "KasperskyはDantiの起源を不明とした上で、NetTravelerおよびDragonOKとの"
                "接続可能性を疑っていると記述した。"
            ),
            "confidence": "low",
            "first_observed": time_point(
                None, "unknown", "unknown", "not-stated"
            ),
            "last_observed": time_point(
                "2016-08-11T00:00:00Z", "day", "known", "source-assessment"
            ),
            "evidence_refs": [relation_source_id],
            "analyst_notes": (
                "This is a vendor-stated suspicion, not proof of shared operators "
                "or exact identity. Publication date records the assessment date only."
            ),
        },
    )
    profile["free_text"]["executive_summary"] = (
        "NetTravelerは少なくとも2004年から2013年にかけて40か国・350件超の高位標的を"
        "侵害したサイバースパイ活動集合である。同名ツールキットを別マルウェア実体として"
        "記録し、Dantiとの関係はKasperskyの低確度な接続疑義に限定する。"
    )


def time_point(
    value: str | None,
    precision: str = "unknown",
    status: str = "unknown",
    basis: str = "not-stated",
) -> dict[str, Any]:
    return {
        "value": value,
        "precision": precision,
        "status": status,
        "basis": basis,
    }


def weak_ref(ref: str) -> bool:
    return ref.startswith(WEAK_PREFIXES)


def weak_only(refs: list[str]) -> bool:
    return bool(refs) and all(weak_ref(ref) for ref in refs)


def strip_weak_refs(item: dict[str, Any]) -> int:
    refs = item.get("evidence_refs", [])
    retained = [ref for ref in refs if not weak_ref(ref)]
    if refs == retained:
        return 0
    item["evidence_refs"] = retained
    return len(refs) - len(retained)


def evidence_refs(value: Any) -> set[str]:
    refs: set[str] = set()
    if isinstance(value, dict):
        refs.update(str(item) for item in value.get("evidence_refs", []) if item)
        for key, nested in value.items():
            if key != "sources":
                refs.update(evidence_refs(nested))
    elif isinstance(value, list):
        for nested in value:
            refs.update(evidence_refs(nested))
    return refs


def source_claim_categories(profile: dict[str, Any]) -> dict[str, set[str]]:
    categories: dict[str, set[str]] = defaultdict(set)
    sections = {
        "actor": "identity",
        "attribution": "attribution",
        "motivations": "motivation",
        "relationships": "relationship",
        "capabilities": "capability",
        "activities": "activity",
        "victim_cases": "victim-case",
        "targets": "targeting",
        "ttps": "ttp",
        "assessment": "assessment",
    }
    for section, category in sections.items():
        for ref in evidence_refs(profile.get(section)):
            categories[ref].add(category)
    return categories


def add_uncertainty(profile: dict[str, Any], text: str) -> None:
    values = profile.setdefault("assessment", {}).setdefault("uncertainties", [])
    if text not in values:
        values.append(text)


def append_manual_lead(
    manual: dict[str, Any], slug: str, category: str, item: dict[str, Any]
) -> None:
    items = manual.setdefault("actors", {}).setdefault(slug, {}).setdefault(category, [])
    key = json.dumps(item, ensure_ascii=False, sort_keys=True)
    if all(json.dumps(existing, ensure_ascii=False, sort_keys=True) != key for existing in items):
        items.append(item)


def append_target_lead(
    manual: dict[str, Any], slug: str, category: str, item: dict[str, Any]
) -> None:
    items = (
        manual.setdefault("actors", {})
        .setdefault(slug, {})
        .setdefault("targets", {})
        .setdefault(category, [])
    )
    key = json.dumps(item, ensure_ascii=False, sort_keys=True)
    if all(json.dumps(existing, ensure_ascii=False, sort_keys=True) != key for existing in items):
        items.append(item)


def append_capability_lead(
    manual: dict[str, Any], slug: str, category: str, item: dict[str, Any]
) -> None:
    items = (
        manual.setdefault("actors", {})
        .setdefault(slug, {})
        .setdefault("capabilities", {})
        .setdefault(category, [])
    )
    key = json.dumps(item, ensure_ascii=False, sort_keys=True)
    if all(json.dumps(existing, ensure_ascii=False, sort_keys=True) != key for existing in items):
        items.append(item)


def ensure_manual_lead_sources(
    profile: dict[str, Any], actor_leads: dict[str, Any]
) -> int:
    required = evidence_refs(actor_leads)
    sources = {source["source_id"]: source for source in profile.get("sources", [])}
    added = 0
    for spec in DATASETS.values():
        source_id = spec["source_id"]
        if source_id in required and source_id not in sources:
            sources[source_id] = copy.deepcopy(spec["source"])
            added += 1
    profile["sources"] = list(sources.values())
    return added


def fix_apt28(profile: dict[str, Any]) -> None:
    activity = next(
        (
            item
            for item in profile.get("activities", [])
            if item.get("activity_id") == APT28_BAD_ACTIVITY
        ),
        None,
    )
    if activity:
        activity.update(
            {
                "name": "APT28によるCVE-2026-21510／CVE-2026-21513悪用活動",
                "activity_type": "cyber-espionage",
                "first_observed": time_point(
                    "2025-12-01T00:00:00Z", "month", "known", "source-stated"
                ),
                "last_observed": time_point(
                    "2026-01-31T00:00:00Z", "month", "known", "source-observed"
                ),
                "description": (
                    "CERT-UAによればAPT28は2025年12月、ウクライナおよび複数のEU諸国を"
                    "標的に、細工したLNKファイル内でCVE-2026-21513とCVE-2026-21510を"
                    "組み合わせ、SmartScreen等を回避してリモートDLLを実行した。Akamaiは"
                    "このAPT28エクスプロイトを2026年1月に検知した。後続のCVE-2026-32202は"
                    "不完全な修正から生じた別脆弱性であり、MicrosoftはAPT28との関連証拠を"
                    "確認していない。"
                ),
                "confidence": "high",
                "evidence_refs": [AKAMAI_SOURCE_ID, APT28_BAD_SOURCE],
                "analyst_notes": (
                    "APT28への帰属範囲はCVE-2026-21510/CVE-2026-21513に限定。"
                    "CVE-2026-32202の悪用主体へは拡張しない。活動期間と報告日を分離した。"
                ),
            }
        )
    for victim in profile.get("victim_cases", []):
        if (
            victim.get("victim_case_id") != APT28_BAD_VICTIM
            and APT28_BAD_ACTIVITY not in victim.get("activity_refs", [])
        ):
            continue
        victim.update(
            {
                "name": "被害事例: APT28によるCVE-2026-21510／CVE-2026-21513悪用活動",
                "victim_name": None,
                "disclosure_status": "aggregate",
                "victim_type": "multiple-organizations",
                "case_status": "reported",
                "description": activity["description"] if activity else victim.get("description", ""),
                "activity_refs": [APT28_BAD_ACTIVITY],
                "first_observed": time_point(
                    "2025-12-01T00:00:00Z", "month", "known", "source-stated"
                ),
                "last_observed": time_point(
                    "2026-01-31T00:00:00Z", "month", "known", "source-observed"
                ),
                "confidence": "high",
                "evidence_refs": [AKAMAI_SOURCE_ID, APT28_BAD_SOURCE],
            }
        )
    vulnerabilities = profile.setdefault("capabilities", {}).setdefault(
        "vulnerabilities", []
    )
    vulnerabilities = [
        item
        for item in vulnerabilities
        if item.get("id") != "vulnerability--cve-2026-32202"
    ]
    if not any(item.get("id") == "vulnerability--cve-2026-21510" for item in vulnerabilities):
        vulnerabilities.append(
            {
                "id": "vulnerability--cve-2026-21510",
                "name": "CVE-2026-21510",
                "description": (
                    "Windows Shell security-feature bypass used with CVE-2026-21513 "
                    "in a weaponized LNK exploitation chain."
                ),
                "first_observed": time_point(
                    "2025-12-01T00:00:00Z", "month", "known", "source-stated"
                ),
                "last_observed": time_point(
                    "2026-01-31T00:00:00Z", "month", "known", "source-observed"
                ),
                "confidence": "high",
                "evidence_refs": [AKAMAI_SOURCE_ID],
                "analyst_notes": "Akamai observed the APT28 exploit and documents its scope.",
            }
        )
    profile["capabilities"]["vulnerabilities"] = vulnerabilities
    sources = {source["source_id"]: source for source in profile.get("sources", [])}
    sources[AKAMAI_SOURCE_ID] = {
        "source_id": AKAMAI_SOURCE_ID,
        "path": "https://www.akamai.com/blog/security-research/incomplete-patch-apt28s-zero-day-cve-2026-32202",
        "url": "https://www.akamai.com/blog/security-research/incomplete-patch-apt28s-zero-day-cve-2026-32202",
        "title": "A Shortcut to Coercion: Incomplete Patch of APT28's Zero-Day Leads to CVE-2026-32202",
        "publisher": "Akamai Security Research",
        "published_at": time_point(
            "2026-04-23T00:00:00Z", "day", "known", "source-published-date"
        ),
        "accessed_at": "2026-09-21T00:00:00Z",
        "language": "en",
        "source_type": "vendor-technical-report",
        "tlp": "TLP:CLEAR",
        "reliability": "high",
        "sha256": None,
        "actor_scope": "exact",
        "claims_supported": ["activity", "targeting", "vulnerability"],
        "analyst_notes": (
            "Akamai distinguishes the APT28 exploitation of CVE-2026-21510/21513 "
            "from the later incomplete-patch vulnerability CVE-2026-32202."
        ),
    }
    profile["sources"] = list(sources.values())
    add_uncertainty(
        profile,
        "CVE-2026-32202はAPT28へ帰属しない。Microsoftは2026-04-30時点で同CVEをAPT28に結び付ける証拠を確認しておらず、APT28が2025-12に悪用したのはCVE-2026-21510である。",
    )


def capability(
    capability_id: str,
    name: str,
    description: str,
    first: dict[str, Any],
    last: dict[str, Any],
    refs: list[str],
) -> dict[str, Any]:
    return {
        "id": capability_id,
        "name": name,
        "description": description,
        "first_observed": first,
        "last_observed": last,
        "confidence": "high",
        "evidence_refs": refs,
        "analyst_notes": "PwC/Lumenの2026年5月共同公開資料からactor scopeと利用文脈を確認。",
    }


def fix_calypso(profile: dict[str, Any]) -> None:
    profile["actor"]["first_seen"] = time_point(
        "2019-01-01T00:00:00Z", "year", "known", "source-stated"
    )
    profile["actor"]["last_seen"] = time_point(
        "2026-05-12T00:00:00Z", "day", "known", "source-stated-infrastructure-observation"
    )
    profile["actor"]["active"] = "yes"
    profile["actor"]["description"] = (
        "Calypso is a China-based cyberespionage cluster tracked by Positive "
        "Technologies and by PwC as Red Lamassu. PwC has tracked the actor since "
        "2019 targeting telecommunications and government entities in Asia."
    )
    for alias in profile["actor"].get("aliases", []):
        if alias.get("name") == "Red Lamassu":
            alias.update(
                {
                    "vendor": "PwC Threat Intelligence",
                    "scope": "exact",
                    "confidence": "high",
                    "evidence_refs": [PWC_SOURCE_ID],
                    "analyst_notes": "PwC explicitly calls Red Lamassu a.k.a. Calypso.",
                }
            )
    profile["attribution"] = {
        "countries": ["China"],
        "sponsor_type": "unknown",
        "organizations": [],
        "assessment": (
            "PwC describes Red Lamassu (Calypso) as a China-based threat actor, "
            "likely operating from Sichuan Province. This does not establish state sponsorship."
        ),
        "confidence": "high",
        "evidence_refs": [PWC_SOURCE_ID],
        "analyst_notes": "Geographic attribution is kept separate from sponsorship.",
    }
    profile["motivations"] = [
        {
            "type": "espionage",
            "description": (
                "PwC states that Red Lamassu uses persistent access for long-term "
                "intelligence collection."
            ),
            "confidence": "high",
            "evidence_refs": [PWC_SOURCE_ID],
            "analyst_notes": "Actor-specific vendor reporting; not inferred from geography.",
        }
    ]
    profile["diamond_model"] = {
        "adversary": "",
        "capability": "",
        "infrastructure": "",
        "victim": "",
        "socio_political": "",
        "analyst_notes": "Use evidence-linked activity-level Diamond models.",
    }
    showboat = capability(
        "malware--showboat",
        "Showboat",
        "Modular Linux post-exploitation framework with remote shell, file-transfer, process-hiding, persistence, and SOCKS5 proxy functions.",
        time_point("2022-01-01T00:00:00Z", "year", "known", "source-stated-at-least-mid-year"),
        time_point("2026-04-01T00:00:00Z", "month", "known", "source-stated"),
        [LUMEN_SOURCE_ID, PWC_SOURCE_ID],
    )
    jfm = capability(
        "malware--jfmbackdoor",
        "JFMBackdoor",
        "Windows backdoor delivered through DLL side-loading with shell, file, proxy, screenshot, service, registry, and self-removal functions.",
        time_point("2025-07-01T00:00:00Z", "month", "known", "source-stated-range"),
        time_point("2025-10-01T00:00:00Z", "month", "known", "source-stated-range"),
        [PWC_SOURCE_ID],
    )
    profile["capabilities"]["malware"] = [showboat, jfm]
    activity = next(
        (
            item
            for item in profile.get("activities", [])
            if item.get("activity_id") == "activity--daily-651f2178af4ab3c90c96"
        ),
        None,
    )
    if activity:
        activity.update(
            {
                "name": "Red LamassuによるShowboat／JFMBackdoor通信事業者侵入活動",
                "activity_type": "cyber-espionage",
                "first_observed": time_point(
                    "2022-01-01T00:00:00Z",
                    "year",
                    "known",
                    "source-stated-at-least-mid-year",
                ),
                "last_observed": time_point(
                    "2026-04-01T00:00:00Z", "month", "known", "source-stated"
                ),
                "reported_at": time_point(
                    "2026-05-21T00:00:00Z", "day", "known", "source-published-date"
                ),
                "description": (
                    "PwCはRed Lamassu（別名Calypso）を追跡し、アジアの通信・政府組織を"
                    "標的にしていると報告した。PwCが確認した"
                    "2025年7月から10月の公開ディレクトリには、Windowsバックドア"
                    "JFMBackdoorと、LumenがShowboatと命名したLinuxマルウェアが共存した。"
                    "LumenはShowboat関連活動を少なくとも2022年半ばから追跡し、"
                    "アフガニスタンとアゼルバイジャンの被害通信を確認した。"
                ),
                "malware_refs": ["malware--jfmbackdoor", "malware--showboat"],
                "confidence": "high",
                "evidence_refs": [LUMEN_SOURCE_ID, PWC_SOURCE_ID],
                "analyst_notes": (
                    "Lumen単独では固有アクター名を断定していないため、Calypso/Red Lamassuの"
                    "actor scopeは共同公開されたPwC原文で確認。公開日と活動観測期間を分離した。"
                ),
            }
        )
    profile["free_text"]["executive_summary"] = (
        "PwCとLumenの一次資料でRed Lamassu（Calypso）の通信事業者標的活動と"
        "Showboat／JFMBackdoorの利用を確認したプロファイル。"
    )
    # Preserve the deterministic structured-targeting summary produced by
    # enrich_targeting_scope.py.  Other legacy prose on this profile came from
    # the contaminated workbook mapping and must not survive the migration.
    profile["free_text"]["targeting_details"] = "\n".join(
        line
        for line in profile["free_text"].get("targeting_details", "").splitlines()
        if line.startswith("構造化ターゲット監査:")
    )
    profile["free_text"]["capability_details"] = ""
    profile["assessment"]["key_judgments"] = [
        {
            "statement": (
                "Calypso is retained as a separate espionage cluster; PwC explicitly "
                "uses Red Lamassu as an alternate name, while Bronze Medley remains an aggregation lead."
            ),
            "confidence": "high",
            "evidence_refs": [PWC_SOURCE_ID],
            "analyst_notes": "APT1/Comment Crew, Mirage, and Pitty Tiger are not aliases.",
        }
    ]
    profile["assessment"]["gaps"] = [
        "Bronze Medley equivalence still requires the original SecureWorks source.",
        "State sponsorship remains unknown.",
    ]
    sources = {source["source_id"]: source for source in profile.get("sources", [])}
    sources[LUMEN_SOURCE_ID] = {
        **sources.get(LUMEN_SOURCE_ID, {}),
        "source_id": LUMEN_SOURCE_ID,
        "path": "https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms",
        "url": "https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms",
        "title": "Introducing Showboat: A new malware family taunts defenses and targets international telecom firms",
        "publisher": "Lumen Black Lotus Labs",
        "published_at": time_point(
            "2026-05-21T00:00:00Z", "day", "known", "source-published-date"
        ),
        "accessed_at": "2026-09-21T00:00:00Z",
        "language": "en",
        "source_type": "vendor-technical-report",
        "tlp": "TLP:CLEAR",
        "reliability": "high",
        "sha256": None,
        "actor_scope": "unnamed-prc-aligned-clusters",
        "claims_supported": ["activity", "malware", "targeting", "infrastructure"],
        "analyst_notes": (
            "Lumen reports the Showboat cluster and collaboration with PwC but does not "
            "independently name Calypso/Red Lamassu; actor identity is supported by PwC."
        ),
    }
    sources[PWC_SOURCE_ID] = {
        "source_id": PWC_SOURCE_ID,
        "path": "https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/red-lamassu-open-season.html",
        "url": "https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/red-lamassu-open-season.html",
        "title": "Open Directory, Open Season: Inside Red Lamassu's JFMBackdoor",
        "publisher": "PwC Threat Intelligence",
        "published_at": time_point(
            "2026-05-21T00:00:00Z", "day", "known", "source-published-date"
        ),
        "accessed_at": "2026-09-21T00:00:00Z",
        "language": "en",
        "source_type": "vendor-technical-report",
        "tlp": "TLP:CLEAR",
        "reliability": "high",
        "sha256": None,
        "actor_scope": "exact",
        "claims_supported": [
            "identity",
            "alias",
            "attribution",
            "motivation",
            "activity",
            "malware",
            "targeting",
            "infrastructure",
        ],
        "analyst_notes": (
            "PwC explicitly identifies Red Lamassu as Calypso and documents the "
            "JFMBackdoor/Showboat-linked intrusion infrastructure."
        ),
    }
    profile["sources"] = list(sources.values())


def clear_legacy_diamond(profile: dict[str, Any]) -> bool:
    diamond = profile.get("diamond_model", {})
    changed = any(diamond.get(field) for field in LEGACY_DIAMOND_FIELDS)
    for field in LEGACY_DIAMOND_FIELDS:
        diamond[field] = ""
    diamond["analyst_notes"] = (
        "Legacy source-unbound prose was cleared in the 2026-09 evidence audit; "
        "use evidence-linked activity-level Diamond models."
    )
    return changed


def normalize_web_source_metadata(profile: dict[str, Any]) -> int:
    categories = source_claim_categories(profile)
    changed = 0
    for source in profile.get("sources", []):
        path = source.get("url") or source.get("path", "")
        if not isinstance(path, str) or not path.startswith(("http://", "https://")):
            continue
        before = json.dumps(source, ensure_ascii=False, sort_keys=True)
        source.setdefault("url", path)
        source.setdefault("accessed_at", None)
        source.setdefault("actor_scope", "unknown")
        source.setdefault(
            "claims_supported",
            sorted(categories.get(source.get("source_id", ""), {"profile-source"})),
        )
        if source.get("accessed_at") is None:
            note = (
                "Legacy source metadata: the original retrieval timestamp is unavailable; "
                "accessed_at is explicitly null rather than inferred."
            )
            if note not in source.get("analyst_notes", ""):
                source["analyst_notes"] = (
                    source.get("analyst_notes", "").rstrip() + " " + note
                ).strip()
        changed += before != json.dumps(source, ensure_ascii=False, sort_keys=True)
    return changed


def fix_reviewed_alias_scopes(slug: str, profile: dict[str, Any]) -> int:
    changed = 0
    for alias in profile.get("actor", {}).get("aliases", []):
        review = REVIEWED_ALIAS_SCOPES.get((slug, alias.get("name")))
        if review is None:
            continue
        before = json.dumps(alias, ensure_ascii=False, sort_keys=True)
        alias["scope"] = review["scope"]
        alias["analyst_notes"] = review["note"]
        changed += before != json.dumps(alias, ensure_ascii=False, sort_keys=True)

    if slug == "teampcp":
        old_gap = "PCPCatとTeamPCPの対応関係が一次資料で説明されていない。"
        new_gap = (
            "MITRE ATT&CKはPCPCatをTeamPCPのAssociated Groupとして関連付けるが、"
            "exact equivalenceまでは表明していない。"
        )
        gaps = profile.get("assessment", {}).get("gaps", [])
        profile.get("assessment", {})["gaps"] = [
            new_gap if item == old_gap else item for item in gaps
        ]

    if slug == "carberb":
        curation_source_id = "source--actor-census-curation-carberp"
        sources = {
            item["source_id"]: item for item in profile.get("sources", [])
        }
        sources[curation_source_id] = {
            "source_id": curation_source_id,
            "path": "actor_profile/actor-census-curation.json",
            "title": "Analyst-reviewed Carberp identity curation",
            "publisher": "threatactor-intel-analysis maintainers",
            "published_at": time_point(None),
            "language": "en",
            "source_type": "analyst-curation",
            "tlp": "TLP:CLEAR",
            "reliability": "high",
            "sha256": None,
            "actor_scope": "exact",
            "claims_supported": ["identity", "alias"],
            "analyst_notes": (
                "Records the reviewed normalization of the corpus-local spelling "
                "Carberb to the actor-specific canonical name Carberp."
            ),
        }
        profile["sources"] = list(sources.values())
        for alias in profile.get("actor", {}).get("aliases", []):
            if alias.get("name") == "Carberb":
                alias["evidence_refs"] = [curation_source_id]
        source = next(
            (
                item
                for item in profile.get("sources", [])
                if item.get("source_id") == "source--group-ib-carberp-gang"
            ),
            None,
        )
        if source:
            before = json.dumps(source, ensure_ascii=False, sort_keys=True)
            source["actor_scope"] = "exact"
            source["claims_supported"] = [
                "identity",
                "attribution",
                "motivation",
                "activity",
                "targeting",
                "malware",
                "assessment",
            ]
            changed += before != json.dumps(source, ensure_ascii=False, sort_keys=True)
    return changed


def remove_entity_refs(
    profile: dict[str, Any], removed_activities: set[str], removed_malware: set[str]
) -> None:
    for activity in profile.get("activities", []):
        activity["malware_refs"] = [
            ref for ref in activity.get("malware_refs", []) if ref not in removed_malware
        ]
    for ttp in profile.get("ttps", []):
        ttp["activity_refs"] = [
            ref for ref in ttp.get("activity_refs", []) if ref not in removed_activities
        ]
        ttp["malware_refs"] = [
            ref for ref in ttp.get("malware_refs", []) if ref not in removed_malware
        ]
    for victim in profile.get("victim_cases", []):
        victim["activity_refs"] = [
            ref for ref in victim.get("activity_refs", []) if ref not in removed_activities
        ]
        victim["malware_refs"] = [
            ref for ref in victim.get("malware_refs", []) if ref not in removed_malware
        ]


def migrate_profile(
    slug: str, profile: dict[str, Any], manual: dict[str, Any]
) -> dict[str, int]:
    stats = defaultdict(int)
    if slug == "apt28":
        fix_apt28(profile)
        stats["apt28"] += 1
    if slug == "apt29":
        before = len(profile.get("relationships", []))
        profile["relationships"] = [
            item
            for item in profile.get("relationships", [])
            if item.get("relationship_id") not in APT29_REVERSE_RELATIONSHIPS
        ]
        stats["apt29_reverse_relationships"] += before - len(profile["relationships"])
    if slug == "calypso":
        fix_calypso(profile)
        stats["calypso"] += 1
    if slug == "strongpity":
        fix_promethium_identity(profile)
        stats["promethium_identity"] += 1
    if slug == "unc7005":
        fix_unc7005_relationship(profile)
        stats["unc7005_relationship"] += 1
    if slug == "invisimole":
        fix_invisimole_primary_evidence(profile)
        stats["invisimole_primary_evidence"] += 1
    if slug == "konni":
        fix_konni_primary_evidence(profile)
        stats["konni_primary_evidence"] += 1
    if slug == "nettraveler":
        fix_nettraveler_primary_evidence(profile)
        stats["nettraveler_primary_evidence"] += 1
    stats["reviewed_alias_scopes"] += fix_reviewed_alias_scopes(slug, profile)

    kept_aliases = []
    moved_aliases = 0
    for item in profile.get("actor", {}).get("aliases", []):
        if weak_only(item.get("evidence_refs", [])):
            lead = copy.deepcopy(item)
            lead["verification_status"] = "unresolved"
            lead["analyst_notes"] = (
                lead.get("analyst_notes", "").rstrip()
                + " Moved from canonical because only aggregation/workbook evidence exists."
            ).strip()
            append_manual_lead(manual, slug, "aliases", lead)
            stats["aliases"] += 1
            moved_aliases += 1
        else:
            stats["weak_refs_stripped"] += strip_weak_refs(item)
            kept_aliases.append(item)
    profile["actor"]["aliases"] = kept_aliases
    if moved_aliases:
        add_uncertainty(
            profile,
            f"{moved_aliases} alias lead(s) remain non-canonical pending original-source review.",
        )

    kept_activities = []
    removed_activities: set[str] = set()
    for item in profile.get("activities", []):
        if weak_only(item.get("evidence_refs", [])):
            lead = copy.deepcopy(item)
            lead["verification_status"] = "unresolved"
            lead["analyst_notes"] = (
                lead.get("analyst_notes", "").rstrip()
                + " Moved from canonical because only aggregation/workbook evidence exists."
            ).strip()
            append_manual_lead(manual, slug, "activities", lead)
            removed_activities.add(item["activity_id"])
            stats["activities"] += 1
        else:
            stats["weak_refs_stripped"] += strip_weak_refs(item)
            kept_activities.append(item)
    profile["activities"] = kept_activities

    removed_malware: set[str] = set()
    for category in (
        "malware",
        "tools",
        "infrastructure",
        "delivery_formats",
        "vulnerabilities",
        "operational_capabilities",
    ):
        retained = []
        for item in profile.get("capabilities", {}).get(category, []):
            if weak_only(item.get("evidence_refs", [])):
                lead = copy.deepcopy(item)
                lead["verification_status"] = "unresolved"
                lead["analyst_notes"] = (
                    lead.get("analyst_notes", "").rstrip()
                    + " Moved from canonical because only aggregation/workbook evidence exists."
                ).strip()
                append_capability_lead(manual, slug, category, lead)
                if category == "malware":
                    removed_malware.add(item["id"])
                stats["capabilities"] += 1
            else:
                stats["weak_refs_stripped"] += strip_weak_refs(item)
                retained.append(item)
        profile["capabilities"][category] = retained

    remove_entity_refs(profile, removed_activities, removed_malware)

    kept_motivations = []
    for item in profile.get("motivations", []):
        if weak_only(item.get("evidence_refs", [])):
            lead = copy.deepcopy(item)
            lead["value"] = lead.pop("type", "unknown")
            lead["verification_status"] = "unresolved"
            lead["analyst_notes"] = (
                lead.get("analyst_notes", "").rstrip()
                + " Migrated from canonical because only aggregation/workbook evidence exists."
            ).strip()
            append_manual_lead(manual, slug, "motivations", lead)
            add_uncertainty(
                profile,
                f"Motivation lead '{lead['value']}' is not canonical; only aggregation/workbook evidence is available.",
            )
            stats["motivations"] += 1
        else:
            stats["weak_refs_stripped"] += strip_weak_refs(item)
            kept_motivations.append(item)
    profile["motivations"] = kept_motivations

    kept_relationships = []
    for item in profile.get("relationships", []):
        if weak_only(item.get("evidence_refs", [])):
            lead = copy.deepcopy(item)
            lead["verification_status"] = "unresolved"
            lead["analyst_notes"] = (
                lead.get("analyst_notes", "").rstrip()
                + " Migrated from canonical because only aggregation/workbook evidence exists."
            ).strip()
            append_manual_lead(manual, slug, "relationships", lead)
            stats["relationships"] += 1
        else:
            stats["weak_refs_stripped"] += strip_weak_refs(item)
            kept_relationships.append(item)
    profile["relationships"] = kept_relationships

    attribution = profile.get("attribution", {})
    if weak_only(attribution.get("evidence_refs", [])):
        lead = copy.deepcopy(attribution)
        lead["verification_status"] = "unresolved"
        lead["analyst_notes"] = (
            lead.get("analyst_notes", "").rstrip()
            + " Migrated from canonical because only aggregation/workbook evidence exists."
        ).strip()
        append_manual_lead(manual, slug, "attribution", lead)
        profile["attribution"] = {
            "countries": [],
            "sponsor_type": "unknown",
            "organizations": [],
            "assessment": "Attribution remains unknown pending original-source review.",
            "confidence": "unknown",
            "evidence_refs": [],
            "analyst_notes": "Aggregation/workbook-only attribution was moved to research leads.",
        }
        stats["attribution"] += 1
    else:
        stats["weak_refs_stripped"] += strip_weak_refs(attribution)

    targets = profile.get("targets", {})
    for category in ("countries", "regions", "sectors", "roles"):
        retained = []
        for item in targets.get(category, []):
            if weak_only(item.get("evidence_refs", [])):
                lead = copy.deepcopy(item)
                lead["value"] = lead.pop("name", "unknown")
                lead["verification_status"] = "unresolved"
                lead["analyst_notes"] = (
                    lead.get("analyst_notes", "").rstrip()
                    + " Migrated from canonical because only aggregation/workbook evidence exists."
                ).strip()
                append_target_lead(manual, slug, category, lead)
                stats["targets"] += 1
            else:
                stats["weak_refs_stripped"] += strip_weak_refs(item)
                retained.append(item)
        targets[category] = retained

    kept_judgments = []
    for item in profile.get("assessment", {}).get("key_judgments", []):
        if weak_only(item.get("evidence_refs", [])):
            lead = copy.deepcopy(item)
            lead["verification_status"] = "unresolved"
            lead["analyst_notes"] = (
                lead.get("analyst_notes", "").rstrip()
                + " Moved from canonical because only aggregation/workbook evidence exists."
            ).strip()
            append_manual_lead(manual, slug, "assessment", lead)
            stats["assessment"] += 1
        else:
            stats["weak_refs_stripped"] += strip_weak_refs(item)
            kept_judgments.append(item)
    profile["assessment"]["key_judgments"] = kept_judgments

    stats["legacy_diamond"] += clear_legacy_diamond(profile)
    stats["source_metadata"] += normalize_web_source_metadata(profile)
    materialize_profile_diamonds(profile)
    return dict(stats)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--profiles-root", type=Path, default=DEFAULT_PROFILES)
    parser.add_argument("--manual-leads", type=Path, default=DEFAULT_LEADS)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    catalog = load_json(args.catalog)
    manual = (
        load_json(args.manual_leads)
        if args.manual_leads.exists()
        else {"schema_version": "1.0.0", "actors": {}}
    )
    totals: dict[str, int] = defaultdict(int)
    changed = 0
    catalog_slugs = {actor["slug"] for actor in catalog["actors"]}
    profile_paths = sorted(args.profiles_root.glob("*/actor-profile.json"))
    for path in profile_paths:
        slug = path.parent.name
        profile = load_json(path)
        before = json.dumps(profile, ensure_ascii=False, sort_keys=True)
        for key, value in migrate_profile(slug, profile, manual).items():
            totals[key] += value
        totals["manual_lead_sources"] += ensure_manual_lead_sources(
            profile, manual.get("actors", {}).get(slug, {})
        )
        after = json.dumps(profile, ensure_ascii=False, sort_keys=True)
        if before == after:
            continue
        changed += 1
        if args.apply:
            profile["updated_at"] = utc_now()
            write_json_atomic(path, profile)

    if args.apply:
        manual["generated_at"] = utc_now()
        manual["catalog_actor_count"] = len(catalog_slugs)
        manual["profile_count"] = len(profile_paths)
        write_json_atomic(args.manual_leads, manual)
    print(json.dumps({"mode": "apply" if args.apply else "dry-run", "profiles_changed": changed, **totals}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
