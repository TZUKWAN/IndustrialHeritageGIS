from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "huangshi_heritage_buildings_2019": {
        "source_type": "government_notice",
        "title": "关于公布第二批历史建筑的通知（黄政发〔2019〕6号，45处）",
        "org": "黄石市人民政府",
        "pub_date": "2019-01-30",
        "url": "http://www.huangshi.gov.cn/xxxgk/2020_zc/2020_gfxwj/202011/t20201109_727799.html",
        "authority": "A",
        "notes": "黄政发〔2019〕6号确定大冶市有色金属公司办公楼1等45处建筑为黄石市第二批历史建筑；附件doc已下载核读（本地存档 raw/huangshi_heritage2/）：大冶有色金属公司办公楼1-2（下陆大道0122号，2栋）、大冶铁矿厂矿山二路宿舍1-24（铁山区矿山二路，24栋）、源华煤矿办公楼（西塞山区东井煤矿下窑桐厂街）、油铺湾1号民居、向阳路22号住宅1-3、下陆火车站（老下陆街28号）、大冶铁矿厂光明里宿舍1-12（胜利路，12栋）、黄石市第一届市委办公楼旧址（黄棉村4-10号）。",
    },
}


RECORDS = [
    {
        "inventory_id": "HBI-HS-041",
        "name": "大冶铁矿厂矿山二路宿舍群（24栋）",
        "city": "黄石市",
        "district_county": "铁山区矿山二路",
        "industry_category_l1": "工业社区",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "黄石市第二批历史建筑（黄政发〔2019〕6号名录第3-26项，共24栋）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["huangshi_heritage_buildings_2019"],
        "cultural_evidence": {
            "material_carriers": "矿山二路1-33号（缺号连续编号）24栋职工宿舍（铁山区矿山二路）；栋型、结构与保存状态待现场测绘；与大冶铁矿厂矿山二路宿舍历史文化街区（湖北省历史文化街区）的空间关系待保护规划核对",
            "technical_memory": "大冶铁矿职工宿舍群的营建形制与矿区生活配套布局，代表矿冶企业成规模建设工人村的传统",
            "social_memory": "大冶铁矿几代矿工与家属的矿区生活记忆，矿山二路宿舍群是黄石矿冶工业社区活态样本",
            "current_use_or_loss": "以第二批历史建筑身份纳入保护体系；居住使用现状与修缮计划待核",
        },
        "notes": "直接取自黄政发〔2019〕6号附件名单（A级，doc核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["大冶铁矿厂矿山二路宿舍"],
        "asset_kind": "industrial_residential_landscape",
    },
    {
        "inventory_id": "HBI-HS-042",
        "name": "大冶铁矿厂光明里宿舍群（12栋）",
        "city": "黄石市",
        "district_county": "铁山区胜利路",
        "industry_category_l1": "工业社区",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "黄石市第二批历史建筑（黄政发〔2019〕6号名录第33-44项，共12栋）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["huangshi_heritage_buildings_2019"],
        "cultural_evidence": {
            "material_carriers": "胜利路9-20号连续12栋职工宿舍（光明里）；栋型、结构与保存状态待现场测绘",
            "technical_memory": "光明里宿舍群与矿山二路宿舍群同属大冶铁矿工人村体系，反映矿冶社区成片建设的规划布局",
            "social_memory": "光明里矿区家属区生活记忆",
            "current_use_or_loss": "以第二批历史建筑身份纳入保护体系；居住使用现状与修缮计划待核",
        },
        "notes": "直接取自黄政发〔2019〕6号附件名单（A级，doc核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["大冶铁矿厂光明里宿舍"],
        "asset_kind": "industrial_residential_landscape",
    },
    {
        "inventory_id": "HBI-HS-043",
        "name": "大冶有色金属公司办公楼（2栋）",
        "city": "黄石市",
        "district_county": "下陆区下陆大道",
        "industry_category_l1": "有色冶金工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "黄石市第二批历史建筑（黄政发〔2019〕6号名录第1-2项，共2栋）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["huangshi_heritage_buildings_2019"],
        "cultural_evidence": {
            "material_carriers": "大冶有色金属公司办公楼2栋（下陆大道0122号）；建造年代与结构待现场测绘",
            "technical_memory": "大冶有色作为全国重要铜冶炼企业的总部办公建筑，承载 company 治理与冶炼工业管理记忆",
            "social_memory": "大冶有色职工与下陆有色社区记忆",
            "current_use_or_loss": "以第二批历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自黄政发〔2019〕6号附件名单（A级，doc核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["大冶有色金属公司"],
        "asset_kind": "industrial_building",
    },
]


HS011_PATCH = {
    "source_keys_append": ["huangshi_heritage_buildings_2019"],
    "notes_append": "2019年黄石市第二批历史建筑名录（黄政发〔2019〕6号）第27项将源华煤矿办公楼（西塞山区东井煤矿下窑桐厂街）列为市级历史建筑，补充本条对象的市级历史建筑保护身份。",
}

HS019_PATCH = {
    "source_keys_append": ["huangshi_heritage_buildings_2019"],
    "notes_append": "2019年黄石市第二批历史建筑名录（黄政发〔2019〕6号）第32项将下陆火车站（老下陆街28号）列为市级历史建筑，补充市级历史建筑保护身份。",
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    added = 0
    for record in RECORDS:
        existing = next((row for row in records if row["inventory_id"] == record["inventory_id"]), None)
        if existing is not None:
            if existing != record:
                raise SystemExit(f"conflicting duplicate record: {record['inventory_id']}")
            continue
        if any(row["name"] == record["name"] for row in records):
            raise SystemExit(f"conflicting duplicate name: {record['name']}")
        records.append(record)
        added += 1
    for key, source in SOURCES.items():
        if key in sources and sources[key] != source:
            raise SystemExit(f"conflicting source: {key}")
    sources.update(SOURCES)
    updated = 0
    for record_id, patch in (("HBI-HS-011", HS011_PATCH), ("HBI-HS-019", HS019_PATCH)):
        record = next((row for row in records if row["inventory_id"] == record_id), None)
        if record is None:
            raise SystemExit(f"record not found: {record_id}")
        for key in patch["source_keys_append"]:
            if key not in record["source_keys"]:
                record["source_keys"].append(key)
                updated = 1
        if patch["notes_append"] not in record["notes"]:
            record["notes"] = record["notes"] + patch["notes_append"]
            updated = 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_bj_sources={len(SOURCES)} added_records={added} updated_records={updated} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
