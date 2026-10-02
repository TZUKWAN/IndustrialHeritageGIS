from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "tianmen_fourth_history_buildings_2026": {
        "source_type": "municipal_government_historic_building_register",
        "title": "市人民政府关于公布天门市第四批历史建筑名单的通知",
        "org": "天门市人民政府",
        "pub_date": "2026-01-23",
        "url": "https://www.tianmen.gov.cn/zwgk/zc/qtzdgk/t_5947092.shtml",
        "authority": "A",
        "notes": "天门市政府正式公布第四批45处历史建筑及逐项简介。附件直接记载龙尾山121基地、苏氏粮仓、石家河拖车厂、石河老罐头厂、张港镇供销社、张港镇码头候船室、岳口镇电力设备厂、天门老化肥厂、吴源茂商号故居、老搬运站办公楼、黄潭镇水塔等生产、仓储、交通、能源和商贸相关对象的年代、地址、功能或沿革；本来源确认历史建筑身份，但不替代单体工业遗产认定。",
    },
    "xiantao_1979_culture_2023": {
        "source_type": "official_media_industrial_memory_report",
        "title": "留存那一抹工业记忆——仙桃杜湖街道1979街区改造记",
        "org": "湖北日报新闻客户端",
        "pub_date": "2023-02-20",
        "url": "https://news.hubeidaily.net/pc/1111888.html",
        "authority": "B",
        "notes": "湖北日报记录仙桃棉纺厂纺线梭子、红砖墙车间和居民代际记忆，并确认杜湖街道1979街区由原沔阳县砖瓦厂于1979年筹建演变而来；改造保留红砖墙体、砖瓦印记巷、棉纺岁月巷及老物件展示。来源用于工业文化与更新利用证据，不等同法定工业遗产认定。",
    },
    "qianjiang_five_seven_official_2025": {
        "source_type": "provincial_patriotic_education_base_profile",
        "title": "江汉油田五七油田会战指挥部旧址",
        "org": "红色湖北（湖北省爱国主义教育基地）",
        "pub_date": "2025-02-01",
        "url": "https://www.cnhubei.com/xwzt/2024/hshb/hshbgfjyjd/hshbagzyjyjdqj/202502/t4750545.shtml",
        "authority": "A",
        "notes": "官方基地资料确认旧址位于潜江市江汉油田五七会战路2号，始建于20世纪60年代，是1969年五七油田会战指挥部重要办公场所；2015年修缮、2023年升级，基地总面积3675平方米，2019年入选中央企业工业文化遗产、2022年列为湖北省爱国主义教育基地、2023年列为中国石化红色教育基地。",
    },
    "shennongjia_development_archive_2026": {
        "source_type": "provincial_archive_official_feature",
        "title": "‘十四五巡礼’| 红色基因铸魂 绿色档案赋能——神农架林区档案史志工作高质量发展纪实",
        "org": "湖北省档案馆/神农架林区档案馆",
        "pub_date": "2026-01-28",
        "url": "https://www.hbda.gov.cn/info/6700",
        "authority": "A",
        "notes": "湖北档案信息网报道神农架林区档案馆征集并保存记录林区开发建设的电影胶片、上世纪领导讲话原始录音磁带等特色档案，并说明馆藏数字化和开放鉴定工作；来源用于补强林业开发工业文化的档案载体，不把馆藏档案误写成独立建筑遗产。",
    },
    "huanggang_bailian_aluminum_community_2024": {
        "source_type": "official_media_industrial_community_update",
        "title": "黄州区赤壁街道铝业社区：找回居民老厂区记忆 打造老工业风社区",
        "org": "湖北日报新闻客户端",
        "pub_date": "2024-06-20",
        "url": "https://news.hubeidaily.net/mobile/c_2778269.html",
        "authority": "B",
        "notes": "湖北日报确认黄冈市黄州区铝业社区为原白莲铝业集团破产改制社区，保留红砖厂房、铝厂记忆雕塑、工业标语和11栋职工居民楼；改造中设置‘火红年代’微型博物馆、文化墙，并以铝锭、铝管、铝丝等生产元素讲述铝厂历史。",
    },
    "huanggang_bailian_aluminum_memory_2024": {
        "source_type": "official_media_industrial_memory_museum_report",
        "title": "黄州区铝业社区组织铝厂老职工参观铝厂记忆馆",
        "org": "湖北日报新闻客户端",
        "pub_date": "2024-11-18",
        "url": "https://news.hubeidaily.net/pc/c_3345730.html",
        "authority": "B",
        "notes": "湖北日报记录铝厂记忆馆以老照片、旧物件、工作服和‘峥嵘岁月’‘光辉历程’‘铝厂精神’‘老厂新生’等板块保存黄冈铝业集团历史，并组织老职工集体参观和记忆传承。",
    },
}


def ev(material: str, technical: str, social: str, current: str) -> dict[str, str]:
    return {
        "material_carriers": material,
        "technical_memory": technical,
        "social_memory": social,
        "current_use_or_loss": current,
    }


def rec(
    inventory_id: str,
    name: str,
    city: str,
    district: str | None,
    industry: str,
    level: str,
    status: str,
    source_keys: list[str],
    notes: str,
    cultural_evidence: dict[str, str],
    *,
    aliases: list[str] | None = None,
    asset_kind: str | None = None,
    related_inventory_ids: list[str] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "inventory_id": inventory_id,
        "name": name,
        "city": city,
        "district_county": district,
        "industry_category_l1": industry,
        "recognition_level": level,
        "recognition_status": status,
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": source_keys,
        "cultural_evidence": cultural_evidence,
        "notes": notes,
    }
    if aliases:
        row["aliases"] = aliases
    if asset_kind:
        row["asset_kind"] = asset_kind
    if related_inventory_ids:
        row["related_inventory_ids"] = related_inventory_ids
    return row


NEW_RECORDS: list[dict[str, Any]] = [
    rec(
        "HBI-TM-011",
        "张港镇供销社原址",
        "天门市",
        "张港镇",
        "供销商贸与农资流通",
        "municipal_historical_building",
        "天门市第四批历史建筑（2026）",
        ["tianmen_fourth_history_buildings_2026"],
        "天门市政府第四批历史建筑名单确认张港镇供销社原址始建于1983年，位于张港镇芦茯街205号，后为天门农贸总公司张港分公司，现为闲置建筑。它是乡镇集体商业、物资供应和农产品流通体系的实体节点；具体仓储、柜台和附属用房边界待测绘。",
        ev(
            "芦茯街205号供销社原址及其商业、仓储和附属空间；公开名单未提供建筑面积、结构与设备清单",
            "计划经济时期乡镇供销、农资供应和农产品收购流通组织的技术与管理记忆；具体商品谱系和仓储流程待地方志、企业档案补证",
            "张港镇居民采购、交售农副产品、供销社职工和乡镇商业网络形成的社会记忆；职工口述与票据档案待采集",
            "现为闲置建筑，已列天门市第四批历史建筑；产权、建筑保存状况、再利用和开放边界待核",
        ),
        aliases=["张港镇供销社旧址", "天门农贸总公司张港分公司旧址"],
        asset_kind="industrial_trade_site",
    ),
    rec(
        "HBI-TM-012",
        "张港镇码头候船室",
        "天门市",
        "张港镇",
        "内河交通与货运服务",
        "municipal_historical_building",
        "天门市第四批历史建筑（2026）",
        ["tianmen_fourth_history_buildings_2026"],
        "天门市政府第四批历史建筑名单确认张港镇码头候船室建于1973年，原为镇码头候船空间，现为民用住宅。它反映江汉平原水运客货集散与基层交通服务体系；码头、装卸设施和候船室原始边界待交通档案和现场核验。",
        ev(
            "1973年张港镇码头候船室建筑本体及其与码头、堤岸和装卸空间的关系；现状为民用住宅，原附属设施待查",
            "内河客运、货运候船、装卸衔接和水陆转运组织的交通工业技术记忆；船型、航线和货运档案待补",
            "沿河居民出行、农副产品水运、船工和码头服务人员形成的地方交通记忆；口述史和老照片待采集",
            "已列天门市第四批历史建筑，现转为民用住宅；公共开放、原真性和码头整体保存状态待核",
        ),
        aliases=["张港码头候船室", "张港镇老码头候船室"],
        asset_kind="industrial_transport_site",
    ),
    rec(
        "HBI-TM-013",
        "吴源茂商号故居",
        "天门市",
        "渔薪镇",
        "商贸、棉油加工与石油流通",
        "municipal_historical_building",
        "天门市第四批历史建筑（2026）",
        ["tianmen_fourth_history_buildings_2026"],
        "天门市政府名单确认吴源茂商号为吴氏家族1874年创办的商行，早期经营丝绢包头，后扩展到日杂百货、棉油加工，并经营汉江和长江口岸，与美孚石油公司合作开设光华石油公司；故居位于渔薪镇渔薪社区，建筑具有民国特色。商号经营空间、作坊和仓储附属关系待核。",
        ev(
            "渔薪镇渔薪社区吴源茂商号故居及可能保留的店铺、仓储和棉油加工空间；官方名单未给出面积和构件清单",
            "丝绢贸易、日杂百货、棉油加工、汉江长江口岸转运以及光华石油公司经营构成近代商贸工业技术网络；账簿、设备和作坊遗存待查",
            "吴氏家族商贸、地方慈善、渔薪镇商业街和跨汉江长江贸易形成的社会记忆；家族档案与社区口述史待采集",
            "列入天门市第四批历史建筑，现作为历史建筑与地方人文记忆载体；商号原功能、产权和展示利用方式待核",
        ),
        aliases=["吴源茂商号旧址", "吴源茂故居", "光华石油公司渔薪关联旧址"],
        asset_kind="industrial_trade_site",
    ),
    rec(
        "HBI-TM-014",
        "老搬运站办公楼",
        "天门市",
        "竟陵街道",
        "货运搬运与仓储服务",
        "municipal_historical_building",
        "天门市第四批历史建筑（2026）",
        ["tianmen_fourth_history_buildings_2026"],
        "天门市政府名单将义河北街35号对面的老搬运站办公楼列入第四批历史建筑，记载其为建国初期两层砖混建筑，墙面刻有‘为人民服务’字样。该对象是城市货运搬运、仓储调度和工人组织的服务设施；原搬运站作业场地与附属仓库待核。",
        ev(
            "义河北街35号对面老搬运站两层办公楼及其可能关联的装卸、仓储和调度空间；公开资料未列附属物项",
            "建国初期城市货运搬运、车辆调度、货物装卸和仓储管理的基础设施记忆；搬运工具、车队和业务档案待补",
            "搬运工、码头与街区商贸、城市居民收发货物形成的劳动记忆；工会和老职工口述史待采集",
            "列入天门市第四批历史建筑，建筑主体保存信息有限；原搬运站范围、产权、利用和开放状态待现场核验",
        ),
        aliases=["天门老搬运站办公楼", "义河北街搬运站旧址"],
        asset_kind="industrial_transport_site",
    ),
    rec(
        "HBI-TM-015",
        "黄潭镇水塔",
        "天门市",
        "黄潭镇",
        "城镇供水基础设施",
        "municipal_historical_building",
        "天门市第四批历史建筑（2026）",
        ["tianmen_fourth_history_buildings_2026"],
        "天门市政府名单确认黄潭镇水塔建于1973年，曾承担周边居民日常供水并成为地方景观。水塔作为公共供水设施，补充表达乡镇工业化和生活基础设施文化；水塔高度、泵房、管网和运行单位待水务档案核验。",
        ev(
            "1973年黄潭镇水塔塔体及可能关联的泵房、蓄水和供水管网；官方名单未给出工程尺寸和设备清单",
            "乡镇集中供水、蓄水调压、水泵运行和管网维护的基础设施技术记忆；设计图纸和运行台账待补",
            "居民日常取水、公共卫生和乡镇建设记忆；水务职工与社区口述资料待采集",
            "列入天门市第四批历史建筑，持续使用或停用状态、结构安全和开放方式待核",
        ),
        aliases=["黄潭老水塔", "黄潭镇供水水塔"],
        asset_kind="industrial_utility_site",
    ),
    rec(
        "HBI-TM-016",
        "石河老供销社",
        "天门市",
        "石家河镇",
        "供销商贸与乡镇物资供应",
        "municipal_historical_building",
        "天门市第四批历史建筑（2026）",
        ["tianmen_fourth_history_buildings_2026"],
        "天门市政府名单确认石河老供销社建于1955年，位于石家河镇马溪老街，是服务周边村民采购和物资供应的集体所有制商贸场所。它反映计划经济时代乡村商业与农业物资流通；原门市、仓储和办公空间待测绘。",
        ev(
            "石家河镇马溪老街石河老供销社建筑及门市、仓储和办公空间；公开名单未提供面积与构件目录",
            "乡村供销、农资配送、农副产品收购和集体商业经营的技术与管理记忆；商品、票证和仓储档案待补",
            "村民采购、交售和供销社职工形成的乡村商业记忆；老职工口述与地方商业史待采集",
            "列入天门市第四批历史建筑，建筑保存和利用状态需与相邻石河老图书馆、老罐头厂分开核验",
        ),
        aliases=["石河老供销社旧址", "石家河镇老供销社"],
        asset_kind="industrial_trade_site",
    ),
    rec(
        "HBI-TM-017",
        "石河老图书馆（原供销社门市部）",
        "天门市",
        "石家河镇",
        "商贸服务与基层文化供应",
        "municipal_historical_building",
        "天门市第四批历史建筑（2026）",
        ["tianmen_fourth_history_buildings_2026"],
        "天门市政府名单确认石河老图书馆位于石家河镇马溪老街2号，原为石河供销社的杂货图书门市部，曾同时承担商品供应和基层文化服务。该对象连接乡镇商贸与公共文化传播，需补建筑与供销社空间关系、书籍/商品清单及现状。",
        ev(
            "马溪老街2号原供销社杂货图书门市部建筑及其门市空间；公开资料未给出面积、结构与设备清单",
            "乡镇供销门市、图书零售和基层文化物资供应的复合服务网络；经营账册、书籍目录和供销档案待补",
            "村民购书、消费和供销社服务形成的乡镇公共文化记忆；居民口述与地方出版物档案待采集",
            "列入天门市第四批历史建筑；原门市功能已改变，保护边界、产权和开放方式待核",
        ),
        aliases=["石河老图书馆旧址", "石河供销社杂货图书门市部"],
        asset_kind="industrial_trade_site",
    ),
    rec(
        "HBI-TM-018",
        "干驿镇老式建筑（原供销商店）",
        "天门市",
        "干驿镇",
        "供销商贸与基层物资供应",
        "municipal_historical_building",
        "天门市第四批历史建筑（2026）",
        ["tianmen_fourth_history_buildings_2026"],
        "天门市政府名单确认干驿镇中和村一组老式建筑建于1964年，为文革前期供销商店所建，占地约300平方米，保存较好。该对象补充乡镇基层商业建筑与计划经济物资供应网络；原商品、仓储和经营单位档案待核。",
        ev(
            "干驿镇中和村一组1964年供销商店建筑，占地约300平方米；建筑结构、货柜和仓储附属空间待测绘",
            "供销商店零售、农资供应和村级物资分配的基层商业技术记忆；商品票证和经营档案待补",
            "村民日常采购、供销社职工和乡村集体商业形成的社会记忆；社区口述史待采集",
            "列入天门市第四批历史建筑，公开名单称保存较好；产权、使用和开放状态待现场核验",
        ),
        aliases=["干驿镇供销商店旧址", "中和村供销商店"],
        asset_kind="industrial_trade_site",
    ),
    rec(
        "HBI-EZ-029",
        "鄂州市原市麻纺厂片区",
        "鄂州市",
        "鄂城区",
        "纺织与麻纺加工",
        "city_planning",
        "鄂州市‘十五五’规划列入城市更新对象；尚未见独立工业遗产认定",
        ["ezhou_15th_plan_2026"],
        "鄂州市政府‘十五五’规划将原市麻纺厂片区列入城市更新及地产综合开发相关部署。规划材料能够确认其作为历史工业片区的城市更新对象，但未公开厂址边界、建筑清单、设备保存和法定工业遗产级别，故按规划线索单独建档并保持待核。",
        ev(
            "原鄂州市麻纺厂片区的厂房、仓库、生活区或设备遗存尚未由规划网页逐项公开，需四普、规划图则和现场测绘核验",
            "麻纺原料处理、纺纱织造、动力与厂区物流的工业技术记忆目前仅由企业类型推断，工艺和设备不得视为已证实",
            "鄂州纺织工人、厂区社区和城市工业化记忆待地方志、厂志、档案与口述史补证",
            "已进入市级规划的城市更新及地产综合开发语境；保护对象、拆改影响、权属和活化利用尚待专项调查",
        ),
        aliases=["原鄂城市麻纺厂", "鄂州麻纺厂旧厂区", "市麻纺厂片区"],
        asset_kind="industrial_landscape",
    ),
    rec(
        "HBI-SNJ-003",
        "神农架林区开发建设电影胶片与林业生产录音档案",
        "神农架林区",
        None,
        "林业开发与木材生产档案",
        "documentary_heritage",
        "神农架林区档案馆特色馆藏线索；未见独立工业遗产认定",
        ["shennongjia_development_archive_2026", "shennongjia_forestry_history_2025"],
        "湖北档案信息网确认神农架林区档案馆征集保存记录林区开发建设的电影胶片、上世纪领导讲话原始录音磁带等特色档案；国家林草局资料补充20世纪60年代林业生产、木材外运和停伐转型背景。本条把可验证的开发建设档案作为工业文化载体记录，不把档案载体误写为实体厂址。",
        ev(
            "神农架林区档案馆收藏的林区开发建设电影胶片、林业生产与领导讲话原始录音磁带及相关全宗；具体档号和开放目录待查",
            "木材采伐、山地运输、林场组织和天然林停伐转型的声像记录，为林业工业技术史提供一手载体；设备谱系待档案编目补证",
            "林业工人、林场社区、进山建设和生态转型的集体记忆通过影像和录音保存；档案馆数字化和编研工作提供代际传播渠道",
            "档案馆已开展征集、数字化和开放鉴定工作；具体开放权限、复制规则和关联旧林场实体清单待核",
        ),
        aliases=["神农架开发建设声像档案", "神农架林业工业文化档案"],
        asset_kind="documentary_heritage",
    ),
]


PATCHES: dict[str, dict[str, Any]] = {
    "HBI-TM-001": {
        "source_keys": ["tianmen_fourth_history_buildings_2026"],
        "aliases": ["龙尾山121基地", "江汉石油管理局第三机械厂天门基地"],
        "evidence": ev(
            "皂市镇龙尾山社区121基地生产区、生活区、供电供水设施及大体量职工社区；官方名单记载生活区109栋单元楼、生产区和划拨土地，钻采设备与厂房清单待核",
            "中石化江汉石油管理局第三机械厂1969年建立，承担石油钻采机械及配套生产记忆；具体产品、设备和车间沿革待厂志补证",
            "石油机械职工、三线/油田建设、职工社区和资产移交形成的天门地方工业记忆；职工口述与企业档案待采集",
            "2021年资产移交天门市政府并由市国投集团接管，列入天门市第四批历史建筑；生产区、生活区改造和保护边界待核",
        ),
        "notes": "天门市政府第四批历史建筑名单确认龙尾山121基地即中石化江汉石油管理局第三机械厂，1969年建立，包含生产区、生活区、供电供水设施和大体量职工社区；2021年资产移交天门市政府。工业设备、厂房编号和保护边界仍需专项测绘。",
    },
    "HBI-TM-002": {
        "source_keys": ["tianmen_fourth_history_buildings_2026"],
        "aliases": ["多宝镇苏氏粮仓", "苏氏粮仓旧址"],
        "evidence": ev(
            "多宝镇关庙街苏氏粮仓建筑及仓内原建格局、粮食储运空间；仓门、通风、计量和装卸设施待测绘",
            "1955年按原苏联设计图纸建造的粮食仓储、通风防潮和基层粮管所管理技术记忆；设备档案待补",
            "农村交公粮、粮管所职工和国家粮食储备体系形成的地方社会记忆；交粮户与仓储人员口述史待采集",
            "列入天门市第四批历史建筑，官方称内部仍保持原建容貌；产权、开放和结构安全待核",
        ),
        "notes": "天门市政府第四批历史建筑名单确认苏氏粮仓1955年按原苏联设计图纸建造，为多宝镇原粮管所储粮仓库，内部仍保持原建容貌；仓储设备和现状使用待补。",
    },
    "HBI-TM-003": {
        "source_keys": ["tianmen_fourth_history_buildings_2026"],
        "aliases": ["多宝原杂粮仓", "多宝镇杂粮仓旧址"],
        "evidence": ev(
            "多宝镇关庙街1960年砖木结构杂粮仓及其粮食进出、堆存和装卸空间；构件、仓门和附属设施待测绘",
            "基层粮管所杂粮分类、储存、通风和调运的仓储技术记忆；粮种、容量和运行档案待补",
            "多宝镇居民交粮、粮站职工和乡村粮食供应形成的社会记忆；口述史待采集",
            "列入天门市第四批历史建筑，官方称保存较完整；产权、利用和安全状态待核",
        ),
        "notes": "天门市政府第四批历史建筑名单确认多宝原杂粮仓建于1960年，为保存较完整的砖木结构粮仓；具体仓储流程、附属设备和现状待核。",
    },
    "HBI-TM-004": {
        "source_keys": ["tianmen_fourth_history_buildings_2026"],
        "aliases": ["刘方岭村粮仓旧址", "石家河刘方岭粮仓"],
        "evidence": ev(
            "石家河镇刘方岭村七组两座1976年粮仓及其储粮、通风和装卸空间；仓体构件和附属设施待测绘",
            "农村公粮储存、粮仓管理、计量和区域调运的基层粮食技术记忆；粮站台账待补",
            "周边村庄交公粮、粮仓职工和集体农业生产形成的乡土记忆；村民口述史待采集",
            "列入天门市第四批历史建筑；建筑保存、使用和保护边界待核",
        ),
        "notes": "天门市政府第四批历史建筑名单确认刘方岭村粮仓建于1976年，由两座粮仓组成，承担周边区域粮食存储；仓体和设备现状待专项调查。",
    },
    "HBI-TM-005": {
        "source_keys": ["tianmen_fourth_history_buildings_2026"],
        "aliases": ["吴刘粮管所旧址", "石家河吴刘粮站"],
        "evidence": ev(
            "石家河镇吴刘村三组1963年吴刘粮管所建筑及粮食收纳、储存空间；粮仓、办公和计量设施待核",
            "建国初期基层粮食收纳、储存、计量和调运管理技术；粮食流通档案和仓储设备待补",
            "农村交公粮、粮管所职工和周边村庄粮食供应形成的社会记忆；口述史待采集",
            "列入天门市第四批历史建筑；建筑保存、产权、使用和开放状态待核",
        ),
        "notes": "天门市政府第四批历史建筑名单确认吴刘粮管所建于1963年，承担周边区域粮食收纳、存储，是农村交公粮时代的重要场所；具体建筑和粮食流通档案待补。",
    },
    "HBI-TM-006": {
        "source_keys": ["tianmen_fourth_history_buildings_2026"],
        "aliases": ["石家河拖车厂", "天门农机修造七厂旧址", "石家河农用拖车厂"],
        "evidence": ev(
            "石家河镇石家河村一组拖车厂六个生产车间和办公楼；官方名单确认生产空间数量，设备、厂界和生活配套待测绘",
            "前身天门农机修造七厂，1980年改为拖车厂，开展农用拖车设计、焊接、装配和维修；产品型号与设备档案待补",
            "乡镇农机服务、农用拖车使用者、企业职工和农业机械化形成的地方工业记忆；口述史待采集",
            "列入天门市第四批历史建筑，官方称改制后仍正常经营；生产空间保存、产权和开放边界待核",
        ),
        "notes": "天门市政府第四批历史建筑名单确认石家河拖车厂始建于20世纪70年代，前身为天门农机修造七厂，1980年改为拖车厂，含六个生产车间和办公楼；设备与厂界待补。",
    },
    "HBI-TM-007": {
        "source_keys": ["tianmen_fourth_history_buildings_2026"],
        "aliases": ["石河老罐头厂", "石家河罐头食品厂旧址"],
        "evidence": ev(
            "石家河镇马溪街石河老罐头厂厂房及原石河供销社办公空间；车间、锅炉、灌装和仓储设施待测绘",
            "由老供销社转为规模较大罐头食品加工厂的食品加工、包装和供应链技术记忆；产品、设备和工艺档案待补",
            "乡镇食品供应、罐头工人和地方消费形成的工业社会记忆；老职工口述史待采集",
            "列入天门市第四批历史建筑，原厂房保存、功能改变和保护边界待核",
        ),
        "notes": "天门市政府第四批历史建筑名单确认石河老罐头厂建于1970年，由石河老供销社办公楼转为规模较大的罐头食品加工厂；生产车间、产品与现状待补。",
    },
    "HBI-TM-008": {
        "source_keys": ["tianmen_fourth_history_buildings_2026"],
        "aliases": ["岳口镇电力设备厂", "岳口火力发电厂旧址"],
        "evidence": ev(
            "岳口镇粮仓巷村电力设备厂及其约7.3万平方米用地、约4.8万平方米建筑空间；机组、厂房和输配电设施清单待测绘",
            "1958年兴办火力发电厂、1963年正式投运供电并沿革为电力设备厂，体现乡镇电力生产、设备制造和供电组织技术记忆；机组档案待补",
            "岳口居民用电、发电厂职工和地方工业化形成的公共记忆；电力工人和社区口述史待采集",
            "列入天门市第四批历史建筑；现有厂房、设备保存与再利用状态待核",
        ),
        "notes": "天门市政府第四批历史建筑名单确认岳口镇电力设备厂1958年10月兴办火力发电厂，1963年9月正式投运供电，占地7.3万平方米、建筑面积4.8万平方米；机组和后续沿革待补。",
    },
    "HBI-TM-009": {
        "source_keys": ["tianmen_fourth_history_buildings_2026"],
        "aliases": ["天门农药一厂旧址", "岳口老化肥厂"],
        "evidence": ev(
            "岳口镇黄家滩村天门老化肥厂及约1.5万平方米用地、约4307平方米建筑空间；反应装置、仓库和污染治理设施待核",
            "1966年兴办天门农药一厂，后形成化肥/农化生产沿革；原料、合成、包装和环保工艺不能由名单推定，需厂志与环境档案补证",
            "岳口农化工人、农业投入品供应和地方工业化形成的社会记忆；职工口述与环境治理档案待采集",
            "列入天门市第四批历史建筑；现存厂房、设备、环境风险和再利用状态待专项核验",
        ),
        "notes": "天门市政府第四批历史建筑名单确认天门老化肥厂1966年兴办天门农药一厂，位于岳口镇黄家滩村，占地约1.5万平方米、建筑面积约4307平方米；工艺、设备和环境风险待核。",
    },
    "HBI-XT-001": {
        "source_keys": ["xiantao_1979_culture_2023"],
        "aliases": ["仙桃棉纺厂旧厂区", "杜湖街道棉纺岁月巷"],
        "evidence": ev(
            "仙桃棉纺厂纺线梭子、红砖墙车间及1979街区保留的工业物件和展示空间；原厂区边界、厂房编号和设备目录待核",
            "棉纺纺线、车间组织和纺织工人生产技术记忆由梭子与红砖车间线索承载；工艺档案和机器型号待补",
            "棉纺厂职工、居民社区和仙桃工业化代际记忆在棉纺岁月巷中被展示；口述史待规范采集",
            "1979街区更新保留红砖墙、老物件和棉纺岁月巷，形成公共工业记忆空间；原厂区保护边界与产权待核",
        ),
        "notes": "湖北日报2023年报道确认仙桃棉纺厂纺线梭子、红砖墙车间是杜湖街道工业记忆，并在1979街区改造中设置棉纺岁月巷；原厂区边界和设备清单待补。",
    },
    "HBI-XT-002": {
        "source_keys": ["xiantao_1979_culture_2023"],
        "aliases": ["原沔阳县砖瓦厂旧址", "1979老商业街", "杜湖街道1979街区"],
        "evidence": ev(
            "原沔阳县砖瓦厂1979年筹建形成的街区空间、红砖墙体和砖瓦印记巷；砖窑、厂房和生产边界待档案与现场核验",
            "砖瓦生产、建材供应和街区建设关系形成的工业技术记忆；窑炉、设备和产品档案待补",
            "原砖瓦厂职工、居民社区和老商业街代际生活记忆通过改造展示延续；居民口述史待采集",
            "1979街区完成旧改，保留红砖墙体、砖瓦印记巷和老物件展示；原厂遗存比例与保护责任待核",
        ),
        "notes": "湖北日报确认1979街区由原沔阳县砖瓦厂于1979年筹建并演变而来，更新中保留红砖墙体和砖瓦印记巷；原砖瓦厂窑炉、厂房与街区遗产边界待核。",
    },
    "HBI-QJ-002": {
        "source_keys": ["qianjiang_five_seven_official_2025"],
        "aliases": ["五七油田会战指挥部旧址", "江汉油田五七会战指挥部旧址", "五七会战指挥部作战室"],
        "evidence": ev(
            "潜江市江汉油田五七会战路2号指挥部旧址、室内展馆和室外公园，总面积3675平方米；旧址核心办公建筑面积、构件和关联油田设施清单待测绘",
            "20世纪60年代建设、1969年五七油田会战指挥和江汉石油大会战的勘探、钻采、组织调度与能源保障技术记忆；档案目录待补",
            "12万石油工人、转业军人和江汉油田职工共同会战的社会记忆，展陈以‘逐梦千万吨’和能源安全叙事持续传播",
            "2015年修缮、2023年升级为红色教育基地；2019年入选中央企业工业文化遗产、2022年列湖北省爱国主义教育基地、2023年列中石化红色教育基地，公开开放时间已给出，日常保护责任待核",
        ),
        "notes": "官方爱国主义教育基地资料确认五七油田会战指挥部旧址地址、20世纪60年代始建、1969年指挥功能、2015年修缮和2023年升级，并明确2019年中央企业工业文化遗产、2022年湖北省爱国主义教育基地、2023年中国石化红色教育基地身份；本条与江汉第一口油井、岩心库及油田线路保持关联。",
        "related_inventory_ids": ["HBI-QJ-001", "HBI-QJ-003", "HBI-QJ-006"],
    },
    "HBI-SNJ-001": {
        "source_keys": ["shennongjia_development_archive_2026"],
        "aliases": ["神农架林业历史馆", "神农架伐木时代工业文化遗存"],
        "evidence": ev(
            "神农架林业历史馆中的老麻绳、安全帽、刀斧锯凿等伐木生产实物，以及林区开发建设电影胶片和录音档案；馆舍与旧林场建筑清单待核",
            "20世纪60年代木材采伐、山地运输、林场组织和天然林停伐转型的技术记忆，由实物、影像和录音共同保存；设备谱系待补",
            "进山建设的林业工人、林场社区和由木材生产转向生态保护的集体记忆；档案馆编研与林业历史馆展陈提供传播渠道",
            "林业历史馆承担实物展示，神农架档案馆开展开发建设档案征集、数字化和开放鉴定；旧林场边界、馆藏档号和复制权限待核",
        ),
        "notes": "国家林草局报道确认神农架林业历史馆保存伐木时代老麻绳、安全帽、刀斧锯凿等实物；湖北档案信息网进一步确认林区档案馆保存开发建设电影胶片和原始录音磁带。该条继续按林业工业文化景观与馆藏层级表达，不升级为独立工业遗产认定。",
    },
    "HBI-HG-002": {
        "source_keys": ["huanggang_bailian_aluminum_community_2024", "huanggang_bailian_aluminum_memory_2024"],
        "aliases": ["白莲铝业集团旧厂区", "黄州铝业社区", "铝厂记忆馆"],
        "evidence": ev(
            "黄州区赤壁街道铝业社区原白莲铝业集团红砖厂房、11栋职工居民楼、铝厂记忆雕塑、文化墙和微型记忆馆；完整原厂区边界与设备清单待核",
            "白莲铝业主要生产铝锭和铝电线，铝锭、铝管、铝丝、生产机械模型和车间物件保留铝业生产技术记忆；设备谱系待补",
            "破产改制后的老职工、职工社区和铝厂由兴到衰的集体记忆通过老照片、旧物件、工作服和老职工参观活动持续传承",
            "社区更新保留红砖厂房并改为文体活动中心，设置‘火红年代’微型博物馆和铝厂记忆馆；原生产区保护边界、产权和开放制度待核",
        ),
        "notes": "湖北日报两篇报道确认铝业社区为原白莲铝业集团破产改制社区，保留红砖厂房、工业标语、铝厂记忆雕塑和11栋职工居民楼，并以铝锭/铝管/铝丝、生产机械模型、老照片、旧物件和工作服构建记忆馆与社区更新场景；本条按工业社区与文化载体表达，不等同法定工业遗产认定。",
    },
}


def merge_unique(row: dict[str, Any], key: str, values: list[str]) -> None:
    existing = row.setdefault(key, [])
    for value in values:
        if value not in existing:
            existing.append(value)


def patch_record(row: dict[str, Any], patch: dict[str, Any]) -> None:
    merge_unique(row, "source_keys", patch["source_keys"])
    merge_unique(row, "aliases", patch.get("aliases", []))
    row["cultural_evidence"] = patch["evidence"]
    row["notes"] = patch["notes"]
    row["record_status"] = "source_confirmed"
    if patch.get("related_inventory_ids"):
        merge_unique(row, "related_inventory_ids", patch["related_inventory_ids"])


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    existing_by_id = {row["inventory_id"]: row for row in records}
    for new_row in NEW_RECORDS:
        old = existing_by_id.get(new_row["inventory_id"])
        if old is None:
            records.append(new_row)
            existing_by_id[new_row["inventory_id"]] = new_row
        elif old != new_row:
            raise SystemExit(f"conflicting duplicate record: {new_row['inventory_id']}")
    for key, value in NEW_SOURCES.items():
        if key in sources and sources[key] != value:
            raise SystemExit(f"conflicting source: {key}")
        sources[key] = value
    if "ezhou_15th_plan_2026" in sources:
        sources["ezhou_15th_plan_2026"]["notes"] = (
            "市政府规划部署西雷山工业遗址文化传承与焕新工程，提出利用鄂钢、老水泥厂策划工业文化观光、研学和体验产品，并将原市麻纺厂片区列入城市更新及地产综合开发相关部署；本来源支持规划层对象，不替代单体工业遗产认定。"
        )
    for inventory_id, patch in PATCHES.items():
        row = existing_by_id.get(inventory_id)
        if row is None:
            raise SystemExit(f"update target missing: {inventory_id}")
        patch_record(row, patch)
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_u_sources={len(NEW_SOURCES)} added_records={len(NEW_RECORDS)} "
        f"total_records={len(records)} total_sources={len(sources)} patched_records={len(PATCHES)}"
    )


if __name__ == "__main__":
    main()
