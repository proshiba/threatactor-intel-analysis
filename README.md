# Threat Actor Intelligence Profiles

脅威アクターに関する公開レポートと固定OSINTデータセットを基に、アクター別の情報を
同一スキーマで整理したデータセットです。人間が読む日本語プロファイルに加え、
機械処理用JSON、STIX 2.1、IOC、非IOC artifact、主張単位の裏取り結果を収録しています。

> [!IMPORTANT]
> 本リポジトリには元のPDF・XLSXなどの原典レポートやマルウェア検体は含まれません。
> プロファイル内の帰属、関係性、IOCなどには未確定・候補情報も含まれるため、
> `confidence`、`assessment`、`claim-audit.json`、出典情報を確認して利用してください。

## 収録内容

| 項目 | 件数 |
|---|---:|
| アクター／脅威クラスター | 673 |
| 処理資料 | 941 |
| 別名 | 922 |
| マルウェア／ツール | 1,832 |
| TTP | 5,327 |
| IOC | 12,962 |
| IOC観測イベント | 15,159 |
| 非IOCアーティファクト観測 | 17,401 |
| 検証エラー | 0 |

全アクターの一覧とアクター別件数は
[プロファイル索引](profiles/README.md)を参照してください。

## 各プロファイルの構成

```text
profiles/<actor-slug>/
├── actor-profile.json          # 正規データ（Single Source of Truth）
├── claim-audit.json            # 主張ごとの支持・反証・未解決状態
├── osint-crosscheck.json       # 固定OSINTデータセットとの照合結果
├── ioc-sources.json            # IOC取込元と既定メタデータ
├── iocs.json                   # 正規化IOCと全観測イベント
├── artifacts.csv               # コマンド、文字列、パス等の非IOC情報
└── generated/
    ├── profile-ja.md           # 人間向け日本語プロファイル
    └── profile.stix2.json      # STIX 2.1 Bundle
```

`actor-profile.json`には、名称とalias、帰属、モチベーション、他アクターとの関係、
Diamond Model、能力、マルウェア、インフラ、MITRE ATT&CK TTP、活動履歴、
標的国・産業、出典、分析上の留保を保存しています。構造化しきれない重要情報は
`free_text`または`analyst_notes`に残します。

IOCはファイルハッシュ、IPアドレス、ドメイン、URLなどです。各IOCには観測日、
関連キャンペーン、マルウェア、出典、信頼度、複数攻撃での観測状況を可能な範囲で
付与しています。実行コマンド、検体内文字列、ファイル名、パス、レジストリキーなどは
`artifacts.csv`へ分離しています。

## OSINT照合

全673件を固定OSINTデータセットと照合しています。

| 結果 | アクター数 |
|---|---:|
| 一致 | 508 |
| 一致候補 | 2 |
| 一致なし | 163 |

`一致なし`は調査未実施を意味しません。指定データセット内で名前、alias、IDの
完全一致がなかったことを示すだけで、アクターの不存在や誤名を示すものではありません。

主張9,740件の監査結果は次の通りです。

| 状態 | 主張数 |
|---|---:|
| Supported | 7,614 |
| Partially supported | 1,396 |
| Unresolved | 727 |
| Superseded | 3 |

集計データは
[OSINT照合集計](profiles/osint-crosscheck-summary.json)と
[主張監査集計](profiles/claim-audit-summary.json)にあります。利用したデータセットの
バージョン、取得日時、SHA-256は
[dataset-manifest.json](actor_profile/reference/osint/dataset-manifest.json)で確認できます。

## 主要ドキュメント

- [プロファイル一覧](profiles/README.md)
- [フレームワークの利用方法](actor_profile/README.md)
- [データ作成・品質管理ルール](actor_profile/RULES.md)
- [OSINT調査ルール](actor_profile/OSINT_RULES.md)
- [日次ニュース取込](parse-daily/README.md)
- [日次取込エージェント規則](parse-daily/AGENT.md)
- [JSON Schema](actor_profile/schemas/actor-profile.schema.json)
- [処理結果集計](profiles/processing-summary.json)

## 再生成と検証

Python 3で実行できます。PDF・XLSXを新たに取り込む場合は、`pypdf`と`openpyxl`が
利用できる環境が必要です。

```bash
# 既存のIOC/artifactを使って全プロファイルを再生成・検証
python3 actor_profile/scripts/process_all_profiles.py --workers 3 --skip-ingest

# 単体テスト
python3 -m unittest discover -s actor_profile/tests -v
```

新規プロファイルの作成、IOC/artifact取込、個別検証などの詳細は
[Actor Profile Framework](actor_profile/README.md)を参照してください。

`proshiba/tech-memo`の日次ニュースとIOCを更新する場合は、取得、アクター候補照合、
レビュー、冪等反映を行う`parse-daily/`のスクリプトを使用します。ニュース本文の
単純な名前一致や低信頼の帰属は自動反映せず、レビューキューへ保留します。

## 利用上の注意

- 本データは公開情報を基にした脅威インテリジェンスであり、誤検知や情報の陳腐化を含み得ます。
- 候補、情報不明、低信頼度の値を、追加確認なしにブロックや帰属判断へ利用しないでください。
- アクター名の共有やaliasの重複は、必ずしも同一組織を意味しません。
- IOCは時間経過で再割り当てされる可能性があります。観測日と文脈を併せて評価してください。
- STIX出力は交換用の派生物です。修正時は`actor-profile.json`を正規データとして扱ってください。
