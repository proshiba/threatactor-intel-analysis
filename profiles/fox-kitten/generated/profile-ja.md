# Fox Kitten 脅威アクタープロファイル

- プロファイルID: `actor--fox-kitten`
- 状態: draft
- 更新日時: 2026-07-29T23:13:54Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Fox Kittenの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Fox Kitten**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Lemon Sandstorm | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Parisite | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Pay2key | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Pioneer Kitten | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| PioneerKitten. | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| RUBIDIUM | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| UNC757 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

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
| Adversary | [Fox Kitten](https://attack.mitre.org/groups/G0117) is threat actor with a suspected nexus to the Iranian government that has been active since at least 2017 against entities in the Middle East, North Africa, Europe, Australia, and North America. [Fox Kitten](https://attack.mitre.org/groups/G0117) has targeted multiple industrial verticals including oil and gas, technology, government, defense, healthcare, manufacturing, and engineering.(Citation: ClearkSky Fox Kitten February 2020)(Citation: CrowdStrike PIONEER KITTEN August 2020)(Citation: Dragos PARISITE )(Citation: ClearSky Pay2Kitten December 2020) |
| Capability | SystemBC, China Chopper, Pay2Key, SSHNET, Juicy Potato, Port, STSRCHECK, LPManager, Invoke-SMBClient, Invoke-SMBEnum, Invoke-SMBExec, Invoke-TheHash, Invoke-WMIExec, SOCKET-Based Backdoor, Pay2Key ransomware, FRPC, ngrok, PsExec |
| Infrastructure |  |
| Victim | IT, Telecommunication, Oil and Gas, Aviation, Government, and Security sectors around the world. |
| Socio-political | Iran |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | Parisite, Fox Kitten, Pioneer Kitten | canonical-name | 高 | Iran | https://dragos.com/blog/industry-news/the-state-of-threats-to-electric-entities-in-north-america/<br>https://threatpost.com/oil-and-gas-specialist-apt-pivots-to-u-s-power-plants/151699/<br>https://www.clearskysec.com/wp-content/uploads/2020/02/ClearSky-Fox-Kitten-Campaign-v1.pdf |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Lemon Sandstorm | multiple-name-intersection | 高 | Iran | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Fox Kitten | canonical-name | 高 | IR | https://youtu.be/pBDu8EGWRC4?t=2492<br>https://www.dragos.com/threat/parisite<br>https://www.dragos.com/wp-content/uploads/The-ICS-Threat-Landscape.pdf |
| misp-microsoft-activity-group | Lemon Sandstorm | canonical-name | 高 | IR, Iran | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Fox Kitten - G0117 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0117<br>https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://us-cert.cisa.gov/ncas/alerts/aa20-259a |
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
| malware--systembc | SystemBC | [SystemBC](https://attack.mitre.org/software/S9001) is a malware family offered as a malware-as-a-service (MaaS) that is used to establish command and control and facilitate follow-on activity, including ransomware deployment.[SystemBC](https://attack.mitre.org/software/S9001) executes a variety of tasks including setting up SOCKS5 proxies, maintaining persistence, ingesting malicious files, and handing C2 communication. [SystemBC](https://attack.mitre.org/software/S9001) was first detected in 2018, and has been used by [Wizard Spider](https://attack.mitre.org/groups/G0102) since at least 2020, and by [FIN7](https://attack.mitre.org/groups/G0046) since at least 2022.(Citation: TrumanKroll_SYSTEMBCServer_Jan2024)(Citation: SophosGnGal_SystemBC_Dec2020)(Citation: BlackBasta)(Citation: AhnLab_SystemBC_Apr2022)(Citation: Lumen_SystemBC_Sept2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--china-chopper | China Chopper | [China Chopper](https://attack.mitre.org/software/S0020) is a [Web Shell](https://attack.mitre.org/techniques/T1505/003) hosted on Web servers to provide access back into an enterprise network that does not rely on an infected system calling back to a remote command and control server.(Citation: Lee 2013) It has been used by several threat groups.(Citation: Dell TG-3390)(Citation: FireEye Periscope March 2018)(Citation: CISA AA21-200A APT40 July 2021)(Citation: Rapid7 HAFNIUM Mar 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--pay2key | Pay2Key | [Pay2Key](https://attack.mitre.org/software/S0556) is a ransomware written in C++ that has been used by [Fox Kitten](https://attack.mitre.org/groups/G0117) since at least July 2020 including campaigns against Israeli companies. [Pay2Key](https://attack.mitre.org/software/S0556) has been incorporated with a leak site to display stolen sensitive information to further pressure victims into payment.(Citation: ClearkSky Fox Kitten February 2020)(Citation: Check Point Pay2Key November 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--sshnet | SSHNET | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--juicy-potato | Juicy Potato | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--port | Port | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--stsrcheck | STSRCHECK | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--lpmanager | LPManager | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--invoke-smbclient | Invoke-SMBClient | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--invoke-smbenum | Invoke-SMBEnum | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--invoke-smbexec | Invoke-SMBExec | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--invoke-thehash | Invoke-TheHash | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--invoke-wmiexec | Invoke-WMIExec | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--socket-based-backdoor | SOCKET-Based Backdoor | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--pay2key-ransomware | Pay2Key ransomware | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| malware--frpc | FRPC | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--ngrok | ngrok | [ngrok](https://attack.mitre.org/software/S0508) is a legitimate reverse proxy tool that can create a secure tunnel to servers located behind firewalls or on local machines that do not have a public IP. [ngrok](https://attack.mitre.org/software/S0508) has been leveraged by threat actors in several campaigns including use for lateral movement and data exfiltration.(Citation: Zdnet Ngrok September 2018)(Citation: FireEye Maze May 2020)(Citation: Cyware Ngrok May 2019)(Citation: MalwareBytes LazyScripter Feb 2021) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
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
| Pay2Key | operation | 不明 | 不明 | 不明 |  |  |  |  | Operation name listed in the repository actor-mapping workbook. | 中 | `source--actor-mapping-workbook` |

Pay2Key

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | アラブ首長国連邦 | 構造化OSINTの被害国フィールドでFox Kittenの標的・被害国としてアラブ首長国連邦が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イスラエル | 構造化OSINTの被害国フィールドでFox Kittenの標的・被害国としてイスラエルが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | イタリア | 構造化OSINTの被害国フィールドでFox Kittenの標的・被害国としてイタリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オーストラリア | 構造化OSINTの被害国フィールドでFox Kittenの標的・被害国としてオーストラリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | オーストリア | 構造化OSINTの被害国フィールドでFox Kittenの標的・被害国としてオーストリアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | クウェート | 構造化OSINTの被害国フィールドでFox Kittenの標的・被害国としてクウェートが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | サウジアラビア | 構造化OSINTの被害国フィールドでFox Kittenの標的・被害国としてサウジアラビアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ドイツ | 構造化OSINTの被害国フィールドでFox Kittenの標的・被害国としてドイツが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ハンガリー | 構造化OSINTの被害国フィールドでFox Kittenの標的・被害国としてハンガリーが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フィンランド | 構造化OSINTの被害国フィールドでFox Kittenの標的・被害国としてフィンランドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | フランス | 構造化OSINTの被害国フィールドでFox Kittenの標的・被害国としてフランスが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | ポーランド | 構造化OSINTの被害国フィールドでFox Kittenの標的・被害国としてポーランドが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | マレーシア | 構造化OSINTの被害国フィールドでFox Kittenの標的・被害国としてマレーシアが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | レバノン | 構造化OSINTの被害国フィールドでFox Kittenの標的・被害国としてレバノンが記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| countries | 米国 | 構造化OSINTの被害国フィールドでFox Kittenの標的・被害国として米国が記録されている。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 中東 | アラブ首長国連邦、イスラエル、クウェート、サウジアラビア、レバノンで確認された標的・被害事例を中東として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 全世界 | レビュー済みアクターマッピングの標的欄に記録された全世界を構造化した。 | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| regions | 東欧 | ハンガリー、ポーランドで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| regions | 欧州 | イタリア、オーストリア、ドイツ、ハンガリー、フィンランド、フランス、ポーランドで確認された標的・被害事例を欧州として集約した地域表示。 | 不明 | 不明 | 中 | `source--target-audit-etda-threat-group-cards` |
| sectors | 製造・産業 | [Fox Kitten](https://attack.mitre.org/groups/G0117) has targeted multiple industrial verticals including oil and gas, technology, government, defense, healthcare, manufacturing, and engineering.(Citation: ClearkSky Fox Kitten February 2020)(Citation: CrowdStrike PIONEER KITTEN August 2020)(Citation: Dragos PARISITE )(Citation: ClearSky Pay2Ki | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 防衛・軍事 | [Fox Kitten](https://attack.mitre.org/groups/G0117) has targeted multiple industrial verticals including oil and gas, technology, government, defense, healthcare, manufacturing, and engineering.(Citation: ClearkSky Fox Kitten February 2020)(Citation: CrowdStrike PIONEER KITTEN August 2020)(Citation: Dragos PARISITE )(Citation: ClearSky Pay2Kitten December 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 医療・ヘルスケア | [Fox Kitten](https://attack.mitre.org/groups/G0117) has targeted multiple industrial verticals including oil and gas, technology, government, defense, healthcare, manufacturing, and engineering.(Citation: ClearkSky Fox Kitten February 2020)(Citation: CrowdStrike PIONEER KITTEN August 2020)(Citation: Dragos PARISITE )(Citation: ClearSky Pay2Kitten December 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | Energy | Targeting text indicates the Energy sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1` |
| sectors | Government | Targeting text indicates the Government sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook`, `source--mitre-attack-19-1` |
| sectors | Technology | Targeting text indicates the Technology sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Telecommunications | Targeting text indicates the Telecommunications sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |
| sectors | Transportation | Targeting text indicates the Transportation sector. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.001 | LSASS Memory | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used prodump to dump credentials from LSASS.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.003 | NTDS | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used Volume Shadow Copy to access credential information from NTDS.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1005 | Data from Local System | [Fox Kitten](https://attack.mitre.org/groups/G0117) has searched local system resources to access sensitive documents.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1012 | Query Registry | [Fox Kitten](https://attack.mitre.org/groups/G0117) has accessed Registry hives ntuser.dat and UserClass.dat.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1018 | Remote System Discovery | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used Angry IP Scanner to detect remote systems.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used RDP to log in and move laterally in the target environment.(Citation: CISA AA20-259A Iran-Based Actor September 2020)(Citation: ClearSky Pay2Kitten December 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used valid accounts to access SMB shares.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.004 | SSH | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used the PuTTY and Plink tools for lateral movement.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.005 | VNC | [Fox Kitten](https://attack.mitre.org/groups/G0117) has installed TightVNC server and client on compromised servers and endpoints for lateral movement.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.010 | Command Obfuscation | [Fox Kitten](https://attack.mitre.org/groups/G0117) has base64 encoded scripts to avoid detection.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | [Fox Kitten](https://attack.mitre.org/groups/G0117) has base64 encoded payloads to avoid detection.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.004 | Masquerade Task or Service | [Fox Kitten](https://attack.mitre.org/groups/G0117) has named the task for a reverse proxy lpupdate to appear legitimate.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [Fox Kitten](https://attack.mitre.org/groups/G0117) has named binaries and configuration files svhost and dllhost respectively to appear legitimate.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1039 | Data from Network Shared Drive | [Fox Kitten](https://attack.mitre.org/groups/G0117) has searched network shares to access sensitive documents.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1046 | Network Service Discovery | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used tools including NMAP to conduct broad scanning to identify open ports.(Citation: CISA AA20-259A Iran-Based Actor September 2020)(Citation: ClearSky Pay2Kitten December 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used Scheduled Tasks for persistence and to load and execute a reverse proxy binary.(Citation: CISA AA20-259A Iran-Based Actor September 2020)(Citation: ClearSky Pay2Kitten December 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059 | Command and Scripting Interpreter | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used a Perl reverse shell to communicate with C2.(Citation: ClearSky Pay2Kitten December 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used PowerShell scripts to access credential data.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used cmd.exe likely as a password changing mechanism.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used valid credentials with various services during lateral movement.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used WizTree to obtain network files and directory listings.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.001 | Local Account | [Fox Kitten](https://attack.mitre.org/groups/G0117) has accessed ntuser.dat and UserClass.dat on compromised hosts.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1087.002 | Domain Account | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used the Softerra LDAP browser to browse documentation on service accounts.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090 | Proxy | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used the open source reverse proxy tools including FRPC and Go Proxy to establish connections from C2 to local servers.(Citation: CISA AA20-259A Iran-Based Actor September 2020)(Citation: ClearSky Pay2Kitten December 2020)(Citation: Check Point Pay2Key November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1102 | Web Service | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used Amazon Web Services to host C2.(Citation: ClearSky Pay2Kitten December 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | [Fox Kitten](https://attack.mitre.org/groups/G0117) has downloaded additional tools including [PsExec](https://attack.mitre.org/software/S0029) directly to endpoints.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110 | Brute Force | [Fox Kitten](https://attack.mitre.org/groups/G0117) has brute forced RDP credentials.(Citation: ClearSky Pay2Kitten December 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1136.001 | Local Account | [Fox Kitten](https://attack.mitre.org/groups/G0117) has created a local user account with administrator privileges.(Citation: ClearSky Pay2Kitten December 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [Fox Kitten](https://attack.mitre.org/groups/G0117) has exploited known vulnerabilities in Fortinet, PulseSecure, and Palo Alto VPN appliances.(Citation: ClearkSky Fox Kitten February 2020)(Citation: Dragos PARISITE )(Citation: CrowdStrike PIONEER KITTEN August 2020)(Citation: CISA AA20-259A Iran-Based Actor September 2020)(Citation: ClearSky Pay2Kitten December 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1210 | Exploitation of Remote Services | [Fox Kitten](https://attack.mitre.org/groups/G0117) has exploited known vulnerabilities in remote services including RDP.(Citation: ClearkSky Fox Kitten February 2020)(Citation: CrowdStrike PIONEER KITTEN August 2020)(Citation: ClearSky Pay2Kitten December 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1213.005 | Messaging Applications | [Fox Kitten](https://attack.mitre.org/groups/G0117) has accessed victim security and IT environments and Microsoft Teams to mine valuable information.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1217 | Browser Information Discovery | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used Google Chrome bookmarks to identify internal resources and assets.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | [Fox Kitten](https://attack.mitre.org/groups/G0117) has installed web shells on compromised hosts to maintain access.(Citation: CISA AA20-259A Iran-Based Actor September 2020)(Citation: ClearSky Pay2Kitten December 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1530 | Data from Cloud Storage | [Fox Kitten](https://attack.mitre.org/groups/G0117) has obtained files from the victim's cloud storage instances.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1546.008 | Accessibility Features | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used sticky keys to launch a command prompt.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1552.001 | Credentials In Files | [Fox Kitten](https://attack.mitre.org/groups/G0117) has accessed files to gain valid credentials.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.005 | Password Managers | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used scripts to access credential information from the KeePass database.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used 7-Zip to archive data.(Citation: CISA AA20-259A Iran-Based Actor September 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1572 | Protocol Tunneling | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used protocol tunneling for communication and RDP activity on compromised hosts through the use of open source tools such as [ngrok](https://attack.mitre.org/software/S0508) and custom tool SSHMinion.(Citation: CrowdStrike PIONEER KITTEN August 2020)(Citation: CISA AA20-259A Iran-Based Actor September 2020)(Citation: ClearSky Pay2Kitten December 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585 | Establish Accounts | [Fox Kitten](https://attack.mitre.org/groups/G0117) has created KeyBase accounts to communicate with ransomware victims.(Citation: ClearSky Pay2Kitten December 2020)(Citation: Check Point Pay2Key November 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1585.001 | Social Media Accounts | [Fox Kitten](https://attack.mitre.org/groups/G0117) has used a Twitter account to communicate with ransomware victims.(Citation: ClearSky Pay2Kitten December 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 5件
- IOC観測: 5件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 77件（`artifacts.csv`）

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
| source--fox-kitten--68d32d872b6207de | fox kitten |  | 不明 | actor_profile/evidence/fox-kitten.csv | structured-data | TLP:CLEAR | 中 |
| source--fox-kitten--a29f90eeb2998a21 | evol agrius |  | 不明 | Agrius/evol-agrius.pdf | report | TLP:CLEAR | 中 |
| source--fox-kitten--7bf511c858a0593d | ClearSky Fox Kitten Campaign v1 |  | 不明 | International Strategic/Iran/ClearSky-Fox-Kitten-Campaign-v1.pdf | report | TLP:CLEAR | 中 |
| source--fox-kitten--e497b91589d44570 | report incident response middle east |  | 不明 | International Strategic/Iran/report-incident-response-middle-east.pdf | report | TLP:CLEAR | 中 |
| source--fox-kitten--bd43f9bae91915a9 | Dragos 2026 OT Cybersecurity Report A Year in Review |  | 2026 | OT/Dragos-2026-OT-Cybersecurity-Report-A-Year-in-Review.pdf | report | TLP:CLEAR | 中 |
| source--fox-kitten--126387d8e509dcec | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--fox-kitten--e090b856c071a69b | Virtual Routes Pharos Report Series No. 3 |  | 不明 | cybercrime/2025/Virtual-Routes-Pharos-Report-Series-No.-3.pdf | report | TLP:CLEAR | 中 |
| source--fox-kitten--650617e9e84a1999 | microsoft threat actor list |  | 不明 | microsoft-threat-actor-list.xlsx | spreadsheet | TLP:CLEAR | 中 |
| source--fox-kitten--d190a14d35c245e8 | 2021(APT) Microsoft Digital Defense Report |  | 2021 | summary/2021/2021(APT) Microsoft Digital Defense Report.pdf | report | TLP:CLEAR | 中 |
| source--fox-kitten--9d0744f0ec6a67ea | APT group activities under the shadow of the epidemic(2020) |  | 2020 | summary/2021/APT group activities under the shadow of the epidemic(2020).pdf | report | TLP:CLEAR | 中 |
| source--fox-kitten--d845543d641a9f86 | The CrowdStrike 2021 Global Threat Report |  | 2021 | summary/2021/The CrowdStrike 2021 Global Threat Report.pdf | report | TLP:CLEAR | 中 |
| source--fox-kitten--8eddf3afe1311416 | 2021 Advanced Threat Trends Research Report dbappsecurity |  | 2021 | summary/2022/2021 Advanced Threat Trends Research Report-dbappsecurity.pdf | report | TLP:CLEAR | 中 |
| source--fox-kitten--66edc9e16b145a4f | 2022 Global Threat Report |  | 2022 | summary/2022/2022 Global Threat Report.pdf | report | TLP:CLEAR | 中 |
| source--fox-kitten--f4c4e16785f2dd01 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--fox-kitten--b19913b52f96921f | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--fox-kitten--c333de97344e175e | Raport analize PROFILI I GRUPEVE TE HAKERAVE IRANIANE |  | 不明 | summary/2024/Raport-analize-PROFILI-I-GRUPEVE-TE-HAKERAVE-IRANIANE.pdf | report | TLP:CLEAR | 中 |
| source--fox-kitten--db62df908a4cf3b5 | eset threat report h22024 |  | 不明 | summary/2024/eset-threat-report-h22024.pdf | report | TLP:CLEAR | 中 |
| source--fox-kitten--a406ba85b32fce7a | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--fox-kitten--121600b49b777938 | Cybersecurity Threats 2024 Annual Report QAX |  | 2024 | summary/2025/Cybersecurity Threats 2024 Annual Report_QAX.pdf | report | TLP:CLEAR | 中 |
| source--fox-kitten--8763a02dcb2e159c | Dragos 2025 OT Cybersecurity Report A Year in Review |  | 2025 | summary/2025/Dragos-2025-OT-Cybersecurity-Report-A-Year-in-Review.pdf | report | TLP:CLEAR | 中 |
| source--fox-kitten--44003b271e87ab7b | cybercrime multifaceted national security threat |  | 不明 | summary/2025/cybercrime-multifaceted-national-security-threat.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
