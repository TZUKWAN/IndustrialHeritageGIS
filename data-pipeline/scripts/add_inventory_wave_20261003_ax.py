from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "xiaogan_heritage_buildings_2021": {
        "source_type": "municipal_government_notice",
        "title": "孝感市人民政府关于公布孝感市第一批优秀历史建筑名录的通知（孝感政发〔2021〕7号）",
        "org": "孝感市人民政府门户网站",
        "pub_date": "2021-12-21",
        "url": "https://www.xiaogan.gov.cn/c/www/gfxwj/221399.jhtml",
        "authority": "A",
        "notes": "孝感政发〔2021〕7号公布56处第一批优秀历史建筑并附PDF名录表（扫描件已下载逐页视觉核读，本地存档 raw/xiaogan_heritage_2021/）：第25项城隍潭码头遗址（市直，省保）、第27项北泾咀泵站（孝南，县保）、第51项陡山渡槽（孝昌，县保）、第54项青山口渡槽（孝昌，登记文物点）；另含人民公社/礼堂旧址（13、28、29）等年代史迹。",
    },
}


RECORDS = [
    {
        "inventory_id": "HBI-XG-014",
        "name": "北泾咀泵站",
        "city": "孝感市",
        "district_county": "孝南区",
        "industry_category_l1": "水利工程与泵站",
        "recognition_level": "county_relic_related",
        "recognition_status": "孝感市第一批优秀历史建筑（孝感政发〔2021〕7号名录第27项）；县级文物保护单位",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["xiaogan_heritage_buildings_2021"],
        "cultural_evidence": {
            "material_carriers": "泵站建筑与设备本体（孝南区）；机组型号、装机与站房结构待现场测绘",
            "technical_memory": "府澴河流域农田排灌泵站的机电提水技术记忆；建站年代与工程档案待补",
            "social_memory": "孝南平原湖区排涝保丰收的集体记忆与泵站职工运行值守传统",
            "current_use_or_loss": "以县保与市级优秀历史建筑双重身份纳入保护体系；在用/退役状态与保护范围待核",
        },
        "notes": "直接取自孝感政发〔2021〕7号附件名录表第27项（扫描件视觉核读）；名录未载建站年代与机组参数；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_utility_site",
    },
    {
        "inventory_id": "HBI-XG-015",
        "name": "陡山渡槽",
        "city": "孝感市",
        "district_county": "孝昌县",
        "industry_category_l1": "水利工程与泵站",
        "recognition_level": "county_relic_related",
        "recognition_status": "孝感市第一批优秀历史建筑（孝感政发〔2021〕7号名录第51项）；县级文物保护单位",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["xiaogan_heritage_buildings_2021"],
        "cultural_evidence": {
            "material_carriers": "渡槽建筑本体（孝昌县）；长度、跨径、结构形式与保存状态待现场测绘",
            "technical_memory": "丘陵灌区渡槽输水工程技术，代表农业水利建设时期的架空输水构造工艺；建设年代与灌区档案待补",
            "social_memory": "灌区乡镇农业灌溉与水利建设者的集体记忆",
            "current_use_or_loss": "以县保与市级优秀历史建筑双重身份纳入保护体系；在用/停用状态与保护范围待核",
        },
        "notes": "直接取自孝感政发〔2021〕7号附件名录表第51项（扫描件视觉核读）；与咸宁八燕渡槽、大市渡槽（HBI-XN-002/003）同为鄂渡槽水利遗存记录模式；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_utility_site",
    },
    {
        "inventory_id": "HBI-XG-016",
        "name": "青山口渡槽",
        "city": "孝感市",
        "district_county": "孝昌县",
        "industry_category_l1": "水利工程与泵站",
        "recognition_level": "county_relic_related",
        "recognition_status": "孝感市第一批优秀历史建筑（孝感政发〔2021〕7号名录第54项）；登记文物点",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["xiaogan_heritage_buildings_2021"],
        "cultural_evidence": {
            "material_carriers": "渡槽建筑本体（孝昌县）；长度、结构形式与保存状态待现场测绘",
            "technical_memory": "丘陵灌区渡槽输水工程技术；建设年代与所属灌区待核",
            "social_memory": "当地农业灌溉与水利建设记忆",
            "current_use_or_loss": "以登记文物点与市级优秀历史建筑身份纳入保护体系（登记文物点为未定级文物）；在用/停用状态待核",
        },
        "notes": "直接取自孝感政发〔2021〕7号附件名录表第54项（扫描件视觉核读）；名录标注其为登记文物点（未定级）；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_utility_site",
    },
]


XG010_PATCH = {
    "source_keys_append": ["xiaogan_heritage_buildings_2021"],
    "notes_append": "孝感政发〔2021〕7号第一批优秀历史建筑名录第25项（扫描件核读）将城隍潭码头遗址列为市级优秀历史建筑（文物级别标注省保），补充市级优秀历史建筑身份。",
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
    xg010 = next((row for row in records if row["inventory_id"] == "HBI-XG-010"), None)
    if xg010 is None:
        raise SystemExit("record not found: HBI-XG-010")
    updated = 0
    for key in XG010_PATCH["source_keys_append"]:
        if key not in xg010["source_keys"]:
            xg010["source_keys"].append(key)
            updated = 1
    if XG010_PATCH["notes_append"] not in xg010["notes"]:
        xg010["notes"] = xg010["notes"] + XG010_PATCH["notes_append"]
        updated = 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_ax_sources={len(SOURCES)} added_records={added} updated_records={updated} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
