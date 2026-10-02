from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "xiantao_heritage_buildings_2024": {
        "source_type": "municipal_official_media",
        "title": "调查：从藏在“深闺”到挂牌保护 仙桃历史建筑如何“活”在当下？",
        "org": "中国仙桃网（仙桃周刊融媒体）",
        "pub_date": "2024-07-12",
        "url": "http://www.cnxiantao.com/wsd/202407/t20240712_431142.html",
        "authority": "B",
        "notes": "2024年7月9日仙桃市住房和城市更新局启动历史建筑挂牌，对前期认定并公示的“胡海林老屋”等32处建筑物实地挂牌；报道实地探访记录沙湖泵站通顺河节制闸（始建于1974年，至今汛期仍正常使用）与沙湖原种场火脑沟分场合心水塔（1991年始建，曾供7个村民小组生活用水，现停用但塔体完好）；名单含粮仓、水塔、涵闸、影剧院、信用社等特定年代城市记忆点；渔泛村历史建筑以用促保为例。",
    },
}


RECORDS = [
    {
        "inventory_id": "HBI-XT-008",
        "name": "合心水塔",
        "city": "仙桃市",
        "district_county": "沙湖原种场火脑沟分场",
        "industry_category_l1": "城镇供水基础设施",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "仙桃市历史建筑（2024年7月9日市住房和城市更新局实地挂牌保护，此前认定并公示的32处之一；1991年始建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["xiantao_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "塔体完好的村镇供水水塔一座，位于沙湖原种场火脑沟分场；塔高、结构形式与精确位置待现场测绘",
            "technical_memory": "1991年建成的分场集中供水设施，代表村镇自来水普及时期的供水工程技术与施工工艺；构造细节待补",
            "social_memory": "曾为火脑沟分场7个村民小组提供生活用水，“卸任多年”后仍是分场居民共同生活记忆地标",
            "current_use_or_loss": "已停用多年，塔体周遭长满草木但本体依旧完好；2024年列入仙桃市历史建筑挂牌保护，后续修缮与活化利用方案由市住房和城市更新局及属地推进，具体范围待核",
        },
        "notes": "来自中国仙桃网历史建筑挂牌调查报道的实地探访记录；历史建筑挂牌保护不等于文物保护单位或工业遗产法定认定；塔体结构、产权与保护范围待核；坐标未核验保持待核。",
        "aliases": ["沙湖原种场合心水塔"],
        "asset_kind": "industrial_utility_site",
    },
]


XT007_PATCH = {
    "source_keys_append": ["xiantao_heritage_buildings_2024"],
    "cultural_evidence_material_carriers": "大垸子、沙湖泵站的泵房、闸站、老旧办公宿舍及配套水利设施；2024年挂牌调查报道确认沙湖泵站通顺河节制闸始建于1974年、至今汛期仍正常节制河水；公开报道未列完整单体清单和坐标",
    "notes": "省自然资源厅报道整合仙桃市大垸子、沙湖泵站闲置土地、老旧办公宿舍，改造老旧水利设施为水利产教融合实训课堂；本条将其作为水利工业文化景观群记录，不把项目规划直接等同于泵站文保或工业遗产认定。2024年7月中国仙桃网挂牌调查报道补入沙湖泵站通顺河节制闸年代与使用状态；节制闸是否属于32处挂牌名单报道未明示，待官方名单核对。",
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
    xt007 = next((row for row in records if row["inventory_id"] == "HBI-XT-007"), None)
    if xt007 is None:
        raise SystemExit("record not found: HBI-XT-007")
    updated = 0
    for key in XT007_PATCH["source_keys_append"]:
        if key not in xt007["source_keys"]:
            xt007["source_keys"].append(key)
            updated = 1
    carriers_key = "cultural_evidence_material_carriers"
    if xt007["cultural_evidence"]["material_carriers"] != XT007_PATCH[carriers_key]:
        xt007["cultural_evidence"]["material_carriers"] = XT007_PATCH[carriers_key]
        updated = 1
    if xt007["notes"] != XT007_PATCH["notes"]:
        xt007["notes"] = XT007_PATCH["notes"]
        updated = 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_au_sources={len(SOURCES)} added_records={added} updated_records={updated} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
