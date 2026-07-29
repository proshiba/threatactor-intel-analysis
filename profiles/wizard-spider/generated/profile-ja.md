# Wizard Spider 脅威アクタープロファイル

- プロファイルID: `actor--wizard-spider`
- 状態: draft
- 更新日時: 2026-07-29T15:36:13Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Wizard Spiderの標準化プロファイル。リポジトリ内の専用資料2件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Wizard Spider**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| DEV-0193 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| DEV-0237 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| FIN12 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| GOLD BLACKBURN | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Grim Spider | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| ITG23 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Periwinkle Tempest | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Pistachio Tempest | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TEMP.MixMaster | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| UNC1878 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

## 帰属

未評価

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: なし

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| financial-gain | Financially motivated intrusion or fraud. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| EXOTIC LILY | related-to | [EXOTIC LILY](https://attack.mitre.org/groups/G1011) is a financially motivated group that has been closely linked with [Wizard Spider](https://attack.mitre.org/groups/G0102) and the deployment of ransomware including [Conti](https://attack.mitre.org/software/S0575) and [Diavol](https://attack.mitre.org/software/S0659). | 中 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Wizard Spider](https://attack.mitre.org/groups/G0102) is a Russia-based financially motivated threat group originally known for the creation and deployment of [TrickBot](https://attack.mitre.org/software/S0266) since at least 2016. [Wizard Spider](https://attack.mitre.org/groups/G0102) possesses a diverse arsenal of tools and has conducted ransomware campaigns against a variety of organizations, ranging from major corporations to hospitals.(Citation: CrowdStrike Ryuk January 2019)(Citation: DHS/CISA Ransomware Targeting Healthcare October 2020)(Citation: CrowdStrike Wizard Spider October 2020) |
| Capability | TrickBot, Emotet, SystemBC, Conti, Diavol, Anchor, Dyre, Bazar, Ryuk, Cobalt Strike, GrimAgent, Net, BloodHound, Empire, BITSAdmin, Nltest, Mimikatz, LaZagne, Ping, Rubeus, AdFind, PsExec |
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
| etda-threat-group-cards | FIN12 | single-alias-intersection | 中 |  | https://www.mandiant.com/resources/fin12-ransomware-intrusion-actor-pursuing-healthcare-targets<br>https://www.mandiant.com/media/12596/download<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=FIN12&n=1 |
| etda-threat-group-cards | UNC1878 | single-alias-intersection | 中 |  | https://www.bleepingcomputer.com/news/security/brooklyn-and-vermont-hospitals-are-latest-ryuk-ransomware-victims/<br>https://redcanary.com/blog/how-one-hospital-thwarted-a-ryuk-ransomware-outbreak/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=UNC1878&n=1 |
| etda-threat-group-cards | Wizard Spider, Gold Blackburn | canonical-name | 高 | Russia | https://www.crowdstrike.com/blog/sin-ful-spiders-wizard-spider-and-lunar-spider-sharing-the-same-web/<br>https://www.crowdstrike.com/blog/wizard-spider-lunar-spider-shared-proxy-module/<br>https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Periwinkle Tempest | canonical-name | 高 | Russia | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| microsoft-threat-actor-mapping | Pistachio Tempest | multiple-name-intersection | 高 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| microsoft-threat-actor-mapping | Storm-0230 | canonical-name | 高 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | GRIM SPIDER | single-alias-intersection | 中 |  | https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/<br>https://www.fireeye.com/blog/threat-research/2019/01/a-nasty-trick-from-credential-theft-malware-to-business-disruption.html |
| misp-threat-actor | WIZARD SPIDER | canonical-name | 高 | RU, Russian Federation | https://labs.sentinelone.com/top-tier-russian-organized-cybercrime-group-unveils-fileless-stealthy-powertrick-backdoor-for-high-value-targets/<br>https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/<br>https://www.crowdstrike.com/blog/sin-ful-spiders-wizard-spider-and-lunar-spider-sharing-the-same-web/ |
| misp-threat-actor | UNC1878 | single-alias-intersection | 中 |  | https://twitter.com/anthomsec/status/1321865315513520128<br>https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html<br>https://gist.github.com/aaronst/6aa7f61246f53a8dd4befea86e832456 |
| misp-microsoft-activity-group | Periwinkle Tempest | canonical-name | 高 | RU, Russia | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Pistachio Tempest | multiple-name-intersection | 高 |  | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Storm-0230 | canonical-name | 高 |  | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Wizard Spider - G0102 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0102<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://securityintelligence.com/posts/trickbot-gang-doubles-down-enterprise-infection/ |
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
| malware--trickbot | TrickBot | [TrickBot](https://attack.mitre.org/software/S0266) is a Trojan spyware program written in C++ that first emerged in September 2016 as a possible successor to [Dyre](https://attack.mitre.org/software/S0024). [TrickBot](https://attack.mitre.org/software/S0266) was developed and initially used by [Wizard Spider](https://attack.mitre.org/groups/G0102) for targeting banking sites in North America, Australia, and throughout Europe; it has since been used against all sectors worldwide as part of "big game hunting" ransomware campaigns.(Citation: S2 Grupo TrickBot June 2017)(Citation: Fidelis TrickBot Oct 2016)(Citation: IBM TrickBot Nov 2016)(Citation: CrowdStrike Wizard Spider October 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--emotet | Emotet | [Emotet](https://attack.mitre.org/software/S0367) is a modular malware variant which is primarily used as a downloader for other malware variants such as [TrickBot](https://attack.mitre.org/software/S0266) and [IcedID](https://attack.mitre.org/software/S0483). Emotet first emerged in June 2014, initially targeting the financial sector, and has expanded to multiple verticals over time.(Citation: Trend Micro Banking Malware Jan 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--systembc | SystemBC | [SystemBC](https://attack.mitre.org/software/S9001) is a malware family offered as a malware-as-a-service (MaaS) that is used to establish command and control and facilitate follow-on activity, including ransomware deployment.[SystemBC](https://attack.mitre.org/software/S9001) executes a variety of tasks including setting up SOCKS5 proxies, maintaining persistence, ingesting malicious files, and handing C2 communication. [SystemBC](https://attack.mitre.org/software/S9001) was first detected in 2018, and has been used by [Wizard Spider](https://attack.mitre.org/groups/G0102) since at least 2020, and by [FIN7](https://attack.mitre.org/groups/G0046) since at least 2022.(Citation: TrumanKroll_SYSTEMBCServer_Jan2024)(Citation: SophosGnGal_SystemBC_Dec2020)(Citation: BlackBasta)(Citation: AhnLab_SystemBC_Apr2022)(Citation: Lumen_SystemBC_Sept2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--conti | Conti | [Conti](https://attack.mitre.org/software/S0575) is a Ransomware-as-a-Service (RaaS) that was first observed in December 2019. [Conti](https://attack.mitre.org/software/S0575) has been deployed via [TrickBot](https://attack.mitre.org/software/S0266) and used against major corporations and government agencies, particularly those in North America. As with other ransomware families, actors using [Conti](https://attack.mitre.org/software/S0575) steal sensitive files and information from compromised networks, and threaten to publish this data unless the ransom is paid.(Citation: Cybereason Conti Jan 2021)(Citation: CarbonBlack Conti July 2020)(Citation: Cybleinc Conti January 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--diavol | Diavol | [Diavol](https://attack.mitre.org/software/S0659) is a ransomware variant first observed in June 2021 that is capable of prioritizing file types to encrypt based on a pre-configured list of extensions defined by the attacker.  The [Diavol](https://attack.mitre.org/software/S0659) Ransomware-as-a Service (RaaS) program is managed by [Wizard Spider](https://attack.mitre.org/groups/G0102) and it has been observed being deployed by [Bazar](https://attack.mitre.org/software/S0534).(Citation: Fortinet Diavol July 2021)(Citation: FBI Flash Diavol January 2022)(Citation: DFIR Diavol Ransomware December 2021)(Citation: Microsoft Ransomware as a Service) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--anchor | Anchor | [Anchor](https://attack.mitre.org/software/S0504) is one of a family of backdoor malware that has been used in conjunction with [TrickBot](https://attack.mitre.org/software/S0266) on selected high profile targets since at least 2018.(Citation: Cyberreason Anchor December 2019)(Citation: Medium Anchor DNS July 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--dyre | Dyre | [Dyre](https://attack.mitre.org/software/S0024) is a banking Trojan that has been used for financial gain. <br> (Citation: Symantec Dyre June 2015)(Citation: Malwarebytes Dyreza November 2015) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--bazar | Bazar | [Bazar](https://attack.mitre.org/software/S0534) is a downloader and backdoor that has been used since at least April 2020, with infections primarily against professional services, healthcare, manufacturing, IT, logistics and travel companies across the US and Europe. [Bazar](https://attack.mitre.org/software/S0534) reportedly has ties to [TrickBot](https://attack.mitre.org/software/S0266) campaigns and can be used to deploy additional malware, including ransomware, and to steal sensitive data.(Citation: Cybereason Bazar July 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--ryuk | Ryuk | [Ryuk](https://attack.mitre.org/software/S0446) is a ransomware designed to target enterprise environments that has been used in attacks since at least 2018. [Ryuk](https://attack.mitre.org/software/S0446) shares code similarities with Hermes ransomware.(Citation: CrowdStrike Ryuk January 2019)(Citation: FireEye Ryuk and Trickbot January 2019)(Citation: FireEye FIN6 Apr 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--cobalt-strike | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) is a commercial, full-featured, remote access tool that bills itself as “adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors”. Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.(Citation: cobaltstrike manual)<br><br>In addition to its own capabilities, [Cobalt Strike](https://attack.mitre.org/software/S0154) leverages the capabilities of other well-known tools such as Metasploit and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: cobaltstrike manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--grimagent | GrimAgent | [GrimAgent](https://attack.mitre.org/software/S0632) is a backdoor that has been used before the deployment of [Ryuk](https://attack.mitre.org/software/S0446) ransomware since at least 2020; it is likely used by [FIN6](https://attack.mitre.org/groups/G0037) and [Wizard Spider](https://attack.mitre.org/groups/G0102).(Citation: Group IB GrimAgent July 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--bloodhound | BloodHound | [BloodHound](https://attack.mitre.org/software/S0521) is an Active Directory (AD) reconnaissance tool that can reveal hidden relationships and identify attack paths within an AD environment.(Citation: GitHub Bloodhound)(Citation: CrowdStrike BloodHound April 2018)(Citation: FoxIT Wocao December 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--empire | Empire | [Empire](https://attack.mitre.org/software/S0363) is an open-source, cross-platform remote administration and post-exploitation framework that is publicly available on GitHub. While the tool itself is primarily written in Python, the post-exploitation agents are written in pure [PowerShell](https://attack.mitre.org/techniques/T1059/001) for Windows and Python for Linux/macOS. [Empire](https://attack.mitre.org/software/S0363) was one of five tools singled out by a joint report on public hacking tools being widely used by adversaries.(Citation: NCSC Joint Report Public Tools)(Citation: Github PowerShell Empire)(Citation: GitHub ATTACK Empire) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--bitsadmin | BITSAdmin | [BITSAdmin](https://attack.mitre.org/software/S0190) is a command line tool used to create and manage [BITS Jobs](https://attack.mitre.org/techniques/T1197). (Citation: Microsoft BITSAdmin) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--nltest | Nltest | [Nltest](https://attack.mitre.org/software/S0359) is a Windows command-line utility used to list domain controllers and enumerate domain trusts.(Citation: Nltest Manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--lazagne | LaZagne | [LaZagne](https://attack.mitre.org/software/S0349) is a post-exploitation, open-source tool used to recover stored passwords on a system. It has modules for Windows, Linux, and OSX, but is mainly focused on Windows systems. [LaZagne](https://attack.mitre.org/software/S0349) is publicly available on GitHub.(Citation: GitHub LaZagne Dec 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ping | Ping | [Ping](https://attack.mitre.org/software/S0097) is an operating system utility commonly used to troubleshoot and verify network connections. (Citation: TechNet Ping) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--rubeus | Rubeus | [Rubeus](https://attack.mitre.org/software/S1071) is a C# toolset designed for raw Kerberos interaction that has been used since at least 2020, including in ransomware operations.(Citation: GitHub Rubeus March 2023)(Citation: FireEye KEGTAP SINGLEMALT October 2020)(Citation: DFIR Ryuk's Return October 2020)(Citation: DFIR Ryuk 2 Hour Speed Run November 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
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
| Dataresolution.net (MSP for multiple US newpapers) | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Onslow, North Carolina water | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

Onslow, North Carolina water; Dataresolution.net (MSP for multiple US newpapers)

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | 医療・ヘルスケア | [Wizard Spider](https://attack.mitre.org/groups/G0102) possesses a diverse arsenal of tools and has conducted ransomware campaigns against a variety of organizations, ranging from major corporations to hospitals.(Citation: CrowdStrike Ryuk January 2019)(Citation: DHS/CISA Ransomware Targeting Healthcare October 2020)(Citation: CrowdStrike Wizard Spider October 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 未評価

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.001 | LSASS Memory | [Wizard Spider](https://attack.mitre.org/groups/G0102) has dumped the lsass.exe memory to harvest credentials with the use of open-source tool [LaZagne](https://attack.mitre.org/software/S0349).(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.002 | Security Account Manager | [Wizard Spider](https://attack.mitre.org/groups/G0102) has acquired credentials from the SAM/SECURITY registry hives.(Citation: FireEye KEGTAP SINGLEMALT October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.003 | NTDS | [Wizard Spider](https://attack.mitre.org/groups/G0102) has gained access to credentials via exported copies of the ntds.dit Active Directory database. [Wizard Spider](https://attack.mitre.org/groups/G0102) has also created a volume shadow copy and used a batch script file to collect NTDS.dit with the use of the Windows utility, ntdsutil.(Citation: FireEye KEGTAP SINGLEMALT October 2020)(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | [Wizard Spider](https://attack.mitre.org/groups/G0102) has collected data from a compromised host prior to exfiltration.(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used [ipconfig](https://attack.mitre.org/software/S0100) to identify the network configuration of a victim machine. [Wizard Spider](https://attack.mitre.org/groups/G0102) has also used the PowerShell cmdlet `Get-ADComputer` to collect IP address data from Active Directory.(Citation: Sophos New Ryuk Attack October 2020)(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used networkdll for network discovery and psfin specifically for financial and point of sale indicators. [Wizard Spider](https://attack.mitre.org/groups/G0102) has also used [AdFind](https://attack.mitre.org/software/S0552), <code>nltest/dclist</code>, and PowerShell script Get-DataInfo.ps1 to enumerate domain computers, including the domain controller.(Citation: FireEye Ryuk and Trickbot January 2019)(Citation: CrowdStrike Grim Spider May 2019)(Citation: FireEye KEGTAP SINGLEMALT October 2020)(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: DFIR Ryuk's Return October 2020)(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021 | Remote Services | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used the WebDAV protocol to execute [Ryuk](https://attack.mitre.org/software/S0446) payloads hosted on network file shares.(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used RDP for lateral movement and to deploy ransomware interactively.(Citation: CrowdStrike Grim Spider May 2019)(Citation: DHS/CISA Ransomware Targeting Healthcare October 2020)(Citation: DFIR Ryuk 2 Hour Speed Run November 2020)(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used SMB to drop Cobalt Strike Beacon on a domain controller for lateral movement.(Citation: DFIR Ryuk 2 Hour Speed Run November 2020)(Citation: DFIR Ryuk's Return October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.006 | Windows Remote Management | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used Window Remote Management to move laterally through a victim network.(Citation: DHS/CISA Ransomware Targeting Healthcare October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.010 | Command Obfuscation | [Wizard Spider](https://attack.mitre.org/groups/G0102) used Base64 encoding to obfuscate an [Empire](https://attack.mitre.org/software/S0363) service and PowerShell commands.(Citation: FireEye Ryuk and Trickbot January 2019)(Citation: DFIR Ryuk's Return October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used "whoami" to identify the local user and their privileges.(Citation: Sophos New Ryuk Attack October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.004 | Masquerade Task or Service | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used scheduled tasks to install [TrickBot](https://attack.mitre.org/software/S0266), using task names to appear legitimate such as WinDotNet, GoogleTask, or Sysnetsf.(Citation: CrowdStrike Grim Spider May 2019) It has also used common document file names for other malware binaries.(Citation: FireEye KEGTAP SINGLEMALT October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | [Wizard Spider](https://attack.mitre.org/groups/G0102) has exfiltrated domain credentials and network enumeration information over command and control (C2) channels.(Citation: CrowdStrike Grim Spider May 2019)(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used WMI and LDAP queries for network discovery and to move laterally. [Wizard Spider](https://attack.mitre.org/groups/G0102) has also used batch scripts to leverage WMIC to deploy ransomware.(Citation: CrowdStrike Grim Spider May 2019)(Citation: DHS/CISA Ransomware Targeting Healthcare October 2020)(Citation: FireEye KEGTAP SINGLEMALT October 2020)(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1048.003 | Exfiltration Over Unencrypted Non-C2 Protocol | [Wizard Spider](https://attack.mitre.org/groups/G0102) has exfiltrated victim information using FTP.(Citation: DFIR Ryuk's Return October 2020)(Citation: DFIR Ryuk 2 Hour Speed Run November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used scheduled tasks to establish persistence for [TrickBot](https://attack.mitre.org/software/S0266) and other malware.(Citation: CrowdStrike Grim Spider May 2019)(Citation: DHS/CISA Ransomware Targeting Healthcare October 2020)(Citation: FireEye KEGTAP SINGLEMALT October 2020)(Citation: DFIR Ryuk 2 Hour Speed Run November 2020)(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055 | Process Injection | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used process injection to execute payloads to escalate privileges.(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055.001 | Dynamic-link Library Injection | [Wizard Spider](https://attack.mitre.org/groups/G0102) has injected malicious DLLs into memory with read, write, and execute permissions.(Citation: DHS/CISA Ransomware Targeting Healthcare October 2020)(Citation: DFIR Ryuk 2 Hour Speed Run November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used macros to execute PowerShell scripts to download malware on victim's machines.(Citation: CrowdStrike Grim Spider May 2019) It has also used PowerShell to execute commands and move laterally through a victim network.(Citation: DHS/CISA Ransomware Targeting Healthcare October 2020)(Citation: FireEye KEGTAP SINGLEMALT October 2020)(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used `cmd.exe` to execute commands on a victim's machine.(Citation: DFIR Ryuk's Return October 2020)(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used file deletion to remove some modules and configurations from an infected host after use.(Citation: CrowdStrike Grim Spider May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used HTTP for network communications.(Citation: CrowdStrike Grim Spider May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074 | Data Staged | [Wizard Spider](https://attack.mitre.org/groups/G0102) has collected and staged credentials and network enumeration information, using  the networkdll and psfin [TrickBot](https://attack.mitre.org/software/S0266) modules.(Citation: CrowdStrike Grim Spider May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | [Wizard Spider](https://attack.mitre.org/groups/G0102) has staged ZIP files in local directories such as, `C:\PerfLogs\1\` and `C:\User\1\` prior to exfiltration.(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used valid credentials for privileged accounts with the goal of accessing domain controllers.(Citation: CrowdStrike Grim Spider May 2019)(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.002 | Domain Accounts | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used administrative accounts, including Domain Admin, to move laterally within a victim network.(Citation: FireEye KEGTAP SINGLEMALT October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used [Systeminfo](https://attack.mitre.org/software/S0096) and similar commands to acquire detailed configuration information of a victim's machine. [Wizard Spider](https://attack.mitre.org/groups/G0102) has also utilized the PowerShell cmdlet `Get-ADComputer` to collect DNS hostnames, last logon dates, and operating system information from Active Directory.(Citation: DFIR Ryuk's Return October 2020)(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | [Wizard Spider](https://attack.mitre.org/groups/G0102) has identified domain admins through the use of `net group "Domain admins" /DOMAIN`. [Wizard Spider](https://attack.mitre.org/groups/G0102) has also leveraged the PowerShell cmdlet `Get-ADComputer` to collect account names from Active Directory data.(Citation: DFIR Ryuk's Return October 2020)(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [Wizard Spider](https://attack.mitre.org/groups/G0102) can transfer malicious payloads such as ransomware to compromised machines.(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | [Wizard Spider](https://attack.mitre.org/groups/G0102) has modified the Registry key <code>HKLM\System\CurrentControlSet\Control\SecurityProviders\WDigest</code> by setting the <code>UseLogonCredential</code> registry value to <code>1</code> in order to force credentials to be stored in clear text in memory. [Wizard Spider](https://attack.mitre.org/groups/G0102) has also modified the WDigest registry key to allow plaintext credentials to be cached in memory.(Citation: CrowdStrike Grim Spider May 2019)(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence | T1133 | External Remote Services | [Wizard Spider](https://attack.mitre.org/groups/G0102) has accessed victim networks by using stolen credentials to access the corporate VPN infrastructure.(Citation: FireEye KEGTAP SINGLEMALT October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1135 | Network Share Discovery | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used the “net view” command to locate mapped network shares.(Citation: DHS/CISA Ransomware Targeting Healthcare October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1136.001 | Local Account | [Wizard Spider](https://attack.mitre.org/groups/G0102) has created local administrator accounts to maintain persistence in compromised networks.(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1136.002 | Domain Account | [Wizard Spider](https://attack.mitre.org/groups/G0102) has created and used new accounts within a victim's Active Directory environment to maintain persistence.(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Stealth | T1197 | BITS Jobs | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used batch scripts that utilizes WMIC to execute a [BITSAdmin](https://attack.mitre.org/software/S0190) transfer of a ransomware payload to each compromised machine.(Citation: Mandiant FIN12 Oct 2021)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | [Wizard Spider](https://attack.mitre.org/groups/G0102) has lured victims into clicking a malicious link delivered through spearphishing.(Citation: DHS/CISA Ransomware Targeting Healthcare October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [Wizard Spider](https://attack.mitre.org/groups/G0102) has lured victims to execute malware with spearphishing attachments containing macros to download either [Emotet](https://attack.mitre.org/software/S0367), Bokbot, [TrickBot](https://attack.mitre.org/software/S0266), or [Bazar](https://attack.mitre.org/software/S0534).(Citation: CrowdStrike Grim Spider May 2019)(Citation: CrowdStrike Wizard Spider October 2020)(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1210 | Exploitation of Remote Services | [Wizard Spider](https://attack.mitre.org/groups/G0102) has exploited or attempted to exploit Zerologon (CVE-2020-1472) and EternalBlue (MS17-010) vulnerabilities.(Citation: FireEye KEGTAP SINGLEMALT October 2020)(Citation: DFIR Ryuk's Return October 2020)(Citation: DFIR Ryuk in 5 Hours October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.011 | Rundll32 | [Wizard Spider](https://attack.mitre.org/groups/G0102) has utilized `rundll32.exe` to deploy ransomware commands with the use of WebDAV.(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1222.001 | Windows Permissions | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used the icacls command to modify access control to backup servers, providing them with full control of all the system folders.(Citation: Sophos New Ryuk Attack October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1489 | Service Stop | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used taskkill.exe and net.exe to stop backup, catalog, cloud, and other services prior to network encryption.(Citation: DFIR Ryuk's Return October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1490 | Inhibit System Recovery | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used WMIC and vssadmin to manually delete volume shadow copies. [Wizard Spider](https://attack.mitre.org/groups/G0102) has also used [Conti](https://attack.mitre.org/software/S0575) ransomware to delete volume shadow copies automatically with the use of vssadmin.(Citation: Mandiant FIN12 Oct 2021)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518.001 | Security Software Discovery | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used WMI to identify anti-virus products installed on a victim's machine.(Citation: DFIR Ryuk's Return October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518.002 | Backup Software Discovery | [Wizard Spider](https://attack.mitre.org/groups/G0102) has utilized the PowerShell script `Get-DataInfo.ps1` to collect installed backup software information from a compromised machine.(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | [Wizard Spider](https://attack.mitre.org/groups/G0102) has installed [TrickBot](https://attack.mitre.org/software/S0266) as a service named ControlServiceA in order to establish persistence.(Citation: CrowdStrike Grim Spider May 2019)(Citation: Mandiant FIN12 Oct 2021)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [Wizard Spider](https://attack.mitre.org/groups/G0102) has established persistence via the Registry key <code>HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run</code> and a shortcut within the startup folder.(Citation: DHS/CISA Ransomware Targeting Healthcare October 2020)(Citation: FireEye KEGTAP SINGLEMALT October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.004 | Winlogon Helper DLL | [Wizard Spider](https://attack.mitre.org/groups/G0102) has established persistence using Userinit by adding the Registry key HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon.(Citation: FireEye KEGTAP SINGLEMALT October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1550.002 | Pass the Hash | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used the `Invoke-SMBExec` PowerShell cmdlet to execute the pass-the-hash technique and utilized stolen password hashes to move laterally.(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.006 | Group Policy Preferences | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used PowerShell cmdlets `Get-GPPPassword` and `Find-GPOPassword` to find unsecured credentials in a compromised network group policy.(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1553.002 | Code Signing | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used Digicert code-signing certificates for some of its malware.(Citation: DFIR Ryuk 2 Hour Speed Run November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.004 | Windows Credential Manager | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used PowerShell cmdlet `Invoke-WCMDump` to enumerate Windows credentials in the Credential Manager in a compromised network.(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1557.001 | Name Resolution Poisoning and SMB Relay | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used the Invoke-Inveigh PowerShell cmdlets, likely for name service poisoning.(Citation: FireEye KEGTAP SINGLEMALT October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1558.003 | Kerberoasting | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used Rubeus, MimiKatz Kerberos module, and the Invoke-Kerberoast cmdlet to steal AES hashes.(Citation: DFIR Ryuk's Return October 2020)(Citation: FireEye KEGTAP SINGLEMALT October 2020)(Citation: DHS/CISA Ransomware Targeting Healthcare October 2020)(Citation: DFIR Ryuk 2 Hour Speed Run November 2020)(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | [Wizard Spider](https://attack.mitre.org/groups/G0102) has archived data into ZIP files on compromised machines.(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used spearphishing attachments to deliver Microsoft documents containing macros or PDFs containing malicious links to download either [Emotet](https://attack.mitre.org/software/S0367), Bokbot, [TrickBot](https://attack.mitre.org/software/S0266), or [Bazar](https://attack.mitre.org/software/S0534).(Citation: CrowdStrike Grim Spider May 2019)(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | [Wizard Spider](https://attack.mitre.org/groups/G0102) has sent phishing emails containing a link to an actor-controlled Google Drive document or other free online file hosting services.(Citation: DHS/CISA Ransomware Targeting Healthcare October 2020)(Citation: DFIR Ryuk 2 Hour Speed Run November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | [Wizard Spider](https://attack.mitre.org/groups/G0102) has exfiltrated stolen victim data to various cloud storage providers.(Citation: Mandiant FIN12 Oct 2021)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1569.002 | Service Execution | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used `services.exe` to execute scripts and executables during lateral movement within a victim's network. [Wizard Spider](https://attack.mitre.org/groups/G0102) has also used batch scripts that leverage [PsExec](https://attack.mitre.org/software/S0029) to execute a previously transferred ransomware payload on a victim's network.(Citation: DFIR Ryuk's Return October 2020)(Citation: DFIR Ryuk in 5 Hours October 2020)(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1570 | Lateral Tool Transfer | [Wizard Spider](https://attack.mitre.org/groups/G0102) has used stolen credentials to copy tools into the <code>%TEMP%</code> directory of domain controllers.(Citation: CrowdStrike Grim Spider May 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.002 | Email Accounts | [Wizard Spider](https://attack.mitre.org/groups/G0102) has leveraged ProtonMail email addresses in ransom notes when delivering [Ryuk](https://attack.mitre.org/software/S0446) ransomware.(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [Wizard Spider](https://attack.mitre.org/groups/G0102) has utilized tools such as [Empire](https://attack.mitre.org/software/S0363), [Cobalt Strike](https://attack.mitre.org/software/S0154), [Cobalt Strike](https://attack.mitre.org/software/S0154), [Rubeus](https://attack.mitre.org/software/S1071), [AdFind](https://attack.mitre.org/software/S0552), [BloodHound](https://attack.mitre.org/software/S0521), Metasploit, Advanced IP Scanner, Nirsoft PingInfoView, and SoftPerfect Network Scanner for targeting efforts.(Citation: FireEye KEGTAP SINGLEMALT October 2020)(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.003 | Code Signing Certificates | [Wizard Spider](https://attack.mitre.org/groups/G0102) has obtained code signing certificates signed by DigiCert, GlobalSign, and COMOOD for malware payloads.(Citation: DFIR Ryuk 2 Hour Speed Run November 2020)(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | [Wizard Spider](https://attack.mitre.org/groups/G0102) has shut down or uninstalled security applications on victim systems that might prevent ransomware from executing.(Citation: DHS/CISA Ransomware Targeting Healthcare October 2020)(Citation: FireEye KEGTAP SINGLEMALT October 2020)(Citation: DFIR Ryuk's Return October 2020)(Citation: Mandiant FIN12 Oct 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 96件
- IOC観測: 112件
- 複数攻撃で観測: 0件
- 要レビュー候補: 52件
- 非IOC artifact観測: 5件（`artifacts.csv`）

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
| source--wizard-spider--9a0477438aa5fd18 | README |  | 不明 | Wizard Spider/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--wizard-spider--22dc374104658049 | WizardSpider TLPWHITE v.1.4 |  | 不明 | Wizard Spider/WizardSpider_TLPWHITE_v.1.4.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
