# UNC5820 脅威アクタープロファイル

- プロファイルID: `actor--unc5820`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

UNC5820の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC5820**
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
| misp-threat-actor | UNC5820 | canonical-name | 高 |  | https://cloud.google.com/blog/topics/threat-intelligence/fortimanager-zero-day-exploitation-cve-2024-47575/ |
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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Mandiant、新たなFortinet FortiManager脆弱性が6月から悪用されていると報告 | intrusion | 不明 | 不明 | 2024-10-25 |  |  |  | victim--activity-rule--41b13ed1fc20995ddb16 | Mandiantは、Fortinet FortiManagerの脆弱性（CVE-2024-47575）が6月以降に50台以上のサーバーで悪用されていると報告。 Mandiantは、「UNC5820」と呼ばれる脅威アクターが、2024年6月27日からFortiManagerデバイスを悪用していることを発見。 攻撃者は未認証のAPIコマンドを利用し、FortiGateデバイスの構成情報を盗み出す。 侵害されたデバイスのメモリを分析したが、悪意のあるペイロードやシステムファイルの改ざんの兆候は見つからなかった。 攻撃者はデバイスからデータを抜き取ったが、このデバイスを使って、横方向に拡散したり、ネットワークに侵入したりした兆候はない。 Fortinetは既に修正パッチと緩和策を公開。 | 中 | `source--daily-ed6655e2b5b3dfb73449` |



## ターゲット

ターゲット情報なし

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Mandiant、新たなFortinet FortiManager脆弱性が6月から悪用されていると報告 | 非公開 | anonymous | unknown | reported |  |  |  | サーバー |  | 不明 | 不明 | 2024-10-25 | 中 | `source--daily-ed6655e2b5b3dfb73449` |

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 8件（`artifacts.csv`）

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
| source--daily-ed6655e2b5b3dfb73449 | Mandiant、新たなFortinet FortiManager脆弱性が6月から悪用されていると報告 | bleepingcomputer.com | 2024-10-25 | https://www.bleepingcomputer.com/news/security/mandiant-says-new-fortinet-fortimanager-flaw-has-been-exploited-since-june/ | osint-report | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unc5820--1f21514fedcc496c | unc5820 |  | 不明 | actor_profile/evidence/unc5820.csv | structured-data | TLP:CLEAR | 中 |
| source--unc5820--4d02ae697eca83ac | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--unc5820--9a1030814ebda99e | PL Report CP 2024 |  | 2024 | summary/2025/PL_Report_CP_2024.pdf | report | TLP:CLEAR | 中 |
| source--unc5820--dbe57843e4e901ef | Cybersecurity Threats 2024 Annual Report QAX |  | 2024 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | report | TLP:CLEAR | 中 |
| source--unc5820--ddd57eb55f808376 | 2024 Annual Cybersecurity Vulnerability Threat Landscape Research Report |  | 2024 | summary/2025/2024_Annual_Cybersecurity_Vulnerability_Threat_Landscape_Research_Report.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
