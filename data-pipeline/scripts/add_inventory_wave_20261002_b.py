from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "huangshi_mining_group_2025": {
        "source_type": "government_page",
        "title": "大冶铁矿工业遗产群",
        "org": "黄石市人民政府/东楚网",
        "pub_date": "2025-11-20",
        "url": "https://www.huangshi.gov.cn/ztjj/zjhsgyyc/gyycditu/202511/t20251120_1281951.html",
        "authority": "A",
        "notes": "黄石市工业遗产地图逐项列出东露天采场旧址、炸药洞旧址、麻雀山碉堡旧址、厂区宿舍楼、厂房/选矿厂历史建筑、铁门坎摩崖石刻、铁山老火车站及老桥洞，并给出建造、工艺和现状信息。",
    },
    "huangshi_huaxin_2024": {
        "source_type": "official_media",
        "title": "华新历史风貌区：一座城市转型发展的缩影——“老街新韵”系列之六",
        "org": "湖北省文化和旅游厅/湖北日报",
        "pub_date": "2024-05-25",
        "url": "https://wlt.hubei.gov.cn/bmdt/mtjj/202405/t20240525_5216612.shtml",
        "authority": "A",
        "notes": "官方报道记录华新旧址36处文物建筑、湿法回转窑、车间和装车站台、332台套设备、五羊巷职工生活区礼堂/剧院/浴室等，并记录1907文化公园的展示和再利用。",
    },
    "daye_ironworks_2017": {
        "source_type": "government_page",
        "title": "旅游信息：大冶铁厂与国家工业遗产",
        "org": "大冶市人民政府",
        "pub_date": "2017-12-13",
        "url": "https://www.hbdaye.gov.cn/zjdy/dyly/lyxx/201712/t20171213_529608.html",
        "authority": "A",
        "notes": "大冶市政府页面确认汉冶萍公司—大冶铁厂国家工业遗产身份、1921年高炉残基、瞭望塔、水塔、栈桥、日式/欧式建筑和钢轨等核心物项。",
    },
    "hubei_archival_heritage_2025": {
        "source_type": "government_news",
        "title": "第三批湖北省档案文献遗产名录公布",
        "org": "湖北省文化和旅游厅/湖北日报",
        "pub_date": "2025-06-05",
        "url": "https://wlt.hubei.gov.cn/bmdt/xydt/202506/t20250605_5679902.shtml",
        "authority": "A",
        "notes": "官方报道列出民国华新水泥股份有限公司档案、湖北应城石膏股份有限公司档案、荆江分洪档案，并确认汉冶萍档案等7项入选中国档案文献遗产。",
    },
    "hanyeping_archives_national": {
        "source_type": "government_register",
        "title": "中国档案文献遗产名录：汉冶萍煤铁厂矿有限公司档案",
        "org": "国家档案局",
        "pub_date": None,
        "url": "https://www.saac.gov.cn/mowcn/cn/c100395/jyml_6.shtml",
        "authority": "A",
        "notes": "国家档案局名录将汉冶萍煤铁厂矿有限公司档案列入中国档案文献遗产，时间范围1899—1948；记录为工业文化档案载体，不等同于厂址实体保护认定。",
    },
    "hubei_archives_first_2019": {
        "source_type": "government_register",
        "title": "湖北省档案文献遗产名录（首批）",
        "org": "湖北省档案馆",
        "pub_date": None,
        "url": "https://www.hbda.gov.cn/info/3131.jspx",
        "authority": "A",
        "notes": "湖北省档案馆首批省级档案文献遗产名录页面；名录资料包含汉冶萍档案、华中钢铁公司档案、宜都茶厂文书档案等工业档案对象。",
    },
    "jingzhou_yangmatou_2024": {
        "source_type": "official_media",
        "title": "沙市洋码头：漫步两公里 穿越近百年——“老街新韵”系列之二",
        "org": "湖北省文化和旅游厅/湖北日报",
        "pub_date": "2024-05-21",
        "url": "https://wlt.hubei.gov.cn/bmdt/mtjj/202405/t20240521_5198187.shtml",
        "authority": "A",
        "notes": "官方报道确认1927年沙市打包厂、50余处老建筑、约2.3万平方米厂区、原料罐/烟囱和活力28老厂房工业成就展，并记录文创园保护性改造和市民工业记忆。",
    },
    "wuhan_606_2024": {
        "source_type": "government_news",
        "title": "“工业锈带”蝶变“产业秀带”——武钢老厂房重生记",
        "org": "湖北省经济和信息化厅/湖北日报",
        "pub_date": "2024-02-20",
        "url": "https://jxt.hubei.gov.cn/bmdt/cyfz/202402/t20240220_5088665.shtml",
        "authority": "A",
        "notes": "官方报道确认武钢云谷·606产业园原为1954年始建的武汉冶金设备制造厂，保留水塔、龙门吊、红砖厂房和原热处理/钻具/下料车间，已改造为产业园。",
    },
    "wuhan_simei_2026": {
        "source_type": "government_news",
        "title": "百年交通线成城市风景线，铁路工业遗存成文化公园",
        "org": "武汉市人民政府/长江日报",
        "pub_date": "2026-01-30",
        "url": "https://www.wuhan.gov.cn/whyw/gqdt/202601/t20260130_2721887.shtml",
        "authority": "A",
        "notes": "官方报道确认四美塘铁路遗址文化公园保留老铁轨、龙门吊、红砖厂房和武昌北站/徐家棚站记忆，并记录原中铁重工武北厂区、武昌机务段的铁路工业背景。",
    },
    "wuhan_guishan_2026": {
        "source_type": "government_news",
        "title": "《人民日报》聚焦武汉：着力推进工业旧址改造更新，老旧厂房焕发新活力",
        "org": "武汉市人民政府/人民日报",
        "pub_date": "2026-06-15",
        "url": "https://www.wuhan.gov.cn/sy/kwh/202606/t20260615_2777225.shtml",
        "authority": "A",
        "notes": "官方转载明确华中小龟山金融文化公园由20世纪70年代中国电建湖北电力工程公司设备生产基地改造而来，并记录其现状产业导入。",
    },
    "wuhan_old_sites_2026": {
        "source_type": "government_news",
        "title": "《人民日报》聚焦武汉：着力推进工业旧址改造更新，老旧厂房焕发新活力",
        "org": "武汉市人民政府/人民日报",
        "pub_date": "2026-06-15",
        "url": "https://www.wuhan.gov.cn/sy/kwh/202606/t20260615_2777225.shtml",
        "authority": "A",
        "notes": "同一官方报道明确硚口汉江湾人工智能产业园由柴油机厂和床单厂旧址改造而来；记录为成片更新对象，具体原厂边界仍需专项普查。",
    },
    "suizhou_industrial_history_2024": {
        "source_type": "official_media",
        "title": "随州工业发展史：老工业企业与城市转型报道",
        "org": "随州日报",
        "pub_date": "2024-09-30",
        "url": "https://szrb.suiw.cn/szrb/20240930/html/content_20240930002001.htm",
        "authority": "B",
        "notes": "随州日报报道记载湖北油泵油嘴厂、武汉长江配件厂北郊拖车车间、齿轮厂、插秧机厂、气刹厂、机床厂、避雷器厂等企业在随州落地并推动城市工业化；具体旧址边界需档案和实测复核。",
    },
    "suizhou_arrester_address_2024": {
        "source_type": "property_page",
        "title": "聚玉街358号原避雷器厂地址线索",
        "org": "随州房产信息网",
        "pub_date": None,
        "url": "https://m.szfcol.com/zf/8524.shtml",
        "authority": "C",
        "notes": "第三方房产信息页面将聚玉街358号标注为原避雷器厂，仅作地址线索，不能替代官方名录、档案或现场核验。",
    },
    "yidu_tea_archives_2021": {
        "source_type": "government_archive",
        "title": "宜都茶厂档案",
        "org": "湖北省档案馆",
        "pub_date": "2021-09-23",
        "url": "https://www.hbda.gov.cn/info/3544",
        "authority": "A",
        "notes": "湖北省档案馆确认宜都茶厂档案形成于1950—1987年、现藏宜都市档案馆，共232卷，包含生产建设、规章制度、会议记录、花名册和工资表等。",
    },
    "yidu_3line_archives_2023": {
        "source_type": "official_media",
        "title": "宜都三线建设档案入选湖北省档案文献遗产名录",
        "org": "湖北省档案馆/荆楚网",
        "pub_date": "2023-03-14",
        "url": "https://yc.cnhubei.com/content/2023-03/14/content_15571810.html",
        "authority": "B",
        "notes": "公开报道确认宜都三线建设档案进入省级档案文献遗产名录，重点涉及焦枝铁路宜都县民兵师报纸卷；具体全宗范围需向档案馆目录核验。",
    },
}


def rec(
    inventory_id: str,
    name: str,
    city: str,
    industry: str,
    level: str,
    status: str,
    source_keys: list[str],
    notes: str,
    cultural_evidence: dict[str, str],
    *,
    district: str | None = None,
    aliases: list[str] | None = None,
    asset_kind: str | None = None,
    record_status: str = "source_confirmed",
    related_heritage_ids: list[str] | None = None,
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
        "record_status": record_status,
        "geocode_status": "pending",
        "source_keys": source_keys,
        "cultural_evidence": cultural_evidence,
        "notes": notes,
    }
    if aliases:
        row["aliases"] = aliases
    if asset_kind:
        row["asset_kind"] = asset_kind
    if related_heritage_ids:
        row["related_heritage_ids"] = related_heritage_ids
    if related_inventory_ids:
        row["related_inventory_ids"] = related_inventory_ids
    return row


def component_evidence(material: str, technical: str, social: str, current: str) -> dict[str, str]:
    return {
        "material_carriers": material,
        "technical_memory": technical,
        "social_memory": social,
        "current_use_or_loss": current,
    }


NEW_RECORDS: list[dict[str, Any]] = [
    rec("HBI-HS-020", "大冶铁矿东露天采场旧址", "黄石市", "采掘冶金工业", "provincial_relic_related", "第六批湖北省文物保护单位；大冶铁矿工业遗产群组成项", ["huangshi_mining_group_2025"], "官方工业遗产地图确认东露天采场由象鼻山、狮子山、尖山三个矿体组成，2014年公布为第六批省级文物保护单位；单列为大冶铁矿工业遗产群组成项，不表示新增独立国家工业遗产认定。", component_evidence("东露天采场、象鼻山/狮子山/尖山矿体、采场边坡和矿坑空间", "近代机械化露天采矿、矿体开采和矿石运输技术", "矿工劳动、矿山城市和黄石采掘工业记忆", "官方称为国家矿山公园组成内容；开放线路、产权和安全边界待管理方复核"), district="铁山区", asset_kind="heritage_component", related_inventory_ids=["HBI-HS-005"]),
    rec("HBI-HS-021", "大冶铁矿炸药洞旧址", "黄石市", "采掘冶金工业", "municipal_related", "大冶铁矿工业遗产群组成项", ["huangshi_mining_group_2025"], "官方工业遗产地图记录炸药洞20世纪初作为炸药和备件储存空间，抗战时期由日铁使用，1955年重建后继续作为库房至20世纪末；现以组成项入库。", component_evidence("炸药洞洞室、库房和备件储存空间", "露天矿山爆破物资储存与采矿保障系统", "矿工、库房管理和战争时期矿山经历的地方记忆", "官方称其为大冶铁矿工业遗产群内容，洞室现状和开放条件待现场核验"), district="铁山区", asset_kind="heritage_component", related_inventory_ids=["HBI-HS-005"]),
    rec("HBI-HS-022", "大冶铁矿麻雀山碉堡旧址", "黄石市", "采掘冶金工业", "municipal_related", "大冶铁矿工业遗产群组成项", ["huangshi_mining_group_2025"], "官方工业遗产地图记录碉堡由日铁时期修建，保留射击孔、砖墙和汉冶萍厂徽/官厂印记，并已纳入保护范围；作为工业—战争复合记忆组成项入库。", component_evidence("圆形碉堡、射击孔、砖墙、厂徽或官厂印记、水泥墩柱", "矿山警戒、防护和工业设施安全管理", "汉冶萍、日铁矿山经营和地方战争记忆", "官方称已纳入保护范围并为国家矿山公园组成内容；维护状况待复核"), district="铁山区", asset_kind="heritage_component", related_inventory_ids=["HBI-HS-005"]),
    rec("HBI-HS-023", "大冶铁矿厂区宿舍楼", "黄石市", "采掘冶金工业社区", "municipal_related", "大冶铁矿工业遗产群组成项", ["huangshi_mining_group_2025"], "官方工业遗产地图将厂区宿舍楼列为大冶铁矿工业遗产群组成项；单列用于补足矿山职工居住、社区和日常生活文化证据，具体楼栋编号待核。", component_evidence("矿山厂区宿舍楼、职工居住空间和社区公共设施（楼栋清单待核）", "矿山生产—居住—服务一体化组织", "矿工家庭、邻里和铁山矿区社区记忆", "遗产群现状保护、产权和可进入范围待地方档案与现场核验"), district="铁山区", asset_kind="heritage_component", related_inventory_ids=["HBI-HS-005"]),
    rec("HBI-HS-024", "大冶铁矿选矿厂历史建筑群", "黄石市", "选矿工业", "municipal_related", "大冶铁矿工业遗产群组成项", ["huangshi_mining_group_2025"], "官方工业遗产地图明确选矿厂1957年开工、1958年一期投产，保留破碎、选别、脱水流程和主厂房、浮选设备等历史建筑；生产状态以官方页面为准。", component_evidence("选矿主厂房、破碎/选别/脱水设施、浮选大井和钢梁框架建筑", "年处理原矿、破碎—选别—脱水连续选矿工艺", "选矿工人、技术班组和黄石矿业城市记忆", "官方称历史建筑保存基本完好且选矿流程仍运行；生产安全边界与开放方式待复核"), district="铁山区", asset_kind="heritage_component", related_inventory_ids=["HBI-HS-005"]),
    rec("HBI-HS-025", "铁山老火车站及老桥洞", "黄石市", "铁路与采掘冶金工业", "municipal_related", "大冶铁矿工业遗产群组成项", ["huangshi_mining_group_2025"], "官方工业遗产地图记载1891年张之洞修建大冶铁矿至石灰窑运矿铁路，铁山老火车站及老桥洞为其后续铁路工业遗存；线路大部已不存，保留物项需测绘。", component_evidence("老火车站、老桥洞、铁路走向及相关桥涵空间", "矿石铁路运输、站场组织和机车编组", "铁路工人、矿石运输和铁山—黄石城市联系记忆", "运矿铁路现已不存，老站和桥洞现状、开放范围及保护责任待核"), district="铁山区", asset_kind="heritage_component", related_inventory_ids=["HBI-HS-005"]),
    rec("HBI-HS-026", "铁门坎摩崖石刻", "黄石市", "采掘冶金工业文化", "municipal_relic_related", "黄石市文物保护单位；大冶铁矿工业遗产群组成项", ["huangshi_mining_group_2025"], "官方工业遗产地图确认《大冶铁矿盛公纪念碑》刻于1924年，记录盛宣怀承办大冶铁矿历史，2016年公布为黄石市文物保护单位；作为工业企业人物与社会记忆载体入库。", component_evidence("摩崖石刻、题刻本体、围栏、风雨亭和怀盛园空间", "近代矿业招商、企业经营和纪念性书写", "盛宣怀、大冶铁矿和地方工业开办记忆", "官方称石刻本体保存较好并设玻璃罩、围栏和风雨亭；现状保护需继续复核"), district="铁山区", asset_kind="heritage_component", related_inventory_ids=["HBI-HS-005"]),
    rec("HBI-HS-027", "民国华新水泥股份有限公司档案", "黄石市", "水泥工业档案", "provincial_documentary_heritage", "第三批湖北省档案文献遗产", ["hubei_archival_heritage_2025"], "湖北省文化和旅游厅公布的第三批湖北省档案文献遗产明确列出民国华新水泥股份有限公司档案；本条是档案文献遗产，不新增华新厂址实体认定。", component_evidence("民国华新水泥股份有限公司形成的档案文书、生产经营和企业管理记录（卷目待档案馆核验）", "近代水泥生产、设备引进、企业经营和工程供货技术记忆", "华新工人、企业制度和黄石水泥城市记忆", "列入省级档案文献遗产；开放卷目、复制和利用条件需向收藏机构核验"), district="黄石港区", asset_kind="documentary_heritage", related_heritage_ids=["HER-0577e36e016"], related_inventory_ids=["HBI-HS-009"]),
    rec("HBI-HS-028", "汉冶萍煤铁厂矿有限公司档案", "黄石市", "近代冶金工业档案", "national_documentary_heritage", "中国档案文献遗产", ["hanyeping_archives_national"], "国家档案局名录确认汉冶萍煤铁厂矿有限公司档案为中国档案文献遗产，时间范围1899—1948；与汉阳铁厂、大冶铁厂及汉冶萍矿铁体系关联，记录为文化档案载体。", component_evidence("企业章程、往来文书、生产经营和矿铁企业管理档案（具体全宗和馆藏地待核）", "近代煤铁联合生产、企业组织、矿山与冶炼技术记忆", "汉冶萍工人、企业制度、近代工业化和区域城市记忆", "国家档案文献遗产；查阅权限、数字化程度和关联厂址索引待档案馆核验"), district="西塞山区", asset_kind="documentary_heritage", related_heritage_ids=["HER-0127dfd1ca78", "HER-3318e785a779"], related_inventory_ids=["HBI-HS-001"]),
    rec("HBI-HS-029", "华中钢铁公司档案", "黄石市", "钢铁工业档案", "provincial_documentary_heritage", "湖北省档案文献遗产（首批）", ["hubei_archives_first_2019"], "湖北省档案馆首批省级档案文献遗产页面列出华中钢铁公司档案；企业全宗范围、年代和馆藏地需以省档案馆目录核验。", component_evidence("华中钢铁公司企业档案、生产建设和管理文书（卷目待核）", "钢铁生产组织、设备运行和企业技术管理记忆", "钢铁工人、厂区社区和黄石工业城市记忆", "省级档案文献遗产；公开利用范围和数字化状态待档案馆核验"), district="黄石市", asset_kind="documentary_heritage"),
    rec("HBI-HS-030", "华新水泥厂五羊巷职工生活区（组成项）", "黄石市", "水泥工业社区文化", "municipal_related", "华新水泥厂旧址工业文化组成项", ["huangshi_huaxin_2024"], "湖北省文化和旅游厅报道确认五羊巷曾是华新水泥厂职工生活区，保留礼堂、剧院、浴室等48处文物建筑；单列为国家工业遗产相关的职工社区组成项。", component_evidence("职工生活区、礼堂、剧院、浴室及48处文物建筑", "工厂生产—居住—文化服务一体化组织", "职工家庭、文艺活动、公共浴室和黄石工人社区记忆", "报道记载修旧如旧并建设湖北美术学院协同创新示范基地；实际开放与产权待核"), district="黄石港区", asset_kind="heritage_component", related_heritage_ids=["HER-0577e36e016"], related_inventory_ids=["HBI-HS-009"]),
    rec("HBI-HS-031", "华新水泥厂湿法回转窑与装车站台（组成项）", "黄石市", "水泥工业", "national_cultural_relic_related", "第三批国家工业遗产华新水泥厂旧址组成项", ["huangshi_huaxin_2024"], "官方报道确认1、2号湿法回转窑、华新型3号窑及新/老装车站台原地保留并承担展示、展演和公共文化功能；单列为技术载体组成项。", component_evidence("1—3号湿法回转窑、装车站台、铁轨、火车头和相关生产设备", "水泥湿法回转窑烧成、装运和完整生产流程", "水泥工人、国家重点工程供货和黄石工业记忆", "旧址已转为华新历史风貌区/华新1907文化公园，具体设备保护清单待管理方核验"), district="黄石港区", asset_kind="heritage_component", related_heritage_ids=["HER-0577e36e016"], related_inventory_ids=["HBI-HS-009"]),
    rec("HBI-HS-032", "汉冶萍公司—大冶铁厂核心物项（1921年高炉等）", "黄石市", "冶金工业", "national_cultural_relic_related", "第一批国家工业遗产汉冶萍公司—大冶铁厂核心物项", ["daye_ironworks_2017"], "大冶市政府页面逐项记载1921年冶炼高炉残基、瞭望塔、水塔、高炉栈桥、日式建筑4栋、欧式建筑1栋和钢轨；本条是核心物项集合，不新增独立名录对象。", component_evidence("1921年高炉残基、瞭望塔、水塔、高炉栈桥、日式/欧式建筑和钢轨", "近代高炉炼铁、厂区供水、物料输送和工业建筑技术", "汉冶萍、大冶铁厂和黄石近代冶金工业记忆", "国家工业遗产核心物项；具体保存点、开放范围和管理主体待现场/管理资料核验"), district="西塞山区", asset_kind="heritage_component", related_heritage_ids=["HER-0127dfd1ca78"], related_inventory_ids=["HBI-HS-001"]),
    rec("HBI-JZ-006", "荆江分洪档案", "荆州市", "水利工程档案", "provincial_documentary_heritage", "第三批湖北省档案文献遗产", ["hubei_archival_heritage_2025"], "湖北省文化和旅游厅报道将荆江分洪档案列入第三批湖北省档案文献遗产；与荆江分洪闸工程实体和防洪技术体系关联。", component_evidence("工程档案、设计施工文件、运行管理记录和影像资料（全宗范围待核）", "分洪工程规划、施工、调度和防洪技术", "荆江治理、工程建设者和长江防洪公共记忆", "列入省级档案文献遗产；查阅范围和数字化状态待档案馆核验"), district="沙市区", asset_kind="documentary_heritage", related_inventory_ids=["HBI-JZ-005"]),
    rec("HBI-JZ-007", "沙市洋码头老码头与老厂房工业文化街区", "荆州市", "港口与轻工业文化景观", "city_planning", "来源确认的工业文化景观与城市更新对象", ["jingzhou_yangmatou_2024"], "官方报道确认洋码头约2公里岸线、1927年打包厂、50余处老建筑和活力28老厂房等组成连续的码头—仓储—轻工业文化景观；本条为街区尺度对象，不等同单体文保认定。", component_evidence("老码头、打包厂、候船室、老厂房、原料罐、烟囱和滨江岸线", "港口装卸、棉花打包、日化生产和沿江物流组织", "沙市商埠、码头工人、活力28品牌和轻工业城市记忆", "已改造为洋码头文创园，兼具文化展示、创意工坊和旅游休闲；具体保护单元清单待核"), district="沙市区", asset_kind="industrial_cultural_landscape", related_inventory_ids=["HBI-JZ-001", "HBI-JZ-004"]),
    rec("HBI-WUHAN-031", "武钢云谷·606产业园（原武汉冶金设备制造厂）", "武汉市", "冶金装备制造工业", "city_planning", "来源确认的老厂房更新对象", ["wuhan_606_2024"], "省经信厅官方报道确认606产业园原为1954年始建的武汉冶金设备制造厂，保留水塔、龙门吊、红砖建筑及热处理/钻具/下料车间，已完成首发区改造；不写成正式市级或省级名录认定。", component_evidence("水塔、龙门吊、红砖厂房、原热处理车间、钻具车间和下料车间", "冶金设备制造、热处理、钻具加工和大型厂区生产组织", "武钢子公司职工、厂区社区和武汉钢铁工业记忆", "原厂区已更新为606产业园，官方报道确认首发区13座建筑改造；整体边界、开放和保护责任待核"), district="洪山区", asset_kind="industrial_cultural_landscape"),
    rec("HBI-WUHAN-032", "四美塘铁路遗址文化公园（武昌北站/徐家棚站及机修车间段）", "武汉市", "铁路运输与机车检修工业", "city_planning", "来源确认的铁路工业文化公园对象", ["wuhan_simei_2026"], "武汉市政府/长江日报报道确认四美塘铁路遗址文化公园保留武昌北站（原徐家棚站）、老铁轨、龙门吊、红砖厂房和武昌机务段/中铁重工武北厂区记忆；作为公园整体对象入库。", component_evidence("武昌北站站场、老铁轨、蒸汽机车、龙门吊、红砖厂房和机修空间", "粤汉铁路终点站、机车检修、编组和铁路装卸技术", "铁路工人、徐家棚社区和武汉近现代交通工业记忆", "已更新为四美塘铁路遗址文化公园，保留部分工业遗存并开放公共活动；保护单元清单待核"), district="武昌区", asset_kind="industrial_cultural_landscape"),
    rec("HBI-WUHAN-033", "华中小龟山金融文化公园（原中国电建湖北电力工程公司设备生产基地）", "武汉市", "电力设备制造工业", "city_planning", "来源确认的老厂房更新对象", ["wuhan_guishan_2026"], "武汉市政府转载人民日报报道确认小龟山金融文化公园由20世纪70年代中国电建湖北电力工程公司设备生产基地改造而来；作为工业旧址更新对象入库，不新增名录认定。", component_evidence("20世纪70年代设备生产基地厂房与园区空间（现存建筑清单待核）", "电力工程设备制造、生产基地组织和工业厂区技术记忆", "电力建设职工、武昌城市更新和设备制造工业记忆", "现为金融文化公园并有上百家企业入驻；原厂房保存比例、具体建筑和展示文本待核"), district="武昌区", asset_kind="industrial_cultural_landscape"),
    rec("HBI-WUHAN-034", "汉江湾人工智能产业园（原柴油机厂、床单厂旧址）", "武汉市", "机械制造与纺织工业文化景观", "city_planning", "来源确认的成片工业旧址更新对象", ["wuhan_old_sites_2026"], "武汉市政府转载人民日报报道明确汉江湾人工智能产业园由原柴油机厂和床单厂旧址改造而来，现入驻高科技和文创企业；厂区边界和原企业谱系待专项普查。", component_evidence("柴油机厂、床单厂原厂区建筑和生产空间（具体单体待普查）", "柴油机制造、纺织生产和老城区工业空间转换", "硚口工人、老企业社区和汉江湾工业城市记忆", "已更新为人工智能产业园，报道确认产业导入；遗存保留比例和可展示对象待现场核验"), district="硚口区", asset_kind="industrial_cultural_landscape"),
    rec("HBI-SZ-003", "湖北油泵油嘴厂旧址候选", "随州市", "汽车零部件工业", "research_candidate", "随州工业史报道确认的历史企业线索（待实地核验）", ["suizhou_industrial_history_2024"], "随州日报报道将湖北油泵油嘴厂列为落地随州并推动工业化的企业；本条记录企业历史线索，具体厂址、建筑和设备不写成已确认遗产。", component_evidence("原厂房、设备和厂区空间待档案/实测核验", "油泵油嘴制造及汽车零部件配套技术", "随州工人、汽车配件产业和城市工业化记忆", "企业旧址现状、拆改和再利用状态待官方档案与现场核验"), district="随州市", asset_kind="industrial_site", record_status="source_confirmed"),
    rec("HBI-SZ-004", "武汉长江配件厂北郊拖车车间旧址候选", "随州市", "汽车配件与机械工业", "research_candidate", "随州工业史报道确认的历史车间线索（待实地核验）", ["suizhou_industrial_history_2024"], "随州日报报道记载武汉长江配件厂北郊拖车车间曾落地随州；车间具体地址、建筑遗存和企业沿革需档案核验。", component_evidence("拖车车间、厂房和机械设备待核", "拖车/汽车配件制造、维修和机械加工", "工人迁入、配件产业和随州工业城市记忆", "旧址保存、搬迁和现状用途待官方档案及现场核验"), district="随州市", asset_kind="industrial_site"),
    rec("HBI-SZ-005", "湖北齿轮厂旧址候选", "随州市", "齿轮制造工业", "research_candidate", "随州工业史报道确认的历史企业线索（待实地核验）", ["suizhou_industrial_history_2024"], "随州日报报道将齿轮厂列为随州工业化时期的重要企业；具体企业全称、厂址和现存物项需地方志、厂志与现场核验。", component_evidence("齿轮厂房、机床和量具待核", "齿轮加工、热处理和机械传动配套技术", "齿轮工人、技能培训和随州机械工业记忆", "遗址是否保留、改造或消失待核"), district="随州市", asset_kind="industrial_site"),
    rec("HBI-SZ-006", "随县插秧机厂旧址候选", "随州市", "农业机械工业", "research_candidate", "随州工业史报道确认的历史企业线索（待实地核验）", ["suizhou_industrial_history_2024"], "随州日报报道将插秧机厂列为随州工业化时期的企业；具体厂址、产品谱系和遗存边界待地方档案与现场核验。", component_evidence("插秧机生产厂房、模具和装配设备待核", "插秧机设计、铸造/机加工和农业机械装配", "农机工人、农业机械推广和县域工业记忆", "旧址和设备现状待核"), district="随县", asset_kind="industrial_site"),
    rec("HBI-SZ-007", "湖北气刹厂旧址候选", "随州市", "汽车制动器工业", "research_candidate", "随州工业史报道确认的历史企业线索（待实地核验）", ["suizhou_industrial_history_2024"], "随州日报报道将气刹厂列为随州工业化时期企业；企业正式名称、厂址和遗存现状待地方志、企业档案与实地核验。", component_evidence("气刹生产车间、试验设备和厂区建筑待核", "汽车气压制动器制造和检验技术", "汽车配件工人、技能传承和随州机械工业记忆", "旧址保存、拆改和再利用状态待核"), district="随州市", asset_kind="industrial_site"),
    rec("HBI-SZ-008", "随州机床厂旧址候选", "随州市", "机床制造工业", "research_candidate", "随州工业史报道确认的历史企业线索（待实地核验）", ["suizhou_industrial_history_2024"], "随州日报报道将机床厂列为随州工业化时期企业；具体厂址、机床谱系、工人社区和现存建筑待地方档案与现场核验。", component_evidence("机床厂房、机床设备、量具和动力设施待核", "机床制造、机械加工和工业装备配套", "机床工人、技术学校和随州装备制造记忆", "旧址及设备现状待核"), district="随州市", asset_kind="industrial_site"),
    rec("HBI-SZ-009", "随州避雷器厂旧址候选（聚玉街358号线索）", "随州市", "电力器材工业", "research_candidate", "第三方地址线索与随州工业史报道对应的候选（待官方核验）", ["suizhou_industrial_history_2024", "suizhou_arrester_address_2024"], "随州日报记载避雷器厂曾落地随州；第三方房产页面将聚玉街358号标注为原避雷器厂。地址与企业对应关系尚未由官方档案或现场核定，保持线索级状态。", component_evidence("聚玉街358号原厂房线索，建筑和设备待核", "避雷器制造、绝缘/电力器材生产技术待档案补证", "避雷器厂职工、城市供电和电力工业记忆", "仅有第三方地址线索，现状、产权和可见遗存必须现场核验"), district="曾都区", asset_kind="industrial_site", record_status="source_lead"),
    rec("HBI-XG-004", "湖北应城石膏股份有限公司档案", "孝感市", "石膏矿业与建材工业档案", "provincial_documentary_heritage", "第三批湖北省档案文献遗产", ["hubei_archival_heritage_2025"], "湖北省文化和旅游厅报道明确将湖北应城石膏股份有限公司档案列入第三批湖北省档案文献遗产；与应城石膏矿工业遗产实体形成档案—遗址关联。", component_evidence("公司档案、采矿/加工/经营文书和企业管理记录（全宗范围待核）", "石膏开采、加工、运输和建材企业管理技术记忆", "矿工、应城石膏产业和地方资源型工业记忆", "列入省级档案文献遗产；馆藏、开放和数字化状态待档案馆核验"), district="应城市", asset_kind="documentary_heritage", related_inventory_ids=["HBI-XG-001"]),
    rec("HBI-YC-010", "宜都茶厂档案", "宜昌市", "茶叶加工工业档案", "provincial_documentary_heritage", "湖北省档案馆珍档资料；宜都茶厂档案", ["yidu_tea_archives_2021"], "湖北省档案馆确认宜都茶厂档案形成于1950—1987年、共232卷，记录从建厂到转型的历史进程；与省级工业遗产拟认定对象宜都红茶厂形成档案关联。", component_evidence("232卷宜都茶厂档案、规章制度、计划总结、生产建设、会议记录、花名册和工资表", "宜红茶收购、精制、出口和企业生产组织", "茶厂职工、宜红茶产区和宜都地方工业记忆", "现藏宜都市档案馆；查档、复制和开放范围需按档案馆规定核验"), district="宜都市", asset_kind="documentary_heritage", related_inventory_ids=["HBI-PROV-002"]),
    rec("HBI-YC-011", "宜都三线建设档案", "宜昌市", "铁路与三线建设档案", "provincial_documentary_heritage", "湖北省档案文献遗产线索", ["yidu_3line_archives_2023"], "公开报道确认宜都三线建设档案进入湖北省档案文献遗产名录，重点涉及焦枝铁路宜都县民兵师报纸卷；全宗范围和与具体工程点位的对应关系待档案馆目录核验。", component_evidence("焦枝铁路宜都县民兵师报纸卷及相关三线建设档案（全宗待核）", "铁路建设、民兵组织和三线工程施工技术记忆", "宜都三线建设者、铁路沿线社区和地方现代化记忆", "列入省级档案文献遗产线索；公开查阅范围和数字化状态待核"), district="宜都市", asset_kind="documentary_heritage"),
]


UPDATES: dict[str, dict[str, Any]] = {
    "HBI-HS-001": {
        "source_keys_add": ["hanyeping_archives_national"],
        "cultural_evidence": component_evidence(
            "汉冶萍煤铁厂矿有限公司档案与汉冶萍煤铁厂矿旧址、冶炼铁炉、建筑、栈桥和码头",
            "煤铁联合生产、矿山—炼铁—运输一体化技术与企业组织",
            "汉冶萍工人、企业制度和黄石近代工业城市记忆",
            "档案和实体旧址分属不同保护/利用体系，馆藏与厂址开放边界待核",
        ),
    },
    "HBI-HS-005": {
        "source_keys_add": ["huangshi_mining_group_2025"],
        "cultural_evidence": component_evidence(
            "东露天采场、炸药洞、麻雀山碉堡、宿舍楼、选矿厂历史建筑、铁门坎石刻、老火车站和老桥洞",
            "露天采矿、爆破物资储存、选矿、铁路运输和矿山设施防护",
            "矿工、铁山社区、汉冶萍/日铁历史和黄石矿业城市记忆",
            "官方工业遗产地图称其为国家矿山公园和工业遗产群；具体组成项保护边界需逐项核验",
        ),
    },
    "HBI-HS-009": {
        "source_keys_add": ["huangshi_huaxin_2024"],
        "cultural_evidence": component_evidence(
            "36处文物建筑、湿法回转窑、粗磨/细磨/包装车间、装车站台、铁轨、火车头、五羊巷职工生活区",
            "从石灰石加工到水泥烧成、粉磨、包装和装运的完整工艺链",
            "华新工人、职工社区、国家重点工程供货和黄石水泥城市记忆",
            "华新1907文化公园/历史风貌区承担文博、文创和公共文化利用；设备和建筑清单需管理方复核",
        ),
    },
    "HBI-JZ-001": {
        "source_keys_add": ["jingzhou_yangmatou_2024"],
        "cultural_evidence": component_evidence(
            "活力28老厂房、原料罐、烟囱、办公楼和生产设备",
            "日化生产、原料储存和沙市轻工业生产组织",
            "活力28品牌、沙市职工和日化城市记忆",
            "老厂房改造为“沙市工业成就”展馆并纳入洋码头文创园；开放范围和设备清单待核",
        ),
    },
    "HBI-JZ-004": {
        "source_keys_add": ["jingzhou_yangmatou_2024"],
        "cultural_evidence": component_evidence(
            "1927年打包厂、两主楼、红砖外墙、夹丝玻璃、消防/喷淋设备和50余处老建筑",
            "棉花打包、港口仓储和沿江装卸物流组织",
            "沙市商埠、码头工人、战争年代建筑痕迹和洋码头城市记忆",
            "打包厂与洋码头文创园实施保护性改造，建筑保护单元和日常运营信息待核",
        ),
    },
    "HBI-JZ-005": {
        "source_keys_add": ["hubei_archival_heritage_2025"],
        "cultural_evidence": component_evidence(
            "荆江分洪闸及其工程档案、设计施工和运行记录",
            "分洪调度、闸门运行和长江防洪工程技术",
            "工程建设者、荆江治理和长江防洪公共记忆",
            "实体工程持续承担水利功能；档案开放范围和现场展示利用待核",
        ),
    },
    "HBI-PROV-002": {
        "source_keys_add": ["yidu_tea_archives_2021"],
        "cultural_evidence": component_evidence(
            "宜都红茶厂厂房、茶叶加工设备和232卷宜都茶厂档案",
            "宜红茶收购、精制、出口及生产组织技术",
            "茶厂职工、宜红茶产区和宜都地方工业记忆",
            "档案现藏宜都市档案馆；厂址与设备现状、拟认定后保护责任待核",
        ),
    },
}


def merge_update(row: dict[str, Any], patch: dict[str, Any]) -> None:
    for key in patch.get("source_keys_add", []):
        if key not in row.setdefault("source_keys", []):
            row["source_keys"].append(key)
    if "cultural_evidence" in patch:
        existing = row.get("cultural_evidence")
        if existing is None:
            row["cultural_evidence"] = patch["cultural_evidence"]
        elif existing != patch["cultural_evidence"]:
            raise SystemExit(f"conflicting cultural_evidence for {row['inventory_id']}")
    for key in ("related_heritage_ids", "related_inventory_ids"):
        if key in patch:
            values = row.setdefault(key, [])
            for value in patch[key]:
                if value not in values:
                    values.append(value)
    row["source_keys"] = sorted(set(row.get("source_keys") or []))


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    existing_by_id = {row["inventory_id"]: row for row in records}
    existing_names = {row["name"] for row in records}
    duplicate_sources = set(NEW_SOURCES) & set(sources)
    duplicate_ids = {row["inventory_id"] for row in NEW_RECORDS} & set(existing_by_id)
    duplicate_names = {row["name"] for row in NEW_RECORDS} & existing_names
    if duplicate_sources or duplicate_ids or duplicate_names:
        all_new_present = (
            set(NEW_SOURCES) <= set(sources)
            and all(sources[key] == value for key, value in NEW_SOURCES.items())
            and all(row["inventory_id"] in existing_by_id and existing_by_id[row["inventory_id"]] == row for row in NEW_RECORDS)
        )
        if not all_new_present:
            raise SystemExit(
                "partial or conflicting prior application: "
                f"sources={sorted(duplicate_sources)} ids={sorted(duplicate_ids)} names={sorted(duplicate_names)}"
            )
    else:
        missing = sorted({key for row in NEW_RECORDS for key in row["source_keys"] if key not in sources and key not in NEW_SOURCES})
        if missing:
            raise SystemExit(f"missing source keys: {missing}")
        sources.update(NEW_SOURCES)
        records.extend(NEW_RECORDS)
        existing_by_id = {row["inventory_id"]: row for row in records}

    for inventory_id, patch in UPDATES.items():
        row = existing_by_id.get(inventory_id)
        if row is None:
            raise SystemExit(f"update target missing: {inventory_id}")
        merge_update(row, patch)

    data["research_targets"]["coverage_rule"] = (
        "每条对象至少绑定名录/普查/规划/企业史/档案遗产或来源确认资料；"
        "工业遗产实体、工业文化景观、档案文献和待核验线索分层记录。"
        "文化证据字段只记录来源中明确出现的载体、技术、社会记忆和利用状态，未核实内容保持待核。"
    )
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_b_records={len(NEW_RECORDS)} wave_b_sources={len(NEW_SOURCES)} "
        f"total_records={len(records)} total_sources={len(sources)} updates={len(UPDATES)}"
    )


if __name__ == "__main__":
    main()

