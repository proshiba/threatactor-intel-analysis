# Candiru 脅威アクタープロファイル

- プロファイルID: `actor--candiru`
- 状態: draft
- 更新日時: 2026-11-15T09:02:08Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

Candiruの標準化プロファイル。リポジトリ内の専用資料3件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Candiru**
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
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Caramel Tsunami | canonical-name | 高 |  | https://decoded.avast.io/threatresearch/avast-q2-2022-threat-report/<br>https://decoded.avast.io/janvojtesek/the-return-of-candiru-zero-days-in-the-middle-east/<br>https://citizenlab.ca/2022/04/catalangate-extensive-mercenary-spyware-operation-against-catalans-using-pegasus-candiru/ |
| misp-microsoft-activity-group | Caramel Tsunami | canonical-name | 高 | IL | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | 一致なし |  |  |  |  |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | 一致なし |  |  |  |  |

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
| 標的型広告の表示だけでCandiruスパイウェアに感染するゼロクリック攻撃 | cyber-espionage | 2024 | 2025 | 2026-10-17 | target--activity-rule--sector--5403aec9c83d6a925f61, target--activity-rule--sector--d406c8e5b7fa7aeff7d2 |  |  | victim--activity-rule--f59d8cd27581f6f4e91f | Citizen Labは、Al Jazeeraの端末に標的型広告経由でCandiruスパイウェアを感染させた「AdFection」を確認した。広告をクリックする必要はなく、端末上に表示されるだけで攻撃が進行する。 イスラエル企業Discover-Techは、主要な広告ネットワークで配信枠を購入し、広告にJavaScriptを埋め込んだ。接続元IPや広告識別子などで標的を選別し、対象端末にだけ追加コードを返していた。 Al Jazeeraが提供した証拠には、2024～2025年に少なくとも45台を標的とした攻撃が含まれる。通信ログでは広告基盤からCandiruの検証サーバー、続いてC2への接続が確認された。 侵害されたWindows端末から回収したDLLは、既知検体とのコードやインフラの共通点から、高い確信度でCandiruに帰属された。同社の監視ツールは過去にも記者や活動家らへの攻撃に使われている。 2026年3～6月の広告入札は37.7億件、落札は4.42億件に上り、関連スクリプト付き広告は75,373のアプリと120,768のサイトに掲載された。ただし、これらは感染件数を示さない。 | 高 | `source--daily-ab07ef22a949312f9e64` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| 標的型広告の表示だけでCandiruスパイウェアに感染するゼロクリック攻撃 | Candiru | 情報なし | 情報なし | 情報なし | メディア・報道, 非営利・市民社会 | 被害事例: 標的型広告の表示だけでCandiruスパイウェアに感染するゼロクリック攻撃 | 高 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | メディア・報道 | 活動「標的型広告の表示だけでCandiruスパイウェアに感染するゼロクリック攻撃」の記述で標的として明示された産業。 | 2024 | 2025 | 中 | `source--daily-ab07ef22a949312f9e64` |
| sectors | 非営利・市民社会 | 活動「標的型広告の表示だけでCandiruスパイウェアに感染するゼロクリック攻撃」の記述で標的として明示された産業。 | 2024 | 2025 | 中 | `source--daily-ab07ef22a949312f9e64` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 標的型広告の表示だけでCandiruスパイウェアに感染するゼロクリック攻撃 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--5403aec9c83d6a925f61, target--activity-rule--sector--d406c8e5b7fa7aeff7d2 |  |  | サーバー, エンドポイント |  | 2024 | 2025 | 2026-10-17 | 高 | `source--daily-ab07ef22a949312f9e64` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution | T1203 | Exploitation for Client Execution | velopment: Acquire Infrastructure: Server T1583.004 Initial Access : Spearphishing Link T1566.002 Execution: Exploitation for Client Execution T1203 26 CTA20250805 Recorded Future ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--candiru--80a5eb8801038e0a` |
| Initial Access | T1566.002 | Spearphishing Link | structure: Virtual Private Server T1583.003 Resource Development: Acquire Infrastructure: Server T1583.004 Initial Access : Spearphishing Link T1566.002 Execution: Exploitation for Client Execution T1203 26 CTA20250805 Recorded Future ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--candiru--80a5eb8801038e0a` |
| Resource Development | T1583.001 | Domains | THREAT ANALYSIS Appendix B — MITRE ATT&CK Techniques Tactic: Technique ATT&CK Code Resource Development: Acquire Infrastructure: Domains T1583.001 Resource Development: Acquire Infrastructure: Virtual Private Server T1583.003 Resource Development: Acquire Infrastructure: Server T1583.004 Initial Access : Spearphishing Link T1566.002 Execution: Exploitation for Client Execution T1203 |  |  | 不明 | 不明 | 中 | `source--candiru--80a5eb8801038e0a` |
| Resource Development | T1583.003 | Virtual Private Server | T&CK Code Resource Development: Acquire Infrastructure: Domains T1583.001 Resource Development: Acquire Infrastructure: Virtual Private Server T1583.003 Resource Development: Acquire Infrastructure: Server T1583.004 Initial Access : Spearphishing Link T1566.002 Execution: Exploitation for Client Execution T1203 26 CTA20250805 Record |  |  | 不明 | 不明 | 中 | `source--candiru--80a5eb8801038e0a` |
| Resource Development | T1583.004 | Server | T1583.001 Resource Development: Acquire Infrastructure: Virtual Private Server T1583.003 Resource Development: Acquire Infrastructure: Server T1583.004 Initial Access : Spearphishing Link T1566.002 Execution: Exploitation for Client Execution T1203 26 CTA20250805 Recorded Future ® \| www.recordedfuture.com |  |  | 不明 | 不明 | 中 | `source--candiru--80a5eb8801038e0a` |

## IOC／artifact概要

- IOC値: 228件
- IOC観測: 344件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 2件（`artifacts.csv`）

## 主要判断と不確実性

主要判断なし

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.
- Motivation lead 'commercial' is not canonical; only aggregation/workbook evidence is available.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--candiru--230b73087475fed0 | Candiru product |  | 不明 | Candiru/Candiru_product.pdf | report | TLP:CLEAR | 中 |
| source--candiru--806053148fe55022 | README |  | 不明 | Candiru/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--candiru--80a5eb8801038e0a | Tracking Candiru’s DevilsTongue Spyware in Multiple Countries |  | 不明 | Candiru/Tracking Candiru’s DevilsTongue Spyware in Multiple Countries.pdf | report | TLP:CLEAR | 中 |
| source--daily-ab07ef22a949312f9e64 | 標的型広告の表示だけでCandiruスパイウェアに感染するゼロクリック攻撃 | citizenlab.ca | 2026-10-17 | https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/ | osint-report | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
