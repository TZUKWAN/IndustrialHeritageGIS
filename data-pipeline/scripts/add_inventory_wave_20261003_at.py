from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCE_UPDATE = {
    "hubei_archive_machinery_1966": {
        "source_type": "provincial_archive_catalog",
        "title": "湖北省工业厅工业企业设计任务书档案目录",
        "org": "湖北省档案馆",
        "pub_date": None,
        "url": "https://www.hbda.gov.cn/searchitembykey/207_8.jspx?page=3517",
        "authority": "A",
        "accessed_date": "2026-10-03",
        "notes": "省档案馆开放目录（第3517页，2026-10-03实读）列出1963—1967年形成的工业设计和基建档案，其中：档号SZ 90-1-279（1966，永久）《关于湖北省油泵厂、湖北省齿轮厂、沙市三厂(拖拉机厂)、长江配件厂、湖北省柴油机厂设计任务书的批复》；档号SZ 90-1-280（1966，永久）《湖北省工业厅关于湖北省拖拉机厂设计任务书和扩大设计任务书批复》；档号SZ 90-1-281（1967，永久）列湖北空压机厂、湖北省油泵厂、郧县风动工具厂、宜都矿山机械厂等扩建设计任务书。目录另见油泵厂、齿轮厂、长江配件厂等名称。pub_date留空以区分档案形成年度与网页发布日期。题名可核，实体位置、厂界和保存状态待调档与现场核验；目录题名不推断实体存续。",
    }
}


RECORD_UPDATE = {
    "HBI-JZ-017": {
        "recognition_status": "湖北省档案馆开放目录档号SZ 90-1-279（1966年批复，永久）题名《关于湖北省油泵厂、湖北省齿轮厂、沙市三厂(拖拉机厂)、长江配件厂、湖北省柴油机厂设计任务书的批复》——档案题名明确“沙市三厂”即拖拉机厂建设主体；未见实体和法定工业遗产认定",
    }
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    updated_sources = 0
    for key, source in SOURCE_UPDATE.items():
        current = sources.get(key)
        if current == source:
            continue
        if current is None:
            raise SystemExit(f"source not found: {key}")
        sources[key] = source
        updated_sources += 1
    updated_records = 0
    for record_id, patch in RECORD_UPDATE.items():
        record = next((row for row in records if row["inventory_id"] == record_id), None)
        if record is None:
            raise SystemExit(f"record not found: {record_id}")
        if record.get("recognition_status") == patch["recognition_status"]:
            continue
        record.update(patch)
        updated_records += 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_at_updated_sources={updated_sources} updated_records={updated_records} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
