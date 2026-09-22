#!/usr/bin/env python3
"""Regression checks for the reviewed Darkhotel KCTV-lure campaign."""

from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PROFILE_DIR = ROOT / "profiles" / "darkhotel"
ACTIVITY_ID = "activity--darkhotel-kctv-lure-2026"
LEGACY_ACTIVITY_ID = "activity--daily-fbc4f59c4a844e18e5ab"
LEGACY_SOURCE_ID = "source--daily-a945409955df891618a3"
SOURCE_ID = "source--360-apt-c-06-darkhotel-kctv-lure-2026"


class DarkhotelKctvCampaignTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.profile = json.loads(
            (PROFILE_DIR / "actor-profile.json").read_text(encoding="utf-8")
        )
        cls.iocs = json.loads(
            (PROFILE_DIR / "iocs.json").read_text(encoding="utf-8")
        )
        with (PROFILE_DIR / "artifacts.csv").open(
            encoding="utf-8", newline=""
        ) as stream:
            cls.artifacts = list(csv.DictReader(stream))

    def test_apt_c_06_is_a_primary_source_scoped_overlap(self) -> None:
        alias = next(
            item
            for item in self.profile["actor"]["aliases"]
            if item["name"] == "APT-C-06"
        )
        self.assertEqual(alias["scope"], "overlapping")
        self.assertEqual(alias["confidence"], "high")
        self.assertEqual(alias["evidence_refs"], [SOURCE_ID])

        source = next(
            item for item in self.profile["sources"] if item["source_id"] == SOURCE_ID
        )
        self.assertEqual(
            source["url"],
            "https://mp.weixin.qq.com/s/KrQyZ2AZn9dcL3Fqyg_y3Q",
        )
        self.assertEqual(source["archive_url"], "https://cn-sec.com/archives/5398327.html")
        self.assertIn("直接再取得できなかった", source["analyst_notes"])
        self.assertIn("原文始发", source["analyst_notes"])
        self.assertEqual(source["published_at"]["value"], "2026-08-12T00:00:00Z")
        self.assertEqual(source["published_at"]["basis"], "source-publication")
        self.assertIsNone(source["accessed_at"])

        same_url_sources = [
            item
            for item in self.profile["sources"]
            if item.get("url") == source["url"] or item.get("path") == source["url"]
        ]
        self.assertEqual([item["source_id"] for item in same_url_sources], [SOURCE_ID])

    def test_campaign_period_is_source_stated_and_false_targets_are_absent(self) -> None:
        activity = next(
            item
            for item in self.profile["activities"]
            if item["activity_id"] == ACTIVITY_ID
        )
        self.assertEqual(activity["first_observed"]["value"], "2026-04-01T00:00:00Z")
        self.assertEqual(activity["first_observed"]["precision"], "month")
        self.assertEqual(activity["last_observed"]["value"], "2026-05-01T00:00:00Z")
        self.assertEqual(activity["last_observed"]["precision"], "month")
        self.assertEqual(activity["reported_at"]["value"], "2026-08-12T00:00:00Z")
        self.assertEqual(activity["reported_at"]["basis"], "source-publication")
        self.assertIn(SOURCE_ID, activity["evidence_refs"])
        self.assertNotIn(LEGACY_SOURCE_ID, activity["evidence_refs"])

        canonical = json.dumps(
            {
                "profile": self.profile,
                "iocs": self.iocs,
                "artifacts": self.artifacts,
                "manifest": json.loads(
                    (PROFILE_DIR / "ioc-sources.json").read_text(encoding="utf-8")
                ),
            },
            ensure_ascii=False,
        )
        self.assertNotIn(LEGACY_ACTIVITY_ID, canonical)
        self.assertNotIn(LEGACY_SOURCE_ID, canonical)

        targets = {
            item["id"]: item["name"]
            for category in ("countries", "regions", "sectors", "roles")
            for item in self.profile["targets"][category]
        }
        linked_names = {targets[ref] for ref in activity["target_refs"]}
        self.assertNotIn("北朝鮮", linked_names)
        self.assertNotIn("タイ", linked_names)
        self.assertNotIn("小売・ホスピタリティ", linked_names)

    def test_primary_iocs_are_campaign_linked_without_invented_dates_or_roles(self) -> None:
        expected = {
            "built.3jkg8d.com",
            "4a88efd00ba8b036ec4642fcecbe6df3",
            "60fd3dbfeb1a44ed2a8ad46113d58262",
            "d033868f7b4374936dc462b0b016abaf",
            "be6d6d01740d210cb16973d81a1fd782",
        }
        indicators = {
            item["normalized_value"]: item
            for item in self.iocs["indicators"]
            if item["normalized_value"] in expected
        }
        self.assertEqual(set(indicators), expected)
        for indicator in indicators.values():
            self.assertEqual(indicator["campaign_refs"], [ACTIVITY_ID])
            self.assertEqual(indicator["roles"], [])
            self.assertEqual(indicator["first_observed"]["status"], "unknown")
            self.assertEqual(indicator["last_observed"]["status"], "unknown")
            self.assertEqual(indicator["observations"][0]["source_id"], SOURCE_ID)

    def test_primary_artifacts_are_generated_from_structured_input(self) -> None:
        rows = [row for row in self.artifacts if row["source_id"] == SOURCE_ID]
        self.assertEqual(len(rows), 15)
        values = {row["value"] for row in rows}
        self.assertTrue(
            {
                "\\Microsoft\\Windows\\AppID\\PolicyManager",
                "\\ScriptingSchedule",
                "del kctv.msi;schtasks /delete /tn ScriptingSchedule /F",
                "kctv.msi",
                "tp.ps1",
                "iii",
                "iii/t.m",
                "VdPlayer.exe",
                "C:\\Programdata\\vdplayer",
                "C:\\ProgramData\\0_a^r(9)+!+$&)#",
                "조선중앙텔레비죤 실시간방영프로그람 해설서.docx",
                "jh421a",
                "gs9j",
                "jqe",
                "6MVD",
            }
            <= values
        )
        for row in rows:
            self.assertEqual(row["observed_at"], "")
            self.assertEqual(row["observed_at_status"], "unknown")
            self.assertEqual(json.loads(row["campaign_refs"]), [ACTIVITY_ID])
        vdplayer = next(row for row in rows if row["value"] == "VdPlayer.exe")
        self.assertIn("正規", vdplayer["context_excerpt"])


if __name__ == "__main__":
    unittest.main()
