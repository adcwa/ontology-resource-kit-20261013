# 分领域目录

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
