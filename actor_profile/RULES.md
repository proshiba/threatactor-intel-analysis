# 脅威アクタープロファイル作成規約

規約バージョン: 1.0.0

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

Activityは`ttp_refs`と`victim_refs`も必ず持つ。参照先が判明しない場合は空配列にする。
TTP・マルウェア・標的・被害事例を活動へ結び付ける際は、同じ証拠がその活動内での
利用または被害を支持することを確認する。単なるアクター一般の利用実績は活動へ
結び付けない。

## 4.1 被害事例

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

## 6. アクター間関係

`relationship_type`は次を優先する。

- `part-of`
- `subordinate-to`
- `overlaps-with`
- `shares-tools-with`
- `shares-infrastructure-with`
- `shares-targeting-with`
- `cooperates-with`
- `successor-of`
- `related-to`

「同一アクター」と「ツール／インフラの重複」を分離する。関係には必ず説明、確度、
証拠を付ける。

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
- Malware: `malware`
- Tool: `tool`
- Infrastructure: `infrastructure`
- TTP: `attack-pattern`
- Activity: `campaign`
- Targets/attribution organizations: `identity`
- IOC: `indicator`
- 観測: `observed-data`と`note`、またはIndicatorの外部参照
- 関係: `relationship`

STIXに直接表しにくい精度、証拠、自由記述は`x_`カスタムプロパティとして保持する。

`artifacts.csv`の非IOC artifactは、該当するSCOへ安全に変換できる場合だけSTIXへ含める。
変換できないコマンドや文字列は、STIX `artifact` SCOへ無理に格納せず、`note`または
カスタムプロパティで参照する。

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
