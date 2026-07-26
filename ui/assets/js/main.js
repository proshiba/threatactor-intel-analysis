/* エントリポイント: 索引の読み込みとハッシュルーティング
 *
 * データソース:
 *   - ui/data/actors.json                   (build_data.py が生成する索引)
 *   - ../profiles/<slug>/actor-profile.json (詳細表示時に取得)
 *   - ../profiles/<slug>/iocs.json          (IOCセクションで遅延取得)
 */

import { state, loadIndex } from "./data.js";
import { num, renderError } from "./util.js";
import { renderList } from "./view-list.js";
import { renderActor } from "./view-actor.js";
import { renderGraph } from "./view-graph.js";

const ROUTES = [
  {
    pattern: /^#\/actor\/([A-Za-z0-9._-]+)/,
    view: "actor",
    render: (m) => renderActor(decodeURIComponent(m[1])),
  },
  {
    pattern: /^#\/relations(?:\/([A-Za-z0-9._-]+))?/,
    view: "graph",
    render: (m) => renderGraph(m[1] ? decodeURIComponent(m[1]) : null),
  },
];

function route() {
  if (state.graphAnim) {
    cancelAnimationFrame(state.graphAnim);
    state.graphAnim = null;
  }
  const hash = location.hash || "#/";
  for (const r of ROUTES) {
    const m = hash.match(r.pattern);
    if (m) {
      // 一覧から離れるときはスクロール位置を保存(戻ったとき復元)
      if (state.currentView === "list") state.listScroll = window.scrollY;
      state.currentView = r.view;
      r.render(m);
      return;
    }
  }
  state.currentView = "list";
  renderList();
}

async function boot() {
  try {
    const data = await loadIndex();
    const meta = document.getElementById("footer-meta");
    if (meta) meta.textContent = `索引生成: ${data.generated_at} / アクター ${num(data.stats.actors)} 件`;
    route();
  } catch (err) {
    renderError(err.message);
  }
}

window.addEventListener("hashchange", route);
boot();
