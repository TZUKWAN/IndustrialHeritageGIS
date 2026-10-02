from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "qichun_chain_factory_history_2016": {
        "source_type": "third_party_enterprise_directory",
        "title": "湖北三虎链条有限公司企业沿革线索",
        "org": "企业目录网站",
        "pub_date": None,
        "url": "https://www.ypshop.net/list--91----search-1551-.html",
        "authority": "D",
        "notes": "第三方企业目录称湖北三虎链条有限公司由原国有湖北链条厂派生，地址指向湖北省蕲春县漕河镇六房湾村；来源可能为企业黄页转载，不能单独证明旧厂址、厂界或改制关系。",
    },
    "qichun_chain_restructuring_2016": {
        "source_type": "regional_media_enterprise_restructuring",
        "title": "湖北蕲春‘明星企业家’夫妻涉嫌诈骗1.7亿元（链条厂沿革段）",
        "org": "区域媒体转载",
        "pub_date": None,
        "url": "https://mxgxt.com/news/view/1880133",
        "authority": "D",
        "notes": "区域媒体转载材料提到2006年虎牌链条由原湖北链条厂改制、承租车间和收购工厂的叙述；内容涉及案件报道，作为企业改制线索交叉来源使用，不作为遗产认定或事实终局证明。",
    },
}


NEW_RECORD = {
    "inventory_id": "HBI-HG-014",
    "name": "蕲春县湖北链条厂旧址（线索）",
    "city": "黄冈市",
    "district_county": "蕲春县漕河镇（具体厂址待核）",
    "industry_category_l1": "机械传动与链条制造工业",
    "recognition_level": "archive_lead",
    "recognition_status": "省政府公报与低权重企业资料共同提供的历史企业线索；未见实体和法定工业遗产认定",
    "record_status": "source_lead",
    "geocode_status": "pending",
    "source_keys": ["hubei_industry_export_1989", "qichun_chain_factory_history_2016", "qichun_chain_restructuring_2016"],
    "cultural_evidence": {
        "material_carriers": "湖北链条厂/后续链条企业的厂房、车间、设备和职工设施待地方志、档案与现场核验",
        "technical_memory": "工业链条、滚子链、输送链和机械传动产品制造技术；设备、工艺和产品谱系待厂志核实",
        "social_memory": "蕲春漕河镇国有工业、链条厂职工和企业改制记忆；职工社区、口述史和老照片待采集",
        "current_use_or_loss": "省政府公报确认历史企业名称，第三方资料提示后续改制与漕河镇地址线索；现厂区、产权、停产/改制和利用状态待核",
    },
    "notes": "省政府公报的‘湖北链条厂’名单线索与低权重企业资料对蕲春漕河镇、三虎/虎牌链条改制的描述尚未完成档案交叉核验；本条严格保持source_lead，不将企业新闻或黄页信息直接写成正式遗产事实。",
    "aliases": ["湖北链条厂", "蕲春链条厂", "湖北三虎链条", "虎牌链条"],
    "asset_kind": "industrial_site",
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    by_id = {row["inventory_id"]: row for row in records}
    if NEW_RECORD["inventory_id"] in by_id:
        if by_id[NEW_RECORD["inventory_id"]] != NEW_RECORD:
            raise SystemExit("conflicting duplicate record")
        added = 0
    else:
        if NEW_RECORD["name"] in {row["name"] for row in records}:
            raise SystemExit("conflicting duplicate name")
        records.append(NEW_RECORD)
        added = 1
    for key, value in NEW_SOURCES.items():
        if key in sources and sources[key] != value:
            raise SystemExit(f"conflicting source: {key}")
        sources[key] = value
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_ao_sources={len(NEW_SOURCES)} added_records={added} updated_records=0 total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
