from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


RECORDS = [
    {
        "inventory_id": "HBI-SY-037",
        "name": "五一厂电影院旧址与十堰工厂羽毛球馆",
        "city": "十堰市",
        "district_county": "茅箭区东城开发区",
        "industry_category_l1": "三线军工工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "十堰市历史建筑（十政发〔2024〕10号2024年度名录第31、33项：五一厂电影院旧址、十堰工厂羽毛球馆，均位于东风大道黑龙江路9号）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["shiyan_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "名录载明东风大道黑龙江路9号两处单体：五一厂电影院旧址与十堰工厂羽毛球馆（同址）；建筑年代、结构与保存状态待现场测绘",
            "technical_memory": "三线时期专业厂文化设施（电影院）与体育设施（羽毛球馆）的建筑形制，反映厂区文教体配套建设传统；五一厂企业全称待厂志核验",
            "social_memory": "专业厂职工观影、文体活动的集体记忆；电影院与球馆是几代东风人厂区生活记忆载体",
            "current_use_or_loss": "以2024年历史建筑身份纳入保护体系；电影院停用/活化状态与球馆在用情况待核",
        },
        "notes": "直接取自十政发〔2024〕10号附件名录表（郧西县政府网转载页实读）；名录以代号表述，企业全称待档案核验；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["五一厂电影院旧址", "十堰工厂羽毛球馆"],
        "asset_kind": "industrial_social_site",
    },
    {
        "inventory_id": "HBI-SY-038",
        "name": "“102”三团土楼旧址",
        "city": "十堰市",
        "district_county": "茅箭区二堰街道",
        "industry_category_l1": "三线建设兵工建制遗存",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "十堰市历史建筑（十政发〔2024〕10号2024年度名录第21项：102三团土楼旧址，二堰街道北京南路5号）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["shiyan_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "土楼形制旧址一处（北京南路5号）；建筑规模、结构与保存状态待现场测绘",
            "technical_memory": "“102三团”为三线建设时期施工建制代号，土楼为建设者集体的居建结合构筑物；建制沿革与建造工艺待档案核验",
            "social_memory": "三线建设者（施工部队/民兵团）集体劳动与居住记忆",
            "current_use_or_loss": "以2024年历史建筑身份纳入保护体系；现状用途与保存边界待核",
        },
        "notes": "直接取自十政发〔2024〕10号附件名录表；“102三团”建制性质（施工部队/民兵师）未见于名录，待三线建设档案核验后补注；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_site",
    },
    {
        "inventory_id": "HBI-SY-039",
        "name": "茅箭工人文化宫",
        "city": "十堰市",
        "district_county": "茅箭区五堰街道",
        "industry_category_l1": "工业社区文化",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "十堰市历史建筑（十政发〔2024〕10号2024年度名录第22项：工人文化宫，五堰街道公园路2号）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["shiyan_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "工人文化宫建筑本体（公园路2号）；建筑面积、建造年代与结构待现场测绘",
            "technical_memory": "计划经济时期城市工人文化宫的建筑形制与功能布局",
            "social_memory": "车城工人文艺、集会与职工业余教育的公共记忆空间",
            "current_use_or_loss": "以2024年历史建筑身份纳入保护体系；现用途（文化活动/商业改造）待核",
        },
        "notes": "直接取自十政发〔2024〕10号附件名录表；与荆门工人文化宫旧址（HBI-JM-012）同为鄂西北工人文化设施遗存；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["十堰工人文化宫"],
        "asset_kind": "industrial_social_site",
    },
    {
        "inventory_id": "HBI-SY-040",
        "name": "东风技术中心办公楼（车城西路）",
        "city": "十堰市",
        "district_county": "张湾区",
        "industry_category_l1": "汽车工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "十堰市历史建筑（十政发〔2024〕10号2024年度名录第49项：技术中心办公楼，车城西路4号）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["shiyan_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "技术中心办公楼（车城西路4号）；建造年代、层数与结构待现场测绘",
            "technical_memory": "二汽/东风汽车研发技术中心办公建筑，承载汽车工业自主研发体系的空间载体；沿革与使用单位谱系待厂志核验",
            "social_memory": "东风技术人员研发攻关的集体记忆",
            "current_use_or_loss": "以2024年历史建筑身份纳入保护体系；在用/迁空状态待核",
        },
        "notes": "直接取自十政发〔2024〕10号附件名录表；名录仅载“技术中心办公楼”，与东风公司技术中心体系的对应关系待核；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_building",
    },
    {
        "inventory_id": "HBI-SY-041",
        "name": "余河村老供销社仓库",
        "city": "十堰市",
        "district_county": "郧阳区沧浪山国家森林公园管理局余河村",
        "industry_category_l1": "供销商贸与基层物资供应",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "十堰市历史建筑（十政发〔2024〕10号2024年度名录第71项：余河村老供销社仓库，余河村二组16号）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["shiyan_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "村级供销社仓库建筑（余河村二组16号）；面积、形制与保存状态待现场测绘",
            "technical_memory": "农村供销合作社体系的仓储建筑形制与物资流通功能",
            "social_memory": "计划经济时期山区村组统购统销与生产生活资料供应的集体记忆",
            "current_use_or_loss": "以2024年历史建筑身份纳入保护体系；停用/再利用状态待核",
        },
        "notes": "直接取自十政发〔2024〕10号附件名录表；与天门供销社系列（HBI-TM-011/016/017/018）同为基层商贸遗存记录模式；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_storage_site",
    },
    {
        "inventory_id": "HBI-SY-042",
        "name": "冻青沟村老供销社",
        "city": "十堰市",
        "district_county": "郧阳区胡家营镇冻青沟村",
        "industry_category_l1": "供销商贸与基层物资供应",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "十堰市历史建筑（十政发〔2024〕10号2024年度名录第92项：冻青沟村老供销社，胡家营镇冻青沟村）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["shiyan_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "村级供销社建筑本体（胡家营镇冻青沟村）；形制与保存状态待现场测绘",
            "technical_memory": "汉江山区村级供销网点建筑形制；与冻青沟村传统民居群（名录第70项何家庄老屋同村）构成村落历史风貌",
            "social_memory": "山区村组商品流通与日常生活记忆",
            "current_use_or_loss": "以2024年历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自十政发〔2024〕10号附件名录表；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_trade_site",
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
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_aw_added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
