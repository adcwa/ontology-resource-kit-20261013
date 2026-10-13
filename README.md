# 本体与标准 · 整理与下载工具包

整理日期：2026-10-13。

**本包已完成目录整理，但没有下载齐全上游资料。当前随包收录的上游原文件是 0 份。** 制作环境能访问部分网页文本，但外网原文件下载失败；没有用网页入口、摘要或占位文件冒充 `.owl`、`.ttl`、规范 PDF 或仓库 ZIP。

原清单的 **84 条记录**均已保留，归并为 **75 项资源、14 个领域**；另补充 **33 项**原清单未列出的常用本体与标准（共 108 项，标记为“补充项”，暂无自动下载任务，只提供官方入口）。去重的是重复入口，不是本体语义；SSN/SOSA、AAS 等跨领域保留交叉引用，Commons 的两个版本也保留。

## 先打开什么

解压后直接双击 `index.html`。不需要联网、不需要启动服务器，就能搜索目录、按领域/类型/获取方式筛选、查看原始链接、阅读纠错记录、勾选资源、导出选择及复制下载命令。网页展示的是**目录与本地下载记录**，不是上游网站的镜像。

完整 Markdown 清单：`docs/01-resource-catalog.md`。

官方获取来源：网页“获取来源”标签页或 `docs/05-official-sources.md`，列出每项资源的发布/维护方、权威类型（标准组织、发布方官网、官方仓库、官方注册中心）、获取权限（免费、付费、需许可）和官方入口。来源由整理者依据公开信息选定，**未在制作环境逐项访问核验**，以发布方页面为准。

错链与版本检查：`docs/02-link-and-version-audit.md`。已记录 15 项问题或澄清，包括两处指向完全无关标准的 ISO 链接；没有宣称其余所有链接都已逐项验证。

## 在本地取得原文件

需要 Python 3.9 或更新版本，以及能访问发布方网站的网络。基本下载功能只使用 Python 标准库，无需 `pip install`。不会自动安装软件，不需要 Git，不需要提供账号密码。

### macOS / Linux

在解压后的目录打开终端：

```bash
# 先查看下载计划，不联网、不下载
python3 download.py --all --docs --include-large --dry-run

# 执行公开候选资料下载，包括大型资源，并将真正下载到的文件打包
python3 download.py --all --docs --include-large --pack
```

也可以双击 `download_public.command`（默认跳过大型资源），或 `download_all_public.command`（包含大型候选）。macOS 未保留可执行权限时，在终端执行 `bash download_public.command`。不要通过关闭系统安全功能来运行不明文件。

### Windows

双击 `download_public.bat`，或在 PowerShell / 命令提示符中进入目录：

```powershell
py -3 download.py --all --docs --include-large --pack
```

如果 Python Launcher 不存在，可用已安装的 Python 3 对应的 `python` 命令。脚本不为你安装 Python。

### 只获取所需领域

```bash
# 查看领域编号和资源 ID
python3 download.py --list

# 03 为制造 / 工业 4.0；AAS 等资源虽然还属于数字孪生，只保存一次
python3 download.py --category 03 --docs --pack

# 按 ID 选择一组文件
python3 download.py --ids bfo,iof,skos,prov-o,dcat3,aas --docs --pack

# 只抓机器文件/直接附属资料，不下载仓库或单页快照
python3 download.py --all --only assets --include-large --pack

# 已下载文件将先核验 SHA-256，再跳过；失败文件从头重试
python3 download.py --all --docs --include-large --pack

# 验证已有下载，不访问网络
python3 download.py --verify
```

“恢复下载”是**按已完成文件继续**，不是 HTTP Range 字节级断点续传。未完成的 `.part` 文件会重新获取，不会登记为成功。

## 获取范围与状态

| 类型 | 工具行为 | 不代表什么 |
|---|---|---|
| GitHub 仓库 | 查询实际默认分支，解析为 commit SHA，再下载固定提交 ZIP；记录 SHA 和仓库许可标识 | 不等于最新版稳定发行，也不保证包含 Git LFS 实体或子模块内容 |
| 机器文件 | 尝试公开 OWL / RDF / TTL / OBO 等端点，核对响应类型并计算 SHA-256 | 不等于 OWL DL 一致性通过或依赖完整 |
| 公开规范 | 下载明确的 PDF，或从指定页面筛选直接链接文件 | 不等于该标准系列的全部分册 |
| 文档快照 | 仅在 `--docs` 时保存所列单页 HTML/PDF | 不镜像全站、图片、CSS、脚本或外链，离线样式和动态内容可能不完整 |
| 生态/平台入口 | 保留入口和可选介绍页 | 不下载整个 OBO / OSDU / UN/CEFACT 等生态 |
| 人工/许可项 | 保留链接、原因及后续要求，不自动下载正文 | 不绕过注册、授权、会员或付费机制 |
| 待核验来源 | 默认跳过 3 个未核实的仓库；保留原链接 | 不把访问失败当成来源不存在 |

全部 108 项都有归档说明；其中并非每一项都对应可自动下载的原文件。下载清单含 107 个候选任务（包括文档页和发现任务），**任务数不是已下载文件数**。一个发现任务可能取得多个文件，也可能没有符合条件的文件。脚本最多抓取每个指定页面直接链接的 40 个匹配文件；达到上限会报告 `partial`，不会声称全量完成。

## 下载后的目录

```text
ontology-resource-kit-20261013/
  index.html                         可搜索网页目录
  README.md                          使用说明和交付边界
  catalog/
    original.tsv                     84 条原始清单（保留原链接）
    catalog.json                     108 项规范化目录、来源及计划
    download-manifest.json           107 个候选下载任务
  docs/
    01-resource-catalog.md            完整清单
    02-link-and-version-audit.md      15 项检查记录
    03-manual-and-licensing.md        人工获取与授权项
    04-using-downloaded-ontologies.md 离线使用边界
    05-official-sources.md            官方获取来源
    category-01.md … category-14.md   分领域说明
  resources/<领域编号>/<资源 ID>/      本地运行后真正下载的原文件
  reports/
    delivery-status.json             本次交付状态（不会被下载结果改写）
    download-state.json              每份下载的 URL、路径、字节、SHA-256
    download-report.md               成功、失败、部分完成、跳过原因
    SHA256SUMS.downloads.txt          下载原文件校验值
    status.js                        网页目录读取的本地执行状态
  download.py                        下载、验证、打包 CLI
  tests/                             不依赖外网的自动测试
```

打包文件输出到解压目录的上一层，并附带 `.sha256` 校验文件。后续运行后重新打开 `index.html`，即可查看本地下载记录。`delivery-status.json` 和本 README 描述的是最初交付事实；后续文件数量以 `reports/download-state.json` 为准。

## 限流、体积与失败处理

默认并发 3，单文件上限 512 MiB，单次网络传输预算 2048 MiB（包含失败重试），ZIP 展开大小上限 4096 MiB。大型本体/仓库可能触发上限。确认磁盘空间和来源后可以明确调大：

```bash
python3 download.py --all --docs --include-large --max-mb 1024 --total-mb 8192 --pack
```

失败或部分完成的任务会让进程返回码为 `1`，但已经成功下载的文件仍然保留，`--pack` 仍会打包现有成果。返回 `0` 只说明本次选中的自动任务没有报错，**不表示人工、跳过或整个标准生态的资料齐全**。返回 `2` 表示参数/配置/打包问题。

GitHub 未登录 API 有访问配额。脚本会复用已解析的 commit，避免重复请求。确实需要提高配额时，可在本机通过 `GITHUB_TOKEN` 环境变量提供具备公开仓库读取权限的令牌；不要把令牌写入本文件、清单、截图或压缩包。令牌只发给 `api.github.com`，跨主机重定向会移除认证头。

默认遵循本机标准代理环境变量；保留 HTTPS 证书校验，不提供跳过证书或绕过站点访问控制的选项。遇到登录页、验证码、403 或限流时查看报告并使用官方入口处理。

`--refresh` 会重新解析仓库分支并重新获取浮动端点；它表示选择新的快照，不保证回到本清单整理日。归档需要固定版本时，应保留下载报告、原文件与校验值，不要仅保留一个 `latest` URL。

## 文件校验与安全

默认做响应类型、文件签名、部分格式结构检查与 SHA-256 记录；**这不是完整语法校验或 OWL 语义推理**。HTML 错误页不会被存成成功的 `.owl`/`.ttl` 文件。JSON 使用语法解析；RDF/XML 的默认检查只探测根元素，带 DTD 的文件不展开实体。

可选 `--rdf-validate` 使用本机已安装的 `rdflib` 验证 RDF/XML、Turtle 语法。脚本不会自动安装它；大型 RDF 文件应使用专用工具校验。该选项仍不验证 OWL Profile、一致性或 imports 闭包，也不把外部 imports 自动拉入。

ZIP 默认保留原包。只有 `--extract` 才解压，执行路径穿越、符号链接、文件数量和展开体积检查；从不执行下载的代码。不要直接运行仓库中的未知脚本。

## 本包的许可边界

`download.py`、本包原创网页和整理说明按本包 `LICENSE.txt` 使用；第三方标准、本体、文档、术语与数据仍适用各自原始许可。代码许可与资料再分发许可不可互相替代。归档只保留原始表达，不自行把 75 项标准合并成一个 OWL 本体。

制作过程未修改你的 GitHub 仓库、网盘、标准购买账户，也没有购买或取得付费标准使用权。

## 本次自检结果

28 项不依赖网络的单元测试通过，覆盖目录完整性、类型校验、错误页拦截、下载模拟、校验后跳过、损坏后重取、来源访问限制、GitHub 固定提交解析、发现上限、ZIP 安全及打包。

网页另通过 16 项 Chromium DOM 检查，包括 75 张资源卡、84 条原始记录、15 项检查记录、筛选、选择导出、弹窗及手机宽度布局。制作环境限制直接打开 file://，因此该测试使用内存载入生成的 HTML 和本地状态脚本；不宣称已验证所有本机浏览器或远端下载。

```bash
python3 -m unittest discover -s tests -v
```

可选网页测试位于 `tests/ui_smoke.py`，仅在本机已安装 Playwright 和 Chromium 时运行，不属于下载功能的依赖。实际结果见 `reports/test-results.txt` 与 `reports/ui-test-results.json`。**上述均为离线或模拟测试，不是 107 个候选下载任务的联网验收。**
