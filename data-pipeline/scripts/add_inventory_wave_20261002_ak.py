from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "jingshan_mechanical_residential_2020": {
        "source_type": "provincial_housing_renewal_case",
        "title": "城镇老旧小区改造小故事（一）——荆门篇",
        "org": "湖北省住房和城乡建设厅",
        "pub_date": "2020-10-19",
        "url": "https://zjt.hubei.gov.cn/bmdt/dtyw/szsm/202010/t20201019_2961830.shtml",
        "authority": "A",
        "notes": "省住建厅官方案例明确京山市原机械厂生活区于2019年启动老旧小区改造，记录线路、道路、管网、居民生活和原厂职工社区语境；用于工业社区文化证据，不替代原机械厂厂区边界、设备和法定遗产认定。",
    },
    "hubei_industry_export_1989": {
        "source_type": "provincial_gazette_industry_list",
        "title": "湖北省工业企业与出口专厂历史名单（1989年省政府公报）",
        "org": "湖北省人民政府公报",
        "pub_date": "1989-04-01",
        "url": "https://www.hubei.gov.cn/gbhis/1989/1989-4.pdf",
        "authority": "A",
        "notes": "省政府公报PDF检出湖北齿轮厂、京山机械厂、荆州机床厂等工业企业/出口专厂名称，作为企业谱系和历史名录线索；PDF版面文字存在识别误差，具体厂址、厂区实体和现状待地方志、档案及现场核验。",
    },
}


def ev(material: str, technical: str, social: str, current: str) -> dict[str, str]:
    return {
        "material_carriers": material,
        "technical_memory": technical,
        "social_memory": social,
        "current_use_or_loss": current,
    }


NEW_RECORDS = [
    {
        "inventory_id": "HBI-JM-018",
        "name": "京山市原机械厂生活区工业文化景观",
        "city": "荆门市",
        "district_county": "京山市（具体生活区与原厂界待核）",
        "industry_category_l1": "机械制造工业与职工社区",
        "recognition_level": "city_planning",
        "recognition_status": "省住建厅官方案例确认的原机械厂职工生活区更新对象；未见法定工业遗产认定",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["jingshan_mechanical_residential_2020", "hubei_industry_export_1989"],
        "cultural_evidence": ev(
            "原机械厂职工生活区住宅、道路、管网和公共空间；省住建厅确认生活区改造，生产厂房与生活区边界待核",
            "京山机械制造、农机/轻工机械生产和职工技术组织记忆；厂史、产品与设备资料待补",
            "原机械厂职工、家属和京山市工业社区生活记忆；居民口述、老照片和公共服务设施待采集",
            "2019年启动老旧小区改造，实施线路、道路、管网、绿化和停车等更新；原厂区关联、产权和现状开放边界待核",
        ),
        "notes": "本条把生产企业的职工生活区作为工业文化景观单列，来源确认对象是生活区更新和企业记忆，不推断原机械厂生产厂房仍存或已获法定遗产认定。",
        "aliases": ["京山市原机械厂生活区", "京山机械厂职工生活区", "京山机械厂社区"],
        "asset_kind": "industrial_residential_landscape",
    },
    {
        "inventory_id": "HBI-JZ-018",
        "name": "荆州机床厂旧址（省志线索）",
        "city": "荆州市",
        "district_county": "荆州市（具体厂址待核）",
        "industry_category_l1": "机床制造工业",
        "recognition_level": "archive_lead",
        "recognition_status": "省政府公报历史工业企业名单线索；未见实体和法定工业遗产认定",
        "record_status": "source_lead",
        "geocode_status": "pending",
        "source_keys": ["hubei_industry_export_1989"],
        "cultural_evidence": ev(
            "荆州机床厂厂房、机床设备、办公和职工生活设施待地方志、档案与现场核验",
            "车床、钻床、磨床等机床制造、加工和维修技术记忆；产品谱系与设备型号待厂志补证",
            "荆州机床厂与沙市/荆州机械工业、技术工人和地方工业化记忆相连；职工社区与口述史待采集",
            "1989年省政府公报可确认企业名称出现在历史工业名单，停产、搬迁、改制和现用途待核",
        ),
        "notes": "省政府公报PDF检出‘荆州机床厂’名称，但版面识别和历史行政称谓需进一步校勘；保持档案线索层级，不推断厂址和现存设备。",
        "aliases": ["荆州机床厂", "沙市机床厂（待核）"],
        "asset_kind": "industrial_site",
    },
]


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    by_id = {row["inventory_id"]: row for row in records}
    names = {row["name"] for row in records}
    added = 0
    for row in NEW_RECORDS:
        if row["inventory_id"] in by_id:
            if by_id[row["inventory_id"]] != row:
                raise SystemExit(f"conflicting duplicate record: {row['inventory_id']}")
            continue
        if row["name"] in names:
            raise SystemExit(f"conflicting duplicate name: {row['name']}")
        records.append(row)
        by_id[row["inventory_id"]] = row
        names.add(row["name"])
        added += 1
    for key, value in NEW_SOURCES.items():
        if key in sources and sources[key] != value:
            raise SystemExit(f"conflicting source: {key}")
        sources[key] = value
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_ak_sources={len(NEW_SOURCES)} added_records={added} updated_records=0 total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
