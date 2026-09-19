import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from bootstrap_all_profiles import actor_name_cells  # noqa: E402
from migrate_workbook_aliases import migrate_aliases  # noqa: E402


class WorkbookAliasBoundaryTests(unittest.TestCase):
    def test_only_explicit_name_columns_become_alias_candidates(self) -> None:
        record = {
            "sheet": "Others",
            "row": 49,
            "fields": {
                "Common Name": "GravityRAT",
                "Other Names": "Alias One, Alias Two / Alias Three; Alias Four",
                "Country": "Pakistan",
                "Origin": "Pakistan",
                "Sponsor": "Unknown",
                "Comment": "activity aligns sharply with state interests",
                "Targets": "India",
                "Toolset / Malware": "GravityRAT",
            },
        }
        self.assertEqual(
            actor_name_cells(record),
            ["GravityRAT", "Alias One", "Alias Two", "Alias Three", "Alias Four"],
        )

    def test_country_and_descriptive_prose_are_not_aliases(self) -> None:
        record = {
            "sheet": "Others",
            "row": 1,
            "fields": {
                "Common Name": "ModifiedElephant",
                "Country": "India",
                "Attribution": '"ModifiedElephant activity aligns sharply with Indian state interests"',
                "Description": "offshore APT organization from South Asia",
            },
        }
        self.assertEqual(actor_name_cells(record), ["ModifiedElephant"])

    def test_migration_replaces_only_workbook_aliases(self) -> None:
        profile = {
            "updated_at": "2026-01-01T00:00:00Z",
            "actor": {
                "canonical_name": "Example",
                "analyst_notes": "",
                "aliases": [
                    {
                        "name": "Trusted Alias",
                        "vendor": "MITRE ATT&CK",
                        "scope": "overlapping",
                        "confidence": "high",
                        "evidence_refs": ["source--mitre"],
                    },
                    {
                        "name": "Pakistan",
                        "vendor": "actor-mapping-workbook",
                        "scope": "unknown",
                        "confidence": "medium",
                        "evidence_refs": ["source--actor-mapping-workbook"],
                    },
                ],
            },
        }
        actor = {"slug": "example", "name": "Example", "aliases": []}
        record = {
            "sheet": "Others",
            "row": 2,
            "fields": {
                "Common Name": "Example",
                "Other Names": "Workbook Alias A, Workbook Alias B",
                "Country": "Pakistan",
            },
        }
        result = migrate_aliases(profile, actor, record)
        self.assertTrue(result["changed"])
        self.assertEqual(result["removed"], ["Pakistan"])
        names = [item["name"] for item in profile["actor"]["aliases"]]
        self.assertEqual(
            names,
            ["Trusted Alias", "Workbook Alias A", "Workbook Alias B"],
        )


if __name__ == "__main__":
    unittest.main()
