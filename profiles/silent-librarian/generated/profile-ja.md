# Silent Librarian 脅威アクタープロファイル

- プロファイルID: `actor--silent-librarian`
- 状態: draft
- 更新日時: 2026-08-28T15:27:20Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

Silent Librarianの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Silent Librarian**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Cobalt Dickens | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Mabna Institute | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TA407 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Yellow Nabu | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

## 帰属

The repository mapping workbook places this actor in the Iran worksheet.

- 国: Iran
- スポンサー種別: state
- 確度: 中
- 証拠: `source--actor-mapping-workbook`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | State-sponsored intelligence collection or strategic operations. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

## 他アクターとの関係

確認された関係なし

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [Silent Librarian](https://attack.mitre.org/groups/G0122) is a group that has targeted research and proprietary data at universities, government agencies, and private sector companies worldwide since at least 2013. Members of  [Silent Librarian](https://attack.mitre.org/groups/G0122) are known to have been affiliated with the Iran-based Mabna Institute which has conducted cyber intrusions at the behest of the government of Iran, specifically the Islamic Revolutionary Guard Corps (IRGC).(Citation: DOJ Iran Indictments March 2018)(Citation: Phish Labs Silent Librarian)(Citation: Malwarebytes Silent Librarian October 2020) |
| Capability |  |
| Infrastructure |  |
| Victim | 144 universities in the United States, 176 foreign universities in 21 countries, five federal and state government agencies in the United States, 36 private companies in the United States, 11 foreign private companies, and two international non-governmental organizations |
| Socio-political | Iran |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Mabna Institute, Cobalt Dickens, Silent Librarian | canonical-name | 高 | Iran | https://www.proofpoint.com/us/threat-insight/post/threat-actor-profile-ta407-silent-librarian<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Mabna+Institute%2C+Cobalt+Dickens%2C+Silent+Librarian&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Silent Librarian | canonical-name | 高 | IR | https://info.phishlabs.com/blog/silent-librarian-more-to-the-story-of-the-iranian-mabna-institute-indictment<br>https://info.phishlabs.com/blog/silent-librarian-university-attacks-continue-unabated-in-days-following-indictment<br>https://www.justice.gov/usao-sdny/pr/nine-iranians-charged-conducting-massive-cyber-theft-campaign-behalf-islamic |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Silent Librarian - G0122 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0122<br>https://blog.malwarebytes.com/malwarebytes-news/2020/10/silent-librarian-apt-phishing-attack/<br>https://info.phishlabs.com/blog/silent-librarian-more-to-the-story-of-the-iranian-mabna-institute-indictment |
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

未確認

### ツール

未確認

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
| 米国、Mabna Institute所属とされるイラン人17人を追起訴 | law-enforcement-action | 2026-08-18 | 2026-08-18 | 2026-08-20 |  |  |  |  | 米司法省は2026年8月18日、Mabna Instituteに所属するとされるイラン人17人を対象とする14件の訴因からなる追起訴状(superseding S2 indictment)を開封した。うち9人は2018年3月に公表された7訴因の起訴状で既に訴追されており、本件で8人が追加された。米国務省は17人のうち5人の所在につながる情報へ最大1,000万ドルの報奨金を設定している。対象となった犯行期間そのものは activity--silent-librarian-mabna-campaign-2013-2017 に分離した。 | 中 | `source--daily-ac0aab951821b27df384`, `source--doj-mabna-institute-indictment-2026` |
| Mabna Instituteによる学術・知的財産窃取キャンペーン | cyber-espionage | 2013 | 2017-12 | 2026-08-18 | target--activity-rule--country--9e0b33ddb91d0135fb82, target--activity-rule--sector--d406c8e5b7fa7aeff7d2, target--activity-rule--sector--e7608f51421ca8b1e297, target--country--united-states |  |  | victim--activity-rule--b5da905da954ea14cd81 | Mabna Instituteに所属するとされるイラン人17人が、2013年頃から2017年12月まで継続した協調的なサイバー侵入キャンペーンを実行した。米国内144大学、国外178大学、米国内私企業42社以上、国外私企業11社以上、米連邦および州政府機関5機関以上、NGO 2団体を標的とし、世界中の教授10万件超のアカウントを狙って約8,000件の侵害に成功した。窃取したのは論文、学位論文、電子書籍、研究資料等31.5TB超で、米国内大学の調達費用に換算して34億ドル超と評価されている。窃取データはMegapaper.irおよびGigapaper.irを通じてイラン国内へ販売された。標的国には米国のほか、オーストラリア、カナダ、中国、日本、イスラエル、英国、トルコ、スイス、香港等が含まれる。 | 中 | `source--doj-mabna-institute-indictment-2026`, `source--daily-ac0aab951821b27df384` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| 米国、Mabna Institute所属とされるイラン人17人を追起訴 | Silent Librarian | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |
| Mabna Instituteによる学術・知的財産窃取キャンペーン | Silent Librarian | 情報なし | 情報なし | 情報なし | イラン, 非営利・市民社会, 教育・研究, 米国 | 被害事例: Mabna Instituteによる学術・知的財産窃取キャンペーン | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | イスラエル | 活動「Mabna Instituteによる学術・知的財産窃取キャンペーン」の記述で標的・被害国として明示されている。 | 2013 | 2017-12 | 中 | `source--daily-ac0aab951821b27df384`, `source--doj-mabna-institute-indictment-2026`, `source--target-audit-etda-threat-group-cards` |
| countries | イラン | 活動「Mabna Instituteによる学術・知的財産窃取キャンペーン」の記述で標的として明示された国・地域。 | 2013 | 2017-12 | 中 | `source--daily-ac0aab951821b27df384`, `source--doj-mabna-institute-indictment-2026` |
| countries | オーストラリア | 活動「Mabna Instituteによる学術・知的財産窃取キャンペーン」の記述で標的・被害国として明示されている。 | 2013 | 2017-12 | 中 | `source--daily-ac0aab951821b27df384`, `source--doj-mabna-institute-indictment-2026`, `source--target-audit-etda-threat-group-cards` |
| countries | カナダ | 活動「Mabna Instituteによる学術・知的財産窃取キャンペーン」の記述で標的・被害国として明示されている。 | 2013 | 2017-12 | 中 | `source--daily-ac0aab951821b27df384`, `source--doj-mabna-institute-indictment-2026`, `source--target-audit-etda-threat-group-cards` |
| countries | スイス | 活動「Mabna Instituteによる学術・知的財産窃取キャンペーン」の記述で標的・被害国として明示されている。 | 2013 | 2017-12 | 中 | `source--daily-ac0aab951821b27df384`, `source--doj-mabna-institute-indictment-2026`, `source--target-audit-etda-threat-group-cards` |
| countries | トルコ | 活動「Mabna Instituteによる学術・知的財産窃取キャンペーン」の記述で標的・被害国として明示されている。 | 2013 | 2017-12 | 中 | `source--daily-ac0aab951821b27df384`, `source--doj-mabna-institute-indictment-2026`, `source--target-audit-etda-threat-group-cards` |
| countries | 中国 | 活動「Mabna Instituteによる学術・知的財産窃取キャンペーン」の記述で標的・被害国として明示されている。 | 2013 | 2017-12 | 中 | `source--daily-ac0aab951821b27df384`, `source--doj-mabna-institute-indictment-2026`, `source--target-audit-etda-threat-group-cards` |
| countries | 日本 | 活動「Mabna Instituteによる学術・知的財産窃取キャンペーン」の記述で標的・被害国として明示されている。 | 2013 | 2017-12 | 中 | `source--daily-ac0aab951821b27df384`, `source--doj-mabna-institute-indictment-2026`, `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | Targeting text mentions united states. | 2013 | 2017-12 | 中 | `source--actor-mapping-workbook`, `source--daily-ac0aab951821b27df384`, `source--doj-mabna-institute-indictment-2026`, `source--target-audit-etda-threat-group-cards` |
| countries | 英国 | 活動「Mabna Instituteによる学術・知的財産窃取キャンペーン」の記述で標的・被害国として明示されている。 | 2013 | 2017-12 | 中 | `source--daily-ac0aab951821b27df384`, `source--doj-mabna-institute-indictment-2026`, `source--target-audit-etda-threat-group-cards` |
| countries | 香港 | 活動「Mabna Instituteによる学術・知的財産窃取キャンペーン」の記述で標的・被害国として明示されている。 | 2013 | 2017-12 | 中 | `source--daily-ac0aab951821b27df384`, `source--doj-mabna-institute-indictment-2026`, `source--target-audit-etda-threat-group-cards` |
| regions | 中東 | イスラエル、イラン、トルコで確認された標的・被害事例を中東として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-ac0aab951821b27df384`, `source--doj-mabna-institute-indictment-2026`, `source--target-audit-etda-threat-group-cards` |
| regions | 北米 | カナダ、米国で確認された標的・被害事例を北米として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--daily-ac0aab951821b27df384`, `source--doj-mabna-institute-indictment-2026`, `source--target-audit-etda-threat-group-cards` |
| regions | 東アジア | 中国、日本、香港で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-ac0aab951821b27df384`, `source--doj-mabna-institute-indictment-2026`, `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | スイス、トルコ、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--daily-ac0aab951821b27df384`, `source--doj-mabna-institute-indictment-2026`, `source--target-audit-etda-threat-group-cards` |
| sectors | 非営利・市民社会 | 活動「Mabna Instituteによる学術・知的財産窃取キャンペーン」の記述で標的として明示された産業。 | 2013 | 2017-12 | 中 | `source--daily-ac0aab951821b27df384`, `source--doj-mabna-institute-indictment-2026` |
| sectors | 教育・研究 | 活動「Mabna Instituteによる学術・知的財産窃取キャンペーン」の記述で標的として明示された産業。 | 2013 | 2017-12 | 中 | `source--daily-ac0aab951821b27df384`, `source--doj-mabna-institute-indictment-2026` |
| sectors | Government | Targeting text indicates the Government sector. | 2013 | 2017-12 | 中 | `source--actor-mapping-workbook`, `source--daily-ac0aab951821b27df384`, `source--mitre-attack-19-1` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Mabna Instituteによる学術・知的財産窃取キャンペーン | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--9e0b33ddb91d0135fb82, target--activity-rule--sector--d406c8e5b7fa7aeff7d2, target--activity-rule--sector--e7608f51421ca8b1e297, target--country--united-states |  |  |  |  | 2013 | 2017-12 | 2026-08-18 | 中 | `source--daily-ac0aab951821b27df384`, `source--doj-mabna-institute-indictment-2026` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [Silent Librarian](https://attack.mitre.org/groups/G0122) has used compromised credentials to obtain unauthorized access to online accounts.(Citation: DOJ Iran Indictments March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110.003 | Password Spraying | [Silent Librarian](https://attack.mitre.org/groups/G0122) has used collected lists of names and e-mail accounts to use in password spraying attacks against private sector targets.(Citation: DOJ Iran Indictments March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114 | Email Collection | [Silent Librarian](https://attack.mitre.org/groups/G0122) has exfiltrated entire mailboxes from compromised accounts.(Citation: DOJ Iran Indictments March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1114.003 | Email Forwarding Rule | [Silent Librarian](https://attack.mitre.org/groups/G0122) has set up auto forwarding rules on compromised e-mail accounts.(Citation: DOJ Iran Indictments March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [Silent Librarian](https://attack.mitre.org/groups/G0122) has acquired domains to establish credential harvesting pages, often spoofing the target organization and using free top level domains .TK, .ML, .GA, .CF, and .GQ.(Citation: DOJ Iran Indictments March 2018)(Citation: Phish Labs Silent Librarian)(Citation: Secureworks COBALT DICKENS August 2018)(Citation: Proofpoint TA407 September 2019)(Citation: Secureworks COBALT DICKENS September 2019)(Citation: Malwarebytes Silent Librarian October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.002 | Email Accounts | [Silent Librarian](https://attack.mitre.org/groups/G0122) has established e-mail accounts to receive e-mails forwarded from compromised accounts.(Citation: DOJ Iran Indictments March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [Silent Librarian](https://attack.mitre.org/groups/G0122) has obtained free and publicly available tools including SingleFile and HTTrack to copy login pages of targeted organizations.(Citation: Proofpoint TA407 September 2019)(Citation: Secureworks COBALT DICKENS September 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.004 | Digital Certificates | [Silent Librarian](https://attack.mitre.org/groups/G0122) has obtained free Let's Encrypt SSL certificates for use on their phishing pages.(Citation: Phish Labs Silent Librarian)(Citation: Secureworks COBALT DICKENS September 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589.002 | Email Addresses | [Silent Librarian](https://attack.mitre.org/groups/G0122) has collected e-mail addresses from targeted organizations from open Internet searches.(Citation: DOJ Iran Indictments March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1589.003 | Employee Names | [Silent Librarian](https://attack.mitre.org/groups/G0122) has collected lists of names for individuals from targeted organizations.(Citation: DOJ Iran Indictments March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1594 | Search Victim-Owned Websites | [Silent Librarian](https://attack.mitre.org/groups/G0122) has searched victim's websites to identify the interests and academic areas of targeted individuals and to scrape source code, branding, and organizational contact information for phishing pages.(Citation: DOJ Iran Indictments March 2018)(Citation: Phish Labs Silent Librarian)(Citation: Proofpoint TA407 September 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1598.003 | Spearphishing Link | [Silent Librarian](https://attack.mitre.org/groups/G0122) has used links in e-mails to direct victims to credential harvesting websites designed to appear like the targeted organization's login page.(Citation: DOJ Iran Indictments March 2018)(Citation: Phish Labs Silent Librarian)(Citation: Secureworks COBALT DICKENS August 2018)(Citation: Proofpoint TA407 September 2019)(Citation: Secureworks COBALT DICKENS September 2019)(Citation: Malwarebytes Silent Librarian October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1608.005 | Link Target | [Silent Librarian](https://attack.mitre.org/groups/G0122) has cloned victim organization login pages and staged them for later use in credential harvesting campaigns. [Silent Librarian](https://attack.mitre.org/groups/G0122) has also made use of a variety of URL shorteners for these staged websites.(Citation: Secureworks COBALT DICKENS September 2019)(Citation: Malwarebytes Silent Librarian October 2020)(Citation: Proofpoint TA407 September 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 25件（`artifacts.csv`）

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
| source--daily-ac0aab951821b27df384 | 米国、34億ドル相当の知的財産窃取に関与したイラン人ハッカーを起訴 | justice.gov | 2026-08-20 | https://www.justice.gov/opa/pr/17-iranians-charged-conducting-massive-cyber-theft-campaign-behalf-islamic-revolutionary | osint-report | TLP:CLEAR | 中 |
| source--doj-mabna-institute-indictment-2026 | 17 Iranians Charged with Conducting Massive Cyber Theft Campaign on Behalf of the Islamic Revolutionary Guard Corps and Other Iranian Entities | U.S. Department of Justice, Office of Public Affairs | 2026-08-18 | https://www.justice.gov/opa/pr/17-iranians-charged-conducting-massive-cyber-theft-campaign-behalf-islamic-revolutionary | law-enforcement-release | TLP:CLEAR | 高 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--silent-librarian--08f205a61fe8698f | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--silent-librarian--3464e33fce328076 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--silent-librarian--3f2755172c94632d | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--silent-librarian--8face31a321e90fd | silent librarian |  | 不明 | actor_profile/evidence/silent-librarian.csv | structured-data | TLP:CLEAR | 中 |
| source--silent-librarian--946ba58701120acd | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--silent-librarian--c4f9158d7899ed12 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
