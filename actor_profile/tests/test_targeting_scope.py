#!/usr/bin/env python3
"""Regression tests for corpus-wide target-geography auditing."""

from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path


FRAMEWORK = Path(__file__).resolve().parents[1]
SCRIPTS = FRAMEWORK / "scripts"
sys.path.insert(0, str(SCRIPTS))

from enrich_activity_intelligence import compile_rules  # noqa: E402
from enrich_targeting_scope import (  # noqa: E402
    Geography,
    collect_reviewed_targeting_text,
    process_profile,
)


def load_fixture(name: str) -> dict:
    return json.loads((FRAMEWORK / name).read_text(encoding="utf-8"))


class TargetingScopeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.geography = Geography(load_fixture("target-geography.json"))
        cls.rules = compile_rules(
            load_fixture("activity-observation-rules.json"),
            load_fixture("corpus-catalog.json"),
        )
        cls.curation = load_fixture("targeting-curation.json")["actors"]

    @staticmethod
    def profile(name: str, slug: str) -> dict:
        return {
            "schema_version": "1.2.0",
            "profile_id": f"actor--{slug}",
            "name": name,
            "actor": {"canonical_name": name, "aliases": []},
            "sources": [],
            "activities": [],
            "victim_cases": [],
            "targets": {
                "countries": [],
                "regions": [],
                "sectors": [],
                "roles": [],
                "selection_logic": "",
                "analyst_notes": "",
            },
            "free_text": {"targeting_details": ""},
        }

    def _arrest_profile(self, activity_type: str) -> dict:
        profile = self.profile("TeamPCP", "teampcp")
        profile["activities"] = [
            {
                "activity_id": "activity--test-arrest",
                "name": "TeamPCPのメンバーとされるハッカー2人、オーストラリアで逮捕",
                "description": (
                    "オーストラリア当局は、長期にわたるソフトウェアサプライチェーン攻撃で"
                    "知られるTeamPCPのメンバーとみられる男性2人を逮捕した。"
                    "同グループはオーストラリアの組織を含む被害を広げてきた。"
                ),
                "activity_type": activity_type,
                "target_refs": [],
                "malware_refs": [],
                "ttp_refs": [],
                "victim_refs": [],
                "evidence_refs": ["source--test"],
            }
        ]
        return profile

    def test_law_enforcement_activity_does_not_add_arrest_country_as_target(
        self,
    ) -> None:
        """摘発が行われた国を標的国として取り込まない（RULES.md 4.3-3）。"""
        profile = self._arrest_profile("law-enforcement-action")

        process_profile(
            profile,
            slug="teampcp",
            geography=self.geography,
            compiled_rules=self.rules,
            group=None,
            crosscheck=None,
            dataset_indexes={},
            curation=None,
        )

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertNotIn("オーストラリア", countries)

    def test_same_text_as_attack_activity_still_adds_country(self) -> None:
        """除外は活動種別によるものであり、本文の抑制ではないことを示す対照。"""
        profile = self._arrest_profile("intrusion")

        process_profile(
            profile,
            slug="teampcp",
            geography=self.geography,
            compiled_rules=self.rules,
            group=None,
            crosscheck=None,
            dataset_indexes={},
            curation=None,
        )

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("オーストラリア", countries)

    def test_structured_value_classifies_country_region_and_not_organization(
        self,
    ) -> None:
        countries, regions = self.geography.classify_value("Japan")
        self.assertEqual(countries, {"日本"})
        self.assertEqual(regions, set())

        countries, regions = self.geography.classify_value("Worldwide")
        self.assertEqual(countries, set())
        self.assertEqual(regions, {"全世界"})

        countries, regions = self.geography.classify_value(
            "World Anti-Doping Agency"
        )
        self.assertEqual(countries, set())
        self.assertEqual(regions, set())

    def test_attribution_country_is_not_read_as_target_from_mitre_summary(
        self,
    ) -> None:
        profile = self.profile("Example Group", "example")
        group = {
            "external_id": "G9999",
            "description": (
                "Example Group is a Chinese cyber espionage group that has "
                "targeted government organizations in Japan and the United States."
            ),
        }

        process_profile(
            profile,
            slug="example",
            geography=self.geography,
            compiled_rules=self.rules,
            group=group,
            crosscheck=None,
            dataset_indexes={},
            curation=None,
        )

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertEqual(countries, {"日本", "米国"})

    def test_reviewed_targeting_text_structures_us_without_matching_pronoun(
        self,
    ) -> None:
        profile = self.profile("Example Group", "example")
        profile["sources"].append({"source_id": "source--actor-mapping-workbook"})
        profile["free_text"]["targeting_details"] = (
            "US and Israeli defense companies in the Middle East"
        )
        countries: dict = {}
        regions: dict = {}

        collect_reviewed_targeting_text(
            profile,
            self.geography,
            countries,
            regions,
        )

        self.assertEqual(set(countries), {"米国", "イスラエル"})
        self.assertEqual(set(regions), {"中東"})

        profile["free_text"]["targeting_details"] = "Companies asked us for help"
        countries = {}
        regions = {}
        collect_reviewed_targeting_text(
            profile,
            self.geography,
            countries,
            regions,
        )
        self.assertEqual(countries, {})

    def test_apt10_primary_source_curation_preserves_japan_and_global_scope(
        self,
    ) -> None:
        profile = self.profile("menuPass", "menupass")

        report = process_profile(
            profile,
            slug="menupass",
            geography=self.geography,
            compiled_rules=self.rules,
            group=None,
            crosscheck=None,
            dataset_indexes={},
            curation=copy.deepcopy(self.curation["menupass"]),
        )

        countries = {item["name"] for item in profile["targets"]["countries"]}
        regions = {item["name"] for item in profile["targets"]["regions"]}
        self.assertTrue(
            {
                "日本",
                "米国",
                "英国",
                "インド",
                "ブラジル",
                "アラブ首長国連邦",
            }.issubset(countries)
        )
        self.assertIn("全世界", regions)
        self.assertNotIn("japan-only", report["flags"])
        source_ids = {item["source_id"] for item in profile["sources"]}
        self.assertEqual(
            source_ids,
            {
                "source--doj-apt10-global-campaign-2018",
                "source--uk-apt10-global-campaign-2018",
            },
        )


if __name__ == "__main__":
    unittest.main()
