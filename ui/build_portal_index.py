#!/usr/bin/env python3
"""Build the portal cross-search index (spec v1) published under ui/api/v1/.

ポータル(proshiba/research_bench)は各アプリが GitHub Pages に置いた静的 JSON を
fetch して手元で索引し、同じ値が複数ソースに現れたことを検出して横串を作る。
このスクリプトは profiles/<slug>/ 配下の正規データを読み、横断検索用の
エンティティ集合へ集約する。

    python3 ui/build_portal_index.py

出力:
    ui/api/v1/meta.json    自己紹介(ポータルが最初に読む)
    ui/api/v1/search.json  索引本体

ui/data/actors.json は UI が依存しているため一切変更しない。
"""
from __future__ import annotations

import hashlib
import ipaddress
import json
import re
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PROFILES_DIR = REPO_ROOT / "profiles"
REFERENCE_HOSTS_PATH = REPO_ROOT / "actor_profile" / "reference" / "reference-hosts.json"
OUT_DIR = Path(__file__).resolve().parent / "api" / "v1"

SPEC_VERSION = "1.0"
APP_ID = "threatactor-intel-analysis"
SITE_URL = "https://proshiba.github.io/threatactor-intel-analysis/ui/"
REPOSITORY = "https://github.com/proshiba/threatactor-intel-analysis"

MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]*\)")
CITATION_RE = re.compile(r"\(Citation:[^)]*\)")
CVE_RE = re.compile(r"CVE-\d{4}-\d{4,7}", re.IGNORECASE)
TECHNIQUE_RE = re.compile(r"^T\d{4}(?:\.\d{3})?$", re.IGNORECASE)
SUMMARY_LEN = 200

# iocs.json の type から spec v1 の type 語彙へ。語彙に無い型は索引に入れない。
IOC_TYPE_MAP = {
    "md5": "ioc.md5",
    "sha1": "ioc.sha1",
    "sha256": "ioc.sha256",
    "sha512": "ioc.sha512",
    "ipv4": "ioc.ipv4",
    "ipv6": "ioc.ipv6",
    "domain": "ioc.domain",
    "url": "ioc.url",
    "email": "ioc.email",
}
# 型ごとの16進桁数。長さで検証するので、型と値の不一致（50桁の値が
# ioc.sha256 で来る等）を弾ける。HASH_TYPES はこのキー集合と同じにする。
HASH_LENGTHS = {"ioc.md5": 32, "ioc.sha1": 40, "ioc.sha256": 64, "ioc.sha512": 128}
HASH_TYPES = frozenset(HASH_LENGTHS)

# activity_type がこれらのものを campaign エンティティとして出す
CAMPAIGN_ACTIVITY_TYPES = {
    "campaign",
    "operation",
    "infrastructure-campaign",
    "cyber-espionage",
    "historical-activity-cluster",
}

# 難読化(defang)表記の復元。バリデータは defang 残りをエラーにする。
DEFANG_SUBS = [
    (re.compile(r"\[\s*\.\s*\]"), "."),
    (re.compile(r"\(\s*\.\s*\)"), "."),
    (re.compile(r"\{\s*\.\s*\}"), "."),
    (re.compile(r"\[\s*dot\s*\]", re.IGNORECASE), "."),
    (re.compile(r"\[\s*@\s*\]"), "@"),
    (re.compile(r"\(\s*@\s*\)"), "@"),
    (re.compile(r"\[\s*at\s*\]", re.IGNORECASE), "@"),
    (re.compile(r"\[\s*:\s*\]"), ":"),
    (re.compile(r"\[\s*/\s*\]"), "/"),
    (re.compile(r"h\s*x\s*x\s*p", re.IGNORECASE), "http"),
    (re.compile(r"\bmeow\b", re.IGNORECASE), "http"),
]

# domain として抽出されたがファイル名と見られる値を弾くための拡張子。
# 実在する TLD (.md=Moldova, .py=Paraguay, .sh, .io, .zip, .mov 等) は
# 誤って除外しないよう、TLD として存在しないものだけを列挙する。
NON_TLD_EXTENSIONS = {
    "txt", "html", "htm", "exe", "dll", "php", "asp", "aspx", "jsp",
    "png", "jpg", "jpeg", "gif", "bmp", "ico", "svg",
    "bin", "dat", "log", "json", "csv", "xml", "yml", "yaml",
    "xls", "xlsx", "doc", "docx", "ppt", "pptx", "pdf", "rtf",
    "bat", "ps1", "vbs", "hta", "lnk", "scr", "cpl", "sys",
    "tmp", "cfg", "ini", "conf", "sql", "db", "sqlite",
    "jar", "war", "class", "js", "css", "cpp", "hpp",
    "rar", "gz", "tgz", "bz2", "cab", "iso", "img", "msi",
    "pyc", "pyd", "ocx", "drv", "inf", "reg", "key", "pem", "crt",
}


# ---------------------------------------------------------------- helpers


def load_json(path: Path):
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def _load_reference_data(key: str) -> frozenset[str]:
    try:
        return frozenset(
            entry.strip().lower()
            for entry in load_json(REFERENCE_HOSTS_PATH).get(key, [])
            if entry.strip()
        )
    except (OSError, ValueError):
        return frozenset()


REFERENCE_HOSTS = _load_reference_data("hosts")
PUBLIC_SUFFIXES = _load_reference_data("public_suffixes")
PUBLIC_RESOLVERS = frozenset({
    "8.8.8.8", "8.8.4.4", "1.1.1.1", "1.0.0.1", "9.9.9.9", "149.112.112.112",
    "208.67.222.222", "208.67.220.220", "4.2.2.1", "4.2.2.2", "114.114.114.114",
    "223.5.5.5", "180.76.76.76", "77.88.8.8",
})
URL_HOST_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.\-]*://([^/?#:]+)")


def is_non_indicator(spec_type: str, value: str) -> bool:
    """指標として扱えない値かどうか。

    出典レポートの参考リンク、公開サフィックス単体、到達不能・予約済みアドレスを
    判定する。取り込み時(actor_profile/scripts/ingest_observables.py)と同じ一覧を
    共有する。原典レポートはリポジトリに含まれず再取り込みができないため、既に
    profiles/ に入っている分はここで落とす。取り込み側と違い、出典で難読化されて
    いたかどうかは正規化済みの値から復元できないので例外は設けない。
    """
    if spec_type in ("ioc.ipv4", "ioc.ipv6"):
        try:
            address = ipaddress.ip_address(value)
        except ValueError:
            return True
        return (
            address.is_private
            or address.is_loopback
            or address.is_reserved
            or address.is_multicast
            or address.is_unspecified
            or address.is_link_local
            or value in PUBLIC_RESOLVERS
        )
    if spec_type not in ("ioc.url", "ioc.domain", "ioc.email"):
        return False
    match = URL_HOST_RE.match(value)
    host = (match.group(1) if match else value).lower().rstrip(".")
    if "@" in host:
        host = host.rsplit("@", 1)[-1]
    if host.startswith("www."):
        host = host[4:]
    if spec_type == "ioc.domain" and host in PUBLIC_SUFFIXES:
        return True
    if host in REFERENCE_HOSTS:
        return True
    labels = host.split(".")
    return any(
        ".".join(labels[i:]) in REFERENCE_HOSTS for i in range(1, len(labels) - 1)
    )


def refang(value: str) -> str:
    """難読化表記を解除する。索引には常に生の値を入れる。"""
    for pattern, repl in DEFANG_SUBS:
        value = pattern.sub(repl, value)
    return value


def plain_text(text: str | None, limit: int = SUMMARY_LEN) -> str:
    if not text:
        return ""
    text = MD_LINK_RE.sub(r"\1", text)
    text = CITATION_RE.sub("", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > limit:
        text = text[: limit - 1].rstrip() + "…"
    return text


def name_key(name: str) -> str:
    """マルウェア名・ツール名を id 用のキーへ。ポータル側の突き合わせと同じ流儀。"""
    return re.sub(r"[^a-z0-9]+", "-", str(name).lower()).strip("-")


def short_hash(value: str) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()[:12]


def normalize_ioc(spec_type: str, value: str) -> str | None:
    """spec v1 の正規化規則を適用する。索引に入れられない値は None。"""
    value = refang(str(value or "")).strip()
    if not value:
        return None
    if spec_type == "ioc.domain":
        value = value.lower().rstrip(".")
        if "." not in value or " " in value:
            return None
        tld = value.rsplit(".", 1)[-1]
        # ファイル名の誤抽出は横串で誤結合を招くため落とす
        if tld in NON_TLD_EXTENSIONS or not tld.isalpha():
            return None
    elif spec_type == "ioc.email":
        value = value.lower()
        if "@" not in value:
            return None
    elif spec_type == "ioc.url":
        # スキームのみ小文字化。パスは大小文字が意味を持つため触らない
        value = re.sub(r"^([A-Za-z][A-Za-z0-9+.\-]*)://", lambda m: m.group(1).lower() + "://", value)
    elif spec_type in HASH_TYPES:
        value = value.lower()
        if not re.fullmatch(r"[0-9a-f]{%d}" % HASH_LENGTHS[spec_type], value):
            return None
    elif spec_type == "ioc.ipv4":
        if not re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", value):
            return None
    return value or None


# ------------------------------------------------------- per-profile read


def read_profile(slug: str) -> dict | None:
    """1 アクターぶんの素材を抽出する(ワーカープロセスで実行)。"""
    profile_dir = PROFILES_DIR / slug
    profile_path = profile_dir / "actor-profile.json"
    if not profile_path.exists():
        return None
    profile = load_json(profile_path)

    actor = profile.get("actor") or {}
    attribution = profile.get("attribution") or {}
    capabilities = profile.get("capabilities") or {}
    targets = profile.get("targets") or {}
    free_text = profile.get("free_text") or {}

    aliases: list[str] = []
    seen_alias = set()
    for alias in actor.get("aliases") or []:
        name = alias.get("name") if isinstance(alias, dict) else alias
        if name and name.lower() not in seen_alias:
            seen_alias.add(name.lower())
            aliases.append(name)

    software = []
    for kind, items in (("malware", capabilities.get("malware") or []),
                        ("tool", capabilities.get("tools") or [])):
        for item in items:
            name = (item.get("name") or "").strip()
            if not name:
                continue
            software.append({
                "kind": kind,
                "name": name,
                "ref_id": item.get("id") or "",
                "aliases": [a for a in (item.get("aliases") or []) if a and a != name],
            })

    # CVE: capabilities.vulnerabilities[] を主とし、構造化テキストからも拾う。
    # vulnerabilities[] だけでは 1 件しか取れず、脆弱性インテルとの橋にならないため。
    cves: dict[str, str] = {}  # CVE -> 出所 ("構造化" / "本文")
    for vuln in capabilities.get("vulnerabilities") or []:
        blob = f"{vuln.get('id', '')} {vuln.get('name', '')} {' '.join(vuln.get('aliases') or [])}"
        for found in CVE_RE.findall(blob):
            cves[found.upper()] = "構造化"
    text_blobs = [actor.get("description") or ""]
    text_blobs += [str(v) for v in free_text.values()]
    text_blobs += [a.get("description") or "" for a in profile.get("activities") or []]
    text_blobs += [t.get("observed_behavior") or "" for t in profile.get("ttps") or []]
    text_blobs += [s.get("description") or "" for s in
                   (capabilities.get("malware") or []) + (capabilities.get("tools") or [])]
    text_blobs += [j.get("statement") or "" for j in
                   (profile.get("assessment") or {}).get("key_judgments") or []]
    for blob in text_blobs:
        for found in CVE_RE.findall(blob):
            cves.setdefault(found.upper(), "本文")

    ttps = []
    for ttp in profile.get("ttps") or []:
        tid = (ttp.get("technique_id") or "").strip().upper()
        if TECHNIQUE_RE.fullmatch(tid):
            ttps.append({"id": tid, "name": (ttp.get("technique_name") or "").strip()})

    campaigns = []
    for act in profile.get("activities") or []:
        if (act.get("activity_type") or "") not in CAMPAIGN_ACTIVITY_TYPES:
            continue
        name = (act.get("name") or "").strip()
        if not name:
            continue
        campaigns.append({
            "name": name,
            "ref_id": act.get("activity_id") or "",
            "activity_type": act.get("activity_type") or "",
        })

    # IOC: 値ごとに畳むのは呼び出し側。ここでは正規化まで済ませる。
    iocs = []
    iocs_path = profile_dir / "iocs.json"
    if iocs_path.exists():
        for ind in load_json(iocs_path).get("indicators") or []:
            if (ind.get("disposition") or "") == "rejected":
                continue  # 誤検知として棄却済み
            spec_type = IOC_TYPE_MAP.get(ind.get("type") or "")
            if not spec_type:
                continue  # certificate-fingerprint 等、語彙に無い型
            value = normalize_ioc(spec_type, ind.get("normalized_value") or ind.get("value") or "")
            if not value:
                continue
            if is_non_indicator(spec_type, value):
                continue  # 出典レポートの参考リンク / 公開サフィックス単体
            iocs.append({
                "type": spec_type,
                "value": value,
                "disposition": ind.get("disposition") or "",
                "observations": int(ind.get("observation_count") or 0),
                "malware_refs": [r for r in (ind.get("malware_refs") or []) if r],
                "campaign_refs": [r for r in (ind.get("campaign_refs") or []) if r],
                "roles": [r for r in (ind.get("roles") or []) if r],
            })

    return {
        "slug": slug,
        "name": profile.get("name") or actor.get("canonical_name") or slug,
        "aliases": aliases,
        "actor_types": actor.get("actor_types") or [],
        "countries": attribution.get("countries") or [],
        "sponsor_type": attribution.get("sponsor_type") or "",
        "confidence": attribution.get("confidence") or "",
        "motivations": sorted({m.get("type") for m in profile.get("motivations") or [] if m.get("type")}),
        "target_countries": [
            t.get("name")
            for t in targets.get("countries") or []
            if t.get("name")
        ],
        "target_regions": [
            t.get("name")
            for t in targets.get("regions") or []
            if t.get("name")
        ],
        "sectors": [t.get("name") for t in targets.get("sectors") or [] if t.get("name")],
        "summary": plain_text(free_text.get("executive_summary") or actor.get("description")),
        "updated_at": profile.get("updated_at") or "",
        "relationships": [
            {"target": r.get("target_actor"), "rel": r.get("relationship_type") or "関連"}
            for r in profile.get("relationships") or [] if r.get("target_actor")
        ],
        "software": software,
        "cves": cves,
        "ttps": ttps,
        "campaigns": campaigns,
        "iocs": iocs,
    }


# ------------------------------------------------------------- aggregation


def build_entities(profiles: list[dict]) -> tuple[list[dict], dict[str, int]]:
    entities: list[dict] = []

    # --- actor ---------------------------------------------------------
    name_to_slug: dict[str, str] = {}
    for p in profiles:
        name_to_slug[p["name"].lower()] = p["slug"]
    for p in profiles:
        for alias in p["aliases"]:
            name_to_slug.setdefault(alias.lower(), p["slug"])

    # software id 解決用: (slug, "malware--x") -> canonical entity id
    software_ref_index: dict[tuple[str, str], str] = {}
    campaign_ref_index: dict[tuple[str, str], str] = {}

    # --- malware / tool -------------------------------------------------
    software_entities: dict[str, dict] = {}
    actor_software: dict[str, list[str]] = {}  # slug -> [entity_id]
    for p in profiles:
        for item in p["software"]:
            key = name_key(item["name"])
            if not key:
                continue
            entity_id = f"{item['kind']}:{key}"
            used = actor_software.setdefault(p["slug"], [])
            if entity_id not in used:
                used.append(entity_id)
            entry = software_entities.get(entity_id)
            if entry is None:
                entry = software_entities[entity_id] = {
                    "type": item["kind"],
                    "id": entity_id,
                    "label": item["name"],
                    "aliases": [],
                    "actors": [],
                }
            for alias in item["aliases"]:
                if alias not in entry["aliases"] and alias != entry["label"]:
                    entry["aliases"].append(alias)
            if p["slug"] not in entry["actors"]:
                entry["actors"].append(p["slug"])
            if item["ref_id"]:
                software_ref_index[(p["slug"], item["ref_id"])] = entity_id

    # --- campaign -------------------------------------------------------
    campaign_entities: dict[str, dict] = {}
    for p in profiles:
        for camp in p["campaigns"]:
            key = name_key(camp["name"])
            if not key:
                continue
            entity_id = f"campaign:{key}"
            entry = campaign_entities.get(entity_id)
            if entry is None:
                entry = campaign_entities[entity_id] = {
                    "type": "campaign",
                    "id": entity_id,
                    "label": camp["name"],
                    "activity_type": camp["activity_type"],
                    "actors": [],
                }
            if p["slug"] not in entry["actors"]:
                entry["actors"].append(p["slug"])
            if camp["ref_id"]:
                campaign_ref_index[(p["slug"], camp["ref_id"])] = entity_id

    # --- ioc ------------------------------------------------------------
    ioc_entities: dict[str, dict] = {}
    for p in profiles:
        for ioc in p["iocs"]:
            entity_id = f"ioc:{short_hash(ioc['type'] + '|' + ioc['value'])}"
            entry = ioc_entities.get(entity_id)
            if entry is None:
                entry = ioc_entities[entity_id] = {
                    "type": ioc["type"],
                    "id": entity_id,
                    "label": ioc["value"],
                    "actors": [],
                    "dispositions": set(),
                    "observations": 0,
                    "roles": [],
                    "targets": [],
                }
            if p["slug"] not in entry["actors"]:
                entry["actors"].append(p["slug"])
            entry["dispositions"].add(ioc["disposition"])
            entry["observations"] += ioc["observations"]
            for role in ioc["roles"]:
                if role not in entry["roles"]:
                    entry["roles"].append(role)
            # IOC -> マルウェア / キャンペーン(同一ファイル内 id のみ)
            for ref in ioc["malware_refs"]:
                target = software_ref_index.get((p["slug"], ref))
                if target and target not in entry["targets"]:
                    entry["targets"].append(target)
            for ref in ioc["campaign_refs"]:
                target = campaign_ref_index.get((p["slug"], ref))
                if target and target not in entry["targets"]:
                    entry["targets"].append(target)

    # --- cve / ttp ------------------------------------------------------
    cve_entities: dict[str, dict] = {}
    for p in profiles:
        for cve, origin in p["cves"].items():
            entry = cve_entities.setdefault(f"cve:{cve}", {
                "type": "cve", "id": f"cve:{cve}", "label": cve, "actors": [], "origins": set(),
            })
            if p["slug"] not in entry["actors"]:
                entry["actors"].append(p["slug"])
            entry["origins"].add(origin)

    ttp_entities: dict[str, dict] = {}
    for p in profiles:
        for ttp in p["ttps"]:
            entry = ttp_entities.setdefault(f"ttp:{ttp['id']}", {
                "type": "ttp", "id": f"ttp:{ttp['id']}", "label": ttp["id"],
                "name": ttp["name"], "actors": [],
            })
            if not entry["name"] and ttp["name"]:
                entry["name"] = ttp["name"]
            if p["slug"] not in entry["actors"]:
                entry["actors"].append(p["slug"])

    # --- emit -----------------------------------------------------------
    for p in profiles:
        attrs: dict[str, object] = {}
        if p["actor_types"]:
            attrs["種別"] = "、".join(p["actor_types"])
        if p["countries"]:
            attrs["帰属"] = "、".join(p["countries"])
        if p["confidence"]:
            attrs["確度"] = p["confidence"]
        if p["motivations"]:
            attrs["動機"] = "、".join(p["motivations"])
        if p["target_countries"]:
            attrs["標的国"] = "、".join(p["target_countries"][:16])
        if p["target_regions"]:
            attrs["標的地域"] = "、".join(p["target_regions"][:12])
        if p["sectors"]:
            attrs["標的分野"] = "、".join(p["sectors"][:8])
        if p["summary"]:
            attrs["概要"] = p["summary"]
        if p["updated_at"]:
            attrs["更新"] = p["updated_at"][:10]
        flags = []
        if p["sponsor_type"] == "state":
            flags.append("国家支援")
        if flags:
            attrs["flags"] = flags

        refs = []
        seen_ref = set()
        for rel in p["relationships"]:
            target_slug = name_to_slug.get(str(rel["target"]).lower())
            if not target_slug or target_slug == p["slug"]:
                continue
            pair = (rel["rel"], target_slug)
            if pair in seen_ref:
                continue
            seen_ref.add(pair)
            refs.append({"rel": rel["rel"], "target": f"actor:{target_slug}"})
        # アクターからも使用マルウェア/ツールへ辿れるようにする(双方向)
        for entity_id in actor_software.get(p["slug"], []):
            rel = "使用マルウェア" if entity_id.startswith("malware:") else "使用ツール"
            refs.append({"rel": rel, "target": entity_id})

        entity = {
            "type": "actor",
            "id": f"actor:{p['slug']}",
            "label": p["name"],
            "detail": p["slug"],
        }
        if p["aliases"]:
            entity["aliases"] = p["aliases"]
        if attrs:
            entity["attrs"] = attrs
        if refs:
            entity["refs"] = refs
        entities.append(entity)

    for entity_id, entry in sorted(software_entities.items()):
        item = {
            "type": entry["type"],
            "id": entity_id,
            "label": entry["label"],
        }
        if entry["aliases"]:
            item["aliases"] = entry["aliases"]
        item["attrs"] = {"使用アクター数": len(entry["actors"])}
        item["refs"] = [{"rel": "使用アクター", "target": f"actor:{s}"} for s in entry["actors"]]
        entities.append(item)

    for entity_id, entry in sorted(cve_entities.items()):
        entities.append({
            "type": "cve",
            "id": entity_id,
            "label": entry["label"],
            "attrs": {
                "関連アクター数": len(entry["actors"]),
                "抽出元": "、".join(sorted(entry["origins"])),
            },
            "refs": [{"rel": "悪用アクター", "target": f"actor:{s}"} for s in entry["actors"]],
        })

    for entity_id, entry in sorted(ttp_entities.items()):
        item = {
            "type": "ttp",
            "id": entity_id,
            "label": f"{entry['label']} {entry['name']}".strip(),
            "value": entry["label"],
            "attrs": {"使用アクター数": len(entry["actors"])},
            "refs": [{"rel": "使用アクター", "target": f"actor:{s}"} for s in entry["actors"]],
        }
        entities.append(item)

    for entity_id, entry in sorted(campaign_entities.items()):
        entities.append({
            "type": "campaign",
            "id": entity_id,
            "label": entry["label"],
            "attrs": {"活動種別": entry["activity_type"]},
            "refs": [{"rel": "実行アクター", "target": f"actor:{s}"} for s in entry["actors"]],
        })

    for entity_id, entry in sorted(ioc_entities.items()):
        attrs: dict[str, object] = {}
        dispositions = sorted(d for d in entry["dispositions"] if d)
        if dispositions:
            attrs["確度"] = "、".join(dispositions)
        if entry["observations"]:
            attrs["観測数"] = entry["observations"]
        if entry["roles"]:
            attrs["役割"] = "、".join(entry["roles"][:5])
        refs = [{"rel": "観測アクター", "target": f"actor:{s}"} for s in entry["actors"]]
        refs += [{"rel": "関連", "target": t} for t in entry["targets"]]
        item = {
            "type": entry["type"],
            "id": entity_id,
            "label": entry["label"],
        }
        if attrs:
            item["attrs"] = attrs
        if refs:
            item["refs"] = refs
        entities.append(item)

    counts: dict[str, int] = {}
    for entity in entities:
        family = entity["type"].split(".")[0]
        counts[family] = counts.get(family, 0) + 1
    return entities, counts


# ------------------------------------------------------------------- main


def write_if_changed(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text(encoding="utf-8") != content:
        path.write_text(content, encoding="utf-8")


def main() -> int:
    if not PROFILES_DIR.is_dir():
        print(f"profiles directory not found: {PROFILES_DIR}", file=sys.stderr)
        return 1

    slugs = sorted(p.name for p in PROFILES_DIR.iterdir() if p.is_dir())
    with ProcessPoolExecutor() as pool:
        profiles = [p for p in pool.map(read_profile, slugs, chunksize=8) if p]

    entities, counts = build_entities(profiles)

    # 入力が同じなら出力も同じになるよう、生成時刻はプロファイルの最新更新日時を使う
    generated_at = max((p["updated_at"] for p in profiles), default="") or None

    meta = {
        "spec_version": SPEC_VERSION,
        "app_id": APP_ID,
        "name": "アクター情報",
        "description": "公開レポートと OSINT データセットから標準化した脅威アクタープロファイルの索引。",
        "generated_at": generated_at,
        "repository": REPOSITORY,
        "site_url": SITE_URL,
        "endpoints": {"search": "api/v1/search.json"},
        "deep_links": {
            "actor": "#/actor/{detail}",
            "_graph": "#/relations/{detail}",
        },
        "capabilities": ["iframe", "deep-link", "graph"],
        "stats": counts,
        # ポータルは各アプリを iframe で表示するため、アプリ側のヘッダー・フッターが
        # ポータルのクロームと二重になる。同一オリジンなのでこの CSS を注入して隠せる。
        "embed_css": (
            ".site-header,.site-footer{display:none!important}"
            "#app{padding-top:12px}"
            ".tab-bar{top:0!important}"
        ),
    }

    search = {
        "spec_version": SPEC_VERSION,
        "app_id": APP_ID,
        "generated_at": generated_at,
        "entities": entities,
    }

    write_if_changed(OUT_DIR / "meta.json",
                     json.dumps(meta, ensure_ascii=False, indent=2) + "\n")
    write_if_changed(OUT_DIR / "search.json",
                     json.dumps(search, ensure_ascii=False, separators=(",", ":")) + "\n")

    size_kb = (OUT_DIR / "search.json").stat().st_size / 1024
    print(f"wrote {OUT_DIR}/search.json ({len(entities)} entities, {size_kb:.0f} KiB)")
    print("  " + "  ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
