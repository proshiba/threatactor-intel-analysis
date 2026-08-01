# ZIRCONIUM 脅威アクタープロファイル

- プロファイルID: `actor--zirconium`
- 状態: draft
- 更新日時: 2026-07-29T23:13:55Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

ZIRCONIUMの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **ZIRCONIUM**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| APT31 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Violet Typhoon | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Hurricane Panda | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 54; mapping requires review. |
| BRONZE VINEWOOD | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 54; mapping requires review. |
| Black Vine | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 54; mapping requires review. |
| TEMP.Avengers | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 54; mapping requires review. |
| Zirconium, TA412 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook China row 54; mapping requires review. |

## 帰属

The repository mapping workbook places this actor in the China worksheet.

- 国: China
- スポンサー種別: state
- 確度: 中
- 証拠: `source--actor-mapping-workbook`

## モチベーション

未評価

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Hurricane Panda | overlaps-with | 共有alias: APT31, Zirconium, ZIRCONIUM | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |
| Violet Typhoon | overlaps-with | 共有alias: APT31, Violet Typhoon, ZIRCONIUM | 低 | `source--mitre-attack-19-1`, `source--actor-mapping-workbook` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) is a threat group operating out of China, active since at least 2017, that has targeted individuals associated with the 2020 US presidential election and prominent leaders in the international affairs community.(Citation: Microsoft Targeting Elections September 2020)(Citation: Check Point APT31 February 2021) |
| Capability | China Chopper Webshell, PlugX, Mimikatz, Sakula |
| Infrastructure |  |
| Victim | Aerospace, Healthcare, Energy (gas & electric turbine manufacturing), Military and defense, Finance, Agriculture, Technology, Japan, United States, United Kingdom, India, Canada, Brazil, South Africa, Australia, Thailand, South Korea, France, Switzerland, Sweden, Finland, Norway |
| Socio-political | China |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | APT 17, Deputy Dog, Elderwood, Sneaky Panda | single-alias-intersection | 中 | China | http://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-elderwood-project.pdf<br>https://intrusiontruth.wordpress.com/2019/07/24/apt17-is-run-by-the-jinan-bureau-of-the-chinese-ministry-of-state-security/<br>https://intezer.com/evidence-aurora-operation-still-active-supply-chain-attack-through-ccleaner/ |
| etda-threat-group-cards | APT 31, Judgment Panda, Zirconium | canonical-name | 高 | China | https://blog.confiant.com/uncovering-2017s-largest-malvertising-operation-b84cd38d6b85<br>https://blog.confiant.com/zirconium-was-one-step-ahead-of-chromes-redirect-blocker-with-0-day-2d61802efd0d<br>https://threatpost.com/microsoft-offers-analysis-of-zero-day-being-exploited-by-zirconium-group/124600/ |
| etda-threat-group-cards | Hurricane Panda | single-alias-intersection | 中 | China | https://www.crowdstrike.com/blog/cyber-deterrence-in-action-a-story-of-one-long-hurricane-panda-campaign/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Hurricane+Panda&n=1 |
| etda-threat-group-cards | Turbine Panda, APT 26, Shell Crew, WebMasters, KungFu Kittens | single-alias-intersection | 中 | China | https://paper.seebug.org/papers/APT/APT_CyberCriminal_Campagin/2014/h12756-wp-shell-crew.pdf<br>https://www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-black-vine-cyberespionage-group.pdf<br>https://www.crowdstrike.com/resources/wp-content/brochures/reports/huge-fan-of-your-work-intelligence-report.pdf |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Violet Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | APT19 | multiple-name-intersection | 高 | CN, China | http://cybercampaigns.net/wp-content/uploads/2013/06/Deep-Panda.pdf<br>https://docs.huihoo.com/rsaconference/usa-2014/anf-t07b-the-art-of-attribution-identifying-and-pursuing-your-cyber-adversaries-final.pdf<br>https://www.cfr.org/interactive/cyber-operations/deep-panda |
| misp-threat-actor | HURRICANE PANDA | single-alias-intersection | 中 | CN | http://www.crowdstrike.com/blog/cyber-deterrence-in-action-a-story-of-one-long-hurricane-panda-campaign/<br>https://www.crowdstrike.com/blog/crowdstrike-discovers-use-64-bit-zero-day-privilege-escalation-exploit-cve-2014-4113-hurricane-panda/<br>https://www.crowdstrike.com/blog/storm-chasing/ |
| misp-threat-actor | APT31 | canonical-name | 高 | CN | https://www.microsoft.com/security/blog/2017/03/27/detecting-and-mitigating-elevation-of-privilege-exploit-for-cve-2017-0005/<br>https://duo.com/decipher/apt-groups-moving-down-the-supply-chain<br>https://go.recordedfuture.com/hubfs/reports/cta-2019-0206.pdf |
| misp-microsoft-activity-group | Violet Typhoon | canonical-name | 高 | CN, China | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | ZIRCONIUM | canonical-name | 高 |  | https://blogs.technet.microsoft.com/mmpc/2017/03/27/detecting-and-mitigating-elevation-of-privilege-exploit-for-cve-2017-0005/ |
| misp-mitre-enterprise-intrusion-set | Deep Panda - G0009 | single-alias-intersection | 中 |  | https://attack.mitre.org/wiki/Group/G0009<br>https://blog.crowdstrike.com/deep-thought-chinese-targeting-national-security-think-tanks/<br>https://www.threatconnect.com/the-anthem-hack-all-roads-lead-to-china/ |
| misp-mitre-intrusion-set | Deep Panda - G0009 | single-alias-intersection | 中 |  | https://attack.mitre.org/groups/G0009<br>https://web.archive.org/web/20170823094836/http:/www.symantec.com/content/en/us/enterprise/media/security_response/whitepapers/the-black-vine-cyberespionage-group.pdf<br>https://web.archive.org/web/20171017072306/https://icitech.org/icit-brief-chinas-espionage-dynasty-economic-death-by-a-thousand-cuts/ |
| misp-mitre-intrusion-set | ZIRCONIUM - G0128 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0128<br>https://blogs.microsoft.com/on-the-issues/2020/09/10/cyberattacks-us-elections-trump-biden/<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide |
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
| malware--china-chopper-webshell | China Chopper Webshell | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--plugx | PlugX | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--mimikatz | Mimikatz | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--sakula | Sakula | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

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
| Op. Poisoned Hurricane | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| Op. Poisoned Hurricane | ZIRCONIUM | 情報なし | 情報なし | 情報なし | 情報なし | 情報なし | 中 |

Op. Poisoned Hurricane

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | インド | Targeting text mentions india. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | オーストラリア | Targeting text mentions australia. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | カナダ | Targeting text mentions canada. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | スイス | Targeting text mentions switzerland. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | スウェーデン | Targeting text mentions sweden. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | タイ | Targeting text mentions thailand. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | チェコ | 構造化OSINTの被害国フィールドでZIRCONIUMの標的・被害国としてチェコが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ノルウェー | Targeting text mentions norway. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | フィンランド | レビュー済みアクターマッピングの標的欄に記録されたフィンランドを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | フランス | Targeting text mentions france. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | ブラジル | Targeting text mentions brazil. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | ベラルーシ | 構造化OSINTの被害国フィールドでZIRCONIUMの標的・被害国としてベラルーシが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | モンゴル | 構造化OSINTの被害国フィールドでZIRCONIUMの標的・被害国としてモンゴルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ロシア | 構造化OSINTの被害国フィールドでZIRCONIUMの標的・被害国としてロシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 南アフリカ | レビュー済みアクターマッピングの標的欄に記録された南アフリカを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | 日本 | Targeting text mentions japan. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| countries | 米国 | Targeting text mentions united states. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| countries | 英国 | Targeting text mentions united kingdom. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| countries | 韓国 | Targeting text mentions south korea. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| regions | アフリカ | レビュー済みアクターマッピングの標的欄に記録されたアフリカを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| regions | 北米 | カナダ、米国で確認された標的・被害事例を北米として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1`, `source--target-audit-etda-threat-group-cards`, `source--target-audit-misp-threat-actor` |
| regions | 東アジア | モンゴル、日本、韓国で確認された標的・被害事例を東アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| regions | 東欧 | チェコ、ベラルーシ、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | スイス、スウェーデン、チェコ、ノルウェー、フィンランド、フランス、ベラルーシ、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-etda-threat-group-cards` |
| sectors | Defense | Targeting text indicates the Defense sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Energy | Targeting text indicates the Energy sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Finance | Targeting text indicates the Finance sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Healthcare | Targeting text indicates the Healthcare sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Manufacturing | Targeting text indicates the Manufacturing sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Technology | Targeting text indicates the Technology sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Discovery | T1012 | Query Registry | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used a tool to query the Registry for proxy settings.(Citation: Zscaler APT31 Covid-19 October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used a tool to enumerate proxy settings in the target environment.(Citation: Zscaler APT31 Covid-19 October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.002 | Software Packing | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used multi-stage packers for exploit code.(Citation: Check Point APT31 February 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used a tool to capture the username on a compromised host in order to register it with C2.(Citation: Zscaler APT31 Covid-19 October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036 | Masquerading | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has spoofed legitimate applications in phishing lures and changed file extensions to conceal  installation of malware.(Citation: Google Election Threats October 2020)(Citation: Zscaler APT31 Covid-19 October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.004 | Masquerade Task or Service | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has created a run key named <code>Dropbox Update Setup</code> to mask a persistence mechanism for a malicious binary.(Citation: Zscaler APT31 Covid-19 October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has exfiltrated files via the Dropbox API C2.(Citation: Zscaler APT31 Covid-19 October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used a tool to open a Windows Command Shell on a remote host.(Citation: Zscaler APT31 Covid-19 October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.006 | Python | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used Python-based implants to interact with compromised hosts.(Citation: Google Election Threats October 2020)(Citation: Zscaler APT31 Covid-19 October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1068 | Exploitation for Privilege Escalation | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has exploited CVE-2017-0005 for local privilege escalation.(Citation: Check Point APT31 February 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used a tool to capture the processor architecture of a compromised host in order to register it with C2.(Citation: Zscaler APT31 Covid-19 October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090.003 | Multi-hop Proxy | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has utilized an ORB (operational relay box) network – consisting compromised devices such as small office and home office (SOHO) routers, IoT devices, and leased virtual private servers (VPS) – to proxy traffic.(Citation: ORB Mandiant)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102.002 | Bidirectional Communication | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used Dropbox for C2 allowing upload and download of files as well as execution of arbitrary commands.(Citation: Google Election Threats October 2020)(Citation: Zscaler APT31 Covid-19 October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used tools to download malicious files to compromised hosts.(Citation: Zscaler APT31 Covid-19 October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1124 | System Time Discovery | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used a tool to capture the time on a compromised host in order to register it with C2.(Citation: Zscaler APT31 Covid-19 October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used the AES256 algorithm with a SHA1 derived key to decrypt exploit code.(Citation: Check Point APT31 February 2021) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used malicious links in e-mails to lure victims into downloading malware.(Citation: Google Election Threats October 2020)(Citation: Zscaler APT31 Covid-19 October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.007 | Msiexec | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used the msiexec.exe command-line utility to download and execute malicious MSI files.(Citation: Zscaler APT31 Covid-19 October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1547.001 | Registry Run Keys / Startup Folder | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has created a Registry Run key named <code>Dropbox Update Setup</code> to establish persistence for a malicious Python binary.(Citation: Zscaler APT31 Covid-19 October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.003 | Credentials from Web Browsers | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used a tool to steal credentials from installed web browsers including Microsoft Internet Explorer and Google Chrome.(Citation: Zscaler APT31 Covid-19 October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.002 | Spearphishing Link | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used malicious links in e-mails to deliver malware.(Citation: Microsoft Targeting Elections September 2020)(Citation: Google Election Threats October 2020)(Citation: Zscaler APT31 Covid-19 October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has exfiltrated stolen data to Dropbox.(Citation: Zscaler APT31 Covid-19 October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573.001 | Symmetric Cryptography | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used AES encrypted communications in C2.(Citation: Zscaler APT31 Covid-19 October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has purchased domains for use in targeted campaigns.(Citation: Microsoft Targeting Elections September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.006 | Web Services | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used GitHub to host malware linked in spearphishing e-mails.(Citation: Google Election Threats October 2020)(Citation: Zscaler APT31 Covid-19 October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1584.008 | Network Devices | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has compromised network devices such as small office and home office (SOHO) routers and IoT devices for ORB (operational relay box) [Proxy](https://attack.mitre.org/techniques/T1090) networks.(Citation: ORB APT31)(Citation: ORB Mandiant)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1598 | Phishing for Information | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) targeted presidential campaign staffers with credential phishing e-mails.(Citation: Google Election Threats October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1598.003 | Spearphishing Link | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has used web beacons in e-mails to track hits to attacker-controlled URL's.(Citation: Microsoft Targeting Elections September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1665 | Hide Infrastructure | [ZIRCONIUM](https://attack.mitre.org/groups/G0128) has utilized an ORB (operational relay box) network – consisting compromised devices such as small office and home office (SOHO) routers, IoT devices, and leased virtual private servers (VPS) – to obfuscate the origin of C2 traffic.(Citation: ORB Mandiant)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 2件
- IOC観測: 2件
- 複数攻撃で観測: 0件
- 要レビュー候補: 2件
- 非IOC artifact観測: 64件（`artifacts.csv`）

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
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--zirconium--697d8c01c0f19339 | zirconium |  | 不明 | actor_profile/evidence/zirconium.csv | structured-data | TLP:CLEAR | 中 |
| source--zirconium--dd1b7d29d2c342de | 0day  In the Wild |  | 不明 | 0day _In the Wild_.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--zirconium--a1b549c321c12989 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--zirconium--3f1ac4692a5526cb | A three beat waltz The ecosystem behind Chinese state sponsored cyber threats |  | 不明 | International Strategic/China/A-three-beat-waltz-The-ecosystem-behind-Chinese-state-sponsored-cyber-threats.pdf | report | TLP:CLEAR | 中 |
| source--zirconium--d9b40fdc3a722385 | Charting China’s Climb as a Leading Global Cyber Power |  | 不明 | International Strategic/China/Charting China’s Climb as a Leading Global Cyber Power.pdf | report | TLP:CLEAR | 中 |
| source--zirconium--4b9dd71f4680ed26 | china cyber report |  | 不明 | International Strategic/China/china-cyber-report.pdf | report | TLP:CLEAR | 中 |
| source--zirconium--3bd1556baaf50cbf | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--zirconium--14be4719baf5914e | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--zirconium--399ff98834a7c9d3 | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--zirconium--757e14936b431285 | 2021(APT) Microsoft Digital Defense Report |  | 2021 | summary/2021/2021(APT) Microsoft Digital Defense Report.pdf | report | TLP:CLEAR | 中 |
| source--zirconium--ba5cd7da7e379e6b | rpt security predictions 2021 fireeye |  | 2021 | summary/2021/rpt-security-predictions-2021-fireeye.pdf | report | TLP:CLEAR | 中 |
| source--zirconium--152e68fc4f2455a4 | Modern Asian APT groups TTPs report eng |  | 不明 | summary/2023/Modern-Asian-APT-groups-TTPs_report_eng.pdf | report | TLP:CLEAR | 中 |
| source--zirconium--f520b53b8ab352ef | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--zirconium--81c17a78f73d6169 | kaspersky ics cert apt attacks on industrial organizations in h2 2022 en |  | 2022 | summary/2023/kaspersky-ics-cert-apt-attacks-on-industrial-organizations-in-h2-2022-en.pdf | report | TLP:CLEAR | 中 |
| source--zirconium--09fe2a34952c8404 | 2023 Adversary Infrastructure Report |  | 2023 | summary/2024/2023 Adversary Infrastructure Report .pdf | report | TLP:CLEAR | 中 |
| source--zirconium--7f193d6c25852183 | CERTFR 2024 CTI 002 |  | 2024 | summary/2024/CERTFR-2024-CTI-002.pdf | report | TLP:CLEAR | 中 |
| source--zirconium--a74565c0efcc49fa | Hurdling Over Hazards  Multifaceted Threats to the Paris Olympics |  | 不明 | summary/2024/Hurdling Over Hazards- Multifaceted Threats to the Paris Olympics.pdf | report | TLP:CLEAR | 中 |
| source--zirconium--b4a9854e4f9739ad | state of the threat report 2024 |  | 2024 | summary/2024/state-of-the-threat-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--zirconium--7ad663632c9695c8 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--zirconium--b6e7595230a38411 | 2025 Cyber Security Report Final |  | 2025 | summary/2025/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--zirconium--f52d334cc84eed9b | eset apt activity report q4 2024 q1 2025 |  | 2024 | summary/2025/eset-apt-activity-report-q4-2024-q1-2025.pdf | report | TLP:CLEAR | 中 |
| source--zirconium--5de9fb3672988a03 | 2025 Cyber Security Report Final |  | 2025 | summary/2026/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--zirconium--03d58f007a29d0e8 | CERTFR 2026 CTI 003 |  | 2026 | summary/2026/CERTFR-2026-CTI-003.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
