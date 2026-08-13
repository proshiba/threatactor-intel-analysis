# UAC-0145 脅威アクタープロファイル

- プロファイルID: `actor--uac-0145`
- 状態: draft
- 更新日時: 2026-08-13T10:58:19Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

UAC-0145はCERT-UAが追跡するサイバー脅威クラスタで、CERT-UAはこれをUAC-0002(Sandworm、APT44、Seashell Blizzardの別名でも知られる)のサブクラスタと明示している。ウクライナを対象に、トレントトラッカーで配布するバックドア入りWindows/Officeインストーラー、Signalでの「アンチウイルス保護」偽装、侵害済みウェブサイトでの偽CAPTCHA(ClickFix)、保護アプリを装うAndroid向けAPK、そして2026年5月以降は偽の採用プロセスを通じた改変WireGuardクライアントSopraVPNの配布という、複数の初期侵害ベクターを並行して運用する。標的は政府機関と軍のほか、企業リソースへ到達しうるシステム管理者・IT専門職個人に及ぶ。

## アクター名とAlias

- 正規名: **UAC-0145**
- 初回観測: 不明
- 最終観測: 2026-07
- 活動状態: yes

Aliasなし

## 帰属

CERT-UAは2件の資料でいずれも「кластером кіберзагроз UAC-0145 (субкластер UAC-0002, також відомий як Sandworm, APT44, Seashell Blizzard)」と記載し、UAC-0145をUAC-0002のサブクラスタとして明示している。一方で、この2件の資料自体はUAC-0145の後援国やスポンサー種別を記載していない。親クラスタ側の帰属評価はSandworm Teamプロファイルが保持しており、本プロファイルへは複製しない。

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: `source--certua-6318437-uac-0145`, `source--certua-6318863-uac-0145`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | ウクライナの政府機関・軍と、企業リソースへ到達しうるIT技術者を対象に、遠隔アクセスの確保、端末・ブラウザー・メッセンジャーのデータ収集、位置情報の追跡を行う。トレント経由で侵害した端末が組織内の横展開に用いられ、中央行政機関インフラへの破壊的サイバー攻撃の条件が作られた事例も報告されている。 | 高 | `source--certua-6318437-uac-0145`, `source--certua-6318863-uac-0145` | CERT-UAは破壊的攻撃の「条件が作られた」と記載しており、本クラスタが破壊的攻撃自体を実行したとは明記していない。そのため動機はespionageのみとし、sabotageを独立した動機として立てない。 |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| UAC-0002 | part-of | CERT-UAは2026-07-15と2026-08-08の2件の資料でUAC-0145をUAC-0002のサブクラスタ(субкластер)と明示している。 | 高 | `source--certua-6318437-uac-0145`, `source--certua-6318863-uac-0145` |
| Sandworm Team | part-of | CERT-UAは親クラスタUAC-0002をSandworm、APT44、Seashell Blizzardの別名でも知られると記載している。したがってUAC-0145はSandworm Teamとして追跡されるクラスタのサブクラスタにあたる。 | 高 | `source--certua-6318437-uac-0145`, `source--certua-6318863-uac-0145` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | CERT-UAが追跡するクラスタUAC-0145。CERT-UAはUAC-0002(Sandworm、APT44、Seashell Blizzard)のサブクラスタと位置付ける。本資料群は後援国を明示していない。 |
| Capability | KALAMBUR、SUMBUR、TAMBUR、ローダーFLUIDLEECH/LOADLOOP、VBSドロッパーGHETTOVIBE、PowerShell偵察スクリプトSCOUTCURL、PythonバックドアFREAKYPOLL、ウェブインジェクトSMARTAXE、AndroidバックドアCOWARDDUCK、改変WireGuardクライアントSopraVPN。正規ツールとしてOpenSSH、TOR、RSYNC、cURLを併用する。 |
| Infrastructure | 偽CAPTCHAを配信する侵害済みウェブサイト群、クローキングサービスCloaking.House、SopraVPNを配布するSourceForgeプロジェクト、Sopra SteriaとATLAS Business Groupを騙る偽企業ドメイン、コマンド取得に悪用される正規サービスとEthereumスマートコントラクト。 |
| Victim | ウクライナの政府機関・軍と、企業リソースへ接続しうるシステム管理者・IT専門職個人。CERT-UAは通信事業者とIT企業に対して注意喚起している。 |
| Socio-political | ウクライナの国家機関と防衛関連要員、およびそこへ接続しうる技術者個人を対象とする諜報活動。中央行政機関インフラへの破壊的攻撃の前提が作られた事例が報告されている。 |

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--uac-0145-kalambur | KALAMBUR | CERT-UAがUAC-0145の既知の実装として挙げるマルウェア。Signalで「アンチウイルス保護」の導入が必要だと持ちかける社会工学と組み合わせて配布された。 | 不明 | 不明 | 高 | `source--certua-6318437-uac-0145` |
| malware--uac-0145-sumbur | SUMBUR | CERT-UAがUAC-0145の既知の実装として挙げるマルウェア。KALAMBUR・TAMBURと併記されている。 | 不明 | 不明 | 高 | `source--certua-6318437-uac-0145` |
| malware--uac-0145-tambur | TAMBUR | CERT-UAがUAC-0145の既知の実装として挙げるマルウェア。KALAMBUR・SUMBURと併記されている。 | 不明 | 不明 | 高 | `source--certua-6318437-uac-0145` |
| malware--uac-0145-ghettovibe | GHETTOVIBE | 偽CAPTCHA(ClickFix)で利用者に実行させるPowerShellコマンドが設置するVBSファイル。スタートアップ(Startup)ディレクトリへ保存され自動実行される。検体名は「Copilot Agent.vbs」「Work Copilot.vbs」。 | 不明 | 不明 | 高 | `source--certua-6318437-uac-0145` |
| malware--uac-0145-scoutcurl | SCOUTCURL | 攻撃対象の重要度を判定するために後続で投下されるPowerShellスクリプト。コンピューターの基本情報、導入プログラム、ファイル、ブラウザーデータ等を収集して外部へ送信する。検体名は「reshV1_2.ps1」。 | 不明 | 不明 | 高 | `source--certua-6318437-uac-0145` |
| malware--uac-0145-fluidleech | FLUIDLEECH | 「ウイルス」除去ツールを装ったローダー。ESET AV Removerを騙る実行ファイルにupdatus.exeとして内包された形で確認されている。 | 不明 | 不明 | 高 | `source--certua-6318437-uac-0145` |
| malware--uac-0145-loadloop | LOADLOOP | CERT-UAがFLUIDLEECHと並べて挙げるローダー。検体名は「sl3.exe」。 | 不明 | 不明 | 高 | `source--certua-6318437-uac-0145` |
| malware--uac-0145-freakypoll | FREAKYPOLL | インシデント対応を実施した被害端末から発見されたPythonバックドア。コンパイル済みバイトコード(.pyc)の形で配置される。検体名は「update.cpython-314.pyc」で、%LOCALAPPDATA%\SystemHelper\python\配下に置かれる。 | 不明 | 不明 | 高 | `source--certua-6318437-uac-0145` |
| malware--uac-0145-smartaxe | SMARTAXE | 侵害済みウェブサイトへ設置され、訪問者に表示するコンテンツ(偽CAPTCHA等)を差し替えるJavaScript。遠隔リソースのドメイン名を、コード内に指定したコントラクトアドレスと関数セレクタに対するEthereumスマートコントラクト呼び出し(eth_call)で動的に取得する点が特徴。検体名は「wp-header.js」。 | 2026-06 | 2026-07 | 高 | `source--certua-6318437-uac-0145` |
| malware--uac-0145-cowardduck | COWARDDUCK | 保護ツールを装ったAPKとしてメッセンジャー経由で配布されるAndroidバックドア。端末情報、連絡先、指定ディレクトリ(DCIM/Documents/Downloads/Pictures/Alarms)と指定拡張子(.conf/.json/.ovpn/.txt/.doc/.docx/.xls/.xlsx/.pptx/.zip/.rar)のファイル、リアルタイム位置情報を収集する。ファイル送出にはDropbox APIを使用し、コマンドとデータはimages.stockmemory.site、images.stockmemory.space、steamcommunity.comといった正規サービス上のオブジェクト(画像等)から取得する。通信はproxy.duckduckgo.com経由で行われる。 | 不明 | 不明 | 高 | `source--certua-6318437-uac-0145` |
| malware--uac-0145-sopravpn | SopraVPN | WireGuardのソースコードを改変して作成されたVPNクライアント。設定処理に非標準オプション「SymmetricKey」を追加し、その値をBASE64復号したnonce・暗号文・認証タグをAES-256-GCMで復号する。AES-256鍵には「PrivateKey」を復号した32バイト値を用いる。復号されたPowerShellコードはWireGuard本来の「runScriptCommand」機構(PostUpオプション用)へ渡されて実行される。「PrivateKey」「PublicKey」のBASE64復号も改変されており、「SymmetricKey」文字列のCRC32和をmath/randのseedとしたFisher-Yatesシャッフルで並べ替えた非標準64文字アルファベットを使う。Windowsでは復号PowerShellがタスクを登録したうえでインターネット上の追加ペイロードを取得し、LinuxではVPN経由で攻撃者基盤からcURLで追加実行ファイルを取得する。 | 2026-05 | 不明 | 高 | `source--certua-6318863-uac-0145` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--uac-0145-openssh | OpenSSH | 不正な遠隔アクセスの確保に使用される正規プログラム。ローカルネットワークポート(445、3389、22等)を攻撃者管理サーバーへフォワードし、実質的に攻撃者インフラ内へ公開する用途で用いられる。 | 不明 | 不明 | 高 | `source--certua-6318437-uac-0145` |
| tool--uac-0145-tor | TOR | OpenSSHと併用され、ポートフォワーディングによる遠隔アクセスの匿名化に使用される。 | 不明 | 不明 | 高 | `source--certua-6318437-uac-0145` |
| tool--uac-0145-rsync | RSYNC | Signal・WhatsAppの鍵やデータを窃取するプログラムが収集した情報の外部送出に使用されうると記載されている。 | 不明 | 不明 | 中 | `source--certua-6318437-uac-0145` |
| tool--uac-0145-curl | cURL | SopraVPNのLinux版が、VPN経由で攻撃者基盤から追加実行ファイルを取得する際に使用する。 | 不明 | 不明 | 高 | `source--certua-6318863-uac-0145` |

### インフラ

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| infrastructure--uac-0145-compromised-websites | 侵害済みウェブサイト群 | 偽CAPTCHA(ClickFix)を表示するために侵害された10件超のウェブリソース。CERT-UAはウェブサイトが攻撃に使われた事実自体が、CMS・コンポーネントの脆弱性、認証情報の漏えい、ウェブシェル、正規スクリプトの改変、サーバー上のバックドア等のいずれかによる侵害を示すと注意喚起している。 | 2026-06 | 2026-07 | 高 | `source--certua-6318437-uac-0145` |
| infrastructure--uac-0145-cloaking-house | Cloaking.House | トラフィックを条件で振り分け、訪問者へ別のHTMLページを表示・iframe化・リダイレクトできる正規サービス。UAC-0145は標準機能に加えて独自コードSMARTAXEを併用している。 | 2026-06 | 2026-07 | 高 | `source--certua-6318437-uac-0145` |
| infrastructure--uac-0145-sourceforge-hosting | SourceForge上のSopraVPN配布プロジェクト | 改変WireGuardクライアントSopraVPNを配布するために作成されたSourceForgeプロジェクト(soprabulgariavpn、sopravpn)。偽企業サイト上の「Corporate VPN on Sourceforge」ボタンからリンクされる。 | 2026-05 | 不明 | 高 | `source--certua-6318863-uac-0145` |
| infrastructure--uac-0145-fake-company-domains | 偽IT企業ドメイン群 | 国際IT企業Sopra Steriaの地域オフィスを騙るsoprasteria-bg[.]com(2026-07-16)、soprasteriabg[.]com(2026-05-14)と、ATLAS Business Groupを騙るatlasgroup-ua[.]com(2026-02-10)。Sopra Steriaの正規ドメインはsoprasteria[.]comおよびsoprasteria[.]bg。 | 2026-02 | 2026-07 | 高 | `source--certua-6318863-uac-0145` |

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 偽の採用プロセスによる社会工学と改変WireGuardクライアントSopraVPNの配布 | cyber-espionage | 2026-05 | 不明 | 2026-08-08 | target--uac-0145--country--ukraine, target--uac-0145--role--system-administrator, target--uac-0145--sector--information-technology, target--uac-0145--sector--telecommunications | malware--uac-0145-sopravpn | ttp--uac-0145-t1027, ttp--uac-0145-t1053-005, ttp--uac-0145-t1059-001, ttp--uac-0145-t1105, ttp--uac-0145-t1204-002, ttp--uac-0145-t1566-003, ttp--uac-0145-t1583-001, ttp--uac-0145-t1585-001, ttp--uac-0145-t1587-001, ttp--uac-0145-t1589-002, ttp--uac-0145-t1608-001, ttp--uac-0145-t1656 | victim--activity-rule--78b1925bf226403f16ea, victim--uac-0145-it-specialists-recruitment | 求人サイト上で候補者の履歴書を事前に調査したうえで、IT企業(例: ATLAS Business Group)を名乗って接触する。対象は通常システム管理者またはIT専門職である。最初のやり取りはサイト内チャットで行われ、その後Telegram等の連絡先が提示される。Telegramでは、あるプロジェクト(確認された事例ではSopra Steria Bulgaria)の一次選考を担当するというHR担当者との面談が行われ、勤務形態や英語力の確認とZoom会議のリンク提示が行われる。Zoom会議は実際に開催され、30〜35歳の男性が英語で対応する。並行して、技術面接に関する追加指示が電子メールで送られ、テスト課題の実施と称して「企業」VPNへWireGuard(Linux/Windows)で接続するための設定ファイルと、作業中の随伴用として別のZoom会議リンクが提供される。送信元アドレスmike.weitzman@soprasteria-bg[.]comは国際IT企業Sopra Steriaの地域オフィスを騙っている(正規ドメインはsoprasteria[.]com、soprasteria[.]bg)。提供された設定ファイルではVPN接続時にエラーが発生するため、攻撃者はSourceForge上に置いた独自の適応版VPNクライアント「SopraVPN」のダウンロードを勧める。リンクは「企業」の公式サイトsoprasteria-bg[.]com上の「Corporate VPN on Sourceforge」ボタンにある。 | 高 | `source--certua-6318863-uac-0145` |
| 2026年7月時点の初期侵害ベクター群: トレント配布、Signal、ClickFix、Android | cyber-espionage | 2026-03 | 2026-07 | 2026-07-15 | target--uac-0145--country--ukraine, target--uac-0145--sector--defense, target--uac-0145--sector--government | malware--uac-0145-kalambur, malware--uac-0145-sumbur, malware--uac-0145-tambur, malware--uac-0145-ghettovibe, malware--uac-0145-scoutcurl, malware--uac-0145-fluidleech, malware--uac-0145-loadloop, malware--uac-0145-freakypoll, malware--uac-0145-smartaxe, malware--uac-0145-cowardduck | ttp--activity-rule--2faf5da270a809926a8c, ttp--activity-rule--3cc75c9b7f23052570a6, ttp--uac-0145-t1005, ttp--uac-0145-t1027, ttp--uac-0145-t1048, ttp--uac-0145-t1059-001, ttp--uac-0145-t1059-005, ttp--uac-0145-t1082, ttp--uac-0145-t1102, ttp--uac-0145-t1105, ttp--uac-0145-t1204-002, ttp--uac-0145-t1204-004, ttp--uac-0145-t1547-001, ttp--uac-0145-t1566-003, ttp--uac-0145-t1567-002, ttp--uac-0145-t1572, ttp--uac-0145-t1584-004 | victim--activity-rule--d4867e4a4ff96231fa56, victim--uac-0145-central-executive-authority | CERT-UAがウクライナのサイバーセキュリティ確保主体と連携して継続実施しているUAC-0145調査の、2026年7月時点での初期侵害ベクターまとめ。数年にわたり主要な手段の一つだったのは、トレントトラッカーからバックドア入りのWindowsおよびMicrosoft Officeインストーラーを利用者自身が導入する「受動的」侵害である。その後、とりわけ軍人を対象として、Signalで「アンチウイルス保護」の導入を持ちかける手口が拡大した。実行前に長時間の対話が行われ、指示の実行に対して金銭的報酬が提示される場合もある。この経路ではKALAMBUR、SUMBUR、TAMBURが用いられ、遠隔アクセスは主にOpenSSHとTORによるローカルポート(445、3389、22)のフォワーディングで確保された。Signal・WhatsAppの鍵とデータを窃取するプログラムも広まり、送出にはRSYNCが使用されうる。2026年春から夏にかけては、侵害済みウェブサイトで偽CAPTCHAを表示し、通過のためと称してPowerShellコマンドをターミナルで実行させるClickFixによる感染が確認された。このコマンドは例としてスタートアップへVBSファイルを保存するもので、その一種がGHETTOVIBEである。後続で投下されるSCOUTCURLが端末情報を収集して攻撃対象の重要度を判定する。ローダーとしてはFLUIDLEECHとLOADLOOPが、対応実施済みの被害端末からはPythonバックドアFREAKYPOLLが確認された。6〜7月にはClickFixの実装を10件超の侵害済みウェブリソースで詳細解析し、Cloaking.Houseの標準機能に加えて独自コードSMARTAXEが用いられていること、SMARTAXEが遠隔リソースのドメイン名をEthereumスマートコントラクトのeth_call呼び出しで動的に取得することが判明した。Androidに対しては、保護ツールを装ったAPKとして配布されるバックドアCOWARDDUCKが使用され、Dropbox APIでのファイル送出と、正規サービス上のオブジェクトを介したコマンド取得を行う。 | 高 | `source--certua-6318437-uac-0145` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| 偽の採用プロセスによる社会工学と改変WireGuardクライアントSopraVPNの配布 | UAC-0145 | COWARDDUCK, FREAKYPOLL, SCOUTCURL, SopraVPN | T1027 Obfuscated Files or Information, T1053.005 Scheduled Task/Job: Scheduled Task, T1059.001 Command and Scripting Interpreter: PowerShell, T1105 Ingress Tool Transfer, T1204.002 User Execution: Malicious File, T1566.003 Phishing: Spearphishing via Service, T1583.001 Acquire Infrastructure: Domains, T1585.001 Establish Accounts: Social Media Accounts, T1587.001 Develop Capabilities: Malware, T1589.002 Gather Victim Identity Information: Email Addresses, T1608.001 Stage Capabilities: Upload Malware, T1656 Impersonation | 偽IT企業ドメイン群, SourceForge上のSopraVPN配布プロジェクト | ウクライナ, システム管理者・IT専門職, IT企業, 通信事業者 | 被害事例: 偽の採用プロセスによる社会工学と改変WireGuardクライアントSopraVPNの配布, 被害事例: 偽の採用プロセスを通じたシステム管理者・IT専門職の侵害 | 高 |
| 2026年7月時点の初期侵害ベクター群: トレント配布、Signal、ClickFix、Android | UAC-0145 | COWARDDUCK, FLUIDLEECH, FREAKYPOLL, GHETTOVIBE, KALAMBUR, LOADLOOP, SCOUTCURL, SMARTAXE, SopraVPN, SUMBUR, TAMBUR | T1059.001 PowerShell, T1204.004 Malicious Copy and Paste, T1005 Data from Local System, T1027 Obfuscated Files or Information, T1048 Exfiltration Over Alternative Protocol, T1059.001 Command and Scripting Interpreter: PowerShell, T1059.005 Command and Scripting Interpreter: Visual Basic, T1082 System Information Discovery, T1102 Web Service, T1105 Ingress Tool Transfer, T1204.002 User Execution: Malicious File, T1204.004 User Execution: Malicious Copy and Paste, T1547.001 Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder, T1566.003 Phishing: Spearphishing via Service, T1567.002 Exfiltration Over Web Service: Exfiltration to Cloud Storage, T1572 Protocol Tunneling, T1584.004 Compromise Infrastructure: Server | Cloaking.House, 侵害済みウェブサイト群 | ウクライナ, 国防・軍, 政府機関 | 被害事例: 2026年7月時点の初期侵害ベクター群: トレント配布、Signal、ClickFix、Android, 被害事例: トレント経由の侵害端末を起点とした中央行政機関インフラへの破壊的攻撃準備 | 高 |

CERT-UAはウクライナの主要なサイバーセキュリティ確保主体と連携し、長期にわたりUAC-0145を対象とした調査を実施してきた。数年にわたって主要な初期アクセス手段の一つだったのは、トレントトラッカーからバックドア入りのWindowsおよびMicrosoft Officeインストーラーを利用者自身が導入する「受動的」侵害である。その後、とりわけ軍人を対象としてSignal経由の配布が拡大し、2026年春から夏にかけてClickFixによる感染が確認された。2026年5月以降は求人・採用プロセスを悪用する社会工学が加わっている。

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | ウクライナ | CERT-UAはウクライナのサイバーセキュリティ確保主体と連携してUAC-0145を継続調査しており、被害はウクライナ国内で観測されている。中央行政機関のインフラに対する破壊的サイバー攻撃の前提条件が作られた事例が報告されている。 | 2026-03 | 2026-07 | 高 | `source--certua-6318437-uac-0145`, `source--certua-6318863-uac-0145` |
| sectors | 国防・軍 | Signalでの「アンチウイルス保護」導入を装った配布は、とりわけ軍人を対象として拡大したとCERT-UAが記載している。 | 不明 | 不明 | 高 | `source--certua-6318437-uac-0145` |
| sectors | 政府機関 | トレント経由で侵害された端末が組織内ネットワークでの присутність確保と横展開に利用され、ウクライナ中央行政機関のインフラに対する破壊的攻撃の条件が作られた事例が少なくとも1件記載されている。 | 不明 | 不明 | 高 | `source--certua-6318437-uac-0145` |
| sectors | IT企業 | 偽の求人・技術面接を通じてIT専門職へ接触する手口の対象。CERT-UAは通信事業者と並べてIT企業へ注意喚起している。 | 2026-05 | 不明 | 中 | `source--certua-6318863-uac-0145` |
| sectors | 通信事業者 | CERT-UAは就職過程を悪用する社会工学について、とりわけ通信事業者・プロバイダーとIT企業に対し、管理対象端末からのみ企業リソースへ接続させるよう注意喚起している。 | 2026-05 | 不明 | 中 | `source--certua-6318863-uac-0145` |
| roles | システム管理者・IT専門職 | 求人サイト上で履歴書を事前に調査したうえで接触する対象。CERT-UAは「як правило системним адміністратором/ІТ фахівцем」(通常はシステム管理者/IT専門職)と記載している。 | 2026-05 | 不明 | 高 | `source--certua-6318863-uac-0145` |

選定ロジック: ウクライナの政府機関・軍と、そこへ接続しうるIT/通信分野の技術者個人の双方を対象とする。前者は組織ネットワークへの足がかりと破壊的攻撃の前提づくり、後者は管理者権限を持つ個人端末経由での企業リソース到達を狙う。 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 偽の採用プロセスによる社会工学と改変WireGuardクライアントSopraVPNの配布 | 非公開 | aggregate | multiple-organizations | reported | target--uac-0145--country--ukraine, target--uac-0145--role--system-administrator, target--uac-0145--sector--information-technology, target--uac-0145--sector--telecommunications | malware--uac-0145-sopravpn | ttp--uac-0145-t1027, ttp--uac-0145-t1053-005, ttp--uac-0145-t1059-001, ttp--uac-0145-t1105, ttp--uac-0145-t1204-002, ttp--uac-0145-t1566-003, ttp--uac-0145-t1583-001, ttp--uac-0145-t1585-001, ttp--uac-0145-t1587-001, ttp--uac-0145-t1589-002, ttp--uac-0145-t1608-001, ttp--uac-0145-t1656 | メール／メールアカウント, VPN／リモートアクセス機器 |  | 2026-05 | 不明 | 2026-08-08 | 高 | `source--certua-6318863-uac-0145` |
| 被害事例: 2026年7月時点の初期侵害ベクター群: トレント配布、Signal、ClickFix、Android | 非公開 | aggregate | multiple-organizations | reported | target--uac-0145--country--ukraine, target--uac-0145--sector--defense, target--uac-0145--sector--government | malware--uac-0145-cowardduck, malware--uac-0145-fluidleech, malware--uac-0145-freakypoll, malware--uac-0145-ghettovibe, malware--uac-0145-kalambur, malware--uac-0145-loadloop, malware--uac-0145-scoutcurl, malware--uac-0145-smartaxe, malware--uac-0145-sumbur, malware--uac-0145-tambur | ttp--activity-rule--2faf5da270a809926a8c, ttp--activity-rule--3cc75c9b7f23052570a6, ttp--uac-0145-t1005, ttp--uac-0145-t1027, ttp--uac-0145-t1048, ttp--uac-0145-t1059-001, ttp--uac-0145-t1059-005, ttp--uac-0145-t1082, ttp--uac-0145-t1102, ttp--uac-0145-t1105, ttp--uac-0145-t1204-002, ttp--uac-0145-t1204-004, ttp--uac-0145-t1547-001, ttp--uac-0145-t1566-003, ttp--uac-0145-t1567-002, ttp--uac-0145-t1572, ttp--uac-0145-t1584-004 | エンドポイント, モバイル端末 | data-theft: Signal・WhatsAppの鍵とデータを窃取するプログラムも広まり、送出にはRSYNCが使用されうる。 | 2026-03 | 2026-07 | 2026-07-15 | 高 | `source--certua-6318437-uac-0145` |
| 被害事例: トレント経由の侵害端末を起点とした中央行政機関インフラへの破壊的攻撃準備 | 非公開 | anonymous | organization | reported | target--uac-0145--country--ukraine, target--uac-0145--sector--government |  | ttp--uac-0145-t1204-002 | 利用者端末, 組織内ローカルネットワーク, 中央行政機関のインフラ | espionage: 侵害端末を起点とした組織内ネットワークでの足がかり確保と横展開。CERT-UAはこれにより中央行政機関インフラに対する破壊的サイバー攻撃を実施する条件が作られたと記載するが、破壊的攻撃の実行自体は本資料に記載がない。 | 不明 | 不明 | 2026-07-15 | 高 | `source--certua-6318437-uac-0145` |
| 被害事例: 偽の採用プロセスを通じたシステム管理者・IT専門職の侵害 | 非公開 | aggregate | multiple-persons | reported | target--uac-0145--country--ukraine, target--uac-0145--role--system-administrator | malware--uac-0145-sopravpn | ttp--uac-0145-t1566-003, ttp--uac-0145-t1656, ttp--uac-0145-t1204-002, ttp--uac-0145-t1059-001, ttp--uac-0145-t1053-005 | IT専門職の個人端末, 企業VPN接続経路 | espionage: 改変VPNクライアント経由のPowerShell実行と追加ペイロード取得、およびWindowsではスケジュールタスクによる持続化。IT専門職の端末を経由した所属組織の企業リソースへの到達が狙われる。 | 2026-05 | 不明 | 2026-08-08 | 高 | `source--certua-6318863-uac-0145` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution | T1059.001 | PowerShell | 2026年春から夏にかけては、侵害済みウェブサイトで偽CAPTCHAを表示し、通過のためと称してPowerShellコマンドをターミナルで実行させるClickFixによる感染が確認された。 |  | activity--uac-0145-initial-access-vectors-2026 | 2026-03 | 2026-07 | 中 | `source--certua-6318437-uac-0145` |
| Execution | T1204.004 | Malicious Copy and Paste | 2026年7月時点の初期侵害ベクター群: トレント配布、Signal、ClickFix、Android |  | activity--uac-0145-initial-access-vectors-2026 | 2026-03 | 2026-07 | 中 | `source--certua-6318437-uac-0145` |
| Collection | T1005 | Data from Local System | SignalとWhatsAppの鍵およびデータを窃取するプログラムが用いられる。COWARDDUCKは指定ディレクトリと指定拡張子のファイル、連絡先、リアルタイム位置情報を収集する。 | malware--uac-0145-cowardduck | activity--uac-0145-initial-access-vectors-2026 | 2026-03 | 2026-07 | 高 | `source--certua-6318437-uac-0145` |
| Defense Evasion | T1027 | Obfuscated Files or Information | SopraVPNは実行するPowerShellをAES-256-GCMで暗号化して設定値へ埋め込み、鍵素材のBASE64も「SymmetricKey」のCRC32和をseedとしたFisher-Yatesシャッフルで並べ替えた非標準アルファベットで符号化する。FREAKYPOLLはコンパイル済みバイトコード(.pyc)で配置される。 | malware--uac-0145-sopravpn, malware--uac-0145-freakypoll | activity--uac-0145-initial-access-vectors-2026, activity--uac-0145-fake-employment-sopravpn-2026 | 2026-03 | 2026-07 | 高 | `source--certua-6318437-uac-0145`, `source--certua-6318863-uac-0145` |
| Exfiltration | T1048 | Exfiltration Over Alternative Protocol | Signal・WhatsAppから窃取した鍵とデータの送出にRSYNCが使用されうるとCERT-UAが記載している。 |  | activity--uac-0145-initial-access-vectors-2026 | 2026-03 | 2026-07 | 中 | `source--certua-6318437-uac-0145` |
| Persistence | T1053.005 | Scheduled Task/Job: Scheduled Task | Windows版SopraVPNの復号PowerShellが、スケジュールタスク(\Microsoft\Windows\ApplicationData\Microsoft)を作成してから追加ペイロードを取得する。 | malware--uac-0145-sopravpn | activity--uac-0145-fake-employment-sopravpn-2026 | 2026-05 | 不明 | 高 | `source--certua-6318863-uac-0145` |
| Execution | T1059.001 | Command and Scripting Interpreter: PowerShell | ClickFixで実行させるコマンドがスタートアップへVBSを設置し、偵察スクリプトSCOUTCURLもPowerShellで実装される。SopraVPNでは復号したPowerShellコードをWireGuardのrunScriptCommand機構へ渡して実行する。 | malware--uac-0145-scoutcurl, malware--uac-0145-sopravpn | activity--uac-0145-initial-access-vectors-2026, activity--uac-0145-fake-employment-sopravpn-2026 | 2026-03 | 2026-07 | 高 | `source--certua-6318437-uac-0145`, `source--certua-6318863-uac-0145` |
| Execution | T1059.005 | Command and Scripting Interpreter: Visual Basic | GHETTOVIBEはVBSファイルとして配置され、Windowsのスクリプトホストで実行される。 | malware--uac-0145-ghettovibe | activity--uac-0145-initial-access-vectors-2026 | 2026-03 | 2026-07 | 高 | `source--certua-6318437-uac-0145` |
| Discovery | T1082 | System Information Discovery | SCOUTCURLがコンピューターの基本特性、導入プログラム、ファイル、ブラウザーデータ等を収集して攻撃対象の重要度を判定する。 | malware--uac-0145-scoutcurl | activity--uac-0145-initial-access-vectors-2026 | 2026-03 | 2026-07 | 高 | `source--certua-6318437-uac-0145` |
| Command and Control | T1102 | Web Service | COWARDDUCKはimages.stockmemory.site、images.stockmemory.space、steamcommunity.comといった正規サービス上のオブジェクトからコマンドやデータを取得し、通信はproxy.duckduckgo.com経由で行う。SMARTAXEは遠隔リソースのドメイン名をEthereumスマートコントラクトのeth_call呼び出しで解決する。 | malware--uac-0145-cowardduck, malware--uac-0145-smartaxe | activity--uac-0145-initial-access-vectors-2026 | 2026-03 | 2026-07 | 高 | `source--certua-6318437-uac-0145` |
| Command and Control | T1105 | Ingress Tool Transfer | ClickFix経路ではSCOUTCURL等を後続で投下し、SopraVPN経路ではWindowsがインターネット上から、LinuxがVPN経由で攻撃者基盤からcURLで追加実行ファイルを取得する。 | malware--uac-0145-scoutcurl, malware--uac-0145-sopravpn | activity--uac-0145-initial-access-vectors-2026, activity--uac-0145-fake-employment-sopravpn-2026 | 2026-03 | 2026-07 | 高 | `source--certua-6318437-uac-0145`, `source--certua-6318863-uac-0145` |
| Execution | T1204.002 | User Execution: Malicious File | トレントトラッカーで配布されるバックドア入りWindows/Microsoft Officeインストーラー、保護ツールを装ったAPK、改変VPNクライアントSopraVPNのいずれも、利用者自身の実行を必要とする。 | malware--uac-0145-cowardduck, malware--uac-0145-sopravpn | activity--uac-0145-initial-access-vectors-2026, activity--uac-0145-fake-employment-sopravpn-2026 | 2026-03 | 2026-07 | 高 | `source--certua-6318437-uac-0145`, `source--certua-6318863-uac-0145` |
| Execution | T1204.004 | User Execution: Malicious Copy and Paste | 侵害済みウェブサイトで偽CAPTCHAを表示し、通過のためと称してPowerShellコマンドをコピーしてターミナルで実行させる(ClickFix)。 | malware--uac-0145-ghettovibe | activity--uac-0145-initial-access-vectors-2026 | 2026-03 | 2026-07 | 高 | `source--certua-6318437-uac-0145` |
| Persistence | T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder | %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\Copilot Agent.vbs をスタートアップへ配置して自動実行を確保する。 | malware--uac-0145-ghettovibe | activity--uac-0145-initial-access-vectors-2026 | 2026-03 | 2026-07 | 高 | `source--certua-6318437-uac-0145` |
| Initial Access | T1566.003 | Phishing: Spearphishing via Service | Signalで「アンチウイルス保護」の導入が必要だと持ちかけ、実行に先立って長時間の対話を行い、指示の実行に対して金銭的報酬を提示する場合もある。求人経路ではサイト内チャットからTelegramへ誘導する。 |  | activity--uac-0145-initial-access-vectors-2026, activity--uac-0145-fake-employment-sopravpn-2026 | 2026-03 | 2026-07 | 高 | `source--certua-6318437-uac-0145`, `source--certua-6318863-uac-0145` |
| Exfiltration | T1567.002 | Exfiltration Over Web Service: Exfiltration to Cloud Storage | COWARDDUCKはファイルの送出にDropboxのAPIを使用する。 | malware--uac-0145-cowardduck | activity--uac-0145-initial-access-vectors-2026 | 2026-03 | 2026-07 | 高 | `source--certua-6318437-uac-0145` |
| Command and Control | T1572 | Protocol Tunneling | OpenSSHとTORでローカルネットワークポート(445、3389、22)を攻撃者管理サーバーへフォワードし、攻撃者インフラ内へ公開する形で不正な遠隔アクセスを確保する。 |  | activity--uac-0145-initial-access-vectors-2026 | 2026-03 | 2026-07 | 高 | `source--certua-6318437-uac-0145` |
| Resource Development | T1583.001 | Acquire Infrastructure: Domains | Sopra Steriaの地域オフィスを騙るsoprasteria-bg[.]com等と、ATLAS Business Groupを騙るatlasgroup-ua[.]comを取得し、偽の採用活動の正当性を演出している。 |  | activity--uac-0145-fake-employment-sopravpn-2026 | 2026-02 | 2026-07 | 高 | `source--certua-6318863-uac-0145` |
| Resource Development | T1584.004 | Compromise Infrastructure: Server | 偽CAPTCHAを表示させるために10件超のウェブリソースを侵害し、正規スクリプトの改変やウェブシェル設置等によりコンテンツ差し替えの足場を得ている。 |  | activity--uac-0145-initial-access-vectors-2026 | 2026-06 | 2026-07 | 高 | `source--certua-6318437-uac-0145` |
| Resource Development | T1585.001 | Establish Accounts: Social Media Accounts | 求人サイトの企業アカウント、Telegramアカウント(@Sales_ManagerABG)、メールアドレス(mike.weitzman@soprasteria-bg[.]com、alex.boichenkoit@ukr[.]net)を用意し、HR担当者を名乗る人物がZoom面接まで実施する。 |  | activity--uac-0145-fake-employment-sopravpn-2026 | 2026-05 | 不明 | 高 | `source--certua-6318863-uac-0145` |
| Resource Development | T1587.001 | Develop Capabilities: Malware | WireGuardのソースコードを改変し、非標準の設定オプションSymmetricKeyと独自BASE64アルファベットを追加した独自VPNクライアントをビルドしている。 | malware--uac-0145-sopravpn | activity--uac-0145-fake-employment-sopravpn-2026 | 2026-05 | 不明 | 高 | `source--certua-6318863-uac-0145` |
| Reconnaissance | T1589.002 | Gather Victim Identity Information: Email Addresses | 求人サイト上で候補者の履歴書を事前に調査したうえで接触する。 |  | activity--uac-0145-fake-employment-sopravpn-2026 | 2026-05 | 不明 | 中 | `source--certua-6318863-uac-0145` |
| Resource Development | T1608.001 | Stage Capabilities: Upload Malware | 改変WireGuardクライアントSopraVPNをSourceForgeプロジェクトへ配置し、偽企業サイトの「Corporate VPN on Sourceforge」ボタンから誘導する。 | malware--uac-0145-sopravpn | activity--uac-0145-fake-employment-sopravpn-2026 | 2026-05 | 不明 | 高 | `source--certua-6318863-uac-0145` |
| Defense Evasion | T1656 | Impersonation | 国際IT企業Sopra SteriaのブルガリアオフィスとIT企業ATLAS Business Groupを騙り、求人・HR面談・技術面接という一連の採用プロセスを演じる。Zoom会議には実在の人物が英語で対応する。 |  | activity--uac-0145-fake-employment-sopravpn-2026 | 2026-05 | 不明 | 高 | `source--certua-6318863-uac-0145` |

## IOC／artifact概要

- IOC値: 56件
- IOC観測: 56件
- 複数攻撃で観測: 0件
- 要レビュー候補: 2件
- 非IOC artifact観測: 21件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| UAC-0145はCERT-UAがUAC-0002(Sandworm、APT44、Seashell Blizzard)のサブクラスタとして明示するクラスタであり、ウクライナを対象に複数の初期侵害ベクターを並行運用している。 | 高 | `source--certua-6318437-uac-0145`, `source--certua-6318863-uac-0145` |  |
| 2026年5月以降、求人・採用プロセスを悪用してシステム管理者とIT専門職個人へ接触し、改変WireGuardクライアントSopraVPNを導入させる手口が継続している。 | 高 | `source--certua-6318863-uac-0145` |  |
| 初期侵害は単一の手口ではなく、トレント配布、Signal、ClickFix、Android向け偽保護アプリ、偽採用プロセスが並行して運用されている。 | 高 | `source--certua-6318437-uac-0145`, `source--certua-6318863-uac-0145` |  |

### 情報ギャップ

- UAC-0145としての追跡開始時期をCERT-UAが記載していないため、actor.first_seenはunknownである。
- トレント経由の侵害は「数年にわたり」とのみ記載され、開始時期と件数が不明である。
- 被害組織名、被害件数、被害の広がりが2件の資料のいずれにも記載されていない。
- SopraVPNが取得する追加ペイロードの実体が資料に記載されていない。
- CERT-UA以外の独立した一次資料をまだ確認できていない。

### 不確実性

- UAC-0002とUAC-0145のスコープ差(サブクラスタの境界)をCERT-UAは定義していない。Sandworm Team/APT44/Seashell Blizzardの各ベンダー定義との対応も明示されていない。
- KALAMBUR、SUMBUR、TAMBURの機能と観測期間が資料に記載されていない。
- 通信事業者とIT企業は注意喚起の名宛人として挙げられており、被害が確認された業種として明示されているわけではない。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--certua-6318437-uac-0145 | Вектори первинної компрометації UAC-0145 станом на липень 2026 року | CERT-UA | 2026-07-15 | https://cert.gov.ua/article/6318437 | government-advisory | TLP:CLEAR | 高 |
| source--certua-6318863-uac-0145 | Соціальна інженерія у виконанні UAC-0145: компрометація у процесі працевлаштування | CERT-UA | 2026-08-08 | https://cert.gov.ua/article/6318863 | government-advisory | TLP:CLEAR | 高 |

## 自由記述

CERT-UAは、ウェブサイトが攻撃に使われた事実自体が、CMSやコンポーネントの脆弱性、認証情報の漏えい、ウェブシェル、外部プラグイン、正規スクリプトとウェブページの改変、サーバー上のバックドア等のいずれかによる侵害を示すとして、ウェブサイト管理者とホスティング事業者に対応を求めている。
