# Konni 脅威アクタープロファイル

プロファイルID: `actor--konni`  
状態: draft  
更新日時: 2026-07-25T14:07:08Z  
構造バージョン: 1.0.0

## エグゼクティブサマリー

Konniの標準化プロファイル。リポジトリ内の専用資料7件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Konni**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

Aliasなし

## 帰属

未評価

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: なし

## モチベーション

未評価

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability |  |
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
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Opal Sleet | canonical-name | 高 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Opal Sleet | canonical-name | 高 | KP | https://nsfocusglobal.com/the-new-apt-group-darkcasino-and-the-global-surge-in-winrar-0-day-exploits/<br>https://paper.seebug.org/3031/<br>https://www.rewterz.com/rewterz-news/rewterz-threat-alert-konni-apt-group-active-iocs-11 |
| misp-microsoft-activity-group | Opal Sleet | canonical-name | 高 | KP, North Korea | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Kimsuky | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

未確認

### ツール

未確認

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

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1001 | Data Obfuscation | 1082 System Information Discovery T1083 File and Directory Discovery T1518 Software Discovery Collection T1005 Data from Local System Command and Control T1001 Data Obfuscation T1132.001 Data Encoding: Standard Encoding Exfiltration T1041 Exfiltration Over C2 Channel [표 18] MITRE ATT&CK, Tactics and Techniques 11 ATT&CK : The Adversarial Tactics, Techniques, and Common Knowledge |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53` |
| Collection | T1005 | Data from Local System | Configuration Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1518 Software Discovery Collection T1005 Data from Local System Command and Control T1001 Data Obfuscation T1132.001 Data Encoding: Standard Encoding Exfiltration T1041 Exfiltration Over C2 Channel [표 18] MITRE ATT&CK, Tactics and Techniques 11 ATT&CK : The Adv |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53` |
| Discovery | T1016 | System Network Configuration Discovery | Obfuscated Files or Information: Command Obfuscation T1036.007 Masquerading: Double File Extension T1140 Deobfuscate/Decode Files or Information Discovery T1016 System Network Configuration Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1518 Software Discovery Collection T1005 Data from Local System Command and Control T1001 Data Obfuscation T1132.001 Data Encoding: Stan |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53` |
| Stealth | T1027.001 | Binary Padding | Basic T1204.002 User Execution: Malicious File Persistence T1547.001 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder Defense Evasion T1027.001 Obfuscated Files or Information: Binary Padding T1027.010 Obfuscated Files or Information: Command Obfuscation T1036.007 Masquerading: Double File Extension T1140 Deobfuscate/Decode Files or Information Discovery T1016 System Network Configuration Discovery T1057 Process |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53` |
| Stealth | T1027.010 | Command Obfuscation | e T1547.001 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder Defense Evasion T1027.001 Obfuscated Files or Information: Binary Padding T1027.010 Obfuscated Files or Information: Command Obfuscation T1036.007 Masquerading: Double File Extension T1140 Deobfuscate/Decode Files or Information Discovery T1016 System Network Configuration Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File a |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53` |
| Stealth | T1036.007 | Double File Extension | / Startup Folder Defense Evasion T1027.001 Obfuscated Files or Information: Binary Padding T1027.010 Obfuscated Files or Information: Command Obfuscation T1036.007 Masquerading: Double File Extension T1140 Deobfuscate/Decode Files or Information Discovery T1016 System Network Configuration Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1518 Software Discovery Collection T100 |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | ware Discovery Collection T1005 Data from Local System Command and Control T1001 Data Obfuscation T1132.001 Data Encoding: Standard Encoding Exfiltration T1041 Exfiltration Over C2 Channel [표 18] MITRE ATT&CK, Tactics and Techniques 11 ATT&CK : The Adversarial Tactics, Techniques, and Common Knowledge 12 MITRE ATT&CK Software - KONNI |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53`, `source--konni--8c179de8de042c5a`, `source--konni--9f9859221e0eb3bc` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | 3 CommandandScriptingInterpreter:Windows CommandShell T1059.005 CommandandScriptingInterpreter:Visual Basic T1204.002 User Execution:Malicious File Persistence T1053.005 ScheduledTask/Job:ScheduledTask DefenseEvasion T1070.004 Indicator Removal:FileDeletionT1140 Deobfuscate/DecodeFiles or Information Discovery T1057 Process DiscoveryT1082 SystemInformationDiscoveryT1083 FileandDirectoryDiscoveryCollection T1119 AutomatedCollectionCommandand T107 |  |  | 不明 | 不明 | 中 | `source--konni--8c179de8de042c5a`, `source--konni--9f9859221e0eb3bc` |
| Discovery | T1057 | Process Discovery | scation T1036.007 Masquerading: Double File Extension T1140 Deobfuscate/Decode Files or Information Discovery T1016 System Network Configuration Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1518 Software Discovery Collection T1005 Data from Local System Command and Control T1001 Data Obfuscation T1132.001 Data Encoding: Standard Encoding Exfiltration T1041 Exfiltration |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53`, `source--konni--8c179de8de042c5a`, `source--konni--9f9859221e0eb3bc` |
| Execution | T1059.001 | PowerShell | cription Reconnaissance T1598.002 Phishing for Information: Spearphishing Attachment Initial Access T1566.001 Phishing: Spearphishing Attachment Execution T1059.001 Command and Scripting Interpreter: PowerShell T1059.003 Command and Scripting Interpreter: Windows Command Shell T1059.005 Command and Scripting Interpreter: Visual Basic T1204.002 User Execution: Malicious File Persistence T1547.001 Boot or Logon Autostart Execution: Regis |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53`, `source--konni--9f9859221e0eb3bc` |
| Execution | T1059.003 | Windows Command Shell | on: Spearphishing Attachment Initial Access T1566.001 Phishing: Spearphishing Attachment Execution T1059.001 Command and Scripting Interpreter: PowerShell T1059.003 Command and Scripting Interpreter: Windows Command Shell T1059.005 Command and Scripting Interpreter: Visual Basic T1204.002 User Execution: Malicious File Persistence T1547.001 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder Defense Evasion T1027.00 |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53`, `source--konni--8c179de8de042c5a`, `source--konni--9f9859221e0eb3bc` |
| Execution | T1059.005 | Visual Basic | arphishing Attachment Execution T1059.001 Command and Scripting Interpreter: PowerShell T1059.003 Command and Scripting Interpreter: Windows Command Shell T1059.005 Command and Scripting Interpreter: Visual Basic T1204.002 User Execution: Malicious File Persistence T1547.001 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder Defense Evasion T1027.001 Obfuscated Files or Information: Binary Padding T1027.010 Obfuscat |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53`, `source--konni--8c179de8de042c5a`, `source--konni--9f9859221e0eb3bc` |
| Stealth | T1070.004 | File Deletion | 59.005 CommandandScriptingInterpreter:Visual Basic T1204.002 User Execution:Malicious File Persistence T1053.005 ScheduledTask/Job:ScheduledTask DefenseEvasion T1070.004 Indicator Removal:FileDeletionT1140 Deobfuscate/DecodeFiles or Information Discovery T1057 Process DiscoveryT1082 SystemInformationDiscoveryT1083 FileandDirectoryDiscoveryCollection T1119 AutomatedCollectionCommandand T1071.001 ApplicationLayer Protocol: 10 Konni 9 https://attac |  |  | 不明 | 不明 | 中 | `source--konni--8c179de8de042c5a`, `source--konni--9f9859221e0eb3bc` |
| Command And Control | T1071 | Application Layer Protocol | eDeletion T1070.004SystemInformationDiscovery T1082FileandDirectoryDiscovery T1083ProcessDiscovery T1057ExfiltrationOverC2Channel T1041ApplicationLayerProtocol T1071 11 |  |  | 不明 | 不明 | 中 | `source--konni--8c179de8de042c5a` |
| Command And Control | T1071.001 | Web Protocols | s or Information Discovery T1057 Process DiscoveryT1082 SystemInformationDiscoveryT1083 FileandDirectoryDiscoveryCollection T1119 AutomatedCollectionCommandand T1071.001 ApplicationLayer Protocol: 10 Konni 9 https://attack.mitre.org/tactics/enterprise/ Genians SecurityCenter 46 |  |  | 不明 | 不明 | 中 | `source--konni--9f9859221e0eb3bc` |
| Discovery | T1082 | System Information Discovery | rading: Double File Extension T1140 Deobfuscate/Decode Files or Information Discovery T1016 System Network Configuration Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1518 Software Discovery Collection T1005 Data from Local System Command and Control T1001 Data Obfuscation T1132.001 Data Encoding: Standard Encoding Exfiltration T1041 Exfiltration Over C2 Channel [표 18] |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53`, `source--konni--8c179de8de042c5a`, `source--konni--9f9859221e0eb3bc` |
| Discovery | T1083 | File and Directory Discovery | Deobfuscate/Decode Files or Information Discovery T1016 System Network Configuration Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1518 Software Discovery Collection T1005 Data from Local System Command and Control T1001 Data Obfuscation T1132.001 Data Encoding: Standard Encoding Exfiltration T1041 Exfiltration Over C2 Channel [표 18] MITRE ATT&CK, Tactics and Techniques |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53`, `source--konni--8c179de8de042c5a`, `source--konni--9f9859221e0eb3bc` |
| Collection | T1119 | Automated Collection | DeletionT1140 Deobfuscate/DecodeFiles or Information Discovery T1057 Process DiscoveryT1082 SystemInformationDiscoveryT1083 FileandDirectoryDiscoveryCollection T1119 AutomatedCollectionCommandand T1071.001 ApplicationLayer Protocol: 10 Konni 9 https://attack.mitre.org/tactics/enterprise/ Genians SecurityCenter 46 |  |  | 不明 | 不明 | 中 | `source--konni--9f9859221e0eb3bc` |
| Command And Control | T1132.001 | Standard Encoding | Discovery T1083 File and Directory Discovery T1518 Software Discovery Collection T1005 Data from Local System Command and Control T1001 Data Obfuscation T1132.001 Data Encoding: Standard Encoding Exfiltration T1041 Exfiltration Over C2 Channel [표 18] MITRE ATT&CK, Tactics and Techniques 11 ATT&CK : The Adversarial Tactics, Techniques, and Common Knowledge 12 MITRE ATT&CK Software - K |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | bfuscated Files or Information: Binary Padding T1027.010 Obfuscated Files or Information: Command Obfuscation T1036.007 Masquerading: Double File Extension T1140 Deobfuscate/Decode Files or Information Discovery T1016 System Network Configuration Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1518 Software Discovery Collection T1005 Data from Local System Command and Cont |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53`, `source--konni--8c179de8de042c5a`, `source--konni--9f9859221e0eb3bc` |
| Execution | T1204.002 | Malicious File | ipting Interpreter: PowerShell T1059.003 Command and Scripting Interpreter: Windows Command Shell T1059.005 Command and Scripting Interpreter: Visual Basic T1204.002 User Execution: Malicious File Persistence T1547.001 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder Defense Evasion T1027.001 Obfuscated Files or Information: Binary Padding T1027.010 Obfuscated Files or Information: Command Obfuscation T1036.007 Ma |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53`, `source--konni--9f9859221e0eb3bc` |
| Discovery | T1518 | Software Discovery | tion Discovery T1016 System Network Configuration Discovery T1057 Process Discovery T1082 System Information Discovery T1083 File and Directory Discovery T1518 Software Discovery Collection T1005 Data from Local System Command and Control T1001 Data Obfuscation T1132.001 Data Encoding: Standard Encoding Exfiltration T1041 Exfiltration Over C2 Channel [표 18] MITRE ATT&CK, Tactics and Techniques |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | Scripting Interpreter: Windows Command Shell T1059.005 Command and Scripting Interpreter: Visual Basic T1204.002 User Execution: Malicious File Persistence T1547.001 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder Defense Evasion T1027.001 Obfuscated Files or Information: Binary Padding T1027.010 Obfuscated Files or Information: Command Obfuscation T1036.007 Masquerading: Double File Extension T1140 Deobfuscate/D |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53` |
| Collection | T1560 | Archive Collected Data | TheKonni APTChronicle: TracingTheir Intelligence-DrivenAttackChain ArchiveCollectedData T1560 Mitigations ● Regularlyeducateandtrainemployeesabout thedangersof spear-phishingattacks.Teachthemhowtorecognizephishingattempts, especiallythoseinvolvingmaliciouslinks. Encouragea"thinkbeforeyouclick" mentalitytoreducethechancesof fallingfor theseattacks.● Implement applicationw |  |  | 不明 | 不明 | 中 | `source--konni--8c179de8de042c5a` |
| Initial Access | T1566.001 | Spearphishing Attachment | Matrix - Konni12 Group Descriptions Tactic Technique Description Reconnaissance T1598.002 Phishing for Information: Spearphishing Attachment Initial Access T1566.001 Phishing: Spearphishing Attachment Execution T1059.001 Command and Scripting Interpreter: PowerShell T1059.003 Command and Scripting Interpreter: Windows Command Shell T1059.005 Command and Scripting Interpreter: Visual Basic T1204.002 User Execution: Malicious File Persi |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53` |
| Initial Access | T1566.002 | Spearphishing Link | ishingfor Information:SpearphishingLink ResourceDevelopment T1585.002 EstablishAccounts:Email Accounts T1585.003 EstablishAccounts:CloudAccounts Initial Access T1566.002 Phishing:SpearphishingLink T1566.003 Phishing:SpearphishingviaService Execution T1059.001 CommandandScriptingInterpreter:PowerShell T1059.003 CommandandScriptingInterpreter:Windows CommandShell T1059.005 CommandandScriptingInterpreter:Visual Basic T1204.002 User Execution:Malici |  |  | 不明 | 不明 | 中 | `source--konni--8c179de8de042c5a`, `source--konni--9f9859221e0eb3bc` |
| Initial Access | T1566.003 | Spearphishing via Service | nk ResourceDevelopment T1585.002 EstablishAccounts:Email Accounts T1585.003 EstablishAccounts:CloudAccounts Initial Access T1566.002 Phishing:SpearphishingLink T1566.003 Phishing:SpearphishingviaService Execution T1059.001 CommandandScriptingInterpreter:PowerShell T1059.003 CommandandScriptingInterpreter:Windows CommandShell T1059.005 CommandandScriptingInterpreter:Visual Basic T1204.002 User Execution:Malicious File Persistence T1053.005 Schedu |  |  | 不明 | 不明 | 中 | `source--konni--9f9859221e0eb3bc` |
| Resource Development | T1585.002 | Email Accounts | ue Description Reconnaissance T1598.002 Phishingfor Information:SpearphishingAttachment T1598.003 Phishingfor Information:SpearphishingLink ResourceDevelopment T1585.002 EstablishAccounts:Email Accounts T1585.003 EstablishAccounts:CloudAccounts Initial Access T1566.002 Phishing:SpearphishingLink T1566.003 Phishing:SpearphishingviaService Execution T1059.001 CommandandScriptingInterpreter:PowerShell T1059.003 CommandandScriptingInterpreter:Window |  |  | 不明 | 不明 | 中 | `source--konni--9f9859221e0eb3bc` |
| Resource Development | T1585.003 | Cloud Accounts | shingfor Information:SpearphishingAttachment T1598.003 Phishingfor Information:SpearphishingLink ResourceDevelopment T1585.002 EstablishAccounts:Email Accounts T1585.003 EstablishAccounts:CloudAccounts Initial Access T1566.002 Phishing:SpearphishingLink T1566.003 Phishing:SpearphishingviaService Execution T1059.001 CommandandScriptingInterpreter:PowerShell T1059.003 CommandandScriptingInterpreter:Windows CommandShell T1059.005 CommandandScriptin |  |  | 不明 | 不明 | 中 | `source--konni--9f9859221e0eb3bc` |
| Reconnaissance | T1598.002 | Spearphishing Attachment | 44 07. 공격 지표 (Indicator of Attack) a. MITRE ATT&CK11 Matrix - Konni12 Group Descriptions Tactic Technique Description Reconnaissance T1598.002 Phishing for Information: Spearphishing Attachment Initial Access T1566.001 Phishing: Spearphishing Attachment Execution T1059.001 Command and Scripting Interpreter: PowerShell T1059.003 Command and Scripting Interpreter: Windows Command Shell T1059.005 Command and Script |  |  | 不明 | 不明 | 中 | `source--konni--079e51a056632f53`, `source--konni--9f9859221e0eb3bc` |
| Reconnaissance | T1598.003 | Spearphishing Link | Matrix - MITREATT&CK Matrix- Konni GroupDescriptions 9 10 Tactic Technique Description Reconnaissance T1598.002 Phishingfor Information:SpearphishingAttachment T1598.003 Phishingfor Information:SpearphishingLink ResourceDevelopment T1585.002 EstablishAccounts:Email Accounts T1585.003 EstablishAccounts:CloudAccounts Initial Access T1566.002 Phishing:SpearphishingLink T1566.003 Phishing:SpearphishingviaService Execution T1059.001 CommandandScripti |  |  | 不明 | 不明 | 中 | `source--konni--9f9859221e0eb3bc` |

## IOC／artifact概要

- IOC値: 240件
- IOC観測: 340件
- 複数攻撃で観測: 0件
- 要レビュー候補: 55件
- 非IOC artifact観測: 289件（`artifacts.csv`）

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
| source--konni--079e51a056632f53 | 20230727 threat inteligence report Konni |  | 2023-07-27 | konni/20230727_threat_inteligence_report_Konni.pdf | report | TLP:CLEAR | 中 |
| source--konni--9f9859221e0eb3bc | 20230926 threat inteligence report konniapt |  | 2023-09-26 | konni/20230926_threat_inteligence_report_konniapt.pdf | report | TLP:CLEAR | 中 |
| source--konni--a7ca5a441a2a4faf | ReadME |  | 不明 | konni/ReadME.md | repository-notes | TLP:CLEAR | 中 |
| source--konni--e22c456560b2d889 | bluesky |  | 不明 | konni/bluesky.txt | text-data | TLP:CLEAR | 中 |
| source--konni--5b6e99ac261cea7a | konni threat insight paper triple threat N Korea aligned TA406 steals scams spies |  | 不明 | konni/konni-threat-insight-paper-triple-threat-N-Korea-aligned-TA406-steals-scams-spies.pdf | report | TLP:CLEAR | 中 |
| source--konni--2ab1db8e5d0c048a | konni ioclist 202111 |  | 2021-11 | konni/konni_ioclist_202111.csv | structured-data | TLP:CLEAR | 中 |
| source--konni--8c179de8de042c5a | the konni apt chronicle tracing their intelligence driven attack chain |  | 不明 | konni/the-konni-apt-chronicle-tracing-their-intelligence-driven-attack-chain.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
