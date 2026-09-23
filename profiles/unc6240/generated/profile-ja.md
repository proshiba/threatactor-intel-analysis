# UNC6240 脅威アクタープロファイル

- プロファイルID: `actor--unc6240`
- 状態: draft
- 更新日時: 2026-09-23T12:16:55Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

UNC6240の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC6240**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Bling Libra | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2`, `source--mitre-attack-g1057` | Official MITRE ATT&CK associated-group name for G1057. |
| ShinyHunters | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2`, `source--mitre-attack-g1057` | GTIGは原文で「UNC6240 (also known as ShinyHunters), a financially motivated threat cluster specializing in high-volume software-as-a-service (SaaS) data exfiltration and extortion operations」と明示的に同一視している。UNC指定子の命名主体自身による対応付けであり確度はhighとする。ただしscopeはexactとしない。同じMandiant/GTIGが2026-02-02報告で「UNC6661/UNC6671/UNC6240(ShinyHunters)」と述べ、UNC6661とUNC6671が侵入・窃取、UNC6240が恐喝を担う分業として整理しているのに対し、報道や被害組織の文脈で用いられる「ShinyHunters」は侵入から恐喝までの作戦全体を指すことが多く、公称の指す範囲がUNC6240より広い。OSINT_RULESの「新aliasは既存クラスターとのスコープをexactと断定しない」に従いoverlappingとする。 Official MITRE ATT&CK associated-group name for G1057. |
| Storm-3127 | Microsoft | overlapping | 高 | `source--osint-microsoft-threat-actor-mapping` | Microsoft's official mapping links this name to the profile identifier; cross-vendor collection boundaries may differ. |

## 帰属

未評価

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: なし

## モチベーション

未評価

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Scattered Spider | related-to | [ShinyHunters](https://attack.mitre.org/groups/G1057) has been associated with the broader collective called The Community, also known as The Com whose members have also included [Scattered Spider](https://attack.mitre.org/groups/G1015) and [LAPSUS$](https://attack.mitre.org/groups/G1004). | 中 | `source--mitre-attack-19-2` |
| LAPSUS$ | related-to | [ShinyHunters](https://attack.mitre.org/groups/G1057) has been associated with the broader collective called The Community, also known as The Com whose members have also included [Scattered Spider](https://attack.mitre.org/groups/G1015) and [LAPSUS$](https://attack.mitre.org/groups/G1004). | 中 | `source--mitre-attack-19-2` |
| UNC6040 | related-to | GTIG tracks the initial Salesforce vishing and data theft as UNC6040 and the subsequent ShinyHunters-branded extortion as UNC6240; a partnership is possible but not established as exact identity. | 高 | `source--gtig-unc6040-salesforce-vishing-2025` |
| UNC6671 | taxonomy-overlaps-with | GTIG tracks UNC6661, UNC6671, and UNC6240 separately within recent ShinyHunters-branded SaaS theft reporting to preserve possible partnership and impersonation boundaries. | 高 | `source--gtig-shinyhunters-saas-clusters-2026` |
| UNC6661 | related-to | GTIG attributes extortion following UNC6661 intrusions to UNC6240, based on negotiation-account and extortion-artifact overlaps. | 高 | `source--gtig-shinyhunters-saas-clusters-2026` |

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

- 判定: `matched`
- 調査日時: 2026-09-21T02:39:13Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | ShinyHunters | single-alias-intersection | 中 |  | https://www.zerofox.com/blog/shinyhunters-breach/<br>https://www.bleepingcomputer.com/news/security/hacker-group-floods-dark-web-with-data-stolen-from-11-companies/<br>https://www.zdnet.com/article/a-hacker-group-is-selling-more-than-73-million-user-records-on-the-dark-web/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Storm-3127 | canonical-name | 高 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | ShinyHunters | single-alias-intersection | 中 |  | https://cyberwarzone.com/shinyhunters-22-year-old-member-pleads-guilty-to-cyber-extortion-causing-6-million-in-damage/<br>https://www.bitdefender.com/blog/hotforsecurity/pizza-hut-australia-leaks-one-million-customers-details-claims-shinyhunters-hacking-group/<br>https://www.justice.gov/usao-wdwa/pr/alleged-french-cybercriminal-appear-seattle-indictment-conspiracy-computer-intrusion |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | ShinyHunters - G1057 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1057<br>https://blog.eclecticiq.com/shinyhunters-calling-financially-motivated-data-extortion-group-targeting-enterprise-cloud-applications<br>https://cloud.google.com/blog/topics/threat-intelligence/expansion-shinyhunters-saas-data-theft |
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

未確認

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--tor | Tor | [Tor](https://attack.mitre.org/software/S0183) is a software suite and network that provides increased anonymity on the Internet. It creates a multi-hop proxy network and utilizes multilayer encryption to protect both the message and routing information. [Tor](https://attack.mitre.org/software/S0183) utilizes "Onion Routing," in which messages are encrypted with multiple layers of encryption; at each step in the proxy network, the topmost layer is decrypted and the contents forwarded on to the next node until it reaches its destination. (Citation: Dingledine Tor The Second-Generation Onion Router) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

### インフラ

未確認

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

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

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Mandiant、ShinyHuntersがSSOを悪用してクラウドデータを窃取する手口を詳述 | ransomware-extortion | 不明 | 不明 | 2026-02-02 |  |  |  | victim--activity-rule--08fecf1c5b48c6bc87e9 | Mandiantは、ShinyHuntersのSaaSデータ窃取が、電話を伴うvishingと企業風フィッシングでSSO資格情報とMFAコードを奪う手口で拡大と説明。 攻撃者はIT/ヘルプデスクを装い通話中に偽ポータルへ誘導、奪取直後にログインし正規MFAを操作して自機を登録して持続化。 侵害後はOkta/Entra/GoogleのSSOダッシュボードを足場に、Salesforce（主標的）やMicrosoft 365、SharePoint、DocuSignなどへ横断アクセス。 MandiantはUNC6661/UNC6671/UNC6240（ShinyHunters）を追跡し、前二者が侵入・窃取、UNC6240が恐喝を担いTox IDを再利用と指摘。 これらの攻撃を検知するために、SSO侵害直後の大量流出、SharePoint/OneDriveのPowerShell UAでのアクセス、ToogleBox Recallの不意なOAuthやMFA通知削除を監視することを提案。 | 中 | `source--daily-02e1336153d9062de8f2` |
| Salesforce攻撃後にFarmers Insuranceのデータ侵害、110万人に影響 | ransomware-extortion | 2025-05-29 | 2025-05-29 | 2025-08-26 | target--activity-rule--sector--4221b5fbb827488c6eaa |  |  | victim--activity-rule--dd9c7a0f1e6caf1b0984 | サードパーティベンダー経由で不正アクセス、1,111,386人の顧客データが流出。 侵害は2025年5月29日発生、翌30日に検知・封じ込めを実施と説明。 氏名・住所・生年月日・運転免許番号・SSN下4桁などが流出。 8月22日から影響者へ通知、メイン州AGに通知サンプル提出。 攻撃はSalesforce悪用で、vishingと悪性OAuth連携→データ窃取・恐喝。 | 中 | `source--daily-8012423fa9a259605e9c` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| Mandiant、ShinyHuntersがSSOを悪用してクラウドデータを窃取する手口を詳述 | UNC6240 | 情報なし | 情報なし | 情報なし | 情報なし | 被害事例: Mandiant、ShinyHuntersがSSOを悪用してクラウドデータを窃取する手口を詳述 | 中 |
| Salesforce攻撃後にFarmers Insuranceのデータ侵害、110万人に影響 | UNC6240 | 情報なし | 情報なし | 情報なし | 金融 | Salesforce攻撃後にFarmers Insurance | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| sectors | 金融 | 活動「Salesforce攻撃後にFarmers Insuranceのデータ侵害、110万人に影響」の記述で標的として明示された産業。 | 2025-05-29 | 2025-05-29 | 中 | `source--daily-8012423fa9a259605e9c` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Mandiant、ShinyHuntersがSSOを悪用してクラウドデータを窃取する手口を詳述 | 非公開 | aggregate | multiple-organizations | reported |  |  |  | メール／メールアカウント, クラウド／SaaS | data-theft: Mandiant、ShinyHuntersがSSOを悪用してクラウドデータを窃取する手口を詳述 | 不明 | 不明 | 2026-02-02 | 中 | `source--daily-02e1336153d9062de8f2` |
| 被害事例: Salesforce攻撃後にFarmers Insuranceのデータ侵害、110万人に影響 | Salesforce攻撃後にFarmers Insurance | named | organization | reported | target--activity-rule--sector--4221b5fbb827488c6eaa |  |  | クラウド／SaaS | data-theft: サードパーティベンダー経由で不正アクセス、1,111,386人の顧客データが流出。 | 2025-05-29 | 2025-05-29 | 2025-08-26 | 中 | `source--daily-8012423fa9a259605e9c` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Discovery | T1016 | System Network Configuration Discovery | [ShinyHunters](https://attack.mitre.org/groups/G1057) has collected machine names and IP addresses by parsing the process scheduler configuration file psappsrv.cfg.(Citation: Google_SHOracle_Jun2026)     |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1018 | Remote System Discovery | [ShinyHunters](https://attack.mitre.org/groups/G1057) has enumerated the internal subnet using ` cat /etc/hosts \| grep -E "[redacted_victim_string]"`.(Citation: Google_SHOracle_Jun2026)     |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [ShinyHunters](https://attack.mitre.org/groups/G1057) has disguised MeshCentral agent binaries as Microsoft Azure services, e.g. meshagent32-azure-ops.exe, meshagent64-azure-ops.exe, and meshagent64-v2.exe.(Citation: Google_SHOracle_Jun2026)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.007 | JavaScript | [ShinyHunters](https://attack.mitre.org/groups/G1057) has used the MeshCentral command-line interface utility meshctrl.js and npm to interact with compromised systems. Specifically for npm, [ShinyHunters](https://attack.mitre.org/groups/G1057) has checked for the authenticode tool using the command `npm list global authenticode`.(Citation: Google_SHOracle_Jun2026) Additionally, [ShinyHunters](https://attack.mitre.org/groups/G1057) has used the MeshCentral command to execute the propagation script: ` node meshctrl.js RunCommand --loginuser admin --loginpass '[password]' --id '[agent_id]' --run 'bash /tmp/[victim_abbreviation]_fanout.sh' `.(Citation: Google_SHOracle_Jun2026)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.009 | Cloud API | [ShinyHunters](https://attack.mitre.org/groups/G1057) has used the AWS Command Line Interface (CLI) for operations to include a variety of API calls, such as `ListBuckets`, `CreateBucket` and `DeleteBucket`.(Citation: Unit42KelleyVaya_BlingLibra_Aug2024)    |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1069.003 | Cloud Groups | [ShinyHunters](https://attack.mitre.org/groups/G1057) has executed API calls to enumerate permissions for compromised AWS accounts.(Citation: Unit42KelleyVaya_BlingLibra_Aug2024)    |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution, Lateral Movement | T1072 | Software Deployment Tools | [ShinyHunters](https://attack.mitre.org/groups/G1057) has abused software deployment tools for lateral movement.(Citation: SOCRadar_ShinyHunters_Mar2024)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [ShinyHunters](https://attack.mitre.org/groups/G1057) has used valid high-privileged SSO users as leverage during negotiations.(Citation: ElecticIQ Buyukkaya_ShinyHunters_Sept2025)    |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.002 | Domain Accounts | [ShinyHunters](https://attack.mitre.org/groups/G1057) has used valid domain accounts to gain initial access or to escalate privileges within environments.(Citation: SOCRadar_ShinyHunters_Mar2024)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.004 | Cloud Accounts | [ShinyHunters](https://attack.mitre.org/groups/G1057) has used valid cloud accounts to gain initial access or to escalate privileges within cloud environments.(Citation: SOCRadar_ShinyHunters_Mar2024) Additionally, [ShinyHunters](https://attack.mitre.org/groups/G1057) has also used valid credentials from public repositories to include access keys to gain access to the victim organization’s AWS environment.(Citation: Unit42KelleyVaya_BlingLibra_Aug2024)(Citation: Intel471_SH_Aug2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1082 | System Information Discovery | [ShinyHunters](https://attack.mitre.org/groups/G1057) has used the MeshCentral command-line utility meshctrl.js to collect hostnames and IDs of compromised systems.(Citation: Google_SHOracle_Jun2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1083 | File and Directory Discovery | [ShinyHunters](https://attack.mitre.org/groups/G1057) has checked mount points for Oracle PeopleSoft configurations and has checked the process scheduler configuration file psappsrv.cfg. Additionally, [ShinyHunters](https://attack.mitre.org/groups/G1057) has read WebLogic server XML configurations files (config.xml).(Citation: Google_SHOracle_Jun2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1090.003 | Multi-hop Proxy | [ShinyHunters](https://attack.mitre.org/groups/G1057) has used [Tor](https://attack.mitre.org/software/S0183) to host their DLS.(Citation: FBI_SHLMS_May2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1105 | Ingress Tool Transfer | [ShinyHunters](https://attack.mitre.org/groups/G1057) has deployed custom scripts to targeted systems from customized MeshAgents in their staging environment.(Citation: Google_SHOracle_Jun2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Credential Access | T1110 | Brute Force | [ShinyHunters](https://attack.mitre.org/groups/G1057) has performed brute force attacks against edge devices, such as VPNs or firewall solutions.(Citation: ElecticIQ Buyukkaya_ShinyHunters_Sept2025)    |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1190 | Exploit Public-Facing Application | [ShinyHunters](https://attack.mitre.org/groups/G1057) has exploited CVE-2026-35273 against Oracle PeopleSoft application infrastructure.(Citation: Google_SHOracle_Jun2026) [ShinyHunters](https://attack.mitre.org/groups/G1057) has exploited known vulnerabilities in internet-facing servers.(Citation: ElecticIQ Buyukkaya_ShinyHunters_Sept2025)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access | T1195.001 | Compromise Software Dependencies and Development Tools | [ShinyHunters](https://attack.mitre.org/groups/G1057) has compromised CI/CD pipelines by gaining access to high privilege engineering accounts on Git version control, BrowserStack, JFrog and other cloud project management platforms.(Citation: ElecticIQ Buyukkaya_ShinyHunters_Sept2025)    |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1203 | Exploitation for Client Execution | [ShinyHunters](https://attack.mitre.org/groups/G1057) has exploited vulnerabilities in the target company’s GitHub repository source code to enable more complex follow-on third-party or supply chain attacks.(Citation: Intel471_SH_Aug2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Lateral Movement | T1210 | Exploitation of Remote Services | [ShinyHunters](https://attack.mitre.org/groups/G1057) has exploited vulnerabilities in remote services for lateral movement.(Citation: SOCRadar_ShinyHunters_Mar2024)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Collection | T1213.003 | Code Repositories | [ShinyHunters](https://attack.mitre.org/groups/G1057) has gathered information from and has searched for vulnerabilities in the target company’s GitHub repository source code.(Citation: Intel471_SH_Aug2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Collection | T1213.006 | Databases | [ShinyHunters](https://attack.mitre.org/groups/G1057) has collected Salesforce datasets from victims in the airline and retail sectors.(Citation: ElecticIQ Buyukkaya_ShinyHunters_Sept2025)     |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1219 | Remote Access Tools | [ShinyHunters](https://attack.mitre.org/groups/G1057) has used MeshCentral and [ConnectWise](https://attack.mitre.org/software/S0591) to gain initial access, to run administrative command queries and to deploy the custom lateral movement and defacement script [victim_abbreviation]_fanout.sh.(Citation: Google_SHOracle_Jun2026)(Citation: ElecticIQ Buyukkaya_ShinyHunters_Sept2025)    |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Impact | T1485 | Data Destruction | [ShinyHunters](https://attack.mitre.org/groups/G1057) has executed the `DeleteBucket` API call to delete buckets.(Citation: Unit42KelleyVaya_BlingLibra_Aug2024)    |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Impact | T1491.001 | Internal Defacement | [ShinyHunters](https://attack.mitre.org/groups/G1057) has left ransom notes titled README-IF-YOU-SEE-THIS-YOUVE-BEEN-HACKED.TXT.(Citation: Google_SHOracle_Jun2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Credential Access | T1528 | Steal Application Access Token | [ShinyHunters](https://attack.mitre.org/groups/G1057) has stolen valid OAuth credentials from DevOps personnel or a company GitHub repository.(Citation: Intel471_SH_Aug2021) Additionally, [ShinyHunters](https://attack.mitre.org/groups/G1057) has stolen application access tokens to access cloud services and to bypass authentication mechanisms.(Citation: SOCRadar_ShinyHunters_Mar2024)    |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Collection | T1530 | Data from Cloud Storage | [ShinyHunters](https://attack.mitre.org/groups/G1057) has collected data from insecure cloud buckets.(Citation: SOCRadar_ShinyHunters_Mar2024)    |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Lateral Movement | T1550.001 | Application Access Token | [ShinyHunters](https://attack.mitre.org/groups/G1057) has used stolen OAuth keys to access cloud infrastructure and to bypass two-factor authentication.(Citation: Intel471_SH_Aug2021)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Credential Access | T1552.001 | Credentials In Files | [ShinyHunters](https://attack.mitre.org/groups/G1057) has gathered PII from database infrastructure.(Citation: Intel471_SH_Aug2021)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Collection | T1560.002 | Archive via Library | [ShinyHunters](https://attack.mitre.org/groups/G1057) has used the following command to compress collected data: ` pv -s "$(du -sb exfil \| awk '{print $1}')" \| zstd -3 -T0 -o exfil.tar.zst `.(Citation: Google_SHOracle_Jun2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Exfiltration | T1567 | Exfiltration Over Web Service | [ShinyHunters](https://attack.mitre.org/groups/G1057) has used compromised Salesforce CRM (Customer Relationship Management) dashboards to exfiltrate bulk data. Additionally, [ShinyHunters](https://attack.mitre.org/groups/G1057) has used LimeWire, a file-sharing service, to showcase samples of stolen data.(Citation: ElecticIQ Buyukkaya_ShinyHunters_Sept2025)    |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1573.002 | Asymmetric Cryptography | [ShinyHunters](https://attack.mitre.org/groups/G1057) has established a connection between the staging host and the C2 using SSH.(Citation: Google_SHOracle_Jun2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1580 | Cloud Infrastructure Discovery | [ShinyHunters](https://attack.mitre.org/groups/G1057) has used Amazon Simple Storage Service (S3) Browser and WinSCP to collect information on S3 bucket configurations.(Citation: Unit42KelleyVaya_BlingLibra_Aug2024)(Citation: SOCRadar_ShinyHunters_Mar2024)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1583.001 | Domains | [ShinyHunters](https://attack.mitre.org/groups/G1057) has established clearnet and Tor data leak sites (DLS) including one named “SHINYHUNTERS” for the exfiltration and posting of stolen data.(Citation: Mandiant_SHDataTheft_Jan2026)(Citation: FBI_SHLMS_May2026) Additionally, [ShinyHunters](https://attack.mitre.org/groups/G1057) has registered domains that mimic legitimate Microsoft Azure NetApp Files endpoints, such as azurenetfiles[.]net, and legitimate Okta SSO login pages, such as trial-6857053.okta[.]com.(Citation: Google_SHOracle_Jun2026)(Citation: ElecticIQ Buyukkaya_ShinyHunters_Sept2025)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1583.004 | Server | [ShinyHunters](https://attack.mitre.org/groups/G1057) has used five IP addresses to host Python SimpleHTTP servers on port 8888, which exposed staging materials, customized agents, and .bash_history files.(Citation: Google_SHOracle_Jun2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1585.002 | Email Accounts | [ShinyHunters](https://attack.mitre.org/groups/G1057) has established multiple email accounts, such as shinycorp@tutonota[.]com, for use in extortion activities.(Citation: Google Salesforce JUN 2025)(Citation: Unit42KelleyVaya_BlingLibra_Aug2024)    |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1587.004 | Exploits | [ShinyHunters](https://attack.mitre.org/groups/G1057) has exploited zero-day vulnerability CVE-2026-35273 against Oracle PeopleSoft application infrastructure.(Citation: Google_SHOracle_Jun2026) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1588.002 | Tool | [ShinyHunters](https://attack.mitre.org/groups/G1057) has obtained MeshCentral to deploy agents masquerading as legitimate cloud endpoints.(Citation: Google_SHOracle_Jun2026) [ShinyHunters](https://attack.mitre.org/groups/G1057) has obtained WinSCP to gather information on S3 bucket configurations.(Citation: Unit42KelleyVaya_BlingLibra_Aug2024) [ShinyHunters](https://attack.mitre.org/groups/G1057) has obtained [ConnectWise](https://attack.mitre.org/software/S0591) and other RMM tools to gain initial access.(Citation: ElecticIQ Buyukkaya_ShinyHunters_Sept2025)        |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1588.007 | Artificial Intelligence | [ShinyHunters](https://attack.mitre.org/groups/G1057) has used Bland AI to create conversational pathways tailored to specific scenarios during voice phishing attacks.(Citation: ElecticIQ Buyukkaya_ShinyHunters_Sept2025)    |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Reconnaissance | T1589.001 | Credentials | [ShinyHunters](https://attack.mitre.org/groups/G1057) has collected credentials containing PII, ultimately selling the information on their DLS.(Citation: Intel471_SH_Aug2021)(Citation: Unit42KelleyVaya_BlingLibra_Aug2024)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Reconnaissance | T1593.003 | Code Repositories | [ShinyHunters](https://attack.mitre.org/groups/G1057) has searched through target companies’ GitHub repositories for login credentials or API keys.(Citation: SOCRadar_ShinyHunters_Mar2024)    |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Reconnaissance | T1595.002 | Vulnerability Scanning | [ShinyHunters](https://attack.mitre.org/groups/G1057) has searched through victim companies’ GitHub repositories for vulnerabilities.(Citation: SOCRadar_ShinyHunters_Mar2024)    |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Reconnaissance | T1598 | Phishing for Information | [ShinyHunters](https://attack.mitre.org/groups/G1057) has sent phishing emails to Microsoft Office 365 corporate users in order to steal credentials.(Citation: Intel471_SH_Aug2021)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Reconnaissance | T1598.003 | Spearphishing Link | [ShinyHunters](https://attack.mitre.org/groups/G1057) has used spearphishing emails with malicious links to gain initial access and credentials.(Citation: SOCRadar_ShinyHunters_Mar2024)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1619 | Cloud Storage Object Discovery | [ShinyHunters](https://attack.mitre.org/groups/G1057) has used Amazon Simple Storage Service (S3) Browser and WinSCP to access S3 objects.(Citation: Unit42KelleyVaya_BlingLibra_Aug2024)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Impact | T1657 | Financial Theft | [ShinyHunters](https://attack.mitre.org/groups/G1057) has called or sent text messages or emails to employees of victim organizations to demand payment in Bitcoin within 72 hours. Email addresses used in extortion activities include shinycorp@tuta[.]com, shinygroup@tuta[.]com, shinycorp@tutanota[.]com, and shinygroup@onionmail[.]com.(Citation: Google Salesforce JUN 2025)(Citation: Mandiant_SHDataTheft_Jan2026)(Citation: FBI_SHLMS_May2026)(Citation: Intel471_SH_Aug2021)(Citation: Unit42KelleyVaya_BlingLibra_Aug2024)(Citation: SOCRadar_ShinyHunters_Mar2024)(Citation: ElecticIQ Buyukkaya_ShinyHunters_Sept2025)   |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1684 | Social Engineering | [ShinyHunters](https://attack.mitre.org/groups/G1057) has used social engineering to demand payment from victims.(Citation: FBI_SHLMS_May2026)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

## IOC／artifact概要

- IOC値: 13件
- IOC観測: 22件
- 複数攻撃で観測: 0件
- 要レビュー候補: 5件
- 非IOC artifact観測: 0件（`artifacts.csv`）

## 主要判断と不確実性

主要判断なし

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.
- parse-daily/unknown-clusters.json の unknown-cluster--shinyhunters は本プロファイルへ統合(merged)したが、同台帳が保持する観測4件(Health-ISAC 2026-07-30、Brinks Home 2026-07-31、ReliaQuest 2026-08-26、McKesson SEC Form 8-K 2026-08-29)は活動としては取り込んでいない。被害組織3社の開示はいずれもShinyHuntersを名指ししておらず、帰属が攻撃者の犯行主張と報道に依存するためである。犯行主張のみを根拠とする活動を本リポジトリでどう扱うかの方針が未決であり、方針決定後に観測単位で再判断する。
- 2026-09-14の走査で、フロリダ州DAVIDデータベース侵害について州当局の公式確認が得られた。フロリダ州高速道路安全自動車局(FLHSMV)は2026-09-11に「On September 4, 2026, FLHSMV learned of a data breach conducted by an international cybercriminal organization」と公表し、Plant City警察署の職員1名の資格情報が個人所有端末へ不適切に保存されていたものを悪用された経路も示した。ただしFLHSMVは実行主体を「international cybercriminal organization」とのみ表現してShinyHuntersを名指しせず、同集団が主張する20万件超という件数も確認していない。すなわち確認されたのは侵害の発生であって帰属ではないため、犯行主張のみを根拠とする活動の扱いという上記の未決方針は解消していない。関連レコード(unc6240|https://x.com/flhsmv/status/2098239548660514979)は不採用として判断理由を保存している。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--daily-02e1336153d9062de8f2 | Mandiant、ShinyHuntersがSSOを悪用してクラウドデータを窃取する手口を詳述 | bleepingcomputer.com | 2026-02-02 | https://www.bleepingcomputer.com/news/security/mandiant-details-how-shinyhunters-abuse-sso-to-steal-cloud-data/ | osint-report | TLP:CLEAR | 中 |
| source--daily-8012423fa9a259605e9c | Salesforce攻撃後にFarmers Insuranceのデータ侵害、110万人に影響 | bleepingcomputer.com | 2025-08-26 | https://www.bleepingcomputer.com/news/security/farmers-insurance-data-breach-impacts-11m-people-after-salesforce-attack/ | osint-report | TLP:CLEAR | 中 |
| source--unc6240--2c7acfc0f73ec191 | ShinyHunters |  | 不明 | cybercrime/ShinyHunters/ShinyHunters.pdf | report | TLP:CLEAR | 中 |
| source--unc6240--ddfed6d1e692a60c | cybersecurity forecast 2026 en |  | 2026 | summary/2025/cybersecurity-forecast-2026-en.pdf | report | TLP:CLEAR | 中 |
| source--unc6240--df2a78f9305a5534 | unc6240 |  | 不明 | actor_profile/evidence/unc6240.csv | structured-data | TLP:CLEAR | 中 |
| source--gtig-adversarial-ai-2026 | GTIG AI Threat Tracker: From Prompting to Autonomy - The Evolution of Adversarial AI | Google Threat Intelligence Group | 2026-09-08 | https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai | vendor-research | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--mitre-attack-g1057 | ShinyHunters, Group G1057 | MITRE ATT&CK | 2026-07-31 | https://attack.mitre.org/groups/G1057/ | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--gtig-unc6040-salesforce-vishing-2025 | The Cost of a Call: From Voice Phishing to Data Extortion | Google Threat Intelligence Group | 2025-06-04 | https://cloud.google.com/blog/topics/threat-intelligence/voice-phishing-data-extortion | vendor-threat-research | TLP:CLEAR | 高 |
| source--gtig-shinyhunters-saas-clusters-2026 | Vishing for Access: Tracking the Expansion of ShinyHunters-Branded SaaS Data Theft | Mandiant / Google Threat Intelligence Group | 2026-01-30 | https://cloud.google.com/blog/topics/threat-intelligence/expansion-shinyhunters-saas-data-theft | vendor-threat-research | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
