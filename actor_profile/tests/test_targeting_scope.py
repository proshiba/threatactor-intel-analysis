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
    LEGACY_TARGET_DERIVATION_NOTE,
    LEGACY_TARGET_NOTES,
    LEGACY_TARGET_SELECTION_LOGIC,
    TARGET_DERIVATION_NOTE,
    TARGET_SELECTION_LOGIC,
    append_audit_notes,
    link_activity_target,
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
            "schema_version": "1.4.0",
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

    def test_subject_matter_region_is_not_treated_as_victim_location(self) -> None:
        countries, regions = self.geography.target_mentions(
            (
                "米国政府機関と朝鮮半島情勢に職業上関係する米国外の"
                "外国人を標的とした。"
            ),
            target_context_patterns=self.rules["_target_context_patterns"],
            actor_pattern=self.rules.get("_actor_pattern"),
            mitre=False,
        )

        self.assertEqual(countries, {"米国"})
        self.assertNotIn("東アジア", regions)

    def test_country_name_inside_filename_is_not_a_victim_location(self) -> None:
        countries, regions = self.geography.target_mentions(
            (
                "中国関連のAPTグループがASEAN加盟国を狙った。"
                "マルウェアはTalking_Points_for_China.exeを含む。"
            ),
            target_context_patterns=self.rules["_target_context_patterns"],
            actor_pattern=self.rules.get("_actor_pattern"),
            mitre=False,
        )

        self.assertNotIn("中国", countries)
        self.assertIn("東南アジア", regions)

    def test_southeast_asia_does_not_imply_south_asia_or_generic_asia(self) -> None:
        countries, regions = self.geography.target_mentions(
            "攻撃者は東南アジアの外交官を標的にした。",
            target_context_patterns=self.rules["_target_context_patterns"],
            actor_pattern=self.rules.get("_actor_pattern"),
            mitre=False,
        )

        self.assertEqual(countries, set())
        self.assertEqual(regions, {"東南アジア"})

    def test_condemning_organization_is_not_treated_as_target_region(self) -> None:
        countries, regions = self.geography.target_mentions(
            "NATOとEUはドイツへのロシアのサイバー攻撃を非難した。",
            target_context_patterns=self.rules["_target_context_patterns"],
            actor_pattern=self.rules.get("_actor_pattern"),
            mitre=False,
        )

        self.assertIn("ドイツ", countries)
        self.assertNotIn("NATO加盟国", regions)

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

    def test_workbook_targeting_text_remains_noncanonical(self) -> None:
        profile = self.profile("Example Group", "example")
        profile["sources"].append({"source_id": "source--actor-mapping-workbook"})
        profile["free_text"]["targeting_details"] = (
            "US and Israeli defense companies in the Middle East"
        )

        process_profile(
            profile,
            slug="example",
            geography=self.geography,
            compiled_rules=self.rules,
            group=None,
            crosscheck=None,
            dataset_indexes={},
            curation=None,
        )

        self.assertEqual(profile["targets"]["countries"], [])
        self.assertEqual(profile["targets"]["regions"], [])
        self.assertIn(
            "US and Israeli defense companies in the Middle East",
            profile["free_text"]["targeting_details"],
        )

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

    def test_aggregation_crosscheck_remains_external_lead_only(self) -> None:
        profile = self.profile("Example Group", "example")
        crosscheck = {
            "actor_matches": {
                "etda-threat-group-cards": [
                    {
                        "entry_uuid": "entry-1",
                        "match_confidence": "high",
                        "match_basis": "canonical-name",
                    }
                ]
            }
        }
        datasets = {
            "etda-threat-group-cards": {
                "entry-1": {
                    "uuid": "entry-1",
                    "observed-countries": ["Japan"],
                }
            }
        }

        report = process_profile(
            profile,
            slug="example",
            geography=self.geography,
            compiled_rules=self.rules,
            group=None,
            crosscheck=crosscheck,
            dataset_indexes=datasets,
            curation=None,
        )

        self.assertEqual(profile["targets"]["countries"], [])
        self.assertEqual(
            [source["source_id"] for source in profile["sources"]],
            ["source--target-audit-etda-threat-group-cards"],
        )
        self.assertEqual(
            report["external_lead_sources"],
            ["source--target-audit-etda-threat-group-cards"],
        )

    def test_activity_geography_is_linked_back_to_the_activity(self) -> None:
        profile = self.profile("Example Group", "example")
        unknown = {
            "value": None,
            "precision": "unknown",
            "status": "unknown",
            "basis": "not-stated",
        }
        profile["activities"] = [
            {
                "activity_id": "activity--example",
                "name": "Japan targeting",
                "description": "Example Group targeted organizations in Japan.",
                "first_observed": copy.deepcopy(unknown),
                "last_observed": copy.deepcopy(unknown),
                "reported_at": copy.deepcopy(unknown),
                "activity_type": "reported-activity",
                "target_refs": [],
                "malware_refs": [],
                "infrastructure_refs": [],
                "ttp_refs": [],
                "victim_refs": [],
                "confidence": "high",
                "evidence_refs": ["source--example"],
                "analyst_notes": "",
            }
        ]

        process_profile(
            profile,
            slug="example",
            geography=self.geography,
            compiled_rules=self.rules,
            group=None,
            crosscheck=None,
            dataset_indexes={},
            curation=None,
        )

        japan = next(
            item for item in profile["targets"]["countries"] if item["name"] == "日本"
        )
        self.assertIn(japan["id"], profile["activities"][0]["target_refs"])

    def test_audit_notes_replace_legacy_policy_and_are_idempotent(self) -> None:
        profile = self.profile("Example Group", "example")
        profile["targets"]["selection_logic"] = (
            f"Actor-specific note. {LEGACY_TARGET_SELECTION_LOGIC} "
            f"{TARGET_SELECTION_LOGIC}"
        )
        profile["targets"]["analyst_notes"] = (
            f"{LEGACY_TARGET_NOTES[0]} Actor-specific note. "
            f"{LEGACY_TARGET_DERIVATION_NOTE}"
        )

        append_audit_notes(profile)
        append_audit_notes(profile)

        selection_logic = profile["targets"]["selection_logic"]
        analyst_notes = profile["targets"]["analyst_notes"]
        self.assertEqual(selection_logic.count(TARGET_SELECTION_LOGIC), 1)
        self.assertNotIn(LEGACY_TARGET_SELECTION_LOGIC, selection_logic)
        self.assertEqual(analyst_notes.count(TARGET_DERIVATION_NOTE), 1)
        self.assertNotIn(LEGACY_TARGET_DERIVATION_NOTE, analyst_notes)
        self.assertNotIn(LEGACY_TARGET_NOTES[0], analyst_notes)
        self.assertIn("Actor-specific note.", selection_logic)
        self.assertIn("Actor-specific note.", analyst_notes)

    def test_activity_target_refs_are_deterministically_sorted(self) -> None:
        profile = self.profile("Example Group", "example")
        profile["activities"] = [
            {
                "activity_id": "activity--example",
                "target_refs": ["target--z", "target--b"],
            }
        ]

        link_activity_target(
            profile,
            {"activity_ids": {"activity--example"}},
            "target--a",
        )

        self.assertEqual(
            profile["activities"][0]["target_refs"],
            ["target--a", "target--b", "target--z"],
        )

    def test_reviewed_activity_geography_exclusion_is_honored(self) -> None:
        profile = self.profile("Example Group", "example")
        unknown = {
            "value": None,
            "precision": "unknown",
            "status": "unknown",
            "basis": "not-stated",
        }
        profile["activities"] = [
            {
                "activity_id": "activity--example",
                "name": "日本と米国への攻撃",
                "description": "日本と米国の政府機関を標的にした。",
                "first_observed": copy.deepcopy(unknown),
                "last_observed": copy.deepcopy(unknown),
                "reported_at": copy.deepcopy(unknown),
                "activity_type": "intrusion",
                "target_refs": [],
                "malware_refs": [],
                "infrastructure_refs": [],
                "ttp_refs": [],
                "victim_refs": [],
                "confidence": "high",
                "evidence_refs": [],
                "analyst_notes": "",
            }
        ]
        rules = copy.deepcopy(self.rules)
        rules["_activity_target_exclusions"] = {
            "activity--example": {"日本"}
        }

        process_profile(
            profile,
            slug="example",
            geography=self.geography,
            compiled_rules=rules,
            group=None,
            crosscheck=None,
            dataset_indexes={},
            curation=None,
        )

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertEqual(countries, {"米国"})


if __name__ == "__main__":
    unittest.main()
