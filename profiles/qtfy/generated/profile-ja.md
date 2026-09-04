# QTFY 脅威アクタープロファイル

- プロファイルID: `actor--qtfy`
- 状態: draft
- 更新日時: 2026-09-02T13:11:10Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

QTFYは、中国国家安全部と人民解放軍を顧客とする中国国家支援のハッキングサービス提供者である。自ら最終標的へ侵入するのではなく、IoT機器の大量侵害(QScan)と、商用プロキシを乗っ取った暗号化中継網(Fast Labyrinth / QTRouter / QTProxy)によって、中国系アクターの活動の発信元を隠す共有基盤を提供する。米司法省とFBIは2026年8月26日、両プラットフォームにハードコードされたドメインを裁判所の許可を得て差し押さえ、QScanとQTRouterを動作不能にしたと公表した。標的として名指しされたのはNASA、連邦準備制度、エネルギー省、司法省、保健福祉省、国立衛生研究所、米国上院である。

## アクター名とAlias

- 正規名: **QTFY**
- 初回観測: 2018
- 最終観測: 2026-08-26
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Quartermaster | Lumen Technologies (Black Lotus Labs) | overlapping | 中 | `source--qtfy--lumen-quartermaster` | Black Lotus Labsは同一のQScan／QTRouter／QTProxy／Fast Labyrinth基盤を「a private technical quartermaster that may originate from Nanjing, China」として記述するが、報告本文に「QTFY」の語は現れない。両者の同一性はDOJプレスリリースが同報告を「a description of QTFY's tactics, techniques, and procedures」として参照していることに依拠する。ベンダー自身が宣言した別名ではないため scope は exact ではなく overlapping とする。 |

## 帰属

米司法省・FBIは法廷文書に基づきQTFYを中華人民共和国の国家支援グループと明示的に帰属している。政府・法執行機関による直接の帰属であり、単一ベンダーの評価より上位の根拠に当たる。ただしQTFY自体は最終標的への侵入を実行する部隊ではなく、MSSやPLAを含む顧客へ偵察・匿名化基盤を提供する技術支援主体として記述されている点を、下流アクターの活動と混同しないよう分離して扱う。

- 国: China
- スポンサー種別: state-sponsored
- 確度: 高
- 証拠: `source--daily-f3e970d5f0009ebe4c40`, `source--qtfy--lumen-quartermaster`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | 顧客である中国の情報機関・軍に対し、標的の発見・プロファイリングと帰属困難な通信経路を提供することで、諜報作戦を成立させる。 | 高 | `source--daily-f3e970d5f0009ebe4c40`, `source--qtfy--lumen-quartermaster` | DOJは顧客としてMSSとPLAを挙げ、Lumenは下流の中国系諜報作戦を支える再利用可能なサービス層と評価している。 |
| state-service-provision | 有償顧客向けにハッキングサービスを販売する営利的な請負構造を持つ。侵入そのものより、偵察・プロキシ・経路管理という基盤機能の提供を収益源とする。 | 高 | `source--daily-f3e970d5f0009ebe4c40` | 「offers computer hacking services to its paying customers」というDOJの記述に基づく。金銭目的の一般的サイバー犯罪とは区別する。 |

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
| malware--qscan | QScan | 世界中のIoT機器を走査して自動的に侵害し、QTRouterネットワークへ組み込む偵察・侵害フレームワーク。Lumenの記述では、Celery/RabbitMQを組み合わせた中央タスクブローカー(mq-task.qt-proxy.org / 154.64.238[.]222)がタスクを配分し、世界に分散したワーカーノード群が30日周期で異なる/24サブネットブロックへ計画的に切り替えながら走査を実行する。収集したアプリケーションバナー、開放ポートマップ、設定状態などのメタデータは圧縮のうえ高性能Redisクラスタ(mq-result.qt-proxy.org / 154.64.238[.]247)へ送出される。 | 不明 | 不明 | 高 | `source--daily-f3e970d5f0009ebe4c40`, `source--qtfy--lumen-quartermaster` |
| malware--qtproxy | QTProxy | Fast Labyrinthの運用ノードを管理する管理コントロールプレーン。運用者は事前設定済みの中継を利用するか、標的組織へ向けた固有の経路を個別に構成できる。Lumenは管理系のチェックイン記録から、南京に割り当てられた中国電信・中国聯通のIP空間からの運用管理活動と、乗っ取られたノードへ解決するIPからのセッションが交錯していることを確認している。 | 不明 | 不明 | 高 | `source--qtfy--lumen-quartermaster` |
| malware--qtrouter | QTRouter | QScanが侵害したIoT機器に加え、商用プロキシサービス機器と賃借した仮想専用サーバーから構成される難読化ネットワーク。QTFYおよび他の悪性アクターが侵入活動のPRC由来を隠すために用いる。悪性通信は標的ネットワークの外部、場合によっては標的と同じ地域にある機器から発信されているように見える。Lumenの記述では、運用者と顧客がプロキシ基盤およびプロキシノード管理系へアクセスするための事前設定済み物理アクセス機器として位置付けられる。 | 不明 | 不明 | 高 | `source--daily-f3e970d5f0009ebe4c40`, `source--qtfy--lumen-quartermaster` |

### ツール

未確認

### インフラ

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| infrastructure--fast-labyrinth | Fast Labyrinth | 商用の消費者向けプロキシ基盤(Lumenの表記では「Airport」)を乗っ取って構成した暗号化中継ネットワーク。標的組織との双方向通信を難読化する運用層を提供する。通信量の大半は一般的な商用VPN利用者と見分けのつかない routine traffic であり、攻撃者はその中に活動を紛れ込ませる。QScanが発見・プロファイルしたネットワークは、後にFast Labyrinth経由の双方向通信に現れる。 | 不明 | 不明 | 高 | `source--qtfy--lumen-quartermaster` |

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 米司法省、中国によるハッキングに関する主張を訂正し、米政府機関は「被害者」ではなく「標的」だったと説明 | intrusion | 不明 | 不明 | 2026-09-01 | target--activity-rule--sector--210dddb39397dbe50e91 | malware--qscan, malware--qtrouter | ttp--activity-rule--dad2781185b18bbdcf37 | victim--activity-rule--015651a588ad0e25bc2c | 米司法省は、中国国家支援グループQTFYによる攻撃について、NASAやFRB、司法省など複数の米政府機関を「被害者」ではなく「標的」とするよう過去の発表を訂正した。 QTFYは中国企業Nanjing Xinjiuwei Network Technologyに所属し、中国国家安全部からの支払いを受けて北京のためにサイバー活動を実施しているとみられる。 同グループは2018年頃から活動し、QScanとQTRouterを用いて脆弱なIoT機器を侵害し、攻撃元を隠蔽するOperational Relay Boxネットワークを構築してきた。 2019年にはPulse Secure VPNのCVE-2019-11510を悪用してNASAへの侵入を試みたとされるほか、病院、通信、電力、金融、防衛関連組織なども標的としている。 FBIはQScanとQTRouterが使用する3ドメインを差し押さえて機能を停止させたが、訂正により標的となった全組織が実際に侵害されたわけではないことが明確化された。 | 高 | `source--daily-0a5826ce9e99e3db29e4`, `source--daily-f3e970d5f0009ebe4c40` |
| クオーターマスター型基盤による諜報作戦の支援(Fast Labyrinth / QScan) | infrastructure-operation | 不明 | 不明 | 2026-08-26 | target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--country--f9601e2d842c9a05202b, target--activity-rule--sector--260bd106ff4950e5430d, target--activity-rule--sector--b8d6639a1884e2bacaa4, target--activity-rule--sector--b94dc560a327b601965d, target--activity-rule--sector--e7608f51421ca8b1e297 | malware--qscan, malware--qtrouter, malware--qtproxy |  | victim--activity-rule--547eb506c9eb1e68e54f | Black Lotus Labsが1年間追跡した、サイバー諜報活動を支える基盤提供者の作戦。偵察(QScan)、プロキシ統制(QTProxy)、運用経路(Fast Labyrinth)、アクセス管理(QTRouter)を再利用可能なサービス層として統合し、下流の複数アクターへ帰属困難な通信路と標的検証テレメトリを同時提供する。Fast Labyrinthの通信を背景ノイズで絞り込むと、特定の戦略分野に限定した profiling キャンペーンが現れる。標的には世界各国の主要研究大学(先端物理学、バイオインフォマティクス、航空宇宙・衛星システム)、各国の政府・防衛・公共部門ネットワークが含まれ、とりわけ米国、英国、アジア太平洋地域の機関が対象となっている。米国では軍・防衛ネットワークが重点的にプロファイルされ、稼働中の通信ゲートウェイ、アクセス制御、機微な物流を扱うサプライヤーの境界が注視されている。地質・環境関連の政府機関、および世界各地の司法ノードと欧州のインフラも関心対象である。攻撃者は公開された開発環境の境界、未修正のクラウドストレージ、認証情報窃取に着目している。 | 中 | `source--qtfy--lumen-quartermaster` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| 米司法省、中国によるハッキングに関する主張を訂正し、米政府機関は「被害者」ではなく「標的」だったと説明 | QTFY | QScan, QTRouter | T1190 Exploit Public-Facing Application | 情報なし | 政府・行政 | 被害事例: 米司法省、中国によるハッキングに関する主張を訂正し、米政府機関は「被害者」ではなく「標的」だったと説明 | 高 |
| クオーターマスター型基盤による諜報作戦の支援(Fast Labyrinth / QScan) | QTFY | QScan, QTProxy, QTRouter | 情報なし | Fast Labyrinth | 米国, 英国, 医療・ヘルスケア, 運輸・航空・海運, 防衛・軍事, 教育・研究 | 被害事例: クオーターマスター型基盤による諜報作戦の支援(Fast Labyrinth / QScan) | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 米国 | 活動「クオーターマスター型基盤による諜報作戦の支援(Fast Labyrinth / QScan)」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--qtfy--lumen-quartermaster` |
| countries | 英国 | 活動「クオーターマスター型基盤による諜報作戦の支援(Fast Labyrinth / QScan)」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--qtfy--lumen-quartermaster` |
| regions | アジア | 活動「クオーターマスター型基盤による諜報作戦の支援(Fast Labyrinth / QScan)」の記述で標的地域としてアジアが明示されている。 | 不明 | 不明 | 中 | `source--qtfy--lumen-quartermaster` |
| regions | アジア太平洋 | 活動「クオーターマスター型基盤による諜報作戦の支援(Fast Labyrinth / QScan)」の記述で標的地域としてアジア太平洋が明示されている。 | 不明 | 不明 | 中 | `source--qtfy--lumen-quartermaster` |
| sectors | 政府・行政 | 活動「米司法省、中国によるハッキングに関する主張を訂正し、米政府機関は「被害者」ではなく「標的」だったと説明」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-0a5826ce9e99e3db29e4`, `source--daily-f3e970d5f0009ebe4c40` |
| sectors | 医療・ヘルスケア | 活動「クオーターマスター型基盤による諜報作戦の支援(Fast Labyrinth / QScan)」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--qtfy--lumen-quartermaster` |
| sectors | 運輸・航空・海運 | 活動「クオーターマスター型基盤による諜報作戦の支援(Fast Labyrinth / QScan)」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--qtfy--lumen-quartermaster` |
| sectors | 防衛・軍事 | 活動「クオーターマスター型基盤による諜報作戦の支援(Fast Labyrinth / QScan)」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--qtfy--lumen-quartermaster` |
| sectors | 教育・研究 | 活動「クオーターマスター型基盤による諜報作戦の支援(Fast Labyrinth / QScan)」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--qtfy--lumen-quartermaster` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 米司法省、中国によるハッキングに関する主張を訂正し、米政府機関は「被害者」ではなく「標的」だったと説明 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--210dddb39397dbe50e91 | malware--qscan, malware--qtrouter | ttp--activity-rule--dad2781185b18bbdcf37 | VPN／リモートアクセス機器, ネットワーク機器 |  | 不明 | 不明 | 2026-09-01 | 高 | `source--daily-0a5826ce9e99e3db29e4`, `source--daily-f3e970d5f0009ebe4c40` |
| 被害事例: クオーターマスター型基盤による諜報作戦の支援(Fast Labyrinth / QScan) | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--6604ad21c713b8dfd8c7, target--activity-rule--country--f9601e2d842c9a05202b, target--activity-rule--sector--260bd106ff4950e5430d, target--activity-rule--sector--b8d6639a1884e2bacaa4, target--activity-rule--sector--b94dc560a327b601965d, target--activity-rule--sector--e7608f51421ca8b1e297 | malware--qscan, malware--qtproxy, malware--qtrouter |  | ネットワーク機器, クラウド／SaaS, 開発環境／ソースコード | credential-theft: 攻撃者は公開された開発環境の境界、未修正のクラウドストレージ、認証情報窃取に着目している。<br>espionage: Black Lotus Labsが1年間追跡した、サイバー諜報活動を支える基盤提供者の作戦。 | 不明 | 不明 | 2026-08-26 | 中 | `source--qtfy--lumen-quartermaster` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Initial Access | T1190 | Exploit Public-Facing Application | 2019年にはPulse Secure VPNのCVE-2019-11510を悪用してNASAへの侵入を試みたとされるほか、病院、通信、電力、金融、防衛関連組織なども標的としている。 |  | activity--daily-a49b84f62f89cb5c3f4b | 不明 | 不明 | 中 | `source--daily-0a5826ce9e99e3db29e4`, `source--daily-f3e970d5f0009ebe4c40` |

## IOC／artifact概要

- IOC値: 4件
- IOC観測: 4件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| QTFYは中華人民共和国の国家支援グループであり、南京鑫玖维网络科技有限公司に雇用され、MSSとPLAを含む有償顧客へ偵察・匿名化基盤を提供する技術支援主体である。 | 高 | `source--daily-f3e970d5f0009ebe4c40` | 米司法省・FBIが法廷文書に基づき公表した帰属であり、政府・法執行機関による一次資料に当たる。 |
| QTFYの中核的価値は最終標的への侵入ではなく、複数の下流アクターが同時利用できる共有難読化基盤の提供にある。したがって単一のクオーターマスターの停止は複数の作戦能力を同時に低下させる。 | 中 | `source--qtfy--lumen-quartermaster` | Lumenの評価に基づく。実際にDOJはハードコードされたドメインの差押えによりQScanとQTRouterを動作不能にしたと述べており、評価と整合する。 |

### 情報ギャップ

- FBIとNSAが同日公表したQTFYの侵害指標入りサイバーセキュリティアドバイザリの原文を未確認である。DOJプレスリリースの参照によって存在は確認できているが、アドバイザリ本体のIOCと2018年まで遡る観測期間の詳細は取り込んでいない。
- DOJが参照する affidavit(宣誓供述書)の原文を未確認である。
- 二次報道が伝える別名「QT」「QTCYBER」、2019年のPulse Secure VPN脆弱性CVE-2019-11510を用いたNASAへの侵入試行、病院・通信・電力・金融・防衛を含む標的分野の記述は、DOJおよびLumenの一次資料では確認できていない。確認できるまでプロファイルへ取り込まない。
- Fast Labyrinth経由で観測された下流作戦のうち、どれがQTFY自身の作戦でどれが顧客アクターの作戦かを分離する根拠がない。

### 不確実性

- Lumen Black Lotus Labsの報告は「QTFY」の名称を用いていない。QTFYとLumenの「quartermaster」の同一性は、DOJプレスリリースが同報告をQTFYのTTP解説として参照している点に依拠する。
- DOJプレスリリースは2026年8月28日に更新され、標的となった米政府機関を「被害者」ではなく「標的」とする趣旨の訂正が加えられている。本文末尾に「Edits have been made to ensure this press release accurately reflects the government's allegations in the affidavit」との注記がある。列挙された政府機関が実際に侵害されたことを意味しないため、victim_casesは作成していない。
- 南京というIPジオロケーション上の所在は、Lumen自身が運用者の物理的所在を判定できないと明記している。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--daily-0a5826ce9e99e3db29e4 | 米司法省、中国によるハッキングに関する主張を訂正し、米政府機関は「被害者」ではなく「標的」だったと説明 — IOC補助資料 | thehackernews.com | 不明 | https://thehackernews.com/2026/08/doj-corrects-china-hacking-claim-says.html | osint-report | TLP:CLEAR | 中 |
| source--daily-f3e970d5f0009ebe4c40 | 米司法省、中国によるハッキングに関する主張を訂正し、米政府機関は「被害者」ではなく「標的」だったと説明 | justice.gov | 2026-09-01 | https://www.justice.gov/opa/pr/justice-department-and-fbi-seize-platforms-operated-and-used-china-state-sponsored-hackers | osint-report | TLP:CLEAR | 中 |
| source--qtfy--lumen-quartermaster | The infrastructure quartermaster: inside a China-nexus state enablement model | Lumen Technologies (Black Lotus Labs) | 2026-08-26 | https://www.lumen.com/blog/en-us/the-infrastructure-quartermaster-inside-a-china-nexus-state-enablement-model | vendor-technical-report | TLP:CLEAR | 高 |

## 自由記述

なし
