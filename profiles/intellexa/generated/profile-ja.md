# Intellexa 脅威アクタープロファイル

- プロファイルID: `actor--intellexa`
- 状態: draft
- 更新日時: 2026-07-29T23:12:00Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Intellexaの標準化プロファイル。リポジトリ内の専用資料5件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Intellexa**
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

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| commercial | Commercial offensive-security or surveillance operations. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

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

- 判定: `no-match`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | 一致なし |  |  |  |  |
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

活動履歴なし

### 活動別ダイヤモンドモデル

活動別ダイヤモンドモデルなし



## ターゲット

ターゲット情報なし

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution | T1203 | Exploitation for Client Execution | velopment: Acquire Infrastructure: Server T1583.004 Initial Access : Spearphishing Link T1566.002 Execution: Exploitation for Client Execution T1203 27 CTA20251203 Recorded Future ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--intellexa--5ff4d83bd862cc12`, `source--intellexa--9480e5576b2c2ac2` |
| Initial Access | T1566.002 | Spearphishing Link | structure: Virtual Private Server T1583.003 Resource Development: Acquire Infrastructure: Server T1583.004 Initial Access : Spearphishing Link T1566.002 Execution: Exploitation for Client Execution T1203 27 CTA20251203 Recorded Future ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--intellexa--42a37dbf3c479318`, `source--intellexa--5ff4d83bd862cc12`, `source--intellexa--9480e5576b2c2ac2` |
| Resource Development | T1583.001 | Domains | 8 89[.]150[.]57[.]85 Appendix B MITRE ATT&CK Techniques Tactic: Technique ATT&CK Code Resource Development: Acquire Infrastructure: Domains T1583.001 Resource Development: Acquire Infrastructure: Virtual Private Server T1583.003 Resource Development: Acquire Infrastructure: Server T1583.004 Initial Access : Spearphishing Link T1566.002 Execution: Exploitation for Client Execution T1203 |  |  | 不明 | 不明 | 中 | `source--intellexa--42a37dbf3c479318`, `source--intellexa--5ff4d83bd862cc12`, `source--intellexa--9480e5576b2c2ac2` |
| Resource Development | T1583.003 | Virtual Private Server | T&CK Code Resource Development: Acquire Infrastructure: Domains T1583.001 Resource Development: Acquire Infrastructure: Virtual Private Server T1583.003 Resource Development: Acquire Infrastructure: Server T1583.004 Initial Access : Spearphishing Link T1566.002 Execution: Exploitation for Client Execution T1203 27 CTA20251203 Recor |  |  | 不明 | 不明 | 中 | `source--intellexa--42a37dbf3c479318`, `source--intellexa--5ff4d83bd862cc12`, `source--intellexa--9480e5576b2c2ac2` |
| Resource Development | T1583.004 | Server | T1583.001 Resource Development: Acquire Infrastructure: Virtual Private Server T1583.003 Resource Development: Acquire Infrastructure: Server T1583.004 Initial Access : Spearphishing Link T1566.002 Execution: Exploitation for Client Execution T1203 27 CTA20251203 Recorded Future ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--intellexa--42a37dbf3c479318`, `source--intellexa--5ff4d83bd862cc12`, `source--intellexa--9480e5576b2c2ac2` |

## IOC／artifact概要

- IOC値: 140件
- IOC観測: 196件
- 複数攻撃で観測: 0件
- 要レビュー候補: 26件
- 非IOC artifact観測: 19件（`artifacts.csv`）

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
| source--intellexa--b279ea1a756f7c4b | ACT1072452023ENGLISH |  | 不明 | Intellexa/Predator Files/ACT1072452023ENGLISH.pdf | report | TLP:CLEAR | 中 |
| source--intellexa--5ff4d83bd862cc12 | Intellexa’s Global Corporate Web |  | 不明 | Intellexa/Predator Files/Intellexa’s Global Corporate Web.pdf | report | TLP:CLEAR | 中 |
| source--intellexa--42a37dbf3c479318 | Predator Spyware Infrastructure Returns Following Exposure and Sanctions |  | 不明 | Intellexa/Predator Files/Predator Spyware Infrastructure Returns Following Exposure and Sanctions.pdf | report | TLP:CLEAR | 中 |
| source--intellexa--9480e5576b2c2ac2 | Predator Spyware Operators Rebuild Multi Tier Infrastructure to Target Mobile Devices |  | 不明 | Intellexa/Predator Files/Predator Spyware Operators Rebuild Multi-Tier Infrastructure to Target Mobile Devices.pdf | report | TLP:CLEAR | 中 |
| source--intellexa--fbeee8880ea7f05f | readme |  | 不明 | Intellexa/Predator Files/readme.md | repository-notes | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
