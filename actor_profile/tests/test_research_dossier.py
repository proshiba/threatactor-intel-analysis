from __future__ import annotations

import sys
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from build_actor_research_dossiers import (  # noqa: E402
    explicit_time,
    linked_period,
    malware_records,
)


def point(value: str | None) -> dict:
    return {
        "value": value,
        "precision": "day" if value else "unknown",
        "status": "known" if value else "unknown",
        "basis": "source-stated" if value else "not-stated",
    }


class ResearchDossierTests(unittest.TestCase):
    def test_aggregation_time_can_be_marked_inferred(self) -> None:
        result = explicit_time(
            "2024-03-01",
            "aggregation; original source not reviewed",
            status="inferred",
        )
        self.assertEqual(result["status"], "inferred")
        self.assertEqual(result["precision"], "day")

    def test_linked_period_ignores_unknown_activity_dates(self) -> None:
        observations = [
            {"first_observed": point(None)},
            {"first_observed": point("2024-05-02T00:00:00Z")},
            {"first_observed": point("2023-04-01T00:00:00Z")},
        ]
        result = linked_period(observations, "first_observed", "min")
        self.assertEqual(result["value"], "2023-04-01T00:00:00Z")
        self.assertEqual(result["status"], "inferred")
        self.assertEqual(result["basis"], "explicit-linked-activity-period")

    def test_malware_use_period_requires_an_activity_link(self) -> None:
        profile = {
            "capabilities": {
                "malware": [
                    {
                        "id": "malware--sample",
                        "name": "Sample",
                        "evidence_refs": ["source--one"],
                    }
                ]
            },
            "activities": [
                {
                    "activity_id": "activity--one",
                    "name": "One",
                    "malware_refs": [],
                    "first_observed": point("2024-01-01T00:00:00Z"),
                    "last_observed": point("2024-01-02T00:00:00Z"),
                    "evidence_refs": ["source--one"],
                }
            ],
            "ttps": [],
        }
        result = malware_records(profile, {})[0]
        self.assertEqual(result["activity_observations"], [])
        self.assertIsNone(result["derived_first_observed"]["value"])
        self.assertIn("actor-level-only", result["temporal_assessment"])


if __name__ == "__main__":
    unittest.main()
