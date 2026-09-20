# Calypso 脅威アクタープロファイル

- プロファイルID: `actor--calypso`
- 状態: draft
- 更新日時: 2026-09-20T12:23:31Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Calypsoの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Calypso**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Bronze Medley | SecureWorks | overlapping | 中 | `source--osint-etda-threat-group-cards` | ETDA Threat Group Cards maps Bronze Medley (SecureWorks) to Calypso (Positive Technologies). |
| Red Lamassu | Lumen Black Lotus Labs | exact | 中 | `source--daily-350d930382dd3ed9f923` | Lumen reporting cited in the reviewed daily activity describes the cluster as Calypso, aka Red Lamassu. |

## 帰属

ETDA Threat Group Cards lists Calypso as China-linked. This geographic attribution is kept separate from any state-sponsorship claim.

- 国: China
- スポンサー種別: unknown
- 確度: 中
- 証拠: `source--osint-etda-threat-group-cards`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | ETDA describes the group's motivation as information theft and espionage. | 中 | `source--osint-etda-threat-group-cards` | Aggregated actor card. |

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability | WEBC2, BISCUIT and many others |
| Infrastructure |  |
| Victim | U.S. cybersecurity firm Mandiant, later purchased by FireEye, released a report in February 2013 that exposed one of China's cyber espionage units, Unit 61398. The group, which FireEye called APT1, is a unit within China's People's Liberation Army (PLA) that has been linked to a wide range of cyber operations targeting U.S. private sector entities for espionage purposes. The comprehensive report detailed evidence connecting APT1 and the PLA, offered insight into APT1's operational malware and methodologies, and provided timelines of the espionage it conducted. |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-09-20T12:23:31Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | Calypso | canonical-name | 高 | China | https://www.ptsecurity.com/ww-en/analytics/calypso-apt-2019/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Calypso&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Calypso | canonical-name | 高 | CN | https://www.ptsecurity.com/upload/corporate/ru-ru/analytics/calypso-apt-2019-rus.pdf<br>https://www.welivesecurity.com/2021/03/10/exchange-servers-under-siege-10-apt-groups/<br>https://www.pwc.com/gx/en/issues/cybersecurity/cyber-threat-intelligence/red-lamassu-open-season.html |
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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 中国系ハッカーが新たなLinux/Windowsマルウェアで通信事業者を標的化 | cyber-espionage | 不明 | 不明 | 2026-05-22 | target--activity-rule--sector--97fa6f38a056d42117be |  | ttp--activity-rule--20b1bae9b0c6bca32748, ttp--activity-rule--7f1ef34595aa281d7470, ttp--activity-rule--b2ce07fcea1c942aa118 | victim--activity-rule--72a9b284ae5c1aa7f781 | 中国系サイバースパイ活動が、Linux向けShowboatとWindows向けJFMBackdoorで通信事業者を標的化。 活動は少なくとも2022年半ばから続き、アジア太平洋と中東の組織を狙い、Calypso(別名、Red Lamassu)に帰属。 攻撃者は複数の通信事業者風ドメインを用意し、標的組織になりすますインフラを使用していた。 Showboatはモジュール式のフレームワークで、侵害後の永続化、情報収集、ファイル転送、プロセス隠蔽、SOCKS5プロキシ機能を備える。 JFMBackdoorは多機能な諜報用マルウェアで、DLLサイドローディングで読み込まれ、リバースシェル、ファイル操作、画面取得、痕跡削除などが可能。 | 中 | `source--daily-350d930382dd3ed9f923` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| 中国系ハッカーが新たなLinux/Windowsマルウェアで通信事業者を標的化 | Calypso | 情報なし | T1090 Proxy, T1083 File and Directory Discovery, T1574.001 DLL | 情報なし | 情報通信 | 被害事例: 中国系ハッカーが新たなLinux/Windowsマルウェアで通信事業者を標的化 | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アフガニスタン | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてアフガニスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | インド | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてインドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ウクライナ | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてウクライナが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | カザフスタン | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてカザフスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | キルギス | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてキルギスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | タイ | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてタイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | トルコ | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてトルコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ブラジル | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてブラジルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ベラルーシ | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてベラルーシが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | モンゴル | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてモンゴルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ロシア | 構造化OSINTの被害国フィールドでCalypsoの標的・被害国としてロシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 中国 | Targeting text mentions china. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | 米国 | レビュー済みアクターマッピングの標的欄に記録された米国を構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| regions | 中央アジア | カザフスタン、キルギスで確認された標的・被害事例を中央アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 南アジア | アフガニスタン、インドで確認された標的・被害事例を南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東アジア | モンゴル、中国で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| regions | 東欧 | ウクライナ、ベラルーシ、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | ウクライナ、トルコ、ベラルーシで確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| sectors | 情報通信 | 活動「中国系ハッカーが新たなLinux/Windowsマルウェアで通信事業者を標的化」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-350d930382dd3ed9f923` |
| sectors | Technology | Targeting text indicates the Technology sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 中国系ハッカーが新たなLinux/Windowsマルウェアで通信事業者を標的化 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--97fa6f38a056d42117be |  | ttp--activity-rule--20b1bae9b0c6bca32748, ttp--activity-rule--7f1ef34595aa281d7470, ttp--activity-rule--b2ce07fcea1c942aa118 |  | espionage: 中国系サイバースパイ活動が、Linux向けShowboatとWindows向けJFMBackdoorで通信事業者を標的化。 | 不明 | 不明 | 2026-05-22 | 中 | `source--daily-350d930382dd3ed9f923` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1090 | Proxy | Showboatはモジュール式のフレームワークで、侵害後の永続化、情報収集、ファイル転送、プロセス隠蔽、SOCKS5プロキシ機能を備える。 |  | activity--daily-651f2178af4ab3c90c96 | 不明 | 不明 | 中 | `source--daily-350d930382dd3ed9f923` |
| Discovery | T1083 | File and Directory Discovery | JFMBackdoorは多機能な諜報用マルウェアで、DLLサイドローディングで読み込まれ、リバースシェル、ファイル操作、画面取得、痕跡削除などが可能。 |  | activity--daily-651f2178af4ab3c90c96 | 不明 | 不明 | 中 | `source--daily-350d930382dd3ed9f923` |
| Execution, Stealth | T1574.001 | DLL | JFMBackdoorは多機能な諜報用マルウェアで、DLLサイドローディングで読み込まれ、リバースシェル、ファイル操作、画面取得、痕跡削除などが可能。 |  | activity--daily-651f2178af4ab3c90c96 | 不明 | 不明 | 中 | `source--daily-350d930382dd3ed9f923` |

## IOC／artifact概要

- IOC値: 10件
- IOC観測: 10件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 58件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| Calypso is retained as a separate espionage cluster with Bronze Medley and Red Lamassu as scoped cross-vendor names; APT1/Comment Crew, Mirage, and Pitty Tiger are not treated as aliases. | 中 | `source--osint-etda-threat-group-cards`, `source--daily-350d930382dd3ed9f923` | Corrected after alias/entity review. |

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--calypso--0e7e4f509f2d953e | 200407 MWB COVID White Paper Final |  | 2004-07 | COVID/200407-MWB-COVID-White-Paper_Final.pdf | report | TLP:CLEAR | 中 |
| source--calypso--2e8dcdc34e3d8a19 | Automating APT Campaign and Group Attribution |  | 不明 | APT-hunting/Automating APT Campaign and Group Attribution.pdf | report | TLP:CLEAR | 中 |
| source--calypso--3a2fabd4303aaf44 | 360 APT Annual Research Report 2022 |  | 2022 | summary/2023/360_APT_Annual_Research_Report_2022.pdf | report | TLP:CLEAR | 中 |
| source--calypso--3c36875326389864 | calypso |  | 不明 | actor_profile/evidence/calypso.csv | structured-data | TLP:CLEAR | 中 |
| source--calypso--4122cc635cc78682 | eset threat report t12021 |  | 不明 | summary/2021/eset_threat_report_t12021.pdf | report | TLP:CLEAR | 中 |
| source--calypso--4d8d55f96e9fdb8f | Secureworks NC3 2022StateoftheThreat |  | 2022 | summary/2023/Secureworks_NC3_2022StateoftheThreat.pdf | report | TLP:CLEAR | 中 |
| source--calypso--4ed45b721c043e96 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--calypso--572db5bc0325ab0e | 2021 Vulnerability Landscape |  | 2021 | summary/2022/2021 Vulnerability Landscape.pdf | report | TLP:CLEAR | 中 |
| source--calypso--5a96fdf874b38e48 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--calypso--5cf6cac8ca43bf04 | Raport analize PROFILI I GRUPEVE TE HAKERAVE IRANIANE |  | 不明 | summary/2024/Raport-analize-PROFILI-I-GRUPEVE-TE-HAKERAVE-IRANIANE.pdf | report | TLP:CLEAR | 中 |
| source--calypso--5df2ed07b29f5b9b | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--calypso--623eb96ebf0ea82b | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--calypso--8977615ec58b186c | Modern Asian APT groups TTPs report eng |  | 不明 | summary/2023/Modern-Asian-APT-groups-TTPs_report_eng.pdf | report | TLP:CLEAR | 中 |
| source--calypso--a663e4b258965c58 | china cyber report |  | 不明 | International Strategic/China/china-cyber-report.pdf | report | TLP:CLEAR | 中 |
| source--calypso--cbe1bfe741302951 | 2024 Malicious Infrastructure Report |  | 2024 | summary/2025/2024 Malicious Infrastructure Report.pdf | report | TLP:CLEAR | 中 |
| source--calypso--e04640fed1c55bf5 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--daily-350d930382dd3ed9f923 | 中国系ハッカーが新たなLinux/Windowsマルウェアで通信事業者を標的化 | lumen.com | 2026-05-22 | https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms | osint-report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。 2026-09 entity review: removed APT1/Comment Crew, Mirage, Pitty Tiger alias contamination and workbook-only GhostNet/software mappings.
