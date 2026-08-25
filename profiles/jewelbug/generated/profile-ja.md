# Jewelbug 脅威アクタープロファイル

- プロファイルID: `actor--jewelbug`
- 状態: draft
- 更新日時: 2026-08-25T22:34:54Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Jewelbug(別名Earth Alux、REF7707、CL-STA-0049)は、Symantecが2026-08-13に報告した中国拠点のhack-for-hire型APTクラスタである。中東・東南アジア・南アジアの政府省庁・軍・国営通信事業者・警察に対する諜報活動と、中国語話者を標的とする大規模な暗号資産詐欺を、同一の管理パネルと重複する基盤・手法で並行運用する点が最大の特徴である。

## アクター名とAlias

- 正規名: **Jewelbug**
- 初回観測: 不明
- 最終観測: 2026-08-13
- 活動状態: yes

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Earth Alux | Trend Micro | overlapping | 中 | `source--symantec-jewelbug-2026`, `source--trendmicro-earth-alux-2025` | Symantecが「Jewelbug (aka Earth Alux, REF7707, CL-STA-0049), a China-based APT group」と記載する。Trend Microの原文(2025-03-31)ではEarth Aluxを中国系の侵入セットとして独立に定義しており、観測期間(2023年Q2〜)とマルウェア群(VARGEIT、COBEACON、RAILLOAD、RAILSETTER、MASQLOADER、GODZILLA)はSymantecがJewelbugとして報告した実装群と重ならない。同一視の根拠はSymantecの記載のみであるためscopeはoverlappingとし、Earth Alux側の実績は本プロファイルへ複製しない。 |
| REF7707 | Elastic Security Labs | overlapping | 中 | `source--symantec-jewelbug-2026`, `source--elastic-ref7707-2025` | Elasticの原文(2025-02-13)はREF7707を南米某国外務省への侵入から追跡したクラスタとして定義し、FINALDRAFT、PATHLOADER、GUIDLOADERを挙げる。出身国の帰属は主張していない。SymantecのみがJewelbugと同一視しているためscopeはoverlappingとする。 |
| CL-STA-0049 | Palo Alto Networks Unit 42 | overlapping | 低 | `source--symantec-jewelbug-2026` | Symantecの別名列挙にのみ基づく。本レビューではUnit 42側の一次資料を確認できていないため確度はlowとし、未照合であることを明記する。 |

## 帰属

Symantecは「Jewelbug (aka Earth Alux, REF7707, CL-STA-0049), a China-based APT group」と記載し、運用者が中国国内から活動していると評価する。根拠として、中国本土向け宛先を迂回するよう構成されたVPNルーティング、UTC+8の午後から深夜に集中する稼働パターン、湖南省長沙市に登記され自らSEO事業として広告する企業と、政府発行の身分証から特定された唯一の法定代表者を挙げる。運用者は管理パネル上で admin / admin_s を用い、ニックネームople500、ハンドルpaopaodada、エクスプロイトモジュール群の署名Xg Teamが確認されている。一方で、同資料はJewelbugを発注・後援する国家機関や組織を特定していないため、sponsor_typeはunknownのままとする。hack-for-hireという性格付けと、諜報活動と自己資金調達的な暗号資産詐欺の並行運用は同資料の評価である。

- 国: 中国
- スポンサー種別: unknown
- 確度: 中
- 証拠: `source--symantec-jewelbug-2026`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | 中東・東南アジア・南アジアの政府省庁、軍、国営通信事業者、警察に対し、Webメールのcookie・認証情報・メール本文の窃取と、内部の仮想化管理基盤や政府通信システムへの到達を行う。 | 高 | `source--symantec-jewelbug-2026` |  |
| financial-gain | 中国語話者の暗号資産利用者を対象に、SEOポイズニングと偽の取引所配布ページ、ブラウザー拡張機能による暗号資産アドレスの差し替えで資金を窃取する。Symantecはこれを諜報活動と同一基盤・同一パネルで並行運用される活動として記述している。 | 高 | `source--symantec-jewelbug-2026` | 諜報活動の資金源であるか否かは資料が明示していないため、動機として分離して記載する。 |

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | Symantecが中国拠点のhack-for-hire型APTと評価するクラスタJewelbug。運用者は湖南省長沙市に登記された企業と結び付き、UTC+8の稼働パターンを示す。後援主体は特定されていない。 |
| Capability | WindowsバックドアAntino、悪意あるブラウザー拡張機能PDF Viewer、Rust実装のLinux/ルーターインプラントClientKing、自作の遠隔操作・情報窃取プラットフォームXG-Web。カーネルモジュール型ルートキットとsu/sudoフック型認証モジュールを併用する。 |
| Infrastructure | 侵害した国営通信事業者の共有Webメールホスティング、40台超のCMSサーバーと数百の類似ドメイン、Google Fontsを模したC&Cドメイン、C&CチャネルとしてのMicrosoft Graph API、Google Docs経由のペイロード配信。 |
| Victim | 中東・東南アジア・南アジアの政府省庁、軍、国営通信事業者、警察。詐欺側では中国語話者の暗号資産利用者。 |
| Socio-political | 政府・軍への諜報という国家的関心の対象と、中国語話者を狙う金銭目的の詐欺が、同一の運用者・同一の管理パネルで並行している。Symantecはこれをhack-for-hireの性格として整理している。 |

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--jewelbug-antino | Antino | HTAダウンローダーや偽のAdobe Flash・インストーラーを介して配布されるWindowsバックドア。C&CチャネルにMicrosoft Graph APIを悪用し、悪意あるブラウザー拡張機能「PDF Viewer」をサイドロードする。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| malware--jewelbug-pdf-viewer-extension | PDF Viewer (悪意あるブラウザー拡張機能) | Chrome/Firefox向けの悪意ある拡張機能。認証情報、cookie、閲覧履歴、ブックマーク、スクリーンショット、クリップボードを窃取し、暗号資産アドレスを差し替えるモジュールを備える。ネイティブメッセージングホスト com.microsoft.runedge と対で動作し、ブラウザーのサンドボックスから離脱する。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| malware--jewelbug-clientking | ClientKing | Rustで実装されたLinux・ルーター向けインプラント。x86-64、ARM64、ASUSルーターを対象とする37種のビルドが確認されている。独自のDNSトンネルを含む5系統のC&Cトランスポートを備え、カーネルモジュールの読み込み、SOCKSによるピボット、認証情報窃取に対応する。カーネルモジュール型ルートキットと、su/sudoをフックする悪意ある認証モジュールを伴う。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--jewelbug-xg-web | XG-Web | 攻撃者が自作したブラウザー中心の遠隔操作・情報窃取プラットフォーム。Node.jsバックエンド上のReact製パネルとMySQLデータベースで構成され、被害端末のランデブーポイントとして機能する。パネル上では自らを「penetration-testing platform」と称している。諜報活動と暗号資産詐欺の双方がこの単一パネルから運用されている。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |

### インフラ

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| infrastructure--jewelbug-cms-fleet | CMSサーバー群と類似ドメイン | 40台超のコンテンツ管理サーバーと数百の類似ドメインからなる基盤。AI生成の偽取引所ダウンロードページ、OKX・Binanceのタイポスクワットドメイン、クローラー向けに内容を出し分けるクローキングページを配信する。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| infrastructure--jewelbug-compromised-shared-hosting | 侵害済み共有ウェブホスティング | 国営通信事業者が運用する共有Webメールホスティング基盤。単一のウォータリングホール注入で15を超える政府テナントへ共通の悪意あるJavaScriptを配信する起点となった。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |

### 配送・ファイル形式

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| delivery--jewelbug-hta | HTAダウンローダー | Antinoの配布に用いられるHTA形式のダウンローダー。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| delivery--jewelbug-fake-installer | 偽Adobe Flash／Microsoft Edge更新インストーラー | 重要標的に対して表示される偽の更新・インストーラー。flashcenter_pp_ax_install_en.exe のような正規名称を模した実行ファイルを含む。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| delivery--jewelbug-browser-extension | 悪意あるブラウザー拡張機能 | 「PDF Viewer」の名称でChrome/Firefoxへ導入される拡張機能。Antinoによりサイドロードされる。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| delivery--jewelbug-google-docs | Google Docs経由のペイロード配信 | 正規のGoogle Docsを配信経路として用いるペイロード投下と実行。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |

### 脆弱性

未確認

### 運用能力

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| opcap--jewelbug-multi-tenant-watering-hole | 共有ホスティング侵害による多テナント同時ウォータリングホール | 単一の侵害点への注入で15を超える政府Webメールテナントの利用者へ同時に到達する。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| opcap--jewelbug-session-token-theft | ログインフォームのフックとセッショントークンのリアルタイム窃取 | ログインフォームをフックして認証情報を取得し、cookieの窃取と併せてセッショントークンをリアルタイムで奪取する。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| opcap--jewelbug-native-messaging-escape | ネイティブメッセージングによるブラウザーサンドボックスからの離脱 | ネイティブメッセージングホスト com.microsoft.runedge を介して拡張機能からホスト側の実行へ橋渡しする。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| opcap--jewelbug-seo-poisoning | SEOポイズニングとクリックボットによる検索順位操作 | 40台超のCMSサーバー、AI生成ページ、クリックボット、クローキングを組み合わせて検索結果を操作する。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| opcap--jewelbug-detection-monitoring | VirusTotal評価の定期確認による検知状況の監視 | 12時間ごとに自らの検体の評価を確認する。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| opcap--jewelbug-vpn-split-tunneling | 中国本土向け宛先を迂回するVPNスプリットトンネリング | 運用者の所在を秘匿しつつ中国本土のフィルタリングを回避する構成。帰属評価の根拠のひとつでもある。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SEOポイズニングと偽取引所サイトによる暗号資産詐欺 | financial-fraud | 不明 | 不明 | 2026-08-13 | target--activity-rule--country--95e363d6dfa8c6f2ecbb, target--activity-rule--sector--63c9fa67327d005b07b7, target--jewelbug--role--chinese-speaking-crypto-users | malware--jewelbug-pdf-viewer-extension | ttp--jewelbug-t1036-005, ttp--jewelbug-t1608-006 | victim--activity-rule--da2d2e0da904c89a5535 | 諜報活動と同一の管理パネルから運用される、中国語話者を標的とする暗号資産詐欺。40台超のコンテンツ管理サーバーと数百の類似ドメインを用い、AI生成の偽取引所ダウンロードページ、OKX・Binanceのタイポスクワットドメイン、クローラー向けに内容を出し分けるクローキングページを配信する。クリックボットで検索順位を操作するSEOポイズニングにより被害者を誘導し、悪意あるブラウザー拡張機能の暗号資産アドレス差し替えモジュールと組み合わせて資金を窃取する。スポーツ賭博、海賊版ライブ配信サイト、私立探偵詐欺といった別の誘導手口も併用されている。 | 高 | `source--symantec-jewelbug-2026` |
| 共有Webメールホスティング侵害による政府・軍への諜報活動 | cyber-espionage | 不明 | 不明 | 2026-08-13 | target--activity-rule--sector--97fa6f38a056d42117be, target--jewelbug--country--taiwan, target--jewelbug--region--middle-east, target--jewelbug--region--south-asia, target--jewelbug--region--southeast-asia, target--jewelbug--sector--defense, target--jewelbug--sector--government, target--jewelbug--sector--law-enforcement, target--jewelbug--sector--telecommunications | malware--jewelbug-antino, malware--jewelbug-pdf-viewer-extension, malware--jewelbug-clientking | ttp--activity-rule--d370d222c172b5e5788d, ttp--jewelbug-t1014, ttp--jewelbug-t1036-005, ttp--jewelbug-t1071-004, ttp--jewelbug-t1090, ttp--jewelbug-t1102-002, ttp--jewelbug-t1176-001, ttp--jewelbug-t1189, ttp--jewelbug-t1204-002, ttp--jewelbug-t1539, ttp--jewelbug-t1556-003, ttp--jewelbug-t1584-004 | victim--activity-rule--60d3466b22698b895c22, victim--jewelbug-government-webmail-tenants | 国営通信事業者などが運用する共有ウェブホスティングを侵害し、単一のウォータリングホール注入で15を超える政府Webメールテナントへ共通の悪意あるJavaScriptを配信した。スクリプトはWebメールのcookieと電子メールアドレスを窃取し、重要標的には偽のAdobe Flash更新等を表示してWindowsバックドアAntinoと悪意あるブラウザー拡張機能「PDF Viewer」を追加投入する。LinuxホストとルーターにはRust実装のインプラントClientKingを配置し、独自DNSトンネルを含む5系統のC&C、SOCKSピボット、カーネルモジュール型ルートキット、su/sudoフックによる認証情報窃取を行う。内部の仮想化管理クラスタや政府の通信システムにも到達している。攻撃者の基盤には約110万件の位置情報イベント、58万件超のcookie、数千件の認証情報、2,300件超のメール本文が記録されていた。 | 高 | `source--symantec-jewelbug-2026` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| SEOポイズニングと偽取引所サイトによる暗号資産詐欺 | Jewelbug | PDF Viewer (悪意あるブラウザー拡張機能) | T1036.005 Match Legitimate Resource Name or Location, T1608.006 SEO Poisoning | CMSサーバー群と類似ドメイン | 中国, 暗号資産・Web3, 中国語話者の暗号資産利用者 | 被害事例: SEOポイズニングと偽取引所サイトによる暗号資産詐欺 | 高 |
| 共有Webメールホスティング侵害による政府・軍への諜報活動 | Jewelbug | Antino, ClientKing, PDF Viewer (悪意あるブラウザー拡張機能) | T1071.004 DNS, T1014 Rootkit, T1036.005 Match Legitimate Resource Name or Location, T1071.004 DNS, T1090 Proxy, T1102.002 Bidirectional Communication, T1176.001 Browser Extensions, T1189 Drive-by Compromise, T1204.002 Malicious File, T1539 Steal Web Session Cookie, T1556.003 Pluggable Authentication Modules, T1584.004 Server | 侵害済み共有ウェブホスティング | 情報通信, 台湾, 中東, 南アジア, 東南アジア, 国防・軍, 政府・行政, 法執行機関, 通信 | 被害事例: 共有Webメールホスティング侵害による政府・軍への諜報活動, 被害事例: 共有ホスティング上の政府Webメールテナント15超の侵害 | 高 |

Symantecは数カ月にわたる調査として本件を報告しているが、活動の開始時期は明示していない。別名として挙がるEarth AluxはTrend Microが2025-03-31に、REF7707はElastic Security Labsが2025-02-13に、それぞれ独立に定義・公表したクラスタである。

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 中国 | 活動「SEOポイズニングと偽取引所サイトによる暗号資産詐欺」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--symantec-jewelbug-2026` |
| countries | 台湾 | Symantecは台湾の政府機関の体裁を模したデコイ文書が使用されたと記載している。 | 不明 | 不明 | 中 | `source--symantec-jewelbug-2026` |
| regions | 中東 | 国営通信事業者が運用する共有Webメールホスティングの侵害を通じ、中東某国の15を超える政府Webメールテナントが侵害された。基盤の記録では中東某国からの接続が53,100件確認されている。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| regions | 南アジア | 南アジアでは警察および政府の電子メールアドレス90件超が侵害対象として確認されている。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| regions | 東アジア | 中国、台湾で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--symantec-jewelbug-2026` |
| regions | 東南アジア | 東南アジアの国営通信事業者と軍のネットワークが標的とされた。基盤の記録では東南アジア某国からの接続が87,200件、別の東南アジア某国から15,000件確認されている。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| sectors | 暗号資産・Web3 | 活動「SEOポイズニングと偽取引所サイトによる暗号資産詐欺」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--symantec-jewelbug-2026` |
| sectors | 情報通信 | 活動「共有Webメールホスティング侵害による政府・軍への諜報活動」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--symantec-jewelbug-2026` |
| sectors | 国防・軍 | 東南アジアの軍ネットワークが標的として記載されている。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| sectors | 政府・行政 | 中東・東南アジア・南アジアの政府省庁と政府通信システムが諜報活動の主対象である。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| sectors | 法執行機関 | 南アジアの警察の電子メールアドレスが政府アドレスと併せて90件超確認されている。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| sectors | 通信 | 国営通信事業者およびナショナルキャリアが、直接の標的であると同時に共有ホスティング侵害を通じた配信経路としても利用された。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| roles | 中国語話者の暗号資産利用者 | 暗号資産詐欺側のSEOポイズニングとタイポスクワットは中国語話者の暗号資産利用者を対象としている。 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |

選定ロジック: 諜報側は政府・軍・通信・法執行のWebメールと通信系システムを、共有ホスティングの侵害によって広く同時に取得できる標的として選定している。詐欺側は検索経由で偽の取引所配布ページへ誘導できる中国語話者の暗号資産利用者を対象とする。両者は同一の管理パネルと重複する基盤・手法で運用されている。 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 共有Webメールホスティング侵害による政府・軍への諜報活動 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--97fa6f38a056d42117be, target--jewelbug--country--taiwan, target--jewelbug--region--middle-east, target--jewelbug--region--south-asia, target--jewelbug--region--southeast-asia, target--jewelbug--sector--defense, target--jewelbug--sector--government, target--jewelbug--sector--law-enforcement, target--jewelbug--sector--telecommunications | malware--jewelbug-antino, malware--jewelbug-clientking, malware--jewelbug-pdf-viewer-extension | ttp--activity-rule--d370d222c172b5e5788d, ttp--jewelbug-t1014, ttp--jewelbug-t1036-005, ttp--jewelbug-t1071-004, ttp--jewelbug-t1090, ttp--jewelbug-t1102-002, ttp--jewelbug-t1176-001, ttp--jewelbug-t1189, ttp--jewelbug-t1204-002, ttp--jewelbug-t1539, ttp--jewelbug-t1556-003, ttp--jewelbug-t1584-004 | メール／メールアカウント, ネットワーク機器 | credential-theft: LinuxホストとルーターにはRust実装のインプラントClientKingを配置し、独自DNSトンネルを含む5系統のC&C、SOCKSピボット、カーネルモジュール型ルートキット、su/sudoフックによる認証情報窃取を行う。 | 不明 | 不明 | 2026-08-13 | 高 | `source--symantec-jewelbug-2026` |
| 被害事例: SEOポイズニングと偽取引所サイトによる暗号資産詐欺 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--95e363d6dfa8c6f2ecbb, target--activity-rule--sector--63c9fa67327d005b07b7, target--jewelbug--role--chinese-speaking-crypto-users | malware--jewelbug-pdf-viewer-extension | ttp--jewelbug-t1036-005, ttp--jewelbug-t1608-006 | サーバー | financial-loss: クリックボットで検索順位を操作するSEOポイズニングにより被害者を誘導し、悪意あるブラウザー拡張機能の暗号資産アドレス差し替えモジュールと組み合わせて資金を窃取する。 | 不明 | 不明 | 2026-08-13 | 高 | `source--symantec-jewelbug-2026` |
| 被害事例: 共有ホスティング上の政府Webメールテナント15超の侵害 | 非公開 | aggregate | multiple-organizations | reported | target--jewelbug--region--middle-east, target--jewelbug--region--southeast-asia, target--jewelbug--region--south-asia, target--jewelbug--sector--government, target--jewelbug--sector--defense, target--jewelbug--sector--telecommunications, target--jewelbug--sector--law-enforcement | malware--jewelbug-antino, malware--jewelbug-pdf-viewer-extension, malware--jewelbug-clientking | ttp--jewelbug-t1584-004, ttp--jewelbug-t1189, ttp--jewelbug-t1539, ttp--jewelbug-t1204-002, ttp--jewelbug-t1176-001, ttp--jewelbug-t1102-002, ttp--jewelbug-t1071-004, ttp--jewelbug-t1090, ttp--jewelbug-t1014, ttp--jewelbug-t1556-003, ttp--jewelbug-t1036-005 | メール／メールアカウント, 共有ウェブホスティング, 仮想化管理基盤, ルーター／ネットワーク機器 | 認証情報の窃取: 数千件の認証情報が攻撃者基盤に記録されていた。<br>セッションcookieの窃取: 58万件超のブラウザーcookieが記録され、セッショントークンのリアルタイム奪取に用いられた。<br>データ窃取: 2,300件超のメール本文が3カ月未満の期間に窃取・記録された。 | 不明 | 不明 | 2026-08-13 | 高 | `source--symantec-jewelbug-2026` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1071.004 | DNS | LinuxホストとルーターにはRust実装のインプラントClientKingを配置し、独自DNSトンネルを含む5系統のC&C、SOCKSピボット、カーネルモジュール型ルートキット、su/sudoフックによる認証情報窃取を行う。 | malware--jewelbug-clientking | activity--jewelbug-government-webmail-espionage-2026 | 不明 | 不明 | 中 | `source--symantec-jewelbug-2026` |
| Defense Evasion | T1014 | Rootkit | ClientKingに随伴するツールキットにカーネルモジュール型ルートキットが含まれる。 | malware--jewelbug-clientking | activity--jewelbug-government-webmail-espionage-2026 | 不明 | 不明 | 中 | `source--symantec-jewelbug-2026` |
| Defense Evasion | T1036.005 | Match Legitimate Resource Name or Location | C&Cドメインに fonts[.]chrorne[.]com のようなGoogle Fontsを模した名称を用い、ネイティブメッセージングホスト名にも com.microsoft.runedge を用いる。 |  | activity--jewelbug-government-webmail-espionage-2026, activity--jewelbug-crypto-fraud-seo-2026 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| Command and Control | T1071.004 | DNS | ClientKingは独自実装のDNSトンネルを含む5系統のC&Cトランスポートを備える。 | malware--jewelbug-clientking | activity--jewelbug-government-webmail-espionage-2026 | 不明 | 不明 | 中 | `source--symantec-jewelbug-2026` |
| Command and Control | T1090 | Proxy | ClientKingはSOCKSによるピボットに対応し、侵害したLinuxホストやルーターを経由点として利用する。 | malware--jewelbug-clientking | activity--jewelbug-government-webmail-espionage-2026 | 不明 | 不明 | 中 | `source--symantec-jewelbug-2026` |
| Command and Control | T1102.002 | Bidirectional Communication | AntinoはMicrosoft Graph APIをC&Cチャネルとして悪用する。 | malware--jewelbug-antino | activity--jewelbug-government-webmail-espionage-2026 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| Persistence | T1176.001 | Browser Extensions | Antinoが悪意あるブラウザー拡張機能「PDF Viewer」をサイドロードし、ネイティブメッセージングホスト com.microsoft.runedge と対で常駐させた。 | malware--jewelbug-pdf-viewer-extension, malware--jewelbug-antino | activity--jewelbug-government-webmail-espionage-2026 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| Initial Access | T1189 | Drive-by Compromise | 侵害した共有ホスティング上のWebメールへ共通の悪意あるJavaScriptを注入し、15を超える政府テナントの利用者に対するウォータリングホールとした。 |  | activity--jewelbug-government-webmail-espionage-2026 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| Execution | T1204.002 | Malicious File | 重要標的に対し、偽のAdobe Flash更新やインストーラーを表示してAntinoバックドアを実行させた。 | malware--jewelbug-antino | activity--jewelbug-government-webmail-espionage-2026 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| Credential Access | T1539 | Steal Web Session Cookie | 注入したスクリプトと拡張機能によりWebメールのcookieを窃取し、セッショントークンをリアルタイムで奪取した。基盤には58万件超のcookieが記録されていた。 | malware--jewelbug-pdf-viewer-extension | activity--jewelbug-government-webmail-espionage-2026 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| Credential Access | T1556.003 | Pluggable Authentication Modules | su および sudo をフックする悪意ある認証モジュールを配置し、認証情報を取得する。 | malware--jewelbug-clientking | activity--jewelbug-government-webmail-espionage-2026 | 不明 | 不明 | 中 | `source--symantec-jewelbug-2026` |
| Resource Development | T1584.004 | Server | 国営通信事業者が運用する共有Webメールホスティング基盤を侵害し、配信起点として利用した。 |  | activity--jewelbug-government-webmail-espionage-2026 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |
| Resource Development | T1608.006 | SEO Poisoning | AI生成の偽ダウンロードページ、40台超のCMSサーバー、クリックボットによる順位操作を組み合わせ、中国語話者の検索結果へ偽の取引所配布ページを露出させた。 |  | activity--jewelbug-crypto-fraud-seo-2026 | 不明 | 不明 | 高 | `source--symantec-jewelbug-2026` |

## IOC／artifact概要

- IOC値: 52件
- IOC観測: 52件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| Jewelbugは政府・軍への諜報と、中国語話者を狙う暗号資産詐欺を、同一の管理パネルと重複する基盤・手法で並行運用している。 | 高 | `source--symantec-jewelbug-2026` | Symantecは「Cryptocurrency fraud and espionage campaigns share the same infrastructure, overlapping techniques and one control panel」と記載する。 |
| 諜報側の中核は、国営通信事業者が運用する共有ウェブホスティングを侵害し、単一のウォータリングホール注入で15を超える政府Webメールテナントへ同時に到達する手口である。 | 高 | `source--symantec-jewelbug-2026` |  |
| 運用者の所在は中国であるとSymantecが複数の根拠(UTC+8の稼働パターン、中国本土向け宛先を迂回するVPN構成、湖南省長沙市の登記企業と法定代表者)から評価しているが、発注者・後援主体は特定されていない。 | 中 | `source--symantec-jewelbug-2026` | 単一ベンダーの評価であるため確度はmedium。所在国の確度と後援主体の有無の確度を分離して扱う。 |
| 別名として挙がるEarth Alux(Trend Micro)とREF7707(Elastic Security Labs)は独立した一次資料を持つクラスタであり、新規プロファイル昇格の閾値を満たすが、同一クラスタであるかはSymantecの記載以外に裏付けがない。 | 低 | `source--symantec-jewelbug-2026`, `source--trendmicro-earth-alux-2025`, `source--elastic-ref7707-2025` | 各別名側の観測期間・マルウェア群はSymantecの報告内容と重ならない。aliasのscopeはoverlappingとし、実績を相互に流用しない。 |

### 情報ギャップ

- 被害国の大半が原文で匿名化されており、個別国単位の標的確定ができない。
- 活動の開始日・終了日が原文に明示されておらず、活動期間はunknownのままである。
- 別名CL-STA-0049についてはPalo Alto Networks Unit 42側の一次資料を本レビューで確認できていない。
- Earth Alux・REF7707との同一視はSymantecの記載のみに依拠しており、各クラスタ側の資料は同一視を主張していない。

### 不確実性

- Earth Alux(Trend Micro, 2025-03-31)およびREF7707(Elastic, 2025-02-13)の観測期間・マルウェア群はSymantecがJewelbugとして報告した実装群と重ならないため、3者が同一クラスタであるかは未解決である。aliasのscopeはoverlappingとし、実績を相互に流用していない。
- hack-for-hireという性格付けはSymantecの評価であり、顧客・発注関係を示す直接証拠は公開されていない。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--symantec-jewelbug-2026 | Jewelbug: Crypto Fraud and Espionage | Symantec Threat Hunter Team | 2026-08-13 | https://www.security.com/threat-intelligence/jewelbug-crypto-fraud-espionage | vendor-research-report | TLP:CLEAR | 高 |
| source--trendmicro-earth-alux-2025 | The Espionage Toolkit of Earth Alux: A Closer Look at its Advanced Techniques | Trend Micro | 2025-03-31 | https://www.trendmicro.com/en_us/research/25/c/the-espionage-toolkit-of-earth-alux.html | vendor-research-report | TLP:CLEAR | 高 |
| source--elastic-ref7707-2025 | From South America to Southeast Asia: The Fragile Web of REF7707 | Elastic Security Labs | 2025-02-13 | https://www.elastic.co/security-labs/fragile-web-ref7707 | vendor-research-report | TLP:CLEAR | 高 |

## 自由記述

本プロファイルはSymantecがJewelbugの名称で報告した範囲に限定する。Earth AluxおよびREF7707の活動・マルウェア実績は、同一視の根拠がSymantecの記載のみであるため本プロファイルへ複製していない。
