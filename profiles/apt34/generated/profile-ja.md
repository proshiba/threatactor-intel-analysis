# APT34 脅威アクタープロファイル

- プロファイルID: `actor--apt34`
- 状態: review
- 更新日時: 2026-07-29T23:11:59Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

APT34の標準化プロファイル。リポジトリ内の専用資料2件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **APT34**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| COBALT GYPSY | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Crambus | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| EUROPIUM | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Earth Simnavaz | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Evasive Serpens | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Hazel Sandstorm | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Helix Kitten | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| IRN2 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| ITG13 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| OilRig | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TA452 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Twisted Kitten | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Iran row 11; mapping requires review. |
| Chrysene | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Iran row 11; mapping requires review. |

## 帰属

The repository mapping workbook places this actor in the Iran worksheet.

- 国: Iran
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
| HEXANE | related-to | [HEXANE](https://attack.mitre.org/groups/G1001)'s TTPs appear similar to [APT33](https://attack.mitre.org/groups/G0064) and [OilRig](https://attack.mitre.org/groups/G0049) but due to differences in victims and tools it is tracked as a separate entity.(Citation: Dragos Hexane)(Citation: Kaspersky Lyceum October 2021)(Citation: ClearSky Siamesekitten August 2021)(Citation: Accenture Lyceum Targets November 2021) | 中 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [OilRig](https://attack.mitre.org/groups/G0049) is a suspected Iranian threat group that has targeted Middle Eastern and international victims since at least 2014. The group has targeted a variety of sectors, including financial, government, energy, chemical, and telecommunications. It appears the group carries out supply chain attacks, leveraging the trust relationship between organizations to attack their primary targets. The group works on behalf of the Iranian government based on infrastructure details that contain references to Iran, use of Iranian infrastructure, and targeting that aligns with nation-state interests.(Citation: FireEye APT34 Dec 2017)(Citation: Palo Alto OilRig April 2017)(Citation: ClearSky OilRig Jan 2017)(Citation: Palo Alto OilRig May 2016)(Citation: Palo Alto OilRig Oct 2016)(Citation: Unit42 OilRig Playbook 2023)(Citation: Unit 42 QUADAGENT July 2018) |
| Capability | SEASHARPEE, POWRUNER, PowerExchange, ODAgent, RDAT, ISMInjector, QUADAGENT, ZeroCleare, OopsIE, OilCheck, SampleCheck5000, OilBooster, Solar, RGDoor, Mango, BONDUPDATER, SideTwist, Helminth, ISMDoor, Clayslide, ALMA Communicator, customized Mimikatz, Invoke-Obfuscation, POWBAT, POWRUNER (PS Backdoor), malicious RTF files CVE-2017-0199 and CVE-2017-11882, ELVENDOOR, PLink, SSH Tunnels to Windows Servers, Webshells (TwoFace, DarkSeaGreenShell, LittleFace), PowDesk, Net, certutil, ipconfig, Tasklist, ngrok, netstat, Systeminfo, Mimikatz, LaZagne, Reg, ftp, PsExec |
| Infrastructure |  |
| Victim |  |
| Socio-political | Iran |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | OilRig, APT 34, Helix Kitten, Chrysene | canonical-name | 高 | Iran | https://unit42.paloaltonetworks.com/unit42-striking-oil-closer-look-adversary-infrastructure/<br>https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-november-helix-kitten/<br>https://marcoramilli.com/2019/08/07/oilrig-the-techniques-evolution-over-time/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Hazel Sandstorm | canonical-name | 高 | Iran | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Cleaver | single-alias-intersection | 中 | IR, Iran (Islamic Republic of) | https://www.secureworks.com/research/the-curious-case-of-mia-ash<br>https://www.cfr.org/interactive/cyber-operations/operation-cleaver<br>http://www.secureworks.com/cyber-threat-intelligence/threats/suspected-iran-based-hacker-group-creates-network-of-fake-linkedin-profiles/ |
| misp-threat-actor | OilRig | canonical-name | 高 | IR, Iran (Islamic Republic of) | https://blog.morphisec.com/iranian-fileless-cyberattack-on-israel-word-vulnerability<br>https://unit42.paloaltonetworks.com/unit42-striking-oil-closer-look-adversary-infrastructure/<br>https://unit42.paloaltonetworks.com/unit42-introducing-the-adversary-playbook-first-up-oilrig/ |
| misp-threat-actor | CHRYSENE | multiple-name-intersection | 高 | Unknown | https://dragos.com/adversaries.html<br>https://dragos.com/media/2017-Review-Industrial-Control-System-Threats.pdf<br>https://www.cfr.org/interactive/cyber-operations/chrysene |
| misp-microsoft-activity-group | Hazel Sandstorm | canonical-name | 高 | IR, Iran | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | APT34 - G0057 | canonical-name | 高 |  | https://attack.mitre.org/wiki/Group/G0057<br>https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html |
| misp-mitre-enterprise-intrusion-set | OilRig - G0049 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0049<br>http://researchcenter.paloaltonetworks.com/2017/04/unit42-oilrig-actors-provide-glimpse-development-testing-efforts/<br>http://www.clearskysec.com/oilrig/ |
| misp-mitre-enterprise-intrusion-set | Magic Hound - G0059 | single-alias-intersection | 中 |  | https://attack.mitre.org/wiki/Group/G0059<br>https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/ |
| misp-mitre-intrusion-set | APT34 - G0057 | canonical-name | 高 |  | https://attack.mitre.org/groups/G0057 |
| misp-mitre-intrusion-set | OilRig - G0049 | mitre-external-id | 高 |  | http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/<br>http://researchcenter.paloaltonetworks.com/2016/10/unit42-oilrig-malware-campaign-updates-toolset-and-expands-targets/<br>http://researchcenter.paloaltonetworks.com/2017/04/unit42-oilrig-actors-provide-glimpse-development-testing-efforts/ |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Cleaver | similar | misp-mitre-enterprise-intrusion-set | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| CHRYSENE | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Charming Kitten | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Cleaver | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Clever Kitten | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Cutting Kitten | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Flying Kitten | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Greenbug | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| OilRig | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Rocket Kitten | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--seasharpee | SEASHARPEE | [SEASHARPEE](https://attack.mitre.org/software/S0185) is a Web shell that has been used by [OilRig](https://attack.mitre.org/groups/G0049). (Citation: FireEye APT34 Webinar Dec 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--powruner | POWRUNER | [POWRUNER](https://attack.mitre.org/software/S0184) is a PowerShell script that sends and receives commands to and from the C2 server. (Citation: FireEye APT34 Dec 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--powerexchange | PowerExchange | [PowerExchange](https://attack.mitre.org/software/S1173) is a PowerShell backdoor that has been used by [OilRig](https://attack.mitre.org/groups/G0049) since at least 2023 including against government targets in the Middle East.(Citation: Symantec Crambus OCT 2023) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--odagent | ODAgent | [ODAgent](https://attack.mitre.org/software/S1170) is a C#/.NET downloader that has been used by [OilRig](https://attack.mitre.org/groups/G0049) since at least 2022 including against target organizations in Israel to download and execute payloads and to exfiltrate staged files.(Citation: ESET OilRig Downloaders DEC 2023) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--rdat | RDAT | [RDAT](https://attack.mitre.org/software/S0495) is a backdoor used by the suspected Iranian threat group [OilRig](https://attack.mitre.org/groups/G0049). [RDAT](https://attack.mitre.org/software/S0495) was originally identified in 2017 and targeted companies in the telecommunications sector.(Citation: Unit42 RDAT July 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--isminjector | ISMInjector | [ISMInjector](https://attack.mitre.org/software/S0189) is a Trojan used to install another [OilRig](https://attack.mitre.org/groups/G0049) backdoor, ISMAgent. (Citation: OilRig New Delivery Oct 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--quadagent | QUADAGENT | [QUADAGENT](https://attack.mitre.org/software/S0269) is a PowerShell backdoor used by [OilRig](https://attack.mitre.org/groups/G0049). (Citation: Unit 42 QUADAGENT July 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--zerocleare | ZeroCleare | [ZeroCleare](https://attack.mitre.org/software/S1151) is a wiper malware that has been used in conjunction with the [RawDisk](https://attack.mitre.org/software/S0364) driver since at least 2019 by suspected Iran-nexus threat actors including activity targeting the energy and industrial sectors in the Middle East and political targets in Albania.(Citation: Microsoft Albanian Government Attacks September 2022)(Citation: CISA Iran Albanian Attacks September 2022)(Citation: Mandiant ROADSWEEP August 2022)(Citation: IBM ZeroCleare Wiper December 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--oopsie | OopsIE | [OopsIE](https://attack.mitre.org/software/S0264) is a Trojan used by [OilRig](https://attack.mitre.org/groups/G0049) to remotely execute commands as well as upload/download files to/from victims. (Citation: Unit 42 OopsIE! Feb 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--oilcheck | OilCheck | [OilCheck](https://attack.mitre.org/software/S1171) is a C#/.NET downloader that has been used by [OilRig](https://attack.mitre.org/groups/G0049) since at least 2022 including against targets in Israel. [OilCheck](https://attack.mitre.org/software/S1171) uses draft messages created in a shared email account for C2 communication.(Citation: ESET OilRig Downloaders DEC 2023) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--samplecheck5000 | SampleCheck5000 | [SampleCheck5000](https://attack.mitre.org/software/S1168) is a downloader with multiple variants that was used by [OilRig](https://attack.mitre.org/groups/G0049) including during the [Outer Space](https://attack.mitre.org/campaigns/C0042) campaign to download and execute additional payloads. (Citation: ESET OilRig Campaigns Sep 2023)(Citation: ESET OilRig Downloaders DEC 2023) | 2021-01-01T05:00:00.000Z | 2021-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| malware--oilbooster | OilBooster | [OilBooster](https://attack.mitre.org/software/S1172) is a downloader written in Microsoft Visual C/C++ that has been used by [OilRig](https://attack.mitre.org/groups/G0049) since at least 2022 including against target organizations in Israel to download and execute files and for exfiltration.(Citation: ESET OilRig Downloaders DEC 2023)    | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--solar | Solar | [Solar](https://attack.mitre.org/software/S1166) is a C#/.NET backdoor that was used by [OilRig](https://attack.mitre.org/groups/G0049) during the [Outer Space](https://attack.mitre.org/campaigns/C0042) campaign to download, execute, and exfiltrate files.(Citation: ESET OilRig Campaigns Sep 2023) | 2021-01-01T05:00:00.000Z | 2021-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| malware--rgdoor | RGDoor | [RGDoor](https://attack.mitre.org/software/S0258) is a malicious Internet Information Services (IIS) backdoor developed in the C++ language. [RGDoor](https://attack.mitre.org/software/S0258) has been seen deployed on webservers belonging to the Middle East government organizations. [RGDoor](https://attack.mitre.org/software/S0258) provides backdoor access to compromised IIS servers. (Citation: Unit 42 RGDoor Jan 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--mango | Mango | [Mango](https://attack.mitre.org/software/S1169) is a first-stage backdoor written in C#/.NET that was used by [OilRig](https://attack.mitre.org/groups/G0049) during the [Juicy Mix](https://attack.mitre.org/campaigns/C0044) campaign. [Mango](https://attack.mitre.org/software/S1169) is the successor to [Solar](https://attack.mitre.org/software/S1166) and includes additional exfiltration capabilities, the use of native APIs, and added detection evasion code.(Citation: ESET OilRig Campaigns Sep 2023) | 2022-01-01T05:00:00.000Z | 2022-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| malware--bondupdater | BONDUPDATER | [BONDUPDATER](https://attack.mitre.org/software/S0360) is a PowerShell backdoor used by [OilRig](https://attack.mitre.org/groups/G0049). It was first observed in November 2017 during targeting of a Middle Eastern government organization, and an updated version was observed in August 2018 being used to target a government organization with spearphishing emails.(Citation: FireEye APT34 Dec 2017)(Citation: Palo Alto OilRig Sep 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--sidetwist | SideTwist | [SideTwist](https://attack.mitre.org/software/S0610) is a C-based backdoor that has been used by [OilRig](https://attack.mitre.org/groups/G0049) since at least 2021.(Citation: Check Point APT34 April 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--helminth | Helminth | [Helminth](https://attack.mitre.org/software/S0170) is a backdoor that has at least two variants - one written in VBScript and PowerShell that is delivered via a macros in Excel spreadsheets, and one that is a standalone Windows executable. (Citation: Palo Alto OilRig May 2016) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--ismdoor | ISMDoor | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--clayslide | Clayslide | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--alma-communicator | ALMA Communicator | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--customized-mimikatz | customized Mimikatz | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--invoke-obfuscation | Invoke-Obfuscation | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--powbat | POWBAT | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--powruner-ps-backdoor | POWRUNER (PS Backdoor) | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--malicious-rtf-files-cve-2017-0199-and-cve-2017-11882 | malicious RTF files CVE-2017-0199 and CVE-2017-11882 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--elvendoor | ELVENDOOR | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--plink | PLink | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--ssh-tunnels-to-windows-servers | SSH Tunnels to Windows Servers | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--webshells-twoface | Webshells (TwoFace | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--darkseagreenshell | DarkSeaGreenShell | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--littleface | LittleFace) | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--powdesk | PowDesk | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--certutil | certutil | [certutil](https://attack.mitre.org/software/S0160) is a command-line utility that can be used to obtain certificate authority information and configure Certificate Services. (Citation: TechNet Certutil) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ipconfig | ipconfig | [ipconfig](https://attack.mitre.org/software/S0100) is a Windows utility that can be used to find information about a system's TCP/IP, DNS, DHCP, and adapter configuration. (Citation: TechNet Ipconfig) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--tasklist | Tasklist | The [Tasklist](https://attack.mitre.org/software/S0057) utility displays a list of applications and services with their Process IDs (PID) for all tasks running on either a local or a remote computer. It is packaged with Windows operating systems and can be executed from the command-line interface. (Citation: Microsoft Tasklist) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ngrok | ngrok | [ngrok](https://attack.mitre.org/software/S0508) is a legitimate reverse proxy tool that can create a secure tunnel to servers located behind firewalls or on local machines that do not have a public IP. [ngrok](https://attack.mitre.org/software/S0508) has been leveraged by threat actors in several campaigns including use for lateral movement and data exfiltration.(Citation: Zdnet Ngrok September 2018)(Citation: FireEye Maze May 2020)(Citation: Cyware Ngrok May 2019)(Citation: MalwareBytes LazyScripter Feb 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--netstat | netstat | [netstat](https://attack.mitre.org/software/S0104) is an operating system utility that displays active TCP connections, listening ports, and network statistics. (Citation: TechNet Netstat) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--systeminfo | Systeminfo | [Systeminfo](https://attack.mitre.org/software/S0096) is a Windows utility that can be used to gather detailed information about a computer. (Citation: TechNet Systeminfo) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--lazagne | LaZagne | [LaZagne](https://attack.mitre.org/software/S0349) is a post-exploitation, open-source tool used to recover stored passwords on a system. It has modules for Windows, Linux, and OSX, but is mainly focused on Windows systems. [LaZagne](https://attack.mitre.org/software/S0349) is publicly available on GitHub.(Citation: GitHub LaZagne Dec 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--reg | Reg | [Reg](https://attack.mitre.org/software/S0075) is a Windows utility used to interact with the Windows Registry. It can be used at the command-line interface to query, add, modify, and remove information. (Citation: Microsoft Reg)<br><br>Utilities such as [Reg](https://attack.mitre.org/software/S0075) are known to be used by persistent threats. (Citation: Windows Commands JPCERT) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ftp | ftp | [ftp](https://attack.mitre.org/software/S0095) is a utility commonly available with operating systems to transfer information over the File Transfer Protocol (FTP). Adversaries can use it to transfer other tools onto a system or to exfiltrate data.(Citation: Microsoft FTP)(Citation: Linux FTP) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--psexec | PsExec | [PsExec](https://attack.mitre.org/software/S0029) is a free Microsoft tool that can be used to execute a program on another computer. It is used by IT administrators and attackers.(Citation: Russinovich Sysinternals)(Citation: SANS PsExec) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### インフラ

未確認

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| capability--apt34-destructive-wiper-operations | Destructive Wiper Operations | Unit 42's 2026 retrospective identifies Evasive Serpens (APT34/OilRig) among Iranian groups that targeted IT infrastructure with high-visibility disk-wiping malware during 2016-2019. | 2016 | 2019 | 高 | `source--unit42-iran-threat-evolution-2026` |

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| APT34 Destructive Wiper Operations (2016-2019) | historical-activity-cluster | 2016 | 2019 | 2026 |  |  | ttp--t1485--apt34-destructive-2016-2019 |  | Unit 42 retrospectively places APT34/Evasive Serpens among Iranian groups conducting visible disk-wiping operations against IT infrastructure in this period. | 高 | `source--unit42-iran-threat-evolution-2026` |
| Juicy Mix | campaign | 2022-01-01T05:00:00.000Z | 2022-12-01T05:00:00.000Z | 2026-05-12 | target--activity-rule--country--904728608f27c39df0df, target--activity-rule--sector--d406c8e5b7fa7aeff7d2 | malware--mango | ttp--mitre-campaign--3f554025662d533005a2, ttp--mitre-campaign--45d595a59b4403b0ff53, ttp--mitre-campaign--4682c397f864d36d8d5e, ttp--mitre-campaign--55bd494b10c7be2552fc, ttp--mitre-campaign--5a1c112991a3b253718e, ttp--mitre-campaign--95cce26df981a692565b, ttp--mitre-campaign--962bae9a2d45b0cb28ca, ttp--mitre-campaign--ae147b7ed211196d2c79, ttp--mitre-campaign--bf0febcece56b15f6f7b, ttp--mitre-campaign--c3fa70ca93f2965cc404, ttp--mitre-campaign--ccb061178b22cbe8338a, ttp--mitre-campaign--d8efd1b57e514a7f2067, ttp--mitre-campaign--d9f5583d0b11893e6f26, ttp--mitre-campaign--da02368b41ff7202bb02 | victim--activity-rule--6d3c9d3af50a8eb2a8f1 | [Juicy Mix](https://attack.mitre.org/campaigns/C0044) was a campaign conducted by [OilRig](https://attack.mitre.org/groups/G0049) throughout 2022 that targeted Israeli organizations with the [Mango](https://attack.mitre.org/software/S1169) backdoor.(Citation: ESET OilRig Campaigns Sep 2023) | 高 | `source--mitre-attack-19-1` |
| Outer Space | campaign | 2021-01-01T05:00:00.000Z | 2021-12-01T05:00:00.000Z | 2026-05-12 | target--activity-rule--country--904728608f27c39df0df | malware--samplecheck5000, malware--solar | ttp--mitre-campaign--370306537b6f2363fb8b, ttp--mitre-campaign--53408b5a05843b864b73, ttp--mitre-campaign--730c95821decbcad8fe2, ttp--mitre-campaign--9e078c2330c1fb463ca5, ttp--mitre-campaign--a2af178d25acc75b8775, ttp--mitre-campaign--b168a610f26c4a9cbb67, ttp--mitre-campaign--c885f44008c6ee88e614, ttp--mitre-campaign--e2838ec9850b74f19ee1 | victim--activity-rule--e3776dc3d4004d3aaf8c | [Outer Space](https://attack.mitre.org/campaigns/C0042) was a campaign conducted by [OilRig](https://attack.mitre.org/groups/G0049) throughout 2021 that used the [SampleCheck5000](https://attack.mitre.org/software/S1168) downloader and [Solar](https://attack.mitre.org/software/S1166) backdoor to target Israeli organizations.(Citation: ESET OilRig Campaigns Sep 2023) | 高 | `source--mitre-attack-19-1` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| APT34 Destructive Wiper Operations (2016-2019) | APT34 | 情報なし | T1485 Data Destruction | 情報なし | 情報なし | 情報なし | 高 |
| Juicy Mix | APT34 | Mango | T1059.001 PowerShell, T1071.001 Web Protocols, T1059.005 Visual Basic, T1518 Software Discovery, T1587.001 Malware, T1555.004 Windows Credential Manager, T1074.001 Local Data Staging, T1140 Deobfuscate/Decode Files or Information, T1584.004 Server, T1132.001 Standard Encoding, T1082 System Information Discovery, T1217 Browser Information Discovery, T1555.003 Credentials from Web Browsers, T1053.005 Scheduled Task | 情報なし | イスラエル, 非営利・市民社会 | 被害事例: Juicy Mix | 高 |
| Outer Space | APT34 | SampleCheck5000, Solar | T1584.004 Server, T1585.003 Cloud Accounts, T1071.001 Web Protocols, T1217 Browser Information Discovery, T1587.001 Malware, T1027.013 Encrypted/Encoded File, T1105 Ingress Tool Transfer, T1059.005 Visual Basic | 情報なし | イスラエル | 被害事例: Outer Space | 高 |

Unit 42は2026年の回顧分析で、Evasive Serpens（APT34/OilRig）を2016～2019年にITインフラへ高可視性のディスク破壊攻撃を行ったイラン系グループの一つとして位置付けた。周辺記述は複数グループを扱うため、個別マルウェアの帰属は限定して記録した。

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アゼルバイジャン | 構造化OSINTの被害国フィールドでAPT34の標的・被害国としてアゼルバイジャンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | アラブ首長国連邦 | 構造化OSINTの被害国フィールドでAPT34の標的・被害国としてアラブ首長国連邦が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | アルバニア | 構造化OSINTの被害国フィールドでAPT34の標的・被害国としてアルバニアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イスラエル | 活動「Juicy Mix」の記述で標的として明示された国・地域。 | 2021-01-01T05:00:00.000Z | 2022-12-01T05:00:00.000Z | 中 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | イラク | 構造化OSINTの被害国フィールドでAPT34の標的・被害国としてイラクが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | イラン | The group works on behalf of the Iranian government based on infrastructure details that contain references to Iran, use of Iranian infrastructure, and targeting that aligns with nation-state interests.(Citation: FireEye APT34 Dec 2017)(Citation: Palo Alto OilRig April 2017)(Citation: ClearSky Oi | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| countries | エジプト | 構造化OSINTの被害国フィールドでAPT34の標的・被害国としてエジプトが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オマーン | 構造化OSINTの被害国フィールドでAPT34の標的・被害国としてオマーンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | カタール | 構造化OSINTの被害国フィールドでAPT34の標的・被害国としてカタールが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | クウェート | 構造化OSINTの被害国フィールドでAPT34の標的・被害国としてクウェートが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | サウジアラビア | 構造化OSINTの被害国フィールドでAPT34の標的・被害国としてサウジアラビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | トルコ | 構造化OSINTの被害国フィールドでAPT34の標的・被害国としてトルコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | バーレーン | 構造化OSINTの被害国フィールドでAPT34の標的・被害国としてバーレーンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | パキスタン | 構造化OSINTの被害国フィールドでAPT34の標的・被害国としてパキスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | モーリシャス | 構造化OSINTの被害国フィールドでAPT34の標的・被害国としてモーリシャスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ヨルダン | 構造化OSINTの被害国フィールドでAPT34の標的・被害国としてヨルダンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | レバノン | 構造化OSINTの被害国フィールドでAPT34の標的・被害国としてレバノンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 中国 | 構造化OSINTの被害国フィールドでAPT34の標的・被害国として中国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | 構造化OSINTの被害国フィールドでAPT34の標的・被害国として米国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 英国 | 構造化OSINTの被害国フィールドでAPT34の標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | アフリカ | エジプト、モーリシャスで確認された標的・被害事例をアフリカとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 中東 | MITRE ATT&CKのGroup概要でAPT34の標的範囲として中東が明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 欧州 | アルバニア、トルコ、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| sectors | 非営利・市民社会 | 活動「Juicy Mix」の記述で標的として明示された産業。 | 2022-01-01T05:00:00.000Z | 2022-12-01T05:00:00.000Z | 中 | `source--mitre-attack-19-1` |
| sectors | エネルギー | The group has targeted a variety of sectors, including financial, government, energy, chemical, and telecommunications. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 政府・行政 | The group has targeted a variety of sectors, including financial, government, energy, chemical, and telecommunications. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 金融 | The group has targeted a variety of sectors, including financial, government, energy, chemical, and telecommunications. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 情報通信 | The group has targeted a variety of sectors, including financial, government, energy, chemical, and telecommunications. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Juicy Mix | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--904728608f27c39df0df, target--activity-rule--sector--d406c8e5b7fa7aeff7d2 | malware--mango | ttp--mitre-campaign--3f554025662d533005a2, ttp--mitre-campaign--45d595a59b4403b0ff53, ttp--mitre-campaign--4682c397f864d36d8d5e, ttp--mitre-campaign--55bd494b10c7be2552fc, ttp--mitre-campaign--5a1c112991a3b253718e, ttp--mitre-campaign--95cce26df981a692565b, ttp--mitre-campaign--962bae9a2d45b0cb28ca, ttp--mitre-campaign--ae147b7ed211196d2c79, ttp--mitre-campaign--bf0febcece56b15f6f7b, ttp--mitre-campaign--c3fa70ca93f2965cc404, ttp--mitre-campaign--ccb061178b22cbe8338a, ttp--mitre-campaign--d8efd1b57e514a7f2067, ttp--mitre-campaign--d9f5583d0b11893e6f26, ttp--mitre-campaign--da02368b41ff7202bb02 |  |  | 2022-01-01T05:00:00.000Z | 2022-12-01T05:00:00.000Z | 2026-05-12 | 高 | `source--mitre-attack-19-1` |
| 被害事例: Outer Space | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--904728608f27c39df0df | malware--samplecheck5000, malware--solar | ttp--mitre-campaign--370306537b6f2363fb8b, ttp--mitre-campaign--53408b5a05843b864b73, ttp--mitre-campaign--730c95821decbcad8fe2, ttp--mitre-campaign--9e078c2330c1fb463ca5, ttp--mitre-campaign--a2af178d25acc75b8775, ttp--mitre-campaign--b168a610f26c4a9cbb67, ttp--mitre-campaign--c885f44008c6ee88e614, ttp--mitre-campaign--e2838ec9850b74f19ee1 |  |  | 2021-01-01T05:00:00.000Z | 2021-12-01T05:00:00.000Z | 2026-05-12 | 高 | `source--mitre-attack-19-1` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Resource Development | T1584.004 | Server | During [Outer Space](https://attack.mitre.org/campaigns/C0042), [OilRig](https://attack.mitre.org/groups/G0049) compromised an Israeli human resources site to use as a C2 server.(Citation: ESET OilRig Campaigns Sep 2023) |  | activity--outer-space | 2021-01-01T05:00:00.000Z | 2021-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | During [Juicy Mix](https://attack.mitre.org/campaigns/C0044), [OilRig](https://attack.mitre.org/groups/G0049) used a PowerShell script to steal credentials.(Citation: ESET OilRig Campaigns Sep 2023) |  | activity--juicy-mix | 2022-01-01T05:00:00.000Z | 2022-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | During [Juicy Mix](https://attack.mitre.org/campaigns/C0044), [OilRig](https://attack.mitre.org/groups/G0049) used a VBS script to send POST requests to register installed malware with C2.(Citation: ESET OilRig Campaigns Sep 2023) |  | activity--juicy-mix | 2022-01-01T05:00:00.000Z | 2022-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | During [Juicy Mix](https://attack.mitre.org/campaigns/C0044), [OilRig](https://attack.mitre.org/groups/G0049) used VBS droppers to deliver and establish persistence for the [Mango](https://attack.mitre.org/software/S1169) backdoor.(Citation: ESET OilRig Campaigns Sep 2023) |  | activity--juicy-mix | 2022-01-01T05:00:00.000Z | 2022-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.003 | Cloud Accounts | During [Outer Space](https://attack.mitre.org/campaigns/C0042), [OilRig](https://attack.mitre.org/groups/G0049) created M365 email accounts to be used as part of C2.(Citation: ESET OilRig Campaigns Sep 2023) |  | activity--outer-space | 2021-01-01T05:00:00.000Z | 2021-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518 | Software Discovery | During [Juicy Mix](https://attack.mitre.org/campaigns/C0044), [OilRig](https://attack.mitre.org/groups/G0049) used browser data dumper tools to create a list of users with Google Chrome installed.(Citation: ESET OilRig Campaigns Sep 2023) |  | activity--juicy-mix | 2022-01-01T05:00:00.000Z | 2022-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | For [Juicy Mix](https://attack.mitre.org/campaigns/C0044), [OilRig](https://attack.mitre.org/groups/G0049) improved on [Solar](https://attack.mitre.org/software/S1166) by developing the [Mango](https://attack.mitre.org/software/S1169) backdoor.(Citation: ESET OilRig Campaigns Sep 2023) |  | activity--juicy-mix | 2022-01-01T05:00:00.000Z | 2022-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | During [Outer Space](https://attack.mitre.org/campaigns/C0042), [OilRig](https://attack.mitre.org/groups/G0049) used HTTP to communicate between installed backdoors and compromised servers including via the Microsoft Exchange Web Services API.(Citation: ESET OilRig Campaigns Sep 2023) |  | activity--outer-space | 2021-01-01T05:00:00.000Z | 2021-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.004 | Windows Credential Manager | During [Juicy Mix](https://attack.mitre.org/campaigns/C0044), [OilRig](https://attack.mitre.org/groups/G0049) used a Windows Credential Manager stealer for credential access.(Citation: ESET OilRig Campaigns Sep 2023) |  | activity--juicy-mix | 2022-01-01T05:00:00.000Z | 2022-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | During [Juicy Mix](https://attack.mitre.org/campaigns/C0044), [OilRig](https://attack.mitre.org/groups/G0049) used browser data and credential stealer tools to stage stolen files named Cupdate, Eupdate, and IUpdate in the %TEMP% directory.(Citation: ESET OilRig Campaigns Sep 2023) |  | activity--juicy-mix | 2022-01-01T05:00:00.000Z | 2022-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Discovery | T1217 | Browser Information Discovery | During [Outer Space](https://attack.mitre.org/campaigns/C0042), [OilRig](https://attack.mitre.org/groups/G0049) used a Chrome data dumper named MKG.(Citation: ESET OilRig Campaigns Sep 2023) |  | activity--outer-space | 2021-01-01T05:00:00.000Z | 2021-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | For [Outer Space](https://attack.mitre.org/campaigns/C0042), [OilRig](https://attack.mitre.org/groups/G0049) created new implants including the [Solar](https://attack.mitre.org/software/S1166) backdoor.(Citation: ESET OilRig Campaigns Sep 2023) |  | activity--outer-space | 2021-01-01T05:00:00.000Z | 2021-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | During [Juicy Mix](https://attack.mitre.org/campaigns/C0044), [OilRig](https://attack.mitre.org/groups/G0049) used a script to concatenate and deobfuscate encoded strings in [Mango](https://attack.mitre.org/software/S1169).(Citation: ESET OilRig Campaigns Sep 2023) |  | activity--juicy-mix | 2022-01-01T05:00:00.000Z | 2022-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | During [Outer Space](https://attack.mitre.org/campaigns/C0042), [OilRig](https://attack.mitre.org/groups/G0049) deployed VBS droppers with obfuscated strings.(Citation: ESET OilRig Campaigns Sep 2023) |  | activity--outer-space | 2021-01-01T05:00:00.000Z | 2021-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.004 | Server | During [Juicy Mix](https://attack.mitre.org/campaigns/C0044), [OilRig](https://attack.mitre.org/groups/G0049) compromised an Israeli job portal to use for a C2 server.(Citation: ESET OilRig Campaigns Sep 2023) |  | activity--juicy-mix | 2022-01-01T05:00:00.000Z | 2022-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1132.001 | Standard Encoding | During [Juicy Mix](https://attack.mitre.org/campaigns/C0044), [OilRig](https://attack.mitre.org/groups/G0049) used a VBS script to send the Base64-encoded name of the compromised computer to C2.(Citation: ESET OilRig Campaigns Sep 2023) |  | activity--juicy-mix | 2022-01-01T05:00:00.000Z | 2022-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | During [Outer Space](https://attack.mitre.org/campaigns/C0042), [OilRig](https://attack.mitre.org/groups/G0049) downloaded additional tools to comrpomised infrastructure.(Citation: ESET OilRig Campaigns Sep 2023) |  | activity--outer-space | 2021-01-01T05:00:00.000Z | 2021-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | During [Juicy Mix](https://attack.mitre.org/campaigns/C0044), [OilRig](https://attack.mitre.org/groups/G0049) used a script to send the name of the compromised host via HTTP `POST` to register it with C2.(Citation: ESET OilRig Campaigns Sep 2023) |  | activity--juicy-mix | 2022-01-01T05:00:00.000Z | 2022-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Discovery | T1217 | Browser Information Discovery | During [Juicy Mix](https://attack.mitre.org/campaigns/C0044), [OilRig](https://attack.mitre.org/groups/G0049) used the CDumper (Chrome browser) and EDumper (Edge browser) data stealers to collect cookies, browsing history, and credentials.(Citation: ESET OilRig Campaigns Sep 2023) |  | activity--juicy-mix | 2022-01-01T05:00:00.000Z | 2022-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.003 | Credentials from Web Browsers | During [Juicy Mix](https://attack.mitre.org/campaigns/C0044), [OilRig](https://attack.mitre.org/groups/G0049) used the CDumper (Chrome browser) and EDumper (Edge browser) to collect credentials.(Citation: ESET OilRig Campaigns Sep 2023) |  | activity--juicy-mix | 2022-01-01T05:00:00.000Z | 2022-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | During [Juicy Mix](https://attack.mitre.org/campaigns/C0044), [OilRig](https://attack.mitre.org/groups/G0049) used VBS droppers to schedule tasks for persistence.(Citation: ESET OilRig Campaigns Sep 2023) |  | activity--juicy-mix | 2022-01-01T05:00:00.000Z | 2022-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | During [Outer Space](https://attack.mitre.org/campaigns/C0042), [OilRig](https://attack.mitre.org/groups/G0049) used VBS droppers to deploy malware.(Citation: ESET OilRig Campaigns Sep 2023) |  | activity--outer-space | 2021-01-01T05:00:00.000Z | 2021-12-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.001 | LSASS Memory | [OilRig](https://attack.mitre.org/groups/G0049) has used credential dumping tools such as [Mimikatz](https://attack.mitre.org/software/S0002) to steal credentials to accounts logged into the compromised system and to Outlook Web Access.(Citation: Unit42 OilRig Playbook 2023)(Citation: FireEye APT34 Webinar Dec 2017)(Citation: FireEye APT35 2018)(Citation: FireEye APT34 July 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.004 | LSA Secrets | [OilRig](https://attack.mitre.org/groups/G0049) has used credential dumping tools such as [LaZagne](https://attack.mitre.org/software/S0349) to steal credentials to accounts logged into the compromised system and to Outlook Web Access.(Citation: Unit42 OilRig Playbook 2023)(Citation: FireEye APT34 Webinar Dec 2017)(Citation: FireEye APT35 2018)(Citation: FireEye APT34 July 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.005 | Cached Domain Credentials | [OilRig](https://attack.mitre.org/groups/G0049) has used credential dumping tools such as [LaZagne](https://attack.mitre.org/software/S0349) to steal credentials to accounts logged into the compromised system and to Outlook Web Access.(Citation: Unit42 OilRig Playbook 2023)(Citation: FireEye APT34 Webinar Dec 2017)(Citation: FireEye APT35 2018)(Citation: FireEye APT34 July 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | [OilRig](https://attack.mitre.org/groups/G0049) has used PowerShell to upload files from compromised systems.(Citation: Trend Micro Earth Simnavaz October 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1007 | System Service Discovery | [OilRig](https://attack.mitre.org/groups/G0049) has used <code>sc query</code> on a victim to gather information about services.(Citation: Palo Alto OilRig May 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1008 | Fallback Channels | [OilRig](https://attack.mitre.org/groups/G0049) malware ISMAgent falls back to its DNS tunneling mechanism if it is unable to reach the C2 server over HTTP.(Citation: OilRig ISMAgent July 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1012 | Query Registry | [OilRig](https://attack.mitre.org/groups/G0049) has used <code>reg query “HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default”</code> on a victim to query the Registry.(Citation: Palo Alto OilRig May 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | [OilRig](https://attack.mitre.org/groups/G0049) has run <code>ipconfig /all</code> on a victim.(Citation: Palo Alto OilRig May 2016)(Citation: Palo Alto OilRig Oct 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | [OilRig](https://attack.mitre.org/groups/G0049) has used Remote Desktop Protocol for lateral movement. The group has also used tunneling tools to tunnel RDP into the environment.(Citation: Unit42 OilRig Playbook 2023)(Citation: FireEye APT34 Webinar Dec 2017)(Citation: Crowdstrike GTR2020 Mar 2020)(Citation: Symantec Crambus OCT 2023)(Citation: Symantec Crambus OCT 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.004 | SSH | [OilRig](https://attack.mitre.org/groups/G0049) has used Putty to access compromised systems.(Citation: Unit42 OilRig Playbook 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1025 | Data from Removable Media | [OilRig](https://attack.mitre.org/groups/G0049) has used Wireshark’s usbcapcmd utility to capture USB traffic.(Citation: Symantec Crambus OCT 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.005 | Indicator Removal from Tools | [OilRig](https://attack.mitre.org/groups/G0049) has tested malware samples to determine AV detection and subsequently modified the samples to ensure AV evasion.(Citation: Palo Alto OilRig April 2017)(Citation: Unit42 OilRig Nov 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | [OilRig](https://attack.mitre.org/groups/G0049) has encrypted and encoded data in its malware, including by using base64.(Citation: FireEye APT34 Dec 2017)(Citation: Unit 42 QUADAGENT July 2018)(Citation: Unit42 OilRig Playbook 2023)(Citation: Crowdstrike Helix Kitten Nov 2018)(Citation: Unit42 OilRig Nov 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | [OilRig](https://attack.mitre.org/groups/G0049) has run <code>whoami</code> on a victim.(Citation: Palo Alto OilRig May 2016)(Citation: Palo Alto OilRig Oct 2016)(Citation: Check Point APT34 April 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036 | Masquerading | [OilRig](https://attack.mitre.org/groups/G0049) has used .doc file extensions to mask malicious executables.(Citation: Check Point APT34 April 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [OilRig](https://attack.mitre.org/groups/G0049) has named a downloaded copy of the Plink tunneling utility as \ProgramData\Adobe.exe.(Citation: Symantec Crambus OCT 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1046 | Network Service Discovery | [OilRig](https://attack.mitre.org/groups/G0049) has used the publicly available tool SoftPerfect Network Scanner as well as a custom tool called GOLDIRONY to conduct network scanning.(Citation: FireEye APT34 Webinar Dec 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | [OilRig](https://attack.mitre.org/groups/G0049) has used WMI for execution.(Citation: FireEye APT34 Webinar Dec 2017)(Citation: Symantec Crambus OCT 2023)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1048.003 | Exfiltration Over Unencrypted Non-C2 Protocol | [OilRig](https://attack.mitre.org/groups/G0049) has exfiltrated data via Microsoft Exchange and over FTP separately from its primary C2 channel over DNS.(Citation: Palo Alto OilRig Oct 2016)(Citation: Trend Micro Earth Simnavaz October 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | [OilRig](https://attack.mitre.org/groups/G0049) has used <code>netstat -an</code> on a victim to get a listing of network connections.(Citation: Palo Alto OilRig May 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [OilRig](https://attack.mitre.org/groups/G0049) has created scheduled tasks that run a VBScript to execute a payload on victim machines.(Citation: Unit 42 OopsIE! Feb 2018)(Citation: Unit 42 QUADAGENT July 2018)(Citation: FireEye APT34 July 2019)(Citation: Check Point APT34 April 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056.001 | Keylogging | [OilRig](https://attack.mitre.org/groups/G0049) has employed keyloggers including KEYPUNCH and LONGWATCH.(Citation: FireEye APT34 Webinar Dec 2017)(Citation: FireEye APT34 July 2019)(Citation: Symantec Crambus OCT 2023)	<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | [OilRig](https://attack.mitre.org/groups/G0049) has run <code>tasklist</code> on a victim's machine and used infostealers to capture processes.(Citation: Palo Alto OilRig May 2016)(Citation: Symantec Crambus OCT 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059 | Command and Scripting Interpreter | [OilRig](https://attack.mitre.org/groups/G0049) has used various types of scripting for execution.(Citation: FireEye APT34 Dec 2017)(Citation: OilRig ISMAgent July 2017)(Citation: Unit 42 OopsIE! Feb 2018)(Citation: Unit 42 QUADAGENT July 2018)(Citation: Unit42 OilRig Nov 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [OilRig](https://attack.mitre.org/groups/G0049) has used PowerShell scripts for execution, including use of a macro to run a PowerShell command to decode file contents.(Citation: FireEye APT34 Dec 2017)(Citation: OilRig New Delivery Oct 2017)(Citation: Crowdstrike Helix Kitten Nov 2018)(Citation: Trend Micro Earth Simnavaz October 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [OilRig](https://attack.mitre.org/groups/G0049) has used macros to deliver malware such as [QUADAGENT](https://attack.mitre.org/software/S0269) and [OopsIE](https://attack.mitre.org/software/S0264).(Citation: FireEye APT34 Dec 2017)(Citation: OilRig ISMAgent July 2017)(Citation: Unit 42 OopsIE! Feb 2018)(Citation: Unit 42 QUADAGENT July 2018)(Citation: Unit42 OilRig Nov 2018) [OilRig](https://attack.mitre.org/groups/G0049) has used batch scripts.(Citation: FireEye APT34 Dec 2017)(Citation: OilRig ISMAgent July 2017)(Citation: Unit 42 OopsIE! Feb 2018)(Citation: Unit 42 QUADAGENT July 2018)(Citation: Unit42 OilRig Nov 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | [OilRig](https://attack.mitre.org/groups/G0049) has used VBScript macros for execution on compromised hosts.(Citation: Check Point APT34 April 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1068 | Exploitation for Privilege Escalation | [OilRig](https://attack.mitre.org/groups/G0049) has exploited the Windows Kernel Elevation of Privilege vulnerability, CVE-2024-30088.(Citation: Trend Micro Earth Simnavaz October 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1069.001 | Local Groups | [OilRig](https://attack.mitre.org/groups/G0049) has used <code>net localgroup administrators</code> to find local administrators on compromised systems.(Citation: Palo Alto OilRig May 2016)(Citation: Symantec Crambus OCT 2023)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1069.002 | Domain Groups | [OilRig](https://attack.mitre.org/groups/G0049) has used <code>net group /domain</code>, <code>net group “domain admins” /domain</code>, and <code>net group “Exchange Trusted Subsystem” /domain</code> to find domain group permission settings.(Citation: Palo Alto OilRig May 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | [OilRig](https://attack.mitre.org/groups/G0049) has deleted files associated with their payload after execution.(Citation: FireEye APT34 Dec 2017)(Citation: Unit 42 OopsIE! Feb 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [OilRig](https://attack.mitre.org/groups/G0049) has used HTTP for C2.(Citation: Unit42 OilRig Playbook 2023)(Citation: FireEye APT34 Webinar Dec 2017)(Citation: FireEye APT34 July 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.004 | DNS | [OilRig](https://attack.mitre.org/groups/G0049) has used DNS for C2 including the publicly available <code>requestbin.net</code> tunneling service.(Citation: Unit42 OilRig Playbook 2023)(Citation: FireEye APT34 Webinar Dec 2017)(Citation: FireEye APT34 July 2019)(Citation: Check Point APT34 April 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [OilRig](https://attack.mitre.org/groups/G0049) has used compromised credentials to access other systems on a victim network.(Citation: Unit42 OilRig Playbook 2023)(Citation: FireEye APT34 Webinar Dec 2017)(Citation: Crowdstrike GTR2020 Mar 2020)(Citation: IBM ZeroCleare Wiper December 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.002 | Domain Accounts | <br>[OilRig](https://attack.mitre.org/groups/G0049) has used an exfiltration tool named STEALHOOK to retreive valid domain credentials.(Citation: Trend Micro Earth Simnavaz October 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [OilRig](https://attack.mitre.org/groups/G0049) has run <code>hostname</code> and <code>systeminfo</code> on a victim.(Citation: Palo Alto OilRig May 2016)(Citation: Palo Alto OilRig Oct 2016)(Citation: FireEye APT34 July 2019)(Citation: Check Point APT34 April 2021)(Citation: Symantec Crambus OCT 2023)<br>	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.001 | Local Account | [OilRig](https://attack.mitre.org/groups/G0049) has run <code>net user</code>, <code>net user /domain</code>, <code>net group “domain admins” /domain</code>, and <code>net group “Exchange Trusted Subsystem” /domain</code> to get account listings on a victim.(Citation: Palo Alto OilRig May 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | [OilRig](https://attack.mitre.org/groups/G0049) has run <code>net user</code>, <code>net user /domain</code>, <code>net group “domain admins” /domain</code>, and <code>net group “Exchange Trusted Subsystem” /domain</code> to get account listings on a victim.(Citation: Palo Alto OilRig May 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [OilRig](https://attack.mitre.org/groups/G0049) had downloaded remote files onto victim infrastructure.(Citation: FireEye APT34 Dec 2017)(Citation: Trend Micro Earth Simnavaz October 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110 | Brute Force | [OilRig](https://attack.mitre.org/groups/G0049) has used brute force techniques to obtain credentials.(Citation: FireEye APT34 Webinar Dec 2017)(Citation: IBM ZeroCleare Wiper December 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | [OilRig](https://attack.mitre.org/groups/G0049) has used reg.exe to modify system configuration.(Citation: Symantec Crambus OCT 2023)(Citation: Trend Micro Earth Simnavaz October 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1113 | Screen Capture | [OilRig](https://attack.mitre.org/groups/G0049) has a tool called CANDYKING to capture a screenshot of user's desktop.(Citation: FireEye APT34 Webinar Dec 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1115 | Clipboard Data | [OilRig](https://attack.mitre.org/groups/G0049) has used infostealer tools to copy clipboard data.(Citation: Symantec Crambus OCT 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1119 | Automated Collection | [OilRig](https://attack.mitre.org/groups/G0049) has used automated collection.(Citation: Unit42 OilRig Playbook 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1120 | Peripheral Device Discovery | [OilRig](https://attack.mitre.org/groups/G0049) has used tools to identify if a mouse is connected to a targeted system.(Citation: Check Point APT34 April 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence | T1133 | External Remote Services | [OilRig](https://attack.mitre.org/groups/G0049) uses remote services such as VPN, Citrix, or OWA to persist in an environment.(Citation: FireEye APT34 Webinar Dec 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1137.004 | Outlook Home Page | [OilRig](https://attack.mitre.org/groups/G0049) has abused the Outlook Home Page feature for persistence. [OilRig](https://attack.mitre.org/groups/G0049) has also used CVE-2017-11774 to roll back the initial patch designed to protect against Home Page abuse.(Citation: FireEye Outlook Dec 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | A [OilRig](https://attack.mitre.org/groups/G0049) macro has run a PowerShell command to decode file contents. [OilRig](https://attack.mitre.org/groups/G0049) has also used [certutil](https://attack.mitre.org/software/S0160) to decode base64-encoded files on victims.(Citation: FireEye APT34 Dec 2017)(Citation: OilRig New Delivery Oct 2017)(Citation: Unit 42 OopsIE! Feb 2018)(Citation: Crowdstrike GTR2020 Mar 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1195 | Supply Chain Compromise | [OilRig](https://attack.mitre.org/groups/G0049) has leveraged compromised organizations to conduct supply chain attacks on government entities.(Citation: Trend Micro Earth Simnavaz October 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1201 | Password Policy Discovery | [OilRig](https://attack.mitre.org/groups/G0049) has used net.exe in a script with <code>net accounts /domain</code> to find the password policy of a domain.(Citation: FireEye Targeted Attacks Middle East Banks) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | [OilRig](https://attack.mitre.org/groups/G0049) has exploited CVE-2024-30088 to run arbitrary code in the context of `SYSTEM`.(Citation: Trend Micro Earth Simnavaz October 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | [OilRig](https://attack.mitre.org/groups/G0049) has delivered malicious links to achieve execution on the target system.(Citation: Unit 42 OopsIE! Feb 2018)(Citation: Unit 42 QUADAGENT July 2018)(Citation: Crowdstrike Helix Kitten Nov 2018)(Citation: ClearSky OilRig Jan 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [OilRig](https://attack.mitre.org/groups/G0049) has delivered macro-enabled documents that required targets to click the "enable content" button to execute the payload on the system.(Citation: Unit 42 OopsIE! Feb 2018)(Citation: Unit 42 QUADAGENT July 2018)(Citation: Crowdstrike Helix Kitten Nov 2018)(Citation: Check Point APT34 April 2021)(Citation: ClearSky OilRig Jan 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.001 | Compiled HTML File | [OilRig](https://attack.mitre.org/groups/G0049) has used a CHM payload to load and execute another malicious file once delivered to a victim.(Citation: Palo Alto OilRig May 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1219 | Remote Access Tools | [OilRig](https://attack.mitre.org/groups/G0049) has incorporated remote monitoring and management (RMM) tools into their operations including [ngrok](https://attack.mitre.org/software/S0508).(Citation: Trend Micro Earth Simnavaz October 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1485 | Data Destruction | Historical APT34 activity included high-visibility disk-wiping operations intended to disrupt IT infrastructure. |  | activity--apt34-destructive-operations-2016-2019 | 2016 | 2019 | 高 | `source--unit42-iran-threat-evolution-2026` |
| Discovery, Stealth | T1497.001 | System Checks | [OilRig](https://attack.mitre.org/groups/G0049) has used macros to verify if a mouse is connected to a compromised machine.(Citation: Check Point APT34 April 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | [OilRig](https://attack.mitre.org/groups/G0049) has used web shells, often to maintain access to a victim network.(Citation: Unit42 OilRig Playbook 2023)(Citation: FireEye APT34 Webinar Dec 2017)(Citation: Crowdstrike GTR2020 Mar 2020)(Citation: Trend Micro Earth Simnavaz October 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | [OilRig](https://attack.mitre.org/groups/G0049) has used a compromised Domain Controller to create a service on a remote host.(Citation: Symantec Crambus OCT 2023)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.001 | Credentials In Files | [OilRig](https://attack.mitre.org/groups/G0049) has used credential dumping tools such as [LaZagne](https://attack.mitre.org/software/S0349) to steal credentials to accounts logged into the compromised system and to Outlook Web Access.(Citation: Unit42 OilRig Playbook 2023)(Citation: FireEye APT34 Webinar Dec 2017)(Citation: FireEye APT35 2018)(Citation: FireEye APT34 July 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1553.002 | Code Signing | [OilRig](https://attack.mitre.org/groups/G0049) has signed its malware with stolen certificates.(Citation: ClearSky OilRig Jan 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555 | Credentials from Password Stores | [OilRig](https://attack.mitre.org/groups/G0049) has used credential dumping tools such as [LaZagne](https://attack.mitre.org/software/S0349) to steal credentials to accounts logged into the compromised system and to Outlook Web Access.(Citation: Unit42 OilRig Playbook 2023)(Citation: FireEye APT34 Webinar Dec 2017)(Citation: FireEye APT35 2018)(Citation: FireEye APT34 July 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.003 | Credentials from Web Browsers | [OilRig](https://attack.mitre.org/groups/G0049) has used credential dumping tools such as [LaZagne](https://attack.mitre.org/software/S0349) to steal credentials to accounts logged into the compromised system and to Outlook Web Access.(Citation: Unit42 OilRig Playbook 2023)(Citation: FireEye APT34 Webinar Dec 2017)(Citation: FireEye APT35 2018)(Citation: FireEye APT34 July 2019) [OilRig](https://attack.mitre.org/groups/G0049) has also used tool named PICKPOCKET to dump passwords from web browsers.(Citation: FireEye APT34 July 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.004 | Windows Credential Manager | [OilRig](https://attack.mitre.org/groups/G0049) has used credential dumping tool named VALUEVAULT to steal credentials from the Windows Credential Manager.(Citation: FireEye APT34 July 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access, Defense Impairment, Persistence | T1556.002 | Password Filter DLL | [OilRig](https://attack.mitre.org/groups/G0049) has registered a password filter DLL in order to drop malware.(Citation: Trend Micro Earth Simnavaz October 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [OilRig](https://attack.mitre.org/groups/G0049) has sent spearphising emails with malicious attachments to potential victims using compromised and/or spoofed email accounts.(Citation: Unit 42 OopsIE! Feb 2018)(Citation: Unit 42 QUADAGENT July 2018)(Citation: Crowdstrike Helix Kitten Nov 2018)(Citation: ClearSky OilRig Jan 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | [OilRig](https://attack.mitre.org/groups/G0049) has sent spearphising emails with malicious links to potential victims.(Citation: Unit 42 OopsIE! Feb 2018)(Citation: ClearSky OilRig Jan 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.003 | Spearphishing via Service | [OilRig](https://attack.mitre.org/groups/G0049) has used LinkedIn to send spearphishing links.(Citation: FireEye APT34 July 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1572 | Protocol Tunneling | [OilRig](https://attack.mitre.org/groups/G0049) has used the Plink utility and other tools to create tunnels to C2 servers.(Citation: Unit42 OilRig Playbook 2023)(Citation: FireEye APT34 Webinar Dec 2017)(Citation: FireEye APT34 July 2019)(Citation: Symantec Crambus OCT 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573.002 | Asymmetric Cryptography | [OilRig](https://attack.mitre.org/groups/G0049) used the [PowerExchange](https://attack.mitre.org/software/S1173) utility and other tools to create tunnels to C2 servers.(Citation: FireEye APT34 Webinar Dec 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [OilRig](https://attack.mitre.org/groups/G0049) has set up fake VPN portals, conference sign ups, and job application websites to target victims.(Citation: ClearSky OilRig Jan 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1586.002 | Email Accounts | [OilRig](https://attack.mitre.org/groups/G0049) has compromised email accounts to send phishing emails.(Citation: ClearSky OilRig Jan 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | [OilRig](https://attack.mitre.org/groups/G0049) actively developed and used a series of downloaders during 2022.(Citation: ESET OilRig Downloaders DEC 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [OilRig](https://attack.mitre.org/groups/G0049) has made use of the publicly available tools including Plink and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: Symantec Crambus OCT 2023)(Citation: Trend Micro Earth Simnavaz October 2024)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.003 | Code Signing Certificates | [OilRig](https://attack.mitre.org/groups/G0049) has obtained stolen code signing certificates to digitally sign malware.(Citation: ClearSky OilRig Jan 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.001 | Upload Malware | [OilRig](https://attack.mitre.org/groups/G0049) has hosted malware on fake websites designed to target specific audiences.(Citation: ClearSky OilRig Jan 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1686.003 | Windows Host Firewall | [OilRig](https://attack.mitre.org/groups/G0049) has modified Windows firewall rules to enable remote access.(Citation: Symantec Crambus OCT 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 55件
- IOC観測: 55件
- 複数攻撃で観測: 0件
- 要レビュー候補: 55件
- 非IOC artifact観測: 1件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| APT34's historical mission set included destructive effects in addition to its better-known espionage activity. | 高 | `source--unit42-iran-threat-evolution-2026` |  |

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.
- {'statement': 'The 2026 source does not support assigning every wiper named in the regional retrospective exclusively to APT34.', 'confidence': 'high', 'evidence_refs': ['source--unit42-iran-threat-evolution-2026'], 'analyst_notes': ''}

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--apt34--4605945b1ccca9f5 | phone |  | 不明 | APT34/APT34 's hacker-picture/phone.txt | text-data | TLP:CLEAR | 中 |
| source--apt34--664060a2981e2a43 | README |  | 不明 | APT34/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--unit42-iran-threat-evolution-2026 | Iranian Cyber Threat Evolution: From MBR Wipers to Identity Weaponization | Palo Alto Networks Unit 42 | 2026 | https://unit42.paloaltonetworks.com/evolution-of-iran-cyber-threats/ | vendor-threat-assessment | TLP:CLEAR | 高 |
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
