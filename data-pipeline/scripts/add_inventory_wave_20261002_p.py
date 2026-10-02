from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "hubei_industrial_survey_2019": {
        "source_type": "provincial_government_reply",
        "title": "关于对省政协十二届二次会议第20190017号提案的答复",
        "org": "湖北省经济和信息化厅",
        "pub_date": "2019-08-30",
        "url": "https://jxt.hubei.gov.cn/fbjd/xxgkml/qtzdgknr/jytabl/zxwyta/201908/t20190830_363861.shtml",
        "authority": "A",
        "notes": "湖北省经信厅公开答复明确：2018年开展全省工业遗产摸底并建立省工业遗产项目库，另开展湖北工业遗产（1949—1979年）专项调查，基本摸清保存状况；这是本项目覆盖逻辑的省级政策与普查依据，不是某一处具体遗址的认定文件。",
    },
    "hubei_industrial_management_draft_2024": {
        "source_type": "provincial_policy_draft",
        "title": "省经济和信息化厅办公室关于征求《湖北省工业遗产管理办法（征求意见稿）》修改意见的函",
        "org": "湖北省经济和信息化厅",
        "pub_date": "2024-12-13",
        "url": "https://jxt.hubei.gov.cn/fbjd/zc/qtzdgkwj/gsgg/202412/t20241213_5461585.shtml",
        "authority": "A",
        "notes": "公开征求意见稿将工业遗产的物质遗存扩展至厂房、车间、作坊、矿区、设备、工具、产品、档案等，并将生产工艺、规章制度、企业文化和工业精神列为非物质遗存；文件仍是征求意见稿，不能当作正式认定名单。",
    },
    "xianning_fangyuan_shipyard_2021": {
        "source_type": "municipal_water_bureau_report",
        "title": "〖咸宁长江岸线行④〗做好水文章 打好生态牌",
        "org": "咸宁市水利和湖泊局（咸宁日报供稿）",
        "pub_date": "2021-11-03",
        "url": "https://slj.xianning.gov.cn/ztzl/cjdbh/202111/t20211112_2428530.shtml",
        "authority": "A",
        "notes": "官方水利部门转载报道定位嘉鱼县陆溪镇方圆船厂旧址，记载船厂占地近300亩、岸线约900米、码头吃水约9米，2016年停产后于2020年底前拆除并复绿，现场仍可见老船厂旗杆痕迹；同时记录千余员工、厂房和800吨龙门吊等工业文化景观信息。",
    },
    "jingmen_refinery_headquarters_2024": {
        "source_type": "provincial_media_industrial_history",
        "title": "荆门炼油厂厂部旧址：当时的指挥部，如今的创新摇篮",
        "org": "湖北日报新闻客户端",
        "pub_date": "2024-11-15",
        "url": "https://news.hubeidaily.net/pc/c_3340991.html",
        "authority": "B",
        "notes": "湖北日报报道确认厂部旧址位于荆门高新区·掇刀区白庙街道五一桥社区、炼厂路104号，已入选荆门市第三批历史建筑名录；文章记录1969年五七油田会战第八分部、1972年荆门炼油厂、1973—1975年厂部大楼建设、占地5258平方米、会议室和档案室等物质与社会记忆。",
    },
    "jingzhou_first_provincial_industrial_heritage_2024": {
        "source_type": "municipal_media_industrial_heritage_list",
        "title": "湖北省首批省级工业遗产名单公布 荆州市2个企业项目入选",
        "org": "荆州日报（长江网转载）",
        "pub_date": "2024-03-10",
        "url": "https://news.cjn.cn/zjjjdpd/yw_20048/202403/t4845318.htm",
        "authority": "B",
        "notes": "报道援引荆州市经信局信息，明确石油四机企业文化陈列馆和白云边国家级荣誉档案入选湖北省首批省级工业遗产；同时给出四机陈列馆建筑、三线建设与汽车驾驶室工间信息，以及白云边档案、兼香型白酒产业史和酒博物馆利用信息。",
    },
    "jingzhou_siji_industry_2019": {
        "source_type": "public_organization_industry_report",
        "title": "农工党荆州市长大总支参观考察中石化四机石油机械有限公司",
        "org": "中国农工民主党湖北省委员会",
        "pub_date": "2019-10-29",
        "url": "https://www.hbng.gov.cn/index.php?id=2451",
        "authority": "B",
        "notes": "公开报道介绍荆州石油机械产业集群、江汉石油管理局第四机械厂及四机企业文化陈列馆，记录固井压裂设备、钻机、修井机等产品谱系和“浴火而生”“西北拓荒”“战略转移”等展陈板块，用于补足四机的技术与社会文化证据。",
    },
    "huanggang_guanyao_industrial_heritage_2026": {
        "source_type": "local_media_industrial_heritage_report",
        "title": "蕲春县管窑镇岚头矶工艺陶器厂入选省级工业遗产名单，千年陶脉再添荣光！",
        "org": "云上黄冈（黄冈日报）",
        "pub_date": "2026-01-01",
        "url": "https://pc.hgdaily.com.cn/p/481903.html",
        "authority": "B",
        "notes": "黄冈日报报道确认蕲春县管窑镇岚头矶工艺陶器厂入选省级工业遗产，并记录废旧礼堂改造文化小剧场、推板窑车间工业遗存展示、老车间美术馆/非遗展馆和研学文创利用；正式省级名单附件、项目边界和公布日期仍需经信部门原件复核。",
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
        "HBI-XN-013",
        "方圆船厂旧址（陆溪镇）",
        "咸宁市",
        "嘉鱼县",
        "船舶修造与港口运输",
        "research_candidate",
        "来源确认的船厂旧址（已拆除；工业文化景观）",
        ["xianning_fangyuan_shipyard_2021"],
        "咸宁市水利和湖泊局转载的官方报道定位嘉鱼县陆溪镇方圆船厂旧址，记录其2008年落户、近300亩用地、约900米岸线、可建造和靠泊5万吨级船舶，2016年停产并于2020年底前拆除复绿。现地仅报道可见老船厂旗杆痕迹，故保留为已拆除工业文化景观候选，不把厂房和龙门吊写成现存遗产。",
        ev(
            "方圆船厂旧址、原厂房、混凝土路面和800吨龙门吊等已拆除工业设施；报道仅确认现场仍可见老船厂旗杆痕迹",
            "船舶建造与港口作业，近900米岸线、约9米吃水和5万吨级船舶靠泊条件构成技术与工程记忆",
            "陆溪古镇轮船码头、河沙码头、货运码头、千余名船厂员工和长江沿线产业生活构成工业文化与社区记忆",
            "方圆船舶2016年停产、2019—2020年因长江岸线整治拆除并复绿；现状边界、遗存标识与口述史待现场核验",
        ),
        aliases=["陆溪方圆船厂旧址", "方圆船舶旧址", "嘉鱼方圆船厂旧址"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-JM-017",
        "荆门炼油厂厂部旧址",
        "荆门市",
        "掇刀区",
        "石油化工工业",
        "municipal_historical_building",
        "荆门市第三批历史建筑；官方媒体报道确认的三线石化厂部旧址",
        ["jingmen_refinery_headquarters_2024"],
        "湖北日报报道确认荆门炼油厂厂部旧址位于炼厂路104号、荆门高新区·掇刀区白庙街道五一桥社区辖区，入选荆门市第三批历史建筑名录。报道记载厂部建筑占地5258平方米，含主楼、附楼、前后院、档案室和可容纳约200人的会议室；本条保持历史建筑认定与工业遗产研究对象的层级区别。",
        ev(
            "厂部旧址主楼、两座附楼、前后院、档案室和保持原貌的会议室；建筑占地约5258平方米，具体构件清单待测绘",
            "1969年五七油田会战第八分部、1972年荆门炼油厂、1973年底设计和约1975年投用的厂部大楼，连接战备石化基地建设与炼油工程管理技术",
            "全国各地建设者、荆门炼油厂第一代设计和管理人员、石化职工及三线建设者的奋斗与铁人精神记忆",
            "1989年厂部搬迁后由设计院及金中工程持续使用，现为办公场所并定期维护；保护边界、档案开放和公众参观方式待核",
        ),
        aliases=["荆门炼油厂厂部大楼", "荆门石化厂部旧址", "炼厂路104号厂部旧址"],
        asset_kind="industrial_building",
    ),
    rec(
        "HBI-JZ-013",
        "石油四机企业文化陈列馆（原三线厂房）",
        "荆州市",
        "荆州区",
        "石油装备制造工业",
        "provincial",
        "湖北省首批省级工业遗产",
        ["jingzhou_first_provincial_industrial_heritage_2024", "jingzhou_siji_industry_2019"],
        "荆州日报报道和公开行业参观资料确认石油四机企业文化陈列馆为湖北省首批省级工业遗产项目，原为20世纪70年代初从甘肃敦煌迁建至荆州、支援江汉油田会战的第一栋厂房和汽车驾驶室生产工间。红砖外墙、砖木混合结构平房和宣传标语保留了原始风貌；陈列馆与现企业生产区的边界、展品目录和开放制度待补档案。",
        ev(
            "原三线厂房、红砖外墙、砖木混合结构平房、宣传标语及企业文化陈列空间；设备和档案目录待核",
            "汽车驾驶室生产工间、石油钻采装备制造、固井压裂设备、钻机和修井机等产品与工艺谱系",
            "从敦煌战略转移、三线建设、支援江汉油田会战和几代石油四机职工形成的“石油师”劳动与企业精神记忆",
            "已作为企业文化陈列馆和红色教育/参观空间使用；省级工业遗产核心物项清单、产权和开放时段待核",
        ),
        aliases=["四机企业文化陈列馆", "江汉石油管理局第四机械厂旧址", "石油四机原厂房"],
        asset_kind="industrial_building",
    ),
    rec(
        "HBI-JZ-014",
        "白云边国家级荣誉档案",
        "荆州市",
        "松滋市",
        "酿酒工业与企业档案",
        "provincial",
        "湖北省首批省级工业遗产（档案类项目）",
        ["jingzhou_first_provincial_industrial_heritage_2024"],
        "荆州日报报道确认白云边国家级荣誉档案入选湖北省首批省级工业遗产，记录白云边从地方型白酒发展为兼香型白酒企业的产业历程；白云边·酒博物馆作为档案展览区域已接待10万余人次。档案全宗、实物奖项清单和数字化开放范围待档案馆及企业核验。",
        ev(
            "白云边国家级荣誉档案、品牌奖项和白云边·酒博物馆展陈空间；完整档案全宗及实物目录待核",
            "兼香型白酒生产、产品品牌化和地方酿酒企业发展谱系；具体曲药、窖池、设备和工艺档案待补",
            "松滋白酒产业、企业职工、品牌消费记忆和地方工业身份由档案展陈与参观活动承载",
            "作为省级工业遗产档案项目在白云边·酒博物馆展示并用于工业旅游；档案保管、借阅和长期数字保存待核",
        ),
        aliases=["白云边荣誉档案", "白云边酒业工业档案", "白云边·酒博物馆档案展"],
        asset_kind="documentary_heritage",
    ),
    rec(
        "HBI-HG-007",
        "蕲春县管窑镇岚头矶工艺陶器厂",
        "黄冈市",
        "蕲春县",
        "陶瓷工业",
        "provincial",
        "湖北省首批省级工业遗产（地方媒体报道；正式附件待复核）",
        ["huanggang_guanyao_industrial_heritage_2026"],
        "黄冈日报报道确认蕲春县管窑镇岚头矶工艺陶器厂入选省级工业遗产，并记录推板窑车间、旧礼堂、老车间和陶器生产文化空间的活化利用。与底册中的“HBI-PROV-008 湖北管窑传统陶器生产制造基地”可能存在同址或申报主体关联，因暂未取得省级正式附件，先分列并保留关联核验任务。",
        ev(
            "岚头矶工艺陶器厂老车间、推板窑车间、旧礼堂和陶器生产设施；展示空间与核心物项清单待现场和申报材料核验",
            "传统陶器生产、推板窑烧成及窑业作坊组织；产品谱系、燃料、窑具和工艺流程待补",
            "管窑制陶技艺、工匠传承、地方陶业身份和蕲春陶器消费记忆由厂区展示与非遗展馆承载",
            "旧礼堂已改造为文化小剧场，推板窑车间用于工业遗存展示，老车间兼作美术馆/非遗技艺展馆和研学文创空间；产权、开放与保护边界待核",
        ),
        aliases=["岚头矶工艺陶器厂", "管窑陶器厂", "蕲春管窑工艺陶器厂"],
        asset_kind="industrial_cultural_landscape",
        related_inventory_ids=["HBI-PROV-008"],
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

    duplicate_ids = {row["inventory_id"] for row in NEW_RECORDS} & set(existing_by_id)
    if duplicate_ids:
        if not all(
            existing_by_id[i] == row
            for i, row in ((r["inventory_id"], r) for r in NEW_RECORDS if r["inventory_id"] in duplicate_ids)
        ):
            raise SystemExit(f"conflicting duplicate records: {sorted(duplicate_ids)}")
    else:
        records.extend(NEW_RECORDS)

    sources.update({key: value for key, value in NEW_SOURCES.items() if key not in sources})
    data.setdefault("research_targets", {})["coverage_sources"] = [
        "hubei_industrial_survey_2019",
        "hubei_industrial_management_draft_2024",
    ]
    data["research_targets"]["coverage_rule"] = (
        "每条对象至少绑定名录/普查/规划/企业史/档案遗产或来源确认资料；"
        "工业遗产实体、工业文化景观、工业金融与贸易节点、工业旅游相关场景、档案文献和待核验线索分层记录。"
        "省级摸底和管理办法征求意见稿只作为范围、字段和分级依据，不替代具体对象的名录或现场证据；"
        "古代窑业、矿冶、铸钱与史前纺织遗址仅在来源明确出现生产性证据时纳入，并保留考古候选或相关层级；"
        "文化证据字段只记录来源中明确出现的载体、技术、社会记忆和利用状态，未核实内容保持待核。"
    )
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_p_sources={len(NEW_SOURCES)} added_records={len(NEW_RECORDS)} "
        f"total_records={len(records)} total_sources={len(sources)}"
    )


if __name__ == "__main__":
    main()
