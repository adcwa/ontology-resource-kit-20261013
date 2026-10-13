#!/usr/bin/env python3
"""Rebuild the curated catalog. Inputs are preserved separately in original.tsv."""
import csv,json,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((ROOT/'catalog/original.tsv').open(encoding='utf-8'),delimiter='\t'))
categories=[{'id':f'{i:02d}','name':n} for i,n in enumerate(dict.fromkeys(r['category'] for r in rows),1)]
catids={r['name']:r['id'] for r in categories}
# title | kind | download policy | scope note. "open" is a download candidate, NOT a blanket redistribution licence.
profile_text='''bfo|BFO 2020 / ISO 21838-2 配套实现|顶层本体|open|保留 BFO 2020 仓库定位；不要把仓库版本名称与早期 BFO 2.0 简单视为同一发布包。
dolce|DOLCE|顶层本体|open|官方 DOLCE 的一阶逻辑形式与 DOLCE Lite、DUL 的 OWL 重构版本须分别管理。
ontouml|UFO / OntoUML 文档|建模语言与方法|open|原链接是 OntoUML 语言文档，不是一个完整的 UFO OWL 本体文件。
sumo|SUMO|顶层本体|open|下载仓库原始表示；不要假定其原生逻辑内容能作为普通 OWL DL 本体直接导入。
gfo|GFO|顶层本体|open|完整本体采用模块组织；离线使用还需检查 imports 与版本 IRI。
owl2|OWL 2|建模语言规范|open|语言规范，不是行业本体；附带词汇文件也不等于规范的全部语义。
rdf11|RDF 1.1|数据模型规范|open|保留原指定 RDF 1.1；不把 RDF 图数据与 OWL 逻辑本体混称。
skos|SKOS|词汇与知识组织|open|规范文档与机器可读词汇分别下载。
prov-o|PROV-O|基础本体|open|溯源词汇与规范；保留上游命名空间。
dcat3|DCAT 3|基础本体|open|优先下载明确的 dcat3 序列化，避免与其他版本混淆。
ssn-sosa|SSN / SOSA|基础本体|open|在基础设施与能源类别中交叉引用；原文件仅存一份。
schemaorg|Schema.org|通用词汇|open|沿用原目录位置，但 Schema.org 不等同于 W3C Recommendation；数据词汇与文档分开。
sparql11|SPARQL 1.1|查询语言规范|open|查询语言规范，不是 OWL 本体文件。
iof|IOF 工业本体|领域本体|open|下载仓库快照；快照不自动等同于已正式发布的 IOF 版本。
step|STEP / ISO 10303-242|数据交换标准|manual|原 ISO 链接只覆盖 AP242:2022，并非整个 ISO 10303 系列；不自动下载付费标准正文。
ontostep|OntoSTEP|映射与实现|open|保留 NIST 实现仓库，与 ISO 标准正文分开；下载成功不证明覆盖整个 STEP 系列。
rami40|RAMI 4.0|参考架构|open|参考架构文档，不是可直接导入的 OWL 行业本体。
aas|AAS / IDTA|信息模型与接口|open|原仓库已重定向到元模型仓库；该仓库不代表所有 AAS API 与子模型模板。
saref4inma|SAREF4INMA|领域本体|open|已核实页面指向 v2.1.1；下载该版本正文与序列化，imports 仍需另行检查。
cim|IEC CIM / 第三方 OWL 实现|领域信息模型|review|IEC TC57 页面和第三方 CIM-OWL 仓库分开保留；本次未能核实原仓库，不视为 IEC 官方 OWL 发布。
iec61850|IEC 61850|通信与信息模型标准|manual|原链接只是 IEC 首页，无法唯一定位系列规范、分册、版本或可下载包。
saref4ener|SAREF4ENER|领域本体|open|下载其公开序列化；实际版本以下载报告为准。
iso15926|ISO 15926 系列|生命周期数据标准|manual|原链接错配为 ISO 15614-11:2025；新增正确的 Part 2 数据模型标准入口。
iso15926-impl|ISO 15926 RDF/OWL 实现候选|映射与实现|review|本次未能核实原 GitHub 仓库可用性；保留待核验，不能认定为完整标准实现。
osdu|OSDU|数据平台与生态|portal|生态与平台入口，不存在一个代表整个 OSDU 的单一本体文件；只收录入口与可选单页快照。
ppdm|PPDM|领域数据模型|manual|需到发布方确认版本、会员/许可与下载范围；工具不使用账户或绕过登录。
fibo|FIBO|领域本体|open|仓库与浏览器合并为一项；仓库默认分支快照不自动等于 production 发布版。
commons|OMG Commons 1.2 / 1.3|基础本体|open|保留 1.2 历史版本；1.3 已于 2026 年 6 月正式采纳，不再标为 beta。
actus|ACTUS|合约与计算标准|portal|标准与生态入口，不等同于单个 OWL 本体；可选保存介绍页。
snomedct|SNOMED CT|医学术语体系|manual|浏览器和下载入口合并；需按地区及用途核对许可并从官方渠道取得发行包。
fhir|HL7 FHIR|医疗交换规范|open|FHIR 规范、结构定义与数据实例不是同一类资源；不把整个站点冒充一份本体。
fhir-rdf|HL7 FHIR RDF|RDF 表示规范|open|保留 RDF 表示规范；标准描述页面并不等于本地已经存在完整 RDF 发行包。
obo|OBO Foundry|本体注册与生态|portal|注册目录不是一个本体；不自动递归下载所有成员本体。
go|Gene Ontology|领域本体|open|配置公开 go-basic.obo 下载候选；它不是全部 GO 注释数据或所有产品。
chebi|ChEBI|领域本体与数据库|open|大型资源按需下载；词汇、本体与化合物数据库应分别管理。
uberon|UBERON|领域本体|open|仓库可能较大；源码快照不等于包含所有依赖的发行产品。
loinc|LOINC|医学术语体系|manual|需从官方下载页选择版本并接受相应使用条款；不自动处理注册登录。
rxnorm|RxNorm|医学术语体系|manual|完整发行包与其他下载产品许可范围不同；从官方入口人工选择，不默认整包可自由再分发。
icd11|ICD-11 MMS / 2025-01|分类体系|manual|保留用户指定的 2025-01 历史版本；浏览器入口不等于可下载的完整发行包。
mesh|MeSH|医学词表|portal|先在官方页面选择年度和发行格式；不把官网首页当作完整词表。
ifc|IFC|BIM 数据交换标准|open|规范与 schema 按发行版管理；IFC 与 ifcOWL 不合并为同一个文件。
ifcowl|ifcOWL / IFC4 ADD2 TC1|映射与实现|open|保留原指定 IFC4 ADD2 TC1 路径；不宣称与其他 IFC 版本完全等价。
bot|BOT|领域本体|open|官网与仓库合并；保留源文件、语言标签与许可证。
citygml|CityGML 3.0|城市信息模型标准|open|概念模型与编码实现分开；仅抓取入口页直接链接的选定资料，不镜像整个 OGC。
iso23387|ISO 23387 / BIM 数据模板|信息模型标准|manual|原入口未成功访问；新增官方 ISO 23387:2025 入口，标准正文按官方许可获取。
gs1voc|GS1 Web Vocabulary|领域词汇|open|词汇与企业商品主数据不是一回事；不抓取商品实例数据。
cbv|GS1 CBV|业务事件词汇标准|open|当前原链接返回 CBV 2.0 PDF；原清单的 ISO/IEC 19988:2024 标注本次未独立核验。
epcis|EPCIS 2.0|事件数据交换标准|open|下载规范及页面直接链接的 schema；不将其称作一份完整 OWL 本体。
goodrelations|GoodRelations|领域本体|open|保留原官网并尝试公开 OWL 序列化；历史 HTTP 入口可能跳转或失效。
uncefact|UN/CEFACT|标准生态与数据模型|portal|组织入口覆盖多项标准，需进一步指定业务范围和版本才能获得完整资料集。
saref|SAREF 核心与扩展索引|本体家族|open|下载核心及本清单列出的扩展；“全系列”索引不代表已下载网站上所有扩展。
saref4city|SAREF4CITY|领域本体|open|实际版本与序列化以下载日志为准。
saref4bldg|SAREF4BLDG|领域本体|open|实际版本与序列化以下载日志为准。
saref4watr|SAREF4WATR|领域本体|open|实际版本与序列化以下载日志为准。
onem2m|oneM2M 基础本体入口|标准与本体入口|portal|原页面是规范索引；需选择适用的 Base Ontology 分册和版本，而非整个标准目录。
smof|SMOF（待核验）|待核验资源|review|本次未能核实 wddabc/SMOF 仓库的可访问性和所指资源，不猜测替代项目。
iso30173|ISO/IEC 30173:2023|概念与术语标准|manual|数字孪生概念与术语标准，不是可直接导入的 OWL 数据包。
dtdl|DTDL|数字孪生建模语言|open|建模语言与模型定义格式；不要当作 OWL 本体直接交给 OWL 推理机。
wot-td|W3C WoT Thing Description|物描述与接口规范|open|下载指定规范及直接链接的机器可读附属文件；区分规范版本与设备实例。
ido|IDO / ISO 23726-3|工业本体标准|manual|原 URL 指向 ISO 5409:2024。正确入口为 ISO/FDIS 23726-3，当前仍处于审批阶段。
lkif|LKIF Core|领域本体|open|下载完整模块仓库；离线使用时检查所有 imports。
legalruleml|OASIS LegalRuleML 1.0|规则交换规范|open|法律规则交换格式，不等于一个 OWL 本体；保留规范与 schema。
akoma|Akoma Ntoso|文档标记规范|portal|法律文档结构化格式；门户不是完整机器可读发行包。
eli|ELI|标识与元数据框架|open|官方说明页与其直接链接的本体/规范分开；不抓取全部欧盟法律正文。
odrl|ODRL|策略模型与词汇|open|保留模型规范与词汇；不把模型表达直接等同于法律有效性判断。
agrovoc|AGROVOC|农业词表|portal|浏览器与 SPARQL 接口合并；SPARQL endpoint 是服务地址，不是离线全量文件。
saref4agri|SAREF4AGRI|领域本体|open|实际版本与序列化以下载日志为准。
foodon|FoodOn|领域本体|open|大型本体仓库，按需选择；保留依赖和许可信息。
agro|AgrO / AgroOntology|领域本体|open|配置 OBO 官方持久地址作为下载候选；记录实际重定向与版本，不把页面下载当成本体下载。
datex2|DATEX II|交通数据交换模型|portal|下载入口可能需要选择模型配置和发行版；不尝试登录或替用户接受条款。
siri|SIRI|交通数据交换规范|portal|原入口未指定分册、版本或 schema 包；保留给人工选择。
transmodel-netex|Transmodel / NeTEx|交通模型与交换规范|portal|两者属于相关但不同层次的资源，保留组合原条目并说明范围，不能合并语义。
otm|OpenTripModel 5|物流信息模型|open|保留 OTM 5 文档及公开的直接附属文件；不是 OWL 本体默认入口。
gtfs|GTFS Schedule|交通数据交换格式|open|规范与真实运营机构的 feed 不同；本包不包含各地时刻表数据。
gtfs-rdf|Linked GTFS|RDF 词汇实现|open|保留原项目仓库；不假定它与最新 GTFS 所有字段完全同步。'''
profiles={}
for ln in profile_text.splitlines():
 k,title,kind,policy,note=ln.split('|',4); profiles[k]=dict(title=title,kind=kind,policy=policy,scope_note=note)
assert set(profiles)=={r['resource_id'] for r in rows}
# id | what it is (quick recognition) | typical use. Descriptive text only; no claims about download status.
summary_text='''bfo|面向科学研究的上层本体，把世界分为持续存在的实体（continuant）与发生的过程（occurrent），是 ISO 21838-2 标准。|作为生物医学及工业本体（OBO 成员、IOF）的共同顶层，统一“物体/属性/过程”的建模方式。
dolce|意大利 ISTC-CNR 的认知导向顶层本体，区分持续体、事件、质与抽象，强调自然语言与常识中的范畴。|为领域本体提供哲学上严谨的上层分类；常用 DOLCE-Lite / DUL 轻量版本。
ontouml|OntoUML 是基于 UFO 的概念建模语言，用构造型（kind、role、phase 等）标注 UML 类图。|在落地为 OWL 前先做概念模型的本体正确性分析与评审。
sumo|IEEE 倡导的大型形式化上层本体，含中层与领域扩展，以 SUO-KIF 逻辑语言编写，并映射到 WordNet。|需要一阶逻辑公理、自然语言词义映射或大范围通用知识的场景。
gfo|莱比锡大学的通用形式本体，覆盖范畴、过程、角色、时空等，同时服务生物医学与社会科学。|作为兼顾物质与过程的上层本体参考，或对比 BFO / DOLCE 的选型。
owl2|W3C 的本体 Web 语言，在 RDF 之上定义类、属性、公理及 DL 语义，分 EL/QL/RL/DL 等子语言。|编写与推理本体的基础语言；决定本体能表达什么、推理机能做什么。
rdf11|W3C 数据模型：以“主语-谓语-宾语”三元组构成有向图，并带有 Turtle、RDF/XML 等序列化。|所有语义 Web 数据与本体的底层格式，是理解其他资源的起点。
skos|W3C 的简单知识组织系统，用 Concept、broader/narrower、prefLabel 表示叙词表、分类法。|把现有词表、分类表发布为链接数据；不适合做严格逻辑推理。
prov-o|W3C 溯源本体，核心为 Entity（实体）、Activity（活动）、Agent（主体）及其关系。|记录数据“从哪来、谁做的、怎么生成”，用于审计、数据血缘与可信度。
dcat3|W3C 数据目录词汇第 3 版，描述 Catalog、Dataset、Distribution、DataService，并支持数据系列。|发布数据门户、数据资产目录与开放数据元数据。
ssn-sosa|W3C 传感器、观测与执行器本体；SOSA 为轻量核心，SSN 为带公理的扩展。|描述传感器、观测、采样与执行器，是物联网与环境监测本体的共同底座。
schemaorg|由搜索引擎联合维护的网页结构化数据词汇，覆盖商品、组织、事件、文章等数千类型。|在网页中嵌入 JSON-LD / 微数据以利于搜索展示；也常作通用实体词汇。
sparql11|W3C 的 RDF 查询语言与协议规范，含 SELECT/CONSTRUCT、更新、联邦查询等。|查询知识图谱与本体数据；是语言规范，无本体文件。
iof|工业本体基金会的开放本体体系，以 BFO 为顶层，覆盖产品、过程、资源、供应链与维护。|构建制造业跨系统语义互操作，是工业 4.0 语义层的核心候选。
step|ISO 10303（STEP）系列的 AP242 部分，用于交换 3D 产品制造信息（PMI）与产品结构。|CAD / PLM 之间交换几何、公差、装配与材料数据；是付费标准，非本体。
ontostep|NIST 将 STEP AP242 的 EXPRESS 模型转为 OWL 的实现，便于对 CAD 数据做语义推理。|把 STEP 产品数据接入本体与知识图谱。
rami40|德国工业 4.0 参考架构模型：层级、生命周期价值流与架构层三维框架，已列入 IEC PAS 63088。|用来定位工业 4.0 组件，是规划参考框架而非可导入本体。
aas|工业 4.0 资产管理壳：以元模型描述资产的子模型、属性与语义引用，由 IDTA 维护。|制造设备数字孪生的标准化信息模型；与 ECLASS 等语义字典配合使用。
saref4inma|ETSI SAREF 的工业制造扩展，建模工件、生产设备、物料与生产过程。|智能制造设备与产品数据的语义对接。
cim|IEC 61970/61968 公共信息模型，描述电力系统的设备、拓扑、量测与资产，常以 UML/RDFS 表达。|电网调度、资产管理与能源系统之间的数据交换。
iec61850|电力自动化通信标准，定义变电站设备的逻辑节点、数据对象与服务模型。|变电站与分布式能源的设备建模及通信。
saref4ener|ETSI SAREF 的能源扩展，建模需求响应、设备能耗与能量曲线，对接 EEBus 等。|智能家居、能源管理与需求响应设备的语义互通。
iso15926|流程工业全生命周期数据集成标准，Part 2 提供通用数据模型，并配参考数据库。|石化、油气工厂设计、建造到运维的数据交换与集成。
iso15926-impl|ISO 15926 生命周期模型的 RDF/OWL 实现候选，来源与完整性待核验。|参考 ISO 15926 的 OWL 化思路；使用前需先确认其来源。
osdu|开放式地下数据宇宙：能源行业的开源数据平台，定义统一数据架构与数据类型。|油气勘探开发数据整合；是平台生态，无单一本体文件。
ppdm|石油行业数据管理协会的关系数据模型，覆盖井、地震、油田、合同等。|油气上游数据管理与数据库设计。
fibo|EDM Council 的金融业商业本体，覆盖证券、衍生品、贷款、机构、合约等，多模块组织。|金融数据治理、监管报告及风险数据的统一语义。
commons|OMG 的公共本体库，提供日期时间、数量、合约、组织等通用概念，是 FIBO 的基础。|复用跨领域基础概念，避免各本体重复定义。
actus|金融合约算法标准，用统一的现金流模式与参数描述各类合约的行为。|对贷款、债券、衍生品等合约做现金流计算与风险模拟。
snomedct|全球最大的临床术语体系，含数十万概念及属性关系，以描述逻辑形式化。|电子病历中诊断、操作与发现的标准编码；需按地区许可使用。
fhir|HL7 的医疗互操作标准，以 REST 与资源（Patient、Observation 等）交换临床数据。|医院系统、移动应用间的医疗数据 API；本身为交换标准，不是本体。
fhir-rdf|FHIR 的 RDF 表示，使 FHIR 资源能表达为三元组并用 SPARQL 查询、校验。|把 FHIR 数据接入知识图谱和语义推理。
obo|OBO 本体注册联盟：维护一批互相对齐、遵循共同原则的开放生物医学本体。|检索与选用生物医学本体；本身是注册中心。
go|基因本体：描述基因产物的分子功能、生物过程与细胞组分的受控词表。|基因功能注释与富集分析。
chebi|生物相关小分子化合物本体，含结构、角色与分类关系。|代谢、药物及化学实体的标准化命名与归类。
uberon|跨物种解剖学本体，覆盖器官、组织及其结构与发育关系。|跨物种表型、基因表达的解剖位置对齐。
loinc|实验室检验与临床观察的通用编码，按成分、属性、时间、系统等六轴命名。|检验项目与测量结果的标准编码与互通。
rxnorm|美国 NLM 的药品标准名称与编码，整合多个药品词表的映射。|药品命名归一、处方与药物相互作用对接。
icd11|WHO 疾病与相关健康问题的国际分类第 11 版，MMS 用于统计与编码。|疾病统计、医保与死因编码；2025-01 为指定历史版本。
mesh|NLM 的医学主题词表，层级组织，用于 PubMed 文献标引与检索。|医学文献标引、主题检索与语义扩展。
ifc|buildingSMART 的建筑信息模型（BIM）开放数据交换标准，ISO 16739。|建筑、结构、设备专业之间的 BIM 模型交换。
ifcowl|IFC 的 OWL 版本，以 EXPRESS 转换，使 BIM 数据可用 RDF 与 SPARQL 处理。|将 BIM 模型接入语义 Web，做查询与规则检查；转换结果体量大。
bot|W3C LBD 社区的建筑拓扑本体：Site/Building/Storey/Space/Element 等轻量核心。|在语义 Web 中描述建筑空间拓扑，与 IFC、SAREF 等配合。
citygml|OGC 的三维城市模型标准，含建筑、道路、地形、植被等对象及多级细节。|数字城市、规划与仿真；3.0 区分概念模型与 GML/JSON 编码。
iso23387|ISO 的 BIM 数据模板标准：以结构化属性模板描述建筑产品及其特性。|建筑产品数据的标准化交付，与 IFC 属性集对应。
gs1voc|GS1 的 Web 词汇，扩展 Schema.org，描述商品、品牌、成分、包装等属性。|电商与零售商品数据的语义标记。
cbv|GS1 的核心业务词汇，规定 EPCIS 事件中业务步骤、状态、位置的取值。|供应链可追溯事件的值域统一。
epcis|GS1 的电子产品代码信息服务标准，记录“什么物品、何时何地、因何事”事件。|供应链追踪溯源与可视化；2.0 增加 JSON-LD 与 REST。
goodrelations|早期的电商本体，描述报价、商品、价格、业务实体与条款，后被 Schema.org 采纳。|理解电商语义标记的历史；新项目多直接用 Schema.org。
uncefact|联合国贸易便利化与电子商务中心的标准集，含核心组件、跨行业发票与贸易模型。|国际贸易单证与跨境数据交换。
saref|ETSI 智能应用参考本体：对设备、功能、状态、服务与测量建模的核心及多个扩展。|智能家居、楼宇、能源等物联网设备的语义互操作。
saref4city|SAREF 的智慧城市扩展，覆盖城市设施、兴趣点、交通与环境。|智慧城市传感与服务的数据建模。
saref4bldg|SAREF 的建筑扩展，描述建筑空间、设备及其与 IFC 概念的对照。|智能楼宇与设备管理的语义集成。
saref4watr|SAREF 的水务扩展，描述水表、管网、水质与用水行为。|智能水务监测与分析。
onem2m|oneM2M 物联网标准的基础本体，将资源与设备映射到 SAREF，便于语义互操作。|物联网平台间的语义发现与跨厂商互操作。
smof|待核验资源：仅保留原仓库链接，具体含义尚未确认。|须先核实仓库身份后再使用。
iso30173|ISO/IEC 数字孪生概念与术语标准，定义孪生、实体、同步等基本概念。|统一数字孪生项目的术语和概念共识；是术语标准，非本体。
dtdl|微软数字孪生定义语言，以 JSON-LD 定义接口、遥测、属性、命令与关系。|在 Azure Digital Twins 等平台建模设备与环境；不是 OWL。
wot-td|W3C 物联网 Web 描述，以 JSON-LD 描述设备的属性、动作、事件与交互协议。|让不同厂商设备以 Web 方式被发现与调用。
ido|ISO/FDIS 23726-3 工业数据本体：以 BFO 为基础的工业领域上层，补充工业概念。|工业领域顶层语义标准化；标准仍在审批阶段。
lkif|欧洲 ESTRELLA 项目的法律知识交换格式核心本体，含法律行为、规范、角色与主体。|法律推理、合规与法律知识库的参考模块。
legalruleml|OASIS 的法律规则 XML 交换标准，可表示义务、许可、禁止及规则间的冲突与废止。|法律条文的规则化表示与合规自动化。
akoma|法律与议会文档的 XML 标记标准，含结构、元数据与版本引用。|立法文本的结构化、检索与跨国共享。
eli|欧洲立法标识符及元数据本体：为法律文本提供 URI、元数据与版本关系。|在欧盟及成员国之间链接和检索法规。
odrl|W3C 的权利表达语言：策略由许可、禁止与义务构成，规定对资产的约束。|数字内容使用授权、数据空间中的使用策略。
agrovoc|联合国粮农组织的多语言农业叙词表，含数十万概念，以 SKOS 发布。|农业文献标引与多语言检索、数据对齐。
saref4agri|SAREF 的农业扩展，建模农场、作物、传感器与农事活动。|智慧农业设备与农事数据互联。
foodon|食品本体：描述食品来源、加工、营养成分与分类，基于 OBO 原则。|食品数据标注、溯源与营养研究。
agro|农业本体：描述农业流程、作物、农艺措施及相关表型。|农业研究数据的标准化标注。
datex2|欧洲交通数据交换标准，描述路况、事故、施工、停车及交通管理信息。|交通管理中心之间交换实时交通信息。
siri|公共交通服务接口：实时到站、车辆位置、预计到达及偏差。|公共交通实时信息系统的互联。
transmodel-netex|Transmodel 是欧洲公共交通概念数据模型；NeTEx 是其 XML 交换实现。|公交线网、时刻与票价数据的跨系统交换。
otm|OpenTripModel：描述运输服务、预定、报价与履约的物流信息模型。|货运物流与门到门出行服务之间的数据交换。
gtfs|通用公交数据规范：用 CSV 文件描述线路、站点、班次与时刻。|Google 地图等发布公交时刻；开放数据最常用格式。
gtfs-rdf|GTFS 的 RDF 词汇，让公交时刻数据成为链接数据，可在 SPARQL 中查询。|把公交数据融合入知识图谱或与其他数据集链接。'''
for ln in summary_text.splitlines():
 k,s,u=ln.split('|',2); profiles[k]['summary']=s; profiles[k]['use_for']=u
assert all('summary' in v for v in profiles.values())
from supplement_data import SUPPLEMENT_TEXT,SOURCE_TEXT
supp_cats={}
for ln in SUPPLEMENT_TEXT.splitlines():
 k,title,kind,cats_,policy_,s,u=ln.split('|',6)
 assert k not in profiles,k
 profiles[k]=dict(title=title,kind=kind,policy=policy_,summary=s,use_for=u,scope_note='补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。');supp_cats[k]=cats_.split(',')
sources={}
for ln in SOURCE_TEXT.splitlines():
 k,pub,auth,acc,links,how=ln.split('|',5)
 assert k in profiles and k not in sources,k
 sources[k]=dict(publisher=pub,authority=auth,access=acc,links=[dict(label=a.split('::')[0],url=a.split('::',1)[1]) for a in links.split(' ;; ')],how=how)
assert set(sources)==set(profiles),set(profiles)^set(sources)
repos={'bfo':'BFO-ontology/BFO-2020','ontouml':'OntoUML/OntoUML','sumo':'ontologyportal/sumo','gfo':'Onto-Med/GFO','iof':'iofoundry/ontology','ontostep':'usnistgov/OntoSTEP','aas':'admin-shell-io/aas-specs-metamodel','cim':'griddigit-ci/CIM-OWL','iso15926-impl':'Posccaesar/Life-Cycle-Model','fibo':'edmcouncil/fibo','uberon':'obophenotype/uberon','bot':'w3c-lbd-cg/bot','smof':'wddabc/SMOF','dtdl':'Azure/opendigitaltwins-dtdl','lkif':'RinkeHoekstra/lkif-core','foodon':'FoodOntology/foodon','gtfs-rdf':'OpenTransport/linked-gtfs'}
canonical={'bfo':'https://github.com/BFO-ontology/BFO-2020','dolce':'https://www.loa.istc.cnr.it/dolce/overview.html','aas':'https://github.com/admin-shell-io/aas-specs-metamodel','cim':'https://www.iec.ch/TC57','iso15926':'https://www.iso.org/standard/29557.html','commons':'https://www.omg.org/spec/Commons/1.3','iso23387':'https://www.iso.org/standard/85391.html','ido':'https://www.iso.org/standard/87560.html','saref4inma':'https://saref.etsi.org/saref4inma/v2.1.1/'}
verified={'bfo','dolce','ontouml','gfo','iof','aas','step','iso15926','commons','iso23387','ido','iso30173','saref4inma','cbv','gtfs-rdf','dcat3','skos','prov-o','lkif'}
issues={
 'bfo':('名称澄清','链接为 BFO 2020 artifacts；不能仅按 BFO 2.0 的旧标签归档。','https://github.com/BFO-ontology/BFO-2020'),
 'ontouml':('类型纠正','给定仓库明确为 OntoUML Language Documentation，并非 UFO OWL 本体发行包。','https://github.com/OntoUML/OntoUML'),
 'dolce':('形式化区分','官方 DOLCE 为 FOL；DOLCE Lite 与 DUL 为不同程度的 OWL 适配/重构。','https://www.loa.istc.cnr.it/dolce/overview.html'),
 'step':('范围与版本','原链接是已撤回的 ISO 10303-242:2022；官方页列有 2025 替代版。不是整个 STEP 系列。','https://www.iso.org/standard/84667.html'),
 'aas':('仓库重定向','原 aas-specs 已重定向为 aas-specs-metamodel。','https://github.com/admin-shell-io/aas-specs-metamodel'),
 'iso15926':('错链','原 /81785.html 是 ISO 15614-11:2025 焊接程序试验。已新增 ISO 15926-2:2003 正确入口。','https://www.iso.org/standard/29557.html'),
 'iso23387':('入口与版本','原 /75486.html 本次返回 404；ISO 23387:2025 正确入口为 /85391.html。','https://www.iso.org/standard/85391.html'),
 'ido':('错链与状态','原 /84706.html 是 ISO 5409:2024 烟气汞检测。正确项目为 ISO/FDIS 23726-3，阶段 50.20（核验时）。','https://www.iso.org/standard/87560.html'),
 'commons':('状态更新','1.3 已列入 Formal Versions，采纳日期 June 2026；原 beta 标签过时。1.2 保留作为历史版本。','https://www.omg.org/spec/Commons/1.3'),
 'saref4inma':('版本补全','原无版本页面重定向至 v2.1.1，页面标注发布日期 2025-04-25。','https://saref.etsi.org/saref4inma/v2.1.1/'),
 'cim':('待核验','原 CIM-OWL 仓库本次未能获取；不能仅据一次失败断言仓库不存在。IEC TC57 不是该 OWL 包的下载页。','https://github.com/griddigit-ci/CIM-OWL'),
 'iso15926-impl':('待核验','原 Life-Cycle-Model 仓库本次未能获取；保留原 URL，不静默替换其他项目。','https://github.com/Posccaesar/Life-Cycle-Model'),
 'smof':('待核验','原 SMOF 仓库与项目身份本次未核实；默认不自动下载该候选。','https://github.com/wddabc/SMOF'),
 'iec61850':('链接过泛','原链接是 IEC 首页，不足以定位 IEC 61850 的适用分册与发行文件。','https://www.iec.ch/homepage'),
 'cbv':('正文类型确认','原地址返回 Release 2.0、June 2022 的 GS1 CBV PDF；ISO/IEC 19988:2024 编号本次未独立核验。','https://ref.gs1.org/standards/cbv/'),
}
# Asset endpoints are plans. Even a verified documentation page does not prove a file has been downloaded.
assets={
 'bfo':[('https://raw.githubusercontent.com/BFO-ontology/BFO-2020/master/21838-2/owl/bfo-core.owl','bfo-core.owl','rdfxml')],
 'owl2':[('https://www.w3.org/2002/07/owl','owl-vocabulary.rdf','rdfxml')],
 'rdf11':[('https://www.w3.org/1999/02/22-rdf-syntax-ns','rdf-syntax.rdf','rdfxml'),('https://www.w3.org/2000/01/rdf-schema','rdfs.rdf','rdfxml')],
 'skos':[('https://www.w3.org/2004/02/skos/core.rdf','skos-core.rdf','rdfxml')],
 'prov-o':[('https://www.w3.org/ns/prov-o.ttl','prov-o.ttl','turtle')],
 'dcat3':[('https://www.w3.org/ns/dcat3.ttl','dcat3.ttl','turtle'),('https://www.w3.org/ns/dcat3.rdf','dcat3.rdf','rdfxml')],
 'ssn-sosa':[('https://www.w3.org/ns/sosa/sosa.ttl','sosa.ttl','turtle'),('https://www.w3.org/ns/ssn/ssn.ttl','ssn.ttl','turtle')],
 'schemaorg':[('https://schema.org/version/latest/schemaorg-current-https.ttl','schemaorg-current-https.ttl','turtle')],
 'go':[('https://purl.obolibrary.org/obo/go/go-basic.obo','go-basic.obo','obo')],
 'agro':[('https://purl.obolibrary.org/obo/agro.owl','agro.owl','rdfxml')],
 'cbv':[('https://ref.gs1.org/standards/cbv/','cbv-standard.pdf','pdf')],
 'epcis':[('https://ref.gs1.org/standards/epcis/','epcis-standard.pdf','pdf')],
 'goodrelations':[('http://purl.org/goodrelations/v1','goodrelations.rdf','rdfxml')],
 'odrl':[('https://www.w3.org/ns/odrl/2/ODRL22.ttl','ODRL22.ttl','turtle')],
}
# Content negotiation at canonical ETSI IRIs avoids inventing a versioned filename.
for ident in ['saref','saref4inma','saref4ener','saref4city','saref4bldg','saref4watr','saref4agri']:
 url=canonical.get(ident, 'https://saref.etsi.org/'+('core' if ident=='saref' else ident)+'/')
 assets[ident]=[(url,ident+'.ttl','turtle')]
discovery={'dolce':{'pattern':r'(DOLCE|DLP|DUL|\.owl$|\.zip$)'},'commons':{},'ifc':{},'ifcowl':{},'citygml':{},'gs1voc':{},'legalruleml':{},'eli':{},'wot-td':{},'fhir-rdf':{},'fhir':{'pattern':r'(definitions|validation|schema|rdf)'},'rami40':{},'otm':{},'chebi':{'large':True}}
records=[];tasks=[]
for ident in profiles:
 entries=[dict(x,original_row=i+1) for i,x in enumerate(rows) if x['resource_id']==ident]
 cats=supp_cats[ident] if ident in supp_cats else list(dict.fromkeys(catids[x['category']] for x in entries))
 r=dict(id=ident,**profiles[ident],categories=cats,original_entries=entries,origin='supplement' if ident in supp_cats else 'original',official_sources=sources[ident],canonical_url=canonical.get(ident,entries[0]['url'] if entries else sources[ident]['links'][0]['url']),verification=('page_checked' if ident in verified else 'not_individually_verified'),verified_on=('2026-10-13' if ident in verified else None),issue=None,download_state='not_downloaded',local_files=[],licence_note='以各上游资源的 LICENSE、版权声明及适用条款为准；本目录不授予第三方内容的再分发权。')
 if ident in issues:
  typ,note,url=issues[ident];r['issue']={'type':typ,'note':note,'source_url':url}
 if ident in repos:
  r['repository']=repos[ident]
  tasks.append({'id':ident+'-repository','resource_id':ident,'kind':'github','repository':repos[ident],'large':ident in ['fibo','uberon','foodon'],'policy':r['policy'],'note':'下载时解析默认分支为 commit SHA 后固定归档；不是 latest stable 声明。'})
 for i,(url,name,fmt) in enumerate(assets.get(ident,[]),1):
  tasks.append({'id':ident+'-asset-'+str(i),'resource_id':ident,'kind':'file','url':url,'filename':name,'format':fmt,'large':ident in ['go','schemaorg'],'policy':r['policy'],'endpoint_status':'candidate_not_downloaded'})
 if ident in discovery:
  d=discovery[ident]
  pages=[r['canonical_url']]
  if ident=='commons':pages+=['https://www.omg.org/spec/Commons/1.2']
  for i,url in enumerate(pages,1):
   tasks.append({'id':ident+'-discover-'+str(i),'resource_id':ident,'kind':'discover','url':url,'pattern':d.get('pattern',''),'large':d.get('large',False),'policy':r['policy'],'endpoint_status':'discover_at_runtime'})
 if r['policy'] not in ['manual','review'] and ident not in supp_cats:
  # Single-page documentation snapshots are explicitly opt-in, not counted as ontology assets.
  urls=list(dict.fromkeys([r['canonical_url']]+[e['url'] for e in entries if 'github.com/' not in e['url']]))
  for i,url in enumerate(urls,1):
   if 'github.com/' in url or '/sparql' in url or ident in ['cbv','epcis']:continue
   tasks.append({'id':ident+'-doc-'+str(i),'resource_id':ident,'kind':'document','url':url,'filename':f'official-page-{i}.html','format':'document','large':False,'policy':r['policy'],'note':'单页 HTML/PDF 快照，不是全站离线镜像，也不等于本体文件。'})
 records.append(r)
manifest={'schema_version':1,'created_on':'2026-10-13','original_entry_count':len(rows),'resource_count':len(records),'original_resource_count':len(records)-len(supp_cats),'supplement_count':len(supp_cats),'category_count':len(categories),'categories':categories,'resources':records,'tasks':tasks,'delivery':{'original_files_included':0,'status':'catalog_and_downloader_only','note':'当前制作环境外网文件下载失败；没有将上游文件伪装为已下载。开放资源需在本地运行 download.py；手动或待核验项保留明确状态。'}}
(ROOT/'catalog/catalog.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(ROOT/'catalog/download-manifest.json').write_text(json.dumps({'schema_version':1,'tasks':tasks},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(ROOT/'reports/delivery-status.json').write_text(json.dumps(manifest['delivery'],ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(ROOT/'reports/download-state.json').write_text('{"schema_version":1,"files":{},"task_results":{},"updated_at":null}\n',encoding='utf-8') if not (ROOT/'reports/download-state.json').exists() else None
(ROOT/'reports/status.js').write_text('window.DOWNLOAD_STATE='+ (ROOT/'reports/download-state.json').read_text(encoding='utf-8').strip()+';\n',encoding='utf-8')
print(len(rows),'original entries;',len(records),'resources (',len(supp_cats),'supplements );',len(tasks),'download tasks')
