# Kimsuky 脅威アクタープロファイル

更新日: 2026-07-25  
対象期間: 少なくとも2012年 - 2025年  
分析基準: リポジトリ内資料のみ  
確度表現: 高 / 中 / 低  
配布区分: TLP:CLEAR相当（元資料の配布条件が優先）

## 1. エグゼクティブサマリー

Kimsukyは、北朝鮮（DPRK）の偵察総局（Reconnaissance General Bureau: RGB）に従属する国家支援型のサイバー諜報アクターである。2024年の米政府共同勧告は、より具体的にRGB傘下の第63研究センター（63rd Research Center）への行政的従属を記載している。主要任務は、北朝鮮の政策・外交・軍事・核開発上の意思決定に役立つ情報を窃取し、政権へ地政学的洞察を提供することである。[S01][S02]

最大の強みは、高度なゼロデイ開発そのものよりも、対象者を綿密に調査し、記者・研究者・政府関係者などを装い、複数回の自然な会話で信頼を築くソーシャルエンジニアリングにある。最終目的は、メール認証情報、メールボックス、非公開の研究・政策文書、連絡先、ブラウザ情報などへの継続的アクセスである。[S01][S03]

技術面では、HWP・Office文書、LNK、CHM、MSC、JavaScript、VBScript、PowerShell、悪性ブラウザ拡張、Androidアプリなどを組み合わせる。AppleSeed、AlphaSeed、BabyShark、KGH、FPSpy、KLogEXE、XenoRAT、TutorialRATなど、独自・改変・公開ツールを混在させる。インフラは、タイポスクワットドメイン、無料メール、VPS、侵害済みWebサーバ、無料TLS証明書、Google Drive・Dropbox・GitHub、メールサービス自体をC2に利用するなど、正規サービスと侵害資産を積極的に取り込む。[S03][S04][S05][S06]

## 2. 評価の要点

| 項目 | 評価 | 確度 |
|---|---|---|
| 帰属 | 北朝鮮RGB傘下。2024年共同勧告は第63研究センターへの行政的従属を記載 | 高 |
| 主目的 | 戦略・外交・安全保障・核政策に関する諜報、認証情報・メール窃取 | 高 |
| 活動開始 | 少なくとも2012年 | 高 |
| 中核能力 | 対象調査、ペルソナ構築、長期的な信頼醸成、スピアフィッシング | 高 |
| 技術的特徴 | 多様なスクリプト、悪性文書、公開RATと独自バックドアの併用 | 高 |
| 主標的 | 政府、外交、軍・防衛、シンクタンク、学術、メディア、核・研究分野 | 高 |
| 主対象地域 | 韓国が中心。米国、日本、ドイツを含む欧州、その他DPRK関心国へ拡大 | 高 |
| 金銭目的 | APT43という広い追跡集合には暗号資産関連活動の報告があるが、本プロファイルの中核は諜報 | 中 |
| 他DPRKアクターとの関係 | ツール・コード・インフラ・標的の重複、およびRGB内共有の可能性。組織的同一性は未確定 | 中 |
| 2025年の傾向 | 記者ペルソナ、ブラウザ中心の窃取、クラウド配布、XenoRAT/GitHub C2 | 中 |

## 3. 名前、別名、スコープ

### 3.1 中核名称

- 正規名: **Kimsuky**
- Kasperskyが2013年に公開した名称として広く定着。
- STIX上の主オブジェクト名もKimsukyとする。

### 3.2 高確度の別名

| 名称 | 主な追跡元 | 扱い |
|---|---|---|
| Emerald Sleet | Microsoft | 2024年米政府共同勧告がKimsuky活動集合として明記 |
| Thallium | Microsoft旧称 | Microsoftの対応表でEmerald Sleet、Kimsuky、Velvet Chollimaに対応 |
| Velvet Chollima | CrowdStrike | 共同勧告・複数総覧でKimsukyの別名として扱う |
| Black Banshee | PwC | 2023年共同勧告でKimsuky活動集合として扱う |
| APT43 | Mandiant | 共同勧告でKimsuky活動集合として扱う。ただしAPT43はより広い活動スコープを含み得る |

[S01][S02][S07][S08]

### 3.3 ベンダー固有クラスタ／関連名称

次の名称は資料によってKimsukyと同一または近接する活動として扱われるが、各ベンダーの観測範囲が一致するとは限らない。

- TA427 / Sparkling Pisces
- SharpTongue
- Springtail
- APT-Q-2
- PatheticSlug

これらは別名フィールドに含める一方、**完全な一対一対応を保証しない**。検知・インシデント対応では、名称ではなく観測されたTTP、インフラ、マルウェア、標的、時間軸を併用して判断する。[S03][S06][S09][S10]

### 3.4 混同しやすい名称

- **APT37 / ScarCruft / Group123**: 別アクターとして扱う。標的、誘引テーマ、BabyShark等のツール、インフラに重複報告があり、一部資料で誤ってThalliumがAPT37の別名に混入している。
- **Konni / TA406**: 別クラスタとして扱う。ペルソナ、資格情報窃取、Star/BabyShark関連コードや文字列などに重複がある。
- **Lazarus**: 別アクターとして扱う。PEBBLEDASH等のツール再利用・共有を示唆する資料があるが、同一組織を意味しない。

## 4. 帰属、組織、モチベーション

### 4.1 帰属

- 国家: 朝鮮民主主義人民共和国（北朝鮮、DPRK）
- 上位組織: 偵察総局（RGB）
- 下位位置づけ: 第63研究センターへの行政的従属（2024年米政府共同勧告）
- スポンサー種別: 国家支援
- 活動開始: 少なくとも2012年

確度は高い。米国・韓国の複数政府機関による共同勧告が、RGBへの従属と任務を明示している。[S01][S02]

### 4.2 主モチベーション

1. **戦略諜報**: 米国、韓国、その他関心国の政策・軍事・経済動向を把握する。
2. **外交・核政策情報の収集**: DPRKウォッチャー、外交官、研究者の未公開見解や研究を窃取する。
3. **メールと人的ネットワークの掌握**: 侵害メールを使って次の標的を発見し、信頼された人物として横展開する。
4. **防衛・科学技術情報の収集**: 防衛、航空宇宙、原子力、工学研究などを対象とする。
5. **限定的な資金獲得**: APT43という広いスコープでは暗号資産関連の資金獲得が報告されるが、Kimsukyの一貫した中心任務は諜報である。

### 4.3 インテリジェンス要求の推定

- 米韓の対北朝鮮政策
- 非核化、核戦略、ミサイル、防衛政策
- 米中韓日露の外交関係
- 制裁・国際関係
- 北朝鮮に関する世論、専門家分析、報道予定
- 防衛技術、航空宇宙、原子力、科学技術研究

## 5. 他アクターとの関係

| 相手 | 観測された関係 | 評価 | 確度 |
|---|---|---|---|
| RGB / 第63研究センター | 指揮・行政的従属 | 組織上の上位関係 | 高 |
| APT37 / ScarCruft | 標的、誘引、マルウェア、インフラの重複。DarkHorseではAPT37説よりKimsuky類似性を評価 | 別アクターだが境界が曖昧な活動あり | 中 |
| Konni / TA406 | Star、BabyShark、AppleSeed周辺の文字列、ペルソナ、資格情報窃取に重複 | ツール・開発・運用知識の共有可能性 | 中 |
| Lazarus | PEBBLEDASH等の再利用、コード・構成の類似 | DPRK内部のツール共有または開発者再配置の可能性 | 中 |
| その他DPRKサイバー部隊 | 盗取データを他の北朝鮮アクターが高価値標的への攻撃に利用し得る | 情報・アクセスの共有 | 中 - 高 |

注意: 共通ツールやインフラは、同一組織の証明ではない。DPRK内でのリソース共有、開発者移動、同じ公開コードの利用、第三者インフラの再利用でも説明できる。[S01][S11][S12][S13]

## 6. ダイヤモンドモデル

### 6.1 Adversary

- 北朝鮮国家支援型、RGB傘下
- 高度なペルソナ構築・標的調査
- 多数の並行フィッシング活動を運用
- 検知回避より、アクセスの再確立と運用量を優先する傾向
- 独自開発、公開ツール改変、正規サービス悪用を組み合わせる

### 6.2 Capability

- OSINTによる対象選定と関係性調査
- 記者、学者、研究者、政府関係者、組織内連絡先のなりすまし
- 信頼構築型スピアフィッシング
- 資格情報フィッシング、AiTM型プロキシ、メール自動転送
- HWP/Office、LNK、CHM、MSC、悪性ブラウザ拡張、Androidアプリ
- PowerShell、JavaScript/JScript、VBScript、BAT
- 独自バックドア、キーロガー、情報窃取、公開RAT、遠隔管理ソフト
- RDP、Webシェル、侵害済みサーバを用いた持続性と中継

### 6.3 Infrastructure

- 正規サービスに似たタイポスクワットドメイン
- 攻撃者登録の無料メールアカウント
- VPSと一般ホスティング
- 侵害したWebサーバ／国内外の踏み台
- 無料TLS証明書（主にLet's Encrypt）
- Google Drive、Dropbox、OneDrive、GitHub
- Naver/Daum等のメールをC2として使用
- 類似パス（`/downX/`、`/uploadX/`）とIP再利用
- PHPフィッシングキット、プロキシページ、Green Dinosaur / Webadmin Webシェル

### 6.4 Victim

- 政府・外交・議会
- 軍・防衛・国家安全保障
- シンクタンク、学術、大学、研究機関
- 記者、報道機関、DPRKウォッチャー
- 原子力、航空宇宙、科学・工学
- 金融、保険、暗号資産
- 医療、製薬、エネルギー
- 韓国を中心に、米国、日本、ドイツを含む欧州、中国ほか

### 6.5 Social-political meta-features

- 北朝鮮核・ミサイル、米韓関係、ウクライナ戦争、対中・対露関係など時事性の高い話題
- アンケート、取材依頼、論文執筆依頼、会議招待、履歴書・文書レビュー
- 正当な過去メール、署名、連絡先を再利用
- 初回は無害なメールを送り、2 - 3日以内に追跡連絡
- 支払いや謝礼、締切、パスワード付きアーカイブで心理的圧力と検知回避を両立

## 7. Capability詳細

### 7.1 ソーシャルエンジニアリング／フィッシング

典型的な攻撃チェーン:

1. OSINTで政策専門家、研究者、記者、組織内関係者を調査。
2. 実在人物に似たメールアドレス、ドメイン、オンラインペルソナを準備。
3. 無害な取材・アンケート・会議依頼で接触し、複数回会話。
4. 信頼成立後、資格情報フィッシングURL、悪性文書、パスワード付きRAR等を送付。
5. 資格情報やメールを窃取し、メール自動転送やブラウザ拡張で継続監視。
6. 侵害したアカウント、署名、過去メールを用いて次の標的へ横展開。
7. 必要に応じマルウェアを導入し、情報収集、画面・キー入力取得、遠隔操作、流出を実施。

### 7.2 マルウェア／ツール

| 名称 | 種別 | 主機能・特徴 | 確度 |
|---|---|---|---|
| AppleSeed | 独自バックドア | コマンド実行、情報窃取、アップロード／ダウンロード、キー入力・画面取得、二重XOR、PDFヘッダ偽装、メールC2の亜種 | 高 |
| AlphaSeed | Go製バックドア | AppleSeed類似。NaverメールとChrome DevTools Protocol、CookieをC2認証に利用 | 高 |
| BabyShark | VBScript系マルウェア | マクロ起点の初期活動、継続アクセス、メール関連活動。複数亜種 | 高 |
| KGH Spyware | 情報窃取／遠隔操作 | ブラウザ、メールクライアント、資格情報、WinSCP等を収集。FTP C2、持続性、遠隔コマンド | 高 |
| KLogEXE | キーロガー | キー入力収集。FPSpyと共に2024年活動で報告 | 中 - 高 |
| FPSpy | バックドア | 情報収集・遠隔操作。2024年にKLogEXEと共に報告 | 中 - 高 |
| XenoRAT | 公開.NET RAT | 2025年、クラウド配布とGitHub C2を伴う活動で報告 | 中 |
| TutorialRAT | 公開.NET RAT | 情報・資格情報窃取を備えたRAT。軽微な改変で使用 | 中 - 高 |
| XeroRAT | .NET RAT | PowerShellからメモリ内ロードされた例 | 中 - 高 |
| PEBBLEDASH | バックドア | 従来Lazarus帰属のツールとKimsuky活動の重複。DPRK内共有の可能性 | 中 |
| httpSpy | バックドア | Kimsukyの複数クラスタで言及 | 中 |
| FastViewer / FastSpy / FastFire | Androidマルウェア | Google Playの同期／開発者機能を悪用して配布 | 高 |
| Quasar RAT | 公開RAT | 侵害端末の継続アクセス | 高 |
| Ammyy Admin / AnyDesk / TeamViewer | 正規遠隔管理 | アクセス継続、手動操作 | 高 |
| RDP Wrapper | 正規／公開ツール | 複数RDPセッション、継続アクセス | 高 |
| Meterpreter / Metasploit | 公開攻撃フレームワーク | Operation Newtonでサーバアクセス・ペイロード実行 | 高 |
| Green Dinosaur | Webシェル | C2管理、ファイル操作、侵害サイト上の運用 | 高 |
| Webadmin | Webシェル | C2管理、ファイル操作 | 高 |
| Mail Sending Program ver10.0 | フィッシング運用ツール | 送信元、宛先、件名、リンク等を設定し大規模化 | 高 |
| espoofer改変版 | メール偽装ツール | Naver/Google等を装う送信元詐称 | 高 |

### 7.3 配送・実行形式

- HWP / DOC / DOCX / RTF（マクロ、脆弱性、誘引文書）
- LNK（ダブル拡張子、HWP等のアイコン、埋め込み／ダウンロード型）
- CHM（HTML、JSE、VBSの自動実行）
- MSC（Microsoft Management Consoleの自動実行機能）
- RAR / ZIP（パスワード保護、メール検査回避）
- JavaScript / JScript / VBScript / PowerShell / BAT
- Chromium拡張
- Android APK

### 7.4 インフラ運用

| 構成 | 利用目的 |
|---|---|
| タイポスクワット／類似ドメイン | Naver、Kakao、Google、Yahoo、報道機関等を偽装 |
| 侵害Webサーバ | フィッシング、ペイロード配布、C2、Webシェル |
| VPS／ホスティング | C2、ステージング、スキャン、攻撃管理 |
| Google Drive / Dropbox / OneDrive | 正規サービスの評判を利用したペイロード配布 |
| GitHub | ペイロード／XenoRATの隠密C2 |
| Naver / Daumメール | AppleSeed／AlphaSeed系C2 |
| 無料TLS | 短期間のフィッシングサイトをHTTPS化 |
| RDP侵害端末 | フィッシングメール送信、踏み台、ツール保管 |
| PHPプロキシ／Webシェル | 資格情報窃取、C2運用、流出データ保管 |

公開IoCは時間劣化が速いため、STIX試作版では代表的かつ資料で明示されたものだけを収録し、ドメイン名の類似性やホスティング事業者だけでブロックしない。

## 8. MITRE ATT&CK対応

| ID | Technique | Kimsukyでの観測 |
|---|---|---|
| T1589 | Gather Victim Identity Information | 専門家、記者、研究者、連絡先をOSINT調査 |
| T1585.001 | Establish Accounts: Social Media Accounts | 偽ペルソナ、SNS・メールアカウント |
| T1583.001 | Acquire Infrastructure: Domains | 類似・タイポスクワットドメイン |
| T1584.004 | Compromise Infrastructure: Server | 侵害Webサーバをフィッシング／C2に利用 |
| T1566.001 | Phishing: Spearphishing Attachment | HWP、Office、LNK、CHM、MSC、アーカイブ |
| T1566.002 | Phishing: Spearphishing Link | 資格情報窃取、クラウド配布リンク |
| T1204.001 | User Execution: Malicious Link | リンククリックを誘導 |
| T1204.002 | User Execution: Malicious File | 誘引文書・ショートカット実行 |
| T1059.001 | PowerShell | ダウンロード、復号、メモリ内実行、収集 |
| T1059.005 | Visual Basic | VBScriptによる初期実行・収集 |
| T1059.007 | JavaScript/JScript | CHM/LNK後段、AppleSeed配送 |
| T1218.010 | Regsvr32 | AppleSeed DLL実行 |
| T1218.011 | Rundll32 | DLLのプロキシ実行 |
| T1053.005 | Scheduled Task/Job | 定期実行と持続性 |
| T1547.001 | Registry Run Keys / Startup Folder | AppleSeed等の持続性 |
| T1219 | Remote Access Software | AnyDesk、TeamViewer、Ammyy、Quasar |
| T1021.001 | Remote Services: RDP | 侵害端末操作と横展開 |
| T1190 | Exploit Public-Facing Application | Webサーバ侵害 |
| T1505.003 | Server Software Component: Web Shell | Green Dinosaur、Webadmin |
| T1027 | Obfuscated/Compressed Files and Information | PowerShell難読化、二重Base64、パスワード付きRAR |
| T1105 | Ingress Tool Transfer | C2／クラウドから後段を取得 |
| T1071.001 | Application Layer Protocol: Web Protocols | HTTP/HTTPS C2 |
| T1071.003 | Application Layer Protocol: Mail Protocols | メールサービスをC2として利用 |
| T1114 | Email Collection | メール内容・メールボックス窃取 |
| T1114.003 | Email Forwarding Rule | 侵害メールの自動転送 |
| T1056.003 | Input Capture: Web Portal Capture | 偽ログインページ、AiTM／プロキシ |
| T1056.001 | Input Capture: Keylogging | AppleSeed、KLogEXE、PowerShellキーロガー |
| T1113 | Screen Capture | AppleSeed、ブラウザ中心の窃取 |
| T1057 | Process Discovery | tasklist等によるプロセス収集 |
| T1082 | System Information Discovery | ホスト情報、環境情報の収集 |
| T1074.001 | Data Staged: Local Data Staging | `%TEMP%`、`%APPDATA%`等で収集・中継 |
| T1041 | Exfiltration Over C2 Channel | HTTP、FTP、メールC2による流出 |
| T1070.001 | Indicator Removal: Clear Windows Event Logs | RDP・イベントログ削除 |

マッピングは資料の動作記述に基づく分析マッピングであり、元資料が常にATT&CK IDを明記しているわけではない。

## 9. 攻撃活動の履歴

| 時期 | 活動／変化 | 評価 |
|---|---|---|
| 2012 - | RGB目的を支援する広範な諜報活動を開始 | 共同勧告が「少なくとも2012年」と評価 |
| 2013 | KasperskyがKimsukyとして公表 | 名称の一般化 |
| 2014 | 韓国水力原子力（KHNP）関連攻撃との関連が後年資料で指摘 | 帰属には分析差あり |
| 2018 - 2019 | BabyShark、KimJongRAT、PCRat、Baby系キャンペーン | マクロ、VBScript、資格情報・情報窃取 |
| 2019-03 - 04 | Operation Low Kick、Stealth Power、Smoke Screen、Giant Baby | HWP/DOC、HTA、PowerShellキーロガー、韓米のDPRK関係者 |
| 2019-05 | AppleSeedの初期版を観測 | 独自バックドアの長期運用開始 |
| 2020 | 新型コロナ等の時事誘引、米韓政府のKimsuky注意喚起 | ソーシャルエンジニアリングを継続 |
| 2020 - 2021 | Operation Newton | 工学研究者、メール資格情報、Webシェル、AppleSeed、Meterpreter、Linux/Windows横展開 |
| 2021 | KGH Spyware新版 | CVE-2019-0880、FTP C2、ブラウザ・メール・資格情報窃取 |
| 2022-02 - | DarkHorse系CHM活動が開始 | VBSからJSEへ変化、暗号資産・金融・保険テーマ |
| 2022-04 - 2023-09 | Operation Covert Stalker観測期間 | RDP侵害、フィッシング運用、Webシェル、遠隔管理、AppleSeed |
| 2022 | Android向けAppleSeed／モバイルマルウェア | SMS等のモバイル情報を収集 |
| 2023-03 | Chromium拡張とGoogle Play同期機能の悪用をBfV/NISが公表 | Gmail窃取、Androidアプリの限定配布 |
| 2023-06 | 米韓共同勧告が記者・学者・シンクタンクへの長期信頼構築型攻撃を詳述 | 戦略諜報が中心 |
| 2023 | AlphaSeed等のGo系能力を観測 | メール／DevToolsをC2に利用 |
| 2023-10 | Operation DarkHorse報告 | CHM/JSE、金融・保険を装う攻撃 |
| 2023-11 | Operation Covert Stalker報告 | 17か月のフィッシング・マルウェア・C2運用を整理 |
| 2023末 - 2024初 | 弱いDMARC設定を悪用した送信元偽装 | 記者・研究者を装い政策専門家を標的 |
| 2024 | 日本組織、韓国大学、ドイツ防衛関連への活動が報告 | 地域・業種の拡大 |
| 2024 | MSC、KLogEXE、FPSpy、RDP Wrapper、PEBBLEDASHを含む活動 | 配送形式とツールを更新 |
| 2025 | PatheticSlugとして記者ペルソナ、悪性ブラウザ拡張、クラウド配布、XenoRAT/GitHub C2が報告 | 最新総覧に基づくため確度は中 |

## 10. ターゲット

### 10.1 国・地域

| 優先度 | 国・地域 | 根拠・特徴 |
|---|---|---|
| 最重要 | 韓国 | 政府、議会、外交、軍、防衛、大学、研究、メディア、ポータル利用者 |
| 高 | 米国 | 政府関係者、政策専門家、シンクタンク、学術、メディア |
| 高 | 日本 | 2024年に標的拡大が報告、DPRK政策・組織 |
| 高 | ドイツ | 2023年共同勧告、2024年防衛関連報告 |
| 中 | 欧州各国 | 外交、安全保障、研究機関 |
| 中 | 中国 | 在中韓国大使館等の誘引、地域政策 |
| 中 | ロシア | KGH等で関連標的が示唆 |
| 中 | その他 | DPRKの外交・軍事・制裁上の関心国 |

### 10.2 産業・役割

1. 政府、外交、議会、公共部門
2. 軍、国家安全保障、防衛産業
3. シンクタンク、政策研究
4. 大学、学術、科学・工学研究
5. メディア、記者、放送関係者
6. 原子力、エネルギー
7. 航空宇宙
8. 金融、保険、暗号資産
9. 医療、製薬
10. DPRK関連のNGO、人権活動、退職専門家、社会的ネットワーク

### 10.3 標的選定ロジック

組織の規模よりも、**北朝鮮に関する非公開情報や信頼ネットワークへのアクセスを持つ個人**が重要である。職場メールだけでなく個人メール、退職者、学会・社会クラブ、連絡先リストも狙われる。

## 11. 分析上の不確実性

1. ベンダーごとにクラスタの粒度が異なり、APT43、TA427、SharpTongue等は完全一致しない可能性がある。
2. APT37、Konni、Lazarusとのコード・インフラ重複は、同一組織ではなく共有・再配置・再利用で説明できる。
3. DarkHorseのKimsuky帰属は、類似性に基づく推定であり、報告内でもAPT37説との競合が示される。
4. 2025年のPatheticSlug活動は単一の年次総覧に依存するため確度を中とした。
5. `APTDown`資料は第三者が取得したと主張するリークで、真正性・完全性・改変有無を独立検証できない。中核評価には使用せず、補助的な調査候補に限定した。
6. IOCは短命であり、過去のドメイン・IP・ハッシュへの一致が現在の活動や帰属を自動的に証明しない。

## 12. 収集・分析方法

- `.git`を除くリポジトリ内1,007ファイルを棚卸し。
- 681 PDF、5 Excel、README、CSV、JSON、STIX、テキストを対象に名称・別名・主要マルウェア語で全文検索。
- Kimsuky関連候補109ファイルを抽出。
- Kimsuky直下のPDF、Excel、READMEを全件テキスト化。
- 政府共同勧告、技術報告、年次総覧、索引を相互照合。
- 感染済みアーカイブ、DLL、PHP、PoC、サンプルは展開・実行していない。
- 画像主体のPDFでは抽出テキストが空または限定的な場合があるため、別資料との相互確認を行った。

## 13. 主要出典

| ID | 資料 | 利用箇所 |
|---|---|---|
| S01 | `kimsuky/Joint_CSA_NK_Using_Social_Engineering_20230531.pdf`（特にpp.1-6） | 帰属、任務、別名、標的、ソーシャルエンジニアリング |
| S02 | `kimsuky/Exploit Weak DMARC.pdf`（特にpp.1-4） | 第63研究センター、Emerald Sleet、DMARC悪用 |
| S03 | `kimsuky/rapid7-Kimsukys-Phishing-and-Payload-Tactics_wp.pdf`（pp.3-16） | 配送、マルウェア、インフラ、標的 |
| S04 | `kimsuky/Operation_Newton_Kimsuky-APPLE(SEED).pdf`（pp.2-25） | AppleSeed、Operation Newton、C2、標的、横展開 |
| S05 | `kimsuky/20231101_Kimsuky_OP.-Covert-Stalker-EN.pdf`（pp.4-89） | RDP、C2、Webシェル、運用ツール |
| S06 | `summary/2026/Cloudflare-2026-threat-report.pdf`（pp.26付近） | 2025年PatheticSlug、XenoRAT、GitHub C2 |
| S07 | `microsoft-threat-actor-list.xlsx` | Thallium / Emerald Sleet / Kimsuky対応 |
| S08 | `Threat_Group_Cards_v2.0.pdf`（Kimsuky項） | Velvet Chollima、Thallium、Black Banshee、動機 |
| S09 | `summary/2025/2024 Threat Intelligence Annual Report.pdf` | APT-Q-2、Sparkling Pisces、対象業種 |
| S10 | `summary/2025/2025-dbir-data-breach-investigations-report.pdf` | Sparkling Pisces、KLogEXE、FPSpy |
| S11 | `International Strategic/Korea/ Blurred-Lines-of-Cyber-Threat-Attribution.pdf` | DPRK内ツール共有、PEBBLEDASH、帰属境界 |
| S12 | `konni/konni-threat-insight-paper-triple-threat-N-Korea-aligned-TA406-steals-scams-spies.pdf` | TA406/TA427、Star、BabySharkの重複 |
| S13 | `kimsuky/20231016_threat_inteligence_report_DarkHorse.pdf` | APT37との帰属競合、CHM/JSE活動 |
| S14 | `kimsuky/Kimsuky-KGH.pdf` | KGH、FTP C2、情報窃取、CVE-2019-0880 |
| S15 | `kimsuky/kimsuky-2023-03-20-joint-cyber-security-advisory.pdf` | Chromium拡張、Google Play同期悪用 |
| S16 | `kimsuky/Smoke Screen.pdf` | 2019年Smoke Screen、Stealth Power、HWP、PowerShell |
| S17 | `baby-kimsuky/BabyShark Rule - Mal Cert and others.xlsx` | BabyShark関連ハッシュ・分類 |
| S18 | `summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf` | 2024年の国・業種・マルウェア変化 |

## 14. STIX表現方針

付属の`kimsuky-profile.stix2.json`はSTIX 2.1 Bundleで、次を収録する。

- Intrusion Set: Kimsuky
- Identity: DPRK RGB、第63研究センター、標的組織カテゴリ
- Malware: 主要マルウェア／RAT
- Tool: 公開ツール、遠隔管理、フィッシング運用ツール
- Infrastructure: 代表的なインフラ類型
- Attack Pattern: 主要ATT&CK技法
- Campaign: 主要活動履歴
- Relationships: uses、targets、attributed-to、part-of、related-to
- Indicators: 資料で明示された代表例
- Report: 本プロファイルを束ねるSTIX Report

STIXでは別名を`aliases`に保持するが、ベンダークラスタのスコープ差は`description`と`note`で明示する。
