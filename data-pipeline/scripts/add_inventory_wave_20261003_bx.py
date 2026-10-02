from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "gongan_brick_close_2015": {
        "source_type": "county_government_normative_document",
        "title": "县人民政府办公室关于印发公安县关闭粘土砖瓦生产企业实施方案的通知（公政办发〔2015〕13号）",
        "org": "公安县人民政府办公室",
        "pub_date": "2015-04-14",
        "url": "http://zwgk.gongan.gov.cn/31975/202209/t20220922/106389.shtml",
        "authority": "A",
        "notes": "载明依法关闭取缔全县范围内粘土砖瓦企业，2015年8月31日前关闭并拆除全县所有粘土砖瓦企业及生产设施（每家5万元、每门窑5000元奖励）——全县砖瓦企业2015年整体终结的断代依据。另见杨家厂镇第一砖瓦厂征地/社保公告链（2022-2023，公政土征安置公告〔2022〕025/027/029号等，285人符合补偿条件；http://zwgk.gongan.gov.cn/38554/202212/t20221205/244247.shtml）——系镇属砖瓦厂，与1965年县属厂同一性待档案核对。",
    },
    "xiangyang_coal_port_plan_2026": {
        "source_type": "municipal_planning_document",
        "title": "襄阳市国民经济和社会发展第十五个五年规划纲要（涉煤货场与港口资源整合章节）",
        "org": "襄阳市经济和信息化局（市政府网）",
        "pub_date": "2026-05-08",
        "url": "http://jxj.xiangyang.gov.cn/zwgk/gkml/ghjh/202605/t20260508_3996959.shtml",
        "authority": "A",
        "notes": "规划载明依托浩吉铁路襄州北站运力整合涉煤货场与港口资源、建设国家级煤炭应急储备基地——证实现代煤炭物流集中于襄州北站/浩吉铁路格局，与余家湖港（1996年襄樊电厂源起）均非1965年省档案馆“襄阳县煤货场”题名实体。",
    },
    "xiangyang_yangdoukou_coal_2016": {
        "source_type": "municipal_government_culture_article",
        "title": "樊城马道口地名初探（载煤建公司等汉江码头区老企业）",
        "org": "襄阳市民政局（市军休四所）",
        "pub_date": "2016-12-28",
        "url": "http://mzj.xiangyang.gov.cn/zxzx/gzdt/201612/t20161228_25519.shtml",
        "authority": "A",
        "notes": "地名考证文章载明樊城马道口—中山前后街片区有市二米厂、钉丝厂、煤建公司、市一房管所等单位（2013年旧城改造前格局）——证实樊城（市级）煤建公司位于汉江码头区，煤炭依赖水运码头的布局模式与“襄阳县煤货场”选址逻辑互证；1965年县属煤货场地块可按保康县燃料公司煤球厂不动产注销公告先例（baokang.gov.cn 2020-11-24）在襄州区不动产登记档案追查。",
    },
    "hbbid_suixian_grain_2025": {
        "source_type": "official_bidding_platform",
        "title": "随县粮食储备有限公司建设4万吨粮仓项目一期2#准低温粮库评标结果公示（招标人地址随县厉山镇北岗村）",
        "org": "湖北省电子招投标交易平台（随县中心）",
        "pub_date": "2025-10-28",
        "url": "https://www.hbbidcloud.cn/",
        "authority": "A",
        "notes": "评标公示载明招标人随县粮食储备有限公司地址“随县厉山镇北岗村”（标段编号HBSX-202509FJ-011001001）；工商信息交叉验证：随县粮食储备有限公司（统一社会信用代码91421321615747936H，2003年成立，曾用名随县金良粮食储备有限公司）注册地址与年报地址均为随县厉山镇北岗村，行业装卸搬运和仓储业。",
    },
    "hubei_daily_tangxian_grain_2025": {
        "source_type": "official_media",
        "title": "随县唐县镇：盘活“沉睡”国资（原砂子粮站拍卖活化）",
        "org": "湖北日报客户端",
        "pub_date": None,
        "url": "https://news.hubeidaily.net/mobile/c_5591902.html",
        "authority": "B",
        "notes": "载明唐县镇原砂子粮站（近10亩，体制改革闲置多年）2025年2月公开拍卖139万元，随州鑫动机械投资2000多万元建粮食机械制造基地；原烟草站改建养老综合体——随县粮站资产活化实证。",
    },
    "anlu_loji_renov_2021": {
        "source_type": "county_city_government_portal",
        "title": "北正社区粮机片区老旧小区改造正式开工（粮机小区/粮机居民区/银河小区，27栋996户）",
        "org": "安陆市人民政府门户网站",
        "pub_date": "2021-12-12",
        "url": "http://www.anlu.gov.cn/",
        "authority": "A",
        "notes": "官网图片新闻载明安陆市2021年老旧小区改造开工仪式在北正社区粮机片区举行，涉及粮机小区、粮机居民区、银河小区3个老旧小区、27栋房屋、996户、3000余名常住居民（属府城街道）——原东方红粮机厂生活区（粮机片区）现状坐实。另据湖北日报客户端报道，社区建有“粮机记忆馆”、粮机文化墙与“四状元里”牌坊（工业遗产活化载体）。",
    },
    "hbdfh_official_site": {
        "source_type": "enterprise_official_site",
        "title": "东方红集团（湖北）粮食机械股份有限公司官网企业简介（原中华人民共和国安陆粮机厂）",
        "org": "东方红集团（湖北）粮食机械股份有限公司",
        "pub_date": None,
        "url": "http://www.hbdfh.com.cn/",
        "authority": "C",
        "notes": "企业官网自述：原中华人民共和国安陆粮机厂，前身为国家粮食部上海粮机厂1966年内迁湖北安陆，2006年湖北骏马集团收购控股，现址安陆市经济开发区粮机北路1号（占地12.21万平方米）——生产主体存续与现址坐实；粮机北路路名本身即遗产记忆留存。",
    },
    "shiyan_daily_chassis_2018": {
        "source_type": "official_party_newspaper",
        "title": "东风零部件两大新公司分别在十堰襄阳成立（42/45/54/46厂整合为底盘系统公司）",
        "org": "十堰日报数字报",
        "pub_date": "2018-11-23",
        "url": "http://syrb.10yan.com/",
        "authority": "A",
        "notes": "党报载明2018年11月17日东风汽车底盘系统有限公司挂牌（注册资本4.79亿元），由东风车轮、东风传动轴、东风悬架弹簧、东风泵业4家整合而成；历史沿革明确：42厂=东风汽车车轮有限公司（前身二汽车轮厂，1970年9月十堰城区中心神定河畔兴建）、45厂=东风汽车泵业（前身1969年二汽底盘零件厂，汉江路）、46厂=东风汽车悬架弹簧（前身1969年二汽钢板弹簧厂）、54厂=东风汽车传动轴（前身1969年二汽传动轴厂，三堰杨家沟）。秦楚网2018-11-21《东风六家单位整合》另载“东风车轮(42)、东风泵业(45)、东风悬架弹簧(46)、东风传动轴(54)、东风电子(63)、东风电气(65)数字代号厂名最后一次被叫响”及子公司名录（东风车轮随州有限公司、东风襄阳旋压件、上海欧雷法弹簧）。",
    },
}


UPGRADE = {
    "HBI-SZ-012": {
        "record_status": "source_confirmed",
        "recognition_status": "随县粮食储备仓库机构与地址坐实：随县粮食储备有限公司（曾用名随县金良粮食储备有限公司）位于随县厉山镇北岗村，官方招投标公告与工商登记双重验证；与1965年省档案馆题名仓库的延续关系待档案终核",
        "district_county": "随县厉山镇北岗村",
        "material_carriers": "随县粮食储备有限公司库区（厉山镇北岗村，2025年在建4万吨粮仓项目一期2#准低温粮库）；1965年题名仓址与现库建筑对应待现场核验",
        "notes_append": "2026-10-03第五组复核升格：湖北省电子招投标交易平台评标公示（A，含招标人地址）与工商登记交叉验证锁定厉山镇北岗村，自 archive_lead 升格为 source_confirmed（升格表示机构地址坐实，不表示建筑本体与法定认定）；唐县镇砂子粮站活化与尚市镇储备库改扩建（总投资2.14亿）为库点网络旁证。",
    },
}


NOTES_APPENDS = {
    "HBI-JZ-016": "2026-10-03第五组复核补充：公政办发〔2015〕13号载明2015年8月底全县粘土砖瓦企业整体关闭拆除（厂址终态断代）；杨家厂镇第一砖瓦厂征地/社保公告链（2022-2023，285人补偿）系镇属厂旁证，与1965年县属厂同一性待档案核对——维持 source_lead，县志在线版与省地情网均不可达，转线下。",
    "HBI-XIANGYANG-029": "2026-10-03第五组复核：襄阳市政府站群SSP接口检索“襄樊市化肥厂”0条精确匹配、“化肥厂”137条均为县属厂；《襄樊市志》在线版不可达（省地情网502、万方需登录），襄阳市档案馆子站404——1965年市属化肥厂仅档案原件可证，维持 source_lead 转线下调档。",
    "HBI-XIANGYANG-031": "2026-10-03第五组复核补充：市国资委2010年督办报道证实樊城肉联厂系市直改制/破产企业（食品公司体系，含两个肉联厂）；“襄樊市冷冻厂”专名仍未命中，维持 source_lead 转档案/报纸原件。",
    "HBI-XIANGYANG-033": "2026-10-03第五组复核：枣阳市政府站群isearch检索“拖拉机站”0条（58条均为现行农机事项），《枣阳县志》在线版不可达——维持 source_lead，以《中国财政》1958年八一拖拉机站一手文献为最早已知依据，转线下调档。",
    "HBI-XIANGYANG-032": "2026-10-03第五组复核补充（煤货场追查路径）：樊城马道口地名考证证实市级煤建公司位于汉江码头区（布局模式互证）；保康县燃料公司煤球厂不动产注销公告为各县燃料公司地块追查提供先例——1965年县属煤货场地块建议在襄州区（原襄阳县）不动产登记档案按此路径追查，维持 archive_lead。",
    "HBI-XG-013": "2026-10-03第五组复核补充（粮机厂区活化证据）：安陆市政府网证实北正社区粮机片区（粮机小区/粮机居民区/银河小区，27栋996户）2021年老旧小区改造开工；湖北日报客户端证实社区建“粮机记忆馆”、粮机文化墙；东方红集团官网证实生产主体存续（现址经济开发区粮机北路1号）。注意：粮机厂区（制造粮机）与档案题名“粮食加工与棉花轧花设施”（加工粮食与轧花）为两组不同设施，同一性仍待档案比对，维持 source_lead；“粮机记忆馆”可作为后续独立活化载体线索。",
    "HBI-SZ-009": "2026-10-03第五组复核补充：随州市档案馆官网站内检索“避雷器”0条且无开放档案栏目，1976年建厂批文线上无公开渠道——档案馆地址沿河大道113号区委大院内、查阅电话0722-3062697，建议线下调卷补A级文件。",
    "HBI-SY-027": "2026-10-03第五组复核补充（老厂号厂史坐实）：十堰日报2018-11-23载明42厂=车轮（1970年9月神定河畔兴建）、45厂=泵业（1969年底盘零件厂，汉江路）、46厂=悬架弹簧（1969年钢板弹簧厂）、54厂=传动轴（1969年，三堰杨家沟），2018年11月17日四厂整合底盘系统公司（注册资本4.79亿元）——车轮老厂区位于神定河畔的语境补入。",
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    for key, source in SOURCES.items():
        if key in sources and sources[key] != source:
            sources[key] = source
    sources.update(SOURCES)
    updated = 0
    sz012 = next((row for row in records if row["inventory_id"] == "HBI-SZ-012"), None)
    if sz012 is None:
        raise SystemExit("record not found: HBI-SZ-012")
    patch = UPGRADE["HBI-SZ-012"]
    for key in ("record_status", "recognition_status", "district_county"):
        if key in patch and sz012[key] != patch[key]:
            sz012[key] = patch[key]
            updated += 1
    if "material_carriers" in patch and sz012["cultural_evidence"]["material_carriers"] != patch["material_carriers"]:
        sz012["cultural_evidence"]["material_carriers"] = patch["material_carriers"]
        updated += 1
    for k in ("hbbid_suixian_grain_2025", "hubei_daily_tangxian_grain_2025"):
        if k not in sz012["source_keys"]:
            sz012["source_keys"].append(k)
            updated += 1
    if patch["notes_append"] not in sz012["notes"]:
        sz012["notes"] = sz012["notes"] + patch["notes_append"]
        updated += 1
    for record_id, notes_append in NOTES_APPENDS.items():
        record = next((row for row in records if row["inventory_id"] == record_id), None)
        if record is None:
            raise SystemExit(f"record not found: {record_id}")
        if notes_append not in record["notes"]:
            record["notes"] = record["notes"] + notes_append
            updated += 1
    sy027 = next((row for row in records if row["inventory_id"] == "HBI-SY-027"), None)
    if "shiyan_daily_chassis_2018" not in sy027["source_keys"]:
        sy027["source_keys"].append("shiyan_daily_chassis_2018")
        updated += 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_bx_updated={updated} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
