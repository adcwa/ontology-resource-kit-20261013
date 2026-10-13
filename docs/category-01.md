# 分领域目录

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
