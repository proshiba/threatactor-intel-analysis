# UAC-0125 脅威アクタープロファイル

- プロファイルID: `actor--uac-0125`
- 状態: draft
- 更新日時: 2026-07-29T23:12:01Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

UAC-0125の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UAC-0125**
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
| etda-threat-group-cards | Sandworm Team, Iron Viking, Voodoo Bear | canonical-name | 高 | Russia | https://blog.trendmicro.com/trendlabs-security-intelligence/timeline-of-sandworm-attacks/<br>https://www.crowdstrike.com/blog/meet-crowdstrikes-adversary-of-the-month-for-january-voodoo-bear/<br>https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/ |
| cert-ua-uac-index | UAC-0125 | canonical-name | 高 |  | https://cert.gov.ua/article/6281701 |
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
| countries | アゼルバイジャン | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてアゼルバイジャンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | アフガニスタン | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてアフガニスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | アルゼンチン | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてアルゼンチンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | アンゴラ | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてアンゴラが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イスラエル | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてイスラエルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イタリア | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてイタリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イラン | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてイランが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | インド | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてインドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ウクライナ | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてウクライナが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ウズベキスタン | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてウズベキスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | エジプト | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてエジプトが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オマーン | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてオマーンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オランダ | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてオランダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オーストラリア | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてオーストラリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オーストリア | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてオーストリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | カザフスタン | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてカザフスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | カナダ | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてカナダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | カンボジア | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてカンボジアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ガーナ | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてガーナが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | キルギス | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてキルギスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | コロンビア | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてコロンビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | シリア | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてシリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ジョージア | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてジョージアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | スウェーデン | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてスウェーデンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | スペイン | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてスペインが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | セルビア | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてセルビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | タイ | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてタイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | チェコ | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてチェコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | デンマーク | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてデンマークが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | トルコ | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてトルコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ドイツ | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてドイツが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ナイジェリア | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてナイジェリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ノルウェー | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてノルウェーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ハンガリー | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてハンガリーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | パキスタン | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてパキスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | パラグアイ | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてパラグアイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フランス | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてフランスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ブルガリア | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてブルガリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベトナム | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてベトナムが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベラルーシ | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてベラルーシが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベルギー | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてベルギーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ペルー | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてペルーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ポルトガル | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてポルトガルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ポーランド | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてポーランドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ミャンマー | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてミャンマーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | モルドバ | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてモルドバが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ラトビア | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてラトビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | リトアニア | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてリトアニアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ルクセンブルク | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてルクセンブルクが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ルーマニア | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてルーマニアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ロシア | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国としてロシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 中国 | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国として中国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国として米国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 英国 | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 韓国 | 構造化OSINTの被害国フィールドでUAC-0125の標的・被害国として韓国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | アフリカ | アンゴラ、エジプト、ガーナ、ナイジェリアで確認された標的・被害事例をアフリカとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | コーカサス | アゼルバイジャン、ジョージアで確認された標的・被害事例をコーカサスとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 中南米 | アルゼンチン、コロンビア、パラグアイ、ペルーで確認された標的・被害事例を中南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 中央アジア | ウズベキスタン、カザフスタン、キルギスで確認された標的・被害事例を中央アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 中東 | イスラエル、イラン、オマーン、シリア、トルコで確認された標的・被害事例を中東として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 北米 | カナダ、米国で確認された標的・被害事例を北米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 南アジア | アフガニスタン、インド、パキスタンで確認された標的・被害事例を南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 南欧 | イタリア、スペイン、セルビア、ポルトガルで確認された標的・被害事例を南欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 南米 | アルゼンチン、コロンビア、パラグアイ、ペルーで確認された標的・被害事例を南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東アジア | 中国、韓国で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東南アジア | カンボジア、タイ、ベトナム、ミャンマーで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東欧 | ウクライナ、チェコ、ハンガリー、ブルガリア、ベラルーシ、ポーランド、モルドバ、ルーマニア、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | イタリア、ウクライナ、オランダ、オーストリア、スウェーデン、スペイン、セルビア、チェコ、デンマーク、トルコ、ドイツ、ノルウェー、ハンガリー、フランス、ブルガリア、ベラルーシ、ベルギー、ポルトガル、ポーランド、モルドバ、ラトビア、リトアニア、ルクセンブルク、ルーマニア、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |

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
| source--uac-0125--c2f63851776c77a6 | uac 0125 |  | 不明 | actor_profile/evidence/uac-0125.csv | structured-data | TLP:CLEAR | 中 |
| source--uac-0125--008b3383c3195ac4 | Russian Cyber Operations Attack Automation, Espionage Against Defense Sector and New Tactics |  | 不明 | International Strategic/Russia/Russian Cyber Operations Attack Automation, Espionage Against Defense Sector and New Tactics.pdf | report | TLP:CLEAR | 中 |
| source--osint-cert-ua-uac-index | CERT-UA UAC Article Index | CERT-UA | 不明 | actor_profile/reference/osint/cert-ua-uac-index.json | government-cert-article-index | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
