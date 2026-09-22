from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def load_json(relative_path: str):
    return json.loads((ROOT / relative_path).read_text(encoding="utf-8"))


class EvidenceSafeDataBoundaryTests(unittest.TestCase):
    def test_actor_origin_countries_are_not_retained_as_victim_targets(self) -> None:
        expectations = {
            "salt-typhoon": ({"中国"}, {"インド", "米国"}),
            "callisto": ({"ロシア"}, set()),
            "daggerfly": ({"中国"}, set()),
            "unc3886": ({"中国"}, {"シンガポール", "米国"}),
            "apt28": ({"ロシア"}, {"ポーランド", "ウクライナ"}),
            "turla": ({"ロシア"}, {"インド", "ウクライナ"}),
            "unc5812": ({"ロシア"}, {"ウクライナ"}),
        }
        for slug, (excluded, retained) in expectations.items():
            with self.subTest(slug=slug):
                profile = load_json(f"profiles/{slug}/actor-profile.json")
                countries = {
                    item["name"] for item in profile["targets"]["countries"]
                }
                self.assertTrue(excluded.isdisjoint(countries))
                self.assertTrue(retained.issubset(countries))

        callisto = load_json("profiles/callisto/actor-profile.json")
        self.assertIn(
            "NATO加盟国",
            {item["name"] for item in callisto["targets"]["regions"]},
        )

    def test_toy_ghouls_keeps_head_mare_out_of_the_july_incident(self) -> None:
        profile = load_json("profiles/toy-ghouls/actor-profile.json")
        iocs = load_json("profiles/toy-ghouls/iocs.json")
        activities = {item["activity_id"]: item for item in profile["activities"]}
        ttps = {item["ttp_id"]: item for item in profile["ttps"]}

        july = activities["activity--toy-ghouls-july-2025-construction-incident"]
        self.assertNotIn(
            "infrastructure--toy-ghouls-head-mare-shared",
            july["infrastructure_refs"],
        )
        self.assertNotIn(
            "ttp--toy-ghouls-head-mare-shared-proxy-observation",
            july["ttp_refs"],
        )
        for ttp_ref in july["ttp_refs"]:
            self.assertNotIn(
                "infrastructure--toy-ghouls-head-mare-shared",
                ttps[ttp_ref]["infrastructure_refs"],
            )

        shared = ttps["ttp--toy-ghouls-head-mare-shared-proxy-observation"]
        self.assertEqual(
            shared["activity_refs"], ["activity--toy-ghouls-ransomware-2025-2026"]
        )
        self.assertEqual(
            shared["evidence_refs"], ["source--kaspersky-toy-ghouls-2026-03-12"]
        )

        expected = {
            "195.133.32.213": "indicator--sha256:3f23c7790795429fc6ba24fc3144fca828d864f08d6e76e4b61c69248f7b94b5",
            "meet.element.tw": "indicator--sha256:ef2c28bc99d58cac5212ccfdd044f9c7bf8ac416776d9a3b2f9fd69669b86bfa",
        }
        pivots = {item["value"]: item for item in profile["hunting_pivots"]}
        indicator_ids = {item["indicator_id"] for item in iocs["indicators"]}
        for value, indicator_id in expected.items():
            self.assertEqual(pivots[value]["indicator_refs"], [indicator_id])
            self.assertIn(indicator_id, indicator_ids)

        f6_source = next(
            item
            for item in profile["sources"]
            if item["source_id"] == "source--f6-bearlyfy-2025-09-23"
        )
        self.assertEqual(
            f6_source["archive_url"],
            "https://web.archive.org/web/20251006200710id_/https://www.f6.ru/blog/bearlyfy/",
        )
        self.assertEqual(
            f6_source["sha256"],
            "baca14b555e6dbcc26516f079c9dee019185772a5938c5e67bac65fc143e5fc1",
        )
        self.assertNotIn("検索インデックス", f6_source["analyst_notes"])

    def test_unknown_cluster_dates_and_capability_categories_are_source_scoped(self) -> None:
        ledger = load_json("parse-daily/unknown-clusters.json")
        clusters = {item["cluster_id"]: item for item in ledger["clusters"]}

        quicsilver = clusters["unknown-cluster--quicsilver"]
        self.assertEqual((quicsilver["first_seen"], quicsilver["last_seen"]), ("2026-04", "2026-07"))
        quic_observation = quicsilver["observations"][0]
        self.assertIsNone(quic_observation["observed_on"])
        self.assertEqual(quic_observation["tools"], ["ftp.exe"])
        self.assertEqual(quic_observation["delivery_formats"], ["VHD", "LNK"])
        self.assertEqual(quic_observation["services"], ["Cloudflare Workers"])

        cameraswarm = clusters["unknown-cluster--cameraswarm"]
        self.assertEqual(
            (cameraswarm["first_seen"], cameraswarm["last_seen"]),
            ("2026-06-17", "2026-07-23"),
        )
        self.assertIsNone(cameraswarm["observations"][0]["observed_on"])

        thehatman = clusters["unknown-cluster--thehatman"]
        self.assertEqual((thehatman["first_seen"], thehatman["last_seen"]), ("unknown", "unknown"))
        self.assertIsNone(thehatman["observations"][0]["observed_on"])
        self.assertTrue(
            all(
                item["claim_status"] == "self-claimed-unverified"
                for item in thehatman["observations"][0]["techniques"]
            )
        )

        heartless = clusters["unknown-cluster--heartlesssoul"]
        self.assertEqual((heartless["first_seen"], heartless["last_seen"]), ("2025-09", "unknown"))
        self.assertTrue(all(item["observed_on"] is None for item in heartless["observations"]))

        cav3rn = clusters["unknown-cluster--project-cav3rn"]
        module = cav3rn["observations"][0]
        self.assertIsNone(module["observed_on"])
        self.assertEqual(module["module_timestamp"], "2026-05-19")
        self.assertEqual(module["tools"], [])
        self.assertEqual(module["services"][0]["name"], "Microsoft Graph / Outlook calendar")

    def test_goffee_publication_dates_do_not_become_tool_observations(self) -> None:
        profile = load_json("profiles/goffee/actor-profile.json")
        tools = {item["id"]: item for item in profile["capabilities"]["tools"]}
        activities = {item["activity_id"]: item for item in profile["activities"]}
        ttps = {item["ttp_id"]: item for item in profile["ttps"]}

        chisel = tools["tool--goffee-chisel"]
        self.assertEqual(chisel["last_observed"]["status"], "unknown")
        self.assertIsNone(chisel["last_observed"]["value"])
        self.assertIn("2024-12-25は資料公開日", chisel["analyst_notes"])
        self.assertEqual(profile["actor"]["last_seen"]["value"], "2026-06-01T00:00:00Z")
        self.assertIn("2026-06", profile["actor"]["analyst_notes"])

        q2 = activities["activity--goffee-q2-container-campaign-2026"]
        expected_tools = {
            "tool--goffee-mythic",
            "tool--goffee-powershell",
            "tool--goffee-certutil",
            "tool--goffee-mshta",
            "tool--goffee-installutil",
            "tool--goffee-pgadmin",
        }
        self.assertEqual(set(q2["tool_refs"]), expected_tools)
        self.assertTrue(q2["ttp_refs"])
        for ref in q2["tool_refs"]:
            self.assertIn("source--kaspersky-goffee-q2-containers-2026", tools[ref]["evidence_refs"])
        for ref in q2["ttp_refs"]:
            self.assertEqual(
                ttps[ref]["evidence_refs"],
                ["source--kaspersky-goffee-q2-containers-2026"],
            )

    def test_storm_2603_tools_and_ttps_stay_with_their_activities(self) -> None:
        profile = load_json("profiles/storm-2603/actor-profile.json")
        iocs = load_json("profiles/storm-2603/iocs.json")
        with (ROOT / "profiles/storm-2603/artifacts.csv").open(
            encoding="utf-8", newline=""
        ) as stream:
            artifacts = list(csv.DictReader(stream))
        activities = {item["activity_id"]: item for item in profile["activities"]}
        ttps = {item["ttp_id"]: item for item in profile["ttps"]}
        malware = {item["id"]: item for item in profile["capabilities"]["malware"]}

        self.assertNotIn("activity--daily-b80b607914fb7f62f988", activities)
        toolshell = activities[
            "activity--storm-2603--toolshell-warlock-2025"
        ]
        self.assertEqual(
            set(toolshell["tool_refs"]),
            {
                "tool--storm-2603-mimikatz",
                "tool--storm-2603-psexec",
                "tool--storm-2603-impacket",
            },
        )
        self.assertEqual(
            set(toolshell["infrastructure_refs"]),
            {
                "infrastructure--storm-2603-post-exploitation-c2",
                "infrastructure--storm-2603-updatemicfosoft-c2",
            },
        )
        self.assertIn("malware--storm-2603-lockbit-ransomware", malware)
        self.assertEqual(
            malware["malware--storm-2603-lockbit-ransomware"]["first_observed"][
                "status"
            ],
            "unknown",
        )
        self.assertNotIn(
            "malware--storm-2603-lockbit-ransomware", toolshell["malware_refs"]
        )
        parallel = activities["activity--storm-2603--parallel-intrusion-2026"]
        self.assertEqual(
            set(parallel["tool_refs"]),
            {
                "tool--storm-2603-velociraptor",
                "tool--storm-2603-cloudflare-tunnel",
                "tool--zoho-assist-unattended-agent",
                "tool--storm-2603-vscode-remote-ssh",
            },
        )
        self.assertEqual(parallel["infrastructure_refs"], [])
        for ref in toolshell["ttp_refs"]:
            self.assertEqual(ttps[ref]["activity_refs"], [toolshell["activity_id"]])
        for ref in parallel["ttp_refs"]:
            self.assertEqual(ttps[ref]["activity_refs"], [parallel["activity_id"]])

        ttp_text = " ".join(item["observed_behavior"] for item in profile["ttps"])
        for unsupported in ("NNSA", "欧州", "中東"):
            self.assertNotIn(unsupported, ttp_text)
        self.assertEqual(profile["targets"]["countries"], [])
        self.assertNotIn("標的国=中国", profile["free_text"]["targeting_details"])
        self.assertNotIn("標的国=米国", profile["free_text"]["targeting_details"])

        expected_web_shells = {
            "24480dbe306597da1ba393b6e30d542673066f98826cc07ac4b9033137f37dbf",
            "b5a78616f709859a0d9f830d28ff2f9dbbb2387df1753739407917e96dadf6b0",
            "c27b725ff66fdfb11dd6487a3815d1d1eba89d61b0e919e4d06ed3ac6a74fe94",
            "1eb914c09c873f0a7bcf81475ab0f6bdfaccc6b63bf7e5f2dbf19295106af192",
        }
        expected_iis_backdoors = {
            "4c1750a14915bf2c0b093c2cb59063912dfa039a2adfe6d26d6914804e2ae928",
            "83705c75731e1d590b08f9357bc3b0f04741e92a033618736387512b40dab060",
            "f54ae00a9bae73da001c4d3d690d26ddf5e8e006b5562f936df472ec5e299441",
            "b180ab0a5845ed619939154f67526d2b04d28713fcc1904fbd666275538f431d",
            "6753b840cec65dfba0d7d326ec768bff2495784c60db6a139f51c5e83349ac4d",
            "7ae971e40528d364fa52f3bb5e0660ac25ef63e082e3bbd54f153e27b31eae68",
            "567cb8e8c8bd0d909870c656b292b57bcb24eb55a8582b884e0a228e298e7443",
            "445a37279d3a229ed18513e85f0c8d861c6f560e0f914a5869df14a74b679b86",
            "ffbc9dfc284b147e07a430fe9471e66c716a84a1f18976474a54bee82605fa9a",
            "6b273c2179518dacb1218201fd37ee2492a5e1713be907e69bf7ea56ceca53a5",
            "c2c1fec7856e8d49f5d49267e69993837575dbbec99cd702c5be134a85b2c139",
            "6f6db63ece791c6dc1054f1e1231b5bbcf6c051a49bad0784569271753e24619",
        }
        indicators = {item["normalized_value"]: item for item in iocs["indicators"]}
        self.assertEqual(len(indicators), 19)
        self.assertEqual(
            {
                value
                for value, item in indicators.items()
                if "web-shell" in item["roles"]
            },
            expected_web_shells,
        )
        self.assertEqual(
            {
                value
                for value, item in indicators.items()
                if "iis-backdoor" in item["roles"]
            },
            expected_iis_backdoors,
        )
        self.assertEqual(
            set(indicators) - expected_web_shells - expected_iis_backdoors,
            {
                "update.updatemicfosoft.com",
                "msupdate.updatemicfosoft.com",
                "65.38.121.198",
            },
        )
        self.assertTrue(
            all(
                item["first_observed"]["status"] == "unknown"
                and item["last_observed"]["status"] == "unknown"
                and item["campaign_refs"]
                == ["activity--storm-2603--toolshell-warlock-2025"]
                and item["observations"][0]["source_id"]
                == "source--microsoft-toolshell-2025"
                for item in indicators.values()
            )
        )
        excluded = {
            "92bb4ddb98eeaf11fc15bb32e71d0a63256a0ed826a03ba293ce3a8bf057a514",
            "d6da885c90a5d1fb88d0a3f0b5d9817a82d5772d5510a0773c80ca581ce2486d",
            "62881359e75c9e8899c4bc9f452ef9743e68ce467f8b3e4398bebacde9550dea",
            "131.226.2.6",
            "134.199.202.205",
            "104.238.159.149",
            "188.130.206.168",
        }
        self.assertTrue(excluded.isdisjoint(indicators))
        self.assertEqual(
            [(item["artifact_type"], item["normalized_value"]) for item in artifacts],
            [("file-name", "IIS_Server_dll.dll")],
        )

        pivots = {item["value"]: item for item in profile["hunting_pivots"]}
        for value in (
            "update.updatemicfosoft.com",
            "msupdate.updatemicfosoft.com",
            "65.38.121.198",
        ):
            self.assertEqual(
                pivots[value]["indicator_refs"],
                [indicators[value]["indicator_id"]],
            )
            self.assertEqual(pivots[value]["continuity"]["active_status"], "unknown")
            self.assertFalse(
                pivots[value]["continuity"]["passive_scan_performed"]
            )
        self.assertFalse(
            any("完全なIOC一覧がない" in item for item in profile["assessment"]["gaps"])
        )

    def test_teampcp_oligo_lineage_is_a_medium_confidence_grouping(self) -> None:
        profile = load_json("profiles/teampcp/actor-profile.json")
        serialized = json.dumps(profile, ensure_ascii=False)
        activity = next(
            item
            for item in profile["activities"]
            if item["activity_id"] == "activity--teampcp-oligo-lineage-2020-2026"
        )
        self.assertEqual(activity["stix_object_type"], "grouping")
        self.assertEqual(activity["grouping_context"], "suspicious-activity")
        self.assertEqual(activity["confidence"], "medium")
        self.assertEqual(activity["reported_at"]["value"], "2026-08-05T00:00:00Z")
        self.assertEqual(activity["evidence_refs"], ["source--oligo-teampcp-2026"])
        self.assertEqual(activity["victim_refs"], ["victim--teampcp-exposed-cloud-services"])
        victim = next(
            item
            for item in profile["victim_cases"]
            if item["victim_case_id"] == "victim--teampcp-exposed-cloud-services"
        )
        self.assertEqual(victim["confidence"], "medium")
        self.assertEqual(victim["evidence_refs"], ["source--oligo-teampcp-2026"])
        self.assertNotIn("source--daily-", serialized)
        self.assertNotIn("activity--daily-", serialized)
        self.assertEqual(profile["targets"]["regions"], [])
        self.assertNotIn("全世界", serialized)
        self.assertEqual([item["type"] for item in profile["motivations"]], ["financial-gain"])
        unc6780 = next(item for item in profile["actor"]["aliases"] if item["name"] == "UNC6780")
        self.assertIn("source--gtig-ai-threat-tracker-2026-05", unc6780["evidence_refs"])

    def test_silent_librarian_curated_claims_use_stable_ids_and_medium_boundary(self) -> None:
        profile = load_json("profiles/silent-librarian/actor-profile.json")
        serialized = json.dumps(profile, ensure_ascii=False)
        self.assertNotIn("source--daily-", serialized)
        self.assertNotIn("activity--daily-", serialized)

        activity = next(
            item
            for item in profile["activities"]
            if item["activity_id"] == "activity--silent-librarian-mabna-campaign-2013-2017"
        )
        self.assertEqual(activity["confidence"], "medium")
        self.assertEqual(activity["reported_at"]["value"], "2018-03-23T00:00:00Z")
        self.assertIn("source--mitre-attack-19-2", activity["evidence_refs"])
        self.assertEqual(profile["attribution"]["confidence"], "medium")
        self.assertIn("source--mitre-attack-19-2", profile["attribution"]["evidence_refs"])

        victim = profile["victim_cases"][0]
        self.assertEqual(victim["case_status"], "alleged")
        self.assertEqual(victim["confidence"], "medium")
        self.assertTrue(
            all(
                item["confidence"] != "high"
                for category in ("countries", "regions", "sectors", "roles")
                for item in profile["targets"][category]
            )
        )

        mabna_person_relationships = [
            item
            for item in profile["entity_relationships"]
            if item["source_ref"].startswith("threat-actor-individual--")
            and item["target_ref"] == "organization--mabna-institute"
        ]
        self.assertEqual(len(mabna_person_relationships), 17)
        self.assertEqual(
            {
                relationship_type: sum(
                    item["relationship_type"] == relationship_type
                    for item in mabna_person_relationships
                )
                for relationship_type in {
                    item["relationship_type"] for item in mabna_person_relationships
                }
            },
            {
                "founder-of": 2,
                "alleged-contractor-for": 12,
                "alleged-affiliate-of": 2,
                "alleged-associated-with": 1,
            },
        )
        people = {
            item["entity_id"]: item
            for item in profile["associated_entities"]
            if item["entity_id"].startswith("threat-actor-individual--")
        }
        self.assertTrue(
            all("alleged-mabna-member" not in item["roles"] for item in people.values())
        )
        self.assertEqual(people["threat-actor-individual--ehsan-mohammadi"]["roles"], ["founder", "managing-director"])
        self.assertEqual(people["threat-actor-individual--mojtaba-galekuhi"]["roles"], ["alleged-co-conspirator"])
        filing = next(
            item
            for item in profile["sources"]
            if item["source_id"] == "source--doj-mabna-s2-indictment-2026"
        )
        self.assertEqual(
            filing["sha256"],
            "117d2d0d4458997d1d941289fe6e7b9f1fd86a92d361e19ed25d9269b3a2f86a",
        )
        self.assertIn("paragraphs 12–28", filing["analyst_notes"])
        self.assertNotIn("alleged-member-of", serialized)

    def test_generated_stix_preserves_grouping_and_stable_activity_ids(self) -> None:
        team_stix = load_json("profiles/teampcp/generated/profile.stix2.json")
        lineage = next(
            item
            for item in team_stix["objects"]
            if item.get("x_profile_object_id")
            == "activity--teampcp-oligo-lineage-2020-2026"
        )
        self.assertEqual(lineage["type"], "grouping")
        self.assertEqual(lineage["context"], "suspicious-activity")

        silent_stix = load_json("profiles/silent-librarian/generated/profile.stix2.json")
        campaign = next(
            item
            for item in silent_stix["objects"]
            if item.get("x_profile_object_id")
            == "activity--silent-librarian-mabna-campaign-2013-2017"
        )
        self.assertEqual(campaign["type"], "campaign")
        serialized = json.dumps(silent_stix, ensure_ascii=False)
        self.assertNotIn("source--daily-ac0aab951821b27df384", serialized)
        self.assertNotIn("activity--daily-4d15dec07641eea42e80", serialized)
        person_associations = [
            item
            for item in silent_stix["objects"]
            if item.get("type") == "relationship"
            and item.get("x_profile_relationship_type")
            in {
                "founder-of",
                "alleged-contractor-for",
                "alleged-affiliate-of",
                "alleged-associated-with",
            }
            and item.get("source_ref", "").startswith("threat-actor--")
        ]
        self.assertEqual(len(person_associations), 17)
        self.assertEqual(
            {
                relationship_type: sum(
                    item["x_profile_relationship_type"] == relationship_type
                    for item in person_associations
                )
                for relationship_type in {
                    item["x_profile_relationship_type"]
                    for item in person_associations
                }
            },
            {
                "founder-of": 2,
                "alleged-contractor-for": 12,
                "alleged-affiliate-of": 2,
                "alleged-associated-with": 1,
            },
        )
        self.assertTrue(
            all(item["relationship_type"] == "related-to" for item in person_associations)
        )
        self.assertNotIn("alleged-member-of", serialized)

        storm_stix = load_json("profiles/storm-2603/generated/profile.stix2.json")
        tool_names = {
            item["name"]
            for item in storm_stix["objects"]
            if item.get("type") == "tool"
        }
        self.assertTrue(
            {
                "Mimikatz",
                "PsExec",
                "Impacket",
                "Velociraptor",
                "Cloudflare Tunnel",
                "Visual Studio Code Remote - SSH",
                "Zoho Assist Unattended Agent",
            }.issubset(tool_names)
        )


if __name__ == "__main__":
    unittest.main()
