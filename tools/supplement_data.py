"""Supplementary resources and official-source records for build_catalog.py.

Sources are chosen from the publisher's own sites and were NOT individually visited in the build environment.
"""
# id | title | kind | categories | policy | summary | use_for
SUPPLEMENT_TEXT='''cco|Common Core Ontologies (CCO)|中层本体|01|portal|以 BFO 为基础的一组中层本体，覆盖事件、人、组织、时间、地理与信息实体，由美国国防与情报界推动。|在 BFO 与具体领域本体之间提供共用的中层概念，常与 IOF 配合。
shacl|SHACL|数据校验规范|02|portal|W3C 的 RDF 图形状约束语言，用 Shape 描述节点与属性必须满足的条件。|校验知识图谱数据质量；与 OWL 互补（OWL 推理，SHACL 校验）。
owl-time|OWL-Time|基础本体|02|portal|W3C 时间本体，描述时刻、区间、时长、时区及它们之间的 Allen 关系。|给任何领域的数据加上标准化的时间表达。
org|W3C Organization Ontology (ORG)|基础本体|02|portal|描述组织、组织单元、成员、岗位与层级关系的词汇。|组织架构、供应商或机构关系的建模。
foaf|FOAF|基础词汇|02|portal|描述人及其关系、账号与文档的经典 RDF 词汇。|表示人员与社交关系；很多本体用它引用“人”。
dcterms|Dublin Core Terms (DCMI)|元数据词汇|02|portal|通用资源元数据词汇：标题、创建者、日期、主题、许可等。|给任何资源打元数据；DCAT 与许多本体都复用它。
jsonld11|JSON-LD 1.1|数据格式规范|02|portal|W3C 的 JSON 链接数据格式，通过 @context 把普通 JSON 映射到 RDF 词汇。|让 API 与网页数据同时是 JSON 和语义数据；WoT、DTDL、Schema.org 均使用。
qudt|QUDT|基础本体|02|portal|量、单位、量纲与数据类型本体，含 SI 及大量单位的换算关系。|给传感器、工程和科学数据标注统一的单位与量纲。
opcua|OPC UA 信息模型|工业通信标准|03|portal|OPC 基金会的工业通信标准，其信息模型把设备、变量、方法以节点图形式暴露，并有各行业伴随规范。|工厂设备与 MES/SCADA 的统一接入；与 AAS 可互相映射。
eclass|ECLASS|产品分类与属性字典|03|manual|标准化产品分类与属性语义字典，含数万产品类和属性定义，被 AAS 广泛用作语义标识。|给设备和零部件的属性提供全球唯一的语义 ID；下载需按许可获取。
emmo|EMMO|领域本体|03|portal|欧洲材料与建模本体，用统一框架描述材料、过程、性质与建模表示。|材料科学与制造研发的数据语义化。
energistics|Energistics 标准（WITSML / RESQML / PRODML）|行业数据标准|05|portal|油气上游数据交换标准族：钻井（WITSML）、地质建模（RESQML）、生产（PRODML），现由 OSDU 管理。|钻井、油藏与生产数据在厂商和系统之间交换。
iso20022|ISO 20022|金融报文标准|06|portal|金融服务通用报文标准，含统一的业务模型和报文库，被支付系统广泛采用。|银行支付、证券清算报文的统一语义。
xbrl|XBRL|财务报告标准|06|portal|用于财务与监管报告的 XML 标准，以分类法（taxonomy）定义报表概念。|上市公司与监管机构的结构化财报申报。
hpo|Human Phenotype Ontology (HPO)|领域本体|07|portal|人类疾病表型术语的本体，覆盖症状、体征及其层级关系。|罕见病诊断与基因-表型分析。
doid|Disease Ontology (DO)|领域本体|07|portal|人类疾病的标准分类本体，与 MeSH、ICD、SNOMED 等有交叉引用。|疾病数据整合与跨库对齐。
mondo|Mondo Disease Ontology|领域本体|07|portal|整合多个疾病分类的统一疾病本体，对 OMIM、Orphanet、DO 等做等价映射。|罕见病与遗传病的跨数据库疾病对齐。
ncit|NCI Thesaurus (NCIt)|医学术语体系|07|portal|美国国家癌症研究所的大型生物医学叙词表，覆盖癌症、药物、基因与临床研究概念。|肿瘤学与临床研究的数据标注。
omop|OMOP 通用数据模型与标准词汇|数据模型|07|portal|OHDSI 的医疗观察数据通用模型，配套整合 SNOMED、LOINC、RxNorm 等的标准词汇。|把各医院的真实世界数据转成统一结构做队列研究。
brick|Brick Schema|领域本体|08|portal|描述楼宇设备、空间、点位及其关系的开放本体，面向楼宇自动化与分析。|楼宇系统（暖通、照明、电表）的元数据统一，支撑数据分析应用。
realestatecore|RealEstateCore|领域本体|08|portal|面向房地产与智能建筑的本体，覆盖建筑、空间、租户、设备与合同。|智能建筑、物业管理与数字孪生应用。
gs1-dl|GS1 Digital Link|标识标准|09|portal|把 GTIN、批号等 GS1 标识编码成 Web URI 的标准，使二维码可直接指向产品信息。|产品追溯、消费者扫码与产品护照。
geosparql|GeoSPARQL|基础本体|10|portal|OGC 标准，为 RDF 提供空间对象与几何表示及 SPARQL 空间函数。|在知识图谱里做空间查询，如城市、地块、设施位置。
smartdatamodels|Smart Data Models|数据模型集合|10|portal|FIWARE 等社区维护的跨领域数据模型库，涵盖智慧城市、能源、农业与制造，并带 JSON Schema 与 JSON-LD 上下文。|快速取得面向 NGSI-LD / API 的现成数据模型。
sensorthings|OGC SensorThings API|接口标准|10|portal|OGC 的物联网传感器数据 API，数据模型与 SOSA/SSN 对应。|传感器与观测数据的标准化 REST 服务。
iso23247|ISO 23247 制造数字孪生框架|数字孪生标准|11|manual|制造领域数字孪生的框架标准系列，定义参考架构与功能实体。|制造数字孪生的整体设计参考；付费标准，非本体。
dpv|Data Privacy Vocabulary (DPV)|基础本体|12|portal|W3C 数据隐私社区组的词汇，描述个人数据处理的目的、法律依据、主体权利与措施，并映射 GDPR。|隐私合规记录、同意管理与数据处理清单。
cropontology|Crop Ontology|领域本体|13|portal|作物性状、方法与尺度的本体集合，服务作物育种数据。|育种试验与表型数据标准化。
po|Plant Ontology (PO)|领域本体|13|portal|植物解剖结构与发育阶段的本体，OBO 成员。|植物基因表达与表型数据的结构对齐。
envo|Environment Ontology (ENVO)|领域本体|13|portal|描述环境系统、生物群落、环境材料的本体，OBO 成员。|生态与农业数据的环境背景标注。
railml|railML|铁路数据标准|14|portal|铁路领域 XML 数据交换标准，覆盖时刻表、基础设施与车辆。|铁路设计、运营系统间的数据交换。
gbfs|GBFS|共享出行数据规范|14|portal|共享单车、电动滑板车和租车的实时数据规范：站点、车辆可用性与定价。|共享出行信息在地图与出行服务中的开放展示。
transxchange|TransXChange|交通数据标准|14|portal|英国公交线路与时刻的 XML 交换格式。|公交运营商向政府和出行平台提供时刻数据。'''
# id | publisher | authority | access | label::url ;; label::url | how to obtain
SOURCE_TEXT='''bfo|BFO 社区 / ISO/IEC JTC1 SC32|官方仓库|公开免费 / 标准正文付费|BFO-2020 仓库::https://github.com/BFO-ontology/BFO-2020 ;; ISO/IEC 21838-2::https://www.iso.org/standard/74572.html|OWL 文件位于仓库 21838-2/owl；ISO 标准正文需向 ISO 购买。
dolce|意大利 ISTC-CNR 应用本体实验室（LOA）|发布方官网|公开免费|DOLCE 总览::http://www.loa.istc.cnr.it/dolce/overview.html ;; DUL 本体::http://www.ontologydesignpatterns.org/ont/dul/DUL.owl|官网提供 DOLCE 文档；DUL / DOLCE-Lite 是 OWL 重构版，需分别获取。
ontouml|NEMO 研究组（巴西 UFES）/ OntoUML 社区|官方仓库|公开免费|OntoUML 仓库::https://github.com/OntoUML/OntoUML ;; 文档站::https://ontouml.readthedocs.io|从仓库取得语言文档与示例；UFO 的 OWL 版本需另找发布方。
sumo|Articulate Software / Adam Pease|发布方官网|公开免费|SUMO 门户::https://www.ontologyportal.org ;; 源码仓库::https://github.com/ontologyportal/sumo|门户提供在线浏览，仓库提供 SUO-KIF 源文件。
gfo|莱比锡大学 Onto-Med 研究组|官方仓库|公开免费|GFO 仓库::https://github.com/Onto-Med/GFO ;; 项目网站::https://www.onto-med.de/ontologies/gfo|从仓库下载模块文件。
owl2|W3C OWL 工作组|标准组织|公开免费|OWL 2 概述::https://www.w3.org/TR/owl2-overview/ ;; OWL 主页::https://www.w3.org/OWL/|W3C Recommendation 免费公开。
rdf11|W3C RDF 工作组|标准组织|公开免费|RDF 1.1 概念::https://www.w3.org/TR/rdf11-concepts/ ;; RDF 1.1 入门::https://www.w3.org/TR/rdf11-primer/|W3C Recommendation 免费公开。
skos|W3C|标准组织|公开免费|SKOS 参考::https://www.w3.org/TR/skos-reference/ ;; 命名空间::https://www.w3.org/2004/02/skos/core|命名空间 URL 可通过内容协商取得 RDF。
prov-o|W3C Provenance 工作组|标准组织|公开免费|PROV-O 规范::https://www.w3.org/TR/prov-o/ ;; 命名空间::https://www.w3.org/ns/prov|命名空间可取得 Turtle / RDF 文件。
dcat3|W3C 数据交换工作组（DXWG）|标准组织|公开免费|DCAT 3 规范::https://www.w3.org/TR/vocab-dcat-3/ ;; 命名空间::https://www.w3.org/ns/dcat|规范页含序列化链接。
ssn-sosa|W3C / OGC 空间数据 Web 工作组|标准组织|公开免费|SSN 规范::https://www.w3.org/TR/vocab-ssn/ ;; 命名空间::https://www.w3.org/ns/sosa/|SOSA 与 SSN 是两个命名空间文件。
schemaorg|Schema.org 社区|发布方官网|公开免费|Schema.org 下载与文档::https://schema.org/docs/developers.html ;; 源码仓库::https://github.com/schemaorg/schemaorg|开发者页提供各版本 RDF / JSON-LD / Turtle 下载。
sparql11|W3C SPARQL 工作组|标准组织|公开免费|SPARQL 1.1 概述::https://www.w3.org/TR/sparql11-overview/|规范文档免费公开，无本体文件。
iof|工业本体基金会（IOF）|发布方官网|公开免费|IOF 官网::https://www.industrialontologies.org ;; 仓库::https://github.com/iofoundry/ontology|发布版本以仓库 Release 和官网为准。
step|ISO TC184/SC4|标准组织|付费|ISO 10303-242 页面::https://www.iso.org/standard/84667.html|向 ISO 或国家标准机构购买；公开页面只提供摘要。
ontostep|美国 NIST|官方仓库|公开免费|OntoSTEP 仓库::https://github.com/usnistgov/OntoSTEP|直接从仓库取得代码与 OWL 产物。
rami40|德国工业 4.0 平台（Plattform Industrie 4.0）|发布方官网|公开免费 / 部分标准付费|工业 4.0 平台::https://www.plattform-i40.de|在官网搜索 RAMI 4.0 出版物；DIN SPEC 91345 与 IEC PAS 63088 需向对应标准机构购买。
aas|工业数字孪生协会（IDTA）|官方仓库|公开免费|IDTA 官网::https://industrialdigitaltwin.org ;; 官方 GitHub::https://github.com/admin-shell-io|元模型、API 与子模型模板位于不同仓库，需分别获取。
saref4inma|ETSI（欧洲电信标准化协会）|标准组织|公开免费|SAREF4INMA 页面::https://saref.etsi.org/saref4inma/v2.1.1/ ;; SAREF 门户::https://saref.etsi.org|ETSI 门户提供各版本 Turtle 与文档；也有对应 ETSI TS 技术规范。
cim|IEC TC57 / CIM 用户组|标准组织|标准付费 / 部分模型文件公开|IEC TC57::https://www.iec.ch/TC57 ;; CIM 用户组::https://cimug.ucaiug.org|IEC 61970 / 61968 向 IEC 购买；CIMug 提供部分免费 RDFS 与示例。
iec61850|IEC TC57 WG10|标准组织|付费|IEC TC57::https://www.iec.ch/TC57 ;; IEC Webstore::https://webstore.iec.ch|需在 IEC Webstore 购买指定分册与版本。
saref4ener|ETSI|标准组织|公开免费|SAREF4ENER::https://saref.etsi.org/saref4ener/|从 ETSI SAREF 门户取得最新或指定版本。
iso15926|ISO TC184/SC4 / POSC Caesar 协会|标准组织|标准付费 / 参考数据公开|ISO 15926-2::https://www.iso.org/standard/29557.html ;; POSC Caesar::https://www.posccaesar.org|标准正文向 ISO 购买；PCA 提供参考数据与实施资料。
iso15926-impl|POSC Caesar 协会|待核验|待核验|PCA 官网::https://www.posccaesar.org ;; 原链接::https://github.com/Posccaesar/Life-Cycle-Model|需先确认仓库身份，再从 PCA 官方渠道获取。
osdu|OSDU 论坛（The Open Group）|官方社区|公开免费|OSDU 论坛::https://osduforum.org ;; 社区代码::https://community.opengroup.org/osdu|数据定义在社区 GitLab，按里程碑版本获取。
ppdm|PPDM 协会|发布方官网|会员 / 付费|PPDM::https://ppdm.org|通过 PPDM 协会按会员或购买方式获取数据模型。
fibo|EDM Council|发布方官网|公开免费|FIBO 规范站::https://spec.edmcouncil.org/fibo/ ;; 仓库::https://github.com/edmcouncil/fibo|规范站提供按发布版本的 RDF/OWL；仓库是开发快照。
commons|对象管理组织（OMG）|标准组织|公开免费|Commons 规范::https://www.omg.org/spec/Commons/|OMG 规范页提供各版本 PDF 与 OWL/RDF 文件。
actus|ACTUS 金融研究基金会|发布方官网|公开免费|ACTUS::https://www.actusfrf.org|官网提供技术规范与字典。
snomedct|SNOMED International|发布方官网|需许可（各国不同）|SNOMED International::https://www.snomed.org ;; 在线浏览器::https://browser.ihtsdotools.org|成员国可通过国家发布中心免费获取；非成员国需向 SNOMED International 申请许可。
fhir|HL7 国际|标准组织|公开免费|FHIR 规范::https://hl7.org/fhir/ ;; 源码::https://github.com/HL7/fhir|规范页提供各版本定义下载；注意区分发布版与 CI 构建。
fhir-rdf|HL7 国际|标准组织|公开免费|FHIR RDF::https://hl7.org/fhir/rdf.html|与 FHIR 规范一起发布。
obo|OBO Foundry|官方注册中心|公开免费|OBO Foundry::https://obofoundry.org ;; 注册库::https://github.com/OBOFoundry/OBOFoundry.github.io|在注册表里查各成员本体及 PURL。
go|基因本体联盟|发布方官网|公开免费（CC BY 4.0）|GO 官网::http://geneontology.org ;; 当前版本下载::https://current.geneontology.org/ontology/|官网提供 go-basic、go-plus 等版本，并有存档的历史发布。
chebi|欧洲生物信息学研究所（EMBL-EBI）|发布方官网|公开免费|ChEBI::https://www.ebi.ac.uk/chebi/ ;; FTP 下载::https://ftp.ebi.ac.uk/pub/databases/chebi/|FTP 提供 OWL、OBO 与数据库文件。
uberon|Uberon 社区（OBO）|官方仓库|公开免费|Uberon 站点::http://obophenotype.github.io/uberon/ ;; 仓库::https://github.com/obophenotype/uberon|通过 OBO PURL 或 GitHub Release 取得发行文件。
loinc|Regenstrief 研究所|发布方官网|免费但需注册并接受许可|LOINC::https://loinc.org ;; 下载页::https://loinc.org/downloads/|创建账号并接受许可条款后下载。
rxnorm|美国国家医学图书馆（NLM）|发布方官网|部分免费 / 需 UMLS 许可|RxNorm::https://www.nlm.nih.gov/research/umls/rxnorm/ ;; 文件说明::https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html|完整版需申请 UMLS 许可；部分子集无需。
icd11|世界卫生组织（WHO）|标准组织|公开（需遵守条款）|ICD-11::https://icd.who.int/en ;; ICD API::https://icd.who.int/icdapi|WHO 提供浏览器、API 与发布包；注意区分 MMS 与基础组件。
mesh|美国国家医学图书馆（NLM）|发布方官网|公开免费|MeSH::https://www.nlm.nih.gov/mesh/ ;; 下载::https://www.nlm.nih.gov/databases/download/mesh.html|按年度下载 XML、RDF 或 ASCII。
ifc|buildingSMART 国际|标准组织|公开免费（ISO 16739 正文付费）|IFC 标准页::https://technical.buildingsmart.org/standards/ifc/ ;; 概览::https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/|技术站提供各版本 schema；ISO 正文向 ISO 购买。
ifcowl|buildingSMART 国际 / 学术社区|标准组织|公开免费|IFC 格式::https://technical.buildingsmart.org/standards/ifc/ifc-formats/|以 buildingSMART 官方发布为准，不同 IFC 版本的 OWL 文件需分别获取。
bot|W3C 建筑关联数据社区组（LBD CG）|官方仓库|公开免费|BOT 命名空间::https://w3id.org/bot ;; 仓库::https://github.com/w3c-lbd-cg/bot|命名空间可协商取得 Turtle。
citygml|开放地理空间联盟（OGC）|标准组织|公开免费|CityGML::https://www.ogc.org/standard/citygml/ ;; 3.0 概念模型::https://docs.ogc.org/is/20-010/20-010.html|OGC 官方文档站免费下载。
iso23387|ISO TC59/SC13|标准组织|付费|ISO 23387:2025::https://www.iso.org/standard/85391.html|向 ISO 或国家标准机构购买。
gs1voc|GS1|发布方官网|公开免费|GS1 词汇::https://www.gs1.org/voc/ ;; 参考站::https://ref.gs1.org/voc/|词汇页可取得 RDF / JSON-LD。
cbv|GS1|标准组织|公开免费|CBV::https://ref.gs1.org/standards/cbv/|GS1 参考站提供标准 PDF。
epcis|GS1|标准组织|公开免费|EPCIS::https://ref.gs1.org/standards/epcis/|GS1 参考站提供标准 PDF 与 schema。
goodrelations|Martin Hepp（GoodRelations 作者）|发布方官网|公开免费|GoodRelations::http://purl.org/goodrelations/|通过 PURL 取得 OWL；该词汇已并入 Schema.org。
uncefact|UN/CEFACT（联合国欧洲经济委员会）|标准组织|公开免费|UN/CEFACT::https://unece.org/trade/uncefact|在官网选择具体标准，如核心组件库、跨行业发票。
saref|ETSI|标准组织|公开免费|SAREF 门户::https://saref.etsi.org ;; 核心::https://saref.etsi.org/core/|门户列出核心与所有扩展的版本。
saref4city|ETSI|标准组织|公开免费|SAREF4CITY::https://saref.etsi.org/saref4city/|从 ETSI SAREF 门户取得。
saref4bldg|ETSI|标准组织|公开免费|SAREF4BLDG::https://saref.etsi.org/saref4bldg/|从 ETSI SAREF 门户取得。
saref4watr|ETSI|标准组织|公开免费|SAREF4WATR::https://saref.etsi.org/saref4watr/|从 ETSI SAREF 门户取得。
onem2m|oneM2M 伙伴组织|标准组织|公开免费|oneM2M::https://www.onem2m.org ;; 已发布规范::https://www.onem2m.org/technical/published-drafts|在已发布规范中选择 Base Ontology 分册。
smof|待核验|待核验|待核验|原链接::https://github.com/wddabc/SMOF|先确认资源身份和维护方。
iso30173|ISO/IEC JTC1 SC41|标准组织|付费|ISO 搜索::https://www.iso.org/search.html?q=30173|向 ISO 或国家标准机构购买。
dtdl|微软|官方仓库|公开免费|DTDL 仓库::https://github.com/Azure/opendigitaltwins-dtdl ;; 文档::https://learn.microsoft.com/azure/digital-twins/concepts-models|仓库含规范与 JSON-LD 上下文。
wot-td|W3C WoT 工作组|标准组织|公开免费|WoT TD 1.1::https://www.w3.org/TR/wot-thing-description11/ ;; WoT TD 1.0::https://www.w3.org/TR/wot-thing-description/|规范页含 JSON schema 与本体链接。
ido|ISO TC184/SC4 / IOF|标准组织|付费（审批中）|ISO 23726-3::https://www.iso.org/standard/87560.html|标准审批完成前可关注 IOF 公开资料。
lkif|ESTRELLA 项目 / Rinke Hoekstra|官方仓库|公开免费|LKIF Core::https://github.com/RinkeHoekstra/lkif-core|直接从仓库取得模块文件。
legalruleml|OASIS LegalRuleML 技术委员会|标准组织|公开免费|LegalRuleML TC::https://www.oasis-open.org/committees/legalruleml/ ;; 核心规范 v1.0::https://docs.oasis-open.org/legalruleml/legalruleml-core-spec/v1.0/legalruleml-core-spec-v1.0.html|OASIS 文档站提供规范及 schema。
akoma|OASIS LegalDocML 技术委员会|标准组织|公开免费|Akoma Ntoso::https://www.akomantoso.org ;; OASIS 词汇规范::https://docs.oasis-open.org/legaldocml/akn-core/v1.0/akn-core-v1.0-part1-vocabulary.html|OASIS 文档站提供 XSD 和规范。
eli|欧盟出版局（Publications Office）|官方注册中心|公开免费|ELI::https://eur-lex.europa.eu/eli-register/about.html ;; EU Vocabularies::https://op.europa.eu/en/web/eu-vocabularies/eli|在 EU Vocabularies 取得 ELI 本体。
odrl|W3C 权利语言工作组|标准组织|公开免费|ODRL 信息模型::https://www.w3.org/TR/odrl-model/ ;; ODRL 词汇::https://www.w3.org/TR/odrl-vocab/|命名空间可协商取得 Turtle。
agrovoc|联合国粮农组织（FAO）|发布方官网|公开免费|AGROVOC::https://www.fao.org/agrovoc/ ;; 浏览器::https://agrovoc.fao.org/browse/|官网提供 RDF 下载与 SPARQL 服务。
saref4agri|ETSI|标准组织|公开免费|SAREF4AGRI::https://saref.etsi.org/saref4agri/|从 ETSI SAREF 门户取得。
foodon|FoodOn 联盟（OBO）|官方仓库|公开免费|FoodOn::https://foodon.org ;; 仓库::https://github.com/FoodOntology/foodon|通过 OBO PURL 或 GitHub Release 取得。
agro|农业语义社区（OBO）|官方注册中心|公开免费|OBO 页面::http://obofoundry.org/ontology/agro.html|OBO Foundry 页面指向官方 PURL 与仓库。
datex2|CEN TC278 / DATEX II 组织|标准组织|公开免费|DATEX II::https://www.datex2.eu|官网提供模型与 schema 下载，需选择版本。
siri|CEN TC278 / Transmodel 站点|标准组织|公开免费 / 部分文本付费|Transmodel 站点::https://www.transmodel-cen.eu|XSD 公开；CEN 技术规范文本需向标准机构购买。
transmodel-netex|CEN TC278|标准组织|公开免费 / 部分文本付费|Transmodel::https://www.transmodel-cen.eu ;; NeTEx::https://netex-cen.eu|NeTEx XSD 与示例公开；CEN 正式文本需购买。
otm|OpenTripModel 基金会|发布方官网|公开免费|OpenTripModel::https://opentripmodel.org ;; 组织仓库::https://github.com/OpenTripModel|从官网与仓库取得规范。
gtfs|MobilityData / Google|发布方官网|公开免费|GTFS 规范::https://gtfs.org/documentation/schedule/reference/ ;; 源仓库::https://github.com/google/transit|gtfs.org 为社区维护的规范站。
gtfs-rdf|OpenTransport 社区|官方仓库|公开免费|Linked GTFS::https://github.com/OpenTransport/linked-gtfs|取得 RDF 词汇与示例。
cco|CUBRC / Common Core Ontologies 社区|官方仓库|公开免费|CCO 仓库::https://github.com/CommonCoreOntology/CommonCoreOntologies|从 Release 取得各模块。
shacl|W3C 数据 Shapes 工作组|标准组织|公开免费|SHACL::https://www.w3.org/TR/shacl/|规范免费公开。
owl-time|W3C / OGC 空间数据 Web 工作组|标准组织|公开免费|OWL-Time::https://www.w3.org/TR/owl-time/ ;; 命名空间::https://www.w3.org/2006/time|命名空间可协商取得 Turtle。
org|W3C 政府关联数据工作组|标准组织|公开免费|ORG::https://www.w3.org/TR/vocab-org/ ;; 命名空间::https://www.w3.org/ns/org|命名空间可协商取得 Turtle。
foaf|FOAF 项目|发布方官网|公开免费|FOAF 规范::http://xmlns.com/foaf/spec/|命名空间可协商取得 RDF。
dcterms|都柏林核心元数据倡议（DCMI）|标准组织|公开免费|DCMI Terms::https://www.dublincore.org/specifications/dublin-core/dcmi-terms/|官网提供 RDF 下载。
jsonld11|W3C JSON-LD 工作组|标准组织|公开免费|JSON-LD 1.1::https://www.w3.org/TR/json-ld11/|规范免费公开。
qudt|QUDT.org / NASA 与 TopQuadrant 起源|发布方官网|公开免费|QUDT::https://qudt.org ;; 仓库::https://github.com/qudt/qudt-public-repo|从官网或仓库取得各版本 Turtle。
opcua|OPC 基金会|标准组织|公开免费（部分需会员）|OPC 基金会::https://opcfoundation.org ;; 信息模型::https://reference.opcfoundation.org|参考站提供规范；NodeSet 文件按伴随规范获取。
eclass|ECLASS e.V.|发布方官网|付费 / 许可|ECLASS::https://eclass.eu|在 ECLASS 官网按许可与版本获取；部分内容可在线浏览。
emmo|EMMC / EMMO 社区|官方仓库|公开免费|EMMO 仓库::https://github.com/emmo-repo/EMMO|从仓库 Release 取得 OWL。
energistics|Energistics（现属 OSDU / The Open Group）|发布方官网|公开免费|Energistics 标准::https://energistics.org/standards|标准下载页按 WITSML、RESQML、PRODML 提供 schema。
iso20022|ISO 20022 注册管理机构|标准组织|公开免费|ISO 20022::https://www.iso20022.org|官网提供报文库与业务模型下载。
xbrl|XBRL 国际|标准组织|公开免费|XBRL::https://www.xbrl.org|官网提供规范；分类法由各监管机构发布。
hpo|Monarch 倡议 / HPO 项目|官方仓库|公开免费|HPO::https://hpo.jax.org ;; 仓库::https://github.com/obophenotype/human-phenotype-ontology|通过官网或仓库 Release 取得。
doid|Disease Ontology 项目|发布方官网|公开免费|Disease Ontology::https://disease-ontology.org|官网与仓库提供 OBO / OWL。
mondo|Monarch 倡议|官方仓库|公开免费|Mondo::https://mondo.monarchinitiative.org|官网与仓库提供各发行文件。
ncit|美国国家癌症研究所（NCI）|发布方官网|公开免费|NCI EVS::https://evs.nci.nih.gov|NCI EVS 提供 OWL 与流文件下载。
omop|OHDSI 社区|发布方官网|公开免费|OHDSI 数据标准化::https://www.ohdsi.org/data-standardization/ ;; Athena 词汇下载::https://athena.ohdsi.org|Athena 提供标准词汇下载，部分词汇需另行取得许可。
brick|Brick 联盟|发布方官网|公开免费|Brick::https://brickschema.org ;; 仓库::https://github.com/BrickSchema/Brick|从官网或仓库取得各版本 Turtle。
realestatecore|RealEstateCore 联盟|发布方官网|公开免费|RealEstateCore::https://www.realestatecore.io|官网与其 GitHub 组织提供本体。
gs1-dl|GS1|标准组织|公开免费|GS1 Digital Link::https://www.gs1.org/standards/gs1-digital-link|GS1 官网提供标准 PDF。
geosparql|开放地理空间联盟（OGC）|标准组织|公开免费|GeoSPARQL::https://www.ogc.org/standard/geosparql/|OGC 官网提供规范与本体。
smartdatamodels|Smart Data Models 项目（FIWARE 等社区）|发布方官网|公开免费|Smart Data Models::https://smartdatamodels.org|官网与其 GitHub 组织提供各领域模型。
sensorthings|开放地理空间联盟（OGC）|标准组织|公开免费|SensorThings::https://www.ogc.org/standard/sensorthings/|OGC 官网提供规范文档。
iso23247|ISO TC184/SC4|标准组织|付费|ISO 23247-1::https://www.iso.org/standard/75066.html|向 ISO 或国家标准机构购买。
dpv|W3C 数据隐私词汇与控制社区组（DPVCG）|标准组织|公开免费|DPV::https://w3c.github.io/dpv/|规范站提供 Turtle 与 JSON-LD 下载。
cropontology|Crop Ontology 项目（CGIAR）|发布方官网|公开免费|Crop Ontology::https://cropontology.org|官网按作物提供本体下载。
po|Plant Ontology 联盟（OBO）|官方注册中心|公开免费|OBO 页面::https://obofoundry.org/ontology/po.html|通过 OBO 页面取得官方 PURL。
envo|ENVO 项目（OBO）|官方注册中心|公开免费|OBO 页面::https://obofoundry.org/ontology/envo.html ;; 仓库::https://github.com/EnvironmentOntology/envo|通过 OBO 页面取得官方 PURL。
railml|railML.org|发布方官网|公开免费|railML::https://www.railml.org|官网提供各版本 schema。
gbfs|MobilityData / NABSA|发布方官网|公开免费|GBFS::https://gbfs.org ;; 仓库::https://github.com/MobilityData/gbfs|规范和 JSON schema 在仓库。
transxchange|英国交通部（DfT）|发布方官网|公开免费|TransXChange::https://www.gov.uk/government/collections/transxchange|政府网站提供 schema 与指南。'''
