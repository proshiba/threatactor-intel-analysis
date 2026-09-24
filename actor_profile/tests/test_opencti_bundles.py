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
    OPENCTI_MODEL_MODIFIED,
    PRODUCER_CREATED,
    PRODUCER_MODIFIED,
    build_actor_bundle,
    build_actor_index,
    build_activity_bundle,
    build_campaign_bundle,
    build_observable_role_index,
    campaign_dependency_profile_ids,
    normalize_shared_object_versions,
    observable_object,
    observable_objects_from_indicator_pattern,
    prepare_profile_objects,
    preserve_prepared_object_versions,
    preserve_object_versions,
    profile_scoped_stix_id,
    producer_identity,
    repository_producer_identity,
    validate_actor_identity_keys,
    validate_bundle,
    validate_shared_object_definitions,
)
from render_profile import (  # noqa: E402
    alias_assessment_note,
    opencti_identity_aliases,
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
            "tools": [
                {
                    "id": "tool--example",
                    "name": "Example Tool",
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
                "tool_refs": ["tool--example"],
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
    tool_id = stix_id("tool", "tool--example")
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
            "x_roles": ["c2"],
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
            "x_roles": ["phishing"],
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
            "tool",
            "tool--example",
            NOW,
            {
                "name": "Example Tool",
                "tool_types": ["remote-access"],
                "x_profile_object_id": "tool--example",
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
            f"{campaign_id}:uses:{tool_id}",
            NOW,
            {
                "relationship_type": "uses",
                "source_ref": campaign_id,
                "target_ref": tool_id,
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
                    "indicator_id": "indicator--unscoped",
                    "type": "domain",
                    "value": "unscoped.example",
                    "normalized_value": "unscoped.example",
                    "disposition": "confirmed",
                    "campaign_refs": [],
                    "infrastructure_refs": [],
                    "roles": ["c2"],
                    "observations": [
                        {
                            "source_id": "source--ioc",
                            "roles": ["c2"],
                            "observed_at": point(),
                            "source_published_at": point(NOW),
                        }
                    ],
                },
                {
                    "indicator_id": "indicator--scoped",
                    "type": "domain",
                    "value": "scoped.example",
                    "normalized_value": "scoped.example",
                    "disposition": "candidate",
                    "campaign_refs": ["activity--example-operation"],
                    "infrastructure_refs": ["infra--example"],
                    "roles": ["phishing"],
                    "observations": [
                        {
                            "source_id": "source--ioc",
                            "roles": ["phishing"],
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

    def test_repository_producer_has_its_own_pinned_version(self) -> None:
        producer = repository_producer_identity()
        self.assertEqual(producer["created"], PRODUCER_CREATED)
        self.assertEqual(producer["modified"], PRODUCER_MODIFIED)
        self.assertNotEqual(producer["modified"], NOW)

    def test_rebuild_preserves_created_and_unchanged_modified(self) -> None:
        object_id = stix_id("report", "version-test")
        previous_object = stix_base(
            "report",
            "version-test",
            CREATED,
            {"name": "Version test", "object_refs": []},
        )
        current_object = copy.deepcopy(previous_object)
        current_object["created"] = NOW
        current_object["modified"] = NOW
        current_bundle = {"type": "bundle", "objects": [current_object]}
        previous_bundle = {"type": "bundle", "objects": [previous_object]}

        preserve_object_versions(current_bundle, previous_bundle)

        rebuilt = current_bundle["objects"][0]
        self.assertEqual(rebuilt["id"], object_id)
        self.assertEqual(rebuilt["created"], CREATED)
        self.assertEqual(rebuilt["modified"], CREATED)

    def test_semantic_change_requires_newer_modified(self) -> None:
        previous_object = stix_base(
            "report",
            "version-change-test",
            CREATED,
            {"name": "Old name", "object_refs": []},
        )
        current_object = copy.deepcopy(previous_object)
        current_object["name"] = "New name"
        current_object["created"] = NOW
        current_bundle = {"type": "bundle", "objects": [current_object]}
        previous_bundle = {"type": "bundle", "objects": [previous_object]}

        with self.assertRaisesRegex(
            ValueError, "semantic content changed without a newer modified"
        ):
            preserve_object_versions(current_bundle, previous_bundle)

        current_object["modified"] = NOW
        preserve_object_versions(current_bundle, previous_bundle)
        self.assertEqual(current_object["created"], CREATED)
        self.assertEqual(current_object["modified"], NOW)

    def test_unversioned_observable_allows_only_role_label_migration(self) -> None:
        indicator = {
            "type": "domain",
            "normalized_value": "roles.example",
        }
        previous = observable_object(indicator, roles=[])
        current = observable_object(indicator, roles=["c2"])
        assert previous is not None and current is not None

        preserve_object_versions(
            {"objects": [current]}, {"objects": [previous]}
        )
        self.assertEqual(current["x_opencti_labels"], ["c2"])

        invalid = copy.deepcopy(current)
        invalid["value"] = "changed.example"
        with self.assertRaisesRegex(
            ValueError, "stable unversioned STIX object changed"
        ):
            preserve_object_versions(
                {"objects": [invalid]}, {"objects": [previous]}
            )

    def test_shared_versions_are_restored_before_bundle_slicing(self) -> None:
        previous = stix_base(
            "relationship",
            "shared-version-before-slicing",
            CREATED,
            {
                "relationship_type": "consists-of",
                "source_ref": stix_id("infrastructure", "shared-source"),
                "target_ref": stix_id("domain-name", "shared-target"),
            },
        )
        current = copy.deepcopy(previous)
        current["created"] = NOW
        current["modified"] = NOW
        records = [
            {"objects": [copy.deepcopy(current)]},
            {"objects": [copy.deepcopy(current)]},
        ]

        preserve_prepared_object_versions(records, {previous["id"]: previous})

        self.assertEqual(records[0]["objects"][0], previous)
        self.assertEqual(records[1]["objects"][0], previous)

    def test_only_exact_high_aliases_are_opencti_identity_keys(self) -> None:
        aliases = [
            {
                "name": "Exact High",
                "vendor": "Example",
                "scope": "exact",
                "confidence": "high",
                "evidence_refs": ["source--example"],
                "analyst_notes": "Verified rename.",
            },
            {
                "name": "Exact Medium",
                "vendor": "Example",
                "scope": "exact",
                "confidence": "medium",
                "evidence_refs": ["source--example"],
                "analyst_notes": "Identity is not yet high confidence.",
            },
            {
                "name": "Overlap Name",
                "vendor": "Other vendor",
                "scope": "overlapping",
                "confidence": "high",
                "evidence_refs": ["source--example"],
                "analyst_notes": "Cluster boundaries differ.",
            },
        ]
        actor = {"canonical_name": "Example Actor", "aliases": aliases}

        self.assertEqual(opencti_identity_aliases(actor), ["Exact High"])

        profile = copy.deepcopy(self.profile)
        profile["actor"]["aliases"] = aliases
        note = alias_assessment_note(
            profile,
            actor_ref=stix_id("intrusion-set", profile["profile_id"]),
            source_by_id={
                item["source_id"]: item for item in profile["sources"]
            },
        )
        self.assertIsNotNone(note)
        assert note is not None
        self.assertEqual(note["type"], "note")
        self.assertEqual(
            [item["name"] for item in note["x_alias_assessments"]],
            ["Exact Medium", "Overlap Name"],
        )
        self.assertIn("Overlap Name", note["content"])
        self.assertEqual(
            note["external_references"][0]["external_id"],
            "source--example",
        )

    def test_bundle_validator_rejects_non_identity_native_alias(self) -> None:
        bundle = copy.deepcopy(fixture_bundle(self.profile))
        actor = next(
            item for item in bundle["objects"]
            if item["type"] == "intrusion-set"
        )
        actor["aliases"] = ["Unsafe Overlap"]
        actor["x_alias_assessments"] = [
            {
                "name": "Unsafe Overlap",
                "vendor": "Example",
                "scope": "overlapping",
                "confidence": "high",
                "evidence_refs": ["source--example"],
                "analyst_notes": "Not exact identity.",
            }
        ]

        errors = validate_bundle(bundle)

        self.assertTrue(
            any("contains a non-identity alias" in item for item in errors),
            errors,
        )

    def test_actor_identity_keys_must_be_unique_across_active_profiles(self) -> None:
        left = fixture_profile()
        left["actor"]["aliases"] = [
            {
                "name": "Shared Exact Name",
                "vendor": "Example",
                "scope": "exact",
                "confidence": "high",
                "evidence_refs": ["source--example"],
                "analyst_notes": "Verified rename.",
            }
        ]
        right = related_profile()
        right["actor"]["canonical_name"] = "Shared_Exact-Name"
        errors = validate_actor_identity_keys(
            [
                {"slug": "left", "profile": left},
                {"slug": "right", "profile": right},
            ]
        )

        self.assertEqual(len(errors), 1)
        self.assertIn("actor--example", errors[0])
        self.assertIn("actor--related", errors[0])

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
        unscoped_indicator = next(
            item
            for item in bundle["objects"]
            if item.get("name") == "domain: unscoped.example"
        )
        unscoped_observable = next(
            item
            for item in bundle["objects"]
            if item.get("type") == "domain-name"
            and item.get("value") == "unscoped.example"
        )
        self.assertEqual(
            unscoped_indicator["x_opencti_main_observable_type"],
            "Domain-Name",
        )
        self.assertEqual(unscoped_indicator["labels"], ["c2"])
        self.assertEqual(unscoped_observable["x_opencti_labels"], ["c2"])
        self.assertEqual(unscoped_observable["x_ioc_roles"], ["c2"])
        based_on = next(
            item
            for item in bundle["objects"]
            if (
                item.get("relationship_type") == "based-on"
                and item.get("source_ref") == unscoped_indicator["id"]
                and item.get("target_ref") == unscoped_observable["id"]
            )
        )
        self.assertEqual(based_on["x_ioc_roles"], ["c2"])
        self.assertEqual(
            based_on["x_ioc_role_source_refs"], ["source--ioc"]
        )
        self.assertFalse(
            any(
                item.get("type") == "domain-name"
                and item.get("value") == "scoped.example"
                for item in bundle["objects"]
            )
        )
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
        self.assertEqual(relation["stop_time"], CREATED)
        self.assertNotIn("x_stop_time_is_fallback", relation)
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

    def test_actor_relationship_unknown_end_gets_marked_opencti_fallback(
        self,
    ) -> None:
        profile = copy.deepcopy(self.profile)
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
        self.assertEqual(relation["start_time"], CREATED)
        self.assertEqual(relation["stop_time"], CREATED)
        self.assertTrue(relation["x_stop_time_is_fallback"])
        self.assertEqual(
            relation["x_stop_time_basis"],
            "opencti-required-start-time-fallback",
        )
        self.assertIsNone(relation["x_last_observed"]["value"])
        self.assertGreaterEqual(relation["modified"], OPENCTI_MODEL_MODIFIED)

    def test_bundle_validator_rejects_start_without_stop_time(self) -> None:
        related = {"slug": "related", "profile": related_profile()}
        by_id, by_name = build_actor_index([self.record, related])
        bundle, _ = build_actor_bundle(
            self.record, self.producer, by_id, by_name
        )
        relation = next(
            item
            for item in bundle["objects"]
            if item.get("x_profile_relationship_id")
            == "relationship--example-related"
        )
        relation.pop("stop_time")

        errors = validate_bundle(bundle, expected_scope="actor")

        self.assertTrue(
            any("start_time without required stop_time" in item for item in errors),
            errors,
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
        self.assertIn("Example Tool", names)
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
        scoped_indicator = next(
            item
            for item in bundle["objects"]
            if item.get("name") == "domain: scoped.example"
        )
        scoped_observable = next(
            item
            for item in bundle["objects"]
            if item.get("type") == "domain-name"
            and item.get("value") == "scoped.example"
        )
        self.assertEqual(
            scoped_indicator["x_opencti_main_observable_type"],
            "Domain-Name",
        )
        self.assertTrue(
            any(
                item.get("relationship_type") == "based-on"
                and item.get("source_ref") == scoped_indicator["id"]
                and item.get("target_ref") == scoped_observable["id"]
                for item in bundle["objects"]
            )
        )
        tool = next(
            item
            for item in bundle["objects"]
            if item.get("x_profile_object_id") == "tool--example"
        )
        self.assertTrue(
            any(
                item.get("relationship_type") == "uses"
                and item.get("source_ref") == campaign_ref
                and item.get("target_ref") == tool["id"]
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
        indicator = next(
            item
            for item in bundle["objects"]
            if item.get("name") == "domain: scoped.example"
        )
        self.assertTrue(
            any(
                item.get("relationship_type") == "based-on"
                and item.get("source_ref") == indicator["id"]
                and item.get("target_ref") == observable["id"]
                for item in bundle["objects"]
            )
        )

    def test_file_hash_ioc_creates_file_observable(self) -> None:
        observable = observable_object(
            {
                "type": "sha256",
                "value": "a" * 64,
                "normalized_value": "a" * 64,
            }
        )

        self.assertIsNotNone(observable)
        assert observable is not None
        self.assertEqual(observable["type"], "file")
        self.assertEqual(observable["hashes"], {"SHA-256": "a" * 64})

    def test_shared_observable_roles_are_corpus_wide_union(self) -> None:
        first = {
            "type": "domain",
            "normalized_value": "shared.example",
            "disposition": "confirmed",
            "roles": ["c2"],
        }
        second = {
            **first,
            "roles": ["delivery", "free text is not a label"],
        }
        records = [
            {"iocs": {"indicators": [first]}},
            {"iocs": {"indicators": [second]}},
        ]

        role_index = build_observable_role_index(records)
        unlabelled = observable_object(first, roles=[])
        assert unlabelled is not None
        observable = observable_object(
            first, roles=role_index[unlabelled["id"]]
        )

        assert observable is not None
        self.assertEqual(
            observable["x_opencti_labels"], ["c2", "delivery"]
        )
        self.assertEqual(observable["x_ioc_roles"], ["c2", "delivery"])
        self.assertEqual(
            observable["x_ioc_role_scope"], "corpus-observed-uses"
        )

    def test_exact_hunting_pattern_creates_direct_observables(self) -> None:
        first_hash = "A" * 64
        second_hash = "B" * 64
        pivot = stix_base(
            "indicator",
            "hunting-pivot--multi-hash",
            NOW,
            {
                "name": "Hunting pivot: multi-hash",
                "pattern": (
                    f"[file:hashes.'SHA-256' = '{first_hash}' OR "
                    f"file:hashes.'SHA-256' = '{second_hash}']"
                ),
                "pattern_type": "stix",
                "valid_from": CREATED,
                "x_profile_object_id": "hunting-pivot--multi-hash",
                "x_hunting_pivot": True,
                "x_confidence": "high",
            },
        )
        observables = observable_objects_from_indicator_pattern(pivot)

        self.assertEqual(len(observables), 2)
        self.assertEqual(
            {next(iter(item["hashes"].values())) for item in observables},
            {first_hash.lower(), second_hash.lower()},
        )

        full_bundle = fixture_bundle(self.profile)
        full_bundle["objects"].append(pivot)
        objects, _ = prepare_profile_objects(
            self.profile,
            self.record["iocs"],
            full_bundle,
            self.producer["id"],
            COUNTRY_INDEX,
        )
        exported_pivot = next(
            item
            for item in objects
            if item.get("x_profile_object_id") == "hunting-pivot--multi-hash"
        )
        relations = [
            item
            for item in objects
            if item.get("relationship_type") == "based-on"
            and item.get("source_ref") == exported_pivot["id"]
        ]
        self.assertEqual(len(relations), 2)
        self.assertEqual(
            exported_pivot["x_opencti_main_observable_type"], "StixFile"
        )

    def test_wildcard_hunting_pattern_does_not_invent_observable(self) -> None:
        observables = observable_objects_from_indicator_pattern(
            {
                "x_hunting_pivot": True,
                "pattern": (
                    "[domain-name:value MATCHES "
                    "'^[^.]+\\\\.example\\\\.com$']"
                ),
            }
        )

        self.assertEqual(observables, [])

    def test_validator_rejects_indicator_without_based_on_observable(self) -> None:
        activity = self.profile["activities"][0]
        bundle = build_activity_bundle(self.record, activity, self.producer)
        bundle["objects"] = [
            item
            for item in bundle["objects"]
            if item.get("relationship_type") != "based-on"
        ]

        errors = validate_bundle(bundle, expected_scope="campaign")

        self.assertTrue(
            any("exactly one generated based-on" in item for item in errors),
            errors,
        )

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
        relations = [
            item
            for item in bundle["objects"]
            if item.get("type") == "relationship"
        ]
        self.assertEqual(
            sorted(item.get("relationship_type") for item in relations),
            ["based-on", "consists-of"],
        )

    def test_parent_grouping_keeps_child_grouping_definition_identical(self) -> None:
        record = copy.deepcopy(self.record)
        profile = record["profile"]
        parent = profile["activities"][0]
        parent["stix_object_type"] = "grouping"
        parent["grouping_context"] = "suspicious-activity"
        old_parent_ref = profile_scoped_stix_id(
            profile["profile_id"],
            "campaign",
            stix_id("campaign", parent["activity_id"]),
        )
        parent_ref = profile_scoped_stix_id(
            profile["profile_id"],
            "grouping",
            stix_id("grouping", parent["activity_id"]),
        )
        converted: list[dict[str, object]] = []
        for obj in record["objects"]:
            if obj.get("type") == "relationship" and old_parent_ref in {
                obj.get("source_ref"),
                obj.get("target_ref"),
            }:
                continue
            if obj.get("id") == old_parent_ref:
                obj["type"] = "grouping"
                obj["id"] = parent_ref
                obj["context"] = "suspicious-activity"
                obj["object_refs"] = []
                obj["x_stix_object_type"] = "grouping"
            converted.append(obj)
        record["objects"] = converted
        child_id = "activity--child-evidence-grouping"
        child = {
            "activity_id": child_id,
            "name": "Child evidence grouping",
            "activity_type": "information-collection",
            "stix_object_type": "grouping",
            "grouping_context": "suspicious-activity",
            "activity_refs": [],
            "malware_refs": ["malware--example"],
            "tool_refs": ["tool--example"],
            "infrastructure_refs": ["infra--example"],
            "target_refs": ["target--country-example"],
            "ttp_refs": ["ttp--example"],
            "victim_refs": ["victim--example"],
        }
        profile["activities"].append(child)
        parent["activity_refs"] = [child_id]
        child_ref = profile_scoped_stix_id(
            profile["profile_id"], "grouping", stix_id("grouping", child_id)
        )
        record["objects"].append(
            stix_base(
                "grouping",
                f"{profile['profile_id']}:grouping:{stix_id('grouping', child_id)}",
                NOW,
                {
                    "name": child["name"],
                    "context": "suspicious-activity",
                    "object_refs": [],
                    "x_profile_object_id": child_id,
                    "created_by_ref": self.producer["id"],
                },
            )
        )
        # stix_base above uses the same scoped key formula but assert explicitly
        # so a future ID helper change cannot make the fixture silently invalid.
        record["objects"][-1]["id"] = child_ref

        cross_activity_note = stix_base(
            "note",
            "cross-activity-hunting-note",
            NOW,
            {
                "abstract": "Cross-activity note",
                "content": "This note must be sliced, not put in the child grouping.",
                "object_refs": [parent_ref, child_ref],
                "x_profile_hunting_pivot_id": "hunting-pivot--cross-activity",
                "created_by_ref": self.producer["id"],
            },
        )
        record["objects"].append(cross_activity_note)

        parent_bundle = build_activity_bundle(record, parent, self.producer)
        child_bundle = build_activity_bundle(record, child, self.producer)
        self.assertEqual(validate_bundle(parent_bundle, expected_scope="grouping"), [])
        self.assertEqual(validate_bundle(child_bundle, expected_scope="grouping"), [])
        parent_child = next(
            item for item in parent_bundle["objects"] if item["id"] == child_ref
        )
        standalone_child = next(
            item for item in child_bundle["objects"] if item["id"] == child_ref
        )
        self.assertEqual(parent_child, standalone_child)
        self.assertNotIn(cross_activity_note["id"], standalone_child["object_refs"])
        self.assertTrue(
            any(
                item.get("x_profile_object_id") == "tool--example"
                for item in parent_bundle["objects"]
            )
        )

    def test_activity_dependency_cycles_terminate(self) -> None:
        record = copy.deepcopy(self.record)
        profile = record["profile"]
        parent = profile["activities"][0]
        parent["stix_object_type"] = "grouping"
        parent["grouping_context"] = "suspicious-activity"
        child = {
            **copy.deepcopy(parent),
            "activity_id": "activity--cycle-child",
            "name": "Cycle child",
            "activity_refs": [parent["activity_id"]],
        }
        parent["activity_refs"] = [child["activity_id"]]
        profile["activities"].append(child)
        dependencies = campaign_dependency_profile_ids(profile, parent)
        self.assertIn(child["activity_id"], dependencies)
        self.assertIn(parent["activity_id"], dependencies)

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
