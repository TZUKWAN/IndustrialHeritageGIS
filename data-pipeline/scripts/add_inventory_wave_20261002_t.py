from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "donghu_guanggu_survey_notice_2025": {
        "source_type": "district_government_fourth_cultural_relic_survey_notice",
        "title": "武汉东湖高新区文化旅游体育局关于公布东湖高新区第四次全国文物普查新发现不可移动文物名录的通知",
        "org": "武汉东湖新技术开发区文化旅游体育局",
        "pub_date": "2025-11-07",
        "url": "https://www.wehdz.gov.cn/2022/zfxxgk/fdzdgk/gysy/ggwhfw/202511/t20251107_2673811.shtml",
        "authority": "A",
        "notes": "东湖高新区文旅体局正式通知，说明第四次全国文物普查新发现11处不可移动文物，文物级别为未核定，附件为逐条名录；网页正文明确葛店化工厂一号楼旧址等工业相关对象已进入新发现名录。",
    },
    "donghu_guanggu_survey_list_2025": {
        "source_type": "district_government_fourth_cultural_relic_survey_attachment",
        "title": "东湖高新区第四次全国文物普查新发现不可移动文物名录（附件）",
        "org": "武汉东湖新技术开发区文化旅游体育局",
        "pub_date": "2025-11-07",
        "url": "https://www.wehdz.gov.cn/2022/zfxxgk/fdzdgk/gysy/ggwhfw/202511/P020251107567138047161.pdf",
        "authority": "A",
        "notes": "官方附件逐项列出葛店化工厂一号楼旧址（1969年，左岭街道化工路31号）和葛店化工厂机械厂旧址（1960年，左岭街道化工路31号），类别均为近现代重要史迹及代表性建筑，保护级别均为尚未核定。",
    },
    "gehua_group_history_2026": {
        "source_type": "enterprise_official_history",
        "title": "武汉葛化集团有限公司关于我们与历史沿革",
        "org": "武汉葛化集团有限公司",
        "pub_date": "2026-01-01",
        "url": "https://www.whghjt.com/about_us.html",
        "authority": "A",
        "notes": "企业官网确认武汉葛店化工厂1958年8月6日在葛店左岭成立，1996年组建葛化集团，并记录氯碱、化工原料和农药生产相关企业史与‘赶路、大修、马达、创一流’职工精神。网页未逐栋说明旧址建筑，建筑事实仍以四普附件为准。",
    },
    "wuhan_wenshi_gehua_history_2025": {
        "source_type": "municipal_history_publication",
        "title": "时代年轮：武汉工业建设中的葛店化工厂",
        "org": "武汉市政协文史资料",
        "pub_date": "2025-11-14",
        "url": "https://www.whzx.gov.cn/zxzl/wsl/whwszl/202511/P020251114362517576374.pdf",
        "authority": "A",
        "notes": "武汉市政协文史资料记载葛店化工厂1958年8月动工、1959年3月投产，主要生产氯碱、化工原料和多种农药，并将其置于武汉化学工业区形成史中；用于补充技术与城市工业史背景。",
    },
    "hubei_env_gehua_site_2023": {
        "source_type": "provincial_environmental_site_register",
        "title": "湖北省建设用地土壤污染风险管控和修复名录（原葛店化工厂场地）",
        "org": "湖北省生态环境厅",
        "pub_date": "2023-09-14",
        "url": "https://sthjt.hubei.gov.cn/fbjd/zc/zcwj/sthjt/tzgg/202309/P020230914359854524181.pdf",
        "authority": "A",
        "notes": "省生态环境厅名录记录原葛店化工厂南区B、C地块的位置、四至和修复阶段，说明旧厂区仍处于工业场地治理与再利用的现实过程；该来源只用于现状/风险证据，不替代文物认定。",
    },
    "enshi_tobacco_factory_reuse_2025": {
        "source_type": "provincial_media_urban_renewal_report",
        "title": "巧手‘绣’新景——恩施州以绣花功夫焕新老街区老厂区",
        "org": "湖北广播电视台/恩施日报",
        "pub_date": "2025-09-10",
        "url": "https://news.hbtv.com.cn/p/4548181.html",
        "authority": "B",
        "notes": "省级媒体报道确认恩施市航空路1988街区前身为恩施市烟叶复烤厂厂房旧址，1988年奠基、空间约25983平方米、2020年公开招租后活化；同时报道利川市滨江北路原烟叶复烤厂保留烟囱并于2024年改造。来源同时覆盖两处独立厂址，入库时拆分为两条对象。",
    },
    "hubei_enshi_tobacco_factory_safety_2014": {
        "source_type": "provincial_fire_safety_inspection_register",
        "title": "湖北省重大火灾隐患挂牌督办单位（恩施复烤厂）",
        "org": "湖北省人民政府",
        "pub_date": "2014-01-01",
        "url": "https://www.hubei.gov.cn/download/122fire.pdf",
        "authority": "A",
        "notes": "省政府公开消防安全资料记录恩施复烤厂位于恩施市经济开发区硒都工业园99号，列出挑选车间、原烟A-E库、联合工房等建筑及面积/消防设施情况，为厂房组成与历史使用功能提供旁证；不把安全隐患文件当作文保认定。",
    },
    "hefeng_zhongying_red_army_2025": {
        "source_type": "provincial_red_heritage_guide",
        "title": "鹤峰县中营镇红三军军部旧址群",
        "org": "湖北日报传媒集团·红色湖北",
        "pub_date": "2025-02-01",
        "url": "https://www.cnhubei.com/xwzt/2024/hshb/hshbgfjyjd/hshbagzyjyjdes/202502/t4748380.shtml",
        "authority": "B",
        "notes": "红色湖北专题资料明确中营镇红岩坪村旧址群现为湖北省文物保护单位，保存红三军枪炮局、红三军被服厂等16处旧址和8处遗址，并记录县级文保、爱国主义教育基地和全民国防教育基地等保护利用层级。",
    },
    "hefeng_wuliping_industrial_memory_2020": {
        "source_type": "provincial_democratic_league_history_article",
        "title": "五里坪革命旧址中的铁厂、枪炮局与被服厂",
        "org": "中国民主同盟湖北省委员会",
        "pub_date": "2020-01-01",
        "url": "https://www.hubeimm.gov.cn/index.php?id=10125",
        "authority": "B",
        "notes": "民盟湖北公开史料记载五里坪红军旧址保存铁厂、枪炮局、被服厂、医院及供销合作社等生产和后勤节点，说明革命旧址的工业/军需生产文化层；原文未逐项提供单体测绘，保持组成项待核。",
    },
    "badong_gun_factory_repair_2024": {
        "source_type": "county_government_cultural_relic_repair_tender",
        "title": "金果坪乡红三军革命旧址群—枪炮局修缮保护及周边环境整治项目（土建）招标公告",
        "org": "巴东县金果坪乡人民政府",
        "pub_date": "2024-07-12",
        "url": "https://hbtba.com/pro/pro.php?id=5b7405df-ec94-4e1a-b4b9-98692a8a2805",
        "authority": "B",
        "notes": "招标公告确认项目业主为巴东县金果坪乡人民政府，建设地点为江家村，项目对枪炮局旧址周边民居和环境实施文物保护工程与红色文化场景提升；公告不单独给出枪炮局文保级别。",
    },
    "badong_gun_factory_history_2022": {
        "source_type": "provincial_media_revolutionary_history",
        "title": "巴东记忆：寻先烈遗迹忆红色岁月",
        "org": "湖北日报新闻客户端",
        "pub_date": "2022-01-01",
        "url": "https://news.hubeidaily.net/mobile/1360181.html",
        "authority": "B",
        "notes": "湖北日报资料确认1933年巴东县金果坪乡江家村四组设立红三军枪炮局，功能为维修各类军械，并附有残存楼房和旧址影像说明；用于补充生产功能与位置，现存构件仍需现场测绘。",
    },
    "enshi_sanxingdong_gunworks_2023": {
        "source_type": "provincial_media_local_red_heritage_report",
        "title": "恩施市红土乡‘骏马’奔腾的地方：三星洞红军地下军工厂",
        "org": "湖北日报新闻客户端",
        "pub_date": "2023-01-01",
        "url": "https://news.hubeidaily.net/pc/c_1620601.html",
        "authority": "B",
        "notes": "湖北日报报道恩施市红土乡石灰窑村三星洞为红三军制火药、造土枪土炮的地下军工厂，2023年由乡党委政府通过场景复原、文物展览和纪录片升级为红色教育基地；尚未见独立文保名录，保持研究对象层级。",
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
        "HBI-WUHAN-059",
        "葛店化工厂一号楼旧址",
        "武汉市",
        "东湖新技术开发区左岭街道",
        "基础化学工业",
        "district_immovable_relic",
        "东湖高新区第四次全国文物普查新发现、尚未核定级别不可移动文物（1969年）",
        ["donghu_guanggu_survey_notice_2025", "donghu_guanggu_survey_list_2025", "gehua_group_history_2026", "wuhan_wenshi_gehua_history_2025", "hubei_env_gehua_site_2023"],
        "东湖高新区四普官方附件将葛店化工厂一号楼旧址列为近现代重要史迹及代表性建筑，年代1969年，位置为左岭街道化工路31号，保护级别尚未核定。葛化集团官网和武汉政协文史资料补充葛店化工厂1958年建设、1959年投产及氯碱/化工原料/农药生产史；省生态环境厅资料显示原厂区部分地块进入土壤修复与再利用过程。建筑本体、楼号对应关系和厂区保护边界需现场测绘确认。",
        ev(
            "化工路31号葛店化工厂一号楼旧址（1969年）及其所在原厂区工业空间；四普附件未提供建筑面积、结构和设备清单",
            "葛店化工厂氯碱、化工原料和农药生产形成的基础化工技术记忆；一号楼具体行政/生产功能不能由楼号臆测，待厂志与档案核验",
            "1958年建厂、葛化职工社区和‘赶路、大修、马达、创一流’企业精神构成城市化工工业记忆；职工口述与原始档案仍需补录",
            "四普登记为尚未核定不可移动文物；原葛店化工厂南区部分地块处于环境治理和再利用过程中，建筑保存、拆改和公众开放状态待核",
        ),
        aliases=["葛店化工厂一号楼", "葛化一号楼旧址", "左岭化工路31号一号楼"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-WUHAN-060",
        "葛店化工厂机械厂旧址",
        "武汉市",
        "东湖新技术开发区左岭街道",
        "化工机械与设备维修",
        "district_immovable_relic",
        "东湖高新区第四次全国文物普查新发现、尚未核定级别不可移动文物（1960年）",
        ["donghu_guanggu_survey_notice_2025", "donghu_guanggu_survey_list_2025", "gehua_group_history_2026", "hubei_env_gehua_site_2023"],
        "东湖高新区四普官方附件将葛店化工厂机械厂旧址列为近现代重要史迹及代表性建筑，年代1960年，位置为左岭街道化工路31号，保护级别尚未核定。‘机械厂’名称提供化工企业设备制造/维修的功能线索；葛化集团企业史和原厂区环境治理资料可以确认厂区工业谱系与现状风险，但没有公开逐栋设备、工艺或边界清单，保持待核。",
        ev(
            "化工路31号葛店化工厂机械厂旧址及原厂区附属工业空间；现存车间、机修设备和厂房边界未由公开附件逐项确认",
            "机械厂名称与葛店化工厂基础化工生产配套的设备制造、维修记忆；具体机加工、焊接、安装工艺和产品谱系待厂志/设备档案补证",
            "化工企业机修工人、设备保障和葛化职工社区形成的工业组织记忆；企业官网提供职工精神线索，口述史和工会档案待收集",
            "四普登记为尚未核定不可移动文物；原厂区部分地块纳入土壤风险管控/修复名录，旧机械厂本体保存与再利用状态待现场核验",
        ),
        aliases=["葛店化工厂机械厂", "葛化机械厂旧址", "左岭化工路31号机械厂"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-ES-013",
        "恩施市烟叶复烤厂厂房旧址（航空路1988街区）",
        "恩施州",
        "恩施市",
        "烟叶复烤与烟草加工",
        "city_planning",
        "城市更新活化的老厂房对象；尚未见独立工业遗产名录认定",
        ["enshi_tobacco_factory_reuse_2025", "hubei_enshi_tobacco_factory_safety_2014"],
        "湖北广播电视台/恩施日报报道确认航空路1988街区前身为恩施市烟叶复烤厂厂房旧址，1988年奠基，空间约25983平方米，曾因行业调控闲置，2020年通过公开招租引入运营商；铁楼梯和厂房空间被保留并改造为餐饮、音乐、运动和创业街区。省政府消防资料补充恩施复烤厂原烟库、联合工房和挑选车间等功能建筑线索。当前按城市更新对象表达，不把活化报道升格为法定工业遗产认定。",
        ev(
            "1988年奠基的烟叶复烤厂厂房、铁楼梯及原烟库/联合工房/挑选车间等生产空间；建筑逐栋清单和原设备目录待测绘",
            "烟叶复烤、原烟分选、仓储和联合工房组织生产的烟草加工技术记忆；公开资料未给出设备型号与工艺参数",
            "恩施烟草工人、国有烟草企业和航空路工业片区记忆；街区保留工业构件并通过新业态吸引公众，职工口述与企业档案待补",
            "2020年公开招租后转为航空路1988街区，已形成商业、运动和创业空间；原厂房保护边界、产权责任和开放管理需现场核验",
        ),
        aliases=["恩施烟叶复烤厂旧址", "航空路1988街区", "恩施复烤厂厂房"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-ES-014",
        "利川市烟叶复烤厂旧址（滨江北路片区）",
        "恩施州",
        "利川市",
        "烟叶复烤与烟草加工",
        "city_planning",
        "城市更新活化的老厂房对象；尚未见独立工业遗产名录认定",
        ["enshi_tobacco_factory_reuse_2025"],
        "湖北广播电视台/恩施日报报道确认利川市滨江北路原烟叶复烤厂在更新前厂房破败，2024年由城市更新项目投入专项资金改造，保留原烟囱并改造成具有实用与景观功能的‘烟囱温度计’，片区转为商业餐饮街区。报道未给出厂房建成年代、原生产设备和独立文保级别，保持城市更新对象层级。",
        ev(
            "滨江北路原烟叶复烤厂厂房、烟囱及配套工业空间；现存建筑编号、设备和厂界未公开",
            "烟叶复烤、烟叶仓储与烟囱排放设施构成烟草加工技术景观线索；具体工艺和企业沿革待利川地方志/企业档案核验",
            "利川烟草产业、烟叶工人和城市居民对厂区烟囱的地方记忆；烟囱温度计成为新公共文化地标，口述资料待补",
            "2024年完成片区系统更新，保留烟囱原貌并植入商业餐饮业态；原厂房真实性、保存比例和运营保护责任待现场核验",
        ),
        aliases=["利川烟叶复烤厂旧址", "滨江北路原烟叶复烤厂", "利川复烤厂烟囱"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-ES-015",
        "鹤峰县中营镇红三军枪炮局旧址",
        "恩施州",
        "鹤峰县中营镇",
        "革命军械维修与制造",
        "provincial_heritage_related",
        "湖北省文物保护单位中营镇红三军军部旧址群的生产性组成项；单体级别和边界待核",
        ["hefeng_zhongying_red_army_2025"],
        "红色湖北专题资料确认中营镇红岩坪村红三军军部旧址群为湖北省文物保护单位，群内保存红三军枪炮局、红三军被服厂等16处旧址和8处遗址。枪炮局作为群内明确列名的军械生产/维修节点单独建档，以便表达工业文化载体；现存房屋、工具、设备和单体保护范围尚需文保档案与现场核验。",
        ev(
            "红岩坪村中营镇红三军军部旧址群内枪炮局旧址及相关房屋遗存；公开资料未提供单体测绘、工具和设备清单",
            "土地革命时期红三军枪炮局军械维修与制造的生产记忆；具体枪械、火药、金属加工工艺和生产组织待档案及实物调查",
            "贺龙率红三军驻扎、军民协作和红岩坪村革命生产生活记忆；旧址群作为国防教育基地承担公共传播功能",
            "旧址群已列湖北省文物保护单位并开放为红色教育/国防教育基地；枪炮局单体保存、展陈和开放边界待核",
        ),
        aliases=["红三军枪炮局旧址", "中营红三军枪炮局", "红岩坪枪炮局"],
        asset_kind="revolutionary_industrial_site",
    ),
    rec(
        "HBI-ES-016",
        "鹤峰县中营镇红三军被服厂旧址",
        "恩施州",
        "鹤峰县中营镇",
        "革命军需纺织与被服生产",
        "provincial_heritage_related",
        "湖北省文物保护单位中营镇红三军军部旧址群的生产性组成项；单体级别和边界待核",
        ["hefeng_zhongying_red_army_2025"],
        "红色湖北专题资料将红三军被服厂列为中营镇红三军军部旧址群保存的生产性旧址之一。它与枪炮局分开建档，表达革命军需纺织和被服生产的工业文化层；公开资料没有提供缝纫工具、厂房编号和单体保护范围，不能把群体认定替代单体证据。",
        ev(
            "红岩坪村旧址群内红三军被服厂相关房屋和生产空间；缝纫工具、纺织设备、布料和建筑边界待核",
            "红军被服、布料裁剪和军需生产组织的技术记忆；具体工序、人员和产量没有公开档案支撑，保持待核",
            "红三军后方保障、当地群众支援和被服厂劳动记忆；旧址群教育活动提供社会传播入口，口述史待补",
            "被服厂作为省级文保群组成项纳入红色教育和国防教育展示；单体是否开放、原真性和日常管理待核",
        ),
        aliases=["红三军被服厂旧址", "中营红三军被服厂", "红岩坪被服厂"],
        asset_kind="revolutionary_industrial_site",
    ),
    rec(
        "HBI-ES-017",
        "恩施市红土乡三星洞红三军地下军工厂遗址",
        "恩施州",
        "恩施市红土乡",
        "革命军火与火药制造",
        "research_candidate",
        "地方红色文化保护与活化对象；尚未见独立文物保护单位或工业遗产认定",
        ["enshi_sanxingdong_gunworks_2023"],
        "湖北日报报道恩施市红土乡石灰窑村三星洞一带在1929—1933年成为红三军地下军工厂，曾制火药、造土枪土炮；2023年乡党委政府通过场景复原、文物展览和纪录片将其升级为红色教育基地。来源能确认生产叙事和公共利用，但洞体遗存、工具、历史边界和法定名录状态仍需文保调查，故保持研究对象层级。",
        ev(
            "石灰窑村文家铺组三星洞天然洞体、红军洞及周边地下军工空间；现存炉具、工具和遗物清单待现场调查",
            "1929—1933年制火药、造土枪土炮的地下军工生产记忆；公开报道未提供配方、工序、产量和人员档案",
            "红三军驻扎、当地群众支援和军民共同生产记忆；红土乡群众传唱、场景复原和红色教育基地形成当代传播",
            "2023年升级为红色教育基地，开展场景复原、文物展览和纪录片展示；洞体安全、原真性和保护级别待核",
        ),
        aliases=["三星洞红军兵工厂", "红土乡三星洞军工厂", "三星洞红三军兵工遗址"],
        asset_kind="industrial_archaeology",
    ),
    rec(
        "HBI-ES-018",
        "巴东县金果坪乡红三军枪炮局旧址",
        "恩施州",
        "巴东县金果坪乡江家村",
        "革命军械维修与制造",
        "county_relic_related",
        "金果坪乡红三军革命旧址群修缮保护项目对象；单体文保级别待核",
        ["badong_gun_factory_repair_2024", "badong_gun_factory_history_2022"],
        "湖北日报资料确认1933年在巴东县金果坪乡江家村四组设立红三军枪炮局，功能为维修各类军械，并记录残存楼房；巴东县金果坪乡人民政府2024年招标公告确认枪炮局旧址周边民居和环境整治项目已按文物保护工程立项建设。现有资料可确认名称、位置、功能和保护行动，但未公开单体级别、建筑测绘及设备清单。",
        ev(
            "江家村四组红三军枪炮局旧址及残存楼房、周边民居环境；招标公告没有公布完整测绘和设备目录",
            "1933年红三军维修各类军械的军工技术和后勤组织记忆；具体维修设备、金属加工工具和产品范围待实物/档案核验",
            "金果坪红色根据地、军民协作和红三军枪炮局社会记忆；枪炮局串联金果红路红色教育线路",
            "2024年启动旧址修缮保护和周边环境整治，设置红军标语、主题雕塑等展示设施；工程完成度、原真性和开放制度待核",
        ),
        aliases=["红三军枪炮局旧址（巴东）", "金果坪枪炮局", "江家村红三军枪炮局"],
        asset_kind="revolutionary_industrial_site",
    ),
    rec(
        "HBI-ES-019",
        "鹤峰县五里坪革命旧址群生产性组成项",
        "恩施州",
        "鹤峰县走马镇",
        "革命军需生产与铁工",
        "national_heritage_related",
        "五里坪革命旧址群中的铁厂、枪炮局、被服厂等生产性组成项；工业子项边界待核",
        ["hefeng_wuliping_industrial_memory_2020", "hubei_revolutionary_register_2021"],
        "民盟湖北公开史料记载五里坪革命旧址保存铁厂、枪炮局、被服厂、红军医院和供销合作社等生产/后勤节点；湖北省革命文物名录制度来源用于确认革命文物保护层级边界，但未在公开附件中逐项拆出工业子项。此条作为旧址群工业文化组成项记录，不把生产节点错误写成独立国家工业遗产。",
        ev(
            "五里坪老街革命旧址群内铁厂、枪炮局、被服厂及相关房屋、工具和后勤空间；组成项位置与保存状况待分项测绘",
            "铁工、枪械制造/维修、被服生产和革命根据地后勤组织构成复合型军需工业技术记忆；设备与工艺档案待补",
            "红二军、红四军与鹤峰群众共同建设根据地、组织生产和供给保障的社会记忆；五里坪红色教育和地方文化传播持续承载",
            "旧址群作为革命文物和红色旅游节点利用；铁厂、枪炮局、被服厂单体边界、保护责任和开放方式待核",
        ),
        aliases=["五里坪红军铁厂旧址", "五里坪枪炮局旧址", "五里坪红军被服厂旧址", "五里坪革命生产旧址群"],
        asset_kind="revolutionary_industrial_cluster",
    ),
]


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
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_t_sources={len(NEW_SOURCES)} added_records={len(NEW_RECORDS)} "
        f"total_records={len(records)} total_sources={len(sources)} patched_records=0"
    )


if __name__ == "__main__":
    main()
