#!/usr/bin/env python3
"""Regression tests for hunting pivots and associated-entity STIX output."""

from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "actor_profile" / "scripts"
sys.path.insert(0, str(SCRIPTS))

from apply_hunting_entity_research import (  # noqa: E402
    apply_update,
    canonical_hunting_pivot,
    canonical_update,
    merge_by_id,
)
from render_profile import render_stix  # noqa: E402
from validate_profile import (  # noqa: E402
    Issue,
    validate_observation_time,
    validate_profile,
)


APT41_SHARED_CERT = "hunting-pivot--apt41-gala-lab-cert-serial"
CONFUCIUS_CERT = "hunting-pivot--confucius-asyncrat-tls-certificate"
SANDWORM_DEVICE_PROFILE = (
    "hunting-pivot--sandworm-cyclops-blink-tls-protocol-profile"
)
MEDUSA_DRIVER = "hunting-pivot--medusa-abyssworker-driver-lineage"
MEDUSA_CERTIFICATES = (
    "hunting-pivot--medusa-abyssworker-signing-fingerprints"
)
BLACKBYTE_DRIVERS = "hunting-pivot--blackbyte-four-driver-set-2024"
STORM_0501_PROFILE = "hunting-pivot--storm-0501-beacon-tls-http-profile"
AKIRA_DRIVER_CHAIN = "hunting-pivot--akira-rwdrv-hlpdrv-chain"
LAZARUS_DBUTIL = "hunting-pivot--lazarus-dbutil-driver-2021"
MUSTANG_PANDA_MSAGENT_CERT = (
    "hunting-pivot--mustang-panda-coolclient-msagent-signing-certificate"
)


def load_profile(slug: str) -> dict[str, Any]:
    return json.loads(
        (ROOT / "profiles" / slug / "actor-profile.json").read_text(
            encoding="utf-8"
        )
    )


class HuntingEntityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.profiles = {
            slug: load_profile(slug)
            for slug in (
                "apt41",
                "akira",
                "blackbyte",
                "confucius",
                "ember-bear",
                "indrik-spider",
                "lazarus",
                "medusa-group",
                "mustang-panda",
                "sandworm",
                "storm-0501",
            )
        }
        cls.bundles = {
            slug: render_stix(profile, None, None)
            for slug, profile in cls.profiles.items()
        }

    def pivot(self, slug: str, pivot_id: str) -> dict[str, Any]:
        return next(
            item
            for item in self.profiles[slug]["hunting_pivots"]
            if item["pivot_id"] == pivot_id
        )

    def stix_object(
        self,
        slug: str,
        field: str,
        value: str,
    ) -> dict[str, Any]:
        return next(
            item
            for item in self.bundles[slug]["objects"]
            if item.get(field) == value
        )

    def entity(self, slug: str, entity_id: str) -> dict[str, Any]:
        return next(
            item
            for item in self.profiles[slug]["associated_entities"]
            if item["entity_id"] == entity_id
        )

    def test_apt41_shared_certificate_keeps_both_cluster_observations(
        self,
    ) -> None:
        pivot = self.pivot("apt41", APT41_SHARED_CERT)
        observations = pivot["observations"]

        self.assertEqual(
            {item["observation_id"] for item in observations},
            {
                "pivot-observation--gala-cert-unc3914-2020",
                "pivot-observation--gala-cert-dusttrap-2024",
            },
        )
        self.assertEqual(pivot["observation_count"], 2)
        self.assertEqual(pivot["source_count"], 1)
        self.assertEqual(pivot["activity_count"], 1)
        self.assertEqual(
            pivot["first_observed"]["value"], "2020-01-01T00:00:00Z"
        )
        self.assertIsNone(pivot["last_observed"]["value"])
        self.assertEqual(
            pivot["last_observed"]["basis"], "latest-use-date-not-stated"
        )
        dusttrap_observation = next(
            item
            for item in observations
            if item["observation_id"]
            == "pivot-observation--gala-cert-dusttrap-2024"
        )
        self.assertIsNone(dusttrap_observation["observed_at"]["value"])
        self.assertIn(
            "not-stated", dusttrap_observation["observed_at"]["basis"]
        )
        self.assertEqual(pivot["continuity"]["assessment"], "reused")

        indicator = self.stix_object(
            "apt41", "x_profile_object_id", APT41_SHARED_CERT
        )
        note = self.stix_object(
            "apt41", "x_profile_hunting_pivot_id", APT41_SHARED_CERT
        )
        self.assertEqual(indicator["type"], "indicator")
        self.assertEqual(indicator["x_observation_count"], 2)
        self.assertEqual(indicator["x_source_count"], 1)
        self.assertEqual(indicator["x_activity_count"], 1)
        self.assertIsNone(indicator["x_last_observed"]["value"])
        self.assertEqual(len(note["x_observations"]), 2)
        self.assertEqual(note["x_attribution_scope"], "shared")

    def test_confucius_certificate_does_not_claim_current_activity(self) -> None:
        pivot = self.pivot("confucius", CONFUCIUS_CERT)
        continuity = pivot["continuity"]

        self.assertEqual(continuity["assessment"], "single-observation")
        self.assertEqual(continuity["active_status"], "unknown")
        self.assertFalse(continuity["passive_scan_performed"])

        indicator = self.stix_object(
            "confucius", "x_profile_object_id", CONFUCIUS_CERT
        )
        self.assertEqual(
            indicator["x_continuity"]["active_status"], "unknown"
        )
        self.assertFalse(
            indicator["x_continuity"]["passive_scan_performed"]
        )
        self.assertNotIn("valid_until", indicator)
        self.assertNotIn("revoked", indicator)

    def test_sandworm_per_device_cert_design_is_not_a_stix_pattern(self) -> None:
        pivot = self.pivot("sandworm", SANDWORM_DEVICE_PROFILE)

        self.assertIsNone(pivot["stix_pattern"])
        self.assertIn("per-device generated TLS keys/certificates", pivot["value"])
        self.assertFalse(
            any(
                item.get("type") == "indicator"
                and item.get("x_profile_object_id") == SANDWORM_DEVICE_PROFILE
                for item in self.bundles["sandworm"]["objects"]
            )
        )

        note = self.stix_object(
            "sandworm",
            "x_profile_hunting_pivot_id",
            SANDWORM_DEVICE_PROFILE,
        )
        self.assertEqual(note["type"], "note")
        self.assertEqual(note["x_observation_count"], 2)
        self.assertIn(
            "Do not create a reusable certificate-fingerprint IOC",
            note["x_analyst_notes"],
        )
        query = pivot["hunt_queries"][0]
        self.assertIn("has_ssl:true", query["query"])
        self.assertNotIn(" ssl:true", query["query"])

    def test_vt_first_seen_is_not_promoted_to_medusa_activity_time(self) -> None:
        for pivot_id in (MEDUSA_DRIVER, MEDUSA_CERTIFICATES):
            pivot = self.pivot("medusa-group", pivot_id)
            self.assertIsNone(pivot["first_observed"]["value"])
            self.assertIsNone(pivot["last_observed"]["value"])
            self.assertTrue(
                all(
                    observation["observed_at"]["value"] is None
                    for observation in pivot["observations"]
                )
            )
            self.assertIn(
                "vt-first-seen", pivot["first_observed"]["basis"]
            )

            note = self.stix_object(
                "medusa-group", "x_profile_hunting_pivot_id", pivot_id
            )
            self.assertIsNone(note["x_first_observed"]["value"])
            self.assertIsNone(note["x_last_observed"]["value"])

        indicator = self.stix_object(
            "medusa-group", "x_profile_object_id", MEDUSA_DRIVER
        )
        self.assertIsNone(indicator["x_first_observed"]["value"])
        self.assertIsNone(indicator["x_last_observed"]["value"])
        self.assertNotIn(
            indicator["valid_from"],
            {"2024-08-08T00:00:00Z", "2025-02-24T00:00:00Z"},
        )

    def test_report_dates_are_not_reused_as_activity_observations(self) -> None:
        blackbyte = self.pivot("blackbyte", BLACKBYTE_DRIVERS)
        self.assertIsNone(blackbyte["observations"][0]["observed_at"]["value"])
        self.assertEqual(blackbyte["observation_count"], 4)
        blackbyte_indicator = self.stix_object(
            "blackbyte", "x_profile_object_id", BLACKBYTE_DRIVERS
        )
        self.assertNotEqual(
            blackbyte_indicator["valid_from"], "2024-08-01T00:00:00Z"
        )

        storm = self.pivot("storm-0501", STORM_0501_PROFILE)
        self.assertEqual(
            storm["observations"][0]["observed_at"]["value"],
            "2020-07-01T00:00:00Z",
        )
        self.assertEqual(
            storm["observations"][1]["observed_at"]["value"],
            "2021-06-01T00:00:00Z",
        )
        self.assertEqual(
            storm["last_observed"]["value"], "2021-10-01T00:00:00Z"
        )
        source = next(
            item
            for item in self.profiles["storm-0501"]["sources"]
            if item["source_id"] == "source--mandiant-unc2190-sabbath-2021"
        )
        self.assertEqual(
            source["published_at"]["value"], "2021-11-29T00:00:00Z"
        )

    def test_earliest_known_date_does_not_invent_akira_last_seen(self) -> None:
        pivot = self.pivot("akira", AKIRA_DRIVER_CHAIN)
        self.assertEqual(
            pivot["first_observed"]["value"], "2025-07-15T00:00:00Z"
        )
        self.assertIsNone(pivot["last_observed"]["value"])
        self.assertEqual(
            pivot["last_observed"]["basis"],
            "latest-incident-date-not-stated",
        )

    def test_lazarus_dbutil_is_not_linked_to_different_campaign(self) -> None:
        pivot = self.pivot("lazarus", LAZARUS_DBUTIL)

        self.assertEqual(pivot["activity_refs"], [])
        self.assertEqual(pivot["activity_count"], 0)
        self.assertTrue(
            all(
                observation["activity_ref"] is None
                for observation in pivot["observations"]
            )
        )

    def test_mustang_panda_shared_driver_certificate_keeps_scope_boundary(
        self,
    ) -> None:
        pivot = self.pivot("mustang-panda", MUSTANG_PANDA_MSAGENT_CERT)

        self.assertEqual(pivot["attribution_scope"], "shared")
        self.assertEqual(pivot["observation_count"], 5)
        self.assertEqual(pivot["source_count"], 1)
        self.assertEqual(pivot["activity_count"], 1)
        self.assertTrue(
            all(
                observation["observed_at"]["value"] is None
                for observation in pivot["observations"]
            )
        )
        self.assertIsNone(pivot["first_observed"]["value"])
        self.assertIsNone(pivot["last_observed"]["value"])
        self.assertEqual(pivot["continuity"]["active_status"], "unknown")
        self.assertFalse(pivot["continuity"]["passive_scan_performed"])
        self.assertIn("no evidence linking", pivot["description"])
        self.assertFalse(
            any(
                entity["name"] == "Nanjing Ranyi Technology Co., Ltd."
                for entity in self.profiles["mustang-panda"][
                    "associated_entities"
                ]
            )
        )

        indicator = self.stix_object(
            "mustang-panda",
            "x_profile_object_id",
            MUSTANG_PANDA_MSAGENT_CERT,
        )
        note = self.stix_object(
            "mustang-panda",
            "x_profile_hunting_pivot_id",
            MUSTANG_PANDA_MSAGENT_CERT,
        )
        self.assertEqual(indicator["x_observation_count"], 5)
        self.assertEqual(indicator["x_attribution_scope"], "shared")
        self.assertEqual(len(note["x_observations"]), 2)
        self.assertIn(
            "Nanjing Ranyi Technology Co., Ltd.",
            note["x_pivot_value"],
        )

    def test_hunting_pivot_count_and_live_status_metadata_is_consistent(self) -> None:
        profiles = [
            load_profile(path.parent.name)
            for path in sorted((ROOT / "profiles").glob("*/actor-profile.json"))
        ]
        pivots = [
            pivot
            for profile in profiles
            for pivot in profile.get("hunting_pivots", [])
        ]
        self.assertTrue(pivots)

        for pivot in pivots:
            with self.subTest(pivot_id=pivot["pivot_id"]):
                observations = pivot["observations"]
                self.assertEqual(
                    pivot["observation_count"],
                    sum(item["count"] for item in observations),
                )
                self.assertEqual(
                    pivot["source_count"],
                    len({item["source_ref"] for item in observations}),
                )
                self.assertEqual(
                    pivot["activity_count"],
                    len(
                        {
                            item["activity_ref"]
                            for item in observations
                            if item.get("activity_ref")
                        }
                    ),
                )
                continuity = pivot["continuity"]
                self.assertEqual(continuity["active_status"], "unknown")
                self.assertFalse(continuity["passive_scan_performed"])
                for query in pivot["hunt_queries"]:
                    self.assertTrue(query["requires_validation"])
                    self.assertTrue(query["false_positive_notes"])

    def test_shared_research_entity_and_source_ids_have_identical_definitions(
        self,
    ) -> None:
        research = json.loads(
            (
                ROOT
                / "actor_profile"
                / "osint"
                / "hunting-entity-research.json"
            ).read_text(encoding="utf-8")
        )
        id_fields = {
            "associated_entities": "entity_id",
            "sources": "source_id",
        }
        seen: dict[tuple[str, str], tuple[str, dict[str, Any]]] = {}

        for slug, update in research["profiles"].items():
            for collection, id_field in id_fields.items():
                for item in update.get(collection, []):
                    key = (collection, item[id_field])
                    previous = seen.get(key)
                    if previous is None:
                        seen[key] = (slug, item)
                        continue
                    previous_slug, previous_item = previous
                    self.assertEqual(
                        item,
                        previous_item,
                        f"{key[1]} differs between {previous_slug} and {slug}",
                    )

    def test_hunt_query_requires_validation_and_false_positive_notes(self) -> None:
        profile = copy.deepcopy(self.profiles["apt41"])
        query = profile["hunting_pivots"][0]["hunt_queries"][0]
        query["requires_validation"] = False
        query["false_positive_notes"] = "   "

        issues: list[Issue] = []
        validate_profile(profile, issues)

        messages = {
            (item.location, item.message)
            for item in issues
            if item.severity == "error"
        }
        self.assertTrue(
            any(
                location.endswith(".requires_validation")
                and "must require analyst validation" in message
                for location, message in messages
            )
        )
        self.assertTrue(
            any(
                location.endswith(".false_positive_notes")
                and "must document false-positive conditions" in message
                for location, message in messages
            )
        )

    def test_implicit_pivot_count_basis_stays_unknown(self) -> None:
        raw_pivot = copy.deepcopy(
            self.profiles["apt41"]["hunting_pivots"][0]
        )
        raw_pivot["observations"][0].pop("count_basis")

        canonical = canonical_hunting_pivot(raw_pivot)

        self.assertEqual(
            canonical["observations"][0]["count_basis"], "unknown"
        )
        self.assertEqual(canonical["continuity"]["checks"], [])

    def test_pivot_observation_refs_must_be_declared_by_parent(self) -> None:
        profile = copy.deepcopy(self.profiles["apt41"])
        pivot = profile["hunting_pivots"][0]
        source_ref = pivot["observations"][0]["source_ref"]
        activity_ref = next(
            observation["activity_ref"]
            for observation in pivot["observations"]
            if observation.get("activity_ref")
        )
        pivot["evidence_refs"] = [
            ref for ref in pivot["evidence_refs"] if ref != source_ref
        ]
        pivot["activity_refs"] = [
            ref for ref in pivot["activity_refs"] if ref != activity_ref
        ]

        issues: list[Issue] = []
        validate_profile(profile, issues)
        messages = [item.message for item in issues if item.severity == "error"]

        self.assertTrue(
            any("must include every observation source" in item for item in messages)
        )
        self.assertTrue(
            any("must include every observation activity" in item for item in messages)
        )

    def test_live_status_requires_structured_validated_check(self) -> None:
        profile = copy.deepcopy(self.profiles["apt41"])
        continuity = profile["hunting_pivots"][0]["continuity"]
        continuity["active_status"] = "active"
        continuity["passive_scan_performed"] = True
        continuity["checks"] = []

        issues: list[Issue] = []
        validate_profile(profile, issues)
        messages = [item.message for item in issues if item.severity == "error"]

        self.assertTrue(
            any("requires a structured check record" in item for item in messages)
        )
        self.assertTrue(
            any("requires a validated, evidenced" in item for item in messages)
        )

    def test_organization_and_individual_have_distinct_stix_types(self) -> None:
        organization = self.stix_object(
            "apt41", "x_profile_object_id", "organization--chengdu-404"
        )
        individual = self.stix_object(
            "apt41",
            "x_profile_object_id",
            "threat-actor-individual--jiang-lizhi",
        )

        self.assertEqual(organization["type"], "identity")
        self.assertEqual(organization["identity_class"], "organization")
        self.assertEqual(organization["x_entity_type"], "organization")
        self.assertEqual(individual["type"], "threat-actor")
        self.assertEqual(individual["resource_level"], "individual")
        self.assertEqual(
            individual["x_opencti_type"], "Threat-Actor-Individual"
        )
        self.assertEqual(
            individual["x_entity_type"], "threat-actor-individual"
        )

    def test_threat_actor_group_is_not_merged_with_intrusion_set(self) -> None:
        group = self.stix_object(
            "indrik-spider",
            "x_profile_object_id",
            "threat-actor-group--evil-corp",
        )
        overlap = self.stix_object(
            "indrik-spider",
            "x_profile_relationship_id",
            "entity-relationship--evil-corp-overlaps-indrik-spider",
        )

        self.assertEqual(group["type"], "threat-actor")
        self.assertEqual(group["x_opencti_type"], "Threat-Actor-Group")
        self.assertEqual(group["resource_level"], "organization")
        self.assertEqual(group["x_entity_type"], "threat-actor-group")
        self.assertEqual(overlap["relationship_type"], "related-to")
        self.assertEqual(
            overlap["x_profile_relationship_type"], "overlaps-with"
        )
        self.assertTrue(overlap["source_ref"].startswith("threat-actor--"))
        self.assertTrue(overlap["target_ref"].startswith("intrusion-set--"))

    def test_threat_actor_group_requires_group_id_prefix(self) -> None:
        profile = copy.deepcopy(self.profiles["indrik-spider"])
        group = next(
            entity
            for entity in profile["associated_entities"]
            if entity["entity_type"] == "threat-actor-group"
        )
        old_id = group["entity_id"]
        group["entity_id"] = "threat-actor-individual--evil-corp"
        for relationship in profile["entity_relationships"]:
            for field in ("source_ref", "target_ref"):
                if relationship.get(field) == old_id:
                    relationship[field] = group["entity_id"]

        issues: list[Issue] = []
        validate_profile(profile, issues)

        self.assertTrue(
            any(
                item.severity == "error"
                and item.message
                == "threat-actor-group ID must start with threat-actor-group--"
                for item in issues
            )
        )

    def test_indrik_legal_dates_do_not_reuse_publication_dates(self) -> None:
        for entity_id in (
            "threat-actor-individual--maksim-yakubets",
            "threat-actor-individual--igor-turashev",
        ):
            indictment = next(
                action
                for action in self.entity("indrik-spider", entity_id)[
                    "legal_actions"
                ]
                if action["action_type"] == "indictment"
            )
            self.assertEqual(
                indictment["action_date"]["value"],
                "2019-11-12T00:00:00Z",
            )
            self.assertEqual(
                indictment["action_date"]["basis"],
                "indictment-filed-date",
            )

        ryzhenkov_actions = {
            action["action_type"]: action
            for action in self.entity(
                "indrik-spider",
                "threat-actor-individual--aleksandr-ryzhenkov",
            )["legal_actions"]
        }
        self.assertIsNone(
            ryzhenkov_actions["indictment"]["action_date"]["value"]
        )
        self.assertEqual(
            ryzhenkov_actions["indictment"]["action_date"]["basis"],
            "indictment-return-date-not-stated",
        )
        self.assertEqual(
            ryzhenkov_actions["wanted"]["action_date"]["value"],
            "2023-03-22T00:00:00Z",
        )
        self.assertEqual(
            ryzhenkov_actions["wanted"]["action_date"]["basis"],
            "federal-arrest-warrant-issued-date",
        )

    def test_evil_corp_sanctions_cover_people_and_companies(self) -> None:
        sanctioned_2019_people = {
            "threat-actor-individual--maksim-yakubets",
            "threat-actor-individual--igor-turashev",
            "threat-actor-individual--denis-gusev",
            "threat-actor-individual--dmitriy-smirnov",
            "threat-actor-individual--artem-yakubets",
            "threat-actor-individual--ivan-tuchkov",
            "threat-actor-individual--andrey-plotnitskiy",
            "threat-actor-individual--dmitriy-slobodskoy",
            "threat-actor-individual--kirill-slobodskoy",
            "threat-actor-individual--aleksei-bashlikov",
            "threat-actor-individual--ruslan-zamulko",
            "threat-actor-individual--david-guberman",
            "threat-actor-individual--carlos-alvares",
            "threat-actor-individual--georgios-manidis",
            "threat-actor-individual--tatiana-shevchuk",
            "threat-actor-individual--azamat-safarov",
            "threat-actor-individual--gulsara-burkhonova",
        }
        sanctioned_2019_entities = {
            "threat-actor-group--evil-corp",
            "organization--biznes-stolitsa",
            "organization--optima-ooo",
            "organization--treid-invest",
            "organization--tsao-ooo",
            "organization--vertikal-ooo",
            "organization--yunikom-ooo",
        }
        profile_entities = {
            item["entity_id"]: item
            for item in self.profiles["indrik-spider"][
                "associated_entities"
            ]
        }
        self.assertTrue(
            sanctioned_2019_people | sanctioned_2019_entities
            <= profile_entities.keys()
        )
        self.assertIn(
            "Dridex Gang",
            profile_entities["threat-actor-group--evil-corp"]["aliases"],
        )
        self.assertEqual(
            profile_entities["threat-actor-individual--maksim-yakubets"][
                "aliases"
            ],
            ["AQUA"],
        )
        self.assertEqual(
            set(
                profile_entities[
                    "threat-actor-individual--igor-turashev"
                ]["aliases"]
            ),
            {"ENKI", "NINTUTU"},
        )
        for entity_id in sanctioned_2019_people | sanctioned_2019_entities:
            sanction = next(
                action
                for action in profile_entities[entity_id]["legal_actions"]
                if action["action_type"] == "sanction"
                and action["action_date"]["value"]
                == "2019-12-05T00:00:00Z"
            )
            self.assertEqual(sanction["status"], "completed")

        for entity_id in sanctioned_2019_entities - {
            "threat-actor-group--evil-corp"
        }:
            self.assertEqual(
                profile_entities[entity_id]["entity_type"], "organization"
            )

        for entity_id in (
            "organization--vympel-assistance",
            "organization--solar-invest",
        ):
            sanction = profile_entities[entity_id]["legal_actions"][0]
            self.assertEqual(sanction["action_type"], "sanction")
            self.assertEqual(
                sanction["action_date"]["value"],
                "2024-10-01T00:00:00Z",
            )

        financial_facilitator_ids = {
            "threat-actor-individual--aleksei-bashlikov",
            "threat-actor-individual--ruslan-zamulko",
            "threat-actor-individual--david-guberman",
            "threat-actor-individual--carlos-alvares",
            "threat-actor-individual--georgios-manidis",
            "threat-actor-individual--tatiana-shevchuk",
            "threat-actor-individual--azamat-safarov",
            "threat-actor-individual--gulsara-burkhonova",
        }
        relationships = self.profiles["indrik-spider"][
            "entity_relationships"
        ]
        for entity_id in financial_facilitator_ids:
            relationship = next(
                item
                for item in relationships
                if item["source_ref"] == entity_id
            )
            self.assertEqual(
                relationship["relationship_type"],
                "provides-financial-and-material-assistance-to",
            )
            self.assertIsNone(relationship["first_observed"]["value"])
            self.assertIsNone(relationship["last_observed"]["value"])

    def test_unit29155_uk_sanctions_keep_action_dates_distinct(self) -> None:
        expected_dates = {
            "organization--gru-unit-29155": "2025-07-18T00:00:00Z",
            "threat-actor-individual--yuriy-denisov": (
                "2025-07-18T00:00:00Z"
            ),
            "threat-actor-individual--vladislav-borovkov": (
                "2025-07-18T00:00:00Z"
            ),
            "threat-actor-individual--nikolay-korchagin": (
                "2025-07-18T00:00:00Z"
            ),
            "threat-actor-individual--vitaliy-shevchenko": (
                "2025-07-18T00:00:00Z"
            ),
            "threat-actor-individual--denis-denisenko": (
                "2025-12-04T00:00:00Z"
            ),
            "threat-actor-individual--dmitriy-goloshubov": (
                "2025-12-04T00:00:00Z"
            ),
        }
        for entity_id, expected_date in expected_dates.items():
            entity = self.entity("ember-bear", entity_id)
            sanctions = [
                action
                for action in entity["legal_actions"]
                if action["authority"] == "United Kingdom"
            ]
            self.assertEqual(len(sanctions), 1)
            self.assertEqual(
                sanctions[0]["action_date"]["value"], expected_date
            )
            self.assertEqual(
                sanctions[0]["action_date"]["basis"], "sanctions-date"
            )

        stigal = self.entity(
            "ember-bear", "threat-actor-individual--amin-stigal"
        )
        self.assertFalse(
            any(
                action["authority"] == "United Kingdom"
                for action in stigal["legal_actions"]
            )
        )
        self.assertEqual(
            {
                action["action_date"]["value"]
                for action in stigal["legal_actions"]
                if action["action_type"] == "indictment"
            },
            {"2024-06-25T00:00:00Z", "2024-08-07T00:00:00Z"},
        )

    def test_russian_person_and_cluster_boundaries_remain_explicit(self) -> None:
        evil_corp_members = {
            "threat-actor-individual--viktor-yakubets",
            "threat-actor-individual--sergey-ryzhenkov",
            "threat-actor-individual--aleksey-shchetinin",
            "threat-actor-individual--beyat-ramazanov",
            "threat-actor-individual--vadim-pogodin",
        }
        indrik_entities = {
            item["entity_id"]: item
            for item in self.profiles["indrik-spider"][
                "associated_entities"
            ]
        }
        self.assertTrue(evil_corp_members <= indrik_entities.keys())
        for entity_id in evil_corp_members:
            entity = indrik_entities[entity_id]
            self.assertEqual(entity["entity_type"], "threat-actor-individual")
            sanction = next(
                action
                for action in entity["legal_actions"]
                if action["action_type"] == "sanction"
            )
            self.assertEqual(
                sanction["action_date"]["value"],
                "2024-10-01T00:00:00Z",
            )
            membership = next(
                item
                for item in self.profiles["indrik-spider"][
                    "entity_relationships"
                ]
                if item["source_ref"] == entity_id
            )
            self.assertEqual(
                membership["target_ref"], "threat-actor-group--evil-corp"
            )
            self.assertIsNone(membership["first_observed"]["value"])
            self.assertIsNone(membership["last_observed"]["value"])

        unit_29155_defendants = {
            "threat-actor-individual--yuriy-denisov",
            "threat-actor-individual--vladislav-borovkov",
            "threat-actor-individual--denis-denisenko",
            "threat-actor-individual--dmitriy-goloshubov",
            "threat-actor-individual--nikolay-korchagin",
            "threat-actor-individual--amin-stigal",
        }
        ember_entities = {
            item["entity_id"]: item
            for item in self.profiles["ember-bear"]["associated_entities"]
        }
        self.assertTrue(unit_29155_defendants <= ember_entities.keys())
        for entity_id in unit_29155_defendants:
            entity = ember_entities[entity_id]
            self.assertEqual(entity["entity_type"], "threat-actor-individual")
            action_types = {
                action["action_type"]: action
                for action in entity["legal_actions"]
            }
            self.assertEqual(action_types["indictment"]["status"], "alleged")
            self.assertEqual(action_types["wanted"]["status"], "pending")
            self.assertEqual(
                action_types["indictment"]["action_date"]["value"],
                "2024-08-07T00:00:00Z",
            )

        bashev = ember_entities["threat-actor-individual--evgeniy-bashev"]
        self.assertEqual(
            {action["authority"] for action in bashev["legal_actions"]},
            {"European Union", "United Kingdom"},
        )
        self.assertFalse(
            any(
                "actor--ember-bear"
                in (item["source_ref"], item["target_ref"])
                for item in self.profiles["ember-bear"][
                    "entity_relationships"
                ]
            )
        )

    def test_nonstandard_relationship_keeps_original_profile_type(self) -> None:
        relationship = self.stix_object(
            "apt41",
            "x_profile_relationship_id",
            "entity-relationship--chengdu404-supports-apt41",
        )

        self.assertEqual(relationship["type"], "relationship")
        self.assertEqual(relationship["relationship_type"], "related-to")
        self.assertEqual(
            relationship["x_profile_relationship_type"], "alleged-supports"
        )
        self.assertTrue(relationship["source_ref"].startswith("identity--"))
        self.assertTrue(
            relationship["target_ref"].startswith("intrusion-set--")
        )

    def test_indictments_remain_allegations_in_profile_and_stix(self) -> None:
        profile_indictments = [
            action
            for slug in ("apt41", "sandworm")
            for entity in self.profiles[slug]["associated_entities"]
            for action in entity.get("legal_actions", [])
            if action["action_type"] == "indictment"
        ]
        self.assertTrue(profile_indictments)
        self.assertEqual(
            {action["status"] for action in profile_indictments}, {"alleged"}
        )

        stix_indictments = [
            item
            for slug in ("apt41", "sandworm")
            for item in self.bundles[slug]["objects"]
            if item.get("x_legal_action_type") == "indictment"
        ]
        self.assertEqual(len(stix_indictments), len(profile_indictments))
        self.assertEqual(
            {item["x_legal_status"] for item in stix_indictments},
            {"alleged"},
        )

        arrest = self.stix_object(
            "apt41",
            "x_profile_legal_action_id",
            "legal-action--ling-yang-ching-arrest-2020",
        )
        self.assertEqual(arrest["x_legal_status"], "completed")

    def test_observation_counts_sum_events_and_deduplicate_scopes(self) -> None:
        pivot = canonical_hunting_pivot(
            {
                "pivot_id": "hunting-pivot--count-regression",
                "category": "infrastructure",
                "pivot_type": "test-pivot",
                "value": "test-value",
                "observations": [
                    {
                        "observation_id": "observation--one",
                        "observed_at": {
                            "value": "2024-03-01T00:00:00Z",
                            "precision": "day",
                            "basis": "source-stated",
                        },
                        "source_ref": "source--one",
                        "activity_ref": "activity--one",
                        "count": 2,
                    },
                    {
                        "observation_id": "observation--two",
                        "observed_at": {
                            "value": "2023-02-01T00:00:00Z",
                            "precision": "day",
                            "basis": "source-stated",
                        },
                        "source_ref": "source--one",
                        "activity_ref": "activity--one",
                        "count": 3,
                    },
                    {
                        "observation_id": "observation--three",
                        "observed_at": {
                            "value": "2025-04-01T00:00:00Z",
                            "precision": "day",
                            "basis": "source-stated",
                        },
                        "source_ref": "source--two",
                        "count": 1,
                    },
                ],
            }
        )

        self.assertEqual(pivot["observation_count"], 6)
        self.assertEqual(pivot["source_count"], 2)
        self.assertEqual(pivot["activity_count"], 1)
        self.assertEqual(
            pivot["evidence_refs"], ["source--one", "source--two"]
        )
        self.assertEqual(
            pivot["first_observed"]["value"], "2023-02-01T00:00:00Z"
        )
        self.assertEqual(
            pivot["last_observed"]["value"], "2025-04-01T00:00:00Z"
        )

    def test_research_merge_preserves_existing_source_order(self) -> None:
        merged = merge_by_id(
            [
                {"source_id": "source--z", "title": "Z"},
                {"source_id": "source--a", "title": "old"},
            ],
            [
                {"source_id": "source--a", "title": "updated"},
                {"source_id": "source--m", "title": "new"},
            ],
            "source_id",
        )

        self.assertEqual(
            [item["source_id"] for item in merged],
            ["source--z", "source--a", "source--m"],
        )
        self.assertEqual(merged[1]["title"], "updated")

    def test_web_research_sources_keep_unknown_access_time_explicit(self) -> None:
        update = canonical_update(
            {
                "sources": [
                    {
                        "source_id": "source--web",
                        "title": "Primary report",
                        "publisher": "Example CERT",
                        "url": "https://example.invalid/report",
                    }
                ],
                "hunting_pivots": [
                    {
                        "pivot_id": "hunting-pivot--metadata-regression",
                        "category": "infrastructure",
                        "pivot_type": "tls-fingerprint",
                        "value": "example",
                        "observations": [
                            {
                                "observation_id": "pivot-observation--metadata",
                                "source_ref": "source--web",
                            }
                        ],
                    }
                ],
            }
        )
        source = update["sources"][0]

        self.assertIsNone(source["accessed_at"])
        self.assertIn(
            "access timestamp was not preserved", source["analyst_notes"]
        )
        self.assertEqual(source["actor_scope"], "direct")
        self.assertEqual(
            source["claims_supported"],
            ["hunting-pivot", "infrastructure"],
        )

    def test_explicit_unknown_last_observed_is_not_inferred_from_snapshot(self) -> None:
        pivot = canonical_hunting_pivot(
            {
                "pivot_id": "hunting-pivot--unknown-last-regression",
                "category": "infrastructure",
                "pivot_type": "example",
                "value": "example",
                "observations": [
                    {
                        "observation_id": "pivot-observation--known-start",
                        "observed_at": {
                            "value": "2019-06-01T00:00:00Z",
                            "precision": "month",
                            "basis": "active-since",
                        },
                        "source_ref": "source--one",
                    }
                ],
                "last_observed": {"basis": "last-use-not-stated"},
            }
        )

        self.assertEqual(
            pivot["first_observed"]["value"], "2019-06-01T00:00:00Z"
        )
        self.assertIsNone(pivot["last_observed"]["value"])
        self.assertEqual(
            pivot["last_observed"]["basis"], "last-use-not-stated"
        )

    def test_non_activity_metadata_is_rejected_as_observation_time(self) -> None:
        for basis in (
            "vt-first-seen",
            "virustotal_first_seen",
            "certificate-validity-not-before",
        ):
            with self.subTest(basis=basis):
                issues: list[Issue] = []
                validate_observation_time(
                    {
                        "value": "2025-01-01T00:00:00Z",
                        "precision": "day",
                        "status": "known",
                        "basis": basis,
                    },
                    "$.observed_at",
                    issues,
                )
                self.assertTrue(
                    any(
                        item.severity == "error"
                        and "cannot be used as an activity observation date"
                        in item.message
                        for item in issues
                    )
                )

    def test_research_update_can_remove_superseded_records(self) -> None:
        profile = {
            "sources": [],
            "associated_entities": [
                {"entity_id": "organization--keep"},
                {"entity_id": "organization--remove"},
            ],
            "entity_relationships": [
                {"relationship_id": "entity-relationship--remove"}
            ],
            "hunting_pivots": [],
        }

        changed = apply_update(
            profile,
            {
                "remove_ids": {
                    "associated_entities": ["organization--remove"],
                    "entity_relationships": [
                        "entity-relationship--remove"
                    ],
                }
            },
        )

        self.assertTrue(changed)
        self.assertEqual(
            [item["entity_id"] for item in profile["associated_entities"]],
            ["organization--keep"],
        )
        self.assertEqual(profile["entity_relationships"], [])


if __name__ == "__main__":
    unittest.main()
