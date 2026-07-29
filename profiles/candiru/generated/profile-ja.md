# Candiru 脅威アクタープロファイル

- プロファイルID: `actor--candiru`
- 状態: draft
- 更新日時: 2026-07-25T14:07:08Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Candiruの標準化プロファイル。リポジトリ内の専用資料3件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Candiru**
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

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Caramel Tsunami | canonical-name | 高 |  | https://decoded.avast.io/threatresearch/avast-q2-2022-threat-report/<br>https://decoded.avast.io/janvojtesek/the-return-of-candiru-zero-days-in-the-middle-east/<br>https://citizenlab.ca/2022/04/catalangate-extensive-mercenary-spyware-operation-against-catalans-using-pegasus-candiru/ |
| misp-microsoft-activity-group | Caramel Tsunami | canonical-name | 高 | IL | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
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



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution | T1203 | Exploitation for Client Execution | velopment: Acquire Infrastructure: Server T1583.004 Initial Access : Spearphishing Link T1566.002 Execution: Exploitation for Client Execution T1203 26 CTA20250805 Recorded Future ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--candiru--80a5eb8801038e0a` |
| Initial Access | T1566.002 | Spearphishing Link | structure: Virtual Private Server T1583.003 Resource Development: Acquire Infrastructure: Server T1583.004 Initial Access : Spearphishing Link T1566.002 Execution: Exploitation for Client Execution T1203 26 CTA20250805 Recorded Future ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--candiru--80a5eb8801038e0a` |
| Resource Development | T1583.001 | Domains | THREAT ANALYSIS Appendix B — MITRE ATT&CK Techniques Tactic: Technique ATT&CK Code Resource Development: Acquire Infrastructure: Domains T1583.001 Resource Development: Acquire Infrastructure: Virtual Private Server T1583.003 Resource Development: Acquire Infrastructure: Server T1583.004 Initial Access : Spearphishing Link T1566.002 Execution: Exploitation for Client Execution T1203 |  |  | 不明 | 不明 | 中 | `source--candiru--80a5eb8801038e0a` |
| Resource Development | T1583.003 | Virtual Private Server | T&CK Code Resource Development: Acquire Infrastructure: Domains T1583.001 Resource Development: Acquire Infrastructure: Virtual Private Server T1583.003 Resource Development: Acquire Infrastructure: Server T1583.004 Initial Access : Spearphishing Link T1566.002 Execution: Exploitation for Client Execution T1203 26 CTA20250805 Record |  |  | 不明 | 不明 | 中 | `source--candiru--80a5eb8801038e0a` |
| Resource Development | T1583.004 | Server | T1583.001 Resource Development: Acquire Infrastructure: Virtual Private Server T1583.003 Resource Development: Acquire Infrastructure: Server T1583.004 Initial Access : Spearphishing Link T1566.002 Execution: Exploitation for Client Execution T1203 26 CTA20250805 Recorded Future ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--candiru--80a5eb8801038e0a` |

## IOC／artifact概要

- IOC値: 133件
- IOC観測: 153件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 2件（`artifacts.csv`）

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
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--candiru--230b73087475fed0 | Candiru product |  | 不明 | Candiru/Candiru_product.pdf | report | TLP:CLEAR | 中 |
| source--candiru--806053148fe55022 | README |  | 不明 | Candiru/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--candiru--80a5eb8801038e0a | Tracking Candiru’s DevilsTongue Spyware in Multiple Countries |  | 不明 | Candiru/Tracking Candiru’s DevilsTongue Spyware in Multiple Countries.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
