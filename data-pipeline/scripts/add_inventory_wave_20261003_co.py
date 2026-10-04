from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


RECORD = {
    "inventory_id": "HBI-EZ-032",
    "name": "牛石岭礼堂",
    "city": "鄂州市",
    "district_county": "梁子湖区太和镇牛石村",
    "industry_category_l1": "工业社区",
    "recognition_level": "municipal_historical_building",
    "recognition_status": "鄂州市第一批历史建筑（鄂州政发〔2020〕13号，2020-12-28公布，名录第5项；1961年建）",
    "record_status": "source_confirmed",
    "geocode_status": "pending",
    "source_keys": ["ezhou_heritage_buildings_2020"],
    "cultural_evidence": {
        "material_carriers": "礼堂建筑本体（牛石岭，1961年，砖木结构、灰墙青瓦、两面坡式屋顶）；主体结构保持原貌，现为村民居住和大队办公使用；规模待现场测绘",
        "technical_memory": "1961年大队礼堂的砖木建筑工艺与集会功能空间布局",
        "social_memory": "牛石岭村集体集会、文艺活动与大队治理的公共记忆（名录简介载主体结构基本保持原貌）",
        "current_use_or_loss": "名录简介载现为村民居住和大队办公使用——礼堂功能延续的活态样本；以第一批历史建筑身份正式公布保护",
    },
    "notes": "直接取自鄂州政发〔2020〕13号名录表（A级，含逐处简介，第89批鄂州水利闸入库轮次同源核读）；与团风/石首/麻城礼堂群同为大集体公共建筑记录模式；名录简介载其仍在原功能延续使用；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
    "aliases": [],
    "asset_kind": "industrial_social_site",
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
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
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_co_added_records={added} total_records={len(records)} total_sources={len(data.get('sources', {}))}")


if __name__ == "__main__":
    main()
