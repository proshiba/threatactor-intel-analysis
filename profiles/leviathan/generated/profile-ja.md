# Leviathan 脅威アクタープロファイル

- プロファイルID: `actor--leviathan`
- 状態: draft
- 更新日時: 2026-07-29T23:12:00Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Leviathanの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Leviathan**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| APT40 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| BRONZE MOHAWK | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Gadolinium | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Gingham Typhoon | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Hainan Xiandun Technology Company | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Kryptonite Panda | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| MUDCARP | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Red Ladon | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| ScanBox | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TA423 | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Temp.Jumper | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TEMP.Periscope | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Temp.Jumper, GADOLINIUM, MUDCARP, Hainan Xiandun Technology Company, TA423, Red Ladon, ScanBox | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 39; mapping requires review. |

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
| Adversary | [Leviathan](https://attack.mitre.org/groups/G0065) is a Chinese state-sponsored cyber espionage group that has been attributed to the Ministry of State Security's (MSS) Hainan State Security Department and an affiliated front company.(Citation: CISA AA21-200A APT40 July 2021) Active since at least 2009, [Leviathan](https://attack.mitre.org/groups/G0065) has targeted the following sectors: academia, aerospace/aviation, biomedical, defense industrial base, government, healthcare, manufacturing, maritime, and transportation across the US, Canada, Australia, Europe, the Middle East, and Southeast Asia.(Citation: CISA AA21-200A APT40 July 2021)(Citation: Proofpoint Leviathan Oct 2017)(Citation: FireEye Periscope March 2018)(Citation: CISA Leviathan 2024) |
| Capability | MURKYTOP, Orz, BADFLICK, China Chopper, NanHaiShu, HOMEFRY, gh0st RAT, Derusbi, Cobalt Strike, BLACKCOFFEE, AIRBREAK, PHOTO, LUNCHMONEY, Beacon, CVE-2017-11882, RoyalRoad RTF Weaponizer, Net, at, PowerSploit, Windows Credential Editor, Empire, BITSAdmin, Tor |
| Infrastructure |  |
| Victim | maritime-related targets across multiple verticals, including engineering firms, shipping and transportation, manufacturing, defense, government offices, and research universities |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Leviathan, APT 40, TEMP.Periscope | canonical-name | 高 | China | https://www.fireeye.com/blog/threat-research/2019/03/apt40-examining-a-china-nexus-espionage-actor.html<br>https://intrusiontruth.wordpress.com/2020/01/09/what-is-the-hainan-xiandun-technology-development-company/<br>https://intrusiontruth.wordpress.com/2020/01/10/who-is-mr-gu/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Gingham Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | APT40 | canonical-name | 高 | CN, China | https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets<br>https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html<br>https://www.cfr.org/interactive/cyber-operations/apt-40 |
| misp-microsoft-activity-group | GADOLINIUM | single-alias-intersection | 中 |  | https://www.microsoft.com/security/blog/2020/09/24/gadolinium-detecting-empires-cloud/ |
| misp-microsoft-activity-group | Gingham Typhoon | canonical-name | 高 | CN, China | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | Leviathan - G0065 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0065<br>https://www.proofpoint.com/us/threat-insight/post/leviathan-espionage-actor-spearphishes-maritime-and-defense-targets<br>https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html |
| misp-mitre-intrusion-set | Leviathan - G0065 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0065<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://us-cert.cisa.gov/ncas/alerts/aa21-200a |
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
| malware--murkytop | MURKYTOP | [MURKYTOP](https://attack.mitre.org/software/S0233) is a reconnaissance tool used by [Leviathan](https://attack.mitre.org/groups/G0065). (Citation: FireEye Periscope March 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--orz | Orz | [Orz](https://attack.mitre.org/software/S0229) is a custom JavaScript backdoor used by [Leviathan](https://attack.mitre.org/groups/G0065). It was observed being used in 2014 as well as in August 2017 when it was dropped by Microsoft Publisher files. (Citation: Proofpoint Leviathan Oct 2017) (Citation: FireEye Periscope March 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--badflick | BADFLICK | [BADFLICK](https://attack.mitre.org/software/S0642) is a backdoor used by [Leviathan](https://attack.mitre.org/groups/G0065) in spearphishing campaigns first reported in 2018 that targeted the U.S. engineering and maritime industries.(Citation: FireEye Periscope March 2018)(Citation: Accenture MUDCARP March 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--china-chopper | China Chopper | [China Chopper](https://attack.mitre.org/software/S0020) is a [Web Shell](https://attack.mitre.org/techniques/T1505/003) hosted on Web servers to provide access back into an enterprise network that does not rely on an infected system calling back to a remote command and control server.(Citation: Lee 2013) It has been used by several threat groups.(Citation: Dell TG-3390)(Citation: FireEye Periscope March 2018)(Citation: CISA AA21-200A APT40 July 2021)(Citation: Rapid7 HAFNIUM Mar 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--nanhaishu | NanHaiShu | [NanHaiShu](https://attack.mitre.org/software/S0228) is a remote access tool and JScript backdoor used by [Leviathan](https://attack.mitre.org/groups/G0065). [NanHaiShu](https://attack.mitre.org/software/S0228) has been used to target government and private-sector organizations that have relations to the South China Sea dispute. (Citation: Proofpoint Leviathan Oct 2017) (Citation: fsecure NanHaiShu July 2016) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--homefry | HOMEFRY | [HOMEFRY](https://attack.mitre.org/software/S0232) is a 64-bit Windows password dumper/cracker that has previously been used in conjunction with other [Leviathan](https://attack.mitre.org/groups/G0065) backdoors. (Citation: FireEye Periscope March 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--gh0st-rat | gh0st RAT | [gh0st RAT](https://attack.mitre.org/software/S0032) is a remote access tool (RAT). The source code is public and it has been used by multiple groups.(Citation: FireEye Hacking Team)(Citation: Arbor Musical Chairs Feb 2018)(Citation: Nccgroup Gh0st April 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--derusbi | Derusbi | [Derusbi](https://attack.mitre.org/software/S0021) is malware used by multiple Chinese APT groups.(Citation: Novetta-Axiom)(Citation: ThreatConnect Anthem) Both Windows and Linux variants have been observed.(Citation: Fidelis Turbo) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--cobalt-strike | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) is a commercial, full-featured, remote access tool that bills itself as “adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors”. Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.(Citation: cobaltstrike manual)<br><br>In addition to its own capabilities, [Cobalt Strike](https://attack.mitre.org/software/S0154) leverages the capabilities of other well-known tools such as Metasploit and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: cobaltstrike manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--blackcoffee | BLACKCOFFEE | [BLACKCOFFEE](https://attack.mitre.org/software/S0069) is malware that has been used by several Chinese groups since at least 2013. (Citation: FireEye APT17) (Citation: FireEye Periscope March 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--airbreak | AIRBREAK | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--photo | PHOTO | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--lunchmoney | LUNCHMONEY | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--beacon | Beacon | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--cve-2017-11882 | CVE-2017-11882 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--royalroad-rtf-weaponizer | RoyalRoad RTF Weaponizer | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--at | at | [at](https://attack.mitre.org/software/S0110) is used to schedule tasks on a system to run at a specified date or time.(Citation: TechNet At)(Citation: Linux at) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--powersploit | PowerSploit | [PowerSploit](https://attack.mitre.org/software/S0194) is an open source, offensive security framework comprised of [PowerShell](https://attack.mitre.org/techniques/T1059/001) modules and scripts that perform a wide range of tasks related to penetration testing such as code execution, persistence, bypassing anti-virus, recon, and exfiltration. (Citation: GitHub PowerSploit May 2012) (Citation: PowerShellMagazine PowerSploit July 2014) (Citation: PowerSploit Documentation) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--windows-credential-editor | Windows Credential Editor | [Windows Credential Editor](https://attack.mitre.org/software/S0005) is a password dumping tool. (Citation: Amplia WCE) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--empire | Empire | [Empire](https://attack.mitre.org/software/S0363) is an open-source, cross-platform remote administration and post-exploitation framework that is publicly available on GitHub. While the tool itself is primarily written in Python, the post-exploitation agents are written in pure [PowerShell](https://attack.mitre.org/techniques/T1059/001) for Windows and Python for Linux/macOS. [Empire](https://attack.mitre.org/software/S0363) was one of five tools singled out by a joint report on public hacking tools being widely used by adversaries.(Citation: NCSC Joint Report Public Tools)(Citation: Github PowerShell Empire)(Citation: GitHub ATTACK Empire) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--bitsadmin | BITSAdmin | [BITSAdmin](https://attack.mitre.org/software/S0190) is a command line tool used to create and manage [BITS Jobs](https://attack.mitre.org/techniques/T1197). (Citation: Microsoft BITSAdmin) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--tor | Tor | [Tor](https://attack.mitre.org/software/S0183) is a software suite and network that provides increased anonymity on the Internet. It creates a multi-hop proxy network and utilizes multilayer encryption to protect both the message and routing information. [Tor](https://attack.mitre.org/software/S0183) utilizes "Onion Routing," in which messages are encrypted with multiple layers of encryption; at each step in the proxy network, the topmost layer is decrypted and the contents forwarded on to the next node until it reaches its destination. (Citation: Dingledine Tor The Second-Generation Onion Router) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| Leviathan Australian Intrusions | campaign | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 2026-05-12 | target--mitre-group--country--4fabe7d586d1591c953e |  | ttp--activity-rule--7b161e2dd2783fd8def0, ttp--mitre-campaign--040a9e5527da36ef102f, ttp--mitre-campaign--0faf84021505e1cc0e12, ttp--mitre-campaign--187f9d121d77791a29cb, ttp--mitre-campaign--1a625a0af199c865a5f2, ttp--mitre-campaign--203982771da558165f46, ttp--mitre-campaign--291cbebad14f781d9e5f, ttp--mitre-campaign--301e1358e0f179779be9, ttp--mitre-campaign--4225beaf8d52820fd11e, ttp--mitre-campaign--458f37ee9c31cd960234, ttp--mitre-campaign--557f5a195d073bde6530, ttp--mitre-campaign--5bb0c25759be88aba1f1, ttp--mitre-campaign--68f230ae9f7be0d7e4d2, ttp--mitre-campaign--7b161e2dd2783fd8def0, ttp--mitre-campaign--7cbfd9c11e236f02df12, ttp--mitre-campaign--8720cfc5eeec7fc8d0c7, ttp--mitre-campaign--9fb8ab89ea9e9e26447b, ttp--mitre-campaign--a07899a6df3209a4af7d, ttp--mitre-campaign--b3666c7bfd9b0b84ab13, ttp--mitre-campaign--b42a2396ecb73006644e, ttp--mitre-campaign--b77d64a6478daf8325fd, ttp--mitre-campaign--cd9e5136ab9f22147cad, ttp--mitre-campaign--dba5b1e61643b94087cf, ttp--mitre-campaign--f9344a6478c31b3cd303, ttp--mitre-campaign--ff786d4885b2a458ebd0, ttp--mitre-campaign--ff8f6b83553531050cc1, ttp--mitre-campaign--ffe9c75146a30e398fb5 | victim--activity-rule--80dd52ed5da841845027 | [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049) consisted of at least two long-term intrusions against victims in Australia by [Leviathan](https://attack.mitre.org/groups/G0065), relying on similar tradecraft such as external service exploitation followed by extensive credential capture and re-use to enable privilege escalation and lateral movement. [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049) were focused on exfiltrating sensitive data including valid credentials for the victim organizations.(Citation: CISA Leviathan 2024) | 高 | `source--mitre-attack-19-1` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| Leviathan Australian Intrusions | Leviathan | 情報なし | T1078 Valid Accounts, T1078.003 Local Accounts, T1082 System Information Discovery, T1558.003 Kerberoasting, T1135 Network Share Discovery, T1588.006 Vulnerabilities, T1021.004 SSH, T1190 Exploit Public-Facing Application, T1056 Input Capture, T1482 Domain Trust Discovery, T1594 Search Victim-Owned Websites, T1505.003 Web Shell, T1041 Exfiltration Over C2 Channel, T1078 Valid Accounts, T1074.001 Local Data Staging, T1213.006 Databases, T1111 Multi-Factor Authentication Interception, T1686 Disable or Modify System Firewall, T1615 Group Policy Discovery, T1018 Remote System Discovery, T1068 Exploitation for Privilege Escalation, T1021.002 SMB/Windows Admin Shares, T1552 Unsecured Credentials, T1552.001 Credentials In Files, T1528 Steal Application Access Token, T1078.002 Domain Accounts, T1212 Exploitation for Credential Access | 情報なし | オーストラリア | 被害事例: Leviathan Australian Intrusions | 高 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | インドネシア | 構造化OSINTの被害国フィールドでLeviathanの標的・被害国としてインドネシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オーストラリア | at least 2009, [Leviathan](https://attack.mitre.org/groups/G0065) has targeted the following sectors: academia, aerospace/aviation, biomedical, defense industrial base, government, healthcare, manufacturing, maritime, and transportation across the US, Canada, Australia, Europe, the Middle East, and Southeast Asia.(Citation: CISA AA21-200A APT40 July 2021)(Citation: Proofpoint Leviathan Oct 2017)(Citation: FireEye Periscope March 2018)(Citation: CISA Leviathan 2024) | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| countries | カナダ | e since at least 2009, [Leviathan](https://attack.mitre.org/groups/G0065) has targeted the following sectors: academia, aerospace/aviation, biomedical, defense industrial base, government, healthcare, manufacturing, maritime, and transportation across the US, Canada, Australia, Europe, the Middle East, and Southeast Asia.(Citation: CISA AA21-200A APT40 July 2021)(Citation: Proofpoint Leviathan Oct 2017)(Citation: FireEye Periscope March 2018)(Citation: CISA Leviathan 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| countries | カンボジア | 構造化OSINTの被害国フィールドでLeviathanの標的・被害国としてカンボジアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | サウジアラビア | 構造化OSINTの被害国フィールドでLeviathanの標的・被害国としてサウジアラビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | スイス | 構造化OSINTの被害国フィールドでLeviathanの標的・被害国としてスイスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | タイ | 構造化OSINTの被害国フィールドでLeviathanの標的・被害国としてタイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ドイツ | 構造化OSINTの被害国フィールドでLeviathanの標的・被害国としてドイツが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ニュージーランド | 構造化OSINTの被害国フィールドでLeviathanの標的・被害国としてニュージーランドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ノルウェー | 構造化OSINTの被害国フィールドでLeviathanの標的・被害国としてノルウェーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | フィリピン | 構造化OSINTの被害国フィールドでLeviathanの標的・被害国としてフィリピンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ベトナム | 構造化OSINTの被害国フィールドでLeviathanの標的・被害国としてベトナムが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベルギー | 構造化OSINTの被害国フィールドでLeviathanの標的・被害国としてベルギーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | マレーシア | 構造化OSINTの被害国フィールドでLeviathanの標的・被害国としてマレーシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | ミャンマー | 構造化OSINTの被害国フィールドでLeviathanの標的・被害国としてミャンマーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ラオス | 構造化OSINTの被害国フィールドでLeviathanの標的・被害国としてラオスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | 構造化OSINTの被害国フィールドでLeviathanの標的・被害国として米国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 英国 | 構造化OSINTの被害国フィールドでLeviathanの標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 香港 | 構造化OSINTの被害国フィールドでLeviathanの標的・被害国として香港が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | アジア太平洋 | 構造化OSINTの被害地域フィールドでLeviathanの標的範囲としてアジア太平洋が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | オセアニア | オーストラリア、ニュージーランドで確認された標的・被害事例をオセアニアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| regions | 中東 | MITRE ATT&CKのGroup概要でLeviathanの標的範囲として中東が明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| regions | 北米 | カナダ、米国で確認された標的・被害事例を北米として集約した地域表示。 | 不明 | 不明 | 中 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 東南アジア | インドネシア、カンボジア、タイ、フィリピン、ベトナム、マレーシア、ミャンマー、ラオスで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 欧州 | MITRE ATT&CKのGroup概要でLeviathanの標的範囲として欧州が明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| sectors | 医療・ヘルスケア | SS) Hainan State Security Department and an affiliated front company.(Citation: CISA AA21-200A APT40 July 2021) Active since at least 2009, [Leviathan](https://attack.mitre.org/groups/G0065) has targeted the following sectors: academia, aerospace/aviation, biomedical, defense industrial base, government, healthcare, manufacturing, maritime, and transportation across the US, Canada, Australia, Europe, the Middle East, and Southeast Asia.(Citation: CISA AA21-200A APT40 July 2021)(Citation: Proofpoint Leviathan Oct 2017)(Cit | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 運輸・航空・海運 | Security's (MSS) Hainan State Security Department and an affiliated front company.(Citation: CISA AA21-200A APT40 July 2021) Active since at least 2009, [Leviathan](https://attack.mitre.org/groups/G0065) has targeted the following sectors: academia, aerospace/aviation, biomedical, defense industrial base, government, healthcare, manufacturing, maritime, and transportation across the US, Canada, Australia, Europe, the Middle East, and Southeast Asia.(Citation: CISA AA21-200A APT40 July 2021)(Citation: Proofpoint Leviathan O | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 製造・産業 | Security Department and an affiliated front company.(Citation: CISA AA21-200A APT40 July 2021) Active since at least 2009, [Leviathan](https://attack.mitre.org/groups/G0065) has targeted the following sectors: academia, aerospace/aviation, biomedical, defense industrial base, government, healthcare, manufacturing, maritime, and transportation across the US, Canada, Australia, Europe, the Middle East, and Southeast Asia.(Citation: CISA AA21-200A APT40 July 2021)(Citation: Proofpoint Leviathan Oct 2017)(Citation: FireEye Peris | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | Defense | Targeting text indicates the Defense sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1` |
| sectors | Education and Research | Targeting text indicates the Education and Research sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Government | Targeting text indicates the Government sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1` |
| sectors | Manufacturing | Targeting text indicates the Manufacturing sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Transportation | Targeting text indicates the Transportation sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Leviathan Australian Intrusions | 非公開 | aggregate | multiple-organizations | reported | target--mitre-group--country--4fabe7d586d1591c953e |  | ttp--activity-rule--7b161e2dd2783fd8def0, ttp--mitre-campaign--040a9e5527da36ef102f, ttp--mitre-campaign--0faf84021505e1cc0e12, ttp--mitre-campaign--187f9d121d77791a29cb, ttp--mitre-campaign--1a625a0af199c865a5f2, ttp--mitre-campaign--203982771da558165f46, ttp--mitre-campaign--291cbebad14f781d9e5f, ttp--mitre-campaign--301e1358e0f179779be9, ttp--mitre-campaign--4225beaf8d52820fd11e, ttp--mitre-campaign--458f37ee9c31cd960234, ttp--mitre-campaign--557f5a195d073bde6530, ttp--mitre-campaign--5bb0c25759be88aba1f1, ttp--mitre-campaign--68f230ae9f7be0d7e4d2, ttp--mitre-campaign--7b161e2dd2783fd8def0, ttp--mitre-campaign--7cbfd9c11e236f02df12, ttp--mitre-campaign--8720cfc5eeec7fc8d0c7, ttp--mitre-campaign--9fb8ab89ea9e9e26447b, ttp--mitre-campaign--a07899a6df3209a4af7d, ttp--mitre-campaign--b3666c7bfd9b0b84ab13, ttp--mitre-campaign--b42a2396ecb73006644e, ttp--mitre-campaign--b77d64a6478daf8325fd, ttp--mitre-campaign--cd9e5136ab9f22147cad, ttp--mitre-campaign--dba5b1e61643b94087cf, ttp--mitre-campaign--f9344a6478c31b3cd303, ttp--mitre-campaign--ff786d4885b2a458ebd0, ttp--mitre-campaign--ff8f6b83553531050cc1, ttp--mitre-campaign--ffe9c75146a30e398fb5 |  | data-theft: [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049) were focused on exfiltrating sensitive data including valid credentials for the victim organizations.(Citation: CISA Leviathan 2024)<br>credential-theft: [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049) were focused on exfiltrating sensitive data including valid credentials for the victim organizations.(Citation: CISA Leviathan 2024) | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 2026-05-12 | 高 | `source--mitre-attack-19-1` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049) were focused on exfiltrating sensitive data including valid credentials for the victim organizations.(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 中 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.003 | Local Accounts | [Leviathan](https://attack.mitre.org/groups/G0065) used captured local account information, such as service accounts, for actions during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [Leviathan](https://attack.mitre.org/groups/G0065) performed host enumeration and data gathering operations on victim machines during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1558.003 | Kerberoasting | [Leviathan](https://attack.mitre.org/groups/G0065) used Kerberoasting techniques during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Discovery | T1135 | Network Share Discovery | [Leviathan](https://attack.mitre.org/groups/G0065) scanned and enumerated remote network shares in victim environments during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.006 | Vulnerabilities | [Leviathan](https://attack.mitre.org/groups/G0065) weaponized publicly-known vulnerabilities for initial access and other purposes during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.004 | SSH | [Leviathan](https://attack.mitre.org/groups/G0065) used SSH brute force techniques to move laterally within victim environments during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [Leviathan](https://attack.mitre.org/groups/G0065) exploited public-facing web applications and appliances for initial access during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056 | Input Capture | [Leviathan](https://attack.mitre.org/groups/G0065) captured submitted multfactor authentication codes and other technical artifacts related to remote access sessions during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Discovery | T1482 | Domain Trust Discovery | [Leviathan](https://attack.mitre.org/groups/G0065) performed Active Directory enumeration of victim environments during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1594 | Search Victim-Owned Websites | [Leviathan](https://attack.mitre.org/groups/G0065) enumerated compromised web application resources to identify additional endpoints and resources linkd to the website for follow-on access during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | [Leviathan](https://attack.mitre.org/groups/G0065) relied extensively on web shell use following initial access for persistence and command execution purposes in victim environments during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | [Leviathan](https://attack.mitre.org/groups/G0065) exfiltrated collected data over existing command and control channels during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [Leviathan](https://attack.mitre.org/groups/G0065) used captured, valid account information to log into victim web applications and appliances during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | [Leviathan](https://attack.mitre.org/groups/G0065) stored captured credential material on local log files on victim systems during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Collection | T1213.006 | Databases | [Leviathan](https://attack.mitre.org/groups/G0065) gathered information from SQL servers and Building Management System (BMS) servers during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1111 | Multi-Factor Authentication Interception | [Leviathan](https://attack.mitre.org/groups/G0065) abused compromised appliance access to collect multifactor authentication token values during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1686 | Disable or Modify System Firewall | [Leviathan](https://attack.mitre.org/groups/G0065) modified system firewalls to add two open listening ports on 9998 and 9999 during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Discovery | T1615 | Group Policy Discovery | [Leviathan](https://attack.mitre.org/groups/G0065) performed extensive Active Directory enumeration of victim environments during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | [Leviathan](https://attack.mitre.org/groups/G0065) performed extensive remote host enumeration to build their own map of victim networks during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1068 | Exploitation for Privilege Escalation | [Leviathan](https://attack.mitre.org/groups/G0065) exploited software vulnerabilities in victim environments to escalate privileges during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | [Leviathan](https://attack.mitre.org/groups/G0065) used remote shares to move laterally through victim networks during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552 | Unsecured Credentials | [Leviathan](https://attack.mitre.org/groups/G0065) gathered credentials hardcoded in binaries located on victim devices during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.001 | Credentials In Files | [Leviathan](https://attack.mitre.org/groups/G0065) gathered credentials stored in files related to Building Management System (BMS) operations during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1528 | Steal Application Access Token | [Leviathan](https://attack.mitre.org/groups/G0065) abused access to compromised appliances to collect JSON Web Tokens (JWTs), used for creating virtual desktop sessions, during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.002 | Domain Accounts | [Leviathan](https://attack.mitre.org/groups/G0065) compromised domain credentials during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049).(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1212 | Exploitation for Credential Access | [Leviathan](https://attack.mitre.org/groups/G0065) exploited vulnerable network appliances during [Leviathan Australian Intrusions](https://attack.mitre.org/campaigns/C0049), leading to the collection and exfiltration of valid credentials.(Citation: CISA Leviathan 2024) |  | activity--leviathan-australian-intrusions | 2022-04-01T06:00:00.000Z | 2022-09-01T06:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003 | OS Credential Dumping | [Leviathan](https://attack.mitre.org/groups/G0065) has used publicly available tools to dump password hashes, including [HOMEFRY](https://attack.mitre.org/software/S0232).(Citation: FireEye APT40 March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.001 | LSASS Memory | [Leviathan](https://attack.mitre.org/groups/G0065) has used publicly available tools to dump password hashes, including ProcDump and WCE.(Citation: FireEye APT40 March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | [Leviathan](https://attack.mitre.org/groups/G0065) has targeted RDP credentials and used it to move through the victim environment.(Citation: FireEye APT40 March 2019)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.004 | SSH | [Leviathan](https://attack.mitre.org/groups/G0065) used ssh for internal reconnaissance.(Citation: FireEye APT40 March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.001 | Binary Padding | [Leviathan](https://attack.mitre.org/groups/G0065) has inserted garbage characters into code, presumably to avoid anti-virus detection.(Citation: Proofpoint Leviathan Oct 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.003 | Steganography | [Leviathan](https://attack.mitre.org/groups/G0065) has used steganography to hide stolen data inside other files stored on Github.(Citation: CISA AA21-200A APT40 July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | [Leviathan](https://attack.mitre.org/groups/G0065) has obfuscated code using base64.(Citation: Proofpoint Leviathan Oct 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.015 | Compression | [Leviathan](https://attack.mitre.org/groups/G0065) has obfuscated code using gzip compression.(Citation: Proofpoint Leviathan Oct 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | [Leviathan](https://attack.mitre.org/groups/G0065) has exfiltrated data over its C2 channel.(Citation: CISA AA21-200A APT40 July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | [Leviathan](https://attack.mitre.org/groups/G0065) has used WMI for execution.(Citation: Proofpoint Leviathan Oct 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055.001 | Dynamic-link Library Injection | [Leviathan](https://attack.mitre.org/groups/G0065) has utilized techniques like reflective DLL loading to write a DLL into memory and load a shell that provides backdoor access to the victim.(Citation: Accenture MUDCARP March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [Leviathan](https://attack.mitre.org/groups/G0065) has used PowerShell for execution.(Citation: Proofpoint Leviathan Oct 2017)(Citation: FireEye Periscope March 2018)(Citation: CISA AA21-200A APT40 July 2021)(Citation: Accenture MUDCARP March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | [Leviathan](https://attack.mitre.org/groups/G0065) has used VBScript.(Citation: Proofpoint Leviathan Oct 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | [Leviathan](https://attack.mitre.org/groups/G0065) has used C:\Windows\Debug and C:\Perflogs as staging directories.(Citation: FireEye Periscope March 2018)(Citation: CISA AA21-200A APT40 July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.002 | Remote Data Staging | [Leviathan](https://attack.mitre.org/groups/G0065) has staged data remotely prior to exfiltration.(Citation: CISA AA21-200A APT40 July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [Leviathan](https://attack.mitre.org/groups/G0065) has obtained valid accounts to gain initial access.(Citation: CISA AA21-200A APT40 July 2021)(Citation: Accenture MUDCARP March 2019)(Citation: CISA Leviathan 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090.003 | Multi-hop Proxy | [Leviathan](https://attack.mitre.org/groups/G0065) has used multi-hop proxies to disguise the source of their malicious traffic.(Citation: CISA AA21-200A APT40 July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102.003 | One-Way Communication | [Leviathan](https://attack.mitre.org/groups/G0065) has received C2 instructions from user profiles created on legitimate websites such as Github and TechNet.(Citation: FireEye Periscope March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [Leviathan](https://attack.mitre.org/groups/G0065) has downloaded additional scripts and files from adversary-controlled servers.(Citation: Proofpoint Leviathan Oct 2017)(Citation: FireEye Periscope March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence | T1133 | External Remote Services | [Leviathan](https://attack.mitre.org/groups/G0065) has used external remote services such as virtual private networks (VPN) to gain initial access.(Citation: CISA AA21-200A APT40 July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | [Leviathan](https://attack.mitre.org/groups/G0065) has used a DLL known as SeDll to decrypt and execute other JavaScript backdoors.(Citation: Proofpoint Leviathan Oct 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1189 | Drive-by Compromise | [Leviathan](https://attack.mitre.org/groups/G0065) has infected victims using watering holes.(Citation: CISA AA21-200A APT40 July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [Leviathan](https://attack.mitre.org/groups/G0065) has used exploits against publicly-disclosed vulnerabilities for initial access into victim networks.(Citation: CISA Leviathan 2024) |  |  | 不明 | 不明 | 高 | `source--leviathan--b779bf8c7014ad15`, `source--mitre-attack-19-1` |
| Initial Access | T1195 | Supply Chain Compromise | p (DPRK-linked) Strategic espionage; financial gain targeting RoK government, defense, and cryptocurren- cy firms Spear phishing (T1566) Supply-chain exploits (T1195) APT40 (China-nexus) Espionage aligned with BRI; targets Southeast Asian Governments, Telecommunications, Australia, Japan Exploit public-facing apps (T1190) Spear phishing (T1566) Encrypted webshells (T1505.003) Mirror |  |  | 不明 | 不明 | 中 | `source--leviathan--b779bf8c7014ad15` |
| Execution, Persistence, Stealth | T1197 | BITS Jobs | [Leviathan](https://attack.mitre.org/groups/G0065) has used [BITSAdmin](https://attack.mitre.org/software/S0190) to download additional tools.(Citation: FireEye Periscope March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | [Leviathan](https://attack.mitre.org/groups/G0065) has exploited multiple Microsoft Office and .NET vulnerabilities for execution, including CVE-2017-0199, CVE-2017-8759, and CVE-2017-11882.(Citation: Proofpoint Leviathan Oct 2017)(Citation: FireEye Periscope March 2018)(Citation: CISA AA21-200A APT40 July 2021)(Citation: Accenture MUDCARP March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | [Leviathan](https://attack.mitre.org/groups/G0065) has sent spearphishing email links attempting to get a user to click.(Citation: Proofpoint Leviathan Oct 2017)(Citation: CISA AA21-200A APT40 July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [Leviathan](https://attack.mitre.org/groups/G0065) has sent spearphishing attachments attempting to get a user to click.(Citation: Proofpoint Leviathan Oct 2017)(Citation: CISA AA21-200A APT40 July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.010 | Regsvr32 | [Leviathan](https://attack.mitre.org/groups/G0065) has used regsvr32 for execution.(Citation: Proofpoint Leviathan Oct 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | [Leviathan](https://attack.mitre.org/groups/G0065) relies on web shells for an initial foothold as well as persistence into the victim's systems.(Citation: FireEye APT40 March 2019)(Citation: CISA AA21-200A APT40 July 2021)(Citation: CISA Leviathan 2024) |  |  | 不明 | 不明 | 高 | `source--leviathan--b779bf8c7014ad15`, `source--mitre-attack-19-1` |
| Lateral Movement | T1534 | Internal Spearphishing | [Leviathan](https://attack.mitre.org/groups/G0065) has conducted internal spearphishing within the victim's environment for lateral movement.(Citation: CISA AA21-200A APT40 July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1546.003 | Windows Management Instrumentation Event Subscription | [Leviathan](https://attack.mitre.org/groups/G0065) has used WMI for persistence.(Citation: FireEye Periscope March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [Leviathan](https://attack.mitre.org/groups/G0065) has used JavaScript to create a shortcut file in the Startup folder that points to its main backdoor.(Citation: Proofpoint Leviathan Oct 2017)(Citation: FireEye Periscope March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.009 | Shortcut Modification | [Leviathan](https://attack.mitre.org/groups/G0065) has used JavaScript to create a shortcut file in the Startup folder that points to its main backdoor.(Citation: Proofpoint Leviathan Oct 2017)(Citation: FireEye Periscope March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1553.002 | Code Signing | [Leviathan](https://attack.mitre.org/groups/G0065) has used stolen code signing certificates to sign malware.(Citation: FireEye Periscope March 2018)(Citation: FireEye APT40 March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1559.002 | Dynamic Data Exchange | [Leviathan](https://attack.mitre.org/groups/G0065) has utilized OLE as a method to insert malicious content inside various phishing documents. (Citation: Accenture MUDCARP March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560 | Archive Collected Data | [Leviathan](https://attack.mitre.org/groups/G0065) has archived victim's data prior to exfiltration.(Citation: CISA AA21-200A APT40 July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566 | Phishing | RGETS KEY TACTICS Lazarus Group (DPRK-linked) Strategic espionage; financial gain targeting RoK government, defense, and cryptocurren- cy firms Spear phishing (T1566) Supply-chain exploits (T1195) APT40 (China-nexus) Espionage aligned with BRI; targets Southeast Asian Governments, Telecommunications, Australia, Japan Exploit public-facing apps (T1190) Spear phishing (T1566) Encrypted webshells (T1505.003) Mirror |  |  | 不明 | 不明 | 中 | `source--leviathan--b779bf8c7014ad15` |
| Initial Access | T1566.001 | Spearphishing Attachment | [Leviathan](https://attack.mitre.org/groups/G0065) has sent spearphishing emails with malicious attachments, including .rtf, .doc, and .xls files.(Citation: Proofpoint Leviathan Oct 2017)(Citation: CISA AA21-200A APT40 July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | [Leviathan](https://attack.mitre.org/groups/G0065) has sent spearphishing emails with links, often using a fraudulent lookalike domain and stolen branding.(Citation: Proofpoint Leviathan Oct 2017)(Citation: CISA AA21-200A APT40 July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | [Leviathan](https://attack.mitre.org/groups/G0065) has used an uploader known as LUNCHMONEY that can exfiltrate files to Dropbox.(Citation: Proofpoint Leviathan Oct 2017)(Citation: FireEye Periscope March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1572 | Protocol Tunneling | [Leviathan](https://attack.mitre.org/groups/G0065) has used protocol tunneling to further conceal C2 communications and infrastructure.(Citation: CISA AA21-200A APT40 July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [Leviathan](https://attack.mitre.org/groups/G0065) has established domains that impersonate legitimate entities to use for targeting efforts. (Citation: CISA AA21-200A APT40 July 2021)(Citation: Accenture MUDCARP March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.004 | Server | [Leviathan](https://attack.mitre.org/groups/G0065) has used compromised legitimate websites as command and control nodes for operations.(Citation: CISA Leviathan 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.008 | Network Devices | [Leviathan](https://attack.mitre.org/groups/G0065) has used compromised networking devices, such as small office/home office (SOHO) devices, as operational command and control infrastructure.(Citation: CISA Leviathan 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.001 | Social Media Accounts | [Leviathan](https://attack.mitre.org/groups/G0065) has created new social media accounts for targeting efforts.(Citation: CISA AA21-200A APT40 July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.002 | Email Accounts | [Leviathan](https://attack.mitre.org/groups/G0065) has created new email accounts for targeting efforts.(Citation: CISA AA21-200A APT40 July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1586.001 | Social Media Accounts | [Leviathan](https://attack.mitre.org/groups/G0065) has compromised social media accounts to conduct social engineering attacks.(Citation: CISA AA21-200A APT40 July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1586.002 | Email Accounts | [Leviathan](https://attack.mitre.org/groups/G0065) has compromised email accounts to conduct social engineering attacks.(Citation: CISA AA21-200A APT40 July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.004 | Exploits | [Leviathan](https://attack.mitre.org/groups/G0065) has rapidly transformed and adapted public exploit proof-of-concept code for new vulnerabilities and utilized them against target networks.(Citation: CISA Leviathan 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589.001 | Credentials | [Leviathan](https://attack.mitre.org/groups/G0065) has collected compromised credentials to use for targeting efforts.(Citation: CISA AA21-200A APT40 July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1595.002 | Vulnerability Scanning | [Leviathan](https://attack.mitre.org/groups/G0065) has conducted reconnaissance against target networks of interest looking for vulnerable, end-of-life, or no longer maintainted devices against which to rapidly deploy exploits.(Citation: CISA Leviathan 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 2件
- IOC観測: 3件
- 複数攻撃で観測: 0件
- 要レビュー候補: 2件
- 非IOC artifact観測: 89件（`artifacts.csv`）

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
| source--leviathan--b779bf8c7014ad15 | leviathan |  | 不明 | actor_profile/evidence/leviathan.csv | structured-data | TLP:CLEAR | 中 |
| source--leviathan--b5009077341bfaec | Large scale online deanonymization with LLMs |  | 不明 | AISecurity/Large-scale online deanonymization with LLMs.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--4dd1a72d8e3453ce | Automating APT Campaign and Group Attribution |  | 不明 | APT-hunting/Automating APT Campaign and Group Attribution.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--ff7b46f151461496 | F Secure Dukes Whitepaper |  | 不明 | APT29/F-Secure_Dukes_Whitepaper.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--8e5b4cea64f668ba | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--77cff642f45345b0 | A three beat waltz The ecosystem behind Chinese state sponsored cyber threats |  | 不明 | International Strategic/China/A-three-beat-waltz-The-ecosystem-behind-Chinese-state-sponsored-cyber-threats.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--5ffc940f5c75f342 | china cyber report |  | 不明 | International Strategic/China/china-cyber-report.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--a7788b2aa3e71770 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--9e18949ba7ac111d | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--b288cfa4f528b425 | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--leviathan--ca380475e98e61c5 | global perspective of the sidewinder apt |  | 不明 | sidewinder/global-perspective-of-the-sidewinder-apt.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--13205b97995ff349 | 2021(APT) Microsoft Digital Defense Report |  | 2021 | summary/2021/2021(APT) Microsoft Digital Defense Report.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--c1bb241de450b38c | Adversary Infrastructure Report 2020 |  | 2020 | summary/2021/Adversary Infrastructure Report 2020.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--de865c13b97e3ac1 | The CrowdStrike 2021 Global Threat Report |  | 2021 | summary/2021/The CrowdStrike 2021 Global Threat Report.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--50cab98466f04a7b | rpt mtrends 2021 fireeye |  | 2021 | summary/2021/rpt-mtrends-2021-fireeye.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--ff748e287558d2f5 | 2021 Adversary Infrastructure Report |  | 2021 | summary/2022/2021 Adversary Infrastructure Report.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--b1bc20957a5fe376 | Microsoft Digital Defense Report 2022 |  | 2022 | summary/2022/Microsoft Digital Defense Report 2022.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--743119fb84d607c2 | 2022 year in retrospect report |  | 2022 | summary/2023/2022-year-in-retrospect-report.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--9c8aca131fe1e591 | M Trends 2023 Report MANDIANT SPECIAL REPORT |  | 2023 | summary/2023/M-Trends 2023 Report MANDIANT SPECIAL REPORT.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--9f3d9cae57c39507 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--c7e7d44bd750a836 | kaspersky ics cert apt attacks on industrial organizations in h2 2022 en |  | 2022 | summary/2023/kaspersky-ics-cert-apt-attacks-on-industrial-organizations-in-h2-2022-en.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--019994537c208975 | Hurdling Over Hazards  Multifaceted Threats to the Paris Olympics |  | 不明 | summary/2024/Hurdling Over Hazards- Multifaceted Threats to the Paris Olympics.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--da24d16f1e40edd8 | m trends 2024 |  | 2024 | summary/2024/m-trends-2024.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--b021d913765c5d2a | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--leviathan--5bbc643c9a8c13c8 | NCSC Cyber Threat Report 2024 FINAL |  | 2024 | summary/2025/NCSC-Cyber-Threat-Report-2024-FINAL.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--baab664e4950756d | Cloudflare 2026 threat report |  | 2026 | summary/2026/Cloudflare-2026-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--leviathan--6607ed0c96b2b169 | Threat Report 2026 v4 |  | 2026 | summary/2026/Threat Report 2026 v4.pdf | report | TLP:CLEAR | 中 |
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
