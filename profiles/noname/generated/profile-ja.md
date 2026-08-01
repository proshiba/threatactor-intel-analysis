# NoName 脅威アクタープロファイル

- プロファイルID: `actor--noname`
- 状態: draft
- 更新日時: 2026-07-29T23:12:00Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

NoNameの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **NoName**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

Aliasなし

## 帰属

The repository mapping workbook places this actor in the North Korea worksheet.

- 国: North Korea
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
| Capability | malware with name "mySingleMessenger.exe" |
| Infrastructure |  |
| Victim |  |
| Socio-political | North Korea |

## OSINTクロスチェック

- 判定: `no-match`
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
| malware--malware-with-name-mysinglemessenger-exe | malware with name "mySingleMessenger.exe" | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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
| NoNameランサムウェアグループ、最近の攻撃でRansomHubマルウェアを展開 | ransomware-extortion | 不明 | 不明 | 2024-09-11 |  |  | ttp--activity-rule--45325343e04a1a174aa3 | victim--activity-rule--edf680b19e3e31961ae3 | NoName(cosmicbeetle)ランサムウェアグループがRansomHubマルウェアを使用した攻撃を実行。 NoNameは、ScRansomなどの独自ランサムウェアを使用していたが、最近の攻撃でRansomHubを利用したことが観測された。ただし、ScRansomもまだ活発に開発中である。 このグループは、脆弱性攻撃やブルートフォース攻撃で初期アクセスを取得。主に中小企業をターゲットにしている。 最新の攻撃ではEDR（Endpoint Detection and Response）ソフトウェアを無効化する技術も使用。 グループはRansomHubのアフィリエイトとして活動している可能性がある。 | 高 | `source--daily-f4f1d6491185f16c56e8` |
| スイス政府はITサプライヤーへのランサムウェア攻撃がデータに影響を及ぼした可能性があると発表。 攻撃はPlayランサムウェアギャングにより行われ、機密データが盗まれたと主張。 スイス政府は、漏洩したデータが連邦行政のものである可能性が高いと述べている。 さらに、スイス政府のウェブサイトとオンラインサービスがDDoS攻撃 | ransomware-extortion | 不明 | 不明 | 2023-06-13 | target--activity-rule--country--72caf60a2fbce4a1be7a |  |  | victim--activity-rule--8e2b381dfb5516bf0def | スイス政府はITサプライヤーへのランサムウェア攻撃がデータに影響を及ぼした可能性があると発表。 攻撃はPlayランサムウェアギャングにより行われ、機密データが盗まれたと主張。 スイス政府は、漏洩したデータが連邦行政のものである可能性が高いと述べている。 さらに、スイス政府のウェブサイトとオンラインサービスがDDoS攻撃を受けていると警告。 攻撃はNoNameというプロロシアのハクティビストグループによるもの。 | 中 | `source--daily-1ac461ba97988d7cde92` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| NoNameランサムウェアグループ、最近の攻撃でRansomHubマルウェアを展開 | NoName | 情報なし | T1110 Brute Force | 情報なし | 情報なし | 被害事例: NoNameランサムウェアグループ、最近の攻撃でRansomHubマルウェアを展開 | 高 |
| スイス政府はITサプライヤーへのランサムウェア攻撃がデータに影響を及ぼした可能性があると発表。 攻撃はPlayランサムウェアギャングにより行われ、機密データが盗まれたと主張。 スイス政府は、漏洩したデータが連邦行政のものである可能性が高いと述べている。 さらに、スイス政府のウェブサイトとオンラインサービスがDDoS攻撃 | NoName | 情報なし | 情報なし | 情報なし | ロシア | スイス政府はITサプライヤーへ | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | スイス | 活動「スイス政府はITサプライヤーへのランサムウェア攻撃がデータに影響を及ぼした可能性があると発表。 攻撃はPlayランサムウェアギャングにより行われ、機密データが盗まれたと主張。 スイス政府は、漏洩したデータが連邦行政のものである可能性が高いと述べている。 さらに、スイス政府のウェブサイトとオンラインサービスがDDoS攻撃」の記述で標的・被害国として明示されている。 | 不明 | 不明 | 中 | `source--daily-1ac461ba97988d7cde92` |
| countries | ロシア | 活動「スイス政府はITサプライヤーへのランサムウェア攻撃がデータに影響を及ぼした可能性があると発表。 攻撃はPlayランサムウェアギャングにより行われ、機密データが盗まれたと主張。 スイス政府は、漏洩したデータが連邦行政のものである可能性が高いと述べている。 さらに、スイス政府のウェブサイトとオンラインサービスがDDoS攻撃」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-1ac461ba97988d7cde92` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: スイス政府はITサプライヤーへのランサムウェア攻撃がデータに影響を及ぼした可能性があると発表。 攻撃はPlayランサムウェアギャングにより行われ、機密データが盗まれたと主張。 スイス政府は、漏洩したデータが連邦行政のものである可能性が高いと述べている。 さらに、スイス政府のウェブサイトとオンラインサービスがDDoS攻撃 | スイス政府はITサプライヤーへ | named | organization | reported | target--activity-rule--country--72caf60a2fbce4a1be7a |  |  |  | encryption: スイス政府はITサプライヤーへのランサムウェア攻撃がデータに影響を及ぼした可能性があると発表。 | 不明 | 不明 | 2023-06-13 | 中 | `source--daily-1ac461ba97988d7cde92` |
| 被害事例: NoNameランサムウェアグループ、最近の攻撃でRansomHubマルウェアを展開 | 非公開 | aggregate | multiple-organizations | reported |  |  | ttp--activity-rule--45325343e04a1a174aa3 | エンドポイント | encryption: NoNameランサムウェアグループ、最近の攻撃でRansomHubマルウェアを展開 | 不明 | 不明 | 2024-09-11 | 高 | `source--daily-f4f1d6491185f16c56e8` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1110 | Brute Force | このグループは、脆弱性攻撃やブルートフォース攻撃で初期アクセスを取得。 |  | activity--daily-1f8fe6a2645a9e1b6a0e | 不明 | 不明 | 中 | `source--daily-f4f1d6491185f16c56e8` |

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
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
| source--daily-1ac461ba97988d7cde92 | スイス政府はITサプライヤーへのランサムウェア攻撃がデータに影響を及ぼした可能性があると発表。 攻撃はPlayランサムウェアギャングにより行われ、機密データが盗まれたと主張。 スイス政府は、漏洩したデータが連邦行政のものである可能性が高いと述べている。 さらに、スイス政府のウェブサイトとオンラインサービスがDDoS攻撃 | bleepingcomputer.com | 2023-06-13 | https://www.bleepingcomputer.com/news/security/swiss-government-warns-of-ongoing-ddos-attacks-data-leak/ | osint-report | TLP:CLEAR | 中 |
| source--daily-f4f1d6491185f16c56e8 | NoNameランサムウェアグループ、最近の攻撃でRansomHubマルウェアを展開 | bleepingcomputer.com | 2024-09-11 | https://www.bleepingcomputer.com/news/security/noname-ransomware-gang-deploying-ransomhub-malware-in-recent-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--noname--0530cdc6b1a27089 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--noname--84a159674aeaf9b5 | eset threat report h22024 |  | 不明 | summary/2024/eset-threat-report-h22024.pdf | report | TLP:CLEAR | 中 |
| source--noname--dc8dc6b79013e2f1 | noname |  | 不明 | actor_profile/evidence/noname.csv | structured-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
