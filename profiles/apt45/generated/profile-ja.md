# APT45 脅威アクタープロファイル

- プロファイルID: `actor--apt45`
- 状態: draft
- 更新日時: 2026-07-29T15:36:09Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

APT45の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **APT45**
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
| etda-threat-group-cards | Andariel, Silent Chollima | canonical-name | 高 | North Korea | https://asec.ahnlab.com/en/56405/<br>https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-207a<br>https://cloud.google.com/blog/topics/threat-intelligence/apt45-north-korea-digital-military-machine |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Onyx Sleet | canonical-name | 高 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | APT45 | canonical-name | 高 | KP | https://cloud.google.com/blog/topics/threat-intelligence/apt45-north-korea-digital-military-machine |
| misp-microsoft-activity-group | Onyx Sleet | canonical-name | 高 | KP, North Korea | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
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
| 北朝鮮のハッカーAPT45は、サイバースパイ活動からランサムウェア攻撃へシフト | ransomware-extortion | 不明 | 不明 | 2024-07-26 |  |  |  | victim--activity-rule--3fc2bc4c3d84f7161583 | 北朝鮮のAPT45がサイバースパイ活動からランサムウェア攻撃に移行。 APT45はSHATTEREDGLASSやMauiなどのランサムウェアを展開。 主なターゲットは韓国、日本、米国の重要インフラ。 APT45の活動は北朝鮮の資金調達に寄与。 偽の身元を用いた北朝鮮のIT労働者による企業侵入事例も発覚。 | 高 | `source--daily-e35da9939e754bf10218` |
| 北朝鮮のハッカーがVPN更新の脆弱性を悪用してマルウェアをインストール | malware-campaign | 不明 | 不明 | 2024-08-06 | target--activity-rule--country--6cb716c577f256f44a3e, target--activity-rule--sector--dfc80b76cad93a318adc |  | ttp--activity-rule--53a28d47982cd79a8719 | victim--activity-rule--c4d401b281a00a4bcbd2 | 北朝鮮のハッカーグループがVPNのアップデートの脆弱性を悪用し、マルウェアをインストール。 攻撃者はKimsukyとAndariel（APT43とAPT45）で、韓国の産業機密を狙う。 VPNソフトウェアの通信プロトコルの脆弱性を悪用し、更新プログラムを置き換えてトロイの木馬化。遠隔操作用のDoraRATをインストール。 攻撃は産業機器や設計文書の盗難を目的としている。 NCSCが警告を発表し、セキュリティ対策を推奨。 | 中 | `source--daily-444c87a0051642065f55` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 韓国 | 活動「北朝鮮のハッカーがVPN更新の脆弱性を悪用してマルウェアをインストール」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-444c87a0051642065f55` |
| sectors | 製造・産業 | 活動「北朝鮮のハッカーがVPN更新の脆弱性を悪用してマルウェアをインストール」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-444c87a0051642065f55` |

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 北朝鮮のハッカーAPT45は、サイバースパイ活動からランサムウェア攻撃へシフト | 非公開 | aggregate | multiple-organizations | reported |  |  |  |  | encryption: 北朝鮮のハッカーAPT45は、サイバースパイ活動からランサムウェア攻撃へシフト<br>espionage: 北朝鮮のハッカーAPT45は、サイバースパイ活動からランサムウェア攻撃へシフト | 不明 | 不明 | 2024-07-26 | 高 | `source--daily-e35da9939e754bf10218` |
| 被害事例: 北朝鮮のハッカーがVPN更新の脆弱性を悪用してマルウェアをインストール | 非公開 | anonymous | unknown | reported | target--activity-rule--country--6cb716c577f256f44a3e, target--activity-rule--sector--dfc80b76cad93a318adc |  | ttp--activity-rule--53a28d47982cd79a8719 | VPN／リモートアクセス機器 |  | 不明 | 不明 | 2024-08-06 | 中 | `source--daily-444c87a0051642065f55` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Initial Access | T1190 | Exploit Public-Facing Application | 北朝鮮のハッカーがVPN更新の脆弱性を悪用してマルウェアをインストール 攻撃者はKimsukyとAndariel（APT43とAPT45）で、韓国の産業機密を狙う。 |  | activity--daily-a0afddb5a69c4389af0b | 不明 | 不明 | 中 | `source--daily-444c87a0051642065f55` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 22件（`artifacts.csv`）

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
| source--apt45--0bfb3f1c3d25fac7 | SixMap Research Energy Sector Exposure Assessment |  | 不明 | summary/2025/SixMap-Research_Energy-Sector-Exposure-Assessment.pdf | report | TLP:CLEAR | 中 |
| source--apt45--1054ae071b3a9c43 | apt45 |  | 不明 | actor_profile/evidence/apt45.csv | structured-data | TLP:CLEAR | 中 |
| source--apt45--38791834d8aa772c | Cloudflare 2026 threat report |  | 2026 | summary/2026/Cloudflare-2026-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--apt45--5e3057c48655e4ec | Virtual Routes Pharos Report Series No. 3 |  | 不明 | cybercrime/2025/Virtual-Routes-Pharos-Report-Series-No.-3.pdf | report | TLP:CLEAR | 中 |
| source--apt45--a05d0ca7a4a8b82d | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--apt45--b313d496e3267518 | The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities |  | 不明 | International Strategic/Korea/The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities.pdf | report | TLP:CLEAR | 中 |
| source--apt45--ed6fa2ffb268612d | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | CyberMerceNary/ITWorker/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--apt45--f1ae5dcf9266c803 | cybercrime multifaceted national security threat |  | 不明 | summary/2025/cybercrime-multifaceted-national-security-threat.pdf | report | TLP:CLEAR | 中 |
| source--apt45--f4eaeeca006b5c39 | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | International Strategic/Korea/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--daily-444c87a0051642065f55 | 北朝鮮のハッカーがVPN更新の脆弱性を悪用してマルウェアをインストール | bleepingcomputer.com | 2024-08-06 | https://www.bleepingcomputer.com/news/security/north-korean-hackers-exploit-vpn-update-flaw-to-install-malware/ | osint-report | TLP:CLEAR | 中 |
| source--daily-e35da9939e754bf10218 | 北朝鮮のハッカーAPT45は、サイバースパイ活動からランサムウェア攻撃へシフト | thehackernews.com | 2024-07-26 | https://thehackernews.com/2024/07/north-korean-hackers-shift-from-cyber.html | osint-report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
