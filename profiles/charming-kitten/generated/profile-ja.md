# Charming Kitten 脅威アクタープロファイル

- プロファイルID: `actor--charming-kitten`
- 状態: draft
- 更新日時: 2026-07-29T15:36:10Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Charming Kittenの標準化プロファイル。リポジトリ内の専用資料7件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Charming Kitten**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| APT35 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| COBALT ILLUSION | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| ITG18 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Magic Hound | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Mint Sandstorm | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Newscaster | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Phosphorus | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TA453 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Cutting Kitten | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Iran row 3; mapping requires review. |
| TG-2889 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Iran row 3; mapping requires review. |
| Ghambar | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Iran row 3; mapping requires review. |
| COBALT GYPSY | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Iran row 3; mapping requires review. |

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
| APT42 | overlaps-with | While there are behavior and software overlaps between [Magic Hound](https://attack.mitre.org/groups/G0059) and [APT42](https://attack.mitre.org/groups/G1044), they appear to be distinct entities and are tracked as separate entities by their originating vendor. | 高 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Magic Hound](https://attack.mitre.org/groups/G0059) is an Iranian-sponsored threat group that conducts long term, resource-intensive cyber espionage operations, likely on behalf of the Islamic Revolutionary Guard Corps. They have targeted European, U.S., and Middle Eastern government and military personnel, academics, journalists, and organizations such as the World Health Organization (WHO), via complex social engineering campaigns since at least 2014.(Citation: FireEye APT35 2018)(Citation: ClearSky Kittens Back 3 August 2020)(Citation: Certfa Charming Kitten January 2021)(Citation: Secureworks COBALT ILLUSION Threat Profile)(Citation: Proofpoint TA453 July2021) |
| Capability | PowerLess, CharmPower, DownPaper, TinyZBot, PupyRAT, Net, Impacket, ipconfig, FRP, netsh, Systeminfo, Mimikatz, Ping, Pupy, PsExec |
| Infrastructure |  |
| Victim | This threat actor targets governments and private sector entities for espionage and sabotage purposes. It is believed to be responsible for compromising U.S. Navy computers at the Navy Marine Corps Intranet in San Diego, the U.S. energy company Calpine Corporation, Saudi Aramco, Pemex, Qatar Airways, and Korean Air |
| Socio-political | Iran |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Cutting Kitten, TG-2889 | multiple-name-intersection | 高 | Iran | https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Cutting+Kitten%2C+TG-2889&n=1 |
| etda-threat-group-cards | ITG18 | single-alias-intersection | 中 | Iran | https://securityintelligence.com/posts/new-research-exposes-iranian-threat-group-operations/<br>https://securityintelligence.com/posts/itg18-operational-security-errors-plague-iranian-threat-group/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=ITG18&n=1 |
| etda-threat-group-cards | Magic Hound, APT 35, Cobalt Illusion, Charming Kitten | canonical-name | 高 | Iran | https://www.clearskysec.com/wp-content/uploads/2017/12/Charming_Kitten_2017.pdf<br>https://en.wikipedia.org/wiki/Charming_Kitten<br>https://vblocalhost.com/uploads/VB2021-Haeghebaert.pdf |
| etda-threat-group-cards | OilRig, APT 34, Helix Kitten, Chrysene | single-alias-intersection | 中 | Iran | https://unit42.paloaltonetworks.com/unit42-striking-oil-closer-look-adversary-infrastructure/<br>https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-november-helix-kitten/<br>https://marcoramilli.com/2019/08/07/oilrig-the-techniques-evolution-over-time/ |
| etda-threat-group-cards | Rocket Kitten, Newscaster, NewsBeef | single-alias-intersection | 中 | Iran | https://securelist.com/freezer-paper-around-free-meat/74503/<br>https://blog.checkpoint.com/wp-content/uploads/2015/11/rocket-kitten-report.pdf<br>https://www.trendmicro.de/cloud-content/us/pdfs/security-intelligence/white-papers/wp-the-spy-kittens-are-back.pdf |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Hazel Sandstorm | single-alias-intersection | 中 | Iran | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| microsoft-threat-actor-mapping | Mint Sandstorm | canonical-name | 高 | Iran | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Cutting Kitten | single-alias-intersection | 中 | IR, Iran (Islamic Republic of) | https://www.cfr.org/interactive/cyber-operations/itsecteam<br>https://www.justice.gov/usao-sdny/file/835061/download |
| misp-threat-actor | Charming Kitten | canonical-name | 高 | IR, Iran (Islamic Republic of) | https://en.wikipedia.org/wiki/Operation_Newscaster<br>https://iranthreats.github.io/resources/macdownloader-macos-malware/<br>https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2014/2014.05.28.NewsCaster_An_Iranian_Threat_Within_Social_Networks/file-2581720763-pdf.pdf |
| misp-threat-actor | Cleaver | multiple-name-intersection | 高 | IR, Iran (Islamic Republic of) | https://www.secureworks.com/research/the-curious-case-of-mia-ash<br>https://www.cfr.org/interactive/cyber-operations/operation-cleaver<br>http://www.secureworks.com/cyber-threat-intelligence/threats/suspected-iran-based-hacker-group-creates-network-of-fake-linkedin-profiles/ |
| misp-threat-actor | OilRig | single-alias-intersection | 中 | IR, Iran (Islamic Republic of) | https://blog.morphisec.com/iranian-fileless-cyberattack-on-israel-word-vulnerability<br>https://unit42.paloaltonetworks.com/unit42-striking-oil-closer-look-adversary-infrastructure/<br>https://unit42.paloaltonetworks.com/unit42-introducing-the-adversary-playbook-first-up-oilrig/ |
| misp-threat-actor | APT35 | multiple-name-intersection | 高 | IR | https://www.fireeye.com/content/dam/collateral/en/mtrends-2018.pdf<br>https://attack.mitre.org/groups/G0059/<br>https://www.cfr.org/interactive/cyber-operations/magic-hound |
| misp-threat-actor | TA453 | single-alias-intersection | 中 | IR | https://www.proofpoint.com/us/blog/threat-insight/ta453-refuses-be-bound-expectations<br>https://www.proofpoint.com/us/blog/threat-insight/badblood-ta453-targets-us-and-israeli-medical-research-personnel-credential |
| misp-microsoft-activity-group | Hazel Sandstorm | single-alias-intersection | 中 | IR, Iran | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Mint Sandstorm | canonical-name | 高 | IR, Iran | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | Cleaver - G0003 | single-alias-intersection | 中 |  | https://attack.mitre.org/wiki/Group/G0003<br>https://www.cylance.com/content/dam/cylance/pages/operation-cleaver/Cylance%20Operation%20Cleaver%20Report.pdf<br>http://www.secureworks.com/cyber-threat-intelligence/threats/suspected-iran-based-hacker-group-creates-network-of-fake-linkedin-profiles/ |
| misp-mitre-enterprise-intrusion-set | Charming Kitten - G0058 | canonical-name | 高 |  | https://attack.mitre.org/wiki/Group/G0058<br>http://www.clearskysec.com/wp-content/uploads/2017/12/Charming%20Kitten%202017.pdf |
| misp-mitre-enterprise-intrusion-set | Magic Hound - G0059 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0059<br>https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/ |
| misp-mitre-intrusion-set | Charming Kitten - G0058 | canonical-name | 高 |  | http://www.clearskysec.com/wp-content/uploads/2017/12/Charming_Kitten_2017.pdf<br>https://attack.mitre.org/groups/G0058 |
| misp-mitre-intrusion-set | Magic Hound - G0059 | mitre-external-id | 高 |  | http://www.clearskysec.com/wp-content/uploads/2017/12/Charming_Kitten_2017.pdf<br>https://attack.mitre.org/groups/G0059<br>https://blog.certfa.com/posts/charming-kitten-christmas-gift/ |
| misp-mitre-intrusion-set | Cleaver - G0003 | single-alias-intersection | 中 |  | http://www.secureworks.com/cyber-threat-intelligence/threats/suspected-iran-based-hacker-group-creates-network-of-fake-linkedin-profiles/<br>https://attack.mitre.org/groups/G0003<br>https://www.cylance.com/content/dam/cylance/pages/operation-cleaver/Cylance_Operation_Cleaver_Report.pdf |
| misp-mitre-intrusion-set | OilRig - G0049 | single-alias-intersection | 中 |  | http://researchcenter.paloaltonetworks.com/2016/05/the-oilrig-campaign-attacks-on-saudi-arabian-organizations-deliver-helminth-backdoor/<br>http://researchcenter.paloaltonetworks.com/2016/10/unit42-oilrig-malware-campaign-updates-toolset-and-expands-targets/<br>http://researchcenter.paloaltonetworks.com/2017/04/unit42-oilrig-actors-provide-glimpse-development-testing-efforts/ |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Cleaver | similar | misp-mitre-enterprise-intrusion-set | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Magic Hound | similar | misp-mitre-enterprise-intrusion-set | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| APT35 | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| APT42 | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| CHRYSENE | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Charming Kitten | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Cleaver | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Clever Kitten | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Cutting Kitten | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Flying Kitten | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
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
| malware--powerless | PowerLess | [PowerLess](https://attack.mitre.org/software/S1012) is a PowerShell-based modular backdoor that has been used by [Magic Hound](https://attack.mitre.org/groups/G0059) since at least 2022.(Citation: Cybereason PowerLess February 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--charmpower | CharmPower | [CharmPower](https://attack.mitre.org/software/S0674) is a PowerShell-based, modular backdoor that has been used by [Magic Hound](https://attack.mitre.org/groups/G0059) since at least 2022.(Citation: Check Point APT35 CharmPower January 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--downpaper | DownPaper | [DownPaper](https://attack.mitre.org/software/S0186) is a backdoor Trojan; its main functionality is to download and run second stage malware. (Citation: ClearSky Charming Kitten Dec 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--tinyzbot | TinyZBot | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--pupyrat | PupyRAT | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--impacket | Impacket | [Impacket](https://attack.mitre.org/software/S0357) is an open source collection of modules written in Python for programmatically constructing and manipulating network protocols. [Impacket](https://attack.mitre.org/software/S0357) contains several tools for remote service execution, Kerberos manipulation, Windows credential dumping, packet sniffing, and relay attacks.(Citation: Impacket Tools) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ipconfig | ipconfig | [ipconfig](https://attack.mitre.org/software/S0100) is a Windows utility that can be used to find information about a system's TCP/IP, DNS, DHCP, and adapter configuration. (Citation: TechNet Ipconfig) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--frp | FRP | [FRP](https://attack.mitre.org/software/S1144), which stands for Fast Reverse Proxy, is an openly available tool that is capable of exposing a server located behind a firewall or Network Address Translation (NAT) to the Internet. [FRP](https://attack.mitre.org/software/S1144) can support multiple protocols including TCP, UDP, and HTTP(S) and has been abused by threat actors to proxy command and control communications.(Citation: FRP GitHub)(Citation: Joint Cybersecurity Advisory Volt Typhoon June 2023)(Citation: RedCanary Mockingbird May 2020)(Citation: DFIR Phosphorus November 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--netsh | netsh | [netsh](https://attack.mitre.org/software/S0108) is a scripting utility used to interact with networking components on local or remote systems. (Citation: TechNet Netsh) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--systeminfo | Systeminfo | [Systeminfo](https://attack.mitre.org/software/S0096) is a Windows utility that can be used to gather detailed information about a computer. (Citation: TechNet Systeminfo) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ping | Ping | [Ping](https://attack.mitre.org/software/S0097) is an operating system utility commonly used to troubleshoot and verify network connections. (Citation: TechNet Ping) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--pupy | Pupy | [Pupy](https://attack.mitre.org/software/S0192) is an open source, cross-platform (Windows, Linux, OSX, Android) remote administration and post-exploitation tool. (Citation: GitHub Pupy) It is written in Python and can be generated as a payload in several different ways (Windows exe, Python file, PowerShell oneliner/file, Linux elf, APK, Rubber Ducky, etc.). (Citation: GitHub Pupy) [Pupy](https://attack.mitre.org/software/S0192) is publicly available on GitHub. (Citation: GitHub Pupy) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Cleaver | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

Cleaver

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 米国 | They have targeted European, U.S., and Middle Eastern government and military personnel, academics, journalists, and organizations such as the World Health Organization (WHO), via complex social engineering campaigns since at least 2014.(Citation: FireEye APT35 2018)(Citation: ClearSky Kitten | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 教育・研究 | They have targeted European, U.S., and Middle Eastern government and military personnel, academics, journalists, and organizations such as the World Health Organization (WHO), via complex social engineering campaigns since at least 2014.(Citation: FireEye APT35 2018)(Citation: ClearSky Kittens Back 3 August 2020)(Citation: Certfa Charming Kitten January 2 | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 防衛・軍事 | They have targeted European, U.S., and Middle Eastern government and military personnel, academics, journalists, and organizations such as the World Health Organization (WHO), via complex social engineering campaigns since at least 2014.(Citation: FireEye APT35 2018)(Citation: ClearSky Kittens Back 3 August 2020)(Citation: Certfa Charm | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | メディア・報道 | They have targeted European, U.S., and Middle Eastern government and military personnel, academics, journalists, and organizations such as the World Health Organization (WHO), via complex social engineering campaigns since at least 2014.(Citation: FireEye APT35 2018)(Citation: ClearSky Kittens Back 3 August 2020)(Citation: Certfa Charming Kitten January 2021)(Citation | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 製造・産業 | They have targeted European, U.S., and Middle Eastern government and military personnel, academics, journalists, and organizations such as the World Health Organization (WHO), via complex social engineering campaigns since at least 2014.(Citation: FireEye APT35 2018)(Citation: ClearSky Kittens Back 3 August 2020)(Citation: Certfa Charming Kitten January 2021)(Citation: Secureworks COBALT ILLUSION Threat Profile)(Citation: Proofpoint TA453 July2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | Energy | Targeting text indicates the Energy sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Government | Targeting text indicates the Government sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1` |
| sectors | Technology | Targeting text indicates the Technology sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.001 | LSASS Memory | [Magic Hound](https://attack.mitre.org/groups/G0059) has stolen domain credentials by dumping LSASS process memory using Task Manager, comsvcs.dll, and from a Microsoft Active Directory Domain Controller using [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: FireEye APT35 2018)(Citation: DFIR Report APT35 ProxyShell March 2022)(Citation: DFIR Phosphorus November 2021)(Citation: Microsoft Iranian Threat Actor Trends November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | [Magic Hound](https://attack.mitre.org/groups/G0059) has used a web shell to exfiltrate a ZIP file containing a dump of LSASS memory on a compromised machine.(Citation: DFIR Report APT35 ProxyShell March 2022)(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | [Magic Hound](https://attack.mitre.org/groups/G0059) malware gathers the victim's local IP address, MAC address, and external IP address.(Citation: Unit 42 Magic Hound Feb 2017)(Citation: DFIR Report APT35 ProxyShell March 2022)(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016.001 | Internet Connection Discovery | [Magic Hound](https://attack.mitre.org/groups/G0059) has conducted a network call out to a specific website as part of their initial discovery activity.(Citation: DFIR Phosphorus November 2021)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016.002 | Wi-Fi Discovery | [Magic Hound](https://attack.mitre.org/groups/G0059) has collected names and passwords of all Wi-Fi networks to which a device has previously connected.(Citation: Check Point APT35 CharmPower January 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | [Magic Hound](https://attack.mitre.org/groups/G0059) has used [Ping](https://attack.mitre.org/software/S0097) for discovery on targeted networks.(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | [Magic Hound](https://attack.mitre.org/groups/G0059) has used Remote Desktop Services to copy tools on targeted systems.(Citation: DFIR Report APT35 ProxyShell March 2022)(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027 | Obfuscated Files or Information | tional security solutions. This includes multi-stage infection chains and reliance on legitimate services like Cloudflare to mask their infrastructure. T1027: Obfuscated Files or Information Collection Exfiltration over C2 Channel TA455 uses its established C2 channel, facilitated through GitHub and encoded communication, to exfiltrate collected data from compromised systems. T1041: Exfiltration Over C2 Channel |  |  | 不明 | 不明 | 中 | `source--charming-kitten--723fe9a87e44f1ca` |
| Stealth | T1027.010 | Command Obfuscation | [Magic Hound](https://attack.mitre.org/groups/G0059) has used base64-encoded commands.(Citation: Unit 42 Magic Hound Feb 2017)(Citation: Microsoft Iranian Threat Actor Trends November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | [Magic Hound](https://attack.mitre.org/groups/G0059) malware has used base64-encoded files and has also encrypted embedded strings with AES.(Citation: Unit 42 Magic Hound Feb 2017)(Citation: Microsoft Iranian Threat Actor Trends November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | [Magic Hound](https://attack.mitre.org/groups/G0059) malware has obtained the victim username and sent it to the C2 server.(Citation: Unit 42 Magic Hound Feb 2017)(Citation: DFIR Report APT35 ProxyShell March 2022)(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.004 | Masquerade Task or Service | [Magic Hound](https://attack.mitre.org/groups/G0059) has named a malicious script CacheTask.bat to mimic a legitimate task.(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [Magic Hound](https://attack.mitre.org/groups/G0059) has used `dllhost.exe` to mask Fast Reverse Proxy (FRP) and `MicrosoftOutLookUpdater.exe` for Plink.(Citation: DFIR Report APT35 ProxyShell March 2022)(Citation: DFIR Phosphorus November 2021)(Citation: Microsoft Iranian Threat Actor Trends November 2021) |  |  | 不明 | 不明 | 高 | `source--charming-kitten--723fe9a87e44f1ca`, `source--mitre-attack-19-1` |
| Stealth | T1036.010 | Masquerade Account Name | [Magic Hound](https://attack.mitre.org/groups/G0059) has created local accounts named `help` and `DefaultAccount` on compromised machines.(Citation: DFIR Report APT35 ProxyShell March 2022)(Citation: Microsoft Iranian Threat Actor Trends November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | nnel TA455 uses its established C2 channel, facilitated through GitHub and encoded communication, to exfiltrate collected data from compromised systems. T1041: Exfiltration Over C2 Channel |  |  | 不明 | 不明 | 中 | `source--charming-kitten--723fe9a87e44f1ca` |
| Discovery | T1046 | Network Service Discovery | [Magic Hound](https://attack.mitre.org/groups/G0059) has used KPortScan 3.0 to perform SMB, RDP, and LDAP scanning.(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | [Magic Hound](https://attack.mitre.org/groups/G0059) has used a tool to run `cmd /c wmic computersystem get domain` for discovery.(Citation: DFIR Report APT35 ProxyShell March 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | [Magic Hound](https://attack.mitre.org/groups/G0059) has used quser.exe to identify existing RDP connections.(Citation: DFIR Report APT35 ProxyShell March 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [Magic Hound](https://attack.mitre.org/groups/G0059) has used scheduled tasks to establish persistence and execution.(Citation: DFIR Report APT35 ProxyShell March 2022)(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--charming-kitten--9b4fbd2a0eb8ca99`, `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056.001 | Keylogging | [Magic Hound](https://attack.mitre.org/groups/G0059) malware is capable of keylogging.(Citation: Unit 42 Magic Hound Feb 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | [Magic Hound](https://attack.mitre.org/groups/G0059) malware can list running processes.(Citation: Unit 42 Magic Hound Feb 2017) |  |  | 不明 | 不明 | 高 | `source--charming-kitten--9b4fbd2a0eb8ca99`, `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [Magic Hound](https://attack.mitre.org/groups/G0059) has used PowerShell for execution and privilege escalation.(Citation: Unit 42 Magic Hound Feb 2017)(Citation: FireEye APT35 2018)(Citation: DFIR Report APT35 ProxyShell March 2022)(Citation: DFIR Phosphorus November 2021)(Citation: Microsoft Iranian Threat Actor Trends November 2021) |  |  | 不明 | 不明 | 高 | `source--charming-kitten--9b4fbd2a0eb8ca99`, `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [Magic Hound](https://attack.mitre.org/groups/G0059) has used the command-line interface for code execution.(Citation: Unit 42 Magic Hound Feb 2017)(Citation: DFIR Report APT35 ProxyShell March 2022)(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.004 | Unix Shell | nitial Access: SpearphishingLink T1566.002 Execution: CommandandScriptingInterpreter: PowerShell T1059.001 Execution: CommandandScriptingInterpreter: UnixShell T1059.004 Persistence: Boot or LogonAutostart Execution: RegistryRunKeys/StartupFolder T1547.001 Persistence: ScheduledTask/Job: ScheduledTask T1053.005 Discovery: SystemInformationDiscovery T1082 Discovery: ProcessDiscovery T1057 CommandandControl: ApplicationLayer Protocol: WebProtocols |  |  | 不明 | 不明 | 中 | `source--charming-kitten--9b4fbd2a0eb8ca99` |
| Execution | T1059.005 | Visual Basic | [Magic Hound](https://attack.mitre.org/groups/G0059) malware has used VBS scripts for execution.(Citation: Unit 42 Magic Hound Feb 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.003 | Clear Command History | [Magic Hound](https://attack.mitre.org/groups/G0059) has removed mailbox export requests from compromised Exchange servers.(Citation: DFIR Report APT35 ProxyShell March 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | [Magic Hound](https://attack.mitre.org/groups/G0059) has deleted and overwrote files to cover tracks.(Citation: Unit 42 Magic Hound Feb 2017)(Citation: FireEye APT35 2018)(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071 | Application Layer Protocol | [Magic Hound](https://attack.mitre.org/groups/G0059) malware has used IRC for C2.(Citation: Unit 42 Magic Hound Feb 2017)(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [Magic Hound](https://attack.mitre.org/groups/G0059) has used HTTP for C2.(Citation: Unit 42 Magic Hound Feb 2017)(Citation: DFIR Report APT35 ProxyShell March 2022)(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--charming-kitten--9b4fbd2a0eb8ca99`, `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.001 | Default Accounts | [Magic Hound](https://attack.mitre.org/groups/G0059) enabled and used the default system managed account, DefaultAccount, via `"powershell.exe" /c net user DefaultAccount /active:yes` to connect to a targeted Exchange server over RDP.(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.002 | Domain Accounts | [Magic Hound](https://attack.mitre.org/groups/G0059) has used domain administrator accounts after dumping LSASS process memory.(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [Magic Hound](https://attack.mitre.org/groups/G0059) malware has used a PowerShell command to check the victim system architecture to determine if it is an x64 machine. Other malware has obtained the OS version, UUID, and computer/host name to send to the C2 server.(Citation: Unit 42 Magic Hound Feb 2017)(Citation: DFIR Report APT35 ProxyShell March 2022)(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--charming-kitten--9b4fbd2a0eb8ca99`, `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | [Magic Hound](https://attack.mitre.org/groups/G0059) malware can list a victim's logical drives and the type, as well the total/free space of the fixed devices. Other malware can list a directory's contents.(Citation: Unit 42 Magic Hound Feb 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.003 | Email Account | [Magic Hound](https://attack.mitre.org/groups/G0059) has used Powershell to discover email accounts.(Citation: DFIR Report APT35 ProxyShell March 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090 | Proxy | [Magic Hound](https://attack.mitre.org/groups/G0059) has used Fast Reverse Proxy (FRP) for RDP traffic.(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1098.002 | Additional Email Delegate Permissions | [Magic Hound](https://attack.mitre.org/groups/G0059) granted compromised email accounts read access to the email boxes of additional targeted accounts. The group then was able to authenticate to the intended victim's OWA (Outlook Web Access) portal and read hundreds of email communications for information on Middle East organizations.(Citation: FireEye APT35 2018)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1098.007 | Additional Local or Domain Groups | [Magic Hound](https://attack.mitre.org/groups/G0059) has added a user named DefaultAccount to the Administrators and Remote Desktop Users groups.(Citation: DFIR Report APT35 ProxyShell March 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102.001 | Dead Drop Resolver | ss within seemingly innocuous files on a GitHub repository, they can retrieve it while blending in with legitimate users, making detection more difficult. T1102.001: Web Service: Dead Drop Resolver: GitHub Defense Evasion Impersonation of Other Threat Actors TA455 deliberately mimics tactics and tools associated with North Korean Lazarus APT Group, creating intentional misattribution in an attempt to deflect blame and complica |  |  | 不明 | 不明 | 中 | `source--charming-kitten--723fe9a87e44f1ca` |
| Command And Control | T1102.002 | Bidirectional Communication | [Magic Hound](https://attack.mitre.org/groups/G0059) malware can use a SOAP Web service to communicate with its C2 server.(Citation: Unit 42 Magic Hound Feb 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [Magic Hound](https://attack.mitre.org/groups/G0059) has downloaded additional code and files from servers onto victims.(Citation: Unit 42 Magic Hound Feb 2017)(Citation: DFIR Report APT35 ProxyShell March 2022)(Citation: DFIR Phosphorus November 2021)(Citation: Microsoft Iranian Threat Actor Trends November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | [Magic Hound](https://attack.mitre.org/groups/G0059) has modified Registry settings for security tools.(Citation: DFIR Report APT35 ProxyShell March 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1113 | Screen Capture | [Magic Hound](https://attack.mitre.org/groups/G0059) malware can take a screenshot and upload the file to its C2 server.(Citation: Unit 42 Magic Hound Feb 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114 | Email Collection | [Magic Hound](https://attack.mitre.org/groups/G0059) has compromised email credentials in order to steal sensitive data.(Citation: Certfa Charming Kitten January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114.001 | Local Email Collection | [Magic Hound](https://attack.mitre.org/groups/G0059) has collected .PST archives.(Citation: FireEye APT35 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114.002 | Remote Email Collection | [Magic Hound](https://attack.mitre.org/groups/G0059) has exported emails from compromised Exchange servers including through use of the cmdlet `New-MailboxExportRequest.`(Citation: DFIR Report APT35 ProxyShell March 2022)(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1136.001 | Local Account | [Magic Hound](https://attack.mitre.org/groups/G0059) has created local accounts named `help` and `DefaultAccount` on compromised machines.(Citation: DFIR Report APT35 ProxyShell March 2022)(Citation: Microsoft Iranian Threat Actor Trends November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1189 | Drive-by Compromise | [Magic Hound](https://attack.mitre.org/groups/G0059) has conducted watering-hole attacks through media and magazine websites.(Citation: ClearSky Kittens Back 3 August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [Magic Hound](https://attack.mitre.org/groups/G0059) has exploited the Log4j utility (CVE-2021-44228), on-premises MS Exchange servers via "ProxyShell" (CVE-2021-34473, CVE-2021-34523, CVE-2021-31207), and Fortios SSL VPNs (CVE-2018-13379).(Citation: Check Point APT35 CharmPower January 2022)(Citation: DFIR Report APT35 ProxyShell March 2022)(Citation: Cybereason PowerLess February 2022)(Citation: DFIR Phosphorus November 2021)(Citation: Microsoft Iranian Threat Actor Trends November 2021)(Citation: Microsoft Log4j Vulnerability Exploitation December 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | [Magic Hound](https://attack.mitre.org/groups/G0059) has attempted to lure victims into opening malicious links embedded in emails.(Citation: ClearSky Kittens Back 3 August 2020)(Citation: Certfa Charming Kitten January 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [Magic Hound](https://attack.mitre.org/groups/G0059) has attempted to lure victims into opening malicious email attachments.(Citation: ClearSky Kittens Back 3 August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.011 | Rundll32 | [Magic Hound](https://attack.mitre.org/groups/G0059) has used rundll32.exe to execute MiniDump from comsvcs.dll when dumping LSASS memory.(Citation: DFIR Report APT35 ProxyShell March 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1482 | Domain Trust Discovery | [Magic Hound](https://attack.mitre.org/groups/G0059) has used a web shell to execute `nltest /trusted_domains` to identify trust relationships.(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1486 | Data Encrypted for Impact | [Magic Hound](https://attack.mitre.org/groups/G0059) has used BitLocker and DiskCryptor to encrypt targeted workstations. (Citation: DFIR Phosphorus November 2021)(Citation: Microsoft Iranian Threat Actor Trends November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | [Magic Hound](https://attack.mitre.org/groups/G0059) has used multiple web shells to gain execution.(Citation: DFIR Report APT35 ProxyShell March 2022)(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [Magic Hound](https://attack.mitre.org/groups/G0059) malware has used Registry Run keys to establish persistence.(Citation: Unit 42 Magic Hound Feb 2017)(Citation: DFIR Phosphorus November 2021)(Citation: Microsoft Iranian Threat Actor Trends November 2021) |  |  | 不明 | 不明 | 高 | `source--charming-kitten--9b4fbd2a0eb8ca99`, `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | [Magic Hound](https://attack.mitre.org/groups/G0059) has used gzip to archive dumped LSASS process memory and RAR to stage and compress local folders.(Citation: FireEye APT35 2018)(Citation: DFIR Report APT35 ProxyShell March 2022)(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.003 | Hidden Window | [Magic Hound](https://attack.mitre.org/groups/G0059) malware has a function to determine whether the C2 server wishes to execute the newly dropped file in a hidden window.(Citation: Unit 42 Magic Hound Feb 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | ceDevelopment:AcquireInfrastructure: Domains T1583.001 ResourceDevelopment: EstablishAccounts: Email Accounts T1585.002 Initial Access: SpearphishingAttachment T1566.001 Initial Access: SpearphishingLink T1566.002 Execution: CommandandScriptingInterpreter: PowerShell T1059.001 Execution: CommandandScriptingInterpreter: UnixShell T1059.004 Persistence: Boot or LogonAutostart Execution: RegistryRunKeys/StartupFolder T1547.001 Persistence: Schedule |  |  | 不明 | 不明 | 中 | `source--charming-kitten--723fe9a87e44f1ca`, `source--charming-kitten--9b4fbd2a0eb8ca99` |
| Initial Access | T1566.002 | Spearphishing Link | [Magic Hound](https://attack.mitre.org/groups/G0059) has sent malicious URL links through email to victims. In some cases the URLs were shortened or linked to Word documents with malicious macros that executed PowerShells scripts to download [Pupy](https://attack.mitre.org/software/S0192).(Citation: Secureworks Cobalt Gypsy Feb 2017)(Citation: ClearSky Kittens Back 3 August 2020)(Citation: Certfa Charming Kitten January 2021)(Citation: Microsoft Iranian Threat Actor Trends November 2021) |  |  | 不明 | 不明 | 高 | `source--charming-kitten--723fe9a87e44f1ca`, `source--charming-kitten--9b4fbd2a0eb8ca99`, `source--mitre-attack-19-1` |
| Initial Access | T1566.003 | Spearphishing via Service | [Magic Hound](https://attack.mitre.org/groups/G0059) used various social media channels (such as LinkedIn) as well as messaging services (such as WhatsApp) to spearphish victims.(Citation: SecureWorks Mia Ash July 2017)(Citation: Microsoft Phosphorus Mar 2019)(Citation: ClearSky Kittens Back 3 August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567 | Exfiltration Over Web Service | [Magic Hound](https://attack.mitre.org/groups/G0059) has used the Telegram API `sendMessage` to relay data on compromised devices.(Citation: Google Iran Threats October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1570 | Lateral Tool Transfer | [Magic Hound](https://attack.mitre.org/groups/G0059) has copied tools within a compromised network using RDP.(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1571 | Non-Standard Port | [Magic Hound](https://attack.mitre.org/groups/G0059) malware has communicated with its C2 server over TCP ports 4443 and 10151 using HTTP.(Citation: Unit 42 Magic Hound Feb 2017)(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1572 | Protocol Tunneling | [Magic Hound](https://attack.mitre.org/groups/G0059) has used Plink to tunnel RDP over SSH.(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573 | Encrypted Channel | [Magic Hound](https://attack.mitre.org/groups/G0059) has used an encrypted http proxy in C2 communications.(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1574.002 | MITRE ATT&CK T1574.002 | L instead of the legitimate one. This technique allows them to execute malicious code within the context of a trusted process, making it harder to detect. T1574.002: DLL Side- Loading Discovery IP Address Discovery Determining the victim's IP address is crucial for the attackers to assess the target's location and potentially tailor their attacks based on geographic region or organizational affiliation. TA455 utilizes the website a |  |  | 不明 | 不明 | 中 | `source--charming-kitten--723fe9a87e44f1ca` |
| Resource Development | T1583.001 | Domains | [Magic Hound](https://attack.mitre.org/groups/G0059) has registered fraudulent domains such as "mail-newyorker.com" and "news12.com.recover-session-service.site" to target specific victims with phishing attacks.(Citation: Certfa Charming Kitten January 2021) |  |  | 不明 | 不明 | 高 | `source--charming-kitten--9b4fbd2a0eb8ca99`, `source--mitre-attack-19-1` |
| Resource Development | T1583.006 | Web Services | [Magic Hound](https://attack.mitre.org/groups/G0059) has acquired Amazon S3 buckets to use in C2.(Citation: Check Point APT35 CharmPower January 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.001 | Domains | [Magic Hound](https://attack.mitre.org/groups/G0059) has used compromised domains to host links targeted to specific phishing victims.(Citation: ClearSky Kittens Back 3 August 2020)(Citation: Proofpoint TA453 July2021)(Citation: Certfa Charming Kitten January 2021)(Citation: Google Iran Threats October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.001 | Social Media Accounts | [Magic Hound](https://attack.mitre.org/groups/G0059) has created fake LinkedIn and other social media accounts to contact targets and convince them--through messages and voice communications--to open malicious links.(Citation: ClearSky Kittens Back 3 August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.002 | Email Accounts | [Magic Hound](https://attack.mitre.org/groups/G0059) has established email accounts using fake personas for spearphishing operations.(Citation: IBM ITG18 2020)(Citation: Proofpoint TA453 March 2021) |  |  | 不明 | 不明 | 高 | `source--charming-kitten--9b4fbd2a0eb8ca99`, `source--mitre-attack-19-1` |
| Resource Development | T1586.002 | Email Accounts | [Magic Hound](https://attack.mitre.org/groups/G0059) has compromised personal email accounts through the use of legitimate credentials and gathered additional victim information.(Citation: IBM ITG18 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [Magic Hound](https://attack.mitre.org/groups/G0059) has obtained and used tools like [Havij](https://attack.mitre.org/software/S0224), [sqlmap](https://attack.mitre.org/software/S0225), Metasploit, [Mimikatz](https://attack.mitre.org/software/S0002), and Plink.(Citation: Check Point Rocket Kitten)(Citation: FireEye APT35 2018)(Citation: Check Point APT35 CharmPower January 2022)(Citation: DFIR Phosphorus November 2021)(Citation: Microsoft Iranian Threat Actor Trends November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589 | Gather Victim Identity Information | [Magic Hound](https://attack.mitre.org/groups/G0059) has acquired mobile phone numbers of potential targets, possibly for mobile malware or additional phishing operations.(Citation: Proofpoint TA453 July2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589.001 | Credentials | [Magic Hound](https://attack.mitre.org/groups/G0059) gathered credentials from two victims that they then attempted to validate across 75 different websites. [Magic Hound](https://attack.mitre.org/groups/G0059) has also collected credentials from over 900 Fortinet VPN servers in the US, Europe, and Israel.(Citation: IBM ITG18 2020)(Citation: Microsoft Iranian Threat Actor Trends November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589.002 | Email Addresses | [Magic Hound](https://attack.mitre.org/groups/G0059) has identified high-value email accounts in academia, journalism, NGO's, foreign policy, and national security for targeting.(Citation: Proofpoint TA453 July2021)(Citation: Google Iran Threats October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1590.005 | IP Addresses | [Magic Hound](https://attack.mitre.org/groups/G0059) has captured the IP addresses of visitors to their phishing sites.(Citation: Google Iran Threats October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1591.001 | Determine Physical Locations | [Magic Hound](https://attack.mitre.org/groups/G0059) has collected location information from visitors to their phishing sites.(Citation: Google Iran Threats October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1592 | Gather Victim Host Information | potentially tailor their attacks based on geographic region or organizational affiliation. TA455 utilizes the website api[.]ipify[.]org for this purpose. T1592: Gather Victim Host Information |  |  | 不明 | 不明 | 中 | `source--charming-kitten--723fe9a87e44f1ca` |
| Reconnaissance | T1592.002 | Software | [Magic Hound](https://attack.mitre.org/groups/G0059) has captured the user-agent strings from visitors to their phishing sites.(Citation: Google Iran Threats October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1595.002 | Vulnerability Scanning | [Magic Hound](https://attack.mitre.org/groups/G0059) has conducted widespread scanning to identify public-facing systems vulnerable to CVE-2021-44228 in Log4j and ProxyShell vulnerabilities; CVE-2021-26855, CVE-2021-26857, CVE-2021-26858, and CVE-2021-27065 in on-premises MS Exchange Servers; and CVE-2018-13379 in Fortinet FortiOS SSL VPNs.(Citation: Check Point APT35 CharmPower January 2022)(Citation: Microsoft Iranian Threat Actor Trends November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1598.003 | Spearphishing Link | [Magic Hound](https://attack.mitre.org/groups/G0059) has used SMS and email messages with links designed to steal credentials or track victims.(Citation: Certfa Charming Kitten January 2021)(Citation: ClearSky Kittens Back 3 August 2020)(Citation: Proofpoint TA453 March 2021)(Citation: Proofpoint TA453 July2021)(Citation: Google Iran Threats October 2021)(Citation: Microsoft Iranian Threat Actor Trends November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | [Magic Hound](https://attack.mitre.org/groups/G0059) has disabled antivirus services on targeted systems in order to upload malicious payloads.(Citation: DFIR Report APT35 ProxyShell March 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685.001 | Disable or Modify Windows Event Log | [Magic Hound](https://attack.mitre.org/groups/G0059) has executed scripts to disable the event log service.(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1686.003 | Windows Host Firewall | [Magic Hound](https://attack.mitre.org/groups/G0059) has added the following rule to a victim's Windows firewall to allow RDP traffic - `"netsh" advfirewall firewall add rule name="Terminal Server" dir=in action=allow protocol=TCP localport=3389`.(Citation: DFIR Report APT35 ProxyShell March 2022)(Citation: DFIR Phosphorus November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 109件
- IOC観測: 160件
- 複数攻撃で観測: 0件
- 要レビュー候補: 9件
- 非IOC artifact観測: 7件（`artifacts.csv`）

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
| source--charming-kitten--368647d362b4c669 | 2023 08 10 cyber brief no 01 2023 |  | 2023-08-10 | Charming Kitten/2023-08-10-cyber-brief-no-01-2023.pdf | report | TLP:CLEAR | 中 |
| source--charming-kitten--9b4fbd2a0eb8ca99 | GreenCharlie Infrastructure Targeting US Political Entities with Advanced Phishing and Malware |  | 不明 | Charming Kitten/GreenCharlie Infrastructure Targeting US Political Entities with Advanced Phishing and Malware.pdf | report | TLP:CLEAR | 中 |
| source--charming-kitten--723fe9a87e44f1ca | Iranian Dream Job ver1 |  | 不明 | Charming Kitten/Iranian-Dream-Job-ver1.pdf | report | TLP:CLEAR | 中 |
| source--charming-kitten--71dd5e5d5a32e4cf | README |  | 不明 | Charming Kitten/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--charming-kitten--ac6a31187dd4d289 | The Kittens Are Back in Town Charming Kitten 2019 |  | 2019 | Charming Kitten/The-Kittens-Are-Back-in-Town-Charming-Kitten-2019.pdf | report | TLP:CLEAR | 中 |
| source--charming-kitten--84d6787ece8e2894 | The Kittens are Back in Town 3 |  | 不明 | Charming Kitten/The-Kittens-are-Back-in-Town-3.pdf | report | TLP:CLEAR | 中 |
| source--charming-kitten--ad1bc567cd5cb254 | readme |  | 不明 | Charming Kitten/dataleak/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
