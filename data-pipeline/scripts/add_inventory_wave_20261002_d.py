from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "miit_recheck_2025": {
        "source_type": "government_register",
        "title": "通过复核的第三批国家工业遗产名单",
        "org": "工业和信息化部/中国政府网",
        "pub_date": "2025-10-17",
        "url": "https://www.gov.cn/zhengce/zhengceku/202510/P020251023673841442628.pdf",
        "authority": "A",
        "notes": "工信部官方附件第28项列湖北5133厂，地址为湖北省襄阳市老河口市，核心物项包括建设指挥部、北办公楼、301/302/305工房、铁路专用线、工人俱乐部、招待所、溜冰场、篮球场及多类机械和光学设备；本来源用于确认2025年第三批复核口径。",
    },
    "laohekou_industrial_reuse_2026": {
        "source_type": "government_media",
        "title": "老河口市精准施策，提升节约集约用地水平——让“沉睡资源”变“增收活水”",
        "org": "湖北省自然资源厅/中国自然资源报",
        "pub_date": "2026-01-15",
        "url": "https://zrzyt.hubei.gov.cn/bmdt/sxdt/202601/t20260115_5856401.shtml",
        "authority": "A",
        "notes": "官方报道确认酂阳街道原老河口市余热发电厂始建于20世纪70年代，厂房和设备闲置后于2025年招商活化；同时记录原湖北东沃专用汽车有限公司68亩工业用地、约1.3万平方米厂房和办公楼停产后由专用汽车企业再利用。",
    },
    "huangshi_wuyunduo_2026": {
        "source_type": "government_news",
        "title": "争创国家历史文化名城——“中国保尔”的初心从这里点燃 吴运铎和黄石的红色情缘",
        "org": "黄石市住房和城市更新局/云上黄石",
        "pub_date": "2026-06-23",
        "url": "https://zjj.huangshi.gov.cn/ztlm/lsjcyy/tzgg8/202606/t20260623_1336841.html",
        "authority": "A",
        "notes": "黄石市住房和城市更新局报道确认西塞山区桐厂社区原煤矿机电车间旧址为吴运铎曾工作之处；第四次全国文物普查已确认，拟申报文物保护单位，产权单位已开展修缮并筹划煤炭工业遗址展示中心。",
    },
    "huangshi_kangning_2026": {
        "source_type": "government_media",
        "title": "湖北黄石探索三大低效用地再开发路径 推动城市功能提档升级",
        "org": "湖北省自然资源厅/中国自然资源报",
        "pub_date": "2026-04-14",
        "url": "https://zrzyt.hubei.gov.cn/bmdt/sxdt/202604/t20260414_5914182.shtml",
        "authority": "A",
        "notes": "官方报道确认下陆区中国十五冶公司闲置仓库改造为康宁园工友茶馆和幸福食堂，保留钢结构、斑驳砖墙并融入十五冶、纺机厂工业文化；同页记录原国营黄石纺织机械厂旧厂区保护性修缮与再开发。",
    },
    "huaxin1907_2026": {
        "source_type": "government_media",
        "title": "争创国家历史文化名城——窑火百年 温暖新生",
        "org": "黄石市住房和城市更新局/黄石日报",
        "pub_date": "2026-07-23",
        "url": "https://zjj.huangshi.gov.cn/ztlm/lsjcyy/tzgg8/202607/t20260723_1345391.html",
        "authority": "A",
        "notes": "官方报道记录华新1907文化公园保留传送长廊、水泥筒仓、红砖水塔、蒸汽火车、旧机械和湿法回转窑等核心工业载体，385亩工业遗址分为文博、文创、文商板块，联动五羊巷和老工人生活区活化利用。",
    },
    "wuhan_guibei_2026": {
        "source_type": "government_news",
        "title": "蛇山龟山焕新，游客一秒入戏，沉浸式体验“活化”的长江文明",
        "org": "武汉市人民政府/武汉城建集团",
        "pub_date": "2026-03-01",
        "url": "https://3g.wuhan.gov.cn/zjwh/whly/202603/t20260301_2733995.shtml",
        "authority": "A",
        "notes": "武汉市政府报道确认龟北启动片占地209亩，保留并改造原汉阳特种汽车制造厂、鹦鹉磁带厂等8.8万平方米老厂房，结合汉阳兵工厂和鹦鹉磁带厂历史建筑开展展示与城市更新。",
    },
    "wuhan_fuxin_2025": {
        "source_type": "government_reply",
        "title": "市住房和城市更新局对市政协十四届四次会议第20250688号提案的答复",
        "org": "武汉市住房和城市更新局",
        "pub_date": "2025-10-14",
        "url": "https://zgj.wuhan.gov.cn/xxgk/xxgkml/qtzdgknr/jytabl/202510/t20251014_2659847.shtml",
        "authority": "A",
        "notes": "官方答复确认福新第五面粉厂旧址位于硚口区沿河大道364号，1918年建成，2011年列为市级文物保护单位并纳入武汉市第一批工业遗产名录；目前已完成安全、抗震鉴定和地质勘探，推进修缮活化方案。",
    },
    "wuhan_qiaokou_industrial_2026": {
        "source_type": "government_news",
        "title": "央视网：武汉城市更新进行时 | 硚口区：从“工业锈带”到“发展秀带”",
        "org": "武汉市人民政府/央视网",
        "pub_date": "2026-04-15",
        "url": "https://www.wuhan.gov.cn/sy/kwh/202604/t20260415_2753343.shtml",
        "authority": "A",
        "notes": "官方报道确认硚口皮子街片区保留1910年康成酒厂和1916年南洋烟厂工业遗存，汉江湾保留床单厂等老厂房，古田四路47号德必·古田坊由28幢老厂房改造并融入文创、非遗和社区服务。",
    },
    "wuhan_industrial_list_2026": {
        "source_type": "government_news",
        "title": "武汉市无线电厂入选省级工业遗产",
        "org": "武汉市经济和信息化局",
        "pub_date": "2026-02-03",
        "url": "https://jxj.wuhan.gov.cn/xwzx_9/gzdt/202602/t20260204_2724898.html",
        "authority": "A",
        "notes": "武汉市经信局官方页面确认武汉已有5处国家工业遗产、1处湖北省工业遗产和27处武汉市工业遗产，并补充无线电厂1961年成立、长江牌音响和7栋包豪斯建筑等文化信息；27处完整清单通过页面外链继续核验。",
    },
    "xiangyang_609_2025": {
        "source_type": "government_media",
        "title": "空置老厂区摇变文旅新地标",
        "org": "湖北省文化和旅游厅/湖北日报",
        "pub_date": "2025-09-17",
        "url": "https://wlt.hubei.gov.cn/bmdt/szyw/xy/202509/t20250917_5774057.shtml",
        "authority": "A",
        "notes": "官方报道确认襄阳609园区前身为中国航空工业第609研究所（红旗研究所），20世纪60年代初迁入，保留厂房、家属楼、百货商店、公社大食堂、航空物件和飞机模型，正建设三线记忆与军工文化复合型旅游园区。",
    },
    "enshi_industrial_heritage_2026": {
        "source_type": "government_news",
        "title": "恩施：多方协同共护工业遗产",
        "org": "湖北省人民检察院",
        "pub_date": "2026-05-28",
        "url": "https://www.hbjc.gov.cn/ejxw/gddt/202605/t20260529_1890336.shtml",
        "authority": "A",
        "notes": "省检察院报道确认狮子桥水电站1964年由张富清带领群众建成，2025年12月列为湖北省文物保护单位；老虎洞水电站1958年建成、为恩施州首座水电站，2014年为省保、2023年入选国家能源集团首批工业遗产，并记录水库环境治理和协同管护。",
    },
    "qianjiang_oilcity_2026": {
        "source_type": "government_news",
        "title": "“油城”不靠油：潜江靠什么？",
        "org": "潜江市人民政府/白鹭湖管理区",
        "pub_date": "2026-01-19",
        "url": "https://www.hbqj.gov.cn/blhq/xwzx/gsgg/202601/t20260119_5857728.html",
        "authority": "A",
        "notes": "潜江市政府报道以江汉第一口油井纪念碑、五七油田会战指挥部旧址为叙事核心，确认1965年钟11井工业油流、1972年江汉石油管理局成立、1976年潜江市石油化工厂前身建立，并记录12万石油大军会战记忆。",
    },
    "qianjiang_route_2025": {
        "source_type": "government_news",
        "title": "勇担使命强服务 共绘油地融合新篇章",
        "org": "潜江市人民政府/潜江新闻网",
        "pub_date": "2025-05-28",
        "url": "https://www.hbqj.gov.cn/xwzx/jrqj/qjyw/202505/t20250528_5667225.html",
        "authority": "A",
        "notes": "潜江市广华寺街道官方访谈提出依托五七会战指挥部旧址、江汉油田第一口井和岩心库打造石油特色工业旅游线路与科普研学基地，明确油田元素进入地方产业和公共文化场景的利用方向。",
    },
    "qianjiang_cultural_2026": {
        "source_type": "government_news",
        "title": "楚韵虾香·乐享春光——潜江市春季文旅推介新闻发布会",
        "org": "潜江市人民政府",
        "pub_date": "2026-03-13",
        "url": "https://www.hbqj.gov.cn/zmhd/xwfbh/202603/t20260313_5891912.html",
        "authority": "A",
        "notes": "潜江市政府新闻发布材料将五七油田会战指挥部旧址表述为中央企业工业文化遗产和湖北省爱国主义教育基地，补充油田学校等工业社区文化载体信息。",
    },
    "tianmen_textile_2026": {
        "source_type": "government_news",
        "title": "天门纺机捐赠设备模型丰富纺织服装博物馆馆藏",
        "org": "天门市人民政府/天门网",
        "pub_date": "2026-07-16",
        "url": "https://www.tianmen.gov.cn/xwzx/tmxw/202607/t20260716_5977667.shtml",
        "authority": "A",
        "notes": "天门市政府报道确认天门纺织机械股份有限公司向天门纺织服装博物馆捐赠3台不同发展时期的并条机设备模型，其中含1997年款老式模型；公司深耕纺机制造70载。该来源用于工业文化载体和馆藏记录，不等同旧厂址认定。",
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


def ev(material: str, technical: str, social: str, current: str) -> dict[str, str]:
    return {
        "material_carriers": material,
        "technical_memory": technical,
        "social_memory": social,
        "current_use_or_loss": current,
    }


NEW_RECORDS: list[dict[str, Any]] = [
    rec(
        "HBI-XIANGYANG-021",
        "湖北5133厂（江山重工）三线工业文化档案扩展",
        "襄阳市",
        "军工机械工业",
        "national_cultural_relic_related",
        "第三批国家工业遗产（2025年复核通过；文化档案扩展记录）",
        ["jiangshan_official", "jiangshan_cjyun", "miit_recheck_2025"],
        "工信部2025年复核附件、湖北省国防科工部门和官方媒体共同确认湖北5133厂即江山重工旧址。本条作为国家主表HER-407fe7b65baa的文化档案扩展，补充三线厂区、设备、档案和职工生活载体，不另立重复国家遗产点。",
        ev(
            "建设指挥部、北办公楼、301/302/305工房、铁路专用线、工人俱乐部、招待所、溜冰场、篮球场，以及车床、滚齿机、插齿机、投影仪、光切显微镜等核心物项",
            "三线火箭炮总装、机械加工、精密齿轮加工和光学检测生产组织；1969年兴建、1972年竣工的军工生产技术记忆",
            "三线建设者、军工职工、家属区和老河口洪山嘴镇苏家河村工业社区记忆",
            "2025年第三批复核通过；保护、开放范围、档案目录和涉密边界需与产权单位和地方普查资料继续核验",
        ),
        district="老河口市",
        aliases=["江山重工集团旧址", "湖北5133厂旧址", "江山机械厂"],
        asset_kind="industrial_site",
        related_heritage_ids=["HER-407fe7b65baa"],
    ),
    rec(
        "HBI-XIANGYANG-022",
        "原老河口市余热发电厂旧址（八禧礼宴艺术中心活化）",
        "襄阳市",
        "电力能源",
        "research_candidate",
        "官方报道确认的工业遗迹活化对象（未见正式名录认定）",
        ["laohekou_industrial_reuse_2026"],
        "湖北省自然资源厅报道确认原老河口市余热发电厂位于酂阳街道临江社区，始建于20世纪70年代，厂房和设备闲置后于2025年招商建设八禧礼宴艺术中心；本条保持研究候选层级。",
        ev(
            "20世纪70年代余热发电厂厂房、发电设备和厂院空间（具体设备清单待现场核验）",
            "余热发电、工业能源循环和热电厂运行组织",
            "老河口工业转型、热电厂职工和临江社区工业记忆",
            "2025年导入艺术中心等新功能，规划建筑面积约5392.61平方米；原设备保存状态和公共展示边界待核",
        ),
        district="老河口市",
        aliases=["老河口市余热发电厂旧址", "八禧礼宴艺术中心旧厂区"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-XIANGYANG-023",
        "原湖北东沃专用汽车有限责任公司旧厂区",
        "襄阳市",
        "专用汽车制造",
        "research_candidate",
        "官方报道确认的停产工业厂区再利用对象（未见正式名录认定）",
        ["laohekou_industrial_reuse_2026"],
        "官方报道将原湖北东沃专用汽车有限公司列为老河口经济技术开发区低效工业用地再利用案例；来源确认68亩工业用地、约1.3万平方米厂房和办公楼，记录为工业遗存研究候选，不把再利用项目直接写成遗产认定。",
        ev(
            "原东沃公司厂房、办公楼和68亩工业用地（具体保留建筑待核）",
            "专用汽车制造、厂区布局和停产后工业空间再利用",
            "东沃公司职工、老河口汽车制造和产业转型记忆",
            "2019年由湖北锡宇汽车有限公司租用并继续用于专用汽车制造，原建筑保留比例和可展示内容待核",
        ),
        district="老河口市",
        aliases=["湖北东沃专用汽车有限责任公司旧址", "东沃专用汽车厂旧厂房"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-HS-034",
        "吴运铎曾工作过的原煤矿机电车间旧址",
        "黄石市",
        "煤炭工业与机械制造",
        "municipal_relic_related",
        "第四次全国文物普查确认；拟申报文物保护单位",
        ["huangshi_wuyunduo_2026"],
        "黄石市住房和城市更新局报道确认西塞山区桐厂社区原煤矿机电车间旧址，吴运铎1930—1938年在此学习并工作；西塞山区文旅局已在第四次全国文物普查中确认并拟申报文保单位，当前不提前升级正式级别。",
        ev(
            "红砖红瓦、蓝色窗格的原煤矿机电车间，车间内景和吴运铎工作空间",
            "电工、钳工、车工、焊工和矿山机械维修技艺；吴运铎在车间讲授技术并形成军工技能基础",
            "吴运铎、富源/源华煤矿工友、矿工运动、读报学习和黄石煤炭工业社区记忆",
            "产权属黄石工矿集团，2025年已投入外部整治和修缮，正在推进陈列布展并筹划煤炭工业遗址展示中心",
        ),
        district="西塞山区",
        aliases=["吴运铎工运车间", "源华煤矿电机车间旧址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-HS-035",
        "中国十五冶闲置仓库—康宁园工友茶馆",
        "黄石市",
        "冶金建设与机械制造",
        "industrial_tourism_related",
        "官方工业遗存活化利用对象（未见独立名录认定）",
        ["huangshi_kangning_2026"],
        "湖北省自然资源厅报道确认下陆区中国十五冶公司闲置仓库改造为康宁园工友茶馆和幸福食堂，保留钢结构、斑驳砖墙并融入十五冶、纺机厂工业文化；本条记录物质遗存与社会记忆的活化载体。",
        ev(
            "中国十五冶闲置仓库钢结构、斑驳砖墙、仓储空间和康宁园社区环境",
            "冶金建设企业仓储、工业厂房轻量化改造和社区公共空间再利用",
            "十五冶职工、黄石纺机厂、下岗职工和康宁园居民的老工业社区记忆",
            "已改造为工友茶馆、幸福食堂和社区微旅游场景，保留比例、原仓库编号和产权资料待核",
        ),
        district="下陆区",
        aliases=["康宁园工友茶馆", "十五冶闲置仓库活化项目"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-HS-036",
        "华新1907文化公园（华新水泥厂活化区）",
        "黄石市",
        "水泥工业与工业文化旅游",
        "national_cultural_relic_related",
        "国家工业遗产/全国重点文物保护单位活化利用场景",
        ["huaxin1907_2026"],
        "华新1907文化公园是华新水泥厂旧址的活化利用范围，本条作为文化景观和公共利用层记录，关联国家工业遗产HER-0577e36e0167及其组成项，不另立遗产认定。",
        ev(
            "老式传送长廊、巨型水泥筒仓、红砖水塔、复古蒸汽火车、旧机械、粗细磨车间、湿法回转窑和6栋保留老厂房",
            "1907年以来水泥生产、湿法回转窑、物料输送和厂区能源物流技术",
            "华新职工、华新街与华新二村老工人生活区、民族工业和国家工程建设记忆",
            "385亩工业遗址已分为文博、文创、文商板块，开放为文化公园、研学和文旅消费空间；保护单元清单持续补核",
        ),
        asset_kind="industrial_cultural_landscape",
        related_heritage_ids=["HER-0577e36e0167"],
    ),
    rec(
        "HBI-WUHAN-042",
        "康成酒厂旧址（南洋1916园区核心区）",
        "武汉市",
        "食品饮料工业与城市更新",
        "city_planning",
        "官方城市更新报道确认的工业遗存对象；与片区历史标签待测绘厘清",
        ["wuhan_qiaokou_industrial_2026"],
        "官方报道明确南洋1916园区前身为1910年康成酒厂，并记录原结构、原型制、原工艺、原材料修缮。现有底册另有“南洋1916园区（原武汉床单总厂老厂房）”记录，两者可能是片区不同历史层，本条先并列保存并要求专项测绘、档案核对。",
        ev(
            "康成酒厂老厂房、红砖墙面、拱券顶和皮子街片区工业建筑肌理",
            "近代酒类生产、厂房原结构修缮和老工业片区空间更新",
            "硚口老城居民、康成酒厂职工和汉口近代轻工业记忆",
            "纳入南洋1916园区保护性修缮，已导入文创、商业和公共服务；酒厂与床单厂历史边界待核",
        ),
        district="硚口区",
        aliases=["康成酒厂旧址", "南洋1916园区康成酒厂层"],
        asset_kind="industrial_cultural_landscape",
        related_inventory_ids=["HBI-WUHAN-039"],
    ),
    rec(
        "HBI-WUHAN-043",
        "德必·古田坊工业遗存片区",
        "武汉市",
        "综合工业与城市更新",
        "city_planning",
        "官方城市更新报道确认的老厂房活化片区",
        ["wuhan_qiaokou_industrial_2026"],
        "武汉市政府报道确认古田四路47号德必·古田坊占地110余亩，由28幢老旧厂房改造而成；原企业谱系和逐栋工业遗产级别尚待普查，故保留城市更新层级。",
        ev(
            "28幢老旧厂房、旧仓库、老邮局、内街和工业园区空间肌理",
            "多类型工业厂房适应性再利用、仓储空间改造和园区运营",
            "硚口古田片区工人、居民、婚姻服务和地方民俗记忆",
            "已导入文创、非遗展示、亲子研学、婚姻登记和社区服务，原企业与设备清单待核",
        ),
        district="硚口区",
        aliases=["古田坊", "德必古田坊老厂房片区"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-WUHAN-044",
        "龟北启动片老厂房更新区",
        "武汉市",
        "近代工业建筑与城市更新",
        "city_planning",
        "官方城市更新确认的工业文化景观片区",
        ["wuhan_guibei_2026"],
        "武汉市政府报道确认龟北启动片在汉阳近代工业发源地背景下，保留并改造原汉阳特种汽车制造厂、鹦鹉磁带厂等8.8万平方米老厂房；本条为片区尺度对象，关联已有单体记录。",
        ev(
            "原汉阳特种汽车制造厂、鹦鹉磁带厂等8.8万平方米老厂房、红砖墙和厂区空间",
            "特种汽车制造、磁带与音像工业、近代厂房结构和城市更新展示技术",
            "汉阳兵工厂、汉阳特种汽车厂、鹦鹉磁带厂职工与近代工业城市记忆",
            "项目分期建设，计划首开区2026年底、二期2027年底完成；保留建筑逐栋清单和开放边界待核",
        ),
        district="汉阳区",
        aliases=["龟北启动片工业遗存", "汉阳特种汽车厂—鹦鹉磁带厂更新区"],
        asset_kind="industrial_cultural_landscape",
        related_inventory_ids=["HBI-WUHAN-025", "HBI-WUHAN-026"],
    ),
    rec(
        "HBI-QJ-006",
        "江汉油田五七会战工业文化线路",
        "潜江市",
        "石油工业与工业文化旅游",
        "city_planning",
        "官方规划和文旅报道确认的工业文化线路（不等同单体遗产认定）",
        ["qianjiang_oilcity_2026", "qianjiang_route_2025", "qianjiang_cultural_2026"],
        "潜江市官方材料将江汉第一口油井、五七油田会战指挥部旧址、岩心库和油田社区共同纳入石油工业旅游、科普研学和工业文化传播场景；本条为线路和文化景观层，单体认定沿用各自记录。",
        ev(
            "江汉第一口油井纪念碑、五七油田会战指挥部旧址、岩心库、油田学校和广华矿区公共空间",
            "石油勘探、钻井、岩心保存、油田会战组织和石化产业链演进",
            "12万石油大军、江汉油田职工、油田学校、广华社区和自力更生工业精神",
            "官方提出打造石油特色工业旅游线路、科普研学基地和油地融合文化场景；具体游线和开放管理持续核验",
        ),
        district="广华寺街道",
        aliases=["五七油田工业文化线路", "江汉油田工业旅游线路"],
        asset_kind="industrial_cultural_landscape",
        related_inventory_ids=["HBI-QJ-001", "HBI-QJ-002", "HBI-QJ-003", "HBI-QJ-005"],
    ),
    rec(
        "HBI-TM-010",
        "天门纺织机械并条机模型与纺织服装博物馆馆藏",
        "天门市",
        "纺织机械工业",
        "research_candidate",
        "企业捐赠的工业文化载体（非旧址认定）",
        ["tianmen_textile_2026"],
        "天门市政府报道确认天门纺织机械股份有限公司向天门纺织服装博物馆捐赠3台不同发展时期的并条机设备模型；本条把可验证的设备模型、馆藏和产业记忆纳入工业文化层，不将现役企业或模型误写成旧厂址。",
        ev(
            "3台不同发展时期的并条机设备模型，包括1997年款老式设备模型和天门纺织服装博物馆馆藏体系",
            "并条机研发、棉纺工艺迭代、纺织机械制造和行业标准建设",
            "天门纺机70年企业史、纺织工人、地方纺织产业和博物馆公共记忆",
            "设备模型已进入博物馆展陈并用于讲述天门纺织故事；原企业老厂房、完整图样和档案目录待继续补查",
        ),
        aliases=["天门纺机并条机模型", "天门纺织服装博物馆纺机馆藏"],
        asset_kind="documentary_heritage",
    ),
]


UPDATES: dict[str, dict[str, Any]] = {
    "HBI-HS-009": {
        "source_keys_add": ["huaxin1907_2026"],
    },
    "HBI-HS-015": {
        "source_keys_add": ["huangshi_kangning_2026"],
        "cultural_evidence": ev(
            "黄石纺织机械厂老厂区厂房和保留工业肌理的建筑空间",
            "纺织机械制造、厂区生产组织和老厂房修缮再利用",
            "纺机厂职工、下陆老工业基地和社区工友记忆",
            "原厂区纳入低效用地再开发并引入山力科技产业园，保留建筑单体和设备清单待核",
        ),
    },
    "HBI-WUHAN-009": {
        "source_keys_add": ["wuhan_fuxin_2025"],
        "cultural_evidence": ev(
            "1918年福新第五面粉厂厂房、沿河大道364号厂区主体和面粉工业建筑构件",
            "近代民族面粉生产、粮食加工厂房和城市工业供应体系",
            "武汉民族工业、硚口沿江工业社区和面粉厂职工记忆",
            "官方答复确认已完成安全、抗震鉴定和地质勘探，正在推进修缮与活化利用；开放方案待审批",
        ),
    },
    "HBI-WUHAN-025": {
        "source_keys_add": ["wuhan_guibei_2026"],
        "cultural_evidence": ev(
            "原汉阳特种汽车制造厂老厂房及龟北片保留的红砖建筑空间",
            "特种汽车制造、近代机械工业和厂房适应性再利用",
            "汉阳特种汽车厂职工、汉阳兵工传统和龟北工业社区记忆",
            "纳入龟北启动片城市更新并计划分期开放；具体厂房编号、设备和产权边界待核",
        ),
    },
    "HBI-WUHAN-026": {
        "source_keys_add": ["wuhan_guibei_2026"],
        "cultural_evidence": ev(
            "鹦鹉磁带厂老厂房、龟北片红砖建筑和原厂区空间格局",
            "磁带与音像产品制造、电子工业生产和厂房再利用",
            "鹦鹉磁带厂职工、汉阳近代工业和音像产品城市记忆",
            "纳入龟北启动片保留改造范围；原设备、产品档案和厂房逐栋保护状态待核",
        ),
    },
    "HBI-PROV-003": {"source_keys_add": ["wuhan_industrial_list_2026"]},
    "HBI-WUHAN-034": {"source_keys_add": ["wuhan_qiaokou_industrial_2026"]},
    "HBI-WUHAN-039": {"source_keys_add": ["wuhan_qiaokou_industrial_2026"]},
    "HBI-XIANGYANG-005": {
        "source_keys_add": ["xiangyang_609_2025"],
        "cultural_evidence": ev(
            "609园区老厂房、红砖家属楼、百货商店、公社大食堂、航空物件和飞机模型",
            "航空机载机电科研生产、三线军工厂区组织和航空工业技术记忆",
            "609研究所职工、家属区、三线建设者和襄城樱桃沟社区记忆",
            "原研究所2005年整体迁往南京后，园区正转为生态休闲、教育培训和军工文化旅游园区；涉密资料边界待核",
        ),
    },
    "HBI-ES-001": {"source_keys_add": ["enshi_industrial_heritage_2026"]},
    "HBI-ES-002": {"source_keys_add": ["enshi_industrial_heritage_2026"]},
    "HBI-QJ-001": {
        "source_keys_add": ["qianjiang_oilcity_2026", "qianjiang_route_2025", "qianjiang_cultural_2026"]
    },
    "HBI-QJ-002": {
        "source_keys_add": ["qianjiang_oilcity_2026", "qianjiang_route_2025", "qianjiang_cultural_2026"]
    },
    "HBI-QJ-003": {"source_keys_add": ["qianjiang_route_2025"]},
    "HBI-QJ-005": {"source_keys_add": ["qianjiang_route_2025", "qianjiang_cultural_2026"]},
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
        "工业遗产实体、工业文化景观、工业旅游相关场景、档案文献和待核验线索分层记录。"
        "文化证据字段只记录来源中明确出现的载体、技术、社会记忆和利用状态，未核实内容保持待核。"
    )
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_d_records={len(NEW_RECORDS)} wave_d_sources={len(NEW_SOURCES)} "
        f"total_records={len(records)} total_sources={len(sources)} updates={len(UPDATES)}"
    )


if __name__ == "__main__":
    main()
