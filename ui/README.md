# Threat Actor Intelligence Profiles — GitHub Pages UI

`profiles/` 配下の脅威アクタープロファイルをブラウザで閲覧するための静的UIです。
ビルド不要のVanilla JS製SPA(ハッシュルーティング)で、コードはすべて `ui/` に収まっています。

## 構成

```text
ui/
├── index.html          # エントリポイント(一覧・詳細を1ページで切替)
├── assets/
│   ├── app.js          # SPA本体(検索・フィルタ・詳細描画・IOC遅延読込)
│   └── style.css       # ダークテーマのスタイル
├── data/
│   └── actors.json     # 検索・フィルタ用の軽量索引(build_data.pyで生成)
└── build_data.py       # 索引の生成スクリプト
```

- **一覧ページ**: 全アクターの統計、名前・alias・slug検索、帰属国 / 支援形態 /
  アクター種別 / 動機 / 標的産業のフィルタ、各種ソート。
- **詳細ページ** (`#/actor/<slug>`): `profiles/<slug>/actor-profile.json` を実行時に取得し、
  概要、Key Judgments、帰属、ダイヤモンドモデル(ひし形レイアウト)、
  他アクターとの関係(発信・被参照の双方向、相互リンク付き)、
  マルウェア/ツール、活動、標的、ATT&CK TTP(戦術別・MITREへのリンク付き)、出典を表示。
- **関係グラフ** (`#/relations`、ヘッダーからも遷移可): 全プロファイルの
  アクター間関係を力学レイアウトのグラフで表示。エッジ色は関係種別
  (overlaps-with / related-to / cooperates-with など)、ノード色は帰属国。
  ノードクリックで詳細ページへ、`#/relations/<slug>` で特定アクターに
  フォーカスした状態で開けます(詳細ページの関係セクションからリンクあり)。
- **IOC**: 件数が多いためボタン押下で `iocs.json` を遅延読み込みし、
  種別・値で絞り込み表示します。表示値はdefang済み(`hxxp` / `[.]`)です。

## GitHub Pages での公開

リポジトリの **Settings → Pages** で以下を設定してください。

- Source: `Deploy from a branch`
- Branch: 公開したいブランチ / フォルダ `/ (root)`

UIはリポジトリルートから相対パスで `profiles/` を読むため、フォルダは
`/ (root)` を指定する必要があります(`/docs` ではなく)。公開URLは
`https://<user>.github.io/<repo>/ui/` になります。

ルートに `.nojekyll` を置いてあるため、Jekyllビルドはスキップされます
(大量のMarkdown/JSONを含むリポジトリのため必須です)。

## 索引の再生成

プロファイルを追加・更新した後は索引を再生成してコミットしてください。

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
