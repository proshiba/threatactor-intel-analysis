# Famous Chollima 脅威アクタープロファイル

- プロファイルID: `actor--famous-chollima`
- 状態: draft
- 更新日時: 2026-09-21T13:20:00Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

FAMOUS CHOLLIMAはCrowdStrikeが追跡するDPRK-nexus Actor。AI等を用いた偽装身元でリモートIT職へ潜入し、北朝鮮政権へ収益を送る活動を主に追跡する。

## アクター名とAlias

- 正規名: **Famous Chollima**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

Aliasなし

## 帰属

CrowdStrike consistently describes FAMOUS CHOLLIMA as a DPRK-nexus adversary; its IT-worker revenue generation supports the North Korean regime.

- 国: North Korea
- スポンサー種別: state
- 確度: 高
- 証拠: `source--crowdstrike-famous-chollima-2026`, `source--crowdstrike-famous-chollima-2025`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| financial-gain | CrowdStrike states that FAMOUS CHOLLIMA's IT-worker infiltration is primarily financially motivated and generates revenue for the North Korean regime. | 高 | `source--crowdstrike-famous-chollima-2026` | Actor-specific vendor reporting. |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| DPRK IT Worker Schemes | related-to | FAMOUS CHOLLIMA is a named CrowdStrike adversary operating within the broader DPRK remote IT-worker revenue-generation ecosystem represented by the repository's scheme profile. | 高 | `source--crowdstrike-famous-chollima-2026`, `source--doj-dprk-it-worker-schemes-2025` |
| Contagious Interview | overlaps-with | CrowdStrike tracking and community identifiers overlap with activity commonly described as Contagious Interview, but the two repository entities are not modeled as exact aliases. | 中 | `source--crowdstrike-famous-chollima-2025` |

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

- 判定: `matched`
- 調査日時: 2026-09-21T02:39:13Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | WageMole | canonical-name | 高 | KP | https://unit42.paloaltonetworks.com/two-campaigns-by-north-korea-bad-actors-target-job-hunters/<br>https://unit42.paloaltonetworks.com/fake-north-korean-it-worker-activity-cluster/<br>https://www.trendmicro.com/en_us/research/25/d/russian-infrastructure-north-korean-cybercrime.html |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | Famous Chollima | canonical-name | 高 | KP |  |

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

CrowdStrikeは2024〜2026年にかけてFAMOUS CHOLLIMAのIT-worker/insider型活動の拡大を継続報告している。

## ターゲット

ターゲット情報なし

選定ロジック: Only source-explicit actor-specific targeting is structured. 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

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
| FAMOUS CHOLLIMA is a distinct vendor-named DPRK-nexus adversary and should not be used as an exact alias for the broad DPRK IT Worker Schemes ecosystem. | 高 | `source--crowdstrike-famous-chollima-2026`, `source--crowdstrike-famous-chollima-2025` | Entity-scope correction. |

### 情報ギャップ

- Public vendor cluster boundaries between FAMOUS CHOLLIMA and Contagious Interview remain overlapping.

### 不確実性

- Government reporting describes the wider DPRK IT-worker scheme without necessarily using CrowdStrike's FAMOUS CHOLLIMA label.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--crowdstrike-famous-chollima-2026 | CrowdStrike 2026 Technology Threat Landscape Report | CrowdStrike | 2026-06-09 | https://www.crowdstrike.com/en-us/blog/crowdstrike-2026-technology-threat-landscape-report/ | vendor-threat-research | TLP:CLEAR | 高 |
| source--crowdstrike-famous-chollima-2025 | CrowdStrike 2025 Threat Hunting Report | CrowdStrike | 2025-08-04 | https://www.crowdstrike.com/en-us/blog/crowdstrike-2025-threat-hunting-report-ai-weapon-target/ | vendor-threat-research | TLP:CLEAR | 高 |
| source--doj-dprk-it-worker-schemes-2025 | Justice Department Announces Coordinated, Nationwide Actions to Combat North Korean Remote IT Workers' Illicit Revenue Generation Schemes | U.S. Department of Justice | 2025-06-30 | https://www.justice.gov/opa/pr/justice-department-announces-coordinated-nationwide-actions-combat-north-korean-remote | government-law-enforcement | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

DPRK IT Worker Schemesは上位ecosystemとして別profileで保持。Contagious Interviewとはoverlap関係として扱いexact aliasにはしない。
