# Actor Profile Framework

脅威アクターごとの情報を、同じ構造で作成・検証・出力するためのフレームワークです。

## 成果物

各アクターのディレクトリには、原則として次を配置します。

```text
profiles/<actor-slug>/
├── actor-profile.json          # 正規データ（Single Source of Truth）
├── claim-audit.json            # 主張単位の支持・反証・未解決台帳
├── osint-crosscheck.json       # 固定OSINTデータセットの全件照合結果
├── ioc-sources.json            # IOC取込対象と既定メタデータ
├── iocs.json                   # 正規化・集約済みIOCと全観測イベント
├── artifacts.csv               # コマンド、文字列、パス等の非IOC artifact観測
└── generated/
    ├── profile-ja.md           # 人間向け文書
    └── profile.stix2.json      # STIX 2.1 Bundle
```

自由記述は`free_text`、分析上の留保は`assessment`、各構造化項目固有の補足は
`analyst_notes`に保存します。構造化できないことを理由に情報を捨てません。

## 基本コマンド

```bash
python3 actor_profile/scripts/create_profile.py "Actor Name"

python3 actor_profile/scripts/ingest_observables.py \
  profiles/actor-name/ioc-sources.json \
  --iocs-output profiles/actor-name/iocs.json \
  --artifacts-output profiles/actor-name/artifacts.csv

python3 actor_profile/scripts/render_profile.py \
  profiles/actor-name/actor-profile.json \
  --iocs profiles/actor-name/iocs.json \
  --artifacts profiles/actor-name/artifacts.csv

python3 actor_profile/scripts/validate_profile.py \
  profiles/actor-name/actor-profile.json \
  --iocs profiles/actor-name/iocs.json \
  --artifacts profiles/actor-name/artifacts.csv \
  --stix profiles/actor-name/generated/profile.stix2.json \
  --strict
```

実際には、CodexのバンドルPythonを使うとPDF・XLSX取込も有効になります。

```bash
/Users/hiroshiba/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 \
  actor_profile/scripts/ingest_observables.py ...
```

## 対応するIOC入力

- PDF（`pypdf`がある場合）
- XLSX（`openpyxl`がある場合）
- CSV / TSV
- JSON
- STIX 2.1 JSON
- Markdown / TXT

ZIP、RAR、7z、実行ファイル、DLL、マルウェアサンプルは開きません。

詳細な規約は[RULES.md](RULES.md)を参照してください。

## 全アクターの一括処理

対象と統合・除外ルールは`corpus-catalog.json`で管理します。

```bash
# 全レポートを走査し、アクター名・追跡IDと証拠箇所を列挙
python3 actor_profile/scripts/build_actor_census.py

# 未登録アクターを分類し、actor-scoped evidenceとカタログ項目を作成
python3 actor_profile/scripts/materialize_actor_census.py

# 既存の手動プロファイルを保持し、不足するプロファイルを作成
python3 actor_profile/scripts/bootstrap_all_profiles.py --scan-report-ttps

# IOC/artifact取込、Markdown/STIX生成、検証
python3 actor_profile/scripts/process_all_profiles.py --workers 3

# 共有aliasによる候補関係を低信頼度のoverlapとして保存
python3 actor_profile/scripts/apply_alias_overlap_relationships.py

# 既存のIOC/artifactを使って再レンダリング・再検証のみ
python3 actor_profile/scripts/process_all_profiles.py --workers 3 --skip-ingest

# 全体索引
python3 actor_profile/scripts/render_collection_index.py \
  profiles/processing-summary.json \
  actor_profile/corpus-catalog.json \
  profiles/README.md
```

MITRE ATT&CKのactor、software、campaign、technique関係は
`reference/attack-index.json`に保存したEnterprise ATT&CK 19.1のコンパクト索引を使います。
資料本文にTechnique IDがある場合は、その資料もTTPの根拠へ追加します。

全コーパス走査の根拠は`actor-census.json`、採用・統合・除外判断は
`actor-census-decisions.json`に保存します。複数アクターを扱う年次報告書から
無関係なIOCを誤帰属させないため、新規プロファイルのIOC/artifact取込には
`evidence/<actor-slug>.csv`のアクター周辺文脈だけを使います。原レポートのパスと
ページ／行は同CSVと各プロファイルの`sources`に残します。

共有aliasは一対一の同一性を意味しません。候補関係は
`actor-alias-overlaps.json`へ`candidate`・`low`として保存し、各プロファイルでも
`overlaps-with`として明示します。

OSINT裏取りの主張台帳は各プロファイルの`claim-audit.json`、全体集計は
`profiles/claim-audit-summary.json`です。公式ATT&CK本文から明示的な別グループ参照を
抽出した関係は`osint/mitre-described-relationships.json`、人手で一次資料と
スコープ差を確認した関係は`osint/verified-relationships.json`に保存します。

全件OSINT照合は次の順で再現できます。

```bash
# 公開データを固定した後、CERT-UA索引を構造化
python3 actor_profile/scripts/build_cert_ua_index.py

# canonical name、alias、MITRE ID、帰属候補を全プロファイルで照合
python3 actor_profile/scripts/crosscheck_all_actors.py

# 主張台帳と人間向けMarkdown／STIXを再生成
python3 actor_profile/scripts/build_claim_audits.py
python3 actor_profile/scripts/process_all_profiles.py --workers 3 --skip-ingest
```

固定データセットのバージョン、取得時刻、SHA-256は
`reference/osint/dataset-manifest.json`へ保存します。照合対象はMISP Galaxy、
Microsoft公式actor mapping、CERT-UA公式記事索引、ETDA/ThaiCERT Threat Group
Cardsです。`no-match`は「調査未実施」ではなく、指定された全データセットに
exactな名前／alias／ID一致がなかったことを表します。アクターの不存在や誤名を
意味しません。
