# Threat Group-3390 脅威アクタープロファイル

- プロファイルID: `actor--threat-group-3390`
- 状態: draft
- 更新日時: 2026-07-29T23:13:55Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Threat Group-3390の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Threat Group-3390**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| APT27 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| BRONZE UNION | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| BRONZE UNION, TG-3390 | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Earth Smilodon | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Emissary Panda | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Group 35 | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Iron Tiger | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Linen Typhoon | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| LuckyMouse | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TEMP.Hippo | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TG-3390 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| ZipToken | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| ZipToken, Iron Tiger | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 49; mapping requires review. |
| DEV-0322, Earth Berberoka | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 49; mapping requires review. |

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
| Adversary | [Threat Group-3390](https://attack.mitre.org/groups/G0027) is a Chinese threat group that has extensively used strategic Web compromises to target victims.(Citation: Dell TG-3390) The group has been active since at least 2010 and has targeted organizations in the aerospace, government, defense, technology, energy, manufacturing and gambling/betting sectors.(Citation: SecureWorks BRONZE UNION June 2017)(Citation: Securelist LuckyMouse June 2018)(Citation: Trend Micro DRBControl February 2020) |
| Capability | RCSession, ASPXSpy, China Chopper, HyperBro, PlugX, Clambling, gh0st RAT, Pandora, Cobalt Strike, SysUpdate, ZxShell, HTTPBrowser, China Chopper Webshell, Hunter, ASPXTool, wce, htran, Net, certutil, Windows Credential Editor, Impacket, ipconfig, Tasklist, netstat, Systeminfo, pwdump, Mimikatz, gsecdump, NBTscan |
| Infrastructure |  |
| Victim | US Gov and contractors, Western think tanks, Gaming, iGaming, Gambling |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Emissary Panda, APT 27, LuckyMouse, Bronze Union | multiple-name-intersection | 高 | China | https://www.secureworks.com/research/threat-group-3390-targets-organizations-for-cyberespionage<br>https://www.secureworks.com/research/a-peek-into-bronze-unions-toolbox<br>https://www.secureworks.com/research/bronze-union |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Circle Typhoon | multiple-name-intersection | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| microsoft-threat-actor-mapping | Linen Typhoon | multiple-name-intersection | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | APT27 | multiple-name-intersection | 高 | CN, Unknown | https://i.blackhat.com/Asia-22/Friday-Materials/AS-22-Li-To-Loot-Or-Not-To-Loot-That-Is-Not-a-Question.pdf<br>https://web.archive.org/web/20140129192702/https://www.scmagazineuk.com/iran-and-russia-blamed-for-state-sponsored-espionage/article/330401/<br>https://labs.bitdefender.com/2018/02/operation-pzchao-a-possible-return-of-the-iron-tiger-apt/ |
| misp-microsoft-activity-group | Circle Typhoon | multiple-name-intersection | 高 | CN, China | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Linen Typhoon | multiple-name-intersection | 高 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | Threat Group-3390 - G0027 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0027<br>http://www.secureworks.com/cyber-threat-intelligence/threats/threat-group-3390-targets-organizations-for-cyberespionage/<br>https://www.secureworks.com/research/bronze-union |
| misp-mitre-intrusion-set | Threat Group-3390 - G0027 | mitre-external-id | 高 |  | http://arstechnica.com/security/2015/08/newly-discovered-chinese-hacking-group-hacked-100-websites-to-use-as-watering-holes/<br>https://attack.mitre.org/groups/G0027<br>https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf |
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
| malware--rcsession | RCSession | [RCSession](https://attack.mitre.org/software/S0662) is a backdoor written in C++ that has been in use since at least 2018 by [Mustang Panda](https://attack.mitre.org/groups/G0129) and by [Threat Group-3390](https://attack.mitre.org/groups/G0027) (Type II Backdoor).(Citation: Secureworks BRONZE PRESIDENT December 2019)(Citation: Trend Micro Iron Tiger April 2021)(Citation: Trend Micro DRBControl February 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--aspxspy | ASPXSpy | [ASPXSpy](https://attack.mitre.org/software/S0073) is a Web shell. It has been modified by [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors to create the ASPXTool version. (Citation: Dell TG-3390) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--china-chopper | China Chopper | [China Chopper](https://attack.mitre.org/software/S0020) is a [Web Shell](https://attack.mitre.org/techniques/T1505/003) hosted on Web servers to provide access back into an enterprise network that does not rely on an infected system calling back to a remote command and control server.(Citation: Lee 2013) It has been used by several threat groups.(Citation: Dell TG-3390)(Citation: FireEye Periscope March 2018)(Citation: CISA AA21-200A APT40 July 2021)(Citation: Rapid7 HAFNIUM Mar 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--hyperbro | HyperBro | [HyperBro](https://attack.mitre.org/software/S0398) is a custom in-memory backdoor used by [Threat Group-3390](https://attack.mitre.org/groups/G0027).(Citation: Unit42 Emissary Panda May 2019)(Citation: Securelist LuckyMouse June 2018)(Citation: Hacker News LuckyMouse June 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--plugx | PlugX | [PlugX](https://attack.mitre.org/software/S0013) is a remote access tool (RAT) with modular plugins that has been used by multiple threat groups.(Citation: Lastline PlugX Analysis)(Citation: FireEye Clandestine Fox Part 2)(Citation: New DragonOK)(Citation: Dell TG-3390) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--clambling | Clambling | [Clambling](https://attack.mitre.org/software/S0660) is a modular backdoor written in C++ that has been used by [Threat Group-3390](https://attack.mitre.org/groups/G0027) since at least 2017.(Citation: Trend Micro DRBControl February 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--gh0st-rat | gh0st RAT | [gh0st RAT](https://attack.mitre.org/software/S0032) is a remote access tool (RAT). The source code is public and it has been used by multiple groups.(Citation: FireEye Hacking Team)(Citation: Arbor Musical Chairs Feb 2018)(Citation: Nccgroup Gh0st April 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--pandora | Pandora | [Pandora](https://attack.mitre.org/software/S0664) is a multistage kernel rootkit with backdoor functionality that has been in use by [Threat Group-3390](https://attack.mitre.org/groups/G0027) since at least 2020.(Citation: Trend Micro Iron Tiger April 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--cobalt-strike | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) is a commercial, full-featured, remote access tool that bills itself as “adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors”. Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.(Citation: cobaltstrike manual)<br><br>In addition to its own capabilities, [Cobalt Strike](https://attack.mitre.org/software/S0154) leverages the capabilities of other well-known tools such as Metasploit and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: cobaltstrike manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--sysupdate | SysUpdate | [SysUpdate](https://attack.mitre.org/software/S0663) is a backdoor written in C++ that has been used by [Threat Group-3390](https://attack.mitre.org/groups/G0027) since at least 2020.(Citation: Trend Micro Iron Tiger April 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--zxshell | ZxShell | [ZxShell](https://attack.mitre.org/software/S0412) is a remote administration tool and backdoor that can be downloaded from the Internet, particularly from Chinese hacker websites. It has been used since at least 2004.(Citation: FireEye APT41 Aug 2019)(Citation: Talos ZxShell Oct 2014) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--httpbrowser | HTTPBrowser | [HTTPBrowser](https://attack.mitre.org/software/S0070) is malware that has been used by several threat groups. (Citation: ThreatStream Evasion Analysis) (Citation: Dell TG-3390) It is believed to be of Chinese origin. (Citation: ThreatConnect Anthem) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--china-chopper-webshell | China Chopper Webshell | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--hunter | Hunter | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--aspxtool | ASPXTool | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--wce | wce | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--htran | htran | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--certutil | certutil | [certutil](https://attack.mitre.org/software/S0160) is a command-line utility that can be used to obtain certificate authority information and configure Certificate Services. (Citation: TechNet Certutil) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--windows-credential-editor | Windows Credential Editor | [Windows Credential Editor](https://attack.mitre.org/software/S0005) is a password dumping tool. (Citation: Amplia WCE) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--impacket | Impacket | [Impacket](https://attack.mitre.org/software/S0357) is an open source collection of modules written in Python for programmatically constructing and manipulating network protocols. [Impacket](https://attack.mitre.org/software/S0357) contains several tools for remote service execution, Kerberos manipulation, Windows credential dumping, packet sniffing, and relay attacks.(Citation: Impacket Tools) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ipconfig | ipconfig | [ipconfig](https://attack.mitre.org/software/S0100) is a Windows utility that can be used to find information about a system's TCP/IP, DNS, DHCP, and adapter configuration. (Citation: TechNet Ipconfig) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--tasklist | Tasklist | The [Tasklist](https://attack.mitre.org/software/S0057) utility displays a list of applications and services with their Process IDs (PID) for all tasks running on either a local or a remote computer. It is packaged with Windows operating systems and can be executed from the command-line interface. (Citation: Microsoft Tasklist) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--netstat | netstat | [netstat](https://attack.mitre.org/software/S0104) is an operating system utility that displays active TCP connections, listening ports, and network statistics. (Citation: TechNet Netstat) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--systeminfo | Systeminfo | [Systeminfo](https://attack.mitre.org/software/S0096) is a Windows utility that can be used to gather detailed information about a computer. (Citation: TechNet Systeminfo) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--pwdump | pwdump | [pwdump](https://attack.mitre.org/software/S0006) is a credential dumper. (Citation: Wikipedia pwdump) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--gsecdump | gsecdump | [gsecdump](https://attack.mitre.org/software/S0008) is a publicly-available credential dumper used to obtain password hashes and LSA secrets from Windows operating systems. (Citation: TrueSec Gsecdump) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--nbtscan | NBTscan | [NBTscan](https://attack.mitre.org/software/S0590) is an open source tool that has been used by state groups to conduct internal reconnaissance within a compromised network.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan June 2003)(Citation: Symantec Waterbug Jun 2019)(Citation: FireEye APT39 Jan 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| A Tale of Two Targets | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| A Tale of Two Targets | Threat Group-3390 | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |

A Tale of Two Targets

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | イスラエル | 構造化OSINTの被害国フィールドでThreat Group-3390の標的・被害国としてイスラエルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | イラン | 構造化OSINTの被害国フィールドでThreat Group-3390の標的・被害国としてイランが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | インド | 構造化OSINTの被害国フィールドでThreat Group-3390の標的・被害国としてインドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | オーストラリア | 構造化OSINTの被害国フィールドでThreat Group-3390の標的・被害国としてオーストラリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | カナダ | 構造化OSINTの被害国フィールドでThreat Group-3390の標的・被害国としてカナダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | スペイン | 構造化OSINTの被害国フィールドでThreat Group-3390の標的・被害国としてスペインが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | タイ | 構造化OSINTの被害国フィールドでThreat Group-3390の標的・被害国としてタイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | トルコ | 構造化OSINTの被害国フィールドでThreat Group-3390の標的・被害国としてトルコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ドイツ | 構造化OSINTの被害国フィールドでThreat Group-3390の標的・被害国としてドイツが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フィリピン | 構造化OSINTの被害国フィールドでThreat Group-3390の標的・被害国としてフィリピンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フランス | 構造化OSINTの被害国フィールドでThreat Group-3390の標的・被害国としてフランスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | モンゴル | 構造化OSINTの被害国フィールドでThreat Group-3390の標的・被害国としてモンゴルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ロシア | 構造化OSINTの被害国フィールドでThreat Group-3390の標的・被害国としてロシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 中国 | 構造化OSINTの被害国フィールドでThreat Group-3390の標的・被害国として中国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 台湾 | 構造化OSINTの被害国フィールドでThreat Group-3390の標的・被害国として台湾が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 日本 | 構造化OSINTの被害国フィールドでThreat Group-3390の標的・被害国として日本が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 米国 | レビュー済みアクターマッピングの標的欄に記録された米国を構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 英国 | 構造化OSINTの被害国フィールドでThreat Group-3390の標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 韓国 | 構造化OSINTの被害国フィールドでThreat Group-3390の標的・被害国として韓国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 香港 | 構造化OSINTの被害国フィールドでThreat Group-3390の標的・被害国として香港が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | チベット | 構造化OSINTの被害地域フィールドでThreat Group-3390の標的範囲としてチベットが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 中東 | 構造化OSINTの被害地域フィールドでThreat Group-3390の標的範囲として中東が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 北米 | カナダ、米国で確認された標的・被害事例を北米として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 東アジア | モンゴル、中国、台湾、日本、韓国、香港で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 東南アジア | タイ、フィリピンで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 欧州 | スペイン、トルコ、ドイツ、フランス、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| sectors | エネルギー | ups/G0027) is a Chinese threat group that has extensively used strategic Web compromises to target victims.(Citation: Dell TG-3390) The group has been active since at least 2010 and has targeted organizations in the aerospace, government, defense, technology, energy, manufacturing and gambling/betting sectors.(Citation: SecureWorks BRONZE UNION June 2017)(Citation: Securelist LuckyMouse June 2018)(Citation: Trend Micro DRBControl February 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 政府・行政 | 390](https://attack.mitre.org/groups/G0027) is a Chinese threat group that has extensively used strategic Web compromises to target victims.(Citation: Dell TG-3390) The group has been active since at least 2010 and has targeted organizations in the aerospace, government, defense, technology, energy, manufacturing and gambling/betting sectors.(Citation: SecureWorks BRONZE UNION June 2017)(Citation: Securelist LuckyMouse June 2018)(Citation: Trend Micro DRBControl February 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 製造・産業 | 7) is a Chinese threat group that has extensively used strategic Web compromises to target victims.(Citation: Dell TG-3390) The group has been active since at least 2010 and has targeted organizations in the aerospace, government, defense, technology, energy, manufacturing and gambling/betting sectors.(Citation: SecureWorks BRONZE UNION June 2017)(Citation: Securelist LuckyMouse June 2018)(Citation: Trend Micro DRBControl February 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 防衛・軍事 | eat Group-3390](https://attack.mitre.org/groups/G0027) is a Chinese threat group that has extensively used strategic Web compromises to target victims.(Citation: Dell TG-3390) The group has been active since at least 2010 and has targeted organizations in the aerospace, government, defense, technology, energy, manufacturing and gambling/betting sectors.(Citation: SecureWorks BRONZE UNION June 2017)(Citation: Securelist LuckyMouse June 2018)(Citation: Trend Micro DRBControl February 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003 | OS Credential Dumping | DEINFO payload on the compromised machines. They also made use of previously undocumented malware, which we named MirrorStealer, to steal victims’ credentials (T1003 [8]). LuckyMouse In September 2022, a gambling company in Hong Kong was compromised via a malicious update pushed by the EsafeNet Cobra DocGuard Client (T1195.002 [9]). This victim was compromised by LuckyMouse using the same techniqu |  |  | 不明 | 不明 | 中 | `source--threat-group-3390--d3fae7c81ec01a26` |
| Credential Access | T1003.001 | LSASS Memory | [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors have used a modified version of [Mimikatz](https://attack.mitre.org/software/S0002) called Wrapikatz to dump credentials. They have also dumped credentials from domain controllers.(Citation: Dell TG-3390)(Citation: SecureWorks BRONZE UNION June 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.002 | Security Account Manager | [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors have used [gsecdump](https://attack.mitre.org/software/S0008) to dump credentials. They have also dumped credentials from domain controllers.(Citation: Dell TG-3390)(Citation: SecureWorks BRONZE UNION June 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.004 | LSA Secrets | [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors have used [gsecdump](https://attack.mitre.org/software/S0008) to dump credentials. They have also dumped credentials from domain controllers.(Citation: Dell TG-3390)(Citation: SecureWorks BRONZE UNION June 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | [Threat Group-3390](https://attack.mitre.org/groups/G0027) ran a command to compile an archive of file types of interest from the victim user's directories.(Citation: SecureWorks BRONZE UNION June 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1012 | Query Registry | A [Threat Group-3390](https://attack.mitre.org/groups/G0027) tool can read and decrypt stored Registry values.(Citation: Nccgroup Emissary Panda May 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors use [NBTscan](https://attack.mitre.org/software/S0590) to discover vulnerable systems.(Citation: Dell TG-3390) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used the <code>net view</code> command.(Citation: Nccgroup Emissary Panda May 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.006 | Windows Remote Management | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used WinRM to enable remote execution.(Citation: SecureWorks BRONZE UNION June 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.002 | Software Packing | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has packed malware and tools, including using VMProtect.(Citation: Trend Micro DRBControl February 2020)(Citation: Trend Micro Iron Tiger April 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | A [Threat Group-3390](https://attack.mitre.org/groups/G0027) tool can encrypt payloads using XOR. [Threat Group-3390](https://attack.mitre.org/groups/G0027) malware is also obfuscated using Metasploit’s shikata_ga_nai encoder.(Citation: Nccgroup Emissary Panda May 2018)(Citation: Securelist LuckyMouse June 2018)(Citation: Unit42 Emissary Panda May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.015 | Compression | [Threat Group-3390](https://attack.mitre.org/groups/G0027) malware is compressed with LZNT1 compression.(Citation: Nccgroup Emissary Panda May 2018)(Citation: Securelist LuckyMouse June 2018)(Citation: Unit42 Emissary Panda May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1030 | Data Transfer Size Limits | [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors have split RAR files for exfiltration into parts.(Citation: Dell TG-3390) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used `whoami` to collect system user information.(Citation: Trend Micro DRBControl February 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1046 | Network Service Discovery | [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors use the Hunter tool to conduct network service discovery for vulnerable systems.(Citation: Dell TG-3390)(Citation: Unit42 Emissary Panda May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | A [Threat Group-3390](https://attack.mitre.org/groups/G0027) tool can use WMI to execute a binary.(Citation: Nccgroup Emissary Panda May 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used `net use` and `netstat` to conduct internal discovery of systems. The group has also used `quser.exe` to identify existing RDP sessions on a victim.(Citation: SecureWorks BRONZE UNION June 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.002 | At | [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors use [at](https://attack.mitre.org/software/S0110) to schedule tasks to run self-extracting RAR archives, which install [HTTPBrowser](https://attack.mitre.org/software/S0070) or [PlugX](https://attack.mitre.org/software/S0013) on other victims on a network.(Citation: Dell TG-3390) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055.012 | Process Hollowing | A [Threat Group-3390](https://attack.mitre.org/groups/G0027) tool can spawn `svchost.exe` and inject the payload into that process.(Citation: Nccgroup Emissary Panda May 2018)(Citation: Securelist LuckyMouse June 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056.001 | Keylogging | [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors installed a credential logger on Microsoft Exchange servers. [Threat Group-3390](https://attack.mitre.org/groups/G0027) also leveraged the reconnaissance framework, ScanBox, to capture keystrokes.(Citation: Dell TG-3390)(Citation: Hacker News LuckyMouse June 2018)(Citation: Securelist LuckyMouse June 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used PowerShell for execution.(Citation: SecureWorks BRONZE UNION June 2017)(Citation: Trend Micro DRBControl February 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used command-line interfaces for execution.(Citation: SecureWorks BRONZE UNION June 2017)(Citation: Unit42 Emissary Panda May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1068 | Exploitation for Privilege Escalation | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used CVE-2014-6324 and CVE-2017-0213 to escalate privileges.(Citation: SecureWorks BRONZE UNION June 2017)(Citation: Profero APT27 December 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has deleted existing logs and exfiltrated file archives from a victim.(Citation: SecureWorks BRONZE UNION June 2017)(Citation: Trend Micro DRBControl February 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.005 | Network Share Connection Removal | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has detached network shares after exfiltrating files, likely to evade detection.(Citation: SecureWorks BRONZE UNION June 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [Threat Group-3390](https://attack.mitre.org/groups/G0027) malware has used HTTP for C2.(Citation: Securelist LuckyMouse June 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has locally staged encrypted archives for later exfiltration efforts.(Citation: SecureWorks BRONZE UNION June 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.002 | Remote Data Staging | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has moved staged encrypted archives to Internet-facing servers that had previously been compromised with [China Chopper](https://attack.mitre.org/software/S0020) prior to exfiltration.(Citation: SecureWorks BRONZE UNION June 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors obtain legitimate credentials using a variety of methods and use them to further lateral movement on victim networks.(Citation: Dell TG-3390) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.001 | Local Account | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used <code>net user</code> to conduct internal discovery of systems.(Citation: SecureWorks BRONZE UNION June 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has downloaded additional malware and tools, including through the use of `certutil`, onto a compromised host .(Citation: Dell TG-3390)(Citation: Trend Micro DRBControl February 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | A [Threat Group-3390](https://attack.mitre.org/groups/G0027) tool has created new Registry keys under `HKEY_CURRENT_USER\Software\Classes\` and `HKLM\SYSTEM\CurrentControlSet\services`.(Citation: Nccgroup Emissary Panda May 2018)(Citation: Trend Micro Iron Tiger April 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1119 | Automated Collection | [Threat Group-3390](https://attack.mitre.org/groups/G0027) ran a command to compile an archive of file types of interest from the victim user's directories.(Citation: SecureWorks BRONZE UNION June 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence | T1133 | External Remote Services | [Threat Group-3390](https://attack.mitre.org/groups/G0027) actors look for and use VPN profiles during an operation to access the network using external VPN services.(Citation: Dell TG-3390) [Threat Group-3390](https://attack.mitre.org/groups/G0027) has also obtained OWA account credentials during intrusions that it subsequently used to attempt to regain access when evicted from a victim network.(Citation: SecureWorks BRONZE UNION June 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | During execution, [Threat Group-3390](https://attack.mitre.org/groups/G0027) malware deobfuscates and decompresses code that was encoded with Metasploit’s shikata_ga_nai encoder as well as compressed with LZNT1 compression.(Citation: Securelist LuckyMouse June 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1189 | Drive-by Compromise | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has extensively used strategic web compromises to target victims.(Citation: Dell TG-3390)(Citation: Securelist LuckyMouse June 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has exploited the Microsoft SharePoint vulnerability CVE-2019-0604 and CVE-2021-26855, CVE-2021-26857, CVE-2021-26858, and CVE-2021-27065 in Exchange Server.(Citation: Trend Micro Iron Tiger April 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1195.002 | Compromise Software Supply Chain | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has compromised the Able Desktop installer to gain access to victim's environments.(Citation: Trend Micro Iron Tiger April 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--threat-group-3390--d3fae7c81ec01a26` |
| Initial Access | T1199 | Trusted Relationship | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has compromised third party service providers to gain access to victim's environments.(Citation: Profero APT27 December 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has exploited CVE-2018-0798 in Equation Editor.(Citation: Trend Micro Iron Tiger April 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has lured victims into opening malicious files containing malware.(Citation: Trend Micro DRBControl February 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1210 | Exploitation of Remote Services | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has exploited MS17-010 to move laterally to other systems on the network.(Citation: Unit42 Emissary Panda May 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used a variety of Web shells.(Citation: Unit42 Emissary Panda May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | [Threat Group-3390](https://attack.mitre.org/groups/G0027)'s malware can create a new service, sometimes naming it after the config information, to gain persistence.(Citation: Nccgroup Emissary Panda May 2018)(Citation: Lunghi Iron Tiger Linux) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [Threat Group-3390](https://attack.mitre.org/groups/G0027)'s malware can add a Registry key to `Software\Microsoft\Windows\CurrentVersion\Run` for persistence.(Citation: Nccgroup Emissary Panda May 2018)(Citation: Lunghi Iron Tiger Linux) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1548.002 | Bypass User Account Control | A [Threat Group-3390](https://attack.mitre.org/groups/G0027) tool can use a public UAC bypass method to elevate privileges.(Citation: Nccgroup Emissary Panda May 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.005 | Password Managers | [Threat Group-3390](https://attack.mitre.org/groups/G0027) obtained a KeePass database from a compromised host.(Citation: Trend Micro DRBControl February 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.002 | Archive via Library | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used RAR to compress, encrypt, and password-protect files prior to exfiltration.(Citation: SecureWorks BRONZE UNION June 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used e-mail to deliver malicious attachments to victims.(Citation: Trend Micro DRBControl February 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has exfiltrated stolen data to Dropbox.(Citation: Trend Micro DRBControl February 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has performed DLL search order hijacking to execute their payload.(Citation: Nccgroup Emissary Panda May 2018) [Threat Group-3390](https://attack.mitre.org/groups/G0027) has also used DLL side-loading, including by using legitimate Kaspersky antivirus variants as well as `rc.exe`, a legitimate Microsoft Resource Compiler.(Citation: Dell TG-3390)(Citation: SecureWorks BRONZE UNION June 2017)(Citation: Securelist LuckyMouse June 2018)(Citation: Unit42 Emissary Panda May 2019)(Citation: Lunghi Iron Tiger Linux) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has registered domains for C2.(Citation: Lunghi Iron Tiger Linux) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has obtained and used tools such as [Impacket](https://attack.mitre.org/software/S0357), [pwdump](https://attack.mitre.org/software/S0006), [Mimikatz](https://attack.mitre.org/software/S0002), [gsecdump](https://attack.mitre.org/software/S0008), [NBTscan](https://attack.mitre.org/software/S0590), and [Windows Credential Editor](https://attack.mitre.org/software/S0005).(Citation: Unit42 Emissary Panda May 2019)(Citation: Dell TG-3390) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.003 | Code Signing Certificates | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has obtained stolen valid certificates, including from VMProtect and the Chinese instant messaging application Youdu, for their operations.(Citation: Lunghi Iron Tiger Linux) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.001 | Upload Malware | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has hosted malicious payloads on Dropbox.(Citation: Trend Micro DRBControl February 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.002 | Upload Tool | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has staged tools, including [gsecdump](https://attack.mitre.org/software/S0008) and WCE, on previously compromised websites.(Citation: Dell TG-3390) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.004 | Drive-by Target | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has embedded malicious code into websites to screen a potential victim's IP address and then exploit their browser if they are of interest.(Citation: Gallagher 2015) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685.001 | Disable or Modify Windows Event Log | [Threat Group-3390](https://attack.mitre.org/groups/G0027) has used appcmd.exe to disable logging on a victim server.(Citation: SecureWorks BRONZE UNION June 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 73件（`artifacts.csv`）

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
| source--threat-group-3390--d3fae7c81ec01a26 | threat group 3390 |  | 不明 | actor_profile/evidence/threat-group-3390.csv | structured-data | TLP:CLEAR | 中 |
| source--threat-group-3390--1fa2ae74e748412e | Booz Allen Hamilton |  | 不明 | AISecurity/2026/Booz Allen Hamilton.pdf | report | TLP:CLEAR | 中 |
| source--threat-group-3390--8fa35fcbbcf46804 | hunting cobaltstrike beacons in the dark |  | 不明 | APT-hunting/hunting-cobaltstrike-beacons-in-the-dark.pdf | report | TLP:CLEAR | 中 |
| source--threat-group-3390--de9d752da0a18c78 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--threat-group-3390--7c865dc39b1f6943 | A three beat waltz The ecosystem behind Chinese state sponsored cyber threats |  | 不明 | International Strategic/China/A-three-beat-waltz-The-ecosystem-behind-Chinese-state-sponsored-cyber-threats.pdf | report | TLP:CLEAR | 中 |
| source--threat-group-3390--335d77244647a7c1 | Charting China’s Climb as a Leading Global Cyber Power |  | 不明 | International Strategic/China/Charting China’s Climb as a Leading Global Cyber Power.pdf | report | TLP:CLEAR | 中 |
| source--threat-group-3390--6c7294abe828da29 | china cyber report |  | 不明 | International Strategic/China/china-cyber-report.pdf | report | TLP:CLEAR | 中 |
| source--threat-group-3390--ba3221cc22c87d05 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--threat-group-3390--b958899ba10144ea | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--threat-group-3390--ea17a3a26249f478 | The CrowdStrike 2021 Global Threat Report |  | 2021 | summary/2021/The CrowdStrike 2021 Global Threat Report.pdf | report | TLP:CLEAR | 中 |
| source--threat-group-3390--fcb97139fbeb3b28 | eset threat report t12021 |  | 不明 | summary/2021/eset_threat_report_t12021.pdf | report | TLP:CLEAR | 中 |
| source--threat-group-3390--a500d0549f9223c8 | mpressioncss ta report 2020 5 en |  | 2020 | summary/2021/mpressioncss_ta_report_2020_5_en.pdf | report | TLP:CLEAR | 中 |
| source--threat-group-3390--13ae8f99e17325d6 | 2021 Vulnerability Landscape |  | 2021 | summary/2022/2021 Vulnerability Landscape.pdf | report | TLP:CLEAR | 中 |
| source--threat-group-3390--830e2d2f23d7dfa8 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--threat-group-3390--45fecafc123c4c6d | 2022 year in retrospect report |  | 2022 | summary/2023/2022-year-in-retrospect-report.pdf | report | TLP:CLEAR | 中 |
| source--threat-group-3390--8ca2869d9015bdb8 | Modern Asian APT groups TTPs report eng |  | 不明 | summary/2023/Modern-Asian-APT-groups-TTPs_report_eng.pdf | report | TLP:CLEAR | 中 |
| source--threat-group-3390--7736fc1eb03694c3 | eset apt activity report t32022 |  | 不明 | summary/2023/eset_apt_activity_report_t32022.pdf | report | TLP:CLEAR | 中 |
| source--threat-group-3390--0939acf155fa2b77 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--threat-group-3390--c0c2a237abfbad6a | Raport analize PROFILI I GRUPEVE TE HAKERAVE IRANIANE |  | 不明 | summary/2024/Raport-analize-PROFILI-I-GRUPEVE-TE-HAKERAVE-IRANIANE.pdf | report | TLP:CLEAR | 中 |
| source--threat-group-3390--c0a7e2c6d105443c | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--threat-group-3390--8a8df0cccce4ef82 | SixMap Research Energy Sector Exposure Assessment |  | 不明 | summary/2025/SixMap-Research_Energy-Sector-Exposure-Assessment.pdf | report | TLP:CLEAR | 中 |
| source--threat-group-3390--565bde59f549433e | UK NCC Group Cyber Threat Intelligence Report September 2025 |  | 2025 | summary/2025/UK_NCC_Group_Cyber_Threat_Intelligence_Report_September_2025_.pdf | report | TLP:CLEAR | 中 |
| source--threat-group-3390--69487211d666a7d0 | eset apt activity report q4 2024 q1 2025 |  | 2024 | summary/2025/eset-apt-activity-report-q4-2024-q1-2025.pdf | report | TLP:CLEAR | 中 |
| source--threat-group-3390--f2223f73e65ec67f | Bridewell 2026 Cyber Threat Intelligence Report |  | 2026 | summary/2026/Bridewell 2026 Cyber Threat Intelligence Report.pdf | report | TLP:CLEAR | 中 |
| source--threat-group-3390--a56de8b81487164a | Cloudflare 2026 threat report |  | 2026 | summary/2026/Cloudflare-2026-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
