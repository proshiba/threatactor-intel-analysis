# 脅威アクタープロファイル作成規約

規約バージョン: 1.2.0

## 1. 基本原則

1. `actor-profile.json`を唯一の正規データとし、MarkdownとSTIXは生成物とする。
2. 全アクターで同じ最上位構造を使用する。情報がない項目も削除せず、空配列または
   `null`と理由を残す。
3. 構造化できない重要情報は`free_text`または`analyst_notes`に保存する。
4. 事実、情報源の主張、分析者の推定を区別する。
5. 不明な日付、帰属、関係、対象を推測で埋めない。
6. 各重要主張は1件以上の`evidence_refs`で`source_id`へ結び付ける。
7. ベンダー別名は、完全一致が確認できない場合に`scope`と`confidence`を明記する。
8. IOCだけでアクター帰属を断定しない。
9. 感染済みアーカイブやサンプルをIOC抽出のために実行・展開しない。

## 2. ID規則

IDはアクター内で一意かつ安定させる。

| 対象 | 形式例 |
|---|---|
| Profile | `actor--kimsuky` |
| Source | `source--joint-csa-2023` |
| Malware | `malware--appleseed` |
| Infrastructure | `infra--lookalike-domains` |
| Activity | `activity--operation-newton` |
| Relationship | `relationship--kimsuky-apt37-overlap` |
| Target | `target--think-tanks-academia` |
| IOC | `indicator--sha256:<stable digest>` |
| Observation | `observation--sha256:<stable digest>` |
| Hunting Pivot | `hunting-pivot--<actor>-<stable name>` |
| Pivot Observation | `pivot-observation--<stable name>` |

表示名が変わっても既存IDを変更しない。

## 3. 確度

`confidence`は`high`、`medium`、`low`、`unknown`のいずれかとする。

- `high`: 政府共同勧告、複数の独立した技術資料、直接観測で裏付け。
- `medium`: 信頼できる単一資料、または複数の間接証拠。
- `low`: 単一の間接情報、帰属競合、未検証リーク。
- `unknown`: 評価する情報がない。

数値が必要な出力先では、high=85、medium=60、low=30、unknown=0を既定値とする。

## 4. 時間情報

すべての時間はISO 8601で保存する。日付精度は別フィールドに記録する。

```json
{
  "value": "2023-05-31T00:00:00Z",
  "precision": "day",
  "status": "known",
  "basis": "source-stated"
}
```

不明の場合:

```json
{
  "value": null,
  "precision": "unknown",
  "status": "unknown",
  "basis": "not-stated"
}
```

資料の発行日、ファイル更新時刻、リポジトリ追加日は、IOCの観測日と同一視しない。
観測時期が「2023年5月」の場合は月初へ正規化し、`precision: "month"`を付ける。

Activityは`first_observed`、`last_observed`に加えて`reported_at`を必ず持つ。
`reported_at`は活動を報告した資料の発行日または日次収集日であり、攻撃期間ではない。
攻撃期間が不明でもActivity自体を省略せず、`first_observed`と`last_observed`をunknown、
`reported_at`を判明範囲で記録する。UIの「過去1年」「過去3年」等の活動・TTP・
マルウェア期間集計と並び替えには`reported_at`を使用しない。報告日は活動時期不明の
理由を明示する補助表示に限り、STIX Campaignの`first_seen`/`last_seen`へ転用しない。

Activityは`activity_type`とは別に、STIX entity境界を明示する`stix_object_type`を必ず持つ。
値は`campaign`、`incident`、`grouping`のいずれかとする。`intrusion`等の意味ラベルだけから
全件をCampaignへ変換してはいけない。Groupingは`grouping_context`と`activity_refs`を持ち、
包含されたオブジェクト間のRelationshipを暗黙に主張しない。詳細な判断と時間相関規則は
[OPENCTI_INGESTION_RULES.md](OPENCTI_INGESTION_RULES.md)を正とする。

Activityは`ttp_refs`と`victim_refs`も必ず持つ。参照先が判明しない場合は空配列にする。
正規の管理ツール、RMM、OS標準機能、攻撃フレームワーク等を活動内で利用した根拠がある場合は、
Malwareへ混在させず`capabilities.tools`のToolを`tool_refs`で参照する。`tool_refs`は後方互換の
任意フィールドであり、未評価と利用なしを区別する必要がある場合だけ明示的な空配列を使う。
TTP・マルウェア・ツール・標的・被害事例を活動へ結び付ける際は、同じ証拠がその活動内での
利用または被害を支持することを確認する。単なるアクター一般の利用実績は活動へ結び付けない。

### 4.1 活動別ダイヤモンドモデル

すべてのActivityは`diamond_model`を持つ。これはアクター全体の`diamond_model`とは
別物であり、その活動に直接結び付いた構造化情報だけから次の4頂点を構成する。

- `adversary`: `actor_ref`、正規名、帰属国、帰属組織参照
- `capability`: 活動・被害事例・活動TTPに結び付いた`malware_refs`、明示された
  `tool_refs`、`ttp_refs`
- `infrastructure`: 活動または活動TTPに結び付いた`infrastructure_refs`
- `victim`: 活動と被害事例に結び付いた`target_refs`と`victim_refs`

`meta_features`には活動期間・報告日、活動種別、ATT&CKフェーズ、被害結果、
攻撃元国から標的国・地域への方向を保存する。帰属国は攻撃元、標的国・地域は被害側として
分離し、同じ配列へ混在させない。被害事例に結び付いた標的、マルウェア、TTP、影響は、
同じActivityへの明示参照がある場合に限りモデルへ統合できる。

活動単位の証拠がない頂点は空配列のままにし、アクター全体で利用実績があるという理由で
補完しない。モデルは正規レコードの参照から生成する派生構造であり、活動・TTP・被害事例を
変更した後は次を実行する。

```bash
python3 actor_profile/scripts/materialize_activity_diamonds.py --apply
```

## 4.2 被害事例

被害事例は`victim_cases`へ保存し、単なる標的一覧と分離する。公開情報が個別組織名を
明示しない場合も、匿名組織または集約事例として保存できる。必須項目は次の通り。

- `victim_case_id`
- `victim_name`と`disclosure_status`
- `victim_type`
- `case_status`
- `activity_refs`
- `target_refs`
- `malware_refs`
- `ttp_refs`
- `affected_assets`
- `impacts`
- `first_observed`、`last_observed`、`reported_at`
- `confidence`、`evidence_refs`

`disclosure_status`は`named`、`anonymous`、`aggregate`、`unknown`のいずれかとする。
`case_status`は`confirmed`、`reported`、`alleged`、`disputed`、`unknown`のいずれかとし、
攻撃者のリークサイト上の主張、被害組織の確認、第三者報告、明示的な否定を混同しない。
アクターの帰属国、報告元の所在地、ニュース発行国を被害国として推定しない。
被害組織名、国、産業、影響は情報源が明示した範囲だけを記録する。複数組織をまとめた
統計は、架空の単一被害者へ変換せず`aggregate`として保持する。

## 5. Alias規則

各aliasには以下を持たせる。

- `name`
- `vendor`
- `scope`: `exact`、`overlapping`、`broader`、`narrower`、`unknown`
- `confidence`
- `evidence_refs`
- `analyst_notes`

異なるベンダークラスタを、名称一覧だけを根拠に`exact`へ統合しない。

OpenCTI/STIXの標準`aliases`は検索用の自由語彙ではなく、OpenCTIがIntrusion Setの
重複排除に使う同一性キーである。このため、標準`aliases`へ出力できるのは
`scope: exact`かつ`confidence: high`の名称だけとする。`exact`でも確度がmedium/lowの名称、
および`overlapping`、`broader`、`narrower`、`unknown`は
`x_alias_assessments`と根拠付きNoteへ保持し、`aliases`または`x_opencti_aliases`へ入れない。
同じ正規化aliasが複数のactive profileの同一性キーになる場合は生成を失敗させる。

aliasが存在しないことは有効な状態である。大文字小文字、空白、ハイフンだけを機械的に
変えた名称や、集約資料・workbookだけの候補を、件数を埋めるためにalias化しない。
ベンダー公式mappingでも、旧称、他社対応名、Software、Campaign、Organizationが混在し得る。
同一ベンダーの明示的renameはそのtaxonomy内の`exact`にできるが、他社対応名は原則
`overlapping`とし、entity種別と既存profile衝突を確認する。

一方、公式ATT&CKの同一Group IDと命名元ベンダー資料で単なるrenameであることを確認した
名称は、別のcanonical profileを作らず既存profileの`exact` aliasとして保持する。
同一性の確認には名前一致だけでなく、Group IDとactor-specificな原典を必要とする。
Software/Malware名とActor名が一致する場合はentity種別を先に確認し、原典が独立した
operator/groupを定義していなければActorとしてmaterializeしない。

## 6. アクター間関係

`relationship_type`は次を優先する。

- `part-of`
- `subordinate-to`
- `distinct-from`
- `overlaps-with`
- `shares-tools-with`
- `shares-infrastructure-with`
- `shares-targeting-with`
- `cooperates-with`
- `successor-of`
- `related-to`

「同一アクター」と「ツール／インフラの重複」を分離する。関係には必ず説明、確度、
証拠を付ける。

### 6.1 関連企業・自然人・法的措置

schema 1.4.0では、既存のActor profile（原則`intrusion-set`）とは別に、実在する企業、
自然人、および人間の集団として十分に識別されたThreat Actor Groupを
`associated_entities`へ保存する。

- 法人格を持つ企業、研究機関、請負会社等は`entity_type: organization`、
  `entity_id: organization--...`とする。企業名をAPTクラスタのaliasにしない。
- 実在する自然人が攻撃実行、指揮、開発、仲介等へ関与したことを根拠付きで識別できる場合は
  `entity_type: threat-actor-individual`、`entity_id: threat-actor-individual--...`とする。
  同姓同名、ハンドル一致、勤務先だけでは同一人物または攻撃者と断定しない。
- 犯罪シンジケート、国家機関内の実行者集団等、人間の集団として直接識別された対象は
  `entity_type: threat-actor-group`、`entity_id: threat-actor-group--...`とする。
  同名・aliasだけで既存Intrusion Setと統合せず、境界が部分的なら別オブジェクトのまま
  `overlaps-with`等で結ぶ。
- 企業・個人・Intrusion Set間の関係は`entity_relationships`へ保存する。雇用関係は
  `employed-by`、役員・創業関係は`officer-of` / `founder-of`、攻撃クラスタへの参加を
  原典が直接支持する場合だけ`member-of` / `operates`等を使用する。
- Relationshipの向きは`個人 → employed-by/officer-of/founder-of → Organization`、
  `個人 → member-of/operates → Threat Actor GroupまたはIntrusion Set`、
  `Organization → supports/facilitates/front-company-for → 攻撃主体`、
  `組織・当局 → tasks/directs → 個人または集団`を標準とする。原典が`alleged`、
  `assessed`、`likely`等の留保を付ける場合は、動詞、説明、確度から留保を落とさない。
- `個人 employed-by 企業`および`企業 supports Intrusion Set`から、個人の
  `member-of Intrusion Set`を推移的に生成してはいけない。人物ごとの直接の根拠を要求する。
- 起訴、訴追、制裁、逮捕、指名手配、有罪判決、量刑は対象entityの`legal_actions`へ保存する。
  起訴状・訴追資料が主張する行為は有罪認定ではないため、`indictment` / `charge`の
  `status`は`alleged`とする。後日の`conviction`や`sentencing`は別のlegal actionとして追加し、
  過去の起訴レコードを有罪判決へ書き換えない。

`legal_actions[].action_date`は起訴、制裁指定、逮捕等の法的措置日である。
`associated_entities[].first_observed` / `last_observed`および
`entity_relationships[].first_observed` / `last_observed`は、人物・企業または関係が実際に
サイバー活動上の役割・関与で観測された期間であり、法人設立日、出生情報、単なる資料初出、
法的措置日、資料公開日を代入しない。活動期間が不明ならunknownのままにし、起訴日から
活動開始・終了を推定しない。

同一の実在企業・自然人・Threat Actor Groupを複数profileへ収録する場合は同じ安定
`entity_id`を使用し、名称、alias、entity type、identity-level description、legal action、
evidence定義を一致させる。アクター固有の役割、関係、観測期間はentity本体へ混在させず、
各profileの`entity_relationships`へ保存する。同じ`source_id`も同一定義を持たせる。

## 7. CapabilityとTTP

Capabilityは以下を分離する。

- マルウェア
- ツール
- インフラ
- 配送・ファイル形式
- 脆弱性
- 運用能力

TTPは1行を「Actor × Technique × Activity」として扱える粒度にする。
同じTechniqueでも活動、マルウェア、観測時期が異なる場合は別レコードにできる。

必須項目:

- `tactic`
- `technique_id`
- `technique_name`
- `observed_behavior`
- `activity_refs`
- `malware_refs`
- `infrastructure_refs`
- `first_observed`
- `last_observed`
- `confidence`
- `evidence_refs`

UIの期間別集計では、活動参照を持つTTPだけを「観測」として数える。汎用的な
Actor→Techniqueマッピングは基礎マッピングとして表示できるが、活動頻度には加算しない。
`all time`は日付不明の活動別観測も含める。過去1年・過去3年などの期間表示は、
TTP自身の`first_observed`または`last_observed`がknown/inferredの場合だけ対象にする。
資料発行日`reported_at`をTTP観測日へ代入しない。互換データに
`basis: source-publication`や`publication/ongoing`が残る場合も、期間集計から除外する。

## 8. IOCモデル

IOC値と観測イベントを分離する。IOCとして扱うのは、原則として次の値である。

- MD5 / SHA-1 / SHA-256 / SHA-512
- IPv4 / IPv6
- ドメイン
- URL
- メールアドレス
- 証明書フィンガープリント

実行コマンド、ファイルパス、検体内文字列等はIOCへ混在させず、`artifacts.csv`へ保存する。

### 8.0 IOCとして扱わない値

次の値は、形式が上記に当てはまってもIOCとして取り込まない。いずれも脅威と無関係な値であり、
横断検索で無関係な資料同士を誤って結び付けるためである。判定用のデータは
[reference-hosts.json](reference/reference-hosts.json)と
[iana-tlds.json](reference/iana-tlds.json)に置き、`scripts/ingest_observables.py`（取込）、
`scripts/validate_profile.py`（検証）、`../ui/build_portal_index.py`（公開索引）が共有する。

**1. 出典レポート自身の参考リンク**

ベンダーブログ、CERT、報道、リファレンスサイトのURL・ドメイン・問い合わせ窓口
メールアドレス。`securelist.com`、`attack.mitre.org`、`www.microsoft.com`など。
ホスト名の完全一致とドット区切りのサフィックス一致で判定する。

**2. ホストとして成立しない値**

TLDが[IANAの委任一覧](reference/iana-tlds.json)に存在しない値は、ファイル名
（`dbconn.asp`、`loader.exe`）か文の断片（`safe.headquartered`）であってドメインではない。
ドットを含まない値（`https://www/`、`https://unit42/`）も抽出途中で切れたものとして扱う。

ファイル拡張子を列挙して判定してはならない。`.com`はCOM実行ファイルの拡張子でもあるが
TLDとして実在するため、列挙すると本物のドメインを取りこぼす。`.md`（モルドバ）、
`.py`（パラグアイ）、`.zip`、`.mov`も同様である。判定はTLDの実在性だけで行う。

`.onion`、`.i2p`、`.bit`、`.exit`は委任TLDではないが指標として正当なので除外しない。

**3. 公開サフィックス単体**

`co.kr`、`ddns.net`など。サブドメイン（`mfahost.ddns.net`）は実際の指標なので残す。

**4. 到達不能・予約済みアドレス**

ループバック、RFC1918、ドキュメント用レンジ（`192.0.2.0/24`等の伏字）、マルチキャスト、
および公開DNSリゾルバ。ホストがIPアドレスのURLは指標として正当なので除外しない。

**5. ハッシュでない16進列**

マルウェア解析の資料には、逆アセンブル結果・PEヘッダのダンプ・シェルコード・スクリプトや
ファイル名の16進表現が普通に載る。これらがちょうど32/40/64/128桁で切り出されると、
長さだけではMD5/SHA-1/SHA-256/SHA-512と区別できない。`" run in DOS mode"`（PEのDOSスタブ）、
`" = Get-ChildItem"`（PowerShellの断片）、`c74424XX`の繰り返し（x86機械語）などが実例である。

判定は「ランダムな16バイト以上では確率的に起きえない特徴」だけで行う
（`ingest_observables.looks_like_hash()`）。

| 条件 | 本物で起きない理由 |
|---|---|
| ゼロバイトが20%以上 | 1バイトが`0x00`になる確率は1/256 |
| 同じバイトが4連以上 | 同上。ダンプのパディング由来 |
| 同じ3バイトの並びが3回以上 | 3バイトの空間は2^24 |
| 可読ASCII（`[A-Za-z0-9 _./$\-]`）が10バイト以上連続 | 文字列を16進化したものだけ |

**「16進文字の偏り」と「印字可能バイトの割合」を単独で使ってはならない。** MD5の長さ
（16バイト）では本物が誤爆する。印字可能75%以上では1883件のMD5から7件前後の本物が
引っかかる。閾値を長さごとに変える必要が出て脆くなる。

**3バイトの並びの条件を落としてはならない。** x86の`c74424XX`やRLO制御文字の繰り返しは、
ゼロ埋めでも同一バイトの連続でも可読文字列でもないため、この条件でしか捕まらない。

この判定は精度（弾いたものが誤検知だった）を確認しているが、再現率は測れていない。
暗号鍵の一部や圧縮済みデータの断片のようにランダムに見える16進列は、本物のハッシュと
統計的に区別できないため弾けない。

既存データの点検には`scripts/audit_hash_iocs.py`を使う（判定は
`ingest_observables.looks_like_hash()`をそのまま呼ぶ）。

**例外**

出典側で難読化されている値（`hxxps://github[.]com/...`）と、構造化IOC表から取り込んだ値は、
アナリストが指標として明示したものとみなし1.に関わらず残す。2.〜5.に例外はない。
とくに5.は値そのものが指標でないため、`disposition`が`confirmed`でも除去する。

攻撃者が正規サービスをペイロード置き場に使う場合（Kimsukyによる
`raw.githubusercontent.com`上の配布等）があるため、この例外は取込後の検証と
公開索引にも適用する。保存済みIndicatorでは難読化が正規化で消えているため、
観測側の`extraction_method`（`tech-memo-structured-csv`）と`raw_value`の難読化痕跡で
判定する（`ingest_observables.analyst_marked_indicator()`。
`validate_profile.py`と`../ui/build_portal_index.py`が共有する規則）。

`t.me`、`bit.ly`、`telegra.ph`、`webhook.site`のように攻撃者の実利用が多いサービスは、
参考リンクとしての出現があっても一覧に入れない。

既存データの点検には`scripts/audit_reference_iocs.py`と`scripts/audit_hash_iocs.py`を使う。
どちらも検出のみが既定で、`--apply`で`iocs.json`から除去する。除去後は生成物の再生成が
必要である。

### 8.1 Indicator

同じ正規化値は1件に集約する。

- `indicator_id`
- `type`
- `value`
- `normalized_value`
- `stix_pattern`
- `disposition`: `confirmed`、`candidate`、`rejected`
- `first_observed`
- `last_observed`
- `observation_count`
- `campaign_count`
- `seen_in_multiple_campaigns`
- `campaign_refs`
- `malware_refs`
- `infrastructure_refs`
- `roles`
- `observations`

### 8.2 Observation

1件の資料・位置・時点での観測を1イベントとする。

- 観測日時と精度
- 資料発行日
- `source_id`
- ファイル、ページ、シート、行、行番号、JSONパス
- 関連する攻撃活動
- 関連するマルウェア
- 関連するインフラ
- IOCの役割（C2、phishing、payload、download、exfiltration等）
- 抽出方式
- 文脈
- 確度

同じIOCが同じ資料の別ページにあれば別観測として保存する。完全に同一の資料位置・値だけを
重複排除する。

IOCの`roles`は、原典またはレビュー済み構造化表がその値の用途を明示する場合だけ保存する。
IP/domainだからC2、hashだからpayload、Campaignに含まれるからphishing等の型・包含による
推測は禁止する。役割は小文字の機械可読slug（`c2`、`payload`、`phishing-sender`等）とし、
自由文や原典行全体をroleへ入れない。複数Observationで異なる役割が確認された場合は、
Indicatorの`roles`をその和集合とし、各Observationにはその資料が直接支持する役割だけを残す。

OpenCTI出力ではIndicatorの標準`labels`とObservableの`x_opencti_labels`へ根拠付きroleを反映する。
同じatomic Observableは複数profileで共有されるため、Observable側のrole labelはコーパス全体の
観測用途の和集合とする。これは「いずれかの根拠付き観測でその用途だった」ことを表し、
永続的な悪性、現在の稼働、特定Actorへの排他的帰属を意味しない。文脈ごとのroleと根拠Sourceは
Indicatorおよび`Indicator ──based-on──> Observable` Relationshipへ保持する。

### 8.3 取りこぼし防止

抽出した候補は捨てず、確証がないものは`disposition: "candidate"`として保存する。
プレーンな一般ドメイン、メールアドレスは自動的にconfirmedへ昇格しない。

ただしこの原則は「指標になり得る値」に対するものである。8.0で挙げた値は指標に
なり得ないため、`candidate`として保存するのではなく取り込まない。確証の不足と、
そもそも指標でないことを混同しない。

### 8.4 日付

各Observationは必ず`observed_at`を持つ。不明でもオブジェクト自体を省略しない。
優先順位は次のとおり。

1. IOC表の観測日列
2. IOCと同一行・同一段落に明記された観測日
3. source manifestの`default_observed_at`（資料が観測期間を明示する場合のみ）
4. unknown

### 8.5 Hunting Pivot

`hunting_pivots`は、単発IOCとは別に、今後の検体・通信・公開インフラ調査で再利用できる
探索属性を保存する。証明書fingerprint/serial/subject、TLS fingerprint、コード署名、
driver、User-Agent、URI、port/serviceの組合せ、ASN/hosting傾向等が対象になり得る。
IOCが1件存在することだけではHunting Pivotへ複製せず、再利用性、特徴性、調査目的、
誤検知条件を説明できる場合だけ作成する。

Pivotの根拠に正確なfile hash、IP、domain、URL等の通常IOCが含まれる場合、Pivotは
`iocs.json`の代替にならない。同じ原典・Activity/Malware参照を持つIOC Observationも
構造化Sourceから生成し、その`indicator_id`をPivotの`indicator_refs`へ必ず追加する。
参照先IOC ObservationはPivotと同じ原典を持たなければならない。Pivot側では組合せ、
継続性、探索目的、誤検知条件を付加する。
証明書fingerprintを構造化IOCへ取り込む場合は`type: certificate-fingerprint`と
`hash_algorithm`（`md5` / `sha1` / `sha256` / `sha512`）を別々に保存し、file hashへ
分類しない。STIX X.509 patternのalgorithmはこの明示値から生成する。
ただし、hash algorithmが原典で不明な証明書fingerprint、証明書serial、per-device生成値、
複合的な挙動を推測したIOC型へ押し込んではならない。

各Pivotは最低限、次を持つ。

- `pivot_id`、`category`、`pivot_type`、`value`、`description`
- 機械表現できる場合の`stix_pattern`。per-device証明書設計や複合的な運用特徴など、
  単一の安全なpatternにできない場合は`null`
- `attribution_scope`、関連するmalware/infrastructure/activity/indicatorの参照
- `observations`、`first_observed`、`last_observed`
- `observation_count`、`source_count`、`activity_count`
- `continuity`、`hunt_queries`、`confidence`、`evidence_refs`、誤検知・留保

`observations[].count`は、その観測レコードが根拠付きで表すイベント数であり、必ず
`count_basis`（`documented-events`、`documented-samples`、`documented-hosts`、
`documented-observables`、`minimum-events`、`source-stated`、`unknown`）と組にする。
`observation_count`は各Observationの`count`の合計、`source_count`は一意な`source_ref`数、
`activity_count`はnullでない一意な`activity_ref`数とする。記事中の言及回数、ページ数、
同じReport sliceの数を攻撃件数へ変換しない。正確な件数が不明な「複数」は、根拠が許す
下限値と`minimum-events`のbasisを使う。数の含意もない1件の記述は`count: 1`、
`count_basis: unknown`として「1観測レコード」を表し、攻撃件数とは説明しない。

非nullの`observations[].activity_ref`はすべて上位`activity_refs`へ含め、すべての
`observations[].source_ref`は上位`evidence_refs`へ含める。Observation参照を件数計算だけに
使わず、STIX Noteのobject/evidence参照にも反映する。

`continuity.assessment`は過去の観測構造、`active_status`は評価日時点の利用状態であり、
互いに独立する。値は次の意味で使う。

- `single-observation`: Observationレコードが1件。レコード内countが複数でも継続観測ではない。
- `reobserved`: 同じPivotを独立した時点、資料またはtelemetryで2回以上確認した。
- `reused`: 原典が複数検体、hostまたは活動での再利用を明示した。
- `historical-only`: 根拠の対象期間が過去に限定されるが、現在未使用とは断定しない。
- `unknown`: 再利用性を評価できない。

受動検索を実行した場合は`continuity.checks`へ実行時刻、platform、query、index/time window、
結果件数・要約、analyst validation、根拠、限界を構造化する。`evaluated_at`は評価実施時刻であり
攻撃観測時刻ではない。`active` / `inactive`は検証済みcheckと根拠がある場合だけ使用する。
単一検索の0件だけで`inactive`にせず、廃止・撤去の明示または範囲を記録した反復確認が
なければ`unknown`を維持する。

Pivotの時間は活動観測の時間だけを`first_observed` / `last_observed`へ入れる。次は活動日ではない。

- X.509証明書の`notBefore` / `notAfter`（証明書の有効期間）
- Source公開日・アクセス日
- VirusTotal等の`first-seen` / first submission（そのサービスでの初回確認）
- Shodan/Censys等のscan時刻（公開サービス上のscan観測であり、攻撃実行時刻ではない）

上記は用途に応じた別フィールドまたはObservationの`basis`へ保存し、相互に代用しない。
現在も利用中であることを示すlive scan、現在のsample telemetry、または同等の明示的根拠が
なければ`continuity.active_status`は`unknown`とする。検索を実行していない場合は
`passive_scan_performed: false`とし、未検索を「現在観測なし」へ言い換えない。

issuer、subjectの一般名、ASN、hosting provider、CDN、正規サービスroot、汎用port、
offensive-security frameworkの既定値等はgeneric pivotであり、それ単独ではアクター固有の
Indicatorでも関係根拠でもない。既知SAN/fingerprint、URI、sample設定、観測時間等との
組合せ、必要な追加確認、誤検知条件を記録する。Shodan/Censys等の`hunt_queries`は候補生成用で、
`requires_validation: true`と具体的な`false_positive_notes`を必須とする。クエリ結果を
自動的にIOC、Infrastructure、Actor関係へ昇格しない。

## 9. 出典

Sourceには以下を持たせる。

- リポジトリ相対パス
- タイトル
- 発行者
- 発行日
- 言語
- 資料種別
- TLP／配布条件
- 信頼度
- ハッシュ（任意）
- 自由記述

ページ番号や行番号はObservationまたはEvidenceに保存する。
プロファイル本文で引用する主要資料は`actor-profile.json/sources`へ、IOC／artifact抽出専用の
全資料は`iocs.json/sources`にも自動保存する。検証時は両方のSource IDを有効とする。

## 10. 非IOC artifact

次の情報は`artifacts.csv`へ、1行1観測で保存する。

- `command`: 実行コマンド、PowerShell、cmd、シェルコマンド
- `sample-string`: 検体内の特徴的文字列、設定キー、暗号鍵、マーカー
- `pdb-path`: PDBパス
- `file-path`: Windows／Unixファイルパス
- `file-name`: 特徴的なファイル名
- `registry-key`: レジストリキー／値
- `mutex`: Mutex名
- `named-pipe`: Named Pipe
- `scheduled-task`: スケジュールタスク名
- `service-name`: サービス名
- `process-name`: プロセス名
- `user-agent`: User-Agent
- `uri-path`: C2のURIパス（完全URLはIOC）
- `email-subject`: フィッシング件名
- `lure-name`: 誘引文書名・テーマ
- `other`: 上記に収まらない重要artifact

CSVの配列列（`campaign_refs`等）はJSON配列文字列として保存する。
`artifact_id`はtypeと正規化値から安定生成し、`observation_id`は値・資料・位置から生成する。
同じartifactが複数攻撃で見つかった場合、全該当行で`seen_in_multiple_campaigns=true`、
`campaign_count`を一意な攻撃数にする。

`artifacts.csv`の列順は`schemas/artifacts-csv-columns.json`を正とする。

## 11. STIX出力

- Actor: `intrusion-set`
- 関連企業: `identity`（`identity_class: organization`）
- 関連自然人: `threat-actor`（OpenCTIではThreat Actor Individualとして明示）
- 関連Threat Actor Group: `threat-actor`（OpenCTIではThreat Actor Groupとして明示）
- 法的措置: 対象entityを参照する`note`
- Malware: `malware`
- Tool: `tool`
- Infrastructure: `infrastructure`
- TTP: `attack-pattern`
- Activity: 明示した`stix_object_type`に従い`campaign`、`incident`、`grouping`
- Targets/attribution organizations: `identity`
- IOC: `indicator`と対応する原子的SCO。OpenCTI取込用Bundleでは同じ正規IOCレコードから
  生成した両者を`Indicator ──based-on──> Observable`で直接結ぶ
- Hunting Pivot: STIX patternがある場合は`indicator`と`note`、ない場合は`note`のみ。
  exact値を安全に実体化できるpatternでは対応SCOと`based-on`も生成する
- 観測: `observed-data`と`note`、またはIndicatorの外部参照
- 関係: `relationship`

STIXに直接表しにくい精度、証拠、自由記述は`x_`カスタムプロパティとして保持する。

正規データの`entity_relationships.relationship_type`は、`employed-by`、`founder-of`、
`officer-of`、`member-of`、`supports`、`front-company-for`等の根拠に合う意味を保持する。
OpenCTIがその動詞を安全に受理できない場合、STIX出力では`relationship_type: related-to`へ
フォールバックし、元の動詞を`x_profile_relationship_type`、正規Relationship IDを
`x_profile_relationship_id`へ保存する。説明、確度、出典、観測期間も保持し、互換性のために
意味や証拠を捨てない。OpenCTIで受理できることを理由に、正規データ側の動詞を最初から
`related-to`へ弱めてはいけない。

`artifacts.csv`の非IOC artifactは、該当するSCOへ安全に変換できる場合だけSTIXへ含める。
変換できないコマンドや文字列は、STIX `artifact` SCOへ無理に格納せず、`note`または
カスタムプロパティで参照する。

### 11.1 OpenCTI取込用Bundle

OpenCTI向け出力は`opencti/actors/`のアクター単位Bundle、
`opencti/campaigns/<actor>/`のCampaign Bundle、`opencti/activities/<actor>/`の
Incident/Grouping Bundleへ分割する。

- Actor BundleはActivityを含めず、アクター全体の知識とActivity未割当IOCを保持する。
- 各Activity Bundleは主となるCampaign/Incident/Groupingを明示し、同じ活動へ明示参照されたオブジェクトだけを
  含める。アクター一般の利用実績から活動別マルウェア、TTP、標的を補完しない。
- 各Bundleは`created_by_ref`、Relationshipの両端、Reportの`object_refs`をBundle内で解決し、
  標準TLP marking以外の参照切れを許可しない。
- 複数Bundleへ同じSTIX IDを含める場合、そのSDO/SCOは`created` / `modified`を除く意味内容も
  同一にする。プロファイル固有の説明・出典・期間を共有IDの本体へ混在させず、Relationship、
  Noteまたはprofile-scoped IDへ置く。
- Reportの`object_refs`にはRelationshipも含め、OpenCTI上で知識コンテナとして確認できるようにする。
- 国・地域は`Location`、産業・役割は`identity_class: class`の`Identity`へ変換する。
- 国は`reference/opencti-country-index.json`で固定したOpenCTI公式Countryの英語名、
  ISO 3166-1 alpha-3コード、座標、aliasへ照合する。一致しない国コードは推測しない。
  公式IDは参照値として保持する。actor-specificな標的説明と出典は、重複排除される
  Country本体ではなく、そのCountryを対象とするRelationshipへ移す。
- アクター関係の対象をcanonical名、Profile ID、根拠付き`exact` aliasで一意に解決できない場合、
  新しいIntrusion Setを推測生成しない。元関係は`Note`とmanifestへ残す。
- Activity割当済みIOCは該当Activity Bundleへ、未割当IOCはActor Bundleへ収録する。
- 非rejectedの原子的IOCは値ごとの安定SCOとして出力し、対応Indicatorから`based-on`を直接結ぶ。
  Network Observableに明示的な`infrastructure_refs`がある場合だけ、別途Infrastructureから
  `consists-of`を結ぶ。ファイルハッシュはFile SCOへ変換するがInfrastructureへ自動所属させない。
  実観測日時がない`consists-of` Relationshipへ公開日由来の`start_time`/`stop_time`を付けない。
- Relationshipへ`start_time`を出力する場合はOpenCTI取込互換性のため`stop_time`も必須とする。
  実際の終了時刻が不明なら`stop_time = start_time`とし、暫定補完フラグとbasisを付ける。
  `x_last_observed`はunknownのまま保持し、暫定値を実観測の終了日時として解釈しない。
- 公開日が判明するSourceは原典Reportとして`Report.published`を保持する。公開日不明のSourceへ
  profile更新日時等を代入しない。
- OpenCTI既定の50 MiB取込上限を下回るよう、生成時の上限は45 MiBとする。

OpenCTI表現規則だけを変更した場合、全profileが同日に新しいOSINTを得たかのように
`updated_at`を一括変更しない。`build_opencti_bundles.py`の`OPENCTI_MODEL_MODIFIED`を進め、
意味内容が変わるIndicator、Relationship、Report等の`modified`だけを進める。既存IDの
`created`は旧版から保持し、意味内容が不変なobjectの`modified`も不要に変更しない。

## 12. 検証の重大度

- Error: 必須項目欠落、重複ID、参照切れ、不正日付、IOC集計不一致、STIX参照切れ。
- Warning: 証拠なし、日付不明、aliasスコープ不明、候補IOC、自由記述のみの重要項目。
- Info: 改善可能だが有効なデータ。

`--strict`ではWarningも終了コード1とする。

## 13. OSINTによる主張検証

OSINTはプロファイル本文への追記だけで終わらせず、各プロファイルの
`claim-audit.json`へ主張単位で保存する。

`verification_status`は次のいずれかとする。

- `supported`: 信頼できる情報源が主張とそのスコープを支持する
- `partially-supported`: 主体・時期・範囲の一部だけを支持する
- `contradicted`: 信頼できる情報源が主張を明示的に否定する
- `unresolved`: 根拠不足、または情報源間のスコープ差を解消できない
- `superseded`: 後続情報により古い評価として置き換えられた

検索結果のスニペットだけを最終根拠にしない。政府機関、司法資料、制裁指定、
公式ATT&CK、当該ベンダーの一次調査を優先し、発行日とアクセス日を分けて記録する。
反証が見つからないことを「反証なし」と断定せず、検索範囲と未解決点を残す。

claim auditはalias、帰属国、関係、主要malware/TTPだけに限定しない。少なくとも
`actor.actor_types`、`attribution.sponsor_type`、帰属組織、motivation、activity、
victim case、target、全capability区分、TTP、key judgmentを個別のclaimとして監査する。
根拠参照が空の主張を既定で`partially-supported`にしてはならず、`unresolved`とする。

`state-sponsored`は特に強い主張として扱い、actor-specificなスポンサー関係の明示を
必要とする。一般的な国・originラベルは根拠にしない。外部taxonomyを使う場合も、その
taxonomy自身が対象区分をnation-state actorとして明示し、canonical名または`exact`
aliasが一致するときだけ使用する。`overlapping`、`related`、`broader`、`narrower`の
alias一致から国家支援を継承しない。`state-aligned`の根拠しかない場合、
`state-sponsored` claimは最大でも`partially-supported`である。

アクター関係は、最低でも次を分離する。

- 組織関係: `part-of`、`subordinate-to`
- 運用関係: `cooperates-with`、`successor-of`
- 観測上の共有: `shares-tools-with`、`shares-infrastructure-with`、
  `shares-targeting-with`
- ベンダー分類上の関係: `overlaps-with`、`related-to`

共有aliasだけの関係は候補・低信頼度とする。一次資料が「partial overlap」
と述べる場合、`exact`な同一性へ強めない。別部隊間の協力はalias統合の根拠にしない。

## 14. 全件OSINTクロスチェック

各アクターには`osint-crosscheck.json`を必須とし、固定した公開データセットすべてに
対して、正規名、既知alias、MITRE Group IDを照合する。

`overall_assessment`は次の意味で使う。

- `matched`: 正規名、MITRE ID、または複数名の交差で高信頼度の一致がある
- `possible-match`: 単一aliasだけが一致し、スコープ確定に原典確認が必要
- `needs-review`: 帰属国が排他的に衝突する、またはcanonical anchorのない複数一致
- `no-match`: 固定データセットをすべて検索したがexact一致がない

`no-match`を未調査扱いに戻さない。また、外部データセットの情報を自動的に
正規aliasや帰属へ昇格しない。MISP、ETDA等の集約データは原典URLを保持し、
taxonomyの`similar`関係は低信頼度の関係候補として保存する。

国、スポンサー、組織帰属が競合する場合は、既存値を黙って上書きしない。
旧主張を`contradicted`または`superseded`として主張台帳に残し、直接観測した
政府・CERT・ベンダー資料と、単なるワークブック配置や二次集約を区別する。

Malpediaとの名前一致はマルウェアのカタログ存在だけを意味し、そのアクターが
使用した証拠にはしない。

## 15. 全アクター調査票

全active actorに`generated/research-dossier.json`を生成し、少なくとも関係アクター、
活動時期、活動別malware、標的、動機、帰属、各主張の根拠参照とclaim audit結果をまとめる。
値が存在しない次元は空欄を推測で埋めず、`unknown`と`research_gaps`で明示する。

ETDA、MISP、TIDAL等の集約データから得たcampaign、software、標的、動機、帰属候補は
`external_research_leads`に隔離する。集約データの日付は、原典を確認するまで確定観測日と
せず、`inferred`または報告日として保存する。canonicalへの昇格には、actor scope、
entity種別、活動との結び付き、観測期間を原典で確認したevidenceが必要である。


## 16. 生成・エージェント用ガードレール

自動生成、エージェント更新、日次取込、OSINT補完のすべてで次を必須とする。詳細と
具体例は[GENERATION_RULES.md](GENERATION_RULES.md)を参照する。

1. **地理情報から国家支援を推定しない。** 国別worksheet、origin、言語、IP所在地、
   被害地域、インフラ所在地は`state-sponsored`、`sponsor_type: state`の根拠ではない。
2. **国家支援から動機を推定しない。** `state-sponsored`であってもespionage、
   disruption、destruction、financial gainなどは別主張であり、個別の証拠を要求する。
3. **製品・ベンダーと攻撃実行主体を分離する。** 「X社の製品／exploitをYが使用した」
   場合、原則としてadversaryはYでありXではない。X自身の攻撃実行を示す証拠が必要。
4. **Actor、Organization、Software、Malware、Campaign/Operationを混同しない。**
   同名ブランドが複数entity種別に存在する場合は、スコープを明記して別IDで保持する。
5. **alias一致を同一性へ自動昇格しない。** canonical/aliasの重複はレビューキューへ送り、
   `exact`はベンダー境界と原典を確認した場合だけ使用する。
6. **低確度・未解決主張を高確度フィールドへ昇格しない。** `unresolved`、
   `partially-supported`、単一の集約データセットだけの値は、追加根拠なしに
   attributionやmotivationの確定値へ変換しない。
7. **自動生成は保守的に失敗させる。** 根拠がなければ`unknown`または空配列を選び、
   「もっともらしい補完」をしない。

これらは品質上の必須条件であり、コード変更時は回帰テストを追加する。
