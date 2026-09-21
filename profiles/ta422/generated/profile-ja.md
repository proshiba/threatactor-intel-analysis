# TA422 脅威アクタープロファイル

- プロファイルID: `actor--ta422`
- 状態: draft
- 更新日時: 2026-09-21T04:35:03Z
- 構造バージョン: 1.3.0

## エグゼクティブサマリー

TA422の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **TA422**
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
- 調査日時: 2026-09-21T02:39:13Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | Sofacy, APT 28, Fancy Bear, Sednit | canonical-name | 高 | Russia | https://securelist.com/sofacy-apt-hits-high-profile-targets-with-updated-toolset/72924/<br>http://download.bitdefender.com/resources/media/materials/white-papers/en/Bitdefender_In-depth_analysis_of_APT28%E2%80%93The_Political_Cyber-Espionage.pdf<br>https://securelist.com/a-slice-of-2017-sofacy-activity/83930/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | APT28 | canonical-name | 高 | RU, Russian Federation | https://attack.mitre.org/groups/G0007/<br>https://en.wikipedia.org/wiki/Fancy_Bear<br>https://en.wikipedia.org/wiki/Sofacy_Group |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | 一致なし |  |  |  |  |

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
| 国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開 | phishing-campaign | 不明 | 不明 | 2025-04-18 | target--targeting-audit--country--125e563a9a62cd92b307, target--targeting-audit--country--a02303084613eafa1fdb, target--targeting-audit--country--de555bc59f8ab43a5b0c |  | ttp--activity-rule--8081fa6e652256cf2728 | victim--activity-rule--971d498a43ed69e6e34a | 中国・イラン・ロシア・北朝鮮支援のAPTがClickFixを用いたフィッシング攻撃を展開。 TA427 (Kimsuky): 2025年1月と2月に、シンクタンク部門の少数組織の個人を標的としたフィッシングキャンペーンでClickFixを使用 TA450 (MuddyWater): イランに関連するこのグループは、持続的なアクセスを維持するために、Levelなどの正当なリモート監視および管理 (RMM) ソフトウェアを悪用するためにClickFixを利用 UNK_RemoteRogue: 2024年末に確認されたこのロシアの可能性のあるグループは、侵害された可能性のあるZimbraサーバーから送信された、Microsoft Officeドキュメントへのリンクを含むおとりメールを使用してClickFixを使用 PowerShellコマンドを利用しQuasar RATやRMMソフトを導入。 日本大使館を装った誘導や、YouTube動画を含む偽ページなどを利用。 | 中 | `source--daily-07ef6046e1668f840b3a` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| 国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開 | TA422 | 情報なし | T1204.004 Malicious Copy and Paste | 情報なし | イラン, ロシア, 中国 | 被害事例: 国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開 | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | イラン | 活動「国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開」の記述で標的・被害国として明示されている。 | 不明 | 不明 | 中 | `source--daily-07ef6046e1668f840b3a` |
| countries | ロシア | 活動「国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開」の記述で標的・被害国として明示されている。 | 不明 | 不明 | 中 | `source--daily-07ef6046e1668f840b3a` |
| countries | 中国 | 活動「国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開」の記述で標的・被害国として明示されている。 | 不明 | 不明 | 中 | `source--daily-07ef6046e1668f840b3a` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開 | 非公開 | anonymous | unknown | reported |  |  | ttp--activity-rule--8081fa6e652256cf2728 |  |  | 不明 | 不明 | 2025-04-18 | 中 | `source--daily-07ef6046e1668f840b3a` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution | T1204.004 | Malicious Copy and Paste | 国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開 |  | activity--daily-4dbf28fc88ea904541ab | 不明 | 不明 | 中 | `source--daily-07ef6046e1668f840b3a` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

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
| source--daily-07ef6046e1668f840b3a | 国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開 | thehackernews.com | 2025-04-18 | https://thehackernews.com/2025/04/state-sponsored-hackers-weaponize.html | osint-report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--ta422--16fb561dcabc6f55 | 2023 Network Vulnerability Situation Research Report |  | 2023 | summary/2024/2023 Network Vulnerability Situation Research Report.pdf | report | TLP:CLEAR | 中 |
| source--ta422--7fd387441a658629 | Qianxin 2023 APT Report |  | 2023 | summary/2024/Qianxin 2023 APT Report.pdf | report | TLP:CLEAR | 中 |
| source--ta422--f4cdd55af197fe3c | ta422 |  | 不明 | actor_profile/evidence/ta422.csv | structured-data | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
