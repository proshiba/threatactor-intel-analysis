# UNC3886 脅威アクタープロファイル

- プロファイルID: `actor--unc3886`
- 状態: draft
- 更新日時: 2026-07-29T15:38:36Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

UNC3886の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **UNC3886**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

Aliasなし

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
| Adversary | [UNC3886](https://attack.mitre.org/groups/G1048) is a China-nexus cyberespionage group that has been active since at least 2022, targeting defense, technology, and telecommunication organizations located in the United States and the Asia-Pacific-Japan (APJ) regions. [UNC3886](https://attack.mitre.org/groups/G1048) has displayed a deep understanding of edge devices and virtualization technologies through the exploitation of zero-day vulnerabilities and the use of novel malware families and utilities.(Citation: Mandiant Fortinet Zero Day)(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023) |
| Capability | MEDUSA, CASTLETAP, THINCRUST, REPTILE, VIRTUALPIE, MOPSLED, RIFLESPINE, VIRTUALPITA |
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
| etda-threat-group-cards | UNC3886 | canonical-name | 高 | China | https://cloud.google.com/blog/topics/threat-intelligence/uncovering-unc3886-espionage-operations<br>https://therecord.media/singapore-accuses-chinese-backed-hackers-critical-infrastructure-attacks<br>https://www.trendmicro.com/en_us/research/25/g/revisiting-unc3886-tactics-to-defend-against-present-risk.html |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | UNC3886 | canonical-name | 高 | CN | https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem<br>https://www.mandiant.com/resources/blog/esxi-hypervisors-malware-persistence<br>https://www.mandiant.com/resources/blog/vmware-esxi-zero-day-bypass |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | UNC3886 - G1048 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1048<br>https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/<br>https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem |
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
| malware--castletap | CASTLETAP | [CASTLETAP](https://attack.mitre.org/software/S1224) is an ICMP port knocking backdoor that has been installed on compromised FortiGate firewalls by [UNC3886](https://attack.mitre.org/groups/G1048).(Citation: Mandiant Fortinet Zero Day) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--medusa | MEDUSA | [MEDUSA](https://attack.mitre.org/software/S1220) is an open-source rootkit that is capable of dynamic linker hijacking, command execution, and logging credentials.(Citation: Google Cloud Mandiant UNC3886 2024) | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| malware--mopsled | MOPSLED | [MOPSLED](https://attack.mitre.org/software/S1221) is a shellcode-based modular backdoor that has been used by China-nexus cyber espionage actors including [UNC3886](https://attack.mitre.org/groups/G1048) and [APT41](https://attack.mitre.org/groups/G0096).(Citation: Google Cloud Mandiant UNC3886 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--reptile | REPTILE | [REPTILE](https://attack.mitre.org/software/S1219) is an open-source Linux rootkit with multiple components that provides backdoor access and functionality.(Citation: Google Cloud Mandiant UNC3886 2024) | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| malware--riflespine | RIFLESPINE | [RIFLESPINE](https://attack.mitre.org/software/S1222) is a cross-platform backdoor that leverages Google Drive for file transfer and command execution.(Citation: Google Cloud Mandiant UNC3886 2024) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--thincrust | THINCRUST | [THINCRUST](https://attack.mitre.org/software/S1223) is a Python-based backdoor tool that has been used by [UNC3886](https://attack.mitre.org/groups/G1048) since at least 2023.(Citation: Mandiant Fortinet Zero Day) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--virtualpie | VIRTUALPIE | [VIRTUALPIE](https://attack.mitre.org/software/S1218) is a lightweight backdoor written in Python that spawns an IPv6 listener on a VMware ESXi server and features command line execution, file transfer,  and reverse shell capabilities. [VIRTUALPIE](https://attack.mitre.org/software/S1218) has been in use since at least 2022 including by [UNC3886](https://attack.mitre.org/groups/G1048) who installed it via malicious vSphere Installation Bundles (VIBs).(Citation: Google Cloud Threat Intelligence ESXi VIBs 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| malware--virtualpita | VIRTUALPITA | [VIRTUALPITA](https://attack.mitre.org/software/S1217) is a passive backdoor with ESXi and Linux vCenter variants capable of command execution, file transfer, and starting and stopping processes. [VIRTUALPITA](https://attack.mitre.org/software/S1217) has been in use since at least 2022 including by [UNC3886](https://attack.mitre.org/groups/G1048) who leveraged malicious vSphere Installation Bundles (VIBs) for install on ESXi hypervisors.(Citation: Google Cloud Threat Intelligence ESXi VIBs 2022) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| 中国関連のUNC3886、サイバースパイ活動でシンガポール通信業界を標的に | cyber-espionage | 不明 | 不明 | 2026-02-10 | target--mitre-group--sector--821695aff5b1b61d9bc1 |  |  | victim--activity-rule--eba9c2c4be97b5bcf961 | シンガポールのCSAは、中国系APT「UNC3886」が国内の主要通信事業者4社を狙う標的型スパイ活動を行ったと公表した。 攻撃は周到に計画され、境界ファイアウォールを迂回するためゼロデイを武器化し、技術データを少量取得した事例がある。 別事例ではルートキットを展開して永続化と痕跡隠蔽を図り、一部ネットワーク領域（重要と見なされる領域を含む）へ不正アクセスした。 ただしサービス停止に至るほど深刻ではなく、顧客記録など個人データ流出やインターネット断の証拠はないとCSAは述べた。 CSAは「CYBER GUARDIAN」作戦で対抗し、侵入口の遮断や監視強化などの是正措置を通信各社で進めたとしている。 | 高 | `source--daily-7033dbe4bb2c2c20106c` |
| 中国のサイバースパイ、Juniperルーターにバックドアを仕掛けてステルスアクセスを実現 | cyber-espionage | 不明 | 不明 | 2025-03-13 |  |  |  |  | 中国のハッカーグループUNC3886は、サポートが終了したJuniper NetworksのJunos OS MXルーターにカスタムバックドアを展開し、ステルスアクセスを実現している。 これらのバックドアは、Linuxシステム上でデータ交換やコマンド実行を可能にするオープンソースツール「TinyShell」の亜種である。 攻撃者は、ネットワークデバイスを管理するためのターミナルサーバーから侵入し、Junos OSのCLIにアクセス、FreeBSDシェルモードにエスカレーションしている。 信頼されたプロセスにコードを注入することで、Junos OSのファイル整合性システム「Veriexec」を回避し、6つのカスタムバックドアをMXルーターにインストールしている。 UNC3886は、以前にもFortinetやVMware ESXiのゼロデイ脆弱性を利用した攻撃を行っていた。 | 中 | `source--daily-68aa782163620e0cd16f` |
| Juniper、2024年半ば以降、中国のサイバースパイがルーターにバックドアを仕掛けた脆弱性を修正 | cyber-espionage | 不明 | 不明 | 2025-03-14 |  |  |  |  | Juniper Networksは、Junos OSの脆弱性（CVE-2025-21590）を修正する緊急セキュリティアップデートをリリースしました。 この脆弱性は、中国のサイバースパイグループUNC3886によって悪用され、ルーターにバックドアを設置されていました。 攻撃者は、TINYSHELLバックドアの改変版を使用し、ルーターへのステルスアクセスを維持していました。 脆弱性は、NFXシリーズ、Virtual SRX、SRXシリーズ、EXシリーズ、QFXシリーズ、ACX、MXシリーズのデバイスに影響を及ぼします。 Juniperは、影響を受けるデバイスのファームウェアを最新バージョンにアップデートすることを強く推奨しています。 | 中 | `source--daily-dd052f5bf8f217c32fc3` |
| UNC3886のハッカーがLinuxルートキットを使用してVMware ESXi VMに潜伏 | malware-campaign | 不明 | 不明 | 2024-06-21 | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--b8d6639a1884e2bacaa4, target--activity-rule--sector--fb803c0a91ed53ea76f9, target--mitre-group--sector--e68e01d9baac208e6b2d | malware--medusa, malware--mopsled, malware--reptile, malware--riflespine |  | victim--activity-rule--fb99d2c0e1337648a132 | UNC3886という中国のハッカー集団がLinuxルートキット「Reptile」と「Medusa」を使用してVMware ESXi仮想マシンに潜伏 これらのルートキットは長期的なアクセス維持と検出回避のために使用 攻撃は政府、通信、技術、航空宇宙、防衛、エネルギー・ユーティリティ部門をターゲット 地理的には、北米、東南アジア、オセアニアの組織を標的としており、ヨーロッパ、アフリカ、アジアの他の地域でも被害者が確認されている UNC3886はカスタムマルウェアツール「Mopsled」や「Riflespine」を使用 | 高 | `source--daily-4fd1a9d4d043a65933bd` |
| 中国のサイバー諜報グループがFortinetとVMwareのゼロデイを悪用 | cyber-espionage | 不明 | 不明 | 2024-06-20 | target--activity-rule--sector--210dddb39397dbe50e91 | malware--medusa, malware--mopsled, malware--reptile, malware--riflespine | ttp--activity-rule--4b68390034dd0a918d46 | victim--activity-rule--ea1152a5d569414a67bb | UNC3886がFortinetとVMwareのゼロデイ脆弱性を利用。 侵入後、持続的なアクセスを確保するための多くの手法を使用。 北米、東南アジア、オセアニアの政府や企業を主な標的。 ReptileやMedusaなどのルートキットを使用。 GitHubとGoogle DriveをC2チャンネルとして活用するMOPSLEDとRIFLESPINEといったバックドアも利用。 | 中 | `source--daily-2991ab0470fb4a03b3f8` |
| RedPenguin | campaign | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 2026-05-12 |  | malware--medusa, malware--reptile | ttp--mitre-campaign--08acf831aa5f21efc6cc, ttp--mitre-campaign--17ac5ae8828f0e5e6755, ttp--mitre-campaign--265dbd000d8ddc451e5a, ttp--mitre-campaign--3914e5b54be82cc8d66b, ttp--mitre-campaign--427f0f6f61e6a719c020, ttp--mitre-campaign--5863cbc30bb68710714a, ttp--mitre-campaign--5afc7da9618dfa8f1a0a, ttp--mitre-campaign--64c2f929021967ac10d4, ttp--mitre-campaign--6e804efb01a0ebd3e8c2, ttp--mitre-campaign--7622212b1a65bdcc887f, ttp--mitre-campaign--77515494201647c9e27d, ttp--mitre-campaign--7d3ae469a41321736e42, ttp--mitre-campaign--80d19865f75e3da5dc96, ttp--mitre-campaign--829c435afdc9dd012f72, ttp--mitre-campaign--97376d5a2ae3627753a5, ttp--mitre-campaign--9ba4c615f3f2810d25ec, ttp--mitre-campaign--9d551f6c5d33c8d526ea, ttp--mitre-campaign--a1a85fbf7d7a470f82a9, ttp--mitre-campaign--a438d8e0f62e542e8149, ttp--mitre-campaign--a7c159e46c2d21e2584d, ttp--mitre-campaign--abbbfed5cc4113d555e0, ttp--mitre-campaign--bf327b3e5b4642f4573c, ttp--mitre-campaign--dc6aafc7f13540e9c00e, ttp--mitre-campaign--e5e4c0875bfa513a1e3e, ttp--mitre-campaign--e6fc785007a6dfdb6edc, ttp--mitre-campaign--ff05cc93ff678bea66e9 |  | The [RedPenguin](https://attack.mitre.org/campaigns/C0056) project was launched by Juniper in July 2024 to investigate reported malware infections of Juniper MX Series routers. [RedPenguin](https://attack.mitre.org/campaigns/C0056) activity was separately attributed to [UNC3886](https://attack.mitre.org/groups/G1048) and included the deployment of multiple custom versions of the publicly-available TINYSHELL backdoor on Juniper routers.(Citation: Juniper RedPenguin MAR 2025)(Citation: Mandiant UNC3886 Juniper Routers MAR 2025) | 高 | `source--mitre-attack-19-1` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 米国 | [UNC3886](https://attack.mitre.org/groups/G1048) is a China-nexus cyberespionage group that has been active since at least 2022, targeting defense, technology, and telecommunication organizations located in the United States and the Asia-Pacific-Japan (APJ) regions. | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| sectors | 政府・行政 | 活動「UNC3886のハッカーがLinuxルートキットを使用してVMware ESXi VMに潜伏」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-2991ab0470fb4a03b3f8`, `source--daily-4fd1a9d4d043a65933bd` |
| sectors | 運輸・航空・海運 | 活動「UNC3886のハッカーがLinuxルートキットを使用してVMware ESXi VMに潜伏」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-4fd1a9d4d043a65933bd` |
| sectors | エネルギー | 活動「UNC3886のハッカーがLinuxルートキットを使用してVMware ESXi VMに潜伏」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-4fd1a9d4d043a65933bd` |
| sectors | 情報通信 | [UNC3886](https://attack.mitre.org/groups/G1048) is a China-nexus cyberespionage group that has been active since at least 2022, targeting defense, technology, and telecommunication organizations located in the United States and the Asia-Pacific-Japan (APJ) regions. | 不明 | 不明 | 高 | `source--daily-7033dbe4bb2c2c20106c`, `source--mitre-attack-19-1` |
| sectors | 防衛・軍事 | [UNC3886](https://attack.mitre.org/groups/G1048) is a China-nexus cyberespionage group that has been active since at least 2022, targeting defense, technology, and telecommunication organizations located in the United States and the Asia-Pacific-Japan (APJ) regions. | 不明 | 不明 | 高 | `source--daily-4fd1a9d4d043a65933bd`, `source--mitre-attack-19-1` |

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: 中国のサイバー諜報グループがFortinetとVMwareのゼロデイを悪用 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--210dddb39397dbe50e91 | malware--medusa, malware--mopsled, malware--reptile, malware--riflespine | ttp--activity-rule--4b68390034dd0a918d46 | 開発環境／ソースコード | espionage: 中国のサイバー諜報グループがFortinetとVMwareのゼロデイを悪用 | 不明 | 不明 | 2024-06-20 | 中 | `source--daily-2991ab0470fb4a03b3f8` |
| 被害事例: 中国関連のUNC3886、サイバースパイ活動でシンガポール通信業界を標的に | 非公開 | anonymous | unknown | reported | target--mitre-group--sector--821695aff5b1b61d9bc1 |  |  | ネットワーク機器 | data-theft: ただしサービス停止に至るほど深刻ではなく、顧客記録など個人データ流出やインターネット断の証拠はないとCSAは述べた。<br>disruption: ただしサービス停止に至るほど深刻ではなく、顧客記録など個人データ流出やインターネット断の証拠はないとCSAは述べた。<br>espionage: 中国関連のUNC3886、サイバースパイ活動でシンガポール通信業界を標的に | 不明 | 不明 | 2026-02-10 | 高 | `source--daily-7033dbe4bb2c2c20106c` |
| 被害事例: UNC3886のハッカーがLinuxルートキットを使用してVMware ESXi VMに潜伏 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--b8d6639a1884e2bacaa4, target--activity-rule--sector--fb803c0a91ed53ea76f9, target--mitre-group--sector--e68e01d9baac208e6b2d | malware--medusa, malware--mopsled, malware--reptile, malware--riflespine |  |  |  | 不明 | 不明 | 2024-06-21 | 高 | `source--daily-4fd1a9d4d043a65933bd` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1102.003 | One-Way Communication | GitHubとGoogle DriveをC2チャンネルとして活用するMOPSLEDとRIFLESPINEといったバックドアも利用。 | malware--mopsled, malware--riflespine | activity--daily-c8c7410b209e5a38dbfe | 不明 | 不明 | 中 | `source--daily-2991ab0470fb4a03b3f8` |
| Resource Development | T1587.001 | Malware | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) deployed custom malware based on the publicly-available TINYSHELL backdoor.(Citation: Mandiant UNC3886 Juniper Routers MAR 2025)(Citation: Censys RedPenguin MAR 2025) |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Stealth | T1014 | Rootkit | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) used rootkits such as [REPTILE](https://attack.mitre.org/software/S1219) and [MEDUSA](https://attack.mitre.org/software/S1220).(Citation: Mandiant UNC3886 Juniper Routers MAR 2025) |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Command And Control, Persistence, Stealth | T1205 | Traffic Signaling | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) leveraged malware capable of inpecting packets for a magic-string to activate backdoor functionalities.(Citation: Mandiant UNC3886 Juniper Routers MAR 2025)<br> |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) used malware capaple of removing scripts after execution.(Citation: Mandiant UNC3886 Juniper Routers MAR 2025)<br><br> |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) created multiple strains of malware using names to mimic legitimate binaries such as appid, to, irad, lmpad, jdosd, and oemd.(Citation: Mandiant UNC3886 Juniper Routers MAR 2025)<br> |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055 | Process Injection | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) exploited CVE-2025-21590 to enable malicious code injection into the memory of legitimate processes.(Citation: Mandiant UNC3886 Juniper Routers MAR 2025)(Citation: Juniper RedPenguin MAR 2025) |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.007 | Clear Network Connection History and Configurations | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) used an implant to delete logs associated with unauthorized access to targeted Junos OS devices.(Citation: Juniper RedPenguin MAR 2025) |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Persistence | T1554 | Compromise Host Software Binary | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) peformed a local memory patching attack to modify the snmpd and mgd Junos OS daemons.(Citation: Juniper RedPenguin MAR 2025)<br> |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1104 | Multi-Stage Channels | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) used malware with separate channels to request and carry out tasks from C2.(Citation: Mandiant UNC3886 Juniper Routers MAR 2025) |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1095 | Non-Application Layer Protocol | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) leveraged malware that used UDP and TCP sockets for C2.(Citation: Mandiant UNC3886 Juniper Routers MAR 2025)(Citation: Censys RedPenguin MAR 2025)(Citation: Juniper RedPenguin MAR 2025) |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1105 | Ingress Tool Transfer | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) used backdoor malware capable of downloading files to compromised infrastructure.(Citation: Mandiant UNC3886 Juniper Routers MAR 2025) |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.004 | Unix Shell | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) used malware capable of launching an interactive shell.(Citation: Mandiant UNC3886 Juniper Routers MAR 2025)(Citation: Juniper RedPenguin MAR 2025) |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090 | Proxy | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) used malware capable of establishing a SOCKS proxy connection to a specified IP and port.(Citation: Mandiant UNC3886 Juniper Routers MAR 2025)(Citation: Juniper RedPenguin MAR 2025) |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Stealth | T1140 | Deobfuscate/Decode Files or Information | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) used malware implants to deobfuscate incoming C2 messages and encoded archives.(Citation: Mandiant UNC3886 Juniper Routers MAR 2025)(Citation: Juniper RedPenguin MAR 2025) |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1690 | Prevent Command History Logging | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) used malware to clear the `HISTFILE` environmental variable and to inject into Junos OS processes to inhibit logging.(Citation: Mandiant UNC3886 Juniper Routers MAR 2025)(Citation: Juniper RedPenguin MAR 2025)<br> |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.008 | Network Device CLI | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) accessed the Junos OS CLI on targeted devices.(Citation: Mandiant UNC3886 Juniper Routers MAR 2025)(Citation: Juniper RedPenguin MAR 2025) |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Discovery | T1016 | System Network Configuration Discovery | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) leveraged JunoOS CLI queries to obtain the interface index which contains system and network details.(Citation: Mandiant UNC3886 Juniper Routers MAR 2025)(Citation: Juniper RedPenguin MAR 2025) |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) used legitimate credentials to gain priviliged access to Juniper routers.(Citation: Mandiant UNC3886 Juniper Routers MAR 2025)(Citation: Censys RedPenguin MAR 2025)<br><br> |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1571 | Non-Standard Port | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) used a backdoor that binds to port 45678 by default.(Citation: Mandiant UNC3886 Juniper Routers MAR 2025)<br> |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) exploited CVE-2025-21590 to bypass Veriexec protections in Junos OS designed to prevent unauthorized binary execution.(Citation: Mandiant UNC3886 Juniper Routers MAR 2025)(Citation: Juniper RedPenguin MAR 2025)<br> |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1041 | Exfiltration Over C2 Channel | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) uploaded specified files from compromised devices to a remote server. (Citation: Mandiant UNC3886 Juniper Routers MAR 2025) |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573.001 | Symmetric Cryptography | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) malware used the RC4 cipher to encrypt outgoing C2 messages.(Citation: Juniper RedPenguin MAR 2025)<br> |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090.003 | Multi-hop Proxy | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) used infrastructure associated with operational relay box (ORB) networks.(Citation: Mandiant UNC3886 Juniper Routers MAR 2025) |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.013 | Encrypted/Encoded File | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) generated Base64-encoded files in the FreeBSD shell environment of targeted Juniper devices.(Citation: Mandiant UNC3886 Juniper Routers MAR 2025)(Citation: Juniper RedPenguin MAR 2025)<br> |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) used malware capable of reading the PID for the Junos OS snmpd daemon.(Citation: Juniper RedPenguin MAR 2025) |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Credential Access, Discovery | T1040 | Network Sniffing | During [RedPenguin](https://attack.mitre.org/campaigns/C0056), [UNC3886](https://attack.mitre.org/groups/G1048) used a passive backdoor to act as a libpcap-based packet sniffer.(Citation: Mandiant UNC3886 Juniper Routers MAR 2025)<br> |  | activity--redpenguin | 2024-07-01T04:00:00.000Z | 2025-03-01T05:00:00.000Z | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1003.001 | LSASS Memory |  [UNC3886](https://attack.mitre.org/groups/G1048) has used MiniDump to dump process memory and search for cleartext credentials.(Citation: Google Cloud Threat Intelligence ESXi VIBs 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1008 | Fallback Channels | [UNC3886](https://attack.mitre.org/groups/G1048) has employed layers of redundancy to maintain access to compromised environments including network devices, hypervisors, and virtual machines.(Citation: Google Cloud Mandiant UNC3886 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1014 | Rootkit | [UNC3886](https://attack.mitre.org/groups/G1048) has used the publicly available rootkits [REPTILE](https://attack.mitre.org/software/S1219) and [MEDUSA](https://attack.mitre.org/software/S1220) on targeted VMs.(Citation: Google Cloud Mandiant UNC3886 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1021.004 | SSH | [UNC3886](https://attack.mitre.org/groups/G1048) has established remote SSH access to targeted ESXi hosts.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023)(Citation: Mandiant Fortinet Zero Day) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1027.005 | Indicator Removal from Tools | [UNC3886](https://attack.mitre.org/groups/G1048) has replaced atomic indicators mentioned in threat intelligence publications, sometimes as quickly as under a week after release.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.004 | Masquerade Task or Service | [UNC3886](https://attack.mitre.org/groups/G1048) has named a file ‘fgfm’ in an attempt to disguise it as the legitimate service ‘fgfmd’ which facilitates communication between FortiManager and the FortiGate firewall.(Citation: Mandiant Fortinet Zero Day) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1037 | Boot or Logon Initialization Scripts | [UNC3886](https://attack.mitre.org/groups/G1048) has attempted to bypass digital signature verification checks at startup by adding a command to the startup config `/etc/init.d/localnet` within the rootfs.gz archive of both FortiManager and FortiAnalyzer devices.(Citation: Mandiant Fortinet Zero Day) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1037.004 | RC Scripts | [UNC3886](https://attack.mitre.org/groups/G1048) has placed a bash installation script into `/etc/rc.local.d/` to establish persistence.(Citation: Google Cloud Threat Intelligence ESXi VIBs 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access, Discovery | T1040 | Network Sniffing | [UNC3886](https://attack.mitre.org/groups/G1048) has used the LOOKOVER sniffer to sniff TACACS+ authentication packets.(Citation: Google Cloud Mandiant UNC3886 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1057 | Process Discovery | [UNC3886](https://attack.mitre.org/groups/G1048) has run scripts to list all running processes on a guest VM from an ESXi host.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.001 | PowerShell |  [UNC3886](https://attack.mitre.org/groups/G1048) has used a PowerShell script to search memory dumps for credentials.(Citation: Google Cloud Threat Intelligence ESXi VIBs 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.003 | Windows Command Shell |  [UNC3886](https://attack.mitre.org/groups/G1048) has executed Windows commands on guest virtual machines through `vmtoolsd.exe`.(Citation: Google Cloud Threat Intelligence ESXi VIBs 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.004 | Unix Shell |  [UNC3886](https://attack.mitre.org/groups/G1048) has used a bash script to install malicious vSphere Installation Bundles (VIBs).(Citation: Google Cloud Threat Intelligence ESXi VIBs 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.006 | Python | [UNC3886](https://attack.mitre.org/groups/G1048) has used Python scripts to enumerate ESXi hosts and guest VMs.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.012 | Hypervisor CLI | [UNC3886](https://attack.mitre.org/groups/G1048) has used the esxcli command line utility to modify firewall rules, install malware, and for artifact removal.(Citation: Google Cloud Threat Intelligence ESXi VIBs 2022)(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1068 | Exploitation for Privilege Escalation | [UNC3886](https://attack.mitre.org/groups/G1048) has exploited zero-day vulnerability CVE-2023-20867 to enable execution of privileged commands across Windows, Linux, and PhotonOS (vCenter) guest VMs.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.004 | File Deletion | [UNC3886](https://attack.mitre.org/groups/G1048) has used the the esxcli command line to remove files created by malicious vSphere Installation Bundles from disk.(Citation: Google Cloud Threat Intelligence ESXi VIBs 2022)(Citation: Mandiant Fortinet Zero Day) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.006 | Timestomp | [UNC3886](https://attack.mitre.org/groups/G1048) has used scripts to timestomp ESXi hosts prior to installing malicious vSphere Installation Bundles (VIBs).(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1070.007 | Clear Network Connection History and Configurations | [UNC3886](https://attack.mitre.org/groups/G1048) has cleared specific events that contained the threat actor’s IP address from multiple log sources.(Citation: Mandiant Fortinet Zero Day) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1074.001 | Local Data Staging | <br>[UNC3886](https://attack.mitre.org/groups/G1048) has staged captured credentials in `var/log/ldapd<unique_keyword>.2.gz`.(Citation: Google Cloud Mandiant UNC3886 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [UNC3886](https://attack.mitre.org/groups/G1048) has used tools to hijack valid SSH accounts.(Citation: Google Cloud Mandiant UNC3886 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.001 | Default Accounts | [UNC3886](https://attack.mitre.org/groups/G1048) has harvested and used vCenter Server service accounts.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery |  [UNC3886](https://attack.mitre.org/groups/G1048) has used `vmtoolsd.exe` to enumerate files on guest machines.(Citation: Google Cloud Threat Intelligence ESXi VIBs 2022)(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1095 | Non-Application Layer Protocol | [UNC3886](https://attack.mitre.org/groups/G1048) has deployed backdoors that communicate over TCP to compromised network devices and over VMCI to ESXi hosts.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023)(Citation: Google Cloud Mandiant UNC3886 2024)(Citation: Mandiant Fortinet Zero Day)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1124 | System Time Discovery | [UNC3886](https://attack.mitre.org/groups/G1048) has used installation scripts to collect the system time on targeted ESXi hosts.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [UNC3886](https://attack.mitre.org/groups/G1048) has exploited CVE-2022-42475 in FortiOS SSL VPNs to obtain access.(Citation: Google Cloud Mandiant UNC3886 2024)(Citation: Mandiant Fortinet Zero Day) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1203 | Exploitation for Client Execution | [UNC3886](https://attack.mitre.org/groups/G1048) has exoloited CVE-2023-34048 to enable command execution on vCenter servers and CVE-2023-20867 in VMware Tools to execute unauthenticated Guest Operations from ESXi hosts to guest VMs.(Citation: Google Cloud Mandiant UNC3886 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control, Persistence, Stealth | T1205 | Traffic Signaling | [UNC3886](https://attack.mitre.org/groups/G1048) has used the TABLEFLIP traffic redirection utility to listen for specialized command packets on compromised FortiManager devices.(Citation: Mandiant Fortinet Zero Day) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control, Persistence, Stealth | T1205.001 | Port Knocking | [UNC3886](https://attack.mitre.org/groups/G1048) maintained persistence on FortiGate Firewalls through ICMP port knocking.(Citation: Mandiant Fortinet Zero Day) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1212 | Exploitation for Credential Access | [UNC3886](https://attack.mitre.org/groups/G1048) exploited CVE-2022-22948 in VMware vCenter to obtain encrypted credentials from the vCenter postgresDB.(Citation: Google Cloud Mandiant UNC3886 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1218.011 | Rundll32 |  [UNC3886](https://attack.mitre.org/groups/G1048) has used rundll32.exe to execute MiniDump for dumping LSASS process memory.(Citation: Google Cloud Threat Intelligence ESXi VIBs 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1505.006 | vSphere Installation Bundles | [UNC3886](https://attack.mitre.org/groups/G1048) has used vSphere Installation Bundles (VIBs) to install malware and establish persistence across ESXi hypervisors.(Citation: Google Cloud Threat Intelligence ESXi VIBs 2022)(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023)(Citation: Mandiant Fortinet Zero Day) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation | T1548 | Abuse Elevation Control Mechanism |  [UNC3886](https://attack.mitre.org/groups/G1048) has used vSphere Installation Bundles (VIBs) that contained modified descriptor XML files with the `acceptance-level` set to `partner` which allowed for privilege escalation.(Citation: Google Cloud Threat Intelligence ESXi VIBs 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1554 | Compromise Host Software Binary | [UNC3886](https://attack.mitre.org/groups/G1048) has trojanized Fortinet firmware and replaced the legitimate `/usr/bin/tac_plus` TACACS+ daemon for Linux with a malicious version containing credential logging functionality.(Citation: Google Cloud Mandiant UNC3886 2024)(Citation: Mandiant Fortinet Zero Day) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1555.005 | Password Managers |  [UNC3886](https://attack.mitre.org/groups/G1048) has targeted KeyPass password database files for credential access.(Citation: Google Cloud Threat Intelligence ESXi VIBs 2022) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.001 | Archive via Utility | [UNC3886](https://attack.mitre.org/groups/G1048) has used Gzip and the Windows command `makecab` to compress files and stolen credentials from victim systems.(Citation: Google Cloud Threat Intelligence ESXi VIBs 2022)(Citation: Google Cloud Mandiant UNC3886 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1560.003 | Archive via Custom Method | [UNC3886](https://attack.mitre.org/groups/G1048) has XOR encrypted and Gzip compressed captured credentials.(Citation: Google Cloud Mandiant UNC3886 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1564.011 | Ignore Process Interrupts | [UNC3886](https://attack.mitre.org/groups/G1048) modified the startup file `/etc/init.d/localnet` to execute the line `nohup /bin/support &` so the script would run when the system was rebooted.(Citation: Mandiant Fortinet Zero Day) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1570 | Lateral Tool Transfer | [UNC3886](https://attack.mitre.org/groups/G1048) has utilzed Python scripts to transfer files between ESXi hosts and guest VMs.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | [UNC3886](https://attack.mitre.org/groups/G1048) has deployed custom malware families on Fortinet and VMware systems.(Citation: Mandiant Fortinet Zero Day) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.004 | Exploits | [UNC3886](https://attack.mitre.org/groups/G1048) has used zero-day vulnerabilities CVE-2022-41328 against FortiOS and CVE-2023-20867 and CVE-2023-34048 against VMware vCenter.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023)(Citation: Google Cloud Mandiant UNC3886 2024)(Citation: Mandiant Fortinet Zero Day) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.001 | Malware | [UNC3886](https://attack.mitre.org/groups/G1048) has used the publicly available rootkits [REPTILE](https://attack.mitre.org/software/S1219) and [MEDUSA](https://attack.mitre.org/software/S1220).(Citation: Google Cloud Mandiant UNC3886 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.004 | Digital Certificates | [UNC3886](https://attack.mitre.org/groups/G1048) has deployed malware using the victim's legitimate TLS certificate obtained from a compromised FortiGate device.(Citation: Google Cloud Mandiant UNC3886 2024) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1673 | Virtual Machine Discovery | [UNC3886](https://attack.mitre.org/groups/G1048) has used scripts to enumerate ESXi hypervisors and their guest VMs.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1675 | ESXi Administration Command | [UNC3886](https://attack.mitre.org/groups/G1048) used `vmtoolsd.exe` to run commands on guest virtual machines from a compromised ESXi host.(Citation: Google Cloud Threat Intelligence ESXi VIBs 2022)(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023)(Citation: Google Cloud Mandiant UNC3886 2024)(Citation: Mandiant Fortinet Zero Day) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1681 | Search Threat Vendor Data | [UNC3886](https://attack.mitre.org/groups/G1048) has replaced indicators mentioned in open-source threat intelligence publications at times under a week after their release.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | [UNC3886](https://attack.mitre.org/groups/G1048) has disabled OpenSSL digital signature verification of system files through corruption of boot files.(Citation: Mandiant Fortinet Zero Day) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1686 | Disable or Modify System Firewall |  [UNC3886](https://attack.mitre.org/groups/G1048) has used the TABLEFLIP traffic redirection utility and the esxcli command line to modify firewall rules.(Citation: Google Cloud Threat Intelligence ESXi VIBs 2022)(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023)(Citation: Mandiant Fortinet Zero Day) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1690 | Prevent Command History Logging | [UNC3886](https://attack.mitre.org/groups/G1048) has tampered with and disabled logging services on targeted systems.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 15件（`artifacts.csv`）

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
| source--daily-2991ab0470fb4a03b3f8 | 中国のサイバー諜報グループがFortinetとVMwareのゼロデイを悪用 | thehackernews.com | 2024-06-20 | https://thehackernews.com/2024/06/chinese-cyber-espionage-group-exploits.html | osint-report | TLP:CLEAR | 中 |
| source--daily-4fd1a9d4d043a65933bd | UNC3886のハッカーがLinuxルートキットを使用してVMware ESXi VMに潜伏 | bleepingcomputer.com | 2024-06-21 | https://www.bleepingcomputer.com/news/security/unc3886-hackers-use-linux-rootkits-to-hide-on-vmware-esxi-vms/ | osint-report | TLP:CLEAR | 中 |
| source--daily-68aa782163620e0cd16f | 中国のサイバースパイ、Juniperルーターにバックドアを仕掛けてステルスアクセスを実現 | bleepingcomputer.com | 2025-03-13 | https://www.bleepingcomputer.com/news/security/chinese-cyberspies-backdoor-juniper-routers-for-stealthy-access/ | osint-report | TLP:CLEAR | 中 |
| source--daily-7033dbe4bb2c2c20106c | 中国関連のUNC3886、サイバースパイ活動でシンガポール通信業界を標的に | thehackernews.com | 2026-02-10 | https://thehackernews.com/2026/02/china-linked-unc3886-targets-singapore.html | osint-report | TLP:CLEAR | 中 |
| source--daily-dd052f5bf8f217c32fc3 | Juniper、2024年半ば以降、中国のサイバースパイがルーターにバックドアを仕掛けた脆弱性を修正 | bleepingcomputer.com | 2025-03-14 | https://www.bleepingcomputer.com/news/security/juniper-patches-bug-that-let-chinese-cyberspies-backdoor-routers-since-mid-2024/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--unc3886--4d93b1915bebe3ac | 2024 security report |  | 2024 | summary/2024/2024-security-report.pdf | report | TLP:CLEAR | 中 |
| source--unc3886--53065b1953b8eeea | rapid7 2024 attack intelligence report |  | 2024 | summary/2024/rapid7_2024_attack_intelligence_report.pdf | report | TLP:CLEAR | 中 |
| source--unc3886--66796923dd140870 | GreyNoise The Invisible Army Residential Proxy Report |  | 不明 | APT-hunting/GreyNoise-The-Invisible-Army-Residential-Proxy-Report.pdf | report | TLP:CLEAR | 中 |
| source--unc3886--802a1983833a7bf2 | Year in Review of ZeroDays |  | 不明 | summary/2024/Year_in_Review_of_ZeroDays.pdf | report | TLP:CLEAR | 中 |
| source--unc3886--a581a629a5547c1a | unc3886 |  | 不明 | actor_profile/evidence/unc3886.csv | structured-data | TLP:CLEAR | 中 |
| source--unc3886--af780f84a52f5356 | m trends 2024 |  | 2024 | summary/2024/m-trends-2024.pdf | report | TLP:CLEAR | 中 |
| source--unc3886--e5512d3a63039b72 | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--unc3886--fb18a320d1b96523 | 2025 Year in Review  Malicious Infrastructure |  | 2025 | summary/2026/2025 Year in Review- Malicious Infrastructure.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
