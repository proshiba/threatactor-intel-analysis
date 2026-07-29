# Revil 脅威アクタープロファイル

- プロファイルID: `actor--revil`
- 状態: draft
- 更新日時: 2026-07-25T11:07:06Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Revilの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Revil**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| GrandCrab | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| Water Mare | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |

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
| Adversary |  |
| Capability | Sodinokibi, IcedID, Qakbot, PsExec, FileZilla |
| Infrastructure |  |
| Victim | Transportation, Financial, Oil and Gas, Technology, Healthcare, in United States, Mexico, Germany, Japan, Israel |
| Socio-political | Russia |

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

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--sodinokibi | Sodinokibi | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--icedid | IcedID | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--qakbot | Qakbot | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--psexec | PsExec | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--filezilla | FileZilla | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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
| Medibank November 2022 | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

Medibank November 2022

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | United States | Targeting text mentions united states. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Germany | Targeting text mentions germany. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Mexico | Targeting text mentions mexico. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Israel | Targeting text mentions israel. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Japan | Targeting text mentions japan. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Technology | Targeting text indicates the Technology sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Energy | Targeting text indicates the Energy sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Finance | Targeting text indicates the Finance sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Healthcare | Targeting text indicates the Healthcare sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Transportation | Targeting text indicates the Transportation sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 8件
- IOC観測: 9件
- 複数攻撃で観測: 0件
- 要レビュー候補: 5件
- 非IOC artifact観測: 108件（`artifacts.csv`）

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
| source--revil--b42d350c7709dcaf | revil |  | 不明 | actor_profile/evidence/revil.csv | structured-data | TLP:CLEAR | 中 |
| source--revil--6a5cee7931c9166d | hunting cobaltstrike beacons in the dark |  | 不明 | APT-hunting/hunting-cobaltstrike-beacons-in-the-dark.pdf | report | TLP:CLEAR | 中 |
| source--revil--1014d48336153bec | google fog of war research report |  | 不明 | International Strategic/Russia/google_fog_of_war_research_report.pdf | report | TLP:CLEAR | 中 |
| source--revil--def01b5e167b7ef3 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--revil--4ede95d326e969cf | WizardSpider TLPWHITE v.1.4 |  | 不明 | Wizard Spider/WizardSpider_TLPWHITE_v.1.4.pdf | report | TLP:CLEAR | 中 |
| source--revil--a6caacd2dcfbb03a | Virtual Routes Pharos Report Series No. 3 |  | 不明 | cybercrime/2025/Virtual-Routes-Pharos-Report-Series-No.-3.pdf | report | TLP:CLEAR | 中 |
| source--revil--574a3773e97d801d | ESET Threat Report Q22020 |  | 不明 | summary/2020/ESET_Threat_Report_Q22020.pdf | report | TLP:CLEAR | 中 |
| source--revil--7578cd581e3efce4 | PWC cyber threats 2019 retrospect |  | 2019 | summary/2020/PWC-cyber-threats-2019-retrospect.pdf | report | TLP:CLEAR | 中 |
| source--revil--1d89a6dec5e0deeb | Global APT Research Report for the first half of 2021 360 |  | 2021 | summary/2021/Global APT Research Report for the first half of 2021-360.pdf | report | TLP:CLEAR | 中 |
| source--revil--dda5e737f86803f1 | The CrowdStrike 2021 Global Threat Report |  | 2021 | summary/2021/The CrowdStrike 2021 Global Threat Report.pdf | report | TLP:CLEAR | 中 |
| source--revil--059c35d990c26ec7 | eset threat report t12021 |  | 不明 | summary/2021/eset_threat_report_t12021.pdf | report | TLP:CLEAR | 中 |
| source--revil--b8ced6f44a31ea3b | sophos 2021 threat report |  | 2021 | summary/2021/sophos-2021-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--revil--dc82c3ad42f42b3c | 2021 Advanced Threat Trends Research Report dbappsecurity |  | 2021 | summary/2022/2021 Advanced Threat Trends Research Report-dbappsecurity.pdf | report | TLP:CLEAR | 中 |
| source--revil--e62aa93039f602c1 | 2021 Vulnerability Landscape |  | 2021 | summary/2022/2021 Vulnerability Landscape.pdf | report | TLP:CLEAR | 中 |
| source--revil--2cd4f48d797bd1dd | 2022 Apr Ransomware Report v3 |  | 2022 | summary/2022/2022-Apr-Ransomware-Report-v3.pdf | report | TLP:CLEAR | 中 |
| source--revil--26f90b8b5a5d8fee | 2022 Yoroi Cybersecurity Annual Report |  | 2022 | summary/2022/2022-Yoroi_Cybersecurity_Annual_Report.pdf | report | TLP:CLEAR | 中 |
| source--revil--a7a785e0fe00a083 | 2022 unit42 incident response report final |  | 2022 | summary/2022/2022-unit42-incident-response-report-final.pdf | report | TLP:CLEAR | 中 |
| source--revil--66e421a718bed07c | ACSC Annual Cyber Threat Report 2022 |  | 2022 | summary/2022/ACSC-Annual-Cyber-Threat-Report-2022.pdf | report | TLP:CLEAR | 中 |
| source--revil--f2b78d75fbcd9d48 | Expel Great eXpeltations 2022 Report |  | 2022 | summary/2022/Expel-Great-eXpeltations-2022-Report.pdf | report | TLP:CLEAR | 中 |
| source--revil--be185b2759d12411 | Intel471 Cyber Threats 2022 |  | 2022 | summary/2022/Intel471_Cyber_Threats_2022.pdf | report | TLP:CLEAR | 中 |
| source--revil--4213cb396cd4f0bb | Microsoft Digital Defense Report 2022 |  | 2022 | summary/2022/Microsoft Digital Defense Report 2022.pdf | report | TLP:CLEAR | 中 |
| source--revil--b5728d6e100e8ed4 | WEF Global Cybersecurity Outlook 2022 |  | 2022 | summary/2022/WEF_Global_Cybersecurity_Outlook_2022.pdf | report | TLP:CLEAR | 中 |
| source--revil--4ffb492dd19a42bc | XForce Threat Intelligence 2022 |  | 2022 | summary/2022/XForce_Threat_Intelligence_2022.pdf | report | TLP:CLEAR | 中 |
| source--revil--b857de50fddfdf32 | rpt toward a new momentum trend micro security predictions for 2022 |  | 2022 | summary/2022/rpt-toward-a-new-momentum-trend-micro-security-predictions-for-2022.pdf | report | TLP:CLEAR | 中 |
| source--revil--936d64ebeeb5bbb8 | sophos 2022 threat report |  | 2022 | summary/2022/sophos-2022-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--revil--39327a03f880b49b | 2022 year in retrospect report |  | 2022 | summary/2023/2022-year-in-retrospect-report.pdf | report | TLP:CLEAR | 中 |
| source--revil--508858715c9981c0 | 2022cyberComprehensiveSituationObservationManual |  | 2022 | summary/2023/2022cyberComprehensiveSituationObservationManual.pdf | report | TLP:CLEAR | 中 |
| source--revil--b6cc395d75ddcca2 | M Trends 2023 Report MANDIANT SPECIAL REPORT |  | 2023 | summary/2023/M-Trends 2023 Report MANDIANT SPECIAL REPORT.pdf | report | TLP:CLEAR | 中 |
| source--revil--3f3b91a5b8f615af | MDDR FINAL 2023 1004 |  | 2023-10-04 | summary/2023/MDDR_FINAL_2023_1004.pdf | report | TLP:CLEAR | 中 |
| source--revil--eb9f887488ecf576 | Secureworks NC3 2022StateoftheThreat |  | 2022 | summary/2023/Secureworks_NC3_2022StateoftheThreat.pdf | report | TLP:CLEAR | 中 |
| source--revil--6aaa9a5c213abf47 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--revil--22adc141f28a0dd0 | 2024 security report |  | 2024 | summary/2024/2024-security-report.pdf | report | TLP:CLEAR | 中 |
| source--revil--47c75b39d341f748 | 2024 Trustwave Public Sector Threat Landscape |  | 2024 | summary/2024/2024_Trustwave_Public_Sector_Threat_Landscape.pdf | report | TLP:CLEAR | 中 |
| source--revil--23b3502d69fcd198 | Recordedfuture 2023 Annual Report ta 2024 0321 |  | 2023 | summary/2024/Recordedfuture 2023 Annual Report ta-2024-0321.pdf | report | TLP:CLEAR | 中 |
| source--revil--bc8935bc5a6c25a4 | Symantec Ransomware Threat Landscape 2024 |  | 2024 | summary/2024/Symantec_Ransomware_Threat_Landscape_2024.pdf | report | TLP:CLEAR | 中 |
| source--revil--96e754b9e9b5edd5 | Worldwide Ransomware Attacks as of June 2024 Consistent With Previous Year Sep2024 |  | 2024 | summary/2024/Worldwide_Ransomware_Attacks_as_of_June_2024_Consistent_With_Previous_Year_Sep2024.pdf | report | TLP:CLEAR | 中 |
| source--revil--0453ef91b62279f1 | state of the threat report 2024 |  | 2024 | summary/2024/state-of-the-threat-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--revil--151f8841f0b18e24 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--revil--4bb4c0e2f1297195 | 2024 cybersecurity trends report |  | 2024 | summary/2025/2024-cybersecurity-trends-report.pdf | report | TLP:CLEAR | 中 |
| source--revil--7a5e0bd233c6a037 | Bridewell 2026 Cyber Threat Intelligence Report |  | 2026 | summary/2026/Bridewell 2026 Cyber Threat Intelligence Report.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
