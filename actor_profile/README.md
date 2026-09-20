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

## 関与組織レジストリ

攻撃に関与する組織（民間受託企業、商用スパイウェアベンダー、政府機関、軍部隊）は
`actor_profile/organizations.json`で組織側から一意に管理します。

```text
actor_profile/
├── curated-organizations.json  # 手入力部分（種別、国、profile_slug、固有の出典）
├── build_organizations.py      # profiles/ の attribution.organizations を集約
└── organizations.json          # 生成物。直接編集しない
```

```bash
python3 actor_profile/build_organizations.py          # 差分確認
python3 actor_profile/build_organizations.py --apply  # 書き出し
```

`attribution.organizations`はアクター単位の属性のため、組織側から関与アクターを
逆引きできません。1組織が複数アクターに関与する例は既に存在し（`apt-c-27`と
`apt-c-37`がいずれもSyrian Air Force Intelligenceを参照）、i-Soonのように流出資料が
多数のクラスタへ結び付く対象では逆引きが必須になります。レジストリはこれを補います。

組織の扱いは3通りに分かれます。

- **組織自体を攻撃主体／商用攻撃事業者としてプロファイルする場合**:
  `profiles/<slug>/actor-profile.json`を作成し、レジストリ側は`status: profiled`と
  `profile_slug`で参照します。ただし会社・製品ベンダーというentityと、顧客や政府機関が
  実行する個別侵入活動は分離します。製品が攻撃で使われたという事実だけで、開発会社を
  adversaryへ置いてはいけません。Cellebriteのような端末解析ベンダーは特にこの区別を
  必須とします。
- **アクターの関与組織**: レジストリに`status: tracking`で登録し、関係は
  各プロファイルの`attribution.organizations`側に残します。
- **未調査の調査対象**: `status: planned`で枠だけ確保します。主張を一切含めず、
  記述の追加前に一次資料を確認します。

組織IDは`organization--<name>`へ正規化します。既存プロファイルには`org--<name>`形式が
残っているため、`build_organizations.py`が正規化したうえで元の表記を`legacy_ids`へ
保存します。`profiles/`側の表記統一は未実施です。

本レジストリは`profiles/`配下ではないため、`ui/build_data.py`と
`ui/build_portal_index.py`のどちらからも読まれずUIには出ません。

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
自動生成・エージェント更新時の禁止事項と判断手順は
[GENERATION_RULES.md](GENERATION_RULES.md)を必ず併読してください。

既存profileに旧生成ロジック由来のcountry→state→espionage推定が残っている場合は、
`python3 actor_profile/scripts/migrate_generated_attribution.py --apply`を使用します。
このmigrationは定型的な旧自動生成値だけを対象にし、手動attributionや日次Activity、IOC等は保持します。

## 全アクターの一括処理

対象と統合・除外ルールは`corpus-catalog.json`で管理します。

```bash
# 全レポートを走査し、アクター名・追跡IDと証拠箇所を列挙
python3 actor_profile/scripts/build_actor_census.py

# 未登録アクターを分類し、actor-scoped evidenceとカタログ項目を作成
python3 actor_profile/scripts/materialize_actor_census.py

# 既存の手動プロファイルを保持し、不足するプロファイルを作成
python3 actor_profile/scripts/bootstrap_all_profiles.py --scan-report-ttps

# 一次情報で確認した最新alias、改称、明示的なentity境界を反映
python3 actor_profile/scripts/apply_verified_alias_updates.py

# IOC/artifact取込、Markdown/STIX生成、検証
python3 actor_profile/scripts/process_all_profiles.py --workers 3

# 共有aliasによる候補関係を低信頼度のoverlapとして保存
python3 actor_profile/scripts/apply_alias_overlap_relationships.py

# 既存のIOC/artifactを使って再レンダリング・再検証のみ
python3 actor_profile/scripts/process_all_profiles.py --workers 3 --skip-ingest

# Activity、TTP、被害事例、標的の参照から活動別Diamond Modelを再生成
python3 actor_profile/scripts/materialize_activity_diamonds.py --apply

# 全体索引
python3 actor_profile/scripts/render_collection_index.py \
  profiles/processing-summary.json \
  actor_profile/corpus-catalog.json \
  profiles/README.md
```

MITRE ATT&CKのactor、software、campaign、technique関係は
`reference/attack-index.json`に保存したEnterprise ATT&CK 19.1と、
`reference/attack-ics-index.json`に保存したICS ATT&CK 19.2のコンパクト索引を使います。
資料本文にTechnique IDがある場合は、その資料もTTPの根拠へ追加します。

全コーパス走査の根拠は`actor-census.json`、採用・統合・除外判断は
`actor-census-decisions.json`に保存します。自動censusだけでは安全に判断できない
entity種別、canonical名、重複統合、alias、actor typeの人手補正は
`actor-census-curation.json`に保存します。curationは自動materializationより優先し、
`exclude`（Actorとして生成しない）、`merge`（既存profileへ統合）、`override`
（canonical名・slug・alias・actor typeの補正）を再生成時にも維持します。

curationへ追加する場合は必ずactor-specificな根拠URLと理由を記録します。単なる
名前一致やcountry/originだけを根拠にoverrideしてはいけません。

複数アクターを扱う年次報告書から
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
python3 actor_profile/scripts/enrich_activity_intelligence.py --apply
python3 actor_profile/scripts/enrich_targeting_scope.py --apply
python3 actor_profile/scripts/materialize_activity_diamonds.py --apply
python3 actor_profile/scripts/process_all_profiles.py --workers 3 --skip-ingest
```

`enrich_targeting_scope.py`は、活動本文、MITRE ATT&CK Group概要、高確度で
アクター照合できたMISP／ETDAの被害地理フィールド、レビュー済み一次資料補正を
標的国・地域へ統合します。帰属国、C2の所在国、帰属表明を行った国は標的として
扱いません。広域活動は`全世界`等の地域を保持し、日本の被害が確認できる場合は
地域表示とは別に`日本`を個別保持します。複数の個別国から導出した地域は
「域内全体が標的だった」という意味ではなく、UIでの集約表示用です。

監査結果は`profiles/targeting-audit.json`に保存されます。
`no-structured-geography`、`single-country-no-region`、
`unresolved-osint-values`は追加調査キューとして扱い、証拠のない国を推測で
補完しません。一次資料で確認した例外・補正は
`actor_profile/targeting-curation.json`へ根拠とともに追加します。

単一アクターの日次更新では、全件の監査時刻を書き換えずに対象台帳だけを再生成できます。

```bash
python3 actor_profile/scripts/build_claim_audits.py --actor actor-slug
```

固定データセットのバージョン、取得時刻、SHA-256は
`reference/osint/dataset-manifest.json`へ保存します。照合対象はMISP Galaxy、
Microsoft公式actor mapping、CERT-UA公式記事索引、ETDA/ThaiCERT Threat Group
Cardsです。`no-match`は「調査未実施」ではなく、指定された全データセットに
exactな名前／alias／ID一致がなかったことを表します。アクターの不存在や誤名を
意味しません。
