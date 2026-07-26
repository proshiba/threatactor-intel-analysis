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


if __name__ == "__main__":
    unittest.main()
