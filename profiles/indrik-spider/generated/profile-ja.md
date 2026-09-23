# Indrik Spider 脅威アクタープロファイル

- プロファイルID: `actor--indrik-spider`
- 状態: draft
- 更新日時: 2026-09-23T12:16:55Z
- 構造バージョン: 1.4.0

## エグゼクティブサマリー

Indrik Spiderの標準化プロファイル。リポジトリ内の専用資料1件とMITRE ATT&CK、アクターマッピング表を基礎情報としている。

## アクター名とAlias

- 正規名: **Indrik Spider**
- 初回観測: 不明
- 最終観測: 不明
- 活動状態: unknown

| Alias | 追跡元 | スコープ | 確度 | 証拠 | 補足 |
|---|---|---|---|---|---|
| DEV-0243 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |
| Evil Corp | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |
| Manatee Tempest | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |
| UNC2165 | MITRE ATT&CK | overlapping | 高 | `source--mitre-attack-19-2` | Alias scope must be reviewed before publication. |

## 帰属

未評価

- 国: 不明
- スポンサー種別: unknown
- 確度: 不明
- 証拠: なし

## モチベーション

未評価

## 他アクターとの関係

| 対象 | 関係 | 説明 | 確度 | 証拠 |
|---|---|---|---|---|
| TA505 | overlaps-with | 共有alias: Evil Corp, Indrik Spider | 低 | `source--mitre-attack-19-1` |
| Mustard Tempest | related-to | [Mustard Tempest](https://attack.mitre.org/groups/G1020) has partnered with [Indrik Spider](https://attack.mitre.org/groups/G0119) to provide access for the download of additional malware including LockBit, [WastedLocker](https://attack.mitre.org/software/S0612), and remote access tools.(Citation: Microsoft Ransomware as a Service)(Citation: Microsoft Threat Actor Naming July 2023)(Citation: Secureworks Gold Prelude Profile)(Citation: SocGholish-update) | 中 | `source--mitre-attack-19-2` |

## 関連する企業・個人

| ID | 名称 | 種別 | 役割 | 国 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|
| organization--russian-fsb | Federal Security Service of the Russian Federation | organization | government-intelligence-organization | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--treasury-evil-corp-fsb-enablers-2024` |
| organization--solar-invest | Solar-Invest LLC | organization | commercial-company | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-fsb-enablers-2024` |
| organization--vympel-assistance | Vympel-Assistance LLC | organization | commercial-company | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-fsb-enablers-2024` |
| threat-actor-individual--aleksandr-ryzhenkov | Aleksandr Viktorovich Ryzhenkov | threat-actor-individual | evil-corp-second-in-command, cybercriminal | Russia | 2017-06 | 不明 | 高 | `source--fbi-ryzhenkov-wanted`, `source--doj-ryzhenkov-ransomware-2024`, `source--treasury-evil-corp-fsb-enablers-2024` |
| threat-actor-individual--eduard-benderskiy | Eduard Vitalevich Benderskiy | threat-actor-individual | former-intelligence-officer, evil-corp-enabler, company-owner | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-fsb-enablers-2024` |
| threat-actor-individual--igor-turashev | Igor Olegovich Turashev | threat-actor-individual | evil-corp-administrator, cybercriminal | Russia | 不明 | 不明 | 高 | `source--doj-yakubets-turashev-indictment-2019`, `source--doj-yakubets-turashev-2019`, `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-individual--maksim-yakubets | Maksim Viktorovich Yakubets | threat-actor-individual | evil-corp-leader, cybercriminal, state-tasked-operator | Russia | 2009-05 | 不明 | 高 | `source--doj-yakubets-turashev-indictment-2019`, `source--doj-yakubets-turashev-2019`, `source--treasury-evil-corp-sanctions-2019`, `source--treasury-evil-corp-fsb-enablers-2024`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-group--evil-corp | Evil Corp | threat-actor-group | cybercriminal-organization, malware-operator | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--treasury-evil-corp-fsb-enablers-2024`, `source--mitre-attack-19-2`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-individual--viktor-yakubets | Viktor Grigoryevich Yakubets | threat-actor-individual | evil-corp-member, technical-procurement-support | Russia | 2020 | 不明 | 高 | `source--treasury-evil-corp-fsb-enablers-2024` |
| threat-actor-individual--sergey-ryzhenkov | Sergey Viktorovich Ryzhenkov | threat-actor-individual | evil-corp-member, malware-development-support | Russia | 2019 | 2020 | 高 | `source--treasury-evil-corp-fsb-enablers-2024` |
| threat-actor-individual--aleksey-shchetinin | Aleksey Yevgenevich Shchetinin | threat-actor-individual | evil-corp-member, financial-facilitator | Russia | 2017 | 2018 | 高 | `source--treasury-evil-corp-fsb-enablers-2024` |
| threat-actor-individual--beyat-ramazanov | Beyat Enverovich Ramazanov | threat-actor-individual | evil-corp-member, general-support | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-fsb-enablers-2024` |
| threat-actor-individual--vadim-pogodin | Vadim Gennadievich Pogodin | threat-actor-individual | evil-corp-member, ransomware-operator | Russia | 2020 | 不明 | 高 | `source--treasury-evil-corp-fsb-enablers-2024` |
| organization--biznes-stolitsa | Biznes-Stolitsa, OOO | organization | commercial-company, evil-corp-member-owned-company | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| organization--optima-ooo | Optima, OOO | organization | commercial-company, evil-corp-member-owned-company | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| organization--treid-invest | Treid-Invest, OOO | organization | commercial-company, evil-corp-member-owned-company | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| organization--tsao-ooo | TSAO, OOO | organization | commercial-company, evil-corp-member-owned-company | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| organization--vertikal-ooo | Vertikal, OOO | organization | commercial-company, evil-corp-member-owned-company | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| organization--yunikom-ooo | Yunikom, OOO | organization | commercial-company, evil-corp-member-owned-company | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-individual--denis-gusev | Denis Igorevich Gusev | threat-actor-individual | evil-corp-senior-member, financial-facilitator, company-director | Russia | 2017 | 2018 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-individual--dmitriy-smirnov | Dmitriy Konstantinovich Smirnov | threat-actor-individual | evil-corp-core-member | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-individual--artem-yakubets | Artem Viktorovich Yakubets | threat-actor-individual | evil-corp-core-member | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-individual--ivan-tuchkov | Ivan Dmitriyevich Tuchkov | threat-actor-individual | evil-corp-core-member | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-individual--andrey-plotnitskiy | Andrey Plotnitskiy | threat-actor-individual | evil-corp-core-member | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-individual--dmitriy-slobodskoy | Dmitriy Alekseyevich Slobodskoy | threat-actor-individual | evil-corp-core-member | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-individual--kirill-slobodskoy | Kirill Alekseyevich Slobodskoy | threat-actor-individual | evil-corp-core-member | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-individual--aleksei-bashlikov | Aleksei Bashlikov | threat-actor-individual | evil-corp-financial-facilitator | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-individual--ruslan-zamulko | Ruslan Zamulko | threat-actor-individual | evil-corp-financial-facilitator | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-individual--david-guberman | David Guberman | threat-actor-individual | evil-corp-financial-facilitator | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-individual--carlos-alvares | Carlos Alvares | threat-actor-individual | evil-corp-financial-facilitator | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-individual--georgios-manidis | Georgios Manidis | threat-actor-individual | evil-corp-financial-facilitator | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-individual--tatiana-shevchuk | Tatiana Shevchuk | threat-actor-individual | evil-corp-financial-facilitator | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-individual--azamat-safarov | Azamat Safarov | threat-actor-individual | evil-corp-financial-facilitator | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-individual--gulsara-burkhonova | Gulsara Burkhonova | threat-actor-individual | evil-corp-financial-facilitator | Russia | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |

### エンティティ関係

| 起点 | 関係 | 終点 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|
| threat-actor-individual--eduard-benderskiy | owns-and-leads | organization--solar-invest | Treasury identifies Benderskiy as founder, 100-percent owner and general director. | 不明 | 不明 | 高 | `source--treasury-evil-corp-fsb-enablers-2024` |
| threat-actor-individual--eduard-benderskiy | owns-and-leads | organization--vympel-assistance | Treasury identifies Benderskiy as founder, 100-percent owner and general director. | 不明 | 不明 | 高 | `source--treasury-evil-corp-fsb-enablers-2024` |
| threat-actor-individual--maksim-yakubets | works-for-on-cyber-tasking | organization--russian-fsb | Treasury states Yakubets worked for the FSB by 2017 and performed state cyber tasks. The specific FSB center is not identified. | 2017 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019` |
| threat-actor-group--evil-corp | overlaps-with | actor--indrik-spider | MITRE ATT&CK lists Evil Corp as an overlapping alias for the Indrik Spider tracking cluster. This preserves the vendor-boundary overlap without asserting exact identity between the human group and the intrusion set. | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| threat-actor-individual--maksim-yakubets | leads | threat-actor-group--evil-corp | Treasury identifies Yakubets as Evil Corp's leader and states that he supervised the group's malicious cyber activity as of 2017. | 2017 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--treasury-evil-corp-fsb-enablers-2024` |
| threat-actor-individual--igor-turashev | administrator-of | threat-actor-group--evil-corp | Treasury states Turashev served as an administrator for Yakubets, controlled Dridex as of 2015 and helped Evil Corp exploit victim networks as of 2017. | 2015 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019` |
| threat-actor-individual--eduard-benderskiy | enables | threat-actor-group--evil-corp | Treasury identifies Benderskiy as a key enabler of Evil Corp's relationship with the Russian state and says he protected the group after the December 2019 sanctions. | 不明 | 不明 | 高 | `source--treasury-evil-corp-fsb-enablers-2024` |
| threat-actor-individual--aleksandr-ryzhenkov | second-in-command-of | threat-actor-group--evil-corp | Treasury identifies Ryzhenkov as Yakubets's long-term associate and Evil Corp second-in-command, and states that he oversaw group operations from at least mid-2017. | 2017-06 | 不明 | 高 | `source--treasury-evil-corp-fsb-enablers-2024` |
| threat-actor-individual--viktor-yakubets | member-of | threat-actor-group--evil-corp | Treasury directly identifies Viktor Yakubets as an Evil Corp member. The full membership period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-fsb-enablers-2024` |
| threat-actor-individual--sergey-ryzhenkov | member-of | threat-actor-group--evil-corp | Treasury directly identifies Sergey Ryzhenkov as an Evil Corp member. The full membership period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-fsb-enablers-2024` |
| threat-actor-individual--aleksey-shchetinin | member-of | threat-actor-group--evil-corp | Treasury directly identifies Shchetinin as an Evil Corp member. The full membership period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-fsb-enablers-2024` |
| threat-actor-individual--beyat-ramazanov | member-of | threat-actor-group--evil-corp | Treasury directly identifies Ramazanov as an Evil Corp member. The full membership period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-fsb-enablers-2024` |
| threat-actor-individual--vadim-pogodin | member-of | threat-actor-group--evil-corp | Treasury directly identifies Pogodin as an Evil Corp member. The full membership period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-fsb-enablers-2024` |
| threat-actor-individual--eduard-benderskiy | formerly-officer-of | organization--russian-fsb | Treasury directly identifies Benderskiy as a former FSB Spetsnaz officer. His service dates and specific FSB component are not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-fsb-enablers-2024` |
| threat-actor-individual--denis-gusev | senior-member-of | threat-actor-group--evil-corp | Treasury directly identifies Gusev as a senior Evil Corp member. The cited 2017 and 2018 conduct observations do not establish the full membership period, so relationship times remain unknown. | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019` |
| threat-actor-individual--dmitriy-smirnov | member-of | threat-actor-group--evil-corp | Treasury directly identifies Smirnov as an additional core Evil Corp member. The full membership period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019` |
| threat-actor-individual--artem-yakubets | member-of | threat-actor-group--evil-corp | Treasury directly identifies Artem Yakubets as an additional core Evil Corp member. The full membership period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019` |
| threat-actor-individual--ivan-tuchkov | member-of | threat-actor-group--evil-corp | Treasury directly identifies Tuchkov as an additional core Evil Corp member. The full membership period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019` |
| threat-actor-individual--andrey-plotnitskiy | member-of | threat-actor-group--evil-corp | Treasury directly identifies Plotnitskiy as an additional core Evil Corp member. The full membership period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019` |
| threat-actor-individual--dmitriy-slobodskoy | member-of | threat-actor-group--evil-corp | Treasury directly identifies Dmitriy Slobodskoy as an additional core Evil Corp member. The full membership period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019` |
| threat-actor-individual--kirill-slobodskoy | member-of | threat-actor-group--evil-corp | Treasury directly identifies Kirill Slobodskoy as an additional core Evil Corp member. The full membership period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019` |
| threat-actor-individual--aleksei-bashlikov | provides-financial-and-material-assistance-to | threat-actor-group--evil-corp | Treasury directly identifies Bashlikov as a financial facilitator providing financial and material assistance to Evil Corp; it does not identify him as a core member. The assistance period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019` |
| threat-actor-individual--ruslan-zamulko | provides-financial-and-material-assistance-to | threat-actor-group--evil-corp | Treasury directly identifies Zamulko as a financial facilitator providing financial and material assistance to Evil Corp; it does not identify him as a core member. The assistance period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019` |
| threat-actor-individual--david-guberman | provides-financial-and-material-assistance-to | threat-actor-group--evil-corp | Treasury directly identifies Guberman as a financial facilitator providing financial and material assistance to Evil Corp; it does not identify him as a core member. The assistance period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019` |
| threat-actor-individual--carlos-alvares | provides-financial-and-material-assistance-to | threat-actor-group--evil-corp | Treasury directly identifies Alvares as a financial facilitator providing financial and material assistance to Evil Corp; it does not identify him as a core member. The assistance period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019` |
| threat-actor-individual--georgios-manidis | provides-financial-and-material-assistance-to | threat-actor-group--evil-corp | Treasury directly identifies Manidis as a financial facilitator providing financial and material assistance to Evil Corp; it does not identify him as a core member. The assistance period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019` |
| threat-actor-individual--tatiana-shevchuk | provides-financial-and-material-assistance-to | threat-actor-group--evil-corp | Treasury directly identifies Shevchuk as a financial facilitator providing financial and material assistance to Evil Corp; it does not identify her as a core member. The assistance period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019` |
| threat-actor-individual--azamat-safarov | provides-financial-and-material-assistance-to | threat-actor-group--evil-corp | Treasury directly identifies Safarov as a financial facilitator providing financial and material assistance to Evil Corp; it does not identify him as a core member. The assistance period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019` |
| threat-actor-individual--gulsara-burkhonova | provides-financial-and-material-assistance-to | threat-actor-group--evil-corp | Treasury directly identifies Burkhonova as a financial facilitator providing financial and material assistance to Evil Corp; it does not identify her as a core member. The assistance period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019` |
| threat-actor-individual--denis-gusev | owns-or-controls | organization--biznes-stolitsa | Treasury identifies Gusev as general director of the company and designated it as owned or controlled by him. The ownership/control period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-individual--denis-gusev | owns-or-controls | organization--optima-ooo | Treasury identifies Gusev as general director of the company and designated it as owned or controlled by him. The ownership/control period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-individual--denis-gusev | owns-or-controls | organization--treid-invest | Treasury identifies Gusev as general director of the company and designated it as owned or controlled by him. The ownership/control period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-individual--denis-gusev | owns-or-controls | organization--tsao-ooo | Treasury identifies Gusev as general director of the company and designated it as owned or controlled by him. The ownership/control period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-individual--denis-gusev | owns-or-controls | organization--vertikal-ooo | Treasury identifies Gusev as general director of the company and designated it as owned or controlled by him. The ownership/control period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| threat-actor-individual--denis-gusev | owns-or-controls | organization--yunikom-ooo | Treasury identifies Gusev as general director of the company and designated it as owned or controlled by him. The ownership/control period is not stated. | 不明 | 不明 | 高 | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |

### 法的措置

| 対象 | 措置 | 当局 | 日付 | 状態 | 説明 | 証拠 |
|---|---|---|---|---|---|---|
| Solar-Invest LLC | sanction | U.S. Department of the Treasury | 2024-10-01 | completed | OFAC designated Solar-Invest LLC as owned or controlled by, or acting for or on behalf of, Eduard Benderskiy. | `source--treasury-evil-corp-fsb-enablers-2024` |
| Vympel-Assistance LLC | sanction | U.S. Department of the Treasury | 2024-10-01 | completed | OFAC designated Vympel-Assistance LLC as owned or controlled by, or acting for or on behalf of, Eduard Benderskiy. | `source--treasury-evil-corp-fsb-enablers-2024` |
| Aleksandr Viktorovich Ryzhenkov | indictment | U.S. District Court for the Northern District of Texas | 不明 | alleged | A federal indictment charged Ryzhenkov with alleged ransomware and money-laundering offenses; DOJ unsealed it on 2024-10-01, but the cited public sources do not state its return date. | `source--fbi-ryzhenkov-wanted`, `source--doj-ryzhenkov-ransomware-2024` |
| Aleksandr Viktorovich Ryzhenkov | wanted | U.S. District Court for the Northern District of Texas | 2023-03-22 | pending | A federal arrest warrant was issued after Ryzhenkov was charged. | `source--fbi-ryzhenkov-wanted` |
| Aleksandr Viktorovich Ryzhenkov | sanction | U.S. Department of the Treasury | 2024-10-01 | completed | Designated for Evil Corp and ransomware activity. | `source--treasury-evil-corp-fsb-enablers-2024` |
| Eduard Vitalevich Benderskiy | sanction | U.S. Department of the Treasury | 2024-10-01 | completed | Designated for enabling Evil Corp and facilitating its relationship with the Russian state. | `source--treasury-evil-corp-fsb-enablers-2024` |
| Igor Olegovich Turashev | indictment | U.S. District Court for the Western District of Pennsylvania | 2019-11-12 | alleged | A federal indictment concerning alleged Bugat/Dridex cybercrime was filed on 2019-11-12 and unsealed on 2019-12-05. | `source--doj-yakubets-turashev-indictment-2019`, `source--doj-yakubets-turashev-2019` |
| Igor Olegovich Turashev | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | Designated for Evil Corp activity. | `source--treasury-evil-corp-sanctions-2019` |
| Maksim Viktorovich Yakubets | indictment | U.S. District Court for the Western District of Pennsylvania | 2019-11-12 | alleged | A federal indictment concerning alleged Bugat/Dridex cybercrime was filed on 2019-11-12 and unsealed on 2019-12-05. | `source--doj-yakubets-turashev-indictment-2019`, `source--doj-yakubets-turashev-2019` |
| Maksim Viktorovich Yakubets | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | Designated as Evil Corp's leader and for malicious cyber activity. | `source--treasury-evil-corp-sanctions-2019` |
| Evil Corp | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | OFAC designated Evil Corp for malicious cyber-enabled activity associated with Dridex. | `source--treasury-evil-corp-sanctions-2019` |
| Viktor Grigoryevich Yakubets | sanction | U.S. Department of the Treasury | 2024-10-01 | completed | Designated for materially supporting Evil Corp. | `source--treasury-evil-corp-fsb-enablers-2024` |
| Sergey Viktorovich Ryzhenkov | sanction | U.S. Department of the Treasury | 2024-10-01 | completed | Designated for materially supporting Evil Corp. | `source--treasury-evil-corp-fsb-enablers-2024` |
| Aleksey Yevgenevich Shchetinin | sanction | U.S. Department of the Treasury | 2024-10-01 | completed | Designated for materially supporting Evil Corp. | `source--treasury-evil-corp-fsb-enablers-2024` |
| Beyat Enverovich Ramazanov | sanction | U.S. Department of the Treasury | 2024-10-01 | completed | Designated for materially supporting Evil Corp. | `source--treasury-evil-corp-fsb-enablers-2024` |
| Vadim Gennadievich Pogodin | sanction | U.S. Department of the Treasury | 2024-10-01 | completed | Designated for materially supporting Evil Corp. | `source--treasury-evil-corp-fsb-enablers-2024` |
| Biznes-Stolitsa, OOO | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | OFAC designated the company for being owned or controlled by Denis Gusev. | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| Optima, OOO | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | OFAC designated the company for being owned or controlled by Denis Gusev. | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| Treid-Invest, OOO | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | OFAC designated the company for being owned or controlled by Denis Gusev. | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| TSAO, OOO | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | OFAC designated the company for being owned or controlled by Denis Gusev. | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| Vertikal, OOO | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | OFAC designated the company for being owned or controlled by Denis Gusev. | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| Yunikom, OOO | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | OFAC designated the company for being owned or controlled by Denis Gusev. | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| Denis Igorevich Gusev | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | OFAC designated Gusev for acting for or on behalf of and providing material assistance to Evil Corp. | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| Dmitriy Konstantinovich Smirnov | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | OFAC designated Smirnov for acting for or on behalf of and providing material assistance to Evil Corp. | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| Artem Viktorovich Yakubets | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | OFAC designated Artem Yakubets for acting for or on behalf of and providing material assistance to Evil Corp. | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| Ivan Dmitriyevich Tuchkov | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | OFAC designated Tuchkov for acting for or on behalf of and providing material assistance to Evil Corp. | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| Andrey Plotnitskiy | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | OFAC designated Plotnitskiy for acting for or on behalf of and providing material assistance to Evil Corp. | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| Dmitriy Alekseyevich Slobodskoy | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | OFAC designated Dmitriy Slobodskoy for acting for or on behalf of and providing material assistance to Evil Corp. | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| Kirill Alekseyevich Slobodskoy | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | OFAC designated Kirill Slobodskoy for acting for or on behalf of and providing material assistance to Evil Corp. | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| Aleksei Bashlikov | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | OFAC designated Bashlikov for providing financial and material assistance to Evil Corp. | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| Ruslan Zamulko | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | OFAC designated Zamulko for providing financial and material assistance to Evil Corp. | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| David Guberman | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | OFAC designated Guberman for providing financial and material assistance to Evil Corp. | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| Carlos Alvares | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | OFAC designated Alvares for providing financial and material assistance to Evil Corp. | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| Georgios Manidis | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | OFAC designated Manidis for providing financial and material assistance to Evil Corp. | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| Tatiana Shevchuk | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | OFAC designated Shevchuk for providing financial and material assistance to Evil Corp. | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| Azamat Safarov | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | OFAC designated Safarov for providing financial and material assistance to Evil Corp. | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |
| Gulsara Burkhonova | sanction | U.S. Department of the Treasury | 2019-12-05 | completed | OFAC designated Burkhonova for providing financial and material assistance to Evil Corp. | `source--treasury-evil-corp-sanctions-2019`, `source--ofac-evil-corp-sdn-update-2019` |

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
- 複数taxonomyスコープ: あり

| データセット | 一致エントリ | 根拠 | 確度 | 帰属候補 | 原典URL |
|---|---|---|---|---|---|
| gtig-threat-actor-naming | 一致なし |  |  |  |  |
| etda-threat-group-cards | Indrik Spider | canonical-name | 高 | Russia | https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/<br>https://www.welivesecurity.com/2018/01/26/friedex-bitpaymer-ransomware-work-dridex-authors/<br>https://www.mcafee.com/blogs/other-blogs/mcafee-labs/spanish-mssp-targeted-by-bitpaymer-ransomware/ |
| cert-ua-uac-index | 一致なし |  |  |  |  |
| microsoft-threat-actor-mapping | Manatee Tempest | canonical-name | 高 | Russia | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| microsoft-threat-actor-mapping | Mustard Tempest | canonical-name | 高 |  | https://github.com/microsoft/mstic/blob/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-threat-actor | INDRIK SPIDER | canonical-name | 高 | RU | https://www.crowdstrike.com/blog/big-game-hunting-the-evolution-of-indrik-spider-from-dridex-wire-fraud-to-bitpaymer-targeted-ransomware/ |
| misp-threat-actor | Evil Corp | single-alias-intersection | 中 |  | https://krebsonsecurity.com/2019/12/inside-evil-corp-a-100m-cybercrime-menace/<br>https://en.wikipedia.org/wiki/Maksim_Yakubets<br>https://www.bbc.com/news/world-us-canada-53195749 |
| misp-microsoft-activity-group | Manatee Tempest | canonical-name | 高 | RU, Russia | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-microsoft-activity-group | Mustard Tempest | canonical-name | 高 |  | https://learn.microsoft.com/en-us/microsoft-365/security/intelligence/microsoft-threat-actor-naming?view=o365-worldwide<br>https://raw.githubusercontent.com/microsoft/mstic/master/PublicFeeds/ThreatActorNaming/MicrosoftMapping.json |
| misp-mitre-enterprise-intrusion-set | Indrik Spider - G0119 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0119<br>https://cloud.google.com/blog/topics/threat-intelligence/unc2165-shifts-to-evade-sanctions/<br>https://home.treasury.gov/news/press-releases/sm845 |
| misp-mitre-intrusion-set | Indrik Spider - G0119 | mitre-external-id | 高 |  | https://attack.mitre.org/groups/G0119<br>https://cloud.google.com/blog/topics/threat-intelligence/unc2165-shifts-to-evade-sanctions/<br>https://home.treasury.gov/news/press-releases/sm845 |
| misp-360net | 一致なし |  |  |  |  |
| misp-tidal-groups | Indrik Spider | canonical-name | 高 | RU |  |

### 関係性候補（未統合）

| 対象 | 関係 | データセット | 確度 | 評価 |
|---|---|---|---|---|
| Mustard Tempest | similar | misp-threat-actor | 低 | MISP Galaxy relationship candidate. Review the original references and actor scopes before integration. |

### クロスチェック上の制約

- Exact normalized-name matching does not prove one-to-one actor identity.
- MISP Galaxy is an aggregation layer; original references remain authoritative.
- A no-match result means no exact match in the fixed datasets, not that the actor does not exist.
- A Malpedia name match confirms catalogue presence only, not actor use.

## Capability

### マルウェア

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| malware--bitpaymer | BitPaymer | [BitPaymer](https://attack.mitre.org/software/S0570) is a ransomware variant first observed in August 2017 targeting hospitals in the U.K. [BitPaymer](https://attack.mitre.org/software/S0570) uses a unique encryption key, ransom note, and contact information for each operation. [BitPaymer](https://attack.mitre.org/software/S0570) has several indicators suggesting overlap with the [Dridex](https://attack.mitre.org/software/S0384) malware and is often delivered via [Dridex](https://attack.mitre.org/software/S0384).(Citation: Crowdstrike Indrik November 2018) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--cobalt-strike | Cobalt Strike | [Cobalt Strike](https://attack.mitre.org/software/S0154) is a commercial, full-featured, remote access tool that bills itself as “adversary simulation software designed to execute targeted attacks and emulate the post-exploitation actions of advanced threat actors”. Cobalt Strike’s interactive post-exploit capabilities cover the full range of ATT&CK tactics, all executed within a single, integrated system.(Citation: cobaltstrike manual)<br><br>In addition to its own capabilities, [Cobalt Strike](https://attack.mitre.org/software/S0154) leverages the capabilities of other well-known tools such as Metasploit and [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: cobaltstrike manual) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--dridex | Dridex | [Dridex](https://attack.mitre.org/software/S0384) is a prolific banking Trojan that first appeared in 2014. By December 2019, the US Treasury estimated [Dridex](https://attack.mitre.org/software/S0384) had infected computers in hundreds of banks and financial institutions in over 40 countries, leading to more than $100 million in theft. [Dridex](https://attack.mitre.org/software/S0384) was created from the source code of the Bugat banking Trojan (also known as Cridex).(Citation: Dell Dridex Oct 2015)(Citation: Kaspersky Dridex May 2017)(Citation: Treasury EvilCorp Dec 2019) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| malware--wastedlocker | WastedLocker | [WastedLocker](https://attack.mitre.org/software/S0612) is a ransomware family attributed to [Indrik Spider](https://attack.mitre.org/groups/G0119) that has been used since at least May 2020. [WastedLocker](https://attack.mitre.org/software/S0612) has been used against a broad variety of sectors, including manufacturing, information technology, and media.(Citation: Symantec WastedLocker June 2020)(Citation: NCC Group WastedLocker June 2020)(Citation: Sentinel Labs WastedLocker July 2020)  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

### ツール

| ID | 名称 | 説明 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|
| tool--donut | Donut | [Donut](https://attack.mitre.org/software/S0695) is an open source framework used to generate position-independent shellcode.(Citation: Donut Github)(Citation: Introducing Donut) [Donut](https://attack.mitre.org/software/S0695) generated code has been used by multiple threat actors to inject and load malicious payloads into memory.(Citation: NCC Group WastedLocker June 2020) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| tool--empire | Empire | [Empire](https://attack.mitre.org/software/S0363) is an open-source, cross-platform remote administration and post-exploitation framework that is publicly available on GitHub. While the tool itself is primarily written in Python, the post-exploitation agents are written in pure [PowerShell](https://attack.mitre.org/techniques/T1059/001) for Windows and Python for Linux/macOS. [Empire](https://attack.mitre.org/software/S0363) was one of five tools singled out by a joint report on public hacking tools being widely used by adversaries.(Citation: NCSC Joint Report Public Tools)(Citation: Github PowerShell Empire)(Citation: GitHub ATTACK Empire) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| tool--mimikatz | Mimikatz | [Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation: Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| tool--psexec | PsExec | [PsExec](https://attack.mitre.org/software/S0029) is a free Microsoft tool that can be used to execute a program on another computer. It is used by IT administrators and attackers.(Citation: Russinovich Sysinternals)(Citation: SANS PsExec) | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

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

活動履歴なし

### 活動別ダイヤモンドモデル

活動別ダイヤモンドモデルなし



## ターゲット

ターゲット情報なし

選定ロジック: 標的国・地域は、活動本文、MITRE ATT&CK、一次資料でレビューした個別補正から収録する。ETDA、MISP、旧ワークブック等の集約値はexternal research leadに隔離する。帰属国、インフラ所在国、帰属表明国は除外し、日本は確認できた場合に地域表示とは別に個別保持する。

## 被害事例

構造化された被害事例なし

## MITRE ATT&CK Matrixデータ

| Tactic | Technique ID | Technique | 観測内容 | マルウェア | 活動 | 初回 | 最終 | 確度 | 証拠 |
|---|---|---|---|---|---|---|---|---|---|
| Credential Access | T1003.001 | LSASS Memory | [Indrik Spider](https://attack.mitre.org/groups/G0119) used [Cobalt Strike](https://attack.mitre.org/software/S0154) to carry out credential dumping using ProcDump.(Citation: Symantec WastedLocker June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1007 | System Service Discovery | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used the win32_service WMI class to retrieve a list of services from the system.(Citation: Symantec WastedLocker June 2020)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1012 | Query Registry | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used a service account to extract copies of the `Security` Registry hive.(Citation: Mandiant_UNC2165) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Discovery | T1018 | Remote System Discovery | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used PowerView to enumerate all Windows Server, Windows Server 2003, and Windows 7 instances in the Active Directory database.(Citation: Symantec WastedLocker June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Lateral Movement | T1021.001 | Remote Desktop Protocol | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used RDP for lateral movement.(Citation: Mandiant_UNC2165) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Lateral Movement | T1021.004 | SSH | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used SSH for lateral movement.(Citation: Mandiant_UNC2165) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Stealth | T1036.005 | Match Legitimate Resource Name or Location | [Indrik Spider](https://attack.mitre.org/groups/G0119) used fake updates for FlashPlayer plugin and Google Chrome as initial infection vectors.(Citation: Crowdstrike Indrik November 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1047 | Windows Management Instrumentation | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used WMIC to execute commands on remote computers.(Citation: Symantec WastedLocker June 2020)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.001 | PowerShell | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used PowerShell [Empire](https://attack.mitre.org/software/S0363) for execution of malware.(Citation: Crowdstrike Indrik November 2018)(Citation: Symantec WastedLocker June 2020)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.003 | Windows Command Shell | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used batch scripts on victim's machines.(Citation: Crowdstrike Indrik November 2018)(Citation: Mandiant_UNC2165) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1059.007 | JavaScript | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used malicious JavaScript files for several components of their attack.(Citation: Symantec WastedLocker June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Collection | T1074.001 | Local Data Staging | [Indrik Spider](https://attack.mitre.org/groups/G0119) has stored collected data in a .tmp file.(Citation: Symantec WastedLocker June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078 | Valid Accounts | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used valid accounts for initial access and lateral movement.(Citation: Mandiant_UNC2165) [Indrik Spider](https://attack.mitre.org/groups/G0119) has also maintained access to the victim environment through the VPN infrastructure.(Citation: Mandiant_UNC2165) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Initial Access, Persistence, Privilege Escalation, Stealth | T1078.002 | Domain Accounts | [Indrik Spider](https://attack.mitre.org/groups/G0119) has collected credentials from infected systems, including domain accounts.(Citation: Crowdstrike Indrik November 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Command And Control | T1105 | Ingress Tool Transfer | [Indrik Spider](https://attack.mitre.org/groups/G0119) has downloaded additional scripts, malware, and tools onto a compromised host.(Citation: Crowdstrike Indrik November 2018)(Citation: Symantec WastedLocker June 2020)(Citation: Mandiant_UNC2165) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Defense Impairment, Persistence | T1112 | Modify Registry | [Indrik Spider](https://attack.mitre.org/groups/G0119) has modified registry keys to prepare for ransomware execution and to disable common administrative utilities.(Citation: Mandiant_UNC2165) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Persistence | T1136 | Create Account | [Indrik Spider](https://attack.mitre.org/groups/G0119) used <code>wmic.exe</code> to add a new user to the system.(Citation: Symantec WastedLocker June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Persistence | T1136.001 | Local Account | [Indrik Spider](https://attack.mitre.org/groups/G0119) has created local system accounts and has added the accounts to privileged groups.(Citation: Mandiant_UNC2165) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Execution | T1204.002 | Malicious File | [Indrik Spider](https://attack.mitre.org/groups/G0119) has attempted to get users to click on a malicious zipped file.(Citation: Symantec WastedLocker June 2020)  |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Defense Impairment, Privilege Escalation | T1484.001 | Group Policy Modification | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used Group Policy Objects to deploy batch scripts.(Citation: Crowdstrike Indrik November 2018)(Citation: Mandiant_UNC2165) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Impact | T1486 | Data Encrypted for Impact | [Indrik Spider](https://attack.mitre.org/groups/G0119) has encrypted domain-controlled systems using [BitPaymer](https://attack.mitre.org/software/S0570).(Citation: Crowdstrike Indrik November 2018) Additionally, [Indrik Spider](https://attack.mitre.org/groups/G0119) used [PsExec](https://attack.mitre.org/software/S0029) to execute a ransomware script.(Citation: Mandiant_UNC2165) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Impact | T1489 | Service Stop | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used [PsExec](https://attack.mitre.org/software/S0029) to stop services prior to the execution of ransomware.(Citation: Symantec WastedLocker June 2020) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Credential Access | T1552.001 | Credentials In Files | [Indrik Spider](https://attack.mitre.org/groups/G0119) has searched files to obtain and exfiltrate credentials.(Citation: Mandiant_UNC2165) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Credential Access | T1555.005 | Password Managers | [Indrik Spider](https://attack.mitre.org/groups/G0119) has accessed and exported passwords from password managers.(Citation: Mandiant_UNC2165) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Credential Access | T1558.003 | Kerberoasting | [Indrik Spider](https://attack.mitre.org/groups/G0119) has conducted Kerberoasting attacks using a module from GitHub.(Citation: Mandiant_UNC2165) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | [Indrik Spider](https://attack.mitre.org/groups/G0119) has exfiltrated data using [Rclone](https://attack.mitre.org/software/S1040) or MEGASync prior to deploying ransomware.(Citation: Mandiant_UNC2165) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1583 | Acquire Infrastructure | [Indrik Spider](https://attack.mitre.org/groups/G0119) has purchased access to victim VPNs to facilitate access to victim environments.(Citation: Mandiant_UNC2165)    |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1584.004 | Server | [Indrik Spider](https://attack.mitre.org/groups/G0119) has served fake updates via legitimate websites that have been compromised.(Citation: Crowdstrike Indrik November 2018)	 |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1585.002 | Email Accounts | [Indrik Spider](https://attack.mitre.org/groups/G0119) has created email accounts to communicate with their ransomware victims, to include providing payment and decryption details.(Citation: Crowdstrike Indrik November 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Resource Development | T1587.001 | Malware | [Indrik Spider](https://attack.mitre.org/groups/G0119) has developed malware for their operations, including ransomware such as [BitPaymer](https://attack.mitre.org/software/S0570) and [WastedLocker](https://attack.mitre.org/software/S0612).(Citation: Crowdstrike Indrik November 2018) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Reconnaissance | T1590 | Gather Victim Network Information | [Indrik Spider](https://attack.mitre.org/groups/G0119) has downloaded tools, such as the Advanced Port Scanner utility and Lansweeper, to conduct internal reconnaissance of the victim network. [Indrik Spider](https://attack.mitre.org/groups/G0119) has also accessed the victim’s VMware VCenter, which had information about host configuration, clusters, etc.(Citation: Mandiant_UNC2165) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Defense Impairment | T1685 | Disable or Modify Tools | [Indrik Spider](https://attack.mitre.org/groups/G0119) used [PsExec](https://attack.mitre.org/software/S0029) to leverage Windows Defender to disable scanning of all downloaded files and to restrict real-time monitoring.(Citation: Symantec WastedLocker June 2020) [Indrik Spider](https://attack.mitre.org/groups/G0119) has used `MpCmdRun` to revert the definitions in Microsoft Defender.(Citation: Mandiant_UNC2165) Additionally, [Indrik Spider](https://attack.mitre.org/groups/G0119) has used WMI to stop or uninstall and reset anti-virus products and other defensive services.(Citation: Mandiant_UNC2165) |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |
| Defense Impairment | T1685.005 | Clear Windows Event Logs | [Indrik Spider](https://attack.mitre.org/groups/G0119) has used [Cobalt Strike](https://attack.mitre.org/software/S0154) to empty log files.(Citation: Symantec WastedLocker June 2020) Additionally, [Indrik Spider](https://attack.mitre.org/groups/G0119) has cleared all event logs using `wevutil`.(Citation: Mandiant_UNC2165)    |  |  | 不明 | 不明 | 高 | `source--mitre-attack-19-2` |

## IOC／artifact概要

- IOC値: 1件
- IOC観測: 1件
- 複数攻撃で観測: 0件
- 要レビュー候補: 1件
- 非IOC artifact観測: 1件（`artifacts.csv`）

## 主要判断と不確実性

主要判断なし

### 情報ギャップ

- Unknown observation dates must not be replaced by publication dates.
- Automatically mapped aliases, targets, and workbook software require analyst review.

### 不確実性

- Vendor cluster boundaries may differ from the canonical name used here.
- Motivation lead 'financial-gain' is not canonical; only aggregation/workbook evidence is available.

## 出典

| Source ID | タイトル | 発行者 | 発行日 | パス | 種別 | TLP | 信頼度 |
|---|---|---|---|---|---|---|---|
| source--actor-mapping-workbook | APT Groups and Operations | Florian Roth and community contributors | 不明 | APT Groups and Operations.xlsx | community-actor-mapping | TLP:CLEAR | 中 |
| source--indrik-spider--a7807818688b2d13 | indrik spider |  | 不明 | actor_profile/evidence/indrik-spider.csv | structured-data | TLP:CLEAR | 中 |
| source--indrik-spider--64297ef3a630cbbc | A Threat Actor Encyclopedia |  | 不明 | A_Threat_Actor_Encyclopedia.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--cbadaaf90ee50632 | google fog of war research report |  | 不明 | International Strategic/Russia/google_fog_of_war_research_report.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--6fd598fe1fcac443 | SilverFish Solarwinds |  | 不明 | SunBurst/SilverFish_Solarwinds.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--ce53bebb42542a0d | Threat Group Cards |  | 不明 | Threat Group Cards.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--f80c8c2cfdcc741c | Threat Group Cards v2.0 |  | 不明 | Threat_Group_Cards_v2.0.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--6cec91c3e1522995 | Virtual Routes Pharos Report Series No. 3 |  | 不明 | cybercrime/2025/Virtual-Routes-Pharos-Report-Series-No.-3.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--bcf3ee52f21f524c | Evil Corp   Behind the Screens |  | 不明 | cybercrime/Evil Corp/Evil Corp - Behind the Screens.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--4c793f9b8d13e8c7 | PWC cyber threats 2019 retrospect |  | 2019 | summary/2020/PWC-cyber-threats-2019-retrospect.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--06ed0ce775c23234 | 2021 Threat Detection Report |  | 2021 | summary/2021/2021-Threat-Detection-Report.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--d7560bf8da8f051e | The CrowdStrike 2021 Global Threat Report |  | 2021 | summary/2021/The CrowdStrike 2021 Global Threat Report.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--63e9d1d33d42c6f5 | APT group Intelligence Research handbook 2022 |  | 2022 | summary/2022/APT group Intelligence Research handbook-2022.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--9c231dd3135e2ac2 | sophos 2022 threat report |  | 2022 | summary/2022/sophos-2022-threat-report.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--07dfdf4511cd0ab2 | 2022 year in retrospect report |  | 2022 | summary/2023/2022-year-in-retrospect-report.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--0da34bbcf3843eea | ACD6 full report |  | 不明 | summary/2023/ACD6-full-report.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--5455e07d866f14be | M Trends 2023 Report MANDIANT SPECIAL REPORT |  | 2023 | summary/2023/M-Trends 2023 Report MANDIANT SPECIAL REPORT.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--67ee214b27cfb27b | Secureworks NC3 2022StateoftheThreat |  | 2022 | summary/2023/Secureworks_NC3_2022StateoftheThreat.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--3a26666f1cbd15d7 | group ib hi tech crime trends 2022 2023 ru |  | 不明 | summary/2023/group-ib-hi-tech-crime-trends-2022-2023-ru.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--cce2a9fb9c14aa85 | Symantec Ransomware Threat Landscape 2024 |  | 2024 | summary/2024/Symantec_Ransomware_Threat_Landscape_2024.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--ffb588856d1ede30 | m trends 2024 |  | 2024 | summary/2024/m-trends-2024.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--1c5eee2c100e607f | threat actor list from cs |  | 不明 | summary/2024/threat actor list from cs.csv | structured-data | TLP:CLEAR | 中 |
| source--indrik-spider--5e5b3bd442704da0 | 2024 Annual Cybersecurity Vulnerability Threat Landscape Research Report |  | 2024 | summary/2025/2024_Annual_Cybersecurity_Vulnerability_Threat_Landscape_Research_Report.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--9b2374e1fc7db4e4 | 2025 Cyber Security Report Final |  | 2025 | summary/2025/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--586bfdab8f414282 | 2025 dbir data breach investigations report |  | 2025 | summary/2025/2025-dbir-data-breach-investigations-report.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--afca2bbe5bba46c5 | Cyber Threat Intelligence Report 2025 2 |  | 2025 | summary/2025/Cyber Threat Intelligence Report 2025 2.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--30823fe563da2031 | Global Threat Report 2025 |  | 2025 | summary/2025/Global Threat Report 2025.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--0db6e1bbb4d6a408 | m trends 2025 en |  | 2025 | summary/2025/m-trends-2025-en.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--be3e5eb6e4f751c3 | threat horizons report h1 2025 |  | 2025 | summary/2025/threat_horizons_report_h1_2025.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--ff48255298008637 | 2025 Cyber Security Report Final |  | 2025 | summary/2026/2025 Cyber Security Report_Final.pdf | report | TLP:CLEAR | 中 |
| source--indrik-spider--7338c1599b9f719e | HJS Crypto Currency Report web final |  | 不明 | summary/2026/HJS-Crypto-Currency-Report-web-final.pdf | report | TLP:CLEAR | 中 |
| source--osint-misp-microsoft-activity-group | MISP Galaxy Microsoft Activity Group | MISP Project / Microsoft | 不明 | actor_profile/reference/osint/misp-microsoft-activity-group.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-mitre-intrusion-set | MISP Galaxy MITRE Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-threat-actor | MISP Galaxy Threat Actor | MISP Project | 不明 | actor_profile/reference/osint/misp-threat-actor.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--osint-microsoft-threat-actor-mapping | Microsoft Threat Actor Naming Mapping | Microsoft | 不明 | actor_profile/reference/osint/microsoft-threat-actor-mapping.json | official-vendor-actor-mapping | TLP:CLEAR | 高 |
| source--osint-etda-threat-group-cards | Threat Group Cards: A Threat Actor Encyclopedia | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--osint-misp-mitre-enterprise-intrusion-set | MISP Galaxy MITRE Enterprise ATT&CK Intrusion Set | MISP Project / MITRE ATT&CK | 不明 | actor_profile/reference/osint/misp-mitre-enterprise-attack-intrusion-set.json | structured-osint-aggregation | TLP:CLEAR | 高 |
| source--osint-misp-tidal-groups | MISP Galaxy TIDAL Groups | MISP Project / TIDAL Cyber | 不明 | actor_profile/reference/osint/misp-tidal-groups.json | structured-osint-aggregation | TLP:CLEAR | 中 |
| source--target-audit-etda-threat-group-cards | ETDA Threat Group Cards observed-country fields | ETDA / ThaiCERT | 不明 | actor_profile/reference/osint/etda-threat-group-cards.json | government-threat-actor-encyclopedia | TLP:CLEAR | 中 |
| source--mitre-attack-19-1 | MITRE Enterprise ATT&CK 19.1 compact local index | MITRE | 2026-05-12 | actor_profile/reference/attack-enterprise-19.1.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--mitre-attack-19-2 | MITRE Enterprise ATT&CK 19.2 compact local index | MITRE | 2026-08-05 | actor_profile/reference/attack-index.json | structured-knowledge-base | TLP:CLEAR | 高 |
| source--treasury-evil-corp-fsb-enablers-2024 | Treasury Sanctions Members of the Russia-Based Cybercriminal Group Evil Corp in Tri-Lateral Action with the United Kingdom and Australia | U.S. Department of the Treasury | 2024-10-01 | https://home.treasury.gov/news/press-releases/jy2623 | government-sanctions | TLP:CLEAR | 高 |
| source--treasury-evil-corp-sanctions-2019 | Treasury Sanctions Evil Corp, the Russia-Based Cybercriminal Group Behind Dridex Malware | U.S. Department of the Treasury | 2019-12-05 | https://home.treasury.gov/news/press-releases/sm845 | government-sanctions | TLP:CLEAR | 高 |
| source--doj-yakubets-turashev-2019 | Russian National Charged with Decade-Long Series of Hacking and Bank Fraud Offenses Resulting in Tens of Millions in Losses and Second Russian National Charged with Involvement in Deployment of Bugat Malware | U.S. Department of Justice | 2019-12-05 | https://www.justice.gov/archives/opa/pr/russian-national-charged-decade-long-series-hacking-and-bank-fraud-offenses-resulting-tens | government-legal | TLP:CLEAR | 高 |
| source--doj-ryzhenkov-ransomware-2024 | Russian National Indicted for Series of Ransomware Attacks | U.S. Department of Justice | 2024-10-01 | https://www.justice.gov/archives/opa/pr/russian-national-indicted-series-ransomware-attacks | government-legal | TLP:CLEAR | 高 |
| source--fbi-ryzhenkov-wanted | Aleksandr Ryzhenkov | Federal Bureau of Investigation | 不明 | https://www.fbi.gov/wanted/cyber/aleksandr-ryzhenkov | government-wanted-notice | TLP:CLEAR | 高 |
| source--doj-yakubets-turashev-indictment-2019 | Indictment: United States v. Maksim Yakubets and Igor Turashev | U.S. District Court for the Western District of Pennsylvania | 不明 | https://www.justice.gov/d9/press-releases/attachments/2019/12/05/final_yakubetsturashev_indictment_wdpa_0.pdf | government-legal | TLP:CLEAR | 高 |
| source--ofac-evil-corp-sdn-update-2019 | Cyber-related Designations; Counter Terrorism Designation Removal | U.S. Department of the Treasury, Office of Foreign Assets Control | 2019-12-05 | https://ofac.treasury.gov/recent-actions/20191205 | government-sanctions-list | TLP:CLEAR | 高 |

## 自由記述

自動構造化した項目はdraftであり、candidateとunknownを分析者がレビューする。
