from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "hubei_archive_machinery_1966": {
        "source_type": "provincial_archive_catalog",
        "title": "湖北省工业厅工业企业设计任务书档案目录",
        "org": "湖北省档案馆",
        "pub_date": None,
        "url": "https://www.hbda.gov.cn/searchitembykey/207_8.jspx?page=3517",
        "authority": "A",
        "notes": "省档案馆开放目录列出1964—1967年形成的工业设计和基建档案，明确出现湖北省油泵厂、湖北省齿轮厂、沙市三厂（拖拉机厂）、长江配件厂、湖北省柴油机厂、湖北省拖拉机厂，以及湖北空压机厂、郧县风动工具厂、宜都矿山机械厂等名称；pub_date留空以区分档案形成年度与网页发布日期。题名可核，实体位置、厂界和保存状态待调档与现场核验。",
    },
    "hubei_archive_suizhou_silk_1965": {
        "source_type": "provincial_archive_catalog",
        "title": "湖北省外贸局关于随县缫丝厂搬迁基建等费用",
        "org": "湖北省档案馆",
        "pub_date": None,
        "url": "https://www.hbda.gov.cn/searchitem/207_8?page=3050",
        "authority": "A",
        "notes": "省档案馆目录显示档号SZ 77-2-301，档案形成于1965年，题名明确出现随县缫丝厂搬迁、基建及费用；用于补强随州缫丝厂区历史沿革，不替代厂界、建筑和设备测绘。",
    },
    "hubei_archive_suizhou_silk_1967": {
        "source_type": "provincial_archive_catalog",
        "title": "湖北省外贸局基建决算与随县缫丝厂车间扩建",
        "org": "湖北省档案馆",
        "pub_date": None,
        "url": "https://www.hbda.gov.cn/searchitembykey/207_8.jspx?page=3054",
        "authority": "A",
        "notes": "省档案馆目录显示档号SZ 77-2-348，档案形成于1967年，题名同时出现年度基建维修计划、1966年基建决算和随县缫丝厂车间扩建；用于补强缫丝生产空间和扩建沿革，设备清单与厂界待核。",
    },
    "hubei_archive_suizhou_silk_1972": {
        "source_type": "provincial_archive_catalog",
        "title": "关于改变随县缫丝厂领导关系、纺织配件与涤棉生产计划",
        "org": "湖北省档案馆",
        "pub_date": None,
        "url": "https://www.hbda.gov.cn/searchitem/207_8.jspx?page=1717",
        "authority": "A",
        "notes": "省档案馆目录显示档号SZ 63-1-63，档案形成于1972年，题名涉及随县缫丝厂领导关系、纺织配件、涤棉生产计划、规划和征地；用于补强企业组织与技术生产链条，不替代具体建筑和设备认定。",
    },
    "hubei_archive_suizhou_silk_1978": {
        "source_type": "provincial_archive_catalog",
        "title": "关于随县缫丝厂、棉纺厂亦工亦农轮换的处理意见",
        "org": "湖北省档案馆",
        "pub_date": None,
        "url": "https://www.hbda.gov.cn/searchitem/207_8.jspx?page=1424",
        "authority": "A",
        "notes": "省档案馆目录显示档号SZ 48-2-290，档案形成于1978年，题名涉及随县缫丝厂、棉纺厂职工亦工亦农轮换，补足企业劳动组织与社会记忆证据；不替代厂区边界和社区口述史。",
    },
}


def ev(material: str, technical: str, social: str, current: str) -> dict[str, str]:
    return {
        "material_carriers": material,
        "technical_memory": technical,
        "social_memory": social,
        "current_use_or_loss": current,
    }


def lead_record(inventory_id: str, name: str, city: str, district: str, industry: str, aliases: list[str]) -> dict[str, Any]:
    return {
        "inventory_id": inventory_id,
        "name": name,
        "city": city,
        "district_county": district,
        "industry_category_l1": industry,
        "recognition_level": "archive_lead",
        "recognition_status": "湖北省档案馆工业设计/基建档案题名线索；未见实体和法定工业遗产认定",
        "record_status": "source_lead",
        "geocode_status": "pending",
        "source_keys": ["hubei_archive_machinery_1966"],
        "cultural_evidence": ev(
            "档案题名确认历史企业或厂建项目，厂房、设备、生活设施和厂界待档案调阅、地方志及现场核验",
            "对应行业生产、设计和基建技术记忆；工艺流程、产品谱系和设备型号待厂志与企业档案核实",
            "企业与湖北工业化、工人群体和地方产业组织相连；职工社区、口述史和老照片待采集",
            "档案可确认设计、基建或管理活动，投产、搬迁、停产、遗址存续和现用途待核",
        ),
        "notes": "本条来自省档案馆开放目录的档案题名，先保留为来源线索，不将历史文件题名直接等同于现存遗产实体。",
        "aliases": aliases,
        "asset_kind": "industrial_site",
    }


NEW_RECORDS: list[dict[str, Any]] = [
    lead_record("HBI-JZ-017", "沙市三厂（拖拉机厂）旧址（档案线索）", "荆州市", "沙市区（具体厂址待核）", "农业机械与机械制造工业", ["沙市三厂", "沙市拖拉机厂"]),
    lead_record("HBI-PROV-010", "湖北省柴油机厂旧址（档案线索）", "湖北省（地市待核）", "待核", "柴油机与动力机械工业", ["湖北柴油机厂"]),
    lead_record("HBI-PROV-011", "湖北空压机厂旧址（档案线索）", "湖北省（地市待核）", "待核", "通用机械工业", ["湖北省空气压缩机厂", "湖北空压机厂"]),
    lead_record("HBI-SY-029", "郧县风动工具厂旧址（档案线索）", "十堰市", "郧阳区（原郧县，具体厂址待核）", "风动工具与机械制造工业", ["郧县风动工具厂", "郧阳风动工具厂"]),
    lead_record("HBI-YC-019", "宜都矿山机械厂旧址（档案线索）", "宜昌市", "宜都市（具体厂址待核）", "矿山机械工业", ["宜都矿山机械厂"]),
]


UPDATES: dict[str, dict[str, Any]] = {
    "HBI-SZ-003": {
        "source_keys": ["suizhou_industrial_history_2024", "hubei_archive_machinery_1966"],
        "notes": "随州日报确认湖北油泵油嘴厂曾落地随州；湖北省档案馆1964—1966年设计任务书目录另明确出现湖北省油泵厂，补强企业名称与基建谱系。具体厂址、建筑、设备和现状仍待地方志、厂志和现场核验。",
    },
    "HBI-SZ-004": {
        "source_keys": ["suizhou_industrial_history_2024", "hubei_archive_machinery_1966"],
        "notes": "随州日报确认武汉长江配件厂北郊拖车车间曾落地随州；湖北省档案馆设计任务书目录出现长江配件厂，补强企业与车间谱系。具体厂址、建筑和设备仍待档案和现场核验。",
    },
    "HBI-SZ-005": {
        "source_keys": ["suizhou_industrial_history_2024", "hubei_archive_machinery_1966"],
        "notes": "随州日报确认齿轮厂为随州工业化时期企业；湖北省档案馆设计任务书目录出现湖北省齿轮厂，补强齿轮制造企业谱系。具体厂址、设备和保护边界仍待核。",
    },
    "HBI-HS-016": {
        "source_keys": ["huangshi2019", "huangshi_steel_textile_2023", "hubei_archive_machinery_1966"],
        "notes": "黄石市首批工业遗产中的湖北省拖拉机厂旧址；黄石市住房和城市更新局报道确认老厂区产权和保护利用问题，省档案馆设计任务书目录另确认湖北省拖拉机厂1966年设计与扩建设计文件，厂房、设备和保护边界仍待核。",
    },
    "HBI-SZ-011": {
        "source_keys": ["suizhou_silk_reuse_2026", "suizhou_silk_community_2016", "hubei_archive_suizhou_silk_1965", "hubei_archive_suizhou_silk_1967", "hubei_archive_suizhou_silk_1972", "hubei_archive_suizhou_silk_1978"],
        "cultural_evidence": ev(
            "缫丝厂区原厂房、缫丝社区居民楼及周边公共空间；省档案馆目录补充1965年搬迁基建、1967年车间扩建，具体建筑、设备和厂界待测绘",
            "缫丝生产、纺织配件、涤棉计划与车间扩建的技术和组织记忆；省档案馆1972年目录补足生产计划与企业领导关系，机器清单待厂志核验",
            "缫丝社区作为典型企业社区，连接产业工人、居民生活和随州城市发展记忆；1978年档案涉及职工亦工亦农轮换，社区口述、老照片和生活设施待采集",
            "2026年随州日报报道市级规划现场调研缫丝厂区改造，提出保护与发展统一、推动厂区活化并植入多元业态；产权、环境风险、开放边界和档案原件待核",
        ),
        "notes": "随州日报报道确认缫丝厂区工业记忆、企业社区和活化改造方向；湖北省档案馆目录进一步提供1965年搬迁基建、1967年车间扩建、1972年生产组织、1978年劳动组织等连续档案题名。本条仍不推断完整厂界、具体设备或法定遗产级别。",
        "aliases": ["随州缫丝厂", "随县缫丝厂", "缫丝厂区改造", "缫丝社区"],
    },
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    by_id = {row["inventory_id"]: row for row in records}
    names = {row["name"] for row in records}
    added = 0
    updated = 0
    for row in NEW_RECORDS:
        if row["inventory_id"] in by_id:
            if by_id[row["inventory_id"]] != row:
                raise SystemExit(f"conflicting duplicate record: {row['inventory_id']}")
            continue
        if row["name"] in names:
            raise SystemExit(f"conflicting duplicate name: {row['name']}")
        records.append(row)
        by_id[row["inventory_id"]] = row
        names.add(row["name"])
        added += 1
    for key, value in NEW_SOURCES.items():
        if key in sources and sources[key] != value:
            raise SystemExit(f"conflicting source: {key}")
        sources[key] = value
    for inventory_id, patch in UPDATES.items():
        if inventory_id not in by_id:
            raise SystemExit(f"missing update target: {inventory_id}")
        row = by_id[inventory_id]
        for key, value in patch.items():
            row[key] = value
        updated += 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_ae_sources={len(NEW_SOURCES)} added_records={added} updated_records={updated} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
