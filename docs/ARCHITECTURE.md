# 架构 (ARCHITECTURE)

本产品 = **OpenGIS 原架构**(未破坏) + **工业文化遗产数据与功能层**(新增)。

```
┌────────────────────────── Electron 30 ───────────────────────────┐
│ main (electron/)  loading窗口 + 主窗口 + PythonManager + fs IPC   │
│ preload (contextBridge: electronAPI)                              │
│ renderer (src/)                                                   │
│  ├─ OpenGIS 原有: MainLayout / MapView(MapEngine单例+MapLibre)     │
│  │   LayerPanel / ChatView / AssetExplorer / LayoutComposer …     │
│  ├─ ★ 新增 features/heritage/                                     │
│  │   HeritagePanel(侧栏: 筛选+列表+分析)                           │
│  │   HeritageDetailPanel(详情抽屉: 7 Tab)                          │
│  │   HeritageTemporalBar(形成/认定双维度时间轴)                     │
│  │   heritageBootstrap(图层装载/筛选同步/点选详情)                  │
│  │   heritageAssets(资产绑定)                                      │
│  ├─ ★ 新增 services/heritage/(types+数据访问层+图层构建)            │
│  ├─ ★ 新增 stores/heritageStore.ts(面板/筛选/选中状态)             │
│  └─ ★ 内置数据包 src/data/heritage/(sites/details/events/          │
│       relations/profiles/sources/analysis/)                        │
└──────────────┬────────────────────────────────────────────────────┘
               │ WebSocket JSON-RPC
┌──────────────┴────────────────────────────────────────────────────┐
│ python-backend (FastAPI + litellm Agent)                           │
│  ├─ 原有: AgentLoop / tools/builtin/*(自动发现) / operations       │
│  ├─ ★ 新增 tools/builtin/heritage_tool.py                          │
│  │   action=search/detail/timeline/stats — LLM 可直接查询本地数据集 │
│  └─ ★ data/heritage/(随应用分发的数据副本)                          │
└────────────────────────────────────────────────────────────────────┘
               ▲
               │ 离线脚本链 (Python, 只读原件)
data-pipeline/: raw → interim → processed → (analysis) → 前端/后端数据包
```

## 关键设计决策

1. **图层走原生管道**: 遗产点(categorized by 行业)、省级统计(graduated)、KDE(image 栅格)均为标准 `MapLayerDefinition` 进 mapStore, 由 MapEngine 渲染器插件渲染 —— 与用户手载图层完全同权, 自动获得显隐/过滤/identify/图例/导出能力。
2. **筛选 = 样式过滤**: 面板筛选编译为 `LayerFilterSpec`(扩展了 `anyAttribute` OR 语义, 向后兼容)作用于地图; 列表与统计用同一 `HeritageFilters` 经 `filterSites()` 计算 —— 地图与统计永不脱节。
3. **首屏最小化**: sites.json(精简字段)随首包; details.json 在首次打开详情时懒加载并缓存。
4. **数据访问层纯函数化**(heritageService): 全部可 vitest 直测, UI 仅消费。
5. **研究数据底线**: 档案由事件程序化生成并内嵌来源引用; 无史实的遗产显示"资料待补"而不生成内容; 推测关系标 inferred; 冲突年份标 disputed。
6. **品牌**: 用户可见文案统一【工业文化遗产GIS智能体】(i18n 两棵树), 内部包名/协议标识/许可证保持上游原样。

## 新增文件清单

前端: `src/services/heritage/{types,heritageService,heritageLayer}.ts`、`src/stores/heritageStore.ts`、`src/features/heritage/{HeritagePanel,HeritageDetailPanel,HeritageTemporalBar,heritageBootstrap,heritageAssets}`、`src/data/heritage/**`
后端: `python-backend/opengis_backend/tools/builtin/heritage_tool.py`、`opengis_backend/data/heritage/**`
改动: `MapView.tsx`(挂载 bootstrap+抽屉+时间轴)、`MainLayout.tsx`(侧栏白名单+case)、`Sidebar.tsx`(图标)、`i18n/{en,zh}.ts`(heritage 段)、`geo/types.ts`(LayerFilterSpec.anyAttribute)、`styleExpressions.ts`(编译)、`electron-builder.yml`(产品名)、品牌文案(见 CHANGELOG)。
数据: `data-pipeline/**`(原件只读副本+脚本+interim+processed+reports+tests)。
