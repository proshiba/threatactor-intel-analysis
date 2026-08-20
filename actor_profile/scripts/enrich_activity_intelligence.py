#!/usr/bin/env python3
"""Enrich profiles with activity-linked ATT&CK, targets, malware, and victim cases.

The script has two evidence-preserving inputs:

* MITRE ATT&CK campaign relationships and procedure examples.
* Explicit behavior and targeting phrases already present in reviewed activities.

Publication/report dates are never copied into observation dates.
"""

from __future__ import annotations

import argparse
import copy
import json
import re
from pathlib import Path
from typing import Any, Iterable

from common import (
    load_json,
    stable_digest,
    unknown_time,
    utc_now,
    write_json_atomic,
)
from activity_diamond import materialize_profile_diamonds


HERE = Path(__file__).resolve().parent
FRAMEWORK_ROOT = HERE.parent
REPO_ROOT = FRAMEWORK_ROOT.parent
DEFAULT_RULES = FRAMEWORK_ROOT / "activity-observation-rules.json"
DEFAULT_ATTACK = FRAMEWORK_ROOT / "reference" / "attack-index.json"
DEFAULT_CATALOG = FRAMEWORK_ROOT / "corpus-catalog.json"
DEFAULT_PROFILES = REPO_ROOT / "profiles"
MITRE_SOURCE_ID = "source--mitre-attack-19-1"
GENERATED_TTP_PREFIXES = ("ttp--activity-rule--", "ttp--mitre-campaign--")
GENERATED_TARGET_PREFIX = "target--activity-rule--"
GENERATED_MITRE_TARGET_PREFIX = "target--mitre-group--"
GENERATED_TARGET_PREFIXES = (
    GENERATED_TARGET_PREFIX,
    GENERATED_MITRE_TARGET_PREFIX,
)
GENERATED_VICTIM_PREFIX = "victim--activity-rule--"
DERIVATION_NOTE = "[activity-rule-v1]"


def normalized_name(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.casefold())


def confidence_floor(value: str) -> str:
    return value if value in {"low", "medium"} else "medium"


def compile_patterns(values: Iterable[str]) -> list[re.Pattern[str]]:
    return [re.compile(value) for value in values]


def compile_rules(
    raw: dict[str, Any],
    catalog: dict[str, Any] | None = None,
) -> dict[str, Any]:
    rules = copy.deepcopy(raw)
    for rule in rules["ttp_rules"]:
        rule["_patterns"] = compile_patterns(rule["patterns"])
        rule["_exclude_patterns"] = compile_patterns(rule.get("exclude_patterns", []))
    rules["_target_context_patterns"] = compile_patterns(
        rules["target_context_patterns"]
    )
    for category in ("countries", "sectors", "assets", "impacts"):
        for rule in rules[category]:
            rule["_patterns"] = compile_patterns(rule["patterns"])
    names = {
        value.strip()
        for item in (catalog or {}).get("actors", [])
        for value in [item.get("name", ""), *item.get("aliases", [])]
        if len(normalized_name(value)) >= 4 and "*" not in value
    }
    rules["_actor_pattern"] = (
        re.compile(
            r"(?i)(?<![a-z0-9])("
            + "|".join(
                re.escape(value) for value in sorted(names, key=len, reverse=True)
            )
            + r")(?![a-z0-9])"
        )
        if names
        else None
    )
    return rules


def known_time(point: dict[str, Any] | None) -> bool:
    return bool(
        point
        and point.get("value")
        and point.get("status") in {"known", "inferred"}
    )


def activity_time(point: dict[str, Any] | None) -> dict[str, Any]:
    if not known_time(point):
        return unknown_time()
    result = copy.deepcopy(point)
    basis = result.get("basis", "source-stated")
    if "activity-period" not in basis:
        result["basis"] = f"{basis}; activity-period"
    return result


def explicit_point(
    year: str,
    month: str | None = None,
    day: str | None = None,
) -> dict[str, Any]:
    if day:
        value = f"{int(year):04d}-{int(month or 1):02d}-{int(day):02d}T00:00:00Z"
        precision = "day"
    elif month:
        value = f"{int(year):04d}-{int(month):02d}-01T00:00:00Z"
        precision = "month"
    else:
        value = f"{int(year):04d}-01-01T00:00:00Z"
        precision = "year"
    return {
        "value": value,
        "precision": precision,
        "status": "known",
        "basis": "activity-description-explicit-period",
    }


def enrich_explicit_activity_period(
    profile: dict[str, Any],
    activity: dict[str, Any],
    rules: dict[str, Any],
) -> bool:
    """Read only unambiguous attack-period phrases from actor-scoped activity text."""
    if known_time(activity.get("first_observed")) and known_time(
        activity.get("last_observed")
    ):
        return False
    text = activity_text(profile, activity, rules)
    first: dict[str, Any] | None = None
    last: dict[str, Any] | None = None

    match = re.search(
        r"(20\d{2})年(\d{1,2})月(?:(\d{1,2})日)?"
        r"(?:から|～|〜|-)(?:(20\d{2})年)?(\d{1,2})月(?:(\d{1,2})日)?"
        r"(?:まで|にかけて|の間|にわたり|)",
        text,
    )
    if match:
        y1, m1, d1, y2, m2, d2 = match.groups()
        first = explicit_point(y1, m1, d1)
        last = explicit_point(y2 or y1, m2, d2)
    if first is None:
        match = re.search(
            r"(20\d{2})年(\d{1,2})月(?:と|、)(\d{1,2})月に"
            r"[^。\n]{0,90}(?:攻撃|キャンペーン|活動|標的|フィッシング|"
            r"使用|展開|発生|観測|確認|実行|開始)",
            text,
        )
        if match:
            year, month1, month2 = match.groups()
            first = explicit_point(year, month1)
            last = explicit_point(year, month2)
    if first is None:
        match = re.search(
            r"(20\d{2})年(\d{1,2})月(?:～|〜|-)(\d{1,2})月に"
            r"[^。\n]{0,90}(?:攻撃|キャンペーン|活動|標的|フィッシング|"
            r"使用|展開|発生|観測|確認|実行|開始)",
            text,
        )
        if match:
            year, month1, month2 = match.groups()
            first = explicit_point(year, month1)
            last = explicit_point(year, month2)
    if first is None:
        match = re.search(
            r"(20\d{2})-(\d{2})-(\d{2})\s*(?:to|through|～|〜|-)\s*"
            r"(20\d{2})-(\d{2})-(\d{2})",
            text,
            re.IGNORECASE,
        )
        if match:
            first = explicit_point(*match.groups()[:3])
            last = explicit_point(*match.groups()[3:])
    if first is None:
        match = re.search(
            r"(20\d{2})年から(20\d{2})年(?:まで|にかけて|の間)"
            r"[^。\n]{0,90}(?:攻撃|キャンペーン|活動|標的|侵害|観測)",
            text,
        )
        if match:
            first = explicit_point(match.group(1))
            last = explicit_point(match.group(2))
    if first is None:
        match = re.search(
            r"(?:(?:攻撃|侵害|キャンペーン|活動|事案)[^。\n]{0,30})?"
            r"(20\d{2})年(\d{1,2})月(\d{1,2})日"
            r"[^。\n]{0,40}(?:発生|開始|確認|観測|実行|展開|侵害|攻撃)",
            text,
        )
        if match:
            first = last = explicit_point(*match.groups())
    if first is None:
        match = re.search(
            r"(20\d{2})年(上半期|下半期|第[1-4]四半期)に"
            r"[^。\n]{0,100}(?:攻撃|キャンペーン|活動|標的|フィッシング|"
            r"使用|展開|発生|観測|確認|実行|開始)",
            text,
        )
        if match:
            year, period = match.groups()
            month_ranges = {
                "上半期": ("1", "6"),
                "下半期": ("7", "12"),
                "第1四半期": ("1", "3"),
                "第2四半期": ("4", "6"),
                "第3四半期": ("7", "9"),
                "第4四半期": ("10", "12"),
            }
            first_month, last_month = month_ranges[period]
            first = explicit_point(year, first_month)
            last = explicit_point(year, last_month)
    if first is None:
        match = re.search(
            r"(20\d{2})年(\d{1,2})月(?:上旬|中旬|下旬|前半|後半)?に"
            r"[^。\n]{0,100}(?:攻撃|キャンペーン|活動|標的|フィッシング|"
            r"使用|展開|発生|観測|確認|実行|開始|悪用|侵害)",
            text,
        )
        if match:
            first = last = explicit_point(*match.groups())
    if first is None:
        match = re.search(
            r"(20\d{2})年(\d{1,2})月以降[^。\n]{0,100}"
            r"(?:攻撃|キャンペーン|活動|標的|フィッシング|使用|展開|"
            r"発生|観測|確認|実行|開始|悪用|侵害)",
            text,
        )
        if match:
            first = explicit_point(*match.groups())
    if first is None and last is None:
        match = re.search(
            r"(20\d{2})年(\d{1,2})月までに[^。\n]{0,100}"
            r"(?:攻撃|キャンペーン|活動|標的|フィッシング|使用|展開|"
            r"発生|観測|確認|実行|開始|悪用|侵害)",
            text,
        )
        if match:
            last = explicit_point(*match.groups())
    if first is None:
        match = re.search(
            r"(20\d{2})年(?:初頭|初め|年初|年末)に"
            r"[^。\n]{0,100}(?:攻撃|キャンペーン|活動|標的|フィッシング|"
            r"使用|展開|発生|観測|確認|実行|開始|悪用|侵害)",
            text,
        )
        if match:
            first = last = explicit_point(match.group(1))
    if first is None and last is None:
        return False
    if first is not None and not known_time(activity.get("first_observed")):
        activity["first_observed"] = first
    if last is not None and not known_time(activity.get("last_observed")):
        activity["last_observed"] = last
    marker = (
        f"{DERIVATION_NOTE} 活動記述に明示された攻撃期間を構造化。"
        "資料発行日・ニュース日付・IOC収集日は使用していない。"
    )
    if marker not in activity.get("analyst_notes", ""):
        activity["analyst_notes"] = (
            f"{activity.get('analyst_notes', '').rstrip()} {marker}".strip()
        )
    return True


def date_min(
    left: dict[str, Any] | None,
    right: dict[str, Any] | None,
) -> dict[str, Any]:
    if not known_time(left):
        return copy.deepcopy(right) if right else unknown_time()
    if not known_time(right):
        return copy.deepcopy(left)
    return copy.deepcopy(left if left["value"] <= right["value"] else right)


def date_max(
    left: dict[str, Any] | None,
    right: dict[str, Any] | None,
) -> dict[str, Any]:
    if not known_time(left):
        return copy.deepcopy(right) if right else unknown_time()
    if not known_time(right):
        return copy.deepcopy(left)
    return copy.deepcopy(left if left["value"] >= right["value"] else right)


def first_match(
    patterns: Iterable[re.Pattern[str]],
    text: str,
) -> re.Match[str] | None:
    matches = [match for pattern in patterns if (match := pattern.search(text))]
    return min(matches, key=lambda item: item.start()) if matches else None


def excerpt_for(text: str, match: re.Match[str], *, radius: int = 180) -> str:
    start = max(
        text.rfind("。", 0, match.start()),
        text.rfind("\n", 0, match.start()),
        text.rfind(". ", 0, match.start()),
    )
    start = max(0, start + 1, match.start() - radius)
    ends = [
        value
        for value in (
            text.find("。", match.end()),
            text.find("\n", match.end()),
            text.find(". ", match.end()),
        )
        if value >= 0
    ]
    end = min(ends) + 1 if ends else min(len(text), match.end() + radius)
    return re.sub(r"\s+", " ", text[start:end]).strip()[:600]


def source_references(profile: dict[str, Any]) -> set[str]:
    return {item["source_id"] for item in profile.get("sources", [])}


def contains_evidence_reference(value: Any, source_id: str) -> bool:
    if isinstance(value, dict):
        if source_id in value.get("evidence_refs", []):
            return True
        return any(
            contains_evidence_reference(child, source_id)
            for key, child in value.items()
            if key != "sources"
        )
    if isinstance(value, list):
        return any(contains_evidence_reference(child, source_id) for child in value)
    return False


def ensure_mitre_source(profile: dict[str, Any], attack: dict[str, Any]) -> None:
    if MITRE_SOURCE_ID in source_references(profile):
        return
    source = attack.get("source", {})
    profile.setdefault("sources", []).append(
        {
            "source_id": MITRE_SOURCE_ID,
            "path": "actor_profile/reference/attack-index.json",
            "title": (
                f"MITRE {source.get('name', 'Enterprise ATT&CK')} "
                f"{source.get('version', '')} compact local index"
            ).strip(),
            "publisher": "MITRE",
            "published_at": unknown_time(),
            "language": "en",
            "source_type": "structured-knowledge-base",
            "tlp": "TLP:CLEAR",
            "reliability": "high",
            "sha256": None,
            "analyst_notes": (
                "Derived from the official MITRE attack-stix-data repository. "
                "ATT&CK relationship modification dates are not observation dates."
            ),
        }
    )


def cleanup_generated(profile: dict[str, Any]) -> None:
    removed_ttps = {
        item["ttp_id"]
        for item in profile.get("ttps", [])
        if item.get("ttp_id", "").startswith(GENERATED_TTP_PREFIXES)
    }
    removed_targets = {
        item["id"]
        for category in ("countries", "regions", "sectors", "roles")
        for item in profile.get("targets", {}).get(category, [])
        if item.get("id", "").startswith(GENERATED_TARGET_PREFIXES)
    }
    removed_victims = {
        item["victim_case_id"]
        for item in profile.get("victim_cases", [])
        if item.get("victim_case_id", "").startswith(GENERATED_VICTIM_PREFIX)
    }
    profile["ttps"] = [
        item
        for item in profile.get("ttps", [])
        if item.get("ttp_id") not in removed_ttps
    ]
    for category in ("countries", "regions", "sectors", "roles"):
        profile["targets"][category] = [
            item
            for item in profile["targets"].get(category, [])
            if item.get("id") not in removed_targets
        ]
    profile["victim_cases"] = [
        item
        for item in profile.get("victim_cases", [])
        if item.get("victim_case_id") not in removed_victims
    ]
    for activity in profile.get("activities", []):
        activity["ttp_refs"] = [
            ref for ref in activity.get("ttp_refs", []) if ref not in removed_ttps
        ]
        activity["target_refs"] = [
            ref for ref in activity.get("target_refs", []) if ref not in removed_targets
        ]
        activity["victim_refs"] = [
            ref for ref in activity.get("victim_refs", []) if ref not in removed_victims
        ]


def profile_actor_names(profile: dict[str, Any]) -> set[str]:
    return {
        normalized_name(value)
        for value in [
            profile.get("name", ""),
            profile.get("actor", {}).get("canonical_name", ""),
            *(
                item.get("name", "")
                for item in profile.get("actor", {}).get("aliases", [])
            ),
        ]
        if value
    }


def activity_text(
    profile: dict[str, Any],
    activity: dict[str, Any],
    rules: dict[str, Any],
) -> str:
    title = activity.get("name", "")
    description = activity.get("description", "")
    actor_pattern = rules.get("_actor_pattern")
    if not actor_pattern:
        return f"{title}\n{description}".strip()
    all_mentions = {
        normalized_name(match.group(1))
        for match in actor_pattern.finditer(description)
    }
    if len(all_mentions) <= 1:
        return f"{title}\n{description}".strip()

    # Multi-actor roundups are common in daily news. Keep only the current
    # actor's segment and its following behavior sentences.
    parts = [
        item.strip()
        for item in re.split(
            r"(?:\r?\n)+|(?<=[。.!?])\s+|"
            r"(?=(?<![A-Za-z0-9])(?:APT|TA|UNC|UAC|UNK|Storm-)\w+"
            r"(?:\s*\([^)]{1,60}\))?\s*:)",
            description,
        )
        if item.strip()
    ]
    own_names = profile_actor_names(profile)
    selected: list[str] = []
    for index, part in enumerate(parts):
        mentions = {
            normalized_name(match.group(1))
            for match in actor_pattern.finditer(part)
        }
        if not (mentions & own_names):
            continue
        selected.append(part)
        for following in parts[index + 1 : index + 4]:
            following_mentions = {
                normalized_name(match.group(1))
                for match in actor_pattern.finditer(following)
            }
            if following_mentions and not (following_mentions & own_names):
                break
            selected.append(following)
    if not selected:
        return title
    return "\n".join(dict.fromkeys([title, *selected]))


def malware_refs_in_excerpt(
    profile: dict[str, Any],
    excerpt: str,
) -> list[str]:
    folded = excerpt.casefold()
    result: set[str] = set()
    for item in profile.get("capabilities", {}).get("malware", []):
        for name in [item.get("name", ""), *item.get("aliases", [])]:
            name = name.strip()
            if len(name) < 4:
                continue
            if re.search(
                rf"(?<![a-z0-9]){re.escape(name.casefold())}(?![a-z0-9])",
                folded,
            ):
                result.add(item["id"])
                break
    return sorted(result)


def add_rule_ttps(
    profile: dict[str, Any],
    activity: dict[str, Any],
    rules: dict[str, Any],
    attack: dict[str, Any],
) -> list[str]:
    text = activity_text(profile, activity, rules)
    added: list[str] = []
    for rule in rules["ttp_rules"]:
        match = first_match(rule["_patterns"], text)
        if match is None:
            continue
        window = text[
            max(0, match.start() - 100) : min(len(text), match.end() + 100)
        ]
        if any(pattern.search(window) for pattern in rule["_exclude_patterns"]):
            continue
        technique_id = rule["technique_id"]
        technique = attack.get("techniques", {}).get(technique_id)
        if not technique:
            continue
        digest = stable_digest(activity["activity_id"], technique_id)[:20]
        ttp_id = f"ttp--activity-rule--{digest}"
        excerpt = excerpt_for(text, match)
        item = {
            "ttp_id": ttp_id,
            "tactic": ", ".join(technique.get("tactics", []) or ["Uncategorized"]),
            "technique_id": technique_id,
            "technique_name": technique.get("name", technique_id),
            "observed_behavior": excerpt,
            "activity_refs": [activity["activity_id"]],
            "malware_refs": malware_refs_in_excerpt(profile, excerpt),
            "infrastructure_refs": [],
            "first_observed": activity_time(activity.get("first_observed")),
            "last_observed": activity_time(activity.get("last_observed")),
            "confidence": confidence_floor(activity.get("confidence", "unknown")),
            "evidence_refs": sorted(set(activity.get("evidence_refs", []))),
            "analyst_notes": (
                f"{DERIVATION_NOTE} 活動記述に明示された行動をATT&CKへ分析者対応付け。"
                "資料発行日は観測日として使用していない。"
            ),
        }
        profile["ttps"].append(item)
        added.append(ttp_id)
    activity["ttp_refs"] = sorted(set(activity.get("ttp_refs", [])) | set(added))
    return added


def actor_attribution_context(
    text: str,
    match: re.Match[str],
    actor_pattern: re.Pattern[str] | None = None,
) -> bool:
    after = text[match.end() : match.end() + 55]
    before = text[max(0, match.start() - 80) : match.start()]
    citation_start = before.rfind("(Citation:")
    citation_end = before.rfind(")")
    if citation_start > citation_end:
        return True
    attribution_suffix = (
        r"(?i)^\s*(?:[a-z]{1,4})?\s*"
        r"(?:(?:\([^)]{1,16}\)|['’]s)\s*)?"
        r"(?:[-–—]\s*)?(?:based|backed|sponsored|aligned|linked|nexus|"
        r"speaking|state[- ](?:sponsored|backed)|government[- ]backed|"
        r"threat (?:actor|group)|cyber\s*(?:espionage|spy) (?:actor|group)|"
        r"ministry|foreign intelligence|federal security)"
    )
    actor_terms = (
        r"(?i)^\s*(?:linked|based|backed|sponsored|state-sponsored|"
        r"government-backed|nexus)?\s*(?:apt|hackers?|actors?|groups?|"
        r"threat actors?|cyberspies|cyber espionage groups?)"
    )
    japanese_terms = (
        r"^\s*(?:(?:系|関連|関与|支援|国家支援|政府支援)(?:の)?|"
        r"の(?:国家|政府)?(?:支援)?)?\s*人?\s*"
        r"(?:APT|ハッカー|ハッキンググループ|アクター|攻撃者|グループ|"
        r"サイバー部隊|SVR|GRU|FSB)"
    )
    # 「イラン人17人を起訴」のように国籍＋人数で被疑者を数える表現は攻撃者側の
    # 国籍であり、被害国ではない。「日本人を標的」のような被害者表現は数詞を
    # 伴わないため、この判定では除外されない。
    japanese_nationality_count = r"^\s*人\s*(?:約)?\d+\s*人"
    if (
        re.search(attribution_suffix, after)
        or re.search(actor_terms, after)
        or re.search(japanese_terms, after)
        or re.search(japanese_nationality_count, after)
        or re.search(r"^\s*(?:系|関連|関与|支援)(?:の)?", after)
        or re.search(r"^\s*の(?:敵対国|同盟国|友好国)", after)
    ):
        return True
    if actor_pattern:
        actor_match = actor_pattern.search(after)
        if actor_match and actor_match.start() <= 35:
            return True
    return bool(
        re.search(
            r"(?i)(?:from|by|"
            r"(?:linked|aligned|affiliated|attributed)\s+(?:to|with)|"
            r"operat(?:e|es|ed|ing)\s+out\s+of|on\s+behalf\s+of)\s*$",
            before,
        )
    )


def contextual_match(
    text: str,
    patterns: Iterable[re.Pattern[str]],
    context_patterns: Iterable[re.Pattern[str]],
    *,
    country: bool = False,
    actor_pattern: re.Pattern[str] | None = None,
) -> re.Match[str] | None:
    for pattern in patterns:
        for match in pattern.finditer(text):
            if country and actor_attribution_context(text, match, actor_pattern):
                continue
            if explicit_target_context(text, match, country=country):
                return match
            # Country lists often place the targeting verb only before the
            # first country (for example, "targeted ... in the United States,
            # Israel, Australia, Russia, and India").  Treat every country in
            # that sentence as a target while retaining the attribution-country
            # guard above.
            sentence_start = max(
                text.rfind(delimiter, 0, match.start())
                for delimiter in (".", "!", "?", "。", "！", "？", "\n")
            )
            sentence_ends = [
                position
                for delimiter in (".", "!", "?", "。", "！", "？", "\n")
                if (position := text.find(delimiter, match.end())) >= 0
            ]
            sentence_end = min(sentence_ends, default=len(text))
            sentence = text[sentence_start + 1 : sentence_end]
            if country and any(
                pattern.search(sentence) for pattern in context_patterns
            ):
                return match
    return None


def explicit_target_context(
    text: str,
    match: re.Match[str],
    *,
    country: bool,
) -> bool:
    before = text[max(0, match.start() - 100) : match.start()]
    after = text[match.end() : min(len(text), match.end() + 100)]
    if re.search(
        r"(?i)(?:target|attack|breach|compromise|phish|spy on|victims? in|"
        r"victims? across)(?:ed|es|ing|s)?(?:\s+\w+){0,8}\s*$",
        before,
    ) or re.search(
        r"(?:標的|攻撃|侵害|フィッシング|諜報|窃取|被害)(?:とした|にした|する|"
        r"した|された)?[^。\n]{0,45}$",
        before,
    ):
        return True
    if country:
        return bool(
            re.search(
                r"(?i)^(?:n|ian|ese|ish)?\s+(?:government|organizations?|"
                r"firms?|companies|users?|systems?|entities|officials?|"
                r"institutes?|parties|sector)[^.\n]{0,60}"
                r"(?:target|attack|breach|compromise|phish|steal)",
                after,
            )
            or re.search(
                r"^[^、。\n]{0,70}(?:を[^、。\n]{0,35}(?:標的|攻撃|侵害)|"
                r"を狙|への攻撃|に対する攻撃|で被害|"
                r"に対して(?:使用|展開))",
                after,
            )
            or re.search(
                r"^(?:を|への|に対する|国内での)[^。\n]{0,45}"
                r"(?:標的|攻撃|侵害|フィッシング|諜報|窃取|被害)",
                after,
            )
        )
    return bool(
        re.search(
            r"(?i)^(?:\s+(?:organizations?|firms?|companies|users?|systems?|"
            r"entities|officials?|institutes?|sector))?[^.\n]{0,55}"
            r"(?:target|attack|breach|compromise|phish|victim)",
            after,
        )
        or re.search(
            r"^[^、。\n]{0,70}(?:を[^、。\n]{0,35}(?:標的|攻撃|侵害)|"
            r"を狙|への攻撃|に対する攻撃|で被害|"
            r"に対して(?:使用|展開)|フィッシング)",
            after,
        )
    )


def semantic_target(
    targets: list[dict[str, Any]],
    rule: dict[str, Any],
) -> dict[str, Any] | None:
    for target in targets:
        if target.get("name") == rule["name"]:
            return target
        if any(pattern.fullmatch(target.get("name", "")) for pattern in rule["_patterns"]):
            return target
    return None


def add_targets(
    profile: dict[str, Any],
    activity: dict[str, Any],
    rules: dict[str, Any],
) -> list[str]:
    text = activity_text(profile, activity, rules)
    refs: set[str] = set(activity.get("target_refs", []))
    for source_key, category, kind in (
        ("countries", "countries", "country"),
        ("sectors", "sectors", "sector"),
    ):
        targets = profile["targets"][category]
        for rule in rules[source_key]:
            match = contextual_match(
                text,
                rule["_patterns"],
                rules["_target_context_patterns"],
                country=kind == "country",
                actor_pattern=rules.get("_actor_pattern"),
            )
            if match is None:
                continue
            target = semantic_target(targets, rule)
            if target is None:
                digest = stable_digest(kind, rule["name"])[:20]
                target = {
                    "id": f"{GENERATED_TARGET_PREFIX}{kind}--{digest}",
                    "name": rule["name"],
                    "description": (
                        f"活動「{activity['name']}」の記述で標的として明示された"
                        f"{'国・地域' if kind == 'country' else '産業'}。"
                    ),
                    "first_observed": activity_time(activity.get("first_observed")),
                    "last_observed": activity_time(activity.get("last_observed")),
                    "confidence": confidence_floor(
                        activity.get("confidence", "unknown")
                    ),
                    "evidence_refs": sorted(
                        set(activity.get("evidence_refs", []))
                    ),
                    "analyst_notes": (
                        f"{DERIVATION_NOTE} 標的文脈を伴う明示語から構造化。"
                        "アクター帰属国と被害国は分離している。"
                    ),
                }
                targets.append(target)
            else:
                target["first_observed"] = date_min(
                    target.get("first_observed"),
                    activity_time(activity.get("first_observed")),
                )
                target["last_observed"] = date_max(
                    target.get("last_observed"),
                    activity_time(activity.get("last_observed")),
                )
                target["evidence_refs"] = sorted(
                    set(target.get("evidence_refs", []))
                    | set(activity.get("evidence_refs", []))
                )
            refs.add(target["id"])
    activity["target_refs"] = sorted(refs)
    return sorted(refs)


def mitre_target_match(
    text: str,
    patterns: Iterable[re.Pattern[str]],
    *,
    country: bool,
    actor_pattern: re.Pattern[str] | None,
) -> re.Match[str] | None:
    """Find a target in an official ATT&CK group summary."""
    for pattern in patterns:
        for match in pattern.finditer(text):
            if country and actor_attribution_context(text, match, actor_pattern):
                continue
            excerpt = excerpt_for(text, match, radius=260)
            if re.search(
                r"(?i)\b(?:target(?:ed|s|ing)?|victims?|campaigns?\s+against|"
                r"operations?\s+(?:expanded|extended)\s+to\s+include|"
                r"compromis(?:ed|es|ing))\b",
                excerpt,
            ):
                return match
    return None


def add_mitre_group_targets(
    profile: dict[str, Any],
    group: dict[str, Any],
    rules: dict[str, Any],
) -> int:
    """Add actor-level country/sector targeting stated by ATT&CK."""
    text = group.get("description", "")
    if not text:
        return 0
    added = 0
    for source_key, category, kind in (
        ("countries", "countries", "country"),
        ("sectors", "sectors", "sector"),
    ):
        targets = profile["targets"][category]
        for rule in rules[source_key]:
            match = mitre_target_match(
                text,
                rule["_patterns"],
                country=kind == "country",
                actor_pattern=rules.get("_actor_pattern"),
            )
            if match is None:
                continue
            target = semantic_target(targets, rule)
            if target is None:
                digest = stable_digest(group.get("external_id", ""), kind, rule["name"])[
                    :20
                ]
                target = {
                    "id": f"{GENERATED_MITRE_TARGET_PREFIX}{kind}--{digest}",
                    "name": rule["name"],
                    "description": excerpt_for(text, match, radius=260),
                    "first_observed": unknown_time(),
                    "last_observed": unknown_time(),
                    "confidence": "high",
                    "evidence_refs": [MITRE_SOURCE_ID],
                    "analyst_notes": (
                        "[mitre-group-target-v1] 公式ATT&CKのGroup概要で"
                        "標的として明示された国・地域または産業。"
                        "Group概要には通常、個別の観測日はない。"
                    ),
                }
                targets.append(target)
                added += 1
            else:
                target["evidence_refs"] = sorted(
                    set(target.get("evidence_refs", [])) | {MITRE_SOURCE_ID}
                )
    return added


def matching_rule_names(
    text: str,
    rules: Iterable[dict[str, Any]],
) -> list[str]:
    return [
        rule["name"]
        for rule in rules
        if first_match(rule["_patterns"], text) is not None
    ]


def matching_impacts(
    text: str,
    rules: Iterable[dict[str, Any]],
) -> list[dict[str, str]]:
    impacts: list[dict[str, str]] = []
    for rule in rules:
        match = first_match(rule["_patterns"], text)
        if match is None:
            continue
        impacts.append(
            {
                "impact_type": rule["impact_type"],
                "description": excerpt_for(text, match),
            }
        )
    return impacts


def named_victim(
    activity: dict[str, Any],
    profile: dict[str, Any],
) -> str | None:
    title = activity.get("name", "").strip()
    patterns = (
        re.compile(
            r"^([A-Z][A-Za-z0-9&.'’()/ -]{2,70}?)\s+"
            r"(?:confirms?|discloses?|reports?|says?|takes? .{0,20} offline|"
            r"hit by|suffers?)\b"
        ),
        re.compile(
            r"^([A-Z][A-Za-z0-9&.'’()/ -]{2,70}?)[、が]"
            r"(?:データ侵害|情報漏えい|サイバー攻撃|ランサムウェア|侵害|被害|"
            r"サーバーをオフライン)"
        ),
        re.compile(
            r"^([^、]{2,70})、[^。]{0,70}(?:攻撃後|侵害を(?:公表|確認)|"
            r"攻撃を(?:公表|確認)|被害を(?:公表|確認)|データ侵害|情報漏えい|"
            r"身代金要求|攻撃に関する[^。]{0,25}(?:共有|更新))"
        ),
        re.compile(
            r"^([^、]{2,70})の(?:社内|企業|コーポレート)?[^、]{0,45}"
            r"(?:ネットワーク|システム|サーバー|データ)[^、]{0,25}"
            r"(?:侵害|攻撃|暗号化)"
        ),
        re.compile(
            r"(?:攻撃で|攻撃後の)([A-Z][A-Za-z0-9&.'’()/ -]{2,70}?)が"
            r"(?:身代金要求|被害|侵害)"
        ),
    )
    candidate = None
    for pattern in patterns:
        match = pattern.search(title)
        if match:
            candidate = match.group(1).strip(" -、")
            break
    if not candidate:
        return None
    aliases = {
        normalized_name(profile.get("name", "")),
        normalized_name(profile.get("actor", {}).get("canonical_name", "")),
        *(
            normalized_name(item.get("name", ""))
            for item in profile.get("actor", {}).get("aliases", [])
        ),
    }
    lowered = candidate.casefold()
    if (
        normalized_name(candidate) in aliases
        or re.fullmatch(
            r"(?i)(?:recent|today|yesterday|government|authorities|"
            r"fbi|cisa|ncsc|sec)|(?:最近|本日|昨日|政府|当局|警察|英国政府)",
            candidate,
        )
        or re.search(
            r"(?i)\b(?:apt|hackers?|actors?|group|ransomware)\b|"
            r"(?:ハッカー|アクター|攻撃者|グループ)$",
            lowered,
        )
    ):
        return None
    return candidate


def victim_case_status(text: str) -> str:
    if re.search(
        r"(?i)(?:denies?|denied|disputes?|rebut|rejects?).{0,50}"
        r"(?:breach|attack|compromise|data theft|claim)|"
        r"(?:breach|attack|compromise|data theft|claim).{0,50}"
        r"(?:denies?|denied|disputes?|rebut|rejects?)|"
        r"(?:データ侵害|情報漏えい|被害|犯行声明|攻撃を受けたとの主張)"
        r"[^。]{0,35}(?:否定|反論|事実ではない|主張を退け)",
        text,
    ):
        return "disputed"
    if re.search(
        r"(?i)(?:alleged|claims?|claimed|threatens? to leak).{0,50}"
        r"(?:breach|attack|compromise|data theft)|"
        r"(?:breach|attack|compromise|data theft).{0,50}(?:claims?|claimed)|"
        r"(?:犯行声明|侵害したと主張|攻撃したと発表|リークを予告|"
        r"データ侵害主張)",
        text,
    ):
        return "alleged"
    if re.search(
        r"(?i)\b(?:confirms?|confirmed|discloses?|acknowledges?)\b|"
        r"(?:確認|公表|認め|発表)",
        text,
    ):
        return "reported"
    return "reported"


def has_case_signal(activity: dict[str, Any], text: str, impacts: list[dict[str, str]]) -> bool:
    if activity.get("target_refs"):
        return True
    if activity.get("activity_type") in {
        "intrusion",
        "ransomware-extortion",
        "disruptive-activity",
    }:
        return True
    if any(item["impact_type"] != "espionage" for item in impacts):
        return bool(
            re.search(
                r"(?i)\b(?:victims?|breach(?:ed|es|ing)?|compromise(?:d|s|ing)?|"
                r"attack(?:ed|s|ing)?)\b|(?:被害|侵害|攻撃|窃取|流出)",
                text,
            )
        )
    return False


def add_victim_case(
    profile: dict[str, Any],
    activity: dict[str, Any],
    rules: dict[str, Any],
) -> str | None:
    text = activity_text(profile, activity, rules)
    impacts = matching_impacts(text, rules["impacts"])
    if not has_case_signal(activity, text, impacts):
        return None
    victim = named_victim(activity, profile)
    aggregate_signal = bool(
        re.search(
            r"(?i)\b(?:multiple|numerous|hundreds?|thousands?|organizations?|"
            r"companies|firms|users|victims)\b|(?:複数|多数|数百|数千|組織|企業|"
            r"利用者|ユーザー|被害者)",
            text,
        )
    )
    disclosure = "named" if victim else ("aggregate" if aggregate_signal else "anonymous")
    victim_type = (
        "organization"
        if victim
        else ("multiple-organizations" if aggregate_signal else "unknown")
    )
    digest = stable_digest(activity["activity_id"])[:20]
    victim_id = f"{GENERATED_VICTIM_PREFIX}{digest}"
    case = {
        "victim_case_id": victim_id,
        "name": f"被害事例: {activity['name']}",
        "victim_name": victim,
        "disclosure_status": disclosure,
        "victim_type": victim_type,
        "case_status": victim_case_status(text),
        "description": activity.get("description", ""),
        "activity_refs": [activity["activity_id"]],
        "target_refs": sorted(set(activity.get("target_refs", []))),
        "malware_refs": sorted(set(activity.get("malware_refs", []))),
        "ttp_refs": sorted(set(activity.get("ttp_refs", []))),
        "affected_assets": matching_rule_names(text, rules["assets"]),
        "impacts": impacts,
        "first_observed": copy.deepcopy(activity.get("first_observed") or unknown_time()),
        "last_observed": copy.deepcopy(activity.get("last_observed") or unknown_time()),
        "reported_at": copy.deepcopy(activity.get("reported_at") or unknown_time()),
        "confidence": activity.get("confidence", "unknown"),
        "evidence_refs": sorted(set(activity.get("evidence_refs", []))),
        "analyst_notes": (
            f"{DERIVATION_NOTE} 活動と標的・影響の明示記述から被害事例を構造化。"
            "個別被害者名が公開されていない場合は匿名または集約事例として保持。"
            "被害主張への明示的な否定・反論はdisputedとして分離。"
        ),
    }
    profile["victim_cases"].append(case)
    activity["victim_refs"] = sorted(
        set(activity.get("victim_refs", [])) | {victim_id}
    )
    return victim_id


def capability_from_attack(
    software: dict[str, Any],
    activity: dict[str, Any],
) -> dict[str, Any]:
    kind = software.get("software_type", "malware")
    prefix = "malware" if kind == "malware" else "tool"
    external_id = software.get("external_id") or stable_digest(software.get("name", ""))[:20]
    return {
        "id": f"{prefix}--mitre--{external_id.casefold()}",
        "name": software.get("name", external_id),
        "aliases": software.get("aliases", []),
        "types": software.get("platforms", []),
        "description": software.get("description", ""),
        "first_observed": activity_time(activity.get("first_observed")),
        "last_observed": activity_time(activity.get("last_observed")),
        "confidence": "high",
        "evidence_refs": [MITRE_SOURCE_ID],
        "analyst_notes": (
            "MITRE ATT&CK campaign-to-software relationship. "
            "ATT&CK coverage is a public-reporting subset."
        ),
    }


def ensure_campaign_software(
    profile: dict[str, Any],
    activity: dict[str, Any],
    uses: list[dict[str, Any]],
    attack: dict[str, Any],
) -> None:
    malware_lookup = {
        normalized_name(item.get("name", "")): item
        for item in profile["capabilities"]["malware"]
    }
    tool_lookup = {
        normalized_name(item.get("name", "")): item
        for item in profile["capabilities"]["tools"]
    }
    for use in uses:
        software = attack.get("software", {}).get(use.get("target_ref", ""))
        if not software:
            continue
        kind = software.get("software_type")
        lookup = malware_lookup if kind == "malware" else tool_lookup
        collection = (
            profile["capabilities"]["malware"]
            if kind == "malware"
            else profile["capabilities"]["tools"]
        )
        key = normalized_name(software.get("name", ""))
        item = lookup.get(key)
        if item is None:
            item = capability_from_attack(software, activity)
            collection.append(item)
            lookup[key] = item
        else:
            item["first_observed"] = date_min(
                item.get("first_observed"),
                activity_time(activity.get("first_observed")),
            )
            item["last_observed"] = date_max(
                item.get("last_observed"),
                activity_time(activity.get("last_observed")),
            )
            item["evidence_refs"] = sorted(
                set(item.get("evidence_refs", [])) | {MITRE_SOURCE_ID}
            )
        if kind == "malware":
            activity["malware_refs"] = sorted(
                set(activity.get("malware_refs", [])) | {item["id"]}
            )


def mitre_campaign_ttp(
    activity: dict[str, Any],
    use: dict[str, Any],
    attack: dict[str, Any],
) -> dict[str, Any] | None:
    technique_id = use.get("target_external_id", "")
    technique = attack.get("techniques", {}).get(technique_id)
    if not technique:
        return None
    digest = stable_digest(activity["activity_id"], technique_id)[:20]
    return {
        "ttp_id": f"ttp--mitre-campaign--{digest}",
        "tactic": ", ".join(technique.get("tactics", []) or ["Uncategorized"]),
        "technique_id": technique_id,
        "technique_name": technique.get("name", technique_id),
        "observed_behavior": use.get("description", ""),
        "activity_refs": [activity["activity_id"]],
        "malware_refs": [],
        "infrastructure_refs": [],
        "first_observed": activity_time(activity.get("first_observed")),
        "last_observed": activity_time(activity.get("last_observed")),
        "confidence": "high",
        "evidence_refs": [MITRE_SOURCE_ID],
        "analyst_notes": (
            "MITRE ATT&CK campaign-to-technique relationship. "
            "Campaign period is used as the observation interval; relationship "
            "modification and source publication dates are not used."
        ),
    }


def find_activity(
    profile: dict[str, Any],
    name: str,
) -> dict[str, Any] | None:
    key = normalized_name(name)
    return next(
        (
            item
            for item in profile.get("activities", [])
            if normalized_name(item.get("name", "")) == key
        ),
        None,
    )


def add_mitre_campaigns(
    profile: dict[str, Any],
    group: dict[str, Any] | None,
    attack: dict[str, Any],
) -> int:
    if not group:
        return 0
    added_ttps = 0
    for campaign_ref in group.get("campaign_refs", []):
        campaign = attack.get("campaigns", {}).get(campaign_ref)
        if not campaign:
            continue
        activity = find_activity(profile, campaign.get("name", ""))
        if activity is None:
            digest = stable_digest(campaign_ref)[:20]
            activity = {
                "activity_id": f"activity--mitre-campaign--{digest}",
                "name": campaign.get("name", campaign.get("external_id", "Campaign")),
                "activity_type": "campaign",
                "first_observed": (
                    {
                        "value": campaign["first_seen"],
                        "precision": "day",
                        "status": "known",
                        "basis": "mitre-attack-campaign",
                    }
                    if campaign.get("first_seen")
                    else unknown_time()
                ),
                "last_observed": (
                    {
                        "value": campaign["last_seen"],
                        "precision": "day",
                        "status": "known",
                        "basis": "mitre-attack-campaign",
                    }
                    if campaign.get("last_seen")
                    else unknown_time()
                ),
                "reported_at": unknown_time(),
                "description": campaign.get("description", ""),
                "target_refs": [],
                "malware_refs": [],
                "infrastructure_refs": [],
                "ttp_refs": [],
                "victim_refs": [],
                "confidence": "high",
                "evidence_refs": [MITRE_SOURCE_ID],
                "analyst_notes": (
                    "MITRE ATT&CK campaign attributed to this group. "
                    "ATT&CK campaign coverage is not exhaustive."
                ),
            }
            profile["activities"].append(activity)
        ensure_campaign_software(
            profile,
            activity,
            campaign.get("software_uses", []),
            attack,
        )
        for use in campaign.get("technique_uses", []):
            ttp = mitre_campaign_ttp(activity, use, attack)
            if ttp is None:
                continue
            profile["ttps"].append(ttp)
            activity["ttp_refs"] = sorted(
                set(activity.get("ttp_refs", [])) | {ttp["ttp_id"]}
            )
            added_ttps += 1
    return added_ttps


def enrich_general_mitre_ttps(
    profile: dict[str, Any],
    group: dict[str, Any] | None,
) -> int:
    if not group:
        return 0
    uses = {
        item.get("target_external_id"): item
        for item in group.get("technique_uses", [])
        if item.get("target_external_id")
    }
    count = 0
    for ttp in profile.get("ttps", []):
        if ttp.get("activity_refs"):
            continue
        use = uses.get(ttp.get("technique_id"))
        if not use or not use.get("description"):
            continue
        if (
            ttp.get("observed_behavior") == "MITRE ATT&CK maps this technique to the actor."
            or not ttp.get("observed_behavior")
        ):
            ttp["observed_behavior"] = use["description"]
            ttp["analyst_notes"] = (
                "MITRE ATT&CK actor-level procedure example. "
                "No activity period is inferred from source publication or "
                "relationship modification dates."
            )
            count += 1
    return count


def catalog_group_map(catalog: dict[str, Any]) -> dict[str, str]:
    return {
        item["slug"]: item["mitre_group_id"]
        for item in catalog.get("actors", [])
        if item.get("mitre_group_id")
    }


def profile_stats(profile: dict[str, Any]) -> dict[str, int]:
    return {
        "activities": len(profile.get("activities", [])),
        "dated_activities": sum(
            known_time(item.get("first_observed"))
            or known_time(item.get("last_observed"))
            for item in profile.get("activities", [])
        ),
        "victim_cases": len(profile.get("victim_cases", [])),
        "named_victim_cases": sum(
            bool(item.get("victim_name"))
            for item in profile.get("victim_cases", [])
        ),
        "disputed_victim_cases": sum(
            item.get("case_status") == "disputed"
            for item in profile.get("victim_cases", [])
        ),
        "activity_linked_ttps": sum(
            bool(item.get("activity_refs")) for item in profile.get("ttps", [])
        ),
        "dated_activity_linked_ttps": sum(
            bool(item.get("activity_refs"))
            and (
                known_time(item.get("first_observed"))
                or known_time(item.get("last_observed"))
            )
            for item in profile.get("ttps", [])
        ),
        "activity_target_refs": sum(
            len(item.get("target_refs", []))
            for item in profile.get("activities", [])
        ),
        "activity_malware_refs": sum(
            len(item.get("malware_refs", []))
            for item in profile.get("activities", [])
        ),
        "targets": sum(
            len(profile.get("targets", {}).get(category, []))
            for category in ("countries", "regions", "sectors", "roles")
        ),
    }


def enrich_profile(
    profile: dict[str, Any],
    rules: dict[str, Any],
    attack: dict[str, Any],
    group: dict[str, Any] | None,
) -> dict[str, int]:
    cleanup_generated(profile)
    if group:
        ensure_mitre_source(profile, attack)
        enrich_general_mitre_ttps(profile, group)
        add_mitre_group_targets(profile, group, rules)
        add_mitre_campaigns(profile, group, attack)
    else:
        # This source is generated by this script and is not relevant without a
        # mapped ATT&CK Group, unless a reviewed relationship or other record
        # already cites it.
        if contains_evidence_reference(profile, MITRE_SOURCE_ID):
            ensure_mitre_source(profile, attack)
        else:
            profile["sources"] = [
                item
                for item in profile.get("sources", [])
                if item.get("source_id") != MITRE_SOURCE_ID
            ]
    # ATT&CK campaign activities are processed through the same target/victim
    # logic as repository and daily activities.
    for activity in profile.get("activities", []):
        activity.setdefault("ttp_refs", [])
        activity.setdefault("victim_refs", [])
        enrich_explicit_activity_period(profile, activity, rules)
        add_targets(profile, activity, rules)
        add_rule_ttps(profile, activity, rules, attack)
        add_victim_case(profile, activity, rules)
    profile["ttps"].sort(key=lambda item: item["ttp_id"])
    profile["activities"].sort(key=lambda item: item["activity_id"])
    profile["victim_cases"].sort(key=lambda item: item["victim_case_id"])
    for category in ("countries", "regions", "sectors", "roles"):
        profile["targets"][category].sort(key=lambda item: item["id"])
    materialize_profile_diamonds(profile)
    return profile_stats(profile)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profiles_root", nargs="?", type=Path, default=DEFAULT_PROFILES)
    parser.add_argument("--rules", type=Path, default=DEFAULT_RULES)
    parser.add_argument("--attack-index", type=Path, default=DEFAULT_ATTACK)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument(
        "--actor",
        action="append",
        default=[],
        help="Limit processing to one or more profile slugs.",
    )
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    catalog = load_json(args.catalog)
    rules = compile_rules(load_json(args.rules), catalog)
    attack = load_json(args.attack_index)
    group_ids = catalog_group_map(catalog)
    rows: list[dict[str, Any]] = []
    changed = 0
    for path in sorted(args.profiles_root.glob("*/actor-profile.json")):
        if args.actor and path.parent.name not in set(args.actor):
            continue
        profile = load_json(path)
        before = json.dumps(profile, ensure_ascii=False, sort_keys=True)
        slug = path.parent.name
        group = attack.get("groups", {}).get(group_ids.get(slug, ""))
        stats = enrich_profile(profile, rules, attack, group)
        after = json.dumps(profile, ensure_ascii=False, sort_keys=True)
        is_changed = before != after
        if is_changed:
            changed += 1
            if args.apply:
                profile["updated_at"] = utc_now()
                write_json_atomic(path, profile)
        rows.append({"slug": slug, "changed": is_changed, **stats})

    summary = {
        "mode": "apply" if args.apply else "dry-run",
        "profiles_scanned": len(rows),
        "profiles_changed": changed,
        "profiles_with_victim_cases": sum(row["victim_cases"] > 0 for row in rows),
        "dated_activities": sum(row["dated_activities"] for row in rows),
        "victim_cases": sum(row["victim_cases"] for row in rows),
        "named_victim_cases": sum(row["named_victim_cases"] for row in rows),
        "disputed_victim_cases": sum(
            row["disputed_victim_cases"] for row in rows
        ),
        "profiles_with_activity_linked_ttps": sum(
            row["activity_linked_ttps"] > 0 for row in rows
        ),
        "profiles_with_targets": sum(row["targets"] > 0 for row in rows),
        "targets": sum(row["targets"] for row in rows),
        "activity_linked_ttps": sum(row["activity_linked_ttps"] for row in rows),
        "dated_activity_linked_ttps": sum(
            row["dated_activity_linked_ttps"] for row in rows
        ),
        "activity_target_refs": sum(row["activity_target_refs"] for row in rows),
        "activity_malware_refs": sum(row["activity_malware_refs"] for row in rows),
    }
    report = {"summary": summary, "profiles": rows}
    if args.report:
        write_json_atomic(args.report, report)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
