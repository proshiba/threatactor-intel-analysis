# Kimsuky 脅威アクタープロファイル

- プロファイルID: `actor--kimsuky`
- 状態: review
- 更新日時: 2026-07-30T12:43:04Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Kimsukyは北朝鮮RGB傘下と評価される国家支援型サイバー諜報アクターである。政策専門家、政府、外交、軍・防衛、研究、メディアを対象に、調査とペルソナ構築を伴う信頼醸成型スピアフィッシングを行い、認証情報、メール、非公開資料を窃取する。

## アクター名とAlias

- 正規名: **Kimsuky**
- 初回観測: 2012
- 最終観測: 2025
- 活動状態: yes

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Emerald Sleet | Microsoft | overlapping | 高 | `source--dmarc-2024`, `source--microsoft-actor-list` | 政府共同勧告は同一活動集合として扱うが、ベンダーの収集スコープ差を考慮する。 |
| Thallium | Microsoft (legacy) | overlapping | 高 | `source--joint-csa-2023`, `source--microsoft-actor-list` |  |
| Velvet Chollima | CrowdStrike | overlapping | 高 | `source--joint-csa-2023` |  |
| Black Banshee | PwC | overlapping | 高 | `source--joint-csa-2023` |  |
| APT43 | Mandiant | broader | 中 | `source--joint-csa-2023`, `source--dmarc-2024` | APT43にはKimsukyより広い活動スコープが含まれる可能性がある。 |
| TA427 | Proofpoint | overlapping | 中 | `source--rapid7-2024` |  |
| Sparkling Pisces | Palo Alto Networks | overlapping | 中 | `source--qax-2024` |  |

## 帰属

北朝鮮の偵察総局（RGB）に従属し、2024年共同勧告は第63研究センターへの行政的従属を記載する。

- 国: North Korea
- スポンサー種別: state
- 確度: 高
- 証拠: `source--joint-csa-2023`, `source--dmarc-2024`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| strategic-espionage | 北朝鮮の政策・外交・軍事・核開発上の意思決定に役立つ情報を収集する。 | 高 | `source--joint-csa-2023`, `source--dmarc-2024` |  |
| credential-and-mailbox-access | 認証情報とメールボックスを窃取し、信頼関係と連絡網を次の標的への足掛かりにする。 | 高 | `source--joint-csa-2023`, `source--rapid7-2024` |  |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| APT37 | overlaps-with | 標的、誘引テーマ、ツール、インフラに重複が報告されるが、別アクターとして扱う。 | 中 | `source--darkhorse-2023`, `source--qax-2024` |
| Lazarus Group | shares-tools-with | PEBBLEDASH等の再利用はDPRK内部のツール共有または開発者再配置の可能性を示す。 | 中 | `source--blurred-attribution`, `source--qax-2024` |
| APT43 | overlaps-with | 共有alias: Kimsuky | 低 | `source--joint-csa-2023` |
| APT43 | overlaps-with | MITRE treats APT43 as an associated Kimsuky group name, while Mandiant defines APT43 using its own collection scope. The overlap is well supported, but exact one-to-one identity is not. | 高 | `source--mitre-live-kimsuky-2026`, `source--mandiant-apt43-2023` |
| Lazarus Group | overlaps-with | DPRK threat actor cluster boundaries overlap in open source reporting, with some security researchers consolidating all attributed North Korean state-sponsored cyber activity under [Lazarus Group](https://attack.mitre.org/groups/G0032), rather than tracking operationally distinct subgroups. | 高 | `source--mitre-live-kimsuky-2026` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | 北朝鮮RGB傘下。対象調査と信頼醸成型ソーシャルエンジニアリングを大規模に運用する。 |
| Capability | フィッシングキット、悪性文書、LNK/CHM/MSC、PowerShell/VBScript/JScript、独自・公開RAT、Androidマルウェア。 |
| Infrastructure | 類似ドメイン、無料メール、VPS、侵害Webサーバ、クラウドストレージ、GitHub、メールC2。 |
| Victim | 政府、外交、軍・防衛、シンクタンク、大学、研究者、メディア、原子力・航空宇宙・金融等。 |
| Socio-political | 核・ミサイル、米韓関係、対中・対露関係、制裁など時事性の高い話題を誘引に使う。 |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Kimsuky, Velvet Chollima | canonical-name | 高 | North Korea | https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/<br>https://securityintelligence.com/media/recent-activity-from-itg16-a-north-korean-threat-group/<br>https://us-cert.cisa.gov/ncas/alerts/aa20-301a |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Emerald Sleet | canonical-name | 高 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| microsoft-threat-actor-mapping | Opal Sleet | multiple-name-intersection | 高 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| microsoft-threat-actor-mapping | Ruby Sleet | single-alias-intersection | 中 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Kimsuky | canonical-name | 高 | KP, Korea (Democratic People's Republic of) | https://securelist.com/the-kimsuky-operation-a-north-korean-apt/57915/<br>https://www.cfr.org/interactive/cyber-operations/kimsuky<br>https://www.pwc.co.uk/issues/cyber-security-data-privacy/research/tracking-kimsuky-north-korea-based-cyber-espionage-group-part-2.html |
| misp-threat-actor | APT43 | single-alias-intersection | 中 |  | https://www.mandiant.com/resources/blog/apt43-north-korea-cybercrime-espionage<br>https://mandiant.widen.net/s/zvmfw5fnjs/apt43-report |
| misp-microsoft-activity-group | Emerald Sleet | canonical-name | 高 | KP, North Korea | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Opal Sleet | multiple-name-intersection | 高 | KP, North Korea | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Ruby Sleet | single-alias-intersection | 中 | KP, North Korea | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Kimsuky - G0094 | mitre-external-id | 高 |  | https://asert.arbornetworks.com/stolen-pencil-campaign-targets-academia/<br>https://attack.mitre.org/groups/G0094<br>https://blog.alyac.co.kr/2234 |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Opal Sleet | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Ruby Sleet | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--alphaseed | AlphaSeed | Go製。NaverメールとChrome DevTools ProtocolをC2に利用するAppleSeed系能力。 | 2023-06 | 2024 | 高 | `source--rapid7-2024` |
| malware--appleseed | AppleSeed | コマンド実行、収集、キー入力・画面取得、ファイル転送を行う独自バックドア。 | 2019-05-06 | 2024 | 高 | `source--operation-newton`, `source--rapid7-2024` |
| malware--babyshark | BabyShark | VBScriptを中心とする初期活動・情報収集マルウェア。 | 2018 | 2024 | 高 | `source--joint-csa-2023`, `source--rapid7-2024` |
| malware--daily-1432659072aa52651920 | HttpSpy | Kimsukyとの直接的な利用関係が一次資料レビューで確認されたマルウェア。 | 不明 | 2026-04 | 中 | `source--daily-f05f4888998c8f53f5ca` |
| malware--daily-36c21f1c91a9419fec3b | PrxClient | Kimsukyとの直接的な利用関係が一次資料レビューで確認されたマルウェア。 | 不明 | 不明 | 高 | `source--daily-6f6e88199bc7e8479193` |
| malware--fastviewer | FastViewer Android Malware | Google Play同期・開発者機能の悪用で配布されたAndroidマルウェア群。 | 2022 | 不明 | 高 | `source--browser-advisory-2023` |
| malware--kgh | KGH Spyware | ブラウザ、メールクライアント、資格情報等を収集し、FTP C2と遠隔コマンドを利用する。 | 2020 | 不明 | 高 | `source--kgh-2021` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--mail-sending-program | Mail Sending Program ver10.0 | フィッシングメールの作成・送信を大規模化する運用ツール。 | 2022-08-17 | 2024 | 高 | `source--joint-csa-2023`, `source--rapid7-2024` |
| tool--remote-admin | Remote Administration Tool Set | 侵害端末への継続アクセスと手動操作に使う正規・公開ツール群。 | 2021 | 2024 | 高 | `source--covert-stalker`, `source--qax-2024` |

### インフラ

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| infra--lookalike-domains | Lookalike Phishing Domains | ポータル、報道機関、大学、信頼サービスに似せたドメイン。 | 2012 | 2025 | 高 | `source--joint-csa-2023`, `source--dmarc-2024`, `source--rapid7-2024` |
| infra--compromised-web-servers | Compromised Web Servers | フィッシング、ペイロード、Webシェル、C2に利用する侵害済みサーバ。 | 2019 | 2024 | 高 | `source--smoke-screen`, `source--operation-newton`, `source--covert-stalker` |
| infra--cloud-code-hosting | Cloud and Code Hosting Services | 正規サービスの評判を利用した配布・C2・ステージング。 | 2020 | 2025 | 高 | `source--joint-csa-2023`, `source--rapid7-2024` |
| infra--qr-credential-phishing | QR-code Credential Phishing Infrastructure | QR codes direct targets through landing pages to actor-controlled credential harvesting pages impersonating services such as Google login. | 2025-05 | 2025-06 | 高 | `source--fbi-kimsuky-quishing-2026` |

### 配送・ファイル形式

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| delivery--documents-shortcuts-help-console | HWP/Office/LNK/CHM/MSC | 悪性文書、ショートカット、HTML Help、管理コンソールによる配送と実行。 | 2012 | 2025 | 高 | `source--rapid7-2024`, `source--darkhorse-2023` |

### 脆弱性

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| vulnerability--cve-2019-0708 | CVE-2019-0708 | Operation Covert StalkerでRDP脆弱システムの侵害・踏み台化に使用したと報告。 | 2022 | 2023-09 | 高 | `source--covert-stalker` |

### 運用能力

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| opcap--trust-building-phishing | Trust-building Spearphishing | 複数回の無害な連絡で信頼を築き、後続で悪性リンクや文書を送る。 | 2012 | 2025 | 高 | `source--joint-csa-2023`, `source--dmarc-2024` |

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 北朝鮮マルウェアのモジュール化：多様性と機能特化 | cyber-espionage | 不明 | 不明 | 2026-04-06 | target--activity-rule--sector--63c9fa67327d005b07b7, target--activity-rule--sector--932f4928d5e1ec28e2df, target--mitre-group--sector--85e4128fa590941f9478 |  | ttp--activity-rule--139ca10483e8bad29269 | victim--activity-rule--c806e08389faabc69c62 | 本記事は、北朝鮮のサイバー活動を単一集団ではなく、任務別に分業された統制下のマルウェア生態系として分析している。 こうした分業化は、国際制裁、法執行の強化、マルウェア公開分析の蓄積で個別ツールの寿命が短くなったことへの合理的な適応だと位置付けている。 北朝鮮のモデルが他の国家主導のAPT（ロシア、中国、イランなど）と決定的に異なる点は、マルウェアを貴重な資産ではなく消耗品として扱っていること。 諜報系は Kimsuky を代表例とし、PowerShell や VBS、ソーシャルエンジニアリング、クラウド悪用、長期潜伏による静かな情報収集を重視すると説明する。 金銭獲得系は Lazarus を中心に、暗号資産事業者や開発者基盤を狙い、ウォレット窃取やサプライチェーン侵害で素早い収益化を図るとされる。 破壊・威圧系は Andariel に結び付けられ、ワイパーや急速な横展開で短時間に目立つ被害を与え、政治的メッセージを伴うと述べる。 | 中 | `source--daily-ec97ed0896afb842c91e` |
| DPRK作戦の内情：LazarusとKimsukyの新インフラを世界的キャンペーンから特定 | infrastructure-operation | 不明 | 不明 | 2025-12-18 |  |  |  |  | Hunt.ioとAcronisの共同調査で、Lazarus/Kimsukyの未公開インフラ群（C2・FRP・証明書等）の連関を発見。 オープンディレクトリに資格窃取ツールやQuasar/BADCALLを配置する恒常的手口が複数ノードで確認。 FRPは同一10MBバイナリがTCP/9999で8ホストに展開され、再利用可能な痕跡として有効と指摘。 証明書の再利用により12IPが同一クラスタに紐づき、Bluenoroffとの重なりも一部で示唆。 記事末にIOC一覧を提示し、防御側は露出ディレクトリ・FRP・証明書パターンの継続監視を推奨。 | 高 | `source--daily-f27405f22a33397d0072` |
| 北朝鮮のハッカーがVPN更新の脆弱性を悪用してマルウェアをインストール | malware-campaign | 不明 | 不明 | 2024-08-06 | target--mitre-group--sector--85e4128fa590941f9478, target--south-korea |  | ttp--activity-rule--866c7fa9fa78e9f314c7 | victim--activity-rule--e2b0c84831cb7f6ab33f | 北朝鮮のハッカーグループがVPNのアップデートの脆弱性を悪用し、マルウェアをインストール。 攻撃者はKimsukyとAndariel（APT43とAPT45）で、韓国の産業機密を狙う。 VPNソフトウェアの通信プロトコルの脆弱性を悪用し、更新プログラムを置き換えてトロイの木馬化。遠隔操作用のDoraRATをインストール。 攻撃は産業機器や設計文書の盗難を目的としている。 NCSCが警告を発表し、セキュリティ対策を推奨。 | 中 | `source--daily-444c87a0051642065f55` |
| Kimsukyグループによる外交関係者を装った攻撃事例（PebbleDash、PrxClient） | phishing-campaign | 不明 | 不明 | 2026-07-30 |  | malware--daily-36c21f1c91a9419fec3b |  |  | Kimsukyは外交関係者を装ったスピアフィッシングで悪性LNKを配布し、PebbleDashやPrxClientなど複数のツールを導入している。 LNKはPowerShell、JavaScript、HTAを実行し、追加ペイロードの取得、端末情報の収集、ファイルの窃取を行う。 PebbleDashはコマンド実行、ファイル操作、プロセス制御、システム情報収集などを備え、LSASSへ注入される亜種も確認された。 攻撃者はRDP Wrapper、バックドアアカウント、RDP Patcherを使い、感染端末への継続的な遠隔アクセスを確保していた。 | 高 | `source--daily-6f6e88199bc7e8479193` |
| 北朝鮮のAPT「Kimsuky」、LNKファイルを使用してブラウザに保存された認証情報を窃取するforceCopyマルウェアを配布 | phishing-campaign | 不明 | 不明 | 2025-02-07 |  |  | ttp--activity-rule--9f5f511f9650ee41dace, ttp--activity-rule--e0f37374ccce7abb7368, ttp--activity-rule--f0e72b5798f70a2f9617 | victim--activity-rule--f0068fe489ba8681b2a9 | 北朝鮮のハッカー集団「Kimsuky」が、スピアフィッシング攻撃で情報窃取型マルウェア「forceCopy」を配布。 攻撃は、Microsoft OfficeやPDF文書に偽装したLNKファイルを含むフィッシングメールから始まる。 LNKファイルを開くと、PowerShellやmshta.exeが実行され、外部から次のペイロードをダウンロード・実行。 最終的に、トロイの木馬「PEBBLEDASH」やカスタム版の「RDP Wrapper」などが展開される。 forceCopyは、ウェブブラウザの関連ディレクトリ内のファイルをコピーし、認証情報を窃取する。 | 高 | `source--daily-6f57fcf4dc3991af9b4e` |
| VS Codeエクステンションを悪用するKimsuky：ランサムウェアと永続化のためのキャンペーンとは？ | ransomware-extortion | 不明 | 不明 | 2025-11-19 |  |  | ttp--activity-rule--5bc4f7380e62aafda9c6, ttp--activity-rule--9d7fe74bcca8ad1357ae, ttp--activity-rule--acef6838bb761cf3129e | victim--activity-rule--80b91cae7f1445dd7f6d | 北朝鮮支援のKimsukyが開発者向けエクステンションを悪用し、JavaScript系マルウェアで永続的なC2を構築すると報告。 初期ドロッパー“Themes.js”はmedianewsonline[.]com上に置かれ、難読化薄めのコードで通信を開始する設計。 iuh234[.]medianewsonline[.]com/dwnkl.phpへGETでホスト名と認証キーを送信し、選別後に多段でペイロードを展開。 C:\Users配下の列挙やプロセス収集を実施し、結果をCAB化して同C2へPOSTで流出、CodePageをUTF-8に変更。 %APPDATA%配下に自身を保存しタスクでwscriptを毎分実行、空のWord文書配布も確認され二次感染に用いる可能性。 | 高 | `source--daily-28742c9ae0a7173b9225` |
| 日本、北朝鮮のKimsukyハッカーに関連する攻撃を警告 | phishing-campaign | 不明 | 不明 | 2024-07-11 | target--activity-rule--country--f35cd09db0a72555b38a, target--mitre-group--sector--4eba90b76b16e9d6d89b, target--mitre-group--sector--c5b1f7936acf85af11e4 |  | ttp--activity-rule--300616f23614b4974d79 | victim--activity-rule--2cd9ac0252a3c2e9acc2 | 日本政府は北朝鮮のKimsukyハッカーによるサイバー攻撃のリスクを警告 攻撃対象は政府機関、大学、研究機関 Kimsukyはフィッシング攻撃とマルウェア感染を使用 攻撃はフィッシングから始まり、悪意のある ZIP ファイルを添付したフィッシング メールを日本の標的に送信。ZIP には、マルウェア感染を引き起こす実行ファイルと2つのおとり文書ファイルが含まれる。 実行ファイルを実行すると、VBS ファイルをダウンロードして実行。さらに'C:\Users\Public\Pictures\desktop.ini.bak' が Wscript 経由で自動起動するように設定される。 | 高 | `source--daily-d930e3ca01c519bf5740` |
| 北朝鮮のハッカー、標的型マルウェアキャンペーンでFacebook Messengerを悪用 | malware-campaign | 不明 | 不明 | 2024-05-17 |  |  |  |  | Kimsukyグループが偽のFacebookアカウントを使用し、標的にマルウェアを配布。 攻撃はMessengerを通じて行われ、被害者にOneDrive上にホストされている悪意のある文書ファイルを開かせる。 ドキュメント: 日本、韓国、米国の 3 か国首脳会談に関連するエッセイやコンテンツを装った Microsoft Common Consoleドキュメント ファイル名は、「My_Essay(prof).msc」または「NZZ_Interview_Kohei Yamaha.msc」。後者は日本からアップロードされたもの。 MSCファイルを開き、Microsoft管理コンソール(MMC)で開くことを同意すると、攻撃が開始。 偽装のために「Essay on Resolution of Korean Forced Labor Claims.docx」という文書ファイルも開かれる。 | 中 | `source--daily-75d0d2c890d6c822d6f6` |
| 新たなDEEP#GOSUマルウェアキャンペーン、Windowsユーザーを高度な戦術で狙う | infrastructure-operation | 不明 | 不明 | 2024-03-19 |  |  | ttp--activity-rule--adfe10f37acf740aecd1, ttp--activity-rule--e74d04ae1a699f39b9d5 |  | PowerShellとVBScriptを使用しWindowsシステムを感染させ、情報を窃取 このキャンペーンは、北朝鮮のKimsukyと関連があるとSecuronixが指摘 DropboxやGoogle Docsを利用し、C2通信を隠蔽 開始点はPDFファイルに偽装した悪意あるメール添付ファイル TruRatを含む複数のステージを持つ高度なマルウェア | 中 | `source--daily-66a67b66f7f04fd72d52` |
| FBI、KimsukyがQRコードを使って米国組織をフィッシングしていると警告 | phishing-campaign | 不明 | 不明 | 2026-01-10 | target--activity-rule--country--6604ad21c713b8dfd8c7 |  | ttp--activity-rule--32b62558046788e695f4 | victim--activity-rule--cf9f7422af16e0e9dbab | FBIは北朝鮮系APT「Kimsuky（APT43）」が、悪性QRコード付きスピアフィッシング（Quishing）を米国組織へ行っていると警告。 対象は北朝鮮関連の政策・研究に関わるNGO、シンクタンク、学術機関、戦略アドバイザリ、政府組織などとされる。 QRをスマホで読ませてメール防御を迂回し、偽ログイン等へ誘導して資格情報やセッショントークン窃取→MFA回避に繋げる手口。 2025年5〜6月に、アンケート／セキュアドライブ／会議登録を装い、攻撃者管理インフラ経由で偽Microsoft 365等へ誘導した事例を提示。 対策として、QRコード教育、送信元検証、MDM導入、フィッシング耐性MFAの徹底、スキャン後の監視・通報を推奨。 | 高 | `source--daily-4c3098e731ae81f16008` |
| Kimsuky、BlueKeep RDP脆弱性を悪用し、韓国と日本のシステムを侵害 | phishing-campaign | 不明 | 不明 | 2025-04-22 | target--activity-rule--country--f35cd09db0a72555b38a, target--south-korea |  | ttp--activity-rule--8efb9226234d380e7b25 | victim--activity-rule--4327a3f821366839b177 | 北朝鮮支援のAPTグループ「Kimsuky」が、BlueKeep（CVE-2019-0708）を悪用し、韓国と日本の組織を標的にした攻撃を実施。 CVE-2019-0708は、認証されていない攻撃者が任意プログラムのインストールなどができる重大な脆弱性。この脆弱性は2019年5月にMicrosoftによって修正されている。 AhnLabはこの活動を「Larva-24005」と命名し、RDP脆弱性スキャナの存在を確認。 初期侵入手段として、BlueKeepの他にCVE-2017-11882を含むフィッシングメールも使用。 侵入後、MySpyマルウェアやRDPWrapを導入し、RDPアクセスを有効化。 最終的に、KimaLoggerやRandomQueryなどのキーロガーを展開し、情報収集を行う。 | 高 | `source--daily-00bf22365ce019ee25a6` |
| Kimsukyは寛容なDMARCポリシーを利用してメールを偽装 | phishing-campaign | 不明 | 不明 | 2024-04-17 | target--activity-rule--sector--5403aec9c83d6a925f61, target--mitre-group--sector--4eba90b76b16e9d6d89b, target--mitre-group--sector--c5b1f7936acf85af11e4 |  |  | victim--activity-rule--db5cce1fb86560a03996 | Kimsukyグループは、緩いDMARCポリシーを利用して別組織になりすましたメールを送信 DMARCプロトコルのオプションとして、認証に失敗したメールの送信をどのように取り扱うか決められる。Kimsukyは認証に失敗しても何しないとなっているドメインになりすます 攻撃は情報収集を目的としており、標的はシンクタンク、政府、ジャーナリスト 攻撃メールには、ターゲットによる電子メールの開封有無、いつ、どのデバイスで開いたかなどのデータを追跡するために、追跡ピクセルが埋め込まれている | 高 | `source--daily-8c76eeb938a1170375af` |
| Kimsukyの高度な攻撃手法：JSONPing、Webex偽装、新たなHttpSpy亜種 | infrastructure-operation | 不明 | 2026-04 | 2026-05-30 | target--south-korea | malware--daily-1432659072aa52651920 |  | victim--activity-rule--a937e2a007f4f2de0934 | ENKIは2026年4月までに、Kimsukyが韓国の軍・企業を狙いマルウェアを展開した複数事例を確認した。 攻撃では、韓国B2Bメッセージングサービスのセキュリティソフト導入ページやWebex会議ページを偽装した。 偽ページはJSONPで感染端末上のローカルサーバーへ問い合わせ、マルウェア実行有無を確認するJSONPingという新たな手法を使う。 Webex偽装事例では、実在の会議予定を悪用し、jseドロッパー経由で新たな3段階構成のHttpSpy亜種を導入した。これは事前に参加者のアカウントやデバイスを侵害し、スケジュールを入手していた可能性を示唆している。 インフラ、コード類似性、RC4鍵再利用、証明書など複数の指標から、これらの活動をKimsukyに関連付けている。 | 中 | `source--daily-f05f4888998c8f53f5ca` |
| 北朝鮮のハッキンググループが韓国の防衛請負業者を侵害 | malware-campaign | 不明 | 不明 | 2024-04-24 | target--activity-rule--sector--b94dc560a327b601965d, target--mitre-group--sector--85e4128fa590941f9478, target--south-korea |  |  | victim--activity-rule--34a81485acecf6617bee | 北朝鮮のハッキンググループが韓国の防衛産業を標的に 韓国警察の報告書では、Lazarus, Andariel, Kimsukyが関与している3つのインシデントを記載 ターゲットまたはその下請け組織のネットワークの脆弱性を利用しマルウェアを植え付ける インシデントの1つでは、データの抜き取りとクラウドサーバへの転送が行われた 韓国警察は、多要素認証の導入・外国からのIPアクセスのブロックなどのセキュリティ強化を勧めている | 中 | `source--daily-b9be11e58ab6c82617ab` |
| Pythonベースのバックドアを配布する悪性LNKファイルと配布手法の変化（Kimsukyグループ） | infrastructure-operation | 不明 | 不明 | 2026-04-04 |  |  | ttp--activity-rule--29d8235d14af386ac5ad, ttp--activity-rule--4397bb55001837fdcfcf, ttp--activity-rule--d7ba1acbdbcf8abfbb94, ttp--activity-rule--f3bf1175031240a606d3 |  | ASECは、Kimsukyが用いる悪性LNK配布手法の変化を確認し、最終的にPython製バックドアまたはダウンローダを実行する流れ自体は維持されていると説明した。 従来はLNK→PowerShell→BATの比較的単純な流れだったが、最近はLNK→PowerShell→デコイ/XML/PS1/VBS生成へ変化し、中間段階が多段化した。 新しい手口では隠し属性付きのC:\windirr配下に複数ファイルを生成し、Task Scheduler経由でVBS、PS1、BATを順に実行してZIPを取得・展開する。 pp.ps1はDropboxをC2伝達に使って端末情報を送信し、続くhh.batは分割ZIPからbeauty.pyを展開して別のスケジュールタスクでPythonバックドアを起動する。 バックドアは45[.]95[.]186[.]232:8080と通信し、コマンド実行、ドライブ照会、ファイル送受信・削除、EXE/BAT/VBS実行などを行える。 マルウェアは、HAPPYという文字列を送ってC2サーバに感染を通知している。 | 高 | `source--daily-d289a4c2f4400dbffb6f` |
| 北朝鮮関連のKimsuky、継続的なサイバー攻撃でコンパイル済みHTMLヘルプファイルに移行 | infrastructure-operation | 不明 | 不明 | 2024-03-25 | target--south-korea |  | ttp--activity-rule--aab21b466b971ffe5f9e | victim--activity-rule--e7e9ae319582ebd6f222 | Kimsuky、CHMファイルを利用し機密データを盗む新手法を使用 2012年から活動、主に韓国、北米、アジア、ヨーロッパを標的 攻撃ではISO、LNKファイル、Office文書も利用 CHMファイルはISO、VHD、ZIP、RAR内で配布、JavaScript実行 感染の流れは、CHM file > html file > vbs file(C2と接続) C2と接続後、収集したデータをDATファイルにして窃取 | 高 | `source--daily-0477636fe03aea54224d` |
| 北朝鮮系ハッカーが「ClickFix」を悪用し、暗号資産の偽求人でBeaverTailを配布 | campaign | 不明 | 不明 | 2025-09-22 |  |  | ttp--activity-rule--e28f89337bc79ca60896 |  | 北朝鮮関係者がClickFix誘導を用い、BeaverTailとInvisibleFerretを偽求人経由で配布する手口が確認された。 従来の開発者狙いから、暗号資産・小売のマーケ/トレーダー職志望者へ標的を拡大し、Vercel製偽採用サイトを配布基盤に利用。 OS別コマンド実行を促す偽マイク障害表示で、シェル/VBスクリプト経由の軽量版BeaverTailを展開するのが特徴。 2025年5月後半の波では、pkgやPyInstallerで作成したWindows/macOS/Linux向けバイナリ化版の投入が観測された。 この攻撃キャンペーンに時期を合わせ、北朝鮮と連携するKimsuky (別名 APT43)による2つの攻撃キャンペーンも観測されている。 | 中 | `source--daily-dddef70e68c0dc59a5d3` |
| 北朝鮮のハッカー、新しいKLogEXEとFPSpyマルウェアを標的型攻撃に使用 | phishing-campaign | 不明 | 不明 | 2024-09-27 |  |  | ttp--activity-rule--0abff0edccdadf8d2395, ttp--activity-rule--a75091343851bf6ac794 |  | 北朝鮮系ハッカー「Kimsuky」がKLogEXEとFPSpyという2つの新しいマルウェアを展開。 KLogEXEはキーロガーで、実行中のアプリケーションやキーストロークを収集。 FPSpyはシステム情報を収集し、任意のコマンドを実行できるバックドア型マルウェア。 スピアフィッシングで攻撃。信頼できる人物からのメールを装って、被害者を騙してマルウェアをダウンロードさせている。 主に韓国や日本がターゲット。 | 中 | `source--daily-5d4c990e46241ee39e8d` |
| Smoke Screen / Stealth Power | campaign | 2019-03 | 2019-05 | 2019-04-17 | target--government-diplomacy, target--south-korea |  | ttp--activity-rule--a2250f5bde5c4e0d27c0, ttp--t1059-001--powershell, ttp--t1566-001--documents | victim--activity-rule--c4bf5579c78fe551b1fe | DPRK関連のHWP/DOCフィッシング、HTA、PowerShellキーロガーを伴う活動。 | 高 | `source--smoke-screen` |
| Operation Newton | campaign | 2020 | 不明 | 2021-10 | target--research-academia | malware--appleseed | ttp--activity-rule--4c1985318db9368ef803, ttp--t1041--exfiltration-c2, ttp--t1056-003--web-portal, ttp--t1505-003--webshell, ttp--t1566-002--credential-links | victim--activity-rule--c1e4a930d9a5d2836a85 | 工学研究者への資格情報フィッシングからAppleSeed、Webシェル、サーバ横展開へ進む活動。 | 高 | `source--operation-newton` |
| Browser Extension and Google Play Abuse | campaign | 2022 | 不明 | 2023-03-20 | target--germany, target--research-academia | malware--fastviewer | ttp--t1114--email-collection, ttp--t1566-002--credential-links | victim--activity-rule--81ab232ac4d2bee5f37b | Chromium拡張でGmailを窃取し、Google Play同期機能でAndroidマルウェアを配布。 | 高 | `source--browser-advisory-2023` |
| Operation DarkHorse | campaign | 2022-02 | 不明 | 2023-10-16 | target--finance |  | ttp--t1059-001--powershell, ttp--t1566-001--documents | victim--activity-rule--190f76f226f2f78defa7 | VBSからJSEへ変化したCHM活動。暗号資産、金融、保険等の誘引を利用。 | 中 | `source--darkhorse-2023` |
| 北朝鮮のハッカー、新たなGolangマルウェア「Durian」を暗号通貨企業に対して使用 | malware-campaign | 2023-08 | 2023-11 | 2024-05-11 | target--south-korea |  |  | victim--activity-rule--b40066714da8e40790a5 | 北朝鮮のAPT「Kimsuky」、Golangベースの新マルウェア「Durian」を使用 韓国の暗号通貨企業2社が標的にされた マルウェアはバックドア機能を備え、ファイルを抽出 侵入手段は韓国固有の正規ソフトウェアを通じたものであるが、正確なメカニズムは明らかにされていない 攻撃は2023年8月と11月に発生 | 中 | `source--daily-a5ca98841868974d600b` |
| Kimsukyハッカー、韓国への攻撃に新しいLinuxバックドアを使用 | infrastructure-operation | 2024 | 2024 | 2024-05-17 | target--mitre-group--sector--4eba90b76b16e9d6d89b, target--south-korea |  | ttp--activity-rule--d97d1bd687c6c8f70793 | victim--activity-rule--643a32a3eac4d1304920 | 北朝鮮のKimsukyグループがGomirマルウェアを使用。 攻撃は2024年初めに始まり、韓国政府機関を標的。 GomirはGoBearのLinux版で、持続性とC2通信を持つ。 マルウェアはroot権限で動作し、/var/log/syslogdにコピーされる。 マルウェアは17の操作をサポートしており、HTTP POSTリクエストで実行。 操作の例: C&Cサーバーとの通信を一時停止、任意のシェルコマンドを実行、リモート接続用のリバース プロキシを開始、システムからファイルを取得、など | 高 | `source--daily-01bbfa4ce1d271e9e220` |
| Kimsuky、TRANSLATEXT Chrome拡張機能を使用して機密データを盗む | reported-activity | 2024-03 | 2024-03 | 2024-06-29 |  |  | ttp--activity-rule--5c91761bada372170084 |  | 北朝鮮のハッカーグループKimsukyがTRANSLATEXTという悪意のあるChrome拡張機能を使用。 拡張機能は、メールアドレス、ユーザー名、パスワード、クッキー、ブラウザのスクリーンショットを収集。 主なターゲットは韓国の学術機関で、北朝鮮の政治問題に焦点を当てた学術関係が特に狙われた。 Zscaler ThreatLabzが2024年3月に活動を観測。 拡張機能はGoogle Translateを装い、セキュリティを回避。 | 高 | `source--daily-303f2ea1899dc2bdab19` |
| 国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開 | phishing-campaign | 2025-01 | 2025-02 | 2025-04-18 | target--mitre-group--sector--c5b1f7936acf85af11e4 |  | ttp--activity-rule--1f8b1ff7e839aaca7ece | victim--activity-rule--78b3d620ec98d71ea8ad | 中国・イラン・ロシア・北朝鮮支援のAPTがClickFixを用いたフィッシング攻撃を展開。 TA427 (Kimsuky): 2025年1月と2月に、シンクタンク部門の少数組織の個人を標的としたフィッシングキャンペーンでClickFixを使用 TA450 (MuddyWater): イランに関連するこのグループは、持続的なアクセスを維持するために、Levelなどの正当なリモート監視および管理 (RMM) ソフトウェアを悪用するためにClickFixを利用 UNK_RemoteRogue: 2024年末に確認されたこのロシアの可能性のあるグループは、侵害された可能性のあるZimbraサーバーから送信された、Microsoft Officeドキュメントへのリンクを含むおとりメールを使用してClickFixを使用 PowerShellコマンドを利用しQuasar RATやRMMソフトを導入。 日本大使館を装った誘導や、YouTube動画を含む偽ページなどを利用。 | 中 | `source--daily-07ef6046e1668f840b3a` |
| 北朝鮮のハッカー、PowerShellの手法を悪用して新たなサイバー攻撃を実行 | phishing-campaign | 2025-01 | 不明 | 2025-02-13 | target--mitre-group--sector--4eba90b76b16e9d6d89b |  |  | victim--activity-rule--b327511a595ac3276ab1 | 北朝鮮のハッカーグループ「Kimsuky」が、PowerShellを管理者権限で実行させ、悪意のあるコードを実行させる新たな手法を使用しています。 攻撃者は、南韓政府関係者を装い、ターゲットと関係を構築した後、PDF添付のスピアフィッシングメールを送信します。 被害者は、Windowsシステムの登録手順を記載したURLをクリックするよう促され、PowerShellを管理者として実行し、提示されたコードをコピー&ペーストして実行するよう指示されます。 このコードは、リモートサーバーからブラウザベースのリモートデスクトップツールと証明書ファイルをダウンロードし、攻撃者がデバイスにアクセスし、データを抽出できるようにします。 この手法は、2025年1月以降、限定的な攻撃で観測されており、Kimsukyが使う従来の手法から逸脱しています。 | 中 | `source--daily-b859524205edbc7c576c` |
| Kimsuky QR-code Spearphishing Campaign | campaign | 2025-05 | 2025-06 | 2026-01-08 | target--journalists-policy-experts, target--research-academia |  | ttp--t1056-003--kimsuky-quishing-2025, ttp--t1098--kimsuky-quishing-2025, ttp--t1550-004--kimsuky-quishing-2025, ttp--t1566-002--kimsuky-quishing-2025 | victim--activity-rule--8a36dde11b25a11054ec | Kimsuky impersonated foreign advisers, embassy and think-tank personnel, and conference organizers. QR codes led think-tank and strategic-advisory targets to credential-harvesting infrastructure. | 高 | `source--fbi-kimsuky-quishing-2026` |
| Kimsuky、武器化QRコード経由で悪性モバイルアプリを配布し利用者を攻撃 | infrastructure-operation | 2025-09 | 2025-09 | 2025-12-18 |  |  |  |  | 北朝鮮関与のKimsukyが、宅配追跡を装う偽サイトと武器化QRコードでAndroid向けマルウェア「DOCSWAP」を配布。 2025年9月に観測。スミッシングで偽追跡サイトへ誘導し、QR読取や直接アクセスで「セキュリティアプリ」偽装APKを落とさせる。 配布C2は27.102.137.181。SecDelivery.apk内のsecurity.datをlibnative-lib.soで復号し、多権限取得と常駐を確立。 RATは57コマンドを実装し、録音・録画、位置・通話・連絡先・SMS収集、遠隔操作、アクセシビリティ経由のキー入力記録を実施。 インフラやHTMLの韓国語コメント、「Million OK !!!!」が過去作戦と一致し、Kimsuky関与の根拠となった。 | 高 | `source--daily-f7383fd875d71ae63151` |
| 2026年第1四半期 DPRK Operation Kimsuky 分析 | phishing-campaign | 2026-01 | 2026-06 | 2026-05-20 | target--activity-rule--sector--63c9fa67327d005b07b7, target--activity-rule--sector--932f4928d5e1ec28e2df, target--activity-rule--sector--b94dc560a327b601965d, target--mitre-group--sector--c5b1f7936acf85af11e4 |  | ttp--activity-rule--4e7a9106baf629cb2a5d, ttp--activity-rule--e326bf94ac733031173e | victim--activity-rule--3df32433e6e912714b2a | Logpressoは、2026年上半期にKimsukyが実行した4件のスピアフィッシングキャンペーンを分析した。 標的は採用担当者、暗号資産関係者、開発者、国防関係者、公的機関や大学院委託教育関係者など。 各攻撃は、偽装文書表示、ペイロード投下、永続化、C2通信や遠隔操作という共通の流れを持つ。 GitHub raw/API、Microsoft CDN、VSCodeトンネルなどの正規サービス悪用が目立ち、評判ベースの遮断回避が意図されている。 LNK/JSEによる初期実行、LotL、難読化、タスクスケジューラ永続化、uid/IP/MACによる被害者識別が共通TTPとして整理されている。 | 中 | `source--daily-f3e6fda98089cb5da96d` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| 北朝鮮マルウェアのモジュール化：多様性と機能特化 | Kimsuky | 情報なし | T1059.001 PowerShell | 情報なし | 暗号資産・Web3, IT・ソフトウェア, 製造・産業 | 被害事例: 北朝鮮マルウェアのモジュール化：多様性と機能特化 | 中 |
| DPRK作戦の内情：LazarusとKimsukyの新インフラを世界的キャンペーンから特定 | Kimsuky | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 高 |
| 北朝鮮のハッカーがVPN更新の脆弱性を悪用してマルウェアをインストール | Kimsuky | 情報なし | T1190 Exploit Public-Facing Application | 情報なし | 製造・産業, 韓国 | 被害事例: 北朝鮮のハッカーがVPN更新の脆弱性を悪用してマルウェアをインストール | 中 |
| Kimsukyグループによる外交関係者を装った攻撃事例（PebbleDash、PrxClient） | Kimsuky | PrxClient | 情報なし | 情報なし | 情報なし | 情報なし | 高 |
| 北朝鮮のAPT「Kimsuky」、LNKファイルを使用してブラウザに保存された認証情報を窃取するforceCopyマルウェアを配布 | Kimsuky | 情報なし | T1555.003 Credentials from Web Browsers, T1036 Masquerading, T1105 Ingress Tool Transfer | 情報なし | 情報なし | 被害事例: 北朝鮮のAPT「Kimsuky」、LNKファイルを使用してブラウザに保存された認証情報を窃取するforceCopyマルウェアを配布 | 高 |
| VS Codeエクステンションを悪用するKimsuky：ランサムウェアと永続化のためのキャンペーンとは？ | Kimsuky | 情報なし | T1027 Obfuscated Files or Information, T1057 Process Discovery, T1053.005 Scheduled Task | 情報なし | 情報なし | 被害事例: VS Codeエクステンションを悪用するKimsuky：ランサムウェアと永続化のためのキャンペーンとは？ | 高 |
| 日本、北朝鮮のKimsukyハッカーに関連する攻撃を警告 | Kimsuky | 情報なし | T1566.001 Spearphishing Attachment | 情報なし | 日本, 政府・行政, 教育・研究 | 被害事例: 日本、北朝鮮のKimsukyハッカーに関連する攻撃を警告 | 高 |
| 北朝鮮のハッカー、標的型マルウェアキャンペーンでFacebook Messengerを悪用 | Kimsuky | 情報なし | 情報なし | Cloud and Code Hosting Services | 情報なし | 情報なし | 中 |
| 新たなDEEP#GOSUマルウェアキャンペーン、Windowsユーザーを高度な戦術で狙う | Kimsuky | 情報なし | T1036 Masquerading, T1102.003 One-Way Communication | Cloud and Code Hosting Services | 情報なし | 情報なし | 中 |
| FBI、KimsukyがQRコードを使って米国組織をフィッシングしていると警告 | Kimsuky | 情報なし | T1566.002 Spearphishing Link | 情報なし | 米国 | 被害事例: FBI、KimsukyがQRコードを使って米国組織をフィッシングしていると警告 | 高 |
| Kimsuky、BlueKeep RDP脆弱性を悪用し、韓国と日本のシステムを侵害 | Kimsuky | 情報なし | T1056.001 Keylogging | 情報なし | 日本, 韓国 | 被害事例: Kimsuky、BlueKeep RDP脆弱性を悪用し、韓国と日本のシステムを侵害 | 高 |
| Kimsukyは寛容なDMARCポリシーを利用してメールを偽装 | Kimsuky | 情報なし | 情報なし | 情報なし | メディア・報道, 政府・行政, 教育・研究 | 被害事例: Kimsukyは寛容なDMARCポリシーを利用してメールを偽装 | 高 |
| Kimsukyの高度な攻撃手法：JSONPing、Webex偽装、新たなHttpSpy亜種 | Kimsuky | HttpSpy | 情報なし | 情報なし | 韓国 | 被害事例: Kimsukyの高度な攻撃手法：JSONPing、Webex偽装、新たなHttpSpy亜種 | 中 |
| 北朝鮮のハッキンググループが韓国の防衛請負業者を侵害 | Kimsuky | 情報なし | 情報なし | 情報なし | 防衛・軍事, 製造・産業, 韓国 | 被害事例: 北朝鮮のハッキンググループが韓国の防衛請負業者を侵害 | 中 |
| Pythonベースのバックドアを配布する悪性LNKファイルと配布手法の変化（Kimsukyグループ） | Kimsuky | 情報なし | T1053.005 Scheduled Task, T1059.006 Python, T1102.003 One-Way Communication, T1059.001 PowerShell | Cloud and Code Hosting Services | 情報なし | 情報なし | 高 |
| 北朝鮮関連のKimsuky、継続的なサイバー攻撃でコンパイル済みHTMLヘルプファイルに移行 | Kimsuky | 情報なし | T1059.005 Visual Basic | 情報なし | 韓国 | 被害事例: 北朝鮮関連のKimsuky、継続的なサイバー攻撃でコンパイル済みHTMLヘルプファイルに移行 | 高 |
| 北朝鮮系ハッカーが「ClickFix」を悪用し、暗号資産の偽求人でBeaverTailを配布 | Kimsuky | 情報なし | T1204.004 Malicious Copy and Paste | 情報なし | 情報なし | 情報なし | 中 |
| 北朝鮮のハッカー、新しいKLogEXEとFPSpyマルウェアを標的型攻撃に使用 | Kimsuky | 情報なし | T1056.001 Keylogging, T1082 System Information Discovery | 情報なし | 情報なし | 情報なし | 中 |
| Smoke Screen / Stealth Power | Kimsuky | 情報なし | T1056.001 Keylogging, T1059.001 Command and Scripting Interpreter: PowerShell, T1566.001 Phishing: Spearphishing Attachment | Compromised Web Servers, Lookalike Phishing Domains | Government and Diplomacy, 韓国 | 被害事例: Smoke Screen / Stealth Power | 高 |
| Operation Newton | Kimsuky | AppleSeed, FastViewer Android Malware, KGH Spyware | T1505.003 Web Shell, T1041 Exfiltration Over C2 Channel, T1056.003 Input Capture: Web Portal Capture, T1505.003 Server Software Component: Web Shell, T1566.002 Phishing: Spearphishing Link | Cloud and Code Hosting Services, Compromised Web Servers, Lookalike Phishing Domains | Think Tanks and Academia | 被害事例: Operation Newton | 高 |
| Browser Extension and Google Play Abuse | Kimsuky | AppleSeed, FastViewer Android Malware | T1114 Email Collection, T1566.002 Phishing: Spearphishing Link | Cloud and Code Hosting Services, Lookalike Phishing Domains | ドイツ, Think Tanks and Academia | 被害事例: Browser Extension and Google Play Abuse | 高 |
| Operation DarkHorse | Kimsuky | 情報なし | T1059.001 Command and Scripting Interpreter: PowerShell, T1566.001 Phishing: Spearphishing Attachment | Compromised Web Servers, Lookalike Phishing Domains | Finance, Insurance, and Cryptocurrency | 被害事例: Operation DarkHorse | 中 |
| 北朝鮮のハッカー、新たなGolangマルウェア「Durian」を暗号通貨企業に対して使用 | Kimsuky | 情報なし | 情報なし | 情報なし | 韓国 | 被害事例: 北朝鮮のハッカー、新たなGolangマルウェア「Durian」を暗号通貨企業に対して使用 | 中 |
| Kimsukyハッカー、韓国への攻撃に新しいLinuxバックドアを使用 | Kimsuky | 情報なし | T1083 File and Directory Discovery | 情報なし | 政府・行政, 韓国 | 被害事例: Kimsukyハッカー、韓国への攻撃に新しいLinuxバックドアを使用 | 高 |
| Kimsuky、TRANSLATEXT Chrome拡張機能を使用して機密データを盗む | Kimsuky | 情報なし | T1113 Screen Capture | 情報なし | 情報なし | 情報なし | 高 |
| 国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開 | Kimsuky | 情報なし | T1204.004 Malicious Copy and Paste | 情報なし | 教育・研究 | 被害事例: 国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開 | 中 |
| 北朝鮮のハッカー、PowerShellの手法を悪用して新たなサイバー攻撃を実行 | Kimsuky | 情報なし | 情報なし | 情報なし | 政府・行政 | 被害事例: 北朝鮮のハッカー、PowerShellの手法を悪用して新たなサイバー攻撃を実行 | 中 |
| Kimsuky QR-code Spearphishing Campaign | Kimsuky | 情報なし | T1056.003 Input Capture: Web Portal Capture, T1098 Account Manipulation, T1550.004 Use Alternate Authentication Material: Web Session Cookie, T1566.002 Phishing: Spearphishing Link | QR-code Credential Phishing Infrastructure | Journalists and Policy Experts, Think Tanks and Academia | 被害事例: Kimsuky QR-code Spearphishing Campaign | 高 |
| Kimsuky、武器化QRコード経由で悪性モバイルアプリを配布し利用者を攻撃 | Kimsuky | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 高 |
| 2026年第1四半期 DPRK Operation Kimsuky 分析 | Kimsuky | 情報なし | T1027 Obfuscated Files or Information, T1053.005 Scheduled Task | Cloud and Code Hosting Services | 暗号資産・Web3, IT・ソフトウェア, 防衛・軍事, 教育・研究 | 被害事例: 2026年第1四半期 DPRK Operation Kimsuky 分析 | 中 |

少なくとも2012年から活動。2019年のSmoke ScreenとAppleSeed、2020-2021年のOperation Newton、2022-2023年のDarkHorseとCovert Stalker、2023年のブラウザ拡張・Google Play悪用、2024年のDMARC悪用へと配送・収集能力を更新している。

2025年5月から6月、FBIはKimsukyがQRコードを用いてシンクタンクや戦略助言組織を標的にし、偽Googleログイン等で認証情報を窃取する活動を観測した。

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | イラン | 活動「国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開」の記述で標的・被害国として明示されている。 | 2025-01 | 2025-02 | 中 | `source--daily-07ef6046e1668f840b3a` |
| countries | ウクライナ | 構造化OSINTの被害国フィールドでKimsukyの標的・被害国としてウクライナが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | タイ | 構造化OSINTの被害国フィールドでKimsukyの標的・被害国としてタイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ドイツ | 政策専門家および防衛関連。 | 2021 | 2024 | 高 | `source--browser-advisory-2023`, `source--qax-2024`, `source--target-audit-misp-threat-actor` |
| countries | ベトナム | 構造化OSINTの被害国フィールドでKimsukyの標的・被害国としてベトナムが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ロシア | 活動「国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開」の記述で標的・被害国として明示されている。 | 2025-01 | 2025-02 | 中 | `source--daily-07ef6046e1668f840b3a` |
| countries | 中国 | 活動「国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開」の記述で標的・被害国として明示されている。 | 2025-01 | 2025-02 | 中 | `source--daily-07ef6046e1668f840b3a` |
| countries | 日本 | 活動「日本、北朝鮮のKimsukyハッカーに関連する攻撃を警告」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-00bf22365ce019ee25a6`, `source--daily-d930e3ca01c519bf5740`, `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | 活動「FBI、KimsukyがQRコードを使って米国組織をフィッシングしていると警告」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-4c3098e731ae81f16008`, `source--target-audit-etda-threat-group-cards` |
| countries | 韓国 | 最重要の継続的対象。 | 2012 | 2026-04 | 高 | `source--daily-00bf22365ce019ee25a6`, `source--daily-01bbfa4ce1d271e9e220`, `source--daily-0477636fe03aea54224d`, `source--daily-444c87a0051642065f55`, `source--daily-a5ca98841868974d600b`, `source--daily-b9be11e58ab6c82617ab`, `source--daily-f05f4888998c8f53f5ca`, `source--joint-csa-2023`, `source--mitre-attack-19-1`, `source--rapid7-2024`, `source--target-audit-etda-threat-group-cards` |
| regions | アジア | 活動「北朝鮮関連のKimsuky、継続的なサイバー攻撃でコンパイル済みHTMLヘルプファイルに移行」の記述で標的地域としてアジアが明示されている。 | 不明 | 不明 | 中 | `source--daily-0477636fe03aea54224d` |
| regions | 北米 | 活動「北朝鮮関連のKimsuky、継続的なサイバー攻撃でコンパイル済みHTMLヘルプファイルに移行」の記述で標的地域として北米が明示されている。 | 不明 | 不明 | 中 | `source--daily-0477636fe03aea54224d` |
| regions | 東アジア | 中国、日本、韓国で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-00bf22365ce019ee25a6`, `source--daily-01bbfa4ce1d271e9e220`, `source--daily-0477636fe03aea54224d`, `source--daily-07ef6046e1668f840b3a`, `source--daily-444c87a0051642065f55`, `source--daily-a5ca98841868974d600b`, `source--daily-b9be11e58ab6c82617ab`, `source--daily-d930e3ca01c519bf5740`, `source--daily-f05f4888998c8f53f5ca`, `source--joint-csa-2023`, `source--mitre-attack-19-1`, `source--rapid7-2024`, `source--target-audit-etda-threat-group-cards` |
| regions | 東南アジア | タイ、ベトナムで確認された標的・被害事例を東南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東欧 | ウクライナ、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-07ef6046e1668f840b3a`, `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | 活動「北朝鮮関連のKimsuky、継続的なサイバー攻撃でコンパイル済みHTMLヘルプファイルに移行」の記述で標的地域として欧州が明示されている。 | 不明 | 不明 | 中 | `source--browser-advisory-2023`, `source--daily-0477636fe03aea54224d`, `source--qax-2024`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| sectors | メディア・報道 | 活動「Kimsukyは寛容なDMARCポリシーを利用してメールを偽装」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-8c76eeb938a1170375af` |
| sectors | 暗号資産・Web3 | 活動「北朝鮮マルウェアのモジュール化：多様性と機能特化」の記述で標的として明示された産業。 | 2026-01 | 2026-06 | 中 | `source--daily-ec97ed0896afb842c91e`, `source--daily-f3e6fda98089cb5da96d` |
| sectors | IT・ソフトウェア | 活動「北朝鮮マルウェアのモジュール化：多様性と機能特化」の記述で標的として明示された産業。 | 2026-01 | 2026-06 | 中 | `source--daily-ec97ed0896afb842c91e`, `source--daily-f3e6fda98089cb5da96d` |
| sectors | 防衛・軍事 | 活動「2026年第1四半期 DPRK Operation Kimsuky 分析」の記述で標的として明示された産業。 | 2026-01 | 2026-06 | 中 | `source--daily-b9be11e58ab6c82617ab`, `source--daily-f3e6fda98089cb5da96d` |
| sectors | Finance, Insurance, and Cryptocurrency | 金融契約、保険、暗号資産関連の組織と個人。 | 2022 | 2024 | 中 | `source--darkhorse-2023`, `source--qax-2024` |
| sectors | Government and Diplomacy | 政府、議会、外交、政策関係者。 | 2012 | 2025 | 高 | `source--joint-csa-2023` |
| sectors | 政府・行政 | The group initially targeted South Korean government agencies, think tanks, and subject-matter experts in various fields. | 2024 | 2024 | 高 | `source--daily-01bbfa4ce1d271e9e220`, `source--daily-8c76eeb938a1170375af`, `source--daily-b859524205edbc7c576c`, `source--daily-d930e3ca01c519bf5740`, `source--mitre-attack-19-1` |
| sectors | 製造・産業 | Its operations expanded to include the United Nations and organizations in the government, education, business services, and manufacturing sectors across the United States, Japan, Russia, and Europe. | 不明 | 不明 | 高 | `source--daily-444c87a0051642065f55`, `source--daily-b9be11e58ab6c82617ab`, `source--daily-ec97ed0896afb842c91e`, `source--mitre-attack-19-1` |
| sectors | 教育・研究 | The group initially targeted South Korean government agencies, think tanks, and subject-matter experts in various fields. | 2025-01 | 2026-06 | 高 | `source--daily-07ef6046e1668f840b3a`, `source--daily-8c76eeb938a1170375af`, `source--daily-d930e3ca01c519bf5740`, `source--daily-f3e6fda98089cb5da96d`, `source--mitre-attack-19-1` |
| sectors | Think Tanks and Academia | 政策研究、大学、学術、科学・工学研究者。 | 2012 | 2025 | 高 | `source--joint-csa-2023`, `source--rapid7-2024` |
| roles | Journalists and Policy Experts | DPRK政策に関する非公開見解と信頼ネットワークを持つ個人。 | 2012 | 2025 | 高 | `source--joint-csa-2023`, `source--dmarc-2024` |

選定ロジック: 組織規模より、北朝鮮に関する非公開情報や信頼ネットワークへアクセスできる個人を優先する。 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Operation DarkHorse | 非公開 | anonymous | unknown | reported | target--finance |  | ttp--t1059-001--powershell, ttp--t1566-001--documents |  |  | 2022-02 | 不明 | 2023-10-16 | 中 | `source--darkhorse-2023` |
| 被害事例: 日本、北朝鮮のKimsukyハッカーに関連する攻撃を警告 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--f35cd09db0a72555b38a, target--mitre-group--sector--4eba90b76b16e9d6d89b, target--mitre-group--sector--c5b1f7936acf85af11e4 |  | ttp--activity-rule--300616f23614b4974d79 | メール／メールアカウント |  | 不明 | 不明 | 2024-07-11 | 高 | `source--daily-d930e3ca01c519bf5740` |
| 被害事例: 北朝鮮のハッキンググループが韓国の防衛請負業者を侵害 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--b94dc560a327b601965d, target--mitre-group--sector--85e4128fa590941f9478, target--south-korea |  |  | クラウド／SaaS |  | 不明 | 不明 | 2024-04-24 | 中 | `source--daily-b9be11e58ab6c82617ab` |
| 被害事例: 2026年第1四半期 DPRK Operation Kimsuky 分析 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--63c9fa67327d005b07b7, target--activity-rule--sector--932f4928d5e1ec28e2df, target--activity-rule--sector--b94dc560a327b601965d, target--mitre-group--sector--c5b1f7936acf85af11e4 |  | ttp--activity-rule--4e7a9106baf629cb2a5d, ttp--activity-rule--e326bf94ac733031173e | 開発環境／ソースコード |  | 2026-01 | 2026-06 | 2026-05-20 | 中 | `source--daily-f3e6fda98089cb5da96d` |
| 被害事例: Kimsuky、BlueKeep RDP脆弱性を悪用し、韓国と日本のシステムを侵害 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--f35cd09db0a72555b38a, target--south-korea |  | ttp--activity-rule--8efb9226234d380e7b25 | メール／メールアカウント | espionage: 最終的に、KimaLoggerやRandomQueryなどのキーロガーを展開し、情報収集を行う。 | 不明 | 不明 | 2025-04-22 | 高 | `source--daily-00bf22365ce019ee25a6` |
| 被害事例: Kimsukyハッカー、韓国への攻撃に新しいLinuxバックドアを使用 | 非公開 | anonymous | unknown | reported | target--mitre-group--sector--4eba90b76b16e9d6d89b, target--south-korea |  | ttp--activity-rule--d97d1bd687c6c8f70793 | サーバー |  | 2024 | 2024 | 2024-05-17 | 高 | `source--daily-01bbfa4ce1d271e9e220` |
| 被害事例: 国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開 | 非公開 | aggregate | multiple-organizations | reported | target--mitre-group--sector--c5b1f7936acf85af11e4 |  | ttp--activity-rule--1f8b1ff7e839aaca7ece |  |  | 2025-01 | 2025-02 | 2025-04-18 | 中 | `source--daily-07ef6046e1668f840b3a` |
| 被害事例: VS Codeエクステンションを悪用するKimsuky：ランサムウェアと永続化のためのキャンペーンとは？ | 非公開 | anonymous | unknown | reported |  |  | ttp--activity-rule--5bc4f7380e62aafda9c6, ttp--activity-rule--9d7fe74bcca8ad1357ae, ttp--activity-rule--acef6838bb761cf3129e |  | encryption: VS Codeエクステンションを悪用するKimsuky：ランサムウェアと永続化のためのキャンペーンとは？ | 不明 | 不明 | 2025-11-19 | 高 | `source--daily-28742c9ae0a7173b9225` |
| 被害事例: Browser Extension and Google Play Abuse | 非公開 | anonymous | unknown | reported | target--germany, target--research-academia | malware--fastviewer | ttp--t1114--email-collection, ttp--t1566-002--credential-links |  |  | 2022 | 不明 | 2023-03-20 | 高 | `source--browser-advisory-2023` |
| 被害事例: Kimsuky QR-code Spearphishing Campaign | 非公開 | anonymous | unknown | reported | target--journalists-policy-experts, target--research-academia |  | ttp--t1056-003--kimsuky-quishing-2025, ttp--t1098--kimsuky-quishing-2025, ttp--t1550-004--kimsuky-quishing-2025, ttp--t1566-002--kimsuky-quishing-2025 |  |  | 2025-05 | 2025-06 | 2026-01-08 | 高 | `source--fbi-kimsuky-quishing-2026` |
| 被害事例: Kimsukyの高度な攻撃手法：JSONPing、Webex偽装、新たなHttpSpy亜種 | 非公開 | aggregate | multiple-organizations | reported | target--south-korea | malware--daily-1432659072aa52651920 |  | サーバー, エンドポイント |  | 不明 | 2026-04 | 2026-05-30 | 中 | `source--daily-f05f4888998c8f53f5ca` |
| 被害事例: 北朝鮮のハッカー、PowerShellの手法を悪用して新たなサイバー攻撃を実行 | 非公開 | aggregate | multiple-organizations | reported | target--mitre-group--sector--4eba90b76b16e9d6d89b |  |  | メール／メールアカウント, サーバー, エンドポイント |  | 2025-01 | 不明 | 2025-02-13 | 中 | `source--daily-b859524205edbc7c576c` |
| 被害事例: 北朝鮮のハッカー、新たなGolangマルウェア「Durian」を暗号通貨企業に対して使用 | 非公開 | aggregate | multiple-organizations | reported | target--south-korea |  |  |  |  | 2023-08 | 2023-11 | 2024-05-11 | 中 | `source--daily-a5ca98841868974d600b` |
| 被害事例: Operation Newton | 非公開 | anonymous | unknown | reported | target--research-academia | malware--appleseed | ttp--activity-rule--4c1985318db9368ef803, ttp--t1041--exfiltration-c2, ttp--t1056-003--web-portal, ttp--t1505-003--webshell, ttp--t1566-002--credential-links |  |  | 2020 | 不明 | 2021-10 | 高 | `source--operation-newton` |
| 被害事例: Smoke Screen / Stealth Power | 非公開 | anonymous | unknown | reported | target--government-diplomacy, target--south-korea |  | ttp--activity-rule--a2250f5bde5c4e0d27c0, ttp--t1059-001--powershell, ttp--t1566-001--documents |  |  | 2019-03 | 2019-05 | 2019-04-17 | 高 | `source--smoke-screen` |
| 被害事例: 北朝鮮マルウェアのモジュール化：多様性と機能特化 | 非公開 | anonymous | unknown | reported | target--activity-rule--sector--63c9fa67327d005b07b7, target--activity-rule--sector--932f4928d5e1ec28e2df, target--mitre-group--sector--85e4128fa590941f9478 |  | ttp--activity-rule--139ca10483e8bad29269 | クラウド／SaaS | espionage: 諜報系は Kimsuky を代表例とし、PowerShell や VBS、ソーシャルエンジニアリング、クラウド悪用、長期潜伏による静かな情報収集を重視すると説明する。 | 不明 | 不明 | 2026-04-06 | 中 | `source--daily-ec97ed0896afb842c91e` |
| 被害事例: FBI、KimsukyがQRコードを使って米国組織をフィッシングしていると警告 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--6604ad21c713b8dfd8c7 |  | ttp--activity-rule--32b62558046788e695f4 | メール／メールアカウント | credential-theft: QRをスマホで読ませてメール防御を迂回し、偽ログイン等へ誘導して資格情報やセッショントークン窃取→MFA回避に繋げる手口。 | 不明 | 不明 | 2026-01-10 | 高 | `source--daily-4c3098e731ae81f16008` |
| 被害事例: Kimsukyは寛容なDMARCポリシーを利用してメールを偽装 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--5403aec9c83d6a925f61, target--mitre-group--sector--4eba90b76b16e9d6d89b, target--mitre-group--sector--c5b1f7936acf85af11e4 |  |  | メール／メールアカウント | espionage: Kimsukyは認証に失敗しても何しないとなっているドメインになりすます 攻撃は情報収集を目的としており、標的はシンクタンク、政府、ジャーナリスト 攻撃メールには、ターゲットによる電子メールの開封有無、いつ、どのデバイスで開いたかなどのデータを追跡するために、追跡ピクセルが埋め込まれている | 不明 | 不明 | 2024-04-17 | 高 | `source--daily-8c76eeb938a1170375af` |
| 被害事例: 北朝鮮のハッカーがVPN更新の脆弱性を悪用してマルウェアをインストール | 非公開 | anonymous | unknown | reported | target--mitre-group--sector--85e4128fa590941f9478, target--south-korea |  | ttp--activity-rule--866c7fa9fa78e9f314c7 | VPN／リモートアクセス機器 |  | 不明 | 不明 | 2024-08-06 | 中 | `source--daily-444c87a0051642065f55` |
| 被害事例: 北朝鮮関連のKimsuky、継続的なサイバー攻撃でコンパイル済みHTMLヘルプファイルに移行 | 非公開 | anonymous | unknown | reported | target--south-korea |  | ttp--activity-rule--aab21b466b971ffe5f9e |  | data-theft: ファイルを利用し機密データを盗む新手法を使用 2012年から活動、主に韓国、北米、アジア、ヨーロッパを標的 攻撃ではISO、LNKファイル、Office文書も利用 CHMファイルはISO、VHD、ZIP、RAR内で配布、JavaScript実行 感染の流れは、CHM file > html file > vbs file(C2と接続) C2と接続後、収集したデータをDATファイルにして窃取 | 不明 | 不明 | 2024-03-25 | 高 | `source--daily-0477636fe03aea54224d` |
| 被害事例: 北朝鮮のAPT「Kimsuky」、LNKファイルを使用してブラウザに保存された認証情報を窃取するforceCopyマルウェアを配布 | 非公開 | anonymous | unknown | reported |  |  | ttp--activity-rule--9f5f511f9650ee41dace, ttp--activity-rule--e0f37374ccce7abb7368, ttp--activity-rule--f0e72b5798f70a2f9617 | メール／メールアカウント | data-theft: 北朝鮮のAPT「Kimsuky」、LNKファイルを使用してブラウザに保存された認証情報を窃取するforceCopyマルウェアを配布<br>credential-theft: 北朝鮮のAPT「Kimsuky」、LNKファイルを使用してブラウザに保存された認証情報を窃取するforceCopyマルウェアを配布 | 不明 | 不明 | 2025-02-07 | 高 | `source--daily-6f57fcf4dc3991af9b4e` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Collection, Credential Access | T1056.001 | Keylogging | KLogEXEはキーロガーで、実行中のアプリケーションやキーストロークを収集。 |  | activity--daily-f50d80d6e62f1cc6f82d | 不明 | 不明 | 中 | `source--daily-5d4c990e46241ee39e8d` |
| Execution | T1059.001 | PowerShell | 諜報系は Kimsuky を代表例とし、PowerShell や VBS、ソーシャルエンジニアリング、クラウド悪用、長期潜伏による静かな情報収集を重視すると説明する。 |  | activity--daily-1a2aa6449d0568cc8dea | 不明 | 不明 | 中 | `source--daily-ec97ed0896afb842c91e` |
| Execution | T1204.004 | Malicious Copy and Paste | 国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開 |  | activity--daily-0c474e6b7ce54ba49c5e | 2025-01 | 2025-02 | 中 | `source--daily-07ef6046e1668f840b3a` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | pp.ps1はDropboxをC2伝達に使って端末情報を送信し、続くhh.batは分割ZIPからbeauty.pyを展開して別のスケジュールタスクでPythonバックドアを起動する。 |  | activity--daily-dab1d0dba78542a4ea0f | 不明 | 不明 | 中 | `source--daily-d289a4c2f4400dbffb6f` |
| Initial Access | T1566.001 | Spearphishing Attachment | 日本政府は北朝鮮のKimsukyハッカーによるサイバー攻撃のリスクを警告 攻撃対象は政府機関、大学、研究機関 Kimsukyはフィッシング攻撃とマルウェア感染を使用 攻撃はフィッシングから始まり、悪意のある ZIP ファイルを添付したフィッシング メールを日本の標的に送信。 |  | activity--daily-3cf8adbe41fb4452e711 | 不明 | 不明 | 中 | `source--daily-d930e3ca01c519bf5740` |
| Initial Access | T1566.002 | Spearphishing Link | FBI、KimsukyがQRコードを使って米国組織をフィッシングしていると警告 |  | activity--daily-7fba10858bc6d43d600f | 不明 | 不明 | 中 | `source--daily-4c3098e731ae81f16008` |
| Execution | T1059.006 | Python | Pythonベースのバックドアを配布する悪性LNKファイルと配布手法の変化（Kimsukyグループ） |  | activity--daily-dab1d0dba78542a4ea0f | 不明 | 不明 | 中 | `source--daily-d289a4c2f4400dbffb6f` |
| Persistence | T1505.003 | Web Shell | 工学研究者への資格情報フィッシングからAppleSeed、Webシェル、サーバ横展開へ進む活動。 | malware--appleseed | activity--operation-newton | 2020 | 不明 | 中 | `source--operation-newton` |
| Stealth | T1027 | Obfuscated Files or Information | LNK/JSEによる初期実行、LotL、難読化、タスクスケジューラ永続化、uid/IP/MACによる被害者識別が共通TTPとして整理されている。 |  | activity--daily-9a84486a6c98d6fea40f | 2026-01 | 2026-06 | 中 | `source--daily-f3e6fda98089cb5da96d` |
| Stealth | T1027 | Obfuscated Files or Information | 初期ドロッパー“Themes.js”はmedianewsonline[.]com上に置かれ、難読化薄めのコードで通信を開始する設計。 |  | activity--daily-3996d05478fc77c622e2 | 不明 | 不明 | 中 | `source--daily-28742c9ae0a7173b9225` |
| Collection | T1113 | Screen Capture | 拡張機能は、メールアドレス、ユーザー名、パスワード、クッキー、ブラウザのスクリーンショットを収集。 |  | activity--daily-a75732bcf0cbd93ba89d | 2024-03 | 2024-03 | 中 | `source--daily-303f2ea1899dc2bdab19` |
| Initial Access | T1190 | Exploit Public-Facing Application | 北朝鮮のハッカーがVPN更新の脆弱性を悪用してマルウェアをインストール 攻撃者はKimsukyとAndariel（APT43とAPT45）で、韓国の産業機密を狙う。 |  | activity--daily-2b96011a31e356d6d9ab | 不明 | 不明 | 中 | `source--daily-444c87a0051642065f55` |
| Collection, Credential Access | T1056.001 | Keylogging | 最終的に、KimaLoggerやRandomQueryなどのキーロガーを展開し、情報収集を行う。 |  | activity--daily-8721476f36a3485f1496 | 不明 | 不明 | 中 | `source--daily-00bf22365ce019ee25a6` |
| Discovery | T1057 | Process Discovery | C:\Users配下の列挙やプロセス収集を実施し、結果をCAB化して同C2へPOSTで流出、CodePageをUTF-8に変更。 |  | activity--daily-3996d05478fc77c622e2 | 不明 | 不明 | 中 | `source--daily-28742c9ae0a7173b9225` |
| Credential Access | T1555.003 | Credentials from Web Browsers | 北朝鮮のAPT「Kimsuky」、LNKファイルを使用してブラウザに保存された認証情報を窃取するforceCopyマルウェアを配布 |  | activity--daily-309ace8d538b441913e7 | 不明 | 不明 | 中 | `source--daily-6f57fcf4dc3991af9b4e` |
| Collection, Credential Access | T1056.001 | Keylogging | DPRK関連のHWP/DOCフィッシング、HTA、PowerShellキーロガーを伴う活動。 |  | activity--smoke-screen | 2019-03 | 2019-05 | 中 | `source--smoke-screen` |
| Discovery | T1082 | System Information Discovery | FPSpyはシステム情報を収集し、任意のコマンドを実行できるバックドア型マルウェア。 |  | activity--daily-f50d80d6e62f1cc6f82d | 不明 | 不明 | 中 | `source--daily-5d4c990e46241ee39e8d` |
| Execution | T1059.005 | Visual Basic | Kimsuky、CHMファイルを利用し機密データを盗む新手法を使用 2012年から活動、主に韓国、北米、アジア、ヨーロッパを標的 攻撃ではISO、LNKファイル、Office文書も利用 CHMファイルはISO、VHD、ZIP、RAR内で配布、JavaScript実行 感染の流れは、CHM file > html file > vbs file(C2と接続) C2と接続後、収集したデータをDATファイルにして窃取 |  | activity--daily-ea9ff4545671891d56e1 | 不明 | 不明 | 中 | `source--daily-0477636fe03aea54224d` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | %APPDATA%配下に自身を保存しタスクでwscriptを毎分実行、空のWord文書配布も確認され二次感染に用いる可能性。 |  | activity--daily-3996d05478fc77c622e2 | 不明 | 不明 | 中 | `source--daily-28742c9ae0a7173b9225` |
| Stealth | T1036 | Masquerading | PowerShellとVBScriptを使用しWindowsシステムを感染させ、情報を窃取 このキャンペーンは、北朝鮮のKimsukyと関連があるとSecuronixが指摘 DropboxやGoogle Docsを利用し、C2通信を隠蔽 開始点はPDFファイルに偽装した悪意あるメール添付ファイル TruRatを含む複数のステージを持つ高度なマルウェア |  | activity--daily-6bbe7ca259b014595e2a | 不明 | 不明 | 中 | `source--daily-66a67b66f7f04fd72d52` |
| Command And Control | T1102.003 | One-Way Communication | pp.ps1はDropboxをC2伝達に使って端末情報を送信し、続くhh.batは分割ZIPからbeauty.pyを展開して別のスケジュールタスクでPythonバックドアを起動する。 |  | activity--daily-dab1d0dba78542a4ea0f | 不明 | 不明 | 中 | `source--daily-d289a4c2f4400dbffb6f` |
| Discovery | T1083 | File and Directory Discovery | 操作の例: C&Cサーバーとの通信を一時停止、任意のシェルコマンドを実行、リモート接続用のリバース プロキシを開始、システムからファイルを取得、など |  | activity--daily-7a9584dd178b67430a5e | 2024 | 2024 | 中 | `source--daily-01bbfa4ce1d271e9e220` |
| Stealth | T1036 | Masquerading | 攻撃は、Microsoft OfficeやPDF文書に偽装したLNKファイルを含むフィッシングメールから始まる。 |  | activity--daily-309ace8d538b441913e7 | 不明 | 不明 | 中 | `source--daily-6f57fcf4dc3991af9b4e` |
| Execution | T1204.004 | Malicious Copy and Paste | 北朝鮮系ハッカーが「ClickFix」を悪用し、暗号資産の偽求人でBeaverTailを配布 |  | activity--daily-f1c379b17bba17ff7692 | 不明 | 不明 | 中 | `source--daily-dddef70e68c0dc59a5d3` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | LNK/JSEによる初期実行、LotL、難読化、タスクスケジューラ永続化、uid/IP/MACによる被害者識別が共通TTPとして整理されている。 |  | activity--daily-9a84486a6c98d6fea40f | 2026-01 | 2026-06 | 中 | `source--daily-f3e6fda98089cb5da96d` |
| Command And Control | T1102.003 | One-Way Communication | PowerShellとVBScriptを使用しWindowsシステムを感染させ、情報を窃取 このキャンペーンは、北朝鮮のKimsukyと関連があるとSecuronixが指摘 DropboxやGoogle Docsを利用し、C2通信を隠蔽 開始点はPDFファイルに偽装した悪意あるメール添付ファイル TruRatを含む複数のステージを持つ高度なマルウェア |  | activity--daily-6bbe7ca259b014595e2a | 不明 | 不明 | 中 | `source--daily-66a67b66f7f04fd72d52` |
| Command And Control | T1105 | Ingress Tool Transfer | LNKファイルを開くと、PowerShellやmshta.exeが実行され、外部から次のペイロードをダウンロード・実行。 |  | activity--daily-309ace8d538b441913e7 | 不明 | 不明 | 中 | `source--daily-6f57fcf4dc3991af9b4e` |
| Execution | T1059.001 | PowerShell | 従来はLNK→PowerShell→BATの比較的単純な流れだったが、最近はLNK→PowerShell→デコイ/XML/PS1/VBS生成へ変化し、中間段階が多段化した。 |  | activity--daily-dab1d0dba78542a4ea0f | 不明 | 不明 | 中 | `source--daily-d289a4c2f4400dbffb6f` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | HTTP、FTP、メールC2を通じて収集データを流出させる。 | malware--appleseed, malware--kgh | activity--operation-newton | 2019-05-06 | 2025 | 高 | `source--operation-newton`, `source--kgh-2021` |
| Persistence | T1053.005 | Scheduled Task/Job: Scheduled Task | マルウェアやスクリプトを定期実行するタスクを作成する。 | malware--appleseed |  | 2019-05-06 | 2024 | 高 | `source--operation-newton`, `source--rapid7-2024` |
| Credential Access, Collection | T1056.003 | Input Capture: Web Portal Capture | A fake Google account login page collected credentials entered by targeted users. |  | activity--kimsuky-quishing-2025 | 2025-06 | 2025-06 | 高 | `source--fbi-kimsuky-quishing-2026` |
| Credential Access | T1056.003 | Input Capture: Web Portal Capture | 偽ログインページとプロキシで認証情報を窃取する。 |  | activity--operation-newton | 2012 | 2025 | 高 | `source--joint-csa-2023`, `source--operation-newton` |
| Execution | T1059.001 | Command and Scripting Interpreter: PowerShell | 後段取得、復号、メモリ内実行、情報収集、持続化にPowerShellを使う。 |  | activity--smoke-screen, activity--darkhorse | 2019-03 | 2025 | 高 | `source--smoke-screen`, `source--rapid7-2024` |
| Persistence, Privilege Escalation | T1098 | Account Manipulation | The FBI lifecycle identifies account persistence or manipulation after successful credential and session theft. |  | activity--kimsuky-quishing-2025 | 2025-05 | 2025-06 | 高 | `source--fbi-kimsuky-quishing-2026` |
| Collection | T1114 | Email Collection | 資格情報、ブラウザ拡張、メール転送等でメールボックス内容を窃取する。 |  | activity--browser-google-play | 2012 | 2025 | 高 | `source--joint-csa-2023`, `source--browser-advisory-2023` |
| Persistence | T1505.003 | Server Software Component: Web Shell | 侵害WebサーバにPHP/JSP Webシェルを配置し、C2管理とファイル操作に使う。 |  | activity--operation-newton | 2019 | 2023-09 | 高 | `source--operation-newton`, `source--covert-stalker` |
| Lateral Movement | T1550.004 | Use Alternate Authentication Material: Web Session Cookie | The FBI attack lifecycle identifies session-token theft and MFA bypass following credential capture. |  | activity--kimsuky-quishing-2025 | 2025-05 | 2025-06 | 高 | `source--fbi-kimsuky-quishing-2026` |
| Initial Access | T1566.001 | Phishing: Spearphishing Attachment | HWP、Office、LNK、CHM、MSC、パスワード付きアーカイブを配送する。 |  | activity--smoke-screen, activity--darkhorse | 2012 | 2025 | 高 | `source--rapid7-2024`, `source--darkhorse-2023` |
| Initial Access | T1566.002 | Phishing: Spearphishing Link | 資格情報フィッシング、侵害サイト、クラウド上のペイロードへのリンクを送る。 | malware--appleseed, malware--fastviewer | activity--operation-newton, activity--browser-google-play | 2012 | 2025 | 高 | `source--joint-csa-2023`, `source--operation-newton` |
| Initial Access | T1566.002 | Phishing: Spearphishing Link | Delivered QR images in targeted emails; scanning the code led the victim to a registration or secure-drive lure and onward to credential harvesting. |  | activity--kimsuky-quishing-2025 | 2025-05 | 2025-06 | 高 | `source--fbi-kimsuky-quishing-2026` |
| Reconnaissance | T1589 | Gather Victim Identity Information | 専門家、記者、研究者、連絡先をOSINTで調査する。 |  |  | 2012 | 2025 | 高 | `source--joint-csa-2023`, `source--dmarc-2024` |

## IOC／artifact概要

- IOC値: 989件
- IOC観測: 1254件
- 複数攻撃で観測: 0件
- 要レビュー候補: 279件
- 非IOC artifact観測: 871件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| Kimsukyの中核任務は北朝鮮政権のための戦略諜報と認証情報・メール窃取である。 | 高 | `source--joint-csa-2023`, `source--dmarc-2024` |  |
| 最大の強みは高度なソーシャルエンジニアリングと信頼構築である。 | 高 | `source--joint-csa-2023`, `source--rapid7-2024` |  |
| Kimsuky added QR-code delivery to its established trust-building spearphishing and credential-theft workflow during May-June 2025. | 高 | `source--fbi-kimsuky-quishing-2026` |  |
| MITRE treats APT43 as an associated Kimsuky group name, while Mandiant defines APT43 using its own collection scope. The overlap is well supported, but exact one-to-one identity is not. | 高 | `source--mitre-live-kimsuky-2026`, `source--mandiant-apt43-2023` | verification_status=partially-supported; Vendor collection boundaries differ; do not replace both profiles with a single exact alias record. The sources support overlap but do not establish that every APT43 observation belongs to the narrower Kimsuky activity set. |

### 情報ギャップ

- ベンダー別クラスタ間の厳密な境界。
- DPRK内部でのツール共有と開発者再配置の実態。
- 一部画像主体PDFの完全なテキスト抽出。

### 不確実性

- APT37、Konni、Lazarusとの重複は同一性ではなく共有・再利用で説明できる。
- DarkHorseのKimsuky帰属には競合評価がある。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--blurred-attribution | Blurred Lines of Cyber Threat Attribution | Repository source | 2025 | International Strategic/Korea/ Blurred-Lines-of-Cyber-Threat-Attribution.pdf | conference-report | TLP:CLEAR | 中 |
| source--browser-advisory-2023 | Warning on KIMSUKY Cyber Actor's Recent Campaigns against Google's Browser and App Store Services | BfV and NIS | 2023-03-20 | kimsuky/kimsuky-2023-03-20-joint-cyber-security-advisory.pdf | government-advisory | TLP:CLEAR | 高 |
| source--covert-stalker | Operation Covert Stalker | AhnLab | 2023-11-01 | kimsuky/20231101_Kimsuky_OP.-Covert-Stalker-EN.pdf | vendor-report | TLP:CLEAR | 高 |
| source--daily-00bf22365ce019ee25a6 | Kimsuky、BlueKeep RDP脆弱性を悪用し、韓国と日本のシステムを侵害 | thehackernews.com | 2025-04-22 | https://thehackernews.com/2025/04/kimsuky-exploits-bluekeep-rdp.html | osint-report | TLP:CLEAR | 中 |
| source--daily-01bbfa4ce1d271e9e220 | Kimsukyハッカー、韓国への攻撃に新しいLinuxバックドアを使用 | bleepingcomputer.com | 2024-05-17 | https://www.bleepingcomputer.com/news/security/kimsuky-hackers-deploy-new-linux-backdoor-in-attacks-on-south-korea/ | osint-report | TLP:CLEAR | 中 |
| source--daily-0477636fe03aea54224d | 北朝鮮関連のKimsuky、継続的なサイバー攻撃でコンパイル済みHTMLヘルプファイルに移行 | thehackernews.com | 2024-03-25 | https://thehackernews.com/2024/03/n-korea-linked-kimsuky-shifts-to.html | osint-report | TLP:CLEAR | 中 |
| source--daily-07ef6046e1668f840b3a | 国家支援ハッカー、ClickFix手法を武器化し標的型マルウェア攻撃を展開 | thehackernews.com | 2025-04-18 | https://thehackernews.com/2025/04/state-sponsored-hackers-weaponize.html | osint-report | TLP:CLEAR | 中 |
| source--daily-28742c9ae0a7173b9225 | VS Codeエクステンションを悪用するKimsuky：ランサムウェアと永続化のためのキャンペーンとは？ | iototsecnews.jp | 2025-11-19 | https://iototsecnews.jp/2025/11/07/threat-actors-may-abuse-vs-code-extensions-to-deploy-ransomware-and-use-github-as-c2-server/ | osint-report | TLP:CLEAR | 中 |
| source--daily-303f2ea1899dc2bdab19 | Kimsuky、TRANSLATEXT Chrome拡張機能を使用して機密データを盗む | thehackernews.com | 2024-06-29 | https://thehackernews.com/2024/06/kimsuky-using-translatext-chrome.html | osint-report | TLP:CLEAR | 中 |
| source--daily-444c87a0051642065f55 | 北朝鮮のハッカーがVPN更新の脆弱性を悪用してマルウェアをインストール | bleepingcomputer.com | 2024-08-06 | https://www.bleepingcomputer.com/news/security/north-korean-hackers-exploit-vpn-update-flaw-to-install-malware/ | osint-report | TLP:CLEAR | 中 |
| source--daily-4c3098e731ae81f16008 | FBI、KimsukyがQRコードを使って米国組織をフィッシングしていると警告 | bleepingcomputer.com | 2026-01-10 | https://www.bleepingcomputer.com/news/security/fbi-warns-about-kimsuky-hackers-using-qr-codes-to-phish-us-orgs/ | osint-report | TLP:CLEAR | 中 |
| source--daily-5d4c990e46241ee39e8d | 北朝鮮のハッカー、新しいKLogEXEとFPSpyマルウェアを標的型攻撃に使用 | thehackernews.com | 2024-09-27 | https://thehackernews.com/2024/09/n-korean-hackers-deploy-new-klogexe-and.html | osint-report | TLP:CLEAR | 中 |
| source--daily-66a67b66f7f04fd72d52 | 新たなDEEP#GOSUマルウェアキャンペーン、Windowsユーザーを高度な戦術で狙う | thehackernews.com | 2024-03-19 | https://thehackernews.com/2024/03/new-deepgosu-malware-campaign-targets.html | osint-report | TLP:CLEAR | 中 |
| source--daily-6f57fcf4dc3991af9b4e | 北朝鮮のAPT「Kimsuky」、LNKファイルを使用してブラウザに保存された認証情報を窃取するforceCopyマルウェアを配布 | thehackernews.com | 2025-02-07 | https://thehackernews.com/2025/02/north-korean-apt-kimsuky-uses-lnk-files.html | osint-report | TLP:CLEAR | 中 |
| source--daily-6f6e88199bc7e8479193 | Kimsukyグループによる外交関係者を装った攻撃事例（PebbleDash、PrxClient） | asec.ahnlab.com | 2026-07-30 | https://asec.ahnlab.com/jp/94655/ | osint-report | TLP:CLEAR | 中 |
| source--daily-75d0d2c890d6c822d6f6 | 北朝鮮のハッカー、標的型マルウェアキャンペーンでFacebook Messengerを悪用 | thehackernews.com | 2024-05-17 | https://thehackernews.com/2024/05/north-korean-hackers-exploit-facebook.html | osint-report | TLP:CLEAR | 中 |
| source--daily-8c76eeb938a1170375af | Kimsukyは寛容なDMARCポリシーを利用してメールを偽装 | databreachtoday.com | 2024-04-17 | https://www.databreachtoday.com/kimsuky-uses-permissive-dmarc-policies-to-spoof-emails-a-24857 | osint-report | TLP:CLEAR | 中 |
| source--daily-a5ca98841868974d600b | 北朝鮮のハッカー、新たなGolangマルウェア「Durian」を暗号通貨企業に対して使用 | thehackernews.com | 2024-05-11 | https://thehackernews.com/2024/05/north-korean-hackers-deploy-new-golang.html | osint-report | TLP:CLEAR | 中 |
| source--daily-b859524205edbc7c576c | 北朝鮮のハッカー、PowerShellの手法を悪用して新たなサイバー攻撃を実行 | thehackernews.com | 2025-02-13 | https://thehackernews.com/2025/02/north-korean-hackers-exploit-powershell.html | osint-report | TLP:CLEAR | 中 |
| source--daily-b9be11e58ab6c82617ab | 北朝鮮のハッキンググループが韓国の防衛請負業者を侵害 | bleepingcomputer.com | 2024-04-24 | https://www.bleepingcomputer.com/news/security/dprk-hacking-groups-breach-south-korean-defense-contractors/ | osint-report | TLP:CLEAR | 中 |
| source--daily-d289a4c2f4400dbffb6f | Pythonベースのバックドアを配布する悪性LNKファイルと配布手法の変化（Kimsukyグループ） | asec.ahnlab.com | 2026-04-04 | https://asec.ahnlab.com/en/93151/ | osint-report | TLP:CLEAR | 中 |
| source--daily-d930e3ca01c519bf5740 | 日本、北朝鮮のKimsukyハッカーに関連する攻撃を警告 | bleepingcomputer.com | 2024-07-11 | https://www.bleepingcomputer.com/news/security/japan-warns-of-attacks-linked-to-north-korean-kimsuky-hackers/ | osint-report | TLP:CLEAR | 中 |
| source--daily-dddef70e68c0dc59a5d3 | 北朝鮮系ハッカーが「ClickFix」を悪用し、暗号資産の偽求人でBeaverTailを配布 | thehackernews.com | 2025-09-22 | https://thehackernews.com/2025/09/dprk-hackers-use-clickfix-to-deliver.html | osint-report | TLP:CLEAR | 中 |
| source--daily-ec97ed0896afb842c91e | 北朝鮮マルウェアのモジュール化：多様性と機能特化 | dti.domaintools.com | 2026-04-06 | https://dti.domaintools.com/research/dprk-malware-modularity-diversity-and-functional-specialization | osint-report | TLP:CLEAR | 中 |
| source--daily-f05f4888998c8f53f5ca | Kimsukyの高度な攻撃手法：JSONPing、Webex偽装、新たなHttpSpy亜種 | enki.co.kr | 2026-05-30 | https://www.enki.co.kr/en/media-center/blog/kimsuky-s-advanced-attack-techniques-jsonping-webex-spoofing-and-a-new-httpspy-variant | osint-report | TLP:CLEAR | 中 |
| source--daily-f27405f22a33397d0072 | DPRK作戦の内情：LazarusとKimsukyの新インフラを世界的キャンペーンから特定 | hunt.io | 2025-12-18 | https://hunt.io/blog/dprk-lazarus-kimsuky-infrastructure-uncovered | osint-report | TLP:CLEAR | 中 |
| source--daily-f3e6fda98089cb5da96d | 2026年第1四半期 DPRK Operation Kimsuky 分析 | logpresso.com | 2026-05-20 | https://logpresso.com/ko/blog/2026-05-15-1Q-Kimsuky-report | osint-report | TLP:CLEAR | 中 |
| source--daily-f7383fd875d71ae63151 | Kimsuky、武器化QRコード経由で悪性モバイルアプリを配布し利用者を攻撃 | cybersecuritynews.com | 2025-12-18 | https://cybersecuritynews.com/kimsuky-hackers-attacking-users/ | osint-report | TLP:CLEAR | 中 |
| source--darkhorse-2023 | Operation DarkHorse CHM Attack Analysis | Genians | 2023-10-16 | kimsuky/20231016_threat_inteligence_report_DarkHorse.pdf | vendor-report | TLP:CLEAR | 中 |
| source--dmarc-2024 | North Korean Actors Exploit Weak DMARC Security Policies | FBI, DOS, NSA | 2024-05-02 | kimsuky/Exploit Weak DMARC.pdf | government-advisory | TLP:CLEAR | 高 |
| source--fbi-kimsuky-quishing-2026 | North Korean Kimsuky Actors Use Malicious QR Codes to Target Organizations | Federal Bureau of Investigation / IC3 | 2026-01-08 | https://www.ic3.gov/CSA/2026/260108.pdf | government-flash | TLP:CLEAR | 高 |
| source--joint-csa-2023 | North Korea Using Social Engineering to Enable Hacking of Think Tanks, Academia, and Media | FBI, DOS, NSA, NIS, NPA, MOFA | 2023-06-01 | kimsuky/Joint_CSA_NK_Using_Social_Engineering_20230531.pdf | government-advisory | TLP:CLEAR | 高 |
| source--kgh-2021 | Kimsuky New KGH Spyware Component Analysis | ThreatBook Labs | 2021-07 | kimsuky/Kimsuky-KGH.pdf | vendor-report | TLP:CLEAR | 中 |
| source--mandiant-apt43-2023 | APT43: North Korean Group Uses Cybercrime to Fund Espionage Operations | Mandiant | 2023-03-28 | https://cloud.google.com/blog/topics/threat-intelligence/apt43-north-korea-cybercrime-espionage/ | vendor-research | TLP:CLEAR | 高 |
| source--microsoft-actor-list | Microsoft Threat Actor List | Microsoft-derived repository data | 不明 | microsoft-threat-actor-list.xlsx | reference-table | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 不明 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--mitre-live-kimsuky-2026 | Kimsuky, Group G0094 | MITRE ATT&CK | 2026-04-23 | https://attack.mitre.org/groups/G0094/ | structured-knowledge-base | TLP:CLEAR | 高 |
| source--operation-newton | Operation Newton: Hi Kimsuky? | Virus Bulletin | 2021-10 | kimsuky/Operation_Newton_Kimsuky-APPLE(SEED).pdf | technical-report | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--qax-2024 | Cybersecurity Threats 2024 Annual Report | QAX | 2025 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | annual-report | TLP:CLEAR | 中 |
| source--rapid7-2024 | Kimsuky's Phishing and Payload Tactics | Rapid7 | 2024 | kimsuky/rapid7-Kimsukys-Phishing-and-Payload-Tactics_wp.pdf | vendor-report | TLP:CLEAR | 高 |
| source--smoke-screen | Analysis of the APT Campaign Smoke Screen | ESRC | 2019-04-17 | kimsuky/Smoke Screen.pdf | vendor-report | TLP:CLEAR | 高 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

未検証リークは中核評価に使用しない。IOCとartifactは観測イベント単位で別ファイルへ保存する。
