# Shamoon 脅威アクタープロファイル

- プロファイルID: `actor--shamoon`
- 状態: draft
- 更新日時: 2026-07-25T14:07:08Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Shamoonの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Shamoon**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Volatile Kitten | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |

## 帰属

The repository mapping workbook places this actor in the Iran worksheet.

- 国: Iran
- スポンサー種別: state
- 確度: 中
- 証拠: `source--actor-mapping-workbook`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | State-sponsored intelligence collection or strategic operations. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability | Shamoon / Disttrack |
| Infrastructure |  |
| Victim | This threat actor targets energy sector, oil and gas industry as well as transportation and telecommunication services. |
| Socio-political | Iran |

## OSINTクロスチェック

- 判定: `possible-match`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Greenbug, Volatile Kitten | single-alias-intersection | 中 | Iran | https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Subgroup%3A+Greenbug%2C+Volatile+Kitten&n=1 |
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

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--shamoon-disttrack | Shamoon / Disttrack | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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
| sectors | Telecommunications | Targeting text indicates the Telecommunications sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Energy | Targeting text indicates the Energy sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Transportation | Targeting text indicates the Transportation sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Impact | T1485 | Data Destruction | Anonymous/RussiaUkrainewar/Report_Notes_of_Cyber_inspector_.pdf {"page": 67} Shamoon T1485 Data Destruction BlackJack применяли вредоносную программу Shamoon (известную как вайпер) для уничтожения данных в скомпрометированных системах. Этот инструмент перезаписывает данные на диске жертвы, включая загрузочные секторы, что приводит к невозможности восстановления систем |  |  | 不明 | 不明 | 中 | `source--shamoon--f6a320e89012bb39` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 59件（`artifacts.csv`）

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
| source--shamoon--f6a320e89012bb39 | shamoon |  | 不明 | actor_profile/evidence/shamoon.csv | structured-data | TLP:CLEAR | 中 |
| source--shamoon--2fa322ff7aed7371 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--shamoon--46ad3f29236655fa | evol agrius |  | 不明 | Agrius/evol-agrius.pdf | report | TLP:CLEAR | 中 |
| source--shamoon--178f16224615320c | Report Notes of Cyber inspector |  | 不明 | Anonymous/RussiaUkrainewar/Report_Notes_of_Cyber_inspector_.pdf | report | TLP:CLEAR | 中 |
| source--shamoon--c6ec59c289302bba | ClearSky Fox Kitten Campaign v1 |  | 不明 | International Strategic/Iran/ClearSky-Fox-Kitten-Campaign-v1.pdf | report | TLP:CLEAR | 中 |
| source--shamoon--0be4214b3447458e | README |  | 不明 | International Strategic/Iran/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--shamoon--218117ae3a94b6d1 | Raport analize Teknikat Taktikat Procedurat per sulmuesit Iraniane |  | 不明 | International Strategic/Iran/Raport-analize-Teknikat-Taktikat-Procedurat-per-sulmuesit-Iraniane.pdf | report | TLP:CLEAR | 中 |
| source--shamoon--2e9b5f8fe1772b70 | Saudi Arabia CNA report |  | 不明 | International Strategic/Iran/Saudi-Arabia-CNA-report.pdf | report | TLP:CLEAR | 中 |
| source--shamoon--4bb7281f572f2954 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--shamoon--6738ab2c4a225b00 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--shamoon--b7b293731720fe66 | Virtual Routes Pharos Report Series No. 3 |  | 不明 | cybercrime/2025/Virtual-Routes-Pharos-Report-Series-No.-3.pdf | report | TLP:CLEAR | 中 |
| source--shamoon--43ce21bb56cb0262 | PWC cyber threats 2019 retrospect |  | 2019 | summary/2020/PWC-cyber-threats-2019-retrospect.pdf | report | TLP:CLEAR | 中 |
| source--shamoon--031ecb7aa452f720 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--shamoon--04a18704d2015a86 | RedReport2023 Picus |  | 2023 | summary/2023/RedReport2023-Picus.pdf | report | TLP:CLEAR | 中 |
| source--shamoon--88edd4c7ca69a7a2 | Raport analize PROFILI I GRUPEVE TE HAKERAVE IRANIANE |  | 不明 | summary/2024/Raport-analize-PROFILI-I-GRUPEVE-TE-HAKERAVE-IRANIANE.pdf | report | TLP:CLEAR | 中 |
| source--shamoon--985fc49e9c2ecf58 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--shamoon--19879982443b5b5b | tool of first resort israel hamas war cyber |  | 不明 | summary/2024/tool-of-first-resort-israel-hamas-war-cyber.pdf | report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
