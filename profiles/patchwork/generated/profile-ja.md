# Patchwork 脅威アクタープロファイル

- プロファイルID: `actor--patchwork`
- 状態: draft
- 更新日時: 2026-07-27T11:04:34Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Patchworkの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Patchwork**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Chinastrats | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Dropping Elephant | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Hangover Group | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| MONSOON | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Operation Hangover | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Capricorn Organisation | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 6; mapping requires review. |
| APT-C-09 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 6; mapping requires review. |
| Viceroy Tiger | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 6; mapping requires review. |
| Mahaboo | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 6; mapping requires review. |
| Neon, Confucius | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 6; mapping requires review. |
| offshore APT organization from South Asia | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 6; mapping requires review. |

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
| Confucius | related-to | Security researchers have noted similarities between [Confucius](https://attack.mitre.org/groups/G0142) and [Patchwork](https://attack.mitre.org/groups/G0040), particularly in their respective custom malware code and targets.(Citation: TrendMicro Confucius APT Feb 2018)(Citation: TrendMicro Confucius APT Aug 2021)(Citation: Uptycs Confucius APT Jan 2021) | 中 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Patchwork](https://attack.mitre.org/groups/G0040) is a cyber espionage group that was first observed in December 2015. While the group has not been definitively attributed, circumstantial evidence suggests the group may be a pro-Indian or Indian entity. [Patchwork](https://attack.mitre.org/groups/G0040) has been seen targeting industries related to diplomatic and government agencies. Much of the code used by this group was copied and pasted from online forums. [Patchwork](https://attack.mitre.org/groups/G0040) was also seen operating spearphishing campaigns targeting U.S. think tank groups in March and April of 2018.(Citation: Cymmetria Patchwork) (Citation: Symantec Patchwork)(Citation: TrendMicro Patchwork Dec 2017)(Citation: Volexity Patchwork June 2018) |
| Capability | TINYTYPHON, Unknown Logger, BackConfig, NDiskMonitor, BADNEWS, AutoIt backdoor, Unknown Logger Public, PowerSploit, QuasarRAT |
| Infrastructure |  |
| Victim | global, including targets in the US, Europe, and the Middle East, many of the target countries are in the area surrounding the Indian subcontinent |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Operation HangOver, Monsoon, Viceroy Tiger | multiple-name-intersection | 高 | India | https://keybase.pub/kung_foo/papers_and_presentations/Unveiling_an_Indian_Cyberattack_Infrastructure.pdf<br>https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2013/Unveiling%20an%20Indian%20Cyberattack%20Infrastructure%20-%20appendixes.pdf<br>https://www.darkreading.com/attacks-breaches/hangover-persists-more-mac-malware-found/d/d-id/1140147 |
| etda-threat-group-cards | Patchwork, Dropping Elephant | canonical-name | 高 | India | https://s3-us-west-2.amazonaws.com/cymmetria-blog/public/Unveiling_Patchwork.pdf<br>https://www.symantec.com/connect/blogs/patchwork-cyberespionage-group-expands-targets-governments-wide-range-industries<br>https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | VICEROY TIGER | multiple-name-intersection | 高 | IN | https://github.com/jack8daniels2/threat-INTel/blob/master/2013/Unveiling-an-Indian-Cyberattack-Infrastructure-appendixes.pdf<br>https://ti.360.net/blog/articles/latest-activity-of-apt-c-35/<br>https://www.netscout.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia |
| misp-threat-actor | QUILTED TIGER | canonical-name | 高 | IN, India | https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=09308982-77bd-41e0-8269-f2cc9ce3266e&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments<br>https://www.forcepoint.com/blog/x-labs/monsoon-analysis-apt-campaign<br>https://www.cymmetria.com/patchwork-targeted-attack/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | Patchwork - G0040 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0040<br>https://s3-us-west-2.amazonaws.com/cymmetria-blog/public/Unveiling%20Patchwork.pdf<br>http://www.symantec.com/connect/blogs/patchwork-cyberespionage-group-expands-targets-governments-wide-range-industries |
| misp-mitre-enterprise-intrusion-set | MONSOON - G0042 | single-alias-intersection | 中 |  | https://attack.mitre.org/wiki/Group/G0042 |
| misp-mitre-intrusion-set | Patchwork - G0040 | mitre-external-id | 高 |  | http://www.symantec.com/connect/blogs/patchwork-cyberespionage-group-expands-targets-governments-wide-range-industries<br>https://attack.mitre.org/groups/G0040<br>https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf |
| misp-mitre-intrusion-set | MONSOON - G0042 | single-alias-intersection | 中 |  | https://attack.mitre.org/groups/G0042 |
| misp-360net | 摩诃草 - APT-C-09 | canonical-name | 高 | india | https://apt.360.net/report/apts/110.html<br>https://apt.360.net/report/apts/6.html |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| MONSOON | similar | misp-mitre-enterprise-intrusion-set | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Patchwork | similar | misp-mitre-enterprise-intrusion-set | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--autoit-backdoor | AutoIt backdoor | [AutoIt backdoor](https://attack.mitre.org/software/S0129) is malware that has been used by the actors responsible for the MONSOON campaign. The actors frequently used it in weaponized .pps files exploiting CVE-2014-6352. (Citation: Forcepoint Monsoon) This malware makes use of the legitimate scripting language for Windows GUI automation with the same name. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--backconfig | BackConfig | [BackConfig](https://attack.mitre.org/software/S0475) is a custom Trojan with a flexible plugin architecture that has been used by [Patchwork](https://attack.mitre.org/groups/G0040).(Citation: Unit 42 BackConfig May 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--badnews | BADNEWS | [BADNEWS](https://attack.mitre.org/software/S0128) is malware that has been used by the actors responsible for the [Patchwork](https://attack.mitre.org/groups/G0040) campaign. Its name was given due to its use of RSS feeds, forums, and blogs for command and control. (Citation: Forcepoint Monsoon) (Citation: TrendMicro Patchwork Dec 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--ndiskmonitor | NDiskMonitor | [NDiskMonitor](https://attack.mitre.org/software/S0272) is a custom backdoor written in .NET that appears to be unique to [Patchwork](https://attack.mitre.org/groups/G0040). (Citation: TrendMicro Patchwork Dec 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--tinytyphon | TINYTYPHON | [TINYTYPHON](https://attack.mitre.org/software/S0131) is a backdoor  that has been used by the actors responsible for the MONSOON campaign. The majority of its code was reportedly taken from the MyDoom worm. (Citation: Forcepoint Monsoon) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--unknown-logger | Unknown Logger | [Unknown Logger](https://attack.mitre.org/software/S0130) is a publicly released, free backdoor. Version 1.5 of the backdoor has been used by the actors responsible for the MONSOON campaign. (Citation: Forcepoint Monsoon) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--unknown-logger-public | Unknown Logger Public | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--powersploit | PowerSploit | [PowerSploit](https://attack.mitre.org/software/S0194) is an open source, offensive security framework comprised of [PowerShell](https://attack.mitre.org/techniques/T1059/001) modules and scripts that perform a wide range of tasks related to penetration testing such as code execution, persistence, bypassing anti-virus, recon, and exfiltration. (Citation: GitHub PowerSploit May 2012) (Citation: PowerShellMagazine PowerSploit July 2014) (Citation: PowerSploit Documentation) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|
| Patchworkハッカー、高度なBrute Ratel C4ツールでブータンを標的に | malware-campaign | 不明 | 不明 | 2024-07-25 | PatchworkハッカーがBrute Ratel C4ツールを使用し、ブータンを標的に ロマンスをテーマにしたおとりを使ってパキスタンとインドの被害者を誘い込み、VajraSpyというマルウェアに感染させる攻撃を実施 攻撃はWindowsショートカット（LNK）ファイルを介して開始 感染により、リモートシェル機能を持つPGoShellバックドアやBrute Ratel C4を配布 攻撃は主に政府機関や人権団体を対象 | 高 | `source--daily-b4dd81678daba2178538` |
| Hangover | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |
| Monsoon | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

Hangover; Monsoon

## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Collection | T1005 | Data from Local System | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.001 | Binary Padding | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.002 | Software Packing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.005 | Indicator Removal from Tools | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.010 | Command Obfuscation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055.012 | Process Hollowing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102.001 | Dead Drop Resolver | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1119 | Automated Collection | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1132.001 | Standard Encoding | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1189 | Drive-by Compromise | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Stealth | T1197 | BITS Jobs | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518.001 | Security Software Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1548.002 | Bypass User Account Control | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1553.002 | Code Signing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.003 | Credentials from Web Browsers | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1559.002 | Dynamic Data Exchange | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560 | Archive Collected Data | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.002 | Code Signing Certificates | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1598.003 | Spearphishing Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1680 | Local Storage Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| source--daily-b4dd81678daba2178538 | Patchworkハッカー、高度なBrute Ratel C4ツールでブータンを標的に | thehackernews.com | 2024-07-25 | https://thehackernews.com/2024/07/patchwork-hackers-target-bhutan-with.html | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-360net | MISP Galaxy 360.net Threat Actors | MISP Project / 360 Netlab | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--patchwork--a29942955af8ffca | README |  | 不明 | Patchwork/README.MD | repository-notes | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
