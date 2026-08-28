# GOFFEE 脅威アクタープロファイル

- プロファイルID: `actor--goffee`
- 状態: draft
- 更新日時: 2026-08-28T15:25:24Z
- 構造バージョン: 1.2.0

## エグゼクティブサマリー

GOFFEE(別名 Paper Werewolf)は、少なくとも2022年初頭からロシア国内の組織を標的とするサイバースパイ目的のAPTグループである。標的型フィッシングを主要な初期侵入手段とし、Mythicフレームワークの非公開改変エージェントを中核に据える。2024年はPowerModulとFlashFileGrabber、USBワームを併用し、2026年第2四半期にはSMB/WebDAV経由のリモートテンプレートインジェクションへ移行、同年3月のキャンペーンではバイナリRATのWarpRATとPowerTaskel v2を配布して100組織超を侵害した。

## アクター名とAlias

- 正規名: **GOFFEE**
- 初回観測: 2022
- 最終観測: 2026-04-01T00:00:00Z
- 活動状態: yes

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| Paper Werewolf | BI.ZONE | exact | 中 | `source--securelist-goffee-warprat-2026-08` | Kaspersky原文が「GOFFEE (также известная как Paper Werewolf)」と同一視している。呼称自体はBI.ZONEのもの。BI.ZONE側の原文はHTTP 403で取得できず、BI.ZONEがGOFFEEと同一視しているかを直接確認できていないため、scopeはexactとしつつconfidenceはmediumに留める。 |

## 帰属

確認した3本の一次資料はいずれも攻撃元の国家、後援組織、実行者の国籍を述べていない。標的がロシアおよびCIS諸国に偏ることから対立側の関与を推測する余地はあるが、資料に記載がないため帰属は未評価とする。

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: `source--securelist-goffee-new-attacks-2025`, `source--securelist-goffee-container-attacks-2026-07`, `source--securelist-goffee-warprat-2026-08`

## モチベーション

| 種別 | 説明 | 確度 | 証拠 | 補足 |
|---|---|---|---|---|
| espionage | 原文が「Основная мотивация группы — кибершпионаж」と明記する。 | 高 | `source--securelist-goffee-warprat-2026-08` |  |
| financial | 原文は、侵害済み環境へ任意のマルウェアを展開できる能力から、恐喝・資金窃取・秘密裏のマイニングといった目的も果たしうると述べる。実際にこれらを実行した観測は記載されていない。 | 低 | `source--securelist-goffee-warprat-2026-08` | 原文は可能性の指摘に留まり、観測された動機ではない。確度をlowとし、実行の裏付けが得られるまで引き上げない。 |

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| HeartlessSoul | suspected-shared-operators | Kasperskyは「Со средней степенью уверенности можно заключить, что за этими двумя группами стоят одни и те же атакующие, однако их инструментарий существенно различается」として、GOFFEEとHeartlessSoulの背後に同一の攻撃者がいると中程度の確度で評価する。ツールセットは大きく異なるとしており、同一クラスタの断定ではない。 | 中 | `source--securelist-goffee-warprat-2026-08` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary | 少なくとも2022年初頭から活動するAPTグループ。Kasperskyが「Киберпреступная APT-группа」と表現するが、国家の後援や実行者の国籍を示す一次資料はない。BI.ZONEはPaper Werewolfとして追跡する。 |
| Capability | Mythicフレームワークの非公開改変エージェント(PowerTaskel、PowerTaskel v2)、PowerShellローダPowerModul、バイナリRAT WarpRAT、データ窃取のFlashFileGrabber、IISモジュールOwowaを運用する。攻撃準備の一部を自動化しており、AIの利用が指摘されている。 |
| Infrastructure | キャンペーンごとにインフラを刷新する。2026年3月のキャンペーンではntp・ssl・time・sync系の語を組み合わせた.onlineドメインを多数運用し、WarpRATとPowerTaskel v2が共通のC2を共有していた。 |
| Victim | ロシア国内の組織が一貫した中心。2026年にベラルーシへ拡大し、CIS諸国と欧州でも事例が確認されている。産業はキャンペーンごとに変動する。 |
| Socio-political | 主動機はサイバースパイ活動。ロシアおよび周辺国の政府機関と基幹産業に関心が偏る。 |

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--powertaskel | PowerTaskel | Mythicフレームワーク用の非公開改変PowerShellエージェント。コマンド実行と偵察に用いる。2026年にはより小型のPowerTaskel v2へ更新された。 | 2024-07 | 2026-03 | 高 | `source--securelist-goffee-new-attacks-2025`, `source--securelist-goffee-container-attacks-2026-07`, `source--securelist-goffee-warprat-2026-08` |
| malware--powertaskel-v2 | PowerTaskel v2 | PowerTaskelの後継となる小型のPowerShell製Mythicエージェント。WarpRATと共通のC2インフラを用いることが確認され、同一グループへの帰属根拠となった。 | 2026-03 | 2026-03 | 高 | `source--securelist-goffee-warprat-2026-08` |
| malware--warprat | WarpRAT | バイナリ型のリモートアクセストロイ。C2ポート、SSL利用、スリープ間隔、buildId、アンチVM等をJSON設定として保持する。キャンペーンごとに多数の検体が作成されている。 | 2026-03 | 2026-03 | 高 | `source--securelist-goffee-warprat-2026-08` |
| malware--powermodul | PowerModul | PowerShell製のダウンローダ/ローダ。二次ペイロードを配信し、USBワーム経由でも拡散する。 | 2024-07 | 2024-12 | 高 | `source--securelist-goffee-new-attacks-2025` |
| malware--flashfilegrabber | FlashFileGrabber | リムーバブルメディア上のファイルを窃取するデータスティーラ。 | 2024-07 | 2024-12 | 高 | `source--securelist-goffee-new-attacks-2025` |
| malware--owowa | Owowa | 認証情報窃取を目的とする悪性IISモジュール。2022〜2023年の活動で使用された。 | 2022 | 2023-12 | 中 | `source--securelist-goffee-new-attacks-2025` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--mythic | Mythic | 公開のペンテスト用C2フレームワーク。GOFFEEは非公開の改変エージェントをWindows版・Linux版ともに運用する。 | 2024-07 | 2026-03 | 高 | `source--securelist-goffee-new-attacks-2025`, `source--securelist-goffee-container-attacks-2026-07`, `source--securelist-goffee-warprat-2026-08` |
| tool--inno-setup | Inno Setup | 正規のインストーラ作成ツール。2026年3月のキャンペーンでは、WarpRATとおとりPDFを同梱するドロッパーの作成に転用された(バージョン6.7.0 Unicode)。 | 2026-03 | 2026-03 | 高 | `source--securelist-goffee-warprat-2026-08` |
| tool--lolbins | certutil / curl / wget / mshta / PowerShell | 環境常設の正規ユーティリティ。ペイロード取得とスクリプト実行に利用する。 | 2026-04-01T00:00:00Z | 2026-04-01T00:00:00Z | 中 | `source--securelist-goffee-container-attacks-2026-07` |

### インフラ

未確認

### 配送・ファイル形式

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| delivery--spearphishing-pdf-link | 悪性リンク入りPDF | Acrobat Reader更新通知を装ったPDFに「更新をインストール」ボタンを配置し、ZIPアーカイブの取得先へ誘導する。 | 2026-03 | 2026-03 | 高 | `source--securelist-goffee-warprat-2026-08` |
| delivery--rar-patched-executable | パッチ済み実行ファイル入りRAR | explorer.exe、xpsrchvw.exe等の正規実行ファイルにシェルコードを埋め込み、RARアーカイブで配布する。 | 2024-07 | 2024-12 | 高 | `source--securelist-goffee-new-attacks-2025` |
| delivery--office-macro | 悪性VBAマクロ入りOffice文書 | RARアーカイブに同梱したOffice文書のVBAマクロから感染連鎖を開始する。 | 2024-07 | 2024-12 | 高 | `source--securelist-goffee-new-attacks-2025` |
| delivery--remote-template-injection | リモートテンプレートインジェクション | SMBおよびWebDAV経由でリモートテンプレートを読み込ませ、マクロを実行する。 | 2026-04-01T00:00:00Z | 2026-04-01T00:00:00Z | 高 | `source--securelist-goffee-container-attacks-2026-07` |

### 脆弱性

未確認

### 運用能力

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| opcap--ai-assisted-preparation | AIを用いた攻撃準備の自動化 | 原文は、グループが攻撃準備において自動化手段を用いており、その一部がAIを基盤とするものだと述べる。 | 2026-03 | 2026-03 | 中 | `source--securelist-goffee-warprat-2026-08` |
| opcap--infrastructure-rotation | キャンペーン単位のインフラ刷新 | 原文は、実質的にキャンペーンごとにインフラを変更すると述べる。 | 2022 | 2026-03 | 高 | `source--securelist-goffee-warprat-2026-08` |

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| リモートテンプレートインジェクションによるロシア・ベラルーシの技術系組織への攻撃 | cyber-espionage | 2026-04-01T00:00:00Z | 2026-04-01T00:00:00Z | 2026-07-29 | target--country--belarus, target--country--russia, target--sector--technology | malware--powertaskel | ttp--activity-rule--0d2f7d98a5d694134f2a, ttp--goffee-t1059-001-powershell, ttp--goffee-t1105-ingress-tool-transfer, ttp--goffee-t1218-005-mshta, ttp--goffee-t1221-template-injection, ttp--goffee-t1566-001-spearphishing-attachment | victim--activity-rule--979270edb5bbdece0fd6 | 2026年第2四半期、GOFFEEの被害は引き続きロシア国内の組織が中心で、この四半期では主に技術セクターの企業が対象となった。原文はまた、それまで標的圏になかったベラルーシへ本格的に攻撃を開始したと述べる。初期侵入はOffice文書の悪性マクロを用い、SMBおよびWebDAV経由のリモートテンプレートインジェクションでテンプレートを取得させる。実行にはmshta.exeを用い、certutil、curl、wget、PowerShellといった環境常設ユーティリティでペイロードを取得する。Mythicエージェントはコンテナ環境を含むWindows版とLinux版の双方が確認されている。 | 高 | `source--securelist-goffee-container-attacks-2026-07` |
| PowerModulとPowerTaskelによるロシア国内組織への標的型フィッシング | cyber-espionage | 2024-07 | 2024-12 | 2025-04-10 | target--country--russia, target--sector--construction, target--sector--energy, target--sector--government, target--sector--media, target--sector--telecommunications | malware--powermodul, malware--powertaskel, malware--flashfilegrabber | ttp--activity-rule--29aaf71e9c80a41431e8, ttp--activity-rule--f83f205a8b5bd0c44eb7, ttp--goffee-t1059-001-powershell, ttp--goffee-t1091-removable-media, ttp--goffee-t1566-001-spearphishing-attachment | victim--activity-rule--3d96ab3e9b4c36cc32c3 | 2024年7月から12月にかけて、GOFFEEはロシア国内の組織に対する標的型フィッシングを継続した。RARアーカイブにシェルコードを埋め込んだパッチ済みのexplorer.exe・xpsrchvw.exeを同梱する方式と、悪性VBAマクロ入りOffice文書を同梱する方式の2系統を用いた。新たな実装としてPowerShell製ローダのPowerModulを投入し、リムーバブルメディアからファイルを窃取するFlashFileGrabberと、PowerModulをUSB経由で拡散するワームを併用した。横展開には自己構成型シェルコードであるバイナリ版Mythicエージェントを用いている。標的はメディア、通信、建設、政府機関、エネルギー企業。 | 高 | `source--securelist-goffee-new-attacks-2025` |
| WarpRATとPowerTaskel v2を配布する2026年3月のフィッシングキャンペーン | cyber-espionage | 2026-03 | 2026-03 | 2026-08-28 | target--country--russia, target--region--cis, target--region--europe, target--sector--government, target--sector--manufacturing | malware--warprat, malware--powertaskel-v2 | ttp--activity-rule--d647d878053fb68bdda0, ttp--goffee-t1059-001-powershell, ttp--goffee-t1566-002-spearphishing-link | victim--activity-rule--245c3bfbf40a31ce330d, victim--goffee-warprat-2026-03-aggregate | 2026年3月、GOFFEEはAcrobat Readerの更新通知を装ったPDFを添付したフィッシングメールを配信した。PDF内の「更新をインストール」ボタンからAdobe_Reader_RU.zipを取得させ、Inno Setup 6.7.0で作成されたドロッパーがWarpRAT本体(adbp.exe)とおとりのPDF文書を展開する。おとり文書は高純度化学製品の需要照会を装ったロシア語の公式文書である。WarpRATはJSON形式の設定でC2ポート443、SSL利用、アンチVMを指定し、軽量な代替ペイロードとしてPowerShell製のPowerTaskel v2が用意されている。両者は共通のC2インフラで結び付けられ、高い確度で同一グループに帰属された。Kasperskyのテレメトリでは、本キャンペーンの被害組織は100を超え、本文では約120組織とされる。標的は機械工学、製造、政府セクターが中心で、ロシア国内に加えCIS諸国で複数、EUで散発的な事例が確認されている。 | 高 | `source--securelist-goffee-warprat-2026-08` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| リモートテンプレートインジェクションによるロシア・ベラルーシの技術系組織への攻撃 | GOFFEE | PowerModul, PowerTaskel, PowerTaskel v2 | T1105 Ingress Tool Transfer, T1059.001 PowerShell, T1105 Ingress Tool Transfer, T1218.005 Mshta, T1221 Template Injection, T1566.001 Spearphishing Attachment | 情報なし | ベラルーシ, ロシア, 技術 | 被害事例: リモートテンプレートインジェクションによるロシア・ベラルーシの技術系組織への攻撃 | 高 |
| PowerModulとPowerTaskelによるロシア国内組織への標的型フィッシング | GOFFEE | FlashFileGrabber, PowerModul, PowerTaskel, PowerTaskel v2 | T1059.005 Visual Basic, T1560.001 Archive via Utility, T1059.001 PowerShell, T1091 Replication Through Removable Media, T1566.001 Spearphishing Attachment | 情報なし | ロシア, 建設, エネルギー, 政府・行政, メディア, 通信 | 被害事例: PowerModulとPowerTaskelによるロシア国内組織への標的型フィッシング | 高 |
| WarpRATとPowerTaskel v2を配布する2026年3月のフィッシングキャンペーン | GOFFEE | PowerModul, PowerTaskel, PowerTaskel v2, WarpRAT | T1566.001 Spearphishing Attachment, T1059.001 PowerShell, T1566.002 Spearphishing Link | 情報なし | ロシア, 独立国家共同体（CIS）, 欧州, 政府・行政, 製造・産業 | 被害事例: WarpRATとPowerTaskel v2を配布する2026年3月のフィッシングキャンペーン, 被害事例: 2026年3月キャンペーンの被害組織(集約) | 高 |

2022〜2023年: 悪性IISモジュールOwowaによる認証情報窃取。2024年7月〜12月: パッチ済み実行ファイルおよびVBAマクロ入りOffice文書をRARで配布し、PowerModulを投入。2026年第2四半期: 標的をベラルーシへ拡大し、技術セクターを中心に攻撃。2026年3月: WarpRATとPowerTaskel v2を配布するキャンペーン(2026-08-28に公開)。

## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | ベラルーシ | 2026年第2四半期の資料が、それまで標的圏になかったベラルーシへ攻撃を開始したと述べる。 | 2026-04-01T00:00:00Z | 2026-04-01T00:00:00Z | 高 | `source--securelist-goffee-container-attacks-2026-07` |
| countries | ロシア | 3本の一次資料すべてが、主たる被害組織をロシア国内の組織と明記する。 | 2022 | 2026-04-01T00:00:00Z | 高 | `source--securelist-goffee-container-attacks-2026-07`, `source--securelist-goffee-new-attacks-2025`, `source--securelist-goffee-warprat-2026-08` |
| regions | 東欧 | ベラルーシ、ロシアで確認された標的・被害事例を東欧として集約した地域表示。 | 不明 | 不明 | 中 | `source--securelist-goffee-container-attacks-2026-07`, `source--securelist-goffee-new-attacks-2025`, `source--securelist-goffee-warprat-2026-08` |
| regions | 欧州 | 2026年3月のキャンペーンで、EU域内において散発的な事例が確認されている。 | 2026-03 | 2026-03 | 低 | `source--securelist-goffee-warprat-2026-08` |
| regions | 独立国家共同体（CIS） | 2026年3月のキャンペーンで、ロシア国外のCIS諸国において複数の被害が確認されている。 | 2026-03 | 2026-03 | 中 | `source--securelist-goffee-warprat-2026-08` |
| sectors | 建設 | 2024年の活動で標的として明示された産業。 | 2024-07 | 2024-12 | 高 | `source--securelist-goffee-new-attacks-2025` |
| sectors | エネルギー | 2024年の活動で標的として明示された産業。 | 2024-07 | 2024-12 | 高 | `source--securelist-goffee-new-attacks-2025` |
| sectors | 政府・行政 | 2024年および2026年3月の活動で標的として明示された。 | 2024-07 | 2026-03 | 高 | `source--securelist-goffee-new-attacks-2025`, `source--securelist-goffee-warprat-2026-08` |
| sectors | 製造・産業 | 2026年3月のキャンペーンで標的として明示された産業。 | 2026-03 | 2026-03 | 高 | `source--securelist-goffee-warprat-2026-08` |
| sectors | メディア | 2024年の活動で標的として明示された産業。 | 2024-07 | 2024-12 | 高 | `source--securelist-goffee-new-attacks-2025` |
| sectors | 技術 | 2026年第2四半期の主たる標的として明示された産業。 | 2026-04-01T00:00:00Z | 2026-04-01T00:00:00Z | 高 | `source--securelist-goffee-container-attacks-2026-07` |
| sectors | 通信 | 2024年の活動で標的として明示された産業。 | 2024-07 | 2024-12 | 高 | `source--securelist-goffee-new-attacks-2025` |

選定ロジック: 少数の標的に絞った計画的な作戦を特徴とし、産業構成はキャンペーンごとに変化する。2024年はメディア・通信・建設・政府・エネルギー、2026年第2四半期は技術セクター、2026年3月は製造・産業・政府が中心であった。 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正、および高確度でアクター照合できた構造化OSINTの被害地理フィールドから収録する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: WarpRATとPowerTaskel v2を配布する2026年3月のフィッシングキャンペーン | 非公開 | aggregate | multiple-organizations | reported | target--country--russia, target--region--cis, target--region--europe, target--sector--government, target--sector--manufacturing | malware--powertaskel-v2, malware--warprat | ttp--activity-rule--d647d878053fb68bdda0, ttp--goffee-t1059-001-powershell, ttp--goffee-t1566-002-spearphishing-link | メール／メールアカウント |  | 2026-03 | 2026-03 | 2026-08-28 | 高 | `source--securelist-goffee-warprat-2026-08` |
| 被害事例: PowerModulとPowerTaskelによるロシア国内組織への標的型フィッシング | 非公開 | aggregate | multiple-organizations | reported | target--country--russia, target--sector--construction, target--sector--energy, target--sector--government, target--sector--media, target--sector--telecommunications | malware--flashfilegrabber, malware--powermodul, malware--powertaskel | ttp--activity-rule--29aaf71e9c80a41431e8, ttp--activity-rule--f83f205a8b5bd0c44eb7, ttp--goffee-t1059-001-powershell, ttp--goffee-t1091-removable-media, ttp--goffee-t1566-001-spearphishing-attachment |  | data-theft: 新たな実装としてPowerShell製ローダのPowerModulを投入し、リムーバブルメディアからファイルを窃取するFlashFileGrabberと、PowerModulをUSB経由で拡散するワームを併用した。 | 2024-07 | 2024-12 | 2025-04-10 | 高 | `source--securelist-goffee-new-attacks-2025` |
| 被害事例: リモートテンプレートインジェクションによるロシア・ベラルーシの技術系組織への攻撃 | 非公開 | aggregate | multiple-organizations | reported | target--country--belarus, target--country--russia, target--sector--technology | malware--powertaskel | ttp--activity-rule--0d2f7d98a5d694134f2a, ttp--goffee-t1059-001-powershell, ttp--goffee-t1105-ingress-tool-transfer, ttp--goffee-t1218-005-mshta, ttp--goffee-t1221-template-injection, ttp--goffee-t1566-001-spearphishing-attachment |  |  | 2026-04-01T00:00:00Z | 2026-04-01T00:00:00Z | 2026-07-29 | 高 | `source--securelist-goffee-container-attacks-2026-07` |
| 被害事例: 2026年3月キャンペーンの被害組織(集約) | 非公開 | aggregate | organization | reported |  |  |  |  | espionage: サイバースパイ活動を目的とした侵害。原文は具体的な被害内容を示していない。 | 2026-03 | 2026-03 | 2026-08-28 | 中 | `source--securelist-goffee-warprat-2026-08` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Command And Control | T1105 | Ingress Tool Transfer | 実行にはmshta.exeを用い、certutil、curl、wget、PowerShellといった環境常設ユーティリティでペイロードを取得する。 |  | activity--goffee-container-attacks-2026-q2 | 2026-04-01T00:00:00Z | 2026-04-01T00:00:00Z | 中 | `source--securelist-goffee-container-attacks-2026-07` |
| Execution | T1059.005 | Visual Basic | RARアーカイブにシェルコードを埋め込んだパッチ済みのexplorer.exe・xpsrchvw.exeを同梱する方式と、悪性VBAマクロ入りOffice文書を同梱する方式の2系統を用いた。 |  | activity--goffee-powermodul-2024 | 2024-07 | 2024-12 | 中 | `source--securelist-goffee-new-attacks-2025` |
| Initial Access | T1566.001 | Spearphishing Attachment | WarpRATとPowerTaskel v2を配布する2026年3月のフィッシングキャンペーン 2026年3月、GOFFEEはAcrobat Readerの更新通知を装ったPDFを添付したフィッシングメールを配信した。 | malware--powertaskel, malware--powertaskel-v2, malware--warprat | activity--goffee-warprat-2026-03 | 2026-03 | 2026-03 | 中 | `source--securelist-goffee-warprat-2026-08` |
| Collection | T1560.001 | Archive via Utility | RARアーカイブにシェルコードを埋め込んだパッチ済みのexplorer.exe・xpsrchvw.exeを同梱する方式と、悪性VBAマクロ入りOffice文書を同梱する方式の2系統を用いた。 |  | activity--goffee-powermodul-2024 | 2024-07 | 2024-12 | 中 | `source--securelist-goffee-new-attacks-2025` |
| execution | T1059.001 | PowerShell | Mythicの非公開改変エージェントPowerTaskelおよびローダPowerModulをPowerShellで実行する。 | malware--powertaskel, malware--powertaskel-v2, malware--powermodul | activity--goffee-powermodul-2024, activity--goffee-container-attacks-2026-q2, activity--goffee-warprat-2026-03 | 2024-07 | 2026-03 | 高 | `source--securelist-goffee-new-attacks-2025`, `source--securelist-goffee-container-attacks-2026-07`, `source--securelist-goffee-warprat-2026-08` |
| lateral-movement | T1091 | Replication Through Removable Media | USBワームによりPowerModulをリムーバブルメディア経由で拡散し、FlashFileGrabberで同メディア上のファイルを窃取する。 | malware--powermodul, malware--flashfilegrabber | activity--goffee-powermodul-2024 | 2024-07 | 2024-12 | 高 | `source--securelist-goffee-new-attacks-2025` |
| command-and-control | T1105 | Ingress Tool Transfer | certutil、curl、wget等の環境常設ユーティリティで追加ペイロードを取得する。 |  | activity--goffee-container-attacks-2026-q2 | 2026-04-01T00:00:00Z | 2026-04-01T00:00:00Z | 高 | `source--securelist-goffee-container-attacks-2026-07` |
| defense-evasion | T1218.005 | Mshta | mshta.exeを用いてスクリプトを実行する。 |  | activity--goffee-container-attacks-2026-q2 | 2026-04-01T00:00:00Z | 2026-04-01T00:00:00Z | 高 | `source--securelist-goffee-container-attacks-2026-07` |
| defense-evasion | T1221 | Template Injection | SMBおよびWebDAV経由でリモートテンプレートを読み込ませ、マクロ実行につなげる。 |  | activity--goffee-container-attacks-2026-q2 | 2026-04-01T00:00:00Z | 2026-04-01T00:00:00Z | 高 | `source--securelist-goffee-container-attacks-2026-07` |
| persistence | T1505.004 | IIS Components | 悪性IISモジュールOwowaを設置し、認証情報を窃取する。 | malware--owowa |  | 2022 | 2023-12 | 中 | `source--securelist-goffee-new-attacks-2025` |
| initial-access | T1566.001 | Spearphishing Attachment | RARアーカイブにシェルコードを埋め込んだパッチ済み実行ファイル、または悪性VBAマクロ入りOffice文書を添付して配信する。 | malware--powermodul, malware--powertaskel | activity--goffee-powermodul-2024, activity--goffee-container-attacks-2026-q2 | 2024-07 | 2026-04-01T00:00:00Z | 高 | `source--securelist-goffee-new-attacks-2025`, `source--securelist-goffee-container-attacks-2026-07` |
| initial-access | T1566.002 | Spearphishing Link | Acrobat Reader更新通知を装ったPDF内のボタンから、ZIPアーカイブの配布URLへ誘導する。 | malware--warprat | activity--goffee-warprat-2026-03 | 2026-03 | 2026-03 | 高 | `source--securelist-goffee-warprat-2026-08` |

## IOC／artifact概要

- IOC値: 53件
- IOC観測: 53件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

## 主要判断と不確実性

| 判断 | 確度 | 証拠 | 補足 |
|---|---|---|---|
| GOFFEEは少なくとも2022年初頭から継続してロシア国内の組織を標的とするサイバースパイ目的のAPTグループであり、2026年時点でも活動を継続している。 | 高 | `source--securelist-goffee-new-attacks-2025`, `source--securelist-goffee-container-attacks-2026-07`, `source--securelist-goffee-warprat-2026-08` | 3本の一次資料が一貫して同じ標的圏と継続性を示す。 |
| 同グループはMythicフレームワークの非公開改変エージェントを中核に据えつつ、キャンペーンごとにツールセットとインフラを更新している。2026年にはPowerTaskelからPowerTaskel v2とバイナリRAT WarpRATへ移行した。 | 高 | `source--securelist-goffee-new-attacks-2025`, `source--securelist-goffee-container-attacks-2026-07`, `source--securelist-goffee-warprat-2026-08` | WarpRATとPowerTaskel v2の同一グループへの帰属は共通C2に基づく。 |
| 標的圏は2026年に拡大しており、ベラルーシが新たに加わったほか、CIS諸国と欧州でも事例が確認されている。 | 中 | `source--securelist-goffee-container-attacks-2026-07`, `source--securelist-goffee-warprat-2026-08` | 欧州の事例は原文が「единичные случаи」と述べるに留まり、国名も件数も示されていない。 |
| GOFFEEとHeartlessSoulの背後に同一の攻撃者がいる可能性がある。 | 中 | `source--securelist-goffee-warprat-2026-08` | Kaspersky自身が中程度の確度と述べ、ツールセットは大きく異なるとしている。同一クラスタとして統合しない。 |

### 情報ギャップ

- 攻撃元の国家、後援組織、実行者の国籍を示す一次資料が確認できていない。
- BI.ZONEのPaper Werewolf報告はHTTP 403で取得できず、BI.ZONE側がGOFFEEと同一視しているかを直接確認できていない。別名の裏付けはKaspersky側の記述のみ。
- 2025-04-10および2026-07-29の資料が公開するIOC(後者はドメイン27件、IPv4 4件、ハッシュ70件超)は本作業では未取込。取り込んだのは2026-08-28資料の47件のみ。
- 2022〜2023年のOwowa使用について、対応するActivityを作成していない。
- 個別の被害組織名は3本の資料いずれも公表しておらず、被害事例は集約値のみ。

### 不確実性

- Paper WerewolfとGOFFEEのクラスタ境界。Kasperskyは同一視するが、BI.ZONE側の定義範囲を一次資料で確認できていない。
- HeartlessSoulとの運用主体の同一性。Kasperskyは中程度の確度と明示している。
- 資金窃取・恐喝・マイニングといった動機は原文が可能性として述べるに留まり、実行された観測はない。

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--securelist-goffee-new-attacks-2025 | Goffee’s recent attacks: new tools and techniques | Kaspersky (Securelist / GReAT) | 2025-04-10 | https://securelist.com/goffee-apt-new-attacks/116139/ | vendor-research-report | TLP:CLEAR | 高 |
| source--securelist-goffee-container-attacks-2026-07 | GOFFEE расширяет свои TTP и осваивает контейнеры | Kaspersky (Securelist / GReAT) | 2026-07-29 | https://securelist.ru/tr/goffee-new-ttps-and-container-attacks/116431/ | vendor-research-report | TLP:CLEAR | 高 |
| source--securelist-goffee-warprat-2026-08 | APT-группа GOFFEE продолжает атаки на организации в РФ, распространяя два бэкдора через целевой фишинг | Kaspersky (Securelist / GReAT) | 2026-08-28 | https://securelist.ru/tr/goffee-apt-attacks-with-mythic-agent-and-warprat/116796/ | vendor-research-report | TLP:CLEAR | 高 |

## 自由記述

本プロファイルは2026-08-28の日次チェックで、securelist.ruのみに掲載された新規報告を契機に作成した。定期確認の情報源にsecurelist.ruが含まれていなかったため検知が遅れる構造的な取りこぼしがあり、ROUTINE.mdの8情報源との差異として記録している。
