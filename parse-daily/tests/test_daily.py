from __future__ import annotations

import csv
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

import daily_check  # noqa: E402
import apply_review_queue  # noqa: E402
import validate_daily  # noqa: E402
from build_review_queue import apply_decision  # noqa: E402
from daily_check import latest_activity  # noqa: E402
from apply_review_queue import (  # noqa: E402
    activity_override_rerun_issues,
    activity_override_ownership_issues,
    planned_activity_identity_migrations,
    rebuild_actor_slugs,
)

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
    add_dataset_source,
    activity_bounds,
    activity_id_override_issue,
    activity_identity_migration_issues,
    activity_reported_at,
    profile_source,
    reviewed_reported_at_issue,
    activity_entry,
    activity_id_for,
    build_ledger,
    daily_rebuild_dependency_issues,
    ensure_malware_capabilities,
    merge_artifacts,
    merge_ioc_record,
    merge_duplicate_artifact_rows,
    merge_duplicate_observations,
    merge_materialized_activity,
    merge_materialized_source,
    migrate_cross_file_source_identities,
    migrate_activity_identities,
    migrate_profile_source_identities,
    migrate_source_manifest,
    reconcile_dataset_source_identity,
    reconcile_profile_source_identity,
    remove_daily_materialization,
    source_id_for_value,
    source_id_for_url,
    source_identity_migration_issues,
    source_manifest_migration_issues,
    source_items,
)
from ingest_observables import expand_sources  # noqa: E402


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
    def test_rebuild_refuses_to_strip_evidence_from_retained_claim(self) -> None:
        daily_source = "source--daily-example"
        profile_data = {
            "sources": [{"source_id": daily_source}],
            "activities": [],
            "actor": {
                "aliases": [
                    {
                        "name": "Reviewed alias",
                        "evidence_refs": [daily_source],
                    }
                ]
            },
            "capabilities": {"malware": []},
            "ttps": [],
            "victim_cases": [],
        }
        dataset = {"sources": [], "indicators": []}
        before = json.loads(json.dumps(profile_data))

        issues = daily_rebuild_dependency_issues(profile_data, dataset, [])

        self.assertTrue(any("actor.aliases" in issue for issue in issues))
        with self.assertRaisesRegex(ValueError, "retained claims"):
            remove_daily_materialization(profile_data, dataset, [])
        self.assertEqual(profile_data, before)

    def test_rebuild_dependency_audit_catches_singular_pivot_source(self) -> None:
        profile_data = {
            "sources": [{"source_id": "source--daily-example"}],
            "activities": [],
            "hunting_pivots": [
                {
                    "observations": [
                        {"source_ref": "source--daily-example"}
                    ]
                }
            ],
            "capabilities": {"malware": []},
        }

        issues = daily_rebuild_dependency_issues(
            profile_data, {"sources": [], "indicators": []}, []
        )

        self.assertTrue(any("source_ref" in issue for issue in issues))

    def test_rebuild_dependency_audit_catches_manifest_daily_refs(self) -> None:
        issues = daily_rebuild_dependency_issues(
            {
                "sources": [],
                "activities": [],
                "capabilities": {"malware": []},
            },
            {"sources": [], "indicators": []},
            [],
            {
                "defaults": {
                    "campaign_refs": ["activity--daily-example"]
                },
                "sources": [
                    {
                        "source_id": "source--daily-example",
                        "path": "evidence/example.csv",
                    }
                ],
            },
        )

        self.assertTrue(any("ioc-sources.defaults" in item for item in issues))
        self.assertTrue(any("source--daily-example" in item for item in issues))

    def test_rebuild_drops_indicator_with_only_daily_observations(self) -> None:
        daily_source = "source--daily-example"
        daily_activity = "activity--daily-example"
        profile_data = {
            "sources": [],
            "activities": [],
            "capabilities": {"malware": []},
            "ttps": [],
            "victim_cases": [],
        }
        observation = {
            "observation_id": "observation--daily",
            "source_id": daily_source,
            "observed_at": dict(UNKNOWN_POINT),
            "campaign_refs": [daily_activity],
            "malware_refs": [],
            "infrastructure_refs": [],
            "roles": [],
            "extraction_method": "tech-memo-structured-csv",
        }
        dataset = {
            "sources": [{"source_id": daily_source}],
            "indicators": [
                {
                    "type": "domain",
                    "normalized_value": "example.test",
                    "observation_count": 1,
                    "campaign_refs": [daily_activity],
                    "malware_refs": [],
                    "infrastructure_refs": [],
                    "roles": [],
                    "observations": [observation],
                }
            ],
        }

        self.assertEqual(
            daily_rebuild_dependency_issues(profile_data, dataset, []), []
        )
        remove_daily_materialization(profile_data, dataset, [])
        self.assertEqual(dataset["indicators"], [])

    def test_rebuild_refreshes_mixed_indicator_from_retained_observations(self) -> None:
        daily_source = "source--daily-example"
        stable_source = "source--curated-example"
        daily_observation = {
            "observation_id": "observation--daily",
            "source_id": daily_source,
            "observed_at": dict(UNKNOWN_POINT),
            "campaign_refs": ["activity--daily-example"],
            "malware_refs": ["malware--daily-example"],
            "infrastructure_refs": [],
            "roles": ["c2"],
            "extraction_method": "tech-memo-structured-csv",
        }
        stable_observation = {
            "observation_id": "observation--stable",
            "source_id": stable_source,
            "observed_at": known_point("2026-08-10T00:00:00Z"),
            "campaign_refs": ["campaign--stable"],
            "malware_refs": ["malware--stable"],
            "infrastructure_refs": ["infrastructure--stable"],
            "roles": ["payload-host"],
            "extraction_method": "csv-row",
        }
        profile_data = {
            "sources": [],
            "activities": [],
            "capabilities": {"malware": []},
            "ttps": [],
            "victim_cases": [],
        }
        dataset = {
            "sources": [
                {"source_id": daily_source},
                {"source_id": stable_source},
            ],
            "indicators": [
                {
                    "type": "domain",
                    "normalized_value": "example.test",
                    "observation_count": 2,
                    "campaign_refs": [
                        "activity--daily-example",
                        "campaign--stable",
                    ],
                    "malware_refs": [
                        "malware--daily-example",
                        "malware--stable",
                    ],
                    "infrastructure_refs": ["infrastructure--stable"],
                    "roles": ["c2", "payload-host"],
                    "observations": [daily_observation, stable_observation],
                }
            ],
        }

        self.assertEqual(
            daily_rebuild_dependency_issues(profile_data, dataset, []), []
        )
        remove_daily_materialization(profile_data, dataset, [])

        indicator = dataset["indicators"][0]
        self.assertEqual(indicator["observation_count"], 1)
        self.assertEqual(indicator["campaign_refs"], ["campaign--stable"])
        self.assertEqual(indicator["malware_refs"], ["malware--stable"])
        self.assertEqual(indicator["roles"], ["payload-host"])

        unsafe_dataset = json.loads(json.dumps(dataset))
        unsafe_dataset["indicators"][0]["observations"][0][
            "source_id"
        ] = daily_source
        issues = daily_rebuild_dependency_issues(
            profile_data, unsafe_dataset, []
        )
        self.assertTrue(any("source--daily-example" in issue for issue in issues))

    def test_rebuild_ignores_generated_ttp_and_victim_case_removed_with_activity(self) -> None:
        daily_activity = "activity--daily-example"
        profile_data = {
            "sources": [],
            "activities": [{"activity_id": daily_activity}],
            "capabilities": {"malware": []},
            "ttps": [
                {
                    "ttp_id": "ttp--activity-rule--example",
                    "activity_refs": [daily_activity],
                }
            ],
            "victim_cases": [
                {
                    "victim_id": "victim--daily-example",
                    "activity_refs": [daily_activity],
                }
            ],
        }
        dataset = {"sources": [], "indicators": []}

        self.assertEqual(
            daily_rebuild_dependency_issues(profile_data, dataset, []), []
        )
        remove_daily_materialization(profile_data, dataset, [])
        self.assertEqual(profile_data["ttps"], [])
        self.assertEqual(profile_data["victim_cases"], [])

    def test_rebuild_actor_set_includes_rejected_and_ledger_only_actors(self) -> None:
        queue = {
            "records": [
                {
                    "review_status": "rejected",
                    "actor": {"slug": "rejected-actor"},
                }
            ]
        }
        with tempfile.TemporaryDirectory() as directory:
            profiles_root = Path(directory)
            ledger = profiles_root / "ledger-only" / "daily-observations.json"
            ledger.parent.mkdir()
            ledger.write_text("{}", encoding="utf-8")

            self.assertEqual(
                rebuild_actor_slugs(queue, profiles_root),
                {"rejected-actor", "ledger-only"},
            )

    def test_date_from_path(self) -> None:
        self.assertEqual(date_from_path(Path("20260725.md")), "2026-07-25")
        self.assertIsNone(date_from_path(Path("notes.md")))

    def test_reconciled_unknown_clusters_preserve_entity_boundaries(self) -> None:
        ledger = json.loads((HERE / "unknown-clusters.json").read_text(encoding="utf-8"))
        clusters = {item["cluster_id"]: item for item in ledger["clusters"]}
        self.assertEqual(len(clusters), len(ledger["clusters"]))

        # BigBear 2.0 はCapability/Platform、General Bossは未確定の運用者ハンドル。
        # SecFlowもCapabilityであり、反復するNieをexact aliasへ昇格しない。
        self.assertEqual(clusters["unknown-cluster--bigbear-2-0"]["aliases"], [])
        self.assertEqual(clusters["unknown-cluster--secflow-ai-operator"]["aliases"], [])
        self.assertEqual(clusters["unknown-cluster--bigbear-2-0"]["entity_type"], "campaign")
        self.assertEqual(
            clusters["unknown-cluster--secflow-ai-operator"]["entity_type"], "campaign"
        )
        self.assertEqual(
            clusters["unknown-cluster--secflow-ai-operator"]["primary_name"],
            "SecFlow AI-agent campaign（運用者は未命名）",
        )
        self.assertEqual(
            (
                clusters["unknown-cluster--secflow-ai-operator"]["first_seen"],
                clusters["unknown-cluster--secflow-ai-operator"]["last_seen"],
            ),
            ("2026-05-15", "2026-08-04"),
        )
        self.assertEqual(
            (
                clusters["unknown-cluster--bigbear-2-0"]["first_seen"],
                clusters["unknown-cluster--bigbear-2-0"]["last_seen"],
            ),
            ("2026-06", "unknown"),
        )

        knaithe = clusters["unknown-cluster--knaithe-knyuan"]
        self.assertEqual(knaithe["entity_type"], "actor-cluster")
        self.assertNotEqual(knaithe["entity_type"], "individual")
        self.assertEqual(
            {(item["name"], item["scope"]) for item in knaithe["aliases"]},
            {("knaithe", "source-reported"), ("KnYuan", "source-reported")},
        )
        self.assertIn("460超は", knaithe["observations"][0]["targets"])
        codex = next(
            tool
            for tool in knaithe["observations"][0]["tools"]
            if tool["name"] == "Codex"
        )
        self.assertEqual(codex["usage_status"], "unverified")

        xentry = clusters["unknown-cluster--xentry-team"]
        self.assertEqual(xentry["entity_type"], "incident")
        self.assertEqual(
            (xentry["first_seen"], xentry["last_seen"]),
            ("2026-02", "2026-05"),
        )
        self.assertEqual(xentry["observations"][0]["malware"], [])
        self.assertIn("MSSQL", xentry["observations"][0]["summary"])
        self.assertIn("侵入経路ではなく", xentry["observations"][0]["summary"])
        self.assertTrue(
            all(
                tool["classification"].startswith("legitimate-")
                for tool in xentry["observations"][0]["tools"]
            )
        )

        project = clusters["unknown-cluster--project-cav3rn"]
        cavern = clusters["unknown-cluster--cavern-manticore"]
        self.assertEqual(project["entity_type"], "grouping")
        self.assertEqual(cavern["entity_type"], "group")
        self.assertNotEqual(project["cluster_id"], cavern["cluster_id"])
        self.assertEqual(project["aliases"], [])
        self.assertEqual(cavern["aliases"], [])
        oilrig = next(
            item for item in project["related_profiles"] if item["slug"] == "apt34"
        )
        self.assertEqual(oilrig["confidence"], "low")
        self.assertIn("直接のコード再利用とインフラ重複がない", oilrig["basis"])
        self.assertEqual(cavern["last_seen"], "unknown")
        self.assertEqual(
            {item["slug"] for item in cavern["related_profiles"]},
            {"apt34", "muddywater"},
        )

        toy_aliases = {
            item["name"] for item in clusters["unknown-cluster--toy-ghouls"]["aliases"]
        }
        self.assertIn("Labubu", toy_aliases)
        self.assertNotIn("Labuib", toy_aliases)

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

    def test_config_ignores_known_product_and_vulnerability_names(self) -> None:
        """過去の走査でアクター候補になった製品名・脆弱性名を再検出しない。"""
        ignored = CONFIG["matching"]["ignored_name_candidates"]
        article = {
            "title": "",
            "body": (
                "- その他\n"
                "    - 脅威アクターBigBear 2.0が観測されたとの記述。\n"
                "    - 脅威アクターMikroTik RouterOSが観測されたとの記述。\n"
                "    - 脅威アクターOpenAI Codexが観測されたとの記述。\n"
                "    - 脅威アクターShellshockが観測されたとの記述。\n"
                "    - 脅威アクターTrezorが観測されたとの記述。\n"
                "    - 脅威アクターVBScriptが観測されたとの記述。\n"
            ),
        }
        self.assertEqual(name_candidates(article, self.registry_with("APT28"), ignored), [])

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

    def test_reviewed_activity_id_override_is_stable_and_actor_scoped(self) -> None:
        record = {
            "record_id": "daily-record--example",
            "actor": {"slug": "darkhotel"},
            "activity": {
                "activity_reference": "https://vendor.example/report"
            },
            "activity_id_override": "activity--darkhotel-kctv-lure-2026",
        }

        self.assertEqual(
            activity_id_for(record),
            "activity--darkhotel-kctv-lure-2026",
        )
        self.assertIsNone(
            activity_id_override_issue(
                record["activity_id_override"], "darkhotel"
            )
        )
        self.assertIsNotNone(
            activity_id_override_issue(
                "activity--other-kctv-lure-2026", "darkhotel"
            )
        )
        self.assertIsNotNone(
            activity_id_override_issue(
                "activity--daily-fbc4f59c4a844e18e5ab", "darkhotel"
            )
        )

    def test_two_generated_activities_cannot_share_one_stable_override(self) -> None:
        records = [
            {
                "record_id": f"record--{suffix}",
                "actor": {"slug": "example"},
                "activity": {
                    "activity_reference": f"https://example.test/{suffix}"
                },
                "activity_id_override": "activity--example-reviewed-operation",
            }
            for suffix in ("one", "two")
        ]

        with self.assertRaisesRegex(ValueError, "is shared by"):
            planned_activity_identity_migrations(records)

    def test_cross_actor_override_ownership_is_rejected(self) -> None:
        target_id = "activity--example-stable-operation"
        grouped = {
            "example": [
                {
                    "record_id": "record--one",
                    "actor": {"slug": "example"},
                    "activity": {
                        "activity_reference": "https://example.test/one"
                    },
                    "activity_id_override": target_id,
                }
            ]
        }
        with tempfile.TemporaryDirectory() as directory:
            profiles_root = Path(directory)
            for slug, activities in (
                ("example", []),
                ("other", [{"activity_id": target_id}]),
            ):
                profile_dir = profiles_root / slug
                profile_dir.mkdir()
                (profile_dir / "actor-profile.json").write_text(
                    json.dumps({"activities": activities}), encoding="utf-8"
                )

            issues = activity_override_ownership_issues(grouped, profiles_root)

        self.assertTrue(any("already owned by other" in issue for issue in issues))

    def test_same_actor_existing_override_requires_rerun_ownership_proof(self) -> None:
        record = {
            "record_id": "daily-record--example",
            "actor": {"slug": "example"},
            "activity": {"activity_reference": "https://example.test/report"},
            "activity_id_override": "activity--example-reviewed-operation",
        }
        profile_data = {
            "activities": [
                {"activity_id": "activity--example-reviewed-operation"}
            ]
        }

        self.assertTrue(
            activity_override_rerun_issues(profile_data, [record], None)
        )
        self.assertEqual(
            activity_override_rerun_issues(
                profile_data,
                [record],
                {
                    "records": [
                        {
                            "record_id": record["record_id"],
                            "activity_id_override": record[
                                "activity_id_override"
                            ],
                        }
                    ]
                },
            ),
            [],
        )

    def test_activity_identity_migration_updates_every_structured_reference(self) -> None:
        class Common:
            @staticmethod
            def json_array_cell(value: object) -> str:
                return json.dumps(value, ensure_ascii=False)

        old_id = "activity--daily-example"
        new_id = "activity--example-reviewed-2026"
        profile_data = {
            "activities": [{"activity_id": old_id, "activity_refs": []}],
            "ttps": [{"activity_refs": [old_id]}],
            "victim_cases": [{"activity_refs": [old_id]}],
        }
        observation = {
            "campaign_refs": [old_id],
            "malware_refs": [],
            "infrastructure_refs": [],
            "roles": [],
            "observed_at": dict(UNKNOWN_POINT),
        }
        dataset = {
            "indicators": [
                {
                    "observations": [observation],
                    "campaign_refs": [old_id],
                }
            ]
        }
        artifacts = [
            {
                "campaign_refs": json.dumps([old_id]),
                "campaign_count": "1",
                "seen_in_multiple_campaigns": "false",
            }
        ]
        manifest = {
            "defaults": {"campaign_refs": [old_id]},
            "sources": [],
            "source_groups": [],
        }

        migrated_artifacts = migrate_activity_identities(
            profile_data,
            dataset,
            artifacts,
            manifest,
            {old_id: new_id},
            Common(),
        )

        self.assertEqual(profile_data["activities"][0]["activity_id"], new_id)
        self.assertEqual(profile_data["ttps"][0]["activity_refs"], [new_id])
        self.assertEqual(dataset["indicators"][0]["campaign_refs"], [new_id])
        self.assertEqual(observation["campaign_refs"], [new_id])
        self.assertEqual(manifest["defaults"]["campaign_refs"], [new_id])
        self.assertEqual(
            json.loads(migrated_artifacts[0]["campaign_refs"]), [new_id]
        )

    def test_activity_identity_collision_is_rejected_before_migration(self) -> None:
        old_id = "activity--daily-example"
        new_id = "activity--example-reviewed-2026"
        issues = activity_identity_migration_issues(
            {
                "activities": [
                    {"activity_id": old_id},
                    {"activity_id": new_id},
                ]
            },
            {"indicators": []},
            [],
            None,
            {old_id: new_id},
        )

        self.assertTrue(any("already exists beside source" in item for item in issues))

    def test_override_activity_refreshes_reviewed_core_and_keeps_manual_refs(self) -> None:
        existing = {
            "activity_id": "activity--darkhotel-kctv-lure-2026",
            "name": "old title",
            "reported_at": known_point("2026-08-11T00:00:00Z"),
            "activity_refs": [],
            "target_refs": [],
            "malware_refs": [],
            "infrastructure_refs": [],
            "tool_refs": ["tool--manual"],
            "ttp_refs": ["ttp--manual"],
            "victim_refs": [],
            "evidence_refs": ["source--manual"],
            "analyst_notes": "manual enrichment",
            "diamond_model": {"stale": True},
        }
        modeled = {
            **existing,
            "name": "reviewed title",
            "reported_at": known_point("2026-08-12T00:00:00Z"),
            "tool_refs": [],
            "ttp_refs": [],
            "evidence_refs": ["source--reviewed"],
            "analyst_notes": "reviewed decision",
            "diamond_model": {"stale": False},
        }

        merged = merge_materialized_activity(existing, modeled)

        self.assertEqual(merged["name"], "reviewed title")
        self.assertEqual(
            merged["reported_at"]["value"], "2026-08-12T00:00:00Z"
        )
        self.assertEqual(merged["tool_refs"], ["tool--manual"])
        self.assertEqual(merged["ttp_refs"], ["ttp--manual"])
        self.assertEqual(
            merged["evidence_refs"],
            ["source--manual", "source--reviewed"],
        )
        self.assertEqual(merged["diamond_model"], {"stale": False})
        self.assertEqual(
            merge_materialized_activity(merged, modeled), merged
        )

    def test_duplicate_context_merge_is_idempotent(self) -> None:
        class Common:
            @staticmethod
            def json_array_cell(value: object) -> str:
                return json.dumps(value, ensure_ascii=False)

        observation = {
            "campaign_refs": [],
            "malware_refs": [],
            "infrastructure_refs": [],
            "roles": [],
            "confidence": "medium",
            "context_excerpt": "first | second",
            "analyst_notes": "one | two",
            "observed_at": dict(UNKNOWN_POINT),
        }
        incoming = {
            **observation,
            "context_excerpt": "second",
            "analyst_notes": "two",
        }
        merged_observation = merge_duplicate_observations(
            observation, incoming
        )
        self.assertEqual(merged_observation["context_excerpt"], "first | second")
        self.assertEqual(merged_observation["analyst_notes"], "one | two")
        self.assertEqual(
            merge_duplicate_observations(merged_observation, incoming),
            merged_observation,
        )

        artifact = {
            "campaign_refs": "[]",
            "malware_refs": "[]",
            "infrastructure_refs": "[]",
            "roles": "[]",
            "confidence": "medium",
            "context_excerpt": "first | second",
            "analyst_notes": "one | two",
            "observed_at": "",
        }
        incoming_artifact = {
            **artifact,
            "context_excerpt": "second",
            "analyst_notes": "two",
        }
        merged_artifact = merge_duplicate_artifact_rows(
            artifact, incoming_artifact, Common()
        )
        self.assertEqual(merged_artifact["context_excerpt"], "first | second")
        self.assertEqual(merged_artifact["analyst_notes"], "one | two")
        self.assertEqual(
            merge_duplicate_artifact_rows(
                merged_artifact, incoming_artifact, Common()
            ),
            merged_artifact,
        )

    def test_daily_source_reuses_curated_identity_for_same_canonical_url(self) -> None:
        source = {
            "url": "https://vendor.example/report",
            "source_type": "primary-report",
        }
        existing = [
            {
                "source_id": "source--curated-report",
                "path": "https://vendor.example/report",
                "published_at": {
                    "value": "2026-08-12T00:00:00Z",
                    "precision": "day",
                    "status": "known",
                    "basis": "source-publication",
                },
            }
        ]

        self.assertEqual(
            source_id_for_url(source, existing),
            "source--curated-report",
        )
        self.assertEqual(
            source_id_for_url(source, []),
            source_id_for_value("https://vendor.example/report"),
        )

    def test_source_identity_ignores_tracking_fragment_and_trailing_slash(self) -> None:
        canonical_url = "https://vendor.example/report"
        source = {
            "url": (
                "https://vendor.example/report/"
                "?utm_source=newsletter&utm_campaign=incident&srsltid=tracking"
                "#technical-details"
            )
        }
        existing = [
            {
                "source_id": "source--curated-report",
                "path": canonical_url,
            }
        ]

        self.assertEqual(
            source_id_for_url(source, existing),
            "source--curated-report",
        )
        self.assertEqual(
            source_id_for_url(source, []),
            source_id_for_value(canonical_url),
        )

    def test_source_identity_preserves_meaningful_query_parameters(self) -> None:
        base_url = "https://vendor.example/report"
        selected_url = (
            "https://vendor.example/report/?document=42&utm_source=newsletter#section"
        )
        existing = [
            {
                "source_id": "source--curated-base",
                "path": base_url,
            }
        ]

        self.assertNotEqual(
            source_id_for_url({"url": selected_url}, existing),
            "source--curated-base",
        )
        self.assertEqual(
            source_id_for_url({"url": selected_url}, []),
            source_id_for_value("https://vendor.example/report?document=42"),
        )

    def test_reviewed_publication_fills_unknown_curated_source_date(self) -> None:
        curated = {
            "source_id": "source--curated-report",
            "title": "Curated title",
            "published_at": dict(UNKNOWN_POINT),
            "source_type": "vendor-threat-research",
        }
        reviewed = {
            "source_id": "source--daily-example",
            "title": "Daily title",
            "published_at": {
                "value": "2026-08-12T00:00:00Z",
                "precision": "day",
                "status": "known",
                "basis": "source-publication",
            },
            "source_type": "osint-report",
        }

        merged = merge_materialized_source(curated, reviewed)

        self.assertEqual(merged["source_id"], "source--curated-report")
        self.assertEqual(merged["title"], "Curated title")
        self.assertEqual(merged["source_type"], "vendor-threat-research")
        self.assertEqual(merged["published_at"], reviewed["published_at"])

    def test_curated_source_identity_wins_over_same_url_daily_source(self) -> None:
        source = {"url": "https://vendor.example/report"}
        existing = [
            {
                "source_id": source_id_for_value(source["url"]),
                "path": source["url"],
            },
            {
                "source_id": "source--curated-report",
                "path": source["url"],
            },
        ]

        self.assertEqual(
            source_id_for_url(source, existing),
            "source--curated-report",
        )

    def test_source_identity_reconciliation_deduplicates_ioc_observations(self) -> None:
        class Common:
            @staticmethod
            def stable_id(kind: str, *parts: object) -> str:
                return f"{kind}--" + "|".join(str(item) for item in parts)

        url = "https://vendor.example/report"
        old_id = source_id_for_value(url)
        new_id = "source--curated-report"
        observation = {
            "observation_id": "observation--legacy",
            "observed_at": dict(UNKNOWN_POINT),
            "source_published_at": dict(UNKNOWN_POINT),
            "source_id": old_id,
            "source_path": url,
            "source_location": {"path": "daily-news/iocs/20260815.csv", "row": 2},
            "extraction_method": "tech-memo-structured-csv",
            "campaign_refs": ["activity--daily-example"],
            "malware_refs": [],
            "infrastructure_refs": [],
            "roles": [],
        }
        dataset = {
            "actor_ref": "actor--example",
            "sources": [
                {"source_id": old_id, "path": url, "published_at": dict(UNKNOWN_POINT)},
                {
                    "source_id": new_id,
                    "path": url,
                    "published_at": {
                        "value": "2026-08-12T00:00:00Z",
                        "precision": "day",
                        "status": "known",
                        "basis": "source-publication",
                    },
                },
            ],
            "indicators": [
                {
                    "type": "domain",
                    "normalized_value": "example.test",
                    "observations": [
                        {
                            **observation,
                            "campaign_refs": ["activity--old"],
                            "malware_refs": ["malware--old"],
                            "confidence": "low",
                        },
                        {
                            **observation,
                            "source_id": new_id,
                            "campaign_refs": ["activity--new"],
                            "malware_refs": ["malware--new"],
                            "confidence": "high",
                        },
                    ],
                }
            ],
        }

        reconcile_dataset_source_identity(
            dataset, {"url": url}, new_id, Common()
        )

        self.assertEqual([item["source_id"] for item in dataset["sources"]], [new_id])
        observations = dataset["indicators"][0]["observations"]
        self.assertEqual(len(observations), 1)
        self.assertEqual(observations[0]["source_id"], new_id)
        self.assertEqual(
            observations[0]["campaign_refs"], ["activity--new", "activity--old"]
        )
        self.assertEqual(
            observations[0]["malware_refs"], ["malware--new", "malware--old"]
        )
        self.assertEqual(observations[0]["confidence"], "low")
        self.assertEqual(dataset["indicators"][0]["observation_count"], 1)

    def test_source_reconciliation_refreshes_publication_without_old_identity(self) -> None:
        class Common:
            @staticmethod
            def stable_id(kind: str, *parts: object) -> str:
                return f"{kind}--" + "|".join(str(item) for item in parts)

        url = "https://vendor.example/report"
        source_id = "source--curated-report"
        published = {
            "value": "2026-08-12T00:00:00Z",
            "precision": "day",
            "status": "known",
            "basis": "source-publication",
        }
        dataset = {
            "actor_ref": "actor--example",
            "sources": [
                {"source_id": source_id, "path": url, "published_at": published}
            ],
            "indicators": [
                {
                    "type": "domain",
                    "normalized_value": "example.test",
                    "observations": [
                        {
                            "observation_id": "observation--stable",
                            "observed_at": dict(UNKNOWN_POINT),
                            "source_published_at": dict(UNKNOWN_POINT),
                            "source_id": source_id,
                            "source_path": url,
                            "campaign_refs": [],
                            "malware_refs": [],
                            "infrastructure_refs": [],
                            "roles": [],
                        }
                    ],
                }
            ],
        }

        reconcile_dataset_source_identity(
            dataset, {"url": url}, source_id, Common()
        )

        observation = dataset["indicators"][0]["observations"][0]
        self.assertEqual(observation["observation_id"], "observation--stable")
        self.assertEqual(observation["source_published_at"], published)

    def test_profile_source_reconciliation_updates_plural_and_singular_refs(self) -> None:
        url = "https://vendor.example/report"
        old_id = source_id_for_value(url)
        new_id = "source--curated-report"
        profile_data = {
            "sources": [
                {"source_id": old_id, "path": url},
                {"source_id": new_id, "path": url},
            ],
            "activities": [{"evidence_refs": [old_id]}],
            "hunting_pivots": [{"observations": [{"source_ref": old_id}]}],
        }

        reconcile_profile_source_identity(profile_data, {"url": url}, new_id)

        self.assertEqual(
            [item["source_id"] for item in profile_data["sources"]], [new_id]
        )
        self.assertEqual(profile_data["activities"][0]["evidence_refs"], [new_id])
        self.assertEqual(
            profile_data["hunting_pivots"][0]["observations"][0]["source_ref"],
            new_id,
        )

    def test_ioc_materialization_uses_profile_curated_source_identity(self) -> None:
        class Common:
            @staticmethod
            def normalize_observable(_kind: str, value: str) -> str:
                return value.casefold()

            @staticmethod
            def stable_id(kind: str, *parts: object) -> str:
                return f"{kind}--" + "|".join(str(item) for item in parts)

            @staticmethod
            def stix_pattern(kind: str, value: str) -> str:
                return f"[{kind}:value = '{value}']"

        url = "https://vendor.example/report"
        record = {
            "record_id": "daily-record--example",
            "actor": {"slug": "example"},
            "activity": {
                "title": "Example report",
                "news_path": "daily-news/news/20260815.md",
                "news_date": "2026-08-15",
                "activity_reference": url,
                "primary_url": url,
            },
            "reported_at": {
                "value": "2026-08-12T00:00:00Z",
                "precision": "day",
                "status": "known",
                "basis": "source-publication",
            },
            "confidence": "high",
            "iocs": [
                {
                    "type": "domain",
                    "value": "EXAMPLE.TEST",
                    "reference": url,
                    "source_path": "daily-news/iocs/20260815.csv",
                    "row": 2,
                    "observed_date": "",
                }
            ],
        }
        dataset = {"actor_ref": "actor--example", "sources": [], "indicators": []}
        queue = {"source": {"repository": "owner/repo", "commit": "abc"}}

        merge_ioc_record(
            dataset,
            record,
            queue,
            Common(),
            preferred_sources=[{"source_id": "source--curated", "path": url}],
        )

        self.assertEqual(dataset["sources"][0]["source_id"], "source--curated")
        self.assertEqual(
            dataset["indicators"][0]["observations"][0]["source_id"],
            "source--curated",
        )
        observation = dataset["indicators"][0]["observations"][0]
        observation["campaign_refs"].append("activity--historical")
        observation["malware_refs"].append("malware--historical")

        merge_ioc_record(
            dataset,
            record,
            queue,
            Common(),
            preferred_sources=[{"source_id": "source--curated", "path": url}],
        )

        observation = dataset["indicators"][0]["observations"][0]
        self.assertIn("activity--historical", observation["campaign_refs"])
        self.assertIn("malware--historical", observation["malware_refs"])

    def test_cross_file_source_migration_preserves_ingest_id_contract(self) -> None:
        class Common:
            @staticmethod
            def stable_id(kind: str, *parts: object) -> str:
                return f"{kind}--" + "|".join(str(item) for item in parts)

            @staticmethod
            def json_array_cell(value: object) -> str:
                return json.dumps(value, ensure_ascii=False)

        old_id = "source--daily-old"
        new_id = "source--curated"
        published = {
            "value": "2026-08-12T00:00:00Z",
            "precision": "day",
            "status": "known",
            "basis": "source-publication",
        }
        location = {"row": 2}
        dataset = {
            "actor_ref": "actor--example",
            "sources": [
                {
                    "source_id": old_id,
                    "path": "actor_profile/evidence/example.csv",
                    "published_at": dict(UNKNOWN_POINT),
                }
            ],
            "indicators": [
                {
                    "type": "certificate-fingerprint",
                    "normalized_value": "aabb",
                    "observations": [
                        {
                            "observation_id": "observation--old",
                            "source_id": old_id,
                            "source_location": location,
                            "source_published_at": dict(UNKNOWN_POINT),
                            "observed_at": dict(UNKNOWN_POINT),
                            "hash_algorithm": "SHA-256",
                            "extraction_method": "csv-row",
                            "campaign_refs": ["activity--old"],
                            "malware_refs": [],
                            "infrastructure_refs": [],
                            "roles": [],
                            "confidence": "medium",
                        }
                    ],
                }
            ],
        }
        artifact_rows = [
            {
                "actor_ref": "actor--example",
                "observation_id": "observation--artifact-old",
                "artifact_type": "file-name",
                "normalized_value": "sample.exe",
                "source_id": old_id,
                "source_location": json.dumps(location),
                "source_published_at": "",
                "extraction_method": "csv-row",
                "campaign_refs": "[]",
                "malware_refs": "[]",
                "infrastructure_refs": "[]",
                "roles": "[]",
                "confidence": "medium",
                "context_excerpt": "",
                "analyst_notes": "",
            }
        ]

        artifacts = migrate_cross_file_source_identities(
            dataset,
            artifact_rows,
            {old_id: new_id},
            [
                {
                    "source_id": new_id,
                    "path": "https://vendor.example/report",
                    "published_at": published,
                }
            ],
            Common(),
        )

        observation = dataset["indicators"][0]["observations"][0]
        location_json = json.dumps(location, sort_keys=True)
        self.assertEqual(observation["source_id"], new_id)
        self.assertEqual(
            observation["observation_id"],
            (
                "observation--actor--example|certificate-fingerprint|SHA-256|"
                f"aabb|{new_id}|{location_json}"
            ),
        )
        self.assertEqual(observation["source_published_at"], published)
        self.assertEqual(
            artifacts[0]["observation_id"],
            f"observation--actor--example|file-name|sample.exe|{new_id}|{location_json}",
        )
        self.assertEqual(artifacts[0]["source_published_at"], published["value"])

    def test_rebuild_migrates_safe_retained_source_refs_before_daily_removal(self) -> None:
        class Common:
            @staticmethod
            def stable_id(kind: str, *parts: object) -> str:
                return f"{kind}--" + "|".join(str(item) for item in parts)

            @staticmethod
            def json_array_cell(value: object) -> str:
                return json.dumps(value, ensure_ascii=False)

        old_id = "source--daily-old"
        new_id = "source--curated-report"
        published = {
            "value": "2026-08-12T00:00:00Z",
            "precision": "day",
            "status": "known",
            "basis": "source-publication",
        }
        profile_data = {
            "sources": [
                {"source_id": old_id, "path": "https://example.test/report"},
                {
                    "source_id": new_id,
                    "path": "https://example.test/report",
                    "published_at": published,
                },
            ],
            "actor": {"aliases": [{"name": "Alias", "evidence_refs": [old_id]}]},
            "activities": [],
            "capabilities": {"malware": []},
            "ttps": [],
            "victim_cases": [],
        }
        location = {"row": 2}
        dataset = {
            "actor_ref": "actor--example",
            "sources": [{"source_id": old_id}],
            "indicators": [
                {
                    "type": "domain",
                    "normalized_value": "example.test",
                    "observations": [
                        {
                            "observation_id": "observation--old",
                            "source_id": old_id,
                            "source_location": location,
                            "source_published_at": dict(UNKNOWN_POINT),
                            "observed_at": dict(UNKNOWN_POINT),
                            "extraction_method": "csv-row",
                            "campaign_refs": [],
                            "malware_refs": [],
                            "infrastructure_refs": [],
                            "roles": [],
                            "confidence": "medium",
                        }
                    ],
                }
            ],
        }
        artifacts = [
            {
                "actor_ref": "actor--example",
                "observation_id": "observation--artifact-old",
                "artifact_type": "file-name",
                "normalized_value": "sample.exe",
                "source_id": old_id,
                "source_location": json.dumps(location),
                "source_published_at": "",
                "extraction_method": "csv-row",
                "campaign_refs": "[]",
                "malware_refs": "[]",
                "infrastructure_refs": "[]",
                "roles": "[]",
                "confidence": "medium",
                "context_excerpt": "",
                "analyst_notes": "",
            }
        ]
        source_map = {old_id: new_id}

        migrate_profile_source_identities(profile_data, source_map)
        artifacts = migrate_cross_file_source_identities(
            dataset,
            artifacts,
            source_map,
            profile_data["sources"],
            Common(),
        )

        self.assertEqual(
            daily_rebuild_dependency_issues(profile_data, dataset, artifacts), []
        )
        artifacts = remove_daily_materialization(
            profile_data, dataset, artifacts
        )
        self.assertEqual(
            profile_data["actor"]["aliases"][0]["evidence_refs"], [new_id]
        )
        self.assertEqual(
            dataset["indicators"][0]["observations"][0]["source_id"], new_id
        )
        self.assertEqual(artifacts[0]["source_id"], new_id)

    def test_unknown_source_migration_method_is_rejected_in_preflight(self) -> None:
        class Common:
            @staticmethod
            def stable_id(kind: str, *parts: object) -> str:
                return f"{kind}--" + "|".join(str(item) for item in parts)

        old_id = "source--daily-old"
        dataset = {
            "actor_ref": "actor--example",
            "indicators": [
                {
                    "type": "domain",
                    "normalized_value": "example.test",
                    "observations": [
                        {
                            "observation_id": "observation--old",
                            "source_id": old_id,
                            "source_location": {"row": 2},
                            "extraction_method": "custom-parser",
                            "campaign_refs": [],
                            "malware_refs": [],
                            "infrastructure_refs": [],
                            "roles": [],
                        }
                    ],
                }
            ],
        }

        issues = source_identity_migration_issues(
            dataset, [], {old_id: "source--curated"}, Common()
        )

        self.assertTrue(
            any("unsupported IOC extraction_method" in item for item in issues)
        )

    def test_manifest_source_migration_survives_reingest_expansion(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repository_root = Path(directory)
            first = repository_root / "first.csv"
            second = repository_root / "second.csv"
            first.write_text("value\nfirst.example\n", encoding="utf-8")
            second.write_text("value\nsecond.example\n", encoding="utf-8")
            old_first = "source--daily-first"
            old_second = "source--daily-second"
            selected = "source--curated-report"
            manifest = {
                "defaults": {},
                "sources": [
                    {
                        "source_id": old_first,
                        "path": first.name,
                        "field_map": {"value": "value"},
                    },
                    {
                        "source_id": old_second,
                        "path": second.name,
                        "field_map": {"value": "value"},
                    },
                ],
                "source_groups": [],
            }

            migrate_source_manifest(
                manifest,
                {old_first: selected, old_second: selected},
            )
            expanded = expand_sources(manifest, repository_root)

            self.assertEqual(len(manifest["sources"]), 2)
            self.assertEqual(len(expanded), 2)
            self.assertEqual(
                {item["source_id"] for item in expanded}, {selected}
            )
            self.assertNotIn(
                old_first,
                {item["source_id"] for item in expanded},
            )
            self.assertEqual(
                manifest["sources"][0]["field_map"], {"value": "value"}
            )

    def test_manifest_source_group_generated_id_migration_is_rejected(self) -> None:
        old_id = "source--corpus--0123456789abcdef"
        issues = source_manifest_migration_issues(
            {
                "sources": [],
                "source_groups": [
                    {
                        "source_id_prefix": "source--corpus",
                        "path_glob": "evidence/*.csv",
                    }
                ],
            },
            {old_id: "source--curated"},
        )

        self.assertTrue(any("can regenerate" in item for item in issues))

    def test_manifest_source_merge_conflict_is_rejected_before_write(self) -> None:
        manifest = {
            "defaults": {"confidence": "unknown", "tlp": "TLP:CLEAR"},
            "sources": [
                {
                    "source_id": "source--daily-one",
                    "path": "one.csv",
                    "published_at": "2026-08-11",
                },
                {
                    "source_id": "source--daily-two",
                    "path": "two.csv",
                    "published_at": "2026-08-12",
                },
            ],
            "source_groups": [],
        }

        issues = source_manifest_migration_issues(
            manifest,
            {
                "source--daily-one": "source--curated",
                "source--daily-two": "source--curated",
            },
        )

        self.assertTrue(
            any("conflicting published_at" in item for item in issues)
        )

    def test_manifest_source_merge_allows_unknown_to_known_metadata(self) -> None:
        manifest = {
            "defaults": {"confidence": "unknown", "tlp": "TLP:CLEAR"},
            "sources": [
                {
                    "source_id": "source--daily-one",
                    "path": "one.csv",
                    "published_at": None,
                },
                {
                    "source_id": "source--daily-two",
                    "path": "two.csv",
                    "published_at": "2026-08-12",
                    "confidence": "high",
                },
            ],
            "source_groups": [],
        }

        issues = source_manifest_migration_issues(
            manifest,
            {
                "source--daily-one": "source--curated",
                "source--daily-two": "source--curated",
            },
        )

        self.assertEqual(issues, [])

    def test_dynamic_manifest_campaign_refs_block_activity_id_migration(self) -> None:
        issues = activity_identity_migration_issues(
            {"activities": []},
            {"indicators": []},
            [],
            {
                "defaults": {},
                "sources": [
                    {
                        "source_id": "source--example",
                        "path": "evidence.csv",
                        "field_map": {"campaign_refs": "campaign_refs"},
                    }
                ],
                "source_groups": [],
            },
            {"activity--daily-old": "activity--example-stable"},
        )

        self.assertTrue(any("dynamic Activity refs" in item for item in issues))

    def test_global_osint_input_blocks_unmigrated_activity_override(self) -> None:
        record = {
            "record_id": "daily-record--example",
            "actor": {"slug": "example"},
            "activity": {"activity_reference": "https://example.test/report"},
            "activity_id_override": "activity--example-stable-operation",
        }
        old_id = activity_id_for(
            {key: value for key, value in record.items() if key != "activity_id_override"}
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            profiles_root = root / "profiles"
            profile_dir = profiles_root / "example"
            profile_dir.mkdir(parents=True)
            (profile_dir / "actor-profile.json").write_text(
                '{"activities": []}', encoding="utf-8"
            )
            osint_dir = root / "actor_profile" / "osint"
            osint_dir.mkdir(parents=True)
            (osint_dir / "hunting-entity-research.json").write_text(
                json.dumps({"activity_refs": [old_id]}), encoding="utf-8"
            )

            with mock.patch.object(apply_review_queue, "REPO_ROOT", root):
                issues = activity_override_ownership_issues(
                    {"example": [record]}, profiles_root
                )

        self.assertTrue(
            any("global Activity curation" in issue for issue in issues)
        )

    def test_multi_actor_apply_preflights_all_dates_before_writing(self) -> None:
        reviewed = {
            "value": "2026-08-12T00:00:00Z",
            "precision": "day",
            "status": "known",
            "basis": "source-publication",
        }
        url = "https://vendor.example/report"
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            profiles_root = root / "profiles"
            snapshots: dict[Path, bytes] = {}
            for slug, sources in (
                ("actor-a", []),
                (
                    "actor-b",
                    [
                        {
                            "source_id": "source--curated",
                            "path": url,
                            "published_at": {**reviewed, "value": "2026-08-11T00:00:00Z"},
                        }
                    ],
                ),
            ):
                actor_dir = profiles_root / slug
                actor_dir.mkdir(parents=True)
                files = {
                    actor_dir / "actor-profile.json": json.dumps(
                        {"sources": sources}, ensure_ascii=False
                    ).encode(),
                    actor_dir / "iocs.json": b'{"sources": [], "indicators": []}',
                    actor_dir / "artifacts.csv": b"observation_id,source_id,extraction_method\n",
                }
                for path, content in files.items():
                    path.write_bytes(content)
                    snapshots[path] = content
            records = []
            for slug in ("actor-a", "actor-b"):
                records.append(
                    {
                        "record_id": f"record--{slug}",
                        "review_status": "approved",
                        "actor": {"slug": slug},
                        "activity": {
                            "title": "Example",
                            "news_date": "2026-08-15",
                            "news_path": "daily-news/news/20260815.md",
                            "primary_url": url,
                            "activity_reference": url,
                        },
                        "reported_at": reviewed,
                    }
                )
            queue_path = root / "queue.json"
            queue_path.write_text(
                json.dumps(
                    {
                        "source": {"repository": "owner/repo", "commit": "abc"},
                        "decision_issues": [],
                        "records": records,
                    }
                ),
                encoding="utf-8",
            )

            argv = [
                "apply_review_queue.py",
                str(queue_path),
                "--profiles-root",
                str(profiles_root),
                "--apply",
                "--no-render",
            ]
            with mock.patch.object(sys, "argv", argv):
                with self.assertRaisesRegex(SystemExit, "preflight failed before writes"):
                    apply_review_queue.main()

            for path, content in snapshots.items():
                self.assertEqual(path.read_bytes(), content)

    def test_rebuild_dry_run_rejects_unsafe_manifest_dependency(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            actor_dir = root / "profiles" / "actor-a"
            actor_dir.mkdir(parents=True)
            (actor_dir / "actor-profile.json").write_text(
                json.dumps(
                    {
                        "sources": [],
                        "activities": [],
                        "actor": {"aliases": []},
                        "capabilities": {"malware": []},
                        "ttps": [],
                        "victim_cases": [],
                    }
                ),
                encoding="utf-8",
            )
            (actor_dir / "ioc-sources.json").write_text(
                json.dumps(
                    {
                        "defaults": {
                            "campaign_refs": ["activity--daily-example"]
                        },
                        "sources": [],
                        "source_groups": [],
                    }
                ),
                encoding="utf-8",
            )
            (actor_dir / "iocs.json").write_text(
                '{"sources": [], "indicators": []}', encoding="utf-8"
            )
            (actor_dir / "artifacts.csv").write_text(
                "observation_id,source_id,extraction_method\n",
                encoding="utf-8",
            )
            queue_path = root / "queue.json"
            queue_path.write_text(
                json.dumps(
                    {
                        "source": {"repository": "owner/repo", "commit": "abc"},
                        "decision_issues": [],
                        "records": [
                            {
                                "record_id": "record--actor-a",
                                "review_status": "rejected",
                                "actor": {"slug": "actor-a"},
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            argv = [
                "apply_review_queue.py",
                str(queue_path),
                "--profiles-root",
                str(root / "profiles"),
                "--rebuild-daily",
            ]

            with mock.patch.object(sys, "argv", argv):
                with self.assertRaisesRegex(
                    SystemExit, "rebuild dependency"
                ):
                    apply_review_queue.main()

    def test_darkhotel_stable_activity_rebuild_is_idempotent(self) -> None:
        source_dir = HERE.parent / "profiles" / "darkhotel"
        with tempfile.TemporaryDirectory() as directory:
            profiles_root = Path(directory) / "profiles"
            actor_dir = profiles_root / "darkhotel"
            actor_dir.mkdir(parents=True)
            for name in (
                "actor-profile.json",
                "iocs.json",
                "artifacts.csv",
                "ioc-sources.json",
                "daily-observations.json",
            ):
                shutil.copy2(source_dir / name, actor_dir / name)
            stable_id = "activity--darkhotel-kctv-lure-2026"
            legacy_id = "activity--daily-fbc4f59c4a844e18e5ab"
            # Reconstruct the pre-migration canonical state while leaving the
            # reviewed override in the separate queue/ledger input.
            for name in (
                "actor-profile.json",
                "iocs.json",
                "artifacts.csv",
                "ioc-sources.json",
            ):
                path = actor_dir / name
                path.write_text(
                    path.read_text(encoding="utf-8").replace(
                        stable_id, legacy_id
                    ),
                    encoding="utf-8",
                )
            queue = json.loads(
                (actor_dir / "daily-observations.json").read_text(
                    encoding="utf-8"
                )
            )
            queue["source"] = {
                "repository": "proshiba/tech-memo",
                "commit": queue["records"][0]["source_commit"],
            }
            queue_path = Path(directory) / "queue.json"
            queue_path.write_text(
                json.dumps(queue, ensure_ascii=False), encoding="utf-8"
            )
            argv = [
                "apply_review_queue.py",
                str(queue_path),
                "--profiles-root",
                str(profiles_root),
                "--actor",
                "darkhotel",
                "--rebuild-daily",
                "--apply",
                "--no-render",
            ]
            outputs: list[dict] = []
            for _ in range(2):
                output = io.StringIO()
                with mock.patch.object(sys, "argv", argv), mock.patch(
                    "sys.stdout", output
                ):
                    self.assertEqual(apply_review_queue.main(), 0)
                outputs.append(json.loads(output.getvalue()))

            profile_data = json.loads(
                (actor_dir / "actor-profile.json").read_text(encoding="utf-8")
            )
            serialized = "\n".join(
                (actor_dir / name).read_text(encoding="utf-8")
                for name in (
                    "actor-profile.json",
                    "iocs.json",
                    "artifacts.csv",
                    "ioc-sources.json",
                )
            )

        self.assertTrue(
            any(outputs[0]["actors"]["darkhotel"]["written"].values())
        )
        self.assertFalse(
            any(outputs[1]["actors"]["darkhotel"]["written"].values())
        )
        self.assertEqual(
            sum(
                activity.get("activity_id")
                == stable_id
                for activity in profile_data["activities"]
            ),
            1,
        )
        self.assertNotIn(legacy_id, serialized)

    def test_auxiliary_ioc_source_keeps_curated_publication_metadata(self) -> None:
        curated_date = {
            "value": "2026-08-12T00:00:00Z",
            "precision": "day",
            "status": "known",
            "basis": "source-publication",
        }
        dataset = {"sources": []}
        record = {
            "activity": {
                "activity_reference": "https://vendor.example/primary",
                "news_date": "2026-08-15",
            }
        }
        source = {
            "url": "https://vendor.example/ioc-appendix",
            "source_type": "ioc-reference",
        }

        source_id = add_dataset_source(
            dataset,
            record,
            source,
            preferred_sources=[
                {
                    "source_id": "source--curated-ioc-appendix",
                    "path": source["url"],
                    "published_at": curated_date,
                }
            ],
        )

        self.assertEqual(source_id, "source--curated-ioc-appendix")
        self.assertEqual(dataset["sources"][0]["published_at"], curated_date)

    def test_artifact_source_identity_change_replaces_legacy_observation(self) -> None:
        class Common:
            @staticmethod
            def normalize_observable(_kind: str, value: str) -> str:
                return value.casefold()

            @staticmethod
            def stable_id(kind: str, *parts: object) -> str:
                return f"{kind}--" + "|".join(str(item) for item in parts)

            @staticmethod
            def json_array_cell(value: object) -> str:
                return json.dumps(value, ensure_ascii=False)

        url = "https://vendor.example/report"
        record = {
            "record_id": "daily-record--example",
            "actor": {"slug": "example"},
            "activity": {
                "title": "Example report",
                "news_path": "daily-news/news/20260815.md",
                "news_date": "2026-08-15",
                "activity_reference": url,
                "primary_url": url,
            },
            "reported_at": {
                "value": "2026-08-12T00:00:00Z",
                "precision": "day",
                "status": "known",
                "basis": "source-publication",
            },
            "confidence": "high",
            "artifacts": [
                {
                    "artifact_type": "file-name",
                    "value": "sample.exe",
                    "review_status": "approved",
                }
            ],
        }
        queue = {"source": {"repository": "owner/repo", "commit": "abc"}}
        legacy = {
            "observation_id": "observation--legacy",
            "artifact_type": "file-name",
            "normalized_value": "sample.exe",
            "source_id": source_id_for_value(url),
            "source_path": url,
            "extraction_method": "tech-memo-reviewed-artifact",
            "analyst_notes": "daily record: daily-record--example",
            "campaign_refs": json.dumps(["activity--historical"]),
            "malware_refs": json.dumps(["malware--historical"]),
            "infrastructure_refs": "[]",
            "roles": json.dumps(["payload"]),
            "confidence": "medium",
            "context_excerpt": "historical context",
        }

        current = {
            **legacy,
            "observation_id": (
                "observation--actor--example|file-name|sample.exe|"
                "source--curated|daily-record--example"
            ),
            "source_id": "source--curated",
        }
        rows = merge_artifacts(
            [legacy, {**legacy, "observation_id": "observation--legacy-duplicate"}, current],
            record,
            queue,
            "actor--example",
            Common(),
            source_id="source--curated",
        )

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["source_id"], "source--curated")
        self.assertNotEqual(rows[0]["observation_id"], "observation--legacy")
        self.assertIn(
            "activity--historical", json.loads(rows[0]["campaign_refs"])
        )
        self.assertIn(
            "malware--historical", json.loads(rows[0]["malware_refs"])
        )
        self.assertIn("historical context", rows[0]["context_excerpt"])

    def test_known_curated_source_date_is_not_overwritten(self) -> None:
        curated_date = {
            "value": "2026-08-11T00:00:00Z",
            "precision": "day",
            "status": "known",
            "basis": "source-publication",
        }
        curated = {
            "source_id": "source--curated-report",
            "published_at": curated_date,
        }
        reviewed = {
            "source_id": "source--daily-example",
            "published_at": {
                "value": "2026-08-12T00:00:00Z",
                "precision": "day",
                "status": "known",
                "basis": "source-publication",
            },
        }

        self.assertEqual(
            merge_materialized_source(curated, reviewed)["published_at"],
            curated_date,
        )

    def test_collection_date_does_not_fill_unknown_curated_publication(self) -> None:
        curated = {
            "source_id": "source--curated-report",
            "published_at": dict(UNKNOWN_POINT),
        }
        collection_dated = {
            "source_id": "source--daily-example",
            "published_at": {
                "value": "2026-08-15T00:00:00Z",
                "precision": "day",
                "status": "known",
                "basis": "daily-news-file-date",
            },
        }

        self.assertEqual(
            merge_materialized_source(curated, collection_dated)["published_at"],
            UNKNOWN_POINT,
        )

    def test_reviewed_reported_at_rejects_non_rfc3339_and_wrong_basis(self) -> None:
        invalid_value = {
            "value": "2026-08-12",
            "precision": "day",
            "status": "known",
            "basis": "source-publication",
        }
        invalid_basis = {
            "value": "2026-08-12T00:00:00Z",
            "precision": "day",
            "status": "known",
            "basis": "daily-news-file-date",
        }

        self.assertIn("RFC 3339", reviewed_reported_at_issue(invalid_value))
        self.assertIn("source-publication", reviewed_reported_at_issue(invalid_basis))
        self.assertIsNone(reviewed_reported_at_issue(dict(UNKNOWN_POINT)))

    def test_reviewed_reported_at_precision_requires_normalized_value(self) -> None:
        cases = (
            ("year", "2026-12-31T00:00:00Z", "January 1"),
            ("month", "2026-08-31T00:00:00Z", "day 1"),
            ("day", "2026-08-12T12:00:00Z", "00:00:00Z"),
        )
        for precision, value, expected in cases:
            with self.subTest(precision=precision, value=value):
                issue = reviewed_reported_at_issue(
                    {
                        "value": value,
                        "precision": precision,
                        "status": "known",
                        "basis": "source-publication",
                    }
                )
                self.assertIn(expected, issue or "")

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

    def test_reviewed_source_publication_overrides_collection_report_date(self) -> None:
        record = {
            "record_id": "daily-record--example",
            "actor": {"slug": "darkhotel"},
            "activity": {
                "title": "Darkhotel activity",
                "summary": "Darkhotel conducted an attack.",
                "news_date": "2026-08-15",
                "activity_reference": "https://example.test/report",
            },
            "reported_at": {
                "value": "2026-08-12T00:00:00Z",
                "precision": "day",
                "status": "known",
                "basis": "source-publication",
            },
            "confidence": "high",
            "iocs": [],
            "activity_claim": {"assessment": "strong-subject"},
        }
        profile_data = {
            "actor": {"canonical_name": "Darkhotel"},
            "capabilities": {"malware": [], "infrastructure": []},
            "targets": {"countries": [], "regions": [], "sectors": [], "roles": []},
        }

        self.assertEqual(activity_reported_at(record), record["reported_at"])
        activity = activity_entry(record, ["source--primary"], profile_data)
        self.assertEqual(activity["reported_at"], record["reported_at"])
        self.assertIn("一次資料公開日", activity["analyst_notes"])

        source = {
            "url": "https://example.test/report",
            "source_path": "daily-news/news/20260815.md",
            "source_type": "primary-report",
        }
        queue = {"source": {"repository": "owner/repo", "commit": "abc"}}
        materialized_source = profile_source(record, source, queue)
        self.assertEqual(materialized_source["published_at"], record["reported_at"])

    def test_curated_source_publication_overrides_collection_report_date(self) -> None:
        record = {
            "record_id": "daily-record--example",
            "actor": {"slug": "example"},
            "activity": {
                "title": "Example activity",
                "summary": "Example Actor conducted an attack.",
                "news_date": "2026-08-15",
                "news_path": "daily-news/news/20260815.md",
                "activity_reference": "https://example.test/report",
            },
            "confidence": "high",
            "iocs": [],
            "activity_claim": {"assessment": "strong-subject"},
        }
        curated_date = {
            "value": "2026-08-12T00:00:00Z",
            "precision": "day",
            "status": "known",
            "basis": "source-publication",
        }
        sources = [
            {
                "source_id": "source--curated-report",
                "path": "https://example.test/report",
                "published_at": curated_date,
            }
        ]
        profile_data = {
            "actor": {"canonical_name": "Example Actor"},
            "sources": sources,
            "capabilities": {"malware": [], "infrastructure": []},
            "targets": {"countries": [], "regions": [], "sectors": [], "roles": []},
        }

        self.assertEqual(activity_reported_at(record, sources), curated_date)
        activity = activity_entry(record, ["source--curated-report"], profile_data)
        self.assertEqual(activity["reported_at"], curated_date)
        self.assertIn("一次資料公開日", activity["analyst_notes"])

    def test_reviewed_and_curated_publication_conflict_is_rejected(self) -> None:
        record = {
            "actor": {"slug": "example"},
            "activity": {
                "title": "Example",
                "news_date": "2026-08-15",
                "activity_reference": "https://example.test/report",
            },
            "reported_at": {
                "value": "2026-08-12T00:00:00Z",
                "precision": "day",
                "status": "known",
                "basis": "source-publication",
            },
        }
        sources = [
            {
                "source_id": "source--curated-report",
                "path": "https://example.test/report",
                "published_at": {
                    "value": "2026-08-11T00:00:00Z",
                    "precision": "day",
                    "status": "known",
                    "basis": "source-publication",
                },
            }
        ]

        with self.assertRaisesRegex(ValueError, "conflicts"):
            activity_reported_at(record, sources)

    def test_reviewed_publication_replaces_daily_collection_date_without_conflict(self) -> None:
        record = {
            "actor": {"slug": "example"},
            "activity": {
                "title": "Example",
                "news_date": "2026-08-15",
                "activity_reference": "https://example.test/report",
            },
            "reported_at": {
                "value": "2026-08-12T00:00:00Z",
                "precision": "day",
                "status": "known",
                "basis": "source-publication",
            },
        }
        existing_daily_source = [
            {
                "source_id": source_id_for_value("https://example.test/report"),
                "path": "https://example.test/report",
                "published_at": {
                    "value": "2026-08-15T00:00:00Z",
                    "precision": "day",
                    "status": "known",
                    "basis": "daily-news-file-date",
                },
            }
        ]

        self.assertEqual(
            activity_reported_at(record, existing_daily_source),
            record["reported_at"],
        )

    def test_unknown_reviewed_publication_preserves_known_collection_date(self) -> None:
        record = {
            "record_id": "daily-record--unknown-publication",
            "actor": {"slug": "darkhotel"},
            "activity": {
                "title": "Darkhotel activity",
                "summary": "Darkhotel conducted an attack.",
                "news_date": "2026-08-15",
                "activity_reference": "https://example.test/report",
            },
            "reported_at": {
                "value": None,
                "precision": "unknown",
                "status": "unknown",
                "basis": "not-stated",
            },
            "confidence": "high",
            "iocs": [],
            "activity_claim": {"assessment": "strong-subject"},
        }
        profile_data = {
            "actor": {"canonical_name": "Darkhotel"},
            "capabilities": {"malware": [], "infrastructure": []},
            "targets": {"countries": [], "regions": [], "sectors": [], "roles": []},
        }

        expected = {
            "value": "2026-08-15T00:00:00Z",
            "precision": "day",
            "status": "known",
            "basis": "daily-news-file-date",
        }
        self.assertEqual(activity_reported_at(record), expected)
        activity = activity_entry(record, ["source--primary"], profile_data)
        self.assertEqual(activity["reported_at"], expected)
        self.assertIn("tech-memo日次ファイルの日付", activity["analyst_notes"])

        source = {
            "url": "https://example.test/report",
            "source_path": "daily-news/news/20260815.md",
            "source_type": "primary-report",
        }
        queue = {"source": {"repository": "owner/repo", "commit": "abc"}}
        self.assertEqual(
            profile_source(record, source, queue)["published_at"],
            expected,
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


class CurationMergeResolutionTests(unittest.TestCase):
    """entity境界curationで統合された旧canonical名の照合保証。

    実データに対する不変条件テスト。actor-census-curation.jsonのmerge判断で
    deprecated化した旧canonical名は、統合先のactive profileへ一意に解決しなければ
    ならない（AGENT.md アクター照合）。alias再検証やcensus再materializeで統合先の
    aliasが失われると、日次の検知がtombstone名で取りこぼすため、ここで検出する。
    """

    REPO_ROOT = HERE.parent

    def test_merged_tombstone_names_resolve_to_target_slug(self) -> None:
        curation_path = (
            self.REPO_ROOT / "actor_profile" / "actor-census-curation.json"
        )
        profiles_root = self.REPO_ROOT / "profiles"
        if not curation_path.exists() or not profiles_root.is_dir():
            self.skipTest("repository data is not available")
        with curation_path.open(encoding="utf-8") as handle:
            curation = json.load(handle)
        with (HERE / "config.json").open(encoding="utf-8") as handle:
            config = json.load(handle)
        registry = ActorRegistry(profiles_root, config)
        checked = 0
        for rule in curation.get("identities", {}).values():
            if not isinstance(rule, dict) or rule.get("action") != "merge":
                continue
            source_slug = rule.get("source_slug")
            target_slug = rule.get("target_slug")
            if not source_slug or not target_slug:
                continue  # tombstoneを持たないcensus内部のmerge
            tombstone_path = (
                profiles_root / source_slug / "actor-profile.json"
            )
            if not tombstone_path.exists():
                continue
            with tombstone_path.open(encoding="utf-8") as handle:
                tombstone = json.load(handle)
            self.assertEqual(
                tombstone.get("status"),
                "deprecated",
                f"merge元 {source_slug} はtombstoneであるべき",
            )
            name = (
                tombstone.get("name")
                or (tombstone.get("actor") or {}).get("canonical_name")
                or ""
            )
            matches = registry.exact(name, "ioc-actor-field")
            self.assertEqual(
                sorted({match.slug for match in matches}),
                [target_slug],
                f"旧canonical名 {name!r} は {target_slug} へ一意に解決すべき",
            )
            checked += 1
        self.assertGreater(checked, 0, "merge判断が1件も検査されていない")


class DailyCheckTests(unittest.TestCase):
    """日次チェックの抽出ロジック（daily_check.py）。"""

    def test_deprecated_profiles_are_not_recent_actors(self) -> None:
        """curationで統合済みのtombstoneは直近活動アクターに数えない。"""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for slug, status in (("active-actor", "draft"), ("dead-actor", "deprecated")):
                (root / slug).mkdir()
                (root / slug / "actor-profile.json").write_text(
                    json.dumps({
                        "name": slug,
                        "status": status,
                        "actor": {"last_seen": known_point("2099-01-01T00:00:00Z")},
                        "activities": [],
                    }),
                    encoding="utf-8",
                )
            with mock.patch.object(daily_check, "PROFILES_DIR", root):
                rows = daily_check.collect_recent_actors(365)
        self.assertEqual([row["slug"] for row in rows], ["active-actor"])

    def test_report_date_is_not_used_when_period_is_unknown(self) -> None:
        """資料公開日だけでは攻撃者を直近活動へ昇格させない。"""
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
        self.assertEqual(latest_activity(profile), (None, ""))

    def test_new_report_does_not_outrank_older_activity_period(self) -> None:
        """古い活動の新しい起訴記事を新規攻撃として扱わない。"""
        profile = {
            "activities": [
                {
                    "first_observed": known_point("2013-01-01T00:00:00Z"),
                    "last_observed": known_point("2017-12-01T00:00:00Z"),
                    "reported_at": known_point("2026-08-18T00:00:00Z"),
                }
            ],
            "actor": {"last_seen": UNKNOWN_POINT},
        }
        point, basis = latest_activity(profile)
        self.assertEqual(point.date().isoformat(), "2017-12-01")
        self.assertEqual(basis, "activity.last_observed")

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

        curated = [
            {
                "source_id": "source--curated-ioc-report",
                "path": "https://x.example/status/1",
            }
        ]
        self.assertIn(
            "source--curated-ioc-report",
            validate_daily.ioc_bearing_source_ids(record, self.QUEUE, curated),
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


class ActivityOverrideValidationTests(unittest.TestCase):
    @staticmethod
    def _record(reference: str, record_id: str) -> dict:
        return {
            "record_id": record_id,
            "review_status": "approved",
            "actor": {"slug": "darkhotel", "scope": "exact"},
            "activity": {
                "title": "Reviewed activity",
                "news_date": "2026-08-12",
                "news_path": "daily-news/news/20260812.md",
                "primary_url": reference,
                "activity_reference": reference,
            },
            "activity_id_override": "activity--darkhotel-kctv-lure-2026",
            "capability_decisions": [],
            "iocs": [],
            "artifacts": [],
        }

    @staticmethod
    def _run_validator(queue_path: Path, profiles_root: Path, *extra: str) -> dict:
        argv = [
            "validate_daily.py",
            str(queue_path),
            "--profiles-root",
            str(profiles_root),
            *extra,
        ]
        output = io.StringIO()
        with mock.patch.object(sys, "argv", argv), mock.patch(
            "sys.stdout", output
        ):
            validate_daily.main()
        return json.loads(output.getvalue())

    def test_validator_rejects_two_generated_activities_for_one_override(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            profiles_root = root / "profiles"
            actor_dir = profiles_root / "darkhotel"
            actor_dir.mkdir(parents=True)
            (actor_dir / "actor-profile.json").write_text(
                '{"sources": []}', encoding="utf-8"
            )
            queue_path = root / "queue.json"
            queue_path.write_text(
                json.dumps(
                    {
                        "schema_version": "2.0.0",
                        "records": [
                            self._record("https://example.test/one", "record--one"),
                            self._record("https://example.test/two", "record--two"),
                        ],
                    }
                ),
                encoding="utf-8",
            )

            result = self._run_validator(queue_path, profiles_root)

        self.assertFalse(result["valid"])
        self.assertIn(
            "activity-id-collision",
            {item["code"] for item in result["issues"]},
        )

    def test_check_applied_rejects_stale_generated_activity_reference(self) -> None:
        record = self._record(
            "https://example.test/report", "daily-record--example"
        )
        old_id = activity_id_for({
            key: value
            for key, value in record.items()
            if key != "activity_id_override"
        })
        stable_id = record["activity_id_override"]
        source_id = source_id_for_value(record["activity"]["primary_url"])
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            profiles_root = root / "profiles"
            actor_dir = profiles_root / "darkhotel"
            actor_dir.mkdir(parents=True)
            (actor_dir / "actor-profile.json").write_text(
                json.dumps(
                    {
                        "sources": [
                            {
                                "source_id": source_id,
                                "path": record["activity"]["primary_url"],
                            }
                        ],
                        "activities": [{"activity_id": stable_id}],
                    }
                ),
                encoding="utf-8",
            )
            (actor_dir / "iocs.json").write_text(
                json.dumps(
                    {
                        "sources": [],
                        "indicators": [
                            {
                                "campaign_refs": [old_id],
                                "observations": [],
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )
            (actor_dir / "artifacts.csv").write_text(
                "campaign_refs\n[]\n", encoding="utf-8"
            )
            (actor_dir / "daily-observations.json").write_text(
                json.dumps({"records": [record]}), encoding="utf-8"
            )
            queue_path = root / "queue.json"
            queue_path.write_text(
                json.dumps(
                    {
                        "schema_version": "2.0.0",
                        "source": {"repository": "owner/repo", "commit": "abc"},
                        "records": [record],
                    }
                ),
                encoding="utf-8",
            )

            result = self._run_validator(
                queue_path, profiles_root, "--check-applied"
            )

        self.assertFalse(result["valid"])
        self.assertIn(
            "stale-activity-id", {item["code"] for item in result["issues"]}
        )


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

    def test_reviewed_reported_at_is_copied_to_record(self) -> None:
        record = self._record()
        decisions = self._decisions()
        reported_at = {
            "value": "2026-08-12T00:00:00Z",
            "precision": "day",
            "status": "known",
            "basis": "source-publication",
        }
        decisions["unc1549|https://example.test/report"]["reported_at"] = reported_at

        apply_decision(record, decisions, report_unmatched=False)

        self.assertEqual(record["reported_at"], reported_at)

    def test_valid_activity_id_override_is_copied_to_record(self) -> None:
        record = self._record()
        decisions = self._decisions()
        expected = "activity--unc1549-reviewed-operation-2026"
        decisions["unc1549|https://example.test/report"]["activity_id_override"] = (
            expected
        )

        apply_decision(record, decisions, report_unmatched=False)

        self.assertEqual(record["activity_id_override"], expected)
        self.assertNotIn("decision_issues", record)

    def test_invalid_activity_id_override_is_not_copied_to_record(self) -> None:
        for invalid in (
            "activity--daily-example",
            "activity--other-reviewed-operation-2026",
        ):
            with self.subTest(invalid=invalid):
                record = self._record()
                decisions = self._decisions()
                decisions["unc1549|https://example.test/report"][
                    "activity_id_override"
                ] = invalid

                apply_decision(record, decisions, report_unmatched=False)

                self.assertNotIn("activity_id_override", record)
                self.assertTrue(
                    any(
                        "activity_id_overrideが不正" in item
                        for item in record["decision_issues"]
                    )
                )

    def test_invalid_reviewed_reported_at_is_rejected_before_materialization(self) -> None:
        record = self._record()
        decisions = self._decisions()
        decisions["unc1549|https://example.test/report"]["reported_at"] = {
            "value": "2026-08-12",
            "precision": "invalid",
            "status": "known",
            "basis": "source-publication",
        }

        apply_decision(record, decisions, report_unmatched=False)

        self.assertNotIn("reported_at", record)
        self.assertTrue(
            any("reported_atが不正" in item for item in record["decision_issues"])
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
