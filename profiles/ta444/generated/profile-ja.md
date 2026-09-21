# TA444 脅威アクタープロファイル

- プロファイルID: `actor--ta444`
- 状態: draft
- 更新日時: 2026-09-21T08:15:06Z
- 構造バージョン: 1.3.0

## エグゼクティブサマリー

TA444の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **TA444**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| BlueNoroff | Huntress / Proofpoint | overlapping | 高 | `source--huntress-bluenoroff-macos-2025`, `source--proofpoint-ta444-2023` | Huntress uses these names interchangeably for the June 2025 intrusion, while Proofpoint states that APT38 heavily overlaps TA444. The alias is therefore scoped as overlapping across vendor taxonomies, not globally exact. |
| CageyChameleon | Huntress / Proofpoint | overlapping | 高 | `source--huntress-bluenoroff-macos-2025`, `source--proofpoint-ta444-2023` | Huntress uses these names interchangeably for the June 2025 intrusion, while Proofpoint states that APT38 heavily overlaps TA444. The alias is therefore scoped as overlapping across vendor taxonomies, not globally exact. |
| COPERNICIUM | Huntress / Proofpoint | overlapping | 高 | `source--huntress-bluenoroff-macos-2025`, `source--proofpoint-ta444-2023` | Huntress uses these names interchangeably for the June 2025 intrusion, while Proofpoint states that APT38 heavily overlaps TA444. The alias is therefore scoped as overlapping across vendor taxonomies, not globally exact. |
| Sapphire Sleet | Huntress / Proofpoint | overlapping | 高 | `source--huntress-bluenoroff-macos-2025`, `source--proofpoint-ta444-2023` | Huntress uses these names interchangeably for the June 2025 intrusion, while Proofpoint states that APT38 heavily overlaps TA444. The alias is therefore scoped as overlapping across vendor taxonomies, not globally exact. |
| STARDUST CHOLLIMA | Huntress / Proofpoint | overlapping | 高 | `source--huntress-bluenoroff-macos-2025`, `source--proofpoint-ta444-2023` | Huntress uses these names interchangeably for the June 2025 intrusion, while Proofpoint states that APT38 heavily overlaps TA444. The alias is therefore scoped as overlapping across vendor taxonomies, not globally exact. |

## 帰属

未評価

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: なし

## モチベーション

未評価

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| APT38 | overlaps-with | Proofpoint tracks TA444 as a distinct cluster and states that APT38 heavily overlaps with it; Huntress also uses TA444/BlueNoroff naming for the June 2025 intrusion. | 高 | `source--proofpoint-ta444-2023`, `source--huntress-bluenoroff-macos-2025` |

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
| etda-threat-group-cards | Bluenoroff, APT 38, Stardust Chollima | canonical-name | 高 | North Korea | https://threatpost.com/lazarus-apt-spinoff-linked-to-banking-hacks/124746/<br>https://www.microsoft.com/en-us/security/blog/2024/11/22/microsoft-shares-latest-intelligence-on-north-korean-and-chinese-threat-actors-at-cyberwarcon/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Subgroup%3A+Bluenoroff%2C+APT+38%2C+Stardust+Chollima&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | TA444 | canonical-name | 高 | KP | https://www.proofpoint.com/us/blog/threat-insight/ta444-apt-startup-aimed-at-your-funds<br>https://cyberscoop.com/north-korean-cryptocurrency-hackers-education-government/<br>https://www.darkreading.com/remote-workforce/north-korea-apt-swindled-1b-crypto-investors-2022 |
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
| malware--cryptobot-ta444 | CryptoBot | Go infostealer focused on cryptocurrency wallet and browser-extension data. | 2025-06-11 | 2025-06-11 | 高 | `source--huntress-bluenoroff-macos-2025` |
| malware--injectwithdyld | InjectWithDyld | C++ loader that decrypts and injects additional payloads. | 2025-06-11 | 2025-06-11 | 高 | `source--huntress-bluenoroff-macos-2025` |
| malware--netchk | NetChk | Recovered malicious component that continuously generated random numbers. | 2025-06-11 | 2025-06-11 | 高 | `source--huntress-bluenoroff-macos-2025` |
| malware--ta444-nim-implant | Nim Implant | Injected implant with asynchronous command-execution capability. | 2025-06-11 | 2025-06-11 | 高 | `source--huntress-bluenoroff-macos-2025` |
| malware--root-troy-v4 | Root Troy V4 | Go backdoor used to download and execute additional implants. | 2025-06-11 | 2025-06-11 | 高 | `source--huntress-bluenoroff-macos-2025` |
| malware--telegram-2 | Telegram 2 | Nim persistence implant that starts the primary backdoor. | 2025-06-11 | 2025-06-11 | 高 | `source--huntress-bluenoroff-macos-2025` |
| malware--xscreen | XScreen | Objective-C keylogger with clipboard and screen-capture capability. | 2025-06-11 | 2025-06-11 | 高 | `source--huntress-bluenoroff-macos-2025` |

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
| TA444／BlueNoroff、ディープフェイクZoom会議からWeb3組織のmacOSを侵害 | malware-campaign | 2025-06-11 | 2025-06-11 | 2025-06-19 | target--activity-rule--sector--63c9fa67327d005b07b7 | malware--cryptobot-ta444, malware--injectwithdyld, malware--netchk, malware--root-troy-v4, malware--ta444-nim-implant, malware--telegram-2, malware--xscreen | ttp--activity-rule--e0bddf476245d6242ee7 | victim--activity-rule--9eadafe82d0168882b86 | 2025年6月11日、TA444／BlueNoroffは暗号資産財団の従業員を幹部らのディープフェイクを使った偽Zoom会議へ誘導し、偽拡張機能のAppleScriptを実行させた。Huntressは侵害端末から、永続化を担うTelegram 2、バックドアRoot Troy V4、ローダーInjectWithDyld、Nim Implant、キーロガー兼画面・クリップボード収集機XScreen、暗号資産情報窃取型CryptoBot、NetChkを回収した。Huntressはこの侵入をTA444にhigh confidenceで帰属した。 | 高 | `source--daily-a449b8d5424ffffad583`, `source--huntress-bluenoroff-macos-2025` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| TA444／BlueNoroff、ディープフェイクZoom会議からWeb3組織のmacOSを侵害 | TA444 | CryptoBot, InjectWithDyld, NetChk, Root Troy V4, Nim Implant, Telegram 2, XScreen | T1056.001 Keylogging | 情報なし | 暗号資産・Web3 | 被害事例: TA444／BlueNoroff、ディープフェイクZoom会議からWeb3組織のmacOSを侵害 | 高 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | 暗号資産・Web3 | 活動「TA444／BlueNoroff、ディープフェイクZoom会議からWeb3組織のmacOSを侵害」の記述で標的として明示された産業。 | 2025-06-11 | 2025-06-11 | 中 | `source--daily-a449b8d5424ffffad583`, `source--huntress-bluenoroff-macos-2025` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: TA444／BlueNoroff、ディープフェイクZoom会議からWeb3組織のmacOSを侵害 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--63c9fa67327d005b07b7 | malware--cryptobot-ta444, malware--injectwithdyld, malware--netchk, malware--root-troy-v4, malware--ta444-nim-implant, malware--telegram-2, malware--xscreen | ttp--activity-rule--e0bddf476245d6242ee7 | エンドポイント |  | 2025-06-11 | 2025-06-11 | 2025-06-19 | 高 | `source--daily-a449b8d5424ffffad583`, `source--huntress-bluenoroff-macos-2025` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Collection, Credential Access | T1056.001 | Keylogging | Huntressは侵害端末から、永続化を担うTelegram 2、バックドアRoot Troy V4、ローダーInjectWithDyld、Nim Implant、キーロガー兼画面・クリップボード収集機XScreen、暗号資産情報窃取型CryptoBot、NetChkを回収した。 | malware--cryptobot-ta444, malware--injectwithdyld, malware--netchk, malware--root-troy-v4, malware--ta444-nim-implant, malware--telegram-2, malware--xscreen | activity--daily-e034301964da7955795d | 2025-06-11 | 2025-06-11 | 中 | `source--daily-a449b8d5424ffffad583`, `source--huntress-bluenoroff-macos-2025` |

## IOC／artifact概要

- IOC値: 5件
- IOC観測: 5件
- 複数攻撃で観測: 0件
- 要レビュー候補: 5件
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
| source--daily-a449b8d5424ffffad583 | 北朝鮮ハッカー集団がZoom通話で重役をディープフェイクし、Macマルウェアを拡散 | bleepingcomputer.com | 2025-06-19 | https://www.bleepingcomputer.com/news/security/north-korean-hackers-deepfake-execs-in-zoom-call-to-spread-mac-malware/ | osint-report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--ta444--01f6dbb3cdcf5f99 | ta444 |  | 不明 | actor_profile/evidence/ta444.csv | structured-data | TLP:CLEAR | 中 |
| source--ta444--153a3a81efbff396 | Qianxin 2023 APT Report |  | 2023 | summary/2024/Qianxin 2023 APT Report.pdf | report | TLP:CLEAR | 中 |
| source--ta444--3626abb1436b84a4 | [Report] Bitsight State of the Underground 2026 |  | 2026 | summary/2026/[Report] Bitsight State of the Underground 2026.pdf | report | TLP:CLEAR | 中 |
| source--ta444--9d95eacf9707f985 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--ta444--b46c1dc9431c015c | North Korea’s Cyber Strategy |  | 不明 | International Strategic/Korea/North Korea’s Cyber Strategy.pdf | report | TLP:CLEAR | 中 |
| source--ta444--b4f4dd45ea4593ef | Global APT 2023 Mid Year Report QIANXIN |  | 2023 | summary/2023/Global APT 2023 Mid-Year Report-QIANXIN.pdf | report | TLP:CLEAR | 中 |
| source--huntress-bluenoroff-macos-2025 | Inside the BlueNoroff Web3 macOS Intrusion Analysis | Huntress | 2025-06-18 | https://www.huntress.com/blog/inside-bluenoroff-web3-intrusion-analysis | vendor-threat-research | TLP:CLEAR | 高 |
| source--proofpoint-ta444-2023 | TA444: The APT Startup Aimed at Acquisition (of Your Funds) | Proofpoint Threat Research | 2023-01-25 | https://www.proofpoint.com/uk/blog/threat-insight/ta444-apt-startup-aimed-at-your-funds | vendor-threat-research | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
