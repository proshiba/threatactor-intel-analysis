# Mustard Tempest 脅威アクタープロファイル

- プロファイルID: `actor--mustard-tempest`
- 状態: draft
- 更新日時: 2026-07-29T23:12:00Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Mustard Tempestの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Mustard Tempest**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| DEV-0206 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| GOLD PRELUDE | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Purple Vallhund | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TA569 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| UNC1543 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| Indrik Spider | related-to | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has partnered with [Indrik Spider](https://attack.mitre.org/groups/G0119) to provide access for the download of additional malware including LockBit, [WastedLocker](https://attack.mitre.org/software/S0612), and remote access tools.(Citation: Microsoft Ransomware as a Service)(Citation: Microsoft Threat Actor Naming July 2023)(Citation: Secureworks Gold Prelude Profile)(Citation: SocGholish-update) | 中 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Mustard Tempest](https://attack.mitre.org/groups/G1020) is an initial access broker that has operated the [SocGholish](https://attack.mitre.org/software/S1124) distribution network since at least 2017. [Mustard Tempest](https://attack.mitre.org/groups/G1020) has partnered with [Indrik Spider](https://attack.mitre.org/groups/G0119) to provide access for the download of additional malware including LockBit, [WastedLocker](https://attack.mitre.org/software/S0612), and remote access tools.(Citation: Microsoft Ransomware as a Service)(Citation: Microsoft Threat Actor Naming July 2023)(Citation: Secureworks Gold Prelude Profile)(Citation: SocGholish-update) |
| Capability | SocGholish, Cobalt Strike |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Indrik Spider | canonical-name | 高 | Russia | https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/<br>https://www.welivesecurity.com/2018/01/26/friedex-bitpaymer-ransomware-work-dridex-authors/<br>https://www.mcafee.com/blogs/other-blogs/mcafee-labs/spanish-mssp-targeted-by-bitpaymer-ransomware/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Mustard Tempest | canonical-name | 高 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | GOLD PRELUDE | multiple-name-intersection | 高 |  | https://www.secureworks.com/research/threat-profiles/gold-prelude |
| misp-threat-actor | Mustard Tempest | canonical-name | 高 |  | https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/<br>http://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-worm-part-of-larger-ecosystem-facilitating-pre-ransomware-activity/ |
| misp-microsoft-activity-group | Mustard Tempest | canonical-name | 高 |  | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Mustard Tempest - G1020 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1020<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://www.microsoft.com/en-us/security/blog/2022/05/09/ransomware-as-a-service-understanding-the-cybercrime-gig-economy-and-how-to-protect-yourself/ |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| INDRIK SPIDER | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--cobalt-strike | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) is a commercial, full-featured, remote access tool that bills itself as “adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors”. Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.(Citation: cobaltstrike manual)<br><br>In addition to its own capabilities, [Cobalt Strike](https://attack.mitre.org/software/S0154) leverages the capabilities of other well-known tools such as Metasploit and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: cobaltstrike manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--socgholish | SocGholish | [SocGholish](https://attack.mitre.org/software/S1124) is a JavaScript-based loader malware that has been used since at least 2017. It has been observed in use against multiple sectors globally for initial access, primarily through drive-by-downloads masquerading as software updates. SocGholish is operated by [Mustard Tempest](https://attack.mitre.org/groups/G1020) and its access has been sold to groups including [Indrik Spider](https://attack.mitre.org/groups/G0119) for downloading secondary RAT and ransomware payloads.(Citation: SentinelOne SocGholish Infrastructure November 2022)(Citation: SocGholish-update)(Citation: Red Canary SocGholish March 2024)(Citation: Secureworks Gold Prelude Profile)  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| 広告ツールを悪用して拡散するSocGholishマルウェア：LockBitやEvil Corp等への初期アクセスを提供 | malware-campaign | 不明 | 不明 | 2025-08-08 |  | malware--socgholish |  |  | SocGholishがParrot/KeitaroなどのTDSを悪用し、ユーザーを不正サイトへ誘導。 偽のブラウザ更新を装うJSローダーで、改ざんサイトから配信される。 侵害端末へのアクセスは、Evil CorpやLockBit、Dridex等に販売される。 Raspberry Robin経由の拡散も観測、ChaCha20やCVE-2024-38196の悪用に言及。 Keitaroは正規利用も多く、過剰検知なく全面遮断は困難と指摘。 | 中 | `source--daily-4c5a096408cb1636d9f7` |
| HORNSキャンペーン、偽のメールとJavaScriptペイロードを通じてRATを配信 | malware-campaign | 不明 | 不明 | 2024-12-04 |  |  |  |  | HORNSキャンペーンは、主にロシアの個人ユーザー、小売業者、サービス業者を標的とし、NetSupport RATやBurnsRATを配信しています。 これらの攻撃の最終的な目標は、これらのトロイの木馬によって得られたアクセス権を利用して、RhadamanthysやMeduzaなどの窃盗マルウェアをインストールすることです。 攻撃は、潜在的な顧客やパートナーからのリクエストや入札に偽装したZIPアーカイブ内のJScriptスクリプトを含むメールを送信する手法を取っています。 これらのスクリプトは、リモートサーバーから追加のマルウェアをダウンロードし、感染したシステムにインストールします。 攻撃者は、JavaScriptペイロードを積極的に開発し、キャンペーンの進行中に大幅な変更を加えています。 このキャンペーンは、TA569（別名Gold Prelude、Mustard Tempest、Purple Vallhund）と呼ばれる脅威アクターによるものとされています。 | 中 | `source--daily-766a563d30b306b7681d` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| 広告ツールを悪用して拡散するSocGholishマルウェア：LockBitやEvil Corp等への初期アクセスを提供 | Mustard Tempest | SocGholish | 情報なし | 情報なし | 情報なし | 情報なし | 中 |
| HORNSキャンペーン、偽のメールとJavaScriptペイロードを通じてRATを配信 | Mustard Tempest | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | ロシア | 活動「HORNSキャンペーン、偽のメールとJavaScriptペイロードを通じてRATを配信」の記述で標的・被害国として明示されている。 | 不明 | 不明 | 中 | `source--daily-766a563d30b306b7681d` |
| regions | 全世界 | 構造化OSINTの被害地域フィールドでMustard Tempestの標的範囲として全世界が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has used the filename `AutoUpdater.js` to mimic legitimate update files and has also used the Cyrillic homoglyph characters С `(0xd0a1)` and а `(0xd0b0)`, to produce the filename `Сhrome.Updаte.zip`.(Citation: Red Canary SocGholish March 2024)(Citation: SocGholish-update) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has used implants to perform system reconnaissance on targeted systems.(Citation: Microsoft Ransomware as a Service) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has deployed secondary payloads and third stage implants to compromised hosts.(Citation: Microsoft Ransomware as a Service) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1189 | Drive-by Compromise | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has used drive-by downloads for initial infection, often using fake browser updates as a lure.(Citation: SocGholish-update)(Citation: SentinelOne SocGholish Infrastructure November 2022)(Citation: Red Canary SocGholish March 2024)(Citation: Secureworks Gold Prelude Profile) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has lured users into downloading malware through malicious links in fake advertisements and spearphishing emails.(Citation: Microsoft Ransomware as a Service)(Citation: SocGholish-update) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has sent victims emails containing links to compromised websites.(Citation: SocGholish-update) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.004 | Server | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has acquired servers to host second-stage payloads that remain active for a period of either days, weeks, or months.(Citation: SentinelOne SocGholish Infrastructure November 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.008 | Malvertising | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has posted false advertisements including for software packages and browser updates in order to distribute malware.(Citation: Microsoft Ransomware as a Service) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.001 | Domains | [Mustard Tempest](https://attack.mitre.org/groups/G1020) operates a global network of compromised websites that redirect into a traffic distribution system (TDS) to select victims for a fake browser update page.(Citation: Secureworks Gold Prelude Profile)(Citation: SocGholish-update)(Citation: SentinelOne SocGholish Infrastructure November 2022)(Citation: Red Canary SocGholish March 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.001 | Upload Malware | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has hosted payloads on acquired second-stage servers for periods of either days, weeks, or months.(Citation: SentinelOne SocGholish Infrastructure November 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.004 | Drive-by Target | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has injected malicious JavaScript into compromised websites to infect victims via drive-by download.(Citation: SocGholish-update)(Citation: SentinelOne SocGholish Infrastructure November 2022)(Citation: Red Canary SocGholish March 2024)(Citation: Secureworks Gold Prelude Profile) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.006 | SEO Poisoning | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has poisoned search engine results to return fake software updates in order to distribute malware.(Citation: Microsoft Ransomware as a Service)(Citation: SocGholish-update) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 10件
- IOC観測: 10件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 23件（`artifacts.csv`）

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
| source--daily-4c5a096408cb1636d9f7 | 広告ツールを悪用して拡散するSocGholishマルウェア：LockBitやEvil Corp等への初期アクセスを提供 | thehackernews.com | 2025-08-08 | https://thehackernews.com/2025/08/socgholish-malware-spread-via-ad-tools.html | osint-report | TLP:CLEAR | 中 |
| source--daily-766a563d30b306b7681d | HORNSキャンペーン、偽のメールとJavaScriptペイロードを通じてRATを配信 | thehackernews.com | 2024-12-04 | https://thehackernews.com/2024/12/horns-campaign-delivers-rats-via-fake.html | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--mustard-tempest--0a466fea7e0945f8 | mustard tempest |  | 不明 | actor_profile/evidence/mustard-tempest.csv | structured-data | TLP:CLEAR | 中 |
| source--mustard-tempest--509050c86fcdad1d | 2024 security report |  | 2024 | summary/2024/2024-security-report.pdf | report | TLP:CLEAR | 中 |
| source--mustard-tempest--9dd35f193f60cb8c | 2025 Cyber Security Report Final |  | 2025 | summary/2025/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--mustard-tempest--9de7957331bbb5b7 | threat horizons report h1 2025 |  | 2025 | summary/2025/threat_horizons_report_h1_2025.pdf | report | TLP:CLEAR | 中 |
| source--mustard-tempest--c4567d5d62fc30b6 | 2025 Cyber Security Report Final |  | 2025 | summary/2026/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--mustard-tempest--c47d4f4c6bf80318 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--mustard-tempest--d190c655ff782ecf | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--mustard-tempest--d4cc3e9620c36e0b | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--mustard-tempest--e3319085a6142472 | Secureworks NC3 2022StateoftheThreat |  | 2022 | summary/2023/Secureworks_NC3_2022StateoftheThreat.pdf | report | TLP:CLEAR | 中 |
| source--mustard-tempest--e76b0a45237b26c8 | infoblox research report registered dgas the prolific new menace no one is talking about |  | 不明 | cybercrime/2024/infoblox-research-report-registered-dgas-the-prolific-new-menace-no-one-is-talking-about.pdf | report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
