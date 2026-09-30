# 基线报告 (Stage 0)

日期: 2026-10-01
仓库: `D:\地理信息系统\IndustrialHeritageGIS`（自 `D:\地理信息系统\OpenGIS` 完整复制，含 .git，工作分支 `feature/industrial-heritage-gis`，原仓库保持只读）

## 1. 技术栈

| 层 | 技术 |
|---|---|
| 桌面壳 | Electron 30 + electron-vite 2.3（main/preload/renderer 三段构建 → `out/`） |
| 前端 | React 18 + Zustand 4 + Tailwind 3 + react-resizable-panels |
| 地图 | MapLibre GL 4.7（单例 MapEngine，OSM/Carto 底图，渲染器插件式 `src/features/map/renderers/`） |
| 后端 | Python FastAPI + WebSocket JSON-RPC（litellm Agent 循环，工具装饰器自动发现） |
| 测试 | Vitest 2（13 个文件 155 用例，node 环境）；Python 侧 pytest 15 个文件；无 E2E 框架 |
| AI | litellm（OpenRouter 已在 `src/features/settings/providerMap.ts` 预置） |

## 2. 数据文件盘点（第 1—7 批国家工业遗产名单）

见 `data-pipeline/manifest/raw_files.json`（含 sha256）。对应关系：

| 批次 | 文件 | 记录数 |
|---|---|---|
| 1 | 7799881.xls | 11 |
| 2 | 7799405.pdf | 42 |
| 3 | 7576103.pdf | 49 |
| 4 | 国家工业遗产名单（第四批）.docx | 62（含第二批增补 1 条） |
| 5 | ec7698fcea41463885cd22e31943d9db.pdf | 31 |
| 6 | 907087582fcb435c9f2ab3e828162f61.pdf | 37 |
| 7 | e3061bbc941c419c9413f8ac35678a8f.pdf | 32 |
| 合计 | | 264 条原始记录 |

## 3. 改造前基线验证（未修改任何代码）

| 检查 | 命令 | 结果 |
|---|---|---|
| 依赖安装 | `npm install` | PASS（exit 0） |
| Typecheck | `npx tsc --noEmit` | PASS（exit 0） |
| 单元测试 | `npx vitest run` | **2 FAIL / 153 PASS**（历史失败，见 §4） |
| Lint | `npx eslint . --ext .ts,.tsx` | **FAIL（历史问题）**：仓库无 `eslint.config.js`，ESLint 9 无法启动 |
| 生产构建 | `npm run build` | PASS（渲染段 56.6s） |

## 4. 历史失败清单（改造前已存在，非本次引入）

1. `src/services/rpc/__tests__/handlers.test.ts` "registers expected method count"：期望 53 个 handler，实际注册 56 个 —— 上游新增 handler 未同步测试计数。
2. 同文件 "rpc.ui.map.add_raster_from_url with invalid params returns -32602"：传非法参数时返回 result 而非 -32602 —— 该 RPC 方法的 zod 校验缺失或测试契约漂移。
3. ESLint 9 需要平面配置文件，仓库缺失 → lint 脚本完全不可用。

处置计划：第 1、3 项与本项目相关且修复风险低，纳入修复（阶段 9 前完成）；第 2 项需判断是上游实现缺陷还是测试过期，甄别后修复并记录。若均无法安全修复，将写入 TEST_REPORT 已知问题。Python 侧 pytest 因涉及 venv 安装，在阶段 9 干净环境验证时运行。

## 5. 基线结论

- 以此为基准：本次改造不得新增上述之外的任何失败。
- OpenGIS 原有核心交互（地图平移/缩放/图层/identify/聊天/板模式）为回归保护对象。
- 数据侧已完成（详见 `data-pipeline/reports/normalize_report.json`）：
  - 264 条原始记录全部解析成功，序号连续、关键字段零缺失；
  - 1 条跨批增补自动归并（第四批#62 → 第二批"北京卫星制造厂"），产出 263 条主表记录；
  - 地理编码：253 区县精确 + 2 模糊匹配（源文件笔误，已标记复核）+ 7 城市回退（历史辖区/开发区，标记）+ 1 省级回退（源地址仅"甘肃省"，标记）+ 0 失败；全部坐标 GCJ-02→WGS84 转换，来源与精度逐条记录；
  - 行业分类规则 v1 覆盖率 100%（26 条"其他"经规则补全后归零），核心物项五类映射完成。
