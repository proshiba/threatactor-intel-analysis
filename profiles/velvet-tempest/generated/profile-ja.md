# Velvet Tempest 脅威アクタープロファイル

- プロファイルID: `actor--velvet-tempest`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Velvet Tempestの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Velvet Tempest**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| DEV-0504 | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |

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
| microsoft-threat-actor-mapping | Velvet Tempest | canonical-name | 高 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Velvet Tempest | canonical-name | 高 |  | https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/<br>http://www.microsoft.com/security/blog/2022/06/13/the-many-lives-of-blackcat-ransomware/ |
| misp-microsoft-activity-group | Velvet Tempest | canonical-name | 高 |  | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
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
| ClickFixとCastleRAT攻撃に結び付くTermiteランサムウェア侵害 | ransomware-extortion | 不明 | 不明 | 2026-03-09 |  |  | ttp--activity-rule--0340cc3b09f76a67a2b9, ttp--activity-rule--2d1cff90d507f785194b, ttp--activity-rule--7663020e8831577e6f57, ttp--activity-rule--ab1701024d8b466b0fa0 | victim--activity-rule--10854ac29d4fa44cfdf0 | MalBeaconは、Velvet TempestがClickFixと正規のWindowsユーティリティを使い、DonutLoaderとCastleRATを展開する一連の侵害活動を観測した。 観測は2026年2月3日から16日にかけて、米国の非営利組織を模した3,000超の端末と2,500超の利用者を持つ観測環境で12日間実施された。 初期侵入は悪性広告から誘導されるClickFixとCAPTCHAの組み合わせで、難読化コマンドをWindowsの「ファイル名を指定して実行」に貼り付けさせる手口だった。 侵入後はActive Directory偵察、ホスト探索、環境把握、Chrome保存認証情報の窃取、PowerShellやcsc.exeによる追加ペイロード取得とPython永続化が確認された。 最終的にDonutLoaderとCastleRATが展開されたが、今回MalBeaconが観測した侵害ではTermiteランサムウェア本体が実行された形跡はなかった。 | 中 | `source--daily-ebcbecadd73228eda327` |



## ターゲット

ターゲット情報なし

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: ClickFixとCastleRAT攻撃に結び付くTermiteランサムウェア侵害 | 非公開 | aggregate | multiple-organizations | reported |  |  | ttp--activity-rule--0340cc3b09f76a67a2b9, ttp--activity-rule--2d1cff90d507f785194b, ttp--activity-rule--7663020e8831577e6f57, ttp--activity-rule--ab1701024d8b466b0fa0 | エンドポイント | credential-theft: 侵入後はActive Directory偵察、ホスト探索、環境把握、Chrome保存認証情報の窃取、PowerShellやcsc.exeによる追加ペイロード取得とPython永続化が確認された。<br>encryption: ClickFixとCastleRAT攻撃に結び付くTermiteランサムウェア侵害 | 不明 | 不明 | 2026-03-09 | 中 | `source--daily-ebcbecadd73228eda327` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1555.003 | Credentials from Web Browsers | 侵入後はActive Directory偵察、ホスト探索、環境把握、Chrome保存認証情報の窃取、PowerShellやcsc.exeによる追加ペイロード取得とPython永続化が確認された。 |  | activity--daily-29144f6bc264652b3e32 | 不明 | 不明 | 中 | `source--daily-ebcbecadd73228eda327` |
| Execution | T1204.004 | Malicious Copy and Paste | ClickFixとCastleRAT攻撃に結び付くTermiteランサムウェア侵害 |  | activity--daily-29144f6bc264652b3e32 | 不明 | 不明 | 中 | `source--daily-ebcbecadd73228eda327` |
| Stealth | T1027 | Obfuscated Files or Information | 初期侵入は悪性広告から誘導されるClickFixとCAPTCHAの組み合わせで、難読化コマンドをWindowsの「ファイル名を指定して実行」に貼り付けさせる手口だった。 |  | activity--daily-29144f6bc264652b3e32 | 不明 | 不明 | 中 | `source--daily-ebcbecadd73228eda327` |
| Command And Control | T1105 | Ingress Tool Transfer | 侵入後はActive Directory偵察、ホスト探索、環境把握、Chrome保存認証情報の窃取、PowerShellやcsc.exeによる追加ペイロード取得とPython永続化が確認された。 |  | activity--daily-29144f6bc264652b3e32 | 不明 | 不明 | 中 | `source--daily-ebcbecadd73228eda327` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 4件（`artifacts.csv`）

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
| source--daily-ebcbecadd73228eda327 | ClickFixとCastleRAT攻撃に結び付くTermiteランサムウェア侵害 | bleepingcomputer.com | 2026-03-09 | https://www.bleepingcomputer.com/news/security/termite-ransomware-breaches-linked-to-clickfix-castlerat-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--velvet-tempest--2e7a5b64f876a17e | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--velvet-tempest--31feb678dc5d0564 | 2022cyberComprehensiveSituationObservationManual |  | 2022 | summary/2023/2022cyberComprehensiveSituationObservationManual.pdf | report | TLP:CLEAR | 中 |
| source--velvet-tempest--cd5814175ad93cad | velvet tempest |  | 不明 | actor_profile/evidence/velvet-tempest.csv | structured-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
