#!/usr/bin/env python3
"""Render canonical actor profile JSON into Markdown and STIX 2.1."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
from typing import Any

from common import load_json, stable_digest, write_json_atomic


TLP_CLEAR = "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487"


def md_escape(value: Any) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", "<br>")


def time_label(point: dict[str, Any]) -> str:
    if not point or point.get("status") == "unknown":
        return "不明"
    value = point.get("value", "")
    precision = point.get("precision")
    if precision == "year":
        return value[:4]
    if precision == "month":
        return value[:7]
    if precision == "day":
        return value[:10]
    return value


def confidence_label(value: str) -> str:
    return {
        "high": "高",
        "medium": "中",
        "low": "低",
        "unknown": "不明",
    }.get(value, value)


def source_map(profile: dict[str, Any]) -> dict[str, str]:
    return {
        source["source_id"]: source.get("title") or source.get("path")
        for source in profile.get("sources", [])
    }


def refs_label(refs: list[str], sources: dict[str, str]) -> str:
    return ", ".join(f"`{ref}`" for ref in refs) if refs else "なし"


def table(headers: list[str], rows: list[list[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "|" + "|".join("---" for _ in headers) + "|",
    ]
    lines.extend(
        "| " + " | ".join(md_escape(cell) for cell in row) + " |" for row in rows
    )
    return "\n".join(lines)


def render_markdown(
    profile: dict[str, Any],
    iocs: dict[str, Any] | None,
    artifacts_path: Path | None,
    crosscheck: dict[str, Any] | None = None,
) -> str:
    sources = source_map(profile)
    actor = profile["actor"]
    lines = [
        f"# {profile['name']} 脅威アクタープロファイル",
        "",
        f"- プロファイルID: `{profile['profile_id']}`",
        f"- 状態: {profile['status']}",
        f"- 更新日時: {profile['updated_at']}",
        f"- 構造バージョン: {profile['schema_version']}",
        "",
        "## エグゼクティブサマリー",
        "",
        profile["free_text"].get("executive_summary") or actor.get("description") or "未記入",
        "",
        "## アクター名とAlias",
        "",
        f"- 正規名: **{actor['canonical_name']}**",
        f"- 初回観測: {time_label(actor['first_seen'])}",
        f"- 最終観測: {time_label(actor['last_seen'])}",
        f"- 活動状態: {actor['active']}",
        "",
    ]
    alias_rows = [
        [
            alias["name"],
            alias.get("vendor", ""),
            alias.get("scope", ""),
            confidence_label(alias.get("confidence", "unknown")),
            refs_label(alias.get("evidence_refs", []), sources),
            alias.get("analyst_notes", ""),
        ]
        for alias in actor.get("aliases", [])
    ]
    lines.extend(
        [
            table(
                ["Alias", "追跡元", "スコープ", "確度", "証拠", "補足"],
                alias_rows,
            )
            if alias_rows
            else "Aliasなし",
            "",
            "## 帰属",
            "",
            profile["attribution"].get("assessment") or "未評価",
            "",
            f"- 国: {', '.join(profile['attribution'].get('countries', [])) or '不明'}",
            f"- スポンサー種別: {profile['attribution'].get('sponsor_type', 'unknown')}",
            f"- 確度: {confidence_label(profile['attribution'].get('confidence', 'unknown'))}",
            f"- 証拠: {refs_label(profile['attribution'].get('evidence_refs', []), sources)}",
            "",
            "## モチベーション",
            "",
        ]
    )
    motivation_rows = [
        [
            item["type"],
            item["description"],
            confidence_label(item["confidence"]),
            refs_label(item["evidence_refs"], sources),
            item.get("analyst_notes", ""),
        ]
        for item in profile.get("motivations", [])
    ]
    lines.extend(
        [
            table(["種別", "説明", "確度", "証拠", "補足"], motivation_rows)
            if motivation_rows
            else "未評価",
            "",
            "## 他アクターとの関係",
            "",
        ]
    )
    relationship_rows = [
        [
            item["target_actor"],
            item["relationship_type"],
            item["description"],
            confidence_label(item["confidence"]),
            refs_label(item["evidence_refs"], sources),
        ]
        for item in profile.get("relationships", [])
    ]
    lines.extend(
        [
            table(["対象", "関係", "説明", "確度", "証拠"], relationship_rows)
            if relationship_rows
            else "確認された関係なし",
            "",
            "## ダイヤモンドモデル",
            "",
            table(
                ["要素", "内容"],
                [
                    ["Adversary", profile["diamond_model"]["adversary"]],
                    ["Capability", profile["diamond_model"]["capability"]],
                    ["Infrastructure", profile["diamond_model"]["infrastructure"]],
                    ["Victim", profile["diamond_model"]["victim"]],
                    ["Socio-political", profile["diamond_model"]["socio_political"]],
                ],
            ),
            "",
        ]
    )
    if crosscheck:
        match_rows = []
        for dataset_id, matches in crosscheck.get("actor_matches", {}).items():
            if not matches:
                match_rows.append(
                    [dataset_id, "一致なし", "", "", "", ""]
                )
                continue
            for match in matches:
                match_rows.append(
                    [
                        dataset_id,
                        match.get("entry_value", ""),
                        match.get("match_basis", ""),
                        confidence_label(match.get("match_confidence", "unknown")),
                        ", ".join(match.get("countries", [])),
                        "<br>".join(match.get("refs", [])[:3]),
                    ]
                )
        candidate_rows = [
            [
                item.get("target_actor", ""),
                item.get("relationship_type", ""),
                item.get("dataset_id", ""),
                confidence_label(item.get("confidence", "unknown")),
                item.get("assessment", ""),
            ]
            for item in crosscheck.get("relationship_candidates", [])
        ]
        lines.extend(
            [
                "## OSINTクロスチェック",
                "",
                f"- 判定: `{crosscheck.get('overall_assessment', 'unknown')}`",
                f"- 調査日時: {crosscheck.get('searched_at', '不明')}",
                (
                    "- 国別メタデータ衝突: "
                    + (
                        "あり"
                        if crosscheck.get("country_comparison", {}).get("conflict")
                        else "なし"
                    )
                ),
                (
                    "- 複数taxonomyスコープ: "
                    + (
                        "あり"
                        if crosscheck.get("ambiguities", {}).get(
                            "scope_divergence_detected"
                        )
                        else "なし"
                    )
                ),
                "",
                table(
                    ["データセット", "一致エントリ", "根拠", "確度", "帰属候補", "原典URL"],
                    match_rows,
                ),
                "",
                "### 関係性候補（未統合）",
                "",
                table(
                    ["対象", "関係", "データセット", "確度", "評価"],
                    candidate_rows,
                )
                if candidate_rows
                else "候補なし",
                "",
                "### クロスチェック上の制約",
                "",
                *[
                    f"- {item}"
                    for item in crosscheck.get("limitations", [])
                ],
                "",
            ]
        )
    lines.extend(["## Capability", ""])
    for category, label in [
        ("malware", "マルウェア"),
        ("tools", "ツール"),
        ("infrastructure", "インフラ"),
        ("delivery_formats", "配送・ファイル形式"),
        ("vulnerabilities", "脆弱性"),
        ("operational_capabilities", "運用能力"),
    ]:
        items = profile["capabilities"].get(category, [])
        lines.extend([f"### {label}", ""])
        if not items:
            lines.extend(["未確認", ""])
            continue
        lines.extend(
            [
                table(
                    ["ID", "名称", "説明", "初回", "最終", "確度", "証拠"],
                    [
                        [
                            item["id"],
                            item["name"],
                            item["description"],
                            time_label(item["first_observed"]),
                            time_label(item["last_observed"]),
                            confidence_label(item["confidence"]),
                            refs_label(item["evidence_refs"], sources),
                        ]
                        for item in items
                    ],
                ),
                "",
            ]
        )
    lines.extend(["## 攻撃活動の履歴", ""])
    activity_rows = [
        [
            item["name"],
            item["activity_type"],
            time_label(item["first_observed"]),
            time_label(item["last_observed"]),
            time_label(item["reported_at"]),
            item["description"],
            confidence_label(item["confidence"]),
            refs_label(item["evidence_refs"], sources),
        ]
        for item in profile.get("activities", [])
    ]
    lines.extend(
        [
            table(
                ["活動", "種別", "初回", "最終", "報告日", "説明", "確度", "証拠"],
                activity_rows,
            )
            if activity_rows
            else "活動履歴なし",
            "",
            profile["free_text"].get("history", ""),
            "",
            "## ターゲット",
            "",
        ]
    )
    target_rows = []
    for category in ("countries", "regions", "sectors", "roles"):
        for item in profile["targets"].get(category, []):
            target_rows.append(
                [
                    category,
                    item["name"],
                    item["description"],
                    time_label(item["first_observed"]),
                    time_label(item["last_observed"]),
                    confidence_label(item["confidence"]),
                    refs_label(item["evidence_refs"], sources),
                ]
            )
    lines.extend(
        [
            table(
                ["分類", "名称", "説明", "初回", "最終", "確度", "証拠"],
                target_rows,
            )
            if target_rows
            else "ターゲット情報なし",
            "",
            f"選定ロジック: {profile['targets'].get('selection_logic') or '未評価'}",
            "",
            "## MITRE ATT&CK Matrixデータ",
            "",
        ]
    )
    ttp_rows = [
        [
            item["tactic"],
            item["technique_id"],
            item["technique_name"],
            item["observed_behavior"],
            ", ".join(item["malware_refs"]),
            ", ".join(item["activity_refs"]),
            time_label(item["first_observed"]),
            time_label(item["last_observed"]),
            confidence_label(item["confidence"]),
            refs_label(item["evidence_refs"], sources),
        ]
        for item in profile.get("ttps", [])
    ]
    lines.extend(
        [
            table(
                [
                    "Tactic", "Technique ID", "Technique", "観測内容",
                    "マルウェア", "活動", "初回", "最終", "確度", "証拠",
                ],
                ttp_rows,
            )
            if ttp_rows
            else "TTPなし",
            "",
            "## IOC／artifact概要",
            "",
        ]
    )
    if iocs:
        indicators = iocs.get("indicators", [])
        lines.extend(
            [
                f"- IOC値: {len(indicators)}件",
                f"- IOC観測: {sum(item['observation_count'] for item in indicators)}件",
                f"- 複数攻撃で観測: {sum(item['seen_in_multiple_campaigns'] for item in indicators)}件",
                f"- 要レビュー候補: {sum(item['disposition'] == 'candidate' for item in indicators)}件",
            ]
        )
    else:
        lines.append("- IOCデータ未指定")
    if artifacts_path and artifacts_path.exists():
        with artifacts_path.open("r", encoding="utf-8-sig", newline="") as stream:
            artifact_count = sum(1 for _ in csv.DictReader(stream))
        lines.append(f"- 非IOC artifact観測: {artifact_count}件（`artifacts.csv`）")
    else:
        lines.append("- artifactデータ未指定")
    lines.extend(["", "## 主要判断と不確実性", ""])
    judgment_rows = [
        [
            item["statement"],
            confidence_label(item["confidence"]),
            refs_label(item["evidence_refs"], sources),
            item.get("analyst_notes", ""),
        ]
        for item in profile["assessment"].get("key_judgments", [])
    ]
    lines.extend(
        [
            table(["判断", "確度", "証拠", "補足"], judgment_rows)
            if judgment_rows
            else "主要判断なし",
            "",
            "### 情報ギャップ",
            "",
            *[f"- {item}" for item in profile["assessment"].get("gaps", [])],
            "",
            "### 不確実性",
            "",
            *[f"- {item}" for item in profile["assessment"].get("uncertainties", [])],
            "",
            "## 出典",
            "",
        ]
    )
    source_rows = [
        [
            item["source_id"],
            item["title"],
            item["publisher"],
            time_label(item["published_at"]),
            item["path"],
            item["source_type"],
            item["tlp"],
            confidence_label(item["reliability"]),
        ]
        for item in profile.get("sources", [])
    ]
    lines.extend(
        [
            table(
                ["Source ID", "タイトル", "発行者", "発行日", "パス", "種別", "TLP", "信頼度"],
                source_rows,
            )
            if source_rows
            else "出典なし",
            "",
            "## 自由記述",
            "",
            profile["free_text"].get("additional_notes") or "なし",
            "",
        ]
    )
    return "\n".join(lines)


def stable_uuid_v4(name: str) -> str:
    raw = bytearray(hashlib.sha256(name.encode("utf-8")).digest()[:16])
    raw[6] = (raw[6] & 0x0F) | 0x40
    raw[8] = (raw[8] & 0x3F) | 0x80
    value = raw.hex()
    return f"{value[:8]}-{value[8:12]}-{value[12:16]}-{value[16:20]}-{value[20:]}"


def stix_id(kind: str, key: str) -> str:
    return f"{kind}--{stable_uuid_v4(f'actor-profile:{kind}:{key}')}"


def stix_base(kind: str, key: str, now: str, extra: dict[str, Any]) -> dict[str, Any]:
    return {
        "type": kind,
        "spec_version": "2.1",
        "id": stix_id(kind, key),
        "created": now,
        "modified": now,
        "object_marking_refs": [TLP_CLEAR],
        **extra,
    }


def external_refs(
    evidence_refs: list[str], source_by_id: dict[str, dict[str, Any]]
) -> list[dict[str, Any]]:
    result = []
    for source_id in evidence_refs:
        source = source_by_id.get(source_id)
        if not source:
            continue
        result.append(
            {
                "source_name": source.get("publisher") or source_id,
                "description": f"Local source: {source.get('path', '')}",
                "external_id": source_id,
            }
        )
    return result


def render_stix(
    profile: dict[str, Any],
    iocs: dict[str, Any] | None,
    artifacts_path: Path | None,
    crosscheck: dict[str, Any] | None = None,
    previous_bundle: dict[str, Any] | None = None,
) -> dict[str, Any]:
    # Use the canonical profile timestamp so repeated rendering is byte-stable.
    now = profile["updated_at"]
    previous_by_id = {
        item["id"]: item
        for item in (previous_bundle or {}).get("objects", [])
    }
    objects: list[dict[str, Any]] = []
    source_by_id = {item["source_id"]: item for item in profile["sources"]}
    actor = profile["actor"]
    intrusion = stix_base(
        "intrusion-set",
        profile["profile_id"],
        now,
        {
            "name": actor["canonical_name"],
            "aliases": [item["name"] for item in actor["aliases"]],
            "description": actor.get("description") or profile["free_text"]["executive_summary"],
            "first_seen": actor["first_seen"].get("value"),
            "last_seen": actor["last_seen"].get("value"),
            "goals": [item["description"] for item in profile["motivations"]],
            "external_references": external_refs(
                profile["attribution"].get("evidence_refs", []), source_by_id
            ),
            "x_profile_id": profile["profile_id"],
            "x_alias_assessments": actor["aliases"],
            "x_attribution": profile["attribution"],
            "x_free_text": profile["free_text"],
        },
    )
    for key in ("first_seen", "last_seen"):
        if intrusion[key] is None:
            del intrusion[key]
    if crosscheck:
        intrusion["x_osint_crosscheck"] = crosscheck
    objects.append(intrusion)

    object_id_by_profile_id: dict[str, str] = {
        profile["profile_id"]: intrusion["id"]
    }
    capability_kind = {
        "malware": "malware",
        "tools": "tool",
        "infrastructure": "infrastructure",
    }
    for category, stix_kind in capability_kind.items():
        for item in profile["capabilities"][category]:
            common = {
                "name": item["name"],
                "description": item["description"],
                "external_references": external_refs(item["evidence_refs"], source_by_id),
                "x_profile_object_id": item["id"],
                "x_confidence": item["confidence"],
                "x_analyst_notes": item.get("analyst_notes", ""),
            }
            if stix_kind == "malware":
                common.update(
                    {
                        "is_family": True,
                        "malware_types": item.get("types") or ["unknown"],
                        "aliases": item.get("aliases", []),
                    }
                )
            elif stix_kind == "tool":
                common["tool_types"] = item.get("types") or ["unknown"]
            else:
                common["infrastructure_types"] = item.get("types") or ["unknown"]
            obj = stix_base(stix_kind, item["id"], now, common)
            objects.append(obj)
            object_id_by_profile_id[item["id"]] = obj["id"]

    for activity in profile["activities"]:
        obj = stix_base(
            "campaign",
            activity["activity_id"],
            now,
            {
                "name": activity["name"],
                "description": activity["description"],
                "first_seen": activity["first_observed"].get("value"),
                "last_seen": activity["last_observed"].get("value"),
                "external_references": external_refs(activity["evidence_refs"], source_by_id),
                "x_profile_object_id": activity["activity_id"],
                "x_confidence": activity["confidence"],
                "x_analyst_notes": activity.get("analyst_notes", ""),
                "x_reported_at": activity["reported_at"],
            },
        )
        for key in ("first_seen", "last_seen"):
            if obj[key] is None:
                del obj[key]
        objects.append(obj)
        object_id_by_profile_id[activity["activity_id"]] = obj["id"]

    for category in ("countries", "regions", "sectors", "roles"):
        for target in profile["targets"][category]:
            obj = stix_base(
                "identity",
                target["id"],
                now,
                {
                    "name": target["name"],
                    "identity_class": "organization",
                    "description": target["description"],
                    "external_references": external_refs(target["evidence_refs"], source_by_id),
                    "x_target_category": category,
                    "x_confidence": target["confidence"],
                },
            )
            objects.append(obj)
            object_id_by_profile_id[target["id"]] = obj["id"]

    for ttp in profile["ttps"]:
        obj = stix_base(
            "attack-pattern",
            ttp["ttp_id"],
            now,
            {
                "name": ttp["technique_name"],
                "description": ttp["observed_behavior"],
                "external_references": [
                    {
                        "source_name": "mitre-attack",
                        "external_id": ttp["technique_id"],
                        "url": "https://attack.mitre.org/techniques/"
                        + ttp["technique_id"].replace(".", "/")
                        + "/",
                    },
                    *external_refs(ttp["evidence_refs"], source_by_id),
                ],
                "x_profile_object_id": ttp["ttp_id"],
                "x_tactic": ttp["tactic"],
                "x_activity_refs": ttp["activity_refs"],
                "x_malware_refs": ttp["malware_refs"],
                "x_infrastructure_refs": ttp["infrastructure_refs"],
                "x_first_observed": ttp["first_observed"],
                "x_last_observed": ttp["last_observed"],
                "x_confidence": ttp["confidence"],
                "x_analyst_notes": ttp.get("analyst_notes", ""),
            },
        )
        objects.append(obj)
        object_id_by_profile_id[ttp["ttp_id"]] = obj["id"]

    def add_relationship(
        source_ref: str,
        relationship_type: str,
        target_ref: str,
        description: str,
        confidence: str,
    ) -> None:
        key = f"{source_ref}:{relationship_type}:{target_ref}"
        objects.append(
            stix_base(
                "relationship",
                key,
                now,
                {
                    "relationship_type": relationship_type,
                    "source_ref": source_ref,
                    "target_ref": target_ref,
                    "description": description,
                    "x_confidence": confidence,
                },
            )
        )

    for category in ("malware", "tools", "infrastructure"):
        for item in profile["capabilities"][category]:
            add_relationship(
                intrusion["id"],
                "uses",
                object_id_by_profile_id[item["id"]],
                f"{actor['canonical_name']} uses {item['name']}.",
                item["confidence"],
            )
    for activity in profile["activities"]:
        campaign_id = object_id_by_profile_id[activity["activity_id"]]
        add_relationship(
            campaign_id,
            "attributed-to",
            intrusion["id"],
            f"{activity['name']} is attributed or linked to {actor['canonical_name']}.",
            activity["confidence"],
        )
        for ref in activity["malware_refs"] + activity["infrastructure_refs"]:
            if ref in object_id_by_profile_id:
                add_relationship(
                    campaign_id,
                    "uses",
                    object_id_by_profile_id[ref],
                    f"{activity['name']} uses {ref}.",
                    activity["confidence"],
                )
        for ref in activity["target_refs"]:
            if ref in object_id_by_profile_id:
                add_relationship(
                    campaign_id,
                    "targets",
                    object_id_by_profile_id[ref],
                    f"{activity['name']} targets {ref}.",
                    activity["confidence"],
                )
    for ttp in profile["ttps"]:
        attack_id = object_id_by_profile_id[ttp["ttp_id"]]
        add_relationship(
            intrusion["id"],
            "uses",
            attack_id,
            ttp["observed_behavior"],
            ttp["confidence"],
        )

    if iocs:
        for indicator in iocs.get("indicators", []):
            indicator_stix_id = stix_id("indicator", indicator["indicator_id"])
            previous_indicator = previous_by_id.get(indicator_stix_id, {})
            valid_from = (
                indicator["first_observed"].get("value")
                or previous_indicator.get("valid_from")
                or profile["created_at"]
            )
            obj = stix_base(
                "indicator",
                indicator["indicator_id"],
                now,
                {
                    "name": f"{indicator['type']}: {indicator['normalized_value']}",
                    "pattern": indicator["stix_pattern"],
                    "pattern_type": "stix",
                    "pattern_version": "2.1",
                    "valid_from": valid_from,
                    "indicator_types": ["malicious-activity"],
                    "description": "Repository-derived observable. Historical data; do not use as sole attribution evidence.",
                    "x_disposition": indicator["disposition"],
                    "x_observation_count": indicator["observation_count"],
                    "x_campaign_count": indicator["campaign_count"],
                    "x_seen_in_multiple_campaigns": indicator["seen_in_multiple_campaigns"],
                    "x_campaign_refs": indicator["campaign_refs"],
                    "x_malware_refs": indicator["malware_refs"],
                    "x_infrastructure_refs": indicator["infrastructure_refs"],
                    "x_roles": indicator["roles"],
                    "x_observations": indicator["observations"],
                },
            )
            objects.append(obj)
            if indicator["disposition"] == "confirmed":
                add_relationship(
                    obj["id"],
                    "indicates",
                    intrusion["id"],
                    "Confirmed repository-derived indicator associated with this actor profile.",
                    "medium",
                )

    if artifacts_path and artifacts_path.exists():
        with artifacts_path.open("r", encoding="utf-8-sig", newline="") as stream:
            artifact_count = sum(1 for _ in csv.DictReader(stream))
        objects.append(
            stix_base(
                "note",
                f"artifact-dataset:{profile['profile_id']}",
                now,
                {
                    "abstract": "Non-IOC artifact dataset",
                    "content": "Commands, sample strings, paths, registry keys, mutexes, named pipes, task/service names and other non-IOC artifacts are stored in artifacts.csv.",
                    "object_refs": [intrusion["id"]],
                    "x_artifacts_path": artifacts_path.name,
                    "x_artifact_observation_count": artifact_count,
                },
            )
        )

    report_refs = [
        obj["id"]
        for obj in objects
        if obj["type"] not in {"relationship", "note", "report"}
    ]
    objects.append(
        stix_base(
            "report",
            f"report:{profile['profile_id']}",
            now,
            {
                "name": f"{profile['name']} Threat Actor Profile",
                "description": profile["free_text"]["executive_summary"],
                "report_types": ["threat-actor"],
                "published": now,
                "object_refs": report_refs,
                "x_schema_version": profile["schema_version"],
            },
        )
    )
    if previous_bundle:
        for item in objects:
            previous = previous_by_id.get(item["id"])
            if not previous:
                continue
            item["created"] = previous.get("created", item["created"])
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
                item["modified"] = previous.get("modified", item["modified"])
    return {
        "type": "bundle",
        "id": stix_id("bundle", profile["profile_id"]),
        "objects": objects,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", type=Path)
    parser.add_argument("--iocs", type=Path)
    parser.add_argument("--artifacts", type=Path)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()

    profile_path = args.profile.resolve()
    profile = load_json(profile_path)
    iocs = load_json(args.iocs.resolve()) if args.iocs and args.iocs.exists() else None
    artifacts_path = args.artifacts.resolve() if args.artifacts else None
    crosscheck_path = profile_path.parent / "osint-crosscheck.json"
    crosscheck = load_json(crosscheck_path) if crosscheck_path.exists() else None
    output_dir = (
        args.output_dir.resolve()
        if args.output_dir
        else profile_path.parent / "generated"
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    markdown_path = output_dir / "profile-ja.md"
    stix_path = output_dir / "profile.stix2.json"
    previous_bundle = load_json(stix_path) if stix_path.exists() else None
    markdown_path.write_text(
        render_markdown(profile, iocs, artifacts_path, crosscheck),
        encoding="utf-8",
    )
    write_json_atomic(
        stix_path,
        render_stix(
            profile,
            iocs,
            artifacts_path,
            crosscheck,
            previous_bundle=previous_bundle,
        ),
    )
    print(
        json.dumps(
            {
                "markdown": str(markdown_path),
                "stix": str(stix_path),
                "stix_objects": len(load_json(stix_path)["objects"]),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
