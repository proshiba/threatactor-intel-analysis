# APT38 脅威アクタープロファイル

- プロファイルID: `actor--apt38`
- 状態: draft
- 更新日時: 2026-08-01T23:18:25Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

APT38の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **APT38**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| BeagleBoyz | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Bluenoroff | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| COPERNICIUM | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| COPERNICIUM (Microsoft) | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| ElectricFish | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Genie Spider | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| NICKEL GLADSTONE | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Sapphire Sleet | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Stardust Chollima | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TA444 (Proofpoint) | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| TEMP.Hermit | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| G0082 | actor-mapping-workbook | unknown | 中 | `source--actor-mapping-workbook` | Workbook North Korea row 9; mapping requires review. |

## 帰属

The repository mapping workbook places this actor in the North Korea worksheet.

- 国: North Korea
- スポンサー種別: state
- 確度: 中
- 証拠: `source--actor-mapping-workbook`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | State-sponsored intelligence collection or strategic operations. | 低 | `source--actor-mapping-workbook` | Inferred from catalog actor type; corroborate with actor-specific reporting. |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Lazarus Group | overlaps-with | Government sources connect Bluenoroff/APT38 and Lazarus under the RGB and a common conspiracy, while industry reporting preserves APT38 as a financially focused cluster. | 高 | `source--treasury-dprk-groups-2019`, `source--doj-dprk-conspiracy-2021` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | [APT38](https://attack.mitre.org/groups/G0082) is a North Korean state-sponsored threat group that specializes in financial cyber operations; it has been attributed to the Reconnaissance General Bureau.(Citation: CISA AA20-239A BeagleBoyz August 2020) Active since at least 2014, [APT38](https://attack.mitre.org/groups/G0082) has targeted banks, financial institutions, casinos, cryptocurrency exchanges, SWIFT system endpoints, and ATMs in at least 38 countries worldwide. Significant operations include the 2016 Bank of Bangladesh heist, during which [APT38](https://attack.mitre.org/groups/G0082) stole $81 million, as well as attacks against Bancomext (Citation: FireEye APT38 Oct 2018) and Banco de Chile (Citation: FireEye APT38 Oct 2018); some of their attacks have been destructive.(Citation: CISA AA20-239A BeagleBoyz August 2020)(Citation: FireEye APT38 Oct 2018)(Citation: DOJ North Korea Indictment Feb 2021)(Citation: Kaspersky Lazarus Under The Hood Blog 2017)<br><br>North Korean group definitions are known to have significant overlap, and some security researchers report all North Korean state-sponsored cyber activity under the name [Lazarus Group](https://attack.mitre.org/groups/G0032) instead of tracking clusters or subgroups. |
| Capability | HOPLIGHT, DarkComet, KillDisk, ECCENTRICBANDWAGON, VOLGMER, PEACHPIT, Net, Mimikatz |
| Infrastructure |  |
| Victim | Korean Peninsula, US Aerospace, SWIFT-fraud operations in East Asia |
| Socio-political | North Korea |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | BeagleBoyz | single-alias-intersection | 中 | North Korea | https://us-cert.cisa.gov/ncas/alerts/aa20-239a<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Subgroup%3A+BeagleBoyz&n=1 |
| etda-threat-group-cards | Bluenoroff, APT 38, Stardust Chollima | canonical-name | 高 | North Korea | https://threatpost.com/lazarus-apt-spinoff-linked-to-banking-hacks/124746/<br>https://www.microsoft.com/en-us/security/blog/2024/11/22/microsoft-shares-latest-intelligence-on-north-korean-and-chinese-threat-actors-at-cyberwarcon/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Subgroup%3A+Bluenoroff%2C+APT+38%2C+Stardust+Chollima&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Sapphire Sleet | multiple-name-intersection | 高 | North Korea | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Lazarus Group | canonical-name | 高 | KP, Korea (Democratic People's Republic of) | https://threatpost.com/operation-blockbuster-coalition-ties-destructive-attacks-to-lazarus-group/116422/<br>https://www.us-cert.gov/ncas/alerts/TA17-164A<br>https://www.us-cert.gov/ncas/alerts/TA17-318A |
| misp-threat-actor | TEMP.Hermit | single-alias-intersection | 中 | KP | https://www.fireeye.com/blog/threat-research/2018/02/attacks-leveraging-adobe-zero-day.html |
| misp-threat-actor | STARDUST CHOLLIMA | multiple-name-intersection | 高 |  | https://www.crowdstrike.com/blog/big-game-hunting-with-ryuk-another-lucrative-targeted-ransomware/ |
| misp-microsoft-activity-group | Sapphire Sleet | multiple-name-intersection | 高 | KP, North Korea | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | APT38 - G0082 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0082<br>https://go.crowdstrike.com/rs/281-OBQ-266/images/Report2021GTR.pdf<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide |
| misp-360net | Lazarus - APT-C-26 | canonical-name | 高 | korea | https://apt.360.net/report/apts/9.html<br>https://apt.360.net/report/apts/101.html<br>https://apt.360.net/report/apts/90.html |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Lazarus Group | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| Operation Sharpshooter | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| STARDUST CHOLLIMA | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |
| TraderTraitor | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--daily-f30dd669ecd1c3776828 | typo-crypto | APT38との直接的な利用関係が一次資料レビューで確認されたマルウェア。 | 不明 | 不明 | 中 | `source--daily-a7e2c22924a222a6eb0f` |
| malware--darkcomet | DarkComet | [DarkComet](https://attack.mitre.org/software/S0334) is a Windows remote administration tool and backdoor.(Citation: TrendMicro DarkComet Sept 2014)(Citation: Malwarebytes DarkComet March 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--eccentricbandwagon | ECCENTRICBANDWAGON | [ECCENTRICBANDWAGON](https://attack.mitre.org/software/S0593) is a remote access Trojan (RAT) used by North Korean cyber actors that was first identified in August 2020. It is a reconnaissance tool--with keylogging and screen capture functionality--used for information gathering on compromised systems.(Citation: CISA EB Aug 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--hoplight | HOPLIGHT | [HOPLIGHT](https://attack.mitre.org/software/S0376) is a backdoor Trojan that has reportedly been used by the North Korean government.(Citation: US-CERT HOPLIGHT Apr 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--killdisk | KillDisk | [KillDisk](https://attack.mitre.org/software/S0607) is a disk-wiping tool designed to overwrite files with random data to render the OS unbootable. It was first observed as a component of [BlackEnergy](https://attack.mitre.org/software/S0089) malware during cyber attacks against Ukraine in 2015. [KillDisk](https://attack.mitre.org/software/S0607) has since evolved into stand-alone malware used by a variety of threat actors against additional targets in Europe and Latin America; in 2016 a ransomware component was also incorporated into some [KillDisk](https://attack.mitre.org/software/S0607) variants.(Citation: KillDisk Ransomware)(Citation: ESEST Black Energy Jan 2016)(Citation: Trend Micro KillDisk 1)(Citation: Trend Micro KillDisk 2) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--peachpit | PEACHPIT | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--volgmer | VOLGMER | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--net | Net | The [Net](https://attack.mitre.org/software/S0039) utility is a component of the Windows operating system. It is used in command-line operations for control of users, groups, services, and network connections. (Citation: Microsoft Net Utility)<br><br>[Net](https://attack.mitre.org/software/S0039) has a great deal of functionality, (Citation: Savill 1999) much of which is useful for an adversary, such as gathering system and network information for Discovery, moving laterally through [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) using <code>net use</code> commands, and interacting with services. The net1.exe utility is executed for certain functionality when net.exe is run and can be used directly in commands such as <code>net1 user</code>. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| Amazon、オープンソースのサプライチェーン攻撃を行う北朝鮮ハッカー集団を特定 | infrastructure-operation | 不明 | 不明 | 2026-07-31 |  | malware--daily-f30dd669ecd1c3776828 |  |  | Amazonは、typo-crypto、debug、chalk、axiosのNPMパッケージ侵害を、同一の北朝鮮関連攻撃グループによる活動と中程度の確度で評価した。 攻撃者は信頼されたメンテナーをソーシャルエンジニアリングで侵害し、悪意ある更新を公開して依存する多数の環境へ侵入した。 typo-cryptoでは、特定のハッシュ入力を受けるとC2から第2段階ペイロードを取得し、Windows、macOS、Linux上で実行するコードが確認された。 攻撃手法は、複数パッケージへの機能分割、長期間の信頼構築、外部リソースによる後付けの悪性化、暗号化や解析環境回避へ高度化している。 生成AIは自然なコードや偽の開発者情報の生成、存在しない依存関係を悪用するslopsquatting、AIコード審査への間接プロンプトインジェクションに利用され得る。 | 中 | `source--daily-a7e2c22924a222a6eb0f` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| Amazon、オープンソースのサプライチェーン攻撃を行う北朝鮮ハッカー集団を特定 | APT38 | typo-crypto | 情報なし | 情報なし | 情報なし | 情報なし | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | インド | 構造化OSINTの被害国フィールドでAPT38の標的・被害国としてインドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-360net`, `source--target-audit-misp-threat-actor` |
| countries | オーストラリア | 構造化OSINTの被害国フィールドでAPT38の標的・被害国としてオーストラリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | カナダ | 構造化OSINTの被害国フィールドでAPT38の標的・被害国としてカナダが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | グアテマラ | 構造化OSINTの被害国フィールドでAPT38の標的・被害国としてグアテマラが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | タイ | 構造化OSINTの被害国フィールドでAPT38の標的・被害国としてタイが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ドイツ | 構造化OSINTの被害国フィールドでAPT38の標的・被害国としてドイツが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | バングラデシュ | 構造化OSINTの被害国フィールドでAPT38の標的・被害国としてバングラデシュが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | フランス | 構造化OSINTの被害国フィールドでAPT38の標的・被害国としてフランスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | ブラジル | 構造化OSINTの被害国フィールドでAPT38の標的・被害国としてブラジルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | 中国 | 構造化OSINTの被害国フィールドでAPT38の標的・被害国として中国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-360net`, `source--target-audit-misp-threat-actor` |
| countries | 日本 | 構造化OSINTの被害国フィールドでAPT38の標的・被害国として日本が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | 米国 | レビュー済みアクターマッピングの標的欄に記録された米国を構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-misp-360net`, `source--target-audit-misp-threat-actor` |
| countries | 英国 | 構造化OSINTの被害国フィールドでAPT38の標的・被害国として英国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| countries | 韓国 | 構造化OSINTの被害国フィールドでAPT38の標的・被害国として韓国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-360net`, `source--target-audit-misp-threat-actor` |
| countries | 香港 | 構造化OSINTの被害国フィールドでAPT38の標的・被害国として香港が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| regions | 中南米 | グアテマラ、ブラジルで確認された標的・被害事例を中南米として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| regions | 全世界 | MITRE ATT&CKのGroup概要でAPT38の標的範囲として全世界が明示されている。 | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| regions | 北米 | カナダ、米国で確認された標的・被害事例を北米として集約した地域表示。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-misp-360net`, `source--target-audit-misp-threat-actor` |
| regions | 南アジア | インド、バングラデシュで確認された標的・被害事例を南アジアとして集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-misp-360net`, `source--target-audit-misp-threat-actor` |
| regions | 東アジア | レビュー済みアクターマッピングの標的欄に記録された東アジアを構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--target-audit-misp-360net`, `source--target-audit-misp-threat-actor` |
| regions | 欧州 | ドイツ、フランス、英国で確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-misp-threat-actor` |
| sectors | 暗号資産・Web3 | ial cyber operations; it has been attributed to the Reconnaissance General Bureau.(Citation: CISA AA20-239A BeagleBoyz August 2020) Active since at least 2014, [APT38](https://attack.mitre.org/groups/G0082) has targeted banks, financial institutions, casinos, cryptocurrency exchanges, SWIFT system endpoints, and ATMs in at least 38 countries worldwide. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 金融 | [APT38](https://attack.mitre.org/groups/G0082) is a North Korean state-sponsored threat group that specializes in financial cyber operations; it has been attributed to the Reconnaissance General Bureau.(Citation: CISA AA20-239A BeagleBoyz August 2020) Active since at least 2014, [APT38](https://attack.mitre.org/groups/G0082) has targeted banks, financial institutions, casinos, cryptocurrency exchanges, SWIFT system endpoints, and ATMs in at least 38 countries worldwide. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | Defense | Targeting text indicates the Defense sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Collection | T1005 | Data from Local System | [APT38](https://attack.mitre.org/groups/G0082) has collected data from a compromised host.(Citation: CISA AA20-239A BeagleBoyz August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.002 | Software Packing | [APT38](https://attack.mitre.org/groups/G0082) has used several code packing methods such as Themida, Enigma, VMProtect, and Obsidium, to pack their implants.(Citation: FireEye APT38 Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1033 | System Owner/User Discovery | [APT38](https://attack.mitre.org/groups/G0082) has identified primary users, currently logged in users, sets of users that commonly use a system, or inactive users.(Citation: CISA AA20-239A BeagleBoyz August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.003 | Rename Legitimate Utilities | [APT38](https://attack.mitre.org/groups/G0082) has renamed system utilities, such as `rundll32.exe` and `mshta.exe`, to avoid detection.(Citation: 1 - appv)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.006 | Space after Filename | [APT38](https://attack.mitre.org/groups/G0082) has put several spaces before a file extension to avoid detection and suspicion.(Citation: 1 - appv)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | [APT38](https://attack.mitre.org/groups/G0082) installed a port monitoring tool, MAPMAKER, to print the active TCP connections on the local system.(Citation: FireEye APT38 Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.003 | Cron | [APT38](https://attack.mitre.org/groups/G0082) has used cron to create pre-scheduled and periodic background jobs on a Linux system.(Citation: CISA AA20-239A BeagleBoyz August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [APT38](https://attack.mitre.org/groups/G0082) has used Task Scheduler to run programs at system startup or on a scheduled basis for persistence.(Citation: CISA AA20-239A BeagleBoyz August 2020) Additionally, [APT38](https://attack.mitre.org/groups/G0082) has used living-off-the-land scripts to execute a malicious script via a scheduled task.(Citation: 1 - appv)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055 | Process Injection | [APT38](https://attack.mitre.org/groups/G0082) has injected malicious payloads into the `explorer.exe` process.(Citation: 1 - appv)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056.001 | Keylogging | [APT38](https://attack.mitre.org/groups/G0082) used a Trojan called KEYLIME to capture keystrokes from the victim’s machine.(Citation: FireEye APT38 Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | [APT38](https://attack.mitre.org/groups/G0082) leveraged Sysmon to understand the processes, services in the organization.(Citation: FireEye APT38 Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [APT38](https://attack.mitre.org/groups/G0082) has used PowerShell to execute commands and other operational tasks.(Citation: CISA AA20-239A BeagleBoyz August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [APT38](https://attack.mitre.org/groups/G0082) has used a command-line tunneler, NACHOCHEESE, to give them shell access to a victim’s machine.(Citation: FireEye APT38 Oct 2018) Additionally, [APT38](https://attack.mitre.org/groups/G0082) has used batch scripts.(Citation: 1 - appv)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.005 | Visual Basic | [APT38](https://attack.mitre.org/groups/G0082) has used VBScript to execute commands and other operational tasks.(Citation: CISA AA20-239A BeagleBoyz August 2020)(Citation: 1 - appv) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | [APT38](https://attack.mitre.org/groups/G0082) has used a utility called CLOSESHAVE that can securely delete a file from the system. They have also removed malware, tools, or other non-native files used during the intrusion to reduce their footprint or as part of the post-intrusion cleanup process.(Citation: FireEye APT38 Oct 2018)(Citation: CISA AA20-239A BeagleBoyz August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.006 | Timestomp | [APT38](https://attack.mitre.org/groups/G0082) has modified data timestamps to mimic files that are in the same folder on a compromised host.(Citation: CISA AA20-239A BeagleBoyz August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071.001 | Web Protocols | [APT38](https://attack.mitre.org/groups/G0082) used a backdoor, QUICKRIDE, to communicate to the C2 server over HTTP and HTTPS.(Citation: FireEye APT38 Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1082 | System Information Discovery | [APT38](https://attack.mitre.org/groups/G0082) has attempted to get detailed information about a compromised host, including the operating system, version, patches, hotfixes, and service packs.(Citation: CISA AA20-239A BeagleBoyz August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | [APT38](https://attack.mitre.org/groups/G0082) have enumerated files and directories, or searched in specific locations within a compromised host.(Citation: CISA AA20-239A BeagleBoyz August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [APT38](https://attack.mitre.org/groups/G0082) used a backdoor, NESTEGG, that has the capability to download and upload files to and from a victim’s machine.(Citation: FireEye APT38 Oct 2018) Additionally, [APT38](https://attack.mitre.org/groups/G0082) has downloaded other payloads onto a victim’s machine.(Citation: 1 - appv)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1106 | Native API | [APT38](https://attack.mitre.org/groups/G0082) has used the Windows API to execute code within a victim's system.(Citation: CISA AA20-239A BeagleBoyz August 2020)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110 | Brute Force | [APT38](https://attack.mitre.org/groups/G0082) has used brute force techniques to attempt account access when passwords are unknown or when password hashes are unavailable.(Citation: CISA AA20-239A BeagleBoyz August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment, Persistence | T1112 | Modify Registry | [APT38](https://attack.mitre.org/groups/G0082) uses a tool called CLEANTOAD that has the capability to modify Registry keys.(Citation: FireEye APT38 Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1115 | Clipboard Data | [APT38](https://attack.mitre.org/groups/G0082) used a Trojan called KEYLIME to collect data from the clipboard.(Citation: FireEye APT38 Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1135 | Network Share Discovery | [APT38](https://attack.mitre.org/groups/G0082) has enumerated network shares on a compromised host.(Citation: CISA AA20-239A BeagleBoyz August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | [APT38](https://attack.mitre.org/groups/G0082) has used the RC4 algorithm to decrypt configuration data. (Citation: 1 - appv)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1189 | Drive-by Compromise | [APT38](https://attack.mitre.org/groups/G0082) has conducted watering holes schemes to gain initial access to victims.(Citation: FireEye APT38 Oct 2018)(Citation: CISA AA20-239A BeagleBoyz August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.001 | Malicious Link | [APT38](https://attack.mitre.org/groups/G0082) has used links to execute a malicious Visual Basic script.(Citation: 1 - appv)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1204.002 | Malicious File | [APT38](https://attack.mitre.org/groups/G0082)  has attempted to lure victims into enabling malicious macros within email attachments.(Citation: CISA AA20-239A BeagleBoyz August 2020) Additionally, [APT38](https://attack.mitre.org/groups/G0082) has used malicious Word documents and shortcut files.(Citation: 1 - appv)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1217 | Browser Information Discovery | [APT38](https://attack.mitre.org/groups/G0082) has collected browser bookmark information to learn more about compromised hosts, obtain personal information about users, and acquire details about internal network resources.(Citation: CISA AA20-239A BeagleBoyz August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.001 | Compiled HTML File | [APT38](https://attack.mitre.org/groups/G0082) has used CHM files to move concealed payloads.(Citation: Kaspersky Lazarus Under The Hood APR 2017) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.005 | Mshta | [APT38](https://attack.mitre.org/groups/G0082) has used a renamed version of `mshta.exe` to execute malicious HTML files.(Citation: 1 - appv)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.007 | Msiexec | [APT38](https://attack.mitre.org/groups/G0082) has used `msiexec.exe` to execute malicious files.(Citation: 1 - appv)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.011 | Rundll32 | [APT38](https://attack.mitre.org/groups/G0082) has used rundll32.exe to execute binaries, scripts, and Control Panel Item files and to execute code via proxy to avoid triggering security tools.(Citation: CISA AA20-239A BeagleBoyz August 2020)(Citation: 1 - appv) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1480.002 | Mutual Exclusion | [APT38](https://attack.mitre.org/groups/G0082) has created a mutex to avoid duplicate execution.(Citation: 1 - appv)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1485 | Data Destruction | [APT38](https://attack.mitre.org/groups/G0082) has used a custom secure delete function to make deleted files unrecoverable.(Citation: FireEye APT38 Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1486 | Data Encrypted for Impact | [APT38](https://attack.mitre.org/groups/G0082) has used Hermes ransomware to encrypt files with AES256.(Citation: FireEye APT38 Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | [APT38](https://attack.mitre.org/groups/G0082) has used web shells for persistence or to ensure redundant access.(Citation: CISA AA20-239A BeagleBoyz August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1518.001 | Security Software Discovery | [APT38](https://attack.mitre.org/groups/G0082) has identified security software, configurations, defensive tools, and sensors installed on a compromised system.(Citation: CISA AA20-239A BeagleBoyz August 2020)(Citation: 1 - appv) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1529 | System Shutdown/Reboot | [APT38](https://attack.mitre.org/groups/G0082) has used a custom MBR wiper named BOOTWRECK, which will initiate a system reboot after wiping the victim's MBR.(Citation: FireEye APT38 Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1543.003 | Windows Service | [APT38](https://attack.mitre.org/groups/G0082) has installed a new Windows service to establish persistence.(Citation: CISA AA20-239A BeagleBoyz August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1548.002 | Bypass User Account Control | [APT38](https://attack.mitre.org/groups/G0082) has used the legitimate application `ieinstal.exe` to bypass UAC.(Citation: 1 - appv)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1553.005 | Mark-of-the-Web Bypass | [APT38](https://attack.mitre.org/groups/G0082) has used ISO and VHD files to deploy malware and to bypass Mark-of-the-Web (MOTW) security measures.(Citation: 1 - appv)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1561.002 | Disk Structure Wipe | [APT38](https://attack.mitre.org/groups/G0082) has used a custom MBR wiper named BOOTWRECK to render systems inoperable.(Citation: FireEye APT38 Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1565.001 | Stored Data Manipulation | [APT38](https://attack.mitre.org/groups/G0082) has used DYEPACK to create, delete, and alter records in databases used for SWIFT transactions.(Citation: FireEye APT38 Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1565.002 | Transmitted Data Manipulation | [APT38](https://attack.mitre.org/groups/G0082) has used DYEPACK to manipulate SWIFT messages en route to a printer.(Citation: FireEye APT38 Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Impact | T1565.003 | Runtime Data Manipulation | [APT38](https://attack.mitre.org/groups/G0082) has used DYEPACK.FOX to manipulate PDF data as it is accessed to remove traces of fraudulent SWIFT transactions from the data displayed to the end user.(Citation: FireEye APT38 Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1566.001 | Spearphishing Attachment | [APT38](https://attack.mitre.org/groups/G0082) has conducted spearphishing campaigns using malicious email attachments.(Citation: CISA AA20-239A BeagleBoyz August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1569.002 | Service Execution | [APT38](https://attack.mitre.org/groups/G0082) has created new services or modified existing ones to run executables, commands, or scripts.(Citation: CISA AA20-239A BeagleBoyz August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.001 | Domains | [APT38](https://attack.mitre.org/groups/G0082) has created fake domains to imitate legitimate venture capital or bank domains.(Citation: 1 - appv)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [APT38](https://attack.mitre.org/groups/G0082) has obtained and used open-source tools such as [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: ESET Lazarus KillDisk April 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | [APT38](https://attack.mitre.org/groups/G0082) has unhooked DLLs to disable endpoint detection and response (EDR) or anti-virus (AV) tools.(Citation: 1 - appv)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685.005 | Clear Windows Event Logs | [APT38](https://attack.mitre.org/groups/G0082) clears Window Event logs and Sysmon logs from the system.(Citation: FireEye APT38 Oct 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1686 | Disable or Modify System Firewall | [APT38](https://attack.mitre.org/groups/G0082) have created firewall exemptions on specific ports, including ports 443, 6443, 8443, and 9443.(Citation: CISA AA20-239A BeagleBoyz August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1686.002 | Network Device Firewall | [APT38](https://attack.mitre.org/groups/G0082) have created firewall exemptions on specific ports, including ports 443, 6443, 8443, and 9443. (Citation: CISA AA20-239A BeagleBoyz August 2020)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1690 | Prevent Command History Logging | [APT38](https://attack.mitre.org/groups/G0082) has prepended a space to all of their terminal commands to operate without leaving traces in the HISTCONTROL environment.(Citation: CISA AA20-239A BeagleBoyz August 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 18件
- IOC観測: 22件
- 複数攻撃で観測: 0件
- 要レビュー候補: 14件
- 非IOC artifact観測: 148件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| Government sources connect Bluenoroff/APT38 and Lazarus under the RGB and a common conspiracy, while industry reporting preserves APT38 as a financially focused cluster. | 高 | `source--treasury-dprk-groups-2019`, `source--doj-dprk-conspiracy-2021` | verification_status=partially-supported; APT38, Bluenoroff, and Lazarus have vendor-dependent scopes; exact equivalence should not be asserted. The DOJ's common-conspiracy framing is organizational/legal and does not prove identical operational clustering. |

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--apt38--10c7f8863a1297b9 | Secureworks NC3 2022StateoftheThreat |  | 2022 | summary/2023/Secureworks_NC3_2022StateoftheThreat.pdf | report | TLP:CLEAR | 中 |
| source--apt38--131cb847887ec4c7 | [Report] Bitsight State of the Underground 2026 |  | 2026 | summary/2026/[Report] Bitsight State of the Underground 2026.pdf | report | TLP:CLEAR | 中 |
| source--apt38--1a90d368468861d6 | README |  | 不明 | lazarus/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--apt38--1f3c1f0eb49c4e13 | Microsoft Digital Defense Report 2022 |  | 2022 | summary/2022/Microsoft Digital Defense Report 2022.pdf | report | TLP:CLEAR | 中 |
| source--apt38--241e1ed62d69493a | The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities |  | 不明 | International Strategic/Korea/The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities.pdf | report | TLP:CLEAR | 中 |
| source--apt38--2d795fb8c565e03e | 360 APT Annual Research Report 2022 |  | 2022 | summary/2023/360_APT_Annual_Research_Report_2022.pdf | report | TLP:CLEAR | 中 |
| source--apt38--2f6ecd70b84c34a8 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--apt38--329643e7ed4efd13 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--apt38--36507790ef9f1a89 | 2022 year in retrospect report |  | 2022 | summary/2023/2022-year-in-retrospect-report.pdf | report | TLP:CLEAR | 中 |
| source--apt38--3e70a5b10ab68475 | rpt mtrends 2021 fireeye |  | 2021 | summary/2021/rpt-mtrends-2021-fireeye.pdf | report | TLP:CLEAR | 中 |
| source--apt38--44e73e38915723b6 | Cybersecurity Threats 2024 Mid Year Report |  | 2024 | summary/2024/Cybersecurity Threats 2024 Mid-Year Report.pdf | report | TLP:CLEAR | 中 |
| source--apt38--482c8b9909ecf926 | Global APT 2023 Mid Year Report QIANXIN |  | 2023 | summary/2023/Global APT 2023 Mid-Year Report-QIANXIN.pdf | report | TLP:CLEAR | 中 |
| source--apt38--50e0d17aebf86ad9 | Cybersecurity Threats 2024 Annual Report QAX |  | 2024 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | report | TLP:CLEAR | 中 |
| source--apt38--5312c7555374eaf2 | Microsoft Digital Defense Report 2024 |  | 2024 | summary/2024/Microsoft Digital Defense Report 2024.pdf | report | TLP:CLEAR | 中 |
| source--apt38--53d39dedbb8502ab | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | International Strategic/Korea/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--apt38--5715dee99bf684fd | DTEX Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce |  | 不明 | CyberMerceNary/ITWorker/DTEX-Exposing+DPRK+Cyber+Syndicate+and+Hidden+IT+Workforce.pdf | report | TLP:CLEAR | 中 |
| source--apt38--579d11dfe0ae4238 | apt38 |  | 不明 | actor_profile/evidence/apt38.csv | structured-data | TLP:CLEAR | 中 |
| source--apt38--5f640852eff44ad7 | The CrowdStrike 2021 Global Threat Report |  | 2021 | summary/2021/The CrowdStrike 2021 Global Threat Report.pdf | report | TLP:CLEAR | 中 |
| source--apt38--63cd13ed4cefa69d | MacMalware 2023 |  | 2023 | summary/2024/MacMalware_2023.pdf | report | TLP:CLEAR | 中 |
| source--apt38--7fd482a6ac8d3f55 | CryptoCore Lazarus Clearsky |  | 不明 | lazarus/CryptoCore-Lazarus-Clearsky.pdf | report | TLP:CLEAR | 中 |
| source--apt38--80fa0a2750b497b7 | Global APT 2022 Annual Report qianxin |  | 2022 | summary/2023/Global APT 2022 Annual Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--apt38--81945794ed3781bf | Recordedfuture 2023 Annual Report ta 2024 0321 |  | 2023 | summary/2024/Recordedfuture 2023 Annual Report ta-2024-0321.pdf | report | TLP:CLEAR | 中 |
| source--apt38--8b396a1f8f9232e2 | Threat Hunting with VirusTotal |  | 不明 | APT-hunting/Threat Hunting with VirusTotal.pdf | report | TLP:CLEAR | 中 |
| source--apt38--8c50143c640cbc8a | 2025 Cyber Security Report Final |  | 2025 | summary/2025/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--apt38--8ec0ecccad50b690 | The Lazarus Constellation |  | 不明 | lazarus/The_Lazarus_Constellation.pdf | report | TLP:CLEAR | 中 |
| source--apt38--98edf8a69714332e | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--apt38--9d1e25591670c1ec | M Trends 2023 Report MANDIANT SPECIAL REPORT |  | 2023 | summary/2023/M-Trends 2023 Report MANDIANT SPECIAL REPORT.pdf | report | TLP:CLEAR | 中 |
| source--apt38--a1d16d34983b49f2 | 2022cyberComprehensiveSituationObservationManual |  | 2022 | summary/2023/2022cyberComprehensiveSituationObservationManual.pdf | report | TLP:CLEAR | 中 |
| source--apt38--a2aeec7d62eed864 | CrowdStrike 2026 Global Threat Report |  | 2026 | summary/2026/CrowdStrike-2026-Global-Threat-Report.pdf | report | TLP:CLEAR | 中 |
| source--apt38--ab912926e1db0f93 | Dream Job Campaign |  | 不明 | lazarus/Dream-Job-Campaign.pdf | report | TLP:CLEAR | 中 |
| source--apt38--abb4e7a3abb0df2e | US Army report on North Korean military |  | 不明 | International Strategic/Korea/US-Army-report-on-North-Korean-military.pdf | report | TLP:CLEAR | 中 |
| source--apt38--ac5857b429eb9fae | APT43 Report |  | 不明 | APT43/APT43 Report.pdf | report | TLP:CLEAR | 中 |
| source--apt38--b01813ad282937d2 | 2025 Cyber Security Report Final |  | 2025 | summary/2026/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--apt38--b22f71c52e45c313 | WithSecure Lazarus No Pineapple Threat Intelligence Report 2023 |  | 2023 | lazarus/WithSecure-Lazarus-No-Pineapple-Threat-Intelligence-Report-2023.pdf | report | TLP:CLEAR | 中 |
| source--apt38--b5f4049ef39ac59a | README |  | 不明 | summary/2023/README.MD | repository-notes | TLP:CLEAR | 中 |
| source--apt38--baf5e7425ad06679 | Cloudflare 2026 threat report |  | 2026 | summary/2026/Cloudflare-2026-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--apt38--c48f3b9eefe4e599 | APT group activities under the shadow of the epidemic(2020) |  | 2020 | summary/2021/APT group activities under the shadow of the epidemic(2020).pdf | report | TLP:CLEAR | 中 |
| source--apt38--c8152777606f552b | readme |  | 不明 | summary/2026/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--apt38--c8e994207a21c4f2 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--apt38--d016ac2267587e6b | Global APT Mid 2022 Report qianxin |  | 2022 | summary/2022/Global APT Mid-2022 Report-qianxin.pdf | report | TLP:CLEAR | 中 |
| source--apt38--d8f348da3d009aaa | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--apt38--da7029581b779c62 | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--apt38--dcaff719d29e70be | cybercrime multifaceted national security threat |  | 不明 | summary/2025/cybercrime-multifaceted-national-security-threat.pdf | report | TLP:CLEAR | 中 |
| source--apt38--df7ff2e2140af116 | 2025 CrowdStrike European Threat Landscape Report |  | 2025 | summary/2025/2025-CrowdStrike-European-Threat-Landscape-Report_.pdf | report | TLP:CLEAR | 中 |
| source--apt38--e08f3a9e3b41c4c2 | Qianxin 2023 APT Report |  | 2023 | summary/2024/Qianxin 2023 APT Report.pdf | report | TLP:CLEAR | 中 |
| source--apt38--e42a45b52776f627 | Virtual Routes Pharos Report Series No. 3 |  | 不明 | cybercrime/2025/Virtual-Routes-Pharos-Report-Series-No.-3.pdf | report | TLP:CLEAR | 中 |
| source--apt38--e9e44d11654ffedb | Automating APT Campaign and Group Attribution |  | 不明 | APT-hunting/Automating APT Campaign and Group Attribution.pdf | report | TLP:CLEAR | 中 |
| source--apt38--ea65e855cff8bdeb | eset apt activity report q4 2025 q1 2026 |  | 2025 | summary/2026/eset-apt-activity-report-q4-2025-q1-2026.pdf | report | TLP:CLEAR | 中 |
| source--apt38--ee91d582d1fad020 | North Korea’s Cyber Strategy |  | 不明 | International Strategic/Korea/North Korea’s Cyber Strategy.pdf | report | TLP:CLEAR | 中 |
| source--apt38--f046b89cc1453339 | 2022 APT TRENDS INSIGHT REPORT |  | 2022 | summary/2023/2022_APT_TRENDS_INSIGHT_REPORT.pdf | report | TLP:CLEAR | 中 |
| source--apt38--f4b0f1caa4b664f7 | MDDR FINAL 2023 1004 |  | 2023-10-04 | summary/2023/MDDR_FINAL_2023_1004.pdf | report | TLP:CLEAR | 中 |
| source--apt38--f55795b108df62ba | 2025 Blockchain Security and AML Annual Report |  | 2025 | summary/2025/2025-Blockchain-Security-and-AML-Annual-Report.pdf | report | TLP:CLEAR | 中 |
| source--apt38--f82a58381fcab3cb | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--apt38--fc581fa134eaf2de | readme |  | 不明 | summary/2024/readme.md | repository-notes | TLP:CLEAR | 中 |
| source--daily-a7e2c22924a222a6eb0f | Amazon、オープンソースのサプライチェーン攻撃を行う北朝鮮ハッカー集団を特定 | aws.amazon.com | 2026-07-31 | https://aws.amazon.com/jp/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/ | osint-report | TLP:CLEAR | 中 |
| source--doj-dprk-conspiracy-2021 | Three North Korean Military Hackers Indicted in Wide-Ranging Scheme | U.S. Department of Justice | 2021-02-17 | https://www.justice.gov/archives/opa/pr/three-north-korean-military-hackers-indicted-wide-ranging-scheme-commit-cyberattacks-and | government-legal-announcement | TLP:CLEAR | 高 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-360net | MISP Galaxy 360.net Threat Actors | MISP Project / 360 Netlab | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-misp-360net | MISP 360.net suspected-victim fields | MISP Project / 360.net | 不明 | actor_profile/reference/osint/misp-360net.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-misp-threat-actor | MISP Galaxy Threat Actor victim geography fields | MISP Project / Council on Foreign Relations | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--treasury-dprk-groups-2019 | Treasury Sanctions North Korean State-Sponsored Malicious Cyber Groups | U.S. Department of the Treasury | 2019-09-13 | https://home.treasury.gov/news/press-releases/sm774 | government-designation | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
