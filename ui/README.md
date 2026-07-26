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
└── build_data.py       # 索引の生成スクリプト
```

- **一覧ページ**: 全アクターの統計、名前・alias・slug検索、帰属国 / 支援形態 /
  アクター種別 / 動機 / 標的産業のフィルタ、各種ソート。
- **詳細ページ** (`#/actor/<slug>[/タブ]`): `profiles/<slug>/actor-profile.json` を実行時に取得し、
  タブで表示します(空のタブは自動的に非表示、タブはURLで直接指定可能)。
  - **概要**: 説明、Alias、Key Judgments、帰属・動機、ダイヤモンドモデル(ひし形レイアウト)、標的
  - **関係**: 他アクターとの関係(発信・被参照の双方向、相互リンク・グラフへのリンク付き)
  - **Capabilities**: マルウェア、ツール、インフラ・サービス、脆弱性など
  - **TTP**: ATT&CK マトリックス表示(戦術別の列、ホバーで観測内容、クリックでMITREへ)
  - **Activities**: 活動履歴のタイムライン(過去1/3/5/10年の期間フィルタ、日付不明分は別掲)
  - **Technical Artifacts**: IOC(遅延読み込み+種別・値フィルタ、defang表示)と、
    非IOC artifact(コマンド、検体内文字列、パス、レジストリキー等の
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

## ローカルでの確認

`fetch()` を使うため、`file://` ではなくHTTPサーバ経由で開いてください。

```bash
# リポジトリルートで実行
python3 -m http.server 8000
# → http://localhost:8000/ui/ を開く
```

## 注意

- 本UIは閲覧用の派生物です。正規データは各 `actor-profile.json` を参照してください。
- IOC・帰属・関係には `candidate` や低信頼度の値が含まれます。`confidence` と出典を
  確認のうえ利用してください。
