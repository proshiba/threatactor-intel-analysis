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
FILE_LIKE_RE = re.compile(
    r"^[^/\\\s]+\.(?:exe|dll|sys|ps1|bat|cmd|js|jse|vbs|hta|lnk|"
    r"docm?|xlsm?|pptm?|pdf|zip|rar|7z|apk|dmg|pkg|sh|py)$",
    re.IGNORECASE,
)
LOW_QUALIFIERS = ("low confidence", "suspected", "possible", "疑い", "低信頼")
HIGH_QUALIFIERS = ("high confidence", "高信頼")
UNKNOWN_TIME = {
    "value": None,
    "precision": "unknown",
    "status": "unknown",
    "basis": "not-stated",
}
ACTIVITY_ACTION_RE = re.compile(
    r"(?:攻撃|侵害|標的|配布|展開|悪用|窃取|窃盗|強奪|使用|利用|採用|"
    r"構築|設置|感染|詐欺|暗号化|ハッキング|ハック|スパイ|諜報|フィッシング|"
    r"ランサム|マルウェア|バックドア|ボットネット|作戦|キャンペーン|"
    r"活動|インフラ|偽装|乗っ取|脅迫|データ流出|ワイパー|"
    r"\bC2\b|\btarget(?:s|ed|ing)?\b|\battack(?:s|ed|ing)?\b|"
    r"\bcampaigns?\b|\bdeploy(?:s|ed|ing)?\b|\bexploit(?:s|ed|ing)?\b|"
    r"\bmalware\b|\bransomware\b|\bphish(?:ing|ed)?\b|\bbreach(?:es|ed|ing)?\b|"
    r"\bintrusion\b|\bespionage\b|\boperations?\b|\binfrastructure\b|"
    r"\bsteal(?:s|ing)?\b|\bstole\b|\buse(?:s|d|ing)?\b|\badopt(?:s|ed|ing)?\b|"
    r"\bcompromis(?:e|es|ed|ing)\b|\bbackdoor\b)",
    re.IGNORECASE,
)
NON_OPERATIONAL_ACTIVITY_RE = re.compile(
    r"(?:逮捕|起訴|有罪|判決|禁錮|懲役|身柄|制裁|報奨金|情報提供|容疑者|"
    r"無罪を主張|罪状認否|釈放|引き渡し|首領|首謀者|レッドノーティス|"
    r"活動を停止|活動停止|"
    r"(?:年|月)の刑|"
    r"\barrest(?:s|ed)?\b|\bindict(?:s|ed|ment)?\b|\bsentenc(?:e|ed)\b|"
    r"\bconvict(?:s|ed|ion)?\b|\bextradit(?:e|ed|ion)\b|\bsanction(?:s|ed)?\b|"
    r"\bplead(?:s|ed)?\b|\bprison\b|\bcharged?\b)",
    re.IGNORECASE,
)
UNCERTAIN_OR_CONTEXT_ONLY_RE = re.compile(
    r"(?:類似|重複|後継|リブランド|可能性|かもしれない|疑われ|確証はなし|"
    r"関連があるか|関連の可能性|無関係|"
    r"本キャンペーン自体の確定帰属は不明|整合する|"
    r"低信頼で示唆|帰属は明確ではない|現時点で本件との関連は不明|"
    r"を模倣|の関係者|関係者で構成|と提携|傘下|を名乗る一味|"
    r"Scattered\s+Lapsus(?:\\\$)?\s+Hunters|"
    r"公式に特定されず|本件.{0,30}特定されず|"
    r"\bsimilar(?:ity)?\b|\boverlap(?:s|ped)?\b|\bsuccessor\b|\brebrand(?:ed)?\b|"
    r"\bmay be\b|\bpossibly\b|\buncertain\b)",
    re.IGNORECASE,
)
HISTORICAL_CONTEXT_RE = re.compile(
    r"(?:過去|以前|歴史がある|例として|挙げ|知られている|"
    r"\bpreviously\b|\bhistorically\b|\bin the past\b|\bknown to\b)",
    re.IGNORECASE,
)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def stable_digest(*parts: str) -> str:
    return hashlib.sha256("\x1f".join(parts).encode("utf-8", errors="replace")).hexdigest()


def write_json_atomic(path: Path, value: Any) -> None:
    content = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    write_text_atomic(path, content)


def write_text_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False
    ) as stream:
        stream.write(content)
        temporary = Path(stream.name)
    temporary.chmod(0o644)
    temporary.replace(path)


def write_json_if_changed(path: Path, value: Any) -> bool:
    """Write JSON only when its canonical serialized form changed."""
    content = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    write_json_atomic(path, value)
    return True


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


def source_reliability(url: str) -> str:
    """Assess source quality independently from actor-attribution confidence."""
    if not url.startswith(("http://", "https://")):
        return "low"
    return "medium"


def is_file_like(value: str) -> bool:
    return bool(FILE_LIKE_RE.fullmatch(value.strip()))


def evidence_excerpt(text: str, term: str, limit: int = 600) -> str:
    """Return the line/sentence containing an actor term for human review."""
    match = re.search(re.escape(term), text, flags=re.IGNORECASE)
    if not match:
        return ""
    starts = [
        text.rfind("\n", 0, match.start()),
        text.rfind("。", 0, match.start()),
        text.rfind(".", 0, match.start()),
    ]
    start = max(starts) + 1
    ends = [
        value
        for value in (
            text.find("\n", match.end()),
            text.find("。", match.end()),
            text.find(".", match.end()),
        )
        if value >= 0
    ]
    end = min(ends) + 1 if ends else min(len(text), match.end() + limit)
    return re.sub(r"\s+", " ", text[start:end]).strip()[:limit]


def has_direct_actor_role(excerpt: str, term: str) -> bool:
    """Check that the matched actor term, not another noun, owns the action."""
    term_re = re.escape(term)
    alias_note = r"(?:[（(][^）)]{0,80}[）)])?"
    closing = r"(?:」|』|\)|）)?"
    descriptor = (
        r"(?:と呼ばれる)?(?:[^、。]{0,24}の)?"
        r"(?:ハッカーグループ|脅威グループ|脅威アクター|ランサムウェア"
        r"(?:グループ|のアフィリエイト)?|攻撃者|ハッカー|グループ|集団|APT|"
        r"作戦|キャンペーン)?"
    )
    action = (
        r"(?:攻撃|侵害|標的|配布|展開|悪用|窃取|窃盗|強奪|使用|利用|採用|"
        r"実施|運用|構築|設置|感染|詐欺|暗号化|ハッキング|"
        r"活動|スパイ|諜報|フィッシング|ランサムウェア|マルウェア|"
        r"target|attack|campaign|deploy|exploit|malware|ransomware|use|adopt|"
        r"phish|breach|intrusion|espionage|operation|steal|compromis)"
    )
    patterns = (
        rf"{term_re}{closing}{alias_note}{descriptor}(?:が|は).{{0,100}}{action}",
        rf"{term_re}{closing}{alias_note}{descriptor}\s*[、,:：]"
        rf"(?!\s*[A-Z][A-Za-z0-9$._ -]{{2,24}}[、,/]).{{0,100}}{action}",
        rf"{term_re}{closing}{alias_note}(?:\s*APT)?(?:の)?"
        rf"(?:攻撃|活動|作戦|キャンペーン).{{0,48}}(?:が|は|の).{{0,100}}{action}",
        rf"{term_re}{closing}{alias_note}{descriptor}(?:によって|により).{{0,80}}{action}",
        rf"{term_re}.{{0,56}}(?:が関与|の関与|の背後|が実行主体)",
        rf"(?:攻撃者|攻撃主体|実行主体)(?:は|が|[:：])?"
        rf"[^、。；;はが]{{0,48}}{term_re}{closing}",
        rf"(?:攻撃|侵害|活動|キャンペーン)[^、。]{{0,48}}(?:は|が)?"
        rf"{term_re}.{{0,36}}(?:による|と特定|に帰属|とされ)",
        rf"{term_re}.{{0,40}}(?:used|targeted|deployed|attacked|breached)",
        rf"(?:used|deployed|operated|conducted).{{0,24}}by.{{0,32}}{term_re}",
        rf"(?:attributed to|tracked as|identified as).{{0,32}}{term_re}",
    )
    return any(re.search(pattern, excerpt, flags=re.IGNORECASE) for pattern in patterns)


def has_explicit_activity_attribution(excerpt: str, term: str) -> bool:
    """Check for an explicit, but not necessarily high-confidence, attribution."""
    term_re = re.escape(term)
    subject = r"(?:攻撃|侵害|活動|キャンペーン|作戦|攻撃者|脅威アクター)"
    relation = (
        r"(?:に帰属|と特定|として追跡|と関連(?:付けられ|してい|があ|する)|"
        r"に関連(?:付けられ|してい|する)|が関与|によるものとされ)"
    )
    patterns = (
        rf"{subject}.{{0,100}}{term_re}.{{0,40}}{relation}",
        rf"(?:attack|intrusion|activity|campaign|operation).{{0,100}}"
        rf"(?:attributed|linked|associated).{{0,32}}(?:to|with).{{0,32}}{term_re}",
    )
    return any(re.search(pattern, excerpt, flags=re.IGNORECASE) for pattern in patterns)


def assess_activity_claim(
    match: "ActorMatch",
    title: str,
    body: str,
    config: dict[str, Any],
) -> dict[str, Any]:
    """Assess whether collected prose states an actor-operated activity.

    This is deliberately stricter than name discovery.  It does not prove
    attribution; it records why a record is suitable for analyst approval.
    """
    location = "title" if match.reason == "news-title" else "body"
    excerpt = title if location == "title" else evidence_excerpt(body, match.term)
    unsafe = {
        normalized_name(value)
        for value in config.get("matching", {}).get("unsafe_prose_aliases", [])
    }
    reasons: list[str] = []
    assessment = "candidate"

    if normalized_name(match.term) in unsafe:
        assessment = "name-collision"
        reasons.append("一般語・製品名・地域名と衝突しやすいalias")
    elif match.scope != "exact":
        assessment = "scope-review-required"
        reasons.append(f"alias scopeが{match.scope}であり同一アクターと断定できない")
    elif NON_OPERATIONAL_ACTIVITY_RE.search(title):
        assessment = "non-operational"
        reasons.append("タイトルの主題が逮捕・起訴・制裁等であり攻撃活動ではない")
    elif not ACTIVITY_ACTION_RE.search(title):
        assessment = "context-only"
        reasons.append("タイトルが攻撃・キャンペーン等の活動を主題としていない")
    elif location == "title":
        assessment = "strong-subject"
        reasons.append("exact名が活動を主題とする記事タイトルに明記されている")
    elif not excerpt:
        reasons.append("本文内の一致箇所を抽出できない")
    elif UNCERTAIN_OR_CONTEXT_ONLY_RE.search(excerpt):
        assessment = "attribution-uncertain"
        reasons.append("一致箇所が推測・類似・関連のみを示している")
    elif re.search(
        rf"{re.escape(match.term)}.{{0,32}}(?:傘下|の一部|後継|リブランド|"
        r"と重複|との重複|と類似|との類似)",
        excerpt,
        flags=re.IGNORECASE,
    ):
        assessment = "context-only"
        reasons.append("一致箇所が親子・後継・重複関係の説明に留まる")
    elif HISTORICAL_CONTEXT_RE.search(excerpt):
        assessment = "historical-reference"
        reasons.append("一致箇所が記事主題ではなく過去事例・一般的利用の説明である")
    elif re.search(r"(?:予想|見込|想定|expected to)", excerpt, flags=re.IGNORECASE):
        assessment = "forecast"
        reasons.append("一致箇所が観測済み活動ではなく将来予測である")
    elif has_direct_actor_role(excerpt, match.term):
        assessment = "strong-subject"
        reasons.append("要約の同一文でアクターが活動の実行主体として明記されている")
    elif has_explicit_activity_attribution(excerpt, match.term):
        assessment = "attributed-subject"
        reasons.append("要約の同一文で当該活動への明示的な帰属が記載されている")
    else:
        reasons.append("名前一致はあるが実行主体を示す表現が不足している")

    suggested_confidence = (
        "high"
        if assessment == "strong-subject" and location == "title"
        else "medium"
        if assessment in {"strong-subject", "attributed-subject"}
        else "low"
    )
    return {
        "assessment": assessment,
        "actor_role": (
            "operator"
            if assessment == "strong-subject"
            else "attributed-operator"
            if assessment == "attributed-subject"
            else "unknown"
        ),
        "match_location": location,
        "evidence_text": excerpt,
        "reasons": reasons,
        "suggested_confidence": suggested_confidence,
    }


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
            resolved.term.casefold().strip()
            for values in candidates.values()
            if (resolved := self._resolve(values)) and resolved.term.strip()
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
        def match_rank(value: ActorMatch) -> tuple[Any, ...]:
            return (
                value.reason != "news-title",
                value.scope != "exact",
                value.confidence not in {"high", "medium"},
                -len(value.term),
                value.term.casefold(),
            )

        title_terms = {normalized_name(match.group()) for match in self.mention_pattern.finditer(title)}
        body_terms = {normalized_name(match.group()) for match in self.mention_pattern.finditer(body)}
        for key in sorted(title_terms | body_terms):
            values = self.terms.get(key, [])
            item = self._resolve(values)
            if not item:
                continue
            reason = "news-title" if key in title_terms else "news-body"
            candidate = ActorMatch(
                item.slug, item.name, item.term, item.scope, item.confidence, reason
            )
            current = found.get(item.slug)
            if current is None or match_rank(candidate) < match_rank(current):
                found[item.slug] = candidate
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
