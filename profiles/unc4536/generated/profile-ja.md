# UNC4536 脅威アクタープロファイル

- プロファイルID: `actor--unc4536`
- 状態: draft
- 更新日時: 2026-07-27T11:17:26Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

UNC4536の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC4536**
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
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | UNC4536 | canonical-name | 高 |  | https://www.googlecloudcommunity.com/gc/Community-Blog/Finding-Malware-Unveiling-NUMOZYLOD-with-Google-Security/ba-p/789551 |
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
| 人気のソフトウェア検索を悪用するサイバー犯罪者 | phishing-campaign | 不明 | 不明 | 2024-08-20 | サイバー犯罪者が、不正広告キャンペーンを通じて、FakeBatと呼ばれるローダーを拡散 感染には、トロイの木馬化されたMSIXインストーラーが使用される。このインストーラは、PowerShellスクリプトを実行してペイロードをダウンロード 被害者はBraveやKeePassなどになりすましたインストーラーを使って感染させる。 FakeBatはEugenfestという脅威アクターに関連付けられる。また、このマルウェアはMaaSで提供されており、このMaaSの提供元をUNC4536として追跡。 FakeBatは、IcedID、RedLine Stealer、Lumma Stealer、SectopRAT、Carbanakなどの他マルウェアの配信に使用。 | 中 | `source--daily-b4aa05b2cb79bd0a59d6` |



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
- 非IOC artifact観測: 1件（`artifacts.csv`）

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
| source--daily-b4aa05b2cb79bd0a59d6 | 人気のソフトウェア検索を悪用するサイバー犯罪者 | thehackernews.com | 2024-08-20 | https://thehackernews.com/2024/08/cybercriminals-exploit-popular-software.html | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unc4536--1a9cdc39c7ff3468 | unc4536 |  | 不明 | actor_profile/evidence/unc4536.csv | structured-data | TLP:CLEAR | 中 |
| source--unc4536--6875735979c7f9cb | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
