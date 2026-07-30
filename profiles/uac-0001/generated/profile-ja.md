# UAC-0001 脅威アクタープロファイル

- プロファイルID: `actor--uac-0001`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

UAC-0001の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UAC-0001**
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
| cert-ua-uac-index | UAC-0001 | canonical-name | 高 |  | https://cert.gov.ua/article/6281123<br>https://cert.gov.ua/article/6287250 |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | APT28 | canonical-name | 高 | RU, Russian Federation | https://attack.mitre.org/groups/G0007/<br>https://en.wikipedia.org/wiki/Fancy_Bear<br>https://en.wikipedia.org/wiki/Sofacy_Group |
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
| APTグループ「Pawn Storm」がマルウェア群「PRISMEX」を展開：政府機関や重要インフラ関連組織への攻撃を確認 | cyber-espionage | 不明 | 不明 | 2026-04-22 | target--activity-rule--country--36f1b9323d5faab92f39, target--activity-rule--country--72caf60a2fbce4a1be7a, target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--b94dc560a327b601965d |  | ttp--activity-rule--0200d906a0fd1da614c8 | victim--activity-rule--901695fa9c5e37834e54 | ロシア背景のPawn Stormは、PRISMEXと総称される連携型マルウェア群を用い、ウクライナやNATO加盟国の防衛サプライチェーンを標的にした。 攻撃ではステガノグラフィ、COMハイジャック、正規クラウドサービス悪用を組み合わせ、EDR回避とC&C通信を実現していた。 2026年1月下旬のキャンペーンではCVE-2026-21509が悪用され、関連検体ではCVE-2026-21513のゼロデイ悪用も確認された。 PRISMEXはPrismexSheet、PrismexDrop、PrismexLoader、PrismexStagerで構成され、Filen系サブドメインを使ってCovenant経由の通信を行う。 調査ではサイバー諜報だけでなく、%USERPROFILE%配下を削除するワイパーコマンドも見つかり、破壊工作の可能性も示された。 | 中 | `source--daily-183d3d6935d0c269b0c9` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アフガニスタン | 構造化OSINTの被害国フィールドでUAC-0001の標的・被害国としてアフガニスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | アルメニア | 構造化OSINTの被害国フィールドでUAC-0001の標的・被害国としてアルメニアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ウクライナ | 活動「APTグループ「Pawn Storm」がマルウェア群「PRISMEX」を展開：政府機関や重要インフラ関連組織への攻撃を確認」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-183d3d6935d0c269b0c9`, `source--target-audit-misp-threat-actor` |
| countries | カザフスタン | 構造化OSINTの被害国フィールドでUAC-0001の標的・被害国としてカザフスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ジョージア | 構造化OSINTの被害国フィールドでUAC-0001の標的・被害国としてジョージアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | タジキスタン | 構造化OSINTの被害国フィールドでUAC-0001の標的・被害国としてタジキスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | トルコ | 構造化OSINTの被害国フィールドでUAC-0001の標的・被害国としてトルコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ドイツ | 構造化OSINTの被害国フィールドでUAC-0001の標的・被害国としてドイツが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ハンガリー | 構造化OSINTの被害国フィールドでUAC-0001の標的・被害国としてハンガリーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | パキスタン | 構造化OSINTの被害国フィールドでUAC-0001の標的・被害国としてパキスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | フランス | 構造化OSINTの被害国フィールドでUAC-0001の標的・被害国としてフランスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ベルギー | 構造化OSINTの被害国フィールドでUAC-0001の標的・被害国としてベルギーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ポーランド | 構造化OSINTの被害国フィールドでUAC-0001の標的・被害国としてポーランドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | モンゴル | 構造化OSINTの被害国フィールドでUAC-0001の標的・被害国としてモンゴルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ヨルダン | 構造化OSINTの被害国フィールドでUAC-0001の標的・被害国としてヨルダンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ロシア | 活動「APTグループ「Pawn Storm」がマルウェア群「PRISMEX」を展開：政府機関や重要インフラ関連組織への攻撃を確認」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-183d3d6935d0c269b0c9` |
| countries | 中国 | 構造化OSINTの被害国フィールドでUAC-0001の標的・被害国として中国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | 日本 | 構造化OSINTの被害国フィールドでUAC-0001の標的・被害国として日本が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | 米国 | 構造化OSINTの被害国フィールドでUAC-0001の標的・被害国として米国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | 英国 | 構造化OSINTの被害国フィールドでUAC-0001の標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| regions | NATO加盟国 | 活動「APTグループ「Pawn Storm」がマルウェア群「PRISMEX」を展開：政府機関や重要インフラ関連組織への攻撃を確認」の記述で標的地域としてNATO加盟国が明示されている。 | 不明 | 不明 | 中 | `source--daily-183d3d6935d0c269b0c9`, `source--target-audit-misp-threat-actor` |
| regions | アジア太平洋 | 構造化OSINTの被害地域フィールドでUAC-0001の標的範囲としてアジア太平洋が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| regions | コーカサス | アルメニア、ジョージアで確認された標的・被害事例をコーカサスとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| regions | 中央アジア | カザフスタン、タジキスタンで確認された標的・被害事例を中央アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| regions | 中東 | トルコ、ヨルダンで確認された標的・被害事例を中東として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| regions | 南アジア | アフガニスタン、パキスタンで確認された標的・被害事例を南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| regions | 東アジア | モンゴル、中国、日本で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| regions | 東欧 | ウクライナ、ハンガリー、ポーランド、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-183d3d6935d0c269b0c9`, `source--target-audit-misp-threat-actor` |
| regions | 欧州 | 構造化OSINTの被害地域フィールドでUAC-0001の標的範囲として欧州が記録されている。 | 不明 | 不明 | 中 | `source--daily-183d3d6935d0c269b0c9`, `source--target-audit-misp-threat-actor` |
| sectors | 政府・行政 | 活動「APTグループ「Pawn Storm」がマルウェア群「PRISMEX」を展開：政府機関や重要インフラ関連組織への攻撃を確認」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-183d3d6935d0c269b0c9` |
| sectors | 防衛・軍事 | 活動「APTグループ「Pawn Storm」がマルウェア群「PRISMEX」を展開：政府機関や重要インフラ関連組織への攻撃を確認」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-183d3d6935d0c269b0c9` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: APTグループ「Pawn Storm」がマルウェア群「PRISMEX」を展開：政府機関や重要インフラ関連組織への攻撃を確認 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--36f1b9323d5faab92f39, target--activity-rule--country--72caf60a2fbce4a1be7a, target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--b94dc560a327b601965d |  | ttp--activity-rule--0200d906a0fd1da614c8 | クラウド／SaaS | destruction: 調査ではサイバー諜報だけでなく、%USERPROFILE%配下を削除するワイパーコマンドも見つかり、破壊工作の可能性も示された。<br>espionage: 調査ではサイバー諜報だけでなく、%USERPROFILE%配下を削除するワイパーコマンドも見つかり、破壊工作の可能性も示された。 | 不明 | 不明 | 2026-04-22 | 中 | `source--daily-183d3d6935d0c269b0c9` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Impact | T1485 | Data Destruction | 調査ではサイバー諜報だけでなく、%USERPROFILE%配下を削除するワイパーコマンドも見つかり、破壊工作の可能性も示された。 |  | activity--daily-00e51d0ed75215a24fee | 不明 | 不明 | 中 | `source--daily-183d3d6935d0c269b0c9` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
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
| source--daily-183d3d6935d0c269b0c9 | APTグループ「Pawn Storm」がマルウェア群「PRISMEX」を展開：政府機関や重要インフラ関連組織への攻撃を確認 | trendmicro.com | 2026-04-22 | https://www.trendmicro.com/ja_jp/research/26/d/pawn-storm-targets-govt-infra.html | osint-report | TLP:CLEAR | 中 |
| source--osint-cert-ua-uac-index | CERT-UA UAC Article Index | CERT-UA | 不明 | actor_profile/reference/osint/cert-ua-uac-index.json | government-cert-article-index | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--uac-0001--26bdbcc83365e3fe | CERTFR 2025 CTI 007 |  | 2025 | APT28/CERTFR-2025-CTI-007.pdf | report | TLP:CLEAR | 中 |
| source--uac-0001--50f4adb1177b4d95 | Cyber operations by russia new goals, tools and groups |  | 不明 | International Strategic/Russia/Cyber operations by russia new goals, tools and groups.pdf | report | TLP:CLEAR | 中 |
| source--uac-0001--5e59f4c3e1675fd5 | uac 0001 |  | 不明 | actor_profile/evidence/uac-0001.csv | structured-data | TLP:CLEAR | 中 |
| source--uac-0001--b6eaa0164d8e8fa5 | Cyber Threat Intelligence Report 2025 2 |  | 2025 | summary/2025/Cyber Threat Intelligence Report 2025 2.pdf | report | TLP:CLEAR | 中 |
| source--uac-0001--c7a54bcc2d7d227d | CERTFR 2026 CTI 003 |  | 2026 | summary/2026/CERTFR-2026-CTI-003.pdf | report | TLP:CLEAR | 中 |
| source--uac-0001--e9aee5c565abec18 | Russian Cyber Operations Attack Automation, Espionage Against Defense Sector and New Tactics |  | 不明 | International Strategic/Russia/Russian Cyber Operations Attack Automation, Espionage Against Defense Sector and New Tactics.pdf | report | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
