from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "jingzhou_heritage_2024_35": {
        "source_type": "municipal_notice_district_repost",
        "title": "荆州市人民政府关于公布中山纪念堂等35处建筑为荆州市历史建筑的通知（2024年新增35处历史建筑名录，编号102-136）",
        "org": "荆州市人民政府（沙市区人民政府网转载附件图）",
        "pub_date": "2024-11-08",
        "url": "http://www.shashi.gov.cn/ssqxw/ssyw/202411/t20241108_968178.shtml",
        "authority": "A",
        "notes": "2024年荆州新增35处历史建筑名录（编号续接2019年100处，102-136）附件图两张已下载逐张视觉核读（本地存档 raw/jingzhou_35/）：第105项沙市装卸大楼、第106-108项富友实业建筑群一号/二号/三号仓库、第109项怡和洋行、第110-112项港务集团建筑群一号/二号/三号仓库、第113-122项活力28集团建筑群（保全车间、香皂车间、一号/二号/三号/四号仓库、包装车间、肥皂皂化间、成品仓库、一号办公楼共10栋）、第123项长江大学东校区院内水塔、第125项新垸水塔、第126项李埠水塔、第132项源通运业有限公司办公楼；另含中山纪念堂、中山公园东大门/凌波桥、江陵车站钟楼、张居正故居等。",
    },
}


RECORDS = [
    {
        "inventory_id": "HBI-JZ-023",
        "name": "沙市装卸大楼",
        "city": "荆州市",
        "district_county": "沙市区",
        "industry_category_l1": "港口与水运工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "荆州市历史建筑（2024年新增35处名录第105项，编号105）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["jingzhou_heritage_2024_35"],
        "cultural_evidence": {
            "material_carriers": "港口装卸作业大楼建筑本体；建筑面积、结构与建造年代待现场测绘",
            "technical_memory": "沙市长江码头货物装卸组织与机械化装卸工艺的指挥中枢载体，与洋码头—打包厂码头仓储带同属港口作业谱系",
            "social_memory": "码头装卸工人与沙市港航运贸易集体记忆",
            "current_use_or_loss": "以市级历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自2024年新增35处名录附件图（A级，视觉核读）；名录仅载名称；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_building",
    },
    {
        "inventory_id": "HBI-JZ-024",
        "name": "富友实业建筑群（一号、二号、三号仓库）",
        "city": "荆州市",
        "district_county": "沙市区",
        "industry_category_l1": "工业仓储与运输",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "荆州市历史建筑（2024年新增35处名录第106-108项，共3栋）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["jingzhou_heritage_2024_35"],
        "cultural_evidence": {
            "material_carriers": "仓库建筑3栋（一号、二号、三号仓库）；仓型、结构与保存状态待现场测绘",
            "technical_memory": "富友实业仓储建筑的储存工艺与结构形制；企业沿革（富友实业经营门类）待地方志核验",
            "social_memory": "仓储职工与沙市工商业流通记忆",
            "current_use_or_loss": "以市级历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自2024年新增35处名录附件图（A级，视觉核读）；名录仅载名称；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["富友实业建筑群"],
        "asset_kind": "industrial_storage_site",
    },
    {
        "inventory_id": "HBI-JZ-025",
        "name": "港务集团建筑群（一号、二号、三号仓库）",
        "city": "荆州市",
        "district_county": "沙市区",
        "industry_category_l1": "港口与水运工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "荆州市历史建筑（2024年新增35处名录第110-112项，共3栋）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["jingzhou_heritage_2024_35"],
        "cultural_evidence": {
            "material_carriers": "港务仓库建筑3栋（一号、二号、三号仓库）；仓型、跨度与保存状态待现场测绘",
            "technical_memory": "荆州港务集团的港口后方仓储体系，与沙市装卸大楼、洋码头码头带构成港口作业—仓储完整链条",
            "social_memory": "港务职工与长江航运物流记忆",
            "current_use_or_loss": "以市级历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自2024年新增35处名录附件图（A级，视觉核读）；名录仅载名称；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["港务集团建筑群"],
        "asset_kind": "industrial_storage_site",
    },
    {
        "inventory_id": "HBI-JZ-026",
        "name": "怡和洋行",
        "city": "荆州市",
        "district_county": "沙市区",
        "industry_category_l1": "近代航运与民族工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "荆州市历史建筑（2024年新增35处名录第109项）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["jingzhou_heritage_2024_35"],
        "cultural_evidence": {
            "material_carriers": "怡和洋行建筑本体；建造年代、结构与保存状态待现场测绘",
            "technical_memory": "怡和洋行为近代英国综合商行，沙市开埠（1895年《马关条约》开埠语境）后外资洋行在长江中游口岸的航运贸易经营载体；与源泰洋行（HBI-WUHAN 记录）同属湖北近代洋行谱系",
            "social_memory": "沙市开埠与近代口岸贸易记忆",
            "current_use_or_loss": "以市级历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自2024年新增35处名录附件图（A级，视觉核读）；名录仅载名称，洋行在沙的具体经营年代与建筑沿革待地方志核验；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_trade_site",
    },
]


JZ001_PATCH = {
    "source_keys_append": ["jingzhou_heritage_2024_35"],
    "notes_append": "2024年新增35处历史建筑名录（编号113-122）将活力28集团建筑群10栋（保全车间、香皂车间、一号/二号/三号/四号仓库、包装车间、肥皂皂化间、成品仓库、一号办公楼）列为市级历史建筑，本条活力28老厂房（沙市日化旧厂区）获得逐栋载明的市级历史建筑保护身份。",
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
    jz001 = next((row for row in records if row["inventory_id"] == "HBI-JZ-001"), None)
    if jz001 is None:
        raise SystemExit("record not found: HBI-JZ-001")
    updated = 0
    for key in JZ001_PATCH["source_keys_append"]:
        if key not in jz001["source_keys"]:
            jz001["source_keys"].append(key)
            updated = 1
    if JZ001_PATCH["notes_append"] not in jz001["notes"]:
        jz001["notes"] = jz001["notes"] + JZ001_PATCH["notes_append"]
        updated = 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_bl_sources={len(SOURCES)} added_records={added} updated_records={updated} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
