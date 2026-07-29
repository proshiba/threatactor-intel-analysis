# OceanLotus 脅威アクタープロファイル

- プロファイルID: `actor--oceanlotus`
- 状態: draft
- 更新日時: 2026-07-25T14:07:08Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

OceanLotusの標準化プロファイル。リポジトリ内の専用資料9件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **OceanLotus**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| APT32 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| APT-C-00 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| BISMUTH | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Canvas Cyclone | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| SeaLotus | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| SectorF01 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 14; mapping requires review. |
| CyberOne Security, CyberOne Technologies, Hành Tinh Company Limited, Planet and Diacauso | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 14; mapping requires review. |
| Vietnam | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 14; mapping requires review. |

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
| Adversary | [APT32](https://attack.mitre.org/groups/G0050) is a suspected Vietnam-based threat group that has been active since at least 2014. The group has targeted multiple private sector industries as well as foreign governments, dissidents, and journalists with a strong focus on Southeast Asian countries like Vietnam, the Philippines, Laos, and Cambodia. They have extensively used strategic web compromises to compromise victims.(Citation: FireEye APT32 May 2017)(Citation: Volexity OceanLotus Nov 2017)(Citation: ESET OceanLotus) |
| Capability | RotaJakiro, KOMPROGO, Kerrdown, WINDSHIELD, SOUNDBITE, Cobalt Strike, OSX_OCEANLOTUS.D, Goopy, Denis, PHOREAL, Unique suite & OTS, Microsoft ActiveMime file attachments, Net, ipconfig, Arp, netsh, Mimikatz |
| Infrastructure |  |
| Victim | This threat actor targets organizations of interest to the Vietnamese government for espionage purposes. Victims have included human rights organizations, research institutes and maritime construction firms in China, and media organizations. Heavily targeting the automotive sector since 2018. |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | APT 32, OceanLotus, SeaLotus | canonical-name | 高 | Vietnam | https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html<br>https://www.welivesecurity.com/wp-content/uploads/2018/03/ESET_OceanLotus.pdf<br>https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/SpyRATsofOceanLotusMalwareWhitePaper.pdf |
| etda-threat-group-cards | Bismuth | multiple-name-intersection | 高 | Vietnam | https://www.microsoft.com/security/blog/2020/11/30/threat-actor-leverages-coin-miner-techniques-to-stay-under-the-radar-heres-how-to-spot-them/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Bismuth&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Canvas Cyclone | canonical-name | 高 | Vietnam | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | APT32 | canonical-name | 高 | VN, Vietnam | https://attack.mitre.org/groups/G0050/<br>https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html<br>https://www.cybereason.com/labs-operation-cobalt-kitty-a-large-scale-apt-in-asia-carried-out-by-the-oceanlotus-group/ |
| misp-microsoft-activity-group | Canvas Cyclone | canonical-name | 高 | VN, Vietnam | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | APT32 - G0050 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0050<br>https://www.fireeye.com/blog/threat-research/2017/05/cyber-espionage-apt32.html<br>https://www.volexity.com/blog/2017/11/06/oceanlotus-blossoms-mass-digital-surveillance-and-exploitation-of-asean-nations-the-media-human-rights-and-civil-society/ |
| misp-mitre-intrusion-set | APT32 - G0050 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0050<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://www.amnestyusa.org/wp-content/uploads/2021/02/Click-and-Bait_Vietnamese-Human-Rights-Defenders-Targeted-with-Spyware-Attacks.pdf |
| misp-360net | 海莲花 - APT-C-00 | canonical-name | 高 | vietnam | https://apt.360.net/report/apts/93.html<br>https://apt.360.net/report/apts/1.html<br>https://apt.360.net/report/apts/94.html |

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
| malware--rotajakiro | RotaJakiro | [RotaJakiro](https://attack.mitre.org/software/S1078) is a 64-bit Linux backdoor used by [APT32](https://attack.mitre.org/groups/G0050). First seen in 2018, it uses a plugin architecture to extend capabilities. [RotaJakiro](https://attack.mitre.org/software/S1078) can determine it's permission level and execute according to access type (`root` or `user`).(Citation: RotaJakiro 2021 netlab360 analysis)(Citation: netlab360 rotajakiro vs oceanlotus) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--komprogo | KOMPROGO | [KOMPROGO](https://attack.mitre.org/software/S0156) is a signature backdoor used by [APT32](https://attack.mitre.org/groups/G0050) that is capable of process, file, and registry management. (Citation: FireEye APT32 May 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--kerrdown | Kerrdown | [Kerrdown](https://attack.mitre.org/software/S0585) is a custom downloader that has been used by [APT32](https://attack.mitre.org/groups/G0050) since at least 2018 to install spyware from a server on the victim's network.(Citation: Amnesty Intl. Ocean Lotus February 2021)(Citation: Unit 42 KerrDown February 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--windshield | WINDSHIELD | [WINDSHIELD](https://attack.mitre.org/software/S0155) is a signature backdoor used by [APT32](https://attack.mitre.org/groups/G0050). (Citation: FireEye APT32 May 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--soundbite | SOUNDBITE | [SOUNDBITE](https://attack.mitre.org/software/S0157) is a signature backdoor used by [APT32](https://attack.mitre.org/groups/G0050). (Citation: FireEye APT32 May 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--cobalt-strike | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) is a commercial, full-featured, remote access tool that bills itself as “adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors”. Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.(Citation: cobaltstrike manual)<br><br>In addition to its own capabilities, [Cobalt Strike](https://attack.mitre.org/software/S0154) leverages the capabilities of other well-known tools such as Metasploit and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: cobaltstrike manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--osx-oceanlotus-d | OSX_OCEANLOTUS.D | [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) is a macOS backdoor used by [APT32](https://attack.mitre.org/groups/G0050). First discovered in 2015, [APT32](https://attack.mitre.org/groups/G0050) has continued to make improvements using a plugin architecture to extend capabilities, specifically using `.dylib` files. [OSX_OCEANLOTUS.D](https://attack.mitre.org/software/S0352) can also determine it's permission level and execute according to access type (`root` or `user`).(Citation: Unit42 OceanLotus 2017)(Citation: TrendMicro MacOS April 2018)(Citation: Trend Micro MacOS Backdoor November 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--goopy | Goopy | [Goopy](https://attack.mitre.org/software/S0477) is a Windows backdoor and Trojan used by [APT32](https://attack.mitre.org/groups/G0050) and shares several similarities to another backdoor used by the group ([Denis](https://attack.mitre.org/software/S0354)). [Goopy](https://attack.mitre.org/software/S0477) is named for its impersonation of the legitimate Google Updater executable.(Citation: Cybereason Cobalt Kitty 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--denis | Denis | [Denis](https://attack.mitre.org/software/S0354) is a Windows backdoor and Trojan used by [APT32](https://attack.mitre.org/groups/G0050). [Denis](https://attack.mitre.org/software/S0354) shares several similarities to the [SOUNDBITE](https://attack.mitre.org/software/S0157) backdoor and has been used in conjunction with the [Goopy](https://attack.mitre.org/software/S0477) backdoor.(Citation: Cybereason Oceanlotus May 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--phoreal | PHOREAL | [PHOREAL](https://attack.mitre.org/software/S0158) is a signature backdoor used by [APT32](https://attack.mitre.org/groups/G0050). (Citation: FireEye APT32 May 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--unique-suite-ots | Unique suite & OTS | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--microsoft-activemime-file-attachments | Microsoft ActiveMime file attachments | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ipconfig | ipconfig | [ipconfig](https://attack.mitre.org/software/S0100) is a Windows utility that can be used to find information about a system's TCP/IP, DNS, DHCP, and adapter configuration. (Citation: TechNet Ipconfig) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--arp | Arp | [Arp](https://attack.mitre.org/software/S0099) displays and modifies information about a system's Address Resolution Protocol (ARP) cache. (Citation: TechNet Arp) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--netsh | netsh | [netsh](https://attack.mitre.org/software/S0108) is a scripting utility used to interact with networking components on local or remote systems. (Citation: TechNet Netsh) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| Cobalt Kitty | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

Cobalt Kitty

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | China | Targeting text mentions china. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Government | Targeting text indicates the Government sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Education and Research | Targeting text indicates the Education and Research sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Media | Targeting text indicates the Media sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Transportation | Targeting text indicates the Transportation sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1001 | Data Obfuscation | Screen Capture T1115 Clipboard Data Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考链接 https://s.tencent.com/research/report/715.html 6.5 详细技术细节 1、 样本组织部干部四处最新通知更新.doc（c90c7abcee1d98a8663904d739185d16） 该样本里的宏代码经过混淆处理，对变量名函数名等进行简单命名后如下： |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Credential Access | T1003 | OS Credential Dumping | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.001 | LSASS Memory | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | TLP：WHITE 腾讯安全御见威胁情报中心 39 / 88 T1007 System Service Discovery Lateral Movement T1534 Internal Spearphishing Collection T1005 Data from Local System T1025 Data from Removable Media T1123 Audio Capture T1056 Input Capture T1113 Screen Capture T1115 Clipboard Data Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscat |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Discovery | T1007 | System Service Discovery | TLP：WHITE 腾讯安全御见威胁情报中心 39 / 88 T1007 System Service Discovery Lateral Movement T1534 Internal Spearphishing Collection T1005 Data from Local System T1025 Data from Removable Media T1123 Audio Capture T1056 Input Capture T1113 Screen Capture T1115 Clipboard Data Command and Control T1043 Commonly Used Port T1094 Cus |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Discovery | T1012 | Query Registry | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1024 | MITRE ATT&CK T1024 | io Capture T1056 Input Capture T1113 Screen Capture T1115 Clipboard Data Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考链接 https://s.tencent.com/research/report/715.html 6.5 详细技术细节 1、 样本组织部干部四处最新通知更新.doc（c90c7abcee1d98a8663904d739185d16） 该样本里的宏代码经过混淆处理，对变量名函数名等进行简单命名后如下： |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Collection | T1025 | Data from Removable Media | TLP：WHITE 腾讯安全御见威胁情报中心 39 / 88 T1007 System Service Discovery Lateral Movement T1534 Internal Spearphishing Collection T1005 Data from Local System T1025 Data from Removable Media T1123 Audio Capture T1056 Input Capture T1113 Screen Capture T1115 Clipboard Data Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Por |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Stealth | T1027 | Obfuscated Files or Information | 0 Registry Run Keys / Startup Folder Defense Evasion T1107 File Deletion T1140 Deobfuscate/Decode Files or Information T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp T1117 Regsvr32 Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discovery T1057 Process Discovery T1082 System Inform |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Stealth | T1027.010 | Command Obfuscation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.011 | Fileless Storage | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.016 | Junk Code Insertion | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036 | Masquerading | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--oceanlotus--e15849fad928c3c1` |
| Stealth | T1036.003 | Rename Legitimate Utilities | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.004 | Masquerade Task or Service | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1043 | Commonly Used Port | 05 Data from Local System T1025 Data from Removable Media T1123 Audio Capture T1056 Input Capture T1113 Screen Capture T1115 Clipboard Data Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考链接 https://s.tencent.com/research/report/715.html 6.5 详细技术细节 1、 样本组织部干部四处最新通知更新.doc（c90c7abcee1d98a8663904d739185d16） 该样本里的宏代码 |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Discovery | T1046 | Network Service Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--oceanlotus--e15849fad928c3c1` |
| Execution | T1047 | Windows Management Instrumentation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1048.003 | Exfiltration Over Unencrypted Non-C2 Protocol | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053 | Scheduled Task/Job | TLP：WHITE 腾讯安全御见威胁情报中心 38 / 88 T1053 Scheduled Task T1117 Regsvr32 Persistence T1179 Hooking T1053 Scheduled Task T1060 Registry Run Keys / Startup Folder Defense Evasion T1107 File Deletion T1140 Deobfuscate/Decode Files or Information T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055 | Process Injection | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056 | Input Capture | on T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp T1117 Regsvr32 Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discovery T1057 Process Discovery T1082 System Information Discovery |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Collection, Credential Access | T1056.001 | Keylogging | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | 2 Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discovery T1057 Process Discovery T1082 System Information Discovery |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Execution | T1059 | Command and Scripting Interpreter | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.007 | JavaScript | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1060 | MITRE ATT&CK T1060 | TLP：WHITE 腾讯安全御见威胁情报中心 38 / 88 T1053 Scheduled Task T1117 Regsvr32 Persistence T1179 Hooking T1053 Scheduled Task T1060 Registry Run Keys / Startup Folder Defense Evasion T1107 File Deletion T1140 Deobfuscate/Decode Files or Information T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp T1117 Regsvr32 Credential Access T1179 Hooking T1056 |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Uncategorized | T1065 | MITRE ATT&CK T1065 | lipboard Data Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考链接 https://s.tencent.com/research/report/715.html 6.5 详细技术细节 1、 样本组织部干部四处最新通知更新.doc（c90c7abcee1d98a8663904d739185d16） 该样本里的宏代码经过混淆处理，对变量名函数名等进行简单命名后如下： |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Privilege Escalation | T1068 | Exploitation for Privilege Escalation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.006 | Timestomp | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.003 | Mail Protocols | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Lateral Movement | T1072 | Software Deployment Tools | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.003 | Local Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--oceanlotus--e15849fad928c3c1` |
| Discovery | T1083 | File and Directory Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--oceanlotus--e15849fad928c3c1` |
| Uncategorized | T1085 | MITRE ATT&CK T1085 | Initial Access T1193 Spearphishing Attachment Execution T1106 Execution through API T1129 Execution through Module Load T1203 Exploitation for Client Execution T1085 Rundll32 T1204 User Execution T1223 Compiled HTML File |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Discovery | T1087.001 | Local Account | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1094 | MITRE ATT&CK T1094 | T1025 Data from Removable Media T1123 Audio Capture T1056 Input Capture T1113 Screen Capture T1115 Clipboard Data Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考链接 https://s.tencent.com/research/report/715.html 6.5 详细技术细节 1、 样本组织部干部四处最新通知更新.doc（c90c7abcee1d98a8663904d739185d16） 该样本里的宏代码经过混淆处理，对变量名函数名等进行简单命名后如下： |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Uncategorized | T1099 | MITRE ATT&CK T1099 | T1107 File Deletion T1140 Deobfuscate/Decode Files or Information T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp T1117 Regsvr32 Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Service Scanning T1135 Network Share Discovery T1057 Process Discovery T1082 System Information Discovery |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Command And Control | T1102 | Web Service | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1106 | Native API | hardware.com cdnwebmedia.com 43.251.100.20 43.254.217.67 114.118.80.233 6.3 MITRE ATT&CK Tactic ID Name Initial Access T1193 Spearphishing Attachment Execution T1106 Execution through API T1129 Execution through Module Load T1203 Exploitation for Client Execution T1085 Rundll32 T1204 User Execution T1223 Compiled HTML File |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Uncategorized | T1107 | MITRE ATT&CK T1107 | 讯安全御见威胁情报中心 38 / 88 T1053 Scheduled Task T1117 Regsvr32 Persistence T1179 Hooking T1053 Scheduled Task T1060 Registry Run Keys / Startup Folder Defense Evasion T1107 File Deletion T1140 Deobfuscate/Decode Files or Information T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp T1117 Regsvr32 Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discove |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--oceanlotus--e15849fad928c3c1` |
| Collection | T1113 | Screen Capture | y Lateral Movement T1534 Internal Spearphishing Collection T1005 Data from Local System T1025 Data from Removable Media T1123 Audio Capture T1056 Input Capture T1113 Screen Capture T1115 Clipboard Data Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考链接 https://s.tencent.com/research/report/715.html 6.5 详细技术细节 1、 |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Collection | T1115 | Clipboard Data | 534 Internal Spearphishing Collection T1005 Data from Local System T1025 Data from Removable Media T1123 Audio Capture T1056 Input Capture T1113 Screen Capture T1115 Clipboard Data Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考链接 https://s.tencent.com/research/report/715.html 6.5 详细技术细节 1、 样本组织部干部四处最新通知更新.doc（c |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Uncategorized | T1117 | MITRE ATT&CK T1117 | TLP：WHITE 腾讯安全御见威胁情报中心 38 / 88 T1053 Scheduled Task T1117 Regsvr32 Persistence T1179 Hooking T1053 Scheduled Task T1060 Registry Run Keys / Startup Folder Defense Evasion T1107 File Deletion T1140 Deobfuscate/Decode Files or Information T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Collection | T1123 | Audio Capture | 中心 39 / 88 T1007 System Service Discovery Lateral Movement T1534 Internal Spearphishing Collection T1005 Data from Local System T1025 Data from Removable Media T1123 Audio Capture T1056 Input Capture T1113 Screen Capture T1115 Clipboard Data Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cryptographic Protocol T1001 Data Obfuscation T1065 Uncommonly Used Port 6.4 参考链接 https://s.tencent.com |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Execution | T1129 | Shared Modules | 43.251.100.20 43.254.217.67 114.118.80.233 6.3 MITRE ATT&CK Tactic ID Name Initial Access T1193 Spearphishing Attachment Execution T1106 Execution through API T1129 Execution through Module Load T1203 Exploitation for Client Execution T1085 Rundll32 T1204 User Execution T1223 Compiled HTML File |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Discovery | T1135 | Network Share Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--oceanlotus--e15849fad928c3c1` |
| Persistence | T1137 | Office Application Startup | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | T1053 Scheduled Task T1117 Regsvr32 Persistence T1179 Hooking T1053 Scheduled Task T1060 Registry Run Keys / Startup Folder Defense Evasion T1107 File Deletion T1140 Deobfuscate/Decode Files or Information T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp T1117 Regsvr32 Credential Access T1179 Hooking T1056 Input Capture Discovery T1083 File and Directory Discovery T1046 Network Ser |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Uncategorized | T1179 | MITRE ATT&CK T1179 | TLP：WHITE 腾讯安全御见威胁情报中心 38 / 88 T1053 Scheduled Task T1117 Regsvr32 Persistence T1179 Hooking T1053 Scheduled Task T1060 Registry Run Keys / Startup Folder Defense Evasion T1107 File Deletion T1140 Deobfuscate/Decode Files or Information T1036 Masquerading T1112 Modify Registry T1027 Obfuscated Files or Information T1085 Rundll32 T1099 Timestomp T1117 Regsvr32 Cr |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Initial Access | T1189 | Drive-by Compromise | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1193 | MITRE ATT&CK T1193 | us.melvillepitcairn.com upgrade.coldriverhardware.com cdnwebmedia.com 43.251.100.20 43.254.217.67 114.118.80.233 6.3 MITRE ATT&CK Tactic ID Name Initial Access T1193 Spearphishing Attachment Execution T1106 Execution through API T1129 Execution through Module Load T1203 Exploitation for Client Execution T1085 Rundll32 T1204 User Execution T1223 Compiled HTML File |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Execution | T1203 | Exploitation for Client Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--oceanlotus--e15849fad928c3c1` |
| Execution | T1204 | User Execution | T1193 Spearphishing Attachment Execution T1106 Execution through API T1129 Execution through Module Load T1203 Exploitation for Client Execution T1085 Rundll32 T1204 User Execution T1223 Compiled HTML File |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Execution | T1204.001 | Malicious Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1216.001 | PubPrn | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.005 | Mshta | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.010 | Regsvr32 | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.011 | Rundll32 | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1222.002 | Linux and Mac Permissions | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1223 | MITRE ATT&CK T1223 | ttachment Execution T1106 Execution through API T1129 Execution through Module Load T1203 Exploitation for Client Execution T1085 Rundll32 T1204 User Execution T1223 Compiled HTML File |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Persistence | T1505.003 | Web Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1534 | Internal Spearphishing | TLP：WHITE 腾讯安全御见威胁情报中心 39 / 88 T1007 System Service Discovery Lateral Movement T1534 Internal Spearphishing Collection T1005 Data from Local System T1025 Data from Removable Media T1123 Audio Capture T1056 Input Capture T1113 Screen Capture T1115 Clipboard Data Command and Control T1043 Commonly Used Port T1094 Custom Command and Control Protocol T1024 Custom Cr |  |  | 不明 | 不明 | 中 | `source--oceanlotus--e15849fad928c3c1` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1550.002 | Pass the Hash | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1550.003 | Pass the Ticket | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.002 | Credentials in Registry | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560 | Archive Collected Data | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.001 | Hidden Files and Directories | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.003 | Hidden Window | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.004 | NTFS File Attributes | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1569.002 | Service Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1570 | Lateral Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1571 | Non-Standard Port | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.006 | Web Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.001 | Social Media Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589 | Gather Victim Identity Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589.002 | Email Addresses | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1598.003 | Spearphishing Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.001 | Upload Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.004 | Drive-by Target | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685.005 | Clear Windows Event Logs | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 339件
- IOC観測: 387件
- 複数攻撃で観測: 0件
- 要レビュー候補: 186件
- 非IOC artifact観測: 327件（`artifacts.csv`）

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
| source--oceanlotus--a7175b421ca1736c | ESET OceanLotus |  | 不明 | Oceanlotus/ESET_OceanLotus.pdf | report | TLP:CLEAR | 中 |
| source--oceanlotus--d9ef73283beaecf5 | OceanLotus' Attacks to Indochinese Peninsula Evolution of Targets, Techniques and Procedure |  | 不明 | Oceanlotus/OceanLotus' Attacks to Indochinese Peninsula Evolution of Targets, Techniques and Procedure.pdf | report | TLP:CLEAR | 中 |
| source--oceanlotus--0a5ba4ea429a9916 | OceanLotus Steganography Malware Analysis White Paper |  | 不明 | Oceanlotus/OceanLotus-Steganography-Malware-Analysis-White-Paper.pdf | report | TLP:CLEAR | 中 |
| source--oceanlotus--9a1ee229cc72c74b | Oceanlotus APK sample |  | 不明 | Oceanlotus/Oceanlotus-APK-sample.TXT | text-data | TLP:CLEAR | 中 |
| source--oceanlotus--8c52284824684bb3 | README |  | 不明 | Oceanlotus/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--oceanlotus--4987b0d4cde44760 | Stairwell threat report The origin of APT32 macros |  | 不明 | Oceanlotus/Stairwell-threat-report-The-origin-of-APT32-macros.pdf | report | TLP:CLEAR | 中 |
| source--oceanlotus--e15849fad928c3c1 | apt32 report 2019 |  | 2019 | Oceanlotus/apt32_report_2019.pdf | report | TLP:CLEAR | 中 |
| source--oceanlotus--5bb5ce3ec25f97e9 | hunting rule |  | 不明 | Oceanlotus/hunting-rule.txt | text-data | TLP:CLEAR | 中 |
| source--oceanlotus--692f1686b5c44964 | README |  | 不明 | Oceanlotus/sample/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--osint-misp-360net | MISP Galaxy 360.net Threat Actors | MISP Project / 360 Netlab | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
