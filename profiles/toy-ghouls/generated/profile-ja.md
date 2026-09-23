# Toy Ghouls 脅威アクタープロファイル

- プロファイルID: `actor--toy-ghouls`
- 状態: draft
- 更新日時: 2026-09-23T12:16:55Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

Toy Ghouls（Bearlyfy、Labubu、Laboo.boo、Feral Wolf）は、2025年1月以降ロシア企業を標的にするランサムウェア／恐喝クラスタである。2025年にはLockBit、Babuk、PolyVice等と公開ツールを使用し、2026年には独自GenieLocker、mqtt-bird-agent、matrix-bird-agentへ発展した。Head Mareとの共有インフラ・ツールと協力、PhantomCoreとのインフラ重複が報告されるが、同一主体・包含関係を示す証拠はない。

## アクター名とAlias

- 正規名: **Toy Ghouls**
- 初回観測: 2025-01
- 最終観測: 2026-07
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Bearlyfy | Kaspersky / F6 | overlapping | 高 | `source--kaspersky-toy-ghouls-2026-03-12`, `source--f6-bearlyfy-2026-03-25`, `source--kaspersky-genielocker-2026-07-30`, `source--kaspersky-toy-ghouls-bird-backdoors-2026-09-04` | KasperskyとF6がそれぞれToy Ghouls/Bearlyfyを同じ追跡対象として記述する。ただしベンダー間の収集境界まで完全一致すると立証されたわけではないためexactにはしない。 |
| Labubu | F6 / Kaspersky | overlapping | 高 | `source--f6-bearlyfy-2026-03-25`, `source--kaspersky-genielocker-2026-07-30` | F6の「Bearlyfy (aka Labubu)」とKasperskyの別名列挙に基づく。Labuibは採用しない。 |
| Laboo.boo | Kaspersky | overlapping | 高 | `source--kaspersky-toy-ghouls-2026-03-12`, `source--kaspersky-genielocker-2026-07-30`, `source--kaspersky-toy-ghouls-bird-backdoors-2026-09-04` | KasperskyがToy Ghoulsの別名として一貫して列挙する。連絡先ドメインとの同名性だけでなく本文の明示的対応に基づくが、ベンダー内スコープとして保持する。 |
| Feral Wolf | Kaspersky | overlapping | 中 | `source--kaspersky-toy-ghouls-bird-backdoors-2026-09-04` | 2026-09-04のKaspersky記事1本でのみ別名として確認したためmedium。exactへ昇格しない。 |

## 帰属

KasperskyはToy Ghoulsを金銭目的のランサムウェア集団として扱い、F6は恐喝と妨害を組み合わせるサイバー犯罪グループとして記述し、2026-03-25発表ではBearlyfyをpro-Ukrainianと形容する。この行為類型に限ってcriminalを付与し、pro-UkrainianはF6のsource-scopedな政治的整列評価として注記するが、出身国、所在国、国家後援、運営企業はどの一次資料も特定していない。

- 国: 不明
- スポンサー種別: criminal
- 確度: 高
- 証拠: `source--kaspersky-toy-ghouls-2026-03-12`, `source--f6-bearlyfy-2026-03-25`, `source--kaspersky-genielocker-2026-07-30`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| financial-gain | 身代金要求による金銭獲得。F6は要求額と支払率に関する集計を示し、Kasperskyも恐喝を主要目的として記述する。 | 高 | `source--kaspersky-toy-ghouls-2026-03-12`, `source--f6-bearlyfy-2026-03-25`, `source--kaspersky-genielocker-2026-07-30` | 実際の支払率はF6の集計に依存するため、個々の被害事例へ一般化しない。 |
| destruction | F6はToy Ghoulsの活動を恐喝だけでなく企業活動の妨害・サボタージュとの二重目的として評価する。 | 中 | `source--f6-bearlyfy-2026-03-25` | F6単独の評価であり、KasperskyのGenieLocker事例では情報流出や二重恐喝の証拠が確認されていない。 |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| Head Mare | shares-infrastructure-with | Kasperskyは195.133.32.213をToy Ghoulsの一攻撃のC2として観測し、同じIPがHead Mareにも少なくとも2025年8月から使われたと報告した。31.56.27.60とnextcloud.soft-trust.comも、Toy Ghouls環境で実行されたツールの接続先として、Head Mareの既知C2と重なる。 | 中 | `source--kaspersky-toy-ghouls-2026-03-12` |
| Head Mare | shares-tools-with | Toy Ghoulsの被害環境で、Head Mareの既知C2へ接続するMeshAgentおよびRsocx/Socks5Proxyが観測された。また両クラスタで使われたLockBit検体のコード類似が報告された。 | 中 | `source--kaspersky-toy-ghouls-2026-03-12` |
| Head Mare | cooperates-with | F6はBearlyfy/Toy Ghoulsについて、Head Mareのような、より経験豊富なpro-Ukrainianグループとの協力を観測したと報告する。 | 中 | `source--f6-bearlyfy-2026-03-25` |
| PhantomCore | shares-infrastructure-with | F6は2025年のBearlyfy調査でMeshCentralサーバー集合の一部がPhantomCoreの2025年3月攻撃でも使われ、185.158.248.107はBearlyfyの2025年6月攻撃とPhantomCoreの2024年7月攻撃の双方で使われたと報告した。 | 中 | `source--f6-bearlyfy-2025-09-23` |

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
- 調査日時: 2026-09-21T23:43:14Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | 一致なし |  |  |  |  |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Bearlyfy | multiple-name-intersection | 高 | UA | https://therecord.media/ransomware-ukraine-russia-bearlyfy<br>https://www.f6.ru/blog/bearlyfy/ |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
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
| malware--redalert | RedAlert | KasperskyがToy Ghoulsの攻撃で使用を確認し、IOC節に3件のMD5を掲載したランサムウェア。 | 不明 | 不明 | 高 | `source--kaspersky-toy-ghouls-2026-03-12` |
| malware--lockbit-3-black | LockBit 3.0 Black | KasperskyとF6がToy Ghouls/Bearlyfyによる使用を報告した公開・流通ランサムウェア。 | 不明 | 不明 | 高 | `source--kaspersky-toy-ghouls-2026-03-12`, `source--f6-bearlyfy-2026-03-25` |
| malware--babuk | Babuk | Toy Ghoulsが改変版を使用したとF6が報告し、KasperskyがLinux検体のMD5を掲載したランサムウェア。 | 不明 | 不明 | 高 | `source--kaspersky-toy-ghouls-2026-03-12`, `source--f6-bearlyfy-2026-03-25` |
| malware--polyvice | PolyVice | F6は2025年5月以降の一部攻撃でBearlyfyがPolyViceを使用したと報告する。 | 2025-05 | 不明 | 中 | `source--f6-bearlyfy-2026-03-25` |
| malware--genielocker | GenieLocker | Toy Ghoulsが2026年3月から使用した独自ランサムウェア。KasperskyはWindows、Linux、ESXi版を分析し、F6も3月初旬からの使用を独立に報告した。 | 2026-03 | 不明 | 高 | `source--f6-bearlyfy-2026-03-25`, `source--kaspersky-genielocker-2026-07-30` |
| malware--mqtt-bird-agent | mqtt-bird-agent | Toy Ghoulsの独自Rustバックドア。MQTTをC2に使用し、config.tomlの一部をMachineGuid由来鍵のChaCha20-Poly1305で保護する。 | 2026-07 | 不明 | 高 | `source--kaspersky-toy-ghouls-bird-backdoors-2026-09-04` |
| malware--matrix-bird-agent | matrix-bird-agent | Toy Ghoulsの独自Rustバックドア。Matrix/ElementをC2に使い、設定をHKLM\Software\synapse\Config\SealedConfigへ保存する。 | 2026-07 | 不明 | 高 | `source--kaspersky-toy-ghouls-bird-backdoors-2026-09-04` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--meshagent | MeshAgent | Toy Ghouls被害環境で観測され、Head Mareの既知C2へ接続した遠隔管理エージェント。 | 不明 | 不明 | 高 | `source--kaspersky-toy-ghouls-2026-03-12` |
| tool--rsocx-socks5proxy | Rsocx / Socks5Proxy | Toy Ghouls被害環境で観測され、Head Mareの既知C2へ接続したプロキシツール。 | 不明 | 不明 | 高 | `source--kaspersky-toy-ghouls-2026-03-12` |
| tool--toy-ghouls-network-scanners | fscan and Advanced IP Scanner | 侵害環境のネットワーク探索に使用されたスキャンツール群。 | 不明 | 不明 | 高 | `source--kaspersky-toy-ghouls-2026-03-12` |
| tool--localtonet | Localtonet | 侵害環境から外部へトンネルを作成するために使用されたツール。 | 不明 | 不明 | 高 | `source--kaspersky-toy-ghouls-2026-03-12` |
| tool--evil-winrm-winrm-fs | Evil-WinRM and WinRM-fs | Toy Ghoulsがbird-agentをWinRM経由で配布する際に使用したツール群。 | 2026-07 | 不明 | 高 | `source--kaspersky-toy-ghouls-bird-backdoors-2026-09-04` |
| tool--cloudflared | cloudflared | 2025年6月攻撃で外部接続・ネットワーク中継に用いられた公開Cloudflare Tunnelクライアント。 | 2025-02 | 2025-06 | 高 | `source--f6-bearlyfy-2025-09-23` |
| tool--gost | GOST | 2025年6月攻撃で使われた公開ソース由来のプロキシ／トンネル。F6は改変版の利用を報告した。 | 2025-06 | 2025-06 | 高 | `source--f6-bearlyfy-2025-09-23` |
| tool--psmapexec | PsMapExec | 2025年6月攻撃でWindows/Active Directory内の移動に使用されたツール。 | 2025-06 | 2025-06 | 高 | `source--f6-bearlyfy-2025-09-23` |
| tool--modified-shinysocks | Modified ShinySocks | ShinySOCKS v1.3.3の公開コードを基にし、winScHostサービスとして動作するよう改変されたプロキシ。 | 2025-02 | 2025-06 | 高 | `source--f6-bearlyfy-2025-09-23` |

### インフラ

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| infrastructure--toy-ghouls-laboo | Laboo.boo contact infrastructure | support、oil、far、xjiebの各laboo.booメールアドレスを含む攻撃者連絡用インフラ。 | 不明 | 不明 | 高 | `source--kaspersky-toy-ghouls-2026-03-12` |
| infrastructure--toy-ghouls-1cbit | Toy Ghouls 1cbit.dev infrastructure | 1cbit.dev、akselerator.1cbit.dev、nextcloud.1cbit.dev。 | 不明 | 不明 | 高 | `source--kaspersky-toy-ghouls-2026-03-12` |
| infrastructure--toy-ghouls-ransomware-operations | Toy Ghouls ransomware-operation infrastructure | 202.71.14.145、31.57.93.105、217.154.172.41など、KasperskyがToy Ghouls IOCとして列挙した運用インフラ。 | 不明 | 不明 | 高 | `source--kaspersky-toy-ghouls-2026-03-12` |
| infrastructure--toy-ghouls-head-mare-shared | Toy Ghouls / Head Mare shared infrastructure observations | 195.133.32.213、31.56.27.60、nextcloud.soft-trust.comと、そこへ接続したMeshAgent/Rsocxの観測をまとめる。 | 不明 | 不明 | 中 | `source--kaspersky-toy-ghouls-2026-03-12` |
| infrastructure--toy-ghouls-phantomcore-overlap | Bearlyfy / PhantomCore infrastructure-overlap observations | F6がBearlyfyの2025年4月攻撃から得たMeshCentralサーバー集合と、185.158.248.107の明示的なPhantomCore重複をまとめる分析コンテナ。 | 2025-04 | 2025-06 | 中 | `source--f6-bearlyfy-2025-09-23` |
| infrastructure--toy-ghouls-genielocker-c2 | GenieLocker C2 infrastructure | Kaspersky IOC節に掲載された89.125.66.101。 | 2026-03 | 不明 | 高 | `source--kaspersky-genielocker-2026-07-30` |
| infrastructure--toy-ghouls-bird-c2 | Toy Ghouls bird-agent messaging infrastructure | matrix-bird-agentのmeet.element.twと、正規HiveMQブローカーを利用するmqtt-bird-agentの通信構成。 | 2026-07 | 不明 | 高 | `source--kaspersky-toy-ghouls-bird-backdoors-2026-09-04` |

### 配送・ファイル形式

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| delivery--toy-ghouls-1c-external-processing | 1C external processing files | fix.epf、Исправление.epf、ЗагрузкаXML.epfとして観測された1C外部処理ファイル。 | 不明 | 不明 | 高 | `source--kaspersky-toy-ghouls-2026-03-12` |

### 脆弱性

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| vulnerability--cve-2020-1472 | CVE-2020-1472 (Zerologon) | F6は2025年6月のコンサルティング会社攻撃で、脆弱なWindows Serverドメインコントローラーに対するZerologon悪用を報告した。 | 2025-06 | 2025-06 | 高 | `source--f6-bearlyfy-2025-09-23` |

### 運用能力

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| capability--toy-ghouls-cross-platform-encryption | Cross-platform encryption | GenieLockerでWindows、Linux、ESXi環境を暗号化する能力。 | 2026-03 | 不明 | 高 | `source--f6-bearlyfy-2026-03-25`, `source--kaspersky-genielocker-2026-07-30` |
| capability--toy-ghouls-winrm-deployment | WinRM-based backdoor deployment | 有効な認証情報とEvil-WinRM/WinRM-fsを使ってbird-agentを遠隔配布する。 | 2026-07 | 不明 | 高 | `source--kaspersky-toy-ghouls-bird-backdoors-2026-09-04` |
| capability--toy-ghouls-messaging-c2 | Messaging-protocol C2 | MQTTおよびMatrix/Elementのメッセージング基盤をC2として使用する。 | 2026-07 | 不明 | 高 | `source--kaspersky-toy-ghouls-bird-backdoors-2026-09-04` |

## C2・マルウェア ハンティング・ピボット

| ID | 分類 | 型 | 値 | 帰属範囲 | 観測数 | 出典数 | 活動数 | 初回 | 最終 | 継続評価 | 稼働評価 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| hunting-pivot--toy-ghouls-head-mare-shared-ip | infrastructure | ipv4 | 195.133.32.213 | shared | 1 | 1 | 1 | 不明 | 不明 | single-observation | unknown | 中 | `source--kaspersky-toy-ghouls-2026-03-12` |
| hunting-pivot--toy-ghouls-matrix-c2 | infrastructure | domain | meet.element.tw | unknown | 1 | 1 | 1 | 2026-07 | 不明 | single-observation | unknown | 高 | `source--kaspersky-toy-ghouls-bird-backdoors-2026-09-04` |

### 観測根拠

| Pivot | 観測ID | 観測時期 | 数 | 数の根拠 | 活動 | 出典 | 文脈 |
|---|---|---|---|---|---|---|---|
| hunting-pivot--toy-ghouls-head-mare-shared-ip | pivot-observation--toy-ghouls-head-mare-shared-ip-kaspersky | 不明 | 1 | documented-events | activity--toy-ghouls-ransomware-2025-2026 | source--kaspersky-toy-ghouls-2026-03-12 | Toy Ghoulsの一攻撃のC2として観測。Head Mareも少なくとも2025年8月から使用したとKasperskyが記述。 |
| hunting-pivot--toy-ghouls-matrix-c2 | pivot-observation--toy-ghouls-matrix-c2-kaspersky | 2026-07 | 1 | documented-observables | activity--toy-ghouls-bird-backdoors-july-2026 | source--kaspersky-toy-ghouls-bird-backdoors-2026-09-04 | 2026年7月初旬に初観測されたmatrix-bird-agentのIOCとして掲載。 |

### ハントクエリ

| Pivot | 基盤 | クエリ | 目的 | 検証 | 誤検知上の注意 |
|---|---|---|---|---|---|
| hunting-pivot--toy-ghouls-head-mare-shared-ip | shodan | `net:195.133.32.213/32` | 現在のサービス、証明書、近接インフラを確認し、追加観測との時間的近接性を検証する。 | 要 | VPSの再割当、共有ホスティング、第三者による再利用があり得る。IP一致だけでToy GhoulsまたはHead Mareへ帰属しない。 |
| hunting-pivot--toy-ghouls-matrix-c2 | censys | `dns.names: meet.element.tw` | 当該ホストの証明書・DNS履歴と、同時期のMatrixインフラ候補を調査する。 | 要 | Matrixサーバーは複数利用者に共有され得る。ドメインや証明書の一致だけで全利用者・全通信をToy Ghoulsへ帰属しない。 |

### 継続利用チェック

実行済みの受動検索・継続利用チェックなし

`active_status` は明示的なテレメトリまたはスキャン根拠がない限り `unknown` です。出典公開日は観測時刻に転用していません。

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | ツール | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Toy Ghouls ransomware and extortion operations since January 2025 | ransomware-extortion | 2025-01 | 不明 | 2026-03-12 | target--country-russia | malware--redalert, malware--lockbit-3-black, malware--babuk, malware--polyvice | tool--meshagent, tool--rsocx-socks5proxy, tool--toy-ghouls-network-scanners, tool--localtonet, tool--cloudflared, tool--gost, tool--psmapexec, tool--modified-shinysocks | ttp--toy-ghouls-data-encrypted-for-impact, ttp--toy-ghouls-network-service-scanning, ttp--toy-ghouls-proxy, ttp--toy-ghouls-head-mare-shared-proxy-observation, ttp--toy-ghouls-os-credential-dumping | victim--toy-ghouls-russian-organizations-aggregate | 少なくとも2025年1月からロシアの組織を標的とし、LockBit 3 Black、RedAlert、改変Babuk、2025年5月以降の一部ではPolyViceを用いた継続的な恐喝・暗号化活動。F6は2026年3月時点で70件超の攻撃を観測したと報告する。 | 高 | `source--f6-bearlyfy-2025-09-23`, `source--kaspersky-toy-ghouls-2026-03-12`, `source--f6-bearlyfy-2026-03-25` |
| April 2025 Russian oil-company incident | ransomware-incident | 2025-04 | 2025-04 | 2025-09-23 | target--country-russia, target--sector-energy | malware--lockbit-3-black, malware--babuk | tool--meshagent | ttp--toy-ghouls-data-encrypted-for-impact, ttp--toy-ghouls-rdp, ttp--toy-ghouls-windows-admin-shares, ttp--toy-ghouls-powershell |  | ロシアの石油企業に対する2025年4月の単発事例。WindowsをLockBit 3 Black、ハイパーバイザーをBabukで暗号化し、RDP、PowerShell、PsExec/Admin Sharesを使用した。MeshAgent検体からMeshCentralサーバー一覧が得られ、その一部がPhantomCoreでも使われたとF6が報告した。 | 高 | `source--f6-bearlyfy-2025-09-23` |
| June 2025 consulting and engineering attacks | ransomware-activity | 2025-06 | 2025-06 | 2025-09-23 | target--country-russia, target--sector-professional-services, target--sector-engineering | malware--lockbit-3-black, malware--babuk | tool--cloudflared, tool--gost, tool--psmapexec, tool--modified-shinysocks | ttp--toy-ghouls-data-encrypted-for-impact, ttp--toy-ghouls-exploit-public-facing-application, ttp--toy-ghouls-exploitation-remote-services, ttp--toy-ghouls-rdp, ttp--toy-ghouls-winrm, ttp--toy-ghouls-valid-accounts, ttp--toy-ghouls-proxy |  | ロシアのコンサルティング会社とエンジニアリング会社に対する別個の6月攻撃をまとめたGrouping。脆弱なBitrix、Zerologon、WinRM、PsMapExec、Cloudflared、GOST、ShinySocks改変版、RDP、SSHトンネルを利用し、LockBit 3 BlackとBabukで暗号化した。 | 高 | `source--f6-bearlyfy-2025-09-23` |
| July 2025 Russian construction-company incident | ransomware-incident | 2025-07 | 2025-07 | 2025-09-23 | target--country-russia, target--sector-construction |  |  | ttp--toy-ghouls-data-encrypted-for-impact, ttp--toy-ghouls-rdp, ttp--toy-ghouls-windows-admin-shares, ttp--toy-ghouls-scheduled-task, ttp--toy-ghouls-powershell, ttp--toy-ghouls-proxy |  | ロシアの建設会社を暗号化し、8万ユーロを要求した2025年7月の単発事例。RDPセッションのクリップボード、スケジュールタスク、PowerShell/SMBの3方式でランサムウェアを配布・実行し、45.158.169.131:443へのSSHトンネルを構成した。 | 高 | `source--f6-bearlyfy-2025-09-23` |
| GenieLocker campaign from March 2026 | ransomware-extortion | 2026-03 | 不明 | 2026-07-30 | target--country-russia | malware--genielocker |  | ttp--toy-ghouls-data-encrypted-for-impact |  | Toy Ghoulsが2026年3月から独自GenieLockerをWindows、Linux、ESXi環境へ展開した活動。Kasperskyは3月末の一事例を詳細分析した。 | 高 | `source--f6-bearlyfy-2026-03-25`, `source--kaspersky-genielocker-2026-07-30` |
| Toy Ghouls bird-agent malware-analysis grouping | custom-backdoor-deployment | 2026-07 | 不明 | 2026-09-04 | target--country-russia | malware--mqtt-bird-agent, malware--matrix-bird-agent | tool--evil-winrm-winrm-fs | ttp--toy-ghouls-valid-accounts, ttp--toy-ghouls-winrm, ttp--toy-ghouls-windows-service, ttp--toy-ghouls-modify-registry, ttp--toy-ghouls-web-service |  | 2026年7月初旬に初観測されたmqtt-bird-agentとmatrix-bird-agentの配布・永続化・C2挙動をまとめた分析単位。反復する独立キャンペーン波は資料から確定できないためGroupingとした。 | 高 | `source--kaspersky-toy-ghouls-bird-backdoors-2026-09-04` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | ツール | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|---|
| Toy Ghouls ransomware and extortion operations since January 2025 | Toy Ghouls | Babuk, LockBit 3.0 Black, PolyVice, RedAlert | cloudflared, GOST, Localtonet, MeshAgent, Modified ShinySocks, PsMapExec, Rsocx / Socks5Proxy, fscan and Advanced IP Scanner | T1486 Data Encrypted for Impact, T1090 Proxy, T1046 Network Service Discovery, T1003 OS Credential Dumping, T1090 Proxy | Toy Ghouls 1cbit.dev infrastructure, Toy Ghouls / Head Mare shared infrastructure observations, Laboo.boo contact infrastructure, Toy Ghouls ransomware-operation infrastructure | Russia | F6 aggregate of more than 70 Russian-company attacks | 高 |
| April 2025 Russian oil-company incident | Toy Ghouls | Babuk, LockBit 3.0 Black | MeshAgent | T1486 Data Encrypted for Impact, T1059.001 PowerShell, T1021.001 Remote Desktop Protocol, T1021.002 SMB/Windows Admin Shares | Bearlyfy / PhantomCore infrastructure-overlap observations | Russia, Energy (oil) | 情報なし | 高 |
| June 2025 consulting and engineering attacks | Toy Ghouls | Babuk, LockBit 3.0 Black | cloudflared, GOST, Modified ShinySocks, PsMapExec | T1486 Data Encrypted for Impact, T1190 Exploit Public-Facing Application, T1210 Exploitation of Remote Services, T1090 Proxy, T1021.001 Remote Desktop Protocol, T1078 Valid Accounts, T1021.006 Windows Remote Management | Bearlyfy / PhantomCore infrastructure-overlap observations, Toy Ghouls ransomware-operation infrastructure | Russia, Engineering, Professional services (consulting) | 情報なし | 高 |
| July 2025 Russian construction-company incident | Toy Ghouls | 情報なし | 情報なし | T1486 Data Encrypted for Impact, T1059.001 PowerShell, T1090 Proxy, T1021.001 Remote Desktop Protocol, T1053.005 Scheduled Task/Job: Scheduled Task, T1021.002 SMB/Windows Admin Shares | Toy Ghouls ransomware-operation infrastructure | Russia, Construction | 情報なし | 高 |
| GenieLocker campaign from March 2026 | Toy Ghouls | GenieLocker | 情報なし | T1486 Data Encrypted for Impact | GenieLocker C2 infrastructure | Russia | 情報なし | 高 |
| Toy Ghouls bird-agent malware-analysis grouping | Toy Ghouls | matrix-bird-agent, mqtt-bird-agent | Evil-WinRM and WinRM-fs | T1112 Modify Registry, T1078 Valid Accounts, T1102 Web Service, T1543.003 Windows Service, T1021.006 Windows Remote Management | Toy Ghouls bird-agent messaging infrastructure | Russia | 情報なし | 高 |

F6は2025年1月15日のLockBit検体を起点に、2月の追加検体、4月の石油企業、6月のコンサルティング・エンジニアリング企業、7月の建設企業への攻撃を記録した。Kasperskyは2026年3月に詳細なKill ChainとHead Mare重複を報告し、F6は同月までに70件超とGenieLocker移行を報告した。Kasperskyは7月のbird-agent初観測を9月に公表した。

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | Russia | KasperskyとF6がロシアの組織・企業を主要標的として報告する。 | 2025-01 | 2026-07 | 高 | `source--kaspersky-toy-ghouls-2026-03-12`, `source--f6-bearlyfy-2026-03-25`, `source--kaspersky-genielocker-2026-07-30`, `source--kaspersky-toy-ghouls-bird-backdoors-2026-09-04` |
| sectors | Manufacturing | KasperskyがToy Ghoulsの標的業種として列挙。 | 不明 | 不明 | 高 | `source--kaspersky-genielocker-2026-07-30` |
| sectors | Construction | F6が2025年7月のロシア建設会社への攻撃を報告し、KasperskyもToy Ghoulsの標的業種として列挙。 | 2025-07 | 不明 | 高 | `source--f6-bearlyfy-2025-09-23`, `source--kaspersky-genielocker-2026-07-30` |
| sectors | Financial services | KasperskyがToy Ghoulsの標的業種として列挙。 | 不明 | 不明 | 高 | `source--kaspersky-genielocker-2026-07-30` |
| sectors | Retail | KasperskyがToy Ghoulsの標的業種として列挙。 | 不明 | 不明 | 高 | `source--kaspersky-genielocker-2026-07-30` |
| sectors | Technology | KasperskyがToy Ghoulsの標的業種として列挙。 | 不明 | 不明 | 高 | `source--kaspersky-genielocker-2026-07-30` |
| sectors | Energy (oil) | F6が2025年4月のロシア石油企業への攻撃を報告。 | 2025-04 | 2025-04 | 高 | `source--f6-bearlyfy-2025-09-23` |
| sectors | Professional services (consulting) | F6が2025年6月のロシアのコンサルティング会社への攻撃を報告。 | 2025-06 | 2025-06 | 高 | `source--f6-bearlyfy-2025-09-23` |
| sectors | Engineering | F6が2025年6月のロシアのエンジニアリング会社への攻撃を報告。 | 2025-06 | 2025-06 | 高 | `source--f6-bearlyfy-2025-09-23` |

選定ロジック: ロシアの組織を広く標的とし、Kasperskyは製造、建設、金融、流通、小売、IT・通信を含む複数業種を挙げる。公開資料から特定の規模・地域・役職選別は確定できない。標的国・地域は、活動本文と一次資料でレビューした個別主張から収録し、集約OSINTの値はexternal research leadに隔離する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F6 aggregate of more than 70 Russian-company attacks | 非公開 | aggregate | multiple-organizations | reported | target--country-russia | malware--lockbit-3-black, malware--babuk, malware--polyvice | ttp--toy-ghouls-data-encrypted-for-impact | enterprise Windows/Linux/virtualization environments (aggregate; exact assets not enumerated) | encryption: ランサムウェアによる暗号化。<br>financial-loss: 身代金要求と一部被害者による支払。<br>disruption: F6が二重目的の一つとして事業妨害を評価。 | 2025-01 | 不明 | 2026-03-25 | 中 | `source--f6-bearlyfy-2026-03-25` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| impact | T1486 | Data Encrypted for Impact | LockBit、RedAlert、Babuk、PolyVice、GenieLockerを用いてWindows、Linux、ESXiのデータを暗号化した。 |  | activity--toy-ghouls-ransomware-2025-2026, activity--toy-ghouls-april-2025-oil-incident, activity--toy-ghouls-june-2025-attacks, activity--toy-ghouls-july-2025-construction-incident, activity--toy-ghouls-genielocker-march-2026 | 2025-01 | 2026-03 | 高 | `source--f6-bearlyfy-2025-09-23`, `source--kaspersky-toy-ghouls-2026-03-12`, `source--f6-bearlyfy-2026-03-25`, `source--kaspersky-genielocker-2026-07-30` |
| discovery | T1046 | Network Service Discovery | SoftPerfect Network Scanner、fscan、netstat、pingなどで内部ネットワークとサービスを探索した。 |  | activity--toy-ghouls-ransomware-2025-2026 | 不明 | 不明 | 高 | `source--kaspersky-toy-ghouls-2026-03-12` |
| command-and-control | T1090 | Proxy | F6が2025年6月・7月の事例で、逆SSHトンネル、GOST、cloudflared等による通信中継を観測した。 |  | activity--toy-ghouls-ransomware-2025-2026, activity--toy-ghouls-june-2025-attacks, activity--toy-ghouls-july-2025-construction-incident | 2025-06 | 2025-07 | 高 | `source--f6-bearlyfy-2025-09-23` |
| command-and-control | T1090 | Proxy | Kasperskyは、Toy Ghoulsの被害環境で実行されたRsocx/Socks5Proxy等がHead Mareの既知C2へ接続したと報告した。共有ツール・共有インフラの観測であり、所有権、共同運用、同一主体を意味しない。 |  | activity--toy-ghouls-ransomware-2025-2026 | 不明 | 不明 | 中 | `source--kaspersky-toy-ghouls-2026-03-12` |
| credential-access | T1003 | OS Credential Dumping | Mimikatz、ntdsutil等を使った資格情報・ドメイン情報へのアクセスをKasperskyが報告した。 |  | activity--toy-ghouls-ransomware-2025-2026 | 不明 | 不明 | 高 | `source--kaspersky-toy-ghouls-2026-03-12` |
| initial-access, persistence, privilege-escalation, defense-evasion | T1078 | Valid Accounts | 2025年6月攻撃ではローカル管理者・ドメイン管理者のアカウントを用い、2026年7月のbird-agent活動では侵害済みの正規認証情報をWinRM接続に使用した。 |  | activity--toy-ghouls-june-2025-attacks, activity--toy-ghouls-bird-backdoors-july-2026 | 2025-06 | 2026-07 | 高 | `source--f6-bearlyfy-2025-09-23`, `source--kaspersky-toy-ghouls-bird-backdoors-2026-09-04` |
| lateral-movement | T1021.006 | Windows Remote Management | 2025年6月攻撃でWinRMとPsMapExecを内部移動に使用し、2026年7月にはEvil-WinRMとWinRM-fsでbird-agentを遠隔システムへ配置した。 |  | activity--toy-ghouls-june-2025-attacks, activity--toy-ghouls-bird-backdoors-july-2026 | 2025-06 | 2026-07 | 高 | `source--f6-bearlyfy-2025-09-23`, `source--kaspersky-toy-ghouls-bird-backdoors-2026-09-04` |
| persistence, privilege-escalation | T1543.003 | Windows Service | mqtt-bird-agentをcplsupport、matrix-bird-agentをwtasというWindowsサービスとして登録した。 | malware--mqtt-bird-agent, malware--matrix-bird-agent | activity--toy-ghouls-bird-backdoors-july-2026 | 2026-07 | 2026-07 | 高 | `source--kaspersky-toy-ghouls-bird-backdoors-2026-09-04` |
| defense-evasion, persistence | T1112 | Modify Registry | matrix-bird-agentが暗号化設定をHKLM\Software\synapse\Config\SealedConfig、メトリクス間隔をHKLM\Software\SynapseAgent\metrics_intervalへ保存した。 | malware--matrix-bird-agent | activity--toy-ghouls-bird-backdoors-july-2026 | 2026-07 | 2026-07 | 高 | `source--kaspersky-toy-ghouls-bird-backdoors-2026-09-04` |
| command-and-control | T1102 | Web Service | mqtt-bird-agentがHiveMQのMQTTブローカー、matrix-bird-agentがMatrix/ElementをC2として利用した。 | malware--mqtt-bird-agent, malware--matrix-bird-agent | activity--toy-ghouls-bird-backdoors-july-2026 | 2026-07 | 2026-07 | 高 | `source--kaspersky-toy-ghouls-bird-backdoors-2026-09-04` |
| initial-access, lateral-movement | T1021.001 | Remote Desktop Protocol | 4月・6月・7月の攻撃でRDP接続を用い、7月にはRDPクリップボードでランサムウェアを配布した。 |  | activity--toy-ghouls-april-2025-oil-incident, activity--toy-ghouls-june-2025-attacks, activity--toy-ghouls-july-2025-construction-incident | 2025-04 | 2025-07 | 高 | `source--f6-bearlyfy-2025-09-23` |
| lateral-movement | T1021.002 | SMB/Windows Admin Shares | 4月攻撃ではLockBitのAdmin Shares/PsExec自己拡散が有効化され、7月攻撃ではPowerShellからSMB経由で未暗号化システムを暗号化した。 |  | activity--toy-ghouls-april-2025-oil-incident, activity--toy-ghouls-july-2025-construction-incident | 2025-04 | 2025-07 | 高 | `source--f6-bearlyfy-2025-09-23` |
| execution | T1059.001 | PowerShell | 4月攻撃でBabukをPowerShellスクリプトから起動し、7月攻撃ではPowerShellからSMB経由の暗号化を実行した。 |  | activity--toy-ghouls-april-2025-oil-incident, activity--toy-ghouls-july-2025-construction-incident | 2025-04 | 2025-07 | 高 | `source--f6-bearlyfy-2025-09-23` |
| execution, persistence | T1053.005 | Scheduled Task/Job: Scheduled Task | 2025年7月の建設会社攻撃でスケジュールタスクを作成し、ランサムウェアの配布と実行に用いた。 |  | activity--toy-ghouls-july-2025-construction-incident | 2025-07 | 2025-07 | 高 | `source--f6-bearlyfy-2025-09-23` |
| initial-access | T1190 | Exploit Public-Facing Application | 2025年6月のコンサルティング会社攻撃では脆弱なBitrixが初期アクセス経路になった。 |  | activity--toy-ghouls-june-2025-attacks | 2025-06 | 2025-06 | 高 | `source--f6-bearlyfy-2025-09-23` |
| lateral-movement | T1210 | Exploitation of Remote Services | 2025年6月のコンサルティング会社攻撃でZerologonを悪用し、権限昇格と内部移動を行った。 |  | activity--toy-ghouls-june-2025-attacks | 2025-06 | 2025-06 | 高 | `source--f6-bearlyfy-2025-09-23` |

## IOC／artifact概要

- IOC値: 101件
- IOC観測: 104件
- 複数攻撃で観測: 16件
- 要レビュー候補: 0件
- 非IOC artifact観測: 66件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| Toy Ghouls/Bearlyfyは、少なくとも2025年1月から継続して観測され、標的・恐喝目的・ランサムウェア群・インフラ・独自マルウェア開発の時系列が複数の独立一次情報源で整理できるため、draft intrusion-setとして管理する根拠がある。 | 高 | `source--f6-bearlyfy-2025-09-23`, `source--kaspersky-toy-ghouls-2026-03-12`, `source--f6-bearlyfy-2026-03-25`, `source--kaspersky-genielocker-2026-07-30`, `source--kaspersky-toy-ghouls-bird-backdoors-2026-09-04` | KasperskyとF6は独立した観測主体であり、F6 2025はInternet Archive保存版本文・IOC節を直接取得して再現確認した。 |
| Head Mareとのインフラ・ツール重複およびF6が報告する協力は、Toy GhoulsがHead Mareの一部または同一主体であることを立証しない。 | 高 | `source--kaspersky-toy-ghouls-2026-03-12`, `source--f6-bearlyfy-2026-03-25` | Kasperskyの明示的留保とF6の協力評価を別Relationshipに保持した。 |
| PhantomCoreとの関係はインフラ重複に限定され、F6は両者のTTP差からBearlyfyを別個の自律的構造と評価する。 | 高 | `source--f6-bearlyfy-2025-09-23` | shared IOCを同一主体、part-of、協力関係へ昇格しない。 |
| 2026年にはGenieLockerと2種のbird-agentという独自ツールが確認され、公開・流出ツール中心だった2025年から能力開発が進んだ。 | 高 | `source--f6-bearlyfy-2026-03-25`, `source--kaspersky-genielocker-2026-07-30`, `source--kaspersky-toy-ghouls-bird-backdoors-2026-09-04` | GenieLockerはF6とKasperskyが独立に報告し、bird-agentは現時点でKaspersky単独の技術分析。 |

### 情報ギャップ

- Toy Ghouls運営者の実名、国籍、所在、国家または組織的後援は不明。
- F6 2025記事はWayback raw replayと取得本文ハッシュを固定したが、現行一次URLの将来の可用性は保証されない。
- Head Mareとの協力の期間、契約・指揮関係、メンバー重複は不明。
- PhantomCoreと重複したMeshCentral一覧中の個別サーバー対応は、185.158.248.107以外は原文から一意に特定できない。
- IOCの現在の稼働状況、再割当、証明書履歴は受動スキャンで未検証。

### 不確実性

- F6のpro-Ukrainian表現は政治的整列のベンダー評価であり、攻撃者のorigin・国籍・国家後援とは同義ではない。
- 共有ホスティング、公開ツール、正規サービスの一致だけでは関係性や帰属を確定できない。
- Feral WolfはKaspersky 2026-09-04の1資料だけで確認された別名である。
- Kasperskyの2026-07-30事例で情報流出が確認されなかったことは、Toy Ghoulsの全活動で流出がないことを意味しない。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--f6-bearlyfy-2025-09-23 | Bearlyfy: эволюция новой группировки вымогателей и её связь с PhantomCore | F6 Threat Intelligence / F6 Digital Forensics and Malware Analysis Laboratory | 2025-09-23 | https://www.f6.ru/blog/bearlyfy/ | vendor-research | TLP:CLEAR | 高 |
| source--kaspersky-toy-ghouls-2026-03-12 | Вас посетил вымогатель Лабубу: Toy Ghouls шифруют данные российских компаний | Kaspersky Threat Research / Securelist | 2026-03-12 | https://securelist.ru/tr/toy-ghouls/115909/ | vendor-research | TLP:CLEAR | 高 |
| source--f6-bearlyfy-2026-03-25 | Bearlyfy выпустили джинна: F6 проанализировала свежие атаки группы | F6 Digital Forensics Laboratory | 2026-03-25 | https://www.f6.ru/media-center/press-releases/bearlyfy-research/ | vendor-press-release | TLP:CLEAR | 高 |
| source--kaspersky-genielocker-2026-07-30 | New GenieLocker ransomware for Windows, ESXi, and Linux | Kaspersky Securelist | 2026-07-30 | https://securelist.com/genielocker-ransomware-for-windows-linux-and-esxi/120843/ | vendor-research | TLP:CLEAR | 高 |
| source--kaspersky-toy-ghouls-bird-backdoors-2026-09-04 | New backdoors from Toy Ghouls | Kaspersky Securelist | 2026-09-04 | https://securelist.com/toy-ghouls-new-hivemq-and-element-backdoors/121270/ | vendor-research | TLP:CLEAR | 高 |

## 自由記述

継続利用や現在のC2稼働は未検証。Shodan/Censys等の結果は割当履歴と時間的近接性を確認し、IP・証明書・共有サービスの単独一致で帰属しない。
