# 本体与标准资源目录

整理日期：2026-10-13。原清单 84 条，按资源归并为 75 项，另补充 33 项（共 108 项），保留 14 个领域。

**本交付是整理目录与下载工具包，不是已下载齐全的本体资料库。当前包含上游原文件 0 份。**

归并只整理入口，不合并本体语义；不同版本和原始链接均保留。

## 目录

- [01 · 顶层本体](#01)
- [02 · W3C 跨行业基础设施](#02)
- [03 · 制造 / 工业 4.0](#03)
- [04 · 能源 / 电力](#04)
- [05 · 油气 / 流程工业](#05)
- [06 · 金融 / 监管](#06)
- [07 · 医疗 / 生命科学](#07)
- [08 · 建筑 / BIM](#08)
- [09 · 供应链 / 零售](#09)
- [10 · 智慧城市 / IoT](#10)
- [11 · 数字孪生](#11)
- [12 · 法律 / 合规](#12)
- [13 · 农业 / 食品](#13)
- [14 · 交通 / 物流](#14)

<a id="01"></a>
## 01 · 顶层本体

| ID | 资源 | 类型 | 获取方式 |
|---|---|---|---|
| `bfo` | [BFO 2020 / ISO 21838-2 配套实现](https://github.com/BFO-ontology/BFO-2020) | 顶层本体 | 公开下载候选 |
| `dolce` | [DOLCE](https://www.loa.istc.cnr.it/dolce/overview.html) | 顶层本体 | 公开下载候选 |
| `ontouml` | [UFO / OntoUML 文档](https://github.com/OntoUML/OntoUML) | 建模语言与方法 | 公开下载候选 |
| `sumo` | [SUMO](https://github.com/ontologyportal/sumo) | 顶层本体 | 公开下载候选 |
| `gfo` | [GFO](https://github.com/Onto-Med/GFO) | 顶层本体 | 公开下载候选 |
| `cco` | [Common Core Ontologies (CCO)](https://github.com/CommonCoreOntology/CommonCoreOntologies) | 中层本体 | 入口/生态，非单一资料包 |

### BFO 2020 / ISO 21838-2 配套实现

面向科学研究的上层本体，把世界分为持续存在的实体（continuant）与发生的过程（occurrent），是 ISO 21838-2 标准。

**典型用途：**作为生物医学及工业本体（OBO 成员、IOF）的共同顶层，统一“物体/属性/过程”的建模方式。

**获取与范围说明：**保留 BFO 2020 仓库定位；不要把仓库版本名称与早期 BFO 2.0 简单视为同一发布包。

核验范围：已访问相关页面/目录，但未取得原始文件。
归档标识：`bfo`；原文件状态：**未下载**。

- 原清单第 1 条：[BFO 2.0 (ISO 21838-2)](https://github.com/BFO-ontology/BFO-2020)（顶层本体）

**名称澄清：** 链接为 BFO 2020 artifacts；不能仅按 BFO 2.0 的旧标签归档。
来源：https://github.com/BFO-ontology/BFO-2020

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `github`：https://github.com/BFO-ontology/BFO-2020
- `file`：https://raw.githubusercontent.com/BFO-ontology/BFO-2020/master/21838-2/owl/bfo-core.owl

### DOLCE

意大利 ISTC-CNR 的认知导向顶层本体，区分持续体、事件、质与抽象，强调自然语言与常识中的范畴。

**典型用途：**为领域本体提供哲学上严谨的上层分类；常用 DOLCE-Lite / DUL 轻量版本。

**获取与范围说明：**官方 DOLCE 的一阶逻辑形式与 DOLCE Lite、DUL 的 OWL 重构版本须分别管理。

核验范围：已访问相关页面/目录，但未取得原始文件。
归档标识：`dolce`；原文件状态：**未下载**。

- 原清单第 2 条：[DOLCE](http://www.loa.istc.cnr.it/dolce/overview.html)（顶层本体）

**形式化区分：** 官方 DOLCE 为 FOL；DOLCE Lite 与 DUL 为不同程度的 OWL 适配/重构。
来源：https://www.loa.istc.cnr.it/dolce/overview.html

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `discover`：https://www.loa.istc.cnr.it/dolce/overview.html

### UFO / OntoUML 文档

OntoUML 是基于 UFO 的概念建模语言，用构造型（kind、role、phase 等）标注 UML 类图。

**典型用途：**在落地为 OWL 前先做概念模型的本体正确性分析与评审。

**获取与范围说明：**原链接是 OntoUML 语言文档，不是一个完整的 UFO OWL 本体文件。

核验范围：已访问相关页面/目录，但未取得原始文件。
归档标识：`ontouml`；原文件状态：**未下载**。

- 原清单第 3 条：[UFO / OntoUML](https://github.com/OntoUML/OntoUML)（顶层本体）

**类型纠正：** 给定仓库明确为 OntoUML Language Documentation，并非 UFO OWL 本体发行包。
来源：https://github.com/OntoUML/OntoUML

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `github`：https://github.com/OntoUML/OntoUML

### SUMO

IEEE 倡导的大型形式化上层本体，含中层与领域扩展，以 SUO-KIF 逻辑语言编写，并映射到 WordNet。

**典型用途：**需要一阶逻辑公理、自然语言词义映射或大范围通用知识的场景。

**获取与范围说明：**下载仓库原始表示；不要假定其原生逻辑内容能作为普通 OWL DL 本体直接导入。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`sumo`；原文件状态：**未下载**。

- 原清单第 4 条：[SUMO](https://github.com/ontologyportal/sumo)（顶层本体）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `github`：https://github.com/ontologyportal/sumo

### GFO

莱比锡大学的通用形式本体，覆盖范畴、过程、角色、时空等，同时服务生物医学与社会科学。

**典型用途：**作为兼顾物质与过程的上层本体参考，或对比 BFO / DOLCE 的选型。

**获取与范围说明：**完整本体采用模块组织；离线使用还需检查 imports 与版本 IRI。

核验范围：已访问相关页面/目录，但未取得原始文件。
归档标识：`gfo`；原文件状态：**未下载**。

- 原清单第 5 条：[GFO](https://github.com/Onto-Med/GFO)（顶层本体）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `github`：https://github.com/Onto-Med/GFO

### Common Core Ontologies (CCO)

以 BFO 为基础的一组中层本体，覆盖事件、人、组织、时间、地理与信息实体，由美国国防与情报界推动。

**典型用途：**在 BFO 与具体领域本体之间提供共用的中层概念，常与 IOF 配合。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`cco`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

<a id="02"></a>
## 02 · W3C 跨行业基础设施

| ID | 资源 | 类型 | 获取方式 |
|---|---|---|---|
| `owl2` | [OWL 2](https://www.w3.org/TR/owl2-overview/) | 建模语言规范 | 公开下载候选 |
| `rdf11` | [RDF 1.1](https://www.w3.org/TR/rdf11-concepts/) | 数据模型规范 | 公开下载候选 |
| `skos` | [SKOS](https://www.w3.org/TR/skos-reference/) | 词汇与知识组织 | 公开下载候选 |
| `prov-o` | [PROV-O](https://www.w3.org/TR/prov-o/) | 基础本体 | 公开下载候选 |
| `dcat3` | [DCAT 3](https://www.w3.org/TR/vocab-dcat-3/) | 基础本体 | 公开下载候选 |
| `ssn-sosa` | [SSN / SOSA](https://www.w3.org/TR/vocab-ssn/) | 基础本体 | 公开下载候选 |
| `schemaorg` | [Schema.org](https://schema.org/docs/schemas.html) | 通用词汇 | 公开下载候选 |
| `sparql11` | [SPARQL 1.1](https://www.w3.org/TR/sparql11-overview/) | 查询语言规范 | 公开下载候选 |
| `shacl` | [SHACL](https://www.w3.org/TR/shacl/) | 数据校验规范 | 入口/生态，非单一资料包 |
| `owl-time` | [OWL-Time](https://www.w3.org/TR/owl-time/) | 基础本体 | 入口/生态，非单一资料包 |
| `org` | [W3C Organization Ontology (ORG)](https://www.w3.org/TR/vocab-org/) | 基础本体 | 入口/生态，非单一资料包 |
| `foaf` | [FOAF](http://xmlns.com/foaf/spec/) | 基础词汇 | 入口/生态，非单一资料包 |
| `dcterms` | [Dublin Core Terms (DCMI)](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) | 元数据词汇 | 入口/生态，非单一资料包 |
| `jsonld11` | [JSON-LD 1.1](https://www.w3.org/TR/json-ld11/) | 数据格式规范 | 入口/生态，非单一资料包 |
| `qudt` | [QUDT](https://qudt.org) | 基础本体 | 入口/生态，非单一资料包 |

### OWL 2

W3C 的本体 Web 语言，在 RDF 之上定义类、属性、公理及 DL 语义，分 EL/QL/RL/DL 等子语言。

**典型用途：**编写与推理本体的基础语言；决定本体能表达什么、推理机能做什么。

**获取与范围说明：**语言规范，不是行业本体；附带词汇文件也不等于规范的全部语义。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`owl2`；原文件状态：**未下载**。

- 原清单第 6 条：[OWL 2](https://www.w3.org/TR/owl2-overview/)（W3C 跨行业基础设施）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `file`：https://www.w3.org/2002/07/owl

### RDF 1.1

W3C 数据模型：以“主语-谓语-宾语”三元组构成有向图，并带有 Turtle、RDF/XML 等序列化。

**典型用途：**所有语义 Web 数据与本体的底层格式，是理解其他资源的起点。

**获取与范围说明：**保留原指定 RDF 1.1；不把 RDF 图数据与 OWL 逻辑本体混称。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`rdf11`；原文件状态：**未下载**。

- 原清单第 7 条：[RDF 1.1](https://www.w3.org/TR/rdf11-concepts/)（W3C 跨行业基础设施）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `file`：https://www.w3.org/1999/02/22-rdf-syntax-ns
- `file`：https://www.w3.org/2000/01/rdf-schema

### SKOS

W3C 的简单知识组织系统，用 Concept、broader/narrower、prefLabel 表示叙词表、分类法。

**典型用途：**把现有词表、分类表发布为链接数据；不适合做严格逻辑推理。

**获取与范围说明：**规范文档与机器可读词汇分别下载。

核验范围：已访问相关页面/目录，但未取得原始文件。
归档标识：`skos`；原文件状态：**未下载**。

- 原清单第 8 条：[SKOS](https://www.w3.org/TR/skos-reference/)（W3C 跨行业基础设施）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `file`：https://www.w3.org/2004/02/skos/core.rdf

### PROV-O

W3C 溯源本体，核心为 Entity（实体）、Activity（活动）、Agent（主体）及其关系。

**典型用途：**记录数据“从哪来、谁做的、怎么生成”，用于审计、数据血缘与可信度。

**获取与范围说明：**溯源词汇与规范；保留上游命名空间。

核验范围：已访问相关页面/目录，但未取得原始文件。
归档标识：`prov-o`；原文件状态：**未下载**。

- 原清单第 9 条：[PROV-O](https://www.w3.org/TR/prov-o/)（W3C 跨行业基础设施）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `file`：https://www.w3.org/ns/prov-o.ttl

### DCAT 3

W3C 数据目录词汇第 3 版，描述 Catalog、Dataset、Distribution、DataService，并支持数据系列。

**典型用途：**发布数据门户、数据资产目录与开放数据元数据。

**获取与范围说明：**优先下载明确的 dcat3 序列化，避免与其他版本混淆。

核验范围：已访问相关页面/目录，但未取得原始文件。
归档标识：`dcat3`；原文件状态：**未下载**。

- 原清单第 10 条：[DCAT 3](https://www.w3.org/TR/vocab-dcat-3/)（W3C 跨行业基础设施）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `file`：https://www.w3.org/ns/dcat3.ttl
- `file`：https://www.w3.org/ns/dcat3.rdf

### SSN / SOSA

W3C 传感器、观测与执行器本体；SOSA 为轻量核心，SSN 为带公理的扩展。

**典型用途：**描述传感器、观测、采样与执行器，是物联网与环境监测本体的共同底座。

**获取与范围说明：**在基础设施与能源类别中交叉引用；原文件仅存一份。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`ssn-sosa`；原文件状态：**未下载**。

- 原清单第 11 条：[SSN / SOSA](https://www.w3.org/TR/vocab-ssn/)（W3C 跨行业基础设施）
- 原清单第 24 条：[W3C SSN/SOSA](https://www.w3.org/TR/vocab-ssn/)（能源 / 电力）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `file`：https://www.w3.org/ns/sosa/sosa.ttl
- `file`：https://www.w3.org/ns/ssn/ssn.ttl

### Schema.org

由搜索引擎联合维护的网页结构化数据词汇，覆盖商品、组织、事件、文章等数千类型。

**典型用途：**在网页中嵌入 JSON-LD / 微数据以利于搜索展示；也常作通用实体词汇。

**获取与范围说明：**沿用原目录位置，但 Schema.org 不等同于 W3C Recommendation；数据词汇与文档分开。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`schemaorg`；原文件状态：**未下载**。

- 原清单第 12 条：[Schema.org](https://schema.org/docs/schemas.html)（W3C 跨行业基础设施）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `file`：https://schema.org/version/latest/schemaorg-current-https.ttl（大型，需 --include-large）

### SPARQL 1.1

W3C 的 RDF 查询语言与协议规范，含 SELECT/CONSTRUCT、更新、联邦查询等。

**典型用途：**查询知识图谱与本体数据；是语言规范，无本体文件。

**获取与范围说明：**查询语言规范，不是 OWL 本体文件。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`sparql11`；原文件状态：**未下载**。

- 原清单第 13 条：[SPARQL 1.1](https://www.w3.org/TR/sparql11-overview/)（W3C 跨行业基础设施）

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### SHACL

W3C 的 RDF 图形状约束语言，用 Shape 描述节点与属性必须满足的条件。

**典型用途：**校验知识图谱数据质量；与 OWL 互补（OWL 推理，SHACL 校验）。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`shacl`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### OWL-Time

W3C 时间本体，描述时刻、区间、时长、时区及它们之间的 Allen 关系。

**典型用途：**给任何领域的数据加上标准化的时间表达。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`owl-time`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### W3C Organization Ontology (ORG)

描述组织、组织单元、成员、岗位与层级关系的词汇。

**典型用途：**组织架构、供应商或机构关系的建模。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`org`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### FOAF

描述人及其关系、账号与文档的经典 RDF 词汇。

**典型用途：**表示人员与社交关系；很多本体用它引用“人”。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`foaf`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### Dublin Core Terms (DCMI)

通用资源元数据词汇：标题、创建者、日期、主题、许可等。

**典型用途：**给任何资源打元数据；DCAT 与许多本体都复用它。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`dcterms`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### JSON-LD 1.1

W3C 的 JSON 链接数据格式，通过 @context 把普通 JSON 映射到 RDF 词汇。

**典型用途：**让 API 与网页数据同时是 JSON 和语义数据；WoT、DTDL、Schema.org 均使用。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`jsonld11`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### QUDT

量、单位、量纲与数据类型本体，含 SI 及大量单位的换算关系。

**典型用途：**给传感器、工程和科学数据标注统一的单位与量纲。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`qudt`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

<a id="03"></a>
## 03 · 制造 / 工业 4.0

| ID | 资源 | 类型 | 获取方式 |
|---|---|---|---|
| `iof` | [IOF 工业本体](https://github.com/iofoundry/ontology) | 领域本体 | 公开下载候选 |
| `step` | [STEP / ISO 10303-242](https://www.iso.org/standard/84667.html) | 数据交换标准 | 需人工选择/确认授权 |
| `ontostep` | [OntoSTEP](https://github.com/usnistgov/OntoSTEP) | 映射与实现 | 公开下载候选 |
| `rami40` | [RAMI 4.0](https://www.plattform-i40.de/IP/Redaktion/EN/Downloads/Publikation/rami40-an-introduction.html) | 参考架构 | 公开下载候选 |
| `aas` | [AAS / IDTA](https://github.com/admin-shell-io/aas-specs-metamodel) | 信息模型与接口 | 公开下载候选 |
| `saref4inma` | [SAREF4INMA](https://saref.etsi.org/saref4inma/v2.1.1/) | 领域本体 | 公开下载候选 |
| `opcua` | [OPC UA 信息模型](https://opcfoundation.org) | 工业通信标准 | 入口/生态，非单一资料包 |
| `eclass` | [ECLASS](https://eclass.eu) | 产品分类与属性字典 | 需人工选择/确认授权 |
| `emmo` | [EMMO](https://github.com/emmo-repo/EMMO) | 领域本体 | 入口/生态，非单一资料包 |

### IOF 工业本体

工业本体基金会的开放本体体系，以 BFO 为顶层，覆盖产品、过程、资源、供应链与维护。

**典型用途：**构建制造业跨系统语义互操作，是工业 4.0 语义层的核心候选。

**获取与范围说明：**下载仓库快照；快照不自动等同于已正式发布的 IOF 版本。

核验范围：已访问相关页面/目录，但未取得原始文件。
归档标识：`iof`；原文件状态：**未下载**。

- 原清单第 14 条：[IOF 工业本体联盟](https://github.com/iofoundry/ontology)（制造 / 工业 4.0）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `github`：https://github.com/iofoundry/ontology

### STEP / ISO 10303-242

ISO 10303（STEP）系列的 AP242 部分，用于交换 3D 产品制造信息（PMI）与产品结构。

**典型用途：**CAD / PLM 之间交换几何、公差、装配与材料数据；是付费标准，非本体。

**获取与范围说明：**原 ISO 链接只覆盖 AP242:2022，并非整个 ISO 10303 系列；不自动下载付费标准正文。

核验范围：已访问相关页面/目录，但未取得原始文件。
归档标识：`step`；原文件状态：**未下载**。

- 原清单第 15 条：[ISO 10303 (STEP)](https://www.iso.org/standard/84667.html)（制造 / 工业 4.0）

**范围与版本：** 原链接是已撤回的 ISO 10303-242:2022；官方页列有 2025 替代版。不是整个 STEP 系列。
来源：https://www.iso.org/standard/84667.html

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### OntoSTEP

NIST 将 STEP AP242 的 EXPRESS 模型转为 OWL 的实现，便于对 CAD 数据做语义推理。

**典型用途：**把 STEP 产品数据接入本体与知识图谱。

**获取与范围说明：**保留 NIST 实现仓库，与 ISO 标准正文分开；下载成功不证明覆盖整个 STEP 系列。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`ontostep`；原文件状态：**未下载**。

- 原清单第 16 条：[OntoSTEP (OWL)](https://github.com/usnistgov/OntoSTEP)（制造 / 工业 4.0）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `github`：https://github.com/usnistgov/OntoSTEP

### RAMI 4.0

德国工业 4.0 参考架构模型：层级、生命周期价值流与架构层三维框架，已列入 IEC PAS 63088。

**典型用途：**用来定位工业 4.0 组件，是规划参考框架而非可导入本体。

**获取与范围说明：**参考架构文档，不是可直接导入的 OWL 行业本体。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`rami40`；原文件状态：**未下载**。

- 原清单第 17 条：[RAMI 4.0 参考架构](https://www.plattform-i40.de/IP/Redaktion/EN/Downloads/Publikation/rami40-an-introduction.html)（制造 / 工业 4.0）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `discover`：https://www.plattform-i40.de/IP/Redaktion/EN/Downloads/Publikation/rami40-an-introduction.html

### AAS / IDTA

工业 4.0 资产管理壳：以元模型描述资产的子模型、属性与语义引用，由 IDTA 维护。

**典型用途：**制造设备数字孪生的标准化信息模型；与 ECLASS 等语义字典配合使用。

**获取与范围说明：**原仓库已重定向到元模型仓库；该仓库不代表所有 AAS API 与子模型模板。

核验范围：已访问相关页面/目录，但未取得原始文件。
归档标识：`aas`；原文件状态：**未下载**。

- 原清单第 18 条：[AAS 资产管理壳 IDTA v3](https://github.com/admin-shell-io/aas-specs)（制造 / 工业 4.0）
- 原清单第 64 条：[AAS 规范 (IDTA)](https://industrialdigitaltwin.org/content-hub/aasspecifications)（数字孪生）
- 原清单第 65 条：[AAS GitHub](https://github.com/admin-shell-io/aas-specs)（数字孪生）

**仓库重定向：** 原 aas-specs 已重定向为 aas-specs-metamodel。
来源：https://github.com/admin-shell-io/aas-specs-metamodel

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `github`：https://github.com/admin-shell-io/aas-specs-metamodel

### SAREF4INMA

ETSI SAREF 的工业制造扩展，建模工件、生产设备、物料与生产过程。

**典型用途：**智能制造设备与产品数据的语义对接。

**获取与范围说明：**已核实页面指向 v2.1.1；下载该版本正文与序列化，imports 仍需另行检查。

核验范围：已访问相关页面/目录，但未取得原始文件。
归档标识：`saref4inma`；原文件状态：**未下载**。

- 原清单第 19 条：[ETSI SAREF4INMA](https://saref.etsi.org/saref4inma/)（制造 / 工业 4.0）

**版本补全：** 原无版本页面重定向至 v2.1.1，页面标注发布日期 2025-04-25。
来源：https://saref.etsi.org/saref4inma/v2.1.1/

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `file`：https://saref.etsi.org/saref4inma/v2.1.1/

### OPC UA 信息模型

OPC 基金会的工业通信标准，其信息模型把设备、变量、方法以节点图形式暴露，并有各行业伴随规范。

**典型用途：**工厂设备与 MES/SCADA 的统一接入；与 AAS 可互相映射。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`opcua`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### ECLASS

标准化产品分类与属性语义字典，含数万产品类和属性定义，被 AAS 广泛用作语义标识。

**典型用途：**给设备和零部件的属性提供全球唯一的语义 ID；下载需按许可获取。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`eclass`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### EMMO

欧洲材料与建模本体，用统一框架描述材料、过程、性质与建模表示。

**典型用途：**材料科学与制造研发的数据语义化。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`emmo`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

<a id="04"></a>
## 04 · 能源 / 电力

| ID | 资源 | 类型 | 获取方式 |
|---|---|---|---|
| `ssn-sosa` | [SSN / SOSA](https://www.w3.org/TR/vocab-ssn/) | 基础本体 | 公开下载候选 |
| `cim` | [IEC CIM / 第三方 OWL 实现](https://www.iec.ch/TC57) | 领域信息模型 | 来源待核验 |
| `iec61850` | [IEC 61850](https://www.iec.ch/homepage) | 通信与信息模型标准 | 需人工选择/确认授权 |
| `saref4ener` | [SAREF4ENER](https://saref.etsi.org/saref4ener/) | 领域本体 | 公开下载候选 |

### SSN / SOSA

W3C 传感器、观测与执行器本体；SOSA 为轻量核心，SSN 为带公理的扩展。

**典型用途：**描述传感器、观测、采样与执行器，是物联网与环境监测本体的共同底座。

**获取与范围说明：**在基础设施与能源类别中交叉引用；原文件仅存一份。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`ssn-sosa`；原文件状态：**未下载**。

- 原清单第 11 条：[SSN / SOSA](https://www.w3.org/TR/vocab-ssn/)（W3C 跨行业基础设施）
- 原清单第 24 条：[W3C SSN/SOSA](https://www.w3.org/TR/vocab-ssn/)（能源 / 电力）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `file`：https://www.w3.org/ns/sosa/sosa.ttl
- `file`：https://www.w3.org/ns/ssn/ssn.ttl

### IEC CIM / 第三方 OWL 实现

IEC 61970/61968 公共信息模型，描述电力系统的设备、拓扑、量测与资产，常以 UML/RDFS 表达。

**典型用途：**电网调度、资产管理与能源系统之间的数据交换。

**获取与范围说明：**IEC TC57 页面和第三方 CIM-OWL 仓库分开保留；本次未能核实原仓库，不视为 IEC 官方 OWL 发布。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`cim`；原文件状态：**未下载**。

- 原清单第 20 条：[IEC CIM (61970/61968) OWL](https://github.com/griddigit-ci/CIM-OWL)（能源 / 电力）
- 原清单第 21 条：[IEC CIM 官方页面](https://www.iec.ch/TC57)（能源 / 电力）

**待核验：** 原 CIM-OWL 仓库本次未能获取；不能仅据一次失败断言仓库不存在。IEC TC57 不是该 OWL 包的下载页。
来源：https://github.com/griddigit-ci/CIM-OWL

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `github`：https://github.com/griddigit-ci/CIM-OWL

### IEC 61850

电力自动化通信标准，定义变电站设备的逻辑节点、数据对象与服务模型。

**典型用途：**变电站与分布式能源的设备建模及通信。

**获取与范围说明：**原链接只是 IEC 首页，无法唯一定位系列规范、分册、版本或可下载包。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`iec61850`；原文件状态：**未下载**。

- 原清单第 22 条：[IEC 61850 概览](https://www.iec.ch/homepage)（能源 / 电力）

**链接过泛：** 原链接是 IEC 首页，不足以定位 IEC 61850 的适用分册与发行文件。
来源：https://www.iec.ch/homepage

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### SAREF4ENER

ETSI SAREF 的能源扩展，建模需求响应、设备能耗与能量曲线，对接 EEBus 等。

**典型用途：**智能家居、能源管理与需求响应设备的语义互通。

**获取与范围说明：**下载其公开序列化；实际版本以下载报告为准。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`saref4ener`；原文件状态：**未下载**。

- 原清单第 23 条：[ETSI SAREF4ENER](https://saref.etsi.org/saref4ener/)（能源 / 电力）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `file`：https://saref.etsi.org/saref4ener/

<a id="05"></a>
## 05 · 油气 / 流程工业

| ID | 资源 | 类型 | 获取方式 |
|---|---|---|---|
| `iso15926` | [ISO 15926 系列](https://www.iso.org/standard/29557.html) | 生命周期数据标准 | 需人工选择/确认授权 |
| `iso15926-impl` | [ISO 15926 RDF/OWL 实现候选](https://github.com/Posccaesar/Life-Cycle-Model) | 映射与实现 | 来源待核验 |
| `osdu` | [OSDU](https://osduforum.org) | 数据平台与生态 | 入口/生态，非单一资料包 |
| `ppdm` | [PPDM](https://ppdm.org/ppdm/PPDM/Standards) | 领域数据模型 | 需人工选择/确认授权 |
| `energistics` | [Energistics 标准（WITSML / RESQML / PRODML）](https://energistics.org/standards) | 行业数据标准 | 入口/生态，非单一资料包 |

### ISO 15926 系列

流程工业全生命周期数据集成标准，Part 2 提供通用数据模型，并配参考数据库。

**典型用途：**石化、油气工厂设计、建造到运维的数据交换与集成。

**获取与范围说明：**原链接错配为 ISO 15614-11:2025；新增正确的 Part 2 数据模型标准入口。

核验范围：已访问相关页面/目录，但未取得原始文件。
归档标识：`iso15926`；原文件状态：**未下载**。

- 原清单第 25 条：[ISO 15926](https://www.iso.org/standard/81785.html)（油气 / 流程工业）

**错链：** 原 /81785.html 是 ISO 15614-11:2025 焊接程序试验。已新增 ISO 15926-2:2003 正确入口。
来源：https://www.iso.org/standard/29557.html

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### ISO 15926 RDF/OWL 实现候选

ISO 15926 生命周期模型的 RDF/OWL 实现候选，来源与完整性待核验。

**典型用途：**参考 ISO 15926 的 OWL 化思路；使用前需先确认其来源。

**获取与范围说明：**本次未能核实原 GitHub 仓库可用性；保留待核验，不能认定为完整标准实现。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`iso15926-impl`；原文件状态：**未下载**。

- 原清单第 26 条：[ISO 15926 RDF/OWL 实现](https://github.com/Posccaesar/Life-Cycle-Model)（油气 / 流程工业）

**待核验：** 原 Life-Cycle-Model 仓库本次未能获取；保留原 URL，不静默替换其他项目。
来源：https://github.com/Posccaesar/Life-Cycle-Model

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `github`：https://github.com/Posccaesar/Life-Cycle-Model

### OSDU

开放式地下数据宇宙：能源行业的开源数据平台，定义统一数据架构与数据类型。

**典型用途：**油气勘探开发数据整合；是平台生态，无单一本体文件。

**获取与范围说明：**生态与平台入口，不存在一个代表整个 OSDU 的单一本体文件；只收录入口与可选单页快照。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`osdu`；原文件状态：**未下载**。

- 原清单第 27 条：[OSDU 油气数据宇宙](https://osduforum.org)（油气 / 流程工业）

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### PPDM

石油行业数据管理协会的关系数据模型，覆盖井、地震、油田、合同等。

**典型用途：**油气上游数据管理与数据库设计。

**获取与范围说明：**需到发布方确认版本、会员/许可与下载范围；工具不使用账户或绕过登录。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`ppdm`；原文件状态：**未下载**。

- 原清单第 28 条：[PPDM](https://ppdm.org/ppdm/PPDM/Standards)（油气 / 流程工业）

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### Energistics 标准（WITSML / RESQML / PRODML）

油气上游数据交换标准族：钻井（WITSML）、地质建模（RESQML）、生产（PRODML），现由 OSDU 管理。

**典型用途：**钻井、油藏与生产数据在厂商和系统之间交换。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`energistics`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

<a id="06"></a>
## 06 · 金融 / 监管

| ID | 资源 | 类型 | 获取方式 |
|---|---|---|---|
| `fibo` | [FIBO](https://github.com/edmcouncil/fibo) | 领域本体 | 公开下载候选 |
| `commons` | [OMG Commons 1.2 / 1.3](https://www.omg.org/spec/Commons/1.3) | 基础本体 | 公开下载候选 |
| `actus` | [ACTUS](https://www.actusfrf.org) | 合约与计算标准 | 入口/生态，非单一资料包 |
| `iso20022` | [ISO 20022](https://www.iso20022.org) | 金融报文标准 | 入口/生态，非单一资料包 |
| `xbrl` | [XBRL](https://www.xbrl.org) | 财务报告标准 | 入口/生态，非单一资料包 |

### FIBO

EDM Council 的金融业商业本体，覆盖证券、衍生品、贷款、机构、合约等，多模块组织。

**典型用途：**金融数据治理、监管报告及风险数据的统一语义。

**获取与范围说明：**仓库与浏览器合并为一项；仓库默认分支快照不自动等于 production 发布版。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`fibo`；原文件状态：**未下载**。

- 原清单第 29 条：[FIBO (GitHub OWL)](https://github.com/edmcouncil/fibo)（金融 / 监管）
- 原清单第 30 条：[FIBO 在线浏览器](https://spec.edmcouncil.org/fibo/)（金融 / 监管）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `github`：https://github.com/edmcouncil/fibo（大型，需 --include-large）

### OMG Commons 1.2 / 1.3

OMG 的公共本体库，提供日期时间、数量、合约、组织等通用概念，是 FIBO 的基础。

**典型用途：**复用跨领域基础概念，避免各本体重复定义。

**获取与范围说明：**保留 1.2 历史版本；1.3 已于 2026 年 6 月正式采纳，不再标为 beta。

核验范围：已访问相关页面/目录，但未取得原始文件。
归档标识：`commons`；原文件状态：**未下载**。

- 原清单第 31 条：[OMG Commons Ontology Library v1.2](https://www.omg.org/spec/Commons/1.2)（金融 / 监管）
- 原清单第 32 条：[OMG Commons v1.3 beta](https://www.omg.org/spec/Commons)（金融 / 监管）

**状态更新：** 1.3 已列入 Formal Versions，采纳日期 June 2026；原 beta 标签过时。1.2 保留作为历史版本。
来源：https://www.omg.org/spec/Commons/1.3

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `discover`：https://www.omg.org/spec/Commons/1.3
- `discover`：https://www.omg.org/spec/Commons/1.2

### ACTUS

金融合约算法标准，用统一的现金流模式与参数描述各类合约的行为。

**典型用途：**对贷款、债券、衍生品等合约做现金流计算与风险模拟。

**获取与范围说明：**标准与生态入口，不等同于单个 OWL 本体；可选保存介绍页。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`actus`；原文件状态：**未下载**。

- 原清单第 33 条：[ACTUS 金融合约标准](https://www.actusfrf.org)（金融 / 监管）

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### ISO 20022

金融服务通用报文标准，含统一的业务模型和报文库，被支付系统广泛采用。

**典型用途：**银行支付、证券清算报文的统一语义。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`iso20022`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### XBRL

用于财务与监管报告的 XML 标准，以分类法（taxonomy）定义报表概念。

**典型用途：**上市公司与监管机构的结构化财报申报。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`xbrl`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

<a id="07"></a>
## 07 · 医疗 / 生命科学

| ID | 资源 | 类型 | 获取方式 |
|---|---|---|---|
| `snomedct` | [SNOMED CT](https://browser.ihtsdotools.org) | 医学术语体系 | 需人工选择/确认授权 |
| `fhir` | [HL7 FHIR](https://hl7.org/fhir/) | 医疗交换规范 | 公开下载候选 |
| `fhir-rdf` | [HL7 FHIR RDF](https://hl7.org/fhir/rdf.html) | RDF 表示规范 | 公开下载候选 |
| `obo` | [OBO Foundry](https://obofoundry.org) | 本体注册与生态 | 入口/生态，非单一资料包 |
| `go` | [Gene Ontology](https://geneontology.org) | 领域本体 | 公开下载候选 |
| `chebi` | [ChEBI](https://www.ebi.ac.uk/chebi/) | 领域本体与数据库 | 公开下载候选 |
| `uberon` | [UBERON](https://github.com/obophenotype/uberon) | 领域本体 | 公开下载候选 |
| `loinc` | [LOINC](https://loinc.org/downloads/) | 医学术语体系 | 需人工选择/确认授权 |
| `rxnorm` | [RxNorm](https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html) | 医学术语体系 | 需人工选择/确认授权 |
| `icd11` | [ICD-11 MMS / 2025-01](https://icd.who.int/browse/2025-01/mms/en) | 分类体系 | 需人工选择/确认授权 |
| `mesh` | [MeSH](https://www.nlm.nih.gov/mesh/meshhome.html) | 医学词表 | 入口/生态，非单一资料包 |
| `hpo` | [Human Phenotype Ontology (HPO)](https://hpo.jax.org) | 领域本体 | 入口/生态，非单一资料包 |
| `doid` | [Disease Ontology (DO)](https://disease-ontology.org) | 领域本体 | 入口/生态，非单一资料包 |
| `mondo` | [Mondo Disease Ontology](https://mondo.monarchinitiative.org) | 领域本体 | 入口/生态，非单一资料包 |
| `ncit` | [NCI Thesaurus (NCIt)](https://evs.nci.nih.gov) | 医学术语体系 | 入口/生态，非单一资料包 |
| `omop` | [OMOP 通用数据模型与标准词汇](https://www.ohdsi.org/data-standardization/) | 数据模型 | 入口/生态，非单一资料包 |

### SNOMED CT

全球最大的临床术语体系，含数十万概念及属性关系，以描述逻辑形式化。

**典型用途：**电子病历中诊断、操作与发现的标准编码；需按地区许可使用。

**获取与范围说明：**浏览器和下载入口合并；需按地区及用途核对许可并从官方渠道取得发行包。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`snomedct`；原文件状态：**未下载**。

- 原清单第 34 条：[SNOMED CT 浏览器](https://browser.ihtsdotools.org)（医疗 / 生命科学）
- 原清单第 35 条：[SNOMED CT 下载](https://www.snomed.org/snomed-ct/get-snomed)（医疗 / 生命科学）

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### HL7 FHIR

HL7 的医疗互操作标准，以 REST 与资源（Patient、Observation 等）交换临床数据。

**典型用途：**医院系统、移动应用间的医疗数据 API；本身为交换标准，不是本体。

**获取与范围说明：**FHIR 规范、结构定义与数据实例不是同一类资源；不把整个站点冒充一份本体。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`fhir`；原文件状态：**未下载**。

- 原清单第 36 条：[HL7 FHIR](https://hl7.org/fhir/)（医疗 / 生命科学）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `discover`：https://hl7.org/fhir/

### HL7 FHIR RDF

FHIR 的 RDF 表示，使 FHIR 资源能表达为三元组并用 SPARQL 查询、校验。

**典型用途：**把 FHIR 数据接入知识图谱和语义推理。

**获取与范围说明：**保留 RDF 表示规范；标准描述页面并不等于本地已经存在完整 RDF 发行包。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`fhir-rdf`；原文件状态：**未下载**。

- 原清单第 37 条：[HL7 FHIR RDF](https://hl7.org/fhir/rdf.html)（医疗 / 生命科学）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `discover`：https://hl7.org/fhir/rdf.html

### OBO Foundry

OBO 本体注册联盟：维护一批互相对齐、遵循共同原则的开放生物医学本体。

**典型用途：**检索与选用生物医学本体；本身是注册中心。

**获取与范围说明：**注册目录不是一个本体；不自动递归下载所有成员本体。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`obo`；原文件状态：**未下载**。

- 原清单第 38 条：[OBO Foundry](https://obofoundry.org)（医疗 / 生命科学）

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### Gene Ontology

基因本体：描述基因产物的分子功能、生物过程与细胞组分的受控词表。

**典型用途：**基因功能注释与富集分析。

**获取与范围说明：**配置公开 go-basic.obo 下载候选；它不是全部 GO 注释数据或所有产品。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`go`；原文件状态：**未下载**。

- 原清单第 39 条：[Gene Ontology (GO)](https://geneontology.org)（医疗 / 生命科学）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `file`：https://purl.obolibrary.org/obo/go/go-basic.obo（大型，需 --include-large）

### ChEBI

生物相关小分子化合物本体，含结构、角色与分类关系。

**典型用途：**代谢、药物及化学实体的标准化命名与归类。

**获取与范围说明：**大型资源按需下载；词汇、本体与化合物数据库应分别管理。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`chebi`；原文件状态：**未下载**。

- 原清单第 40 条：[ChEBI](https://www.ebi.ac.uk/chebi/)（医疗 / 生命科学）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `discover`：https://www.ebi.ac.uk/chebi/（大型，需 --include-large）

### UBERON

跨物种解剖学本体，覆盖器官、组织及其结构与发育关系。

**典型用途：**跨物种表型、基因表达的解剖位置对齐。

**获取与范围说明：**仓库可能较大；源码快照不等于包含所有依赖的发行产品。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`uberon`；原文件状态：**未下载**。

- 原清单第 41 条：[UBERON](https://github.com/obophenotype/uberon)（医疗 / 生命科学）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `github`：https://github.com/obophenotype/uberon（大型，需 --include-large）

### LOINC

实验室检验与临床观察的通用编码，按成分、属性、时间、系统等六轴命名。

**典型用途：**检验项目与测量结果的标准编码与互通。

**获取与范围说明：**需从官方下载页选择版本并接受相应使用条款；不自动处理注册登录。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`loinc`；原文件状态：**未下载**。

- 原清单第 42 条：[LOINC](https://loinc.org/downloads/)（医疗 / 生命科学）

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### RxNorm

美国 NLM 的药品标准名称与编码，整合多个药品词表的映射。

**典型用途：**药品命名归一、处方与药物相互作用对接。

**获取与范围说明：**完整发行包与其他下载产品许可范围不同；从官方入口人工选择，不默认整包可自由再分发。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`rxnorm`；原文件状态：**未下载**。

- 原清单第 43 条：[RxNorm](https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html)（医疗 / 生命科学）

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### ICD-11 MMS / 2025-01

WHO 疾病与相关健康问题的国际分类第 11 版，MMS 用于统计与编码。

**典型用途：**疾病统计、医保与死因编码；2025-01 为指定历史版本。

**获取与范围说明：**保留用户指定的 2025-01 历史版本；浏览器入口不等于可下载的完整发行包。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`icd11`；原文件状态：**未下载**。

- 原清单第 44 条：[ICD-11](https://icd.who.int/browse/2025-01/mms/en)（医疗 / 生命科学）

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### MeSH

NLM 的医学主题词表，层级组织，用于 PubMed 文献标引与检索。

**典型用途：**医学文献标引、主题检索与语义扩展。

**获取与范围说明：**先在官方页面选择年度和发行格式；不把官网首页当作完整词表。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`mesh`；原文件状态：**未下载**。

- 原清单第 45 条：[MeSH](https://www.nlm.nih.gov/mesh/meshhome.html)（医疗 / 生命科学）

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### Human Phenotype Ontology (HPO)

人类疾病表型术语的本体，覆盖症状、体征及其层级关系。

**典型用途：**罕见病诊断与基因-表型分析。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`hpo`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### Disease Ontology (DO)

人类疾病的标准分类本体，与 MeSH、ICD、SNOMED 等有交叉引用。

**典型用途：**疾病数据整合与跨库对齐。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`doid`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### Mondo Disease Ontology

整合多个疾病分类的统一疾病本体，对 OMIM、Orphanet、DO 等做等价映射。

**典型用途：**罕见病与遗传病的跨数据库疾病对齐。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`mondo`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### NCI Thesaurus (NCIt)

美国国家癌症研究所的大型生物医学叙词表，覆盖癌症、药物、基因与临床研究概念。

**典型用途：**肿瘤学与临床研究的数据标注。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`ncit`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### OMOP 通用数据模型与标准词汇

OHDSI 的医疗观察数据通用模型，配套整合 SNOMED、LOINC、RxNorm 等的标准词汇。

**典型用途：**把各医院的真实世界数据转成统一结构做队列研究。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`omop`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

<a id="08"></a>
## 08 · 建筑 / BIM

| ID | 资源 | 类型 | 获取方式 |
|---|---|---|---|
| `ifc` | [IFC](https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/) | BIM 数据交换标准 | 公开下载候选 |
| `ifcowl` | [ifcOWL / IFC4 ADD2 TC1](https://standards.buildingsmart.org/IFC/DEV/IFC4/ADD2_TC1/OWL/) | 映射与实现 | 公开下载候选 |
| `bot` | [BOT](https://w3id.org/bot) | 领域本体 | 公开下载候选 |
| `citygml` | [CityGML 3.0](https://www.ogc.org/standard/citygml/) | 城市信息模型标准 | 公开下载候选 |
| `iso23387` | [ISO 23387 / BIM 数据模板](https://www.iso.org/standard/85391.html) | 信息模型标准 | 需人工选择/确认授权 |
| `brick` | [Brick Schema](https://brickschema.org) | 领域本体 | 入口/生态，非单一资料包 |
| `realestatecore` | [RealEstateCore](https://www.realestatecore.io) | 领域本体 | 入口/生态，非单一资料包 |

### IFC

buildingSMART 的建筑信息模型（BIM）开放数据交换标准，ISO 16739。

**典型用途：**建筑、结构、设备专业之间的 BIM 模型交换。

**获取与范围说明：**规范与 schema 按发行版管理；IFC 与 ifcOWL 不合并为同一个文件。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`ifc`；原文件状态：**未下载**。

- 原清单第 46 条：[IFC (buildingSMART)](https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/)（建筑 / BIM）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `discover`：https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/

### ifcOWL / IFC4 ADD2 TC1

IFC 的 OWL 版本，以 EXPRESS 转换，使 BIM 数据可用 RDF 与 SPARQL 处理。

**典型用途：**将 BIM 模型接入语义 Web，做查询与规则检查；转换结果体量大。

**获取与范围说明：**保留原指定 IFC4 ADD2 TC1 路径；不宣称与其他 IFC 版本完全等价。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`ifcowl`；原文件状态：**未下载**。

- 原清单第 47 条：[ifcOWL](https://standards.buildingsmart.org/IFC/DEV/IFC4/ADD2_TC1/OWL/)（建筑 / BIM）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `discover`：https://standards.buildingsmart.org/IFC/DEV/IFC4/ADD2_TC1/OWL/

### BOT

W3C LBD 社区的建筑拓扑本体：Site/Building/Storey/Space/Element 等轻量核心。

**典型用途：**在语义 Web 中描述建筑空间拓扑，与 IFC、SAREF 等配合。

**获取与范围说明：**官网与仓库合并；保留源文件、语言标签与许可证。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`bot`；原文件状态：**未下载**。

- 原清单第 48 条：[BOT 建筑拓扑本体](https://w3id.org/bot)（建筑 / BIM）
- 原清单第 49 条：[BOT GitHub](https://github.com/w3c-lbd-cg/bot)（建筑 / BIM）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `github`：https://github.com/w3c-lbd-cg/bot

### CityGML 3.0

OGC 的三维城市模型标准，含建筑、道路、地形、植被等对象及多级细节。

**典型用途：**数字城市、规划与仿真；3.0 区分概念模型与 GML/JSON 编码。

**获取与范围说明：**概念模型与编码实现分开；仅抓取入口页直接链接的选定资料，不镜像整个 OGC。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`citygml`；原文件状态：**未下载**。

- 原清单第 50 条：[CityGML 3.0](https://www.ogc.org/standard/citygml/)（建筑 / BIM）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `discover`：https://www.ogc.org/standard/citygml/

### ISO 23387 / BIM 数据模板

ISO 的 BIM 数据模板标准：以结构化属性模板描述建筑产品及其特性。

**典型用途：**建筑产品数据的标准化交付，与 IFC 属性集对应。

**获取与范围说明：**原入口未成功访问；新增官方 ISO 23387:2025 入口，标准正文按官方许可获取。

核验范围：已访问相关页面/目录，但未取得原始文件。
归档标识：`iso23387`；原文件状态：**未下载**。

- 原清单第 51 条：[ISO 23387 (BIM 数据模板)](https://www.iso.org/standard/75486.html)（建筑 / BIM）

**入口与版本：** 原 /75486.html 本次返回 404；ISO 23387:2025 正确入口为 /85391.html。
来源：https://www.iso.org/standard/85391.html

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### Brick Schema

描述楼宇设备、空间、点位及其关系的开放本体，面向楼宇自动化与分析。

**典型用途：**楼宇系统（暖通、照明、电表）的元数据统一，支撑数据分析应用。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`brick`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### RealEstateCore

面向房地产与智能建筑的本体，覆盖建筑、空间、租户、设备与合同。

**典型用途：**智能建筑、物业管理与数字孪生应用。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`realestatecore`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

<a id="09"></a>
## 09 · 供应链 / 零售

| ID | 资源 | 类型 | 获取方式 |
|---|---|---|---|
| `gs1voc` | [GS1 Web Vocabulary](https://www.gs1.org/voc/) | 领域词汇 | 公开下载候选 |
| `cbv` | [GS1 CBV](https://ref.gs1.org/standards/cbv/) | 业务事件词汇标准 | 公开下载候选 |
| `epcis` | [EPCIS 2.0](https://ref.gs1.org/standards/epcis/) | 事件数据交换标准 | 公开下载候选 |
| `goodrelations` | [GoodRelations](http://www.heppnetz.de/projects/goodrelations/) | 领域本体 | 公开下载候选 |
| `uncefact` | [UN/CEFACT](https://unece.org/trade/uncefact) | 标准生态与数据模型 | 入口/生态，非单一资料包 |
| `gs1-dl` | [GS1 Digital Link](https://www.gs1.org/standards/gs1-digital-link) | 标识标准 | 入口/生态，非单一资料包 |

### GS1 Web Vocabulary

GS1 的 Web 词汇，扩展 Schema.org，描述商品、品牌、成分、包装等属性。

**典型用途：**电商与零售商品数据的语义标记。

**获取与范围说明：**词汇与企业商品主数据不是一回事；不抓取商品实例数据。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`gs1voc`；原文件状态：**未下载**。

- 原清单第 52 条：[GS1 Web Vocabulary](https://www.gs1.org/voc/)（供应链 / 零售）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `discover`：https://www.gs1.org/voc/

### GS1 CBV

GS1 的核心业务词汇，规定 EPCIS 事件中业务步骤、状态、位置的取值。

**典型用途：**供应链可追溯事件的值域统一。

**获取与范围说明：**当前原链接返回 CBV 2.0 PDF；原清单的 ISO/IEC 19988:2024 标注本次未独立核验。

核验范围：已访问相关页面/目录，但未取得原始文件。
归档标识：`cbv`；原文件状态：**未下载**。

- 原清单第 53 条：[GS1 CBV (ISO/IEC 19988:2024)](https://ref.gs1.org/standards/cbv/)（供应链 / 零售）

**正文类型确认：** 原地址返回 Release 2.0、June 2022 的 GS1 CBV PDF；ISO/IEC 19988:2024 编号本次未独立核验。
来源：https://ref.gs1.org/standards/cbv/

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `file`：https://ref.gs1.org/standards/cbv/

### EPCIS 2.0

GS1 的电子产品代码信息服务标准，记录“什么物品、何时何地、因何事”事件。

**典型用途：**供应链追踪溯源与可视化；2.0 增加 JSON-LD 与 REST。

**获取与范围说明：**下载规范及页面直接链接的 schema；不将其称作一份完整 OWL 本体。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`epcis`；原文件状态：**未下载**。

- 原清单第 54 条：[EPCIS 2.0](https://ref.gs1.org/standards/epcis/)（供应链 / 零售）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `file`：https://ref.gs1.org/standards/epcis/

### GoodRelations

早期的电商本体，描述报价、商品、价格、业务实体与条款，后被 Schema.org 采纳。

**典型用途：**理解电商语义标记的历史；新项目多直接用 Schema.org。

**获取与范围说明：**保留原官网并尝试公开 OWL 序列化；历史 HTTP 入口可能跳转或失效。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`goodrelations`；原文件状态：**未下载**。

- 原清单第 55 条：[GoodRelations](http://www.heppnetz.de/projects/goodrelations/)（供应链 / 零售）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `file`：http://purl.org/goodrelations/v1

### UN/CEFACT

联合国贸易便利化与电子商务中心的标准集，含核心组件、跨行业发票与贸易模型。

**典型用途：**国际贸易单证与跨境数据交换。

**获取与范围说明：**组织入口覆盖多项标准，需进一步指定业务范围和版本才能获得完整资料集。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`uncefact`；原文件状态：**未下载**。

- 原清单第 56 条：[UN/CEFACT](https://unece.org/trade/uncefact)（供应链 / 零售）

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### GS1 Digital Link

把 GTIN、批号等 GS1 标识编码成 Web URI 的标准，使二维码可直接指向产品信息。

**典型用途：**产品追溯、消费者扫码与产品护照。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`gs1-dl`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

<a id="10"></a>
## 10 · 智慧城市 / IoT

| ID | 资源 | 类型 | 获取方式 |
|---|---|---|---|
| `saref` | [SAREF 核心与扩展索引](https://saref.etsi.org) | 本体家族 | 公开下载候选 |
| `saref4city` | [SAREF4CITY](https://saref.etsi.org/saref4city/) | 领域本体 | 公开下载候选 |
| `saref4bldg` | [SAREF4BLDG](https://saref.etsi.org/saref4bldg/) | 领域本体 | 公开下载候选 |
| `saref4watr` | [SAREF4WATR](https://saref.etsi.org/saref4watr/) | 领域本体 | 公开下载候选 |
| `onem2m` | [oneM2M 基础本体入口](https://www.onem2m.org/technical/published-specifications) | 标准与本体入口 | 入口/生态，非单一资料包 |
| `smof` | [SMOF（待核验）](https://github.com/wddabc/SMOF) | 待核验资源 | 来源待核验 |
| `geosparql` | [GeoSPARQL](https://www.ogc.org/standard/geosparql/) | 基础本体 | 入口/生态，非单一资料包 |
| `smartdatamodels` | [Smart Data Models](https://smartdatamodels.org) | 数据模型集合 | 入口/生态，非单一资料包 |
| `sensorthings` | [OGC SensorThings API](https://www.ogc.org/standard/sensorthings/) | 接口标准 | 入口/生态，非单一资料包 |

### SAREF 核心与扩展索引

ETSI 智能应用参考本体：对设备、功能、状态、服务与测量建模的核心及多个扩展。

**典型用途：**智能家居、楼宇、能源等物联网设备的语义互操作。

**获取与范围说明：**下载核心及本清单列出的扩展；“全系列”索引不代表已下载网站上所有扩展。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`saref`；原文件状态：**未下载**。

- 原清单第 57 条：[ETSI SAREF 全系列](https://saref.etsi.org)（智慧城市 / IoT）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `file`：https://saref.etsi.org/core/

### SAREF4CITY

SAREF 的智慧城市扩展，覆盖城市设施、兴趣点、交通与环境。

**典型用途：**智慧城市传感与服务的数据建模。

**获取与范围说明：**实际版本与序列化以下载日志为准。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`saref4city`；原文件状态：**未下载**。

- 原清单第 58 条：[SAREF4CITY](https://saref.etsi.org/saref4city/)（智慧城市 / IoT）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `file`：https://saref.etsi.org/saref4city/

### SAREF4BLDG

SAREF 的建筑扩展，描述建筑空间、设备及其与 IFC 概念的对照。

**典型用途：**智能楼宇与设备管理的语义集成。

**获取与范围说明：**实际版本与序列化以下载日志为准。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`saref4bldg`；原文件状态：**未下载**。

- 原清单第 59 条：[SAREF4BLDG](https://saref.etsi.org/saref4bldg/)（智慧城市 / IoT）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `file`：https://saref.etsi.org/saref4bldg/

### SAREF4WATR

SAREF 的水务扩展，描述水表、管网、水质与用水行为。

**典型用途：**智能水务监测与分析。

**获取与范围说明：**实际版本与序列化以下载日志为准。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`saref4watr`；原文件状态：**未下载**。

- 原清单第 60 条：[SAREF4WATR](https://saref.etsi.org/saref4watr/)（智慧城市 / IoT）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `file`：https://saref.etsi.org/saref4watr/

### oneM2M 基础本体入口

oneM2M 物联网标准的基础本体，将资源与设备映射到 SAREF，便于语义互操作。

**典型用途：**物联网平台间的语义发现与跨厂商互操作。

**获取与范围说明：**原页面是规范索引；需选择适用的 Base Ontology 分册和版本，而非整个标准目录。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`onem2m`；原文件状态：**未下载**。

- 原清单第 61 条：[oneM2M 基础本体](https://www.onem2m.org/technical/published-specifications)（智慧城市 / IoT）

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### SMOF（待核验）

待核验资源：仅保留原仓库链接，具体含义尚未确认。

**典型用途：**须先核实仓库身份后再使用。

**获取与范围说明：**本次未能核实 wddabc/SMOF 仓库的可访问性和所指资源，不猜测替代项目。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`smof`；原文件状态：**未下载**。

- 原清单第 62 条：[SMOF](https://github.com/wddabc/SMOF)（智慧城市 / IoT）

**待核验：** 原 SMOF 仓库与项目身份本次未核实；默认不自动下载该候选。
来源：https://github.com/wddabc/SMOF

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `github`：https://github.com/wddabc/SMOF

### GeoSPARQL

OGC 标准，为 RDF 提供空间对象与几何表示及 SPARQL 空间函数。

**典型用途：**在知识图谱里做空间查询，如城市、地块、设施位置。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`geosparql`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### Smart Data Models

FIWARE 等社区维护的跨领域数据模型库，涵盖智慧城市、能源、农业与制造，并带 JSON Schema 与 JSON-LD 上下文。

**典型用途：**快速取得面向 NGSI-LD / API 的现成数据模型。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`smartdatamodels`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### OGC SensorThings API

OGC 的物联网传感器数据 API，数据模型与 SOSA/SSN 对应。

**典型用途：**传感器与观测数据的标准化 REST 服务。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`sensorthings`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

<a id="11"></a>
## 11 · 数字孪生

| ID | 资源 | 类型 | 获取方式 |
|---|---|---|---|
| `aas` | [AAS / IDTA](https://github.com/admin-shell-io/aas-specs-metamodel) | 信息模型与接口 | 公开下载候选 |
| `iso30173` | [ISO/IEC 30173:2023](https://www.iso.org/standard/81442.html) | 概念与术语标准 | 需人工选择/确认授权 |
| `dtdl` | [DTDL](https://github.com/Azure/opendigitaltwins-dtdl) | 数字孪生建模语言 | 公开下载候选 |
| `wot-td` | [W3C WoT Thing Description](https://www.w3.org/TR/wot-thing-description/) | 物描述与接口规范 | 公开下载候选 |
| `ido` | [IDO / ISO 23726-3](https://www.iso.org/standard/87560.html) | 工业本体标准 | 需人工选择/确认授权 |
| `iso23247` | [ISO 23247 制造数字孪生框架](https://www.iso.org/standard/75066.html) | 数字孪生标准 | 需人工选择/确认授权 |

### AAS / IDTA

工业 4.0 资产管理壳：以元模型描述资产的子模型、属性与语义引用，由 IDTA 维护。

**典型用途：**制造设备数字孪生的标准化信息模型；与 ECLASS 等语义字典配合使用。

**获取与范围说明：**原仓库已重定向到元模型仓库；该仓库不代表所有 AAS API 与子模型模板。

核验范围：已访问相关页面/目录，但未取得原始文件。
归档标识：`aas`；原文件状态：**未下载**。

- 原清单第 18 条：[AAS 资产管理壳 IDTA v3](https://github.com/admin-shell-io/aas-specs)（制造 / 工业 4.0）
- 原清单第 64 条：[AAS 规范 (IDTA)](https://industrialdigitaltwin.org/content-hub/aasspecifications)（数字孪生）
- 原清单第 65 条：[AAS GitHub](https://github.com/admin-shell-io/aas-specs)（数字孪生）

**仓库重定向：** 原 aas-specs 已重定向为 aas-specs-metamodel。
来源：https://github.com/admin-shell-io/aas-specs-metamodel

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `github`：https://github.com/admin-shell-io/aas-specs-metamodel

### ISO/IEC 30173:2023

ISO/IEC 数字孪生概念与术语标准，定义孪生、实体、同步等基本概念。

**典型用途：**统一数字孪生项目的术语和概念共识；是术语标准，非本体。

**获取与范围说明：**数字孪生概念与术语标准，不是可直接导入的 OWL 数据包。

核验范围：已访问相关页面/目录，但未取得原始文件。
归档标识：`iso30173`；原文件状态：**未下载**。

- 原清单第 63 条：[ISO/IEC 30173:2023](https://www.iso.org/standard/81442.html)（数字孪生）

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### DTDL

微软数字孪生定义语言，以 JSON-LD 定义接口、遥测、属性、命令与关系。

**典型用途：**在 Azure Digital Twins 等平台建模设备与环境；不是 OWL。

**获取与范围说明：**建模语言与模型定义格式；不要当作 OWL 本体直接交给 OWL 推理机。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`dtdl`；原文件状态：**未下载**。

- 原清单第 66 条：[DTDL (微软)](https://github.com/Azure/opendigitaltwins-dtdl)（数字孪生）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `github`：https://github.com/Azure/opendigitaltwins-dtdl

### W3C WoT Thing Description

W3C 物联网 Web 描述，以 JSON-LD 描述设备的属性、动作、事件与交互协议。

**典型用途：**让不同厂商设备以 Web 方式被发现与调用。

**获取与范围说明：**下载指定规范及直接链接的机器可读附属文件；区分规范版本与设备实例。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`wot-td`；原文件状态：**未下载**。

- 原清单第 67 条：[W3C WoT Thing Description](https://www.w3.org/TR/wot-thing-description/)（数字孪生）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `discover`：https://www.w3.org/TR/wot-thing-description/

### IDO / ISO 23726-3

ISO/FDIS 23726-3 工业数据本体：以 BFO 为基础的工业领域上层，补充工业概念。

**典型用途：**工业领域顶层语义标准化；标准仍在审批阶段。

**获取与范围说明：**原 URL 指向 ISO 5409:2024。正确入口为 ISO/FDIS 23726-3，当前仍处于审批阶段。

核验范围：已访问相关页面/目录，但未取得原始文件。
归档标识：`ido`；原文件状态：**未下载**。

- 原清单第 68 条：[ISO 23726 (IDO, 制定中)](https://www.iso.org/standard/84706.html)（数字孪生）

**错链与状态：** 原 /84706.html 是 ISO 5409:2024 烟气汞检测。正确项目为 ISO/FDIS 23726-3，阶段 50.20（核验时）。
来源：https://www.iso.org/standard/87560.html

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### ISO 23247 制造数字孪生框架

制造领域数字孪生的框架标准系列，定义参考架构与功能实体。

**典型用途：**制造数字孪生的整体设计参考；付费标准，非本体。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`iso23247`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

<a id="12"></a>
## 12 · 法律 / 合规

| ID | 资源 | 类型 | 获取方式 |
|---|---|---|---|
| `lkif` | [LKIF Core](https://github.com/RinkeHoekstra/lkif-core) | 领域本体 | 公开下载候选 |
| `legalruleml` | [OASIS LegalRuleML 1.0](https://docs.oasis-open.org/legalruleml/legalruleml-core-spec/v1.0/) | 规则交换规范 | 公开下载候选 |
| `akoma` | [Akoma Ntoso](http://www.akomantoso.org) | 文档标记规范 | 入口/生态，非单一资料包 |
| `eli` | [ELI](https://eur-lex.europa.eu/eli-register/about.html) | 标识与元数据框架 | 公开下载候选 |
| `odrl` | [ODRL](https://www.w3.org/TR/odrl-model/) | 策略模型与词汇 | 公开下载候选 |
| `dpv` | [Data Privacy Vocabulary (DPV)](https://w3c.github.io/dpv/) | 基础本体 | 入口/生态，非单一资料包 |

### LKIF Core

欧洲 ESTRELLA 项目的法律知识交换格式核心本体，含法律行为、规范、角色与主体。

**典型用途：**法律推理、合规与法律知识库的参考模块。

**获取与范围说明：**下载完整模块仓库；离线使用时检查所有 imports。

核验范围：已访问相关页面/目录，但未取得原始文件。
归档标识：`lkif`；原文件状态：**未下载**。

- 原清单第 69 条：[LKIF (GitHub)](https://github.com/RinkeHoekstra/lkif-core)（法律 / 合规）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `github`：https://github.com/RinkeHoekstra/lkif-core

### OASIS LegalRuleML 1.0

OASIS 的法律规则 XML 交换标准，可表示义务、许可、禁止及规则间的冲突与废止。

**典型用途：**法律条文的规则化表示与合规自动化。

**获取与范围说明：**法律规则交换格式，不等于一个 OWL 本体；保留规范与 schema。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`legalruleml`；原文件状态：**未下载**。

- 原清单第 70 条：[OASIS LegalRuleML](https://docs.oasis-open.org/legalruleml/legalruleml-core-spec/v1.0/)（法律 / 合规）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `discover`：https://docs.oasis-open.org/legalruleml/legalruleml-core-spec/v1.0/

### Akoma Ntoso

法律与议会文档的 XML 标记标准，含结构、元数据与版本引用。

**典型用途：**立法文本的结构化、检索与跨国共享。

**获取与范围说明：**法律文档结构化格式；门户不是完整机器可读发行包。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`akoma`；原文件状态：**未下载**。

- 原清单第 71 条：[Akoma Ntoso](http://www.akomantoso.org)（法律 / 合规）

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### ELI

欧洲立法标识符及元数据本体：为法律文本提供 URI、元数据与版本关系。

**典型用途：**在欧盟及成员国之间链接和检索法规。

**获取与范围说明：**官方说明页与其直接链接的本体/规范分开；不抓取全部欧盟法律正文。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`eli`；原文件状态：**未下载**。

- 原清单第 72 条：[ELI (欧盟法律链接)](https://eur-lex.europa.eu/eli-register/about.html)（法律 / 合规）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `discover`：https://eur-lex.europa.eu/eli-register/about.html

### ODRL

W3C 的权利表达语言：策略由许可、禁止与义务构成，规定对资产的约束。

**典型用途：**数字内容使用授权、数据空间中的使用策略。

**获取与范围说明：**保留模型规范与词汇；不把模型表达直接等同于法律有效性判断。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`odrl`；原文件状态：**未下载**。

- 原清单第 73 条：[W3C ODRL](https://www.w3.org/TR/odrl-model/)（法律 / 合规）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `file`：https://www.w3.org/ns/odrl/2/ODRL22.ttl

### Data Privacy Vocabulary (DPV)

W3C 数据隐私社区组的词汇，描述个人数据处理的目的、法律依据、主体权利与措施，并映射 GDPR。

**典型用途：**隐私合规记录、同意管理与数据处理清单。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`dpv`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

<a id="13"></a>
## 13 · 农业 / 食品

| ID | 资源 | 类型 | 获取方式 |
|---|---|---|---|
| `agrovoc` | [AGROVOC](https://agrovoc.fao.org/browse/agrovoc/en/) | 农业词表 | 入口/生态，非单一资料包 |
| `saref4agri` | [SAREF4AGRI](https://saref.etsi.org/saref4agri/) | 领域本体 | 公开下载候选 |
| `foodon` | [FoodOn](https://github.com/FoodOntology/foodon) | 领域本体 | 公开下载候选 |
| `agro` | [AgrO / AgroOntology](https://obofoundry.org/ontology/agro.html) | 领域本体 | 公开下载候选 |
| `cropontology` | [Crop Ontology](https://cropontology.org) | 领域本体 | 入口/生态，非单一资料包 |
| `po` | [Plant Ontology (PO)](https://obofoundry.org/ontology/po.html) | 领域本体 | 入口/生态，非单一资料包 |
| `envo` | [Environment Ontology (ENVO)](https://obofoundry.org/ontology/envo.html) | 领域本体 | 入口/生态，非单一资料包 |

### AGROVOC

联合国粮农组织的多语言农业叙词表，含数十万概念，以 SKOS 发布。

**典型用途：**农业文献标引与多语言检索、数据对齐。

**获取与范围说明：**浏览器与 SPARQL 接口合并；SPARQL endpoint 是服务地址，不是离线全量文件。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`agrovoc`；原文件状态：**未下载**。

- 原清单第 74 条：[AGROVOC](https://agrovoc.fao.org/browse/agrovoc/en/)（农业 / 食品）
- 原清单第 75 条：[AGROVOC SPARQL](https://agrovoc.fao.org/sparql)（农业 / 食品）

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### SAREF4AGRI

SAREF 的农业扩展，建模农场、作物、传感器与农事活动。

**典型用途：**智慧农业设备与农事数据互联。

**获取与范围说明：**实际版本与序列化以下载日志为准。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`saref4agri`；原文件状态：**未下载**。

- 原清单第 76 条：[ETSI SAREF4AGRI](https://saref.etsi.org/saref4agri/)（农业 / 食品）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `file`：https://saref.etsi.org/saref4agri/

### FoodOn

食品本体：描述食品来源、加工、营养成分与分类，基于 OBO 原则。

**典型用途：**食品数据标注、溯源与营养研究。

**获取与范围说明：**大型本体仓库，按需选择；保留依赖和许可信息。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`foodon`；原文件状态：**未下载**。

- 原清单第 77 条：[FOODON](https://github.com/FoodOntology/foodon)（农业 / 食品）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `github`：https://github.com/FoodOntology/foodon（大型，需 --include-large）

### AgrO / AgroOntology

农业本体：描述农业流程、作物、农艺措施及相关表型。

**典型用途：**农业研究数据的标准化标注。

**获取与范围说明：**配置 OBO 官方持久地址作为下载候选；记录实际重定向与版本，不把页面下载当成本体下载。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`agro`；原文件状态：**未下载**。

- 原清单第 78 条：[AgroOntology (OBO)](https://obofoundry.org/ontology/agro.html)（农业 / 食品）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `file`：https://purl.obolibrary.org/obo/agro.owl

### Crop Ontology

作物性状、方法与尺度的本体集合，服务作物育种数据。

**典型用途：**育种试验与表型数据标准化。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`cropontology`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### Plant Ontology (PO)

植物解剖结构与发育阶段的本体，OBO 成员。

**典型用途：**植物基因表达与表型数据的结构对齐。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`po`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### Environment Ontology (ENVO)

描述环境系统、生物群落、环境材料的本体，OBO 成员。

**典型用途：**生态与农业数据的环境背景标注。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`envo`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

<a id="14"></a>
## 14 · 交通 / 物流

| ID | 资源 | 类型 | 获取方式 |
|---|---|---|---|
| `datex2` | [DATEX II](https://www.datex2.eu/datex2/downloads) | 交通数据交换模型 | 入口/生态，非单一资料包 |
| `siri` | [SIRI](https://www.transmodel-cen.eu/downloads/) | 交通数据交换规范 | 入口/生态，非单一资料包 |
| `transmodel-netex` | [Transmodel / NeTEx](https://www.transmodel-cen.eu) | 交通模型与交换规范 | 入口/生态，非单一资料包 |
| `otm` | [OpenTripModel 5](https://otm5.opentripmodel.org) | 物流信息模型 | 公开下载候选 |
| `gtfs` | [GTFS Schedule](https://gtfs.org/documentation/schedule/reference/) | 交通数据交换格式 | 公开下载候选 |
| `gtfs-rdf` | [Linked GTFS](https://github.com/OpenTransport/linked-gtfs) | RDF 词汇实现 | 公开下载候选 |
| `railml` | [railML](https://www.railml.org) | 铁路数据标准 | 入口/生态，非单一资料包 |
| `gbfs` | [GBFS](https://gbfs.org) | 共享出行数据规范 | 入口/生态，非单一资料包 |
| `transxchange` | [TransXChange](https://www.gov.uk/government/collections/transxchange) | 交通数据标准 | 入口/生态，非单一资料包 |

### DATEX II

欧洲交通数据交换标准，描述路况、事故、施工、停车及交通管理信息。

**典型用途：**交通管理中心之间交换实时交通信息。

**获取与范围说明：**下载入口可能需要选择模型配置和发行版；不尝试登录或替用户接受条款。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`datex2`；原文件状态：**未下载**。

- 原清单第 79 条：[DATEX II](https://www.datex2.eu/datex2/downloads)（交通 / 物流）

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### SIRI

公共交通服务接口：实时到站、车辆位置、预计到达及偏差。

**典型用途：**公共交通实时信息系统的互联。

**获取与范围说明：**原入口未指定分册、版本或 schema 包；保留给人工选择。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`siri`；原文件状态：**未下载**。

- 原清单第 80 条：[SIRI](https://www.transmodel-cen.eu/downloads/)（交通 / 物流）

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### Transmodel / NeTEx

Transmodel 是欧洲公共交通概念数据模型；NeTEx 是其 XML 交换实现。

**典型用途：**公交线网、时刻与票价数据的跨系统交换。

**获取与范围说明：**两者属于相关但不同层次的资源，保留组合原条目并说明范围，不能合并语义。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`transmodel-netex`；原文件状态：**未下载**。

- 原清单第 81 条：[Transmodel / NeTEx](https://www.transmodel-cen.eu)（交通 / 物流）

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### OpenTripModel 5

OpenTripModel：描述运输服务、预定、报价与履约的物流信息模型。

**典型用途：**货运物流与门到门出行服务之间的数据交换。

**获取与范围说明：**保留 OTM 5 文档及公开的直接附属文件；不是 OWL 本体默认入口。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`otm`；原文件状态：**未下载**。

- 原清单第 82 条：[OTM 开放交通模型](https://otm5.opentripmodel.org)（交通 / 物流）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `discover`：https://otm5.opentripmodel.org

### GTFS Schedule

通用公交数据规范：用 CSV 文件描述线路、站点、班次与时刻。

**典型用途：**Google 地图等发布公交时刻；开放数据最常用格式。

**获取与范围说明：**规范与真实运营机构的 feed 不同；本包不包含各地时刻表数据。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`gtfs`；原文件状态：**未下载**。

- 原清单第 83 条：[GTFS](https://gtfs.org/documentation/schedule/reference/)（交通 / 物流）

本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### Linked GTFS

GTFS 的 RDF 词汇，让公交时刻数据成为链接数据，可在 SPARQL 中查询。

**典型用途：**把公交数据融合入知识图谱或与其他数据集链接。

**获取与范围说明：**保留原项目仓库；不假定它与最新 GTFS 所有字段完全同步。

核验范围：已访问相关页面/目录，但未取得原始文件。
归档标识：`gtfs-rdf`；原文件状态：**未下载**。

- 原清单第 84 条：[GTFS-RDF](https://github.com/OpenTransport/linked-gtfs)（交通 / 物流）

下载计划（未执行/未落盘，不等于已验证的发行包）：
- `github`：https://github.com/OpenTransport/linked-gtfs

### railML

铁路领域 XML 数据交换标准，覆盖时刻表、基础设施与车辆。

**典型用途：**铁路设计、运营系统间的数据交换。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`railml`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### GBFS

共享单车、电动滑板车和租车的实时数据规范：站点、车辆可用性与定价。

**典型用途：**共享出行信息在地图与出行服务中的开放展示。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`gbfs`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。

### TransXChange

英国公交线路与时刻的 XML 交换格式。

**典型用途：**公交运营商向政府和出行平台提供时刻数据。

**获取与范围说明：**补充项：不在原 84 条清单内，尚未配置自动下载；请从“获取来源”所列官方入口取得，并确认版本与许可。

核验范围：未逐项确认页面及发行文件，仅保留原始入口和下载计划。
归档标识：`transxchange`；原文件状态：**未下载**。


本项保留人工入口；不自动抓取付费、登录后内容或整个标准生态。
