/* アクター詳細ビュー(タブ構成)
 *
 * タブ:
 *   overview     … 説明、別名、主要判断、帰属・動機、ダイヤモンドモデル、標的
 *   relations    … 他アクターとの関係(発信+被参照)とグラフへのリンク
 *   capabilities … マルウェア、ツール、インフラ・サービス
 *   ttps         … ATT&CK マトリックス表示
 *   activities   … 活動履歴のタイムライン(期間フィルタ付き)
 *   artifacts    … IOCと非IOCアーティファクト(遅延読み込み)
 *   sources      … 出典とデータダウンロード
 */

import { PROFILES_BASE, REPO_BLOB, IOC_PAGE, TACTIC_ORDER } from "./config.js";
import { state, findActor, slugForName, getGraph, incomingRelationships } from "./data.js";
import {
  app, esc, md, num, chips, section, dataTable, resultCount,
  fmtDate, confBadge, defang, fetchJson, fetchText, parseCsv, renderError,
  bindLiveSearch, bindMoreButton,
} from "./util.js";
import { ja, jaTactic, jaNarrative } from "./locale-ja.js";

/* ---------- 小さなリンク・部品 ---------- */

function actorLink(name) {
  const slug = slugForName(name);
  return slug
    ? `<a href="#/actor/${encodeURIComponent(slug)}">${esc(name)}</a>`
    : esc(name);
}

function mitreUrl(id) {
  return `https://attack.mitre.org/techniques/${encodeURIComponent(String(id).replace(".", "/"))}/`;
}

// 指定キーのfree_textを折りたたみブロックで
function freeTextBlocks(freeText, keys) {
  const labels = {
    history: "経緯・沿革",
    capability_details: "能力の詳細",
    infrastructure_details: "インフラの詳細",
    targeting_details: "標的選定の詳細",
    additional_notes: "補足メモ",
  };
  let html = "";
  for (const key of keys) {
    const text = freeText?.[key];
    if (text && text.trim()) {
      html += `<details class="fold"><summary>${esc(labels[key] || key)}</summary>
        <div class="fold-body"><p class="small">${md(text)}</p></div></details>`;
    }
  }
  return html;
}

// 文字列配列ならチップ、オブジェクト配列ならテーブルで表示
function genericItems(items) {
  if (!items || !items.length) return "";
  if (typeof items[0] === "string") return chips(items);
  return softwareTable(items);
}

function softwareTable(items) {
  if (!items || !items.length) return "";
  return dataTable(
    ["名前", "別名", "種別", "概要"],
    items.map((m) => `<tr>
      <td><strong>${esc(m.name || m.id || "?")}</strong></td>
      <td class="small">${esc((m.aliases || []).filter((x) => x !== m.name).join(", "))}</td>
      <td class="small">${esc((m.types || []).map((t) => ja(t, "softwareType")).join(", "))}</td>
      <td class="small muted">${md((m.description || "").slice(0, 300))}</td>
    </tr>`).join("")
  );
}

/* ---------- ヘッダー ---------- */

function buildHeader(profile, summary, slug) {
  const actor = profile.actor || {};
  const attribution = profile.attribution || {};
  const badges = [];
  for (const c of attribution.countries || []) badges.push(`<span class="badge country">帰属: ${esc(ja(c, "country"))}</span>`);
  if (attribution.sponsor_type && attribution.sponsor_type !== "unknown") badges.push(`<span class="badge state">${esc(ja(attribution.sponsor_type, "sponsor"))}</span>`);
  for (const t of actor.actor_types || []) badges.push(`<span class="badge type">${esc(ja(t, "actorType"))}</span>`);
  badges.push(confBadge(attribution.confidence));

  return `<a class="back-link" href="#/">← アクター一覧へ戻る</a>
    <div class="actor-header">
      <h1>${esc(profile.name || summary.name)}</h1>
      <div class="actor-meta">${badges.join("")}<span class="sep">slug: <code>${esc(slug)}</code></span></div>
    </div>`;
}

/* ---------- overview タブ ---------- */

function buildOverviewTab(profile, summary) {
  const actor = profile.actor || {};
  const attribution = profile.attribution || {};
  const freeText = profile.free_text || {};
  const judgments = profile.assessment?.key_judgments || [];
  const targets = profile.targets || {};
  const dm = profile.diamond_model || {};

  const overview = `
    ${freeText.executive_summary ? `<p>${md(freeText.executive_summary)}</p>` : actor.description ? `<p>${md(actor.description)}</p>` : ""}
    <div class="kv-grid">
      <div class="kv"><div class="k">初観測</div><div class="v">${esc(fmtDate(actor.first_seen))}</div></div>
      <div class="kv"><div class="k">最終観測</div><div class="v">${esc(fmtDate(actor.last_seen))}</div></div>
      <div class="kv"><div class="k">活動状態</div><div class="v">${esc(ja(actor.active || "unknown", "active"))}</div></div>
      <div class="kv"><div class="k">プロファイル更新</div><div class="v">${esc(summary.updated_at || "不明")}</div></div>
    </div>
    ${freeTextBlocks(freeText, ["history", "targeting_details", "additional_notes"])}
  `;

  const judgmentsHtml = judgments
    .map((j) => `<div class="judgment">${md(jaNarrative(j.statement))}${confBadge(j.confidence)}</div>`)
    .join("");

  const attributionHtml = `
    <div class="kv-grid">
      <div class="kv"><div class="k">帰属国</div><div class="v">${esc((attribution.countries || []).map((c) => ja(c, "country")).join(", ") || "不明")}</div></div>
      <div class="kv"><div class="k">支援形態</div><div class="v">${esc(ja(attribution.sponsor_type || "unknown", "sponsor"))}</div></div>
      <div class="kv"><div class="k">確度</div><div class="v">${esc(ja(attribution.confidence || "unknown", "confidence"))}</div></div>
    </div>
    ${attribution.assessment ? `<p class="small muted">${md(jaNarrative(attribution.assessment))}</p>` : ""}
    ${(profile.motivations || []).length ? `<h3>動機</h3>${chips(profile.motivations.map((m) => ja(m.type, "motivation")))}` : ""}
  `;

  let diamondHtml = "";
  if (["adversary", "capability", "infrastructure", "victim"].some((k) => dm[k])) {
    const dmNode = (key, label, text) => `<div class="dm-node dm-${key}">
        <div class="k">${esc(label)}</div>
        <div class="v small">${text ? md(text) : '<span class="muted">情報なし</span>'}</div>
      </div>`;
    diamondHtml = `<div class="diamond-wrap">
        <svg class="diamond-lines" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
          <path d="M50 3 L97 50 L50 97 L3 50 Z" fill="none" stroke="currentColor" stroke-width="0.5"/>
          <path d="M50 3 L50 97 M3 50 L97 50" fill="none" stroke="currentColor" stroke-width="0.3" stroke-dasharray="1.5 2"/>
        </svg>
        ${dmNode("adversary", "攻撃者 (Adversary)", dm.adversary)}
        ${dmNode("infrastructure", "インフラ (Infrastructure)", dm.infrastructure)}
        ${dmNode("capability", "能力 (Capability)", dm.capability)}
        ${dmNode("victim", "被害者 (Victim)", dm.victim)}
        <div class="dm-center">ダイヤモンド<br>モデル</div>
      </div>
      ${dm.socio_political ? `<p class="small muted">社会・政治的背景: ${md(dm.socio_political)}</p>` : ""}`;
  }

  const targetsHtml = `
    <h3>標的国・地域(${(targets.countries || []).length})</h3>
    ${chips((targets.countries || []).map((t) => ja(t.name, "country")), "country")}
    <h3>標的産業(${(targets.sectors || []).length})</h3>
    ${chips((targets.sectors || []).map((t) => ja(t.name, "sector")), "type")}
    ${targets.selection_logic ? `<p class="small muted">選定ロジック: ${md(targets.selection_logic)}</p>` : ""}
  `;

  const parts = [section("概要", overview)];
  if ((actor.aliases || []).length) parts.push(section(`別名(${actor.aliases.length})`, chips(actor.aliases.map((a) => a.name || a))));
  if (judgmentsHtml) parts.push(section("主要判断", judgmentsHtml));
  parts.push(section("帰属・動機", attributionHtml));
  if (diamondHtml) parts.push(section("ダイヤモンドモデル", diamondHtml));
  parts.push(section("標的", targetsHtml));
  return parts.join("");
}

/* ---------- relations タブ ---------- */

function buildRelationsTab(profile, slug, incoming) {
  const outgoing = profile.relationships || [];
  const parts = [];
  if (!outgoing.length && !incoming.length) {
    parts.push('<p class="muted">記録された関係はありません。</p>');
  }
  if (outgoing.length) {
    parts.push(`<h3>このアクターが持つ関係(${outgoing.length})</h3>` + dataTable(
      ["相手アクター", "関係", "説明", "確度"],
      outgoing.map((r) => `<tr>
        <td>${actorLink(r.target_actor)}</td>
        <td class="small">${esc(ja(r.relationship_type || "", "relationship"))}</td>
        <td class="small muted">${md(r.description || "")}</td>
        <td class="small">${esc(ja(r.confidence || "", "confidence"))}</td>
      </tr>`).join("")
    ));
  }
  if (incoming.length) {
    parts.push(`<h3>このアクターを参照する関係(${incoming.length})</h3>` + dataTable(
      ["参照元アクター", "関係", "確度"],
      incoming.map((r) => `<tr>
        <td><a href="#/actor/${encodeURIComponent(r.from.slug)}">${esc(r.from.name)}</a></td>
        <td class="small">${esc(ja(r.type || "", "relationship"))}</td>
        <td class="small">${esc(ja(r.confidence || "", "confidence"))}</td>
      </tr>`).join("")
    ));
  }
  if (getGraph().nodes.has(slug)) {
    parts.push(`<p class="small"><a href="#/relations/${encodeURIComponent(slug)}">◇ 関係グラフでこのアクターを表示 →</a></p>`);
  }
  return section("他アクターとの関係", parts.join(""));
}

/* ---------- capabilities タブ ---------- */

function buildCapabilitiesTab(profile) {
  const c = profile.capabilities || {};
  const freeText = profile.free_text || {};
  const parts = [];
  if ((c.malware || []).length) parts.push(section(`マルウェア(${c.malware.length})`, softwareTable(c.malware)));
  if ((c.tools || []).length) parts.push(section(`ツール(${c.tools.length})`, softwareTable(c.tools)));
  if ((c.infrastructure || []).length) parts.push(section(`インフラ・サービス(${c.infrastructure.length})`, softwareTable(c.infrastructure)));
  if ((c.vulnerabilities || []).length) parts.push(section(`悪用脆弱性(${c.vulnerabilities.length})`, genericItems(c.vulnerabilities)));
  if ((c.delivery_formats || []).length) parts.push(section(`配送形式(${c.delivery_formats.length})`, genericItems(c.delivery_formats)));
  if ((c.operational_capabilities || []).length) parts.push(section(`作戦能力(${c.operational_capabilities.length})`, genericItems(c.operational_capabilities)));
  const folds = freeTextBlocks(freeText, ["capability_details", "infrastructure_details"]);
  if (folds) parts.push(section("詳細メモ", folds));
  if (!parts.length) parts.push(section("能力", '<p class="muted">記録された能力情報はありません。</p>'));
  return parts.join("");
}

/* ---------- ttps タブ(マトリックス表示) ---------- */

// tacticはカンマ区切りの複合値があるため分割し、各戦術の列へ振り分ける
function groupTtpsByTactic(ttps) {
  const groups = new Map();
  for (const t of ttps) {
    const tactics = String(t.tactic || "その他").split(",").map((s) => s.trim()).filter(Boolean);
    for (const tactic of tactics.length ? tactics : ["その他"]) {
      const key = tactic.toLowerCase();
      if (!groups.has(key)) groups.set(key, { label: jaTactic(tactic), items: [] });
      groups.get(key).items.push(t);
    }
  }
  const orderOf = (key) => {
    const i = TACTIC_ORDER.indexOf(key);
    return i === -1 ? 99 : i;
  };
  return [...groups.entries()].sort((a, b) => orderOf(a[0]) - orderOf(b[0]) || a[0].localeCompare(b[0]));
}

function buildTtpsTab(ttps) {
  if (!ttps || !ttps.length) return section("MITRE ATT&CK TTP", '<p class="muted">TTP情報なし</p>');
  const columns = groupTtpsByTactic(ttps).map(([, group]) => {
    // 同一Techniqueの重複をまとめる
    const byId = new Map();
    for (const t of group.items) {
      const id = t.technique_id || t.technique_name || "?";
      if (!byId.has(id)) byId.set(id, { ...t, count: 0 });
      byId.get(id).count += 1;
    }
    const cells = [...byId.values()]
      .sort((a, b) => String(a.technique_id).localeCompare(String(b.technique_id)))
      .map((t) => {
        const behavior = String(t.observed_behavior || "").replace(/\(Citation:[^)]*\)/g, " ").trim();
        return `<a class="ttp-cell" href="${t.technique_id ? mitreUrl(t.technique_id) : "#"}"
          target="_blank" rel="noopener" title="${esc(behavior.slice(0, 400))}">
          <span class="mono">${esc(t.technique_id || "")}</span>
          <span class="ttp-name">${esc(t.technique_name || "")}</span>
          ${t.count > 1 ? `<span class="ttp-count">×${t.count}</span>` : ""}
        </a>`;
      }).join("");
    return `<div class="ttp-col">
      <div class="ttp-col-head">${esc(group.label)}<span class="muted">${byId.size}</span></div>
      ${cells}
    </div>`;
  }).join("");
  return section(
    "MITRE ATT&CK マトリックス",
    `<p class="small muted">戦術ごとの観測Technique一覧です。セルにカーソルを乗せると観測内容、クリックでMITRE ATT&CKの解説を表示します。</p>
     <div class="ttp-matrix">${columns}</div>`
  );
}

/* ---------- activities タブ(タイムライン+期間フィルタ) ---------- */

const ACTIVITY_FILTERS = [
  { years: 0, label: "すべて" },
  { years: 1, label: "過去1年" },
  { years: 3, label: "過去3年" },
  { years: 5, label: "過去5年" },
  { years: 10, label: "過去10年" },
];

function knownDate(field) {
  return field?.status === "known" && field.value ? new Date(field.value) : null;
}

function activityDate(a) {
  return knownDate(a.last_observed) || knownDate(a.first_observed);
}

function activityPeriod(a) {
  const f = fmtDate(a.first_observed);
  const l = fmtDate(a.last_observed);
  if (f === "不明" && l === "不明") return "時期不明";
  if (f === l) return f;
  return `${f} 〜 ${l}`;
}

function timelineHtml(dated) {
  if (!dated.length) return '<p class="muted">該当期間に日付付きの活動はありません。</p>';
  return `<div class="timeline">${dated.map((a) => `
    <div class="tl-item">
      <div class="tl-date">${esc(activityPeriod(a))}</div>
      <div class="tl-title">${esc(a.name || "")}${a.activity_type ? ` <span class="badge type">${esc(ja(a.activity_type, "activityType"))}</span>` : ""}</div>
      ${a.description ? `<div class="small muted">${md(a.description)}</div>` : ""}
    </div>`).join("")}</div>`;
}

function buildActivitiesTab(profile) {
  const activities = profile.activities || [];
  if (!activities.length) return section("活動・キャンペーン", '<p class="muted">記録された活動はありません。</p>');
  const filters = ACTIVITY_FILTERS.map((f, i) =>
    `<button type="button" class="filter-btn ${i === 0 ? "active" : ""}" data-years="${f.years}">${f.label}</button>`).join("");
  return section(
    `活動・キャンペーン(${activities.length})`,
    `<div class="filter-row" id="act-filters">${filters}</div>
     <div id="act-area"></div>`
  );
}

// activities タブ表示後にタイムラインとフィルタを紐づける
function bindActivities(profile) {
  const area = document.getElementById("act-area");
  if (!area) return;
  const activities = profile.activities || [];
  const dated = activities
    .map((a) => ({ a, d: activityDate(a) }))
    .filter((x) => x.d)
    .sort((x, y) => y.d - x.d);
  const undated = activities.filter((a) => !activityDate(a));

  const render = (years) => {
    let rows = dated;
    if (years > 0) {
      const cutoff = new Date();
      cutoff.setFullYear(cutoff.getFullYear() - years);
      rows = dated.filter((x) => x.d >= cutoff);
    }
    area.innerHTML = `
      <p class="small muted">日付付き ${num(rows.length)} 件${years ? `(過去${years}年)` : ""} / 日付不明 ${num(undated.length)} 件</p>
      ${timelineHtml(rows.map((x) => x.a))}
      ${undated.length ? `<details class="fold"><summary>日付情報のない活動(${undated.length})</summary>
        <div class="fold-body">${dataTable(
          ["名称", "種別", "説明"],
          undated.map((a) => `<tr>
            <td><strong>${esc(a.name || "")}</strong></td>
            <td class="small">${esc(ja(a.activity_type || "", "activityType"))}</td>
            <td class="small muted">${md(a.description || "")}</td>
          </tr>`).join("")
        )}</div></details>` : ""}
    `;
  };

  document.querySelectorAll("#act-filters .filter-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll("#act-filters .filter-btn").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      render(Number(btn.dataset.years));
    });
  });
  render(0);
}

/* ---------- 技術的アーティファクト タブ(IOC+非IOCアーティファクト) ---------- */

function buildArtifactsTab(summary) {
  const parts = [];

  // IOC(正規化済みの機械可読指標)
  if (summary.counts.iocs) {
    const typeChips = Object.entries(summary.ioc_types)
      .sort((a, b) => b[1] - a[1])
      .map(([t, n]) => `<span class="badge">${esc(ja(t, "iocType"))}: ${num(n)}</span>`)
      .join("");
    parts.push(section(
      `IOC(${num(summary.counts.iocs)})`,
      `<div class="chip-list">${typeChips}</div>
       <p class="defanged-note">表示上の値は defang 済みです(hxxp / [.])。原値は iocs.json を参照してください。</p>
       <div id="ioc-area"><div class="more-row"><button class="load-btn" id="ioc-load" type="button">IOC ${num(summary.counts.iocs)} 件を読み込む</button></div></div>`
    ));
  } else {
    parts.push(section("IOC", '<p class="muted">このアクターに正規化済みIOCはありません。</p>'));
  }

  // 非IOCアーティファクト(コマンド、検体内文字列、パス等 — IOCとしては使いづらい痕跡)
  if (summary.counts.artifacts) {
    parts.push(section(
      `非IOCアーティファクト(${num(summary.counts.artifacts)})`,
      `<p class="small muted">実行コマンド、検体内文字列、ファイル名・パス、レジストリキーなど、単体ではIOCとして使いづらい技術的痕跡です。
       多くは自動抽出された候補であり、検知利用の前に出典の文脈確認が必要です。</p>
       <div id="artifact-area"><div class="more-row"><button class="load-btn" id="artifact-load" type="button">アーティファクト ${num(summary.counts.artifacts)} 件を読み込む</button></div></div>`
    ));
  } else {
    parts.push(section("非IOCアーティファクト", '<p class="muted">このアクターに記録された非IOCアーティファクトはありません。</p>'));
  }

  return parts.join("");
}

async function loadArtifacts(slug, summary) {
  const area = document.getElementById("artifact-area");
  area.innerHTML = '<div class="loading">アーティファクトを読み込み中…</div>';
  let rows0;
  try {
    if (state.artifactCache.has(slug)) {
      rows0 = state.artifactCache.get(slug);
    } else {
      const text = await fetchText(`${PROFILES_BASE}/${encodeURIComponent(slug)}/artifacts.csv`);
      rows0 = parseCsv(text);
      state.artifactCache.set(slug, rows0);
    }
  } catch (err) {
    area.innerHTML = `<div class="error-box">${esc(err.message)}</div>`;
    return;
  }

  const typeCounts = new Map();
  for (const r of rows0) {
    const t = r.artifact_type || "other";
    typeCounts.set(t, (typeCounts.get(t) || 0) + 1);
  }
  const types = [...typeCounts.keys()].sort();
  const view = { q: "", type: "", limit: IOC_PAGE };

  const render = () => {
    const q = view.q.trim().toLowerCase();
    const rows = rows0.filter((r) =>
      (!view.type || r.artifact_type === view.type) &&
      (!q || String(r.value || "").toLowerCase().includes(q)));
    const shown = rows.slice(0, view.limit);
    area.innerHTML = `
      <div class="ioc-controls">
        <input type="search" id="artifact-q" placeholder="アーティファクト値で絞り込み…" value="${esc(view.q)}" autocomplete="off">
        <select id="artifact-type">
          <option value="">種別: すべて</option>
          ${types.map((t) => `<option value="${esc(t)}" ${t === view.type ? "selected" : ""}>${esc(ja(t, "artifactType"))} (${num(typeCounts.get(t))})</option>`).join("")}
        </select>
      </div>
      ${resultCount(rows.length, shown.length)}
      ${dataTable(
        ["種別", "値", "状態", "確度", "観測日", "出典"],
        shown.map((r) => `<tr>
          <td class="small">${esc(ja(r.artifact_type, "artifactType"))}</td>
          <td><span class="mono" title="${esc((r.context_excerpt || "").slice(0, 400))}">${esc(String(r.value || "").slice(0, 240))}</span></td>
          <td class="small">${esc(ja(r.disposition || "", "disposition"))}</td>
          <td class="small">${esc(ja(r.confidence || "", "confidence"))}</td>
          <td class="small">${esc(r.observed_at ? String(r.observed_at).slice(0, 10) : "不明")}</td>
          <td class="small muted">${esc((r.source_path || "").split("/").pop())}</td>
        </tr>`).join("")
      )}
      ${rows.length > shown.length ? '<div class="more-row"><button class="more-btn" id="artifact-more" type="button">さらに表示</button></div>' : ""}
    `;
    bindLiveSearch("artifact-q", (value) => { view.q = value; view.limit = IOC_PAGE; render(); });
    document.getElementById("artifact-type").addEventListener("change", (e) => {
      view.type = e.target.value; view.limit = IOC_PAGE; render();
    });
    bindMoreButton("artifact-more", () => { view.limit += IOC_PAGE * 2; render(); });
  };
  render();
}

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
          ${types.map((t) => `<option value="${esc(t)}" ${t === view.type ? "selected" : ""}>${esc(ja(t, "iocType"))} (${num(summary.ioc_types[t])})</option>`).join("")}
        </select>
      </div>
      ${resultCount(rows.length, shown.length)}
      ${dataTable(
        ["種別", "値(defang済)", "状態", "観測数", "初観測", "最終観測"],
        shown.map((ind) => `<tr>
          <td class="small">${esc(ja(ind.type, "iocType"))}</td>
          <td><span class="mono">${esc(defang(ind.value, ind.type))}</span></td>
          <td class="small">${esc(ja(ind.disposition || "", "disposition"))}</td>
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

/* ---------- sources タブ ---------- */

function buildSourcesTab(profile, slug) {
  const sources = profile.sources || [];
  const parts = [];
  if (sources.length) {
    parts.push(section(`出典(${sources.length})`, dataTable(
      ["タイトル", "発行元", "発行日", "種別"],
      sources.map((s) => `<tr>
        <td class="small">${esc(s.title || s.source_id || "")}</td>
        <td class="small">${esc(s.publisher || "")}</td>
        <td class="small">${esc(fmtDate(s.published_at))}</td>
        <td class="small">${esc(ja(s.source_type || "", "sourceType"))}</td>
      </tr>`).join("")
    )));
  }
  const base = `${PROFILES_BASE}/${encodeURIComponent(slug)}`;
  const blob = `${REPO_BLOB}/profiles/${encodeURIComponent(slug)}`;
  parts.push(section("データダウンロード", `<div class="dl-links">
      <a href="${base}/actor-profile.json" download>actor-profile.json</a>
      <a href="${base}/iocs.json" download>iocs.json</a>
      <a href="${base}/generated/profile.stix2.json" download>STIX 2.1 Bundle</a>
      <a href="${blob}/generated/profile-ja.md" target="_blank" rel="noopener">日本語プロファイル (GitHub) ↗</a>
      <a href="${blob}/claim-audit.json" target="_blank" rel="noopener">主張監査 (GitHub) ↗</a>
      <a href="${blob}/artifacts.csv" target="_blank" rel="noopener">artifacts.csv (GitHub) ↗</a>
    </div>`));
  return parts.join("");
}

/* ---------- エントリポイント ---------- */

export async function renderActor(slug, initialTab) {
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

  const c = profile.capabilities || {};
  const incoming = incomingRelationships(slug);
  const relCount = (profile.relationships || []).length + incoming.length;
  const capCount = (c.malware || []).length + (c.tools || []).length + (c.infrastructure || []).length +
    (c.vulnerabilities || []).length + (c.delivery_formats || []).length + (c.operational_capabilities || []).length;

  const tabs = [
    { id: "overview", label: "概要", build: () => buildOverviewTab(profile, summary) },
    { id: "relations", label: `関係 (${relCount})`, build: () => buildRelationsTab(profile, slug, incoming), empty: !relCount },
    { id: "capabilities", label: `能力 (${capCount})`, build: () => buildCapabilitiesTab(profile), empty: !capCount },
    { id: "ttps", label: `TTP (${(profile.ttps || []).length})`, build: () => buildTtpsTab(profile.ttps), empty: !(profile.ttps || []).length },
    { id: "activities", label: `活動 (${(profile.activities || []).length})`, build: () => buildActivitiesTab(profile), empty: !(profile.activities || []).length, bind: () => bindActivities(profile) },
    { id: "artifacts", label: `技術的アーティファクト (${num(summary.counts.iocs + summary.counts.artifacts)})`, build: () => buildArtifactsTab(summary), bind: () => {
        const iocBtn = document.getElementById("ioc-load");
        if (iocBtn) iocBtn.addEventListener("click", () => loadIocs(slug, summary));
        const artifactBtn = document.getElementById("artifact-load");
        if (artifactBtn) artifactBtn.addEventListener("click", () => loadArtifacts(slug, summary));
      } },
    { id: "sources", label: `出典 (${(profile.sources || []).length})`, build: () => buildSourcesTab(profile, slug) },
  ].filter((t) => !t.empty);

  if (initialTab === "iocs") initialTab = "artifacts"; // 旧URL互換
  const validIds = new Set(tabs.map((t) => t.id));
  let current = validIds.has(initialTab) ? initialTab : "overview";

  app.innerHTML = `
    ${buildHeader(profile, summary, slug)}
    <nav class="tab-bar" id="tab-bar">
      ${tabs.map((t) => `<button type="button" class="tab-btn" data-tab="${t.id}">${esc(t.label)}</button>`).join("")}
    </nav>
    <div id="tab-content"></div>
  `;

  const content = document.getElementById("tab-content");
  const showTab = (id, updateHash) => {
    const tab = tabs.find((t) => t.id === id) || tabs[0];
    current = tab.id;
    document.querySelectorAll("#tab-bar .tab-btn").forEach((b) =>
      b.classList.toggle("active", b.dataset.tab === tab.id));
    content.innerHTML = tab.build();
    if (tab.bind) tab.bind();
    if (updateHash) {
      const suffix = tab.id === "overview" ? "" : `/${tab.id}`;
      history.replaceState(null, "", `#/actor/${encodeURIComponent(slug)}${suffix}`);
    }
  };

  document.querySelectorAll("#tab-bar .tab-btn").forEach((btn) => {
    btn.addEventListener("click", () => showTab(btn.dataset.tab, true));
  });

  showTab(current, false);
  window.scrollTo(0, 0);
}
