# BREEZE COMET 脅威アクタープロファイル

- プロファイルID: `actor--breeze-comet`
- 状態: draft
- 更新日時: 2026-09-02T13:04:42Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

BREEZE COMET(旧UNC5669)は、ブラジルの金融サービス、小売、eコマースを標的とする金銭目的の脅威アクターである。Mandiantは2024年から一連の侵害を調査してきた。決済システムと銀行ソフトウェアを操作して不正送金を行うことを目的とし、Pix、STR、Boletoへ認証済みの取引指示を送出するために必要なmTLS資格情報と、RSFNへのアクセスを持つ組織の権限を狙う。Rust、Nim、Goによる多層のカスタムバックドア群と、侵害した正規サイトを用いた配布・C2、そして生成AIによる作戦スクリプトの高速生成を組み合わせる点に特徴がある。アクセス確立から24〜48時間以内に数百件規模の不正送金を実行した事例が確認されている。

## アクター名とAlias

- 正規名: **BREEZE COMET**
- 初回観測: 2024
- 最終観測: 2026
- 活動状態: yes

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| UNC5669 | Google Threat Intelligence Group / Mandiant | exact | 高 | `source--breeze-comet--gtig-brazil-2026` | GTIGは「GTIG tracks this activity as BREEZE COMET (formerly UNC5669)」と記載しており、同一クラスタの旧指定子として明示している。ベンダー自身による改称であるためscopeはexactとする。 |
| Plump Spider | 他ベンダーの公開報告(GTIGが参照) | overlapping | 中 | `source--breeze-comet--gtig-brazil-2026` | GTIGの記述は「This activity overlaps with operations publicly reported as Plump Spider and SHADOW-AETHER-064」であり、作戦の重複を述べるにとどまる。同一クラスタとの断定ではないためscopeはexactにしない。Plump Spiderを用いるベンダーの原報告は未確認である。 |
| SHADOW-AETHER-064 | 他ベンダーの公開報告(GTIGが参照) | overlapping | 中 | `source--breeze-comet--gtig-brazil-2026` | 同上。作戦の重複としての言及であり、原報告は未確認である。 |

## 帰属

GTIGはBREEZE COMETを金銭目的(financially motivated)の脅威アクターと評価し、国家や特定組織への帰属は行っていない。標的と運用がブラジルに集中し、回収されたスクリプトのコメントがポルトガル語であることは運用言語・活動地域の指標であって、攻撃者の所在国の帰属根拠として扱わない。

- 国: 不明
- スポンサー種別: non-state
- 確度: 中
- 証拠: `source--breeze-comet--gtig-brazil-2026`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| financial-gain | 銀行ソフトウェア、API、決済システム(Pix、STR、Boleto)を通じて取引を実行する権限を持つ組織を侵害し、大量の不正送金を実行して資産を窃取する。 | 高 | `source--breeze-comet--gtig-brazil-2026` | GTIGは「a financially motivated threat actor specializing in manipulating payment systems and banking software in Brazil to conduct fraudulent transfers」と明記している。 |

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability |  |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--cobaltspin | COBALTSPIN | Rustで書かれた軽量かつ回避性の高いネットワークトンネラー。WebSocket上にリバースSOCKS5プロキシを確立し、C2と内部標的の間でトラフィックを双方向に中継する。分割された金融ネットワークを移動し、内部ファイアウォールを越えた横展開を、検知を誘発しがちな常駐型の永続化機構なしで実現する。金融API基盤への持続的なネットワークアクセスの維持に用いられる。 | 不明 | 不明 | 高 | `source--breeze-comet--gtig-brazil-2026` |
| malware--lightpaint | LIGHTPAINT | SoftEther等の正規VPNを導入し自動永続化するよう構成するJava製のカスタムバックドア。導入したVPNマネージャーからの全通信を許可するWindows Defenderファイアウォールの受信規則をプログラム的に追加し、その後Windows Networking Vpn Plugin Platformのイベントログを消去して接続のフォレンジック痕跡を抹消する。 | 不明 | 不明 | 高 | `source--breeze-comet--gtig-brazil-2026` |
| malware--mildfrost | MILDFROST | JVMのプロセス空間内に潜む受動型のJava JARバックドア。DnsCommandBeacon.classなどのクラスを用いて低速かつ隠密なDNSトンネルを確立する。フォールバックC2としても機能し、委譲されたサブドメインを動的に問い合わせて指示を受け取り、C++実行ファイルの新しいコピーを取得する。 | 不明 | 不明 | 高 | `source--breeze-comet--gtig-brazil-2026` |
| malware--kickplate | KICKPLATE | Windows Update Health Toolsを騙るNim製のカスタムバックドア。補助ペイロードの継続的な配信とホストレベルの永続化の強制に用いられる。SOCKS5トンネラーの制御、レジストリのスタートアップキーの更新、Windowsサービスの秘密裏な変更を行うコマンドを実行する。SYSTEM権限で動作するschtasks.exeによる標準の計画タスクと、ユーザーのスタートアップフォルダー内の悪性ショートカット(.lnk)の改変を補助的に併用する。 | 不明 | 不明 | 高 | `source--breeze-comet--gtig-brazil-2026` |
| malware--boatbeam | BOATBEAM | 443番ポートで偽のIIS HTTPSサーバーを起動するGo製バックドア。正規のWebサーバーを装ってバックドア通信を隠蔽し、特定のセッションCookieを受信したときにのみC2機能を有効化する。冗長化アーキテクチャの最終層を成す。 | 不明 | 不明 | 高 | `source--breeze-comet--gtig-brazil-2026` |
| malware--realbreeze | REALBREEZE | カスタムのLDAP総当たりユーティリティ。可視性の低い環境で特権昇格に用いられる。 | 不明 | 不明 | 高 | `source--breeze-comet--gtig-brazil-2026` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--breeze-comet--commodity-set | 汎用ツール群(XWORM、AnyDesk等のRMM、Impacket、ADRecon、ADVipscan、Netcat) | 初期アクセスと偵察に用いる共有ツール群。XWORMはサイバー犯罪フォーラムで広く販売され、リークまたはクラック版も流通する汎用バックドアで、スタートアップショートカットの自動改変によって永続化するよう設定される。AnyDesk等のRMMはITサポートを装う音声通話で導入させる。Impacket、ADRecon、ADVipscanはGitHubから取得しPowerShellでメモリ上で実行することで防御回避を図る。 | 不明 | 不明 | 高 | `source--breeze-comet--gtig-brazil-2026` |

### インフラ

未確認

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| capability--breeze-comet--llm-assisted-tooling | LLMによる作戦スクリプトの生成 | 大規模言語モデルを用いて、ネットワーク偵察、資格情報の検証、大量展開、被害組織ごとのピボット、データ抽出のためのカスタムスクリプトを高速に作成する。回収されたスクリプトは高度に個別化され機能するが、人間特有の癖に乏しく、展開されたコード構造、冗長な説明コメント、定型的な実行ヘッダーに強く依存している。 | 不明 | 不明 | 中 | `source--breeze-comet--gtig-brazil-2026` |
| capability--breeze-comet--physical-rogue-device | 小売店舗ネットワークへの不正ハードウェア設置 | 2025年に、小売店舗のネットワークへ不正なハードウェア機器を直接接続して足がかりを確立する手口が初めて観測された。このネットワークアクセスから内部システムへ横展開し、Netcatとカスタムスクリプトを取得して外部のオープンディレクトリから後続のポストエクスプロイトフレームワークを引き込む。 | 2025 | 不明 | 高 | `source--breeze-comet--gtig-brazil-2026` |

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ブラジルの金融・小売・eコマースを標的とした決済システム操作による不正送金 | intrusion | 2024 | 2026 | 2026-09-01 | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--4221b5fbb827488c6eaa, target--activity-rule--sector--570d54d1d21fab6540a9 | malware--cobaltspin, malware--lightpaint, malware--mildfrost, malware--kickplate, malware--boatbeam, malware--realbreeze | ttp--activity-rule--2b2ebbe6402eafb1b795 | victim--activity-rule--c411e51fdcb57e39118a | ブラジルの銀行、決済処理事業者、小売、取引所、フィンテックおよび銀行ソフトウェア提供者を標的とし、決済システムを操作して不正送金を実行する一連の侵害。標的はPix、STR、Boletoといった銀行ソフトウェア・API・決済システムを通じて取引を実行する権限を持つ組織である。初期アクセスにはパスワードスプレー、ITサポート部門を騙る音声通話によるAnyDesk等のRMM導入、内部関係者の勧誘の試み(Axurが報告)が用いられた。2025年半ば以降は、侵害したブラジルの小規模な政府系ウェブサイトを、税務書類や領収書(ComprovantePDF.exe等)を装ったインフォスティーラー、RMM、XWORMバックドアの配布拠点およびC2エンドポイントとして悪用し、ドメイン評価フィルタによる検知を回避した。権限昇格ではImpacket、ADRecon、ADVipscanに加えカスタムのLDAP総当たりツールREALBREEZEを用い、CI/CD環境からハードコードされたパイプライン資格情報、APIキー、高特権のクラウドアクセストークンを窃取する。中核銀行システムに対して認証するために必要なmTLS資格情報と管理者証明書を、内部のhostsファイルや環境変数からboleto、cnab、remessa、webhook.*pix、instant.*payment等の検索語で探索する。横展開では乗っ取ったサービスアカウントによる不正なRDPセッションとSMB共有経由のコマンド実行、およびRust製トンネラーCOBALTSPINによる境界ファイアウォール越えを行う。永続化にはLIGHTPAINT、MILDFROST、KICKPLATE、BOATBEAMの多層冗長構成と、2025年に観測された悪性Kubernetesポッドによるクラウドシークレット窃取(dontpad[.]com等の公開メモサイトへ持ち出し)を用いる。防御弱体化としてSet-MpPreference -DisableRealtimeMonitoring $true を実行しWindows Defenderのリアルタイム監視を停止する。アクセス確立から24〜48時間以内に数百件規模の不正送金を2波にわたって実行し、少なくとも1件で数万米ドル規模の資産を窃取した。その後、横展開・権限昇格・決済APIとの通信の証跡を隠すため、侵害ホスト全体のイベントログを消去し、作成したディレクトリを削除する。 | 高 | `source--breeze-comet--gtig-brazil-2026` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| ブラジルの金融・小売・eコマースを標的とした決済システム操作による不正送金 | BREEZE COMET | BOATBEAM, COBALTSPIN, KICKPLATE, LIGHTPAINT, MILDFROST, REALBREEZE | T1110.003 Password Spraying | 情報なし | 政府・行政, 金融, 小売・ホスピタリティ | 被害事例: ブラジルの金融・小売・eコマースを標的とした決済システム操作による不正送金 | 高 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | ブラジル | 活動「ブラジルの金融・小売・eコマースを標的とした決済システム操作による不正送金」の記述で標的・被害国として明示されている。 | 2024 | 2026 | 中 | `source--breeze-comet--gtig-brazil-2026` |
| sectors | 政府・行政 | 活動「ブラジルの金融・小売・eコマースを標的とした決済システム操作による不正送金」の記述で標的として明示された産業。 | 2024 | 2026 | 中 | `source--breeze-comet--gtig-brazil-2026` |
| sectors | 金融 | 活動「ブラジルの金融・小売・eコマースを標的とした決済システム操作による不正送金」の記述で標的として明示された産業。 | 2024 | 2026 | 中 | `source--breeze-comet--gtig-brazil-2026` |
| sectors | 小売・ホスピタリティ | 活動「ブラジルの金融・小売・eコマースを標的とした決済システム操作による不正送金」の記述で標的として明示された産業。 | 2024 | 2026 | 中 | `source--breeze-comet--gtig-brazil-2026` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: ブラジルの金融・小売・eコマースを標的とした決済システム操作による不正送金 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--4221b5fbb827488c6eaa, target--activity-rule--sector--570d54d1d21fab6540a9 | malware--boatbeam, malware--cobaltspin, malware--kickplate, malware--lightpaint, malware--mildfrost, malware--realbreeze | ttp--activity-rule--2b2ebbe6402eafb1b795 | ネットワーク機器, エンドポイント, クラウド／SaaS | credential-theft: 権限昇格ではImpacket、ADRecon、ADVipscanに加えカスタムのLDAP総当たりツールREALBREEZEを用い、CI/CD環境からハードコードされたパイプライン資格情報、APIキー、高特権のクラウドアクセストークンを窃取する。 | 2024 | 2026 | 2026-09-01 | 高 | `source--breeze-comet--gtig-brazil-2026` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1110.003 | Password Spraying | 初期アクセスにはパスワードスプレー、ITサポート部門を騙る音声通話によるAnyDesk等のRMM導入、内部関係者の勧誘の試み(Axurが報告)が用いられた。 |  | activity--breeze-comet--brazil-payment-fraud-2026 | 2024 | 2026 | 中 | `source--breeze-comet--gtig-brazil-2026` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| BREEZE COMETは、ラテンアメリカのサイバー犯罪において、クライアント側の大量小口詐欺から中核的な金融スイッチおよび即時決済基盤への直接侵入へと転換した事例であり、同地域の今後の金銭目的脅威の雛形となり得る。 | 中 | `source--breeze-comet--gtig-brazil-2026` | GTIGの見通しに基づく評価であり、観測事実ではない。 |
| 作戦の中核要件は、RSFNへのアクセスを持つ組織の経由、Pix/STR等へ認証済み取引指示を送出できるmTLS資格情報、標的組織のADおよびクラウド環境における複数アカウントの持続的アクセス、ならびに送金処理手順・ネットワーク統制・不正検知の理解である。 | 高 | `source--breeze-comet--gtig-brazil-2026` | GTIGが作戦の維持要件として明示的に列挙した4点に基づく。 |

### 情報ギャップ

- GTIGが参照するPlump SpiderおよびSHADOW-AETHER-064の原報告を未確認であり、クラスタ境界の一致度を独立に検証できていない。
- Axurによる音声フィッシングと内部関係者勧誘の裏付け、およびTrend Microが報告したJBoss AS脆弱性の悪用は、いずれもGTIGが参照した他社の観測であり原報告を未確認である。
- 原文にIOC一覧は掲載されているが本作業では取り込んでおらず、profiles/breeze-comet/iocs.json は未作成である。
- 被害組織名は原文に一切記載がないため victim_cases は作成していない。

### 不確実性

- GTIGは金銭目的と評価しており国家帰属は行っていない。ブラジルは標的国であって攻撃者の所在国ではない。
- 生成AIの利用判定はコードの文体的特徴に基づくものであり、使用されたモデルやサービスは特定されていない。
- BREEZE COMETのインフラはラテンアメリカ他国およびアフリカへの拡大意図を示唆するとGTIGは述べるが、当該地域での実際の被害は確認されていない。侵害された自治体ドメインは配布インフラであり標的ではない。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--breeze-comet--gtig-brazil-2026 | Financially Motivated Threat Actor BREEZE COMET Targets Brazil | Google Threat Intelligence Group / Mandiant | 2026-09-01 | https://cloud.google.com/blog/topics/threat-intelligence/financially-motivated-threat-actor-breeze-comet-targets-brazil | vendor-technical-report | TLP:CLEAR | 高 |

## 自由記述

なし
