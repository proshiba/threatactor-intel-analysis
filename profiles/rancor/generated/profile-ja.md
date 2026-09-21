# Rancor 脅威アクタープロファイル

- プロファイルID: `actor--rancor`
- 状態: draft
- 更新日時: 2026-09-21T13:20:00Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

Rancorの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Rancor**
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

## 関連する企業・個人

関連エンティティなし

### エンティティ関係

確認された関係なし

### 法的措置

確認された法的措置なし

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
| etda-threat-group-cards | Rancor | canonical-name | 高 | China | https://unit42.paloaltonetworks.com/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/<br>https://research.checkpoint.com/2019/rancor-the-year-of-the-phish/<br>https://unit42.paloaltonetworks.com/rancor-cyber-espionage-group-uses-new-custom-malware-to-attack-southeast-asia/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | RANCOR | canonical-name | 高 | CN, China | https://unit42.paloaltonetworks.com/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/<br>https://www.cfr.org/interactive/cyber-operations/rancor<br>https://attack.mitre.org/groups/G0075/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | Rancor - G0075 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0075<br>https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/ |
| misp-mitre-intrusion-set | Rancor - G0075 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0075<br>https://researchcenter.paloaltonetworks.com/2018/06/unit42-rancor-targeted-attacks-south-east-asia-using-plaintee-ddkong-malware-families/ |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | Rancor | canonical-name | 高 |  |  |

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
| malware--ddkong | DDKONG | [DDKONG](https://attack.mitre.org/software/S0255) is a malware sample that was part of a campaign by [Rancor](https://attack.mitre.org/groups/G0075). [DDKONG](https://attack.mitre.org/software/S0255) was first seen used in February 2017. (Citation: Rancor Unit42 June 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--plaintee | PLAINTEE | [PLAINTEE](https://attack.mitre.org/software/S0254) is a malware sample that has been used by [Rancor](https://attack.mitre.org/groups/G0075) in targeted attacks in Singapore and Cambodia. (Citation: Rancor Unit42 June 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--certutil | certutil | [certutil](https://attack.mitre.org/software/S0160) is a command-line utility that can be used to obtain certificate authority information and configure Certificate Services. (Citation: TechNet Certutil) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| tool--reg | Reg | [Reg](https://attack.mitre.org/software/S0075) is a Windows utility used to interact with the Windows Registry. It can be used at the command-line interface to query, add, modify, and remove information. (Citation: Microsoft Reg)<br><br>Utilities such as [Reg](https://attack.mitre.org/software/S0075) are known to be used by persistent threats. (Citation: Windows Commands JPCERT) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

### インフラ

未確認

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

## C2・マルウェア ハンティング・ピボット

構造化されたハンティング・ピボットなし

### 観測根拠

観測記録なし

### ハントクエリ

クエリなし

### 継続利用チェック

実行済みの受動検索・継続利用チェックなし

`active_status` は明示的なテレメトリまたはスキャン根拠がない限り `unknown` です。出典公開日は観測時刻に転用していません。

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
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [Rancor](https://attack.mitre.org/groups/G0075) launched a scheduled task to gain persistence using the <code>schtasks /create /sc</code> command.(Citation: Rancor Unit42 June 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.003 | Windows Command Shell | [Rancor](https://attack.mitre.org/groups/G0075) has used cmd.exe to execute commmands.(Citation: Rancor Unit42 June 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.005 | Visual Basic | [Rancor](https://attack.mitre.org/groups/G0075) has used VBS scripts as well as embedded macros for execution.(Citation: Rancor Unit42 June 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1071.001 | Web Protocols | [Rancor](https://attack.mitre.org/groups/G0075) has used HTTP for C2.(Citation: Rancor Unit42 June 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1105 | Ingress Tool Transfer | [Rancor](https://attack.mitre.org/groups/G0075) has downloaded additional malware, including by using [certutil](https://attack.mitre.org/software/S0160).(Citation: Rancor Unit42 June 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1204.002 | Malicious File | [Rancor](https://attack.mitre.org/groups/G0075) attempted to get users to click on an embedded macro within a Microsoft Office Excel document to launch their malware.(Citation: Rancor Unit42 June 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1218.007 | Msiexec | [Rancor](https://attack.mitre.org/groups/G0075) has used <code>msiexec</code> to download and execute malicious installer files over HTTP.(Citation: Rancor Unit42 June 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Persistence, Privilege Escalation | T1546.003 | Windows Management Instrumentation Event Subscription | [Rancor](https://attack.mitre.org/groups/G0075) has complied VBScript-generated MOF files into WMI event subscriptions for persistence.(Citation: Rancor WMI) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1566.001 | Spearphishing Attachment | [Rancor](https://attack.mitre.org/groups/G0075) has attached a malicious document to an email to gain initial access.(Citation: Rancor Unit42 June 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 3件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
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
| source--rancor--8095b52ae8a88b34 | rancor |  | 不明 | actor_profile/evidence/rancor.csv | structured-data | TLP:CLEAR | 中 |
| source--rancor--6ebb348d0e02a3ea | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--rancor--395aeeaeeb696844 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--rancor--8770154620450dc7 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-enterprise-19.1.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
