#!/usr/bin/env python3
"""Regression tests for activity-level Diamond Model materialization."""

from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from activity_diamond import (  # noqa: E402
    SCHEMA_VERSION,
    build_activity_diamond,
    materialize_profile_diamonds,
)
from common import unknown_time  # noqa: E402


class ActivityDiamondTests(unittest.TestCase):
    def profile(self) -> dict:
        activity_id = "activity--example"
        return {
            "schema_version": "1.1.0",
            "profile_id": "actor--example",
            "name": "Example Actor",
            "actor": {"canonical_name": "Example Actor"},
            "attribution": {
                "countries": ["Exampleland"],
                "organizations": [{"id": "org--example"}],
            },
            "capabilities": {
                "malware": [
                    {"id": "malware--linked", "name": "LinkedRAT"},
                    {"id": "malware--general", "name": "GeneralRAT"},
                ],
                "infrastructure": [
                    {"id": "infra--linked", "name": "Linked C2"}
                ],
            },
            "targets": {
                "countries": [{"id": "target--japan", "name": "日本"}],
                "regions": [{"id": "target--east-asia", "name": "東アジア"}],
                "sectors": [{"id": "target--finance", "name": "金融"}],
                "roles": [],
            },
            "activities": [
                {
                    "activity_id": activity_id,
                    "name": "Example campaign",
                    "activity_type": "campaign",
                    "first_observed": unknown_time(),
                    "last_observed": unknown_time(),
                    "reported_at": unknown_time(),
                    "description": "",
                    "target_refs": ["target--japan"],
                    "malware_refs": ["malware--linked"],
                    "infrastructure_refs": [],
                    "ttp_refs": ["ttp--example"],
                    "victim_refs": ["victim--example"],
                    "confidence": "high",
                    "evidence_refs": ["source--activity"],
                    "analyst_notes": "",
                }
            ],
            "victim_cases": [
                {
                    "victim_case_id": "victim--example",
                    "activity_refs": [activity_id],
                    "target_refs": ["target--finance"],
                    "malware_refs": [],
                    "ttp_refs": ["ttp--example"],
                    "impacts": [
                        {"impact_type": "data-theft", "description": ""}
                    ],
                    "evidence_refs": ["source--victim"],
                }
            ],
            "ttps": [
                {
                    "ttp_id": "ttp--example",
                    "tactic": "Initial Access, Execution",
                    "malware_refs": ["malware--linked"],
                    "infrastructure_refs": ["infra--linked"],
                    "evidence_refs": ["source--ttp"],
                }
            ],
        }

    def test_builds_four_vertices_and_meta_features_from_linked_records(self) -> None:
        profile = self.profile()
        diamond = build_activity_diamond(profile, profile["activities"][0])

        self.assertEqual(diamond["adversary"]["actor_ref"], "actor--example")
        self.assertEqual(
            diamond["capability"]["malware_refs"], ["malware--linked"]
        )
        self.assertNotIn("malware--general", diamond["capability"]["malware_refs"])
        self.assertEqual(
            diamond["infrastructure"]["infrastructure_refs"],
            ["infra--linked"],
        )
        self.assertEqual(
            diamond["victim"]["target_refs"],
            ["target--finance", "target--japan"],
        )
        self.assertEqual(
            diamond["meta_features"]["direction"]["target_country_refs"],
            ["target--japan"],
        )
        self.assertEqual(
            diamond["meta_features"]["phases"], ["Execution", "Initial Access"]
        )
        self.assertEqual(diamond["meta_features"]["results"], ["data-theft"])
        self.assertEqual(
            diamond["evidence_refs"],
            ["source--activity", "source--ttp", "source--victim"],
        )

    def test_materialization_is_idempotent_and_updates_schema(self) -> None:
        profile = self.profile()
        self.assertEqual(materialize_profile_diamonds(profile), 1)
        first = copy.deepcopy(profile["activities"][0]["diamond_model"])
        self.assertEqual(profile["schema_version"], SCHEMA_VERSION)
        self.assertEqual(materialize_profile_diamonds(profile), 0)
        self.assertEqual(profile["activities"][0]["diamond_model"], first)


if __name__ == "__main__":
    unittest.main()
