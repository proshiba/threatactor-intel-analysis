# OpenCTI import bundles

このディレクトリは`actor-profile.json`と`iocs.json`から生成した、OpenCTIの
`ImportFileStix`コネクタで取り込むためのSTIX 2.1 Bundleです。

## 構成

```text
opencti/
├── manifest.json
├── actors/
│   └── <actor-slug>.stix2.json
├── campaigns/
│   ├── <actor-slug>/<activity-id>.stix2.json
│   └── unattributed/<activity-id>.stix2.json
└── activities/
    ├── <actor-slug>/<activity-id>.stix2.json
    └── unattributed/<activity-id>.stix2.json
```

- `actors/`: アクター本体、アクター全体のマルウェア・ツール・インフラ・TTP・標的、
  Activity未割当IOC、解決済みアクター関係を収録します。Campaign/Incident/Groupingは含みません。
- `campaigns/`: 1ファイルにつきCampaignを1件だけ収録します。アクター本体に加え、
  その活動へ明示的に結び付いたマルウェア、インフラ、TTP、標的、被害事例、IOC、
  関係を含む自己完結Bundleです。
- `activities/`: 主オブジェクトがIncidentまたはGroupingのActivityを収録します。
  Groupingの包含は分析集合を意味し、包含オブジェクト間のRelationshipを暗黙に作りません。
- `campaigns/unattributed/`と`activities/unattributed/`: 根拠はあるがActorへ昇格できない
  Standalone Activityです。`actor_profile/standalone-activity-curation.json`で明示的に
  採用した対象だけを出力し、Intrusion Set、Threat Actor、Activity→Actor関係は含めません。
- `manifest.json`: 全ファイル、表示名、元Profile/Activity ID、オブジェクト数、サイズ、
  解決できなかったアクター関係を列挙します。

## ダウンロードとRelease配布

OpenCTIへ取り込む配布物は、この`opencti/`だけを使用します。
`profiles/*/generated/profile.stix2.json`はプロファイル単位の別表現であり、deprecatedな
旧プロファイルも保持するため、OpenCTI Bundleと混在させて取り込まないでください。

[GitHub Releases](https://github.com/proshiba/threatactor-intel-analysis/releases)では、
次のassetを配布します。Archiveは1個の巨大なSTIX Bundleではなく、このディレクトリの
自己完結Bundleをそのまま保持します。OpenCTIへはArchive自体を渡さず、展開後のJSONを
取り込んでください。

- `opencti-stix-all.tar.gz`: README、corpus-wide manifest、全Bundle。
- `opencti-stix-all.zip`: 上記と同じ内容のZIP版。
- `opencti-stix-actors.tar.gz`: README、corpus-wide manifest、Actor Bundle。
- `opencti-stix-campaigns.tar.gz`: README、corpus-wide manifest、Campaign Bundle。
- `opencti-stix-activities.tar.gz`: README、corpus-wide manifest、Incident/Grouping Bundle。
- `opencti-manifest.json`: Archive内`opencti/manifest.json`のbyte同一コピー。
- `SHA256SUMS`: 上記6 assetのSHA-256。自身は一覧に含めません。

分類別Archive内のmanifestも全corpusを記述します。そのArchiveだけに含まれるファイルの
一覧ではないため、分類別の実ファイルはmanifestの`actors`、`campaigns`、`activities`の
該当配列を参照してください。

GitHub CLIで全体tar.gzを取得する例:

```bash
gh release download \
  --repo proshiba/threatactor-intel-analysis \
  --pattern 'opencti-stix-all.tar.gz' \
  --pattern 'SHA256SUMS'
sha256sum --ignore-missing -c SHA256SUMS
tar -xzf opencti-stix-all.tar.gz
```

macOSでは検証行を絞って
`grep 'opencti-stix-all.tar.gz$' SHA256SUMS | shasum -a 256 -c -`を使用できます。

国・地域はOpenCTIの`Location`（`x_opencti_location_type`を付与）、産業・役割は
`identity_class: class`の`Identity`として出力します。国は固定したOpenCTI公式データセットの
英語名、ISO 3166-1 alpha-3コード、座標、aliasへ照合し、元の日本語名もaliasとして保持します。
公式IDは追跡用の`x_opencti_reference_id`に保存します。OpenCTIは名称・aliasとLocation種別で
Countryを重複排除するため、アクター固有の標的説明と出典は共有Country本体ではなく
`targets` Relationshipへ移して保持します。アクター境界を安全に解決できない関係は
別アクターを自動生成せず、元アクターを参照する`Note`として根拠と評価を保持します。

IP、ドメイン、URL、メール、証明書は値ごとのSCOとして出力し、`iocs.json`に明示された
Infrastructureからだけ`consists-of`で結びます。関係の`start_time`/`stop_time`には実観測時刻
だけを使い、出典公開日しかない場合は`x_temporal_basis: report-published-fallback`として
保持します。公開日が判明した出典はSource Reportとなり、`Report.published`に原典公開日を
保存します。詳細は[取込モデリング規則](../actor_profile/OPENCTI_INGESTION_RULES.md)を参照してください。

## OpenCTIへの取込

OpenCTIで`ImportFileStix`コネクタを有効にし、Data import / Analyst WorkbenchからJSONを
アップロードします。先に`actors/`、次に`campaigns/`、最後に必要な`activities/`を取り込むと
確認しやすくなります。各Activity Bundleも必要な参照先を同梱しているため、単独取込が可能です。

全オブジェクトIDは元Profile/Activity IDから安定生成します。同じファイルを再取込しても
別IDを増殖させず、同じSTIXオブジェクトとして更新されます。全Bundleは`TLP:CLEAR`で、
生成時の最大ファイルサイズを45 MiB未満に制限しています（OpenCTIの既定50 MiB上限に余裕を
持たせるため）。

OpenCTI公式資料:

- [Import from files](https://docs.opencti.io/latest/usage/import-files/)
- [Containers](https://docs.opencti.io/latest/usage/containers/)
- [Data model](https://docs.opencti.io/latest/usage/data-model/)
- [OpenCTI geography dataset](https://github.com/OpenCTI-Platform/datasets/blob/417372284aa696acdd8ee86f4c17904e1391046f/data/geography.json)

## 再生成

```bash
python3 actor_profile/scripts/process_all_profiles.py --workers 3 --skip-ingest
python3 actor_profile/scripts/build_opencti_bundles.py --prune

# manifestと全Bundleを検証し、再現可能なRelease assetとSHA256SUMSを作成
python3 actor_profile/scripts/package_opencti_release.py \
  --output-dir dist/opencti-release
```

`Package and release OpenCTI STIX` Workflowは、手動実行時には14日保持のActions artifactを
作成し、`opencti-vYYYY.MM.DD`形式のtag push時には同じ検証済みassetをGitHub Releaseへ
公開します。Release tagは`main`上のcommitを指す移動されていないlightweight tagだけを
許可します。同日に複数回公開する場合は
`opencti-vYYYY.MM.DD-2`のように末尾へ番号を付けます。

```bash
git switch main
git pull --ff-only
git tag opencti-vYYYY.MM.DD
git push origin opencti-vYYYY.MM.DD
```

このディレクトリは生成物です。修正は`profiles/<actor>/actor-profile.json`、`iocs.json`、
Standalone Activityの場合は`actor_profile/standalone-activity-curation.json`と参照先の
`parse-daily/unknown-clusters.json`、それ以外は生成スクリプトへ行ってください。
