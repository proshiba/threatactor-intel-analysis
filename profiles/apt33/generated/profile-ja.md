# APT33 脅威アクタープロファイル

- プロファイルID: `actor--apt33`
- 状態: draft
- 更新日時: 2026-07-29T23:13:53Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

APT33の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **APT33**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Elfin | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| HOLMIUM | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Peach Sandstorm | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Magic Hound | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Iran row 15; mapping requires review. |
| Timberworm | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Iran row 15; mapping requires review. |
| MAGNALLIUM | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Iran row 15; mapping requires review. |
| Refined Kitten | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Iran row 15; mapping requires review. |

## 帰属

The repository mapping workbook places this actor in the Iran worksheet.

- 国: Iran
- スポンサー種別: state
- 確度: 中
- 証拠: `source--actor-mapping-workbook`

## モチベーション

未評価

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Peach Sandstorm | overlaps-with | 共有alias: APT33, HOLMIUM, Peach Sandstorm | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |
| HEXANE | related-to | [HEXANE](https://attack.mitre.org/groups/G1001)'s TTPs appear similar to [APT33](https://attack.mitre.org/groups/G0064) and [OilRig](https://attack.mitre.org/groups/G0049) but due to differences in victims and tools it is tracked as a separate entity.(Citation: Dragos Hexane)(Citation: Kaspersky Lyceum October 2021)(Citation: ClearSky Siamesekitten August 2021)(Citation: Accenture Lyceum Targets November 2021) | 中 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [APT33](https://attack.mitre.org/groups/G0064) is a suspected Iranian threat group that has carried out operations since at least 2013. The group has targeted organizations across multiple industries in the United States, Saudi Arabia, and South Korea, with a particular interest in the aviation and energy sectors.(Citation: FireEye APT33 Sept 2017)(Citation: FireEye APT33 Webinar Sept 2017) |
| Capability | NETWIRE, StoneDrill, NanoCore, TURNEDUP, POWERTON, DEADWOOD, AutoIt backdoor, Shamoon, PUPYRAT, POSHC2 (.NET backdoor), Gpppassword, Quasar RAT, Remcos, SniffPass, DarkComet, AutoIt FTP tool, .NET FTP tool, PowerShell downloader (registry.ps1), POSHC2 backdoor, different keyloggers, Net, PowerSploit, Empire, PoshC2, Ruler, Mimikatz, LaZagne, Pupy, ftp |
| Infrastructure |  |
| Victim | A threat actor used malware known as Shamoon 2.0 to exfiltrate and delete data from computers in the Saudi transportation sector. Commercial entities, Middle East, US, South Korea, DND focussed entities, Airlines, Airline suppliers. |
| Socio-political | Iran |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | APT 33, Elfin, Magnallium | canonical-name | 高 | Iran | https://www.fireeye.com/blog/threat-research/2017/09/apt33-insights-into-iranian-cyber-espionage.html<br>https://en.wikipedia.org/wiki/Elfin_Team<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=APT+33%2C+Elfin%2C+Magnallium&n=1 |
| etda-threat-group-cards | Magic Hound, APT 35, Cobalt Illusion, Charming Kitten | multiple-name-intersection | 高 | Iran | https://www.clearskysec.com/wp-content/uploads/2017/12/Charming_Kitten_2017.pdf<br>https://en.wikipedia.org/wiki/Charming_Kitten<br>https://vblocalhost.com/uploads/VB2021-Haeghebaert.pdf |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Peach Sandstorm | canonical-name | 高 | Iran | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | APT33 | canonical-name | 高 | IR, Iran (Islamic Republic of) | https://www.fireeye.com/blog/threat-research/2017/09/apt33-insights-into-iranian-cyber-espionage.html<br>https://blog.trendmicro.com/trendlabs-security-intelligence/more-than-a-dozen-obfuscated-apt33-botnets-used-for-extreme-narrow-targeting/<br>https://www.brighttalk.com/webcast/10703/275683 |
| misp-threat-actor | Rocket Kitten | single-alias-intersection | 中 | IR, Iran (Islamic Republic of) | https://www.trendmicro.com/vinfo/us/security/news/cyber-attacks/operation-woolen-goldfish-when-kittens-go-phishing<br>https://www.trendmicro.com/cloud-content/us/pdfs/security-intelligence/white-papers/wp-the-spy-kittens-are-back.pdf<br>http://www.clearskysec.com/thamar-reservoir/ |
| misp-threat-actor | APT35 | single-alias-intersection | 中 | IR | https://www.fireeye.com/content/dam/collateral/en/mtrends-2018.pdf<br>https://attack.mitre.org/groups/G0059/<br>https://www.cfr.org/interactive/cyber-operations/magic-hound |
| misp-microsoft-activity-group | Peach Sandstorm | canonical-name | 高 | IR, Iran | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | Magic Hound - G0059 | single-alias-intersection | 中 |  | https://attack.mitre.org/wiki/Group/G0059<br>https://researchcenter.paloaltonetworks.com/2017/02/unit42-magic-hound-campaign-attacks-saudi-targets/ |
| misp-mitre-enterprise-intrusion-set | APT33 - G0064 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0064<br>https://www.fireeye.com/blog/threat-research/2017/09/apt33-insights-into-iranian-cyber-espionage.html<br>https://www.brighttalk.com/webcast/10703/275683 |
| misp-mitre-intrusion-set | Magic Hound - G0059 | single-alias-intersection | 中 |  | http://www.clearskysec.com/wp-content/uploads/2017/12/Charming_Kitten_2017.pdf<br>https://attack.mitre.org/groups/G0059<br>https://blog.certfa.com/posts/charming-kitten-christmas-gift/ |
| misp-mitre-intrusion-set | APT33 - G0064 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0064<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://www.brighttalk.com/webcast/10703/275683 |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Cleaver | similar | misp-mitre-enterprise-intrusion-set | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| CHRYSENE | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Charming Kitten | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Cleaver | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Clever Kitten | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Flying Kitten | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| OilRig | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--autoit-backdoor | AutoIt backdoor | [AutoIt backdoor](https://attack.mitre.org/software/S0129) is malware that has been used by the actors responsible for the MONSOON campaign. The actors frequently used it in weaponized .pps files exploiting CVE-2014-6352. (Citation: Forcepoint Monsoon) This malware makes use of the legitimate scripting language for Windows GUI automation with the same name. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--autoit-ftp-tool | AutoIt FTP tool | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--darkcomet | DarkComet | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--deadwood | DEADWOOD | [DEADWOOD](https://attack.mitre.org/software/S1134) is wiper malware written in C++ using Boost libraries. [DEADWOOD](https://attack.mitre.org/software/S1134) was first observed in an unattributed wiping event in Saudi Arabia in 2019, and has since been incorporated into [Agrius](https://attack.mitre.org/groups/G1030) operations.(Citation: SentinelOne Agrius 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--different-keyloggers | different keyloggers | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--gpppassword | Gpppassword | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--nanocore | NanoCore | [NanoCore](https://attack.mitre.org/software/S0336) is a modular remote access tool developed in .NET that can be used to spy on victims and steal information. It has been used by threat actors since 2013.(Citation: DigiTrust NanoCore Jan 2017)(Citation: Cofense NanoCore Mar 2018)(Citation: PaloAlto NanoCore Feb 2016)(Citation: Unit 42 Gorgon Group Aug 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--net-ftp-tool | .NET FTP tool | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--netwire | NETWIRE | [NETWIRE](https://attack.mitre.org/software/S0198) is a publicly available, multiplatform remote administration tool (RAT) that has been used by criminal and APT groups since at least 2012.(Citation: FireEye APT33 Sept 2017)(Citation: McAfee Netwire Mar 2015)(Citation: FireEye APT33 Webinar Sept 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--poshc2-backdoor | POSHC2 backdoor | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--poshc2-net-backdoor | POSHC2 (.NET backdoor) | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--powershell-downloader-registry-ps1 | PowerShell downloader (registry.ps1) | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--powerton | POWERTON | [POWERTON](https://attack.mitre.org/software/S0371) is a custom PowerShell backdoor first observed in 2018. It has typically been deployed as a late-stage backdoor by [APT33](https://attack.mitre.org/groups/G0064). At least two variants of the backdoor have been identified, with the later version containing improved functionality.(Citation: FireEye APT33 Guardrail) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--pupyrat | PUPYRAT | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--quasar-rat | Quasar RAT | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--remcos | Remcos | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--shamoon | Shamoon | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--sniffpass | SniffPass | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--stonedrill | StoneDrill | [StoneDrill](https://attack.mitre.org/software/S0380) is wiper malware discovered in destructive campaigns against both Middle Eastern and European targets in association with [APT33](https://attack.mitre.org/groups/G0064).(Citation: FireEye APT33 Sept 2017)(Citation: Kaspersky StoneDrill 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--turnedup | TURNEDUP | [TURNEDUP](https://attack.mitre.org/software/S0199) is a non-public backdoor. It has been dropped by [APT33](https://attack.mitre.org/groups/G0064)'s [StoneDrill](https://attack.mitre.org/software/S0380) malware. (Citation: FireEye APT33 Sept 2017) (Citation: FireEye APT33 Webinar Sept 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--powersploit | PowerSploit | [PowerSploit](https://attack.mitre.org/software/S0194) is an open source, offensive security framework comprised of [PowerShell](https://attack.mitre.org/techniques/T1059/001) modules and scripts that perform a wide range of tasks related to penetration testing such as code execution, persistence, bypassing anti-virus, recon, and exfiltration. (Citation: GitHub PowerSploit May 2012) (Citation: PowerShellMagazine PowerSploit July 2014) (Citation: PowerSploit Documentation) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--empire | Empire | [Empire](https://attack.mitre.org/software/S0363) is an open-source, cross-platform remote administration and post-exploitation framework that is publicly available on GitHub. While the tool itself is primarily written in Python, the post-exploitation agents are written in pure [PowerShell](https://attack.mitre.org/techniques/T1059/001) for Windows and Python for Linux/macOS. [Empire](https://attack.mitre.org/software/S0363) was one of five tools singled out by a joint report on public hacking tools being widely used by adversaries.(Citation: NCSC Joint Report Public Tools)(Citation: Github PowerShell Empire)(Citation: GitHub ATTACK Empire) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--poshc2 | PoshC2 | [PoshC2](https://attack.mitre.org/software/S0378) is an open source remote administration and post-exploitation framework that is publicly available on GitHub. The server-side components of the tool are primarily written in Python, while the implants are written in [PowerShell](https://attack.mitre.org/techniques/T1059/001). Although [PoshC2](https://attack.mitre.org/software/S0378) is primarily focused on Windows implantation, it does contain a basic Python dropper for Linux/macOS.(Citation: GitHub PoshC2) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ruler | Ruler | [Ruler](https://attack.mitre.org/software/S0358) is a tool to abuse Microsoft Exchange services. It is publicly available on GitHub and the tool is executed via the command line. The creators of [Ruler](https://attack.mitre.org/software/S0358) have also released a defensive tool, NotRuler, to detect its usage.(Citation: SensePost Ruler GitHub)(Citation: SensePost NotRuler) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--lazagne | LaZagne | [LaZagne](https://attack.mitre.org/software/S0349) is a post-exploitation, open-source tool used to recover stored passwords on a system. It has modules for Windows, Linux, and OSX, but is mainly focused on Windows systems. [LaZagne](https://attack.mitre.org/software/S0349) is publicly available on GitHub.(Citation: GitHub LaZagne Dec 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--pupy | Pupy | [Pupy](https://attack.mitre.org/software/S0192) is an open source, cross-platform (Windows, Linux, OSX, Android) remote administration and post-exploitation tool. (Citation: GitHub Pupy) It is written in Python and can be generated as a payload in several different ways (Windows exe, Python file, PowerShell oneliner/file, Linux elf, APK, Rubber Ducky, etc.). (Citation: GitHub Pupy) [Pupy](https://attack.mitre.org/software/S0192) is publicly available on GitHub. (Citation: GitHub Pupy) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ftp | ftp | [ftp](https://attack.mitre.org/software/S0095) is a utility commonly available with operating systems to transfer information over the File Transfer Protocol (FTP). Adversaries can use it to transfer other tools onto a system or to exfiltrate data.(Citation: Microsoft FTP)(Citation: Linux FTP) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| APT33(イランのハッキンググループ)、新しいTicklerマルウェアを使用して米国政府・防衛機関にバックドアを設置 | infrastructure-operation | 2024-04 | 2024-07 | 2024-08-29 |  |  | ttp--activity-rule--6150c1b75682e486b452 |  | APT33が新しいTicklerマルウェアを使用し、米国やUAEの政府・防衛機関のネットワークにバックドアを設置。 2024年4月から7月にかけて、情報収集活動の一環としてこの新しいマルウェアを使用。 2024年4月から5月にかけてパスワードスプレー攻撃を通じて侵入。 Microsoftの調査により、Azureインフラを利用した攻撃が明らかに。 APT33はIRGC（イラン革命防衛隊）に関連しているとされる。 | 高 | `source--daily-f8c5f7e3f2497c4aec2e` |
| Stonedrill/ Shamoon2.0 | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| APT33(イランのハッキンググループ)、新しいTicklerマルウェアを使用して米国政府・防衛機関にバックドアを設置 | APT33 | 情報なし | T1110.003 Password Spraying | 情報なし | 情報なし | 情報なし | 高 |
| Stonedrill/ Shamoon2.0 | APT33 | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |

Stonedrill/ Shamoon2.0

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アフガニスタン | 構造化OSINTの被害国フィールドでAPT33の標的・被害国としてアフガニスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | アラブ首長国連邦 | 構造化OSINTの被害国フィールドでAPT33の標的・被害国としてアラブ首長国連邦が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イエメン | 構造化OSINTの被害国フィールドでAPT33の標的・被害国としてイエメンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イスラエル | 構造化OSINTの被害国フィールドでAPT33の標的・被害国としてイスラエルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イラク | 構造化OSINTの被害国フィールドでAPT33の標的・被害国としてイラクが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イラン | 構造化OSINTの被害国フィールドでAPT33の標的・被害国としてイランが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | エジプト | 構造化OSINTの被害国フィールドでAPT33の標的・被害国としてエジプトが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | カナダ | 構造化OSINTの被害国フィールドでAPT33の標的・被害国としてカナダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | クウェート | 構造化OSINTの被害国フィールドでAPT33の標的・被害国としてクウェートが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | サウジアラビア | MITRE ATT&CKのGroup概要でAPT33の標的国として明示されている。 | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | シリア | 構造化OSINTの被害国フィールドでAPT33の標的・被害国としてシリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | スペイン | 構造化OSINTの被害国フィールドでAPT33の標的・被害国としてスペインが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | トルコ | 構造化OSINTの被害国フィールドでAPT33の標的・被害国としてトルコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | パキスタン | 構造化OSINTの被害国フィールドでAPT33の標的・被害国としてパキスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | パレスチナ | 構造化OSINTの被害国フィールドでAPT33の標的・被害国としてパレスチナが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フランス | 構造化OSINTの被害国フィールドでAPT33の標的・被害国としてフランスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ブラジル | 構造化OSINTの被害国フィールドでAPT33の標的・被害国としてブラジルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベネズエラ | 構造化OSINTの被害国フィールドでAPT33の標的・被害国としてベネズエラが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベルギー | 構造化OSINTの被害国フィールドでAPT33の標的・被害国としてベルギーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | モロッコ | 構造化OSINTの被害国フィールドでAPT33の標的・被害国としてモロッコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ヨルダン | 構造化OSINTの被害国フィールドでAPT33の標的・被害国としてヨルダンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | The group has targeted organizations across multiple industries in the United States, Saudi Arabia, and South Korea, with a particular interest in the aviation and energy sectors.(Citation: FireEye APT33 Sept 2017)(Citation: FireEye APT33 Webinar Sept 2017) | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 英国 | 構造化OSINTの被害国フィールドでAPT33の標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 韓国 | Targeting text mentions south korea. | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | アフリカ | エジプト、モロッコで確認された標的・被害事例をアフリカとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 中南米 | ブラジル、ベネズエラで確認された標的・被害事例を中南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 中東 | レビュー済みアクターマッピングの標的欄に記録された中東を構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 北アフリカ | エジプト、モロッコで確認された標的・被害事例を北アフリカとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 北米 | カナダ、米国で確認された標的・被害事例を北米として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 南アジア | アフガニスタン、パキスタンで確認された標的・被害事例を南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 南米 | ブラジル、ベネズエラで確認された標的・被害事例を南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | スペイン、トルコ、フランス、ベルギー、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| sectors | 運輸・航空・海運 | The group has targeted organizations across multiple industries in the United States, Saudi Arabia, and South Korea, with a particular interest in the aviation and energy sectors.(Citation: FireEye APT33 Sept 2017)(Citation: FireEye APT33 Webinar Sept 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | エネルギー | The group has targeted organizations across multiple industries in the United States, Saudi Arabia, and South Korea, with a particular interest in the aviation and energy sectors.(Citation: FireEye APT33 Sept 2017)(Citation: FireEye APT33 Webinar Sept 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | Transportation | Targeting text indicates the Transportation sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1110.003 | Password Spraying | 2024年4月から5月にかけてパスワードスプレー攻撃を通じて侵入。 |  | activity--daily-0e31a7a9dbd25f8d63f4 | 2024-04 | 2024-07 | 中 | `source--daily-f8c5f7e3f2497c4aec2e` |
| Credential Access | T1003.001 | LSASS Memory | [APT33](https://attack.mitre.org/groups/G0064) has used a variety of publicly available tools like [LaZagne](https://attack.mitre.org/software/S0349), [Mimikatz](https://attack.mitre.org/software/S0002), and ProcDump to dump credentials.(Citation: Symantec Elfin Mar 2019)(Citation: FireEye APT33 Guardrail) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.004 | LSA Secrets | [APT33](https://attack.mitre.org/groups/G0064) has used a variety of publicly available tools like [LaZagne](https://attack.mitre.org/software/S0349) to gather credentials.(Citation: Symantec Elfin Mar 2019)(Citation: FireEye APT33 Guardrail) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.005 | Cached Domain Credentials | [APT33](https://attack.mitre.org/groups/G0064) has used a variety of publicly available tools like [LaZagne](https://attack.mitre.org/software/S0349) to gather credentials.(Citation: Symantec Elfin Mar 2019)(Citation: FireEye APT33 Guardrail) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | [APT33](https://attack.mitre.org/groups/G0064) has used base64 to encode payloads.(Citation: FireEye APT33 Guardrail) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access, Discovery | T1040 | Network Sniffing | [APT33](https://attack.mitre.org/groups/G0064) has used SniffPass to collect credentials by sniffing network traffic.(Citation: Symantec Elfin Mar 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1048.003 | Exfiltration Over Unencrypted Non-C2 Protocol | [APT33](https://attack.mitre.org/groups/G0064) has used FTP to exfiltrate files (separately from the C2 channel).(Citation: Symantec Elfin Mar 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [APT33](https://attack.mitre.org/groups/G0064) has created a scheduled task to execute a .vbe file multiple times a day.(Citation: Symantec Elfin Mar 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [APT33](https://attack.mitre.org/groups/G0064) has utilized PowerShell to download files from the C2 server and run various scripts. (Citation: Symantec Elfin Mar 2019)(Citation: Microsoft Holmium June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | [APT33](https://attack.mitre.org/groups/G0064) has used VBScript to initiate the delivery of payloads.(Citation: Microsoft Holmium June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1068 | Exploitation for Privilege Escalation | [APT33](https://attack.mitre.org/groups/G0064) has used a publicly available exploit for CVE-2017-0213 to escalate privileges on a local system.(Citation: FireEye APT33 Guardrail) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [APT33](https://attack.mitre.org/groups/G0064) has used HTTP for command and control.(Citation: Symantec Elfin Mar 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [APT33](https://attack.mitre.org/groups/G0064) has used valid accounts for initial access and privilege escalation.(Citation: FireEye APT33 Webinar Sept 2017)(Citation: FireEye APT33 Guardrail) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.004 | Cloud Accounts | [APT33](https://attack.mitre.org/groups/G0064) has used compromised Office 365 accounts in tandem with [Ruler](https://attack.mitre.org/software/S0358) in an attempt to gain control of endpoints.(Citation: Microsoft Holmium June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [APT33](https://attack.mitre.org/groups/G0064) has downloaded additional files and programs from its C2 server.(Citation: Symantec Elfin Mar 2019)(Citation: Microsoft Holmium June 2020)	<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110.003 | Password Spraying | [APT33](https://attack.mitre.org/groups/G0064) has used password spraying to gain access to target systems.(Citation: FireEye APT33 Guardrail)(Citation: Microsoft Holmium June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1132.001 | Standard Encoding | [APT33](https://attack.mitre.org/groups/G0064) has used base64 to encode command and control traffic.(Citation: FireEye APT33 Guardrail) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | [APT33](https://attack.mitre.org/groups/G0064) has attempted to exploit a known vulnerability in WinRAR (CVE-2018-20250), and attempted to gain remote code execution via a security bypass vulnerability (CVE-2017-11774).(Citation: Symantec Elfin Mar 2019)(Citation: Microsoft Holmium June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | [APT33](https://attack.mitre.org/groups/G0064) has lured users to click links to malicious HTML applications delivered via spearphishing emails.(Citation: FireEye APT33 Sept 2017)(Citation: Symantec Elfin Mar 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [APT33](https://attack.mitre.org/groups/G0064) has used malicious e-mail attachments to lure victims into executing malware.(Citation: Microsoft Holmium June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1546.003 | Windows Management Instrumentation Event Subscription | [APT33](https://attack.mitre.org/groups/G0064) has attempted to use WMI event subscriptions to establish persistence on compromised hosts.(Citation: Microsoft Holmium June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [APT33](https://attack.mitre.org/groups/G0064) has deployed a tool known as [DarkComet](https://attack.mitre.org/software/S0334) to the Startup folder of a victim, and used Registry run keys to gain persistence.(Citation: Symantec Elfin Mar 2019)(Citation: Microsoft Holmium June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.001 | Credentials In Files | [APT33](https://attack.mitre.org/groups/G0064) has used a variety of publicly available tools like [LaZagne](https://attack.mitre.org/software/S0349) to gather credentials.(Citation: Symantec Elfin Mar 2019)(Citation: FireEye APT33 Guardrail) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.006 | Group Policy Preferences | [APT33](https://attack.mitre.org/groups/G0064) has used a variety of publicly available tools like Gpppassword to gather credentials.(Citation: Symantec Elfin Mar 2019)(Citation: FireEye APT33 Guardrail) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555 | Credentials from Password Stores | [APT33](https://attack.mitre.org/groups/G0064) has used a variety of publicly available tools like [LaZagne](https://attack.mitre.org/software/S0349) to gather credentials.(Citation: Symantec Elfin Mar 2019)(Citation: FireEye APT33 Guardrail) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.003 | Credentials from Web Browsers | [APT33](https://attack.mitre.org/groups/G0064) has used a variety of publicly available tools like [LaZagne](https://attack.mitre.org/software/S0349) to gather credentials.(Citation: Symantec Elfin Mar 2019)(Citation: FireEye APT33 Guardrail) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | [APT33](https://attack.mitre.org/groups/G0064) has used WinRAR to compress data prior to exfil.(Citation: Symantec Elfin Mar 2019)	<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [APT33](https://attack.mitre.org/groups/G0064) has sent spearphishing e-mails with archive attachments.(Citation: Microsoft Holmium June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | [APT33](https://attack.mitre.org/groups/G0064) has sent spearphishing emails containing links to .hta files.(Citation: FireEye APT33 Sept 2017)(Citation: Symantec Elfin Mar 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1571 | Non-Standard Port | [APT33](https://attack.mitre.org/groups/G0064) has used HTTP over TCP ports 808 and 880 for command and control.(Citation: Symantec Elfin Mar 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573.001 | Symmetric Cryptography | [APT33](https://attack.mitre.org/groups/G0064) has used AES for encryption of command and control traffic.(Citation: FireEye APT33 Guardrail) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [APT33](https://attack.mitre.org/groups/G0064) has obtained and leveraged publicly-available tools for early intrusion activities.(Citation: FireEye APT33 Guardrail)(Citation: Symantec Elfin Mar 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 6件
- IOC観測: 11件
- 複数攻撃で観測: 0件
- 要レビュー候補: 5件
- 非IOC artifact観測: 91件（`artifacts.csv`）

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
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--apt33--02fb6f75ae3e030e | APT group activities under the shadow of the epidemic(2020) |  | 2020 | summary/2021/APT group activities under the shadow of the epidemic(2020).pdf | report | TLP:CLEAR | 中 |
| source--apt33--065b937e991ce756 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--apt33--0b9dafc56d80c625 | evol agrius |  | 不明 | Agrius/evol-agrius.pdf | report | TLP:CLEAR | 中 |
| source--apt33--0cb2bbf15acf2e99 | Qianxin 2023 APT Report |  | 2023 | summary/2024/Qianxin 2023 APT Report.pdf | report | TLP:CLEAR | 中 |
| source--apt33--17fedb1ca82c301b | Cybersecurity Threats 2024 Mid Year Report |  | 2024 | summary/2024/Cybersecurity Threats 2024 Mid-Year Report.pdf | report | TLP:CLEAR | 中 |
| source--apt33--22c66d8bf511e128 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--apt33--25513805dfd844fe | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--apt33--258a58c52d4301e7 | 2024 Malicious Infrastructure Report |  | 2024 | summary/2025/2024 Malicious Infrastructure Report.pdf | report | TLP:CLEAR | 中 |
| source--apt33--25e4e06ab5e0bc91 | 2023 Adversary Infrastructure Report |  | 2023 | summary/2024/2023 Adversary Infrastructure Report .pdf | report | TLP:CLEAR | 中 |
| source--apt33--2b15b977c6f02cb7 | ClearSky Fox Kitten Campaign v1 |  | 不明 | International Strategic/Iran/ClearSky-Fox-Kitten-Campaign-v1.pdf | report | TLP:CLEAR | 中 |
| source--apt33--2c68e293fe52b9cc | Raport analize PROFILI I GRUPEVE TE HAKERAVE IRANIANE |  | 不明 | summary/2024/Raport-analize-PROFILI-I-GRUPEVE-TE-HAKERAVE-IRANIANE.pdf | report | TLP:CLEAR | 中 |
| source--apt33--30f97955f8029d4a | Global APT 2022 Annual Report qianxin |  | 2022 | summary/2023/Global APT 2022 Annual Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--apt33--39a72f5f3ddb46fd | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--apt33--4ff21597c1864686 | Cybersecurity Threats 2024 Annual Report QAX |  | 2024 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | report | TLP:CLEAR | 中 |
| source--apt33--6fb4e6d6fa2340bb | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--apt33--7773507fff9457cc | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--apt33--7b9b37d39177d968 | apt33 |  | 不明 | actor_profile/evidence/apt33.csv | structured-data | TLP:CLEAR | 中 |
| source--apt33--843b3708dccce06b | Global APT Mid 2022 Report qianxin |  | 2022 | summary/2022/Global APT Mid-2022 Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--apt33--88ae954aeb191674 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--apt33--8bf16e0018a71b02 | 2022 APT Activity Analysis Report threatbook |  | 2022 | summary/2023/2022 APT Activity Analysis Report threatbook.pdf | report | TLP:CLEAR | 中 |
| source--apt33--8d3dfd25cba877a4 | README |  | 不明 | International Strategic/Iran/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--apt33--a3a96d88c9ca32d0 | Adversary Infrastructure Report 2020 |  | 2020 | summary/2021/Adversary Infrastructure Report 2020.pdf | report | TLP:CLEAR | 中 |
| source--apt33--a6d57633cace8799 | Automating APT Campaign and Group Attribution |  | 不明 | APT-hunting/Automating APT Campaign and Group Attribution.pdf | report | TLP:CLEAR | 中 |
| source--apt33--b0f3813af35af268 | Cloudflare 2026 threat report |  | 2026 | summary/2026/Cloudflare-2026-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--apt33--c236c1b55a556af4 | rpt mtrends 2021 fireeye |  | 2021 | summary/2021/rpt-mtrends-2021-fireeye.pdf | report | TLP:CLEAR | 中 |
| source--apt33--c3aef2ab0a2726d2 | Virtual Routes Pharos Report Series No. 3 |  | 不明 | cybercrime/2025/Virtual-Routes-Pharos-Report-Series-No.-3.pdf | report | TLP:CLEAR | 中 |
| source--apt33--d072cdd45109e424 | Dream Job Campaign |  | 不明 | lazarus/Dream-Job-Campaign.pdf | report | TLP:CLEAR | 中 |
| source--apt33--d3df871da4b1750d | MDDR FINAL 2023 1004 |  | 2023-10-04 | summary/2023/MDDR_FINAL_2023_1004.pdf | report | TLP:CLEAR | 中 |
| source--apt33--e033bbba77c28cbb | PWC cyber threats 2019 retrospect |  | 2019 | summary/2020/PWC-cyber-threats-2019-retrospect.pdf | report | TLP:CLEAR | 中 |
| source--daily-f8c5f7e3f2497c4aec2e | APT33(イランのハッキンググループ)、新しいTicklerマルウェアを使用して米国政府・防衛機関にバックドアを設置 | bleepingcomputer.com | 2024-08-29 | https://www.bleepingcomputer.com/news/security/APT33-Iranian-hacking-group-uses-new-tickler-malware-to-backdoor-us-govt-defense-orgs/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
