#!/usr/bin/env python3
"""Build an actor-identifier index from Google Threat Intelligence articles."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import time
import xml.etree.ElementTree as ET
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup

from common import stable_id, utc_now, write_json_atomic


ACTOR_RE = re.compile(
    r"(?i)\b(?:UNC|FIN|DEV|UAC|TAG|TA|APT|STORM)[- ]?\d{2,5}\b"
)
TI_PATH = "/blog/topics/threat-intelligence/"


def get(url: str, retries: int = 2) -> bytes:
    error: Exception | None = None
    for attempt in range(retries):
        try:
            result = subprocess.run(
                [
                    "curl",
                    "-L",
                    "--fail",
                    "--silent",
                    "--show-error",
                    "--max-time",
                    "15",
                    "--user-agent",
                    "threatactor-intel-analysis/1.0",
                    url,
                ],
                check=True,
                capture_output=True,
                timeout=20,
            )
            return result.stdout
        except Exception as exc:
            error = exc
            time.sleep(0.2 * (attempt + 1))
    assert error is not None
    raise error


def sitemap_urls(content: bytes) -> list[str]:
    root = ET.fromstring(content)
    return [
        element.text.strip()
        for element in root.iter()
        if element.tag.endswith("loc") and element.text
    ]


def normalize_actor_id(value: str) -> str:
    compact = re.sub(r"\s+", "", value.upper())
    if "-" not in compact:
        match = re.match(r"([A-Z]+)(\d+)$", compact)
        if match and match.group(1) in {"DEV", "UAC", "TAG", "STORM"}:
            return f"{match.group(1)}-{match.group(2)}"
    return compact


def parse_article(url: str, content: bytes) -> dict[str, Any]:
    soup = BeautifulSoup(content, "html.parser")
    for node in soup(["script", "style", "nav", "footer"]):
        node.decompose()
    title_node = soup.find("h1") or soup.find("title")
    title = title_node.get_text(" ", strip=True) if title_node else url
    text = re.sub(r"\s+", " ", soup.get_text(" ", strip=True))
    published = ""
    for attrs in (
        {"itemprop": "datePublished"},
        {"property": "article:published_time"},
        {"name": "date"},
    ):
        node = soup.find(attrs=attrs)
        if node:
            published = str(node.get("content") or node.get_text(" ", strip=True))
            if published:
                break
    actors: dict[str, str] = {}
    for match in ACTOR_RE.finditer(text):
        actor_id = normalize_actor_id(match.group())
        start = max(0, match.start() - 220)
        end = min(len(text), match.end() + 420)
        actors.setdefault(actor_id, text[start:end])
    return {
        "url": url,
        "title": title,
        "published_at": published,
        "actors": actors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--sitemap-index",
        type=Path,
        default=Path("actor_profile/reference/osint/google-cloud-sitemap.xml"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(
            "actor_profile/reference/osint/google-threat-intelligence-actor-index.json"
        ),
    )
    parser.add_argument("--workers", type=int, default=12)
    args = parser.parse_args()
    sitemap_list = sitemap_urls(args.sitemap_index.read_bytes())
    article_urls: set[str] = set()
    sitemap_errors: list[dict[str, str]] = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        future_map = {pool.submit(get, url): url for url in sitemap_list}
        for future in as_completed(future_map):
            url = future_map[future]
            try:
                for candidate in sitemap_urls(future.result()):
                    if TI_PATH in candidate:
                        article_urls.add(candidate)
            except Exception as exc:
                sitemap_errors.append(
                    {"url": url, "error": f"{type(exc).__name__}: {exc}"}
                )
    print(
        json.dumps(
            {
                "stage": "sitemaps",
                "processed": len(sitemap_list),
                "errors": len(sitemap_errors),
                "threat_intelligence_urls": len(article_urls),
            },
            ensure_ascii=False,
        ),
        flush=True,
    )
    articles: list[dict[str, Any]] = []
    article_errors: list[dict[str, str]] = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        future_map = {
            pool.submit(get, url): url for url in sorted(article_urls)
        }
        for future in as_completed(future_map):
            url = future_map[future]
            try:
                article = parse_article(url, future.result())
                if article["actors"]:
                    articles.append(article)
            except Exception as exc:
                article_errors.append(
                    {"url": url, "error": f"{type(exc).__name__}: {exc}"}
                )
    print(
        json.dumps(
            {
                "stage": "articles",
                "processed": len(article_urls),
                "matched": len(articles),
                "errors": len(article_errors),
            },
            ensure_ascii=False,
        ),
        flush=True,
    )
    by_actor: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for article in articles:
        for actor_id, excerpt in article["actors"].items():
            by_actor[actor_id].append(
                {
                    "url": article["url"],
                    "title": article["title"],
                    "published_at": article["published_at"],
                    "context_excerpt": excerpt,
                }
            )
    values = []
    for actor_id, actor_articles in sorted(by_actor.items()):
        actor_articles.sort(
            key=lambda item: (item["published_at"], item["url"]), reverse=True
        )
        values.append(
            {
                "uuid": stable_id("google-ti-actor", actor_id),
                "value": actor_id,
                "description": actor_articles[0]["context_excerpt"],
                "meta": {
                    "synonyms": [],
                    "refs": [item["url"] for item in actor_articles],
                    "article_count": len(actor_articles),
                    "articles": actor_articles,
                },
            }
        )
    result = {
        "name": "Google Threat Intelligence Actor Identifier Index",
        "source": "Google Cloud Threat Intelligence article corpus",
        "type": "threat-actor",
        "version": utc_now(),
        "retrieved_at": utc_now(),
        "sitemap_count": len(sitemap_list),
        "article_url_count": len(article_urls),
        "matched_article_count": len(articles),
        "sitemap_errors": sorted(sitemap_errors, key=lambda item: item["url"]),
        "article_errors": sorted(article_errors, key=lambda item: item["url"]),
        "values": values,
    }
    write_json_atomic(args.output.resolve(), result)
    print(
        json.dumps(
            {
                "sitemaps": len(sitemap_list),
                "article_urls": len(article_urls),
                "matched_articles": len(articles),
                "actors": len(values),
                "errors": len(sitemap_errors) + len(article_errors),
                "output": str(args.output),
            },
            ensure_ascii=False,
        )
    )
    return 1 if sitemap_errors or article_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
