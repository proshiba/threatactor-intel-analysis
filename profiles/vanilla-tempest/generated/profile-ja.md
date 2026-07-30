# Vanilla Tempest 脅威アクタープロファイル

- プロファイルID: `actor--vanilla-tempest`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Vanilla Tempestの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Vanilla Tempest**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| DEV-0832 | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |

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
| microsoft-threat-actor-mapping | Vanilla Tempest | canonical-name | 高 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Vanilla Tempest | canonical-name | 高 |  | https://www.microsoft.com/en-us/security/blog/2022/10/25/dev-0832-vice-society-opportunistic-ransomware-campaigns-impacting-us-education-sector/<br>https://fourcore.io/blogs/rhysida-ransomware-history-ttp-adversary-emulation<br>https://detect.fyi/rhysida-ransomware-and-the-detection-opportunities-3599e9a02bb2 |
| misp-microsoft-activity-group | Vanilla Tempest | canonical-name | 高 |  | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
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
| Microsoft：Vanilla Tempestが医療機関をINCランサムウェアで攻撃 | ransomware-extortion | 不明 | 不明 | 2024-09-19 | target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--sector--260bd106ff4950e5430d |  |  | victim--activity-rule--05f5af54d1d0b127513b | Vanilla Tempest(別名:DEV-0832、Vice Society)は米国の医療機関にINCランサムウェアを使用した攻撃を実施。 攻撃の一環として、Gootloader経由でネットワーク侵入し、SupperマルウェアやAnyDeskを使用した。 攻撃により患者データベースのアクセスが失われ、予定の変更を余儀なくされた。 Vanilla Tempestはランサムウェアのアフィリエイトであり、BlackCat、Quantum Locker、Zeppelin、Rhysidaなどのさまざまなランサムウェアを使用。 Vanilla Tempestは他にも教育、製造業、IT分野を標的にしている。 | 高 | `source--daily-c1b12b52abae4635e5ea` |
| Microsoftプラットフォームを悪用してマルウェアに署名していたサイバー犯罪サービスが妨害される | disruptive-activity | 不明 | 不明 | 2026-05-21 |  |  |  | victim--activity-rule--680c09627006db7a0e67 | Microsoftは、Artifact Signingを悪用してマルウェア用の不正なコード署名証明書を生成するMSaaS運営「Fox Tempest」を妨害した。 Fox Tempestは1,000件超の証明書と数百のAzureテナント・サブスクリプションを作成していたとされる。 Microsoftはsignspace[.]cloudを差し押さえ、関連する数百台の仮想マシンをオフライン化し、基盤へのアクセスを遮断した。 このサービスはOyster、Lumma Stealer、Vidar、Rhysida、Akira、INC、Qilin、BlackByteなどの活動に関連していた。 署名済みマルウェアはMicrosoft Teams、AnyDesk、PuTTY、Webexなど正規ソフトを装って配布されていた。 | 中 | `source--daily-1f90e973408c7fac0a86` |
| Microsoft、Teams利用者を狙うランサムウェア攻撃を妨害 | ransomware-extortion | 不明 | 不明 | 2025-10-17 | target--activity-rule--sector--260bd106ff4950e5430d, target--activity-rule--sector--dfc80b76cad93a318adc, target--activity-rule--sector--e7608f51421ca8b1e297 |  |  | victim--activity-rule--f98095af9352ea1ab8e2 | Microsoftは10月上旬のRhysida連携攻撃を妨害し、偽Teamsインストーラ署名に使われた200超の証明書を失効させた。 攻撃者Vanilla Tempest（Vice Society/VICE SPIDER）はteams-install[.]top等の偽サイトでOysterバックドアを配布した。 配布は9月下旬のマルバタイジングやSEOポイズニングで行われ、正規と同名MSTeamsSetup[.]exeで利用者を欺いた。 悪性インストーラは署名済みOysterを展開し、遠隔操作・情報窃取・追加ペイロード投下を可能にする。 同集団は金銭目的で教育・医療・IT・製造を頻繁に標的化し、近年は主にRhysidaを展開している。 | 中 | `source--daily-5287a969660d1bb7e309` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 米国 | 活動「Microsoft：Vanilla Tempestが医療機関をINCランサムウェアで攻撃」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-c1b12b52abae4635e5ea` |
| sectors | 医療・ヘルスケア | 活動「Microsoft：Vanilla Tempestが医療機関をINCランサムウェアで攻撃」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-5287a969660d1bb7e309`, `source--daily-c1b12b52abae4635e5ea` |
| sectors | 製造・産業 | 活動「Microsoft、Teams利用者を狙うランサムウェア攻撃を妨害」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-5287a969660d1bb7e309` |
| sectors | 教育・研究 | 活動「Microsoft、Teams利用者を狙うランサムウェア攻撃を妨害」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-5287a969660d1bb7e309` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Microsoft：Vanilla Tempestが医療機関をINCランサムウェアで攻撃 | 非公開 | anonymous | unknown | reported | target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--sector--260bd106ff4950e5430d |  |  |  | encryption: Microsoft：Vanilla Tempestが医療機関をINCランサムウェアで攻撃 | 不明 | 不明 | 2024-09-19 | 高 | `source--daily-c1b12b52abae4635e5ea` |
| 被害事例: Microsoftプラットフォームを悪用してマルウェアに署名していたサイバー犯罪サービスが妨害される | 非公開 | anonymous | unknown | reported |  |  |  |  |  | 不明 | 不明 | 2026-05-21 | 中 | `source--daily-1f90e973408c7fac0a86` |
| 被害事例: Microsoft、Teams利用者を狙うランサムウェア攻撃を妨害 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--260bd106ff4950e5430d, target--activity-rule--sector--dfc80b76cad93a318adc, target--activity-rule--sector--e7608f51421ca8b1e297 |  |  |  | encryption: Microsoft、Teams利用者を狙うランサムウェア攻撃を妨害 | 不明 | 不明 | 2025-10-17 | 中 | `source--daily-5287a969660d1bb7e309` |

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
| source--daily-1f90e973408c7fac0a86 | Microsoftプラットフォームを悪用してマルウェアに署名していたサイバー犯罪サービスが妨害される | microsoft.com | 2026-05-21 | https://www.microsoft.com/en-us/security/blog/2026/05/19/exposing-fox-tempest-a-malware-signing-service-operation/ | osint-report | TLP:CLEAR | 中 |
| source--daily-5287a969660d1bb7e309 | Microsoft、Teams利用者を狙うランサムウェア攻撃を妨害 | bleepingcomputer.com | 2025-10-17 | https://www.bleepingcomputer.com/news/microsoft/microsoft-disrupts-ransomware-attacks-targeting-teams-users/ | osint-report | TLP:CLEAR | 中 |
| source--daily-c1b12b52abae4635e5ea | Microsoft：Vanilla Tempestが医療機関をINCランサムウェアで攻撃 | bleepingcomputer.com | 2024-09-19 | https://www.bleepingcomputer.com/news/microsoft/microsoft-vanilla-tempest-hit-healthcare-with-inc-ransomware/ | osint-report | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--vanilla-tempest--8a1291014fecfa23 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--vanilla-tempest--aaf7df4e91b7c721 | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--vanilla-tempest--b98106625f6c9506 | vanilla tempest |  | 不明 | actor_profile/evidence/vanilla-tempest.csv | structured-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
