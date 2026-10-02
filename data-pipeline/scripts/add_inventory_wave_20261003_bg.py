from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "ezhou_heritage_buildings_2020": {
        "source_type": "municipal_government_notice",
        "title": "市人民政府关于公布鄂州市第一批历史建筑的通知（鄂州政发〔2020〕13号，8处）",
        "org": "鄂州市人民政府门户网站",
        "pub_date": "2020-12-28",
        "url": "https://www.ezhou.gov.cn/gk/zc/gfxwj/ezzf/202012/t20201230_377265.html",
        "authority": "A",
        "notes": "鄂州政发〔2020〕13号将原人民银行鄂州支行（营业厅）等8处建筑确定为鄂州市第一批历史建筑，正文附名录表（含位置、年代与逐处简介）：第3项六十口闸（梁子湖区东沟镇六十村，1961年，灌排两用闸，顶部立“毛主席万岁”标语）、第4项磨刀矶节制闸（东沟镇磨刀矶村长港口，1977年动工1979年建成、1983年船闸通航，梁子湖通九十里长港咽喉、樊口电排站主要配套工程）；另有人民银行建筑2处、牛石岭礼堂、古井、老宅、祠堂。",
    },
}


RECORDS = [
    {
        "inventory_id": "HBI-EZ-030",
        "name": "六十口闸",
        "city": "鄂州市",
        "district_county": "梁子湖区东沟镇六十村",
        "industry_category_l1": "水利工程与泵站",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "鄂州市第一批历史建筑（鄂州政发〔2020〕13号名录第3项；1961年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["ezhou_heritage_buildings_2020"],
        "cultural_evidence": {
            "material_carriers": "两层灌排闸主体（陈家湾），顶部立“毛主席万岁”五个大字，闸基基础较好、主体保持原貌；闸孔尺寸与结构待现场测绘",
            "technical_memory": "1961年集体水利建设时期的灌排两用闸工法，涨水季节放水灌水的调蓄功能设计",
            "social_memory": "闸顶标语与集体兴修水利的年代记忆；梁子湖区圩区灌排生产传统",
            "current_use_or_loss": "以第一批历史建筑身份纳入保护体系；在用状态与保护范围待核",
        },
        "notes": "直接取自鄂州政发〔2020〕13号名录表（A级，逐处简介核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_utility_site",
    },
    {
        "inventory_id": "HBI-EZ-031",
        "name": "磨刀矶节制闸",
        "city": "鄂州市",
        "district_county": "梁子湖区东沟镇磨刀矶村",
        "industry_category_l1": "水利工程与泵站",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "鄂州市第一批历史建筑（鄂州政发〔2020〕13号名录第4项；1977年动工、1979年建成、1983年船闸通航）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["ezhou_heritage_buildings_2020"],
        "cultural_evidence": {
            "material_carriers": "节制闸与船闸组合枢纽（长港口）；闸体结构与启闭设备待现场测绘",
            "technical_memory": "梁子湖通九十里长港的咽喉枢纽，樊口电排站主要配套工程——节制排渍、通航功能一体的水利组合设计（1977年动工、1979年建成、1983年船闸通航）",
            "social_memory": "梁子湖区排渍除涝、长港航运与沿湖居民生产生活记忆",
            "current_use_or_loss": "名录载其建成以来为排除梁子湖区内渍水、解除洪涝灾害发挥重要作用；在用状态与保护范围待核",
        },
        "notes": "直接取自鄂州政发〔2020〕13号名录表（A级，逐处简介核读）；与底册荆江分洪闸（HBI-JZ-005）同属湖北水利枢纽脉络；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_utility_site",
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
    print(f"wave_bg_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
