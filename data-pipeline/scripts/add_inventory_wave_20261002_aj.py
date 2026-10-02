from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "enrichment" / "hubei_inventory.json"


NEW_SOURCE: dict[str, Any] = {
    "jingzhou_spark_factory_2021": {
        "source_type": "regional_media_industrial_history",
        "title": "湖北荆州：文旅融合促‘老厂房’升级‘工业遗产’",
        "org": "中国网/湖北",
        "pub_date": "2021-03-30",
        "url": "https://hb.china.com.cn/2021-03/30/content_41515156.htm",
        "authority": "C",
        "notes": "报道明确位于长港路的沙市荧光灯厂是荆州城区保留较完整的工业厂区，保存两根年代感烟囱和苏式厂房；同时将沙市老工业厂区与文旅保护利用讨论相连。来源为区域媒体报道，具体建筑、设备、产权和法定级别待官方档案与现场核验。",
    }
}


UPDATES = {
    "HBI-JZ-002": {
        "source_keys": ["jingzhou_old_factory", "jingzhou_spark_factory_2021"],
        "cultural_evidence": {
            "material_carriers": "沙市荧光灯厂长港路老厂区、苏式厂房和两根工业烟囱；报道确认城区保留较完整，具体车间、设备与厂界待测绘",
            "technical_memory": "荧光灯及照明器材制造、玻璃/电气生产和沙市轻工业技术组织；工艺档案与设备清单待补",
            "social_memory": "沙市轻工业城市、荧光灯厂职工与家属社区记忆；职工名册、口述史和老照片待采集",
            "current_use_or_loss": "报道将老厂区置于荆州工业遗产文旅保护利用讨论中，具体更新、产权、开放条件和环境风险待核",
        },
        "notes": "中国网湖北报道补充长港路沙市荧光灯厂保存较完整、苏式厂房和两根烟囱等对象级物质证据；原企业沿革、设备、厂界和法定级别仍待核。",
    }
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    by_id = {row["inventory_id"]: row for row in records}
    for key, value in NEW_SOURCE.items():
        if key in sources and sources[key] != value:
            raise SystemExit(f"conflicting source: {key}")
        sources[key] = value
    for inventory_id, patch in UPDATES.items():
        if inventory_id not in by_id:
            raise SystemExit(f"missing update target: {inventory_id}")
        for key, value in patch.items():
            by_id[inventory_id][key] = value
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_aj_sources=1 added_records=0 updated_records=1 total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
