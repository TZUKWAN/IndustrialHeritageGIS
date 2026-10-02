from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"
SOURCE_KEY = "hubei_provincial_relics_1098"


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
    notes: str,
    cultural_evidence: dict[str, str],
    *,
    district: str | None = None,
    aliases: list[str] | None = None,
    asset_kind: str | None = None,
    related_inventory_ids: list[str] | None = None,
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
        "source_keys": [SOURCE_KEY],
        "cultural_evidence": cultural_evidence,
        "notes": notes,
    }
    if aliases:
        row["aliases"] = aliases
    if asset_kind:
        row["asset_kind"] = asset_kind
    if related_inventory_ids:
        row["related_inventory_ids"] = related_inventory_ids
    return row


def relic_evidence(kind: str, detail: str) -> dict[str, str]:
    return ev(
        f"湖北省省级文物保护单位名录确认的{kind}；{detail}现存建筑、构筑物、设备和保护边界待现场核验",
        f"{kind}对应的生产、运输或工程技术构成工业文化线索；工艺流程、设备谱系和工程档案待补",
        f"{kind}所连接的工人、作坊、运输或社区记忆；人物、组织与口述史待补证",
        "省级文物保护单位名录已确认名称和行政区；当前保存、利用、产权、开放与风险信息待继续核验",
    )


NEW_RECORDS: list[dict[str, Any]] = [
    rec(
        "HBI-XIANGYANG-024",
        "南漳县夹马寨造纸作坊",
        "襄阳市",
        "传统造纸与手工业",
        "provincial_heritage_related",
        "湖北省省级文物保护单位（名录列名）",
        "湖北省文旅厅省级文保名录列出清代夹马寨造纸作坊；本条把传统纸业生产空间纳入工业文化层，名录未提供作坊单体、纸池、工具和技艺传承信息，均保持待补。",
        relic_evidence("清代夹马寨造纸作坊", "作坊建筑、纸池、晾晒空间和工具清单"),
        district="南漳县",
        aliases=["夹马寨造纸作坊旧址", "夹马寨古造纸作坊"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-ES-008",
        "咸丰县黄金洞炼硝场遗址",
        "恩施州",
        "矿物加工与化学工业",
        "provincial_heritage_related",
        "湖北省省级文物保护单位（名录列名）",
        "湖北省文旅厅省级文保名录列出明代黄金洞炼硝场遗址；本条记录硝业生产遗存和矿物加工技术线索，不把古遗址直接写成工信部门工业遗产认定。",
        relic_evidence("明代黄金洞炼硝场遗址", "炼硝窑炉、作业空间、原料来源与遗址边界"),
        district="咸丰县",
        aliases=["黄金洞炼硝场旧址", "黄金洞硝场遗址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-WUHAN-045",
        "武昌武泰闸旧址",
        "武汉市",
        "水利工程工业",
        "provincial_heritage_related",
        "湖北省省级文物保护单位（名录列名）",
        "湖北省文旅厅省级文保名录将1906年武泰闸列为武汉市武昌区近现代重要史迹；本条记录城市水利工程及其运行文化，闸体、附属设施、工程档案和现状需继续核验。",
        relic_evidence("1906年武泰闸水利工程", "闸体、闸门、堤岸和调度设施"),
        district="武昌区",
        aliases=["武泰闸", "武泰闸水利工程"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-XIANGYANG-025",
        "襄樊码头遗址",
        "襄阳市",
        "港口与水运工业",
        "national_cultural_relic_related",
        "全国重点文物保护单位（2019年第八批；省级名录登记）",
        "湖北省文旅厅省级文保名录登记清代襄樊码头，并注明2019年公布为第八批全国重点文物保护单位、公布名称为襄樊码头遗址；本条纳入交通工业文化层，不等同工信部门国家工业遗产名录。",
        ev(
            "清代襄樊码头遗址及滨水装卸、泊岸和历史街区空间；具体遗存清单待现场核验",
            "汉江港口装卸、航运组织和商贸物流技术；设备与工程档案待补",
            "襄阳码头工人、商贸往来、汉江航运和城市港口社会记忆",
            "国家文物保护单位名录身份已由省级名录注明；现状开放、产权和保护范围待核",
        ),
        district="襄城区",
        aliases=["襄樊码头", "襄樊码头旧址"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-XG-010",
        "孝南区城隍潭码头遗址",
        "孝感市",
        "港口与水运工业",
        "provincial_heritage_related",
        "湖北省省级文物保护单位（2021年第八批）",
        "湖北省文旅厅名录列出孝感市孝南区城隍潭码头遗址，年代为明清；本条把内河码头、货运与水乡工业文化纳入底册，现存码头构筑物和城市水运谱系待核。",
        relic_evidence("明清城隍潭码头遗址", "码头岸线、仓储/装卸空间和水运遗迹"),
        district="孝南区",
        aliases=["城隍潭码头旧址", "孝感城隍潭码头"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-YC-012",
        "兴山县川汉铁路桥墩遗址",
        "宜昌市",
        "铁路工程工业",
        "provincial_heritage_related",
        "湖北省省级文物保护单位（名录列名）",
        "湖北省文旅厅省级文保名录列出1909—1911年兴山川汉铁路桥墩；本条作为川汉铁路夷陵段之外的独立组成项，避免把兴山县桥墩与夷陵区线路混为同一行政片区。",
        relic_evidence("1909—1911年川汉铁路桥墩", "桥墩、路基、施工遗迹和沿线工程边界"),
        district="兴山县",
        aliases=["川汉铁路兴山段桥墩", "兴山川汉铁路桥墩"],
        asset_kind="heritage_component",
    ),
    rec(
        "HBI-WUHAN-046",
        "武昌第一纱厂旧址（省保名录整体项）",
        "武汉市",
        "纺织工业",
        "provincial_heritage_related",
        "湖北省省级文物保护单位（名录列名）",
        "湖北省文旅厅省级文保名录登记武昌第一纱厂旧址；现有底册另有武汉市首批工业遗产第一纱厂办公楼旧址，本条作为省保名录整体项单独保留并关联办公楼，不把单体办公楼替代完整厂址。",
        ev(
            "武昌第一纱厂整体厂址及纺织工业建筑、设备空间；现存单体与保护范围待测绘",
            "近代纺纱、织造、厂区动力和城市纺织生产组织；设备谱系与工艺档案待补",
            "武昌纺织工人、家属区和近代武汉纺织工业城市记忆",
            "省保名录确认整体项；办公楼已有市级工业遗产记录，厂区其余部分的现状和利用待核",
        ),
        district="武昌区",
        aliases=["武昌第一纱厂", "第一纱厂旧址整体项"],
        asset_kind="industrial_site",
        related_inventory_ids=["HBI-WUHAN-011"],
    ),
]


UPDATES: dict[str, dict[str, Any]] = {
    "HBI-YC-006": {"source_keys_add": [SOURCE_KEY]},
    "HBI-HS-020": {"source_keys_add": [SOURCE_KEY]},
}


def merge_update(row: dict[str, Any], patch: dict[str, Any]) -> None:
    for key in patch.get("source_keys_add", []):
        if key not in row.setdefault("source_keys", []):
            row["source_keys"].append(key)
    row["source_keys"] = sorted(set(row.get("source_keys") or []))


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
            and existing_by_id[row["inventory_id"]] == row
            for row in NEW_RECORDS
        )
        if not all_new_present:
            raise SystemExit(
                "partial or conflicting prior application: "
                f"ids={sorted(duplicate_ids)} names={sorted(duplicate_names)}"
            )
    else:
        missing = sorted({SOURCE_KEY} - set(sources))
        if missing:
            raise SystemExit(f"missing source keys: {missing}")
        records.extend(NEW_RECORDS)
        existing_by_id = {row["inventory_id"]: row for row in records}

    for inventory_id, patch in UPDATES.items():
        row = existing_by_id.get(inventory_id)
        if row is None:
            raise SystemExit(f"update target missing: {inventory_id}")
        merge_update(row, patch)

    data["research_targets"]["coverage_rule"] = (
        "每条对象至少绑定名录/普查/规划/企业史/档案遗产或来源确认资料；"
        "工业遗产实体、工业文化景观、工业旅游相关场景、档案文献和待核验线索分层记录。"
        "文化证据字段只记录来源中明确出现的载体、技术、社会记忆和利用状态，未核实内容保持待核。"
    )
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_f_records={len(NEW_RECORDS)} wave_f_sources=0 "
        f"total_records={len(records)} total_sources={len(sources)} updates={len(UPDATES)}"
    )


if __name__ == "__main__":
    main()
