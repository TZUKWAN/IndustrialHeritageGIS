# 实施摘要 / CHANGELOG

分支 `feature/industrial-heritage-gis`(基于上游 main dbe7027) ｜ 日期 2026-10-01

## 阶段 0 — 基线
- 原仓库保持只读; 完整复制为 `IndustrialHeritageGIS`(含 .git)。
- 基线: typecheck ✓ / build ✓ / vitest 153/155(2 个历史失败) / lint 不可用(缺配置)。
- 记录于 `docs/baseline_report.md`。

## 阶段 1 — 品牌
- 用户可见文案统一【工业文化遗产GIS智能体】: 浏览器标题、loading 页、地图徽标、聊天头部、alt 文本、i18n 空态、菜单、脚本运行器默认头、工作流版本提示、GeoTIFF 提示、electron-builder 产品名(制品名保持 ASCII)。
- 保留: 开源许可证、MIT 声明、内部包名 `opengis`、协议标识(`com.opengis.desktop`、`OPENGIS_*`、`.opengis/` 工作区目录)。

## 阶段 2 — 数据管线
- `parse_raw.py`: xls/pdf/docx 通用解析。要点: 表格线网格优先+字符聚类回退、序号锚定行、跨页续行归并、上下标/中西文混排行聚类、表头词精确匹配、语义校验(264 条全干净, 序号连续, 关键字段零缺失)。
- `fetch_admin.py`: DataV 行政区划索引(3238 条, GCJ-02)。
- `normalize.py`: 263 条主表(264 原始记录 − 1 条跨批自动归并), 稳定 ID, 查重报告, 行业规则 v1(覆盖率 100%, 关键词依据入库), 核心物项五类映射, GCJ-02→WGS84 地理编码(253 精确+2 模糊+7 城市回退+1 省回退+0 失败), 质检三报告。
- `docs/baseline_report.md` 记录数据基线指标。

## 阶段 3/4 — 数据模型与史实采集
- `build_enrichment.py`: 事件/关系/档案/来源模型; 档案程序化生成可溯源。
- 3 个研究代理并行采集: 7 批公告日期精确到日+官方 URL+文号(含复核作废链); 13 处试点史实(85 条已核实事件、31 条关系、32 条网络来源, 全部带 A-D 分级与访问日期)。
- 263 处全部获得官方认定事件(A 级); 13 处 research_status=verified, 其余 250 处诚实标注待补。

## 阶段 5 — 空间分析
- `analysis.py`: Albers 等积投影(Snyder 14-15, 往返 <1e-8°)、KDE(Silverman, PNG+WGS84 角点)、ANN(R=0.507, z=−15.31 显著聚集)、全局 Moran's I(省级 KNN k=4, z=0.43 不显著)、省界 DP 简化、批次/行业统计; 全部参数与版本入档。
- pytest 47 项(坐标/ID/地址/匹配/分类/投影/DP/ANN/Moran/KDE/数据回归/对抗边界)。

## 阶段 6 — 数据访问层
- `heritageService.ts`(纯函数数据层+懒加载缓存+筛选/搜索/统计)、`heritageLayer.ts`(三层构建+筛选编译)、`heritageStore.ts`、`export_frontend.py`(前端包+后端数据副本)。
- `LayerFilterSpec` 增加 `anyAttribute`(OR 语义, 向后兼容)。

## 阶段 7 — 前端
- 侧栏【工业遗产】面板(筛选+列表+分析), 详情抽屉(概览/故事/时间线/核心物项/关系/来源/数据质量), 双维度时间轴(形成/认定+播放), 地图点选详情, 分析图层开关。
- 17 项前端 vitest(筛选/事件/来源/图层构建/品牌断言)。

## 阶段 8 — 智能体
- `heritage_tool.py`(search/detail/timeline/stats), group 加入各 profile; 数据副本随后端分发。
- OpenRouter 真实链路冒烟: 连通 ✓ / 注册 ✓ / 模型自主 tool_call ✓(密钥仅环境变量)。

## 阶段 9 — 质量与五轮测试
- 五轮测试(详见 docs/TEST_REPORT.md §2), 修复: 侧栏白名单、条件钩子崩溃、.geojson 资产、require、Moran 零方差、SubagentRow hooks 违规。
- 历史失败清零: handlers 计数、URL schema、eslint.config.mjs 补齐。
- 终态: lint 0 错误 / tsc 0 错误 / vitest 172/172 / pytest 47/47 / build 通过 / 浏览器与 Electron 实测通过。

## 阶段 10 — 文档
- docs/: baseline_report / DATA_DICTIONARY / DATA_PROVENANCE / ARCHITECTURE / ANALYSIS_METHODS / TEST_REPORT / IMPLEMENTATION_SUMMARY(本文)。README 更新安装/启动/测试说明。
