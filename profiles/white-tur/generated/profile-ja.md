# White Tur 脅威アクタープロファイル

- プロファイルID: `actor--white-tur`
- 状態: draft
- 更新日時: 2026-07-25T11:07:07Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

White Turの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **White Tur**
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

- 判定: `no-match`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
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



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Exfiltration | T1041 | Exfiltration Over C2 Channel | ации жертвы. White Tur Регион Начало операции TOP Mitre Европа 2017 • Command and Scripting Interpreter: PowerShell (T1059.001) • Exfiltration Over C2 Channel (T1041) • Command and Scripting Interpreter: Visual Basic (T1059.005) • XSL Script |  |  | 不明 | 不明 | 中 | `source--white-tur--b6318d27aa82342b` |
| Execution | T1059.001 | PowerShell | нял XSS-атаку на веб-почту Zimbra в организации жертвы. White Tur Регион Начало операции TOP Mitre Европа 2017 • Command and Scripting Interpreter: PowerShell (T1059.001) • Exfiltration Over C2 Channel (T1041) • Command and Scripting Interpreter: Visual Basic (T1059.005) • XSL Script |  |  | 不明 | 不明 | 中 | `source--white-tur--b6318d27aa82342b` |
| Execution | T1059.005 | Visual Basic | ропа 2017 • Command and Scripting Interpreter: PowerShell (T1059.001) • Exfiltration Over C2 Channel (T1041) • Command and Scripting Interpreter: Visual Basic (T1059.005) • XSL Script |  |  | 不明 | 不明 | 中 | `source--white-tur--b6318d27aa82342b` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | 111} White Tur (T1041) • Command and Scripting Interpreter: Visual Basic (T1059.005) • XSL Script Processing (T1220) • Deobfuscate/Decode Files or Information (T1140) Еще одна обнаруженная в этом периоде группировка получила название White Tur. Использование названия белого цвета говорит о том, что официально местонахождение группировки неизвестно. Уникальной особенностью этого злоумышленника является его виктимология, нацеленная на оборонны |  |  | 不明 | 不明 | 中 | `source--white-tur--b6318d27aa82342b` |
| Stealth | T1220 | XSL Script Processing | ib-hi-tech-crime-trends-2022-2023-ru.pdf {"page": 111} White Tur (T1041) • Command and Scripting Interpreter: Visual Basic (T1059.005) • XSL Script Processing (T1220) • Deobfuscate/Decode Files or Information (T1140) Еще одна обнаруженная в этом периоде группировка получила название White Tur. Использование названия белого цвета говорит о том, что официально местонахождение группировки неизвестно. Уникальной особенностью этого злоумышленника |  |  | 不明 | 不明 | 中 | `source--white-tur--b6318d27aa82342b` |

## IOC／artifact概要

- IOC値: 2件
- IOC観測: 2件
- 複数攻撃で観測: 0件
- 要レビュー候補: 2件
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
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--white-tur--b6318d27aa82342b | white tur |  | 不明 | actor_profile/evidence/white-tur.csv | structured-data | TLP:CLEAR | 中 |
| source--white-tur--85a95d406cb9e95a | 2022 year in retrospect report |  | 2022 | summary/2023/2022-year-in-retrospect-report.pdf | report | TLP:CLEAR | 中 |
| source--white-tur--56f0631994eb16f2 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
