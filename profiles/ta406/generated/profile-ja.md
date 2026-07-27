# TA406 脅威アクタープロファイル

- プロファイルID: `actor--ta406`
- 状態: draft
- 更新日時: 2026-07-27T11:17:25Z
- 構造バージョン: 1.0.0

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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|
| 北朝鮮、ウクライナでの戦争リスク評価のためサイバースパイ活動を強化 | phishing-campaign | 不明 | 不明 | 2025-05-14 | 北朝鮮支援のハッカーグループ「Konni（TA406）」が、ウクライナ政府機関を標的に情報収集活動を実施。 フィッシングメールでシンクタンクを装い、政治・軍事イベントに関するリンクを送信。 リンク先でパスワード付きRARファイルを配布し、PowerShellスクリプトで感染させる。 攻撃の目的は、北朝鮮軍のウクライナ派遣に伴うリスク評価とロシアからの追加要請の可能性を分析すること。 攻撃には、偽のMicrosoftセキュリティ警告を用いた認証情報の収集も含まれる。 | 中 | `source--daily-a70f8f04454a7b9e932e` |
| Konniハッカー、AI生成マルウェアでブロックチェーン技術者を標的に | infrastructure-operation | 不明 | 不明 | 2026-01-26 | 北朝鮮系Konni（Opal Sleet/TA406）がAI生成と見られるPowerShellマルウェアでブロックチェーン開発者・技術者を標的化。 Check Point分析では日本・豪州・インド由来の検体が確認され、APACを中心とする最近の活動とされる。 攻撃はDiscordホストのリンクからZIPを配布、PDFおとりと悪性LNKで開始しPowerShellローダでDOCXとCABを展開。 CABにはPSバックドア・2つのBAT・UAC回避用実行ファイルが含まれ、OneDrive偽装のタスクでXOR暗号化スクリプトを定期実行・痕跡削除。 バックドアは難読化されC2と定期通信、整然としたコメントやUUID記述からAI支援生成の痕跡が示唆されKonniに帰属。 | 中 | `source--daily-96093ec62047a80740ea` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
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
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--ta406--0cd2d3dd1d9de766 | North Korea’s Cyber Strategy |  | 不明 | International Strategic/Korea/North Korea’s Cyber Strategy.pdf | report | TLP:CLEAR | 中 |
| source--ta406--4c6e980faaf5d978 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--ta406--8474b74fc891e822 | The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities |  | 不明 | International Strategic/Korea/The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities.pdf | report | TLP:CLEAR | 中 |
| source--ta406--aa4b972d485757d1 | konni threat insight paper triple threat N Korea aligned TA406 steals scams spies |  | 不明 | konni/konni-threat-insight-paper-triple-threat-N-Korea-aligned-TA406-steals-scams-spies.pdf | report | TLP:CLEAR | 中 |
| source--ta406--f6af5ad229019991 | ta406 |  | 不明 | actor_profile/evidence/ta406.csv | structured-data | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
