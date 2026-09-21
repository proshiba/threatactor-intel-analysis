# TA578 脅威アクタープロファイル

- プロファイルID: `actor--ta578`
- 状態: draft
- 更新日時: 2026-09-21T04:18:00Z
- 構造バージョン: 1.3.0

## エグゼクティブサマリー

TA578の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **TA578**
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
- 調査日時: 2026-09-21T02:39:13Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | TA578 | canonical-name | 高 |  | https://www.proofpoint.com/us/blog/threat-insight/bumblebee-is-still-transforming |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | TA578 - G1038 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1038<br>https://www.bitsight.com/blog/latrodectus-are-you-coming-back<br>https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice |
| misp-mitre-intrusion-set | TA578 - G1038 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1038<br>https://www.bitsight.com/blog/latrodectus-are-you-coming-back<br>https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | TA578 | canonical-name | 高 |  |  |

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
| malware--bumblebee | Bumblebee | [Bumblebee](https://attack.mitre.org/software/S1039) is a custom loader written in C++ that has been used by multiple threat actors, including possible initial access brokers, to download and execute additional payloads since at least March 2022. [Bumblebee](https://attack.mitre.org/software/S1039) has been linked to ransomware operations including [Conti](https://attack.mitre.org/software/S0575), Quantum, and Mountlocker and derived its name from the appearance of "bumblebee" in the user-agent.(Citation: Google EXOTIC LILY March 2022)(Citation: Proofpoint Bumblebee April 2022)(Citation: Symantec Bumblebee June 2022)<br> | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--icedid | IcedID | [IcedID](https://attack.mitre.org/software/S0483) is a modular banking malware designed to steal financial information that has been observed in the wild since at least 2017.  [IcedID](https://attack.mitre.org/software/S0483)  has been downloaded by [Emotet](https://attack.mitre.org/software/S0367) in multiple campaigns.(Citation: IBM IcedID November 2017)(Citation: Juniper IcedID June 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--latrodectus | Latrodectus | [Latrodectus](https://attack.mitre.org/software/S1160) is a Windows malware downloader that has been used since at least 2023 to download and execute additional payloads and modules. [Latrodectus](https://attack.mitre.org/software/S1160) has most often been distributed through email campaigns, primarily by [TA577](https://attack.mitre.org/groups/G1037) and [TA578](https://attack.mitre.org/groups/G1038), and has infrastructure overlaps with historic [IcedID](https://attack.mitre.org/software/S0483) operations.(Citation: Latrodectus APR 2024)(Citation: Bleeping Computer Latrodectus April 2024)(Citation: Bitsight Latrodectus June 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution | T1059.007 | JavaScript | [TA578](https://attack.mitre.org/groups/G1038) has used JavaScript files in malware execution chains.(Citation: Latrodectus APR 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1204.001 | Malicious Link | [TA578](https://attack.mitre.org/groups/G1038) has placed malicious links in contact forms on victim sites, often spoofing a copyright complaint, to redirect users to malicious file downloads.(Citation: Latrodectus APR 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1583.006 | Web Services | [TA578](https://attack.mitre.org/groups/G1038) has used Google Firebase to host malicious scripts.(Citation: Latrodectus APR 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Reconnaissance | T1594 | Search Victim-Owned Websites | [TA578](https://attack.mitre.org/groups/G1038) has filled out contact forms on victims' websites to direct them to adversary-controlled URLs.(Citation: Latrodectus APR 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

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
| source--ta578--3b6e0cf5d9740894 | ta578 |  | 不明 | actor_profile/evidence/ta578.csv | structured-data | TLP:CLEAR | 中 |
| source--ta578--e4407c968b337540 | 20240405 |  | 2024-04-05 | parse-daily/.cache/tech-memo/daily-news/news/2024_04-06/20240405.md | repository-notes | TLP:CLEAR | 中 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-enterprise-19.1.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
