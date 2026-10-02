# 实施摘要 / CHANGELOG

分支 `feature/industrial-heritage-gis`(基于上游 main dbe7027) ｜ 最终审计日期 2026-10-02

> 本文保留从全国数据基线到湖北发布包的实施过程。阶段 0—10 中的全国数量和中间测试数字是历史记录；最终公开产品以“阶段 11 — 湖北发布交付”及 `docs/TEST_REPORT.md` 为准。

## 阶段 0 — 基线
- 原仓库保持只读; 完整复制为 `IndustrialHeritageGIS`(含 .git)。
- 基线: typecheck ✓ / build ✓ / vitest 153/155(2 个历史失败) / lint 不可用(缺配置)。
- 记录于 `docs/baseline_report.md`。

## 阶段 1 — 品牌
- 用户可见文案统一【工业文化遗产GIS智能体】: 浏览器标题、loading 页、地图徽标、聊天头部、alt 文本、i18n 空态、菜单、脚本运行器默认头、工作流版本提示、GeoTIFF 提示、electron-builder 产品名(制品名保持 ASCII)。
- 保留: 开源许可证、MIT 声明、内部包名 `opengis`、协议标识(`com.opengis.desktop`、`OPENGIS_*`、`.opengis/` 工作区目录)。

## 阶段 2 — 数据管线
- `parse_raw.py`: xls/pdf/docx 通用解析。要点: 表格线网格优先+字符聚类回退、序号锚定行、跨页续行归并、上下标/中西文混排行聚类、表头词精确匹配、语义校验(265 条全干净, 序号连续, 关键字段零缺失)。
- `fetch_admin.py`: DataV 行政区划索引(3238 条, GCJ-02)。
- `normalize.py`: 265 条主表（原始记录经跨批重复处理后的当前结果）, 稳定 ID, 查重报告, 行业规则 v1(覆盖率 100%, 关键词依据入库), 核心物项五类映射, GCJ-02→WGS84 地理编码(253 精确+2 模糊+7 城市回退+1 省回退+0 失败), 质检三报告。
- `docs/baseline_report.md` 记录数据基线指标。

## 阶段 3/4 — 数据模型与史实采集
- `build_enrichment.py`: 事件/关系/档案/来源模型; 档案程序化生成可溯源。
- 3 个研究代理并行采集: 7 批公告日期精确到日+官方 URL+文号(含复核作废链); 13 处试点史实(85 条已核实事件、31 条关系、32 条网络来源, 全部带 A-D 分级与访问日期)。
- 265 处全部获得官方认定事件(A 级); 波次2增量采集后 57 处 research_status=verified(第1批全覆盖+第2-7批代表站点), 其余 208 处诚实标注待补。

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
- 中间阶段门禁: lint 0 错误 / tsc 0 错误 / vitest 172/172 / pytest 47/47 / build 通过 / 浏览器与 Electron 实测通过；最终湖北发布包门禁见阶段 11。

## 阶段 10 — 文档
- docs/: baseline_report / DATA_DICTIONARY / DATA_PROVENANCE / ARCHITECTURE / ANALYSIS_METHODS / TEST_REPORT / IMPLEMENTATION_SUMMARY(本文)。README 更新安装/启动/测试说明。

## 数据增量 (发布后持续更新)

- 仓库已发布: https://github.com/TZUKWAN/IndustrialHeritageGIS (公开, MIT)。
- 波次 2 史实采集(44 处): F/B/C/A/D/E/G 七组全部入库 — 事件 349→670, 关系 31→144, 网络来源 32→242, 已核实站点 13→57。
- 修正一次 ID 映射错误(汉阳铁厂史料曾误挂菱湖丝厂 ID, 已纠正并重跑管线)。
- 每批次增量: build_enrichment.py → export_frontend.py → pytest → commit → push main+feature。

## 阶段 11 — 湖北发布交付（最终公开口径）

- 公开范围冻结为湖北省 13 处国家工业遗产；全国 265 条主表和中间处理结果继续保留在 `data-pipeline/`，只用于追溯与重新切片。
- 新增独立工业文化档案层 `hubei_cultural_profiles.json` / `cultural.json`：13 处全部有文化载体、技术/技艺、人物/组织、社会记忆、保护利用和来源边界字段；其中 4 处为 `documented`，8 处为 `baseline`，待补证内容显式标记，不冒充已核实史实。
- 当前发布包: 13 处、41 条事件、10 条关系、276 个公开来源（原始底册286个来源键）、13 份文化档案、377 条扩展底册记录（353 条来源确认、24 条来源线索；144 条达到名录认定统计口径、292 条含四项文化证据）；前端与后端数据副本一致。
- 领域分类修正: 湖北 5133 厂→机械装备；二三四八蒲纺总厂→纺织工业；青山热电厂→电力能源，理由记录于 `classification_basis`。
- 当前门禁: 第四十三轮377条数据包已通过原始层审计、脚本幂等性、build_enrichment、analysis、湖北导出、数据管线52/52和定向导出审计；第三十一轮前端全套门禁仍有效，浏览器刷新后应显示全量底册377条。第四十三轮新增湖北第三内燃机配件厂档案与工业文化谱系、华中工学院机械厂与实习工厂工业文化景观；第四十二轮及更早波次继续保留。
