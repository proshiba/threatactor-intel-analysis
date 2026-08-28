#!/usr/bin/env python3
"""Shared helpers for the actor-profile framework."""

from __future__ import annotations

import hashlib
import json
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlsplit, urlunsplit


CONFIDENCE = {"high", "medium", "low", "unknown"}
TIME_PRECISIONS = {"second", "day", "month", "year", "range", "unknown"}
TIME_STATUSES = {"known", "inferred", "unknown"}

# 攻撃活動ではない活動種別（RULES.md 4.3）。逮捕・起訴・制裁・テイクダウンは
# アクターを対象とする措置であって、アクターによる攻撃ではない。
# 標的・TTP・被害事例の自動導出と期間集計から除外する。除外しないと、
# 摘発が行われた国が標的国として、罪状の記述が被害事例として取り込まれる。
NON_OPERATIONAL_ACTIVITY_TYPES = {
    "law-enforcement-action",
    "disruption-operation",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "actor"


def stable_digest(*parts: str) -> str:
    joined = "\x1f".join(parts)
    return hashlib.sha256(joined.encode("utf-8", errors="replace")).hexdigest()


def stable_id(prefix: str, *parts: str) -> str:
    return f"{prefix}--sha256:{stable_digest(*parts)}"


def unknown_time() -> dict[str, Any]:
    return {
        "value": None,
        "precision": "unknown",
        "status": "unknown",
        "basis": "not-stated",
    }


def normalize_time(value: Any, *, basis: str = "source-stated") -> dict[str, Any]:
    if isinstance(value, dict):
        result = {
            "value": value.get("value"),
            "precision": value.get("precision", "unknown"),
            "status": value.get("status", "unknown"),
            "basis": value.get("basis", basis),
        }
        return result
    if value is None or str(value).strip() == "":
        return unknown_time()
    text = str(value).strip()
    patterns = [
        (r"^\d{4}$", "year", f"{text}-01-01T00:00:00Z"),
        (r"^\d{4}[-/.]\d{1,2}$", "month", None),
        (r"^\d{4}[-/.]\d{1,2}[-/.]\d{1,2}$", "day", None),
        (r"^\d{4}-\d{2}-\d{2}T", "second", text),
    ]
    for pattern, precision, normalized in patterns:
        if not re.match(pattern, text):
            continue
        if precision == "month":
            year, month = re.split(r"[-/.]", text)
            normalized = f"{int(year):04d}-{int(month):02d}-01T00:00:00Z"
        elif precision == "day":
            year, month, day = re.split(r"[-/.]", text)
            normalized = f"{int(year):04d}-{int(month):02d}-{int(day):02d}T00:00:00Z"
        elif precision == "second":
            normalized = text.replace("+00:00", "Z")
        try:
            datetime.fromisoformat(normalized.replace("Z", "+00:00"))
        except (TypeError, ValueError):
            return {
                "value": None,
                "precision": "unknown",
                "status": "unknown",
                "basis": f"invalid-calendar-date:{basis}",
            }
        return {
            "value": normalized,
            "precision": precision,
            "status": "known",
            "basis": basis,
        }
    return {
        "value": None,
        "precision": "unknown",
        "status": "unknown",
        "basis": f"unparsed:{basis}",
    }


def time_sort_key(point: dict[str, Any]) -> tuple[int, str]:
    value = point.get("value")
    return (1, value) if value else (0, "")


def earliest_time(points: Iterable[dict[str, Any]]) -> dict[str, Any]:
    known = [p for p in points if p.get("value")]
    return min(known, key=time_sort_key) if known else unknown_time()


def latest_time(points: Iterable[dict[str, Any]]) -> dict[str, Any]:
    known = [p for p in points if p.get("value")]
    return max(known, key=time_sort_key) if known else unknown_time()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as stream:
        return json.load(stream)


def write_json_atomic(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False
    ) as stream:
        stream.write(content)
        temp_path = Path(stream.name)
    temp_path.chmod(0o644)
    temp_path.replace(path)


def resolve_inside(root: Path, relative_or_absolute: str) -> Path:
    candidate = Path(relative_or_absolute)
    if not candidate.is_absolute():
        candidate = root / candidate
    candidate = candidate.resolve()
    root_resolved = root.resolve()
    try:
        candidate.relative_to(root_resolved)
    except ValueError as exc:
        raise ValueError(f"Path escapes repository root: {candidate}") from exc
    return candidate


def merge_metadata(*items: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    array_fields = {
        "campaign_refs",
        "malware_refs",
        "infrastructure_refs",
        "roles",
    }
    for item in items:
        for key, value in item.items():
            if value is None:
                continue
            if key in array_fields:
                previous = result.get(key, [])
                result[key] = sorted(set(previous) | set(value))
            else:
                result[key] = value
    return result


_DEFANG_BRACKETS = (
    (re.compile(r"\[\s*\.\s*\]"), "."),
    (re.compile(r"\(\s*\.\s*\)"), "."),
    (re.compile(r"\{\s*\.\s*\}"), "."),
    (re.compile(r"\[\s*dot\s*\]", re.IGNORECASE), "."),
    (re.compile(r"\[\s*:\s*\]"), ":"),
    (re.compile(r"\[\s*/\s*\]"), "/"),
    (re.compile(r"\[\s*@\s*\]"), "@"),
    (re.compile(r"\(\s*@\s*\)"), "@"),
    (re.compile(r"\[\s*at\s*\]", re.IGNORECASE), "@"),
)
_DEFANG_SCHEME = re.compile(r"h\s*x\s*x\s*p(s?)", re.IGNORECASE)


def refang(value: str) -> str:
    """Restore defanged notation.

    Brackets are resolved before the scheme so that mixed forms such as
    ``hxxps[:]//example.com`` do not leave an ``hxxp`` behind, and the scheme is
    matched case-insensitively so ``HXXPS://`` and ``hXXps://`` are covered too.
    """
    value = value.strip()
    for pattern, replacement in _DEFANG_BRACKETS:
        value = pattern.sub(replacement, value)
    return _DEFANG_SCHEME.sub(lambda m: "http" + m.group(1).lower(), value)


def normalize_observable(kind: str, value: str) -> str:
    cleaned = refang(value).strip().strip("`'\"<>[](),;.")
    if kind in {"md5", "sha1", "sha256", "sha512", "certificate-fingerprint"}:
        return re.sub(r"[^0-9a-fA-F]", "", cleaned).lower()
    if kind in {"domain", "email"}:
        return cleaned.rstrip(".").lower()
    if kind in {"ipv4", "ipv6"}:
        return cleaned.lower()
    if kind == "url":
        try:
            parts = urlsplit(cleaned)
            host = (parts.hostname or "").lower()
            if not host:
                return cleaned
            netloc = host
            if parts.port:
                netloc += f":{parts.port}"
            return urlunsplit(
                (
                    parts.scheme.lower(),
                    netloc,
                    parts.path or "/",
                    parts.query,
                    "",
                )
            )
        except ValueError:
            return cleaned
    return re.sub(r"\s+", " ", cleaned).strip()


def stix_pattern(kind: str, normalized: str) -> str:
    escaped = normalized.replace("\\", "\\\\").replace("'", "\\'")
    mapping = {
        "md5": f"[file:hashes.'MD5' = '{escaped}']",
        "sha1": f"[file:hashes.'SHA-1' = '{escaped}']",
        "sha256": f"[file:hashes.'SHA-256' = '{escaped}']",
        "sha512": f"[file:hashes.'SHA-512' = '{escaped}']",
        "ipv4": f"[ipv4-addr:value = '{escaped}']",
        "ipv6": f"[ipv6-addr:value = '{escaped}']",
        "domain": f"[domain-name:value = '{escaped}']",
        "url": f"[url:value = '{escaped}']",
        "email": f"[email-addr:value = '{escaped}']",
        "certificate-fingerprint": f"[x509-certificate:hashes.'SHA-256' = '{escaped}']",
    }
    return mapping[kind]


def json_array_cell(values: Iterable[str]) -> str:
    return json.dumps(sorted(set(values)), ensure_ascii=False, separators=(",", ":"))


def parse_json_array_cell(value: str) -> list[str]:
    parsed = json.loads(value or "[]")
    if not isinstance(parsed, list) or not all(isinstance(item, str) for item in parsed):
        raise ValueError("Expected JSON string array")
    return parsed
