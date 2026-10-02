from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCE = {
    "hubei_third_ic_engine_archive_2026": {
        "source_type": "university_archive_official",
        "title": "湖北工业大学档案馆全宗简介",
        "org": "湖北工业大学档案馆",
        "pub_date": None,
        "url": "https://dag.hbut.edu.cn/bggk/qzjj.htm",
        "authority": "A",
        "notes": "湖北工业大学档案馆官方页面明确设有湖北第三内燃机配件厂全宗，保存该厂1970年成立至1990年并入学校机械总厂期间，以及1991—2012年机械总厂撤销期间形成的档案，近1万卷；用于登记档案型工业文化载体，不替代原厂址、建筑和设备现场核验。",
    }
}


RECORD = {
    "inventory_id": "HBI-WUHAN-066",
    "name": "湖北第三内燃机配件厂档案与工业文化谱系",
    "city": "武汉市",
    "district_county": "湖北工业大学/原湖北农业机械专科学校关联区域（具体厂址待核）",
    "industry_category_l1": "内燃机配件与机械制造工业",
    "recognition_level": "research_candidate",
    "recognition_status": "湖北工业大学档案馆官方全宗确认的企业与机械总厂档案载体；未见法定工业遗产认定",
    "record_status": "source_confirmed",
    "geocode_status": "pending",
    "source_keys": ["hubei_third_ic_engine_archive_2026"],
    "cultural_evidence": {
        "material_carriers": "湖北第三内燃机配件厂1970—1990年厂档、1991—2012年机械总厂档案近1万卷；原厂房、设备、实验工厂和校内机械总厂空间待核",
        "technical_memory": "内燃机配件、机械加工、学校实习工厂与机械总厂生产技术；档案分类、产品、设备和工艺资料可供后续调阅",
        "social_memory": "农业机械教育、实习工厂、技术工人、师生和机械总厂组织变迁记忆；人物、职工与校友口述待采集",
        "current_use_or_loss": "1990年并入学校机械总厂，2012年机械总厂撤销；档案仍由高校档案馆保存，实体厂址、产权、开放条件和可展示物项待核",
    },
    "notes": "本条将官方档案全宗作为工业文化载体登记，保留档案与实体空间的边界；档案馆全宗的存在不等同于原生产厂房完整保存或已获工业遗产认定。",
    "aliases": ["湖北第三内燃机配件厂", "湖北农机专科学校实习工厂", "湖北工业大学机械总厂"],
    "asset_kind": "industrial_archive",
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    by_id = {row["inventory_id"]: row for row in records}
    if RECORD["inventory_id"] in by_id:
        if by_id[RECORD["inventory_id"]] != RECORD:
            raise SystemExit("conflicting duplicate record")
        added = 0
    else:
        if RECORD["name"] in {row["name"] for row in records}:
            raise SystemExit("conflicting duplicate name")
        records.append(RECORD)
        added = 1
    if "hubei_third_ic_engine_archive_2026" in sources and sources["hubei_third_ic_engine_archive_2026"] != SOURCE["hubei_third_ic_engine_archive_2026"]:
        raise SystemExit("conflicting source")
    sources.update(SOURCE)
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_aq_sources=1 added_records={added} updated_records=0 total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
