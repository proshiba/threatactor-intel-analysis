# Violet Typhoon 脅威アクタープロファイル

- プロファイルID: `actor--violet-typhoon`
- 状態: draft
- 更新日時: 2026-07-27T11:17:27Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Violet Typhoonの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Violet Typhoon**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| APT31 | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| ZIRCONIUM | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| Hurricane Panda | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 54; mapping requires review. |
| BRONZE VINEWOOD | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 54; mapping requires review. |
| Black Vine | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 54; mapping requires review. |
| TEMP.Avengers | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 54; mapping requires review. |
| Zirconium, TA412 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 54; mapping requires review. |

## 帰属

The repository mapping workbook places this actor in the China worksheet.

- 国: China
- スポンサー種別: state
- 確度: 中
- 証拠: `source--actor-mapping-workbook`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | State-sponsored intelligence collection or strategic operations. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Hurricane Panda | overlaps-with | 共有alias: APT31, Zirconium, ZIRCONIUM | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |
| ZIRCONIUM | overlaps-with | 共有alias: APT31, Violet Typhoon, ZIRCONIUM | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability | China Chopper Webshell, PlugX, Mimikatz, Sakula |
| Infrastructure |  |
| Victim | Aerospace, Healthcare, Energy (gas & electric turbine manufacturing), Military and defense, Finance, Agriculture, Technology, Japan, United States, United Kingdom, India, Canada, Brazil, South Africa, Australia, Thailand, South Korea, France, Switzerland, Sweden, Finland, Norway |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | APT 17, Deputy Dog, Elderwood, Sneaky Panda | single-alias-intersection | 中 | China | http://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-elderwood-project.pdf<br>https://intrusiontruth.wordpress.com/2019/07/24/apt17-is-run-by-the-jinan-bureau-of-the-chinese-ministry-of-state-security/<br>https://intezer.com/evidence-aurora-operation-still-active-supply-chain-attack-through-ccleaner/ |
| etda-threat-group-cards | APT 31, Judgment Panda, Zirconium | canonical-name | 高 | China | https://blog.confiant.com/uncovering-2017s-largest-malvertising-operation-b84cd38d6b85<br>https://blog.confiant.com/zirconium-was-one-step-ahead-of-chromes-redirect-blocker-with-0-day-2d61802efd0d<br>https://threatpost.com/microsoft-offers-analysis-of-zero-day-being-exploited-by-zirconium-group/124600/ |
| etda-threat-group-cards | Hurricane Panda | single-alias-intersection | 中 | China | https://www.crowdstrike.com/blog/cyber-deterrence-in-action-a-story-of-one-long-hurricane-panda-campaign/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Hurricane+Panda&n=1 |
| etda-threat-group-cards | Turbine Panda, APT 26, Shell Crew, WebMasters, KungFu Kittens | single-alias-intersection | 中 | China | https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2014/h12756-wp-shell-crew.pdf<br>https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-black-vine-cyberespionage-group.pdf<br>https://www.crowdstrike.com/resources/wp-content/brochures/reports/huge-fan-of-your-work-intelligence-report.pdf |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Violet Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | APT19 | multiple-name-intersection | 高 | CN, China | http://cybercampaigns.net/wp-content/uploads/2013/06/Deep-Panda.pdf<br>https://docs.huihoo.com/rsaconference/usa-2014/anf-t07b-the-art-of-attribution-identifying-and-pursuing-your-cyber-adversaries-final.pdf<br>https://www.cfr.org/interactive/cyber-operations/deep-panda |
| misp-threat-actor | HURRICANE PANDA | single-alias-intersection | 中 | CN | http://www.crowdstrike.com/blog/cyber-deterrence-in-action-a-story-of-one-long-hurricane-panda-campaign/<br>https://www.crowdstrike.com/blog/crowdstrike-discovers-use-64-bit-zero-day-privilege-escalation-exploit-cve-2014-4113-hurricane-panda/<br>https://www.crowdstrike.com/blog/storm-chasing/ |
| misp-threat-actor | APT31 | canonical-name | 高 | CN | https://www.microsoft.com/security/blog/2017/03/27/detecting-and-mitigating-elevation-of-privilege-exploit-for-cve-2017-0005/<br>https://duo.com/decipher/apt-groups-moving-down-the-supply-chain<br>https://go.recordedfuture.com/hubfs/reports/cta-2019-0206.pdf |
| misp-microsoft-activity-group | Violet Typhoon | canonical-name | 高 | CN, China | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | ZIRCONIUM | single-alias-intersection | 中 |  | https://blogs.technet.microsoft.com/mmpc/2017/03/27/detecting-and-mitigating-elevation-of-privilege-exploit-for-cve-2017-0005/ |
| misp-mitre-enterprise-intrusion-set | Deep Panda - G0009 | single-alias-intersection | 中 |  | https://attack.mitre.org/wiki/Group/G0009<br>https://blog.crowdstrike.com/deep-thought-chinese-targeting-national-security-think-tanks/<br>https://www.threatconnect.com/the-anthem-hack-all-roads-lead-to-china/ |
| misp-mitre-intrusion-set | Deep Panda - G0009 | single-alias-intersection | 中 |  | https://attack.mitre.org/groups/G0009<br>https://web.archive.org/web/20170823094836/http:/www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-black-vine-cyberespionage-group.pdf<br>https://web.archive.org/web/20171017072306/https://icitech.org/icit-brief-chinas-espionage-dynasty-economic-death-by-a-thousand-cuts/ |
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

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--china-chopper-webshell | China Chopper Webshell | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--mimikatz | Mimikatz | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--plugx | PlugX | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--sakula | Sakula | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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
| 中国関与のAPT31、クラウドサービスを悪用してロシアITを秘匿攻撃 | phishing-campaign | 不明 | 不明 | 2025-11-24 | 中国関与とされるAPT31が2024～2025年にロシアIT分野を標的に長期潜伏し、サイバースパイ活動を実施。 Yandex CloudやOneDriveなど正規クラウドをC2/データ流出に活用し、通常トラフィックに紛れて検知を回避。 週末・祝日に活動を集中し、SNS上に暗号化コマンドを置く手口で秘匿性を強化。2022年末侵入例も言及。 フィッシングでLNKを起点にCloudyLoaderをDLLサイドロードし、Cobalt Strike展開が確認された。 SharpChromeやOwawa、LocalPlugX、CloudSorcerer等の多様なツールを使用し、タスク登録で永続化を確立。 | 中 | `source--daily-627b32691a33594d7d9a` |
| ランサムウェアグループがMicrosoft SharePointサーバーを狙う攻撃に加勢 | ransomware-extortion | 不明 | 不明 | 2025-08-05 | Palo Alto Networks Unit 42はSharePoint脆弱性チェーン「ToolShell」で4L4MD4Rランサムウェアを確認。 ローダーは theinnovationfactory[.]it (145[.]239[.]97[.]206) からペイロードを取得し、監視機能を無効化。 CVE-2025-49706/49704は、CVE-2025-53770/53771という新しいCVE IDを割り当て2025年7月のパッチで修正済み。 Linen/Violet Typhoonなど中国国家系3グループが関与し、少なくとも148組織を侵害。 CISAはCVE-2025-53770をKEVに追加し、24時間以内の対策を要求。 | 中 | `source--daily-0e75e392e2685f601677` |
| 米国国家核安全保障局、Microsoft SharePoint攻撃で侵害 | intrusion | 不明 | 不明 | 2025-07-24 | Microsoft SharePointゼロデイ（ToolShell）悪用で米国国家核安全保障局(NNSA)に侵入。 攻撃は7月18日開始、影響はごく少数システムで復旧中、機密データ流出は未確認。 米教育省・州政府や欧州・中東の政府など計148組織以上が同一手口で被害。 Microsoft/Googleは中国系Linen Typhoon・Violet Typhoon・Storm-2603の関与を指摘。 CISAはCVE-2025-53770を緊急カタログ入り、連邦機関へ24時間以内の対策を命令。 | 中 | `source--daily-c9fa26bbe8d21f50b441` |
| Op. Poisoned Hurricane | operation | 不明 | 不明 | 不明 | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

Op. Poisoned Hurricane

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | United Kingdom | Targeting text mentions united kingdom. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | United States | Targeting text mentions united states. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | South Korea | Targeting text mentions south korea. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Switzerland | Targeting text mentions switzerland. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Australia | Targeting text mentions australia. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Thailand | Targeting text mentions thailand. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Sweden | Targeting text mentions sweden. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Canada | Targeting text mentions canada. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Brazil | Targeting text mentions brazil. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Norway | Targeting text mentions norway. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | France | Targeting text mentions france. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | India | Targeting text mentions india. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | Japan | Targeting text mentions japan. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Defense | Targeting text indicates the Defense sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Technology | Targeting text indicates the Technology sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Energy | Targeting text indicates the Energy sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Finance | Targeting text indicates the Finance sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Healthcare | Targeting text indicates the Healthcare sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Manufacturing | Targeting text indicates the Manufacturing sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 2件
- IOC観測: 2件
- 複数攻撃で観測: 0件
- 要レビュー候補: 2件
- 非IOC artifact観測: 64件（`artifacts.csv`）

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
| source--daily-0e75e392e2685f601677 | ランサムウェアグループがMicrosoft SharePointサーバーを狙う攻撃に加勢 | bleepingcomputer.com | 2025-08-05 | https://www.bleepingcomputer.com/news/security/ransomware-gangs-join-attacks-targeting-microsoft-sharepoint-servers/ | osint-report | TLP:CLEAR | 中 |
| source--daily-627b32691a33594d7d9a | 中国関与のAPT31、クラウドサービスを悪用してロシアITを秘匿攻撃 | thehackernews.com | 2025-11-24 | https://thehackernews.com/2025/11/china-linked-apt31-launches-stealthy.html | osint-report | TLP:CLEAR | 中 |
| source--daily-c9fa26bbe8d21f50b441 | 米国国家核安全保障局、Microsoft SharePoint攻撃で侵害 | bleepingcomputer.com | 2025-07-24 | https://www.bleepingcomputer.com/news/security/us-nuclear-weapons-agency-hacked-in-microsoft-sharepoint-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
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
