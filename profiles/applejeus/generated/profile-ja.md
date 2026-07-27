# AppleJeus 脅威アクタープロファイル

- プロファイルID: `actor--applejeus`
- 状態: draft
- 更新日時: 2026-07-27T11:17:21Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

AppleJeusの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **AppleJeus**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Citrine Sleet | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Gleaming Pisces | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| UNC1720 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| UNC4736 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| Lazarus Group | related-to | Associated with the broader [Lazarus Group](https://attack.mitre.org/groups/G0032) umbrella of actors, [AppleJeus](https://attack.mitre.org/groups/G1049) has been active since at least 2018 and is closely aligned in resources with TEMP.hermit, another DPRK-affiliated group under the same umbrella.(Citation: dtex DPRK 2025 structure ITworkers) The group’s primary mission is to generate and launder revenue to provide financial support to the government. | 中 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [AppleJeus](https://attack.mitre.org/groups/G1049) is a North Korean state-sponsored threat group attributed to the Reconnaissance General Bureau. Associated with the broader [Lazarus Group](https://attack.mitre.org/groups/G0032) umbrella of actors, [AppleJeus](https://attack.mitre.org/groups/G1049) has been active since at least 2018 and is closely aligned in resources with TEMP.hermit, another DPRK-affiliated group under the same umbrella.(Citation: dtex DPRK 2025 structure ITworkers) The group’s primary mission is to generate and launder revenue to provide financial support to the government. [AppleJeus](https://attack.mitre.org/groups/G1049) primarily targets the cryptocurrency industry and is most notably responsible for the [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057).(Citation: Mandiant 3cx UNC4736 2023) The group traditionally deploys malicious cryptocurrency software in combination with [Phishing](https://attack.mitre.org/techniques/T1566). From these compromised environments, it selectively deploys additional backdoors to enable extended operations against high-value financial targets.(Citation: Mandiant DPRK Groups 2023)(Citation: JPCert Blog Laz Subgroups 2025) |
| Capability |  |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Lazarus Group, Hidden Cobra, Labyrinth Chollima | multiple-name-intersection | 高 | North Korea | https://blog.malwarebytes.com/threat-analysis/2019/03/the-advanced-persistent-threat-files-lazarus-group/<br>https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/a-look-into-the-lazarus-groups-operations<br>https://www.kaspersky.com/about/press-releases/2017_chasing-lazarus-a-hunt-for-the-infamous-hackers-to-prevent-large-bank-robberies |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Citrine Sleet | single-alias-intersection | 中 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Lazarus Group | single-alias-intersection | 中 | KP, Korea (Democratic People's Republic of) | https://threatpost.com/operation-blockbuster-coalition-ties-destructive-attacks-to-lazarus-group/116422/<br>https://www.us-cert.gov/ncas/alerts/TA17-164A<br>https://www.us-cert.gov/ncas/alerts/TA17-318A |
| misp-threat-actor | UNC4736 | single-alias-intersection | 中 | KP | https://www.mandiant.com/resources/blog/3cx-software-supply-chain-compromise |
| misp-microsoft-activity-group | Citrine Sleet | single-alias-intersection | 中 | KP, North Korea | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | AppleJeus - G1049 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1049<br>https://blogs.jpcert.or.jp/en/2025/03/classifying-lazaruss-subgroup.html<br>https://cloud.google.com/blog/topics/threat-intelligence/3cx-software-supply-chain-compromise/ |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Operation Sharpshooter | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| STARDUST CHOLLIMA | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| TraderTraitor | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

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
| Radiant、5,000万ドルの暗号通貨強奪を北朝鮮ハッカーと結びつける | malware-campaign | 不明 | 不明 | 2024-12-10 | Radiant Capitalは、10月16日のサイバー攻撃で5,000万ドルの暗号通貨が盗まれたと発表。 サイバーセキュリティ企業Mandiantの調査により、攻撃者は北朝鮮の国家支援ハッカー「Citrine Sleet」（別名UNC4736、AppleJeus）であると特定。 攻撃は、3人の信頼された開発者のデバイスにマルウェアを感染させ、正規の署名を収集して不正な取引を実行する手法で行われた。 ハッカーは、ルーチンのマルチシグネチャプロセスを悪用し、トランザクションエラーを装って有効な署名を収集し、ArbitrumおよびBSC市場から資金を窃取。 米国政府は以前から、北朝鮮のハッカーが暗号通貨企業を標的にして資金を窃取し、国家活動を支援していると警告している。 攻撃は2024年9月11日に始まり、Radiantの開発者が元請負業者を装ったTelegramメッセージを受信し、悪意のあるZIPファイルをダウンロードするように仕向けられた。このZIPファイルには、「InletDrift」という名前のmacOSマルウェアがあった。 | 中 | `source--daily-f645f7df90b96e0f1b18` |
| 3CX Supply Chain Attack | campaign | 2022-11-01T06:00:00.000Z | 2023-03-01T05:00:00.000Z | 2026-05-12 | The [3CX Supply Chain Attack](https://attack.mitre.org/campaigns/C0057) was the first publicly reported case of one supply chain compromise triggering another, leading to a cascading, two-stage intrusion. The initial supply chain attack began when a 3CX employee downloaded and executed a trojanized, end-of-life version of the X_Trader trading software from Trading Technologies. This provided UNC4736, a threat cluster associated with [AppleJeus](https://attack.mitre.org/groups/G1049), access to the 3CX environment. From there UNC4736 compromised the Windows and macOS build environments used to distribute the 3CX desktop application to their customers.(Citation: Mandiant 3cx UNC4736 2023) While 3CX serves more than 600,000 customers and 12 million users, only a subset of systems were affected. Subsequent targeting focused on victims in the defense and cryptocurrency sectors, where attackers deployed secondary payloads such as Gopuram for credential theft and persistence.(Citation: Kaspersky 3CX Gopuram 2023) The campaign began in late 2022 and was disrupted after security vendors publicly reported the compromise in March 2023.(Citation: 3cx official statement 2023)(Citation: Krebs 3cx overview 2023) | 高 | `source--mitre-attack-19-1` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Initial Access | T1566 | Phishing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1657 | Financial Theft | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 23件
- IOC観測: 32件
- 複数攻撃で観測: 0件
- 要レビュー候補: 23件
- 非IOC artifact観測: 84件（`artifacts.csv`）

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
| source--applejeus--00a6486816050b51 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--09d7c9a46f9d6193 | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--0e13b86d117533be | M Trends 2023 Report MANDIANT SPECIAL REPORT |  | 2023 | summary/2023/M-Trends 2023 Report MANDIANT SPECIAL REPORT.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--11eecd7bc046b964 | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | International Strategic/Korea/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--20545ea2e414402a | Global APT 2022 Annual Report qianxin |  | 2022 | summary/2023/Global APT 2022 Annual Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--2c3875edf437d32b | Dream Job Campaign |  | 不明 | lazarus/Dream-Job-Campaign.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--360fff7f63ffb03c | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--applejeus--44c7ca0cab019d23 | 360 APT Annual Research Report 2022 |  | 2022 | summary/2023/360_APT_Annual_Research_Report_2022.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--4ac4c38ded7903e2 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--50bbc5ff9b7c43f0 | multiple campaigns of the Lazarus group and their connections |  | 不明 | lazarus/multiple campaigns of the Lazarus group and their connections.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--53a55fb8b8c47aeb | konni threat insight paper triple threat N Korea aligned TA406 steals scams spies |  | 不明 | konni/konni-threat-insight-paper-triple-threat-N-Korea-aligned-TA406-steals-scams-spies.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--55753821d8e9785a | Automating APT Campaign and Group Attribution |  | 不明 | APT-hunting/Automating APT Campaign and Group Attribution.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--5e1bdc358cbf325b | Blurred Lines of Cyber Threat Attribution |  | 不明 | International Strategic/Korea/ Blurred-Lines-of-Cyber-Threat-Attribution.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--62358c65b873eb55 | kaspersky ics cert lazarus targets defense industry with threatneedle en 20210225 |  | 2021-02-25 | lazarus/kaspersky-ics-cert-lazarus-targets-defense-industry-with-threatneedle-en-20210225.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--6ee8d02ff0668468 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--721829f759b32d33 | Global APT Mid 2022 Report qianxin |  | 2022 | summary/2022/Global APT Mid-2022 Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--842144722ffec290 | 2022 Yearbook of APT group Analysis |  | 2022 | summary/2023/2022 Yearbook of APT group Analysis.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--868f81b0e798b812 | RedReport2023 Picus |  | 2023 | summary/2023/RedReport2023-Picus.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--9242cd7af5ccb5b0 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--949fcdd4db2f5cff | The Lazarus Constellation |  | 不明 | lazarus/The_Lazarus_Constellation.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--a8ea13d9767203dc | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | CyberMerceNary/ITWorker/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--b33828eedd3c6e22 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--b6740c4ccfa1c71a | 2026 Mid year Blockchain Security and AML Report |  | 2026 | summary/2026/2026 Mid-year Blockchain Security and AML Report.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--c47e2b21577e983f | m trends 2024 |  | 2024 | summary/2024/m-trends-2024.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--ccee8dd6cc668e73 | The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities |  | 不明 | International Strategic/Korea/The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--d13cc73cd3f9745f | applejeus |  | 不明 | actor_profile/evidence/applejeus.csv | structured-data | TLP:CLEAR | 中 |
| source--applejeus--d45c0b5342dc3f98 | Secureworks NC3 2022StateoftheThreat |  | 2022 | summary/2023/Secureworks_NC3_2022StateoftheThreat.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--e02cad3035fecb76 | README |  | 不明 | summary/2023/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--applejeus--ec8f2f2be49c9846 | 2025 Blockchain Security and AML Annual Report |  | 2025 | summary/2025/2025-Blockchain-Security-and-AML-Annual-Report.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--f41bf6d2b1b91d22 | MDDR FINAL 2023 1004 |  | 2023-10-04 | summary/2023/MDDR_FINAL_2023_1004.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--f4eb431117358cfc | Microsoft Digital Defense Report 2024 |  | 2024 | summary/2024/Microsoft Digital Defense Report 2024.pdf | report | TLP:CLEAR | 中 |
| source--applejeus--fa072972102e0db5 | 2022cyberComprehensiveSituationObservationManual |  | 2022 | summary/2023/2022cyberComprehensiveSituationObservationManual.pdf | report | TLP:CLEAR | 中 |
| source--daily-f645f7df90b96e0f1b18 | Radiant、5,000万ドルの暗号通貨強奪を北朝鮮ハッカーと結びつける | bleepingcomputer.com | 2024-12-10 | https://www.bleepingcomputer.com/news/security/radiant-links-50-million-crypto-heist-to-north-korean-hackers/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
