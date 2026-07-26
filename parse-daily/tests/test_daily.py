from __future__ import annotations

import csv
import json
import sys
import tempfile
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

from daily_common import (  # noqa: E402
    ActorRegistry,
    date_from_path,
    is_safe_structured_match,
    parse_news_file,
    read_ioc_csv,
    write_json_if_changed,
)
from daily_materializer import (  # noqa: E402
    activity_bounds,
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


if __name__ == "__main__":
    unittest.main()
