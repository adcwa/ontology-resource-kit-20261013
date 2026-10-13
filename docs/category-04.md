# 分领域目录

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
