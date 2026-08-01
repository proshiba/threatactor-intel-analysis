# TA547 脅威アクタープロファイル

- プロファイルID: `actor--ta547`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

TA547の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **TA547**
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
| etda-threat-group-cards | Scully Spider, TA547 | canonical-name | 高 |  | https://www.proofpoint.com/us/threat-insight/post/danabot-new-banking-trojan-surfaces-down-under-0<br>https://h3collective.io/review-of-a-danabot-infection/<br>https://www.fortinet.com/blog/threat-research/breakdown-of-a-targeted-danabot-attack.html |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | TA547 | canonical-name | 高 |  | https://www.thaicert.or.th/downloads/files/Threat_Group_Cards_v2.0.pdf |
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
| 悪意あるPowerShellスクリプトがマルウェアを配布、スクリプトがAIによって作成された可能性 | phishing-campaign | 2023-03 | 2023-03 | 2024-04-11 |  |  | ttp--activity-rule--4dc10c9afacef7260003, ttp--activity-rule--b33ceb1943ccf057e2ec, ttp--activity-rule--ce7d1017411c75b1dc88 |  | AI技術を使用して作成された可能性がある悪意あるPowerShellスクリプトがRhadamanthys情報窃取マルウェアを配布 スクリプトは2023年3月にドイツの多数の組織を狙ったメールキャンペーンで使用された 攻撃者TA547はMetroキャッシュ＆キャリーブランドになりすましたメールで組織をだましてZIPアーカイブを開かせる PowerShellスクリプトは、メモリ内で直接実行されるようBase64でエンコードされたRhadamanthys実行可能ファイルをデコード AIによるコード生成技術の利用が疑われるが、確証はない | 中 | `source--daily-4e35e5a6c9eb6f31a645` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| 悪意あるPowerShellスクリプトがマルウェアを配布、スクリプトがAIによって作成された可能性 | TA547 | 情報なし | T1059.001 PowerShell, T1560.001 Archive via Utility, T1140 Deobfuscate/Decode Files or Information | 情報なし | 情報なし | 情報なし | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | イタリア | 構造化OSINTの被害国フィールドでTA547の標的・被害国としてイタリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イラク | 構造化OSINTの被害国フィールドでTA547の標的・被害国としてイラクが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ウクライナ | 構造化OSINTの被害国フィールドでTA547の標的・被害国としてウクライナが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オーストラリア | 構造化OSINTの被害国フィールドでTA547の標的・被害国としてオーストラリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オーストリア | 構造化OSINTの被害国フィールドでTA547の標的・被害国としてオーストリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | カナダ | 構造化OSINTの被害国フィールドでTA547の標的・被害国としてカナダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | コロンビア | 構造化OSINTの被害国フィールドでTA547の標的・被害国としてコロンビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | スイス | 構造化OSINTの被害国フィールドでTA547の標的・被害国としてスイスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | スペイン | 構造化OSINTの被害国フィールドでTA547の標的・被害国としてスペインが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ドイツ | 構造化OSINTの被害国フィールドでTA547の標的・被害国としてドイツが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ニュージーランド | 構造化OSINTの被害国フィールドでTA547の標的・被害国としてニュージーランドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ブラジル | 構造化OSINTの被害国フィールドでTA547の標的・被害国としてブラジルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ポーランド | 構造化OSINTの被害国フィールドでTA547の標的・被害国としてポーランドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | 構造化OSINTの被害国フィールドでTA547の標的・被害国として米国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 英国 | 構造化OSINTの被害国フィールドでTA547の標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 香港 | 構造化OSINTの被害国フィールドでTA547の標的・被害国として香港が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | オセアニア | オーストラリア、ニュージーランドで確認された標的・被害事例をオセアニアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 中南米 | コロンビア、ブラジルで確認された標的・被害事例を中南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 北米 | カナダ、米国で確認された標的・被害事例を北米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 南欧 | イタリア、スペインで確認された標的・被害事例を南欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 南米 | コロンビア、ブラジルで確認された標的・被害事例を南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東欧 | ウクライナ、ポーランドで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | イタリア、ウクライナ、オーストリア、スイス、スペイン、ドイツ、ポーランド、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution | T1059.001 | PowerShell | 悪意あるPowerShellスクリプトがマルウェアを配布、スクリプトがAIによって作成された可能性 |  | activity--daily-6d5bdadebf1a9b6fccc5 | 2023-03 | 2023-03 | 中 | `source--daily-4e35e5a6c9eb6f31a645` |
| Collection | T1560.001 | Archive via Utility | AI技術を使用して作成された可能性がある悪意あるPowerShellスクリプトがRhadamanthys情報窃取マルウェアを配布 スクリプトは2023年3月にドイツの多数の組織を狙ったメールキャンペーンで使用された 攻撃者TA547はMetroキャッシュ＆キャリーブランドになりすましたメールで組織をだましてZIPアーカイブを開かせる PowerShellスクリプトは、メモリ内で直接実行されるようBase64でエンコードされたRhadamanthys実行可能ファイルをデコード AIによるコード生成技術の利用が疑われるが、確証はない |  | activity--daily-6d5bdadebf1a9b6fccc5 | 2023-03 | 2023-03 | 中 | `source--daily-4e35e5a6c9eb6f31a645` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | ys情報窃取マルウェアを配布 スクリプトは2023年3月にドイツの多数の組織を狙ったメールキャンペーンで使用された 攻撃者TA547はMetroキャッシュ＆キャリーブランドになりすましたメールで組織をだましてZIPアーカイブを開かせる PowerShellスクリプトは、メモリ内で直接実行されるようBase64でエンコードされたRhadamanthys実行可能ファイルをデコード AIによるコード生成技術の利用が疑われるが、確証はない |  | activity--daily-6d5bdadebf1a9b6fccc5 | 2023-03 | 2023-03 | 中 | `source--daily-4e35e5a6c9eb6f31a645` |

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 13件（`artifacts.csv`）

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
| source--daily-4e35e5a6c9eb6f31a645 | 悪意あるPowerShellスクリプトがマルウェアを配布、スクリプトがAIによって作成された可能性 | bleepingcomputer.com | 2024-04-11 | https://www.bleepingcomputer.com/news/security/malicious-powershell-script-pushing-malware-looks-ai-written/ | osint-report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--ta547--3a26b7d958dde0c9 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--ta547--40c697ba6bfa27b6 | state of the threat report 2024 |  | 2024 | summary/2024/state-of-the-threat-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--ta547--77681344f6deb05c | ta547 |  | 不明 | actor_profile/evidence/ta547.csv | structured-data | TLP:CLEAR | 中 |
| source--ta547--dcd9195a4b26e097 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
