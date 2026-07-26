/* アプリ状態と索引データ・関係グラフデータへのアクセス */

import { LIST_PAGE, DEFAULT_FILTERS, UNKNOWN_COUNTRY } from "./config.js";
import { fetchJson } from "./util.js";

export const state = {
  index: null,          // data/actors.json payload
  currentView: null,    // "list" | "actor" | "graph"
  bySlug: new Map(),    // slug -> 索引レコード
  nameToSlug: new Map(),// 正規名/alias(小文字) -> slug
  graph: null,          // {nodes: Map, edges: []} 遅延構築
  graphAnim: null,      // requestAnimationFrame handle
  filters: { ...DEFAULT_FILTERS },
  listLimit: LIST_PAGE,
  listScroll: 0,
  profileCache: new Map(),
  iocCache: new Map(),
  artifactCache: new Map(),
};

export function resetFilters() {
  state.filters = { ...DEFAULT_FILTERS };
}

export async function loadIndex() {
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
  return data;
}

export function findActor(slug) {
  return state.bySlug.get(slug) || null;
}

export function slugForName(name) {
  return state.nameToSlug.get(String(name || "").toLowerCase()) || null;
}

// 索引の relationships からノード・エッジを構築(無向・種別単位で重複除去)
export function getGraph() {
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

// slugを参照先に持つ関係(被参照)を索引から集める
export function incomingRelationships(slug) {
  const incoming = [];
  for (const other of state.index.actors) {
    if (other.slug === slug) continue;
    for (const r of other.relationships || []) {
      if (r.target_slug === slug) incoming.push({ from: other, type: r.type, confidence: r.confidence });
    }
  }
  return incoming;
}
