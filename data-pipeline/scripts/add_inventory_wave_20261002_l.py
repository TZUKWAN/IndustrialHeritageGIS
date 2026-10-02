from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "dpm_panwan_kiln_2022": {
        "source_type": "museum_research_pdf",
        "title": "湖北丹江口庞湾琉璃窑址",
        "org": "故宫博物院/湖北省文物考古研究院",
        "pub_date": "2022-01-19",
        "url": "https://www.dpm.org.cn/Uploads/File/2022/01/19/u61e7b88513790.pdf",
        "authority": "A",
        "notes": "故宫博物院公开科技分析资料记载庞湾窑址联合发掘、明代后期至清代早期层位、烧造区与成型加工区、琉璃建筑构件和‘和记’铭文瓦件，并据此讨论武当山建筑材料供给与原料/工艺来源。",
    },
    "pku_panwan_kiln_2021": {
        "source_type": "academic_repository",
        "title": "湖北丹江口庞湾窑址出土窑业遗物的科技分析",
        "org": "北京大学机构知识库/故宫博物院/湖北省文物考古研究院",
        "pub_date": "2021-12-31",
        "url": "https://ir.pku.edu.cn/handle/20.500.11897/633455",
        "authority": "A",
        "notes": "北京大学机构知识库收录庞湾窑址科技分析，摘要确认其为明代专供武当山琉璃烧制的皇家官窑，并涉及胎釉组成、制作工艺和原料来源。",
    },
    "shennongjia_salt_road_2025": {
        "source_type": "official_media",
        "title": "回首“盐道往事” 大九湖36位农民演火新生活",
        "org": "湖北省文化和旅游厅/湖北日报",
        "pub_date": "2025-08-27",
        "url": "https://wlt.hubei.gov.cn/bmdt/szyw/snj/202508/t20250827_5756356.shtml",
        "authority": "A",
        "notes": "省文旅厅转载湖北日报资料梳理川鄂古盐道两条线路：从保康、房县进入神农架，经阳日、松柏、宋洛、徐家庄、黑水河、板仓、大九湖通往四川大宁盐厂；同时记录地方村民以实景剧传承盐道记忆。",
    },
    "hubei_tanzidong_tea_2021": {
        "source_type": "government_agriculture_media",
        "title": "湖北日报报道：鹤峰古茶树备受呵护",
        "org": "湖北省农业农村厅/湖北日报",
        "pub_date": "2021-06-11",
        "url": "https://nyt.hubei.gov.cn/bmdt/yw/mtksn/202106/t20210611_3590125.shtml",
        "authority": "A",
        "notes": "省农业农村厅转载湖北日报报道记载鹤峰坛子洞古茶树群、茶园保护发展中心档案、保护碑与界桩、编号和管护，以及2020年列为县级文物保护单位；规模、权属和生态边界仍需以专项调查为准。",
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
    industry: str,
    level: str,
    status: str,
    source_keys: list[str],
    notes: str,
    cultural_evidence: dict[str, str],
    *,
    district: str | None = None,
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
        "HBI-SY-016",
        "庞湾窑址",
        "十堰市",
        "明代琉璃建材制造",
        "provincial_heritage_related",
        "第六批湖北省文物保护单位；明代古遗址",
        [
            "hubei_provincial_relics_1098",
            "dpm_panwan_kiln_2022",
            "pku_panwan_kiln_2021",
        ],
        "省级名录、故宫博物院和北京大学资料共同确认丹江口市习家店镇庞湾窑址为明代琉璃烧造遗址；考古科技分析把其与武当山五龙宫、玉虚宫等建筑构件和皇家官窑供料联系起来。本条记录窑业生产系统，不把武当山建筑群与窑址合并为同一空间对象。",
        ev(
            "窑炉、烧造区、成型加工区、淘泥/炼泥设施、匣钵、支钉、垫砖、瓦当、滴水、板瓦、筒瓦和勾头等琉璃构件；考古揭露范围与保护边界待测绘",
            "明代琉璃建筑构件成型、施釉、烧造、胎釉配方和原料来源；故宫博物院与北大资料支持窑业遗物科技分析及武当山供料关系",
            "窑工、作坊组织、丹江口山地资源与武当山建筑工程之间的生产协作和地方记忆；工匠名录、运输路线和口述史待补",
            "省级文保身份与考古科技研究已确认；窑址开放、展示、产权、修缮和文物库房管理需按最新资料复核",
        ),
        district="丹江口市",
        aliases=["庞湾琉璃窑址", "庞湾明代官窑", "丹江口庞湾窑址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-SNJ-002",
        "川鄂古盐道（神农架段）",
        "神农架林区",
        "盐运交通与山地贸易路线",
        "provincial_heritage_related",
        "湖北省省级文物保护单位名录列名（明、清）；神农架段",
        ["hubei_provincial_relics_1098", "shennongjia_salt_road_2025"],
        "湖北省名录列出川鄂古盐道（神农架段），省文旅厅资料进一步梳理保康、房县经神农架进入四川大宁盐厂的两条盐道线路，并记录大九湖地方社区以实景剧传承盐道故事。本条按山地盐运基础设施与贸易景观记录，路线分段和遗存本体待普查。",
        ev(
            "山路、栈道、渡口、客店、集市和可能的盐运节点；省级名录只确认神农架段名称，具体路基、桥涵、遗迹和保护边界待测绘",
            "盐包驮运、山地挑运、河谷转运和长距离贸易组织技术；官方资料确认两条路线和终点，运输工具、驿站与货物流量档案待补",
            "盐夫、茶女、商人、官兵、客栈和大九湖村落共同形成的劳动与商贸记忆；实景剧和地方叙事可作为社会记忆线索，口述史待规范采集",
            "省级文保名录身份和地方展示利用已确认；路线连续性、权属、开放、保护工程与旅游承载风险需分段核验",
        ),
        district="神农架林区",
        aliases=["川鄂盐道神农架段", "神农架古盐道", "盐道遗址（神农架段）"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-ES-012",
        "坛子洞古茶园",
        "恩施州",
        "古茶树资源与茶业生产景观",
        "provincial_heritage_related",
        "第八批湖北省文物保护单位（2021）；2020年鹤峰县级文物保护单位；清代",
        [
            "hubei_8th_relics_2021",
            "hubei_chenghuang_boundary_2024",
            "hubei_tanzidong_tea_2021",
        ],
        "省级名录和省政府公报确认鹤峰县坛子洞古茶园为第八批省级文物保护单位、时代为清；省农业农村厅转载报道记录古茶树群、保护发展中心档案、保护碑界桩和2020年县级文保身份。本条聚焦古茶园作为茶业原料生产与万里茶道茶源景观的文化价值。",
        ev(
            "坛子洞古茶园、古茶树群、保护碑、界桩、编号系统和茶园山场；省政府公报已明确保护范围方向，完整地块边界和构筑物待测绘",
            "古茶树选育、采摘、原料供给、茶园管护和向宜红茶/万里茶道茶业网络供料的生产线索；加工设备与历史产量待档案补证",
            "鹤峰茶农、土家族村落、茶商和古茶树保护者共同形成的茶源地记忆；茶树档案和社区口述史可继续补充",
            "省级、县级文保身份以及档案化保护、保险和管护措施已有官方报道；茶园经营、开放、产权和生态风险需按最新管理资料复核",
        ),
        district="鹤峰县",
        aliases=["坛子洞古茶树群", "鹤峰坛子洞古茶园", "坛子洞茶园"],
        asset_kind="industrial_cultural_landscape",
    ),
]


PATCHES: dict[str, dict[str, Any]] = {
    "HBI-WUHAN-052": {
        "aliases": ["斧头湖窑址", "湖泗窑址", "斧头湖古窑址"],
    },
    "HBI-EZ-013": {
        "aliases": ["主仓屋窑址", "华容王仓屋窑址"],
    },
    "HBI-YC-006": {
        "aliases": ["川汉铁路上风垭山峒遗址", "川汉铁路夷陵段", "黄家场火车站遗址"],
        "notes": "省级名录和宜昌市政府资料确认川汉铁路夷陵段遗址由上风垭山峒遗址、川汉铁路夷陵段及黄家场火车站等关系项构成；本条合并别名以便名录检索，但不把桥墩、车站和线路未经测绘地合并成同一精确点位。",
    },
}


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
    existing_names = {row["name"] for row in records}
    duplicate_ids = {row["inventory_id"] for row in NEW_RECORDS} & set(existing_by_id)
    duplicate_names = {row["name"] for row in NEW_RECORDS} & existing_names
    if duplicate_ids or duplicate_names:
        all_new_present = all(
            row["inventory_id"] in existing_by_id
            and existing_by_id[row["inventory_id"]]["name"] == row["name"]
            for row in NEW_RECORDS
        )
        if not all_new_present:
            raise SystemExit(
                "partial or conflicting prior application: "
                f"ids={sorted(duplicate_ids)} names={sorted(duplicate_names)}"
            )
    else:
        sources.update({key: value for key, value in NEW_SOURCES.items() if key not in sources})
        records.extend(NEW_RECORDS)

    for inventory_id, patch in PATCHES.items():
        row = existing_by_id.get(inventory_id)
        if row is None:
            raise SystemExit(f"patch target missing: {inventory_id}")
        for key in ("source_keys", "aliases"):
            values = patch.get(key)
            if values:
                merge_unique(row, key, values)
        for key, value in patch.items():
            if key not in {"source_keys", "aliases"}:
                row[key] = value

    data["research_targets"]["coverage_rule"] = (
        "每条对象至少绑定名录/普查/规划/企业史/档案遗产或来源确认资料；"
        "工业遗产实体、工业文化景观、工业旅游相关场景、档案文献和待核验线索分层记录。"
        "文化证据字段只记录来源中明确出现的载体、技术、社会记忆和利用状态，未核实内容保持待核。"
    )
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_l_records={len(NEW_RECORDS)} wave_l_sources={len(NEW_SOURCES)} "
        f"patched_records={len(PATCHES)} total_records={len(records)} total_sources={len(sources)}"
    )


if __name__ == "__main__":
    main()
