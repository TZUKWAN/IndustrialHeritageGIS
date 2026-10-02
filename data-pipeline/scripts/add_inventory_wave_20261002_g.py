from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "hubei_revolutionary_register_2022": {
        "source_type": "government_register",
        "title": "省文化和旅游厅关于公布第二批湖北省革命文物名录的通知",
        "org": "湖北省文化和旅游厅",
        "pub_date": "2022-12-07",
        "url": "https://wlt.hubei.gov.cn/zfxxgk/zc/qtzdgkwj/202212/t20221207_4445353.shtml",
        "authority": "A",
        "notes": "省文旅厅通知确认第二批名录包含不可移动文物579处，其中省保6处、市县保41处、未定级532处；附件一为本轮生产性旧址和茶业生产景观的名称与行政区依据。",
    },
    "hubei_revolutionary_sites_2022": {
        "source_type": "government_register_attachment",
        "title": "湖北省不可移动革命文物名录（第二批）",
        "org": "湖北省文化和旅游厅",
        "pub_date": "2022-12-07",
        "url": "https://wlt.hubei.gov.cn/zfxxgk/zc/qtzdgkwj/202212/P020221208373333318248.pdf",
        "authority": "A",
        "notes": "官方附件逐条列出江陵县鄂西红军兵工厂旧址、监利县洪湖兵工厂遗址、柳关红军被服厂旧址、沙洋县新四军豫鄂边印钞厂遗址和红安县狮子山新四军第五师茶园；附件文本中沙洋县一行存在疑似排版/OCR异常，已结合相邻沙洋县条目和湖北行政区标准名暂归沙洋县，需地方档案复核。",
    },
    "hubei_daily_handspinning_2022": {
        "source_type": "official_media",
        "title": "鄂北手纺织训练所：抗战干部的摇篮",
        "org": "湖北日报",
        "pub_date": "2022-11-07",
        "url": "https://news.hubeidaily.net/pc/946393.html",
        "authority": "B",
        "notes": "湖北日报报道确认1939年鄂北手纺织训练所位于谷城县茨河镇下街，三期培训200多人、提供军需棉纱100万斤，并在多地设织布厂、铁工厂、木工厂分厂；报道还记录旧址修复、展览馆建设和生产实物展示。",
    },
}

SOURCE_PATCHES: dict[str, dict[str, Any]] = {
    # This key was created in an earlier wave for the same official PDF.  Keep
    # its note aligned with the full attachment so URL de-duplication does not
    # export a misleading single-object summary.
    "hg_hongan_repair_2022": {
        "source_type": "government_register_attachment",
        "pub_date": "2022-12-07",
        "notes": "省文旅厅第二批不可移动革命文物名录附件，逐条列出红安县红一军修械所旧址以及本轮江陵、监利、沙洋、红安等生产性旧址/生产景观；红一军修械所条目标注为红安县文物保护单位，其他条目的级别以附件逐项标注为准。",
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


def listed_production_evidence(kind: str, level: str) -> dict[str, str]:
    return ev(
        f"官方革命文物名录确认的{kind}旧址/遗址名称；现存建筑、厂房、设备和保护边界待现场核验",
        f"名录所指{kind}生产或修配活动构成工业技术线索；工艺流程、工具、产品谱系和生产组织待档案与实测补证",
        "革命战争时期相关生产人员、地方社会和工业记忆；具体人物、组织与口述史待补",
        f"列入湖北省第二批不可移动革命文物名录（{level}）；现状保存、利用、开放和产权信息待继续核验",
    )


NEW_RECORDS: list[dict[str, Any]] = [
    rec(
        "HBI-XIANGYANG-026",
        "谷城县鄂北手纺织训练所旧址",
        "襄阳市",
        "纺织工业与工业教育",
        "provincial_heritage_related",
        "湖北省第五批文物保护单位；第一批革命文物名录省级文物保护单位",
        [
            "hubei_provincial_relics_1098",
            "hubei_revolutionary_sites_2021",
            "hubei_daily_handspinning_2022",
        ],
        "省级文保名录和第一批革命文物附件确认鄂北手纺织训练所旧址位于襄阳市谷城县；湖北日报进一步记录训练班、军需棉纱生产及织布厂、铁工厂、木工厂分厂。该条把生产、技术教育和抗战社会记忆合并记录，不升级为工信部门工业遗产认定。",
        ev(
            "茨河镇下街汉江边鄂北手纺织训练所旧址、石碑、修复中的四栋12间房屋和展览馆图片/实物展示；设备原件、建筑测绘与保护边界待核",
            "1939—1940年三期训练班、军需棉纱生产和棉布/毛巾/药棉/被服制作；谷城庙滩、盛康、城关、石花街等地织布厂、铁工厂、木工厂分厂构成区域生产网络",
            "面向鄂西北15个县培养200多名学员、发展党员和抗日骨干；训练所兼具工业教育、后勤生产与地方党组织活动空间",
            "省级文保与革命文物名录身份已确认；旧址按原貌修复四栋12间房屋，展览馆于2021年开始建设，开放、产权和完整保存范围待核",
        ),
        district="谷城县",
        aliases=["鄂北手纺织训练所旧址", "茨河手纺织训练所", "鄂西北区党委茨河手纺织训练所旧址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-JZ-009",
        "江陵县鄂西红军兵工厂旧址",
        "荆州市",
        "军工制造工业",
        "ungraded_revolutionary_relic",
        "湖北省第二批不可移动革命文物名录；未定级不可移动文物",
        ["hubei_revolutionary_register_2022", "hubei_revolutionary_sites_2022"],
        "省文旅厅第二批革命文物附件逐条列出江陵县鄂西红军兵工厂旧址；湖北日报关于江陵沙岗湘鄂西革命根据地旧址群的报道确认当地曾设红军兵工厂等后勤基地。本条保持未定级和待核状态，不把区域叙述替代单体地址与遗存核验。",
        listed_production_evidence("鄂西红军兵工厂", "未定级不可移动文物"),
        district="江陵县",
        aliases=["鄂西红军兵工厂遗址", "沙岗红军兵工厂旧址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-JZ-010",
        "监利县洪湖兵工厂遗址",
        "荆州市",
        "军工制造工业",
        "ungraded_revolutionary_relic",
        "湖北省第二批不可移动革命文物名录；未定级不可移动文物",
        ["hubei_revolutionary_register_2022", "hubei_revolutionary_sites_2022"],
        "省文旅厅第二批革命文物附件列出监利县洪湖兵工厂遗址；监利地方红色资源整理资料还提到湘鄂西兵工厂遗址保护利用，但未能将其与本名录条目建立精确空间对应，因此现存厂房、设备和具体村落位置全部保留待核。",
        listed_production_evidence("洪湖兵工厂", "未定级不可移动文物"),
        district="监利县",
        aliases=["洪湖兵工厂旧址", "湘鄂西兵工厂遗址（名称待核）"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-JZ-011",
        "监利县柳关红军被服厂旧址",
        "荆州市",
        "军需纺织工业",
        "ungraded_revolutionary_relic",
        "湖北省第二批不可移动革命文物名录；未定级不可移动文物",
        ["hubei_revolutionary_register_2022", "hubei_revolutionary_sites_2022"],
        "省文旅厅第二批革命文物附件列出监利县柳关红军被服厂旧址；柳关作为湘鄂西革命根据地后方和物资集散地的历史叙述可与该生产性旧址互证，但厂房、缝纫设备、产品和具体边界仍需地方档案与现场调查。",
        listed_production_evidence("柳关红军被服厂", "未定级不可移动文物"),
        district="监利县",
        aliases=["柳关红军被服厂遗址", "柳关被服厂旧址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-JM-015",
        "沙洋县新四军豫鄂边印钞厂遗址",
        "荆门市",
        "印刷与金融物资工业",
        "ungraded_revolutionary_relic",
        "湖北省第二批不可移动革命文物名录；未定级不可移动文物",
        ["hubei_revolutionary_register_2022", "hubei_revolutionary_sites_2022"],
        "省文旅厅第二批革命文物附件列出新四军豫鄂边印钞厂遗址；附件该行的县名出现疑似排版/OCR异常，结合同页连续沙洋县条目和荆门市行政区标准名暂归沙洋县，需用地方文保档案或原件复核具体行政村和地址。",
        ev(
            "官方名录确认印钞厂遗址名称；现存印刷建筑、纸张/制版/印刷工具、厂址边界和遗存状态待现场核验",
            "战时纸币印刷、制版、纸张供应与金融物资生产构成印刷工业技术线索；设备谱系和工艺档案待补",
            "新四军豫鄂边根据地印钞人员、金融组织、物资运输和地方社会记忆；人物与口述史待补",
            "第二批革命文物名录确认名称，但县名文本存在校勘风险；保护级别、产权、开放与保存情况待核",
        ),
        district="沙洋县",
        aliases=["新四军豫鄂边印钞厂旧址", "豫鄂边印钞厂遗址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-HG-006",
        "红安县狮子山新四军第五师茶园",
        "黄冈市",
        "茶业生产与工业文化景观",
        "ungraded_revolutionary_relic",
        "湖北省第二批不可移动革命文物名录；未定级不可移动文物",
        ["hubei_revolutionary_register_2022", "hubei_revolutionary_sites_2022"],
        "省文旅厅第二批革命文物附件列出红安县狮子山新四军第五师茶园；本条只把茶园作为茶业原料生产端和革命生产景观纳入工业文化关联底册，未将其直接认定为工业遗产，茶叶加工、运输和具体保存边界需专项调查。",
        ev(
            "狮子山茶园及其可能关联的山地生产空间、道路和水土设施；茶园范围与现存构筑物待测绘",
            "茶树栽培、采摘和原料供给构成茶业生产链线索；加工场所、工具、产品和供应关系未由本名录说明，待补证",
            "新四军第五师驻地及地方茶农、供给人员和革命生产记忆；人物、组织和口述史待补",
            "第二批革命文物名录确认未定级茶园名称；是否仍有连续生产、展示利用或保护管理措施待核",
        ),
        district="红安县",
        aliases=["狮子山茶园", "新四军第五师茶园遗址"],
        asset_kind="industrial_cultural_landscape",
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
        missing = sorted(set(NEW_SOURCES) - set(sources))
        if missing:
            sources.update(NEW_SOURCES)
        records.extend(NEW_RECORDS)

    for source_key, patch in SOURCE_PATCHES.items():
        source = sources.get(source_key)
        if source is None:
            raise SystemExit(f"source patch target missing: {source_key}")
        source.update(patch)

    data["research_targets"]["coverage_rule"] = (
        "每条对象至少绑定名录/普查/规划/企业史/档案遗产或来源确认资料；"
        "工业遗产实体、工业文化景观、工业旅游相关场景、档案文献和待核验线索分层记录。"
        "文化证据字段只记录来源中明确出现的载体、技术、社会记忆和利用状态，未核实内容保持待核。"
    )
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_g_records={len(NEW_RECORDS)} wave_g_sources={len(NEW_SOURCES)} "
        f"total_records={len(records)} total_sources={len(sources)}"
    )


if __name__ == "__main__":
    main()
