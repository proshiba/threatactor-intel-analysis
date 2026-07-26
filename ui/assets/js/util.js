/* DOM非依存の整形ヘルパーと、複数ビューで共有する小さなUI部品 */

import { ja } from "./locale-ja.js";

export const app = document.getElementById("app");

export function esc(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
}

// escape + minimal markdown ([label](url) のみリンク化、(Citation: …) は除去)
export function md(text) {
  return esc(String(text ?? "").replace(/\(Citation:[^)]*\)/g, " ")).replace(
    /\[([^\]]+)\]\((https?:\/\/[^)\s]+)\)/g,
    '<a href="$2" target="_blank" rel="noopener">$1</a>'
  );
}

// {value, precision, status, ...} 形式の日付フィールドを表示用文字列へ
export function fmtDate(field) {
  if (field && typeof field === "object") {
    if (field.status === "known" && field.value) return String(field.value).slice(0, 10);
    return "不明";
  }
  return field ? String(field).slice(0, 10) : "不明";
}

export function confBadge(confidence) {
  const c = (confidence || "unknown").toLowerCase();
  const label = { high: "high", medium: "medium", low: "low" }[c] || "unknown";
  return `<span class="badge conf-${esc(label)}">確度: ${esc(ja(confidence || "unknown", "confidence"))}</span>`;
}

export function defang(value, type) {
  let v = String(value ?? "");
  if (["domain", "url", "email", "ipv4", "ipv6"].includes(type)) {
    v = v.replace(/^http/i, "hxxp").replace(/\./g, "[.]").replace(/@/g, "[@]");
  }
  return v;
}

export function num(n) { return Number(n || 0).toLocaleString("ja-JP"); }

export function chips(items, cls) {
  if (!items || !items.length) return '<span class="muted small">情報なし</span>';
  return '<div class="chip-list">' +
    items.map((x) => `<span class="badge ${cls || ""}">${esc(x)}</span>`).join("") +
    "</div>";
}

export function section(title, bodyHtml) {
  return `<section class="section"><h2>${esc(title)}</h2>${bodyHtml}</section>`;
}

// ヘッダ配列と<tr>…</tr>連結済みHTMLからテーブルを組み立てる
export function dataTable(headers, rowsHtml) {
  return `<div class="tbl-wrap"><table class="data">
    <thead><tr>${headers.map((h) => `<th>${esc(h)}</th>`).join("")}</tr></thead>
    <tbody>${rowsHtml}</tbody></table></div>`;
}

export function resultCount(total, shown) {
  return `<div class="result-count">${num(total)} 件該当${total !== shown ? `(${num(shown)} 件表示中)` : ""}</div>`;
}

export async function fetchJson(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`${url} の取得に失敗しました (HTTP ${res.status})`);
  return res.json();
}

export async function fetchText(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`${url} の取得に失敗しました (HTTP ${res.status})`);
  return res.text();
}

// RFC 4180準拠の簡易CSVパーサ(引用符内のカンマ・改行・二重引用符に対応)。
// 1行目をヘッダとしてオブジェクト配列を返す。
export function parseCsv(text) {
  const rows = [];
  let row = [];
  let field = "";
  let inQuotes = false;
  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    if (inQuotes) {
      if (ch === '"') {
        if (text[i + 1] === '"') { field += '"'; i++; }
        else inQuotes = false;
      } else {
        field += ch;
      }
    } else if (ch === '"') {
      inQuotes = true;
    } else if (ch === ",") {
      row.push(field); field = "";
    } else if (ch === "\n" || ch === "\r") {
      if (ch === "\r" && text[i + 1] === "\n") i++;
      row.push(field); field = "";
      if (row.length > 1 || row[0] !== "") rows.push(row);
      row = [];
    } else {
      field += ch;
    }
  }
  if (field !== "" || row.length) { row.push(field); rows.push(row); }
  if (!rows.length) return [];
  const header = rows[0];
  return rows.slice(1).map((r) => {
    const obj = {};
    header.forEach((h, i) => { obj[h] = r[i] ?? ""; });
    return obj;
  });
}

export function renderError(message) {
  app.innerHTML = `<div class="error-box"><strong>エラー:</strong> ${esc(message)}<br>
    <a href="#/">一覧へ戻る</a></div>`;
}

// 検索ボックス: デバウンス後にコールバック→(再描画で要素が作り直されるため)カーソルを末尾へ復元
export function bindLiveSearch(id, onValue, delay = 150) {
  const el = document.getElementById(id);
  if (!el) return;
  let timer = null;
  el.addEventListener("input", (e) => {
    clearTimeout(timer);
    timer = setTimeout(() => {
      onValue(e.target.value);
      const box = document.getElementById(id);
      if (box) {
        box.focus();
        box.setSelectionRange(box.value.length, box.value.length);
      }
    }, delay);
  });
}

// 「さらに表示」: 再描画してもスクロール位置を保つ
export function bindMoreButton(id, onMore) {
  const btn = document.getElementById(id);
  if (!btn) return;
  btn.addEventListener("click", () => {
    const y = window.scrollY;
    onMore();
    window.scrollTo(0, y);
  });
}
