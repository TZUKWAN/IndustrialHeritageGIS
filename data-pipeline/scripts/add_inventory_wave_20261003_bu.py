from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


RECORDS = [
    {
        "inventory_id": "HBI-ES-033",
        "name": "建始县老电厂旧址（“和美小镇”城市更新项目）",
        "city": "恩施州",
        "district_county": "建始县（业州镇，具体厂址待核）",
        "industry_category_l1": "火力发电",
        "recognition_level": "city_update",
        "recognition_status": "州住建局“县市联播”报道的老电厂城市更新活化项目（“和美小镇”）；未见历史建筑或工业遗产法定认定",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["enshi_zjw_428_2026"],
        "cultural_evidence": {
            "material_carriers": "老电厂厂房与设备遗存（业州镇，具体厂址与保留范围待现场测绘）",
            "technical_memory": "县域小火电的发电供电技术记忆与建始县电气化历程",
            "social_memory": "电厂职工与县城“点灯记忆”",
            "current_use_or_loss": "州住建局“县市联播”2026年8月报道老电厂改造“和美小镇”城市更新项目；改造方案与保留清单待核",
        },
        "notes": "直接取自州住建局县市联播报道（A级，智能体核读）；活化项目参照层级入库（同仙桃低效工业载体模式），不推断法定认定；厂址门牌与建设年代待核；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_building",
    },
    {
        "inventory_id": "HBI-ES-034",
        "name": "利川市原复烤仓储基地烟囱（38米，改造“温度计”地标）",
        "city": "恩施州",
        "district_county": "利川市（复烤仓储基地片区）",
        "industry_category_l1": "烟叶复烤与烟草加工",
        "recognition_level": "city_update",
        "recognition_status": "州住建局“县市联播”报道的复烤仓储基地城市更新活化项目（38米排气烟囱改造为“温度计”地标）；未见历史建筑或工业遗产法定认定",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["enshi_zjw_428_2026"],
        "cultural_evidence": {
            "material_carriers": "复烤仓储基地38米排气烟囱（改造为城市“温度计”地标）及基地仓储建筑；与 HBI-ES-014 利川市烟叶复烤厂旧址（滨江北路片区）的空间关系待核",
            "technical_memory": "烟叶复烤与仓储的排烟、储运工艺设施；烟囱地标化改造的工业构筑物再利用手法",
            "social_memory": "利川烟叶复烤产业职工与城市工业地标记忆",
            "current_use_or_loss": "州住建局“县市联播”2026年8月报道烟囱改造“温度计”城市更新项目；改造范围与基地其他建筑处置待核",
        },
        "notes": "直接取自州住建局县市联播报道（A级，智能体核读）；活化项目参照层级入库，不推断法定认定；与 HBI-ES-014 的空间/隶属关系待核（防重复登记）；坐标未核验保持待核。",
        "aliases": ["利川复烤厂烟囱"],
        "asset_kind": "industrial_utility_site",
    },
]


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
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
    print(f"wave_bu_added_records={added} total_records={len(records)} total_sources={len(data.get('sources', {}))}")


if __name__ == "__main__":
    main()
