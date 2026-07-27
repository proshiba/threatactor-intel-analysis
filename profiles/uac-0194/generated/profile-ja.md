# UAC-0194 脅威アクタープロファイル

- プロファイルID: `actor--uac-0194`
- 状態: draft
- 更新日時: 2026-07-27T11:04:37Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

UAC-0194の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UAC-0194**
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
| misp-threat-actor | UAC-0194 | canonical-name | 高 | RU | https://www.clearskysec.com/0d-vulnerability-exploited-in-the_wild/ |
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
| Microsoftがウクライナへの攻撃で悪用されたWindowsのゼロデイ脆弱性を修正 | phishing-campaign | 不明 | 不明 | 2024-11-14 | Microsoftは、ウクライナへのサイバー攻撃で悪用されていたWindowsのゼロデイ脆弱性を修正しました。 脆弱性CVE-2024-43451は、NTLMハッシュを不正に取得するため、攻撃者が準備したリモートサーバに接続を誘導する可能性があります。 この攻撃は、フィッシングメールのリンクを介して教育省サーバーから拡散されていました。 リンクは、この攻撃以前に侵害していたサーバー（osvita-kp.gov[.]ua）を悪用していました。 SparkRATを利用し、被害者のシステム制御を試みるリモートアクセスが確認されています。 Microsoftは11月のパッチで修正し、CISAは12月3日までの対応を勧告しました。 | 中 | `source--daily-f0e69b17ee92aa7c00c6` |



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
| source--daily-f0e69b17ee92aa7c00c6 | Microsoftがウクライナへの攻撃で悪用されたWindowsのゼロデイ脆弱性を修正 | bleepingcomputer.com | 2024-11-14 | https://www.bleepingcomputer.com/news/security/microsoft-patches-windows-zero-day-exploited-in-attacks-on-ukraine/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--uac-0194--401dc8fe4c0241c8 | Cybersecurity Threats 2024 Annual Report QAX |  | 2024 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | report | TLP:CLEAR | 中 |
| source--uac-0194--d9b7cb891c070366 | Zero day cve 2024 4351 report |  | 不明 | Exploit/Zero-day-cve-2024-4351-report.pdf | report | TLP:CLEAR | 中 |
| source--uac-0194--f5f31433703dd34f | uac 0194 |  | 不明 | actor_profile/evidence/uac-0194.csv | structured-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
