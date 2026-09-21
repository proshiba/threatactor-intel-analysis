from __future__ import annotations

import sys
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from sync_attack_reference import (  # noqa: E402
    CURRENT_SOURCE_ID,
    OLD_SOURCE_ID,
    boundary_aliases,
    sync_aliases,
)


class AttackReferenceSyncTests(unittest.TestCase):
    def test_current_alias_migrates_but_stale_alias_keeps_only_other_evidence(self) -> None:
        profile = {
            "actor": {
                "canonical_name": "Example",
                "aliases": [
                    {
                        "name": "Current Name",
                        "vendor": "MITRE ATT&CK",
                        "scope": "overlapping",
                        "confidence": "high",
                        "evidence_refs": [OLD_SOURCE_ID],
                        "analyst_notes": "",
                    },
                    {
                        "name": "Retired Name",
                        "vendor": "MITRE ATT&CK",
                        "scope": "overlapping",
                        "confidence": "high",
                        "evidence_refs": [OLD_SOURCE_ID],
                        "analyst_notes": "",
                    },
                    {
                        "name": "Vendor Name",
                        "vendor": "Vendor",
                        "scope": "overlapping",
                        "confidence": "medium",
                        "evidence_refs": [OLD_SOURCE_ID, "source--vendor"],
                        "analyst_notes": "",
                    },
                ],
            }
        }
        sync_aliases(
            profile,
            {"aliases": ["Example", "Current Name"]},
        )
        aliases = {item["name"]: item for item in profile["actor"]["aliases"]}
        self.assertNotIn("Retired Name", aliases)
        self.assertEqual(aliases["Current Name"]["evidence_refs"], [CURRENT_SOURCE_ID])
        self.assertEqual(aliases["Vendor Name"]["evidence_refs"], ["source--vendor"])

    def test_reviewed_boundary_blocks_attck_associated_name(self) -> None:
        profile = {
            "actor": {
                "canonical_name": "Broad Group",
                "aliases": [
                    {
                        "name": "Separate Group",
                        "vendor": "MITRE ATT&CK",
                        "scope": "overlapping",
                        "confidence": "high",
                        "evidence_refs": [CURRENT_SOURCE_ID],
                        "analyst_notes": "",
                    }
                ],
            }
        }
        curation = {
            "identity_boundaries": [
                {"names": ["Broad Group", "Separate Group"]}
            ]
        }

        blocked = boundary_aliases(curation, "Broad Group")
        sync_aliases(
            profile,
            {"aliases": ["Broad Group", "Separate Group"]},
            blocked_aliases=blocked,
        )

        self.assertEqual(profile["actor"]["aliases"], [])

    def test_primary_reviewed_exact_alias_is_not_overwritten_by_attck(self) -> None:
        profile = {
            "actor": {
                "canonical_name": "Canonical Group",
                "aliases": [
                    {
                        "name": "Primary Exact Name",
                        "vendor": "Government CERT",
                        "scope": "exact",
                        "confidence": "high",
                        "evidence_refs": ["source--primary-government"],
                        "analyst_notes": "Explicitly identified as the same actor.",
                    }
                ],
            }
        }

        sync_aliases(
            profile,
            {"aliases": ["Canonical Group", "Primary Exact Name"]},
        )

        alias = profile["actor"]["aliases"][0]
        self.assertEqual(alias["vendor"], "Government CERT")
        self.assertEqual(alias["scope"], "exact")
        self.assertEqual(alias["evidence_refs"], ["source--primary-government"])


if __name__ == "__main__":
    unittest.main()
