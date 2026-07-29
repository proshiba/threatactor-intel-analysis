# UNC1549 脅威アクタープロファイル

- プロファイルID: `actor--unc1549`
- 状態: draft
- 更新日時: 2026-07-29T23:13:55Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

UNC1549はイラン系と評価される情報収集クラスタで、KasperskyはMirage Kitten、Smoke Sandstorm、Nimbus Manticoreとして追跡している。2026年7月の報告では、中東・アフリカの航空宇宙、航空、防衛、通信などを対象とする活動と、NightLedger、ArcBridge、BridgeHeadの新規ツールセットが明らかになった。

## アクター名とAlias

- 正規名: **UNC1549**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Mirage Kitten | Kaspersky | exact | 中 | `source--kaspersky-mirage-kitten-2026` | KasperskyはUNC1549の別名として明示している。ベンダーごとの追跡範囲が完全に一致するとは限らないため、確度はmediumとする。 |
| Smoke Sandstorm | Kaspersky | exact | 中 | `source--kaspersky-mirage-kitten-2026` | KasperskyはUNC1549の別名として明示している。ベンダーごとの追跡範囲が完全に一致するとは限らないため、確度はmediumとする。 |
| Nimbus Manticore | Kaspersky | exact | 中 | `source--kaspersky-mirage-kitten-2026` | KasperskyはUNC1549の別名として明示している。ベンダーごとの追跡範囲が完全に一致するとは限らないため、確度はmediumとする。 |

## 帰属

複数資料はUNC1549をイラン系またはイランの情報目的に整合する脅威クラスタとして評価している。

- 国: Iran
- スポンサー種別: state-aligned
- 確度: 中
- 証拠: `source--daily-96ac11961cae303bc9fd`, `source--unc1549--5ad26a22b1f5c730`, `source--unc1549--c47ef662fbdb6d88`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | 航空宇宙、航空、防衛、通信分野を中心とする情報収集。 | 高 | `source--kaspersky-mirage-kitten-2026` | Kasperskyは一連の活動をcyberespionageとして記述している。 |

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | UNC1549（Kaspersky追跡名: Mirage Kitten。別名: Smoke Sandstorm、Nimbus Manticore）。 |
| Capability | NightLedgerバックドア、ArcBridgeおよびBridgeHead WebSocketトンネラー。DLL検索順序ハイジャック、SOCKS5トンネリング、偵察、プロセス実行、ファイル操作、画面取得などを行う。 |
| Infrastructure | HTTPSとWebSocketを用いるC2、Azure App ServiceやCloudflare配下を含むドメイン、標的別に調整したドメインや採用・ビデオ会議を装う誘導基盤。 |
| Victim | 中東・アフリカの航空宇宙、航空、防衛、通信、政府、金融分野。2026年報告ではEgypt、Pakistan、Jordan、Tanzania、Ethiopia、Burkina Fasoの組織が挙げられた。 |
| Socio-political | 情報収集目的のサイバースパイ活動。既存資料ではイランの情報目的やIRGC-CECとの整合性が評価されている。 |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | TA455, Smoke Sandstorm | canonical-name | 高 | Iran | https://www.microsoft.com/en-us/security/security-insider/smoke-sandstorm<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Subgroup%3A+TA455%2C+Smoke+Sandstorm&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Smoke Sandstorm | canonical-name | 高 | Iran | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | UNC1549 | canonical-name | 高 | IR | https://www.mandiant.com/resources/blog/suspected-iranian-unc1549-targets-israel-middle-east<br>https://research.checkpoint.com/2025/nimbus-manticore-deploys-new-malware-targeting-europe<br>https://blog.checkpoint.com/research/iranian-threat-actor-nimbus-manticore-expands-campaigns-into-europe-with-advanced-malware-and-fake-job-lures/ |
| misp-microsoft-activity-group | Smoke Sandstorm | canonical-name | 高 | IR, Iran | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
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
| malware--nightledger | NightLedger | DLL検索順序ハイジャックで実行されるWindowsバックドア。ホスト偵察、プロセス実行・列挙、ファイル操作、画面取得、DLLロード、アップロード、ドライブ列挙などのコマンドを備える。 | 不明 | 不明 | 高 | `source--kaspersky-mirage-kitten-2026` |
| malware--arcbridge | ArcBridge | DNS解決とTCP通信をWebSocket経由で中継するカスタムトンネラー。設定を実行ファイル末尾から読み込み、企業プロキシを考慮した通信を行う。 | 2026-04 | 不明 | 高 | `source--kaspersky-mirage-kitten-2026` |
| malware--bridgehead | BridgeHead | WebSocket上でSOCKS5通信を中継するカスタムトンネラー。レジストリまたは末尾付加設定からC2を読み込み、企業プロキシ経由でも接続する。 | 不明 | 不明 | 高 | `source--kaspersky-mirage-kitten-2026` |

### ツール

未確認

### インフラ

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| infrastructure--mirage-kitten-cloud-c2 | Cloud-hosted HTTPS/WebSocket C2 | Azure App Service、Cloudflare配下のホスト、標的に合わせた名称のドメインを組み合わせ、HTTPSおよびWebSocketでバックドアとトンネラーを制御する。 | 不明 | 不明 | 高 | `source--kaspersky-mirage-kitten-2026`, `source--unc1549--c47ef662fbdb6d88` |

### 配送・ファイル形式

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| delivery--recruitment-videoconference-archive | 採用・ビデオ会議を装うアーカイブ配布 | 採用をテーマにした内容と正規ビデオ会議サービスの類似ページを用い、第三者サービス上の悪性アーカイブへ標的を誘導する。 | 不明 | 不明 | 高 | `source--kaspersky-mirage-kitten-2026` |

### 脆弱性

未確認

### 運用能力

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| capability--per-victim-execution-gating | 標的別の実行制御 | 標的ごとの実行条件を設け、意図した被害環境以外でのペイロード実行を抑制する。 | 不明 | 不明 | 高 | `source--kaspersky-mirage-kitten-2026` |
| capability--proxy-aware-websocket-tunneling | プロキシ対応WebSocketトンネリング | 企業プロキシを検出・利用し、WebSocket上でDNS、TCP、SOCKS5通信を中継する。 | 不明 | 不明 | 高 | `source--kaspersky-mirage-kitten-2026` |

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| イラン系APT「Screening Serpens」の2026年サイバースパイキャンペーンを追跡 | cyber-espionage | 2026-02 | 2026-04 | 2026-05-25 | target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--country--904728608f27c39df0df |  | ttp--activity-rule--58d557d2679ee65b66a5 | victim--activity-rule--071152112a80d6125133 | Unit 42は、イラン系APTのScreening Serpensによる2026年2月〜4月の攻撃活動を観測した。 攻撃は米国、イスラエル、UAE、中東の複数組織を標的にした可能性があり、技術職を狙う採用・会議ルアーが使われた。 同グループはMiniUpdateとMiniJunk V2という2系統のRATを展開し、DLLサイドローディングで感染を開始した。 MiniUpdateではAppDomainManagerハイジャックを使い、.NETのETWや署名検証を無効化して検出回避を強化した。 RATはC2通信、コマンド実行、DLLのメモリ内実行、プロセス操作、ファイル窃取、永続化などの機能を持つ。 | 中 | `source--daily-96ac11961cae303bc9fd` |
| Mirage Kittenによる中東・アフリカの航空宇宙、防衛、通信分野へのサイバースパイ活動 | cyber-espionage | 不明 | 不明 | 2026-07-28 | target--activity-rule--sector--4221b5fbb827488c6eaa, target--country--burkina-faso, target--country--egypt, target--country--ethiopia, target--country--jordan, target--country--pakistan, target--country--tanzania, target--sector--aerospace, target--sector--aviation, target--sector--defense, target--sector--financial-services, target--sector--government, target--sector--telecommunications | malware--nightledger, malware--arcbridge, malware--bridgehead | ttp--activity-rule--543c54c03eee4074488f, ttp--activity-rule--64e01cb31f20cb632f2c, ttp--activity-rule--eee5857560ca39325182, ttp--t1057--nightledger, ttp--t1071-001--mirage-kitten-2026, ttp--t1082--nightledger, ttp--t1090--bridgehead, ttp--t1113--nightledger, ttp--t1566-002--mirage-kitten-2026, ttp--t1574-001--nightledger | victim--activity-rule--15a1bbc4304a95fa57dc | Kasperskyは、Mirage Kitten（UNC1549）が中東・アフリカの航空宇宙、航空、防衛、通信、政府、金融分野を標的にした活動を報告した。EgyptとPakistanでは、採用・ビデオ会議を装う標的型誘導の後、BridgeHeadを侵害後のトンネラーとして展開した。新たに確認されたツールセットはNightLedger、ArcBridge、BridgeHeadで、HTTPS/WebSocket C2、SOCKS5中継、DLL検索順序ハイジャック、偵察、プロセス実行、ファイル操作、画面取得などを行う。 | 高 | `source--kaspersky-mirage-kitten-2026` |

2026年2月〜4月にはUnit 42がScreening Serpens名義の活動を報告した。Kasperskyは2026年4月にArcBridgeを中東の活動から初めて特定し、7月28日にMiddle EastおよびAfricaでのMirage Kitten活動としてNightLedger、ArcBridge、BridgeHeadを公開した。活動全体の開始・終了日は明記されていない。

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アラブ首長国連邦 | 活動「イラン系APT「Screening Serpens」の2026年サイバースパイキャンペーンを追跡」の記述で標的・被害国として明示されている。 | 2026-02 | 2026-04 | 中 | `source--daily-96ac11961cae303bc9fd`, `source--target-audit-etda-threat-group-cards` |
| countries | アルバニア | 構造化OSINTの被害国フィールドでUNC1549の標的・被害国としてアルバニアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イスラエル | 活動「イラン系APT「Screening Serpens」の2026年サイバースパイキャンペーンを追跡」の記述で標的として明示された国・地域。 | 2026-02 | 2026-04 | 中 | `source--daily-96ac11961cae303bc9fd`, `source--target-audit-etda-threat-group-cards` |
| countries | インド | 構造化OSINTの被害国フィールドでUNC1549の標的・被害国としてインドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | エジプト | BridgeHeadを含む侵害後活動が確認された。 | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--kaspersky-mirage-kitten-2026` |
| countries | エチオピア | 通信分野の被害組織が報告された。 | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--kaspersky-mirage-kitten-2026` |
| countries | タンザニア | 中小組織または政府関連組織を含む標的地域として報告された。 | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--kaspersky-mirage-kitten-2026` |
| countries | トルコ | 構造化OSINTの被害国フィールドでUNC1549の標的・被害国としてトルコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | パキスタン | 航空宇宙・航空分野でBridgeHeadを含む侵害後活動が確認された。 | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--kaspersky-mirage-kitten-2026` |
| countries | ブルキナファソ | 金融分野の被害組織が報告された。 | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--kaspersky-mirage-kitten-2026` |
| countries | ヨルダン | 中小組織または政府関連組織を含む標的地域として報告された。 | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--kaspersky-mirage-kitten-2026` |
| countries | 米国 | 活動「イラン系APT「Screening Serpens」の2026年サイバースパイキャンペーンを追跡」の記述で標的として明示された国・地域。 | 2026-02 | 2026-04 | 中 | `source--daily-96ac11961cae303bc9fd` |
| regions | アフリカ | 2026年報告で活動範囲の拡大が確認された地域。 | 不明 | 不明 | 高 | `source--actor-mapping-workbook`, `source--kaspersky-mirage-kitten-2026` |
| regions | 中東 | 継続的な重点標的地域として報告された。 | 2026-02 | 2026-04 | 高 | `source--actor-mapping-workbook`, `source--daily-96ac11961cae303bc9fd`, `source--kaspersky-mirage-kitten-2026`, `source--target-audit-etda-threat-group-cards`, `source--unc1549--c47ef662fbdb6d88` |
| regions | 南アジア | インド、パキスタンで確認された標的・被害事例を南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--kaspersky-mirage-kitten-2026`, `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | アルバニア、トルコで確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| sectors | 金融 | 活動「Mirage Kittenによる中東・アフリカの航空宇宙、防衛、通信分野へのサイバースパイ活動」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--kaspersky-mirage-kitten-2026` |
| sectors | Aerospace | 主要な情報収集標的分野。 | 不明 | 不明 | 高 | `source--kaspersky-mirage-kitten-2026`, `source--unc1549--c47ef662fbdb6d88` |
| sectors | Aviation | 主要な情報収集標的分野。 | 不明 | 不明 | 高 | `source--kaspersky-mirage-kitten-2026`, `source--unc1549--c47ef662fbdb6d88` |
| sectors | Defense | 主要な情報収集標的分野。 | 不明 | 不明 | 高 | `source--kaspersky-mirage-kitten-2026`, `source--unc1549--c47ef662fbdb6d88` |
| sectors | Financial Services | Burkina Fasoの被害例で挙げられた標的分野。 | 不明 | 不明 | 高 | `source--kaspersky-mirage-kitten-2026` |
| sectors | Government | JordanおよびTanzaniaに関する報告で対象組織種別として挙げられた。 | 不明 | 不明 | 高 | `source--kaspersky-mirage-kitten-2026` |
| sectors | Telecommunications | Ethiopiaの被害例を含む標的分野。 | 不明 | 不明 | 高 | `source--kaspersky-mirage-kitten-2026` |

選定ロジック: 航空宇宙、航空、防衛、通信など、国家・産業上の情報価値が高い組織を選び、技術職向けの採用・会議テーマを用いて個別に接触する。 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: イラン系APT「Screening Serpens」の2026年サイバースパイキャンペーンを追跡 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--country--904728608f27c39df0df |  | ttp--activity-rule--58d557d2679ee65b66a5 |  | data-theft: RATはC2通信、コマンド実行、DLLのメモリ内実行、プロセス操作、ファイル窃取、永続化などの機能を持つ。 | 2026-02 | 2026-04 | 2026-05-25 | 中 | `source--daily-96ac11961cae303bc9fd` |
| 被害事例: Mirage Kittenによる中東・アフリカの航空宇宙、防衛、通信分野へのサイバースパイ活動 | 非公開 | anonymous | unknown | reported | target--activity-rule--sector--4221b5fbb827488c6eaa, target--country--burkina-faso, target--country--egypt, target--country--ethiopia, target--country--jordan, target--country--pakistan, target--country--tanzania, target--sector--aerospace, target--sector--aviation, target--sector--defense, target--sector--financial-services, target--sector--government, target--sector--telecommunications | malware--arcbridge, malware--bridgehead, malware--nightledger | ttp--activity-rule--543c54c03eee4074488f, ttp--activity-rule--64e01cb31f20cb632f2c, ttp--activity-rule--eee5857560ca39325182, ttp--t1057--nightledger, ttp--t1071-001--mirage-kitten-2026, ttp--t1082--nightledger, ttp--t1090--bridgehead, ttp--t1113--nightledger, ttp--t1566-002--mirage-kitten-2026, ttp--t1574-001--nightledger |  | espionage: Mirage Kittenによる中東・アフリカの航空宇宙、防衛、通信分野へのサイバースパイ活動 | 不明 | 不明 | 2026-07-28 | 高 | `source--kaspersky-mirage-kitten-2026` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution, Stealth | T1574.001 | DLL | 新たに確認されたツールセットはNightLedger、ArcBridge、BridgeHeadで、HTTPS/WebSocket C2、SOCKS5中継、DLL検索順序ハイジャック、偵察、プロセス実行、ファイル操作、画面取得などを行う。 | malware--arcbridge, malware--bridgehead, malware--nightledger | activity--mirage-kitten-middle-east-africa-2026 | 不明 | 不明 | 中 | `source--kaspersky-mirage-kitten-2026` |
| Execution, Stealth | T1574.001 | DLL | 同グループはMiniUpdateとMiniJunk V2という2系統のRATを展開し、DLLサイドローディングで感染を開始した。 |  | activity--daily-6b2a23bcddd9757abbb0 | 2026-02 | 2026-04 | 中 | `source--daily-96ac11961cae303bc9fd` |
| Discovery | T1057 | Process Discovery | 新たに確認されたツールセットはNightLedger、ArcBridge、BridgeHeadで、HTTPS/WebSocket C2、SOCKS5中継、DLL検索順序ハイジャック、偵察、プロセス実行、ファイル操作、画面取得などを行う。 | malware--arcbridge, malware--bridgehead, malware--nightledger | activity--mirage-kitten-middle-east-africa-2026 | 不明 | 不明 | 中 | `source--kaspersky-mirage-kitten-2026` |
| Discovery | T1083 | File and Directory Discovery | 新たに確認されたツールセットはNightLedger、ArcBridge、BridgeHeadで、HTTPS/WebSocket C2、SOCKS5中継、DLL検索順序ハイジャック、偵察、プロセス実行、ファイル操作、画面取得などを行う。 | malware--arcbridge, malware--bridgehead, malware--nightledger | activity--mirage-kitten-middle-east-africa-2026 | 不明 | 不明 | 中 | `source--kaspersky-mirage-kitten-2026` |
| Discovery | T1057 | Process Discovery | NightLedgerは実行中プロセスを列挙するコマンドを備える。 | malware--nightledger | activity--mirage-kitten-middle-east-africa-2026 | 不明 | 不明 | 中 | `source--kaspersky-mirage-kitten-2026`, `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | NightLedgerはHTTPS、ArcBridgeとBridgeHeadはWebSocketを用いてC2通信を行った。 | malware--nightledger, malware--arcbridge, malware--bridgehead | activity--mirage-kitten-middle-east-africa-2026 | 不明 | 不明 | 中 | `source--kaspersky-mirage-kitten-2026`, `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | NightLedgerは被害ホストのシステム情報を収集する偵察コマンドを備える。 | malware--nightledger | activity--mirage-kitten-middle-east-africa-2026 | 不明 | 不明 | 中 | `source--kaspersky-mirage-kitten-2026`, `source--mitre-attack-19-1` |
| Command And Control | T1090 | Proxy | BridgeHeadはWebSocket上でSOCKS5通信を中継し、ArcBridgeとともに企業プロキシ経由の接続に対応した。 | malware--arcbridge, malware--bridgehead | activity--mirage-kitten-middle-east-africa-2026 | 不明 | 不明 | 中 | `source--kaspersky-mirage-kitten-2026`, `source--mitre-attack-19-1` |
| Collection | T1113 | Screen Capture | NightLedgerは画面を取得してC2へ送るコマンドを備える。 | malware--nightledger | activity--mirage-kitten-middle-east-africa-2026 | 不明 | 不明 | 中 | `source--kaspersky-mirage-kitten-2026`, `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | 採用をテーマにした内容とビデオ会議サービスの類似ページを用い、第三者サービス上の悪性アーカイブへ標的を誘導した。 | malware--bridgehead | activity--mirage-kitten-middle-east-africa-2026 | 不明 | 不明 | 中 | `source--kaspersky-mirage-kitten-2026`, `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | 正規のAppVShNotify.exeにSspiCli.dllを読み込ませるDLL検索順序ハイジャックでNightLedgerを実行した。 | malware--nightledger | activity--mirage-kitten-middle-east-africa-2026 | 不明 | 不明 | 中 | `source--kaspersky-mirage-kitten-2026`, `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 32件
- IOC観測: 32件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 30件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| KasperskyがMirage Kittenとして追跡するUNC1549は、2026年にNightLedger、ArcBridge、BridgeHeadからなる新たなWindowsツールセットを運用した。 | 高 | `source--kaspersky-mirage-kitten-2026` | 一次解析レポート内の検体解析と被害事例に基づく。 |
| 同活動は中東に加えてアフリカへ対象を広げ、航空宇宙、航空、防衛、通信、政府、金融分野を狙っている。 | 高 | `source--kaspersky-mirage-kitten-2026` | 報告で明示された被害国・産業に限定した判断。 |

### 情報ギャップ

- IOCの初回・最終観測日は原文に記載がなく、公開日で補完していない。
- NightLedgerとBridgeHeadの初回確認時期、活動全体の開始・終了時期は不明。
- Kaspersky以外のベンダーが使うTA455、GalaxyGato、Screening Serpens等とのクラスタ境界には追加の一次資料レビューが必要。

### 不確実性

- ベンダーごとに追跡するクラスタ範囲が異なる可能性がある。
- 既存資料が示すイラン系・IRGC-CEC整合性は帰属評価であり、今回報告された個々の侵害に対する指揮関係を直接証明しない。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--kaspersky-mirage-kitten-2026 | Mirage Kitten targets Middle East and Africa region with new malware | Kaspersky GReAT | 2026-07-28 | https://securelist.com/mirage-kitten-new-tools/120811/ | vendor-research | TLP:CLEAR | 高 |
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--daily-96ac11961cae303bc9fd | イラン系APT「Screening Serpens」の2026年サイバースパイキャンペーンを追跡 | unit42.paloaltonetworks.com | 2026-05-25 | https://unit42.paloaltonetworks.com/tracking-iran-apt-screening-serpens/?utm_campaign=u42+research_screening-serpens-iran-apt&utm_source=twitter&utm_medium=social&utm_content=1779461416 | osint-report | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unc1549--58f9a9044c894db2 | unc1549 |  | 不明 | actor_profile/evidence/unc1549.csv | structured-data | TLP:CLEAR | 中 |
| source--unc1549--5ad26a22b1f5c730 | Dragos 2026 OT Cybersecurity Report A Year in Review |  | 2026 | OT/Dragos-2026-OT-Cybersecurity-Report-A-Year-in-Review.pdf | report | TLP:CLEAR | 中 |
| source--unc1549--9829507d9159174b | eset apt activity report q2 2025 q3 2025 |  | 2025 | summary/2025/eset-apt-activity-report-q2-2025-q3-2025.pdf | report | TLP:CLEAR | 中 |
| source--unc1549--c47ef662fbdb6d88 | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 不明 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

Kasperskyが明示した別名はexactとして保持するが確度はmediumとし、他ベンダーの追跡名を根拠なく統合しない。IOCの観測日は不明のまま保持する。
