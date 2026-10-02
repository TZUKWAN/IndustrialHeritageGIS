from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "jingmen_heritage_buildings_batch3_2024": {
        "source_type": "municipal_official_media",
        "title": "我市公布第三批历史建筑名录（23处）",
        "org": "荆门新闻网",
        "pub_date": None,
        "url": "https://www.jmnews.cn/news/2024/10/409495.shtml",
        "authority": "B",
        "notes": "2024年10月荆门市政府确定李氏老屋、李宜云老屋等23处建筑为荆门市第三批历史建筑：名单含工人文化宫旧址、荆门啤酒厂旧址、荆门炼油厂厂部旧址、石龙村砖圆仓、罗汉寺老场部、荆门市雕“满弓待发”、湖心亭、岚光阁、长沟桥及多处老宅祠堂等；报道为名称列表未附逐处详情。",
    },
}


RECORDS = [
    {
        "inventory_id": "HBI-JM-019",
        "name": "石龙村砖圆仓",
        "city": "荆门市",
        "district_county": None,
        "industry_category_l1": "粮食仓储工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "荆门市第三批历史建筑（2024年10月公布，23处之一）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["jingmen_heritage_buildings_batch3_2024"],
        "cultural_evidence": {
            "material_carriers": "砖砌圆筒粮仓（石龙村）；个数、容量与结构待现场测绘",
            "technical_memory": "砖圆仓为集体化时期粮食储备的典型构筑物形制，砌筑工艺与通风防潮设计代表当时粮仓建造水平",
            "social_memory": "乡村集体储粮与公粮征收记忆",
            "current_use_or_loss": "以第三批历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自荆门新闻网第三批名录报道（B级，名称列表）；石龙村所属乡镇、建造年代与所属粮站体系待官方名录详情核对；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_storage_site",
    },
    {
        "inventory_id": "HBI-JM-020",
        "name": "罗汉寺老场部",
        "city": "荆门市",
        "district_county": None,
        "industry_category_l1": "综合工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "荆门市第三批历史建筑（2024年10月公布，23处之一）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["jingmen_heritage_buildings_batch3_2024"],
        "cultural_evidence": {
            "material_carriers": "老场部建筑本体（罗汉寺）；建筑面积与结构待现场测绘",
            "technical_memory": "场部为计划经济时期国营场（农场/园艺场/蚕种场等）的管理中枢建筑；场属单位性质待核",
            "social_memory": "场部职工与周边村组的场社往来记忆",
            "current_use_or_loss": "以第三批历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自荆门新闻网第三批名录报道（B级，名称列表）；名录仅载“罗汉寺老场部”，所属场单位、行业性质与建造年代待官方名录详情核对，行业分类暂列综合工业；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_site",
    },
]


JM008_PATCH = {
    "source_keys_append": ["jingmen_heritage_buildings_batch3_2024"],
    "notes_append": "2024年荆门市第三批历史建筑名录（荆门新闻网报道名称列表）含“荆门啤酒厂旧址”，与本条金龙泉啤酒厂旧址（民主街）的空间关系按既有报道互证，名录详情核对后可确认同一性。",
}

JM012_PATCH = {
    "source_keys_append": ["jingmen_heritage_buildings_batch3_2024"],
    "notes_append": "2024年荆门市第三批历史建筑名录（荆门新闻网报道名称列表）含“工人文化宫旧址”，与本条对象对应，市级历史建筑身份待官方名录详情进一步确认。",
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
    updated = 0
    for record_id, patch in (("HBI-JM-008", JM008_PATCH), ("HBI-JM-012", JM012_PATCH)):
        record = next((row for row in records if row["inventory_id"] == record_id), None)
        if record is None:
            raise SystemExit(f"record not found: {record_id}")
        for key in patch["source_keys_append"]:
            if key not in record["source_keys"]:
                record["source_keys"].append(key)
                updated = 1
        if patch["notes_append"] not in record["notes"]:
            record["notes"] = record["notes"] + patch["notes_append"]
            updated = 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_bh_sources={len(SOURCES)} added_records={added} updated_records={updated} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
