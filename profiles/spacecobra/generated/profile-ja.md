# SpaceCobra 脅威アクタープロファイル

- プロファイルID: `actor--spacecobra`
- 状態: draft
- 更新日時: 2026-09-21T13:20:00Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

SpaceCobraはESETがGravityRAT運用主体を追跡するために用いるActor名。GravityRAT自体はMITRE ATT&CK S0237のMalwareとして分離する。

## アクター名とAlias

- 正規名: **SpaceCobra**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

Aliasなし

## 帰属

ESET states that the real identity of the actor behind GravityRAT remains unknown; earlier reporting speculated about a Pakistan-based group, but this profile does not elevate that lead into structured attribution.

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: `source--eset-spacecobra-gravityrat-2023`

## モチベーション

未評価

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

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--gravityrat | GravityRAT | MITRE ATT&CK models GravityRAT as Software S0237. ESET attributes GravityRAT campaigns using BingeChat and Chatico to SpaceCobra. | 不明 | 不明 | 高 | `source--mitre-gravityrat-s0237`, `source--eset-spacecobra-gravityrat-2023` |

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

ESETは2023年、BingeChatおよびChaticoを用いるGravityRATキャンペーンをSpaceCobraへ帰属した。

## ターゲット

ターゲット情報なし

選定ロジック: Only source-explicit targeting should be structured. 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| SpaceCobra is the appropriate actor tracking entity for the ESET-attributed GravityRAT campaigns; GravityRAT itself is malware. | 高 | `source--eset-spacecobra-gravityrat-2023`, `source--mitre-gravityrat-s0237` | Entity-boundary correction. |

### 情報ギャップ

- The real-world identity and organizational affiliation behind SpaceCobra remain unknown.

### 不確実性

- Vendor tracking scope may not cover every historical GravityRAT deployment.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--eset-spacecobra-gravityrat-2023 | Android GravityRAT goes after WhatsApp backups | ESET | 2023-06-15 | https://www.welivesecurity.com/2023/06/15/android-gravityrat-goes-after-whatsapp-backups/ | vendor-threat-research | TLP:CLEAR | 高 |
| source--mitre-gravityrat-s0237 | GravityRAT, Software S0237 | MITRE ATT&CK | 不明 | https://attack.mitre.org/software/S0237/ | structured-knowledge-base | TLP:CLEAR | 高 |

## 自由記述

実体組織は不明。Pakistan関連の過去推測を構造化帰属へ昇格しない。
