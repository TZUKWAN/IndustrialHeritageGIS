from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    row = next(item for item in data["records"] if item["inventory_id"] == "HBI-PROV-011")
    row["city"] = "襄阳市"
    row["district_county"] = "樊城区米公街道（生活区线索，具体厂界待核）"
    row["recognition_status"] = "省档案馆设计任务书与第三方POI共同提供的襄阳企业/生活区线索；未见实体和法定工业遗产认定"
    row["notes"] = "省档案馆1967年扩建设计任务书确认湖北空压机厂名称，第三方POI显示襄阳市樊城区米公街道‘湖北空压机厂生活区1栋’地址线索；城市归属据此校正为襄阳市，但厂房、生产区、设备、产权和现状仍待官方档案与现场核验。"
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_am_sources=0 added_records=0 updated_records=1 total_records={len(data['records'])} total_sources={len(data['sources'])}")


if __name__ == "__main__":
    main()
