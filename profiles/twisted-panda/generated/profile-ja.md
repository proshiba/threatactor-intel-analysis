# Twisted Panda 脅威アクタープロファイル

- プロファイルID: `actor--twisted-panda`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Twisted Pandaの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Twisted Panda**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Stone Panda, Mustang Panda | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 75; mapping requires review. |

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
| Capability |  |
| Infrastructure |  |
| Victim |  |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Twisted Panda | canonical-name | 高 | China | https://research.checkpoint.com/2022/twisted-panda-chinese-apt-espionage-operation-against-russians-state-owned-defense-institutes/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Twisted+Panda&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | 一致なし |  |  |  |  |
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

活動履歴なし

### 活動別ダイヤモンドモデル

活動別ダイヤモンドモデルなし



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | ベラルーシ | 構造化OSINTの被害国フィールドでTwisted Pandaの標的・被害国としてベラルーシが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ロシア | 構造化OSINTの被害国フィールドでTwisted Pandaの標的・被害国としてロシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東欧 | ベラルーシ、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution, Persistence, Privilege Escalation | T1053 | Scheduled Task/Job | рации TOP Mitre Россия и СНГ Июнь 2021 • Hijack Execution Flow (T1574) • Ingress Tool Transfer (T1105) • File and Directory Discovery (T1083) • Scheduled Task (T1053) • System Information Discovery (T10 |  |  | 不明 | 不明 | 中 | `source--twisted-panda--b941810771b65047` |
| Discovery | T1082 | System Information Discovery | • Hijack Execution Flow (T1574) • Ingress Tool Transfer (T1105) • File and Directory Discovery (T1083) • Scheduled Task (T1053) • System Information Discovery (T1082) Исследователи раскрыли кампанию Twisted Panda, в ходе которой в течение нескольких месяцев использовались приманки, связанные с санкциями, для атак на российские оборонные институты, входящие в корпорацию «Ростех». Другая цель находится в Беларуси, и, веро- ятно |  |  | 不明 | 不明 | 中 | `source--twisted-panda--b941810771b65047` |
| Discovery | T1083 | File and Directory Discovery | d Panda Регион Начало операции TOP Mitre Россия и СНГ Июнь 2021 • Hijack Execution Flow (T1574) • Ingress Tool Transfer (T1105) • File and Directory Discovery (T1083) • Scheduled Task (T1053) • System Information Discovery (T10 |  |  | 不明 | 不明 | 中 | `source--twisted-panda--b941810771b65047` |
| Command And Control | T1105 | Ingress Tool Transfer | й атаки через платформу Windows. Twisted Panda Регион Начало операции TOP Mitre Россия и СНГ Июнь 2021 • Hijack Execution Flow (T1574) • Ingress Tool Transfer (T1105) • File and Directory Discovery (T1083) • Scheduled Task (T1053) • System Information Discovery (T10 |  |  | 不明 | 不明 | 中 | `source--twisted-panda--b941810771b65047` |
| Execution, Stealth | T1574 | Hijack Execution Flow | и эксперты не обнаружили ни одной атаки через платформу Windows. Twisted Panda Регион Начало операции TOP Mitre Россия и СНГ Июнь 2021 • Hijack Execution Flow (T1574) • Ingress Tool Transfer (T1105) • File and Directory Discovery (T1083) • Scheduled Task (T1053) • System Information Discovery (T10 |  |  | 不明 | 不明 | 中 | `source--twisted-panda--b941810771b65047` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 5件（`artifacts.csv`）

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
| source--twisted-panda--b941810771b65047 | twisted panda |  | 不明 | actor_profile/evidence/twisted-panda.csv | structured-data | TLP:CLEAR | 中 |
| source--twisted-panda--384b1d4daf53c4f3 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
