/* アクター詳細ビュー: profiles/<slug>/actor-profile.json を取得して各セクションを描画 */

import { PROFILES_BASE, REPO_BLOB, IOC_PAGE, TACTIC_ORDER } from "./config.js";
import { state, findActor, slugForName, getGraph, incomingRelationships } from "./data.js";
import {
  app, esc, md, num, chips, section, dataTable, resultCount,
  fmtDate, confBadge, defang, fetchJson, renderError,
  bindLiveSearch, bindMoreButton,
} from "./util.js";

/* ---------- 小さなリンク・部品 ---------- */

function actorLink(name) {
  const slug = slugForName(name);
  return slug
    ? `<a href="#/actor/${encodeURIComponent(slug)}">${esc(name)}</a>`
    : esc(name);
}

function techniqueLink(id) {
  if (!id) return "";
  const path = String(id).replace(".", "/");
  return `<a href="https://attack.mitre.org/techniques/${encodeURIComponent(path)}/" target="_blank" rel="noopener" class="mono">${esc(id)}</a>`;
}

/* ---------- セクションビルダー ---------- */

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

function buildHeader(profile, summary, slug) {
  const actor = profile.actor || {};
  const attribution = profile.attribution || {};
  const badges = [];
  for (const c of attribution.countries || []) badges.push(`<span class="badge country">帰属: ${esc(c)}</span>`);
  if (attribution.sponsor_type && attribution.sponsor_type !== "unknown") badges.push(`<span class="badge state">${esc(attribution.sponsor_type)}</span>`);
  for (const t of actor.actor_types || []) badges.push(`<span class="badge type">${esc(t)}</span>`);
  badges.push(confBadge(attribution.confidence));

  return `<a class="back-link" href="#/">← アクター一覧へ戻る</a>
    <div class="actor-header">
      <h1>${esc(profile.name || summary.name)}</h1>
      <div class="actor-meta">${badges.join("")}<span class="sep">slug: <code>${esc(slug)}</code></span></div>
    </div>`;
}

function buildOverview(profile, summary) {
  const actor = profile.actor || {};
  const freeText = profile.free_text || {};
  return `
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
}

function buildJudgments(profile) {
  const judgments = profile.assessment?.key_judgments || [];
  return judgments
    .map((j) => `<div class="judgment">${md(j.statement)}${confBadge(j.confidence)}</div>`)
    .join("");
}

function buildAttribution(profile) {
  const attribution = profile.attribution || {};
  return `
    <div class="kv-grid">
      <div class="kv"><div class="k">帰属国</div><div class="v">${esc((attribution.countries || []).join(", ") || "不明")}</div></div>
      <div class="kv"><div class="k">支援形態</div><div class="v">${esc(attribution.sponsor_type || "unknown")}</div></div>
      <div class="kv"><div class="k">確度</div><div class="v">${esc(attribution.confidence || "unknown")}</div></div>
    </div>
    ${attribution.assessment ? `<p class="small muted">${md(attribution.assessment)}</p>` : ""}
    ${(profile.motivations || []).length ? `<h3>動機</h3>${chips(profile.motivations.map((m) => m.type))}` : ""}
  `;
}

function buildDiamond(profile) {
  const dm = profile.diamond_model || {};
  if (!["adversary", "capability", "infrastructure", "victim"].some((k) => dm[k])) return "";
  const dmNode = (key, label, text) => `<div class="dm-node dm-${key}">
      <div class="k">${esc(label)}</div>
      <div class="v small">${text ? md(text) : '<span class="muted">情報なし</span>'}</div>
    </div>`;
  return `<div class="diamond-wrap">
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
    ${dm.socio_political ? `<p class="small muted">社会・政治的背景: ${md(dm.socio_political)}</p>` : ""}`;
}

// 発信(プロファイル記載)+被参照(他プロファイルからの逆引き)を1セクションに
function buildRelationships(profile, slug) {
  const outgoing = profile.relationships || [];
  const incoming = incomingRelationships(slug);
  const parts = [];
  if (outgoing.length) {
    parts.push(dataTable(
      ["相手アクター", "関係", "説明", "確度"],
      outgoing.map((r) => `<tr>
        <td>${actorLink(r.target_actor)}</td>
        <td class="small">${esc(r.relationship_type || "")}</td>
        <td class="small muted">${md(r.description || "")}</td>
        <td class="small">${esc(r.confidence || "")}</td>
      </tr>`).join("")
    ));
  }
  if (incoming.length) {
    parts.push(`<h3>このアクターを参照する関係(${incoming.length})</h3>` + dataTable(
      ["参照元アクター", "関係", "確度"],
      incoming.map((r) => `<tr>
        <td><a href="#/actor/${encodeURIComponent(r.from.slug)}">${esc(r.from.name)}</a></td>
        <td class="small">${esc(r.type || "")}</td>
        <td class="small">${esc(r.confidence || "")}</td>
      </tr>`).join("")
    ));
  }
  if (getGraph().nodes.has(slug)) {
    parts.push(`<p class="small"><a href="#/relations/${encodeURIComponent(slug)}">◇ 関係グラフでこのアクターを表示 →</a></p>`);
  }
  return { html: parts.join(""), total: outgoing.length + incoming.length };
}

function softwareTable(items) {
  if (!items || !items.length) return "";
  return dataTable(
    ["名前", "別名", "種別", "概要"],
    items.map((m) => `<tr>
      <td><strong>${esc(m.name || m.id || "?")}</strong></td>
      <td class="small">${esc((m.aliases || []).filter((x) => x !== m.name).join(", "))}</td>
      <td class="small">${esc((m.types || []).join(", "))}</td>
      <td class="small muted">${md((m.description || "").slice(0, 300))}</td>
    </tr>`).join("")
  );
}

function buildActivities(profile) {
  const activities = profile.activities || [];
  if (!activities.length) return "";
  return dataTable(
    ["名称", "種別", "初観測", "最終観測", "説明"],
    activities.map((a) => `<tr>
      <td><strong>${esc(a.name || "")}</strong></td>
      <td class="small">${esc(a.activity_type || "")}</td>
      <td class="small">${esc(fmtDate(a.first_observed))}</td>
      <td class="small">${esc(fmtDate(a.last_observed))}</td>
      <td class="small muted">${md(a.description || "")}</td>
    </tr>`).join("")
  );
}

function buildTargets(profile) {
  const targets = profile.targets || {};
  return `
    <h3>標的国・地域(${(targets.countries || []).length})</h3>
    ${chips((targets.countries || []).map((t) => t.name), "country")}
    <h3>標的産業(${(targets.sectors || []).length})</h3>
    ${chips((targets.sectors || []).map((t) => t.name), "type")}
    ${targets.selection_logic ? `<p class="small muted">選定ロジック: ${md(targets.selection_logic)}</p>` : ""}
  `;
}

function buildTtps(ttps) {
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
      <div class="fold-body">${dataTable(["Technique", "名称", "観測された挙動"], rows)}</div></details>`;
  }).join("");
}

function buildSources(profile) {
  const sources = profile.sources || [];
  if (!sources.length) return "";
  return dataTable(
    ["タイトル", "発行元", "発行日", "種別"],
    sources.map((s) => `<tr>
      <td class="small">${esc(s.title || s.source_id || "")}</td>
      <td class="small">${esc(s.publisher || "")}</td>
      <td class="small">${esc(fmtDate(s.published_at))}</td>
      <td class="small">${esc(s.source_type || "")}</td>
    </tr>`).join("")
  );
}

function buildDownloads(slug) {
  const base = `${PROFILES_BASE}/${encodeURIComponent(slug)}`;
  const blob = `${REPO_BLOB}/profiles/${encodeURIComponent(slug)}`;
  return `<div class="dl-links">
      <a href="${base}/actor-profile.json" download>actor-profile.json</a>
      <a href="${base}/iocs.json" download>iocs.json</a>
      <a href="${base}/generated/profile.stix2.json" download>STIX 2.1 Bundle</a>
      <a href="${blob}/generated/profile-ja.md" target="_blank" rel="noopener">日本語プロファイル (GitHub) ↗</a>
      <a href="${blob}/claim-audit.json" target="_blank" rel="noopener">主張監査 (GitHub) ↗</a>
      <a href="${blob}/artifacts.csv" target="_blank" rel="noopener">artifacts.csv (GitHub) ↗</a>
    </div>`;
}

function buildIocSection(summary) {
  if (!summary.counts.iocs) return '<p class="muted">このアクターに正規化済みIOCはありません。</p>';
  const typeChips = Object.entries(summary.ioc_types)
    .sort((a, b) => b[1] - a[1])
    .map(([t, n]) => `<span class="badge">${esc(t)}: ${num(n)}</span>`)
    .join("");
  return `<div class="chip-list">${typeChips}</div>
    <p class="defanged-note">表示上の値は defang 済みです(hxxp / [.])。原値は iocs.json を参照してください。</p>
    <div id="ioc-area"><div class="more-row"><button class="load-btn" id="ioc-load" type="button">IOC ${num(summary.counts.iocs)} 件を読み込む</button></div></div>`;
}

/* ---------- IOC 遅延読み込み ---------- */

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
      ${resultCount(rows.length, shown.length)}
      ${dataTable(
        ["種別", "値(defang済)", "状態", "観測数", "初観測", "最終観測"],
        shown.map((ind) => `<tr>
          <td class="small">${esc(ind.type)}</td>
          <td><span class="mono">${esc(defang(ind.value, ind.type))}</span></td>
          <td class="small">${esc(ind.disposition || "")}</td>
          <td class="num small">${num(ind.observation_count)}</td>
          <td class="small">${esc(fmtDate(ind.first_observed))}</td>
          <td class="small">${esc(fmtDate(ind.last_observed))}</td>
        </tr>`).join("")
      )}
      ${rows.length > shown.length ? '<div class="more-row"><button class="more-btn" id="ioc-more" type="button">さらに表示</button></div>' : ""}
    `;
    bindLiveSearch("ioc-q", (value) => { view.q = value; view.limit = IOC_PAGE; render(); });
    document.getElementById("ioc-type").addEventListener("change", (e) => {
      view.type = e.target.value; view.limit = IOC_PAGE; render();
    });
    bindMoreButton("ioc-more", () => { view.limit += IOC_PAGE * 2; render(); });
  };
  render();
}

/* ---------- エントリポイント ---------- */

export async function renderActor(slug) {
  const summary = findActor(slug);
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
  if ((location.hash || "").indexOf(slug) === -1) return; // 読み込み中に別ページへ遷移済み

  const actor = profile.actor || {};
  const capabilities = profile.capabilities || {};
  const judgmentsHtml = buildJudgments(profile);
  const diamondHtml = buildDiamond(profile);
  const relationships = buildRelationships(profile, slug);
  const activitiesHtml = buildActivities(profile);
  const sourcesHtml = buildSources(profile);

  const parts = [buildHeader(profile, summary, slug), section("概要", buildOverview(profile, summary))];
  if ((actor.aliases || []).length) parts.push(section(`Alias(${actor.aliases.length})`, chips(actor.aliases.map((a) => a.name || a))));
  if (judgmentsHtml) parts.push(section("主要判断(Key Judgments)", judgmentsHtml));
  parts.push(section("帰属・動機", buildAttribution(profile)));
  if (diamondHtml) parts.push(section("ダイヤモンドモデル", diamondHtml));
  if (relationships.html) parts.push(section(`他アクターとの関係(${relationships.total})`, relationships.html));
  if ((capabilities.malware || []).length) parts.push(section(`マルウェア(${capabilities.malware.length})`, softwareTable(capabilities.malware)));
  if ((capabilities.tools || []).length) parts.push(section(`ツール(${capabilities.tools.length})`, softwareTable(capabilities.tools)));
  if (activitiesHtml) parts.push(section(`活動・キャンペーン(${profile.activities.length})`, activitiesHtml));
  parts.push(section("標的", buildTargets(profile)));
  parts.push(section(`MITRE ATT&CK TTP(${(profile.ttps || []).length})`, buildTtps(profile.ttps)));
  parts.push(section(`IOC(${num(summary.counts.iocs)})/ 非IOC artifact(${num(summary.counts.artifacts)})`, buildIocSection(summary)));
  if (sourcesHtml) parts.push(section(`出典(${profile.sources.length})`, sourcesHtml));
  parts.push(section("データダウンロード", buildDownloads(slug)));

  app.innerHTML = parts.join("");
  window.scrollTo(0, 0);

  const loadBtn = document.getElementById("ioc-load");
  if (loadBtn) loadBtn.addEventListener("click", () => loadIocs(slug, summary));
}
