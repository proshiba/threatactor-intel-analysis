# UAC-0099 脅威アクタープロファイル

- プロファイルID: `actor--uac-0099`
- 状態: draft
- 更新日時: 2026-09-03T13:41:51Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

UAC-0099の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UAC-0099**
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
| cert-ua-uac-index | UAC-0099 | canonical-name | 高 |  | https://cert.gov.ua/article/6318634<br>https://cert.gov.ua/article/6281681<br>https://cert.gov.ua/article/4818341 |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | UAC-0099 | canonical-name | 高 |  | https://cert.gov.ua/article/4818341<br>https://www.deepinstinct.com/blog/threat-actor-uac-0099-continues-to-target-ukraine |
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
| malware--daily-0067ca7bc8c9a3dd3e9d | BURNYBEAR | UAC-0099との直接的な利用関係が一次資料レビューで確認されたマルウェア。 | 不明 | 不明 | 中 | `source--daily-b6ba84745cdc81a329c5` |
| malware--daily-75ab18d562d78bfce191 | LUNCHPOKE | UAC-0099との直接的な利用関係が一次資料レビューで確認されたマルウェア。 | 不明 | 不明 | 中 | `source--daily-b6ba84745cdc81a329c5` |
| malware--daily-8759c33e657f191deae0 | MATCHBOIL.V2 | UAC-0099との直接的な利用関係が一次資料レビューで確認されたマルウェア。 | 不明 | 不明 | 中 | `source--daily-b6ba84745cdc81a329c5` |

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
| ロシア系UAC-0099、マルウェアに「核兵器」プロンプトを埋め込みAI解析を妨害 | disruptive-activity | 2026-07 | 2026-07 | 2026-09-02 | target--activity-rule--country--36f1b9323d5faab92f39, target--activity-rule--sector--b8d6639a1884e2bacaa4, target--activity-rule--sector--dfc80b76cad93a318adc, target--activity-rule--sector--fb803c0a91ed53ea76f9 |  |  | victim--activity-rule--3a6def6b1e7230e2c121 | ESETは、ロシア系脅威アクターUAC-0099が、AI支援型マルウェア解析を妨害する新手法「GuardBreaker」をウクライナの標的に使用したと報告した。 攻撃では悪性VBSスクリプトのコメント欄に核兵器製造を求める安全上問題のある文章を埋め込み、LLMの安全機構を作動させ解析拒否へ誘導する。 GuardBreakerを含むVBSは、UAC-0099専用のC#ローダー「MATCHBOIL」をダウンロード・導入し、追加ペイロードを配布する目的で使用される。 UAC-0099は過去に交通・エネルギー分野を標的としており、2026年7月には偽Notepad++プラグインを用いて新型MATCHBOILを展開していた。 同様のLLM向け敵対的プロンプトはMini Shai-Huludなどでも確認されており、AIを最初の解析器として無防備に使うワークフローの弱点が示されている。 | 高 | `source--daily-d7f23202e68f653b1ad9` |
| ハッカーがNotepad++プラグインを悪用し、密かにマルウェアをインストール | malware-campaign | 不明 | 不明 | 2026-07-24 | target--activity-rule--country--36f1b9323d5faab92f39 | malware--daily-0067ca7bc8c9a3dd3e9d, malware--daily-75ab18d562d78bfce191, malware--daily-8759c33e657f191deae0 | ttp--activity-rule--26fad87edd30aab65d0c, ttp--activity-rule--8235faa69f53cdff20b8 | victim--activity-rule--32a83d51aade8f9e290c | ウクライナのCERT-UAは、正規のNotepad++と悪性プラグイン「LunchPoke」を含むアーカイブを配布し、永続性を確保する攻撃を確認した。 UAC-0099はPDFを装うVBSスクリプトからEvernote.zipを取得させ、Notepad++の通常のプラグイン読込機能で悪性NppExport.dllを実行する。 LunchPokeはスケジュールタスクを作成し、BurnyBearとMatchBoil V2ローダーを展開して、追加プログラムの取得と実行を可能にする。 BurnyBearは起動に失敗した場合、ホストのRAMとCPUを枯渇させる攻撃を行う代替機能も備えている。 本攻撃はNotepad++のサプライチェーン侵害ではなく、正規アプリケーションと悪性ファイルを一緒に配布して信頼を悪用する手法である。 | 中 | `source--daily-b6ba84745cdc81a329c5` |
| Sandwormハッカーがデータワイパーでウクライナの穀物セクターを妨害 | disruptive-activity | 2025-06 | 2025-09 | 2025-11-07 | target--activity-rule--country--36f1b9323d5faab92f39, target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--598ee8d6d22873efc495, target--activity-rule--sector--e7608f51421ca8b1e297 |  | ttp--activity-rule--5178b790ed1002745052, ttp--activity-rule--ac677bbe93733e1f8ef3 | victim--activity-rule--f9da9dc6b868f567f3c8 | ロシア支援のSandworm（APT44）が教育・政府・物流・穀物輸出などを狙い、複数のデータワイパーを投入したとESETが報告。 攻撃は2025年6月と9月に確認され、ファイルやパーティション等を破壊して復旧困難な混乱を引き起こす破壊活動が目的。 穀物輸出は同国の主要収入源であり、標的化はウクライナの戦時経済を弱体化させる狙いと分析されている。 4月には大学でZeroLotやStingも使用。Stingは「goulash」にちなんだ名前のスケジュールタスク経由で実行、初期侵入はUAC-0099が関与。 防御策としてオフラインバックアップ、強力なEDR/侵入防止、ソフト更新の徹底が有効とされる。 | 中 | `source--daily-acae91555bc1bc0a4220` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| ロシア系UAC-0099、マルウェアに「核兵器」プロンプトを埋め込みAI解析を妨害 | UAC-0099 | 情報なし | 情報なし | 情報なし | ウクライナ, 運輸・航空・海運, 製造・産業, エネルギー | 被害事例: ロシア系UAC-0099、マルウェアに「核兵器」プロンプトを埋め込みAI解析を妨害 | 高 |
| ハッカーがNotepad++プラグインを悪用し、密かにマルウェアをインストール | UAC-0099 | BURNYBEAR, LUNCHPOKE, MATCHBOIL.V2 | T1036 Masquerading, T1053.005 Scheduled Task | 情報なし | ウクライナ | 被害事例: ハッカーがNotepad++プラグインを悪用し、密かにマルウェアをインストール | 中 |
| Sandwormハッカーがデータワイパーでウクライナの穀物セクターを妨害 | UAC-0099 | 情報なし | T1485 Data Destruction, T1053.005 Scheduled Task | 情報なし | ウクライナ, 政府・行政, 農業・食品, 教育・研究 | 被害事例: Sandwormハッカーがデータワイパーでウクライナの穀物セクターを妨害 | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | ウクライナ | 活動「ロシア系UAC-0099、マルウェアに「核兵器」プロンプトを埋め込みAI解析を妨害」の記述で標的として明示された国・地域。 | 2025-06 | 2026-07 | 中 | `source--daily-acae91555bc1bc0a4220`, `source--daily-b6ba84745cdc81a329c5`, `source--daily-d7f23202e68f653b1ad9` |
| sectors | 政府・行政 | 活動「Sandwormハッカーがデータワイパーでウクライナの穀物セクターを妨害」の記述で標的として明示された産業。 | 2025-06 | 2025-09 | 中 | `source--daily-acae91555bc1bc0a4220` |
| sectors | 農業・食品 | 活動「Sandwormハッカーがデータワイパーでウクライナの穀物セクターを妨害」の記述で標的として明示された産業。 | 2025-06 | 2025-09 | 中 | `source--daily-acae91555bc1bc0a4220` |
| sectors | 運輸・航空・海運 | 活動「ロシア系UAC-0099、マルウェアに「核兵器」プロンプトを埋め込みAI解析を妨害」の記述で標的として明示された産業。 | 2026-07 | 2026-07 | 中 | `source--daily-d7f23202e68f653b1ad9` |
| sectors | 製造・産業 | 活動「ロシア系UAC-0099、マルウェアに「核兵器」プロンプトを埋め込みAI解析を妨害」の記述で標的として明示された産業。 | 2026-07 | 2026-07 | 中 | `source--daily-d7f23202e68f653b1ad9` |
| sectors | 教育・研究 | 活動「Sandwormハッカーがデータワイパーでウクライナの穀物セクターを妨害」の記述で標的として明示された産業。 | 2025-06 | 2025-09 | 中 | `source--daily-acae91555bc1bc0a4220` |
| sectors | エネルギー | 活動「ロシア系UAC-0099、マルウェアに「核兵器」プロンプトを埋め込みAI解析を妨害」の記述で標的として明示された産業。 | 2026-07 | 2026-07 | 中 | `source--daily-d7f23202e68f653b1ad9` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: ハッカーがNotepad++プラグインを悪用し、密かにマルウェアをインストール | 非公開 | anonymous | unknown | reported | target--activity-rule--country--36f1b9323d5faab92f39 | malware--daily-0067ca7bc8c9a3dd3e9d, malware--daily-75ab18d562d78bfce191, malware--daily-8759c33e657f191deae0 | ttp--activity-rule--26fad87edd30aab65d0c, ttp--activity-rule--8235faa69f53cdff20b8 |  |  | 不明 | 不明 | 2026-07-24 | 中 | `source--daily-b6ba84745cdc81a329c5` |
| 被害事例: ロシア系UAC-0099、マルウェアに「核兵器」プロンプトを埋め込みAI解析を妨害 | 非公開 | anonymous | unknown | reported | target--activity-rule--country--36f1b9323d5faab92f39, target--activity-rule--sector--b8d6639a1884e2bacaa4, target--activity-rule--sector--dfc80b76cad93a318adc, target--activity-rule--sector--fb803c0a91ed53ea76f9 |  |  |  |  | 2026-07 | 2026-07 | 2026-09-02 | 高 | `source--daily-d7f23202e68f653b1ad9` |
| 被害事例: Sandwormハッカーがデータワイパーでウクライナの穀物セクターを妨害 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--36f1b9323d5faab92f39, target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--598ee8d6d22873efc495, target--activity-rule--sector--e7608f51421ca8b1e297 |  | ttp--activity-rule--5178b790ed1002745052, ttp--activity-rule--ac677bbe93733e1f8ef3 |  | destruction: Sandwormハッカーがデータワイパーでウクライナの穀物セクターを妨害<br>disruption: 防御策としてオフラインバックアップ、強力なEDR/侵入防止、ソフト更新の徹底が有効とされる。 | 2025-06 | 2025-09 | 2025-11-07 | 中 | `source--daily-acae91555bc1bc0a4220` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1036 | Masquerading | UAC-0099はPDFを装うVBSスクリプトからEvernote.zipを取得させ、Notepad++の通常のプラグイン読込機能で悪性NppExport.dllを実行する。 |  | activity--daily-72da5dad97e2e21f550f | 不明 | 不明 | 中 | `source--daily-b6ba84745cdc81a329c5` |
| Impact | T1485 | Data Destruction | Sandwormハッカーがデータワイパーでウクライナの穀物セクターを妨害 |  | activity--daily-e526344e9500f358b6b5 | 2025-06 | 2025-09 | 中 | `source--daily-acae91555bc1bc0a4220` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | LunchPokeはスケジュールタスクを作成し、BurnyBearとMatchBoil V2ローダーを展開して、追加プログラムの取得と実行を可能にする。 | malware--daily-0067ca7bc8c9a3dd3e9d, malware--daily-75ab18d562d78bfce191 | activity--daily-72da5dad97e2e21f550f | 不明 | 不明 | 中 | `source--daily-b6ba84745cdc81a329c5` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | Stingは「goulash」にちなんだ名前のスケジュールタスク経由で実行、初期侵入はUAC-0099が関与。 |  | activity--daily-e526344e9500f358b6b5 | 2025-06 | 2025-09 | 中 | `source--daily-acae91555bc1bc0a4220` |

## IOC／artifact概要

- IOC値: 51件
- IOC観測: 51件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 10件（`artifacts.csv`）

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
| source--daily-acae91555bc1bc0a4220 | Sandwormハッカーがデータワイパーでウクライナの穀物セクターを妨害 | bleepingcomputer.com | 2025-11-07 | https://www.bleepingcomputer.com/news/security/sandworm-hackers-use-data-wipers-to-disrupt-ukraines-grain-sector/ | osint-report | TLP:CLEAR | 中 |
| source--daily-b6ba84745cdc81a329c5 | ハッカーがNotepad++プラグインを悪用し、密かにマルウェアをインストール | cert.gov.ua | 2026-07-24 | https://cert.gov.ua/article/6318634 | osint-report | TLP:CLEAR | 中 |
| source--daily-d7f23202e68f653b1ad9 | ロシア系UAC-0099、マルウェアに「核兵器」プロンプトを埋め込みAI解析を妨害 | x.com | 2026-09-02 | https://x.com/ESETresearch/status/2092885120562741652 | osint-report | TLP:CLEAR | 中 |
| source--osint-cert-ua-uac-index | CERT-UA UAC Article Index | CERT-UA | 不明 | actor_profile/reference/osint/cert-ua-uac-index.json | government-cert-article-index | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--uac-0099--196d7c629d73d165 | RussianCyber |  | 不明 | summary/2024/RussianCyber.pdf | report | TLP:CLEAR | 中 |
| source--uac-0099--1bbf512130c53602 | Russian Cyber Operations Attack Automation, Espionage Against Defense Sector and New Tactics |  | 不明 | International Strategic/Russia/Russian Cyber Operations Attack Automation, Espionage Against Defense Sector and New Tactics.pdf | report | TLP:CLEAR | 中 |
| source--uac-0099--c98bdf401e349de9 | apt44 unearthing sandworm |  | 不明 | Sandworm/apt44-unearthing-sandworm.pdf | report | TLP:CLEAR | 中 |
| source--uac-0099--d1390da5cc0a8ca5 | uac 0099 |  | 不明 | actor_profile/evidence/uac-0099.csv | structured-data | TLP:CLEAR | 中 |
| source--uac-0099--da9ce7085469e683 | 2025 Global APT Threat Research Report |  | 2025 | summary/2026/2025 Global APT Threat Research Report.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
