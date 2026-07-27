# UNC4899 脅威アクタープロファイル

- プロファイルID: `actor--unc4899`
- 状態: draft
- 更新日時: 2026-07-27T11:04:38Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

UNC4899の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC4899**
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
| etda-threat-group-cards | Lazarus Group, Hidden Cobra, Labyrinth Chollima | canonical-name | 高 | North Korea | https://blog.malwarebytes.com/threat-analysis/2019/03/the-advanced-persistent-threat-files-lazarus-group/<br>https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/a-look-into-the-lazarus-groups-operations<br>https://www.kaspersky.com/about/press-releases/2017_chasing-lazarus-a-hunt-for-the-infamous-hackers-to-prevent-large-bank-robberies |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | TraderTraitor | canonical-name | 高 | KP | https://www.mandiant.com/resources/blog/north-korea-supply-chain<br>https://us-cert.cisa.gov/ncas/alerts/aa22-108a<br>https://www.mandiant.com/resources/blog/north-korea-cyber-structure-alignment-2023 |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Lazarus Group | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

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
| 北朝鮮のハッカー、洗練されたフィッシング戦術でブラジルのフィンテックを標的に | phishing-campaign | 不明 | 不明 | 2024-06-15 | 北朝鮮のハッカーが、ブラジルのフィンテック企業を標的に洗練されたフィッシング攻撃を実行。 UNC4899（Jade Sleet）がPythonアプリをトロイの木馬化し、SNSで標的に接触し、GitHubプロジェクトを通じてマルウェアを配布。 有名な暗号通貨企業を装う求人でフィッシング。無害なPDFが添付されている。ターゲットが求人に反応したら追加のPDFを送る。 PDFで、スキルに関するアンケートと、GitHubからプロジェクトをダウンロードして、コーディング課題を完了するように要求。このプロジェクトにマルウェアが仕込まれている。 他の北朝鮮グループも同様の手法を使用し、フィッシングメールで悪意のあるソフトウェアを配信。 | 中 | `source--daily-eba291a90b11ea99ea6e` |
| 北朝鮮系ハッカーグループ「Slow Pisces」、暗号通貨開発者を標的にしたPythonマルウェア攻撃を展開 | infrastructure-operation | 不明 | 不明 | 2025-04-16 | 北朝鮮と関連があるとされるハッカーグループ「Slow Pisces」（別名：Jade Sleet、PUKCHONG、TraderTraitor、UNC4899）は、暗号通貨開発者を標的にしたマルウェアキャンペーンを実施。 LinkedInを通じて開発者に接触し、偽の求人情報やコーディング課題を装ってマルウェアを配布。 被害者は、GitHub上のトロイの木馬化されたPythonプロジェクトをダウンロード・実行するよう誘導され、これにより「RN Loader」および「RN Stealer」と呼ばれるマルウェアに感染。 「RN Stealer」はmacOSシステム上で機密情報（iCloudキーチェーン、SSHキー、AWS/Kubernetes/Google Cloudの設定ファイルなど）を収集。 攻撃は多段階で行われ、C2サーバーは被害者のIPアドレスや地理情報などに基づいてペイロードの配信を制御。 コード実行には、`yaml.load()`や`ejs.render()`などの手法を用いて検出を回避。 | 中 | `source--daily-744b9664f686bf2ed5cd` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 17件（`artifacts.csv`）

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
| source--daily-744b9664f686bf2ed5cd | 北朝鮮系ハッカーグループ「Slow Pisces」、暗号通貨開発者を標的にしたPythonマルウェア攻撃を展開 | thehackernews.com | 2025-04-16 | https://thehackernews.com/2025/04/crypto-developers-targeted-by-python.html | osint-report | TLP:CLEAR | 中 |
| source--daily-eba291a90b11ea99ea6e | 北朝鮮のハッカー、洗練されたフィッシング戦術でブラジルのフィンテックを標的に | thehackernews.com | 2024-06-15 | https://thehackernews.com/2024/06/north-korean-hackers-target-brazilian.html | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unc4899--028ff7267b0d9392 | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | International Strategic/Korea/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--unc4899--0ff0d325de512842 | 2024 Blockchain Security and AML Annual Report(EN) |  | 2024 | summary/2025/2024-Blockchain-Security-and-AML-Annual-Report(EN).pdf | report | TLP:CLEAR | 中 |
| source--unc4899--1390332551d8c3af | advances in threat actor usage of ai tools en |  | 不明 | AISecurity/2025/advances-in-threat-actor-usage-of-ai-tools-en.pdf | report | TLP:CLEAR | 中 |
| source--unc4899--2246c521b1b228d1 | unc4899 |  | 不明 | actor_profile/evidence/unc4899.csv | structured-data | TLP:CLEAR | 中 |
| source--unc4899--3e59f7f25cb2d69e | The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities |  | 不明 | International Strategic/Korea/The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities.pdf | report | TLP:CLEAR | 中 |
| source--unc4899--49cddfde804b2b45 | 2025 Blockchain Security and AML Annual Report |  | 2025 | summary/2025/2025-Blockchain-Security-and-AML-Annual-Report.pdf | report | TLP:CLEAR | 中 |
| source--unc4899--79cdef4e25eb8cd8 | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--unc4899--b5b8dda7301c9303 | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | CyberMerceNary/ITWorker/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--unc4899--d91b559d4a2e0f1b | cybercrime multifaceted national security threat |  | 不明 | summary/2025/cybercrime-multifaceted-national-security-threat.pdf | report | TLP:CLEAR | 中 |
| source--unc4899--e1520dd17d1e4dfd | Qianxin 2023 APT Report |  | 2023 | summary/2024/Qianxin 2023 APT Report.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
