/* 関係グラフビュー: Canvas上の力学レイアウト(外部ライブラリなし)
 *
 * 構成:
 *   buildPageHtml()      … ページ骨格・凡例
 *   createSimulation()   … 反発・ばね・重力の物理シミュレーション
 *   renderGraph()        … 描画ループとポインタ・ズーム・検索のバインド
 */

import {
  EDGE_COLORS, EDGE_FALLBACK_COLOR,
  COUNTRY_PALETTE, UNKNOWN_COUNTRY, UNKNOWN_COUNTRY_COLOR,
} from "./config.js";
import { state, getGraph } from "./data.js";
import { app, esc, num } from "./util.js";

function countryColors(nodeArr) {
  const countries = [...new Set(nodeArr.map((n) => n.country))]
    .sort((a, b) => (a === UNKNOWN_COUNTRY) - (b === UNKNOWN_COUNTRY) || a.localeCompare(b));
  const colorOf = {};
  let i = 0;
  for (const c of countries) {
    colorOf[c] = c === UNKNOWN_COUNTRY ? UNKNOWN_COUNTRY_COLOR : COUNTRY_PALETTE[i++ % COUNTRY_PALETTE.length];
  }
  return { countries, colorOf };
}

function buildPageHtml(nodeArr, edges, countries, colorOf) {
  const typesPresent = [...new Set(edges.map((e) => e.type))];
  return `
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
        ${typesPresent.map((t) => `<span class="lg"><span class="sw-line ${t === "distinct-from" ? "dashed" : ""}" style="border-color:${EDGE_COLORS[t] || EDGE_FALLBACK_COLOR}"></span>${esc(t)}</span>`).join("")}
      </div>
      <div class="graph-legend">
        ${countries.map((c) => `<span class="lg"><span class="sw-dot" style="background:${colorOf[c]}"></span>${esc(c)}</span>`).join("")}
      </div>
    </section>`;
}

// 次数の大きいノードを内側にした同心円(黄金角)で初期配置
function seedPositions(nodeArr) {
  const sorted = [...nodeArr].sort((a, b) => b.deg - a.deg);
  sorted.forEach((n, i) => {
    const r = 40 + 26 * Math.sqrt(i);
    const th = i * 2.39996;
    n.x = r * Math.cos(th);
    n.y = r * Math.sin(th);
    n.vx = 0; n.vy = 0;
  });
}

function createSimulation(nodeArr, edges, nodeOf) {
  const sim = {
    alpha: 1,
    dragNode: null,
    boost(v) { sim.alpha = Math.max(sim.alpha, v); },
    tick() {
      // ノード間の反発
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
      // エッジのばね
      for (const e of edges) {
        const a = nodeOf(e.a), b = nodeOf(e.b);
        const dx = b.x - a.x, dy = b.y - a.y;
        const d = Math.max(Math.sqrt(dx * dx + dy * dy), 1);
        const f = (d - 120) * 0.02;
        a.vx += (dx / d) * f; a.vy += (dy / d) * f;
        b.vx -= (dx / d) * f; b.vy -= (dy / d) * f;
      }
      // 中心への重力と減衰
      for (const n of nodeArr) {
        n.vx -= n.x * 0.004; n.vy -= n.y * 0.004;
        n.vx *= 0.82; n.vy *= 0.82;
        if (n !== sim.dragNode) { n.x += n.vx * sim.alpha; n.y += n.vy * sim.alpha; }
      }
      sim.alpha = Math.max(sim.alpha * 0.995, 0.03);
    },
    warmup(steps) { for (let i = 0; i < steps; i++) sim.tick(); },
  };
  return sim;
}

export function renderGraph(initialFocus) {
  document.title = "関係グラフ | Threat Actor Intelligence Profiles";
  const g = getGraph();
  const nodeArr = [...g.nodes.values()];
  const edges = g.edges;
  const nodeOf = (slug) => g.nodes.get(slug);
  const { countries, colorOf } = countryColors(nodeArr);

  app.innerHTML = buildPageHtml(nodeArr, edges, countries, colorOf);

  const canvas = document.getElementById("g-canvas");
  const tip = document.getElementById("g-tip");
  const box = canvas.parentElement;
  const dpr = window.devicePixelRatio || 1;
  let W = box.clientWidth, H = box.clientHeight;
  canvas.width = W * dpr;
  canvas.height = H * dpr;
  const ctx = canvas.getContext("2d");

  seedPositions(nodeArr);
  const sim = createSimulation(nodeArr, edges, nodeOf);
  sim.warmup(200); // 描画前にレイアウトを収束させる

  const view = { k: 1, tx: W / 2, ty: H / 2 };
  let focusSlug = null;
  let neighborSet = new Set();
  let hoverNode = null;

  const radiusOf = (n) => Math.min(5 + n.deg * 1.6, 16);

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

  function draw() {
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);
    ctx.setTransform(dpr * view.k, 0, 0, dpr * view.k, dpr * view.tx, dpr * view.ty);

    for (const e of edges) {
      const a = nodeOf(e.a), b = nodeOf(e.b);
      const active = !focusSlug || e.a === focusSlug || e.b === focusSlug;
      ctx.globalAlpha = active ? 0.75 : 0.08;
      ctx.strokeStyle = EDGE_COLORS[e.type] || EDGE_FALLBACK_COLOR;
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

    ctx.font = `${11 / view.k}px "Hiragino Kaku Gothic ProN", system-ui, sans-serif`;
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
    sim.tick();
    draw();
    state.graphAnim = requestAnimationFrame(loop);
  }

  /* ---- ポインタ操作: ノードドラッグ / 背景パン / クリックで詳細へ ---- */
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
  const localXY = (ev) => {
    const rect = canvas.getBoundingClientRect();
    return { mx: ev.clientX - rect.left, my: ev.clientY - rect.top };
  };

  let pointer = null; // {mx, my, moved}
  canvas.addEventListener("pointerdown", (ev) => {
    const { mx, my } = localXY(ev);
    pointer = { mx, my, moved: 0 };
    sim.dragNode = findNode(mx, my);
    canvas.classList.add("dragging");
    canvas.setPointerCapture(ev.pointerId);
    if (sim.dragNode) sim.boost(0.3);
  });
  canvas.addEventListener("pointermove", (ev) => {
    const { mx, my } = localXY(ev);
    if (pointer) {
      const dx = mx - pointer.mx, dy = my - pointer.my;
      pointer.moved += Math.abs(dx) + Math.abs(dy);
      if (sim.dragNode) {
        const w = toWorld(mx, my);
        sim.dragNode.x = w.x; sim.dragNode.y = w.y;
        sim.dragNode.vx = 0; sim.dragNode.vy = 0;
        sim.boost(0.25);
      } else {
        view.tx += dx; view.ty += dy;
      }
      pointer.mx = mx; pointer.my = my;
      return;
    }
    hoverNode = findNode(mx, my);
    canvas.style.cursor = hoverNode ? "pointer" : "grab";
    if (hoverNode) {
      const a = state.bySlug.get(hoverNode.slug);
      tip.style.display = "block";
      tip.style.left = Math.min(mx + 14, W - 290) + "px";
      tip.style.top = (my + 14) + "px";
      tip.innerHTML = `<div class="t-name">${esc(hoverNode.name)}</div>
        <div>${esc(hoverNode.country)} / 関係 ${hoverNode.deg} 本</div>
        ${a && a.aliases.length ? `<div class="muted">別名: ${esc(a.aliases.slice(0, 3).join(", "))}</div>` : ""}
        <div class="muted">クリックで詳細ページへ</div>`;
    } else {
      tip.style.display = "none";
    }
  });
  canvas.addEventListener("pointerup", () => {
    if (!pointer) return;
    const clicked = pointer.moved < 5 ? findNode(pointer.mx, pointer.my) : null;
    pointer = null;
    sim.dragNode = null;
    canvas.classList.remove("dragging");
    if (clicked) location.hash = `#/actor/${encodeURIComponent(clicked.slug)}`;
  });
  canvas.addEventListener("pointercancel", () => {
    pointer = null;
    sim.dragNode = null;
    canvas.classList.remove("dragging");
  });
  canvas.addEventListener("pointerleave", () => { hoverNode = null; tip.style.display = "none"; });

  canvas.addEventListener("wheel", (ev) => {
    ev.preventDefault();
    const { mx, my } = localXY(ev);
    const factor = Math.exp(-ev.deltaY * 0.0012);
    const k2 = Math.min(Math.max(view.k * factor, 0.15), 5);
    view.tx = mx - ((mx - view.tx) / view.k) * k2;
    view.ty = my - ((my - view.ty) / view.k) * k2;
    view.k = k2;
  }, { passive: false });

  /* ---- 検索フォーカスとリサイズ ---- */
  document.getElementById("g-search").addEventListener("change", (ev) => {
    const q = ev.target.value.trim().toLowerCase();
    if (!q) return;
    const n = nodeArr.find((x) => x.name.toLowerCase() === q) ||
      nodeArr.find((x) => x.name.toLowerCase().includes(q));
    if (n) { setFocus(n.slug, true); sim.boost(0.1); }
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
