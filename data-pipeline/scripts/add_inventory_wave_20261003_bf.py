from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "jingzhou_heritage_buildings_2019": {
        "source_type": "official_media_full_text_repost",
        "title": "荆州市人民政府关于公布荆州市中心城区历史建筑的通知（2019年，100处名录全表）",
        "org": "荆州市人民政府（荆州日报/澎湃新闻转载全文）",
        "pub_date": "2019-09-30",
        "url": "https://m.thepaper.cn/baijiahao_4925826",
        "authority": "B",
        "notes": "2019年9月30日市政府确定大慈街口民居等100处建筑为荆州市中心城区历史建筑（对第一、二批重新鉴定评估后公布），转载文含完整名录：沙市打包厂建筑群南北主楼/经理楼/物料仓库/动力车间（5-8）、供电公司建筑群办公楼/仓库（9-10）、白云机电建筑群办公大楼与西区一二三号/中区一二三号/东区一号/北区联排厂房（11-19）、荆州粮食加工厂稻谷圆库（49）、纺织姑娘雕塑（59）、沙市修防处办公大楼旧址（92）等；另含吉祥花号、安利英行等商贸行栈与大量民居。",
    },
}


RECORDS = [
    {
        "inventory_id": "HBI-JZ-019",
        "name": "白云机电建筑群",
        "city": "荆州市",
        "district_county": "沙市区",
        "industry_category_l1": "机械制造工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "荆州市中心城区历史建筑（2019年9月30日市政府公布100处名录第11-19项，共9栋）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["jingzhou_heritage_buildings_2019"],
        "cultural_evidence": {
            "material_carriers": "名录载明9栋：办公大楼、西区一号厂房、西区二号联排厂房、西区三号厂房、中区一号厂房、中区二号厂房、中区三号厂房、东区一号厂房、北区联排厂房；各栋跨度、结构与企业全称待现场测绘与厂志核验",
            "technical_memory": "白云机电的机械制造厂房群按西、中、东、北区分区布局，反映原地规模化机械工业的生产组织；产品谱系与停产沿革待补",
            "social_memory": "白云机电职工与沙市机械工业街区记忆",
            "current_use_or_loss": "以中心城区历史建筑身份纳入保护体系；厂区现状用途待核",
        },
        "notes": "直接取自2019年市政府100处名录（荆州日报/澎湃转载全文核读）；转载来源为B级，通知主体为市政府；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["白云机电"],
        "asset_kind": "industrial_building",
    },
    {
        "inventory_id": "HBI-JZ-020",
        "name": "供电公司建筑群（办公楼、仓库）",
        "city": "荆州市",
        "district_county": "沙市区",
        "industry_category_l1": "电力能源",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "荆州市中心城区历史建筑（2019年9月30日市政府公布100处名录第9-10项，共2栋）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["jingzhou_heritage_buildings_2019"],
        "cultural_evidence": {
            "material_carriers": "供电公司办公楼与仓库2栋；建造年代与结构待现场测绘",
            "technical_memory": "沙市电力供应体系的经营与仓储设施；与永耀电灯公司（宜昌）、汉口电灯公司共同构成湖北电力工业城市谱系的荆州节点",
            "social_memory": "供电职工与城市照明记忆",
            "current_use_or_loss": "以中心城区历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自2019年市政府100处名录（转载全文核读）；名录未载具体门牌与年代；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_utility_site",
    },
    {
        "inventory_id": "HBI-JZ-021",
        "name": "荆州粮食加工厂稻谷圆库",
        "city": "荆州市",
        "district_county": "荆州区",
        "industry_category_l1": "粮食加工工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "荆州市中心城区历史建筑（2019年9月30日市政府公布100处名录第49项）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["jingzhou_heritage_buildings_2019"],
        "cultural_evidence": {
            "material_carriers": "稻谷圆库（立式圆筒粮仓）建筑本体；容量、个数与结构待现场测绘",
            "technical_memory": "圆筒仓是粮食加工厂散粮储存的典型构筑物，代表机械化粮食加工的仓储环节",
            "social_memory": "荆州粮食加工与江汉平原稻米集散记忆",
            "current_use_or_loss": "以中心城区历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自2019年市政府100处名录（转载全文核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_storage_site",
    },
    {
        "inventory_id": "HBI-JZ-022",
        "name": "沙市修防处办公大楼旧址",
        "city": "荆州市",
        "district_county": "沙市区",
        "industry_category_l1": "水利工程与泵站",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "荆州市中心城区历史建筑（2019年9月30日市政府公布100处名录第92项）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["jingzhou_heritage_buildings_2019"],
        "cultural_evidence": {
            "material_carriers": "修防处办公大楼旧址建筑本体；建造年代与结构待现场测绘",
            "technical_memory": "长江荆江段堤防修防管理机构（修防处）的办公指挥设施，承载荆江大堤防洪工程建设管理记忆；与荆江分洪闸（HBI-JZ-005）同属荆江水利脉络",
            "social_memory": "修防职工与沿江居民防洪保安全集体记忆",
            "current_use_or_loss": "以中心城区历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自2019年市政府100处名录（转载全文核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_utility_site",
    },
]


JZ004_PATCH = {
    "notes_append": "2019年荆州市中心城区100处历史建筑名录第5-8项将沙市打包厂建筑群南北主楼、经理楼、物料仓库、动力车间4栋单体列为市级历史建筑（荆州日报/澎湃转载全文核读）。",
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    added = 0
    for record in RECORDS:
        existing = next((row for row in records if row["inventory_id"] == record["inventory_id"]), None)
        if existing is not None:
            if existing != record:
                raise SystemExit(f"conflicting duplicate record: {record['inventory_id']}")
            continue
        if any(row["name"] == record["name"] for row in records):
            raise SystemExit(f"conflicting duplicate name: {record['name']}")
        records.append(record)
        added += 1
    for key, source in SOURCES.items():
        if key in sources and sources[key] != source:
            raise SystemExit(f"conflicting source: {key}")
    sources.update(SOURCES)
    jz004 = next((row for row in records if row["inventory_id"] == "HBI-JZ-004"), None)
    if jz004 is None:
        raise SystemExit("record not found: HBI-JZ-004")
    updated = 0
    if JZ004_PATCH["notes_append"] not in jz004["notes"]:
        jz004["notes"] = jz004["notes"] + JZ004_PATCH["notes_append"]
        updated = 1
    if "jingzhou_heritage_buildings_2019" not in jz004["source_keys"]:
        jz004["source_keys"].append("jingzhou_heritage_buildings_2019")
        updated = 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_bf_sources={len(SOURCES)} added_records={added} updated_records={updated} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
