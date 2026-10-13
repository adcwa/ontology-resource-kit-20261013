# 分领域目录

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
