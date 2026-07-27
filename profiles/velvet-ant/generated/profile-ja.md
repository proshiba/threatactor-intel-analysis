# Velvet Ant 脅威アクタープロファイル

- プロファイルID: `actor--velvet-ant`
- 状態: draft
- 更新日時: 2026-07-27T11:04:39Z
- 構造バージョン: 1.0.0

## エグゼクティブサマリー

Velvet Antの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Velvet Ant**
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
| Adversary | [Velvet Ant](https://attack.mitre.org/groups/G1047) is a threat actor operating since at least 2021. [Velvet Ant](https://attack.mitre.org/groups/G1047) is associated with complex persistence mechanisms, the targeting of network devices and appliances during operations, and the use of zero day exploits.(Citation: Sygnia VelvetAnt 2024A)(Citation: Sygnia VelvetAnt 2024B) |
| Capability | PlugX, Impacket |
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
| etda-threat-group-cards | Velvet Ant | canonical-name | 高 | China | https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Velvet+Ant&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | 一致なし |  |  |  |  |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Velvet Ant - G1047 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1047<br>https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/<br>https://www.sygnia.co/threat-reports-and-advisories/china-nexus-threat-group-velvet-ant-exploits-cisco-0-day/ |
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
| malware--plugx | PlugX | [PlugX](https://attack.mitre.org/software/S0013) is a remote access tool (RAT) with modular plugins that has been used by multiple threat groups.(Citation: Lastline PlugX Analysis)(Citation: FireEye Clandestine Fox Part 2)(Citation: New DragonOK)(Citation: Dell TG-3390) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--impacket | Impacket | [Impacket](https://attack.mitre.org/software/S0357) is an open source collection of modules written in Python for programmatically constructing and manipulating network protocols. [Impacket](https://attack.mitre.org/software/S0357) contains several tools for remote service execution, Kerberos manipulation, Windows credential dumping, packet sniffing, and relay attacks.(Citation: Impacket Tools) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| Velvet Antの「Operation Highland」：中国関連アクターが内部ネットワークへ侵入し検知されず潜伏 | infrastructure-operation | 不明 | 不明 | 2026-06-16 | Sygniaは、中国関連脅威アクターVelvet Antによる「Operation Highland」の侵害調査を公開した。 最古のフォレンジック痕跡は2016年で、攻撃者はインターネット接続のない内部ネットワークに約10年潜伏していた。 攻撃者は外部公開サーバーからITネットワークを経由し、分離された重要インフラ環境へ多段階で到達した。 GS-Netcat、SOCKS5プロキシ、Nginx/FastCGI悪用に加え、PAMとOpenSSHを改ざんして認証基盤自体をバックドア化した。 改ざんされたpam_unix.soやssh/sshd/scpにより、認証回避、認証情報窃取、キーロギング、永続化が実現されていた。 | 高 | `source--daily-2458b73767c4166d02ee` |
| ハッカーがF5 BIG-IPマルウェアを使用して数年間データを密かに盗み続ける | malware-campaign | 不明 | 不明 | 2024-06-18 | 中国の「Velvet Ant」グループがF5 BIG-IPデバイスを侵害。 数年間にわたり顧客や財務データを盗み続けた。 PlugX、PMCD、MCDP、SAMRID、ESRDEなどのマルウェアを使用。大規模な駆除活動を行った後も、新たな構成のPlugXを再展開してきた。 アウトバウンド接続の制限と管理ポートの制御などが推奨される。 エッジ ネットワーク デバイスは、一般的にセキュリティソリューションをサポートしておらず、インターネット公開されるため、人気の攻撃ターゲットになっている。 | 中 | `source--daily-358b578d3773fff3ba70` |
| 中国のハッカー、Ciscoスイッチのゼロデイ脆弱性を悪用してシステムを制御 | malware-campaign | 不明 | 不明 | 2024-08-23 | 中国のハッカーグループ「Velvet Ant」がCiscoスイッチのゼロデイ脆弱性（CVE-2024-20399）を悪用し、システムを制御 この脆弱性は、攻撃者が管理者権限でスイッチの管理コンソールにアクセスすることで、NX-OS CLIをバイパスし、Linux OS上で任意のコマンドを実行できる この攻撃により、データの窃取と持続的なアクセスが可能となる この脆弱性を悪用して「VELVETSHELL」マルウェアが展開された。このマルウェアはTiny SHellと呼ばれるUnixバックドアと3proxyと呼ばれるプロキシユーティリティを組み合わせたもの Ciscoはこの脆弱性を修正済み | 中 | `source--daily-fde72f5ea92c79372580` |
| Cisco、NX-OSのゼロデイ脆弱性がカスタムマルウェアの展開に悪用されたと警告 | malware-campaign | 不明 | 不明 | 2024-07-02 | CiscoはNX-OSのゼロデイ脆弱性（CVE-2024-20399）に対する修正をリリース。 攻撃者は中国の国家支援ハッカー「Velvet Ant」とされ、カスタムマルウェアを展開。 影響を受けるのは複数のNexusおよびMDSスイッチ。 管理者権限を持つ攻撃者が、デバイスのOS上でルート権限での任意コマンドが実行可能。 Ciscoはnetwork-adminおよびvdc-admin管理ユーザーの資格情報を定期的に変更することを推奨。 | 中 | `source--daily-5d965e40acbf5f57fde8` |



## ターゲット

ターゲット情報なし

選定ロジック: 未評価

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Lateral Movement | T1021.002 | SMB/Windows Admin Shares | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1037.004 | RC Scripts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access, Discovery | T1040 | Network Sniffing | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1047 | Windows Management Instrumentation | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1049 | System Network Connections Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Privilege Escalation, Stealth | T1055 | Process Injection | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1059.004 | Unix Shell | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1071 | Application Layer Protocol | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.003 | Local Accounts | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Discovery | T1083 | File and Directory Discovery | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1090.001 | Internal Proxy | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1132 | Data Encoding | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access, Persistence | T1133 | External Remote Services | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Stealth | T1211 | Exploitation for Stealth | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution | T1569.002 | Service Execution | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Lateral Movement | T1570 | Lateral Tool Transfer | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1571 | Non-Standard Port | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1573.002 | Asymmetric Cryptography | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Execution, Stealth | T1574.001 | DLL | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685 | Disable or Modify Tools | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1686 | Disable or Modify System Firewall | MITRE ATT&CK maps this technique to the actor. |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 3件（`artifacts.csv`）

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
| source--daily-2458b73767c4166d02ee | Velvet Antの「Operation Highland」：中国関連アクターが内部ネットワークへ侵入し検知されず潜伏 | sygnia.co | 2026-06-16 | https://www.sygnia.co/blog/operation-highland-velvet-ant/ | osint-report | TLP:CLEAR | 中 |
| source--daily-358b578d3773fff3ba70 | ハッカーがF5 BIG-IPマルウェアを使用して数年間データを密かに盗み続ける | bleepingcomputer.com | 2024-06-18 | https://www.bleepingcomputer.com/news/security/hackers-use-f5-big-ip-malware-to-stealthily-steal-data-for-years/ | osint-report | TLP:CLEAR | 中 |
| source--daily-5d965e40acbf5f57fde8 | Cisco、NX-OSのゼロデイ脆弱性がカスタムマルウェアの展開に悪用されたと警告 | bleepingcomputer.com | 2024-07-02 | https://www.bleepingcomputer.com/news/security/cisco-warns-of-nx-os-zero-day-exploited-to-deploy-custom-malware/ | osint-report | TLP:CLEAR | 中 |
| source--daily-fde72f5ea92c79372580 | 中国のハッカー、Ciscoスイッチのゼロデイ脆弱性を悪用してシステムを制御 | thehackernews.com | 2024-08-23 | https://thehackernews.com/2024/08/chinese-hackers-exploit-zero-day-cisco.html | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--velvet-ant--267d6aacf05086f7 | velvet ant |  | 不明 | actor_profile/evidence/velvet-ant.csv | structured-data | TLP:CLEAR | 中 |
| source--velvet-ant--70ada71300af89ab | 2025 dbir data breach investigations report |  | 2025 | summary/2025/2025-dbir-data-breach-investigations-report.pdf | report | TLP:CLEAR | 中 |
| source--velvet-ant--89cef32c633ba5db | TLP CLEAR CERT EU TLR 2024 v1 |  | 2024 | summary/2025/TLP-CLEAR-CERT-EU-TLR-2024-v1.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
