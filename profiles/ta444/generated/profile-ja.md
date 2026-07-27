# TA444 脅威アクタープロファイル

- プロファイルID: `actor--ta444`
- 状態: draft
- 更新日時: 2026-07-27T11:04:36Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

TA444の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **TA444**
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
| etda-threat-group-cards | Bluenoroff, APT 38, Stardust Chollima | canonical-name | 高 | North Korea | https://threatpost.com/lazarus-apt-spinoff-linked-to-banking-hacks/124746/<br>https://www.microsoft.com/en-us/security/blog/2024/11/22/microsoft-shares-latest-intelligence-on-north-korean-and-chinese-threat-actors-at-cyberwarcon/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Subgroup%3A+Bluenoroff%2C+APT+38%2C+Stardust+Chollima&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | TA444 | canonical-name | 高 | KP | https://www.proofpoint.com/us/blog/threat-insight/ta444-apt-startup-aimed-at-your-funds<br>https://cyberscoop.com/north-korean-cryptocurrency-hackers-education-government/<br>https://www.darkreading.com/remote-workforce/north-korea-apt-swindled-1b-crypto-investors-2022 |
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

未確認

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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|
| 北朝鮮ハッカー集団がZoom通話で重役をディープフェイクし、Macマルウェアを拡散 | malware-campaign | 不明 | 不明 | 2025-06-19 | 北朝鮮のAPT集団BlueNoroffがZoom会議にディープフェイクを巧妙に埋め込んだ攻撃を実行 2025年6月11日にHuntressが調査した企業ネットワーク侵害で発見 Telegram経由の招待リンクは偽Zoomドメインへ誘導。被害者が参加すると企業の幹部や外部参加者のディープフェイク動画が流れる 会議中に被害者のマイクが機能しないという問題が発生したように見せかけ、問題を修正するためとして、Zoomの拡張機能と称するダウンロードを指示し、AppleScriptをダウンロードさせる マルウェアはRosetta 2のインストール有無を判定し、インストールされていなければインストールしてペイロードを/tmp/icloud_helperから実行 Telegram型持続インプラントやバックドアなど8種のMacマルウェアが確認 | 中 | `source--daily-a449b8d5424ffffad583` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 5件（`artifacts.csv`）

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
| source--daily-a449b8d5424ffffad583 | 北朝鮮ハッカー集団がZoom通話で重役をディープフェイクし、Macマルウェアを拡散 | bleepingcomputer.com | 2025-06-19 | https://www.bleepingcomputer.com/news/security/north-korean-hackers-deepfake-execs-in-zoom-call-to-spread-mac-malware/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--ta444--01f6dbb3cdcf5f99 | ta444 |  | 不明 | actor_profile/evidence/ta444.csv | structured-data | TLP:CLEAR | 中 |
| source--ta444--153a3a81efbff396 | Qianxin 2023 APT Report |  | 2023 | summary/2024/Qianxin 2023 APT Report.pdf | report | TLP:CLEAR | 中 |
| source--ta444--3626abb1436b84a4 | [Report] Bitsight State of the Underground 2026 |  | 2026 | summary/2026/[Report] Bitsight State of the Underground 2026.pdf | report | TLP:CLEAR | 中 |
| source--ta444--9d95eacf9707f985 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--ta444--b46c1dc9431c015c | North Korea’s Cyber Strategy |  | 不明 | International Strategic/Korea/North Korea’s Cyber Strategy.pdf | report | TLP:CLEAR | 中 |
| source--ta444--b4f4dd45ea4593ef | Global APT 2023 Mid Year Report QIANXIN |  | 2023 | summary/2023/Global APT 2023 Mid-Year Report-QIANXIN.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
