# ZooPark 脅威アクタープロファイル

- プロファイルID: `actor--zoopark`
- 状態: draft
- 更新日時: 2026-07-29T15:36:13Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

ZooParkの標準化プロファイル。リポジトリ内の専用資料2件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **ZooPark**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| APT-C-38 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Middle East row 19; mapping requires review. |
| Saber Lion | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Middle East row 19; mapping requires review. |

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
| Victim | Egypt, Jordan, Morocco, Lebanon, Iran, Iraqi Kurdistan |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | ZooPark | canonical-name | 高 |  | https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/05/24122414/ZooPark_for_public_final_edited.pdf<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=ZooPark&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | ZooPark | canonical-name | 高 |  | https://securelist.com/whos-who-in-the-zoo/85394/ |
| misp-threat-actor | COBALT JUNO | single-alias-intersection | 中 |  | https://www.secureworks.com/research/threat-profiles/cobalt-juno |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 军刀狮 - APT-C-38 | single-alias-intersection | 中 |  | https://apt.360.net/report/apts/30.html |

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

活動履歴なし



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | Egypt | Targeting text mentions egypt. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Iran | Targeting text mentions iran. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Jordan | Targeting text mentions jordan. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Lebanon | Targeting text mentions lebanon. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 64件
- IOC観測: 85件
- 複数攻撃で観測: 0件
- 要レビュー候補: 29件
- 非IOC artifact観測: 30件（`artifacts.csv`）

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
| source--zoopark--07f2019e233e54e9 | README |  | 不明 | ZooPark/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--zoopark--295a661ca75d1f1a | ZooPark for public final edited |  | 不明 | ZooPark/ZooPark_for_public_final_edited.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-360net | MISP Galaxy 360.net Threat Actors | MISP Project / 360 Netlab | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
