# UAC-0099 脅威アクタープロファイル

プロファイルID: `actor--uac-0099`  
状態: draft  
更新日時: 2026-07-26T05:28:45Z  
構造バージョン: 1.0.0

## エグゼクティブサマリー

UAC-0099の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UAC-0099**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

Aliasなし

## 帰属

未評価

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: なし

## モチベーション

未評価

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability |  |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | UAC-0099 | canonical-name | 高 |  | https://cert.gov.ua/article/6318634<br>https://cert.gov.ua/article/6281681<br>https://cert.gov.ua/article/4818341 |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | UAC-0099 | canonical-name | 高 |  | https://cert.gov.ua/article/4818341<br>https://www.deepinstinct.com/blog/threat-actor-uac-0099-continues-to-target-ukraine |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

候補なし

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--daily-0067ca7bc8c9a3dd3e9d | BURNYBEAR | tech-memo日次IOCでUAC-0099による使用が報告されたマルウェア。 | 2026-07-21 | 2026-07-21 | 中 | `source--daily-b6ba84745cdc81a329c5` |
| malware--daily-75ab18d562d78bfce191 | LUNCHPOKE | tech-memo日次IOCでUAC-0099による使用が報告されたマルウェア。 | 2026-07-21 | 2026-07-21 | 中 | `source--daily-b6ba84745cdc81a329c5` |
| malware--daily-8759c33e657f191deae0 | MATCHBOIL.V2 | tech-memo日次IOCでUAC-0099による使用が報告されたマルウェア。 | 2026-07-21 | 2026-07-21 | 中 | `source--daily-b6ba84745cdc81a329c5` |

### ツール

未確認

### インフラ

未確認

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| ハッカーがNotepad++プラグインを悪用し、密かにマルウェアをインストール | reported-activity | 2026-07-21 | 2026-07-21 | ウクライナのCERT-UAは、正規のNotepad++と悪性プラグイン「LunchPoke」を含むアーカイブを配布し、永続性を確保する攻撃を確認した。 UAC-0099はPDFを装うVBSスクリプトからEvernote.zipを取得させ、Notepad++の通常のプラグイン読込機能で悪性NppExport.dllを実行する。 LunchPokeはスケジュールタスクを作成し、BurnyBearとMatchBoil V2ローダーを展開して、追加プログラムの取得と実行を可能にする。 BurnyBearは起動に失敗した場合、ホストのRAMとCPUを枯渇させる攻撃を行う代替機能も備えている。 本攻撃はNotepad++のサプライチェーン侵害ではなく、正規アプリケーションと悪性ファイルを一緒に配布して信頼を悪用する手法である。 | 中 | `source--daily-b6ba84745cdc81a329c5` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 52件
- IOC観測: 53件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 10件（`artifacts.csv`）

## 主要判断と不確実性

主要判断なし

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--daily-b6ba84745cdc81a329c5 | ハッカーがNotepad++プラグインを悪用し、密かにマルウェアをインストール | cert.gov.ua | 2026-07-24 | https://cert.gov.ua/article/6318634 | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-cert-ua-uac-index | CERT-UA UAC Article Index | CERT-UA | 不明 | actor_profile/reference/osint/cert-ua-uac-index.json | government-cert-article-index | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--uac-0099--196d7c629d73d165 | RussianCyber |  | 不明 | summary/2024/RussianCyber.pdf | report | TLP:CLEAR | 中 |
| source--uac-0099--1bbf512130c53602 | Russian Cyber Operations Attack Automation, Espionage Against Defense Sector and New Tactics |  | 不明 | International Strategic/Russia/Russian Cyber Operations Attack Automation, Espionage Against Defense Sector and New Tactics.pdf | report | TLP:CLEAR | 中 |
| source--uac-0099--c98bdf401e349de9 | apt44 unearthing sandworm |  | 不明 | Sandworm/apt44-unearthing-sandworm.pdf | report | TLP:CLEAR | 中 |
| source--uac-0099--d1390da5cc0a8ca5 | uac 0099 |  | 不明 | actor_profile/evidence/uac-0099.csv | structured-data | TLP:CLEAR | 中 |
| source--uac-0099--da9ce7085469e683 | 2025 Global APT Threat Research Report |  | 2025 | summary/2026/2025 Global APT Threat Research Report.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
