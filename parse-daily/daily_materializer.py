"""Pure modeling helpers for approved daily intelligence records."""

from __future__ import annotations

import csv
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import unquote_plus, urlsplit, urlunsplit

from daily_common import (
    UNKNOWN_TIME,
    is_file_like,
    load_json,
    source_publisher,
    source_reliability,
    stable_digest,
    time_point,
)


REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "actor_profile" / "scripts"))
from activity_diamond import build_activity_diamond  # noqa: E402
from common import normalize_time as normalize_profile_time  # noqa: E402
from stix_modeling import default_stix_object_type  # noqa: E402

FILE_NAME_SEARCH = re.compile(
    r"([^/\\\s]+\.(?:exe|dll|sys|ps1|bat|cmd|js|jse|vbs|hta|lnk|"
    r"docm?|xlsm?|pptm?|pdf|zip|rar|7z|apk|dmg|pkg|sh|py))",
    re.IGNORECASE,
)
DAILY_ID_PREFIXES = ("source--daily-", "activity--daily-", "malware--daily-")
DAILY_ID_SEARCH = re.compile(
    r"(?:source|activity|malware)--daily-[A-Za-z0-9._:-]+"
)
TRACKING_QUERY_PARAMETERS = frozenset(
    {
        "_ga",
        "_gl",
        "dclid",
        "fbclid",
        "gclid",
        "mc_cid",
        "mc_eid",
        "msclkid",
        "srsltid",
    }
)


def source_id_for_value(value: str) -> str:
    return f"source--daily-{stable_digest(value)[:20]}"


def canonical_source_url(value: str) -> str:
    """Return a conservative identity key for an HTTP(S) source URL.

    Fragments and well-known analytics parameters do not identify a different
    publication.  Other query parameters can select different content, so
    they are preserved byte-for-byte (including their order and encoding).
    Non-web paths are left untouched.
    """
    if not value:
        return ""
    try:
        parsed = urlsplit(value)
    except ValueError:
        return value
    if parsed.scheme.casefold() not in {"http", "https"} or not parsed.netloc:
        return value

    query_parts = []
    for part in parsed.query.split("&") if parsed.query else []:
        raw_key = part.partition("=")[0]
        key = unquote_plus(raw_key).casefold()
        if key.startswith("utm_") or key in TRACKING_QUERY_PARAMETERS:
            continue
        query_parts.append(part)

    # Treat the common URL spellings ``/report`` and ``/report/`` as one
    # publication without changing any other path semantics.
    path = parsed.path.rstrip("/")
    return urlunsplit(
        (parsed.scheme, parsed.netloc, path, "&".join(query_parts), "")
    )


def source_id_for_url(
    source: dict[str, Any], existing_sources: list[dict[str, Any]] | None = None
) -> str:
    """Reuse an existing curated Source identity when its canonical URL matches."""
    url = source.get("url") or source.get("path") or ""
    canonical_url = canonical_source_url(url)
    matches = [
        existing
        for existing in existing_sources or []
        if canonical_url
        and canonical_source_url(
            existing.get("url") or existing.get("path") or ""
        )
        == canonical_url
    ]
    if matches:
        curated = next(
            (
                item
                for item in matches
                if not item.get("source_id", "").startswith("source--daily-")
            ),
            None,
        )
        return (curated or matches[0])["source_id"]
    return source.get("source_id") or source_id_for_value(canonical_url)


def reconcile_profile_source_identity(
    profile: dict[str, Any], source: dict[str, Any], selected_source_id: str
) -> set[str]:
    """Replace same-URL legacy daily Source references with curated identity."""
    url = source.get("url") or source.get("path") or ""
    canonical_url = canonical_source_url(url)
    old_ids = {
        item["source_id"]
        for item in profile.get("sources", [])
        if canonical_url
        and canonical_source_url(item.get("url") or item.get("path") or "")
        == canonical_url
        and item.get("source_id") != selected_source_id
        and item.get("source_id", "").startswith("source--daily-")
    }
    if not old_ids:
        return set()

    def replace_refs(value: Any) -> None:
        if isinstance(value, dict):
            for key, item in value.items():
                if key == "source_ref" and item in old_ids:
                    value[key] = selected_source_id
                elif key.endswith("_refs") and isinstance(item, list):
                    value[key] = sorted(
                        {
                            selected_source_id if ref in old_ids else ref
                            for ref in item
                        }
                    )
                else:
                    replace_refs(item)
        elif isinstance(value, list):
            for item in value:
                replace_refs(item)

    replace_refs(profile)
    profile["sources"] = [
        item
        for item in profile.get("sources", [])
        if item.get("source_id") not in old_ids
    ]
    return old_ids


def merge_materialized_source(
    existing_source: dict[str, Any], modeled_source: dict[str, Any]
) -> dict[str, Any]:
    """Preserve curated metadata while filling a reviewed publication date.

    A canonical-URL match gives the curated Source ownership of identity and
    descriptive metadata.  An unknown curated ``published_at`` is absence of a
    fact, however, and must not erase a known analyst-reviewed source
    publication date from the daily record.
    """
    merged = {**modeled_source, **existing_source}
    existing_published = existing_source.get("published_at") or UNKNOWN_TIME
    modeled_published = modeled_source.get("published_at") or UNKNOWN_TIME
    if (
        existing_published.get("status") == "unknown"
        and modeled_published.get("status") == "known"
        and modeled_published.get("value")
        and modeled_published.get("basis") == "source-publication"
    ):
        merged["published_at"] = dict(modeled_published)
    return merged


def reviewed_reported_at_issue(point: Any) -> str | None:
    """Return why a reviewed publication time is unsafe, or ``None``."""
    required = {"value", "precision", "status", "basis"}
    if not isinstance(point, dict):
        return "reported_at must be a timePoint object"
    if set(point) != required:
        return "reported_at must contain only value/precision/status/basis"
    status = point.get("status")
    if status == "unknown":
        if point.get("value") is not None or point.get("precision") != "unknown":
            return "unknown reported_at requires value=null and precision=unknown"
        if not isinstance(point.get("basis"), str) or not point["basis"]:
            return "unknown reported_at requires a non-empty basis"
        return None
    if status != "known":
        return "reported_at status must be known or unknown"
    if point.get("basis") != "source-publication":
        return "known reported_at basis must be source-publication"
    if point.get("precision") not in {"second", "day", "month", "year"}:
        return "known reported_at has invalid precision"
    value = point.get("value")
    if not isinstance(value, str) or not re.fullmatch(
        r"20\d{2}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", value
    ):
        return "known reported_at value must be an RFC 3339 UTC date-time"
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return "known reported_at contains an invalid calendar date-time"
    precision = point["precision"]
    if precision == "year" and (
        parsed.month != 1
        or parsed.day != 1
        or parsed.hour
        or parsed.minute
        or parsed.second
    ):
        return "year-precision reported_at must be normalized to January 1 00:00:00Z"
    if precision == "month" and (
        parsed.day != 1 or parsed.hour or parsed.minute or parsed.second
    ):
        return "month-precision reported_at must be normalized to day 1 00:00:00Z"
    if precision == "day" and (parsed.hour or parsed.minute or parsed.second):
        return "day-precision reported_at must be normalized to 00:00:00Z"
    return None


def activity_reference(record: dict[str, Any]) -> str:
    activity = record["activity"]
    return (
        activity.get("activity_reference")
        or activity.get("primary_url")
        or activity["news_path"]
    )


def generated_activity_id_for(record: dict[str, Any]) -> str:
    return (
        f"activity--daily-"
        f"{stable_digest(record['actor']['slug'], activity_reference(record))[:20]}"
    )


def activity_id_override_issue(value: Any, actor_slug: str) -> str | None:
    """Return why a curated Activity ID override is unsafe, or ``None``."""
    if not isinstance(value, str) or not re.fullmatch(
        r"activity--[a-z0-9][a-z0-9._-]*", value
    ):
        return "activity_id_override must be a lowercase stable activity-- ID"
    if value.startswith("activity--daily-"):
        return "activity_id_override must not use the daily-owned namespace"
    if not value.startswith(f"activity--{actor_slug}-"):
        return (
            "activity_id_override must be scoped to its actor slug "
            f"(activity--{actor_slug}-...)"
        )
    return None


def activity_id_for(record: dict[str, Any]) -> str:
    override = record.get("activity_id_override")
    if override is not None:
        issue = activity_id_override_issue(
            override, record.get("actor", {}).get("slug", "")
        )
        if issue:
            raise ValueError(issue)
        return override
    return generated_activity_id_for(record)


def _replace_exact_ids(value: Any, replacements: dict[str, str]) -> Any:
    """Replace exact structured identifiers without rewriting prose."""
    if isinstance(value, dict):
        for key, item in list(value.items()):
            value[key] = _replace_exact_ids(item, replacements)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            value[index] = _replace_exact_ids(item, replacements)
    elif isinstance(value, str):
        return replacements.get(value, value)
    return value


def _structured_ref_issues(value: Any, path: str) -> list[str]:
    issues: list[str] = []
    if isinstance(value, dict):
        for key, item in value.items():
            child_path = f"{path}.{key}"
            if key == "field_map":
                # Manifest field maps name evidence columns; e.g.
                # {"campaign_refs": "campaign_refs"} is not a static ref list.
                continue
            if key in {"activity_refs", "campaign_refs"} and (
                not isinstance(item, list)
                or not all(isinstance(ref, str) for ref in item)
            ):
                issues.append(f"{child_path} must be an array of strings")
            else:
                issues.extend(_structured_ref_issues(item, child_path))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            issues.extend(_structured_ref_issues(item, f"{path}[{index}]"))
    return issues


def activity_identity_migration_issues(
    profile: dict[str, Any],
    dataset: dict[str, Any],
    artifact_rows: list[dict[str, str]],
    source_manifest: dict[str, Any] | None,
    activity_id_map: dict[str, str],
) -> list[str]:
    """Validate stable Activity migrations before mutating any actor output."""
    issues: list[str] = []
    target_ids: dict[str, str] = {}
    for old_id, new_id in activity_id_map.items():
        if not old_id.startswith("activity--daily-"):
            issues.append(f"Activity migration source is not daily-owned: {old_id}")
        if new_id.startswith("activity--daily-") or not new_id.startswith(
            "activity--"
        ):
            issues.append(f"Activity migration target is not stable: {new_id}")
        prior = target_ids.get(new_id)
        if prior and prior != old_id:
            issues.append(
                f"Activity migration collision: {prior} and {old_id} -> {new_id}"
            )
        target_ids[new_id] = old_id
        if new_id in activity_id_map:
            issues.append(
                f"Activity migration chain/collision is unsafe: {old_id} -> {new_id}"
            )

    activity_ids = [
        item.get("activity_id") for item in profile.get("activities", [])
    ]
    for activity_id in set(activity_ids):
        if activity_id and activity_ids.count(activity_id) > 1:
            issues.append(f"duplicate Activity ID in profile: {activity_id}")
    for old_id, new_id in activity_id_map.items():
        if old_id in activity_ids and new_id in activity_ids:
            issues.append(
                f"Activity migration target already exists beside source: "
                f"{old_id} -> {new_id}"
            )

    issues.extend(_structured_ref_issues(profile, "profile"))
    issues.extend(_structured_ref_issues(dataset, "iocs"))
    if source_manifest is not None:
        issues.extend(_structured_ref_issues(source_manifest, "ioc-sources"))
        for collection in ("sources", "source_groups"):
            for index, source in enumerate(source_manifest.get(collection, [])):
                field_map = source.get("field_map", {}) if isinstance(source, dict) else {}
                if activity_id_map and isinstance(field_map, dict) and (
                    {"activity_refs", "campaign_refs"} & set(field_map)
                ):
                    issues.append(
                        f"ioc-sources.{collection}[{index}].field_map has dynamic "
                        "Activity refs; migrate the evidence column explicitly"
                    )
    for index, row in enumerate(artifact_rows):
        try:
            _json_array_values(row.get("campaign_refs", ""))
        except (TypeError, ValueError) as exc:
            issues.append(f"artifacts[{index}].campaign_refs: {exc}")
    return issues


def migrate_activity_identities(
    profile: dict[str, Any],
    dataset: dict[str, Any],
    artifact_rows: list[dict[str, str]],
    source_manifest: dict[str, Any] | None,
    activity_id_map: dict[str, str],
    common: Any,
) -> list[dict[str, str]]:
    """Propagate explicit daily→stable Activity identity changes everywhere."""
    if not activity_id_map:
        return artifact_rows
    issues = activity_identity_migration_issues(
        profile, dataset, artifact_rows, source_manifest, activity_id_map
    )
    if issues:
        raise ValueError("; ".join(issues))

    _replace_exact_ids(profile, activity_id_map)
    _replace_exact_ids(dataset, activity_id_map)
    if source_manifest is not None:
        _replace_exact_ids(source_manifest, activity_id_map)
    for indicator in dataset.get("indicators", []):
        if indicator.get("observations"):
            refresh_indicator(indicator)

    migrated_artifacts: list[dict[str, str]] = []
    for original in artifact_rows:
        row = dict(original)
        campaign_refs = {
            activity_id_map.get(ref, ref)
            for ref in _json_array_values(row.get("campaign_refs", ""))
        }
        row["campaign_refs"] = common.json_array_cell(sorted(campaign_refs))
        row["campaign_count"] = str(len(campaign_refs))
        row["seen_in_multiple_campaigns"] = (
            "true" if len(campaign_refs) > 1 else "false"
        )
        migrated_artifacts.append(row)
    return migrated_artifacts


def merge_materialized_activity(
    existing: dict[str, Any], modeled: dict[str, Any]
) -> dict[str, Any]:
    """Refresh an override-backed Activity without erasing later curation."""
    # Core report facts are owned by the reviewed daily decision so corrections
    # to title/type/period/report date/description/confidence remain applicable.
    # Analyst-enriched graph edges and notes are additive and must survive a
    # full-history rebuild.  ``materialize_profile_diamonds`` refreshes the
    # derived diamond after this merge at the end of apply_review_queue.
    merged = {**existing, **modeled}
    for field in (
        "activity_refs",
        "target_refs",
        "malware_refs",
        "infrastructure_refs",
        "tool_refs",
        "ttp_refs",
        "victim_refs",
        "evidence_refs",
    ):
        merged[field] = sorted(
            set(existing.get(field, [])) | set(modeled.get(field, []))
        )
    note_parts = {
        part.strip()
        for value in (
            existing.get("analyst_notes", ""),
            modeled.get("analyst_notes", ""),
        )
        for part in value.split(" | ")
        if part.strip()
    }
    merged["analyst_notes"] = " | ".join(sorted(note_parts))
    return merged


def repository_url(queue: dict[str, Any], path: str) -> str:
    return (
        f"https://github.com/{queue['source']['repository']}/blob/"
        f"{queue['source']['commit']}/{path}"
    )


def source_items(record: dict[str, Any], queue: dict[str, Any]) -> list[dict[str, str]]:
    values = record.get("sources", [])
    if not values:
        activity = record["activity"]
        values = [
            {
                "url": activity.get("primary_url") or "",
                "source_path": activity["news_path"],
                "source_type": "primary-report",
            }
        ]
    result: list[dict[str, str]] = []
    seen: set[str] = set()
    for item in values:
        path = item.get("source_path") or record["activity"]["news_path"]
        url = item.get("url") or repository_url(queue, path)
        canonical_url = canonical_source_url(url)
        if canonical_url in seen:
            continue
        seen.add(canonical_url)
        entry = {
            "url": url,
            "source_path": path,
            "source_type": item.get("source_type", "osint-report"),
        }
        # 別の記事から集約した出典は、その記事自身の日付と見出しを保持する
        for field in ("news_date", "title"):
            if item.get(field):
                entry[field] = item[field]
        result.append(entry)
    return sorted(result, key=lambda item: item["url"])


def source_for_row(
    record: dict[str, Any], row: dict[str, Any], queue: dict[str, Any]
) -> dict[str, str]:
    reference = row.get("reference", "").strip()
    if reference:
        return {
            "url": reference,
            "source_path": row.get("source_path") or record["activity"]["news_path"],
            "source_type": (
                "primary-report"
                if reference == activity_reference(record)
                else "ioc-reference"
            ),
        }
    return source_items(record, queue)[0]


def primary_source(
    record: dict[str, Any], queue: dict[str, Any]
) -> dict[str, str]:
    sources = source_items(record, queue)
    reference = activity_reference(record)
    return next(
        (
            item
            for item in sources
            if canonical_source_url(item["url"])
            == canonical_source_url(reference)
            or item["source_type"] == "primary-report"
        ),
        sources[0],
    )


def profile_source(
    record: dict[str, Any], source: dict[str, str], queue: dict[str, Any]
) -> dict[str, Any]:
    activity = record["activity"]
    primary = source["url"]
    # 集約した出典は自分の日付と見出しを持つ。無い場合だけ活動側の値を使う。
    news_date = source.get("news_date") or activity.get("news_date")
    title = source.get("title") or activity["title"]
    reviewed_publication = reviewed_source_publication(record)
    if (
        source["source_type"] == "primary-report"
        and canonical_source_url(primary)
        == canonical_source_url(activity_reference(record))
        and reviewed_publication is not None
    ):
        published = reviewed_publication
    elif source["source_type"] == "primary-report":
        published = time_point(news_date, "daily-news-file-date")
    else:
        published = dict(UNKNOWN_TIME)
    return {
        "source_id": source_id_for_value(canonical_source_url(primary)),
        "path": primary,
        "title": (
            title
            if source["source_type"] == "primary-report"
            else f"{title} — IOC補助資料"
        ),
        "publisher": source_publisher(primary),
        "published_at": published,
        "language": "unknown",
        "source_type": "osint-report",
        "tlp": "TLP:CLEAR",
        "reliability": source_reliability(primary),
        "sha256": None,
        "analyst_notes": (
            f"tech-memo日次収集から取込。元ファイル: {source['source_path']}; "
            f"source commit: {queue['source']['commit']}; "
            "出典信頼性はアクター帰属確度と分離して評価。"
        ),
    }


def activity_bounds(record: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    reviewed = record.get("activity_period", {})
    if reviewed:
        return (
            dict(reviewed.get("first_observed") or UNKNOWN_TIME),
            dict(reviewed.get("last_observed") or UNKNOWN_TIME),
        )
    return dict(UNKNOWN_TIME), dict(UNKNOWN_TIME)


def reviewed_source_publication(record: dict[str, Any]) -> dict[str, Any] | None:
    """Return a usable reviewed publication time, never an unknown placeholder."""
    reviewed = record.get("reported_at")
    if (
        isinstance(reviewed, dict)
        and reviewed.get("status") == "known"
        and reviewed.get("value")
        and reviewed.get("basis") == "source-publication"
    ):
        return dict(reviewed)
    return None


def curated_source_publication(
    record: dict[str, Any],
    preferred_sources: list[dict[str, Any]] | None = None,
) -> dict[str, Any] | None:
    """Return a known publication point from the selected canonical Source."""
    primary_url = activity_reference(record)
    selected_source_id = source_id_for_url(
        {"url": primary_url}, preferred_sources or []
    )
    for source in preferred_sources or []:
        if source.get("source_id") != selected_source_id:
            continue
        if canonical_source_url(
            source.get("url") or source.get("path") or ""
        ) != canonical_source_url(primary_url):
            continue
        published = source.get("published_at") or UNKNOWN_TIME
        if (
            published.get("status") in {"known", "inferred"}
            and published.get("value")
            # The tech-memo file date is a collection timestamp, not an
            # independently curated publication fact.  It must not conflict
            # with a later review that supplies the real source publication
            # date.
            and published.get("basis") != "daily-news-file-date"
        ):
            return dict(published)
    return None


def activity_reported_at(
    record: dict[str, Any],
    preferred_sources: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Prefer reviewed/curated publication time over the collection date."""
    reviewed = reviewed_source_publication(record)
    curated = curated_source_publication(record, preferred_sources)
    if reviewed is not None and curated is not None:
        if reviewed.get("value") != curated.get("value"):
            raise ValueError(
                "reviewed reported_at conflicts with canonical Source published_at"
            )
        return reviewed
    if reviewed is not None:
        return reviewed
    if curated is not None:
        return curated
    return time_point(record["activity"].get("news_date"), "daily-news-file-date")


def activity_type_for(record: dict[str, Any]) -> str:
    reviewed = record.get("activity_type")
    if isinstance(reviewed, str) and reviewed:
        return reviewed
    text = (
        f"{record['activity'].get('title', '')} "
        f"{record['activity'].get('summary', '')}"
    ).casefold()
    categories = (
        (("ransom", "ランサム", "extortion", "恐喝"), "ransomware-extortion"),
        (("phish", "フィッシング", "なりすまし"), "phishing-campaign"),
        (("espionage", "諜報", "スパイ"), "cyber-espionage"),
        (("ddos", "ワイパー", "disrupt", "破壊", "妨害"), "disruptive-activity"),
        (("botnet", "c2", "インフラ"), "infrastructure-operation"),
        (("malware", "マルウェア", "backdoor", "バックドア"), "malware-campaign"),
        (("breach", "intrusion", "侵害", "侵入"), "intrusion"),
        (("campaign", "operation", "キャンペーン", "作戦"), "campaign"),
    )
    for terms, category in categories:
        if any(term in text for term in terms):
            return category
    return "reported-activity"


def _mentioned_profile_refs(
    profile: dict[str, Any] | None,
    category: str,
    text: str,
) -> list[str]:
    if not profile:
        return []
    items: list[dict[str, Any]]
    if category == "targets":
        items = [
            item
            for key in ("countries", "regions", "sectors", "roles")
            for item in profile.get("targets", {}).get(key, [])
        ]
    else:
        items = profile.get("capabilities", {}).get(category, [])
    refs: set[str] = set()
    folded = text.casefold()
    for item in items:
        names = [item.get("name", ""), *item.get("aliases", [])]
        if any(
            len(name.strip()) >= 4
            and re.search(
                rf"(?<![a-z0-9]){re.escape(name.strip().casefold())}(?![a-z0-9])",
                folded,
            )
            for name in names
            if name.strip()
        ):
            refs.add(item["id"])
    return sorted(refs)


def activity_entry(
    record: dict[str, Any],
    evidence_refs: list[str],
    profile: dict[str, Any] | None = None,
) -> dict[str, Any]:
    first, last = activity_bounds(record)
    text = (
        f"{record['activity'].get('title', '')} "
        f"{record['activity'].get('summary', '')}"
    )
    malware_refs = sorted(
        {
            ref
            for row in record.get("iocs", [])
            for ref in row.get("malware_refs", [])
        }
        | set(_mentioned_profile_refs(profile, "malware", text))
    )
    activity_type = activity_type_for(record)
    stix_object_type = default_stix_object_type(activity_type)
    reported_at = activity_reported_at(
        record, (profile or {}).get("sources", [])
    )
    modeled = {
        "activity_id": activity_id_for(record),
        "name": record["activity"]["title"],
        "activity_type": activity_type,
        "stix_object_type": stix_object_type,
        "grouping_context": (
            "suspicious-activity" if stix_object_type == "grouping" else None
        ),
        "activity_refs": [],
        "first_observed": first,
        "last_observed": last,
        "reported_at": reported_at,
        "description": record["activity"].get("summary") or "日次OSINTで報告された活動。",
        "target_refs": _mentioned_profile_refs(profile, "targets", text),
        "malware_refs": malware_refs,
        "infrastructure_refs": _mentioned_profile_refs(
            profile, "infrastructure", text
        ),
        "ttp_refs": [],
        "victim_refs": [],
        "confidence": record.get("confidence", "unknown"),
        "evidence_refs": sorted(evidence_refs),
        "analyst_notes": (
            f"日次収集レコード {record['record_id']} から取込。"
            "活動期間はレビュー済みの一次資料記載がある場合だけ設定し、"
            "ニュース公開日やIOC収集日からは推定しない。"
            + (
                " reported_atは活動期間ではなく、レビュー済みの一次資料公開日。"
                if reported_at.get("basis") != "daily-news-file-date"
                else " reported_atは活動期間ではなくtech-memo日次ファイルの日付。"
            )
            + f" 主体判定: {record.get('activity_claim', {}).get('assessment', '未記録')}。"
            + f" レビュー: {record.get('review_notes') or '記載なし'}"
        ),
    }
    diamond_profile = profile or {
        "profile_id": f"actor--{record['actor']['slug']}",
        "name": record["actor"].get("canonical_name") or record["actor"]["slug"],
        "actor": {
            "canonical_name": record["actor"].get("canonical_name")
            or record["actor"]["slug"]
        },
        "attribution": {},
        "victim_cases": [],
        "targets": {},
        "ttps": [],
    }
    modeled["diamond_model"] = build_activity_diamond(diamond_profile, modeled)
    return modeled


def capability_decision(record: dict[str, Any], name: str) -> dict[str, str]:
    for item in record.get("capability_decisions", []):
        if item.get("name", "").casefold() == name.casefold():
            return item
    return {
        "name": name,
        "status": "pending",
        "reason": "Capabilityレビューが未実施。",
    }


def _malware_lookup(profile: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for item in profile["capabilities"]["malware"]:
        result[item.get("name", "").casefold()] = item
        for alias in item.get("aliases", []):
            result[alias.casefold()] = item
    return result


def ensure_malware_capabilities(
    profile: dict[str, Any],
    record: dict[str, Any],
    evidence_refs: list[str],
) -> None:
    malware = profile["capabilities"]["malware"]
    lookup = _malware_lookup(profile)
    record_first, record_last = activity_bounds(record)
    for row in record.get("iocs", []):
        refs: set[str] = set()
        raw_malware = row.get("malware", "").strip()
        for raw_name in re.split(r"[,;|]", raw_malware):
            name = raw_name.strip()
            if name.casefold() in {"", "unknown", "n/a", "na", "none", "知られていない"}:
                continue
            match = FILE_NAME_SEARCH.search(name)
            if is_file_like(name) or match:
                continue
            decision = capability_decision(record, name)
            if decision.get("status") != "approved":
                continue
            item = lookup.get(name.casefold())
            if item is None:
                malware_type = row.get("malware_type", "").strip()
                types = (
                    [malware_type]
                    if malware_type.casefold()
                    not in {"", "unknown", "n/a", "na", "none"}
                    else []
                )
                item = {
                    "id": f"malware--daily-{stable_digest(name)[:20]}",
                    "name": name,
                    "aliases": [],
                    "types": types,
                    "description": (
                        f"{profile['actor']['canonical_name']}との直接的な利用関係が"
                        "一次資料レビューで確認されたマルウェア。"
                    ),
                    "first_observed": record_first,
                    "last_observed": record_last,
                    "confidence": record.get("confidence", "unknown"),
                    "evidence_refs": sorted(evidence_refs),
                    "analyst_notes": decision.get("reason", ""),
                }
                malware.append(item)
                lookup[name.casefold()] = item
            elif item["id"].startswith("malware--daily-"):
                malware_type = row.get("malware_type", "").strip()
                confidence_rank = {
                    "unknown": 0,
                    "low": 1,
                    "medium": 2,
                    "high": 3,
                }
                confidence_values = {
                    item.get("confidence", "unknown"),
                    record.get("confidence", "unknown"),
                }
                item.update(
                    {
                        "types": sorted(
                            set(item.get("types", []))
                            | (
                                {malware_type}
                                if malware_type.casefold()
                                not in {"", "unknown", "n/a", "na", "none"}
                                else set()
                            )
                        ),
                        "description": (
                            f"{profile['actor']['canonical_name']}との直接的な利用関係が"
                            "一次資料レビューで確認されたマルウェア。"
                        ),
                        "first_observed": _merge_time_point(
                            item.get("first_observed", UNKNOWN_TIME),
                            record_first,
                            latest=False,
                        ),
                        "last_observed": _merge_time_point(
                            item.get("last_observed", UNKNOWN_TIME),
                            record_last,
                            latest=True,
                        ),
                        "confidence": min(
                            confidence_values,
                            key=lambda value: confidence_rank.get(value, 0),
                        ),
                        "evidence_refs": sorted(
                            set(item.get("evidence_refs", [])) | set(evidence_refs)
                        ),
                        "analyst_notes": " | ".join(
                            sorted(
                                {
                                    value
                                    for value in (
                                        item.get("analyst_notes", ""),
                                        decision.get("reason", ""),
                                    )
                                    if value
                                }
                            )
                        ),
                    }
                )
            else:
                item["evidence_refs"] = sorted(
                    set(item.get("evidence_refs", [])) | set(evidence_refs)
                )
            refs.add(item["id"])
        row["malware_refs"] = sorted(refs)


def minmax_time(observations: list[dict[str, Any]], latest: bool) -> dict[str, Any]:
    known = [
        item["observed_at"] for item in observations if item["observed_at"].get("value")
    ]
    if not known:
        return dict(UNKNOWN_TIME)
    return (max if latest else min)(known, key=lambda item: item["value"])


def _merge_time_point(
    left: dict[str, Any], right: dict[str, Any], *, latest: bool
) -> dict[str, Any]:
    known = [item for item in (left, right) if item.get("value")]
    if not known:
        return dict(UNKNOWN_TIME)
    return dict((max if latest else min)(known, key=lambda item: item["value"]))


def add_dataset_source(
    dataset: dict[str, Any],
    record: dict[str, Any],
    source: dict[str, str],
    preferred_sources: list[dict[str, Any]] | None = None,
) -> str:
    source_id = source_id_for_url(
        source,
        [*(preferred_sources or []), *dataset.get("sources", [])],
    )
    preferred_source = next(
        (
            item
            for item in preferred_sources or []
            if item.get("source_id") == source_id
            and canonical_source_url(
                item.get("url") or item.get("path") or ""
            )
            == canonical_source_url(source["url"])
        ),
        None,
    )
    preferred_published = (
        preferred_source.get("published_at", UNKNOWN_TIME)
        if preferred_source
        else UNKNOWN_TIME
    )
    if preferred_published.get("status") in {"known", "inferred"} and preferred_published.get(
        "value"
    ):
        # A canonical profile Source owns publication metadata even when the
        # daily IOC row references it as an auxiliary ``ioc-reference``.
        published = dict(preferred_published)
    elif (
        source["source_type"] == "primary-report"
        and canonical_source_url(source["url"])
        == canonical_source_url(activity_reference(record))
    ):
        published = activity_reported_at(record, preferred_sources)
    elif source["source_type"] == "primary-report":
        published = time_point(
            source.get("news_date") or record["activity"].get("news_date"),
            "daily-news-file-date",
        )
    else:
        published = dict(UNKNOWN_TIME)
    modeled = {
        "source_id": source_id,
        "path": source["url"],
        "published_at": published,
        "confidence": source_reliability(source["url"]),
        "tlp": "TLP:CLEAR",
        "analyst_notes": (
            "source confidenceは出典信頼性であり、アクター帰属確度ではない。"
        ),
    }
    source_indexes = {
        item["source_id"]: index
        for index, item in enumerate(dataset["sources"])
    }
    if source_id in source_indexes:
        existing_source = dataset["sources"][source_indexes[source_id]]
        if source_id.startswith("source--daily-"):
            dataset["sources"][source_indexes[source_id]] = modeled
        else:
            # Keep analyst-curated metadata when the daily record references the
            # same canonical URL under an existing non-daily Source identity,
            # while allowing a reviewed date to fill an unknown date.
            dataset["sources"][source_indexes[source_id]] = merge_materialized_source(
                existing_source, modeled
            )
    else:
        dataset["sources"].append(modeled)
    return source_id


def merge_duplicate_observations(
    existing: dict[str, Any], incoming: dict[str, Any]
) -> dict[str, Any]:
    """Merge one logical observation without discarding curated context."""
    merged = {**existing, **incoming}
    for field in (
        "campaign_refs",
        "malware_refs",
        "infrastructure_refs",
        "roles",
    ):
        merged[field] = sorted(
            set(existing.get(field, [])) | set(incoming.get(field, []))
        )
    confidence_rank = {"unknown": 0, "low": 1, "medium": 2, "high": 3}
    merged["confidence"] = min(
        (
            existing.get("confidence", "unknown"),
            incoming.get("confidence", "unknown"),
        ),
        key=lambda item: confidence_rank.get(item, 0),
    )
    for field in ("context_excerpt", "analyst_notes"):
        values = {
            part.strip()
            for value in (existing.get(field, ""), incoming.get(field, ""))
            for part in value.split(" | ")
            if part.strip()
        }
        merged[field] = " | ".join(sorted(values))
    existing_time = existing.get("observed_at", UNKNOWN_TIME)
    incoming_time = incoming.get("observed_at", UNKNOWN_TIME)
    if not incoming_time.get("value") and existing_time.get("value"):
        merged["observed_at"] = dict(existing_time)
    return merged


INGEST_EXTRACTION_METHODS = frozenset(
    {"csv-row", "pdf-text", "text-line", "xlsx-row"}
)
DAILY_IOC_EXTRACTION_METHOD = "tech-memo-structured-csv"
DAILY_ARTIFACT_EXTRACTION_METHOD = "tech-memo-reviewed-artifact"


def _ingest_location_json(location: Any) -> str:
    if not isinstance(location, dict):
        raise ValueError("ingest observation requires an object source_location")
    return json.dumps(location, sort_keys=True)


def migrated_ioc_observation_id(
    observation: dict[str, Any],
    indicator: dict[str, Any],
    actor_ref: str,
    selected_source_id: str,
    common: Any,
) -> str:
    """Recreate an IOC observation ID with its original generator contract."""
    method = observation.get("extraction_method")
    if method == DAILY_IOC_EXTRACTION_METHOD:
        location = observation.get("source_location")
        if not isinstance(location, dict):
            raise ValueError(
                "tech-memo IOC observation requires an object source_location"
            )
        observed = observation.get("observed_at") or {}
        observed_date = (
            observed.get("value", "")[:10]
            if observed.get("status") in {"known", "inferred"}
            and observed.get("value")
            else ""
        )
        return common.stable_id(
            "observation",
            actor_ref,
            indicator["type"],
            indicator["normalized_value"],
            selected_source_id,
            location.get("path", ""),
            str(location.get("row") or ""),
            observed_date,
        )
    if method in INGEST_EXTRACTION_METHODS:
        return common.stable_id(
            "observation",
            actor_ref,
            indicator["type"],
            observation.get("hash_algorithm") or "",
            indicator["normalized_value"],
            selected_source_id,
            _ingest_location_json(observation.get("source_location")),
        )
    raise ValueError(
        f"unsupported IOC extraction_method for Source migration: {method!r}"
    )


def _daily_artifact_record_id(row: dict[str, str]) -> str:
    match = re.search(
        r"(?:^|(?:\s*[;|]\s*))daily record:\s*([^;|]+)",
        row.get("analyst_notes", ""),
    )
    if not match:
        raise ValueError(
            "tech-memo artifact observation lacks its daily record ID"
        )
    return match.group(1).strip()


def migrated_artifact_observation_id(
    row: dict[str, str],
    selected_source_id: str,
    common: Any,
) -> str:
    """Recreate an artifact observation ID with its original generator contract."""
    method = row.get("extraction_method")
    if method == DAILY_ARTIFACT_EXTRACTION_METHOD:
        return common.stable_id(
            "observation",
            row["actor_ref"],
            row["artifact_type"],
            row["normalized_value"],
            selected_source_id,
            _daily_artifact_record_id(row),
        )
    if method in INGEST_EXTRACTION_METHODS:
        try:
            location = json.loads(row.get("source_location", ""))
        except json.JSONDecodeError as exc:
            raise ValueError(
                "ingest artifact observation has invalid source_location JSON"
            ) from exc
        return common.stable_id(
            "observation",
            row["actor_ref"],
            row["artifact_type"],
            row["normalized_value"],
            selected_source_id,
            _ingest_location_json(location),
        )
    raise ValueError(
        f"unsupported artifact extraction_method for Source migration: {method!r}"
    )


def source_identity_migration_issues(
    dataset: dict[str, Any],
    artifact_rows: list[dict[str, str]],
    source_id_map: dict[str, str],
    common: Any,
) -> list[str]:
    """Return unsafe cross-file Source migrations before any write begins."""
    issues: list[str] = []
    actor_ref = dataset.get("actor_ref", "")
    for indicator in dataset.get("indicators", []):
        for observation in indicator.get("observations", []):
            old_id = observation.get("source_id")
            if old_id not in source_id_map:
                continue
            try:
                migrated_ioc_observation_id(
                    observation,
                    indicator,
                    actor_ref,
                    source_id_map[old_id],
                    common,
                )
            except (KeyError, TypeError, ValueError) as exc:
                issues.append(
                    f"IOC {observation.get('observation_id', '<unknown>')}: {exc}"
                )
            for field in (
                "campaign_refs",
                "malware_refs",
                "infrastructure_refs",
                "roles",
            ):
                refs = observation.get(field, [])
                if not isinstance(refs, list) or not all(
                    isinstance(ref, str) for ref in refs
                ):
                    issues.append(
                        f"IOC {observation.get('observation_id', '<unknown>')}: "
                        f"{field} must be an array of strings"
                    )
    for row in artifact_rows:
        old_id = row.get("source_id")
        if old_id not in source_id_map:
            continue
        try:
            migrated_artifact_observation_id(row, source_id_map[old_id], common)
        except (KeyError, TypeError, ValueError) as exc:
            issues.append(
                f"artifact {row.get('observation_id', '<unknown>')}: {exc}"
            )
        for field in (
            "campaign_refs",
            "malware_refs",
            "infrastructure_refs",
            "roles",
        ):
            try:
                _json_array_values(row.get(field, ""))
            except (TypeError, ValueError) as exc:
                issues.append(
                    f"artifact {row.get('observation_id', '<unknown>')}: "
                    f"{field}: {exc}"
                )
    return issues


def profile_source_identity_migration_issues(
    profile: dict[str, Any], source_id_map: dict[str, str]
) -> list[str]:
    """Validate direct profile Source-ID replacement for rebuild preflight."""
    issues: list[str] = []
    source_ids = [
        source.get("source_id") for source in profile.get("sources", [])
    ]
    for source_id in set(source_ids):
        if source_id and source_ids.count(source_id) > 1:
            issues.append(f"duplicate Source ID in profile: {source_id}")
    for old_id, new_id in source_id_map.items():
        if new_id not in source_ids:
            issues.append(
                f"canonical Source {new_id} required for migration of {old_id} "
                "is missing from profile"
            )
    return issues


def migrate_profile_source_identities(
    profile: dict[str, Any], source_id_map: dict[str, str]
) -> None:
    """Replace retained profile refs before removing daily-owned Sources."""
    if not source_id_map:
        return
    issues = profile_source_identity_migration_issues(profile, source_id_map)
    if issues:
        raise ValueError("; ".join(issues))
    profile["sources"] = [
        source
        for source in profile.get("sources", [])
        if source.get("source_id") not in source_id_map
    ]
    _replace_exact_ids(profile, source_id_map)


def source_manifest_migration_issues(
    manifest: Any, source_id_map: dict[str, str]
) -> list[str]:
    """Validate an IOC source manifest before replacing explicit Source IDs."""
    if not isinstance(manifest, dict):
        return ["ioc-sources.json root must be an object"]
    issues: list[str] = []
    defaults = manifest.get("defaults", {})
    if not isinstance(defaults, dict):
        issues.append("ioc-sources.json defaults must be an object")
        defaults = {}
    sources = manifest.get("sources", [])
    valid_sources: list[dict[str, Any]] = []
    if not isinstance(sources, list):
        issues.append("ioc-sources.json sources must be an array")
    else:
        for index, source in enumerate(sources):
            if not isinstance(source, dict):
                issues.append(f"ioc-sources.json sources[{index}] must be an object")
                continue
            if not isinstance(source.get("source_id"), str):
                issues.append(
                    f"ioc-sources.json sources[{index}].source_id must be a string"
                )
            if not isinstance(source.get("path"), str) or not source.get("path"):
                issues.append(
                    f"ioc-sources.json sources[{index}].path must be a non-empty string"
                )
            if "field_map" in source and not isinstance(source["field_map"], dict):
                issues.append(
                    f"ioc-sources.json sources[{index}].field_map must be an object"
                )
            if isinstance(source.get("source_id"), str):
                valid_sources.append(source)

    # Multiple evidence paths may intentionally converge on one Source ID, but
    # identity-level metadata must remain ingestible after that migration.
    grouped_sources: dict[str, list[dict[str, Any]]] = {}
    for source in valid_sources:
        selected_id = source_id_map.get(source["source_id"], source["source_id"])
        effective = dict(defaults)
        effective.update(
            {key: value for key, value in source.items() if value is not None}
        )
        grouped_sources.setdefault(selected_id, []).append(effective)
    for source_id, source_group in grouped_sources.items():
        publications = {
            json.dumps(point, ensure_ascii=False, sort_keys=True)
            for source in source_group
            if (
                (point := normalize_profile_time(
                    source.get("published_at"), basis="source-publication"
                )).get("status")
                != "unknown"
                and point.get("value")
            )
        }
        if len(publications) > 1:
            issues.append(
                f"ioc-sources.json Source {source_id} has conflicting "
                "published_at metadata after migration"
            )
        for field in ("confidence", "tlp"):
            values = {
                str(source.get(field))
                for source in source_group
                if source.get(field) is not None
                and str(source.get(field)).casefold() not in {"", "unknown"}
            }
            if len(values) > 1:
                issues.append(
                    f"ioc-sources.json Source {source_id} has conflicting "
                    f"{field} metadata after migration"
                )

    groups = manifest.get("source_groups", [])
    if not isinstance(groups, list):
        issues.append("ioc-sources.json source_groups must be an array")
        groups = []
    for index, group in enumerate(groups):
        if not isinstance(group, dict):
            issues.append(
                f"ioc-sources.json source_groups[{index}] must be an object"
            )
            continue
        prefix = group.get("source_id_prefix")
        path_glob = group.get("path_glob")
        if not isinstance(prefix, str) or not prefix:
            issues.append(
                f"ioc-sources.json source_groups[{index}].source_id_prefix "
                "must be a non-empty string"
            )
            continue
        if not isinstance(path_glob, str) or not path_glob:
            issues.append(
                f"ioc-sources.json source_groups[{index}].path_glob "
                "must be a non-empty string"
            )
        if "field_map" in group and not isinstance(group["field_map"], dict):
            issues.append(
                f"ioc-sources.json source_groups[{index}].field_map must be an object"
            )
        generated_id = re.compile(rf"^{re.escape(prefix)}--[0-9a-f]{{16}}$")
        for old_id in source_id_map:
            if generated_id.fullmatch(old_id):
                issues.append(
                    f"ioc-sources.json source_groups[{index}] can regenerate "
                    f"mapped Source {old_id}; migrate the group explicitly"
                )
    for old_id, new_id in source_id_map.items():
        if old_id == new_id:
            issues.append(f"Source migration maps {old_id} to itself")
        if new_id in source_id_map:
            issues.append(
                f"Source migration chain/collision is unsafe: {old_id} -> {new_id}"
            )
    return issues


def migrate_source_manifest(
    manifest: dict[str, Any], source_id_map: dict[str, str]
) -> None:
    """Replace only explicit manifest Source IDs, preserving every entry."""
    issues = source_manifest_migration_issues(manifest, source_id_map)
    if issues:
        raise ValueError("; ".join(issues))
    for source in manifest.get("sources", []):
        source_id = source["source_id"]
        if source_id in source_id_map:
            source["source_id"] = source_id_map[source_id]


def _json_array_values(value: str) -> set[str]:
    try:
        parsed = json.loads(value or "[]")
    except (json.JSONDecodeError, TypeError) as exc:
        raise ValueError("must contain a JSON array") from exc
    if not isinstance(parsed, list) or not all(
        isinstance(item, str) for item in parsed
    ):
        raise ValueError("must contain a JSON array of strings")
    return set(parsed)


def merge_duplicate_artifact_rows(
    existing: dict[str, str], incoming: dict[str, str], common: Any
) -> dict[str, str]:
    merged = {**existing, **incoming}
    for field in (
        "campaign_refs",
        "malware_refs",
        "infrastructure_refs",
        "roles",
    ):
        values = _json_array_values(existing.get(field, "")) | _json_array_values(
            incoming.get(field, "")
        )
        merged[field] = common.json_array_cell(sorted(values))
    campaign_count = len(_json_array_values(merged.get("campaign_refs", "")))
    merged["campaign_count"] = str(campaign_count)
    merged["seen_in_multiple_campaigns"] = (
        "true" if campaign_count > 1 else "false"
    )
    confidence_rank = {"unknown": 0, "low": 1, "medium": 2, "high": 3}
    merged["confidence"] = min(
        (existing.get("confidence", "unknown"), incoming.get("confidence", "unknown")),
        key=lambda item: confidence_rank.get(item, 0),
    )
    for field in ("context_excerpt", "analyst_notes"):
        values = {
            part.strip()
            for value in (existing.get(field, ""), incoming.get(field, ""))
            for part in value.split(" | ")
            if part.strip()
        }
        merged[field] = " | ".join(sorted(values))
    if not incoming.get("observed_at") and existing.get("observed_at"):
        for field in (
            "observed_at",
            "observed_at_precision",
            "observed_at_status",
            "observed_at_basis",
        ):
            merged[field] = existing.get(field, "")
    return merged


def migrate_cross_file_source_identities(
    dataset: dict[str, Any],
    artifact_rows: list[dict[str, str]],
    source_id_map: dict[str, str],
    preferred_sources: list[dict[str, Any]],
    common: Any,
) -> list[dict[str, str]]:
    """Propagate profile Source reconciliation into IOC and artifact outputs."""
    if not source_id_map:
        return artifact_rows
    issues = source_identity_migration_issues(
        dataset, artifact_rows, source_id_map, common
    )
    if issues:
        raise ValueError("; ".join(issues))
    published_by_id = {
        source.get("source_id"): source.get("published_at") or UNKNOWN_TIME
        for source in preferred_sources
    }

    migrated_sources: dict[str, dict[str, Any]] = {}
    for original in dataset.get("sources", []):
        source = dict(original)
        old_id = source.get("source_id")
        selected_source_id = source_id_map.get(old_id, old_id)
        source["source_id"] = selected_source_id
        published = published_by_id.get(selected_source_id)
        if published and published.get("value"):
            source["published_at"] = dict(published)
        if selected_source_id in migrated_sources:
            if old_id in source_id_map:
                source = merge_materialized_source(
                    migrated_sources[selected_source_id], source
                )
            else:
                source = merge_materialized_source(
                    source, migrated_sources[selected_source_id]
                )
        migrated_sources[selected_source_id] = source
    for selected_source_id in sorted(set(source_id_map.values())):
        if selected_source_id in migrated_sources:
            continue
        preferred = next(
            (
                item
                for item in preferred_sources
                if item.get("source_id") == selected_source_id
            ),
            None,
        )
        if preferred:
            migrated_sources[selected_source_id] = {
                "source_id": selected_source_id,
                "path": preferred.get("url") or preferred.get("path") or "",
                "published_at": dict(
                    preferred.get("published_at") or UNKNOWN_TIME
                ),
                "confidence": preferred.get("reliability", "unknown"),
                "tlp": preferred.get("tlp", "TLP:CLEAR"),
                "analyst_notes": preferred.get("analyst_notes", ""),
            }
    dataset["sources"] = list(migrated_sources.values())

    actor_ref = dataset["actor_ref"]
    for indicator in dataset.get("indicators", []):
        migrated_observations: dict[str, dict[str, Any]] = {}
        for original in indicator.get("observations", []):
            observation = dict(original)
            old_id = observation.get("source_id")
            if old_id in source_id_map:
                selected_source_id = source_id_map[old_id]
                observation["source_id"] = selected_source_id
                published = published_by_id.get(selected_source_id)
                if published:
                    observation["source_published_at"] = dict(published)
                observation["observation_id"] = migrated_ioc_observation_id(
                    observation,
                    indicator,
                    actor_ref,
                    selected_source_id,
                    common,
                )
            observation_id = observation["observation_id"]
            if observation_id in migrated_observations:
                migrated_observations[observation_id] = merge_duplicate_observations(
                    migrated_observations[observation_id], observation
                )
            else:
                migrated_observations[observation_id] = observation
        indicator["observations"] = list(migrated_observations.values())
        if indicator["observations"]:
            refresh_indicator(indicator)

    migrated_artifacts: dict[str, dict[str, str]] = {}
    for original in artifact_rows:
        row = dict(original)
        old_id = row.get("source_id")
        if old_id in source_id_map:
            selected_source_id = source_id_map[old_id]
            row["source_id"] = selected_source_id
            published = published_by_id.get(selected_source_id)
            if published:
                row["source_published_at"] = published.get("value") or ""
            row["observation_id"] = migrated_artifact_observation_id(
                row, selected_source_id, common
            )
        observation_id = row["observation_id"]
        if observation_id in migrated_artifacts:
            migrated_artifacts[observation_id] = merge_duplicate_artifact_rows(
                migrated_artifacts[observation_id], row, common
            )
        else:
            migrated_artifacts[observation_id] = row
    return list(migrated_artifacts.values())


def reconcile_dataset_source_identity(
    dataset: dict[str, Any],
    source: dict[str, Any],
    selected_source_id: str,
    common: Any,
) -> set[str]:
    """Migrate same-URL daily Source observations without duplicating them."""
    url = source.get("url") or source.get("path") or ""
    canonical_url = canonical_source_url(url)
    old_ids = {
        item["source_id"]
        for item in dataset.get("sources", [])
        if canonical_url
        and canonical_source_url(item.get("url") or item.get("path") or "")
        == canonical_url
        and item.get("source_id") != selected_source_id
        and item.get("source_id", "").startswith("source--daily-")
    }
    selected_source = next(
        item
        for item in dataset.get("sources", [])
        if item.get("source_id") == selected_source_id
    )
    published = selected_source.get("published_at", UNKNOWN_TIME)
    actor_ref = dataset["actor_ref"]

    for indicator in dataset.get("indicators", []):
        migrated: dict[str, dict[str, Any]] = {}
        for original in indicator.get("observations", []):
            observation = dict(original)
            is_old_source = observation.get("source_id") in old_ids
            is_selected_source = (
                observation.get("source_id") == selected_source_id
                and canonical_source_url(observation.get("source_path", ""))
                == canonical_url
            )
            if is_old_source or is_selected_source:
                observation["source_id"] = selected_source_id
                observation["source_published_at"] = dict(published)
            if is_old_source or (old_ids and is_selected_source):
                observation["observation_id"] = migrated_ioc_observation_id(
                    observation,
                    indicator,
                    actor_ref,
                    selected_source_id,
                    common,
                )
            observation_id = observation["observation_id"]
            if observation_id in migrated:
                migrated[observation_id] = merge_duplicate_observations(
                    migrated[observation_id], observation
                )
            else:
                migrated[observation_id] = observation
        indicator["observations"] = list(migrated.values())
        if indicator["observations"]:
            refresh_indicator(indicator)
    dataset["sources"] = [
        item
        for item in dataset.get("sources", [])
        if item.get("source_id") not in old_ids
    ]
    return old_ids


def merge_ioc_record(
    dataset: dict[str, Any],
    record: dict[str, Any],
    queue: dict[str, Any],
    common: Any,
    preferred_sources: list[dict[str, Any]] | None = None,
) -> None:
    by_key = {
        (item["type"], item["normalized_value"]): item
        for item in dataset["indicators"]
    }
    activity_id = activity_id_for(record)
    actor_ref = dataset["actor_ref"]
    for row in record.get("iocs", []):
        kind = row["type"]
        normalized = common.normalize_observable(kind, row["value"])
        if not normalized:
            continue
        source = source_for_row(record, row, queue)
        source_id = add_dataset_source(
            dataset, record, source, preferred_sources=preferred_sources
        )
        reconcile_dataset_source_identity(dataset, source, source_id, common)
        source_published_at = next(
            item["published_at"]
            for item in dataset["sources"]
            if item["source_id"] == source_id
        )
        key = (kind, normalized)
        observation = {
            "observation_id": common.stable_id(
                "observation",
                actor_ref,
                kind,
                normalized,
                source_id,
                row.get("source_path", ""),
                str(row.get("row", "")),
                row.get("observed_date", ""),
            ),
            "observed_at": time_point(row.get("observed_date"), "daily-ioc-date"),
            "source_published_at": dict(source_published_at),
            "source_id": source_id,
            "source_path": source["url"],
            "source_location": {
                "repository": queue["source"]["repository"],
                "commit": queue["source"]["commit"],
                "path": row.get("source_path", record["activity"]["news_path"]),
                "row": row.get("row"),
            },
            "campaign_refs": [activity_id],
            "malware_refs": row.get("malware_refs", []),
            "infrastructure_refs": [],
            "roles": row.get("roles", []),
            "confidence": row.get("confidence", record.get("confidence", "unknown")),
            "tlp": "TLP:CLEAR",
            "extraction_method": "tech-memo-structured-csv",
            "raw_value": row["value"],
            "context_excerpt": row.get("description", "")[:500],
            "analyst_notes": (
                f"actor field: {row.get('actor', '')}; "
                f"actor_attribute: {row.get('actor_attribute', '')}; "
                f"reference: {row.get('reference', '')}"
            ),
        }
        if key not in by_key:
            indicator = {
                "indicator_id": common.stable_id(
                    "indicator", actor_ref, kind, normalized
                ),
                "type": kind,
                "value": row["value"],
                "normalized_value": normalized,
                "stix_pattern": common.stix_pattern(kind, normalized),
                "disposition": "confirmed",
                "first_observed": observation["observed_at"],
                "last_observed": observation["observed_at"],
                "observation_count": 1,
                "campaign_count": 1,
                "seen_in_multiple_campaigns": False,
                "campaign_refs": [activity_id],
                "malware_refs": row.get("malware_refs", []),
                "infrastructure_refs": [],
                "roles": row.get("roles", []),
                "observations": [observation],
            }
            dataset["indicators"].append(indicator)
            by_key[key] = indicator
            continue
        indicator = by_key[key]
        indexes = {
            item["observation_id"]: index
            for index, item in enumerate(indicator["observations"])
        }
        if observation["observation_id"] in indexes:
            index = indexes[observation["observation_id"]]
            indicator["observations"][index] = merge_duplicate_observations(
                indicator["observations"][index], observation
            )
        else:
            indicator["observations"].append(observation)
        refresh_indicator(indicator)


def refresh_indicator(indicator: dict[str, Any]) -> None:
    observations = indicator["observations"]
    indicator["observation_count"] = len(observations)
    for field in ("campaign_refs", "malware_refs", "infrastructure_refs", "roles"):
        indicator[field] = sorted(
            {
                ref
                for observation in observations
                for ref in observation.get(field, [])
            }
        )
    indicator["campaign_count"] = len(indicator["campaign_refs"])
    indicator["seen_in_multiple_campaigns"] = indicator["campaign_count"] > 1
    indicator["first_observed"] = minmax_time(observations, latest=False)
    indicator["last_observed"] = minmax_time(observations, latest=True)


def load_artifact_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def merge_artifacts(
    rows: list[dict[str, str]],
    record: dict[str, Any],
    queue: dict[str, Any],
    actor_ref: str,
    common: Any,
    source_id: str | None = None,
    source_published_at: dict[str, Any] | None = None,
) -> list[dict[str, str]]:
    approved = [
        item
        for item in record.get("artifacts", [])
        if item.get("review_status") == "approved"
    ]
    source = primary_source(record, queue)
    source_id = source_id or source_id_for_value(
        canonical_source_url(source["url"])
    )
    activity_id = activity_id_for(record)
    first, _ = activity_bounds(record)
    published = source_published_at or activity_reported_at(record)
    for item in approved:
        normalized = common.normalize_observable("artifact", item["value"])
        observation_id = common.stable_id(
            "observation",
            actor_ref,
            item["artifact_type"],
            normalized,
            source_id,
            record["record_id"],
        )
        modeled_row = {
                "schema_version": "1.0.0",
                "actor_ref": actor_ref,
                "artifact_id": common.stable_id(
                    "artifact", item["artifact_type"], normalized
                ),
                "observation_id": observation_id,
                "artifact_type": item["artifact_type"],
                "value": item["value"],
                "normalized_value": normalized,
                "disposition": "confirmed",
                "observed_at": first.get("value") or "",
                "observed_at_precision": first["precision"],
                "observed_at_status": first["status"],
                "observed_at_basis": first["basis"],
                "source_published_at": published.get("value") or "",
                "source_id": source_id,
                "source_path": source["url"],
                "source_location": json.dumps(
                    {
                        "repository": queue["source"]["repository"],
                        "commit": queue["source"]["commit"],
                        "path": record["activity"]["news_path"],
                    },
                    ensure_ascii=False,
                    sort_keys=True,
                ),
                "campaign_refs": common.json_array_cell([activity_id]),
                "malware_refs": common.json_array_cell([]),
                "infrastructure_refs": common.json_array_cell([]),
                "roles": common.json_array_cell([]),
                "campaign_count": "1",
                "seen_in_multiple_campaigns": "false",
                "confidence": record.get("confidence", "unknown"),
                "tlp": "TLP:CLEAR",
                "extraction_method": "tech-memo-reviewed-artifact",
                "context_excerpt": item.get("context", "")[:500],
                "analyst_notes": f"daily record: {record['record_id']}",
            }
        exact_indexes = [
            index
            for index, row in enumerate(rows)
            if row.get("observation_id") == observation_id
        ]
        semantic_indexes = [
            index
            for index, row in enumerate(rows)
            if row.get("extraction_method") == "tech-memo-reviewed-artifact"
            and row.get("artifact_type") == item["artifact_type"]
            and row.get("normalized_value") == normalized
            and canonical_source_url(row.get("source_path", ""))
            == canonical_source_url(source["url"])
            and row.get("analyst_notes") == f"daily record: {record['record_id']}"
        ]
        matching_indexes = set(exact_indexes) | set(semantic_indexes)
        if not matching_indexes:
            rows.append(modeled_row)
        else:
            # Prefer the already-current row's position when present, then
            # remove every stale daily-ID or duplicate semantic observation.
            # Re-materialization must not undo the conservative union performed
            # by Source-ID migration immediately beforehand.
            replacement_index = (
                exact_indexes[0] if exact_indexes else min(matching_indexes)
            )
            merged_row = modeled_row
            for index in sorted(matching_indexes):
                merged_row = merge_duplicate_artifact_rows(
                    rows[index], merged_row, common
                )
            rows[replacement_index] = merged_row
            rows[:] = [
                row
                for index, row in enumerate(rows)
                if index == replacement_index or index not in matching_indexes
            ]
    return rows


def remove_daily_materialization(
    profile: dict[str, Any],
    dataset: dict[str, Any],
    artifact_rows: list[dict[str, str]],
    source_manifest: dict[str, Any] | None = None,
) -> list[dict[str, str]]:
    dependency_issues = daily_rebuild_dependency_issues(
        profile, dataset, artifact_rows, source_manifest
    )
    if dependency_issues:
        preview = "; ".join(dependency_issues[:10])
        raise ValueError(
            "daily rebuild would remove evidence still referenced by retained "
            f"claims ({len(dependency_issues)} reference(s)): {preview}"
        )
    daily_activity_refs = {
        item["activity_id"]
        for item in profile.get("activities", [])
        if item["activity_id"].startswith("activity--daily-")
    }
    profile["sources"] = [
        item
        for item in profile.get("sources", [])
        if not item["source_id"].startswith("source--daily-")
    ]
    profile["activities"] = [
        item
        for item in profile.get("activities", [])
        if not item["activity_id"].startswith("activity--daily-")
    ]
    profile["capabilities"]["malware"] = [
        item
        for item in profile["capabilities"]["malware"]
        if not item["id"].startswith("malware--daily-")
    ]
    profile["ttps"] = [
        item
        for item in profile.get("ttps", [])
        if not (
            item.get("ttp_id", "").startswith("ttp--activity-rule--")
            and set(item.get("activity_refs", [])) & daily_activity_refs
        )
    ]
    profile["victim_cases"] = [
        item
        for item in profile.get("victim_cases", [])
        if not (set(item.get("activity_refs", [])) & daily_activity_refs)
    ]
    _remove_daily_refs(profile)

    dataset["sources"] = [
        item
        for item in dataset.get("sources", [])
        if not item["source_id"].startswith("source--daily-")
    ]
    dataset["indicators"] = _retained_non_daily_indicators(dataset)
    return [
        row
        for row in artifact_rows
        if not row.get("extraction_method", "").startswith("tech-memo-")
    ]


def _daily_refs_with_paths(value: Any, path: str) -> list[str]:
    """Return exact daily-owned identifiers contained in a retained value."""
    issues: list[str] = []
    if isinstance(value, dict):
        for key, item in value.items():
            issues.extend(_daily_refs_with_paths(item, f"{path}.{key}"))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            issues.extend(_daily_refs_with_paths(item, f"{path}[{index}]"))
    elif isinstance(value, str):
        if value.startswith(DAILY_ID_PREFIXES):
            issues.append(f"{path} -> {value}")
        elif "--daily-" in value:
            # CSV JSON-array cells are strings. Restrict matching to an ID-like
            # token so ordinary prose mentioning the daily workflow is ignored.
            issues.extend(
                f"{path} -> {match.group(0)}"
                for match in DAILY_ID_SEARCH.finditer(value)
            )
    return issues


def _retained_non_daily_indicators(
    dataset: dict[str, Any],
) -> list[dict[str, Any]]:
    """Drop daily observations and rebuild every retained indicator aggregate."""
    retained_indicators: list[dict[str, Any]] = []
    for original in dataset.get("indicators", []):
        retained_observations = [
            item
            for item in original.get("observations", [])
            if not item.get("extraction_method", "").startswith("tech-memo-")
        ]
        if not retained_observations:
            continue
        indicator = {**original, "observations": retained_observations}
        refresh_indicator(indicator)
        retained_indicators.append(indicator)
    return retained_indicators


def daily_rebuild_dependency_issues(
    profile: dict[str, Any],
    dataset: dict[str, Any],
    artifact_rows: list[dict[str, str]],
    source_manifest: dict[str, Any] | None = None,
) -> list[str]:
    """Find retained claims that depend on materialization-owned daily IDs.

    A full-history rebuild may replace daily Sources, Activities, malware, IOC
    observations, and artifact rows. It must not silently strip those IDs from
    analyst-curated aliases, relationships, targeting, pivots, or other retained
    claims. Until each such claim has a stable curated evidence identity, the
    rebuild is rejected before any file is written.
    """
    daily_activity_refs = {
        item.get("activity_id", "")
        for item in profile.get("activities", [])
        if item.get("activity_id", "").startswith("activity--daily-")
    }
    retained_profile: dict[str, Any] = {}
    for key, value in profile.items():
        if key == "sources":
            retained_profile[key] = [
                item
                for item in value
                if not item.get("source_id", "").startswith("source--daily-")
            ]
        elif key == "activities":
            retained_profile[key] = [
                item
                for item in value
                if not item.get("activity_id", "").startswith("activity--daily-")
            ]
        elif key == "capabilities" and isinstance(value, dict):
            retained_profile[key] = {
                **value,
                "malware": [
                    item
                    for item in value.get("malware", [])
                    if not item.get("id", "").startswith("malware--daily-")
                ],
            }
        elif key == "ttps" and isinstance(value, list):
            retained_profile[key] = [
                item
                for item in value
                if not (
                    item.get("ttp_id", "").startswith("ttp--activity-rule--")
                    and set(item.get("activity_refs", [])) & daily_activity_refs
                )
            ]
        elif key == "victim_cases" and isinstance(value, list):
            retained_profile[key] = [
                item
                for item in value
                if not set(item.get("activity_refs", [])) & daily_activity_refs
            ]
        else:
            retained_profile[key] = value

    retained_dataset = {
        key: value
        for key, value in dataset.items()
        if key not in {"sources", "indicators"}
    }
    retained_dataset["sources"] = [
        item
        for item in dataset.get("sources", [])
        if not item.get("source_id", "").startswith("source--daily-")
    ]
    retained_dataset["indicators"] = _retained_non_daily_indicators(dataset)

    retained_artifacts = [
        row
        for row in artifact_rows
        if not row.get("extraction_method", "").startswith("tech-memo-")
    ]
    issues = [
        *_daily_refs_with_paths(retained_profile, "profile"),
        *_daily_refs_with_paths(retained_dataset, "iocs"),
        *_daily_refs_with_paths(retained_artifacts, "artifacts"),
        *_daily_refs_with_paths(source_manifest or {}, "ioc-sources"),
    ]
    return sorted(set(issues))


def _remove_daily_refs(value: Any) -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            if isinstance(item, list) and key.endswith("_refs"):
                value[key] = [
                    ref
                    for ref in item
                    if not (
                        isinstance(ref, str)
                        and ref.startswith(
                            ("source--daily-", "activity--daily-", "malware--daily-")
                        )
                    )
                ]
            else:
                _remove_daily_refs(item)
    elif isinstance(value, list):
        for item in value:
            _remove_daily_refs(item)


def finalize_dataset(dataset: dict[str, Any]) -> None:
    dataset["indicators"] = [
        item for item in dataset["indicators"] if item.get("observations")
    ]
    ingestion = dataset.setdefault("ingestion", {})
    ingestion["source_count"] = len(dataset["sources"])
    ingestion["processed_source_count"] = len(dataset["sources"])
    ingestion["candidate_count"] = sum(
        item.get("disposition") == "candidate" for item in dataset["indicators"]
    )


def artifact_columns() -> list[str]:
    return load_json(
        REPO_ROOT / "actor_profile" / "schemas" / "artifacts-csv-columns.json"
    )["columns"]


def build_ledger(
    existing: dict[str, Any] | None,
    actor_ref: str,
    records: list[dict[str, Any]],
    source_commit: str,
    updated_at: str,
    *,
    rebuild: bool,
) -> dict[str, Any]:
    retained = {} if rebuild else {
        item["record_id"]: item
        for item in (existing or {}).get("records", [])
    }
    for record in records:
        retained[record["record_id"]] = {
            **record,
            "source_commit": source_commit,
        }
    return {
        "schema_version": "2.0.0",
        "actor_ref": actor_ref,
        "updated_at": updated_at,
        "records": sorted(retained.values(), key=lambda item: item["record_id"]),
    }
