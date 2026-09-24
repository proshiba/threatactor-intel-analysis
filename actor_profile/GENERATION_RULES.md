# Actor Profile Generation Rules

この文書は、`actor_profile/`と`profiles/`を自動生成・更新するスクリプトおよび
AIエージェント向けの必須ガードレールです。一般的なデータ規約は
[RULES.md](RULES.md)、OSINT検証は[OSINT_RULES.md](OSINT_RULES.md)を参照してください。

## 1. 最優先原則

自動化は「情報を埋めること」より「誤った断定をしないこと」を優先します。
根拠が足りない場合の正しい値は`unknown`、空配列、またはレビュー待ちです。

## 2. 地理情報と帰属を分離する

次は国家支援の証拠ではありません。

- 国別worksheetへの配置
- actorのorigin / country label
- 使用言語、タイムゾーン、キーボード
- C2・VPN・VPS・WHOISの所在地
- 被害国・標的国
- 開発者や逮捕者の国籍・居住地

これらだけを理由に`state-sponsored`、`state-aligned`、
`sponsor_type: state`を設定してはいけません。

国家支援を構造化するには、政府共同勧告、公式帰属、MITRE ATT&CKのactor-specificな
明示記述、または複数の独立した高品質資料など、スポンサー関係そのものを述べる証拠を
必要とします。

### 禁止例

```text
Russia worksheet
→ Russian actor
→ state-sponsored
→ espionage
```

この連鎖はすべて禁止です。

### 帰属国を標的国へ流用しない（活動記述からの自動構造化）

`enrich_activity_intelligence.py`の`actor_attribution_context()`は、活動記述に現れる
国名のうち実行主体側を指すものを標的候補から除外します。除外する日本語の語形は
次のとおりで、いずれも被害側の表現とは助詞または連結の形が異なります。

| 語形 | 例 | 被害側の形 |
|---|---|---|
| `X系`、`X関連`、`Xの国家支援` + 主体語 | 北朝鮮系ハッカーグループ | 日本の政府機関 |
| `X` + `サイバー攻撃/犯罪/諜報` + 主体語 | 北朝鮮サイバー攻撃グループ | — |
| `Xを背景とする／した` | 北朝鮮を背景とするグループ | — |
| `XIT労働者`（助詞を挟まない連結） | 北朝鮮IT労働者 | 日本のIT労働者 |
| `Xによる攻撃/侵害/諜報` | 中国によるハッキング | 日本への攻撃 |
| `Xからの圧力/制裁/要求` | 米国からの圧力 | 米国の重要インフラ |
| `X人 N人`（国籍付きの人数） | イラン人17人を起訴 | 日本人を標的 |

語形を追加するときは、被害側の表現を巻き込まないことを確認し、
`actor_profile/tests/test_activity_intelligence.py`へ肯定・否定の両方の回帰テストを
同じ変更に含めてください。国名が囮・デコイの主題を示すだけの場合も標的国にしません。
ただし、`targeted North Korea with a lure`や`日本を狙う囮文書`のように、標的動詞が
当該国を直接目的語・被害範囲として支配する場合は被害側として保持します。別の国を標的に
当該国を題材とする`targeted Japan using North Korea-themed lures`は北朝鮮を保持しません。

英数語の産業語はword boundaryを必須とし、`Darkhotel`の中の`hotel`のような
部分一致を産業として扱いません。カタカナ国名もカタカナ語境界を要求し、
`タイ`を`リアルタイム`・`タイポスクワッティング`・`ワンタイム`から、`シリア`を
`デシリアライズ`から抽出しません。
国名が`Japanese-made`、`German-built`、`中国製ルータ`、`日本語版`のように製品の製造国・
開発元・言語だけを修飾する場合も、被害組織の所在を示さないため標的国にしません。
日本語の`製`は既知の製品名詞または単独の`X製`に限って製品由来と判定し、`中国製薬会社`や
`中国製造拠点`の`製`を製品原産地の接尾辞として扱いません。
`China Chopper`のように国名を含むマルウェア・ツール・製品の固有名も、名称中の国名だけを
標的国へ昇格しません。同じ活動が当該国の組織を明示的に標的としている場合は、その別の
被害記述を根拠として保持します。

C2、VPS、プロキシ、トンネル等が攻撃者側の所在・経由地として明示された場合は標的国にせず、
同じ文にある明示的な被害国だけを保持します。一方、`targeted servers in Germany`、
`critical infrastructure in Ukraine was attacked`、標的機器が`インドに所在`のように、
サーバ、ホスト、インフラまたは機器そのものが被害資産である場合は、その国を保持します。
単に`server/infrastructure/host in X`または`Xに所在`という語形だけで攻撃者側インフラと
決めません。

攻撃インフラの停止、差し押さえ、テイクダウン等に協力した政府・法執行機関の国も、
その役割だけでは標的国にしません。同じ資料が当該国の被害を別途明示する場合は、協力者としての
言及ではなく、その被害記述を根拠として保持します。

この囮、製品原産地、言語、インフラ所在の除外規則はActivity本文だけでなく、MITRE ATT&CKの
Group概要から標的を生成する経路にも同一に適用します。見出しの省略表現や企業名のために
役割を機械判定できない既知Activityは`activity_target_exclusions`へ根拠とともに明示し、
同じ国の別Activityや明示的な被害国をアクター全体で一括除外しません。

既存プロファイルの自動生成targetは生成IDを基準に再生成時に除去・再評価します。
旧処理でcanonical IDへ変換されたものは、旧自動生成文言と
`[targeting-scope-audit-v1]`の両方が残る場合だけ除去します。導出マーカーは監査根拠を
既存の手動targetへ追記する場合もあるため、マーカー単独を所有権や削除条件にしません。

## 3. 国家支援と動機を分離する

国家支援の有無と、作戦目的・動機は別の主張です。

`state-sponsored`から自動的に`espionage`を生成してはいけません。
国家系アクターでも、諜報、破壊、妨害、影響工作、資金獲得など複数の目的があり得ます。
motivationはactor-specificな本文が明示した範囲だけを記録します。

## 4. Vendor / Product / Operator / Adversaryを分離する

記事中に企業名や製品名が出たことは、その企業が攻撃主体であることを意味しません。

例:

```text
Serbian authority used a Cellebrite exploit/product against a device
```

この場合、攻撃実行主体として検討するのはSerbian authority側です。
Cellebriteはvendor/developerとして関係を記録できますが、同社自身が侵入を実行したと
示す別証拠なしにDiamond ModelのAdversaryへ置いてはいけません。

同じ規則を、RMM、EDR、offensive-security tool、spyware platform、exploit broker、
cloud/CDN、hosting providerにも適用します。

## 5. Entity種別を先に決める

新しいcanonical profileを作る前に、対象が次のどれかを確認します。

- Threat Actor / Intrusion Set / Activity Cluster
- Organization / Government Unit / Company
- Malware / Ransomware / Tool / Software
- Campaign / Operation
- Infrastructure / Service

同じ名称が複数の意味で使われる場合は統合せず、スコープを分けます。

例: REvilは文脈によってransomware/software family、RaaS brand、operatorsを指します。
既存のGOLD SOUTHFIELDのようなoperator profileがある場合、software名とactor名を
機械的に同一化してはいけません。

schema 1.4.0で実在する企業・自然人または人間の集団を追加するときは、既存Actor profileを
置き換えず`associated_entities`へ保存します。

- 企業その他の法人は`organization--...` / `entity_type: organization`とし、OpenCTIでは
  Organizationへ変換します。
- 攻撃実行、指揮、開発、仲介等へ関与した実在自然人は
  `threat-actor-individual--...` / `entity_type: threat-actor-individual`とし、OpenCTIでは
  Threat Actor Individualへ変換します。
- 犯罪シンジケート等、人間の集団として根拠付きで識別された対象は
  `threat-actor-group--...` / `entity_type: threat-actor-group`とし、OpenCTIでは
  Threat Actor Groupへ変換します。既存Intrusion Setと名前が重なっても別objectにし、
  根拠が部分一致なら`overlaps-with`等で結びます。
- APT名、ベンダー追跡クラスタ、部署を、実在企業や自然人へ名前一致だけで置換しません。
- 同じ実在entityまたはSourceを複数profileへ再掲する場合は同じ安定IDと同一定義を使います。
  profile固有の関係・役割・期間はentity本体でなく`entity_relationships`へ置きます。

### 企業・個人・攻撃クラスタの関係

`entity_relationships`は原典が直接支持する最小の関係だけを保存します。次の推論は禁止です。

```text
個人 employed-by 企業
企業 supports APT-X
→ 個人 member-of APT-X
```

勤務、役員、創業、株式保有、委託、支援、指揮、クラスタ参加はそれぞれ別の主張です。
雇用関係が確認できても、本人による当該APT活動への参加を示す証拠がなければ
`member-of`や`operates`を生成しません。逆に、個人のAPT参加が確認できても、推測した
勤務先や政府組織を補いません。

関係の向きは、個人から勤務先・所属先、支援企業から支援対象、tasking組織からtasked対象を
基本とします。原典がalleged/assessed/likelyと述べる関係を確定動詞へ強めません。

### 起訴・制裁等の法的情報

法的措置は`associated_entities[].legal_actions`へ保存します。起訴または訴追の事実を
記録する場合でも、起訴状中の行為は未確定の主張なので`action_type: indictment`または
`charge`、`status: alleged`とします。政府資料の信頼度が高いことと、被告人の有罪が
確定していることを混同しません。制裁、逮捕、有罪判決、量刑は別actionとして保持します。

`legal_actions[].action_date`、Sourceの`published_at`、entity・Relationshipの
`first_observed` / `last_observed`、Activityの期間は相互に代用しません。例えば起訴日を
攻撃の`last_observed`へ、制裁日をAPT membershipの開始日へコピーしてはいけません。


### Entity境界の追加ルール

- MITRE ATT&CKでSoftware/Malwareとして管理される名称を、名前一致だけでcanonical Actorにしてはいけない。
  例: GravityRAT(S0237)、Shamoon(S0140)。Operator/clusterは別entityとして追跡する。
- Malware名が歴史的にoperatorの通称として使われる場合も、softwareとactorの両スコープを
  同一profileへ混在させず、legacy profileはdeprecated化し、根拠のあるActor名へ分離する。
- 広域scheme/ecosystemとvendor-specific named adversaryをexact aliasにしない。
  DPRK IT Worker Schemesのような上位ecosystemとFAMOUS CHOLLIMAのようなvendor追跡Actorは
  `related-to` / `overlaps-with`等のrelationshipで結ぶ。
- `actor-census-curation.json`の`exclude`/`override`を使い、次回census materializationで
  software名や誤aliasが再びcanonical Actorへ戻らないようにする。
- ATT&CKの同一Group IDでvendor renameがAssociated Groupとして確認できる場合は、
  rename後の名称を第二のcanonical Actorとして残さず、`merge`で既存のstable profileへ
  統合する。統合元のactor-scoped evidenceは統合先の`source_dirs`へ引き継ぎ、既存profileは
  stable ID互換のため`deprecated` tombstoneとして残す。
- ATT&CK Softwareと同名の候補は、命名元の原典が独立したoperator/groupも同名で追跡して
  いる場合を除きActor化しない。Zebrocyのように原典が明示的にmalware/toolsetとし、別の
  groupが運用すると述べる名称は`exclude`する。
- deprecated profileをSTIXへ出力する場合、`intrusion-set`に`revoked: true`と
  `x_profile_status: deprecated`を付け、active entityとして再利用されないようにする。

## 6. Workbookからのalias抽出

`APT Groups and Operations.xlsx`等のmapping workbookでは、alias候補として扱う列を
**allowlist**する。`Common Name`、`Other Name(s)`、`Alias(es)`のような明示的な
名前列だけを使用し、Country / Origin / Sponsor / Attribution / Comment / Description /
Targets / Operation / Toolset / Malwareなどをaliasへ流用してはいけない。

複数aliasを含む名前セルは`,`、`;`、改行、区切りとしての` / `で分割する。
国名単体、帰属説明文、スポンサー説明文、地域説明などはaliasではない。

元Workbookは本リポジトリに保持しないため、既存profileの補正では
`actor_profile/scripts/migrate_workbook_aliases.py --apply`を使用し、
`actor-mapping-workbook`だけを根拠とするaliasを除去する。MITRE、catalog、
actor-specific source由来のaliasは保持する。元Workbookを利用できる生成環境では、
上記allowlist列だけからaliasを再抽出する。

## 7. Aliasと重複プロファイル

canonical nameとaliasの正規化一致を検出したら、自動統合ではなくレビュー対象にします。

特に次を確認します。

1. 同じ一次資料・同じcampaignを指していないか
2. MITRE IDなど安定IDが同じではないか
3. 一方がbroader/narrower/overlappingなvendor clusterではないか
4. 会社名、malware名、operation名の同名衝突ではないか

先頭の`The`、空白、ハイフン、大小文字だけの差は重複候補として扱います。
同一プロファイル内で正規化後に同じになるaliasは、先に現れた根拠付き表記を残して
materialization時に重複排除します。

OpenCTI向け生成では、`scope: exact`かつ`confidence: high`だけをIntrusion Setの標準
`aliases`へ出力します。OpenCTIは`name OR alias`を重複排除へ使用するため、
`overlapping`等を標準aliasに平坦化すると別クラスタが誤統合されます。非同一性aliasは
`x_alias_assessments`とprofile-scoped Noteへ出力し、名称、vendor、scope、confidence、
`evidence_refs`、留保を保持します。`x_opencti_aliases`はscopeを表現する標準属性ではなく、
非exact名称の退避先として使用しません。

alias生成・移行は次をfail closedで検証します。

1. 必須6フィールドと列挙値がschemaに一致すること。
2. canonical名との自己alias、正規化後の重複、出典切れがないこと。
3. active profile横断でcanonical名とOpenCTI同一性aliasが衝突しないこと。
4. Actor名がSoftware/Malware、Campaign/Operation、Organization、Individualではないこと。
5. 公式mappingの対応を別ベンダーの帰属・活動・能力へ推移させないこと。

## 8. Claim auditからの昇格条件

`unresolved`または`partially-supported`は「誤り」とは限りませんが、
自動生成が確定的なattribution/motivation/exact aliasへ昇格させる根拠にはできません。

重要主張の自動昇格には、少なくとも以下を満たします。

- actor-specificな証拠である
- source scopeが主張のscopeと一致する
- entity種別が一致する
- contradictionが未解消ではない

`build_claim_audits.py`は、identity/alias/relationshipに加えて、actor type、sponsor type、
帰属組織、motivation、activity、victim case、target、全capability区分、TTP、key judgmentを
監査対象にします。参照がない主張は`unresolved`、集約資料またはrepository内取込だけを
根拠とする主張は原則`partially-supported`です。
deprecated profileの台帳は過去の主張を現行主張として残さず、`superseded`の
lifecycle claim 1件だけを保持し、現行コレクション集計から除外します。

`state-sponsored`の自動支持は次のいずれかに限定します。

- actor-specificな証拠を持つ`attribution.sponsor_type: state`
- actor-specificなMITRE ATT&CK記述が国家支援を明示する
- nation-state区分であることを明示した外部taxonomyにcanonical名または`exact` aliasが一致する

国・originの値だけ、非exact alias、`state-aligned`だけでは`state-sponsored`を
`supported`にしません。

## 9. Source precedence

自動化の既定優先順位:

1. 政府・法執行機関・CERT等の一次資料
2. MITRE ATT&CK等、原典参照を持つactor-specific knowledge base
3. ベンダーのactor-specific technical report
4. 複数資料を集約したOSINT dataset
5. mapping workbook / naming list / search snippet

4と5は候補生成・cross-checkには使えますが、それ単独で国家支援や動機を確定しません。

同じ原典を複数の構造化evidence fileへ分ける場合、それらは同じ`source_id`を共有できる。
`ioc-sources.json`の各entryはpath、field mapping、観測refsを保持したまま全件処理し、
`iocs.json.sources`のSource metadataだけを`source_id`単位で1件へ集約する。代表`path`に加えて
全ローカルpathを`evidence_paths`と`analyst_notes`へ残し、再ingestで出典経路を失わない。
共有ID間の`published_at`、`confidence`、`tlp`は同値、またはunknownから既知値を補完できる場合だけ
統合する。複数の既知値が競合する場合は、最初のevidence fileを開く前に取込全体を停止し、
どちらかを推測採用しない。異なる`source_id`の非移行entryは従来どおり別Sourceとして保持する。

## 10. Census curation

`actor-census.json`からの自動materializationでentity種別や重複を安全に解決できない場合は、
`actor_profile/actor-census-curation.json`へ人手補正を記録します。

- `exclude`: software/brand等をcanonical Actorとして生成しない
- `merge`: census identityを既存profileへ統合する
- `override`: canonical名、stable slug、alias、actor typeを根拠付きで補正する

各ruleには`reason`と`evidence_urls`を必須とし、再生成時も自動推定よりcurationを優先します。
既存profileのstable IDを維持する必要がある場合は`slug`を明示します。

## 11. Hunting Pivotの生成

`hunting_pivots`はIOC一覧の別表示ではない。生成処理は、すべてのIOC、証明書、ASN、port、
driver名を一律にPivotへ昇格してはいけない。原典が探索上の特徴を説明しているか、複数時点・
複数活動での再利用が確認されているか、または単発でも防御的な再検索方法と誤検知条件を
明示できる場合に限って候補を作る。単発のIP/domain/hashそのものは`iocs.json`に保持する。

Pivotに正確なfile hash、IP、domain、URL等が含まれる場合、その原子的な値は構造化Sourceから
通常のIOC Observationにも取り込み、生成された`indicator_id`をPivotの`indicator_refs`へ
必ず追加する。参照先IOCとPivotは同じ原典を共有しなければならない。Pivotだけにhashを
埋め込んで`iocs.json`から欠落させない。
証明書fingerprintは`certificate-fingerprint`として取り込み、原典が明示した
`hash_algorithm`からX.509 patternを生成する。SHA-1 thumbprintをfile SHA-1へ、または
algorithm不明のfingerprintやserialをX.509 SHA-256へ誤変換してはならない。
heuristic抽出済みの値を原典レビューで誤分類と確認した場合は、該当Source manifestの
`excluded_iocs`に元のtype、値、理由を記録し、正しい型の構造化Sourceへ移す。値だけを
無言で削除したり、actor全体の同値IOCを一律に抑止したりしない。

生成・集計時は次を守る。

1. Observationごとの`count`と`count_basis`を保持し、`observation_count`はcountの合計とする。
   行数・引用数・ページ数をイベント数にしない。単位が明示されない既定値は`unknown`とし、
   `documented-events`へ自動昇格しない。
2. `source_count`は一意な`source_ref`、`activity_count`は一意な非null `activity_ref`から算出する。
   同じ原典のBundle sliceや同じ活動の再掲を別件として数えない。Observationの非null
   `activity_ref`と`source_ref`は、それぞれ上位`activity_refs`と`evidence_refs`にも含める。
3. 証明書の有効期間、Source公開日、VirusTotal等のfirst-seen、scan時刻を攻撃活動日へコピーしない。
   時間の意味を`basis`に残し、活動時点が不明ならunknownのままにする。
   構造化Sourceが`observed_at`列を明示的にmappingしている場合、空セルはunknownである。
   CSV行全体へ日付regexを再適用してcampaign IDやsource ID中の年を観測時刻へ補完しない。
   明示的な`default_observed_at`があるSourceだけ、その既定値を使用できる。
4. live scanまたは現在のtelemetryを実際に確認していない限り、
   `continuity.active_status`を`active`へしない。既定は`unknown`であり、検索未実施なら
   `passive_scan_performed: false`とする。検索を実施した場合は`continuity.checks`へ実行時刻、
   platform、query、index/time window、結果、analyst validation、根拠、限界を保存する。
   `reused` / `reobserved`は過去の観測構造であり、現在の`active`を意味しない。単一の0件検索を
   `inactive`の根拠にしない。
5. issuer、ASN、hosting provider、CDN、port、正規サービス、Cobalt Strike等の汎用特徴を
   actor-specificへ自動昇格しない。複合条件と追加検証が必要なgeneric pivotとして扱う。
6. Shodan/Censys等の検索式は自動スキャン命令ではなく、analyst向け候補生成式である。
   `requires_validation: true`と`false_positive_notes`を必須にし、field schema変更も確認する。
7. 同じPivot値の共有はActor同一性・協力・帰属を意味しない。必要ならGroupingへ観測集合として
   含めるが、追加証拠なしにActor Relationshipを生成しない。

通常IOCのrole labelも同じ証拠境界に従う。生成処理は`iocs.json`のIndicator/Observationに
構造化された`roles`だけをIndicatorの`labels`とObservableの`x_opencti_labels`へ変換する。
値の型、Infrastructure/Campaignとの共存、Actor一般のTTP、文脈中の曖昧な単語から`c2`、
`payload`等を補完しない。自由文はlabel化せず、原典の文脈またはanalyst notesへ残す。
共有SCOのlabelは全profileとStandalone Activityの和集合を事前計算し、部分生成でも同じSTIX IDが
同じ定義になるようにする。各Indicator固有のroleとSource参照は`based-on` Relationshipにも残す。

STIX生成では、安全な`stix_pattern`があるPivotをIndicatorとNoteの両方へ変換し、観測・件数・
continuity・query・留保をNoteにも完全に残す。exact equalityで値を実体化できるpatternは
対応SCOと`based-on`も生成する。patternが`null`の複合特徴、per-device生成証明書、再現不能な
設計特徴はNoteだけにし、wildcardや複合patternから架空のSCO、fingerprintを作らない。
この生成ロジックを変更するときは、単発IOCとの分離、count集計、unknown active status、
generic pivot、Indicator/Note境界の回帰テストを同じ変更へ含める。

OpenCTI Bundleの分割では、同じSTIX IDへ異なるprofile固有description、evidence、観測情報を
載せてはいけない。TTP観測、Indicator assertion、Capability、Activity、標的・被害等のclaimは
profile namespaceの安定IDにし、共有するCountry・entity・atomic SCOはprofile固有情報を除いた
同一objectとして再利用する。Actor Relationship endpointは対象profileの完全なActor objectを
再利用し、簡略stubで同じIDを上書きしない。NoteをBundleごとに参照縮約する場合はslice固有IDを
使う。生成後は全Bundle横断で同一IDのbyte同一性を検証し、差分をfirst-winsで隠さずerrorにする。

## 12. Agent preflight checklist

プロファイルまたは生成コードを変更するエージェントは、commit前に次を確認します。

- [ ] country/originをsponsorshipへ変換していない
- [ ] state-sponsoredをespionageへ変換していない
- [ ] vendor/productをadversaryへ変換していない
- [ ] software/campaign/organizationをactorとして新設していない
- [ ] 企業をOrganization、根拠付きで識別した自然人をThreat Actor Individualとして分離した
- [ ] 雇用・役員・創業関係からAPT membershipを推論していない
- [ ] indictment / chargeを`status: alleged`として扱い、有罪認定と混同していない
- [ ] 法的措置日を活動日・entity関係期間へコピーしていない
- [ ] ActivityごとにCampaign / Incident / Groupingを明示し、全件Campaign化していない
- [ ] Groupingの`object_refs`から未立証Relationshipを生成していない
- [ ] 非rejectedの原子的IOCについて、Indicatorと対応Observableを直接`based-on`で結び、
      Infrastructureの有無に依存させていない
- [ ] 根拠付きIOC roleをIndicator/Observableのlabelへ反映し、`based-on`にroleとSource参照を残した
- [ ] 型や共存関係だけからC2/payload等のroleを推測していない
- [ ] 共有Observableのrole labelをコーパス全体で統一した
- [ ] Source公開日を観測時刻やRelationship期間へコピーしていない
- [ ] Relationshipへ`start_time`を出す場合は`stop_time`も出し、終了不明の同値補完へ
      `x_stop_time_is_fallback`とbasisを付けた
- [ ] IOC共有を時刻なしの強い相関・同一Actor根拠として扱っていない
- [ ] 単発IOCを理由なくHunting Pivotへ複製していない
- [ ] Pivotのcount basisとsource/activity countを別々に集計した
- [ ] 証明書有効期間・公開日・VT first-seen・scan時刻を活動日へ転用していない
- [ ] live evidenceなしに`active_status: active`としていない
- [ ] generic issuer/ASN/service/portをactor-specificとして扱っていない
- [ ] Shodan/Censys queryをanalyst validation必須としている
- [ ] alias一致だけでexact identityにしていない
- [ ] unresolved/partial claimを確定値へ昇格していない
- [ ] actor-specific evidence_refが重要主張に付いている
- [ ] canonical/alias重複候補を確認した
- [ ] 同じSTIX IDの意味内容を変更した場合、`updated_at`と生成物の`modified`を進めた
- [ ] OpenCTI表現だけを変更した場合は正規OSINTの`updated_at`を偽装せず、
      `OPENCTI_MODEL_MODIFIED`と影響する生成objectの`modified`を進めた
- [ ] 同じSTIX IDの`created`を旧版から変更していない
- [ ] 同じ`id` + `modified`で異なる意味内容を生成していない
- [ ] 回帰テストを追加または実行した
- [ ] 生成物と集計を再生成した

## 13. 変更後の推奨実行順

```bash
python3 -m unittest discover -s actor_profile/tests -v
python3 -m unittest discover -s parse-daily/tests -v

python3 actor_profile/scripts/materialize_actor_census.py

# 旧生成ルールで既存profileへ入った地理由来のstate/espionage等だけを安全に移行
python3 actor_profile/scripts/migrate_generated_attribution.py --apply
python3 actor_profile/scripts/migrate_stix_modeling.py --apply

# 新規profileをbootstrapする場合のみ使用（既存profileの一括overwriteは禁止）
python3 actor_profile/scripts/bootstrap_all_profiles.py --scan-report-ttps

# 新規profileを含むcanonical側へmergeデータを移し、一次情報aliasを反映
python3 actor_profile/scripts/migrate_curated_entity_boundaries.py --apply
python3 actor_profile/scripts/apply_verified_alias_updates.py
python3 actor_profile/scripts/sync_attack_reference.py
python3 actor_profile/scripts/enrich_activity_intelligence.py --apply
python3 actor_profile/scripts/migrate_evidence_boundaries.py --apply
python3 actor_profile/scripts/apply_primary_source_corrections.py
python3 actor_profile/scripts/enrich_targeting_scope.py --apply
python3 actor_profile/scripts/materialize_activity_diamonds.py --apply
python3 actor_profile/scripts/build_claim_audits.py
python3 actor_profile/scripts/process_all_profiles.py --workers 3 --skip-ingest
python3 actor_profile/scripts/build_opencti_bundles.py --prune
python3 actor_profile/scripts/build_tidal_activity_index.py
python3 actor_profile/scripts/build_actor_research_dossiers.py

python3 actor_profile/scripts/render_collection_index.py \
  profiles/processing-summary.json \
  actor_profile/corpus-catalog.json \
  profiles/README.md
```

生成結果に大規模な差分が出る場合は、原因となったルール変更とデータ再生成を別commitまたは
別PRに分け、レビュー可能な状態を保ちます。
