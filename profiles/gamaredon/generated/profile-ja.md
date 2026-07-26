# Gamaredon 脅威アクタープロファイル

- プロファイルID: `actor--gamaredon`
- 状態: draft
- 更新日時: 2026-07-26T06:00:42Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Gamaredonの標準化プロファイル。リポジトリ内の専用資料9件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Gamaredon**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| ACTINIUM | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Aqua Blizzard | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Armageddon | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| DEV-0157 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Gamaredon Group | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| IRON TILDEN | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| NastyShrew | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Primitive Bear | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Shuckworm | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| Adversary | [Gamaredon Group](https://attack.mitre.org/groups/G0047) is a suspected Russian cyber espionage group that has targeted military, law enforcement, judiciary, non-profit, and non-governmental organizations in Ukraine since at least 2013. The name [Gamaredon Group](https://attack.mitre.org/groups/G0047) derives from a misspelling of the word "Armageddon," found in early campaigns.(Citation: Palo Alto Gamaredon Feb 2017)(Citation: TrendMicro Gamaredon April 2020)(Citation: ESET Gamaredon June 2020)(Citation: Symantec Shuckworm January 2022)(Citation: Microsoft Actinium February 2022)<br><br>In November 2021, the Ukrainian government publicly attributed [Gamaredon Group](https://attack.mitre.org/groups/G0047) to Russia’s Federal Security Service (FSB) Center 18, an assessment later supported by multiple independent cybersecurity researchers. (Citation: Bleepingcomputer Gamardeon FSB November 2021)(Citation: Microsoft Actinium February 2022) |
| Capability | QuietSieve, Pteranodon, PowerPunch, Remcos, Ping, Reg |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Gamaredon Group | multiple-name-intersection | 高 | Russia | https://www.lookingglasscyber.com/wp-content/uploads/2015/08/Operation_Armageddon_Final.pdf<br>https://unit42.paloaltonetworks.com/unit-42-title-gamaredon-group-toolset-evolution/<br>https://www.fortinet.com/blog/threat-research/gamaredon-group-ttp-profile-analysis.html |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Aqua Blizzard | canonical-name | 高 | Russia | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Gamaredon Group | multiple-name-intersection | 高 | RU | http://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution<br>https://www.lookingglasscyber.com/wp-content/uploads/2015/08/Operation_Armageddon_Final.pdf<br>https://unit42.paloaltonetworks.com/unit-42-title-gamaredon-group-toolset-evolution |
| misp-microsoft-activity-group | Aqua Blizzard | canonical-name | 高 | RU, Russia | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | Gamaredon Group - G0047 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0047<br>https://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution/ |
| misp-mitre-intrusion-set | Gamaredon Group - G0047 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0047<br>https://blog.cloudflare.com/2026-threat-report/<br>https://blog.trendmicro.com/trendlabs-security-intelligence/gamaredon-apt-group-use-covid-19-lure-in-campaigns/ |
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
| malware--daily-d2f92cab7d572d733a5d | GammaWorm | Gamaredonとの直接的な利用関係が一次資料レビューで確認されたマルウェア。 | 不明 | 不明 | 中 | `source--daily-f9666a37c61d10f83b24` |
| malware--daily-dee986e090a2e04cffbb | GammaPhish | Gamaredonとの直接的な利用関係が一次資料レビューで確認されたマルウェア。 | 不明 | 不明 | 中 | `source--daily-f9666a37c61d10f83b24` |
| malware--powerpunch | PowerPunch | [PowerPunch](https://attack.mitre.org/software/S0685) is a lightweight downloader that has been used by [Gamaredon Group](https://attack.mitre.org/groups/G0047) since at least 2021.(Citation: Microsoft Actinium February 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--pteranodon | Pteranodon | [Pteranodon](https://attack.mitre.org/software/S0147) is a custom backdoor used by [Gamaredon Group](https://attack.mitre.org/groups/G0047). (Citation: Palo Alto Gamaredon Feb 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--quietsieve | QuietSieve | [QuietSieve](https://attack.mitre.org/software/S0686) is an information stealer that has been used by [Gamaredon Group](https://attack.mitre.org/groups/G0047) since at least 2021.(Citation: Microsoft Actinium February 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--remcos | Remcos | [Remcos](https://attack.mitre.org/software/S0332) is a closed-source tool that is marketed as a remote control and surveillance software by a company called Breaking Security. [Remcos](https://attack.mitre.org/software/S0332) has been observed being used in malware campaigns.(Citation: Riskiq Remcos Jan 2018)(Citation: Talos Remcos Aug 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ping | Ping | [Ping](https://attack.mitre.org/software/S0097) is an operating system utility commonly used to troubleshoot and verify network connections. (Citation: TechNet Ping) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--reg | Reg | [Reg](https://attack.mitre.org/software/S0075) is a Windows utility used to interact with the Windows Registry. It can be used at the command-line interface to query, add, modify, and remove information. (Citation: Microsoft Reg)<br><br>Utilities such as [Reg](https://attack.mitre.org/software/S0075) are known to be used by persistent threats. (Citation: Windows Commands JPCERT) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### インフラ

未確認

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| FSBのマトリョーシカ #1/3：展開され続けるGamaredonの贈り物――GammaPhishとGammaWorm | reported-activity | 不明 | 不明 | Sekoiaは、2026年1月に展開されたGamaredonの感染チェーンの初期アクセスとワーム部分を分析した。 GamaredonはロシアFSBに公式に関連付けられるAPTで、ウクライナの政府・軍・重要インフラを長期的に標的化している。 GammaPhishはxHTMLとRARを使い、WinRARのCVE-2025-8088を悪用してStartupフォルダへHTAを配置する。 GammaWormはVBScript、NTFS ADS、RunOnce、スケジュールタスクを悪用して永続化し、USBやネットワーク共有で拡散する。 Telegram、Cloudflare、Teletype、Telegra.phなどの正規サービスをDDRとして悪用し、C2構成更新と任意コード実行を行う。 | 中 | `source--daily-f9666a37c61d10f83b24` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1001 | Data Obfuscation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003 | OS Credential Dumping | rdcoded namelist T1218 .011 Signed Binary Proxy Execution: Rundll32 Malware has used rundll32 to launch additional malicious components Credential Access T1003 Credential Dumping Mimikatz on numerous PC was executed Discovery T1082 System Information Discovery During cyber attack first stage scripts always collect system information and send it to C2 T1120 Peripheral Device Discovery Malware files hunt for removable stora |  |  | 不明 | 不明 | 中 | `source--gamaredon--9d4f2351eb5fd5c0` |
| Collection | T1005 | Data from Local System | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Command And Control | T1008 | Fallback Channels | uses base64 to encode data prior to exfiltration. T1568.001 Dynamic Resolution: Fast Flux DNS Gamaredon uses fast flux DNS for its C&C infrastructure. T1008 Fallback Channels PteroPSLoad obtains the C&C IP address from a Telegram channel. T1105 Ingress Tool Transfer PteroClone uses the rclone utility to download payloads from MEGA cloud storage. T1095 Non-Application Layer Protocol PteroPShell uses the TCP protocol for |  |  | 不明 | 不明 | 中 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995` |
| Discovery | T1012 | Query Registry | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--43ece8b760fd4f72`, `source--mitre-attack-19-1` |
| Discovery | T1016.001 | Internet Connection Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1020 | Automated Exfiltration | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Lateral Movement | T1021.005 | VNC | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1025 | Data from Removable Media | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--9d4f2351eb5fd5c0`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Stealth | T1027 | Obfuscated Files or Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--9d4f2351eb5fd5c0`, `source--mitre-attack-19-1` |
| Stealth | T1027.004 | Compile After Delivery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.006 | HTML Smuggling | c T1059.005 Execution:JavaScript T1059.007 Execution: MaliciousFile T1204.002 Persistence:RegistryRunKeys/ StartupFolder T1547.001 DefenseEvasion:HTMLSmuggling T1027.006 DefenseEvasion:Encrypted/EncodedFile T1027.013 CommandandControl:WebProtocols T1071.001 CommandandControl:Fast FluxDNS T1568.001 13 CTARU20241205 RecordedFuture ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--56ce9c37d34fb725`, `source--gamaredon--daa9dc266e370995` |
| Stealth | T1027.009 | Embedded Payloads | disable Word macro security. T1027.006 Obfuscated Files or Information: HTML Smuggling Gamaredon uses HTML smuggling in its spearphishing campaigns. T1027.009 Obfuscated Files or Information: Embedded Payloads PteroCDrop drops an embedded payload. T1027.010 Obfuscated Files or Information: Command Obfuscation Gamaredon uses base64 to encode PowerShell commands. T1027.011 Obfuscated Files or Information: Fileless St |  |  | 不明 | 不明 | 中 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995` |
| Stealth | T1027.010 | Command Obfuscation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Stealth | T1027.011 | Fileless Storage | CDrop drops an embedded payload. T1027.010 Obfuscated Files or Information: Command Obfuscation Gamaredon uses base64 to encode PowerShell commands. T1027.011 Obfuscated Files or Information: Fileless Storage PteroDig installs itself into the Registry. T1027.013 Obfuscated Files or Information: Encrypted/Encoded File Gamaredon obfuscates strings in payloads . T1218.005 System Binary Proxy Execution: Mshta Gamaredon |  |  | 不明 | 不明 | 中 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995` |
| Stealth | T1027.012 | LNK Icon Smuggling | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | ution: MaliciousFile T1204.002 Persistence:RegistryRunKeys/ StartupFolder T1547.001 DefenseEvasion:HTMLSmuggling T1027.006 DefenseEvasion:Encrypted/EncodedFile T1027.013 CommandandControl:WebProtocols T1071.001 CommandandControl:Fast FluxDNS T1568.001 13 CTARU20241205 RecordedFuture ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--56ce9c37d34fb725`, `source--gamaredon--daa9dc266e370995` |
| Stealth | T1027.015 | Compression | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Stealth | T1027.016 | Junk Code Insertion | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--9d4f2351eb5fd5c0`, `source--mitre-attack-19-1` |
| Stealth | T1036 | Masquerading | HKCU\Software\Microsoft\Office\<versio n>\<product>\Security\AccessVBOM T1036 Masquerading Group places components into Windows folder with names mimicking common system services or drivers T1221 Template Injection DOCX files contain a request body to download malicious DOT document templates T1497 .002 Virtualization/Sandbox Evasion Malware |  |  | 不明 | 不明 | 中 | `source--gamaredon--9d4f2351eb5fd5c0` |
| Stealth | T1036.003 | Rename Legitimate Utilities | eir C&C servers. T1070.004 Indicator Removal: File Deletion PteroBox, PteroPSDoor, and PteroVDoor delete staged files after successful exfiltration. T1036.003 Masquerading: Rename Legitimate Utilities PteroBox downloads the rclone utility under a different name. T1036.004 Masquerading: Masquerade Task or Service Various Gamaredon tools create scheduled tasks with benign -looking names. T1036.005 Masquerading: Match |  |  | 不明 | 不明 | 中 | `source--gamaredon--daa9dc266e370995` |
| Stealth | T1036.004 | Masquerade Task or Service | calling the method AmsiUtils.Uninitialize . T1070.004 Indicator Removal: File Deletion PteroPSDoor deletes staged files after successful exfiltration. T1036.004 Masquerading: Masquerade Task or Service Gamaredon creates registry keys with benign -looking names. T1036.007 Masquerading: Double File Extension PteroLNK creates files with so-called double extension s .docx.lnk and .rtf.lnk . T1112 Modify Registry PteroDoc m |  |  | 不明 | 不明 | 中 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Stealth | T1036.007 | Double File Extension | files after successful exfiltration. T1036.004 Masquerading: Masquerade Task or Service Gamaredon creates registry keys with benign -looking names. T1036.007 Masquerading: Double File Extension PteroLNK creates files with so-called double extension s .docx.lnk and .rtf.lnk . T1112 Modify Registry PteroDoc modifies the registry to disable Word macro security. T1027.006 Obfuscated Files or Information: HTML Smuggling Ga |  |  | 不明 | 不明 | 中 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995` |
| Stealth | T1036.008 | Masquerade File Type | ing itself. T1036.007 Masquerading: Double File Extension PteroLNK creates files with so -called double extensions, such as .docx.lnk and .jpeg.lnk . T1036.008 Masquerading: Masquerade File Type Various Gamaredon tools store VBScript payloads in files with randomized extensions. T1027.006 Obfuscated Files or Information: HTML Smuggling Gamaredon uses HTML smuggling in its spearphishing campaigns. T1027.009 Obfuscated Fi |  |  | 不明 | 不明 | 中 | `source--gamaredon--daa9dc266e370995` |
| Persistence, Privilege Escalation | T1037.001 | Logon Script (Windows) | oot or Logon Autostart Execution: Registry Run Keys / Startup Folder Downloader of PteroPSDoor variant 1 uses the Startup directory for persistence. T1037.001 Boot or Logon Initialization Scripts: Logon Script (Windows) PteroSand achieves persistence by setting the UserInitMprLogonScript regist ry key . T1137.001 Office Application Startup: Office Template Macros PteroTemplate inserts a VBA macro into the Normal.dotm |  |  | 不明 | 不明 | 中 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995` |
| Collection | T1039 | Data from Network Shared Drive | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--43ece8b760fd4f72`, `source--gamaredon--9d4f2351eb5fd5c0`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--9d4f2351eb5fd5c0`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053 | Scheduled Task/Job | Spearphishing Link Execution T1059 .001 PowerShell Group executes ps1 scripts in system .005 Visual Basic Group executes numerous vbs scripts in system T1053 .005 Scheduled Task Group sets up scheduled tasks to launch scripts and downloaded tasklist T1047 WMI Group uses WMI commands in code to retrieve system information T1059 Command-Line Interface Group executes cmd scripts in system T1559 .001 Inter-Process Communication: |  |  | 不明 | 不明 | 中 | `source--gamaredon--9d4f2351eb5fd5c0` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055 | Process Injection | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Execution | T1059 | Command and Scripting Interpreter | ial Access T1566 .001 Spearphishing Attachment Group sends spear phishing emails with malicious attachments or links .002 Spearphishing Link Execution T1059 .001 PowerShell Group executes ps1 scripts in system .005 Visual Basic Group executes numerous vbs scripts in system T1053 .005 Scheduled Task Group sets up scheduled tasks to launch scripts and downloaded tasklist T1047 WMI Group uses WMI commands in code to retrieve sy |  |  | 不明 | 不明 | 中 | `source--gamaredon--9d4f2351eb5fd5c0` |
| Execution | T1059.001 | PowerShell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--56ce9c37d34fb725`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Execution | T1059.007 | JavaScript | dixB—MITREATT&CKTechniques Tactic:Technique ATT&CKCode Initial Access: SpearphishingAttachment T1566.001 Execution: Visual Basic T1059.005 Execution:JavaScript T1059.007 Execution: MaliciousFile T1204.002 Persistence:RegistryRunKeys/ StartupFolder T1547.001 DefenseEvasion:HTMLSmuggling T1027.006 DefenseEvasion:Encrypted/EncodedFile T1027.013 CommandandControl:WebProtocols T1071.001 CommandandControl:Fast FluxDNS T1568.001 13 CTARU20241205 Rec |  |  | 不明 | 不明 | 中 | `source--gamaredon--56ce9c37d34fb725`, `source--gamaredon--daa9dc266e370995` |
| Stealth | T1070 | Indicator Removal | coded scripts, for instance inserting junk code T1140 Deobfuscate/Decode Files or Information Group uses XOR method to decode information from payloads T1070 .004 Indicator Removal on Host: File Deletion Scripts can delete files used during an cyber attack T1112 Modify Registry Actively changing registry security settings for VBA macro HKCU\Software\Microsoft\Office\<versio n>\<product>\Security\VBAWarnings and |  |  | 不明 | 不明 | 中 | `source--gamaredon--9d4f2351eb5fd5c0` |
| Stealth | T1070.004 | File Deletion | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Command And Control | T1071 | Application Layer Protocol | 47 Data from Information Repositories T1213 Obfuscated Files or Information T1083 Query Registry T1012 Software Discovery T1518 Application Layer Protocol T1071 Exfiltration Over C2 Channel T1041 Modify Registry T1112 |  |  | 不明 | 不明 | 中 | `source--gamaredon--43ece8b760fd4f72` |
| Command And Control | T1071.001 | Web Protocols | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--56ce9c37d34fb725`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | ions from mapped network drives. T1025 Data from Removable Media PteroPSDoor exfiltrates files with specific file extensions from connected USB drives. T1074.001 Data Staged: Local Data Stagin g PteroPSDoor stages files prior to exfiltration. T1113 Screen Capture PteroScreen captures and exfiltrates screenshots. |  |  | 不明 | 不明 | 中 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995` |
| Lateral Movement | T1080 | Taint Shared Content | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--9d4f2351eb5fd5c0`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--43ece8b760fd4f72`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Command And Control | T1090 | Proxy | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Command And Control | T1090.003 | Multi-hop Proxy | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Lateral Movement | T1091 | Replication Through Removable Media | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--9d4f2351eb5fd5c0`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Command And Control | T1095 | Non-Application Layer Protocol | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Command And Control | T1102 | Web Service | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102.001 | Dead Drop Resolver | Non-Application Layer Protocol PteroPShell uses the TCP protocol for C&C communication. T1090 Proxy PteroSocks serves as a reverse SOCKS proxy server. T1102.001 Web Service: Dead Drop Resolver PteroPSLoad obtains its C&C IP address from the telegra.ph service. Exfiltration T1041 Exfiltration Over C2 Channel PteroPSDoor exfiltrates files over the C&C channel. T1567.002 Exfiltration Over Web Service: Exfiltration to Clo |  |  | 不明 | 不明 | 中 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995` |
| Command And Control | T1102.002 | Bidirectional Communication | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102.003 | One-Way Communication | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--9d4f2351eb5fd5c0`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Execution | T1106 | Native API | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--9d4f2351eb5fd5c0`, `source--mitre-attack-19-1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--43ece8b760fd4f72`, `source--gamaredon--9d4f2351eb5fd5c0`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Collection | T1113 | Screen Capture | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--9d4f2351eb5fd5c0`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Collection | T1119 | Automated Collection | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--9d4f2351eb5fd5c0`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Discovery | T1120 | Peripheral Device Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--9d4f2351eb5fd5c0`, `source--mitre-attack-19-1` |
| Command And Control | T1132.001 | Standard Encoding | escription Command and Control T1071.001 Application Layer Protocol: Web Protocols Gamaredon uses HTTP and HTTPS protocols for C&C communication. T1132.001 Data Encoding: Standard Encoding PteroCookie uses base64 to encode data prior to exfiltration. T1568.001 Dynamic Resolution: Fast Flux DNS Gamaredon uses fast flux DNS for its C&C infrastructure. T1008 Fallback Channels PteroPSLoad obtains the C&C IP address from a |  |  | 不明 | 不明 | 中 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995` |
| Persistence | T1137 | Office Application Startup | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--9d4f2351eb5fd5c0`, `source--mitre-attack-19-1` |
| Persistence | T1137.001 | Office Template Macros | 001 Boot or Logon Initialization Scripts: Logon Script (Windows) PteroSand achieves persistence by setting the UserInitMprLogonScript regist ry key . T1137.001 Office Application Startup: Office Template Macros PteroTemplate inserts a VBA macro into the Normal.dotm template to achiev e persistence. T1053.005 Scheduled Task/Job: Scheduled Task PteroPSLoad creates a scheduled task for persistence. Defense Evasion T1140 D |  |  | 不明 | 不明 | 中 | `source--gamaredon--0512c893b55f399d` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--9d4f2351eb5fd5c0`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Execution, Persistence, Stealth | T1197 | BITS Jobs | itMprLogonScript registry value. T1053.005 Scheduled Task/Job: Scheduled Task Various Gamaredon tools create scheduled tasks for persistence. Stealth T1197 BITS Jobs PteroPSDoor downloads Tor using BITS. T1140 Deobfuscate/Decode Files or Information Various Gamaredon tools use base64 to decode downloaded payloads. T1480.001 Execution Guardrails: Environmental Keying Various Gamaredon tools use the volume serial number |  |  | 不明 | 不明 | 中 | `source--gamaredon--daa9dc266e370995` |
| Execution | T1203 | Exploitation for Client Execution | payloads. T1059.007 Command and Scripting Interpreter: JavaScript/JScript PteroLNK drops malicious LNK files that use JavaScript to execute payloads. T1203 Exploitation for Client Execution Gamaredon exploits the RCE vulnerability CVE-2025-8088 for execution. |  |  | 不明 | 不明 | 中 | `source--gamaredon--daa9dc266e370995` |
| Execution | T1204 | User Execution | ion: Compon ent Object Model Group embeds macros into documents T1106 Native API Scripts has used CreateProcess to launch additional malicious components T1204 .001 User Execution: Malicious Link Group uses technics to encourage users to click on malicious links from phishing emails T1204 .002 User Execution: Malicious File Group uses technics to encourage users to click on malicious Office attachments or archives Persiste |  |  | 不明 | 不明 | 中 | `source--gamaredon--9d4f2351eb5fd5c0` |
| Execution | T1204.001 | Malicious Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--56ce9c37d34fb725`, `source--gamaredon--a0d52e16421d8b11`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Collection | T1213 | Data from Information Repositories | fostealer 14 MITRE ATT&CK Technique Name Technique ID Phishing T1566 Boot Or Logon Autostart Execution T1547 Data from Information Repositories T1213 Obfuscated Files or Information T1083 Query Registry T1012 Software Discovery T1518 Application Layer Protocol T1071 Exfiltration Over C2 Channel T1041 Modify Registry T1112 |  |  | 不明 | 不明 | 中 | `source--gamaredon--43ece8b760fd4f72` |
| Stealth | T1218 | System Binary Proxy Execution | Sandbox Evasion Malware pings for DNS servers and checks for launched processes. Also try to identify sandbox name and compare it with hardcoded namelist T1218 .011 Signed Binary Proxy Execution: Rundll32 Malware has used rundll32 to launch additional malicious components Credential Access T1003 Credential Dumping Mimikatz on numerous PC was executed Discovery T1082 System Information Discovery During cyber attack first sta |  |  | 不明 | 不明 | 中 | `source--gamaredon--9d4f2351eb5fd5c0` |
| Stealth | T1218.005 | Mshta | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--a0d52e16421d8b11`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Stealth | T1218.011 | Rundll32 | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Command And Control | T1219 | Remote Access Tools | cuments with certain extentions Command and Control T1105 Ingress Tool Transfer Malware has capabilities of downloading and executing additional payloads T1219 Remote Access Tools RMS and UltraVNC software were used Exfiltration T1041 Exfiltration Over C2 Channel Scripts transfer collected data to C2 |  |  | 不明 | 不明 | 中 | `source--gamaredon--9d4f2351eb5fd5c0` |
| Stealth | T1221 | Template Injection | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--9d4f2351eb5fd5c0`, `source--gamaredon--a0d52e16421d8b11`, `source--mitre-attack-19-1` |
| Stealth | T1480 | Execution Guardrails | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1480.001 | Environmental Keying | 50 Cyberespionage the Gamaredon way: Analysis of toolset used to spy on Ukraine in 2022 and 2023 Tactic ID Name Description T1480.001 Execution Guardrails: Environmental Keying PteroX uses the volume serial number from a compromised system as an XOR key for payloads. Credential Access T1555.003 Credentials from Password Stores: Credentials from Web Browsers PteroSteal gathers and exfiltrates |  |  | 不明 | 不明 | 中 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995` |
| Stealth | T1480.002 | Mutual Exclusion | 1 Execution Guardrails: Environmental Keying Various Gamaredon tools use the volume serial number from a compromised system as an XOR key for payloads. T1480.002 Execution Guardrails: Mutual Exclusion Various Gamaredon tools create mutexes to prevent duplicate execution. T1564.001 Hide Artifacts: Hidden Files and Directories Various Gamaredon tools create hidden files. |  |  | 不明 | 不明 | 中 | `source--gamaredon--daa9dc266e370995` |
| Impact | T1491.001 | Internal Defacement | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery, Stealth | T1497 | Virtualization/Sandbox Evasion | mes mimicking common system services or drivers T1221 Template Injection DOCX files contain a request body to download malicious DOT document templates T1497 .002 Virtualization/Sandbox Evasion Malware pings for DNS servers and checks for launched processes. Also try to identify sandbox name and compare it with hardcoded namelist T1218 .011 Signed Binary Proxy Execution: Rundll32 Malware has used rundll32 to launch additiona |  |  | 不明 | 不明 | 中 | `source--gamaredon--9d4f2351eb5fd5c0` |
| Discovery, Stealth | T1497.001 | System Checks | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518 | Software Discovery | t Or Logon Autostart Execution T1547 Data from Information Repositories T1213 Obfuscated Files or Information T1083 Query Registry T1012 Software Discovery T1518 Application Layer Protocol T1071 Exfiltration Over C2 Channel T1041 Modify Registry T1112 |  |  | 不明 | 不明 | 中 | `source--gamaredon--43ece8b760fd4f72` |
| Discovery | T1518.001 | Security Software Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Lateral Movement | T1534 | Internal Spearphishing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--9d4f2351eb5fd5c0`, `source--mitre-attack-19-1` |
| Credential Access | T1539 | Steal Web Session Cookie | T1555.003 Credentials from Password Stores: Credentials from Web Browsers PteroSteal gathers and exfiltrates credentials stored by various browsers. T1539 Steal Web Session Cookie PteroCookie gathers and exfiltrates cookies stored by various browsers. T1552.002 Unsecured Credentials: Credentials in Registry PteroSteal gathers and exfiltrates Outlook credentials stored in the registry. Discovery T1083 File and Directo |  |  | 不明 | 不明 | 中 | `source--gamaredon--0512c893b55f399d` |
| Persistence, Privilege Escalation | T1547 | Boot or Logon Autostart Execution | Technical Analysis of the Armageddon's Infostealer 14 MITRE ATT&CK Technique Name Technique ID Phishing T1566 Boot Or Logon Autostart Execution T1547 Data from Information Repositories T1213 Obfuscated Files or Information T1083 Query Registry T1012 Software Discovery T1518 Application Layer Protocol T1071 Exfiltration Over C2 Channel T1041 Modify Registry T1112 |  |  | 不明 | 不明 | 中 | `source--gamaredon--43ece8b760fd4f72`, `source--gamaredon--9d4f2351eb5fd5c0` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--56ce9c37d34fb725`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.009 | Shortcut Modification | tostart Execution: Registry Run Keys / Startup Folder Various Gamaredon tools use the HKCU Run or RunOnce key, or the Startup folder for persistence. T1547.009 Boot or Logon Autostart Execution: Shortcut Modification PteroBox creates a LNK file in the Startup folder to ensure persistence. T1037.001 Boot or Logon Initialization Scripts: Logon Script (Windows) PteroPaste and PteroPSLoad achieve persistence by setting th |  |  | 不明 | 不明 | 中 | `source--gamaredon--daa9dc266e370995` |
| Credential Access | T1552.002 | Credentials in Registry | iltrates credentials stored by various browsers. T1539 Steal Web Session Cookie PteroCookie gathers and exfiltrates cookies stored by various browsers. T1552.002 Unsecured Credentials: Credentials in Registry PteroSteal gathers and exfiltrates Outlook credentials stored in the registry. Discovery T1083 File and Directory Discovery PteroPSDoor searches for files with specific file extensions. T1518.001 Softwa re Discovery: |  |  | 不明 | 不明 | 中 | `source--gamaredon--0512c893b55f399d` |
| Credential Access | T1555.003 | Credentials from Web Browsers | ecution Guardrails: Environmental Keying PteroX uses the volume serial number from a compromised system as an XOR key for payloads. Credential Access T1555.003 Credentials from Password Stores: Credentials from Web Browsers PteroSteal gathers and exfiltrates credentials stored by various browsers. T1539 Steal Web Session Cookie PteroCookie gathers and exfiltrates cookies stored by various browsers. T1552.002 Unsecured |  |  | 不明 | 不明 | 中 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995` |
| Execution | T1559 | Inter-Process Communication | oaded tasklist T1047 WMI Group uses WMI commands in code to retrieve system information T1059 Command-Line Interface Group executes cmd scripts in system T1559 .001 Inter-Process Communication: Compon ent Object Model Group embeds macros into documents T1106 Native API Scripts has used CreateProcess to launch additional malicious components T1204 .001 User Execution: Malicious Link Group uses technics to encourage users to |  |  | 不明 | 不明 | 中 | `source--gamaredon--9d4f2351eb5fd5c0` |
| Execution | T1559.001 | Component Object Model | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Collection | T1560.002 | Archive via Library | 38 Gamaredon in 2025: Leveraging tunnels, workers, dead drops, and new alliances Tactic ID Name Description Collection T1560.002 Archive Collected Data: Archive via Library PteroGram packs files into a ZIP archive prior to exfiltration. T1119 Automated Collection PteroBox, PteroPSDoor, and PteroVDoor periodically search for files with specific file extensions. T1005 Data from Local System |  |  | 不明 | 不明 | 中 | `source--gamaredon--daa9dc266e370995` |
| Impact | T1561.001 | Disk Content Wipe | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Uncategorized | T1562.001 | MITRE ATT&CK T1562.001 | ed to spy on Ukraine in 2022 and 2023 Tactic ID Name Description T1564.001 Hide Artifacts: Hidden Files and Directories PteroLNK creates hidden files. T1562.001 Impair Defenses: Disable or Modify Tools PteroSocks disables AMSI by calling the method AmsiUtils.Uninitialize . T1070.004 Indicator Removal: File Deletion PteroPSDoor deletes staged files after successful exfiltration. T1036.004 Masquerading: Masquerade Task or |  |  | 不明 | 不明 | 中 | `source--gamaredon--0512c893b55f399d` |
| Stealth | T1564.001 | Hidden Files and Directories | 49 Cyberespionage the Gamaredon way: Analysis of toolset used to spy on Ukraine in 2022 and 2023 Tactic ID Name Description T1564.001 Hide Artifacts: Hidden Files and Directories PteroLNK creates hidden files. T1562.001 Impair Defenses: Disable or Modify Tools PteroSocks disables AMSI by calling the method AmsiUtils.Uninitialize . T1070.004 Indicator Removal: File Deletion PteroPSDoor deletes sta |  |  | 不明 | 不明 | 中 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995` |
| Stealth | T1564.003 | Hidden Window | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Stealth | T1564.004 | NTFS File Attributes | iances Tactic ID Name Description T1564.003 Hide Artifacts: Hidden Window Various Gamaredon tools spawn PowerShell processes with hidden windows. T1564.004 Hide Artifacts: NTFS File Attributes Various Gamaredon tools use alternate data streams to hide themselves and their C&C servers. T1070.004 Indicator Removal: File Deletion PteroBox, PteroPSDoor, and PteroVDoor delete staged files after successful exfiltration. T |  |  | 不明 | 不明 | 中 | `source--gamaredon--daa9dc266e370995` |
| Initial Access | T1566 | Phishing | Cybergun: Technical Analysis of the Armageddon's Infostealer 14 MITRE ATT&CK Technique Name Technique ID Phishing T1566 Boot Or Logon Autostart Execution T1547 Data from Information Repositories T1213 Obfuscated Files or Information T1083 Query Registry T1012 Software Discovery T1518 Application Layer Protocol T1071 Exfiltration Over C2 Channel T1041 Modify Registry T1112 |  |  | 不明 | 不明 | 中 | `source--gamaredon--43ece8b760fd4f72`, `source--gamaredon--9d4f2351eb5fd5c0` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--56ce9c37d34fb725`, `source--gamaredon--a0d52e16421d8b11`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | its own C&C server s. Initial Access T1566.001 Phishing: Spearphishing Attachment Gamaredon sends spearphishing emails with malicious attachments. T1566.002 Phishing: Spearphishing Link Gamaredon sends spearphishing emails with malicious links. Execution T1059.001 Command and Scripting Interpreter: PowerShell Gamaredon uses PowerShell to execute payloads. T1059.003 Command and Scripting Interpreter: Windows Comm |  |  | 不明 | 不明 | 中 | `source--gamaredon--daa9dc266e370995` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | its C&C IP address from the telegra.ph service. Exfiltration T1041 Exfiltration Over C2 Channel PteroPSDoor exfiltrates files over the C&C channel. T1567.002 Exfiltration Over Web Service: Exfiltration to Cloud Storage PteroClone exfiltrates data to the MEGA cloud storage. |  |  | 不明 | 不明 | 中 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995` |
| Command And Control | T1568 | Dynamic Resolution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1568.001 | Fast Flux DNS | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--56ce9c37d34fb725`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Command And Control | T1571 | Non-Standard Port | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Command And Control | T1572 | Protocol Tunneling | yer Protocol PteroPShell uses TCP for C&C communication. T1571 Non-Standard Port PteroPShell uses nonstandard ports for connecting to its C&C server. T1572 Protocol Tunneling Various Gamaredon tools use DoH to resolve C&C IP addresses. T1090 Proxy PteroSocks serves as a reverse SOCKS proxy server. T1102.001 Web Service: Dead Drop Resolver Various Gamaredon tools can retrieve C&C servers from third -party services, such |  |  | 不明 | 不明 | 中 | `source--gamaredon--daa9dc266e370995` |
| Command And Control | T1573.001 | Symmetric Cryptography | base64 to encode data prior to exfiltration. T1568.001 Dynamic Resolution: Fast Flux DNS Gamaredon can use fast flux DNS for its C&C infrastructure. T1573.001 Encrypted Channel: Symmetric Cryptography Gamaredon uses XOR and 3DES to encrypt payloads. T1573.002 Encrypted Channel: Asymmetric Cryptography Gamaredon uses RSA to encrypt FQDNs of C&C servers that are then staged on dead - drop services . T1008 Fallback Chann |  |  | 不明 | 不明 | 中 | `source--gamaredon--daa9dc266e370995` |
| Command And Control | T1573.002 | Asymmetric Cryptography | n use fast flux DNS for its C&C infrastructure. T1573.001 Encrypted Channel: Symmetric Cryptography Gamaredon uses XOR and 3DES to encrypt payloads. T1573.002 Encrypted Channel: Asymmetric Cryptography Gamaredon uses RSA to encrypt FQDNs of C&C servers that are then staged on dead - drop services . T1008 Fallback Channels Various Gamaredon tools use multiple fallback methods for communication with C&C servers. T1665 Hid |  |  | 不明 | 不明 | 中 | `source--gamaredon--daa9dc266e370995` |
| Resource Development | T1583.001 | Domains | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Resource Development | T1583.003 | Virtual Private Server | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995`, `source--mitre-attack-19-1` |
| Resource Development | T1583.006 | Web Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.007 | Serverless | n registers domains for its C&C servers. T1583.003 Acquire Infrastructure: Virtual Private Server Gamaredon rents servers for its C&C infrastructure. T1583.007 Acquire Infrastructure: Serverless Gamaredon hides its C&C infrastructure behind Cloudflare w orkers. T1587.001 Develop Capabilities: Malware Gamaredon develops its own custom malware. T1588.006 Obtain Capabilities: Vulnerabilities Gamaredon weaponizes the RCE |  |  | 不明 | 不明 | 中 | `source--gamaredon--daa9dc266e370995` |
| Resource Development | T1587.001 | Malware | register s domains for its C&C servers. T1583.003 Acquire Infrastructure: Virtual Private Server Gamaredon rent s servers for its C&C infrastructure. T1587.001 Develop Capabilities: Malware Gamaredon develop s its own custom malware. T1588.002 Obtain Capabilities: Tool Gamaredon use s various open -source tools like ReVBShell and Cloudflare Tunnel client. Initial Access T1566.001 Phishing: Spearphishing Attachment |  |  | 不明 | 不明 | 中 | `source--gamaredon--0512c893b55f399d`, `source--gamaredon--daa9dc266e370995` |
| Resource Development | T1587.003 | Digital Certificates | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--gamaredon--0512c893b55f399d`, `source--mitre-attack-19-1` |
| Resource Development | T1588.006 | Vulnerabilities | Gamaredon hides its C&C infrastructure behind Cloudflare w orkers. T1587.001 Develop Capabilities: Malware Gamaredon develops its own custom malware. T1588.006 Obtain Capabilities: Vulnerabilities Gamaredon weaponizes the RCE vulnerability CVE-2025-8088 for initial access. T1608.002 Stage Capabilities: Upload Tool Gamaredon staged Tor on the Filemail file - hosting service, and rclone on its own C&C server s. Initial A |  |  | 不明 | 不明 | 中 | `source--gamaredon--daa9dc266e370995` |
| Resource Development | T1608.001 | Upload Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.002 | Upload Tool | its own custom malware. T1588.006 Obtain Capabilities: Vulnerabilities Gamaredon weaponizes the RCE vulnerability CVE-2025-8088 for initial access. T1608.002 Stage Capabilities: Upload Tool Gamaredon staged Tor on the Filemail file - hosting service, and rclone on its own C&C server s. Initial Access T1566.001 Phishing: Spearphishing Attachment Gamaredon sends spearphishing emails with malicious attachments. T1566. |  |  | 不明 | 不明 | 中 | `source--gamaredon--daa9dc266e370995` |
| Stealth | T1620 | Reflective Code Loading | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1665 | Hide Infrastructure | then staged on dead - drop services . T1008 Fallback Channels Various Gamaredon tools use multiple fallback methods for communication with C&C servers. T1665 Hide Infrastructure Gamaredon uses various tunnel and worker services to hide its C&C infrastructure. |  |  | 不明 | 不明 | 中 | `source--gamaredon--daa9dc266e370995` |
| Stealth | T1684.001 | Impersonation | packed in ZIP and RAR archives. T1027.016 Obfuscated Files or Information: Junk Code Insertion Gamaredon inserts junk code into its malicious tools. T1684.001 Social Engineering: Impersonation Gamaredon sends spearphishing emails impersonating Ukrainian governmental entities. T1684.002 Social Engineering: Email Spoofing Gamaredon spoofs senders’ email addresses in its spearphishing campaigns. T1218.005 Signed Binary Prox |  |  | 不明 | 不明 | 中 | `source--gamaredon--daa9dc266e370995` |
| Stealth | T1684.002 | Email Spoofing | its malicious tools. T1684.001 Social Engineering: Impersonation Gamaredon sends spearphishing emails impersonating Ukrainian governmental entities. T1684.002 Social Engineering: Email Spoofing Gamaredon spoofs senders’ email addresses in its spearphishing campaigns. T1218.005 Signed Binary Proxy Execution: Mshta Gamaredon uses mshta.exe to execute HTA files. T1218.011 Signed Binary Proxy Execution: Rundll32 LNK files |  |  | 不明 | 不明 | 中 | `source--gamaredon--daa9dc266e370995` |
| Defense Impairment | T1685 | Disable or Modify Tools | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 1688件
- IOC観測: 1751件
- 複数攻撃で観測: 0件
- 要レビュー候補: 53件
- 非IOC artifact観測: 532件（`artifacts.csv`）

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
| source--daily-f9666a37c61d10f83b24 | FSBのマトリョーシカ #1/3：展開され続けるGamaredonの贈り物――GammaPhishとGammaWorm | blog.sekoia.io | 2026-06-03 | https://blog.sekoia.io/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm/ | osint-report | TLP:CLEAR | 中 |
| source--gamaredon--0512c893b55f399d | cyberespionage gamaredon way |  | 不明 | Gamaredon/cyberespionage-gamaredon-way.pdf | report | TLP:CLEAR | 中 |
| source--gamaredon--24d0ac8621d42b62 | README |  | 不明 | Gamaredon/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--gamaredon--43ece8b760fd4f72 | Cybergun Technical Analysis of the Armageddons Infostealer |  | 不明 | Gamaredon/Cybergun_Technical_Analysis_of_the_Armageddons_Infostealer.pdf | report | TLP:CLEAR | 中 |
| source--gamaredon--56ce9c37d34fb725 | BlueAlpha Abuses Cloudflare Tunneling Service for GammaDrop Staging Infrastructure |  | 不明 | Gamaredon/BlueAlpha Abuses Cloudflare Tunneling Service for GammaDrop Staging Infrastructure.pdf | report | TLP:CLEAR | 中 |
| source--gamaredon--68bb036eb943d265 | Gamaredon202102 ioc1000+ |  | 2021-02 | Gamaredon/Gamaredon202102_ioc1000+.csv | structured-data | TLP:CLEAR | 中 |
| source--gamaredon--9d4f2351eb5fd5c0 | Technical report Armagedon |  | 不明 | Gamaredon/Technical report Armagedon.pdf | report | TLP:CLEAR | 中 |
| source--gamaredon--a0d52e16421d8b11 | Beyond Bullets and Bombs An Examination of Armageddon Groups Cyber |  | 不明 | Gamaredon/Beyond_Bullets_and_Bombs_An_Examination_of_Armageddon_Groups_Cyber.pdf | report | TLP:CLEAR | 中 |
| source--gamaredon--b32b75e3cedfdb37 | Platinum feature article   Targeted attacks in South and Southeast Asia April 2016 |  | 2016 | Gamaredon/Platinum feature article - Targeted attacks in South and Southeast Asia April 2016.pdf | report | TLP:CLEAR | 中 |
| source--gamaredon--daa9dc266e370995 | gamaredon in 2025 |  | 2025 | Gamaredon/gamaredon-in-2025.pdf | report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
