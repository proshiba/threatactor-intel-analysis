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
  currentView: null,    // "list" | "actor" | "graph"
  bySlug: new Map(),
  graph: null,          // {nodes: Map, edges: []} 遅延構築
  graphAnim: null,      // requestAnimationFrame handle
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
      state.bySlug.set(actor.slug, actor);
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
  if (state.graphAnim) {
    cancelAnimationFrame(state.graphAnim);
    state.graphAnim = null;
  }
  const hash = location.hash || "#/";
  const actorMatch = hash.match(/^#\/actor\/([A-Za-z0-9._-]+)/);
  const graphMatch = hash.match(/^#\/relations(?:\/([A-Za-z0-9._-]+))?/);
  if (actorMatch) {
    if (state.currentView === "list") state.listScroll = window.scrollY;
    state.currentView = "actor";
    renderActor(decodeURIComponent(actorMatch[1]));
  } else if (graphMatch) {
    if (state.currentView === "list") state.listScroll = window.scrollY;
    state.currentView = "graph";
    renderGraph(graphMatch[1] ? decodeURIComponent(graphMatch[1]) : null);
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
  const dmNode = (key, label, text) => `<div class="dm-node dm-${key}">
      <div class="k">${esc(label)}</div>
      <div class="v small">${text ? md(text) : '<span class="muted">情報なし</span>'}</div>
    </div>`;
  const diamondHtml = ["adversary", "capability", "infrastructure", "victim"].some((k) => dm[k])
    ? `<div class="diamond-wrap">
        <svg class="diamond-lines" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
          <path d="M50 3 L97 50 L50 97 L3 50 Z" fill="none" stroke="currentColor" stroke-width="0.5"/>
          <path d="M50 3 L50 97 M3 50 L97 50" fill="none" stroke="currentColor" stroke-width="0.3" stroke-dasharray="1.5 2"/>
        </svg>
        ${dmNode("adversary", "Adversary(攻撃者)", dm.adversary)}
        ${dmNode("infrastructure", "Infrastructure(インフラ)", dm.infrastructure)}
        ${dmNode("capability", "Capability(能力)", dm.capability)}
        ${dmNode("victim", "Victim(被害者)", dm.victim)}
        <div class="dm-center">Diamond<br>Model</div>
      </div>
      ${dm.socio_political ? `<p class="small muted">社会・政治的背景: ${md(dm.socio_political)}</p>` : ""}`
    : "";

  const relationships = profile.relationships || [];
  const incoming = [];
  for (const other of state.index.actors) {
    if (other.slug === slug) continue;
    for (const r of other.relationships || []) {
      if (r.target_slug === slug) incoming.push({ from: other, type: r.type, confidence: r.confidence });
    }
  }
  const inGraph = getGraph().nodes.has(slug);
  const relParts = [];
  if (relationships.length) {
    relParts.push(`<div class="tbl-wrap"><table class="data">
        <thead><tr><th>相手アクター</th><th>関係</th><th>説明</th><th>確度</th></tr></thead>
        <tbody>${relationships.map((r) => `<tr>
          <td>${actorLink(r.target_actor)}</td>
          <td class="small">${esc(r.relationship_type || "")}</td>
          <td class="small muted">${md(r.description || "")}</td>
          <td class="small">${esc(r.confidence || "")}</td>
        </tr>`).join("")}</tbody></table></div>`);
  }
  if (incoming.length) {
    relParts.push(`<h3>このアクターを参照する関係(${incoming.length})</h3>
      <div class="tbl-wrap"><table class="data">
        <thead><tr><th>参照元アクター</th><th>関係</th><th>確度</th></tr></thead>
        <tbody>${incoming.map((r) => `<tr>
          <td><a href="#/actor/${encodeURIComponent(r.from.slug)}">${esc(r.from.name)}</a></td>
          <td class="small">${esc(r.type || "")}</td>
          <td class="small">${esc(r.confidence || "")}</td>
        </tr>`).join("")}</tbody></table></div>`);
  }
  if (inGraph) {
    relParts.push(`<p class="small"><a href="#/relations/${encodeURIComponent(slug)}">◇ 関係グラフでこのアクターを表示 →</a></p>`);
  }
  const relationshipsHtml = relParts.join("");

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
  if (relationshipsHtml) parts.push(section(`他アクターとの関係(${relationships.length + incoming.length})`, relationshipsHtml));
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

/* ---------- relations graph ---------- */

const EDGE_COLORS = {
  "overlaps-with": "#fbbf24",
  "related-to": "#4cc2ff",
  "cooperates-with": "#34d399",
  "shares-tools-with": "#2dd4bf",
  "part-of": "#a78bfa",
  "distinct-from": "#f87171",
};
const COUNTRY_PALETTE = ["#f87171", "#fbbf24", "#a78bfa", "#34d399", "#4cc2ff", "#f472b6", "#fb923c", "#e2e8f0"];
const UNKNOWN_COUNTRY = "帰属不明";

function getGraph() {
  if (state.graph) return state.graph;
  const nodes = new Map();
  const edges = [];
  const seen = new Set();
  const ensure = (slug) => {
    if (!nodes.has(slug)) {
      const a = state.bySlug.get(slug);
      nodes.set(slug, {
        slug,
        name: a ? a.name : slug,
        country: a?.attribution.countries[0] || UNKNOWN_COUNTRY,
        deg: 0, x: 0, y: 0, vx: 0, vy: 0,
      });
    }
    return nodes.get(slug);
  };
  for (const a of state.index.actors) {
    for (const r of a.relationships || []) {
      if (!r.target_slug || r.target_slug === a.slug) continue;
      const key = [a.slug, r.target_slug].sort().join("|") + "|" + r.type;
      if (seen.has(key)) continue;
      seen.add(key);
      ensure(a.slug).deg += 1;
      ensure(r.target_slug).deg += 1;
      edges.push({ a: a.slug, b: r.target_slug, type: r.type, confidence: r.confidence });
    }
  }
  state.graph = { nodes, edges };
  return state.graph;
}

function renderGraph(initialFocus) {
  document.title = "関係グラフ | Threat Actor Intelligence Profiles";
  const g = getGraph();
  const nodeArr = [...g.nodes.values()];
  const edges = g.edges;

  const countries = [...new Set(nodeArr.map((n) => n.country))]
    .sort((a, b) => (a === UNKNOWN_COUNTRY) - (b === UNKNOWN_COUNTRY) || a.localeCompare(b));
  const colorOf = {};
  let ci = 0;
  for (const c of countries) colorOf[c] = c === UNKNOWN_COUNTRY ? "#64748b" : COUNTRY_PALETTE[ci++ % COUNTRY_PALETTE.length];

  const typesPresent = [...new Set(edges.map((e) => e.type))];
  app.innerHTML = `
    <a class="back-link" href="#/">← アクター一覧へ戻る</a>
    <section class="section">
      <h2>アクター関係グラフ</h2>
      <p class="small muted">プロファイルに記録された他アクターとの関係(${num(edges.length)} 本 / ${num(nodeArr.length)} アクター)を可視化しています。
      ノードをクリックすると詳細ページへ移動します。背景ドラッグで移動、ホイールでズーム、ノードはドラッグで動かせます。</p>
      <div class="graph-toolbar">
        <input id="g-search" list="g-actors" placeholder="アクター名で検索してフォーカス…" autocomplete="off">
        <datalist id="g-actors">${nodeArr.map((n) => `<option value="${esc(n.name)}"></option>`).join("")}</datalist>
        <button class="reset-btn" id="g-reset" type="button">全体表示</button>
      </div>
      <div class="graph-box">
        <canvas id="g-canvas"></canvas>
        <div class="graph-tip" id="g-tip"></div>
      </div>
      <div class="graph-legend">
        ${typesPresent.map((t) => `<span class="lg"><span class="sw-line ${t === "distinct-from" ? "dashed" : ""}" style="border-color:${EDGE_COLORS[t] || "#8b9ab5"}"></span>${esc(t)}</span>`).join("")}
      </div>
      <div class="graph-legend">
        ${countries.map((c) => `<span class="lg"><span class="sw-dot" style="background:${colorOf[c]}"></span>${esc(c)}</span>`).join("")}
      </div>
    </section>`;

  const canvas = document.getElementById("g-canvas");
  const tip = document.getElementById("g-tip");
  const box = canvas.parentElement;
  const dpr = window.devicePixelRatio || 1;
  let W = box.clientWidth, H = box.clientHeight;
  canvas.width = W * dpr;
  canvas.height = H * dpr;
  const ctx = canvas.getContext("2d");

  // 初期配置: 次数の大きいノードを内側にした同心円
  const sorted = [...nodeArr].sort((a, b) => b.deg - a.deg);
  sorted.forEach((n, i) => {
    const r = 40 + 26 * Math.sqrt(i);
    const th = i * 2.39996; // golden angle
    n.x = r * Math.cos(th);
    n.y = r * Math.sin(th);
    n.vx = 0; n.vy = 0;
  });

  const nodeOf = (slug) => g.nodes.get(slug);
  let alpha = 1;
  let hoverNode = null;
  let dragNode = null;
  function tick() {
    for (let i = 0; i < nodeArr.length; i++) {
      const a = nodeArr[i];
      for (let j = i + 1; j < nodeArr.length; j++) {
        const b = nodeArr[j];
        let dx = a.x - b.x, dy = a.y - b.y;
        let d2 = dx * dx + dy * dy;
        if (d2 < 1) { dx = (Math.random() - 0.5); dy = (Math.random() - 0.5); d2 = 1; }
        if (d2 > 90000) continue;
        const f = 2200 / d2;
        const d = Math.sqrt(d2);
        dx /= d; dy /= d;
        a.vx += dx * f; a.vy += dy * f;
        b.vx -= dx * f; b.vy -= dy * f;
      }
    }
    for (const e of edges) {
      const a = nodeOf(e.a), b = nodeOf(e.b);
      const dx = b.x - a.x, dy = b.y - a.y;
      const d = Math.max(Math.sqrt(dx * dx + dy * dy), 1);
      const f = (d - 120) * 0.02;
      a.vx += (dx / d) * f; a.vy += (dy / d) * f;
      b.vx -= (dx / d) * f; b.vy -= (dy / d) * f;
    }
    for (const n of nodeArr) {
      n.vx -= n.x * 0.004; n.vy -= n.y * 0.004;
      n.vx *= 0.82; n.vy *= 0.82;
      if (n !== dragNode) { n.x += n.vx * alpha; n.y += n.vy * alpha; }
    }
    alpha = Math.max(alpha * 0.995, 0.03);
  }
  for (let i = 0; i < 200; i++) tick(); // 描画前にレイアウトを収束させる

  const view = { k: 1, tx: W / 2, ty: H / 2 };
  let focusSlug = null;
  let neighborSet = new Set();

  function fitAll() {
    let minX = 1e9, maxX = -1e9, minY = 1e9, maxY = -1e9;
    for (const n of nodeArr) {
      minX = Math.min(minX, n.x); maxX = Math.max(maxX, n.x);
      minY = Math.min(minY, n.y); maxY = Math.max(maxY, n.y);
    }
    const k = Math.min((W - 80) / Math.max(maxX - minX, 1), (H - 80) / Math.max(maxY - minY, 1), 2.5);
    view.k = k;
    view.tx = W / 2 - ((minX + maxX) / 2) * k;
    view.ty = H / 2 - ((minY + maxY) / 2) * k;
  }

  function setFocus(slug, updateHash) {
    focusSlug = slug && g.nodes.has(slug) ? slug : null;
    neighborSet = new Set();
    if (focusSlug) {
      neighborSet.add(focusSlug);
      for (const e of edges) {
        if (e.a === focusSlug) neighborSet.add(e.b);
        if (e.b === focusSlug) neighborSet.add(e.a);
      }
      const n = nodeOf(focusSlug);
      view.k = 1.6;
      view.tx = W / 2 - n.x * view.k;
      view.ty = H / 2 - n.y * view.k;
    } else {
      fitAll();
    }
    if (updateHash) {
      history.replaceState(null, "", focusSlug ? `#/relations/${encodeURIComponent(focusSlug)}` : "#/relations");
    }
  }

  const radiusOf = (n) => Math.min(5 + n.deg * 1.6, 16);

  function draw() {
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);
    ctx.setTransform(dpr * view.k, 0, 0, dpr * view.k, dpr * view.tx, dpr * view.ty);

    for (const e of edges) {
      const a = nodeOf(e.a), b = nodeOf(e.b);
      const active = !focusSlug || e.a === focusSlug || e.b === focusSlug;
      ctx.globalAlpha = active ? 0.75 : 0.08;
      ctx.strokeStyle = EDGE_COLORS[e.type] || "#8b9ab5";
      ctx.lineWidth = (e.confidence === "high" ? 2.2 : 1.2) / view.k;
      ctx.setLineDash(e.type === "distinct-from" ? [5 / view.k, 4 / view.k] : []);
      ctx.beginPath();
      ctx.moveTo(a.x, a.y);
      ctx.lineTo(b.x, b.y);
      ctx.stroke();
    }
    ctx.setLineDash([]);

    for (const n of nodeArr) {
      const active = !focusSlug || neighborSet.has(n.slug);
      ctx.globalAlpha = active ? 1 : 0.12;
      ctx.fillStyle = colorOf[n.country];
      ctx.beginPath();
      ctx.arc(n.x, n.y, radiusOf(n), 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = n.slug === focusSlug || n === hoverNode ? "#ffffff" : "#0b0f17";
      ctx.lineWidth = (n.slug === focusSlug || n === hoverNode ? 2.5 : 1.5) / view.k;
      ctx.stroke();
    }

    const fontPx = 11 / view.k;
    ctx.font = `${fontPx}px "Hiragino Kaku Gothic ProN", system-ui, sans-serif`;
    ctx.textAlign = "center";
    for (const n of nodeArr) {
      const active = !focusSlug || neighborSet.has(n.slug);
      const showLabel = n === hoverNode || n.slug === focusSlug ||
        (active && (n.deg >= 3 || view.k >= 1.15));
      if (!showLabel) continue;
      ctx.globalAlpha = active ? 0.95 : 0.15;
      ctx.fillStyle = "#dbe4f3";
      ctx.fillText(n.name, n.x, n.y - radiusOf(n) - 5 / view.k);
    }
    ctx.globalAlpha = 1;
  }

  function loop() {
    if (!document.body.contains(canvas)) return; // 画面遷移済み
    tick();
    draw();
    state.graphAnim = requestAnimationFrame(loop);
  }

  // ---- interaction ----
  const toWorld = (mx, my) => ({ x: (mx - view.tx) / view.k, y: (my - view.ty) / view.k });
  const findNode = (mx, my) => {
    const w = toWorld(mx, my);
    let best = null, bestD = 1e9;
    for (const n of nodeArr) {
      const dx = n.x - w.x, dy = n.y - w.y;
      const d = Math.sqrt(dx * dx + dy * dy);
      if (d < radiusOf(n) + 6 / view.k && d < bestD) { best = n; bestD = d; }
    }
    return best;
  };

  let pointer = null; // {mx,my,moved}
  canvas.addEventListener("pointerdown", (ev) => {
    const rect = canvas.getBoundingClientRect();
    const mx = ev.clientX - rect.left, my = ev.clientY - rect.top;
    pointer = { mx, my, moved: 0 };
    dragNode = findNode(mx, my);
    canvas.classList.add("dragging");
    canvas.setPointerCapture(ev.pointerId);
    if (dragNode) alpha = Math.max(alpha, 0.3);
  });
  canvas.addEventListener("pointermove", (ev) => {
    const rect = canvas.getBoundingClientRect();
    const mx = ev.clientX - rect.left, my = ev.clientY - rect.top;
    if (pointer) {
      const dx = mx - pointer.mx, dy = my - pointer.my;
      pointer.moved += Math.abs(dx) + Math.abs(dy);
      if (dragNode) {
        const w = toWorld(mx, my);
        dragNode.x = w.x; dragNode.y = w.y;
        dragNode.vx = 0; dragNode.vy = 0;
        alpha = Math.max(alpha, 0.25);
      } else {
        view.tx += dx; view.ty += dy;
      }
      pointer.mx = mx; pointer.my = my;
      return;
    }
    const n = findNode(mx, my);
    hoverNode = n;
    canvas.style.cursor = n ? "pointer" : "grab";
    if (n) {
      const a = state.bySlug.get(n.slug);
      tip.style.display = "block";
      tip.style.left = Math.min(mx + 14, W - 290) + "px";
      tip.style.top = (my + 14) + "px";
      tip.innerHTML = `<div class="t-name">${esc(n.name)}</div>
        <div>${esc(n.country)} / 関係 ${n.deg} 本</div>
        ${a && a.aliases.length ? `<div class="muted">別名: ${esc(a.aliases.slice(0, 3).join(", "))}</div>` : ""}
        <div class="muted">クリックで詳細ページへ</div>`;
    } else {
      tip.style.display = "none";
    }
  });
  const endPointer = (ev) => {
    if (!pointer) return;
    const clicked = pointer.moved < 5 ? findNode(pointer.mx, pointer.my) : null;
    pointer = null;
    dragNode = null;
    canvas.classList.remove("dragging");
    if (clicked) location.hash = `#/actor/${encodeURIComponent(clicked.slug)}`;
  };
  canvas.addEventListener("pointerup", endPointer);
  canvas.addEventListener("pointercancel", () => { pointer = null; dragNode = null; canvas.classList.remove("dragging"); });
  canvas.addEventListener("pointerleave", () => { hoverNode = null; tip.style.display = "none"; });

  canvas.addEventListener("wheel", (ev) => {
    ev.preventDefault();
    const rect = canvas.getBoundingClientRect();
    const mx = ev.clientX - rect.left, my = ev.clientY - rect.top;
    const factor = Math.exp(-ev.deltaY * 0.0012);
    const k2 = Math.min(Math.max(view.k * factor, 0.15), 5);
    view.tx = mx - ((mx - view.tx) / view.k) * k2;
    view.ty = my - ((my - view.ty) / view.k) * k2;
    view.k = k2;
  }, { passive: false });

  document.getElementById("g-search").addEventListener("change", (ev) => {
    const q = ev.target.value.trim().toLowerCase();
    if (!q) return;
    const n = nodeArr.find((x) => x.name.toLowerCase() === q) ||
      nodeArr.find((x) => x.name.toLowerCase().includes(q));
    if (n) { setFocus(n.slug, true); alpha = Math.max(alpha, 0.1); }
  });
  document.getElementById("g-reset").addEventListener("click", () => {
    document.getElementById("g-search").value = "";
    setFocus(null, true);
  });

  window.addEventListener("resize", function onResize() {
    if (!document.body.contains(canvas)) { window.removeEventListener("resize", onResize); return; }
    W = box.clientWidth; H = box.clientHeight;
    canvas.width = W * dpr; canvas.height = H * dpr;
  });

  setFocus(initialFocus, false);
  window.scrollTo(0, 0);
  loop();
}

boot();
