# 分领域目录

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
