# Carberp 脅威アクタープロファイル

- プロファイルID: `actor--carberb`
- 状態: draft
- 更新日時: 2026-09-23T12:16:55Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

Carberpの標準化プロファイル。Group-IBのactor-specific調査に基づき、金融目的の犯罪グループとして整理する。

## アクター名とAlias

- 正規名: **Carberp**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Carberb | legacy-corpus | exact | 低 | `source--actor-census-curation-carberp` | Legacy repository spelling retained as an exact lookup variant of the reviewed canonical name Carberp; confidence remains low because the misspelling is corpus-local. |

## 帰属

Group-IB identifies Carberp as a criminal hacking group focused on financial theft; no state sponsorship is asserted.

- 国: 不明
- スポンサー種別: criminal
- 確度: 高
- 証拠: `source--group-ib-carberp-gang`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| financial-gain | Group-IB lists the group's motivation as Financial and documents theft from banking customers. | 高 | `source--group-ib-carberp-gang` | Actor-specific investigation. |

## 他アクターとの関係

確認された関係なし

## 関連する企業・個人

関連エンティティなし

### エンティティ関係

確認された関係なし

### 法的措置

確認された法的措置なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability |  |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `no-match`
- 調査日時: 2026-09-21T02:39:13Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | 一致なし |  |  |  |  |
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

## C2・マルウェア ハンティング・ピボット

構造化されたハンティング・ピボットなし

### 観測根拠

観測記録なし

### ハントクエリ

クエリなし

### 継続利用チェック

実行済みの受動検索・継続利用チェックなし

`active_status` は明示的なテレメトリまたはスキャン根拠がない限り `unknown` です。出典公開日は観測時刻に転用していません。

## 攻撃活動の履歴

活動履歴なし

### 活動別ダイヤモンドモデル

活動別ダイヤモンドモデルなし

Group-IBは2010〜2012年のCarberp gangの活動と、法執行機関による構成員の摘発を記録している。

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| regions | 全世界 | Group-IB lists the geography of Carberp attacks as Worldwide. | 不明 | 不明 | 高 | `source--group-ib-carberp-gang` |
| sectors | 金融 | Group-IB lists the financial sector and banks as Carberp targets. | 不明 | 不明 | 高 | `source--group-ib-carberp-gang` |

選定ロジック: Actor-specific Group-IB investigation only; geography is not reused as sponsorship evidence. 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 2件
- IOC観測: 4件
- 複数攻撃で観測: 0件
- 要レビュー候補: 2件
- 非IOC artifact観測: 2件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| Carberp is a financially motivated criminal hacking group; the legacy 'Carberb' spelling and Russia/state/espionage classification are not used as canonical attribution. | 高 | `source--group-ib-carberp-gang` | Group-IB actor-specific investigation. |

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--carberb--5501c7dbfeb0afae | carberb |  | 不明 | actor_profile/evidence/carberb.csv | structured-data | TLP:CLEAR | 中 |
| source--group-ib-carberp-gang | Carberp gang knocked down | Group-IB | 不明 | https://www.group-ib.com/top-investigations/carberp-gang/ | actor-specific-investigation | TLP:CLEAR | 高 |
| source--actor-census-curation-carberp | Analyst-reviewed Carberp identity curation | threatactor-intel-analysis maintainers | 不明 | actor_profile/actor-census-curation.json | analyst-curation | TLP:CLEAR | 高 |

## 自由記述

Carberp groupとCarberp malwareを同一entityとして扱わない。Carberbは旧コーパス表記としてのみ保持する。
