# UNC4899 脅威アクタープロファイル

- プロファイルID: `actor--unc4899`
- 状態: review
- 更新日時: 2026-09-23T12:16:55Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

UNC4899の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC4899**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| TraderTraitor | SentinelLabs | overlapping | 中 | `source--sentinellabs-tradertraitor-2026-09` | SentinelLabs が本報告の冒頭で "the financially motivated DPRK state-sponsored Lazarus subgroup TraderTraitor (aka UNC4899, PUKCHONG, Jade Sleet)" と記載している。単一ベンダーによる呼称の並記であり、ベンダークラスタ境界を原典で確認できていないため scope は exact へ昇格させず overlapping とする。 |
| PUKCHONG | SentinelLabs | overlapping | 中 | `source--sentinellabs-tradertraitor-2026-09` | SentinelLabs が本報告の冒頭で "the financially motivated DPRK state-sponsored Lazarus subgroup TraderTraitor (aka UNC4899, PUKCHONG, Jade Sleet)" と記載している。単一ベンダーによる呼称の並記であり、ベンダークラスタ境界を原典で確認できていないため scope は exact へ昇格させず overlapping とする。 |
| Jade Sleet | SentinelLabs | overlapping | 中 | `source--sentinellabs-tradertraitor-2026-09` | SentinelLabs が本報告の冒頭で "the financially motivated DPRK state-sponsored Lazarus subgroup TraderTraitor (aka UNC4899, PUKCHONG, Jade Sleet)" と記載している。単一ベンダーによる呼称の並記であり、ベンダークラスタ境界を原典で確認できていないため scope は exact へ昇格させず overlapping とする。 |

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
| etda-threat-group-cards | Lazarus Group, Hidden Cobra, Labyrinth Chollima | canonical-name | 高 | North Korea | https://blog.malwarebytes.com/threat-analysis/2019/03/the-advanced-persistent-threat-files-lazarus-group/<br>https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/a-look-into-the-lazarus-groups-operations<br>https://www.kaspersky.com/about/press-releases/2017_chasing-lazarus-a-hunt-for-the-infamous-hackers-to-prevent-large-bank-robberies |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Jade Sleet | single-alias-intersection | 中 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | TraderTraitor | canonical-name | 高 | KP | https://www.mandiant.com/resources/blog/north-korea-supply-chain<br>https://us-cert.cisa.gov/ncas/alerts/aa22-108a<br>https://www.mandiant.com/resources/blog/north-korea-cyber-structure-alignment-2023 |
| misp-microsoft-activity-group | Jade Sleet | single-alias-intersection | 中 | KP, North Korea | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Lazarus Group | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--flatroof | FLATROOF | ARM64 の Rust 製 macOS バックドア。"SystemUpdate" として配置され、ブラウザーデータ、ターミナル履歴、プロセス一覧、システムプロファイルを収集し Telegram 経由で外部送信する。次段ペイロードに対して Gatekeeper の検証を抑止する。SentinelLabs が以前 macOS.Gaslight として報告した実装と同一である。 | 2026-03-18 | 2026-04-20 | 中 | `source--sentinellabs-tradertraitor-2026-09` |
| malware--roofdeck | ROOFDECK | ARM64 の Rust 製 macOS バックドア。C2 の探索に Nostr リレーネットワークを用いる。シェル実行、ファイル操作、LaunchAgents による永続化に対応し、埋め込んだ RSA 公開鍵でコマンドの署名を検証する。 | 2026-03-29 | 2026-06-01 | 中 | `source--sentinellabs-tradertraitor-2026-09` |

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
| 北朝鮮のハッカー、洗練されたフィッシング戦術でブラジルのフィンテックを標的に | phishing-campaign | 不明 | 不明 | 2024-06-15 | target--targeting-audit--country--3d2cc0a2a96320ae86c4 |  |  | victim--activity-rule--52b83d60644538555152 | 北朝鮮のハッカーが、ブラジルのフィンテック企業を標的に洗練されたフィッシング攻撃を実行。 UNC4899（Jade Sleet）がPythonアプリをトロイの木馬化し、SNSで標的に接触し、GitHubプロジェクトを通じてマルウェアを配布。 有名な暗号通貨企業を装う求人でフィッシング。無害なPDFが添付されている。ターゲットが求人に反応したら追加のPDFを送る。 PDFで、スキルに関するアンケートと、GitHubからプロジェクトをダウンロードして、コーディング課題を完了するように要求。このプロジェクトにマルウェアが仕込まれている。 他の北朝鮮グループも同様の手法を使用し、フィッシングメールで悪意のあるソフトウェアを配信。 | 中 | `source--daily-eba291a90b11ea99ea6e` |
| 北朝鮮系ハッカーグループ「Slow Pisces」、暗号通貨開発者を標的にしたPythonマルウェア攻撃を展開 | infrastructure-operation | 不明 | 不明 | 2025-04-16 | target--activity-rule--country--f0d8df51439c4d0f3a05, target--activity-rule--sector--932f4928d5e1ec28e2df |  | ttp--activity-rule--5287d9830bb2ca5ae994 | victim--activity-rule--a255592b2e5fc1bdeb05 | 北朝鮮と関連があるとされるハッカーグループ「Slow Pisces」（別名：Jade Sleet、PUKCHONG、TraderTraitor、UNC4899）は、暗号通貨開発者を標的にしたマルウェアキャンペーンを実施。 LinkedInを通じて開発者に接触し、偽の求人情報やコーディング課題を装ってマルウェアを配布。 被害者は、GitHub上のトロイの木馬化されたPythonプロジェクトをダウンロード・実行するよう誘導され、これにより「RN Loader」および「RN Stealer」と呼ばれるマルウェアに感染。 「RN Stealer」はmacOSシステム上で機密情報（iCloudキーチェーン、SSHキー、AWS/Kubernetes/Google Cloudの設定ファイルなど）を収集。 攻撃は多段階で行われ、C2サーバーは被害者のIPアドレスや地理情報などに基づいてペイロードの配信を制御。 コード実行には、`yaml.load()`や`ejs.render()`などの手法を用いて検出を回避。 | 中 | `source--daily-744b9664f686bf2ed5cd` |
| インドのITサービス事業者に対する TraderTraitor の macOS バックドア侵害 (2026年3月〜6月) | intrusion | 2026-03-18 | 2026-06-01 | 2026-09-18 | target--targeting-audit--country--a5e16727ee50a3229e2f | malware--flatroof, malware--roofdeck | ttp--activity-rule--27317de8fad143103d24 | victim--activity-rule--02cdbdef3e6b8d3a8be3 | SentinelOne は、2026年4月に公表された LayerZero に対する TraderTraitor の攻撃と同じ macOS バックドアを用いた別の被害組織を特定した。原文は被害組織を "an IT services provider based in India and unaffiliated with cryptocurrency" と記載し、暗号資産と無関係の組織が標的となった点を本報告の主眼としている。2026-03-18 に FLATROOF がディスク上に存在し、2026-03-25〜03-28 の休止期間を経て 2026-03-29 05:00:41 UTC 以降に初回実行と C2 接続が発生した。2026-04-13 に GitHub リポジトリがクローンされ、2026-04-20 に第3段階が配備されて当初のインプラントが削除された。最後の C2 ビーコンは 2026-06-01、検体のゴミ箱移動は 2026-06-17 に観測された。FLATROOF は Telegram を、ROOFDECK は Nostr リレーネットワークを C2 の探索・通信に用いる。 | 中 | `source--sentinellabs-tradertraitor-2026-09` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| 北朝鮮のハッカー、洗練されたフィッシング戦術でブラジルのフィンテックを標的に | UNC4899 | 情報なし | 情報なし | 情報なし | ブラジル | 被害事例: 北朝鮮のハッカー、洗練されたフィッシング戦術でブラジルのフィンテックを標的に | 中 |
| 北朝鮮系ハッカーグループ「Slow Pisces」、暗号通貨開発者を標的にしたPythonマルウェア攻撃を展開 | UNC4899 | 情報なし | T1083 File and Directory Discovery | 情報なし | 北朝鮮, IT・ソフトウェア | 被害事例: 北朝鮮系ハッカーグループ「Slow Pisces」、暗号通貨開発者を標的にしたPythonマルウェア攻撃を展開 | 中 |
| インドのITサービス事業者に対する TraderTraitor の macOS バックドア侵害 (2026年3月〜6月) | UNC4899 | FLATROOF, ROOFDECK | T1102.003 One-Way Communication | 情報なし | インド | 被害事例: インドのITサービス事業者に対する TraderTraitor の macOS バックドア侵害 (2026年3月〜6月) | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | インド | 活動「インドのITサービス事業者に対する TraderTraitor の macOS バックドア侵害 (2026年3月〜6月)」の記述で標的・被害国として明示されている。 | 2026-03-18 | 2026-06-01 | 中 | `source--sentinellabs-tradertraitor-2026-09` |
| countries | ブラジル | 活動「北朝鮮のハッカー、洗練されたフィッシング戦術でブラジルのフィンテックを標的に」の記述で標的・被害国として明示されている。 | 不明 | 不明 | 中 | `source--daily-eba291a90b11ea99ea6e` |
| countries | 北朝鮮 | 活動「北朝鮮系ハッカーグループ「Slow Pisces」、暗号通貨開発者を標的にしたPythonマルウェア攻撃を展開」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-744b9664f686bf2ed5cd` |
| sectors | IT・ソフトウェア | 活動「北朝鮮系ハッカーグループ「Slow Pisces」、暗号通貨開発者を標的にしたPythonマルウェア攻撃を展開」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-744b9664f686bf2ed5cd` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: インドのITサービス事業者に対する TraderTraitor の macOS バックドア侵害 (2026年3月〜6月) | 非公開 | aggregate | multiple-organizations | reported |  | malware--flatroof, malware--roofdeck | ttp--activity-rule--27317de8fad143103d24 | 開発環境／ソースコード |  | 2026-03-18 | 2026-06-01 | 2026-09-18 | 中 | `source--sentinellabs-tradertraitor-2026-09` |
| 被害事例: 北朝鮮のハッカー、洗練されたフィッシング戦術でブラジルのフィンテックを標的に | 非公開 | aggregate | multiple-organizations | reported |  |  |  | メール／メールアカウント, 開発環境／ソースコード |  | 不明 | 不明 | 2024-06-15 | 中 | `source--daily-eba291a90b11ea99ea6e` |
| 被害事例: 北朝鮮系ハッカーグループ「Slow Pisces」、暗号通貨開発者を標的にしたPythonマルウェア攻撃を展開 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--f0d8df51439c4d0f3a05, target--activity-rule--sector--932f4928d5e1ec28e2df |  | ttp--activity-rule--5287d9830bb2ca5ae994 | サーバー, クラウド／SaaS, 開発環境／ソースコード |  | 不明 | 不明 | 2025-04-16 | 中 | `source--daily-744b9664f686bf2ed5cd` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1102.003 | One-Way Communication | FLATROOF は Telegram を、ROOFDECK は Nostr リレーネットワークを C2 の探索・通信に用いる。 | malware--flatroof, malware--roofdeck | activity--unc4899-tradertraitor-india-it-services-2026 | 2026-03-18 | 2026-06-01 | 中 | `source--sentinellabs-tradertraitor-2026-09` |
| Discovery | T1083 | File and Directory Discovery | 「RN Stealer」はmacOSシステム上で機密情報（iCloudキーチェーン、SSHキー、AWS/Kubernetes/Google Cloudの設定ファイルなど）を収集。 |  | activity--daily-db38d43f17473660e294 | 不明 | 不明 | 中 | `source--daily-744b9664f686bf2ed5cd` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

## 主要判断と不確実性

主要判断なし

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.
- SentinelLabs は TraderTraitor を "DPRK state-sponsored Lazarus subgroup" と記述するが、本リポジトリの規約では国家支援の確定には政府共同勧告・公式帰属・ATT&CK の actor-specific な明示記述または複数の独立した高品質資料を要する。単一ベンダー報告であるため attribution と sponsor_type は unknown のまま据え置き、主張のみを記録する。
- TraderTraitor / PUKCHONG / Jade Sleet と UNC4899 の同一性は SentinelLabs の "aka" 記載に基づく。ベンダークラスタの境界を原典で確認できていないため alias scope は overlapping とし、exact identity へ昇格させない。
- Lazarus との組織関係(subgroup)も同じ単一ベンダー記述に依存するため、relationships へは追加せず未解決事項として保持する。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--daily-744b9664f686bf2ed5cd | 北朝鮮系ハッカーグループ「Slow Pisces」、暗号通貨開発者を標的にしたPythonマルウェア攻撃を展開 | thehackernews.com | 2025-04-16 | https://thehackernews.com/2025/04/crypto-developers-targeted-by-python.html | osint-report | TLP:CLEAR | 中 |
| source--daily-eba291a90b11ea99ea6e | 北朝鮮のハッカー、洗練されたフィッシング戦術でブラジルのフィンテックを標的に | thehackernews.com | 2024-06-15 | https://thehackernews.com/2024/06/north-korean-hackers-target-brazilian.html | osint-report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unc4899--028ff7267b0d9392 | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | International Strategic/Korea/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--unc4899--0ff0d325de512842 | 2024 Blockchain Security and AML Annual Report(EN) |  | 2024 | summary/2025/2024-Blockchain-Security-and-AML-Annual-Report(EN).pdf | report | TLP:CLEAR | 中 |
| source--unc4899--1390332551d8c3af | advances in threat actor usage of ai tools en |  | 不明 | AISecurity/2025/advances-in-threat-actor-usage-of-ai-tools-en.pdf | report | TLP:CLEAR | 中 |
| source--unc4899--2246c521b1b228d1 | unc4899 |  | 不明 | actor_profile/evidence/unc4899.csv | structured-data | TLP:CLEAR | 中 |
| source--unc4899--3e59f7f25cb2d69e | The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities |  | 不明 | International Strategic/Korea/The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities.pdf | report | TLP:CLEAR | 中 |
| source--unc4899--49cddfde804b2b45 | 2025 Blockchain Security and AML Annual Report |  | 2025 | summary/2025/2025-Blockchain-Security-and-AML-Annual-Report.pdf | report | TLP:CLEAR | 中 |
| source--unc4899--79cdef4e25eb8cd8 | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--unc4899--b5b8dda7301c9303 | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | CyberMerceNary/ITWorker/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--unc4899--d91b559d4a2e0f1b | cybercrime multifaceted national security threat |  | 不明 | summary/2025/cybercrime-multifaceted-national-security-threat.pdf | report | TLP:CLEAR | 中 |
| source--unc4899--e1520dd17d1e4dfd | Qianxin 2023 APT Report |  | 2023 | summary/2024/Qianxin 2023 APT Report.pdf | report | TLP:CLEAR | 中 |
| source--sentinellabs-tradertraitor-2026-09 | Don't Call Us, We'll Call Your APIs \| TraderTraitor Backdoors Resurface on Victim With No Crypto Ties | SentinelLabs (SentinelOne) | 2026-09-18 | https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/ | vendor-research | TLP:CLEAR | 高 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
