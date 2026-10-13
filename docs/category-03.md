# 分领域目录

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
