from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


def _jz(record_id: str, name: str, dc: str, cat: str, no: str, kind: str, material: str, tech: str, social: str, use: str, notes: str, aliases: list) -> dict:
    return {
        "inventory_id": record_id,
        "name": name,
        "city": "荆州市",
        "district_county": dc,
        "industry_category_l1": cat,
        "recognition_level": "municipal_historical_building",
        "recognition_status": f"荆州市中心城区历史建筑（2019年9月30日市政府公布100处名录第{no}项）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["jingzhou_heritage_buildings_2019"],
        "cultural_evidence": {
            "material_carriers": material,
            "technical_memory": tech,
            "social_memory": social,
            "current_use_or_loss": use,
        },
        "notes": notes,
        "aliases": aliases,
        "asset_kind": kind,
    }


RECORDS = [
    _jz("HBI-JZ-042", "观音矶", "沙市区（荆江大堤）", "水利工程与泵站", "60",
        "industrial_utility_site",
        "荆江大堤重要矶头（观音矶，又名象鼻矶），矶头挑流石砌体与矶身条石护坡；矶长与砌体规模待水利部门资料核补",
        "荆江防洪工程体系的关键挑流节点，矶头挑流护岸的水工技术，为新中国成立后荆江分洪与大堤加固工程的重要观测点",
        "1998年抗洪等历次荆江防汛的集体记忆地标，沙市市民江边观水 first 地标",
        "以中心城区历史建筑身份纳入保护体系；水利工程运行管理现状待水利部门核",
        "直接取自2019年市政府100处名录（B级转载全文核读）；观音矶为荆江大堤著名险工段矶头，水利技术参数待水利志核补；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["象鼻矶"],
    ),
    _jz("HBI-JZ-043", "总工会职工剧场", "沙市区", "工业社区文化", "58",
        "industrial_social_site",
        "职工剧场建筑本体（总工会所属），观众厅与舞台格局待现场测绘",
        "工会系统职工文化设施的剧场建筑形制，职工文艺汇演与电影放映功能载体",
        "沙市工业系统职工文艺生活与工会文化服务记忆",
        "以中心城区历史建筑身份纳入保护体系；现状用途（演出/放映/改造）待核",
        "直接取自2019年市政府100处名录（B级转载全文核读）；与茅箭工人文化宫（HBI-SY-039）、荆门工人文化宫（HBI-JM-012）同为职工文化设施记录模式；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    _jz("HBI-JZ-044", "黄州会馆", "沙市区", "历史水运、码头与城市商贸", "99",
        "industrial_trade_site",
        "会馆建筑本体，戏楼/正殿/厢房格局待现场测绘",
        "黄州商帮在沙市的行会会馆，见证长江中游商帮贸易与码头集散的组织形态（同类参照汉口黄州会馆脉络）",
        "黄州商帮客商聚议、寄寓与乡土认同的商贸组织记忆",
        "以中心城区历史建筑身份纳入保护体系；现状用途待核",
        "直接取自2019年市政府100处名录（B级转载全文核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
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
    print(f"wave_bz_added_records={added} total_records={len(records)} total_sources={len(data.get('sources', {}))}")


if __name__ == "__main__":
    main()
