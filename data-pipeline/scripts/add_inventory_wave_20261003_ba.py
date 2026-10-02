from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "luotian_heritage_buildings_2024": {
        "source_type": "county_government_notice",
        "title": "关于罗田县第三批历史建筑的公示（附罗田县第三批备选历史建筑名录33处）",
        "org": "罗田县住房和城乡建设局（罗田县政府网）",
        "pub_date": "2024-05-11",
        "url": "http://www.luotian.gov.cn/zwgk/grassroots/6636850/1376583.html",
        "authority": "A",
        "notes": "罗田县第三批33处县级历史建筑公示（公示期2024-05-11至20），正文附名录表：第33项薄刀峰林场工区管理用房旧址（薄刀峰林场，60年代）为林业工业对象；第32项罗田县“五七”干校旧址（九资河张家咀村，1972年）与第22项知青点（三里畈车潭畈村村部，60年代）为年代史迹，生产性构成未在名录中明示；其余30处为古民居、祠堂、寺庙、戏楼、故居等传统建筑。另核读团风县第二批历史建筑公示（2023-07-27，tfzf.gov.cn）：13处均为水晶坳村民居，无工业对象（负结果记录）。",
    },
}


RECORD = {
    "inventory_id": "HBI-HG-019",
    "name": "薄刀峰林场工区管理用房旧址",
    "city": "黄冈市",
    "district_county": "罗田县薄刀峰林场",
    "industry_category_l1": "林业开发与木材生产",
    "recognition_level": "municipal_historical_building",
    "recognition_status": "罗田县第三批历史建筑（2024年5月11日至20日公示，名录第33项；60年代建）",
    "record_status": "source_confirmed",
    "geocode_status": "pending",
    "source_keys": ["luotian_heritage_buildings_2024"],
    "cultural_evidence": {
        "material_carriers": "薄刀峰林场工区管理用房旧址建筑本体（薄刀峰林场场部）；栋数、建筑面积与保存状态待现场测绘",
        "technical_memory": "大别山山区国营林场开发时期的工区管理与木材生产组织载体；建场沿革与伐木、运输、育林工艺档案待补",
        "social_memory": "林场职工扎根山区护林育林的生产生活记忆，与罗田山区林业开发史互证",
        "current_use_or_loss": "以县级历史建筑身份纳入保护公示名单；旧址现状用途与保存边界待核",
    },
    "notes": "直接取自罗田县住建局第三批备选历史建筑名录正文表（A级，已核读）；与神农架林业系列、断江坪伐木队线索同属湖北林业工业脉络；公示层级后续是否正式认定待跟踪；名录未载林场建场年代与工区构成；坐标未核验保持待核。",
    "aliases": [],
    "asset_kind": "industrial_site",
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    existing = next((row for row in records if row["inventory_id"] == RECORD["inventory_id"]), None)
    if existing is not None:
        if existing != RECORD:
            raise SystemExit("conflicting duplicate record")
        added = 0
    else:
        if any(row["name"] == RECORD["name"] for row in records):
            raise SystemExit("conflicting duplicate name")
        records.append(RECORD)
        added = 1
    for key, source in SOURCES.items():
        if key in sources and sources[key] != source:
            raise SystemExit(f"conflicting source: {key}")
    sources.update(SOURCES)
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_ba_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
