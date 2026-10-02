from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "hubei_history_streets_xiangyang_2026": {
        "source_type": "district_government_official_media",
        "title": "全省第三批历史文化街区名单出炉！襄阳六〇三、六〇九榜上有名！",
        "org": "襄城区人民政府门户网站（汉水襄阳）",
        "pub_date": "2026-06-18",
        "url": "http://xc.xiangyang.gov.cn/news/202606/t20260618_4019626.shtml",
        "authority": "A",
        "notes": "省政府确定9处街区为湖北省第三批历史文化街区（2026-06-18公布），襄阳市文字六〇三厂历史文化街区与襄阳市六〇九研究所历史文化街区入选（均位于襄城区）；六〇三厂1965年建成、曾为全国印刷行业翘楚，90年代低谷后2017年起修旧如旧改造，已集聚60余家企业、带动3000余人创业就业、年产值近3亿元；六〇九研究所前身为中国航空工业第609研究所（航空机载机电），60年代初迁址、2005年整体搬南京后厂区改造为文旅地标（老厂房、红砖家属楼、百货商店、公社大食堂、网球场、杉水民宿），近20家企业签约落户；襄阳累计5处省级历史文化街区（另含陈老巷、东津十字街、太平店老街）。",
    },
}


RECORD = {
    "inventory_id": "HBI-XIANGYANG-034",
    "name": "六〇九研究所旧址（中国航空工业第609研究所历史文化街区）",
    "city": "襄阳市",
    "district_county": "襄城区隆中大道",
    "industry_category_l1": "航空军工工业",
    "recognition_level": "provincial_heritage_related",
    "recognition_status": "湖北省第三批历史文化街区（2026年6月18日公布，襄阳市六〇九研究所历史文化街区）；三线航空工业旧址活化对象",
    "record_status": "source_confirmed",
    "geocode_status": "pending",
    "source_keys": ["hubei_history_streets_xiangyang_2026"],
    "cultural_evidence": {
        "material_carriers": "老厂房群、红砖家属楼、杉树林、百货商店、公社大食堂等三线建设时期建筑与街区肌理（隆中大道）；核心物项清单与保护范围待街区保护规划核验",
        "technical_memory": "中国航空工业第609研究所为航空机载机电领域重要力量，60年代初迁址襄阳的 三线建设航空工业布局记忆",
        "social_memory": "研究所职工与家属区数十年生活记忆；2005年整体搬迁南京后生活区空置与三线记忆封存，改造后公社大食堂、杉树林成为时代记忆载体",
        "current_use_or_loss": "按修旧如旧、保护为主、原址原貌、落架重修原则改造为文旅新地标：标准化室外网球场运营、杉水民宿成为网红打卡地，近20家企业签约落户涵盖观光旅游、体育健身、休闲度假业态；2026年获省级历史文化街区身份",
    },
    "notes": "直接取自襄城区政府网转载汉水襄阳报道（A级）；本条为三线航空研究所旧址活化记录，609所现址在南京、襄阳部分为旧址街区；历史文化街区保护不等于工业遗产法定认定；街区保护规划、核心物项与产权边界待核；坐标未核验保持待核。",
    "aliases": ["中国航空工业第609研究所旧址", "六〇九历史文化街区"],
    "asset_kind": "industrial_site",
}


PROV007_PATCH = {
    "source_keys_append": ["hubei_history_streets_xiangyang_2026"],
    "current_use_or_loss": "以修旧如旧方式改造为六〇三文创园，2025年建设603印·刻非遗传承中心和603印刷博物馆；2026年6月文字六〇三厂历史文化街区获评湖北省第三批历史文化街区，已集聚60余家企业、带动3000余人创业就业、年产值近3亿元，从工业锈带蜕变为融合文创、展览、休闲、消费的生活秀带；保护边界和展陈开放制度待核",
    "notes_append": "2026年6月获评湖北省第三批历史文化街区（与2025年度省级工业遗产构成双身份），活化数据（60余家企业、3000余人就业、年产值近3亿元）见襄城区政府网2026-06-18报道。",
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    existing = next((row for row in records if row["inventory_id"] == RECORD["inventory_id"]), None)
    if existing is not None:
        if existing != RECORD:
            raise SystemExit("conflicting duplicate record")
        added = 0
    else:
        if any(row["name"] == RECORD["name"] for row in records):
            raise SystemExit("conflicting duplicate name")
        records.append(RECORD)
        added = 1
    for key, source in SOURCES.items():
        if key in sources and sources[key] != source:
            raise SystemExit(f"conflicting source: {key}")
    sources.update(SOURCES)
    prov007 = next((row for row in records if row["inventory_id"] == "HBI-PROV-007"), None)
    if prov007 is None:
        raise SystemExit("record not found: HBI-PROV-007")
    updated = 0
    for key in PROV007_PATCH["source_keys_append"]:
        if key not in prov007["source_keys"]:
            prov007["source_keys"].append(key)
            updated = 1
    if prov007["cultural_evidence"]["current_use_or_loss"] != PROV007_PATCH["current_use_or_loss"]:
        prov007["cultural_evidence"]["current_use_or_loss"] = PROV007_PATCH["current_use_or_loss"]
        updated = 1
    if PROV007_PATCH["notes_append"] not in prov007["notes"]:
        prov007["notes"] = prov007["notes"] + PROV007_PATCH["notes_append"]
        updated = 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_bc_sources={len(SOURCES)} added_records={added} updated_records={updated} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
