# Head Mare 脅威アクタープロファイル

- プロファイルID: `actor--head-mare`
- 状態: draft
- 更新日時: 2026-08-10T07:28:34Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Head Mareは2023年に出現し、ロシアとベラルーシの組織へ被害を与えることを目的とするハクティビスト集団である。独自バックドアPhantomCore系統を一貫して運用し、2026年8月には未更新のTrueConf Serverを侵害して正規クライアントインストーラーを汚染する組織内サプライチェーン攻撃が確認された。

## アクター名とAlias

- 正規名: **Head Mare**
- 初回観測: 2023
- 最終観測: 2026-07
- 活動状態: yes

Aliasなし

## 帰属

一次資料は国家帰属を示していない。Kasperskyはハクティビスト集団と分類し、ロシア・ベラルーシ組織への加害を目的とすると評価している。帰属国は確認できないため空のままとし、標的国から攻撃元国を推定しない。

- 国: 不明
- スポンサー種別: hacktivist
- 確度: 中
- 証拠: `source--kaspersky-head-mare-2024`, `source--kaspersky-head-mare-trueconf-2026`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| hacktivism | 対象企業への被害最大化を主目的とすると一次資料が評価している。 | 高 | `source--kaspersky-head-mare-2024` |  |
| financial | ランサムウェア展開に伴う身代金要求も併用する。主目的とは区別する。 | 中 | `source--kaspersky-head-mare-2024` |  |

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | ロシア・ベラルーシ組織を標的とするハクティビスト集団Head Mare。国家帰属は不明。 |
| Capability | 独自バックドアPhantomDL/PhantomCore/PhantomGraph、LockBitとBabukのランサムウェア、Sliver、Mimikatz、ngrok、rsockstun。 |
| Infrastructure | フィッシング配信基盤、侵害したTrueConf Server上のWebシェル、C2として悪用するMicrosoft OneDrive、リバースSSHトンネル先。 |
| Victim | ロシアとベラルーシの政府機関、運輸、エネルギー、製造、エンターテインメント、計測機器、電子、IT、ソフトウェア開発分野の組織。 |
| Socio-political | ロシア・ウクライナ戦争を背景とする対ロシア・ベラルーシのハクティビズム。 |

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--babuk | Babuk | Linux/ESXi環境で使用するランサムウェア。Head Mare独自の開発ではなく流用である。 | 不明 | 不明 | 高 | `source--kaspersky-head-mare-2024` |
| malware--lockbit | LockBit | Windows環境で使用するランサムウェア。Head Mare独自の開発ではなく流用である。 | 不明 | 不明 | 高 | `source--kaspersky-head-mare-2024` |
| malware--phantomcore | PhantomCore | Head Mareの独自RAT。C2からのファイル取得、侵害ホストからのファイル送出、cmd.exe経由のコマンド実行を行う。初期はGo製、後にC++製が確認されている。 | 2023 | 2026-07 | 高 | `source--daily-fff05927bf91551e1b96`, `source--kaspersky-head-mare-2024`, `source--kaspersky-head-mare-trueconf-2026` |
| malware--phantomdl | PhantomDL | フィッシング経由で配布される独自ダウンローダー/バックドア。PhantomCoreの後継として記載される。 | 2023 | 不明 | 高 | `source--kaspersky-head-mare-2024` |
| malware--phantomgraph | PhantomGraph | SysExcSvc.dllとSysReadSvc.dllの2モジュールで構成されるバックドア。Microsoft OneDriveをC2として命令を取得し、LSASSメモリダンプ、偵察、リバースSSHトンネルを実行する。 | 2026-07 | 不明 | 高 | `source--daily-fff05927bf91551e1b96`, `source--kaspersky-head-mare-trueconf-2026` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--sliver | Sliver | 侵害後の指令統制に使用するオープンソースC2フレームワーク。 | 不明 | 不明 | 高 | `source--kaspersky-head-mare-2024` |
| tool--mimikatz | Mimikatz | 資格情報窃取に使用する公開ツール。 | 不明 | 不明 | 高 | `source--kaspersky-head-mare-2024` |
| tool--ngrok | ngrok | 内部ホストの外部公開・トンネリングに使用する正規サービス。 | 不明 | 不明 | 高 | `source--kaspersky-head-mare-2024` |
| tool--rsockstun | rsockstun | リバースSOCKSトンネルの構築に使用する公開ツール。 | 不明 | 不明 | 高 | `source--kaspersky-head-mare-2024` |

### インフラ

未確認

### 配送・ファイル形式

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| delivery--rar-archive | 悪性RARアーカイブ | CVE-2023-38831を悪用するよう細工したRARアーカイブをフィッシングメールに添付する。 | 不明 | 不明 | 高 | `source--kaspersky-head-mare-2024` |
| delivery--trojanized-installer | 汚染TrueConf Clientインストーラー | 侵害したTrueConf Serverから配布される未署名のバックドア入りクライアント更新。 | 不明 | 不明 | 高 | `source--kaspersky-head-mare-trueconf-2026` |

### 脆弱性

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| vuln--cve-2023-38831 | CVE-2023-38831 | WinRARのアーカイブ処理の脆弱性。細工した書庫を開かせることで任意コード実行が可能。 | 不明 | 不明 | 高 | `source--kaspersky-head-mare-2024` |
| vuln--klcert-26-057 | KLCERT-26-057 | TrueConf Serverの脆弱性。KLCERT-26-058と連鎖させることで認証なしのSYSTEM権限コード実行に至る。5.3.9、5.4.9、5.5.5で修正され、修正版は2026-06-18に公開された。 | 不明 | 不明 | 高 | `source--kaspersky-head-mare-trueconf-2026` |
| vuln--klcert-26-058 | KLCERT-26-058 | TrueConf Serverの脆弱性。KLCERT-26-057と連鎖して悪用される。 | 不明 | 不明 | 高 | `source--kaspersky-head-mare-trueconf-2026` |

### 運用能力

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| opcap--supply-chain-via-trusted-server | 信頼済みサーバー経由の配布汚染 | 侵害した社内サーバーの正規配布物を差し替え、組織内の利用者へ更新として配布する。 | 不明 | 不明 | 高 | `source--kaspersky-head-mare-trueconf-2026` |
| opcap--multi-vector-initial-access | 多経路の初期侵入 | フィッシング、公開Webサーバーの脆弱性悪用、請負業者経由の侵入を使い分ける。 | 不明 | 不明 | 高 | `source--kaspersky-head-mare-trueconf-2026` |

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ハッカーがTrueConfを侵害し、クライアントインストーラーをバックドア入りに改ざん | infrastructure-operation | 2026-07 | 不明 | 2026-08-10 | target--head-mare--country--russia, target--head-mare--sector--energy, target--head-mare--sector--instrumentation, target--head-mare--sector--software-development | malware--phantomcore, malware--phantomgraph | ttp--activity-rule--209e363ca5019e2456f9, ttp--head-mare-t1003-001-lsass, ttp--head-mare-t1102-onedrive, ttp--head-mare-t1190-trueconf, ttp--head-mare-t1195-002-installer, ttp--head-mare-t1505-003-webshell, ttp--head-mare-t1572-ssh | victim--activity-rule--2e3159757028597a3b7a, victim--head-mare-trueconf-2026 | ハクティビスト集団Head Mareは、未更新のTrueConf Serverに存在する2件の脆弱性を連鎖させ、認証なしでSYSTEM権限のコード実行を実現した。 攻撃者はTrueConfサーバー上のlocale.phpをWebシェルへ置換し、データベースへのアクセスや継続的な遠隔操作を可能にした。 正規のTrueConf ClientインストーラーをPhantomCore入りの未署名版へ差し替え、接続した組織内ユーザーへ更新として配布した。 別のPhantomGraphバックドアはMicrosoft OneDriveをC2として命令を取得し、LSASSメモリダンプや偵察、リバースSSHトンネルを実行した。 Head Mareはロシアの計測機器、電子、運輸、エネルギー、IT、ソフトウェア開発分野を標的に複数の活動中キャンペーンを展開している。 | 高 | `source--daily-fff05927bf91551e1b96` |
| ロシア・ベラルーシ企業を標的とするHead Mareのフィッシングとランサムウェア展開 | hacktivism-ransomware | 2023 | 不明 | 2024-09-02 | target--head-mare--country--russia | malware--phantomdl, malware--phantomcore, malware--lockbit, malware--babuk | ttp--activity-rule--3ea0a3504b02e6bc8bbe, ttp--activity-rule--b0ab12e48afcc3ea04d5, ttp--activity-rule--e731ad0e92c25775432b, ttp--head-mare-t1203-winrar, ttp--head-mare-t1486-ransomware | victim--activity-rule--4a3bbced4c7828f97e61, victim--head-mare-russia-belarus-2024 | Kasperskyは、2023年に出現したハクティビスト集団Head Mareが、ロシアとベラルーシの組織へ最大限の被害を与えることを目的に活動していると報告した。侵入はフィッシングメールに添付したRARアーカイブでCVE-2023-38831(WinRAR)を悪用し、独自マルウェアPhantomDLとPhantomCoreを配布する。侵害後はSliver、Mimikatz、ngrok、rsockstunを併用し、Windows環境ではLockBit、Linux/ESXi環境ではBabukのランサムウェアを展開する。資料には身代金要求の記載もあるが、Kasperskyは主たる目的を金銭ではなく被害の最大化と評価している。 | 高 | `source--kaspersky-head-mare-2024` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| ハッカーがTrueConfを侵害し、クライアントインストーラーをバックドア入りに改ざん | Head Mare | PhantomCore, PhantomGraph | T1505.003 Web Shell, T1003.001 LSASS Memory, T1102 Web Service, T1190 Exploit Public-Facing Application, T1195.002 Compromise Software Supply Chain, T1505.003 Web Shell, T1572 Protocol Tunneling | 情報なし | ロシア, エネルギー, 計測機器, ソフトウェア開発 | 被害事例: ハッカーがTrueConfを侵害し、クライアントインストーラーをバックドア入りに改ざん, TrueConf Serverを運用するロシア組織(集約) | 高 |
| ロシア・ベラルーシ企業を標的とするHead Mareのフィッシングとランサムウェア展開 | Head Mare | Babuk, LockBit, PhantomCore, PhantomDL | T1003 OS Credential Dumping, T1560.001 Archive via Utility, T1566.001 Spearphishing Attachment, T1203 Exploitation for Client Execution, T1486 Data Encrypted for Impact | 情報なし | ロシア | 被害事例: ロシア・ベラルーシ企業を標的とするHead Mareのフィッシングとランサムウェア展開, ロシア・ベラルーシの複数分野組織(集約) | 高 |

2023年にX(旧Twitter)上で存在が確認され、2024年9月にKasperskyがフィッシングとCVE-2023-38831悪用、LockBit/Babuk展開を含む一連の活動を報告した。2026年8月にはTrueConf Serverの脆弱性連鎖とPhantomGraphの導入が報告された。

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | ベラルーシ | 2024年のKaspersky資料が標的国として明示している。 | 2023 | 不明 | 高 | `source--kaspersky-head-mare-2024` |
| countries | ロシア | 一次資料が標的国として明示している。 | 2023 | 2026-07 | 高 | `source--daily-fff05927bf91551e1b96`, `source--kaspersky-head-mare-2024`, `source--kaspersky-head-mare-trueconf-2026` |
| regions | 東欧 | ベラルーシ、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-fff05927bf91551e1b96`, `source--kaspersky-head-mare-2024`, `source--kaspersky-head-mare-trueconf-2026` |
| sectors | 電子 | 2026年資料が標的分野として明示。 | 不明 | 不明 | 高 | `source--kaspersky-head-mare-trueconf-2026` |
| sectors | エネルギー | 2024年・2026年資料が標的分野として明示。 | 不明 | 不明 | 高 | `source--kaspersky-head-mare-2024`, `source--kaspersky-head-mare-trueconf-2026` |
| sectors | エンターテインメント | 2024年資料が標的分野として明示。 | 不明 | 不明 | 高 | `source--kaspersky-head-mare-2024` |
| sectors | 政府機関 | 2024年資料が標的分野として明示。 | 不明 | 不明 | 高 | `source--kaspersky-head-mare-2024` |
| sectors | 計測機器 | 2026年資料が標的分野として明示。 | 不明 | 不明 | 高 | `source--kaspersky-head-mare-trueconf-2026` |
| sectors | IT | 2026年資料が標的分野として明示。 | 不明 | 不明 | 高 | `source--kaspersky-head-mare-trueconf-2026` |
| sectors | 製造 | 2024年資料が標的分野として明示。 | 不明 | 不明 | 高 | `source--kaspersky-head-mare-2024` |
| sectors | ソフトウェア開発 | 2026年資料が標的分野として明示。 | 不明 | 不明 | 高 | `source--kaspersky-head-mare-trueconf-2026` |
| sectors | 運輸 | 2024年・2026年資料が標的分野として明示。 | 不明 | 不明 | 高 | `source--kaspersky-head-mare-2024`, `source--kaspersky-head-mare-trueconf-2026` |

選定ロジック: ロシアとベラルーシに所在する組織を地理条件で選定し、分野は広く取る。2026年は未更新のTrueConf Serverという共通基盤の露出を選定条件としている。 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: ハッカーがTrueConfを侵害し、クライアントインストーラーをバックドア入りに改ざん | 非公開 | aggregate | multiple-organizations | reported | target--head-mare--country--russia, target--head-mare--sector--energy, target--head-mare--sector--instrumentation, target--head-mare--sector--software-development | malware--phantomcore, malware--phantomgraph | ttp--activity-rule--209e363ca5019e2456f9, ttp--head-mare-t1003-001-lsass, ttp--head-mare-t1102-onedrive, ttp--head-mare-t1190-trueconf, ttp--head-mare-t1195-002-installer, ttp--head-mare-t1505-003-webshell, ttp--head-mare-t1572-ssh | サーバー |  | 2026-07 | 不明 | 2026-08-10 | 高 | `source--daily-fff05927bf91551e1b96` |
| 被害事例: ロシア・ベラルーシ企業を標的とするHead Mareのフィッシングとランサムウェア展開 | 非公開 | aggregate | multiple-organizations | reported | target--head-mare--country--russia | malware--babuk, malware--lockbit, malware--phantomcore, malware--phantomdl | ttp--activity-rule--3ea0a3504b02e6bc8bbe, ttp--activity-rule--b0ab12e48afcc3ea04d5, ttp--activity-rule--e731ad0e92c25775432b, ttp--head-mare-t1203-winrar, ttp--head-mare-t1486-ransomware | メール／メールアカウント | encryption: ロシア・ベラルーシ企業を標的とするHead Mareのフィッシングとランサムウェア展開 | 2023 | 不明 | 2024-09-02 | 高 | `source--kaspersky-head-mare-2024` |
| ロシア・ベラルーシの複数分野組織(集約) | 非公開 | aggregate | multiple-organizations | reported |  | malware--phantomdl, malware--phantomcore, malware--lockbit, malware--babuk | ttp--head-mare-t1203-winrar, ttp--head-mare-t1486-ransomware | Windows端末, Linux/ESXiホスト | encryption: LockBitおよびBabukによるファイル暗号化。<br>disruption: 被害最大化を目的とした業務妨害。 | 2023 | 不明 | 2024-09-02 | 高 | `source--kaspersky-head-mare-2024` |
| TrueConf Serverを運用するロシア組織(集約) | 非公開 | aggregate | multiple-organizations | reported |  | malware--phantomcore, malware--phantomgraph | ttp--head-mare-t1190-trueconf, ttp--head-mare-t1195-002-installer, ttp--head-mare-t1003-001-lsass | TrueConf Server, TrueConf Client利用端末 | supply-chain: 正規クライアントインストーラーがバックドア入り未署名版へ差し替えられた。<br>credential-theft: PhantomGraphによるLSASSメモリダンプ。<br>data-theft: Webシェル経由のデータベースアクセスと遠隔操作。 | 2026-07 | 不明 | 2026-08-07 | 高 | `source--kaspersky-head-mare-trueconf-2026` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Persistence | T1505.003 | Web Shell | 攻撃者はTrueConfサーバー上のlocale.phpをWebシェルへ置換し、データベースへのアクセスや継続的な遠隔操作を可能にした。 |  | activity--daily-183fbfb9487ebc5f1327 | 2026-07 | 不明 | 中 | `source--daily-fff05927bf91551e1b96` |
| Credential Access | T1003 | OS Credential Dumping | 侵害後はSliver、Mimikatz、ngrok、rsockstunを併用し、Windows環境ではLockBit、Linux/ESXi環境ではBabukのランサムウェアを展開する。 | malware--babuk, malware--lockbit | activity--head-mare-russia-belarus-2024 | 2023 | 不明 | 中 | `source--kaspersky-head-mare-2024` |
| Collection | T1560.001 | Archive via Utility | 侵入はフィッシングメールに添付したRARアーカイブでCVE-2023-38831(WinRAR)を悪用し、独自マルウェアPhantomDLとPhantomCoreを配布する。 | malware--phantomcore, malware--phantomdl | activity--head-mare-russia-belarus-2024 | 2023 | 不明 | 中 | `source--kaspersky-head-mare-2024` |
| Initial Access | T1566.001 | Spearphishing Attachment | 侵入はフィッシングメールに添付したRARアーカイブでCVE-2023-38831(WinRAR)を悪用し、独自マルウェアPhantomDLとPhantomCoreを配布する。 | malware--phantomcore, malware--phantomdl | activity--head-mare-russia-belarus-2024 | 2023 | 不明 | 中 | `source--kaspersky-head-mare-2024` |
| Credential Access | T1003.001 | LSASS Memory | PhantomGraphがLSASSプロセスのメモリダンプを取得する。 | malware--phantomgraph | activity--daily-183fbfb9487ebc5f1327 | 2026-07 | 不明 | 高 | `source--kaspersky-head-mare-trueconf-2026` |
| Command and Control | T1102 | Web Service | PhantomGraphがMicrosoft OneDriveをC2として利用し、命令の取得と結果の返送を行う。 | malware--phantomgraph | activity--daily-183fbfb9487ebc5f1327 | 2026-07 | 不明 | 高 | `source--kaspersky-head-mare-trueconf-2026` |
| Initial Access | T1190 | Exploit Public-Facing Application | 未更新のTrueConf Serverの脆弱性2件(KLCERT-26-057、KLCERT-26-058)を連鎖させ、認証なしでSYSTEM権限のコード実行を得る。 |  | activity--daily-183fbfb9487ebc5f1327 | 2026-07 | 不明 | 高 | `source--kaspersky-head-mare-trueconf-2026` |
| Initial Access | T1195.002 | Compromise Software Supply Chain | 正規のTrueConf ClientインストーラーをPhantomCore入りの未署名版へ差し替え、サーバーへ接続した組織内ユーザーへ更新として配布する。 | malware--phantomcore | activity--daily-183fbfb9487ebc5f1327 | 2026-07 | 不明 | 高 | `source--kaspersky-head-mare-trueconf-2026` |
| Execution | T1203 | Exploitation for Client Execution | フィッシングメールに添付したRARアーカイブでCVE-2023-38831(WinRAR)を悪用し、PhantomDL/PhantomCoreを実行させる。 | malware--phantomdl, malware--phantomcore | activity--head-mare-russia-belarus-2024 | 2023 | 不明 | 高 | `source--kaspersky-head-mare-2024` |
| Impact | T1486 | Data Encrypted for Impact | Windows環境にLockBit、Linux/ESXi環境にBabukを展開してファイルを暗号化する。 | malware--lockbit, malware--babuk | activity--head-mare-russia-belarus-2024 | 2023 | 不明 | 高 | `source--kaspersky-head-mare-2024` |
| Persistence | T1505.003 | Web Shell | TrueConf Server上のlocale.phpをWebシェルへ置換し、データベースアクセスと継続的な遠隔操作を維持する。 |  | activity--daily-183fbfb9487ebc5f1327 | 2026-07 | 不明 | 高 | `source--kaspersky-head-mare-trueconf-2026` |
| Command and Control | T1572 | Protocol Tunneling | PhantomGraphがリバースSSHトンネルを確立し、侵害環境への継続的な到達性を確保する。 | malware--phantomgraph | activity--daily-183fbfb9487ebc5f1327 | 2026-07 | 不明 | 高 | `source--kaspersky-head-mare-trueconf-2026` |

## IOC／artifact概要

- IOC値: 35件
- IOC観測: 35件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| Head Mareはロシア・ベラルーシ組織を標的とするハクティビスト集団であり、2023年から2026年まで継続的に活動している。 | 高 | `source--kaspersky-head-mare-2024`, `source--kaspersky-head-mare-trueconf-2026` |  |
| 2026年の活動は、侵害した社内TrueConf Serverの正規配布物を差し替える組織内サプライチェーン型の配布へ発展している。 | 高 | `source--kaspersky-head-mare-trueconf-2026` |  |
| PhantomCoreはHead Mare固有の実装として2023年から2026年まで継続利用されており、クラスタ同定の指標になり得る。 | 中 | `source--kaspersky-head-mare-2024`, `source--kaspersky-head-mare-trueconf-2026` | 同名の別実装が存在しないことは確認できていない。 |

### 情報ギャップ

- 2024年資料と2026年資料の間(2025年)の活動を裏付ける一次資料を未取得。
- 個別の被害組織名が公開されておらず、被害規模を定量化できない。
- KLCERT-26-057/058に対応するCVE番号を確認できていない。
- Kasperskyが2026年5月に報じたとされるBO Teamとの連携について、一次資料を未確認のため関係を登録していない。

### 不確実性

- 露語のDFIR年次レポート(summary/2026/DFIR_otchet_za_polnyy_2025_final.pdf)に「Fairy Trickster (Head Mare)」の併記があるが、発行者と対応スコープを原典で確認できていないためaliasとして登録していない。
- PhantomDLとPhantomCoreの前後関係について、資料により記述が異なる可能性がある。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--daily-fff05927bf91551e1b96 | ハッカーがTrueConfを侵害し、クライアントインストーラーをバックドア入りに改ざん | securelist.ru | 2026-08-10 | https://securelist.ru/tr/head-mare-targets-trueconf-server-with-phantomcore/116557/ | osint-report | TLP:CLEAR | 中 |
| source--kaspersky-head-mare-2024 | Head Mare: adventures of a unicorn in Russia and Belarus | Kaspersky (Securelist) | 2024-09-02 | https://securelist.com/head-mare-hacktivists/113555/ | vendor-research-report | TLP:CLEAR | 高 |
| source--kaspersky-head-mare-trueconf-2026 | APT-группировка Head Mare использует уязвимости в необновленном сервере TrueConf для доставки вредоносного ПО PhantomCore и PhantomGraph участникам ВКС | Kaspersky (Securelist RU) | 2026-08-07 | https://securelist.ru/tr/head-mare-targets-trueconf-server-with-phantomcore/116557/ | vendor-research-report | TLP:CLEAR | 高 |

## 自由記述

本プロファイルは2026-08-10の日次更新チェックで未一致名として検知され、独立した一次資料の確認後に昇格した。status: draftから開始する。
