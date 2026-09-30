# 数据字典 (DATA_DICTIONARY)

数据版本: `v1.1.0` ｜ 生成脚本: `data-pipeline/scripts/` ｜ 更新: 2026-10-01

所有字段语义以本文件为准。任何字段不允许"编造填充"——缺失即为空, 并由质量字段标注。

## 1. heritage_sites (主表, 一遗产一行)

`data-pipeline/processed/heritage_sites.json` ＋ 前端包 `src/data/heritage/{sites,details}.json`

| 字段组 | 字段 | 类型 | 语义 |
|---|---|---|---|
| identity | heritage_id | string | 稳定ID `HER-` + md5(规范化名称\|省份\|首批批次)[:12], 可复现 |
| identity | name | string | 正式名称(第6/7批取"核准名称", 其余取名单"名称") |
| identity | aliases | string[] | 别名(第6/7批的"申请名称"等) |
| identity | initial_batch | int | 首次入选批次(永久, 不随后续复核变化) |
| identity | batches | int[] | 全部入选批次(含跨批增补, 如北京卫星制造厂=[2,4]) |
| identity | source_no | int | 首批名单内原始序号 |
| identity | recognition_years | int[] | 各批次工信部公布年份(精确到年的公告日期推导) |
| location | province/city/district_county | string\|null | 从名单地址解析的行政区(未经加工的文本见 address_raw) |
| location | address_raw | string | 名单原文地址(未清洗) |
| location | address_components | object | district_adcodes(行政区划编码), district_names |
| location | longitude/latitude | float\|null | **WGS84** 坐标(由 GCJ-02 中心点转换, 见 §5) |
| location | coordinate_system | string | 恒为 `WGS84`(无坐标时为 null) |
| history | founded_year | int\|null | 始建/创办年份(仅来自有来源的采集, 精度见 founded_year_precision) |
| history | production_start_year / closure_year | int\|null | 投产/停产年份(同上) |
| history | historical_period | string[] | 历史阶段标签, 枚举: 晚清近代工业/民国时期/新中国初期/一五二五时期/三线建设时期/改革开放后 |
| industry | industry_category_l1 | string | 行业一级分类(规则匹配, 见 classification_basis) |
| industry | classification_basis | object | matched_keywords[] + name_hit + basis(规则版本) |
| heritage | core_items_raw | string | 名单核心物项原文 |
| heritage | core_item_categories | string[] | 枚举: 工业建筑与构筑物/生产设备与工具/基础设施/档案文献/工业产品/工艺与技术/其他 |
| heritage | applicant_unit | string | 申报单位(第5-7批) |
| heritage | current_use | string\|null | 当前利用(有来源才填) |
| quality | geocode_* | — | 见 §5 |
| quality | needs_review | object | { geocode, classification, duplicate } 待复核标记 |
| quality | field_completeness | int | 9 个关键字段填充率(%) |
| quality | enrichment_status | string | not_started / verified (verified=已有已核实史实事件) |
| quality | data_version | string | 数据版本号 |

**认定批次 ≠ 形成年代。** founded_year 来自历史资料采集; recognition_years 来自工信部公告; 二者严格分字段。

## 2. heritage_events (事件表)

| 字段 | 语义 |
|---|---|
| event_id | `EVT-{id后12位}-{序号}` / 认定事件 `-R{批次}` |
| heritage_id | 外键 → heritage_sites |
| event_date_start / event_date_end | 起止(ISO 字符串, 允许 `1892` / `1958-06` 粒度) |
| date_precision | exact_date / year / decade / approximate / unknown |
| event_type | 创建/筹建、投产、扩建、技术引进、产品突破、战争影响、迁建、援建、合并重组、制度变化、改制、军转民、停产、搬迁、保护启动、博物馆/园区再利用、**遗产认定**、复核、其他 |
| title / description | 事实化标题与描述(≤80字) |
| related_people / related_orgs | 关联人物/机构(须有来源) |
| source_ids | 外键 → sources (≥1) |
| confidence | high / medium / low |
| disputed | true=不同来源存在冲突记载(前端显示"资料存在不同记载") |

认定事件由 `build_enrichment.py` 依据批次公告统一生成(A级来源, 日期精确到日), 全部 263 处均有。

## 3. heritage_relations (关系表)

relation_id / source_entity(=heritage_id) / relation_type(技术援助、设备来源国、企业谱系、合并重组、国家计划、隶属、关联工程等) / target_entity / description / source_ids / **inferred**(推测性关系为 true, 与事实关系区分)。

## 4. heritage_profiles (可阅读档案)

由事件+主表字段**程序化生成**(`build_enrichment.py`), 每段内嵌 `［source_id］` 引用, 保证可溯源:

overview(一句话定位) / origin_story / development_story / transformation_story / recognition_story / people / period_tags / research_status(`verified`｜`insufficient_sources`) / note。

**无史实的遗产 research_status=insufficient_sources, 档案保持空白并在 UI 明示"当前数据库尚无足够已核实史料"。**

## 5. 地理编码与坐标系统

- 地址匹配: 名单地址 → 省/市/区县文本 → DataV GeoAtlas 行政区划中心点(原始 **GCJ-02**)。
- 匹配质量 `geocode_quality`: `exact`(253处, 区县精确) / `fuzzy`(2处, 源文件笔误纠正, 如"培城区→涪城区", 带复核标记) / `city_fallback`(7处, 历史辖区或开发区无区县) / `province_fallback`(1处, 源地址仅"甘肃省")。
- `geocode_precision`: district_centroid(区县中心点) / city_centroid / province_centroid / *_multi_district(跨区县)。
- **GCJ-02 → WGS84**: 公开近似逆变换算法(城区误差约1-2米), 实现于 `normalize.py::gcj02_to_wgs84`; 原始 GCJ-02 坐标保留在 `geocode_gcj02` 字段。**绝不把 GCJ-02 直接当 WGS84 使用。**
- 分析投影: Albers 等积圆锥 (lon_0=105, lat_1=25, lat_2=47, Krassovsky 椭球), 正逆往返误差 <1e-8°。

## 6. sources (来源表)

| 字段 | 语义 |
|---|---|
| source_id | `src-batch{1..7}`(官方名单文件) / `src-web-{md5(url)[:10]}`(联网采集) |
| authority_level | **A**=政府公文/正式认定材料(工信部通告, 7条) / **B**=博物馆/学术 / **C**=主流媒体/百科/企业官网 / **D**=仅作线索 |
| url / publication_date / accessed_at | 可点击溯源 + 访问日期 |
| origin_file / sha256 | 批次文件的原始文件指纹(data-pipeline/manifest/raw_files.json) |

7 条批次来源均已核实官方 URL(miit.gov.cn / gov.cn)与公告文号(如 工信部政法函〔2024〕301号)。

## 7. 分析结果 (processed/analysis/)

kde_raster.png + kde_meta.json(带宽/网格/CRS/角点) ｜ ann_stats.json ｜ moran_stats.json ｜
province_stats.json ｜ province_boundaries.(geo)json(GCJ-02→WGS84+DP简化) ｜ batch_stats.json ｜
analysis_results.json(数据版本/算法版本/参数/时间, 重跑 `analysis.py` 可完整复现)。

## 8. 复核(review)状态说明

工信部复核机制: 第6批通知(2024-10-23)同时公布通过复核的第1、2批名单并宣布原通告作废; 第7批通知(2025-10-22)含第3批复核结果。主表以 `initial_batch` 保留首次认定批次, 复核信息保存在 sources 的 notes 与认定事件的 disputed 字段中。
