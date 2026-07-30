#!/usr/bin/env python3
"""Regression tests for observable classification and normalization."""

from __future__ import annotations

import sys
import unittest
import json
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from common import normalize_observable, normalize_time, refang  # noqa: E402
from ingest_observables import (  # noqa: E402
    classified_record_values,
    extract_artifacts,
    extract_iocs,
)


class ObservableBoundaryTests(unittest.TestCase):
    def test_ioc_types_are_kept_out_of_artifacts(self) -> None:
        # 192.0.2.0/24 などのドキュメント用レンジは伏字であって指標ではないため、
        # ここでは実際に到達し得るアドレスを使う。
        text = (
            "IOC: hxxps://c2[.]evil-actor.net/path, 45.61.136.56, "
            "44d88612fea8a8f36de82e1278abb02f"
        )
        iocs = extract_iocs(
            text, allow_plain_domains=True, explicit_structured=False
        )
        self.assertIn(("ipv4", "45.61.136.56", "confirmed"), iocs)
        self.assertTrue(any(kind == "url" for kind, _, _ in iocs))
        self.assertTrue(any(kind == "md5" for kind, _, _ in iocs))
        self.assertFalse(extract_artifacts(text, explicit_structured=False))

    def test_non_ioc_artifacts_are_classified(self) -> None:
        text = (
            r"powershell.exe -enc AAA; C:\ProgramData\stage.dll; "
            r"HKCU\SOFTWARE\Example\Run"
        )
        kinds = {
            kind for kind, _, _ in extract_artifacts(text, explicit_structured=True)
        }
        self.assertIn("command", kinds)
        self.assertIn("file-path", kinds)
        self.assertIn("registry-key", kinds)

    def test_explicit_artifact_type_prevents_uuid_hash_misclassification(self) -> None:
        value = "A8215357-F99A-44FE-BC65-D8F0434B0C03"
        record = {
            "text": f"artifact\t{value}\tmutex",
            "location": {"row": 2},
            "fields": {
                "type": "artifact",
                "value": value,
                "artifact_type": "mutex",
            },
            "method": "csv-row",
        }
        metadata = {
            "field_map": {
                "type": "type",
                "value": "value",
                "artifact_type": "artifact_type",
            }
        }
        iocs, artifacts = classified_record_values(record, metadata)
        self.assertEqual(iocs, [])
        self.assertEqual(artifacts, [("mutex", value, "confirmed")])

    def test_file_names_are_not_domains(self) -> None:
        values = extract_iocs(
            "IOC table: loader.exe report.pdf c2.example-actor.org",
            allow_plain_domains=True,
            explicit_structured=False,
        )
        domains = {normalize_observable(kind, value) for kind, value, _ in values}
        self.assertEqual(domains, {"c2.example-actor.org"})

    def test_non_tld_file_names_are_not_domains(self) -> None:
        """実在しないTLDを持つ値はファイル名や文の断片であり domain にしない。"""
        values = extract_iocs(
            "IOC: files readme.txt config.json index.html dbconn.asp "
            "safe.headquartered plus c2.example-actor.org",
            allow_plain_domains=True,
            explicit_structured=False,
        )
        domains = {value for kind, value, _ in values if kind == "domain"}
        self.assertEqual(domains, {"c2.example-actor.org"})

    def test_com_domains_are_not_rejected_as_executables(self) -> None:
        """.comはCOM実行ファイルの拡張子でもあるが、TLDとして実在するため落とさない。"""
        values = extract_iocs(
            "IOC: c2 is malicious-c2.com",
            allow_plain_domains=True,
            explicit_structured=False,
        )
        domains = {value for kind, value, _ in values if kind == "domain"}
        self.assertIn("malicious-c2.com", domains)

    def test_special_use_tlds_are_kept(self) -> None:
        """.onion は委任TLDではないが指標として正当。"""
        values = extract_iocs(
            "IOC: hidden service at fckilfkscwusoopguhi7i6yg3l6tknaz7lrumvlhg5mvtxzxbbxlimid.onion",
            allow_plain_domains=True,
            explicit_structured=False,
        )
        domains = {value for kind, value, _ in values if kind == "domain"}
        self.assertEqual(len(domains), 1)
        self.assertTrue(next(iter(domains)).endswith(".onion"))

    def test_truncated_url_hosts_are_dropped(self) -> None:
        """https://www/ のように抽出途中で切れたURLはIOCにしない。"""
        values = extract_iocs(
            "IOC: see https://www/ and https://unit42/ but c2 was https://evil-c2.net/gate",
            allow_plain_domains=True,
            explicit_structured=False,
        )
        urls = {value for kind, value, _ in values if kind == "url"}
        self.assertEqual(urls, {"https://evil-c2.net/gate"})


class ReferenceHostTests(unittest.TestCase):
    """出典レポート自身の参考リンクを IOC として取り込まないこと。"""

    def test_citation_urls_are_not_iocs(self) -> None:
        text = (
            "IOC report. See https://securelist.com/some-analysis/12345/ and "
            "https://www.microsoft.com/security/blog/post for background. "
            "The C2 was https://evil-c2.net/gate.php"
        )
        urls = {
            value for kind, value, _ in
            extract_iocs(text, allow_plain_domains=True, explicit_structured=False)
            if kind == "url"
        }
        self.assertEqual(urls, {"https://evil-c2.net/gate.php"})

    def test_citation_subdomains_are_not_iocs(self) -> None:
        text = "IOC: https://blog.securelist.com/x and https://unit42.paloaltonetworks.com/y"
        urls = [
            value for kind, value, _ in
            extract_iocs(text, allow_plain_domains=True, explicit_structured=False)
            if kind == "url"
        ]
        self.assertEqual(urls, [])

    def test_bare_reference_domains_are_not_iocs(self) -> None:
        text = "IOC list: securelist.com attack.mitre.org bad-domain.net"
        domains = {
            value for kind, value, _ in
            extract_iocs(text, allow_plain_domains=True, explicit_structured=False)
            if kind == "domain"
        }
        self.assertEqual(domains, {"bad-domain.net"})

    def test_defanged_reference_host_is_kept(self) -> None:
        """難読化はアナリストが悪性と判断した印なので、参考ホストでも残す。"""
        text = "IOC: attacker abused hxxps://github[.]com/evil/repo for payload delivery"
        urls = [
            value for kind, value, _ in
            extract_iocs(text, allow_plain_domains=True, explicit_structured=False)
            if kind == "url"
        ]
        self.assertEqual(len(urls), 1)
        self.assertEqual(refang(urls[0]), "https://github.com/evil/repo")

    def test_vendor_contact_emails_are_not_iocs(self) -> None:
        text = "IOC: contact ti_support@qianxin.com or phish@bad-domain.net"
        emails = {
            value for kind, value, _ in
            extract_iocs(text, allow_plain_domains=True, explicit_structured=False)
            if kind == "email"
        }
        self.assertEqual(emails, {"phish@bad-domain.net"})

    def test_bare_public_suffix_is_not_a_domain(self) -> None:
        """co.kr や ddns.net 単体は指標にならないが、サブドメインは残す。"""
        text = "IOC list: co.kr ddns.net mfahost.ddns.net"
        domains = {
            value for kind, value, _ in
            extract_iocs(text, allow_plain_domains=True, explicit_structured=False)
            if kind == "domain"
        }
        self.assertEqual(domains, {"mfahost.ddns.net"})

    def test_non_routable_and_resolver_ips_are_not_iocs(self) -> None:
        text = "IOC: 127.0.0.1 10.1.2.3 192.168.1.1 8.8.8.8 203.0.113.10 45.61.136.56"
        ips = {
            value for kind, value, _ in
            extract_iocs(text, allow_plain_domains=True, explicit_structured=False)
            if kind == "ipv4"
        }
        self.assertEqual(ips, {"45.61.136.56"})

    def test_structured_source_reference_host_is_kept(self) -> None:
        """構造化IOC表からの取り込みはアナリストが指標として並べたものとみなす。"""
        text = "https://github.com/evil/repo"
        urls = [
            value for kind, value, _ in
            extract_iocs(text, allow_plain_domains=False, explicit_structured=True)
            if kind == "url"
        ]
        self.assertEqual(urls, ["https://github.com/evil/repo"])


class RefangTests(unittest.TestCase):
    def test_bracketed_scheme_leaves_no_residue(self) -> None:
        """[:] を先に解決しないと hxxp が残る(旧実装の不具合)。"""
        self.assertEqual(refang("hxxps[:]//evil-actor.net/a"), "https://evil-actor.net/a")
        self.assertEqual(refang("hxxp[:]//evil-actor.net"), "http://evil-actor.net")

    def test_scheme_is_case_insensitive(self) -> None:
        self.assertEqual(refang("HXXPS://Evil.example"), "https://Evil.example")
        self.assertEqual(refang("hXXps://Evil.example"), "https://Evil.example")

    def test_bracketed_at_and_dot_words(self) -> None:
        self.assertEqual(refang("user[@]evil.example"), "user@evil.example")
        self.assertEqual(refang("evil[dot]example"), "evil.example")
        self.assertEqual(refang("user[at]evil[dot]example"), "user@evil.example")


class TimeTests(unittest.TestCase):
    def test_invalid_calendar_date_becomes_unknown(self) -> None:
        point = normalize_time("2020-46", basis="same-record")
        self.assertEqual(point["status"], "unknown")
        self.assertIsNone(point["value"])
        self.assertEqual(point["basis"], "invalid-calendar-date:same-record")


class CollectionTests(unittest.TestCase):
    def test_catalog_and_generated_profiles_are_complete(self) -> None:
        root = Path(__file__).resolve().parents[2]
        catalog = json.loads(
            (root / "actor_profile" / "corpus-catalog.json").read_text(
                encoding="utf-8"
            )
        )
        slugs = [actor["slug"] for actor in catalog["actors"]]
        self.assertEqual(len(slugs), len(set(slugs)))
        for actor in catalog["actors"]:
            profile_path = root / "profiles" / actor["slug"] / "actor-profile.json"
            self.assertTrue(profile_path.is_file(), actor["slug"])
            profile = json.loads(profile_path.read_text(encoding="utf-8"))
            self.assertEqual(profile["profile_id"], f"actor--{actor['slug']}")
            self.assertFalse(
                any(
                    alias["name"].lower().startswith(("http://", "https://"))
                    for alias in profile["actor"]["aliases"]
                ),
                actor["slug"],
            )

    def test_collection_validation_has_no_errors(self) -> None:
        root = Path(__file__).resolve().parents[2]
        summary = json.loads(
            (root / "profiles" / "processing-summary.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(summary["actor_count"], len(summary["results"]))
        self.assertEqual(summary["error_count"], 0)
        self.assertTrue(all(item["status"] == "complete" for item in summary["results"]))


if __name__ == "__main__":
    unittest.main()
