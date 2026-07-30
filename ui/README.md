# Threat Actor Intelligence Profiles — GitHub Pages UI

`profiles/` 配下の脅威アクタープロファイルをブラウザで閲覧するための静的UIです。
ビルド不要のVanilla JS製SPA(ハッシュルーティング)で、コードはすべて `ui/` に収まっています。

## 構成

```text
ui/
├── index.html          # エントリポイント(一覧・詳細・グラフを1ページで切替)
├── assets/
│   ├── js/             # ESモジュール構成のSPA本体
│   │   ├── main.js         # 起動とハッシュルーティング
│   │   ├── config.js       # 定数(パス、ページサイズ、配色、ATT&CK戦術順)
│   │   ├── util.js         # 整形ヘルパーと共有UI部品(テーブル、検索、ページング)
│   │   ├── data.js         # アプリ状態、索引読込、関係グラフデータ構築
│   │   ├── view-list.js    # 一覧ビュー(統計・検索・フィルタ・ソート)
│   │   ├── view-actor.js   # 詳細ビュー(セクションビルダー群+IOC遅延読込)
│   │   └── view-graph.js   # 関係グラフビュー(Canvas力学レイアウト)
│   └── style.css       # ダークテーマのスタイル
├── data/
│   └── actors.json     # 検索・フィルタ用の軽量索引(build_data.pyで生成)
├── api/v1/             # ポータル連携用の静的インデックス(build_portal_index.pyで生成)
│   ├── meta.json           # 自己紹介(ポータルが最初に読む)
│   └── search.json         # 横断検索用エンティティ集合
├── build_data.py       # UI用索引の生成スクリプト
└── build_portal_index.py   # ポータル用インデックスの生成スクリプト
```

- **一覧ページ**: 全アクターの統計、名前・alias・slug検索、帰属国 / 支援形態 /
  アクター種別 / 動機 / 標的産業のフィルタ、各種ソート。
- **詳細ページ** (`#/actor/<slug>[/タブ]`): `profiles/<slug>/actor-profile.json` を実行時に取得し、
  タブで表示します(空のタブは自動的に非表示、タブはURLで直接指定可能)。
  - **概要**: 日本語要約、別名、主要判断、帰属・動機、ダイヤモンドモデル(ひし形レイアウト)、標的
  - **関係**: 他アクターとの関係(発信・被参照の双方向、相互リンク・グラフへのリンク付き)
  - **能力**: マルウェア、ツール、インフラ・サービス、脆弱性など。マルウェアは
    all time / 過去3年 / 過去1年で活動単位の利用件数と最終観測を表示
  - **TTP**: ATT&CK マトリックス表示。all time / 過去3年 / 過去1年で
    異なる攻撃活動の観測数を集計し、頻度が高いセルほど赤く表示
  - **活動・被害**: 活動履歴のタイムラインと、活動・標的・マルウェア・TTP・
    影響資産を結んだ被害事例(過去1/3/5/10年の期間フィルタ、日付不明分は別掲)
  - **技術的アーティファクト**: IOC(遅延読み込み+種別・値フィルタ、defang表示、
    値をクリックすると横断ポータルのクロスサーチへ)と、
    非IOCアーティファクト(コマンド、検体内文字列、パス、レジストリキー等の
    IOCとしては使いづらい痕跡。artifacts.csv を遅延読み込みして絞り込み表示)
  - **出典**: 出典一覧とデータダウンロード
- **関係グラフ** (`#/relations`、ヘッダーからも遷移可): 全プロファイルの
  アクター間関係を力学レイアウトのグラフで表示。エッジ色は関係種別
  (overlaps-with / related-to / cooperates-with など)、ノード色は帰属国。
  ノードクリックで詳細ページへ、`#/relations/<slug>` で特定アクターに
  フォーカスした状態で開けます(詳細ページの関係セクションからリンクあり)。
- **IOC**: 件数が多いためボタン押下で `iocs.json` を遅延読み込みし、
  種別・値で絞り込み表示します。表示値はdefang済み(`hxxp` / `[.]`)です。

## GitHub Pages での公開

**Settings → Pages** の Source を `GitHub Actions` に設定してください。
`main` へのプッシュごとに [.github/workflows/deploy-pages.yml](../.github/workflows/deploy-pages.yml)
が実行され、以下を行います(手動実行は Actions タブの `workflow_dispatch` から)。

1. `python3 ui/build_data.py` で索引 `ui/data/actors.json` を再生成
   (このためプロファイル更新時に手元で再生成し忘れても、公開サイトは常に最新です)
2. `ui/` と `profiles/` をサイトとして組み立て(ルートには `/ui/` へのリダイレクトを配置)
3. Pages へデプロイ

UIは `profiles/` 配下のJSONを相対パスで読むため、`profiles/` も一緒に配信されます。
公開URLは `https://<user>.github.io/<repo>/ui/`(ルートアクセスは自動で `/ui/` へ)。

## 索引の再生成(ローカル確認用)

デプロイ時に自動再生成されますが、ローカルで動作確認する場合は手動で実行できます。

```bash
python3 ui/build_data.py
```

`profiles/*/actor-profile.json`・`iocs.json`・`artifacts.csv` を読み、
`ui/data/actors.json`(名称、alias、帰属、動機、標的、各種件数、IOC種別内訳、
slug解決済みのアクター間関係)を出力します。
`generated_at`には全プロファイル中の最新`updated_at`を使用するため、入力が同じなら
再実行しても索引ファイルは変化しません。

## ポータル連携用インデックス (spec v1)

別リポジトリのポータル(`proshiba/research_bench`)は、各アプリが GitHub Pages に置いた
静的 JSON を `fetch()` して手元で索引し、**同じ値が複数ソースに現れたこと**を検出して
横串を作ります。そのための索引を `ui/api/v1/` に公開しています。

| パス | 内容 |
| --- | --- |
| `ui/api/v1/meta.json` | 自己紹介(アプリ名、`site_url`、`deep_links`、`embed_css`、件数) |
| `ui/api/v1/search.json` | 索引本体。全アクター横断で集約したエンティティ集合 |

収録するエンティティは `actor` / `malware` / `tool` / `cve` / `ttp` / `campaign` / `ioc.*` です。
マルウェア名・IOC・CVE が他アプリとの結合キーになるため、**同じ値は 1 エンティティに畳み、
観測元アクター全部を `refs` に並べます**。IOC の値は難読化(defang)を解除して格納します。

`artifacts.csv` の非IOCアーティファクトは、誤結合を招きやすく横串の価値が薄いため
索引に入れていません。

出典レポート自身の参考リンク（ベンダーブログ、CERT、報道サイトのURL）、公開サフィックス単体、
到達不能・予約済みアドレスもIOCではないため除外します。判定は取り込み側と同じ
[reference-hosts.json](../actor_profile/reference/reference-hosts.json)を共有し、
規約は[RULES.md の 8. IOCモデル](../actor_profile/RULES.md)にあります。
原典レポートはリポジトリに含まれず再取り込みができないため、既に `profiles/` に入っている
分については索引生成時に同じルールで落としています。

```bash
python3 ui/build_portal_index.py
```

デプロイ時に自動再生成されます。`build_data.py` と同じく、`generated_at` には
全プロファイル中の最新 `updated_at` を使うため、入力が同じなら出力は変化しません。

`ui/data/actors.json` は UI が依存しているため、この対応では一切変更していません。

### IOCからクロスサーチへのピボット

IOC表の値はポータルの横断検索へのリンクになっています。表示は defang したまま、
検索には生の値を渡すため、ポータル側では型を判定した完全一致の結合キーで引かれます。

- ポータルのiframe内で開いている場合は、親フレームを `#/search/<値>` へ遷移させます
  （GitHub Pagesのプロジェクトページは同一オリジンのため親のhashを書き換えられます）
- 単体で開いている場合は別タブでポータルを開きます

遷移先は `assets/js/config.js` の `PORTAL_URL` と `PORTAL_SEARCH_ROUTE` で変更できます。

## ローカルでの確認

`fetch()` を使うため、`file://` ではなくHTTPサーバ経由で開いてください。

```bash
# リポジトリルートで実行
python3 -m http.server 8000
# → http://localhost:8000/ui/ を開く
```

## 注意

- 本UIは閲覧用の派生物です。正規データは各 `actor-profile.json` を参照してください。
- 正規データの値は互換性のため原表記を維持し、UIの分類名・状態・確度・戦術などを
  描画時に日本語化します。アクター名、別名、マルウェア名、ツール名、Technique名は
  固有名詞として原表記を維持します。
- TTPヒートマップは`activity_refs`を持つ活動別観測だけを数えます。日付不明の観測は
  all timeにだけ含め、`reported_at`および`basis`が資料公開日を示す日時を観測日として
  過去1年・3年へ混入させません。活動タイムラインとマルウェア利用履歴も同じ判定です。
- IOC・帰属・関係には候補情報や低信頼度の値が含まれます。確度と出典を
  確認のうえ利用してください。
