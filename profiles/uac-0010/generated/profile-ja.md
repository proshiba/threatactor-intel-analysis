# UAC-0010 脅威アクタープロファイル

- プロファイルID: `actor--uac-0010`
- 状態: draft
- 更新日時: 2026-07-27T11:17:26Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

UAC-0010の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UAC-0010**
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
| etda-threat-group-cards | Gamaredon Group | canonical-name | 高 | Russia | https://www.lookingglasscyber.com/wp-content/uploads/2015/08/Operation_Armageddon_Final.pdf<br>https://unit42.paloaltonetworks.com/unit-42-title-gamaredon-group-toolset-evolution/<br>https://www.fortinet.com/blog/threat-research/gamaredon-group-ttp-profile-analysis.html |
| cert-ua-uac-index | UAC-0010 | canonical-name | 高 |  | https://cert.gov.ua/article/971405<br>https://cert.gov.ua/article/40240<br>https://cert.gov.ua/article/1229152 |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Gamaredon Group | canonical-name | 高 | RU | http://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution<br>https://www.lookingglasscyber.com/wp-content/uploads/2015/08/Operation_Armageddon_Final.pdf<br>https://unit42.paloaltonetworks.com/unit-42-title-gamaredon-group-toolset-evolution |
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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|
| FSBのマトリョーシカ #1/3：展開され続けるGamaredonの贈り物――GammaPhishとGammaWorm | phishing-campaign | 不明 | 不明 | 2026-06-03 | Sekoiaは、2026年1月に展開されたGamaredonの感染チェーンの初期アクセスとワーム部分を分析した。 GamaredonはロシアFSBに公式に関連付けられるAPTで、ウクライナの政府・軍・重要インフラを長期的に標的化している。 GammaPhishはxHTMLとRARを使い、WinRARのCVE-2025-8088を悪用してStartupフォルダへHTAを配置する。 GammaWormはVBScript、NTFS ADS、RunOnce、スケジュールタスクを悪用して永続化し、USBやネットワーク共有で拡散する。 Telegram、Cloudflare、Teletype、Telegra.phなどの正規サービスをDDRとして悪用し、C2構成更新と任意コード実行を行う。 | 中 | `source--daily-f9666a37c61d10f83b24` |



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
- 非IOC artifact観測: 15件（`artifacts.csv`）

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
| source--daily-f9666a37c61d10f83b24 | FSBのマトリョーシカ #1/3：展開され続けるGamaredonの贈り物――GammaPhishとGammaWorm | blog.sekoia.io | 2026-06-03 | https://blog.sekoia.io/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-cert-ua-uac-index | CERT-UA UAC Article Index | CERT-UA | 不明 | actor_profile/reference/osint/cert-ua-uac-index.json | government-cert-article-index | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--uac-0010--0ba16103b9604a22 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--uac-0010--2ffd50a1c7118090 | Cyber operations by russia new goals, tools and groups |  | 不明 | International Strategic/Russia/Cyber operations by russia new goals, tools and groups.pdf | report | TLP:CLEAR | 中 |
| source--uac-0010--468ae9d2482ad88e | Secureworks NC3 2022StateoftheThreat |  | 2022 | summary/2023/Secureworks_NC3_2022StateoftheThreat.pdf | report | TLP:CLEAR | 中 |
| source--uac-0010--7796988d52bfe416 | 2022cyberComprehensiveSituationObservationManual |  | 2022 | summary/2023/2022cyberComprehensiveSituationObservationManual.pdf | report | TLP:CLEAR | 中 |
| source--uac-0010--a76dad0c653387b5 | Russia’s Cyber Tactics Lessons Learned 2022 |  | 2022 | International Strategic/Russia/Russia’s Cyber Tactics Lessons Learned 2022.pdf | report | TLP:CLEAR | 中 |
| source--uac-0010--b45fb340c5aab58c | uac 0010 |  | 不明 | actor_profile/evidence/uac-0010.csv | structured-data | TLP:CLEAR | 中 |
| source--uac-0010--d67ea89733ee989d | Cloudflare 2026 threat report |  | 2026 | summary/2026/Cloudflare-2026-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--uac-0010--fe514e7b8f9ef46b | RussianCyber |  | 不明 | summary/2024/RussianCyber.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
