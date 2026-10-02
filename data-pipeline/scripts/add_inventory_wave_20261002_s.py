from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "ezhou_fourth_survey_new_discovery_2025": {
        "source_type": "municipal_museum_fourth_cultural_relic_survey",
        "title": "鄂州市开展第四次文物普查新发现文物专项调查",
        "org": "鄂州博物馆",
        "pub_date": "2025-04-24",
        "url": "https://ezbwg.com/ReadNews.asp?NewsID=2570",
        "authority": "A",
        "notes": "鄂州博物馆报道市级新发现文物专项调查启动，明确重点关注历史建筑、革命纪念地和其他资源密集区域，全面搜集各行业遗产线索并实施地毯式普查；本来源只作为鄂州覆盖依据，不替代具体对象名录或现场档案。",
    },
    "shiyan_fourth_survey_industrial_2025": {
        "source_type": "municipal_media_fourth_cultural_relic_survey",
        "title": "十堰新发现文物点924处",
        "org": "十堰晚报（十堰日报社）",
        "pub_date": "2025-10-28",
        "url": "https://sywb.10yan.com/html/20251028/207097.html",
        "authority": "B",
        "notes": "十堰晚报报道第四次全国文物普查新发现文物点924处，开展三线建设军工遗产、襄渝铁路和老旧人防工程等专项调查；本来源用于覆盖审计和后续对象检索，不把专项调查总量写成工业遗产名录。",
    },
    "jiangxia_newwu_li_list_2022": {
        "source_type": "district_government_relic_register",
        "title": "江夏区核定为文物保护单位的不可移动文物情况",
        "org": "武汉市江夏区人民政府",
        "pub_date": "2022-09-22",
        "url": "https://www.jiangxia.gov.cn/xxgk_22343/xxgkml_22349/gysyjs_71066/whty/202209/t20220922_2045962.shtml",
        "authority": "A",
        "notes": "江夏区政府名录列新屋李铸造遗址，时代为宋代、地点为山坡街、面积约10000平方米、2011年核定为市级文物保护单位。",
    },
    "wuhan_newwu_li_scope_2020": {
        "source_type": "municipal_government_relic_protection_notice",
        "title": "市人民政府关于公布部分市级文物保护单位保护范围和建设控制地带的通知",
        "org": "武汉市人民政府",
        "pub_date": "2020-03-16",
        "url": "https://www.wuhan.gov.cn/zwgk/xxgk/zfwj/szfwj/202003/t20200316_973960.shtml",
        "authority": "A",
        "notes": "武汉市政府通知明确新屋李铸造遗址位于江夏区山坡乡建国村新屋李湾东南部美山南坡，保护范围为遗址本体外延10米，建设控制地带为保护范围外延20米，并区分遗址I区、II区。",
    },
    "wuhan_exploration_machinery_2025": {
        "source_type": "municipal_urban_management_media",
        "title": "硚口“微更新”点亮城市边边角角",
        "org": "武汉市城市管理局（湖北日报报道）",
        "pub_date": "2025-10-31",
        "url": "https://cgw.wuhan.gov.cn/cgdt/cgsp/202510/t20251031_2670438.shtml",
        "authority": "A",
        "notes": "武汉市城市管理局转载报道明确韩家墩街道简易路一处空间为原武汉探矿机械厂旧址，老厂房修缮后保留历史风貌并与社区公共空间更新相连；报道没有给出厂区完整边界和名录认定，保留城市更新对象层级。",
    },
    "wuhan_exploration_land_registry_2023": {
        "source_type": "municipal_natural_resources_register",
        "title": "武汉市国有土地使用权公开信息（武汉探矿机械厂）",
        "org": "武汉市自然资源和城乡建设局",
        "pub_date": "2023-10-18",
        "url": "https://spxx.zrzyhgh.wuhan.gov.cn/wsbs/jgggjyh850.asp?cid=1501&dept_ID=UG050508000001&id=5&keyword=&page=2959",
        "authority": "A",
        "notes": "武汉市自然资源公开信息记录武汉探矿机械厂位于硚口区韩家墩街简易路50号、工业用地约25840.34平方米，为旧址地址和企业身份提供官方登记旁证。",
    },
    "wuhan_two_shipyard_renewal_2021": {
        "source_type": "municipal_government_urban_renewal_plan",
        "title": "武汉市城市更新与工业遗产活化利用项目表",
        "org": "武汉市人民政府",
        "pub_date": "2021-12-07",
        "url": "https://www.wuhan.gov.cn/zwgk/xxgk/zfgb/202112/P020211207629770417718.pdf",
        "authority": "A",
        "notes": "武汉市政府公报项目表将“江滩公园室内体育馆（原武汉二船厂老旧厂房）提档升级工程”列为城市更新项目；来源足以确认原二船厂老旧厂房及规划利用关系，但未提供建筑测绘、厂史和完成验收资料。",
    },
    "wuhan_mins_luzuofo_official_2026": {
        "source_type": "district_government_cultural_guide",
        "title": "卢作孚纪念馆与武汉抗战遗址介绍",
        "org": "武汉市江岸区人民政府",
        "pub_date": "2026-01-15",
        "url": "https://www.dxh.gov.cn/YXLKG_16692/wszl/202601/P020260115590032299860.pdf",
        "authority": "A",
        "notes": "江岸区政府文化资料确认鄱阳街7号为民生轮船公司汉口分公司旧址，现为卢作孚纪念馆，2013年列入武汉市第八批优秀历史建筑。",
    },
    "wuhan_mins_history_2024": {
        "source_type": "district_government_history_publication",
        "title": "民生轮船汉口公司旧址建筑探讨",
        "org": "武汉市江岸区人民政府（武汉文史资料）",
        "pub_date": "2024-05-09",
        "url": "https://www.dxh.gov.cn/YXLKG_16692/wszl/202402/P020240509222258152031.pdf",
        "authority": "A",
        "notes": "江岸区政府公开的《武汉文史资料》文章记录该址为四层西式建筑，约建于1923—1925年，并介绍卢作孚与民生实业的航运发展背景；具体产权、建筑构件清单和开放制度仍需现场核验。",
    },
    "hubei_worker_heritage_sites_2025": {
        "source_type": "provincial_media_worker_heritage_report",
        "title": "湖北工运旧址寻访整理报道：21处工运旧址集群",
        "org": "湖北省总工会/湖北日报",
        "pub_date": "2025-04-29",
        "url": "https://epaper.hubeidaily.net/pc/attachment/202504/29/62a02e64-a9d3-4aef-979a-b1586bbcd769.pdf",
        "authority": "B",
        "notes": "湖北工运旧址整理报道将汉口民生轮船公司汉口公司旧址、下陆机修厂工人俱乐部旧址和应城膏盐矿遗址列入21处工运旧址集群，并提供部分地址/纪念信息；作为工业文化档案的补充证据，不替代文物登记。",
    },
    "xialu_workers_club_2026": {
        "source_type": "district_government_red_heritage_report",
        "title": "百年前的老屋，时代不灭的印记——下陆机修厂工人俱乐部旧址",
        "org": "黄石市下陆区人民政府",
        "pub_date": "2026-05-20",
        "url": "https://www.xialuqu.gov.cn/jrxl/202606/t20260601_1331836.html",
        "authority": "A",
        "notes": "下陆区政府报道确认旧址位于胜利社区老下陆127号，是黄石地区第一个工人俱乐部和早期中共组织活动旧址；1962年列入黄石市第一批文物保护单位，2023年列入市级不可移动建筑类文物名录，2021年修缮并开展红色课堂活动。",
    },
    "huangshi_workers_club_2021": {
        "source_type": "municipal_culture_tourism_bureau_report",
        "title": "畅游黄石：百年罢工处 工人有力量——下陆机修厂工人俱乐部旧址",
        "org": "黄石市文化和旅游局（黄石图书馆）",
        "pub_date": "2021-10-15",
        "url": "https://hswhj.huangshi.gov.cn/xwzx/gzdt/202110/t20211015_843420.html",
        "authority": "A",
        "notes": "黄石市文旅局文章记录旧址约200多平方米、为套间式民房和木结构，保留早期生活工具及1962年文物保护单位保管执照，说明其与1923年下陆大罢工和工人运动的直接关系。",
    },
    "hubei_cppcc_gypse_salt_2014": {
        "source_type": "provincial_cppcc_history_publication",
        "title": "应城膏盐矿业史料整理",
        "org": "湖北省政协文史资料委员会",
        "pub_date": "2014-09-15",
        "url": "https://www.hbzx.gov.cn/49/2014-09-15/5988.html",
        "authority": "A",
        "notes": "湖北省政协文史资料记录应城膏盐矿业400余年历史，涵盖石膏、食盐生产及深加工、建国前后企业和矿区文史资料编辑工作，明确膏盐业对当地经济、社会和文化的长期影响。",
    },
    "forestry_mining_park_registry_2020": {
        "source_type": "national_government_mining_park_register",
        "title": "国家矿山公园基本情况一览表",
        "org": "国家林业和草原局",
        "pub_date": "2020-04-27",
        "url": "https://www.forestry.gov.cn/html/zrbh/zrbh_1475/20200427151920192889200/file/20200427152034557606418.pdf",
        "authority": "A",
        "notes": "国家林草部门公开名录登记湖北应城国家矿山公园，所在地应城市、面积300平方公里，矿种为膏矿、盐矿和温泉，为应城膏盐矿业景观及其公共展示体系提供国家公园登记依据。",
    },
    "hubei_salt_industry_2024": {
        "source_type": "provincial_economic_industry_report",
        "title": "孝感：深挖地方资源 县域经济发展电能澎湃——膏都盐海化身绿能高地",
        "org": "湖北省经济和信息化厅",
        "pub_date": "2024-12-02",
        "url": "https://jxt.hubei.gov.cn/bmdt/cyfz/202412/t20241202_5433936.shtml",
        "authority": "A",
        "notes": "湖北省经信厅报道应城盐化工业历史可追溯至明朝，保留大量盐穴并形成现代盐化工产业；废弃盐穴被用于压缩空气储能，体现资源型工业遗产的当代转化线索。",
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
        "HBI-WUHAN-055",
        "原武汉探矿机械厂旧址",
        "武汉市",
        "硚口区",
        "探矿机械制造",
        "city_planning",
        "武汉市城市更新与工业记忆对象；未见独立工业遗产名录认定",
        ["wuhan_exploration_machinery_2025", "wuhan_exploration_land_registry_2023"],
        "武汉市城市管理局报道确认韩家墩街道简易路一处空间为原武汉探矿机械厂旧址，老厂房修缮后保留历史风貌；自然资源公开信息记录厂址在简易路50号、工业用地约25840.34平方米。当前资料可以确认厂址和活化线索，但尚未取得完整厂史、厂区边界、建筑清单和独立名录认定，保持城市更新层级。",
        ev(
            "原探矿机械厂老厂房及简易路50号工业用地空间，报道仅确认部分老厂房保留历史风貌，建筑构件和设备目录待测绘",
            "探矿机械制造和硚口工业区生产记忆；产品谱系、设备型号、工艺流程和生产年代待企业档案核验",
            "硚口老工业区、探矿机械厂职工和周边居民的城市工业记忆；现有社区微更新为记忆保留提供公共空间入口",
            "工厂搬迁后旧址一度闲置，2025年报道确认部分老厂房修缮并与社区草坪、公共活动空间结合；完整保护边界和开放管理待核",
        ),
        aliases=["武汉探矿机械厂旧址", "探矿机械厂老厂房", "简易路50号探矿机械厂"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-WUHAN-056",
        "原武汉二船厂老旧厂房",
        "武汉市",
        "硚口区",
        "船舶制造与修造",
        "city_planning",
        "武汉市城市更新项目明确的原武汉二船厂老旧厂房；工业遗产线索，未见独立名录认定",
        ["wuhan_two_shipyard_renewal_2021"],
        "武汉市政府公报项目表将“江滩公园室内体育馆（原武汉二船厂老旧厂房）提档升级工程”列入城市更新项目，确认原二船厂老旧厂房与江滩公共空间的更新关系。现有公开资料未给出厂区年代、保存建筑编号、设备和项目验收状态，保留规划对象层级，不写成已认定工业遗产。",
        ev(
            "原武汉二船厂老旧厂房及江滩闸口周边工业空间；政府项目表未提供建筑测绘、船坞和设备清单，需现场核验",
            "船舶制造、修造和沿江工业生产的技术记忆尚缺厂志与设备档案，暂仅依据企业名称保留行业线索",
            "汉口沿江船舶工业、船厂职工和江滩社区记忆；公共体育空间更新可作为后续口述史和公众展示入口",
            "政府公报将原厂房列入室内体育馆提档升级工程，项目是否完工、原真性保留比例和开放方式待主管部门核验",
        ),
        aliases=["武汉二船厂旧址", "武汉第二船厂老厂房", "江滩公园原二船厂厂房"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-WUHAN-057",
        "汉口民生轮船公司旧址",
        "武汉市",
        "江岸区",
        "近代航运与民族工业",
        "municipal_historical_building",
        "武汉市第八批优秀历史建筑（2013）；尚未核定为文物保护单位",
        ["wuhan_mins_luzuofo_official_2026", "wuhan_mins_history_2024", "hubei_worker_heritage_sites_2025"],
        "江岸区政府资料确认鄱阳街7号为民生轮船公司汉口分公司旧址，建于1923—1925年，现为卢作孚纪念馆，2013年列入武汉市第八批优秀历史建筑；武汉文史资料和湖北工运旧址整理补充其建筑形制、民族航运史和抗战时期工业内迁抢运记忆。它是航运企业办公和工业文化传播节点，不等同于民生机器厂生产遗址。",
        ev(
            "鄱阳街7号四层西式建筑、原民生轮船公司汉口分公司办公空间及现卢作孚纪念馆展陈载体；建筑构件与保护范围需测绘核验",
            "民生实业由小型轮船发展为长江航运企业的组织、航运和内河物流技术记忆；公开文史资料记载其船舶与航线发展，具体档案全宗待核",
            "卢作孚、民族航运、1938年武汉工业设备抢运和民生职工记忆；湖北工运整理资料另记录纪念为搬迁献出生命的116名工人，需以原始档案复核",
            "现为卢作孚纪念馆并列入武汉市优秀历史建筑，承担公共展陈和城市记忆传播功能；开放制度、展陈更新与建筑本体保护状态待现场核验",
        ),
        aliases=["民生轮船公司汉口分公司旧址", "卢作孚纪念馆", "鄱阳街7号民生轮船旧址"],
        asset_kind="industrial_culture_site",
    ),
    rec(
        "HBI-WUHAN-058",
        "新屋李铸造遗址",
        "武汉市",
        "江夏区",
        "古代金属铸造",
        "provincial_heritage_related",
        "湖北省第九批省级文物保护单位（2025）；武汉市级文物保护单位（2011）",
        ["hubei_9th_relics_2025", "jiangxia_newwu_li_list_2022", "wuhan_newwu_li_scope_2020"],
        "湖北省政府第九批省级文物保护单位名单将新屋李铸造遗址列为宋代古遗址，地址为武汉市江夏区；江夏区政府名录补充其约10000平方米、2011年核定为市级文物保护单位；武汉市政府保护范围通知明确其位于山坡乡建国村新屋李湾东南部美山南坡，保护范围外延10米、建设控制地带外延20米并分I区、II区。具体炉址、金属种类、产品和考古出土物待专业报告补证。",
        ev(
            "宋代铸造遗址本体及I区、II区考古空间，约10000平方米；公开保护文件未列出炉址、炉渣、模具和出土物清单，需考古调查补录",
            "宋代金属铸造生产活动是可确认的工业考古主题；金属种类、炉型、燃料、产品与工艺链不能依据现有名录臆测，待考古报告",
            "江夏山坡街地方手工业和古代生产景观记忆；现有来源主要是文保名录和保护范围文件，社区口述、技艺谱系和展示状况待补",
            "已纳入第九批省级文物保护单位并划定保护范围及建设控制地带；现场保存、展示利用、周边建设影响和日常管理状态待核",
        ),
        aliases=["新屋李铸造遗址（宋代）", "江夏新屋李铸造遗址"],
        asset_kind="industrial_archaeology",
    ),
    rec(
        "HBI-HS-037",
        "下陆机修厂工人俱乐部旧址",
        "黄石市",
        "下陆区",
        "矿冶工业与工运文化",
        "municipal_relic_related",
        "黄石市第一批文物保护单位（1962）；市级不可移动建筑类文物名录（2023）",
        ["xialu_workers_club_2026", "huangshi_workers_club_2021", "hubei_worker_heritage_sites_2025"],
        "下陆区政府和黄石市文旅局资料确认旧址位于胜利社区老下陆127号，是黄石地区第一个工人俱乐部、早期中共组织活动旧址和下陆机修厂工人运动节点；1962年列入黄石市第一批文物保护单位，2023年列入市级不可移动建筑类文物名录。公开资料记录旧址约200多平方米、木结构套间式民房、早期生活工具和2021年修缮利用。作为矿冶工业社会文化遗存记录，不新增独立工业遗产认定。",
        ev(
            "胜利社区老下陆127号约200多平方米木结构套间式民房、青砖黛瓦建筑、早期生活工具和1962年文物保护单位保管执照",
            "下陆机修厂与大冶铁矿矿冶生产相配套的机修工人组织记忆；旧址本身不是完整机修车间，具体设备和工艺应与矿区档案分开核验",
            "1922年工人俱乐部成立、1923年下陆大罢工、黄石早期工运和中共组织活动记忆；旧址承载工人权益、技术交流和集体文化活动叙事",
            "2021年修缮后作为社区红色课堂和研学点使用，区政府报道记载每年有百余批次参观；展陈内容、开放时间和建筑安全状况待持续核验",
        ),
        aliases=["下陆机修厂工人俱乐部旧址（大冶铁矿工人俱乐部）", "大冶铁矿工人俱乐部旧址", "下陆湾工人俱乐部"],
        asset_kind="industrial_social_site",
    ),
    rec(
        "HBI-XG-012",
        "应城膏盐矿遗址群",
        "孝感市",
        "应城市",
        "膏盐采掘与盐化工",
        "industrial_landscape_related",
        "应城国家矿山公园矿业景观；省级工运旧址整理对象；尚未见单独工业遗产名录认定",
        ["hubei_cppcc_gypse_salt_2014", "forestry_mining_park_registry_2020", "hubei_worker_heritage_sites_2025", "hubei_salt_industry_2024"],
        "湖北省政协文史资料记录应城膏盐矿业400余年历史，涵盖石膏、食盐生产和深加工；国家林草部门名录登记应城国家矿山公园（膏矿、盐矿和温泉，面积300平方公里）；湖北工运整理资料将应城膏盐矿遗址列入工运旧址集群；省经信厅报道补充明代以来盐化工业、盐穴和废弃盐穴储能利用。该条表达跨矿区工业文化景观，具体矿洞、码头、晒盐台、厂矿边界和档案全宗仍需普查拆分。",
        ev(
            "应城膏盐矿区、矿山公园和膏盐生产景观；公开来源确认国家矿山公园登记和膏盐产业空间，但具体矿洞、盐穴、运输设施和生产工具清单待现场普查",
            "明代以来石膏开采、食盐生产、深加工和现代井矿盐化工技术连续谱系；省政协文史资料记录企业与矿区史料编纂，具体工艺节点待档案和设备核验",
            "膏盐业作为应城经济命脉和地方产业身份、矿工群体、工运历史与盐化城市生活记忆；工运旧址整理资料提供社会记忆线索，口述史仍需补录",
            "应城国家矿山公园提供公共展示载体，现代盐化工产业持续运行，废弃盐穴转化为压缩空气储能设施；矿区保护分区、开放线路和生产安全边界待核",
        ),
        aliases=["应城膏盐矿遗址", "应城膏盐矿业遗产", "应城国家矿山公园矿业遗迹", "膏都盐海工业文化景观"],
        asset_kind="industrial_landscape",
        related_inventory_ids=["HBI-XG-001", "HBI-XG-004"],
    ),
]


def merge_unique(row: dict[str, Any], key: str, values: list[str]) -> None:
    existing = row.setdefault(key, [])
    for value in values:
        if value not in existing:
            existing.append(value)


def patch_record(
    row: dict[str, Any],
    *,
    source_keys: list[str],
    aliases: list[str] | None = None,
    evidence: dict[str, str] | None = None,
    notes: str | None = None,
    related_inventory_ids: list[str] | None = None,
) -> None:
    merge_unique(row, "source_keys", source_keys)
    if aliases:
        merge_unique(row, "aliases", aliases)
    if evidence is not None:
        row["cultural_evidence"] = evidence
    if notes is not None:
        row["notes"] = notes
    if related_inventory_ids:
        merge_unique(row, "related_inventory_ids", related_inventory_ids)
    row["record_status"] = "source_confirmed"


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

    targets = data.setdefault("research_targets", {})
    coverage_sources = targets.setdefault("coverage_sources", [])
    for key in ["ezhou_fourth_survey_new_discovery_2025", "shiyan_fourth_survey_industrial_2025"]:
        if key not in coverage_sources:
            coverage_sources.append(key)

    patch_record(
        existing_by_id["HBI-HS-003"],
        source_keys=["hubei_worker_heritage_sites_2025"],
        aliases=["大冶钢铁厂工会所在地旧址", "大冶钢厂工人俱乐部旧址"],
        evidence=ev(
            "大冶钢厂职工俱乐部旧址及厂区工会活动空间，具体建筑构件和保护边界待现场测绘",
            "钢铁企业职工文化、工会组织和冶金工业社会生产体系的集体记忆；俱乐部建筑不是完整生产设备遗存",
            "大冶钢厂工会、职工俱乐部、产业工人组织和黄石钢铁城市记忆；湖北工运整理资料将其作为工运节点记录",
            "黄石市首批工业遗产与市级文物相关对象，现状由企业和文保主管部门管理；开放、展陈与厂区进入制度待核",
        ),
        notes="黄石工业遗产名录将其列为大冶钢厂职工俱乐部旧址；湖北工运整理资料另称“大冶钢铁厂工会所在地旧址”，两种名称作为同一职工文化设施节点的别名保存。具体建筑范围、档案和现行保护责任待核。",
    )
    patch_record(
        existing_by_id["HBI-XG-001"],
        source_keys=["hubei_cppcc_gypse_salt_2014"],
        aliases=["应城石膏矿一分矿", "应城膏盐矿遗址群组成项"],
        related_inventory_ids=["HBI-XG-012"],
        notes="省文旅厅省级文物名录将应城石膏矿第一分矿旧址列为1950年近现代重要史迹；湖北省政协膏盐矿业史料补充应城膏盐业400余年历史和石膏开采、食盐及深加工谱系。本条继续表达可独立识别的一分矿旧址，与跨矿区膏盐矿遗址群HBI-XG-012建立组成关系，矿井、设备和保护边界待核。",
    )
    patch_record(
        existing_by_id["HBI-XG-004"],
        source_keys=["hubei_cppcc_gypse_salt_2014"],
        related_inventory_ids=["HBI-XG-012"],
        notes="湖北应城石膏股份有限公司档案列入第三批湖北省档案文献遗产；湖北省政协膏盐矿业史料进一步说明应城膏盐业400余年历史和建国前后企业史料整理。档案条目与应城膏盐矿遗址群HBI-XG-012、应城石膏矿一分矿旧址HBI-XG-001形成档案—景观—实体关联。",
    )
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_s_sources={len(NEW_SOURCES)} added_records={len(NEW_RECORDS)} "
        f"total_records={len(records)} total_sources={len(sources)} patched_records=3"
    )


if __name__ == "__main__":
    main()
