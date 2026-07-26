/* 一覧ビュー: 統計、検索・フィルタ・ソート、アクターカード */

import { LIST_PAGE } from "./config.js";
import { state, resetFilters } from "./data.js";
import { app, esc, num, bindLiveSearch, bindMoreButton, resultCount } from "./util.js";

const SORTERS = {
  name: (a, b) => a.name.localeCompare(b.name, "en"),
  iocs: (a, b) => b.counts.iocs - a.counts.iocs,
  ttps: (a, b) => b.counts.ttps - a.counts.ttps,
  malware: (a, b) => (b.counts.malware + b.counts.tools) - (a.counts.malware + a.counts.tools),
  sources: (a, b) => b.counts.sources - a.counts.sources,
};
const SORT_LABELS = { name: "名前順", iocs: "IOC数順", ttps: "TTP数順", malware: "マルウェア数順", sources: "出典数順" };

// picker が返す値ごとの件数を [値, 件数] の頻度降順で返す
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
  const rows = state.index.actors.filter((a) => {
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
  rows.sort(SORTERS[f.sort] || SORTERS.name);
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

function statsGrid(stats) {
  const cards = [
    [stats.actors, "アクター / クラスター"],
    [stats.aliases, "Alias"],
    [stats.malware_tools, "マルウェア / ツール"],
    [stats.ttps, "TTP"],
    [stats.iocs, "IOC"],
    [stats.artifacts, "非IOC artifact"],
  ];
  return `<div class="stats-grid">${cards.map(([v, label]) =>
    `<div class="stat-card"><div class="stat-value">${num(v)}</div><div class="stat-label">${esc(label)}</div></div>`
  ).join("")}</div>`;
}

function selectHtml(id, label, entries, current) {
  return `
    <select id="${id}" title="${esc(label)}">
      <option value="">${esc(label)}: すべて</option>
      ${entries.map(([v, n]) => `<option value="${esc(v)}" ${v === current ? "selected" : ""}>${esc(v)} (${n})</option>`).join("")}
    </select>`;
}

export function renderList() {
  document.title = "Threat Actor Intelligence Profiles";
  const rows = applyFilters();
  const shown = rows.slice(0, state.listLimit);
  const f = state.filters;

  app.innerHTML = `
    ${statsGrid(state.index.stats)}
    <div class="toolbar">
      <input type="search" id="f-q" placeholder="アクター名・alias・slug で検索…" value="${esc(f.q)}" autocomplete="off">
      ${selectHtml("f-country", "帰属国", facetValues((a) => a.attribution.countries), f.country)}
      ${selectHtml("f-sponsor", "支援形態", facetValues((a) => [a.attribution.sponsor_type]), f.sponsor)}
      ${selectHtml("f-type", "アクター種別", facetValues((a) => a.actor_types), f.type)}
      ${selectHtml("f-motivation", "動機", facetValues((a) => a.motivations), f.motivation)}
      ${selectHtml("f-sector", "標的産業", facetValues((a) => a.target_sectors), f.sector)}
      <select id="f-sort" title="並び順">
        ${Object.entries(SORT_LABELS).map(([v, label]) =>
          `<option value="${v}" ${f.sort === v ? "selected" : ""}>${label}</option>`).join("")}
      </select>
      <button class="reset-btn" id="f-reset" type="button">条件クリア</button>
    </div>
    ${resultCount(rows.length, shown.length)}
    <div class="actor-grid">${shown.map(actorCard).join("")}</div>
    ${rows.length > shown.length ? '<div class="more-row"><button class="more-btn" id="list-more" type="button">さらに表示</button></div>' : ""}
  `;

  const rerender = () => { state.listLimit = LIST_PAGE; renderList(); };
  bindLiveSearch("f-q", (value) => { state.filters.q = value; rerender(); });
  const bindSelect = (id, key) => document.getElementById(id).addEventListener("change", (e) => {
    state.filters[key] = e.target.value;
    rerender();
  });
  bindSelect("f-country", "country");
  bindSelect("f-sponsor", "sponsor");
  bindSelect("f-type", "type");
  bindSelect("f-motivation", "motivation");
  bindSelect("f-sector", "sector");
  bindSelect("f-sort", "sort");
  document.getElementById("f-reset").addEventListener("click", () => { resetFilters(); rerender(); });
  bindMoreButton("list-more", () => { state.listLimit += LIST_PAGE * 2; renderList(); });

  if (state.listScroll) {
    window.scrollTo(0, state.listScroll);
    state.listScroll = 0;
  }
}
