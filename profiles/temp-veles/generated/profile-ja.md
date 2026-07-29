# TEMP.Veles 脅威アクタープロファイル

- プロファイルID: `actor--temp-veles`
- 状態: draft
- 更新日時: 2026-07-29T15:38:36Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

TEMP.Velesの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **TEMP.Veles**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| TRISIS | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| Triton | catalog | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |
| XENOTIME | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-1` | Alias scope must be reviewed before publication. |

## 帰属

The repository mapping workbook places this actor in the Russia worksheet.

- 国: Russia
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
| Adversary | [TEMP.Veles](https://attack.mitre.org/groups/G0088) is a Russia-based threat group that has targeted critical infrastructure. The group has been observed utilizing [TRITON](https://attack.mitre.org/software/S0609), a malware framework designed to manipulate industrial safety systems.(Citation: FireEye TRITON 2019)(Citation: FireEye TEMP.Veles 2018)(Citation: FireEye TEMP.Veles JSON April 2019) |
| Capability | Triton, Mimikatz, PsExec |
| Infrastructure |  |
| Victim | Oil refinery, other infrastructure |
| Socio-political | Russia |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-07-25T14:07:08Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| etda-threat-group-cards | TEMP.Veles | canonical-name | 高 | Russia | https://dragos.com/resource/xenotime/<br>https://www.fireeye.com/blog/threat-research/2019/04/triton-actor-ttp-profile-custom-attack-tools-detections.html<br>https://ics-cert.us-cert.gov/sites/default/files/documents/MAR-17-352-01%20HatMan%E2%80%94Safety%20System%20Targeted%20Malware_S508C.pdf |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | TEMP.Veles | canonical-name | 高 |  | https://dragos.com/resource/trisis-analyzing-safety-system-targeting-malware/<br>https://www.fireeye.com/blog/threat-research/2017/12/attackers-deploy-new-ics-attack-framework-triton.html<br>https://attack.mitre.org/groups/G0088/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | TEMP.Veles - G0088 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0088<br>https://dragos.com/resource/xenotime/<br>https://pylos.co/2019/04/12/a-xenotime-to-remember-veles-in-the-wild/ |
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
| malware--triton | Triton | The actor-mapping workbook lists this software or tool. | 不明 | 不明 | 中 | `source--actor-mapping-workbook` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 2014-10-01T04:00:00.000Z | 2017-08-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
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
| C0032 | campaign | 2014-10-01T04:00:00.000Z | 2017-01-01T05:00:00.000Z | 2026-05-12 |  |  | ttp--mitre-campaign--023f70b72f64b5f67d9c, ttp--mitre-campaign--3ba7f12143fe70f675bd, ttp--mitre-campaign--3bb2aac07000c264b64f, ttp--mitre-campaign--4047bfff19aa2396b904, ttp--mitre-campaign--422ac437afb08761baf9, ttp--mitre-campaign--6961fef08dd08ca0cc12, ttp--mitre-campaign--6e1dda584f99f3ad3ac8, ttp--mitre-campaign--79ecf147d17252208628, ttp--mitre-campaign--8680fe94bc75bd7f0aba, ttp--mitre-campaign--877c06cded8ad8dec428, ttp--mitre-campaign--8cca72777cd2d7823d20, ttp--mitre-campaign--91a185565b259f8df517, ttp--mitre-campaign--aa5fdd717d87305589cf, ttp--mitre-campaign--e371388c38e6bf2f5f17, ttp--mitre-campaign--e40f34db33c445ed236c, ttp--mitre-campaign--e86c3cba76bf86afe9ea, ttp--mitre-campaign--f0088e78b1e414a1e4c2 |  | [C0032](https://attack.mitre.org/campaigns/C0032) was an extended campaign suspected to involve the [Triton](https://attack.mitre.org/software/S1009) adversaries with related capabilities and techniques focused on gaining a foothold within IT environments. This campaign occurred in 2019 and was distinctly different from the [Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030).(Citation: FireEye TRITON 2019) | 高 | `source--mitre-attack-19-1` |
| Triton Safety Instrumented System Attack | campaign | 2017-06-01T04:00:00.000Z | 2017-08-01T04:00:00.000Z | 2026-05-12 |  |  | ttp--mitre-campaign--1998a738a233e9a25731, ttp--mitre-campaign--3d8e3df1c423e2ecc5b1, ttp--mitre-campaign--47d04170ee20c13bf35e, ttp--mitre-campaign--6bd42c85b9cb6e5995cd, ttp--mitre-campaign--74baece3a6ca2df2bbb8, ttp--mitre-campaign--8c18db5baf45c52cf640, ttp--mitre-campaign--a8a8d579809a7a485d47, ttp--mitre-campaign--aaaa1a5bdc3185ec1037, ttp--mitre-campaign--d41a62973859a95ff3bf, ttp--mitre-campaign--d6a2b44413491ff742c5 |  | [Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030) was a campaign employed by [TEMP.Veles](https://attack.mitre.org/groups/G0088) which leveraged the [Triton](https://attack.mitre.org/software/S1009) malware framework against a petrochemical organization.(Citation: Triton-EENews-2017) The malware and techniques used within this campaign targeted specific Triconex [Safety Controller](https://attack.mitre.org/assets/A0010)s within the environment.(Citation: FireEye TRITON 2018) The incident was eventually discovered due to a safety trip that occurred as a result of an issue in the malware.(Citation: FireEye TRITON 2017)<br> | 高 | `source--mitre-attack-19-1` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | During the [C0032](https://attack.mitre.org/campaigns/C0032) campaign, [TEMP.Veles](https://attack.mitre.org/groups/G0088) renamed files to look like legitimate files, such as Windows update files or Schneider Electric application files.(Citation: FireEye TRITON 2019) |  | activity--c0032 | 2014-10-01T04:00:00.000Z | 2017-01-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | In the [Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030), [TEMP.Veles](https://attack.mitre.org/groups/G0088) renamed files to look like legitimate files, such as Windows update files or Schneider Electric application files. |  | activity--triton-safety-instrumented-system-attack | 2017-06-01T04:00:00.000Z | 2017-08-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence | T1133 | External Remote Services | During the [C0032](https://attack.mitre.org/campaigns/C0032) campaign, [TEMP.Veles](https://attack.mitre.org/groups/G0088) used VPN access to persist in the victim environment.(Citation: FireEye TRITON 2019) |  | activity--c0032 | 2014-10-01T04:00:00.000Z | 2017-01-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1571 | Non-Standard Port | During the [C0032](https://attack.mitre.org/campaigns/C0032) campaign, [TEMP.Veles](https://attack.mitre.org/groups/G0088) used port-protocol mismatches on ports such as 443, 4444, 8531, and 50501 during C2.(Citation: FireEye TRITON 2019) |  | activity--c0032 | 2014-10-01T04:00:00.000Z | 2017-01-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.001 | LSASS Memory | In the [Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030), [TEMP.Veles](https://attack.mitre.org/groups/G0088) used Mimikatz.(Citation: FireEye TRITON 2018) |  | activity--triton-safety-instrumented-system-attack | 2017-06-01T04:00:00.000Z | 2017-08-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.006 | Timestomp | During the [C0032](https://attack.mitre.org/campaigns/C0032) campaign, [TEMP.Veles](https://attack.mitre.org/groups/G0088) used timestomping to modify the <code>$STANDARD_INFORMATION</code> attribute on tools.(Citation: FireEye TRITON 2019) |  | activity--c0032 | 2014-10-01T04:00:00.000Z | 2017-01-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1546.012 | Image File Execution Options Injection | During the [C0032](https://attack.mitre.org/campaigns/C0032) campaign, [TEMP.Veles](https://attack.mitre.org/groups/G0088) modified and added entries within <code>HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options</code> to maintain persistence.(Citation: FireEye TRITON 2019) |  | activity--c0032 | 2014-10-01T04:00:00.000Z | 2017-01-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | In the [Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030), [TEMP.Veles](https://attack.mitre.org/groups/G0088) used tools such as Mimikatz and other open-source software.(Citation: FireEye TEMP.Veles 2018) |  | activity--triton-safety-instrumented-system-attack | 2017-06-01T04:00:00.000Z | 2017-08-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | During the [C0032](https://attack.mitre.org/campaigns/C0032) campaign, [TEMP.Veles](https://attack.mitre.org/groups/G0088) utilized RDP throughout an operation.(Citation: FireEye TRITON 2019) |  | activity--c0032 | 2014-10-01T04:00:00.000Z | 2017-01-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | In the [Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030), [TEMP.Veles](https://attack.mitre.org/groups/G0088) installed scheduled tasks defined in XML files.(Citation: FireEye TEMP.Veles 2018) |  | activity--triton-safety-instrumented-system-attack | 2017-06-01T04:00:00.000Z | 2017-08-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | During the [C0032](https://attack.mitre.org/campaigns/C0032) campaign, [TEMP.Veles](https://attack.mitre.org/groups/G0088) routinely deleted tools, logs, and other files after they were finished with them.(Citation: FireEye TRITON 2019) |  | activity--c0032 | 2014-10-01T04:00:00.000Z | 2017-01-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573 | Encrypted Channel | In the [Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030), [TEMP.Veles](https://attack.mitre.org/groups/G0088) used cryptcat binaries to encrypt their traffic.(Citation: FireEye TEMP.Veles 2018) |  | activity--triton-safety-instrumented-system-attack | 2017-06-01T04:00:00.000Z | 2017-08-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1583.003 | Virtual Private Server | During the [C0032](https://attack.mitre.org/campaigns/C0032) campaign, [TEMP.Veles](https://attack.mitre.org/groups/G0088) used Virtual Private Server (VPS) infrastructure.(Citation: FireEye TRITON 2019) |  | activity--c0032 | 2014-10-01T04:00:00.000Z | 2017-01-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | During the [C0032](https://attack.mitre.org/campaigns/C0032) campaign, [TEMP.Veles](https://attack.mitre.org/groups/G0088) obtained and used tools such as Mimikatz and PsExec.(Citation: FireEye TRITON 2019) |  | activity--c0032 | 2014-10-01T04:00:00.000Z | 2017-01-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | During the [C0032](https://attack.mitre.org/campaigns/C0032) campaign, [TEMP.Veles](https://attack.mitre.org/groups/G0088) used staging folders that are infrequently used by legitimate users or processes to store data for exfiltration and tool deployment.(Citation: FireEye TRITON 2019) |  | activity--c0032 | 2014-10-01T04:00:00.000Z | 2017-01-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Collection, Credential Access | T1056.003 | Web Portal Capture | In the [Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030), [TEMP.Veles](https://attack.mitre.org/groups/G0088) captured credentials as they were being changed by redirecting text-based login codes to websites they controlled.(Citation: Triton-EENews-2017) |  | activity--triton-safety-instrumented-system-attack | 2017-06-01T04:00:00.000Z | 2017-08-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.004 | SSH | During the [C0032](https://attack.mitre.org/campaigns/C0032) campaign, [TEMP.Veles](https://attack.mitre.org/groups/G0088) relied on encrypted SSH-based tunnels to transfer tools and for remote command/program execution.(Citation: FireEye TRITON 2019) |  | activity--c0032 | 2014-10-01T04:00:00.000Z | 2017-01-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.001 | LSASS Memory | During the [C0032](https://attack.mitre.org/campaigns/C0032) campaign, [TEMP.Veles](https://attack.mitre.org/groups/G0088) used Mimikatz and a custom tool, SecHack, to harvest credentials.(Citation: FireEye TRITON 2019) |  | activity--c0032 | 2014-10-01T04:00:00.000Z | 2017-01-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.005 | Indicator Removal from Tools | In the [Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030), [TEMP.Veles](https://attack.mitre.org/groups/G0088) modified files based on the open-source project cryptcat in an apparent attempt to decrease anti-virus detection rates.(Citation: FireEye TEMP.Veles 2018) |  | activity--triton-safety-instrumented-system-attack | 2017-06-01T04:00:00.000Z | 2017-08-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | During the [C0032](https://attack.mitre.org/campaigns/C0032) campaign, [TEMP.Veles](https://attack.mitre.org/groups/G0088) used compromised VPN accounts.(Citation: FireEye TRITON 2019) |  | activity--c0032 | 2014-10-01T04:00:00.000Z | 2017-01-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | In the [Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030), [TEMP.Veles](https://attack.mitre.org/groups/G0088) developed, prior to the attack, malware capabilities that would require access to specific and specialized hardware and software.(Citation: FireEye TRITON Dec 2017) |  | activity--triton-safety-instrumented-system-attack | 2017-06-01T04:00:00.000Z | 2017-08-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | In the [Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030), [TEMP.Veles](https://attack.mitre.org/groups/G0088) used a publicly available PowerShell-based tool, WMImplant.(Citation: FireEye TEMP.Veles 2018) |  | activity--triton-safety-instrumented-system-attack | 2017-06-01T04:00:00.000Z | 2017-08-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1595 | Active Scanning | In the [Triton Safety Instrumented System Attack](https://attack.mitre.org/campaigns/C0030), [TEMP.Veles](https://attack.mitre.org/groups/G0088) engaged in network reconnaissance against targets of interest.(Citation: FireEye TEMP.Veles 2018) |  | activity--triton-safety-instrumented-system-attack | 2017-06-01T04:00:00.000Z | 2017-08-01T04:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.003 | Web Shell | During the [C0032](https://attack.mitre.org/campaigns/C0032) campaign, [TEMP.Veles](https://attack.mitre.org/groups/G0088) planted Web shells on Outlook Exchange servers.(Citation: FireEye TRITON 2019) |  | activity--c0032 | 2014-10-01T04:00:00.000Z | 2017-01-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution, Persistence, Privilege Escalation | T1053.005 | Scheduled Task | During the [C0032](https://attack.mitre.org/campaigns/C0032) campaign, [TEMP.Veles](https://attack.mitre.org/groups/G0088) used scheduled task XML triggers.(Citation: FireEye TRITON 2019) |  | activity--c0032 | 2014-10-01T04:00:00.000Z | 2017-01-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell | During the [C0032](https://attack.mitre.org/campaigns/C0032) campaign, [TEMP.Veles](https://attack.mitre.org/groups/G0088) used PowerShell to perform timestomping.(Citation: FireEye TRITON 2019) |  | activity--c0032 | 2014-10-01T04:00:00.000Z | 2017-01-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1572 | Protocol Tunneling | During the [C0032](https://attack.mitre.org/campaigns/C0032) campaign, [TEMP.Veles](https://attack.mitre.org/groups/G0088) used encrypted SSH-based PLINK tunnels to transfer tools and enable RDP connections throughout the environment.(Citation: FireEye TRITON 2019) |  | activity--c0032 | 2014-10-01T04:00:00.000Z | 2017-01-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 35件（`artifacts.csv`）

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
| source--temp-veles--bc16c3e80e2172da | temp veles |  | 不明 | actor_profile/evidence/temp-veles.csv | structured-data | TLP:CLEAR | 中 |
| source--temp-veles--25b80e8adcca4c71 | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--temp-veles--e84ff1ed26055019 | ICS eng |  | 不明 | OT/ICS_eng.pdf | report | TLP:CLEAR | 中 |
| source--temp-veles--54ace8e71fe6a32e | pipedream chernovite emerging malware targeting ics |  | 不明 | OT/pipedream-chernovite-emerging-malware-targeting-ics.pdf | report | TLP:CLEAR | 中 |
| source--temp-veles--e8890a524a3953f2 | Buying Spying Insights into Commercial Surveillance Vendors TAG report |  | 不明 | Spyware/Buying_Spying_-_Insights_into_Commercial_Surveillance_Vendors_-_TAG_report.pdf | report | TLP:CLEAR | 中 |
| source--temp-veles--557b0c2f5ad1ca46 | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--temp-veles--7a8bb1afce04f0e5 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--temp-veles--3c7f80240ef9dc63 | 2021(APT) Microsoft Digital Defense Report |  | 2021 | summary/2021/2021(APT) Microsoft Digital Defense Report.pdf | report | TLP:CLEAR | 中 |
| source--temp-veles--2752b45bd086986d | Google Cybersecurity Action Team Threat Horizons Report#5 |  | 不明 | summary/2023/Google_Cybersecurity_Action_Team_Threat_Horizons_Report#5.pdf | report | TLP:CLEAR | 中 |
| source--temp-veles--43b25dbc348d783b | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
