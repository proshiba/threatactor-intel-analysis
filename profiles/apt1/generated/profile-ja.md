# APT1 脅威アクタープロファイル

- プロファイルID: `actor--apt1`
- 状態: draft
- 更新日時: 2026-07-25T14:07:08Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

APT1の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **APT1**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| BrownFox | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Byzantine Candor | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Comment Crew | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Comment Group | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Comment Panda | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| GIF89a | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Group 3 | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| PLA Unit 61398 | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| ShadyRAT | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Shanghai Group | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TG-8223 | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| GIF89a, ShadyRAT, Shanghai Group, Byzantine Candor | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 3; mapping requires review. |

## 帰属

The repository mapping workbook places this actor in the China worksheet.

- 国: China
- スポンサー種別: state
- 確度: 中
- 証拠: `source--actor-mapping-workbook`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | State-sponsored intelligence collection or strategic operations. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Calypso | overlaps-with | 共有alias: Comment Crew | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [APT1](https://attack.mitre.org/groups/G0006) is a Chinese threat group that has been attributed to the 2nd Bureau of the People’s Liberation Army (PLA) General Staff Department’s (GSD) 3rd Department, commonly known by its Military Unit Cover Designator (MUCD) as Unit 61398. (Citation: Mandiant APT1) |
| Capability | WEBC2, CALENDAR, PoisonIvy, Seasalt, BISCUIT, GLOOXMAIL, BISCUIT and many others, Net, ipconfig, Tasklist, Lslsass, xCmd, pwdump, Pass-The-Hash Toolkit, Mimikatz, gsecdump, Cachedump, PsExec |
| Infrastructure |  |
| Victim | U.S. cybersecurity firm Mandiant, later purchased by FireEye, released a report in February 2013 that exposed one of China's cyber espionage units, Unit 61398. The group, which FireEye called APT1, is a unit within China's People's Liberation Army (PLA) that has been linked to a wide range of cyber operations targeting U.S. private sector entities for espionage purposes. The comprehensive report detailed evidence connecting APT1 and the PLA, offered insight into APT1's operational malware and methodologies, and provided timelines of the espionage it conducted. |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Comment Crew, APT 1 | canonical-name | 高 | China | https://www.symantec.com/connect/blogs/apt1-qa-attacks-comment-crew<br>https://en.wikipedia.org/wiki/PLA_Unit_61398<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Comment+Crew%2C+APT+1&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | APT1 | canonical-name | 高 | CN, China | https://en.wikipedia.org/wiki/PLA_Unit_61398<br>http://intelreport.mandiant.com/Mandiant_APT1_Report.pdf<br>https://www.cfr.org/interactive/cyber-operations/pla-unit-61398 |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | APT1 - G0006 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0006<br>https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf |
| misp-mitre-intrusion-set | APT1 - G0006 | mitre-external-id | 高 |  | http://cdn0.vox-cdn.com/assets/4589853/crowdstrike-intelligence-report-putter-panda.original.pdf<br>https://attack.mitre.org/groups/G0006<br>https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf |
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
| malware--webc2 | WEBC2 | [WEBC2](https://attack.mitre.org/software/S0109) is a family of backdoor malware used by [APT1](https://attack.mitre.org/groups/G0006) as early as July 2006. [WEBC2](https://attack.mitre.org/software/S0109) backdoors are designed to retrieve a webpage, with commands hidden in HTML comments or special tags, from a predetermined C2 server. (Citation: Mandiant APT1 Appendix)(Citation: Mandiant APT1) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--calendar | CALENDAR | [CALENDAR](https://attack.mitre.org/software/S0025) is malware used by [APT1](https://attack.mitre.org/groups/G0006) that mimics legitimate Gmail Calendar traffic. (Citation: Mandiant APT1) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--poisonivy | PoisonIvy | [PoisonIvy](https://attack.mitre.org/software/S0012) is a popular remote access tool (RAT) that has been used by many groups.(Citation: FireEye Poison Ivy)(Citation: Symantec Elderwood Sept 2012)(Citation: Symantec Darkmoon Aug 2005) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--seasalt | Seasalt | [Seasalt](https://attack.mitre.org/software/S0345) is malware that has been linked to [APT1](https://attack.mitre.org/groups/G0006)'s 2010 operations. It shares some code similarities with [OceanSalt](https://attack.mitre.org/software/S0346).(Citation: Mandiant APT1 Appendix)(Citation: McAfee Oceansalt Oct 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--biscuit | BISCUIT | [BISCUIT](https://attack.mitre.org/software/S0017) is a backdoor that has been used by [APT1](https://attack.mitre.org/groups/G0006) since as early as 2007. (Citation: Mandiant APT1) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--glooxmail | GLOOXMAIL | [GLOOXMAIL](https://attack.mitre.org/software/S0026) is malware used by [APT1](https://attack.mitre.org/groups/G0006) that mimics legitimate Jabber/XMPP traffic. (Citation: Mandiant APT1) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--biscuit-and-many-others | BISCUIT and many others | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ipconfig | ipconfig | [ipconfig](https://attack.mitre.org/software/S0100) is a Windows utility that can be used to find information about a system's TCP/IP, DNS, DHCP, and adapter configuration. (Citation: TechNet Ipconfig) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--tasklist | Tasklist | The [Tasklist](https://attack.mitre.org/software/S0057) utility displays a list of applications and services with their Process IDs (PID) for all tasks running on either a local or a remote computer. It is packaged with Windows operating systems and can be executed from the command-line interface. (Citation: Microsoft Tasklist) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--lslsass | Lslsass | [Lslsass](https://attack.mitre.org/software/S0121) is a publicly-available tool that can dump active logon session password hashes from the lsass process. (Citation: Mandiant APT1) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--xcmd | xCmd | [xCmd](https://attack.mitre.org/software/S0123) is an open source tool that is similar to [PsExec](https://attack.mitre.org/software/S0029) and allows the user to execute applications on remote systems. (Citation: xCmd) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--pwdump | pwdump | [pwdump](https://attack.mitre.org/software/S0006) is a credential dumper. (Citation: Wikipedia pwdump) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--pass-the-hash-toolkit | Pass-The-Hash Toolkit | [Pass-The-Hash Toolkit](https://attack.mitre.org/software/S0122) is a toolkit that allows an adversary to "pass" a password hash (without knowing the original password) to log in to systems. (Citation: Mandiant APT1) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--gsecdump | gsecdump | [gsecdump](https://attack.mitre.org/software/S0008) is a publicly-available credential dumper used to obtain password hashes and LSA secrets from Windows operating systems. (Citation: TrueSec Gsecdump) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--cachedump | Cachedump | [Cachedump](https://attack.mitre.org/software/S0119) is a publicly-available tool that program extracts cached password hashes from a system’s registry. (Citation: Mandiant APT1) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--psexec | PsExec | [PsExec](https://attack.mitre.org/software/S0029) is a free Microsoft tool that can be used to execute a program on another computer. It is used by IT administrators and attackers.(Citation: Russinovich Sysinternals)(Citation: SANS PsExec) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### インフラ

未確認

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|
| GhostNet | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

GhostNet

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | China | Targeting text mentions china. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Technology | Targeting text indicates the Technology sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.001 | LSASS Memory | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1007 | System Service Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.001 | Local Account | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114.001 | Local Email Collection | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114.002 | Remote Email Collection | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1119 | Automated Collection | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1135 | Network Share Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1550.002 | Pass the Hash | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.001 | Domains | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.002 | Email Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.001 | Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 41件（`artifacts.csv`）

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
| source--apt1--2ed8c7cf265bfa54 | apt1 |  | 不明 | actor_profile/evidence/apt1.csv | structured-data | TLP:CLEAR | 中 |
| source--apt1--ed42c1aa2cfadd01 | Automating APT Campaign and Group Attribution |  | 不明 | APT-hunting/Automating APT Campaign and Group Attribution.pdf | report | TLP:CLEAR | 中 |
| source--apt1--f297252bb07624ef | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--apt1--c44a1010f1f3a09d | china cyber report |  | 不明 | International Strategic/China/china-cyber-report.pdf | report | TLP:CLEAR | 中 |
| source--apt1--63b8b4c26f3fd1fc | National Cyber Power Index 2020 |  | 2020 | National Cyber Power Index 2020.pdf | report | TLP:CLEAR | 中 |
| source--apt1--76e4b8f7e92bf68f | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--apt1--e248528f36568015 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--apt1--e3c2071e81096286 | APT blackberry mobile malware report |  | 不明 | summary/2020/APT-blackberry-mobile-malware-report.pdf | report | TLP:CLEAR | 中 |
| source--apt1--8942e30b05bc39cb | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--apt1--72fda534639ad676 | Modern Asian APT groups TTPs report eng |  | 不明 | summary/2023/Modern-Asian-APT-groups-TTPs_report_eng.pdf | report | TLP:CLEAR | 中 |
| source--apt1--547564205e678ade | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--apt1--de9bf4492a7b126e | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
