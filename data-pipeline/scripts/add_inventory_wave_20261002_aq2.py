from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCE = {
    "wuhan_huazhong_mechanical_factory_2021": {
        "source_type": "municipal_history_official_pdf",
        "title": "华中工学院机械厂孵化记",
        "org": "武汉市政协文史资料",
        "pub_date": "2021-04-01",
        "url": "https://www.whzx.gov.cn/zxzl/wsl/202301/P020240129732649820544.pdf",
        "authority": "A",
        "notes": "武汉市政协文史资料官方PDF口述文章详细记载1954年武汉大学、湖南大学、南昌大学、广西大学实习工厂合并组建华中工学院机械厂，包含铸造、锻工、木模、金工、焊接、热处理车间和库房，生产水泵、车床、镗床并孵化电机厂，记录设备搬迁、工人培训和校办工厂社会记忆；原机械厂具体建筑保存、产权和开放条件待核。",
    }
}


RECORD = {
    "inventory_id": "HBI-WUHAN-067",
    "name": "华中工学院机械厂与实习工厂工业文化景观",
    "city": "武汉市",
    "district_county": "洪山区喻家山华中工学院旧校区（现华中科技大学，具体厂址待核）",
    "industry_category_l1": "教育实习与机械制造工业",
    "recognition_level": "research_candidate",
    "recognition_status": "武汉市政协文史资料官方口述史确认的校办机械厂与实习工厂谱系；未见法定工业遗产认定",
    "record_status": "source_confirmed",
    "geocode_status": "pending",
    "source_keys": ["wuhan_huazhong_mechanical_factory_2021"],
    "cultural_evidence": {
        "material_carriers": "华中工学院机械厂金工、锻工、铸工、焊接、热处理五个车间、库房、机床和搬迁设备；具体建筑、遗存设备与现校园空间待测绘",
        "technical_memory": "水泵、C617/C618车床、镗床、铸造、锻造、焊接、氮化热处理和电机制造技术；官方口述资料提供较完整工艺与设备谱系",
        "social_memory": "武汉大学/华中工学院师生实习、青年工人半工半读、师傅传艺、校办工厂与院系协作记忆；人物档案、校友口述和影像待采集",
        "current_use_or_loss": "机械厂曾因校园教学生活影响搬迁，后续空间、设备去向、产权和开放展示条件待校史档案与现场核验",
    },
    "notes": "本条将高校实习生产体系作为工业文化景观与档案载体登记，强调教育、生产和技术传承关系；官方口述史不等同于现存厂房完整保存或法定工业遗产认定。",
    "aliases": ["华中工学院机械厂", "华中工学院实习工厂", "武汉大学实习工厂", "华中科技大学机械厂"],
    "asset_kind": "industrial_education_landscape",
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
    if "wuhan_huazhong_mechanical_factory_2021" in sources and sources["wuhan_huazhong_mechanical_factory_2021"] != SOURCE["wuhan_huazhong_mechanical_factory_2021"]:
        raise SystemExit("conflicting source")
    sources.update(SOURCE)
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_aq2_sources=1 added_records={added} updated_records=0 total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
