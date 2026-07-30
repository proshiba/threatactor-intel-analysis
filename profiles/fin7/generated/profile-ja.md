# FIN7 脅威アクタープロファイル

- プロファイルID: `actor--fin7`
- 状態: draft
- 更新日時: 2026-07-29T23:13:54Z
- 構造バージョン: 1.1.0

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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FIN7ハッカーグループ、悪意あるGoogle広告を使ってNetSupport RATを配布 | malware-campaign | 不明 | 不明 | 2024-05-13 |  |  |  |  | FIN7がGoogle広告を通じてNetSupport RATを配布 有名ブランドを装った広告によるマルウェア感染が確認 攻撃対象には企業ユーザーが含まれる FIN7は以前から金銭目的のサイバー攻撃を行っている Microsoftはセキュリティ機能を強化し、MSIXプロトコルを無効に | 高 | `source--daily-828f9038762b7cf5681e` |
| FIN7ハッカー、ディープフェイクヌード生成サイトを使いマルウェアを拡散 | malware-campaign | 不明 | 不明 | 2024-10-03 |  |  |  |  | FIN7が偽のディープフェイクヌード生成サイトを利用し、情報窃取マルウェアを拡散。 これらのサイトは、服を着た人の写真から偽のヌードバージョンを作成すると主張しており、ディープフェイクヌードの生成に関心のある人々にとってのハニーポットとして機能。 ユーザーが写真をアップロードすると、ダウンロード可能な生成画像へのリンクが表示。 しかし実際には、ダウンロードしたアーカイブには、Lumma StealerやRedline Stealerが含まれており感染させる。 これらのマルウェアはブラウザの認証情報や暗号通貨ウォレットを盗む。 | 高 | `source--daily-807d3e4b47434ad13a7f` |
| FIN7、Anubisバックドアを展開し、SharePoint経由でWindowsシステムを乗っ取り | malware-campaign | 不明 | 不明 | 2025-04-03 |  |  | ttp--activity-rule--85ff7043ed59c3428534, ttp--activity-rule--cedd0a0b2316fd50d056, ttp--activity-rule--d1e93bd0a09f55baffe6, ttp--activity-rule--f9daa094c8fa810e7348 | victim--activity-rule--af41f8144a4af28ced06 | 金銭目的の脅威アクターFIN7が、Pythonベースのバックドア「Anubis」を使用してWindowsシステムへのリモートアクセスを確立。 Anubisは、被害者を誘導して、侵害されたSharePointサイト上のペイロードを実行させるマルスパムキャンペーンで拡散。 感染はZIPアーカイブ内のPythonスクリプトから始まり、メモリ内で難読化されたペイロードを復号・実行。 バックドアは、Base64エンコードされたTCPソケット通信を介してリモートサーバーと通信し、システム操作を実行。 攻撃者は、キーロギング、スクリーンショット取得、パスワード窃取などの操作を、被害者のシステム上に直接ツールを保存せずに実行可能。 | 高 | `source--daily-aa4ff1b6006e51c3ed82` |
| 研究者がFIN7サイバー犯罪グループに関連する新たなインフラを発見 | infrastructure-operation | 不明 | 不明 | 2024-08-20 |  |  |  |  | FIN7サイバー犯罪グループに関連する新たなインフラが発見された。 発見されたインフラはロシアやエストニアのサービスプロバイダーから提供されていた。 Stark Industriesの再販業者からのインフラ購入が推測されている。 Starkは、このインフラがFIN7によるものであるとSilent Pushが発見した後にテイクダウンした。 FIN7は金銭目的のサイバー犯罪グループ。 | 高 | `source--daily-69aca35bec8446690e17` |
| FIN7、FIN8などがRagnar Loaderを使用して持続的アクセスとランサムウェア攻撃を実行 | ransomware-extortion | 不明 | 不明 | 2025-03-08 |  | malware--revil | ttp--activity-rule--7d77bae4a556494c0709 | victim--activity-rule--948a0bf7f29632afb7d4 | 脅威ハンターたちは、Ragnar Loaderと呼ばれる「洗練された進化するマルウェアツールキット」が、Ragnar Locker（別名Monstrous Mantis）、FIN7、FIN8、Ruthless Mantis（元REvil）などのサイバー犯罪およびランサムウェアグループによって使用されていることを明らかにした。 Ragnar Loaderは、侵害されたシステムへの持続的なアクセスを維持し、攻撃者が長期間にわたってネットワーク内に滞在するのを支援する重要な役割を果たしている。 このマルウェアは、PowerShellベースのペイロードを使用し、RC4やBase64などの強力な暗号化とエンコード手法を組み込み、プロセスインジェクション戦略を活用して、検出を回避し、侵害されたシステム上でのステルスな制御を維持している。 Ragnar Loaderは、リバースシェル、ローカル特権昇格、リモートデスクトップアクセスを容易にする複数のコンポーネントを含むアーカイブファイルパッケージとしてアフィリエイトに提供されている。 このマルウェアは、DLLプラグインやシェルコードを実行し、任意のファイルの内容を読み取り、持ち出す能力を持ち、ネットワーク内での横方向の移動を可能にするために、別のPowerShellベースのピボットファイルを使用している。 | 高 | `source--daily-070fa8287bb523515401` |
| FIN7がアメリカの自動車メーカーのITスタッフをフィッシング攻撃で標的に | phishing-campaign | 不明 | 不明 | 2024-04-19 | target--activity-rule--country--6604ad21c713b8dfd8c7 | malware--carbanak | ttp--activity-rule--229f465ec300f65d7455, ttp--activity-rule--6a4b857a6fd043a5a7e8 | victim--activity-rule--ffc93c47ccaf2f55aaed | FIN7がアメリカの大手自動車メーカーのITスタッフを標的にした 攻撃は権限の大きい従業員を標的にし、スピアフィッシングメールでAnunakバックドアを配布 電子メール内には、Advanced IP Scannerになりすました悪意のあるURLがあり、アクセスすると正規のインストーラを装ったWsTaskLoad.exeのインストールが求められる。 攻撃は最初に感染したホストにとどまり、ネットワーク内の別システムへ感染は拡大しなかった BlackBerryによる分析でFIN7の特有の「PowerTrash」難読化ツールを利用したPowerShellスクリプトが使用されていたことが判明 | 高 | `source--daily-be6e9936378029a65c65` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アイスランド | 構造化OSINTの被害国フィールドでFIN7の標的・被害国としてアイスランドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | インド | 構造化OSINTの被害国フィールドでFIN7の標的・被害国としてインドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ウクライナ | 構造化OSINTの被害国フィールドでFIN7の標的・被害国としてウクライナが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ウズベキスタン | 構造化OSINTの被害国フィールドでFIN7の標的・被害国としてウズベキスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オーストラリア | 構造化OSINTの被害国フィールドでFIN7の標的・被害国としてオーストラリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オーストリア | 構造化OSINTの被害国フィールドでFIN7の標的・被害国としてオーストリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | カナダ | 構造化OSINTの被害国フィールドでFIN7の標的・被害国としてカナダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | スイス | 構造化OSINTの被害国フィールドでFIN7の標的・被害国としてスイスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | スウェーデン | 構造化OSINTの被害国フィールドでFIN7の標的・被害国としてスウェーデンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | スペイン | 構造化OSINTの被害国フィールドでFIN7の標的・被害国としてスペインが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | チェコ | 構造化OSINTの被害国フィールドでFIN7の標的・被害国としてチェコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ドイツ | 構造化OSINTの被害国フィールドでFIN7の標的・被害国としてドイツが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ネパール | 構造化OSINTの被害国フィールドでFIN7の標的・被害国としてネパールが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ノルウェー | 構造化OSINTの被害国フィールドでFIN7の標的・被害国としてノルウェーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | パキスタン | 構造化OSINTの被害国フィールドでFIN7の標的・被害国としてパキスタンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フランス | 構造化OSINTの被害国フィールドでFIN7の標的・被害国としてフランスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ブラジル | 構造化OSINTの被害国フィールドでFIN7の標的・被害国としてブラジルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ブルガリア | 構造化OSINTの被害国フィールドでFIN7の標的・被害国としてブルガリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ポーランド | 構造化OSINTの被害国フィールドでFIN7の標的・被害国としてポーランドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | マルタ | レビュー済みアクターマッピングの標的欄に記録されたマルタを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | モロッコ | 構造化OSINTの被害国フィールドでFIN7の標的・被害国としてモロッコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ルクセンブルク | 構造化OSINTの被害国フィールドでFIN7の標的・被害国としてルクセンブルクが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ロシア | 構造化OSINTの被害国フィールドでFIN7の標的・被害国としてロシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 中国 | 構造化OSINTの被害国フィールドでFIN7の標的・被害国として中国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 台湾 | 構造化OSINTの被害国フィールドでFIN7の標的・被害国として台湾が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | 活動「FIN7がアメリカの自動車メーカーのITスタッフをフィッシング攻撃で標的に」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-be6e9936378029a65c65`, `source--target-audit-etda-threat-group-cards` |
| countries | 英国 | 構造化OSINTの被害国フィールドでFIN7の標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 香港 | 構造化OSINTの被害国フィールドでFIN7の標的・被害国として香港が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 北米 | カナダ、米国で確認された標的・被害事例を北米として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-be6e9936378029a65c65`, `source--target-audit-etda-threat-group-cards` |
| regions | 南アジア | インド、ネパール、パキスタンで確認された標的・被害事例を南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 南欧 | スペイン、マルタで確認された標的・被害事例を南欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| regions | 東アジア | 中国、台湾、香港で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 東欧 | ウクライナ、チェコ、ブルガリア、ポーランド、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | アイスランド、ウクライナ、オーストリア、スイス、スウェーデン、スペイン、チェコ、ドイツ、ノルウェー、フランス、ブルガリア、ポーランド、マルタ、ルクセンブルク、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| sectors | 小売・ホスピタリティ | [FIN7](https://attack.mitre.org/groups/G0046) has targeted the retail, restaurant, hospitality, software, consulting, financial services, medical equipment, cloud services, media, food and beverage, transportation, pharmaceutical, and utilities industries in the United States. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 運輸・航空・海運 | [FIN7](https://attack.mitre.org/groups/G0046) has targeted the retail, restaurant, hospitality, software, consulting, financial services, medical equipment, cloud services, media, food and beverage, transportation, pharmaceutical, and utilities industries in the United States. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 医療・ヘルスケア | [FIN7](https://attack.mitre.org/groups/G0046) has targeted the retail, restaurant, hospitality, software, consulting, financial services, medical equipment, cloud services, media, food and beverage, transportation, pharmaceutical, and utilities industries in the United States. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | メディア・報道 | [FIN7](https://attack.mitre.org/groups/G0046) has targeted the retail, restaurant, hospitality, software, consulting, financial services, medical equipment, cloud services, media, food and beverage, transportation, pharmaceutical, and utilities industries in the United States. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 金融 | [FIN7](https://attack.mitre.org/groups/G0046) has targeted the retail, restaurant, hospitality, software, consulting, financial services, medical equipment, cloud services, media, food and beverage, transportation, pharmaceutical, and utilities industries in the United States. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | Finance | Targeting text indicates the Finance sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: FIN7、FIN8などがRagnar Loaderを使用して持続的アクセスとランサムウェア攻撃を実行 | 非公開 | aggregate | multiple-organizations | reported |  | malware--revil | ttp--activity-rule--7d77bae4a556494c0709 |  | encryption: FIN7、FIN8などがRagnar Loaderを使用して持続的アクセスとランサムウェア攻撃を実行 | 不明 | 不明 | 2025-03-08 | 高 | `source--daily-070fa8287bb523515401` |
| 被害事例: FIN7、Anubisバックドアを展開し、SharePoint経由でWindowsシステムを乗っ取り | 非公開 | aggregate | multiple-organizations | reported |  |  | ttp--activity-rule--85ff7043ed59c3428534, ttp--activity-rule--cedd0a0b2316fd50d056, ttp--activity-rule--d1e93bd0a09f55baffe6, ttp--activity-rule--f9daa094c8fa810e7348 | VPN／リモートアクセス機器, サーバー, エンドポイント | credential-theft: 攻撃者は、キーロギング、スクリーンショット取得、パスワード窃取などの操作を、被害者のシステム上に直接ツールを保存せずに実行可能。 | 不明 | 不明 | 2025-04-03 | 高 | `source--daily-aa4ff1b6006e51c3ed82` |
| 被害事例: FIN7がアメリカの自動車メーカーのITスタッフをフィッシング攻撃で標的に | 非公開 | anonymous | unknown | reported | target--activity-rule--country--6604ad21c713b8dfd8c7 | malware--carbanak | ttp--activity-rule--229f465ec300f65d7455, ttp--activity-rule--6a4b857a6fd043a5a7e8 | メール／メールアカウント |  | 不明 | 不明 | 2024-04-19 | 高 | `source--daily-be6e9936378029a65c65` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Execution | T1059.001 | PowerShell | 攻撃は最初に感染したホストにとどまり、ネットワーク内の別システムへ感染は拡大しなかった BlackBerryによる分析でFIN7の特有の「PowerTrash」難読化ツールを利用したPowerShellスクリプトが使用されていたことが判明 |  | activity--daily-de6c1a21107df6383bb2 | 不明 | 不明 | 中 | `source--daily-be6e9936378029a65c65` |
| Stealth | T1027 | Obfuscated Files or Information | 攻撃は最初に感染したホストにとどまり、ネットワーク内の別システムへ感染は拡大しなかった BlackBerryによる分析でFIN7の特有の「PowerTrash」難読化ツールを利用したPowerShellスクリプトが使用されていたことが判明 |  | activity--daily-de6c1a21107df6383bb2 | 不明 | 不明 | 中 | `source--daily-be6e9936378029a65c65` |
| Privilege Escalation, Stealth | T1055 | Process Injection | このマルウェアは、PowerShellベースのペイロードを使用し、RC4やBase64などの強力な暗号化とエンコード手法を組み込み、プロセスインジェクション戦略を活用して、検出を回避し、侵害されたシステム上でのステルスな制御を維持している。 |  | activity--daily-ddb3ccfc94f068acbcb3 | 不明 | 不明 | 中 | `source--daily-070fa8287bb523515401` |
| Collection | T1560.001 | Archive via Utility | 感染はZIPアーカイブ内のPythonスクリプトから始まり、メモリ内で難読化されたペイロードを復号・実行。 |  | activity--daily-ab167c39e30704e86031 | 不明 | 不明 | 中 | `source--daily-aa4ff1b6006e51c3ed82` |
| Stealth | T1027 | Obfuscated Files or Information | 感染はZIPアーカイブ内のPythonスクリプトから始まり、メモリ内で難読化されたペイロードを復号・実行。 |  | activity--daily-ab167c39e30704e86031 | 不明 | 不明 | 中 | `source--daily-aa4ff1b6006e51c3ed82` |
| Collection | T1113 | Screen Capture | 攻撃者は、キーロギング、スクリーンショット取得、パスワード窃取などの操作を、被害者のシステム上に直接ツールを保存せずに実行可能。 |  | activity--daily-ab167c39e30704e86031 | 不明 | 不明 | 中 | `source--daily-aa4ff1b6006e51c3ed82` |
| Execution | T1059.006 | Python | 金銭目的の脅威アクターFIN7が、Pythonベースのバックドア「Anubis」を使用してWindowsシステムへのリモートアクセスを確立。 |  | activity--daily-ab167c39e30704e86031 | 不明 | 不明 | 中 | `source--daily-aa4ff1b6006e51c3ed82` |
| Collection | T1005 | Data from Local System | [FIN7](https://attack.mitre.org/groups/G0046) has collected files and other sensitive information from a compromised network.(Citation: CrowdStrike Carbon Spider August 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1008 | Fallback Channels | [FIN7](https://attack.mitre.org/groups/G0046)'s Harpy backdoor malware can use DNS as a backup channel for C2 if HTTP fails.(Citation: Crowdstrike GTR2020 Mar 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | [FIN7](https://attack.mitre.org/groups/G0046) has used RDP to move laterally in victim environments.(Citation: CrowdStrike Carbon Spider August 2021)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.004 | SSH | [FIN7](https://attack.mitre.org/groups/G0046) has used SSH to move laterally through victim environments.(Citation: CrowdStrike Carbon Spider August 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.005 | VNC | [FIN7](https://attack.mitre.org/groups/G0046) has used TightVNC to control compromised hosts.(Citation: CrowdStrike Carbon Spider August 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.010 | Command Obfuscation | [FIN7](https://attack.mitre.org/groups/G0046) has used fragmented strings, environment variables, standard input (stdin), and native character-replacement functionalities to obfuscate commands.(Citation: FireEye Obfuscation June 2017)(Citation: FireEye FIN7 Aug 2018)(Citation: CrowdStrike Carbon Spider August 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.016 | Junk Code Insertion | [FIN7](https://attack.mitre.org/groups/G0046) has used random junk code to obfuscate malware code.(Citation: Mandiant FIN7 Apr 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | [FIN7](https://attack.mitre.org/groups/G0046) has used the command `cmd.exe /C quser` to collect user session information.(Citation: Mandiant FIN7 Apr 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.004 | Masquerade Task or Service | [FIN7](https://attack.mitre.org/groups/G0046) has created a scheduled task named “AdobeFlashSync” to establish persistence.(Citation: Morphisec FIN7 June 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [FIN7](https://attack.mitre.org/groups/G0046) has attempted to run Darkside ransomware with the filename sleep.exe.(Citation: CrowdStrike Carbon Spider August 2021) Additionally, [FIN7](https://attack.mitre.org/groups/G0046) has mimicked WsTaskLoad.exe, which is associated with the Wondershare software suite, by using a malicious executable under the same name.(Citation: BlackBerry_FIN7_April2024)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | [FIN7](https://attack.mitre.org/groups/G0046) has used WMI to install malware on targeted systems.(Citation: eSentire FIN7 July 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [FIN7](https://attack.mitre.org/groups/G0046) malware has created scheduled tasks to establish persistence.(Citation: FireEye FIN7 April 2017)(Citation: Morphisec FIN7 June 2017)(Citation: FireEye FIN7 Aug 2018)(Citation: Flashpoint FIN 7 March 2019) Specifically, [FIN7](https://attack.mitre.org/groups/G0046) has used OpenSSH to establish persistence.(Citation: BlackBerry_FIN7_April2024)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | [FIN7](https://attack.mitre.org/groups/G0046) has used the PowerShell script 3CF9.ps1 to perform process discovery by executing `tasklist /v`. Additionally, WsTaskLoad.exe executes `tasklist /v` to perform process discovery.(Citation: BlackBerry_FIN7_April2024)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059 | Command and Scripting Interpreter | [FIN7](https://attack.mitre.org/groups/G0046) used SQL scripts to help perform tasks on the victim's machine.(Citation: FireEye FIN7 Aug 2018)(Citation: Flashpoint FIN 7 March 2019)(Citation: FireEye FIN7 Aug 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [FIN7](https://attack.mitre.org/groups/G0046) used a PowerShell script to launch shellcode that retrieved an additional payload.(Citation: FireEye FIN7 April 2017)(Citation: Morphisec FIN7 June 2017)(Citation: FBI Flash FIN7 USB)(Citation: Mandiant FIN7 Apr 2022)(Citation: Gemini_FIN7_Jan2022) Additionally, [FIN7](https://attack.mitre.org/groups/G0046) has executed a custom obfuscation of the shellcode invoker in [PowerSploit](https://attack.mitre.org/software/S0194) called POWERTRASH.(Citation: BlackBerry_FIN7_April2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [FIN7](https://attack.mitre.org/groups/G0046) used the command prompt to launch commands on the victim’s machine.(Citation: FireEye FIN7 Aug 2018)(Citation: Flashpoint FIN 7 March 2019)(Citation: Mandiant FIN7 Apr 2022) Additionally, [FIN7](https://attack.mitre.org/groups/G0046) has used cmd.exe to open the Run dialog by sending the “Windows + R” keys through malicious USBs acting as virtual keyboards.(Citation: Gemini_FIN7_Jan2022)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | [FIN7](https://attack.mitre.org/groups/G0046) used VBS scripts to help perform tasks on the victim's machine.(Citation: FireEye FIN7 Aug 2018)(Citation: Flashpoint FIN 7 March 2019)(Citation: CrowdStrike Carbon Spider August 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.007 | JavaScript | [FIN7](https://attack.mitre.org/groups/G0046) used JavaScript scripts to help perform tasks on the victim's machine.(Citation: FireEye FIN7 Aug 2018)(Citation: Flashpoint FIN 7 March 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1069.002 | Domain Groups | [FIN7](https://attack.mitre.org/groups/G0046) has used the command `net group "domain admins" /domain` to enumerate domain groups.(Citation: Mandiant FIN7 Apr 2022)(Citation: BlackBerry_FIN7_April2024)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.004 | DNS | [FIN7](https://attack.mitre.org/groups/G0046) has performed C2 using DNS via A, OPT, and TXT records.(Citation: FireEye FIN7 Aug 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [FIN7](https://attack.mitre.org/groups/G0046) has harvested valid administrative credentials for lateral movement.(Citation: CrowdStrike Carbon Spider August 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.003 | Local Accounts | [FIN7](https://attack.mitre.org/groups/G0046) has used compromised credentials for access as SYSTEM on Exchange servers.(Citation: Microsoft Ransomware as a Service) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [FIN7](https://attack.mitre.org/groups/G0046) has used csvde.exe, which is a built-in Windows command line tool, to export system information. Additionally, WsTaskLoad has gathered system information, such as operating system and hostname.(Citation: BlackBerry_FIN7_April2024)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | [FIN7](https://attack.mitre.org/groups/G0046) has used the PowerShell script 3CF9.ps1 and the executable WsTaskLoad to enumerate domain administrations by executing `net group “Domain Admins” /domain`.(Citation: BlackBerry_FIN7_April2024) [FIN7](https://attack.mitre.org/groups/G0046) has also used csvde.exe, which is a built-in Windows command line tool, to export Active Directory information.  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Lateral Movement | T1091 | Replication Through Removable Media | [FIN7](https://attack.mitre.org/groups/G0046) actors have mailed USB drives to potential victims containing malware that downloads and installs various backdoors, including in some cases for ransomware operations.(Citation: FBI Flash FIN7 USB) Additionally, [FIN7](https://attack.mitre.org/groups/G0046) has used malicious USBs that acted as virtual keyboards to install malware and txt files that decode to PowerShell commands.(Citation: Gemini_FIN7_Jan2022)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102.002 | Bidirectional Communication | [FIN7](https://attack.mitre.org/groups/G0046) used legitimate services like Google Docs, Google Scripts, and Pastebin for C2.(Citation: FireEye FIN7 Aug 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [FIN7](https://attack.mitre.org/groups/G0046) has downloaded additional malware to execute on the victim's machine, including by using a PowerShell script to launch shellcode that retrieves an additional payload.(Citation: FireEye FIN7 April 2017)(Citation: DOJ FIN7 Aug 2018)(Citation: Mandiant FIN7 Apr 2022)(Citation: Gemini_FIN7_Jan2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1113 | Screen Capture | [FIN7](https://attack.mitre.org/groups/G0046) captured screenshots and desktop video recordings.(Citation: DOJ FIN7 Aug 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1124 | System Time Discovery | [FIN7](https://attack.mitre.org/groups/G0046) has used the PowerShell script 3CF9.ps1 to execute `net time`.(Citation: BlackBerry_FIN7_April2024)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1125 | Video Capture | [FIN7](https://attack.mitre.org/groups/G0046) created a custom video recording capability that could be used to monitor operations in the victim's environment.(Citation: FireEye FIN7 Aug 2018)(Citation: DOJ FIN7 Aug 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | [FIN7](https://attack.mitre.org/groups/G0046) has decoded a malicious PowerShell script using `certutil -decode hex` and has decoded an XOR-obfuscated block of data with the key `qawsed1q2w3e`, which led to the installation of [Lizar](https://attack.mitre.org/software/S0681).(Citation: Gemini_FIN7_Jan2022)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [FIN7](https://attack.mitre.org/groups/G0046) has compromised targeted organizations through exploitation of CVE-2021-31207 in Exchange.(Citation: Microsoft Ransomware as a Service) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1195.002 | Compromise Software Supply Chain | [FIN7](https://attack.mitre.org/groups/G0046) has gained initial access by compromising a victim's software supply chain.(Citation: Mandiant FIN7 Apr 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1200 | Hardware Additions | доступ к инфраструктуре жертв через наборы эксплоитов. Например, опера - торы ZLoader использовали Spelevo EK, а с Dridex – набор Rig EK. • Hardware additions T1200 В 2021 году группировка FIN7 продолжила проводить атаки типа BadUSB для заражения компьютеров в корпоративной среде, отправляя посылки через почтовую службу США и логистическую компанию UPS. Отправителями значились Министерство здраво - охранени |  |  | 不明 | 不明 | 中 | `source--fin7--6269b5f18e206dc0` |
| Execution | T1204.001 | Malicious Link | [FIN7](https://attack.mitre.org/groups/G0046) has used malicious links to lure victims into downloading malware.(Citation: CrowdStrike Carbon Spider August 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [FIN7](https://attack.mitre.org/groups/G0046) lured victims to double-click on images in the attachments they sent which would then execute the hidden LNK file.(Citation: FireEye FIN7 April 2017)(Citation: eSentire FIN7 July 2021)(Citation: CrowdStrike Carbon Spider August 2021) Additionally, [FIN7](https://attack.mitre.org/groups/G0046) has used malicious Microsoft Word and Excel files and Leo VBS to distribute an updated version of [JSS Loader](https://attack.mitre.org/software/S0648) and to distribute the Harpy backdoor.(Citation: Crowdstrike_CarbonSpider_Part2_Nov2024)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1210 | Exploitation of Remote Services | [FIN7](https://attack.mitre.org/groups/G0046) has exploited ZeroLogon (CVE-2020-1472) against vulnerable domain controllers.(Citation: CrowdStrike Carbon Spider August 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.005 | Mshta | [FIN7](https://attack.mitre.org/groups/G0046) has used mshta.exe to execute VBScript to execute malicious code on victim systems.(Citation: FireEye FIN7 April 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.011 | Rundll32 | [FIN7](https://attack.mitre.org/groups/G0046) has used `rundll32.exe` to execute malware on a compromised network.(Citation: Mandiant FIN7 Apr 2022)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1219 | Remote Access Tools | [FIN7](https://attack.mitre.org/groups/G0046) has utilized the remote management tool Atera to download malware to a compromised system.(Citation: Mandiant FIN7 Apr 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1486 | Data Encrypted for Impact | [FIN7](https://attack.mitre.org/groups/G0046) has encrypted virtual disk volumes on ESXi servers using a version of Darkside ransomware.(Citation: CrowdStrike Carbon Spider August 2021)(Citation: Mandiant FIN7 Apr 2022) Additionally, [FIN7](https://attack.mitre.org/groups/G0046) has deployed ransomware as the end payload during big game hunting.(Citation: BlackBerry_FIN7_April2024)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery, Stealth | T1497.002 | User Activity Based Checks | [FIN7](https://attack.mitre.org/groups/G0046) used images embedded into document lures that only activate the payload when a user double clicks to avoid sandboxes.(Citation: FireEye FIN7 April 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | [FIN7](https://attack.mitre.org/groups/G0046) created new Windows services and added them to the startup directories for persistence.(Citation: FireEye FIN7 Aug 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1546.011 | Application Shimming | [FIN7](https://attack.mitre.org/groups/G0046) has used application shim databases for persistence.(Citation: FireEye FIN7 Shim Databases) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [FIN7](https://attack.mitre.org/groups/G0046) malware has created Registry Run and RunOnce keys to establish persistence, and has also added items to the Startup folder.(Citation: FireEye FIN7 April 2017)(Citation: FireEye FIN7 Aug 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1553.002 | Code Signing | [FIN7](https://attack.mitre.org/groups/G0046) has signed [Carbanak](https://attack.mitre.org/software/S0030) payloads with legally purchased code signing certificates. [FIN7](https://attack.mitre.org/groups/G0046) has also digitally signed their phishing documents, backdoors and other staging tools to bypass security controls.(Citation: FireEye CARBANAK June 2017)(Citation: FireEye FIN7 Aug 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1558.003 | Kerberoasting | [FIN7](https://attack.mitre.org/groups/G0046) has used Kerberoasting PowerShell commands such as, `Invoke-Kerberoast` for credential access and to enable lateral movement.(Citation: CrowdStrike Carbon Spider August 2021)(Citation: Mandiant FIN7 Apr 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1559.002 | Dynamic Data Exchange | [FIN7](https://attack.mitre.org/groups/G0046) spear phishing campaigns have included malicious Word documents with DDE execution.(Citation: CyberScoop FIN7 Oct 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.001 | Hidden Files and Directories | [FIN7](https://attack.mitre.org/groups/G0046) has used `attrib +h “C:\ProgramData\ssh”` to make the SSH folder hidden.(Citation: BlackBerry_FIN7_April2024)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.003 | Hidden Window | [FIN7](https://attack.mitre.org/groups/G0046) has used .txt files to conceal PowerShell commands.(Citation: Gemini_FIN7_Jan2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [FIN7](https://attack.mitre.org/groups/G0046) sent spearphishing emails with either malicious Microsoft Documents or RTF files attached.(Citation: FireEye FIN7 April 2017)(Citation: DOJ FIN7 Aug 2018)(Citation: Flashpoint FIN 7 March 2019)(Citation: eSentire FIN7 July 2021)(Citation: CrowdStrike Carbon Spider August 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | [FIN7](https://attack.mitre.org/groups/G0046) has conducted broad phishing campaigns using malicious links.(Citation: CrowdStrike Carbon Spider August 2021) Additionally, [FIN7](https://attack.mitre.org/groups/G0046) has sent spearphishing emails containing a typosquatted link to “ip-sccanner[.]com.”(Citation: BlackBerry_FIN7_April2024)    |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | [FIN7](https://attack.mitre.org/groups/G0046) has exfiltrated stolen data to the MEGA file sharing site.(Citation: CrowdStrike Carbon Spider August 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1569.002 | Service Execution | [FIN7](https://attack.mitre.org/groups/G0046) has started the SSH service by executing `sc start sshd`.(Citation: BlackBerry_FIN7_April2024)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1571 | Non-Standard Port | [FIN7](https://attack.mitre.org/groups/G0046) has used port-protocol mismatches on ports such as 53, 80, 443, and 8080 during C2.(Citation: FireEye FIN7 Aug 2018) [FIN7](https://attack.mitre.org/groups/G0046) has used TCP ports 59999 and 9898 for firewall rules.(Citation: BlackBerry_FIN7_April2024)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1572 | Protocol Tunneling | [FIN7](https://attack.mitre.org/groups/G0046) has tunneled C2 traffic via OpenSSH.(Citation: BlackBerry_FIN7_April2024)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [FIN7](https://attack.mitre.org/groups/G0046) has registered look-alike domains for use in phishing campaigns.(Citation: eSentire FIN7 July 2021) Additionally, [FIN7](https://attack.mitre.org/groups/G0046) has registered a malicious domain as `advanced-ip-sccanner[.]com` that redirected to an adversary-controlled Dropbox which contained the malicious executable.(Citation: BlackBerry_FIN7_April2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.006 | Web Services | [FIN7](https://attack.mitre.org/groups/G0046) has set up Amazon S3 buckets to host trojanized digital products.(Citation: Mandiant FIN7 Apr 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | [FIN7](https://attack.mitre.org/groups/G0046) has developed malware for use in operations, including the creation of infected removable media.(Citation: FBI Flash FIN7 USB)(Citation: FireEye FIN7 Oct 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [FIN7](https://attack.mitre.org/groups/G0046) has utilized a variety of tools such as [Cobalt Strike](https://attack.mitre.org/software/S0154), [PowerSploit](https://attack.mitre.org/software/S0194), and the remote management tool, Atera for targeting efforts.(Citation: Mandiant FIN7 Apr 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1591 | Gather Victim Org Information | [FIN7](https://attack.mitre.org/groups/G0046) has compiled a list of victims by filtering companies by revenue using Zoominfo, which is a service that provides business information.(Citation: BiZone Lizar May 2021)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1591.004 | Identify Roles | [FIN7](https://attack.mitre.org/groups/G0046) has identified IT staff and employees who had higher levels of administrative rights.(Citation: BlackBerry_FIN7_April2024)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.001 | Upload Malware | [FIN7](https://attack.mitre.org/groups/G0046) has staged legitimate software, that was trojanized to contain an Atera agent installer, on Amazon S3.(Citation: Mandiant FIN7 Apr 2022) [FIN7](https://attack.mitre.org/groups/G0046) has also used an open directory web server as a staging server for payloads and other tools, such as OpenSSH and 7zip.(Citation: Cocomazzi FIN7 Reboot)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.004 | Drive-by Target | [FIN7](https://attack.mitre.org/groups/G0046) has compromised a digital product website and modified multiple download links to point to trojanized versions of offered digital products.(Citation: Mandiant FIN7 Apr 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.005 | Link Target | [FIN7](https://attack.mitre.org/groups/G0046) has created a fake link that redirected to an adversary-controlled Dropbox that downloaded the malicious executable.(Citation: BlackBerry_FIN7_April2024)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1620 | Reflective Code Loading | [FIN7](https://attack.mitre.org/groups/G0046) has loaded a .NET assembly into the currect execution context via `Reflection.Assembly::Load`.(Citation: Gemini_FIN7_Jan2022)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1674 | Input Injection | FIN7 has used malicious USBs to emulate keystrokes to launch PowerShell to download and execute malware from the adversary's server.(Citation: FBI Flash FIN7 USB)(Citation: Gemini_FIN7_Jan2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1686 | Disable or Modify System Firewall | [FIN7](https://attack.mitre.org/groups/G0046) has added a firewall rule to allow TCP port 59999 inbound and a rule to allow sshd.exe on TCP port 9898.(Citation: BlackBerry_FIN7_April2024)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
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
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
