from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "shiyan_heritage_buildings_2024": {
        "source_type": "municipal_government_notice",
        "title": "市人民政府关于公布2024年度104处历史建筑名录的通知（十政发〔2024〕10号）",
        "org": "十堰市人民政府门户网站（郧西县政府网转载页）",
        "pub_date": "2024-08-01",
        "url": "http://www.yunxi.gov.cn/xxgk/fdzdgk/zdmsxx/jdzf/202412/t20241215_4658818.shtml",
        "authority": "A",
        "notes": "十政发〔2024〕10号确定嘉庆桥、胡家大院等104处建筑为十堰市历史建筑并附完整名录表：含大川镇麻纤厂旧址（11）、四四厂旧址（20，茅箭区二堰街道朝阳南路10号）、102三团土楼旧址（21）、工人文化宫（22）、五一厂电影院旧址（31）、十堰工厂羽毛球馆（33）、原十堰市第二砖瓦厂职工住房（45）、25厂原厂房（46）、二五厂半山公园（48）、技术中心办公楼（49）、京能东风大烟囱（53）、23厂退休办老办公楼（54）、23厂老办公楼（55）、马灯精神教育馆（56）、23厂工人俱乐部（57）、余河村老供销社仓库（71）、梨花村酒厂一号/二号车间与谷壳仓库（72-74）、冻青沟村老供销社（92）、原食用油加工厂1-4号车间/1-2号仓库/办公楼（94-100）、原云盖寺绿松石矿区工艺厂房/办公区/宿舍（101-103）、郧阳汉江公路大桥（104）。",
    },
}


RECORDS = [
    {
        "inventory_id": "HBI-SY-030",
        "name": "郧阳区原食用油加工厂建筑群",
        "city": "十堰市",
        "district_county": "郧阳区城关镇北门社区",
        "industry_category_l1": "传统油料加工",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "十堰市历史建筑（十政发〔2024〕10号2024年度名录第94-100项：原食用油加工厂1-4号车间、1-2号仓库、办公楼）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["shiyan_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "名录载明7处单体：1-4号车间、1号仓库、2号仓库、办公楼，均位于城关镇北门社区；单体建筑面积、结构与保存状态待现场测绘",
            "technical_memory": "县城食用油加工的车间、仓储与办公功能分区完整，代表计划经济时期县域粮油加工体系的工艺布局；加工设备与工艺档案待补",
            "social_memory": "郧阳县城粮油供应与职工生产记忆；厂区改制后沿革与职工口述待采集",
            "current_use_or_loss": "以2024年历史建筑身份纳入十堰市保护体系，市住房和城市更新局会同属地政府负责保护利用；现状用途与活化方向待核",
        },
        "notes": "直接取自十政发〔2024〕10号附件名录表（2024-12-15郧西县政府网转载页实读）；历史建筑保护不等于文物保护单位或工业遗产法定认定；建筑本体保存状况与产权待核；坐标未核验保持待核。",
        "aliases": ["郧县原食用油加工厂"],
        "asset_kind": "industrial_site",
    },
    {
        "inventory_id": "HBI-SY-031",
        "name": "梨花村酒厂老厂区建筑群（一号、二号车间及谷壳仓库）",
        "city": "十堰市",
        "district_county": "郧阳区大柳乡杨家村",
        "industry_category_l1": "酿酒工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "十堰市历史建筑（十政发〔2024〕10号2024年度名录第72-74项：梨花村酒厂一号车间、二号车间、谷壳仓库）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["shiyan_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "名录载明3处单体：一号车间、二号车间、谷壳仓库，均位于大柳乡杨家村二组378号；建筑面积与保存状态待现场测绘",
            "technical_memory": "白酒酿造车间与谷壳辅料仓储的功能组合，记录郧阳地方酿酒工业的原料处理与生产布局；酿造工艺与设备谱系待厂志补充",
            "social_memory": "梨花村酒为郧阳地方名酒，老厂区承载地方白酒产业与职工记忆；企业沿革与口述史待采集",
            "current_use_or_loss": "以2024年历史建筑身份纳入保护体系；老厂区现用途（停产/转产/活化）待核",
        },
        "notes": "直接取自十政发〔2024〕10号附件名录表；历史建筑保护不等于文物保护单位或工业遗产法定认定；与现梨花村酒业生产经营厂区的关系待核；坐标未核验保持待核。",
        "aliases": ["梨花村酒厂一号车间", "梨花村酒厂二号车间", "梨花村酒厂谷壳仓库"],
        "asset_kind": "industrial_site",
    },
    {
        "inventory_id": "HBI-SY-032",
        "name": "23厂老办公楼与工人俱乐部（含马灯精神教育馆）",
        "city": "十堰市",
        "district_county": "张湾区车城西路、大炉子沟",
        "industry_category_l1": "三线军工工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "十堰市历史建筑（十政发〔2024〕10号2024年度名录第54-57项：23厂退休办老办公楼、23厂老办公楼、马灯精神教育馆、23厂工人俱乐部）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["shiyan_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "名录载明4处单体：车城西路140号23厂老办公楼与退休办老办公楼，大炉子沟路5号马灯精神教育馆与23厂工人俱乐部；建筑年代与结构待现场测绘",
            "technical_memory": "三线建设时期专业厂办公与工人文化建筑的形制与建造工艺；23厂企业全称与产品谱系待档案核验",
            "social_memory": "二汽专业厂职工的办公、文娱与马灯精神传统——马灯精神教育馆延续三线建设者艰苦创业记忆",
            "current_use_or_loss": "以2024年历史建筑身份纳入保护体系；马灯精神教育馆已承担展教功能，其余建筑现状用途待核",
        },
        "notes": "直接取自十政发〔2024〕10号附件名录表；名录仅以代号“23厂”表述，企业全称与沿革待十堰厂志/档案核验后补注；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["23厂工人俱乐部", "马灯精神教育馆", "23厂老办公楼"],
        "asset_kind": "industrial_social_site",
    },
    {
        "inventory_id": "HBI-SY-033",
        "name": "25厂原厂房（含二五厂半山公园）",
        "city": "十堰市",
        "district_county": "张湾区东岳路",
        "industry_category_l1": "三线军工工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "十堰市历史建筑（十政发〔2024〕10号2024年度名录第46、48项：25厂原厂房、二五厂半山公园）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["shiyan_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "名录载明东岳路96号25厂原厂房与东岳路100号二五厂半山公园；厂房结构、规模与公园工业元素待现场测绘",
            "technical_memory": "三线时期专业厂房的空间形制；25厂企业全称与产品谱系待档案核验",
            "social_memory": "专业厂职工生产生活记忆；半山公园为厂区工业景观与职工休闲记忆的当代延续",
            "current_use_or_loss": "以2024年历史建筑身份纳入保护体系；厂房现用途与公园开放状态待核",
        },
        "notes": "直接取自十政发〔2024〕10号附件名录表；名录仅以代号“25厂”表述，企业全称待厂志核验；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["二五厂半山公园", "25厂原厂房"],
        "asset_kind": "industrial_site",
    },
    {
        "inventory_id": "HBI-SY-034",
        "name": "大川镇麻纤厂旧址",
        "city": "十堰市",
        "district_county": "茅箭区大川镇大川村",
        "industry_category_l1": "纺织工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "十堰市历史建筑（十政发〔2024〕10号2024年度名录第11项：大川镇麻纤厂旧址）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["shiyan_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "麻纤（麻纺织）生产厂旧址，位于大川镇大川村一组；建筑遗存范围与保存状态待现场测绘",
            "technical_memory": "县域麻纤维加工与纺织的原料工艺传统；设备与工艺档案待补",
            "social_memory": "山区乡镇社队/集体工业的生产者记忆；建厂与停产年代待地方志核验",
            "current_use_or_loss": "以2024年历史建筑身份纳入保护体系；现状用途与保存边界待核",
        },
        "notes": "直接取自十政发〔2024〕10号附件名录表；历史建筑保护不等于文物保护单位或工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_site",
    },
    {
        "inventory_id": "HBI-SY-035",
        "name": "原十堰市第二砖瓦厂职工住房",
        "city": "十堰市",
        "district_county": "张湾区西城路",
        "industry_category_l1": "建材工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "十堰市历史建筑（十政发〔2024〕10号2024年度名录第45项：原十堰市第二砖瓦厂职工住房）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["shiyan_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "原市第二砖瓦厂职工住房（西城路88号里）；栋数、形制与保存状态待现场测绘",
            "technical_memory": "砖瓦建材企业自建职工住房的建造形制，与砖瓦生产工业社区配套传统",
            "social_memory": "砖瓦厂职工与家属的居住社区记忆；企业沿革与职工口述待采集",
            "current_use_or_loss": "以2024年历史建筑身份纳入保护体系；居住使用现状与修缮计划待核",
        },
        "notes": "直接取自十政发〔2024〕10号附件名录表；历史建筑保护不等于文物保护单位或工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_residential_landscape",
    },
    {
        "inventory_id": "HBI-SY-036",
        "name": "京能东风大烟囱",
        "city": "十堰市",
        "district_county": "张湾区车城西路",
        "industry_category_l1": "火力发电",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "十堰市历史建筑（十政发〔2024〕10号2024年度名录第53项：京能东风大烟囱）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["shiyan_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "热电联产大烟囱（车城西路68号），十堰东风工业天际线标志性构筑物；高度、建造年代与结构待现场测绘",
            "technical_memory": "东风公司自备热电与集中供热系统的工程技术记忆；烟囱所属电厂沿革与设备档案待补",
            "social_memory": "“十里车城”供热供电与职工生活的共同记忆标志物",
            "current_use_or_loss": "以2024年历史建筑身份纳入保护体系；所属京能东风热电设施运行/退役状态与烟囱在用情况待核",
        },
        "notes": "直接取自十政发〔2024〕10号附件名录表；历史建筑保护不等于文物保护单位或工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["东风大烟囱"],
        "asset_kind": "industrial_utility_site",
    },
]


PROV005_PATCH = {
    "source_keys_append": ["shiyan_heritage_buildings_2024"],
    "material_carriers": "云盖寺矿山矿脉、采掘地貌、矿坑/巷道及矿山公园博物馆、文创中心和游客服务设施；2024年十堰市历史建筑名录（十政发〔2024〕10号）第101-103项载明矿区工艺厂房、办公区、宿舍三处建筑（鲍峡镇云盖寺村）；完整核心物项清单仍待申报材料复核",
    "notes": "湖北省第二批省级工业遗产（2025年度）与2024年十堰市历史建筑名录双身份对象；名录第101-103项为矿区建筑提供市级历史建筑保护身份。坐标未核验保持待核。",
}

SY007_PATCH = {
    "source_keys_append": ["shiyan_heritage_buildings_2024"],
    "notes_append": "2024年十堰市历史建筑名录（十政发〔2024〕10号）第20项“四四厂旧址”（茅箭区二堰街道朝阳南路10号）与本条44厂（二汽车厢厂，茅箭区）对象对应，提供市级历史建筑保护身份。",
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
    for record_id, patch in (("HBI-PROV-005", PROV005_PATCH), ("HBI-SY-007", SY007_PATCH)):
        record = next((row for row in records if row["inventory_id"] == record_id), None)
        if record is None:
            raise SystemExit(f"record not found: {record_id}")
        for key in patch["source_keys_append"]:
            if key not in record["source_keys"]:
                record["source_keys"].append(key)
                updated = 1
        if "material_carriers" in patch and record["cultural_evidence"]["material_carriers"] != patch["material_carriers"]:
            record["cultural_evidence"]["material_carriers"] = patch["material_carriers"]
            updated = 1
        if "notes" in patch and record["notes"] != patch["notes"]:
            record["notes"] = patch["notes"]
            updated = 1
        if "notes_append" in patch and patch["notes_append"] not in record["notes"]:
            record["notes"] = record["notes"] + patch["notes_append"]
            updated = 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_av_sources={len(SOURCES)} added_records={added} updated_records={updated} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
