# TA558 脅威アクタープロファイル

- プロファイルID: `actor--ta558`
- 状態: draft
- 更新日時: 2026-07-27T11:17:25Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

TA558の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **TA558**
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
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | TA558 | canonical-name | 高 |  | https://www.proofpoint.com/us/blog/threat-insight/reservations-requested-ta558-targets-hospitality-and-travel<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=TA558&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | TA558 | canonical-name | 高 |  |  |
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
| SteganoAmor攻撃が全世界の320の組織を標的に | malware-campaign | 不明 | 不明 | 2024-04-16 | SteganoAmorは画像内に隠された悪意あるコードを利用 TA558グループによる攻撃。様々な分野や国に影響を与えた320以上の攻撃が行われた TA558は、2018年から活動しており、標的は主にラテンアメリカのホスピタリティ関連組織 Microsoft Officeの脆弱性CVE-2017-11882を悪用 様々なマルウェアが配布される、AgentTeslaやFormBookなど | 中 | `source--daily-09539f0db091b1cf7875` |
| TA558、AI生成スクリプトを用いてブラジルのホテル攻撃でVenom RATを展開 | phishing-campaign | 不明 | 不明 | 2025-09-18 | 脅威グループTA558（KasperskyはRevengeHotelsとして追跡）が、ブラジルやスペイン語圏のホテルを狙いRATを配布。 2025年夏に観測。請求書や予約・採用通知を装うフィッシングで、ポルトガル語／スペイン語メールから感染を誘導。 LLM生成と推測されるコメント多めのJSローダーとPowerShellダウンローダーで最終的にVenom RATを展開。 Venom RATは窃取・リバースプロキシ・アンチキル・永続化を備え、特権化やDefender停止、USB経由拡散にも対応。 目的はホテルシステムやオンライン旅行代理店(OTA)（例: Booking[.]com）に保管された宿泊客のクレジットカード情報の窃取。 | 高 | `source--daily-f057489c6a517d53de51` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 5件（`artifacts.csv`）

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
| source--daily-09539f0db091b1cf7875 | SteganoAmor攻撃が全世界の320の組織を標的に | bleepingcomputer.com | 2024-04-16 | https://www.bleepingcomputer.com/news/security/new-steganoamor-attacks-use-steganography-to-target-320-orgs-globally/ | osint-report | TLP:CLEAR | 中 |
| source--daily-f057489c6a517d53de51 | TA558、AI生成スクリプトを用いてブラジルのホテル攻撃でVenom RATを展開 | thehackernews.com | 2025-09-18 | https://thehackernews.com/2025/09/ta558-uses-ai-generated-scripts-to.html | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--ta558--4fa855b571aca4ba | 2022cyberComprehensiveSituationObservationManual |  | 2022 | summary/2023/2022cyberComprehensiveSituationObservationManual.pdf | report | TLP:CLEAR | 中 |
| source--ta558--748588cb3831785d | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--ta558--c50b7358c4f07d6d | ta558 |  | 不明 | actor_profile/evidence/ta558.csv | structured-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
