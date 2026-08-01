# Ferocious Kitten 脅威アクタープロファイル

- プロファイルID: `actor--ferocious-kitten`
- 状態: draft
- 更新日時: 2026-07-29T23:12:00Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Ferocious Kittenの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Ferocious Kitten**
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
| Adversary | [Ferocious Kitten](https://attack.mitre.org/groups/G0137) is a threat group that has primarily targeted Persian-speaking individuals in Iran since at least 2015.(Citation: Kaspersky Ferocious Kitten Jun 2021) |
| Capability | MarkiRAT, BITSAdmin |
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
| etda-threat-group-cards | Ferocious Kitten | canonical-name | 高 | Iran | https://securelist.com/apt-trends-report-q1-2021/101967/<br>https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Ferocious+Kitten&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Ferocious Kitten | canonical-name | 高 | IR | https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Ferocious Kitten - G0137 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0137<br>https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/ |
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
| malware--markirat | MarkiRAT | [MarkiRAT](https://attack.mitre.org/software/S0652) is a remote access Trojan (RAT) compiled with Visual Studio that has been used by [Ferocious Kitten](https://attack.mitre.org/groups/G0137) since at least 2015.(Citation: Kaspersky Ferocious Kitten Jun 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--bitsadmin | BITSAdmin | [BITSAdmin](https://attack.mitre.org/software/S0190) is a command line tool used to create and manage [BITS Jobs](https://attack.mitre.org/techniques/T1197). (Citation: Microsoft BITSAdmin) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| countries | イラン | [Ferocious Kitten](https://attack.mitre.org/groups/G0137) is a threat group that has primarily targeted Persian-speaking individuals in Iran since at least 2015.(Citation: Kaspersky Ferocious Kitten Jun 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1036.002 | Right-to-Left Override | [Ferocious Kitten](https://attack.mitre.org/groups/G0137) has used right-to-left override to reverse executables’ names to make them appear to have different file extensions, rather than their real ones.(Citation: Kaspersky Ferocious Kitten Jun 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [Ferocious Kitten](https://attack.mitre.org/groups/G0137) has named malicious files <code>update.exe</code> and loaded them into the compromise host's “Public” folder.(Citation: Kaspersky Ferocious Kitten Jun 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [Ferocious Kitten](https://attack.mitre.org/groups/G0137) has attempted to convince victims to enable malicious content within a spearphishing email by including an odd decoy message.(Citation: Kaspersky Ferocious Kitten Jun 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [Ferocious Kitten](https://attack.mitre.org/groups/G0137) has conducted spearphishing campaigns containing malicious documents to lure victims to open the attachments.(Citation: Kaspersky Ferocious Kitten Jun 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [Ferocious Kitten](https://attack.mitre.org/groups/G0137) has acquired domains imitating legitimate sites.(Citation: Kaspersky Ferocious Kitten Jun 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [Ferocious Kitten](https://attack.mitre.org/groups/G0137) has obtained open source tools for its operations, including JsonCPP and Psiphon.(Citation: Kaspersky Ferocious Kitten Jun 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 8件（`artifacts.csv`）

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
| source--ferocious-kitten--d60284b3347bccf8 | ferocious kitten |  | 不明 | actor_profile/evidence/ferocious-kitten.csv | structured-data | TLP:CLEAR | 中 |
| source--ferocious-kitten--a92f43c142b4b156 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--ferocious-kitten--08ddc700f7ae83ad | Raport analize PROFILI I GRUPEVE TE HAKERAVE IRANIANE |  | 不明 | summary/2024/Raport-analize-PROFILI-I-GRUPEVE-TE-HAKERAVE-IRANIANE.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
