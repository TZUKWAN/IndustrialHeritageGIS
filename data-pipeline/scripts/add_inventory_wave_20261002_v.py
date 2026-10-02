from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "qianjiang_oilfusion_2026": {
        "source_type": "municipal_government_industrial_culture_report",
        "title": "奋力谱写油地融合高质量发展新篇章",
        "org": "潜江市人民政府/潜江新闻网",
        "pub_date": "2026-04-09",
        "url": "https://www.hbqj.gov.cn/xwzx/jrqj/qjyw/202604/t20260409_5910983.html",
        "authority": "A",
        "notes": "潜江市政府报道广华寺街道深度挖掘石油工业遗存，整合江汉第一口油井、五七油田会战指挥部旧址等文旅点位打造石油研学线路，并将油田工业文化与社区、商业和公共文化空间结合；用于补充利用关系和社区景观，不替代单体名录认定。",
    },
    "xiantao_fourth_survey_field_2024": {
        "source_type": "provincial_media_fourth_cultural_relic_survey",
        "title": "用脚丈量，用心记录——仙桃市‘四普’工作有序推进",
        "org": "长江网/仙桃市融媒体中心",
        "pub_date": "2024-06-01",
        "url": "https://news.cjn.cn/hbpd_19912/xt_19940/202406/t4926650.htm",
        "authority": "B",
        "notes": "报道仙桃市第四次全国文物普查实地调查推进情况，作为仙桃市域工业对象继续检索和覆盖审计依据；页面未提供具体工业遗产单体名录，不直接支撑对象认定。",
    },
    "qianjiang_fourth_survey_2025": {
        "source_type": "municipal_government_fourth_cultural_relic_survey",
        "title": "我市圆满完成第四次全国文物普查田野调查数据上传工作",
        "org": "潜江市文化和旅游局",
        "pub_date": "2025-04-01",
        "url": "https://www.hbqj.gov.cn/swhhlyj/xwzx/gzdt/202504/t20250401_5597181.html",
        "authority": "A",
        "notes": "潜江市文旅局确认四普复查338处、核查线索54条、新发现登记文物点54处，覆盖全市区镇街道并包含近现代重要史迹及代表性建筑；作为潜江工业对象继续检索和覆盖审计依据，不把总量写成工业遗产名录。",
    },
}


def ev(material: str, technical: str, social: str, current: str) -> dict[str, str]:
    return {
        "material_carriers": material,
        "technical_memory": technical,
        "social_memory": social,
        "current_use_or_loss": current,
    }


def rec(
    inventory_id: str,
    name: str,
    city: str,
    district: str | None,
    industry: str,
    level: str,
    status: str,
    source_keys: list[str],
    notes: str,
    cultural_evidence: dict[str, str],
    *,
    aliases: list[str] | None = None,
    asset_kind: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "inventory_id": inventory_id,
        "name": name,
        "city": city,
        "district_county": district,
        "industry_category_l1": industry,
        "recognition_level": level,
        "recognition_status": status,
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": source_keys,
        "cultural_evidence": cultural_evidence,
        "notes": notes,
    }
    if aliases:
        row["aliases"] = aliases
    if asset_kind:
        row["asset_kind"] = asset_kind
    return row


NEW_RECORDS: list[dict[str, Any]] = [
    rec(
        "HBI-QJ-007",
        "江汉油田职业技术学校旧址（青少年综合实践学校）",
        "潜江市",
        "广华寺街道",
        "石油工业教育与技工培训",
        "city_planning",
        "官方工业研学利用对象；原油田职业技术学校实体边界和独立认定待核",
        ["qianjiang_cultural_2026", "qianjiang_oilfusion_2026"],
        "潜江市政府文旅推介资料确认江汉油田青少年综合实践学校选址于原江汉油田职业技术学校，由街道与市属投资公司共建，现有教学楼、宿舍等配套，可承接700人食宿研学；潜江市政府关于油地融合的报道又明确依托油田工业遗存发展石油研学线路。本条保存原油田职业教育和当前研学利用关系，但未把现有学校建筑直接等同于法定工业遗产，原校址边界、建成年代和设施沿革待核。",
        ev(
            "原江汉油田职业技术学校校址、教学楼、宿舍及现青少年综合实践学校配套空间；公开资料未给出原校舍编号和完整边界",
            "油田职工技术培训、石油勘探钻采知识传播、技工教育和研学课程组织的工业教育技术记忆；专业、师资与教材档案待补",
            "油田职工子弟教育、技术工人培养、石油大军家庭社区和当代青少年研学形成的连续社会记忆；校友口述史待采集",
            "原校址已转入青少年综合实践学校和石油工业研学利用；校舍原真性、产权、开放管理和保护边界待核",
        ),
        aliases=["江汉油田职工学校旧址", "江汉油田职业技术学校", "潜江油田职校旧址"],
        asset_kind="industrial_social_site",
    ),
    rec(
        "HBI-QJ-008",
        "江汉油田盐化工业园区工业文化景观",
        "潜江市",
        "广华寺街道及相关油田片区",
        "石油、盐化工与能源化工",
        "city_planning",
        "官方工业旅游规划场景；未见独立工业遗产名录认定",
        ["qianjiang_industrial_tourism", "qianjiang_industrial_plan", "qianjiang_oilfusion_2026"],
        "潜江市文化和旅游局公开答复将盐化工业园区与五七油田会战指挥部旧址、江汉第一口油井、岩心库和社区共同列为石油工业文化景区和工业旅游线路场景；国土空间规划又提出江汉油田工业文化片区，依托采油作业区、工业景观与农业景观开展展示体验。公开资料未给出园区内具体遗产单体清单，故按规划尺度工业文化景观记录。",
        ev(
            "盐化工业园区、油田采油作业区、工业景观和农业景观组合空间；具体厂房、井场、管线和边界待专项普查",
            "石油开采、盐卤资源利用、盐化工和能源化工产业链的技术记忆目前由规划和文旅资料概括，工艺设备与企业谱系待补",
            "油田职工、盐化工劳动者、油地融合和江汉油城产业转型形成的社会记忆；社区与企业口述史待采集",
            "已被官方规划和文旅答复纳入工业文化展示、研学与旅游线路；单体保护、权属、环境风险和开放管理待核",
        ),
        aliases=["江汉油田工业文化片区盐化工场景", "潜江盐化工业园工业文化景观"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-QJ-009",
        "江汉油田广华职工社区与油地融合公共空间",
        "潜江市",
        "广华寺街道",
        "石油工业社区与公共服务",
        "city_planning",
        "官方工业文化线路和油地融合对象；具体社区单体边界待核",
        ["qianjiang_industrial_tourism", "qianjiang_route_2025", "qianjiang_cultural_2026", "qianjiang_oilfusion_2026"],
        "潜江市文旅局答复将油田社区与五七油田会战指挥部旧址、江汉第一口油井、岩心库、盐化工业园区等场景共同纳入工业文化景区构想；广华寺街道官方报道继续提出整合油田遗存、社区和商业空间打造研学线路与油地融合发展。本条表达职工社区、公共服务和油田工业文化传播关系，不把未列明的楼栋直接写成法定遗产单体。",
        ev(
            "广华油田职工社区、公共服务设施、社区商业与油田工业景观的组合空间；具体楼栋、学校、医院和公共建筑清单待测绘",
            "油田生产组织、职工生活服务、社区设施维护和油地协同运营形成的工业社会技术记忆；企业社区档案待补",
            "12万石油大军、油田职工家庭、职工子弟教育和广华居民共同形成的油城社会记忆；社区口述史和老照片待采集",
            "官方提出将社区与油田遗存串联为工业旅游、科普研学和油地融合公共文化场景；保护边界、产权和开放制度待核",
        ),
        aliases=["广华油田职工生活区", "江汉油田广华社区", "广华油田工业社区"],
        asset_kind="industrial_social_site",
    ),
    rec(
        "HBI-QJ-010",
        "潜江市石油化工厂历史谱系（今金澳科技前身）",
        "潜江市",
        None,
        "石油化工与炼油",
        "research_candidate",
        "官方企业史确认的地方石化工业谱系；具体旧厂址和实体遗存待核",
        ["qianjiang_oilcity_2026", "qianjiang_oilfusion_2026"],
        "潜江市政府‘油城不靠油’报道确认1965年钟11井工业油流、1972年江汉石油管理局成立，并记载1976年金澳科技前身——潜江市石油化工厂建立，逐步成长为华中重要民营炼油企业。来源能够确认企业史与石化产业谱系，但未提供原厂具体地址、建筑设备或保护利用信息，故按历史企业研究候选记录，不把企业谱系直接当作旧址认定。",
        ev(
            "潜江市石油化工厂历史企业及其可能的原厂区、炼油装置和配套设施；公开报道未给出旧厂址坐标和物项清单",
            "1976年石油化工厂建立、炼油及石化原料生产形成的地方能源化工技术记忆；设备、产品和工艺沿革待企业档案补证",
            "江汉油田、石化工人、油地产业链和潜江‘油城’身份形成的社会记忆；企业职工口述史待采集",
            "企业谱系延续至金澳科技等现有产业，原石油化工厂实体保存、迁改和开放状态未知；保持研究候选层级",
        ),
        aliases=["潜江市石油化工厂旧址线索", "金澳科技前身", "潜江石化厂历史"],
        asset_kind="industrial_culture_site",
    ),
]


def merge_unique(row: dict[str, Any], key: str, values: list[str]) -> None:
    existing = row.setdefault(key, [])
    for value in values:
        if value not in existing:
            existing.append(value)


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    existing_by_id = {row["inventory_id"]: row for row in records}
    for new_row in NEW_RECORDS:
        old = existing_by_id.get(new_row["inventory_id"])
        if old is None:
            records.append(new_row)
            existing_by_id[new_row["inventory_id"]] = new_row
        elif old != new_row:
            raise SystemExit(f"conflicting duplicate record: {new_row['inventory_id']}")
    for key, value in NEW_SOURCES.items():
        if key in sources and sources[key] != value:
            raise SystemExit(f"conflicting source: {key}")
        sources[key] = value
    targets = data.setdefault("research_targets", {})
    coverage = targets.setdefault("coverage_sources", [])
    merge_unique({"coverage_sources": coverage}, "coverage_sources", [
        "xiantao_fourth_survey_field_2024",
        "qianjiang_fourth_survey_2025",
    ])
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_v_sources={len(NEW_SOURCES)} added_records={len(NEW_RECORDS)} "
        f"total_records={len(records)} total_sources={len(sources)} patched_records=0"
    )


if __name__ == "__main__":
    main()
