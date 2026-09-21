# UNC3569 脅威アクタープロファイル

- プロファイルID: `actor--unc3569`
- 状態: draft
- 更新日時: 2026-09-21T13:20:00Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

UNC3569の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC3569**
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
| misp-threat-actor | UNC3569 | canonical-name | 高 | CN | https://cloud.google.com/blog/topics/threat-intelligence/ivanti-post-exploitation-lateral-movement |
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
| malware--daily-92623c41cfe9d6459335 | GRAYRABBIT | UNC3569との直接的な利用関係が一次資料レビューで確認されたマルウェア。 | 不明 | 不明 | 中 | `source--daily-a44134da0f07029e3862` |

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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ハッカー、Tencentアプリの脆弱性を悪用しGrayRabbitマルウェアを展開 | cyber-espionage | 不明 | 不明 | 2026-09-14 |  | malware--daily-92623c41cfe9d6459335 |  |  | 中国系サイバー諜報グループUNC3569が、TencentのWindows向けSogou Input Methodの重大なRCE脆弱性CVE-2026-51990を実際の攻撃で悪用している。 攻撃はsgbiz: URIの引数検証不備、WebViewの任意URL読み込み、古くサンドボックス化されていないChromiumという3つの弱点を連鎖させる。 被害者が細工されたリンクをクリックするとSogouの正規プロセスが攻撃者管理ページを読み込み、古いChromiumの既知脆弱性を悪用してコード実行に至る。 攻撃成功後はGrayRabbitバックドアが導入され、プロセス実行、リバースシェル、ファイル送受信、端末情報収集、メモリ内プラグイン実行などが可能になる。 Tencentは2026年4月21日公開のSogou Input Method 16.3.0.3498で修正したが、内蔵ブラウザ自体は依然古く、サンドボックスなしで動作すると警告されている。 | 中 | `source--daily-a44134da0f07029e3862` |
| 中国関与ハッカー、2023年からJavaScript C2「PeckBirdy」を使用 | infrastructure-operation | 不明 | 不明 | 2026-01-28 | target--activity-rule--sector--210dddb39397dbe50e91, target--targeting-audit--country--39881b6f27f0986ea931, target--targeting-audit--region--af8e0b8ea3f352b88f87 | malware--daily-92623c41cfe9d6459335 | ttp--activity-rule--d23ef70e9a6b6307bc52 | victim--activity-rule--b58e62cfdbc20134f3f1 | Trend Microは、中国関与APTがJScript製C2「PeckBirdy」を2023年から運用し、中国系ギャンブル業界やアジアの政府・企業を標的と指摘。 PeckBirdyはブラウザやMSHTA/WScript/Classic ASP/Node/.NETで動作し、LOLBinsを活用、既定はWebSocketでC2通信しAdobe FlashやCometも併用。 SHADOW-VOID-044は偽Chrome更新ページで感染させ、Cookie窃取やCVE-2020-16040悪用、Electron経由のバックドアやTCPリバースシェル等を展開。 SHADOW-EARTH-045は政府サイトにPeckBirdyリンクを注入し資格情報収集を狙い、MSHTAでの横展開も確認（フィリピンの教育機関も被害）。 インフラ解析でHOLODONUT/MKDOOR/NEXLOADやGRAYRABBIT等との関連、47[.]238[.]184[.]9がEarth Baxia/APT41に関連と示唆。 | 中 | `source--daily-c20a23c702af45ff32d4` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| ハッカー、Tencentアプリの脆弱性を悪用しGrayRabbitマルウェアを展開 | UNC3569 | GRAYRABBIT | 情報なし | 情報なし | 情報なし | 情報なし | 中 |
| 中国関与ハッカー、2023年からJavaScript C2「PeckBirdy」を使用 | UNC3569 | GRAYRABBIT | T1555.003 Credentials from Web Browsers | 情報なし | 政府・行政, フィリピン, アジア | 被害事例: 中国関与ハッカー、2023年からJavaScript C2「PeckBirdy」を使用 | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | フィリピン | 活動「中国関与ハッカー、2023年からJavaScript C2「PeckBirdy」を使用」の記述で標的・被害国として明示されている。 | 不明 | 不明 | 中 | `source--daily-c20a23c702af45ff32d4` |
| regions | アジア | 活動「中国関与ハッカー、2023年からJavaScript C2「PeckBirdy」を使用」の記述で標的地域としてアジアが明示されている。 | 不明 | 不明 | 中 | `source--daily-c20a23c702af45ff32d4` |
| sectors | 政府・行政 | 活動「中国関与ハッカー、2023年からJavaScript C2「PeckBirdy」を使用」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-c20a23c702af45ff32d4` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 中国関与ハッカー、2023年からJavaScript C2「PeckBirdy」を使用 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--210dddb39397dbe50e91 | malware--daily-92623c41cfe9d6459335 | ttp--activity-rule--d23ef70e9a6b6307bc52 |  | credential-theft: SHADOW-VOID-044は偽Chrome更新ページで感染させ、Cookie窃取やCVE-2020-16040悪用、Electron経由のバックドアやTCPリバースシェル等を展開。<br>espionage: SHADOW-EARTH-045は政府サイトにPeckBirdyリンクを注入し資格情報収集を狙い、MSHTAでの横展開も確認（フィリピンの教育機関も被害）。 | 不明 | 不明 | 2026-01-28 | 中 | `source--daily-c20a23c702af45ff32d4` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1555.003 | Credentials from Web Browsers | SHADOW-VOID-044は偽Chrome更新ページで感染させ、Cookie窃取やCVE-2020-16040悪用、Electron経由のバックドアやTCPリバースシェル等を展開。 |  | activity--daily-48716db321e86ff0f407 | 不明 | 不明 | 中 | `source--daily-c20a23c702af45ff32d4` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 1件（`artifacts.csv`）

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
| source--daily-a44134da0f07029e3862 | ハッカー、Tencentアプリの脆弱性を悪用しGrayRabbitマルウェアを展開 | gendigital.com | 2026-09-14 | https://www.gendigital.com/blog/insights/research/one-click-backdoor-sogou | osint-report | TLP:CLEAR | 中 |
| source--daily-c20a23c702af45ff32d4 | 中国関与ハッカー、2023年からJavaScript C2「PeckBirdy」を使用 | thehackernews.com | 2026-01-28 | https://thehackernews.com/2026/01/china-linked-hackers-have-used.html | osint-report | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unc3569--295e739f4cdcf299 | Bridewell 2026 Cyber Threat Intelligence Report |  | 2026 | summary/2026/Bridewell 2026 Cyber Threat Intelligence Report.pdf | report | TLP:CLEAR | 中 |
| source--unc3569--b980f226588807bc | unc3569 |  | 不明 | actor_profile/evidence/unc3569.csv | structured-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
