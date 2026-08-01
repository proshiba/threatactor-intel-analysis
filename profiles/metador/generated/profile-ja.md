# Metador 脅威アクタープロファイル

- プロファイルID: `actor--metador`
- 状態: draft
- 更新日時: 2026-07-29T23:12:00Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Metadorの標準化プロファイル。リポジトリ内の専用資料2件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Metador**
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
| Adversary | [Metador](https://attack.mitre.org/groups/G1013) is a suspected cyber espionage group that was first reported in September 2022. [Metador](https://attack.mitre.org/groups/G1013) has targeted a limited number of telecommunication companies, internet service providers, and universities in the Middle East and Africa. Security researchers named the group [Metador](https://attack.mitre.org/groups/G1013) based on the "I am meta" string in one of the group's malware samples and the expectation of Spanish-language responses from C2 servers.(Citation: SentinelLabs Metador Sept 2022) |
| Capability | Mafalda, metaMain |
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
| misp-threat-actor | Metador | canonical-name | 高 |  | https://www.sentinelone.com/labs/the-mystery-of-metador-unpicking-mafaldas-anti-analysis-techniques/<br>https://www.sentinelone.com/labs/the-mystery-of-metador-an-unattributed-threat-hiding-in-telcos-isps-and-universities/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Metador - G1013 | mitre-external-id | 高 |  | https://assets.sentinelone.com/sentinellabs22/metador#page=1<br>https://attack.mitre.org/groups/G1013 |
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
| malware--mafalda | Mafalda | [Mafalda](https://attack.mitre.org/software/S1060) is a flexible interactive implant that has been used by [Metador](https://attack.mitre.org/groups/G1013). Security researchers assess the [Mafalda](https://attack.mitre.org/software/S1060) name may be inspired by an Argentinian cartoon character that has been popular as a means of political commentary since the 1960s. (Citation: SentinelLabs Metador Sept 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--metamain | metaMain | [metaMain](https://attack.mitre.org/software/S1059) is a backdoor used by [Metador](https://attack.mitre.org/groups/G1013) to maintain long-term access to compromised machines; it has also been used to decrypt [Mafalda](https://attack.mitre.org/software/S1060) into memory.(Citation: SentinelLabs Metador Sept 2022)(Citation: SentinelLabs Metador Technical Appendix Sept 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| regions | アフリカ | MITRE ATT&CKのGroup概要でMetadorの標的範囲としてアフリカが明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| regions | 中東 | MITRE ATT&CKのGroup概要でMetadorの標的範囲として中東が明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 情報通信 | [Metador](https://attack.mitre.org/groups/G1013) has targeted a limited number of telecommunication companies, internet service providers, and universities in the Middle East and Africa. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1027.013 | Encrypted/Encoded File | [Metador](https://attack.mitre.org/groups/G1013) has encrypted their payloads.(Citation: SentinelLabs Metador Sept 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [Metador](https://attack.mitre.org/groups/G1013) has used the Windows command line to execute commands.(Citation: SentinelLabs Metador Sept 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | [Metador](https://attack.mitre.org/groups/G1013) has quickly deleted `cbd.exe` from a compromised host following the successful deployment of their malware.(Citation: SentinelLabs Metador Sept 2022)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [Metador](https://attack.mitre.org/groups/G1013) has used HTTP for C2.(Citation: SentinelLabs Metador Sept 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1095 | Non-Application Layer Protocol | [Metador](https://attack.mitre.org/groups/G1013) has used TCP for C2.(Citation: SentinelLabs Metador Sept 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [Metador](https://attack.mitre.org/groups/G1013) has downloaded tools and malware onto a compromised system.(Citation: SentinelLabs Metador Sept 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1546.003 | Windows Management Instrumentation Event Subscription | [Metador](https://attack.mitre.org/groups/G1013) has established persistence through the use of a WMI event subscription combined with unusual living-off-the-land binaries such as `cdb.exe`.(Citation: SentinelLabs Metador Sept 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.001 | Malware | [Metador](https://attack.mitre.org/groups/G1013) has used unique malware in their operations, including [metaMain](https://attack.mitre.org/software/S1059) and [Mafalda](https://attack.mitre.org/software/S1060).(Citation: SentinelLabs Metador Sept 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [Metador](https://attack.mitre.org/groups/G1013) has used Microsoft's Console Debugger in some of their operations.(Citation: SentinelLabs Metador Sept 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 6件
- IOC観測: 9件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 17件（`artifacts.csv`）

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
| source--metador--a657cf4aadaff4fe | README |  | 不明 | Metador/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--metador--e31981b38a4d57b8 | metador An Unattributed Threat Hiding in Telcos SPs and Universities |  | 不明 | Metador/metador_An_Unattributed_Threat_Hiding_in_Telcos_SPs_and_Universities.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
