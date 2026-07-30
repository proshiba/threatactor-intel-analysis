/* サイト全体で共有する定数 */

export const REPO_URL = "https://github.com/proshiba/threatactor-intel-analysis";
export const REPO_BLOB = REPO_URL + "/blob/main";
export const PROFILES_BASE = "../profiles";

export const LIST_PAGE = 96;   // 一覧の1ページあたり表示件数
export const IOC_PAGE = 200;   // IOCテーブルの1ページあたり表示件数

export const DEFAULT_FILTERS = Object.freeze({
  q: "", country: "", sponsor: "", type: "", motivation: "", sector: "", sort: "name",
});

// MITRE ATT&CK の戦術表示順(小文字で比較)
export const TACTIC_ORDER = [
  "reconnaissance", "resource development", "initial access", "execution",
  "persistence", "privilege escalation", "stealth", "defense impairment",
  "defense evasion", "credential access",
  "discovery", "lateral movement", "collection", "command and control",
  "exfiltration", "impact",
];

/* 関係グラフの配色 */
export const EDGE_COLORS = {
  "overlaps-with": "#fbbf24",
  "related-to": "#4cc2ff",
  "cooperates-with": "#34d399",
  "shares-tools-with": "#2dd4bf",
  "part-of": "#a78bfa",
  "distinct-from": "#f87171",
};
export const EDGE_FALLBACK_COLOR = "#8b9ab5";
export const COUNTRY_PALETTE = ["#f87171", "#fbbf24", "#a78bfa", "#34d399", "#4cc2ff", "#f472b6", "#fb923c", "#e2e8f0"];
export const UNKNOWN_COUNTRY = "帰属不明";
export const UNKNOWN_COUNTRY_COLOR = "#64748b";

/* 横断ポータル(proshiba/research_bench)。IOCからクロスサーチへ飛ばすために使う。
 * ポータルは #/search/<検索語> で横断検索し、アプリを同一オリジンのiframeで表示する。 */
export const PORTAL_URL = "https://proshiba.github.io/research_bench/";
export const PORTAL_SEARCH_ROUTE = "#/search/";
