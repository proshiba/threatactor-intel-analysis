from __future__ import annotations

import sys
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from sync_attack_reference import (  # noqa: E402
    CURRENT_SOURCE_ID,
    OLD_SOURCE_ID,
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


if __name__ == "__main__":
    unittest.main()
