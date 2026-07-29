# TA415 脅威アクタープロファイル

- プロファイルID: `actor--ta415`
- 状態: draft
- 更新日時: 2026-07-29T15:36:12Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

TA415の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **TA415**
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
| etda-threat-group-cards | APT 41 | canonical-name | 高 | China | http://content.fireeye.com/apt41/rpt-apt41<br>https://arstechnica.com/information-technology/2018/05/researchers-link-a-decade-of-potent-hacks-to-chinese-intelligence-group/<br>https://www.kaspersky.com/about/press-releases/2019_operation-shadowhammer-new-supply-chain-attack |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | APT41 | canonical-name | 高 | CN, People's Republic of China | https://securelist.com/winnti-faq-more-than-just-a-game/57585/<br>https://securelist.com/winnti-more-than-just-a-game/37029/<br>http://williamshowalter.com/a-universal-windows-bootkit/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| APT17 | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 中国系TA415、VS Code Remote Tunnelsを悪用し米経済政策専門家をスパイ | phishing-campaign | 不明 | 不明 | 2025-09-18 | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--e7608f51421ca8b1e297 |  | ttp--activity-rule--82b731147199c28add83 | victim--activity-rule--73a796206a0da6325312 | 中国関与とされるTA415が、米政府・シンクタンク・大学の経済政策専門家を狙い、米中テーマで誘導して標的型攻撃を展開。 下院対中特別委員会委員長やU.S.-China Business Councilを装い、送信元にuschina@zohomail[.]comを用いたフィッシングを実施。 送付アーカイブのLNKがバッチを起動し、難読化Pythonローダー「WhirlCoil」を実行、PDFを囮に2時間毎の常駐タスクを設定。 ローダーはVS Code Remote Tunnelsで持続的アクセスを確立し、収集情報をrequestrepo[.]comへHTTP POST（Base64）で送信。 活動は2025年7～8月に観測。APT41／Brass Typhoonとの重複が指摘され、米中通商交渉下での諜報収集が目的と分析。 | 高 | `source--daily-5771658f42dfbb4596d9` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | 政府・行政 | 活動「中国系TA415、VS Code Remote Tunnelsを悪用し米経済政策専門家をスパイ」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-5771658f42dfbb4596d9` |
| sectors | 教育・研究 | 活動「中国系TA415、VS Code Remote Tunnelsを悪用し米経済政策専門家をスパイ」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-5771658f42dfbb4596d9` |

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 中国系TA415、VS Code Remote Tunnelsを悪用し米経済政策専門家をスパイ | 非公開 | anonymous | unknown | reported | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--e7608f51421ca8b1e297 |  | ttp--activity-rule--82b731147199c28add83 |  |  | 不明 | 不明 | 2025-09-18 | 高 | `source--daily-5771658f42dfbb4596d9` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1027 | Obfuscated Files or Information | 送付アーカイブのLNKがバッチを起動し、難読化Pythonローダー「WhirlCoil」を実行、PDFを囮に2時間毎の常駐タスクを設定。 |  | activity--daily-1a4f1dee2ecbdaa47b9d | 不明 | 不明 | 中 | `source--daily-5771658f42dfbb4596d9` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 1件（`artifacts.csv`）

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
| source--daily-5771658f42dfbb4596d9 | 中国系TA415、VS Code Remote Tunnelsを悪用し米経済政策専門家をスパイ | thehackernews.com | 2025-09-18 | https://thehackernews.com/2025/09/chinese-ta415-uses-vs-code-remote.html | osint-report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--ta415--26523ec4fbe0b554 | ta415 |  | 不明 | actor_profile/evidence/ta415.csv | structured-data | TLP:CLEAR | 中 |
| source--ta415--b1de570378ddc906 | Cloudflare 2026 threat report |  | 2026 | summary/2026/Cloudflare-2026-threat-report.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
