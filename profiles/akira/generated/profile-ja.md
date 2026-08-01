# Akira 脅威アクタープロファイル

- プロファイルID: `actor--akira`
- 状態: draft
- 更新日時: 2026-07-29T23:11:59Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Akiraの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Akira**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| GOLD SAHARA | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Howling Scorpius | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| PUNK SPIDER | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| Adversary | [Akira](https://attack.mitre.org/groups/G1024) is a ransomware variant and ransomware deployment entity active since at least March 2023.(Citation: Arctic Wolf Akira 2023) [Akira](https://attack.mitre.org/groups/G1024) uses compromised credentials to access single-factor external access mechanisms such as VPNs for initial access, then various publicly-available tools and techniques for lateral movement.(Citation: Arctic Wolf Akira 2023)(Citation: Secureworks GOLD SAHARA) [Akira](https://attack.mitre.org/groups/G1024) operations are associated with "double extortion" ransomware activity, where data is exfiltrated from victim environments prior to encryption, with threats to publish files if a ransom is not paid. Technical analysis of [Akira](https://attack.mitre.org/software/S1129) ransomware indicates variants capable of targeting Windows or VMWare ESXi hypervisors and multiple overlaps with [Conti](https://attack.mitre.org/software/S0575) ransomware.(Citation: BushidoToken Akira 2023)(Citation: CISA Akira Ransomware APR 2024)(Citation: Cisco Akira Ransomware OCT 2024) |
| Capability | Megazord, Akira, Akira _v2, Rclone, Mimikatz, LaZagne, AdFind, PsExec |
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
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Storm-1567 | single-alias-intersection | 中 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Storm-1567 | canonical-name | 高 |  | https://news.sophos.com/en-us/2023/12/20/cryptoguard-an-asymmetric-approach-to-the-ransomware-battle/<br>https://securelist.com/crimeware-report-fakesg-akira-amos/111483/<br>https://www.trellix.com/en-us/about/newsroom/stories/research/akira-ransomware.html |
| misp-microsoft-activity-group | Storm-1567 | single-alias-intersection | 中 |  | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Akira - G1024 | mitre-external-id | 高 |  | https://arcticwolf.com/resources/blog/conti-and-akira-chained-together/<br>https://attack.mitre.org/groups/G1024<br>https://blog.bushidotoken.net/2023/09/tracking-adversaries-akira-another.html |
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
| malware--akira | Akira | [Akira](https://attack.mitre.org/software/S1129) ransomware, written in C++, is most prominently (but not exclusively) associated with the ransomware-as-a-service entity [Akira](https://attack.mitre.org/groups/G1024). [Akira](https://attack.mitre.org/software/S1129) ransomware has been used in attacks across North America, Europe, and Australia, with a focus on critical infrastructure sectors including manufacturing, education, and IT services. [Akira](https://attack.mitre.org/software/S1129) ransomware employs hybrid encryption and threading to increase the speed and efficiency of encryption and runtime arguments for tailored attacks. Notable variants include Rust-based [Megazord](https://attack.mitre.org/software/S1191) for targeting Windows and [Akira _v2](https://attack.mitre.org/software/S1194) for targeting VMware ESXi servers.(Citation: Kersten Akira 2023)(Citation: CISA Akira Ransomware APR 2024)(Citation: Cisco Akira Ransomware OCT 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--akira-v2 | Akira _v2 | [Akira _v2](https://attack.mitre.org/software/S1194) is a Rust-based variant of [Akira](https://attack.mitre.org/software/S1129) ransomware that has been in use since at least 2024. [Akira _v2](https://attack.mitre.org/software/S1194) is designed to target VMware ESXi servers and includes a new command-line argument set and other expanded capabilities.(Citation: CISA Akira Ransomware APR 2024)(Citation: Cisco Akira Ransomware OCT 2024)(Citation: Palo Alto Howling Scorpius DEC 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--megazord | Megazord | [Megazord](https://attack.mitre.org/software/S1191) is a Rust-based variant of [Akira](https://attack.mitre.org/software/S1129) ransomware that has been in use since at least August 2023 to target Windows environments. [Megazord](https://attack.mitre.org/software/S1191) has been attributed to the [Akira](https://attack.mitre.org/groups/G1024) group based on overlapping infrastructure though is possibly not exclusive to the group.(Citation: CISA Akira Ransomware APR 2024)(Citation: Cisco Akira Ransomware OCT 2024)(Citation: Palo Alto Howling Scorpius DEC 2024)<br><br> | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--rclone | Rclone | [Rclone](https://attack.mitre.org/software/S1040) is a command line program for syncing files with cloud storage services such as Dropbox, Google Drive, Amazon S3, and MEGA. [Rclone](https://attack.mitre.org/software/S1040) has been used in a number of ransomware campaigns, including those associated with the [Conti](https://attack.mitre.org/software/S0575) and DarkSide Ransomware-as-a-Service operations.(Citation: Rclone)(Citation: Rclone Wars)(Citation: Detecting Rclone)(Citation: DarkSide Ransomware Gang)(Citation: DFIR Conti Bazar Nov 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--lazagne | LaZagne | [LaZagne](https://attack.mitre.org/software/S0349) is a post-exploitation, open-source tool used to recover stored passwords on a system. It has modules for Windows, Linux, and OSX, but is mainly focused on Windows systems. [LaZagne](https://attack.mitre.org/software/S0349) is publicly available on GitHub.(Citation: GitHub LaZagne Dec 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--adfind | AdFind | [AdFind](https://attack.mitre.org/software/S0552) is a free command-line query tool that can be used for gathering information from Active Directory.(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: FireEye FIN6 Apr 2019)(Citation: FireEye Ryuk and Trickbot January 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--psexec | PsExec | [PsExec](https://attack.mitre.org/software/S0029) is a free Microsoft tool that can be used to execute a program on another computer. It is used by IT administrators and attackers.(Citation: Russinovich Sysinternals)(Citation: SANS PsExec) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### インフラ

未確認

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FogランサムウェアがSonicWall VPNを標的に企業ネットワークに侵入 | ransomware-extortion | 不明 | 不明 | 2024-10-28 |  | malware--akira | ttp--activity-rule--9388646871131d17eebe | victim--activity-rule--efcb31ad5721ef88aa8b | FogとAkiraランサムウェアがSonicWall VPN脆弱性を悪用してネットワークに侵入。 攻撃はCVE-2024-40766をエクスプロイトして行い、ランサムウェアで攻撃する事例が少なくとも30件発生。 侵入後約10時間で暗号化が進むが、最速で1.5～2時間で完了。 VPNアクセスは既知のログインメッセージIDで監視可能。 一部の攻撃でデータ窃取も行われたが、古いファイルは対象外。 | 中 | `source--daily-3c12eda093e5c59e0ee6` |
| 重大なSonicWall SSLVPNバグ、ランサムウェア攻撃に悪用される | ransomware-extortion | 不明 | 不明 | 2024-09-11 |  | malware--akira | ttp--activity-rule--68de45381ecf965a5cbd | victim--activity-rule--5db282902109648e4f12 | SonicWallのSSLVPN脆弱性（CVE-2024-40766）がランサムウェア攻撃に利用。 Akiraランサムウェアのアフィリエイトがこの脆弱性を悪用。 SonicWallは、この脆弱性は、ファイアウォールの管理アクセスインターフェースのみに影響すると伝えていたが、後にSSLVPN機能にも影響し、攻撃に悪用されていることを明らかにした。 SonicWallはパッチを8月22日に公開し、顧客に迅速な対応を促している。 CISAは連邦機関に9月30日までのパッチ適用を命じた。 | 中 | `source--daily-0662aaff581d0ab45bce` |
| Hitachi Vantara、Akiraランサムウェア攻撃後にサーバーをオフライン化 | ransomware-extortion | 不明 | 不明 | 2025-04-29 | target--activity-rule--sector--210dddb39397dbe50e91 | malware--akira |  | victim--activity-rule--2f29ab2eea3eb52de00e | 日立の子会社である、Hitachi VantaraがAkiraランサムウェア攻撃を受け、一部システムが停止。 外部の専門家を雇い、影響範囲の調査と復旧作業を実施中。 攻撃でファイルが盗まれ、ランサムノートが設置されたことが判明。 クラウドサービスは影響を受けていなかったが、封じ込めの一環としてHitachi Vantaraのシステムおよび製造部門は中断された。 攻撃は政府関連プロジェクトにも影響を与えた可能性がある。 | 高 | `source--daily-7fac464b25387fdb006e` |
| Akiraランサムウェア、SonicWall SSLVPNの重大バグを再悪用 | ransomware-extortion | 不明 | 不明 | 2025-09-12 |  | malware--akira | ttp--activity-rule--a0e15fe7f9856eddb902 | victim--activity-rule--816a2d292a62aa108017 | AkiraがCVE-2024-40766を再悪用し、未更新のSonicWall SSLVPN経由で侵入。 SonicWallは2024年8月に修正公開、更新時はローカルSSLVPNアカウントのPW更新推奨。 ACSCとRapid7が最近の悪用増加を警告、不完全な修復が原因である可能性。 SonicWallはゼロデイ関与を否定、同CVEとの相関が高いと説明。 影響はGen5〜7の特定版。7.3.0以降へのアップデートやMFAの強制・権限見直し等を推奨。 | 高 | `source--daily-c6a57e3d4fd20c381ed8` |
| Apache OpenOffice、ランサムウェア集団のデータ侵害主張に反論 | ransomware-extortion | 不明 | 不明 | 2025-11-06 |  | malware--akira |  | victim--activity-rule--7b83cc15a420f71f6ba8 | Akiraランサムウェアが10月30日、Apache OpenOfficeへの侵入と23GBの機密窃取を主張し、流出予告を掲載。 これに対しApache Software Foundationは、主張内容のような従業員・財務データ自体を保有せず、現時点で証拠なしと反論。 同財団は調査中としつつ、OpenOffice/ASFシステムの侵害痕跡は見つからず、身代金要求の受領も確認していないと説明。 OpenOfficeはOSSで有償雇用の開発者はおらず、課題は公開MLで扱われるため、主張内容と整合しないと強調。 記事時点でAkira側は窃取とするデータを未公開で、ASFは法執行機関や外部専門家への連絡も行っていない。 | 中 | `source--daily-efcfda27f495de5d5c60` |
| トロント動物園、昨年のランサムウェア攻撃に関する最新情報を共有 | ransomware-extortion | 2022-01 | 2023-04 | 2025-03-06 | target--activity-rule--country--ee55e5e8faa5dd675d7b, target--activity-rule--sector--4221b5fbb827488c6eaa | malware--akira |  | victim--activity-rule--2f21c13c1480ac133511 | カナダ最大の動物園であるトロント動物園は、2024年1月に発生したランサムウェア攻撃によるデータ侵害について詳細を公表 侵害された情報には、従業員、元従業員、ボランティア、寄付者の個人情報や財務情報が含まれる 2022年1月から2023年4月の間にクレジットカード取引を行ったゲストや会員の名前、住所、電話番号、メールアドレス、クレジットカードの下4桁および有効期限が漏洩 2000年から2023年4月までの一般入場券や会員購入に関する取引データも含まれる トロント動物園は、オンタリオ州情報プライバシーコミッショナー事務局にデータ侵害を報告し、影響を受けた人々に対し、金融口座の明細を監視するよう助言 トロント動物園は特定の攻撃者を公表していないが、Akiraランサムウェア集団が2024年1月に犯行声明を出し、133GBのデータを盗んだと主張 | 中 | `source--daily-73166036d74c23fae026` |
| AkiraランサムウェアがCPUチューニングツールを悪用しMicrosoft Defenderを無効化 | ransomware-extortion | 2025-07-15 | 2025-07-15 | 2025-08-07 |  | malware--akira |  | victim--activity-rule--b1521ba5d993086623a9 | Intel製CPUチューニングドライバーrwdrv.sysを悪用し、カーネル権限でDefenderを停止 2つ目の悪意ドライバーhlpdrv.sysがDefenderのDisableAntiSpywareレジストリを変更 BYOVD戦術は2025年7月15日以降のAkira攻撃で繰り返し観測 SonicWall SSLVPNを狙う活動やBumblebee/AdaptixC2経路も報告 Bumblebeeマルウェアを使う事例では、ManageEngine OpManagerのSEOポイズニングから感染させる事例もあった GuidePointがYARA・IOC公開、管理者は監視とブロックを推奨 | 高 | `source--daily-4e4cc7628ff86fb403b4` |
| AkiraおよびFogランサムウェア、Veeamの重大なリモートコード実行脆弱性を悪用 | ransomware-extortion | 2024-09 | 2024-09 | 2024-10-14 |  | malware--akira |  | victim--activity-rule--2f20859af17320f58e01 | AkiraとFogランサムウェアがVeeam Backup & ReplicationのRCE脆弱性(CVE-2024-40711)を悪用。 この脆弱性 (CVE-2024-40711) は、認証されていない攻撃者が低複雑度の攻撃で悪用できる、信頼できないデータのデシリアライゼーションによるもの。 攻撃者は、VPNの脆弱性や既に漏洩した資格情報を用いて、ネットワークにアクセス。 悪用により、攻撃者は管理者権限を取得し、ランサムウェアを展開。 同脆弱性に対するパッチは2024年9月に公開されたが、既に悪用されている。 Fogランサムウェアを展開した攻撃者は、Hyper-Vサーバーに侵入し、rcloneでデータを流出させた事例も確認された。 | 高 | `source--daily-29f74832270318181f72` |
| GPUを活用したAkiraランサムウェアの復号ツールがGitHubで公開 | ransomware-extortion | 不明 | 不明 | 2025-03-17 |  | malware--akira |  | victim--activity-rule--cc625bf6599c24c1c7c9 | セキュリティ研究者のYohanes Nugroho氏が、Linux版Akiraランサムウェアの復号ツールを公開 Akiraの暗号鍵生成にタイムスタンプが使用されることを利用し、GPUの計算能力で鍵を特定 復号ツールはGitHubで入手可能。ファイル復元の手順も提供している。 Nugroho氏は復号に約3週間と1,200ドルのGPUリソースを費やした 復号プロセスは各ファイルの暗号鍵をブルートフォース攻撃で特定する手法 | 高 | `source--daily-f08faf92c2b925e530ef` |
| 被害者が支払いをやめたことで、ランサムウェアの利益が減少 | ransomware-extortion | 不明 | 不明 | 2025-10-28 |  | malware--akira |  | victim--activity-rule--903399eb2370a4b426ba | Covewareの最新分析で、身代金を支払った被害組織の割合は2025年Q3に23%まで低下し、観測史上の最低を更新。 平均/中央値の支払い額も前期比で減少し、平均37.7万ドル・中央値14万ドルに下落、支払い忌避の流れが強まる。 攻撃は暗号化＋窃取の二重恐喝が主流で、Q3の76%でデータ流出。窃取のみの攻撃に限ると支払い率は19%。 AkiraやQilinが44%を占め、中堅企業への集中や、リモートアクセス侵害・ソフト脆弱性悪用の増加が顕著。 利益縮小で攻撃は精緻化し、今後は大企業狙いも強まる見通し。ソーシャルエンジニアリングや内通者勧誘の活用が進む。 | 中 | `source--daily-a0023564f914d51f566d` |
| SonicWall、SSLVPNゼロデイ否定　2024年既知脆弱性悪用とAkiraランサム攻撃関連を確認 | ransomware-extortion | 不明 | 不明 | 2025-08-08 |  | malware--akira | ttp--activity-rule--fe14f3f3f9e39e3c3d2e | victim--activity-rule--20e26739710844ffc8b1 | SonicWallはGen 7ファイアウォールのSSLVPN経由Akira攻撃がCVE-2024-40766悪用であると結論。 CVE-2024-40766は2024年8月修正済みの重大アクセス制御欠陥で未更新機器が標的。 移行時に旧パスワードをリセットせず持ち越したケースが多く関連。 推奨はFWをv7.3.0以降へ更新し全ローカルユーザーPWをリセット、特にSSLVPN用。 Reddit等ではベンダー見解に対する疑念もあり、迅速な対策適用が重要とされる。 | 高 | `source--daily-4ccacc67cc78bb4bfd28` |
| Akiraランサムウェア、MFA保護のSonicWall VPNアカウントを侵害 | ransomware-extortion | 不明 | 不明 | 2025-09-29 |  | malware--akira |  | victim--activity-rule--497af04e5011199475c6 | 現在進行中のAkiraがSonicWall SSL VPNを標的にし、OTPを用いたMFAが有効でも認証成功する事例が報告された。 研究者は過去侵入で窃取されたOTPシードの再利用を疑うが、具体的手法は未確定。複数回のOTP挑戦後に成功が観測。 2024年公開の不適切なアクセス制御（CVE-2024-40766）で収集された認証情報が、パッチ適用後も悪用され続けている。 侵入後は数分で内部スキャンを開始し、ImpacketやBloodHound等で横展開、Veeamから資格情報を抽出する手口が確認。 BYOVDでconsent.exeからDLLサイドロードし脆弱ドライバ（rwdrv.sys等）を読み込み、EDRを無効化して暗号化を実行。 | 高 | `source--daily-251d2ee4d8e5443dd89d` |
| CISA、Nutanix VMを狙うAkiraランサムウェアのLinux暗号化器に警告 | ransomware-extortion | 不明 | 不明 | 2025-11-15 |  | malware--akira | ttp--activity-rule--01e7c2fc656b684e5c1f, ttp--activity-rule--af3da9f49926c20d611f, ttp--activity-rule--e56cb1e3d3b1375fe6be | victim--activity-rule--797bd79c49506030ccc9 | 米政府機関（CISA・FBI・DC3・HHS等）は、AkiraがNutanix AHVの仮想ディスクを暗号化する事例を確認し、共同勧告を更新。 2025年6月の初確認では、SonicWallのCVE-2024-40766悪用を足掛かりにAHV環境の.qcow2ディスクを暗号化したと報告。 AkiraのLinux版はESXiではesxcli等でVM停止後に暗号化、AHVではacli/ncliを使わず.qcow2を直接暗号化すると分析。 侵入後は窃取された/総当たりされたアカウントでVPN・SSHでアクセスやSonicWallの脆弱性を悪用するなどして侵入。 AnyDesk/Impacket等で偵察や横展開をし、VeeamのCVE-2023-27532・CVE-2024-40711悪用してバックアップにアクセスし削除。 勧告はオフラインバックアップ整備、MFA強制、既知悪用脆弱性への迅速パッチ適用などの緩和策実施を要請。 | 高 | `source--daily-48e314e2ec6d02091f74` |
| Akiraランサムウェア：支払いだけでは匿名性を保てない | ransomware-extortion | 不明 | 不明 | 2025-06-01 |  | malware--akira | ttp--activity-rule--e6b5ee7e3aed202956a2 | victim--activity-rule--0c45f09657c09ed89b48 | ニュージャージー州の企業がAkiraランサムウェアの被害を受け、60万ドルの要求を20万ドルに交渉し支払った。 攻撃者は「List.7z」アーカイブで被害者のファイル構造を示し、データ所有の証拠として提示。 支払い後、「Deletion.7z」アーカイブでデータ削除の証拠を提供したが、実際の削除は確認できない。 被害者とのチャットログやファイル構造が公開され、匿名性が保たれなかった。 攻撃者はネットワークアクセスをダークウェブで購入し、Kerberoastingでドメイン管理者の資格情報を取得したと主張。 | 高 | `source--daily-08853165537986c77f7f` |
| Akiraランサムウェア攻撃が急増、SonicWallファイアウォールが標的に | ransomware-extortion | 不明 | 不明 | 2025-08-02 |  | malware--akira |  | victim--activity-rule--eab06479686a6f477b11 | 7月中旬以降、AkiraランサムウェアがSonicWall SSL VPNを経由し侵入急増。 Arctic Wolfは未知のゼロデイ利用の可能性を示唆、資格情報攻撃も否定せず。 侵入後すぐ暗号化へ移行する傾向が2024年10月から継続確認。 管理者にはSSL VPN一時停止とホスティング系IPからのVPN認証遮断を推奨。 SMA 100のRCE脆弱性CVE-2025-40599も要パッチ、ログ確認でIoC調査を勧告。 | 高 | `source--daily-339537ab2997fa08795e` |
| FBI: Akiraランサムウェア、250社以上から4200万ドルを詐取 | ransomware-extortion | 2023-03 | 2023-03 | 2024-04-19 |  | malware--akira |  | victim--activity-rule--0c5b8c0e3e6470d94efd | Akiraランサムウェアが250以上の組織を標的に4200万ドルを詐取 2023年3月に出現し、幅広い業界を標的に急速に展開 北米、欧州、豪州で、幅広いビジネスと基盤インフラへ影響 FBIとCISAは組織の脆弱性対策と多要素認証の重要性を強調 攻撃の被害を減少させるための具体的な対策とガイドライン提供 | 高 | `source--daily-89a8fc15ce47bbec4793` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| FogランサムウェアがSonicWall VPNを標的に企業ネットワークに侵入 | Akira | Akira | T1190 Exploit Public-Facing Application | 情報なし | 情報なし | 被害事例: FogランサムウェアがSonicWall VPNを標的に企業ネットワークに侵入 | 中 |
| 重大なSonicWall SSLVPNバグ、ランサムウェア攻撃に悪用される | Akira | Akira | T1190 Exploit Public-Facing Application | 情報なし | 情報なし | 被害事例: 重大なSonicWall SSLVPNバグ、ランサムウェア攻撃に悪用される | 中 |
| Hitachi Vantara、Akiraランサムウェア攻撃後にサーバーをオフライン化 | Akira | Akira | 情報なし | 情報なし | 政府・行政 | Hitachi Vantara | 高 |
| Akiraランサムウェア、SonicWall SSLVPNの重大バグを再悪用 | Akira | Akira | T1190 Exploit Public-Facing Application | 情報なし | 情報なし | 被害事例: Akiraランサムウェア、SonicWall SSLVPNの重大バグを再悪用 | 高 |
| Apache OpenOffice、ランサムウェア集団のデータ侵害主張に反論 | Akira | Akira | 情報なし | 情報なし | 情報なし | Apache OpenOffice | 中 |
| トロント動物園、昨年のランサムウェア攻撃に関する最新情報を共有 | Akira | Akira | 情報なし | 情報なし | カナダ, 金融 | トロント動物園 | 中 |
| AkiraランサムウェアがCPUチューニングツールを悪用しMicrosoft Defenderを無効化 | Akira | Akira | 情報なし | 情報なし | 情報なし | 被害事例: AkiraランサムウェアがCPUチューニングツールを悪用しMicrosoft Defenderを無効化 | 高 |
| AkiraおよびFogランサムウェア、Veeamの重大なリモートコード実行脆弱性を悪用 | Akira | Akira | 情報なし | 情報なし | 情報なし | 被害事例: AkiraおよびFogランサムウェア、Veeamの重大なリモートコード実行脆弱性を悪用 | 高 |
| GPUを活用したAkiraランサムウェアの復号ツールがGitHubで公開 | Akira | Akira | 情報なし | 情報なし | 情報なし | 被害事例: GPUを活用したAkiraランサムウェアの復号ツールがGitHubで公開 | 高 |
| 被害者が支払いをやめたことで、ランサムウェアの利益が減少 | Akira | Akira | 情報なし | 情報なし | 情報なし | 被害事例: 被害者が支払いをやめたことで、ランサムウェアの利益が減少 | 中 |
| SonicWall、SSLVPNゼロデイ否定　2024年既知脆弱性悪用とAkiraランサム攻撃関連を確認 | Akira | Akira | T1190 Exploit Public-Facing Application | 情報なし | 情報なし | 被害事例: SonicWall、SSLVPNゼロデイ否定　2024年既知脆弱性悪用とAkiraランサム攻撃関連を確認 | 高 |
| Akiraランサムウェア、MFA保護のSonicWall VPNアカウントを侵害 | Akira | Akira | 情報なし | 情報なし | 情報なし | 被害事例: Akiraランサムウェア、MFA保護のSonicWall VPNアカウントを侵害 | 高 |
| CISA、Nutanix VMを狙うAkiraランサムウェアのLinux暗号化器に警告 | Akira | Akira | T1190 Exploit Public-Facing Application, T1490 Inhibit System Recovery, T1486 Data Encrypted for Impact | 情報なし | 情報なし | 被害事例: CISA、Nutanix VMを狙うAkiraランサムウェアのLinux暗号化器に警告 | 高 |
| Akiraランサムウェア：支払いだけでは匿名性を保てない | Akira | Akira | T1560.001 Archive via Utility | 情報なし | 情報なし | 被害事例: Akiraランサムウェア：支払いだけでは匿名性を保てない | 高 |
| Akiraランサムウェア攻撃が急増、SonicWallファイアウォールが標的に | Akira | Akira | 情報なし | 情報なし | 情報なし | 被害事例: Akiraランサムウェア攻撃が急増、SonicWallファイアウォールが標的に | 高 |
| FBI: Akiraランサムウェア、250社以上から4200万ドルを詐取 | Akira | Akira | 情報なし | 情報なし | 情報なし | 被害事例: FBI: Akiraランサムウェア、250社以上から4200万ドルを詐取 | 高 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | カナダ | 活動「トロント動物園、昨年のランサムウェア攻撃に関する最新情報を共有」の記述で標的として明示された国・地域。 | 2022-01 | 2023-04 | 中 | `source--daily-73166036d74c23fae026` |
| countries | シリア | 活動「AkiraおよびFogランサムウェア、Veeamの重大なリモートコード実行脆弱性を悪用」の記述で標的・被害国として明示されている。 | 2024-09 | 2024-09 | 中 | `source--daily-29f74832270318181f72` |
| regions | 北米 | 活動「FBI: Akiraランサムウェア、250社以上から4200万ドルを詐取」の記述で標的地域として北米が明示されている。 | 2023-03 | 2023-03 | 中 | `source--daily-89a8fc15ce47bbec4793` |
| regions | 欧州 | 活動「FBI: Akiraランサムウェア、250社以上から4200万ドルを詐取」の記述で標的地域として欧州が明示されている。 | 2023-03 | 2023-03 | 中 | `source--daily-89a8fc15ce47bbec4793` |
| sectors | 政府・行政 | 活動「Hitachi Vantara、Akiraランサムウェア攻撃後にサーバーをオフライン化」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-7fac464b25387fdb006e` |
| sectors | 金融 | 活動「トロント動物園、昨年のランサムウェア攻撃に関する最新情報を共有」の記述で標的として明示された産業。 | 2022-01 | 2023-04 | 中 | `source--daily-73166036d74c23fae026` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Akiraランサムウェア：支払いだけでは匿名性を保てない | 非公開 | aggregate | multiple-organizations | reported |  | malware--akira | ttp--activity-rule--e6b5ee7e3aed202956a2 |  | financial-loss: ニュージャージー州の企業がAkiraランサムウェアの被害を受け、60万ドルの要求を20万ドルに交渉し支払った。<br>encryption: Akiraランサムウェア：支払いだけでは匿名性を保てない | 不明 | 不明 | 2025-06-01 | 高 | `source--daily-08853165537986c77f7f` |
| 被害事例: FBI: Akiraランサムウェア、250社以上から4200万ドルを詐取 | 非公開 | aggregate | multiple-organizations | reported |  | malware--akira |  |  | encryption: FBI: Akiraランサムウェア、250社以上から4200万ドルを詐取 | 2023-03 | 2023-03 | 2024-04-19 | 高 | `source--daily-89a8fc15ce47bbec4793` |
| 被害事例: SonicWall、SSLVPNゼロデイ否定　2024年既知脆弱性悪用とAkiraランサム攻撃関連を確認 | 非公開 | aggregate | multiple-organizations | reported |  | malware--akira | ttp--activity-rule--fe14f3f3f9e39e3c3d2e | VPN／リモートアクセス機器, ネットワーク機器 |  | 不明 | 不明 | 2025-08-08 | 高 | `source--daily-4ccacc67cc78bb4bfd28` |
| 被害事例: AkiraおよびFogランサムウェア、Veeamの重大なリモートコード実行脆弱性を悪用 | 非公開 | anonymous | unknown | reported |  | malware--akira |  | VPN／リモートアクセス機器, サーバー | data-theft: Fogランサムウェアを展開した攻撃者は、Hyper-Vサーバーに侵入し、rcloneでデータを流出させた事例も確認された。<br>encryption: AkiraおよびFogランサムウェア、Veeamの重大なリモートコード実行脆弱性を悪用 | 2024-09 | 2024-09 | 2024-10-14 | 高 | `source--daily-29f74832270318181f72` |
| 被害事例: トロント動物園、昨年のランサムウェア攻撃に関する最新情報を共有 | トロント動物園 | named | organization | alleged | target--activity-rule--country--ee55e5e8faa5dd675d7b, target--activity-rule--sector--4221b5fbb827488c6eaa | malware--akira |  | メール／メールアカウント | encryption: トロント動物園、昨年のランサムウェア攻撃に関する最新情報を共有<br>privacy: カナダ最大の動物園であるトロント動物園は、2024年1月に発生したランサムウェア攻撃によるデータ侵害について詳細を公表 侵害された情報には、従業員、元従業員、ボランティア、寄付者の個人情報や財務情報が含まれる 2022年1月から2023年4月の間にクレジットカード取引を行ったゲストや会員の名前、住所、電話番号、メールアドレス、クレジットカードの下4桁および有効期限が漏洩 2000年から2023年4月までの一般入場券や会員購入に関する取引データも含まれる トロント動物園は、オンタリオ州情報プライバシーコミッショナー事務局にデータ侵害を報告し、影 | 2022-01 | 2023-04 | 2025-03-06 | 中 | `source--daily-73166036d74c23fae026` |
| 被害事例: Hitachi Vantara、Akiraランサムウェア攻撃後にサーバーをオフライン化 | Hitachi Vantara | named | organization | reported | target--activity-rule--sector--210dddb39397dbe50e91 | malware--akira |  | サーバー, クラウド／SaaS | encryption: Hitachi Vantara、Akiraランサムウェア攻撃後にサーバーをオフライン化<br>disruption: Hitachi Vantara、Akiraランサムウェア攻撃後にサーバーをオフライン化 | 不明 | 不明 | 2025-04-29 | 高 | `source--daily-7fac464b25387fdb006e` |
| 被害事例: Akiraランサムウェア、MFA保護のSonicWall VPNアカウントを侵害 | 非公開 | aggregate | multiple-organizations | reported |  | malware--akira |  | VPN／リモートアクセス機器, OT／ICS | encryption: Akiraランサムウェア、MFA保護のSonicWall VPNアカウントを侵害 | 不明 | 不明 | 2025-09-29 | 高 | `source--daily-251d2ee4d8e5443dd89d` |
| 被害事例: 重大なSonicWall SSLVPNバグ、ランサムウェア攻撃に悪用される | 非公開 | anonymous | unknown | reported |  | malware--akira | ttp--activity-rule--68de45381ecf965a5cbd | VPN／リモートアクセス機器, ネットワーク機器 | encryption: 重大なSonicWall SSLVPNバグ、ランサムウェア攻撃に悪用される | 不明 | 不明 | 2024-09-11 | 中 | `source--daily-0662aaff581d0ab45bce` |
| 被害事例: CISA、Nutanix VMを狙うAkiraランサムウェアのLinux暗号化器に警告 | 非公開 | anonymous | unknown | reported |  | malware--akira | ttp--activity-rule--01e7c2fc656b684e5c1f, ttp--activity-rule--af3da9f49926c20d611f, ttp--activity-rule--e56cb1e3d3b1375fe6be | VPN／リモートアクセス機器 | encryption: CISA、Nutanix VMを狙うAkiraランサムウェアのLinux暗号化器に警告<br>disruption: 勧告はオフラインバックアップ整備、MFA強制、既知悪用脆弱性への迅速パッチ適用などの緩和策実施を要請。 | 不明 | 不明 | 2025-11-15 | 高 | `source--daily-48e314e2ec6d02091f74` |
| 被害事例: Apache OpenOffice、ランサムウェア集団のデータ侵害主張に反論 | Apache OpenOffice | named | organization | disputed |  | malware--akira |  |  | encryption: Apache OpenOffice、ランサムウェア集団のデータ侵害主張に反論 | 不明 | 不明 | 2025-11-06 | 中 | `source--daily-efcfda27f495de5d5c60` |
| 被害事例: Akiraランサムウェア、SonicWall SSLVPNの重大バグを再悪用 | 非公開 | anonymous | unknown | reported |  | malware--akira | ttp--activity-rule--a0e15fe7f9856eddb902 | VPN／リモートアクセス機器 | encryption: Akiraランサムウェア、SonicWall SSLVPNの重大バグを再悪用 | 不明 | 不明 | 2025-09-12 | 高 | `source--daily-c6a57e3d4fd20c381ed8` |
| 被害事例: 被害者が支払いをやめたことで、ランサムウェアの利益が減少 | 非公開 | aggregate | multiple-organizations | reported |  | malware--akira |  | VPN／リモートアクセス機器 | data-theft: 攻撃は暗号化＋窃取の二重恐喝が主流で、Q3の76%でデータ流出。<br>encryption: 被害者が支払いをやめたことで、ランサムウェアの利益が減少 | 不明 | 不明 | 2025-10-28 | 中 | `source--daily-a0023564f914d51f566d` |
| 被害事例: AkiraランサムウェアがCPUチューニングツールを悪用しMicrosoft Defenderを無効化 | 非公開 | anonymous | unknown | reported |  | malware--akira |  | VPN／リモートアクセス機器 | encryption: AkiraランサムウェアがCPUチューニングツールを悪用しMicrosoft Defenderを無効化 | 2025-07-15 | 2025-07-15 | 2025-08-07 | 高 | `source--daily-4e4cc7628ff86fb403b4` |
| 被害事例: GPUを活用したAkiraランサムウェアの復号ツールがGitHubで公開 | 非公開 | anonymous | unknown | reported |  | malware--akira |  | 開発環境／ソースコード | encryption: GPUを活用したAkiraランサムウェアの復号ツールがGitHubで公開 | 不明 | 不明 | 2025-03-17 | 高 | `source--daily-f08faf92c2b925e530ef` |
| 被害事例: Akiraランサムウェア攻撃が急増、SonicWallファイアウォールが標的に | 非公開 | anonymous | unknown | reported |  | malware--akira |  | VPN／リモートアクセス機器, ネットワーク機器 | encryption: Akiraランサムウェア攻撃が急増、SonicWallファイアウォールが標的に | 不明 | 不明 | 2025-08-02 | 高 | `source--daily-339537ab2997fa08795e` |
| 被害事例: FogランサムウェアがSonicWall VPNを標的に企業ネットワークに侵入 | 非公開 | aggregate | multiple-organizations | reported |  | malware--akira | ttp--activity-rule--9388646871131d17eebe | VPN／リモートアクセス機器 | data-theft: 一部の攻撃でデータ窃取も行われたが、古いファイルは対象外。<br>encryption: FogランサムウェアがSonicWall VPNを標的に企業ネットワークに侵入 | 不明 | 不明 | 2024-10-28 | 中 | `source--daily-3c12eda093e5c59e0ee6` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Initial Access | T1190 | Exploit Public-Facing Application | 侵入後は窃取された/総当たりされたアカウントでVPN・SSHでアクセスやSonicWallの脆弱性を悪用するなどして侵入。 |  | activity--daily-df141a5fa2743d0b0e36 | 不明 | 不明 | 中 | `source--daily-48e314e2ec6d02091f74` |
| Initial Access | T1190 | Exploit Public-Facing Application | 重大なSonicWall SSLVPNバグ、ランサムウェア攻撃に悪用される SonicWallのSSLVPN脆弱性（CVE-2024-40766）がランサムウェア攻撃に利用。 |  | activity--daily-18024c75810d0541507f | 不明 | 不明 | 中 | `source--daily-0662aaff581d0ab45bce` |
| Initial Access | T1190 | Exploit Public-Facing Application | FogランサムウェアがSonicWall VPNを標的に企業ネットワークに侵入 FogとAkiraランサムウェアがSonicWall VPN脆弱性を悪用してネットワークに侵入。 | malware--akira | activity--daily-168bcc08caaa00d067b7 | 不明 | 不明 | 中 | `source--daily-3c12eda093e5c59e0ee6` |
| Initial Access | T1190 | Exploit Public-Facing Application | Akiraランサムウェア、SonicWall SSLVPNの重大バグを再悪用 AkiraがCVE-2024-40766を再悪用し、未更新のSonicWall SSLVPN経由で侵入。 | malware--akira | activity--daily-2e52ef1ae82d2bb0b0a3 | 不明 | 不明 | 中 | `source--daily-c6a57e3d4fd20c381ed8` |
| Impact | T1490 | Inhibit System Recovery | AnyDesk/Impacket等で偵察や横展開をし、VeeamのCVE-2023-27532・CVE-2024-40711悪用してバックアップにアクセスし削除。 |  | activity--daily-df141a5fa2743d0b0e36 | 不明 | 不明 | 中 | `source--daily-48e314e2ec6d02091f74` |
| Impact | T1486 | Data Encrypted for Impact | CISA、Nutanix VMを狙うAkiraランサムウェアのLinux暗号化器に警告 | malware--akira | activity--daily-df141a5fa2743d0b0e36 | 不明 | 不明 | 中 | `source--daily-48e314e2ec6d02091f74` |
| Collection | T1560.001 | Archive via Utility | 攻撃者は「List.7z」アーカイブで被害者のファイル構造を示し、データ所有の証拠として提示。 |  | activity--daily-dfd75e06c790813a28cd | 不明 | 不明 | 中 | `source--daily-08853165537986c77f7f` |
| Initial Access | T1190 | Exploit Public-Facing Application | SonicWall、SSLVPNゼロデイ否定 2024年既知脆弱性悪用とAkiraランサム攻撃関連を確認 SonicWallはGen 7ファイアウォールのSSLVPN経由Akira攻撃がCVE-2024-40766悪用であると結論。 | malware--akira | activity--daily-cdbff9d44dafa3db675f | 不明 | 不明 | 中 | `source--daily-4ccacc67cc78bb4bfd28` |
| Discovery | T1018 | Remote System Discovery | [Akira](https://attack.mitre.org/groups/G1024) uses software such as Advanced IP Scanner and MASSCAN to identify remote hosts within victim networks.(Citation: Arctic Wolf Akira 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | [Akira](https://attack.mitre.org/groups/G1024) has used RDP for lateral movement.(Citation: Cisco Akira Ransomware OCT 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.001 | Binary Padding | [Akira](https://attack.mitre.org/groups/G1024) has used binary padding to obfuscate payloads.(Citation: Cisco Akira Ransomware OCT 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [Akira](https://attack.mitre.org/groups/G1024) has used legitimate names and locations for files to evade defenses.(Citation: Cisco Akira Ransomware OCT 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [Akira](https://attack.mitre.org/groups/G1024) has used PowerShell scripts for credential harvesting and privilege escalation.(Citation: Cisco Akira Ransomware OCT 2024)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [Akira](https://attack.mitre.org/groups/G1024) uses valid account information to remotely access victim networks, such as VPN credentials.(Citation: Secureworks GOLD SAHARA)(Citation: Arctic Wolf Akira 2023)(Citation: Cisco Akira Ransomware OCT 2024)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102 | Web Service | summary/2026/Threat Report 2026 v4.pdf {"page": 7} Akira and Control - T1102 - Web Service Command and Control - T1219 - Remote Access Tools Command and Control - T1572 - Protocol Tunneling Exfiltration - T1567 - Exfiltration Over Web Service Impact - T1657 - Financial Theft Akira Ransomware Akira ransomware was first observed in the wild in March 2023 a |  |  | 不明 | 不明 | 中 | `source--akira--612fd3b82de9660d` |
| Initial Access, Persistence | T1133 | External Remote Services | [Akira](https://attack.mitre.org/groups/G1024) uses compromised VPN accounts for initial access to victim networks.(Citation: Secureworks GOLD SAHARA) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1213.002 | Sharepoint | [Akira](https://attack.mitre.org/groups/G1024) has accessed and downloaded information stored in SharePoint instances as part of data gathering and exfiltration activity.(Citation: Secureworks GOLD SAHARA) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1219 | Remote Access Tools | [Akira](https://attack.mitre.org/groups/G1024) uses legitimate utilities such as AnyDesk and PuTTy for maintaining remote access to victim environments.(Citation: Secureworks GOLD SAHARA)(Citation: Arctic Wolf Akira 2023) |  |  | 不明 | 不明 | 高 | `source--akira--612fd3b82de9660d`, `source--mitre-attack-19-1` |
| Discovery | T1482 | Domain Trust Discovery | [Akira](https://attack.mitre.org/groups/G1024) uses the built-in [Nltest](https://attack.mitre.org/software/S0359) utility or tools such as [AdFind](https://attack.mitre.org/software/S0552) to enumerate Active Directory trusts in victim environments.(Citation: Arctic Wolf Akira 2023)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1486 | Data Encrypted for Impact | [Akira](https://attack.mitre.org/groups/G1024) encrypts files in victim environments as part of ransomware operations.(Citation: BushidoToken Akira 2023)(Citation: CISA Akira Ransomware APR 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1531 | Account Access Removal | [Akira](https://attack.mitre.org/groups/G1024) deletes administrator accounts in victim networks prior to encryption.(Citation: Secureworks GOLD SAHARA) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1558 | Steal or Forge Kerberos Tickets | [Akira](https://attack.mitre.org/groups/G1024) have used scripts to dump Kerberos authentication credentials.(Citation: Cisco Akira Ransomware OCT 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | [Akira](https://attack.mitre.org/groups/G1024) uses utilities such as WinRAR to archive data prior to exfiltration.(Citation: Secureworks GOLD SAHARA) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567 | Exfiltration Over Web Service | ": 7} Akira and Control - T1102 - Web Service Command and Control - T1219 - Remote Access Tools Command and Control - T1572 - Protocol Tunneling Exfiltration - T1567 - Exfiltration Over Web Service Impact - T1657 - Financial Theft Akira Ransomware Akira ransomware was first observed in the wild in March 2023 and has since emerged as one of the most active and widely de- ployed ransomware families across the global threat landscape. Operating |  |  | 不明 | 不明 | 中 | `source--akira--612fd3b82de9660d` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | [Akira](https://attack.mitre.org/groups/G1024) will exfiltrate victim data using applications such as [Rclone](https://attack.mitre.org/software/S1040).(Citation: Secureworks GOLD SAHARA) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1572 | Protocol Tunneling | mary/2026/Threat Report 2026 v4.pdf {"page": 7} Akira and Control - T1102 - Web Service Command and Control - T1219 - Remote Access Tools Command and Control - T1572 - Protocol Tunneling Exfiltration - T1567 - Exfiltration Over Web Service Impact - T1657 - Financial Theft Akira Ransomware Akira ransomware was first observed in the wild in March 2023 and has since emerged as one of the most active and widely de- ployed ransomware families acr |  |  | 不明 | 不明 | 中 | `source--akira--612fd3b82de9660d` |
| Impact | T1657 | Financial Theft | [Akira](https://attack.mitre.org/groups/G1024) engages in double-extortion ransomware, exfiltrating files then encrypting them, in order to prompt victims to pay a ransom.(Citation: BushidoToken Akira 2023)(Citation: CISA Akira Ransomware APR 2024) |  |  | 不明 | 不明 | 高 | `source--akira--612fd3b82de9660d`, `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | [Akira](https://attack.mitre.org/groups/G1024) has disabled or modified security tools for defense evasion.(Citation: Cisco Akira Ransomware OCT 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 18件
- IOC観測: 20件
- 複数攻撃で観測: 0件
- 要レビュー候補: 16件
- 非IOC artifact観測: 180件（`artifacts.csv`）

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
| source--akira--0010e345a890397c | Dragos 2026 OT Cybersecurity Report A Year in Review |  | 2026 | OT/Dragos-2026-OT-Cybersecurity-Report-A-Year-in-Review.pdf | report | TLP:CLEAR | 中 |
| source--akira--006cc4612e03b47f | 2024 IC3Report |  | 2024 | summary/2025/2024_IC3Report.pdf | report | TLP:CLEAR | 中 |
| source--akira--0628019fb204df48 | annual threat report 2024 |  | 2024 | summary/2025/annual-threat-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--akira--07db6468fd9302b3 | eSentire TRU Report The Industrialization of Cybercrime Identities are Under Attack 2026 |  | 2026 | summary/2026/eSentire_TRU_Report_The-Industrialization-of-Cybercrime-Identities-are-Under-Attack_2026.pdf | report | TLP:CLEAR | 中 |
| source--akira--0e6eb89129aff162 | cybercrime multifaceted national security threat |  | 不明 | summary/2025/cybercrime-multifaceted-national-security-threat.pdf | report | TLP:CLEAR | 中 |
| source--akira--0fe45032204f859a | [Report] Bitsight State of the Underground 2026 |  | 2026 | summary/2026/[Report] Bitsight State of the Underground 2026.pdf | report | TLP:CLEAR | 中 |
| source--akira--15c750a04fa45c17 | Flashpoint 2026 Global Threat Intelligence Report |  | 2026 | summary/2026/Flashpoint_2026_Global_Threat_Intelligence_Report.pdf | report | TLP:CLEAR | 中 |
| source--akira--1a1b03f754d2172b | Global Threat Report 2025 |  | 2025 | summary/2025/Global Threat Report 2025.pdf | report | TLP:CLEAR | 中 |
| source--akira--1cb9d528e50b35ee | 2025 Cyber Security Report Final |  | 2025 | summary/2025/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--akira--27adfa5cb6515962 | Recordedfuture 2023 Annual Report ta 2024 0321 |  | 2023 | summary/2024/Recordedfuture 2023 Annual Report ta-2024-0321.pdf | report | TLP:CLEAR | 中 |
| source--akira--27cb51a35b3bec43 | Semiannual+Ransomware+Report+ +H1+2024 |  | 2024 | cybercrime/2024/Semiannual+Ransomware+Report+-+H1+2024.pdf | report | TLP:CLEAR | 中 |
| source--akira--2b6e6ecd4990de2f | Microsoft Digital Defense Report 2024 |  | 2024 | summary/2024/Microsoft Digital Defense Report 2024.pdf | report | TLP:CLEAR | 中 |
| source--akira--3088fb60e523da28 | Cybersecurity Threats 2024 Mid Year Report |  | 2024 | summary/2024/Cybersecurity Threats 2024 Mid-Year Report.pdf | report | TLP:CLEAR | 中 |
| source--akira--32f65c0bc7e8a84e | MDDR FINAL 2023 1004 |  | 2023-10-04 | summary/2023/MDDR_FINAL_2023_1004.pdf | report | TLP:CLEAR | 中 |
| source--akira--3325725201dc8c60 | CERTFR 2026 CTI 003 |  | 2026 | summary/2026/CERTFR-2026-CTI-003.pdf | report | TLP:CLEAR | 中 |
| source--akira--36aae6f00db529c3 | 2025 dbir data breach investigations report |  | 2025 | summary/2025/2025-dbir-data-breach-investigations-report.pdf | report | TLP:CLEAR | 中 |
| source--akira--36d007865f615629 | CyberProof 2026 Global Threat Intelligence Report |  | 2026 | summary/2026/CyberProof_2026_Global_Threat_Intelligence_Report.pdf | report | TLP:CLEAR | 中 |
| source--akira--38a4f397d065ae6d | UK NCC Group Cyber Threat Intelligence Report September 2025 |  | 2025 | summary/2025/UK_NCC_Group_Cyber_Threat_Intelligence_Report_September_2025_.pdf | report | TLP:CLEAR | 中 |
| source--akira--418d2fa4261239e2 | CERTFR 2025 CTI 004 |  | 2025 | summary/2025/CERTFR-2025-CTI-004.pdf | report | TLP:CLEAR | 中 |
| source--akira--42aad3201fefdae0 | Cloudflare 2026 threat report |  | 2026 | summary/2026/Cloudflare-2026-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--akira--49a673a991a5f187 | 2024 Annual Cybersecurity Vulnerability Threat Landscape Research Report |  | 2024 | summary/2025/2024_Annual_Cybersecurity_Vulnerability_Threat_Landscape_Research_Report.pdf | report | TLP:CLEAR | 中 |
| source--akira--4ad0a6f48bf19b50 | Worldwide Ransomware Attacks as of June 2024 Consistent With Previous Year Sep2024 |  | 2024 | summary/2024/Worldwide_Ransomware_Attacks_as_of_June_2024_Consistent_With_Previous_Year_Sep2024.pdf | report | TLP:CLEAR | 中 |
| source--akira--4b736d62db13a141 | eset threat report h22025 |  | 不明 | summary/2025/eset-threat-report-h22025.pdf | report | TLP:CLEAR | 中 |
| source--akira--514fbc646fc97e62 | Cyber Threat Intelligence Report 2025 2 |  | 2025 | summary/2025/Cyber Threat Intelligence Report 2025 2.pdf | report | TLP:CLEAR | 中 |
| source--akira--51a9a80a40e5b38a | 2023 Network Vulnerability Situation Research Report |  | 2023 | summary/2024/2023 Network Vulnerability Situation Research Report.pdf | report | TLP:CLEAR | 中 |
| source--akira--538a279c502cbba5 | The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities |  | 不明 | International Strategic/Korea/The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities.pdf | report | TLP:CLEAR | 中 |
| source--akira--542d7483eae9b641 | Threat Report 2026 v4 |  | 2026 | summary/2026/Threat Report 2026 v4.pdf | report | TLP:CLEAR | 中 |
| source--akira--568c9a2b36c97964 | 2024 H1 Threat Intel Report Final |  | 2024 | summary/2024/2024-H1-Threat-Intel-Report-Final.pdf | report | TLP:CLEAR | 中 |
| source--akira--58d86e7435abe035 | PL Report CP 2024 |  | 2024 | summary/2025/PL_Report_CP_2024.pdf | report | TLP:CLEAR | 中 |
| source--akira--5b258aa6b988bcdb | readme |  | 不明 | summary/2024/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--akira--5d4c851281b38587 | Year in Review of ZeroDays |  | 不明 | summary/2024/Year_in_Review_of_ZeroDays.pdf | report | TLP:CLEAR | 中 |
| source--akira--5dd0bf7509af3590 | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--akira--6096ad9b7f2a058f | GRIT Ransomware Annual Report 2023 |  | 2023 | summary/2024/GRIT_Ransomware_Annual_Report_2023.pdf | report | TLP:CLEAR | 中 |
| source--akira--612fd3b82de9660d | akira |  | 不明 | actor_profile/evidence/akira.csv | structured-data | TLP:CLEAR | 中 |
| source--akira--6ec6b80b4002a792 | 2025 Cyber Security Report Final |  | 2025 | summary/2026/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--akira--75463246cf0fe661 | 2025 CrowdStrike European Threat Landscape Report |  | 2025 | summary/2025/2025-CrowdStrike-European-Threat-Landscape-Report_.pdf | report | TLP:CLEAR | 中 |
| source--akira--7d5812830952d88f | 2024 Threat Intelligence Annual Report |  | 2024 | summary/2025/2024 Threat Intelligence Annual Report.pdf | report | TLP:CLEAR | 中 |
| source--akira--800af134a98235e6 | 2024YiR report |  | 2024 | summary/2025/2024YiR-report.pdf | report | TLP:CLEAR | 中 |
| source--akira--82ed2309ea8b2680 | managed xdr global threat report |  | 不明 | summary/2026/managed-xdr-global-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--akira--8bae969e58325726 | Bridewell 2026 Cyber Threat Intelligence Report |  | 2026 | summary/2026/Bridewell 2026 Cyber Threat Intelligence Report.pdf | report | TLP:CLEAR | 中 |
| source--akira--98c32bb9a3977abf | eset threat report h12025 |  | 不明 | summary/2025/eset-threat-report-h12025.pdf | report | TLP:CLEAR | 中 |
| source--akira--9bf876aff17c344e | First 6 Half Year Threat Report 2024 |  | 2024 | summary/2024/First 6 Half-Year Threat Report 2024.pdf | report | TLP:CLEAR | 中 |
| source--akira--9e51602583523baa | crowdstrike 2024 threat hunting report |  | 2024 | summary/2024/crowdstrike-2024-threat-hunting-report.pdf | report | TLP:CLEAR | 中 |
| source--akira--a07a0174189cad73 | Microsoft Digital Defense Report 2025 |  | 2025 | summary/2025/Microsoft-Digital-Defense-Report-2025.pdf | report | TLP:CLEAR | 中 |
| source--akira--a07afbfda4fd57e6 | CERTFR 2024 CTI 002 |  | 2024 | summary/2024/CERTFR-2024-CTI-002.pdf | report | TLP:CLEAR | 中 |
| source--akira--a4c2c4f38548d338 | CrowdStrike 2026 Global Threat Report |  | 2026 | summary/2026/CrowdStrike-2026-Global-Threat-Report.pdf | report | TLP:CLEAR | 中 |
| source--akira--a6c9c0cc8f76eac6 | 2024 dbir data breach investigations report |  | 2024 | summary/2024/2024-dbir-data-breach-investigations-report.pdf | report | TLP:CLEAR | 中 |
| source--akira--aabc4ebaab98ede0 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--akira--b3310bf3e8552cd3 | 2025 Global Threat Intelligence Report |  | 2025 | summary/2025/2025 Global Threat Intelligence Report .pdf | report | TLP:CLEAR | 中 |
| source--akira--b9d00c6466436cc2 | rapid7 2024 attack intelligence report |  | 2024 | summary/2024/rapid7_2024_attack_intelligence_report.pdf | report | TLP:CLEAR | 中 |
| source--akira--bb1f08473f70c0dc | Symantec Ransomware Threat Landscape 2024 |  | 2024 | summary/2024/Symantec_Ransomware_Threat_Landscape_2024.pdf | report | TLP:CLEAR | 中 |
| source--akira--bc3cd96a6cfcf450 | national cyber threat assessment 2025 2026 e |  | 不明 | International Strategic/Canada/national-cyber-threat-assessment-2025-2026-e.pdf | report | TLP:CLEAR | 中 |
| source--akira--c28cea4a3fa56026 | CGCYBER 2024 CTIME |  | 2024 | International Strategic/USA/2025/CGCYBER 2024 CTIME.pdf | report | TLP:CLEAR | 中 |
| source--akira--cdc1a83bea8ca73e | 2024 Cyber Threat Report Huntress FINAL |  | 2024 | summary/2024/2024_Cyber_Threat_Report_Huntress_FINAL.pdf | report | TLP:CLEAR | 中 |
| source--akira--d19e3d462720711d | Security Navigator 2026 |  | 2026 | summary/2025/Security_Navigator_2026.pdf | report | TLP:CLEAR | 中 |
| source--akira--d9cd91cce3cfee50 | Cybersecurity Threats 2024 Annual Report QAX |  | 2024 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | report | TLP:CLEAR | 中 |
| source--akira--dc63de875955899e | Norma+Cyber+Annual+Threat+Assessment+ +Spreads |  | 不明 | summary/2024/Norma+Cyber+Annual+Threat+Assessment+-+Spreads.pdf | report | TLP:CLEAR | 中 |
| source--akira--e3e88d8bbef48ddb | 2024 security report |  | 2024 | summary/2024/2024-security-report.pdf | report | TLP:CLEAR | 中 |
| source--akira--f03089def290732f | 2025 IC3Report |  | 2025 | cybercrime/2026/2025_IC3Report.pdf | report | TLP:CLEAR | 中 |
| source--akira--f3b1d62374240b5f | CrowdStrike 2025 Threat Hunting Report |  | 2025 | summary/2025/CrowdStrike 2025 Threat Hunting Report.pdf | report | TLP:CLEAR | 中 |
| source--akira--fb2302896ed07e4f | Dragos 2025 OT Cybersecurity Report A Year in Review |  | 2025 | summary/2025/Dragos-2025-OT-Cybersecurity-Report-A-Year-in-Review.pdf | report | TLP:CLEAR | 中 |
| source--daily-0662aaff581d0ab45bce | 重大なSonicWall SSLVPNバグ、ランサムウェア攻撃に悪用される | bleepingcomputer.com | 2024-09-11 | https://www.bleepingcomputer.com/news/security/critical-sonicwall-sslvpn-bug-exploited-in-ransomware-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-08853165537986c77f7f | Akiraランサムウェア：支払いだけでは匿名性を保てない | suspectfile.com | 2025-06-01 | https://www.suspectfile.com/akira-ransomware-when-paying-isnt-enough-to-stay-anonymous/ | osint-report | TLP:CLEAR | 中 |
| source--daily-251d2ee4d8e5443dd89d | Akiraランサムウェア、MFA保護のSonicWall VPNアカウントを侵害 | bleepingcomputer.com | 2025-09-29 | https://www.bleepingcomputer.com/news/security/akira-ransomware-breaching-mfa-protected-sonicwall-vpn-accounts/ | osint-report | TLP:CLEAR | 中 |
| source--daily-29f74832270318181f72 | AkiraおよびFogランサムウェア、Veeamの重大なリモートコード実行脆弱性を悪用 | bleepingcomputer.com | 2024-10-14 | https://www.bleepingcomputer.com/news/security/akira-and-fog-ransomware-now-exploiting-critical-veeam-rce-flaw/ | osint-report | TLP:CLEAR | 中 |
| source--daily-339537ab2997fa08795e | Akiraランサムウェア攻撃が急増、SonicWallファイアウォールが標的に | bleepingcomputer.com | 2025-08-02 | https://www.bleepingcomputer.com/news/security/surge-of-akira-ransomware-attacks-hits-sonicwall-firewall-devices/ | osint-report | TLP:CLEAR | 中 |
| source--daily-3c12eda093e5c59e0ee6 | FogランサムウェアがSonicWall VPNを標的に企業ネットワークに侵入 | bleepingcomputer.com | 2024-10-28 | https://www.bleepingcomputer.com/news/security/fog-ransomware-targets-sonicwall-vpns-to-breach-corporate-networks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-48e314e2ec6d02091f74 | CISA、Nutanix VMを狙うAkiraランサムウェアのLinux暗号化器に警告 | bleepingcomputer.com | 2025-11-15 | https://www.bleepingcomputer.com/news/security/cisa-warns-of-akira-ransomware-linux-encryptor-targeting-nutanix-vms/ | osint-report | TLP:CLEAR | 中 |
| source--daily-4ccacc67cc78bb4bfd28 | SonicWall、SSLVPNゼロデイ否定　2024年既知脆弱性悪用とAkiraランサム攻撃関連を確認 | bleepingcomputer.com | 2025-08-08 | https://www.bleepingcomputer.com/news/security/sonicwall-finds-no-sslvpn-zero-day-links-ransomware-attacks-to-2024-flaw/ | osint-report | TLP:CLEAR | 中 |
| source--daily-4e4cc7628ff86fb403b4 | AkiraランサムウェアがCPUチューニングツールを悪用しMicrosoft Defenderを無効化 | bleepingcomputer.com | 2025-08-07 | https://www.bleepingcomputer.com/news/security/akira-ransomware-abuses-cpu-tuning-tool-to-disable-microsoft-defender/ | osint-report | TLP:CLEAR | 中 |
| source--daily-73166036d74c23fae026 | トロント動物園、昨年のランサムウェア攻撃に関する最新情報を共有 | bleepingcomputer.com | 2025-03-06 | https://www.bleepingcomputer.com/news/security/toronto-zoo-shares-update-on-last-years-ransomware-attack/ | osint-report | TLP:CLEAR | 中 |
| source--daily-7fac464b25387fdb006e | Hitachi Vantara、Akiraランサムウェア攻撃後にサーバーをオフライン化 | bleepingcomputer.com | 2025-04-29 | https://www.bleepingcomputer.com/news/security/hitachi-vantara-takes-servers-offline-after-akira-ransomware-attack/ | osint-report | TLP:CLEAR | 中 |
| source--daily-89a8fc15ce47bbec4793 | FBI: Akiraランサムウェア、250社以上から4200万ドルを詐取 | bleepingcomputer.com | 2024-04-19 | https://www.bleepingcomputer.com/news/security/fbi-akira-ransomware-raked-in-42-million-from-250-plus-victims/ | osint-report | TLP:CLEAR | 中 |
| source--daily-a0023564f914d51f566d | 被害者が支払いをやめたことで、ランサムウェアの利益が減少 | bleepingcomputer.com | 2025-10-28 | https://www.bleepingcomputer.com/news/security/ransomware-profits-drop-as-victims-stop-paying-hackers/ | osint-report | TLP:CLEAR | 中 |
| source--daily-c6a57e3d4fd20c381ed8 | Akiraランサムウェア、SonicWall SSLVPNの重大バグを再悪用 | bleepingcomputer.com | 2025-09-12 | https://www.bleepingcomputer.com/news/security/akira-ransomware-exploiting-critical-sonicwall-sslvpn-bug-again/ | osint-report | TLP:CLEAR | 中 |
| source--daily-efcfda27f495de5d5c60 | Apache OpenOffice、ランサムウェア集団のデータ侵害主張に反論 | bleepingcomputer.com | 2025-11-06 | https://www.bleepingcomputer.com/news/security/apache-openoffice-disputes-data-breach-claims-by-ransomware-gang/ | osint-report | TLP:CLEAR | 中 |
| source--daily-f08faf92c2b925e530ef | GPUを活用したAkiraランサムウェアの復号ツールがGitHubで公開 | bleepingcomputer.com | 2025-03-17 | https://www.bleepingcomputer.com/news/security/gpu-powered-akira-ransomware-decryptor-released-on-github/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
