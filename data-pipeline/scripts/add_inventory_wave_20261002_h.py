from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "wuhan_jinghan_union_2021": {
        "source_type": "government_news",
        "title": "武汉18处不可移动革命文物入选湖北省首批革命文物名录",
        "org": "武汉市人民政府",
        "pub_date": "2021-03-30",
        "url": "https://www.wuhan.gov.cn/sy/whyw/202103/t20210330_1658486.shtml",
        "authority": "A",
        "notes": "武汉市政府逐项列出首批革命文物中的京汉铁路总工会旧址，并说明武汉入选的18处全国重点文物保护单位级不可移动革命文物；用于确认对象名称、行政区和保护利用语境。",
    },
    "wuhan_jinghan_union_2023": {
        "source_type": "government_news",
        "title": "大学生在武汉街头骑行，重新认识了100年前的他们！",
        "org": "武汉市人民政府",
        "pub_date": "2023-10-03",
        "url": "https://www.wuhan.gov.cn/sy/whyw/202310/t20231003_2274152.shtml",
        "authority": "A",
        "notes": "武汉市政府报道把京汉铁路总工会旧址明确为1923年京汉铁路工人大罢工期间的秘密指挥部，并记录林祥谦、铁路工人运动和旧址现场叙事；用于补足工业社会记忆与当代展示证据。",
    },
    "hubei_industrial_heritage_reply_2018": {
        "source_type": "government_reply",
        "title": "关于湖北省政协十二届一次会议第20180329号提案的答复",
        "org": "湖北省文化和旅游厅",
        "pub_date": "2020-08-05",
        "url": "https://wlt.hubei.gov.cn/zfxxgk/fdzdgknr/qtzdgknr/jytabl/zxwyta/202008/t20200805_2742255.shtml",
        "authority": "A",
        "notes": "省文旅厅答复介绍第三次全国文物普查期间开展湖北工业遗产（1949—1979年）专项调查，并将汉口平汉铁路局旧址等列为省级文物保护与工业遗产保护语境中的重点对象；本来源用于制度和调查背景，不替代具体对象名录。",
    },
    "hubei_industrial_heritage_reply_2019": {
        "source_type": "government_reply",
        "title": "关于对省政协十二届二次会议第20190017号提案的答复",
        "org": "湖北省经济和信息化厅",
        "pub_date": "2019-08-30",
        "url": "https://jxt.hubei.gov.cn/fbjd/xxgkml/qtzdgknr/jytabl/201908/t20190830_363861.shtml",
        "authority": "A",
        "notes": "省经信厅答复称已将汉口平汉铁路局旧址等18处工业遗产申报为全国重点文物保护单位或省级文物保护单位，并要求继续开展工业遗产普查；用于确认铁路管理建筑的工业遗产保护语境。",
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
        "HBI-WUHAN-047",
        "京汉铁路总工会旧址",
        "武汉市",
        "铁路运输与工人文化",
        "national_cultural_relic_related",
        "第七批全国重点文物保护单位；第一批革命文物名录全国重点文物保护单位",
        [
            "hubei_provincial_relics_1098",
            "hubei_revolutionary_sites_2021",
            "wuhan_jinghan_union_2021",
            "wuhan_jinghan_union_2023",
        ],
        "省级文保名录列名为京汉铁路总工会会址，并注明2013年公布为第七批全国重点文物保护单位、公布名称为京汉铁路总工会旧址；武汉市政府资料进一步确认其为京汉铁路工人大罢工期间的秘密指挥部。本条纳入铁路工业生产组织、劳工文化和城市记忆层，不等同工信部门工业遗产名录。",
        ev(
            "京汉铁路总工会旧址建筑、纪念展陈和管理空间；建筑构件、院落边界与铁路相关实物清单待现场核验",
            "京汉铁路运输系统的工会组织、铁路工人协作和罢工期间的信息传递与生产秩序；铁路设备、调度档案和工运文献待补",
            "1923年京汉铁路工人大罢工、林祥谦及铁路工人群体的劳动记忆和工人运动传统；武汉城市工运教育持续使用该旧址叙事",
            "国家重点文物保护单位和革命文物名录身份已确认；由武汉市相关纪念馆管理并用于公共教育，消防、开放和展示范围需按最新管理资料复核",
        ),
        district="江岸区",
        aliases=["京汉铁路总工会会址", "二七大罢工秘密指挥部旧址"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-WUHAN-048",
        "汉口平汉铁路局旧址",
        "武汉市",
        "铁路运输工业与近代建筑",
        "provincial_heritage_related",
        "湖北省第五批文物保护单位（2008）；省级工业遗产保护语境中的铁路管理建筑",
        [
            "hubei_provincial_relics_1098",
            "hubei_industrial_heritage_reply_2018",
            "hubei_industrial_heritage_reply_2019",
        ],
        "省文旅厅1098处名录列出1911年汉口平汉铁路局旧址，所在地为武汉市江岸区；省文旅厅和省经信厅提案答复均将其放入湖北工业遗产调查、申报和保护语境。本条记录近代铁路管理建筑及其运营文化，建筑地址、保护范围和当前使用需以专项测绘与管理资料复核。",
        ev(
            "汉口平汉铁路局旧址建筑及其与胜利街铁路管理空间的关系；建筑结构、门窗、室内办公遗存和保护边界待测绘",
            "京汉/平汉铁路南段管理、调度、维修和运输组织的制度与办公技术记忆；铁路年鉴、线路图、设备和档案谱系待补",
            "铁路职工、铁路机构迁移、汉口城市物流和近代商贸格局记忆；铁路管理人员与周边社区口述史待补",
            "省级文物保护单位身份和工业遗产保护语境已确认；现状使用、产权、开放方式和保护工程需按最新管理资料复核",
        ),
        district="江岸区",
        aliases=["平汉铁路南局", "汉口平汉铁路南局旧址", "平汉铁路局旧址"],
        asset_kind="industrial_site",
    ),
]


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
        sources.update({k: v for k, v in NEW_SOURCES.items() if k not in sources})
        records.extend(NEW_RECORDS)

    data["research_targets"]["coverage_rule"] = (
        "每条对象至少绑定名录/普查/规划/企业史/档案遗产或来源确认资料；"
        "工业遗产实体、工业文化景观、工业旅游相关场景、档案文献和待核验线索分层记录。"
        "文化证据字段只记录来源中明确出现的载体、技术、社会记忆和利用状态，未核实内容保持待核。"
    )
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_h_records={len(NEW_RECORDS)} wave_h_sources={len(NEW_SOURCES)} "
        f"total_records={len(records)} total_sources={len(sources)}"
    )


if __name__ == "__main__":
    main()
