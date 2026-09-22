# Storm-2603 脅威アクタープロファイル

- プロファイルID: `actor--storm-2603`
- 状態: draft
- 更新日時: 2026-09-21T22:28:38Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

Storm-2603の標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Storm-2603**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

Aliasなし

## 帰属

Microsoft assesses with medium confidence that Storm-2603 is a China-based threat actor and states that it has not identified links to other known Chinese threat actors.

- 国: China
- スポンサー種別: unknown
- 確度: 中
- 証拠: `source--microsoft-toolshell-2025`

## モチベーション

未評価

## 他アクターとの関係

確認された関係なし

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
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Storm-2603 | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | Storm-2603 | canonical-name | 高 | CN | https://www.microsoft.com/en-us/security/blog/2025/07/22/disrupting-active-exploitation-of-on-premises-sharepoint-vulnerabilities/ |
| misp-microsoft-activity-group | Storm-2603 | canonical-name | 高 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
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

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--warlock-ransomware | Warlock ransomware | Ransomware deployed by Storm-2603 after ToolShell exploitation. | 2025-07-18 | 不明 | 高 | `source--microsoft-toolshell-2025` |
| malware--storm-2603-lockbit-ransomware | LockBit ransomware | MicrosoftはStorm-2603が過去にLockBitランサムウェアを展開したと報告するが、対象となる活動・亜種・利用時期は示していない。 | 不明 | 不明 | 高 | `source--microsoft-toolshell-2025` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--storm-2603-mimikatz | Mimikatz | MicrosoftがStorm-2603固有のToolShell侵入チェーンで資格情報取得に使用したと報告した公開セキュリティツール。 | 2025-07-18 | 不明 | 高 | `source--microsoft-toolshell-2025` |
| tool--storm-2603-psexec | PsExec | MicrosoftがStorm-2603固有のToolShell侵入チェーンで横展開に使用したと報告した正規管理ツール。 | 2025-07-18 | 不明 | 高 | `source--microsoft-toolshell-2025` |
| tool--storm-2603-impacket | Impacket | MicrosoftがStorm-2603固有のToolShell後侵入活動で使用を明示した公開Pythonネットワークプロトコル・ツールキット。 | 2025-07-18 | 不明 | 高 | `source--microsoft-toolshell-2025` |
| tool--storm-2603-velociraptor | Velociraptor | Microsoft DARTが2026年の並行侵入事例でStorm-2603側の導入を確認した正規DFIR・endpoint visibilityツール。 | 不明 | 不明 | 高 | `source--microsoft-storm2603-parallel-intrusion-2026` |
| tool--storm-2603-cloudflare-tunnel | Cloudflare Tunnel | Microsoft DARTが2026年の並行侵入事例でStorm-2603側の遠隔アクセス経路として確認した正規トンネリングサービス／クライアント。 | 不明 | 不明 | 高 | `source--microsoft-storm2603-parallel-intrusion-2026` |
| tool--storm-2603-vscode-remote-ssh | Visual Studio Code Remote - SSH | Microsoft DARTが2026年の並行侵入事例でStorm-2603側のSSH経由遠隔アクセスに使用されたと報告した正規開発機能。 | 不明 | 不明 | 高 | `source--microsoft-storm2603-parallel-intrusion-2026` |
| tool--zoho-assist-unattended-agent | Zoho Assist Unattended Agent | 正規のリモート監視・管理ツール。Microsoft DARTの並行侵入事例とCisco Talos IRの別の単一インシデントで、Storm-2603側の遠隔操作手段として展開された。製品ベンダーを攻撃主体と解釈しない。 | 不明 | 不明 | 高 | `source--microsoft-storm2603-parallel-intrusion-2026`, `source--talos-ir-trends-q2-2026` |

### インフラ

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| infrastructure--storm-2603-updatemicfosoft-c2 | Storm-2603 updatemicfosoft C2 infrastructure | MicrosoftがStorm-2603 C2と明示するupdate.updatemicfosoft.comとmsupdate.updatemicfosoft.com。前者は4件のweb-shell SHA256の通信先かつactor-specific hunting queryの対象、後者はIOC表がC2 domainとして独立掲載するFQDNである。 | 不明 | 不明 | 高 | `source--microsoft-toolshell-2025` |
| infrastructure--storm-2603-post-exploitation-c2 | Storm-2603 post-exploitation C2 65.38.121.198 | MicrosoftのIOC表がStorm-2603のpost-exploitation C2と明示する65.38.121.198。 | 不明 | 不明 | 高 | `source--microsoft-toolshell-2025` |

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

## C2・マルウェア ハンティング・ピボット

| ID | 分類 | 型 | 値 | 帰属範囲 | 観測数 | 出典数 | 活動数 | 初回 | 最終 | 継続評価 | 稼働評価 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hunting-pivot--storm-2603-update-c2 | infrastructure | domain | update.updatemicfosoft.com | actor-specific | 1 | 1 | 1 | 不明 | 不明 | single-observation | unknown | 高 | `source--microsoft-toolshell-2025` |
| hunting-pivot--storm-2603-msupdate-c2 | infrastructure | domain | msupdate.updatemicfosoft.com | actor-specific | 1 | 1 | 1 | 不明 | 不明 | single-observation | unknown | 高 | `source--microsoft-toolshell-2025` |
| hunting-pivot--storm-2603-post-exploitation-c2-ip | infrastructure | ipv4 | 65.38.121.198 | actor-specific | 1 | 1 | 1 | 不明 | 不明 | single-observation | unknown | 高 | `source--microsoft-toolshell-2025` |

### 観測根拠

| Pivot | 観測ID | 観測時期 | 数 | 数の根拠 | 活動 | 出典 | 文脈 |
|---|---|---|---|---|---|---|---|
| hunting-pivot--storm-2603-update-c2 | pivot-observation--storm-2603-update-c2-microsoft | 不明 | 1 | documented-observables | activity--storm-2603--toolshell-warlock-2025 | source--microsoft-toolshell-2025 | Microsoftが4件のweb-shellの通信先と独自のhunting queryでupdate.updatemicfosoft.comをStorm-2603 C2と明示する。 |
| hunting-pivot--storm-2603-msupdate-c2 | pivot-observation--storm-2603-msupdate-c2-microsoft | 不明 | 1 | documented-observables | activity--storm-2603--toolshell-warlock-2025 | source--microsoft-toolshell-2025 | MicrosoftのIOC表がmsupdate.updatemicfosoft.comをStorm-2603のC2 domainと明示する。 |
| hunting-pivot--storm-2603-post-exploitation-c2-ip | pivot-observation--storm-2603-post-exploitation-c2-microsoft | 不明 | 1 | documented-observables | activity--storm-2603--toolshell-warlock-2025 | source--microsoft-toolshell-2025 | MicrosoftのIOC表が65.38.121.198をStorm-2603のpost-exploitation C2と明示する。 |

### ハントクエリ

| Pivot | 基盤 | クエリ | 目的 | 検証 | 誤検知上の注意 |
|---|---|---|---|---|---|
| hunting-pivot--storm-2603-update-c2 | censys | `dns.names: update.updatemicfosoft.com` | 当該FQDNに結び付く証明書・サービス・ホストを確認し、既知活動と時間的に近接する追加インフラ候補を抽出する。 | 要 | DNS再登録、sinkhole、共有証明書、後続の無関係な運用があり得る。FQDN一致だけで現在のホストや通信をStorm-2603へ帰属せず、観測時刻・証明書・サービス・追加IOCで裏付ける。 |
| hunting-pivot--storm-2603-msupdate-c2 | censys | `dns.names: msupdate.updatemicfosoft.com` | 当該FQDNに結び付く証明書・サービス・ホストを確認し、既知活動と時間的に近接する追加インフラ候補を抽出する。 | 要 | DNS再登録、sinkhole、共有証明書、後続の無関係な運用があり得る。FQDN一致だけで現在のホストや通信をStorm-2603へ帰属せず、観測時刻・証明書・サービス・追加IOCで裏付ける。 |
| hunting-pivot--storm-2603-post-exploitation-c2-ip | shodan | `net:65.38.121.198/32` | 現在の公開サービス、証明書、ホスト名を確認し、追加観測との時間的近接性を検証する。 | 要 | VPS再割当、共有ホスティング、第三者による再利用があり得る。IP一致だけで現在のサービスや近接IPをStorm-2603へ帰属しない。 |

### 継続利用チェック

実行済みの受動検索・継続利用チェックなし

`active_status` は明示的なテレメトリまたはスキャン根拠がない限り `unknown` です。出典公開日は観測時刻に転用していません。

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | ツール | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Storm-2603と無関係な第2主体が同居した並行侵入事例 | intrusion | 不明 | 不明 | 2026-06-22 |  |  | tool--storm-2603-cloudflare-tunnel, tool--storm-2603-velociraptor, tool--storm-2603-vscode-remote-ssh, tool--zoho-assist-unattended-agent | ttp--storm-2603-parallel-protocol-tunneling, ttp--storm-2603-parallel-remote-access-software, ttp--storm-2603-parallel-ssh |  | Microsoft DARTは、一つの被害環境でStorm-2603と無関係な第2主体が並行して活動した事例を報告した。Storm-2603側はSharePointを探索し、Velociraptor、Cloudflare Tunnel、Zoho Assist、VS Code経由SSHなどを用いて権限・永続性・遠隔アクセスを確保した。別主体のDLLサイドローディングや独自バックドアはStorm-2603の能力として扱わない。 | 高 | `source--microsoft-storm2603-parallel-intrusion-2026` |
| Storm-2603、ToolShell悪用後にWarlockランサムウェアを展開 | ransomware-extortion | 2025-07-18 | 不明 | 2025-07-22 |  | malware--warlock-ransomware | tool--storm-2603-mimikatz, tool--storm-2603-psexec, tool--storm-2603-impacket | ttp--activity-rule--af1214636f4d588f7138, ttp--storm-2603-toolshell-credential-dumping, ttp--storm-2603-toolshell-service-execution, ttp--storm-2603-toolshell-domain-policy, ttp--storm-2603-toolshell-encryption-impact |  | Microsoftは、Storm-2603が2025年7月18日以降、オンプレミスSharePointのToolShell脆弱性を悪用し、MimikatzやPsExecで横展開後、グループポリシーでWarlockランサムウェアを展開したと報告した。同時期にはLinen TyphoonとViolet Typhoonも別個に悪用しており、個別被害組織をStorm-2603へ一括帰属しない。 | 高 | `source--microsoft-toolshell-2025` |
| Storm-2603によるZoho Assist Unattended Agent展開事例 | intrusion | 不明 | 不明 | 2026-07-28 |  |  | tool--zoho-assist-unattended-agent | ttp--storm-2603--zoho-assist-t1219-002 |  | Cisco Talos IRはQ2 2026の1件のインシデントで、Warlock ransomware operators（Storm-2603）が正規RMM製品Zoho AssistのUnattended Agentインストーラーを展開したと報告した。TalosがWarlockへの利用を確認したのは初めてで、ユーザーのアクティブセッションなしに持続的な遠隔操作を試みた。本件では暗号化には至っておらず、四半期全体のランサムウェア統計・標的業種・ATT&CK表をこの個別事例へ転用しない。 | 高 | `source--talos-ir-trends-q2-2026` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | ツール | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|---|
| Storm-2603と無関係な第2主体が同居した並行侵入事例 | Storm-2603 | 情報なし | Cloudflare Tunnel, Velociraptor, Visual Studio Code Remote - SSH, Zoho Assist Unattended Agent | T1572 Protocol Tunneling, T1219 Remote Access Software, T1021.004 Remote Services: SSH | 情報なし | 情報なし | 情報なし | 高 |
| Storm-2603、ToolShell悪用後にWarlockランサムウェアを展開 | Storm-2603 | Warlock ransomware | Impacket, Mimikatz, PsExec | T1190 Exploit Public-Facing Application, T1003.001 OS Credential Dumping: LSASS Memory, T1484.001 Domain or Tenant Policy Modification: Group Policy Modification, T1486 Data Encrypted for Impact, T1569.002 System Services: Service Execution | Storm-2603 post-exploitation C2 65.38.121.198, Storm-2603 updatemicfosoft C2 infrastructure | 情報なし | 情報なし | 高 |
| Storm-2603によるZoho Assist Unattended Agent展開事例 | Storm-2603 | 情報なし | Zoho Assist Unattended Agent | T1219.002 Remote Desktop Software | 情報なし | 情報なし | 情報なし | 高 |



## ターゲット

ターゲット情報なし

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Initial Access | T1190 | Exploit Public-Facing Application | Microsoftは、Storm-2603が2025年7月18日以降にオンプレミスSharePointのToolShell脆弱性（CVE-2025-49706、CVE-2025-49704、CVE-2025-53770）を悪用して初期アクセスを得たと報告した。MicrosoftがStorm-2603へ個別帰属していない被害組織・地域は含めない。 |  | activity--storm-2603--toolshell-warlock-2025 | 2025-07-18 | 不明 | 高 | `source--microsoft-toolshell-2025` |
| Credential Access | T1003.001 | OS Credential Dumping: LSASS Memory | Microsoftは、Storm-2603がToolShell侵入後にMimikatzを使って資格情報を取得したと報告した。 |  | activity--storm-2603--toolshell-warlock-2025 | 2025-07-18 | 不明 | 高 | `source--microsoft-toolshell-2025` |
| Lateral Movement | T1569.002 | System Services: Service Execution | Microsoftは、Storm-2603がToolShell侵入後の横展開にPsExecとImpacketを使用したと報告した。 |  | activity--storm-2603--toolshell-warlock-2025 | 2025-07-18 | 不明 | 高 | `source--microsoft-toolshell-2025` |
| Defense Evasion | T1484.001 | Domain or Tenant Policy Modification: Group Policy Modification | Microsoftは、Storm-2603がグループポリシーを用いてWarlockランサムウェアを組織内へ配布したと報告した。 | malware--warlock-ransomware | activity--storm-2603--toolshell-warlock-2025 | 2025-07-18 | 不明 | 高 | `source--microsoft-toolshell-2025` |
| Impact | T1486 | Data Encrypted for Impact | Microsoftは、Storm-2603がToolShell侵入後にWarlockランサムウェアを展開して暗号化を実行したと報告した。 | malware--warlock-ransomware | activity--storm-2603--toolshell-warlock-2025 | 2025-07-18 | 不明 | 高 | `source--microsoft-toolshell-2025` |
| Command And Control | T1219 | Remote Access Software | Microsoft DARTは、並行侵入事例でStorm-2603側がVelociraptorとZoho Assistを遠隔アクセス・管理に利用したと報告した。 |  | activity--storm-2603--parallel-intrusion-2026 | 不明 | 不明 | 高 | `source--microsoft-storm2603-parallel-intrusion-2026` |
| Command And Control | T1572 | Protocol Tunneling | Microsoft DARTは、並行侵入事例でStorm-2603側がCloudflare Tunnelを遠隔アクセス経路として利用したと報告した。 |  | activity--storm-2603--parallel-intrusion-2026 | 不明 | 不明 | 高 | `source--microsoft-storm2603-parallel-intrusion-2026` |
| Lateral Movement | T1021.004 | Remote Services: SSH | Microsoft DARTは、並行侵入事例でStorm-2603側がVisual Studio Code Remote - SSHを用いてSSH経由の遠隔アクセスを行ったと報告した。 |  | activity--storm-2603--parallel-intrusion-2026 | 不明 | 不明 | 高 | `source--microsoft-storm2603-parallel-intrusion-2026` |
| Command And Control | T1219.002 | Remote Desktop Software | Storm-2603がZoho Assist Unattended Agentのインストーラーを展開し、ユーザーがログオンしていない端末への持続的・秘匿的な遠隔操作を試みた。 |  | activity--storm-2603--zoho-assist-incident-2026 | 不明 | 不明 | 高 | `source--talos-ir-trends-q2-2026` |

## IOC／artifact概要

- IOC値: 19件
- IOC観測: 19件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 1件（`artifacts.csv`）

## 主要判断と不確実性

主要判断なし

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.
- MicrosoftのIOC表はStorm-2603固有Indicatorの個別観測日時と現在の稼働状態を示さないため、IOCのfirst/last_observedとcontinuity.active_statusはunknownのまま維持する。

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--storm-2603--358d7946c0a9352d | storm 2603 |  | 不明 | actor_profile/evidence/storm-2603.csv | structured-data | TLP:CLEAR | 中 |
| source--storm-2603--bba67560ab315d2e | UK NCC Group Cyber Threat Intelligence Report September 2025 |  | 2025 | summary/2025/UK_NCC_Group_Cyber_Threat_Intelligence_Report_September_2025_.pdf | report | TLP:CLEAR | 中 |
| source--talos-ir-trends-q2-2026 | IR Trends Q2 2026: Phishing and weaponized remote management tools drive attack chains | Cisco Talos Incident Response | 2026-07-28 | https://blog.talosintelligence.com/ir-trends-q2-2026/ | vendor-incident-response | TLP:CLEAR | 高 |
| source--microsoft-toolshell-2025 | Disrupting active exploitation of on-premises SharePoint vulnerabilities | Microsoft Threat Intelligence | 2025-07-22 | https://www.microsoft.com/en-us/security/blog/2025/07/22/disrupting-active-exploitation-of-on-premises-sharepoint-vulnerabilities/ | vendor-threat-research | TLP:CLEAR | 高 |
| source--microsoft-storm2603-parallel-intrusion-2026 | One intrusion, two cyberattackers: Uncovering parallel threat activity | Microsoft Defender Experts Cybersecurity Incident Response | 2026-06-22 | https://www.microsoft.com/en-us/security/blog/2026/06/22/one-intrusion-two-cyberattackers-uncovering-parallel-threat-activity/ | vendor-threat-research | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
