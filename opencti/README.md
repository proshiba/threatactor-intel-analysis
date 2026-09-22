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
```

このディレクトリは生成物です。修正は`profiles/<actor>/actor-profile.json`、`iocs.json`、
Standalone Activityの場合は`actor_profile/standalone-activity-curation.json`と参照先の
`parse-daily/unknown-clusters.json`、それ以外は生成スクリプトへ行ってください。
