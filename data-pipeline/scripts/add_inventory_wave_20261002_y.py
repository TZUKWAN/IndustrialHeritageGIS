from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "shennongjia_logging_road_2025": {
        "source_type": "national_forestry_industrial_memory",
        "title": "神农架林区远程巡护的一天",
        "org": "国家林业和草原局（中国绿色时报）",
        "pub_date": "2025-05-23",
        "url": "https://www.forestry.gov.cn/c/www/zrgjgy/626400.jhtml",
        "authority": "A",
        "notes": "国家林草局转载中国绿色时报报道徐家庄林场、长坊护林站和当年伐木木材运输路，明确林二代和林场道路由木材外运转为巡护/防火通道的历史变化；用于确认神农架林业生产性交通遗存线索，不替代路线测绘、林场档案和保护边界。",
    },
    "huanggang_silk_factory_peoples_daily_1981": {
        "source_type": "newspaper_archive_industrial_history",
        "title": "湖北黄冈地区缫丝厂关于生丝价格和蚕茧收购问题的来信",
        "org": "人民日报历史版（1981-07-15）",
        "pub_date": "1981-07-15",
        "url": "https://cn.govopendata.com/renminribao/1981/07/15/4/",
        "authority": "C",
        "notes": "人民日报历史版转载页面记录‘湖北黄冈地区缫丝厂’和1300余名工人、1970年代生产经营问题；页面为历史报刊镜像，现阶段只用于建立区域企业史线索，具体厂名、县市、厂址、建筑和档案仍需黄冈地方志/档案馆/现场资料核验。",
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
    record_status: str = "source_confirmed",
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
        "record_status": record_status,
        "geocode_status": "pending",
        "source_keys": source_keys,
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


NEW_RECORDS: list[dict[str, Any]] = [
    rec(
        "HBI-SNJ-004",
        "神农架伐木时代木材运输路（长坊片区）",
        "神农架林区",
        "宋洛乡长坊村—徐家庄林场片区",
        "林业生产与木材运输",
        "research_candidate",
        "国家林草部门报道确认的历史木材运输路；遗迹边界和保护级别待核",
        ["shennongjia_logging_road_2025"],
        "国家林草局报道指出，神农架林场道路曾用于把山中木材运出，现转为林场巡护和防火通道，并记录徐家庄林场、长坊护林站和林场职工代际记忆；本条将历史木材运输路作为林业工业文化景观候选，具体路线、桥涵、装运点和保存状态待林场档案与现场测绘核验。",
        ev(
            "长坊片区当年伐木木材运输路、林场道路及可能保留的桥涵、转运节点；公开报道未给出完整线路和构筑物清单",
            "山地伐木、木材集运和林场道路工程形成的生产技术记忆；运输工具、路基工法和林场档案待补",
            "伐木工、林场修路工、护林员和林二代共同形成的林业生产与生态转型记忆；口述史和老照片待采集",
            "历史运输路部分转为巡护/防火通道，林业生产功能已改变；原路段的可见遗存、权属和保护要求待核",
        ),
        aliases=["神农架木材运输路", "长坊木材运输路", "神农架伐木道路遗存"],
        asset_kind="industrial_transport_site",
        related_inventory_ids=["HBI-SNJ-001", "HBI-SNJ-003"],
    ),
    rec(
        "HBI-SZ-010",
        "随州老火车站旧址（汉丹铁路早期节点）",
        "随州市",
        "随州市区交通大道片区",
        "铁路运输与城市工业化",
        "research_candidate",
        "随州日报工业史报道确认的铁路工业节点；旧站房、线路和保护边界待核",
        ["suizhou_industrial_history_2024"],
        "随州日报记载随州老火车站于1958年开工、1966年汉丹铁路全线通车，并指出交通大道火车站推动城市发展；本条作为铁路工业文化节点候选记录，现存站房、站场、线路遗迹和与工业企业的空间关系需档案及现场核验。",
        ev(
            "随州老火车站站房、站场、铁路线路和交通大道周边配套设施；公开报道未给出旧站房单体清单和现状",
            "汉丹铁路建设、客货运输和工业企业原料/产品流通形成的交通工程技术记忆；线路档案和设备待补",
            "随州居民、铁路职工和工业企业职工围绕老火车站形成的城市扩展与就业流动记忆；口述史待采集",
            "老火车站作为城市早期铁路节点的现状与拆改情况待核；现有交通设施是否保留历史构件尚不明确",
        ),
        aliases=["随州老站", "随州旧火车站", "随州火车站旧址"],
        asset_kind="industrial_transport_site",
    ),
    rec(
        "HBI-HG-008",
        "湖北黄冈地区缫丝厂历史谱系线索",
        "黄冈市",
        None,
        "缫丝与丝绸工业",
        "research_candidate",
        "历史报刊确认的区域企业史线索；具体厂名、县市、厂址和遗存待核",
        ["huanggang_silk_factory_peoples_daily_1981"],
        "人民日报1981年历史版记载‘湖北黄冈地区缫丝厂’为1300余名工人的生产单位，并讨论1970年代生丝价格和蚕茧收购问题。原报道使用的是历史‘黄冈地区’行政称谓，尚未核实对应现代县市、企业全称或旧厂址，故以source_lead记录为后续地方志、档案馆和现场调查入口。",
        ev(
            "目前仅确认存在‘湖北黄冈地区缫丝厂’这一报刊称谓，具体厂房、设备和厂址均待地方档案核验",
            "机器缫丝、生丝生产和蚕茧收购组织形成的区域技术记忆；工艺流程、设备和产品谱系待厂志补证",
            "1300余名工人的就业、蚕桑供应和地区工业组织记忆有报刊记录；职工社区和口述史待采集",
            "停产、迁建、改制或现存状态均无公开对象级证据；不得据此推断旧址或保护利用现状",
        ),
        record_status="source_lead",
        aliases=["黄冈地区缫丝厂", "湖北缫丝厂", "黄冈缫丝工业线索"],
        asset_kind="industrial_site",
    ),
]


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    existing_by_id = {row["inventory_id"]: row for row in records}
    names = {row["name"] for row in records}
    for new_row in NEW_RECORDS:
        old = existing_by_id.get(new_row["inventory_id"])
        if old is None:
            if new_row["name"] in names:
                raise SystemExit(f"conflicting duplicate name: {new_row['name']}")
            records.append(new_row)
            existing_by_id[new_row["inventory_id"]] = new_row
            names.add(new_row["name"])
        elif old != new_row:
            raise SystemExit(f"conflicting duplicate record: {new_row['inventory_id']}")
    for key, value in NEW_SOURCES.items():
        if key in sources and sources[key] != value:
            raise SystemExit(f"conflicting source: {key}")
        sources[key] = value
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_y_sources={len(NEW_SOURCES)} added_records={len(NEW_RECORDS)} "
        f"total_records={len(records)} total_sources={len(sources)}"
    )


if __name__ == "__main__":
    main()
