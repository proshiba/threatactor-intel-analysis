# INC Ransom 脅威アクタープロファイル

- プロファイルID: `actor--inc-ransom`
- 状態: draft
- 更新日時: 2026-07-27T11:17:23Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

INC Ransomの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **INC Ransom**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| GOLD IONIC | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| Adversary | [INC Ransom](https://attack.mitre.org/groups/G1032) is a ransomware and data extortion threat group associated with the deployment of [INC Ransomware](https://attack.mitre.org/software/S1139) that has been active since at least July 2023. [INC Ransom](https://attack.mitre.org/groups/G1032)  has targeted organizations worldwide most commonly in the industrial, healthcare, and education sectors in the US and Europe.(Citation: Bleeping Computer INC Ransomware March 2024)(Citation: Cybereason INC Ransomware November 2023)(Citation: Secureworks GOLD IONIC April 2024)(Citation: SentinelOne INC Ransomware) |
| Capability | INC Ransomware, Net, Rclone, Nltest, esentutl, Tor, AdFind, PsExec |
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
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | 一致なし |  |  |  |  |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | INC Ransom - G1032 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1032<br>https://www.bleepingcomputer.com/news/security/inc-ransom-threatens-to-leak-3tb-of-nhs-scotland-stolen-data/<br>https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf |
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
| malware--inc-ransomware | INC Ransomware | [INC Ransomware](https://attack.mitre.org/software/S1139) is a ransomware strain that has been used by the [INC Ransom](https://attack.mitre.org/groups/G1032) group since at least 2023 against multiple industry sectors worldwide. [INC Ransomware](https://attack.mitre.org/software/S1139) can employ partial encryption combined with multi-threading to speed encryption.(Citation: SentinelOne INC Ransomware)(Citation: Huntress INC Ransom Group August 2023)(Citation: Secureworks GOLD IONIC April 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--rclone | Rclone | [Rclone](https://attack.mitre.org/software/S1040) is a command line program for syncing files with cloud storage services such as Dropbox, Google Drive, Amazon S3, and MEGA. [Rclone](https://attack.mitre.org/software/S1040) has been used in a number of ransomware campaigns, including those associated with the [Conti](https://attack.mitre.org/software/S0575) and DarkSide Ransomware-as-a-Service operations.(Citation: Rclone)(Citation: Rclone Wars)(Citation: Detecting Rclone)(Citation: DarkSide Ransomware Gang)(Citation: DFIR Conti Bazar Nov 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--nltest | Nltest | [Nltest](https://attack.mitre.org/software/S0359) is a Windows command-line utility used to list domain controllers and enumerate domain trusts.(Citation: Nltest Manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--esentutl | esentutl | [esentutl](https://attack.mitre.org/software/S0404) is a command-line tool that provides database utilities for the Windows Extensible Storage Engine.(Citation: Microsoft Esentutl) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--tor | Tor | [Tor](https://attack.mitre.org/software/S0183) is a software suite and network that provides increased anonymity on the Internet. It creates a multi-hop proxy network and utilizes multilayer encryption to protect both the message and routing information. [Tor](https://attack.mitre.org/software/S0183) utilizes "Onion Routing," in which messages are encrypted with multiple layers of encryption; at each step in the proxy network, the topmost layer is decrypted and the contents forwarded on to the next node until it reaches its destination. (Citation: Dingledine Tor The Second-Generation Onion Router) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|
| 小売大手Ahold Delhaize、220万人に影響するデータ侵害を発表 | ransomware-extortion | 不明 | 不明 | 2025-06-28 | 2024年11月6日のランサムウェア攻撃で米国システムが侵害され、2,242,521人分の情報が盗まれた。 被害情報には氏名、連絡先、生年月日、政府発行ID、銀行口座、医療・雇用記録などが含まれる。 ランサムウェアグループINC Ransomが攻撃を主張し、4月にダークウェブで資料の一部を流出させた。 同社は顧客支払い・薬局システムへの影響やクレジットカード情報の流出は確認されていないと説明。 現在も調査中で、攻撃グループ名や暗号化の有無は正式には公表されていない。 | 中 | `source--daily-48e62c0cd488e280d1f7` |
| McLaren病院、ランサムウェア攻撃による混乱が発生 | ransomware-extortion | 不明 | 不明 | 2024-08-08 | McLaren Health CareのITおよび電話システムがランサムウェア攻撃を受けて混乱。 同病院はインシデントの詳細を明らかにしていないが、職員が身代金要求メモを共有。 攻撃者はINC Ransomであり、システムが暗号化されデータが盗まれた。窃取されたデータは身代金を支払わなければ公開すると恐喝。 同病院は患者のデータベースアクセスを失い、一部の予約や手術が延期された。 2023年7月のデータ侵害でも個人情報が漏洩していた。 | 中 | `source--daily-8c1dbec2ef693d083aa2` |
| INC Ransom、NHSスコットランドから盗まれた3TBのデータを漏洩させると脅迫 | ransomware-extortion | 不明 | 不明 | 2024-03-28 | INC RansomがNHSスコットランドから盗んだ3TBのデータの公開を脅迫 医療情報が含まれる複数の画像を共有し、身代金の支払いがなければ公開すると警告 攻撃はNHSスコットランドを構成する地域保健委員会のうち、NHSダムフリーズ・アンド・ガロウェイに限定され、他に影響なし 政府は警察などと共に影響の評価と、影響を受けた可能性のある個人について調査中 NHSダムフリーズ・アンド・ガロウェイは患者データの一部が漏洩したことを確認 | 高 | `source--daily-bab6b26b5c9d46e2d3fa` |
| ペンシルベニア州司法長官室、INC Ransom攻撃後のデータ侵害を確認 | ransomware-extortion | 不明 | 不明 | 2025-11-18 | ペンシルベニア州司法長官室は、8月9日のランサム攻撃で個人・医療情報を含むファイルが不正アクセスされたと確認。 当局は身代金支払いを拒否。調査で氏名・社会保障番号・医療情報が含まれ得ると発表。 攻撃当日はウェブサイト、職員メール、固定電話が停止する深刻な影響。侵入経路の詳細は未公表。 専門家は公開Citrix NetScalerの重大欠陥（CVE-2025-5777／Citrix Bleed 2）悪用の可能性を指摘するが確証はない。 INC Ransomが9月20日に犯行声明と5.7TB窃取を主張、FBI内部網へのアクセス示唆もあるが、当局は公式帰属を示さず。 | 高 | `source--daily-3d064f91540dd031b11b` |
| OnSolveのCodeREDへのサイバー攻撃で全米の緊急警報システムが障害 | ransomware-extortion | 不明 | 不明 | 2025-11-27 | 危機管理企業Crisis24は、OnSolve CodeREDが受けたサイバー攻撃で、全米の自治体・警察・消防の緊急通知に障害が出たと確認。 旧CodeRED環境の廃止を余儀なくされ、緊急・天候アラート等の配信が広範に中断。被害は他システムには拡大していないと説明。 氏名・住所・メール・電話番号・CodeREDプロファイル用パスワードの窃取を確認、ただし現時点で公開流出の証拠はない。 2025年3月31日バックアップから新「CodeRED by Crisis24」へ復旧中で、古いバックアップのため一部アカウント欠落の恐れ。 INC Ransomが犯行声明を出し、11月1日侵入・10日暗号化と主張。平文パスワードの画面を提示し、再利用パスの変更を注意喚起。 | 中 | `source--daily-b7b8f180017c90aab0b8` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Lateral Movement | T1021.001 | Remote Desktop Protocol | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1046 | Network Service Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1069.002 | Domain Groups | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071 | Application Layer Protocol | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074 | Data Staged | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1135 | Network Share Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1219 | Remote Access Tools | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1486 | Data Encrypted for Impact | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1537 | Transfer Data to Cloud Account | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566 | Phishing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1569.002 | Service Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1570 | Lateral Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1657 | Financial Theft | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 3件
- IOC観測: 4件
- 複数攻撃で観測: 0件
- 要レビュー候補: 3件
- 非IOC artifact観測: 25件（`artifacts.csv`）

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
| source--daily-3d064f91540dd031b11b | ペンシルベニア州司法長官室、INC Ransom攻撃後のデータ侵害を確認 | bleepingcomputer.com | 2025-11-18 | https://www.bleepingcomputer.com/news/security/pennsylvania-ag-confirms-data-breach-after-inc-ransom-attack/ | osint-report | TLP:CLEAR | 中 |
| source--daily-48e62c0cd488e280d1f7 | 小売大手Ahold Delhaize、220万人に影響するデータ侵害を発表 | bleepingcomputer.com | 2025-06-28 | https://www.bleepingcomputer.com/news/security/retail-giant-ahold-delhaize-says-data-breach-affects-22-million-people/ | osint-report | TLP:CLEAR | 中 |
| source--daily-8c1dbec2ef693d083aa2 | McLaren病院、ランサムウェア攻撃による混乱が発生 | bleepingcomputer.com | 2024-08-08 | https://www.bleepingcomputer.com/news/security/mclaren-hospitals-disruption-linked-to-inc-ransomware-attack/ | osint-report | TLP:CLEAR | 中 |
| source--daily-b7b8f180017c90aab0b8 | OnSolveのCodeREDへのサイバー攻撃で全米の緊急警報システムが障害 | bleepingcomputer.com | 2025-11-27 | https://www.bleepingcomputer.com/news/security/onsolve-codered-cyberattack-disrupts-emergency-alert-systems-nationwide/ | osint-report | TLP:CLEAR | 中 |
| source--daily-bab6b26b5c9d46e2d3fa | INC Ransom、NHSスコットランドから盗まれた3TBのデータを漏洩させると脅迫 | bleepingcomputer.com | 2024-03-28 | https://www.bleepingcomputer.com/news/security/inc-ransom-threatens-to-leak-3tb-of-nhs-scotland-stolen-data/ | osint-report | TLP:CLEAR | 中 |
| source--inc-ransom--069751c4f5330eee | Cybersecurity Threats 2024 Annual Report QAX |  | 2024 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | report | TLP:CLEAR | 中 |
| source--inc-ransom--1a3fc64db990b21d | Dragos 2025 OT Cybersecurity Report A Year in Review |  | 2025 | summary/2025/Dragos-2025-OT-Cybersecurity-Report-A-Year-in-Review.pdf | report | TLP:CLEAR | 中 |
| source--inc-ransom--1e1d7f3f5eb46d2d | Threat Report 2026 v4 |  | 2026 | summary/2026/Threat Report 2026 v4.pdf | report | TLP:CLEAR | 中 |
| source--inc-ransom--1f3cfbbe42c86b5d | 2023 Network Vulnerability Situation Research Report |  | 2023 | summary/2024/2023 Network Vulnerability Situation Research Report.pdf | report | TLP:CLEAR | 中 |
| source--inc-ransom--283a307c00034b17 | 2024YiR report |  | 2024 | summary/2025/2024YiR-report.pdf | report | TLP:CLEAR | 中 |
| source--inc-ransom--2eceb2754c9cb02c | state of the threat report 2024 |  | 2024 | summary/2024/state-of-the-threat-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--inc-ransom--31b038e2306c372e | CERTFR 2026 CTI 003 |  | 2026 | summary/2026/CERTFR-2026-CTI-003.pdf | report | TLP:CLEAR | 中 |
| source--inc-ransom--43b2a83e2bc03040 | 2025 Cyber Security Report Final |  | 2025 | summary/2025/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--inc-ransom--6e731e9ccd7210cf | 2024 Threat Intelligence Annual Report |  | 2024 | summary/2025/2024 Threat Intelligence Annual Report.pdf | report | TLP:CLEAR | 中 |
| source--inc-ransom--88c4703493142d0c | 2024 security report |  | 2024 | summary/2024/2024-security-report.pdf | report | TLP:CLEAR | 中 |
| source--inc-ransom--a896ec3581dafe21 | 2025 Cyber Security Report Final |  | 2025 | summary/2026/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--inc-ransom--a9194f09607a029e | Dragos 2026 OT Cybersecurity Report A Year in Review |  | 2026 | OT/Dragos-2026-OT-Cybersecurity-Report-A-Year-in-Review.pdf | report | TLP:CLEAR | 中 |
| source--inc-ransom--b8cf8899ce262e9f | UK NCC Group Cyber Threat Intelligence Report September 2025 |  | 2025 | summary/2025/UK_NCC_Group_Cyber_Threat_Intelligence_Report_September_2025_.pdf | report | TLP:CLEAR | 中 |
| source--inc-ransom--e2541b1d09c015cc | Cybersecurity Threats 2024 Mid Year Report |  | 2024 | summary/2024/Cybersecurity Threats 2024 Mid-Year Report.pdf | report | TLP:CLEAR | 中 |
| source--inc-ransom--f97bf4e5f6496290 | inc ransom |  | 不明 | actor_profile/evidence/inc-ransom.csv | structured-data | TLP:CLEAR | 中 |
| source--inc-ransom--f9e580a1429debcd | [Report] Bitsight State of the Underground 2026 |  | 2026 | summary/2026/[Report] Bitsight State of the Underground 2026.pdf | report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
