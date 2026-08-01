# Earth Berberoka 脅威アクタープロファイル

- プロファイルID: `actor--earth-berberoka`
- 状態: draft
- 更新日時: 2026-07-29T23:13:54Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Earth Berberokaの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Earth Berberoka**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Gambling Puppet | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| GamblingPuppet | catalog | overlapping | 中 | `source--actor-mapping-workbook` | Alias scope must be reviewed before publication. |
| GamblingPuppet, Gambling Puppet | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 113; mapping requires review. |
| Emissary Panda, Iron Tiger | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 113; mapping requires review. |

## 帰属

The repository mapping workbook places this actor in the China worksheet.

- 国: China
- スポンサー種別: state
- 確度: 中
- 証拠: `source--actor-mapping-workbook`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | State-sponsored intelligence collection or strategic operations. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability |  |
| Infrastructure |  |
| Victim | Chinese gambling websites, one education-related government institution, two IT services companies, and one electronics manufacturing company |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Earth Berberoka | canonical-name | 高 | China | https://www.trendmicro.com/en_us/research/22/d/new-apt-group-earth-berberoka-targets-gambling-websites-with-old.html<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Earth+Berberoka&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Earth Berberoka | canonical-name | 高 | CN | https://documents.trendmicro.com/assets/white_papers/wp-operation-earth-berberoka.pdf<br>https://www.trendmicro.com/en_us/research/22/d/new-apt-group-earth-berberoka-targets-gambling-websites-with-old.html<br>https://documents.trendmicro.com/assets/txt/earth-berberoka-windows-iocs-2.txt |
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

### 活動別ダイヤモンドモデル

活動別ダイヤモンドモデルなし



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | マレーシア | 構造化OSINTの被害国フィールドでEarth Berberokaの標的・被害国としてマレーシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | 中国 | レビュー済みアクターマッピングの標的欄に記録された中国を構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-misp-threat-actor` |
| countries | 台湾 | 構造化OSINTの被害国フィールドでEarth Berberokaの標的・被害国として台湾が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | 米国 | 構造化OSINTの被害国フィールドでEarth Berberokaの標的・被害国として米国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | 香港 | 構造化OSINTの被害国フィールドでEarth Berberokaの標的・被害国として香港が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| regions | 東アジア | 中国、台湾、香港で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-misp-threat-actor` |
| regions | 東南アジア | 構造化OSINTの被害地域フィールドでEarth Berberokaの標的範囲として東南アジアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| sectors | Education and Research | Targeting text indicates the Education and Research sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Government | Targeting text indicates the Government sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Manufacturing | Targeting text indicates the Manufacturing sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Technology | Targeting text indicates the Technology sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Privilege Escalation, Stealth | T1055 | Process Injection | roka Регион Начало операции TOP Mitre АТР, Америка Декабрь 2020 • Supply Chain Compromise (T1195) • Virtualization/Sandbox Evasion (T1497) • Process Injection (T1055) • Credentials from Password Stores (T1555) • Screen Capt |  |  | 不明 | 不明 | 中 | `source--earth-berberoka--1ee1533d6cfe60f0` |
| Collection | T1113 | Screen Capture | nds-2022-2023-ru.pdf {"page": 112} Earth Berberoka box Evasion (T1497) • Process Injection (T1055) • Credentials from Password Stores (T1555) • Screen Capture (T1113) Согласно анализу, эта группа нацелена на сайты с азартными играми. Расследование также показало, что Earth Berberoka нацелена на плат - формы Windows, Linux и macOS и использует семейства вредоносных программ, которые исторически приписывались синоязычным группам. |  |  | 不明 | 不明 | 中 | `source--earth-berberoka--1ee1533d6cfe60f0` |
| Initial Access | T1195 | Supply Chain Compromise | с груп - пировками, такими как RedFoxtrot и Nomad Panda. Earth Berberoka Регион Начало операции TOP Mitre АТР, Америка Декабрь 2020 • Supply Chain Compromise (T1195) • Virtualization/Sandbox Evasion (T1497) • Process Injection (T1055) • Credentials from Password Stores (T1555) • Screen Capt |  |  | 不明 | 不明 | 中 | `source--earth-berberoka--1ee1533d6cfe60f0` |
| Discovery, Stealth | T1497 | Virtualization/Sandbox Evasion | t и Nomad Panda. Earth Berberoka Регион Начало операции TOP Mitre АТР, Америка Декабрь 2020 • Supply Chain Compromise (T1195) • Virtualization/Sandbox Evasion (T1497) • Process Injection (T1055) • Credentials from Password Stores (T1555) • Screen Capt |  |  | 不明 | 不明 | 中 | `source--earth-berberoka--1ee1533d6cfe60f0` |
| Credential Access | T1555 | Credentials from Password Stores | Америка Декабрь 2020 • Supply Chain Compromise (T1195) • Virtualization/Sandbox Evasion (T1497) • Process Injection (T1055) • Credentials from Password Stores (T1555) • Screen Capt |  |  | 不明 | 不明 | 中 | `source--earth-berberoka--1ee1533d6cfe60f0` |

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 12件（`artifacts.csv`）

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
| source--earth-berberoka--1ee1533d6cfe60f0 | earth berberoka |  | 不明 | actor_profile/evidence/earth-berberoka.csv | structured-data | TLP:CLEAR | 中 |
| source--earth-berberoka--396faba6a4d82eb7 | top 10 macos malware discoveries in 2022 |  | 2022 | summary/2022/top-10-macos-malware-discoveries-in-2022.pdf | report | TLP:CLEAR | 中 |
| source--earth-berberoka--d8625815d52f0be0 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
