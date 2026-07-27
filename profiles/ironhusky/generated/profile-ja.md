# IronHusky 脅威アクタープロファイル

- プロファイルID: `actor--ironhusky`
- 状態: draft
- 更新日時: 2026-07-27T11:04:32Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

IronHuskyの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **IronHusky**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Vicious Panda | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 107; mapping requires review. |

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
| Capability | MysterySnail, CVE-2021-40449 |
| Infrastructure |  |
| Victim |  |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | IronHusky | canonical-name | 高 | China | https://securelist.com/apt-trends-report-q1-2018/85280/<br>https://securelist.com/mysterysnail-new-version/116226/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=IronHusky&n=1 |
| etda-threat-group-cards | Vicious Panda | single-alias-intersection | 中 | China | https://research.checkpoint.com/2020/vicious-panda-the-covid-campaign/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Vicious+Panda&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Vicious Panda | single-alias-intersection | 中 | CN | https://securelist.com/microcin-is-here/97353<br>https://securelist.com/a-simple-example-of-a-complex-cyberattack/82636<br>https://decoded.avast.io/luigicamastra/apt-group-planted-backdoors-targeting-high-profile-networks-in-central-asia |
| misp-threat-actor | IronHusky | canonical-name | 高 | CN | https://securelist.com/mysterysnail-attacks-with-windows-zero-day/104509/<br>https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=&solutionid=sk175885 |
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

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--cve-2021-40449 | CVE-2021-40449 | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--mysterysnail | MysterySnail | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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
| 中国のハッカーがロシア政府を標的に、強化されたRATマルウェアを使用 | malware-campaign | 不明 | 不明 | 2025-04-20 | 中国語を話す「IronHusky」グループが、ロシアおよびモンゴルの政府機関を標的に、強化された「MysterySnail」RATマルウェアを使用している。 攻撃は、Word文書に偽装された悪意のあるMMCスクリプトを通じて行われ、二次ペイロードのダウンロードと永続性の確保が行われた。 新たなバージョン「MysteryMonoSnail」は、単一コンポーネントで構成され、軽量化されている。 このマルウェアは、サービスの管理、シェルコマンドの実行、プロセスの生成・終了、ファイルの操作など、数十のコマンドをサポートする。 過去の攻撃では、CVE-2021-40449やCVE-2017-11882などのゼロデイ脆弱性が悪用されていた。 | 中 | `source--daily-4fa6e9612d1bc97443df` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | cks conducted by the APT group known as IronHusky. These incidents also involved implementations of the subtechnique known as Match Legitimate Name or Location T1036.005. Example 4 We also detected similar behavior from the ToddyCat group. This is an APT group that wa |  |  | 不明 | 不明 | 中 | `source--ironhusky--17a5734d667d6538` |

## IOC／artifact概要

- IOC値: 3件
- IOC観測: 3件
- 複数攻撃で観測: 0件
- 要レビュー候補: 3件
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
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--daily-4fa6e9612d1bc97443df | 中国のハッカーがロシア政府を標的に、強化されたRATマルウェアを使用 | bleepingcomputer.com | 2025-04-20 | https://www.bleepingcomputer.com/news/security/chinese-hackers-target-russian-govt-with-upgraded-rat-malware/ | osint-report | TLP:CLEAR | 中 |
| source--ironhusky--05274cec15ba464e | Modern Asian APT groups TTPs report eng |  | 不明 | summary/2023/Modern-Asian-APT-groups-TTPs_report_eng.pdf | report | TLP:CLEAR | 中 |
| source--ironhusky--17a5734d667d6538 | ironhusky |  | 不明 | actor_profile/evidence/ironhusky.csv | structured-data | TLP:CLEAR | 中 |
| source--ironhusky--37b1eb7ac640a809 | 2021 Advanced Threat Trends Research Report dbappsecurity |  | 2021 | summary/2022/2021 Advanced Threat Trends Research Report-dbappsecurity.pdf | report | TLP:CLEAR | 中 |
| source--ironhusky--680537e8bf8b4058 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--ironhusky--a5bfad247a36ff1c | kaspersky ics cert apt attacks on industrial organizations in h2 2022 en |  | 2022 | summary/2023/kaspersky-ics-cert-apt-attacks-on-industrial-organizations-in-h2-2022-en.pdf | report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
