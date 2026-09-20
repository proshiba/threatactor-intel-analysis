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
import validate_daily  # noqa: E402
from build_review_queue import apply_decision  # noqa: E402
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
    name_candidates,
    parse_news_file,
    read_ioc_csv,
    write_json_if_changed,
)
from daily_materializer import (  # noqa: E402
    activity_bounds,
    profile_source,
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

    def registry_with(self, *names: str) -> ActorRegistry:
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        root = Path(directory.name)
        for name in names:
            slug = name.lower().replace(" ", "-")
            (root / slug).mkdir()
            (root / slug / "actor-profile.json").write_text(
                json.dumps(profile(name, [])), encoding="utf-8"
            )
        return ActorRegistry(root, CONFIG)
    def test_registry_ignores_deprecated_profiles(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "revil").mkdir()
            data = profile("REvil", [])
            data["status"] = "deprecated"
            (root / "revil" / "actor-profile.json").write_text(
                json.dumps(data), encoding="utf-8"
            )
            registry = ActorRegistry(root, CONFIG)
            self.assertEqual(registry.exact("REvil", "ioc-actor-field"), [])

    def test_name_candidate_is_extracted_from_body_without_iocs(self) -> None:
        """IOCを伴わない記事はIOC CSVのactor列に現れないため、本文から名前を拾う。"""
        article = {
            "title": "FulcrumSec、Manchester Airportsへの侵害と86GBのデータ窃取を主張",
            "body": (
                "- 要約\n"
                "    - データ恐喝グループFulcrumSecはManchester Airports Group（MAG）への"
                "侵害を主張し、約86GBのデータを窃取したとBleepingComputerへ説明した。\n"
                "- IOCの列挙\n"
                "    - IOC情報なし\n"
                "- その他\n"
                "    - 攻撃者は2025年から活動する金銭目的のデータ恐喝グループFulcrumSecで、"
                "暗号化より機密データ窃取と公開脅迫を重視する。\n"
            ),
        }
        found = name_candidates(article, self.registry_with("APT28"), [])
        self.assertIn("FulcrumSec", found)
        # 実行主体の位置に現れない被害組織名・ベンダー名は拾わない
        self.assertNotIn("Manchester Airports Group", found)
        self.assertNotIn("BleepingComputer", found)

    def test_name_candidate_skips_registered_actors_and_ignored_values(self) -> None:
        article = {
            "title": "",
            "body": (
                "- その他\n"
                "    - 攻撃者は恐喝グループShinyHuntersで、Microsoft Teamsを悪用した。\n"
                "    - 脅威アクターAPT28が関与したとみられる。\n"
            ),
        }
        registry = self.registry_with("APT28", "ShinyHunters")
        # 登録済みの名前は ActorRegistry.mentions() が扱うため、候補には出さない
        self.assertEqual(name_candidates(article, registry, []), [])
        # 未登録でも、設定の除外リストにある製品名は候補にしない
        found = name_candidates(article, self.registry_with("APT28"), ["Microsoft Teams"])
        self.assertEqual(found, ["ShinyHunters"])

    def test_name_candidate_is_extracted_from_bracketed_name(self) -> None:
        """初出のアクター名を鉤括弧で囲む記事を拾う（Red Heron の取りこぼし事例）。

        当該日のIOC CSVが未作成で、かつ名前が鉤括弧内にあると、IOC actor列経路と
        助詞直結の抽出規則のどちらにも掛からず検知できなかった。
        """
        article = {
            "title": "Red Heron、GiteaのN-day脆弱性を悪用した多国籍攻撃で新たなLinuxルートキットを展開",
            "body": (
                "- 要約\n"
                "    - Acronis TRUは、中国語話者の攻撃者「Red Heron」がGiteaのRCE脆弱性"
                "CVE-2026-60004を公開後数日で武器化し、インターネット公開サーバーを攻撃したと報告した。\n"
                "    - 攻撃では30以上の操作機能を持つLinuxインプラント「JITTERLY」と、"
                "ファイル・プロセス・通信を隠蔽する新規ルートキット「SIXZUT」が使用された。\n"
            ),
        }
        found = name_candidates(article, self.registry_with("APT28"), [])
        self.assertIn("Red Heron", found)
        # 指示語を伴わない鉤括弧はマルウェア名・ツール名を囲むため、実行主体として拾わない
        self.assertNotIn("JITTERLY", found)
        self.assertNotIn("SIXZUT", found)

    def test_name_candidate_rejects_cve_ids_and_short_tokens(self) -> None:
        article = {
            "title": "",
            "body": (
                "- その他\n"
                "    - 攻撃グループCVE-2026-59310を悪用したとされる。\n"
                "    - 攻撃者はABで、詳細は不明。\n"
            ),
        }
        self.assertEqual(name_candidates(article, self.registry_with("APT28"), []), [])

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

        vendor_title = assess_activity_claim(
            ActorMatch(
                "cellebrite",
                "Cellebrite",
                "Cellebrite",
                "exact",
                "high",
                "news-title",
            ),
            "セルビア警察、Cellebriteのゼロデイ攻撃を使用してAndroid携帯をアンロック",
            "",
            CONFIG,
        )
        self.assertEqual(vendor_title["assessment"], "context-only")
        self.assertEqual(vendor_title["actor_role"], "unknown")

        vendor_body = assess_activity_claim(
            ActorMatch(
                "cellebrite",
                "Cellebrite",
                "Cellebrite",
                "exact",
                "high",
                "news-body",
            ),
            "Androidゼロデイを悪用した標的型攻撃",
            "- Cellebriteが開発したゼロデイエクスプロイトチェーンの一部として、セルビア当局が押収端末のロック解除に悪用した。",
            CONFIG,
        )
        self.assertEqual(vendor_body["assessment"], "context-only")
        self.assertEqual(vendor_body["actor_role"], "unknown")

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
        self.assertIn("diamond_model", activity)
        self.assertEqual(
            activity["diamond_model"]["capability"]["malware_refs"],
            ["malware--example-rat"],
        )

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

    def test_external_sources_come_from_config_and_reach_the_report(self) -> None:
        """巡回対象の一次情報源は config.json を正とし、走査出力へ必ず転記する。

        ルーチンのプロンプトが古い版のままでも巡回対象が欠けないようにするための経路。
        securelist.ru はプロンプト側の一覧から3走査連続で欠落していた実績があるため、
        設定に載っている限り出力へ現れることを固定する。
        """
        config = {
            "external_sources": {
                "sources": [
                    {"publisher": "Kaspersky Securelist", "url": "https://securelist.com/"},
                    {
                        "publisher": "Kaspersky Securelist（ロシア語版）",
                        "url": "https://securelist.ru/",
                        "note": ".com へ出ない記事が載る。",
                    },
                ]
            }
        }
        with tempfile.TemporaryDirectory() as tmp:
            config_path = Path(tmp) / "config.json"
            config_path.write_text(json.dumps(config), encoding="utf-8")
            queue_path = Path(tmp) / "review-queue.json"
            queue_path.write_text(json.dumps({"records": []}), encoding="utf-8")
            with mock.patch.object(daily_check, "CONFIG_PATH", config_path), \
                 mock.patch.object(daily_check, "QUEUE_PATH", queue_path), \
                 mock.patch.object(daily_check, "STATE_PATH", Path(tmp) / "missing.json"), \
                 mock.patch.object(daily_check, "collect_recent_actors", return_value=[]):
                report = daily_check.build_report(365, "2026-09-17")
                markdown = daily_check.render_markdown(report, 30)

        self.assertEqual(
            [source["url"] for source in report["external_sources"]],
            ["https://securelist.com/", "https://securelist.ru/"],
        )
        self.assertIn("https://securelist.ru/", markdown)
        self.assertIn(".com へ出ない記事が載る。", markdown)

    def test_external_sources_are_empty_when_config_is_missing(self) -> None:
        """config.json が無くても走査自体は落とさない。"""
        with tempfile.TemporaryDirectory() as tmp:
            queue_path = Path(tmp) / "review-queue.json"
            queue_path.write_text(json.dumps({"records": []}), encoding="utf-8")
            with mock.patch.object(daily_check, "CONFIG_PATH", Path(tmp) / "missing.json"), \
                 mock.patch.object(daily_check, "QUEUE_PATH", queue_path), \
                 mock.patch.object(daily_check, "STATE_PATH", Path(tmp) / "missing.json"), \
                 mock.patch.object(daily_check, "collect_recent_actors", return_value=[]):
                report = daily_check.build_report(365, "2026-09-17")
                markdown = daily_check.render_markdown(report, 30)

        self.assertEqual(report["external_sources"], [])
        self.assertNotIn("確認する一次情報源", markdown)

    def test_shipped_config_lists_both_securelist_domains(self) -> None:
        """同梱の config.json に .com と .ru の双方が載っていること。"""
        sources = daily_check.collect_external_sources()
        urls = [source["url"] for source in sources]
        self.assertIn("https://securelist.com/", urls)
        self.assertIn("https://securelist.ru/", urls)


class AliasedSourceTests(unittest.TestCase):
    """activity_reference_aliases で既存活動へ集約した出典の扱い。"""

    QUEUE = {"source": {"repository": "owner/repo", "commit": "abc"}}

    def _record(self) -> dict:
        return {
            "activity": {
                "title": "集約先の見出し",
                "news_date": "2026-09-02",
                "primary_url": "https://x.example/status/1",
                "news_path": "daily-news/news/20260902.md",
            },
            "sources": [
                {
                    "url": "https://x.example/status/1",
                    "source_path": "daily-news/news/20260902.md",
                    "source_type": "primary-report",
                },
                {
                    "url": "https://vendor.example/writeup",
                    "source_path": "daily-news/news/20260912.md",
                    "source_type": "primary-report",
                    "news_date": "2026-09-12",
                    "title": "集約した記事の見出し",
                },
            ],
        }

    def test_source_items_keeps_aliased_metadata(self) -> None:
        items = source_items(self._record(), self.QUEUE)
        aliased = next(i for i in items if i["url"] == "https://vendor.example/writeup")
        self.assertEqual(aliased["news_date"], "2026-09-12")
        self.assertEqual(aliased["title"], "集約した記事の見出し")

    def test_ioc_validation_ignores_aggregated_source_without_iocs(self) -> None:
        """IOCを1件も掲載していない集約元の記事はIOC出典の欠落として扱わない。

        2026-09-20 の FamousSparrow の取込が実例である。ESETの記事URLと
        github.com/eset/malware-ioc のIOC一覧を1活動へ集約したが、IOC行は
        すべてIOC一覧側を参照しており、記事URLは iocs.json へ観測を持たない。
        """
        record = self._record()
        record["iocs"] = [
            {"reference": "https://vendor.example/iocs", "value": "198.51.100.10"},
            {"reference": "https://vendor.example/iocs", "value": "198.51.100.11"},
        ]
        ids = validate_daily.ioc_bearing_source_ids(record, self.QUEUE)
        self.assertEqual(ids, {source_id_for_value("https://vendor.example/iocs")})
        # 記事側(集約先・集約元のいずれも)はIOCを掲載していないため対象外になる
        self.assertNotIn(source_id_for_value("https://x.example/status/1"), ids)
        self.assertNotIn(source_id_for_value("https://vendor.example/writeup"), ids)

    def test_ioc_validation_still_covers_every_source_that_published_iocs(self) -> None:
        """複数のURLがIOCを掲載している場合は、その全URLを検証対象に残す。"""
        record = self._record()
        record["iocs"] = [
            {"reference": "https://vendor.example/iocs", "value": "198.51.100.10"},
            {"reference": "https://x.example/status/1", "value": "198.51.100.12"},
        ]
        ids = validate_daily.ioc_bearing_source_ids(record, self.QUEUE)
        self.assertEqual(
            ids,
            {
                source_id_for_value("https://vendor.example/iocs"),
                source_id_for_value("https://x.example/status/1"),
            },
        )

    def test_profile_source_prefers_the_source_own_date_and_title(self) -> None:
        record = self._record()
        items = source_items(record, self.QUEUE)
        by_url = {i["url"]: profile_source(record, i, self.QUEUE) for i in items}
        aliased = by_url["https://vendor.example/writeup"]
        # 集約先ではなく、その記事自身の日付と見出しを持つ
        self.assertEqual(aliased["published_at"]["value"], "2026-09-12T00:00:00Z")
        self.assertEqual(aliased["title"], "集約した記事の見出し")
        # 集約先の出典は従来どおり活動側の値を使う
        original = by_url["https://x.example/status/1"]
        self.assertEqual(original["published_at"]["value"], "2026-09-02T00:00:00Z")
        self.assertEqual(original["title"], "集約先の見出し")


class ApplyDecisionTests(unittest.TestCase):
    """保存済み判断の適用と、ウィンドウ走査での未一致の扱い。"""

    @staticmethod
    def _record() -> dict:
        return {
            "actor": {"slug": "unc1549"},
            "activity": {"activity_reference": "https://example.test/report"},
            "review_status": "pending",
            "capability_decisions": [
                {"name": "NodeRabbit / PollCat", "status": "pending", "reason": ""}
            ],
            "artifacts": [],
        }

    @staticmethod
    def _decisions() -> dict:
        return {
            "unc1549|https://example.test/report": {
                "review_status": "approved",
                "capability_decisions": [
                    {"name": "NodeRabbit", "status": "approved"},
                    {"name": "PollCat", "status": "approved"},
                    {"name": "NodeRabbit / PollCat", "status": "rejected"},
                ],
            }
        }

    def test_full_history_reports_capability_without_candidate(self) -> None:
        record = self._record()
        apply_decision(record, self._decisions())
        self.assertEqual(record["review_status"], "approved")
        # 複合値の判断はレコード側の候補へ適用される
        self.assertEqual(record["capability_decisions"][0]["status"], "rejected")
        # 個別名の判断は対応先がないため全履歴走査では課題として報告する
        self.assertEqual(
            record["decision_issues"],
            [
                "Capability判断の対象が入力に存在しない: noderabbit",
                "Capability判断の対象が入力に存在しない: pollcat",
            ],
        )

    def test_windowed_scan_does_not_report_capability_without_candidate(self) -> None:
        """ウィンドウ走査では、既に適用済みの判断が当該ウィンドウの入力に
        現れないことが正常に起こるため decision_issues を立てない。"""
        record = self._record()
        apply_decision(record, self._decisions(), report_unmatched=False)
        self.assertEqual(record["review_status"], "approved")
        self.assertEqual(record["capability_decisions"][0]["status"], "rejected")
        self.assertNotIn("decision_issues", record)

    def test_activity_overrides_replace_display_fields_only(self) -> None:
        """見出しが同じ資料内の別クラスタの作戦を指す場合だけ表示名を差し替える。"""
        record = self._record()
        record["activity"].update(
            {"title": "別クラスタの見出し", "summary": "別クラスタの要約"}
        )
        decisions = self._decisions()
        decisions["unc1549|https://example.test/report"]["activity_overrides"] = {
            "title": "正しい活動名",
            "summary": "正しい要約",
        }
        apply_decision(record, decisions, report_unmatched=False)
        self.assertEqual(record["activity"]["title"], "正しい活動名")
        self.assertEqual(record["activity"]["summary"], "正しい要約")
        # activity ID と record ID の生成元は差し替えない
        self.assertEqual(
            record["activity"]["activity_reference"], "https://example.test/report"
        )

    def test_windowed_scan_does_not_report_artifact_without_candidate(self) -> None:
        record = self._record()
        decisions = self._decisions()
        decisions["unc1549|https://example.test/report"]["approved_artifacts"] = [
            {"artifact_type": "file-name", "value": "absent.exe"}
        ]
        apply_decision(record, decisions, report_unmatched=False)
        self.assertNotIn("decision_issues", record)


if __name__ == "__main__":
    unittest.main()
