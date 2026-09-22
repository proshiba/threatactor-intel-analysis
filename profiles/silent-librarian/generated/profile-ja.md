# Silent Librarian 脅威アクタープロファイル

- プロファイルID: `actor--silent-librarian`
- 状態: draft
- 更新日時: 2026-09-22T00:00:00Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

Silent Librarianの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Silent Librarian**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| COBALT DICKENS | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |
| TA407 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |

## 帰属

U.S. DOJ charging documents and Treasury's 2018 designation allege that the Iran-based Mabna Institute conducted many intrusions for the IRGC and other Iranian government or university clients. Applied to Silent Librarian only through the separately modeled medium-confidence Mabna association.

- 国: Iran
- スポンサー種別: state-aligned
- 確度: 中
- 証拠: `source--doj-mabna-indictment-2018`, `source--doj-mabna-superseding-indictment-2026`, `source--treasury-mabna-sanctions-2018`, `source--mitre-attack-19-2`

## モチベーション

未評価

## 他アクターとの関係

確認された関係なし

## 関連する企業・個人

| ID | 名称 | 種別 | 役割 | 国 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|
| organization--mabna-institute | Mabna Institute | organization | hacking-for-hire-company | Iran | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-indictment-2018`, `source--doj-mabna-superseding-indictment-2026`, `source--treasury-mabna-sanctions-2018` |
| threat-actor-individual--gholamreza-rafatnejad | Gholamreza Rafatnejad | threat-actor-individual | founder | Iran | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026`, `source--doj-mabna-indictment-2018`, `source--treasury-mabna-sanctions-2018` |
| threat-actor-individual--ehsan-mohammadi | Ehsan Mohammadi | threat-actor-individual | founder, managing-director | Iran | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026`, `source--doj-mabna-indictment-2018`, `source--treasury-mabna-sanctions-2018` |
| threat-actor-individual--abdollah-karima | Abdollah Karima | threat-actor-individual | contractor, business-owner | Iran | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026`, `source--doj-mabna-indictment-2018`, `source--treasury-mabna-sanctions-2018` |
| threat-actor-individual--mostafa-sadeghi | Mostafa Sadeghi | threat-actor-individual | affiliate | Iran | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026`, `source--doj-mabna-indictment-2018`, `source--treasury-mabna-sanctions-2018` |
| threat-actor-individual--seyed-ali-mirkarimi | Seyed Ali Mirkarimi | threat-actor-individual | contractor | Iran | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026`, `source--doj-mabna-indictment-2018`, `source--treasury-mabna-sanctions-2018` |
| threat-actor-individual--mohammed-reza-sabahi | Mohammed Reza Sabahi | threat-actor-individual | contractor | Iran | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026`, `source--doj-mabna-indictment-2018`, `source--treasury-mabna-sanctions-2018` |
| threat-actor-individual--roozbeh-sabahi | Roozbeh Sabahi | threat-actor-individual | contractor | Iran | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026`, `source--doj-mabna-indictment-2018`, `source--treasury-mabna-sanctions-2018` |
| threat-actor-individual--abuzar-gohari-moqadam | Abuzar Gohari Moqadam | threat-actor-individual | professor, affiliate | Iran | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026`, `source--doj-mabna-indictment-2018`, `source--treasury-mabna-sanctions-2018` |
| threat-actor-individual--sajjad-tahmasebi | Sajjad Tahmasebi | threat-actor-individual | contractor | Iran | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026`, `source--doj-mabna-indictment-2018`, `source--treasury-mabna-sanctions-2018` |
| threat-actor-individual--saeid-houshyar | Saeid Houshyar | threat-actor-individual | contractor | Iran | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |
| threat-actor-individual--behzad-mesri | Behzad Mesri | threat-actor-individual | contractor | Iran | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026`, `source--treasury-mabna-sanctions-2018` |
| threat-actor-individual--manouchehr-hashemloo | Manouchehr Hashemloo | threat-actor-individual | contractor | Iran | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |
| threat-actor-individual--keyvan-fayaz | Keyvan Fayaz | threat-actor-individual | contractor | Iran | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |
| threat-actor-individual--amir-barati | Amir Barati | threat-actor-individual | contractor | Iran | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |
| threat-actor-individual--saber-shahbazi-ballojeh | Saber Shahbazi Ballojeh | threat-actor-individual | contractor | Iran | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |
| threat-actor-individual--arman-kahzadian | Arman Kahzadian | threat-actor-individual | contractor | Iran | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |
| threat-actor-individual--mojtaba-galekuhi | Mojtaba Galekuhi | threat-actor-individual | alleged-co-conspirator | Iran | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |

### エンティティ関係

| 起点 | 関係 | 終点 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|
| organization--mabna-institute | associated-with | actor--silent-librarian | MITRE states that members of Silent Librarian are known to have been affiliated with Mabna Institute; this does not make the organization and vendor cluster exact aliases. | 不明 | 不明 | 中 | `source--mitre-attack-19-2`, `source--doj-mabna-indictment-2018` |
| threat-actor-individual--gholamreza-rafatnejad | founder-of | organization--mabna-institute | DOJ and Treasury identify the individual as a founder of Mabna Institute in approximately 2013. | 不明 | 不明 | 高 | `source--doj-mabna-indictment-2018`, `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026`, `source--treasury-mabna-sanctions-2018` |
| threat-actor-individual--ehsan-mohammadi | founder-of | organization--mabna-institute | DOJ and Treasury identify the individual as a founder of Mabna Institute in approximately 2013. | 不明 | 不明 | 高 | `source--doj-mabna-indictment-2018`, `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026`, `source--treasury-mabna-sanctions-2018` |
| threat-actor-individual--abdollah-karima | alleged-contractor-for | organization--mabna-institute | The S2 indictment alleges that Abdollah Karima, owner and operator of Falinoos, contracted with Mabna Institute to direct certain hacking activities. | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026` |
| threat-actor-individual--mostafa-sadeghi | alleged-affiliate-of | organization--mabna-institute | The S2 indictment alleges that Mostafa Sadeghi was an affiliate of Mabna Institute. | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026` |
| threat-actor-individual--seyed-ali-mirkarimi | alleged-contractor-for | organization--mabna-institute | The S2 indictment alleges that Seyed Ali Mirkarimi was a contractor for Mabna Institute. | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026` |
| threat-actor-individual--mohammed-reza-sabahi | alleged-contractor-for | organization--mabna-institute | The S2 indictment alleges that Mohammed Reza Sabahi was a contractor for Mabna Institute. | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026` |
| threat-actor-individual--roozbeh-sabahi | alleged-contractor-for | organization--mabna-institute | The S2 indictment alleges that Roozbeh Sabahi was a contractor for Mabna Institute. | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026` |
| threat-actor-individual--abuzar-gohari-moqadam | alleged-affiliate-of | organization--mabna-institute | The S2 indictment alleges that professor Abuzar Gohari Moqadam was an affiliate of Mabna Institute. | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026` |
| threat-actor-individual--sajjad-tahmasebi | alleged-contractor-for | organization--mabna-institute | The S2 indictment alleges that Sajjad Tahmasebi was a contractor for Mabna Institute. | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026` |
| threat-actor-individual--saeid-houshyar | alleged-contractor-for | organization--mabna-institute | The S2 indictment alleges that Saeid Houshyar was a contractor for Mabna Institute. | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026` |
| threat-actor-individual--behzad-mesri | alleged-contractor-for | organization--mabna-institute | The S2 indictment alleges that Behzad Mesri was a contractor for Mabna Institute. | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026` |
| threat-actor-individual--manouchehr-hashemloo | alleged-contractor-for | organization--mabna-institute | The S2 indictment alleges that Manouchehr Hashemloo was a contractor for Mabna Institute. | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026` |
| threat-actor-individual--keyvan-fayaz | alleged-contractor-for | organization--mabna-institute | The S2 indictment alleges that Keyvan Fayaz was a contractor for Mabna Institute. | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026` |
| threat-actor-individual--amir-barati | alleged-contractor-for | organization--mabna-institute | The S2 indictment alleges that Amir Barati was a contractor for Mabna Institute. | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026` |
| threat-actor-individual--saber-shahbazi-ballojeh | alleged-contractor-for | organization--mabna-institute | The S2 indictment alleges that Saber Shahbazi Ballojeh was a contractor for Mabna Institute. | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026` |
| threat-actor-individual--arman-kahzadian | alleged-contractor-for | organization--mabna-institute | The S2 indictment alleges that Arman Kahzadian was a contractor for Mabna Institute. | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026` |
| threat-actor-individual--mojtaba-galekuhi | alleged-associated-with | organization--mabna-institute | The S2 indictment alleges that Mojtaba Galekuhi conspired with certain Mabna defendants; it does not state that he held a formal role at Mabna Institute. | 不明 | 不明 | 高 | `source--doj-mabna-s2-indictment-2026` |

### 法的措置

| 対象 | 措置 | 当局 | 日付 | 状態 | 説明 | 証拠 |
|---|---|---|---|---|---|---|
| Mabna Institute | sanction | U.S. Department of the Treasury, Office of Foreign Assets Control | 2018-03-23 | completed | Designated under Executive Order 13694, as amended. | `source--treasury-mabna-sanctions-2018` |
| Gholamreza Rafatnejad | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the seven-count indictment unsealed on 2018-03-23. | `source--doj-mabna-indictment-2018` |
| Gholamreza Rafatnejad | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the 14-count superseding indictment unsealed on 2026-08-18. | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |
| Gholamreza Rafatnejad | sanction | U.S. Department of the Treasury, Office of Foreign Assets Control | 2018-03-23 | completed | Designated under Executive Order 13694, as amended. | `source--treasury-mabna-sanctions-2018` |
| Ehsan Mohammadi | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the seven-count indictment unsealed on 2018-03-23. | `source--doj-mabna-indictment-2018` |
| Ehsan Mohammadi | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the 14-count superseding indictment unsealed on 2026-08-18. | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |
| Ehsan Mohammadi | sanction | U.S. Department of the Treasury, Office of Foreign Assets Control | 2018-03-23 | completed | Designated under Executive Order 13694, as amended. | `source--treasury-mabna-sanctions-2018` |
| Abdollah Karima | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the seven-count indictment unsealed on 2018-03-23. | `source--doj-mabna-indictment-2018` |
| Abdollah Karima | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the 14-count superseding indictment unsealed on 2026-08-18. | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |
| Abdollah Karima | sanction | U.S. Department of the Treasury, Office of Foreign Assets Control | 2018-03-23 | completed | Designated under Executive Order 13694, as amended. | `source--treasury-mabna-sanctions-2018` |
| Mostafa Sadeghi | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the seven-count indictment unsealed on 2018-03-23. | `source--doj-mabna-indictment-2018` |
| Mostafa Sadeghi | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the 14-count superseding indictment unsealed on 2026-08-18. | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |
| Mostafa Sadeghi | sanction | U.S. Department of the Treasury, Office of Foreign Assets Control | 2018-03-23 | completed | Designated under Executive Order 13694, as amended. | `source--treasury-mabna-sanctions-2018` |
| Seyed Ali Mirkarimi | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the seven-count indictment unsealed on 2018-03-23. | `source--doj-mabna-indictment-2018` |
| Seyed Ali Mirkarimi | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the 14-count superseding indictment unsealed on 2026-08-18. | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |
| Seyed Ali Mirkarimi | sanction | U.S. Department of the Treasury, Office of Foreign Assets Control | 2018-03-23 | completed | Designated under Executive Order 13694, as amended. | `source--treasury-mabna-sanctions-2018` |
| Mohammed Reza Sabahi | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the seven-count indictment unsealed on 2018-03-23. | `source--doj-mabna-indictment-2018` |
| Mohammed Reza Sabahi | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the 14-count superseding indictment unsealed on 2026-08-18. | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |
| Mohammed Reza Sabahi | sanction | U.S. Department of the Treasury, Office of Foreign Assets Control | 2018-03-23 | completed | Designated under Executive Order 13694, as amended. | `source--treasury-mabna-sanctions-2018` |
| Roozbeh Sabahi | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the seven-count indictment unsealed on 2018-03-23. | `source--doj-mabna-indictment-2018` |
| Roozbeh Sabahi | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the 14-count superseding indictment unsealed on 2026-08-18. | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |
| Roozbeh Sabahi | sanction | U.S. Department of the Treasury, Office of Foreign Assets Control | 2018-03-23 | completed | Designated under Executive Order 13694, as amended. | `source--treasury-mabna-sanctions-2018` |
| Abuzar Gohari Moqadam | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the seven-count indictment unsealed on 2018-03-23. | `source--doj-mabna-indictment-2018` |
| Abuzar Gohari Moqadam | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the 14-count superseding indictment unsealed on 2026-08-18. | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |
| Abuzar Gohari Moqadam | sanction | U.S. Department of the Treasury, Office of Foreign Assets Control | 2018-03-23 | completed | Designated under Executive Order 13694, as amended. | `source--treasury-mabna-sanctions-2018` |
| Sajjad Tahmasebi | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the seven-count indictment unsealed on 2018-03-23. | `source--doj-mabna-indictment-2018` |
| Sajjad Tahmasebi | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the 14-count superseding indictment unsealed on 2026-08-18. | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |
| Sajjad Tahmasebi | sanction | U.S. Department of the Treasury, Office of Foreign Assets Control | 2018-03-23 | completed | Designated under Executive Order 13694, as amended. | `source--treasury-mabna-sanctions-2018` |
| Saeid Houshyar | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the 14-count superseding indictment unsealed on 2026-08-18. | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |
| Behzad Mesri | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the 14-count superseding indictment unsealed on 2026-08-18. | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |
| Behzad Mesri | sanction | U.S. Department of the Treasury, Office of Foreign Assets Control | 2018-03-23 | completed | Designated under Executive Order 13694, as amended. | `source--treasury-mabna-sanctions-2018` |
| Manouchehr Hashemloo | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the 14-count superseding indictment unsealed on 2026-08-18. | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |
| Keyvan Fayaz | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the 14-count superseding indictment unsealed on 2026-08-18. | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |
| Amir Barati | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the 14-count superseding indictment unsealed on 2026-08-18. | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |
| Saber Shahbazi Ballojeh | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the 14-count superseding indictment unsealed on 2026-08-18. | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |
| Arman Kahzadian | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the 14-count superseding indictment unsealed on 2026-08-18. | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |
| Mojtaba Galekuhi | indictment | U.S. District Court for the Southern District of New York | 不明 | alleged | Named as a defendant in the 14-count superseding indictment unsealed on 2026-08-18. | `source--doj-mabna-s2-indictment-2026`, `source--doj-mabna-superseding-indictment-2026` |

## ダイヤモンドモデル

| 要素 | 内容 |
|---|---|
| Adversary |  |
| Capability |  |
| Infrastructure |  |
| Victim |  |
| Socio-political |  |

## OSINTクロスチェック

- 判定: `matched`
- 調査日時: 2026-09-21T02:39:13Z
- 国別メタデータ衝突: なし
- 複数taxonomyスコープ: なし

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | Mabna Institute, Cobalt Dickens, Silent Librarian | canonical-name | 高 | Iran | https://www.proofpoint.com/us/threat-insight/post/threat-actor-profile-ta407-silent-librarian<br>https://apt.etda.or.th/cgi-bin/showcard.cgi?g=Mabna+Institute%2C+Cobalt+Dickens%2C+Silent+Librarian&n=1 |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | 一致なし |  |  |  |  |
| misp-threat-actor | Silent Librarian | canonical-name | 高 | IR | https://info.phishlabs.com/blog/silent-librarian-more-to-the-story-of-the-iranian-mabna-institute-indictment<br>https://info.phishlabs.com/blog/silent-librarian-university-attacks-continue-unabated-in-days-following-indictment<br>https://www.justice.gov/usao-sdny/pr/nine-iranians-charged-conducting-massive-cyber-theft-campaign-behalf-islamic |
| misp-microsoft-activity-group | 一致なし |  |  |  |  |
| misp-mitre-enterprise-intrusion-set | Silent Librarian - G0122 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0122<br>https://blog.malwarebytes.com/malwarebytes-news/2020/10/silent-librarian-apt-phishing-attack/<br>https://info.phishlabs.com/blog/silent-librarian-more-to-the-story-of-the-iranian-mabna-institute-indictment |
| misp-mitre-intrusion-set | Silent Librarian - G0122 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0122<br>https://blog.malwarebytes.com/malwarebytes-news/2020/10/silent-librarian-apt-phishing-attack/<br>https://info.phishlabs.com/blog/silent-librarian-more-to-the-story-of-the-iranian-mabna-institute-indictment |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | Silent Librarian | canonical-name | 高 | IR |  |

### 関係性候補（未統合）

候補なし

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

未確認

### ツール

未確認

### インフラ

未確認

### 配送・ファイル形式

未確認

### 脆弱性

未確認

### 運用能力

未確認

## C2・マルウェア ハンティング・ピボット

構造化されたハンティング・ピボットなし

### 観測根拠

観測記録なし

### ハントクエリ

クエリなし

### 継続利用チェック

実行済みの受動検索・継続利用チェックなし

`active_status` は明示的なテレメトリまたはスキャン根拠がない限り `unknown` です。出典公開日は観測時刻に転用していません。

## 攻撃活動の履歴

| 活動 | 種別 | 初回 | 最終 | 報告日 | 標的 | マルウェア | TTP | 被害事例 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Mabna Instituteによる大学・組織侵入キャンペーン（2013–2017） | credential-phishing-and-data-theft-campaign | 2013 | 2017-12 | 2018-03-23 | target--activity-rule--sector--d406c8e5b7fa7aeff7d2, target--activity-rule--sector--e7608f51421ca8b1e297, target--country--united-states, target--sector--government, target--silent-librarian--sector--private-sector, target--silent-librarian--country--australia, target--silent-librarian--country--canada, target--silent-librarian--country--china, target--silent-librarian--country--denmark, target--silent-librarian--country--finland, target--silent-librarian--country--germany, target--silent-librarian--country--ireland, target--silent-librarian--country--israel, target--silent-librarian--country--italy, target--silent-librarian--country--japan, target--silent-librarian--country--malaysia, target--silent-librarian--country--netherlands, target--silent-librarian--country--norway, target--silent-librarian--country--poland, target--silent-librarian--country--saudi-arabia, target--silent-librarian--country--singapore, target--silent-librarian--country--south-korea, target--silent-librarian--country--spain, target--silent-librarian--country--sweden, target--silent-librarian--country--switzerland, target--silent-librarian--country--turkey, target--silent-librarian--country--united-kingdom |  |  | victim--activity-rule--a3fd052f21deca13b807 | 米司法省の2018年および2026年の起訴発表によると、Mabna Instituteの関係者は約2013年から少なくとも2017年12月まで、大学その他の組織を対象とするスピアフィッシングと資格情報窃取キャンペーンを実施したとされる。2026年資料の集計は、米国144大学、国外178大学、米国企業42社以上、国外企業11社以上、米国の連邦・州政府機関5機関以上、NGO 2団体以上である。教授アカウント10万件超を標的とし約8,000件を侵害、31.5TB以上の学術・知的財産データを窃取したとされる。米国大学が対象データの調達・アクセスへ支出した34億ドル超は、窃取額や被害損失の評価ではない。 | 中 | `source--doj-mabna-indictment-2018`, `source--doj-mabna-superseding-indictment-2026`, `source--mitre-attack-19-2` |

### 活動別ダイヤモンドモデル

| 活動 | 攻撃者 | マルウェア | TTP | インフラ | 標的属性 | 被害事例 | 確度 |
|---|---|---|---|---|---|---|---|
| Mabna Instituteによる大学・組織侵入キャンペーン（2013–2017） | Silent Librarian | 情報なし | 情報なし | 情報なし | 非営利・市民社会, 教育・研究, 米国, Government, オーストラリア, カナダ, 中国, デンマーク, フィンランド, ドイツ, アイルランド, イスラエル, イタリア, 日本, マレーシア, オランダ, ノルウェー, ポーランド, サウジアラビア, シンガポール, 韓国, スペイン, スウェーデン, スイス, トルコ, 英国, 民間企業 | 被害事例: Mabna Institute大学・組織侵入キャンペーン | 中 |



## ターゲット

| 分類 | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| countries | 米国 | Targeting text mentions united states. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| countries | オーストラリア | The 2026 DOJ release explicitly lists this country among the locations of foreign universities compromised in the 2013–2017 campaign. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| countries | カナダ | The 2026 DOJ release explicitly lists this country among the locations of foreign universities compromised in the 2013–2017 campaign. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| countries | 中国 | The 2026 DOJ release explicitly lists this country among the locations of foreign universities compromised in the 2013–2017 campaign. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| countries | デンマーク | The 2026 DOJ release explicitly lists this country among the locations of foreign universities compromised in the 2013–2017 campaign. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| countries | フィンランド | The 2026 DOJ release explicitly lists this country among the locations of foreign universities compromised in the 2013–2017 campaign. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| countries | ドイツ | The 2026 DOJ release explicitly lists this country among the locations of foreign universities compromised in the 2013–2017 campaign. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| countries | アイルランド | The 2026 DOJ release explicitly lists this country among the locations of foreign universities compromised in the 2013–2017 campaign. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| countries | イスラエル | The 2026 DOJ release explicitly lists this country among the locations of foreign universities compromised in the 2013–2017 campaign. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| countries | イタリア | The 2026 DOJ release explicitly lists this country among the locations of foreign universities compromised in the 2013–2017 campaign. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| countries | 日本 | The 2026 DOJ release explicitly lists this country among the locations of foreign universities compromised in the 2013–2017 campaign. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| countries | マレーシア | The 2026 DOJ release explicitly lists this country among the locations of foreign universities compromised in the 2013–2017 campaign. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| countries | オランダ | The 2026 DOJ release explicitly lists this country among the locations of foreign universities compromised in the 2013–2017 campaign. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| countries | ノルウェー | The 2026 DOJ release explicitly lists this country among the locations of foreign universities compromised in the 2013–2017 campaign. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| countries | ポーランド | The 2026 DOJ release explicitly lists this country among the locations of foreign universities compromised in the 2013–2017 campaign. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| countries | サウジアラビア | The 2026 DOJ release explicitly lists this country among the locations of foreign universities compromised in the 2013–2017 campaign. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| countries | シンガポール | The 2026 DOJ release explicitly lists this country among the locations of foreign universities compromised in the 2013–2017 campaign. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| countries | 韓国 | The 2026 DOJ release explicitly lists this country among the locations of foreign universities compromised in the 2013–2017 campaign. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| countries | スペイン | The 2026 DOJ release explicitly lists this country among the locations of foreign universities compromised in the 2013–2017 campaign. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| countries | スウェーデン | The 2026 DOJ release explicitly lists this country among the locations of foreign universities compromised in the 2013–2017 campaign. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| countries | スイス | The 2026 DOJ release explicitly lists this country among the locations of foreign universities compromised in the 2013–2017 campaign. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| countries | トルコ | The 2026 DOJ release explicitly lists this country among the locations of foreign universities compromised in the 2013–2017 campaign. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| countries | 英国 | The 2026 DOJ release explicitly lists this country among the locations of foreign universities compromised in the 2013–2017 campaign. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| sectors | 非営利・市民社会 | Mabna Instituteの大学・組織侵入キャンペーンについて、DOJ資料で対象として明示された産業。 | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| sectors | 教育・研究 | Mabna Instituteの大学・組織侵入キャンペーンについて、DOJ資料で対象として明示された産業。 | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |
| sectors | Government | Targeting text indicates the Government sector. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026`, `source--mitre-attack-19-1`, `source--mitre-attack-19-2` |
| sectors | 民間企業 | DOJ reports at least 42 U.S. and 11 foreign private-sector companies in scope. | 2013 | 2017-12 | 中 | `source--doj-mabna-superseding-indictment-2026` |

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

| 事例 | 被害者 | 公開状態 | 種別 | 事例状態 | 標的属性 | マルウェア | TTP | 影響資産 | 影響 | 初回 | 最終 | 報告日 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 被害事例: Mabna Institute大学・組織侵入キャンペーン | 非公開 | aggregate | multiple-organizations | alleged | target--activity-rule--sector--d406c8e5b7fa7aeff7d2, target--activity-rule--sector--e7608f51421ca8b1e297, target--country--united-states, target--sector--government, target--silent-librarian--sector--private-sector, target--silent-librarian--country--australia, target--silent-librarian--country--canada, target--silent-librarian--country--china, target--silent-librarian--country--denmark, target--silent-librarian--country--finland, target--silent-librarian--country--germany, target--silent-librarian--country--ireland, target--silent-librarian--country--israel, target--silent-librarian--country--italy, target--silent-librarian--country--japan, target--silent-librarian--country--malaysia, target--silent-librarian--country--netherlands, target--silent-librarian--country--norway, target--silent-librarian--country--poland, target--silent-librarian--country--saudi-arabia, target--silent-librarian--country--singapore, target--silent-librarian--country--south-korea, target--silent-librarian--country--spain, target--silent-librarian--country--sweden, target--silent-librarian--country--switzerland, target--silent-librarian--country--turkey, target--silent-librarian--country--united-kingdom |  |  |  | data-theft: 約8,000件の教授メールアカウントを侵害し、31.5TB以上の学術データと知的財産を窃取したと米司法省は主張している。 | 2013 | 2017-12 | 2018-03-23 | 中 | `source--doj-mabna-indictment-2018`, `source--doj-mabna-superseding-indictment-2026`, `source--mitre-attack-19-2` |

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [Silent Librarian](https://attack.mitre.org/groups/G0122) has used compromised credentials to obtain unauthorized access to online accounts.(Citation: DOJ Iran Indictments March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Credential Access | T1110.003 | Password Spraying | [Silent Librarian](https://attack.mitre.org/groups/G0122) has used collected lists of names and e-mail accounts to use in password spraying attacks against private sector targets.(Citation: DOJ Iran Indictments March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Collection | T1114 | Email Collection | [Silent Librarian](https://attack.mitre.org/groups/G0122) has exfiltrated entire mailboxes from compromised accounts.(Citation: DOJ Iran Indictments March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Collection | T1114.003 | Email Forwarding Rule | [Silent Librarian](https://attack.mitre.org/groups/G0122) has set up auto forwarding rules on compromised e-mail accounts.(Citation: DOJ Iran Indictments March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1583.001 | Domains | [Silent Librarian](https://attack.mitre.org/groups/G0122) has acquired domains to establish credential harvesting pages, often spoofing the target organization and using free top level domains .TK, .ML, .GA, .CF, and .GQ.(Citation: DOJ Iran Indictments March 2018)(Citation: Phish Labs Silent Librarian)(Citation: Secureworks COBALT DICKENS August 2018)(Citation: Proofpoint TA407 September 2019)(Citation: Secureworks COBALT DICKENS September 2019)(Citation: Malwarebytes Silent Librarian October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1585.002 | Email Accounts | [Silent Librarian](https://attack.mitre.org/groups/G0122) has established e-mail accounts to receive e-mails forwarded from compromised accounts.(Citation: DOJ Iran Indictments March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1588.002 | Tool | [Silent Librarian](https://attack.mitre.org/groups/G0122) has obtained free and publicly available tools including SingleFile and HTTrack to copy login pages of targeted organizations.(Citation: Proofpoint TA407 September 2019)(Citation: Secureworks COBALT DICKENS September 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1588.004 | Digital Certificates | [Silent Librarian](https://attack.mitre.org/groups/G0122) has obtained free Let's Encrypt SSL certificates for use on their phishing pages.(Citation: Phish Labs Silent Librarian)(Citation: Secureworks COBALT DICKENS September 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Reconnaissance | T1589.002 | Email Addresses | [Silent Librarian](https://attack.mitre.org/groups/G0122) has collected e-mail addresses from targeted organizations from open Internet searches.(Citation: DOJ Iran Indictments March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Reconnaissance | T1589.003 | Employee Names | [Silent Librarian](https://attack.mitre.org/groups/G0122) has collected lists of names for individuals from targeted organizations.(Citation: DOJ Iran Indictments March 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Reconnaissance | T1594 | Search Victim-Owned Websites | [Silent Librarian](https://attack.mitre.org/groups/G0122) has searched victim's websites to identify the interests and academic areas of targeted individuals and to scrape source code, branding, and organizational contact information for phishing pages.(Citation: DOJ Iran Indictments March 2018)(Citation: Phish Labs Silent Librarian)(Citation: Proofpoint TA407 September 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Reconnaissance | T1598.003 | Spearphishing Link | [Silent Librarian](https://attack.mitre.org/groups/G0122) has used links in e-mails to direct victims to credential harvesting websites designed to appear like the targeted organization's login page.(Citation: DOJ Iran Indictments March 2018)(Citation: Phish Labs Silent Librarian)(Citation: Secureworks COBALT DICKENS August 2018)(Citation: Proofpoint TA407 September 2019)(Citation: Secureworks COBALT DICKENS September 2019)(Citation: Malwarebytes Silent Librarian October 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1608.005 | Link Target | [Silent Librarian](https://attack.mitre.org/groups/G0122) has cloned victim organization login pages and staged them for later use in credential harvesting campaigns. [Silent Librarian](https://attack.mitre.org/groups/G0122) has also made use of a variety of URL shorteners for these staged websites.(Citation: Secureworks COBALT DICKENS September 2019)(Citation: Malwarebytes Silent Librarian October 2020)(Citation: Proofpoint TA407 September 2019) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

## IOC／artifact概要

- IOC値: 0件
- IOC観測: 0件
- 複数攻撃で観測: 0件
- 要レビュー候補: 0件
- 非IOC artifact観測: 0件（`artifacts.csv`）

## 主要判断と不確実性

主要判断なし

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.
- 2 alias lead(s) remain non-canonical pending original-source review.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--doj-mabna-superseding-indictment-2026 | 17 Iranians Charged with Conducting Massive Cyber Theft Campaign on Behalf of the Islamic Revolutionary Guard Corps and Other Iranian Entities | U.S. Department of Justice, Office of Public Affairs | 2026-08-18 | https://www.justice.gov/opa/pr/17-iranians-charged-conducting-massive-cyber-theft-campaign-behalf-islamic-revolutionary | government-legal-release | TLP:CLEAR | 高 |
| source--doj-mabna-s2-indictment-2026 | Superseding Indictment, United States v. Gholamreza Rafatnejad et al. (S2 18 Cr. 162) | U.S. District Court for the Southern District of New York / U.S. Department of Justice | 2026-08-18 | https://www.justice.gov/usao-sdny/media/1458201/dl | government-legal | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--silent-librarian--08f205a61fe8698f | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--silent-librarian--3464e33fce328076 | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--silent-librarian--3f2755172c94632d | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--silent-librarian--8face31a321e90fd | silent librarian |  | 不明 | actor_profile/evidence/silent-librarian.csv | structured-data | TLP:CLEAR | 中 |
| source--silent-librarian--946ba58701120acd | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--silent-librarian--c4f9158d7899ed12 | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-enterprise-19.1.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--doj-mabna-indictment-2018 | Nine Iranians Charged With Conducting Massive Cyber Theft Campaign on Behalf of the Islamic Revolutionary Guard Corps | U.S. Department of Justice, Office of Public Affairs | 2018-03-23 | https://www.justice.gov/archives/opa/pr/nine-iranians-charged-conducting-massive-cyber-theft-campaign-behalf-islamic-revolutionary | government-legal-release | TLP:CLEAR | 高 |
| source--treasury-mabna-sanctions-2018 | Treasury Sanctions Iranian Cyber Actors for Malicious Cyber-Enabled Activities Targeting Hundreds of Universities | U.S. Department of the Treasury | 2018-03-23 | https://home.treasury.gov/news/press-releases/sm0332 | government-legal-release | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
