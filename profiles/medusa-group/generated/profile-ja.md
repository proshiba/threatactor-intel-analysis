# Medusa Group 脅威アクタープロファイル

- プロファイルID: `actor--medusa-group`
- 状態: draft
- 更新日時: 2026-09-20T13:48:12Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Medusa Groupの標準化プロファイル。リポジトリ内の専用資料0件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Medusa Group**
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
| Adversary | [Medusa Group](https://attack.mitre.org/groups/G1051) has been active since at least 2021 and was initially operated as a closed ransomware group before evolving into a Ransomware-as-a-Service (RaaS) operation. Some reporting indicates that certain attacks may still be conducted directly by the ransomware’s core developers. Public sources have also referred to the group as “Spearwing” or “Medusa Actors.” (Citation: CISA Medusa Group Medusa Ransomware March 2025) (Citation: Broadcom Medusa Ransomware Medusa Group March 2025) [Medusa Group](https://attack.mitre.org/groups/G1051) employs living-off-the-land techniques, frequently leveraging publicly available tools and common remote management software to conduct operations. The group engages in double extortion tactics, exfiltrating data prior to encryption and threatening to publish stolen information if ransom demands are not met. (Citation: Security Scorecard Medusa Ransomware January 2024) For initial access, [Medusa Group](https://attack.mitre.org/groups/G1051) has exploited publicly known vulnerabilities, conducted phishing campaigns, and used credentials or access purchased from Initial Access Brokers (IABs). The group is opportunistic and has targeted a wide range of sectors globally. (Citation: Intel471 Medusa Ransomware May 2025) |
| Capability | Medusa Ransomware, certutil, Rclone, Mimikatz, PsExec |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-09-20T13:47:46Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | 一致なし |  |  |  |  |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | Medusa Group - G1051 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1051<br>https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf<br>https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a |
| misp-mitre-intrusion-set | Medusa Group - G1051 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1051<br>https://securityscorecard.com/wp-content/uploads/2024/01/deep-dive-into-medusa-ransomware.pdf<br>https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-071a |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | 一致なし |  |  |  |  |

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
| malware--medusa-ransomware | Medusa Ransomware | [Medusa Ransomware](https://attack.mitre.org/software/S1244) has been utilized in attacks since at least 2021. [Medusa Ransomware](https://attack.mitre.org/software/S1244) has been known to be utilized in conjunction with living off the land techniques and remote management software. [Medusa Ransomware](https://attack.mitre.org/software/S1244) has been used in campaigns associated with “double extortion” ransomware activity, where data is exfiltrated from victim environments prior to encryption, with threats to publish files if a ransom is not paid. [Medusa Ransomware](https://attack.mitre.org/software/S1244) software was initially a closed ransomware variant which later evolved to a Ransomware as a Service (RaaS). [Medusa Ransomware](https://attack.mitre.org/software/S1244) has impacted victims from a diverse range of sectors within a multitude of countries, and it is assessed [Medusa Ransomware](https://attack.mitre.org/software/S1244) is used in an opportunistic manner.(Citation: CISA Medusa Group Medusa Ransomware March 2025)(Citation: Security Scorecard Medusa Ransomware January 2024)(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024)(Citation: Broadcom Medusa Ransomware Medusa Group March 2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--certutil | certutil | [certutil](https://attack.mitre.org/software/S0160) is a command-line utility that can be used to obtain certificate authority information and configure Certificate Services. (Citation: TechNet Certutil) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| tool--psexec | PsExec | [PsExec](https://attack.mitre.org/software/S0029) is a free Microsoft tool that can be used to execute a program on another computer. It is used by IT administrators and attackers.(Citation: Russinovich Sysinternals)(Citation: SANS PsExec) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| tool--rclone | Rclone | [Rclone](https://attack.mitre.org/software/S1040) is a command line program for syncing files with cloud storage services such as Dropbox, Google Drive, Amazon S3, and MEGA. [Rclone](https://attack.mitre.org/software/S1040) has been used in a number of ransomware campaigns, including those associated with the [Conti](https://attack.mitre.org/software/S0575) and DarkSide Ransomware-as-a-Service operations.(Citation: Rclone)(Citation: Rclone Wars)(Citation: Detecting Rclone)(Citation: DarkSide Ransomware Gang)(Citation: DFIR Conti Bazar Nov 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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

### 活動別ダイヤモンドモデル

活動別ダイヤモンドモデルなし



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| regions | 全世界 | MITRE ATT&CKのGroup概要でMedusa Groupの標的範囲として全世界が明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.001 | LSASS Memory | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged [Mimikatz](https://attack.mitre.org/software/S0002) to dump LSASS to harvest credentials.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Credential Access | T1003.003 | NTDS | [Medusa Group](https://attack.mitre.org/groups/G1051) has accessed the ntds.dit file to engage in credential dumping.(Citation: Broadcom Medusa Ransomware Medusa Group March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1016 | System Network Configuration Discovery | [Medusa Group](https://attack.mitre.org/groups/G1051) has obtained host network details utilizing the command `cmd.exe /c ipconfig /all`.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1018 | Remote System Discovery | [Medusa Group](https://attack.mitre.org/groups/G1051) has used PDQ Inventory to get an inventory of the endpoints on the network.(Citation: Broadcom Medusa Ransomware Medusa Group March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | [Medusa Group](https://attack.mitre.org/groups/G1051) has used RDP to conduct lateral movement and exfiltrate data.(Citation: CISA Medusa Group Medusa Ransomware March 2025) [Medusa Group](https://attack.mitre.org/groups/G1051) has also utilized the Windows executable `mstsc.exe` for RDP activities through the command `mstsc.exe /v:{hostname/ip}`.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1027.002 | Software Packing | [Medusa Group](https://attack.mitre.org/groups/G1051) has packed the code of dropped kernel drivers using the packer ASM Guard.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1027.010 | Command Obfuscation | [Medusa Group](https://attack.mitre.org/groups/G1051) has obfuscated PowerShell scripts with Base64 encoding.(Citation: CISA Medusa Group Medusa Ransomware March 2025) [Medusa Group](https://attack.mitre.org/groups/G1051) has also obfuscated the code of dropped kernel drivers using a software known as Safengine Shielden which randomized the code through code mutations and then leveraged an embedded virtual machine interpreter to execute the code.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1033 | System Owner/User Discovery | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized [PsExec](https://attack.mitre.org/software/S0029) to execute `quser` to discover the user session information.(Citation: Broadcom Medusa Ransomware Medusa Group March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1046 | Network Service Discovery | [Medusa Group](https://attack.mitre.org/groups/G1051) has the capability to use living off the land (LOTL) binaries to perform network enumeration.(Citation: CISA Medusa Group Medusa Ransomware March 2025) [Medusa Group](https://attack.mitre.org/groups/G1051) has also utilized the publicly available scanning tool SoftPerfect Network Scanner (`netscan.exe`) to discover device hostnames and network services.(Citation: Broadcom Medusa Ransomware Medusa Group March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1047 | Windows Management Instrumentation | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized Windows Management Instrumentation to query system information.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024)(Citation: CISA Medusa Group Medusa Ransomware March 2025)(Citation: Intel471 Medusa Ransomware May 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1057 | Process Discovery | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized a hard-coded security tool process list that identifies and terminates using an undocumented IOCTL code 0x222094.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.001 | PowerShell | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged PowerShell for execution and defense evasion.(Citation: Check Point Medusa Ransomware April 2025)(Citation: CISA Medusa Group Medusa Ransomware March 2025)(Citation: Intel471 Medusa Ransomware May 2025) [Medusa Group](https://attack.mitre.org/groups/G1051) has also utilized PowerShell to execute a bitsadmin transfer from file hosting site.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.003 | Windows Command Shell | [Medusa Group](https://attack.mitre.org/groups/G1051) has used Windows Command Prompt to control and execute commands on the system to include ingress, network, and filesystem enumeration activities.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1069.002 | Domain Groups | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized the `net group` command to query domain groups within the victim environment.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1070.003 | Clear Command History | [Medusa Group](https://attack.mitre.org/groups/G1051) has cleared command history by running the PowerShell command `Remove-Item (Get-PSReadlineOption).HistorySavePath`.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1070.004 | File Deletion | [Medusa Group](https://attack.mitre.org/groups/G1051) has deleted previously installed tools.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1071.001 | Web Protocols | [Medusa Group](https://attack.mitre.org/groups/G1051) has communicated through reverse or bind shells over port 443 (HTTPS).(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution, Lateral Movement | T1072 | Software Deployment Tools | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized software deployment and management solutions to deploy their encryption payload to include BigFix and PDQ Deploy.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized compromised legitimate local and domain accounts within the victim environment to facilitate remote access and lateral movement sometimes in combination with [PsExec](https://attack.mitre.org/software/S0029).(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1082 | System Information Discovery | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged `cmd.exe` to identify system info `cmd.exe /c systeminfo`.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1083 | File and Directory Discovery | [Medusa Group](https://attack.mitre.org/groups/G1051) has searched for files within the victim environment for encryption and exfiltration.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024)(Citation: CISA Medusa Group Medusa Ransomware March 2025)(Citation: Security Scorecard Medusa Ransomware January 2024) [Medusa Group](https://attack.mitre.org/groups/G1051) has also identified files associated with remote management services.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024)(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1087.001 | Local Account | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged `net user` for account discovery.(Citation: Broadcom Medusa Ransomware Medusa Group March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1090.003 | Multi-hop Proxy | [Medusa Group](https://attack.mitre.org/groups/G1051) has used TOR nodes for communications.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024)(Citation: Check Point Medusa Ransomware April 2025)(Citation: Broadcom Medusa Ransomware Medusa Group March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1105 | Ingress Tool Transfer | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged [certutil](https://attack.mitre.org/software/S0160), PowerShell, and Windows Command to download additional tools to include RMM services.(Citation: CISA Medusa Group Medusa Ransomware March 2025) [Medusa Group](https://attack.mitre.org/groups/G1051) has also engaged in “Bring Your Own Vulnerable Driver” (BYOVD) and downloaded vulnerable or signed drivers to the victim environment to disable security tools.(Citation: CISA Medusa Group Medusa Ransomware March 2025)(Citation: Broadcom Medusa Ransomware Medusa Group March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1106 | Native API | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged Windows Native API functions to execute payloads.(Citation: Security Scorecard Medusa Ransomware January 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Defense Impairment, Persistence | T1112 | Modify Registry | [Medusa Group](https://attack.mitre.org/groups/G1051) has modified Registry keys to elevate privileges, maintain persistence and allow remote access.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1135 | Network Share Discovery | [Medusa Group](https://attack.mitre.org/groups/G1051) has identified network shares using `cmd.exe /c net share`.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Persistence | T1136.002 | Domain Account | [Medusa Group](https://attack.mitre.org/groups/G1051) has created a domain account within the victim environment.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1190 | Exploit Public-Facing Application | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged public facing vulnerabilities in their campaigns against victim organizations to gain initial access.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024)(Citation: Broadcom Medusa Ransomware Medusa Group March 2025) [Medusa Group](https://attack.mitre.org/groups/G1051) has also utilized CVE-2024-1709 in ScreenConnect, and CVE-2023-48788 in Fortinet EMS for initial access to victim environments.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1218.014 | MMC | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged Microsoft Management Console (MMC) to facilitate lateral movement and to interact locally or remotely with victim devices using the command `mmc.exe compmgmt.msc /computer:{hostname/ip}`.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1219 | Remote Access Tools | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged Remote Access Software for lateral movement and data exfiltration.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024)(Citation: CISA Medusa Group Medusa Ransomware March 2025)(Citation: Broadcom Medusa Ransomware Medusa Group March 2025)(Citation: Security Scorecard Medusa Ransomware January 2024) [Medusa Group](https://attack.mitre.org/groups/G1051) has also been known to utilize Remote Access Software such as AnyDesk, Atera, ConnectWise, eHorus, N-Able, PDQ Deploy, PDQ Inventory, SimpleHelp and Splashtop.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Impact | T1486 | Data Encrypted for Impact | [Medusa Group](https://attack.mitre.org/groups/G1051) has encrypted files using AES-256 encryption which then appends the file extension “.medusa” to encrypted files and leaves a ransomware note named “!READ_ME_MEDUSA!!!.txt.”(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024)(Citation: CISA Medusa Group Medusa Ransomware March 2025)(Citation: Broadcom Medusa Ransomware Medusa Group March 2025)(Citation: Security Scorecard Medusa Ransomware January 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Impact | T1489 | Service Stop | [Medusa Group](https://attack.mitre.org/groups/G1051) has terminated services related to backups, security, databases, communication, filesharing and websites.(Citation: CISA Medusa Group Medusa Ransomware March 2025)(Citation: Broadcom Medusa Ransomware Medusa Group March 2025)(Citation: Security Scorecard Medusa Ransomware January 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Impact | T1490 | Inhibit System Recovery | [Medusa Group](https://attack.mitre.org/groups/G1051) has deleted recovery files such as shadow copies using `vssadmin.exe`.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024)(Citation: CISA Medusa Group Medusa Ransomware March 2025)(Citation: Broadcom Medusa Ransomware Medusa Group March 2025)(Citation: Security Scorecard Medusa Ransomware January 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Persistence | T1505.003 | Web Shell | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized webshells to an exploited Microsoft Exchange Server.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1518.001 | Security Software Discovery | [Medusa Group](https://attack.mitre.org/groups/G1051) has detected security solutions for termination or deletion within the victim device using hard-coded lists of strings containing security product executables.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Impact | T1529 | System Shutdown/Reboot | [Medusa Group](https://attack.mitre.org/groups/G1051) has manually turned off and encrypted virtual machines.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | [Medusa Group](https://attack.mitre.org/groups/G1051) has used vulnerable or signed drivers to modify security solutions on victim devices.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Privilege Escalation | T1548.002 | Bypass User Account Control | [Medusa Group](https://attack.mitre.org/groups/G1051) has attempted to bypass UAC using Component Object Model (COM) interface.(Citation: Intel471 Medusa Ransomware May 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Defense Impairment | T1553.002 | Code Signing | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized vulnerable or signed drivers to kill or delete services associated with endpoint detection and response (EDR) tools.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1559.001 | Component Object Model | [Medusa Group](https://attack.mitre.org/groups/G1051) has leveraged Component Object Model (COM) to bypass UAC.(Citation: Intel471 Medusa Ransomware May 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1564.003 | Hidden Window | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized the `ShowWindow` API function to hide the current window.(Citation: Security Scorecard Medusa Ransomware January 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized [Rclone](https://attack.mitre.org/software/S1040) to exfiltrate data from victim environments to cloud storage.(Citation: CISA Medusa Group Medusa Ransomware March 2025)(Citation: Broadcom Medusa Ransomware Medusa Group March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1569.002 | Service Execution | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized [PsExec](https://attack.mitre.org/software/S0029) to execute scripts and commands within victim environments.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024)(Citation: CISA Medusa Group Medusa Ransomware March 2025)(Citation: Broadcom Medusa Ransomware Medusa Group March 2025) [Medusa Group](https://attack.mitre.org/groups/G1051) has also used the Windows service RoboCopy to search and copy data for exfiltration.(Citation: Broadcom Medusa Ransomware Medusa Group March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Lateral Movement | T1570 | Lateral Tool Transfer | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized legitimate software services such as PDQ Deploy to transfer malicious binaries and tools to other victimized hosts within the target environment.(Citation: Broadcom Medusa Ransomware Medusa Group March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1573.002 | Asymmetric Cryptography | [Medusa Group](https://attack.mitre.org/groups/G1051) has used HTTPS for command and control.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1583.006 | Web Services | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized a file hosting service named filemail[.]com to host a zip file that contained malicious payloads that facilitated follow-on actions.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1585.001 | Social Media Accounts | [Medusa Group](https://attack.mitre.org/groups/G1051) has created social media accounts including Telegram and X to publicize their activities.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024)(Citation: Check Point Medusa Ransomware April 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1585.002 | Email Accounts | [Medusa Group](https://attack.mitre.org/groups/G1051) has created email accounts used in ransomware negotiations.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1588.002 | Tool | [Medusa Group](https://attack.mitre.org/groups/G1051) has obtained and leveraged numerous RMM services, along with publicly available tools used for scanning.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024)(Citation: CISA Medusa Group Medusa Ransomware March 2025)(Citation: Broadcom Medusa Ransomware Medusa Group March 2025) [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized tools such as Advanced IP Scanner and SoftPerfect Network scanner for user, system and network discovery.(Citation: CISA Medusa Group Medusa Ransomware March 2025) [Medusa Group](https://attack.mitre.org/groups/G1051) has also acquired tools for command and control and defense evasion which include tunneling tools Ligolo and Cloudflared.(Citation: CISA Medusa Group Medusa Ransomware March 2025)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1608.002 | Upload Tool | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized a file hosting service called filemail[.]com to host a zip file that contained a RMM service such as ConnectWise.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1650 | Acquire Access | [Medusa Group](https://attack.mitre.org/groups/G1051) has purchased user credentials and other sensitive data from Initial Access Brokers (IABs).(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024)(Citation: Check Point Medusa Ransomware April 2025)(Citation: CISA Medusa Group Medusa Ransomware March 2025)(Citation: Intel471 Medusa Ransomware May 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1652 | Device Driver Discovery | [Medusa Group](https://attack.mitre.org/groups/G1051) has queried drivers on the victim device through the command `driverquery`.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Impact | T1657 | Financial Theft | [Medusa Group](https://attack.mitre.org/groups/G1051) has stolen and encrypted victims' data in order to extort victims into paying a ransom.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024)(Citation: Check Point Medusa Ransomware April 2025)(Citation: CISA Medusa Group Medusa Ransomware March 2025)(Citation: Intel471 Medusa Ransomware May 2025)(Citation: Broadcom Medusa Ransomware Medusa Group March 2025)(Citation: Security Scorecard Medusa Ransomware January 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Defense Impairment | T1685 | Disable or Modify Tools | [Medusa Group](https://attack.mitre.org/groups/G1051) has terminated antivirus services utilizing the gaze.exe executable and utilizing `psexec.exe`.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024)(Citation: CISA Medusa Group Medusa Ransomware March 2025)(Citation: Broadcom Medusa Ransomware Medusa Group March 2025) [Medusa Group](https://attack.mitre.org/groups/G1051) has also leveraged I/O control codes (IOCTLs) for terminating and deleting processes of identified security tools.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Defense Impairment | T1686 | Disable or Modify System Firewall | [Medusa Group](https://attack.mitre.org/groups/G1051) has utilized [PsExec](https://attack.mitre.org/software/S0029) to execute batch scripts that modify firewall settings.(Citation: CISA Medusa Group Medusa Ransomware March 2025)  [Medusa Group](https://attack.mitre.org/groups/G1051) has also enabled and modified firewall rules to allow for RDP connections for lateral movement and device interactions.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Defense Impairment | T1690 | Prevent Command History Logging | [Medusa Group](https://attack.mitre.org/groups/G1051) has removed PowerShell command history through the use of the PSReadLine module by running the PowerShell command `Remove-Item (Get-PSReadlineOption).HistorySavePath`.(Citation: CISA Medusa Group Medusa Ransomware March 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

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
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
