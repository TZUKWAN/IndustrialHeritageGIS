from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "qiaolingling_wusan_2026": {
        "source_type": "management_district_official",
        "title": "屈家岭管理区经济社会发展情况（原湖北省国营五三农场，1953年成立）及农垦罐头厂线索",
        "org": "屈家岭管理区官网/百家号",
        "pub_date": "2026-05-19",
        "url": "http://www.qjl.gov.cn/art/2026/5/19/art_10235_917954.html",
        "authority": "A",
        "notes": "屈家岭管理区官网载明：原为湖北省国营五三农场，1953年成立，新中国成立后湖北省创办最早、规模最大、人口最多的国营农场，李先念同志亲自奠基，王震同志三次亲临，创建'王震同志试验田'；湖北重要商品粮基地、农业机械化和科技示范农场；已完成农场企业化改革，成立湖北五三农场集团公司。百家号报道载明历史上五三农场有罐头厂，注册'仙品桃'品牌（现为田野农谷公司承续）。",
    },
    "songyi_mining_heritage_2024": {
        "source_type": "county_government_portal",
        "title": "松滋老矿区生态治理/松宜矿区简介/湖北日报松宜煤矿转型路（核心证据链）",
        "org": "松滋市人民政府网/宜都市人民政府网/湖北日报/人民网湖北",
        "pub_date": "2024-08-05",
        "url": "http://www.hbsz.gov.cn/gov_news/sz_news/202408/t20240806_947168_zzzq.shtml",
        "authority": "A",
        "notes": "核心证据链：①宜都市政府《松宜矿区管理委员会简介》载明矿区地跨荆州松滋/宜昌宜都两市108平方公里，历史最大生产规模矿井152对、职工民工2万人，2003年下放宜昌市、2004年改制；②湖北日报《百余年松宜煤矿开凿转型路》载明松宜煤矿开采始于1835年，为国家生产原煤7500多万吨，2017年最后两座矿井关闭，陈家河煤矿旧址修旧如旧活化研学基地；③松滋市政府网载明矿洞酸性废水治理试点总投资7462万元（34.4平方公里）；④人民网2022-12-09载明松宜矿区曾为湖北第二大产煤基地，生态环境部列为闭矿治理试点。本地存档 raw/songyi_mining/。",
    },
    "qiyueshan_coal_huangshi": {
        "source_type": "municipal_natural_resources_portal",
        "title": "凡庄村褪去黑袍披绿裳（七约山煤炭基地4000万吨/3万职工/6公里塌陷区/黄石新港起源）",
        "org": "黄石市自然资源和规划局（转载湖北日报2019-09-27）",
        "pub_date": "2020-06-22",
        "url": "http://zrzy.huangshi.gov.cn/xygl/lyzy/zllh/202006/t20200622_637986.html",
        "authority": "A",
        "notes": "湖北日报2019-09-27原文：位于凡庄村的七约山探明储量4000万吨，曾为湖北省三大煤炭基地之一；1976年省七约山煤炭矿务局成立，矿山职工和家属3万多人；1993年老井衰竭、新井遇水患，所有矿井关停；采空区长达6公里，千余亩良田因地面塌陷废弃；2013年金海管理区关停辖区所有煤矿。头条搜索佐证：七约山煤炭输出与黄石新港港址起源直接相关（专用运煤码头）。",
    },
    "zhushan_bridge_east_coal": {
        "source_type": "county_media_report",
        "title": "桥东煤矿关闭退出工作通过市政府验收",
        "org": "今日竹山网（竹山县融媒体中心）",
        "pub_date": None,
        "url": "https://www.zhushan.cn/p/251132952.html",
        "authority": "B",
        "notes": "桥东煤矿位于竹山县城关镇桥东村，1970年兴建，1981年移交地方管理组建县属国营煤矿；2016年以来煤矿停止采矿，15万吨矿井关闭退出煤炭开采序列——三线时期兴建的县属国营煤矿沿革完整。",
    },
}


def _r(rid, nm, city, dc, cat, lvl, status, src, kind, yr, mat, tech, soc, use, notes, aliases):
    return {
        "inventory_id": rid, "name": nm, "city": city, "district_county": dc,
        "industry_category_l1": cat, "recognition_level": lvl, "recognition_status": status,
        "record_status": "source_confirmed", "geocode_status": "pending", "source_keys": src,
        "cultural_evidence": {"material_carriers": mat, "technical_memory": tech, "social_memory": soc, "current_use_or_loss": use},
        "notes": notes, "aliases": aliases, "asset_kind": kind,
    }


RECORDS = [
    _r("HBI-JM-024", "五三农场罐头厂与农垦工业体系", "荆门市", "屈家岭管理区", "食品加工工业",
       "municipal_historical_building",
       "屈家岭管理区历史建筑（管理区官网2026年更新载明农场沿革；罐头厂为历史设施，现由田野农谷公司承续）",
       ["qiaolingling_wusan_2026"], "industrial_building", "1950-1990年代",
       "五三农场罐头厂（注册仙品桃品牌）及农场场办工业体系建筑（98家工商企业，工业产值占工农业总产值68%）；厂房保存状况待现场测绘",
       "国营农场罐头食品加工（黄桃罐头等果蔬加工）与种养加一条龙、农工贸一体化的农垦工业体系",
       "李先念奠基、王震三次亲临的五三农场创建记忆；农垦第二代职工与仙品桃品牌消费记忆",
       "农场企业化改革后成立湖北五三农场集团公司，罐头品牌由田野农谷公司承续（3条果蔬汁生产线，年加工5.8万吨）；原厂房保存状况待核",
       "直接取自屈家岭管理区官网（A级）与百家号报道（C级）；罐头厂原厂房本体保存与仙品桃品牌沿革待档案核验；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
       ["五三农场罐头厂", "仙品桃"],
    ),
    _r("HBI-JZ-070", "松宜矿区陈家河煤矿旧址群", "荆州市", "松滋市刘家场镇（跨宜昌宜都市）", "煤炭工业",
       "municipal_historical_building",
       "松滋市历史建筑认定对象（松滋市政府网2024-08矿洞治理报道确认矿址；陈家河煤矿旧址修旧如旧活化研学基地经三峡宜昌网/中国日报网/宜昌市自规局多源确认；正式历史建筑名录公布通知未检索到）",
       ["songyi_mining_heritage_2024"], "industrial_building", "1835年起采煤/2017年关闭",
       "松宜矿区核心矿井遗存（尖岩河/陈家河两对矿井，2017年关闭）；陈家河煤矿旧址厂房群（修旧如旧改造，建筑齐整、园林景观错落有致）；矿洞酸性废水预处理池+人工湿地（总投资7462万元，34.4平方公里）；矿区铁路专用线（铁路社区即因专用线得名）；官渡坪/松木坪职工安置与康养建筑",
       "1835年起民间土法采煤→民国民营煤矿→解放后宜昌专区接管→计划经济扭转北煤南运夺煤保电→最高年产7500多万吨累计→2017年去产能关闭→矿区生态修复与研学转型——湖北煤炭工业的完整生命周期样本",
       "松宜矿区2万职工民工与4000多户矿工家庭安置记忆；刘家场镇因煤而兴的矿区集镇记忆；矿区闭矿遗留的酸性废水治理与生态修复记忆",
       "2017年全部矿井关闭；陈家河煤矿旧址已活化采煤研学基地（宜昌市自规局2025-12-01导入研学科普教育产业）；矿洞废水治理试点持续运行",
       "核心证据链：宜都市政府矿区管委会简介（A）+松滋市政府矿洞治理报道（A）+湖北日报转型路（B）+人民网矿区叫停报道（B）——4个全文页直读构成完整证据链；矿区跨松滋/宜都两市108平方公里；陈家河煤矿旧址活化研学基地状态待实地核验；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
       ["松宜煤矿", "松宜矿区", "陈家河煤矿", "尖岩河煤矿"],
    ),
    _r("HBI-HS-057", "七约山煤炭矿务局旧址群", "黄石市", "矿区跨黄石开发区·铁山区与阳新县交界", "煤炭工业",
       "municipal_historical_building",
       "黄石市工业遗产候选（2019年首批黄石市工业遗产名录未含七约山；矿区设施待黄石市文保中心认定程序确认）",
       ["qiyueshan_coal_huangshi"], "industrial_building", "1976年省矿务局挂牌（矿区历史至1993年关停）",
       "矿址（凡庄村）、6公里采空塌陷区（现存地貌）、矿区职工医院、高峰期村办小矿井30多处、煤炭输出专用码头（黄石新港港址起源）；矿址建筑保存状况待现场测绘",
       "湖北省三大煤炭基地之一的矿务局建制与煤炭输出专用码头体系；七约山煤矿关停后黄石新港因煤炭输出需求在坡岸发现良港——工业遗产与港口发展交织",
       "七约山矿区3万职工家属与矿地社区记忆；矿山关停后千余亩塌陷区修复茶园的生态转型记忆",
       "1993年矿井全部关停；采空区塌陷地貌存留；矿区设施活化方向（茶园修复/矿山遗址）待现场核验",
       "直接取自黄石市自规局转载湖北日报2019-09-27报道（A级）与头条搜索佐证（七约山煤炭输出与黄石新港起源直接相关）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
       ["七约山煤炭矿务局", "七约山煤矿"],
    ),
    _r("HBI-SY-050", "竹山桥东煤矿旧址", "十堰市", "竹山县城关镇桥东村", "煤炭工业",
       "municipal_historical_building",
       "竹山县矿山关闭退出验收对象（今日竹山网报道，2018年关闭退出；无历史建筑或工业遗产名录认定）",
       ["zhushan_bridge_east_coal"], "industrial_building", "1970年兴建",
       "桥东煤矿矿址（城关镇桥东村，15万吨矿井）；矿洞口、提升设施与矿区建筑留存待现场测绘",
       "三线时期兴建的县属国营煤矿开采工艺与地方管理体制（1970年兴建→1981年移交地方→2018年去产能关闭退出）",
       "竹山煤矿工人与县城能源供应记忆",
       "2018年关闭退出后矿址保存状况待现场核验",
       "直接取自今日竹山网报道（B级，全文核读）；无历史建筑或工业遗产名录认定；坐标未核验保持待核。",
        [],
    ),
]


def main():
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    for key, source in SOURCES.items():
        if key in sources and sources[key] != source:
            raise SystemExit(f"conflicting source: {key}")
    sources.update(SOURCES)
    added = 0
    for record in RECORDS:
        existing = next((r for r in records if r["inventory_id"] == record["inventory_id"]), None)
        if existing is not None:
            if existing != record:
                raise SystemExit(f"conflicting duplicate record: {record['inventory_id']}")
            continue
        if any(r["name"] == record["name"] for r in records):
            raise SystemExit(f"conflicting duplicate name: {record['name']}")
        records.append(record)
        added += 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_cw_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
