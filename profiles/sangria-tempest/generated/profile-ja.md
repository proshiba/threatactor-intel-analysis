# Sangria Tempest 脅威アクタープロファイル

- プロファイルID: `actor--sangria-tempest`
- 状態: draft
- 更新日時: 2026-07-27T11:17:24Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Sangria Tempestの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Sangria Tempest**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Carbon Spider | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| ELBRUS | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| FIN7 | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| Carbanak | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Russia row 8; mapping requires review. |
| Anunak | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Russia row 8; mapping requires review. |

## 帰属

The repository mapping workbook places this actor in the Russia worksheet.

- 国: Russia
- スポンサー種別: state
- 確度: 中
- 証拠: `source--actor-mapping-workbook`

## モチベーション

未評価

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| FIN7 | overlaps-with | 共有alias: Carbon Spider, ELBRUS, FIN7, Sangria Tempest | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability | PowerSource |
| Infrastructure |  |
| Victim | Bank of Valetta, Malta |
| Socio-political | Russia |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Carbanak, Anunak | canonical-name | 高 | Ukraine | https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08064518/Carbanak_APT_eng.pdf<br>https://www.group-ib.com/resources/threat-research/Anunak_APT_against_financial_institutions.pdf<br>https://www.bitdefender.com/files/News/CaseStudies/study/262/Bitdefender-WhitePaper-An-APT-Blueprint-Gaining-New-Visibility-into-Financial-Threats-interactive.pdf |
| etda-threat-group-cards | FIN7 | single-alias-intersection | 中 | Russia | https://www.fireeye.com/blog/threat-research/2018/08/fin7-pursuing-an-enigmatic-and-evasive-global-criminal-operation.html<br>https://atr-blog.gigamon.com/2017/07/25/footprints-of-fin7-tracking-actor-patterns-part-1<br>https://atr-blog.gigamon.com/2017/07/26/footprints-of-fin7-tracking-actor-patterns-part-2 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Sangria Tempest | canonical-name | 高 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | FIN7 | canonical-name | 高 | RU | https://en.wikipedia.org/wiki/Carbanak<br>https://app.box.com/s/p7qzcury97tuwk26694uutujwqmwqyhe<br>http://2014.zeronights.ru/assets/files/slides/ivanovb-zeronights.pdf |
| misp-microsoft-activity-group | Sangria Tempest | canonical-name | 高 | UA | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | FIN7 - G0046 | single-alias-intersection | 中 |  | https://attack.mitre.org/wiki/Group/G0046<br>https://www.fireeye.com/blog/threat-research/2017/03/fin7%20spear%20phishing.html<br>https://www.fireeye.com/blog/threat-research/2017/04/fin7-phishing-lnk.html |
| misp-mitre-enterprise-intrusion-set | Carbanak - G0008 | multiple-name-intersection | 高 |  | https://attack.mitre.org/wiki/Group/G0008<br>https://securelist.com/files/2015/02/Carbanak%20APT%20eng.pdf<br>https://www.fireeye.com/blog/threat-research/2017/04/fin7-phishing-lnk.html |
| misp-mitre-intrusion-set | Carbanak - G0008 | multiple-name-intersection | 高 |  | https://attack.mitre.org/groups/G0008<br>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08064518/Carbanak_APT_eng.pdf<br>https://www.europol.europa.eu/newsroom/news/mastermind-behind-eur-1-billion-cyber-bank-robbery-arrested-in-spain |
| misp-mitre-intrusion-set | FIN7 - G0046 | canonical-name | 高 |  | http://blog.morphisec.com/fin7-attacks-restaurant-industry<br>https://attack.mitre.org/groups/G0046<br>https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319 |
| misp-360net | Carbanak - APT-C-11 | single-alias-intersection | 中 | Ukraine | https://apt.360.net/report/apts/68.html |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Carbanak | similar | misp-mitre-enterprise-intrusion-set | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| FIN7 | similar | misp-mitre-enterprise-intrusion-set | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--powersource | PowerSource | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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
| FIN7、Anubisバックドアを展開し、SharePoint経由でWindowsシステムを乗っ取り | malware-campaign | 不明 | 不明 | 2025-04-03 | 金銭目的の脅威アクターFIN7が、Pythonベースのバックドア「Anubis」を使用してWindowsシステムへのリモートアクセスを確立。 Anubisは、被害者を誘導して、侵害されたSharePointサイト上のペイロードを実行させるマルスパムキャンペーンで拡散。 感染はZIPアーカイブ内のPythonスクリプトから始まり、メモリ内で難読化されたペイロードを復号・実行。 バックドアは、Base64エンコードされたTCPソケット通信を介してリモートサーバーと通信し、システム操作を実行。 攻撃者は、キーロギング、スクリーンショット取得、パスワード窃取などの操作を、被害者のシステム上に直接ツールを保存せずに実行可能。 | 中 | `source--daily-aa4ff1b6006e51c3ed82` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | Finance | Targeting text indicates the Finance sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Initial Access | T1200 | Hardware Additions | доступ к инфраструктуре жертв через наборы эксплоитов. Например, опера - торы ZLoader использовали Spelevo EK, а с Dridex – набор Rig EK. • Hardware additions T1200 В 2021 году группировка FIN7 продолжила проводить атаки типа BadUSB для заражения компьютеров в корпоративной среде, отправляя посылки через почтовую службу США и логистическую компанию UPS. Отправителями значились Министерство здраво - охранени |  |  | 不明 | 不明 | 中 | `source--sangria-tempest--2880b4cdea94039e` |

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 123件（`artifacts.csv`）

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
| source--daily-aa4ff1b6006e51c3ed82 | FIN7、Anubisバックドアを展開し、SharePoint経由でWindowsシステムを乗っ取り | thehackernews.com | 2025-04-03 | https://thehackernews.com/2025/04/fin7-deploys-anubis-backdoor-to-hijack.html | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-360net | MISP Galaxy 360.net Threat Actors | MISP Project / 360 Netlab | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--sangria-tempest--070cb516965bc06d | 2025 dbir data breach investigations report |  | 2025 | summary/2025/2025-dbir-data-breach-investigations-report.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--0fe756b21717318c | readme |  | 不明 | summary/2024/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--sangria-tempest--1418f19d356c776e | Cybersecurity Threats 2024 Mid Year Report |  | 2024 | summary/2024/Cybersecurity Threats 2024 Mid-Year Report.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--15d8b11f6b14fbd9 | 2022 Yearbook of APT group Analysis |  | 2022 | summary/2023/2022 Yearbook of APT group Analysis.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--1fc147fb7bc67894 | Symantec Ransomware Threat Landscape 2024 |  | 2024 | summary/2024/Symantec_Ransomware_Threat_Landscape_2024.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--1fdbd1bcc9e5afeb | The CrowdStrike 2021 Global Threat Report |  | 2021 | summary/2021/The CrowdStrike 2021 Global Threat Report.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--2880b4cdea94039e | sangria tempest |  | 不明 | actor_profile/evidence/sangria-tempest.csv | structured-data | TLP:CLEAR | 中 |
| source--sangria-tempest--31e4540a65502201 | Cybersecurity Threats 2024 Annual Report QAX |  | 2024 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--360f7f2d82cd7a7a | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--sangria-tempest--3979098b90838a1c | 2023 Network Vulnerability Situation Research Report |  | 2023 | summary/2024/2023 Network Vulnerability Situation Research Report.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--3ec96293e67468d1 | Adversary Infrastructure Report 2020 |  | 2020 | summary/2021/Adversary Infrastructure Report 2020.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--3ee04a3bd4299c63 | CERTFR 2025 CTI 004 |  | 2025 | summary/2025/CERTFR-2025-CTI-004.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--43d29daa9046ed1c | 2022 Global Threat Report |  | 2022 | summary/2022/2022 Global Threat Report.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--4daa7b211763dbc5 | 2021 Adversary Infrastructure Report |  | 2021 | summary/2022/2021 Adversary Infrastructure Report.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--4e024f2bdf3ab6eb | eset threat report t12021 |  | 不明 | summary/2021/eset_threat_report_t12021.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--5e3af6aaeffbbbf1 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--63ee75cfdaf644bc | README |  | 不明 | README.md | repository-notes | TLP:CLEAR | 中 |
| source--sangria-tempest--64042626eeef586c | README |  | 不明 | International Strategic/Iran/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--sangria-tempest--67a037acfbd583b8 | Automating APT Campaign and Group Attribution |  | 不明 | APT-hunting/Automating APT Campaign and Group Attribution.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--6a2d831b40cbb5f9 | Bridewell 2026 Cyber Threat Intelligence Report |  | 2026 | summary/2026/Bridewell 2026 Cyber Threat Intelligence Report.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--6bf78f4d5feecff3 | Cyber Threat Intelligence Report 2025 2 |  | 2025 | summary/2025/Cyber Threat Intelligence Report 2025 2.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--7e62ccea07ecf1c3 | rpt mtrends 2021 fireeye |  | 2021 | summary/2021/rpt-mtrends-2021-fireeye.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--816179edbcd4b95a | Qianxin 2023 APT Report |  | 2023 | summary/2024/Qianxin 2023 APT Report.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--8240a6fc112cfca3 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--8b3438c63b925047 | Global APT 2023 Mid Year Report QIANXIN |  | 2023 | summary/2023/Global APT 2023 Mid-Year Report-QIANXIN.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--8b40acd46374312a | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--sangria-tempest--95b3e1b5ce4408fb | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--d306cf2c51026ae8 | 2025 CrowdStrike European Threat Landscape Report |  | 2025 | summary/2025/2025-CrowdStrike-European-Threat-Landscape-Report_.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--d6249a368644feba | M Trends 2023 Report MANDIANT SPECIAL REPORT |  | 2023 | summary/2023/M-Trends 2023 Report MANDIANT SPECIAL REPORT.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--d918ba5e8bdc1648 | 2024 dbir data breach investigations report |  | 2024 | summary/2024/2024-dbir-data-breach-investigations-report.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--e8924f6375a96203 | 2025 Year in Review  Malicious Infrastructure |  | 2025 | summary/2026/2025 Year in Review- Malicious Infrastructure.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--ecd064f5f4058ccf | hunting cobaltstrike beacons in the dark |  | 不明 | APT-hunting/hunting-cobaltstrike-beacons-in-the-dark.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--f01e428998e9d35f | ESET Threat Report Q22020 |  | 不明 | summary/2020/ESET_Threat_Report_Q22020.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--f1de75180991e352 | PWC cyber threats 2019 retrospect |  | 2019 | summary/2020/PWC-cyber-threats-2019-retrospect.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--f4e910b842c9a727 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--fd498c23bc92883d | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--sangria-tempest--fe40b9a2515a1aff | m trends 2024 |  | 2024 | summary/2024/m-trends-2024.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
