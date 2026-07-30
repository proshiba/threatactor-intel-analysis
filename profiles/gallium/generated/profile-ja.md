# GALLIUM 脅威アクタープロファイル

- プロファイルID: `actor--gallium`
- 状態: draft
- 更新日時: 2026-07-29T23:12:00Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

GALLIUMの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **GALLIUM**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Granite Typhoon | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Soft Cell | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| UNSC 2814 | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Soft Cell, UNSC 2814 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 93; mapping requires review. |

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

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [GALLIUM](https://attack.mitre.org/groups/G0093) is a cyberespionage group that has been active since at least 2012, primarily targeting telecommunications companies, financial institutions, and government entities in Afghanistan, Australia, Belgium, Cambodia, Malaysia, Mozambique, the Philippines, Russia, and Vietnam. This group is particularly known for launching Operation Soft Cell, a long-term campaign targeting telecommunications providers.(Citation: Cybereason Soft Cell June 2019) Security researchers have identified [GALLIUM](https://attack.mitre.org/groups/G0093) as a likely Chinese state-sponsored group, based in part on tools used and TTPs commonly associated with Chinese threat actors.(Citation: Cybereason Soft Cell June 2019)(Citation: Microsoft GALLIUM December 2019)(Citation: Unit 42 PingPull Jun 2022) |
| Capability | PingPull, China Chopper, BlackMould, PlugX, PoisonIvy, QuarkBandit, Winrar, Netcat, Net, at, Windows Credential Editor, ipconfig, Mimikatz, NBTscan, Ping, cmd, Reg, HTRAN, PsExec |
| Infrastructure |  |
| Victim | Telecom |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Gallium | canonical-name | 高 | China | https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Gallium&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Granite Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | GALLIUM | canonical-name | 高 | CN | https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/<br>https://www.youtube.com/watch?v=fBFm2fiEPTg<br>https://troopers.de/troopers22/talks/7cv8pz/ |
| misp-microsoft-activity-group | GALLIUM | canonical-name | 高 |  | https://www.microsoft.com/security/blog/2019/12/12/gallium-targeting-global-telecom/ |
| misp-microsoft-activity-group | Granite Typhoon | canonical-name | 高 | CN, China | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | GALLIUM - G0093 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0093<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://unit42.paloaltonetworks.com/pingpull-gallium/ |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Operation Soft Cell | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--pingpull | PingPull | [PingPull](https://attack.mitre.org/software/S1031) is a remote access Trojan (RAT) written in Visual C++ that has been used by [GALLIUM](https://attack.mitre.org/groups/G0093) since at least June 2022. [PingPull](https://attack.mitre.org/software/S1031) has been used to target telecommunications companies, financial institutions, and government entities in Afghanistan, Australia, Belgium, Cambodia, Malaysia, Mozambique, the Philippines, Russia, and Vietnam.(Citation: Unit 42 PingPull Jun 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--china-chopper | China Chopper | [China Chopper](https://attack.mitre.org/software/S0020) is a [Web Shell](https://attack.mitre.org/techniques/T1505/003) hosted on Web servers to provide access back into an enterprise network that does not rely on an infected system calling back to a remote command and control server.(Citation: Lee 2013) It has been used by several threat groups.(Citation: Dell TG-3390)(Citation: FireEye Periscope March 2018)(Citation: CISA AA21-200A APT40 July 2021)(Citation: Rapid7 HAFNIUM Mar 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--blackmould | BlackMould | [BlackMould](https://attack.mitre.org/software/S0564) is a web shell based on [China Chopper](https://attack.mitre.org/software/S0020) for servers running Microsoft IIS. First reported in December 2019, it has been used in malicious campaigns by [GALLIUM](https://attack.mitre.org/groups/G0093) against telecommunication providers.(Citation: Microsoft GALLIUM December 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--plugx | PlugX | [PlugX](https://attack.mitre.org/software/S0013) is a remote access tool (RAT) with modular plugins that has been used by multiple threat groups.(Citation: Lastline PlugX Analysis)(Citation: FireEye Clandestine Fox Part 2)(Citation: New DragonOK)(Citation: Dell TG-3390) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--poisonivy | PoisonIvy | [PoisonIvy](https://attack.mitre.org/software/S0012) is a popular remote access tool (RAT) that has been used by many groups.(Citation: FireEye Poison Ivy)(Citation: Symantec Elderwood Sept 2012)(Citation: Symantec Darkmoon Aug 2005) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--quarkbandit | QuarkBandit | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--winrar | Winrar | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--netcat | Netcat | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--at | at | [at](https://attack.mitre.org/software/S0110) is used to schedule tasks on a system to run at a specified date or time.(Citation: TechNet At)(Citation: Linux at) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--windows-credential-editor | Windows Credential Editor | [Windows Credential Editor](https://attack.mitre.org/software/S0005) is a password dumping tool. (Citation: Amplia WCE) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ipconfig | ipconfig | [ipconfig](https://attack.mitre.org/software/S0100) is a Windows utility that can be used to find information about a system's TCP/IP, DNS, DHCP, and adapter configuration. (Citation: TechNet Ipconfig) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--nbtscan | NBTscan | [NBTscan](https://attack.mitre.org/software/S0590) is an open source tool that has been used by state groups to conduct internal reconnaissance within a compromised network.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan June 2003)(Citation: Symantec Waterbug Jun 2019)(Citation: FireEye APT39 Jan 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ping | Ping | [Ping](https://attack.mitre.org/software/S0097) is an operating system utility commonly used to troubleshoot and verify network connections. (Citation: TechNet Ping) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--cmd | cmd | [cmd](https://attack.mitre.org/software/S0106) is the Windows command-line interpreter that can be used to interact with systems and execute other processes and utilities. (Citation: TechNet Cmd)<br><br>Cmd.exe contains native functionality to perform many operations to interact with the system, including listing files in a directory (e.g., <code>dir</code> (Citation: TechNet Dir)), deleting files (e.g., <code>del</code> (Citation: TechNet Del)), and copying files (e.g., <code>copy</code> (Citation: TechNet Copy)). | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--reg | Reg | [Reg](https://attack.mitre.org/software/S0075) is a Windows utility used to interact with the Windows Registry. It can be used at the command-line interface to query, add, modify, and remove information. (Citation: Microsoft Reg)<br><br>Utilities such as [Reg](https://attack.mitre.org/software/S0075) are known to be used by persistent threats. (Citation: Windows Commands JPCERT) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--htran | HTRAN | [HTRAN](https://attack.mitre.org/software/S0040) is a tool that proxies connections through intermediate hops and aids users in disguising their true geographical location. It can be used by adversaries to hide their location when interacting with the victim networks. (Citation: Operation Quantum Entanglement)(Citation: NCSC Joint Report Public Tools) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
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

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アフガニスタン | MITRE ATT&CKのGroup概要でGALLIUMの標的国として明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| countries | オーストラリア | [GALLIUM](https://attack.mitre.org/groups/G0093) is a cyberespionage group that has been active since at least 2012, primarily targeting telecommunications companies, financial institutions, and government entities in Afghanistan, Australia, Belgium, Cambodia, Malaysia, Mozambique, the Philippines, Russia, and Vietnam. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| countries | カンボジア | MITRE ATT&CKのGroup概要でGALLIUMの標的国として明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| countries | フィリピン | MITRE ATT&CKのGroup概要でGALLIUMの標的国として明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| countries | ベトナム | MITRE ATT&CKのGroup概要でGALLIUMの標的国として明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| countries | ベルギー | MITRE ATT&CKのGroup概要でGALLIUMの標的国として明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| countries | マレーシア | MITRE ATT&CKのGroup概要でGALLIUMの標的国として明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| countries | モザンビーク | MITRE ATT&CKのGroup概要でGALLIUMの標的国として明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| countries | ロシア | s/G0093) is a cyberespionage group that has been active since at least 2012, primarily targeting telecommunications companies, financial institutions, and government entities in Afghanistan, Australia, Belgium, Cambodia, Malaysia, Mozambique, the Philippines, Russia, and Vietnam. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| regions | 東南アジア | カンボジア、フィリピン、ベトナム、マレーシアで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--mitre-attack-19-1` |
| sectors | 情報通信 | [GALLIUM](https://attack.mitre.org/groups/G0093) is a cyberespionage group that has been active since at least 2012, primarily targeting telecommunications companies, financial institutions, and government entities in Afghanistan, Australia, Belgium, Cambodia, Malaysia, Mozambique, the Philippines, Russia, and Vietnam. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 金融 | [GALLIUM](https://attack.mitre.org/groups/G0093) is a cyberespionage group that has been active since at least 2012, primarily targeting telecommunications companies, financial institutions, and government entities in Afghanistan, Australia, Belgium, Cambodia, Malaysia, Mozambique, the Philippines, Russia, and Vietnam. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 政府・行政 | [GALLIUM](https://attack.mitre.org/groups/G0093) is a cyberespionage group that has been active since at least 2012, primarily targeting telecommunications companies, financial institutions, and government entities in Afghanistan, Australia, Belgium, Cambodia, Malaysia, Mozambique, the Philippines, Russia, and Vietnam. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | Telecommunications | Targeting text indicates the Telecommunications sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.001 | LSASS Memory | [GALLIUM](https://attack.mitre.org/groups/G0093) used a modified version of [Mimikatz](https://attack.mitre.org/software/S0002) along with a PowerShell-based [Mimikatz](https://attack.mitre.org/software/S0002) to dump credentials on the victim machines.(Citation: Cybereason Soft Cell June 2019)(Citation: Microsoft GALLIUM December 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.002 | Security Account Manager | [GALLIUM](https://attack.mitre.org/groups/G0093) used <code>reg</code> commands to dump specific hives from the Windows Registry, such as the SAM hive, and obtain password hashes.(Citation: Cybereason Soft Cell June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | [GALLIUM](https://attack.mitre.org/groups/G0093) collected data from the victim's local system, including password hashes from the SAM hive in the Registry.(Citation: Cybereason Soft Cell June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | [GALLIUM](https://attack.mitre.org/groups/G0093) used <code>ipconfig /all</code> to obtain information about the victim network configuration. The group also ran a modified version of [NBTscan](https://attack.mitre.org/software/S0590) to identify available NetBIOS name servers.(Citation: Cybereason Soft Cell June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | [GALLIUM](https://attack.mitre.org/groups/G0093) used a modified version of [NBTscan](https://attack.mitre.org/software/S0590) to identify available NetBIOS name servers over the network as well as <code>ping</code> to identify remote systems.(Citation: Cybereason Soft Cell June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027 | Obfuscated Files or Information | [GALLIUM](https://attack.mitre.org/groups/G0093) used a modified version of [HTRAN](https://attack.mitre.org/software/S0040) in which they obfuscated strings such as debug messages in an apparent attempt to evade detection.(Citation: Cybereason Soft Cell June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.002 | Software Packing | [GALLIUM](https://attack.mitre.org/groups/G0093) packed some payloads using different types of packers, both known and custom.(Citation: Cybereason Soft Cell June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.005 | Indicator Removal from Tools | [GALLIUM](https://attack.mitre.org/groups/G0093) ensured each payload had a unique hash, including by using different types of packers.(Citation: Cybereason Soft Cell June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | [GALLIUM](https://attack.mitre.org/groups/G0093) used <code>whoami</code> and <code>query user</code> to obtain information about the victim user.(Citation: Cybereason Soft Cell June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.003 | Rename Legitimate Utilities | [GALLIUM](https://attack.mitre.org/groups/G0093) used a renamed cmd.exe file to evade detection.(Citation: Cybereason Soft Cell June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | [GALLIUM](https://attack.mitre.org/groups/G0093) used Web shells and [HTRAN](https://attack.mitre.org/software/S0040) for C2 and to exfiltrate data.(Citation: Cybereason Soft Cell June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | [GALLIUM](https://attack.mitre.org/groups/G0093) used WMI for execution to assist in lateral movement as well as for installing tools across multiple assets.(Citation: Cybereason Soft Cell June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | [GALLIUM](https://attack.mitre.org/groups/G0093) used <code>netstat -oan</code> to obtain information about the victim network connections.(Citation: Cybereason Soft Cell June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [GALLIUM](https://attack.mitre.org/groups/G0093) established persistence for [PoisonIvy](https://attack.mitre.org/software/S0012) by created a scheduled task.(Citation: Cybereason Soft Cell June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [GALLIUM](https://attack.mitre.org/groups/G0093) used PowerShell for execution to assist in lateral movement as well as for dumping credentials stored on compromised machines.(Citation: Cybereason Soft Cell June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [GALLIUM](https://attack.mitre.org/groups/G0093) used the Windows command shell to execute commands.(Citation: Cybereason Soft Cell June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | [GALLIUM](https://attack.mitre.org/groups/G0093) compressed and staged files in multi-part archives in the Recycle Bin prior to exfiltration.(Citation: Cybereason Soft Cell June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [GALLIUM](https://attack.mitre.org/groups/G0093) leveraged valid accounts to maintain access to a victim network.(Citation: Cybereason Soft Cell June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090.002 | External Proxy | [GALLIUM](https://attack.mitre.org/groups/G0093) used a modified version of [HTRAN](https://attack.mitre.org/software/S0040) to redirect connections between networks.(Citation: Cybereason Soft Cell June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [GALLIUM](https://attack.mitre.org/groups/G0093) dropped additional tools to victims during their operation, including portqry.exe, a renamed cmd.exe file, winrar, and [HTRAN](https://attack.mitre.org/software/S0040).(Citation: Cybereason Soft Cell June 2019)(Citation: Microsoft GALLIUM December 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence | T1133 | External Remote Services | [GALLIUM](https://attack.mitre.org/groups/G0093) has used VPN services, including SoftEther VPN, to access and maintain persistence in victim environments.(Citation: Cybereason Soft Cell June 2019)(Citation: Microsoft GALLIUM December 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1136.002 | Domain Account | [GALLIUM](https://attack.mitre.org/groups/G0093) created high-privileged domain user accounts to maintain access to victim networks.(Citation: Cybereason Soft Cell June 2019)(Citation: Microsoft GALLIUM December 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [GALLIUM](https://attack.mitre.org/groups/G0093) exploited a publicly-facing servers including Wildfly/JBoss servers to gain access to the network.(Citation: Cybereason Soft Cell June 2019)(Citation: Microsoft GALLIUM December 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | [GALLIUM](https://attack.mitre.org/groups/G0093) used Web shells to persist in victim environments and assist in execution and exfiltration.(Citation: Cybereason Soft Cell June 2019)(Citation: Microsoft GALLIUM December 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1550.002 | Pass the Hash | [GALLIUM](https://attack.mitre.org/groups/G0093) used dumped hashes to authenticate to other machines via pass the hash.(Citation: Cybereason Soft Cell June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1553.002 | Code Signing | [GALLIUM](https://attack.mitre.org/groups/G0093) has used stolen certificates to sign its tools including those from Whizzimo LLC.(Citation: Microsoft GALLIUM December 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | [GALLIUM](https://attack.mitre.org/groups/G0093) used WinRAR to compress and encrypt stolen data prior to exfiltration.(Citation: Cybereason Soft Cell June 2019)(Citation: Microsoft GALLIUM December 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1570 | Lateral Tool Transfer | [GALLIUM](https://attack.mitre.org/groups/G0093) has used [PsExec](https://attack.mitre.org/software/S0029) to move laterally between hosts in the target network.(Citation: Microsoft GALLIUM December 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | [GALLIUM](https://attack.mitre.org/groups/G0093) used DLL side-loading to covertly load [PoisonIvy](https://attack.mitre.org/software/S0012) into memory on the victim machine.(Citation: Cybereason Soft Cell June 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.004 | Server | [GALLIUM](https://attack.mitre.org/groups/G0093) has used Taiwan-based servers that appear to be exclusive to [GALLIUM](https://attack.mitre.org/groups/G0093).(Citation: Microsoft GALLIUM December 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [GALLIUM](https://attack.mitre.org/groups/G0093) has used a variety of widely-available tools, which in some cases they modified to add functionality and/or subvert antimalware solutions.(Citation: Microsoft GALLIUM December 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 28件（`artifacts.csv`）

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
| source--gallium--3c830a306dfb9d8f | gallium |  | 不明 | actor_profile/evidence/gallium.csv | structured-data | TLP:CLEAR | 中 |
| source--gallium--005f21142816f644 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--gallium--9c767654ad42d0aa | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--gallium--77ac2bab5795259c | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--gallium--54756a759231a07b | Microsoft Digital Defense Report 2022 |  | 2022 | summary/2022/Microsoft Digital Defense Report 2022.pdf | report | TLP:CLEAR | 中 |
| source--gallium--eec0e5d304cbdca7 | 2022 year in retrospect report |  | 2022 | summary/2023/2022-year-in-retrospect-report.pdf | report | TLP:CLEAR | 中 |
| source--gallium--d48c2adbd4220394 | Microsoft Digital Defense Report 2024 |  | 2024 | summary/2024/Microsoft Digital Defense Report 2024.pdf | report | TLP:CLEAR | 中 |
| source--gallium--536faf5434cbe42c | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--gallium--3cee436d508cf611 | eset apt activity report q4 2024 q1 2025 |  | 2024 | summary/2025/eset-apt-activity-report-q4-2024-q1-2025.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
