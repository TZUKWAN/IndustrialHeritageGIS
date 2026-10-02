from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


RECORDS = [
    {
        "inventory_id": "HBI-XIANGYANG-042",
        "name": "原襄樊市第四织布厂厂房（1-5号）",
        "city": "襄阳市",
        "district_county": "襄城区襄阳古城街道内环路",
        "industry_category_l1": "织布与纺织工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "襄阳市第二批历史建筑（襄政发〔2024〕6号名录第102-106项；1990年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["xiangyang_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "织布厂厂房5栋（内环路32号）；织机遗存与结构待现场测绘",
            "technical_memory": "襄樊城区织布工业的准备、织造、整理工序脉络；90年代建厂属襄阳纺织工业晚期扩张批次",
            "social_memory": "四织布厂职工与古城内环路工业街区记忆",
            "current_use_or_loss": "以第二批历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自襄政发〔2024〕6号名录表第102-106项（图片附件视觉核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["原襄樊市第四织布厂"],
        "asset_kind": "industrial_building",
    },
    {
        "inventory_id": "HBI-XIANGYANG-043",
        "name": "原襄樊日报社印刷厂（1-5号）",
        "city": "襄阳市",
        "district_county": "襄城区襄阳古城街道东街",
        "industry_category_l1": "印刷工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "襄阳市第二批历史建筑（襄政发〔2024〕6号名录第107-111项；1949年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["xiangyang_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "报社印刷厂建筑5栋（东街67号）；印刷机具遗存与结构待现场测绘",
            "technical_memory": "1949年建厂的党报印刷体系，铅排—胶印技术演进的地方载体；与文字603厂同属襄阳印刷工业谱系",
            "social_memory": "襄樊日报出版印刷职工的新闻生产记忆",
            "current_use_or_loss": "以第二批历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自襄政发〔2024〕6号名录表第107-111项（图片附件视觉核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_building",
    },
    {
        "inventory_id": "HBI-XIANGYANG-044",
        "name": "原中国化学工程第六建设有限公司建筑群",
        "city": "襄阳市",
        "district_county": "襄城区真武山街道胜利街",
        "industry_category_l1": "化学工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "襄阳市第二批历史建筑（襄政发〔2024〕6号名录第112-114项；1969年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["xiangyang_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "化六建建筑3处（胜利街30号）；建筑功能（办公/后勤）与保存状态待现场测绘",
            "technical_memory": "中国化学工程第六建设有限公司1969年三线迁建襄阳，为全国化工建设行业重要力量——基建队伍基地建筑承载化工工程建设组织记忆",
            "social_memory": "化六建职工转战全国各地化工基地的建设者记忆",
            "current_use_or_loss": "以第二批历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自襄政发〔2024〕6号名录表第112-114项（图片附件视觉核读，名录标为公共建筑）；企业全称与沿革以企业志核验为准；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["化六建", "中国化学工程第六建设有限公司"],
        "asset_kind": "industrial_site",
    },
    {
        "inventory_id": "HBI-XIANGYANG-045",
        "name": "原卫东机械厂建筑群（供销社、文化宫、礼堂、职工食堂等）",
        "city": "襄阳市",
        "district_county": "襄城区檀溪街道环山路孙家冲",
        "industry_category_l1": "三线军工工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "襄阳市第二批历史建筑（襄政发〔2024〕6号名录第115-121项；1964年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["xiangyang_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "名录载明7处：供销社、文化宫、礼堂、职工食堂、大众饭店、理发店、电影放映楼（环山路孙家冲1号）；建筑保存状态待现场测绘",
            "technical_memory": "1964年三线建设早期迁建的军工机械厂厂前区生活服务建筑群形制；卫东机械厂企业全称与军品谱系待厂志核验",
            "social_memory": "三线军工职工完整厂区社会（购物、文娱、就餐、放映）记忆，是目前襄阳保存最完整的三线厂前区服务设施组群之一",
            "current_use_or_loss": "以第二批历史建筑身份纳入保护体系；现状用途与卫东化改造利用方向待核",
        },
        "notes": "直接取自襄政发〔2024〕6号名录表第115-121项（图片附件视觉核读，名录标为公共建筑）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["卫东机械厂", "卫东集团"],
        "asset_kind": "industrial_social_site",
    },
    {
        "inventory_id": "HBI-XIANGYANG-046",
        "name": "原青山机械厂建筑群（办公楼、化工库、发电机车间等）",
        "city": "襄阳市",
        "district_county": "襄城区环山路",
        "industry_category_l1": "三线军工工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "襄阳市第二批历史建筑（襄政发〔2024〕6号名录第122-127项；1969年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["xiangyang_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "名录载明6处：办公楼、化工库、文体活动中心、发电机车间、起动力车间、办公楼（环环路22号）；建筑保存状态待现场测绘",
            "technical_memory": "1969年三线军工机械厂的动力（发电机/起动力车间）、化工库与文体配套建筑组合，反映军工厂自备动力体系；青山机械厂企业代号与军品谱系待厂志核验",
            "social_memory": "青山厂三线建设者与家属区记忆",
            "current_use_or_loss": "以第二批历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自襄政发〔2024〕6号名录表第122-127项（图片附件视觉核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["青山机械厂"],
        "asset_kind": "industrial_site",
    },
    {
        "inventory_id": "HBI-XIANGYANG-047",
        "name": "汉丹电器厂建筑群（商店、食堂、机器加工车间等）",
        "city": "襄阳市",
        "district_county": "襄城区檀溪街道虎头山冲路",
        "industry_category_l1": "三线军工工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "襄阳市第二批历史建筑（襄政发〔2024〕6号名录第128-132项；1965年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["xiangyang_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "名录载明5处：商店、超市、食堂、洗澡房、机器加工车间（虎头山冲路1号）；建筑保存状态待现场测绘",
            "technical_memory": "1965年三线时期军工电器厂（汉丹机电厂谱系）的机加工车间与厂区生活服务设施组合；企业沿革待厂志核验",
            "social_memory": "汉丹厂三线职工厂区生活记忆",
            "current_use_or_loss": "以第二批历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自襄政发〔2024〕6号名录表第128-132项（图片附件视觉核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["汉丹电器厂", "汉丹厂"],
        "asset_kind": "industrial_site",
    },
    {
        "inventory_id": "HBI-XIANGYANG-048",
        "name": "襄阳市渡槽管理处建筑群（含渡槽管理处水塔）",
        "city": "襄阳市",
        "district_county": "襄州区石桥镇渠营村",
        "industry_category_l1": "水利工程与泵站",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "襄阳市第二批历史建筑（襄政发〔2024〕6号名录第142-148项；1973年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["xiangyang_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "名录载明渡槽管理处1-6号建筑及水塔（石桥镇渠营村）；与引丹灌渠/排子河渡槽水利体系的管理关系待核",
            "technical_memory": "1973年大型灌区渡槽管理体系的管理处驻地建筑组合与水塔供水设施",
            "social_memory": "引丹灌渠水利管理者驻渠运维的集体记忆",
            "current_use_or_loss": "以第二批历史建筑身份纳入保护体系；现状用途与所属灌区待核",
        },
        "notes": "直接取自襄政发〔2024〕6号名录表第142-148项（图片附件视觉核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_utility_site",
    },
]


PROV007_PATCH = {
    "notes_append": "2024年襄阳市第二批历史建筑名录（襄政发〔2024〕6号）第69-89项将原文字603厂4-29号共21栋建筑（真武山街道盛丰路6号，1969年建）列为市级历史建筑，与省级工业遗产、省级历史文化街区构成三重保护身份。",
}

XY034_PATCH = {
    "notes_append": "2024年襄阳市第二批历史建筑名录（襄政发〔2024〕6号）第90-101项将第六〇九研究所将军楼1-5号、三用堂、平房3-33/3-36栋、福寿养老院1-2号、综治小楼1-2号共12处建筑（隆中大道296号，1977年建）列为市级历史建筑。",
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
    updated = 0
    for record_id, patch in (("HBI-PROV-007", PROV007_PATCH), ("HBI-XIANGYANG-034", XY034_PATCH)):
        record = next((row for row in records if row["inventory_id"] == record_id), None)
        if record is None:
            raise SystemExit(f"record not found: {record_id}")
        if patch["notes_append"] not in record["notes"]:
            record["notes"] = record["notes"] + patch["notes_append"]
            updated = 1
        if "xiangyang_heritage_buildings_2024" not in record["source_keys"]:
            record["source_keys"].append("xiangyang_heritage_buildings_2024")
            updated = 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_be_added_records={added} updated_records={updated} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
