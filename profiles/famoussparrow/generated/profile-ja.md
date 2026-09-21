# FamousSparrow 脅威アクタープロファイル

- プロファイルID: `actor--famoussparrow`
- 状態: draft
- 更新日時: 2026-09-21T13:20:00Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

FamousSparrowはESETが2021年に命名した中国関連のサイバースパイ活動グループである。2025年8月以降、専有バックドア SparrowDoor から新型の SparroWocky へ移行し、ラテンアメリカの政府機関を集中的に標的としている。

## アクター名とAlias

- 正規名: **FamousSparrow**
- 初回観測: 2019
- 最終観測: 2026
- 活動状態: likely

Aliasなし

## 帰属

ESETは2026-09-17の報告で「FamousSparrow is a China-aligned cyberespionage group believed to have been active since at least 2019.」と述べ、中国関連のサイバースパイ活動グループと評価する。最新キャンペーンとSparroWockyバックドアのFamousSparrowへの帰属は「we attribute the latest campaign and the SparroWocky backdoor to FamousSparrow with high confidence」として高確度で行われ、根拠は(1)SparroWockyを用いた初期の攻撃の一部で、FamousSparrow専用のSparrowDoorによって展開されていたこと、(2)被害者像が従来の標的と一致すること、(3)以前SparrowDoorで標的とされた同一組織群への展開試行が記録されていること、の3点である。ESETはラテンアメリカへの標的集中について「likely reflects China's reaction to various recent US initiatives in the region」と地政学的な解釈を示すが、支援組織や指揮系統は名指ししていない。

- 国: China
- スポンサー種別: state-aligned
- 確度: 中
- 証拠: `source--eset-famoussparrow-sparrowocky-2026`, `source--eset-famoussparrow-2021`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | 政府機関、国際機関、業界団体、エンジニアリング企業、法律事務所に対する情報収集。2025年7月以降はラテンアメリカの政府機関に集中しており、ESETは米国の同地域への関与に対する中国の反応を反映した標的選択である可能性が高いと評価する。 | 中 | `source--eset-famoussparrow-sparrowocky-2026`, `source--eset-famoussparrow-2021` | ESETは2021年と2026年の両報告で cyberespionage group と明記している。動機の記述は原文の範囲にとどめ、国家支援の有無から動機を導出していない。 |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Earth Estries | overlaps-with | ESETは2026-09-17の原文で「As mentioned by Trend Micro, FamousSparrow is linked to Earth Estries; however, the exact nature of the link is not fully known.」と述べ、Trend Microが指摘する関連を紹介しつつ、関連の正確な性質は完全には判明していないとする。 | 低 | `source--eset-famoussparrow-sparrowocky-2026` |
| Salt Typhoon | taxonomy-overlaps-with | 公開情報ではFamousSparrowはSalt Typhoonと結び付けられているが、ESETは「due to the absence of any technical indicators, we track them as separate」として技術指標の不在を理由に別クラスタとして追跡している。 | 低 | `source--eset-famoussparrow-sparrowocky-2026` |

## 関連する企業・個人

関連エンティティなし

### エンティティ関係

確認された関係なし

### 法的措置

確認された法的措置なし

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
- 調査日時: 2026-09-21T02:39:13Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | Salt Typhoon, GhostEmperor | canonical-name | 高 | China | https://securelist.com/ghostemperor-from-proxylogon-to-kernel-mode/104407/<br>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2021/09/30094337/GhostEmperor_technical-details_PDF_eng.pdf<br>https://www.trendmicro.com/en_us/research/24/k/breaking-down-earth-estries-persistent-ttps-in-prolonged-cyber-o.html |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Salt Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | GhostEmperor | canonical-name | 高 | CN | https://securelist.com/ghostemperor-from-proxylogon-to-kernel-mode/104407/<br>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2021/09/30094337/GhostEmperor_technical-details_PDF_eng.pdf<br>https://www.welivesecurity.com/2021/09/23/famoussparrow-suspicious-hotel-guest/ |
| misp-microsoft-activity-group | Salt Typhoon | canonical-name | 高 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Earth Estries | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--daily-0304bc2996ed2600a585 | SparroWocky | FamousSparrowとの直接的な利用関係が一次資料レビューで確認されたマルウェア。 | 2025-08 | 2026-06-17 | 高 | `source--daily-7e7db1cf1c7586215c8d`, `source--daily-8ad4c8f610ba00d8b741` |

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

## C2・マルウェア ハンティング・ピボット

構造化されたハンティング・ピボットなし

### 観測根拠

観測記録なし

### ハントクエリ

クエリなし

### 継続利用チェック

実行済みの受動検索・継続利用チェックなし

`active_status` は明示的なテレメトリまたはスキャン根拠がない限り `unknown` です。出典公開日は観測時刻に転用していません。

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SparroWockに注意：噛みつくバックドアと、捕捉につながるコマンド | cyber-espionage | 2025-08 | 2026-06-17 | 2026-09-18 | target--activity-rule--sector--210dddb39397dbe50e91, target--targeting-audit--country--0241a2eb55502ccf50d4, target--targeting-audit--country--10a5063a82e414b95408, target--targeting-audit--country--2cf29d18337a08e084d8, target--targeting-audit--country--40cd7a37e880686f66ac, target--targeting-audit--country--6a93aca55900d94aefce, target--targeting-audit--country--90eb33789aa52aea1f7e, target--targeting-audit--region--517128e07ed31657f60b | malware--daily-0304bc2996ed2600a585 | ttp--activity-rule--347ae49d2b4abd38cd88, ttp--activity-rule--3eb2cb2b43f6ff5058e1 | victim--activity-rule--1f2ead709658f7c05ba9 | 中国関連APT「FamousSparrow」は2025年7月頃から中南米への攻撃を強化し、2025年8月以降、新型バックドアSparroWockyを主要インプラントとして使用している。 2025年半ばから2026年に観測された標的の90%が中南米にあり、アルゼンチン、エクアドル、グアテマラ、ホンジュラス、パナマ、ペルーなどの政府機関が狙われた。 SparroWockyはC++製のモジュール型バックドアで、コマンド・PE・BOF実行、TCPプロキシ、ファイル操作、情報収集、スクリーンショット、データ窃取を実行できる。 DLLサイドローディング、RC4暗号化、リフレクティブロード、APIハッシュ、SilentMoonwalk、スレッド開始位置偽装など高度な検知・解析回避技術を利用する。 ESETはFamousSparrowが中国関連の諜報活動として、中南米政府が米国からの圧力へどう対応するかを監視・予測する目的で活動している可能性が高いと分析した。 | 高 | `source--daily-7e7db1cf1c7586215c8d`, `source--daily-8ad4c8f610ba00d8b741` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| SparroWockに注意：噛みつくバックドアと、捕捉につながるコマンド | FamousSparrow | SparroWocky | T1083 File and Directory Discovery, T1574.001 DLL | 情報なし | 政府・行政, アルゼンチン, グアテマラ, ホンジュラス, ペルー, エクアドル, パナマ, 中南米 | 被害事例: SparroWockに注意：噛みつくバックドアと、捕捉につながるコマンド | 高 |

2021年9月にESETが初報を公開し、ProxyLogon悪用によるホテル・政府・民間企業への攻撃を記述した。2022年以降は公開報告が途絶え活動停止とみられていたが、2024年7月にESETが米国の金融分野の業界団体で侵害を確認し、2025年3月の報告で未文書化のSparrowDoor 2版を公開した。2025年7月以降は標的をラテンアメリカへ集中させ、2025年8月から SparroWocky の展開を開始した。

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アルゼンチン | 活動「SparroWockに注意：噛みつくバックドアと、捕捉につながるコマンド」の記述で標的・被害国として明示されている。 | 2025-08 | 2026-06-17 | 中 | `source--daily-7e7db1cf1c7586215c8d`, `source--daily-8ad4c8f610ba00d8b741` |
| countries | エクアドル | 活動「SparroWockに注意：噛みつくバックドアと、捕捉につながるコマンド」の記述で標的・被害国として明示されている。 | 2025-08 | 2026-06-17 | 中 | `source--daily-7e7db1cf1c7586215c8d`, `source--daily-8ad4c8f610ba00d8b741` |
| countries | グアテマラ | 活動「SparroWockに注意：噛みつくバックドアと、捕捉につながるコマンド」の記述で標的・被害国として明示されている。 | 2025-08 | 2026-06-17 | 中 | `source--daily-7e7db1cf1c7586215c8d`, `source--daily-8ad4c8f610ba00d8b741` |
| countries | パナマ | 活動「SparroWockに注意：噛みつくバックドアと、捕捉につながるコマンド」の記述で標的・被害国として明示されている。 | 2025-08 | 2026-06-17 | 中 | `source--daily-7e7db1cf1c7586215c8d`, `source--daily-8ad4c8f610ba00d8b741` |
| countries | ベネズエラ | ESETは「we've seen the new backdoor deployed against governmental entities in Argentina, Ecuador, Guatemala, Honduras, Panama, Peru, Puerto Rico, and Venezuela.」として8か国・地域の政府機関を挙げる。 | 不明 | 不明 | 高 | `source--eset-famoussparrow-sparrowocky-2026` |
| countries | ペルー | 活動「SparroWockに注意：噛みつくバックドアと、捕捉につながるコマンド」の記述で標的・被害国として明示されている。 | 2025-08 | 2026-06-17 | 中 | `source--daily-7e7db1cf1c7586215c8d`, `source--daily-8ad4c8f610ba00d8b741` |
| countries | ホンジュラス | 活動「SparroWockに注意：噛みつくバックドアと、捕捉につながるコマンド」の記述で標的・被害国として明示されている。 | 2025-08 | 2026-06-17 | 中 | `source--daily-7e7db1cf1c7586215c8d`, `source--daily-8ad4c8f610ba00d8b741` |
| regions | 中南米 | 活動「SparroWockに注意：噛みつくバックドアと、捕捉につながるコマンド」の記述で標的地域として中南米が明示されている。 | 2025-08 | 2026-06-17 | 中 | `source--daily-7e7db1cf1c7586215c8d`, `source--daily-8ad4c8f610ba00d8b741`, `source--eset-famoussparrow-sparrowocky-2026` |
| regions | 南米 | アルゼンチン、エクアドル、ベネズエラ、ペルーで確認された標的・被害事例を南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-7e7db1cf1c7586215c8d`, `source--daily-8ad4c8f610ba00d8b741`, `source--eset-famoussparrow-sparrowocky-2026` |
| sectors | 政府・行政 | 活動「SparroWockに注意：噛みつくバックドアと、捕捉につながるコマンド」の記述で標的として明示された産業。 | 2025-08 | 2026-06-17 | 中 | `source--daily-7e7db1cf1c7586215c8d`, `source--daily-8ad4c8f610ba00d8b741` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: SparroWockに注意：噛みつくバックドアと、捕捉につながるコマンド | 非公開 | anonymous | unknown | reported | target--activity-rule--sector--210dddb39397dbe50e91 | malware--daily-0304bc2996ed2600a585 | ttp--activity-rule--347ae49d2b4abd38cd88, ttp--activity-rule--3eb2cb2b43f6ff5058e1 |  | data-theft: SparroWockyはC++製のモジュール型バックドアで、コマンド・PE・BOF実行、TCPプロキシ、ファイル操作、情報収集、スクリーンショット、データ窃取を実行できる。<br>espionage: SparroWockyはC++製のモジュール型バックドアで、コマンド・PE・BOF実行、TCPプロキシ、ファイル操作、情報収集、スクリーンショット、データ窃取を実行できる。 | 2025-08 | 2026-06-17 | 2026-09-18 | 高 | `source--daily-7e7db1cf1c7586215c8d`, `source--daily-8ad4c8f610ba00d8b741` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Discovery | T1083 | File and Directory Discovery | SparroWockyはC++製のモジュール型バックドアで、コマンド・PE・BOF実行、TCPプロキシ、ファイル操作、情報収集、スクリーンショット、データ窃取を実行できる。 | malware--daily-0304bc2996ed2600a585 | activity--daily-887e71cb9547566da1dd | 2025-08 | 2026-06-17 | 中 | `source--daily-7e7db1cf1c7586215c8d`, `source--daily-8ad4c8f610ba00d8b741` |
| Execution, Stealth | T1574.001 | DLL | DLLサイドローディング、RC4暗号化、リフレクティブロード、APIハッシュ、SilentMoonwalk、スレッド開始位置偽装など高度な検知・解析回避技術を利用する。 |  | activity--daily-887e71cb9547566da1dd | 2025-08 | 2026-06-17 | 中 | `source--daily-7e7db1cf1c7586215c8d`, `source--daily-8ad4c8f610ba00d8b741` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| ESETはSparroWockyの展開経路(FamousSparrow専用のSparrowDoorによる配布)と被害者像の一致を根拠に、最新キャンペーンを高確度でFamousSparrowへ帰属している。 | 高 | `source--eset-famoussparrow-sparrowocky-2026` | 単一ベンダーによる帰属である。政府・CERTによる帰属は確認していない。 |
| 2025年7月以降、標的がラテンアメリカの政府機関へ集中しており、ESETテレメトリでは2025年半ばから2026年の標的の90%が同地域に所在する。中国関連APTとしては観測地域が限定される点が特異である。 | 中 | `source--eset-famoussparrow-sparrowocky-2026` | 割合はESETの自社テレメトリに基づく値であり、母集団はESETの可視範囲に限られる。 |

### 情報ギャップ

- SparroWockyの初期侵入経路について原文に明示がない。
- 本走査ではESETが公開するIOCリポジトリ(github.com/eset/malware-ioc)の原本を未取得であり、tech-memoのIOC CSV経由の値のみを扱う。

### 不確実性

- Salt Typhoon / GhostEmperor / UNC2286 / Earth Estries との同一性は未解決である。ESETは技術指標の不在を理由にSalt Typhoonとは別クラスタとして追跡し、Earth Estriesとの関連も性質不明としている。一方でMicrosoftの命名マッピングとETDA Threat Group Cardsは同一クラスタの別名として扱う。
- 本プロファイルの作成により、同一の集約クラスタを指し得る famoussparrow / salt-typhoon / unc2286 の3プロファイルが併存する。統合または関係の確定には一次資料が必要である。
- 昇格根拠として確認できた actor-specific な一次資料はESETの3本で、いずれも同一ベンダーである。第三者の一次資料としてはTrend Micro(Earth Estriesとの関連)とBitdefenderのSilkParasite報告(2026-08-19、FamousSparrowとの重複を指摘)があるが、どちらも本走査では原典を未確認であり、ESETおよびHunt.io経由の言及にとどまる。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--daily-7e7db1cf1c7586215c8d | SparroWockに注意：噛みつくバックドアと、捕捉につながるコマンド | welivesecurity.com | 2026-09-18 | https://www.welivesecurity.com/en/eset-research/beware-sparrowock-backdoor-bites-commands-catch/#latin-america-in-the-crosshairs | osint-report | TLP:CLEAR | 中 |
| source--daily-8ad4c8f610ba00d8b741 | SparroWockに注意：噛みつくバックドアと、捕捉につながるコマンド — IOC補助資料 | github.com | 不明 | https://github.com/eset/malware-ioc/tree/master/famoussparrow | osint-report | TLP:CLEAR | 中 |
| source--eset-famoussparrow-2021 | FamousSparrow: A suspicious hotel guest | ESET Research | 2021-09-23 | https://www.welivesecurity.com/2021/09/23/famoussparrow-suspicious-hotel-guest/ | vendor-research | TLP:CLEAR | 高 |
| source--eset-famoussparrow-sparrowdoor-2025 | You will always remember this as the day you finally caught FamousSparrow | ESET Research | 2025-03-26 | https://www.welivesecurity.com/en/eset-research/you-will-always-remember-this-as-the-day-you-finally-caught-famoussparrow/ | vendor-research | TLP:CLEAR | 高 |
| source--eset-famoussparrow-sparrowocky-2026 | Beware the SparroWock: The backdoor that bites, the commands that catch | ESET Research | 2026-09-17 | https://www.welivesecurity.com/en/eset-research/beware-sparrowock-backdoor-bites-commands-catch/ | vendor-research | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

なし
