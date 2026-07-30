# HEXANE 脅威アクタープロファイル

- プロファイルID: `actor--hexane`
- 状態: draft
- 更新日時: 2026-07-29T23:13:54Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

HEXANEの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **HEXANE**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Lyceum | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Siamesekitten | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Spirlin | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| APT33 | related-to | [HEXANE](https://attack.mitre.org/groups/G1001)'s TTPs appear similar to [APT33](https://attack.mitre.org/groups/G0064) and [OilRig](https://attack.mitre.org/groups/G0049) but due to differences in victims and tools it is tracked as a separate entity.(Citation: Dragos Hexane)(Citation: Kaspersky Lyceum October 2021)(Citation: ClearSky Siamesekitten August 2021)(Citation: Accenture Lyceum Targets November 2021) | 中 | `source--mitre-attack-19-1` |
| APT34 | related-to | [HEXANE](https://attack.mitre.org/groups/G1001)'s TTPs appear similar to [APT33](https://attack.mitre.org/groups/G0064) and [OilRig](https://attack.mitre.org/groups/G0049) but due to differences in victims and tools it is tracked as a separate entity.(Citation: Dragos Hexane)(Citation: Kaspersky Lyceum October 2021)(Citation: ClearSky Siamesekitten August 2021)(Citation: Accenture Lyceum Targets November 2021) | 中 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [HEXANE](https://attack.mitre.org/groups/G1001) is a cyber espionage threat group that has targeted oil & gas, telecommunications, aviation, and internet service provider organizations since at least 2017. Targeted companies have been located in the Middle East and Africa, including Israel, Saudi Arabia, Kuwait, Morocco, and Tunisia. [HEXANE](https://attack.mitre.org/groups/G1001)'s TTPs appear similar to [APT33](https://attack.mitre.org/groups/G0064) and [OilRig](https://attack.mitre.org/groups/G0049) but due to differences in victims and tools it is tracked as a separate entity.(Citation: Dragos Hexane)(Citation: Kaspersky Lyceum October 2021)(Citation: ClearSky Siamesekitten August 2021)(Citation: Accenture Lyceum Targets November 2021) |
| Capability | DnsSystem, Shark, Milan, DanBot, Kevin, DanDrop, Invoke-Obfuscation, PowerShell, ipconfig, Empire, netstat, PoshC2, BITSAdmin, Mimikatz, Ping |
| Infrastructure |  |
| Victim | Middle East, Kuwait, South Africa |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Hexane | canonical-name | 高 | Iran | https://dragos.com/resource/hexane/<br>https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Hexane&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Storm-0133 | canonical-name | 高 | Iran | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | LYCEUM | canonical-name | 高 | IR, Iran (Islamic Republic of) | https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign<br>https://www.secureworks.com/research/threat-profiles/cobalt-lyceum<br>https://www.prevailion.com/latest-targets-of-cyber-group-lyceum/ |
| misp-microsoft-activity-group | Storm-0133 | canonical-name | 高 | IR, Iran | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | HEXANE - G1001 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1001<br>https://dragos.com/resource/hexane/<br>https://vblocalhost.com/uploads/VB2021-Kayal-etal.pdf |
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
| malware--dnssystem | DnsSystem | [DnsSystem](https://attack.mitre.org/software/S1021) is a .NET based DNS backdoor, which is a customized version of the open source tool DIG.net, that has been used by [HEXANE](https://attack.mitre.org/groups/G1001) since at least June 2022.(Citation: Zscaler Lyceum DnsSystem June 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--shark | Shark | [Shark](https://attack.mitre.org/software/S1019) is a backdoor malware written in C# and .NET that is an updated version of [Milan](https://attack.mitre.org/software/S1015); it has been used by [HEXANE](https://attack.mitre.org/groups/G1001) since at least July 2021.(Citation: ClearSky Siamesekitten August 2021)(Citation: Accenture Lyceum Targets November 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--milan | Milan | [Milan](https://attack.mitre.org/software/S1015) is a backdoor implant based on [DanBot](https://attack.mitre.org/software/S1014) that was written in Visual C++ and .NET. [Milan](https://attack.mitre.org/software/S1015) has been used by [HEXANE](https://attack.mitre.org/groups/G1001) since at least June 2020.(Citation: ClearSky Siamesekitten August 2021)(Citation: Kaspersky Lyceum October 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--danbot | DanBot | [DanBot](https://attack.mitre.org/software/S1014) is a first-stage remote access Trojan written in C# that has been used by [HEXANE](https://attack.mitre.org/groups/G1001) since at least 2018.(Citation: SecureWorks August 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--kevin | Kevin | [Kevin](https://attack.mitre.org/software/S1020) is a backdoor implant written in C++ that has been used by [HEXANE](https://attack.mitre.org/groups/G1001) since at least June 2020, including in operations against organizations in Tunisia.(Citation: Kaspersky Lyceum October 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--dandrop | DanDrop | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--invoke-obfuscation | Invoke-Obfuscation | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--powershell | PowerShell | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--ipconfig | ipconfig | [ipconfig](https://attack.mitre.org/software/S0100) is a Windows utility that can be used to find information about a system's TCP/IP, DNS, DHCP, and adapter configuration. (Citation: TechNet Ipconfig) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--empire | Empire | [Empire](https://attack.mitre.org/software/S0363) is an open-source, cross-platform remote administration and post-exploitation framework that is publicly available on GitHub. While the tool itself is primarily written in Python, the post-exploitation agents are written in pure [PowerShell](https://attack.mitre.org/techniques/T1059/001) for Windows and Python for Linux/macOS. [Empire](https://attack.mitre.org/software/S0363) was one of five tools singled out by a joint report on public hacking tools being widely used by adversaries.(Citation: NCSC Joint Report Public Tools)(Citation: Github PowerShell Empire)(Citation: GitHub ATTACK Empire) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--netstat | netstat | [netstat](https://attack.mitre.org/software/S0104) is an operating system utility that displays active TCP connections, listening ports, and network statistics. (Citation: TechNet Netstat) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--poshc2 | PoshC2 | [PoshC2](https://attack.mitre.org/software/S0378) is an open source remote administration and post-exploitation framework that is publicly available on GitHub. The server-side components of the tool are primarily written in Python, while the implants are written in [PowerShell](https://attack.mitre.org/techniques/T1059/001). Although [PoshC2](https://attack.mitre.org/software/S0378) is primarily focused on Windows implantation, it does contain a basic Python dropper for Linux/macOS.(Citation: GitHub PoshC2) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--bitsadmin | BITSAdmin | [BITSAdmin](https://attack.mitre.org/software/S0190) is a command line tool used to create and manage [BITS Jobs](https://attack.mitre.org/techniques/T1197). (Citation: Microsoft BITSAdmin) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--ping | Ping | [Ping](https://attack.mitre.org/software/S0097) is an operating system utility commonly used to troubleshoot and verify network connections. (Citation: TechNet Ping) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| countries | アラブ首長国連邦 | 構造化OSINTの被害国フィールドでHEXANEの標的・被害国としてアラブ首長国連邦が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イスラエル | Targeted companies have been located in the Middle East and Africa, including Israel, Saudi Arabia, Kuwait, Morocco, and Tunisia. | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | クウェート | レビュー済みアクターマッピングの標的欄に記録されたクウェートを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | サウジアラビア | MITRE ATT&CKのGroup概要でHEXANEの標的国として明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| countries | チュニジア | 構造化OSINTの被害国フィールドでHEXANEの標的・被害国としてチュニジアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | モロッコ | 構造化OSINTの被害国フィールドでHEXANEの標的・被害国としてモロッコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 南アフリカ | レビュー済みアクターマッピングの標的欄に記録された南アフリカを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| regions | アフリカ | MITRE ATT&CKのGroup概要でHEXANEの標的範囲としてアフリカが明示されている。 | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards` |
| regions | 中央アジア | 構造化OSINTの被害地域フィールドでHEXANEの標的範囲として中央アジアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 中東 | MITRE ATT&CKのGroup概要でHEXANEの標的範囲として中東が明示されている。 | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 北アフリカ | チュニジア、モロッコで確認された標的・被害事例を北アフリカとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| sectors | 運輸・航空・海運 | [HEXANE](https://attack.mitre.org/groups/G1001) is a cyber espionage threat group that has targeted oil & gas, telecommunications, aviation, and internet service provider organizations since at least 2017. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 情報通信 | [HEXANE](https://attack.mitre.org/groups/G1001) is a cyber espionage threat group that has targeted oil & gas, telecommunications, aviation, and internet service provider organizations since at least 2017. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Discovery | T1010 | Application Window Discovery | [HEXANE](https://attack.mitre.org/groups/G1001) has used a PowerShell-based keylogging tool to capture the window title.(Citation: SecureWorks August 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | [HEXANE](https://attack.mitre.org/groups/G1001) has used [Ping](https://attack.mitre.org/software/S0097) and `tracert` for network discovery.(Citation: Kaspersky Lyceum October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016.001 | Internet Connection Discovery | [HEXANE](https://attack.mitre.org/groups/G1001) has used tools including [BITSAdmin](https://attack.mitre.org/software/S0190) to test internet connectivity from compromised hosts.(Citation: Kaspersky Lyceum October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | [HEXANE](https://attack.mitre.org/groups/G1001) has used `net view` to enumerate domain machines.(Citation: Kaspersky Lyceum October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | [HEXANE](https://attack.mitre.org/groups/G1001) has used remote desktop sessions for lateral movement.(Citation: SecureWorks August 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.010 | Command Obfuscation | [HEXANE](https://attack.mitre.org/groups/G1001) has used Base64-encoded scripts.(Citation: Kaspersky Lyceum October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | [HEXANE](https://attack.mitre.org/groups/G1001) has run `whoami` on compromised machines to identify the current user.(Citation: Kaspersky Lyceum October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | [HEXANE](https://attack.mitre.org/groups/G1001) has used [netstat](https://attack.mitre.org/software/S0104) to monitor connections to specific ports.(Citation: Kaspersky Lyceum October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [HEXANE](https://attack.mitre.org/groups/G1001) has used a scheduled task to establish persistence for a keylogger.(Citation: Kaspersky Lyceum October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056.001 | Keylogging | [HEXANE](https://attack.mitre.org/groups/G1001) has used a PowerShell-based keylogger named `kl.ps1`.(Citation: SecureWorks August 2019)(Citation: Kaspersky Lyceum October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | [HEXANE](https://attack.mitre.org/groups/G1001) has enumerated processes on targeted systems.(Citation: Kaspersky Lyceum October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [HEXANE](https://attack.mitre.org/groups/G1001) has used PowerShell-based tools and scripts for discovery and collection on compromised hosts.(Citation: SecureWorks August 2019)(Citation: Kaspersky APT Trends Q1 April 2021)(Citation: Kaspersky Lyceum October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | [HEXANE](https://attack.mitre.org/groups/G1001) has used a VisualBasic script named `MicrosoftUpdator.vbs` for execution of a PowerShell keylogger.(Citation: Kaspersky Lyceum October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1069.001 | Local Groups | [HEXANE](https://attack.mitre.org/groups/G1001) has run `net localgroup` to enumerate local groups.(Citation: Kaspersky Lyceum October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [HEXANE](https://attack.mitre.org/groups/G1001) has collected the hostname of a compromised machine.(Citation: Kaspersky Lyceum October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102.002 | Bidirectional Communication | [HEXANE](https://attack.mitre.org/groups/G1001) has used cloud services, including OneDrive, for C2.(Citation: Microsoft POLONIUM June 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [HEXANE](https://attack.mitre.org/groups/G1001) has downloaded additional payloads and malicious scripts onto a compromised host.(Citation: Kaspersky Lyceum October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110 | Brute Force | [HEXANE](https://attack.mitre.org/groups/G1001) has used brute force attacks to compromise valid credentials.(Citation: SecureWorks August 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110.003 | Password Spraying | [HEXANE](https://attack.mitre.org/groups/G1001) has used password spraying attacks to obtain valid credentials.(Citation: SecureWorks August 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [HEXANE](https://attack.mitre.org/groups/G1001) has relied on victim's executing malicious file attachments delivered via email or embedded within actor-controlled websites to deliver malware.(Citation: SecureWorks August 2019)(Citation: Dragos Hexane)(Citation: ClearSky Siamesekitten August 2021)(Citation: Zscaler Lyceum DnsSystem June 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518 | Software Discovery | [HEXANE](https://attack.mitre.org/groups/G1001) has enumerated programs installed on an infected machine.(Citation: Kaspersky Lyceum October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1534 | Internal Spearphishing | [HEXANE](https://attack.mitre.org/groups/G1001) has conducted internal spearphishing attacks against executives, HR, and IT personnel to gain information and access.(Citation: SecureWorks August 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1546.003 | Windows Management Instrumentation Event Subscription | [HEXANE](https://attack.mitre.org/groups/G1001) has used WMI event subscriptions for persistence.(Citation: Kaspersky Lyceum October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555 | Credentials from Password Stores | [HEXANE](https://attack.mitre.org/groups/G1001) has run `cmdkey` on victim machines to identify stored credentials.(Citation: Kaspersky Lyceum October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.003 | Credentials from Web Browsers | [HEXANE](https://attack.mitre.org/groups/G1001) has used a [Mimikatz](https://attack.mitre.org/software/S0002)-based tool and a PowerShell script to steal passwords from Google Chrome.(Citation: Kaspersky Lyceum October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | [HEXANE](https://attack.mitre.org/groups/G1001) has used cloud services, including OneDrive, for data exfiltration.(Citation: Microsoft POLONIUM June 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [HEXANE](https://attack.mitre.org/groups/G1001) has registered and operated domains for campaigns, often using a security or web technology theme or impersonating the targeted organization.(Citation: SecureWorks August 2019)(Citation: Dragos Hexane)(Citation: ClearSky Siamesekitten August 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.002 | DNS Server | [HEXANE](https://attack.mitre.org/groups/G1001) has set up custom DNS servers to send commands to compromised hosts via TXT records.(Citation: Zscaler Lyceum DnsSystem June 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.001 | Social Media Accounts | [HEXANE](https://attack.mitre.org/groups/G1001) has established fraudulent LinkedIn accounts impersonating HR department employees to target potential victims with fake job offers.(Citation: ClearSky Siamesekitten August 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.002 | Email Accounts | [HEXANE](https://attack.mitre.org/groups/G1001) has established email accounts for use in domain registration including for ProtonMail addresses.(Citation: Kaspersky Lyceum October 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1586.002 | Email Accounts | [HEXANE](https://attack.mitre.org/groups/G1001) has used compromised accounts to send spearphishing emails.(Citation: SecureWorks August 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [HEXANE](https://attack.mitre.org/groups/G1001) has acquired, and sometimes customized, open source tools such as [Mimikatz](https://attack.mitre.org/software/S0002), [Empire](https://attack.mitre.org/software/S0363), VNC remote access software, and DIG.net.(Citation: Kaspersky Lyceum October 2021)(Citation: SecureWorks August 2019)(Citation: Zscaler Lyceum DnsSystem June 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589 | Gather Victim Identity Information | [HEXANE](https://attack.mitre.org/groups/G1001) has identified specific potential victims at targeted organizations.(Citation: ClearSky Siamesekitten August 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589.002 | Email Addresses | [HEXANE](https://attack.mitre.org/groups/G1001) has targeted executives, human resources staff, and IT personnel for spearphishing.(Citation: SecureWorks August 2019)(Citation: ClearSky Siamesekitten August 2021)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1591.004 | Identify Roles | [HEXANE](https://attack.mitre.org/groups/G1001) has identified executives, HR, and IT staff at victim organizations for further targeting.(Citation: SecureWorks August 2019)(Citation: ClearSky Siamesekitten August 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.001 | Upload Malware | [HEXANE](https://attack.mitre.org/groups/G1001) has staged malware on fraudulent websites set up to impersonate targeted organizations.(Citation: ClearSky Siamesekitten August 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 65件（`artifacts.csv`）

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
| source--hexane--14d1aa1cc96a4a41 | hexane |  | 不明 | actor_profile/evidence/hexane.csv | structured-data | TLP:CLEAR | 中 |
| source--hexane--6639980b85e94b29 | Raport analize Teknikat Taktikat Procedurat per sulmuesit Iraniane |  | 不明 | International Strategic/Iran/Raport-analize-Teknikat-Taktikat-Procedurat-per-sulmuesit-Iraniane.pdf | report | TLP:CLEAR | 中 |
| source--hexane--dfc6468dc65eef04 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--hexane--d8576bf5c5c3b85d | 2021 Advanced Threat Trends Research Report dbappsecurity |  | 2021 | summary/2022/2021 Advanced Threat Trends Research Report-dbappsecurity.pdf | report | TLP:CLEAR | 中 |
| source--hexane--42669933229b53e0 | Global APT Mid 2022 Report qianxin |  | 2022 | summary/2022/Global APT Mid-2022 Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--hexane--8b9cfc6c9306fadd | Microsoft Digital Defense Report 2022 |  | 2022 | summary/2022/Microsoft Digital Defense Report 2022.pdf | report | TLP:CLEAR | 中 |
| source--hexane--3174ee21b5d1ad35 | README |  | 不明 | summary/2022/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--hexane--2574eec8d6dc0c67 | 2022 year in retrospect report |  | 2022 | summary/2023/2022-year-in-retrospect-report.pdf | report | TLP:CLEAR | 中 |
| source--hexane--13f8a7c1987fcb4f | 2022cyberComprehensiveSituationObservationManual |  | 2022 | summary/2023/2022cyberComprehensiveSituationObservationManual.pdf | report | TLP:CLEAR | 中 |
| source--hexane--e0403803d88dee6f | 360 APT Annual Research Report 2022 |  | 2022 | summary/2023/360_APT_Annual_Research_Report_2022.pdf | report | TLP:CLEAR | 中 |
| source--hexane--5eb5dbe5f1db6cc5 | Global APT 2022 Annual Report qianxin |  | 2022 | summary/2023/Global APT 2022 Annual Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--hexane--51a02efdd4cd082d | README |  | 不明 | summary/2023/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--hexane--7cfae430ecc3d56a | Secureworks NC3 2022StateoftheThreat |  | 2022 | summary/2023/Secureworks_NC3_2022StateoftheThreat.pdf | report | TLP:CLEAR | 中 |
| source--hexane--55c31698ec46ab14 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--hexane--f2554596b550b62b | Raport analize PROFILI I GRUPEVE TE HAKERAVE IRANIANE |  | 不明 | summary/2024/Raport-analize-PROFILI-I-GRUPEVE-TE-HAKERAVE-IRANIANE.pdf | report | TLP:CLEAR | 中 |
| source--hexane--337f511d63fb784f | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--hexane--a29bd01d3bfc6a8d | eset apt activity report q4 2024 q1 2025 |  | 2024 | summary/2025/eset-apt-activity-report-q4-2024-q1-2025.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
