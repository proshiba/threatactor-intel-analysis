# Gunra 脅威アクタープロファイル

- プロファイルID: `actor--gunra`
- 状態: draft
- 更新日時: 2026-09-23T12:16:55Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

Gunraは2025年4月に出現した二重恐喝型ランサムウェアの運用主体であり、2026年1月にRaaSアフィリエイトプログラムを開始した。AhnLabは2026年3月の韓国組織へのGunra感染が、同年1月の匿名state-sponsored clusterによるwatering-hole intrusionと、脆弱性、file/service/argument pattern、SSH key、network infrastructureを共有したと報告した。ただしsame actorや国家帰属は立証されず、技術的重複としてのみ保持する。

## アクター名とAlias

- 正規名: **Gunra**
- 初回観測: 2025-04
- 最終観測: 2026-07
- 活動状態: yes

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Golden Community | FBI | overlapping | 中 | `source--cisa-aa26-222a-gunra` | 共同勧告は「The FBI observed the group adopting new branding aliases (notably operating under the name Golden Community)」と記載する。RaaS展開に伴うブランド名であり、同一クラスタと断定できないためscopeはoverlappingとする。 |

## 帰属

共同勧告は金銭目的のサイバー犯罪(financially motivated cybercriminals)向けのRaaSと記載するのみで、帰属国もスポンサーも示していない。被害国やインフラ所在国から攻撃元国を推定しない。

- 国: 不明
- スポンサー種別: criminal
- 確度: 不明
- 証拠: `source--cisa-aa26-222a-gunra`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| financial-gain | データ窃取と暗号化を組み合わせた二重恐喝により身代金を得ることを目的とする。身代金交渉は数千万米ドル規模から開始されると勧告が記載している。 | 高 | `source--cisa-aa26-222a-gunra` |  |

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

- 判定: `no-match`
- 調査日時: 2026-09-21T02:39:13Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | 一致なし |  |  |  |  |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
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

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--gunra-ransomware | Gunra | 二重恐喝型ランサムウェア。マルチスレッドでChaCha20 + RSA-4096により全ボリュームを暗号化し、暗号化済みファイルへ拡張子.ENCRTを付与する(2025年7月の1検体では.CRYPT)。各ディレクトリへ身代金メモR3ADM3.txtを書き込む。FindFirstFileW/FindNextFileWでA〜Zの全ドライブを走査し、システムディレクトリと.exe/.dll/.sys等を除外する二段フィルタを持つ。IsDebuggerPresentによるデバッガ検知を備え、ネットワーク通信を伴わない自己完結型である。2025年半ばにLinux版が追加された。 | 2025-04 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| malware--gunra-main-exe | main.exe | Microsoft OneDriveとSharePointから被害データを持ち出すためにGunraが使用した悪性実行ファイル。勧告は2件のSHA256を掲載している。 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--gunra-impacket | Impacket | psexec.py / smbclient.py によるSMB経由の横展開と、secretsdump.py によるドメインコントローラーからのNTDS資格情報ダンプに使用。 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| tool--gunra-mimikatz | Mimikatz | Windowsからの認証情報の取得に使用する後侵害ツール。 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| tool--gunra-sliver | Sliver | 遠隔操作に用いるペネトレーションテスト用C2フレームワーク。 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| tool--gunra-rclone | RClone | クラウドストレージ間のファイル操作に用いるコマンドラインツール。データ持ち出しに使用。 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| tool--gunra-openssh | OpenSSH | 攻撃者管理の外部サーバーから取得し、侵害システム間のSSHトンネルと持続化に使用。 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| tool--gunra-archivers | 7-Zip / WinRAR | 持ち出し前の圧縮アーカイブ作成に使用。 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| tool--gunra-filezilla | FileZilla | 代替プロトコル経由でのデータ持ち出しに使用するFTPクライアント。 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| tool--gunra-rmm | AnyDesk / Google Remote Desktop / MobaXterm | 遠隔アクセスと持続化に流用される正規のリモート管理・接続ツール。 | 不明 | 不明 | 中 | `source--cisa-aa26-222a-gunra` |
| tool--gunra-amass | Amass | ネットワークマッピングと情報収集に使用する偵察ツール。 | 不明 | 不明 | 中 | `source--cisa-aa26-222a-gunra` |
| tool--gunra-psexec | PsExec | AhnLabが報告したGunra事例では、hotfix.exeへ改名したPsExecを集中管理ソリューション経由の追加payload配布とPowerShell実行に使用した。 | 不明 | 不明 | 高 | `source--ahnlab-operation-double-barrel-2026` |
| tool--gunra-socat | Socat | AhnLabが分析した2026年3月のGunra感染事例でport forwardingに使用された。 | 2026-03 | 2026-03 | 高 | `source--ahnlab-operation-double-barrel-2026` |
| tool--gunra-operation-double-barrel-openssh | OpenSSH (Operation Double Barrel) | AhnLabが分析した2026年3月のGunra感染事例で設置され、public-key login、内部移動、reverse tunnelに使用された。匿名state-sponsored cluster側でも同一SSH鍵fingerprintを伴うOpenSSH reverse tunnelが確認された。 | 2026-01 | 2026-03 | 高 | `source--ahnlab-operation-double-barrel-2026` |
| tool--gunra-operation-double-barrel-filezilla | FileZilla (Operation Double Barrel) | AhnLabが分析した2026年3月のGunra感染事例で、侵害組織からのデータ持ち出しに使用された。 | 2026-03 | 2026-03 | 高 | `source--ahnlab-operation-double-barrel-2026` |

### インフラ

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| infrastructure--gunra-dls | Tor上のDLSと交渉ポータル | 被害組織の一覧と窃取データを公開するTor上のDLS。被害者にはClient IDと初期パスワードが割り当てられる。2025年6〜7月はclearnetミラーdatapub[.]newsを運用し、2026年3月までに別の.onionアドレスへ移行した。 | 2025-04 | 2026-07 | 高 | `source--cisa-aa26-222a-gunra` |
| infrastructure--gunra-operation-double-barrel-network | Operation Double BarrelでGunraに関連付けられた共有ネットワーク資産 | AhnLabがGunra ransomware attack casesとして列挙したネットワークobservable群。176.65.128[.]26は、匿名のstate-sponsored threat groupによるOpenSSH reverse tunnelとGunraによる追加payload download/C2の双方で明示的に使用された。jshosting[.]meは両者の脆弱性悪用script配布に使用された。anyonecdn[.]comと4件の追加IPは、付録のwatering-hole側とGunra側の双方に掲載されるが、個別の役割はdownloadまたはC2のいずれかに限定できない。 | 不明 | 不明 | 高 | `source--ahnlab-operation-double-barrel-2026` |

### 配送・ファイル形式

未確認

### 脆弱性

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| vulnerability--cve-2024-55591 | CVE-2024-55591 | 特定バージョンのFortiOS/FortiProxyに影響する認証バイパス(CWE-288)。FBIがGunraによる悪用を観測している。悪用によりスーパーユーザー権限の永続アカウントforticloud-syncが作成される。 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| vulnerability--cve-2025-24472 | CVE-2025-24472 | 特定バージョンのFortiOS/FortiProxyに影響する認証バイパス(CWE-288)。FBIがGunraによる悪用を観測している。 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |

### 運用能力

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| opcap--gunra-raas | RaaSアフィリエイトプログラム運営 | 2026年1月にダークウェブフォーラムで開始。管理パネル、設定可能なランサムウェアビルダー、クロスプラットフォームのロッカー、アフィリエイト向け文書を提供する。 | 2026-01 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| opcap--gunra-iab-recruit | 初期アクセスブローカーの募集 | 企業ネットワークへのアクセス提供と引き換えに身代金の分配を提示し、ペネトレーションテスターやethical hackerを募集している。 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |

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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | ツール | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| KNPAが観測したSSL-VPN経由のVDI侵入とMFA回避を伴うランサムウェア展開 | intrusion | 不明 | 不明 | 2026-08-10 | target--gunra--country--south-korea | malware--gunra-ransomware |  | ttp--activity-rule--79e7281b8b02b45a190e, ttp--gunra-t1003, ttp--gunra-t1005, ttp--gunra-t1021-001, ttp--gunra-t1040, ttp--gunra-t1078-001, ttp--gunra-t1078-002, ttp--gunra-t1098, ttp--gunra-t1105, ttp--gunra-t1133, ttp--gunra-t1486, ttp--gunra-t1490, ttp--gunra-t1539, ttp--gunra-t1555, ttp--gunra-t1556-006, ttp--gunra-t1572 | victim--activity-rule--32917a8d98a0a8298a8e, victim--gunra-knpa-vdi | 韓国国家警察庁(KNPA)が観測した被害事例。攻撃者はインターネット公開VPNゲートウェイの資格情報露出とSSHアクセス制御の不備を悪用して不正な遠隔アクセスを得た。ある被害組織では、アカウントロックアウト制御がないSSL-VPN機器の管理者アカウントへ既定資格情報でアクセスし、攻撃者管理サーバーからOpenSSHを取得してSSHトンネルで持続化した。ネットワーク管理者の端末を経由してSSL-VPN管理コンソールへアクセスし、インターネット側と社内側の双方に接続できる未使用アカウントの強制パスワード変更要件を回避する設定変更を行った。SSL-VPN機器のトラフィック制御機能を操作してVDI認証ポータル利用者の資格情報とセッション情報を収集し、窃取したセッションCookieでセッションハイジャックを行い内部VDI環境へ侵入、RDPでVDI認証Webサーバー、内部ADサーバー、IT担当者の仮想デスクトップへ横展開した。さらに認証処理ファイルを改変して攻撃者指定のOTP値でMFAを継続的に回避し、Hiwareのアクセス制御サーバーから共通鍵を窃取して全企業サーバーの資格情報を復号したうえで、DBサーバーとNASを暗号化した。ランサムウェア展開の前後には、主データセンターと災害復旧センターの双方でバックアップとアーカイブデータを削除している。 | 高 | `source--cisa-aa26-222a-gunra` |
| Conti流出コード由来のロッカーによる二重恐喝とRaaSアフィリエイトプログラムの展開 | ransomware-extortion | 2025-04 | 2026-07 | 2026-08-10 | target--gunra--region--global, target--gunra--sector--academia, target--gunra--sector--critical-manufacturing, target--gunra--sector--financial-services, target--gunra--sector--government, target--gunra--sector--healthcare, target--gunra--sector--media, target--gunra--sector--professional-services, target--gunra--sector--retail, target--gunra--sector--transportation, target--gunra--sector--utilities | malware--gunra-main-exe, malware--gunra-ransomware |  | ttp--activity-rule--733895bfebede80e9001, ttp--gunra-t1003-003, ttp--gunra-t1005, ttp--gunra-t1021-002, ttp--gunra-t1047, ttp--gunra-t1048, ttp--gunra-t1049, ttp--gunra-t1059-003, ttp--gunra-t1070-003, ttp--gunra-t1083, ttp--gunra-t1106, ttp--gunra-t1114, ttp--gunra-t1190, ttp--gunra-t1486, ttp--gunra-t1490, ttp--gunra-t1530, ttp--gunra-t1550-002, ttp--gunra-t1550-003, ttp--gunra-t1560, ttp--gunra-t1567, ttp--gunra-t1622, ttp--gunra-t1657 | victim--activity-rule--59bc376b01842d5405da, victim--gunra-dls-multi-sector | FBIは2025年4月にGunraランサムウェアを初めて観測した。攻撃者はTor上にDLSを設置し、被害組織の一覧と窃取データを公開している。2026年1月にはダークウェブフォーラムで正式なRaaSアフィリエイトプログラムを開始し、管理パネル、設定可能なランサムウェアビルダー、クロスプラットフォームのロッカー、アフィリエイト向け文書を提供した。FBIはこの拡大に伴い、当該グループがGolden Communityという名称で活動する新たなブランドを採用したことを観測している。初期侵入はインターネットに露出したファイアウォール・VPN機器の既知脆弱性(CVE-2024-55591、CVE-2025-24472)の悪用が中心で、悪用によりスーパーユーザー権限の永続アカウントforticloud-syncが作成される。侵入後はImpacketによるSMB横展開とNTDSダンプ、Mimikatzによる資格情報取得、ログとコマンド履歴の削除、深夜〜早朝帯での偵察を行い、main.exeでOneDrive/SharePointから、7-Zip・RClone・FileZillaでファイル共有サービスMegaへ最大数十テラバイトを持ち出したうえで、ChaCha20 + RSA-4096により全ボリュームを暗号化する。身代金メモR3ADM3.txtで5〜7日以内の交渉開始を要求し、応じない場合はDLSでの公開と販売を脅迫する。 | 高 | `source--cisa-aa26-222a-gunra` |
| 2026年3月の韓国組織に対するGunraランサムウェア侵入 | ransomware-intrusion | 2026-03 | 2026-03 | 2026-07-30 | target--gunra--country--south-korea, target--gunra--sector--pharmaceuticals | malware--gunra-ransomware | tool--gunra-operation-double-barrel-filezilla, tool--gunra-operation-double-barrel-openssh, tool--gunra-psexec, tool--gunra-socat | ttp--gunra-double-barrel-t1003, ttp--gunra-double-barrel-t1021-001, ttp--gunra-double-barrel-t1021-004, ttp--gunra-double-barrel-t1046, ttp--gunra-double-barrel-t1055, ttp--gunra-double-barrel-t1059-001, ttp--gunra-double-barrel-t1070-001, ttp--gunra-double-barrel-t1070-004, ttp--gunra-double-barrel-t1105, ttp--gunra-double-barrel-t1189, ttp--gunra-double-barrel-t1203, ttp--gunra-double-barrel-t1486, ttp--gunra-double-barrel-t1543-003, ttp--gunra-double-barrel-t1569-002, ttp--gunra-double-barrel-t1572 | victim--gunra-operation-double-barrel-korea-2026 | AhnLabが2026年3月に確認した韓国の匿名組織への侵入事例。韓国の医療機関サイトをwatering holeとして金融セキュリティソフトウェアAの脆弱性を悪用し、正規のSyncHost.exeへcode injectionした。SyncHost.exeはnet.tmp(dropper)とinet.tmp(privilege-escalation tool)を作成・実行し、loaderをuploadmgrサービスとして登録した。攻撃者はOpenSSH reverse tunnelとSocat port forwardingを確立し、SSH sessionからnetwork rangeを走査、NTLM hashを窃取し、RDP/SSHで横展開した。集中管理ソリューションを悪用してhotfix.exeへ改名したPsExecからPowerShellを実行し、176.65.128[.]26:443より追加payloadを取得した。最終的にGunra ransomwareで暗号化し、FileZillaで組織データを持ち出した。報告の結論はGunra側の被害組織を韓国の医薬品会社と記載する。 | 高 | `source--ahnlab-operation-double-barrel-2026` |
| Operation Double Barrel技術重複（匿名state-sponsored cluster / Gunra） | technical-overlap-analysis | 2026-01 | 2026-03 | 2026-07-30 | target--gunra--country--south-korea, target--gunra--sector--academia, target--gunra--sector--pharmaceuticals | malware--gunra-ransomware | tool--gunra-operation-double-barrel-openssh, tool--gunra-psexec | ttp--gunra-double-barrel-t1055, ttp--gunra-double-barrel-t1070-004, ttp--gunra-double-barrel-t1189, ttp--gunra-double-barrel-t1203, ttp--gunra-double-barrel-t1543-003, ttp--gunra-double-barrel-t1572 | victim--gunra-operation-double-barrel-korea-2026 | AhnLabがOperation Double Barrelと名付けた、匿名のstate-sponsored threat groupによる2026年1月のwatering-hole intrusionと、Gunraによる2026年3月のransomware infectionの技術的重複を保持するGrouping。両者は同じ韓国医療機関サイト、金融セキュリティソフトウェアAの脆弱性、SyncHost.exeへのcode injection、net.tmp/_net.tmp・inet.tmp・uploadmgrの作成/登録pattern、inet.tmpの同一argument、同一SSH鍵fingerprint、OpenSSH tunnel、176.65.128[.]26、jshosting[.]me、四文字へrename後に削除するanti-forensic techniqueを共有した。AhnLabはhigh likelihood of technical linkageと評価する一方、collaboration、shared infrastructure、initial-access broker、operational-resource overlapのいずれかは確定せず、same actorとは結論していない。 | 中 | `source--ahnlab-operation-double-barrel-2026` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | ツール | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|---|
| KNPAが観測したSSL-VPN経由のVDI侵入とMFA回避を伴うランサムウェア展開 | Gunra | Gunra | 情報なし | T1490 Inhibit System Recovery, T1003 OS Credential Dumping, T1005 Data from Local System, T1021.001 Remote Services: Remote Desktop Protocol, T1040 Network Sniffing, T1078.001 Valid Accounts: Default Accounts, T1078.002 Valid Accounts: Domain Accounts, T1098 Account Manipulation, T1105 Ingress Tool Transfer, T1133 External Remote Services, T1486 Data Encrypted for Impact, T1490 Inhibit System Recovery, T1539 Steal Web Session Cookie, T1555 Credentials from Password Stores, T1556.006 Modify Authentication Process: Multi-Factor Authentication, T1572 Protocol Tunneling | 情報なし | 韓国 | 被害事例: KNPAが観測したSSL-VPN経由のVDI侵入とMFA回避を伴うランサムウェア展開, 被害事例: KNPAが観測したSSL-VPNからVDI環境への侵入とDB/NAS暗号化 | 高 |
| Conti流出コード由来のロッカーによる二重恐喝とRaaSアフィリエイトプログラムの展開 | Gunra | main.exe, Gunra | 情報なし | T1190 Exploit Public-Facing Application, T1003.003 OS Credential Dumping: NTDS, T1005 Data from Local System, T1021.002 Remote Services: SMB/Windows Admin Shares, T1047 Windows Management Instrumentation, T1048 Exfiltration Over Alternative Protocol, T1049 System Network Connections Discovery, T1059.003 Command and Scripting Interpreter: Windows Command Shell, T1070.003 Indicator Removal: Clear Command History, T1083 File and Directory Discovery, T1106 Native API, T1114 Email Collection, T1190 Exploit Public-Facing Application, T1486 Data Encrypted for Impact, T1490 Inhibit System Recovery, T1530 Data from Cloud Storage, T1550.002 Use Alternate Authentication Material: Pass the Hash, T1550.003 Use Alternate Authentication Material: Pass the Ticket, T1560 Archive Collected Data, T1567 Exfiltration Over Web Service, T1622 Debugger Evasion, T1657 Financial Theft | Tor上のDLSと交渉ポータル | 全世界, 学術, 重要製造業・建設, 金融サービス・保険, 政府サービス・施設, 医療・公衆衛生, メディア・通信, 専門サービス・非営利, 小売, 運輸・物流, 公益事業 | 被害事例: Conti流出コード由来のロッカーによる二重恐喝とRaaSアフィリエイトプログラムの展開, 被害事例: GunraのDLSに掲載された複数地域・複数業種の組織 | 高 |
| 2026年3月の韓国組織に対するGunraランサムウェア侵入 | Gunra | Gunra | FileZilla (Operation Double Barrel), OpenSSH (Operation Double Barrel), PsExec, Socat | T1003 OS Credential Dumping, T1021.001 Remote Services: Remote Desktop Protocol, T1021.004 Remote Services: SSH, T1046 Network Service Discovery, T1055 Process Injection, T1059.001 Command and Scripting Interpreter: PowerShell, T1070.001 Indicator Removal: Clear Windows Event Logs, T1070.004 Indicator Removal: File Deletion, T1105 Ingress Tool Transfer, T1189 Drive-by Compromise, T1203 Exploitation for Client Execution, T1486 Data Encrypted for Impact, T1543.003 Create or Modify System Process: Windows Service, T1569.002 System Services: Service Execution, T1572 Protocol Tunneling | Operation Double BarrelでGunraに関連付けられた共有ネットワーク資産 | 韓国, 医薬品 | 被害事例: Operation Double BarrelでGunraに感染した韓国の匿名組織 | 高 |
| Operation Double Barrel技術重複（匿名state-sponsored cluster / Gunra） | Gunra | Gunra | OpenSSH (Operation Double Barrel), PsExec | T1055 Process Injection, T1070.004 Indicator Removal: File Deletion, T1189 Drive-by Compromise, T1203 Exploitation for Client Execution, T1486 Data Encrypted for Impact, T1543.003 Create or Modify System Process: Windows Service, T1572 Protocol Tunneling | Operation Double BarrelでGunraに関連付けられた共有ネットワーク資産 | 韓国, 学術, 医薬品 | 被害事例: Operation Double BarrelでGunraに感染した韓国の匿名組織 | 中 |

2025年4月にFBIが初観測。同年6〜7月にはTor上のDLSのclearnet mirror datapub[.]newsを運用した。2025年半ばにLinux版が追加され、2026年1月にRaaS affiliate programを開始した。AhnLabは2026年1月の匿名cluster事例と3月のGunra感染をOperation Double Barrelとして比較した。DLSは2026年3月までに別の.onion addressへ移行し、2026年7月まで観測されている。

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 韓国 | 韓国国家警察庁(KNPA)が共同署名機関として国内の被害事例(SSL-VPN管理者アカウント侵害からVDI環境への侵入とDB/NASの暗号化)を提供している。 | 不明 | 不明 | 中 | `source--cisa-aa26-222a-gunra` |
| regions | 全世界 | 勧告は被害組織がAmericas、Europe、Middle East、Africa、Asia-Pacificにまたがると記載している。 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| sectors | 学術 | 勧告のIntended Audienceおよび被害業種一覧に明記されている。 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| sectors | 重要製造業・建設 | 勧告のIntended Audienceおよび被害業種一覧に明記されている。 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| sectors | 金融サービス・保険 | 勧告のIntended Audienceおよび被害業種一覧に明記されている。 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| sectors | 政府サービス・施設 | 勧告のIntended Audienceおよび被害業種一覧に明記されている。 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| sectors | 医療・公衆衛生 | 勧告のIntended Audienceおよび被害業種一覧に明記されている。 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| sectors | メディア・通信 | 勧告のIntended Audienceおよび被害業種一覧に明記されている。 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| sectors | 専門サービス・非営利 | 勧告のIntended Audienceおよび被害業種一覧に明記されている。 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| sectors | 小売 | 勧告のIntended Audienceおよび被害業種一覧に明記されている。 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| sectors | 運輸・物流 | 勧告のIntended Audienceおよび被害業種一覧に明記されている。 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| sectors | 公益事業 | 勧告のIntended Audienceおよび被害業種一覧に明記されている。 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| sectors | 医薬品 | AhnLabはOperation Double Barrelで、Gunra ransomware attackが韓国の医薬品会社を標的にしたと明記している。 | 2026-03 | 2026-03 | 高 | `source--ahnlab-operation-double-barrel-2026` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: KNPAが観測したSSL-VPN経由のVDI侵入とMFA回避を伴うランサムウェア展開 | 非公開 | aggregate | multiple-organizations | reported | target--gunra--country--south-korea | malware--gunra-ransomware | ttp--activity-rule--79e7281b8b02b45a190e, ttp--gunra-t1003, ttp--gunra-t1005, ttp--gunra-t1021-001, ttp--gunra-t1040, ttp--gunra-t1078-001, ttp--gunra-t1078-002, ttp--gunra-t1098, ttp--gunra-t1105, ttp--gunra-t1133, ttp--gunra-t1486, ttp--gunra-t1490, ttp--gunra-t1539, ttp--gunra-t1555, ttp--gunra-t1556-006, ttp--gunra-t1572 | VPN／リモートアクセス機器, サーバー, エンドポイント, OT／ICS | encryption: KNPAが観測したSSL-VPN経由のVDI侵入とMFA回避を伴うランサムウェア展開 | 不明 | 不明 | 2026-08-10 | 高 | `source--cisa-aa26-222a-gunra` |
| 被害事例: Conti流出コード由来のロッカーによる二重恐喝とRaaSアフィリエイトプログラムの展開 | 非公開 | aggregate | multiple-organizations | reported | target--gunra--region--global, target--gunra--sector--academia, target--gunra--sector--critical-manufacturing, target--gunra--sector--financial-services, target--gunra--sector--government, target--gunra--sector--healthcare, target--gunra--sector--media, target--gunra--sector--professional-services, target--gunra--sector--retail, target--gunra--sector--transportation, target--gunra--sector--utilities | malware--gunra-main-exe, malware--gunra-ransomware | ttp--activity-rule--733895bfebede80e9001, ttp--gunra-t1003-003, ttp--gunra-t1005, ttp--gunra-t1021-002, ttp--gunra-t1047, ttp--gunra-t1048, ttp--gunra-t1049, ttp--gunra-t1059-003, ttp--gunra-t1070-003, ttp--gunra-t1083, ttp--gunra-t1106, ttp--gunra-t1114, ttp--gunra-t1190, ttp--gunra-t1486, ttp--gunra-t1490, ttp--gunra-t1530, ttp--gunra-t1550-002, ttp--gunra-t1550-003, ttp--gunra-t1560, ttp--gunra-t1567, ttp--gunra-t1622, ttp--gunra-t1657 | VPN／リモートアクセス機器, ネットワーク機器 | data-theft: 侵入後はImpacketによるSMB横展開とNTDSダンプ、Mimikatzによる資格情報取得、ログとコマンド履歴の削除、深夜〜早朝帯での偵察を行い、main.exeでOneDrive/SharePointから、7-Zip・RClone・FileZillaでファイル共有サービスMegaへ最大数十テラバイトを持ち出したうえで、ChaCha20 + RSA-4096により全ボリュームを暗号化する。<br>encryption: FBIは2025年4月にGunraランサムウェアを初めて観測した。 | 2025-04 | 2026-07 | 2026-08-10 | 高 | `source--cisa-aa26-222a-gunra` |
| 被害事例: GunraのDLSに掲載された複数地域・複数業種の組織 | 非公開 | aggregate | multiple-organizations | reported | target--gunra--sector--healthcare, target--gunra--sector--financial-services, target--gunra--sector--critical-manufacturing, target--gunra--sector--transportation, target--gunra--sector--government, target--gunra--sector--utilities, target--gunra--sector--academia, target--gunra--sector--media, target--gunra--sector--retail, target--gunra--sector--professional-services, target--gunra--region--global | malware--gunra-ransomware | ttp--gunra-t1486, ttp--gunra-t1657 | ファイルサーバー, 業務文書, データベース, 個人情報, 社内メール, Microsoft OneDrive, Microsoft SharePoint | data-theft: 窃取データのDLS公開および販売の脅迫。<br>encryption: Windows/Linux環境のファイル暗号化。 | 2025-04 | 2026-07 | 2026-08-10 | 高 | `source--cisa-aa26-222a-gunra` |
| 被害事例: KNPAが観測したSSL-VPNからVDI環境への侵入とDB/NAS暗号化 | 非公開 | anonymous | organization | reported | target--gunra--country--south-korea | malware--gunra-ransomware | ttp--gunra-t1133, ttp--gunra-t1078-001, ttp--gunra-t1098, ttp--gunra-t1556-006, ttp--gunra-t1555, ttp--gunra-t1486 | SSL-VPN機器, VDI認証Webサーバー, 内部Active Directoryサーバー, IT担当者の仮想デスクトップ, Hiwareアクセス制御サーバー, データベースサーバー, NAS, バックアップ基盤 | credential-theft: 全企業サーバーの資格情報ダンプ。<br>encryption: DBサーバーとNASの暗号化。<br>data-theft: システム・ネットワーク構成情報を含む文書の収集。 | 不明 | 不明 | 2026-08-10 | 高 | `source--cisa-aa26-222a-gunra` |
| 被害事例: Operation Double BarrelでGunraに感染した韓国の匿名組織 | 非公開 | anonymous | organization | reported | target--gunra--country--south-korea, target--gunra--sector--pharmaceuticals | malware--gunra-ransomware | ttp--gunra-double-barrel-t1189, ttp--gunra-double-barrel-t1203, ttp--gunra-double-barrel-t1486 | Windows endpoints, 組織データ, 集中管理ソリューション | data-theft: 組織データを収集しFileZillaで持ち出した。<br>encryption: Gunra ransomwareでfilesを暗号化した。 | 2026-03 | 2026-03 | 2026-07-30 | 高 | `source--ahnlab-operation-double-barrel-2026` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Initial Access | T1190 | Exploit Public-Facing Application | 初期侵入はインターネットに露出したファイアウォール・VPN機器の既知脆弱性(CVE-2024-55591、CVE-2025-24472)の悪用が中心で、悪用によりスーパーユーザー権限の永続アカウントforticloud-syncが作成される。 |  | activity--gunra-raas-2025-2026 | 2025-04 | 2026-07 | 中 | `source--cisa-aa26-222a-gunra` |
| Impact | T1490 | Inhibit System Recovery | ランサムウェア展開の前後には、主データセンターと災害復旧センターの双方でバックアップとアーカイブデータを削除している。 |  | activity--gunra-knpa-vdi-intrusion-2025 | 不明 | 不明 | 中 | `source--cisa-aa26-222a-gunra` |
| Credential Access | T1003 | OS Credential Dumping | 窃取した共通鍵により全企業サーバーに関連する資格情報のダンプを行った。 |  | activity--gunra-knpa-vdi-intrusion-2025 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| Credential Access | T1003.003 | OS Credential Dumping: NTDS | Impacketのsecretsdump.pyで侵害したドメインコントローラーからNTDSのパスワードハッシュを取得した。 |  | activity--gunra-raas-2025-2026 | 2025-04 | 2026-07 | 高 | `source--cisa-aa26-222a-gunra` |
| Collection | T1005 | Data from Local System | 業務上重要な文書、データベース、PII、社内メールを収集する。KNPAの事例ではIT担当者のVDI環境からシステム・ネットワーク構成情報を含む文書を収集した。 |  | activity--gunra-raas-2025-2026, activity--gunra-knpa-vdi-intrusion-2025 | 2025-04 | 2026-07 | 高 | `source--cisa-aa26-222a-gunra` |
| Lateral Movement | T1021.001 | Remote Services: Remote Desktop Protocol | 窃取したセッション情報で内部VDI環境へ侵入し、RDPでVDI認証Webサーバー、内部ADサーバー、IT担当者の仮想デスクトップへ横展開した。 |  | activity--gunra-knpa-vdi-intrusion-2025 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| Lateral Movement | T1021.002 | Remote Services: SMB/Windows Admin Shares | Impacketのpsexec.pyとsmbclient.pyを用いてSMB経由で横展開する。 |  | activity--gunra-raas-2025-2026 | 2025-04 | 2026-07 | 高 | `source--cisa-aa26-222a-gunra` |
| Credential Access | T1040 | Network Sniffing | SSL-VPN機器のトラフィック制御機能を操作し、企業VDI認証ポータルへ認証する利用者の資格情報とセッション情報を収集した。 |  | activity--gunra-knpa-vdi-intrusion-2025 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| Execution | T1047 | Windows Management Instrumentation | WMIを用いて暗号化前にボリュームシャドウコピーの削除を開始する。 |  | activity--gunra-raas-2025-2026 | 2025-04 | 2026-07 | 高 | `source--cisa-aa26-222a-gunra` |
| Exfiltration | T1048 | Exfiltration Over Alternative Protocol | 7-Zip、RClone、FileZillaを用いて収集データを持ち出す。 |  | activity--gunra-raas-2025-2026 | 2025-04 | 2026-07 | 高 | `source--cisa-aa26-222a-gunra` |
| Discovery | T1049 | System Network Connections Discovery | 管理者による検知を避けるため、内部インフラの偵察を深夜から早朝(22時〜6時)に実施する。 |  | activity--gunra-raas-2025-2026 | 2025-04 | 2026-07 | 高 | `source--cisa-aa26-222a-gunra` |
| Execution | T1059.003 | Command and Scripting Interpreter: Windows Command Shell | cmd.exe経由でWMIC.exeを実行し、ボリュームシャドウコピーを削除する。 |  | activity--gunra-raas-2025-2026 | 2025-04 | 2026-07 | 高 | `source--cisa-aa26-222a-gunra` |
| Defense Evasion | T1070.003 | Indicator Removal: Clear Command History | 被害ネットワーク内でコマンド履歴を消去する。 |  | activity--gunra-raas-2025-2026 | 2025-04 | 2026-07 | 高 | `source--cisa-aa26-222a-gunra` |
| Defense Evasion | T1078.001 | Valid Accounts: Default Accounts | SSL-VPN機器の既定資格情報を悪用して管理者権限を取得した。 |  | activity--gunra-knpa-vdi-intrusion-2025 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| Defense Evasion | T1078.002 | Valid Accounts: Domain Accounts | 侵害したドメインアカウントを用いて内部システムへアクセスした。 |  | activity--gunra-knpa-vdi-intrusion-2025 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| Discovery | T1083 | File and Directory Discovery | 暗号化前にA〜Zの全ドライブでファイルとディレクトリを探索し、対象データを特定する。 |  | activity--gunra-raas-2025-2026 | 2025-04 | 2026-07 | 高 | `source--cisa-aa26-222a-gunra` |
| Persistence | T1098 | Account Manipulation | SSL-VPN管理コンソール上で未使用アカウントの設定を変更し、強制パスワード変更要件を回避して悪用可能にした。 |  | activity--gunra-knpa-vdi-intrusion-2025 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| Command and Control | T1105 | Ingress Tool Transfer | 攻撃者管理の外部サーバーからOpenSSHを取得した。 |  | activity--gunra-knpa-vdi-intrusion-2025 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| Execution | T1106 | Native API | Windows版ロッカーがFindFirstFileW/FindNextFileW APIでA〜Zの全ドライブのファイルとディレクトリを列挙する。 |  | activity--gunra-raas-2025-2026 | 2025-04 | 2026-07 | 高 | `source--cisa-aa26-222a-gunra` |
| Collection | T1114 | Email Collection | 社内メール通信を収集対象に含める。 |  | activity--gunra-raas-2025-2026 | 2025-04 | 2026-07 | 高 | `source--cisa-aa26-222a-gunra` |
| Initial Access | T1133 | External Remote Services | SSL-VPN機器の管理者アカウントへ、アカウントロックアウト制御がない状態で既定資格情報を用いてアクセスした。 |  | activity--gunra-knpa-vdi-intrusion-2025 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| Initial Access | T1190 | Exploit Public-Facing Application | インターネットに露出したファイアウォール・VPN機器の既知脆弱性(CVE-2024-55591、CVE-2025-24472)を悪用して初期侵入する。悪用によりスーパーユーザー権限の永続アカウントforticloud-syncが作成される。 |  | activity--gunra-raas-2025-2026 | 2025-04 | 2026-07 | 高 | `source--cisa-aa26-222a-gunra` |
| Impact | T1486 | Data Encrypted for Impact | マルチスレッド構成のロッカーがChaCha20 + RSA-4096で高速に全ファイルシステムを暗号化し、拡張子.ENCRTを付与する。KNPAの事例では窃取した企業サーバー資格情報を用いてDBサーバーとNASを暗号化した。 |  | activity--gunra-raas-2025-2026, activity--gunra-knpa-vdi-intrusion-2025 | 2025-04 | 2026-07 | 高 | `source--cisa-aa26-222a-gunra` |
| Impact | T1490 | Inhibit System Recovery | 暗号化前にボリュームシャドウコピーを削除する。ある被害組織ではランサムウェア展開の前後に主データセンターと災害復旧センターの双方でバックアップとアーカイブデータを削除した。 |  | activity--gunra-raas-2025-2026, activity--gunra-knpa-vdi-intrusion-2025 | 2025-04 | 2026-07 | 高 | `source--cisa-aa26-222a-gunra` |
| Collection | T1530 | Data from Cloud Storage | 悪性実行ファイルmain.exeでMicrosoft OneDriveとSharePointから被害データを持ち出す。 |  | activity--gunra-raas-2025-2026 | 2025-04 | 2026-07 | 高 | `source--cisa-aa26-222a-gunra` |
| Credential Access | T1539 | Steal Web Session Cookie | 窃取したセッションCookieでセッションハイジャックを行い、正規利用者になりすまして内部ネットワークへアクセスした。 |  | activity--gunra-knpa-vdi-intrusion-2025 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| Lateral Movement | T1550.002 | Use Alternate Authentication Material: Pass the Hash | 取得したハッシュを用いて他の特権システムへ横展開した。 |  | activity--gunra-raas-2025-2026 | 2025-04 | 2026-07 | 高 | `source--cisa-aa26-222a-gunra` |
| Lateral Movement | T1550.003 | Use Alternate Authentication Material: Pass the Ticket | 取得した認証情報を用いて他の特権システムへ横展開した。 |  | activity--gunra-raas-2025-2026 | 2025-04 | 2026-07 | 高 | `source--cisa-aa26-222a-gunra` |
| Credential Access | T1555 | Credentials from Password Stores | 侵害した仮想デスクトップからSSHでHiwareのアクセス制御サーバーへ接続し、保管されていた共通鍵を窃取してDB内の企業サーバーアカウントのパスワードを復号した。 |  | activity--gunra-knpa-vdi-intrusion-2025 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| Credential Access | T1556.006 | Modify Authentication Process: Multi-Factor Authentication | VDI認証ポータルサーバーの認証処理ファイルを改変し、攻撃者が指定した特定のOTP値で認証が通るようにしてMFAを継続的に回避した。 |  | activity--gunra-knpa-vdi-intrusion-2025 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| Collection | T1560 | Archive Collected Data | 機微データを圧縮アーカイブへまとめてから持ち出す。 |  | activity--gunra-raas-2025-2026 | 2025-04 | 2026-07 | 高 | `source--cisa-aa26-222a-gunra` |
| Exfiltration | T1567 | Exfiltration Over Web Service | 作成したアーカイブをファイル共有サービスMegaへ持ち出す。持ち出し量は最大で数十テラバイトに及ぶ。 |  | activity--gunra-raas-2025-2026 | 2025-04 | 2026-07 | 高 | `source--cisa-aa26-222a-gunra` |
| Command and Control | T1572 | Protocol Tunneling | 侵害システム間にSSHトンネルを確立して持続化した。 |  | activity--gunra-knpa-vdi-intrusion-2025 | 不明 | 不明 | 高 | `source--cisa-aa26-222a-gunra` |
| Defense Evasion | T1622 | Debugger Evasion | Windows版ロッカーがIsDebuggerPresent APIでデバッガ実行を検知し、リバースエンジニアリングを妨害する。 |  | activity--gunra-raas-2025-2026 | 2025-04 | 2026-07 | 高 | `source--cisa-aa26-222a-gunra` |
| Impact | T1657 | Financial Theft | 指定した暗号資産ウォレットアドレスへの身代金支払いを要求し、交渉は数千万米ドル規模から開始される。 |  | activity--gunra-raas-2025-2026 | 2025-04 | 2026-07 | 高 | `source--cisa-aa26-222a-gunra` |
| Credential Access | T1003 | OS Credential Dumping | 2026年3月のGunra感染事例で、管理不十分なWindows Server 2003からNTLM hashを窃取した。 |  | activity--gunra-operation-double-barrel-incident-2026-03 | 2026-03 | 2026-03 | 高 | `source--ahnlab-operation-double-barrel-2026` |
| Lateral Movement | T1021.001 | Remote Services: Remote Desktop Protocol | 2026年3月のGunra感染事例で、窃取した資格情報を使用してRDPで内部移動した。 |  | activity--gunra-operation-double-barrel-incident-2026-03 | 2026-03 | 2026-03 | 高 | `source--ahnlab-operation-double-barrel-2026` |
| Command and Control | T1105 | Ingress Tool Transfer | AhnLabが報告したGunra事例で、hotfix.exeへ改名したPsExecからPowerShellを実行し、176.65.128[.]26:443から追加payloadを取得した。 |  | activity--gunra-operation-double-barrel-incident-2026-03 | 不明 | 不明 | 高 | `source--ahnlab-operation-double-barrel-2026` |
| Impact | T1486 | Data Encrypted for Impact | 2026年3月のGunra感染事例で、最終的にGunra ransomwareを実行して組織内filesを暗号化した。 | malware--gunra-ransomware | activity--gunra-operation-double-barrel-incident-2026-03 | 2026-03 | 2026-03 | 高 | `source--ahnlab-operation-double-barrel-2026` |
| Command and Control | T1572 | Protocol Tunneling | 匿名state-sponsored cluster側の2026年1月事例とGunra側の2026年3月事例でOpenSSH reverse tunnelが確認され、Gunra側ではSocat port forwardingも使用された。両事例のOpenSSHは同一SSH鍵fingerprintを使用した。 |  | activity--gunra-operation-double-barrel-incident-2026-03, activity--operation-double-barrel-technical-overlap-2026 | 2026-01 | 2026-03 | 高 | `source--ahnlab-operation-double-barrel-2026` |
| Lateral Movement | T1021.004 | Remote Services: SSH | 2026年3月のGunra感染事例で、OpenSSHを設置してpublic-key loginを行い、SSHを内部移動とremote controlに使用した。 |  | activity--gunra-operation-double-barrel-incident-2026-03 | 2026-03 | 2026-03 | 高 | `source--ahnlab-operation-double-barrel-2026` |
| Discovery | T1046 | Network Service Discovery | 2026年3月のGunra感染事例で、SSH sessionから内部network rangeをscanした。 |  | activity--gunra-operation-double-barrel-incident-2026-03 | 2026-03 | 2026-03 | 高 | `source--ahnlab-operation-double-barrel-2026` |
| Defense Evasion | T1055 | Process Injection | 2026年1月の匿名state-sponsored側と2026年3月のGunra側の双方で、金融セキュリティソフトウェアAのcrash後に正規のSyncHost.exeへmalicious codeをinjectした。 |  | activity--gunra-operation-double-barrel-incident-2026-03, activity--operation-double-barrel-technical-overlap-2026 | 2026-01 | 2026-03 | 高 | `source--ahnlab-operation-double-barrel-2026` |
| Execution | T1059.001 | Command and Scripting Interpreter: PowerShell | Gunra attackerはhotfix.exeへ改名したPsExecからPowerShell DownloadStringを実行し、176.65.128[.]26:443から追加payloadを取得した。 |  | activity--gunra-operation-double-barrel-incident-2026-03 | 不明 | 不明 | 高 | `source--ahnlab-operation-double-barrel-2026` |
| Defense Evasion | T1070.001 | Indicator Removal: Clear Windows Event Logs | 2026年3月のGunra感染事例でsystem event logsを削除した。 |  | activity--gunra-operation-double-barrel-incident-2026-03 | 2026-03 | 2026-03 | 高 | `source--ahnlab-operation-double-barrel-2026` |
| Defense Evasion | T1070.004 | Indicator Removal: File Deletion | 匿名state-sponsored側とGunra側の双方で、malwareをrandomな四文字名へrenameしてから削除するanti-forensic patternを使用した。 |  | activity--gunra-operation-double-barrel-incident-2026-03, activity--operation-double-barrel-technical-overlap-2026 | 2026-01 | 2026-03 | 高 | `source--ahnlab-operation-double-barrel-2026` |
| Initial Access | T1189 | Drive-by Compromise | 匿名state-sponsored側とGunra側の双方で、同じ韓国医療機関websiteをwatering holeとして利用し、選別されたvisitorをvulnerability exploitationへ誘導した。 |  | activity--gunra-operation-double-barrel-incident-2026-03, activity--operation-double-barrel-technical-overlap-2026 | 2026-01 | 2026-03 | 高 | `source--ahnlab-operation-double-barrel-2026` |
| Execution | T1203 | Exploitation for Client Execution | 2026年1月と3月の両事例で、韓国の金融セキュリティソフトウェアAの同じ脆弱性をexploitしてinitial shellcodeを実行した。 |  | activity--gunra-operation-double-barrel-incident-2026-03, activity--operation-double-barrel-technical-overlap-2026 | 2026-01 | 2026-03 | 高 | `source--ahnlab-operation-double-barrel-2026` |
| Persistence | T1543.003 | Create or Modify System Process: Windows Service | 両事例でloaderをWindows serviceとして登録し、uploadmgrというservice nameを高頻度に使用した。 |  | activity--gunra-operation-double-barrel-incident-2026-03, activity--operation-double-barrel-technical-overlap-2026 | 2026-01 | 2026-03 | 高 | `source--ahnlab-operation-double-barrel-2026` |
| Execution | T1569.002 | System Services: Service Execution | Gunra attackerはhotfix.exeへrenameしたPsExecからPowerShell commandを実行した。 |  | activity--gunra-operation-double-barrel-incident-2026-03 | 不明 | 不明 | 高 | `source--ahnlab-operation-double-barrel-2026` |

## IOC／artifact概要

- IOC値: 11件
- IOC観測: 11件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 17件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| Gunraは2025年4月に出現し、2026年1月にRaaSへ発展した金銭目的のランサムウェア運用主体であり、複数国の政府機関・重要インフラを含む幅広い業種を標的としている。 | 高 | `source--cisa-aa26-222a-gunra` |  |
| GunraのランサムウェアはContiの流出ソースコードに由来するが、これはコード系譜であり、Conti運用主体との同一性を示すものではない。 | 高 | `source--cisa-aa26-222a-gunra` | 勧告は「derived from the leaked Conti ransomware source code」「appears to be based on, or significantly influenced by」と記載する。既存のBlackByte等Conti系aliasを持つプロファイルへは統合しない。 |
| 初期侵入はインターネット公開のファイアウォール・VPN機器の既知脆弱性悪用と既定資格情報の悪用が中心であり、エッジ機器のパッチ適用と資格情報管理が主要な防御点である。 | 高 | `source--cisa-aa26-222a-gunra` |  |
| AhnLabが比較した2026年1月の匿名state-sponsored threat group事例と2026年3月のGunra感染事例には、同じwatering holeと脆弱性、SyncHost.exe injection、file/service/argument pattern、SSH key fingerprint、network infrastructure、anti-forensic techniqueが重複する。技術的リンクの可能性は高いが、same actor、collaboration、shared infrastructure、initial-access brokerのいずれかは確定できない。 | 中 | `source--ahnlab-operation-double-barrel-2026` | AhnLab自身がsame actorとの結論を否定し、追加証拠が必要と明記する。Gunraをstate-sponsoredへ変更せず、匿名clusterをLazarus/COPPERHEDGE利用者へ同一視しない。 |

### 情報ギャップ

- 個別の被害組織名と各被害の発生時期が公開されていないため、被害規模と時系列を定量化できない。
- アフィリエイトごとのクラスタ分離ができておらず、どの侵入がコア運用主体によるものかを区別できない。
- Golden Communityブランドでの活動を示す独立した一次資料を未取得のため、alias scopeをoverlappingに留めている。
- 勧告が参照するTrend Micro、CYFIRMA、CloudSEK、Breakglass Intelligence各社の報告を原文未確認のため、Linux版の暗号化実装上の欠陥等はプロファイルへ取り込んでいない。
- Operation Double Barrelの匿名state-sponsored clusterには安定した名称、帰属国、組織対応がなく、別Actor/Intrusion Setへ昇格できない。
- AhnLab appendixのGunra IOCは個別のfirst/last observedを示さないため、publication dateとは分離してunknownのまま保持する。

### 不確実性

- 勧告はGunraをランサムウェアファミリー名としても運用主体名としても用いており、両者の境界が資料上明確でない。
- Contiの流出コード由来という評価は他のConti派生ファミリーとも共通するため、コード類似性のみでのクラスタ同定はできない。
- Operation Double Barrelの重複はcollaboration、shared infrastructure、initial-access broker、operational-resource overlapの複数仮説で説明可能であり、現時点でmechanismを選べない。
- Brandoor/COPPERHEDGE型のfile-creation traceはGunra事例のlogsで確認されたがfilesは回収されておらず、BrandoorをGunraの確定malware capabilityとは扱わない。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--cisa-aa26-222a-gunra | #StopRansomware: Gunra Ransomware (AA26-222A) | FBI / CISA / DC3 / NSA / USSS / 韓国国家警察庁(KNPA) | 2026-08-10 | https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-222a | government-advisory | TLP:CLEAR | 高 |
| source--ahnlab-operation-double-barrel-2026 | APT Group Tracking Report: Operation Double Barrel | AhnLab SEcurity intelligence Center (ASEC) | 2026-07-30 | https://image.ahnlab.com/atip/content/file/20260730/[AhnLab]Operation%20Double%20Barrel(ENG)(2026.07.30).pdf | vendor-research | TLP:CLEAR | 高 |

## 自由記述

GunraはBlackByteのcatalog alias「Conti」経由で誤一致していたが、Contiとの関係はcode lineageのみである。Operation Double Barrelの匿名state-sponsored clusterも安定した名称や国帰属がなく、LazarusやCOPPERHEDGE利用者とのexact identityへ昇格しない。技術的重複はGroupingに閉じ込め、根拠のないcollaborates-with relationshipを生成しない。
