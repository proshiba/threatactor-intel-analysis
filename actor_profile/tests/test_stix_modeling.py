#!/usr/bin/env python3
"""Regression tests for explicit Campaign/Incident/Grouping decisions."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from stix_modeling import (  # noqa: E402
    apply_activity_modeling_defaults,
    default_stix_object_type,
)


class StixModelingTests(unittest.TestCase):
    def test_conservative_defaults_do_not_turn_every_record_into_campaign(self) -> None:
        self.assertEqual(default_stix_object_type("intrusion"), "incident")
        self.assertEqual(default_stix_object_type("reported-activity"), "grouping")
        self.assertEqual(default_stix_object_type("phishing-campaign"), "campaign")

    def test_explicit_analyst_decision_is_preserved(self) -> None:
        activity = {
            "activity_type": "intrusion",
            "stix_object_type": "campaign",
            "grouping_context": None,
            "activity_refs": [],
        }
        self.assertFalse(apply_activity_modeling_defaults(activity))
        self.assertEqual(activity["stix_object_type"], "campaign")

    def test_grouping_defaults_have_context_and_no_implied_relationships(self) -> None:
        activity = {"activity_type": "reported-activity"}
        self.assertTrue(apply_activity_modeling_defaults(activity))
        self.assertEqual(activity["stix_object_type"], "grouping")
        self.assertEqual(activity["grouping_context"], "suspicious-activity")
        self.assertEqual(activity["activity_refs"], [])


if __name__ == "__main__":
    unittest.main()
