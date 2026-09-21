# TA406 脅威アクタープロファイル

- プロファイルID: `actor--ta406`
- 状態: draft
- 更新日時: 2026-09-21T13:20:00Z
- 構造バージョン: 1.4.0

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

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Konni | overlaps-with | Proofpoint states that TA406 overlaps activity publicly tracked as Konni and Opal Sleet; Check Point directly attributes the January 2026 report's campaign to the KONNI cluster. | 中 | `source--proofpoint-ta406-konni-boundary-2025`, `source--checkpoint-konni-ai-backdoor-2026` |

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
| etda-threat-group-cards | Kimsuky, Velvet Chollima | canonical-name | 高 | North Korea | https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/<br>https://securityintelligence.com/media/recent-activity-from-itg16-a-north-korean-threat-group/<br>https://us-cert.cisa.gov/ncas/alerts/aa20-301a |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | TA406 | canonical-name | 高 | KP | https://www.proofpoint.com/us/blog/threat-insight/triple-threat-north-korea-aligned-ta406-scams-spies-and-steals<br>https://www.proofpoint.com/us/blog/threat-insight/ta406-pivots-front |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | 一致なし |  |  |  |  |

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
| 北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化 | phishing-campaign | 不明 | 不明 | 2025-05-14 | target--activity-rule--country--36f1b9323d5faab92f39, target--activity-rule--sector--210dddb39397dbe50e91 |  | ttp--activity-rule--3b783b9995900a730cd6, ttp--activity-rule--a6b49b799bed2d732b35 | victim--activity-rule--42003486e06fe6355c62 | 北朝鮮支援のハッカーグループ「Konni（TA406）」が、ウクライナ政府機関を標的に情報収集活動を実施。 フィッシングメールでシンクタンクを装い、政治・軍事イベントに関するリンクを送信。 リンク先でパスワード付きRARファイルを配布し、PowerShellスクリプトで感染させる。 攻撃の目的は、北朝鮮軍のウクライナ派遣に伴うリスク評価とロシアからの追加要請の可能性を分析すること。 攻撃には、偽のMicrosoftセキュリティ警告を用いた認証情報の収集も含まれる。 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| KONNI、ブロックチェーン技術者へAI支援生成のPowerShellバックドアを配布 | infrastructure-operation | 2025-10 | 不明 | 2026-01-22 | target--activity-rule--sector--63c9fa67327d005b07b7, target--activity-rule--sector--932f4928d5e1ec28e2df, target--targeting-audit--country--60ac93d5799e9eb12580, target--targeting-audit--country--75157eeb3ccdec29dfaa |  |  | victim--activity-rule--0327ca792873c263402d | Check Point Researchは、KONNIに関連付けたフィッシング活動で、ブロックチェーン関連の開発者・エンジニアを狙うおとり文書と悪性LNKを確認した。LNKはPowerShellローダから永続化・UAC回避・分析回避・C2タスク実行機能を持つPowerShellバックドアを展開する。2025年10月にアップロードされた初期亜種も確認され、検体投稿元は日本・豪州・インドを含むが、投稿元を被害国の確定値とはしない。Check PointはKONNIへ直接帰属し、ProofpointはTA406をKonni/Opal Sleet活動との重複として扱うため、TA406との完全同一性は断定しない。 | 中 | `source--checkpoint-konni-ai-backdoor-2026`, `source--proofpoint-ta406-konni-boundary-2025` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| 北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化 | TA406 | 情報なし | T1059.001 PowerShell, T1566.002 Spearphishing Link | 情報なし | ウクライナ, 政府・行政 | 被害事例: 北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化 | 中 |
| KONNI、ブロックチェーン技術者へAI支援生成のPowerShellバックドアを配布 | TA406 | 情報なし | 情報なし | 情報なし | 暗号資産・Web3, IT・ソフトウェア, インド, 日本 | 被害事例: KONNIによるブロックチェーン技術者標的化 | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | インド | 活動「KONNI、ブロックチェーン技術者へAI支援生成のPowerShellバックドアを配布」の記述で標的・被害国として明示されている。 | 2025-10 | 不明 | 中 | `source--checkpoint-konni-ai-backdoor-2026`, `source--proofpoint-ta406-konni-boundary-2025` |
| countries | ウクライナ | 活動「北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| countries | 日本 | 活動「KONNI、ブロックチェーン技術者へAI支援生成のPowerShellバックドアを配布」の記述で標的・被害国として明示されている。 | 2025-10 | 不明 | 中 | `source--checkpoint-konni-ai-backdoor-2026`, `source--proofpoint-ta406-konni-boundary-2025` |
| sectors | 政府・行政 | 活動「北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| sectors | 暗号資産・Web3 | 活動「KONNI、ブロックチェーン技術者へAI支援生成のPowerShellバックドアを配布」の記述で標的として明示された産業。 | 2025-10 | 2025-10 | 中 | `source--checkpoint-konni-ai-backdoor-2026`, `source--proofpoint-ta406-konni-boundary-2025` |
| sectors | IT・ソフトウェア | 活動「KONNI、ブロックチェーン技術者へAI支援生成のPowerShellバックドアを配布」の記述で標的として明示された産業。 | 2025-10 | 2025-10 | 中 | `source--checkpoint-konni-ai-backdoor-2026`, `source--proofpoint-ta406-konni-boundary-2025` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: KONNIによるブロックチェーン技術者標的化 | 非公開 | anonymous | unknown | reported | target--activity-rule--sector--63c9fa67327d005b07b7, target--activity-rule--sector--932f4928d5e1ec28e2df |  |  |  |  | 2025-10 | 不明 | 2026-01-22 | 中 | `source--checkpoint-konni-ai-backdoor-2026`, `source--proofpoint-ta406-konni-boundary-2025` |
| 被害事例: 北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化 | 非公開 | anonymous | unknown | reported | target--activity-rule--country--36f1b9323d5faab92f39, target--activity-rule--sector--210dddb39397dbe50e91 |  | ttp--activity-rule--3b783b9995900a730cd6, ttp--activity-rule--a6b49b799bed2d732b35 | メール／メールアカウント | espionage: 北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化 | 不明 | 不明 | 2025-05-14 | 中 | `source--daily-a70f8f04454a7b9e932e` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution | T1059.001 | PowerShell | リンク先でパスワード付きRARファイルを配布し、PowerShellスクリプトで感染させる。 |  | activity--daily-e8d56cd0b459da326e44 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| Initial Access | T1566.002 | Spearphishing Link | フィッシングメールでシンクタンクを装い、政治・軍事イベントに関するリンクを送信。 |  | activity--daily-e8d56cd0b459da326e44 | 不明 | 不明 | 中 | `source--daily-a70f8f04454a7b9e932e` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

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
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--checkpoint-konni-ai-backdoor-2026 | KONNI Adopts AI to Generate PowerShell Backdoors | Check Point Research | 2026-01-22 | https://research.checkpoint.com/2026/konni-targets-developers-with-ai-malware/ | vendor-threat-research | TLP:CLEAR | 高 |
| source--proofpoint-ta406-konni-boundary-2025 | TA406 Pivots to the Front | Proofpoint Threat Research | 2025-05-13 | https://www.proofpoint.com/us/blog/threat-insight/ta406-pivots-front | vendor-threat-research | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
