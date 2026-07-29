# BlackByte 脅威アクタープロファイル

- プロファイルID: `actor--blackbyte`
- 状態: draft
- 更新日時: 2026-07-29T23:11:59Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

BlackByteの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **BlackByte**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Black Basta | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Conti | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| DEV-0569 | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Diavol | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Hecamede | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Quantum | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Royal | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Ryuk (as FIN12) | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Wizard Spider (DEV-0193) | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

## 帰属

The repository mapping workbook places this actor in the Russia worksheet.

- 国: Russia
- スポンサー種別: state
- 確度: 中
- 証拠: `source--actor-mapping-workbook`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | State-sponsored intelligence collection or strategic operations. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [BlackByte](https://attack.mitre.org/groups/G1043) is a ransomware threat actor operating since at least 2021. [BlackByte](https://attack.mitre.org/groups/G1043) is associated with several versions of ransomware also labeled [BlackByte Ransomware](https://attack.mitre.org/software/S1180). [BlackByte](https://attack.mitre.org/groups/G1043) ransomware operations initially used a common encryption key allowing for the development of a universal decryptor, but subsequent versions such as [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) use more robust encryption mechanisms. [BlackByte](https://attack.mitre.org/groups/G1043) is notable for operations targeting critical infrastructure entities among other targets across North America.(Citation: FBI BlackByte 2022)(Citation: Picus BlackByte 2022)(Citation: Symantec BlackByte 2022)(Citation: Microsoft BlackByte 2023)(Citation: Cisco BlackByte 2024) |
| Capability | BlackByte 2.0 Ransomware, Exbyte, BlackByte Ransomware, Cobalt Strike, BATLOADER, Royal Ransomware, Ursnif, Gozi, Vidar Stealer & Cobals Strike as well as legitimate synchro remote monitoring and management (RMM) tools., Arp, Mimikatz, AdFind, PsExec |
| Infrastructure |  |
| Victim | Healthcare, manifacturing, professional, scientific, technical services, wholesale, education |
| Socio-political | Russia |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | DEV-0569 | single-alias-intersection | 中 |  | https://www.microsoft.com/en-us/security/blog/2022/11/17/dev-0569-finds-new-ways-to-deliver-royal-ransomware-various-payloads/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | BlackByte - G1043 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1043<br>https://blog.talosintelligence.com/blackbyte-blends-tried-and-true-tradecraft-with-newly-disclosed-vulnerabilities-to-support-ongoing-attacks/<br>https://www.ic3.gov/CSA/2022/220211.pdf |
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
| malware--batloader | BATLOADER | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--blackbyte-2-0-ransomware | BlackByte 2.0 Ransomware | [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) is a replacement for [BlackByte Ransomware](https://attack.mitre.org/software/S1180). Unlike [BlackByte Ransomware](https://attack.mitre.org/software/S1180), [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) does not have a common key for victim decryption. [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) remains uniquely associated with [BlackByte](https://attack.mitre.org/groups/G1043) operations.(Citation: Microsoft BlackByte 2023) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--blackbyte-ransomware | BlackByte Ransomware | [BlackByte Ransomware](https://attack.mitre.org/software/S1180) is uniquely associated with [BlackByte](https://attack.mitre.org/groups/G1043) operations. [BlackByte Ransomware](https://attack.mitre.org/software/S1180) used a common key for infections, allowing for the creation of a universal decryptor.(Citation: Trustwave BlackByte 2021)(Citation: FBI BlackByte 2022) [BlackByte Ransomware](https://attack.mitre.org/software/S1180) was replaced in [BlackByte](https://attack.mitre.org/groups/G1043) operations by [BlackByte 2.0 Ransomware](https://attack.mitre.org/software/S1181) by 2023.(Citation: Microsoft BlackByte 2023)(Citation: Cisco BlackByte 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--cobalt-strike | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) is a commercial, full-featured, remote access tool that bills itself as “adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors”. Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.(Citation: cobaltstrike manual)<br><br>In addition to its own capabilities, [Cobalt Strike](https://attack.mitre.org/software/S0154) leverages the capabilities of other well-known tools such as Metasploit and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: cobaltstrike manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--exbyte | Exbyte | [Exbyte](https://attack.mitre.org/software/S1179) is an exfiltration tool written in Go that is uniquely associated with [BlackByte](https://attack.mitre.org/groups/G1043) operations. Observed since 2022, [Exbyte](https://attack.mitre.org/software/S1179) transfers collected files to online file sharing and hosting services.(Citation: Symantec BlackByte 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--gozi | Gozi | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--royal-ransomware | Royal Ransomware | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--ursnif | Ursnif | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--vidar-stealer-cobals-strike-as-well-as-legitimate-synchro-remote-monitoring-and-management-rmm-tools | Vidar Stealer & Cobals Strike as well as legitimate synchro remote monitoring and management (RMM) tools. | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--arp | Arp | [Arp](https://attack.mitre.org/software/S0099) displays and modifies information about a system's Address Resolution Protocol (ARP) cache. (Citation: TechNet Arp) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
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
| BazarCall Campaign | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| BlackByteが新たな脆弱性を活用し攻撃を継続 | reported-activity | 不明 | 不明 | 2024-08-29 |  |  |  |  | BlackByteが新たな脆弱性を活用し攻撃を継続 | 高 | `source--daily-41c3c863b2f45c7b4624` |

BazarCall Campaign

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | Education and Research | Targeting text indicates the Education and Research sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Healthcare | Targeting text indicates the Healthcare sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003 | OS Credential Dumping | [BlackByte](https://attack.mitre.org/groups/G1043) used tools such as [Cobalt Strike](https://attack.mitre.org/software/S0154) and [Mimikatz](https://attack.mitre.org/software/S0002) to dump credentials from victim systems.(Citation: Picus BlackByte 2022)(Citation: Microsoft BlackByte 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1012 | Query Registry | [BlackByte](https://attack.mitre.org/groups/G1043) queried registry values to determine system language settings.(Citation: Picus BlackByte 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | [BlackByte](https://attack.mitre.org/groups/G1043) used tools such as [Arp](https://attack.mitre.org/software/S0099) to pull system network information and identify connected devices.(Citation: FBI BlackByte 2022)(Citation: Microsoft BlackByte 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | [BlackByte](https://attack.mitre.org/groups/G1043) used tools such as [Arp](https://attack.mitre.org/software/S0099) to identify remotely-connected devices.(Citation: FBI BlackByte 2022)(Citation: Picus BlackByte 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | [BlackByte](https://attack.mitre.org/groups/G1043) has used RDP to access other hosts within victim networks.(Citation: Microsoft BlackByte 2023)(Citation: Cisco BlackByte 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | [BlackByte](https://attack.mitre.org/groups/G1043) used SMB file shares to distribute payloads throughout victim networks, including BlackByte ransomware variants during wormable operations.(Citation: Picus BlackByte 2022)(Citation: Microsoft BlackByte 2023)(Citation: Cisco BlackByte 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.008 | Masquerade File Type | [BlackByte](https://attack.mitre.org/groups/G1043) masqueraded configuration files containing encryption keys as PNG files.(Citation: FBI BlackByte 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | [BlackByte](https://attack.mitre.org/groups/G1043) transmitted collected victim host information via HTTP POST to command and control infrastructure.(Citation: Microsoft BlackByte 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1046 | Network Service Discovery | [BlackByte](https://attack.mitre.org/groups/G1043) has used tools such as NetScan to enumerate network services in victim environments.(Citation: Microsoft BlackByte 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | [BlackByte](https://attack.mitre.org/groups/G1043) used WMI to delete Volume Shadow Copies on victim machines.(Citation: FBI BlackByte 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [BlackByte](https://attack.mitre.org/groups/G1043) created scheduled tasks for payload execution.(Citation: FBI BlackByte 2022)(Citation: Picus BlackByte 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055 | Process Injection | [BlackByte](https://attack.mitre.org/groups/G1043) has injected [Cobalt Strike](https://attack.mitre.org/software/S0154) into `wuauclt.exe` during intrusions.(Citation: Picus BlackByte 2022) [BlackByte](https://attack.mitre.org/groups/G1043) has injected ransomware into `svchost.exe` before encryption.(Citation: Symantec BlackByte 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055.012 | Process Hollowing | [BlackByte](https://attack.mitre.org/groups/G1043) used process hollowing for defense evasion purposes.(Citation: Microsoft BlackByte 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [BlackByte](https://attack.mitre.org/groups/G1043) used encoded PowerShell commands during operations.(Citation: FBI BlackByte 2022) [BlackByte](https://attack.mitre.org/groups/G1043) has used remote PowerShell commands in victim networks.(Citation: Microsoft BlackByte 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [BlackByte](https://attack.mitre.org/groups/G1043) executed ransomware using the Windows command shell.(Citation: FBI BlackByte 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1068 | Exploitation for Privilege Escalation | [BlackByte](https://attack.mitre.org/groups/G1043) has exploited CVE-2024-37085 in VMWare ESXi software for authentication bypass and subsequent privilege escalation.(Citation: Cisco BlackByte 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | [BlackByte](https://attack.mitre.org/groups/G1043) deleted ransomware executables post-encryption.(Citation: Picus BlackByte 2022)(Citation: Symantec BlackByte 2022)(Citation: Microsoft BlackByte 2023)(Citation: Cisco BlackByte 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [BlackByte](https://attack.mitre.org/groups/G1043) collected victim device information then transmitted this via HTTP POST to command and control infrastructure.(Citation: Microsoft BlackByte 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [BlackByte](https://attack.mitre.org/groups/G1043) has gained access to victim environments through legitimate VPN credentials.(Citation: Cisco BlackByte 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.002 | Domain Accounts | [BlackByte](https://attack.mitre.org/groups/G1043) captured credentials for or impersonated domain administration users.(Citation: Microsoft BlackByte 2023)(Citation: Cisco BlackByte 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [BlackByte](https://attack.mitre.org/groups/G1043) used various system commands and tools to pull system information during operations.(Citation: FBI BlackByte 2022)(Citation: Symantec BlackByte 2022)(Citation: Microsoft BlackByte 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | [BlackByte](https://attack.mitre.org/groups/G1043) has used tools such as [AdFind](https://attack.mitre.org/software/S0552) to identify and enumerate domain accounts.(Citation: Microsoft BlackByte 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [BlackByte](https://attack.mitre.org/groups/G1043) has transferred tools such as [Cobalt Strike](https://attack.mitre.org/software/S0154) to victim environments from file sharing and hosting websites.(Citation: Microsoft BlackByte 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | [BlackByte](https://attack.mitre.org/groups/G1043) performed Registry modifications to escalate privileges and disable security tools.(Citation: Picus BlackByte 2022)(Citation: Cisco BlackByte 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1134.003 | Make and Impersonate Token | [BlackByte](https://attack.mitre.org/groups/G1043) constructed a valid authentication token following Microsoft Exchange exploitation to allow for follow-on privileged command execution.(Citation: Microsoft BlackByte 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1135 | Network Share Discovery | [BlackByte](https://attack.mitre.org/groups/G1043) enumerated network shares on victim devices.(Citation: Cisco BlackByte 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1136.002 | Domain Account | [BlackByte](https://attack.mitre.org/groups/G1043) created privileged domain accounts during intrusions.(Citation: Cisco BlackByte 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | [BlackByte](https://attack.mitre.org/groups/G1043) has encoded commands in base64-encoded sections concatenated together in PowerShell.(Citation: FBI BlackByte 2022) [BlackByte](https://attack.mitre.org/groups/G1043) uses PowerShell commands to disable Windows Defender.(Citation: Picus BlackByte 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [BlackByte](https://attack.mitre.org/groups/G1043) exploited vulnerabilities such as ProxyLogon and ProxyShell for initial access to victim environments.(Citation: FBI BlackByte 2022)(Citation: Picus BlackByte 2022)(Citation: Symantec BlackByte 2022)(Citation: Microsoft BlackByte 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1219 | Remote Access Tools | [BlackByte](https://attack.mitre.org/groups/G1043) has used tools such as AnyDesk in victim environments.(Citation: Picus BlackByte 2022)(Citation: Microsoft BlackByte 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1480 | Execution Guardrails | [BlackByte](https://attack.mitre.org/groups/G1043) stopped execution if identified language settings on victim machines was Russian or one of several language associated with former Soviet republics.(Citation: Picus BlackByte 2022) [BlackByte](https://attack.mitre.org/groups/G1043) has used ransomware variants requiring a key passed on the command line for the malware to execute.(Citation: Cisco BlackByte 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1482 | Domain Trust Discovery | [BlackByte](https://attack.mitre.org/groups/G1043) enumerated Active Directory information and trust relationships during operations.(Citation: FBI BlackByte 2022)(Citation: Microsoft BlackByte 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1486 | Data Encrypted for Impact | [BlackByte](https://attack.mitre.org/groups/G1043) has encrypted victim files for ransom. Early versions of BlackByte ransomware used a common key for encryption, but later versions use unique keys per victim.(Citation: FBI BlackByte 2022)(Citation: Picus BlackByte 2022)(Citation: Symantec BlackByte 2022)(Citation: Microsoft BlackByte 2023)(Citation: Cisco BlackByte 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1490 | Inhibit System Recovery | [BlackByte](https://attack.mitre.org/groups/G1043) resized and deleted volume shadow copy files to prevent system recovery after encryption.(Citation: Picus BlackByte 2022)(Citation: Symantec BlackByte 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1491.001 | Internal Defacement | [BlackByte](https://attack.mitre.org/groups/G1043) left ransom notes in all directories where encryption takes place.(Citation: FBI BlackByte 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | [BlackByte](https://attack.mitre.org/groups/G1043) has used ASPX web shells following exploitation of vulnerabilities in services such as Microsoft Exchange.(Citation: Picus BlackByte 2022)(Citation: Microsoft BlackByte 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518.001 | Security Software Discovery | [BlackByte](https://attack.mitre.org/groups/G1043) enumerated installed security products during operations.(Citation: Microsoft BlackByte 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | [BlackByte](https://attack.mitre.org/groups/G1043) modified multiple services on victim machines to enable encryption operations.(Citation: Symantec BlackByte 2022) [BlackByte](https://attack.mitre.org/groups/G1043) has installed tools such as AnyDesk as a service on victim machines.(Citation: Microsoft BlackByte 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [BlackByte](https://attack.mitre.org/groups/G1043) has used Registry Run keys for persistence.(Citation: Microsoft BlackByte 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560 | Archive Collected Data | [BlackByte](https://attack.mitre.org/groups/G1043) compressed data collected from victim environments prior to exfiltration.(Citation: Picus BlackByte 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567 | Exfiltration Over Web Service | [BlackByte](https://attack.mitre.org/groups/G1043) has used services such as `anonymfiles.com` and `file.io` to exfiltrate victim data.(Citation: Picus BlackByte 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1569.002 | Service Execution | [BlackByte](https://attack.mitre.org/groups/G1043) created malicious services for ransomware execution.(Citation: Symantec BlackByte 2022)(Citation: Cisco BlackByte 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1570 | Lateral Tool Transfer | [BlackByte](https://attack.mitre.org/groups/G1043) transfered tools such as [Cobalt Strike](https://attack.mitre.org/software/S0154) and the AnyDesk remote access tool during operations using SMB shares.(Citation: Picus BlackByte 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.003 | Virtual Private Server | [BlackByte](https://attack.mitre.org/groups/G1043) staged encryption keys on virtual private servers operated by the adversary.(Citation: FBI BlackByte 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.001 | Upload Malware | [BlackByte](https://attack.mitre.org/groups/G1043) has staged tools such as [Cobalt Strike](https://attack.mitre.org/software/S0154) at public file sharing and hosting sites.(Citation: Microsoft BlackByte 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1614.001 | System Language Discovery | [BlackByte](https://attack.mitre.org/groups/G1043) identified system language settings to determine follow-on execution.(Citation: Picus BlackByte 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | [BlackByte](https://attack.mitre.org/groups/G1043) disabled security tools such as Windows Defender and the Raccine anti-ransomware tool during operations.(Citation: FBI BlackByte 2022)(Citation: Picus BlackByte 2022)(Citation: Cisco BlackByte 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1686 | Disable or Modify System Firewall | [BlackByte](https://attack.mitre.org/groups/G1043) modified firewall rules on victim machines to enable remote system discovery.(Citation: Picus BlackByte 2022)(Citation: Symantec BlackByte 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 6件
- IOC観測: 6件
- 複数攻撃で観測: 0件
- 要レビュー候補: 6件
- 非IOC artifact観測: 494件（`artifacts.csv`）

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
| source--blackbyte--023128303a7231cb | Evil Corp   Behind the Screens |  | 不明 | cybercrime/Evil Corp/Evil Corp - Behind the Screens.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--04d0c44c67d01483 | Biometric vulnerabilities |  | 不明 | cybercrime/2025/Biometric-vulnerabilities.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--07ef30310d8a9e7d | ACSC Annual Cyber Threat Report 2022 |  | 2022 | summary/2022/ACSC-Annual-Cyber-Threat-Report-2022.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--0859043ecdc7e620 | 2022 APT TRENDS INSIGHT REPORT |  | 2022 | summary/2023/2022_APT_TRENDS_INSIGHT_REPORT.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--105214c6a687f0b7 | 2024 Cyber Threat Report Huntress FINAL |  | 2024 | summary/2024/2024_Cyber_Threat_Report_Huntress_FINAL.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--136e24665bade0c2 | Global APT Research Report for the first half of 2021 360 |  | 2021 | summary/2021/Global APT Research Report for the first half of 2021-360.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--1a2b77303e4bea99 | 2024 Threat Intelligence Annual Report |  | 2024 | summary/2025/2024 Threat Intelligence Annual Report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--1a46996a47cb6f47 | Cybersecurity Threats 2024 Annual Report QAX |  | 2024 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--1b19514dc8fd1e37 | Google Cybersecurity Action Team Threat Horizons Report#5 |  | 不明 | summary/2023/Google_Cybersecurity_Action_Team_Threat_Horizons_Report#5.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--1b5beda52edf6e46 | 2021 Vulnerability Landscape |  | 2021 | summary/2022/2021 Vulnerability Landscape.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--1d7ea2e072e7c8c5 | 2024 H1 Threat Intel Report Final |  | 2024 | summary/2024/2024-H1-Threat-Intel-Report-Final.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--1f03d7f5d4698daf | Dragos 2025 OT Cybersecurity Report A Year in Review |  | 2025 | summary/2025/Dragos-2025-OT-Cybersecurity-Report-A-Year-in-Review.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--20d3bf682a71cef5 | 2024 Annual Cybersecurity Vulnerability Threat Landscape Research Report |  | 2024 | summary/2025/2024_Annual_Cybersecurity_Vulnerability_Threat_Landscape_Research_Report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--21508329a3ff9907 | CERTFR 2024 CTI 002 |  | 2024 | summary/2024/CERTFR-2024-CTI-002.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--234d16473c934102 | threat horizons report h1 2025 |  | 2025 | summary/2025/threat_horizons_report_h1_2025.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--25229a8a1676398f | 004 |  | 不明 | summary/UNREDACTEDMagazine/004.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--2531bdc60ffcd4c5 | WEF Global Cybersecurity Outlook 2022 |  | 2022 | summary/2022/WEF_Global_Cybersecurity_Outlook_2022.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--28ca45245928c1b8 | 2025 Cyber Security Report Final |  | 2025 | summary/2025/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--2bba016ee99660b3 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--328e93bac543a0c7 | WhiteCompanyOperationShaheenReport |  | 不明 | WhiteCompany/WhiteCompanyOperationShaheenReport.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--3342a9d815c7ccec | pwc cyber risk reg 2025 |  | 2025 | summary/2024/pwc-cyber-risk-reg-2025.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--343d0951158063d8 | national cyber threat assessment 2025 2026 e |  | 不明 | International Strategic/Canada/national-cyber-threat-assessment-2025-2026-e.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--36f5fa97e72dea27 | UK NCC Group Cyber Threat Intelligence Report September 2025 |  | 2025 | summary/2025/UK_NCC_Group_Cyber_Threat_Intelligence_Report_September_2025_.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--3a81450d404ac198 | 2024 Trustwave Public Sector Threat Landscape |  | 2024 | summary/2024/2024_Trustwave_Public_Sector_Threat_Landscape.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--3d08a0f3c434b28f | IBM X Force Cloud Threat Landscape Report 2024 |  | 2024 | summary/2024/IBM X-Force Cloud Threat Landscape Report 2024.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--3da00c4402289e0d | [RIG] RIG Exploit Kit  In Depth Analysis |  | 不明 | cybercrime/[RIG] RIG Exploit Kit_ In-Depth Analysis.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--4233c3a867420314 | M Trends 2023 Report MANDIANT SPECIAL REPORT |  | 2023 | summary/2023/M-Trends 2023 Report MANDIANT SPECIAL REPORT.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--4333e1ae77e6b5f4 | Global APT Mid 2022 Report qianxin |  | 2022 | summary/2022/Global APT Mid-2022 Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--43ae5f2d8c1ec50a | blackbyte |  | 不明 | actor_profile/evidence/blackbyte.csv | structured-data | TLP:CLEAR | 中 |
| source--blackbyte--44f1f1f1379e6abc | CrowdStrike2023GlobalThreatReport |  | 2023 | summary/2023/CrowdStrike2023GlobalThreatReport.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--4519d4d4c3a5e269 | 003 |  | 不明 | summary/UNREDACTEDMagazine/003.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--46025f4d6c57b235 | Radware Threat Report 2026 RWI 6283 |  | 2026 | summary/2026/Radware_Threat_Report_2026_RWI-6283.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--46b41bae57ee54e7 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--48efe4c6800e09f8 | WEF Global Cybersecurity Outlook 2024 |  | 2024 | summary/2024/WEF_Global_Cybersecurity_Outlook_2024.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--4a77f34b96bd5086 | Bridewell 2026 Cyber Threat Intelligence Report |  | 2026 | summary/2026/Bridewell 2026 Cyber Threat Intelligence Report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--4c0faf2fa0095ed3 | CyberProof 2026 Global Threat Intelligence Report |  | 2026 | summary/2026/CyberProof_2026_Global_Threat_Intelligence_Report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--5000bb73eb73a19a | 2026 state of ai security report |  | 2026 | AISecurity/2026/2026-state-of-ai-security-report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--50578d4c00c58ef1 | 2025 IC3Report |  | 2025 | cybercrime/2026/2025_IC3Report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--50a69be90e568eb9 | eset threat report h22025 |  | 不明 | summary/2025/eset-threat-report-h22025.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--533986a4de0d1c1c | Virtual Routes Pharos Report Series No. 3 |  | 不明 | cybercrime/2025/Virtual-Routes-Pharos-Report-Series-No.-3.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--55d47ed05d4929c3 | 2023 Network Vulnerability Situation Research Report |  | 2023 | summary/2024/2023 Network Vulnerability Situation Research Report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--563c03c3d65a21d2 | Quarterly report 2025 closing |  | 2025 | summary/2025/Quarterly report 2025 closing.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--56b4e6b1a3854906 | 2022 Adversary Infrastructure Report |  | 2022 | summary/2022/2022 Adversary Infrastructure Report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--586330916629a812 | CrowdStrikeGlobalThreatReport2025 |  | 2025 | summary/2025/CrowdStrikeGlobalThreatReport2025.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--5cc066f9c1034c8b | PL Report CP 2024 |  | 2024 | summary/2025/PL_Report_CP_2024.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--5d4c9f292c4f9226 | 2024 security report |  | 2024 | summary/2024/2024-security-report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--5e0910aa378d443e | Unlawful by design Exposing the human rights costs of generative AI |  | 不明 | AISecurity/2026/Unlawful by design-Exposing the human rights costs of generative AI.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--5ee95ec6e13411d5 | Secureworks NC3 2022StateoftheThreat |  | 2022 | summary/2023/Secureworks_NC3_2022StateoftheThreat.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--60bc7e7442b11c74 | Yoroi Cybersecurity Annual Security Report 2020 ENGLISH rMT FINAL 1s |  | 2020 | summary/2021/Yoroi_Cybersecurity_Annual_-Security_Report_2020-ENGLISH_rMT-FINAL-1s.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--613ea991aa386d36 | Searching for Diamonds Cross Domain Opportunities in Cyber Threat Intelligence |  | 不明 | AISecurity/CTI/Searching_for_Diamonds_Cross-Domain_Opportunities_in_Cyber_Threat_Intelligence.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--6204098daffdc917 | 2025 dia statement for the record |  | 2025 | International Strategic/USA/2025/2025_dia_statement_for_the_record.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--62a60b2ebf65e778 | eset threat report h12024 |  | 不明 | summary/2024/eset-threat-report-h12024.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--66be49c4a98d16cc | readme |  | 不明 | summary/2026/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--blackbyte--67d99e8d41d94af9 | 2025 CrowdStrike European Threat Landscape Report |  | 2025 | summary/2025/2025-CrowdStrike-European-Threat-Landscape-Report_.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--6957b48ef8fd2b6b | 2025 Cyber Security Report Final |  | 2025 | summary/2026/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--6a918c4c13a7ced7 | Worldwide Ransomware Attacks as of June 2024 Consistent With Previous Year Sep2024 |  | 2024 | summary/2024/Worldwide_Ransomware_Attacks_as_of_June_2024_Consistent_With_Previous_Year_Sep2024.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--6ba7a18be7ae3061 | MDDR FINAL 2023 1004 |  | 2023-10-04 | summary/2023/MDDR_FINAL_2023_1004.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--6d67ce564cb0c13b | HJS Crypto Currency Report web final |  | 不明 | summary/2026/HJS-Crypto-Currency-Report-web-final.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--6eb538ff71a56bf6 | Public Report EN 2025 DIGITAL |  | 2025 | International Strategic/Canada/Public Report_EN_2025_DIGITAL.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--6fb30c50d1164749 | MIVD Openbaarjaarverslag2024 digitaal 1 1 |  | 2024 | International Strategic/European/MIVD_Openbaarjaarverslag2024_digitaal-1-1.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--710b70b025bc5740 | 200407 MWB COVID White Paper Final |  | 2004-07 | COVID/200407-MWB-COVID-White-Paper_Final.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--726fdfa9dad1912d | cybercrime multifaceted national security threat |  | 不明 | summary/2025/cybercrime-multifaceted-national-security-threat.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--736edf9432ec2135 | Semiannual+Ransomware+Report+ +H1+2024 |  | 2024 | cybercrime/2024/Semiannual+Ransomware+Report+-+H1+2024.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--752ff966d508d7a6 | Cybersecurity Threats 2024 Mid Year Report |  | 2024 | summary/2024/Cybersecurity Threats 2024 Mid-Year Report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--76a7b1e0894441be | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--7748145dcd3a6b11 | Quarterly Adversarial Threat Report Q2 2022 |  | 2022 | bitter/2022/Quarterly-Adversarial-Threat-Report-Q2-2022.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--77da2e7809b2fbc8 | cybersecurity forecast 2025 |  | 2025 | summary/2025/cybersecurity-forecast-2025.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--782d146ea69aed79 | XForce Threat Intelligence 2022 |  | 2022 | summary/2022/XForce_Threat_Intelligence_2022.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--7898b8515fb185ac | positive research 2023 eng |  | 2023 | summary/2023/positive-research-2023-eng.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--79bb111a32093970 | annual threat report 2024 |  | 2024 | summary/2025/annual-threat-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--7a927be0cac27ea1 | 2024 dbir data breach investigations report |  | 2024 | summary/2024/2024-dbir-data-breach-investigations-report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--7aa968307cc4def3 | README |  | 不明 | summary/2023/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--blackbyte--7bc31cc7ecee5ea1 | Cyber Threat Intelligence Report 2025 2 |  | 2025 | summary/2025/Cyber Threat Intelligence Report 2025 2.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--7bfc5194c138c458 | global perspective of the sidewinder apt |  | 不明 | sidewinder/global-perspective-of-the-sidewinder-apt.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--7da6278f5f6ac90b | Microsoft Defending Ukraine Early Lessons from the Cyber War |  | 不明 | summary/2022/Microsoft_Defending Ukraine_Early Lessons from the Cyber War.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--7dd3035c4e961302 | wp cyber threat predictions for 2021 fortinet |  | 2021 | summary/2021/wp-cyber-threat-predictions-for-2021-fortinet.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--80a27174fcba86e0 | Amnesty Cellebrite |  | 不明 | Cellebrite/Amnesty-Cellebrite.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--80ef045aa8ddc7a4 | Microsoft Digital Defense Report 2022 |  | 2022 | summary/2022/Microsoft Digital Defense Report 2022.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--81165326639addce | 2022 Apr Ransomware Report v3 |  | 2022 | summary/2022/2022-Apr-Ransomware-Report-v3.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--82eb46b816febc84 | US24 Manatova Relationships Matter Reconstructing The Organizational Wednesday |  | 不明 | cybercrime/2024/US24-Manatova-Relationships-Matter-Reconstructing-The-Organizational-Wednesday.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--8683d921d7d34b2a | eset threat report h12025 |  | 不明 | summary/2025/eset-threat-report-h12025.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--8dacceed76d312a0 | Report Notes of Cyber inspector |  | 不明 | Anonymous/RussiaUkrainewar/Report_Notes_of_Cyber_inspector_.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--8ea887ac880ed5bd | The CrowdStrike 2021 Global Threat Report |  | 2021 | summary/2021/The CrowdStrike 2021 Global Threat Report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--92e88f4ef58e1b6a | aa24 249a russian military cyber actors target us and global critical infrastructure |  | 不明 | International Strategic/Russia/WhisperGate/aa24-249a-russian-military-cyber-actors-target-us-and-global-critical-infrastructure.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--935280cab13e7ce7 | 2021 Threat Detection Report |  | 2021 | summary/2021/2021-Threat-Detection-Report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--9743fa8e900bb6a8 | readme |  | 不明 | summary/2024/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--blackbyte--98d8ffc3c22b654f | eSentire TRU Report The Industrialization of Cybercrime Identities are Under Attack 2026 |  | 2026 | summary/2026/eSentire_TRU_Report_The-Industrialization-of-Cybercrime-Identities-are-Under-Attack_2026.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--991dbd94316f3650 | 2024 Cloud Security Report CheckPoint Final 1 |  | 2024 | summary/2024/2024-Cloud-Security-Report-CheckPoint Final 1.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--99914a93c0472f3e | 2021(APT) Microsoft Digital Defense Report |  | 2021 | summary/2021/2021(APT) Microsoft Digital Defense Report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--999bae97836325ef | First 6 Half Year Threat Report 2024 |  | 2024 | summary/2024/First 6 Half-Year Threat Report 2024.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--9c2862736f7e2df7 | 360 APT Annual Research Report 2022 |  | 2022 | summary/2023/360_APT_Annual_Research_Report_2022.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--a34a87a33e7589e7 | Norma+Cyber+Annual+Threat+Assessment+ +Spreads |  | 不明 | summary/2024/Norma+Cyber+Annual+Threat+Assessment+-+Spreads.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--a3889d2db5a8dfb2 | National Cybersecurity Strategy 2023 |  | 2023 | International Strategic/USA/2023/National-Cybersecurity-Strategy-2023.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--a566c3dcf2fc3aaa | ACD6 full report |  | 不明 | summary/2023/ACD6-full-report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--a6ecc8d8ca31b692 | GRIT Ransomware Annual Report 2023 |  | 2023 | summary/2024/GRIT_Ransomware_Annual_Report_2023.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--a792b6cdc060faea | ADRN Surveillance Supply Chain Report |  | 不明 | International Strategic/Africa/ADRN_Surveillance_Supply_Chain_Report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--aa6690ec7281b001 | 2025 Global Threat Intelligence Report |  | 2025 | summary/2025/2025 Global Threat Intelligence Report .pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--abd0d0a245b11cc5 | Microsoft Digital Defense Report 2025 |  | 2025 | summary/2025/Microsoft-Digital-Defense-Report-2025.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--ae00de6619852845 | Dragos 2026 OT Cybersecurity Report A Year in Review |  | 2026 | OT/Dragos-2026-OT-Cybersecurity-Report-A-Year-in-Review.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--ae84547c333ea2af | Initial Access Brokers Are Key to Rise in Ransomware Attacks |  | 不明 | summary/2022/Initial_Access_Brokers_Are_Key_to_Rise_in_Ransomware_Attacks.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--aea23b0a3002d1de | quantum threat timeline report 2024 |  | 2024 | summary/2024/quantum-threat-timeline-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--b2a2b758b25e239e | rpt toward a new momentum trend micro security predictions for 2022 |  | 2022 | summary/2022/rpt-toward-a-new-momentum-trend-micro-security-predictions-for-2022.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--b49a1c922b25699c | BD BD 2021 Cybersecurity Annual Report EN |  | 2021 | summary/2022/BD_BD-2021-Cybersecurity-Annual-Report_EN.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--b5dbf67d26cb9ee4 | Global APT 2023 Mid Year Report QIANXIN |  | 2023 | summary/2023/Global APT 2023 Mid-Year Report-QIANXIN.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--b5dcde63bda6d413 | Threat Report 2026 v4 |  | 2026 | summary/2026/Threat Report 2026 v4.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--b6c1f3777edd5b66 | sophos 2022 threat report |  | 2022 | summary/2022/sophos-2022-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--b867d08c17b6bc8d | RedFoxtrot group |  | 不明 | International Strategic/China/RedFoxtrot_group.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--baa5bb0a00ac32a6 | Global APT 2022 Annual Report qianxin |  | 2022 | summary/2023/Global APT 2022 Annual Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--badc566ee011bf3c | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--bb28b5cf74709fa8 | eset threat report h22024 |  | 不明 | summary/2024/eset-threat-report-h22024.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--bb49f1dae2b0028e | sophos 2021 threat report |  | 2021 | summary/2021/sophos-2021-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--bcb2002977e52534 | 2025 Blockchain Security and AML Annual Report |  | 2025 | summary/2025/2025-Blockchain-Security-and-AML-Annual-Report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--bcc2590068751472 | 2022 unit42 incident response report final |  | 2022 | summary/2022/2022-unit42-incident-response-report-final.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--bd5ca984ab758bd8 | Security Navigator 2026 |  | 2026 | summary/2025/Security_Navigator_2026.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--bd9988318c78bba0 | google fog of war research report |  | 不明 | International Strategic/Russia/google_fog_of_war_research_report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--bdd91adfc99fb363 | NSA 2023 CYBERSECURITY YEAR IN REVIEW |  | 2023 | summary/2023/NSA 2023 CYBERSECURITY YEAR IN REVIEW.PDF | report | TLP:CLEAR | 中 |
| source--blackbyte--be92d6293105089f | Disjointed Cyber Warfare Internal Conflicts among |  | 不明 | International Strategic/Russia/Disjointed_Cyber_Warfare_Internal_Conflicts_among_.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--bfdeb912035a69ca | 2021 Advanced Threat Trends Research Report dbappsecurity |  | 2021 | summary/2022/2021 Advanced Threat Trends Research Report-dbappsecurity.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--c0cb77d99237c895 | 2025 dbir data breach investigations report |  | 2025 | summary/2025/2025-dbir-data-breach-investigations-report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--c24cf17ae5857a44 | Threat Hunting with VirusTotal |  | 不明 | APT-hunting/Threat Hunting with VirusTotal.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--c4f2214411aa6bdc | mpressioncss ta report 2020 5 en |  | 2020 | summary/2021/mpressioncss_ta_report_2020_5_en.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--c574eef5b522a392 | 2022 year in retrospect report |  | 2022 | summary/2023/2022-year-in-retrospect-report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--c5f426a150ab9e20 | hunting cobaltstrike beacons in the dark |  | 不明 | APT-hunting/hunting-cobaltstrike-beacons-in-the-dark.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--c7e2d399ad72cf64 | Crypto Crime Report 2023 |  | 2023 | summary/2023/Crypto_Crime_Report_2023.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--cad7b421c89c9d1e | Research Russian Speaking Underground |  | 不明 | cybercrime/2025/Research-Russian_Speaking_Underground.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--cc1e6982a3c8252a | 2024 unit42 incident response report compressed |  | 2024 | summary/2024/2024-unit42-incident-response-report_compressed.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--cdf8a024e299c01c | Microsoft Digital Defense Report 2024 |  | 2024 | summary/2024/Microsoft Digital Defense Report 2024.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--cf1b20e5b51c7687 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--d11b5e5531b9bacf | 2024 Insider Threat Report Securonix final |  | 2024 | summary/2024/2024-Insider-Threat-Report-Securonix-final.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--d4e8dd661d19c7a0 | 2021 Adversary Infrastructure Report |  | 2021 | summary/2022/2021 Adversary Infrastructure Report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--d6ffb8948f809fd8 | 2026 TLP CLEAR NFCERT Cyber Threat Landscape (CTL) Report v1.0 |  | 2026 | summary/2026/2026 TLP_CLEAR NFCERT Cyber Threat Landscape (CTL) Report v1.0.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--d8004b54a41b6b0b | Symantec Ransomware Threat Landscape 2024 |  | 2024 | summary/2024/Symantec_Ransomware_Threat_Landscape_2024.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--da95f73d4f96c1f9 | Qianxin 2023 APT Report |  | 2023 | summary/2024/Qianxin 2023 APT Report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--df3b164bfdc60faa | 2024YiR report |  | 2024 | summary/2025/2024YiR-report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--e0984f20e04a6a40 | state of the threat report 2024 |  | 2024 | summary/2024/state-of-the-threat-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--e52ebf9540d6e23e | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--e63c7c54db4e49b8 | RedReport2023 Picus |  | 2023 | summary/2023/RedReport2023-Picus.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--eb80174b62fce89b | Public Report 2023 eng DIGITAL |  | 2023 | summary/2024/Public_Report_2023-eng-DIGITAL.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--ecc4f8462483bbc4 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--blackbyte--ed7ad638f8412be1 | Google Cybersecurity Action Team Threat Horizons Report#3 |  | 不明 | summary/2022/Google_Cybersecurity_Action_Team_Threat_Horizons_Report#3.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--ee6b35ef9294a0dd | Emotet Exposed A Look Inside the Cybercriminal Supply Chain |  | 不明 | cybercrime/emotet/Emotet_Exposed_A_Look_Inside_the_Cybercriminal_Supply_Chain.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--f00c96c147641193 | rapid7 2024 attack intelligence report |  | 2024 | summary/2024/rapid7_2024_attack_intelligence_report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--f84f39fe01ab895c | Estonian Foreign Intelligence raport 2020 en |  | 2020 | summary/2020/Estonian-Foreign-Intelligence-raport-2020-en.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--f8ed7a8e6a1ffa75 | WizardSpider TLPWHITE v.1.4 |  | 不明 | Wizard Spider/WizardSpider_TLPWHITE_v.1.4.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--fb8301bbf7e57578 | 2022cyberComprehensiveSituationObservationManual |  | 2022 | summary/2023/2022cyberComprehensiveSituationObservationManual.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--fb93ff55b8afe52f | 2021 NCC Group Annual Research Report |  | 2021 | summary/2022/2021-NCC-Group-Annual-Research-Report.pdf | report | TLP:CLEAR | 中 |
| source--blackbyte--ffa13d84eee156bb | CERTFR 2026 CTI 003 |  | 2026 | summary/2026/CERTFR-2026-CTI-003.pdf | report | TLP:CLEAR | 中 |
| source--daily-41c3c863b2f45c7b4624 | BlackByteが新たな脆弱性を活用し攻撃を継続 | blog.talosintelligence.com | 2024-08-29 | https://blog.talosintelligence.com/blackbyte-blends-tried-and-true-tradecraft-with-newly-disclosed-vulnerabilities-to-support-ongoing-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
