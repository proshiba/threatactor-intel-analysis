# Golden Chickens 脅威アクタープロファイル

- プロファイルID: `actor--golden-chickens`
- 状態: draft
- 更新日時: 2026-07-29T23:12:00Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Golden Chickensの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Golden Chickens**
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
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Venom Spider, Golden Chickens | canonical-name | 高 | Russia | https://quointelligence.eu/2018/11/golden-chickens-uncovering-a-malware-as-a-service-maas-provider-and-two-new-threat-actors-using/<br>https://medium.com/@quoscient/golden-chickens-uncovering-a-malware-as-a-service-maas-provider-and-two-new-threat-actors-using-61cf0cb87648<br>https://quointelligence.eu/2020/01/the-chicken-keeps-laying-new-eggs-uncovering-new-gc-maas-tools-used-by-top-tier-threat-actors/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | GC01 | canonical-name | 高 |  | https://medium.com/@quoscient/golden-chickens-uncovering-a-malware-as-a-service-maas-provider-and-two-new-threat-actors-using-61cf0cb87648 |
| misp-threat-actor | GC02 | canonical-name | 高 |  | https://medium.com/@quoscient/golden-chickens-uncovering-a-malware-as-a-service-maas-provider-and-two-new-threat-actors-using-61cf0cb87648 |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| GC01 | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| GC02 | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| More_eggsマルウェアが履歴書を装いリクルーターを狙うフィッシング攻撃 | phishing-campaign | 不明 | 不明 | 2024-06-11 |  |  | ttp--activity-rule--4215e3f64293aca10472, ttp--activity-rule--ad89cb22215867c0453f |  | More_eggsマルウェアが履歴書を装い、リクルーターをターゲットにフィッシング攻撃を実施 攻撃はLinkedIn経由で行われ、偽の履歴書ダウンロードサイトに誘導 マルウェアはLNKファイルを利用して悪意のあるDLLを取得し、regsvr32.exeで動かす。システムへの持続性を確保 More_eggsは、Golden Chickens（別名Venom Spider）とされるグループによるMaaSとして他のサイバー犯罪者に提供 | 中 | `source--daily-0e3e2f14439a2e9f9ca0` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 米国 | 構造化OSINTの被害国フィールドでGolden Chickensの標的・被害国として米国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Discovery | T1083 | File and Directory Discovery | More_eggsマルウェアが履歴書を装い、リクルーターをターゲットにフィッシング攻撃を実施 攻撃はLinkedIn経由で行われ、偽の履歴書ダウンロードサイトに誘導 マルウェアはLNKファイルを利用して悪意のあるDLLを取得し、regsvr32.exeで動かす。 |  | activity--daily-339c2ac36665ac48d8ab | 不明 | 不明 | 中 | `source--daily-0e3e2f14439a2e9f9ca0` |
| Stealth | T1218.010 | Regsvr32 | More_eggsマルウェアが履歴書を装い、リクルーターをターゲットにフィッシング攻撃を実施 攻撃はLinkedIn経由で行われ、偽の履歴書ダウンロードサイトに誘導 マルウェアはLNKファイルを利用して悪意のあるDLLを取得し、regsvr32.exeで動かす。 |  | activity--daily-339c2ac36665ac48d8ab | 不明 | 不明 | 中 | `source--daily-0e3e2f14439a2e9f9ca0` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 12件（`artifacts.csv`）

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
| source--daily-0e3e2f14439a2e9f9ca0 | More_eggsマルウェアが履歴書を装いリクルーターを狙うフィッシング攻撃 | thehackernews.com | 2024-06-11 | https://thehackernews.com/2024/06/moreeggs-malware-disguised-as-resumes.html | osint-report | TLP:CLEAR | 中 |
| source--golden-chickens--464f2da935c3e3bd | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--golden-chickens--6d0e5225b513bcbb | Unmasking VenomSpider Report Final |  | 不明 | International Strategic/Russia/GoldenChickens/Unmasking_VenomSpider_Report-Final.pdf | report | TLP:CLEAR | 中 |
| source--golden-chickens--7b514ff30a32bf4a | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--golden-chickens--de4e5cbc16bb4188 | golden chickens |  | 不明 | actor_profile/evidence/golden-chickens.csv | structured-data | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
