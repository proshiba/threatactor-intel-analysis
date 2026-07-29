# TA577 脅威アクタープロファイル

- プロファイルID: `actor--ta577`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

TA577の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **TA577**
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
| Adversary | [TA577](https://attack.mitre.org/groups/G1037) is an initial access broker (IAB) that has distributed [QakBot](https://attack.mitre.org/software/S0650) and [Pikabot](https://attack.mitre.org/software/S1145), and was among the first observed groups distributing [Latrodectus](https://attack.mitre.org/software/S1160) in 2023.(Citation: Latrodectus APR 2024) |
| Capability | Pikabot, Latrodectus, QakBot |
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
| misp-threat-actor | TA577 | canonical-name | 高 | RU | https://www.proofpoint.com/us/blog/threat-insight/first-step-initial-access-leads-ransomware<br>https://thehackernews.com/2021/06/ransomware-attackers-partnering-with.html<br>https://www.itpro.com/security/ransomware/359919/ransomware-criminals-look-to-other-hackers-to-provide-them-with-network |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | TA577 - G1037 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1037<br>https://www.proofpoint.com/us/blog/threat-insight/latrodectus-spider-bytes-ice |
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
| malware--pikabot | Pikabot | [Pikabot](https://attack.mitre.org/software/S1145) is a backdoor used for initial access and follow-on tool deployment active since early 2023. [Pikabot](https://attack.mitre.org/software/S1145) is notable for extensive use of multiple encoding, encryption, and defense evasion mechanisms to evade defenses and avoid analysis. [Pikabot](https://attack.mitre.org/software/S1145) has some overlaps with [QakBot](https://attack.mitre.org/software/S0650), but insufficient evidence exists to definitively link these two malware families. [Pikabot](https://attack.mitre.org/software/S1145) is frequently used to deploy follow on tools such as [Cobalt Strike](https://attack.mitre.org/software/S0154) or ransomware variants.(Citation: Zscaler Pikabot 2023)(Citation: Elastic Pikabot 2024)(Citation: Logpoint Pikabot 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--latrodectus | Latrodectus | [Latrodectus](https://attack.mitre.org/software/S1160) is a Windows malware downloader that has been used since at least 2023 to download and execute additional payloads and modules. [Latrodectus](https://attack.mitre.org/software/S1160) has most often been distributed through email campaigns, primarily by [TA577](https://attack.mitre.org/groups/G1037) and [TA578](https://attack.mitre.org/groups/G1038), and has infrastructure overlaps with historic [IcedID](https://attack.mitre.org/software/S0483) operations.(Citation: Latrodectus APR 2024)(Citation: Bleeping Computer Latrodectus April 2024)(Citation: Bitsight Latrodectus June 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--qakbot | QakBot | [QakBot](https://attack.mitre.org/software/S0650) is a modular banking trojan that has been used primarily by financially-motivated actors since at least 2007. [QakBot](https://attack.mitre.org/software/S0650) is continuously maintained and developed and has evolved from an information stealer into a delivery agent for ransomware, most notably [ProLock](https://attack.mitre.org/software/S0654) and [Egregor](https://attack.mitre.org/software/S0554).(Citation: Trend Micro Qakbot December 2020)(Citation: Red Canary Qbot)(Citation: Kaspersky QakBot September 2021)(Citation: ATT QakBot April 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1027.009 | Embedded Payloads | [TA577](https://attack.mitre.org/groups/G1037) has used LNK files to execute embedded DLLs.(Citation: Latrodectus APR 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [TA577](https://attack.mitre.org/groups/G1037) has used BAT files in malware execution chains.(Citation: Latrodectus APR 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.007 | JavaScript | [TA577](https://attack.mitre.org/groups/G1037) has used JavaScript to execute additional malicious payloads.(Citation: Latrodectus APR 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | [TA577](https://attack.mitre.org/groups/G1037) has lured users into executing malicious JavaScript files by sending malicious links via email.(Citation: Latrodectus APR 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | [TA577](https://attack.mitre.org/groups/G1037) has sent emails containing links to malicious JavaScript files.(Citation: Latrodectus APR 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1586.002 | Email Accounts | [TA577](https://attack.mitre.org/groups/G1037) has sent thread hijacked messages from compromised emails.(Citation: Latrodectus APR 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 11件（`artifacts.csv`）

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
| source--ta577--d76d72d795d38ce4 | ta577 |  | 不明 | actor_profile/evidence/ta577.csv | structured-data | TLP:CLEAR | 中 |
| source--ta577--b8a2e3c23ea0bbb2 | 2021 Adversary Infrastructure Report |  | 2021 | summary/2022/2021 Adversary Infrastructure Report.pdf | report | TLP:CLEAR | 中 |
| source--ta577--656ea5919e5f4236 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--ta577--8733381736e32cfa | 2023 Adversary Infrastructure Report |  | 2023 | summary/2024/2023 Adversary Infrastructure Report .pdf | report | TLP:CLEAR | 中 |
| source--ta577--053b1206e93cc38f | First 6 Half Year Threat Report 2024 |  | 2024 | summary/2024/First 6 Half-Year Threat Report 2024.pdf | report | TLP:CLEAR | 中 |
| source--ta577--224811c7dcab3b77 | 2025 dbir data breach investigations report |  | 2025 | summary/2025/2025-dbir-data-breach-investigations-report.pdf | report | TLP:CLEAR | 中 |
| source--ta577--ac421fcaefb00cb6 | annual threat report 2024 |  | 2024 | summary/2025/annual-threat-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--ta577--c6670ebd16337948 | CERTFR 2026 CTI 003 |  | 2026 | summary/2026/CERTFR-2026-CTI-003.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
