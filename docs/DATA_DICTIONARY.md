# 数据字典 (DATA_DICTIONARY)
 第二十八轮补入十堰46厂博物馆项目、模具/车轮/泵业资料线索，补强44厂具体物项并登记100处不可移动/300项可移动普查规模。
公开数据版本: `v1.1.0` ｜ 公开范围: `湖北省` ｜ 生成脚本: `data-pipeline/scripts/` ｜ 更新: 2026-10-02

所有字段语义以本文件为准。任何字段不允许"编造填充"——缺失即为空, 并由质量字段标注。

## 1. heritage_sites (主表, 一遗产一行)

公开产品主表：前端包 `src/data/heritage/{sites,details}.json`。`data-pipeline/processed/heritage_sites.json` 仍保留全国处理结果，导出时按省份切片。

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

认定事件由 `build_enrichment.py` 依据批次公告统一生成(A级来源, 日期精确到日)；公开湖北包包含 13 处遗产的 41 条事件。

## 3. heritage_relations (关系表)

relation_id / source_entity(=heritage_id) / relation_type(技术援助、设备来源国、企业谱系、合并重组、国家计划、隶属、关联工程等) / target_entity / description / source_ids / **inferred**(推测性关系为 true, 与事实关系区分)。

## 4. heritage_profiles (可阅读档案)

由事件+主表字段**程序化生成**(`build_enrichment.py`), 每段内嵌 `［source_id］` 引用, 保证可溯源:

overview(一句话定位) / origin_story / development_story / transformation_story / recognition_story / people / period_tags / research_status(`verified`｜`insufficient_sources`) / note。

**无史实的遗产 research_status=insufficient_sources, 历史档案保持空白并在 UI 明示"当前数据库尚无足够已核实史料"。**文化档案另见 §5.1，不能用文化解释替代历史事实。

## 5.1 cultural_profiles (工业文化档案)

`src/data/heritage/cultural.json` 与后端同名文件一处遗产一条记录。它把官方认定层与文化研究层分开：

| 字段 | 语义 |
|---|---|
| cultural_status | `documented`=已有事件/公开来源支持；`baseline`=完成官方核心物项的文化载体解释，但关键维度仍待补证 |
| carrier_types | 建筑、设备、产品、档案、遗址、景观等文化载体类型 |
| cultural_dimensions | `technology`、`organization`、`memory`、`continuity` 四类文化维度，含 text、evidence_type、evidence_level、source_ids |
| actors / organizations | 有来源的人物、组织及其角色；来源不足时为空 |
| social_memory_status / current_use_status | `documented` 或 `pending`，明确社会记忆及保护利用证据是否存在 |
| limitations | 当前资料边界和下一步补证任务 |

`official_core_item_interpretation` 表示从官方核心物项做出的研究解释，不能当作原始史实；`research_gap` 表示待补证，不得在 Agent 回答中写成已发生事实。

## 5.2 hubei_inventory (全省扩展底册)

`src/data/heritage/inventory.json` 和后端同名文件保存国家工业遗产主表之外的湖北对象。当前包含377条（353条来源确认、24条来源线索）：除湖北省级2025年度拟认定、武汉市首批市级、黄石市首批市级名录外，还纳入省级文保名录、2025年第九批省保、湖北第一批和第二批革命文物名录中的生产性旧址、天门历史建筑、三线建设、央企/行业遗产、古代窑业与矿冶遗址、茶道/码头/水运/航空工业文化景观、盐运路线、传统茶园、茶叶洋行、工业金融节点、药业—化工—汽水—制冰企业谱系、石油装备和酿酒档案、地方工业记忆与规划资料；第二十一轮补入天门供销/码头/商号/搬运/水塔/老图书馆等历史建筑、鄂州原市麻纺厂规划片区、神农架开发建设声像档案并补强仙桃、潜江、黄冈和神农架工业文化证据；第二十二轮新增潜江油田职业技术学校旧址、盐化工业园区工业文化景观、广华职工社区与油地融合公共空间、潜江市石油化工厂历史谱系并登记仙桃/潜江四普覆盖依据；第二十三轮新增十堰原东风59厂、62厂、6264厂、房县恒达/华球纺织厂、原东风54厂片区和东风小康一工厂旧厂房；第二十四轮新增仙桃原第三服装厂旧厂房、三伏潭无纺布厂区、大垸子—沙湖泵站老旧水利设施群、蒲纺一中旧厂房改建教学楼、二三四八工业文化展览馆和柏墩生甡川砖茶厂清代老厂房；第二十五轮新增神农架伐木时代木材运输路、随州老火车站和黄冈地区缫丝厂历史谱系线索；第二十六轮新增2250kV/9000kVA工频试验成套装置、青山热电厂1号汽轮机转子、青山热电厂首台发电机铭牌、葛洲坝水利枢纽、武钢一号高炉和航天066导弹基地的“共和国印记”实物与保护利用案例文化景观，并补强老虎洞水电站和大冶铁矿群的国家专题案例来源；前二十轮对象继续保留。底册第一轮目标下限为170条，当前已超过该下限，依据公开学术报告中的多部门、多层级数据库规模。记录保留认定层级和研究状态，研究候选不等同于正式认定。新增文化载体记录还提供来源约束的物质载体、技术记忆、社会记忆和当前利用/消失状态摘要；当前292条记录具备四项文化证据。省级摸底、管理办法征求意见稿和鄂州/十堰四普调查报道登记在 `research_targets.coverage_sources`，只用于范围和字段依据，不替代对象认定证据。 第二十七轮新增黄冈城市更新工业对象、补强随州塑料三厂来源并校正神农架林业历史馆来源元数据。 第二十八轮补入十堰46厂博物馆项目、模具/车轮/泵业资料线索，补强44厂具体物项并登记100处不可移动/300项可移动汽车工业文化遗产普查规模；第二十九轮补入随州缫丝厂区—缫丝社区工业文化景观。

| 字段 | 语义 |
|---|---|
| inventory_id | `HBI-` 开头的稳定扩展底册 ID |
| name / aliases | 名录名称及检索别名；别名只用于检索，不改变正式名称 |
| city / district_county | 地市和区县；未核实的行政区保留为空 |
| industry_category_l1 | 名录或来源语境下的暂定行业；不替代主表分类审计 |
| recognition_level / recognition_status | 国家/省/市/县/研究层级与“拟认定”等原始状态；拟认定不写成已认定 |
| record_status | `source_confirmed` 表示名称和名录归属有来源，不表示文化档案已完成 |
| geocode_status | 当前均为 `pending`，完成地址/坐标核验后才进入主地图点位 |
| related_heritage_ids | 与国家主表遗产的组成、重叠或谱系关系 |
| related_inventory_ids | 与底册中另一条对象的组成或工程关系；仅在来源明确时填写 |
| source_ids | 外键 → `sources`；每条记录至少一个名录/普查来源 |
| cultural_evidence | 可选的四项来源约束文化证据：`material_carriers`、`technical_memory`、`social_memory`、`current_use_or_loss`；不代表文化档案已完成 |
| notes | 资料边界、去重关系和下一步补证任务 |

底册与13处国家名录主表分层，避免把线索或地方名录对象伪装成国家认定对象；Agent 通过 `heritage_data(action='inventory')` 查询。

第三十轮补入阳新县浮屠镇老铝厂、山下工业园、麻纺厂，神农架木鱼林场断江坪伐木队工业文化景观，省档案馆1965—1966年安陆、松滋、公安县、襄阳、枣阳、黄陂、随县工业设施题名线索，并补强黄石东钢和湖北省拖拉机厂来源；第三十一轮为随州缫丝厂补入1965、1967、1972、1978年省档案馆连续题名，新增沙市三厂、湖北省柴油机厂、湖北空压机厂、郧县风动工具厂、宜都矿山机械厂档案线索，并补强随州油泵/长江配件/齿轮厂与黄石拖拉机厂档案来源；第三十二轮以硚口区政府工业史、武汉文史资料和十堰三线建设论文升级湖北省柴油机厂、武汉柴油机厂和郧县柳陂风动工具厂的历史沿革、地点或技术证据；第三十三轮补入襄阳湖北空压机厂生活区第三方POI地址线索和宜都矿山机械厂枝城名称沿革交叉来源；第三十四轮补强汉川马口省汽修老厂房/3509厂区、荆门金龙泉啤酒厂旧址和工人文化宫的活化利用与工业文化证据；第三十五轮新增罗田县大河岸缫丝厂和英山县湖北制丝针织厂两个县域来源线索；第三十六轮补强沙市荧光灯厂旧厂区长港路苏式厂房、两根烟囱和保存状态证据；第三十七轮新增京山市原机械厂生活区工业文化景观和荆州机床厂历史名单线索，第三十八轮补全京山机械厂生活区常用检索别名；第四十轮补强京山轻工机械厂技术与组织沿革、沙市第一机床厂老厂门和摇臂钻床生产记忆；第四十一轮新增蕲春县湖北链条厂历史企业与漕河镇改制线索；第四十二轮补强沙市机床一厂/三厂、钻床和空气压缩机专业化协作生产谱系；档案题名对象统一保留 `source_lead` 和待核边界。

第四十三轮新增湖北第三内燃机配件厂档案与工业文化谱系，以湖北工业大学档案馆官方全宗登记1970—2012年企业和机械总厂档案；同时补入华中工学院机械厂与实习工厂工业文化景观，武汉市政协文史资料记录五车间、机床、水泵、工人培养和校办生产；档案对象与原厂房、设备和实体空间保持分层，具体开放、产权和物项边界继续待核。

## 5. 地理编码与坐标系统

- 地址匹配: 名单地址 → 省/市/区县文本 → DataV GeoAtlas 行政区划中心点(原始 **GCJ-02**)。
- 匹配质量 `geocode_quality`: `exact`(255处, 区县精确) / `fuzzy`(2处, 源文件笔误纠正, 如"培城区→涪城区", 带复核标记) / `city_fallback`(7处, 历史辖区或开发区无区县) / `province_fallback`(1处, 源地址仅"甘肃省")。
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

## 7. 分析结果 (公开包 `src/data/heritage/analysis/`)

kde_raster.png + kde_meta.json(带宽/网格/CRS/角点) ｜ ann_stats.json ｜ moran_stats.json ｜
province_stats.json ｜ province_boundaries.(geo)json(GCJ-02→WGS84+DP简化) ｜ batch_stats.json ｜
analysis_results.json(数据版本/算法版本/参数/时间, 默认重跑 `analysis.py` 生成湖北结果；全国分析仅用于内部追溯)。湖北只有一个省级单元，因此 Moran's I 输出为“不适用”。

## 8. 复核(review)状态说明

工信部复核机制: 第6批通知(2024-10-23)同时公布通过复核的第1、2批名单并宣布原通告作废; 第7批通知(2025-10-22)含第3批复核结果。主表以 `initial_batch` 保留首次认定批次, 复核信息保存在 sources 的 notes 与认定事件的 disputed 字段中。
