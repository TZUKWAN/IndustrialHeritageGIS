from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "shiyan_44_local_2022": {
        "source_type": "municipal_media_factory_history",
        "title": "44厂的过往与序章",
        "org": "十堰广播电视台/十堰周刊",
        "pub_date": "2022-07-07",
        "url": "https://www.syiptv.com/article/show/186133",
        "authority": "B",
        "notes": "十堰市融媒体报道以厂志和老职工口述记录原44厂（二汽车厢厂）1969年建设、厂内水井、芦席棚、液压机、底漆电泳槽、红外线烘干室和冲压机等具体物项，并说明2021年整体搬迁、部分厂区面临城市工程和核心区域拟保护开发。",
    },
    "shiyan_46_reply_2020": {
        "source_type": "provincial_government_reply_shiyan",
        "title": "关于湖北省政协十二届一次会议第20180329号提案的答复（46厂项目段）",
        "org": "湖北省文化和旅游厅/十堰市人民政府会办意见",
        "pub_date": "2020-08-05",
        "url": "https://wlt.hubei.gov.cn/zfxxgk/fdzdgknr/qtzdgknr/jytabl/zxwyta/202008/t20200805_2742255.shtml",
        "authority": "A",
        "notes": "省级官方答复明确十堰已为东风悬架弹簧有限公司大岭路老厂区（46厂）汽车工业遗产博物馆建设开展基础工作；来源只确认项目与厂区关系，正式名录、边界和实施结果仍待市级档案核验。",
    },
    "shiyan_auto_protection_measures_2018": {
        "source_type": "government_regulation_mirror",
        "title": "十堰市汽车工业文化遗产保护办法",
        "org": "十堰市人民政府（商务部法规镜像）",
        "pub_date": "2018-01-31",
        "url": "https://policy.mofcom.gov.cn/claw/clawContent.shtml?id=67677",
        "authority": "B",
        "notes": "法规镜像公布十堰市汽车工业文化遗产的物质、可移动和非物质范围、普查认定、档案数据库与保护性利用规则；正式使用时仍应与十堰市政府公报或法制部门原文核对。",
    },
    "shiyan_car_school_2017": {
        "source_type": "university_museum_outreach",
        "title": "‘汽车工业遗产知识’宣传活动走进校园",
        "org": "湖北工业职业技术学院/十堰市博物馆",
        "pub_date": "2017-06-26",
        "url": "https://news.hbgyzy.edu.cn/info/1003/8720.htm",
        "authority": "B",
        "notes": "高校新闻网搜索结果明确活动展板展示汽车弹簧、模具冲压、汽车车轮、汽车泵业等老厂区照片和资料；当前原页面抓取超时，故相关单体只登记为来源线索，待校方或市博物馆档案复核。",
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
    return row


NEW_RECORDS: list[dict[str, Any]] = [
    rec(
        "HBI-SY-025",
        "东风悬架弹簧有限公司大岭路老厂区（46厂）汽车工业遗产博物馆项目",
        "十堰市",
        "十堰城区（大岭路，行政区待核）",
        "汽车零部件工业",
        "municipal_survey",
        "省级官方答复确认的汽车工业文化遗产保护利用项目；正式名录和实施结果待核",
        ["shiyan_46_reply_2020", "shiyan_auto_protection_measures_2018"],
        "湖北省文化和旅游厅答复明确十堰已为东风悬架弹簧有限公司大岭路老厂区（即46厂）汽车工业遗产博物馆建设开展基础工作；本条把厂区、项目和保护利用意图单列，不能据此推断博物馆已建成或厂区已获法定认定。",
        ev(
            "大岭路46厂老厂区及拟建博物馆承载的汽车工业建筑、设备和档案（具体车间、机器、厂界待核）",
            "汽车悬架弹簧及零部件制造的工艺、设备和专业厂协作记忆；公开答复未列具体工艺流程和核心设备",
            "二汽建设者、悬架弹簧厂职工和十堰车城形成的汽车工业社区记忆；博物馆展陈、口述史和厂志待补",
            "官方答复只确认博物馆建设基础工作，现状、产权、开放条件、保护范围和项目是否实施完成待市级规划、企业档案与现场核验",
        ),
        aliases=["46厂老厂区", "东风钢板弹簧厂大岭路旧址"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-SY-026",
        "东风模具冲压技术有限公司模具分公司（汽车工业文化资料对象）",
        "十堰市",
        "张湾区（具体老厂区待核）",
        "汽车模具与冲压工业",
        "research_candidate",
        "十堰汽车工业遗产宣传活动明确的老厂区资料对象；厂址、历史边界和遗存状态待核",
        ["shiyan_car_school_2017"],
        "十堰市博物馆进校园活动的展板材料把模具冲压技术有限公司模具分公司作为具有历史意义的老厂区照片和资料对象；当前原网页抓取超时，暂按来源线索保存，不写成已认定工业遗产。",
        ev(
            "活动展板所称老厂区照片和资料；具体厂房、模具、冲压机和原址坐标待市博物馆或企业档案核验",
            "汽车覆盖件模具设计、制造、调试和冲压工艺的专业技术记忆；历史设备谱系待补",
            "模具工人、专业厂协作和十堰汽车城技术人员形成的工业文化记忆；口述史和厂史资料待采集",
            "当前企业仍有生产活动，但历史厂区是否保留、搬迁或更新不明；本条不推断现状",
        ),
        record_status="source_lead",
        aliases=["东风模具老厂区", "东风模具冲压技术有限公司模具分公司"],
        asset_kind="industrial_archive",
    ),
    rec(
        "HBI-SY-027",
        "东风汽车车轮有限公司（汽车工业文化资料对象）",
        "十堰市",
        "张湾区（老厂区待核）",
        "汽车车轮工业",
        "research_candidate",
        "十堰汽车工业遗产宣传活动明确的老厂区资料对象；原址、厂房和设备待核",
        ["shiyan_car_school_2017"],
        "十堰市博物馆进校园活动展板把汽车车轮有限公司作为具有历史意义的老厂区照片和资料对象；目前只有活动报道线索，尚未取得逐栋建筑、设备或法定认定档案。",
        ev(
            "活动展板所称车轮厂老厂区照片和资料；车轮生产线、模具、设备和厂界待核",
            "钢制车轮制造、冲压成形和汽车专业化配套的技术记忆；历史工艺和设备待补",
            "车轮厂工人、配套生产和车城工业社区记忆；人物、厂志和影像档案待采集",
            "企业名称可由公开产业资料确认，但历史厂区现状和遗存去向未核；本条保持来源线索状态",
        ),
        record_status="source_lead",
        aliases=["东风车轮厂", "汽车车轮有限公司老厂区"],
        asset_kind="industrial_archive",
    ),
    rec(
        "HBI-SY-028",
        "东风汽车泵业有限公司（汽车工业文化资料对象）",
        "十堰市",
        "张湾区（老厂区待核）",
        "汽车零部件工业",
        "research_candidate",
        "十堰汽车工业遗产宣传活动明确的老厂区资料对象；原址、厂房和设备待核",
        ["shiyan_car_school_2017"],
        "十堰市博物馆进校园活动展板把汽车泵业有限公司作为具有历史意义的老厂区照片和资料对象；目前只有活动报道线索，未取得厂志、普查编号、厂界或设备清单。",
        ev(
            "活动展板所称泵业老厂区照片和资料；泵类产品、加工设备、车间与厂界待核",
            "汽车泵类零部件制造和专业化配套的技术记忆；产品谱系、工艺和设备待补",
            "泵业工人、东风专业厂协作和十堰汽车城生活记忆；口述史和企业档案待采集",
            "企业曾作为东风零部件专业厂存在，历史厂区保存和当前利用未知；本条保持来源线索状态",
        ),
        record_status="source_lead",
        aliases=["东风泵业", "汽车泵业有限公司老厂区"],
        asset_kind="industrial_archive",
    ),
]


RECORD_PATCHES: dict[str, dict[str, Any]] = {
    "HBI-SY-007": {
        "source_keys": ["shiyan_44_local_2022"],
        "notes_append": "十堰广播电视台进一步记录44厂厂志和老职工口述：厂内水井、芦席棚、三座近9米液压机、94吨底漆电泳槽、124米红外线烘干室和冲压机等物项；2021年整体搬迁后部分厂区面临城市工程，核心区域拟保护开发。",
        "evidence_append": {
            "material_carriers": "十堰广播电视台还记录厂内水井、三座近9米液压机、94吨底漆电泳槽、124米红外线烘干室和冲压机",
            "technical_memory": "报道记录44厂自制生产设备、94吨电泳槽、124米红外线烘干室及1984年引进2000吨级冲压机的技术升级",
            "social_memory": "厂志和老职工口述保留1969年百二河畔建厂、芦席棚、马灯和干打垒等三线建设记忆",
            "current_use_or_loss": "2021年整体搬迁，部分旧厂区用于城市工程，报道同时记载核心区域拟建工业遗产博物馆或文创产业园",
        },
    },
    "HBI-SY-011": {
        "source_keys": ["shiyan_car_school_2017"],
        "notes_append": "十堰市博物馆进校园活动还将汽车弹簧有限公司老厂区照片和资料列为展示对象；与46厂官方答复可能存在企业沿革关系，但具体挂牌、边界和组成项仍待普查档案核对。",
    },
}


def append_once(row: dict[str, Any], field: str, text: str) -> None:
    old = row.get(field, "")
    if text not in old:
        row[field] = old.rstrip("；。 ") + "；" + text


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    existing_by_id = {row["inventory_id"]: row for row in records}
    names = {row["name"] for row in records}
    added = 0
    for new_row in NEW_RECORDS:
        old = existing_by_id.get(new_row["inventory_id"])
        if old is None:
            if new_row["name"] in names:
                raise SystemExit(f"conflicting duplicate name: {new_row['name']}")
            records.append(new_row)
            existing_by_id[new_row["inventory_id"]] = new_row
            names.add(new_row["name"])
            added += 1
        elif old != new_row:
            raise SystemExit(f"conflicting duplicate record: {new_row['inventory_id']}")
    for key, value in NEW_SOURCES.items():
        if key in sources and sources[key] != value:
            raise SystemExit(f"conflicting source: {key}")
        sources[key] = value
    for inventory_id, patch in RECORD_PATCHES.items():
        row = existing_by_id[inventory_id]
        row["source_keys"] = list(dict.fromkeys(row.get("source_keys", []) + patch.get("source_keys", [])))
        note = patch.get("notes_append")
        if note:
            append_once(row, "notes", note)
        for field, addition in (patch.get("evidence_append") or {}).items():
            append_once(row.setdefault("cultural_evidence", {}), field, addition)

    targets = data.setdefault("research_targets", {})
    coverage = targets.setdefault("coverage_sources", [])
    if "shiyan_auto_protection_measures_2018" not in coverage:
        coverage.append("shiyan_auto_protection_measures_2018")
    known = targets.setdefault("known_survey_outputs", [])
    output = {
        "name": "十堰市汽车工业文化遗产普查成果（2016）",
        "source_keys": ["shiyan_car_survey_2018"],
        "immovable_count": 100,
        "movable_count": 300,
        "status": "省级官方答复确认普查规模；逐项清单、挂牌编号、档案开放范围和现状需向十堰市文物/档案部门申请核验",
    }
    if not any(item.get("name") == output["name"] for item in known):
        known.append(output)
    elif output not in known:
        raise SystemExit("conflicting known survey output")

    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_ab_sources={len(NEW_SOURCES)} added_records={added} "
        f"updated_records={len(RECORD_PATCHES)} total_records={len(records)} total_sources={len(sources)}"
    )


if __name__ == "__main__":
    main()
