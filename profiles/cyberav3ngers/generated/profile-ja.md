# CyberAv3ngers 脅威アクタープロファイル

- プロファイルID: `actor--cyberav3ngers`
- 状態: draft
- 更新日時: 2026-09-20T12:23:31Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

CyberAv3ngersの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **CyberAv3ngers**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| APT Iran | catalog / CISA / joint government advisory | exact | 高 | `source--actor-mapping-workbook`, `source--cisa-aa23-335a` | Alias scope must be reviewed before publication. The joint advisory explicitly lists this as another name used for CyberAv3ngers. |
| Bauxite | catalog / CISA / joint government advisory | exact | 高 | `source--actor-mapping-workbook`, `source--cisa-aa23-335a` | Alias scope must be reviewed before publication. The joint advisory explicitly lists this as another name used for CyberAv3ngers. |
| Hydro Kitten | catalog / CISA / joint government advisory | exact | 高 | `source--actor-mapping-workbook`, `source--cisa-aa23-335a` | Alias scope must be reviewed before publication. The joint advisory explicitly lists this as another name used for CyberAv3ngers. |
| Mr. Soul | catalog / CISA / joint government advisory | exact | 高 | `source--actor-mapping-workbook`, `source--cisa-aa23-335a` | Alias scope must be reviewed before publication. The joint advisory explicitly lists this as another name used for CyberAv3ngers. |
| Shahid Kaveh Group | catalog / CISA / joint government advisory | exact | 高 | `source--actor-mapping-workbook`, `source--cisa-aa23-335a` | Alias scope must be reviewed before publication. The joint advisory explicitly lists this as another name used for CyberAv3ngers. |
| Soldiers of Soloman | MITRE ATT&CK / CISA / joint government advisory | exact | 高 | `source--mitre-attack-ics-19-2`, `source--cisa-aa23-335a` | Alias scope must be reviewed before publication. The joint advisory explicitly lists this as another name used for CyberAv3ngers. |
| Soldiers of Solomon | catalog / CISA / joint government advisory | exact | 高 | `source--actor-mapping-workbook`, `source--cisa-aa23-335a` | Alias scope must be reviewed before publication. The joint advisory explicitly lists this as another name used for CyberAv3ngers. |
| Storm-0784 | CISA / joint government advisory | exact | 高 | `source--actor-mapping-workbook`, `source--cisa-aa23-335a` | The joint CISA advisory explicitly lists Storm-0784 as another name used for CyberAv3ngers. The joint advisory explicitly lists this as another name used for CyberAv3ngers. |
| UNC5691 | CISA / joint government advisory | exact | 高 | `source--actor-mapping-workbook`, `source--cisa-aa23-335a` | The joint CISA advisory explicitly lists UNC5691 as another name used for CyberAv3ngers. The joint advisory explicitly lists this as another name used for CyberAv3ngers. |

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
| Adversary | The [CyberAv3ngers](https://attack.mitre.org/groups/G1027) are a suspected Iranian Government Islamic Revolutionary Guard Corps (IRGC)-affiliated APT group. The [CyberAv3ngers](https://attack.mitre.org/groups/G1027) have been known to be active since at least 2020, with disputed and false claims of critical infrastructure compromises in Israel.(Citation: CISA AA23-335A IRGC-Affiliated December 2023)<br><br>In 2023, the [CyberAv3ngers](https://attack.mitre.org/groups/G1027) engaged in a global targeting and hacking of the Unitronics [Programmable Logic Controller (PLC)](https://attack.mitre.org/assets/A0003) with [Human-Machine Interface (HMI)](https://attack.mitre.org/assets/A0002). This PLC can be found in multiple sectors, including water and wastewater, energy, food and beverage manufacturing, and healthcare. The most notable feature of this attack was the defacement of the devices user interface.(Citation: CISA AA23-335A IRGC-Affiliated December 2023) |
| Capability |  |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-09-20T12:23:31Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | CyberAv3ngers | canonical-name | 高 | Iran | https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=CyberAv3ngers&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Cyber Av3ngers | canonical-name | 高 | IR | https://claroty.com/team82/research/inside-a-new-ot-iot-cyber-weapon-iocontrol<br>https://cyberwarzone.com/cyber-av3ngers-claims-infiltration-of-israeli-water-treatment-stations-amid-ongoing-conflict/<br>https://cyberwarzone.com/hacking-group-cyber-av3ngers-claims-responsibility-for-yavne-power-outages-what-you-need-to-know/ |
| misp-threat-actor | APTIran | single-alias-intersection | 中 | IR | https://www.sophos.com/en-us/blog/hacktivist-campaigns-increase-as-united-states-iran-and-israel-conflict-intensifies<br>https://blog.talosintelligence.com/talos-developing-situation-in-the-middle-east/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | CyberAv3ngers - G1027 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1027<br>https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a |
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
| Unitronics Defacement Campaign | campaign | 2023-11-01T04:00:00.000Z | 2023-11-01T04:00:00.000Z | 不明 |  |  |  |  | The [Unitronics Defacement Campaign](https://attack.mitre.org/campaigns/C0031) was a collection of intrusions across multiple sectors by the [CyberAv3ngers](https://attack.mitre.org/groups/G1027), where threat actors engaged in a seemingly opportunistic and global targeting and defacement of Unitronics Vision Series [Programmable Logic Controller (PLC)](https://attack.mitre.org/assets/A0003) with [Human-Machine Interface (HMI)](https://attack.mitre.org/assets/A0002). The sectors that these PLCs can be commonly found in are water and wastewater, energy, food and beverage manufacturing, and healthcare. The most notable feature of this attack was the defacement of the PLCs' HMIs.(Citation: CISA AA23-335A IRGC-Affiliated December 2023)(Citation: Frank Bajak and Marc Levy December 2023) | 高 | `source--mitre-attack-ics-19-2` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| Unitronics Defacement Campaign | CyberAv3ngers | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 高 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アイルランド | 構造化OSINTの被害国フィールドでCyberAv3ngersの標的・被害国としてアイルランドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イスラエル | 構造化OSINTの被害国フィールドでCyberAv3ngersの標的・被害国としてイスラエルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | 構造化OSINTの被害国フィールドでCyberAv3ngersの標的・被害国として米国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 全世界 | 活動「Unitronics Defacement Campaign」の記述で標的地域として全世界が明示されている。 | 2023-11-01T04:00:00.000Z | 2023-11-01T04:00:00.000Z | 中 | `source--mitre-attack-ics-19-2` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

TTPなし

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 29件（`artifacts.csv`）

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
| source--mitre-attack-ics-19-2 | MITRE ICS ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-ics-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--cyberav3ngers--106f612f8ab97f85 | cyberav3ngers |  | 不明 | actor_profile/evidence/cyberav3ngers.csv | structured-data | TLP:CLEAR | 中 |
| source--cyberav3ngers--d71edb0f6ff67c90 | the rise of state sponsored hacktivism |  | 不明 | Anonymous/the-rise-of-state-sponsored-hacktivism.pdf | report | TLP:CLEAR | 中 |
| source--cyberav3ngers--152c1f2d9b249a24 | Iranian Affiliated Cyber Actors Exploit Programmable Logic Controllers Across US Critical Infrastructure |  | 不明 | International Strategic/Iran/Iranian-Affiliated Cyber Actors Exploit Programmable Logic Controllers Across US Critical Infrastructure.pdf | report | TLP:CLEAR | 中 |
| source--cyberav3ngers--5b62707243ae7ad0 | Dragos 2026 OT Cybersecurity Report A Year in Review |  | 2026 | OT/Dragos-2026-OT-Cybersecurity-Report-A-Year-in-Review.pdf | report | TLP:CLEAR | 中 |
| source--cyberav3ngers--0c21f283be880c9f | Virtual Routes Pharos Report Series No. 3 |  | 不明 | cybercrime/2025/Virtual-Routes-Pharos-Report-Series-No.-3.pdf | report | TLP:CLEAR | 中 |
| source--cyberav3ngers--6057bf0b022bf568 | 20241213 |  | 2024-12-13 | parse-daily/.cache/tech-memo/daily-news/news/2024_10-12/20241213.md | repository-notes | TLP:CLEAR | 中 |
| source--cyberav3ngers--58a94cf3d8d56678 | 20260319 |  | 2026-03-19 | parse-daily/.cache/tech-memo/daily-news/news/2026_01-03/20260319.md | repository-notes | TLP:CLEAR | 中 |
| source--cyberav3ngers--1c5b5d3e97efac05 | review decisions |  | 不明 | parse-daily/review-decisions.json | structured-data | TLP:CLEAR | 中 |
| source--cyberav3ngers--5536060175073630 | 2024 security report |  | 2024 | summary/2024/2024-security-report.pdf | report | TLP:CLEAR | 中 |
| source--cyberav3ngers--7f21615520e6a114 | Hurdling Over Hazards  Multifaceted Threats to the Paris Olympics |  | 不明 | summary/2024/Hurdling Over Hazards- Multifaceted Threats to the Paris Olympics.pdf | report | TLP:CLEAR | 中 |
| source--cyberav3ngers--a7d6d28764eb7ae7 | Microsoft Digital Defense Report 2024 |  | 2024 | summary/2024/Microsoft Digital Defense Report 2024.pdf | report | TLP:CLEAR | 中 |
| source--cyberav3ngers--0c5cffbbe8dc01be | state of the threat report 2024 |  | 2024 | summary/2024/state-of-the-threat-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--cyberav3ngers--553055621b4e70e2 | tool of first resort israel hamas war cyber |  | 不明 | summary/2024/tool-of-first-resort-israel-hamas-war-cyber.pdf | report | TLP:CLEAR | 中 |
| source--cyberav3ngers--728ad1d57fc7069a | 2025 CrowdStrike European Threat Landscape Report |  | 2025 | summary/2025/2025-CrowdStrike-European-Threat-Landscape-Report_.pdf | report | TLP:CLEAR | 中 |
| source--cyberav3ngers--79ab83de3f206258 | Dragos 2025 OT Cybersecurity Report A Year in Review |  | 2025 | summary/2025/Dragos-2025-OT-Cybersecurity-Report-A-Year-in-Review.pdf | report | TLP:CLEAR | 中 |
| source--cyberav3ngers--92a43491c59a7b85 | search |  | 不明 | ui/api/v1/search.json | structured-data | TLP:CLEAR | 中 |
| source--unc5691--b9d192111a17e3e7 | unc5691 |  | 不明 | actor_profile/evidence/unc5691.csv | structured-data | TLP:CLEAR | 中 |
| source--storm-0784--27d1f8d3bbe19980 | storm 0784 |  | 不明 | actor_profile/evidence/storm-0784.csv | structured-data | TLP:CLEAR | 中 |
| source--cisa-aa23-335a | IRGC-Affiliated Cyber Actors Exploit PLCs in Multiple Sectors | CISA, FBI, NSA, EPA, INCD and NCSC-IL | 2023-12-01 | International Strategic/Iran/Iranian-Affiliated Cyber Actors Exploit Programmable Logic Controllers Across US Critical Infrastructure.pdf | government-advisory | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
