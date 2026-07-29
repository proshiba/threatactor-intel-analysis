# menuPass 脅威アクタープロファイル

- プロファイルID: `actor--menupass`
- 状態: draft
- 更新日時: 2026-07-29T15:36:11Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

menuPassの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **menuPass**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| APT10 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| BRONZE RIVERSIDE | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Cicada | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Cloud Hopper | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| CVNX | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| DEV-0401 | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| HOGFISH | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| MenuPass Team | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| POTASSIUM | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Red Apollo | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Stone Panda | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TA429 | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TALONITE | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Red Apollo, CVNX, POTASSIUM, Cloud Hopper, Hogfish, TA429, Cicada, TALONITE, DEV-0401 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 71; mapping requires review. |
| Compromise & Persistence: BUGJUICE, SOGU, SNUGRIDE, Group 27 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 71; mapping requires review. |

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

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Cinnamon Tempest | overlaps-with | 共有alias: DEV-0401 | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |
| MirrorFace | overlaps-with | [MirrorFace](https://attack.mitre.org/groups/G1054) is a People's Republic of China (PRC)-aligned cyberespionage actor believed to be a subgroup under the [menuPass](https://attack.mitre.org/groups/G0045) umbrella based on targeting, tools, and infrastructure overlaps. | 高 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [menuPass](https://attack.mitre.org/groups/G0045) is a threat group that has been active since at least 2006. Individual members of [menuPass](https://attack.mitre.org/groups/G0045) are known to have acted in association with the Chinese Ministry of State Security's (MSS) Tianjin State Security Bureau and worked for the Huaying Haitai Science and Technology Development Company.(Citation: DOJ APT10 Dec 2018)(Citation: District Court of NY APT10 Indictment December 2018)<br><br>[menuPass](https://attack.mitre.org/groups/G0045) has targeted healthcare, defense, aerospace, finance, maritime, biotechnology, energy, and government sectors globally, with an emphasis on Japanese organizations. In 2016 and 2017, the group is known to have targeted managed IT service providers (MSPs), manufacturing and mining companies, and a university.(Citation: Palo Alto menuPass Feb 2017)(Citation: Crowdstrike CrowdCast Oct 2013)(Citation: FireEye Poison Ivy)(Citation: PWC Cloud Hopper April 2017)(Citation: FireEye APT10 April 2017)(Citation: DOJ APT10 Dec 2018)(Citation: District Court of NY APT10 Indictment December 2018) |
| Capability | RedLeaves, Ecipekac, EvilGrab, SNUGRIDE, FYAnti, HUI Loader, PlugX, P8RAT, SodaMaster, Cobalt Strike, PoisonIvy, ChChes, UPPERCUT, IEChecker, Quasar, Trochilus, UPPERCUT (aka ANEL), StoneNetLoader, Net, certutil, PowerSploit, Impacket, pwdump, Mimikatz, Ping, cmd, esentutl, QuasarRAT, AdFind, PsExec |
| Infrastructure |  |
| Victim | Healthcare; Pharma, Defense, Aerospace, Government, MSP, |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Bronze Starlight | single-alias-intersection | 中 | China | https://www.secureworks.com/research/threat-profiles/bronze-starlight<br>https://www.secureworks.com/research/bronze-starlight-ransomware-operations-use-hui-loader<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Bronze+Starlight&n=1 |
| etda-threat-group-cards | Stone Panda, APT 10, menuPass | canonical-name | 高 | China | https://intrusiontruth.wordpress.com/2018/08/15/apt10-was-managed-by-the-tianjin-bureau-of-the-chinese-ministry-of-state-security/<br>https://www.carbonblack.com/2019/02/25/defeating-compiler-level-obfuscations-used-in-apt10-malware/<br>https://adeo.com.tr/wp-content/uploads/2020/02/APT10_v1.2_public.pdf |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Cinnamon Tempest | single-alias-intersection | 中 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| microsoft-threat-actor-mapping | Purple Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | APT10 | multiple-name-intersection | 高 | CN, China | https://unit42.paloaltonetworks.com/unit42-menupass-returns-new-malware-new-attacks-japanese-academics-organizations/<br>https://www.cfr.org/interactive/cyber-operations/apt-10<br>https://www.ncsc.gov.uk/content/files/protected_files/article_files/Joint%20report%20on%20publicly%20available%20hacking%20tools%20%28NCSC%29.pdf |
| misp-threat-actor | BRONZE STARLIGHT | single-alias-intersection | 中 | CN | https://i.blackhat.com/Asia-22/Friday-Materials/AS-22-Li-To-Loot-Or-Not-To-Loot-That-Is-Not-a-Question.pdf<br>https://www.microsoft.com/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself<br>https://www.microsoft.com/security/blog/2021/12/11/guidance-for-preventing-detecting-and-hunting-for-cve-2021-44228-log4j-2-exploitation |
| misp-microsoft-activity-group | Cinnamon Tempest | single-alias-intersection | 中 | CN | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Purple Typhoon | canonical-name | 高 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | menuPass - G0045 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0045<br>http://researchcenter.paloaltonetworks.com/2017/02/unit42-menupass-returns-new-malware-new-attacks-japanese-academics-organizations/<br>https://www.slideshare.net/CrowdStrike/crowd-casts-monthly-you-have-an-adversary-problem |
| misp-mitre-intrusion-set | Cinnamon Tempest - G1021 | single-alias-intersection | 中 |  | https://attack.mitre.org/groups/G1021<br>https://blog.sygnia.co/revealing-emperor-dragonfly-a-chinese-ransomware-group<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide |
| misp-mitre-intrusion-set | menuPass - G0045 | mitre-external-id | 高 |  | http://researchcenter.paloaltonetworks.com/2017/02/unit42-menupass-returns-new-malware-new-attacks-japanese-academics-organizations/<br>http://web.archive.org/web/20220810112638/https:/www.accenture.com/t20180423T055005Z_w_/se-en/_acnmedia/PDF-76/Accenture-Hogfish-Threat-Analysis.pdf<br>https://attack.mitre.org/groups/G0045 |
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
| malware--redleaves | RedLeaves | [RedLeaves](https://attack.mitre.org/software/S0153) is a malware family used by [menuPass](https://attack.mitre.org/groups/G0045). The code overlaps with [PlugX](https://attack.mitre.org/software/S0013) and may be based upon the open source tool Trochilus. (Citation: PWC Cloud Hopper Technical Annex April 2017) (Citation: FireEye APT10 April 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--ecipekac | Ecipekac | [Ecipekac](https://attack.mitre.org/software/S0624) is a multi-layer loader that has been used by [menuPass](https://attack.mitre.org/groups/G0045) since at least 2019 including use as a loader for [P8RAT](https://attack.mitre.org/software/S0626), [SodaMaster](https://attack.mitre.org/software/S0627), and [FYAnti](https://attack.mitre.org/software/S0628).(Citation: Securelist APT10 March 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--evilgrab | EvilGrab | [EvilGrab](https://attack.mitre.org/software/S0152) is a malware family with common reconnaissance capabilities. It has been deployed by [menuPass](https://attack.mitre.org/groups/G0045) via malicious Microsoft Office documents as part of spearphishing campaigns. (Citation: PWC Cloud Hopper Technical Annex April 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--snugride | SNUGRIDE | [SNUGRIDE](https://attack.mitre.org/software/S0159) is a backdoor that has been used by [menuPass](https://attack.mitre.org/groups/G0045) as first stage malware. (Citation: FireEye APT10 April 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--fyanti | FYAnti | [FYAnti](https://attack.mitre.org/software/S0628) is a loader that has been used by [menuPass](https://attack.mitre.org/groups/G0045) since at least 2020, including to deploy [QuasarRAT](https://attack.mitre.org/software/S0262).(Citation: Securelist APT10 March 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--hui-loader | HUI Loader | [HUI Loader](https://attack.mitre.org/software/S1097) is a custom DLL loader that has been used since at least 2015 by China-based threat groups including [Cinnamon Tempest](https://attack.mitre.org/groups/G1021) and [menuPass](https://attack.mitre.org/groups/G0045) to deploy malware on compromised hosts. [HUI Loader](https://attack.mitre.org/software/S1097) has been observed in campaigns loading [SodaMaster](https://attack.mitre.org/software/S0627), [PlugX](https://attack.mitre.org/software/S0013), [Cobalt Strike](https://attack.mitre.org/software/S0154), [Komplex](https://attack.mitre.org/software/S0162), and several strains of ransomware.(Citation: SecureWorks BRONZE STARLIGHT Ransomware Operations June 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--plugx | PlugX | [PlugX](https://attack.mitre.org/software/S0013) is a remote access tool (RAT) with modular plugins that has been used by multiple threat groups.(Citation: Lastline PlugX Analysis)(Citation: FireEye Clandestine Fox Part 2)(Citation: New DragonOK)(Citation: Dell TG-3390) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--p8rat | P8RAT | [P8RAT](https://attack.mitre.org/software/S0626) is a fileless malware used by [menuPass](https://attack.mitre.org/groups/G0045) to download and execute payloads since at least 2020.(Citation: Securelist APT10 March 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--sodamaster | SodaMaster | [SodaMaster](https://attack.mitre.org/software/S0627) is a fileless malware used by [menuPass](https://attack.mitre.org/groups/G0045) to download and execute payloads since at least 2020.(Citation: Securelist APT10 March 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--cobalt-strike | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) is a commercial, full-featured, remote access tool that bills itself as “adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors”. Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.(Citation: cobaltstrike manual)<br><br>In addition to its own capabilities, [Cobalt Strike](https://attack.mitre.org/software/S0154) leverages the capabilities of other well-known tools such as Metasploit and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: cobaltstrike manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--poisonivy | PoisonIvy | [PoisonIvy](https://attack.mitre.org/software/S0012) is a popular remote access tool (RAT) that has been used by many groups.(Citation: FireEye Poison Ivy)(Citation: Symantec Elderwood Sept 2012)(Citation: Symantec Darkmoon Aug 2005) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--chches | ChChes | [ChChes](https://attack.mitre.org/software/S0144) is a Trojan that appears to be used exclusively by [menuPass](https://attack.mitre.org/groups/G0045). It was used to target Japanese organizations in 2016. Its lack of persistence methods suggests it may be intended as a first-stage tool. (Citation: Palo Alto menuPass Feb 2017) (Citation: JPCERT ChChes Feb 2017) (Citation: PWC Cloud Hopper Technical Annex April 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--uppercut | UPPERCUT | [UPPERCUT](https://attack.mitre.org/software/S0275) is a 32-bit HTTP-based backdoor that has been used by [menuPass](https://attack.mitre.org/groups/G0045) since at least 2017.(Citation: FireEye APT10 Sept 2018) Once thought to be exclusive to [menuPass](https://attack.mitre.org/groups/G0045), [UPPERCUT](https://attack.mitre.org/software/S0275) was also observed being used by [menuPass](https://attack.mitre.org/groups/G0045)-associated [MirrorFace](https://attack.mitre.org/groups/G1054) during [Operation AkaiRyū](https://attack.mitre.org/campaigns/C0060).(Citation: Trend Micro Earth Kasha Anel NOV 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--iechecker | IEChecker | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--quasar | Quasar | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--trochilus | Trochilus | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--uppercut-aka-anel | UPPERCUT (aka ANEL) | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--stonenetloader | StoneNetLoader | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--certutil | certutil | [certutil](https://attack.mitre.org/software/S0160) is a command-line utility that can be used to obtain certificate authority information and configure Certificate Services. (Citation: TechNet Certutil) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--powersploit | PowerSploit | [PowerSploit](https://attack.mitre.org/software/S0194) is an open source, offensive security framework comprised of [PowerShell](https://attack.mitre.org/techniques/T1059/001) modules and scripts that perform a wide range of tasks related to penetration testing such as code execution, persistence, bypassing anti-virus, recon, and exfiltration. (Citation: GitHub PowerSploit May 2012) (Citation: PowerShellMagazine PowerSploit July 2014) (Citation: PowerSploit Documentation) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--impacket | Impacket | [Impacket](https://attack.mitre.org/software/S0357) is an open source collection of modules written in Python for programmatically constructing and manipulating network protocols. [Impacket](https://attack.mitre.org/software/S0357) contains several tools for remote service execution, Kerberos manipulation, Windows credential dumping, packet sniffing, and relay attacks.(Citation: Impacket Tools) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--pwdump | pwdump | [pwdump](https://attack.mitre.org/software/S0006) is a credential dumper. (Citation: Wikipedia pwdump) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ping | Ping | [Ping](https://attack.mitre.org/software/S0097) is an operating system utility commonly used to troubleshoot and verify network connections. (Citation: TechNet Ping) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--cmd | cmd | [cmd](https://attack.mitre.org/software/S0106) is the Windows command-line interpreter that can be used to interact with systems and execute other processes and utilities. (Citation: TechNet Cmd)<br><br>Cmd.exe contains native functionality to perform many operations to interact with the system, including listing files in a directory (e.g., <code>dir</code> (Citation: TechNet Dir)), deleting files (e.g., <code>del</code> (Citation: TechNet Del)), and copying files (e.g., <code>copy</code> (Citation: TechNet Copy)). | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--esentutl | esentutl | [esentutl](https://attack.mitre.org/software/S0404) is a command-line tool that provides database utilities for the Windows Extensible Storage Engine.(Citation: Microsoft Esentutl) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--quasarrat | QuasarRAT | [QuasarRAT](https://attack.mitre.org/software/S0262) is an open-source, remote access tool that has been publicly available on GitHub since at least 2014. [QuasarRAT](https://attack.mitre.org/software/S0262) is developed in the C# language.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--adfind | AdFind | [AdFind](https://attack.mitre.org/software/S0552) is a free command-line query tool that can be used for gathering information from Active Directory.(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: FireEye FIN6 Apr 2019)(Citation: FireEye Ryuk and Trickbot January 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
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
| ChessMaster | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Cloud Hopper | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Dust Storm | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

Dust Storm; Cloud Hopper; ChessMaster

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 日本 | [menuPass](https://attack.mitre.org/groups/G0045) has targeted healthcare, defense, aerospace, finance, maritime, biotechnology, energy, and government sectors globally, with an emphasis on Japanese organizations. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 製造・産業 | In 2016 and 2017, the group is known to have targeted managed IT service providers (MSPs), manufacturing and mining companies, and a university.(Citation: Palo Alto menuPass Feb 2017)(Citation: Crowdstrike CrowdCast Oct 2013)(Citation: FireEye Poison Ivy)(Citation: PWC Cloud Hopper April 2017)(Citation: FireEye APT10 April 2017)(Citation: DOJ APT10 Dec 2018)( | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 運輸・航空・海運 | [menuPass](https://attack.mitre.org/groups/G0045) has targeted healthcare, defense, aerospace, finance, maritime, biotechnology, energy, and government sectors globally, with an emphasis on Japanese organizations. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 教育・研究 | In 2016 and 2017, the group is known to have targeted managed IT service providers (MSPs), manufacturing and mining companies, and a university.(Citation: Palo Alto menuPass Feb 2017)(Citation: Crowdstrike CrowdCast Oct 2013)(Citation: FireEye Poison Ivy)(Citation: PWC Cloud Hopper April 2017)(Citation: FireEye APT10 April 2017)(Citation: DOJ APT10 Dec 2018)(Citation: District Court of NY APT10 Indic | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | IT・ソフトウェア | In 2016 and 2017, the group is known to have targeted managed IT service providers (MSPs), manufacturing and mining companies, and a university.(Citation: Palo Alto menuPass Feb 2017)(Citation: Crowdstrike CrowdCast Oct 2013)(Citation: FireEye Poison Ivy)(Citation: PWC Cloud Hopper April 2017)(Citation: FireEye APT10 April 2017)(Citation: DOJ AP | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | エネルギー | [menuPass](https://attack.mitre.org/groups/G0045) has targeted healthcare, defense, aerospace, finance, maritime, biotechnology, energy, and government sectors globally, with an emphasis on Japanese organizations. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | Defense | Targeting text indicates the Defense sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1` |
| sectors | Government | Targeting text indicates the Government sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1` |
| sectors | Healthcare | Targeting text indicates the Healthcare sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1` |

選定ロジック: 未評価

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.002 | Security Account Manager | [menuPass](https://attack.mitre.org/groups/G0045) has used a modified version of pentesting tools wmiexec.vbs and secretsdump.py to dump credentials.(Citation: PWC Cloud Hopper Technical Annex April 2017)(Citation: Github AD-Pentest-Script) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.003 | NTDS | [menuPass](https://attack.mitre.org/groups/G0045) has used Ntdsutil to dump credentials.(Citation: Symantec Cicada November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.004 | LSA Secrets | [menuPass](https://attack.mitre.org/groups/G0045) has used a modified version of pentesting tools wmiexec.vbs and secretsdump.py to dump credentials.(Citation: PWC Cloud Hopper Technical Annex April 2017)(Citation: Github AD-Pentest-Script) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | [menuPass](https://attack.mitre.org/groups/G0045) has collected various files from the compromised computers.(Citation: DOJ APT10 Dec 2018)(Citation: Symantec Cicada November 2020)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | [menuPass](https://attack.mitre.org/groups/G0045) has used several tools to scan for open NetBIOS nameservers and enumerate NetBIOS sessions.(Citation: PWC Cloud Hopper Technical Annex April 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | [menuPass](https://attack.mitre.org/groups/G0045) uses scripts to enumerate IP ranges on the victim network. [menuPass](https://attack.mitre.org/groups/G0045) has also issued the command <code>net view /domain</code> to a [PlugX](https://attack.mitre.org/software/S0013) implant to gather information about remote systems on the network.(Citation: PWC Cloud Hopper Technical Annex April 2017)(Citation: FireEye APT10 April 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | [menuPass](https://attack.mitre.org/groups/G0045) has used RDP connections to move across the victim network.(Citation: PWC Cloud Hopper April 2017)(Citation: District Court of NY APT10 Indictment December 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.004 | SSH | [menuPass](https://attack.mitre.org/groups/G0045) has used Putty Secure Copy Client (PSCP) to transfer data.(Citation: PWC Cloud Hopper April 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | [menuPass](https://attack.mitre.org/groups/G0045) has encoded strings in its malware with base64 as well as with a simple, single-byte XOR obfuscation using key 0x40.(Citation: Accenture Hogfish April 2018)(Citation: FireEye APT10 Sept 2018)(Citation: Symantec Cicada November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036 | Masquerading | [menuPass](https://attack.mitre.org/groups/G0045) has used [esentutl](https://attack.mitre.org/software/S0404) to change file extensions to their true type that were masquerading as .txt files.(Citation: FireEye APT10 Sept 2018)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.003 | Rename Legitimate Utilities | [menuPass](https://attack.mitre.org/groups/G0045) has renamed [certutil](https://attack.mitre.org/software/S0160) and moved it to a different location on the system to avoid detection based on use of the tool.(Citation: FireEye APT10 Sept 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [menuPass](https://attack.mitre.org/groups/G0045) has been seen changing malicious files to appear legitimate.(Citation: District Court of NY APT10 Indictment December 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1039 | Data from Network Shared Drive | [menuPass](https://attack.mitre.org/groups/G0045) has collected data from remote systems by mounting network shares with <code>net use</code> and using Robocopy to transfer data.(Citation: PWC Cloud Hopper April 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1046 | Network Service Discovery | [menuPass](https://attack.mitre.org/groups/G0045) has used tcping.exe, similar to [Ping](https://attack.mitre.org/software/S0097), to probe port status on systems of interest.(Citation: PWC Cloud Hopper Technical Annex April 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | [menuPass](https://attack.mitre.org/groups/G0045) has used a modified version of pentesting script wmiexec.vbs, which logs into a remote machine using WMI.(Citation: PWC Cloud Hopper Technical Annex April 2017)(Citation: Github AD-Pentest-Script)(Citation: Symantec Cicada November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | [menuPass](https://attack.mitre.org/groups/G0045) has used <code>net use</code> to conduct connectivity checks to machines.(Citation: PWC Cloud Hopper April 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [menuPass](https://attack.mitre.org/groups/G0045) has used a script (atexec.py) to execute a command on a target machine via Task Scheduler.(Citation: PWC Cloud Hopper Technical Annex April 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055.012 | Process Hollowing | [menuPass](https://attack.mitre.org/groups/G0045) has used process hollowing in iexplore.exe to load the [RedLeaves](https://attack.mitre.org/software/S0153) implant.(Citation: Accenture Hogfish April 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056.001 | Keylogging | [menuPass](https://attack.mitre.org/groups/G0045) has used key loggers to steal usernames and passwords.(Citation: District Court of NY APT10 Indictment December 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [menuPass](https://attack.mitre.org/groups/G0045) uses [PowerSploit](https://attack.mitre.org/software/S0194) to inject shellcode into PowerShell.(Citation: PWC Cloud Hopper Technical Annex April 2017)(Citation: Symantec Cicada November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [menuPass](https://attack.mitre.org/groups/G0045) executes commands using a command-line interface and reverse shell. The group has used a modified version of pentesting script wmiexec.vbs to execute commands.(Citation: PWC Cloud Hopper April 2017)(Citation: PWC Cloud Hopper Technical Annex April 2017)(Citation: Github AD-Pentest-Script)(Citation: FireEye APT10 Sept 2018) [menuPass](https://attack.mitre.org/groups/G0045) has used malicious macros embedded inside Office documents to execute files.(Citation: Accenture Hogfish April 2018)(Citation: FireEye APT10 Sept 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.003 | Clear Command History | [menuPass](https://attack.mitre.org/groups/G0045) has used [Wevtutil](https://attack.mitre.org/software/S0645) to remove PowerShell execution logs.(Citation: Securelist APT10 March 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | A [menuPass](https://attack.mitre.org/groups/G0045) macro deletes files after it has decoded and decompressed them.(Citation: Accenture Hogfish April 2018)(Citation: District Court of NY APT10 Indictment December 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | [menuPass](https://attack.mitre.org/groups/G0045) stages data prior to exfiltration in multi-part archives, often saved in the Recycle Bin.(Citation: PWC Cloud Hopper April 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.002 | Remote Data Staging | [menuPass](https://attack.mitre.org/groups/G0045) has staged data on remote MSP systems or other victim networks prior to exfiltration.(Citation: PWC Cloud Hopper April 2017)(Citation: Symantec Cicada November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [menuPass](https://attack.mitre.org/groups/G0045) has used valid accounts including shared between Managed Service Providers and clients to move between the two environments.(Citation: PWC Cloud Hopper April 2017)(Citation: Symantec Cicada November 2020)(Citation: District Court of NY APT10 Indictment December 2018)(Citation: Securelist APT10 March 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | [menuPass](https://attack.mitre.org/groups/G0045) has searched compromised systems for folders of interest including those related to HR, audit and expense, and meeting memos.(Citation: Symantec Cicada November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | [menuPass](https://attack.mitre.org/groups/G0045) has used the Microsoft administration tool csvde.exe to export Active Directory data.(Citation: PWC Cloud Hopper Technical Annex April 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090.002 | External Proxy | [menuPass](https://attack.mitre.org/groups/G0045) has used a global service provider's IP as a proxy for C2 traffic from a victim.(Citation: FireEye APT10 April 2017)(Citation: FireEye APT10 Sept 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [menuPass](https://attack.mitre.org/groups/G0045) has installed updates and new malware on victims.(Citation: PWC Cloud Hopper April 2017)(Citation: District Court of NY APT10 Indictment December 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1106 | Native API | [menuPass](https://attack.mitre.org/groups/G0045) has used native APIs including <code>GetModuleFileName</code>, <code>lstrcat</code>, <code>CreateFile</code>, and <code>ReadFile</code>.(Citation: Symantec Cicada November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1119 | Automated Collection | [menuPass](https://attack.mitre.org/groups/G0045) has used the Csvde tool to collect Active Directory files and data.(Citation: Symantec Cicada November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | [menuPass](https://attack.mitre.org/groups/G0045) has used [certutil](https://attack.mitre.org/software/S0160) in a macro to decode base64-encoded content contained in a dropper document attached to an email. The group has also used <code>certutil -decode</code> to decode files on the victim’s machine when dropping [UPPERCUT](https://attack.mitre.org/software/S0275).(Citation: Accenture Hogfish April 2018)(Citation: FireEye APT10 Sept 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [menuPass](https://attack.mitre.org/groups/G0045) has leveraged vulnerabilities in Pulse Secure VPNs to hijack sessions.(Citation: Securelist APT10 March 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1199 | Trusted Relationship | [menuPass](https://attack.mitre.org/groups/G0045) has used legitimate access granted to Managed Service Providers in order to access victims of interest.(Citation: PWC Cloud Hopper Technical Annex April 2017)(Citation: FireEye APT10 April 2017)(Citation: Symantec Cicada November 2020)(Citation: DOJ APT10 Dec 2018)(Citation: District Court of NY APT10 Indictment December 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [menuPass](https://attack.mitre.org/groups/G0045) has attempted to get victims to open malicious files such as Windows Shortcuts (.lnk) and/or Microsoft Office documents, sent via email as part of spearphishing campaigns.(Citation: PWC Cloud Hopper Technical Annex April 2017)(Citation: FireEye APT10 April 2017)(Citation: Accenture Hogfish April 2018)(Citation: FireEye APT10 Sept 2018)(Citation: District Court of NY APT10 Indictment December 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1210 | Exploitation of Remote Services | [menuPass](https://attack.mitre.org/groups/G0045) has used tools to exploit the ZeroLogon vulnerability (CVE-2020-1472).(Citation: Symantec Cicada November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.004 | InstallUtil | [menuPass](https://attack.mitre.org/groups/G0045) has used <code>InstallUtil.exe</code> to execute malicious software.(Citation: PWC Cloud Hopper Technical Annex April 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1553.002 | Code Signing | [menuPass](https://attack.mitre.org/groups/G0045) has resized and added data to the certificate table to enable the signing of modified files with legitimate signatures.(Citation: Securelist APT10 March 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560 | Archive Collected Data | [menuPass](https://attack.mitre.org/groups/G0045) has encrypted files and information before exfiltration.(Citation: DOJ APT10 Dec 2018)(Citation: District Court of NY APT10 Indictment December 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | [menuPass](https://attack.mitre.org/groups/G0045) has compressed files before exfiltration using TAR and RAR.(Citation: PWC Cloud Hopper April 2017)(Citation: PWC Cloud Hopper Technical Annex April 2017)(Citation: Symantec Cicada November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [menuPass](https://attack.mitre.org/groups/G0045) has sent malicious Office documents via email as part of spearphishing campaigns as well as executables disguised as documents.(Citation: PWC Cloud Hopper Technical Annex April 2017)(Citation: FireEye APT10 April 2017)(Citation: FireEye APT10 Sept 2018)(Citation: District Court of NY APT10 Indictment December 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1568.001 | Fast Flux DNS | [menuPass](https://attack.mitre.org/groups/G0045) has used dynamic DNS service providers to host malicious domains.(Citation: District Court of NY APT10 Indictment December 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | [menuPass](https://attack.mitre.org/groups/G0045) has used DLL side-loading to launch versions of Mimikatz and PwDump6 as well as [UPPERCUT](https://attack.mitre.org/software/S0275).(Citation: PWC Cloud Hopper Technical Annex April 2017)(Citation: FireEye APT10 Sept 2018)(Citation: Symantec Cicada November 2020) [menuPass](https://attack.mitre.org/groups/G0045) has also used DLL search order hijacking.(Citation: PWC Cloud Hopper April 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [menuPass](https://attack.mitre.org/groups/G0045) has registered malicious domains for use in intrusion campaigns.(Citation: DOJ APT10 Dec 2018)(Citation: District Court of NY APT10 Indictment December 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [menuPass](https://attack.mitre.org/groups/G0045) has used and modified open-source tools like [Impacket](https://attack.mitre.org/software/S0357), [Mimikatz](https://attack.mitre.org/software/S0002), and [pwdump](https://attack.mitre.org/software/S0006).(Citation: PWC Cloud Hopper Technical Annex April 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 4件
- IOC観測: 4件
- 複数攻撃で観測: 0件
- 要レビュー候補: 4件
- 非IOC artifact観測: 74件（`artifacts.csv`）

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
| source--menupass--89446d94151016f6 | menupass |  | 不明 | actor_profile/evidence/menupass.csv | structured-data | TLP:CLEAR | 中 |
| source--menupass--29904f2fa8aac938 | Automating APT Campaign and Group Attribution |  | 不明 | APT-hunting/Automating APT Campaign and Group Attribution.pdf | report | TLP:CLEAR | 中 |
| source--menupass--525d7a3d1c976f4a | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--menupass--7bd73a7a0ba3bb84 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--menupass--029daaf640b77a1f | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--menupass--57d3cd36cb8df14f | Virtual Routes Pharos Report Series No. 3 |  | 不明 | cybercrime/2025/Virtual-Routes-Pharos-Report-Series-No.-3.pdf | report | TLP:CLEAR | 中 |
| source--menupass--77c6af9c47718ae5 | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--menupass--44d015486a554720 | mpressioncss ta report 2020 5 en |  | 2020 | summary/2021/mpressioncss_ta_report_2020_5_en.pdf | report | TLP:CLEAR | 中 |
| source--menupass--f4ef163a51cff5c9 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--menupass--8d360602c02767f5 | Google Cybersecurity Action Team Threat Horizons Report#5 |  | 不明 | summary/2023/Google_Cybersecurity_Action_Team_Threat_Horizons_Report#5.pdf | report | TLP:CLEAR | 中 |
| source--menupass--6cae8e141659b1b6 | Modern Asian APT groups TTPs report eng |  | 不明 | summary/2023/Modern-Asian-APT-groups-TTPs_report_eng.pdf | report | TLP:CLEAR | 中 |
| source--menupass--0ce74bfa3d0374b6 | Secureworks NC3 2022StateoftheThreat |  | 2022 | summary/2023/Secureworks_NC3_2022StateoftheThreat.pdf | report | TLP:CLEAR | 中 |
| source--menupass--aed928436f41e274 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--menupass--a27b14ea99bd2e21 | CTA 2024 Olympics Threat Assessment Supplemental Report Combined rev |  | 2024 | summary/2024/CTA-2024-Olympics-Threat-Assessment-Supplemental-Report_Combined_rev.pdf | report | TLP:CLEAR | 中 |
| source--menupass--7db0f8e1a0ce51c9 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--menupass--2a3ba371160d125b | 2024 IC3Report |  | 2024 | summary/2025/2024_IC3Report.pdf | report | TLP:CLEAR | 中 |
| source--menupass--e00e00f4fe294ab6 | CrowdStrikeGlobalThreatReport2025 |  | 2025 | summary/2025/CrowdStrikeGlobalThreatReport2025.pdf | report | TLP:CLEAR | 中 |
| source--menupass--6c8babe9ccde2d5f | Cybersecurity Threats 2024 Annual Report QAX |  | 2024 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | report | TLP:CLEAR | 中 |
| source--menupass--f8d6de621a1ea84e | Dragos 2025 OT Cybersecurity Report A Year in Review |  | 2025 | summary/2025/Dragos-2025-OT-Cybersecurity-Report-A-Year-in-Review.pdf | report | TLP:CLEAR | 中 |
| source--menupass--ab68d9d445872cc3 | threat landscape report 2025 |  | 2025 | summary/2025/threat-landscape-report-2025.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
