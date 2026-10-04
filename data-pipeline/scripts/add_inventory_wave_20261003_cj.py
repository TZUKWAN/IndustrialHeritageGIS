from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "wufeng_wenbao_2023": {
        "source_type": "county_cultural_relic_publicity",
        "title": "五峰土家族自治县文物保护单位名录（98处：省12+市14+县72）",
        "org": "五峰土家族自治县文化和旅游局（县政府网）",
        "pub_date": "2023-12-13",
        "url": "http://www.hbwf.gov.cn/zfxxgk/show.html?aid=14&id=64291",
        "authority": "A",
        "notes": "文保名录载明工业相关对象：万里茶道五峰段（省保第七批2019年，含五峰精制茶厂——渔洋关镇钟岭路3号）、石良司（五峰）茶叶机械厂（市保第六批2018年，1957年，五峰镇石良司村）、清水湾龙窑（市保，清，渔洋关镇）、古式水动力压面厂（县保，1950年，牛庄乡金山村洞湾）、柴埠溪电站（县保，1960年，渔洋关镇曹家坪）、大房坪幸福渠渡槽（县保，1965年）、钟岭长途汽车站（县保，1962年）、大面人民公社办公楼旧址（市保，1970年，湾潭镇）、渔洋关桥河跃进桥（1957年）、后槽骡马店（清，采花乡）、茶马古道（市保）等。",
    },
    "xingshan_chuanhan_rail_2014": {
        "source_type": "county_cultural_relic_publicity",
        "title": "兴山县文物保护单位名录（川汉铁路桥墩为省保第六批，1909-1911年）",
        "org": "兴山县文化和旅游局（兴山县人民政府网）",
        "pub_date": "2025-02-26",
        "url": "http://www.xingshan.gov.cn/zfxxgk/show.html?aid=15&id=61030",
        "authority": "A",
        "notes": "兴山县文保名录载明：兴山川汉铁路桥墩（省级文物保护单位，第六批2014年，1909-1911年）位于水月寺镇，5处子项——三拱桥、白石子湾口铁路桥墩、青树包铁路桥墩、学堂坪铁路桥、斑鸠窝铁路桥墩；川汉铁路为詹天佑主持设计的中国早期铁路干线（宜万铁路前身），多为川汉铁路废线上遗存。另市保含兴山县林业科学研究所早期建筑；第八批省保新闻（xingshan.gov.cn/content-18-48058-1.html）载全县381处文保。",
    },
}


def _yc(record_id: str, name: str, dc: str, cat: str, level: str, status: str, kind: str, year: str, material: str, tech: str, social: str, use: str, notes: str, aliases: list, src: list) -> dict:
    return {
        "inventory_id": record_id,
        "name": name,
        "city": "宜昌市",
        "district_county": dc,
        "industry_category_l1": cat,
        "recognition_level": level,
        "recognition_status": status,
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": src,
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
    _yc("HBI-YC-043", "五峰精制茶厂（万里茶道五峰段）", "五峰土家族自治县渔洋关镇钟岭路3号", "茶叶加工工业",
        "provincial_relic_related", "万里茶道五峰段组成部分（省级文物保护单位，第七批2019年）；五峰精制茶厂位于渔洋关镇钟岭路3号",
        "industrial_building", "待核",
        "五峰精制茶厂厂房（钟岭路3号），万里茶道五峰段茶厂遗存；生产线与仓储留存待现场测绘",
        "宜红茶制备与万里茶道南线茶叶集散加工的枢纽厂区工艺",
        "渔洋关茶商与茶厂职工记忆，宜红茶外销史节点",
        "以省保（万里茶道五峰段）身份纳入保护体系；厂区活化利用方向待核",
        "直接取自五峰县文旅局文保名录（A级）；与底册宜都红茶厂（HBI-PROV-002）、宜都候船室（HBI-ES-037）构成宜红茶生产—集散—外运谱系；坐标未核验保持待核。",
        ["五峰精制茶厂"],
        ["wufeng_wenbao_2023"],
    ),
    _yc("HBI-YC-044", "石良司茶叶机械厂旧址", "五峰土家族自治县五峰镇石良司村", "茶叶加工工业",
        "cultural_relic_related", "宜昌市文物保护单位（第六批2018年）；1957年建", "industrial_building", "1957年",
        "茶叶机械厂旧址厂房与制茶机械设备；保存状况待现场测绘",
        "1957年县域茶叶机械专业化制造的先行样本（采茶、制茶机械装配）",
        "五峰茶机工人与茶业机械化记忆",
        "以市保身份纳入保护体系；厂房在用/闲置状态待核",
        "直接取自五峰县文旅局文保名录（A级）；坐标未核验保持待核。",
        ["石良司茶叶机械厂"],
        ["wufeng_wenbao_2023"],
    ),
    _yc("HBI-YC-045", "五峰传统工艺遗存（清水湾龙窑、古式水动力压面厂）", "五峰土家族自治县渔洋关镇、牛庄乡金山村", "传统工艺与食品加工",
        "cultural_relic_related", "清水湾龙窑为市保（清）；古式水动力压面厂为县保（1950年）", "industrial_building", "清/1950年",
        "2处传统工艺设施：清水湾龙窑（渔洋关镇，陶瓷烧成窑体）、古式水动力压面厂（牛庄乡金山村洞湾，水轮驱动压面设备）",
        "龙窑叠烧陶瓷工艺与水轮驱动的粮食加工动力利用传统",
        "窑匠、面匠与山区水力利用的生产记忆",
        "分别以市保、县保身份纳入保护体系；保存与使用状态待核",
        "直接取自五峰县文旅局文保名录（A级）；2处合并记录；坐标未核验保持待核。",
        ["清水湾龙窑", "古式水动力压面厂"],
        ["wufeng_wenbao_2023"],
    ),
    _yc("HBI-YC-046", "柴埠溪电站", "五峰土家族自治县渔洋关镇曹家坪", "水电工程工业",
        "cultural_relic_related", "五峰县文物保护单位（1960年建，渔洋关镇曹家坪）", "industrial_utility_site", "1960年",
        "小水电站厂房、引水渠与机组遗存；装机与运行状态待现场测绘",
        "1960年山区小水电建设的引水式发电工艺",
        "柴埠溪流域电气化起步与电站职工记忆",
        "以县保身份纳入保护体系；运行/退役状态待核",
        "直接取自五峰县文旅局文保名录（A级）；坐标未核验保持待核。",
        [],
        ["wufeng_wenbao_2023"],
    ),
    _yc("HBI-YC-047", "大房坪幸福渠渡槽", "五峰土家族自治县（大房坪）", "水利工程与泵站",
        "cultural_relic_related", "五峰县文物保护单位（1965年建）", "industrial_utility_site", "1965年",
        "幸福渠渡槽本体；跨度与结构待现场测绘",
        "山区引水灌溉渡槽工艺，与麻城/孝感/利川渡槽同谱系",
        "五峰灌区水利建设集体记忆",
        "以县保身份纳入保护体系；在用/停用状态待核",
        "直接取自五峰县文旅局文保名录（A级）；坐标未核验保持待核。",
        [],
        ["wufeng_wenbao_2023"],
    ),
    _yc("HBI-YC-048", "五峰交通与商路遗存（钟岭长途汽车站、渔洋关桥河跃进桥、后槽骡马店）", "五峰土家族自治县渔洋关镇、采花乡", "内河交通与货运服务",
        "cultural_relic_related", "钟岭长途汽车站为县保（1962年）；渔洋关桥河跃进桥（1957年）；后槽骡马店为清代建筑", "industrial_transport_site", "清至1962年",
        "3处交通遗存：钟岭长途汽车站站房（1962年）、渔洋关桥河跃进桥（1957年）、后槽骡马店（清，采花乡）",
        "从骡马店到汽车站的交通业态演进序列，茶马古道—公路运输的接续",
        "五峰山区茶马商旅、班车客运与骡马店宿客记忆",
        "分别以县保/市保身份纳入保护体系；使用状态待核",
        "直接取自五峰县文旅局文保名录（A级）；3处合并记录以保持交通业态演进序列；坐标未核验保持待核。",
        ["钟岭长途汽车站", "跃进桥", "后槽骡马店"],
        ["wufeng_wenbao_2023"],
    ),
    _yc("HBI-YC-049", "大面人民公社办公楼旧址", "五峰土家族自治县湾潭镇", "工业社区",
        "cultural_relic_related", "宜昌市文物保护单位（1970年建，湾潭镇）", "industrial_social_site", "1970年",
        "人民公社办公楼旧址建筑本体；结构与保存状态待现场测绘",
        "1970年人民公社基层治理的办公建筑形制",
        "湾潭镇公社干部与社员集体生产生活记忆",
        "以市保身份纳入保护体系；现状用途待核",
        "直接取自五峰县文旅局文保名录（A级）；坐标未核验保持待核。",
        [],
        ["wufeng_wenbao_2023"],
    ),
    _yc("HBI-YC-050", "兴山川汉铁路桥墩（水月寺镇5处子项）", "宜昌市兴山县水月寺镇", "铁路交通工业",
        "provincial_relic_related", "湖北省文物保护单位（第六批2014年；1909-1911年）", "industrial_transport_site", "1909-1911年",
        "川汉铁路桥墩5处子项：三拱桥、白石子湾口铁路桥墩、青树包铁路桥墩、学堂坪铁路桥、斑鸠窝铁路桥墩（水月寺镇）；桥墩形制与保存状态待现场测绘",
        "川汉铁路为詹天佑主持设计的早期国有铁路干线（宜万铁路前身），1909年开工后停建废线——桥墩为川汉铁路宜昌-万县段实测遗存，近代铁路勘测设计与混凝土桥墩工艺的实物资料",
        "川汉铁路百年梦圆（2010年宜万铁路通车）的国家记忆与鄂西山区铁路梦的世纪等待",
        "以省保身份纳入保护体系；5处子项本体保存与保护范围待文物部门核",
        "直接取自兴山县文保名录（A级，智能体核读）；川汉铁路宜昌段桥墩与汉口粤汉铁路（京汉铁路总工会旧址 HBI-WUHAN-047）同属湖北近代铁路谱系；坐标未核验保持待核。",
        ["川汉铁路桥墩"],
        ["xingshan_chuanhan_rail_2014"],
    ),
]


RENAME = {"HBI-ES-041": "HBI-YC-041"}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    for key, source in SOURCES.items():
        if key in sources and sources[key] != source:
            sources[key] = source
    sources.update(SOURCES)
    renamed = 0
    for record in records:
        old_id = RENAME.get(record["inventory_id"])
        if old_id:
            record["inventory_id"] = old_id
            renamed += 1
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
    print(f"wave_cj_sources={len(SOURCES)} renamed={renamed} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
