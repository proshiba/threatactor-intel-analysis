#!/usr/bin/env python3
"""Extract the published APT29 RDP campaign observables from saved Microsoft HTML."""

from __future__ import annotations

import argparse
import csv
import html
import re
from pathlib import Path


DOMAIN_RE = re.compile(
    r"\b(?:[a-z0-9-]+(?:\.|\[\.\]))+[a-z]{2,}\b",
    re.IGNORECASE,
)
LIST_ITEM_RE = re.compile(r"<li\b[^>]*>(.*?)</li>", re.IGNORECASE | re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>")


def plain_text(value: str) -> str:
    return " ".join(html.unescape(TAG_RE.sub(" ", value)).split())


def section(document: str, start_id: str, end_id: str) -> str:
    start = document.index(f'id="{start_id}"')
    end = document.index(f'id="{end_id}"', start)
    return document[start:end]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    document = args.html.read_text(encoding="utf-8", errors="replace")
    ioc_html = section(document, "indicators-of-compromise", "references")
    sender_html = section(ioc_html, "email-sender-domains", "rdp-file-names")
    filename_html = section(ioc_html, "rdp-file-names", "rdp-remote-computer-domains")
    remote_html = ioc_html[ioc_html.index('id="rdp-remote-computer-domains"') :]

    sender_domains = {
        item.replace("[.]", ".").lower() for item in DOMAIN_RE.findall(sender_html)
    }
    remote_domains = {
        item.replace("[.]", ".").lower() for item in DOMAIN_RE.findall(remote_html)
    }
    filenames = {
        plain_text(item).strip(" -*")
        for item in LIST_ITEM_RE.findall(filename_html)
        if plain_text(item).lower().endswith(".rdp")
    }

    rows: list[dict[str, str]] = []
    common = {
        "campaign_refs": "activity--apt29-rdp-phishing-2024",
        "malware_refs": "",
        "infrastructure_refs": "infra--apt29-actor-controlled-rdp",
    }
    for domain in sorted(sender_domains):
        rows.append(
            {
                "value": domain,
                "type": "domain",
                "artifact_type": "",
                "observed_at": "2024-10-23",
                **common,
                "roles": "phishing-sender",
            }
        )
    for domain in sorted(remote_domains):
        rows.append(
            {
                "value": domain,
                "type": "domain",
                "artifact_type": "",
                "observed_at": "2024-10",
                **common,
                "roles": "rdp-endpoint",
            }
        )
    for filename in sorted(filenames):
        rows.append(
            {
                "value": filename,
                "type": "",
                "artifact_type": "file-name",
                "observed_at": "2024-10",
                **common,
                "roles": "phishing-attachment",
            }
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    columns = [
        "value", "type", "artifact_type", "observed_at", "campaign_refs",
        "malware_refs", "infrastructure_refs", "roles",
    ]
    with args.output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)
    print(
        f"sender_domains={len(sender_domains)} remote_domains={len(remote_domains)} "
        f"rdp_filenames={len(filenames)} rows={len(rows)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
