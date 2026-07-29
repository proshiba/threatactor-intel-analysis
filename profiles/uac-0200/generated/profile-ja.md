# UAC-0200 脅威アクタープロファイル

- プロファイルID: `actor--uac-0200`
- 状態: draft
- 更新日時: 2026-07-27T11:17:26Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

UAC-0200の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UAC-0200**
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
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | UAC-0200 | canonical-name | 高 |  | https://cert.gov.ua/article/6282737 |
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
| ウクライナ軍が新たなSignalスピアフィッシング攻撃の標的に | phishing-campaign | 不明 | 不明 | 2025-03-20 | ウクライナのコンピュータ緊急対応チーム（CERT-UA）は、防衛産業企業の従業員や軍関係者を狙ったSignalアカウントを悪用したマルウェア攻撃を警告。 攻撃者は、会議報告書を装ったアーカイブをSignalメッセージで送信し、既存の連絡先からのメッセージとして信頼性を高めている。 アーカイブ内にはPDFと実行ファイルが含まれ、PDFを開くと実行ファイルを起動するように促される。この実行ファイルからDarkTortillaと呼ばれるマルウェアが展開される。 DarkTortillaは、リモートアクセス型トロイの木馬（RAT）であるDark Crystal RAT（DCRAT）を復号・実行する。 この攻撃活動は、2024年6月以降「UAC-0200」として追跡されており、2025年2月以降、無人航空機（UAV）や電子戦システムなどの軍事技術に関するテーマを餌にしている。 | 中 | `source--daily-1b5373977ade6efec051` |



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
- 非IOC artifact観測: 2件（`artifacts.csv`）

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
| source--daily-1b5373977ade6efec051 | ウクライナ軍が新たなSignalスピアフィッシング攻撃の標的に | bleepingcomputer.com | 2025-03-20 | https://www.bleepingcomputer.com/news/security/ukrainian-military-targeted-in-new-signal-spear-phishing-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-cert-ua-uac-index | CERT-UA UAC Article Index | CERT-UA | 不明 | actor_profile/reference/osint/cert-ua-uac-index.json | government-cert-article-index | TLP:CLEAR | 高 |
| source--uac-0200--7e3a4b353fb977dd | CERTFR 2025 CTI 004 |  | 2025 | summary/2025/CERTFR-2025-CTI-004.pdf | report | TLP:CLEAR | 中 |
| source--uac-0200--80b75f730585a4a0 | Cyber operations by russia new goals, tools and groups |  | 不明 | International Strategic/Russia/Cyber operations by russia new goals, tools and groups.pdf | report | TLP:CLEAR | 中 |
| source--uac-0200--850858c536601d79 | uac 0200 |  | 不明 | actor_profile/evidence/uac-0200.csv | structured-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
