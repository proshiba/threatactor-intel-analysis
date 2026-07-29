# DPRK IT Worker Schemes 脅威アクタープロファイル

- プロファイルID: `actor--dprk-it-workers`
- 状態: draft
- 更新日時: 2026-07-25T09:03:53Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

DPRK IT Worker Schemesの標準化プロファイル。リポジトリ内の専用資料8件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **DPRK IT Worker Schemes**
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

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| financial-gain | Financially motivated intrusion or fraud. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

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

- 判定: `no-match`
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
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
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
| Collection | T1005 | Data from Local System | 1 Application Layer Protocol: Web Protocols T1071.001 Application Layer Protocol: File Transfer Protocols T1071.002 Data from Local System T1005 Exfiltration Over C2 Channel T1041 16 CTANK20250213 Recorded Future ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Discovery | T1016 | System Network Configuration Discovery | Use of systeminfo to obtain system information T1016 — System Network Configuration Discovery Use of netspeedtest Google searches for “where is my location”, “where is my ip” T1614 — System Location Discovery Use of netspeedtest Google searches for “where is my location”, “where is my ip” Command and Control T1219 — Remote Access |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--15da1b5bbfbc5250` |
| Stealth | T1027.013 | Encrypted/Encoded File | es: Credentials from Web Browsers T1555.003 User Execution: Malicious File T1204.002 Obfuscated Files or Information: Encrypted/Encoded File T1027.013 File and Directory Discovery T1083 Archive Collected Data: Archive via Utility T1560.001 Application Layer Protocol: Web Protocols T1071.001 Application Layer Protocol: File Transfer Protocols T1071.002 Data from Local System T1005 Exfiltrati |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | rotocols T1071.001 Application Layer Protocol: File Transfer Protocols T1071.002 Data from Local System T1005 Exfiltration Over C2 Channel T1041 16 CTANK20250213 Recorded Future ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Execution | T1059.006 | Python | Initial Access : Spearphishing Attachment T1566.001 Phishing: Spearphishing via Service T1566.003 Command and Scripting Interpreter: Python T1059.006 Command and Scripting Interpreter: JavaScript T1059.007 System Information Discovery T1082 Acquire Infrastructure : Domains T1583.001 Acquire Infrastructure: Server T1583.004 Credentials from Password Stores: Credentials from Web Browsers T1555.00 |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Execution | T1059.007 | JavaScript | ishing: Spearphishing via Service T1566.003 Command and Scripting Interpreter: Python T1059.006 Command and Scripting Interpreter: JavaScript T1059.007 System Information Discovery T1082 Acquire Infrastructure : Domains T1583.001 Acquire Infrastructure: Server T1583.004 Credentials from Password Stores: Credentials from Web Browsers T1555.003 User Execution: Malicious File T1204.002 Obfuscated |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Command And Control | T1071.001 | Web Protocols | 027.013 File and Directory Discovery T1083 Archive Collected Data: Archive via Utility T1560.001 Application Layer Protocol: Web Protocols T1071.001 Application Layer Protocol: File Transfer Protocols T1071.002 Data from Local System T1005 Exfiltration Over C2 Channel T1041 16 CTANK20250213 Recorded Future ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Command And Control | T1071.002 | File Transfer Protocols | Data: Archive via Utility T1560.001 Application Layer Protocol: Web Protocols T1071.001 Application Layer Protocol: File Transfer Protocols T1071.002 Data from Local System T1005 Exfiltration Over C2 Channel T1041 16 CTANK20250213 Recorded Future ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Discovery | T1082 | System Information Discovery | 003 Command and Scripting Interpreter: Python T1059.006 Command and Scripting Interpreter: JavaScript T1059.007 System Information Discovery T1082 Acquire Infrastructure : Domains T1583.001 Acquire Infrastructure: Server T1583.004 Credentials from Password Stores: Credentials from Web Browsers T1555.003 User Execution: Malicious File T1204.002 Obfuscated Files or Information: Encrypted/Encod |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--15da1b5bbfbc5250`, `source--dprk-it-workers--bc62b8e29937a263` |
| Discovery | T1083 | File and Directory Discovery | 003 User Execution: Malicious File T1204.002 Obfuscated Files or Information: Encrypted/Encoded File T1027.013 File and Directory Discovery T1083 Archive Collected Data: Archive via Utility T1560.001 Application Layer Protocol: Web Protocols T1071.001 Application Layer Protocol: File Transfer Protocols T1071.002 Data from Local System T1005 Exfiltration Over C2 Channel T1041 16 |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Command And Control | T1090 | Proxy | Search Engines Mass search for developers on GitHub Initial Access T1566 — Phishing Mass phishing via GitHub pull requests targeting developers Defense Evasion T1090 — Proxy Use of AstrillVPN to hide real location Discovery T1082 — System Information Discovery Use of DXDIAG to obtain system information 2025/12/25 09:52 Smile, You’re on Camera: A Live Stream from Inside Lazarus Group’s IT Workers Scheme \| by ANY.RUN \| Dec, 2025 \| Medium https |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--15da1b5bbfbc5250` |
| Execution | T1204.002 | Malicious File | re Infrastructure: Server T1583.004 Credentials from Password Stores: Credentials from Web Browsers T1555.003 User Execution: Malicious File T1204.002 Obfuscated Files or Information: Encrypted/Encoded File T1027.013 File and Directory Discovery T1083 Archive Collected Data: Archive via Utility T1560.001 Application Layer Protocol: Web Protocols T1071.001 Application Layer Protocol: File Tran |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Command And Control | T1219 | Remote Access Tools | ation”, “where is my ip” T1614 — System Location Discovery Use of netspeedtest Google searches for “where is my location”, “where is my ip” Command and Control T1219 — Remote Access Software Use of AnyDesk Use of Google Remote Desktop T1090 — Proxy Use of AstrillVPN Written by ANY.RUN 185 followers · 2 following Empowering businesses with proactive security solutions: Interactive Sandbox, TI Lookup and Feeds. Sign up: https://app.any.run#reg |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--15da1b5bbfbc5250` |
| Credential Access | T1555.003 | Credentials from Web Browsers | e Infrastructure : Domains T1583.001 Acquire Infrastructure: Server T1583.004 Credentials from Password Stores: Credentials from Web Browsers T1555.003 User Execution: Malicious File T1204.002 Obfuscated Files or Information: Encrypted/Encoded File T1027.013 File and Directory Discovery T1083 Archive Collected Data: Archive via Utility T1560.001 Application Layer Protocol: Web Protocols T1071. |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Collection | T1560.001 | Archive via Utility | cated Files or Information: Encrypted/Encoded File T1027.013 File and Directory Discovery T1083 Archive Collected Data: Archive via Utility T1560.001 Application Layer Protocol: Web Protocols T1071.001 Application Layer Protocol: File Transfer Protocols T1071.002 Data from Local System T1005 Exfiltration Over C2 Channel T1041 16 CTANK20250213 Rec |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Initial Access | T1566 | Phishing | d Pro Vercel Calendly TTPs / ATT&CK Reconnaissance T1593.002 — Search Open Websites/Domains: Search Engines Mass search for developers on GitHub Initial Access T1566 — Phishing Mass phishing via GitHub pull requests targeting developers Defense Evasion T1090 — Proxy Use of AstrillVPN to hide real location Discovery T1082 — System Information Discovery Use of DXDIAG to obtain system information 2025/12/25 09:52 Smile, You’re on Camera: A Live |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--15da1b5bbfbc5250` |
| Initial Access | T1566.001 | Spearphishing Attachment | CYBER THREAT ANALYSIS Appendix C MITRE ATT&CK Techniques Tactic: Technique ATT&CK Code Initial Access : Spearphishing Attachment T1566.001 Phishing: Spearphishing via Service T1566.003 Command and Scripting Interpreter: Python T1059.006 Command and Scripting Interpreter: JavaScript T1059.007 System Information Discovery T1082 Acquire Infrastructure : Domains T1583.001 Acquire Infras |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Initial Access | T1566.003 | Spearphishing via Service | ITRE ATT&CK Techniques Tactic: Technique ATT&CK Code Initial Access : Spearphishing Attachment T1566.001 Phishing: Spearphishing via Service T1566.003 Command and Scripting Interpreter: Python T1059.006 Command and Scripting Interpreter: JavaScript T1059.007 System Information Discovery T1082 Acquire Infrastructure : Domains T1583.001 Acquire Infrastructure: Server T1583.004 Credentials from Pa |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Resource Development | T1583.001 | Domains | Python T1059.006 Command and Scripting Interpreter: JavaScript T1059.007 System Information Discovery T1082 Acquire Infrastructure : Domains T1583.001 Acquire Infrastructure: Server T1583.004 Credentials from Password Stores: Credentials from Web Browsers T1555.003 User Execution: Malicious File T1204.002 Obfuscated Files or Information: Encrypted/Encoded File T1027.013 File and Directory Disc |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Resource Development | T1583.004 | Server | Interpreter: JavaScript T1059.007 System Information Discovery T1082 Acquire Infrastructure : Domains T1583.001 Acquire Infrastructure: Server T1583.004 Credentials from Password Stores: Credentials from Web Browsers T1555.003 User Execution: Malicious File T1204.002 Obfuscated Files or Information: Encrypted/Encoded File T1027.013 File and Directory Discovery T1083 Archive Collected Data: Arch |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--bc62b8e29937a263` |
| Reconnaissance | T1593.002 | Search Engines | Slack Telegram Online platforms: Github LinkedIn ZipRecruiter Bold Pro Vercel Calendly TTPs / ATT&CK Reconnaissance T1593.002 — Search Open Websites/Domains: Search Engines Mass search for developers on GitHub Initial Access T1566 — Phishing Mass phishing via GitHub pull requests targeting developers Defense Evasion T1090 — Proxy Use of AstrillVPN to hide real location Discovery T1082 — System Informat |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--15da1b5bbfbc5250` |
| Discovery | T1614 | System Location Discovery | fo to obtain system information T1016 — System Network Configuration Discovery Use of netspeedtest Google searches for “where is my location”, “where is my ip” T1614 — System Location Discovery Use of netspeedtest Google searches for “where is my location”, “where is my ip” Command and Control T1219 — Remote Access Software Use of AnyDesk Use of Google Remote Desktop T1090 — Proxy Use of AstrillVPN Written by ANY.RUN 185 followers · 2 follow |  |  | 不明 | 不明 | 中 | `source--dprk-it-workers--15da1b5bbfbc5250` |

## IOC／artifact概要

- IOC値: 150件
- IOC観測: 155件
- 複数攻撃で観測: 0件
- 要レビュー候補: 45件
- 非IOC artifact観測: 60件（`artifacts.csv`）

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
| source--dprk-it-workers--94775915798a421c | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | CyberMerceNary/ITWorker/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--dprk-it-workers--b57b6250dea995f1 | DeceptiveDevelopment and North Korean IT workers from primitive crypto theft to sophisticated AI based deception |  | 不明 | CyberMerceNary/ITWorker/DeceptiveDevelopment-and-North-Korean-IT-workers-from-primitive-crypto-theft-to-sophisticated-AI-based-deception.pdf | report | TLP:CLEAR | 中 |
| source--dprk-it-workers--bc62b8e29937a263 | Inside the ScamNorth Korea’s IT Worker Threat |  | 不明 | CyberMerceNary/ITWorker/Inside the ScamNorth Korea’s IT Worker Threat.pdf | report | TLP:CLEAR | 中 |
| source--dprk-it-workers--a08fdc503ef8f9a4 | JOINT CSA DPRK SOCIAL ENGINEERING |  | 不明 | CyberMerceNary/ITWorker/JOINT_CSA_DPRK_SOCIAL_ENGINEERING.pdf | report | TLP:CLEAR | 中 |
| source--dprk-it-workers--e7356e8e649de477 | OFSI Advisory on North Korean IT Workers |  | 不明 | CyberMerceNary/ITWorker/OFSI_Advisory_on_North_Korean_IT_Workers.pdf | report | TLP:CLEAR | 中 |
| source--dprk-it-workers--15da1b5bbfbc5250 | Smile, You’re on Camera  A Live Stream from Inside Lazarus Group’s IT Workers Scheme |  | 不明 | CyberMerceNary/ITWorker/Smile, You’re on Camera_ A Live Stream from Inside Lazarus Group’s IT Workers Scheme.pdf | report | TLP:CLEAR | 中 |
| source--dprk-it-workers--eb29460df938ef81 | north korean scammers are posing as it freelancers here's how you can protect your business |  | 不明 | CyberMerceNary/ITWorker/north-korean-scammers-are-posing-as-it-freelancers_-here's-how-you-can-protect-your-business.pdf | report | TLP:CLEAR | 中 |
| source--dprk-it-workers--769f09c40948bde0 | readme |  | 不明 | CyberMerceNary/ITWorker/readme.md | repository-notes | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
