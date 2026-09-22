from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class AbandonedBranchReconciliationTests(unittest.TestCase):
    def test_every_unique_abandoned_branch_commit_has_a_recorded_disposition(self) -> None:
        state = json.loads(
            (ROOT / "parse-daily/state.json").read_text(encoding="utf-8")
        )["abandoned_branch_reconciliation"]

        expected = {
            "f46ba8d8b",
            "332ebdc6a",
            "c44736f7d",
            "d571d97d3",
            "9f7efa80e",
            "7cb9966a6",
            "1a9de6fa1",
            "5d338891b",
            "f4c40c352",
        }
        self.assertEqual(set(state["source_commits"]), expected)
        covered = {
            commit
            for record in state["records"]
            for commit in record["source_commits"]
        }
        self.assertEqual(covered, expected)
        equivalent = state["patch_equivalent_branches"]
        self.assertEqual(
            equivalent[0]["branch"],
            "origin/fix/confirmed-profile-corrections-20260919",
        )
        self.assertEqual(equivalent[0]["decision"], "no-unique-patch")

        gunra = next(
            record for record in state["records"] if record.get("subject") == "Gunra"
        )
        self.assertEqual(
            gunra["decision"], "selective-activity-and-observable-integration"
        )
        self.assertIn("exact IOC 11件", gunra["boundary"])
        self.assertIn("hunting artifact 17件", gunra["boundary"])
        self.assertIn("Lazarus/COPPERHEDGE", gunra["boundary"])

    def test_storm_2603_zoho_assist_is_a_non_encrypting_incident(self) -> None:
        profile = json.loads(
            (ROOT / "profiles/storm-2603/actor-profile.json").read_text(encoding="utf-8")
        )
        activity = next(
            item
            for item in profile["activities"]
            if item["activity_id"]
            == "activity--storm-2603--zoho-assist-incident-2026"
        )

        self.assertEqual(activity["stix_object_type"], "incident")
        self.assertEqual(activity["first_observed"]["status"], "unknown")
        self.assertEqual(activity["last_observed"]["status"], "unknown")
        self.assertEqual(activity["target_refs"], [])
        self.assertEqual(activity["malware_refs"], [])
        self.assertEqual(
            activity["tool_refs"], ["tool--zoho-assist-unattended-agent"]
        )
        self.assertEqual(
            activity["diamond_model"]["capability"]["tool_refs"],
            ["tool--zoho-assist-unattended-agent"],
        )
        self.assertIn("暗号化には至っておらず", activity["description"])

        self.assertEqual(profile["attribution"]["countries"], ["China"])
        self.assertEqual(profile["attribution"]["sponsor_type"], "unknown")
        self.assertIn(
            "source--microsoft-toolshell-2025",
            profile["attribution"]["evidence_refs"],
        )
        self.assertEqual(profile["targets"]["countries"], [])

        tools = {item["id"]: item for item in profile["capabilities"]["tools"]}
        self.assertIn("tool--zoho-assist-unattended-agent", tools)
        self.assertIn("正規", tools["tool--zoho-assist-unattended-agent"]["description"])

        source = next(
            item
            for item in profile["sources"]
            if item["source_id"] == "source--talos-ir-trends-q2-2026"
        )
        self.assertEqual(source["published_at"]["value"], "2026-07-28T00:00:00Z")

        stix = json.loads(
            (ROOT / "profiles/storm-2603/generated/profile.stix2.json").read_text(
                encoding="utf-8"
            )
        )
        tool = next(
            item
            for item in stix["objects"]
            if item.get("type") == "tool"
            and item.get("name") == "Zoho Assist Unattended Agent"
        )
        incident = next(
            item
            for item in stix["objects"]
            if item.get("type") == "incident"
            and item.get("name")
            == "Storm-2603によるZoho Assist Unattended Agent展開事例"
        )
        self.assertTrue(
            any(
                item.get("type") == "relationship"
                and item.get("relationship_type") == "uses"
                and item.get("source_ref") == incident["id"]
                and item.get("target_ref") == tool["id"]
                for item in stix["objects"]
            )
        )

    def test_teampcp_legal_actions_are_person_specific(self) -> None:
        profile = json.loads(
            (ROOT / "profiles/teampcp/actor-profile.json").read_text(encoding="utf-8")
        )
        entities = {item["entity_id"]: item for item in profile["associated_entities"]}
        thomson = entities["threat-actor-individual--ruben-ian-thomson"]
        gaebler = entities["threat-actor-individual--louis-michael-gaebler"]

        self.assertEqual(
            {item["action_type"] for item in thomson["legal_actions"]},
            {"arrest", "charge", "indictment"},
        )
        self.assertEqual(
            {item["action_type"] for item in gaebler["legal_actions"]},
            {"arrest", "charge"},
        )
        indictment = next(
            item for item in thomson["legal_actions"] if item["action_type"] == "indictment"
        )
        self.assertEqual(indictment["action_date"]["value"], "2026-08-25T00:00:00Z")
        self.assertEqual(indictment["status"], "alleged")
        for person in (thomson, gaebler):
            for action in person["legal_actions"]:
                if action["action_type"] in {"arrest", "charge"}:
                    self.assertEqual(
                        action["action_date"]["value"], "2026-08-26T00:00:00Z"
                    )
        self.assertEqual(gaebler["countries"], [])
        self.assertTrue(
            all(
                item["relationship_type"] == "alleged-member-of"
                for item in profile["entity_relationships"]
                if "teampcp" in item["relationship_id"]
            )
        )

    def test_silent_librarian_campaign_and_legal_entities_are_separated(self) -> None:
        profile = json.loads(
            (ROOT / "profiles/silent-librarian/actor-profile.json").read_text(
                encoding="utf-8"
            )
        )
        campaign = next(
            item
            for item in profile["activities"]
            if item["activity_id"]
            == "activity--silent-librarian-mabna-campaign-2013-2017"
        )
        self.assertEqual(campaign["stix_object_type"], "campaign")
        self.assertEqual(campaign["first_observed"]["value"], "2013-01-01T00:00:00Z")
        self.assertEqual(campaign["last_observed"]["value"], "2017-12-01T00:00:00Z")
        self.assertEqual(campaign["reported_at"]["value"], "2018-03-23T00:00:00Z")
        self.assertEqual(campaign["reported_at"]["basis"], "source-publication")
        self.assertNotIn("HBO", campaign["description"])
        self.assertIn("target--silent-librarian--country--japan", campaign["target_refs"])
        self.assertEqual(profile["attribution"]["countries"], ["Iran"])
        self.assertEqual(profile["attribution"]["sponsor_type"], "state-aligned")
        self.assertEqual(profile["attribution"]["confidence"], "medium")
        self.assertEqual(
            profile["attribution"]["organizations"][0]["id"],
            "organization--islamic-revolutionary-guard-corps",
        )
        self.assertIn(
            "allegation", profile["attribution"]["analyst_notes"].lower()
        )

        entities = {item["entity_id"]: item for item in profile["associated_entities"]}
        individuals = [
            item
            for item in entities.values()
            if item["entity_type"] == "threat-actor-individual"
        ]
        self.assertEqual(len(individuals), 17)
        self.assertIn("organization--mabna-institute", entities)
        self.assertEqual(
            sum(
                action["action_type"] == "indictment"
                and action["action_id"].endswith("indictment-2026-us")
                for item in individuals
                for action in item["legal_actions"]
            ),
            17,
        )
        self.assertEqual(
            sum(
                action["action_type"] == "sanction"
                for item in entities.values()
                for action in item["legal_actions"]
            ),
            11,
        )
        for item in individuals:
            action = next(
                action
                for action in item["legal_actions"]
                if action["action_id"].endswith("indictment-2026-us")
            )
            self.assertEqual(action["status"], "alleged")
            self.assertEqual(action["action_date"]["status"], "unknown")
        for item in individuals:
            for action in item["legal_actions"]:
                if action["action_type"] == "indictment":
                    self.assertEqual(action["action_date"]["status"], "unknown")
                elif action["action_type"] == "sanction":
                    self.assertEqual(
                        action["action_date"]["value"], "2018-03-23T00:00:00Z"
                    )
        victim = next(
            item
            for item in profile["victim_cases"]
            if item["victim_case_id"] == "victim--activity-rule--a3fd052f21deca13b807"
        )
        self.assertEqual(victim["case_status"], "alleged")
        self.assertEqual(
            {impact["impact_type"] for impact in victim["impacts"]}, {"data-theft"}
        )

    def test_goffee_campaign_ioc_scopes_and_unknown_clusters(self) -> None:
        profile = json.loads(
            (ROOT / "profiles/goffee/actor-profile.json").read_text(encoding="utf-8")
        )
        iocs = json.loads(
            (ROOT / "profiles/goffee/iocs.json").read_text(encoding="utf-8")
        )["indicators"]
        campaigns = {item["activity_id"]: item for item in profile["activities"]}
        march_id = "activity--goffee-warprat-powertaskel-v2-2026"
        q2_id = "activity--goffee-q2-container-campaign-2026"
        self.assertEqual(
            campaigns[march_id]["malware_refs"],
            ["malware--goffee-powertaskel-v2", "malware--goffee-warprat"],
        )
        self.assertEqual(
            campaigns[march_id]["tool_refs"],
            ["tool--goffee-mythic", "tool--goffee-inno-setup"],
        )
        march_victim = next(
            item
            for item in profile["victim_cases"]
            if march_id in item.get("activity_refs", [])
        )
        self.assertEqual(
            march_victim["malware_refs"],
            ["malware--goffee-powertaskel-v2", "malware--goffee-warprat"],
        )
        self.assertEqual(campaigns[q2_id]["stix_object_type"], "campaign")
        self.assertEqual(
            campaigns[q2_id]["tool_refs"],
            [
                "tool--goffee-mythic",
                "tool--goffee-powershell",
                "tool--goffee-certutil",
                "tool--goffee-mshta",
                "tool--goffee-installutil",
                "tool--goffee-pgadmin",
            ],
        )
        tools = {item["id"]: item for item in profile["capabilities"]["tools"]}
        mythic = tools["tool--goffee-mythic"]
        self.assertEqual(
            mythic["last_observed"]["value"], "2026-06-01T00:00:00Z"
        )
        self.assertIn(
            "source--kaspersky-goffee-q2-containers-2026",
            mythic["evidence_refs"],
        )
        for campaign_id in (march_id, q2_id):
            for tool_ref in campaigns[campaign_id]["tool_refs"]:
                self.assertTrue(
                    set(campaigns[campaign_id]["evidence_refs"])
                    & set(tools[tool_ref]["evidence_refs"])
                )

        def linked(indicator: dict, campaign_id: str) -> bool:
            return any(
                campaign_id in observation.get("campaign_refs", [])
                for observation in indicator.get("observations", [])
            )

        self.assertEqual(sum(linked(item, march_id) for item in iocs), 56)
        self.assertEqual(sum(linked(item, q2_id) for item in iocs), 86)
        validssl = next(item for item in iocs if item["value"] == "validsslcheck.com")
        self.assertEqual(
            validssl["malware_refs"],
            ["malware--goffee-powertaskel-v2", "malware--goffee-warprat"],
        )
        q2_known = [
            observation
            for item in iocs
            for observation in item.get("observations", [])
            if q2_id in observation.get("campaign_refs", [])
            and observation["observed_at"]["status"] == "known"
        ]
        self.assertEqual(len(q2_known), 2)
        self.assertEqual({item["raw_value"] for item in q2_known}, {"hepog.org"})
        march_known = [
            observation
            for item in iocs
            for observation in item.get("observations", [])
            if march_id in observation.get("campaign_refs", [])
            and observation["observed_at"]["status"] == "known"
        ]
        self.assertEqual(march_known, [])

        ledger = json.loads(
            (ROOT / "parse-daily/unknown-clusters.json").read_text(encoding="utf-8")
        )
        clusters = {item["cluster_id"]: item for item in ledger["clusters"]}
        self.assertEqual(clusters["unknown-cluster--quicsilver"]["entity_type"], "campaign")
        self.assertEqual(clusters["unknown-cluster--cameraswarm"]["entity_type"], "campaign")
        self.assertIn("2026-07-23", clusters["unknown-cluster--cameraswarm"]["observations"][0]["activity_period"])
        self.assertEqual(
            clusters["unknown-cluster--thehatman"]["attribution"]["state"],
            "self-claimed-unverified",
        )
        heartless_relation = clusters["unknown-cluster--heartlesssoul"]["related_profiles"][0]
        self.assertEqual(clusters["unknown-cluster--heartlesssoul"]["entity_type"], "threat-cluster")
        self.assertEqual(heartless_relation["confidence"], "medium")
        self.assertNotIn("unknown-cluster--medusa", clusters)


if __name__ == "__main__":
    unittest.main()
