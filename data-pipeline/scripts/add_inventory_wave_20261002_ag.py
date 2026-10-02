from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "xiangyang_air_compressor_residential_poi_2026": {
        "source_type": "third_party_poi_lead",
        "title": "湖北空压机厂生活区1栋 POI 线索",
        "org": "POI86（高德地图数据整理页）",
        "pub_date": None,
        "url": "https://www.poi86.com/poi/amap/street/16635/3.html",
        "authority": "D",
        "notes": "第三方POI页面检出‘湖北空压机厂生活区1栋’，页面所在街道为襄阳市樊城区米公街道语境；仅作生活区地址线索，未证明原厂房、厂界或遗产级别，需襄阳地方志、规划档案和现场核验。",
    },
    "yidu_mining_machinery_history_2024": {
        "source_type": "public_company_filing_history",
        "title": "湖北宜都运机机电股份有限公司公开转让说明书",
        "org": "全国中小企业股份转让系统公开披露材料",
        "pub_date": None,
        "url": "https://spdf.askci.com/831390-%E8%82%A1%E8%BD%AC%E4%B9%A6.pdf",
        "authority": "B",
        "notes": "公开披露材料中的人员履历记载1990—1993年曾在枝城市矿山机械厂从事锻压工作，补充宜都（原枝城）矿山机械厂的名称沿革和行业存在证据；未提供厂址边界、建筑设备或保护状态，保持档案线索层级。",
    },
}


UPDATES: dict[str, dict[str, Any]] = {
    "HBI-PROV-011": {
        "district_county": "襄阳市樊城区米公街道（生活区线索，具体厂界待核）",
        "source_keys": ["hubei_archive_machinery_1966", "xiangyang_air_compressor_residential_poi_2026"],
        "aliases": ["湖北省空气压缩机厂", "湖北空压机厂", "襄阳县农机厂"],
        "notes": "省档案馆1967年扩建设计任务书确认湖北空压机厂名称，第三方POI仅显示襄阳市樊城区米公街道‘湖北空压机厂生活区1栋’地址线索；厂房、生产区、设备、产权和现状仍待官方档案与现场核验。",
    },
    "HBI-YC-019": {
        "source_keys": ["hubei_archive_machinery_1966", "yidu_mining_machinery_history_2024"],
        "aliases": ["宜都矿山机械厂", "枝城市矿山机械厂"],
        "notes": "省档案馆1967年扩建设计任务书确认宜都矿山机械厂名称；公开披露材料记载1990—1993年枝城市矿山机械厂锻压从业经历，补足名称沿革交叉证据，但厂址、厂界、设备和保护状态仍待地方志与现场核验。",
    },
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    by_id = {row["inventory_id"]: row for row in records}
    for key, value in NEW_SOURCES.items():
        if key in sources and sources[key] != value:
            raise SystemExit(f"conflicting source: {key}")
        sources[key] = value
    for inventory_id, patch in UPDATES.items():
        if inventory_id not in by_id:
            raise SystemExit(f"missing update target: {inventory_id}")
        for key, value in patch.items():
            by_id[inventory_id][key] = value
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_ag_sources={len(NEW_SOURCES)} added_records=0 updated_records={len(UPDATES)} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
