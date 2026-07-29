# Salt Typhoon 脅威アクタープロファイル

- プロファイルID: `actor--salt-typhoon`
- 状態: draft
- 更新日時: 2026-07-29T15:38:36Z
- 構造バージョン: 1.1.0

## エグゼクティブサマリー

Salt Typhoonの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Salt Typhoon**
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
| Adversary | [Salt Typhoon](https://attack.mitre.org/groups/G1045) is a People's Republic of China (PRC) state-backed actor that has been active since at least 2019 and responsible for numerous compromises of network infrastructure at major U.S. telecommunication and internet service providers (ISP).(Citation: US Dept. of Treasury Salt Typhoon JAN 2025)(Citation: Cisco Salt Typhoon FEB 2025)<br> |
| Capability | JumbledPath |
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
| etda-threat-group-cards | Salt Typhoon, GhostEmperor | canonical-name | 高 | China | https://securelist.com/ghostemperor-from-proxylogon-to-kernel-mode/104407/<br>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2021/09/30094337/GhostEmperor_technical-details_PDF_eng.pdf<br>https://www.trendmicro.com/en_us/research/24/k/breaking-down-earth-estries-persistent-ttps-in-prolonged-cyber-o.html |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Salt Typhoon | canonical-name | 高 | China | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | GhostEmperor | canonical-name | 高 | CN | https://securelist.com/ghostemperor-from-proxylogon-to-kernel-mode/104407/<br>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2021/09/30094337/GhostEmperor_technical-details_PDF_eng.pdf<br>https://www.welivesecurity.com/2021/09/23/famoussparrow-suspicious-hotel-guest/ |
| misp-microsoft-activity-group | Salt Typhoon | canonical-name | 高 | CN, China | https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | 一致なし |  |  |  |  |
| misp-mitre-intrusion-set | Salt Typhoon - G1045 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G1045<br>https://blog.talosintelligence.com/salt-typhoon-analysis/<br>https://home.treasury.gov/news/press-releases/jy2792 |
| misp-360net | 一致なし |  |  |  |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Earth Estries | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--jumbledpath | JumbledPath | [JumbledPath](https://attack.mitre.org/software/S1206) is a custom-built utility written in GO that has been used by [Salt Typhoon](https://attack.mitre.org/groups/G1045) since at least 2024 for packet capture on remote Cisco devices. [JumbledPath](https://attack.mitre.org/software/S1206) is compiled as an ELF binary using x86-64 architecture which makes it potentially useable across Linux operating systems and network devices from multiple vendors.(Citation: Cisco Salt Typhoon FEB 2025) | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

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
| ワイデン議員、Salt Typhoonハッキング後の米国通信網保護法案を提案 | cyber-espionage | 不明 | 不明 | 2024-12-12 |  |  |  |  | 米国上院議員ロン・ワイデン氏は、中国の国家支援ハッカー「Salt Typhoon」による通信会社への侵入を受け、通信ネットワークのセキュリティ強化を目的とした「Secure American Communications Act」を提案した。 この法案は、連邦通信委員会（FCC）に対し、通信事業者がネットワークの脆弱性を年次でテストし、修正し、独立した監査人による年次監査を受けることを義務付けるサイバーセキュリティ規則の策定を求めている。 ワイデン氏は、FCCが通信会社に自主的なサイバーセキュリティ規則を許可した結果、外国のハッカーが米国の通信システムに深く侵入することになったと指摘している。 同氏は、通信会社と連邦規制当局が職務を怠ったため、米国民の通話、メッセージ、電話記録が外国のスパイによってアクセスされ、国家安全保障が脅かされたと述べている。 ワイデン氏は、議会が行動を起こし、通信システムを再び確実に保護するための強制的なセキュリティ規則を制定する必要があると強調している。 | 高 | `source--daily-109114cb275f6abbc31b` |
| 米国、最近の通信事業者侵害に関与したハッカーを阻止するための対策を共有 | intrusion | 不明 | 不明 | 2024-12-04 | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--97fa6f38a056d42117be, target--mitre-group--country--41795735fc0e57933c4e |  |  | victim--activity-rule--6924067bd37617cf6643 | CISAは、中国の脅威グループ「Salt Typhoon」による通信事業者への攻撃に対抗するためのガイダンスを発表しました。 このグループは、AT&T、T-Mobile、Verizonなどの大手通信事業者のネットワークに侵入し、政府関係者の通信を傍受していました。 攻撃者は、米国政府の盗聴プラットフォームにアクセスし、顧客の通話記録や法執行機関の要求データを盗みました。 侵入期間は数ヶ月以上に及び、大量のインターネットトラフィックが盗まれました。 CISAは、ネットワーク防御者に対し、システムの強化と侵入検知のためのベストプラクティスを推奨しています。 | 中 | `source--daily-8e9e2a4c037c66bd65a0` |
| FBI、通信事業者侵害に関与するSalt Typhoonハッカー特定への協力を呼びかけ | malware-campaign | 2024-12 | 2025-01 | 2025-04-26 | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--97fa6f38a056d42117be, target--mitre-group--country--41795735fc0e57933c4e | malware--jumbledpath |  | victim--activity-rule--d9d35d6d2ce492ffcf3d | FBIはSalt Typhoon（中国支援のAPTグループ）特定のため情報提供を要請。 Salt Typhoonは米国および世界中の通信事業者を侵害し、通信記録や政府関係者の一部私的通信にアクセス。 2024年12月から2025年1月の間に、同グループはCisco IOS XE脆弱性を悪用し、侵入。特注マルウェア「JumbledPath」で監視を実施。 米国は関連企業への制裁やTP-Linkルーター禁止検討など対応を進行中。 国務省は情報提供者に最大1,000万ドルの報奨金を用意。 | 高 | `source--daily-201526278f12b51ceb69` |
| 中国のハッカー、T-Mobileのルーターを侵害しネットワークを探索 | intrusion | 不明 | 不明 | 2024-11-28 | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--97fa6f38a056d42117be |  |  | victim--activity-rule--d9e8ee1880b7b515de18 | 中国の国家支援ハッカー「Salt Typhoon」がT-Mobileのルーターを侵害。 攻撃者はネットワーク内を横断的に移動しようと試みたが、T-Mobileの防御により阻止された。 T-Mobileは、顧客情報へのアクセスや重大な影響は確認されていないと報告。 攻撃は、接続された有線プロバイダーのネットワークから開始された。 Salt Typhoonは、政府機関や通信会社を標的とする中国の国家支援ハッカーグループ。 | 中 | `source--daily-f2e6a61340cf29da66e3` |
| Salt Typhoon、JumbledPathマルウェアを使用して米国の通信ネットワークをスパイ | cyber-espionage | 2024-12 | 2025-01 | 2025-02-21 | target--activity-rule--country--48cc6b4cc2919459aec9, target--mitre-group--country--41795735fc0e57933c4e | malware--jumbledpath |  | victim--activity-rule--0dca98f829c8d2966945 | 中国政府支援のハッキンググループであるSalt Typhoon（別名：Earth Estries、GhostEmperor、UNC2286）は、米国の通信プロバイダーを標的とし、カスタムマルウェア「JumbledPath」を使用してネットワークトラフィックを監視し、機密データを収集しています。 Salt Typhoonは、2019年以降活動しており、主に政府機関や通信会社への侵入を行っています。 最近、米国当局は、Salt TyphoonがVerizon、AT&T、Lumen Technologies、T-Mobileなどの米国の主要通信プロバイダーへの侵入に成功し、一部の政府関係者のプライベートな通信や裁判所認可の盗聴要求に関する情報を盗み取ったと確認しました。 さらに、Recorded FutureのInsikt Groupは、Salt Typhoonが2024年12月から2025年1月の間に、米国、南米、インドを含む1,000台以上のCiscoネットワークデバイスを標的にしたと報告しています。 Cisco Talosは、Salt Typhoonのハッカーが主に盗まれた認証情報を使用して、コアネットワークインフラストラクチャに侵入し、一部のケースでは3年以上にわたり活動していたと明らかにしました。 | 高 | `source--daily-976395d39cbe624f587e` |
| 中国、米国の通信企業9社をハッキング、CharterやWindstreamも被害 | intrusion | 不明 | 不明 | 2025-01-07 | target--mitre-group--country--41795735fc0e57933c4e |  |  | victim--activity-rule--56207b644814f78c79d7 | 中国政府支援のハッカーグループ「Salt Typhoon」が、米国の通信企業9社を標的にサイバー攻撃を実施。 被害企業には、AT&T、Verizon、Lumen、T-Mobile、Charter Communications、Consolidated Communications、Windstreamが含まれる。 ハッカーは、ネットワークに侵入し、テキストメッセージ、ボイスメール、電話の通話内容、法執行機関の盗聴情報などにアクセス。 一部の企業は、ネットワークからハッカーを排除したと報告しているが、完全な排除が確認されていない企業も存在。 米国政府は、通信業界に対してサイバーセキュリティ対策の強化を求める新たな規制を検討中。 米国政府は、これらの通信ハッキングに対応して、 China Telecom の米国における最後の事業を禁止する計画を立てている。 | 中 | `source--daily-6148d7a5b4eb95ec4071` |
| ホワイトハウスが9件目の通信事業者侵害を中国ハッカーに関連付ける | cyber-espionage | 不明 | 不明 | 2024-12-29 | target--activity-rule--sector--210dddb39397dbe50e91 |  |  | victim--activity-rule--74c5dc09345513dc8a05 | ホワイトハウスが中国のハッカー「Salt Typhoon」による米国通信企業の9件目の侵害を確認。 Salt Typhoonは、東南アジアを中心に政府機関や通信企業を狙うサイバー諜報活動グループ。 侵害の詳細調査は継続中で、暗号化メッセージアプリの推奨などの対応策を実施。 バイデン政権が、中国のハッカーの活動をネットワーク内で発見するためのガイダンスを発表した後、この新たな被害者が発見された。 米政府は中国通信企業への規制強化や関連機器の使用禁止を検討。 新たな法案や規制が通信ネットワークのセキュリティ強化を目指す。 | 中 | `source--daily-6489f1d71026c247f5db` |
| FCC、Salt Typhoon攻撃を受けた通信ネットワークの保護を命令 | intrusion | 不明 | 不明 | 2025-01-18 | target--activity-rule--country--95e363d6dfa8c6f2ecbb, target--activity-rule--sector--210dddb39397dbe50e91, target--mitre-group--country--41795735fc0e57933c4e |  |  | victim--activity-rule--e362ce2814fcc88377b7 | FCCは通信企業に対し、サイバー攻撃防御強化を命じた。 FCCは、「通信傍受および違法アクセスからネットワークを保護する」ことを通信会社に義務付ける宣言型裁定を採択。これは、国家レベルの脅威に対応するために、米国の通信会社にサイバーセキュリティの向上を義務付ける重要なステップ。 Salt Typhoonによる攻撃で政府関係者の通信が漏洩した。 AT＆T、Verizon、Lumenは12月30日、Salt Typhoonのハッカーをネットワークから排除したと発表。 これらの侵害を受けて、米国当局は中国電信の米国における最後の事業を禁止する計画。また、現在進行中の調査で、TP-Linkルーターの使用が国家安全保障上のリスクをもたらすことが判明した場合、同ルーターの禁止も検討。 | 高 | `source--daily-ee88cbba9f3a1d88bf3a` |
| 中国のSalt Typhoonハッカーによる大手通信会社Viasatへの侵害 | infrastructure-operation | 2024-12 | 2025-01 | 2025-06-20 | target--activity-rule--sector--97fa6f38a056d42117be, target--mitre-group--country--41795735fc0e57933c4e |  |  | victim--activity-rule--a99e825063733131210c | Viasatは今年初め、自社ネットワークへの不正アクセスを発見し連邦当局と共同で調査を実施。 調査の結果、顧客影響の証拠は見つからず、事案は既に是正済みと報告。 Salt Typhoonは2019年以降、AT&TやVerizonなど複数の米国・世界各国の通信事業者を侵害。 2024年12月～2025年1月に未パッチのCisco IOS XE機器を経由し通信インフラに侵入。 NSAとCISAは、ComcastとDigital RealtyもSalt Typhoonの通信攻撃で潜在的に侵害されたと指摘。 | 高 | `source--daily-8261fb78f465363bd3b1` |
| ホワイトハウス：Salt Typhoon、中国のハッカーが数十か国の通信会社を侵害 | infrastructure-operation | 不明 | 不明 | 2024-12-06 | target--activity-rule--sector--97fa6f38a056d42117be |  |  | victim--activity-rule--0225661c7d4843db8d07 | 中国政府支援のハッカー集団「Salt Typhoon」が、世界中の数十か国の通信会社を侵害した。 米国では、少なくとも8社の通信企業が被害を受け、そのうち4社は以前から知られていた。 攻撃は1～2年前から続いているが、大統領補佐官は「現時点では機密通信への影響は確認されていない」と述べた。 FamousSparrow、Earth Estries、Ghost Emperor、UNC2286としても追跡されているこの国家支援のハッキンググループは、少なくとも2019年から東南アジアの政府機関や通信会社に侵入。 CISAは火曜日、Salt Typhoonの攻撃からシステムを強化するために、通信インフラストラクチャを管理するシステム管理者やエンジニアを支援するためのガイダンスを公開。 米国政府は、被害企業と協力して対策を進めているが、攻撃者の完全な排除は確認されていない。 | 高 | `source--daily-a83c00a6ec644814b818` |
| Salt Typhoonの世界的ハッキング作戦、中国のテック企業に関連付け | malware-campaign | 不明 | 不明 | 2025-08-28 | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--b8d6639a1884e2bacaa4 | malware--jumbledpath |  | victim--activity-rule--0e5d66c1a45d1edd74fe | NSA/NCSCなどがSalt Typhoonを中国の3社と関連付ける共同勧告を公表。 2021年以降、政府・通信・運輸・宿泊・軍などを世界的に侵害し情報窃取。 ゼロデイではなく既知のエッジ機器脆弱性を悪用し、持続的に侵入。 ACL改変、非標準ポートでのSSH、GRE/IPsecトンネルの利用、カスタムマルウェアJumbledPathなどで監視。 早急なパッチ適用・設定強化・管理画面の分離・不要機能無効化を推奨。 | 高 | `source--daily-8a40a46ef3af6ea86c29` |
| テレコム攻撃後、CISAがSignalのような暗号化メッセージングアプリへの移行を推奨 | intrusion | 不明 | 不明 | 2024-12-19 |  |  |  | victim--activity-rule--cf8ba34b214abea3904e | CISAが米国内外での通信事業者攻撃を受け、Signalなどの暗号化メッセージングアプリの利用を推奨。 攻撃者は中国支援のSalt Typhoonで、数か月以上にわたり通信データを侵害。 CISAは、高度な標的型攻撃の対象となる個人は、モバイルデバイスとインターネットサービス間のすべての通信が傍受または改ざんされる危険性があると想定すべきであると述べた。 CISAは、高度に標的化された個人にエンドツーエンド暗号化や強力な多要素認証を提案。 SMS認証の回避、最新ソフトウェア更新、セキュリティキーの利用が推奨。 商用VPNは推奨されず、ハードウェアの更新も必要。 | 中 | `source--daily-8f2935254e84a399c0e6` |
| カナダ、Ciscoの脆弱性を介してSalt Typhoonが通信会社をハッキングしたと発表 | intrusion | 不明 | 不明 | 2025-06-24 |  |  | ttp--activity-rule--8d3aeddf9addc8b9e88f | victim--activity-rule--20f676ee158c1adce59a | カナダサイバーセンターとFBIがSalt Typhoonが通信企業を標的としたと確認。 2025年2月、未パッチのCisco IOS XEのCVE-2023-20198を悪用し管理者権限を取得。 攻撃者は設定ファイルを取得し、GREトンネルでネットワークトラフィックを傍受。 2024年10月の米通信事業者侵害後、カナダで偵察活動が複数組織に検出。 Salt Typhoonは複数国の通信業者に影響を与え、攻撃継続の可能性が高いと警告。 | 高 | `source--daily-5ec4eadaaf818bc23030` |
| 中国のハッカー、未修正のCiscoルーターを通じて米国の通信事業者をさらに侵害 | intrusion | 2024-12 | 2025-01 | 2025-02-16 | target--activity-rule--country--48cc6b4cc2919459aec9, target--activity-rule--country--f9601e2d842c9a05202b, target--activity-rule--sector--97fa6f38a056d42117be, target--mitre-group--country--41795735fc0e57933c4e |  | ttp--activity-rule--17ee1acf5bab0c261445 | victim--activity-rule--7ab2089e0707ef1c4e90 | 中国のハッカーグループ「Salt Typhoon」が、未修正のCisco IOS XEネットワークデバイスの脆弱性を悪用し、米国の通信事業者を含む複数の企業ネットワークに侵入。 攻撃者は、CVE-2023-20198の権限昇格とCVE-2023-20273のWeb UIコマンドインジェクションの脆弱性を利用して、ネットワークデバイスを侵害。 被害を受けた企業には、米国のインターネットサービスプロバイダー、英国の通信事業者の米国拠点、南アフリカの通信事業者、イタリアのISP、タイの大手通信事業者などが含まれる。 Salt Typhoonは、侵害したデバイスを再構成し、GREトンネルを介して自身のサーバーと通信することで、持続的なアクセスを確保。 2024年12月から2025年1月にかけて、Salt Typhoonは1,000台以上のCiscoネットワークデバイスを標的とし、その半数以上が米国、南米、インドに所在。 | 中 | `source--daily-f6737c6dffa112b7b406` |
| AT&TとVerizon、Salt Typhoon侵害後にネットワークの安全性を確認 | cyber-espionage | 不明 | 不明 | 2025-01-03 |  |  |  |  | AT&TとVerizonは、中国のハッカー集団「Salt Typhoon」による大規模なスパイ活動の一環としてネットワークが侵害されたことを確認。 両社は、現在は攻撃者をネットワークから排除し、システムの安全性を確保したと発表。 AT&Tは、特定の外国情報収集を目的とした少数の個人が標的にされたと述べ、顧客データへの影響は限定的であったと報告。 Verizonも、現在はネットワーク内に脅威アクターの活動は検出されておらず、今回のインシデントに関連する活動は封じ込められたと発表。 T-Mobileも同様の侵害を受けたが、サイバー防御により攻撃の拡大を防いだと報告。 米国政府は、中国のハッキングキャンペーンが米国の9つの通信会社に影響を与えた、と述べた。 | 高 | `source--daily-913106da6e5b8618db5e` |
| Salt Typhoonハッカー、通信事業者に新たなGhostSpiderマルウェアを仕掛ける | cyber-espionage | 不明 | 不明 | 2024-11-26 | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--97fa6f38a056d42117be |  |  | victim--activity-rule--9a14e31c78b0dd3fc8f1 | 中国の国家支援ハッカー集団Salt Typhoonが、新たなバックドア「GhostSpider」を通信事業者に対して使用。 GhostSpiderは、暗号化とメモリ内のみの常駐を通じて実現される、高度なステルス性を必要とする長期的なスパイ活動のために設計されたモジュール式のバックドア。 Trend Microは、Salt TyphoonがLinuxバックドア「Masol RAT」、ルートキット「Demodex」、モジュール式バックドア「SnappyBee」も使用していると報告。 Salt Typhoonは2019年から活動し、政府機関や通信企業を主な標的としている。 最近、Verizon、AT&T、Lumen Technologies、T-Mobileなどの米国通信事業者への侵入が確認された。 これらの攻撃により、政府関係者の通信や法的な盗聴要請に関する情報が盗まれた可能性がある。 | 高 | `source--daily-b63b619b8242c38ce6a8` |
| AT&TとVerizonが米国政府の通信傍受プラットフォームを狙った攻撃を受ける | infrastructure-operation | 不明 | 不明 | 2024-10-08 | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--97fa6f38a056d42117be, target--mitre-group--country--41795735fc0e57933c4e |  |  | victim--activity-rule--434c24e35c5186e784ea | Salt Typhoonと呼ばれる中国のハッカー集団がAT&TやVerizon、Lumen Technologiesを含む米国の通信事業者を攻撃。 ハッカーは政府の通信傍受システムにアクセスし、通信データを収集した可能性がある。 この傍受システムは、米国政府が裁判所から承認を得て利用するもの。 攻撃の発生時期は不明だが、数か月にわたりインフラに侵入していた可能性がある。攻撃の影響は現在も評価中。 攻撃の目的は情報収集であると見られている。 攻撃は米国政府と民間のセキュリティ専門家によって調査中。 | 中 | `source--daily-783a5f048c1b5f5d1e87` |
| 中国系ハッカーが米政府関係者の通信を最近の通信会社の侵害で傍受 | intrusion | 不明 | 不明 | 2024-11-15 | target--activity-rule--country--ee55e5e8faa5dd675d7b, target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--97fa6f38a056d42117be, target--mitre-group--country--41795735fc0e57933c4e |  |  | victim--activity-rule--38086efc45abebb614ba | 中国系ハッカーが米国の通信会社を標的にし、政府関係者の通信を傍受 この攻撃で一部の通信会社の顧客情報や法執行機関のデータも盗まれた Salt Typhoon（別名: Earth Estries等）のグループが侵害に関与 攻撃者は数か月以上ネットワークにアクセスし続けていた可能性 カナダでも同様のスキャン攻撃が確認され、複数の政府機関が標的となった | 中 | `source--daily-66a6db2a9826ffe94b34` |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | インド | 活動「Salt Typhoon、JumbledPathマルウェアを使用して米国の通信ネットワークをスパイ」の記述で標的として明示された国・地域。 | 2024-12 | 2025-01 | 中 | `source--daily-976395d39cbe624f587e`, `source--daily-f6737c6dffa112b7b406` |
| countries | 中国 | 活動「FCC、Salt Typhoon攻撃を受けた通信ネットワークの保護を命令」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-ee88cbba9f3a1d88bf3a` |
| countries | カナダ | 活動「中国系ハッカーが米政府関係者の通信を最近の通信会社の侵害で傍受」の記述で標的として明示された国・地域。 | 不明 | 不明 | 中 | `source--daily-66a6db2a9826ffe94b34` |
| countries | 英国 | 活動「中国のハッカー、未修正のCiscoルーターを通じて米国の通信事業者をさらに侵害」の記述で標的として明示された国・地域。 | 2024-12 | 2025-01 | 中 | `source--daily-f6737c6dffa112b7b406` |
| countries | 米国 | [Salt Typhoon](https://attack.mitre.org/groups/G1045) is a People's Republic of China (PRC) state-backed actor that has been active since at least 2019 and responsible for numerous compromises of network infrastructure at major U.S. telecommunication and internet service providers (ISP).(Citation: US Dept. | 2024-12 | 2025-01 | 高 | `source--daily-201526278f12b51ceb69`, `source--daily-6148d7a5b4eb95ec4071`, `source--daily-66a6db2a9826ffe94b34`, `source--daily-783a5f048c1b5f5d1e87`, `source--daily-8261fb78f465363bd3b1`, `source--daily-8e9e2a4c037c66bd65a0`, `source--daily-976395d39cbe624f587e`, `source--daily-ee88cbba9f3a1d88bf3a`, `source--daily-f6737c6dffa112b7b406`, `source--mitre-attack-19-1` |
| sectors | 政府・行政 | 活動「米国、最近の通信事業者侵害に関与したハッカーを阻止するための対策を共有」の記述で標的として明示された産業。 | 2024-12 | 2025-01 | 中 | `source--daily-201526278f12b51ceb69`, `source--daily-6489f1d71026c247f5db`, `source--daily-66a6db2a9826ffe94b34`, `source--daily-783a5f048c1b5f5d1e87`, `source--daily-8a40a46ef3af6ea86c29`, `source--daily-8e9e2a4c037c66bd65a0`, `source--daily-b63b619b8242c38ce6a8`, `source--daily-ee88cbba9f3a1d88bf3a`, `source--daily-f2e6a61340cf29da66e3` |
| sectors | 情報通信 | 活動「米国、最近の通信事業者侵害に関与したハッカーを阻止するための対策を共有」の記述で標的として明示された産業。 | 2024-12 | 2025-01 | 中 | `source--daily-201526278f12b51ceb69`, `source--daily-66a6db2a9826ffe94b34`, `source--daily-783a5f048c1b5f5d1e87`, `source--daily-8261fb78f465363bd3b1`, `source--daily-8e9e2a4c037c66bd65a0`, `source--daily-a83c00a6ec644814b818`, `source--daily-b63b619b8242c38ce6a8`, `source--daily-f2e6a61340cf29da66e3`, `source--daily-f6737c6dffa112b7b406` |
| sectors | 運輸・航空・海運 | 活動「Salt Typhoonの世界的ハッキング作戦、中国のテック企業に関連付け」の記述で標的として明示された産業。 | 不明 | 不明 | 中 | `source--daily-8a40a46ef3af6ea86c29` |

選定ロジック: 未評価

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: ホワイトハウス：Salt Typhoon、中国のハッカーが数十か国の通信会社を侵害 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--97fa6f38a056d42117be |  |  |  |  | 不明 | 不明 | 2024-12-06 | 高 | `source--daily-a83c00a6ec644814b818` |
| 被害事例: Salt Typhoon、JumbledPathマルウェアを使用して米国の通信ネットワークをスパイ | 非公開 | anonymous | unknown | reported | target--activity-rule--country--48cc6b4cc2919459aec9, target--mitre-group--country--41795735fc0e57933c4e | malware--jumbledpath |  |  |  | 2024-12 | 2025-01 | 2025-02-21 | 高 | `source--daily-976395d39cbe624f587e` |
| 被害事例: Salt Typhoonの世界的ハッキング作戦、中国のテック企業に関連付け | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--b8d6639a1884e2bacaa4 | malware--jumbledpath |  |  |  | 不明 | 不明 | 2025-08-28 | 高 | `source--daily-8a40a46ef3af6ea86c29` |
| 被害事例: カナダ、Ciscoの脆弱性を介してSalt Typhoonが通信会社をハッキングしたと発表 | 非公開 | aggregate | multiple-organizations | reported |  |  | ttp--activity-rule--8d3aeddf9addc8b9e88f | モバイル端末 |  | 不明 | 不明 | 2025-06-24 | 高 | `source--daily-5ec4eadaaf818bc23030` |
| 被害事例: 中国系ハッカーが米政府関係者の通信を最近の通信会社の侵害で傍受 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--ee55e5e8faa5dd675d7b, target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--97fa6f38a056d42117be, target--mitre-group--country--41795735fc0e57933c4e |  |  |  | privacy: 中国系ハッカーが米国の通信会社を標的にし、政府関係者の通信を傍受 この攻撃で一部の通信会社の顧客情報や法執行機関のデータも盗まれた Salt Typhoon（別名: Earth Estries等）のグループが侵害に関与 攻撃者は数か月以上ネットワークにアクセスし続けていた可能性 カナダでも同様のスキャン攻撃が確認され、複数の政府機関が標的となった | 不明 | 不明 | 2024-11-15 | 中 | `source--daily-66a6db2a9826ffe94b34` |
| 被害事例: AT&TとVerizonが米国政府の通信傍受プラットフォームを狙った攻撃を受ける | 非公開 | anonymous | unknown | reported | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--97fa6f38a056d42117be, target--mitre-group--country--41795735fc0e57933c4e |  |  |  | espionage: 攻撃の目的は情報収集であると見られている。 | 不明 | 不明 | 2024-10-08 | 中 | `source--daily-783a5f048c1b5f5d1e87` |
| 被害事例: 中国、米国の通信企業9社をハッキング、CharterやWindstreamも被害 | 非公開 | aggregate | multiple-organizations | reported | target--mitre-group--country--41795735fc0e57933c4e |  |  | メール／メールアカウント |  | 不明 | 不明 | 2025-01-07 | 中 | `source--daily-6148d7a5b4eb95ec4071` |
| 被害事例: 米国、最近の通信事業者侵害に関与したハッカーを阻止するための対策を共有 | 非公開 | anonymous | unknown | reported | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--97fa6f38a056d42117be, target--mitre-group--country--41795735fc0e57933c4e |  |  |  |  | 不明 | 不明 | 2024-12-04 | 中 | `source--daily-8e9e2a4c037c66bd65a0` |
| 被害事例: ホワイトハウスが9件目の通信事業者侵害を中国ハッカーに関連付ける | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--210dddb39397dbe50e91 |  |  |  | espionage: Salt Typhoonは、東南アジアを中心に政府機関や通信企業を狙うサイバー諜報活動グループ。 | 不明 | 不明 | 2024-12-29 | 中 | `source--daily-6489f1d71026c247f5db` |
| 被害事例: 中国のハッカー、未修正のCiscoルーターを通じて米国の通信事業者をさらに侵害 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--48cc6b4cc2919459aec9, target--activity-rule--country--f9601e2d842c9a05202b, target--activity-rule--sector--97fa6f38a056d42117be, target--mitre-group--country--41795735fc0e57933c4e |  | ttp--activity-rule--17ee1acf5bab0c261445 | サーバー, ネットワーク機器, モバイル端末 |  | 2024-12 | 2025-01 | 2025-02-16 | 中 | `source--daily-f6737c6dffa112b7b406` |
| 被害事例: Salt Typhoonハッカー、通信事業者に新たなGhostSpiderマルウェアを仕掛ける | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--97fa6f38a056d42117be |  |  |  | espionage: GhostSpiderは、暗号化とメモリ内のみの常駐を通じて実現される、高度なステルス性を必要とする長期的なスパイ活動のために設計されたモジュール式のバックドア。 | 不明 | 不明 | 2024-11-26 | 高 | `source--daily-b63b619b8242c38ce6a8` |
| 被害事例: 中国のSalt Typhoonハッカーによる大手通信会社Viasatへの侵害 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--97fa6f38a056d42117be, target--mitre-group--country--41795735fc0e57933c4e |  |  | モバイル端末 |  | 2024-12 | 2025-01 | 2025-06-20 | 高 | `source--daily-8261fb78f465363bd3b1` |
| 被害事例: テレコム攻撃後、CISAがSignalのような暗号化メッセージングアプリへの移行を推奨 | 非公開 | anonymous | unknown | reported |  |  |  | VPN／リモートアクセス機器 |  | 不明 | 不明 | 2024-12-19 | 中 | `source--daily-8f2935254e84a399c0e6` |
| 被害事例: FBI、通信事業者侵害に関与するSalt Typhoonハッカー特定への協力を呼びかけ | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--97fa6f38a056d42117be, target--mitre-group--country--41795735fc0e57933c4e | malware--jumbledpath |  | ネットワーク機器, モバイル端末 |  | 2024-12 | 2025-01 | 2025-04-26 | 高 | `source--daily-201526278f12b51ceb69` |
| 被害事例: 中国のハッカー、T-Mobileのルーターを侵害しネットワークを探索 | 非公開 | anonymous | unknown | reported | target--activity-rule--sector--210dddb39397dbe50e91, target--activity-rule--sector--97fa6f38a056d42117be |  |  | ネットワーク機器 | privacy: T-Mobileは、顧客情報へのアクセスや重大な影響は確認されていないと報告。 | 不明 | 不明 | 2024-11-28 | 中 | `source--daily-f2e6a61340cf29da66e3` |
| 被害事例: FCC、Salt Typhoon攻撃を受けた通信ネットワークの保護を命令 | 非公開 | aggregate | multiple-organizations | reported | target--activity-rule--country--95e363d6dfa8c6f2ecbb, target--activity-rule--sector--210dddb39397dbe50e91, target--mitre-group--country--41795735fc0e57933c4e |  |  | ネットワーク機器 |  | 不明 | 不明 | 2025-01-18 | 高 | `source--daily-ee88cbba9f3a1d88bf3a` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Initial Access | T1190 | Exploit Public-Facing Application | 中国のハッカー、未修正のCiscoルーターを通じて米国の通信事業者をさらに侵害 中国のハッカーグループ「Salt Typhoon」が、未修正のCisco IOS XEネットワークデバイスの脆弱性を悪用し、米国の通信事業者を含む複数の企業ネットワークに侵入。 |  | activity--daily-cadad398daa03d4d231e | 2024-12 | 2025-01 | 中 | `source--daily-f6737c6dffa112b7b406` |
| Discovery | T1083 | File and Directory Discovery | 攻撃者は設定ファイルを取得し、GREトンネルでネットワークトラフィックを傍受。 |  | activity--daily-b313dc66c03e6d019180 | 不明 | 不明 | 中 | `source--daily-5ec4eadaaf818bc23030` |
| Lateral Movement | T1021.004 | SSH | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has modified the loopback address on compromised switches and used them as the source of SSH connections to additional devices within the target environment, allowing them to bypass access control lists (ACLs).(Citation: Cisco Salt Typhoon FEB 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access, Discovery | T1040 | Network Sniffing | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has used a variety of tools and techniques to capture packet data between network interfaces.(Citation: Cisco Salt Typhoon FEB 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Exfiltration | T1048.003 | Exfiltration Over Unencrypted Non-C2 Protocol | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has exfiltrated configuration files from exploited network devices over FTP and TFTP.(Citation: Cisco Salt Typhoon FEB 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence, Privilege Escalation | T1098.004 | SSH Authorized Keys | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has added SSH authorized_keys under root or other users at the Linux level on compromised network devices.(Citation: Cisco Salt Typhoon FEB 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Credential Access | T1110.002 | Password Cracking | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has cracked passwords for accounts with weak encryption obtained from the configuration files of compromised network devices.(Citation: Cisco Salt Typhoon FEB 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Persistence | T1136 | Create Account | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has created Linux-level users on compromised network devices through modification of `/etc/shadow` and `/etc/passwd`.(Citation: Cisco Salt Typhoon FEB 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Initial Access | T1190 | Exploit Public-Facing Application | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has exploited CVE-2018-0171 in the Smart Install feature of Cisco IOS and Cisco IOS XE software for initial access.(Citation: Cisco Salt Typhoon FEB 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Command And Control | T1572 | Protocol Tunneling | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has modified device configurations to create and use Generic Routing Encapsulation (GRE) tunnels.(Citation: Cisco Salt Typhoon FEB 2025)<br> |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1587.001 | Malware | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has used custom tooling including [JumbledPath](https://attack.mitre.org/software/S1206).(Citation: Cisco Salt Typhoon FEB 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Resource Development | T1588.002 | Tool | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has used publicly available tooling to exploit vulnerabilities.(Citation: Cisco Salt Typhoon FEB 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Reconnaissance | T1590.004 | Network Topology | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has used configuration files from exploited network devices to help discover upstream and downstream network segments.(Citation: Cisco Salt Typhoon FEB 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Collection | T1602.002 | Network Device Configuration Dump | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has attempted to acquire credentials by dumping network device configurations.(Citation: Cisco Salt Typhoon FEB 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1685.006 | Clear Linux or Mac System Logs | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has cleared logs including .bash_history, auth.log, lastlog, wtmp, and btmp.(Citation: Cisco Salt Typhoon FEB 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |
| Defense Impairment | T1686 | Disable or Modify System Firewall | [Salt Typhoon](https://attack.mitre.org/groups/G1045) has made changes to the Access Control List (ACL) and loopback interface address on compromised devices.(Citation: Cisco Salt Typhoon FEB 2025) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-1` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 40件（`artifacts.csv`）

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
| source--daily-109114cb275f6abbc31b | ワイデン議員、Salt Typhoonハッキング後の米国通信網保護法案を提案 | bleepingcomputer.com | 2024-12-12 | https://www.bleepingcomputer.com/news/security/wyden-proposes-bill-to-secure-us-telecoms-after-salt-typhoon-hacks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-201526278f12b51ceb69 | FBI、通信事業者侵害に関与するSalt Typhoonハッカー特定への協力を呼びかけ | bleepingcomputer.com | 2025-04-26 | https://www.bleepingcomputer.com/news/security/fbi-seeks-help-to-unmask-salt-typhoon-hackers-behind-telecom-breaches/ | osint-report | TLP:CLEAR | 中 |
| source--daily-5ec4eadaaf818bc23030 | カナダ、Ciscoの脆弱性を介してSalt Typhoonが通信会社をハッキングしたと発表 | bleepingcomputer.com | 2025-06-24 | https://www.bleepingcomputer.com/news/security/canada-says-salt-typhoon-hacked-telecom-firm-via-cisco-flaw/ | osint-report | TLP:CLEAR | 中 |
| source--daily-6148d7a5b4eb95ec4071 | 中国、米国の通信企業9社をハッキング、CharterやWindstreamも被害 | bleepingcomputer.com | 2025-01-07 | https://www.bleepingcomputer.com/news/security/charter-and-windstream-among-nine-us-telecoms-hacked-by-china/ | osint-report | TLP:CLEAR | 中 |
| source--daily-6489f1d71026c247f5db | ホワイトハウスが9件目の通信事業者侵害を中国ハッカーに関連付ける | bleepingcomputer.com | 2024-12-29 | https://www.bleepingcomputer.com/news/security/white-house-links-ninth-telecom-breach-to-chinese-hackers/ | osint-report | TLP:CLEAR | 中 |
| source--daily-66a6db2a9826ffe94b34 | 中国系ハッカーが米政府関係者の通信を最近の通信会社の侵害で傍受 | bleepingcomputer.com | 2024-11-15 | https://www.bleepingcomputer.com/news/security/chinese-hackers-compromised-us-government-officials-private-communications-in-recent-telecom-breach/ | osint-report | TLP:CLEAR | 中 |
| source--daily-783a5f048c1b5f5d1e87 | AT&TとVerizonが米国政府の通信傍受プラットフォームを狙った攻撃を受ける | bleepingcomputer.com | 2024-10-08 | https://www.bleepingcomputer.com/news/security/atandt-verizon-reportedly-hacked-to-target-us-govt-wiretapping-platform/ | osint-report | TLP:CLEAR | 中 |
| source--daily-8261fb78f465363bd3b1 | 中国のSalt Typhoonハッカーによる大手通信会社Viasatへの侵害 | bleepingcomputer.com | 2025-06-20 | https://www.bleepingcomputer.com/news/security/telecom-giant-viasat-breached-by-chinas-salt-typhoon-hackers/ | osint-report | TLP:CLEAR | 中 |
| source--daily-8a40a46ef3af6ea86c29 | Salt Typhoonの世界的ハッキング作戦、中国のテック企業に関連付け | bleepingcomputer.com | 2025-08-28 | https://www.bleepingcomputer.com/news/security/global-salt-typhoon-hacking-campaigns-linked-to-chinese-tech-firms/ | osint-report | TLP:CLEAR | 中 |
| source--daily-8e9e2a4c037c66bd65a0 | 米国、最近の通信事業者侵害に関与したハッカーを阻止するための対策を共有 | bleepingcomputer.com | 2024-12-04 | https://www.bleepingcomputer.com/news/security/us-shares-tips-to-block-hackers-behind-recent-telecom-breaches/ | osint-report | TLP:CLEAR | 中 |
| source--daily-8f2935254e84a399c0e6 | テレコム攻撃後、CISAがSignalのような暗号化メッセージングアプリへの移行を推奨 | bleepingcomputer.com | 2024-12-19 | https://www.bleepingcomputer.com/news/security/cisa-urges-switch-to-signal-like-encrypted-messaging-apps-after-telecom-hacks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-913106da6e5b8618db5e | AT&TとVerizon、Salt Typhoon侵害後にネットワークの安全性を確認 | bleepingcomputer.com | 2025-01-03 | https://www.bleepingcomputer.com/news/security/atandt-and-verizon-say-networks-secure-after-salt-typhoon-breach/ | osint-report | TLP:CLEAR | 中 |
| source--daily-976395d39cbe624f587e | Salt Typhoon、JumbledPathマルウェアを使用して米国の通信ネットワークをスパイ | bleepingcomputer.com | 2025-02-21 | https://www.bleepingcomputer.com/news/security/salt-typhoon-uses-jumbledpath-malware-to-spy-on-us-telecom-networks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-a83c00a6ec644814b818 | ホワイトハウス：Salt Typhoon、中国のハッカーが数十か国の通信会社を侵害 | bleepingcomputer.com | 2024-12-06 | https://www.bleepingcomputer.com/news/security/white-house-salt-typhoon-hacked-telcos-in-dozens-of-countries/ | osint-report | TLP:CLEAR | 中 |
| source--daily-b63b619b8242c38ce6a8 | Salt Typhoonハッカー、通信事業者に新たなGhostSpiderマルウェアを仕掛ける | bleepingcomputer.com | 2024-11-26 | https://www.bleepingcomputer.com/news/security/salt-typhoon-hackers-backdoor-telcos-with-new-ghostspider-malware/ | osint-report | TLP:CLEAR | 中 |
| source--daily-ee88cbba9f3a1d88bf3a | FCC、Salt Typhoon攻撃を受けた通信ネットワークの保護を命令 | bleepingcomputer.com | 2025-01-18 | https://www.bleepingcomputer.com/news/security/fcc-orders-telecoms-to-secure-their-networks-after-salt-tyhpoon-hacks/ | osint-report | TLP:CLEAR | 中 |
| source--daily-f2e6a61340cf29da66e3 | 中国のハッカー、T-Mobileのルーターを侵害しネットワークを探索 | bleepingcomputer.com | 2024-11-28 | https://www.bleepingcomputer.com/news/security/chinese-hackers-breached-t-mobiles-routers-to-scope-out-network/ | osint-report | TLP:CLEAR | 中 |
| source--daily-f6737c6dffa112b7b406 | 中国のハッカー、未修正のCiscoルーターを通じて米国の通信事業者をさらに侵害 | bleepingcomputer.com | 2025-02-16 | https://www.bleepingcomputer.com/news/security/chinese-hackers-breach-more-us-telecoms-via-unpatched-cisco-routers/ | osint-report | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--salt-typhoon--043cc1597bfd3310 | Threat Report 2026 v4 |  | 2026 | summary/2026/Threat Report 2026 v4.pdf | report | TLP:CLEAR | 中 |
| source--salt-typhoon--26372ea7d0eadd7b | 2025 Cyber Security Report Final |  | 2025 | summary/2025/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--salt-typhoon--2fe372a3244b3e4a | Security Navigator 2026 |  | 2026 | summary/2025/Security_Navigator_2026.pdf | report | TLP:CLEAR | 中 |
| source--salt-typhoon--408477a9e4127f4a | CERTFR 2025 CTI 004 |  | 2025 | summary/2025/CERTFR-2025-CTI-004.pdf | report | TLP:CLEAR | 中 |
| source--salt-typhoon--46dce598612a542a | 2024YiR report |  | 2024 | summary/2025/2024YiR-report.pdf | report | TLP:CLEAR | 中 |
| source--salt-typhoon--508c65a85fce8158 | 2025 dbir data breach investigations report |  | 2025 | summary/2025/2025-dbir-data-breach-investigations-report.pdf | report | TLP:CLEAR | 中 |
| source--salt-typhoon--5558fc5fa569c04a | salt typhoon |  | 不明 | actor_profile/evidence/salt-typhoon.csv | structured-data | TLP:CLEAR | 中 |
| source--salt-typhoon--589c093a1792cfef | CERTFR 2026 CTI 003 |  | 2026 | summary/2026/CERTFR-2026-CTI-003.pdf | report | TLP:CLEAR | 中 |
| source--salt-typhoon--61b8e70c3a5c3350 | [Report] Bitsight State of the Underground 2026 |  | 2026 | summary/2026/[Report] Bitsight State of the Underground 2026.pdf | report | TLP:CLEAR | 中 |
| source--salt-typhoon--64baa41e5fa33f43 | Public Report EN 2025 DIGITAL |  | 2025 | International Strategic/Canada/Public Report_EN_2025_DIGITAL.pdf | report | TLP:CLEAR | 中 |
| source--salt-typhoon--7e2b5bd33dc3894c | annual threat report 2024 |  | 2024 | summary/2025/annual-threat-report-2024.pdf | report | TLP:CLEAR | 中 |
| source--salt-typhoon--962250c413fe62fa | Cloudflare 2026 threat report |  | 2026 | summary/2026/Cloudflare-2026-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--salt-typhoon--a3be3e2289fc2615 | CGCYBER 2024 CTIME |  | 2024 | International Strategic/USA/2025/CGCYBER 2024 CTIME.pdf | report | TLP:CLEAR | 中 |
| source--salt-typhoon--ab1218fd0411268d | TLP CLEAR CERT EU TLR 2024 v1 |  | 2024 | summary/2025/TLP-CLEAR-CERT-EU-TLR-2024-v1.pdf | report | TLP:CLEAR | 中 |
| source--salt-typhoon--c162752e4c56b488 | GreyNoise Ten Days Before Zero Report |  | 不明 | summary/2026/GreyNoise-Ten-Days-Before-Zero-Report.pdf | report | TLP:CLEAR | 中 |
| source--salt-typhoon--c3283a5c45aa3c43 | 2025 Cyber Security Report Final |  | 2025 | summary/2026/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--salt-typhoon--dd333d0437859d3e | CrowdStrike 2025 Threat Hunting Report |  | 2025 | summary/2025/CrowdStrike 2025 Threat Hunting Report.pdf | report | TLP:CLEAR | 中 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
