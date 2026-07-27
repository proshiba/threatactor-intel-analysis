# FIN7 脅威アクタープロファイル

- プロファイルID: `actor--fin7`
- 状態: draft
- 更新日時: 2026-07-27T11:04:31Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

FIN7の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **FIN7**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Carbon Spider | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| ELBRUS | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| GOLD NIAGARA | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| ITG14 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Sangria Tempest | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Carbanak | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Russia row 8; mapping requires review. |
| Anunak | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook Russia row 8; mapping requires review. |

## 帰属

The repository mapping workbook places this actor in the Russia worksheet.

- 国: Russia
- スポンサー種別: state
- 確度: 中
- 証拠: `source--actor-mapping-workbook`

## モチベーション

未評価

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Sangria Tempest | overlaps-with | 共有alias: Carbon Spider, ELBRUS, FIN7, Sangria Tempest | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |
| Carbanak | related-to | FIN7 may be linked to the [Carbanak](https://attack.mitre.org/groups/G0008) Group, but multiple threat groups have been observed using [Carbanak](https://attack.mitre.org/software/S0030), leading these groups to be tracked separately.(Citation: FireEye FIN7 March 2017)(Citation: FireEye FIN7 April 2017)(Citation: FireEye CARBANAK June 2017)(Citation: FireEye FIN7 Aug 2018)(Citation: CrowdStrike Carbon Spider August 2021)(Citation: Mandiant FIN7 Apr 2022)(Citation: BiZone Lizar May 2021) | 中 | `source--mitre-attack-19-1` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [FIN7](https://attack.mitre.org/groups/G0046) is a financially-motivated threat group that has been active since 2013. [FIN7](https://attack.mitre.org/groups/G0046) has targeted the retail, restaurant, hospitality, software, consulting, financial services, medical equipment, cloud services, media, food and beverage, transportation, pharmaceutical, and utilities industries in the United States. A portion of [FIN7](https://attack.mitre.org/groups/G0046) was operated out of a front company called Combi Security and often used point-of-sale malware for targeting efforts. Since 2020, [FIN7](https://attack.mitre.org/groups/G0046) shifted operations to big game hunting (BGH), including use of [REvil](https://attack.mitre.org/software/S0496) ransomware and their own Ransomware-as-a-Service (RaaS), Darkside. FIN7 may be linked to the [Carbanak](https://attack.mitre.org/groups/G0008) Group, but multiple threat groups have been observed using [Carbanak](https://attack.mitre.org/software/S0030), leading these groups to be tracked separately.(Citation: FireEye FIN7 March 2017)(Citation: FireEye FIN7 April 2017)(Citation: FireEye CARBANAK June 2017)(Citation: FireEye FIN7 Aug 2018)(Citation: CrowdStrike Carbon Spider August 2021)(Citation: Mandiant FIN7 Apr 2022)(Citation: BiZone Lizar May 2021) |
| Capability | GRIFFON, RDFSNIFFER, HALFBAKED, POWERSOURCE, SystemBC, TEXTMATE, BOOSTWRITE, Carbanak, SQLRat, Cobalt Strike, REvil, Pillowmint, Maze, JSS Loader, Lizar, PowerSploit, Mimikatz, CrackMapExec, AdFind |
| Infrastructure |  |
| Victim | Bank of Valetta, Malta |
| Socio-political | Russia |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Carbanak, Anunak | multiple-name-intersection | 高 | Ukraine | https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08064518/Carbanak_APT_eng.pdf<br>https://www.group-ib.com/resources/threat-research/Anunak_APT_against_financial_institutions.pdf<br>https://www.bitdefender.com/files/News/CaseStudies/study/262/Bitdefender-WhitePaper-An-APT-Blueprint-Gaining-New-Visibility-into-Financial-Threats-interactive.pdf |
| etda-threat-group-cards | FIN7 | canonical-name | 高 | Russia | https://www.fireeye.com/blog/threat-research/2018/08/fin7-pursuing-an-enigmatic-and-evasive-global-criminal-operation.html<br>https://atr-blog.gigamon.com/2017/07/25/footprints-of-fin7-tracking-actor-patterns-part-1<br>https://atr-blog.gigamon.com/2017/07/26/footprints-of-fin7-tracking-actor-patterns-part-2 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Sangria Tempest | multiple-name-intersection | 高 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | FIN7 | canonical-name | 高 | RU | https://en.wikipedia.org/wiki/Carbanak<br>https://app.box.com/s/p7qzcury97tuwk26694uutujwqmwqyhe<br>http://2014.zeronights.ru/assets/files/slides/ivanovb-zeronights.pdf |
| misp-microsoft-activity-group | Sangria Tempest | canonical-name | 高 | UA | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | FIN7 - G0046 | mitre-external-id | 高 |  | https://attack.mitre.org/wiki/Group/G0046<br>https://www.fireeye.com/blog/threat-research/2017/03/fin7%20spear%20phishing.html<br>https://www.fireeye.com/blog/threat-research/2017/04/fin7-phishing-lnk.html |
| misp-mitre-enterprise-intrusion-set | Carbanak - G0008 | multiple-name-intersection | 高 |  | https://attack.mitre.org/wiki/Group/G0008<br>https://securelist.com/files/2015/02/Carbanak%20APT%20eng.pdf<br>https://www.fireeye.com/blog/threat-research/2017/04/fin7-phishing-lnk.html |
| misp-mitre-intrusion-set | Carbanak - G0008 | multiple-name-intersection | 高 |  | https://attack.mitre.org/groups/G0008<br>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08064518/Carbanak_APT_eng.pdf<br>https://www.europol.europa.eu/newsroom/news/mastermind-behind-eur-1-billion-cyber-bank-robbery-arrested-in-spain |
| misp-mitre-intrusion-set | FIN7 - G0046 | mitre-external-id | 高 |  | http://blog.morphisec.com/fin7-attacks-restaurant-industry<br>https://attack.mitre.org/groups/G0046<br>https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319 |
| misp-360net | Carbanak - APT-C-11 | single-alias-intersection | 中 | Ukraine | https://apt.360.net/report/apts/68.html |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Carbanak | similar | misp-mitre-enterprise-intrusion-set | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| FIN7 | similar | misp-mitre-enterprise-intrusion-set | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--boostwrite | BOOSTWRITE | [BOOSTWRITE](https://attack.mitre.org/software/S0415) is a loader crafted to be launched via abuse of the DLL search order of applications used by [FIN7](https://attack.mitre.org/groups/G0046).(Citation: FireEye FIN7 Oct 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--carbanak | Carbanak | [Carbanak](https://attack.mitre.org/software/S0030) is a full-featured, remote backdoor used by a group of the same name ([Carbanak](https://attack.mitre.org/groups/G0008)). It is intended for espionage, data exfiltration, and providing remote access to infected machines. (Citation: Kaspersky Carbanak) (Citation: FireEye CARBANAK June 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--cobalt-strike | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) is a commercial, full-featured, remote access tool that bills itself as “adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors”. Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.(Citation: cobaltstrike manual)<br><br>In addition to its own capabilities, [Cobalt Strike](https://attack.mitre.org/software/S0154) leverages the capabilities of other well-known tools such as Metasploit and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: cobaltstrike manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--griffon | GRIFFON | [GRIFFON](https://attack.mitre.org/software/S0417) is a JavaScript backdoor used by [FIN7](https://attack.mitre.org/groups/G0046). (Citation: SecureList Griffon May 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--halfbaked | HALFBAKED | [HALFBAKED](https://attack.mitre.org/software/S0151) is a malware family consisting of multiple components intended to establish persistence in victim networks. (Citation: FireEye FIN7 April 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--jss-loader | JSS Loader | [JSS Loader](https://attack.mitre.org/software/S0648) is Remote Access Trojan (RAT) with .NET and C++ variants that has been used by [FIN7](https://attack.mitre.org/groups/G0046) since at least 2020.(Citation: eSentire FIN7 July 2021)(Citation: CrowdStrike Carbon Spider August 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--lizar | Lizar | [Lizar](https://attack.mitre.org/software/S0681) is a modular remote access tool written using the .NET Framework that shares structural similarities to [Carbanak](https://attack.mitre.org/software/S0030). It has likely been used by [FIN7](https://attack.mitre.org/groups/G0046) since at least February 2021.(Citation: BiZone Lizar May 2021)(Citation: Threatpost Lizar May 2021)(Citation: Gemini FIN7 Oct 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--maze | Maze | [Maze](https://attack.mitre.org/software/S0449) ransomware, previously known as "ChaCha", was discovered in May 2019. In addition to encrypting files on victim machines for impact, [Maze](https://attack.mitre.org/software/S0449) operators conduct information stealing campaigns prior to encryption and post the information online to extort affected companies.(Citation: FireEye Maze May 2020)(Citation: McAfee Maze March 2020)(Citation: Sophos Maze VM September 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--pillowmint | Pillowmint | [Pillowmint](https://attack.mitre.org/software/S0517) is a point-of-sale malware used by [FIN7](https://attack.mitre.org/groups/G0046) designed to capture credit card information.(Citation: Trustwave Pillowmint June 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--powersource | POWERSOURCE | [POWERSOURCE](https://attack.mitre.org/software/S0145) is a PowerShell backdoor that is a heavily obfuscated and modified version of the publicly available tool DNS_TXT_Pwnage. It was observed in February 2017 in spearphishing campaigns against personnel involved with United States Securities and Exchange Commission (SEC) filings at various organizations. The malware was delivered when macros were enabled by the victim and a VBS script was dropped. (Citation: FireEye FIN7 March 2017) (Citation: Cisco DNSMessenger March 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--rdfsniffer | RDFSNIFFER | [RDFSNIFFER](https://attack.mitre.org/software/S0416) is a module loaded by [BOOSTWRITE](https://attack.mitre.org/software/S0415) which allows an attacker to monitor and tamper with legitimate connections made via an application designed to provide visibility and system management capabilities to remote IT techs.(Citation: FireEye FIN7 Oct 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--revil | REvil | [REvil](https://attack.mitre.org/software/S0496) is a ransomware family that has been linked to the [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) group and operated as ransomware-as-a-service (RaaS) since at least April 2019. [REvil](https://attack.mitre.org/software/S0496), which as been used against organizations in the manufacturing, transportation, and electric sectors, is highly configurable and shares code similarities with the GandCrab RaaS.(Citation: Secureworks REvil September 2019)(Citation: Intel 471 REvil March 2020)(Citation: Group IB Ransomware May 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--sqlrat | SQLRat | [SQLRat](https://attack.mitre.org/software/S0390) is malware that executes SQL scripts to avoid leaving traditional host artifacts. [FIN7](https://attack.mitre.org/groups/G0046) has been observed using it.(Citation: Flashpoint FIN 7 March 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--systembc | SystemBC | [SystemBC](https://attack.mitre.org/software/S9001) is a malware family offered as a malware-as-a-service (MaaS) that is used to establish command and control and facilitate follow-on activity, including ransomware deployment.[SystemBC](https://attack.mitre.org/software/S9001) executes a variety of tasks including setting up SOCKS5 proxies, maintaining persistence, ingesting malicious files, and handing C2 communication. [SystemBC](https://attack.mitre.org/software/S9001) was first detected in 2018, and has been used by [Wizard Spider](https://attack.mitre.org/groups/G0102) since at least 2020, and by [FIN7](https://attack.mitre.org/groups/G0046) since at least 2022.(Citation: TrumanKroll_SYSTEMBCServer_Jan2024)(Citation: SophosGnGal_SystemBC_Dec2020)(Citation: BlackBasta)(Citation: AhnLab_SystemBC_Apr2022)(Citation: Lumen_SystemBC_Sept2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--textmate | TEXTMATE | [TEXTMATE](https://attack.mitre.org/software/S0146) is a second-stage PowerShell backdoor that is memory-resident. It was observed being used along with [POWERSOURCE](https://attack.mitre.org/software/S0145) in February 2017. (Citation: FireEye FIN7 March 2017) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--powersploit | PowerSploit | [PowerSploit](https://attack.mitre.org/software/S0194) is an open source, offensive security framework comprised of [PowerShell](https://attack.mitre.org/techniques/T1059/001) modules and scripts that perform a wide range of tasks related to penetration testing such as code execution, persistence, bypassing anti-virus, recon, and exfiltration. (Citation: GitHub PowerSploit May 2012) (Citation: PowerShellMagazine PowerSploit July 2014) (Citation: PowerSploit Documentation) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--crackmapexec | CrackMapExec | [CrackMapExec](https://attack.mitre.org/software/S0488), or CME, is a post-exploitation tool developed in Python and designed for penetration testing against networks. [CrackMapExec](https://attack.mitre.org/software/S0488) collects Active Directory information to conduct lateral movement through targeted networks.(Citation: CME Github September 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--adfind | AdFind | [AdFind](https://attack.mitre.org/software/S0552) is a free command-line query tool that can be used for gathering information from Active Directory.(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: FireEye FIN6 Apr 2019)(Citation: FireEye Ryuk and Trickbot January 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| FIN7ハッカーグループ、悪意あるGoogle広告を使ってNetSupport RATを配布 | malware-campaign | 不明 | 不明 | 2024-05-13 | FIN7がGoogle広告を通じてNetSupport RATを配布 有名ブランドを装った広告によるマルウェア感染が確認 攻撃対象には企業ユーザーが含まれる FIN7は以前から金銭目的のサイバー攻撃を行っている Microsoftはセキュリティ機能を強化し、MSIXプロトコルを無効に | 高 | `source--daily-828f9038762b7cf5681e` |
| FIN7ハッカー、ディープフェイクヌード生成サイトを使いマルウェアを拡散 | malware-campaign | 不明 | 不明 | 2024-10-03 | FIN7が偽のディープフェイクヌード生成サイトを利用し、情報窃取マルウェアを拡散。 これらのサイトは、服を着た人の写真から偽のヌードバージョンを作成すると主張しており、ディープフェイクヌードの生成に関心のある人々にとってのハニーポットとして機能。 ユーザーが写真をアップロードすると、ダウンロード可能な生成画像へのリンクが表示。 しかし実際には、ダウンロードしたアーカイブには、Lumma StealerやRedline Stealerが含まれており感染させる。 これらのマルウェアはブラウザの認証情報や暗号通貨ウォレットを盗む。 | 高 | `source--daily-807d3e4b47434ad13a7f` |
| FIN7、Anubisバックドアを展開し、SharePoint経由でWindowsシステムを乗っ取り | malware-campaign | 不明 | 不明 | 2025-04-03 | 金銭目的の脅威アクターFIN7が、Pythonベースのバックドア「Anubis」を使用してWindowsシステムへのリモートアクセスを確立。 Anubisは、被害者を誘導して、侵害されたSharePointサイト上のペイロードを実行させるマルスパムキャンペーンで拡散。 感染はZIPアーカイブ内のPythonスクリプトから始まり、メモリ内で難読化されたペイロードを復号・実行。 バックドアは、Base64エンコードされたTCPソケット通信を介してリモートサーバーと通信し、システム操作を実行。 攻撃者は、キーロギング、スクリーンショット取得、パスワード窃取などの操作を、被害者のシステム上に直接ツールを保存せずに実行可能。 | 高 | `source--daily-aa4ff1b6006e51c3ed82` |
| 研究者がFIN7サイバー犯罪グループに関連する新たなインフラを発見 | infrastructure-operation | 不明 | 不明 | 2024-08-20 | FIN7サイバー犯罪グループに関連する新たなインフラが発見された。 発見されたインフラはロシアやエストニアのサービスプロバイダーから提供されていた。 Stark Industriesの再販業者からのインフラ購入が推測されている。 Starkは、このインフラがFIN7によるものであるとSilent Pushが発見した後にテイクダウンした。 FIN7は金銭目的のサイバー犯罪グループ。 | 高 | `source--daily-69aca35bec8446690e17` |
| FIN7、FIN8などがRagnar Loaderを使用して持続的アクセスとランサムウェア攻撃を実行 | ransomware-extortion | 不明 | 不明 | 2025-03-08 | 脅威ハンターたちは、Ragnar Loaderと呼ばれる「洗練された進化するマルウェアツールキット」が、Ragnar Locker（別名Monstrous Mantis）、FIN7、FIN8、Ruthless Mantis（元REvil）などのサイバー犯罪およびランサムウェアグループによって使用されていることを明らかにした。 Ragnar Loaderは、侵害されたシステムへの持続的なアクセスを維持し、攻撃者が長期間にわたってネットワーク内に滞在するのを支援する重要な役割を果たしている。 このマルウェアは、PowerShellベースのペイロードを使用し、RC4やBase64などの強力な暗号化とエンコード手法を組み込み、プロセスインジェクション戦略を活用して、検出を回避し、侵害されたシステム上でのステルスな制御を維持している。 Ragnar Loaderは、リバースシェル、ローカル特権昇格、リモートデスクトップアクセスを容易にする複数のコンポーネントを含むアーカイブファイルパッケージとしてアフィリエイトに提供されている。 このマルウェアは、DLLプラグインやシェルコードを実行し、任意のファイルの内容を読み取り、持ち出す能力を持ち、ネットワーク内での横方向の移動を可能にするために、別のPowerShellベースのピボットファイルを使用している。 | 高 | `source--daily-070fa8287bb523515401` |
| FIN7がアメリカの自動車メーカーのITスタッフをフィッシング攻撃で標的に | phishing-campaign | 不明 | 不明 | 2024-04-19 | FIN7がアメリカの大手自動車メーカーのITスタッフを標的にした 攻撃は権限の大きい従業員を標的にし、スピアフィッシングメールでAnunakバックドアを配布 電子メール内には、Advanced IP Scannerになりすました悪意のあるURLがあり、アクセスすると正規のインストーラを装ったWsTaskLoad.exeのインストールが求められる。 攻撃は最初に感染したホストにとどまり、ネットワーク内の別システムへ感染は拡大しなかった BlackBerryによる分析でFIN7の特有の「PowerTrash」難読化ツールを利用したPowerShellスクリプトが使用されていたことが判明 | 高 | `source--daily-be6e9936378029a65c65` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | Finance | Targeting text indicates the Finance sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Collection | T1005 | Data from Local System | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1008 | Fallback Channels | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.004 | SSH | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.005 | VNC | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.010 | Command Obfuscation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.016 | Junk Code Insertion | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.004 | Masquerade Task or Service | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059 | Command and Scripting Interpreter | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.007 | JavaScript | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1069.002 | Domain Groups | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.004 | DNS | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.003 | Local Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Lateral Movement | T1091 | Replication Through Removable Media | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102.002 | Bidirectional Communication | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1113 | Screen Capture | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1124 | System Time Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1125 | Video Capture | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1195.002 | Compromise Software Supply Chain | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1200 | Hardware Additions | доступ к инфраструктуре жертв через наборы эксплоитов. Например, опера - торы ZLoader использовали Spelevo EK, а с Dridex – набор Rig EK. • Hardware additions T1200 В 2021 году группировка FIN7 продолжила проводить атаки типа BadUSB для заражения компьютеров в корпоративной среде, отправляя посылки через почтовую службу США и логистическую компанию UPS. Отправителями значились Министерство здраво - охранени |  |  | 不明 | 不明 | 中 | `source--fin7--6269b5f18e206dc0` |
| Execution | T1204.001 | Malicious Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1210 | Exploitation of Remote Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.005 | Mshta | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.011 | Rundll32 | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1219 | Remote Access Tools | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1486 | Data Encrypted for Impact | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery, Stealth | T1497.002 | User Activity Based Checks | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1546.011 | Application Shimming | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1553.002 | Code Signing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1558.003 | Kerberoasting | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1559.002 | Dynamic Data Exchange | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.001 | Hidden Files and Directories | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.003 | Hidden Window | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1569.002 | Service Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1571 | Non-Standard Port | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1572 | Protocol Tunneling | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.006 | Web Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1591 | Gather Victim Org Information | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1591.004 | Identify Roles | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.001 | Upload Malware | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.004 | Drive-by Target | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.005 | Link Target | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1620 | Reflective Code Loading | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1674 | Input Injection | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1686 | Disable or Modify System Firewall | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 24件
- IOC観測: 37件
- 複数攻撃で観測: 0件
- 要レビュー候補: 22件
- 非IOC artifact観測: 123件（`artifacts.csv`）

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
| source--daily-070fa8287bb523515401 | FIN7、FIN8などがRagnar Loaderを使用して持続的アクセスとランサムウェア攻撃を実行 | thehackernews.com | 2025-03-08 | https://thehackernews.com/2025/03/fin7-fin8-and-others-use-ragnar-loader.html | osint-report | TLP:CLEAR | 中 |
| source--daily-69aca35bec8446690e17 | 研究者がFIN7サイバー犯罪グループに関連する新たなインフラを発見 | thehackernews.com | 2024-08-20 | https://thehackernews.com/2024/08/researchers-uncover-new-infrastructure.html | osint-report | TLP:CLEAR | 中 |
| source--daily-807d3e4b47434ad13a7f | FIN7ハッカー、ディープフェイクヌード生成サイトを使いマルウェアを拡散 | bleepingcomputer.com | 2024-10-03 | https://www.bleepingcomputer.com/news/security/fin7-hackers-launch-deepfake-nude-generator-sites-to-spread-malware/ | osint-report | TLP:CLEAR | 中 |
| source--daily-828f9038762b7cf5681e | FIN7ハッカーグループ、悪意あるGoogle広告を使ってNetSupport RATを配布 | thehackernews.com | 2024-05-13 | https://thehackernews.com/2024/05/fin7-hacker-group-leverages-malicious.html | osint-report | TLP:CLEAR | 中 |
| source--daily-aa4ff1b6006e51c3ed82 | FIN7、Anubisバックドアを展開し、SharePoint経由でWindowsシステムを乗っ取り | thehackernews.com | 2025-04-03 | https://thehackernews.com/2025/04/fin7-deploys-anubis-backdoor-to-hijack.html | osint-report | TLP:CLEAR | 中 |
| source--daily-be6e9936378029a65c65 | FIN7がアメリカの自動車メーカーのITスタッフをフィッシング攻撃で標的に | bleepingcomputer.com | 2024-04-19 | https://www.bleepingcomputer.com/news/security/fin7-targets-american-automakers-it-staff-in-phishing-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--fin7--107844072f44ce60 | m trends 2024 |  | 2024 | summary/2024/m-trends-2024.pdf | report | TLP:CLEAR | 中 |
| source--fin7--110e114ede691889 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--fin7--1828efa6389ef741 | rpt mtrends 2021 fireeye |  | 2021 | summary/2021/rpt-mtrends-2021-fireeye.pdf | report | TLP:CLEAR | 中 |
| source--fin7--18f2bf4192e979ae | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--fin7--2764defe5f58cc0d | eset threat report t12021 |  | 不明 | summary/2021/eset_threat_report_t12021.pdf | report | TLP:CLEAR | 中 |
| source--fin7--2d7d68548d69052d | 2022 Global Threat Report |  | 2022 | summary/2022/2022 Global Threat Report.pdf | report | TLP:CLEAR | 中 |
| source--fin7--2dcfc9dec52c66b3 | Qianxin 2023 APT Report |  | 2023 | summary/2024/Qianxin 2023 APT Report.pdf | report | TLP:CLEAR | 中 |
| source--fin7--2e3aa08fef4ef108 | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--fin7--41743a16d7fa28c6 | Cybersecurity Threats 2024 Mid Year Report |  | 2024 | summary/2024/Cybersecurity Threats 2024 Mid-Year Report.pdf | report | TLP:CLEAR | 中 |
| source--fin7--4570684f18fda842 | 2024 dbir data breach investigations report |  | 2024 | summary/2024/2024-dbir-data-breach-investigations-report.pdf | report | TLP:CLEAR | 中 |
| source--fin7--4edeca1fc488b0c2 | Symantec Ransomware Threat Landscape 2024 |  | 2024 | summary/2024/Symantec_Ransomware_Threat_Landscape_2024.pdf | report | TLP:CLEAR | 中 |
| source--fin7--51e0fe44fd174522 | CERTFR 2025 CTI 004 |  | 2025 | summary/2025/CERTFR-2025-CTI-004.pdf | report | TLP:CLEAR | 中 |
| source--fin7--6269b5f18e206dc0 | fin7 |  | 不明 | actor_profile/evidence/fin7.csv | structured-data | TLP:CLEAR | 中 |
| source--fin7--676b6dca5e973dcf | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--fin7--6ab74598afb38761 | 2021 Adversary Infrastructure Report |  | 2021 | summary/2022/2021 Adversary Infrastructure Report.pdf | report | TLP:CLEAR | 中 |
| source--fin7--6ca6b137249a1c8c | 2025 Year in Review  Malicious Infrastructure |  | 2025 | summary/2026/2025 Year in Review- Malicious Infrastructure.pdf | report | TLP:CLEAR | 中 |
| source--fin7--6eef167de2f527b5 | Adversary Infrastructure Report 2020 |  | 2020 | summary/2021/Adversary Infrastructure Report 2020.pdf | report | TLP:CLEAR | 中 |
| source--fin7--7644b2b34d42fe72 | README |  | 不明 | README.md | repository-notes | TLP:CLEAR | 中 |
| source--fin7--78877058ace07789 | README |  | 不明 | International Strategic/Iran/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--fin7--7b5988769e592772 | Cyber Threat Intelligence Report 2025 2 |  | 2025 | summary/2025/Cyber Threat Intelligence Report 2025 2.pdf | report | TLP:CLEAR | 中 |
| source--fin7--7dafdc7b042db352 | Bridewell 2026 Cyber Threat Intelligence Report |  | 2026 | summary/2026/Bridewell 2026 Cyber Threat Intelligence Report.pdf | report | TLP:CLEAR | 中 |
| source--fin7--7f8fb2c54b55ed83 | M Trends 2023 Report MANDIANT SPECIAL REPORT |  | 2023 | summary/2023/M-Trends 2023 Report MANDIANT SPECIAL REPORT.pdf | report | TLP:CLEAR | 中 |
| source--fin7--8d69ed1215104525 | The CrowdStrike 2021 Global Threat Report |  | 2021 | summary/2021/The CrowdStrike 2021 Global Threat Report.pdf | report | TLP:CLEAR | 中 |
| source--fin7--94a569e834cd69b0 | Global APT 2023 Mid Year Report QIANXIN |  | 2023 | summary/2023/Global APT 2023 Mid-Year Report-QIANXIN.pdf | report | TLP:CLEAR | 中 |
| source--fin7--9b0b2fe0b0830f30 | 2025 CrowdStrike European Threat Landscape Report |  | 2025 | summary/2025/2025-CrowdStrike-European-Threat-Landscape-Report_.pdf | report | TLP:CLEAR | 中 |
| source--fin7--a4453b3cc38477c8 | hunting cobaltstrike beacons in the dark |  | 不明 | APT-hunting/hunting-cobaltstrike-beacons-in-the-dark.pdf | report | TLP:CLEAR | 中 |
| source--fin7--a6a293a235338d5d | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--fin7--b122d20c8bc9a8c0 | Automating APT Campaign and Group Attribution |  | 不明 | APT-hunting/Automating APT Campaign and Group Attribution.pdf | report | TLP:CLEAR | 中 |
| source--fin7--b63faeb56c04a1b1 | 2025 dbir data breach investigations report |  | 2025 | summary/2025/2025-dbir-data-breach-investigations-report.pdf | report | TLP:CLEAR | 中 |
| source--fin7--c19058160144d9af | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--fin7--c1adcb692ae7988b | 2022 Yearbook of APT group Analysis |  | 2022 | summary/2023/2022 Yearbook of APT group Analysis.pdf | report | TLP:CLEAR | 中 |
| source--fin7--c5c8cf1c411135cd | PWC cyber threats 2019 retrospect |  | 2019 | summary/2020/PWC-cyber-threats-2019-retrospect.pdf | report | TLP:CLEAR | 中 |
| source--fin7--d8c875b95bbf19a4 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--fin7--e68f22a37c00b2e9 | readme |  | 不明 | summary/2024/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--fin7--ed0253ea38e187d8 | ESET Threat Report Q22020 |  | 不明 | summary/2020/ESET_Threat_Report_Q22020.pdf | report | TLP:CLEAR | 中 |
| source--fin7--ed94b2ded2a735c9 | 2023 Network Vulnerability Situation Research Report |  | 2023 | summary/2024/2023 Network Vulnerability Situation Research Report.pdf | report | TLP:CLEAR | 中 |
| source--fin7--f9a7e0814c561d14 | Cybersecurity Threats 2024 Annual Report QAX |  | 2024 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-360net | MISP Galaxy 360.net Threat Actors | MISP Project / 360 Netlab | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
