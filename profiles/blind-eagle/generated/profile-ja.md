# Blind Eagle 脅威アクタープロファイル

- プロファイルID: `actor--blind-eagle`
- 状態: draft
- 更新日時: 2026-07-25T14:07:08Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Blind Eagleの標準化プロファイル。リポジトリ内の専用資料3件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Blind Eagle**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| APT-C-36 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| APT-Q-98 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| AguilaCiega | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TAG-144 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| South America | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 62; mapping requires review. |

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
| Adversary | [APT-C-36](https://attack.mitre.org/groups/G0099) is a suspected South American threat group that has engaged in espionage and financially motivated operations since at least 2018. [APT-C-36](https://attack.mitre.org/groups/G0099) has targeted government institutions and entities in the financial, energy, and professional manufacturing sectors across Colombia and other Latin American countries.(Citation: QiAnXin APT-C-36 Feb2019)(Citation: Kaspersky BlindEagle AUG 2024)(Citation: Check Point Blind Eagle MAR 2025)(Citation: Recorded Future TAG-144 AUG 2025) |
| Capability | HeartCrypt, PureCrypter, Caminho, njRAT, Imminent RAT, DCRAT, AsyncRAT, Remcos, Imminent Monitor, QuasarRAT |
| Infrastructure |  |
| Victim | Colombian government institutions |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Blind Eagle | canonical-name | 高 | Colombia | https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/<br>https://threatmon.io/apt-blind-eagles-malware-arsenal-technical-analysis/<br>https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/tracing-blind-eagle-to-proton66/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | APT-C-36 | canonical-name | 高 |  | https://ti.360.net/blog/articles/apt-c-36-continuous-attacks-targeting-colombian-government-institutions-and-corporations-en/<br>https://www.ecucert.gob.ec/wp-content/uploads/2022/03/alerta-APTs-2022-03-23.pdf<br>https://blogs.blackberry.com/en/2023/02/blind-eagle-apt-c-36-targets-colombia |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | APT-C-36 - G0099 | mitre-external-id | 高 |  | https://assets.recordedfuture.com/insikt-report-pdfs/2025/cta-2025-0826.pdf<br>https://attack.mitre.org/groups/G0099<br>https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/ |
| misp-360net | 盲眼鹰 - APT-C-36 | single-alias-intersection | 中 | namerica | https://apt.360.net/report/apts/83.html |

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
| malware--heartcrypt | HeartCrypt | [HeartCrypt](https://attack.mitre.org/software/S9018) is a packer-as-a-service (PaaS) used to protect malware that has been available since at least 2024. [HeartCrypt](https://attack.mitre.org/software/S9018) has been used to pack a variety of malware including [Lumma Stealer](https://attack.mitre.org/software/S1213), [Remcos](https://attack.mitre.org/software/S0332), and Rhadamanthys. In the [HeartCrypt](https://attack.mitre.org/software/S9018) PaaS model, customers submit malware via private messaging services and it is then packed and returned by the operator as a new binary.(Citation: Palo Alto HeartCrypt DEC 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--purecrypter | PureCrypter | PureCrypter is a fully-featured malware loader, developed by a threat actor called “PureCoder," that has been in use since at least 2021 to distribute a variety of remote access trojans and information stealers.(Citation: Zscaler PureCrypter JUN 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--caminho | Caminho | [Caminho](https://attack.mitre.org/software/S9016) is a downloader that has been used by threat actors since at least 2025 to deliver various strains of malware such as XWorm.(Citation: Zscaler BlindEagle DEC 2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--njrat | njRAT | [njRAT](https://attack.mitre.org/software/S0385) is a remote access tool (RAT) that was first observed in 2012. It has been used by threat actors in the Middle East.(Citation: Fidelis njRAT June 2013) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--imminent-rat | Imminent RAT | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--dcrat | DCRAT | [DCRAT](https://attack.mitre.org/software/S9017) is a variant of the open-source [AsyncRAT](https://attack.mitre.org/software/S1087) developed in C# with additional capabilities such as patching Microsoft’s Antimalware Scan Interface (AMSI).(Citation: Zscaler BlindEagle DEC 2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--asyncrat | AsyncRAT | [AsyncRAT](https://attack.mitre.org/software/S1087) is an open-source remote access tool originally available through the NYANxCAT Github repository that has been used in malicious campaigns.(Citation: Morphisec Snip3 May 2021)(Citation: Cisco Operation Layover September 2021)(Citation: Telefonica Snip3 December 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--remcos | Remcos | [Remcos](https://attack.mitre.org/software/S0332) is a closed-source tool that is marketed as a remote control and surveillance software by a company called Breaking Security. [Remcos](https://attack.mitre.org/software/S0332) has been observed being used in malware campaigns.(Citation: Riskiq Remcos Jan 2018)(Citation: Talos Remcos Aug 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--imminent-monitor | Imminent Monitor | [Imminent Monitor](https://attack.mitre.org/software/S0434) was a commodity remote access tool (RAT) offered for sale from 2012 until 2019, when an operation was conducted to take down the Imminent Monitor infrastructure. Various cracked versions and variations of this RAT are still in circulation.(Citation: Imminent Unit42 Dec2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--quasarrat | QuasarRAT | [QuasarRAT](https://attack.mitre.org/software/S0262) is an open-source, remote access tool that has been publicly available on GitHub since at least 2014. [QuasarRAT](https://attack.mitre.org/software/S0262) is developed in the C# language.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| Stealth | T1027 | Obfuscated Files or Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.003 | Steganography | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.016 | Junk Code Insertion | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036 | Masquerading | dns.org:2050 MITRE ATT&CK ATT&CK NAME ATT&CK ID Powershell T1059.001 Scripting T1064 Startup Folder T1547.001 Process Injection T1055 Masquerading T1036 Sandbox Evasion T1497 Application Layer Protocol T1071 |  |  | 不明 | 不明 | 中 | `source--blind-eagle--6823726904c42306` |
| Stealth | T1036.004 | Masquerade Task or Service | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055 | Process Injection | f IP febenvi[.]duckdns.org:2050 MITRE ATT&CK ATT&CK NAME ATT&CK ID Powershell T1059.001 Scripting T1064 Startup Folder T1547.001 Process Injection T1055 Masquerading T1036 Sandbox Evasion T1497 Application Layer Protocol T1071 |  |  | 不明 | 不明 | 中 | `source--blind-eagle--6823726904c42306` |
| Privilege Escalation, Stealth | T1055.012 | Process Hollowing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--blind-eagle--6823726904c42306`, `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.007 | JavaScript | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1064 | Scripting | nts/940363101067411527/94639004997978 1130/cacha.pdf IP febenvi[.]duckdns.org:2050 MITRE ATT&CK ATT&CK NAME ATT&CK ID Powershell T1059.001 Scripting T1064 Startup Folder T1547.001 Process Injection T1055 Masquerading T1036 Sandbox Evasion T1497 Application Layer Protocol T1071 |  |  | 不明 | 不明 | 中 | `source--blind-eagle--6823726904c42306` |
| Command And Control | T1071 | Application Layer Protocol | Powershell T1059.001 Scripting T1064 Startup Folder T1547.001 Process Injection T1055 Masquerading T1036 Sandbox Evasion T1497 Application Layer Protocol T1071 |  |  | 不明 | 不明 | 中 | `source--blind-eagle--6823726904c42306` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence | T1133 | External Remote Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1480 | Execution Guardrails | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery, Stealth | T1497 | Virtualization/Sandbox Evasion | TT&CK ATT&CK NAME ATT&CK ID Powershell T1059.001 Scripting T1064 Startup Folder T1547.001 Process Injection T1055 Masquerading T1036 Sandbox Evasion T1497 Application Layer Protocol T1071 |  |  | 不明 | 不明 | 中 | `source--blind-eagle--6823726904c42306` |
| Lateral Movement | T1534 | Internal Spearphishing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | /94639004997978 1130/cacha.pdf IP febenvi[.]duckdns.org:2050 MITRE ATT&CK ATT&CK NAME ATT&CK ID Powershell T1059.001 Scripting T1064 Startup Folder T1547.001 Process Injection T1055 Masquerading T1036 Sandbox Evasion T1497 Application Layer Protocol T1071 |  |  | 不明 | 不明 | 中 | `source--blind-eagle--6823726904c42306` |
| Stealth | T1564.003 | Hidden Window | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1568 | Dynamic Resolution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1571 | Non-Standard Port | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.003 | Virtual Private Server | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.006 | Web Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.005 | Botnet | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1586.002 | Email Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1586.003 | Cloud Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.001 | Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1593 | Search Open Websites/Domains | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.001 | Upload Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1683.001 | Written Content | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1683.002 | Audio-Visual Content | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1684.001 | Impersonation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 110件
- IOC観測: 114件
- 複数攻撃で観測: 0件
- 要レビュー候補: 76件
- 非IOC artifact観測: 68件（`artifacts.csv`）

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
| source--blind-eagle--849392cad6eb513c | APT Blind Eagles |  | 不明 | BlindEagle/APT_Blind_Eagles.pdf | report | TLP:CLEAR | 中 |
| source--blind-eagle--6823726904c42306 | APT Blind Eagles Malware Arsenal Technical Analysis of the New |  | 不明 | BlindEagle/APT_Blind_Eagles_Malware_Arsenal_Technical_Analysis_of_the_New.pdf | report | TLP:CLEAR | 中 |
| source--blind-eagle--78eda3d14cb3fe38 | README |  | 不明 | BlindEagle/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--osint-misp-360net | MISP Galaxy 360.net Threat Actors | MISP Project / 360 Netlab | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
