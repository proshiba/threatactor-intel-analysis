#!/usr/bin/env python3
"""Regression tests for OpenCTI-focused STIX bundle generation."""

from __future__ import annotations

import json
import copy
import sys
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from build_opencti_bundles import (  # noqa: E402
    build_actor_bundle,
    build_actor_index,
    build_activity_bundle,
    build_campaign_bundle,
    normalize_shared_object_versions,
    prepare_profile_objects,
    profile_scoped_stix_id,
    producer_identity,
    validate_bundle,
    validate_shared_object_definitions,
)
from render_profile import (  # noqa: E402
    relationship_time_properties,
    stix_base,
    stix_id,
)


NOW = "2026-09-21T00:00:00Z"
CREATED = "2026-01-01T00:00:00Z"
COUNTRY_INDEX = {
    "Exampleland": {
        "id": "location--11111111-1111-4111-8111-111111111111",
        "name": "Exampleland Official",
        "country": "EXL",
        "latitude": 1.5,
        "longitude": 2.5,
        "aliases": ["EXL", "EX"],
    }
}


def point(value: str | None = None) -> dict[str, object]:
    return {
        "value": value,
        "precision": "day" if value else "unknown",
        "status": "known" if value else "unknown",
        "basis": "source-stated" if value else "not-stated",
    }


def fixture_profile() -> dict[str, object]:
    activity_id = "activity--example-operation"
    return {
        "profile_id": "actor--example",
        "name": "Example Actor",
        "status": "review",
        "created_at": CREATED,
        "updated_at": NOW,
        "actor": {
            "canonical_name": "Example Actor",
            "aliases": [],
            "description": "Example actor description.",
            "first_seen": point(),
            "last_seen": point(),
        },
        "free_text": {"executive_summary": "Example summary."},
        "sources": [
            {
                "source_id": "source--example",
                "title": "Example source",
                "publisher": "Example publisher",
                "path": "https://example.invalid/report",
                "source_type": "vendor-report",
                "published_at": point(CREATED),
            }
        ],
        "relationships": [
            {
                "relationship_id": "relationship--example-related",
                "target_actor": "Related Actor",
                "relationship_type": "taxonomy-overlaps-with",
                "description": "Tracked as overlapping taxonomies, not exact aliases.",
                "confidence": "medium",
                "first_observed": point(CREATED),
                "last_observed": point(CREATED),
                "evidence_refs": ["source--example"],
                "analyst_notes": "Keep the original relationship scope.",
            }
        ],
        "capabilities": {
            "malware": [
                {
                    "id": "malware--example",
                    "name": "Example Malware",
                }
            ],
            "infrastructure": [
                {
                    "id": "infra--example",
                    "name": "Example Infrastructure",
                }
            ],
        },
        "targets": {
            "countries": [
                {
                    "id": "target--country-example",
                    "name": "Exampleland",
                    "description": "Country target.",
                    "confidence": "high",
                }
            ],
            "regions": [],
            "sectors": [
                {
                    "id": "target--sector-example",
                    "name": "Example sector",
                    "description": "Sector target.",
                    "confidence": "medium",
                }
            ],
            "roles": [],
        },
        "activities": [
            {
                "activity_id": activity_id,
                "name": "Example Operation",
                "activity_type": "phishing-campaign",
                "stix_object_type": "campaign",
                "grouping_context": None,
                "activity_refs": [],
                "description": "Example campaign.",
                "malware_refs": ["malware--example"],
                "infrastructure_refs": ["infra--example"],
                "target_refs": ["target--country-example"],
                "ttp_refs": ["ttp--example"],
                "victim_refs": ["victim--example"],
            }
        ],
        "victim_cases": [
            {
                "victim_case_id": "victim--example",
                "target_refs": ["target--sector-example"],
                "malware_refs": ["malware--example"],
                "ttp_refs": ["ttp--example"],
            }
        ],
        "ttps": [
            {
                "ttp_id": "ttp--example",
                "malware_refs": ["malware--example"],
                "infrastructure_refs": [],
            }
        ],
    }


def related_profile() -> dict[str, object]:
    return {
        "profile_id": "actor--related",
        "name": "Related Actor",
        "status": "review",
        "created_at": CREATED,
        "updated_at": NOW,
        "actor": {
            "canonical_name": "Related Actor",
            "aliases": [],
            "description": "Related actor.",
            "first_seen": point(),
            "last_seen": point(),
        },
        "free_text": {"executive_summary": "Related actor."},
    }


def fixture_bundle(profile: dict[str, object]) -> dict[str, object]:
    actor_id = stix_id("intrusion-set", profile["profile_id"])
    campaign_id = stix_id("campaign", "activity--example-operation")
    malware_id = stix_id("malware", "malware--example")
    infrastructure_id = stix_id("infrastructure", "infra--example")
    country_id = stix_id("identity", "target--country-example")
    sector_id = stix_id("identity", "target--sector-example")
    ttp_id = stix_id("attack-pattern", "ttp--example")
    victim_id = stix_id("identity", "victim--example")
    unscoped_indicator = stix_base(
        "indicator",
        "indicator--unscoped",
        NOW,
        {
            "name": "domain: unscoped.example",
            "pattern": "[domain-name:value = 'unscoped.example']",
            "pattern_type": "stix",
            "valid_from": CREATED,
            "x_disposition": "confirmed",
            "x_campaign_refs": [],
            "x_malware_refs": ["malware--example"],
            "x_infrastructure_refs": [],
            "x_observations": [{"source_id": "source--ioc"}],
        },
    )
    scoped_indicator = stix_base(
        "indicator",
        "indicator--scoped",
        NOW,
        {
            "name": "domain: scoped.example",
            "pattern": "[domain-name:value = 'scoped.example']",
            "pattern_type": "stix",
            "valid_from": CREATED,
            "x_disposition": "candidate",
            "x_campaign_refs": ["activity--example-operation"],
            "x_malware_refs": ["malware--example"],
            "x_infrastructure_refs": ["infra--example"],
            "x_observations": [{"source_id": "source--ioc"}],
        },
    )
    objects = [
        stix_base(
            "intrusion-set",
            profile["profile_id"],
            NOW,
            {"name": "Example Actor", "x_profile_id": profile["profile_id"]},
        ),
        stix_base(
            "campaign",
            "activity--example-operation",
            NOW,
            {
                "name": "Example Operation",
                "x_profile_object_id": "activity--example-operation",
            },
        ),
        stix_base(
            "malware",
            "malware--example",
            NOW,
            {
                "name": "Example Malware",
                "is_family": True,
                "x_profile_object_id": "malware--example",
            },
        ),
        stix_base(
            "infrastructure",
            "infra--example",
            NOW,
            {
                "name": "Example Infrastructure",
                "infrastructure_types": ["command-and-control"],
                "x_profile_object_id": "infra--example",
            },
        ),
        stix_base(
            "identity",
            "target--country-example",
            NOW,
            {
                "name": "Exampleland",
                "description": "Actor-specific country targeting evidence.",
                "identity_class": "organization",
                "external_references": [
                    {
                        "source_name": "Example publisher",
                        "external_id": "source--example",
                    }
                ],
                "x_target_category": "countries",
            },
        ),
        stix_base(
            "identity",
            "target--sector-example",
            NOW,
            {
                "name": "Example sector",
                "identity_class": "organization",
                "x_target_category": "sectors",
            },
        ),
        stix_base(
            "identity",
            "victim--example",
            NOW,
            {
                "name": "Example victim",
                "identity_class": "organization",
                "x_profile_object_id": "victim--example",
            },
        ),
        stix_base(
            "attack-pattern",
            "ttp--example",
            NOW,
            {"name": "Example TTP", "x_profile_object_id": "ttp--example"},
        ),
        unscoped_indicator,
        scoped_indicator,
        stix_base(
            "relationship",
            f"{actor_id}:uses:{malware_id}",
            NOW,
            {
                "relationship_type": "uses",
                "source_ref": actor_id,
                "target_ref": malware_id,
            },
        ),
        stix_base(
            "relationship",
            f"{campaign_id}:uses:{infrastructure_id}",
            NOW,
            {
                "relationship_type": "uses",
                "source_ref": campaign_id,
                "target_ref": infrastructure_id,
            },
        ),
        stix_base(
            "relationship",
            f"{campaign_id}:attributed-to:{actor_id}",
            NOW,
            {
                "relationship_type": "attributed-to",
                "source_ref": campaign_id,
                "target_ref": actor_id,
            },
        ),
        stix_base(
            "relationship",
            f"{campaign_id}:targets:{country_id}",
            NOW,
            {
                "relationship_type": "targets",
                "source_ref": campaign_id,
                "target_ref": country_id,
            },
        ),
        stix_base(
            "relationship",
            f"{campaign_id}:targets:{victim_id}",
            NOW,
            {
                "relationship_type": "targets",
                "source_ref": campaign_id,
                "target_ref": victim_id,
            },
        ),
        stix_base(
            "relationship",
            f"{campaign_id}:uses:{ttp_id}",
            NOW,
            {
                "relationship_type": "uses",
                "source_ref": campaign_id,
                "target_ref": ttp_id,
            },
        ),
    ]
    return {"type": "bundle", "id": stix_id("bundle", "fixture"), "objects": objects}


class OpenCTIBundleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.profile = fixture_profile()
        self.producer = producer_identity(CREATED, NOW)
        iocs = {
            "sources": [
                {
                    "source_id": "source--ioc",
                    "path": "reports/example.pdf",
                    "title": "IOC appendix",
                    "publisher": "Example publisher",
                    "source_type": "vendor-report",
                    "published_at": point(NOW),
                }
            ],
            "indicators": [
                {
                    "indicator_id": "indicator--scoped",
                    "type": "domain",
                    "value": "scoped.example",
                    "normalized_value": "scoped.example",
                    "disposition": "candidate",
                    "campaign_refs": ["activity--example-operation"],
                    "infrastructure_refs": ["infra--example"],
                    "observations": [
                        {
                            "source_id": "source--ioc",
                            "observed_at": point(),
                            "source_published_at": point(NOW),
                        }
                    ],
                }
            ],
        }
        objects, _ = prepare_profile_objects(
            self.profile,
            iocs,
            fixture_bundle(self.profile),
            self.producer["id"],
            COUNTRY_INDEX,
        )
        self.record = {
            "slug": "example",
            "profile": self.profile,
            "iocs": iocs,
            "objects": objects,
        }

    def test_opencti_target_types_are_preserved_without_fake_organizations(self) -> None:
        country = next(
            item
            for item in self.record["objects"]
            if item.get("x_profile_object_id") == "target--country-example"
        )
        sector = next(
            item
            for item in self.record["objects"]
            if item.get("name") == "Example sector"
        )
        self.assertEqual(country["type"], "location")
        self.assertEqual(country["x_opencti_location_type"], "Country")
        self.assertEqual(country["name"], "Exampleland Official")
        self.assertEqual(country["country"], "EXL")
        self.assertEqual(country["latitude"], 1.5)
        self.assertEqual(country["longitude"], 2.5)
        self.assertEqual(country["confidence"], 100)
        self.assertNotIn("description", country)
        self.assertNotIn("external_references", country)
        self.assertEqual(
            country["x_opencti_reference_id"],
            COUNTRY_INDEX["Exampleland"]["id"],
        )
        self.assertEqual(country["x_opencti_aliases"], ["EX", "EXL", "Exampleland"])
        self.assertEqual(sector["type"], "identity")
        self.assertEqual(sector["identity_class"], "class")
        country_relationship = next(
            item
            for item in self.record["objects"]
            if item.get("type") == "relationship"
            and item.get("target_ref") == country["id"]
        )
        self.assertIn(
            "Actor-specific country targeting evidence.",
            country_relationship["description"],
        )
        self.assertEqual(
            country_relationship["external_references"][0]["external_id"],
            "source--example",
        )

    def test_unknown_relationship_period_remains_explicit_metadata(self) -> None:
        properties = relationship_time_properties(
            point(),
            {
                **point(),
                "basis": "relationship-end-not-stated",
            },
        )

        self.assertEqual(properties["x_first_observed"]["status"], "unknown")
        self.assertEqual(
            properties["x_temporal_basis"]["last"],
            "relationship-end-not-stated",
        )
        self.assertNotIn("start_time", properties)
        self.assertNotIn("stop_time", properties)

    def test_actor_bundle_keeps_unscoped_iocs_and_actor_relationship_scope(self) -> None:
        related = {"slug": "related", "profile": related_profile()}
        by_id, by_name = build_actor_index([self.record, related])
        bundle, unresolved = build_actor_bundle(
            self.record, self.producer, by_id, by_name
        )
        self.assertEqual(unresolved, [])
        self.assertEqual(validate_bundle(bundle, expected_scope="actor"), [])
        types = [item["type"] for item in bundle["objects"]]
        self.assertNotIn("campaign", types)
        names = {item.get("name") for item in bundle["objects"]}
        self.assertIn("domain: unscoped.example", names)
        self.assertNotIn("domain: scoped.example", names)
        relation = next(
            item
            for item in bundle["objects"]
            if item.get("x_profile_relationship_id")
            == "relationship--example-related"
        )
        self.assertEqual(relation["relationship_type"], "related-to")
        self.assertEqual(
            relation["x_profile_relationship_type"], "taxonomy-overlaps-with"
        )
        self.assertEqual(relation["start_time"], CREATED)
        self.assertNotIn("stop_time", relation)
        self.assertEqual(relation["x_first_observed"], point(CREATED))
        self.assertEqual(relation["x_last_observed"], point(CREATED))
        self.assertEqual(
            relation["x_temporal_basis"],
            {
                "first": "source-stated",
                "last": "source-stated",
                "first_precision": "day",
                "last_precision": "day",
            },
        )

    def test_actor_relationship_unknown_period_is_machine_readable(self) -> None:
        profile = copy.deepcopy(self.profile)
        profile["relationships"][0]["first_observed"] = point()
        profile["relationships"][0]["last_observed"] = {
            **point(),
            "basis": "relationship-end-not-stated",
        }
        record = {**self.record, "profile": profile}
        related = {"slug": "related", "profile": related_profile()}
        by_id, by_name = build_actor_index([record, related])

        bundle, unresolved = build_actor_bundle(
            record, self.producer, by_id, by_name
        )

        self.assertEqual(unresolved, [])
        relation = next(
            item
            for item in bundle["objects"]
            if item.get("x_profile_relationship_id")
            == "relationship--example-related"
        )
        self.assertEqual(relation["x_first_observed"]["status"], "unknown")
        self.assertEqual(relation["x_last_observed"]["status"], "unknown")
        self.assertEqual(
            relation["x_temporal_basis"]["last"],
            "relationship-end-not-stated",
        )
        self.assertNotIn("start_time", relation)
        self.assertNotIn("stop_time", relation)

    def test_actor_relationship_reuses_full_target_actor_object(self) -> None:
        related = {"slug": "related", "profile": related_profile()}
        target_ref = stix_id("intrusion-set", "actor--related")
        target_actor = stix_base(
            "intrusion-set",
            "actor--related",
            NOW,
            {
                "name": "Related Actor",
                "description": "Full canonical actor definition.",
                "aliases": ["Related Alias"],
                "goals": ["Documented goal"],
                "x_profile_id": "actor--related",
                "x_profile_status": "review",
                "x_attribution": {"sponsor_type": "unknown"},
                "created_by_ref": self.producer["id"],
            },
        )
        related["objects"] = [target_actor]
        by_id, by_name = build_actor_index([self.record, related])

        bundle, unresolved = build_actor_bundle(
            self.record, self.producer, by_id, by_name
        )

        self.assertEqual(unresolved, [])
        exported = next(item for item in bundle["objects"] if item["id"] == target_ref)
        self.assertEqual(exported, target_actor)

    def test_actor_bundle_prunes_activity_refs_from_hunting_note(self) -> None:
        record = copy.deepcopy(self.record)
        actor_ref = stix_id("intrusion-set", self.profile["profile_id"])
        campaign_ref = profile_scoped_stix_id(
            self.profile["profile_id"],
            "campaign",
            stix_id("campaign", "activity--example-operation"),
        )
        note = stix_base(
            "note",
            "hunting-note:example",
            NOW,
            {
                "abstract": "Hunting pivot",
                "content": "Pivot evidence shared with a campaign bundle.",
                "object_refs": [actor_ref, campaign_ref],
                "x_profile_hunting_pivot_id": "hunting-pivot--example",
            },
        )
        note["created_by_ref"] = self.producer["id"]
        record["objects"].append(note)
        by_id, by_name = build_actor_index([record])

        bundle, _ = build_actor_bundle(
            record, self.producer, by_id, by_name
        )

        exported_note = next(
            item
            for item in bundle["objects"]
            if item.get("x_profile_hunting_pivot_id")
            == "hunting-pivot--example"
        )
        self.assertEqual(exported_note["object_refs"], [actor_ref])
        self.assertEqual(validate_bundle(bundle, expected_scope="actor"), [])

        activity_bundle = build_campaign_bundle(
            record,
            record["profile"]["activities"][0],
            self.producer,
        )
        activity_note = next(
            item
            for item in activity_bundle["objects"]
            if item.get("x_profile_hunting_pivot_id")
            == "hunting-pivot--example"
        )
        self.assertEqual(
            set(activity_note["object_refs"]), {actor_ref, campaign_ref}
        )
        self.assertNotEqual(exported_note["id"], activity_note["id"])
        self.assertEqual(
            validate_bundle(activity_bundle, expected_scope="campaign"), []
        )

    def test_profile_claims_are_namespaced_and_shared_sdos_are_identical(self) -> None:
        other_profile = copy.deepcopy(self.profile)
        other_profile["profile_id"] = "actor--other-example"
        other_profile["name"] = "Other Example Actor"
        other_profile["actor"]["canonical_name"] = "Other Example Actor"
        other_profile["updated_at"] = "2026-09-22T00:00:00Z"
        other_bundle = fixture_bundle(other_profile)
        other_bundle["objects"][0]["name"] = "Other Example Actor"
        other_iocs = copy.deepcopy(self.record["iocs"])
        other_objects, _ = prepare_profile_objects(
            other_profile,
            other_iocs,
            other_bundle,
            self.producer["id"],
            COUNTRY_INDEX,
        )
        records = [
            self.record,
            {
                "slug": "other-example",
                "profile": other_profile,
                "iocs": other_iocs,
                "objects": other_objects,
            },
        ]

        normalize_shared_object_versions(records)

        original_ttp = next(
            item
            for item in self.record["objects"]
            if item.get("x_profile_object_id") == "ttp--example"
        )
        other_ttp = next(
            item
            for item in other_objects
            if item.get("x_profile_object_id") == "ttp--example"
        )
        self.assertNotEqual(original_ttp["id"], other_ttp["id"])

        original_country = next(
            item
            for item in self.record["objects"]
            if item.get("x_profile_object_id") == "target--country-example"
        )
        other_country = next(
            item
            for item in other_objects
            if item.get("x_profile_object_id") == "target--country-example"
        )
        self.assertEqual(original_country, other_country)

        definitions: dict[str, str] = {}
        for record in records:
            for item in record["objects"]:
                serialized = json.dumps(
                    item, sort_keys=True, ensure_ascii=False
                )
                previous = definitions.setdefault(item["id"], serialized)
                self.assertEqual(previous, serialized, item["id"])

    def test_cross_bundle_validator_rejects_same_id_with_different_content(self) -> None:
        definitions: dict[str, str] = {}
        first = {
            "type": "bundle",
            "objects": [
                stix_base(
                    "attack-pattern",
                    "shared-example",
                    NOW,
                    {"name": "Shared technique", "description": "First"},
                )
            ],
        }
        second = copy.deepcopy(first)
        second["objects"][0]["description"] = "Conflicting"

        self.assertEqual(
            validate_shared_object_definitions(first, definitions), []
        )
        errors = validate_shared_object_definitions(second, definitions)
        self.assertEqual(len(errors), 1)
        self.assertIn(first["objects"][0]["id"], errors[0])

    def test_unresolved_actor_relationship_is_retained_as_note(self) -> None:
        by_id, by_name = build_actor_index([self.record])
        bundle, unresolved = build_actor_bundle(
            self.record, self.producer, by_id, by_name
        )
        self.assertEqual(unresolved, ["relationship--example-related"])
        note = next(
            item
            for item in bundle["objects"]
            if item.get("x_profile_relationship_id")
            == "relationship--example-related"
        )
        self.assertEqual(note["type"], "note")
        self.assertEqual(note["x_unresolved_target_actor"], "Related Actor")
        self.assertEqual(validate_bundle(bundle, expected_scope="actor"), [])

    def test_campaign_bundle_is_self_contained_and_campaign_scoped(self) -> None:
        activity = self.profile["activities"][0]
        bundle = build_campaign_bundle(self.record, activity, self.producer)
        self.assertEqual(validate_bundle(bundle, expected_scope="campaign"), [])
        names = {item.get("name") for item in bundle["objects"]}
        self.assertIn("domain: scoped.example", names)
        self.assertNotIn("domain: unscoped.example", names)
        country = next(
            item
            for item in bundle["objects"]
            if item.get("x_profile_object_id") == "target--country-example"
        )
        self.assertEqual(country["type"], "location")
        report = next(
            item
            for item in bundle["objects"]
            if item.get("x_opencti_bundle_scope") == "campaign"
        )
        relationship_ids = {
            item["id"] for item in bundle["objects"] if item["type"] == "relationship"
        }
        self.assertTrue(relationship_ids <= set(report["object_refs"]))
        campaign_ref = profile_scoped_stix_id(
            self.profile["profile_id"],
            "campaign",
            stix_id("campaign", "activity--example-operation"),
        )
        campaign = next(
            item for item in bundle["objects"] if item["id"] == campaign_ref
        )
        self.assertEqual(campaign["x_activity_type"], "phishing-campaign")
        self.assertTrue(
            any(
                item.get("relationship_type") == "indicates"
                and item.get("target_ref") == campaign_ref
                for item in bundle["objects"]
            )
        )

    def test_infrastructure_contains_observable_without_publication_as_validity(self) -> None:
        activity = self.profile["activities"][0]
        bundle = build_activity_bundle(self.record, activity, self.producer)
        observable = next(
            item
            for item in bundle["objects"]
            if item.get("type") == "domain-name"
            and item.get("value") == "scoped.example"
        )
        relation = next(
            item
            for item in bundle["objects"]
            if item.get("relationship_type") == "consists-of"
            and item.get("target_ref") == observable["id"]
        )
        self.assertEqual(relation["x_temporal_basis"], "report-published-fallback")
        self.assertFalse(relation["x_time_correlation_eligible"])
        self.assertNotIn("start_time", relation)
        self.assertNotIn("stop_time", relation)
        source_report = next(
            item
            for item in bundle["objects"]
            if item.get("x_opencti_source_report")
            and item.get("x_source_id") == "source--ioc"
        )
        self.assertEqual(source_report["published"], NOW)
        self.assertEqual(source_report["x_temporal_role"], "publication-only")
        self.assertIn(relation["id"], source_report["object_refs"])

    def test_incident_bundle_uses_explicit_primary_type(self) -> None:
        record = copy.deepcopy(self.record)
        activity = record["profile"]["activities"][0]
        activity["stix_object_type"] = "incident"
        old_id = profile_scoped_stix_id(
            self.profile["profile_id"],
            "campaign",
            stix_id("campaign", activity["activity_id"]),
        )
        new_id = profile_scoped_stix_id(
            self.profile["profile_id"],
            "incident",
            stix_id("incident", activity["activity_id"]),
        )
        for obj in record["objects"]:
            if obj.get("id") == old_id:
                obj["type"] = "incident"
                obj["id"] = new_id
                obj["x_stix_object_type"] = "incident"
            for field in ("source_ref", "target_ref"):
                if obj.get(field) == old_id:
                    obj[field] = new_id
        bundle = build_activity_bundle(record, activity, self.producer)
        self.assertEqual(validate_bundle(bundle, expected_scope="incident"), [])
        self.assertTrue(
            any(
                item.get("type") == "incident"
                and item.get("x_profile_object_id") == activity["activity_id"]
                for item in bundle["objects"]
            )
        )

    def test_grouping_contains_evidence_without_implied_relationship(self) -> None:
        record = copy.deepcopy(self.record)
        activity = record["profile"]["activities"][0]
        activity["stix_object_type"] = "grouping"
        activity["grouping_context"] = "suspicious-activity"
        old_id = profile_scoped_stix_id(
            self.profile["profile_id"],
            "campaign",
            stix_id("campaign", activity["activity_id"]),
        )
        new_id = profile_scoped_stix_id(
            self.profile["profile_id"],
            "grouping",
            stix_id("grouping", activity["activity_id"]),
        )
        converted: list[dict[str, object]] = []
        for obj in record["objects"]:
            if obj.get("type") == "relationship" and old_id in {
                obj.get("source_ref"), obj.get("target_ref")
            }:
                continue
            if obj.get("id") == old_id:
                obj["type"] = "grouping"
                obj["id"] = new_id
                obj["context"] = "suspicious-activity"
                obj["object_refs"] = [
                    stix_id("intrusion-set", record["profile"]["profile_id"])
                ]
                obj["x_stix_object_type"] = "grouping"
            converted.append(obj)
        record["objects"] = converted
        bundle = build_activity_bundle(record, activity, self.producer)
        self.assertEqual(validate_bundle(bundle, expected_scope="grouping"), [])
        grouping = next(item for item in bundle["objects"] if item["id"] == new_id)
        scoped_indicator = next(
            item
            for item in bundle["objects"]
            if item.get("name") == "domain: scoped.example"
        )
        self.assertIn(scoped_indicator["id"], grouping["object_refs"])
        self.assertFalse(
            any(item.get("type") == "relationship" for item in bundle["objects"])
        )

    def test_country_index_covers_every_canonical_country(self) -> None:
        actor_profile_root = Path(__file__).resolve().parents[1]
        geography = json.loads(
            (actor_profile_root / "target-geography.json").read_text(
                encoding="utf-8"
            )
        )
        index = json.loads(
            (
                actor_profile_root
                / "reference"
                / "opencti-country-index.json"
            ).read_text(encoding="utf-8")
        )["countries"]
        expected = {item["name"] for item in geography["countries"]}
        self.assertEqual(set(index), expected)
        for name, item in index.items():
            with self.subTest(country=name):
                self.assertTrue(item["id"].startswith("location--"))
                self.assertEqual(len(item["country"]), 3)
                self.assertTrue(item["name"])


if __name__ == "__main__":
    unittest.main()
