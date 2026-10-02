from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "luotian_dihe_silk_2003": {
        "source_type": "reprinted_provincial_media_enterprise_history",
        "title": "民营业主朱锐锋反哺蚕农百万元",
        "org": "湖北日报（新浪新闻转载）",
        "pub_date": "2003-03-11",
        "url": "https://news.sina.com.cn/s/2003-03-11/1125942024.html",
        "authority": "C",
        "notes": "湖北日报消息转载页面记载1999年租赁濒临破产的罗田县国营缫丝厂并成立润丰茧丝有限公司，补充罗田县国营缫丝厂和企业改制沿革；页面未给出完整厂址、建筑设备或现状边界，保持来源线索层级。",
    },
    "yingshan_silk_industry_2022": {
        "source_type": "provincial_media_industry_history",
        "title": "英山桑蚕产业‘破茧重生’做大谋强观察",
        "org": "荆楚网/湖北日报",
        "pub_date": "2022-05-24",
        "url": "https://www.cnhubei.com/content/2022-05/24/content_14774576.html",
        "authority": "B",
        "notes": "荆楚网转载湖北日报报道列举英山缫丝厂、英山丝绸厂、英山绢纺厂、英山丝织厂、英山特种绸厂、英山丝棉制品厂等企业谱系，说明企业改制和蚕桑产业链变迁；页面存在重定向，公开搜索结果可核，具体厂址和遗存待地方志与现场核验。",
    },
    "yingshan_silk_knit_2008": {
        "source_type": "industry_media_silk_history",
        "title": "湖北制丝针织厂蚕丝产业报道",
        "org": "北方蚕业信息网",
        "pub_date": None,
        "url": "https://www.bfcy.net.cn/index.php/content/1428",
        "authority": "C",
        "notes": "行业媒体报道英山县湖北制丝针织厂原有缫丝规模13200绪、干部职工1100多人，并描述其蚕桑产业链与工农关系；具体建厂时间、厂址、建筑设备和现状待地方志、厂志与现场核验。",
    },
}


def ev(material: str, technical: str, social: str, current: str) -> dict[str, str]:
    return {
        "material_carriers": material,
        "technical_memory": technical,
        "social_memory": social,
        "current_use_or_loss": current,
    }


NEW_RECORDS: list[dict[str, Any]] = [
    {
        "inventory_id": "HBI-HG-012",
        "name": "罗田县大河岸缫丝厂旧址（线索）",
        "city": "黄冈市",
        "district_county": "罗田县大河岸镇（具体厂址待核）",
        "industry_category_l1": "缫丝与丝绸工业",
        "recognition_level": "research_candidate",
        "recognition_status": "公开报道确认的国营缫丝厂及改制谱系线索；未见实体和法定工业遗产认定",
        "record_status": "source_lead",
        "geocode_status": "pending",
        "source_keys": ["luotian_dihe_silk_2003", "huanggang_silk_factory_peoples_daily_1981"],
        "cultural_evidence": ev(
            "罗田县国营缫丝厂及大河岸缫丝厂厂房、车间、设备和职工生活设施待地方志、档案与现场核验",
            "机器缫丝、生丝生产、蚕茧收购和茧丝加工技术记忆；工艺流程、设备型号和产品谱系待厂志补证",
            "罗田缫丝厂工人、蚕农、蚕桑供应链和县域工业化记忆；职工社区、口述史和老照片待采集",
            "1999年公开报道确认罗田县国营缫丝厂曾濒临破产并被租赁改制，现厂区、停产/搬迁和再利用状态待核",
        ),
        "notes": "罗田具体厂名和大河岸企业线索分别来自湖北日报转载报道、行业准产证名单搜索结果和黄冈地区历史报刊；暂不把‘大河岸’直接等同完整厂界，保持来源线索层级。",
        "aliases": ["罗田县缫丝厂", "罗田县国营缫丝厂", "大河岸缫丝厂"],
        "asset_kind": "industrial_site",
    },
    {
        "inventory_id": "HBI-HG-013",
        "name": "英山县湖北制丝针织厂旧址（线索）",
        "city": "黄冈市",
        "district_county": "英山县（具体厂址待核）",
        "industry_category_l1": "缫丝与纺织工业",
        "recognition_level": "research_candidate",
        "recognition_status": "行业媒体和省级媒体报道确认的历史企业谱系线索；未见实体和法定工业遗产认定",
        "record_status": "source_lead",
        "geocode_status": "pending",
        "source_keys": ["yingshan_silk_industry_2022", "yingshan_silk_knit_2008"],
        "cultural_evidence": ev(
            "湖北制丝针织厂原厂房、缫丝车间、针织设施和职工生活配套待地方志、厂志和现场核验",
            "缫丝、制丝、针织和蚕桑加工技术；行业媒体报道原有13200绪缫丝规模，设备与工艺清单待补",
            "英山缫丝女工、蚕农、企业改制和县域蚕桑产业链记忆；职工社区、口述史和老照片待采集",
            "公开报道显示英山缫丝、丝绸和绢纺企业经历改制与产业转型，原厂区保存、搬迁和现用途待核",
        ),
        "notes": "英山多家丝绸企业名称由省级媒体报道列出，行业媒体补充湖北制丝针织厂规模；未取得原厂址和厂界资料，保持来源线索层级。",
        "aliases": ["湖北制丝针织厂", "英山缫丝厂", "英山丝绸厂", "英山绢纺厂"],
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
    print(f"wave_ai_sources={len(NEW_SOURCES)} added_records={added} updated_records=0 total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
