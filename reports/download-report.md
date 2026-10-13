# 下载执行报告

生成时间：2026-10-13T03:09:37+00:00

已登记本地原文件：146；其中资料/仓库文件：107；文档快照：39。

这里只统计真正写入磁盘并记录校验值的文件。下载成功不代表标准符合性、imports 闭包或正式发行版。

任务状态：`{"skipped": 3, "failed": 38, "saved": 64, "partial": 2}`

| 资源 | 本地文件数 | 资料性质 / 后续要求 |
|---|---:|---|
| BFO 2020 / ISO 21838-2 配套实现 | 1 | 保留 BFO 2020 仓库定位；不要把仓库版本名称与早期 BFO 2.0 简单视为同一发布包。 |
| DOLCE | 3 | 官方 DOLCE 的一阶逻辑形式与 DOLCE Lite、DUL 的 OWL 重构版本须分别管理。 |
| UFO / OntoUML 文档 | 0 | 原链接是 OntoUML 语言文档，不是一个完整的 UFO OWL 本体文件。 |
| SUMO | 0 | 下载仓库原始表示；不要假定其原生逻辑内容能作为普通 OWL DL 本体直接导入。 |
| GFO | 0 | 完整本体采用模块组织；离线使用还需检查 imports 与版本 IRI。 |
| OWL 2 | 2 | 语言规范，不是行业本体；附带词汇文件也不等于规范的全部语义。 |
| RDF 1.1 | 3 | 保留原指定 RDF 1.1；不把 RDF 图数据与 OWL 逻辑本体混称。 |
| SKOS | 2 | 规范文档与机器可读词汇分别下载。 |
| PROV-O | 2 | 溯源词汇与规范；保留上游命名空间。 |
| DCAT 3 | 3 | 优先下载明确的 dcat3 序列化，避免与其他版本混淆。 |
| SSN / SOSA | 3 | 在基础设施与能源类别中交叉引用；原文件仅存一份。 |
| Schema.org | 2 | 沿用原目录位置，但 Schema.org 不等同于 W3C Recommendation；数据词汇与文档分开。 |
| SPARQL 1.1 | 0 | 查询语言规范，不是 OWL 本体文件。 |
| IOF 工业本体 | 0 | 下载仓库快照；快照不自动等同于已正式发布的 IOF 版本。 |
| STEP / ISO 10303-242 | 0 | 原 ISO 链接只覆盖 AP242:2022，并非整个 ISO 10303 系列；不自动下载付费标准正文。 |
| OntoSTEP | 0 | 保留 NIST 实现仓库，与 ISO 标准正文分开；下载成功不证明覆盖整个 STEP 系列。 |
| RAMI 4.0 | 1 | 参考架构文档，不是可直接导入的 OWL 行业本体。 |
| AAS / IDTA | 1 | 原仓库已重定向到元模型仓库；该仓库不代表所有 AAS API 与子模型模板。 |
| SAREF4INMA | 3 | 已核实页面指向 v2.1.1；下载该版本正文与序列化，imports 仍需另行检查。 |
| IEC CIM / 第三方 OWL 实现 | 0 | IEC TC57 页面和第三方 CIM-OWL 仓库分开保留；本次未能核实原仓库，不视为 IEC 官方 OWL 发布。 |
| IEC 61850 | 0 | 原链接只是 IEC 首页，无法唯一定位系列规范、分册、版本或可下载包。 |
| SAREF4ENER | 2 | 下载其公开序列化；实际版本以下载报告为准。 |
| ISO 15926 系列 | 0 | 原链接错配为 ISO 15614-11:2025；新增正确的 Part 2 数据模型标准入口。 |
| ISO 15926 RDF/OWL 实现候选 | 0 | 本次未能核实原 GitHub 仓库可用性；保留待核验，不能认定为完整标准实现。 |
| OSDU | 0 | 生态与平台入口，不存在一个代表整个 OSDU 的单一本体文件；只收录入口与可选单页快照。 |
| PPDM | 0 | 需到发布方确认版本、会员/许可与下载范围；工具不使用账户或绕过登录。 |
| FIBO | 1 | 仓库与浏览器合并为一项；仓库默认分支快照不自动等于 production 发布版。 |
| OMG Commons 1.2 / 1.3 | 83 | 保留 1.2 历史版本；1.3 已于 2026 年 6 月正式采纳，不再标为 beta。 |
| ACTUS | 1 | 标准与生态入口，不等同于单个 OWL 本体；可选保存介绍页。 |
| SNOMED CT | 0 | 浏览器和下载入口合并；需按地区及用途核对许可并从官方渠道取得发行包。 |
| HL7 FHIR | 1 | FHIR 规范、结构定义与数据实例不是同一类资源；不把整个站点冒充一份本体。 |
| HL7 FHIR RDF | 3 | 保留 RDF 表示规范；标准描述页面并不等于本地已经存在完整 RDF 发行包。 |
| OBO Foundry | 1 | 注册目录不是一个本体；不自动递归下载所有成员本体。 |
| Gene Ontology | 1 | 配置公开 go-basic.obo 下载候选；它不是全部 GO 注释数据或所有产品。 |
| ChEBI | 1 | 大型资源按需下载；词汇、本体与化合物数据库应分别管理。 |
| UBERON | 0 | 仓库可能较大；源码快照不等于包含所有依赖的发行产品。 |
| LOINC | 0 | 需从官方下载页选择版本并接受相应使用条款；不自动处理注册登录。 |
| RxNorm | 0 | 完整发行包与其他下载产品许可范围不同；从官方入口人工选择，不默认整包可自由再分发。 |
| ICD-11 MMS / 2025-01 | 0 | 保留用户指定的 2025-01 历史版本；浏览器入口不等于可下载的完整发行包。 |
| MeSH | 1 | 先在官方页面选择年度和发行格式；不把官网首页当作完整词表。 |
| IFC | 0 | 规范与 schema 按发行版管理；IFC 与 ifcOWL 不合并为同一个文件。 |
| ifcOWL / IFC4 ADD2 TC1 | 0 | 保留原指定 IFC4 ADD2 TC1 路径；不宣称与其他 IFC 版本完全等价。 |
| BOT | 0 | 官网与仓库合并；保留源文件、语言标签与许可证。 |
| CityGML 3.0 | 3 | 概念模型与编码实现分开；仅抓取入口页直接链接的选定资料，不镜像整个 OGC。 |
| ISO 23387 / BIM 数据模板 | 0 | 原入口未成功访问；新增官方 ISO 23387:2025 入口，标准正文按官方许可获取。 |
| GS1 Web Vocabulary | 0 | 词汇与企业商品主数据不是一回事；不抓取商品实例数据。 |
| GS1 CBV | 1 | 当前原链接返回 CBV 2.0 PDF；原清单的 ISO/IEC 19988:2024 标注本次未独立核验。 |
| EPCIS 2.0 | 1 | 下载规范及页面直接链接的 schema；不将其称作一份完整 OWL 本体。 |
| GoodRelations | 1 | 保留原官网并尝试公开 OWL 序列化；历史 HTTP 入口可能跳转或失效。 |
| UN/CEFACT | 0 | 组织入口覆盖多项标准，需进一步指定业务范围和版本才能获得完整资料集。 |
| SAREF 核心与扩展索引 | 2 | 下载核心及本清单列出的扩展；“全系列”索引不代表已下载网站上所有扩展。 |
| SAREF4CITY | 2 | 实际版本与序列化以下载日志为准。 |
| SAREF4BLDG | 2 | 实际版本与序列化以下载日志为准。 |
| SAREF4WATR | 2 | 实际版本与序列化以下载日志为准。 |
| oneM2M 基础本体入口 | 0 | 原页面是规范索引；需选择适用的 Base Ontology 分册和版本，而非整个标准目录。 |
| SMOF（待核验） | 0 | 本次未能核实 wddabc/SMOF 仓库的可访问性和所指资源，不猜测替代项目。 |
| ISO/IEC 30173:2023 | 0 | 数字孪生概念与术语标准，不是可直接导入的 OWL 数据包。 |
| DTDL | 0 | 建模语言与模型定义格式；不要当作 OWL 本体直接交给 OWL 推理机。 |
| W3C WoT Thing Description | 1 | 下载指定规范及直接链接的机器可读附属文件；区分规范版本与设备实例。 |
| IDO / ISO 23726-3 | 0 | 原 URL 指向 ISO 5409:2024。正确入口为 ISO/FDIS 23726-3，当前仍处于审批阶段。 |
| LKIF Core | 0 | 下载完整模块仓库；离线使用时检查所有 imports。 |
| OASIS LegalRuleML 1.0 | 2 | 法律规则交换格式，不等于一个 OWL 本体；保留规范与 schema。 |
| Akoma Ntoso | 0 | 法律文档结构化格式；门户不是完整机器可读发行包。 |
| ELI | 1 | 官方说明页与其直接链接的本体/规范分开；不抓取全部欧盟法律正文。 |
| ODRL | 2 | 保留模型规范与词汇；不把模型表达直接等同于法律有效性判断。 |
| AGROVOC | 0 | 浏览器与 SPARQL 接口合并；SPARQL endpoint 是服务地址，不是离线全量文件。 |
| SAREF4AGRI | 2 | 实际版本与序列化以下载日志为准。 |
| FoodOn | 0 | 大型本体仓库，按需选择；保留依赖和许可信息。 |
| AgrO / AgroOntology | 2 | 配置 OBO 官方持久地址作为下载候选；记录实际重定向与版本，不把页面下载当成本体下载。 |
| DATEX II | 0 | 下载入口可能需要选择模型配置和发行版；不尝试登录或替用户接受条款。 |
| SIRI | 0 | 原入口未指定分册、版本或 schema 包；保留给人工选择。 |
| Transmodel / NeTEx | 0 | 两者属于相关但不同层次的资源，保留组合原条目并说明范围，不能合并语义。 |
| OpenTripModel 5 | 0 | 保留 OTM 5 文档及公开的直接附属文件；不是 OWL 本体默认入口。 |
| GTFS Schedule | 1 | 规范与真实运营机构的 feed 不同；本包不包含各地时刻表数据。 |
| Linked GTFS | 0 | 保留原项目仓库；不假定它与最新 GTFS 所有字段完全同步。 |

## 失败、部分完成及跳过的任务

- `cim-repository` — skipped：unverified_source
- `iso15926-impl-repository` — skipped：unverified_source
- `smof-repository` — skipped：unverified_source
- `bfo-repository` — failed：DownloadError: HTTP Error 403: rate limit exceeded
- `ontouml-repository` — failed：DownloadError: HTTP Error 403: rate limit exceeded
- `sumo-repository` — failed：DownloadError: HTTP Error 403: rate limit exceeded
- `gfo-repository` — failed：DownloadError: HTTP Error 403: rate limit exceeded
- `iof-repository` — failed：DownloadError: HTTP Error 403: rate limit exceeded
- `ontostep-repository` — failed：DownloadError: HTTP Error 403: rate limit exceeded
- `aas-repository` — failed：DownloadError: HTTP Error 403: rate limit exceeded
- `rami40-discover-1` — failed：DownloadError: No matching direct files found; portal retained for manual selection
- `fibo-repository` — failed：DownloadError: HTTP Error 403: rate limit exceeded
- `osdu-doc-1` — failed：DownloadError: Redirect/discovery host not on the curated allow-list: www.opengroup.org
- `fhir-discover-1` — failed：DownloadError: No matching direct files found; portal retained for manual selection
- `go-asset-1` — failed：DownloadError: Redirect/discovery host not on the curated allow-list: current.geneontology.org
- `chebi-discover-1` — failed：DownloadError: No matching direct files found; portal retained for manual selection
- `uberon-repository` — failed：DownloadError: HTTP Error 403: rate limit exceeded
- `ifc-discover-1` — failed：DownloadError: HTTP Error 403: Forbidden
- `ifc-doc-1` — failed：DownloadError: HTTP Error 403: Forbidden
- `ifcowl-discover-1` — failed：DownloadError: HTTP Error 403: Forbidden
- `ifcowl-doc-1` — failed：DownloadError: HTTP Error 403: Forbidden
- `bot-repository` — failed：DownloadError: HTTP Error 403: rate limit exceeded
- `bot-doc-1` — failed：DownloadError: Redirect/discovery host not on the curated allow-list: w3c-lbd-cg.github.io
- `commons-discover-1` — partial：{"status": "partial", "at": "2026-10-13T03:08:32+00:00", "resource_id": "commons", "saved_files": 40, "errors": [], "omitted_due_to_limit": 61}
- `commons-discover-2` — partial：{"status": "partial", "at": "2026-10-13T03:08:32+00:00", "resource_id": "commons", "saved_files": 40, "errors": [], "omitted_due_to_limit": 1}
- `gs1voc-discover-1` — failed：DownloadError: HTTP Error 403: Forbidden
- `gs1voc-doc-1` — failed：DownloadError: HTTP Error 403: Forbidden
- `goodrelations-asset-1` — failed：DownloadError: Redirect/discovery host not on the curated allow-list: purl.archive.org
- `uncefact-doc-1` — failed：DownloadError: HTTP Error 403: Forbidden
- `onem2m-doc-1` — failed：DownloadError: HTTP Error 403: Forbidden
- `dtdl-repository` — failed：DownloadError: HTTP Error 403: rate limit exceeded
- `lkif-repository` — failed：DownloadError: HTTP Error 403: rate limit exceeded
- `wot-td-discover-1` — failed：DownloadError: All discovered files failed: [{"url": "http://www.etsi.org/deliver/etsi_ts/103200_103299/103264/02.01.01_60/ts_103264v020101p.pdf", "error": "HTTP Error 403: Forbidden"}]
- `eli-discover-1` — failed：DownloadError: No matching direct files found; portal retained for manual selection
- `akoma-doc-1` — failed：DownloadError: Empty response
- `agrovoc-doc-1` — failed：DownloadError: HTTP Error 403: Forbidden
- `foodon-repository` — failed：DownloadError: HTTP Error 403: rate limit exceeded
- `siri-doc-1` — failed：DownloadError: HTTP Error 403: Forbidden
- `transmodel-netex-doc-1` — failed：DownloadError: HTTP Error 403: Forbidden
- `otm-doc-1` — failed：DownloadError: Redirect/discovery host not on the curated allow-list: otm-api-spec.redocly.app
- `gtfs-rdf-repository` — failed：DownloadError: HTTP Error 403: rate limit exceeded
- `otm-discover-1` — failed：DownloadError: Redirect/discovery host not on the curated allow-list: otm-api-spec.redocly.app
- `datex2-doc-1` — failed：DownloadError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1006)>
