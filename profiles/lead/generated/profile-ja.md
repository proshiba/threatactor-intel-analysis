# LEAD 脅威アクタープロファイル

- プロファイルID: `actor--lead`
- 状態: draft
- 更新日時: 2026-07-25T14:07:08Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

LEADの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **LEAD**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Winnti Umbrella | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| Winnti | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 42; mapping requires review. |

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
| BARIUM | overlaps-with | 共有alias: Winnti Umbrella | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |
| Ke3chang | overlaps-with | 共有alias: Winnti Umbrella | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |
| PassCV | overlaps-with | 共有alias: Winnti Umbrella | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability | Winnti Rootkit malware |
| Infrastructure |  |
| Victim | Multinational, multi-industry companies, textiles, chemicals, electronics, pharmaceutical companies, manufacturing |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Lead | canonical-name | 高 | China | https://www.microsoft.com/security/blog/2017/01/25/detecting-threat-actors-in-recent-german-industrial-attacks-with-windows-defender-atp/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Lead&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Leopard Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | APT41 | canonical-name | 高 | CN, People's Republic of China | https://securelist.com/winnti-faq-more-than-just-a-game/57585/<br>https://securelist.com/winnti-more-than-just-a-game/37029/<br>http://williamshowalter.com/a-universal-windows-bootkit/ |
| misp-microsoft-activity-group | LEAD | canonical-name | 高 |  | https://blogs.technet.microsoft.com/mmpc/2017/01/25/detecting-threat-actors-in-recent-german-industrial-attacks-with-windows-defender-atp/ |
| misp-microsoft-activity-group | Leopard Typhoon | canonical-name | 高 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
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
| malware--winnti-rootkit-malware | Winnti Rootkit malware | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | Healthcare | Targeting text indicates the Healthcare sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Manufacturing | Targeting text indicates the Manufacturing sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 23件（`artifacts.csv`）

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
| source--lead--d2e007343a0b4783 | lead |  | 不明 | actor_profile/evidence/lead.csv | structured-data | TLP:CLEAR | 中 |
| source--lead--7335bb22a5d9a015 | china cyber report |  | 不明 | International Strategic/China/china-cyber-report.pdf | report | TLP:CLEAR | 中 |
| source--lead--0b3471c45a608aa4 | Dream Job Campaign |  | 不明 | lazarus/Dream-Job-Campaign.pdf | report | TLP:CLEAR | 中 |
| source--lead--eebc4288c68615b4 | APT blackberry mobile malware report |  | 不明 | summary/2020/APT-blackberry-mobile-malware-report.pdf | report | TLP:CLEAR | 中 |
| source--lead--6f4462f54dae849c | Estonian Foreign Intelligence raport 2020 en |  | 2020 | summary/2020/Estonian-Foreign-Intelligence-raport-2020-en.pdf | report | TLP:CLEAR | 中 |
| source--lead--ecd3e54d7081efed | 2021 Threat Detection Report |  | 2021 | summary/2021/2021-Threat-Detection-Report.pdf | report | TLP:CLEAR | 中 |
| source--lead--37f1c850d3acb2c3 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--lead--ece646dc5eefc2f2 | WEF Global Cybersecurity Outlook 2022 |  | 2022 | summary/2022/WEF_Global_Cybersecurity_Outlook_2022.pdf | report | TLP:CLEAR | 中 |
| source--lead--47473e284d825887 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--lead--2002b170087558d6 | Cloudflare 2026 threat report |  | 2026 | summary/2026/Cloudflare-2026-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--lead--0934a95d729ff7b9 | eset apt activity report q4 2025 q1 2026 |  | 2025 | summary/2026/eset-apt-activity-report-q4-2025-q1-2026.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
