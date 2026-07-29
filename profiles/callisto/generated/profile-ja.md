# Callisto Group 脅威アクタープロファイル

- プロファイルID: `actor--callisto`
- 状態: draft
- 更新日時: 2026-07-29T15:20:22Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Callisto Groupの標準化プロファイル。リポジトリ内の専用資料4件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Callisto Group**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| COLDRIVER | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| SEABORGIUM | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Star Blizzard | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TA446 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

## 帰属

未評価

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: なし

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | State-sponsored intelligence collection or strategic operations. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Star Blizzard](https://attack.mitre.org/groups/G1033) is a cyber espionage and influence group originating in Russia that has been active since at least 2019. [Star Blizzard](https://attack.mitre.org/groups/G1033) campaigns align closely with Russian state interests and have included persistent phishing and credential theft against academic, defense, government, NGO, and think tank organizations in NATO countries, particularly the US and the UK.(Citation: Microsoft Star Blizzard August 2022)(Citation: CISA Star Blizzard Advisory December 2023)(Citation: StarBlizzard)(Citation: Google TAG COLDRIVER January 2024)<br> |
| Capability | Spica |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Callisto Group | canonical-name | 高 |  | https://www.f-secure.com/documents/996508/1030745/callisto-group<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Callisto+Group&n=1 |
| etda-threat-group-cards | Cold River | multiple-name-intersection | 高 | Russia | https://www.lastline.com/labsblog/threat-actor-cold-river-network-traffic-analysis-and-a-deep-dive-on-agent-drable/<br>https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-341a<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Cold+River&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Star Blizzard | canonical-name | 高 | Russia | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Callisto | multiple-name-intersection | 高 | RU | https://web.archive.org/web/20170417102235/https://www.f-secure.com/documents/996508/1030745/callisto-group<br>https://blog.google/threat-analysis-group/tracking-cyber-activity-eastern-europe<br>https://blog.google/threat-analysis-group/update-on-cyber-activity-in-eastern-europe |
| misp-threat-actor | Cold River | single-alias-intersection | 中 |  | https://www.lastline.com/labsblog/threat-actor-cold-river-network-traffic-analysis-and-a-deep-dive-on-agent-drable/ |
| misp-microsoft-activity-group | Star Blizzard | canonical-name | 高 | RU, Russia | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Star Blizzard - G1033 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1033<br>https://blog.google/threat-analysis-group/google-tag-coldriver-russian-phishing-malware/<br>https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-341a |
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
| malware--spica | Spica | [Spica](https://attack.mitre.org/software/S1140) is a custom backdoor written in Rust that has been used by [Star Blizzard](https://attack.mitre.org/groups/G1033) since at least 2023.(Citation: Google TAG COLDRIVER January 2024)  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| Google、ロシアのサイバースパイと関連する新たなデータ窃取マルウェア「LostKeys」を特定 | phishing-campaign | 不明 | 不明 | 2025-05-09 | target--activity-rule--sector--e7608f51421ca8b1e297 |  | ttp--activity-rule--42d1e63e49f3cca5b345, ttp--activity-rule--4eacc810da09c0b2b54d, ttp--activity-rule--714e895c938fc762d78b | victim--activity-rule--c80973708fca655b5050 | GoogleのThreat Intelligence Groupは、ロシアの国家支援型ハッカー集団ColdRiverが新たに使用するマルウェア「LostKeys」を特定。 LostKeysは、特定のファイル拡張子やディレクトリからファイルを窃取し、システム情報や実行中のプロセス情報を攻撃者に送信する機能を持つ。 このマルウェアは、ClickFixと呼ばれるソーシャルエンジニアリング攻撃の一環として、悪意のあるPowerShellスクリプトを通じて配布される。 スクリプトが実行されると、追加のPowerShellペイロードがダウンロード・実行され、最終的にVisual Basic Script (VBS) のデータ窃盗マルウェアであるLostKeysが実行。 ColdRiverは、NATO加盟国の政府、非政府組織、ジャーナリスト、シンクタンクなどを標的にしたスピアフィッシング攻撃で知られている。 | 中 | `source--daily-000ea03bc7f9b3f702ec` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | 教育・研究 | 活動「Google、ロシアのサイバースパイと関連する新たなデータ窃取マルウェア「LostKeys」を特定」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-000ea03bc7f9b3f702ec` |

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Google、ロシアのサイバースパイと関連する新たなデータ窃取マルウェア「LostKeys」を特定 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--e7608f51421ca8b1e297 |  | ttp--activity-rule--42d1e63e49f3cca5b345, ttp--activity-rule--4eacc810da09c0b2b54d, ttp--activity-rule--714e895c938fc762d78b |  | data-theft: Google、ロシアのサイバースパイと関連する新たなデータ窃取マルウェア「LostKeys」を特定 | 不明 | 不明 | 2025-05-09 | 中 | `source--daily-000ea03bc7f9b3f702ec` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1105 | Ingress Tool Transfer | スクリプトが実行されると、追加のPowerShellペイロードがダウンロード・実行され、最終的にVisual Basic Script (VBS) のデータ窃盗マルウェアであるLostKeysが実行。 |  | activity--daily-99b5ac281926f2b2c7f5 | 不明 | 不明 | 中 | `source--daily-000ea03bc7f9b3f702ec` |
| Execution | T1204.004 | Malicious Copy and Paste | このマルウェアは、ClickFixと呼ばれるソーシャルエンジニアリング攻撃の一環として、悪意のあるPowerShellスクリプトを通じて配布される。 |  | activity--daily-99b5ac281926f2b2c7f5 | 不明 | 不明 | 中 | `source--daily-000ea03bc7f9b3f702ec` |
| Execution | T1059.001 | PowerShell | このマルウェアは、ClickFixと呼ばれるソーシャルエンジニアリング攻撃の一環として、悪意のあるPowerShellスクリプトを通じて配布される。 |  | activity--daily-99b5ac281926f2b2c7f5 | 不明 | 不明 | 中 | `source--daily-000ea03bc7f9b3f702ec` |
| Execution | T1059.007 | JavaScript | [Star Blizzard](https://attack.mitre.org/groups/G1033) has used JavaScript to redirect victim traffic from an adversary controlled server to a server hosting the Evilginx phishing framework.(Citation: StarBlizzard)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [Star Blizzard](https://attack.mitre.org/groups/G1033) has used stolen credentials to sign into victim email accounts.(Citation: Microsoft Star Blizzard August 2022)(Citation: CISA Star Blizzard Advisory December 2023)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114.002 | Remote Email Collection | [Star Blizzard](https://attack.mitre.org/groups/G1033) has remotely accessed victims' email accounts to steal messages and attachments.(Citation: CISA Star Blizzard Advisory December 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114.003 | Email Forwarding Rule | [Star Blizzard](https://attack.mitre.org/groups/G1033) has abused email forwarding rules to monitor the activities of a victim, steal information, and maintain persistent access after compromised credentials are reset.(Citation: Microsoft Star Blizzard August 2022)(Citation: CISA Star Blizzard Advisory December 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [Star Blizzard](https://attack.mitre.org/groups/G1033) has lured targets into opening malicious .pdf files to deliver malware.(Citation: Google TAG COLDRIVER January 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1539 | Steal Web Session Cookie | [Star Blizzard](https://attack.mitre.org/groups/G1033) has used EvilGinx to steal the session cookies of victims directed to<br> phishing domains.(Citation: CISA Star Blizzard Advisory December 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1550.004 | Web Session Cookie | [Star Blizzard](https://attack.mitre.org/groups/G1033) has bypassed multi-factor authentication on victim email accounts by using session cookies stolen using EvilGinx.(Citation: CISA Star Blizzard Advisory December 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [Star Blizzard](https://attack.mitre.org/groups/G1033) has sent emails with malicious .pdf files to spread malware.(Citation: Google TAG COLDRIVER January 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583 | Acquire Infrastructure | [Star Blizzard](https://attack.mitre.org/groups/G1033) has used HubSpot and MailerLite marketing platform services to hide the true sender of phishing emails.(Citation: StarBlizzard)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [Star Blizzard](https://attack.mitre.org/groups/G1033) has registered domains using randomized words and with names resembling legitimate organizations.(Citation: CISA Star Blizzard Advisory December 2023)(Citation: StarBlizzard)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.001 | Social Media Accounts | [Star Blizzard](https://attack.mitre.org/groups/G1033) has established fraudulent profiles on professional networking sites to conduct reconnaissance.(Citation: Microsoft Star Blizzard August 2022)(Citation: CISA Star Blizzard Advisory December 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.002 | Email Accounts | [Star Blizzard](https://attack.mitre.org/groups/G1033) has registered impersonation email accounts to spoof experts in a particular field or individuals and organizations affiliated with the intended target.(Citation: Microsoft Star Blizzard August 2022)(Citation: CISA Star Blizzard Advisory December 2023)(Citation: Google TAG COLDRIVER January 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1586.002 | Email Accounts | [Star Blizzard](https://attack.mitre.org/groups/G1033) has used compromised email accounts to conduct spearphishing against<br> contacts of the original victim.(Citation: CISA Star Blizzard Advisory December 2023)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [Star Blizzard](https://attack.mitre.org/groups/G1033) has incorporated the open-source EvilGinx framework into their spearphishing activity.(Citation: CISA Star Blizzard Advisory December 2023)(Citation: StarBlizzard)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589 | Gather Victim Identity Information | [Star Blizzard](https://attack.mitre.org/groups/G1033) has identified ways to engage targets by researching potential victims' interests and social or professional contacts.(Citation: CISA Star Blizzard Advisory December 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1593 | Search Open Websites/Domains | <br>[Star Blizzard](https://attack.mitre.org/groups/G1033) has used open-source research to identify information about victims to use in targeting.(Citation: Microsoft Star Blizzard August 2022)(Citation: CISA Star Blizzard Advisory December 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1598 | Phishing for Information | CYBERTHREATANALYSIS AppendixB—MitreATT&CKTechniques Tactic:Technique ATT&CKCode Reconnaissance: Phishingfor Information T1598 ResourceDevelopment: StageCapabilities T1608 About Insikt Group ® RecordedFuture’sInsikt Group, thecompany’sthreat researchdivision, comprisesanalystsandsecurityresearcherswithdeepgovernment, lawenforcement, military, andintelligenceagencyexperience. Their missionistoproduceinte |  |  | 不明 | 不明 | 中 | `source--callisto--f45614e65d3b5aba` |
| Reconnaissance | T1598.002 | Spearphishing Attachment | [Star Blizzard](https://attack.mitre.org/groups/G1033) has sent emails to establish rapport with targets eventually sending messages with attachments containing links to credential-stealing sites.(Citation: Microsoft Star Blizzard August 2022)(Citation: CISA Star Blizzard Advisory December 2023)(Citation: StarBlizzard)(Citation: Google TAG COLDRIVER January 2024)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1598.003 | Spearphishing Link | [Star Blizzard](https://attack.mitre.org/groups/G1033) has sent emails to establish rapport with targets eventually sending messages with links to credential-stealing sites.(Citation: Microsoft Star Blizzard August 2022)(Citation: CISA Star Blizzard Advisory December 2023)(Citation: StarBlizzard)(Citation: Google TAG COLDRIVER January 2024)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608 | Stage Capabilities | THREATANALYSIS AppendixB—MitreATT&CKTechniques Tactic:Technique ATT&CKCode Reconnaissance: Phishingfor Information T1598 ResourceDevelopment: StageCapabilities T1608 About Insikt Group ® RecordedFuture’sInsikt Group, thecompany’sthreat researchdivision, comprisesanalystsandsecurityresearcherswithdeepgovernment, lawenforcement, military, andintelligenceagencyexperience. Their missionistoproduceintelligencethat reducesriskfor clients, enablest |  |  | 不明 | 不明 | 中 | `source--callisto--f45614e65d3b5aba` |
| Resource Development | T1608.001 | Upload Malware | [Star Blizzard](https://attack.mitre.org/groups/G1033) has uploaded malicious payloads to cloud storage sites.(Citation: Google TAG COLDRIVER January 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1684.001 | Impersonation | [Star Blizzard](https://attack.mitre.org/groups/G1033) has registered impersonation email accounts to spoof experts in a particular field or individuals and organizations affiliated with the intended target.(Citation: Microsoft Star Blizzard August 2022)(Citation: CISA Star Blizzard Advisory December 2023)(Citation: Google TAG COLDRIVER January 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 79件
- IOC観測: 98件
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
| source--callisto--2465541c9b4c01dd | Spearphishing cases in Eastern Europe 2022 2024 technical brief |  | 不明 | Calisto/Spearphishing-cases-in-Eastern-Europe-2022-2024-technical-brief.pdf | report | TLP:CLEAR | 中 |
| source--callisto--7766956c75cbb2fc | readme |  | 不明 | Calisto/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--callisto--9ec82e2a9bfd4c83 | Nisos Research Coldriver Group |  | 不明 | Calisto/Nisos-Research-Coldriver-Group.pdf | report | TLP:CLEAR | 中 |
| source--callisto--f45614e65d3b5aba | BlueCharlie Continues to Deploy New Infrastructure in 2023 |  | 2023 | Calisto/BlueCharlie_Continues_to_Deploy_New_Infrastructure_in_2023.pdf | report | TLP:CLEAR | 中 |
| source--daily-000ea03bc7f9b3f702ec | Google、ロシアのサイバースパイと関連する新たなデータ窃取マルウェア「LostKeys」を特定 | bleepingcomputer.com | 2025-05-09 | https://www.bleepingcomputer.com/news/security/google-links-new-lostkeys-data-theft-malware-to-russian-cyberspies/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
