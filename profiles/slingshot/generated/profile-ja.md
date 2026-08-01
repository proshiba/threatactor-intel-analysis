# Slingshot 脅威アクタープロファイル

- プロファイルID: `actor--slingshot`
- 状態: draft
- 更新日時: 2026-07-29T23:13:55Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Slingshotの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Slingshot**
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
| Capability | Slingshot, Cahnadr, GollumApp, SsCB, ffproxy, NeedleWatch, Sfc2, Minisling, Spork downloader |
| Infrastructure |  |
| Victim | Kenya, Yemen, Libya, Afghanistan, Iraq, Tanzania, Jordan, Mauritius, Somalia, Democratic Republic of the Congo, Turkey, Sudan and United Arab Emirates |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Slingshot | canonical-name | 高 |  | https://securelist.com/apt-slingshot/84312/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Slingshot&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Slingshot | canonical-name | 高 |  | https://securelist.com/apt-slingshot/84312/ |
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
| malware--slingshot | Slingshot | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--cahnadr | Cahnadr | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--gollumapp | GollumApp | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--sscb | SsCB | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--ffproxy | ffproxy | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--needlewatch | NeedleWatch | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--sfc2 | Sfc2 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--minisling | Minisling | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--spork-downloader | Spork downloader | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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
| Mikrotik Router Compromise | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| Mikrotik Router Compromise | Slingshot | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |

Mikrotik Router Compromise

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アフガニスタン | Targeting text mentions afghanistan. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | アラブ首長国連邦 | Targeting text mentions united arab emirates. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | イエメン | レビュー済みアクターマッピングの標的欄に記録されたイエメンを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | イラク | Targeting text mentions iraq. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | ケニア | レビュー済みアクターマッピングの標的欄に記録されたケニアを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | スーダン | レビュー済みアクターマッピングの標的欄に記録されたスーダンを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | ソマリア | レビュー済みアクターマッピングの標的欄に記録されたソマリアを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | タンザニア | レビュー済みアクターマッピングの標的欄に記録されたタンザニアを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | トルコ | Targeting text mentions turkey. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | モーリシャス | レビュー済みアクターマッピングの標的欄に記録されたモーリシャスを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | ヨルダン | Targeting text mentions jordan. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | リビア | レビュー済みアクターマッピングの標的欄に記録されたリビアを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| regions | アフリカ | ケニア、スーダン、ソマリア、タンザニア、モーリシャス、リビアで確認された標的・被害事例をアフリカとして集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| regions | 中東 | アラブ首長国連邦、イエメン、イラク、トルコ、ヨルダンで確認された標的・被害事例を中東として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |

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
- 非IOC artifact観測: 21件（`artifacts.csv`）

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
| source--slingshot--04039e8eb829e124 | slingshot |  | 不明 | actor_profile/evidence/slingshot.csv | structured-data | TLP:CLEAR | 中 |
| source--slingshot--9c90b3c12412a875 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--slingshot--7b76e8dbe54ae4be | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--slingshot--e01ce75f17c59dfe | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--slingshot--b6b7af38cbb7d998 | ESET Threat Report Q22020 |  | 不明 | summary/2020/ESET_Threat_Report_Q22020.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
