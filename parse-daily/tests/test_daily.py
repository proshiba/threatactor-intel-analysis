from __future__ import annotations

import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

import daily_check  # noqa: E402
from daily_check import latest_activity  # noqa: E402

UNKNOWN_POINT = {"value": None, "precision": "unknown", "status": "unknown", "basis": "not-stated"}


def known_point(value: str) -> dict:
    return {"value": value, "precision": "day", "status": "known", "basis": "source-reporting"}

from daily_common import (  # noqa: E402
    ActorMatch,
    ActorRegistry,
    assess_activity_claim,
    date_from_path,
    is_safe_structured_match,
    parse_news_file,
    read_ioc_csv,
    write_json_if_changed,
)
from daily_materializer import (  # noqa: E402
    activity_bounds,
    activity_entry,
    activity_id_for,
    build_ledger,
    ensure_malware_capabilities,
    source_id_for_value,
    source_items,
)


CONFIG = json.loads((HERE / "config.json").read_text(encoding="utf-8"))


def profile(name: str, aliases: list[dict[str, str]]) -> dict:
    return {
        "actor": {
            "canonical_name": name,
            "aliases": [
                {
                    "name": item["name"],
                    "scope": item["scope"],
                    "confidence": "medium",
                }
                for item in aliases
            ],
        },
        "capabilities": {"malware": []},
    }


class DailyCommonTests(unittest.TestCase):
    def test_date_from_path(self) -> None:
        self.assertEqual(date_from_path(Path("20260725.md")), "2026-07-25")
        self.assertIsNone(date_from_path(Path("notes.md")))

    def test_parse_modern_and_legacy_news(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            modern = Path(directory) / "20260725.md"
            modern.write_text(
                "#### Kimsukyの活動\n"
                "https://example.com/article\n\n"
                "- 要約\n"
                "  - 新しい活動を確認した。\n"
                "- その他\n"
                "  - 一次ソース: https://vendor.example/report\n",
                encoding="utf-8",
            )
            parsed = parse_news_file(modern, "daily-news/news/20260725.md")
            self.assertEqual(len(parsed), 1)
            self.assertEqual(parsed[0]["news_date"], "2026-07-25")
            self.assertEqual(parsed[0]["primary_url"], "https://vendor.example/report")

            legacy = Path(directory) / "20230611.md"
            legacy.write_text(
                "1. https://example.com/old\n"
                '- タイトル: "旧形式の記事"\n'
                "- 要約\n"
                "  - 説明。\n",
                encoding="utf-8",
            )
            parsed = parse_news_file(legacy, "daily-news/news/20230611.md")
            self.assertEqual(parsed[0]["title"], "旧形式の記事")

    def test_canonical_name_wins_over_non_exact_alias(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "kimsuky").mkdir()
            (root / "apt43").mkdir()
            (root / "kimsuky" / "actor-profile.json").write_text(
                json.dumps(profile("Kimsuky", [])), encoding="utf-8"
            )
            (root / "apt43" / "actor-profile.json").write_text(
                json.dumps(
                    profile("APT43", [{"name": "Kimsuky", "scope": "overlapping"}])
                ),
                encoding="utf-8",
            )
            registry = ActorRegistry(root, CONFIG)
            matches = registry.exact("Kimsuky", "ioc-actor-field")
            self.assertEqual([item.slug for item in matches], ["kimsuky"])
            self.assertTrue(is_safe_structured_match("Kimsuky", matches[0]))
            self.assertFalse(
                is_safe_structured_match("Kimsuky (low confidence)", matches[0])
            )

    def test_read_structured_ioc_csv(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "20260725.csv"
            with path.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.DictWriter(
                    stream,
                    fieldnames=[
                        "ioc_type", "ioc_value", "date", "category", "actor",
                        "actor_attribute", "malware", "malware_type", "reference",
                        "description", "author", "confidence",
                    ],
                )
                writer.writeheader()
                writer.writerow(
                    {
                        "ioc_type": "file_hash_sha256",
                        "ioc_value": "a" * 64,
                        "date": "2026-07-24",
                        "category": "malware",
                        "actor": "Kimsuky",
                        "actor_attribute": "north-korea",
                        "malware": "Example",
                        "malware_type": "backdoor",
                        "reference": "https://example.com/report",
                        "description": "AI generated. sample",
                        "author": "AI agent",
                        "confidence": "medium",
                    }
                )
            rows = read_ioc_csv(path, CONFIG)
            self.assertEqual(rows[0]["type"], "sha256")
            self.assertEqual(rows[0]["roles"], ["payload"])
            self.assertEqual(rows[0]["row"], 2)

    def test_json_writer_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "value.json"
            self.assertTrue(write_json_if_changed(path, {"value": "同一"}))
            before = path.stat().st_mtime_ns
            self.assertFalse(write_json_if_changed(path, {"value": "同一"}))
            self.assertEqual(path.stat().st_mtime_ns, before)

    def test_activity_and_sources_have_separate_stable_ids(self) -> None:
        record = {
            "record_id": "legacy-id-does-not-control-activity",
            "actor": {"slug": "apt37"},
            "activity": {
                "activity_reference": "https://vendor.example/report",
                "primary_url": "https://vendor.example/report",
                "news_path": "daily-news/news/20260101.md",
            },
            "sources": [
                {
                    "url": "https://vendor.example/report",
                    "source_path": "daily-news/news/20260101.md",
                    "source_type": "primary-report",
                },
                {
                    "url": "https://vendor.example/iocs.sha256",
                    "source_path": "daily-news/iocs/20260101.csv",
                    "source_type": "ioc-reference",
                },
            ],
        }
        queue = {
            "source": {
                "repository": "owner/repo",
                "commit": "abc",
            }
        }
        self.assertEqual(len(source_items(record, queue)), 2)
        self.assertNotEqual(
            activity_id_for(record),
            source_id_for_value("https://vendor.example/report"),
        )
        changed_record_id = {**record, "record_id": "changed"}
        self.assertEqual(activity_id_for(record), activity_id_for(changed_record_id))

    def test_activity_dates_are_not_inferred_from_ioc_collection_date(self) -> None:
        record = {
            "iocs": [{"observed_date": "2026-07-25"}],
        }
        first, last = activity_bounds(record)
        self.assertEqual(first["status"], "unknown")
        self.assertEqual(last["status"], "unknown")

    def test_explicit_activity_claim_is_separate_from_name_discovery(self) -> None:
        match = ActorMatch(
            "kimsuky",
            "Kimsuky",
            "Kimsuky",
            "exact",
            "high",
            "news-body",
        )
        claim = assess_activity_claim(
            match,
            "北朝鮮のハッカーが開発者を標的に攻撃",
            "- Kimsukyグループがマルウェアを配布して攻撃を実施。",
            CONFIG,
        )
        self.assertEqual(claim["assessment"], "strong-subject")
        self.assertEqual(claim["actor_role"], "operator")

        adopted = assess_activity_claim(
            ActorMatch(
                "muddywater",
                "MuddyWater",
                "MuddyWater",
                "exact",
                "high",
                "news-title",
            ),
            "MuddyWater、新しいC2ツールを採用",
            "",
            CONFIG,
        )
        self.assertEqual(adopted["assessment"], "strong-subject")

        attributed = assess_activity_claim(
            match,
            "新たなマルウェアキャンペーンを確認",
            "- このキャンペーンはKimsukyと関連があると報告された。",
            CONFIG,
        )
        self.assertEqual(attributed["assessment"], "attributed-subject")
        self.assertEqual(attributed["actor_role"], "attributed-operator")

        uncertain = assess_activity_claim(
            match,
            "新たなマルウェアキャンペーンを確認",
            "- このキャンペーンはKimsukyと類似するが、確固たる証拠はない。",
            CONFIG,
        )
        self.assertEqual(uncertain["assessment"], "attribution-uncertain")

        legal = assess_activity_claim(
            ActorMatch(
                "revil", "REvil", "REvil", "exact", "high", "news-title"
            ),
            "REvilメンバーをランサムウェア攻撃の罪で逮捕",
            "",
            CONFIG,
        )
        self.assertEqual(legal["assessment"], "non-operational")

        collision = assess_activity_claim(
            ActorMatch(
                "sea-turtle",
                "Sea Turtle",
                "SILICON",
                "overlapping",
                "high",
                "news-title",
            ),
            "Apple Silicon CPUに対する攻撃",
            "",
            CONFIG,
        )
        self.assertEqual(collision["assessment"], "name-collision")

    def test_activity_keeps_unknown_period_and_separate_report_date(self) -> None:
        record = {
            "record_id": "daily-record--example",
            "actor": {"slug": "kimsuky"},
            "activity": {
                "title": "KimsukyがExampleRATを配布",
                "summary": "KimsukyがExampleRATを用いた攻撃を実施。",
                "news_date": "2026-07-25",
                "activity_reference": "https://example.test/report",
                "primary_url": "https://example.test/report",
                "news_path": "daily-news/news/20260725.md",
            },
            "confidence": "high",
            "iocs": [],
            "activity_claim": {"assessment": "strong-subject"},
        }
        profile_data = {
            "capabilities": {
                "malware": [
                    {
                        "id": "malware--example-rat",
                        "name": "ExampleRAT",
                        "aliases": [],
                    }
                ],
                "infrastructure": [],
            },
            "targets": {
                "countries": [],
                "regions": [],
                "sectors": [],
                "roles": [],
            },
        }
        activity = activity_entry(
            record,
            ["source--daily-example"],
            profile_data,
        )
        self.assertEqual(activity["first_observed"]["status"], "unknown")
        self.assertEqual(activity["last_observed"]["status"], "unknown")
        self.assertEqual(
            activity["reported_at"]["value"],
            "2026-07-25T00:00:00Z",
        )
        self.assertEqual(activity["malware_refs"], ["malware--example-rat"])

    def test_only_approved_capability_is_materialized(self) -> None:
        profile_data = {
            "actor": {"canonical_name": "Example Actor"},
            "capabilities": {"malware": []},
        }
        record = {
            "record_id": "daily-record--example",
            "confidence": "medium",
            "iocs": [
                {
                    "malware": "ConfirmedFamily; FalseFlag; sample.exe",
                    "malware_type": "backdoor",
                }
            ],
            "capability_decisions": [
                {
                    "name": "ConfirmedFamily",
                    "status": "approved",
                    "reason": "一次資料で確認",
                },
                {
                    "name": "FalseFlag",
                    "status": "rejected",
                    "reason": "偽旗",
                },
            ],
        }
        ensure_malware_capabilities(
            profile_data, record, ["source--daily-example"]
        )
        self.assertEqual(
            [item["name"] for item in profile_data["capabilities"]["malware"]],
            ["ConfirmedFamily"],
        )
        self.assertEqual(len(record["iocs"][0]["malware_refs"]), 1)

    def test_incremental_ledger_preserves_prior_records(self) -> None:
        existing = {
            "records": [
                {
                    "record_id": "daily-record--old",
                    "source_commit": "old-commit",
                }
            ]
        }
        current = [{"record_id": "daily-record--new"}]
        ledger = build_ledger(
            existing,
            "actor--example",
            current,
            "new-commit",
            "2026-07-26T00:00:00Z",
            rebuild=False,
        )
        self.assertEqual(
            [item["record_id"] for item in ledger["records"]],
            ["daily-record--new", "daily-record--old"],
        )
        rebuilt = build_ledger(
            existing,
            "actor--example",
            current,
            "new-commit",
            "2026-07-26T00:00:00Z",
            rebuild=True,
        )
        self.assertEqual(
            [item["record_id"] for item in rebuilt["records"]],
            ["daily-record--new"],
        )


class DailyCheckTests(unittest.TestCase):
    """日次チェックの抽出ロジック（daily_check.py）。"""

    def test_report_date_is_used_when_period_is_unknown(self) -> None:
        """攻撃期間不明でも reported_at があれば直近活動として拾う。"""
        profile = {
            "activities": [
                {
                    "first_observed": UNKNOWN_POINT,
                    "last_observed": UNKNOWN_POINT,
                    "reported_at": known_point("2026-07-20T00:00:00Z"),
                }
            ],
            "actor": {"last_seen": UNKNOWN_POINT},
        }
        point, basis = latest_activity(profile)
        self.assertIsNotNone(point)
        self.assertEqual(point.date().isoformat(), "2026-07-20")
        self.assertEqual(basis, "activity.reported_at")

    def test_newest_signal_wins_across_fields(self) -> None:
        profile = {
            "activities": [
                {
                    "first_observed": known_point("2024-01-01T00:00:00Z"),
                    "last_observed": known_point("2024-03-01T00:00:00Z"),
                    "reported_at": known_point("2024-04-01T00:00:00Z"),
                }
            ],
            "actor": {"last_seen": known_point("2026-05-05T00:00:00Z")},
        }
        point, basis = latest_activity(profile)
        self.assertEqual(point.date().isoformat(), "2026-05-05")
        self.assertEqual(basis, "actor.last_seen")

    def test_unknown_dates_are_not_treated_as_activity(self) -> None:
        profile = {
            "activities": [{"first_observed": UNKNOWN_POINT, "last_observed": UNKNOWN_POINT}],
            "actor": {"last_seen": UNKNOWN_POINT},
        }
        self.assertEqual(latest_activity(profile), (None, ""))

    def test_mentioned_actors_put_recently_active_first(self) -> None:
        """直近活動のあるアクターが最優先で並ぶこと。"""
        queue = {
            "records": [
                {
                    "review_status": "pending",
                    "actor": {"slug": "quiet-actor", "canonical_name": "Quiet", "matched_term": "Quiet"},
                    "activity": {"title": "記事A", "news_date": "2026-07-27"},
                    "activity_claim": {"assessment": "strong-subject"},
                },
                {
                    "review_status": "pending",
                    "actor": {"slug": "active-actor", "canonical_name": "Active", "matched_term": "Active"},
                    "activity": {"title": "記事B", "news_date": "2026-07-27"},
                    "activity_claim": {"assessment": "candidate"},
                },
            ]
        }
        with tempfile.TemporaryDirectory() as tmp:
            queue_path = Path(tmp) / "review-queue.json"
            queue_path.write_text(json.dumps(queue), encoding="utf-8")
            recent = [{"slug": "active-actor", "last_activity": "2026-07-01"}]
            with mock.patch.object(daily_check, "QUEUE_PATH", queue_path), \
                 mock.patch.object(daily_check, "STATE_PATH", Path(tmp) / "missing.json"), \
                 mock.patch.object(daily_check, "collect_recent_actors", return_value=recent):
                report = daily_check.build_report(365, "2026-07-27")
        names = [entry["slug"] for entry in report["mentioned_actors"]]
        self.assertEqual(names[0], "active-actor")
        self.assertTrue(report["mentioned_actors"][0]["in_recent_set"])
        self.assertEqual(report["statistics"]["mentioned_recent_actors"], 1)


if __name__ == "__main__":
    unittest.main()
