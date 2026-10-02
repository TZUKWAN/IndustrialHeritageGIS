from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "yingshan_heritage_buildings_2023": {
        "source_type": "county_government_notice",
        "title": "关于英山县第二批10处历史建筑的公示（附英山县城区第二批历史建筑名录）",
        "org": "英山县住房和城乡建设局（英山县政府网）",
        "pub_date": "2023-08-29",
        "url": "https://www.chinays.gov.cn/zwgk/grassroots/6636628/1381297.html",
        "authority": "A",
        "notes": "县住建局联合县文旅局经普查遴选拟将伍家冲村石拱桥等十处纳入英山县城区第二批历史建筑，公示期2023-08-29至09-04；附件doc名录载明：渡槽（草盘地镇茶场村一组，1958年，引大沟水库水灌溉，人工石砌，高11米石柱、长15.6米水渠）、同二老茶场（红山镇黄泥岗村二组，1975年，农业学大寨时期英山首个茶叶特色产业园的根据地与办公楼、唯一保留印证）；另含石拱桥、青石桥、古民居、故居等。附件doc已下载核读，本地存档 raw/yingshan_heritage/。",
    },
}


RECORDS = [
    {
        "inventory_id": "HBI-HG-017",
        "name": "草盘地镇茶场村渡槽",
        "city": "黄冈市",
        "district_county": "英山县草盘地镇茶场村",
        "industry_category_l1": "水利工程与泵站",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "英山县城区第二批历史建筑（2023年8月29日公示，名录YSLSJZ004；1958年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["yingshan_heritage_buildings_2023"],
        "cultural_evidence": {
            "material_carriers": "人工石砌渡槽：高11米石柱、长15.6米水渠，将大沟水库之水引至茶场村无河塆灌田；整体保存状况待现场测绘",
            "technical_memory": "1958年农田水利建设时期全人工采石、砌筑的引水渡槽建造工艺，大别山山区自流灌溉工程的代表",
            "social_memory": "茶场村集体投工投劳兴修水利的记忆；渡槽至今见证山区农业灌溉史",
            "current_use_or_loss": "以县级历史建筑身份纳入保护公示名单；在用/停用与保护范围待核",
        },
        "notes": "直接取自英山县住建局第二批历史建筑名录附件doc（A级，已核读）；公示层级（2023年公示）后续是否正式认定待跟踪；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_utility_site",
    },
    {
        "inventory_id": "HBI-HG-018",
        "name": "同二老茶场办公楼",
        "city": "黄冈市",
        "district_county": "英山县红山镇黄泥岗村",
        "industry_category_l1": "茶业种植与原料生产",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "英山县城区第二批历史建筑（2023年8月29日公示，名录YSLSJZ008；1975年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["yingshan_heritage_buildings_2023"],
        "cultural_evidence": {
            "material_carriers": "老茶场办公楼建筑本体（黄泥岗村二组），名录注其引进外国建筑设计风格；建筑面积与保存状态待现场测绘",
            "technical_memory": "1970年代英山茶叶特色产业园区建设时期的园区办公与管理制度载体，农业学大寨开田改地运动中茶产业基地建设的物证",
            "social_memory": "县委书记驻点黄泥岗村（满溪坪公社同二大队）号召开田改地的集体记忆；名录称其为英山首个茶叶特色产业园唯一保留下来的印证",
            "current_use_or_loss": "以县级历史建筑身份纳入保护公示名单；现状用途（闲置/再利用）待核",
        },
        "notes": "直接取自英山县住建局第二批历史建筑名录附件doc（A级，已核读）；英山为产茶县，本条与底册英山制丝针织厂对象分别代表英山茶业与丝绸工业脉络；公示层级后续是否正式认定待跟踪；坐标未核验保持待核。",
        "aliases": ["同二老茶场"],
        "asset_kind": "industrial_site",
    },
]


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
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_az_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
