# UNC2428 脅威アクタープロファイル

- プロファイルID: `actor--unc2428`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

UNC2428の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC2428**
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
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Pink Sandstorm | canonical-name | 高 | IR | https://www.oodaloop.com/archive/2024/01/02/critical-infrastructure-remains-the-brass-ring-for-cyber-attackers-in-2024/<br>https://unit42.paloaltonetworks.com/agonizing-serpens-targets-israeli-tech-higher-ed-sectors/<br>https://socprime.com/blog/agonizing-serpens-attack-detection-iran-backed-hackers-target-israeli-tech-firms-and-educational-institutions/ |
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
| イラン関連ハッカー、偽の求人キャンペーンを通じてイスラエルを標的にMURKYTOURマルウェアを展開 | infrastructure-operation | 不明 | 不明 | 2025-04-24 |  |  |  | victim--activity-rule--c2a1236c011a447d08fe | イラン関連の脅威グループUNC2428が、イスラエルの防衛企業ラファエルを装った偽の求人キャンペーンを実施。 応募者は「RafaelConnect.exe」というツールをダウンロードさせられ、個人情報や履歴書を入力するよう誘導された。 このツールはLONEFLEETインストーラーであり、LEAFPILEランチャーを介してMURKYTOURバックドアを密かに展開。 MURKYTOURは持続的なアクセスを提供し、被害者のマシンを完全に制御可能にする。 このキャンペーンは、イスラエル国家サイバー総局が「Black Shadow」として追跡している活動と重複している。 | 中 | `source--daily-7839c220d8ee6cec8013` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | イスラエル | 活動「イラン関連ハッカー、偽の求人キャンペーンを通じてイスラエルを標的にMURKYTOURマルウェアを展開」の記述で標的・被害国として明示されている。 | 不明 | 不明 | 中 | `source--daily-7839c220d8ee6cec8013` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: イラン関連ハッカー、偽の求人キャンペーンを通じてイスラエルを標的にMURKYTOURマルウェアを展開 | 非公開 | aggregate | multiple-organizations | reported |  |  |  |  | privacy: 応募者は「RafaelConnect.exe」というツールをダウンロードさせられ、個人情報や履歴書を入力するよう誘導された。 | 不明 | 不明 | 2025-04-24 | 中 | `source--daily-7839c220d8ee6cec8013` |

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 3件（`artifacts.csv`）

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
| source--daily-7839c220d8ee6cec8013 | イラン関連ハッカー、偽の求人キャンペーンを通じてイスラエルを標的にMURKYTOURマルウェアを展開 | thehackernews.com | 2025-04-24 | https://thehackernews.com/2025/04/iran-linked-hackers-target-israel-with.html | osint-report | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unc2428--71ce3caf1231d036 | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--unc2428--feccdfdcf533cbe7 | unc2428 |  | 不明 | actor_profile/evidence/unc2428.csv | structured-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
