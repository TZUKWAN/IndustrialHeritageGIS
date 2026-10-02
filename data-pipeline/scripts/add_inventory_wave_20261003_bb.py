from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "yichang_heritage_buildings_2022": {
        "source_type": "municipal_government_notice",
        "title": "市人民政府关于公布宜昌市第二批历史建筑名录的通知（宜府发〔2022〕22号，26处）",
        "org": "宜昌市人民政府门户网站",
        "pub_date": "2022-12-07",
        "url": "http://www.yichang.gov.cn/zfxxgk/show.html?aid=1&id=219461&t=4",
        "authority": "A",
        "notes": "宜府发〔2022〕22号公布满意楼等26处第二批历史建筑，正文附全表（含建筑面积、年代与逐处简介）：第25项普溪河老渡槽遗址（夷陵区分乡镇普溪河村，1966年始建1970年通水23小时后倒塌致42死4重伤，次月复建1971年再通水，2017年被新渡槽替代、2019年拆除上层渠槽现存公路桥遗址，全长1005.3米最大高度57.6米钢混简支梁式）；第3项永耀电灯公司营业部（西陵区解放路3号，1930年代，宜昌最大民族实业公司）；第17-20项猇亭区织布街汪泰丰花行（1803年古老背第一家花行）、郑记染坊（1950公私合营）、刘发记商行与彭和祥商号（六七十年代组建棉一社二社后为宜都县古老背镇棉织厂，刘发记屋墙残存《鞍钢宪法》万岁标语）。",
    },
}


RECORDS = [
    {
        "inventory_id": "HBI-YC-020",
        "name": "普溪河老渡槽遗址",
        "city": "宜昌市",
        "district_county": "夷陵区分乡镇普溪河村",
        "industry_category_l1": "水利工程与泵站",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "宜昌市第二批历史建筑（宜府发〔2022〕22号名录第25项；1966年始建、1970年通水即塌、1971年复建再通水，2019年拆除上层渠槽现存公路桥遗址）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["yichang_heritage_buildings_2022"],
        "cultural_evidence": {
            "material_carriers": "现存公路桥遗址：全长1005.3米、最大高度57.6米的钢混简支梁式渡槽（高架渠与输水桥组合输水系统），2019年4月29日拆除上层渠槽通水部分；遗址本体保存与剩余构件范围待现场测绘",
            "technical_memory": "1966年3月开工、1970年8月1日通水，因设计失误通水仅23小时于8月2日倒塌，1971年4月12日复建竣工通水——设计失误、重大事故与复建的全过程技术教训记忆；2015年新渡槽动工、2017年通水实现功能替代",
            "social_memory": "渡槽倒塌特大事故（42人死亡、4人重伤）是宜昌水利史上的沉痛集体记忆，复建通水与老渡槽服役近半个世纪又承载灌区几代人的用水记忆",
            "current_use_or_loss": "老渡槽水利功能2017年由新渡槽替代、上层渠槽2019年拆除，现存公路桥遗址以第二批历史建筑身份保护；遗址展示利用方案与保护范围待核",
        },
        "notes": "直接取自宜昌市政府第二批历史建筑名录正文表（A级，逐处含面积年代与事故史简介）；本条是全国罕有的以倒塌事故与复建史完整记载的渡槽遗产，技术记忆字段保留事故表述以存真相；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["普溪河渡槽"],
        "asset_kind": "industrial_utility_site",
    },
    {
        "inventory_id": "HBI-YC-021",
        "name": "永耀电灯公司营业部旧址",
        "city": "宜昌市",
        "district_county": "西陵区解放路",
        "industry_category_l1": "电力能源",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "宜昌市第二批历史建筑（宜府发〔2022〕22号名录第3项；1930年代建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["yichang_heritage_buildings_2022"],
        "cultural_evidence": {
            "material_carriers": "三层混合结构营业楼（解放路3号，577.68平方米），欧式双拱门改单门结构、欧式柱式与窗楣、两侧方形欧式柱延伸至顶；室内结构保存状况待现场测绘",
            "technical_memory": "1930年代民族电力工业经营场所——刘梅森创办永耀电灯公司，抗战期间原址沦为丸富洋行与丸腾商店，战后重建为宜昌最大民族实业公司，记录民族资本电力事业的兴衰脉络",
            "social_memory": "宜昌近代电力照明与民族实业家记忆；与汉口电灯公司（HBI-WUHAN-003）共同构成湖北近代电力工业的城市谱系",
            "current_use_or_loss": "以第二批历史建筑身份纳入保护体系，现状商用；保护范围与活化方向待核",
        },
        "notes": "直接取自宜昌市政府第二批历史建筑名录正文表（A级）；本条为建筑（营业部）记录，永耀电灯公司发电厂厂址待后续检索补录；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["永耀电灯公司"],
        "asset_kind": "industrial_building",
    },
    {
        "inventory_id": "HBI-YC-022",
        "name": "古老背织布街纺织业商号建筑群（汪泰丰花行、郑记染坊、刘发记商行、彭和祥商号）",
        "city": "宜昌市",
        "district_county": "猇亭区织布街",
        "industry_category_l1": "纺织工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "宜昌市第二批历史建筑（宜府发〔2022〕22号名录第17-20项，共4处，均位于猇亭区织布街）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["yichang_heritage_buildings_2022"],
        "cultural_evidence": {
            "material_carriers": "名录载明4处单体：汪泰丰花行（织布街91-1号，1803年建，古老背第一家花行，日收棉花500-700包，正立面残存学大寨标语）、郑记染坊（106号，纺织浆染作坊，四合院四水归堂）、刘发记商行（69-1号，六七十年代组建棉一社二社，屋墙残存《鞍钢宪法》万岁标语）、彭和祥商号（69号，经营花纱布）；均为徽派/砖木混合结构，保存细节以名录简介为准",
            "technical_memory": "从清代棉花交易（花行）、纺织浆染作坊到合作社与宜都县古老背镇棉织厂的纺织产业完整脉络；徽派砖木建造与染坊四水归堂工艺",
            "social_memory": "古老背镇因棉织业崛起的市镇记忆，织布街商号家族经营、公私合营与合作社集体生产的多阶段社会变迁；抗战与解放战争时期董记百货地下交通站等红色记忆见同一街区名录记载",
            "current_use_or_loss": "以第二批历史建筑身份纳入保护体系；织布街整体风貌与各单体现状用途待现场核验",
        },
        "notes": "直接取自宜昌市政府第二批历史建筑名录正文表（A级）；4处合并为一条纺织业建筑群记录以保持织布街产业脉络完整（名录另有董记百货、段兴记百货、张记酒行、孟记商行等商贸建筑未入本条，属商业脉络可后续再议）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["汪泰丰花行", "郑记染坊", "刘发记商行", "彭和祥商号", "古老背织布街"],
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
    for key, source in SOURCES.items():
        if key in sources and sources[key] != source:
            raise SystemExit(f"conflicting source: {key}")
    sources.update(SOURCES)
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_bb_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
