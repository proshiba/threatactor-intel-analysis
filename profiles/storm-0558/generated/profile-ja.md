# Storm-0558 脅威アクタープロファイル

- プロファイルID: `actor--storm-0558`
- 状態: draft
- 更新日時: 2026-07-29T15:36:11Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Storm-0558の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Storm-0558**
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
| etda-threat-group-cards | Storm-0558 | canonical-name | 高 | China | https://www.microsoft.com/en-us/security/blog/2023/07/14/analysis-of-storm-0558-techniques-for-unauthorized-email-access/<br>https://www.wiz.io/blog/storm-0558-compromised-microsoft-key-enables-authentication-of-countless-micr<br>https://msrc.microsoft.com/blog/2023/09/results-of-major-technical-investigations-for-storm-0558-key-acquisition/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Antique Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Storm-0558 | canonical-name | 高 | CN, China | https://www.microsoft.com/en-us/security/blog/2023/07/14/analysis-of-storm-0558-techniques-for-unauthorized-email-access/<br>https://www.wiz.io/blog/storm-0558-compromised-microsoft-key-enables-authentication-of-countless-micr<br>https://msrc.microsoft.com/blog/2023/09/results-of-major-technical-investigations-for-storm-0558-key-acquisition/ |
| misp-microsoft-activity-group | Antique Typhoon | canonical-name | 高 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
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
| マイクロソフト、2023年のExchange攻撃でハッカーがMSAキーを盗んだ方法が未だに不明 | cyber-espionage | 不明 | 不明 | 2024-04-05 | target--activity-rule--country--6604ad21c713b8dfd8c7 |  |  | victim--activity-rule--ee35971399080a75f6a1 | 米国国土安全保障省のCSRBがマイクロソフトの対応を批判 ハッカーはエンジニアのラップトップからAzure署名キーを盗んだと考えられる 攻撃は中国のサイバー諜報活動グループ「Storm-0558」によるもの マイクロソフトは署名キーの盗難方法について確たる証拠がないと述べている ハッカーはこの侵害で、22組織から500以上の個人のメールアカウントを侵害した | 中 | `source--daily-bbafe9c31bcf2d45a64d` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 米国 | 活動「マイクロソフト、2023年のExchange攻撃でハッカーがMSAキーを盗んだ方法が未だに不明」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-bbafe9c31bcf2d45a64d` |

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: マイクロソフト、2023年のExchange攻撃でハッカーがMSAキーを盗んだ方法が未だに不明 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--6604ad21c713b8dfd8c7 |  |  | メール／メールアカウント, クラウド／SaaS | espionage: 米国国土安全保障省のCSRBがマイクロソフトの対応を批判 ハッカーはエンジニアのラップトップからAzure署名キーを盗んだと考えられる 攻撃は中国のサイバー諜報活動グループ「Storm-0558」によるもの マイクロソフトは署名キーの盗難方法について確たる証拠がないと述べている ハッカーはこの侵害で、22組織から500以上の個人のメールアカウントを侵害した | 不明 | 不明 | 2024-04-05 | 中 | `source--daily-bbafe9c31bcf2d45a64d` |

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 14件（`artifacts.csv`）

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
| source--daily-bbafe9c31bcf2d45a64d | マイクロソフト、2023年のExchange攻撃でハッカーがMSAキーを盗んだ方法が未だに不明 | bleepingcomputer.com | 2024-04-05 | https://www.bleepingcomputer.com/news/security/microsoft-still-unsure-how-hackers-stole-msa-key-in-2023-exchange-attack/ | osint-report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--storm-0558--146cd0ffcb195800 | Qianxin 2023 APT Report |  | 2023 | summary/2024/Qianxin 2023 APT Report.pdf | report | TLP:CLEAR | 中 |
| source--storm-0558--1dcaa721c6ba7e0f | MDDR FINAL 2023 1004 |  | 2023-10-04 | summary/2023/MDDR_FINAL_2023_1004.pdf | report | TLP:CLEAR | 中 |
| source--storm-0558--455c4b3eba82e2a6 | 2024 security report |  | 2024 | summary/2024/2024-security-report.pdf | report | TLP:CLEAR | 中 |
| source--storm-0558--4b91e3e949473ddc | storm 0558 |  | 不明 | actor_profile/evidence/storm-0558.csv | structured-data | TLP:CLEAR | 中 |
| source--storm-0558--5a3ba709f2e81aae | Booz Allen Hamilton |  | 不明 | AISecurity/2026/Booz Allen Hamilton.pdf | report | TLP:CLEAR | 中 |
| source--storm-0558--99d2d3d63f4589d7 | 2024 dbir data breach investigations report |  | 2024 | summary/2024/2024-dbir-data-breach-investigations-report.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
