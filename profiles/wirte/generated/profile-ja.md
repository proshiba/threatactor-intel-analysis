# WIRTE 脅威アクタープロファイル

- プロファイルID: `actor--wirte`
- 状態: draft
- 更新日時: 2026-07-29T23:13:55Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

WIRTEの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **WIRTE**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Ashen Lepus | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Group WITRE | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| Adversary | [WIRTE](https://attack.mitre.org/groups/G0090) is a cyberespionage actor, believed to be a subgroup of the Hamas-affiliated Gaza Cybergang, that has been active since at least August 2018. [WIRTE](https://attack.mitre.org/groups/G0090) has targeted diplomatic, financial, military, legal, and technology organizations across the Middle East, North Africa, and in Europe to gather intelligence. [WIRTE](https://attack.mitre.org/groups/G0090) has remained persistently active despite the ongoing Israel-Hamas conflict and has expanded their operations to include wiper malware attacks against Israeli targets.(Citation: Lab52 WIRTE Apr 2019)(Citation: Kaspersky WIRTE November 2021)(Citation: Check Point Wirte NOV 2024)(Citation: Palo Alto Ashen Lepus DEC 2025) |
| Capability | IronWind, Havoc, SameCoin, Ferocious, LitePower, AshTag, Empire, Rclone |
| Infrastructure |  |
| Victim | people from the Palestinian authority and UAE |
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
| misp-threat-actor | WIRTE | canonical-name | 高 | PS | https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044/<br>https://lab52.io/blog/wirte-group-attacking-the-middle-east/<br>https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | WIRTE - G0090 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0090<br>https://lab52.io/blog/wirte-group-attacking-the-middle-east/<br>https://research.checkpoint.com/2024/hamas-affiliated-threat-actor-expands-to-disruptive-activity/ |
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
| malware--ironwind | IronWind | [IronWind](https://attack.mitre.org/software/S9029) is a custom loader malware that has been in use since at least 2023 by actors including [WIRTE](https://attack.mitre.org/groups/G0090) to target entities in the Middle East.(Citation: Check Point Wirte NOV 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--havoc | Havoc | [Havoc](https://attack.mitre.org/software/S1229) is an open-source post-exploitation command and control (C2) framework first released on GitHub in October 2022 by C5pider (Paul Ungur), who continues to maintain and develop it with community contributors. [Havoc](https://attack.mitre.org/software/S1229) provides a wide range of offensive security capabilities and has been adopted by multiple threat actors to establish and maintain control over compromised systems. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--samecoin | SameCoin | [SameCoin](https://attack.mitre.org/software/S9030) is a multi-platform wiper with Windows and Android versions that has been used by [WIRTE](https://attack.mitre.org/groups/G0090) to target entities in the Middle East including in Israel.(Citation: Check Point Wirte NOV 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--ferocious | Ferocious | [Ferocious](https://attack.mitre.org/software/S0679) is a first stage implant composed of VBS and PowerShell scripts that has been used by [WIRTE](https://attack.mitre.org/groups/G0090) since at least 2021.(Citation: Kaspersky WIRTE November 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--litepower | LitePower | [LitePower](https://attack.mitre.org/software/S0680) is a downloader and second stage malware that has been used by [WIRTE](https://attack.mitre.org/groups/G0090) since at least 2021.(Citation: Kaspersky WIRTE November 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--ashtag | AshTag | [AshTag](https://attack.mitre.org/software/S9031) is a modular .NET backdoor with multiple features that has been used by [WIRTE](https://attack.mitre.org/groups/G0090) since at least 2025. [AshTag](https://attack.mitre.org/software/S9031) is designed for persistence and remote command execution and can masquerade as a legitimate VisualServer utility.(Citation: Palo Alto Ashen Lepus DEC 2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--empire | Empire | [Empire](https://attack.mitre.org/software/S0363) is an open-source, cross-platform remote administration and post-exploitation framework that is publicly available on GitHub. While the tool itself is primarily written in Python, the post-exploitation agents are written in pure [PowerShell](https://attack.mitre.org/techniques/T1059/001) for Windows and Python for Linux/macOS. [Empire](https://attack.mitre.org/software/S0363) was one of five tools singled out by a joint report on public hacking tools being widely used by adversaries.(Citation: NCSC Joint Report Public Tools)(Citation: Github PowerShell Empire)(Citation: GitHub ATTACK Empire) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--rclone | Rclone | [Rclone](https://attack.mitre.org/software/S1040) is a command line program for syncing files with cloud storage services such as Dropbox, Google Drive, Amazon S3, and MEGA. [Rclone](https://attack.mitre.org/software/S1040) has been used in a number of ransomware campaigns, including those associated with the [Conti](https://attack.mitre.org/software/S0575) and DarkSide Ransomware-as-a-Service operations.(Citation: Rclone)(Citation: Rclone Wars)(Citation: Detecting Rclone)(Citation: DarkSide Ransomware Gang)(Citation: DFIR Conti Bazar Nov 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| countries | アラブ首長国連邦 | レビュー済みアクターマッピングの標的欄に記録されたアラブ首長国連邦を構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | イスラエル | [WIRTE](https://attack.mitre.org/groups/G0090) has remained persistently active despite the ongoing Israel-Hamas conflict and has expanded their operations to include wiper malware attacks against Israeli targets.(Citation: Lab52 WIRTE Apr 2019)(Citation: Kaspersky WIRTE November 2021)(Citation: Check Point Wirte NOV 2024)(Citation: Palo Alto Ashen Lepus DEC 2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| countries | パレスチナ | レビュー済みアクターマッピングの標的欄に記録されたパレスチナを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| regions | アフリカ | MITRE ATT&CKのGroup概要でWIRTEの標的範囲としてアフリカが明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| regions | 中東 | MITRE ATT&CKのGroup概要でWIRTEの標的範囲として中東が明示されている。 | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1` |
| regions | 北アフリカ | MITRE ATT&CKのGroup概要でWIRTEの標的範囲として北アフリカが明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 非営利・市民社会 | [WIRTE](https://attack.mitre.org/groups/G0090) has remained persistently active despite the ongoing Israel-Hamas conflict and has expanded their operations to include wiper malware attacks against Israeli targets.(Citation: Lab52 WIRTE Apr 2019)(Citation: Kaspersky WIRTE November 2021)(Citation: Check Point Wirte NOV 2024)(Citation: Palo Alto Ashen Lepus | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 金融 | [WIRTE](https://attack.mitre.org/groups/G0090) has targeted diplomatic, financial, military, legal, and technology organizations across the Middle East, North Africa, and in Europe to gather intelligence. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 防衛・軍事 | [WIRTE](https://attack.mitre.org/groups/G0090) has targeted diplomatic, financial, military, legal, and technology organizations across the Middle East, North Africa, and in Europe to gather intelligence. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 政府・行政 | [WIRTE](https://attack.mitre.org/groups/G0090) has targeted diplomatic, financial, military, legal, and technology organizations across the Middle East, North Africa, and in Europe to gather intelligence. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1027.010 | Command Obfuscation | [WIRTE](https://attack.mitre.org/groups/G0090) has XOR encrypted command line strings to conceal malware execution chains.(Citation: Check Point Wirte NOV 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.015 | Compression | [WIRTE](https://attack.mitre.org/groups/G0090) has compressed malicious files within RAR and ZIP archives for obfuscation.  (Citation: Check Point Wirte NOV 2024)(Citation: Palo Alto Ashen Lepus DEC 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [WIRTE](https://attack.mitre.org/groups/G0090) has used security service provider naming conventions such as ESET and Kasperky ("Kaspersky Update Agent") in order to appear legitimate.(Citation: Kaspersky WIRTE November 2021)(Citation: Check Point Wirte NOV 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | [WIRTE](https://attack.mitre.org/groups/G0090) has exfiltrated collected victim data to C2 infrastructure.(Citation: Palo Alto Ashen Lepus DEC 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [WIRTE](https://attack.mitre.org/groups/G0090) has used PowerShell for script execution.(Citation: Lab52 WIRTE Apr 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [WIRTE](https://attack.mitre.org/groups/G0090) has used the Windows command line as part of infection chains to open documents.(Citation: Check Point Wirte NOV 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | [WIRTE](https://attack.mitre.org/groups/G0090) has used VBScript  in its operations.(Citation: Lab52 WIRTE Apr 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [WIRTE](https://attack.mitre.org/groups/G0090) has used HTTP for network communication.(Citation: Lab52 WIRTE Apr 2019)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | [WIRTE](https://attack.mitre.org/groups/G0090) has staged collected documents of interest in `C:\Users\Public folder`.(Citation: Palo Alto Ashen Lepus DEC 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [WIRTE](https://attack.mitre.org/groups/G0090) has downloaded PowerShell code from the C2 server to be executed.(Citation: Lab52 WIRTE Apr 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1106 | Native API | [WIRTE](https://attack.mitre.org/groups/G0090) has used the `RtlIpv4StringToAddressA` to convert IP-formatted string to a byte array.(Citation: Check Point Wirte NOV 2024)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114.001 | Local Email Collection | [WIRTE](https://attack.mitre.org/groups/G0090) has collected documents from victims' email accounts.(Citation: Palo Alto Ashen Lepus DEC 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | [WIRTE](https://attack.mitre.org/groups/G0090) has used Base64 to decode malicious VBS script.(Citation: Lab52 WIRTE Apr 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | [WIRTE](https://attack.mitre.org/groups/G0090) has used links embedded in emails to lure users into downloading malicious files.(Citation: Check Point Wirte NOV 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [WIRTE](https://attack.mitre.org/groups/G0090) has attempted to lure users into opening malicious documents including MS Word and Excel files, at times using a decoy document to encourage execution of malicious payloads.(Citation: Kaspersky WIRTE November 2021)(Citation: Check Point Wirte NOV 2024)(Citation: Palo Alto Ashen Lepus DEC 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.010 | Regsvr32 | [WIRTE](https://attack.mitre.org/groups/G0090) has used `regsvr32.exe` to trigger the execution of a malicious script.(Citation: Lab52 WIRTE Apr 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery, Stealth | T1497.001 | System Checks | [WIRTE](https://attack.mitre.org/groups/G0090) has configured C2 servers to check location and user-agent strings for victim endpoints to prevent sending a payload to sandboxed environments.(Citation: Palo Alto Ashen Lepus DEC 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [WIRTE](https://attack.mitre.org/groups/G0090) has sent emails to intended victims with malicious MS Word and Excel attachments.(Citation: Kaspersky WIRTE November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | [WIRTE](https://attack.mitre.org/groups/G0090) has sent targeted spearphishing emails with malicious links directing victims to malware downloads.(Citation: Check Point Wirte NOV 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1571 | Non-Standard Port | [WIRTE](https://attack.mitre.org/groups/G0090) has used HTTPS over ports 2083 and 2087 for C2.(Citation: Kaspersky WIRTE November 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | [WIRTE](https://attack.mitre.org/groups/G0090) has used RAR archives containing a legitimate executable and a lure document to execute malicious DLLs via sideloading.(Citation: Check Point Wirte NOV 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [WIRTE](https://attack.mitre.org/groups/G0090) has registered domains designed to mimic legitimate sites for use in phishing campaigns.(Citation: Check Point Wirte NOV 2024)(Citation: Palo Alto Ashen Lepus DEC 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1586.002 | Email Accounts | [WIRTE](https://attack.mitre.org/groups/G0090) has used compromised emails, including one belonging to an Israel-based technology reseller, to deliver targeted spearphishing messages.(Citation: Check Point Wirte NOV 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [WIRTE](https://attack.mitre.org/groups/G0090) has obtained and used [Empire](https://attack.mitre.org/software/S0363) and [Rclone](https://attack.mitre.org/software/S1040) for post-exploitation activities.(Citation: Lab52 WIRTE Apr 2019)(Citation: Palo Alto Ashen Lepus DEC 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.001 | Upload Malware | [WIRTE](https://attack.mitre.org/groups/G0090) has directed victims to malicious payloads staged on file sharing services.(Citation: Palo Alto Ashen Lepus DEC 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1684.001 | Impersonation | [WIRTE](https://attack.mitre.org/groups/G0090) has used utilized look-alike domains and graphics of trusted security solution providers to entice victims to click on phishing links.(Citation: Check Point Wirte NOV 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 2件
- IOC観測: 3件
- 複数攻撃で観測: 0件
- 要レビュー候補: 2件
- 非IOC artifact観測: 31件（`artifacts.csv`）

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
| source--wirte--d744931b7e0f9e59 | wirte |  | 不明 | actor_profile/evidence/wirte.csv | structured-data | TLP:CLEAR | 中 |
| source--wirte--823d2688088451e5 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--wirte--1ac9b2680803cf77 | 2022 year in retrospect report |  | 2022 | summary/2023/2022-year-in-retrospect-report.pdf | report | TLP:CLEAR | 中 |
| source--wirte--b93b35413dfc6e57 | 2022cyberComprehensiveSituationObservationManual |  | 2022 | summary/2023/2022cyberComprehensiveSituationObservationManual.pdf | report | TLP:CLEAR | 中 |
| source--wirte--d38296cb0fed57a8 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--wirte--e17f32c5942fb8db | state of the threat report 2024 |  | 2024 | summary/2024/state-of-the-threat-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--wirte--664111734df1e646 | 2024 Malicious Infrastructure Report |  | 2024 | summary/2025/2024 Malicious Infrastructure Report.pdf | report | TLP:CLEAR | 中 |
| source--wirte--9b2782a4378687f7 | 2025 Cyber Security Report Final |  | 2025 | summary/2025/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--wirte--902b09a62b32d980 | Cybersecurity Threats 2024 Annual Report QAX |  | 2024 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | report | TLP:CLEAR | 中 |
| source--wirte--01dab65cafb63414 | 2025 Cyber Security Report Final |  | 2025 | summary/2026/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
