from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


RECORDS = [
    {
        "inventory_id": "HBI-JZ-027",
        "name": "长江大学东校区院内水塔",
        "city": "荆州市",
        "district_county": "荆州区（长江大学东校区）",
        "industry_category_l1": "城镇供水基础设施",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "荆州市历史建筑（2024年新增35处名录第123项）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["jingzhou_heritage_2024_35"],
        "cultural_evidence": {
            "material_carriers": "校园供水水塔建筑本体（长江大学东校区院内）；高度、结构与建造年代待现场测绘",
            "technical_memory": "高校校区自建供水系统的水塔构筑物，代表集中供水时代校园基础设施形制",
            "social_memory": "长江大学东校区（原湖北农学院等院校办学史）师生生活记忆地标",
            "current_use_or_loss": "以市级历史建筑身份纳入保护体系；在用/退役状态待核",
        },
        "notes": "直接取自2024年新增35处名录附件图第123项（A级，视觉核读）；名录未载建造年代；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_utility_site",
    },
    {
        "inventory_id": "HBI-JZ-028",
        "name": "新垸水塔",
        "city": "荆州市",
        "district_county": None,
        "industry_category_l1": "城镇供水基础设施",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "荆州市历史建筑（2024年新增35处名录第125项）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["jingzhou_heritage_2024_35"],
        "cultural_evidence": {
            "material_carriers": "水塔建筑本体；位置、高度与结构待现场测绘（名录未附地址列）",
            "technical_memory": "村镇/社区集中供水水塔构筑物形制",
            "social_memory": "当地居民集中供水生活记忆",
            "current_use_or_loss": "以市级历史建筑身份纳入保护体系；在用/退役状态待核",
        },
        "notes": "直接取自2024年新增35处名录附件图第125项（A级，视觉核读）；名录未载地址与年代，具体位置待官方建档资料核对；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_utility_site",
    },
    {
        "inventory_id": "HBI-JZ-029",
        "name": "李埠水塔",
        "city": "荆州市",
        "district_county": "荆州区李埠镇（据名称推断，待核）",
        "industry_category_l1": "城镇供水基础设施",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "荆州市历史建筑（2024年新增35处名录第126项）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["jingzhou_heritage_2024_35"],
        "cultural_evidence": {
            "material_carriers": "水塔建筑本体；位置、高度与结构待现场测绘（名录未附地址列）",
            "technical_memory": "村镇集中供水水塔构筑物形制",
            "social_memory": "李埠一带居民集中供水生活记忆",
            "current_use_or_loss": "以市级历史建筑身份纳入保护体系；在用/退役状态待核",
        },
        "notes": "直接取自2024年新增35处名录附件图第126项（A级，视觉核读）；名录未载地址与年代，所在乡镇按名称推断并标注待核；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_utility_site",
    },
    {
        "inventory_id": "HBI-JZ-030",
        "name": "源通运业有限公司办公楼",
        "city": "荆州市",
        "district_county": None,
        "industry_category_l1": "工业仓储与运输",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "荆州市历史建筑（2024年新增35处名录第132项）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["jingzhou_heritage_2024_35"],
        "cultural_evidence": {
            "material_carriers": "运输企业办公楼建筑本体；面积、结构与建造年代待现场测绘",
            "technical_memory": "公路运输企业的经营办公建筑，与荆州货运流通体系相关",
            "social_memory": "运输企业职工与荆州客货运记忆",
            "current_use_or_loss": "以市级历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自2024年新增35处名录附件图第132项（A级，视觉核读）；名录未载地址与年代，企业沿革待地方志核验；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["源通运业"],
        "asset_kind": "industrial_building",
    },
    {
        "inventory_id": "HBI-JZ-031",
        "name": "江陵车站钟楼",
        "city": "荆州市",
        "district_county": None,
        "industry_category_l1": "铁路交通工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "荆州市历史建筑（2024年新增35处名录第130项）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["jingzhou_heritage_2024_35"],
        "cultural_evidence": {
            "material_carriers": "车站钟楼建筑本体（江陵车站配套）；钟楼高度、钟面构造与保存状态待现场测绘",
            "technical_memory": "车站钟楼作为铁路时刻与站房标识的构筑物传统；江陵车站沿革（沙市—江陵铁路谱系）待铁路志核验",
            "social_memory": "车站旅客候车闻钟与城市门户记忆",
            "current_use_or_loss": "以市级历史建筑身份纳入保护体系；车站运营状态与钟楼在用情况待核",
        },
        "notes": "直接取自2024年新增35处名录附件图第130项（A级，视觉核读）；名录未载地址与年代，与下陆火车站旧址（HBI-HS-019）同属铁路交通遗存记录模式；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["江陵火车站钟楼"],
        "asset_kind": "industrial_transport_site",
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
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_bs_added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
