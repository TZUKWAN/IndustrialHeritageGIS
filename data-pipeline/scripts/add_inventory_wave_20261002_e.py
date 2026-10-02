from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "hubei_revolutionary_register_2021": {
        "source_type": "government_register",
        "title": "关于公布第一批湖北省革命文物名录的通知",
        "org": "湖北省文化和旅游厅",
        "pub_date": "2021-04-06",
        "url": "https://wlt.hubei.gov.cn/zfxxgk/zc/qtzdgkwj/202104/t20210406_3453303.shtml",
        "authority": "A",
        "notes": "省文旅厅公布第一批湖北省革命文物名录，明确全省不可移动革命文物1018处，其中全国重点文物保护单位33处、省级文物保护单位150处、市县级文物保护单位835处；本来源用于确认名录制度、公布日期和保护层级边界。",
    },
    "hubei_revolutionary_sites_2021": {
        "source_type": "government_register_attachment",
        "title": "湖北省不可移动革命文物名录（第一批）",
        "org": "湖北省文化和旅游厅",
        "pub_date": "2021-04-06",
        "url": "https://wlt.hubei.gov.cn/zfxxgk/zc/qtzdgkwj/202104/P020250509516989870325.pdf",
        "authority": "A",
        "notes": "官方附件列出本轮对象的行政区、名称和保护级别：十堰郧西县陕南军区枪械修配厂旧址（县级）；荆门钟祥市新四军江汉军区被服厂遗址（市级）、新四军中州币印刷厂遗址（县级）；孝感大悟县新四军第五师造纸厂、卷烟厂、毛巾厂旧址和鄂豫边区建设银行第二印钞厂遗址（均县级），孝昌县新四军五师弹药厂（县级）；荆州监利县湘鄂西农民银行造币厂遗址（县级）；黄冈红安县鄂豫皖革命军事委员会（熊家咀）兵工厂旧址、新四军第五师兵工厂旧址（均县级）。附件主要提供名录身份和级别，建筑、设备、边界、现状与开放信息需继续补证。",
    },
    "shennongjia_forestry_history_2025": {
        "source_type": "government_media",
        "title": "探秘神农架：从野人传说到绿色奇迹",
        "org": "国家林业和草原局/中国绿色时报",
        "pub_date": "2025-06-18",
        "url": "https://www.forestry.gov.cn/c/www/dfdt/638280.jhtml",
        "authority": "A",
        "notes": "国家林草局报道记载神农架20世纪60年代因国家木材建设需求形成大规模林业生产，十余年外运木材超过180万立方米；林业历史馆保存老麻绳、安全帽、刀斧锯凿等伐木时代实物，报道同时叙述停伐、保护区建立和林业转型。页面未给出单体建筑名录，故本条作为林业工业文化景观与馆藏线索记录。",
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


def listed_factory_evidence(kind: str, level: str) -> dict[str, str]:
    return ev(
        f"官方名录确认的{kind}旧址/遗址名称；现存建筑、厂房、设备和保护边界待现场核验",
        f"名录所指{kind}生产或修配活动构成工业技术线索；工艺流程、工具和生产组织待档案与实测补证",
        "革命战争时期相关生产人员、地方社会和工业记忆；具体人物、组织、口述史待补",
        f"列入湖北省第一批不可移动革命文物名录（{level}）；现状保存、利用、开放和产权信息待继续核验",
    )


NEW_RECORDS: list[dict[str, Any]] = [
    rec(
        "HBI-SY-014",
        "郧西县陕南军区枪械修配厂旧址",
        "十堰市",
        "军工修配工业",
        "county",
        "湖北省第一批不可移动革命文物名录；县级文物保护单位",
        ["hubei_revolutionary_register_2021", "hubei_revolutionary_sites_2021"],
        "省文旅厅名录将陕南军区枪械修配厂旧址列入郧西县县级文物保护单位；本条作为军工修配生产性旧址记录，保留县级文物层级，不升级为工业遗产认定。",
        listed_factory_evidence("枪械修配厂", "县级文物保护单位"),
        district="郧西县",
        aliases=["陕南军区枪械修配厂遗址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-JM-013",
        "钟祥市新四军江汉军区被服厂遗址",
        "荆门市",
        "军需纺织工业",
        "municipal_relic_related",
        "湖北省第一批不可移动革命文物名录；市级文物保护单位",
        ["hubei_revolutionary_register_2021", "hubei_revolutionary_sites_2021"],
        "省文旅厅名录将新四军江汉军区被服厂遗址列为钟祥市市级文物保护单位；本条记录军需纺织生产和革命工业文化，不等同国家或省级工业遗产。",
        listed_factory_evidence("被服厂", "市级文物保护单位"),
        district="钟祥市",
        aliases=["新四军江汉军区被服厂旧址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-JM-014",
        "钟祥市新四军中州币印刷厂遗址",
        "荆门市",
        "印刷与金融物资工业",
        "county",
        "湖北省第一批不可移动革命文物名录；县级文物保护单位",
        ["hubei_revolutionary_register_2021", "hubei_revolutionary_sites_2021"],
        "省文旅厅名录将新四军中州币印刷厂遗址列为钟祥市县级文物保护单位；本条把战时印刷生产空间纳入工业文化底册，未补写名录未提供的厂房和设备细节。",
        listed_factory_evidence("中州币印刷厂", "县级文物保护单位"),
        district="钟祥市",
        aliases=["新四军中州币印刷厂旧址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-XG-005",
        "大悟县新四军第五师造纸厂旧址",
        "孝感市",
        "造纸工业",
        "county",
        "湖北省第一批不可移动革命文物名录；县级文物保护单位",
        ["hubei_revolutionary_register_2021", "hubei_revolutionary_sites_2021"],
        "省文旅厅名录列出大悟县新四军第五师造纸厂旧址并标为县级文物保护单位；本条仅据名录确认生产性旧址身份，生产线、纸张品类、遗存边界和现状待补。",
        listed_factory_evidence("造纸厂", "县级文物保护单位"),
        district="大悟县",
        aliases=["新四军第五师造纸厂遗址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-XG-006",
        "大悟县新四军第五师卷烟厂旧址",
        "孝感市",
        "烟草加工工业",
        "county",
        "湖北省第一批不可移动革命文物名录；县级文物保护单位",
        ["hubei_revolutionary_register_2021", "hubei_revolutionary_sites_2021"],
        "省文旅厅名录列出大悟县新四军第五师卷烟厂旧址并标为县级文物保护单位；现存厂房、生产工具、卷烟工艺和社会记忆需继续从地方文保档案补证。",
        listed_factory_evidence("卷烟厂", "县级文物保护单位"),
        district="大悟县",
        aliases=["新四军第五师卷烟厂遗址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-XG-007",
        "大悟县新四军第五师毛巾厂旧址",
        "孝感市",
        "纺织工业",
        "county",
        "湖北省第一批不可移动革命文物名录；县级文物保护单位",
        ["hubei_revolutionary_register_2021", "hubei_revolutionary_sites_2021"],
        "省文旅厅名录列出大悟县新四军第五师毛巾厂旧址并标为县级文物保护单位；本条作为战时纺织生产旧址，现存建筑、设备和产品谱系待核。",
        listed_factory_evidence("毛巾厂", "县级文物保护单位"),
        district="大悟县",
        aliases=["新四军第五师毛巾厂遗址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-XG-008",
        "大悟县鄂豫边区建设银行第二印钞厂遗址",
        "孝感市",
        "印刷与金融物资工业",
        "county",
        "湖北省第一批不可移动革命文物名录；县级文物保护单位",
        ["hubei_revolutionary_register_2021", "hubei_revolutionary_sites_2021"],
        "省文旅厅名录列出大悟县鄂豫边区建设银行第二印钞厂遗址并标为县级文物保护单位；本条记录金融物资印制相关工业文化，印制设备和遗址空间待专项调查。",
        listed_factory_evidence("第二印钞厂", "县级文物保护单位"),
        district="大悟县",
        aliases=["鄂豫边区建设银行印钞厂遗址", "第二印钞厂旧址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-XG-009",
        "孝昌县新四军五师弹药厂旧址",
        "孝感市",
        "军工制造工业",
        "county",
        "湖北省第一批不可移动革命文物名录；县级文物保护单位",
        ["hubei_revolutionary_register_2021", "hubei_revolutionary_sites_2021"],
        "省文旅厅名录将孝昌县新四军五师弹药厂列为县级文物保护单位；本条作为弹药生产性旧址记录，具体生产设施、位置和保存状态待核验。",
        listed_factory_evidence("弹药厂", "县级文物保护单位"),
        district="孝昌县",
        aliases=["新四军五师弹药厂遗址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-JZ-008",
        "监利县湘鄂西农民银行造币厂遗址",
        "荆州市",
        "金融物资与铸造工业",
        "county",
        "湖北省第一批不可移动革命文物名录；县级文物保护单位",
        ["hubei_revolutionary_register_2021", "hubei_revolutionary_sites_2021"],
        "省文旅厅名录列出监利县湘鄂西农民银行造币厂遗址并标为县级文物保护单位；本条记录造币、金融物资和革命根据地工业文化，铸造设备与遗址边界待补。",
        listed_factory_evidence("农民银行造币厂", "县级文物保护单位"),
        district="监利县",
        aliases=["湘鄂西农民银行造币厂旧址", "湘鄂西农民银行造币厂遗址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-HG-004",
        "红安县鄂豫皖革命军事委员会（熊家咀）兵工厂旧址",
        "黄冈市",
        "军工制造工业",
        "county",
        "湖北省第一批不可移动革命文物名录；县级文物保护单位",
        ["hubei_revolutionary_register_2021", "hubei_revolutionary_sites_2021"],
        "省文旅厅名录列出红安县鄂豫皖革命军事委员会（熊家咀）兵工厂旧址并标为县级文物保护单位；本条与红安其他革命旧址分开建档，避免将不同兵工生产点合并。",
        listed_factory_evidence("熊家咀兵工厂", "县级文物保护单位"),
        district="红安县",
        aliases=["熊家咀兵工厂旧址", "鄂豫皖革命军事委员会兵工厂遗址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-HG-005",
        "红安县新四军第五师兵工厂旧址",
        "黄冈市",
        "军工制造工业",
        "county",
        "湖北省第一批不可移动革命文物名录；县级文物保护单位",
        ["hubei_revolutionary_register_2021", "hubei_revolutionary_sites_2021"],
        "省文旅厅名录列出红安县新四军第五师兵工厂旧址并标为县级文物保护单位；名称与熊家咀兵工厂不同，本条保留独立记录，具体位置、厂房和设备待地方档案核对。",
        listed_factory_evidence("新四军第五师兵工厂", "县级文物保护单位"),
        district="红安县",
        aliases=["新四军第五师兵工厂遗址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-SNJ-001",
        "神农架林业历史馆与伐木时代工业文化遗存",
        "神农架林区",
        "林业采伐与木材工业",
        "documentary_heritage",
        "国家林草局报道确认的林业工业文化景观与馆藏线索（未见独立工业遗产认定）",
        ["shennongjia_forestry_history_2025"],
        "国家林草局报道记载神农架20世纪60年代木材生产、林区工人和停伐转型，并明确林业历史馆保存老麻绳、安全帽、刀斧锯凿等实物；页面未给出馆舍建成年代和具体旧林场清单，故以工业文化景观与馆藏层级入库。",
        ev(
            "神农架林业历史馆中的老麻绳、安全帽、刀斧锯凿等伐木工具和林业生产实物；具体馆舍与旧林场建筑清单待核",
            "木材采伐、山地运输、林场组织和天然林停伐转型技术记忆；设备谱系待馆藏目录补证",
            "20世纪60年代进山建设的林业工人、林场社区和神农架由木材生产转向生态保护的集体记忆",
            "林业历史馆承担工业文化展示功能，神农架已全面停止天然林采伐并转向国家公园与生态保护；馆藏编目和旧林场保护边界待补",
        ),
        aliases=["神农架林业历史馆", "神农架伐木时代遗存"],
        asset_kind="industrial_cultural_landscape",
    ),
]


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    existing_by_id = {row["inventory_id"]: row for row in records}
    existing_names = {row["name"] for row in records}
    duplicate_sources = set(NEW_SOURCES) & set(sources)
    duplicate_ids = {row["inventory_id"] for row in NEW_RECORDS} & set(existing_by_id)
    duplicate_names = {row["name"] for row in NEW_RECORDS} & existing_names
    if duplicate_sources or duplicate_ids or duplicate_names:
        all_new_present = (
            set(NEW_SOURCES) <= set(sources)
            and all(sources[key] == value for key, value in NEW_SOURCES.items())
            and all(
                row["inventory_id"] in existing_by_id
                and existing_by_id[row["inventory_id"]] == row
                for row in NEW_RECORDS
            )
        )
        if not all_new_present:
            raise SystemExit(
                "partial or conflicting prior application: "
                f"sources={sorted(duplicate_sources)} ids={sorted(duplicate_ids)} names={sorted(duplicate_names)}"
            )
    else:
        missing = sorted(
            {
                key
                for row in NEW_RECORDS
                for key in row["source_keys"]
                if key not in sources and key not in NEW_SOURCES
            }
        )
        if missing:
            raise SystemExit(f"missing source keys: {missing}")
        sources.update(NEW_SOURCES)
        records.extend(NEW_RECORDS)

    data["research_targets"]["coverage_rule"] = (
        "每条对象至少绑定名录/普查/规划/企业史/档案遗产或来源确认资料；"
        "工业遗产实体、工业文化景观、工业旅游相关场景、档案文献和待核验线索分层记录。"
        "文化证据字段只记录来源中明确出现的载体、技术、社会记忆和利用状态，未核实内容保持待核。"
    )
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_e_records={len(NEW_RECORDS)} wave_e_sources={len(NEW_SOURCES)} "
        f"total_records={len(records)} total_sources={len(sources)}"
    )


if __name__ == "__main__":
    main()
