# TA406 脅威アクタープロファイル

- プロファイルID: `actor--ta406`
- 状態: draft
- 更新日時: 2026-07-29T15:36:11Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

TA406の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **TA406**
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
| etda-threat-group-cards | Kimsuky, Velvet Chollima | canonical-name | 高 | North Korea | https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/<br>https://securityintelligence.com/media/recent-activity-from-itg16-a-north-korean-threat-group/<br>https://us-cert.cisa.gov/ncas/alerts/aa20-301a |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | TA406 | canonical-name | 高 | KP | https://www.proofpoint.com/us/blog/threat-insight/triple-threat-north-korea-aligned-ta406-scams-spies-and-steals<br>https://www.proofpoint.com/us/blog/threat-insight/ta406-pivots-front |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Kimsuky | part-of | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

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
| 北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化 | phishing-campaign | 不明 | 不明 | 2025-05-14 | target--activity-rule--country--36f1b9323d5faab92f39, target--activity-rule--country--72caf60a2fbce4a1be7a, target--activity-rule--country--f0d8df51439c4d0f3a05, target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--b94dc560a327b601965d, target--activity-rule--sector--e7608f51421ca8b1e297 |  | ttp--activity-rule--3b783b9995900a730cd6, ttp--activity-rule--a6b49b799bed2d732b35 | victim--activity-rule--42003486e06fe6355c62 | 北朝鮮支援のハッカーグループ「Konni（TA406）」が、ウクライナ政府機関を標的に情報収集活動を実施。 フィッシングメールでシンクタンクを装い、政治・軍事イベントに関するリンクを送信。 リンク先でパスワード付きRARファイルを配布し、PowerShellスクリプトで感染させる。 攻撃の目的は、北朝鮮軍のウクライナ派遣に伴うリスク評価とロシアからの追加要請の可能性を分析すること。 攻撃には、偽のMicrosoftセキュリティ警告を用いた認証情報の収集も含まれる。 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| Konniハッカー、AI生成マルウェアでブロックチェーン技術者を標的に | infrastructure-operation | 不明 | 不明 | 2026-01-26 | target--activity-rule--sector--63c9fa67327d005b07b7, target--activity-rule--sector--932f4928d5e1ec28e2df |  | ttp--activity-rule--3fad972c8e2a861c68a1 | victim--activity-rule--0327ca792873c263402d | 北朝鮮系Konni（Opal Sleet/TA406）がAI生成と見られるPowerShellマルウェアでブロックチェーン開発者・技術者を標的化。 Check Point分析では日本・豪州・インド由来の検体が確認され、APACを中心とする最近の活動とされる。 攻撃はDiscordホストのリンクからZIPを配布、PDFおとりと悪性LNKで開始しPowerShellローダでDOCXとCABを展開。 CABにはPSバックドア・2つのBAT・UAC回避用実行ファイルが含まれ、OneDrive偽装のタスクでXOR暗号化スクリプトを定期実行・痕跡削除。 バックドアは難読化されC2と定期通信、整然としたコメントやUUID記述からAI支援生成の痕跡が示唆されKonniに帰属。 | 中 | `source--daily-96093ec62047a80740ea` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | ウクライナ | 活動「北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| countries | ロシア | 活動「北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| countries | 北朝鮮 | 活動「北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| sectors | 政府・行政 | 活動「北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| sectors | 暗号資産・Web3 | 活動「Konniハッカー、AI生成マルウェアでブロックチェーン技術者を標的に」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-96093ec62047a80740ea` |
| sectors | IT・ソフトウェア | 活動「Konniハッカー、AI生成マルウェアでブロックチェーン技術者を標的に」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-96093ec62047a80740ea` |
| sectors | 防衛・軍事 | 活動「北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| sectors | 教育・研究 | 活動「北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Konniハッカー、AI生成マルウェアでブロックチェーン技術者を標的に | 非公開 | anonymous | unknown | reported | target--activity-rule--sector--63c9fa67327d005b07b7, target--activity-rule--sector--932f4928d5e1ec28e2df |  | ttp--activity-rule--3fad972c8e2a861c68a1 |  |  | 不明 | 不明 | 2026-01-26 | 中 | `source--daily-96093ec62047a80740ea` |
| 被害事例: 北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化 | 非公開 | anonymous | unknown | reported | target--activity-rule--country--36f1b9323d5faab92f39, target--activity-rule--country--72caf60a2fbce4a1be7a, target--activity-rule--country--f0d8df51439c4d0f3a05, target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--b94dc560a327b601965d, target--activity-rule--sector--e7608f51421ca8b1e297 |  | ttp--activity-rule--3b783b9995900a730cd6, ttp--activity-rule--a6b49b799bed2d732b35 | メール／メールアカウント | espionage: 北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化 | 不明 | 不明 | 2025-05-14 | 中 | `source--daily-a70f8f04454a7b9e932e` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution | T1059.001 | PowerShell | リンク先でパスワード付きRARファイルを配布し、PowerShellスクリプトで感染させる。 |  | activity--daily-e8d56cd0b459da326e44 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | CABにはPSバックドア・2つのBAT・UAC回避用実行ファイルが含まれ、OneDrive偽装のタスクでXOR暗号化スクリプトを定期実行・痕跡削除。 |  | activity--daily-ed16c556a166870fdeb2 | 不明 | 不明 | 中 | `source--daily-96093ec62047a80740ea` |
| Initial Access | T1566.002 | Spearphishing Link | フィッシングメールでシンクタンクを装い、政治・軍事イベントに関するリンクを送信。 |  | activity--daily-e8d56cd0b459da326e44 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 9件（`artifacts.csv`）

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
| source--daily-96093ec62047a80740ea | Konniハッカー、AI生成マルウェアでブロックチェーン技術者を標的に | bleepingcomputer.com | 2026-01-26 | https://www.bleepingcomputer.com/news/security/konni-hackers-target-blockchain-engineers-with-ai-built-malware/ | osint-report | TLP:CLEAR | 中 |
| source--daily-a70f8f04454a7b9e932e | 北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化 | bleepingcomputer.com | 2025-05-14 | https://www.bleepingcomputer.com/news/security/north-korea-ramps-up-cyberspying-in-ukraine-to-assess-war-risk/ | osint-report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--ta406--0cd2d3dd1d9de766 | North Korea’s Cyber Strategy |  | 不明 | International Strategic/Korea/North Korea’s Cyber Strategy.pdf | report | TLP:CLEAR | 中 |
| source--ta406--4c6e980faaf5d978 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--ta406--8474b74fc891e822 | The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities |  | 不明 | International Strategic/Korea/The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities.pdf | report | TLP:CLEAR | 中 |
| source--ta406--aa4b972d485757d1 | konni threat insight paper triple threat N Korea aligned TA406 steals scams spies |  | 不明 | konni/konni-threat-insight-paper-triple-threat-N-Korea-aligned-TA406-steals-scams-spies.pdf | report | TLP:CLEAR | 中 |
| source--ta406--f6af5ad229019991 | ta406 |  | 不明 | actor_profile/evidence/ta406.csv | structured-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
