# UNC4393 脅威アクタープロファイル

- プロファイルID: `actor--unc4393`
- 状態: draft
- 更新日時: 2026-07-29T15:36:12Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

UNC4393の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC4393**
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
| misp-threat-actor | UNC4393 | canonical-name | 高 |  | https://cloud.google.com/blog/topics/threat-intelligence/unc4393-goes-gently-into-silentnight<br>https://www.security.com/threat-intelligence/black-basta-ransomware-zero-day<br>https://cloud.google.com/blog/topics/threat-intelligence/detecting-disrupting-malvertising-backdoors/ |
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
| Black Bastaランサムウェアグループ、戦略的攻撃のために再編成 | ransomware-extortion | 不明 | 不明 | 2024-11-26 | target--activity-rule--sector--dfc80b76cad93a318adc |  |  | victim--activity-rule--2667818ef83c855b1a5d | Black Bastaは、2022年に出現したランサムウェアグループで、企業を標的にしている。 同グループは、攻撃手法を進化させ、より戦略的な攻撃を展開している。 ボットネット主導のマルウェア配信に焦点を当てることから、綿密に計画されたソーシャルエンジニアリングキャンペーンを通じて標的を欺くことに焦点を移している。 Black Basta の最近の技術には、「大量のスパムメールを送信するために使用される戦術であるメール爆撃」が含まれる。メール爆撃後、Microsoft Teams を介したソーシャルエンジニアリングを行い、被害者のエンドユーザーを騙してリモート監視および管理ツールを介して初期アクセスを提供 悪意のある QR コードが組み込まれた Microsoft Teams の外部チャットメッセージに標的を追加することで、誘導。 彼らは、被害者のデータを暗号化し、身代金を要求する手口を用いている。 | 中 | `source--daily-3db6fd943f36fd38310f` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | 製造・産業 | 活動「Black Bastaランサムウェアグループ、戦略的攻撃のために再編成」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-3db6fd943f36fd38310f` |

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Black Bastaランサムウェアグループ、戦略的攻撃のために再編成 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--dfc80b76cad93a318adc |  |  | メール／メールアカウント | encryption: Black Bastaランサムウェアグループ、戦略的攻撃のために再編成 | 不明 | 不明 | 2024-11-26 | 中 | `source--daily-3db6fd943f36fd38310f` |

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 15件（`artifacts.csv`）

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
| source--daily-3db6fd943f36fd38310f | Black Bastaランサムウェアグループ、戦略的攻撃のために再編成 | databreachtoday.com | 2024-11-26 | https://www.databreachtoday.com/black-basta-ransomware-group-retools-for-strategic-attacks-a-26898 | osint-report | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unc4393--013f6813261c3d9e | Cybersecurity Threats 2024 Annual Report QAX |  | 2024 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | report | TLP:CLEAR | 中 |
| source--unc4393--22fd96d7cd5b64f2 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--unc4393--428e38eab46ab340 | M Trends 2023 Report MANDIANT SPECIAL REPORT |  | 2023 | summary/2023/M-Trends 2023 Report MANDIANT SPECIAL REPORT.pdf | report | TLP:CLEAR | 中 |
| source--unc4393--55005dc77614bc9e | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--unc4393--ad9e94092476adad | m trends 2024 |  | 2024 | summary/2024/m-trends-2024.pdf | report | TLP:CLEAR | 中 |
| source--unc4393--aeaa347def06fd80 | unc4393 |  | 不明 | actor_profile/evidence/unc4393.csv | structured-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
