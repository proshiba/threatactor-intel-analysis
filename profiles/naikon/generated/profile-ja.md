# Naikon 脅威アクタープロファイル

- プロファイルID: `actor--naikon`
- 状態: draft
- 更新日時: 2026-09-21T04:18:00Z
- 構造バージョン: 1.3.0

## エグゼクティブサマリー

Naikonの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Naikon**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| NAIKON CASTLE | Google Threat Intelligence Group | exact | 高 | `source--gtig-unified-actor-naming-2026` | GTIG's July 2026 table explicitly maps the previous name to this new unified name. Exactness is within GTIG's taxonomy; other vendors may use different collection boundaries. |
| Naikon Team | Google Threat Intelligence Group | exact | 高 | `source--gtig-unified-actor-naming-2026` | GTIG's July 2026 table explicitly maps the previous name to this new unified name. Exactness is within GTIG's taxonomy; other vendors may use different collection boundaries. |

## 帰属

Actor-specific MITRE ATT&CK reporting supports state sponsorship; the community workbook country placement is retained only as a geographic lead.

- 国: China
- スポンサー種別: state
- 確度: 中
- 証拠: `source--mitre-attack-19-1`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | Actor-specific reporting explicitly describes espionage or intelligence collection. | 高 | `source--mitre-attack-19-1`, `source--mitre-attack-19-2` | Derived from explicit MITRE ATT&CK actor description; not inferred from country or state sponsorship. |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Lotus Blossom | overlaps-with | 共有alias: APT30 | 低 | `source--mitre-attack-19-1` |
| APT30 | related-to | While [Naikon](https://attack.mitre.org/groups/G0019) shares some characteristics with [APT30](https://attack.mitre.org/groups/G0013), the two groups do not appear to be exact matches.(Citation: Baumgartner Golovkin Naikon 2015) | 中 | `source--mitre-attack-19-2` |

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
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | NAIKON CASTLE | multiple-name-intersection | 高 |  | https://cloud.google.com/blog/topics/threat-intelligence/updated-cyber-threat-actor-naming-system |
| etda-threat-group-cards | Naikon, Lotus Panda | canonical-name | 高 | China | https://securelist.com/the-chronicles-of-the-hellsing-apt-the-empire-strikes-back/69567/<br>https://securelist.com/the-naikon-apt/69953/<br>https://exchange.xforce.ibmcloud.com/threat-group/guid:2f1962c4d7c0c994981c5bc363823c44 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Raspberry Typhoon | single-alias-intersection | 中 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Naikon | canonical-name | 高 | CN, China | https://securelist.com/analysis/publications/69953/the-naikon-apt/<br>https://www.fireeye.com/blog/threat-research/2014/03/spear-phishing-the-news-cycle-apt-actors-leverage-interest-in-the-disappearance-of-malaysian-flight-mh-370.html<br>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf |
| misp-threat-actor | LOTUS PANDA | single-alias-intersection | 中 | CN, China | https://securelist.com/blog/research/70726/the-spring-dragon-apt/<br>https://securelist.com/spring-dragon-updated-activity/79067/<br>https://www.cfr.org/interactive/cyber-operations/lotus-blossom |
| misp-microsoft-activity-group | Raspberry Typhoon | single-alias-intersection | 中 | CN, China | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | Naikon - G0019 | mitre-external-id | 高 |  | http://cdn2.hubspot.net/hubfs/454298/Project_CAMERASHY_ThreatConnect_Copyright_2015.pdf<br>https://attack.mitre.org/groups/G0019<br>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf |
| misp-mitre-intrusion-set | Naikon - G0019 | mitre-external-id | 高 |  | http://cdn2.hubspot.net/hubfs/454298/Project_CAMERASHY_ThreatConnect_Copyright_2015.pdf<br>https://attack.mitre.org/groups/G0019<br>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07205555/TheNaikonAPT-MsnMM1.pdf |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | Naikon | canonical-name | 高 | CN |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Raspberry Typhoon | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--aria-body | Aria-body | [Aria-body](https://attack.mitre.org/software/S0456) is a custom backdoor that has been used by [Naikon](https://attack.mitre.org/groups/G0019) since approximately 2017.(Citation: CheckPoint Naikon May 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--hdoor | HDoor | [HDoor](https://attack.mitre.org/software/S0061) is malware that has been customized and used by the [Naikon](https://attack.mitre.org/groups/G0019) group. (Citation: Baumgartner Naikon 2015) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--nebulae | Nebulae | [Nebulae](https://attack.mitre.org/software/S0630) Is a backdoor that has been used by [Naikon](https://attack.mitre.org/groups/G0019)  since at least 2020.(Citation: Bitdefender Naikon April 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--rainyday | RainyDay | [RainyDay](https://attack.mitre.org/software/S0629) is a backdoor tool that has been used by [Naikon](https://attack.mitre.org/groups/G0019) since at least 2020.(Citation: Bitdefender Naikon April 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--rarstone | RARSTONE | [RARSTONE](https://attack.mitre.org/software/S0055) is malware used by the [Naikon](https://attack.mitre.org/groups/G0019) group that has some characteristics similar to [PlugX](https://attack.mitre.org/software/S0013). (Citation: Aquino RARSTONE) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--sslmm | SslMM | [SslMM](https://attack.mitre.org/software/S0058) is a full-featured backdoor used by [Naikon](https://attack.mitre.org/groups/G0019) that has multiple variants. (Citation: Baumgartner Naikon 2015) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--sys10 | Sys10 | [Sys10](https://attack.mitre.org/software/S0060) is a backdoor that was used throughout 2013 by [Naikon](https://attack.mitre.org/groups/G0019). (Citation: Baumgartner Naikon 2015) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--winmm | WinMM | [WinMM](https://attack.mitre.org/software/S0059) is a full-featured, simple backdoor used by [Naikon](https://attack.mitre.org/groups/G0019). (Citation: Baumgartner Naikon 2015) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--ftp | ftp | [ftp](https://attack.mitre.org/software/S0095) is a utility commonly available with operating systems to transfer information over the File Transfer Protocol (FTP). Adversaries can use it to transfer other tools onto a system or to exfiltrate data.(Citation: Microsoft FTP)(Citation: Linux FTP) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| tool--netsh | netsh | [netsh](https://attack.mitre.org/software/S0108) is a scripting utility used to interact with networking components on local or remote systems. (Citation: TechNet Netsh) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| tool--ping | Ping | [Ping](https://attack.mitre.org/software/S0097) is an operating system utility commonly used to troubleshoot and verify network connections. (Citation: TechNet Ping) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| tool--psexec | PsExec | [PsExec](https://attack.mitre.org/software/S0029) is a free Microsoft tool that can be used to execute a program on another computer. It is used by IT administrators and attackers.(Citation: Russinovich Sysinternals)(Citation: SANS PsExec) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| tool--systeminfo | Systeminfo | [Systeminfo](https://attack.mitre.org/software/S0096) is a Windows utility that can be used to gather detailed information about a computer. (Citation: TechNet Systeminfo) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| tool--tasklist | Tasklist | The [Tasklist](https://attack.mitre.org/software/S0057) utility displays a list of applications and services with their Process IDs (PID) for all tasks running on either a local or a remote computer. It is packaged with Windows operating systems and can be executed from the command-line interface. (Citation: Microsoft Tasklist) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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

Naikon; Camera Shy

## ターゲット

ターゲット情報なし

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Discovery | T1016 | System Network Configuration Discovery | [Naikon](https://attack.mitre.org/groups/G0019) uses commands such as <code>netsh interface show</code> to discover network interface settings.(Citation: Baumgartner Naikon 2015) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1018 | Remote System Discovery | [Naikon](https://attack.mitre.org/groups/G0019) has used a netbios scanner for remote machine identification.(Citation: Bitdefender Naikon April 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1036.004 | Masquerade Task or Service | [Naikon](https://attack.mitre.org/groups/G0019) renamed a malicious service <code>taskmgr</code> to appear to be a legitimate version of Task Manager.(Citation: Bitdefender Naikon April 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [Naikon](https://attack.mitre.org/groups/G0019) has disguised malicious programs as Google Chrome, Adobe, and VMware executables.(Citation: Bitdefender Naikon April 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1046 | Network Service Discovery | [Naikon](https://attack.mitre.org/groups/G0019) has used the LadonGo scanner to scan target networks.(Citation: Bitdefender Naikon April 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1047 | Windows Management Instrumentation | [Naikon](https://attack.mitre.org/groups/G0019) has used WMIC.exe for lateral movement.(Citation: Bitdefender Naikon April 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [Naikon](https://attack.mitre.org/groups/G0019) has used schtasks.exe for lateral movement in compromised networks.(Citation: Bitdefender Naikon April 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.002 | Domain Accounts | [Naikon](https://attack.mitre.org/groups/G0019) has used administrator credentials for lateral movement in compromised networks.(Citation: Bitdefender Naikon April 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Persistence | T1137.006 | Add-ins | [Naikon](https://attack.mitre.org/groups/G0019) has used the RoyalRoad exploit builder to drop a second stage loader, intel.wll, into the Word Startup folder on the compromised host.(Citation: CheckPoint Naikon May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1204.002 | Malicious File | [Naikon](https://attack.mitre.org/groups/G0019) has convinced victims to open malicious attachments to execute malware.(Citation: CheckPoint Naikon May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1518.001 | Security Software Discovery | [Naikon](https://attack.mitre.org/groups/G0019) uses commands such as <code>netsh advfirewall firewall</code> to discover local firewall settings.(Citation: Baumgartner Naikon 2015) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [Naikon](https://attack.mitre.org/groups/G0019) has modified a victim's Windows Run registry to establish persistence.(Citation: Bitdefender Naikon April 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1566.001 | Spearphishing Attachment | [Naikon](https://attack.mitre.org/groups/G0019) has used malicious e-mail attachments to deliver malware.(Citation: CheckPoint Naikon May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution, Stealth | T1574.001 | DLL | [Naikon](https://attack.mitre.org/groups/G0019) has used DLL side-loading to load malicious DLL's into legitimate executables.(Citation: CheckPoint Naikon May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
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
- 3 alias lead(s) remain non-canonical pending original-source review.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--naikon--daaff4c63efd2431 | naikon |  | 不明 | actor_profile/evidence/naikon.csv | structured-data | TLP:CLEAR | 中 |
| source--naikon--33afc7df40fa98b7 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--naikon--ee2e46ca38fa6ff8 | Charting China’s Climb as a Leading Global Cyber Power |  | 不明 | International Strategic/China/Charting China’s Climb as a Leading Global Cyber Power.pdf | report | TLP:CLEAR | 中 |
| source--naikon--069317a15d24d8d5 | RedFoxtrot group |  | 不明 | International Strategic/China/RedFoxtrot_group.pdf | report | TLP:CLEAR | 中 |
| source--naikon--3eaac18ad1c8747e | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--naikon--e357a64bdd648e63 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--naikon--f522c40b911fb776 | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--naikon--4376f78def8ec51e | Modern Asian APT groups TTPs report eng |  | 不明 | summary/2023/Modern-Asian-APT-groups-TTPs_report_eng.pdf | report | TLP:CLEAR | 中 |
| source--naikon--836cfc176f7fceb8 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--naikon--3a23c7fb4bce3712 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--gtig-unified-actor-naming-2026 | Updated Cyber Threat Actor Naming System | Google Threat Intelligence Group | 2026-07-24 | https://cloud.google.com/blog/topics/threat-intelligence/updated-cyber-threat-actor-naming-system | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-gtig-threat-actor-naming | Google Threat Intelligence Group Unified Threat Actor Naming | Google Threat Intelligence Group | 不明 | actor_profile/reference/osint/gtig-threat-actor-naming.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-enterprise-19.1.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
