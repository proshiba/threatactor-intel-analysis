# Turla 脅威アクタープロファイル

プロファイルID: `actor--turla`  
状態: draft  
更新日時: 2026-07-25T14:07:08Z  
構造バージョン: 1.0.0

## エグゼクティブサマリー

Turlaの標準化プロファイル。リポジトリ内の専用資料7件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Turla**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| BELUGASTURGEON | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Group 88 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| IRON HUNTER | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Krypton | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Secret Blizzard | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Snake | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Venomous Bear | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Waterbug | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| WhiteBear | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| Adversary | [Turla](https://attack.mitre.org/groups/G0010) is a cyber espionage threat group that has been attributed to Russia's Federal Security Service (FSB).  They have compromised victims in over 50 countries since at least 2004, spanning a range of industries including government, embassies, military, education, research and pharmaceutical companies. [Turla](https://attack.mitre.org/groups/G0010) is known for conducting watering hole and spearphishing campaigns, and leveraging in-house tools and malware, such as [Uroburos](https://attack.mitre.org/software/S0022).(Citation: Kaspersky Turla)(Citation: ESET Gazer Aug 2017)(Citation: CrowdStrike VENOMOUS BEAR)(Citation: ESET Turla Mosquito Jan 2018)(Citation: Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023) |
| Capability | KOPILUWAK, TinyTurla, HyperStack, Kazuar, LunarLoader, Epic, LightNeuron, Gazer, Uroburos, Crutch, Mosquito, LunarMail, Carbon, Penquin, ComRAT, PowerStallion, LunarWeb, Net, certutil, Tasklist, Arp, Empire, netstat, Systeminfo, Mimikatz, IronNetInjector, nbtstat, NBTscan, Reg, PsExec |
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
| etda-threat-group-cards | Turla, Waterbug, Venomous Bear | canonical-name | 高 | Russia | https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/waterbug-attack-group.pdf<br>https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-march-venomous-bear/<br>https://www.recordedfuture.com/turla-apt-infrastructure/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Secret Blizzard | canonical-name | 高 | Russia | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Turla | canonical-name | 高 | RU, Russian Federation | https://www.circl.lu/pub/tr-25/<br>https://securelist.com/introducing-whitebear/81638/<br>https://securelist.com/the-epic-turla-operation/65545/ |
| misp-threat-actor | White Bear | single-alias-intersection | 中 | RU, Russian Federation | https://securelist.com/introducing-whitebear/81638/<br>https://www.cfr.org/interactive/cyber-operations/whitebear |
| misp-microsoft-activity-group | Secret Blizzard | canonical-name | 高 | RU, Russia | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | Turla - G0010 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0010<br>https://securelist.com/the-epic-turla-operation/65545/<br>https://www.welivesecurity.com/wp-content/uploads/2017/08/eset-gazer.pdf |
| misp-mitre-intrusion-set | Turla - G0010 | mitre-external-id | 高 |  | http://www.secureworks.com/research/threat-profiles/iron-hunter<br>https://attack.mitre.org/groups/G0010<br>https://blog.talosintelligence.com/2021/09/tinyturla.html |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| APT26 | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--kopiluwak | KOPILUWAK | [KOPILUWAK](https://attack.mitre.org/software/S1075) is a JavaScript-based reconnaissance tool that has been used for victim profiling and C2 since at least 2017.(Citation: Mandiant Suspected Turla Campaign February 2023) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--tinyturla | TinyTurla | [TinyTurla](https://attack.mitre.org/software/S0668) is a backdoor that has been used by [Turla](https://attack.mitre.org/groups/G0010) against targets in the US, Germany, and Afghanistan since at least 2020.(Citation: Talos TinyTurla September 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--hyperstack | HyperStack | [HyperStack](https://attack.mitre.org/software/S0537) is a RPC-based backdoor used by [Turla](https://attack.mitre.org/groups/G0010) since at least 2018. [HyperStack](https://attack.mitre.org/software/S0537) has similarities to other backdoors used by [Turla](https://attack.mitre.org/groups/G0010) including [Carbon](https://attack.mitre.org/software/S0335).(Citation: Accenture HyperStack October 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--kazuar | Kazuar | [Kazuar](https://attack.mitre.org/software/S0265) is a fully featured, multi-platform backdoor Trojan written using the Microsoft .NET framework. (Citation: Unit 42 Kazuar May 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--lunarloader | LunarLoader | [LunarLoader](https://attack.mitre.org/software/S1143) is the loader component for the [LunarWeb](https://attack.mitre.org/software/S1141) and [LunarMail](https://attack.mitre.org/software/S1142) backdoors that has been used by [Turla](https://attack.mitre.org/groups/G0010) since at least 2020 including against a European ministry of foreign affairs (MFA). [LunarLoader](https://attack.mitre.org/software/S1143) has been observed as a standalone and as a part of trojanized open-source software such as AdmPwd.(Citation: ESET Turla Lunar toolset May 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--epic | Epic | [Epic](https://attack.mitre.org/software/S0091) is a backdoor that has been used by [Turla](https://attack.mitre.org/groups/G0010). (Citation: Kaspersky Turla) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--lightneuron | LightNeuron | [LightNeuron](https://attack.mitre.org/software/S0395) is a sophisticated backdoor that has targeted Microsoft Exchange servers since at least 2014. [LightNeuron](https://attack.mitre.org/software/S0395) has been used by [Turla](https://attack.mitre.org/groups/G0010) to target diplomatic and foreign affairs-related organizations. The presence of certain strings in the malware suggests a Linux variant of [LightNeuron](https://attack.mitre.org/software/S0395) exists.(Citation: ESET LightNeuron May 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--gazer | Gazer | [Gazer](https://attack.mitre.org/software/S0168) is a backdoor used by [Turla](https://attack.mitre.org/groups/G0010) since at least 2016. (Citation: ESET Gazer Aug 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--uroburos | Uroburos | [Uroburos](https://attack.mitre.org/software/S0022) is a sophisticated cyber espionage tool written in C that has been used by units within Russia's Federal Security Service (FSB) associated with the [Turla](https://attack.mitre.org/groups/G0010) toolset to collect intelligence on sensitive targets worldwide. [Uroburos](https://attack.mitre.org/software/S0022) has several variants and has undergone nearly constant upgrade since its initial development in 2003 to keep it viable after public disclosures. [Uroburos](https://attack.mitre.org/software/S0022) is typically deployed to external-facing nodes on a targeted network and has the ability to leverage additional tools and TTPs to further exploit an internal network. [Uroburos](https://attack.mitre.org/software/S0022) has interoperable implants for Windows, Linux, and macOS, employs a high level of stealth in communications and architecture, and can easily incorporate new or replacement components.(Citation: Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023)(Citation: Kaspersky Turla) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--crutch | Crutch | [Crutch](https://attack.mitre.org/software/S0538) is a backdoor designed for document theft that has been used by [Turla](https://attack.mitre.org/groups/G0010) since at least 2015.(Citation: ESET Crutch December 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--mosquito | Mosquito | [Mosquito](https://attack.mitre.org/software/S0256) is a Win32 backdoor that has been used by [Turla](https://attack.mitre.org/groups/G0010). [Mosquito](https://attack.mitre.org/software/S0256) is made up of three parts: the installer, the launcher, and the backdoor. The main backdoor is called CommanderDLL and is launched by the loader program. (Citation: ESET Turla Mosquito Jan 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--lunarmail | LunarMail | [LunarMail](https://attack.mitre.org/software/S1142) is a backdoor that has been used by [Turla](https://attack.mitre.org/groups/G0010) since at least 2020 including in a compromise of a European ministry of foreign affairs (MFA) in conjunction with [LunarLoader](https://attack.mitre.org/software/S1143) and [LunarWeb](https://attack.mitre.org/software/S1141). [LunarMail](https://attack.mitre.org/software/S1142) is designed to be deployed on workstations and can use email messages and [Steganography](https://attack.mitre.org/techniques/T1001/002) in command and control.(Citation: ESET Turla Lunar toolset May 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--carbon | Carbon | [Carbon](https://attack.mitre.org/software/S0335) is a sophisticated, second-stage backdoor and framework that can be used to steal sensitive information from victims. [Carbon](https://attack.mitre.org/software/S0335) has been selectively used by [Turla](https://attack.mitre.org/groups/G0010) to target government and foreign affairs-related organizations in Central Asia.(Citation: ESET Carbon Mar 2017)(Citation: Securelist Turla Oct 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--penquin | Penquin | [Penquin](https://attack.mitre.org/software/S0587) is a remote access trojan (RAT) with multiple versions used by [Turla](https://attack.mitre.org/groups/G0010) to target Linux systems since at least 2014.(Citation: Kaspersky Turla Penquin December 2014)(Citation: Leonardo Turla Penquin May 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--comrat | ComRAT | [ComRAT](https://attack.mitre.org/software/S0126) is a second stage implant suspected of being a descendant of [Agent.btz](https://attack.mitre.org/software/S0092) and used by [Turla](https://attack.mitre.org/groups/G0010). The first version of [ComRAT](https://attack.mitre.org/software/S0126) was identified in 2007, but the tool has undergone substantial development for many years since.(Citation: Symantec Waterbug)(Citation: NorthSec 2015 GData Uroburos Tools)(Citation: ESET ComRAT May 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--powerstallion | PowerStallion | [PowerStallion](https://attack.mitre.org/software/S0393) is a lightweight [PowerShell](https://attack.mitre.org/techniques/T1059/001) backdoor used by [Turla](https://attack.mitre.org/groups/G0010), possibly as a recovery access tool to install other backdoors.(Citation: ESET Turla PowerShell May 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--lunarweb | LunarWeb | [LunarWeb](https://attack.mitre.org/software/S1141) is a backdoor that has been used by [Turla](https://attack.mitre.org/groups/G0010) since at least 2020 including in a compromise of a European ministry of foreign affairs (MFA) together with [LunarLoader](https://attack.mitre.org/software/S1143) and [LunarMail](https://attack.mitre.org/software/S1142). [LunarWeb](https://attack.mitre.org/software/S1141) has only been observed deployed against servers and can use [Steganography](https://attack.mitre.org/techniques/T1001/002) to obfuscate command and control.(Citation: ESET Turla Lunar toolset May 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--certutil | certutil | [certutil](https://attack.mitre.org/software/S0160) is a command-line utility that can be used to obtain certificate authority information and configure Certificate Services. (Citation: TechNet Certutil) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--tasklist | Tasklist | The [Tasklist](https://attack.mitre.org/software/S0057) utility displays a list of applications and services with their Process IDs (PID) for all tasks running on either a local or a remote computer. It is packaged with Windows operating systems and can be executed from the command-line interface. (Citation: Microsoft Tasklist) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--arp | Arp | [Arp](https://attack.mitre.org/software/S0099) displays and modifies information about a system's Address Resolution Protocol (ARP) cache. (Citation: TechNet Arp) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--empire | Empire | [Empire](https://attack.mitre.org/software/S0363) is an open-source, cross-platform remote administration and post-exploitation framework that is publicly available on GitHub. While the tool itself is primarily written in Python, the post-exploitation agents are written in pure [PowerShell](https://attack.mitre.org/techniques/T1059/001) for Windows and Python for Linux/macOS. [Empire](https://attack.mitre.org/software/S0363) was one of five tools singled out by a joint report on public hacking tools being widely used by adversaries.(Citation: NCSC Joint Report Public Tools)(Citation: Github PowerShell Empire)(Citation: GitHub ATTACK Empire) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--netstat | netstat | [netstat](https://attack.mitre.org/software/S0104) is an operating system utility that displays active TCP connections, listening ports, and network statistics. (Citation: TechNet Netstat) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--systeminfo | Systeminfo | [Systeminfo](https://attack.mitre.org/software/S0096) is a Windows utility that can be used to gather detailed information about a computer. (Citation: TechNet Systeminfo) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ironnetinjector | IronNetInjector | [IronNetInjector](https://attack.mitre.org/software/S0581) is a [Turla](https://attack.mitre.org/groups/G0010) toolchain that utilizes scripts from the open-source IronPython implementation of Python with a .NET injector to drop one or more payloads including [ComRAT](https://attack.mitre.org/software/S0126).(Citation: Unit 42 IronNetInjector February 2021 ) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--nbtstat | nbtstat | [nbtstat](https://attack.mitre.org/software/S0102) is a utility used to troubleshoot NetBIOS name resolution. (Citation: TechNet Nbtstat) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--nbtscan | NBTscan | [NBTscan](https://attack.mitre.org/software/S0590) is an open source tool that has been used by state groups to conduct internal reconnaissance within a compromised network.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan June 2003)(Citation: Symantec Waterbug Jun 2019)(Citation: FireEye APT39 Jan 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--reg | Reg | [Reg](https://attack.mitre.org/software/S0075) is a Windows utility used to interact with the Windows Registry. It can be used at the command-line interface to query, add, modify, and remove information. (Citation: Microsoft Reg)<br><br>Utilities such as [Reg](https://attack.mitre.org/software/S0075) are known to be used by persistent threats. (Citation: Windows Commands JPCERT) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
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

活動履歴なし



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Uncategorized | T0840 | MITRE ATT&CK T0840 | ion layer to the distant command processing layer, can and do remain entirely agnostic to the transport layer as long as it implements 4 MITRE ATT&CK IDs: [T0840], [T1003], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Command And Control | T1001 | Data Obfuscation | 128 encrypted using a different key for incoming and outgoing data. These keys were saved in the 0x2 Container in the 0x227 and 0x228 30 MITRE ATT&CK IDs: [T1001], [T1104] 31 MITRE ATT&CK IDs: [T1074], [T1119], [T1560.003] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Command And Control | T1001.003 | Protocol or Service Impersonation | tion mechanism to distinguish Snake traffic from legitimate traffic destined for application software on the compromised server. This 18 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1071.003], [T1090.003], [T1095], [T1132], [T1572], [T1573] 19 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1132.002], [T1547.006], [T1584] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Credential Access | T1003 | OS Credential Dumping | to the distant command processing layer, can and do remain entirely agnostic to the transport layer as long as it implements 4 MITRE ATT&CK IDs: [T0840], [T1003], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Collection | T1005 | Data from Local System | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1007 | System Service Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1012 | Query Registry | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1014 | Rootkit | %\WinSxS\ directory. Executing WerFault.exe will start the process of decrypting Snake’s components and loading them into memory.11 10 MITRE ATT&CK IDs: [T1014], [T1027], [T1547.006], [T1610] 11 MITRE ATT&CK IDs: [T1027], [T1036], [T1140], [T1564], [T1569.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Discovery | T1016 | System Network Configuration Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016.001 | Internet Connection Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1024 | MITRE ATT&CK T1024 | es Guerrero- Saade (GReAT), Costin Raiu (GReAT), Daniel Moore (King’s College London), Thomas Rid (King’s College London). April 2017. T1105 T1059 T1205 T1024 T1032 T1158 T1222 T1094 8% 8% 25% 17% 42% EXECUTION LATERAL MOVEMENT PERSISTENCE COMMAND AND CONTROL DEFENCE EVASION TACTICS MITRE ATT&CK TTPs |  |  | 不明 | 不明 | 中 | `source--turla--f0c7ef1fbe87f2c6` |
| Collection | T1025 | Data from Removable Media | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027 | Obfuscated Files or Information | directory. Executing WerFault.exe will start the process of decrypting Snake’s components and loading them into memory.11 10 MITRE ATT&CK IDs: [T1014], [T1027], [T1547.006], [T1610] 11 MITRE ATT&CK IDs: [T1027], [T1036], [T1140], [T1564], [T1569.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Stealth | T1027.002 | Software Packing | isguising the installer on a host. The first was as a JPEG viewer; later options included disguising the installer as Notepad++ or 7zip. 8 MITRE ATT&CK IDs: [T1027.002], [T1140], [T1546.016], [T1588], [T1610] 9 MITRE ATT&CK IDs: [T1573.001], [T1573.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Stealth | T1027.005 | Indicator Removal from Tools | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.010 | Command Obfuscation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.011 | Fileless Storage | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1032 | MITRE ATT&CK T1032 | ero- Saade (GReAT), Costin Raiu (GReAT), Daniel Moore (King’s College London), Thomas Rid (King’s College London). April 2017. T1105 T1059 T1205 T1024 T1032 T1158 T1222 T1094 8% 8% 25% 17% 42% EXECUTION LATERAL MOVEMENT PERSISTENCE COMMAND AND CONTROL DEFENCE EVASION TACTICS MITRE ATT&CK TTPs |  |  | 不明 | 不明 | 中 | `source--turla--f0c7ef1fbe87f2c6` |
| Stealth | T1036 | Masquerading | ecrypting Snake’s components and loading them into memory.11 10 MITRE ATT&CK IDs: [T1014], [T1027], [T1547.006], [T1610] 11 MITRE ATT&CK IDs: [T1027], [T1036], [T1140], [T1564], [T1569.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access, Discovery | T1040 | Network Sniffing | istant command processing layer, can and do remain entirely agnostic to the transport layer as long as it implements 4 MITRE ATT&CK IDs: [T0840], [T1003], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Discovery | T1046 | Network Service Discovery | mmand processing layer, can and do remain entirely agnostic to the transport layer as long as it implements 4 MITRE ATT&CK IDs: [T0840], [T1003], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Discovery | T1049 | System Network Connections Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055 | Process Injection | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055.001 | Dynamic-link Library Injection | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--turla--c3043639afceaf63` |
| Collection, Credential Access | T1056.001 | Keylogging | ocessing layer, can and do remain entirely agnostic to the transport layer as long as it implements 4 MITRE ATT&CK IDs: [T0840], [T1003], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Discovery | T1057 | Process Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059 | Command and Scripting Interpreter | ge; by Juan Andres Guerrero- Saade (GReAT), Costin Raiu (GReAT), Daniel Moore (King’s College London), Thomas Rid (King’s College London). April 2017. T1105 T1059 T1205 T1024 T1032 T1158 T1222 T1094 8% 8% 25% 17% 42% EXECUTION LATERAL MOVEMENT PERSISTENCE COMMAND AND CONTROL DEFENCE EVASION TACTICS MITRE ATT&CK TTPs |  |  | 不明 | 不明 | 中 | `source--turla--f0c7ef1fbe87f2c6` |
| Execution | T1059.001 | PowerShell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--turla--c3043639afceaf63` |
| Execution | T1059.003 | Windows Command Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.006 | Python | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.007 | JavaScript | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1068 | Exploitation for Privilege Escalation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1069.001 | Local Groups | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1069.002 | Domain Groups | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071 | Application Layer Protocol | m to distinguish Snake traffic from legitimate traffic destined for application software on the compromised server. This 18 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1071.003], [T1090.003], [T1095], [T1132], [T1572], [T1573] 19 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1132.002], [T1547.006], [T1584] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Command And Control | T1071.001 | Web Protocols | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--turla--c3043639afceaf63` |
| Command And Control | T1071.003 | Mail Protocols | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--turla--c3043639afceaf63` |
| Command And Control | T1071.004 | DNS | llowing structure. Only the low-order seven bits of the flags byte are used, and they have the following significance. 22 MITRE ATT&CK IDs: [T1001.003], [T1071.004], [T1132.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Collection | T1074 | Data Staged | r incoming and outgoing data. These keys were saved in the 0x2 Container in the 0x227 and 0x228 30 MITRE ATT&CK IDs: [T1001], [T1104] 31 MITRE ATT&CK IDs: [T1074], [T1119], [T1560.003] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | r, can and do remain entirely agnostic to the transport layer as long as it implements 4 MITRE ATT&CK IDs: [T0840], [T1003], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.003 | Local Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--turla--c3043639afceaf63` |
| Discovery | T1087.001 | Local Account | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090 | Proxy | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090.001 | Internal Proxy | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090.003 | Multi-hop Proxy | e traffic from legitimate traffic destined for application software on the compromised server. This 18 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1071.003], [T1090.003], [T1095], [T1132], [T1572], [T1573] 19 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1132.002], [T1547.006], [T1584] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Uncategorized | T1094 | MITRE ATT&CK T1094 | tin Raiu (GReAT), Daniel Moore (King’s College London), Thomas Rid (King’s College London). April 2017. T1105 T1059 T1205 T1024 T1032 T1158 T1222 T1094 8% 8% 25% 17% 42% EXECUTION LATERAL MOVEMENT PERSISTENCE COMMAND AND CONTROL DEFENCE EVASION TACTICS MITRE ATT&CK TTPs |  |  | 不明 | 不明 | 中 | `source--turla--f0c7ef1fbe87f2c6` |
| Command And Control | T1095 | Non-Application Layer Protocol | ], [T1003], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Command And Control | T1102 | Web Service | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102.002 | Bidirectional Communication | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1104 | Multi-Stage Channels | mmands/data for the host of the Snake infection. Commands will be queued in this Container until the implant is ready to execute them. 15MITRE ATT&CK IDs: [T1104] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--turla--f0c7ef1fbe87f2c6` |
| Execution | T1106 | Native API | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--turla--c3043639afceaf63` |
| Credential Access | T1110 | Brute Force | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--turla--c3043639afceaf63` |
| Collection | T1119 | Automated Collection | g and outgoing data. These keys were saved in the 0x2 Container in the 0x227 and 0x228 30 MITRE ATT&CK IDs: [T1001], [T1104] 31 MITRE ATT&CK IDs: [T1074], [T1119], [T1560.003] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Discovery | T1120 | Peripheral Device Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1124 | System Time Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1132 | Data Encoding | ate traffic destined for application software on the compromised server. This 18 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1071.003], [T1090.003], [T1095], [T1132], [T1572], [T1573] 19 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1132.002], [T1547.006], [T1584] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Command And Control | T1132.002 | Non-Standard Encoding | r. This 18 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1071.003], [T1090.003], [T1095], [T1132], [T1572], [T1573] 19 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1132.002], [T1547.006], [T1584] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Privilege Escalation, Stealth | T1134.002 | Create Process with Token | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1135 | Network Share Discovery | in entirely agnostic to the transport layer as long as it implements 4 MITRE ATT&CK IDs: [T0840], [T1003], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--turla--c3043639afceaf63` |
| Uncategorized | T1158 | MITRE ATT&CK T1158 | de (GReAT), Costin Raiu (GReAT), Daniel Moore (King’s College London), Thomas Rid (King’s College London). April 2017. T1105 T1059 T1205 T1024 T1032 T1158 T1222 T1094 8% 8% 25% 17% 42% EXECUTION LATERAL MOVEMENT PERSISTENCE COMMAND AND CONTROL DEFENCE EVASION TACTICS MITRE ATT&CK TTPs |  |  | 不明 | 不明 | 中 | `source--turla--f0c7ef1fbe87f2c6` |
| Initial Access | T1189 | Drive-by Compromise | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | layer as long as it implements 4 MITRE ATT&CK IDs: [T0840], [T1003], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Discovery | T1201 | Password Policy Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control, Persistence, Stealth | T1205 | Traffic Signaling | uan Andres Guerrero- Saade (GReAT), Costin Raiu (GReAT), Daniel Moore (King’s College London), Thomas Rid (King’s College London). April 2017. T1105 T1059 T1205 T1024 T1032 T1158 T1222 T1094 8% 8% 25% 17% 42% EXECUTION LATERAL MOVEMENT PERSISTENCE COMMAND AND CONTROL DEFENCE EVASION TACTICS MITRE ATT&CK TTPs |  |  | 不明 | 不明 | 中 | `source--turla--f0c7ef1fbe87f2c6` |
| Collection | T1213.006 | Databases | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1222 | File and Directory Permissions Modification | T), Costin Raiu (GReAT), Daniel Moore (King’s College London), Thomas Rid (King’s College London). April 2017. T1105 T1059 T1205 T1024 T1032 T1158 T1222 T1094 8% 8% 25% 17% 42% EXECUTION LATERAL MOVEMENT PERSISTENCE COMMAND AND CONTROL DEFENCE EVASION TACTICS MITRE ATT&CK TTPs |  |  | 不明 | 不明 | 中 | `source--turla--f0c7ef1fbe87f2c6` |
| Discovery | T1482 | Domain Trust Discovery | ly agnostic to the transport layer as long as it implements 4 MITRE ATT&CK IDs: [T0840], [T1003], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Discovery | T1518.001 | Security Software Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1546.003 | Windows Management Instrumentation Event Subscription | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1546.013 | PowerShell Profile | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1546.016 | Installer Packages | er on a host. The first was as a JPEG viewer; later options included disguising the installer as Notepad++ or 7zip. 8 MITRE ATT&CK IDs: [T1027.002], [T1140], [T1546.016], [T1588], [T1610] 9 MITRE ATT&CK IDs: [T1573.001], [T1573.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.004 | Winlogon Helper DLL | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.006 | Kernel Modules and Extensions | ], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Defense Impairment | T1553.006 | Code Signing Policy Modification | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.004 | Windows Credential Manager | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1559 | Inter-Process Communication | x229 (a CAST-128 key). This key will be used to encrypt and decrypt all of the embedded files and modules within the 0x3 Container. 16 MITRE ATT&CK IDs: [T1559] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Collection | T1560.001 | Archive via Utility | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.003 | Archive via Custom Method | going data. These keys were saved in the 0x2 Container in the 0x227 and 0x228 30 MITRE ATT&CK IDs: [T1001], [T1104] 31 MITRE ATT&CK IDs: [T1074], [T1119], [T1560.003] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Stealth | T1564 | Hide Artifacts | components and loading them into memory.11 10 MITRE ATT&CK IDs: [T1014], [T1027], [T1547.006], [T1610] 11 MITRE ATT&CK IDs: [T1027], [T1036], [T1140], [T1564], [T1569.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Stealth | T1564.012 | File/Path Exclusions | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1569.002 | Service Execution | ts and loading them into memory.11 10 MITRE ATT&CK IDs: [T1014], [T1027], [T1547.006], [T1610] 11 MITRE ATT&CK IDs: [T1027], [T1036], [T1140], [T1564], [T1569.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Lateral Movement | T1570 | Lateral Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--turla--c3043639afceaf63` |
| Command And Control | T1572 | Protocol Tunneling | ic destined for application software on the compromised server. This 18 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1071.003], [T1090.003], [T1095], [T1132], [T1572], [T1573] 19 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1132.002], [T1547.006], [T1584] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Command And Control | T1573 | Encrypted Channel | ed for application software on the compromised server. This 18 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1071.003], [T1090.003], [T1095], [T1132], [T1572], [T1573] 19 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1132.002], [T1547.006], [T1584] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Command And Control | T1573.001 | Symmetric Cryptography | options included disguising the installer as Notepad++ or 7zip. 8 MITRE ATT&CK IDs: [T1027.002], [T1140], [T1546.016], [T1588], [T1610] 9 MITRE ATT&CK IDs: [T1573.001], [T1573.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Command And Control | T1573.002 | Asymmetric Cryptography | uded disguising the installer as Notepad++ or 7zip. 8 MITRE ATT&CK IDs: [T1027.002], [T1140], [T1546.016], [T1588], [T1610] 9 MITRE ATT&CK IDs: [T1573.001], [T1573.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Uncategorized | T1574.002 | MITRE ATT&CK T1574.002 | at are stored in the encrypted registry blob.13 12 MITRE ATT&CK IDs: [T1106], [T1112], [T1547.006] 13 MITRE ATT&CK IDs: [T1027], [T1547.006], [T1569.002], [T1574.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Resource Development | T1583.006 | Web Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584 | Compromise Infrastructure | IDs: [T1001.003], [T1071], [T1071.003], [T1090.003], [T1095], [T1132], [T1572], [T1573] 19 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1132.002], [T1547.006], [T1584] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Resource Development | T1584.003 | Virtual Private Server | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.004 | Server | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.006 | Web Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--turla--c3043639afceaf63` |
| Resource Development | T1588 | Obtain Capabilities | The first was as a JPEG viewer; later options included disguising the installer as Notepad++ or 7zip. 8 MITRE ATT&CK IDs: [T1027.002], [T1140], [T1546.016], [T1588], [T1610] 9 MITRE ATT&CK IDs: [T1573.001], [T1573.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Resource Development | T1588.001 | Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608 | Stage Capabilities | 4 MITRE ATT&CK IDs: [T0840], [T1003], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Execution | T1610 | Deploy Container | t was as a JPEG viewer; later options included disguising the installer as Notepad++ or 7zip. 8 MITRE ATT&CK IDs: [T1027.002], [T1140], [T1546.016], [T1588], [T1610] 9 MITRE ATT&CK IDs: [T1573.001], [T1573.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Discovery | T1615 | Group Policy Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 139件
- IOC観測: 184件
- 複数攻撃で観測: 0件
- 要レビュー候補: 70件
- 非IOC artifact観測: 84件（`artifacts.csv`）

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
| source--turla--3d5a4d35095a89d3 | README |  | 不明 | Turla/2014/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--turla--381349fb0cea34f0 | Penquins Moonlit Maze AppendixB |  | 不明 | Turla/2017/Penquins_Moonlit_Maze_AppendixB.pdf | report | TLP:CLEAR | 中 |
| source--turla--9c3fb3485b0c32a0 | Penquins Moonlit Maze PDF eng |  | 不明 | Turla/2017/Penquins_Moonlit_Maze_PDF_eng.pdf | report | TLP:CLEAR | 中 |
| source--turla--e6c93c546a97e314 | README |  | 不明 | Turla/2017/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--turla--6e90d1ef9571f3b1 | IOC |  | 不明 | Turla/IOC.TXT | text-data | TLP:CLEAR | 中 |
| source--turla--f0c7ef1fbe87f2c6 | Malware Technical Insight  Turla “Penquin x64” |  | 不明 | Turla/Malware Technical Insight _Turla “Penquin_x64”.pdf | report | TLP:CLEAR | 中 |
| source--turla--c3043639afceaf63 | aa23 129a snake malware 2 |  | 不明 | Turla/aa23-129a_snake_malware_2.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
