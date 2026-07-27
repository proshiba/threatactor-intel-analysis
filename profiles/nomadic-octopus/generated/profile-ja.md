# Nomadic Octopus 脅威アクタープロファイル

- プロファイルID: `actor--nomadic-octopus`
- 状態: draft
- 更新日時: 2026-07-25T14:07:08Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Nomadic Octopusの標準化プロファイル。リポジトリ内の専用資料2件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Nomadic Octopus**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| DustSquad | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| Adversary | <br>[Nomadic Octopus](https://attack.mitre.org/groups/G0133) is a Russian-speaking cyber espionage threat group that has primarily targeted Central Asia, including local governments, diplomatic missions, and individuals, since at least 2014. [Nomadic Octopus](https://attack.mitre.org/groups/G0133) has been observed conducting campaigns involving Android and Windows malware, mainly using the Delphi programming language, and building custom variants.(Citation: Security Affairs DustSquad Oct 2018)(Citation: Securelist Octopus Oct 2018)(Citation: ESET Nomadic Octopus 2018) |
| Capability | Octopus |
| Infrastructure |  |
| Victim | Central Asian users and diplomatic entities |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | DustSquad, Golden Falcon | canonical-name | 高 | Russia | https://securelist.com/octopus-infested-seas-of-central-asia/88200/<br>https://www.zdnet.com/article/extensive-hacking-operation-discovered-in-kazakhstan/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=DustSquad%2C+Golden+Falcon&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | DustSquad | canonical-name | 高 | RU | https://securelist.com/octopus-infested-seas-of-central-asia/88200/<br>https://www.prodaft.com/m/reports/PAPERBUG_TLPWHITE-1.pdf<br>https://www.virusbulletin.com/conference/vb2018/abstracts/nomadic-octopus-cyber-espionage-central-asia/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Nomadic Octopus - G0133 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0133<br>https://securelist.com/octopus-infested-seas-of-central-asia/88200/<br>https://securityaffairs.co/wordpress/77165/apt/russia-linked-apt-dustsquad.html |
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
| malware--octopus | Octopus | [Octopus](https://attack.mitre.org/software/S0340) is a Windows Trojan written in the Delphi programming language that has been used by [Nomadic Octopus](https://attack.mitre.org/groups/G0133) to target government organizations in Central Asia since at least 2014.(Citation: Securelist Octopus Oct 2018)(Citation: Security Affairs DustSquad Oct 2018)(Citation: ESET Nomadic Octopus 2018)  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | Government | Targeting text indicates the Government sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Collection | T1005 | Data from Local System | .126.102) T1074 Data Staged .001 Local Data Staging Tools and exfiltrated files are first moved to inconspicously named directories like C : extbackslash intel T1005 Data from Local System Important files, like documents, in the local system are exfiltrated T1025 Data from Removable Media Files from the removable devices are exfiltrated T1114 Email Collection .001 Local Email Collection The operators collect and read emails of victims T1113 |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Discovery | T1007 | System Service Discovery | rnet Connection Discovery Pings network endpoints to check if they are reachable T1033 System Owner/User Discovery Lists all the users registered in the system T1007 System Service Discovery List services and tasks runn Lateral Movement T1570 Lateral Tool Transfer Tools are transfered in between victim machines T1021 Remote Services .001 Remote Desktop Protocol RDP is used to view and control devices of victims .005 VNC VNC is used to view a |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Discovery | T1012 | Query Registry | eral Device Discovery The malware checks peripheral devices in hopes of duplicating itself. T1057 Process Discovery Uses the command tasklist to list processes T1012 Query Registry Queries and edits registry keys to setup proxy for browser T1018 Remote System Discovery Malware checks the hosts file T1016 System Network Configuration Discovery .001 Internet Connection Discovery Pings network endpoints to check if they are reachable T1033 Syst |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Discovery | T1016 | System Network Configuration Discovery | t to list processes T1012 Query Registry Queries and edits registry keys to setup proxy for browser T1018 Remote System Discovery Malware checks the hosts file T1016 System Network Configuration Discovery .001 Internet Connection Discovery Pings network endpoints to check if they are reachable T1033 System Owner/User Discovery Lists all the users registered in the system T1007 System Service Discovery List services and tasks runn Lateral Mov |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Discovery | T1018 | Remote System Discovery | ing itself. T1057 Process Discovery Uses the command tasklist to list processes T1012 Query Registry Queries and edits registry keys to setup proxy for browser T1018 Remote System Discovery Malware checks the hosts file T1016 System Network Configuration Discovery .001 Internet Connection Discovery Pings network endpoints to check if they are reachable T1033 System Owner/User Discovery Lists all the users registered in the system T1007 Syste |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Lateral Movement | T1021 | Remote Services | system T1007 System Service Discovery List services and tasks runn Lateral Movement T1570 Lateral Tool Transfer Tools are transfered in between victim machines T1021 Remote Services .001 Remote Desktop Protocol RDP is used to view and control devices of victims .005 VNC VNC is used to view and control devices of victims T1091 Replication Through Removable Media Malware checks for USB drives and tries to infect DISCLAIMER : This document and |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Collection | T1025 | Data from Removable Media | inconspicously named directories like C : extbackslash intel T1005 Data from Local System Important files, like documents, in the local system are exfiltrated T1025 Data from Removable Media Files from the removable devices are exfiltrated T1114 Email Collection .001 Local Email Collection The operators collect and read emails of victims T1113 Screen Capture The operators capture the screen of victims Command And Control T1071 Application L |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Discovery | T1033 | System Owner/User Discovery | re checks the hosts file T1016 System Network Configuration Discovery .001 Internet Connection Discovery Pings network endpoints to check if they are reachable T1033 System Owner/User Discovery Lists all the users registered in the system T1007 System Service Discovery List services and tasks runn Lateral Movement T1570 Lateral Tool Transfer Tools are transfered in between victim machines T1021 Remote Services .001 Remote Desktop Protocol RD |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Stealth | T1036 | Masquerading | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--nomadic-octopus--85beb3f33e9c346d` |
| Credential Access, Discovery | T1040 | Network Sniffing | aperbug Discovery T1083 File and Directory Discovery Reads and writes ini files T1135 Network Share Discovery Lists network shares and printers using net share T1040 Network Sniffing Uses victim machines to sniff network packets T1120 Peripheral Device Discovery The malware checks peripheral devices in hopes of duplicating itself. T1057 Process Discovery Uses the command tasklist to list processes T1012 Query Registry Queries and edits regis |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | filtration T1048 Exfiltration Over Alternative Protocol .003 Exfiltration Over Unencrypted/ Obfuscated Non-C2 Protocol Data is exfiltrated to via HTTP requests T1041 Exfiltration Over C2 Channel Data is exfiltrated via DustSquad’s C2 server DISCLAIMER : This document and its contents shall be deemed as proprietary and privileged information of PRODAFT and shall be subjected to articles and provisions that have been stipulated in the General |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Execution | T1047 | Windows Management Instrumentation | b .002 At (Windows) Schedules tasks on widows using SCHTASKS to gain persistence .005 Scheduled Task Schedules their malware to run periodically on the machine T1047 Windows Management Instrumentation Use wmic to get information on hotfixes Persistence T1547 Boot or Logon Autostart Execution .001 Registry Run Keys / Startup Folder Adds malware into the Startup folder of compromised machines T1136 Create Account .001 Local Account Creates a u |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Exfiltration | T1048 | Exfiltration Over Alternative Protocol | Encoding Data sent to the C2 server is base64 encoded T1573 Encrypted Channel .002 Asymmetric Cryptography Data sent to the C2 server is encrypted Exfiltration T1048 Exfiltration Over Alternative Protocol .003 Exfiltration Over Unencrypted/ Obfuscated Non-C2 Protocol Data is exfiltrated to via HTTP requests T1041 Exfiltration Over C2 Channel Data is exfiltrated via DustSquad’s C2 server DISCLAIMER : This document and its contents shall be de |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Execution, Persistence, Privilege Escalation | T1053 | Scheduled Task/Job | i machine Execution T1059 Command and Scripting Interpreter .001 PowerShell Powershell is used to execute commans .003 Windows Command Shell cmd.exe /c is used T1053 Scheduled Task/Job .002 At (Windows) Schedules tasks on widows using SCHTASKS to gain persistence .005 Scheduled Task Schedules their malware to run periodically on the machine T1047 Windows Management Instrumentation Use wmic to get information on hotfixes Persistence T1547 Boo |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Discovery | T1057 | Process Discovery | Sniffing Uses victim machines to sniff network packets T1120 Peripheral Device Discovery The malware checks peripheral devices in hopes of duplicating itself. T1057 Process Discovery Uses the command tasklist to list processes T1012 Query Registry Queries and edits registry keys to setup proxy for browser T1018 Remote System Discovery Malware checks the hosts file T1016 System Network Configuration Discovery .001 Internet Connection Discove |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Execution | T1059 | Command and Scripting Interpreter | .002 Domain Accounts Scans the available domain accounts in the network. .003 Local Accounts Scans the local accounts registered in the victi machine Execution T1059 Command and Scripting Interpreter .001 PowerShell Powershell is used to execute commans .003 Windows Command Shell cmd.exe /c is used T1053 Scheduled Task/Job .002 At (Windows) Schedules tasks on widows using SCHTASKS to gain persistence .005 Scheduled Task Schedules their malwa |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Execution | T1059.001 | PowerShell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071 | Application Layer Protocol | 01 Local Email Collection The operators collect and read emails of victims T1113 Screen Capture The operators capture the screen of victims Command And Control T1071 Application Layer Protocol .001 Web Protocols Posts data to the C2 server .004 DNS Runs a DNS lookup for the web server T1132 Data Encoding .001 Standard Encoding Data sent to the C2 server is base64 encoded T1573 Encrypted Channel .002 Asymmetric Cryptography Data sent to the C |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Collection | T1074 | Data Staged | e exfiltrated are compressed using the 7z utility T1185 Browser Session Hijacking Custom proxy is set for browsers to analyze outgoing traffic (185.32.126.102) T1074 Data Staged .001 Local Data Staging Tools and exfiltrated files are first moved to inconspicously named directories like C : extbackslash intel T1005 Data from Local System Important files, like documents, in the local system are exfiltrated T1025 Data from Removable Media Files |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | Nomadic Octopus’ Tajikistan Campaign : Paperbug Initial Access T1091 Replication Through Removable Media Malware checks for USB drives and tries to infect them T1078 Valid Accounts .002 Domain Accounts Scans the available domain accounts in the network. .003 Local Accounts Scans the local accounts registered in the victi machine Execution T1059 Command and Scripting Interpreter .001 PowerShell Powershell is used to execute commans .003 Windo |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Discovery | T1083 | File and Directory Discovery | TLP:CLEAR Nomadic Octopus’ Tajikistan Campaign : Paperbug Discovery T1083 File and Directory Discovery Reads and writes ini files T1135 Network Share Discovery Lists network shares and printers using net share T1040 Network Sniffing Uses victim machines to sniff network packets T1120 Peripheral Device Discovery The malware checks peripheral devices in |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Initial Access, Lateral Movement | T1091 | Replication Through Removable Media | TLP:CLEAR Nomadic Octopus’ Tajikistan Campaign : Paperbug Initial Access T1091 Replication Through Removable Media Malware checks for USB drives and tries to infect them T1078 Valid Accounts .002 Domain Accounts Scans the available domain accounts in the network. .003 Local Accounts Scans the local accounts registered in the victi machine Execution T1059 C |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1113 | Screen Capture | able Media Files from the removable devices are exfiltrated T1114 Email Collection .001 Local Email Collection The operators collect and read emails of victims T1113 Screen Capture The operators capture the screen of victims Command And Control T1071 Application Layer Protocol .001 Web Protocols Posts data to the C2 server .004 DNS Runs a DNS lookup for the web server T1132 Data Encoding .001 Standard Encoding Data sent to the C2 server is b |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Collection | T1114 | Email Collection | al System Important files, like documents, in the local system are exfiltrated T1025 Data from Removable Media Files from the removable devices are exfiltrated T1114 Email Collection .001 Local Email Collection The operators collect and read emails of victims T1113 Screen Capture The operators capture the screen of victims Command And Control T1071 Application Layer Protocol .001 Web Protocols Posts data to the C2 server .004 DNS Runs a DNS |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Discovery | T1120 | Peripheral Device Discovery | ini files T1135 Network Share Discovery Lists network shares and printers using net share T1040 Network Sniffing Uses victim machines to sniff network packets T1120 Peripheral Device Discovery The malware checks peripheral devices in hopes of duplicating itself. T1057 Process Discovery Uses the command tasklist to list processes T1012 Query Registry Queries and edits registry keys to setup proxy for browser T1018 Remote System Discovery Mal |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Command And Control | T1132 | Data Encoding | en of victims Command And Control T1071 Application Layer Protocol .001 Web Protocols Posts data to the C2 server .004 DNS Runs a DNS lookup for the web server T1132 Data Encoding .001 Standard Encoding Data sent to the C2 server is base64 encoded T1573 Encrypted Channel .002 Asymmetric Cryptography Data sent to the C2 server is encrypted Exfiltration T1048 Exfiltration Over Alternative Protocol .003 Exfiltration Over Unencrypted/ Obfuscated |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Discovery | T1135 | Network Share Discovery | TLP:CLEAR Nomadic Octopus’ Tajikistan Campaign : Paperbug Discovery T1083 File and Directory Discovery Reads and writes ini files T1135 Network Share Discovery Lists network shares and printers using net share T1040 Network Sniffing Uses victim machines to sniff network packets T1120 Peripheral Device Discovery The malware checks peripheral devices in hopes of duplicating itself. T1057 Process Discovery Uses the |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Persistence | T1136 | Create Account | tfixes Persistence T1547 Boot or Logon Autostart Execution .001 Registry Run Keys / Startup Folder Adds malware into the Startup folder of compromised machines T1136 Create Account .001 Local Account Creates a user called Admin on compromised machines DISCLAIMER : This document and its contents shall be deemed as proprietary and privileged information of PRODAFT and shall be subjected to articles and provisions that have been stipulated in t |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Collection | T1185 | Browser Session Hijacking | pus’ Tajikistan Campaign : Paperbug Collection T1560 Archive Collected Data .001 Archive via Utility Data to be exfiltrated are compressed using the 7z utility T1185 Browser Session Hijacking Custom proxy is set for browsers to analyze outgoing traffic (185.32.126.102) T1074 Data Staged .001 Local Data Staging Tools and exfiltrated files are first moved to inconspicously named directories like C : extbackslash intel T1005 Data from Local Sys |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Credential Access | T1187 | Forced Authentication | k or Service Renames tools to appear as system tasks .005 Match Legitimate Name or Location Renames tools and puts them in the Mozilla folder Credential Access T1187 Forced Authentication Runs a SCF file attack, with the filename pentesterlab.ico T1555 Credentials from Password Stores .001 Windows Credential Manager Uses LaZagne to steal credentials from vault files .003 Credentials from Web Browsers Uses LaZagne to steal credentials from br |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547 | Boot or Logon Autostart Execution | ed Task Schedules their malware to run periodically on the machine T1047 Windows Management Instrumentation Use wmic to get information on hotfixes Persistence T1547 Boot or Logon Autostart Execution .001 Registry Run Keys / Startup Folder Adds malware into the Startup folder of compromised machines T1136 Create Account .001 Local Account Creates a user called Admin on compromised machines DISCLAIMER : This document and its contents shall be |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Credential Access | T1552 | Unsecured Credentials | indows Credential Manager Uses LaZagne to steal credentials from vault files .003 Credentials from Web Browsers Uses LaZagne to steal credentials from browsers T1552 Unsecured Credentials .001 Credentials In Files Searches for the string password in the whole computer using LaZagne DISCLAIMER : This document and its contents shall be deemed as proprietary and privileged information of PRODAFT and shall be subjected to articles and provisions |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Credential Access | T1555 | Credentials from Password Stores | tion Renames tools and puts them in the Mozilla folder Credential Access T1187 Forced Authentication Runs a SCF file attack, with the filename pentesterlab.ico T1555 Credentials from Password Stores .001 Windows Credential Manager Uses LaZagne to steal credentials from vault files .003 Credentials from Web Browsers Uses LaZagne to steal credentials from browsers T1552 Unsecured Credentials .001 Credentials In Files Searches for the string pa |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Collection | T1560 | Archive Collected Data | TLP:CLEAR Nomadic Octopus’ Tajikistan Campaign : Paperbug Collection T1560 Archive Collected Data .001 Archive via Utility Data to be exfiltrated are compressed using the 7z utility T1185 Browser Session Hijacking Custom proxy is set for browsers to analyze outgoing traffic (185.32.126.102) T1074 Data Staged .001 Local Data Staging Tools and exfiltrate |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Uncategorized | T1562 | MITRE ATT&CK T1562 | LEAR Nomadic Octopus’ Tajikistan Campaign : Paperbug Defense Evasion T1564 Hide Artifacts .003 Hidden Window Creates a hidden powershell window to run commands T1562 Impair Defenses .004 Disable or Modify System Firewall Changes the firewall settings so that it allows their surveillance programs. T1036 Masquerading .004 Masquerade Task or Service Renames tools to appear as system tasks .005 Match Legitimate Name or Location Renames tools and |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Stealth | T1564 | Hide Artifacts | TLP:CLEAR Nomadic Octopus’ Tajikistan Campaign : Paperbug Defense Evasion T1564 Hide Artifacts .003 Hidden Window Creates a hidden powershell window to run commands T1562 Impair Defenses .004 Disable or Modify System Firewall Changes the firewall settings so that it allows their surveillance programs. T1036 Masquerading .004 Masquerade Task or Service Renam |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Stealth | T1564.003 | Hidden Window | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1570 | Lateral Tool Transfer | ble T1033 System Owner/User Discovery Lists all the users registered in the system T1007 System Service Discovery List services and tasks runn Lateral Movement T1570 Lateral Tool Transfer Tools are transfered in between victim machines T1021 Remote Services .001 Remote Desktop Protocol RDP is used to view and control devices of victims .005 VNC VNC is used to view and control devices of victims T1091 Replication Through Removable Media Malwa |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Command And Control | T1573 | Encrypted Channel | sts data to the C2 server .004 DNS Runs a DNS lookup for the web server T1132 Data Encoding .001 Standard Encoding Data sent to the C2 server is base64 encoded T1573 Encrypted Channel .002 Asymmetric Cryptography Data sent to the C2 server is encrypted Exfiltration T1048 Exfiltration Over Alternative Protocol .003 Exfiltration Over Unencrypted/ Obfuscated Non-C2 Protocol Data is exfiltrated to via HTTP requests T1041 Exfiltration Over C2 Cha |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Resource Development | T1587 | Develop Capabilities | t victim’s connections to other possible victims .004 Identify Roles Tries to identift the role of the victim within the business context. Resource Development T1587 Develop Capabilities .001 Malware Installs malware on victim machines to gain control. DISCLAIMER : This document and its contents shall be deemed as proprietary and privileged information of PRODAFT and shall be subjected to articles and provisions that have been stipulated in |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Reconnaissance | T1589 | Gather Victim Identity Information | tem itself .002 Software Gathers information on the OS and installed apps .004 Client Configurations Steal configurations for messagging apps and email clients T1589 Gather Victim Identity Information .001 Credentials Gathers user credentials on the victim machine .002 Email Addresses Gathers email addresses on the victim machine .003 Employee Names Gathers employee information on victim machines T1590 Gather Victim Network Information .002 |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Reconnaissance | T1590 | Gather Victim Network Information | ls on the victim machine .002 Email Addresses Gathers email addresses on the victim machine .003 Employee Names Gathers employee information on victim machines T1590 Gather Victim Network Information .002 DNS Exfiltrates the DNS cache from machines .004 Network Topology Discovers the network topology of compromised machines .005 IP Addresses Does a scan of IP addresses of connected machines T1591 Gather Victim Org Information .002 Business R |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Reconnaissance | T1591 | Gather Victim Org Information | from machines .004 Network Topology Discovers the network topology of compromised machines .005 IP Addresses Does a scan of IP addresses of connected machines T1591 Gather Victim Org Information .002 Business Relationships Gathers information about victim’s connections to other possible victims .004 Identify Roles Tries to identift the role of the victim within the business context. Resource Development T1587 Develop Capabilities .001 Malwa |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Reconnaissance | T1592 | Gather Victim Host Information | dic Octopus’ Tajikistan Campaign : Paperbug 7 TTP Reconnaissance T1595 Active Scanning .001 Scanning IP Blocks Scans the devices in the victim’s network block. T1592 Gather Victim Host Information .001 Hardware Gathers information on the system itself .002 Software Gathers information on the OS and installed apps .004 Client Configurations Steal configurations for messagging apps and email clients T1589 Gather Victim Identity Information .00 |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |
| Reconnaissance | T1595 | Active Scanning | TLP:CLEAR Nomadic Octopus’ Tajikistan Campaign : Paperbug 7 TTP Reconnaissance T1595 Active Scanning .001 Scanning IP Blocks Scans the devices in the victim’s network block. T1592 Gather Victim Host Information .001 Hardware Gathers information on the system itself .002 Software Gathers information on the OS and installed apps .004 Client Configurations Steal co |  |  | 不明 | 不明 | 中 | `source--nomadic-octopus--85beb3f33e9c346d` |

## IOC／artifact概要

- IOC値: 36件
- IOC観測: 47件
- 複数攻撃で観測: 0件
- 要レビュー候補: 11件
- 非IOC artifact観測: 96件（`artifacts.csv`）

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
| source--nomadic-octopus--85beb3f33e9c346d | Nomadic Octopus’ Paperbug Campaign |  | 不明 | DustSquad/Nomadic Octopus’ Paperbug Campaign.pdf | report | TLP:CLEAR | 中 |
| source--nomadic-octopus--7d9417ca3cd26395 | README |  | 不明 | DustSquad/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
