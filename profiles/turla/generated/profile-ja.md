# Turla 脅威アクタープロファイル

- プロファイルID: `actor--turla`
- 状態: draft
- 更新日時: 2026-08-10T07:28:35Z
- 構造バージョン: 1.2.0

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
| malware--carbon | Carbon | [Carbon](https://attack.mitre.org/software/S0335) is a sophisticated, second-stage backdoor and framework that can be used to steal sensitive information from victims. [Carbon](https://attack.mitre.org/software/S0335) has been selectively used by [Turla](https://attack.mitre.org/groups/G0010) to target government and foreign affairs-related organizations in Central Asia.(Citation: ESET Carbon Mar 2017)(Citation: Securelist Turla Oct 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--comrat | ComRAT | [ComRAT](https://attack.mitre.org/software/S0126) is a second stage implant suspected of being a descendant of [Agent.btz](https://attack.mitre.org/software/S0092) and used by [Turla](https://attack.mitre.org/groups/G0010). The first version of [ComRAT](https://attack.mitre.org/software/S0126) was identified in 2007, but the tool has undergone substantial development for many years since.(Citation: Symantec Waterbug)(Citation: NorthSec 2015 GData Uroburos Tools)(Citation: ESET ComRAT May 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--crutch | Crutch | [Crutch](https://attack.mitre.org/software/S0538) is a backdoor designed for document theft that has been used by [Turla](https://attack.mitre.org/groups/G0010) since at least 2015.(Citation: ESET Crutch December 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--diamondback | DIAMONDBACK | GTIGがTurlaの独自ツールキットとしてSTOCKSTAY・KAZUARと併記している。 | 不明 | 不明 | 中 | `source--gtig-stockstay-turla-2026` |
| malware--epic | Epic | [Epic](https://attack.mitre.org/software/S0091) is a backdoor that has been used by [Turla](https://attack.mitre.org/groups/G0010). (Citation: Kaspersky Turla) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--gazer | Gazer | [Gazer](https://attack.mitre.org/software/S0168) is a backdoor used by [Turla](https://attack.mitre.org/groups/G0010) since at least 2016. (Citation: ESET Gazer Aug 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--hyperstack | HyperStack | [HyperStack](https://attack.mitre.org/software/S0537) is a RPC-based backdoor used by [Turla](https://attack.mitre.org/groups/G0010) since at least 2018. [HyperStack](https://attack.mitre.org/software/S0537) has similarities to other backdoors used by [Turla](https://attack.mitre.org/groups/G0010) including [Carbon](https://attack.mitre.org/software/S0335).(Citation: Accenture HyperStack October 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--kazuar | Kazuar | [Kazuar](https://attack.mitre.org/software/S0265) is a fully featured, multi-platform backdoor Trojan written using the Microsoft .NET framework. (Citation: Unit 42 Kazuar May 2017) | 不明 | 不明 | 高 | `source--daily-0e103138b331cf8b266a`, `source--mitre-attack-19-1` |
| malware--kopiluwak | KOPILUWAK | [KOPILUWAK](https://attack.mitre.org/software/S1075) is a JavaScript-based reconnaissance tool that has been used for victim profiling and C2 since at least 2017.(Citation: Mandiant Suspected Turla Campaign February 2023) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--lightneuron | LightNeuron | [LightNeuron](https://attack.mitre.org/software/S0395) is a sophisticated backdoor that has targeted Microsoft Exchange servers since at least 2014. [LightNeuron](https://attack.mitre.org/software/S0395) has been used by [Turla](https://attack.mitre.org/groups/G0010) to target diplomatic and foreign affairs-related organizations. The presence of certain strings in the malware suggests a Linux variant of [LightNeuron](https://attack.mitre.org/software/S0395) exists.(Citation: ESET LightNeuron May 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--lunarloader | LunarLoader | [LunarLoader](https://attack.mitre.org/software/S1143) is the loader component for the [LunarWeb](https://attack.mitre.org/software/S1141) and [LunarMail](https://attack.mitre.org/software/S1142) backdoors that has been used by [Turla](https://attack.mitre.org/groups/G0010) since at least 2020 including against a European ministry of foreign affairs (MFA). [LunarLoader](https://attack.mitre.org/software/S1143) has been observed as a standalone and as a part of trojanized open-source software such as AdmPwd.(Citation: ESET Turla Lunar toolset May 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--lunarmail | LunarMail | [LunarMail](https://attack.mitre.org/software/S1142) is a backdoor that has been used by [Turla](https://attack.mitre.org/groups/G0010) since at least 2020 including in a compromise of a European ministry of foreign affairs (MFA) in conjunction with [LunarLoader](https://attack.mitre.org/software/S1143) and [LunarWeb](https://attack.mitre.org/software/S1141). [LunarMail](https://attack.mitre.org/software/S1142) is designed to be deployed on workstations and can use email messages and [Steganography](https://attack.mitre.org/techniques/T1001/002) in command and control.(Citation: ESET Turla Lunar toolset May 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--lunarweb | LunarWeb | [LunarWeb](https://attack.mitre.org/software/S1141) is a backdoor that has been used by [Turla](https://attack.mitre.org/groups/G0010) since at least 2020 including in a compromise of a European ministry of foreign affairs (MFA) together with [LunarLoader](https://attack.mitre.org/software/S1143) and [LunarMail](https://attack.mitre.org/software/S1142). [LunarWeb](https://attack.mitre.org/software/S1141) has only been observed deployed against servers and can use [Steganography](https://attack.mitre.org/techniques/T1001/002) to obfuscate command and control.(Citation: ESET Turla Lunar toolset May 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--mosquito | Mosquito | [Mosquito](https://attack.mitre.org/software/S0256) is a Win32 backdoor that has been used by [Turla](https://attack.mitre.org/groups/G0010). [Mosquito](https://attack.mitre.org/software/S0256) is made up of three parts: the installer, the launcher, and the backdoor. The main backdoor is called CommanderDLL and is launched by the loader program. (Citation: ESET Turla Mosquito Jan 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--penquin | Penquin | [Penquin](https://attack.mitre.org/software/S0587) is a remote access trojan (RAT) with multiple versions used by [Turla](https://attack.mitre.org/groups/G0010) to target Linux systems since at least 2014.(Citation: Kaspersky Turla Penquin December 2014)(Citation: Leonardo Turla Penquin May 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--powerstallion | PowerStallion | [PowerStallion](https://attack.mitre.org/software/S0393) is a lightweight [PowerShell](https://attack.mitre.org/techniques/T1059/001) backdoor used by [Turla](https://attack.mitre.org/groups/G0010), possibly as a recovery access tool to install other backdoors.(Citation: ESET Turla PowerShell May 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--stockstay | STOCKSTAY | Turlaが継続的に開発・展開する多コンポーネント構成の.NETバックドア。STOCKBROKERがWebSocketトンネラーおよびプロキシ対応通信を、STOCKMARKETがオーケストレーターと設定管理を、STOCKTRADERがコマンド実行を伴うバックドア機能を担う。MARKETMAKERはダウンローダーコンポーネントである。 | 2022-12 | 2025-11 | 高 | `source--gtig-stockstay-turla-2026` |
| malware--tinyturla | TinyTurla | [TinyTurla](https://attack.mitre.org/software/S0668) is a backdoor that has been used by [Turla](https://attack.mitre.org/groups/G0010) against targets in the US, Germany, and Afghanistan since at least 2020.(Citation: Talos TinyTurla September 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--uroburos | Uroburos | [Uroburos](https://attack.mitre.org/software/S0022) is a sophisticated cyber espionage tool written in C that has been used by units within Russia's Federal Security Service (FSB) associated with the [Turla](https://attack.mitre.org/groups/G0010) toolset to collect intelligence on sensitive targets worldwide. [Uroburos](https://attack.mitre.org/software/S0022) has several variants and has undergone nearly constant upgrade since its initial development in 2003 to keep it viable after public disclosures. [Uroburos](https://attack.mitre.org/software/S0022) is typically deployed to external-facing nodes on a targeted network and has the ability to leverage additional tools and TTPs to further exploit an internal network. [Uroburos](https://attack.mitre.org/software/S0022) has interoperable implants for Windows, Linux, and macOS, employs a high level of stealth in communications and architecture, and can easily incorporate new or replacement components.(Citation: Joint Cybersecurity Advisory AA23-129A Snake Malware May 2023)(Citation: Kaspersky Turla) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--wildday | WILDDAY | GTIGがTurlaの独自ツールキットとしてSTOCKSTAY・KAZUARと併記している。 | 不明 | 不明 | 中 | `source--gtig-stockstay-turla-2026` |

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

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| vuln--cve-2025-8088 | CVE-2025-8088 | WinRARのパストラバーサル脆弱性。STOCKSTAY展開の一環として悪用された。 | 不明 | 不明 | 中 | `source--gtig-stockstay-turla-2026` |

### 運用能力

未確認

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ロシアのハッカー、Kazuarバックドアをモジュール型P2Pボットネットへ進化 | infrastructure-operation | 不明 | 不明 | 2026-05-18 |  | malware--kazuar | ttp--activity-rule--23f91b330aff86b4e245, ttp--activity-rule--a065ec3abbf8e6d486d8 | victim--activity-rule--5d49c32b8b1bf735cbd0 | ロシア系ハッカー集団Secret Blizzardは、Kazuarバックドアを長期潜伏・隠密性・情報収集向けのP2Pボットネットへ発展させた。 Microsoftの分析では、新しいKazuarはKernel、Bridge、Workerの3モジュールで構成され、感染環境内で役割を分担する。 Kernelはリーダーを選出し、非リーダー端末をサイレント化することで、C2との外部通信を減らして検知面を縮小する。 Workerはキー入力記録、スクリーンショット、ファイル収集、偵察、メール/MAPIデータ収集、最近使ったファイル窃取などを行う。 Kazuarは150種類の設定項目を持ち、AMSI、ETW、WLDPのバイパスなど多様な回避機能も備えている。 | 高 | `source--daily-0e103138b331cf8b266a` |
| ロシアのTurlaハッカー、パキスタンのAPTサーバーを乗っ取りサイバースパイ活動を展開 | cyber-espionage | 不明 | 不明 | 2024-12-05 | target--activity-rule--country--48cc6b4cc2919459aec9, target--activity-rule--country--72caf60a2fbce4a1be7a, target--mitre-group--sector--8b0d895cbce29b8afc51 | malware--tinyturla |  | victim--activity-rule--fd84357d12102a31bedc | ロシアの国家支援グループTurlaが、パキスタンのAPT「Storm-0156」のインフラを乗っ取り、スパイ活動を実行。 Turlaは、Storm-0156の脅威アクターの既存のC2サーバーを利用し、Storm-0156が侵害していたアフガニスタンやインド政府機関を対象に攻撃を展開。 攻撃には、TinyTurlaバックドア、TwoDashバックドア、MiniPocketダウンローダーなどが使用された。 Storm-0156のマルウェアツール(CrimsonRATマルウェアとWainscotなど)や盗まれた認証情報も収集されていた。 Turlaは外国の標的からのデータの傍受、解読、収集を担当するロシア連邦保安庁（FSB）のCenter 16とつながりのある、ロシア国家が支援するハッキンググループ。高度なサイバー攻撃に長い歴史を持ち、世界中の政府や組織を標的にしている。 | 高 | `source--daily-7b8d62bd6d4144728793` |
| ロシアのサイバースパイ、他のハッカーの背後に隠れてウクライナを標的に | cyber-espionage | 2024-03 | 2024-04 | 2024-12-12 | target--activity-rule--country--36f1b9323d5faab92f39, target--activity-rule--country--72caf60a2fbce4a1be7a, target--mitre-group--sector--227d97728274c9a45564 | malware--epic |  | victim--activity-rule--9899cfc7ca4bd10c1940 | ロシアのサイバー諜報グループ「Turla」（別名「Secret Blizzard」）は、他の脅威アクターのインフラを利用してウクライナの軍事デバイスを標的にしている。 MicrosoftとLumenの報告によれば、Turlaはパキスタンの脅威アクター「Storm-0156」のマルウェアとサーバーをハイジャックして使用している。 2024年3月から4月にかけて、TurlaはAmadeyボットネットや他のロシアのハッキンググループ「Storm-1837」のインフラを利用して、ウクライナのシステムに独自のマルウェア「Tavdig」や「KazuarV2」を展開した。 Microsoftは、TurlaがAmadeyのマルウェア・アズ・ア・サービス（MaaS）を使用したのか、またはAmadeyのコマンド・アンド・コントロール（C2）パネルに密かにアクセスしたのかは不明としている。 この手法は、Turlaが他のハッカーグループの背後に隠れて活動する一例である。 | 中 | `source--daily-785ae8d632612c179b8d` |
| STOCKSTAYバックドアによるウクライナ・イタリア関連組織への諜報活動 | cyber-espionage | 2022-12 | 2025-11 | 2026-06-25 | target--activity-rule--country--36f1b9323d5faab92f39, target--mitre-group--sector--8b0d895cbce29b8afc51 | malware--stockstay, malware--kazuar, malware--wildday, malware--diamondback | ttp--turla-stockstay-t1090-proxy, ttp--turla-stockstay-t1203-winrar, ttp--turla-stockstay-t1566-001, ttp--turla-stockstay-t1572-websocket | victim--activity-rule--48105cd9cb10230243b9, victim--turla-stockstay-ukraine-italy | Google Threat Intelligence Groupは、Turlaが多コンポーネント構成の.NETバックドアSTOCKSTAYを継続的に開発・展開し、政府、軍、外交関連組織への諜報活動に使用していると報告した。ウクライナの政府・軍組織を継続的に標的とし、2024年2月にはイタリアの外交・対外政策関連組織も標的とした。侵入には悪性RDPファイルを用いたフィッシングと侵害済みインフラを使用し、CVE-2025-8088(WinRARのパストラバーサル)も悪用している。STOCKSTAYはKAZUAR、WILDDAY、DIAMONDBACKなど他の独自ツールキットと併用される。最も古い開発痕跡は2022年12月まで遡り、2023年9月には初期版がVirusTotalへ投稿された。2024年1月にウクライナのネットワーク侵害、2025年3月から11月にかけてフィッシングと展開が継続して観測されている。 | 高 | `source--gtig-stockstay-turla-2026` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| ロシアのハッカー、Kazuarバックドアをモジュール型P2Pボットネットへ進化 | Turla | Kazuar | T1083 File and Directory Discovery, T1113 Screen Capture | 情報なし | 情報なし | 被害事例: ロシアのハッカー、Kazuarバックドアをモジュール型P2Pボットネットへ進化 | 高 |
| ロシアのTurlaハッカー、パキスタンのAPTサーバーを乗っ取りサイバースパイ活動を展開 | Turla | TinyTurla | 情報なし | 情報なし | インド, ロシア, 政府・行政 | 被害事例: ロシアのTurlaハッカー、パキスタンのAPTサーバーを乗っ取りサイバースパイ活動を展開 | 高 |
| ロシアのサイバースパイ、他のハッカーの背後に隠れてウクライナを標的に | Turla | Epic | 情報なし | 情報なし | ウクライナ, ロシア, 防衛・軍事 | 被害事例: ロシアのサイバースパイ、他のハッカーの背後に隠れてウクライナを標的に | 中 |
| STOCKSTAYバックドアによるウクライナ・イタリア関連組織への諜報活動 | Turla | DIAMONDBACK, Kazuar, STOCKSTAY, WILDDAY | T1090 Proxy, T1203 Exploitation for Client Execution, T1566.001 Spearphishing Attachment, T1572 Protocol Tunneling | 情報なし | ウクライナ, 政府・行政 | 被害事例: STOCKSTAYバックドアによるウクライナ・イタリア関連組織への諜報活動, ウクライナの政府・軍組織およびイタリアの外交関連組織(集約) | 高 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アゼルバイジャン | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてアゼルバイジャンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | アフガニスタン | 活動「ロシアのTurlaハッカー、パキスタンのAPTサーバーを乗っ取りサイバースパイ活動を展開」の記述で標的・被害国として明示されている。 | 不明 | 不明 | 中 | `source--daily-7b8d62bd6d4144728793`, `source--target-audit-etda-threat-group-cards` |
| countries | アルジェリア | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてアルジェリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | アルメニア | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてアルメニアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イエメン | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてイエメンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イタリア | 活動「STOCKSTAYバックドアによるウクライナ・イタリア関連組織への諜報活動」の記述で標的・被害国として明示されている。 | 2022-12 | 2025-11 | 中 | `source--gtig-stockstay-turla-2026`, `source--target-audit-etda-threat-group-cards` |
| countries | イラク | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてイラクが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | イラン | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてイランが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | インド | 活動「ロシアのTurlaハッカー、パキスタンのAPTサーバーを乗っ取りサイバースパイ活動を展開」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-7b8d62bd6d4144728793`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | インドネシア | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてインドネシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ウクライナ | 活動「ロシアのサイバースパイ、他のハッカーの背後に隠れてウクライナを標的に」の記述で標的として明示された国・地域。 | 2022-12 | 2025-11 | 中 | `source--daily-785ae8d632612c179b8d`, `source--gtig-stockstay-turla-2026`, `source--target-audit-etda-threat-group-cards` |
| countries | ウズベキスタン | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてウズベキスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ウルグアイ | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてウルグアイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | エクアドル | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてエクアドルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | エストニア | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてエストニアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オランダ | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてオランダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | オーストラリア | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてオーストラリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オーストリア | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてオーストリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | カザフスタン | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてカザフスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | カタール | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてカタールが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | キルギス | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてキルギスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | クウェート | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてクウェートが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | サウジアラビア | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてサウジアラビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | シリア | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてシリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ジャマイカ | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてジャマイカが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ジョージア | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてジョージアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | スイス | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてスイスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | スウェーデン | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてスウェーデンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | スペイン | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてスペインが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | セルビア | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてセルビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | タイ | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてタイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | タジキスタン | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてタジキスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | チュニジア | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてチュニジアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | チリ | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてチリが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | デンマーク | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてデンマークが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | トルクメニスタン | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてトルクメニスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ドイツ | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてドイツが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ハンガリー | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてハンガリーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | パキスタン | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてパキスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | パラグアイ | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてパラグアイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フィンランド | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてフィンランドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フランス | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてフランスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ブラジル | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてブラジルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベトナム | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてベトナムが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベネズエラ | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてベネズエラが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベラルーシ | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてベラルーシが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ベルギー | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてベルギーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ボツワナ | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてボツワナが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ボリビア | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてボリビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ポーランド | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてポーランドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | メキシコ | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてメキシコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ヨルダン | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてヨルダンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ラトビア | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてラトビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ルーマニア | 構造化OSINTの被害国フィールドでTurlaの標的・被害国としてルーマニアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ロシア | 活動「ロシアのTurlaハッカー、パキスタンのAPTサーバーを乗っ取りサイバースパイ活動を展開」の記述で標的として明示された国・地域。 | 2024-03 | 2024-04 | 中 | `source--daily-785ae8d632612c179b8d`, `source--daily-7b8d62bd6d4144728793`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 中国 | 構造化OSINTの被害国フィールドでTurlaの標的・被害国として中国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 南アフリカ | 構造化OSINTの被害国フィールドでTurlaの標的・被害国として南アフリカが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | 構造化OSINTの被害国フィールドでTurlaの標的・被害国として米国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 英国 | 構造化OSINTの被害国フィールドでTurlaの標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 香港 | 構造化OSINTの被害国フィールドでTurlaの標的・被害国として香港が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | アフリカ | アルジェリア、チュニジア、ボツワナ、南アフリカで確認された標的・被害事例をアフリカとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | コーカサス | アゼルバイジャン、アルメニア、ジョージアで確認された標的・被害事例をコーカサスとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 中南米 | ウルグアイ、エクアドル、ジャマイカ、チリ、パラグアイ、ブラジル、ベネズエラ、ボリビア、メキシコで確認された標的・被害事例を中南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 中央アジア | ウズベキスタン、カザフスタン、キルギス、タジキスタン、トルクメニスタンで確認された標的・被害事例を中央アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 中東 | イエメン、イラク、イラン、カタール、クウェート、サウジアラビア、シリア、ヨルダンで確認された標的・被害事例を中東として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 北アフリカ | アルジェリア、チュニジアで確認された標的・被害事例を北アフリカとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 北米 | メキシコ、米国で確認された標的・被害事例を北米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 南アジア | アフガニスタン、インド、パキスタンで確認された標的・被害事例を南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-7b8d62bd6d4144728793`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 南欧 | イタリア、スペイン、セルビアで確認された標的・被害事例を南欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--gtig-stockstay-turla-2026`, `source--target-audit-etda-threat-group-cards` |
| regions | 南米 | ウルグアイ、エクアドル、チリ、パラグアイ、ブラジル、ベネズエラ、ボリビアで確認された標的・被害事例を南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東アジア | 中国、香港で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東南アジア | インドネシア、タイ、ベトナムで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東欧 | ウクライナ、ハンガリー、ベラルーシ、ポーランド、ルーマニア、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-785ae8d632612c179b8d`, `source--daily-7b8d62bd6d4144728793`, `source--gtig-stockstay-turla-2026`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 欧州 | イタリア、ウクライナ、エストニア、オランダ、オーストリア、スイス、スウェーデン、スペイン、セルビア、デンマーク、ドイツ、ハンガリー、フィンランド、フランス、ベラルーシ、ベルギー、ポーランド、ラトビア、ルーマニア、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-785ae8d632612c179b8d`, `source--gtig-stockstay-turla-2026`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| sectors | 防衛・軍事 | They have compromised victims in over 50 countries since at least 2004, spanning a range of industries including government, embassies, military, education, research and pharmaceutical companies. | 2024-03 | 2024-04 | 高 | `source--daily-785ae8d632612c179b8d`, `source--mitre-attack-19-1` |
| sectors | 教育・研究 | They have compromised victims in over 50 countries since at least 2004, spanning a range of industries including government, embassies, military, education, research and pharmaceutical companies. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 政府・行政 | They have compromised victims in over 50 countries since at least 2004, spanning a range of industries including government, embassies, military, education, research and pharmaceutical companies. | 2022-12 | 2025-11 | 高 | `source--daily-7b8d62bd6d4144728793`, `source--gtig-stockstay-turla-2026`, `source--mitre-attack-19-1` |
| sectors | 医療・ヘルスケア | They have compromised victims in over 50 countries since at least 2004, spanning a range of industries including government, embassies, military, education, research and pharmaceutical companies. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: STOCKSTAYバックドアによるウクライナ・イタリア関連組織への諜報活動 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--36f1b9323d5faab92f39, target--mitre-group--sector--8b0d895cbce29b8afc51 | malware--diamondback, malware--kazuar, malware--stockstay, malware--wildday | ttp--turla-stockstay-t1090-proxy, ttp--turla-stockstay-t1203-winrar, ttp--turla-stockstay-t1566-001, ttp--turla-stockstay-t1572-websocket |  |  | 2022-12 | 2025-11 | 2026-06-25 | 高 | `source--gtig-stockstay-turla-2026` |
| 被害事例: ロシアのハッカー、Kazuarバックドアをモジュール型P2Pボットネットへ進化 | 非公開 | anonymous | unknown | reported |  | malware--kazuar | ttp--activity-rule--23f91b330aff86b4e245, ttp--activity-rule--a065ec3abbf8e6d486d8 | メール／メールアカウント, エンドポイント | data-theft: Workerはキー入力記録、スクリーンショット、ファイル収集、偵察、メール/MAPIデータ収集、最近使ったファイル窃取などを行う。<br>espionage: ロシア系ハッカー集団Secret Blizzardは、Kazuarバックドアを長期潜伏・隠密性・情報収集向けのP2Pボットネットへ発展させた。 | 不明 | 不明 | 2026-05-18 | 高 | `source--daily-0e103138b331cf8b266a` |
| 被害事例: ロシアのサイバースパイ、他のハッカーの背後に隠れてウクライナを標的に | 非公開 | anonymous | unknown | reported | target--activity-rule--country--36f1b9323d5faab92f39, target--activity-rule--country--72caf60a2fbce4a1be7a, target--mitre-group--sector--227d97728274c9a45564 | malware--epic |  | サーバー | espionage: ロシアのサイバー諜報グループ「Turla」（別名「Secret Blizzard」）は、他の脅威アクターのインフラを利用してウクライナの軍事デバイスを標的にしている。 | 2024-03 | 2024-04 | 2024-12-12 | 中 | `source--daily-785ae8d632612c179b8d` |
| 被害事例: ロシアのTurlaハッカー、パキスタンのAPTサーバーを乗っ取りサイバースパイ活動を展開 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--48cc6b4cc2919459aec9, target--activity-rule--country--72caf60a2fbce4a1be7a, target--mitre-group--sector--8b0d895cbce29b8afc51 | malware--tinyturla |  | サーバー | espionage: ロシアのTurlaハッカー、パキスタンのAPTサーバーを乗っ取りサイバースパイ活動を展開 | 不明 | 不明 | 2024-12-05 | 高 | `source--daily-7b8d62bd6d4144728793` |
| ウクライナの政府・軍組織およびイタリアの外交関連組織(集約) | 非公開 | aggregate | multiple-organizations | reported |  | malware--stockstay | ttp--turla-stockstay-t1566-001, ttp--turla-stockstay-t1203-winrar, ttp--turla-stockstay-t1572-websocket, ttp--turla-stockstay-t1090-proxy | Windows端末, 政府・軍ネットワーク | espionage: 情報収集を目的とした継続的なアクセス。<br>data-theft: STOCKSTAYによるコマンド実行とデータ取得。 | 2022-12 | 2025-11 | 2026-06-25 | 高 | `source--gtig-stockstay-turla-2026` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Discovery | T1083 | File and Directory Discovery | Workerはキー入力記録、スクリーンショット、ファイル収集、偵察、メール/MAPIデータ収集、最近使ったファイル窃取などを行う。 |  | activity--daily-6c5ab84f7ce816df64d9 | 不明 | 不明 | 中 | `source--daily-0e103138b331cf8b266a` |
| Collection | T1113 | Screen Capture | Workerはキー入力記録、スクリーンショット、ファイル収集、偵察、メール/MAPIデータ収集、最近使ったファイル窃取などを行う。 |  | activity--daily-6c5ab84f7ce816df64d9 | 不明 | 不明 | 中 | `source--daily-0e103138b331cf8b266a` |
| Uncategorized | T0840 | MITRE ATT&CK T0840 | ion layer to the distant command processing layer, can and do remain entirely agnostic to the transport layer as long as it implements 4 MITRE ATT&CK IDs: [T0840], [T1003], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Command And Control | T1001 | Data Obfuscation | 128 encrypted using a different key for incoming and outgoing data. These keys were saved in the 0x2 Container in the 0x227 and 0x228 30 MITRE ATT&CK IDs: [T1001], [T1104] 31 MITRE ATT&CK IDs: [T1074], [T1119], [T1560.003] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Command And Control | T1001.003 | Protocol or Service Impersonation | tion mechanism to distinguish Snake traffic from legitimate traffic destined for application software on the compromised server. This 18 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1071.003], [T1090.003], [T1095], [T1132], [T1572], [T1573] 19 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1132.002], [T1547.006], [T1584] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Credential Access | T1003 | OS Credential Dumping | to the distant command processing layer, can and do remain entirely agnostic to the transport layer as long as it implements 4 MITRE ATT&CK IDs: [T0840], [T1003], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Collection | T1005 | Data from Local System | [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors can upload files from victim machines.(Citation: ESET Turla PowerShell May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1007 | System Service Discovery | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover running services and associated processes using the <code>tasklist /svc</code> command.(Citation: Kaspersky Turla) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1012 | Query Registry | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover information in the Windows Registry with the <code>reg query</code> command.(Citation: Kaspersky Turla) [Turla](https://attack.mitre.org/groups/G0010) has also retrieved PowerShell payloads hidden in Registry keys as well as checking keys associated with null session named pipes .(Citation: ESET Turla PowerShell May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1014 | Rootkit | %\WinSxS\ directory. Executing WerFault.exe will start the process of decrypting Snake’s components and loading them into memory.11 10 MITRE ATT&CK IDs: [T1014], [T1027], [T1547.006], [T1610] 11 MITRE ATT&CK IDs: [T1027], [T1036], [T1140], [T1564], [T1569.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Discovery | T1016 | System Network Configuration Discovery | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover network configuration details using the <code>arp -a</code>, <code>nbtstat -n</code>, <code>net config</code>, <code>ipconfig /all</code>, and <code>route</code> commands, as well as [NBTscan](https://attack.mitre.org/software/S0590).(Citation: Kaspersky Turla)(Citation: Symantec Waterbug Jun 2019)(Citation: ESET ComRAT May 2020) [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors have also retrieved registered RPC interface information from process memory.(Citation: ESET Turla PowerShell May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016.001 | Internet Connection Discovery | [Turla](https://attack.mitre.org/groups/G0010) has used <code>tracert</code> to check internet connectivity.(Citation: ESET ComRAT May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover remote systems on a local network using the <code>net view</code> and <code>net view /DOMAIN</code> commands. [Turla](https://attack.mitre.org/groups/G0010) has also used <code>net group "Domain Computers" /domain</code>, <code>net group "Domain Controllers" /domain</code>, and <code>net group "Exchange Servers" /domain</code> to enumerate domain computers, including the organization's DC and Exchange Server.(Citation: Kaspersky Turla)(Citation: ESET ComRAT May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | [Turla](https://attack.mitre.org/groups/G0010) used <code>net use</code> commands to connect to lateral systems within a network.(Citation: Kaspersky Turla) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1024 | MITRE ATT&CK T1024 | es Guerrero- Saade (GReAT), Costin Raiu (GReAT), Daniel Moore (King’s College London), Thomas Rid (King’s College London). April 2017. T1105 T1059 T1205 T1024 T1032 T1158 T1222 T1094 8% 8% 25% 17% 42% EXECUTION LATERAL MOVEMENT PERSISTENCE COMMAND AND CONTROL DEFENCE EVASION TACTICS MITRE ATT&CK TTPs |  |  | 不明 | 不明 | 中 | `source--turla--f0c7ef1fbe87f2c6` |
| Collection | T1025 | Data from Removable Media | [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors can collect files from USB thumb drives.(Citation: ESET Turla PowerShell May 2019)(Citation: Symantec Waterbug Jun 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027 | Obfuscated Files or Information | directory. Executing WerFault.exe will start the process of decrypting Snake’s components and loading them into memory.11 10 MITRE ATT&CK IDs: [T1014], [T1027], [T1547.006], [T1610] 11 MITRE ATT&CK IDs: [T1027], [T1036], [T1140], [T1564], [T1569.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Stealth | T1027.002 | Software Packing | isguising the installer on a host. The first was as a JPEG viewer; later options included disguising the installer as Notepad++ or 7zip. 8 MITRE ATT&CK IDs: [T1027.002], [T1140], [T1546.016], [T1588], [T1610] 9 MITRE ATT&CK IDs: [T1573.001], [T1573.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Stealth | T1027.005 | Indicator Removal from Tools | Based on comparison of [Gazer](https://attack.mitre.org/software/S0168) versions, [Turla](https://attack.mitre.org/groups/G0010) made an effort to obfuscate strings in the malware that could be used as IoCs, including the mutex name and named pipe.(Citation: ESET Gazer Aug 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.010 | Command Obfuscation | [Turla](https://attack.mitre.org/groups/G0010) has used encryption (including salted 3DES via [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Out-EncryptedScript.ps1</code>), random variable names, and base64 encoding to obfuscate PowerShell commands and payloads.(Citation: ESET Turla PowerShell May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.011 | Fileless Storage | [Turla](https://attack.mitre.org/groups/G0010) has used the Registry to store encrypted and encoded payloads.(Citation: ESET Turla PowerShell May 2019)(Citation: Symantec Waterbug Jun 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1032 | MITRE ATT&CK T1032 | ero- Saade (GReAT), Costin Raiu (GReAT), Daniel Moore (King’s College London), Thomas Rid (King’s College London). April 2017. T1105 T1059 T1205 T1024 T1032 T1158 T1222 T1094 8% 8% 25% 17% 42% EXECUTION LATERAL MOVEMENT PERSISTENCE COMMAND AND CONTROL DEFENCE EVASION TACTICS MITRE ATT&CK TTPs |  |  | 不明 | 不明 | 中 | `source--turla--f0c7ef1fbe87f2c6` |
| Stealth | T1036 | Masquerading | ecrypting Snake’s components and loading them into memory.11 10 MITRE ATT&CK IDs: [T1014], [T1027], [T1547.006], [T1610] 11 MITRE ATT&CK IDs: [T1027], [T1036], [T1140], [T1564], [T1569.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [Turla](https://attack.mitre.org/groups/G0010) has named components of [LunarWeb](https://attack.mitre.org/software/S1141) to mimic Zabbix agent logs.(Citation: ESET Turla Lunar toolset May 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access, Discovery | T1040 | Network Sniffing | istant command processing layer, can and do remain entirely agnostic to the transport layer as long as it implements 4 MITRE ATT&CK IDs: [T0840], [T1003], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Discovery | T1046 | Network Service Discovery | mmand processing layer, can and do remain entirely agnostic to the transport layer as long as it implements 4 MITRE ATT&CK IDs: [T0840], [T1003], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Discovery | T1049 | System Network Connections Discovery | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover active local network connections using the <code>netstat -an</code>, <code>net use</code>, <code>net file</code>, and <code>net session</code> commands.(Citation: Kaspersky Turla)(Citation: ESET ComRAT May 2020) [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors have also enumerated the IPv4 TCP connection table via the <code>GetTcpTable2</code> API call.(Citation: ESET Turla PowerShell May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055 | Process Injection | [Turla](https://attack.mitre.org/groups/G0010) has also used [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Invoke-ReflectivePEInjection.ps1</code> to reflectively load a PowerShell payload into a random process on the victim system.(Citation: ESET Turla PowerShell May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055.001 | Dynamic-link Library Injection | [Turla](https://attack.mitre.org/groups/G0010) has used Metasploit to perform reflective DLL injection in order to escalate privileges.(Citation: ESET Turla Mosquito May 2018)(Citation: Github Rapid7 Meterpreter Elevate) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--turla--c3043639afceaf63` |
| Collection, Credential Access | T1056.001 | Keylogging | ocessing layer, can and do remain entirely agnostic to the transport layer as long as it implements 4 MITRE ATT&CK IDs: [T0840], [T1003], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Discovery | T1057 | Process Discovery | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover running processes using the <code>tasklist /v</code> command.(Citation: Kaspersky Turla) [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors have also enumerated processes associated with specific open ports or named pipes.(Citation: ESET Turla PowerShell May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059 | Command and Scripting Interpreter | ge; by Juan Andres Guerrero- Saade (GReAT), Costin Raiu (GReAT), Daniel Moore (King’s College London), Thomas Rid (King’s College London). April 2017. T1105 T1059 T1205 T1024 T1032 T1158 T1222 T1094 8% 8% 25% 17% 42% EXECUTION LATERAL MOVEMENT PERSISTENCE COMMAND AND CONTROL DEFENCE EVASION TACTICS MITRE ATT&CK TTPs |  |  | 不明 | 不明 | 中 | `source--turla--f0c7ef1fbe87f2c6` |
| Execution | T1059.001 | PowerShell | [Turla](https://attack.mitre.org/groups/G0010) has used PowerShell to execute commands/scripts, in some cases via a custom executable or code from [Empire](https://attack.mitre.org/software/S0363)'s PSInject.(Citation: ESET Turla Mosquito May 2018)(Citation: ESET Turla PowerShell May 2019)(Citation: Symantec Waterbug Jun 2019) [Turla](https://attack.mitre.org/groups/G0010) has also used PowerShell scripts to load and execute malware in memory. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--turla--c3043639afceaf63` |
| Execution | T1059.003 | Windows Command Shell | [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors have used cmd.exe to execute commands.(Citation: ESET Turla PowerShell May 2019)(Citation: Symantec Waterbug Jun 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | [Turla](https://attack.mitre.org/groups/G0010) has used VBS scripts throughout its operations.(Citation: Symantec Waterbug Jun 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.006 | Python | [Turla](https://attack.mitre.org/groups/G0010) has used IronPython scripts as part of the [IronNetInjector](https://attack.mitre.org/software/S0581) toolchain to drop payloads.(Citation: Unit 42 IronNetInjector February 2021 ) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.007 | JavaScript | [Turla](https://attack.mitre.org/groups/G0010) has used various JavaScript-based backdoors.(Citation: ESET Turla Mosquito Jan 2018)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1068 | Exploitation for Privilege Escalation | [Turla](https://attack.mitre.org/groups/G0010) has exploited vulnerabilities in the VBoxDrv.sys driver to obtain kernel mode privileges.(Citation: Unit42 AcidBox June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1069.001 | Local Groups | [Turla](https://attack.mitre.org/groups/G0010) has used <code>net localgroup</code> and <code>net localgroup Administrators</code> to enumerate group information, including members of the local administrators group.(Citation: ESET ComRAT May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1069.002 | Domain Groups | [Turla](https://attack.mitre.org/groups/G0010) has used <code>net group "Domain Admins" /domain</code> to identify domain administrators.(Citation: ESET ComRAT May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071 | Application Layer Protocol | m to distinguish Snake traffic from legitimate traffic destined for application software on the compromised server. This 18 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1071.003], [T1090.003], [T1095], [T1132], [T1572], [T1573] 19 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1132.002], [T1547.006], [T1584] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Command And Control | T1071.001 | Web Protocols | [Turla](https://attack.mitre.org/groups/G0010) has used HTTP and HTTPS for C2 communications.(Citation: ESET Turla Mosquito Jan 2018)(Citation: ESET Turla Mosquito May 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--turla--c3043639afceaf63` |
| Command And Control | T1071.003 | Mail Protocols | [Turla](https://attack.mitre.org/groups/G0010) has used multiple backdoors which communicate with a C2 server via email attachments.(Citation: Crowdstrike GTR2020 Mar 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--turla--c3043639afceaf63` |
| Command And Control | T1071.004 | DNS | llowing structure. Only the low-order seven bits of the flags byte are used, and they have the following significance. 22 MITRE ATT&CK IDs: [T1001.003], [T1071.004], [T1132.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Collection | T1074 | Data Staged | r incoming and outgoing data. These keys were saved in the 0x2 Container in the 0x227 and 0x228 30 MITRE ATT&CK IDs: [T1001], [T1104] 31 MITRE ATT&CK IDs: [T1074], [T1119], [T1560.003] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | r, can and do remain entirely agnostic to the transport layer as long as it implements 4 MITRE ATT&CK IDs: [T0840], [T1003], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.003 | Local Accounts | [Turla](https://attack.mitre.org/groups/G0010) has abused local accounts that have the same password across the victim’s network.(Citation: ESET Crutch December 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover operating system configuration details using the <code>systeminfo</code> and <code>set</code> commands.(Citation: Kaspersky Turla)(Citation: ESET ComRAT May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover files in specific locations on the hard disk %TEMP% directory, the current user's desktop, the Program Files directory, and Recent.(Citation: Kaspersky Turla)(Citation: ESET ComRAT May 2020) [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors have also searched for files matching the <code>lPH*.dll</code> pattern.(Citation: ESET Turla PowerShell May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--turla--c3043639afceaf63` |
| Discovery | T1087.001 | Local Account | [Turla](https://attack.mitre.org/groups/G0010) has used <code>net user</code> to enumerate local accounts on the system.(Citation: ESET ComRAT May 2020)(Citation: ESET Crutch December 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | [Turla](https://attack.mitre.org/groups/G0010) has used <code>net user /domain</code> to enumerate domain accounts.(Citation: ESET ComRAT May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090 | Proxy | [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors have included local UPnP RPC proxies.(Citation: ESET Turla PowerShell May 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090.001 | Internal Proxy | [Turla](https://attack.mitre.org/groups/G0010) has compromised internal network systems to act as a proxy to forward traffic to C2.(Citation: Talos TinyTurla September 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090.003 | Multi-hop Proxy | e traffic from legitimate traffic destined for application software on the compromised server. This 18 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1071.003], [T1090.003], [T1095], [T1132], [T1572], [T1573] 19 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1132.002], [T1547.006], [T1584] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Uncategorized | T1094 | MITRE ATT&CK T1094 | tin Raiu (GReAT), Daniel Moore (King’s College London), Thomas Rid (King’s College London). April 2017. T1105 T1059 T1205 T1024 T1032 T1158 T1222 T1094 8% 8% 25% 17% 42% EXECUTION LATERAL MOVEMENT PERSISTENCE COMMAND AND CONTROL DEFENCE EVASION TACTICS MITRE ATT&CK TTPs |  |  | 不明 | 不明 | 中 | `source--turla--f0c7ef1fbe87f2c6` |
| Command And Control | T1095 | Non-Application Layer Protocol | ], [T1003], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Command And Control | T1102 | Web Service | [Turla](https://attack.mitre.org/groups/G0010) has used legitimate web services including Pastebin, Dropbox, and GitHub for C2 communications.(Citation: Accenture HyperStack October 2020)(Citation: ESET Crutch December 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102.002 | Bidirectional Communication | A [Turla](https://attack.mitre.org/groups/G0010) JavaScript backdoor has used Google Apps Script as its C2 server.(Citation: ESET Turla Mosquito Jan 2018)(Citation: ESET Turla Mosquito May 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1104 | Multi-Stage Channels | mmands/data for the host of the Snake infection. Commands will be queued in this Container until the implant is ready to execute them. 15MITRE ATT&CK IDs: [T1104] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Command And Control | T1105 | Ingress Tool Transfer | [Turla](https://attack.mitre.org/groups/G0010) has used shellcode to download Meterpreter after compromising a victim.(Citation: ESET Turla Mosquito May 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--turla--f0c7ef1fbe87f2c6` |
| Execution | T1106 | Native API | [Turla](https://attack.mitre.org/groups/G0010) and its RPC backdoors have used APIs calls for various tasks related to subverting AMSI and accessing then executing commands through RPC and/or named pipes.(Citation: ESET Turla PowerShell May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--turla--c3043639afceaf63` |
| Credential Access | T1110 | Brute Force | [Turla](https://attack.mitre.org/groups/G0010) may attempt to connect to systems within a victim's network using <code>net use</code> commands and a predefined list or collection of passwords.(Citation: Kaspersky Turla) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | [Turla](https://attack.mitre.org/groups/G0010) has modified Registry values to store payloads.(Citation: ESET Turla PowerShell May 2019)(Citation: Symantec Waterbug Jun 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--turla--c3043639afceaf63` |
| Collection | T1119 | Automated Collection | g and outgoing data. These keys were saved in the 0x2 Container in the 0x227 and 0x228 30 MITRE ATT&CK IDs: [T1001], [T1104] 31 MITRE ATT&CK IDs: [T1074], [T1119], [T1560.003] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Discovery | T1120 | Peripheral Device Discovery | [Turla](https://attack.mitre.org/groups/G0010) has used <code>fsutil fsinfo drives</code> to list connected drives.(Citation: ESET ComRAT May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1124 | System Time Discovery | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover the system time by using the <code>net time</code> command.(Citation: Kaspersky Turla) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1132 | Data Encoding | ate traffic destined for application software on the compromised server. This 18 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1071.003], [T1090.003], [T1095], [T1132], [T1572], [T1573] 19 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1132.002], [T1547.006], [T1584] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Command And Control | T1132.002 | Non-Standard Encoding | r. This 18 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1071.003], [T1090.003], [T1095], [T1132], [T1572], [T1573] 19 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1132.002], [T1547.006], [T1584] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Privilege Escalation, Stealth | T1134.002 | Create Process with Token | [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors can impersonate or steal process tokens before executing commands.(Citation: ESET Turla PowerShell May 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1135 | Network Share Discovery | in entirely agnostic to the transport layer as long as it implements 4 MITRE ATT&CK IDs: [T0840], [T1003], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | [Turla](https://attack.mitre.org/groups/G0010) has used a custom decryption routine, which pulls key and salt values from other artifacts such as a WMI filter or [PowerShell Profile](https://attack.mitre.org/techniques/T1546/013), to decode encrypted PowerShell payloads.(Citation: ESET Turla PowerShell May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--turla--c3043639afceaf63` |
| Uncategorized | T1158 | MITRE ATT&CK T1158 | de (GReAT), Costin Raiu (GReAT), Daniel Moore (King’s College London), Thomas Rid (King’s College London). April 2017. T1105 T1059 T1205 T1024 T1032 T1158 T1222 T1094 8% 8% 25% 17% 42% EXECUTION LATERAL MOVEMENT PERSISTENCE COMMAND AND CONTROL DEFENCE EVASION TACTICS MITRE ATT&CK TTPs |  |  | 不明 | 不明 | 中 | `source--turla--f0c7ef1fbe87f2c6` |
| Initial Access | T1189 | Drive-by Compromise | [Turla](https://attack.mitre.org/groups/G0010) has infected victims using watering holes.(Citation: ESET ComRAT May 2020)(Citation: Secureworks IRON HUNTER Profile) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | layer as long as it implements 4 MITRE ATT&CK IDs: [T0840], [T1003], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Discovery | T1201 | Password Policy Discovery | [Turla](https://attack.mitre.org/groups/G0010) has used <code>net accounts</code> and <code>net accounts /domain</code> to acquire password policy information.(Citation: ESET ComRAT May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | [Turla](https://attack.mitre.org/groups/G0010) has used spearphishing via a link to get users to download and run their malware.(Citation: ESET Turla Mosquito Jan 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control, Persistence, Stealth | T1205 | Traffic Signaling | uan Andres Guerrero- Saade (GReAT), Costin Raiu (GReAT), Daniel Moore (King’s College London), Thomas Rid (King’s College London). April 2017. T1105 T1059 T1205 T1024 T1032 T1158 T1222 T1094 8% 8% 25% 17% 42% EXECUTION LATERAL MOVEMENT PERSISTENCE COMMAND AND CONTROL DEFENCE EVASION TACTICS MITRE ATT&CK TTPs |  |  | 不明 | 不明 | 中 | `source--turla--f0c7ef1fbe87f2c6` |
| Collection | T1213.006 | Databases | [Turla](https://attack.mitre.org/groups/G0010) has used a custom .NET tool to collect documents from an organization's internal central database.(Citation: ESET ComRAT May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1222 | File and Directory Permissions Modification | T), Costin Raiu (GReAT), Daniel Moore (King’s College London), Thomas Rid (King’s College London). April 2017. T1105 T1059 T1205 T1024 T1032 T1158 T1222 T1094 8% 8% 25% 17% 42% EXECUTION LATERAL MOVEMENT PERSISTENCE COMMAND AND CONTROL DEFENCE EVASION TACTICS MITRE ATT&CK TTPs |  |  | 不明 | 不明 | 中 | `source--turla--f0c7ef1fbe87f2c6` |
| Discovery | T1482 | Domain Trust Discovery | ly agnostic to the transport layer as long as it implements 4 MITRE ATT&CK IDs: [T0840], [T1003], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Discovery | T1518.001 | Security Software Discovery | [Turla](https://attack.mitre.org/groups/G0010) has obtained information on security software, including security logging information that may indicate whether their malware has been detected.(Citation: ESET ComRAT May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1546.003 | Windows Management Instrumentation Event Subscription | [Turla](https://attack.mitre.org/groups/G0010) has used WMI event filters and consumers to establish persistence.(Citation: ESET Turla PowerShell May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1546.013 | PowerShell Profile | [Turla](https://attack.mitre.org/groups/G0010) has used PowerShell profiles to maintain persistence on an infected machine.(Citation: ESET Turla PowerShell May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1546.016 | Installer Packages | er on a host. The first was as a JPEG viewer; later options included disguising the installer as Notepad++ or 7zip. 8 MITRE ATT&CK IDs: [T1027.002], [T1140], [T1546.016], [T1588], [T1610] 9 MITRE ATT&CK IDs: [T1573.001], [T1573.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | A [Turla](https://attack.mitre.org/groups/G0010) Javascript backdoor added a local_update_check value under the Registry key <code>HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run</code> to establish persistence. Additionally, a [Turla](https://attack.mitre.org/groups/G0010) custom executable containing Metasploit shellcode is saved to the Startup folder to gain persistence.(Citation: ESET Turla Mosquito Jan 2018)(Citation: ESET Turla Mosquito May 2018)(Citation: ESET Turla Lunar toolset May 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.004 | Winlogon Helper DLL | [Turla](https://attack.mitre.org/groups/G0010) established persistence by adding a Shell value under the Registry key <code>HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon</code>.(Citation: ESET Turla Mosquito Jan 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.006 | Kernel Modules and Extensions | ], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Defense Impairment | T1553.006 | Code Signing Policy Modification | [Turla](https://attack.mitre.org/groups/G0010) has modified variables in kernel memory to turn off Driver Signature Enforcement after exploiting vulnerabilities that obtained kernel mode privileges.(Citation: Unit42 AcidBox June 2020)(Citation: GitHub Turla Driver Loader) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.004 | Windows Credential Manager | [Turla](https://attack.mitre.org/groups/G0010) has gathered credentials from the Windows Credential Manager tool.(Citation: Symantec Waterbug Jun 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1559 | Inter-Process Communication | x229 (a CAST-128 key). This key will be used to encrypt and decrypt all of the embedded files and modules within the 0x3 Container. 16 MITRE ATT&CK IDs: [T1559] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Collection | T1560.001 | Archive via Utility | [Turla](https://attack.mitre.org/groups/G0010) has encrypted files stolen from connected USB drives into a RAR file before exfiltration.(Citation: Symantec Waterbug Jun 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.003 | Archive via Custom Method | going data. These keys were saved in the 0x2 Container in the 0x227 and 0x228 30 MITRE ATT&CK IDs: [T1001], [T1104] 31 MITRE ATT&CK IDs: [T1074], [T1119], [T1560.003] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Stealth | T1564 | Hide Artifacts | components and loading them into memory.11 10 MITRE ATT&CK IDs: [T1014], [T1027], [T1547.006], [T1610] 11 MITRE ATT&CK IDs: [T1027], [T1036], [T1140], [T1564], [T1569.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Stealth | T1564.012 | File/Path Exclusions | [Turla](https://attack.mitre.org/groups/G0010) has placed [LunarWeb](https://attack.mitre.org/software/S1141) install files into directories that are excluded from scanning.(Citation: ESET Turla Lunar toolset May 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | [Turla](https://attack.mitre.org/groups/G0010) attempted to trick targets into clicking on a link featuring a seemingly legitimate domain from Adobe.com to download their malware and gain initial access.(Citation: ESET Turla Mosquito Jan 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | [Turla](https://attack.mitre.org/groups/G0010) has used WebDAV to upload stolen USB files to a cloud drive.(Citation: Symantec Waterbug Jun 2019) [Turla](https://attack.mitre.org/groups/G0010) has also exfiltrated stolen files to OneDrive and 4shared.(Citation: ESET ComRAT May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1569.002 | Service Execution | ts and loading them into memory.11 10 MITRE ATT&CK IDs: [T1014], [T1027], [T1547.006], [T1610] 11 MITRE ATT&CK IDs: [T1027], [T1036], [T1140], [T1564], [T1569.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Lateral Movement | T1570 | Lateral Tool Transfer | [Turla](https://attack.mitre.org/groups/G0010) RPC backdoors can be used to transfer files to/from victim machines on the local network.(Citation: ESET Turla PowerShell May 2019)(Citation: Symantec Waterbug Jun 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--turla--c3043639afceaf63` |
| Command And Control | T1572 | Protocol Tunneling | ic destined for application software on the compromised server. This 18 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1071.003], [T1090.003], [T1095], [T1132], [T1572], [T1573] 19 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1132.002], [T1547.006], [T1584] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Command And Control | T1573 | Encrypted Channel | ed for application software on the compromised server. This 18 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1071.003], [T1090.003], [T1095], [T1132], [T1572], [T1573] 19 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1132.002], [T1547.006], [T1584] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Command And Control | T1573.001 | Symmetric Cryptography | options included disguising the installer as Notepad++ or 7zip. 8 MITRE ATT&CK IDs: [T1027.002], [T1140], [T1546.016], [T1588], [T1610] 9 MITRE ATT&CK IDs: [T1573.001], [T1573.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Command And Control | T1573.002 | Asymmetric Cryptography | uded disguising the installer as Notepad++ or 7zip. 8 MITRE ATT&CK IDs: [T1027.002], [T1140], [T1546.016], [T1588], [T1610] 9 MITRE ATT&CK IDs: [T1573.001], [T1573.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Uncategorized | T1574.002 | MITRE ATT&CK T1574.002 | at are stored in the encrypted registry blob.13 12 MITRE ATT&CK IDs: [T1106], [T1112], [T1547.006] 13 MITRE ATT&CK IDs: [T1027], [T1547.006], [T1569.002], [T1574.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Resource Development | T1583.006 | Web Services | [Turla](https://attack.mitre.org/groups/G0010) has created web accounts including Dropbox and GitHub for C2 and document exfiltration.(Citation: ESET Crutch December 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584 | Compromise Infrastructure | IDs: [T1001.003], [T1071], [T1071.003], [T1090.003], [T1095], [T1132], [T1572], [T1573] 19 MITRE ATT&CK IDs: [T1001.003], [T1071], [T1132.002], [T1547.006], [T1584] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Resource Development | T1584.003 | Virtual Private Server | [Turla](https://attack.mitre.org/groups/G0010) has used the VPS infrastructure of compromised Iranian threat actors.(Citation: NSA NCSC Turla OilRig) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.004 | Server | [Turla](https://attack.mitre.org/groups/G0010) has used compromised servers as infrastructure.(Citation: Recorded Future Turla Infra 2020)(Citation: Accenture HyperStack October 2020)(Citation: Talos TinyTurla September 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.006 | Web Services | [Turla](https://attack.mitre.org/groups/G0010) has frequently used compromised WordPress sites for C2 infrastructure.(Citation: Recorded Future Turla Infra 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | [Turla](https://attack.mitre.org/groups/G0010) has developed its own unique malware for use in operations.(Citation: Recorded Future Turla Infra 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--turla--c3043639afceaf63` |
| Resource Development | T1588 | Obtain Capabilities | The first was as a JPEG viewer; later options included disguising the installer as Notepad++ or 7zip. 8 MITRE ATT&CK IDs: [T1027.002], [T1140], [T1546.016], [T1588], [T1610] 9 MITRE ATT&CK IDs: [T1573.001], [T1573.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Resource Development | T1588.001 | Malware | [Turla](https://attack.mitre.org/groups/G0010) has used malware obtained after compromising other threat actors, such as [OilRig](https://attack.mitre.org/groups/G0049).(Citation: NSA NCSC Turla OilRig)(Citation: Recorded Future Turla Infra 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [Turla](https://attack.mitre.org/groups/G0010) has obtained and customized publicly-available tools like [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: Symantec Waterbug Jun 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608 | Stage Capabilities | 4 MITRE ATT&CK IDs: [T0840], [T1003], [T1040], [T1046], [T1056.001], [T1078], [T1083], [T1135], [T1482] 5 MITRE ATT&CK IDs: [T1190], [T1570], [T1587.001], [T1608] 6 MITRE ATT&CK IDs: [T1095], [T1547.006], [T1587.001] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Execution | T1610 | Deploy Container | t was as a JPEG viewer; later options included disguising the installer as Notepad++ or 7zip. 8 MITRE ATT&CK IDs: [T1027.002], [T1140], [T1546.016], [T1588], [T1610] 9 MITRE ATT&CK IDs: [T1573.001], [T1573.002] |  |  | 不明 | 不明 | 中 | `source--turla--c3043639afceaf63` |
| Discovery | T1615 | Group Policy Discovery | [Turla](https://attack.mitre.org/groups/G0010) surveys a system upon check-in to discover Group Policy details using the <code>gpresult</code> command.(Citation: ESET ComRAT May 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | [Turla](https://attack.mitre.org/groups/G0010) has used a AMSI bypass, which patches the in-memory amsi.dll, in PowerShell scripts to bypass Windows antimalware products.(Citation: ESET Turla PowerShell May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command and Control | T1090 | Proxy | STOCKSTAY.STOCKBROKERが企業プロキシ環境を考慮した通信経路を確立する。 | malware--stockstay | activity--gtig-stockstay-turla-2026 | 2022-12 | 2025-11 | 高 | `source--gtig-stockstay-turla-2026` |
| Execution | T1203 | Exploitation for Client Execution | WinRARのパストラバーサル脆弱性CVE-2025-8088を悪用して実行に至らせる。 | malware--stockstay | activity--gtig-stockstay-turla-2026 | 不明 | 不明 | 中 | `source--gtig-stockstay-turla-2026` |
| Initial Access | T1566.001 | Spearphishing Attachment | 悪性のRDPファイルを添付したフィッシングでSTOCKSTAYの実行に至らせる。 | malware--stockstay | activity--gtig-stockstay-turla-2026 | 2022-12 | 2025-11 | 高 | `source--gtig-stockstay-turla-2026` |
| Command and Control | T1572 | Protocol Tunneling | STOCKSTAY.STOCKBROKERがWebSocketトンネラーとしてC2通信を中継する。 | malware--stockstay | activity--gtig-stockstay-turla-2026 | 2022-12 | 2025-11 | 高 | `source--gtig-stockstay-turla-2026` |

## IOC／artifact概要

- IOC値: 125件
- IOC観測: 159件
- 複数攻撃で観測: 0件
- 要レビュー候補: 62件
- 非IOC artifact観測: 84件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| TurlaはSTOCKSTAYを2022年から2025年にかけて継続的に開発・展開し、ウクライナとイタリアの政府・外交関連組織への諜報活動に使用している。 | 高 | `source--gtig-stockstay-turla-2026` |  |

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.
- GTIGのSTOCKSTAY報告(2026-06-25)はtech-memoの日次ニュースに未収録であり、同種の取りこぼしがないか一次情報源の確認範囲を継続的に見直す必要がある。

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.
- STOCKSTAYとKAZUARの共通開発者評価はGTIGの中程度確度の判断であり、両マルウェアを同一系統として統合しない。
- WILDDAYとDIAMONDBACKは本資料では併記に留まり、技術詳細と観測時期を確認できていない。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--daily-0e103138b331cf8b266a | ロシアのハッカー、Kazuarバックドアをモジュール型P2Pボットネットへ進化 | microsoft.com | 2026-05-18 | https://www.microsoft.com/en-us/security/blog/2026/05/14/kazuar-anatomy-of-a-nation-state-botnet/ | osint-report | TLP:CLEAR | 中 |
| source--daily-785ae8d632612c179b8d | ロシアのサイバースパイ、他のハッカーの背後に隠れてウクライナを標的に | bleepingcomputer.com | 2024-12-12 | https://www.bleepingcomputer.com/news/security/russian-cyber-spies-hide-behind-other-hackers-to-target-ukraine/ | osint-report | TLP:CLEAR | 中 |
| source--daily-7b8d62bd6d4144728793 | ロシアのTurlaハッカー、パキスタンのAPTサーバーを乗っ取りサイバースパイ活動を展開 | bleepingcomputer.com | 2024-12-05 | https://www.bleepingcomputer.com/news/security/russian-turla-hackers-hijack-pakistani-apt-servers-for-cyber-espionage-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--turla--381349fb0cea34f0 | Penquins Moonlit Maze AppendixB |  | 不明 | Turla/2017/Penquins_Moonlit_Maze_AppendixB.pdf | report | TLP:CLEAR | 中 |
| source--turla--3d5a4d35095a89d3 | README |  | 不明 | Turla/2014/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--turla--6e90d1ef9571f3b1 | IOC |  | 不明 | Turla/IOC.TXT | text-data | TLP:CLEAR | 中 |
| source--turla--9c3fb3485b0c32a0 | Penquins Moonlit Maze PDF eng |  | 不明 | Turla/2017/Penquins_Moonlit_Maze_PDF_eng.pdf | report | TLP:CLEAR | 中 |
| source--turla--c3043639afceaf63 | aa23 129a snake malware 2 |  | 不明 | Turla/aa23-129a_snake_malware_2.pdf | report | TLP:CLEAR | 中 |
| source--turla--e6c93c546a97e314 | README |  | 不明 | Turla/2017/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--turla--f0c7ef1fbe87f2c6 | Malware Technical Insight  Turla “Penquin x64” |  | 不明 | Turla/Malware Technical Insight _Turla “Penquin_x64”.pdf | report | TLP:CLEAR | 中 |
| source--gtig-stockstay-turla-2026 | STOCKSTAY Another Day: The Latest Addition to Turla's Intelligence Gathering Apparatus | Google Threat Intelligence Group | 2026-06-25 | https://cloud.google.com/blog/topics/threat-intelligence/stockstay-turla-intelligence-gathering | vendor-research-report | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
