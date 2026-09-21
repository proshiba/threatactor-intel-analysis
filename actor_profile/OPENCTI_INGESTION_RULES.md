# OpenCTI / STIX 2.1 取込モデリング規則

この文書は、`actor-profile.json`と`iocs.json`をOpenCTI向けSTIXへ変換する際の
正規ルールです。人間とAI Agentの双方が、同じ情報から異なるentityや誤った時間関係を
作らないことを目的とします。一般的な証拠・確度規則は[RULES.md](RULES.md)、自動生成の
禁止事項は[GENERATION_RULES.md](GENERATION_RULES.md)を併読してください。

## 1. Entityを選ぶ順序

名前ではなく、公開情報が何を識別しているかを先に決めます。

| 状況 | 正規データ / STIX | 判断基準 |
|---|---|---|
| 長期観測された攻撃クラスタ | Actor profile / `intrusion-set` | ベンダー追跡クラスタを含む。実在組織や個人の確定は不要 |
| 実在する企業・組織 | `associated_entities`の`organization` / `identity` | 法人格・実在組織としてのidentityを裏付ける根拠が必要。APTクラスタとは別entityにする |
| 人間の集団として識別された攻撃主体 | `associated_entities`の`threat-actor-group` / `threat-actor` | 構成員・指揮・共同活動等の直接根拠が必要。Intrusion Setの単なる別名では作らない |
| 実在する自然人として識別された実行主体 | `associated_entities`の`threat-actor-individual` / `threat-actor` | 人物identityと攻撃への関与を裏付ける根拠が必要。名前や勤務先だけでは作らない |
| 一定期間・目的・標的・手口を共有する攻撃の波 | Activity + `stix_object_type: campaign` / `campaign` | 1回の配布でも、波として一貫した作戦文脈があればよい |
| 1組織・1システム等に対する個別侵害 | Activity + `stix_object_type: incident` / `incident` | 個別事象を作戦全体へ昇格させない |
| まだ作戦・主体・関係を確定できない分析集合 | Activity + `stix_object_type: grouping` / `grouping` | IP、マルウェア、ポート、AS、証明書等を調査単位として保持 |
| 再利用されるサーバ、ドメイン群、配布基盤 | Capability Infrastructure / `infrastructure` | 攻撃主体、Campaign、Groupingとは分離する |
| IP、ドメイン、URL、メール、証明書 | `iocs.json` / SCO + `indicator` | 値と観測イベントを分離する |
| 継続調査に使う証明書・TLS・署名・driver・通信等の特徴 | `hunting_pivots` / `indicator` + `note` | 単発IOCと分離し、pattern化できない特徴はNoteだけにする |

本リポジトリの既存Actor profileは原則`intrusion-set`として出力します。攻撃者像が詳しく
なったことだけを理由にThreat Actorへ機械昇格しません。また、`intrusion-set`を
「未成熟なThreat Actor」という一方向のライフサイクルとして扱いません。

### 1.1 企業・Threat Actor Group・自然人・法的措置

schema 1.4.0では、APT等の追跡クラスタと、背後に存在すると報告された企業、人間の集団、
自然人を別オブジェクトとして同じprofile内に保持します。

- `entity_type: organization`はSTIX `identity`、`identity_class: organization`へ変換する。
- `entity_type: threat-actor-group`はSTIX `threat-actor`へ変換し、OpenCTIで集団として
  取り込めるよう`x_opencti_type: Threat-Actor-Group`を付ける。組織化された集団には
  STIXの`resource_level: organization`を使う。
- `entity_type: threat-actor-individual`はSTIX `threat-actor`へ変換し、OpenCTIで個人として
  取り込めるよう`resource_level: individual`と
  `x_opencti_type: Threat-Actor-Individual`を付ける。
- 起訴、制裁、逮捕、指名手配、有罪判決、量刑は対象entityを参照するSTIX `note`として出力し、
  `x_legal_action_type`、`x_legal_authority`、`x_legal_action_date`、`x_legal_status`を保持する。
- 起訴・訴追は当局による主張であり、有罪判決ではない。正規データの`indictment` / `charge`は
  `status: alleged`とし、Note本文も断定表現へ変換しない。

企業への雇用とAPT membershipは別Relationshipです。例えば
`Person employed-by Company`と`Company supports APT-X`が存在しても、
`Person member-of APT-X`を生成しません。`member-of`または`operates`は、その人物と
APT活動を直接結ぶ原典がある場合だけ作ります。企業そのものもAPTのaliasにはせず、
`supports`、`facilitates`、`front-company-for`等の根拠に一致する関係で結びます。

法的措置の`action_date`は法的イベントの日付です。entity・Relationshipの
`first_observed` / `last_observed`やCampaign期間には使用しません。起訴状が別途、行為期間を
明示している場合だけ、その記述を根拠として活動・関係期間へ保存します。

## 2. Activityの明示判定

各Activityは、意味を説明する`activity_type`とは別に、必ず次を持ちます。

```json
{
  "stix_object_type": "campaign",
  "grouping_context": null,
  "activity_refs": []
}
```

- `stix_object_type`: `campaign`、`incident`、`grouping`のいずれか。
- `grouping_context`: Groupingなら`suspicious-activity`、`malware-analysis`、
  `unspecified`のいずれか。それ以外は`null`。
- `activity_refs`: Groupingが既存Campaign/Incident等を同じ調査集合へ含める場合の参照。

既定変換は保守的に行います。`intrusion`はIncident、`reported-activity`、
`historical-activity-cluster`、`information-collection`はGrouping、その他の既存の
作戦ラベルはCampaignです。これは初期値であり、原典レビュー後の明示値を上書きしません。
既存レコードを個別レビューした上書き判断は
[activity-stix-model-curation.json](activity-stix-model-curation.json)へ理由付きで保存し、
`migrate_stix_modeling.py`が既定値より優先して適用します。

Groupingの`object_refs`は「同じ分析集合に含まれる」ことだけを意味します。包含された
Campaign、Infrastructure、Observable間に`uses`、`consists-of`、`related-to`等の
Relationshipがあるとはみなしません。関係を裏付ける根拠が得られるまでは、Groupingと
`Note`に仮説・留保を残します。

## 3. Campaign・Infrastructure・Observableの関係

根拠がある場合の基本構造は次のとおりです。

```text
Campaign ──uses────> Malware
Campaign ──uses────> Infrastructure
Campaign ──targets─> Country / Sector / Victim
Infrastructure ──consists-of─> IP / Domain / URL / Email / Certificate SCO
```

同じIP等は値ごとに一つの安定SCO IDを使います。異なるInfrastructureやCampaignで同じ
値が観測された場合、SCOを複製せず、それぞれの根拠付きRelationshipを作ります。

次は原典がその動作を明示した場合だけ作ります。

- Malware `beacons-to` C2 Infrastructure
- Delivery Infrastructure `delivers` Malware
- Malware `downloads` / `drops` Malware

同じCampaignにMalwareとInfrastructureが含まれること、同じレポートに同時掲載されたこと、
IPが重複したことだけから上記を推定してはいけません。ファイルハッシュはマルウェアや検体の
Observableであり、Infrastructureの構成要素へ自動変換しません。

## 4. 時間情報と相関

時間は「何の時刻か」を分離します。

1. 原典が明示した観測時刻: `first_observed` / `last_observed`、Relationshipの
   `start_time` / `stop_time`へ使用可能。
2. 原典から合理的に推定した観測時刻: `status: inferred`と根拠を保存し、上記へ使用可能。
3. レポート公開日: Sourceの`published_at`とSTIX `Report.published`へ保存する。
4. 不明: `value: null`のままにし、公開日やファイル更新日で埋めない。

Relationshipの`start_time` / `stop_time`は、その関係が実際に観測された期間です。
レポート公開日、アクセス日、リポジトリ追加日、profile更新日は入れません。同日しか
判明しない場合は`start_time`だけを設定し、同値の`stop_time`を作りません。

Infrastructure–Observable関係には次の補助値を出力します。

- `x_temporal_basis: observed-at`: 実観測時刻があり、時間相関に使用可能。
- `x_temporal_basis: report-published-fallback`: 公開日しかなく、関係期間は不明。
- `x_temporal_basis: unknown`: 観測時刻も公開日も不明。
- `x_time_correlation_eligible`: 実観測時刻を使える場合だけ`true`。
- `x_report_published_fallback`: 弱い調査手掛かりとしての出典公開日。関係期間ではない。

時刻未設定は「永続的に有効」を意味せず「期間不明」を意味します。OpenCTIの全体Relation
graphだけでIP共有を評価すると、1年離れた再利用IPも近接観測と同じに見えます。相関時は
`x_time_correlation_eligible: true`の関係を優先し、`start_time` / `stop_time`を比較します。
公開日fallbackを使う場合は弱い近接指標として明記し、不明時刻は自動相関から除外します。
EntityやActorのRelationshipも、期間不明ならnative `start_time` / `stop_time`を作らず、
`x_first_observed` / `x_last_observed`と`x_temporal_basis`へunknownと理由を明示します。

## 5. 出典Report

公開日が判明した出典は、OpenCTI Bundle内でSource Reportとして表します。

- `Report.published` = 原典の公開日。
- `x_temporal_role: publication-only`を付ける。
- `object_refs`は、その出典が実際に支えるオブジェクト・Relationshipだけを含める。
- 公開日不明のSourceへ`Report.published`を捏造しない。その場合はExternal Referenceだけを残す。
- Bundle生成日時を示す外側のReportと、原典Reportを混同しない。

自己完結Bundleの参照切れを避けるため、同じ原典を複数Bundleへ収録する場合はBundleごとの
evidence sliceとして別STIX IDを使います。`x_source_id`、公開日、URLで同じ原典だと判断でき、
各sliceの`object_refs`はそのBundle内で原典が支える範囲だけです。sliceの件数を独立した
報告件数として数えてはいけません。

同じ資料に載っていることは証拠文脈の共有であって、掲載オブジェクト間のRelationshipを
自動的に意味しません。

## 6. Hunting PivotのSTIXマッピング

`hunting_pivots`は単発IOCの複製ではなく、再検索可能な特徴とその観測履歴を表す。
STIX/OpenCTIでは次のように変換する。

### 6.1 Patternを持つPivot

安全で十分に限定された`stix_pattern`がある場合、STIX `indicator`と`note`の両方を作る。

- Indicatorはpattern、説明、出典、`x_profile_object_id`、`x_hunting_pivot: true`を保持する。
- `x_pivot_category`、`x_pivot_type`、`x_pivot_value`、`x_attribution_scope`を保持する。
- `x_first_observed` / `x_last_observed`、`x_observation_count`、`x_source_count`、
  `x_activity_count`、`x_continuity`、`x_hunt_queries`を保持する。
- Noteは常に全`observations`、count basis、continuity、query、analyst notesを保持し、
  Actorと明示参照されたMalware/Infrastructure/Activity/Indicatorを`object_refs`で結ぶ。
- Pivot中のexact IOCを通常Indicatorとして生成した場合、そのcanonical `indicator_id`を
  `indicator_refs`へ必ず保存し、Pivotと同じ原典を持つIOC Observationを参照させる。
  非nullの`observations[].activity_ref`と全`source_ref`は、上位`activity_refs`と
  `evidence_refs`にも含める。
- 証明書fingerprintのIndicatorは`certificate-fingerprint`と明示された`hash_algorithm`から
  X.509 patternを生成する。SHA-1 thumbprintをfile SHA-1として出力せず、algorithm不明値や
  serialを推測でSHA-256 fingerprintへ変換しない。
- Actor単位BundleからActivityを分離する場合、そのBundle内のNoteはActor側に存在する参照だけを
  保持する。Activity参照はActivity単位Bundle側に残し、Bundle外を指す`object_refs`を作らない。

Indicatorの`valid_from`はSTIX必須のIndicator有効性フィールドであり、Actorの活動開始日ではない。
source-statedな観測時刻があれば最初の値を使う。観測時刻が不明な場合にschema上の生成時刻を
使用しても、`x_first_observed`はunknownのままとし、Campaign/Relationship期間や時間相関へ
転用しない。証明書有効期間、Source公開日、VT first-seenを`valid_from`または活動期間へ
代入してはいけない。

### 6.2 Patternを持たないPivot

per-deviceで生成される証明書、複合protocol/device profile、公開資料がfingerprintを
明かしていない特徴、広すぎて安全に限定できないissuer/ASN/service条件は`stix_pattern: null`
とし、Noteだけを作る。推測したfingerprint、架空のSCO、issuer/ASN全体を悪性とするIndicatorを
作らない。

### 6.3 件数・継続性・query

- `x_observation_count`はObservationの`count`合計で、count basisをNote側に保持する。
- `x_source_count`と`x_activity_count`は一意参照数であり、observation countと混同しない。
- 現在のlive evidenceがなければ`x_continuity.active_status`は`unknown`。
- passive searchを行っていなければ`passive_scan_performed: false`。
- passive searchを行った場合は`continuity.checks`に実行時刻、platform、query、index/time window、
  結果、analyst validation、根拠、限界を保存する。`evaluated_at`は活動観測日ではない。
- `assessment`は過去の観測構造、`active_status`は評価時点の状態であり独立する。
  `reused` / `reobserved`だけで`active`にせず、単一の0件検索だけで`inactive`にしない。
- Shodan/Censys等の`x_hunt_queries`はanalyst候補生成用で、`requires_validation: true`を必須とする。
  OpenCTI取込、定期生成、AI Agentがqueryを自動実行したり、hitを自動的にIndicator、
  Infrastructure、Actor Relationshipへ昇格したりしてはいけない。
- issuer、ASN、hosting、正規service、port等のgeneric pivotは、`attribution_scope`と誤検知条件を
  保持し、Actor固有Indicatorのように表示・推論しない。

## 7. OpenCTI Bundleの分割と取込順

```text
opencti/
├── actors/<actor>.stix2.json
├── campaigns/<actor>/<activity>.stix2.json
└── activities/<actor>/<activity>.stix2.json
```

- `actors/`: Intrusion Setとアクター全体の知識。Activityは含めない。
- `campaigns/`: 主オブジェクトがCampaignのActivity。
- `activities/`: 主オブジェクトがIncidentまたはGroupingのActivity。
- Grouping Bundleは`activity_refs`で参照したCampaign/Incidentを含められる。
- 推奨順は`actors`、`campaigns`、`activities`。各Bundleは単独でも参照解決できる。

同一STIX IDを複数Bundleへ含める場合、そのobjectは`created` / `modified`を含めてbyte同一にする。
別Actor profileのTTP観測、Indicator assertion、Capability、Activity、標的・被害レコード等、
説明・証拠・観測メタデータがprofileごとに異なるclaimはprofile namespaceの安定IDを使い、
同名や同じATT&CK technique IDだけで一つのSDOへ上書き統合しない。逆にCountry、根拠付きで
同一と確認された関連entity、IP/domain等のatomic SCOのように意図的に共有するobjectは、
profile固有の説明やcampaign参照を本体へ埋め込まず、RelationshipやNoteへ保持する。

Actor Relationshipの終点を別Bundleへ収録するときは簡略stubを作らず、対象Actorの正規な
Intrusion Set objectを再利用する。Bundle自己完結化のためにNoteの`object_refs`をsliceごとに
削る場合は、内容が異なるNoteへ同じSTIX IDを再利用せずslice固有IDを使う。全Bundle生成時は
同一IDのobject定義を横断検証し、semantic差分またはbyte差分があれば取込前に失敗させる。
- 同じSTIX IDを複数Bundleへ収録する場合、`created` / `modified`を除く意味内容も同一にする。
  profile固有の説明・出典・期間は共有SDOへ混在させず、Relationship、Noteまたは
  profile-scoped IDへ保存する。

## 8. 非標準RelationshipのOpenCTIフォールバック

`entity_relationships.relationship_type`は正規データ上ではopen vocabularyとして扱い、
`employed-by`、`founder-of`、`officer-of`、`member-of`、`operates`、`supports`、
`facilitates`、`front-company-for`等、原典が直接支持する意味を保存します。

OpenCTIで安全に受理できるRelationship動詞は実装上`part-of`と`related-to`を基本とします。
それ以外の動詞は次のように出力します。

1. STIX `relationship_type`は`related-to`へフォールバックする。
2. 元の動詞を`x_profile_relationship_type`へ保存する。
3. 正規IDを`x_profile_relationship_id`へ保存する。
4. `description`、`external_references`、確度、`x_analyst_notes`、実観測期間を保持する。

このフォールバックは取込互換性のための表現変換であり、正規データの意味を
`related-to`へ変更するものではありません。OpenCTI側が新しい動詞を受理することを検証して
allowlistへ追加する場合は、生成テストも同時に更新します。Relationshipの端点が一意に
解決できない場合は対象を推測生成せず、関係の説明と元動詞をNoteまたはmanifestへ残します。

## 9. AI Agentの取込チェックリスト

新規・更新時は次を順に確認します。

1. これはActor、Campaign、Incident、Grouping、Infrastructure、Observableのどれか。
2. Campaignとする作戦上のまとまりが原典にあるか。単発個別侵害ならIncidentか。
3. 不確実な相関をRelationshipにせず、Groupingの包含に留めたか。
4. `activity_type`と`stix_object_type`を混同していないか。
5. Relationshipの両端と動詞を原典が支持しているか。
6. 観測時刻と公開日を分離したか。
7. IP等の共有を時間差なしの強い関係として扱っていないか。
8. 同一Observableを値ごとに再利用し、複製していないか。
9. 出典Reportの`object_refs`を出典が支える範囲に限定したか。
10. 企業をOrganization、自然人をThreat Actor IndividualとしてIntrusion Setから分離したか。
11. 雇用・企業支援から人物のAPT membershipを推論していないか。
12. 起訴を`alleged`として保持し、法的措置日と活動期間を分離したか。
13. 非標準Relationshipの元動詞を`x_profile_relationship_type`へ保持したか。
14. 単発IOCとHunting Pivotを分離し、count basisとsource/activity countを確認したか。
15. 証明書有効期間、公開日、VT first-seen、scan時刻を活動日へ転用していないか。
16. live evidenceなしの`active_status`をunknown、未検索を`passive_scan_performed: false`にしたか。
17. generic issuer/ASN/service/portとShodan/Censys queryにanalyst validationを要求したか。
18. PatternなしPivotをNoteだけにし、PatternありPivotをIndicator + Noteへ変換したか。
19. 生成、schema検証、STIX parse、参照切れ検証を実行したか。

### 禁止する自動変換

- すべてのActivityをCampaignにする。
- Groupingの包含からRelationshipを生成する。
- レポート公開日を観測時刻・Campaign期間・Relationship期間へコピーする。
- IP、ASN、ホスティング事業者の一致だけでActor同一性や帰属を確定する。
- Campaign内の共存だけでMalware `beacons-to` Infrastructureを作る。
- 名前が一致するだけでIntrusion Set、Threat Actor、Threat Actor Groupを統合・昇格する。
- 企業への雇用・所属だけで自然人をAPTのmemberまたはoperatorにする。
- 起訴日・制裁日・逮捕日を攻撃活動やmembershipの開始・終了日にする。
- 証明書有効期間、Source公開日、VT first-seen、scan時刻をPivotの活動期間にする。
- issuer、ASN、hosting provider、正規サービス、汎用portの一致だけでActorを帰属する。
- Shodan/Censys queryのhitをanalyst validationなしでIOCまたはRelationshipへ昇格する。
