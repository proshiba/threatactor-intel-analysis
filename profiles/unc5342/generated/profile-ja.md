# UNC5342 脅威アクタープロファイル

- プロファイルID: `actor--unc5342`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

UNC5342の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC5342**
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
| misp-threat-actor | UNC5342 | canonical-name | 高 | KP | https://cloud.google.com/blog/topics/threat-intelligence/dprk-adopts-etherhiding |
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
| 北朝鮮ハッカー、偽の仮想通貨企業と偽就職面接でマルウェアを拡散 | malware-campaign | 不明 | 不明 | 2025-04-26 |  |  | ttp--activity-rule--212f3a2857a12748d2a8 | victim--activity-rule--a44df31e8e4b5309dfc1 | 北朝鮮支援のグループが偽の仮想通貨企業を設立し、就職面接を装いマルウェアを拡散。 BlockNovas、Angeloper、SoftGlideの3社を使い、BeaverTailなど複数マルウェアを配布。 マルウェアはシステム情報収集やリバースシェル作成、ブラウザデータ窃取が可能。 ロシアのIPレンジを使い活動を匿名化し、米FBIはBlockNovasドメインを押収。 活動の背後にはAIツールを利用した偽プロファイル作成も含まれる。 | 中 | `source--daily-cf8c33fcf3e4b3907567` |
| 北朝鮮ハッカーが「EtherHiding」でブロックチェーン上にマルウェアを隠蔽 | malware-campaign | 不明 | 不明 | 2025-10-17 | target--activity-rule--sector--63c9fa67327d005b07b7 |  |  | victim--activity-rule--50584425405683df183b | Google TIGはDPRKのUNC5342が2025年2月からEtherHidingを採用し、スマートコントラクトで悪性ペイロードを配布と報告。 偽の採用面接で開発者にコード実行を促し、技術課題に見せかけてJavaScriptダウンローダを走らせる手口が用いられる。 スマートコントラクトにはJADESNOWを格納し、EthereumやBNB上からInvisibleFerretの第3段階を取得してメモリで実行。 読み取り専用コールで履歴が残りにくく、契約は4か月で20回超更新・平均$1.37の低コストで構成変更が容易と分析。 窃取機能はブラウザ保存のパスワード/クレカ/暗号資産ウォレットを狙う。管理者にダウンロード制限や厳格なブラウザ制御を推奨。 | 中 | `source--daily-658542b50150556febcb` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| 北朝鮮ハッカー、偽の仮想通貨企業と偽就職面接でマルウェアを拡散 | UNC5342 | 情報なし | T1082 System Information Discovery | 情報なし | 情報なし | 被害事例: 北朝鮮ハッカー、偽の仮想通貨企業と偽就職面接でマルウェアを拡散 | 中 |
| 北朝鮮ハッカーが「EtherHiding」でブロックチェーン上にマルウェアを隠蔽 | UNC5342 | 情報なし | 情報なし | 情報なし | 暗号資産・Web3 | 被害事例: 北朝鮮ハッカーが「EtherHiding」でブロックチェーン上にマルウェアを隠蔽 | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | 暗号資産・Web3 | 活動「北朝鮮ハッカーが「EtherHiding」でブロックチェーン上にマルウェアを隠蔽」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-658542b50150556febcb` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 北朝鮮ハッカーが「EtherHiding」でブロックチェーン上にマルウェアを隠蔽 | 非公開 | anonymous | unknown | reported | target--activity-rule--sector--63c9fa67327d005b07b7 |  |  |  | financial-loss: 窃取機能はブラウザ保存のパスワード/クレカ/暗号資産ウォレットを狙う。 | 不明 | 不明 | 2025-10-17 | 中 | `source--daily-658542b50150556febcb` |
| 被害事例: 北朝鮮ハッカー、偽の仮想通貨企業と偽就職面接でマルウェアを拡散 | 非公開 | aggregate | multiple-organizations | reported |  |  | ttp--activity-rule--212f3a2857a12748d2a8 |  | data-theft: マルウェアはシステム情報収集やリバースシェル作成、ブラウザデータ窃取が可能。<br>espionage: マルウェアはシステム情報収集やリバースシェル作成、ブラウザデータ窃取が可能。 | 不明 | 不明 | 2025-04-26 | 中 | `source--daily-cf8c33fcf3e4b3907567` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Discovery | T1082 | System Information Discovery | マルウェアはシステム情報収集やリバースシェル作成、ブラウザデータ窃取が可能。 |  | activity--daily-67541f516bef5213759f | 不明 | 不明 | 中 | `source--daily-cf8c33fcf3e4b3907567` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 7件（`artifacts.csv`）

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
| source--daily-658542b50150556febcb | 北朝鮮ハッカーが「EtherHiding」でブロックチェーン上にマルウェアを隠蔽 | bleepingcomputer.com | 2025-10-17 | https://www.bleepingcomputer.com/news/security/north-korean-hackers-use-etherhiding-to-hide-malware-on-the-blockchain/ | osint-report | TLP:CLEAR | 中 |
| source--daily-cf8c33fcf3e4b3907567 | 北朝鮮ハッカー、偽の仮想通貨企業と偽就職面接でマルウェアを拡散 | thehackernews.com | 2025-04-26 | https://thehackernews.com/2025/04/north-korean-hackers-spread-malware-via.html | osint-report | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unc5342--0cb1ed52898214d0 | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | International Strategic/Korea/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--unc5342--6b4b85e4f862ca27 | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--unc5342--9aa2898da735df6f | unc5342 |  | 不明 | actor_profile/evidence/unc5342.csv | structured-data | TLP:CLEAR | 中 |
| source--unc5342--f8089569ef10b4c8 | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | CyberMerceNary/ITWorker/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
