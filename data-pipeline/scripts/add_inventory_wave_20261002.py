"""Add the next source-bound Hubei industrial heritage inventory wave.

This is a reproducible, idempotent data migration.  It deliberately keeps
candidate, planning, enterprise-memory, and formally recognised records in
their original layers; it does not turn a planning mention into a formal
designation.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "data-pipeline" / "enrichment" / "hubei_inventory.json"


NEW_SOURCES = {
    "shiyan_car_survey_2018": {
        "source_type": "government_reply",
        "title": "关于湖北省政协十二届一次会议第20180329号提案的答复",
        "org": "湖北省文化和旅游厅",
        "pub_date": "2020-08-05",
        "url": "https://wlt.hubei.gov.cn/zfxxgk/fdzdgknr/qtzdgknr/jytabl/zxwyta/202008/t20200805_2742255.shtml",
        "authority": "A",
        "notes": "官方答复记载十堰2016年完成东风基地老厂区摸底普查，形成不可移动保护对象100处、可移动设备和工艺产品300项，并制定保护利用办法；具体对象仍需回到普查档案逐项核验。",
    },
    "dongfeng_museum_2022": {
        "source_type": "enterprise_official_news",
        "title": "东风汽车博物馆正式开工建设",
        "org": "东风汽车集团有限公司",
        "pub_date": "2022-12-09",
        "url": "https://www.dfmc.com.cn/news/company/news_20221209_2210.html",
        "authority": "B",
        "notes": "东风公司官方报道确认博物馆利用原二汽41厂车架厂和43厂总装配厂旧厂房建设，并记载老厂房、老车间、老设备承载的企业记忆。",
    },
    "dongfeng_museum_2025": {
        "source_type": "enterprise_official_news",
        "title": "东风汽车博物馆在十堰盛大开馆",
        "org": "东风汽车集团有限公司",
        "pub_date": "2025-03-27",
        "url": "https://www.dfmc.com.cn/news/company/news_20250327_1025.html",
        "authority": "B",
        "notes": "东风公司官方开馆报道确认博物馆依托二汽历史厂区改造，约2.1万平方米，展出2000余件展品和逾万幅图片，设置三线岁月等专题展区。",
    },
    "shiyan_natural_resources_2026": {
        "source_type": "government_media",
        "title": "唤醒“沉睡土地” 激活发展动能——十堰市探索低效用地活化利用新路径纪实",
        "org": "湖北省自然资源厅/十堰日报",
        "pub_date": "2026-03-12",
        "url": "https://zrzyt.hubei.gov.cn/bmdt/sxdt/202603/t20260312_5891298.shtml",
        "authority": "A",
        "notes": "省自然资源厅转载的官方报道逐项记录44厂、45厂、原东风轮胎厂、20厂和放马坪文化古巷的保存、搬迁、再利用或工业记忆状态。",
    },
    "shiyan_44_university_2026": {
        "source_type": "university_fieldwork",
        "title": "追寻东风工业历史 触摸城市更新脉搏",
        "org": "湖北工业职业技术学院",
        "pub_date": "2026-02-01",
        "url": "https://news.hbgyzy.edu.cn/info/1003/17550.htm",
        "authority": "B",
        "notes": "高校现场调研确认原东风44厂（二汽车厢厂）旧址、1969年建厂背景和保留老厂房结构的活化利用。",
    },
    "shiyan_memory_2025": {
        "source_type": "official_media",
        "title": "重温峥嵘岁月 传承奋斗精神",
        "org": "十堰文明网",
        "pub_date": "2025-06-24",
        "url": "https://hbsy.wenming.cn/w/wmcs/202506/t20250624_8948754.shtml",
        "authority": "B",
        "notes": "官方文明网报道确认原东风64厂职工活动中心改造为东风故里史料陈列馆，展陈车模、手风琴、旧报纸、老照片、访谈和三线建设日记等。",
    },
    "shiyan_suspension_story": {
        "source_type": "media_reprint",
        "title": "十堰工业遗产保护利用：未来将建设国际博物馆之城",
        "org": "搜狐转载（线索来源）",
        "pub_date": "2016",
        "url": "https://www.sohu.com/a/129386535_426335",
        "authority": "C",
        "notes": "仅作为东风悬架弹簧厂老厂区候选线索和规划语境来源；正式认定、挂牌编号、边界与现存物项必须回到十堰普查档案核验。",
    },
    "jingmen_330_cement": {
        "source_type": "official_media",
        "title": "探访湖北三三〇水泥厂纪念馆 见证历史传承初心",
        "org": "中国新闻网/荆楚网",
        "pub_date": "2021-04-27",
        "url": "https://m.cnhubei.com/content/2021-04/27/content_13762346.html",
        "authority": "B",
        "notes": "公开报道记载三三〇水泥厂1971年为葛洲坝工程建设动工、1975年建成首条生产线，并由退休职工活动中心改建纪念馆，保存800余件藏品和1000余张老照片。",
    },
    "jingmen_330_memory_2025": {
        "source_type": "official_media",
        "title": "“葛二代”马罡：我用两千多个日夜，留住父辈的水泥厂青春",
        "org": "荆门新闻网/荆楚网",
        "pub_date": "2025-12-15",
        "url": "https://www.cnhubei.com/content/2025-12/15/content_19726452.html",
        "authority": "B",
        "notes": "公开报道补充三三〇水泥厂退休职工活动中心纪念馆的物件征集、厂史叙事和职工家庭记忆；页面可能存在跳转限制，发布前需保留网页快照或馆方授权。",
    },
    "jingmen_hongtu_company": {
        "source_type": "government_news",
        "title": "荆门宏图公司荣获湖北省第九届长江质量奖",
        "org": "湖北省经济和信息化厅/荆门市经信局",
        "pub_date": "2023-02-17",
        "url": "https://jxt.hubei.gov.cn/bmdt/qyfc/202302/t20230217_4552084.shtml",
        "authority": "A",
        "notes": "省经信厅官方报道确认荆门宏图特种飞行器制造有限公司始建于1971年，前身为中国航空工业宏图飞机制造厂。旧厂区边界和可开放文物仍待核验。",
    },
    "jingmen_power_2025": {
        "source_type": "enterprise_tender",
        "title": "长源电力荆门公司2×640MW超临界燃煤机组集控室智能化改造工程公开招标公告",
        "org": "国家能源集团国能e招",
        "pub_date": "2025-08-29",
        "url": "https://www.chnenergybidding.com.cn/bidweb/001/001002/001002002/20250829/f0f8529d-5c52-4ca2-8b95-551ca00aa142.html",
        "authority": "B",
        "notes": "官方招标公告记载荆门发电公司始建于1976年，一、二期机组已关停并完全拆除；本记录只保存历史厂址和工业记忆，不把已拆除机组写成现存遗存。",
    },
    "ezhou_15th_plan_2026": {
        "source_type": "government_plan",
        "title": "鄂州市国民经济和社会发展第十五个五年规划纲要",
        "org": "鄂州市人民政府",
        "pub_date": "2026-05-20",
        "url": "https://www.ezhou.gov.cn/gk/xxgkml/jhgh/fzgh/202605/t20260520_765137.html",
        "authority": "A",
        "notes": "市政府规划部署西雷山工业遗址文化传承与焕新工程，并提出利用鄂钢、老水泥厂策划工业文化观光、研学和体验产品。",
    },
    "ezhou_steel_history_2023": {
        "source_type": "government_media",
        "title": "从“钢城”到“港城”——鄂州建市40周年系列报道之三",
        "org": "鄂州市人民政府",
        "pub_date": "2023-08-16",
        "url": "https://www.ezhou.gov.cn/zt/zdzt/hwjsl/202309/t20230911_574554.html",
        "authority": "A",
        "notes": "市政府历史报道记载原鄂州市八一钢铁厂搬迁、西山转型和鄂钢“英雄炉”544高炉拆毁；544高炉记录作为已消失工业文化记忆保留。",
    },
    "pufang_national_batch1": {
        "source_type": "ministry_register",
        "title": "工业和信息化部关于公布第一批国家工业遗产名单的通告及附件",
        "org": "工业和信息化部",
        "pub_date": "2017-12-22",
        "url": "https://www.miit.gov.cn/jgsj/zfs/gywh/art/2020/art_74318eb7ebee489b8e7e097f20ede011.html",
        "authority": "A",
        "notes": "第一批国家工业遗产官方通告及附件；蒲纺组成项名称按附件核心物项表拆分，拆分记录不是独立国家认定。",
    },
    "xg_hanchuan_auto_2026": {
        "source_type": "official_media",
        "title": "老厂房“又一春”：汉川马口镇以“微更新”唤醒三线工业遗存",
        "org": "湖北日报新闻客户端",
        "pub_date": "2026-06-28",
        "url": "https://news.hubeidaily.net/mobile/c_5692565.html",
        "authority": "B",
        "notes": "湖北日报报道确认马口省汽修老厂房红砖车间、钢构建筑保存及微更新项目；原厂名称、建设沿革和现存建筑清单需进一步档案核验。",
    },
    "xg_hanchuan_3509_2025": {
        "source_type": "official_media",
        "title": "梦回几代芳华 汉川马口3509“容光”焕发",
        "org": "湖北日报新闻客户端",
        "pub_date": "2025-10-31",
        "url": "https://news.hubeidaily.net/mobile/c_4719806.html",
        "authority": "B",
        "notes": "湖北日报报道确认3509纺织厂始建于1950年、前身为解放军3509工厂，并记录老礼堂、工人俱乐部、社区生活和军工纺织文化传承。",
    },
    "hg_hongan_repair_2022": {
        "source_type": "government_register",
        "title": "湖北省不可移动革命文物名录（第二批）",
        "org": "湖北省文化和旅游厅",
        "pub_date": "2022-12-08",
        "url": "https://wlt.hubei.gov.cn/zfxxgk/zc/qtzdgkwj/202212/P020221208373333318248.pdf",
        "authority": "A",
        "notes": "省文旅厅官方名录将红安县红一军修械所旧址列为红安县文物保护单位；这是军工维修类革命文物，工业文化属性需与普通革命遗址区分研究。",
    },
    "xiantao_piston_ring_2025": {
        "source_type": "official_media_memory",
        "title": "一个老厂的故事",
        "org": "极目新闻",
        "pub_date": "2025-06-16",
        "url": "https://www.ctdsb.net/c1664_202506/2462918.html",
        "authority": "B",
        "notes": "极目新闻结合老工人和作者回访记载沔阳县活塞环厂1958年由张沟农机修配厂起步、遗留车间和高炉等工业记忆；现址与建筑范围需现场测绘。",
    },
    "enshi_lai_feng_power_2021": {
        "source_type": "government_project_plan",
        "title": "省文化和旅游厅关于印发2021年全省文化和旅游及康养产业招商引资工作方案的通知",
        "org": "湖北省文化和旅游厅",
        "pub_date": "2021-01-05",
        "url": "https://wlt.hubei.gov.cn/zfxxgk/fdzdgknr/zdjsxm/202201/t20220105_3952430.shtml",
        "authority": "A",
        "notes": "省文旅厅项目表明确记载来凤刘家坝老发电房、水渠及狮子桥水电站由张富清带领群众修建，并提出修复打造；正式文保层级和现存范围待核。",
    },
    "xiangyang_3line_university": {
        "source_type": "university_fieldwork",
        "title": "我校学子连续三年探访三线建设遗址 推动工业遗产活化利用",
        "org": "武汉科技大学",
        "pub_date": "2025-01-23",
        "url": "https://www.wust.edu.cn/info/1591/440672.htm",
        "authority": "B",
        "notes": "高校现场调研逐名记录襄阳汽车轴承厂旧址、宏伟机械厂旧址、卫东机械厂，并访谈居民和三线建设亲历者；记录为研究候选，不替代正式名录。",
    },
    "xiangyang_15th_plan_2026": {
        "source_type": "government_plan_news",
        "title": "襄阳市国民经济和社会发展第十五个五年规划纲要",
        "org": "襄阳市人民政府/襄阳日报",
        "pub_date": "2026-05-08",
        "url": "https://www.hj.cn/content/2026-05/08/content_20124684.html",
        "authority": "A",
        "notes": "规划新闻明确以襄阳棉纺厂等三线工业遗产打造生活秀带，并将襄城区610厂、609研究所等22个老旧厂区和公共空间纳入改造利用。",
    },
    "yichang_shipyard_2026": {
        "source_type": "government_news",
        "title": "文旅融合 破圈出彩 宜昌奋力打造世界知名文化旅游目的地",
        "org": "宜昌市人民政府",
        "pub_date": "2026-03-06",
        "url": "https://www.yichang.gov.cn/html/zhengwuyizhantong/zhengwuzixun/jinriyaowen/2026/0306/1075700.html",
        "authority": "A",
        "notes": "市政府报道确认始建于1956年的宜昌船厂旧址正在实施长江·西坝旅游岛龙园老船厂活化改造；原厂区边界和保留物项需专项测绘。",
    },
    "yichang_wufeng_yihong_2025": {
        "source_type": "government_news",
        "title": "茶厂工业遗址沉浸秀演绎茶香与民俗",
        "org": "宜昌市人民政府/三峡日报",
        "pub_date": "2025-07-29",
        "url": "https://www.yichang.gov.cn/html/zhengwuyizhantong/zhengwuzixun/jinriyaowen/2025/0729/1070857.html",
        "authority": "A",
        "notes": "市政府页面确认五峰宜红茶工业遗产精制车间为省级文保单位组成核心，并记载沉浸式演艺和展示馆活化利用；精制车间作为组成项单列。",
    },
    "yichang_industrial_shoreline_2026": {
        "source_type": "government_media",
        "title": "从“灰岸线”到“绿风景”宜昌的绿色转型实践",
        "org": "湖北省自然资源厅/中国网",
        "pub_date": "2026-04-16",
        "url": "https://zrzyt.hubei.gov.cn/bmdt/sxdt/202604/t20260416_5916203.shtml",
        "authority": "A",
        "notes": "省自然资源厅报道确认宜昌磨盘港码头原为磷矿露天堆场，保留传送带钢架、旧仓库和废弃反应釜并再生为灯塔广场；具体行政区和遗产边界待核。",
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
    district: str | None = None,
    aliases: list[str] | None = None,
    related_heritage_ids: list[str] | None = None,
    related_inventory_ids: list[str] | None = None,
) -> dict:
    row = {
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
    if related_heritage_ids:
        row["related_heritage_ids"] = related_heritage_ids
    if related_inventory_ids:
        row["related_inventory_ids"] = related_inventory_ids
    return row


NEW_RECORDS = [
    rec("HBI-SY-005", "原二汽车架厂（41厂）旧厂房", "十堰市", "汽车工业", "enterprise_heritage", "东风汽车博物馆依托的企业工业遗存", ["dongfeng_museum_2022", "dongfeng_museum_2025"], "东风公司官方报道确认41厂旧厂房被纳入东风汽车博物馆一期；记录保留企业遗存身份，馆区边界和原设备清单仍需测绘。", {"material_carriers": "原二汽车架厂旧厂房、车间与老设备", "technical_memory": "汽车车架制造及二汽总装体系中的专业化分工", "social_memory": "东风建设者、产业工人和城市汽车记忆", "current_use_or_loss": "改造为东风汽车博物馆一期展陈和公共文化空间"}, aliases=["41厂", "原二汽车架厂"]),
    rec("HBI-SY-006", "原二汽总装配厂（43厂）旧厂房", "十堰市", "汽车工业", "enterprise_heritage", "东风汽车博物馆依托的企业工业遗存", ["dongfeng_museum_2022", "dongfeng_museum_2025", "shiyan_natural_resources_2026"], "东风公司官方资料确认43厂总装配厂旧厂房为博物馆二期依托；省自然资源厅报道补充其总装车间改造和工业文脉展示。", {"material_carriers": "原43厂总装配车间及二汽历史厂区", "technical_memory": "汽车总装工艺、生产组织和整车下线记忆", "social_memory": "东风职工、援建队伍和十堰汽车城成长记忆", "current_use_or_loss": "东风汽车博物馆及相关文旅公共空间"}, aliases=["43厂", "原二汽总装配厂"]),
    rec("HBI-SY-007", "原东风汽车公司44厂（二汽车厢厂）旧址", "十堰市", "汽车工业", "enterprise_heritage", "企业旧址活化利用对象", ["shiyan_44_university_2026", "shiyan_natural_resources_2026"], "高校现场调研和省自然资源厅报道均确认44厂（二汽车厢厂）旧址；1969年建厂、2021年搬迁后保留车间桁架和斑驳墙面并活化为四四厢遇街区。", {"material_carriers": "老车间桁架、红砖墙面和原厂区空间", "technical_memory": "车厢制造与二汽整车生产线专业协作", "social_memory": "车厢厂职工、家庭和四四厂城市生活记忆", "current_use_or_loss": "四四厢遇创意街区，需继续记录原构件和改造边界"}, district="茅箭区", aliases=["44厂", "四四厂", "四四厢遇"]),
    rec("HBI-SY-008", "原东风公司64厂职工活动中心（东风故里史料陈列馆）", "十堰市", "汽车工业", "enterprise_heritage", "企业职工活动中心改造的工业文化展示空间", ["shiyan_memory_2025"], "十堰文明网确认原64厂职工活动中心改造为东风故里史料陈列馆，包含车模、手风琴、旧报纸、老照片、人物访谈和三线建设日记等文化载体。", {"material_carriers": "原64厂职工活动中心建筑和展陈实物", "technical_memory": "汽车工业建设工具、锻压设备和生产组织记忆", "social_memory": "职工活动、文艺宣传队、援建工人和社区生活", "current_use_or_loss": "史料陈列馆与沉浸式教育空间"}, district="张湾区", aliases=["64厂职工活动中心", "东风故里史料陈列馆"]),
    rec("HBI-SY-009", "原东风公司45厂老厂区", "十堰市", "汽车工业", "research_candidate", "来源确认的搬迁老厂区候选", ["shiyan_natural_resources_2026"], "官方报道确认45厂企业腾退后整体搬入工业新区；原址已进入城市开发，记录用于保存厂址沿革和工业记忆，不把已拆或改建部分写成现存遗产。", {"material_carriers": "原45厂厂区历史空间和厂址档案（现存边界待核）", "technical_memory": "东风专业厂分工与退城进园转型", "social_memory": "45厂职工和城市搬迁记忆", "current_use_or_loss": "原厂址已转入城市开发，现存建筑和档案待核"}, district="张湾区", aliases=["45厂老厂区"]),
    rec("HBI-SY-010", "原东风公司20厂（通用铸锻厂）旧址", "十堰市", "汽车铸造工业", "research_candidate", "来源确认的企业旧址候选", ["shiyan_natural_resources_2026"], "省自然资源厅报道确认20厂旧址转型为燕京精酿啤酒张湾工厂；生产建筑、铸锻设备和厂史档案需专项核验。", {"material_carriers": "原20厂铸锻厂区、车间和设备遗存", "technical_memory": "汽车铸造、锻造和零部件制造工艺记忆", "social_memory": "专业厂职工、厂区生活和东风工业社区", "current_use_or_loss": "部分厂区转为啤酒生产与体验空间，原遗存边界待核"}, district="张湾区", aliases=["20厂", "东风通用铸锻厂"]),
    rec("HBI-SY-011", "东风悬架弹簧厂老厂区", "十堰市", "汽车零部件工业", "research_candidate", "普查线索确认的企业旧址候选", ["shiyan_car_survey_2018", "shiyan_suspension_story"], "十堰专项答复确认全市汽车工业文化遗产普查规模；媒体转载将悬架弹簧厂老厂区列为汽车工业遗产规划线索，正式挂牌、边界和现存设备必须回到官方普查档案核验。", {"material_carriers": "悬架弹簧厂老厂房、生产设备和厂区构筑物（待核）", "technical_memory": "钢板弹簧与汽车悬架零部件制造", "social_memory": "零部件产业工人、专业厂组织和城市汽车记忆", "current_use_or_loss": "现状和保护利用主体待核，不进入已认定名录"}, district="张湾区", aliases=["东风悬架弹簧厂", "原二汽钢板弹簧厂"]),
    rec("HBI-SY-012", "原东风轮胎厂旧址", "十堰市", "汽车轮胎工业", "research_candidate", "来源确认的搬迁老厂区候选", ["shiyan_natural_resources_2026"], "官方报道确认原东风轮胎厂32.73万平方米土地已转为物流园；记录保留轮胎工业厂址和城市转型记忆，现存建筑、设备与档案待核。", {"material_carriers": "原轮胎厂厂区和生产空间（现存构件待核）", "technical_memory": "汽车轮胎生产和专业化配套体系", "social_memory": "轮胎厂职工及退城进园转型记忆", "current_use_or_loss": "土地已转为物流仓储用途，原遗存状态待核"}, district="张湾区", aliases=["东风轮胎厂老厂区"]),
    rec("HBI-SY-013", "东风故里放马坪文化古巷", "十堰市", "汽车工业社区", "city_planning", "工业遗产保护与城市功能升级对象", ["shiyan_natural_resources_2026"], "省自然资源厅报道确认放马坪文化古巷保存东风职工生产生活记忆，保留马灯、芦席棚等工业文化符号，是工业遗存与社区生活融合的文化空间。", {"material_carriers": "青石板巷、老职工生活区、马灯和芦席棚等记忆物件", "technical_memory": "东风三线建设的生产—生活组织方式", "social_memory": "职工家属区、社区日常和城市汽车城成长记忆", "current_use_or_loss": "东风故里街区公共文化与社区更新空间"}, district="张湾区", aliases=["放马坪文化古巷", "东风故里街区"]),
    rec("HBI-JM-009", "三三〇水泥厂纪念馆（原职工活动中心）", "荆门市", "建材工业", "enterprise_heritage", "企业纪念馆及职工社会记忆载体", ["jingmen_330_cement", "jingmen_330_memory_2025"], "公开报道确认三三〇水泥厂为葛洲坝工程配套建设、1975年建成首条生产线；原退休职工活动中心改建为纪念馆，作为葛洲坝水泥厂老生产区的文化记忆节点单列。", {"material_carriers": "原职工活动中心建筑、厂史展柜和老物件", "technical_memory": "大坝特种水泥生产、建设组织和建材工业技术", "social_memory": "葛洲坝水泥职工、子弟和退休人员共同记忆", "current_use_or_loss": "三三〇水泥厂纪念馆，藏品和开放授权需继续核实"}, aliases=["三三〇水泥厂纪念馆", "330水泥厂纪念馆"]),
    rec("HBI-JM-010", "宏图飞机制造厂旧址（国营322厂）", "荆门市", "航空军工工业", "research_candidate", "来源确认的三线航空工业候选", ["jingmen_hongtu_company"], "省经信厅官方报道确认宏图公司始建于1971年、前身为中国航空工业宏图飞机制造厂；国营322厂旧厂区边界、原生产建筑与航空实物待核。", {"material_carriers": "宏图飞机制造厂旧厂区、厂房和航空产品档案（待核）", "technical_memory": "航空制造技术向压力容器和能源装备转型的企业谱系", "social_memory": "三线航空工业职工、军转民和企业转型记忆", "current_use_or_loss": "企业仍在延续生产，旧址组成与开放边界待核"}, aliases=["宏图飞机制造厂", "322厂"]),
    rec("HBI-JM-011", "荆门发电厂历史厂址（一期、二期机组工业记忆）", "荆门市", "电力能源工业", "research_candidate", "历史厂址与已拆机组工业记忆", ["jingmen_power_2025"], "国家能源集团官方招标公告确认荆门发电公司1976年始建，一、二期机组已关停并完全拆除；本条不把拆除设备写成现存遗产。", {"material_carriers": "一期、二期机组厂址和电厂档案（现存边界待核）", "technical_memory": "燃煤火电机组、控制室和电力系统建设记忆", "social_memory": "电厂职工、家属区和荆门工业区成长记忆", "current_use_or_loss": "一、二期机组已拆除，三期仍运行，历史物项待档案核验"}, aliases=["荆门热电厂旧址", "国能长源荆门发电公司一期二期"]),
    rec("HBI-JM-012", "荆门工人文化宫旧址（民主街工业社区文化空间）", "荆门市", "工业社区文化", "city_planning", "老工业社区文化空间", ["jingmen_jinlongquan"], "省文旅厅相关报道记载民主街金龙泉啤酒厂旧址与工人文化宫共同记录荆门工业勃兴和城市转型；本条作为工人文化与工业社区载体单列，建筑沿革待核。", {"material_carriers": "工人文化宫建筑、公共文化设施及民主街历史空间", "technical_memory": "啤酒工业城市与产业工人公共文化组织", "social_memory": "工人俱乐部、社区文化和市民共同记忆", "current_use_or_loss": "历史街区修缮后的公共文化空间，现状产权与开放方式待核"}, aliases=["工人文化宫", "民主街工人文化宫"]),
    rec("HBI-EZ-010", "鄂钢“英雄炉”544高炉旧址（已拆除工业记忆）", "鄂州市", "钢铁工业", "research_candidate", "官方报道确认的消失工业文化载体", ["ezhou_steel_history_2023", "ezhou_15th_plan_2026"], "鄂州市政府历史报道明确记载鄂钢“英雄炉”544高炉已拆毁；本条用于保存高炉生产、工人记忆和城市转型证据，不代表仍有实体遗存。", {"material_carriers": "544高炉及其厂区空间（已拆除，档案和影像待收集）", "technical_memory": "钢铁高炉冶炼、鄂钢生产组织和技术改造", "social_memory": "鄂钢工人、退休职工与“钢城”城市记忆", "current_use_or_loss": "实体已拆除，转入工业文化记忆和城市更新叙事"}, district="鄂城区", aliases=["544高炉", "英雄炉"]),
    rec("HBI-XN-005", "蒲纺总厂纺织厂房（国家工业遗产组成项）", "咸宁市", "纺织工业", "national_cultural_relic_related", "第一批国家工业遗产二三四八蒲纺总厂核心物项组成项（非独立认定）", ["pufang_national_batch1"], "按工信部第一批国家工业遗产附件核心物项拆分；本条只表达蒲纺国家工业遗产组成关系，不新增独立认定。", {"material_carriers": "纺织生产厂房及建筑空间", "technical_memory": "棉纺生产线和工业厂房组织方式", "social_memory": "蒲纺职工、家属区和咸宁工业城市记忆", "current_use_or_loss": "现存状态、开放范围和设备清单待现场核实"}, related_heritage_ids=["HER-d0daf5a12b29"]),
    rec("HBI-XN-006", "蒲纺针织一厂俱乐部（国家工业遗产组成项）", "咸宁市", "纺织工业社区文化", "national_cultural_relic_related", "第一批国家工业遗产二三四八蒲纺总厂核心物项组成项（非独立认定）", ["pufang_national_batch1"], "官方附件将针织一厂俱乐部列为蒲纺核心物项；拆分用于补足产业工人公共文化载体，不表示其单独列入国家名录。", {"material_carriers": "针织一厂俱乐部建筑与公共文化空间", "technical_memory": "纺织厂区生产—生活—文体一体化组织", "social_memory": "工人俱乐部、文艺活动和职工社区记忆", "current_use_or_loss": "现存建筑、活动档案和开放状态待核"}, related_heritage_ids=["HER-d0daf5a12b29"]),
    rec("HBI-XN-007", "蒲纺空调冷却水塔遗址（国家工业遗产组成项）", "咸宁市", "纺织工业基础设施", "national_cultural_relic_related", "第一批国家工业遗产二三四八蒲纺总厂核心物项组成项（非独立认定）", ["pufang_national_batch1"], "官方附件将空调冷却水塔列为蒲纺核心物项；作为纺织厂能源与环境控制基础设施单列，现状需核验。", {"material_carriers": "空调冷却水塔及厂区基础设施", "technical_memory": "纺织车间温湿度和生产环境控制技术", "social_memory": "工人对厂区设备景观和生产秩序的共同记忆", "current_use_or_loss": "遗址现存与安全边界待现场核实"}, related_heritage_ids=["HER-d0daf5a12b29"]),
    rec("HBI-XN-008", "蒲纺热电厂遗址（国家工业遗产组成项）", "咸宁市", "电力能源工业", "national_cultural_relic_related", "第一批国家工业遗产二三四八蒲纺总厂核心物项组成项（非独立认定）", ["pufang_national_batch1"], "官方附件将热电厂列为蒲纺核心物项；它是纺织生产能源系统的组成设施，实体和设备状态待核。", {"material_carriers": "热电厂厂房、能源设备和管线（待核）", "technical_memory": "热电联产和纺织工厂能源供应", "social_memory": "热电职工、厂区生活和生产保障记忆", "current_use_or_loss": "现存设备、拆改和产权状态待核"}, related_heritage_ids=["HER-d0daf5a12b29"]),
    rec("HBI-XN-009", "蒲纺专用铁路线遗址（国家工业遗产组成项）", "咸宁市", "铁路交通工业", "national_cultural_relic_related", "第一批国家工业遗产二三四八蒲纺总厂核心物项组成项（非独立认定）", ["pufang_national_batch1"], "官方附件将专用铁路线列为蒲纺核心物项；记录其原料、产品和厂区物流联系，线路走向与现存轨道待测绘。", {"material_carriers": "厂区专用铁路及装卸、连接设施", "technical_memory": "纺织工业原料与产品运输系统", "social_memory": "铁路工人、运输班组和工厂物流记忆", "current_use_or_loss": "线路现状和保留段落待现场测绘"}, related_heritage_ids=["HER-d0daf5a12b29"]),
    rec("HBI-XN-010", "蒲纺跃进门（国家工业遗产组成项）", "咸宁市", "纺织工业社区文化", "national_cultural_relic_related", "第一批国家工业遗产二三四八蒲纺总厂核心物项组成项（非独立认定）", ["pufang_national_batch1"], "官方附件将跃进门列为蒲纺核心物项；作为厂区入口、集体记忆和工业景观符号单列，现状需核实。", {"material_carriers": "厂区跃进门及入口景观", "technical_memory": "厂区组织、班次进出和企业空间秩序", "social_memory": "工人上下班、集体活动和蒲纺城市记忆", "current_use_or_loss": "现存位置、保存程度和开放状态待核"}, related_heritage_ids=["HER-d0daf5a12b29"]),
    rec("HBI-XN-011", "蒲纺1511M-44型织机（国家工业遗产组成项）", "咸宁市", "纺织机械工业", "national_cultural_relic_related", "第一批国家工业遗产二三四八蒲纺总厂核心物项组成项（非独立认定）", ["pufang_national_batch1"], "官方附件将1511M-44型织机列为蒲纺核心物项；设备实物、铭牌、运行工艺和收藏位置待馆藏或现场核验。", {"material_carriers": "1511M-44型织机及其铭牌、配套工具", "technical_memory": "棉纺织机运行、维护和工艺传承", "social_memory": "挡车工、维修工和技能培训记忆", "current_use_or_loss": "现存设备及授权展示状态待核"}, related_heritage_ids=["HER-d0daf5a12b29"]),
    rec("HBI-XG-002", "汉川马口省汽修老厂房", "孝感市", "汽车维修与机械工业", "research_candidate", "来源确认的三线工业遗存候选", ["xg_hanchuan_auto_2026"], "湖北日报确认马口省汽修老厂房红砖车间和钢构建筑保存较好并启动微更新；原企业全称、建设年代、厂区构成和现存设备待档案核验。", {"material_carriers": "20世纪70年代红砖车间、钢构建筑、梁柱和老式门窗", "technical_memory": "汽车维修、机械加工和地方工业服务", "social_memory": "马口工业镇职工、居民和老厂房生活记忆", "current_use_or_loss": "微更新为马口烧烤文创园，分期建设中"}, district="马口镇"),
    rec("HBI-XG-003", "汉川3509纺织厂旧址（3509社区文化空间）", "孝感市", "纺织与军需工业", "research_candidate", "来源确认的三线纺织军工候选", ["xg_hanchuan_3509_2025"], "湖北日报确认3509纺织厂1950年始建、前身为解放军3509工厂，并记录老礼堂、工人俱乐部和社区改造；厂区正式边界和核心建筑清单待核。", {"material_carriers": "3509老礼堂、工人俱乐部、社区公共建筑和红砖空间", "technical_memory": "军需纺织、棉纺生产和企业社区组织", "social_memory": "近万居民、退休职工、工人俱乐部和军工精神", "current_use_or_loss": "3509社区改造为公共文化与文体空间"}, district="马口镇", aliases=["际华三五零九纺织有限公司旧址", "3509社区"]),
    rec("HBI-HG-003", "红安县红一军修械所旧址", "黄冈市", "军工维修工业", "county", "红安县文物保护单位；湖北省第二批不可移动革命文物名录", ["hg_hongan_repair_2022"], "省文旅厅官方革命文物名录明确列出红一军修械所旧址并标注为红安县文物保护单位；记录其军工维修属性，避免与一般革命旧址混同。", {"material_carriers": "修械所旧址建筑和维修工具线索", "technical_memory": "红军武器维修、修理组织和战时生产保障", "social_memory": "红军维修人员、地方群众和革命工业记忆", "current_use_or_loss": "文物保护对象，现存构成与开放状态待地方文物档案核验"}, district="红安县"),
    rec("HBI-XT-004", "沔阳县活塞环厂旧址（张沟农机修配厂沿革）", "仙桃市", "机械制造工业", "research_candidate", "来源确认的地方工业记忆候选", ["xiantao_piston_ring_2025"], "极目新闻结合老工人回访记载1958年张沟农机修配厂起步、后发展为沔阳县活塞环厂，现址残留厂房并闲置；精确地址、建筑和设备需实测。", {"material_carriers": "残留车间、旧厂房和高炉等工业构件（待核）", "technical_memory": "活塞环加工、农机维修和机耕船制造", "social_memory": "老工人、厂二代和张沟工业镇乡土记忆", "current_use_or_loss": "旧址闲置待租，建议先做建筑和口述史抢救"}, district="张沟镇", aliases=["沔阳县活塞环厂", "张沟农机修配厂"]),
    rec("HBI-QJ-005", "江汉油田工业文化片区", "潜江市", "石油工业文化景观", "city_planning", "国土空间规划提出的工业文化片区线索", ["qianjiang_industrial_plan", "qianjiang_industrial_tourism"], "潜江市规划和文旅公开资料提出依托采油作业区、工业景观与农业景观建设江汉油田工业文化片区；本条是规划尺度的文化景观对象，不等同于单体建筑认定。", {"material_carriers": "采油作业区、油田设施、工业景观和农业景观组合", "technical_memory": "江汉油田勘探、钻采、输送与生产组织", "social_memory": "石油大军、会战基地、职工社区和地方发展记忆", "current_use_or_loss": "规划展示与工业旅游利用方向，边界、单体和产权待核"}, district="广华寺街道", aliases=["江汉油田工业文化景区"]),
    rec("HBI-ES-007", "刘家坝老发电房及水渠", "恩施州", "水电工程工业", "research_candidate", "来源确认的地方水电工业文化候选", ["enshi_lai_feng_power_2021"], "省文旅厅项目表明确记载来凤刘家坝老发电房、水渠及狮子桥水电站由张富清带领群众修建，并提出修复打造；本条与现有狮子桥水电站记录形成工程组成关系。", {"material_carriers": "老发电房、水渠及配套水工构筑物", "technical_memory": "山区小型水电建设、引水和发电技术", "social_memory": "张富清、当地群众和来凤水电建设记忆", "current_use_or_loss": "位于杨梅古寨周边，修复和开放状态待核"}, district="来凤县", related_inventory_ids=["HBI-ES-001"]),
    rec("HBI-XIANGYANG-017", "襄阳汽车轴承厂旧址", "襄阳市", "机械制造工业", "research_candidate", "高校三线工业遗址调研候选", ["xiangyang_3line_university"], "武汉科技大学工业文化创新研究中心现场调研逐名记录襄阳汽车轴承厂旧址，并通过测量、拍照和居民访谈了解保存状态；正式名录和厂区边界待核。", {"material_carriers": "旧厂房、工业痕迹和设备遗存（现场记录待公开）", "technical_memory": "汽车轴承制造与三线专业化配套", "social_memory": "三线建设者、工人和居民口述记忆", "current_use_or_loss": "停产多年，建筑遗迹和保护需求待专项建档"}),
    rec("HBI-XIANGYANG-018", "宏伟机械厂旧址", "襄阳市", "机械制造工业", "research_candidate", "高校三线工业遗址调研候选", ["xiangyang_3line_university"], "武汉科技大学官方报道将宏伟机械厂旧址列为襄阳三线建设遗址并开展现场调研；企业谱系、生产工艺和现存构筑物待档案核验。", {"material_carriers": "老厂房和工业建筑痕迹（组成待测绘）", "technical_memory": "三线机械制造和专业厂协作记忆", "social_memory": "建设者、职工和周边居民口述记忆", "current_use_or_loss": "停产或转型状态待核"}),
    rec("HBI-XIANGYANG-019", "襄城区610厂旧址", "襄阳市", "军工机械工业", "city_planning", "襄阳十五五规划老旧厂区改造利用对象", ["xiangyang_15th_plan_2026"], "襄阳市规划明确将襄城区610厂纳入22个老旧厂区和公共空间改造利用；记录保持规划对象层级，涉密边界、历史沿革和现存构筑物待核。", {"material_carriers": "610厂老厂区及公共空间（边界待核）", "technical_memory": "三线军工生产—生活—公共服务组织", "social_memory": "厂区职工、家属区和襄阳三线工业记忆", "current_use_or_loss": "规划导向为文化创意、科技研发和公共服务再利用"}, district="襄城区", aliases=["六一〇厂旧址", "610厂"]),
    rec("HBI-XIANGYANG-020", "襄阳棉纺厂旧址", "襄阳市", "纺织工业", "city_planning", "襄阳十五五规划三线工业遗产活化对象", ["xiangyang_15th_plan_2026"], "襄阳市规划提出依托襄阳棉纺厂等三线工业遗产打造生活秀带，并纳入老旧厂区改造利用；厂区组成、沿革和现存建筑待专项普查。", {"material_carriers": "棉纺厂老厂房、铁路或公共空间（待核）", "technical_memory": "棉纺生产、工厂社区和产业工人技能", "social_memory": "纺织职工、家属区和襄阳工业城市生活", "current_use_or_loss": "规划导向为生活秀带和公共空间再利用"}),
    rec("HBI-YC-007", "宜昌船厂旧址", "宜昌市", "船舶制造工业", "research_candidate", "官方报道确认的老船厂活化改造对象", ["yichang_shipyard_2026"], "宜昌市政府确认宜昌船厂始建于1956年，旧址正在实施西坝龙园活化改造；厂区范围、原船坞/车间和设备保存情况待专项测绘。", {"material_carriers": "1956年船厂旧厂区、车间、船坞和设备（待核）", "technical_memory": "长江船舶修理、制造和航运工业技术", "social_memory": "船厂工人、西坝社区和长江航运记忆", "current_use_or_loss": "纳入长江·西坝旅游岛龙园项目，计划分期运营"}, aliases=["长航宜昌船厂旧址"]),
    rec("HBI-YC-008", "五峰精制茶厂精制车间（宜红茶工业遗产组成项）", "宜昌市", "茶叶加工工业", "provincial_heritage_related", "宜红茶工业遗产省级文保单位核心车间组成项（与HBI-YC-005同址）", ["yichang_wufeng_yihong_2025", "yichang_tea"], "宜昌市政府报道明确将五峰精制茶厂精制车间作为宜红茶工业遗产和省级文保单位核心展示空间；本条作为组成项补充，不新增独立文保认定。", {"material_carriers": "精制茶厂精制车间及茶厂工业建筑", "technical_memory": "宜红茶精制、出口创汇和制茶工艺", "social_memory": "茶厂青年工人、土家民俗和五峰茶乡记忆", "current_use_or_loss": "沉浸式演艺、展示馆、非遗和研学空间"}, district="五峰土家族自治县", aliases=["五峰精制茶厂精制车间"], related_inventory_ids=["HBI-YC-005"]),
    rec("HBI-YC-009", "宜昌磨盘港码头工业遗址", "宜昌市", "港口与磷化工业", "research_candidate", "官方生态修复报道确认的工业遗址再生对象", ["yichang_industrial_shoreline_2026"], "省自然资源厅报道确认磨盘港原为磷矿露天堆场，传送带钢架、旧仓库和废弃反应釜被保留并改造为灯塔广场公共艺术；具体行政区、原企业和遗产边界待核。", {"material_carriers": "码头传送带钢架、旧仓库、废弃反应釜和岸线空间", "technical_memory": "磷矿装卸、堆场物流和沿江工业体系", "social_memory": "码头工人、沿江居民和工业岸线生活记忆", "current_use_or_loss": "灯塔广场生态修复与公共文化空间"})
]


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    existing_ids = {row["inventory_id"] for row in records}
    existing_names = {row["name"] for row in records}

    duplicate_sources = set(NEW_SOURCES) & set(sources)
    duplicate_ids = {row["inventory_id"] for row in NEW_RECORDS} & existing_ids
    duplicate_names = {row["name"] for row in NEW_RECORDS} & existing_names
    if duplicate_sources or duplicate_ids or duplicate_names:
        existing_by_id = {row["inventory_id"]: row for row in records}
        already_applied = (
            set(NEW_SOURCES) <= set(sources)
            and all(sources[key] == value for key, value in NEW_SOURCES.items())
            and set(row["inventory_id"] for row in NEW_RECORDS) <= existing_ids
            and all(existing_by_id[row["inventory_id"]] == row for row in NEW_RECORDS)
        )
        if already_applied:
            print(f"already_present total_records={len(records)} total_sources={len(sources)}")
            return
        raise SystemExit(
            "partial or conflicting prior application: "
            f"source_keys={sorted(duplicate_sources)} ids={sorted(duplicate_ids)} names={sorted(duplicate_names)}"
        )

    missing = sorted({key for row in NEW_RECORDS for key in row["source_keys"] if key not in sources and key not in NEW_SOURCES})
    if missing:
        raise SystemExit(f"missing source keys: {missing}")
    sources.update(NEW_SOURCES)
    records.extend(NEW_RECORDS)
    data["research_targets"]["coverage_rule"] = (
        "每条对象至少绑定名录/普查/规划/企业史或来源确认资料；文化证据字段只记录来源中明确出现的载体、技术、社会记忆和利用状态，未核实内容保持待核。"
    )
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"added_records={len(NEW_RECORDS)} added_sources={len(NEW_SOURCES)} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
