# 数据溯源 (DATA_PROVENANCE)

## 1. 原始名单文件 (第 1—7 批国家工业遗产名单)

存放于 `data-pipeline/raw/`(工作空间原件 `工业文化遗产/` 保持只读, 双方 sha256 一致,
指纹见 `data-pipeline/manifest/raw_files.json`):

| 批次 | 文件 | 格式 | 记录数 | 公告日期(已核实) | 官方来源 |
|---|---|---|---|---|---|
| 1 | 7799881.xls | xls | 11 | 2017-12-22 | miit.gov.cn 产业函〔2017〕589号 |
| 2 | 7799405.pdf | pdf | 42 | 2018-11-21 | miit.gov.cn 产业函〔2018〕417号 |
| 3 | 7576103.pdf | pdf | 49 | 2019-12-19 | miit.gov.cn 产业函〔2019〕403号 |
| 4 | 国家工业遗产名单（第四批）.docx | docx | 62(含第二批增补1条) | 2020-12-24 | miit.gov.cn 政法函〔2020〕348号 |
| 5 | ec7698….pdf | pdf | 31 | 2021-12-13 | miit.gov.cn 政法函〔2021〕332号 |
| 6 | 90708….pdf | pdf | 37 | 2024-10-23 | miit.gov.cn 政法函〔2024〕301号 |
| 7 | e3061….pdf | pdf | 32 | 2025-10-22 | miit.gov.cn 政法函〔2025〕273号 |

发布主体均为中华人民共和国工业和信息化部, 权威等级 **A**。

## 2. 处理链 (raw → interim → processed → src/data + python-backend data)

```
raw/(原件, 只读)
 └─ parse_raw.py      字符级解析: pdf 表格线网格优先+字符聚类回退, 跨页续行/上下标/竖排文本处理
    └─ interim/batch{1..7}.json   (序号连续性+关键字段+语义校验, 264条全部干净)
 └─ fetch_admin.py    DataV GeoAtlas 行政区划(3238条, GCJ-02, 磁盘缓存)
 └─ normalize.py      主表263条: 稳定ID/查重归并/行业分类/地理编码(GCJ-02→WGS84)/质检报告
    └─ processed/heritage_sites.json + heritage_sites.geojson + sources.json
    └─ reports/{normalize,geocoding_report}.json
 └─ analysis.py       KDE/ANN/Moran/省级统计/省界简化 (参数与版本写入输出)
 └─ build_enrichment.py  试点史实+官方认定事件 → events/relations/profiles/sources
 └─ export_frontend.py   打包 src/data/heritage/* + python-backend/opengis_backend/data/heritage/*
```

所有清洗规则编码于脚本, 无任何手工 Excel 修改; 重跑脚本链可完整复现。

## 3. 联网来源分级与使用注意

- **A 级**(可直接支撑关键结论): 工信部通告原文(miit.gov.cn/gov.cn 转发页), 共7条, 均已核实 URL 与发布日期。
- **B 级**: 博物馆/学术页面(如张裕酒文化博物馆官网)。
- **C 级**: 主流媒体/百科/企业官网(新华网、人民日报转载、维基百科、企业官网等) — 用于一般史实。
- **D 级**: 百科搜索摘要等, 仅作线索, 不单独支撑关键结论。
- 采集于 2026-10-01(记录在每个来源的 accessed_at), 采集时遵守站点访问频率。
- 易失网页仅保存标题/机构/URL/访问日期与引用片段, 未做整站镜像; 链接失效时前端有降级提示。

## 4. 行政区划与边界数据

- 来源: 阿里云 DataV GeoAtlas (`geo.datav.aliyun.com/areas_v3`), 数据基础为高德行政区划(审图号 GS(2024)0650 号系数据源自带说明, 使用时请遵循其服务条款)。
- 坐标系: 原始 **GCJ-02**; 前端展示/分析前统一转换为 **WGS84**(公开近似逆变换, 城区误差约1-2米), 转换算法公开且记录于 `normalize.py`。
- 省界在导出时做 Douglas-Peucker 简化(0.008°)以控制体积, 仅供分级统计可视化, 不作为精确边界用途。

## 5. 已知数据边界(诚实声明)

- 名单本身不含始建年份/人物/故事 — 这些字段来自第4阶段采集的 57 处站点(试点 13 处: 张裕、鞍钢、旅顺船坞、永利铔厂、大生纱厂、开滦赵各庄矿、福建船政、葛洲坝、狮子滩、首钢石景山、京张制造厂、华北制药、一汽; 波次2新增 44 处, 覆盖全部第1批及第2-7批代表性遗产), 其余 206 处 enrichment_status=not_started, 档案明确显示"资料待补"。
- "培城区"(绵阳, 实为涪城区)、"新丘区"(阜新, 实为新邱区)等源文件笔误以模糊匹配纠正并全部标记 needs_review。
- 中核四〇四厂源地址仅写"甘肃省", 采用省级中心点并标记复核 — 未用城市中心点冒充。
- 名单为行政区划级地址, 区县中心点是该数据可诚实达到的最高精度; 精确点位需后续实地采集。
