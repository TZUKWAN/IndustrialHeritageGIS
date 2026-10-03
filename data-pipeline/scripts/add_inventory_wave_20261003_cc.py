from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "hanchuan_wenbao_2025": {
        "source_type": "county_cultural_relic_publicity",
        "title": "关于汉川市蔡家嘴遗址等64处县级文物保护单位保护范围和建设控制地带（草案）的公示（附件docx已下载解析）",
        "org": "汉川市文化和旅游局（汉川市人民政府网）",
        "pub_date": "2025-08-19",
        "url": "http://www.hanchuan.gov.cn/tzgg/2058698.jhtml",
        "authority": "A",
        "notes": "64处县级文物保护单位公示名单（附件 /u/cms/hanchuan/202508/21172104a1o5.docx 已解析）中工业/水利相关4处：No.58江汉码头护坡堤（脉旺镇脉北村汉江边，有四至坐标）、No.61永丰北闸（刘家隔镇逼架台村）、No.62南河渡（南河乡南河村）、No.56潘同春酱园（马口镇老正街，前店后厂手工业酱园）；另有杨集桥、马城桥等桥梁。",
    },
    "shishou_heritage_batch2_2024": {
        "source_type": "county_city_government_notice",
        "title": "石首市人民政府关于公布我市历史建筑的通知（石政函〔2024〕12号，21处37栋）及名录扫描件",
        "org": "石首市人民政府门户网站（政府信息公开平台）",
        "pub_date": "2024-07-05",
        "url": "http://zwgk.shishou.gov.cn/sszjj/22318/107220243/t117220243074/508376.shtml",
        "authority": "A",
        "notes": "石政函〔2024〕12号（依鄂建〔2024〕423号“百日行动”）公布21处37栋，公示2024-06-26（http://zwgk.shishou.gov.cn/sszjj/22318/106220243/t126220243064/501959.shtml），名录扫描件已OCR核对：新厂粮库（6栋）、焦山河粮库（6栋）、梅田湖粮库（2栋）、天鹅洲新码头粮库（3栋）、梅田湖供销社、石首县委办公楼、三户街礼堂、物资局仓库、调关镇影剧院、过脉岭窑厂（2栋）、新厂弹药堡、石首师范学校（3栋）、思源亭、江波古居、新风水塔、新厂供销社水塔、江波渡老水塔、高基庙老水厂塔、六虎山泵站等。",
    },
}


def _hc(record_id: str, name: str, dc: str, cat: str, kind: str, material: str, tech: str, social: str, use: str, notes: str, aliases: list) -> dict:
    return {
        "inventory_id": record_id,
        "name": name,
        "city": "孝感市",
        "district_county": dc,
        "industry_category_l1": cat,
        "recognition_level": "county_relic_related",
        "recognition_status": "汉川市县级文物保护单位（2025年8月19日市文旅局64处县级文保单位保护范围和建设控制地带公示名单内）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["hanchuan_wenbao_2025"],
        "cultural_evidence": {
            "material_carriers": material,
            "technical_memory": tech,
            "social_memory": social,
            "current_use_or_loss": use,
        },
        "notes": notes,
        "aliases": aliases,
        "asset_kind": kind,
    }


HC_RECORDS = [
    _hc("HBI-XG-018", "江汉码头护坡堤", "汉川市脉旺镇脉北村汉江边", "港口与水运工业",
        "industrial_transport_site",
        "汉江码头护坡堤（脉北村汉江边，公示载有四至坐标）；堤身砌筑工艺与长度待现场测绘",
        "汉江中游航运码头的护坡堤水工构筑物，条石/混凝土护坡的岸线稳定工艺",
        "脉旺码头水运集散与装卸搬运行业记忆（脉旺为汉川汉江沿线老码头集镇）",
        "以县级文物保护单位身份纳入保护体系（保护范围与建控地带公示中）；使用状态待水利与交通部门核",
        "直接取自汉川市文旅局64处县级文保公示附件docx（A级，已解析）；文保认定不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    _hc("HBI-XG-019", "永丰北闸", "汉川市刘家隔镇逼架台村", "水利工程与泵站",
        "industrial_utility_site",
        "北闸水闸建筑本体（闸室、启闭设施）；闸孔规模与结构待现场测绘",
        "汈汊湖水系排灌闸站的水闸启闭与调度工艺",
        "刘家隔镇排涝保丰收与闸站值守记忆",
        "以县级文物保护单位身份纳入保护体系；在用状态待水利部门核",
        "直接取自汉川市文旅局64处县级文保公示附件docx（A级，已解析）；文保认定不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    _hc("HBI-XG-020", "南河渡", "汉川市南河乡南河村", "内河交通与货运服务",
        "industrial_transport_site",
        "南河渡渡口设施（渡口码头、缆桩或趸船遗迹）；渡运规模与现存设施待现场测绘",
        "内河渡运的摆渡工艺与渡口管理传统，汈汊湖水网乡村渡运节点",
        "南河乡两岸居民过渡与物资渡运的世代记忆",
        "以县级文物保护单位身份纳入保护体系；渡运是否延续待核",
        "直接取自汉川市文旅局64处县级文保公示附件docx（A级，已解析）；文保认定不等于工业遗产法定认定；坐标未核验保持待核。",
        ["南河渡口"],
    ),
    _hc("HBI-XG-021", "潘同春酱园（马口镇老正街）", "汉川市马口镇老正街", "食品加工工业",
        "industrial_building",
        "酱园前店后厂建筑（老正街），店堂、晒酱场与酱缸陈设待现场测绘",
        "马口镇酱园前店后厂的手工酿制工艺（黄豆酱、酱腌菜晒制发酵），老正街商号经营传统",
        "潘同春字号与马口镇商埠酱园消费记忆",
        "以县级文物保护单位身份纳入保护体系；经营延续与建筑保存待核",
        "直接取自汉川市文旅局64处县级文保公示附件docx（A级，已解析）；文保认定不等于工业遗产法定认定；坐标未核验保持待核。",
        ["潘同春酱园"],
    ),
]


SHISHOU_BATCH2 = [
    {
        "inventory_id": "HBI-JZ-062",
        "name": "物资局仓库",
        "city": "荆州市",
        "district_county": "石首市（地址待核）",
        "industry_category_l1": "工业仓储与运输",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "石首市历史建筑（石政函〔2024〕12号名录，物资局仓库）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["shishou_heritage_batch2_2024"],
        "cultural_evidence": {
            "material_carriers": "物资局仓库建筑本体（物资管理系统仓储设施）；仓型与保存状态待现场测绘",
            "technical_memory": "计划经济物资管理局的统配仓储体系",
            "social_memory": "物资局职工与县域物资调配记忆",
            "current_use_or_loss": "以市级历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自石政函〔2024〕12号名录扫描件（A级，OCR核对，第80轮已下载存档）；名录未载地址与年代；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_storage_site",
    },
    {
        "inventory_id": "HBI-JZ-063",
        "name": "过脉岭窑厂旧址（2栋）",
        "city": "荆州市",
        "district_county": "石首市过脉岭",
        "industry_category_l1": "建材工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "石首市历史建筑（石政函〔2024〕12号名录，过脉岭窑厂2栋）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["shishou_heritage_batch2_2024"],
        "cultural_evidence": {
            "material_carriers": "窑厂建筑2栋（窑体与厂房）；窑型（土窑/轮窑）与保存状态待现场测绘",
            "technical_memory": "砖瓦窑烧制工艺（制坯、晾坯、装窑、点火、出砖）",
            "social_memory": "窑厂工人与乡村建材生产记忆",
            "current_use_or_loss": "以市级历史建筑身份纳入保护体系；停产年代与现状待核",
        },
        "notes": "直接取自石政函〔2024〕12号名录扫描件（A级，OCR核对）；名录未载年代与地址明细；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["过脉岭窑厂"],
        "asset_kind": "industrial_building",
    },
    {
        "inventory_id": "HBI-JZ-064",
        "name": "调关镇影剧院",
        "city": "荆州市",
        "district_county": "石首市调关镇",
        "industry_category_l1": "工业社区文化",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "石首市历史建筑（石政函〔2024〕12号名录，调关镇影剧院）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["shishou_heritage_batch2_2024"],
        "cultural_evidence": {
            "material_carriers": "影剧院建筑本体（观众厅、舞台、放映室）；座位规模与保存状态待现场测绘",
            "technical_memory": "乡镇影剧院的放映与演出功能空间形制",
            "social_memory": "调关镇居民观影看戏的文娱记忆（与 HBI-JZ-045/046/047 同镇工业社区配套）",
            "current_use_or_loss": "以市级历史建筑身份纳入保护体系；现状用途（停演/改造）待核",
        },
        "notes": "直接取自石政函〔2024〕12号名录扫描件（A级，OCR核对）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_social_site",
    },
    {
        "inventory_id": "HBI-JZ-065",
        "name": "三户街礼堂",
        "city": "荆州市",
        "district_county": "石首市（三户街，具体乡镇待核）",
        "industry_category_l1": "工业社区",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "石首市历史建筑（石政函〔2024〕12号名录，三户街礼堂）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["shishou_heritage_batch2_2024"],
        "cultural_evidence": {
            "material_carriers": "礼堂建筑本体；规模与保存状态待现场测绘",
            "technical_memory": "乡镇礼堂的集会、演出与放映功能空间形制",
            "social_memory": "三户街集体集会与文娱记忆",
            "current_use_or_loss": "以市级历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自石政函〔2024〕12号名录扫描件（A级，OCR核对）；与卫星/拦河坝/团山寺大礼堂同为礼堂类记录模式；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_social_site",
    },
    {
        "inventory_id": "HBI-JZ-066",
        "name": "新厂弹药堡",
        "city": "荆州市",
        "district_county": "石首市新厂镇",
        "industry_category_l1": "军工修配工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "石首市历史建筑（石政函〔2024〕12号名录，新厂弹药堡）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["shishou_heritage_batch2_2024"],
        "cultural_evidence": {
            "material_carriers": "弹药堡防御/仓储构筑物（新厂镇）；堡体结构、厚度与射孔/门洞形制待现场测绘",
            "technical_memory": "弹药堡为军事防御或战备仓储构筑物，厚墙防御性构造工艺；建造背景（抗战/三线战备）待档案核验",
            "social_memory": "新厂镇战备与地方防卫记忆",
            "current_use_or_loss": "以市级历史建筑身份纳入保护体系；保存状况与原功能考证待核",
        },
        "notes": "直接取自石政函〔2024〕12号名录扫描件（A级，OCR核对）；名录仅载名称，建造背景待档案核验；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_storage_site",
    },
]


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    for key, source in SOURCES.items():
        if key in sources and sources[key] != source:
            raise SystemExit(f"conflicting source: {key}")
    sources.update(SOURCES)
    added = 0
    for record in HC_RECORDS + SHISHOU_BATCH2:
        existing = next((row for row in records if row["inventory_id"] == record["inventory_id"]), None)
        if existing is not None:
            if existing != record:
                raise SystemExit(f"conflicting duplicate record: {record['inventory_id']}")
            continue
        if any(row["name"] == record["name"] for row in records):
            raise SystemExit(f"conflicting duplicate name: {record['name']}")
        records.append(record)
        added += 1
    jz049 = next((row for row in records if row["inventory_id"] == "HBI-JZ-049"), None)
    if jz049 is None:
        raise SystemExit("record not found: HBI-JZ-049")
    note_add = "石政函〔2024〕12号名录另列“天鹅洲新码头粮库（3栋）”，与本条（1972年3圆顶仓+1平房仓）的批次重叠关系待核，暂视为同一对象不重复设条。"
    if note_add not in jz049["notes"]:
        jz049["notes"] = jz049["notes"] + note_add
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_cc_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
