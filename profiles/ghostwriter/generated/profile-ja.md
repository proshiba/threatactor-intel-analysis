# Ghostwriter 脅威アクタープロファイル

- プロファイルID: `actor--ghostwriter`
- 状態: draft
- 更新日時: 2026-07-25T14:07:08Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Ghostwriterの標準化プロファイル。リポジトリ内の専用資料3件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Ghostwriter**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| UNC1151 | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| TA445 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 82; mapping requires review. |
| Belarus | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Others row 82; mapping requires review. |

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
| Adversary |  |
| Capability |  |
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
| etda-threat-group-cards | Operation Ghostwriter | multiple-name-intersection | 高 | Belarus | https://www.fireeye.com/content/dam/fireeye-www/blog/pdfs/Ghostwriter-Influence-Campaign.pdf<br>https://www.prevailion.com/diving-deep-into-unc1151s-infrastructure-ghostwriter-and-beyond/<br>https://www.mandiant.com/resources/unc1151-linked-to-belarus-government |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Ghostwriter | canonical-name | 高 | BY, Belarus | https://www.fireeye.com/blog/threat-research/2020/07/ghostwriter-influence-campaign.html<br>https://twitter.com/hatr/status/1377220336597483520<br>https://www.mandiant.com/resources/unc1151-linked-to-belarus-government |
| misp-microsoft-activity-group | Storm-0257 | single-alias-intersection | 中 |  | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide |
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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|
| Operation Ghostwriter | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

Operation Ghostwriter

## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Collection, Credential Access | T1056 | Input Capture | nd Scripting Interpreter: Virtual Basic • T1071: Application Layer Protocol • T1105: Ingress Tool Transfer • T1140: Deobfuscate/Decode Files or Information • T1056: Input Capture • T1059.001: Command and Scripting Interpreter: PowerShell • T1059.007: Command and Scripting Interpreter: JavaScript • T1559.002: Dynamic Data Exchange 33 WHITE PAPER \| CYBER ESPIONAGE GROUP UNC1151 LIKELY CONDUCTS GHOSTWRITER INFLUENCE ACTIVITY |  |  | 不明 | 不明 | 中 | `source--ghostwriter--e238f98cc4a7878c` |
| Execution | T1059.001 | PowerShell | r: Virtual Basic • T1071: Application Layer Protocol • T1105: Ingress Tool Transfer • T1140: Deobfuscate/Decode Files or Information • T1056: Input Capture • T1059.001: Command and Scripting Interpreter: PowerShell • T1059.007: Command and Scripting Interpreter: JavaScript • T1559.002: Dynamic Data Exchange 33 WHITE PAPER \| CYBER ESPIONAGE GROUP UNC1151 LIKELY CONDUCTS GHOSTWRITER INFLUENCE ACTIVITY |  |  | 不明 | 不明 | 中 | `source--ghostwriter--e238f98cc4a7878c` |
| Execution | T1059.005 | Visual Basic | e any further attribution assessment at this time. Appendix 3: Technical Annex presents additional detail and MITRE ATT&CK techniques (T1547.001, T1218.005, T1059.005, and T1071). UNC1151 Overview UNC1151 has conducted numerous campaigns designed to steal credentials and deliver malware via spear phishing. The group uses an extensive array of domains that mimic major and regional web services and host pages designed to trick a victim into |  |  | 不明 | 不明 | 中 | `source--ghostwriter--e238f98cc4a7878c` |
| Execution | T1059.007 | JavaScript | 105: Ingress Tool Transfer • T1140: Deobfuscate/Decode Files or Information • T1056: Input Capture • T1059.001: Command and Scripting Interpreter: PowerShell • T1059.007: Command and Scripting Interpreter: JavaScript • T1559.002: Dynamic Data Exchange 33 WHITE PAPER \| CYBER ESPIONAGE GROUP UNC1151 LIKELY CONDUCTS GHOSTWRITER INFLUENCE ACTIVITY |  |  | 不明 | 不明 | 中 | `source--ghostwriter--e238f98cc4a7878c` |
| Command And Control | T1071 | Application Layer Protocol | ttribution assessment at this time. Appendix 3: Technical Annex presents additional detail and MITRE ATT&CK techniques (T1547.001, T1218.005, T1059.005, and T1071). UNC1151 Overview UNC1151 has conducted numerous campaigns designed to steal credentials and deliver malware via spear phishing. The group uses an extensive array of domains that mimic major and regional web services and host pages designed to trick a victim into entering t |  |  | 不明 | 不明 | 中 | `source--ghostwriter--e238f98cc4a7878c` |
| Command And Control | T1105 | Ingress Tool Transfer | 01: Registry Run Keys / Startup Folder • T1218.005: Mshta • T1059.005: Command and Scripting Interpreter: Virtual Basic • T1071: Application Layer Protocol • T1105: Ingress Tool Transfer • T1140: Deobfuscate/Decode Files or Information • T1056: Input Capture • T1059.001: Command and Scripting Interpreter: PowerShell • T1059.007: Command and Scripting Interpreter: JavaScript • T1559.002: Dynamic Data Exchange 33 WHITE PAPER \| CYBER ESPIONAG |  |  | 不明 | 不明 | 中 | `source--ghostwriter--e238f98cc4a7878c` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | Folder • T1218.005: Mshta • T1059.005: Command and Scripting Interpreter: Virtual Basic • T1071: Application Layer Protocol • T1105: Ingress Tool Transfer • T1140: Deobfuscate/Decode Files or Information • T1056: Input Capture • T1059.001: Command and Scripting Interpreter: PowerShell • T1059.007: Command and Scripting Interpreter: JavaScript • T1559.002: Dynamic Data Exchange 33 WHITE PAPER \| CYBER ESPIONAGE GROUP UNC1151 LIKELY CONDUCTS |  |  | 不明 | 不明 | 中 | `source--ghostwriter--e238f98cc4a7878c` |
| Stealth | T1218.005 | Mshta | do not make any further attribution assessment at this time. Appendix 3: Technical Annex presents additional detail and MITRE ATT&CK techniques (T1547.001, T1218.005, T1059.005, and T1071). UNC1151 Overview UNC1151 has conducted numerous campaigns designed to steal credentials and deliver malware via spear phishing. The group uses an extensive array of domains that mimic major and regional web services and host pages designed to trick a |  |  | 不明 | 不明 | 中 | `source--ghostwriter--e238f98cc4a7878c` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | groups and do not make any further attribution assessment at this time. Appendix 3: Technical Annex presents additional detail and MITRE ATT&CK techniques (T1547.001, T1218.005, T1059.005, and T1071). UNC1151 Overview UNC1151 has conducted numerous campaigns designed to steal credentials and deliver malware via spear phishing. The group uses an extensive array of domains that mimic major and regional web services and host pages designed |  |  | 不明 | 不明 | 中 | `source--ghostwriter--e238f98cc4a7878c` |
| Execution | T1559.002 | Dynamic Data Exchange | s or Information • T1056: Input Capture • T1059.001: Command and Scripting Interpreter: PowerShell • T1059.007: Command and Scripting Interpreter: JavaScript • T1559.002: Dynamic Data Exchange 33 WHITE PAPER \| CYBER ESPIONAGE GROUP UNC1151 LIKELY CONDUCTS GHOSTWRITER INFLUENCE ACTIVITY |  |  | 不明 | 不明 | 中 | `source--ghostwriter--e238f98cc4a7878c` |

## IOC／artifact概要

- IOC値: 143件
- IOC観測: 157件
- 複数攻撃で観測: 0件
- 要レビュー候補: 7件
- 非IOC artifact観測: 72件（`artifacts.csv`）

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
| source--ghostwriter--94bca5a8ebb026a7 | Ghostwriter Report Final |  | 不明 | Ghostwriter/Ghostwriter-Report-Final.pdf | report | TLP:CLEAR | 中 |
| source--ghostwriter--3d35d6b65a4c4640 | README |  | 不明 | Ghostwriter/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--ghostwriter--e238f98cc4a7878c | unc1151 ghostwriter update report |  | 不明 | Ghostwriter/unc1151-ghostwriter-update-report.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
