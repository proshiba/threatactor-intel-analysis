# Scattered Spider 脅威アクタープロファイル

- プロファイルID: `actor--scattered-spider`
- 状態: draft
- 更新日時: 2026-07-27T11:17:25Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Scattered Spiderの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Scattered Spider**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Octo Tempest | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Roasted 0ktapus | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Storm-0875 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| UNC3944 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

## 帰属

未評価

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: なし

## モチベーション

未評価

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Scattered Spider](https://attack.mitre.org/groups/G1015) is a native English-speaking cybercriminal group active since at least 2022. (Citation: CrowdStrike Scattered Spider Profile) (Citation: MSTIC Octo Tempest Operations October 2023) The group initially targeted customer relationship management (CRM) providers, business process outsourcing (BPO) firms, and telecommunications and technology companies before expanding in 2023 to gaming, hospitality, retail, managed service provider (MSP), manufacturing, and financial sectors. (Citation: MSTIC Octo Tempest Operations October 2023)<br>[Scattered Spider](https://attack.mitre.org/groups/G1015) relies heavily on social engineering, including impersonating IT and help-desk staff, to gain initial access, bypass multi-factor authentication (MFA), and compromise enterprise networks. The group has adapted its tooling to evade endpoint detection and response (EDR) defenses and used ransomware for financial gain. (Citation: CISA Scattered Spider Advisory November 2023) (Citation: CrowdStrike Scattered Spider BYOVD January 2023) (Citation: Crowdstrike TELCO BPO Campaign December 2022)<br>[Scattered Spider](https://attack.mitre.org/groups/G1015) had expanded into hybrid cloud and identity environments, using help-desk impersonation and MFA bypass to obtain administrator access in Okta, AWS, and Office 365. (Citation: Mandiant UNC3944 May 2025) |
| Capability | BlackCat, Raccoon Stealer, WarzoneRAT, Linpeas, ngrok, Rclone, ConnectWise, Mimikatz, LaZagne, Tor |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Scattered Spider | canonical-name | 高 |  | https://www.mandiant.com/resources/blog/unc3944-sms-phishing-sim-swapping-ransomware<br>https://unit42.paloaltonetworks.com/muddled-libra/<br>https://thehackernews.com/2023/10/lucr-3-scattered-spider-getting-saas-y.html |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Octo Tempest | canonical-name | 高 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Scattered Spider | canonical-name | 高 |  | https://www.cybersecurity-insiders.com/scattered-spider-managed-mgm-resort-network-outage-brings-8m-loss-daily/<br>https://www.loginradius.com/blog/identity/oktapus-phishing-targets-okta-identity-credentials/<br>https://www.attackiq.com/2023/11/21/attack-graph-response-to-cisa-advisory-aa23-320a/ |
| misp-microsoft-activity-group | Octo Tempest | canonical-name | 高 |  | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Scattered Spider - G1015 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1015<br>https://cloud.google.com/blog/topics/threat-intelligence/defending-vsphere-from-unc3944<br>https://cloud.google.com/blog/topics/threat-intelligence/unc3944-proactive-hardening-recommendations |
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
| malware--blackcat | BlackCat | [BlackCat](https://attack.mitre.org/software/S1068) is ransomware written in Rust that has been offered via the Ransomware-as-a-Service (RaaS) model. First observed November 2021, [BlackCat](https://attack.mitre.org/software/S1068) has been used to target multiple sectors and organizations in various countries and regions in Africa, the Americas, Asia, Australia, and Europe.(Citation: Microsoft BlackCat Jun 2022)(Citation: Sophos BlackCat Jul 2022)(Citation: ACSC BlackCat Apr 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--linpeas | Linpeas | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--raccoon-stealer | Raccoon Stealer | [Raccoon Stealer](https://attack.mitre.org/software/S1148) is an information stealer malware family active since at least 2019 as a malware-as-a-service offering sold in underground forums. [Raccoon Stealer](https://attack.mitre.org/software/S1148) has experienced two periods of activity across two variants, from 2019 to March 2022, then resurfacing in a revised version in June 2022.(Citation: S2W Racoon 2022)(Citation: Sekoia Raccoon1 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--warzonerat | WarzoneRAT | [WarzoneRAT](https://attack.mitre.org/software/S0670) is a malware-as-a-service remote access tool (RAT) written in C++ that has been publicly available for purchase since at least late 2018.(Citation: Check Point Warzone Feb 2020)(Citation: Uptycs Warzone UAC Bypass November 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--ngrok | ngrok | [ngrok](https://attack.mitre.org/software/S0508) is a legitimate reverse proxy tool that can create a secure tunnel to servers located behind firewalls or on local machines that do not have a public IP. [ngrok](https://attack.mitre.org/software/S0508) has been leveraged by threat actors in several campaigns including use for lateral movement and data exfiltration.(Citation: Zdnet Ngrok September 2018)(Citation: FireEye Maze May 2020)(Citation: Cyware Ngrok May 2019)(Citation: MalwareBytes LazyScripter Feb 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--rclone | Rclone | [Rclone](https://attack.mitre.org/software/S1040) is a command line program for syncing files with cloud storage services such as Dropbox, Google Drive, Amazon S3, and MEGA. [Rclone](https://attack.mitre.org/software/S1040) has been used in a number of ransomware campaigns, including those associated with the [Conti](https://attack.mitre.org/software/S0575) and DarkSide Ransomware-as-a-Service operations.(Citation: Rclone)(Citation: Rclone Wars)(Citation: Detecting Rclone)(Citation: DarkSide Ransomware Gang)(Citation: DFIR Conti Bazar Nov 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--connectwise | ConnectWise | [ConnectWise](https://attack.mitre.org/software/S0591) is a legitimate remote administration tool that has been used since at least 2016 by threat actors including [MuddyWater](https://attack.mitre.org/groups/G0069) and [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) to connect to and conduct lateral movement in target environments.(Citation: Anomali Static Kitten February 2021)(Citation: Trend Micro Muddy Water March 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--lazagne | LaZagne | [LaZagne](https://attack.mitre.org/software/S0349) is a post-exploitation, open-source tool used to recover stored passwords on a system. It has modules for Windows, Linux, and OSX, but is mainly focused on Windows systems. [LaZagne](https://attack.mitre.org/software/S0349) is publicly available on GitHub.(Citation: GitHub LaZagne Dec 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--tor | Tor | [Tor](https://attack.mitre.org/software/S0183) is a software suite and network that provides increased anonymity on the Internet. It creates a multi-hop proxy network and utilizes multilayer encryption to protect both the message and routing information. [Tor](https://attack.mitre.org/software/S0183) utilizes "Onion Routing," in which messages are encrypted with multiple layers of encryption; at each step in the proxy network, the topmost layer is decrypted and the contents forwarded on to the next node until it reaches its destination. (Citation: Dingledine Tor The Second-Generation Onion Router) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### インフラ

未確認

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|
| Marks & Spencerの侵害、Scattered Spiderランサムウェア攻撃に関連 | ransomware-extortion | 不明 | 不明 | 2025-04-29 | 英国小売大手Marks & SpencerがScattered Spiderによるランサムウェア攻撃を受けた。 攻撃者は2月にNTDS.ditファイルを盗み、資格情報を取得。 4月24日にDragonForceランサムウェアでVMware ESXi仮想マシンを暗号化。 CrowdStrike、Microsoft、Fenix24がインシデント対応に協力。 攻撃者グループは若年層で構成され、ソーシャルエンジニアリングに長けている。 | 高 | `source--daily-0d8b0cd3a78d874f7394` |
| 暑かったのは気温だけではない——2025年夏にサイバー攻撃が急増 | ransomware-extortion | 不明 | 不明 | 2025-08-06 | 2025年夏、医療・小売・保険・政府など多業種でサイバー攻撃が急増 Interlock・Rhysida・Qilinらが病院を標的にランサムやデータ漏えいを実行 Scattered Spiderは小売から米保険業へ戦術を変え、音声フィッシングを多用 SharePoint RCE(CVE-2025-53770等)やFortinet脆弱性連鎖を悪用した侵入が顕著 国家・ハクティビストも暗躍し、組織はパッチ適用・ID保護・攻撃シミュレーションが必須 | 中 | `source--daily-1f9abeeb494497e6757c` |
| Scattered SpiderがVMware ESXiを狙ったハッキングを拡大 | ransomware-extortion | 不明 | 不明 | 2025-07-28 | Scattered Spiderが米国の小売・航空などでVMware ESXiハイパーバイザーを集中的に攻撃 初期アクセスはヘルプデスクへのなりすまし電話でADパスワードを変更させ侵入 権限奪取後、vCenter経由でESXiにSSHを有効化しroot再設定、ディスクスワップでNTDS.ditを窃取 バックアップを削除しVMデータストアにランサムウェアを展開、数時間で全環境を制圧可能 GoogleはMFA徹底・SSH無効化・SIEM監視・immutableバックアップなどでの防御を推奨 | 高 | `source--daily-d395324d918e79d06dc6` |
| Aflac、散発するScattered Spiderによる保険会社攻撃の中で侵害を公表 | ransomware-extortion | 不明 | 不明 | 2025-06-21 | 2025年6月20日、米保険大手Aflacがシステム侵害を公表、顧客の個人情報や健康情報が窃取された可能性 ランサムウェア被害は確認されず、データ窃取攻撃の可能性が示唆される 数時間で侵害を検知・封じ込めし、事業継続性は維持されたと発表 外部セキュリティ専門家を招聘し、SEC提出資料で契約者・社員らの請求情報やSSNなど機微情報流出を報告 攻撃はソーシャルエンジニアリングに長けた「Scattered Spider」グループの手口と類似 | 高 | `source--daily-f9d510457677ce905d57` |
| 英国政府、サイバー攻撃後のJLRに15億ポンドのローン保証を実施 | ransomware-extortion | 不明 | 不明 | 2025-09-30 | 大規模サイバー攻撃で生産停止に陥ったJLR支援のため、英国政府が15億ポンドのローン保証を決定。 保証はUK Export FinanceのEDG枠で実施、直接融資ではなく民間融資を政府が保証、返済期間は5年。 攻撃は今月公表され、ITと製造に深刻な障害を引き起こし、複数工場の停止とデータ窃取をJLRが確認。 「Scattered Lapsus$ Hunters」が犯行を主張し、SAPのHOSTSファイル画像を掲示、ランサム展開を示唆。 JLRは段階的再開を近日開始予定で、NCSCや法執行・専門家と連携。保険未締結の報道もあり。 | 中 | `source--daily-04302db7cea311067bd3` |
| Harrods、英国小売業界を狙ったサイバー攻撃の次なる標的に | ransomware-extortion | 不明 | 不明 | 2025-05-02 | 英国の高級百貨店Harrodsがサイバー攻撃の標的となり、同国の小売業界で3件目の被害事例となった。 Harrodsは不正アクセスの試みを受け、即座にインターネットアクセスを制限するなどの対策を講じた。 同社の店舗およびオンラインショップは通常通り営業を継続しており、顧客への影響は報告されていない。 先週には、Marks & Spencer（M&S）とCo-opも同様のサイバー攻撃を受けており、M&Sではオンライン注文の停止などの被害が発生している。 M&Sの攻撃は、ランサムウェア「DragonForce」を用いた「Scattered Spider」グループによるものとされている。 | 中 | `source--daily-087eb7c60fcfe537fd54` |
| サービスデスクが攻撃の標的に：私たちにできる対策は？ | reported-activity | 不明 | 不明 | 2025-05-21 | サービスデスクがソーシャルエンジニアリング攻撃の標的となり、攻撃者が従業員を装って認証情報を取得。 2025年4月～5月にかけて、Marks & Spencer、Co-Op Group、Harrods、Diorなどが被害を受けた。 攻撃者は、Scattered Spiderとされる米英拠点のサイバー犯罪グループ。 攻撃手法は、緊急性や信頼を装い、サービスデスク担当者にパスワードリセットやMFA無効化を依頼。 一部企業では、オンラインサービスの停止や顧客データの漏洩が発生。 | 中 | `source--daily-4e50a94f394205333edf` |
| DragonForceランサムとScattered Spiderの関係を深掘り | ransomware-extortion | 不明 | 不明 | 2025-12-04 | 2023年登場のDragonForceは2025年に「カルテル」へ進化し、脆弱ドライバ悪用と暗号化改良で攻撃を加速。 truesight.sysやrentdrv2.sysなどの脆弱なドライバを悪用して防御停止・保護プロセスを終了させるBYOVD攻撃、また過去の暗号化欠陥を修正したと分析。 最大級の侵害はMarks & Spencer事案で、初期侵入はソーシャルエンジニアリングに長けたScattered Spiderが担ったとされる。 同集団はOSINT、MFA疲労・SIMスワップ、端末登録、RMM( ScreenConnect等 )、AWS SSM Inventory、MEGA/S3への流出を使用。 対策要点はフィッシング耐性MFAの徹底と、RMM導入や脆弱ドライバ読込を検知できるEDRの運用強化。 | 高 | `source--daily-bc6f4aecde8159d70fd7` |
| Scattered Spiderのハッカー、航空および輸送企業への標的をシフト | intrusion | 不明 | 不明 | 2025-06-28 | Scattered Spiderが保険・小売セクターから航空・輸送業界へ標的を拡大。 6月12日、カナダのWestJetが内部サービスとモバイルアプリを一時的に停止。 攻撃者はセルフサービスポスワードリセットでMFA登録後、Citrix経由で侵入。 Hawaiian Airlinesもサイバー攻撃を公表、同一勢力の可能性が示唆。 MandiantとPalo Altoが対応支援、ヘルプデスク認証強化を推奨。 | 高 | `source--daily-21728e38bdfb2401ffa0` |
| Scattered Spiderハッカー、クラウドアプリに焦点をシフトしてデータ窃盗を行う | phishing-campaign | 不明 | 不明 | 2024-06-15 | Scattered SpiderはクラウドアプリやSaaSを標的にしてデータを盗み、仮想マシンを新たに作成して持続性を確保。 Scattered Spiderは、通常はSMSフィッシング、SIMスワッピング、アカウントハイジャックを使用するソーシャルエンジニアリング攻撃を行ってきた。 Mandiantが分析した結果、TTPがクラウドとSaaSに拡大しており、データを窃取して脅迫を行っていると指摘。 最初のアクセスは、ヘルプデスクのエージェントをターゲットにして、ソーシャルエンジニアリング攻撃を行う。正当な個人を装うため、事前に個人情報、役職、およびマネージャー名などを準備。 ソーシャルエンジニアリングでMFAのリセットをさせて被害者の環境にアクセス。侵害したアカウントに紐づいていたOktaを利用して企業のクラウドやSaaSアプリにさらにアクセスを広げた事例があった。 Windows Defenderなどのセキュリティを無効化し、IMPACKETなどの横展開ツールやNGROKなどのトンネリングツールをデプロイ。 | 高 | `source--daily-c18481a1b5cdd9fcdd92` |
| Google、データ侵害でGoogle広告の見込み顧客情報が露出したと確認 | ransomware-extortion | 不明 | 不明 | 2025-08-11 | GoogleはSalesforceの企業CRM侵害がGoogle広告の見込み顧客情報に及んだと認めた。 露出は企業名・電話番号・営業メモ等で、支払い情報やAds製品データの影響はなし。 攻撃はShinyHunters（Scattered Spiderと重なることを示すため現在は「Sp1d3rHunters」と名乗る）によるもの。 従業員へのソーシャルエンジニアリングと悪性OAuth連携でDBを吸い上げ、メールで恐喝すると説明。 盗難データは約255万件と脅威側が主張（重複不明）、Googleへの恐喝要求も報告。 | 中 | `source--daily-dc3caa8934acd3a0365f` |
| Scattered Spider、米国小売業界への攻撃を開始 | ransomware-extortion | 不明 | 不明 | 2025-05-15 | Googleの脅威分析チームは、Scattered Spider（別名UNC3944）が英国小売業界への攻撃に続き、米国の小売業界を標的にしていると警告。 同グループは、特定の業界に集中して攻撃を行う傾向があり、現在は米国小売業界への攻撃が進行中とされる。 英国では、Marks & SpencerがDragonForceランサムウェアによる攻撃を受け、VMware ESXiホスト上の仮想マシンが暗号化された。 また、Co-opは現・元会員のデータが盗まれたことを確認し、Harrodsもネットワーク侵入の試みを受けてインターネットアクセスを制限した。 Scattered Spiderは、ソーシャルエンジニアリングやクラウドアプリケーションへの不正アクセスを駆使し、データ窃取やランサムウェア攻撃を行うことで知られる。 | 高 | `source--daily-b562a237b8d95c792fb9` |
| カンタス航空、570万人の顧客に影響を及ぼすデータ侵害を確認 | intrusion | 不明 | 不明 | 2025-07-10 | 7月1日にカンタス航空はサードパーティプラットフォームへのサイバー攻撃を検知したと発表。 攻撃者は570万件の顧客データを窃取し、公開阻止のために身代金を要求。 流出データは名前、メール、Qantas Frequent Flyer(FF)会員情報が主で、170万人は住所や生年月日等も含む。 パスワードや金融情報、パスポート詳細は漏洩せず、追加のセキュリティ対策を実施中。 カンタスは影響顧客に通知し、偽メールによる二次被害への注意を呼び掛け。 | 中 | `source--daily-af6fa62de402bc99a853` |
| Marks & Spencer、サイバー攻撃により4億200万ドルの利益損失の見込み | ransomware-extortion | 不明 | 不明 | 2025-05-22 | 英国の小売大手Marks & Spencer（M&S）は、サイバー攻撃により約3億ポンド（4億200万ドル）の営業利益損失を予測。 攻撃は、DragonForceランサムウェアを使用したScattered Spiderグループによるもので、VMware ESXiホスト上の仮想マシンが暗号化された。 この攻撃により、M&Sのオンライン注文が停止し、食品供給や物流にも影響が出た。 顧客の個人情報（氏名、住所、電話番号、生年月日など）が盗まれた可能性がある。 M&Sは、保険やコスト削減策により損失をある程度相殺することを目指している。 | 中 | `source--daily-d0008bd69d4947eb98cb` |
| Scattered Spider攻撃でCo-opが1億700万ドルの損失と発表 | ransomware-extortion | 不明 | 不明 | 2025-09-26 | 英Co-opの2025年上期中間決算で、4月のサイバー攻撃に起因する8,000万ポンドの営業損失（約1億700万ドル）と報告。売上も2億600万ポンド減。 影響は一時的な増分コスト2,000万ポンドと、システム停止に伴う販売損失6,000万ポンドに区分。回復過程で下期にさらに2,000万ポンド予想。 4月下旬に一部ITを停止。DragonForce系ランサムに紐づき、Scattered Spider関与とされ、会員650万人分の個人情報窃取を確認。 Windowsドメインコントローラを再構築し、手作業運用や35万点の再配分、会員向け割引券で対応も、在庫配分や一部カテゴリで販売崩れ。 7月10日に英NCAが17–20歳の容疑者4人を逮捕。流動性は8億ポンドを維持し、CFOは資金面の懸念なしと説明。 | 高 | `source--daily-07f4616d6d343671fd3a` |
| 最近のデータ窃取サイバー攻撃でQantasが身代金要求を受ける | reported-activity | 不明 | 不明 | 2025-07-08 | Qantasは7月1日に第三者システムの不審な活動を検知し攻撃を公表。 約600万顧客の氏名、メール、電話、生年月日、マイレージ番号が流出。 クレジットカードやパスワードなどの機密情報は含まれず。 攻撃者はScattered Spiderで、最近は航空業界を標的にしている。 Qantasはオーストラリア連邦警察と協力し調査中と発表。 | 中 | `source--daily-73035cf449d00dd55adf` |
| Microsoft、Scattered SpiderハッカーをQilinランサムウェア攻撃にリンク | ransomware-extortion | 不明 | 不明 | 2024-07-17 | MicrosoftはScattered SpiderグループがQilinランサムウェアを使用していることを確認。 Scattered SpiderはフィッシングやSIMスワッピングなどで初期アクセスを得る。2022年から活動し、130以上の企業を標的にした。 Microsoftは、Scattered Spiderが攻撃キャンペーンのランサムウェアペイロードにRansomHubとQilinを追加したと報告。 QilinランサムウェアはVMware ESXiを含むシステムを狙う。 最近の攻撃ではロンドンの病院が影響を受けた。 | 高 | `source--daily-57b94c665c022e52410d` |
| 英国NCSC：英国小売業者へのサイバー攻撃は警鐘となる | reported-activity | 不明 | 不明 | 2025-05-04 | 英国国家サイバーセキュリティセンター（NCSC）は、英国の複数の小売業者を標的とした最近のサイバー攻撃について、すべての組織にとっての「警鐘」となると警告 NCSCは、被害を受けた小売業者と連携し、攻撃の性質と影響を評価している NCSCのCEOであるリチャード・ホーン博士は、組織のリーダーに対し、NCSCのウェブサイトにあるアドバイスに従い、攻撃を防ぎ、効果的に対応・回復するための適切な対策を講じるよう促している 英国下院のビジネス・貿易委員会は、Marks & SpencerおよびCo-opのCEOに対し、国家犯罪対策庁（NCA）やNCSCなどの政府機関からの支援があったかどうかを報告するよう要請 Harrods、Co-op、Marks & Spencerなど、英国の主要な小売業者がサイバー攻撃の被害を受けており、これらの攻撃はDragonForceやScattered Spiderなどの脅威アクターに関連しているとされる | 中 | `source--daily-8516c3813705dff8c58d` |
| Scattered Spider、ヘルプデスク詐欺を用いた攻撃手法とその対策 | ransomware-extortion | 不明 | 不明 | 2025-06-04 | サイバー犯罪グループ「Scattered Spider」は、企業のヘルプデスクを標的にしたソーシャルエンジニアリング攻撃を展開し、MFA（多要素認証）を回避して管理者アカウントを乗っ取る手法を用いている。 攻撃者は、被害者になりすましてヘルプデスクに連絡し、「新しい電話にしたのでMFAをリセットしてほしい」などと依頼し、MFAリセットリンクを自身のメールアドレスや電話番号に送信させる。 その後、OktaやEntraなどのセルフサービスパスワードリセット機能を悪用してアカウントを完全に掌握し、データ窃取やランサムウェアの展開などの攻撃を行う。 この手法は、2022年からTwilio、LastPass、Riot Games、Coinbaseなどの企業に対して使用されており、最近ではMarks & SpencerやCo-opへの攻撃でも確認されている。 特に、Caesars EntertainmentやMGM Resorts、Transport for Londonへの攻撃では、ヘルプデスクを通じた認証情報のリセットが初期侵入手段として利用され、多大な被害が発生した。 | 高 | `source--daily-7b838d61f8caea5e02cd` |
| 英国、主要小売業へのサイバー攻撃を受けてセキュリティ対策を共有 | ransomware-extortion | 不明 | 不明 | 2025-05-06 | M&S、Co-op、Harrodsがサイバー攻撃を受け、NCSCが全企業に対策強化を呼びかけ。 攻撃者は従業員になりすまし、ITヘルプデスクを騙して認証情報を取得。 M&Sではランサムウェアが展開され、Co-opは暗号化前に攻撃を阻止。 Harrodsは侵入の試みを確認し、アクティブな対応としてインターネットアクセスを制限。結果、侵入は確認されず。 攻撃はDragonForce作戦により行われ、Scattered SpiderやLapsus$の戦術が使用された。 NCSCは、犠牲者や法執行機関と協力して犯人を特定しようとしており、現時点では攻撃が関連しているか、単一のアクターによる組織的なキャンペーンかについては推測を避けている。 | 中 | `source--daily-4cd1fe293925310c02b7` |
| Scattered Spiderは消えていなかった：研究者が新たな攻撃に“生存”の兆候を確認 | phishing-campaign | 不明 | 不明 | 2025-09-18 | 閉鎖を宣言したはずのScattered Spiderが依然活動中で、金融分野を狙う新たな攻撃の兆候が確認された。 ReliaQuestは米国の銀行(法人名は未公表)への侵入を同グループに関連付け、業界向けのなりすましドメイン増加も観測した。 攻撃は幹部アカウントをソーシャルエンジニアリングで操り、Azure ADのセルフサービスPWリセット(SSPR)で初期アクセスを獲得。 その後CitrixやVPNで横展開し、ESXiの資格情報窃取やVM移動、VeeamとAzure全体管理者権限の悪用で昇格。 SnowflakeやAWS等からの流出試行も示唆され、挙動重視の検知とプロアクティブな防御が重要と研究者は助言。 | 高 | `source--daily-ee4056a54607e02fe6d8` |
| Ticketmasterから流出したSnowflake攻撃データ、再び販売リストに掲載 | ransomware-extortion | 不明 | 不明 | 2025-06-11 | 2024年のSnowflake攻撃で流出したTicketmasterの569GB分の顧客データが、Arkana Securityという恐喝グループによって再販リストに一時掲載。 掲載されたデータは以前に盗まれたもので、新たな侵害ではなく再流通である。 データには“RapeFlake”という窃取ツールの痕跡も含まれていた。 当該販売リストは数日で削除され、現在は閲覧不可となっている。 この攻撃にはShinyHuntersやUNC5537（Scattered Spider）などのAPTグループが関与していた。 Arkanaがこのデータを以前購入したのか、以前データを持っていた脅威アクターで構成されているのか、あるいはShinyHuntersと協力して販売しているのかは不明。 | 中 | `source--daily-50b897d744561404ee8d` |
| Qantas、Scattered Spiderによる航空業界攻撃の中でサイバー攻撃を公表 | intrusion | 不明 | 不明 | 2025-07-03 | Qantasはコールセンターのサードパーティプラットフォームで異常を検知後、攻撃を封じ込めた。 約600万人の顧客名、メール、電話番号、生年月日、フリークエントフライヤー番号が窃取された。 クレジットカード情報やパスワード、PIN等は侵害されていないとQantasは説明。 同社は豪州サイバーセキュリティセンター等へ通知し、調査を継続中。 Scattered Spiderの航空業界攻撃と類似し、Hawaiian AirlinesやWestJetも被害報告。 | 高 | `source--daily-0a6ab6298790c80e707e` |
| C0027 | campaign | 2022-06-01T04:00:00.000Z | 2022-12-01T05:00:00.000Z | 2026-05-12 | [C0027](https://attack.mitre.org/campaigns/C0027) was a financially-motivated campaign linked to [Scattered Spider](https://attack.mitre.org/groups/G1015) that targeted telecommunications and business process outsourcing (BPO) companies from at least June through December of 2022. During [C0027](https://attack.mitre.org/campaigns/C0027) [Scattered Spider](https://attack.mitre.org/groups/G1015) used various forms of social engineering, performed SIM swapping, and attempted to leverage access from victim environments to mobile carrier networks.(Citation: Crowdstrike TELCO BPO Campaign December 2022)<br> | 高 | `source--mitre-attack-19-1` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.003 | NTDS | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1006 | Direct Volume Access | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.004 | SSH | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.007 | Cloud Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.004 | Unix Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1068 | Exploitation for Privilege Escalation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1069 | Permission Groups Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1069.002 | Domain Groups | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.008 | Clear Mailbox Data | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074 | Data Staged | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.004 | Cloud Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087 | Account Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090 | Proxy | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1098 | Account Manipulation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1098.003 | Additional Cloud Roles | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114 | Email Collection | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114.003 | Email Forwarding Rule | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence | T1133 | External Remote Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1136 | Create Account | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204 | User Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1213.003 | Code Repositories | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1213.005 | Messaging Applications | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1217 | Browser Information Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1219.002 | Remote Desktop Software | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Privilege Escalation | T1484.002 | Trust Modification | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1486 | Data Encrypted for Impact | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1490 | Inhibit System Recovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1530 | Data from Cloud Storage | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1538 | Cloud Service Dashboard | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1539 | Steal Web Session Cookie | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.002 | Systemd Service | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.001 | Credentials In Files | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.004 | Private Keys | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1553.002 | Code Signing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.005 | Password Managers | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access, Defense Impairment, Persistence | T1556.006 | Multi-Factor Authentication | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access, Defense Impairment, Persistence | T1556.009 | Conditional Access Policies | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.008 | Email Hiding Rules | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566 | Phishing | nt Detection and Response (EDR) controls and support ransomware-driven financial operations. Reconnaissance - T1598 - Phishing for Information Initial Access - T1566 – |  |  | 不明 | 不明 | 中 | `source--scattered-spider--20a695a20abec121` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1572 | Protocol Tunneling | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1578.002 | Create Cloud Instance | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1580 | Cloud Infrastructure Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.001 | Social Media Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.001 | Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589 | Gather Victim Identity Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1598 | Phishing for Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1`, `source--scattered-spider--20a695a20abec121` |
| Reconnaissance | T1598.003 | Spearphishing Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1598.004 | Spearphishing Voice | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1621 | Multi-Factor Authentication Request Generation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1657 | Financial Theft | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1684.001 | Impersonation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 9件
- IOC観測: 11件
- 複数攻撃で観測: 0件
- 要レビュー候補: 5件
- 非IOC artifact観測: 128件（`artifacts.csv`）

## 主要判断と不確実性

主要判断なし

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--daily-04302db7cea311067bd3 | 英国政府、サイバー攻撃後のJLRに15億ポンドのローン保証を実施 | bleepingcomputer.com | 2025-09-30 | https://www.bleepingcomputer.com/news/security/uk-govt-backs-jlr-with-15-billion-loan-guarantee-after-cyberattack/ | osint-report | TLP:CLEAR | 中 |
| source--daily-07f4616d6d343671fd3a | Scattered Spider攻撃でCo-opが1億700万ドルの損失と発表 | bleepingcomputer.com | 2025-09-26 | https://www.bleepingcomputer.com/news/security/co-op-says-it-lost-107-million-after-scattered-spider-attack/ | osint-report | TLP:CLEAR | 中 |
| source--daily-087eb7c60fcfe537fd54 | Harrods、英国小売業界を狙ったサイバー攻撃の次なる標的に | bleepingcomputer.com | 2025-05-02 | https://www.bleepingcomputer.com/news/security/harrods-the-next-uk-retailer-targeted-in-a-cyberattack/ | osint-report | TLP:CLEAR | 中 |
| source--daily-0a6ab6298790c80e707e | Qantas、Scattered Spiderによる航空業界攻撃の中でサイバー攻撃を公表 | bleepingcomputer.com | 2025-07-03 | https://www.bleepingcomputer.com/news/security/qantas-discloses-cyberattack-amid-scattered-spider-aviation-breaches/ | osint-report | TLP:CLEAR | 中 |
| source--daily-0d8b0cd3a78d874f7394 | Marks & Spencerの侵害、Scattered Spiderランサムウェア攻撃に関連 | bleepingcomputer.com | 2025-04-29 | https://www.bleepingcomputer.com/news/security/marks-and-spencer-breach-linked-to-scattered-spider-ransomware-attack/ | osint-report | TLP:CLEAR | 中 |
| source--daily-1f9abeeb494497e6757c | 暑かったのは気温だけではない——2025年夏にサイバー攻撃が急増 | bleepingcomputer.com | 2025-08-06 | https://www.bleepingcomputer.com/news/security/the-heat-wasnt-just-outside-cyber-attacks-spiked-in-summer-2025/ | osint-report | TLP:CLEAR | 中 |
| source--daily-21728e38bdfb2401ffa0 | Scattered Spiderのハッカー、航空および輸送企業への標的をシフト | bleepingcomputer.com | 2025-06-28 | https://www.bleepingcomputer.com/news/security/scattered-spider-hackers-shift-focus-to-aviation-transportation-firms/ | osint-report | TLP:CLEAR | 中 |
| source--daily-4cd1fe293925310c02b7 | 英国、主要小売業へのサイバー攻撃を受けてセキュリティ対策を共有 | bleepingcomputer.com | 2025-05-06 | https://www.bleepingcomputer.com/news/security/uk-shares-security-tips-after-major-retail-cyberattacks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-4e50a94f394205333edf | サービスデスクが攻撃の標的に：私たちにできる対策は？ | bleepingcomputer.com | 2025-05-21 | https://www.bleepingcomputer.com/news/security/service-desks-are-under-attack-what-can-you-do-about-it/ | osint-report | TLP:CLEAR | 中 |
| source--daily-50b897d744561404ee8d | Ticketmasterから流出したSnowflake攻撃データ、再び販売リストに掲載 | bleepingcomputer.com | 2025-06-11 | https://www.bleepingcomputer.com/news/security/stolen-ticketmaster-data-from-snowflake-attacks-briefly-for-sale-again/ | osint-report | TLP:CLEAR | 中 |
| source--daily-57b94c665c022e52410d | Microsoft、Scattered SpiderハッカーをQilinランサムウェア攻撃にリンク | bleepingcomputer.com | 2024-07-17 | https://www.bleepingcomputer.com/news/security/microsoft-links-scattered-spider-hackers-to-qilin-ransomware-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-73035cf449d00dd55adf | 最近のデータ窃取サイバー攻撃でQantasが身代金要求を受ける | bleepingcomputer.com | 2025-07-08 | https://www.bleepingcomputer.com/news/security/qantas-is-being-extorted-in-recent-data-theft-cyberattack/ | osint-report | TLP:CLEAR | 中 |
| source--daily-7b838d61f8caea5e02cd | Scattered Spider、ヘルプデスク詐欺を用いた攻撃手法とその対策 | thehackernews.com | 2025-06-04 | https://thehackernews.com/2025/06/scattered-spider-understanding-help.html | osint-report | TLP:CLEAR | 中 |
| source--daily-8516c3813705dff8c58d | 英国NCSC：英国小売業者へのサイバー攻撃は警鐘となる | bleepingcomputer.com | 2025-05-04 | https://www.bleepingcomputer.com/news/security/uk-ncsc-cyberattacks-impacting-uk-retailers-are-a-wake-up-call/ | osint-report | TLP:CLEAR | 中 |
| source--daily-af6fa62de402bc99a853 | カンタス航空、570万人の顧客に影響を及ぼすデータ侵害を確認 | bleepingcomputer.com | 2025-07-10 | https://www.bleepingcomputer.com/news/security/qantas-confirms-data-breach-impacts-57-million-customers/ | osint-report | TLP:CLEAR | 中 |
| source--daily-b562a237b8d95c792fb9 | Scattered Spider、米国小売業界への攻撃を開始 | bleepingcomputer.com | 2025-05-15 | https://www.bleepingcomputer.com/news/security/google-scattered-spider-switches-targets-to-us-retail-chains/ | osint-report | TLP:CLEAR | 中 |
| source--daily-bc6f4aecde8159d70fd7 | DragonForceランサムとScattered Spiderの関係を深掘り | bleepingcomputer.com | 2025-12-04 | https://www.bleepingcomputer.com/news/security/deep-dive-into-dragonforce-ransomware-and-its-scattered-spider-connection/ | osint-report | TLP:CLEAR | 中 |
| source--daily-c18481a1b5cdd9fcdd92 | Scattered Spiderハッカー、クラウドアプリに焦点をシフトしてデータ窃盗を行う | bleepingcomputer.com | 2024-06-15 | https://www.bleepingcomputer.com/news/security/scattered-spider-hackers-switch-focus-to-cloud-apps-for-data-theft/ | osint-report | TLP:CLEAR | 中 |
| source--daily-d0008bd69d4947eb98cb | Marks & Spencer、サイバー攻撃により4億200万ドルの利益損失の見込み | bleepingcomputer.com | 2025-05-22 | https://www.bleepingcomputer.com/news/security/marks-and-spencer-faces-402-million-profit-hit-after-cyberattack/ | osint-report | TLP:CLEAR | 中 |
| source--daily-d395324d918e79d06dc6 | Scattered SpiderがVMware ESXiを狙ったハッキングを拡大 | bleepingcomputer.com | 2025-07-28 | https://www.bleepingcomputer.com/news/security/scattered-spider-is-running-a-vmware-esxi-hacking-spree/ | osint-report | TLP:CLEAR | 中 |
| source--daily-dc3caa8934acd3a0365f | Google、データ侵害でGoogle広告の見込み顧客情報が露出したと確認 | bleepingcomputer.com | 2025-08-11 | https://www.bleepingcomputer.com/news/security/google-confirms-data-breach-exposed-potential-google-ads-customers-info/ | osint-report | TLP:CLEAR | 中 |
| source--daily-ee4056a54607e02fe6d8 | Scattered Spiderは消えていなかった：研究者が新たな攻撃に“生存”の兆候を確認 | cybernews.com | 2025-09-18 | https://cybernews.com/security/scattered-spider-reliaquest-cyberattacks-financial/ | osint-report | TLP:CLEAR | 中 |
| source--daily-f9d510457677ce905d57 | Aflac、散発するScattered Spiderによる保険会社攻撃の中で侵害を公表 | bleepingcomputer.com | 2025-06-21 | https://www.bleepingcomputer.com/news/security/aflac-discloses-breach-amidst-scattered-spider-insurance-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--scattered-spider--07eb074eccced760 | crowdstrike 2024 threat hunting report |  | 2024 | summary/2024/crowdstrike-2024-threat-hunting-report.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--123eb31ea40be2ac | 2025 DSIR Report |  | 2025 | summary/2025/2025-DSIR-Report.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--1597a286964cfb96 | M Trends 2023 Report MANDIANT SPECIAL REPORT |  | 2023 | summary/2023/M-Trends 2023 Report MANDIANT SPECIAL REPORT.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--163bcd6852170f8a | Microsoft Digital Defense Report 2024 |  | 2024 | summary/2024/Microsoft Digital Defense Report 2024.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--16e2c1405293e403 | Cloud Security Risk Report 2025 |  | 2025 | summary/2026/Cloud_Security_Risk_Report_2025.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--1a7b039bc52ead0d | Bridewell 2026 Cyber Threat Intelligence Report |  | 2026 | summary/2026/Bridewell 2026 Cyber Threat Intelligence Report.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--1c00eea2f5f1e8b8 | GreyNoise The Invisible Army Residential Proxy Report |  | 不明 | APT-hunting/GreyNoise-The-Invisible-Army-Residential-Proxy-Report.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--1c5fcdd97cc085ad | Recordedfuture 2023 Annual Report ta 2024 0321 |  | 2023 | summary/2024/Recordedfuture 2023 Annual Report ta-2024-0321.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--20a695a20abec121 | scattered spider |  | 不明 | actor_profile/evidence/scattered-spider.csv | structured-data | TLP:CLEAR | 中 |
| source--scattered-spider--38f3230cbb979abb | Cydome maritime trends report 2026 final |  | 2026 | summary/2026/Cydome_maritime_trends_report_2026_final.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--3b29c610b5749a4d | Cyber Threat Intelligence Report 2025 2 |  | 2025 | summary/2025/Cyber Threat Intelligence Report 2025 2.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--463f51494faa53b4 | eset threat report h22025 |  | 不明 | summary/2025/eset-threat-report-h22025.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--48ae2cb5ec218f15 | MDDR FINAL 2023 1004 |  | 2023-10-04 | summary/2023/MDDR_FINAL_2023_1004.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--490d4fca01afc100 | 2025 dbir data breach investigations report |  | 2025 | summary/2025/2025-dbir-data-breach-investigations-report.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--4c1fbed241bfefe6 | 2025 Cyber Security Report Final |  | 2025 | summary/2026/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--5bfbea8e698f253b | Symantec Ransomware Threat Landscape 2024 |  | 2024 | summary/2024/Symantec_Ransomware_Threat_Landscape_2024.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--662f684e2e1771e5 | Security Navigator 2026 |  | 2026 | summary/2025/Security_Navigator_2026.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--674b0f00ec836e40 | 2024 Annual Cybersecurity Vulnerability Threat Landscape Research Report |  | 2024 | summary/2025/2024_Annual_Cybersecurity_Vulnerability_Threat_Landscape_Research_Report.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--6b118b27350760da | 2024YiR report |  | 2024 | summary/2025/2024YiR-report.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--6d6617e333f583b0 | tenable cloud risk report 2024 |  | 2024 | summary/2024/tenable-cloud-risk-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--6ea38b7b644f9593 | CrowdStrike 2026 Global Threat Report |  | 2026 | summary/2026/CrowdStrike-2026-Global-Threat-Report.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--70725c1eac18590c | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--scattered-spider--741b4d3df1689237 | Microsoft Digital Defense Report 2025 |  | 2025 | summary/2025/Microsoft-Digital-Defense-Report-2025.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--798d9a44f1a55fe5 | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--8e95a25b9eb735a1 | Cloudflare 2026 threat report |  | 2026 | summary/2026/Cloudflare-2026-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--9874d9660af5208f | Worldwide Ransomware Attacks as of June 2024 Consistent With Previous Year Sep2024 |  | 2024 | summary/2024/Worldwide_Ransomware_Attacks_as_of_June_2024_Consistent_With_Previous_Year_Sep2024.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--9a5cadf266e9024a | UK NCC Group Cyber Threat Intelligence Report September 2025 |  | 2025 | summary/2025/UK_NCC_Group_Cyber_Threat_Intelligence_Report_September_2025_.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--b44d8573ae226f56 | Quarterly report 2025 closing |  | 2025 | summary/2025/Quarterly report 2025 closing.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--b8408d45fa973b39 | Flashpoint 2026 Global Threat Intelligence Report |  | 2026 | summary/2026/Flashpoint_2026_Global_Threat_Intelligence_Report.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--c94c4a72464f97f7 | 2025 IC3Report |  | 2025 | cybercrime/2026/2025_IC3Report.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--d10c8ebe3e4ec438 | state of the threat report 2024 |  | 2024 | summary/2024/state-of-the-threat-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--d407ce08f2ec0fc6 | CERTFR 2026 CTI 003 |  | 2026 | summary/2026/CERTFR-2026-CTI-003.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--d4bf69ba4023a107 | 2025 Cyber Security Report Final |  | 2025 | summary/2025/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--d647298928cd8bc3 | Global Threat Report 2025 |  | 2025 | summary/2025/Global Threat Report 2025.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--d8b463c1e84c17ee | GRIT Ransomware Annual Report 2023 |  | 2023 | summary/2024/GRIT_Ransomware_Annual_Report_2023.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--dd6c9e81ee094acf | CrowdStrike 2025 Threat Hunting Report |  | 2025 | summary/2025/CrowdStrike 2025 Threat Hunting Report.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--dd93c697e3219e27 | ShinyHunters |  | 不明 | cybercrime/ShinyHunters/ShinyHunters.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--e358ca2bca827211 | 2025 CrowdStrike European Threat Landscape Report |  | 2025 | summary/2025/2025-CrowdStrike-European-Threat-Landscape-Report_.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--e4959c5ac9fbf0f2 | Cybersecurity Threats 2024 Annual Report QAX |  | 2024 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--ec861d6f2846303a | m trends 2024 |  | 2024 | summary/2024/m-trends-2024.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--ed8af487231a55ec | CrowdStrikeGlobalThreatReport2025 |  | 2025 | summary/2025/CrowdStrikeGlobalThreatReport2025.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--eeb21cd10661df07 | 2024 Customer Identity Security in Finance |  | 2024 | summary/2024/2024-Customer-Identity-Security-in-Finance.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--f5c2bcd51b106043 | CyberProof 2026 Global Threat Intelligence Report |  | 2026 | summary/2026/CyberProof_2026_Global_Threat_Intelligence_Report.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--f71c4f74eb7a89ae | stokes superseding complaint 0 |  | 不明 | cybercrime/2026/stokes_superseding_complaint_0.pdf | report | TLP:CLEAR | 中 |
| source--scattered-spider--f8504fa88662a428 | Threat Report 2026 v4 |  | 2026 | summary/2026/Threat Report 2026 v4.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
