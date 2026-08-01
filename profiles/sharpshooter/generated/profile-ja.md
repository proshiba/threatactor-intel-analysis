# Sharpshooter 脅威アクタープロファイル

- プロファイルID: `actor--sharpshooter`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Sharpshooterの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Sharpshooter**
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

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Lazarus Group | overlaps-with | Though overlaps between this adversary and [Lazarus Group](https://attack.mitre.org/groups/G0032) have been noted, definitive links have not been established.(Citation: McAfee Sharpshooter December 2018) | 高 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | Operation [Sharpshooter](https://attack.mitre.org/groups/G0104) is the name of a cyber espionage campaign discovered in October 2018 targeting nuclear, defense, energy, and financial companies. Though overlaps between this adversary and [Lazarus Group](https://attack.mitre.org/groups/G0032) have been noted, definitive links have not been established.(Citation: McAfee Sharpshooter December 2018) |
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
| misp-threat-actor | 一致なし |  |  |  |  |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Sharpshooter - G0104 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0104<br>https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-sharpshooter.pdf |
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

活動履歴なし

### 活動別ダイヤモンドモデル

活動別ダイヤモンドモデルなし



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | 金融 | Operation [Sharpshooter](https://attack.mitre.org/groups/G0104) is the name of a cyber espionage campaign discovered in October 2018 targeting nuclear, defense, energy, and financial companies. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 防衛・軍事 | Operation [Sharpshooter](https://attack.mitre.org/groups/G0104) is the name of a cyber espionage campaign discovered in October 2018 targeting nuclear, defense, energy, and financial companies. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | エネルギー | Operation [Sharpshooter](https://attack.mitre.org/groups/G0104) is the name of a cyber espionage campaign discovered in October 2018 targeting nuclear, defense, energy, and financial companies. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
- 非IOC artifact観測: 11件（`artifacts.csv`）

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
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--sharpshooter--b33b001b4b956bdb | sharpshooter |  | 不明 | actor_profile/evidence/sharpshooter.csv | structured-data | TLP:CLEAR | 中 |
| source--sharpshooter--23040d732359e434 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--sharpshooter--77d5d7093cd526dd | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--sharpshooter--13597f827a5fc1ec | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--sharpshooter--cd9769cb3d0fc413 | Dream Job Campaign |  | 不明 | lazarus/Dream-Job-Campaign.pdf | report | TLP:CLEAR | 中 |
| source--sharpshooter--5d58d501065b63c1 | The Lazarus Constellation |  | 不明 | lazarus/The_Lazarus_Constellation.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
