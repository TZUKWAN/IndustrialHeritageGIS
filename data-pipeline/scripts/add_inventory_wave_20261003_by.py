from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


def _base(record_id: str, name: str, dc: str, cat: str, no: str, kind: str, material: str, tech: str, social: str, use: str, notes: str, aliases: list) -> dict:
    return {
        "inventory_id": record_id,
        "name": name,
        "city": "荆州市",
        "district_county": dc,
        "industry_category_l1": cat,
        "recognition_level": "municipal_historical_building",
        "recognition_status": f"荆州市中心城区历史建筑（2019年9月30日市政府公布100处名录第{no}项）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["jingzhou_heritage_buildings_2019"],
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


RECORDS = [
    _base("HBI-JZ-032", "吉祥花号", "沙市区", "棉花加工与棉产流通", "2",
        "industrial_trade_site",
        "花号（棉花贸易行）建筑本体，民国时期商埠店铺形制；门面与内部格局待现场测绘",
        "沙市开埠后棉花集散贸易的行栈经营形制，与沙市打包厂（HBI-JZ-004）构成棉花收购—打包—外运链条前端",
        "沙市花行帮商人与棉农售棉记忆，见证沙市江汉平原棉花集散中心地位",
        "以中心城区历史建筑身份纳入保护体系；现状用途待核",
        "直接取自2019年市政府100处名录（B级转载全文核读，通知主体为市政府）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["吉祥花号棉花行"],
    ),
    _base("HBI-JZ-033", "安利英行", "沙市区", "近代航运与民族工业", "3",
        "industrial_trade_site",
        "英行（外资/合资商行）建筑本体，民国商埠立面形制；结构与保存状态待现场测绘",
        "沙市开埠口岸的外商行栈贸易载体，与怡和洋行（HBI-JZ-026）同属近代口岸商贸谱系",
        "开埠口岸洋行贸易与本地买办商业记忆",
        "以中心城区历史建筑身份纳入保护体系；现状用途待核",
        "直接取自2019年市政府100处名录（B级转载全文核读）；名录未载建筑年代与门牌；坐标未核验保持待核。",
        ["安利英行沙市分行"],
    ),
    _base("HBI-JZ-034", "徐恒记粮行（纯正街44号民居）", "沙市区纯正街", "粮食仓储工业", "91",
        "industrial_trade_site",
        "粮行建筑（纯正街44号民居载体），前店后仓形制待现场测绘",
        "沙市粮食贸易行栈的收购、储存、转运经营形制，江汉平原稻米集散的商业节点",
        "徐恒记粮行商号与沙市米市记忆",
        "以中心城区历史建筑身份纳入保护体系；现状用途待核",
        "直接取自2019年市政府100处名录（B级转载全文核读，名录载“纯正街44号民居(徐恒记粮行)”）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["徐恒记粮行"],
    ),
    _base("HBI-JZ-035", "李义顺斋铺（胜利街109号民居）", "沙市区胜利街", "食品加工工业", "83",
        "industrial_trade_site",
        "斋铺建筑（胜利街109号民居载体），前店后坊形制待现场测绘",
        "沙市茶食糖果业的斋铺前店后坊生产销售形制",
        "李义顺斋铺商号与沙市老字号茶食记忆",
        "以中心城区历史建筑身份纳入保护体系；现状用途待核",
        "直接取自2019年市政府100处名录（B级转载全文核读，名录载“胜利街109号民居(李义顺斋铺)”）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["李义顺斋铺"],
    ),
    _base("HBI-JZ-036", "同善堂药铺", "沙市区", "医药商业", "93",
        "industrial_trade_site",
        "药铺建筑本体，堂柜式药店形制待现场测绘",
        "沙市中医药零售的堂铺经营形制与饮片炮制前台服务传统",
        "同善堂字号与沙市中医药商业记忆",
        "以中心城区历史建筑身份纳入保护体系；现状用途待核",
        "直接取自2019年市政府100处名录（B级转载全文核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    {
        "inventory_id": "HBI-JZ-037",
        "name": "沙市邮政局大楼",
        "city": "荆州市",
        "district_county": "沙市区",
        "industry_category_l1": "通信与城市基础设施",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "荆州市中心城区历史建筑（2019年9月30日市政府公布100处名录第94项）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["jingzhou_heritage_buildings_2019"],
        "cultural_evidence": {
            "material_carriers": "邮政局大楼建筑本体；层数、立面与营业厅格局待现场测绘",
            "technical_memory": "沙市近代邮政通信的营业枢纽建筑，与汉口电灯公司（HBI-WUHAN-003）、永耀电灯公司营业部（HBI-YC-021）、湖北省邮电管理局旧址（HBI-ES-023）同属湖北近现代通信基础设施谱系",
            "social_memory": "沙市市民寄信汇兑与邮政网点服务记忆",
            "current_use_or_loss": "以中心城区历史建筑身份纳入保护体系；现状用途待核",
        },
        "notes": "直接取自2019年市政府100处名录（B级转载全文核读）；名录未载建筑年代与门牌；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_utility_site",
    },
    _base("HBI-JZ-038", "老天宝", "沙市区", "金银加工与商贸", "95",
        "industrial_trade_site",
        "银楼（金银首饰号）建筑本体，门面招牌与柜面形制待现场测绘",
        "沙市银楼业的金银首饰加工与兑卖手艺传统",
        "老天宝字号为沙市著名银楼，婚嫁金银器消费的市民记忆",
        "以中心城区历史建筑身份纳入保护体系；现状用途待核",
        "直接取自2019年市政府100处名录（B级转载全文核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["老天宝银楼"],
    ),
    _base("HBI-JZ-039", "同震银楼", "沙市区", "金银加工与商贸", "96",
        "industrial_trade_site",
        "银楼建筑本体，门面与柜面形制待现场测绘",
        "沙市银楼业金银加工兑卖传统",
        "同震银楼字号与沙市金银商业记忆",
        "以中心城区历史建筑身份纳入保护体系；现状用途待核",
        "直接取自2019年市政府100处名录（B级转载全文核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["同震银楼"],
    ),
    _base("HBI-JZ-040", "好公道酒楼", "沙市区", "商贸服务与基层文化供应", "97",
        "industrial_trade_site",
        "酒楼建筑本体，楼层与门面形制待现场测绘",
        "沙市餐饮业的酒楼经营与鄂菜厨艺传统",
        "好公道字号为沙市餐饮名店，市民宴饮与商埠食俗记忆",
        "以中心城区历史建筑身份纳入保护体系；现状用途待核",
        "直接取自2019年市政府100处名录（B级转载全文核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    _base("HBI-JZ-041", "显容照相馆", "沙市区", "商贸服务与基层文化供应", "98",
        "industrial_trade_site",
        "照相馆建筑本体，门面与摄影棚格局待现场测绘",
        "早期照相术传入沙市后的商业摄影服务形制，玻璃底片与暗房工艺记忆",
        "显容字号与沙市市民照相留影的市井记忆",
        "以中心城区历史建筑身份纳入保护体系；现状用途待核",
        "直接取自2019年市政府100处名录（B级转载全文核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    {
        "inventory_id": "HBI-XG-017",
        "name": "安陆粮机记忆馆与粮机文化片区（北正社区）",
        "city": "孝感市",
        "district_county": "安陆市府城街道北正社区",
        "industry_category_l1": "机械制造工业",
        "recognition_level": "city_update",
        "recognition_status": "原东方红粮机厂生活区（粮机片区，27栋996户）老旧小区改造中的工业记忆活化载体（“粮机记忆馆”、粮机文化墙在建）；未见法定遗产认定",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["anlu_loji_renov_2021", "hbdfh_official_site", "hubei_daily_tangxian_grain_2025"],
        "cultural_evidence": {
            "material_carriers": "粮机片区老旧小区（27栋、996户、3000余名居民，原东方红粮机厂职工及子女居住区）、粮机文化墙、文化长廊与“四状元里”牌坊（2022年改造），“粮机记忆馆”建设中",
            "technical_memory": "东方红粮机厂（1966年上海粮机厂内迁，巅峰年产2925台粮机、市占75%）的制造技艺与厂区生活配套体系记忆；生产主体延续为东方红集团（现址经济开发区粮机北路1号）",
            "social_memory": "粮机厂三代职工与家属的社区生活记忆；社区党委牵头成立粮机历史文化小组开展记忆征集",
            "current_use_or_loss": "老旧小区改造与粮机记忆馆建设并行，为安陆“中国粮油机械之都”工业记忆活化的社区样本；与 XG-013（粮食加工与轧花设施档案线索）为两组对象",
        },
        "notes": "依据安陆市政府网2021年改造报道（A）、湖北日报客户端粮机记忆馆报道（B，第78轮已核读补入XG-013 notes）与东方红集团官网（C）议定独立入库为社区活化载体（参照建始老电厂模式）；不推断法定认定；坐标未核验保持待核。",
        "aliases": ["粮机片区", "粮机记忆馆"],
        "asset_kind": "industrial_social_site",
    },
]


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
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
    print(f"wave_by_added_records={added} total_records={len(records)} total_sources={len(data.get('sources', {}))}")


if __name__ == "__main__":
    main()
