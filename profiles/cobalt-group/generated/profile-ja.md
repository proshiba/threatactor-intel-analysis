# Cobalt Group 脅威アクタープロファイル

- プロファイルID: `actor--cobalt-group`
- 状態: draft
- 更新日時: 2026-07-29T15:36:10Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Cobalt Groupの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Cobalt Group**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Cobalt Gang | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Cobalt Spider | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| GOLD KINGSWOOD | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Magecart Group 4 | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

## 帰属

未評価

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: なし

## モチベーション

未評価

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Carbanak | related-to | The group has been known to target organizations in order to use their access to then compromise additional victims.(Citation: Talos Cobalt Group July 2018)(Citation: PTSecurity Cobalt Group Aug 2017)(Citation: PTSecurity Cobalt Dec 2016)(Citation: Group IB Cobalt Aug 2017)(Citation: Proofpoint Cobalt June 2017)(Citation: RiskIQ Cobalt Nov 2017)(Citation: RiskIQ Cobalt Jan 2018) Reporting indicates there may be links between [Cobalt Group](https://attack.mitre.org/groups/G0080) and both the malware [Carbanak](https://attack.mitre.org/software/S0030) and the group [Carbanak](https://attack.mitre.org/groups/G0008).(Citation: Europol Cobalt Mar 2018) | 中 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Cobalt Group](https://attack.mitre.org/groups/G0080) is a financially motivated threat group that has primarily targeted financial institutions since at least 2016. The group has conducted intrusions to steal money via targeting ATM systems, card processing, payment systems and SWIFT systems. [Cobalt Group](https://attack.mitre.org/groups/G0080) has mainly targeted banks in Eastern Europe, Central Asia, and Southeast Asia. One of the alleged leaders was arrested in Spain in early 2018, but the group still appears to be active. The group has been known to target organizations in order to use their access to then compromise additional victims.(Citation: Talos Cobalt Group July 2018)(Citation: PTSecurity Cobalt Group Aug 2017)(Citation: PTSecurity Cobalt Dec 2016)(Citation: Group IB Cobalt Aug 2017)(Citation: Proofpoint Cobalt June 2017)(Citation: RiskIQ Cobalt Nov 2017)(Citation: RiskIQ Cobalt Jan 2018) Reporting indicates there may be links between [Cobalt Group](https://attack.mitre.org/groups/G0080) and both the malware [Carbanak](https://attack.mitre.org/software/S0030) and the group [Carbanak](https://attack.mitre.org/groups/G0008).(Citation: Europol Cobalt Mar 2018) |
| Capability | SpicyOmelette, Cobalt Strike, More_eggs, Mimikatz, SDelete, PsExec |
| Infrastructure |  |
| Victim | Point of Sale |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Cobalt Group | canonical-name | 高 | Russia | https://www.ptsecurity.com/upload/corporate/ww-en/analytics/Cobalt-2017-eng.pdf<br>https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-september-cobalt-spider/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Cobalt+Group&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Cobalt | canonical-name | 高 |  | https://www.helpnetsecurity.com/2016/11/22/cobalt-hackers-synchronized-atm-heists/<br>https://www.bleepingcomputer.com/news/security/cobalt-hacking-group-tests-banks-in-russia-and-romania/<br>https://www.secureworks.com/blog/cybercriminals-increasingly-trying-to-ensnare-the-big-financial-fish |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Cobalt Group - G0080 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0080<br>https://blog.morphisec.com/cobalt-gang-2.0<br>https://blog.talosintelligence.com/2018/07/multiple-cobalt-personality-disorder.html |
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
| malware--spicyomelette | SpicyOmelette | [SpicyOmelette](https://attack.mitre.org/software/S0646) is a JavaScript based remote access tool that has been used by [Cobalt Group](https://attack.mitre.org/groups/G0080) since at least 2018.(Citation: Secureworks GOLD KINGSWOOD September 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--cobalt-strike | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) is a commercial, full-featured, remote access tool that bills itself as “adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors”. Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.(Citation: cobaltstrike manual)<br><br>In addition to its own capabilities, [Cobalt Strike](https://attack.mitre.org/software/S0154) leverages the capabilities of other well-known tools such as Metasploit and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: cobaltstrike manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--more-eggs | More_eggs | [More_eggs](https://attack.mitre.org/software/S0284) is a JScript backdoor used by [Cobalt Group](https://attack.mitre.org/groups/G0080) and [FIN6](https://attack.mitre.org/groups/G0037). Its name was given based on the variable "More_eggs" being present in its code. There are at least two different versions of the backdoor being used, version 2.0 and version 4.4. (Citation: Talos Cobalt Group July 2018)(Citation: Security Intelligence More Eggs Aug 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--sdelete | SDelete | [SDelete](https://attack.mitre.org/software/S0195) is an application that securely deletes data in a way that makes it unrecoverable. It is part of the Microsoft Sysinternals suite of tools. (Citation: Microsoft SDelete July 2016) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
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
| sectors | 金融 | [Cobalt Group](https://attack.mitre.org/groups/G0080) is a financially motivated threat group that has primarily targeted financial institutions since at least 2016. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 未評価

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Lateral Movement | T1021.001 | Remote Desktop Protocol | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used Remote Desktop Protocol to conduct lateral movement.(Citation: Group IB Cobalt Aug 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.010 | Command Obfuscation | [Cobalt Group](https://attack.mitre.org/groups/G0080) obfuscated several scriptlets and code used on the victim’s machine, including through use of XOR and RC4.(Citation: Talos Cobalt Group July 2018)(Citation: Morphisec Cobalt Gang Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1037.001 | Logon Script (Windows) | [Cobalt Group](https://attack.mitre.org/groups/G0080) has added persistence by registering the file name for the next stage malware under <code>HKCU\Environment\UserInitMprLogonScript</code>.(Citation: Morphisec Cobalt Gang Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1046 | Network Service Discovery | [Cobalt Group](https://attack.mitre.org/groups/G0080) leveraged an open-source tool called SoftPerfect Network Scanner to perform network scanning.(Citation: PTSecurity Cobalt Group Aug 2017)(Citation: PTSecurity Cobalt Dec 2016)(Citation: Group IB Cobalt Aug 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [Cobalt Group](https://attack.mitre.org/groups/G0080) has created Windows tasks to establish persistence.(Citation: Group IB Cobalt Aug 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055 | Process Injection | [Cobalt Group](https://attack.mitre.org/groups/G0080) has injected code into trusted processes.(Citation: Group IB Cobalt Aug 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used powershell.exe to download and execute scripts.(Citation: Talos Cobalt Group July 2018)(Citation: PTSecurity Cobalt Group Aug 2017)(Citation: PTSecurity Cobalt Dec 2016)(Citation: Group IB Cobalt Aug 2017)(Citation: RiskIQ Cobalt Jan 2018)(Citation: TrendMicro Cobalt Group Nov 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used a JavaScript backdoor that is capable of launching cmd.exe to execute shell commands.(Citation: Morphisec Cobalt Gang Oct 2018) The group has used an exploit toolkit known as Threadkit that launches .bat files.(Citation: Talos Cobalt Group July 2018)(Citation: PTSecurity Cobalt Group Aug 2017)(Citation: Group IB Cobalt Aug 2017)(Citation: Morphisec Cobalt Gang Oct 2018)(Citation: Unit 42 Cobalt Gang Oct 2018)(Citation: TrendMicro Cobalt Group Nov 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | [Cobalt Group](https://attack.mitre.org/groups/G0080) has sent Word OLE compound documents with malicious obfuscated VBA macros that will run upon user execution.(Citation: Talos Cobalt Group July 2018)(Citation: PTSecurity Cobalt Group Aug 2017)(Citation: Group IB Cobalt Aug 2017)(Citation: Morphisec Cobalt Gang Oct 2018)(Citation: Unit 42 Cobalt Gang Oct 2018)(Citation: TrendMicro Cobalt Group Nov 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.007 | JavaScript | [Cobalt Group](https://attack.mitre.org/groups/G0080) has executed JavaScript scriptlets on the victim's machine.(Citation: Talos Cobalt Group July 2018)(Citation: PTSecurity Cobalt Group Aug 2017)(Citation: Group IB Cobalt Aug 2017)(Citation: Morphisec Cobalt Gang Oct 2018)(Citation: Unit 42 Cobalt Gang Oct 2018)(Citation: TrendMicro Cobalt Group Nov 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1068 | Exploitation for Privilege Escalation | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used exploits to increase their levels of rights and privileges.(Citation: Group IB Cobalt Aug 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | [Cobalt Group](https://attack.mitre.org/groups/G0080) deleted the DLL dropper from the victim’s machine to cover their tracks.(Citation: Talos Cobalt Group July 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used HTTPS for C2.(Citation: Talos Cobalt Group July 2018)(Citation: PTSecurity Cobalt Dec 2016)(Citation: Group IB Cobalt Aug 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.004 | DNS | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used DNS tunneling for C2.(Citation: Talos Cobalt Group July 2018)(Citation: PTSecurity Cobalt Dec 2016)(Citation: Group IB Cobalt Aug 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used public sites such as github.com and sendspace.com to upload files and then download them to victim computers.(Citation: PTSecurity Cobalt Group Aug 2017)(Citation: PTSecurity Cobalt Dec 2016) The group's JavaScript backdoor is also capable of downloading files.(Citation: Morphisec Cobalt Gang Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1195.002 | Compromise Software Supply Chain | [Cobalt Group](https://attack.mitre.org/groups/G0080) has compromised legitimate web browser updates to deliver a backdoor. (Citation: Crowdstrike GTR2020 Mar 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | [Cobalt Group](https://attack.mitre.org/groups/G0080) had exploited multiple vulnerabilities for execution, including Microsoft’s Equation Editor (CVE-2017-11882), an Internet Explorer vulnerability (CVE-2018-8174), CVE-2017-8570, CVE-2017-0199, and CVE-2017-8759.(Citation: Talos Cobalt Group July 2018)(Citation: PTSecurity Cobalt Group Aug 2017)(Citation: PTSecurity Cobalt Dec 2016)(Citation: Proofpoint Cobalt June 2017)(Citation: RiskIQ Cobalt Nov 2017)(Citation: RiskIQ Cobalt Jan 2018)(Citation: Crowdstrike Global Threat Report Feb 2018)(Citation: TrendMicro Cobalt Group Nov 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | [Cobalt Group](https://attack.mitre.org/groups/G0080) has sent emails containing malicious links that require users to execute a file or macro to infect the victim machine.(Citation: Talos Cobalt Group July 2018)(Citation: Unit 42 Cobalt Gang Oct 2018)(Citation: Secureworks GOLD KINGSWOOD September 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [Cobalt Group](https://attack.mitre.org/groups/G0080) has sent emails containing malicious attachments that require users to execute a file or macro to infect the victim machine.(Citation: Talos Cobalt Group July 2018)(Citation: Unit 42 Cobalt Gang Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.003 | CMSTP | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used the command <code>cmstp.exe /s /ns C:\Users\ADMINI~W\AppData\Local\Temp\XKNqbpzl.txt</code> to bypass AppLocker and launch a malicious script.(Citation: Talos Cobalt Group July 2018)(Citation: Morphisec Cobalt Gang Oct 2018)(Citation: Unit 42 Cobalt Gang Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.008 | Odbcconf | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used <code>odbcconf</code> to proxy the execution of malicious DLL files.(Citation: TrendMicro Cobalt Group Nov 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.010 | Regsvr32 | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used regsvr32.exe to execute scripts.(Citation: Talos Cobalt Group July 2018)(Citation: Morphisec Cobalt Gang Oct 2018)(Citation: TrendMicro Cobalt Group Nov 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1219 | Remote Access Tools | [Cobalt Group](https://attack.mitre.org/groups/G0080) used the Ammyy Admin tool as well as TeamViewer for remote access, including to preserve remote access if a Cobalt Strike module was lost.(Citation: PTSecurity Cobalt Group Aug 2017)(Citation: PTSecurity Cobalt Dec 2016)(Citation: Group IB Cobalt Aug 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1220 | XSL Script Processing | [Cobalt Group](https://attack.mitre.org/groups/G0080) used msxsl.exe to bypass AppLocker and to invoke Jscript code from an XSL file.(Citation: Talos Cobalt Group July 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518.001 | Security Software Discovery | [Cobalt Group](https://attack.mitre.org/groups/G0080) used a JavaScript backdoor that is capable of collecting a list of the security solutions installed on the victim's machine.(Citation: Morphisec Cobalt Gang Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | [Cobalt Group](https://attack.mitre.org/groups/G0080) has created new services to establish persistence.(Citation: Group IB Cobalt Aug 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used Registry Run keys for persistence. The group has also set a Startup path to launch the PowerShell shell command and download Cobalt Strike.(Citation: Group IB Cobalt Aug 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1548.002 | Bypass User Account Control | [Cobalt Group](https://attack.mitre.org/groups/G0080) has bypassed UAC.(Citation: Group IB Cobalt Aug 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1559.002 | Dynamic Data Exchange | [Cobalt Group](https://attack.mitre.org/groups/G0080) has sent malicious Word OLE compound documents to victims.(Citation: Talos Cobalt Group July 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [Cobalt Group](https://attack.mitre.org/groups/G0080) has sent spearphishing emails with various attachment types to corporate and personal email accounts of victim organizations. Attachment types have included .rtf, .doc, .xls, archives containing LNK files, and password protected archives containing .exe and .scr executables.(Citation: Talos Cobalt Group July 2018)(Citation: PTSecurity Cobalt Group Aug 2017)(Citation: PTSecurity Cobalt Dec 2016)(Citation: Group IB Cobalt Aug 2017)(Citation: Proofpoint Cobalt June 2017)(Citation: RiskIQ Cobalt Nov 2017)(Citation: Unit 42 Cobalt Gang Oct 2018)(Citation: TrendMicro Cobalt Group Nov 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | [Cobalt Group](https://attack.mitre.org/groups/G0080) has sent emails with URLs pointing to malicious documents.(Citation: Talos Cobalt Group July 2018)(Citation: Secureworks GOLD KINGSWOOD September 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1572 | Protocol Tunneling | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used the Plink utility to create SSH tunnels.(Citation: Talos Cobalt Group July 2018)(Citation: PTSecurity Cobalt Dec 2016)(Citation: Group IB Cobalt Aug 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573.002 | Asymmetric Cryptography | [Cobalt Group](https://attack.mitre.org/groups/G0080) has used the Plink utility to create SSH tunnels.(Citation: Group IB Cobalt Aug 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [Cobalt Group](https://attack.mitre.org/groups/G0080) has obtained and used a variety of tools including [Mimikatz](https://attack.mitre.org/software/S0002), [PsExec](https://attack.mitre.org/software/S0029), [Cobalt Strike](https://attack.mitre.org/software/S0154), and [SDelete](https://attack.mitre.org/software/S0195).(Citation: PTSecurity Cobalt Dec 2016) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 36件（`artifacts.csv`）

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
| source--cobalt-group--4e131ed745481ff3 | cobalt group |  | 不明 | actor_profile/evidence/cobalt-group.csv | structured-data | TLP:CLEAR | 中 |
| source--cobalt-group--1d434afc0010be0c | hunting cobaltstrike beacons in the dark |  | 不明 | APT-hunting/hunting-cobaltstrike-beacons-in-the-dark.pdf | report | TLP:CLEAR | 中 |
| source--cobalt-group--e1cb42df05c50f1e | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--cobalt-group--48adda536c8c3784 | Unmasking VenomSpider Report Final |  | 不明 | International Strategic/Russia/GoldenChickens/Unmasking_VenomSpider_Report-Final.pdf | report | TLP:CLEAR | 中 |
| source--cobalt-group--d1f4a76ebc5d2e0f | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--cobalt-group--44523b5be1bf986f | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--cobalt-group--3c7427ae4e64ae65 | PWC cyber threats 2019 retrospect |  | 2019 | summary/2020/PWC-cyber-threats-2019-retrospect.pdf | report | TLP:CLEAR | 中 |
| source--cobalt-group--facbdaa1c4d2c0fd | The CrowdStrike 2021 Global Threat Report |  | 2021 | summary/2021/The CrowdStrike 2021 Global Threat Report.pdf | report | TLP:CLEAR | 中 |
| source--cobalt-group--c3c5aa5679d505b2 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--cobalt-group--4ea9ba4467e47d57 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--cobalt-group--13dec3fa8632f475 | SixMap Research Energy Sector Exposure Assessment |  | 不明 | summary/2025/SixMap-Research_Energy-Sector-Exposure-Assessment.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
