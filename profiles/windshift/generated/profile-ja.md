# Windshift 脅威アクタープロファイル

- プロファイルID: `actor--windshift`
- 状態: draft
- 更新日時: 2026-09-23T12:16:55Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

Windshiftの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Windshift**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Bahamut | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |

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
| The White Company | overlaps-with | 共有alias: The White Company | 低 | `source--mitre-attack-19-2` |

## 関連する企業・個人

関連エンティティなし

### エンティティ関係

確認された関係なし

### 法的措置

確認された法的措置なし

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
- 調査日時: 2026-09-21T02:39:13Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | Bahamut | single-alias-intersection | 中 |  | https://www.bellingcat.com/news/mena/2017/06/12/bahamut-pursuing-cyber-espionage-actor-middle-east/<br>https://www.blackberry.com/us/en/forms/enterprise/bahamut-report<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Bahamut&n=1 |
| etda-threat-group-cards | The White Company | single-alias-intersection | 中 |  | https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=The+White+Company&n=1 |
| etda-threat-group-cards | Urpage | single-alias-intersection | 中 |  | https://blog.trendmicro.com/trendlabs-security-intelligence/the-urpage-connection-to-bahamut-confucius-and-patchwork/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Urpage&n=1 |
| etda-threat-group-cards | WindShift | canonical-name | 高 |  | https://unit42.paloaltonetworks.com/shifting-in-the-wind-windshift-attacks-target-middle-eastern-governments/<br>https://gsec.hitb.org/materials/sg2018/D1%20COMMSEC%20-%20In%20the%20Trails%20of%20WINDSHIFT%20APT%20-%20Taha%20Karim.pdf<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=WindShift&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Bahamut | single-alias-intersection | 中 |  | https://www.bellingcat.com/news/mena/2017/06/12/bahamut-pursuing-cyber-espionage-actor-middle-east/<br>https://www.bellingcat.com/resources/case-studies/2017/10/27/bahamut-revisited-cyber-espionage-middle-east-south-asia/ |
| misp-threat-actor | WindShift | canonical-name | 高 |  | https://unit42.paloaltonetworks.com/shifting-in-the-wind-windshift-attacks-target-middle-eastern-governments/<br>https://gsec.hitb.org/materials/sg2018/D1%20COMMSEC%20-%20In%20the%20Trails%20of%20WINDSHIFT%20APT%20-%20Taha%20Karim.pdf<br>https://unit42.paloaltonetworks.com/atoms/windyphoenix/ |
| misp-threat-actor | Urpage | single-alias-intersection | 中 |  | https://www.trendmicro.com/en_us/research/18/h/the-urpage-connection-to-bahamut-confucius-and-patchwork.html |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | The White Company - G0089 | single-alias-intersection | 中 |  | https://attack.mitre.org/groups/G0089<br>https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517 |
| misp-mitre-enterprise-intrusion-set | Windshift - G0112 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0112<br>https://objective-see.com/blog/blog_0x3B.html<br>https://objective-see.com/blog/blog_0x3D.html |
| misp-mitre-intrusion-set | The White Company - G0089 | single-alias-intersection | 中 |  | https://attack.mitre.org/groups/G0089<br>https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517 |
| misp-mitre-intrusion-set | Windshift - G0112 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0112<br>https://objective-see.com/blog/blog_0x3B.html<br>https://objective-see.com/blog/blog_0x3D.html |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | The White Company | single-alias-intersection | 中 |  |  |
| misp-tidal-groups | Windshift | canonical-name | 高 |  |  |

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
| malware--windtail | WindTail | [WindTail](https://attack.mitre.org/software/S0466) is a macOS surveillance implant used by [Windshift](https://attack.mitre.org/groups/G0112). [WindTail](https://attack.mitre.org/software/S0466) shares code similarities with Hack Back aka KitM OSX.(Citation: SANS Windshift August 2018)(Citation: objective-see windtail1 dec 2018)(Citation: objective-see windtail2 jan 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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

## C2・マルウェア ハンティング・ピボット

構造化されたハンティング・ピボットなし

### 観測根拠

観測記録なし

### ハントクエリ

クエリなし

### 継続利用チェック

実行済みの受動検索・継続利用チェックなし

`active_status` は明示的なテレメトリまたはスキャン根拠がない限り `unknown` です。出典公開日は観測時刻に転用していません。

## 攻撃活動の履歴

活動履歴なし

### 活動別ダイヤモンドモデル

活動別ダイヤモンドモデルなし

InPage zero-day; Malicious MDM

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | 政府・行政 | [Windshift](https://attack.mitre.org/groups/G0112) is a threat group that has been active since at least 2017, targeting specific individuals for surveillance in government departments and critical infrastructure across the Middle East.(Citation: SANS Windshift August 2018)(Citation: objective-see windtail1 dec 2018)(Citation: objective-see windtail2 jan 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1027 | Obfuscated Files or Information | [Windshift](https://attack.mitre.org/groups/G0112) has used string encoding with floating point calculations.(Citation: BlackBerry Bahamut) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1033 | System Owner/User Discovery | [Windshift](https://attack.mitre.org/groups/G0112) has used malware to identify the username on a compromised host.(Citation: BlackBerry Bahamut) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1036 | Masquerading | [Windshift](https://attack.mitre.org/groups/G0112) has used icons mimicking MS Office files to mask malicious executables.(Citation: objective-see windtail1 dec 2018) [Windshift](https://attack.mitre.org/groups/G0112) has also attempted to hide executables by changing the file extension to ".scr" to mimic Windows screensavers.(Citation: BlackBerry Bahamut) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1036.001 | Invalid Code Signature | [Windshift](https://attack.mitre.org/groups/G0112) has used revoked certificates to sign malware.(Citation: objective-see windtail1 dec 2018)(Citation: SANS Windshift August 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1047 | Windows Management Instrumentation | [Windshift](https://attack.mitre.org/groups/G0112) has used WMI to collect information about target machines.(Citation: BlackBerry Bahamut) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1057 | Process Discovery | [Windshift](https://attack.mitre.org/groups/G0112) has used malware to enumerate active processes.(Citation: BlackBerry Bahamut) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.005 | Visual Basic | [Windshift](https://attack.mitre.org/groups/G0112) has used Visual Basic 6 (VB6) payloads.(Citation: BlackBerry Bahamut) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1071.001 | Web Protocols | [Windshift](https://attack.mitre.org/groups/G0112) has used tools that communicate with C2 over HTTP.(Citation: BlackBerry Bahamut) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1082 | System Information Discovery | [Windshift](https://attack.mitre.org/groups/G0112) has used malware to identify the computer name of a compromised host.(Citation: BlackBerry Bahamut) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1105 | Ingress Tool Transfer | [Windshift](https://attack.mitre.org/groups/G0112) has used tools to deploy additional payloads to compromised hosts.(Citation: BlackBerry Bahamut) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1189 | Drive-by Compromise | [Windshift](https://attack.mitre.org/groups/G0112) has used compromised websites to register custom URL schemes on a remote system.(Citation: objective-see windtail1 dec 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1204.001 | Malicious Link | [Windshift](https://attack.mitre.org/groups/G0112) has used links embedded in e-mails to lure victims into executing malicious code.(Citation: SANS Windshift August 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1204.002 | Malicious File | [Windshift](https://attack.mitre.org/groups/G0112) has used e-mail attachments to lure victims into executing malicious code.(Citation: SANS Windshift August 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1518 | Software Discovery | [Windshift](https://attack.mitre.org/groups/G0112) has used malware to identify installed software.(Citation: BlackBerry Bahamut) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1518.001 | Security Software Discovery | [Windshift](https://attack.mitre.org/groups/G0112) has used malware to identify installed AV and commonly used forensic and malware analysis tools.(Citation: BlackBerry Bahamut) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [Windshift](https://attack.mitre.org/groups/G0112) has created LNK files in the Startup folder to establish persistence.(Citation: BlackBerry Bahamut) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1566.001 | Spearphishing Attachment | [Windshift](https://attack.mitre.org/groups/G0112) has sent spearphishing emails with attachment to harvest credentials and deliver malware.(Citation: SANS Windshift August 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1566.002 | Spearphishing Link | [Windshift](https://attack.mitre.org/groups/G0112) has sent spearphishing emails with links to harvest credentials and deliver malware.(Citation: SANS Windshift August 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1566.003 | Spearphishing via Service | [Windshift](https://attack.mitre.org/groups/G0112) has used fake personas on social media to engage and target victims.(Citation: SANS Windshift August 2018)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 11件（`artifacts.csv`）

## 主要判断と不確実性

主要判断なし

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.
- 3 alias lead(s) remain non-canonical pending original-source review.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--windshift--e1715ec6eeb0b359 | windshift |  | 不明 | actor_profile/evidence/windshift.csv | structured-data | TLP:CLEAR | 中 |
| source--windshift--ca350aedbdf68250 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--windshift--da7ed7d548ec1ace | Donot Group & Innefu Labs |  | 不明 | Donot/Donot Group & Innefu Labs.pdf | report | TLP:CLEAR | 中 |
| source--windshift--84a669db8ad829d1 | Linking South Asian cyber espionnage groups to publish |  | 不明 | International Strategic/India/Linking_South_Asian_cyber_espionnage_groups-to-publish.pdf | report | TLP:CLEAR | 中 |
| source--windshift--60cf304d1ba566a4 | README |  | 不明 | International Strategic/India/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--windshift--92407ccbc4011e88 | 南亚地区APT组织2019年度攻击活动总结 |  | 2019 | International Strategic/SouthAsia/南亚地区APT组织2019年度攻击活动总结.pdf | report | TLP:CLEAR | 中 |
| source--windshift--fcd59f7219889a9c | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--windshift--68c0fbd061fcafe9 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--windshift--6f57cdb701d6a60d | WhiteCompanyOperationShaheenReport |  | 不明 | WhiteCompany/WhiteCompanyOperationShaheenReport.pdf | report | TLP:CLEAR | 中 |
| source--windshift--207680534fde6cfa | 20230801 |  | 2023-08-01 | parse-daily/.cache/tech-memo/daily-news/news/2023_07-09/20230801.md | repository-notes | TLP:CLEAR | 中 |
| source--windshift--60ebdbd294d0b69b | APT blackberry mobile malware report |  | 不明 | summary/2020/APT-blackberry-mobile-malware-report.pdf | report | TLP:CLEAR | 中 |
| source--windshift--44439d11459eb3b4 | Offensive Cyber Capabilities Proliferation Report |  | 不明 | summary/2021/Offensive-Cyber-Capabilities-Proliferation-Report.pdf | report | TLP:CLEAR | 中 |
| source--windshift--c121b2c19ba1a226 | 2021 Advanced Threat Trends Research Report dbappsecurity |  | 2021 | summary/2022/2021 Advanced Threat Trends Research Report-dbappsecurity.pdf | report | TLP:CLEAR | 中 |
| source--windshift--b3155106af209cc0 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--windshift--4d1a75495f3fed25 | Global APT Mid 2022 Report qianxin |  | 2022 | summary/2022/Global APT Mid-2022 Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--windshift--13ff5a74439edbdb | 2022cyberComprehensiveSituationObservationManual |  | 2022 | summary/2023/2022cyberComprehensiveSituationObservationManual.pdf | report | TLP:CLEAR | 中 |
| source--windshift--50fa611c924cbf99 | 360 APT Annual Research Report 2022 |  | 2022 | summary/2023/360_APT_Annual_Research_Report_2022.pdf | report | TLP:CLEAR | 中 |
| source--windshift--aba90d179796301f | Global APT 2022 Annual Report qianxin |  | 2022 | summary/2023/Global APT 2022 Annual Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--windshift--77a88eed735aa84f | Global APT 2023 Mid Year Report QIANXIN |  | 2023 | summary/2023/Global APT 2023 Mid-Year Report-QIANXIN.pdf | report | TLP:CLEAR | 中 |
| source--windshift--e27601ac612fe0a2 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--windshift--54b3c68c48dfb8a7 | Qianxin 2023 APT Report |  | 2023 | summary/2024/Qianxin 2023 APT Report.pdf | report | TLP:CLEAR | 中 |
| source--windshift--19028a7c1df4e208 | Cybersecurity Threats 2024 Annual Report QAX |  | 2024 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | report | TLP:CLEAR | 中 |
| source--windshift--c1a061a508af0f76 | search |  | 不明 | ui/api/v1/search.json | structured-data | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
