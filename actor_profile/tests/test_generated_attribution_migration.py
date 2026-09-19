import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from migrate_generated_attribution import migrate_profile  # noqa: E402


def base_profile() -> dict:
    return {
        "updated_at": "2026-01-01T00:00:00Z",
        "actor": {
            "actor_types": ["state-sponsored", "threat-cluster"],
            "aliases": [
                {
                    "name": "Catalog Alias",
                    "vendor": "catalog",
                    "scope": "overlapping",
                    "confidence": "high",
                    "evidence_refs": ["source--mitre-attack-19-1"],
                    "analyst_notes": "",
                }
            ],
            "analyst_notes": "",
        },
        "attribution": {
            "countries": ["Russia"],
            "sponsor_type": "state",
            "organizations": [],
            "assessment": (
                "The repository mapping workbook places this actor in the "
                "Russia worksheet."
            ),
            "confidence": "medium",
            "evidence_refs": ["source--actor-mapping-workbook"],
            "analyst_notes": "",
        },
        "motivations": [
            {
                "type": "espionage",
                "description": (
                    "State-sponsored intelligence collection or strategic operations."
                ),
                "confidence": "low",
                "evidence_refs": ["source--actor-mapping-workbook"],
                "analyst_notes": "",
            }
        ],
        "diamond_model": {
            "adversary": "",
            "capability": "",
            "infrastructure": "",
            "victim": "",
            "socio_political": "Russia",
            "analyst_notes": "",
        },
    }


class GeneratedAttributionMigrationTests(unittest.TestCase):
    def test_removes_geography_only_state_and_espionage(self) -> None:
        profile = base_profile()
        actor = {
            "slug": "example",
            "actor_types": ["state-sponsored", "threat-cluster"],
            "profile_basis": "actor-scoped-census-evidence",
        }
        report = migrate_profile(profile, actor, None)
        self.assertTrue(report["state_attribution_removed"])
        self.assertTrue(report["generated_espionage_removed"])
        self.assertEqual(profile["actor"]["actor_types"], ["threat-cluster"])
        self.assertEqual(profile["attribution"]["sponsor_type"], "unknown")
        self.assertEqual(profile["motivations"], [])
        self.assertEqual(profile["diamond_model"]["socio_political"], "")
        self.assertEqual(
            profile["actor"]["aliases"][0]["evidence_refs"],
            ["source--actor-mapping-workbook"],
        )
        self.assertEqual(profile["actor"]["aliases"][0]["confidence"], "medium")

    def test_actor_specific_state_text_rescopes_generated_attribution(self) -> None:
        profile = base_profile()
        actor = {
            "slug": "example",
            "actor_types": ["state-sponsored", "threat-cluster"],
            "profile_basis": "actor-scoped-census-evidence",
        }
        mitre_group = {
            "description": (
                "Example is a state-sponsored threat group conducting cyber espionage."
            ),
            "aliases": [],
        }
        report = migrate_profile(profile, actor, mitre_group)
        self.assertTrue(report["state_attribution_rescoped"])
        self.assertEqual(profile["attribution"]["sponsor_type"], "state")
        self.assertEqual(
            profile["attribution"]["evidence_refs"],
            ["source--mitre-attack-19-1", "source--actor-mapping-workbook"],
        )
        self.assertIn("state-sponsored", profile["actor"]["actor_types"])
        self.assertEqual(
            [item["type"] for item in profile["motivations"]],
            ["espionage"],
        )
        self.assertEqual(
            profile["motivations"][0]["evidence_refs"],
            ["source--mitre-attack-19-1"],
        )

    def test_old_generated_espionage_is_removed_from_non_census_profile(self) -> None:
        profile = base_profile()
        profile["attribution"] = {
            "countries": [],
            "sponsor_type": "unknown",
            "organizations": [],
            "assessment": "",
            "confidence": "unknown",
            "evidence_refs": [],
            "analyst_notes": "",
        }
        actor = {
            "slug": "existing-actor",
            "actor_types": ["state-sponsored"],
        }
        report = migrate_profile(profile, actor, None)
        self.assertTrue(report["generated_espionage_removed"])
        self.assertEqual(profile["actor"]["actor_types"], ["state-sponsored"])
        self.assertEqual(profile["motivations"], [])

    def test_manual_attribution_is_not_cleared(self) -> None:
        profile = base_profile()
        profile["attribution"].update(
            {
                "assessment": "Government advisory attributes the actor.",
                "confidence": "high",
                "evidence_refs": ["source--government-advisory"],
            }
        )
        actor = {
            "slug": "example",
            "actor_types": ["threat-cluster"],
            "profile_basis": "actor-scoped-census-evidence",
        }
        report = migrate_profile(profile, actor, None)
        self.assertFalse(report["state_attribution_removed"])
        self.assertEqual(
            profile["attribution"]["evidence_refs"],
            ["source--government-advisory"],
        )


if __name__ == "__main__":
    unittest.main()
