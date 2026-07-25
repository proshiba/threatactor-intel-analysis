#!/usr/bin/env python3
"""Fetch and combine all public ETDA/ThaiCERT Threat Group Cards."""

from __future__ import annotations

import argparse
import json
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup

from common import load_json, utc_now, write_json_atomic


BASE = "https://apt.etda.or.th"


def fetch(group: str, retries: int = 3) -> tuple[str, dict[str, Any] | None, str | None]:
    query = urllib.parse.urlencode({"g": group, "o": "j"})
    url = f"{BASE}/cgi-bin/getcard.cgi?{query}"
    error = ""
    for attempt in range(retries):
        try:
            request = urllib.request.Request(
                url,
                headers={"User-Agent": "threatactor-intel-analysis/1.0"},
            )
            with urllib.request.urlopen(request, timeout=30) as response:
                data = json.loads(response.read().decode("utf-8", errors="replace"))
            return group, data, None
        except Exception as exc:  # network and upstream format errors are recorded
            error = f"{type(exc).__name__}: {exc}"
            time.sleep(0.5 * (attempt + 1))
    return group, None, error


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--list-html",
        type=Path,
        default=Path("actor_profile/reference/osint/etda-threat-group-list.html"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("actor_profile/reference/osint/etda-threat-group-cards.json"),
    )
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()
    soup = BeautifulSoup(
        args.list_html.read_text(encoding="utf-8", errors="replace"),
        "html.parser",
    )
    groups: list[str] = []
    for link in soup.find_all("a", href=True):
        if "showcard.cgi" not in link["href"]:
            continue
        query = urllib.parse.parse_qs(
            urllib.parse.urlsplit(link["href"]).query
        )
        group = query.get("g", [""])[0].strip()
        if group and group not in groups:
            groups.append(group)
    values: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []
    metadata: dict[str, Any] = {}
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(fetch, group) for group in groups]
        for future in as_completed(futures):
            group, data, error = future.result()
            if error or not data:
                errors.append({"group": group, "error": error or "empty response"})
                continue
            metadata.update(
                {
                    key: value
                    for key, value in data.items()
                    if key != "values"
                }
            )
            for item in data.get("values", []):
                item = dict(item)
                item["_card_url"] = (
                    f"{BASE}/cgi-bin/showcard.cgi?"
                    + urllib.parse.urlencode({"g": group, "n": "1"})
                )
                values.append(item)
    values.sort(key=lambda item: str(item.get("actor", "")).lower())
    result = {
        **metadata,
        "retrieved_at": utc_now(),
        "requested_card_count": len(groups),
        "retrieved_card_count": len(values),
        "errors": sorted(errors, key=lambda item: item["group"]),
        "values": values,
    }
    write_json_atomic(args.output.resolve(), result)
    print(
        json.dumps(
            {
                "requested": len(groups),
                "retrieved": len(values),
                "errors": len(errors),
                "output": str(args.output),
            },
            ensure_ascii=False,
        )
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
