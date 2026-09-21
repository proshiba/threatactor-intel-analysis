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
| 実在する個人・組織として識別された実行主体 | 将来のThreat Actorモデル | 組織・個人としてのidentityを裏付ける根拠が必要。クラスタ名だけでは作らない |
| 共通目的を持つ複数Actorの実組織 | 将来のThreat Actor Groupモデル | 構成員・指揮・共同活動等の根拠が必要。単なる上位aliasやベンダー上の包括名では作らない |
| 一定期間・目的・標的・手口を共有する攻撃の波 | Activity + `stix_object_type: campaign` / `campaign` | 1回の配布でも、波として一貫した作戦文脈があればよい |
| 1組織・1システム等に対する個別侵害 | Activity + `stix_object_type: incident` / `incident` | 個別事象を作戦全体へ昇格させない |
| まだ作戦・主体・関係を確定できない分析集合 | Activity + `stix_object_type: grouping` / `grouping` | IP、マルウェア、ポート、AS、証明書等を調査単位として保持 |
| 再利用されるサーバ、ドメイン群、配布基盤 | Capability Infrastructure / `infrastructure` | 攻撃主体、Campaign、Groupingとは分離する |
| IP、ドメイン、URL、メール、証明書 | `iocs.json` / SCO + `indicator` | 値と観測イベントを分離する |

本リポジトリの既存Actor profileは原則`intrusion-set`として出力します。攻撃者像が詳しく
なったことだけを理由にThreat Actorへ機械昇格しません。また、`intrusion-set`を
「未成熟なThreat Actor」という一方向のライフサイクルとして扱いません。

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

## 6. OpenCTI Bundleの分割と取込順

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

## 7. AI Agentの取込チェックリスト

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
10. 生成、schema検証、STIX parse、参照切れ検証を実行したか。

### 禁止する自動変換

- すべてのActivityをCampaignにする。
- Groupingの包含からRelationshipを生成する。
- レポート公開日を観測時刻・Campaign期間・Relationship期間へコピーする。
- IP、ASN、ホスティング事業者の一致だけでActor同一性や帰属を確定する。
- Campaign内の共存だけでMalware `beacons-to` Infrastructureを作る。
- 名前が一致するだけでIntrusion Set、Threat Actor、Threat Actor Groupを統合・昇格する。
