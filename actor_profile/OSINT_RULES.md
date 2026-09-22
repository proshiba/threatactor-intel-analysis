# OSINT更新規約

## 情報源の優先順位

1. 政府機関、CERT、法執行機関の勧告・起訴・制裁資料
2. 攻撃を直接観測したセキュリティベンダーの技術報告
3. 公式MITRE ATT&CK、公開マルウェア解析、インシデント報告
4. 二次報道・集約サイト（発見用途のみ。可能な限り原典へ遡る）

検索結果のスニペットだけを証拠として使用しない。原文を開き、アクター名、公開日、
観測期間、主張、IOC/TTPの文脈を確認できたものだけを採用する。

## OSINT Source必須項目

- `source_id`
- `url`
- `title`
- `publisher`
- `published_at`
- `accessed_at`
- `source_type`
- `language`
- `tlp`
- `reliability`
- `actor_scope`
- `claims_supported`
- `archive_url`（存在する場合）
- `analyst_notes`

旧レコードで実際の取得時刻が保存されていない場合、`accessed_at`は推測せず
明示的に`null`とし、その理由を`analyst_notes`へ記録する。後日の監査日時を
過去の取得日時として代入しない。

## 更新判定

- 新aliasは、既存クラスターとのスコープを`exact`と断定せず、
  `overlapping`、`broader`、`narrower`、`unknown`を選ぶ。
- 帰属変更は、単独ベンダーの名称変更と政府帰属を分離する。
- 「公開日」と「攻撃観測日」を分離し、公開日を観測日に流用しない。
- 新キャンペーン、マルウェア、インフラ、TTP、標的は、該当主張のURLを
  `evidence_refs`で参照する。
- IOCとartifactは、原文で同一キャンペーン／マルウェアとの関係を確認できた場合のみ
  その参照を付与する。
- 構造化IOC表で`observed_at`列をmappingしているのにセルが空の場合は、観測時刻が
  明示されていないものとしてunknownを維持する。同じ行のcampaign ID、source ID、
  ファイル名、説明に含まれる年を代替のIOC観測時刻として抽出しない。資料が明示した
  Campaign期間も、個別IOCの観測日とは別に管理する。
- 既存情報と競合する場合は上書きせず、`assessment.uncertainties`と
  `analyst_notes`へ両論を残す。
- 集約データセットのcampaign、malware、標的、動機、帰属は調査候補として別層に保存し、
  原典を確認するまで正規プロファイルへ昇格しない。
- 同じ非canonical aliasが複数actorへ一致する場合、mentionを全actorへ複製せず、
  ambiguous aliasとしてレビューキューへ送る。canonical nameの明示一致を優先する。

## 企業・Threat Actor Group・自然人・法的措置の調査

schema 1.4.0の`associated_entities`へ追加する前に、企業、人間の集団、自然人を既存の
APTクラスタから分離して確認する。

- 企業は登記名、政府・司法・制裁資料上の正式名、所在地、別称を確認し、
  `entity_type: organization`とする。会社がAPT活動を支援・実行したとの記載があっても、
  会社名をIntrusion Setのexact aliasにはしない。
- Threat Actor Groupは、単なる活動クラスタ名ではなく、人間の集団・組織として一次資料が
  直接記述する場合に限り作成する。既存Intrusion Setとの別名重複はexact identityではなく、
  原典に応じて`overlaps-with`、`broader`、`narrower`またはunknownで保持する。
- 自然人は氏名、表記、handle、役割を原文で確認し、同姓同名やhandle一致だけで統合しない。
  攻撃への関与が根拠付きで識別できる場合だけ`threat-actor-individual`とする。
- 雇用、役員、創業、請負、政府所属、APT membershipは別々のclaimとして監査する。
  雇用先がAPTへ関与したことだけを理由に、従業員をそのAPTのmemberまたはoperatorとしない。
- 原典が「member、employee、contractor、affiliateのいずれか」のように複数の関係を
  選言でまとめ、人物ごとの区分を示さない場合、いずれか一つの動詞へ確定しない。
  `alleged-associated-with`等の上位関係で選言を保ち、個別に明示されたfounder等だけを
  別Relationshipとして記録する。
- 起訴状、訴追資料、逮捕発表は、当局が直接主張している内容と裁判で確定した事実を分ける。
  起訴・訴追は`legal_actions`へ`status: alleged`として記録し、後日の有罪判決または量刑は
  別資料・別actionで追加する。
- 制裁指定は当該当局による行政上の決定として記録し、有罪判決と言い換えない。

各entityまたは関係について、少なくとも正式名、原文が直接支持する役割・動詞、対象、
行為または観測期間、法的措置日、資料公開日、確度、URL、未解決点を分離して保存する。
法的措置日と資料公開日は、攻撃活動、雇用、membership、支援関係の観測期間ではない。
原典が活動期間を述べない場合は`first_observed` / `last_observed`をunknownのままにする。

## Hunting Pivotの調査

継続観測やC2 huntingに使う特徴は、単発IOCと分けて`hunting_pivots`へ保存する。候補には
証明書fingerprint/serial/subject/SAN、TLS fingerprint、コード署名、悪用driver、URI、
User-Agent、port/serviceの組合せ、ASN/hosting傾向等が含まれる。調査時は次を記録する。

1. 正確なpivot値または複合条件と、何を探索するための特徴か。
2. 観測ごとの`source_ref`、`activity_ref`、時刻、文脈、`count`、`count_basis`。
3. 一意なsource数、activity数、host/sample/event数。これらを相互に加算・代用しない。
4. actor-specificか、複数Actor・crimeware・red teamにも共有されるgeneric/shared特徴か。
5. 誤検知、必要な追加確認、検索範囲、確認できなかった点。

Pivot中のexact hash、IP、domain、URL、アルゴリズム既知の証明書fingerprintを通常IOCとして
取込んだ場合は、その`indicator_id`を`indicator_refs`へ追加する。Pivotと参照IOCは同じ
原典を持たなければならない。また、Observationの非null `activity_ref`と`source_ref`は、
それぞれ上位`activity_refs`と`evidence_refs`にも含める。

「複数」「all investigated attacks」「over 30 hosts」等は原文の単位と下限を保つ。
数値のない複数形を正確な件数へ変換せず、最小値を使う場合は`minimum-events`等の
`count_basis`を明記する。同じ資料内の再掲やページ数は独立したsource/eventではない。

時間は必ず意味を分離する。証明書の`notBefore` / `notAfter`は証明書有効期間、資料の日付は
`published_at`、VirusTotal等のfirst-seenは当該サービスでの初回確認、Shodan/Censysの時刻は
scan観測である。いずれも、それだけでは攻撃実行日またはActorの活動期間ではない。
原典が活動観測時刻を示さない場合、Pivotの`first_observed` / `last_observed`はunknownとする。

現在の継続利用を確認する場合は、利用規約と法令の範囲で受動的な検索・既存telemetryを使い、
`continuity.checks`へ実行日、platform、query、index/time window、結果件数・要約、
analyst validation、根拠、限界を記録する。`evaluated_at`は評価日であり攻撃観測日ではない。
実際に確認していなければ
`passive_scan_performed: false`、`active_status: unknown`とする。検索結果が0件でも、検索範囲、
index期間、query妥当性を検証せず`inactive`と断定しない。

`continuity.assessment`は過去の観測構造を表す。1 Observationは`single-observation`、独立した
複数時点・資料・telemetryでの確認は`reobserved`、原典が複数検体・host・活動での再利用を
明示する場合は`reused`、過去期間に限定された根拠は`historical-only`、評価不能は`unknown`とする。
これは評価時点の`active_status`と独立しており、`reused`でも現在利用は`unknown`になり得る。

issuer、ASN、hosting provider、CDN、正規サービスroot、汎用port、既定のC2 framework profileは
通常genericである。これら単独の一致をIOC、悪性Infrastructure、Actor帰属へ昇格しない。
既知fingerprint/SAN、exact subdomain/path、sample config、時間近接等を組み合わせる。
Shodan/Censys等のクエリは`requires_validation: true`とし、field schema、誤検知、必要な
corroborationを`false_positive_notes`へ残す。クエリ文字列を実行済みの証拠として扱わない。

## 調査状態

各アクターに次の状態を持たせる。

- `not_started`
- `searched`
- `source_verified`
- `integrated`
- `needs_review`

調査クエリ、確認したURL、採用／不採用理由を保存し、同じ検索を繰り返さない。
