from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "xiangyang_heritage_buildings_2024": {
        "source_type": "municipal_government_notice",
        "title": "市人民政府关于公布襄阳市第二批历史建筑名录的通知（襄政发〔2024〕6号，154处）",
        "org": "襄阳市人民政府门户网站（政府信息公开平台）",
        "pub_date": "2024-09-03",
        "url": "http://www.xiangyang.gov.cn/szf/zfxxgk/zc/gfxwj/xzf/202409/t20240904_3668248.shtml",
        "authority": "A",
        "notes": "襄政发〔2024〕6号将陈老巷5号等154处建筑公布为襄阳市第二批历史建筑（2024-09-02），名录表以10张图片附件嵌入（已全部下载并逐张视觉核读，本地存档 raw/xiangyang_heritage/）。工业建筑类对象集中于樊城区与襄城区：原襄阳卷烟厂（27）、原襄樊车桥股份有限公司1号（28）、原襄樊市第一针织厂4号/2号（29-30）、原襄樊市五一棉纺厂棉花仓库（31）、原襄樊橡胶厂1-5号（32-36）、原襄樊内燃机车厂1-2号（39-40）、原襄阳轴承厂1-5号分厂（64-68）、原文字603厂4-29号（69-89共21栋）、原襄樊市第四织布厂1-5号（102-106）、原襄樊日报社印刷厂1-5号（107-111）；另含原中国化学工程第六建设有限公司（112-114）、原卫东机械厂（115-121）、原青山机械厂（122-127）、汉丹电器厂（128-132）等三线军工建筑（名录标为公共建筑）与襄阳市渡槽管理处1-6号及水塔（142-148）。",
    },
}


RECORDS = [
    {
        "inventory_id": "HBI-XIANGYANG-035",
        "name": "原襄阳卷烟厂厂房",
        "city": "襄阳市",
        "district_county": "樊城区米公街道大庆西路",
        "industry_category_l1": "烟草加工工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "襄阳市第二批历史建筑（襄政发〔2024〕6号名录第27项；2008年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["xiangyang_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "卷烟工业厂房（大庆西路55号）；建筑面积与结构待现场测绘",
            "technical_memory": "襄阳卷烟工业的制丝、卷制、包装生产脉络；停产年代与设备谱系待厂志核验",
            "social_memory": "卷烟厂职工与樊城工业街区记忆",
            "current_use_or_loss": "以第二批历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自襄政发〔2024〕6号名录表第27项（图片附件视觉核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_building",
    },
    {
        "inventory_id": "HBI-XIANGYANG-036",
        "name": "原襄樊车桥股份有限公司厂房",
        "city": "襄阳市",
        "district_county": "樊城区米公街道解放路",
        "industry_category_l1": "汽车零部件工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "襄阳市第二批历史建筑（襄政发〔2024〕6号名录第28项；1977年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["xiangyang_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "车桥制造厂房1号（解放路1号）；结构与保存状态待现场测绘",
            "technical_memory": "襄樊车桥作为汽车车桥专业制造企业的锻压、机加工工艺脉络；企业沿革待厂志核验",
            "social_memory": "车桥厂职工与襄阳汽车零部件工业记忆",
            "current_use_or_loss": "以第二批历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自襄政发〔2024〕6号名录表第28项（图片附件视觉核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_building",
    },
    {
        "inventory_id": "HBI-XIANGYANG-037",
        "name": "原襄樊市第一针织厂厂房（2号、4号）",
        "city": "襄阳市",
        "district_county": "樊城区汉江街道建设路",
        "industry_category_l1": "针织与纺织工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "襄阳市第二批历史建筑（襄政发〔2024〕6号名录第29-30项；1958年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["xiangyang_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "针织生产厂房2栋（建设路21号）；栋内结构与设备留存待现场测绘",
            "technical_memory": "1958年建厂的襄樊针织工业织造、染整工艺脉络",
            "social_memory": "一针织职工与樊城轻纺工业街区记忆",
            "current_use_or_loss": "以第二批历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自襄政发〔2024〕6号名录表第29-30项（图片附件视觉核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["原襄樊市第一针织厂"],
        "asset_kind": "industrial_building",
    },
    {
        "inventory_id": "HBI-XIANGYANG-038",
        "name": "原襄樊市五一棉纺厂棉花仓库",
        "city": "襄阳市",
        "district_county": "樊城区王寨街道月路",
        "industry_category_l1": "棉花加工与棉产流通",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "襄阳市第二批历史建筑（襄政发〔2024〕6号名录第31项；1979年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["xiangyang_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "棉花仓库（月路5-6号）；仓容、结构与保存状态待现场测绘",
            "technical_memory": "棉纺企业原棉仓储的堆垛、防潮、消防工艺传统",
            "social_memory": "五一棉纺厂职工与原棉供应链记忆",
            "current_use_or_loss": "以第二批历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自襄政发〔2024〕6号名录表第31项（图片附件视觉核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_storage_site",
    },
    {
        "inventory_id": "HBI-XIANGYANG-039",
        "name": "原襄樊橡胶厂建筑群（1-5号）",
        "city": "襄阳市",
        "district_county": "樊城区王寨街道汉江路",
        "industry_category_l1": "橡胶工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "襄阳市第二批历史建筑（襄政发〔2024〕6号名录第32-36项；1978年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["xiangyang_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "橡胶厂建筑5栋（汉江路60号）；各栋原功能（炼胶/成型/硫化等）与保存状态待现场测绘",
            "technical_memory": "襄樊橡胶工业的炼胶、成型、硫化生产工艺脉络",
            "social_memory": "橡胶厂职工社区与樊城工业记忆",
            "current_use_or_loss": "以第二批历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自襄政发〔2024〕6号名录表第32-36项（图片附件视觉核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["原襄樊橡胶厂"],
        "asset_kind": "industrial_building",
    },
    {
        "inventory_id": "HBI-XIANGYANG-040",
        "name": "原襄樊内燃机车厂厂房（1-2号）",
        "city": "襄阳市",
        "district_county": "襄州区肖湾街道钢铁路",
        "industry_category_l1": "铁路运输与机车检修工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "襄阳市第二批历史建筑（襄政发〔2024〕6号名录第39-40项；1969年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["xiangyang_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "内燃机车厂厂房2栋（钢铁路8号）；跨度、吊车与机床遗存待现场测绘",
            "technical_memory": "1969年三线时期内燃机车检修/制造企业的装配工艺脉络；企业沿革（与襄樊内燃机车厂、东风铁路运输的关系）待厂志核验",
            "social_memory": "机车厂职工与襄阳铁路工业记忆",
            "current_use_or_loss": "以第二批历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自襄政发〔2024〕6号名录表第39-40项（图片附件视觉核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["原襄樊内燃机车厂"],
        "asset_kind": "industrial_building",
    },
    {
        "inventory_id": "HBI-XIANGYANG-041",
        "name": "原襄阳轴承厂建筑群（锻工、机修、磨工分厂）",
        "city": "襄阳市",
        "district_county": "襄城区檀溪街道轴承一路",
        "industry_category_l1": "机械制造工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "襄阳市第二批历史建筑（襄政发〔2024〕6号名录第64-68项；1968年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["xiangyang_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "名录载明5处分厂建筑：1号锻工分厂、2号机修分厂、3号磨一分厂、4号磨二分厂、5号磨三分厂（轴承一路222号）；各分厂设备遗存与结构待现场测绘",
            "technical_memory": "襄阳轴承厂的锻造、机修与磨工（磨削）工艺分厂体系，反映轴承制造从锻坯到精磨的完整工序布局",
            "social_memory": "襄轴职工与轴承一路厂区生活记忆；襄轴曾为全国重要轴承基地",
            "current_use_or_loss": "以第二批历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自襄政发〔2024〕6号名录表第64-68项（图片附件视觉核读）；名录按分厂功能标注建筑名称；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["原襄阳轴承厂", "襄轴"],
        "asset_kind": "industrial_building",
    },
]


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
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_bd_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
