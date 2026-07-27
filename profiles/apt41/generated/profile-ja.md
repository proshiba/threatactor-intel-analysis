# APT41 脅威アクタープロファイル

- プロファイルID: `actor--apt41`
- 状態: review
- 更新日時: 2026-07-27T11:17:22Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

APT41の標準化プロファイル。リポジトリ内の専用資料2件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **APT41**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| BARIUM | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Brass Typhoon | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Wicked Panda | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| HOODOO |  | vendor | 高 | `source--gtig-apt41-toughprogress-2025` |  |

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
| financial-gain | Financially motivated intrusion or fraud. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Winnti Group | overlaps-with | MITRE states that APT41 overlaps at least partially with public reporting on Winnti Group. | 高 | `source--mitre-live-apt41-2025` |
| Earth Lusca | related-to | [Earth Lusca](https://attack.mitre.org/groups/G1006) has used malware commonly used by other Chinese threat groups, including [APT41](https://attack.mitre.org/groups/G0096) and the [Winnti Group](https://attack.mitre.org/groups/G0044) cluster, however security researchers assess [Earth Lusca](https://attack.mitre.org/groups/G1006)'s techniques and infrastructure are separate.(Citation: TrendMicro EarthLusca 2022) | 中 | `source--mitre-attack-19-1` |
| RedEcho | overlaps-with | [RedEcho](https://attack.mitre.org/groups/G1042) overlaps with various other PRC-linked threat groups, such as [APT41](https://attack.mitre.org/groups/G0096), and is linked to [ShadowPad](https://attack.mitre.org/software/S0596) malware use through shared infrastructure.(Citation: RecordedFuture RedEcho 2021)(Citation: RecordedFuture RedEcho 2022) | 高 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [APT41](https://attack.mitre.org/groups/G0096) is a threat group that researchers have assessed as Chinese state-sponsored espionage group that also conducts financially-motivated operations. Active since at least 2012, [APT41](https://attack.mitre.org/groups/G0096) has been observed targeting various industries, including but not limited to healthcare, telecom, technology, finance, education, retail and video game industries in 14 countries.(Citation: apt41_mandiant) Notable behaviors include using a wide range of malware and tools to complete mission objectives. [APT41](https://attack.mitre.org/groups/G0096) overlaps at least partially with public reporting on groups including BARIUM and [Winnti Group](https://attack.mitre.org/groups/G0044).(Citation: FireEye APT41 Aug 2019)(Citation: Group IB APT 41 June 2021)<br> |
| Capability | DUSTTRAP, DUSTPAN, ASPXSpy, China Chopper, LightSpy, PlugX, KEYPLUG, Winnti for Linux, gh0st RAT, Derusbi, MESSAGETAP, Cobalt Strike, MOPSLED, ROCKBOOT, ZxShell, BLACKCOFFEE, njRAT, ShadowPad, CRACKSHOT, GEARSHIFT, HIGHNOON, JUMPALL, POISONPLUG, HOTCHAI, LATELUNCH, LIFEBOAT, LOWKEY, PACMAN, PHOTO, POTROAST, SAGEHIRE, SWEETCANDLE, SOGU, TERA, TIDYELF, WIDETONE, WINTERLOVE, XDoor, Xmrig, Net, certutil, PowerSploit, Impacket, ipconfig, Empire, dsquery, netstat, BITSAdmin, sqlmap, pwdump, Mimikatz, Ping, ftp |
| Infrastructure |  |
| Victim |  |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | APT 41 | canonical-name | 高 | China | http://content.fireeye.com/apt41/rpt-apt41<br>https://arstechnica.com/information-technology/2018/05/researchers-link-a-decade-of-potent-hacks-to-chinese-intelligence-group/<br>https://www.kaspersky.com/about/press-releases/2019_operation-shadowhammer-new-supply-chain-attack |
| etda-threat-group-cards | Barium | multiple-name-intersection | 高 | China | https://threatvector.cylance.com/en_us/home/digitally-signed-malware-targeting-gaming-companies.html<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Barium&n=1 |
| etda-threat-group-cards | Winnti Group, Wicked Panda | single-alias-intersection | 中 | China | https://blog.trendmicro.com/trendlabs-security-intelligence/pigs-malware-examining-possible-member-winnti-group/<br>https://securelist.com/winnti-more-than-just-a-game/37029/<br>https://401trg.com/burning-umbrella/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Brass Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| microsoft-threat-actor-mapping | Leopard Typhoon | single-alias-intersection | 中 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | APT41 | canonical-name | 高 | CN, People's Republic of China | https://securelist.com/winnti-faq-more-than-just-a-game/57585/<br>https://securelist.com/winnti-more-than-just-a-game/37029/<br>http://williamshowalter.com/a-universal-windows-bootkit/ |
| misp-microsoft-activity-group | BARIUM | single-alias-intersection | 中 |  | https://blogs.technet.microsoft.com/mmpc/2017/01/25/detecting-threat-actors-in-recent-german-industrial-attacks-with-windows-defender-atp/ |
| misp-microsoft-activity-group | Brass Typhoon | canonical-name | 高 | CN, China | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Leopard Typhoon | single-alias-intersection | 中 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | APT41 - G0096 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0096<br>https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| APT17 | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--aspxspy | ASPXSpy | [ASPXSpy](https://attack.mitre.org/software/S0073) is a Web shell. It has been modified by [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors to create the ASPXTool version. (Citation: Dell TG-3390) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--blackcoffee | BLACKCOFFEE | [BLACKCOFFEE](https://attack.mitre.org/software/S0069) is malware that has been used by several Chinese groups since at least 2013. (Citation: FireEye APT17) (Citation: FireEye Periscope March 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--china-chopper | China Chopper | [China Chopper](https://attack.mitre.org/software/S0020) is a [Web Shell](https://attack.mitre.org/techniques/T1505/003) hosted on Web servers to provide access back into an enterprise network that does not rely on an infected system calling back to a remote command and control server.(Citation: Lee 2013) It has been used by several threat groups.(Citation: Dell TG-3390)(Citation: FireEye Periscope March 2018)(Citation: CISA AA21-200A APT40 July 2021)(Citation: Rapid7 HAFNIUM Mar 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--cobalt-strike | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) is a commercial, full-featured, remote access tool that bills itself as “adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors”. Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.(Citation: cobaltstrike manual)<br><br>In addition to its own capabilities, [Cobalt Strike](https://attack.mitre.org/software/S0154) leverages the capabilities of other well-known tools such as Metasploit and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: cobaltstrike manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--crackshot | CRACKSHOT | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--derusbi | Derusbi | [Derusbi](https://attack.mitre.org/software/S0021) is malware used by multiple Chinese APT groups.(Citation: Novetta-Axiom)(Citation: ThreatConnect Anthem) Both Windows and Linux variants have been observed.(Citation: Fidelis Turbo) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--dustpan | DUSTPAN | [DUSTPAN](https://attack.mitre.org/software/S1158) is an in-memory dropper written in C/C++ used by [APT41](https://attack.mitre.org/groups/G0096) since 2021 that decrypts and executes an embedded payload.(Citation: Google Cloud APT41 2024)(Citation: Google Cloud APT41 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--dusttrap | DUSTTRAP | [DUSTTRAP](https://attack.mitre.org/software/S1159) is a multi-stage plugin framework associated with [APT41](https://attack.mitre.org/groups/G0096) operations with multiple components.(Citation: Google Cloud APT41 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--gearshift | GEARSHIFT | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--gh0st-rat | gh0st RAT | [gh0st RAT](https://attack.mitre.org/software/S0032) is a remote access tool (RAT). The source code is public and it has been used by multiple groups.(Citation: FireEye Hacking Team)(Citation: Arbor Musical Chairs Feb 2018)(Citation: Nccgroup Gh0st April 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--highnoon | HIGHNOON | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--hotchai | HOTCHAI | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--jumpall | JUMPALL | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--keyplug | KEYPLUG | [KEYPLUG](https://attack.mitre.org/software/S1051) is a modular backdoor written in C++, with Windows and Linux variants, that has been used by [APT41](https://attack.mitre.org/groups/G0096) since at least June 2021.(Citation: Mandiant APT41) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--latelunch | LATELUNCH | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--lifeboat | LIFEBOAT | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--lightspy | LightSpy | First observed in 2018, LightSpy is a modular malware family that initially targeted iOS devices in Southern Asia before expanding to Android and macOS platforms. It consists of a downloader, a main executable that manages network communications, and functionality-specific modules, typically implemented as `.dylib` files (iOS, macOS) or `.apk` files (Android). LightSpy can collect VoIP call recordings, SMS messages, and credential stores, which are then exfiltrated to a command and control (C2) server.(Citation: MelikovBlackBerry LightSpy 2024)  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--lowkey | LOWKEY | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--messagetap | MESSAGETAP | [MESSAGETAP](https://attack.mitre.org/software/S0443) is a data mining malware family deployed by [APT41](https://attack.mitre.org/groups/G0096) into telecommunications networks to monitor and save SMS traffic from specific phone numbers, IMSI numbers, or that contain specific keywords. (Citation: FireEye MESSAGETAP October 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--mopsled | MOPSLED | [MOPSLED](https://attack.mitre.org/software/S1221) is a shellcode-based modular backdoor that has been used by China-nexus cyber espionage actors including [UNC3886](https://attack.mitre.org/groups/G1048) and [APT41](https://attack.mitre.org/groups/G0096).(Citation: Google Cloud Mandiant UNC3886 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--njrat | njRAT | [njRAT](https://attack.mitre.org/software/S0385) is a remote access tool (RAT) that was first observed in 2012. It has been used by threat actors in the Middle East.(Citation: Fidelis njRAT June 2013) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--pacman | PACMAN | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--photo | PHOTO | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--plugx | PlugX | [PlugX](https://attack.mitre.org/software/S0013) is a remote access tool (RAT) with modular plugins that has been used by multiple threat groups.(Citation: Lastline PlugX Analysis)(Citation: FireEye Clandestine Fox Part 2)(Citation: New DragonOK)(Citation: Dell TG-3390) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--plusdrop | PLUSDROP | DLL that decrypts and executes the next-stage payload in memory. | 2024-10 | 2024-10 | 高 | `source--gtig-apt41-toughprogress-2025` |
| malware--plusinject | PLUSINJECT | Performs process hollowing in svchost.exe and injects TOUGHPROGRESS. | 2024-10 | 2024-10 | 高 | `source--gtig-apt41-toughprogress-2025` |
| malware--poisonplug | POISONPLUG | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--potroast | POTROAST | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--rockboot | ROCKBOOT | [ROCKBOOT](https://attack.mitre.org/software/S0112) is a [Bootkit](https://attack.mitre.org/techniques/T1542/003) that has been used by an unidentified, suspected China-based group. (Citation: FireEye Bootkits) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--sagehire | SAGEHIRE | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--shadowpad | ShadowPad | [ShadowPad](https://attack.mitre.org/software/S0596) is a modular backdoor that was first identified in a supply chain compromise of the NetSarang software in mid-July 2017. The malware was originally thought to be exclusively used by [APT41](https://attack.mitre.org/groups/G0096), but has since been observed to be used by various Chinese threat activity groups. (Citation: Recorded Future RedEcho Feb 2021)(Citation: Securelist ShadowPad Aug 2017)(Citation: Kaspersky ShadowPad Aug 2017)  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--sogu | SOGU | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--sweetcandle | SWEETCANDLE | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--tera | TERA | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--tidyelf | TIDYELF | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--toughprogress | TOUGHPROGRESS | Memory-resident backdoor that executes commands and uses attacker-controlled Google Calendar events for encrypted C2. | 2024-10 | 2024-10 | 高 | `source--gtig-apt41-toughprogress-2025` |
| malware--widetone | WIDETONE | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--winnti-for-linux | Winnti for Linux | [Winnti for Linux](https://attack.mitre.org/software/S0430) is a trojan, seen since at least 2015, designed specifically for targeting Linux systems. Reporting indicates the winnti malware family is shared across a number of actors including [Winnti Group](https://attack.mitre.org/groups/G0044). The Windows variant is tracked separately under [Winnti for Windows](https://attack.mitre.org/software/S0141).(Citation: Chronicle Winnti for Linux May 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--winterlove | WINTERLOVE | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--xdoor | XDoor | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--xmrig | Xmrig | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--zxshell | ZxShell | [ZxShell](https://attack.mitre.org/software/S0412) is a remote administration tool and backdoor that can be downloaded from the Internet, particularly from Chinese hacker websites. It has been used since at least 2004.(Citation: FireEye APT41 Aug 2019)(Citation: Talos ZxShell Oct 2014) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--certutil | certutil | [certutil](https://attack.mitre.org/software/S0160) is a command-line utility that can be used to obtain certificate authority information and configure Certificate Services. (Citation: TechNet Certutil) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--powersploit | PowerSploit | [PowerSploit](https://attack.mitre.org/software/S0194) is an open source, offensive security framework comprised of [PowerShell](https://attack.mitre.org/techniques/T1059/001) modules and scripts that perform a wide range of tasks related to penetration testing such as code execution, persistence, bypassing anti-virus, recon, and exfiltration. (Citation: GitHub PowerSploit May 2012) (Citation: PowerShellMagazine PowerSploit July 2014) (Citation: PowerSploit Documentation) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--impacket | Impacket | [Impacket](https://attack.mitre.org/software/S0357) is an open source collection of modules written in Python for programmatically constructing and manipulating network protocols. [Impacket](https://attack.mitre.org/software/S0357) contains several tools for remote service execution, Kerberos manipulation, Windows credential dumping, packet sniffing, and relay attacks.(Citation: Impacket Tools) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ipconfig | ipconfig | [ipconfig](https://attack.mitre.org/software/S0100) is a Windows utility that can be used to find information about a system's TCP/IP, DNS, DHCP, and adapter configuration. (Citation: TechNet Ipconfig) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--empire | Empire | [Empire](https://attack.mitre.org/software/S0363) is an open-source, cross-platform remote administration and post-exploitation framework that is publicly available on GitHub. While the tool itself is primarily written in Python, the post-exploitation agents are written in pure [PowerShell](https://attack.mitre.org/techniques/T1059/001) for Windows and Python for Linux/macOS. [Empire](https://attack.mitre.org/software/S0363) was one of five tools singled out by a joint report on public hacking tools being widely used by adversaries.(Citation: NCSC Joint Report Public Tools)(Citation: Github PowerShell Empire)(Citation: GitHub ATTACK Empire) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--dsquery | dsquery | [dsquery](https://attack.mitre.org/software/S0105) is a command-line utility that can be used to query Active Directory for information from a system within a domain. (Citation: TechNet Dsquery) It is typically installed only on Windows Server versions but can be installed on non-server variants through the Microsoft-provided Remote Server Administration Tools bundle. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--netstat | netstat | [netstat](https://attack.mitre.org/software/S0104) is an operating system utility that displays active TCP connections, listening ports, and network statistics. (Citation: TechNet Netstat) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--bitsadmin | BITSAdmin | [BITSAdmin](https://attack.mitre.org/software/S0190) is a command line tool used to create and manage [BITS Jobs](https://attack.mitre.org/techniques/T1197). (Citation: Microsoft BITSAdmin) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--sqlmap | sqlmap | [sqlmap](https://attack.mitre.org/software/S0225) is an open source penetration testing tool that can be used to automate the process of detecting and exploiting SQL injection flaws. (Citation: sqlmap Introduction) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--pwdump | pwdump | [pwdump](https://attack.mitre.org/software/S0006) is a credential dumper. (Citation: Wikipedia pwdump) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ping | Ping | [Ping](https://attack.mitre.org/software/S0097) is an operating system utility commonly used to troubleshoot and verify network connections. (Citation: TechNet Ping) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ftp | ftp | [ftp](https://attack.mitre.org/software/S0095) is a utility commonly available with operating systems to transfer information over the File Transfer Protocol (FTP). Adversaries can use it to transfer other tools onto a system or to exfiltrate data.(Citation: Microsoft FTP)(Citation: Linux FTP) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### インフラ

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| infra--apt41-compromised-government-site | Compromised Government Website Delivery Infrastructure | A compromised government website hosted the ZIP archive linked from spearphishing messages. | 2024-10 | 2024-10 | 高 | `source--gtig-apt41-toughprogress-2025` |
| infra--apt41-google-calendar-c2 | Attacker-Controlled Google Calendar C2 | TOUGHPROGRESS polled encrypted commands from Calendar event descriptions and wrote encrypted results to events. | 2024-10 | 2025-05-29 | 高 | `source--gtig-apt41-toughprogress-2025` |
| infra--apt41-free-hosting-delivery | Free Web Hosting Malware Delivery | APT41 used Cloudflare Workers, TryCloudflare, InfinityFree and URL shorteners to distribute multiple malware families. | 2024-08 | 2025-05-29 | 高 | `source--gtig-apt41-toughprogress-2025` |

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|
| 中国のAPT41が再び活動を再開し、企業を侵害 | intrusion | 不明 | 不明 | 2024-07-20 | APT41は世界中の複数の組織を侵害。 2023年以来、長期間にわたり不正アクセスを維持。機密データを抜き出すことに成功した。 イタリア、スペイン、台湾、トルコ、英国が主要ターゲット。 メディア、技術、自動車業界などが標的。 DUSTPANやDUSTTRAPなどのコードネームを持つカスタムツールと一般的な悪意のあるソフトウェアを使用。 | 高 | `source--daily-54c9607dee646f91a92f` |
| Winntiの新ツール「UNAPIMON」がセキュリティソフトウェアからマルウェアを隠蔽 | malware-campaign | 不明 | 不明 | 2024-04-04 | Winnti（APT41）が「UNAPIMON」という未文書化マルウェアを使用 マルウェアはセキュリティソフトウェアの検出を回避する UNAPIMONはAPI関数のフックを解除して検出を逃れる この技術はマイクロソフトのDetoursツールを利用 Trend Microが報告、ユニークな回避手法と評価 | 中 | `source--daily-e4bbba7003815c78f3af` |
| 中国のAPT41、DodgeBoxとMoonWalkでマルウェア兵器を強化 | infrastructure-operation | 不明 | 不明 | 2024-07-12 | 中国のAPT41がDodgeBoxとMoonWalkを用いてマルウェア攻撃を強化 DodgeBoxはMoonWalkバックドアを展開する新しいローダー MoonWalkはGoogle DriveをC2通信に利用 APT41は以前から企業や政府を標的にする活動で知られる DodgeBoxはDLLサイドローディングなどの技術を使用 | 高 | `source--daily-6f4ea1988c3e4d76819a` |
| Winnti APT41、日本企業を標的としたRevivalStoneサイバースパイ活動を展開 | cyber-espionage | 不明 | 不明 | 2025-02-19 | 中国系の脅威アクターであるWinnti（APT41）が、2024年3月に日本の製造、素材、エネルギー企業を標的とした「RevivalStone」と呼ばれる新たなキャンペーンを展開しました。 この活動は、Trend Microが「Earth Freybug」として追跡し、Cybereasonが「Operation CuckooBees」として報告しているものと重複しており、APT41のサブグループとみられる。 Winntiは、セキュリティソフトを回避し、重要情報を収集するためのカスタムツールセットを使用し、ステルス性の高い攻撃を行うことで知られています。 最新の攻撃では、未特定のERPシステムのSQLインジェクション脆弱性を悪用し、China ChopperやBehinderといったWebシェルを展開しました。 さらに、共有アカウントを利用してマネージドサービスプロバイダー（MSP）に侵入し、そのインフラを利用して他の3つの組織にマルウェアを拡散させました。 | 高 | `source--daily-936c9eb49c4d8dd15bb1` |
| 中国のハッキンググループがサイバースパイ活動で協力 | cyber-espionage | 不明 | 不明 | 2024-06-06 | 中国の国家支援ハッカーがサイバースパイ活動で協力。Sophosが「Crimson Palace」として追跡。 Sophosの報告によると、新しいマルウェアと3つの活動クラスターが確認された。この活動クラスタは単一の組織の下で集中的に調整され運用されている可能性が高い。 Mustang Panda、APT41などのグループが関与。 主なターゲットは東南アジアの政府機関。 高度な調整と検出回避戦術が用いられている。 | 中 | `source--daily-5bfba001a636c0367a16` |
| 中国のハッカーグループAPT41、台湾政府関連の研究所をShadowPadとCobalt Strikeで攻撃 | reported-activity | 不明 | 不明 | 2024-08-02 | 中国のハッカーグループAPT41、台湾政府関連の研究所をShadowPadとCobalt Strikeで攻撃 | 高 | `source--daily-84e64bef4061ae862a75` |
| 中国関与のAPT41、2025年交渉中に米通商当局者を標的 | phishing-campaign | 不明 | 不明 | 2025-09-11 | 米下院対中特別委がPRC関与の「進行中」の標的型スパイ活動を警告。 標点は通商政策・外交関係者、政府機関、業界団体、法律事務所など。 Moolenaar下院議員名義のメールでフィッシング。添付/リンクを開かせマルウェア展開を狙う。 目的は機微情報窃取。クラウド/開発者ツール悪用で痕跡隠蔽と持続化。 1月はZPMC名義の偽通知でM365資格情報窃取を試行。APT41関与と評価。 | 高 | `source--daily-455b7c4ce0212f6eaae6` |
| 中国のAPT41、活動を再開し企業を侵害 | cyber-espionage | 不明 | 不明 | 2024-07-20 | 中国の国家支援ハッカーグループAPT41が活動を再開し、企業を標的にしている。 攻撃は既知の脆弱性を悪用し、Citrix、F5、Zimbra、Microsoft Exchangeを標的にしている。 攻撃にはPantegana、Spark RAT、Cobalt Strike Beaconなどのツールが使用されている。 APT41は14か国で活動し、政府機関や企業を対象にしたサイバースパイ活動と金融目的のサイバー犯罪を行っている。 | 高 | `source--daily-6bbce1bee38d5532d1d5` |
| APT41、Googleカレンダーを悪用したステルス型C2通信を展開 | infrastructure-operation | 不明 | 不明 | 2025-05-30 | 中国の国家支援型ハッカーグループAPT41が、新たなマルウェア「ToughProgress」を使用し、Googleカレンダーをコマンド＆コントロール（C2）通信に悪用。 攻撃は、政府機関のウェブサイトを侵害し、ZIPアーカイブをホスト。アーカイブには、PDFを装ったLNKファイルと画像ファイルを偽装したペイロード、DLLファイルが含まれていた。 LNKファイルを実行すると、DLL「PlusDrop」が起動し、次段階の「PlusInject」をメモリ上で実行。これにより、最終的なペイロード「ToughProgress」が展開される。 「ToughProgress」は、Googleカレンダーの特定のイベントをポーリングし、イベントの説明欄に埋め込まれた暗号化されたコマンドを取得・実行。結果もカレンダーイベントに書き戻される。 Googleは、攻撃者が管理するGoogleカレンダーとWorkspaceアカウントを特定・削除し、Safe Browsingブロックリストを更新して対策を講じた。 | 高 | `source--daily-7e05524db14274790b02` |
| APT41：イタリア産業を標的とするKeyPlugの脅威 | cyber-espionage | 不明 | 不明 | 2024-05-24 | APT41がイタリアの産業を標的にKeyPlugを使用 KeyPlugは、WindowsとLinux両方で動作。構成によって異なるプロトコルでバックドア通信を行う。 数か月にわたってイタリアのさまざまな産業が攻撃を受けた。 APT41の攻撃動機はスパイ活動から金銭目的まで様々。この攻撃活動による目的は記載されていなかった。 | 高 | `source--daily-dbac07148e6695d210a9` |
| APT41 Winnti の ELF 型クラウド認証情報収集マルウェア：Alibaba のタイポスクワット基盤と 6 年にわたる系譜 | infrastructure-operation | 不明 | 不明 | 2026-04-14 | Breakglass Intelligence は、AWS、GCP、Azure、Alibaba Cloud 上の Linux ワークロードを狙う APT41(Winnti) の ELF バックドアを報告した。 このマルウェアはクラウド認証情報とメタデータを収集し、SMTP の 25/tcp を秘匿 C2 に使い、通常の HTTPS 通信を避ける設計になっている。 C2 サーバーは初回 EHLO に正しいトークンがない接続を遮断する選別型ハンドシェイクを実装し、Shodan や Censys から見えにくい。 関連基盤として Alibaba Cloud や Qianxin を装う 3 つのタイポスクワットドメインが 2026年1月20日から21日に集中登録されていた。 記事は、このサンプルを 2020年の PWNLNX から続く 6 年間の Winnti ELF 系譜上に位置付け、クラウド特化への進化とみなしている。 | 高 | `source--daily-2e4c99df2d0471e846db` |
| C0017 | campaign | 2021-05-01T04:00:00.000Z | 2022-02-01T05:00:00.000Z | 2026-05-12 | [C0017](https://attack.mitre.org/campaigns/C0017) was an [APT41](https://attack.mitre.org/groups/G0096) campaign conducted between May 2021 and February 2022 that successfully compromised at least six U.S. state government networks through the exploitation of vulnerable Internet facing web applications. During [C0017](https://attack.mitre.org/campaigns/C0017), [APT41](https://attack.mitre.org/groups/G0096) was quick to adapt and use publicly-disclosed as well as zero-day vulnerabilities for initial access, and in at least two cases re-compromised victims following remediation efforts. The goals of [C0017](https://attack.mitre.org/campaigns/C0017) are unknown, however [APT41](https://attack.mitre.org/groups/G0096) was observed exfiltrating Personal Identifiable Information (PII).(Citation: Mandiant APT41) | 高 | `source--mitre-attack-19-1` |
| APT41 DUST | campaign | 2023-01-31T23:00:00.000Z | 2024-06-30T22:00:00.000Z | 2026-05-12 | [APT41 DUST](https://attack.mitre.org/campaigns/C0040) was conducted by [APT41](https://attack.mitre.org/groups/G0096) from 2023 to July 2024 against entities in Europe, Asia, and the Middle East. [APT41 DUST](https://attack.mitre.org/campaigns/C0040) targeted sectors such as shipping, logistics, and media for information gathering purposes. [APT41](https://attack.mitre.org/groups/G0096) used previously-observed malware such as [DUSTPAN](https://attack.mitre.org/software/S1158) as well as newly observed tools such as [DUSTTRAP](https://attack.mitre.org/software/S1159) in [APT41 DUST](https://attack.mitre.org/campaigns/C0040).(Citation: Google Cloud APT41 2024) | 高 | `source--mitre-attack-19-1` |
| TOUGHPROGRESS Government Targeting Campaign | campaign | 2024-10 | 2024-10 | 2025-05-29 | APT41 spearphished government entities with a link to a ZIP on a compromised government site. An LNK masquerading as a PDF launched PLUSDROP, PLUSINJECT and TOUGHPROGRESS. | 高 | `source--gtig-apt41-toughprogress-2025` |

2024年10月、GTIGはAPT41が侵害済み政府サイトからLNKを含むZIPを配布し、PLUSDROP、PLUSINJECT、TOUGHPROGRESSを展開する活動を確認した。最終段はGoogle Calendarを暗号化C2として悪用した。

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | Government | The observed TOUGHPROGRESS campaign targeted multiple government entities. | 2024-10 | 2024-10 | 高 | `source--gtig-apt41-toughprogress-2025` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.001 | LSASS Memory | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.002 | Security Account Manager | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.003 | NTDS | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1008 | Fallback Channels | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1012 | Query Registry | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1014 | Rootkit | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027 | Obfuscated Files or Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.002 | Software Packing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1030 | Data Transfer Size Limits | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.004 | Masquerade Task or Service | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1037 | Boot or Logon Initialization Scripts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1046 | Network Service Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055 | Process Injection | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056.001 | Keylogging | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.004 | Unix Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1069 | Permission Groups Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.003 | Clear Command History | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.002 | File Transfer Protocols | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.004 | DNS | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.001 | Local Account | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090 | Proxy | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1098.007 | Additional Local or Domain Groups | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102.001 | Dead Drop Resolver | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1104 | Multi-Stage Channels | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110 | Brute Force | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence | T1133 | External Remote Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1135 | Network Share Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1136.001 | Local Account | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1195.002 | Compromise Software Supply Chain | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Stealth | T1197 | BITS Jobs | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1213.003 | Code Repositories | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.001 | Compiled HTML File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.011 | Rundll32 | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1480.001 | Environmental Keying | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Privilege Escalation | T1484.001 | Group Policy Modification | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1486 | Data Encrypted for Impact | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1496.001 | Compute Hijacking | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Stealth | T1542.003 | Bootkit | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1546.008 | Accessibility Features | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1550.002 | Pass the Hash | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1553.002 | Code Signing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555 | Credentials from Password Stores | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.003 | Credentials from Web Browsers | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1568.002 | Domain Generation Algorithms | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1569.002 | Service Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1570 | Lateral Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.006 | Dynamic Linker Hijacking | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1595.002 | Vulnerability Scanning | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1595.003 | Wordlist Scanning | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1596.005 | Scan Databases | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1599 | Network Boundary Bridging | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1684.001 | Impersonation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685.005 | Clear Windows Event Logs | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Phishing: Spearphishing Link | Sent spearphishing email links to a ZIP hosted on a compromised government website. | malware--plusdrop | activity--apt41-toughprogress-2024 | 2024-10 | 2024-10 | 高 | `source--gtig-apt41-toughprogress-2025` |
| Execution | T1204.002 | User Execution: Malicious File | A user clicking an LNK disguised as a PDF launched the infection chain. | malware--plusdrop | activity--apt41-toughprogress-2024 | 2024-10 | 2024-10 | 高 | `source--gtig-apt41-toughprogress-2025` |
| Defense Evasion, Privilege Escalation | T1055.012 | Process Injection: Process Hollowing | PLUSINJECT hollowed a legitimate svchost.exe process to inject TOUGHPROGRESS. | malware--plusinject, malware--toughprogress | activity--apt41-toughprogress-2024 | 2024-10 | 2024-10 | 高 | `source--gtig-apt41-toughprogress-2025` |
| Command and Control | T1102 | Web Service | TOUGHPROGRESS used attacker-controlled Google Calendar events for encrypted commands and command output. | malware--toughprogress | activity--apt41-toughprogress-2024 | 2024-10 | 2024-10 | 高 | `source--gtig-apt41-toughprogress-2025` |
| Defense Evasion | T1027 | Obfuscated Files or Information | The chain used encryption, compression, memory-only payloads and control-flow obfuscation. | malware--plusdrop, malware--toughprogress | activity--apt41-toughprogress-2024 | 2024-10 | 2024-10 | 高 | `source--gtig-apt41-toughprogress-2025` |

## IOC／artifact概要

- IOC値: 135件
- IOC観測: 143件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 17件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| APT41 continued to blend compromised sites and legitimate cloud services into its malware delivery and C2 chain in late 2024. | 高 | `source--gtig-apt41-toughprogress-2025` |  |
| MITRE states that APT41 overlaps at least partially with public reporting on Winnti Group. | 高 | `source--mitre-live-apt41-2025` | verification_status=supported; Partial overlap is not exact identity and does not imply all Winnti-umbrella activity is APT41. An exact-alias assertion would be stronger than the cited source supports. |

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--apt41--2c5b71a62ab2747a | With KEYPLUG,China’sRedGolf Spies On, Steals From Wide Field of Targets |  | 不明 | APT41/With KEYPLUG,China’sRedGolf Spies On, Steals From Wide Field of Targets.pdf | report | TLP:CLEAR | 中 |
| source--apt41--e93c4dbf79218d60 | README |  | 不明 | APT41/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--daily-2e4c99df2d0471e846db | APT41 Winnti の ELF 型クラウド認証情報収集マルウェア：Alibaba のタイポスクワット基盤と 6 年にわたる系譜 | intel.breakglass.tech | 2026-04-14 | https://intel.breakglass.tech/post/apt41-winnti-elf-cloud-credential-harvester-alibaba-typosquat | osint-report | TLP:CLEAR | 中 |
| source--daily-455b7c4ce0212f6eaae6 | 中国関与のAPT41、2025年交渉中に米通商当局者を標的 | thehackernews.com | 2025-09-11 | https://thehackernews.com/2025/09/china-linked-apt41-hackers-target-us.html | osint-report | TLP:CLEAR | 中 |
| source--daily-54c9607dee646f91a92f | 中国のAPT41が再び活動を再開し、企業を侵害 | security-next.com | 2024-07-20 | https://www.security-next.com/159902 | osint-report | TLP:CLEAR | 中 |
| source--daily-5bfba001a636c0367a16 | 中国のハッキンググループがサイバースパイ活動で協力 | bleepingcomputer.com | 2024-06-06 | https://www.bleepingcomputer.com/news/security/chinese-hacking-groups-team-up-in-cyber-espionage-campaign/ | osint-report | TLP:CLEAR | 中 |
| source--daily-6bbce1bee38d5532d1d5 | 中国のAPT41、活動を再開し企業を侵害 | cybernews.com | 2024-07-20 | https://cybernews.com/security/chinese-apt41-back-in-action-compromising-companies/ | osint-report | TLP:CLEAR | 中 |
| source--daily-6f4ea1988c3e4d76819a | 中国のAPT41、DodgeBoxとMoonWalkでマルウェア兵器を強化 | thehackernews.com | 2024-07-12 | https://thehackernews.com/2024/07/chinese-apt41-upgrades-malware-arsenal.html | osint-report | TLP:CLEAR | 中 |
| source--daily-7e05524db14274790b02 | APT41、Googleカレンダーを悪用したステルス型C2通信を展開 | bleepingcomputer.com | 2025-05-30 | https://www.bleepingcomputer.com/news/security/apt41-malware-abuses-google-calendar-for-stealthy-c2-communication/ | osint-report | TLP:CLEAR | 中 |
| source--daily-84e64bef4061ae862a75 | 中国のハッカーグループAPT41、台湾政府関連の研究所をShadowPadとCobalt Strikeで攻撃 | blog.talosintelligence.com | 2024-08-02 | https://blog.talosintelligence.com/chinese-hacking-group-apt41-compromised-taiwanese-government-affiliated-research-institute-with-shadowpad-and-cobaltstrike-2/ | osint-report | TLP:CLEAR | 中 |
| source--daily-936c9eb49c4d8dd15bb1 | Winnti APT41、日本企業を標的としたRevivalStoneサイバースパイ活動を展開 | thehackernews.com | 2025-02-19 | https://thehackernews.com/2025/02/winnti-apt41-targets-japanese-firms-in.html | osint-report | TLP:CLEAR | 中 |
| source--daily-dbac07148e6695d210a9 | APT41：イタリア産業を標的とするKeyPlugの脅威 | securityaffairs.com | 2024-05-24 | https://securityaffairs.com/163598/apt/apt41-keyplug-targets-italian-industries.html | osint-report | TLP:CLEAR | 中 |
| source--daily-e4bbba7003815c78f3af | Winntiの新ツール「UNAPIMON」がセキュリティソフトウェアからマルウェアを隠蔽 | bleepingcomputer.com | 2024-04-04 | https://www.bleepingcomputer.com/news/security/winntis-new-unapimon-tool-hides-malware-from-security-software/ | osint-report | TLP:CLEAR | 中 |
| source--gtig-apt41-toughprogress-2025 | Mark Your Calendar: APT41 Innovative Tactics | Google Threat Intelligence Group | 2025-05-29 | https://cloud.google.com/blog/topics/threat-intelligence/apt41-innovative-tactics/ | vendor-research | TLP:CLEAR | 高 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--mitre-live-apt41-2025 | APT41, Group G0096 | MITRE ATT&CK | 2025-06-11 | https://attack.mitre.org/groups/G0096/ | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
