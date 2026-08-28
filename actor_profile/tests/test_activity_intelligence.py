#!/usr/bin/env python3
"""Regression tests for activity-scoped intelligence enrichment."""

from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path


FRAMEWORK = Path(__file__).resolve().parents[1]
SCRIPTS = FRAMEWORK / "scripts"
sys.path.insert(0, str(SCRIPTS))

from common import unknown_time  # noqa: E402
from enrich_activity_intelligence import (  # noqa: E402
    add_rule_ttps,
    enrich_profile,
    add_targets,
    add_victim_case,
    add_mitre_group_targets,
    compile_rules,
    contains_evidence_reference,
    enrich_explicit_activity_period,
)
from migrate_activity_model import migrate  # noqa: E402


def load_fixture(name: str) -> dict:
    return json.loads((FRAMEWORK / name).read_text(encoding="utf-8"))


class ActivityIntelligenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rules = compile_rules(
            load_fixture("activity-observation-rules.json"),
            load_fixture("corpus-catalog.json"),
        )
        cls.attack = load_fixture("reference/attack-index.json")

    def profile(self, name: str, aliases: list[str] | None = None) -> dict:
        return {
            "name": name,
            "actor": {
                "canonical_name": name,
                "aliases": [{"name": item} for item in (aliases or [])],
            },
            "sources": [],
            "targets": {
                "countries": [],
                "regions": [],
                "sectors": [],
                "roles": [],
            },
            "capabilities": {
                "malware": [],
                "tools": [],
                "infrastructure": [],
            },
            "ttps": [],
            "victim_cases": [],
        }

    def activity(
        self,
        name: str,
        description: str,
        activity_type: str = "intrusion",
    ) -> dict:
        return {
            "activity_id": "activity--test",
            "name": name,
            "description": description,
            "activity_type": activity_type,
            "first_observed": unknown_time(),
            "last_observed": unknown_time(),
            "reported_at": {
                "value": "2026-07-29T00:00:00Z",
                "precision": "day",
                "status": "known",
                "basis": "report-publication-date",
            },
            "target_refs": [],
            "malware_refs": [],
            "ttp_refs": [],
            "victim_refs": [],
            "confidence": "medium",
            "evidence_refs": ["source--test"],
            "analyst_notes": "",
        }

    def test_law_enforcement_activity_does_not_generate_victim_case(self) -> None:
        """逮捕・起訴の記事から被害事例とTTPを合成しない（RULES.md 4.3-3）。"""
        profile = self.profile("TeamPCP")
        profile["activities"] = [
            self.activity(
                "TeamPCPのメンバーとされるハッカー2人、オーストラリアで逮捕",
                "オーストラリア連邦警察は、サプライチェーン攻撃で組織を侵害したとして"
                "TeamPCPの主要関与者2名を逮捕・起訴した。",
                activity_type="law-enforcement-action",
            )
        ]

        enrich_profile(profile, self.rules, self.attack, None)

        self.assertEqual(profile["victim_cases"], [])
        self.assertEqual(profile["activities"][0]["victim_refs"], [])
        self.assertEqual(profile["activities"][0]["ttp_refs"], [])
        self.assertEqual(profile["activities"][0]["target_refs"], [])

    def test_same_text_as_attack_activity_still_generates_victim_case(self) -> None:
        """除外は活動種別によるものであり、本文の抑制ではないことを示す対照。"""
        profile = self.profile("TeamPCP")
        profile["activities"] = [
            self.activity(
                "TeamPCPがサプライチェーン攻撃で組織を侵害",
                "オーストラリア連邦警察は、サプライチェーン攻撃で組織を侵害したとして"
                "TeamPCPの主要関与者2名を逮捕・起訴した。",
                activity_type="intrusion",
            )
        ]

        enrich_profile(profile, self.rules, self.attack, None)

        self.assertNotEqual(profile["victim_cases"], [])

    def test_multi_actor_article_does_not_mix_following_actor_behavior(self) -> None:
        profile = self.profile("Kimsuky", ["TA427"])
        activity = self.activity(
            "複数アクターの活動",
            (
                "Kimsuky: ClickFixで利用者にコマンドを実行させた。"
                " MuddyWater: PowerShellを使用してペイロードを展開した。"
            ),
        )

        add_rule_ttps(profile, activity, self.rules, self.attack)

        technique_ids = {item["technique_id"] for item in profile["ttps"]}
        self.assertIn("T1204.004", technique_ids)
        self.assertNotIn("T1059.001", technique_ids)

    def test_attribution_country_is_not_added_as_victim_country(self) -> None:
        profile = self.profile("APT41")
        activity = self.activity(
            "台湾の研究所への攻撃",
            "中国関連のAPT41が台湾政府関連の研究所を標的にして侵害した。",
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("台湾", countries)
        self.assertNotIn("中国", countries)

    def test_nationality_of_perpetrators_is_not_a_victim_country(self) -> None:
        profile = self.profile("Silent Librarian")
        activity = self.activity(
            "米国、知的財産窃取に関与したイラン人ハッカーを起訴",
            (
                "米司法省は、Mabna Instituteに所属するとされるイラン人17人を、"
                "米国の大学から長年データを窃取したとして起訴した。"
            ),
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("米国", countries)
        self.assertNotIn("イラン", countries)

    def test_nationality_of_victims_is_still_a_victim_country(self) -> None:
        profile = self.profile("Kimsuky")
        activity = self.activity(
            "日本人利用者への攻撃",
            "Kimsukyは日本人を標的にしたフィッシングで日本の研究機関を侵害した。",
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("日本", countries)

    def test_every_country_in_target_list_is_added(self) -> None:
        profile = self.profile("Lazarus Group")
        activity = self.activity(
            "Operation Dream Job",
            (
                "Lazarus Group targeted the defense and aerospace sectors in "
                "the United States, Israel, Australia, Russia, and India."
            ),
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertEqual(
            countries,
            {"米国", "イスラエル", "オーストラリア", "ロシア", "インド"},
        )

    def test_mitre_group_summary_adds_targets_but_not_attribution_country(self) -> None:
        profile = self.profile("Axiom", ["Group 72"])
        group = {
            "external_id": "G0001",
            "description": (
                "Axiom is a suspected Chinese cyber espionage group that has "
                "targeted the aerospace, defense, government, manufacturing, "
                "and media sectors in the United States."
            ),
        }

        count = add_mitre_group_targets(profile, group, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        sectors = {item["name"] for item in profile["targets"]["sectors"]}
        self.assertGreater(count, 0)
        self.assertIn("米国", countries)
        self.assertNotIn("中国", countries)
        self.assertIn("防衛・軍事", sectors)
        self.assertIn("政府・行政", sectors)
        self.assertIn("製造・産業", sectors)
        self.assertIn("メディア・報道", sectors)

    def test_mitre_adjectival_attribution_country_is_not_a_target(self) -> None:
        profile = self.profile("SideCopy")
        group = {
            "external_id": "G1008",
            "description": (
                "SideCopy is a Pakistani threat group that has primarily "
                "targeted Indian government personnel since at least 2019."
            ),
        }

        add_mitre_group_targets(profile, group, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("インド", countries)
        self.assertNotIn("パキスタン", countries)

    def test_existing_mitre_evidence_reference_is_detected(self) -> None:
        profile = self.profile("APT43")
        profile["relationships"] = [
            {"evidence_refs": ["source--mitre-attack-19-1"]}
        ]

        self.assertTrue(
            contains_evidence_reference(
                profile,
                "source--mitre-attack-19-1",
            )
        )

    def test_publication_date_is_not_used_as_observation_date(self) -> None:
        profile = self.profile("APT41")
        activity = self.activity(
            "期間不明の攻撃",
            "APT41が研究機関を標的にしたことをレポートが報告した。",
        )

        changed = enrich_explicit_activity_period(profile, activity, self.rules)

        self.assertFalse(changed)
        self.assertIsNone(activity["first_observed"]["value"])
        self.assertIsNone(activity["last_observed"]["value"])

    def test_explicit_activity_period_is_structured(self) -> None:
        profile = self.profile("APT41")
        activity = self.activity(
            "明示期間のある攻撃",
            "攻撃は2023年11月から2024年7月にかけて観測された。",
        )

        changed = enrich_explicit_activity_period(profile, activity, self.rules)

        self.assertTrue(changed)
        self.assertEqual(
            activity["first_observed"]["value"],
            "2023-11-01T00:00:00Z",
        )
        self.assertEqual(
            activity["last_observed"]["value"],
            "2024-07-01T00:00:00Z",
        )

    def test_month_pair_activity_period_is_structured(self) -> None:
        profile = self.profile("Kimsuky")
        activity = self.activity(
            "Durianを使用した攻撃",
            "攻撃は2023年8月と11月に発生した。",
        )

        changed = enrich_explicit_activity_period(profile, activity, self.rules)

        self.assertTrue(changed)
        self.assertEqual(
            activity["first_observed"]["value"],
            "2023-08-01T00:00:00Z",
        )
        self.assertEqual(
            activity["last_observed"]["value"],
            "2023-11-01T00:00:00Z",
        )

    def test_single_observed_month_is_structured(self) -> None:
        profile = self.profile("Kimsuky")
        activity = self.activity(
            "DOCSWAPキャンペーン",
            "2025年9月に観測された攻撃でDOCSWAPを展開した。",
        )

        changed = enrich_explicit_activity_period(profile, activity, self.rules)

        self.assertTrue(changed)
        self.assertEqual(
            activity["first_observed"]["value"],
            "2025-09-01T00:00:00Z",
        )
        self.assertEqual(
            activity["last_observed"]["value"],
            "2025-09-01T00:00:00Z",
        )

    def test_half_year_activity_period_is_structured(self) -> None:
        profile = self.profile("Kimsuky")
        activity = self.activity(
            "上半期のキャンペーン",
            "2026年上半期に4件のスピアフィッシング攻撃を実行した。",
        )

        changed = enrich_explicit_activity_period(profile, activity, self.rules)

        self.assertTrue(changed)
        self.assertEqual(
            activity["first_observed"]["value"],
            "2026-01-01T00:00:00Z",
        )
        self.assertEqual(
            activity["last_observed"]["value"],
            "2026-06-01T00:00:00Z",
        )

    def test_denied_breach_claim_is_kept_as_disputed_victim_case(self) -> None:
        profile = self.profile("Akira")
        activity = self.activity(
            "Example Corp、データ侵害主張を否定",
            (
                "AkiraがExample Corpを侵害したと主張したが、"
                "Example Corpはデータ侵害主張を否定した。"
            ),
            activity_type="ransomware-extortion",
        )

        victim_id = add_victim_case(profile, activity, self.rules)

        self.assertIsNotNone(victim_id)
        self.assertEqual(profile["victim_cases"][0]["case_status"], "disputed")
        self.assertEqual(profile["victim_cases"][0]["victim_name"], "Example Corp")
        self.assertIn(victim_id, activity["victim_refs"])

    def test_publication_date_is_removed_from_observation_field(self) -> None:
        activity = self.activity(
            "旧形式の活動",
            "攻撃時期は資料に記載されていない。",
        )
        activity["last_observed"] = {
            "value": "2025-05-01T00:00:00Z",
            "precision": "month",
            "status": "known",
            "basis": "source-publication",
        }
        profile = {
            "schema_version": "1.2.0",
            "activities": [activity],
            "ttps": [],
            "victim_cases": [],
        }

        migrated, changed = migrate(profile)

        self.assertTrue(changed)
        self.assertIsNone(
            migrated["activities"][0]["last_observed"]["value"]
        )
        self.assertIn(
            "last_observed=2025-05-01T00:00:00Z",
            migrated["activities"][0]["analyst_notes"],
        )
        self.assertEqual(
            migrated["activities"][0]["reported_at"]["value"],
            "2026-07-29T00:00:00Z",
        )


if __name__ == "__main__":
    unittest.main()
