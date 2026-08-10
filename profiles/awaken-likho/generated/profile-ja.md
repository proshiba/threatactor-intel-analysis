# Awaken Likho 脅威アクタープロファイル

- プロファイルID: `actor--awaken-likho`
- 状態: draft
- 更新日時: 2026-08-10T07:33:16Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Awaken Likho(別称 Core Werewolf)は、2021年からロシアおよびベラルーシの政府機関、政府請負業者、産業企業を標的とするAPTグループである。長らく正規の遠隔管理ソフトを流用してきたが、2026年に独自バックドアTokenBuoy/TokenBuoySHの運用へ移行した。

## アクター名とAlias

- 正規名: **Awaken Likho**
- 初回観測: 2021-07
- 最終観測: 2026-07
- 活動状態: yes

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Core Werewolf |  | overlapping | 中 | `source--kaspersky-awaken-likho-2024` | Kasperskyが「also named by other vendors as Core Werewolf」と記載している。命名元ベンダーの原典を確認できていないためexactへ強めない。 |

## 帰属

一次資料は帰属国もスポンサーも示していない。標的がロシア・ベラルーシであることから攻撃元国を推定しない。

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: `source--kaspersky-awaken-likho-2024`, `source--kaspersky-awaken-likho-tokenbuoy-2026`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | 政府機関と産業企業への継続的な遠隔アクセスとデータ持ち出しを目的とする。 | 中 | `source--kaspersky-awaken-likho-2024`, `source--kaspersky-awaken-likho-tokenbuoy-2026` |  |

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | ロシア・ベラルーシの政府機関等を標的とするAPTグループAwaken Likho。帰属国は不明。 |
| Capability | 独自バックドアTokenBuoy/TokenBuoySH、正規遠隔管理ソフトUltraVNC・MeshCentral(MeshAgent)の流用、Rcloneによる持ち出し。 |
| Infrastructure | フィッシング配信基盤と攻撃者運用のMeshCentralサーバー。 |
| Victim | ロシアおよびベラルーシの政府組織、政府請負業者、産業企業。 |
| Socio-political | ロシア・ベラルーシの政府機能を対象とする継続的な諜報活動。 |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-08-10T07:33:16Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Awaken Likho | canonical-name | 高 |  | https://securelist.com/awaken-likho-apt-new-implant-campaign/114101/<br>https://bi.zone/eng/expertise/blog/core-werewolf-protiv-opk-i-kriticheskoy-infrastruktury/<br>https://bi.zone/eng/expertise/blog/ne-budi-likho-core-werewolf-sovershenstvuet-ataki-na-rossiyskie-gosorganizatsii/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Awaken Likho | canonical-name | 高 |  | https://securelist.com/awaken-likho-apt-new-implant-campaign/114101/<br>https://bi.zone/eng/expertise/blog/core-werewolf-protiv-opk-i-kriticheskoy-infrastruktury/ |
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
| malware--tokenbuoy | TokenBuoy | C++で実装された約1MBの独自バックドア。2026年の活動から投入された。 | 2026-01 | 不明 | 高 | `source--kaspersky-awaken-likho-tokenbuoy-2026` |
| malware--tokenbuoysh | TokenBuoySH | OpenSSHを統合したTokenBuoyの派生。サイズが約10倍になり、二次ペイロードとして展開される。 | 2026-01 | 不明 | 高 | `source--kaspersky-awaken-likho-tokenbuoy-2026` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--ultravnc | UltraVNC | 初期の活動で遠隔操作に流用していた正規の遠隔管理ソフト。 | 不明 | 不明 | 高 | `source--kaspersky-awaken-likho-2024` |
| tool--meshcentral-meshagent | MeshCentral / MeshAgent | オープンソースの遠隔デバイス管理基盤とそのエージェント。2024年の活動でUltraVNCから切り替えられた。 | 2024-06 | 不明 | 高 | `source--kaspersky-awaken-likho-2024` |
| tool--rclone | Rclone | 2026年の活動でデータ持ち出しに使用される正規のクラウド同期ツール。 | 不明 | 不明 | 高 | `source--kaspersky-awaken-likho-tokenbuoy-2026` |

### インフラ

未確認

### 配送・ファイル形式

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| delivery--sfx-archive | 自己展開書庫(SFX) | 難読化コマンドスクリプトと正規Windowsコンポーネントを装った実行ファイルを含む自己展開書庫。2026年の活動では7-Zip SFXが使用されている。 | 不明 | 不明 | 高 | `source--kaspersky-awaken-likho-2024`, `source--kaspersky-awaken-likho-tokenbuoy-2026` |
| delivery--malicious-rar | 悪性RARアーカイブ | 2026年の活動でフィッシングメールに添付される。 | 不明 | 不明 | 高 | `source--kaspersky-awaken-likho-tokenbuoy-2026` |

### 脆弱性

未確認

### 運用能力

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| opcap--living-off-legitimate-rmm | 正規遠隔管理ソフトの流用 | UltraVNCやMeshCentralなど正規の遠隔管理基盤を流用し、検知回避と運用簡素化を図る。 | 不明 | 不明 | 高 | `source--kaspersky-awaken-likho-2024` |
| opcap--custom-backdoor-development | 独自バックドアの内製化 | 2026年に正規ソフト流用から独自バックドアの開発・運用へ移行した。 | 不明 | 不明 | 高 | `source--kaspersky-awaken-likho-tokenbuoy-2026` |

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MeshAgentを用いたロシア政府機関・産業企業への遠隔操作キャンペーン | espionage | 2024-06 | 2024-08 | 2024-10-07 | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--dfc80b76cad93a318adc, target--awaken-likho--country--russia |  | ttp--activity-rule--00a1028961658cc699e8, ttp--activity-rule--57707f4efc5babf267b5, ttp--activity-rule--7fb90d3f61cc773bf69f, ttp--awaken-likho-t1053-005-scheduled-task, ttp--awaken-likho-t1204-002-sfx, ttp--awaken-likho-t1219-remote-tools | victim--activity-rule--1095b6e3f9313b47df2d, victim--awaken-likho-russian-government-2024 | Kasperskyは、Awaken Likhoが遠隔操作手段をUltraVNCからMeshCentralのエージェントMeshAgentへ切り替えたキャンペーンを報告した。被害者はフィッシングメール経由とみられる悪性URLを受け取り、自己展開書庫(SFX)が難読化コマンドスクリプトと正規Windowsコンポーネントを装った実行ファイルを展開する。永続化はMeshAgentを起動するスケジュールタスクで行い、攻撃者のMeshCentralサーバーへの継続接続を維持する。標的はロシアの政府機関、その請負業者、産業企業である。 | 高 | `source--kaspersky-awaken-likho-2024` |
| 独自バックドアTokenBuoy/TokenBuoySHへの移行とロシア・ベラルーシ政府機関攻撃 | espionage | 2026-01 | 2026-07 | 2026-08-07 | target--activity-rule--sector--210dddb39397dbe50e91, target--awaken-likho--country--russia | malware--tokenbuoy, malware--tokenbuoysh | ttp--activity-rule--66d044943eb633757eaf, ttp--awaken-likho-t1204-002-sfx, ttp--awaken-likho-t1566-001-rar, ttp--awaken-likho-t1567-002-rclone | victim--activity-rule--0dd4c80ea2dbdcd07971, victim--awaken-likho-russia-belarus-2026 | Kasperskyは、Awaken Likhoが正規ソフトウェアの流用から独自バックドアの開発へ移行したと報告した。2026年に入り、C++で実装された約1MBのTokenBuoyと、OpenSSHを統合してサイズが約10倍になったTokenBuoySHを投入している。攻撃連鎖はフィッシングメールの悪性RARアーカイブから7-Zip自己展開書庫を経てTokenBuoyを配置し、続いてTokenBuoySHを二次ペイロードとして展開、Rcloneでデータを持ち出す。標的はロシアおよびベラルーシの政府組織である。 | 高 | `source--kaspersky-awaken-likho-tokenbuoy-2026` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| MeshAgentを用いたロシア政府機関・産業企業への遠隔操作キャンペーン | Awaken Likho | 情報なし | T1053.005 Scheduled Task, T1027 Obfuscated Files or Information, T1566.002 Spearphishing Link, T1053.005 Scheduled Task, T1204.002 Malicious File, T1219 Remote Access Software | 情報なし | 政府・行政, 製造・産業, ロシア | 被害事例: MeshAgentを用いたロシア政府機関・産業企業への遠隔操作キャンペーン, ロシアの政府機関・請負業者・産業企業(集約) | 高 |
| 独自バックドアTokenBuoy/TokenBuoySHへの移行とロシア・ベラルーシ政府機関攻撃 | Awaken Likho | TokenBuoy, TokenBuoySH | T1560.001 Archive via Utility, T1204.002 Malicious File, T1566.001 Spearphishing Attachment, T1567.002 Exfiltration to Cloud Storage | 情報なし | 政府・行政, ロシア | 被害事例: 独自バックドアTokenBuoy/TokenBuoySHへの移行とロシア・ベラルーシ政府機関攻撃, ロシア・ベラルーシの政府組織(集約) | 高 |

Kasperskyは2021年7月から追跡している。2024年6〜8月のキャンペーンではUltraVNCからMeshAgentへ切り替え、2024年10月に報告された。2026年前半から7月にかけて独自バックドアTokenBuoyとTokenBuoySHを投入し、2026年8月に報告された。

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | ベラルーシ | 2026年資料が標的国として明示している。 | 2026-01 | 2026-07 | 高 | `source--kaspersky-awaken-likho-tokenbuoy-2026` |
| countries | ロシア | 両資料が標的国として明示している。 | 2021-07 | 2026-07 | 高 | `source--kaspersky-awaken-likho-2024`, `source--kaspersky-awaken-likho-tokenbuoy-2026` |
| regions | 東欧 | ベラルーシ、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--kaspersky-awaken-likho-2024`, `source--kaspersky-awaken-likho-tokenbuoy-2026` |
| sectors | 政府・行政 | 活動「MeshAgentを用いたロシア政府機関・産業企業への遠隔操作キャンペーン」の記述で標的として明示された産業。 | 2024-06 | 2026-07 | 中 | `source--kaspersky-awaken-likho-2024`, `source--kaspersky-awaken-likho-tokenbuoy-2026` |
| sectors | 製造・産業 | 活動「MeshAgentを用いたロシア政府機関・産業企業への遠隔操作キャンペーン」の記述で標的として明示された産業。 | 2024-06 | 2024-08 | 中 | `source--kaspersky-awaken-likho-2024` |
| sectors | 政府機関 | 両資料が標的分野として明示している。 | 不明 | 不明 | 高 | `source--kaspersky-awaken-likho-2024`, `source--kaspersky-awaken-likho-tokenbuoy-2026` |
| sectors | 政府請負業者 | 2024年資料が標的分野として明示している。 | 不明 | 不明 | 高 | `source--kaspersky-awaken-likho-2024` |
| sectors | 産業企業 | 2024年資料が標的分野として明示している。 | 不明 | 不明 | 高 | `source--kaspersky-awaken-likho-2024` |

選定ロジック: ロシアおよびベラルーシの政府機能とその周辺(請負業者、産業企業)を継続的に選定している。 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 独自バックドアTokenBuoy/TokenBuoySHへの移行とロシア・ベラルーシ政府機関攻撃 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--210dddb39397dbe50e91, target--awaken-likho--country--russia | malware--tokenbuoy, malware--tokenbuoysh | ttp--activity-rule--66d044943eb633757eaf, ttp--awaken-likho-t1204-002-sfx, ttp--awaken-likho-t1566-001-rar, ttp--awaken-likho-t1567-002-rclone | メール／メールアカウント |  | 2026-01 | 2026-07 | 2026-08-07 | 高 | `source--kaspersky-awaken-likho-tokenbuoy-2026` |
| 被害事例: MeshAgentを用いたロシア政府機関・産業企業への遠隔操作キャンペーン | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--dfc80b76cad93a318adc, target--awaken-likho--country--russia |  | ttp--activity-rule--00a1028961658cc699e8, ttp--activity-rule--57707f4efc5babf267b5, ttp--activity-rule--7fb90d3f61cc773bf69f, ttp--awaken-likho-t1053-005-scheduled-task, ttp--awaken-likho-t1204-002-sfx, ttp--awaken-likho-t1219-remote-tools | メール／メールアカウント, サーバー |  | 2024-06 | 2024-08 | 2024-10-07 | 高 | `source--kaspersky-awaken-likho-2024` |
| ロシア・ベラルーシの政府組織(集約) | 非公開 | aggregate | multiple-organizations | reported |  | malware--tokenbuoy, malware--tokenbuoysh | ttp--awaken-likho-t1566-001-rar, ttp--awaken-likho-t1567-002-rclone | Windows端末 | espionage: 独自バックドアによる継続的なアクセス。<br>data-theft: Rcloneによるデータ持ち出し。 | 2026-01 | 2026-07 | 2026-08-07 | 高 | `source--kaspersky-awaken-likho-tokenbuoy-2026` |
| ロシアの政府機関・請負業者・産業企業(集約) | 非公開 | aggregate | multiple-organizations | reported |  |  | ttp--awaken-likho-t1219-remote-tools, ttp--awaken-likho-t1053-005-scheduled-task | Windows端末 | espionage: MeshAgentによる遠隔操作を通じた継続的なアクセス。 | 2024-06 | 2024-08 | 2024-10-07 | 高 | `source--kaspersky-awaken-likho-2024` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | 永続化はMeshAgentを起動するスケジュールタスクで行い、攻撃者のMeshCentralサーバーへの継続接続を維持する。 |  | activity--awaken-likho-meshagent-2024 | 2024-06 | 2024-08 | 中 | `source--kaspersky-awaken-likho-2024` |
| Stealth | T1027 | Obfuscated Files or Information | 被害者はフィッシングメール経由とみられる悪性URLを受け取り、自己展開書庫(SFX)が難読化コマンドスクリプトと正規Windowsコンポーネントを装った実行ファイルを展開する。 |  | activity--awaken-likho-meshagent-2024 | 2024-06 | 2024-08 | 中 | `source--kaspersky-awaken-likho-2024` |
| Collection | T1560.001 | Archive via Utility | 攻撃連鎖はフィッシングメールの悪性RARアーカイブから7-Zip自己展開書庫を経てTokenBuoyを配置し、続いてTokenBuoySHを二次ペイロードとして展開、Rcloneでデータを持ち出す。 | malware--tokenbuoy, malware--tokenbuoysh | activity--awaken-likho-tokenbuoy-2026 | 2026-01 | 2026-07 | 中 | `source--kaspersky-awaken-likho-tokenbuoy-2026` |
| Initial Access | T1566.002 | Spearphishing Link | 被害者はフィッシングメール経由とみられる悪性URLを受け取り、自己展開書庫(SFX)が難読化コマンドスクリプトと正規Windowsコンポーネントを装った実行ファイルを展開する。 |  | activity--awaken-likho-meshagent-2024 | 2024-06 | 2024-08 | 中 | `source--kaspersky-awaken-likho-2024` |
| Persistence | T1053.005 | Scheduled Task | MeshAgentを起動するスケジュールタスクを作成し、MeshCentralサーバーへの継続接続を維持する。 |  | activity--awaken-likho-meshagent-2024 | 2024-06 | 2024-08 | 高 | `source--kaspersky-awaken-likho-2024` |
| Execution | T1204.002 | Malicious File | 自己展開書庫(SFX/7-Zip SFX)を実行させ、難読化スクリプトと正規Windowsコンポーネントを装った実行ファイルを展開する。 |  | activity--awaken-likho-meshagent-2024, activity--awaken-likho-tokenbuoy-2026 | 2024-06 | 2026-07 | 高 | `source--kaspersky-awaken-likho-2024`, `source--kaspersky-awaken-likho-tokenbuoy-2026` |
| Command and Control | T1219 | Remote Access Software | 遠隔操作にUltraVNCを使用していたが、MeshCentralのエージェントMeshAgentへ切り替えた。 |  | activity--awaken-likho-meshagent-2024 | 2024-06 | 2024-08 | 高 | `source--kaspersky-awaken-likho-2024` |
| Initial Access | T1566.001 | Spearphishing Attachment | フィッシングメールに悪性RARアーカイブを添付して配布する。 |  | activity--awaken-likho-tokenbuoy-2026 | 2026-01 | 不明 | 高 | `source--kaspersky-awaken-likho-tokenbuoy-2026` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | Rcloneを用いて窃取データを外部へ持ち出す。 |  | activity--awaken-likho-tokenbuoy-2026 | 2026-01 | 不明 | 高 | `source--kaspersky-awaken-likho-tokenbuoy-2026` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| Awaken Likhoは2021年から2026年まで、ロシア・ベラルーシの政府機能を継続的に標的とするAPTグループである。 | 高 | `source--kaspersky-awaken-likho-2024`, `source--kaspersky-awaken-likho-tokenbuoy-2026` |  |
| 2026年に正規遠隔管理ソフトの流用から独自バックドアの内製化へ運用方針が転換した。 | 高 | `source--kaspersky-awaken-likho-tokenbuoy-2026` |  |

### 情報ギャップ

- Core Werewolfの命名元ベンダーによる一次資料を未取得。
- 2026-07-22付のsecurelist.ru記事(116325)を未確認。次回の収集対象とする。
- 帰属国・スポンサーを示す一次資料が存在しない。
- IOCは本プロファイル作成時点でtech-memoに収録されておらず、未取得である。

### 不確実性

- 2026年キャンペーンの開始時期は資料の「2026年前半」という表現に基づく推定であり、月精度・status: inferredとしている。
- PseudoGamaredonという別称が二次情報に見られるが、原典を確認できていないため登録していない。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--kaspersky-awaken-likho-2024 | Awaken Likho is awake: new techniques of an APT group | Kaspersky (Securelist) | 2024-10-07 | https://securelist.com/awaken-likho-apt-new-implant-campaign/114101/ | vendor-research-report | TLP:CLEAR | 高 |
| source--kaspersky-awaken-likho-tokenbuoy-2026 | Awaken Likho окончательно меняет почерк: переход на собственные бэкдоры TokenBuoy и TokenBuoySH | Kaspersky (Securelist RU) | 2026-08-07 | https://securelist.ru/awaken-likho-tokenbuoy/116536/ | vendor-research-report | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

本プロファイルは2026-08-10の一次情報源確認(securelist.ru)で検知され、利用者承認を経て作成した。status: draftから開始する。
