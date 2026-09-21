#!/usr/bin/env python3
"""Regression tests for entity and legal-action temporal boundaries."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from validate_profile import (  # noqa: E402
    validate_iocs,
    validate_legal_action_time,
    validate_profile,
    validate_time_order,
)


class LegalEntitySemanticsTests(unittest.TestCase):
    @staticmethod
    def unknown_time(basis: str = "not-stated") -> dict[str, object]:
        return {
            "value": None,
            "precision": "unknown",
            "status": "unknown",
            "basis": basis,
        }

    def test_publication_date_is_not_a_legal_action_date(self) -> None:
        issues = []

        validate_legal_action_time(
            {
                "value": "2025-03-05T00:00:00Z",
                "precision": "day",
                "status": "known",
                "basis": "indictment-publication-date",
            },
            "$.action_date",
            issues,
        )

        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].severity, "error")
        self.assertIn("publication date", issues[0].message)

    def test_unseal_date_can_be_retained_as_a_distinct_legal_event(self) -> None:
        issues = []

        validate_legal_action_time(
            {
                "value": "2024-10-01T00:00:00Z",
                "precision": "day",
                "status": "known",
                "basis": "indictment-unseal-date",
            },
            "$.action_date",
            issues,
        )

        self.assertEqual(issues, [])

    def test_first_observed_cannot_be_later_than_last_observed(self) -> None:
        issues = []

        validate_time_order(
            {
                "value": "2025-01-02T00:00:00Z",
                "precision": "day",
                "status": "known",
                "basis": "source-stated",
            },
            {
                "value": "2025-01-01T00:00:00Z",
                "precision": "day",
                "status": "known",
                "basis": "source-stated",
            },
            "$.entity",
            issues,
        )

        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].severity, "error")
        self.assertIn("cannot be later", issues[0].message)

    def test_actor_last_seen_rejects_source_publication_date(self) -> None:
        unknown = self.unknown_time()
        profile = {
            "schema_version": "1.4.0",
            "profile_id": "actor--temporal-regression",
            "name": "Temporal regression",
            "status": "active",
            "created_at": "2025-01-01T00:00:00Z",
            "updated_at": "2025-01-01T00:00:00Z",
            "actor": {
                "aliases": [],
                "first_seen": unknown,
                "last_seen": {
                    "value": "2025-01-01T00:00:00Z",
                    "precision": "day",
                    "status": "known",
                    "basis": "source-publication",
                },
            },
            "attribution": {
                "confidence": "unknown",
                "evidence_refs": [],
            },
            "motivations": [],
            "relationships": [],
            "associated_entities": [],
            "entity_relationships": [],
            "hunting_pivots": [],
            "diamond_model": {},
            "capabilities": {
                "malware": [],
                "tools": [],
                "infrastructure": [],
                "delivery_formats": [],
                "vulnerabilities": [],
                "operational_capabilities": [],
            },
            "activities": [],
            "victim_cases": [],
            "targets": {
                "countries": [],
                "regions": [],
                "sectors": [],
                "roles": [],
            },
            "ttps": [],
            "sources": [],
            "assessment": {"key_judgments": []},
            "free_text": {"executive_summary": "Regression fixture."},
        }
        issues = []

        validate_profile(profile, issues)

        self.assertTrue(
            any(
                item.severity == "error"
                and item.location == "$.actor.last_seen"
                and "publication" in item.message
                for item in issues
            )
        )

    def test_ioc_observation_rejects_source_publication_date(self) -> None:
        unknown = self.unknown_time()
        publication = {
            "value": "2025-01-01T00:00:00Z",
            "precision": "day",
            "status": "known",
            "basis": "source-publication",
        }
        dataset = {
            "schema_version": "1.0.0",
            "actor_ref": "actor--temporal-regression",
            "sources": [
                {
                    "source_id": "source--temporal-regression",
                    "published_at": publication,
                }
            ],
            "indicators": [
                {
                    "indicator_id": "indicator--temporal-regression",
                    "type": "ipv4",
                    "value": "198.51.100.10",
                    "normalized_value": "198.51.100.10",
                    "disposition": "confirmed",
                    "first_observed": unknown,
                    "last_observed": unknown,
                    "observation_count": 1,
                    "campaign_count": 0,
                    "seen_in_multiple_campaigns": False,
                    "campaign_refs": [],
                    "observations": [
                        {
                            "observation_id": "observation--temporal-regression",
                            "observed_at": publication,
                            "source_published_at": publication,
                            "source_id": "source--temporal-regression",
                            "campaign_refs": [],
                            "malware_refs": [],
                            "infrastructure_refs": [],
                        }
                    ],
                }
            ],
        }
        refs = {
            "source_ids": set(),
            "activity_ids": set(),
            "malware_ids": set(),
            "infrastructure_ids": set(),
        }
        issues = []

        validate_iocs(
            dataset,
            {"profile_id": "actor--temporal-regression"},
            refs,
            issues,
        )

        self.assertTrue(
            any(
                item.severity == "error"
                and item.location
                == "iocs.indicators[0].observations[0].observed_at"
                and "publication" in item.message
                for item in issues
            )
        )


if __name__ == "__main__":
    unittest.main()
