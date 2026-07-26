/* Threat Actor Intelligence Profiles — GitHub Pages UI
 * Static SPA (hash routing). Data sources:
 *   - ui/data/actors.json               (build_data.py が生成する索引)
 *   - ../profiles/<slug>/actor-profile.json (詳細表示時に取得)
 *   - ../profiles/<slug>/iocs.json          (IOCタブで遅延取得)
 */
"use strict";

const REPO_URL = "https://github.com/proshiba/threatactor-intel-analysis";
const REPO_BLOB = REPO_URL + "/blob/main";
const PROFILES_BASE = "../profiles";
const LIST_PAGE = 96;
const IOC_PAGE = 200;

const TACTIC_ORDER = [
  "reconnaissance", "resource development", "initial access", "execution",
  "persistence", "privilege escalation", "defense evasion", "credential access",
  "discovery", "lateral movement", "collection", "command and control",
  "exfiltration", "impact",
];

const state = {
  index: null,          // data/actors.json payload
  currentView: null,    // "list" | "actor"
  nameToSlug: new Map(),
  filters: { q: "", country: "", sponsor: "", type: "", motivation: "", sector: "", sort: "name" },
  listLimit: LIST_PAGE,
  listScroll: 0,
  profileCache: new Map(),
  iocCache: new Map(),
};

const app = document.getElementById("app");

/* ---------- helpers ---------- */

function esc(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
}

// escape + minimal markdown ([label](url) のみリンク化、(Citation: …) は除去)
function md(text) {
  return esc(String(text ?? "").replace(/\(Citation:[^)]*\)/g, " ")).replace(
    /\[([^\]]+)\]\((https?:\/\/[^)\s]+)\)/g,
    '<a href="$2" target="_blank" rel="noopener">$1</a>'
  );
}

function fmtDate(field) {
  if (field && typeof field === "object") {
    if (field.status === "known" && field.value) return String(field.value).slice(0, 10);
    return "不明";
  }
  return field ? String(field).slice(0, 10) : "不明";
}

function confBadge(confidence) {
  const c = (confidence || "unknown").toLowerCase();
  const label = { high: "high", medium: "medium", low: "low" }[c] || "unknown";
  return `<span class="badge conf-${esc(label)}">確度: ${esc(confidence || "unknown")}</span>`;
}

function defang(value, type) {
  let v = String(value ?? "");
  if (["domain", "url", "email", "ipv4", "ipv6"].includes(type)) {
    v = v.replace(/^http/i, "hxxp").replace(/\./g, "[.]").replace(/@/g, "[@]");
  }
  return v;
}

function num(n) { return Number(n || 0).toLocaleString("ja-JP"); }

function chips(items, cls) {
  if (!items || !items.length) return '<span class="muted small">情報なし</span>';
  return '<div class="chip-list">' +
    items.map((x) => `<span class="badge ${cls || ""}">${esc(x)}</span>`).join("") +
    "</div>";
}

function section(title, bodyHtml) {
  return `<section class="section"><h2>${esc(title)}</h2>${bodyHtml}</section>`;
}

async function fetchJson(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`${url} の取得に失敗しました (HTTP ${res.status})`);
  return res.json();
}

function renderError(message) {
  app.innerHTML = `<div class="error-box"><strong>エラー:</strong> ${esc(message)}<br>
    <a href="#/">一覧へ戻る</a></div>`;
}

/* ---------- boot & routing ---------- */

async function boot() {
  try {
    const data = await fetchJson("data/actors.json");
    state.index = data;
    for (const actor of data.actors) {
      state.nameToSlug.set(actor.name.toLowerCase(), actor.slug);
      for (const alias of actor.aliases) {
        const key = alias.toLowerCase();
        if (!state.nameToSlug.has(key)) state.nameToSlug.set(key, actor.slug);
      }
    }
    const meta = document.getElementById("footer-meta");
    if (meta) meta.textContent = `索引生成: ${data.generated_at} / アクター ${num(data.stats.actors)} 件`;
    route();
  } catch (err) {
    renderError(err.message);
  }
}

function route() {
  const hash = location.hash || "#/";
  const actorMatch = hash.match(/^#\/actor\/([A-Za-z0-9._-]+)/);
  if (actorMatch) {
    if (state.currentView === "list") state.listScroll = window.scrollY;
    state.currentView = "actor";
    renderActor(decodeURIComponent(actorMatch[1]));
  } else {
    state.currentView = "list";
    renderList();
  }
}

window.addEventListener("hashchange", route);

/* ---------- list view ---------- */

function facetValues(picker) {
  const counter = new Map();
  for (const actor of state.index.actors) {
    for (const value of picker(actor)) {
      if (value) counter.set(value, (counter.get(value) || 0) + 1);
    }
  }
  return [...counter.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));
}

function applyFilters() {
  const f = state.filters;
  const q = f.q.trim().toLowerCase();
  let rows = state.index.actors.filter((a) => {
    if (q) {
      const hay = (a.name + " " + a.slug + " " + a.aliases.join(" ")).toLowerCase();
      if (!hay.includes(q)) return false;
    }
    if (f.country && !a.attribution.countries.includes(f.country)) return false;
    if (f.sponsor && a.attribution.sponsor_type !== f.sponsor) return false;
    if (f.type && !a.actor_types.includes(f.type)) return false;
    if (f.motivation && !a.motivations.includes(f.motivation)) return false;
    if (f.sector && !a.target_sectors.includes(f.sector)) return false;
    return true;
  });
  const sorters = {
    name: (a, b) => a.name.localeCompare(b.name, "en"),
    iocs: (a, b) => b.counts.iocs - a.counts.iocs,
    ttps: (a, b) => b.counts.ttps - a.counts.ttps,
    malware: (a, b) => (b.counts.malware + b.counts.tools) - (a.counts.malware + a.counts.tools),
    sources: (a, b) => b.counts.sources - a.counts.sources,
  };
  rows.sort(sorters[f.sort] || sorters.name);
  return rows;
}

function actorCard(a) {
  const attribution = a.attribution;
  const badges = [];
  for (const c of attribution.countries) badges.push(`<span class="badge country">${esc(c)}</span>`);
  if (attribution.sponsor_type === "state") badges.push('<span class="badge state">国家支援</span>');
  for (const t of a.actor_types.slice(0, 2)) badges.push(`<span class="badge type">${esc(t)}</span>`);
  for (const m of a.motivations.slice(0, 2)) badges.push(`<span class="badge">${esc(m)}</span>`);

  const aliases = a.aliases.length
    ? `<div class="card-aliases">別名: ${esc(a.aliases.slice(0, 4).join(", "))}${a.aliases.length > 4 ? ` 他${a.aliases.length - 4}件` : ""}</div>`
    : "";

  return `<a class="actor-card" href="#/actor/${encodeURIComponent(a.slug)}">
    <h3>${esc(a.name)}</h3>
    <div class="card-badges">${badges.join("")}</div>
    ${a.description ? `<p class="card-desc">${esc(a.description)}</p>` : ""}
    ${aliases}
    <div class="card-counts">
      <span>TTP <b>${num(a.counts.ttps)}</b></span>
      <span>IOC <b>${num(a.counts.iocs)}</b></span>
      <span>マルウェア <b>${num(a.counts.malware + a.counts.tools)}</b></span>
      <span>出典 <b>${num(a.counts.sources)}</b></span>
    </div>
  </a>`;
}

function renderList() {
  document.title = "Threat Actor Intelligence Profiles";
  const stats = state.index.stats;
  const rows = applyFilters();
  const shown = rows.slice(0, state.listLimit);
  const f = state.filters;

  const selectHtml = (id, label, entries, current) => `
    <select id="${id}" title="${esc(label)}">
      <option value="">${esc(label)}: すべて</option>
      ${entries.map(([v, n]) => `<option value="${esc(v)}" ${v === current ? "selected" : ""}>${esc(v)} (${n})</option>`).join("")}
    </select>`;

  app.innerHTML = `
    <div class="stats-grid">
      <div class="stat-card"><div class="stat-value">${num(stats.actors)}</div><div class="stat-label">アクター / クラスター</div></div>
      <div class="stat-card"><div class="stat-value">${num(stats.aliases)}</div><div class="stat-label">Alias</div></div>
      <div class="stat-card"><div class="stat-value">${num(stats.malware_tools)}</div><div class="stat-label">マルウェア / ツール</div></div>
      <div class="stat-card"><div class="stat-value">${num(stats.ttps)}</div><div class="stat-label">TTP</div></div>
      <div class="stat-card"><div class="stat-value">${num(stats.iocs)}</div><div class="stat-label">IOC</div></div>
      <div class="stat-card"><div class="stat-value">${num(stats.artifacts)}</div><div class="stat-label">非IOC artifact</div></div>
    </div>

    <div class="toolbar">
      <input type="search" id="f-q" placeholder="アクター名・alias・slug で検索…" value="${esc(f.q)}" autocomplete="off">
      ${selectHtml("f-country", "帰属国", facetValues((a) => a.attribution.countries), f.country)}
      ${selectHtml("f-sponsor", "支援形態", facetValues((a) => [a.attribution.sponsor_type]), f.sponsor)}
      ${selectHtml("f-type", "アクター種別", facetValues((a) => a.actor_types), f.type)}
      ${selectHtml("f-motivation", "動機", facetValues((a) => a.motivations), f.motivation)}
      ${selectHtml("f-sector", "標的産業", facetValues((a) => a.target_sectors), f.sector)}
      <select id="f-sort" title="並び順">
        <option value="name" ${f.sort === "name" ? "selected" : ""}>名前順</option>
        <option value="iocs" ${f.sort === "iocs" ? "selected" : ""}>IOC数順</option>
        <option value="ttps" ${f.sort === "ttps" ? "selected" : ""}>TTP数順</option>
        <option value="malware" ${f.sort === "malware" ? "selected" : ""}>マルウェア数順</option>
        <option value="sources" ${f.sort === "sources" ? "selected" : ""}>出典数順</option>
      </select>
      <button class="reset-btn" id="f-reset" type="button">条件クリア</button>
    </div>
    <div class="result-count">${num(rows.length)} 件該当${rows.length !== shown.length ? `(${num(shown.length)} 件表示中)` : ""}</div>

    <div class="actor-grid">${shown.map(actorCard).join("")}</div>
    ${rows.length > shown.length ? '<div class="more-row"><button class="more-btn" id="list-more" type="button">さらに表示</button></div>' : ""}
  `;

  const rerender = () => { state.listLimit = LIST_PAGE; renderList(); };
  let timer = null;
  document.getElementById("f-q").addEventListener("input", (e) => {
    clearTimeout(timer);
    timer = setTimeout(() => { state.filters.q = e.target.value; rerender(); refocusSearch(); }, 150);
  });
  const bindSelect = (id, key) => document.getElementById(id).addEventListener("change", (e) => {
    state.filters[key] = e.target.value; rerender();
  });
  bindSelect("f-country", "country");
  bindSelect("f-sponsor", "sponsor");
  bindSelect("f-type", "type");
  bindSelect("f-motivation", "motivation");
  bindSelect("f-sector", "sector");
  bindSelect("f-sort", "sort");
  document.getElementById("f-reset").addEventListener("click", () => {
    state.filters = { q: "", country: "", sponsor: "", type: "", motivation: "", sector: "", sort: "name" };
    rerender();
  });
  const moreBtn = document.getElementById("list-more");
  if (moreBtn) moreBtn.addEventListener("click", () => {
    state.listLimit += LIST_PAGE * 2;
    const y = window.scrollY;
    renderList();
    window.scrollTo(0, y);
  });

  if (state.listScroll) {
    window.scrollTo(0, state.listScroll);
    state.listScroll = 0;
  }
}

function refocusSearch() {
  const box = document.getElementById("f-q");
  if (box) {
    const v = box.value;
    box.focus();
    box.setSelectionRange(v.length, v.length);
  }
}

/* ---------- detail view ---------- */

function actorLink(name) {
  const slug = state.nameToSlug.get(String(name || "").toLowerCase());
  return slug
    ? `<a href="#/actor/${encodeURIComponent(slug)}">${esc(name)}</a>`
    : esc(name);
}

function techniqueLink(id) {
  if (!id) return "";
  const path = String(id).replace(".", "/");
  return `<a href="https://attack.mitre.org/techniques/${encodeURIComponent(path)}/" target="_blank" rel="noopener" class="mono">${esc(id)}</a>`;
}

function freeTextBlocks(freeText) {
  const labels = {
    history: "経緯・沿革",
    capability_details: "能力の詳細",
    infrastructure_details: "インフラの詳細",
    targeting_details: "標的選定の詳細",
    additional_notes: "補足メモ",
  };
  let html = "";
  for (const [key, label] of Object.entries(labels)) {
    const text = freeText?.[key];
    if (text && text.trim()) {
      html += `<details class="fold"><summary>${esc(label)}</summary>
        <div class="fold-body"><p class="small">${md(text)}</p></div></details>`;
    }
  }
  return html;
}

function softwareTable(items) {
  if (!items || !items.length) return "";
  const rows = items.map((m) => `<tr>
      <td><strong>${esc(m.name || m.id || "?")}</strong></td>
      <td class="small">${esc((m.aliases || []).filter((x) => x !== m.name).join(", "))}</td>
      <td class="small">${esc((m.types || []).join(", "))}</td>
      <td class="small muted">${md((m.description || "").slice(0, 300))}</td>
    </tr>`).join("");
  return `<div class="tbl-wrap"><table class="data">
    <thead><tr><th>名前</th><th>別名</th><th>種別</th><th>概要</th></tr></thead>
    <tbody>${rows}</tbody></table></div>`;
}

function ttpSection(ttps) {
  if (!ttps || !ttps.length) return '<p class="muted">TTP情報なし</p>';
  const groups = new Map();
  for (const t of ttps) {
    const key = (t.tactic || "その他").toLowerCase();
    if (!groups.has(key)) groups.set(key, { label: t.tactic || "その他", items: [] });
    groups.get(key).items.push(t);
  }
  const orderOf = (key) => {
    const i = TACTIC_ORDER.indexOf(key);
    return i === -1 ? 99 : i;
  };
  const sorted = [...groups.entries()].sort((a, b) => orderOf(a[0]) - orderOf(b[0]) || a[0].localeCompare(b[0]));
  return sorted.map(([, group]) => {
    const rows = group.items
      .sort((a, b) => String(a.technique_id).localeCompare(String(b.technique_id)))
      .map((t) => `<tr>
        <td>${techniqueLink(t.technique_id)}</td>
        <td>${esc(t.technique_name || "")}</td>
        <td class="small muted">${md(t.observed_behavior || "")}</td>
      </tr>`).join("");
    return `<details class="fold"><summary>${esc(group.label)}<span class="muted small">${group.items.length} 件</span></summary>
      <div class="fold-body tbl-wrap"><table class="data">
        <thead><tr><th>Technique</th><th>名称</th><th>観測された挙動</th></tr></thead>
        <tbody>${rows}</tbody></table></div></details>`;
  }).join("");
}

async function renderActor(slug) {
  const summary = state.index.actors.find((a) => a.slug === slug);
  if (!summary) { renderError(`アクター "${slug}" は索引に存在しません。`); return; }

  document.title = `${summary.name} | Threat Actor Intelligence Profiles`;
  app.innerHTML = '<div class="loading">プロファイルを読み込み中…</div>';

  let profile;
  try {
    if (state.profileCache.has(slug)) {
      profile = state.profileCache.get(slug);
    } else {
      profile = await fetchJson(`${PROFILES_BASE}/${encodeURIComponent(slug)}/actor-profile.json`);
      state.profileCache.set(slug, profile);
    }
  } catch (err) {
    renderError(err.message);
    return;
  }
  if ((location.hash || "").indexOf(slug) === -1) return; // user navigated away

  const actor = profile.actor || {};
  const attribution = profile.attribution || {};
  const capabilities = profile.capabilities || {};
  const targets = profile.targets || {};
  const freeText = profile.free_text || {};
  const judgments = profile.assessment?.key_judgments || [];

  const headerBadges = [];
  for (const c of attribution.countries || []) headerBadges.push(`<span class="badge country">帰属: ${esc(c)}</span>`);
  if (attribution.sponsor_type && attribution.sponsor_type !== "unknown") headerBadges.push(`<span class="badge state">${esc(attribution.sponsor_type)}</span>`);
  for (const t of actor.actor_types || []) headerBadges.push(`<span class="badge type">${esc(t)}</span>`);
  headerBadges.push(confBadge(attribution.confidence));

  const overviewHtml = `
    ${actor.description ? `<p>${md(actor.description)}</p>` : ""}
    ${freeText.executive_summary ? `<p class="muted small">${md(freeText.executive_summary)}</p>` : ""}
    <div class="kv-grid">
      <div class="kv"><div class="k">初観測</div><div class="v">${esc(fmtDate(actor.first_seen))}</div></div>
      <div class="kv"><div class="k">最終観測</div><div class="v">${esc(fmtDate(actor.last_seen))}</div></div>
      <div class="kv"><div class="k">活動状態</div><div class="v">${esc(actor.active || "unknown")}</div></div>
      <div class="kv"><div class="k">プロファイル更新</div><div class="v">${esc(summary.updated_at || "不明")}</div></div>
    </div>
    ${freeTextBlocks(freeText)}
  `;

  const judgmentsHtml = judgments.length
    ? judgments.map((j) => `<div class="judgment">${md(j.statement)}${confBadge(j.confidence)}</div>`).join("")
    : "";

  const attributionHtml = `
    <div class="kv-grid">
      <div class="kv"><div class="k">帰属国</div><div class="v">${esc((attribution.countries || []).join(", ") || "不明")}</div></div>
      <div class="kv"><div class="k">支援形態</div><div class="v">${esc(attribution.sponsor_type || "unknown")}</div></div>
      <div class="kv"><div class="k">確度</div><div class="v">${esc(attribution.confidence || "unknown")}</div></div>
    </div>
    ${attribution.assessment ? `<p class="small muted">${md(attribution.assessment)}</p>` : ""}
    ${(profile.motivations || []).length ? `<h3>動機</h3>${chips(profile.motivations.map((m) => m.type))}` : ""}
  `;

  const dm = profile.diamond_model || {};
  const diamondHtml = ["adversary", "capability", "infrastructure", "victim"].some((k) => dm[k])
    ? `<div class="diamond-grid">
        <div class="kv"><div class="k">Adversary(攻撃者)</div><div class="v small">${md(dm.adversary || "—")}</div></div>
        <div class="kv"><div class="k">Capability(能力)</div><div class="v small">${md(dm.capability || "—")}</div></div>
        <div class="kv"><div class="k">Infrastructure(インフラ)</div><div class="v small">${md(dm.infrastructure || "—")}</div></div>
        <div class="kv"><div class="k">Victim(被害者)</div><div class="v small">${md(dm.victim || "—")}</div></div>
      </div>
      ${dm.socio_political ? `<p class="small muted">社会・政治的背景: ${md(dm.socio_political)}</p>` : ""}`
    : "";

  const relationships = profile.relationships || [];
  const relationshipsHtml = relationships.length
    ? `<div class="tbl-wrap"><table class="data">
        <thead><tr><th>相手アクター</th><th>関係</th><th>説明</th><th>確度</th></tr></thead>
        <tbody>${relationships.map((r) => `<tr>
          <td>${actorLink(r.target_actor)}</td>
          <td class="small">${esc(r.relationship_type || "")}</td>
          <td class="small muted">${md(r.description || "")}</td>
          <td class="small">${esc(r.confidence || "")}</td>
        </tr>`).join("")}</tbody></table></div>`
    : "";

  const activities = profile.activities || [];
  const activitiesHtml = activities.length
    ? `<div class="tbl-wrap"><table class="data">
        <thead><tr><th>名称</th><th>種別</th><th>初観測</th><th>最終観測</th><th>説明</th></tr></thead>
        <tbody>${activities.map((a) => `<tr>
          <td><strong>${esc(a.name || "")}</strong></td>
          <td class="small">${esc(a.activity_type || "")}</td>
          <td class="small">${esc(fmtDate(a.first_observed))}</td>
          <td class="small">${esc(fmtDate(a.last_observed))}</td>
          <td class="small muted">${md(a.description || "")}</td>
        </tr>`).join("")}</tbody></table></div>`
    : "";

  const targetsHtml = `
    <h3>標的国・地域(${(targets.countries || []).length})</h3>
    ${chips((targets.countries || []).map((t) => t.name), "country")}
    <h3>標的産業(${(targets.sectors || []).length})</h3>
    ${chips((targets.sectors || []).map((t) => t.name), "type")}
    ${targets.selection_logic ? `<p class="small muted">選定ロジック: ${md(targets.selection_logic)}</p>` : ""}
  `;

  const sources = profile.sources || [];
  const sourcesHtml = sources.length
    ? `<div class="tbl-wrap"><table class="data">
        <thead><tr><th>タイトル</th><th>発行元</th><th>発行日</th><th>種別</th></tr></thead>
        <tbody>${sources.map((s) => `<tr>
          <td class="small">${esc(s.title || s.source_id || "")}</td>
          <td class="small">${esc(s.publisher || "")}</td>
          <td class="small">${esc(fmtDate(s.published_at))}</td>
          <td class="small">${esc(s.source_type || "")}</td>
        </tr>`).join("")}</tbody></table></div>`
    : "";

  const base = `${PROFILES_BASE}/${encodeURIComponent(slug)}`;
  const blob = `${REPO_BLOB}/profiles/${encodeURIComponent(slug)}`;
  const downloadsHtml = `<div class="dl-links">
      <a href="${base}/actor-profile.json" download>actor-profile.json</a>
      <a href="${base}/iocs.json" download>iocs.json</a>
      <a href="${base}/generated/profile.stix2.json" download>STIX 2.1 Bundle</a>
      <a href="${blob}/generated/profile-ja.md" target="_blank" rel="noopener">日本語プロファイル (GitHub) ↗</a>
      <a href="${blob}/claim-audit.json" target="_blank" rel="noopener">主張監査 (GitHub) ↗</a>
      <a href="${blob}/artifacts.csv" target="_blank" rel="noopener">artifacts.csv (GitHub) ↗</a>
    </div>`;

  const iocTypeChips = Object.entries(summary.ioc_types)
    .sort((a, b) => b[1] - a[1])
    .map(([t, n]) => `<span class="badge">${esc(t)}: ${num(n)}</span>`)
    .join("");
  const iocHtml = summary.counts.iocs
    ? `<div class="chip-list">${iocTypeChips}</div>
       <p class="defanged-note">表示上の値は defang 済みです(hxxp / [.])。原値は iocs.json を参照してください。</p>
       <div id="ioc-area"><div class="more-row"><button class="load-btn" id="ioc-load" type="button">IOC ${num(summary.counts.iocs)} 件を読み込む</button></div></div>`
    : '<p class="muted">このアクターに正規化済みIOCはありません。</p>';

  const parts = [
    `<a class="back-link" href="#/">← アクター一覧へ戻る</a>
     <div class="actor-header">
       <h1>${esc(profile.name || summary.name)}</h1>
       <div class="actor-meta">${headerBadges.join("")}<span class="sep">slug: <code>${esc(slug)}</code></span></div>
     </div>`,
    section("概要", overviewHtml),
  ];
  if ((actor.aliases || []).length) parts.push(section(`Alias(${actor.aliases.length})`, chips(actor.aliases.map((a) => a.name || a))));
  if (judgmentsHtml) parts.push(section("主要判断(Key Judgments)", judgmentsHtml));
  parts.push(section("帰属・動機", attributionHtml));
  if (diamondHtml) parts.push(section("ダイヤモンドモデル", diamondHtml));
  if (relationshipsHtml) parts.push(section(`他アクターとの関係(${relationships.length})`, relationshipsHtml));
  if ((capabilities.malware || []).length) parts.push(section(`マルウェア(${capabilities.malware.length})`, softwareTable(capabilities.malware)));
  if ((capabilities.tools || []).length) parts.push(section(`ツール(${capabilities.tools.length})`, softwareTable(capabilities.tools)));
  if (activitiesHtml) parts.push(section(`活動・キャンペーン(${activities.length})`, activitiesHtml));
  parts.push(section("標的", targetsHtml));
  parts.push(section(`MITRE ATT&CK TTP(${(profile.ttps || []).length})`, ttpSection(profile.ttps)));
  parts.push(section(`IOC(${num(summary.counts.iocs)})/ 非IOC artifact(${num(summary.counts.artifacts)})`, iocHtml));
  if (sourcesHtml) parts.push(section(`出典(${sources.length})`, sourcesHtml));
  parts.push(section("データダウンロード", downloadsHtml));

  app.innerHTML = parts.join("");
  window.scrollTo(0, 0);

  const loadBtn = document.getElementById("ioc-load");
  if (loadBtn) loadBtn.addEventListener("click", () => loadIocs(slug, summary));
}

/* ---------- IOC ---------- */

async function loadIocs(slug, summary) {
  const area = document.getElementById("ioc-area");
  area.innerHTML = '<div class="loading">IOCを読み込み中…(件数が多い場合は時間がかかります)</div>';
  let indicators;
  try {
    if (state.iocCache.has(slug)) {
      indicators = state.iocCache.get(slug);
    } else {
      const data = await fetchJson(`${PROFILES_BASE}/${encodeURIComponent(slug)}/iocs.json`);
      indicators = data.indicators || [];
      state.iocCache.set(slug, indicators);
    }
  } catch (err) {
    area.innerHTML = `<div class="error-box">${esc(err.message)}</div>`;
    return;
  }

  const types = Object.keys(summary.ioc_types).sort();
  const view = { q: "", type: "", limit: IOC_PAGE };

  const render = () => {
    const q = view.q.trim().toLowerCase();
    const rows = indicators.filter((ind) =>
      (!view.type || ind.type === view.type) &&
      (!q || String(ind.value || "").toLowerCase().includes(q)));
    const shown = rows.slice(0, view.limit);
    area.innerHTML = `
      <div class="ioc-controls">
        <input type="search" id="ioc-q" placeholder="IOC値で絞り込み…" value="${esc(view.q)}" autocomplete="off">
        <select id="ioc-type">
          <option value="">種別: すべて</option>
          ${types.map((t) => `<option value="${esc(t)}" ${t === view.type ? "selected" : ""}>${esc(t)} (${num(summary.ioc_types[t])})</option>`).join("")}
        </select>
      </div>
      <div class="result-count">${num(rows.length)} 件該当${rows.length !== shown.length ? `(${num(shown.length)} 件表示中)` : ""}</div>
      <div class="tbl-wrap"><table class="data">
        <thead><tr><th>種別</th><th>値(defang済)</th><th>状態</th><th>観測数</th><th>初観測</th><th>最終観測</th></tr></thead>
        <tbody>${shown.map((ind) => `<tr>
          <td class="small">${esc(ind.type)}</td>
          <td><span class="mono">${esc(defang(ind.value, ind.type))}</span></td>
          <td class="small">${esc(ind.disposition || "")}</td>
          <td class="num small">${num(ind.observation_count)}</td>
          <td class="small">${esc(fmtDate(ind.first_observed))}</td>
          <td class="small">${esc(fmtDate(ind.last_observed))}</td>
        </tr>`).join("")}</tbody></table></div>
      ${rows.length > shown.length ? '<div class="more-row"><button class="more-btn" id="ioc-more" type="button">さらに表示</button></div>' : ""}
    `;

    let timer = null;
    document.getElementById("ioc-q").addEventListener("input", (e) => {
      clearTimeout(timer);
      timer = setTimeout(() => {
        view.q = e.target.value; view.limit = IOC_PAGE; render();
        const box = document.getElementById("ioc-q");
        box.focus(); box.setSelectionRange(box.value.length, box.value.length);
      }, 150);
    });
    document.getElementById("ioc-type").addEventListener("change", (e) => {
      view.type = e.target.value; view.limit = IOC_PAGE; render();
    });
    const more = document.getElementById("ioc-more");
    if (more) more.addEventListener("click", () => {
      view.limit += IOC_PAGE * 2;
      const y = window.scrollY;
      render();
      window.scrollTo(0, y);
    });
  };
  render();
}

boot();
