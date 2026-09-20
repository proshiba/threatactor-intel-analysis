# Violet Typhoon 脅威アクタープロファイル

- プロファイルID: `actor--violet-typhoon`
- 状態: deprecated
- 更新日時: 2026-09-20T08:53:46Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Violet Typhoonの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Violet Typhoon**
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
- 調査日時: 2026-09-19T01:10:23Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | APT 31, Judgment Panda, Zirconium | canonical-name | 高 | China | https://blog.confiant.com/uncovering-2017s-largest-malvertising-operation-b84cd38d6b85<br>https://blog.confiant.com/zirconium-was-one-step-ahead-of-chromes-redirect-blocker-with-0-day-2d61802efd0d<br>https://threatpost.com/microsoft-offers-analysis-of-zero-day-being-exploited-by-zirconium-group/124600/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Violet Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | APT31 | canonical-name | 高 | CN | https://www.microsoft.com/security/blog/2017/03/27/detecting-and-mitigating-elevation-of-privilege-exploit-for-cve-2017-0005/<br>https://duo.com/decipher/apt-groups-moving-down-the-supply-chain<br>https://go.recordedfuture.com/hubfs/reports/cta-2019-0206.pdf |
| misp-microsoft-activity-group | Violet Typhoon | canonical-name | 高 | CN, China | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | ZIRCONIUM | single-alias-intersection | 中 |  | https://blogs.technet.microsoft.com/mmpc/2017/03/27/detecting-and-mitigating-elevation-of-privilege-exploit-for-cve-2017-0005/ |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | ZIRCONIUM - G0128 | canonical-name | 高 |  | https://attack.mitre.org/groups/G0128<br>https://blogs.microsoft.com/on-the-issues/2020/09/10/cyberattacks-us-elections-trump-biden/<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide |
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

### 活動別ダイヤモンドモデル

活動別ダイヤモンドモデルなし

Op. Poisoned Hurricane

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | インド | レビュー済みアクターマッピングの標的欄に記録されたインドを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | オーストラリア | レビュー済みアクターマッピングの標的欄に記録されたオーストラリアを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | カナダ | レビュー済みアクターマッピングの標的欄に記録されたカナダを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | スイス | レビュー済みアクターマッピングの標的欄に記録されたスイスを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | スウェーデン | レビュー済みアクターマッピングの標的欄に記録されたスウェーデンを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | タイ | レビュー済みアクターマッピングの標的欄に記録されたタイを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | チェコ | 構造化OSINTの被害国フィールドでViolet Typhoonの標的・被害国としてチェコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ノルウェー | レビュー済みアクターマッピングの標的欄に記録されたノルウェーを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | フィンランド | レビュー済みアクターマッピングの標的欄に記録されたフィンランドを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | フランス | レビュー済みアクターマッピングの標的欄に記録されたフランスを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | ブラジル | レビュー済みアクターマッピングの標的欄に記録されたブラジルを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | ベラルーシ | 構造化OSINTの被害国フィールドでViolet Typhoonの標的・被害国としてベラルーシが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | モンゴル | 構造化OSINTの被害国フィールドでViolet Typhoonの標的・被害国としてモンゴルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ロシア | 構造化OSINTの被害国フィールドでViolet Typhoonの標的・被害国としてロシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 南アフリカ | レビュー済みアクターマッピングの標的欄に記録された南アフリカを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | 日本 | レビュー済みアクターマッピングの標的欄に記録された日本を構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | 米国 | レビュー済みアクターマッピングの標的欄に記録された米国を構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | 英国 | レビュー済みアクターマッピングの標的欄に記録された英国を構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | 韓国 | レビュー済みアクターマッピングの標的欄に記録された韓国を構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| regions | アフリカ | レビュー済みアクターマッピングの標的欄に記録されたアフリカを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| regions | 北米 | カナダ、米国で確認された標的・被害事例を北米として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| regions | 東アジア | モンゴル、日本、韓国で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| regions | 東欧 | チェコ、ベラルーシ、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | スイス、スウェーデン、チェコ、ノルウェー、フィンランド、フランス、ベラルーシ、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 2件
- IOC観測: 2件
- 複数攻撃で観測: 0件
- 要レビュー候補: 2件
- 非IOC artifact観測: 64件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| This profile is an exact-identity duplicate of ZIRCONIUM (actor--zirconium). | 高 | `source--mitre-attack-19-1` | Entity-boundary correction. |

### 情報ギャップ


### 不確実性


## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--daily-0e75e392e2685f601677 | ランサムウェアグループがMicrosoft SharePointサーバーを狙う攻撃に加勢 | bleepingcomputer.com | 2025-08-05 | https://www.bleepingcomputer.com/news/security/ransomware-gangs-join-attacks-targeting-microsoft-sharepoint-servers/ | osint-report | TLP:CLEAR | 中 |
| source--daily-4f5ca8613b6408a00d37 | 新たな「BlueMoon」キットがWindowsとChromeのゼロデイ脆弱性を悪用 | proofpoint.com | 2026-09-11 | https://www.proofpoint.com/us/blog/threat-insight/once-bluemoon-multiple-state-aligned-threat-actors-rapidly-adopt-novel-exploit | osint-report | TLP:CLEAR | 中 |
| source--daily-627b32691a33594d7d9a | 中国関与のAPT31、クラウドサービスを悪用してロシアITを秘匿攻撃 | thehackernews.com | 2025-11-24 | https://thehackernews.com/2025/11/china-linked-apt31-launches-stealthy.html | osint-report | TLP:CLEAR | 中 |
| source--daily-c9fa26bbe8d21f50b441 | 米国国家核安全保障局、Microsoft SharePoint攻撃で侵害 | bleepingcomputer.com | 2025-07-24 | https://www.bleepingcomputer.com/news/security/us-nuclear-weapons-agency-hacked-in-microsoft-sharepoint-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 不明 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--violet-typhoon--040d5e209d18d19f | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--violet-typhoon--059b0fa08ad0a4be | CERTFR 2024 CTI 002 |  | 2024 | summary/2024/CERTFR-2024-CTI-002.pdf | report | TLP:CLEAR | 中 |
| source--violet-typhoon--163160447c94fa3c | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--violet-typhoon--262314c41e45f378 | 2025 Cyber Security Report Final |  | 2025 | summary/2025/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--violet-typhoon--294e17574a8319c3 | eset apt activity report q4 2024 q1 2025 |  | 2024 | summary/2025/eset-apt-activity-report-q4-2024-q1-2025.pdf | report | TLP:CLEAR | 中 |
| source--violet-typhoon--2e577a430ff7efa3 | 2021(APT) Microsoft Digital Defense Report |  | 2021 | summary/2021/2021(APT) Microsoft Digital Defense Report.pdf | report | TLP:CLEAR | 中 |
| source--violet-typhoon--332e644f1d5708a5 | A three beat waltz The ecosystem behind Chinese state sponsored cyber threats |  | 不明 | International Strategic/China/A-three-beat-waltz-The-ecosystem-behind-Chinese-state-sponsored-cyber-threats.pdf | report | TLP:CLEAR | 中 |
| source--violet-typhoon--332f78d37e02a944 | china cyber report |  | 不明 | International Strategic/China/china-cyber-report.pdf | report | TLP:CLEAR | 中 |
| source--violet-typhoon--4ea9cf1728525644 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--violet-typhoon--6e11e02cfd02cc23 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--violet-typhoon--7b0f27823f586edc | kaspersky ics cert apt attacks on industrial organizations in h2 2022 en |  | 2022 | summary/2023/kaspersky-ics-cert-apt-attacks-on-industrial-organizations-in-h2-2022-en.pdf | report | TLP:CLEAR | 中 |
| source--violet-typhoon--a61d122ef35ff68d | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--violet-typhoon--ab0049a7c7602202 | 0day  In the Wild |  | 不明 | 0day _In the Wild_.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--violet-typhoon--ab54f7ff9a7cde5b | 2025 Cyber Security Report Final |  | 2025 | summary/2026/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--violet-typhoon--b38301b8dbb50eb6 | rpt security predictions 2021 fireeye |  | 2021 | summary/2021/rpt-security-predictions-2021-fireeye.pdf | report | TLP:CLEAR | 中 |
| source--violet-typhoon--ba0eafe71f278cb5 | CERTFR 2026 CTI 003 |  | 2026 | summary/2026/CERTFR-2026-CTI-003.pdf | report | TLP:CLEAR | 中 |
| source--violet-typhoon--bb1e59672dac4cfb | Modern Asian APT groups TTPs report eng |  | 不明 | summary/2023/Modern-Asian-APT-groups-TTPs_report_eng.pdf | report | TLP:CLEAR | 中 |
| source--violet-typhoon--bf82d744fc82c4a0 | 2023 Adversary Infrastructure Report |  | 2023 | summary/2024/2023 Adversary Infrastructure Report .pdf | report | TLP:CLEAR | 中 |
| source--violet-typhoon--e700d40c0cc1e8d2 | violet typhoon |  | 不明 | actor_profile/evidence/violet-typhoon.csv | structured-data | TLP:CLEAR | 中 |
| source--violet-typhoon--e9b79283ae50cc63 | Charting China’s Climb as a Leading Global Cyber Power |  | 不明 | International Strategic/China/Charting China’s Climb as a Leading Global Cyber Power.pdf | report | TLP:CLEAR | 中 |
| source--violet-typhoon--ed95283c2cdc128f | Hurdling Over Hazards  Multifaceted Threats to the Paris Olympics |  | 不明 | summary/2024/Hurdling Over Hazards- Multifaceted Threats to the Paris Olympics.pdf | report | TLP:CLEAR | 中 |
| source--violet-typhoon--ede2b5cedcace249 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--violet-typhoon--ef64906e87bab725 | state of the threat report 2024 |  | 2024 | summary/2024/state-of-the-threat-report-2024.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
