from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "enshi_heritage_buildings_batch4_2025": {
        "source_type": "county_city_government_notice",
        "title": "恩施市人民政府关于公布第四批历史建筑的通知（14处）",
        "org": "恩施市人民政府门户网站",
        "pub_date": "2025-10-28",
        "url": "http://www.es.gov.cn/xxgk/gkml/qtzdgknr/tzgg/202510/t20251028_1747972.shtml",
        "authority": "A",
        "notes": "恩施市第四批历史建筑14处正文附名录表（含街道、地址、建筑类型列）：第2项四维街44号（建筑类型标注“旧厂房”）、第8项棉纺厂3栋厂房（六角亭街道薛家巷69号，旧厂房）；其余为四维街、三义宫巷、薛家巷传统民居。恩施市历史建筑已公布至第四批，第一至第三批名录待后续检索。",
    },
}


RECORDS = [
    {
        "inventory_id": "HBI-ES-020",
        "name": "恩施棉纺厂厂房（薛家巷69号，3栋）",
        "city": "恩施州",
        "district_county": "恩施市六角亭街道薛家巷",
        "industry_category_l1": "纺织工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "恩施市第四批历史建筑（2025年10月28日公布，名录第8项：棉纺厂3栋厂房，建筑类型旧厂房）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["enshi_heritage_buildings_batch4_2025"],
        "cultural_evidence": {
            "material_carriers": "棉纺厂厂房3栋（薛家巷69号）；厂房跨度、锯齿/桁架屋面形制与设备留存待现场测绘",
            "technical_memory": "恩施城区棉纺织工业的纺纱织布生产脉络；建厂与停产年代、企业全称待厂志与档案核验",
            "social_memory": "棉纺厂职工与恩施老城六角亭工业街区记忆",
            "current_use_or_loss": "以第四批历史建筑身份纳入保护体系，市政府要求做好挂牌、测绘和建档；现状用途待核",
        },
        "notes": "直接取自恩施市政府第四批名录正文表（A级，含建筑类型列）；名录未载棉纺厂建厂年代与企业沿革；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["恩施市棉纺厂"],
        "asset_kind": "industrial_building",
    },
    {
        "inventory_id": "HBI-ES-021",
        "name": "四维街44号旧厂房",
        "city": "恩施州",
        "district_county": "恩施市六角亭街道四维街",
        "industry_category_l1": "综合工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "恩施市第四批历史建筑（2025年10月28日公布，名录第2项，建筑类型标注旧厂房）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["enshi_heritage_buildings_batch4_2025"],
        "cultural_evidence": {
            "material_carriers": "旧厂房建筑本体（四维街44号）；面积、结构与原生产行业待现场测绘",
            "technical_memory": "名录建筑类型列标注“旧厂房”而名称作“民居”，名称与分类存在矛盾——原厂房所属企业与行业待官方档案核验，行业分类暂列综合工业",
            "social_memory": "四维街街区生产生活记忆",
            "current_use_or_loss": "以第四批历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自恩施市政府第四批名录正文表（A级，视觉核读原文）；名录第2项名称“四维街44号民居”与建筑类型“旧厂房”矛盾，按类型列收录并以旧厂房表述，名称矛盾待官方澄清；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_building",
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
    print(f"wave_bn_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
