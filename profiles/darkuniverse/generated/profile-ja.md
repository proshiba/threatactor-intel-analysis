# DarkUniverse 脅威アクタープロファイル

- プロファイルID: `actor--darkuniverse`
- 状態: draft
- 更新日時: 2026-07-29T23:13:54Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

DarkUniverseの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **DarkUniverse**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

Aliasなし

## 帰属

The repository mapping workbook places this actor in the China worksheet.

- 国: China
- スポンサー種別: state
- 確度: 中
- 証拠: `source--actor-mapping-workbook`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | State-sponsored intelligence collection or strategic operations. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability | ItaDuke |
| Infrastructure |  |
| Victim | Tibet and Uyghur activists, Syria, Iran, Afghanistan, Tanzania, Ethiopia, Sudan, Russia, Belarus and the United Arab Emirates |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | DarkUniverse | canonical-name | 高 |  | https://securelist.com/darkuniverse-the-mysterious-apt-framework-27/94897/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=DarkUniverse&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | ItaDuke | canonical-name | 高 |  | https://securelist.com/darkuniverse-the-mysterious-apt-framework-27/94897/<br>https://www.fireeye.com/blog/threat-research/2013/02/the-number-of-the-beast.html<br>https://securelist.com/new-uyghur-and-tibetan-themed-attacks-using-pdf-exploits/35465 |
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

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--itaduke | ItaDuke | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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

活動履歴なし

### 活動別ダイヤモンドモデル

活動別ダイヤモンドモデルなし



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アフガニスタン | Targeting text mentions afghanistan. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | アラブ首長国連邦 | Targeting text mentions united arab emirates. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | イラン | Targeting text mentions iran. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | エチオピア | レビュー済みアクターマッピングの標的欄に記録されたエチオピアを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | シリア | Targeting text mentions syria. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | スーダン | レビュー済みアクターマッピングの標的欄に記録されたスーダンを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | タンザニア | レビュー済みアクターマッピングの標的欄に記録されたタンザニアを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | ベラルーシ | Targeting text mentions belarus. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | ロシア | Targeting text mentions russia. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| regions | アフリカ | エチオピア、スーダン、タンザニアで確認された標的・被害事例をアフリカとして集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| regions | チベット | レビュー済みアクターマッピングの標的欄に記録されたチベットを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| regions | 中東 | アラブ首長国連邦、イラン、シリアで確認された標的・被害事例を中東として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| regions | 東欧 | ベラルーシ、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| sectors | Nonprofit and Civil Society | Targeting text indicates the Nonprofit and Civil Society sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

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
| source--darkuniverse--128b402f1401f5fe | darkuniverse |  | 不明 | actor_profile/evidence/darkuniverse.csv | structured-data | TLP:CLEAR | 中 |
| source--darkuniverse--6a7bbf196c53f2d7 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
