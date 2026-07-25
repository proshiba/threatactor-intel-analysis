#!/usr/bin/env python3
"""Build a compact UAC actor index from fixed CERT-UA API responses."""

from __future__ import annotations

import argparse
import html
import re
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

from common import stable_id, utc_now, write_json_atomic


UAC_RE = re.compile(r"(?i)\bUAC[-_]\d{3,4}\b")
TAG_RE = re.compile(r"<[^>]+>")


def clean_html(value: str) -> str:
    return re.sub(r"\s+", " ", TAG_RE.sub(" ", html.unescape(value))).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input-glob",
        default="actor_profile/reference/osint/cert-ua-all-page-*.xml",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("actor_profile/reference/osint/cert-ua-uac-index.json"),
    )
    args = parser.parse_args()
    articles: dict[str, dict[str, str]] = {}
    for path in sorted(Path(".").glob(args.input_glob)):
        root = ET.parse(path).getroot()
        for item in root.findall("./items/items"):
            article_id = item.findtext("id") or ""
            if not article_id:
                continue
            articles[article_id] = {
                "id": article_id,
                "title": item.findtext("title") or "",
                "description": clean_html(item.findtext("description") or ""),
                "date": item.findtext("date") or "",
                "english_id": item.findtext("engId") or "",
            }
    by_actor: dict[str, list[dict[str, str]]] = defaultdict(list)
    for article in articles.values():
        text = article["title"] + " " + article["description"]
        actor_ids = {
            match.group().upper().replace("_", "-")
            for match in UAC_RE.finditer(text)
        }
        for actor_id in actor_ids:
            by_actor[actor_id].append(article)
    values = []
    for actor_id, actor_articles in sorted(by_actor.items()):
        actor_articles.sort(key=lambda item: (item["date"], item["id"]), reverse=True)
        refs = [
            f"https://cert.gov.ua/article/{item['id']}"
            for item in actor_articles
        ]
        values.append(
            {
                "uuid": stable_id("cert-ua-actor", actor_id),
                "value": actor_id,
                "description": actor_articles[0]["description"],
                "meta": {
                    "refs": refs,
                    "synonyms": [],
                    "first_indexed_date": min(
                        item["date"] for item in actor_articles if item["date"]
                    ),
                    "last_indexed_date": max(
                        item["date"] for item in actor_articles if item["date"]
                    ),
                    "article_count": len(actor_articles),
                    "articles": actor_articles,
                },
            }
        )
    result = {
        "name": "CERT-UA UAC Article Index",
        "type": "threat-actor",
        "source": "CERT-UA official API",
        "version": utc_now(),
        "description": (
            "Actor identifiers extracted from the title and official summary of "
            "fixed CERT-UA article-index API responses."
        ),
        "article_count": len(articles),
        "values": values,
    }
    write_json_atomic(args.output.resolve(), result)
    print(
        {
            "article_count": len(articles),
            "actor_count": len(values),
            "output": str(args.output),
        }
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
