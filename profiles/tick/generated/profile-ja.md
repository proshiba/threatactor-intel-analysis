# BRONZE BUTLER 脅威アクタープロファイル

- プロファイルID: `actor--tick`
- 状態: draft
- 更新日時: 2026-07-27T11:17:25Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

BRONZE BUTLERの標準化プロファイル。リポジトリ内の専用資料3件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **BRONZE BUTLER**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Tick | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| REDBALDKNIGHT | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) is a cyber espionage group with likely Chinese origins that has been active since at least 2008. The group primarily targets Japanese organizations, particularly those in government, biotechnology, electronics manufacturing, and industrial chemistry.(Citation: Trend Micro Daserf Nov 2017)(Citation: Secureworks BRONZE BUTLER Oct 2017)(Citation: Trend Micro Tick November 2019) |
| Capability | Avenger, down_new, ABK, Daserf, build_downer, ShadowPad, BBK, whoami, procdump, VBS, WCE, PsExec, Gofarer, Datper, ABK Downloader, avirra Downloader, RoyalRoad RTF Weaponizer, Net, at, Windows Credential Editor, Mimikatz, gsecdump, cmd, schtasks |
| Infrastructure |  |
| Victim |  |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Bronze Butler, Tick, RedBaldNight, Stalker Panda | canonical-name | 高 | China | https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses<br>https://blog.trendmicro.com/trendlabs-security-intelligence/redbaldknight-bronze-butler-daserf-backdoor-now-using-steganography/<br>https://unit42.paloaltonetworks.com/unit42-tick-group-continues-attacks/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Swirl Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Tick | canonical-name | 高 | CN, China | https://wikileaks.org/vault7/document/2015-08-20150814-256-CSIR-15005-Stalker-Panda/2015-08-20150814-256-CSIR-15005-Stalker-Panda.pdf<br>https://www.symantec.com/connect/blogs/tick-cyberespionage-group-zeros-japan<br>https://www.secureworks.jp/resources/rp-bronze-butler |
| misp-microsoft-activity-group | Swirl Typhoon | canonical-name | 高 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | BRONZE BUTLER - G0060 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0060<br>http://blog.trendmicro.com/trendlabs-security-intelligence/redbaldknight-bronze-butler-daserf-backdoor-now-using-steganography/<br>https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses |
| misp-mitre-intrusion-set | BRONZE BUTLER - G0060 | mitre-external-id | 高 |  | http://blog.trendmicro.com/trendlabs-security-intelligence/redbaldknight-bronze-butler-daserf-backdoor-now-using-steganography/<br>https://attack.mitre.org/groups/G0060<br>https://documents.trendmicro.com/assets/pdf/Operation-ENDTRADE-TICK-s-Multi-Stage-Backdoors-for-Attacking-Industries-and-Stealing-Classified-Data.pdf |
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
| malware--abk | ABK | [ABK](https://attack.mitre.org/software/S0469) is a downloader that has been used by [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) since at least 2019.(Citation: Trend Micro Tick November 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--abk-downloader | ABK Downloader | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--avenger | Avenger | [Avenger](https://attack.mitre.org/software/S0473) is a downloader that has been used by [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) since at least 2019.(Citation: Trend Micro Tick November 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--avirra-downloader | avirra Downloader | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--bbk | BBK | [BBK](https://attack.mitre.org/software/S0470) is a downloader that has been used by [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) since at least 2019.(Citation: Trend Micro Tick November 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--build-downer | build_downer | [build_downer](https://attack.mitre.org/software/S0471) is a downloader that has been used by [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) since at least 2019.(Citation: Trend Micro Tick November 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--daserf | Daserf | [Daserf](https://attack.mitre.org/software/S0187) is a backdoor that has been used to spy on and steal from Japanese, South Korean, Russian, Singaporean, and Chinese victims. Researchers have identified versions written in both Visual C and Delphi. (Citation: Trend Micro Daserf Nov 2017) (Citation: Secureworks BRONZE BUTLER Oct 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--datper | Datper | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--down-new | down_new |  [down_new](https://attack.mitre.org/software/S0472) is a downloader that has been used by [BRONZE BUTLER](https://attack.mitre.org/groups/G0060) since at least 2019.(Citation: Trend Micro Tick November 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--gofarer | Gofarer | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--procdump | procdump | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--psexec | PsExec | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--royalroad-rtf-weaponizer | RoyalRoad RTF Weaponizer | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--shadowpad | ShadowPad | [ShadowPad](https://attack.mitre.org/software/S0596) is a modular backdoor that was first identified in a supply chain compromise of the NetSarang software in mid-July 2017. The malware was originally thought to be exclusively used by [APT41](https://attack.mitre.org/groups/G0096), but has since been observed to be used by various Chinese threat activity groups. (Citation: Recorded Future RedEcho Feb 2021)(Citation: Securelist ShadowPad Aug 2017)(Citation: Kaspersky ShadowPad Aug 2017)  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--vbs | VBS | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--wce | WCE | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--whoami | whoami | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--at | at | [at](https://attack.mitre.org/software/S0110) is used to schedule tasks on a system to run at a specified date or time.(Citation: TechNet At)(Citation: Linux at) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--windows-credential-editor | Windows Credential Editor | [Windows Credential Editor](https://attack.mitre.org/software/S0005) is a password dumping tool. (Citation: Amplia WCE) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--gsecdump | gsecdump | [gsecdump](https://attack.mitre.org/software/S0008) is a publicly-available credential dumper used to obtain password hashes and LSA secrets from Windows operating systems. (Citation: TrueSec Gsecdump) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--cmd | cmd | [cmd](https://attack.mitre.org/software/S0106) is the Windows command-line interpreter that can be used to interact with systems and execute other processes and utilities. (Citation: TechNet Cmd)<br><br>Cmd.exe contains native functionality to perform many operations to interact with the system, including listing files in a directory (e.g., <code>dir</code> (Citation: TechNet Dir)), deleting files (e.g., <code>del</code> (Citation: TechNet Del)), and copying files (e.g., <code>copy</code> (Citation: TechNet Copy)). | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--schtasks | schtasks | [schtasks](https://attack.mitre.org/software/S0111) is used to schedule execution of programs or scripts on a Windows system to run at a specific date and time. (Citation: TechNet Schtasks) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### インフラ

未確認

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|
| 中国関与のハッカー、Lanscopeの脆弱性をゼロデイで悪用して攻撃 | cyber-espionage | 不明 | 不明 | 2025-11-03 | 中国関与の諜報系グループ「Bronze Butler（Tick）」が、Motex Lanscope Endpoint ManagerのCVE-2025-61932をゼロデイで悪用して情報窃取を実施。 Sophosは2025年中頃からの悪用を観測、ベンダは10月20日に修正を公開し、CISAはKEVに追加して11月12日までのパッチ適用を要請。 欠陥は要求元検証の不備により未認証でSYSTEM権限の任意コード実行が可能となるもので、9.4.7.2以前のクライアントに影響。 攻撃では更新版Gokcpdoorを投下しKCPサポートを廃止、C2多重化通信を実装。OAED Loader経由のDLLサイドローディングやHavocも併用。 侵害後はgoddiやRDP、7-Zipを使い、クラウドストレージ（io、LimeWire、Piping Server等）を流出先として用いた可能性が示唆。 | 中 | `source--daily-a25c503fb0bab44c84b0` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.001 | LSASS Memory | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1007 | System Service Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.001 | Binary Padding | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.003 | Steganography | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036 | Masquerading | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.002 | Right-to-Left Override | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1039 | Data from Network Shared Drive | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.002 | At | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.006 | Python | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1080 | Taint Shared Content | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102.001 | Dead Drop Resolver | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1113 | Screen Capture | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1124 | System Time Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1132.001 | Standard Encoding | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1189 | Drive-by Compromise | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518 | Software Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1548.002 | Bypass User Account Control | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1550.003 | Pass the Ticket | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573.001 | Symmetric Cryptography | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 84件
- IOC観測: 104件
- 複数攻撃で観測: 0件
- 要レビュー候補: 53件
- 非IOC artifact観測: 93件（`artifacts.csv`）

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
| source--daily-a25c503fb0bab44c84b0 | 中国関与のハッカー、Lanscopeの脆弱性をゼロデイで悪用して攻撃 | bleepingcomputer.com | 2025-11-03 | https://www.bleepingcomputer.com/news/security/china-linked-hackers-exploited-lanscope-flaw-as-a-zero-day-in-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--tick--2314f8608742ea50 | D1 COMMSEC   Tick Group   Activities Of The Tick Cyber Espionage Group In East Asia Over The Last 10 Years   Cha Minseok |  | 不明 | tick/D1 COMMSEC - Tick Group - Activities Of The Tick Cyber Espionage Group In East Asia Over The Last 10 Years - Cha Minseok.pdf | report | TLP:CLEAR | 中 |
| source--tick--4f9a9ec6cf4c57e1 | [Analysis Report]Tick Threat Group |  | 不明 | tick/[Analysis_Report]Tick_Threat_Group.pdf | report | TLP:CLEAR | 中 |
| source--tick--76f986f95686e899 | special ioc |  | 不明 | tick/special-ioc.txt | text-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
