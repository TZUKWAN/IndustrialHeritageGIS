from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


def _gs(record_id: str, name: str, cat: str, material: str, tech: str, social: str, use: str, notes: str, aliases: list) -> dict:
    return {
        "inventory_id": record_id,
        "name": name,
        "city": "随州市",
        "district_county": "广水市（具体门牌待测绘建档成果核验）",
        "industry_category_l1": "食品加工工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "广水市新增历史建筑（2024年，广政函〔2024〕6号批复新增20处之一，政采合同附件按典型测绘列名；正式名录文件政府门户未公开）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["guangshui_survey_contract_2025", "suizhou_bai_ri_action_2024"],
        "cultural_evidence": {
            "material_carriers": material,
            "technical_memory": tech,
            "social_memory": social,
            "current_use_or_loss": use,
        },
        "notes": "名单源自政采合同附件（政府门户暂无名录公布文件，批复广政函〔2024〕6号未见主动公开版本）；传统食品手工作坊（合同测绘分项标注），作坊本体保存与经营延续待测绘建档成果核验；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": aliases,
        "asset_kind": "industrial_building",
    }


RECORDS = [
    _gs(
        "HBI-SZ-015",
        "麻市老豆腐作坊",
        "食品加工工业",
        "传统豆腐制作作坊建筑本体（麻市，即广水马坪/麻竹市一带传统集镇称谓待测绘成果核验）；石磨、灶台与晾晒设施留存待现场测绘",
        "广水传统豆腐手工制作工艺（泡豆、磨浆、点卤、压制成型）",
        "麻市集镇豆制品供应与乡宴饮食记忆",
        "2024年经广政函〔2024〕6号批复新增为历史建筑（典型测绘），2025年完成测绘建档；经营是否延续待核",
        "名单源自政采合同附件（政府门户暂无名录公布文件，批复广政函〔2024〕6号未见主动公开版本）；传统食品手工作坊（合同测绘分项标注），作坊本体保存与经营延续待测绘建档成果核验；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["麻市豆腐坊"],
    ),
    _gs(
        "HBI-SZ-016",
        "麻市老手工面条铺",
        "食品加工工业",
        "传统手工面条铺建筑本体（铺面、晾晒架与和面灶台）；保存状态待现场测绘",
        "广水传统手工切面/银丝面制作工艺（和面、揉压、晾晒、切制）",
        "麻市集镇面条铺与广待人早餐（热干面/汤面）食材供应记忆",
        "2024年经广政函〔2024〕6号批复新增为历史建筑（典型测绘），2025年完成测绘建档；经营是否延续待核",
        "名单源自政采合同附件（政府门户暂无名录公布文件，批复广政函〔2024〕6号未见主动公开版本）；传统食品手工作坊（合同测绘分项标注），作坊本体保存与经营延续待测绘建档成果核验；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["麻市面条铺"],
    ),
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
    print(f"wave_cf_added_records={added} total_records={len(records)} total_sources={len(data.get('sources', {}))}")


if __name__ == "__main__":
    main()
