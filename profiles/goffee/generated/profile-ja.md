# GOFFEE 脅威アクタープロファイル

- プロファイルID: `actor--goffee`
- 状態: draft
- 更新日時: 2026-09-20T12:23:31Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

GOFFEE(BI.ZONE 呼称: Paper Werewolf)は、少なくとも2022年初頭からロシア連邦の組織を標的とする脅威グループである。主たる動機はサイバースパイ活動であり、標的型フィッシングを一貫した初期アクセス手段として、被害インフラへ長期に滞在する。出身国と後援関係はいずれの一次資料でも特定されていない。道具立ての入れ替えが速く、悪性IISモジュール Owowa(2022年5月〜2023年夏)、PowerShell 製の非公開 Mythic エージェント PowerTaskel(2023年初頭〜)、PowerModul とそのペイロードである FlashFileGrabber・USB Worm(2024年)、バイナリRAT の WarpRAT と軽量な PowerTaskel v2(2026年)と推移している。Kaspersky は2026年の報告で約120の被害組織をロシア連邦で確認し、主たる業種を機械製造・製造業・政府部門としている。

## アクター名とAlias

- 正規名: **GOFFEE**
- 初回観測: 2022
- 最終観測: 2026-03
- 活動状態: yes

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Paper Werewolf | BI.ZONE | exact | 高 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026`, `source--bizone-paper-werewolf-destructive-2024` | 両方向の明示がある。Kaspersky は「Киберпреступная APT-группа GOFFEE (также известная как Paper Werewolf)」と述べ、BI.ZONE は「the Paper Werewolf cluster (also known as GOFFEE)」と述べる。両社が同一の技術的特徴(UserCache.ini / UserCache.ini.hta / UserCacheHelper.lnk.js の組、HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows の LOAD 値による永続化、api/texts/<computer>_<user>_<serial> 形式のC2 URL、CountRuns/Interval/Module のXML応答)を独立に記述している点も整合する。 |

## 帰属

3本の一次資料のいずれも GOFFEE / Paper Werewolf の出身国・後援関係を述べていない。Kaspersky は「Киберпреступная APT-группа」(サイバー犯罪的なAPTグループ)と表現し、本キャンペーンを過去の GOFFEE キャンペーンへ結び付ける帰属のみを「С высокой степенью уверенности」(高確度)で行う。その根拠は、GOFFEE へ既に帰属済みの WarpRAT 検体(0x0d1dd7a62f3ea0d0fbeea905a48ae8794f49319ee0c34f15a3a871899404bf05)と本キャンペーンの検体(7b3bd2903f30597499bf8dc717918bb3)の設定データ生成手続きのコード類似、過去の PowerTaskel 検体(29690F86D68F34009CC2D9C0D2E28EEA)と本キャンペーンの検体(F5194119A62590D7DDDC1F677FB470D0)のコード類似、および GOFFEE のキャンペーンに典型的な技術セット(標的型フィッシング、キャンペーンごとの専用ドメイン、C2 秘匿のためのリバースプロキシの多用、長期滞在、選別された被害者層)である。Kaspersky は2025年の報告でも同様に、PowerTaskel の使用、HTAとスクリプト群、パッチ適用済み explorer.exe とシェルコードの類似、被害者像の一致を根拠に 「we can attribute this campaign to GOFFEE with a high degree of confidence」と述べている。BI.ZONE も国家帰属を行わず、クラスタ名による追跡にとどめている。したがって本プロファイルは帰属国を空とし、sponsor_type を unknown とする。

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: `source--kaspersky-goffee-warprat-powertaskel-v2-2026`, `source--kaspersky-goffee-recent-attacks-2025`, `source--bizone-paper-werewolf-destructive-2024`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | Kaspersky は「Основная мотивация группы — кибершпионаж」(本グループの主たる動機はサイバースパイ活動である)と明記する。BI.ZONE も Paper Werewolf を espionage cluster として扱う。 | 高 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026`, `source--bizone-paper-werewolf-destructive-2024` | 両社が独立に諜報目的と評価している。 |
| destruction | BI.ZONE は「While primarily committed to cyber espionage, such clusters can ruin the operation of target infrastructures simply out of spite, once their primary goal is achieved」と述べ、PsExec 経由の cmd.exe /c 'shutdown /r /f /t 5 && reg delete HKEY_LOCAL_MACHINE\SYSTEM /f && reg delete HKEY_LOCAL_MACHINE\SOFTWARE /f' によるレジストリ破壊と再起動、および net user によるアカウントのパスワード変更で被害組織の運用を妨害した事例を1件記録している。 | 中 | `source--bizone-paper-werewolf-destructive-2024` | BI.ZONE 単独の観測かつ「a case」と単数で述べられる1事例であるため medium とした。Kaspersky は破壊行為に言及していない。なお Kaspersky は「атакующие способны развернуть любое вредоносное ПО в скомпрометированной корпоративной среде, что потенциально позволяет им решать и другие задачи — такие как вымогательство, кража средств или скрытый майнинг」として恐喝・金銭窃取・マイニングの潜在的可能性に触れるが、これは能力に関する推論であり観測された動機ではないためfinancial 系の動機は追加しない。 |

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | GOFFEE(BI.ZONE 呼称: Paper Werewolf)。少なくとも2022年初頭から活動する、ロシア連邦の組織を標的とする脅威グループ。いずれの一次資料も出身国・後援関係を述べていない。Kaspersky は過去に HeartlessSoul との関連を確認しており、両グループの背後に同一の攻撃者がいると中程度の確度で評価するが、道具立ては大きく異なるとしている。 |
| Capability | 自製マルウェア: 悪性IISモジュール Owowa、PowerShell製の非公開Mythicエージェント PowerTaskel とその後継 PowerTaskel v2、PowerShellダウンローダ PowerModul(BI.ZONE 呼称 PowerRAT に対応)、リムーバブルメディアからのファイル窃取 FlashFileGrabber/FlashFileGrabberOffline、リムーバブルメディア感染用 USB Worm、バイナリRAT の WarpRAT(別名 EchoGather RAT)、BI.ZONE が挙げる QwakMyAgent。既製品は Mythic フレームワークとその Poseidon エージェント、Chisel、PsExec、Gophish、Inno Setup。Kaspersky は攻撃準備に AI を含む自動化手段を用いると述べる。 |
| Infrastructure | キャンペーンごとに入れ替える .online / .site / .com の短命ドメイン群と VPS。C2 の所在を隠すためにリバースプロキシサーバを多用する。WarpRAT は 443/TCP・TLS・POST を用い、sleepTime と anti-VM を設定で持つ。PowerModul は http://<C2>/api/texts/<computer>_<user>_<disk-serial> 形式で識別子をURLへ付与する。 |
| Victim | ロシア連邦の組織が中心。Kaspersky の2026年の報告では約120の被害組織をロシア連邦で確認し、CIS諸国で数件、EUで単発の被害を確認している(EUへの攻撃は偶発的と評価)。業種は機械製造・製造業・政府部門(2026年)、マスメディアと通信・建設・政府機関・エネルギー(2024年後半)、政府・エネルギー・金融・メディアほか(BI.ZONE)。 |
| Socio-political | 諜報目的が主であり、達成後に被害インフラの運用を妨害した事例が1件ある。いずれの一次資料も国家との関係を述べていないため、地政学的な位置付けは未確定である。 |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-09-20T12:23:31Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | GOFFEE | canonical-name | 高 |  | https://securelist.com/goffee-apt-new-attacks/116139/ |
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
| malware--goffee-owowa | Owowa | IIS へ導入する悪性モジュール。Kaspersky は「Starting in May 2022 and up until summer of 2023, GOFFEE deployed modified Owowa (malicious IIS module) in their attacks」と述べる。BI.ZONE は「a malicious IIS module Owowa that enables them to retrieve credentials during user authorization in the Outlook Web Access (OWA) service」とし、窃取データは HashSet としてメモリ上に保持されると説明する。特定のユーザー名をリクエストヘッダへ与えると、Base64 で符号化したデータ集合を返す、あるいは復号後のデータを削除して RSA 暗号化した Ok 文字列を返すモジュールが存在する。 | 2022-05 | 2023-08 | 高 | `source--kaspersky-goffee-recent-attacks-2025`, `source--bizone-paper-werewolf-destructive-2024` |
| malware--goffee-powertaskel | PowerTaskel | PowerShell で書かれた非公開の Mythic エージェント。Kaspersky は「We have dubbed the non-public PowerShell Mythic agent delivered via a mail-based infection chain since early 2023, as PowerTaskel」と述べる。機能は2つで、標的環境の情報を checkin メッセージとして C2 へ送ること、get_tasking 要求への応答として受け取った PowerShell スクリプトとコマンドを task として実行することである。要求のペイロードは PowerShell オブジェクトを XML へ直列化し、検体ごとに固有の1バイト鍵で XOR してから Base64 化する。Kaspersky は設定パラメータの命名と並び順から、公開の Medusa Mythic エージェント(元は Python)から派生した可能性が高いと評価する。 | 2023 | 2024-12 | 高 | `source--kaspersky-goffee-recent-attacks-2025`, `source--bizone-paper-werewolf-destructive-2024` |
| malware--goffee-powertaskel-v2 | PowerTaskel v2 | 軽量な PowerShell 製 Mythic エージェント。Kaspersky は PowerTaskel の進化形と評価し、便宜的に PowerTaskel v2 と呼称している(「второй — легкий Mythic-агент на базе PowerShell, который, по нашей оценке, представляет собой эволюцию бэкдора PowerTaskel (мы условно назвали эту версию PowerTaskel v2)」)。get_tasking / post_response 形式で C2 と対話し、サーバはコマンド名だけでなく実行に必要なコード自体を送る。 | 2026-03 | 2026-03 | 高 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026` |
| malware--goffee-warprat | WarpRAT | バイナリ形式のリモートアクセス型トロイの木馬。Kaspersky は「широко известный бинарный WarpRAT (известный также как EchoGather RAT)」と述べる。GOFFEE はキャンペーンごとに多数の検体を生成しており、2026年3月のキャンペーンの検体は C2 を ntpsum[.]online、C2_port を 443、useSSL を true、method を POST、sleepTime を 314(± 15 の揺らぎ)、useAntiVM を 1 とする設定を持っていた。 | 2026-03 | 2026-03 | 高 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026` |
| malware--goffee-powermodul | PowerModul | 追加の PowerShell スクリプトを C2 から受領して実行する PowerShell スクリプト。Kaspersky は初出を2024年初頭とし、当初は PowerTaskel を導入するための小さな部品と見なしていたが、独自プロトコル、異なるペイロード種別、PowerTaskel とは別の C2 を持つことから別ファミリへ分類したと述べる。C2 へは http://<C2>/api/texts/{computer_name}_{username}_{serial_number} の形式で識別子を付与して接続し、応答は Base64 符号化スクリプトを含む XML(Module、CountRuns、Interval)である。OfflineWorker() 関数は事前に埋め込まれた文字列を復号して実行し、FlashFileGrabber のコードを保持する事例が観測されている。ペイロードは PowerTaskel、FlashFileGrabber、USB Worm である。 | 2024 | 2024-12 | 高 | `source--kaspersky-goffee-recent-attacks-2025`, `source--bizone-paper-werewolf-destructive-2024` |
| malware--goffee-flashfilegrabber | FlashFileGrabber | リムーバブルメディアからファイルを窃取する道具。2種類が確認されている。FlashFileGrabberOffline は対象拡張子のファイルをローカルディスクへ複写し、%TEMP%\CacheStore\connect\<VolumeSerialNumber>\ 配下へ保存する。同階層の ftree.db に元ファイルの絶対パス、サイズ、最終アクセス日時と更新日時を保存し、%AppData%\internal_profiles.db に当該メタデータの MD5 を保存して同一ファイルの重複複写を避ける。対象拡張子は .7z .conf .csv .doc .docx .dwg .heic .hgt .html .jpeg .jpg .kml .log .lrf .mdb .ods .odt .ovpn .pdf .png .pptx .ps1 .rar .rtf .scr .thm .txt .xlm .xls .xlsm .xlsx .xml .zip である。FlashFileGrabber は同等の機能に加え、収集したファイルを C2 へ送信できる。 | 2024-07 | 2024-12 | 高 | `source--kaspersky-goffee-recent-attacks-2025` |
| malware--goffee-usb-worm | USB Worm | リムーバブルメディアを PowerModul の複製で感染させる。元ファイルを拡張子を保ったままランダムな名前へ改名して Hidden 属性を与え、PowerModul を含む UserCache.ini を同じフォルダへ複写する。PowerModul 起動用の VBS とバッチファイル、および元の文書名を持つショートカットを隠しファイルとして作成し、ショートカットには元ファイルの拡張子に応じた shell32.dll のアイコンを割り当てて偽装する。ショートカットに置き換える文書は LastAccessTime の新しい順に最大5件へ制限される。 | 2024-07 | 2024-12 | 高 | `source--kaspersky-goffee-recent-attacks-2025` |
| malware--goffee-qwakmyagent | QwakMyAgent | BI.ZONE が GOFFEE/Paper Werewolf の自製 Mythic フレームワーク用エージェントとして PowerTaskel と並べて挙げる名称。原文は「we suppose that it involves a Mythic framework agent developed by the adversaries, known as PowerTaskel and QwakMyAgent」と述べる。 | 不明 | 不明 | 低 | `source--bizone-paper-werewolf-destructive-2024` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--goffee-mythic | Mythic | 公開のポストエクスプロイトフレームワーク。GOFFEE はこのフレームワーク向けの独自エージェント(PowerTaskel、PowerTaskel v2、バイナリ Mythic エージェント、BI.ZONE が挙げる QwakMyAgent)を開発して用いる。BI.ZONE は公開エージェント Poseidon の併用も記録している。 | 2023 | 2026-03 | 高 | `source--kaspersky-goffee-recent-attacks-2025`, `source--kaspersky-goffee-warprat-powertaskel-v2-2026`, `source--bizone-paper-werewolf-destructive-2024` |
| tool--goffee-chisel | Chisel | 被害 IT インフラへの冗長なアクセス経路を確保するために使用する公開トンネリングツール。BI.ZONE は mastc.exe client --tls-skip-verify -v https://[redacted]:49611 R:socks の実行を記録している。 | 不明 | 2024-12-25 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| tool--goffee-psexec | PsExec | 遠隔システムでのコマンド実行に使用する。BI.ZONE は「They probably use PsExec to run commands in remote systems」とし、破壊的操作(レジストリ削除と再起動)およびアカウントのパスワード変更の実行手段として記録している。 | 不明 | 不明 | 中 | `source--bizone-paper-werewolf-destructive-2024` |
| tool--goffee-gophish | Gophish | フィッシング耐性試験用の公開フレームワーク。BI.ZONE は「the adversaries often apply the Gophish open-source framework to organize their mailings」と述べ、配信基盤として悪用されていることを記録している。 | 不明 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| tool--goffee-inno-setup | Inno Setup | 正規のインストーラ作成ツール。2026年3月のキャンペーンでは Inno Setup 6.7.0 (Unicode) で作成したドロッパー Adobe_Acrobat_Reader_Plugin_ru.exe が、WarpRAT 本体(adbp.exe)、おとり PDF(「Требование.pdf」)、install_script.iss を内包していた。 | 2026-03 | 2026-03 | 高 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026` |

### インフラ

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| infra--goffee-per-campaign-domains | キャンペーンごとに使い分ける短命ドメイン群 | Kaspersky は GOFFEE の典型的な技術セットとして「использование отдельных доменов для каждой кампании」(キャンペーンごとの専用ドメインの使用)を挙げる。2026年の報告が列挙する悪性ドメインは timemirror[.]online、bellwitch[.]online、timecheck[.]site、ntpcheck[.]online、ntpverify[.]online、timeget[.]online、timefetch[.]online、easytrns[.]com、ntpsync[.]online、syncheaven[.]online、syncpack[.]online、sslfix[.]online、sslchck[.]online、ntp[.]report、mysitte[.]online、sddfghj[.]com、ntpfix[.]online、sslvalid[.]online であり、配布に用いた ntpluck[.]online と WarpRAT 検体の C2 である ntpsum[.]online も本文中に現れる。NTP・時刻同期・SSL 検証を思わせる語を組み合わせた命名が目立つ。 | 2026-03 | 2026-03 | 高 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026` |
| infra--goffee-reverse-proxy | C2 秘匿のためのリバースプロキシ | Kaspersky は GOFFEE のキャンペーンに典型的な特徴として「активное применение серверов обратного проксирования для сокрытия инфраструктуры командных центров」(C2 インフラを秘匿するためのリバースプロキシサーバの積極的な利用)を挙げる。 | 不明 | 不明 | 高 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026` |
| infra--goffee-vps | C2 とマルウェア配置に用いる VPS | BI.ZONE は ATT&CK 対応表で「Paper Werewolf uses VPS to host C2 servers and malware」と記録し、ドメインの取得(「registers C2 server and malware domains」)およびペイロードの自社サーバ上への配置(「stores the payload on its servers」)も併せて挙げている。 | 不明 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |

### 配送・ファイル形式

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| delivery--goffee-rar-double-extension | 二重拡張子の実行ファイルを含む RAR 書庫 | 文書を装った実行ファイルを RAR 書庫へ収める。ファイル名に .pdf.exe や .doc.exe のような二重拡張子を用いる場合がある。実体は Windows のシステムファイル(explorer.exe または xpsrchvw.exe)の一部コードを悪性シェルコードへ差し替えたもので、実行すると C2 からおとり文書を取得して開きつつ、難読化された Mythic エージェントが C2 と通信を開始する。 | 2024-07 | 2024-12 | 高 | `source--kaspersky-goffee-recent-attacks-2025` |
| delivery--goffee-office-macro | VBA マクロを含む Microsoft Office 文書 | RAR 書庫に収めた Word 文書のマクロをドロッパーとして用いる。文書を開くと文字化けした本文と「This document was created in an earlier version of Microsoft Office Word. For Microsoft Office Word to display the contents correctly, click 'Enable Content'」という警告画像が表示される。コンテンツの有効化でマクロが動作し、警告画像を隠して文字置換により本文を復元するとともに、HTA と PowerShell の2ファイルを作成して HTA のパスをレジストリへ書き込む。BI.ZONE は暗号化された文書本文が特殊文字をロシア語の文字へ置換することで復号される点、ペイロードの探索が DigitalRSASignature キー文字列の後から始まり、CHECKSUM 文字列で2分割された Base64 データである点を記録している。 | 2024-07 | 2024-12 | 高 | `source--kaspersky-goffee-recent-attacks-2025`, `source--bizone-paper-werewolf-destructive-2024` |
| delivery--goffee-pdf-fake-update-link | 偽の更新通知を表示する PDF とダウンロードリンク | 2026年3月のキャンペーンで用いた経路。メールに添付した PDF の内部に、Acrobat Reader が古く更新が必要であるという体裁の偽のシステム通知を描画し、「Установить обновление」(更新をインストール)ボタンから攻撃者ドメインの長大なパスへ誘導する。遷移先では Adobe_Reader_RU.zip が配布され、内部の Inno Setup 製ドロッパーがWarpRAT(adbp.exe)とおとり PDF を展開する。 | 2026-03 | 2026-03 | 高 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026` |
| delivery--goffee-removable-media | リムーバブルメディア経由の拡散 | USB Worm がリムーバブルメディア上の文書をショートカットへ置き換え、PowerModul を含む UserCache.ini を同梱して他端末へ拡散する。 | 2024-07 | 2024-12 | 高 | `source--kaspersky-goffee-recent-attacks-2025` |

### 脆弱性

未確認

### 運用能力

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| opcap--goffee-long-dwell | 被害インフラへの長期滞在と高い隠蔽性 | Kaspersky は GOFFEE の特徴として「хорошо спланированные операции, направленные на узкий круг целей, длительное присутствие в инфраструктуре жертвы, высокая скрытность и постоянно меняющийся арсенал утилит, техник, тактик и процедур」を挙げる。 | 不明 | 不明 | 高 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026` |
| opcap--goffee-ai-automation | 攻撃準備における AI を含む自動化の利用 | Kaspersky は「группа применяет средства автоматизации при подготовке атак, в том числе на базе ИИ」(本グループは攻撃準備に、AI を基盤とするものを含む自動化手段を用いる)と述べる。 | 不明 | 不明 | 中 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026` |
| opcap--goffee-tooling-churn | キャンペーンごとの道具立てとインフラの入れ替え | Kaspersky は「частые изменения инфраструктуры (фактически для каждой кампании), использование целевого фишинга, обширный арсенал инструментов, его регулярное обновление или замена」を挙げ、継続的な監視なしには新規キャンペーンの検知が困難であると述べる。 | 不明 | 不明 | 高 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026` |

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GOFFEEによる改変Owowa IISモジュールの設置 | espionage-campaign | 2022-05 | 2023-08 | 2025-04-10 |  | malware--goffee-owowa | ttp--goffee--asymmetric-crypto, ttp--goffee--iis-components, ttp--goffee--web-portal-capture |  | Kasperskyは、GOFFEEが2022年5月から2023年夏にかけて、改変したOwowa(悪性IISモジュール)を攻撃に用いていたと報告した。BI.ZONEは同モジュールがOutlook Web Accessの利用者認証時に資格情報を窃取し、窃取データをHashSetとしてメモリ上に保持すると説明している。特定のユーザー名をリクエストヘッダへ与えると、Base64で符号化したデータ集合を返すモジュール、および復号後のデータを削除してRSA暗号化したOk文字列を返すモジュールが確認されている。 | 高 | `source--kaspersky-goffee-recent-attacks-2025`, `source--bizone-paper-werewolf-destructive-2024` |
| Paper Werewolfによるマクロ文書を用いた一連のキャンペーンと破壊的行為 | espionage-campaign | 2022 | 不明 | 2024-12-25 | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--5403aec9c83d6a925f61, target--goffee--sector--energy, target--goffee--sector--finance | malware--goffee-powermodul, malware--goffee-powertaskel, malware--goffee-owowa, malware--goffee-qwakmyagent | ttp--activity-rule--7176b5924c70b79b0a53, ttp--goffee--acquire-domains, ttp--goffee--acquire-vps, ttp--goffee--data-destruction, ttp--goffee--deobfuscate, ttp--goffee--develop-malware, ttp--goffee--dynamic-api-resolution, ttp--goffee--embedded-payloads, ttp--goffee--encoded-file, ttp--goffee--fallback-channels, ttp--goffee--fileless-storage, ttp--goffee--hidden-files, ttp--goffee--ingress-tool-transfer, ttp--goffee--lateral-tool-transfer, ttp--goffee--obtain-tool, ttp--goffee--phishing, ttp--goffee--powershell, ttp--goffee--registry-run-keys, ttp--goffee--stage-upload-malware, ttp--goffee--system-info-discovery, ttp--goffee--system-owner-discovery, ttp--goffee--system-shutdown, ttp--goffee--user-execution, ttp--goffee--visual-basic, ttp--goffee--web-protocols | victim--activity-rule--a99f98d19df0289fcaf0 | BI.ZONE Threat Intelligenceは、Paper Werewolf(別名GOFFEE)の活動急増を観測し、2022年以降で少なくとも7件のキャンペーンを記録した。被害組織には政府、エネルギー、金融、メディアほかが含まれる。攻撃者は著名な組織(大規模機関、規制当局、法執行機関)を装うフィッシングメールで悪性マクロ入りのWord文書を配布し、配信にはオープンソースのGophishフレームワークをしばしば用いた。文書は研究機関、自治体、電力系統会社などの文書を装っていた。マクロは復号したペイロードを%USERPROFILE%\UserCache.ini(PowerShell)と%USERPROFILE%\UserCache.ini.hta(HTA)へ書き出し、HKEY_CURRENT_USER\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\Windows\LOADへHTAのパスを書き込んで永続化した。環境変数AZURE_RESOURCE_GROUP、ONEDRIVE_RESOURCE_GROUP、AZURE_DECODEへマルウェアを退避して秘匿する手口、および1×1ピクセル画像へのリンクによる開封監視も観測された。諜報目的の達成後に、PsExec経由でcmd.exe /c 'shutdown /r /f /t 5 && reg delete HKEY_LOCAL_MACHINE\SYSTEM /f && reg delete HKEY_LOCAL_MACHINE\SOFTWARE /f'を実行してレジストリを破壊し、net user [redacted] [redacted] /domainでアカウントのパスワードを変更して被害組織の職員によるインフラ操作を妨げた事例が1件確認されている。 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| GOFFEEによるPowerModul・FlashFileGrabber・USB Wormを用いた2024年後半の標的型攻撃 | espionage-campaign | 2024-07 | 2024-12 | 2025-04-10 | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--5403aec9c83d6a925f61, target--goffee--country--russia, target--goffee--sector--construction, target--goffee--sector--energy, target--goffee--sector--telecom | malware--goffee-powermodul, malware--goffee-powertaskel, malware--goffee-flashfilegrabber, malware--goffee-usb-worm | ttp--activity-rule--22646f6aaf2520e13f75, ttp--activity-rule--73ede5bdd0635240e606, ttp--goffee--data-from-removable-media, ttp--goffee--double-file-extension, ttp--goffee--mshta, ttp--goffee--process-injection, ttp--goffee--removable-media-replication, ttp--goffee--spearphishing-attachment | victim--activity-rule--9a954514c78337fd43b4 | Kasperskyは、2024年後半にGOFFEEがロシア連邦の組織へ標的型攻撃を継続し、PowerTaskelに加えて新たなインプラントPowerModulを投入したと報告した。初期感染は悪性添付付きのフィッシングメールで、同時期に2つの経路が併用された。1つは文書を装う実行ファイル(.pdf.exeや.doc.exeの二重拡張子を用いる場合がある)を収めたRAR書庫で、実体はexplorer.exeまたはxpsrchvw.exeの一部コードを悪性シェルコードへ差し替えたものであり、難読化されたMythicエージェントを内包して即座にC2と通信を開始する。もう1つはマクロをドロッパーとするMicrosoft Office文書で、HTAとPowerShellの2ファイルを作成し、HKCU\Software\Microsoft\Windows NT\CurrentVersion\WindowsのLOAD値へHTAのパスを書き込んで自動起動させる。HTAはcmd.exeと出力リダイレクトでUserCacheHelper.lnk.jsを作成して実行し、そのJavaScriptがWMIのWin32_Process経由で非表示のPowerShellを起動してUserCache.ini(PowerModul)を読み込ませる。PowerModulのペイロードはPowerTaskel、FlashFileGrabber、USB Wormであった。横展開の局面ではPowerShellの制約を理由にPowerTaskelからバイナリMythicエージェントへ移行し、PowerTaskelがC2からエージェントを取得して自プロセスへ注入する。被害はロシア連邦に所在する組織で、マスメディアと通信、建設、政府機関、エネルギーの各分野にわたった。 | 高 | `source--kaspersky-goffee-recent-attacks-2025` |
| GOFFEEによる偽Acrobat Reader更新を用いたWarpRATとPowerTaskel v2の配布 | espionage-campaign | 2026-03 | 2026-03 | 2026-08-28 | target--goffee--country--russia, target--goffee--region--cis, target--goffee--region--europe, target--goffee--sector--manufacturing | malware--goffee-warprat, malware--goffee-powertaskel-v2 | ttp--goffee--encrypted-channel, ttp--goffee--proxy, ttp--goffee--sandbox-evasion, ttp--goffee--spearphishing-link, ttp--goffee--user-execution-installer | victim--activity-rule--d86163e519a5c281599b | Kasperskyは2026年3月、GOFFEEが悪性リンクを含むPDFを添付したメールを送るキャンペーンを観測した。PDFはAcrobat Readerが古く更新が必要であるという体裁の偽の通知を内部に描画し、「更新をインストール」ボタンからntpluck[.]onlineの長大なパスへ誘導する。遷移先ではAdobe_Reader_RU.zipが配布され、内部のInno Setup 6.7.0 (Unicode)製ドロッパーAdobe_Acrobat_Reader_Plugin_ru.exeが、WarpRAT本体のadbp.exe、おとりPDF「ОФИЦИАЛЬНЫЙ ЗАПРОС о предоставлении сведений о потребности в особочистой химической продукции」、およびinstall_script.issを展開する。インストールスクリプトはWarpRATを起動した直後におとりPDFを開く。当該WarpRAT検体はC2にntpsum[.]online、ポート443、TLS有効、POST、sleepTime 314(揺らぎ15)、anti-VM有効の設定を持ち、調査時点でC2が稼働していたためKasperskyは実際の通信を記録している。同キャンペーンではもう1つのバックドアとして軽量なPowerShell製Mythicエージェント(PowerTaskel v2)が展開され、get_tasking要求に対してサーバがコマンド名と実行コードの双方を送り、応答をpost_responseとして返す対話が確認された。 | 高 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| GOFFEEによる改変Owowa IISモジュールの設置 | GOFFEE | Owowa | T1573.002 Asymmetric Cryptography, T1505.004 IIS Components, T1056.003 Web Portal Capture | 情報なし | 情報なし | 情報なし | 高 |
| Paper Werewolfによるマクロ文書を用いた一連のキャンペーンと破壊的行為 | GOFFEE | Owowa, PowerModul, PowerTaskel, QwakMyAgent | T1059.001 PowerShell, T1583.001 Domains, T1583.003 Virtual Private Server, T1485 Data Destruction, T1140 Deobfuscate/Decode Files or Information, T1587.001 Malware, T1027.007 Dynamic API Resolution, T1027.009 Embedded Payloads, T1027.013 Encrypted/Encoded File, T1008 Fallback Channels, T1027.011 Fileless Storage, T1564.001 Hidden Files and Directories, T1105 Ingress Tool Transfer, T1570 Lateral Tool Transfer, T1588.002 Tool, T1566 Phishing, T1059.001 PowerShell, T1547.001 Registry Run Keys / Startup Folder, T1608.001 Upload Malware, T1082 System Information Discovery, T1033 System Owner/User Discovery, T1529 System Shutdown/Reboot, T1204.002 Malicious File, T1059.005 Visual Basic, T1071.001 Web Protocols | C2 とマルウェア配置に用いる VPS | 政府・行政, メディア・報道, エネルギー, 金融 | 被害事例: Paper Werewolfによるマクロ文書を用いた一連のキャンペーンと破壊的行為 | 高 |
| GOFFEEによるPowerModul・FlashFileGrabber・USB Wormを用いた2024年後半の標的型攻撃 | GOFFEE | FlashFileGrabber, PowerModul, PowerTaskel, USB Worm | T1027 Obfuscated Files or Information, T1036 Masquerading, T1025 Data from Removable Media, T1036.007 Double File Extension, T1218.005 Mshta, T1055 Process Injection, T1091 Replication Through Removable Media, T1566.001 Spearphishing Attachment | 情報なし | 政府・行政, メディア・報道, ロシア, 建設, エネルギー, 情報通信 | 被害事例: GOFFEEによるPowerModul・FlashFileGrabber・USB Wormを用いた2024年後半の標的型攻撃 | 高 |
| GOFFEEによる偽Acrobat Reader更新を用いたWarpRATとPowerTaskel v2の配布 | GOFFEE | PowerTaskel v2, WarpRAT | T1573 Encrypted Channel, T1090 Proxy, T1497 Virtualization/Sandbox Evasion, T1566.002 Spearphishing Link, T1204.002 Malicious File | キャンペーンごとに使い分ける短命ドメイン群, C2 秘匿のためのリバースプロキシ | ロシア, CIS諸国, 欧州, 製造・産業 | 被害事例: GOFFEEによる偽Acrobat Reader更新を用いたWarpRATとPowerTaskel v2の配布 | 高 |

Kaspersky が本アクターを認知したのは2022年初頭である。2022年5月から2023年夏にかけては改変した Owowa を IIS へ設置し、Outlook Web Access の認証時に資格情報を窃取していた。2024年からはパッチを当てた explorer.exe をスピアフィッシングで配布する手口へ移行し、2024年後半には PowerTaskel に加えて PowerModul を投入した。同年12月、BI.ZONE は Paper Werewolf の活動急増を報告し、2022年以降で少なくとも7件のキャンペーンを記録するとともに、諜報目的の達成後に被害インフラの運用を妨害した事例を1件公表した。2026年3月には偽の Acrobat Reader 更新通知を描画した PDF から WarpRAT を配布する新しい初期アクセス手法が観測され、同時に PowerTaskel の進化形である PowerTaskel v2 の展開が確認された。

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | ロシア | Kasperskyは2025年の報告で「the identified targets of the malicious activities described in this article are located in Russia」とし、2026年の報告では「мы обнаружили около 120 жертв в Российской Федерации」として約120の被害組織をロシア連邦で確認したと述べる。被害の主たる所在をロシア連邦と判断した根拠として、スピアフィッシングのメールとおとりファイルのほとんどがロシア語であったという言語的手掛かりとテレメトリを挙げている。 | 2024-07 | 2026-03 | 高 | `source--bizone-paper-werewolf-destructive-2024`, `source--kaspersky-goffee-recent-attacks-2025`, `source--kaspersky-goffee-warprat-powertaskel-v2-2026` |
| regions | CIS諸国 | Kasperskyは2026年の報告で「несколько — в странах СНГ」として、CIS諸国でも数件の被害を確認したと述べる。個別の国名は原文に記載がない。 | 2026-03 | 2026-03 | 中 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026` |
| regions | 欧州 | Kasperskyは2026年の報告で「единичные — в ЕС」としてEUで単発の被害を確認したが、「Атаки на цели в странах Евросоюза носят случайный характер」として、EU域内の標的への攻撃は偶発的な性質のものであると評価している。 | 2026-03 | 2026-03 | 低 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026` |
| sectors | 政府・行政 | 活動「Paper Werewolfによるマクロ文書を用いた一連のキャンペーンと破壊的行為」の記述で標的として明示された産業。 | 2022 | 2024-12 | 中 | `source--bizone-paper-werewolf-destructive-2024`, `source--kaspersky-goffee-recent-attacks-2025` |
| sectors | メディア・報道 | 活動「Paper Werewolfによるマクロ文書を用いた一連のキャンペーンと破壊的行為」の記述で標的として明示された産業。 | 2022 | 2024-12 | 中 | `source--bizone-paper-werewolf-destructive-2024`, `source--kaspersky-goffee-recent-attacks-2025` |
| sectors | 建設 | Kasperskyは2025年の報告で対象業種に「construction」を挙げる。 | 2024-07 | 2024-12 | 高 | `source--kaspersky-goffee-recent-attacks-2025` |
| sectors | エネルギー | Kasperskyは2025年の報告で対象業種に「energy companies」を挙げる。BI.ZONEも被害組織にエネルギー分野を挙げ、電力系統会社の文書を装ったおとりの使用を記録している。 | 2022 | 2024-12 | 高 | `source--bizone-paper-werewolf-destructive-2024`, `source--kaspersky-goffee-recent-attacks-2025` |
| sectors | 金融 | BI.ZONEは被害組織に金融分野を挙げる(「Among the victims are government, energy, financial, media, and other organizations」)。 | 2022 | 不明 | 中 | `source--bizone-paper-werewolf-destructive-2024` |
| sectors | 製造・産業 | Kasperskyは2026年の報告で「машиностроению, производству」(機械製造、製造業)を主たる標的業種として挙げ、GOFFEEの典型的な被害者層を「государственные учреждения и промышленные предприятия РФ」(ロシア連邦の政府機関と工業企業)と要約する。 | 2026-03 | 2026-03 | 高 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026` |
| sectors | 情報通信 | Kasperskyは2025年の報告で対象業種に「media and telecommunications sectors」を挙げる。 | 2024-07 | 2024-12 | 高 | `source--kaspersky-goffee-recent-attacks-2025` |

選定ロジック: Kasperskyは標的が狭く選別されていること(「направленные на узкий круг целей」「специально отобранный круг жертв」)をGOFFEEの特徴として繰り返し述べる。被害はロシア連邦の組織に集中し、2026年の報告は業種の中心を機械製造・製造業・政府部門とする。CIS諸国での被害は数件、EUでの被害は単発かつ偶発的と評価されている。おとり文書は研究機関、自治体、電力系統会社、規制当局、法執行機関など被害者が信頼しやすい実在組織の文書を模したものが用いられる。 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: GOFFEEによるPowerModul・FlashFileGrabber・USB Wormを用いた2024年後半の標的型攻撃 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--5403aec9c83d6a925f61, target--goffee--country--russia, target--goffee--sector--construction, target--goffee--sector--energy, target--goffee--sector--telecom | malware--goffee-flashfilegrabber, malware--goffee-powermodul, malware--goffee-powertaskel, malware--goffee-usb-worm | ttp--activity-rule--22646f6aaf2520e13f75, ttp--activity-rule--73ede5bdd0635240e606, ttp--goffee--data-from-removable-media, ttp--goffee--double-file-extension, ttp--goffee--mshta, ttp--goffee--process-injection, ttp--goffee--removable-media-replication, ttp--goffee--spearphishing-attachment | メール／メールアカウント |  | 2024-07 | 2024-12 | 2025-04-10 | 高 | `source--kaspersky-goffee-recent-attacks-2025` |
| 被害事例: Paper Werewolfによるマクロ文書を用いた一連のキャンペーンと破壊的行為 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--5403aec9c83d6a925f61, target--goffee--sector--energy, target--goffee--sector--finance | malware--goffee-owowa, malware--goffee-powermodul, malware--goffee-powertaskel, malware--goffee-qwakmyagent | ttp--activity-rule--7176b5924c70b79b0a53, ttp--goffee--acquire-domains, ttp--goffee--acquire-vps, ttp--goffee--data-destruction, ttp--goffee--deobfuscate, ttp--goffee--develop-malware, ttp--goffee--dynamic-api-resolution, ttp--goffee--embedded-payloads, ttp--goffee--encoded-file, ttp--goffee--fallback-channels, ttp--goffee--fileless-storage, ttp--goffee--hidden-files, ttp--goffee--ingress-tool-transfer, ttp--goffee--lateral-tool-transfer, ttp--goffee--obtain-tool, ttp--goffee--phishing, ttp--goffee--powershell, ttp--goffee--registry-run-keys, ttp--goffee--stage-upload-malware, ttp--goffee--system-info-discovery, ttp--goffee--system-owner-discovery, ttp--goffee--system-shutdown, ttp--goffee--user-execution, ttp--goffee--visual-basic, ttp--goffee--web-protocols | メール／メールアカウント, クラウド／SaaS | disruption: 諜報目的の達成後に、PsExec経由でcmd.exe /c 'shutdown /r /f /t 5 && reg delete HKEY_LOCAL_MACHINE\SYSTEM /f && reg delete HKEY_LOCAL_MACHINE\SOFTWARE /f'を実行してレジストリを破壊し、net user [redacted] [redacted] /domainでアカウントのパスワードを変更して被害組織の職員によるインフラ操作を妨げた事例が1件確認されている。 | 2022 | 不明 | 2024-12-25 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| 被害事例: GOFFEEによる偽Acrobat Reader更新を用いたWarpRATとPowerTaskel v2の配布 | 非公開 | anonymous | unknown | reported | target--goffee--country--russia, target--goffee--region--cis, target--goffee--region--europe, target--goffee--sector--manufacturing | malware--goffee-powertaskel-v2, malware--goffee-warprat | ttp--goffee--encrypted-channel, ttp--goffee--proxy, ttp--goffee--sandbox-evasion, ttp--goffee--spearphishing-link, ttp--goffee--user-execution-installer | メール／メールアカウント |  | 2026-03 | 2026-03 | 2026-08-28 | 高 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1027 | Obfuscated Files or Information | 1つは文書を装う実行ファイル(.pdf.exeや.doc.exeの二重拡張子を用いる場合がある)を収めたRAR書庫で、実体はexplorer.exeまたはxpsrchvw.exeの一部コードを悪性シェルコードへ差し替えたものであり、難読化されたMythicエージェントを内包して即座にC2と通信を開始する。 |  | activity--goffee-powermodul-usb-worm-2024 | 2024-07 | 2024-12 | 中 | `source--kaspersky-goffee-recent-attacks-2025` |
| Execution | T1059.001 | PowerShell | マクロは復号したペイロードを%USERPROFILE%\UserCache.ini(PowerShell)と%USERPROFILE%\UserCache.ini.hta(HTA)へ書き出し、HKEY_CURRENT_USER\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\Windows\LOADへHTAのパスを書き込んで永続化した。 |  | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 中 | `source--bizone-paper-werewolf-destructive-2024` |
| Stealth | T1036 | Masquerading | 1つは文書を装う実行ファイル(.pdf.exeや.doc.exeの二重拡張子を用いる場合がある)を収めたRAR書庫で、実体はexplorer.exeまたはxpsrchvw.exeの一部コードを悪性シェルコードへ差し替えたものであり、難読化されたMythicエージェントを内包して即座にC2と通信を開始する。 |  | activity--goffee-powermodul-usb-worm-2024 | 2024-07 | 2024-12 | 中 | `source--kaspersky-goffee-recent-attacks-2025` |
| Resource Development | T1583.001 | Domains | BI.ZONEは「Paper Werewolf registers C2 server and malware domains」として、C2サーバおよびマルウェア配布用ドメインの取得を記録している。 |  | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Resource Development | T1583.003 | Virtual Private Server | BI.ZONEは「Paper Werewolf uses VPS to host C2 servers and malware」として、C2サーバとマルウェアの設置にVPSを用いると記録している。 |  | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Command and Control | T1573.002 | Asymmetric Cryptography | BI.ZONEは「Paper Werewolf uses the RSA algorithm to decrypt credentials intercepted by the malicious IIS Owowa module」として、Owowaが傍受した資格情報のRSAによる復号を記録している。 | malware--goffee-owowa | activity--goffee-owowa-iis-2022-2023 | 2022-05 | 2023-08 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Impact | T1485 | Data Destruction | BI.ZONEは「Paper Werewolf uses the commands reg delete HKEY_LOCAL_MACHINE\SYSTEM /f && reg delete HKEY_LOCAL_MACHINE\SOFTWARE /f and PsExec to delete OS register keys」として、PsExec経由のレジストリキー削除を記録している。 |  | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 中 | `source--bizone-paper-werewolf-destructive-2024` |
| Collection | T1025 | Data from Removable Media | KasperskyはFlashFileGrabberが対象拡張子のファイルをリムーバブルメディアから%TEMP%\CacheStore\connect\<VolumeSerialNumber>\配下へ複写し、ftree.dbへメタデータを、%AppData%\internal_profiles.dbへそのMD5を保存して重複複写を避けると報告している。FlashFileGrabberは収集したファイルをC2へ送信できる。 | malware--goffee-flashfilegrabber | activity--goffee-powermodul-usb-worm-2024 | 2024-07 | 2024-12 | 高 | `source--kaspersky-goffee-recent-attacks-2025` |
| Defense Evasion | T1140 | Deobfuscate/Decode Files or Information | BI.ZONEは「Paper Werewolf decrypts the payload in malicious documents using a VBA macro. Paper Werewolf decrypts and runs the malicious content of the environment variables in the compromised system」として、文書内ペイロードおよび環境変数に退避した内容の復号実行を記録している。 |  | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Resource Development | T1587.001 | Malware | BI.ZONEは「Paper Werewolf uses own crafted malware such as PowerTaskel」として、PowerTaskelをはじめとする自製マルウェアの開発を記録している。 | malware--goffee-powertaskel, malware--goffee-qwakmyagent | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Defense Evasion | T1036.007 | Double File Extension | Kasperskyは「In some cases, the file name uses a double extension, such as '.pdf.exe' or '.doc.exe'」として、二重拡張子による文書偽装を報告している。実体はexplorer.exeまたはxpsrchvw.exeの一部コードを悪性シェルコードへ差し替えたものである。 |  | activity--goffee-powermodul-usb-worm-2024 | 2024-07 | 2024-12 | 高 | `source--kaspersky-goffee-recent-attacks-2025` |
| Defense Evasion | T1027.007 | Dynamic API Resolution | BI.ZONEは「Paper Werewolf applies the Fowler-Noll-Vo algorithm to hash the names of WinAPI functions used in the malicious loader」として、悪性ローダーにおけるWinAPI関数名のFNVハッシュ化を記録している。 |  | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Defense Evasion | T1027.009 | Embedded Payloads | BI.ZONEは「Paper Werewolf uses malicious documents to store the Base64-encoded payload」として、悪性文書内へのBase64符号化ペイロードの埋め込みを記録している。 |  | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Defense Evasion | T1027.013 | Encrypted/Encoded File | BI.ZONEは「Paper Werewolf uses Base-64-encrypted payloads and PowerRAT commands」として、ペイロードとコマンドのBase64符号化を記録している。 | malware--goffee-powermodul | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Command and Control | T1573 | Encrypted Channel | Kasperskyが解析したWarpRAT検体の設定はC2_portを443、useSSLをtrue、methodをPOSTとし、sleepTimeを314(揺らぎ15)としていた。 | malware--goffee-warprat | activity--goffee-warprat-powertaskel-v2-2026 | 2026-03 | 2026-03 | 高 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026` |
| Command and Control | T1008 | Fallback Channels | BI.ZONEは「Paper Werewolf uses Chisel as a redundant access channel to the compromised IT infrastructure」として、Chiselによる冗長なアクセス経路の確保を記録している。 |  | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Defense Evasion | T1027.011 | Fileless Storage | BI.ZONEは「Paper Werewolf uses environment variables AZURE_RESOURCE_GROUP, ONEDRIVE_RESOURCE_GROUP, AZURE_DECODE to hide the malware in the compromised system」として、環境変数へのマルウェア退避を記録している。 |  | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Defense Evasion | T1564.001 | Hidden Files and Directories | BI.ZONEは「Paper Werewolf uses PowerRAT which installs a Hidden attribute for the files UserCache.ini and UserCache.ini.hta」として、両ファイルへのHidden属性付与を記録している。 | malware--goffee-powermodul | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Persistence | T1505.004 | IIS Components | BI.ZONEは「Paper Werewolf installs a malicious Owowa module on the IIS server」として、IISサーバへの悪性Owowaモジュール設置を記録している。 | malware--goffee-owowa | activity--goffee-owowa-iis-2022-2023 | 2022-05 | 2023-08 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Command and Control | T1105 | Ingress Tool Transfer | BI.ZONEは「Paper Werewolf uses own loaders to deliver and launch the malware」として、自製ローダーによるマルウェアの搬入と起動を記録している。 |  | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Lateral Movement | T1570 | Lateral Tool Transfer | BI.ZONEは「Paper Werewolf uses PsExec to advance in the compromised IT infrastructure」として、PsExecによる横展開を記録している。 |  | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Execution | T1218.005 | Mshta | KasperskyはマクロがHTAとPowerShellの2ファイルを作成し、HKCU\Software\Microsoft\Windows NT\CurrentVersion\WindowsのLOAD値へHTAのパスを書き込むことで、当該利用者のログオン時に自動実行されると報告している。HTAはcmd.exeと出力リダイレクトでUserCacheHelper.lnk.jsを作成して実行し、そのJavaScriptがWMIのWin32_Process経由で非表示のPowerShellを起動する。 | malware--goffee-powermodul | activity--goffee-powermodul-usb-worm-2024 | 2024-07 | 2024-12 | 高 | `source--kaspersky-goffee-recent-attacks-2025` |
| Resource Development | T1588.002 | Tool | BI.ZONEは「Paper Werewolf uses tools such as Chisel, PsExec and Mythic, and a Mythic post-exploitation framework」として、Chisel、PsExec、Mythicの取得と利用を記録している。 |  | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Initial Access | T1566 | Phishing | BI.ZONEは「Paper Werewolf sends out phishing emails to distribute documents with a malicious macro」として、悪性マクロ入り文書をフィッシングメールで配布すると記録している。配信基盤にはオープンソースのGophishフレームワークがしばしば用いられた。 |  | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Execution | T1059.001 | PowerShell | BI.ZONEは「Paper Werewolf uses PowerShell tools such as PowerRAT and PowerTaskel to run C2 commands from the compromised host」として、PowerShell製の道具によるC2コマンド実行を記録している。 | malware--goffee-powermodul, malware--goffee-powertaskel | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Defense Evasion | T1055 | Process Injection | Kasperskyは横展開の局面でPowerShellの制約を理由にPowerTaskelからバイナリMythicエージェントへ移行し、PowerTaskelがC2からエージェントを取得して自プロセスへ注入すると報告している。 | malware--goffee-powertaskel | activity--goffee-powermodul-usb-worm-2024 | 2024-07 | 2024-12 | 高 | `source--kaspersky-goffee-recent-attacks-2025` |
| Command and Control | T1090 | Proxy | KasperskyはGOFFEEのキャンペーンに典型的な特徴として「активное применение серверов обратного проксирования для сокрытия инфраструктуры командных центров」(C2インフラを秘匿するためのリバースプロキシサーバの積極的な利用)を挙げている。 |  | activity--goffee-warprat-powertaskel-v2-2026 | 2026-03 | 2026-03 | 高 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026` |
| Persistence | T1547.001 | Registry Run Keys / Startup Folder | BI.ZONEは「Paper Werewolf gains persistence in the compromised system by using a registry parameter HKEY_CURRENT_USER\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\Windows\LOAD, whereto the path to the file UserCache.ini.hta is written」として、LOAD値を用いた永続化を記録している。 | malware--goffee-powermodul | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Lateral Movement | T1091 | Replication Through Removable Media | KasperskyはUSB Wormがリムーバブルメディア上の文書を拡張子を保ったままランダムな名前へ改名してHidden属性を与え、PowerModulを含むUserCache.iniを同じフォルダへ複写すると報告している。起動用のVBSとバッチファイル、および元の文書名を持つショートカットを隠しファイルとして作成し、ショートカットにはshell32.dllのアイコンを割り当てて偽装する。置き換え対象はLastAccessTimeの新しい順に最大5件へ制限される。 | malware--goffee-usb-worm, malware--goffee-powermodul | activity--goffee-powermodul-usb-worm-2024 | 2024-07 | 2024-12 | 高 | `source--kaspersky-goffee-recent-attacks-2025` |
| Defense Evasion | T1497 | Virtualization/Sandbox Evasion | Kasperskyが解析したWarpRAT検体の設定にはuseAntiVMが1として含まれ、Kaspersky Cloud Sandboxでの動的解析でも「проводит разведку окружения на наличие артефактов, связанных с выполнением в песочнице」としてサンドボックス実行の痕跡の探索が確認されている。 | malware--goffee-warprat | activity--goffee-warprat-powertaskel-v2-2026 | 2026-03 | 2026-03 | 高 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026` |
| Initial Access | T1566.001 | Spearphishing Attachment | Kasperskyは2024年後半のキャンペーンについて「The starting point is typically a phishing email with a malicious attachment」と述べ、文書を装う実行ファイルを収めたRAR書庫、およびマクロ入りOffice文書を収めたRAR書庫の2経路が併用されたと報告している。 |  | activity--goffee-powermodul-usb-worm-2024 | 2024-07 | 2024-12 | 高 | `source--kaspersky-goffee-recent-attacks-2025` |
| Initial Access | T1566.002 | Spearphishing Link | Kasperskyは2026年3月のキャンペーンについて、悪性リンクを含むPDFを添付したメールが送られ、PDF内部に描画された偽のAcrobat Reader更新通知のボタンからntpluck[.]onlineの長大なパスへ誘導されたと報告している。 |  | activity--goffee-warprat-powertaskel-v2-2026 | 2026-03 | 2026-03 | 高 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026` |
| Resource Development | T1608.001 | Upload Malware | BI.ZONEは「Paper Werewolf stores the payload on its servers」として、自ら管理するサーバ上へのペイロード配置を記録している。 |  | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Discovery | T1082 | System Information Discovery | BI.ZONEは「Paper Werewolf uses PowerRAT to retrieve the name of the compromised host, the serial number of the system disk」として、ホスト名とシステムディスクのシリアル番号の取得を記録している。Kasperskyも同様に、PowerModulがC2 URLへ computer_name、username、ディスクシリアル番号を連結した識別子を付与すると述べる。 | malware--goffee-powermodul | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024`, `source--kaspersky-goffee-recent-attacks-2025` |
| Discovery | T1033 | System Owner/User Discovery | BI.ZONEは「Paper Werewolf uses PowerRAT to retrieve the compromised host username」として、利用者名の取得を記録している。 | malware--goffee-powermodul | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Impact | T1529 | System Shutdown/Reboot | BI.ZONEは「Paper Werewolf uses the command cmd.exe /c shutdown /r /f /t 5 and PsExec to terminate the host's operation」として、PsExec経由の強制再起動を記録している。 |  | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 中 | `source--bizone-paper-werewolf-destructive-2024` |
| Execution | T1204.002 | Malicious File | BI.ZONEは「Paper Werewolf targets its victims through malicious decoy documents from various companies and government agencies」として、実在企業・政府機関の文書を装ったおとりによる利用者実行の誘導を記録している。 |  | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Execution | T1204.002 | Malicious File | Kasperskyは遷移先で配布されたAdobe_Reader_RU.zipの内部に、Inno Setup 6.7.0 (Unicode)で作成されたドロッパーAdobe_Acrobat_Reader_Plugin_ru.exeが収められ、WarpRAT本体のadbp.exeを起動した直後におとりPDFを開くと報告している。 | malware--goffee-warprat | activity--goffee-warprat-powertaskel-v2-2026 | 2026-03 | 2026-03 | 高 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026` |
| Execution | T1059.005 | Visual Basic | BI.ZONEは「Paper Werewolf creates a VBA macro in documents and an HTA file that creates and executes a VBScript %USERPROFILE%\UserCacheHelper.lnk.js to further run a PowerShell script %USERPROFILE%\UserCache.ini」として、文書内VBAマクロとHTAによる多段実行を記録している。 | malware--goffee-powermodul | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Credential Access | T1056.003 | Web Portal Capture | BI.ZONEは「Paper Werewolf retrieves credentials during user authorization in the OWA service by using the malicious IIS Owawa module」として、Outlook Web Accessの認証時における資格情報の窃取を記録している。 | malware--goffee-owowa | activity--goffee-owowa-iis-2022-2023 | 2022-05 | 2023-08 | 高 | `source--bizone-paper-werewolf-destructive-2024` |
| Command and Control | T1071.001 | Web Protocols | BI.ZONEは「Paper Werewolf uses HTTP to communicate with the C2 servers and receive the payload」として、HTTPによるC2通信とペイロード取得を記録している。 |  | activity--goffee-paper-werewolf-campaigns-2024 | 2022 | 不明 | 高 | `source--bizone-paper-werewolf-destructive-2024` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| GOFFEE と BI.ZONE が追跡する Paper Werewolf は同一のクラスタである。 | 高 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026`, `source--bizone-paper-werewolf-destructive-2024` | 両社が互いの名称を明示している(Kaspersky「GOFFEE (также известная как Paper Werewolf)」、BI.ZONE「the Paper Werewolf cluster (also known as GOFFEE)」)。加えて、UserCache.ini / UserCache.ini.hta / UserCacheHelper.lnk.js の組、LOAD レジストリ値による永続化、api/texts/<computer>_<user>_<serial> 形式の C2 URL、CountRuns / Interval / Module を属性とする XML 応答という技術的特徴が独立に一致する。 |
| 本アクターの主たる被害はロシア連邦の組織であり、主たる動機はサイバースパイ活動である。 | 高 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026`, `source--kaspersky-goffee-recent-attacks-2025`, `source--bizone-paper-werewolf-destructive-2024` | Kaspersky は2025年に「targeting exclusively entities located in the Russian Federation」、2026年に「約120の被害組織をロシア連邦で確認」と述べ、動機を「Основная мотивация группы — кибершпионаж」とする。BI.ZONE も espionage cluster として扱う。 |
| 本アクターの出身国・後援関係は、いずれの一次資料でも特定されていない。 | 高 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026`, `source--kaspersky-goffee-recent-attacks-2025`, `source--bizone-paper-werewolf-destructive-2024` | 3本とも国家帰属を行っていない。MITRE ATT&CK にも公式グループエントリは存在しない。被害国であるロシア連邦を帰属国へ流用してはならない。 |
| GOFFEE は道具立てを継続的に入れ替えており、2026年時点の主力は WarpRAT と PowerTaskel v2 である。 | 高 | `source--kaspersky-goffee-warprat-powertaskel-v2-2026`, `source--kaspersky-goffee-recent-attacks-2025` | Owowa(2022年5月〜2023年夏)、PowerTaskel(2023年初頭〜)、PowerModul とそのペイロード(2024年)、WarpRAT と PowerTaskel v2(2026年)という推移が2本の Kaspersky 報告から追える。 |

### 情報ギャップ

- 3本の一次資料はいずれも被害組織名を明示していないため、victim_cases を構造化できていない。
- Kaspersky が2026年の報告で述べる「攻撃準備におけるAIを含む自動化の利用」は、根拠となる具体的な観測が原文に示されていない。
- BI.ZONE が挙げる QwakMyAgent は、同社自身が当該段階の検体を解析できていないと明記しており、機能も観測日も不明である。
- 2022年から2024年前半までの個々のキャンペーンは、BI.ZONE が「at least seven campaigns since 2022」と件数のみを述べており、個別に構造化できていない。
- Kaspersky が2026年の報告で言及する MythicAcademic キャンペーンの実体が不明であり、GOFFEE との関係も C2 インフラの共有以外は示されていない。
- securelist.ru を巡回対象へ加えたのは2026-09-14の走査からであるため、2026-08-28より前にロシア語版のみで公開された GOFFEE 関連記事が未確認のまま残っている可能性がある。

### 不確実性

- Kaspersky は「Ранее мы установили связь этой группы с другой APT-группой — HeartlessSoul. Со средней степенью уверенности можно заключить, что за этими двумя группами стоят одни и те же атакующие, однако их инструментарий существенно различается」として、HeartlessSoul との背後の同一性を中程度の確度で評価している。HeartlessSoul は本リポジトリに既存プロファイルも未帰属クラスタ台帳のエントリも持たず、根拠となる過去の報告も本稿からは辿れない。確度が中程度にとどまり道具立ても大きく異なるとされるため、relationships へは登録せず本項へ両論として残す。
- PowerModul(Kaspersky)と PowerRAT(BI.ZONE)の同一性は、両社とも明言していない分析者評価である。根拠は capabilities.malware の malware--goffee-powermodul の analyst_notes に記載した。競合する情報が出た場合は上書きせず claim-audit.json へ記録する。
- WarpRAT は Kaspersky が「широко известный」(広く知られた)と述べるバイナリであり、別名 EchoGather RAT も本稿の記述のみを根拠としている。GOFFEE 専用のマルウェアではないため、WarpRAT の検出のみを GOFFEE への帰属根拠として用いない。
- PowerTaskel v2 は当初 MythicAcademic キャンペーンでの使用として観測され、C2 インフラの共有が判明して初めて GOFFEE へ結び付いたと Kaspersky が明記している。MythicAcademic と GOFFEE の関係は本稿では解決されていない。
- PowerTaskel / PowerModul / USB Worm の名称は profiles/anonymous の生成物にも現れるが、これは Kaspersky ICS CERT のハクティビスト TTP 総覧資料に含まれる一般的な技術記述からの取り込みであり、同プロファイルに GOFFEE 由来の IOC は存在しない(iocs.json は0件)。本プロファイルとの重複ではない。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--kaspersky-goffee-warprat-powertaskel-v2-2026 | APT-группа GOFFEE продолжает атаки на организации в РФ, распространяя два бэкдора через целевой фишинг | Kaspersky GReAT (Securelist ロシア語版) | 2026-08-28 | https://securelist.ru/tr/goffee-apt-attacks-with-mythic-agent-and-warprat/116796/ | vendor-research | TLP:CLEAR | 高 |
| source--kaspersky-goffee-recent-attacks-2025 | GOFFEE's recent attacks: new tools and techniques | Kaspersky GReAT (Securelist) | 2025-04-10 | https://securelist.com/goffee-apt-new-attacks/116139/ | vendor-research | TLP:CLEAR | 高 |
| source--bizone-paper-werewolf-destructive-2024 | Espionage cluster Paper Werewolf engages in destructive behavior | BI.ZONE Threat Intelligence | 2024-12-25 | https://bi.zone/eng/expertise/blog/paper-werewolf-sovmeshchaet-kibershpionazh-s-destruktivnymi-deystviyami/ | vendor-research | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

本プロファイルの被害国はロシア連邦であり、これを攻撃者の帰属国へ流用してはならない。3本の一次資料はいずれも攻撃者の出身国を述べていない。Kaspersky が中程度の確度で述べる HeartlessSoul との背後の同一性、および PowerModul と PowerRAT の名称対応は、いずれも未解決として assessment へ残している。
