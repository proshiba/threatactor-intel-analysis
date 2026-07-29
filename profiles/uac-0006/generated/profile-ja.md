# UAC-0006 脅威アクタープロファイル

- プロファイルID: `actor--uac-0006`
- 状態: draft
- 更新日時: 2026-07-29T15:36:12Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

UAC-0006の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UAC-0006**
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
| cert-ua-uac-index | UAC-0006 | canonical-name | 高 |  | https://cert.gov.ua/article/5269451<br>https://cert.gov.ua/article/6276584 |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | UAC-0006 | canonical-name | 高 |  | https://socprime.com/blog/smokeloader-detection-uac-0006-group-launches-a-new-phishing-campaign-against-ukraine/<br>https://socprime.com/blog/smokeloader-malware-detection-uac-0006-hackers-launch-a-wave-of-phishing-attacks-against-ukraine-targeting-accountants/<br>https://socprime.com/blog/detecting-smokeloader-campaign-uac-0006-keep-targeting-ukrainian-financial-institutions-in-a-series-of-phishing-attacks/ |
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



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Exfiltration | T1020 | Automated Exfiltration | page": 18} UAC-0006 pplication Layer Protocol: Web Protocols - [T1090.003] Proxy: Multi-hop Proxy - [T1090.004] Proxy: Domain Fronting Exfiltration [TA0010] - [T1020] Automated Exfiltration - [T1048] Exfiltration Over Alternative Protocol UAC-0006. PLAY, PAUSE, REPLAY A t the beginning of the first half of 2024, the mass phishing campaigns, which started in May 2023 and were carried out by the finan- cially motivated group UAC-0006, continue |  |  | 不明 | 不明 | 中 | `source--uac-0006--9c7b7a162d71d85d` |
| Exfiltration | T1048 | Exfiltration Over Alternative Protocol | yer Protocol: Web Protocols - [T1090.003] Proxy: Multi-hop Proxy - [T1090.004] Proxy: Domain Fronting Exfiltration [TA0010] - [T1020] Automated Exfiltration - [T1048] Exfiltration Over Alternative Protocol UAC-0006. PLAY, PAUSE, REPLAY A t the beginning of the first half of 2024, the mass phishing campaigns, which started in May 2023 and were carried out by the finan- cially motivated group UAC-0006, continued cam- paigns were p |  |  | 不明 | 不明 | 中 | `source--uac-0006--9c7b7a162d71d85d` |
| Command And Control | T1090.003 | Multi-hop Proxy | International Strategic/Russia/Cyber operations by russia new goals, tools and groups.pdf {"page": 18} UAC-0006 pplication Layer Protocol: Web Protocols - [T1090.003] Proxy: Multi-hop Proxy - [T1090.004] Proxy: Domain Fronting Exfiltration [TA0010] - [T1020] Automated Exfiltration - [T1048] Exfiltration Over Alternative Protocol UAC-0006. PLAY, PAUSE, REPLAY A t the beginning of the first half of 2024, the mass phishing campaigns, which star |  |  | 不明 | 不明 | 中 | `source--uac-0006--9c7b7a162d71d85d` |
| Command And Control | T1090.004 | Domain Fronting | ber operations by russia new goals, tools and groups.pdf {"page": 18} UAC-0006 pplication Layer Protocol: Web Protocols - [T1090.003] Proxy: Multi-hop Proxy - [T1090.004] Proxy: Domain Fronting Exfiltration [TA0010] - [T1020] Automated Exfiltration - [T1048] Exfiltration Over Alternative Protocol UAC-0006. PLAY, PAUSE, REPLAY A t the beginning of the first half of 2024, the mass phishing campaigns, which started in May 2023 and were carried out |  |  | 不明 | 不明 | 中 | `source--uac-0006--9c7b7a162d71d85d` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 14件（`artifacts.csv`）

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
| source--uac-0006--9c7b7a162d71d85d | uac 0006 |  | 不明 | actor_profile/evidence/uac-0006.csv | structured-data | TLP:CLEAR | 中 |
| source--uac-0006--c67466806769e49b | Cyber operations by russia new goals, tools and groups |  | 不明 | International Strategic/Russia/Cyber operations by russia new goals, tools and groups.pdf | report | TLP:CLEAR | 中 |
| source--uac-0006--37a227a87893de6a | UAC0006 FC.pdf |  | 不明 | cybercrime/SmokeLoader/UAC0006_FC.pdf.pdf | report | TLP:CLEAR | 中 |
| source--uac-0006--0d4a160c3f1c9f2e | RussianCyber |  | 不明 | summary/2024/RussianCyber.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-cert-ua-uac-index | CERT-UA UAC Article Index | CERT-UA | 不明 | actor_profile/reference/osint/cert-ua-uac-index.json | government-cert-article-index | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
