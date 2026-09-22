#!/usr/bin/env python3
"""Regression tests for activity-scoped intelligence enrichment."""

from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path


FRAMEWORK = Path(__file__).resolve().parents[1]
SCRIPTS = FRAMEWORK / "scripts"
sys.path.insert(0, str(SCRIPTS))

from common import unknown_time  # noqa: E402
from enrich_activity_intelligence import (  # noqa: E402
    add_rule_ttps,
    add_targets,
    add_victim_case,
    add_mitre_group_targets,
    compile_rules,
    contains_evidence_reference,
    enrich_explicit_activity_period,
    ensure_campaign_software,
    link_explicit_activity_malware,
)
from migrate_activity_model import migrate  # noqa: E402


def load_fixture(name: str) -> dict:
    return json.loads((FRAMEWORK / name).read_text(encoding="utf-8"))


class ActivityIntelligenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rules = compile_rules(
            load_fixture("activity-observation-rules.json"),
            load_fixture("corpus-catalog.json"),
        )
        cls.attack = load_fixture("reference/attack-index.json")

    def profile(self, name: str, aliases: list[str] | None = None) -> dict:
        return {
            "name": name,
            "actor": {
                "canonical_name": name,
                "aliases": [{"name": item} for item in (aliases or [])],
            },
            "sources": [],
            "targets": {
                "countries": [],
                "regions": [],
                "sectors": [],
                "roles": [],
            },
            "capabilities": {
                "malware": [],
                "tools": [],
                "infrastructure": [],
            },
            "ttps": [],
            "victim_cases": [],
        }

    def activity(
        self,
        name: str,
        description: str,
        activity_type: str = "intrusion",
    ) -> dict:
        return {
            "activity_id": "activity--test",
            "name": name,
            "description": description,
            "activity_type": activity_type,
            "first_observed": unknown_time(),
            "last_observed": unknown_time(),
            "reported_at": {
                "value": "2026-07-29T00:00:00Z",
                "precision": "day",
                "status": "known",
                "basis": "report-publication-date",
            },
            "target_refs": [],
            "malware_refs": [],
            "ttp_refs": [],
            "victim_refs": [],
            "confidence": "medium",
            "evidence_refs": ["source--test"],
            "analyst_notes": "",
        }

    def test_explicit_existing_malware_is_linked_to_activity(self) -> None:
        profile = self.profile("Example Actor")
        profile["capabilities"]["malware"] = [
            {
                "id": "malware--example",
                "name": "ExampleLoader",
                "aliases": [],
            }
        ]
        activity = self.activity(
            "Example Actor campaign",
            "Example Actor deployed ExampleLoader to affected systems.",
        )
        added = link_explicit_activity_malware(profile, activity, self.rules)
        self.assertEqual(added, ["malware--example"])
        self.assertEqual(activity["malware_refs"], ["malware--example"])

    def test_mitre_campaign_tool_is_linked_as_tool_not_malware(self) -> None:
        profile = self.profile("Example Actor")
        activity = self.activity("Example campaign", "Uses a remote access tool.")
        attack = {
            "software": {
                "software--example-tool": {
                    "name": "Example Remote Tool",
                    "external_id": "S9999",
                    "software_type": "tool",
                    "platforms": ["Windows"],
                    "description": "A legitimate remote access tool.",
                }
            }
        }

        ensure_campaign_software(
            profile,
            activity,
            [{"target_ref": "software--example-tool"}],
            attack,
        )

        self.assertEqual(activity["malware_refs"], [])
        self.assertEqual(activity["tool_refs"], ["tool--mitre--s9999"])
        self.assertEqual(
            profile["capabilities"]["tools"][0]["id"],
            "tool--mitre--s9999",
        )

    def test_actor_software_name_collision_is_not_inferred(self) -> None:
        profile = self.profile("KONNI")
        profile["capabilities"]["malware"] = [
            {"id": "malware--konni", "name": "KONNI", "aliases": []}
        ]
        activity = self.activity(
            "KONNI campaign",
            "KONNI targeted researchers using a phishing document.",
        )
        added = link_explicit_activity_malware(profile, activity, self.rules)
        self.assertEqual(added, [])
        self.assertEqual(activity["malware_refs"], [])

    def test_multi_actor_article_does_not_mix_following_actor_behavior(self) -> None:
        profile = self.profile("Kimsuky", ["TA427"])
        activity = self.activity(
            "複数アクターの活動",
            (
                "Kimsuky: ClickFixで利用者にコマンドを実行させた。"
                " MuddyWater: PowerShellを使用してペイロードを展開した。"
            ),
        )

        add_rule_ttps(profile, activity, self.rules, self.attack)

        technique_ids = {item["technique_id"] for item in profile["ttps"]}
        self.assertIn("T1204.004", technique_ids)
        self.assertNotIn("T1059.001", technique_ids)

    def test_attribution_country_is_not_added_as_victim_country(self) -> None:
        profile = self.profile("APT41")
        activity = self.activity(
            "台湾の研究所への攻撃",
            "中国関連のAPT41が台湾政府関連の研究所を標的にして侵害した。",
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("台湾", countries)
        self.assertNotIn("中国", countries)

    def test_lure_theme_country_is_not_added_as_victim_country(self) -> None:
        profile = self.profile("Darkhotel", ["APT-C-06"])
        activity = self.activity(
            "APT-C-06（Darkhotel）の北朝鮮関連囮キャンペーン",
            (
                "APT-C-06（Darkhotel）は北朝鮮関連の囮文書を利用して、"
                "多数の利用者へフィッシング攻撃を実施した。"
            ),
            activity_type="phishing-campaign",
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertNotIn("北朝鮮", countries)

    def test_country_with_explicit_target_before_lure_is_preserved(self) -> None:
        profile = self.profile("Example Actor")
        activity = self.activity(
            "インド政府機関への攻撃",
            "攻撃者はインドの政府機関を狙う囮文書を送付した。",
            activity_type="phishing-campaign",
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("インド", countries)

    def test_country_with_recipient_scope_before_lure_is_preserved(self) -> None:
        for description in (
            "攻撃者はインド政府機関向けの囮文書を送付した。",
            "攻撃者はインドの政府機関向けに作成した囮文書を送付した。",
        ):
            with self.subTest(description=description):
                profile = self.profile("Example Actor")
                activity = self.activity("インド政府機関への攻撃", description)

                add_targets(profile, activity, self.rules)

                countries = {
                    item["name"] for item in profile["targets"]["countries"]
                }
                self.assertIn("インド", countries)

    def test_country_directly_targeted_before_lure_is_preserved(self) -> None:
        cases = (
            ("The actor targeted North Korea with a lure document.", "北朝鮮"),
            ("The actor attacked Japan using a decoy document.", "日本"),
        )
        for description, expected in cases:
            with self.subTest(description=description):
                profile = self.profile("Example Actor")
                activity = self.activity("Example attack", description)

                add_targets(profile, activity, self.rules)

                countries = {
                    item["name"] for item in profile["targets"]["countries"]
                }
                self.assertIn(expected, countries)

        profile = self.profile("Example Actor")
        activity = self.activity(
            "Example attack",
            "The actor targeted Japan using North Korea-themed lure documents.",
        )
        add_targets(profile, activity, self.rules)
        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("日本", countries)
        self.assertNotIn("北朝鮮", countries)

    def test_katakana_country_is_not_matched_inside_longer_country_name(self) -> None:
        profile = self.profile("Example Actor")
        activity = self.activity(
            "インドネシア政府機関への攻撃",
            "攻撃者はインドネシアの政府機関を標的にした。",
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertNotIn("インド", countries)

    def test_latin_country_terms_are_token_bounded(self) -> None:
        cases = (
            ("The actor targeted organizations in Indianapolis.", "インド"),
            ("The actor targeted AmericanExpress customers.", "米国"),
            ("The actor targeted a Germanium server.", "ドイツ"),
            ("The actor targeted RussianDoll users.", "ロシア"),
        )
        for description, unexpected in cases:
            with self.subTest(description=description):
                profile = self.profile("Example Actor")
                activity = self.activity("Example attack", description)

                add_targets(profile, activity, self.rules)

                countries = {
                    item["name"] for item in profile["targets"]["countries"]
                }
                self.assertNotIn(unexpected, countries)

    def test_latin_country_terms_are_case_insensitive(self) -> None:
        profile = self.profile("Example Actor")
        activity = self.activity(
            "Example attack",
            "The actor targeted government organizations in japan and germany.",
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("日本", countries)
        self.assertIn("ドイツ", countries)

    def test_us_abbreviation_before_target_noun_is_detected(self) -> None:
        profile = self.profile("Example Actor")
        activity = self.activity(
            "Example attack",
            "The actor targeted US government organizations.",
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("米国", countries)

    def test_product_origin_or_language_is_not_victim_geography(self) -> None:
        cases = (
            ("The actor attacked a Japanese-made software package.", "日本"),
            ("The actor compromised a German-built server.", "ドイツ"),
            ("攻撃者は日本語版ソフトウェアを侵害した。", "日本"),
            ("攻撃者は中国製ルータを侵害した。", "中国"),
        )
        for description, unexpected in cases:
            with self.subTest(description=description):
                profile = self.profile("Example Actor")
                activity = self.activity("Example attack", description)

                add_targets(profile, activity, self.rules)

                countries = {
                    item["name"] for item in profile["targets"]["countries"]
                }
                self.assertNotIn(unexpected, countries)

    def test_country_in_malware_name_is_not_victim_geography(self) -> None:
        profile = self.profile("APT41")
        activity = self.activity(
            "RevivalStone",
            (
                "中国系のAPT41が日本企業を標的にし、"
                "China ChopperとBehinderを展開した。"
            ),
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertEqual(countries, {"日本"})

    def test_country_is_kept_when_targeted_despite_malware_name(self) -> None:
        profile = self.profile("Example Actor")
        activity = self.activity(
            "Example attack",
            "攻撃者は中国の組織を標的にし、China Chopperを展開した。",
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("中国", countries)

    def test_japanese_sei_compounds_are_not_misread_as_product_origin(self) -> None:
        for description in (
            "攻撃者は中国製薬会社を標的にした。",
            "攻撃者は中国製造拠点を攻撃した。",
        ):
            with self.subTest(description=description):
                profile = self.profile("Example Actor")
                activity = self.activity("Example attack", description)

                add_targets(profile, activity, self.rules)

                countries = {
                    item["name"] for item in profile["targets"]["countries"]
                }
                self.assertIn("中国", countries)

    def test_infrastructure_location_is_not_victim_geography(self) -> None:
        cases = (
            (
                "Using a C2 server in Russia, the actor targeted Germany.",
                "ロシア",
                "ドイツ",
            ),
            (
                "The actor routed traffic through infrastructure in India to attack Japan.",
                "インド",
                "日本",
            ),
            (
                "攻撃者はロシアのC2サーバを利用して日本を攻撃した。",
                "ロシア",
                "日本",
            ),
            (
                "攻撃者は中国にC2サーバを設置し、日本を標的にした。",
                "中国",
                "日本",
            ),
            (
                "The actor attacked Germany using Russian C2 servers.",
                "ロシア",
                "ドイツ",
            ),
        )
        for description, infrastructure_country, victim_country in cases:
            with self.subTest(description=description):
                profile = self.profile("Example Actor")
                activity = self.activity("Example attack", description)

                add_targets(profile, activity, self.rules)

                countries = {
                    item["name"] for item in profile["targets"]["countries"]
                }
                self.assertNotIn(infrastructure_country, countries)
                self.assertIn(victim_country, countries)

    def test_country_of_explicit_victim_asset_is_preserved(self) -> None:
        cases = (
            ("The actor targeted servers in Germany.", "ドイツ"),
            (
                "The actor attacked critical infrastructure in Ukraine.",
                "ウクライナ",
            ),
            ("The actor compromised hosts in Japan.", "日本"),
            (
                "The actor targeted a C2 server in Germany used by the victim.",
                "ドイツ",
            ),
            (
                "The actor targeted cloud infrastructure in India.",
                "インド",
            ),
            (
                "Salt Typhoonは1,000台以上のネットワーク機器を標的とし、"
                "その半数以上が米国、南米、インドに所在。",
                "インド",
            ),
        )
        for description, expected in cases:
            with self.subTest(description=description):
                profile = self.profile("Example Actor")
                activity = self.activity("Example attack", description)

                add_targets(profile, activity, self.rules)

                countries = {
                    item["name"] for item in profile["targets"]["countries"]
                }
                self.assertIn(expected, countries)

    def test_actor_name_hotel_substring_is_not_a_sector_target(self) -> None:
        profile = self.profile("Darkhotel", ["APT-C-06"])
        activity = self.activity(
            "Darkhotel phishing activity",
            "Darkhotel conducted a phishing attack against numerous users.",
            activity_type="phishing-campaign",
        )

        add_targets(profile, activity, self.rules)

        sectors = {item["name"] for item in profile["targets"]["sectors"]}
        self.assertNotIn("小売・ホスピタリティ", sectors)

    def test_standalone_hotel_target_remains_a_sector_target(self) -> None:
        profile = self.profile("Example Actor")
        activity = self.activity(
            "Hotel phishing activity",
            "Example Actor targeted hotel operators with phishing emails.",
            activity_type="phishing-campaign",
        )

        add_targets(profile, activity, self.rules)

        sectors = {item["name"] for item in profile["targets"]["sectors"]}
        self.assertIn("小売・ホスピタリティ", sectors)

    def test_latin_sector_terms_are_token_bounded(self) -> None:
        cases = (
            ("The actor immediately attacked victims.", "メディア・報道"),
            ("The actor targeted Bankshot malware users.", "金融"),
            ("The actor targeted an embankment control system.", "金融"),
        )
        for description, unexpected in cases:
            with self.subTest(description=description):
                profile = self.profile("Example Actor")
                activity = self.activity("Example attack", description)

                add_targets(profile, activity, self.rules)

                sectors = {item["name"] for item in profile["targets"]["sectors"]}
                self.assertNotIn(unexpected, sectors)

    def test_latin_sector_terms_preserve_inflections_and_casefolding(self) -> None:
        profile = self.profile("Example Actor")
        activity = self.activity(
            "Example attack",
            "The actor targeted manufacturing and technology companies and media organizations.",
        )

        add_targets(profile, activity, self.rules)

        sectors = {item["name"] for item in profile["targets"]["sectors"]}
        self.assertIn("製造・産業", sectors)
        self.assertIn("IT・ソフトウェア", sectors)
        self.assertIn("メディア・報道", sectors)

    def test_possessive_country_actor_phrase_is_not_a_victim_country(self) -> None:
        profile = self.profile("Mustang Panda")
        activity = self.activity(
            "ASEANへの諜報活動",
            "中国のAPTグループMustang PandaがASEAN加盟国を標的にした。",
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertNotIn("中国", countries)

    def test_attribution_country_with_niyoru_phrase_is_not_a_victim_country(
        self,
    ) -> None:
        profile = self.profile("QTFY")
        activity = self.activity(
            "米司法省、中国によるハッキングに関する主張を訂正し、"
            "米政府機関は「被害者」ではなく「標的」だったと説明",
            "米司法省とFBIは、中国国家支援グループQTFYが運用したQScanと"
            "QTRouterのドメインを差し押さえ、米国の重要インフラが標的とされたと発表した。",
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("米国", countries)
        self.assertNotIn("中国", countries)

    def test_government_backing_phrase_is_not_a_country_or_sector_target(
        self,
    ) -> None:
        profile = self.profile("Volt Typhoon")
        activity = self.activity(
            "Volt Typhoonがボットネットを再構築",
            (
                "中国政府支援のこのハッカー集団はSOHOルーターを狙い、"
                "米国の通信事業者を標的にした。"
            ),
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        sectors = {item["name"] for item in profile["targets"]["sectors"]}
        self.assertIn("米国", countries)
        self.assertNotIn("中国", countries)
        self.assertIn("情報通信", sectors)
        self.assertNotIn("政府・行政", sectors)

    def test_english_government_backing_phrase_is_not_a_sector_target(
        self,
    ) -> None:
        profile = self.profile("Example Actor")
        activity = self.activity(
            "Campaign against telecom providers",
            (
                "Chinese government-backed hackers targeted telecommunications "
                "providers in the United States."
            ),
        )

        add_targets(profile, activity, self.rules)

        sectors = {item["name"] for item in profile["targets"]["sectors"]}
        self.assertIn("情報通信", sectors)
        self.assertNotIn("政府・行政", sectors)

    def test_backing_country_phrase_is_not_a_victim_country(self) -> None:
        """「Xを背景とするグループ」は支援国側の記述であり被害国ではない。

        2026-09-20の取込で、警察庁公表(WaterPlum)の活動記述から「北朝鮮」が
        標的国として構造化された実例に基づく回帰テスト。
        """
        profile = self.profile("Contagious Interview")
        activity = self.activity(
            "北朝鮮サイバー攻撃グループ「WaterPlum」によるIT技術者を標的とした"
            "サイバー攻撃並びに北朝鮮IT労働者の活動実態について",
            "北朝鮮を背景とするサイバー攻撃グループWaterPlumは、"
            "日本、米国及び欧州のIT技術者を標的として攻撃を行っている。",
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("米国", countries)
        self.assertNotIn("北朝鮮", countries)

    def test_geopolitical_pressure_source_is_not_a_victim_country(self) -> None:
        """「Xからの圧力」は地政学的な働きかけの主体であり被害国ではない。

        2026-09-20の取込で、ESETのFamousSparrow記事の要約から「米国」が
        標的国として構造化された実例に基づく回帰テスト。
        """
        profile = self.profile("FamousSparrow")
        activity = self.activity(
            "SparroWockに注意",
            "中国関連APTは台湾の政府機関を標的として侵害した。"
            "各国政府が米国からの圧力へどう対応するかを"
            "監視・予測する目的の諜報活動とみられる。",
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("台湾", countries)
        self.assertNotIn("米国", countries)

    def test_political_subject_matter_is_not_a_victim_country(self) -> None:
        profile = self.profile("Kimsuky")
        activity = self.activity(
            "韓国の学術機関への攻撃",
            (
                "北朝鮮のハッカーグループKimsukyが、韓国の学術機関を標的にした。"
                "北朝鮮の政治問題に焦点を当てた学術関係者が特に狙われた。"
            ),
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("韓国", countries)
        self.assertNotIn("北朝鮮", countries)

    def test_multiple_names_for_same_actor_do_not_truncate_activity_text(
        self,
    ) -> None:
        profile = self.profile("Mustang Panda", ["HoneyMyte"])
        activity = self.activity(
            "HoneyMyte activity",
            (
                "HoneyMyte (Mustang Panda) deployed CoolClient. "
                "The actor established persistence. "
                "It collected credentials. "
                "It concealed command traffic. "
                "Victims in Pakistan and Russia were confirmed."
            ),
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertEqual(countries, {"パキスタン", "ロシア"})

    def test_actor_name_after_target_clause_does_not_hide_victim_country(self) -> None:
        profile = self.profile("Konni")
        activity = self.activity(
            "Poseidon campaign",
            (
                "韓国組織を狙うKonni APTの作戦を確認した。"
                "攻撃者は北朝鮮人権団体への成りすましで信用を獲得した。"
            ),
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("韓国", countries)
        self.assertNotIn("北朝鮮", countries)

    def test_campaign_origin_and_related_country_are_not_victim_countries(
        self,
    ) -> None:
        profile = self.profile("Example Actor")
        activity = self.activity(
            "欧州外交組織への攻撃",
            (
                "北朝鮮の攻撃キャンペンが確認された。"
                "中国と関連するサイバー攻撃グループは、ドイツの外交組織を標的にした。"
            ),
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("ドイツ", countries)
        self.assertNotIn("北朝鮮", countries)
        self.assertNotIn("中国", countries)

    def test_geopolitical_deployment_and_request_are_not_victim_countries(
        self,
    ) -> None:
        profile = self.profile("Konni")
        activity = self.activity(
            "ウクライナ政府を狙う活動",
            (
                "Konniはウクライナ政府機関を標的にした。目的は北朝鮮軍の"
                "ウクライナ派遣に伴うリスクとロシアからの追加要請を分析することだった。"
            ),
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("ウクライナ", countries)
        self.assertNotIn("北朝鮮", countries)
        self.assertNotIn("ロシア", countries)

    def test_reviewed_activity_target_exclusions_override_text_matches(self) -> None:
        profile = self.profile("Example Actor")
        activity = self.activity(
            "複数業種への攻撃",
            "攻撃者は日本の防衛組織と米国政府機関を標的にした。",
        )
        rules = copy.deepcopy(self.rules)
        rules["_activity_target_exclusions"] = {
            activity["activity_id"]: {"日本", "防衛・軍事"}
        }

        add_targets(profile, activity, rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        sectors = {item["name"] for item in profile["targets"]["sectors"]}
        self.assertEqual(countries, {"米国"})
        self.assertIn("政府・行政", sectors)
        self.assertNotIn("防衛・軍事", sectors)

    def test_reviewed_actor_origin_exclusions_are_activity_scoped(self) -> None:
        expected = {
            "activity--daily-7dcf9cf6e2fe65afbc24": "中国",
            "activity--daily-989bc2c5989d5df2a48c": "中国",
            "activity--daily-99b5ac281926f2b2c7f5": "ロシア",
            "activity--daily-e6a1fb3331093f1f95ff": "中国",
            "activity--daily-2462ee9ecba7b88d13ba": "中国",
            "activity--daily-70455fdbf70de32136f4": "中国",
            "activity--daily-3cc292e429bde2aa787b": "ロシア",
            "activity--daily-c63f469830d482d2fcb5": "ロシア",
            "activity--daily-a5d93a68e43731ecdd21": "ロシア",
            "activity--daily-d19bcb2ad9591f6dacd1": "ロシア",
            "activity--daily-62cfd32e84dd1b1905b5": "ロシア",
        }
        exclusions = self.rules["_activity_target_exclusions"]
        for activity_id, target_name in expected.items():
            with self.subTest(activity_id=activity_id):
                self.assertIn(target_name, exclusions[activity_id])

        profile = self.profile("UNC5812")
        activity = self.activity(
            "ロシア、ウクライナ徴兵対象者にマルウェアで攻撃",
            "ロシアのUNC5812グループが、ウクライナ徴兵者を標的にした。",
        )
        activity["activity_id"] = "activity--daily-62cfd32e84dd1b1905b5"

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertEqual(countries, {"ウクライナ"})

    def test_victim_side_it_workers_keep_their_country(self) -> None:
        """「Xの IT労働者」は被害側であり、帰属文脈として除外しない。"""
        profile = self.profile("Contagious Interview")
        activity = self.activity(
            "IT労働者を狙う攻撃",
            "攻撃者は日本のIT労働者を標的として偽の求人を送付した。",
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("日本", countries)

    def test_country_possessive_victim_phrase_with_nerau_is_kept(self) -> None:
        profile = self.profile("UNC3753")
        activity = self.activity(
            "法律事務所への攻撃",
            "UNC3753は米国の法律事務所を偽ITサポート通話で積極的に狙っている。",
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("米国", countries)

    def test_country_sector_disruption_title_is_target_context(self) -> None:
        profile = self.profile("Example Actor")
        activity = self.activity(
            "攻撃者がウクライナの穀物セクターを妨害",
            "データワイパーによる破壊活動が確認された。",
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("ウクライナ", countries)

    def test_targeted_policy_professionals_keep_their_country(self) -> None:
        profile = self.profile("Mustang Panda")
        activity = self.activity(
            "政策関係者への攻撃",
            "Mustang Pandaは韓国・米国の政策／外交関係者を狙った。",
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertEqual(countries, {"韓国", "米国"})

    def test_social_engineering_is_not_manufacturing_sector(self) -> None:
        profile = self.profile("FIN6")
        activity = self.activity(
            "採用担当者への攻撃",
            (
                "FIN6 used social engineering against recruiters. "
                "攻撃者はソーシャルエンジニアリングで採用担当者を狙った。"
            ),
        )

        add_targets(profile, activity, self.rules)

        sectors = {item["name"] for item in profile["targets"]["sectors"]}
        self.assertNotIn("製造・産業", sectors)

    def test_nationality_of_perpetrators_is_not_a_victim_country(self) -> None:
        profile = self.profile("Silent Librarian")
        activity = self.activity(
            "米国、知的財産窃取に関与したイラン人ハッカーを起訴",
            (
                "米司法省は、Mabna Instituteに所属するとされるイラン人17人を、"
                "米国の大学から長年データを窃取したとして起訴した。"
            ),
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("米国", countries)
        self.assertNotIn("イラン", countries)

    def test_nationality_of_victims_is_still_a_victim_country(self) -> None:
        profile = self.profile("Kimsuky")
        activity = self.activity(
            "日本人利用者への攻撃",
            "Kimsukyは日本人を標的にしたフィッシングで日本の研究機関を侵害した。",
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("日本", countries)

    def test_every_country_in_target_list_is_added(self) -> None:
        profile = self.profile("Lazarus Group")
        activity = self.activity(
            "Operation Dream Job",
            (
                "Lazarus Group targeted the defense and aerospace sectors in "
                "the United States, Israel, Australia, Russia, and India."
            ),
        )

        add_targets(profile, activity, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertEqual(
            countries,
            {"米国", "イスラエル", "オーストラリア", "ロシア", "インド"},
        )

    def test_mitre_group_summary_adds_targets_but_not_attribution_country(self) -> None:
        profile = self.profile("Axiom", ["Group 72"])
        group = {
            "external_id": "G0001",
            "description": (
                "Axiom is a suspected Chinese cyber espionage group that has "
                "targeted the aerospace, defense, government, manufacturing, "
                "and media sectors in the United States."
            ),
        }

        count = add_mitre_group_targets(profile, group, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        sectors = {item["name"] for item in profile["targets"]["sectors"]}
        self.assertGreater(count, 0)
        self.assertIn("米国", countries)
        self.assertNotIn("中国", countries)
        self.assertIn("防衛・軍事", sectors)
        self.assertIn("政府・行政", sectors)
        self.assertIn("製造・産業", sectors)
        self.assertIn("メディア・報道", sectors)

    def test_mitre_adjectival_attribution_country_is_not_a_target(self) -> None:
        profile = self.profile("SideCopy")
        group = {
            "external_id": "G1008",
            "description": (
                "SideCopy is a Pakistani threat group that has primarily "
                "targeted Indian government personnel since at least 2019."
            ),
        }

        add_mitre_group_targets(profile, group, self.rules)

        countries = {item["name"] for item in profile["targets"]["countries"]}
        self.assertIn("インド", countries)
        self.assertNotIn("パキスタン", countries)

    def test_mitre_targeting_guards_exclude_non_victim_country_contexts(self) -> None:
        cases = (
            (
                "Example Group used C2 servers in Russia to target government "
                "organizations in Germany.",
                {"ドイツ"},
            ),
            (
                "Example Group used a Japanese-made tool to target companies "
                "in Germany.",
                {"ドイツ"},
            ),
            (
                "Example Group used North Korea-themed lure documents to target "
                "organizations in Japan.",
                {"日本"},
            ),
        )
        for description, expected in cases:
            with self.subTest(description=description):
                profile = self.profile("Example Group")
                group = {"external_id": "G9999", "description": description}

                add_mitre_group_targets(profile, group, self.rules)

                countries = {
                    item["name"] for item in profile["targets"]["countries"]
                }
                self.assertEqual(countries, expected)

    def test_existing_mitre_evidence_reference_is_detected(self) -> None:
        profile = self.profile("APT43")
        profile["relationships"] = [
            {"evidence_refs": ["source--mitre-attack-19-2"]}
        ]

        self.assertTrue(
            contains_evidence_reference(
                profile,
                "source--mitre-attack-19-2",
            )
        )

    def test_publication_date_is_not_used_as_observation_date(self) -> None:
        profile = self.profile("APT41")
        activity = self.activity(
            "期間不明の攻撃",
            "APT41が研究機関を標的にしたことをレポートが報告した。",
        )

        changed = enrich_explicit_activity_period(profile, activity, self.rules)

        self.assertFalse(changed)
        self.assertIsNone(activity["first_observed"]["value"])
        self.assertIsNone(activity["last_observed"]["value"])

    def test_explicit_activity_period_is_structured(self) -> None:
        profile = self.profile("APT41")
        activity = self.activity(
            "明示期間のある攻撃",
            "攻撃は2023年11月から2024年7月にかけて観測された。",
        )

        changed = enrich_explicit_activity_period(profile, activity, self.rules)

        self.assertTrue(changed)
        self.assertEqual(
            activity["first_observed"]["value"],
            "2023-11-01T00:00:00Z",
        )
        self.assertEqual(
            activity["last_observed"]["value"],
            "2024-07-01T00:00:00Z",
        )

    def test_prior_campaign_sentence_is_not_used_as_activity_period(self) -> None:
        profile = self.profile("UAC-0099")
        activity = self.activity(
            "UAC-0099、マルウェアにAI解析を妨害するプロンプトを埋め込み",
            (
                "UAC-0099は悪性VBSスクリプトのコメントへ安全上問題のある文章を"
                "埋め込み、LLMの安全機構を作動させて解析を拒否させた。"
                "UAC-0099は過去に交通・エネルギー分野を標的としており、"
                "2026年7月には偽Notepad++プラグインを用いて新型MATCHBOILを"
                "展開していた。"
            ),
        )

        changed = enrich_explicit_activity_period(profile, activity, self.rules)

        self.assertFalse(changed)
        self.assertIsNone(activity["first_observed"]["value"])
        self.assertIsNone(activity["last_observed"]["value"])

    def test_conventional_technique_wording_does_not_block_period(self) -> None:
        profile = self.profile("Kimsuky")
        activity = self.activity(
            "PowerShellを悪用する新手法",
            (
                "この手法は、2025年1月以降、限定的な攻撃で観測されており、"
                "Kimsukyが使う従来の手法から逸脱しています。"
            ),
        )

        changed = enrich_explicit_activity_period(profile, activity, self.rules)

        self.assertTrue(changed)
        self.assertEqual(
            activity["first_observed"]["value"],
            "2025-01-01T00:00:00Z",
        )

    def test_month_pair_activity_period_is_structured(self) -> None:
        profile = self.profile("Kimsuky")
        activity = self.activity(
            "Durianを使用した攻撃",
            "攻撃は2023年8月と11月に発生した。",
        )

        changed = enrich_explicit_activity_period(profile, activity, self.rules)

        self.assertTrue(changed)
        self.assertEqual(
            activity["first_observed"]["value"],
            "2023-08-01T00:00:00Z",
        )
        self.assertEqual(
            activity["last_observed"]["value"],
            "2023-11-01T00:00:00Z",
        )

    def test_single_observed_month_is_structured(self) -> None:
        profile = self.profile("Kimsuky")
        activity = self.activity(
            "DOCSWAPキャンペーン",
            "2025年9月に観測された攻撃でDOCSWAPを展開した。",
        )

        changed = enrich_explicit_activity_period(profile, activity, self.rules)

        self.assertTrue(changed)
        self.assertEqual(
            activity["first_observed"]["value"],
            "2025-09-01T00:00:00Z",
        )
        self.assertEqual(
            activity["last_observed"]["value"],
            "2025-09-01T00:00:00Z",
        )

    def test_half_year_activity_period_is_structured(self) -> None:
        profile = self.profile("Kimsuky")
        activity = self.activity(
            "上半期のキャンペーン",
            "2026年上半期に4件のスピアフィッシング攻撃を実行した。",
        )

        changed = enrich_explicit_activity_period(profile, activity, self.rules)

        self.assertTrue(changed)
        self.assertEqual(
            activity["first_observed"]["value"],
            "2026-01-01T00:00:00Z",
        )
        self.assertEqual(
            activity["last_observed"]["value"],
            "2026-06-01T00:00:00Z",
        )

    def test_denied_breach_claim_is_kept_as_disputed_victim_case(self) -> None:
        profile = self.profile("Akira")
        activity = self.activity(
            "Example Corp、データ侵害主張を否定",
            (
                "AkiraがExample Corpを侵害したと主張したが、"
                "Example Corpはデータ侵害主張を否定した。"
            ),
            activity_type="ransomware-extortion",
        )

        victim_id = add_victim_case(profile, activity, self.rules)

        self.assertIsNotNone(victim_id)
        self.assertEqual(profile["victim_cases"][0]["case_status"], "disputed")
        self.assertEqual(profile["victim_cases"][0]["victim_name"], "Example Corp")
        self.assertIn(victim_id, activity["victim_refs"])

    def test_publication_date_is_removed_from_observation_field(self) -> None:
        activity = self.activity(
            "旧形式の活動",
            "攻撃時期は資料に記載されていない。",
        )
        activity["last_observed"] = {
            "value": "2025-05-01T00:00:00Z",
            "precision": "month",
            "status": "known",
            "basis": "source-publication",
        }
        profile = {
            "schema_version": "1.4.0",
            "activities": [activity],
            "ttps": [],
            "victim_cases": [],
        }

        migrated, changed = migrate(profile)

        self.assertTrue(changed)
        self.assertIsNone(
            migrated["activities"][0]["last_observed"]["value"]
        )
        self.assertIn(
            "last_observed=2025-05-01T00:00:00Z",
            migrated["activities"][0]["analyst_notes"],
        )
        self.assertEqual(
            migrated["activities"][0]["reported_at"]["value"],
            "2026-07-29T00:00:00Z",
        )


if __name__ == "__main__":
    unittest.main()
