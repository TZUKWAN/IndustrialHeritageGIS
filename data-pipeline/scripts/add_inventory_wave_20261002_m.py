from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "hubei_boundary_2017_wlt": {
        "source_type": "government_protection_notice",
        "title": "省政府划定公布809处第一至六批省级文物保护单位保护范围和建设控制地带",
        "org": "湖北省文化和旅游厅（原湖北省文化厅）",
        "pub_date": "2017-12-04",
        "url": "https://wlt.hubei.gov.cn/bmdt/dtyw/201911/t20191121_1356173.shtml",
        "authority": "A",
        "notes": "省文物部门公开说明鄂政办发〔2017〕68号划定第一至六批省级文物保护单位保护范围和建设控制地带，并说明县级初划、省文物局审核和现场论证程序；本来源用于确认保护边界制度背景，具体方向和距离仍以公报文本、测绘和现场核验为准。",
    },
    "wlt_xiantao_relics_2023": {
        "source_type": "official_cultural_heritage_report",
        "title": "仙桃市博物馆匠心做好文物保护留住历史文化印迹",
        "org": "湖北省文化和旅游厅",
        "pub_date": "2023-10-18",
        "url": "https://wlt.hubei.gov.cn/bmdt/szyw/xt/202310/t20231018_4898275.shtml",
        "authority": "A",
        "notes": "省文旅厅报道仙桃市文物调查登记不可移动文物270处，并确认排湖闸入选第八批湖北省文物保护单位；来源补足地方普查、保护管理和现状治理语境，不替代排湖闸本体测绘。",
    },
    "mzw_wufeng_source_yang_2023": {
        "source_type": "government_cultural_trade_report",
        "title": "五峰渔洋关 万里茶道车痕在 千年古镇茶飘香",
        "org": "湖北省民族宗教事务委员会",
        "pub_date": "2023-11-15",
        "url": "https://mzw.hubei.gov.cn/ztzl/dzh/jcdzh/202311/t20231115_4946398.shtml",
        "authority": "A",
        "notes": "省民族宗教事务部门报道清末民初渔洋关有汉口源泰、新泰茶庄等茶商网络，并记载宫文朋与源泰洋行合作设立源泰茶庄、在五峰等地收购毛红茶；用于连接汉口洋行建筑与湖北茶叶生产贸易网络，具体账册和厂址分工仍待档案核验。",
    },
    "whcbs_salt_bank_industrial_network_2020": {
        "source_type": "local_cultural_publishing",
        "title": "第四章“万国建筑博物馆”——汉口盐业银行",
        "org": "武汉出版社/武汉文化出版网站",
        "pub_date": None,
        "url": "https://www.whcbs.com/Upload/BookReadFile/202002/c020dd817d274b44bee1d25f14614edc/OPS/chapter004.html",
        "authority": "B",
        "notes": "武汉地方文化出版资料记载汉口盐业银行为北四行成员、位于中山大道北京路口，曾对交通、铁道及华资工商业、国有工矿企业和公共事业提供融资；本来源支撑工业金融与城市工业网络解释，不等同工厂生产遗址认定。",
    },
    "whcbs_salt_bank_history_2020": {
        "source_type": "local_cultural_publishing",
        "title": "盐业银行——汉口里分文化资料",
        "org": "武汉出版社/武汉文化出版网站",
        "pub_date": None,
        "url": "https://www.whcbs.com/Upload/BookReadFile/202002/815f04fc613b45f399c1d43f7777afc5/ops/chapter017.html",
        "authority": "B",
        "notes": "武汉地方文化出版资料记录盐业银行汉口分行的建造、建筑结构、抗战时期占用、公私合营及其对国有工矿企业和公共事业的投资关系；人物、客户和贷款档案仍需以档案馆目录复核。",
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
        "HBI-WUHAN-053",
        "源泰洋行旧址",
        "武汉市",
        "茶叶加工与贸易文化景观",
        "provincial_heritage_related",
        "第八批湖北省文物保护单位（2021）；近代茶业贸易节点",
        [
            "hubei_provincial_relics_1098",
            "hubei_8th_relics_2021",
            "hubei_chenghuang_boundary_2024",
            "mzw_wufeng_source_yang_2023",
        ],
        "省级名录和公报确认江岸区源泰洋行旧址及其保护范围；省民族宗教事务部门资料把汉口源泰洋行与五峰渔洋关茶庄、毛红茶收购网络联系起来。本条把建筑作为茶业生产—加工—贸易体系的工业文化节点记录，仍与具体茶厂、茶栈和原料产地分开建档。",
        ev(
            "源泰洋行旧址建筑本体及其与汉口俄租界茶业贸易空间的关系；现存室内构件、仓储/办公分区和历史边界待测绘",
            "汉口洋行组织茶叶收购、加工转运、出口和跨区域贸易的经营技术；官方资料确认源泰茶庄在五峰等地收购毛红茶，账册、合同和设备谱系待补",
            "汉口茶商、五峰茶农、茶庄伙计、运输商和万里茶道沿线社区共同形成的生产与贸易记忆；地方口述、企业档案和商号谱系待规范采集",
            "第八批省保身份及2024年保护范围公报已确认；现状经营、开放、产权、修缮和与周边茶业建筑的整体保护关系需复核",
        ),
        district="江岸区",
        aliases=["源泰洋行旧址（那克伐申公馆）", "汉口源泰洋行", "源泰茶庄汉口旧址"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-WUHAN-054",
        "汉口盐业银行大楼",
        "武汉市",
        "工业金融与城市公共事业文化",
        "provincial_heritage_related",
        "湖北省省级文物保护单位（名录列名）；近代工业金融节点",
        [
            "hubei_provincial_relics_1098",
            "hubei_boundary_2017_wlt",
            "whcbs_salt_bank_industrial_network_2020",
            "whcbs_salt_bank_history_2020",
        ],
        "省级名录确认汉口盐业银行大楼（1926年、江岸区）及其文保身份；武汉地方文化出版资料明确记载其对交通、铁道、华资工商业、国有工矿企业和公共事业的融资关系。本条作为工业金融与城市工业网络文化节点纳入扩展层，不把金融建筑混称为生产厂址，客户档案和具体项目清单待档案核验。",
        ev(
            "1926年钢筋混凝土银行大楼、营业大厅、办公层及历史街区环境；建筑构件、室内设备和保护边界按文保公报与现场测绘复核",
            "盐业税收金融、银行放款、交通与铁道建设融资以及工矿企业和公共事业资本组织；公开资料已确认关系方向，贷款档案、客户名录与资金流向待补",
            "银行职员、营造厂、工矿企业、交通部门和汉口金融街共同形成的城市工业化记忆；人物、组织和社区口述史待规范采集",
            "省级文保名录及2017年保护范围制度背景已确认；现为金融机构办公使用的具体状态、开放方式、产权和修缮风险需最新现场资料复核",
        ),
        district="江岸区",
        aliases=["盐业银行大楼", "汉口盐业银行旧址", "盐业银行汉口分行旧址"],
        asset_kind="industrial_cultural_landscape",
    ),
]


PATCHES: dict[str, dict[str, Any]] = {
    "HBI-XT-003": {
        "source_keys_add": ["hubei_chenghuang_boundary_2024", "wlt_xiantao_relics_2023"],
        "notes": "省级名录确认仙桃排湖闸为1951年近现代水利遗产；省政府公报给出闸体保护范围，省文旅厅又确认仙桃市文物普查登记和第八批省保申报背景。本条保留水闸本体、江汉平原排涝灌溉和地方水利社会记忆，精确工程范围、设备和现状管护仍需测绘。",
        "cultural_evidence_updates": {
            "material_carriers": "1951年排湖闸闸体、闸门、启闭设备、堤岸和配套渠系；省政府公报已明确以闸体为基准的保护范围方向和距离，完整工程清单待水利档案与现场测绘核对",
            "technical_memory": "江汉平原排涝、灌溉和闸门调度技术，以及新中国初期水利工程组织；水文记录、设计图纸、机电设备谱系和受益范围待补",
            "social_memory": "排湖周边防洪排涝、农业生产、村落迁建与水利管理形成的公共记忆；工程管理人员、受益村庄和口述史待规范采集",
            "current_use_or_loss": "第八批省级文保身份、2024年保护范围公报和仙桃文物普查报道已确认；实体工程持续使用、开放展示、产权和风险状况需按水利主管部门最新资料复核",
        },
    },
    "HBI-WUHAN-028": {
        "source_keys_add": ["hubei_boundary_2017_wlt"],
        "notes": "省级名录确认汉口英商和利冰厂旧址为1911年近现代工业建筑；省文物部门公开说明第一至六批省保保护范围已按鄂政办发〔2017〕68号划定。本条暂保留省保公布名与和利冰厂/汽水厂企业谱系疑点，冰厂与汽水厂的分址、设备、产权和现状需专项测绘与档案核验。",
        "cultural_evidence_updates": {
            "material_carriers": "和利冰厂/汽水厂旧址建筑、制冰与汽水生产空间、可能的冷媒/供水/装卸设施；省保本体范围已进入保护制度，现存设备与两处厂址关系待核",
            "technical_memory": "近代机械制冰、碳酸饮料生产和城市冷饮供应技术；生产流程、机器型号、工艺档案和产品包装待补",
            "social_memory": "汉口冷饮消费、冰厂与汽水厂工人、法租界商贸和城市公共生活记忆；企业职工与社区口述史待补",
            "current_use_or_loss": "省级文保名录身份和保护边界制度背景已确认；开放利用、产权、修缮及冰厂/汽水厂分址现状需最新现场资料复核",
        },
    },
    "HBI-WUHAN-029": {
        "source_keys_add": ["hubei_chenghuang_boundary_2024"],
        "notes": "省级名录和2024年省政府公报确认俄商新泰茶厂水塔为1876年近现代工业遗存，并公布保护范围和建设控制地带。本条把水塔与汉口砖茶厂生产、供水和俄商茶业贸易网络联系起来，厂房、管网、设备和水塔实际功能仍需档案与现场核验。",
        "cultural_evidence_updates": {
            "material_carriers": "俄商新泰茶厂水塔及与砖茶厂相关的红砖厂房、供水设施和厂区空间；公报已明确水塔保护范围，完整茶厂边界和遗存清单待测绘",
            "technical_memory": "砖茶生产、蒸汽/机械加工和工业供水技术；水塔容量、供水对象、蒸汽设备和产品外销档案待补",
            "social_memory": "俄商茶厂、汉口茶工、鄂南茶源地和万里茶道贸易网络的跨区域记忆；职工、茶商与社区口述史待规范采集",
            "current_use_or_loss": "第八批省保身份、2024年保护范围公报和省级名录已确认；水塔使用、周边改造、开放和产权状况需最新现场资料复核",
        },
    },
    "HBI-XIANGYANG-024": {
        "source_keys_add": ["hubei_boundary_2017_wlt"],
        "notes": "省级名录确认南漳县夹马寨造纸作坊为清代传统纸业生产遗存；省文物部门公开说明第一至六批省保保护范围已按鄂政办发〔2017〕68号划定。本条保留纸作坊建筑、纸池、晾晒和工具等待核字段，不把工艺细节写成已测绘事实。",
    },
    "HBI-ES-008": {
        "source_keys_add": ["hubei_boundary_2017_wlt"],
        "notes": "省级名录确认咸丰县黄金洞炼硝场遗址为明代矿物加工遗存；省文物部门公开说明第一至六批省保保护范围已按鄂政办发〔2017〕68号划定。本条记录炼硝技术与地方资源利用线索，窑炉、原料、生产规模、边界和现状仍待考古与现场资料核验。",
    },
    "HBI-WUHAN-046": {
        "source_keys_add": ["hubei_boundary_2017_wlt"],
        "notes": "省级名录确认武昌第一纱厂旧址为1919年近现代工业建筑；省文物部门公开说明第一至六批省保保护范围已按鄂政办发〔2017〕68号划定。本条与第一纱厂办公楼旧址分别保留名录层级和组成关系，厂区边界、设备、职工社区和现状需继续核验。",
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
        existing_by_id = {row["inventory_id"]: row for row in records}

    # Keep shared official-source notes scoped to every object that reuses the URL.
    if "hubei_8th_relics_2021" in sources:
        sources["hubei_8th_relics_2021"]["notes"] = (
            "省政府公报公布第八批湖北省文物保护单位，列出源泰洋行旧址、俄商新泰茶厂水塔、"
            "排湖闸和坛子洞古茶园等工业、茶业与水利相关对象；具体保护范围另见后续公报。"
        )
    if "hubei_chenghuang_boundary_2024" in sources:
        sources["hubei_chenghuang_boundary_2024"]["notes"] = (
            "省政府公报公布第八批省保保护范围和建设控制地带，涉及源泰洋行旧址、俄商新泰茶厂水塔、"
            "排湖闸、坛子洞古茶园和城隍潭码头遗址等对象；本来源只记录公报级边界证据，精确坐标和现状仍需测绘。"
        )

    for inventory_id, patch in PATCHES.items():
        row = existing_by_id.get(inventory_id)
        if row is None:
            raise SystemExit(f"patch target missing: {inventory_id}")
        merge_unique(row, "source_keys", patch.get("source_keys_add") or [])
        merge_unique(row, "aliases", patch.get("aliases") or [])
        updates = patch.get("cultural_evidence_updates") or {}
        if updates:
            row.setdefault("cultural_evidence", {}).update(updates)
        for key, value in patch.items():
            if key not in {"source_keys_add", "aliases", "cultural_evidence_updates"}:
                row[key] = value
        row["source_keys"] = sorted(set(row.get("source_keys") or []))

    data["research_targets"]["coverage_rule"] = (
        "每条对象至少绑定名录/普查/规划/企业史/档案遗产或来源确认资料；"
        "工业遗产实体、工业文化景观、工业金融与贸易节点、工业旅游相关场景、档案文献和待核验线索分层记录。"
        "文化证据字段只记录来源中明确出现的载体、技术、社会记忆和利用状态，未核实内容保持待核。"
    )
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_m_records={len(NEW_RECORDS)} wave_m_sources={len(NEW_SOURCES)} "
        f"patched_records={len(PATCHES)} total_records={len(records)} total_sources={len(sources)}"
    )


if __name__ == "__main__":
    main()
