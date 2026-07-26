#!/usr/bin/env python3
"""Shared, dependency-free helpers for the daily intelligence pipeline."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlparse


IOC_COLUMNS = [
    "ioc_type", "ioc_value", "date", "category", "actor", "actor_attribute",
    "malware", "malware_type", "reference", "description", "author", "confidence",
]
VALID_CONFIDENCE = {"high", "medium", "low", "unknown"}
LOW_QUALIFIERS = ("low confidence", "suspected", "possible", "疑い", "低信頼")
HIGH_QUALIFIERS = ("high confidence", "高信頼")
UNKNOWN_TIME = {
    "value": None,
    "precision": "unknown",
    "status": "unknown",
    "basis": "not-stated",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def stable_digest(*parts: str) -> str:
    return hashlib.sha256("\x1f".join(parts).encode("utf-8", errors="replace")).hexdigest()


def write_json_atomic(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False
    ) as stream:
        stream.write(content)
        temporary = Path(stream.name)
    temporary.chmod(0o644)
    temporary.replace(path)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as stream:
        return json.load(stream)


def normalized_name(value: str) -> str:
    value = value.casefold().replace("＆", "&")
    return re.sub(r"[^a-z0-9\u3040-\u30ff\u3400-\u9fff]+", "", value)


def strip_actor_qualifiers(value: str) -> str:
    value = re.sub(
        r"\s*\((?:high|medium|low)[^)]*confidence[^)]*\)\s*$",
        "",
        value,
        flags=re.IGNORECASE,
    )
    value = re.sub(r"\s*\((?:suspected|possible)\)\s*$", "", value, flags=re.IGNORECASE)
    return value.strip()


def time_point(value: str | None, basis: str) -> dict[str, Any]:
    if not value:
        return dict(UNKNOWN_TIME)
    if not re.fullmatch(r"20\d{2}-\d{2}-\d{2}", value):
        return dict(UNKNOWN_TIME)
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        return dict(UNKNOWN_TIME)
    return {
        "value": f"{value}T00:00:00Z",
        "precision": "day",
        "status": "known",
        "basis": basis,
    }


def date_from_path(path: Path) -> str | None:
    match = re.search(r"(20\d{2})(\d{2})(\d{2})", path.stem)
    if not match:
        return None
    value = "-".join(match.groups())
    return value if time_point(value, "filename")["status"] == "known" else None


def markdown_urls(text: str) -> list[str]:
    values = re.findall(r"https?://[^\s)`>\]]+", text)
    return list(dict.fromkeys(value.rstrip(".,;") for value in values))


def source_publisher(url: str) -> str:
    return (urlparse(url).hostname or "proshiba/tech-memo").removeprefix("www.")


@dataclass(frozen=True)
class ActorMatch:
    slug: str
    name: str
    term: str
    scope: str
    confidence: str
    reason: str


class ActorRegistry:
    def __init__(self, profiles_root: Path, config: dict[str, Any]):
        minimum = int(config["matching"].get("minimum_alias_length", 4))
        unsafe = {normalized_name(v) for v in config["matching"].get("unsafe_name_tokens", [])}
        candidates: dict[str, list[ActorMatch]] = {}
        self.profiles: dict[str, dict[str, Any]] = {}
        for profile_path in sorted(profiles_root.glob("*/actor-profile.json")):
            profile = load_json(profile_path)
            slug = profile_path.parent.name
            self.profiles[slug] = profile
            canonical = profile["actor"]["canonical_name"]
            entries = [(canonical, "exact", "high")]
            entries.extend(
                (
                    alias.get("name", ""),
                    alias.get("scope", "unknown"),
                    alias.get("confidence", "unknown"),
                )
                for alias in profile["actor"].get("aliases", [])
            )
            for term, scope, confidence in entries:
                key = normalized_name(term)
                if len(key) < minimum or key in unsafe:
                    continue
                candidates.setdefault(key, []).append(
                    ActorMatch(slug, canonical, term, scope, confidence, "registry")
                )
        self.terms = candidates
        safe_terms = {
            values[0].term.casefold().strip()
            for values in candidates.values()
            if self._resolve(values)
            and values[0].term.strip()
        }
        alternatives = "|".join(
            re.escape(term) for term in sorted(safe_terms, key=len, reverse=True)
        )
        self.mention_pattern = re.compile(
            rf"(?<![a-z0-9])(?:{alternatives})(?![a-z0-9])",
            re.IGNORECASE,
        )

    @staticmethod
    def _resolve(values: list[ActorMatch]) -> ActorMatch | None:
        slugs = {item.slug for item in values}
        if len(slugs) == 1:
            return sorted(
                values,
                key=lambda item: (
                    item.scope != "exact",
                    item.confidence not in {"high", "medium"},
                    len(item.term),
                ),
            )[0]
        exact = [item for item in values if item.scope == "exact"]
        if len({item.slug for item in exact}) == 1 and exact:
            return sorted(
                exact,
                key=lambda item: (
                    item.confidence not in {"high", "medium"},
                    len(item.term),
                ),
            )[0]
        return None

    def exact(self, value: str, reason: str) -> list[ActorMatch]:
        key = normalized_name(strip_actor_qualifiers(value))
        matches = self.terms.get(key, [])
        best = self._resolve(matches)
        if not best:
            return []
        return [ActorMatch(best.slug, best.name, best.term, best.scope, best.confidence, reason)]

    def mentions(self, title: str, body: str) -> list[ActorMatch]:
        found: dict[str, ActorMatch] = {}
        title_terms = {normalized_name(match.group()) for match in self.mention_pattern.finditer(title)}
        body_terms = {normalized_name(match.group()) for match in self.mention_pattern.finditer(body)}
        for key in title_terms | body_terms:
            values = self.terms.get(key, [])
            item = self._resolve(values)
            if not item:
                continue
            reason = "news-title" if key in title_terms else "news-body"
            found[item.slug] = ActorMatch(
                item.slug, item.name, item.term, item.scope, item.confidence, reason
            )
        return sorted(found.values(), key=lambda item: item.slug)

    def malware_refs(self, slug: str, values: Iterable[str]) -> list[str]:
        profile = self.profiles[slug]
        lookup: dict[str, str] = {}
        for item in profile.get("capabilities", {}).get("malware", []):
            lookup[normalized_name(item.get("name", ""))] = item["id"]
            for alias in item.get("aliases", []):
                lookup[normalized_name(alias)] = item["id"]
        refs = []
        for value in values:
            for part in re.split(r"[,;/|]", value):
                key = normalized_name(part)
                if key and key not in {"unknown", "na", "none"} and key in lookup:
                    refs.append(lookup[key])
        return sorted(set(refs))


def article_summary(body: str) -> str:
    lines = body.splitlines()
    selected: list[str] = []
    in_summary = False
    for line in lines:
        stripped = line.strip()
        if re.match(r"-\s*(?:要約|概要)\s*$", stripped):
            in_summary = True
            continue
        if in_summary and re.match(r"-\s*(?:IOC|推奨事項|その他|ChatGPT)", stripped):
            break
        if in_summary and stripped.startswith("-"):
            selected.append(re.sub(r"^-\s*", "", stripped))
            if len(selected) == 6:
                break
    if not selected:
        selected = [
            re.sub(r"^-\s*", "", line.strip())
            for line in lines
            if line.strip().startswith("-")
        ][:4]
    return " ".join(selected)[:2000]


def parse_news_file(path: Path, relative_path: str) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    news_date = date_from_path(path)
    articles: list[dict[str, Any]] = []

    section_pattern = re.compile(
        r"^###\s+(Tools|malware campaign|security report|cybercrime topics)\s*$",
        flags=re.MULTILINE | re.IGNORECASE,
    )
    section_matches = list(section_pattern.finditer(text))
    for match in section_matches:
        next_heading = re.search(r"^###\s+", text[match.end():], flags=re.MULTILINE)
        end = match.end() + next_heading.start() if next_heading else len(text)
        body = text[match.end():end]
        for link in re.finditer(r"^-\s+\[([^\]]+)\]\((https?://[^)]+)\)", body, flags=re.MULTILINE):
            articles.append(
                {
                    "title": link.group(1).strip(),
                    "url": link.group(2).strip(),
                    "primary_url": link.group(2).strip(),
                    "summary": link.group(1).strip(),
                    "body": link.group(0),
                    "news_date": news_date,
                    "news_path": relative_path,
                }
            )

    headings = list(re.finditer(r"^####\s+(.+?)\s*$", text, flags=re.MULTILINE))
    for index, match in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        body = text[match.end():end].strip()
        urls = markdown_urls(body)
        if not urls:
            continue
        primary = next(
            (u for u in urls if "一次ソース" in body[max(0, body.find(u) - 30):body.find(u)]),
            urls[0],
        )
        articles.append(
            {
                "title": match.group(1).strip(),
                "url": urls[0],
                "primary_url": primary,
                "summary": article_summary(body),
                "body": body,
                "news_date": news_date,
                "news_path": relative_path,
            }
        )

    legacy = list(re.finditer(r"^(?:\d+)\.\s+(https?://\S+)\s*$", text, flags=re.MULTILINE))
    for index, match in enumerate(legacy):
        end = legacy[index + 1].start() if index + 1 < len(legacy) else len(text)
        body = text[match.end():end].strip()
        title_match = re.search(r'^-\s*タイトル:\s*"?(.+?)"?\s*$', body, flags=re.MULTILINE)
        title = title_match.group(1) if title_match else article_summary(body)[:160]
        articles.append(
            {
                "title": title or match.group(1),
                "url": match.group(1),
                "primary_url": match.group(1),
                "summary": article_summary(body),
                "body": body,
                "news_date": news_date,
                "news_path": relative_path,
            }
        )

    seen: set[tuple[str, str]] = set()
    result = []
    for article in articles:
        key = (article["url"], article["title"])
        if key not in seen:
            seen.add(key)
            result.append(article)
    return result


def extract_artifacts(body: str) -> list[dict[str, str]]:
    labels = {
        "実行コマンド": "command",
        "コマンド": "command",
        "検体内文字列": "sample-string",
        "PDB": "pdb-path",
        "Mutex": "mutex",
        "ミューテックス": "mutex",
        "ファイルパス": "file-path",
        "レジストリ": "registry-key",
        "Named Pipe": "named-pipe",
        "User-Agent": "user-agent",
    }
    results: list[dict[str, str]] = []
    for label, artifact_type in labels.items():
        pattern = re.compile(
            rf"{re.escape(label)}\s*[:：]\s*(?:`([^`\n]+)`|([^\n]+))",
            re.IGNORECASE,
        )
        for match in pattern.finditer(body):
            value = (match.group(1) or match.group(2) or "").strip(" -*`")
            if value and not re.match(r"^(?:hxxps?|https?)://", value, re.IGNORECASE):
                results.append(
                    {"artifact_type": artifact_type, "value": value, "context": match.group(0)}
                )
    unique = {(item["artifact_type"], item["value"]): item for item in results}
    return list(unique.values())


def read_ioc_csv(path: Path, config: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8-sig", errors="replace", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != IOC_COLUMNS:
            raise ValueError(f"Unexpected IOC header in {path}: {reader.fieldnames}")
        for row_number, row in enumerate(reader, start=2):
            raw_type = row["ioc_type"].strip().casefold()
            kind = config["ioc_type_map"].get(raw_type)
            confidence = row["confidence"].strip().casefold()
            rows.append(
                {
                    "row": row_number,
                    "type": kind,
                    "raw_type": raw_type,
                    "value": row["ioc_value"].strip(),
                    "observed_date": row["date"].strip(),
                    "category": row["category"].strip(),
                    "roles": [config["category_role_map"].get(row["category"].strip(), row["category"].strip())],
                    "actor": row["actor"].strip(),
                    "actor_attribute": row["actor_attribute"].strip(),
                    "malware": row["malware"].strip(),
                    "malware_type": row["malware_type"].strip(),
                    "reference": row["reference"].strip(),
                    "description": row["description"].strip(),
                    "confidence": confidence if confidence in VALID_CONFIDENCE else "unknown",
                    "source_path": path.as_posix(),
                }
            )
    return rows


def qualifier_confidence(value: str, fallback: str) -> str:
    folded = value.casefold()
    if any(token in folded for token in LOW_QUALIFIERS):
        return "low"
    if any(token in folded for token in HIGH_QUALIFIERS):
        return "high"
    return fallback if fallback in VALID_CONFIDENCE else "unknown"


def is_safe_structured_match(actor_value: str, match: ActorMatch) -> bool:
    folded = actor_value.casefold()
    return (
        match.scope == "exact"
        and not any(token in folded for token in LOW_QUALIFIERS)
        and "/" not in actor_value
        and "aka" not in folded
    )
