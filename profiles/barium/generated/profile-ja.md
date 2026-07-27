# BARIUM 脅威アクタープロファイル

- プロファイルID: `actor--barium`
- 状態: draft
- 更新日時: 2026-07-25T14:07:08Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

BARIUMの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **BARIUM**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| BRONZE ATLAS | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| TG-2633 | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| Winnti Umbrella | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| Winnti Group | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 11; mapping requires review. |
| Wicked Panda | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 11; mapping requires review. |
| APT41 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 11; mapping requires review. |
| Winnti Umbrella, BARIUM, LEAD, RedEcho, Vanadinite, TAG-22 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 11; mapping requires review. |
| Deep Panda, Wicked Spider | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 11; mapping requires review. |

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
| Axiom | overlaps-with | 共有alias: Winnti Umbrella | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |
| Ke3chang | overlaps-with | 共有alias: Winnti Umbrella | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |
| LEAD | overlaps-with | 共有alias: Winnti Umbrella | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |
| PassCV | overlaps-with | 共有alias: Winnti Umbrella | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability | Winnti, AceHash, PlugX, Webshells, ZxShell, ShadowPad |
| Infrastructure |  |
| Victim | ThyssenKrupp, Gameforge, Valve, Teamviewer,Siemens, Sumitomo, BASF, Covestro, Shin-Etsu, Bayer, Roche |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | APT 41 | multiple-name-intersection | 高 | China | http://content.fireeye.com/apt41/rpt-apt41<br>https://arstechnica.com/information-technology/2018/05/researchers-link-a-decade-of-potent-hacks-to-chinese-intelligence-group/<br>https://www.kaspersky.com/about/press-releases/2019_operation-shadowhammer-new-supply-chain-attack |
| etda-threat-group-cards | Barium | canonical-name | 高 | China | https://threatvector.cylance.com/en_us/home/digitally-signed-malware-targeting-gaming-companies.html<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Barium&n=1 |
| etda-threat-group-cards | Winnti Group, Wicked Panda | multiple-name-intersection | 高 | China | https://blog.trendmicro.com/trendlabs-security-intelligence/pigs-malware-examining-possible-member-winnti-group/<br>https://securelist.com/winnti-more-than-just-a-game/37029/<br>https://401trg.com/burning-umbrella/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Brass Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| microsoft-threat-actor-mapping | Leopard Typhoon | multiple-name-intersection | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | APT41 | canonical-name | 高 | CN, People's Republic of China | https://securelist.com/winnti-faq-more-than-just-a-game/57585/<br>https://securelist.com/winnti-more-than-just-a-game/37029/<br>http://williamshowalter.com/a-universal-windows-bootkit/ |
| misp-microsoft-activity-group | BARIUM | canonical-name | 高 |  | https://blogs.technet.microsoft.com/mmpc/2017/01/25/detecting-threat-actors-in-recent-german-industrial-attacks-with-windows-defender-atp/ |
| misp-microsoft-activity-group | Brass Typhoon | canonical-name | 高 | CN, China | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Leopard Typhoon | multiple-name-intersection | 高 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | Winnti Group - G0044 | single-alias-intersection | 中 |  | https://attack.mitre.org/wiki/Group/G0044<br>https://kasperskycontenthub.com/wp-content/uploads/sites/43/vlpdfs/winnti-more-than-just-a-game-130410.pdf<br>https://securelist.com/games-are-over/70991/ |
| misp-mitre-intrusion-set | Winnti Group - G0044 | single-alias-intersection | 中 |  | http://www.symantec.com/connect/blogs/suckfly-revealing-secret-life-your-code-signing-certificates<br>https://401trg.github.io/pages/burning-umbrella.html<br>https://attack.mitre.org/groups/G0044 |
| misp-mitre-intrusion-set | APT41 - G0096 | canonical-name | 高 |  | https://attack.mitre.org/groups/G0096<br>https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2020CrowdStrikeGlobalThreatReport.pdf<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| APT17 | similar | misp-mitre-enterprise-intrusion-set | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Axiom | similar | misp-mitre-enterprise-intrusion-set | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| APT17 | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--winnti | Winnti | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--acehash | AceHash | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--plugx | PlugX | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--webshells | Webshells | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--zxshell | ZxShell | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--shadowpad | ShadowPad | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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

TTPなし

## IOC／artifact概要

- IOC値: 14件
- IOC観測: 18件
- 複数攻撃で観測: 0件
- 要レビュー候補: 4件
- 非IOC artifact観測: 50件（`artifacts.csv`）

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
| source--barium--1f400a9d3f2e41f0 | barium |  | 不明 | actor_profile/evidence/barium.csv | structured-data | TLP:CLEAR | 中 |
| source--barium--339c36d0d6a6db7b | hunting cobaltstrike beacons in the dark |  | 不明 | APT-hunting/hunting-cobaltstrike-beacons-in-the-dark.pdf | report | TLP:CLEAR | 中 |
| source--barium--21422a698347bb8f | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--barium--81edbe1c428a9855 | A three beat waltz The ecosystem behind Chinese state sponsored cyber threats |  | 不明 | International Strategic/China/A-three-beat-waltz-The-ecosystem-behind-Chinese-state-sponsored-cyber-threats.pdf | report | TLP:CLEAR | 中 |
| source--barium--e336c8205101f88f | china cyber report |  | 不明 | International Strategic/China/china-cyber-report.pdf | report | TLP:CLEAR | 中 |
| source--barium--b2fc1a83e9e428da | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--barium--68a19d1b26dd988c | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--barium--db420ade9ac8e5ca | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--barium--aec9df3f01fe8a80 | APT blackberry mobile malware report |  | 不明 | summary/2020/APT-blackberry-mobile-malware-report.pdf | report | TLP:CLEAR | 中 |
| source--barium--95457a1e86f185fa | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--barium--7c9ff3fad63d6fda | Modern Asian APT groups TTPs report eng |  | 不明 | summary/2023/Modern-Asian-APT-groups-TTPs_report_eng.pdf | report | TLP:CLEAR | 中 |
| source--barium--818ca3056deabc96 | Secureworks NC3 2022StateoftheThreat |  | 2022 | summary/2023/Secureworks_NC3_2022StateoftheThreat.pdf | report | TLP:CLEAR | 中 |
| source--barium--eb48a9941711fdcc | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--barium--1daa9a873506d87b | Cloudflare 2026 threat report |  | 2026 | summary/2026/Cloudflare-2026-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
