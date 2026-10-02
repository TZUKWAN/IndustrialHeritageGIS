from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "republic_industrial_mark_2024": {
        "source_type": "national_ministry_list_report",
        "title": "名单公布！湖北3个+5个",
        "org": "湖北日报",
        "pub_date": "2024-12-09",
        "url": "https://news.hubeidaily.net/pc/c_3424413.html",
        "authority": "B",
        "notes": "湖北日报转述国家文物局、工业和信息化部公布的‘共和国印记’名单，明确湖北3件见证物：2250kV/9000kVA工频试验成套装置、青山热电厂1号汽轮机转子、青山热电厂首台发电机铭牌；并明确5个工业遗产保护利用典型案例：葛洲坝水利枢纽、武钢一号高炉、航天066导弹基地、老虎洞水电站、黄石国家矿山公园。用于补充工业实物和保护利用案例层，不替代各项目的核心物项清单和现场测绘。",
    },
    "cepri_2250kv_wuhan_2026": {
        "source_type": "university_official_field_report",
        "title": "校领导带队赴武汉理工大学、中国电力科学研究院调研交流",
        "org": "湖北理工学院党政办公室",
        "pub_date": "2026-03-20",
        "url": "https://bgs.hbpu.edu.cn/info/1030/9403.htm",
        "authority": "A",
        "notes": "湖北理工学院官网报道，2026年3月19日调研期间参观中国电力科学研究院雷电防护研究所，并明确武汉分院户外试验场保存‘共和国印记’见证物2250kV/9000kVA工频试验成套装置；用于确认武汉分院和户外试验场空间语境，不推断产权边界、开放时间或精确坐标。",
    },
    "qingshan_turbine_history_2026": {
        "source_type": "state_media_industrial_history",
        "title": "工业血脉的见证——寻访国家能源集团国家工业遗产",
        "org": "中国证券报",
        "pub_date": "2026-01-12",
        "url": "https://www.cs.com.cn/cj2020/202601/t20260112_6532832.html",
        "authority": "B",
        "notes": "中国证券报报道青山热电厂1号机组为1957年投运的山海关内早期高温高压火电机组，1号汽轮机转子连续运行50年后于2007年退役并保存在厂区门口；用于补充实物保存和电力技术史信息，现状维护和公众开放边界仍需现场核验。",
    },
    "wugang_case_2025": {
        "source_type": "provincial_media_industrial_case",
        "title": "活力中国调研行丨青山江滩再现漫画晚霞，工业遗址变身生态绿洲",
        "org": "湖北日报",
        "pub_date": "2025-08-26",
        "url": "https://news.hubeidaily.net/pc/c_4446819.html",
        "authority": "B",
        "notes": "湖北日报报道明确指出武钢一号高炉保护案例获评工业遗产保护利用典型案例，并将其与青山热电厂、武钢一米七轧机工程、五粮库码头、红房子等工业文化遗存放在同一片区叙述；用于补充保护利用案例层，不替代国家工业遗产核心物项名录。",
    },
    "yichang_066_case_2025": {
        "source_type": "provincial_government_industrial_case",
        "title": "远安‘旧三线’蝶变‘新三线’",
        "org": "湖北省自然资源厅",
        "pub_date": "2025-05-12",
        "url": "https://zrzyt.hubei.gov.cn/bmdt/sxdt/202505/t20250512_5646817.shtml",
        "authority": "A",
        "notes": "省自然资源厅报道远安县三线航天066基地旧址为全国重点文物保护单位，并入选第六批国家工业遗产，介绍机关片区、历史馆、机关大楼、通讯楼、资料楼、导弹模型展列厅和红峰厂区等保护利用路线；具体核心物项边界仍以名录和测绘资料为准。",
    },
    "national_energy_republic_case_2024": {
        "source_type": "central_enterprise_industrial_case",
        "title": "集团2+3！入选‘共和国印记’见证物和工业遗产保护利用典型案例名单",
        "org": "国家能源集团（中国电力网）",
        "pub_date": "2024-12-05",
        "url": "https://www.chinapower.org.cn/detail/438371.html",
        "authority": "B",
        "notes": "国家能源集团来源报道明确老虎洞水电站入选工业遗产保护利用典型案例，说明其红色基因、历史脉络和民族地区建设记忆，并提出工业遗产、红色教育基地和文明传承中心的活化方向。",
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
        "HBI-WUHAN-061",
        "2250kV/9000kVA工频试验成套装置（武汉分院户外试验场）",
        "武汉市",
        "洪山区",
        "电力试验与防雷装备",
        "republic_witness",
        "国家‘共和国印记’见证物（2024）",
        ["republic_industrial_mark_2024", "cepri_2250kv_wuhan_2026"],
        "国家专题名单将该装置列为湖北工业实物见证物；湖北理工学院官网进一步确认其位于中国电力科学研究院武汉分院户外试验场。装置完整构成、产权、保护级别和开放方式需由中国电科院档案与现场资料补证。",
        ev(
            "中国电力科学研究院武汉分院户外试验场的2250kV/9000kVA工频试验成套装置；公开资料未列出全部分设备和附属构筑物",
            "超高压工频试验、雷电防护和电力设备检验技术记忆，涉及国产试验变压器和成套试验工程；技术档案待进一步开放",
            "电力科研人员、试验工程师和湖北电力工业技术进步共同形成的科研组织记忆；专家、工匠和科研合作口述史待采集",
            "目前仍在武汉分院户外试验场语境中展示或保存；具体维护状态、参观条件和精确坐标未公开",
        ),
        aliases=["2250kV工频试验成套装置", "9000kVA工频试验装置", "中国电科院武汉分院工频试验装置"],
        asset_kind="industrial_equipment",
    ),
    rec(
        "HBI-WUHAN-062",
        "青山热电厂1号汽轮机转子（共和国印记见证物）",
        "武汉市",
        "青山区",
        "火力发电",
        "republic_witness",
        "国家‘共和国印记’见证物（2024）；青山热电厂国家工业遗产核心物项",
        ["republic_industrial_mark_2024", "qingshan_turbine_history_2026"],
        "湖北日报确认该转子入选国家‘共和国印记’见证物，中国证券报报道其对应1957年投运的早期高温高压火电机组，连续运行50年后于2007年退役并保存在厂区门口。保护标识、具体位置和开放边界仍需现场核验。",
        ev(
            "青山热电厂1号机组汽轮机转子及其基座、铭牌和检修痕迹；国家工业遗产名录还列有配电室、生产办公楼和厂区铁路等关联物项",
            "1957年高温高压火电机组运行、检修和国产电力工业技术成长的实物见证；苏联设计和早期热电联产技术记忆待档案补充",
            "青山热电厂职工、武汉工业区供电和热电联产形成的城市工业记忆；几代电力工人口述史和影像资料待归档",
            "公开报道指转子退役后保存在厂区门口；当前维护、展示、产权和公众访问规则需现场核查",
        ),
        aliases=["青山热电厂一号汽轮机转子", "青电1号机组汽轮机转子"],
        asset_kind="industrial_equipment",
    ),
    rec(
        "HBI-WUHAN-063",
        "青山热电厂首台发电机铭牌（共和国印记见证物）",
        "武汉市",
        "青山区",
        "火力发电与电力档案",
        "republic_witness",
        "国家‘共和国印记’见证物（2024）；青山热电厂国家工业遗产档案类物项",
        ["republic_industrial_mark_2024"],
        "湖北日报列明青山热电厂首台发电机铭牌入选国家‘共和国印记’见证物，申报单位为国网湖北省电力有限公司。铭牌的实际保管地点、编号、材质和公开展示状态待权属单位档案核验。",
        ev(
            "青山热电厂首台发电机铭牌这一档案/实物标识，具体尺寸、材质、编号和配套设备尚未公开",
            "1957年青山热电厂首台机组建设、并网和电力工程设备管理的物证信息；机组图纸、档案和设备铭牌谱系待补",
            "首台机组投产对武汉工业区、热电职工和地方电力建设的集体记忆；相关人物和仪式影像待采集",
            "由国网湖北省电力有限公司申报并纳入国家见证物名单；现存状态、展陈地点和访问权限需权属单位确认",
        ),
        aliases=["青山热电厂首台发电机铭牌", "青电首台发电机铭牌"],
        asset_kind="industrial_archive_object",
    ),
    rec(
        "HBI-YC-017",
        "葛洲坝水利枢纽工业遗产保护利用案例",
        "宜昌市",
        "西陵区",
        "水利水电工程",
        "national_cultural_relic_related",
        "国家工业遗产保护利用典型案例（2024）；葛洲坝水利枢纽国家工业遗产",
        ["republic_industrial_mark_2024"],
        "湖北日报列明中国长江电力股份有限公司葛洲坝电厂‘以新质生产力赋能葛洲坝水利枢纽保护和利用’入选国家工业遗产保护利用典型案例。本条记录保护利用文化景观层，坝体、厂房、通航设施和运行档案的具体边界沿用国家名录与现场测绘核定。",
        ev(
            "葛洲坝水利枢纽坝体、泄洪和通航设施、水电厂房及运行展示空间；本轮来源只确认案例名称，核心物项清单需与国家名录逐项对照",
            "大型水利枢纽建设、发电调度、航运组织和运行维护形成的工程技术记忆；工程档案和设备谱系待补",
            "三线建设、水电建设者、宜昌城市发展和长江航运共同形成的工业社会记忆；职工口述史和建设影像待系统整理",
            "工程仍承担发电和通航等功能，保护利用与生产运行并行；参观路线、保护边界和敏感设施开放范围需以管理单位为准",
        ),
        aliases=["葛洲坝电厂工业遗产保护利用", "葛洲坝水利枢纽工业文化景观"],
        asset_kind="industrial_landscape",
    ),
    rec(
        "HBI-WUHAN-064",
        "武钢一号高炉工业遗产保护利用案例",
        "武汉市",
        "青山区",
        "钢铁冶炼",
        "national_cultural_relic_related",
        "国家工业遗产保护利用典型案例（2024）；武钢一号高炉国家工业遗产",
        ["republic_industrial_mark_2024", "wugang_case_2025"],
        "湖北日报确认武钢一号高炉保护案例入选国家工业遗产保护利用典型案例，并将其与青山片区工业遗产活化、武钢一米七轧机工程、五粮库码头和红房子等遗存联系起来。本条强调保护利用和工业文化景观关系，不把新闻报道当作核心物项边界证明。",
        ev(
            "武钢一号高炉炉体、出铁场及相关厂区遗存属于国家工业遗产核心语境；具体构筑物、设备和缓冲范围需依国家名录、保护规划和现场测绘确认",
            "钢铁冶炼、高炉生产组织和大型钢铁联合企业技术进步形成的工业技术记忆；设备档案、工艺流程和厂志待补",
            "武钢职工、青山工业区建设和钢铁城市生活共同形成的产业工人记忆；社区、劳模和口述史资料待继续采集",
            "案例已形成保护利用和片区活化叙事；现状厂区权属、开放范围、展示设施和生产安全边界需现场核验",
        ),
        aliases=["武钢一号高炉保护利用", "武钢1号高炉工业文化景观"],
        asset_kind="industrial_landscape",
    ),
    rec(
        "HBI-YC-018",
        "航天066导弹基地保护利用文化景观",
        "宜昌市",
        "远安县",
        "三线航天军工",
        "national_cultural_relic_related",
        "国家工业遗产保护利用典型案例（2024）；全国重点文物保护单位与第六批国家工业遗产",
        ["republic_industrial_mark_2024", "yichang_066_case_2025"],
        "湖北日报列明航天066导弹基地‘保护+开发’案例入选国家典型案例；省自然资源厅进一步确认远安县066基地旧址为全国重点文物保护单位并入选第六批国家工业遗产，介绍机关片区、历史馆、资料楼、通讯楼和红峰厂区等活化线路。核心物项边界仍需依保护规划核验。",
        ev(
            "机关办公楼、资料楼、通讯楼、印刷厂、机关大礼堂、幼儿园、露天电影院、红峰厂区工具精加车间和设计楼等三线基地遗存；具体清单以国家名录和保护规划为准",
            "导弹研制、工具精加工、军工生产组织和三线建设工程技术形成的航天工业记忆；档案、设备和型号谱系待继续整理",
            "三线建设者、军工职工家庭和远安地方社会共同形成的航天精神与工业社区记忆；人物档案和口述史待补",
            "基地已发展历史馆、展列厅和研学路线等保护利用场景；不同片区的产权、开放、安全和修缮边界需现场核查",
        ),
        aliases=["航天066基地旧址保护利用", "远安三线航天基地工业文化景观"],
        asset_kind="industrial_landscape",
    ),
]


UPDATES: dict[str, dict[str, Any]] = {
    "HBI-ES-002": {
        "source_keys": ["republic_industrial_mark_2024", "national_energy_republic_case_2024"],
        "notes_append": "补充国家‘共和国印记’专题报道：老虎洞水电站入选工业遗产保护利用典型案例，活化方向包括工业遗产、红色教育基地和文明传承中心。",
    },
    "HBI-HS-005": {
        "source_keys": ["republic_industrial_mark_2024"],
        "notes_append": "补充国家‘共和国印记’专题报道：黄石国家矿山公园入选工业遗产保护利用典型案例；不替代大冶铁矿工业遗产群已有的矿区与核心物项来源。",
    },
}


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
    for inventory_id, update in UPDATES.items():
        row = existing_by_id[inventory_id]
        old_sources = row.get("source_keys", [])
        row["source_keys"] = list(dict.fromkeys(old_sources + update["source_keys"]))
        note = update["notes_append"]
        if note not in row.get("notes", ""):
            row["notes"] = row.get("notes", "").rstrip() + " " + note
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_z_sources={len(NEW_SOURCES)} added_records={len(NEW_RECORDS)} "
        f"updated_records={len(UPDATES)} total_records={len(records)} total_sources={len(sources)}"
    )


if __name__ == "__main__":
    main()
