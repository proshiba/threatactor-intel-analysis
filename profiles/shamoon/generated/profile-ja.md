# Shamoon 脅威アクタープロファイル

- プロファイルID: `actor--shamoon`
- 状態: deprecated
- 更新日時: 2026-09-21T02:11:27Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Shamoonはwiper malwareとして扱い、旧actor profileはdeprecatedとする。Actor側はGreenbug / Volatile Kittenを別entityとして追跡する。

## アクター名とAlias

- 正規名: **Shamoon**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

Aliasなし

## 帰属

Deprecated entity conflation.

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

- 判定: `possible-match`
- 調査日時: 2026-09-19T00:54:53Z
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

選定ロジック: Deprecated legacy actor profile. 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 8件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| Shamoon is wiper malware; the legacy Shamoon actor profile is deprecated and actor tracking is separated into Greenbug / Volatile Kitten where supported. | 高 | `source--mitre-shamoon-s0140`, `source--crowdstrike-volatile-kitten` | Entity-type correction. |

### 情報ギャップ


### 不確実性

- Some historical reporting uses Shamoon as a metonym for the operators.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
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
| source--mitre-shamoon-s0140 | Shamoon, Software S0140 | MITRE ATT&CK | 不明 | https://attack.mitre.org/software/S0140/ | structured-knowledge-base | TLP:CLEAR | 高 |
| source--crowdstrike-volatile-kitten | Volatile Kitten Adversary Profile | CrowdStrike | 不明 | https://www.crowdstrike.com/en-us/adversaries/volatile-kitten/ | vendor-adversary-profile | TLP:CLEAR | 高 |

## 自由記述

actor--shamoonは既存参照互換性のため保持する。
