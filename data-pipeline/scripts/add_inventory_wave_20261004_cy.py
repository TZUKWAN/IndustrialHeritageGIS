from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "hanyang_paper_mill": {
        "source_type": "official_media",
        "title": "这里曾被称为纸城 藏着几代李焕英的青葱岁月（汉阳造纸厂）",
        "org": "荆楚网（源：武汉晚报）",
        "pub_date": "2021-03-18",
        "url": "http://news.cnhubei.com/content/2021-03/18/content_13682832.html",
        "authority": "B",
        "notes": "据《汉阳造纸厂志》记载：汉阳造纸厂是新中国成立后湖北兴建的第一批现代化国营工厂，也是湖北省最大的造纸厂，1950年破土动工，1953年建成投产；曾称'纸城'，现生活区（东荆社区）尚存。",
    },
    "wuhan_cigarette_hanyang_2025": {
        "source_type": "official_media",
        "title": "综合投资5亿+！汉阳烟厂将变身创新产业园（人民日报客户端转湖北日报）",
        "org": "人民日报客户端（转湖北日报）",
        "pub_date": "2025-07-09",
        "url": "https://www.peopleapp.com/column/30049609308-500006365266",
        "authority": "A",
        "notes": "位于王家湾，占地约17万平方米、超30栋建筑，1983年正式投产，是红金龙腾飞、黄鹤楼矗立的传奇之地，也是1916的诞生之地；武汉卷烟厂最早在硚口设厂，80年代迁汉阳，2018年迁东西湖后停产，现启动以工业记忆为魂的旧厂改造。",
    },
    "wuchang_shipyard_2023": {
        "source_type": "media_history_article",
        "title": "武昌造船厂成长史（1934年创始沿革完整：常规潜艇制造基地/西陵长江大桥钢箱梁/卫星塔架）",
        "org": "网易号",
        "pub_date": "2023-04-04",
        "url": "https://www.163.com/dy/article/I1FSD4GM05561JVE.html",
        "authority": "B",
        "notes": "武船前身湖北省建设厅武昌机器厂始建于1934年6月（武昌文昌门晚清湖北纺纱官局旧址开工），相继沿用湖北省航业局修船厂、湖北省万县机械厂等名称；1949年湖北机械厂与汉阳船舶修造厂合并成立江汉船舶机械公司，为国家船舶工业局第一个直属造船厂，1953年定名武昌造船厂；常规潜艇制造基地，建造西陵长江大桥钢箱梁、西昌/酒泉卫星发射塔架。",
    },
    "fenghuangshan_substation_2018": {
        "source_type": "international_media",
        "title": "超高压运维人郑汉明：40年见证变电站运维赶超世界（凤凰山500千伏变电站中华第一站）",
        "org": "国际在线湖北",
        "pub_date": "2018-08-03",
        "url": "https://hb.cri.cn/chinanews/20180803/5eaad191-2502-85b2-9b59-330fc99871dd.html",
        "authority": "B",
        "notes": "国家批准建设我国首个500千伏交流输变电工程——河南平顶山至湖北武昌（平武）工程，1982年1月13日正式投产；人称中华第一站的500千伏凤凰山变电站，设备从日、法、瑞典等6国7公司引进。",
    },
    "jingzhou_jingmian_2024": {
        "source_type": "local_media",
        "title": "见证荆州最大棉纺厂的辉煌岁月（荆沙棉纺织厂/荆棉）",
        "org": "荆州新闻网",
        "pub_date": "2024-06-25",
        "url": "https://www.jznews.com.cn/",
        "authority": "B",
        "notes": "上世纪八十年代沙市有一座江汉平原地域上最大的纺织工厂——荆沙棉纺织厂；2023年有打造工业主题荆棉1974口袋公园建议；2001年改制批复。",
    },
    "xiaogan_matang_mijiu": {
        "source_type": "media_report",
        "title": "匠心筑梦 美味传承——孝感麻糖米酒有限责任公司70年发展纪实",
        "org": "网易/孝感日报",
        "pub_date": "2024-10-15",
        "url": "https://hb.news.163.com/24/1015/",
        "authority": "B",
        "notes": "1995年更名为孝感麻糖米酒集团有限责任公司；1954年建立孝感县麻糖厂；中华老字号企业传承70载，品牌含神霖米酒。孝感米酒成于孝、始于宋。",
    },
    "qianjiang_yuanlinqing": {
        "source_type": "county_government_portal",
        "title": "省级非遗：园林青酿酒技艺（潜江市政府网）",
        "org": "潜江市人民政府网",
        "pub_date": "2021-09-06",
        "url": "http://www.hbqj.gov.cn/",
        "authority": "A",
        "notes": "潜江市政府网载明园林青酿酒技艺入选省级非遗；前身1951年潜江县地方国营酒厂，1983年定名园林青酒厂；1985/1990/1995蝉联三届国家金质奖；曹禺两度题词万里故乡酒美哉园林青。",
    },
    "sha_shi_yinran_2017": {
        "source_type": "media_article",
        "title": "老厂印迹｜沙市东风印染厂",
        "org": "搜狐·荆州记忆",
        "pub_date": "2017-12-29",
        "url": "https://www.sohu.com/a/213667153_779643",
        "authority": "B",
        "notes": "前身东明漂染整厂，1954年由七家私营商店合并；1975年改装八色印花机结束只染不印；1980年涤棉线试车成功；荆沙合并后改荆州东风印染厂，1999年改制。",
    },
    "lushan_sanxia_test_dam": {
        "source_type": "government_water_resources",
        "title": "陆水水库水利风景区（三峡试验坝主题公园，1958年经毛泽东周恩来批准兴建）",
        "org": "水利部水利文明网",
        "pub_date": "2022-09-05",
        "url": "http://slwm.mwr.gov.cn/wllm/rhal/sgcwh2/202209/t20220905_1579366.html",
        "authority": "A",
        "notes": "1958年经毛泽东、周恩来批准兴建，为三峡水利工程试验坝；8#副坝为亚洲最长粘土均质坝1543m；现有三峡试验坝主题公园、试验坝展览馆。",
    },
}


def _r(rid, nm, city, dc, cat, lvl, status, src, kind, yr, mat, tech, soc, use, notes, aliases):
    return {
        "inventory_id": rid, "name": nm, "city": city, "district_county": dc,
        "industry_category_l1": cat, "recognition_level": lvl, "recognition_status": status,
        "record_status": "source_confirmed", "geocode_status": "pending", "source_keys": src,
        "cultural_evidence": {"material_carriers": mat, "technical_memory": tech, "social_memory": soc, "current_use_or_loss": use},
        "notes": notes, "aliases": aliases, "asset_kind": kind,
    }


RECORDS = [
    _r("HBI-WUHAN-075", "汉阳造纸厂旧址", "武汉市", "武汉经开区（沌口）", "造纸工业",
       "municipal_historical_building", "武汉市级工业遗产候选（《汉阳造纸厂志》记载+2023年拆迁报道+生活区东荆社区棚改中）",
       ["hanyang_paper_mill"], "industrial_building", "1950-2017年",
       "厂区一侧已建房地产；生活区（东荆社区）红砖红砖宿舍保存成片、棚改中；《汉阳造纸厂志》存档",
       "1950年破土动工、1953年建成投产——新中国成立后湖北兴建的第一批现代化国营工厂，湖北省最大造纸厂，全国八大纸厂之一",
       "纸城记忆：几代汉纸职工与东荆社区生活区记忆；武汉晨鸣二厂延续体",
       "2023年8月厂区启动拆迁；生活区棚改中，红砖宿舍保存成片",
       "汉阳造纸厂志记载（B级全文核读）；1950年建厂至2017年，67年工业史，全国八大纸厂之一，生活区尚存；坐标未核验保持待核。",
        ["汉阳造纸厂", "纸城", "武汉晨鸣二厂"],
    ),
    _r("HBI-WUHAN-076", "武汉卷烟厂汉阳厂区", "武汉市", "汉阳区王家湾", "烟草工业",
       "municipal_historical_building", "武汉市级历史建筑候选（人民日报客户端2025-07-09报道：占地约17万㎡/超30栋建筑，启动以工业记忆为魂的旧厂改造）",
       ["wuhan_cigarette_hanyang_2025"], "industrial_building", "1983年投产/2018年停产",
       "老厂区超30栋建筑（占地约17万㎡），启动以工业记忆为魂的旧厂改造",
       "红金龙、黄鹤楼品牌的传奇之地，1916诞生地——武汉卷烟厂最早在硚口设厂，80年代迁汉阳，2018年迁东西湖",
       "汉阳烟厂职工与红金龙/黄鹤楼品牌消费记忆",
       "2018年迁东西湖后停产，现启动旧厂改造",
        "人民日报客户端转湖北日报2025-07-09（A级，全文核读）；30余栋建筑整体保留改造中；坐标未核验保持待核。",
        ["汉阳烟厂", "武汉卷烟厂"],
    ),
    _r("HBI-WUHAN-077", "武昌造船厂", "武汉市", "武昌区（文昌门原址/现址）", "造船工业",
       "municipal_historical_building", "武汉市级工业遗产候选（1934年创始沿革完整，常规潜艇制造基地/西陵长江大桥钢箱梁/卫星塔架；现役大厂）",
       ["wuchang_shipyard_2023"], "industrial_building", "1934年至今",
       "造船厂厂房、船台、码头（文昌门原址/现址）；常规潜艇制造基地",
       "1934年创始→1949年江汉船舶机械公司（国家船舶工业局第一个直属造船厂）→1953年定名武昌造船厂→常规潜艇制造基地→西陵长江大桥钢箱梁/西昌酒泉卫星塔架",
       "武船职工与武汉造船工业的国家记忆",
       "现役造船大厂；以市级工业遗产候选身份纳入保护体系",
       "武昌造船厂成长史全文核读（B级）；1934年创始沿革完整；现役大厂暂无遗产认定；坐标未核验保持待核。",
        ["武船"],
    ),
    _r("HBI-WUHAN-078", "凤凰山500千伏变电站", "武汉市", "武汉凤凰山（江夏区/武昌南郊）", "电力工业",
       "municipal_historical_building", "武汉市级工业遗产候选（1982年正式投产，中华第一站，中国首座500kV级变电站之一；现役变电站）",
       ["fenghuangshan_substation_2018"], "industrial_utility_site", "1982年",
       "500千伏变电站建筑与变电设备（设备从日、法、瑞典等6国7公司引进）",
       "1982年平武工程（河南平顶山至湖北武昌）500千伏交流输变电——中国首个500kV输变电工程",
       "中国电力工业从500kV追赶到世界领先的跨越记忆",
       "现役变电站；以市级工业遗产候选身份纳入保护体系",
       "国际在线湖北2018-08-03全文核读（B级）；坐标未核验保持待核。",
        ["凤凰山变电站", "中华第一站"],
    ),
    _r("HBI-JZ-075", "荆沙棉纺织厂（荆棉）", "荆州市", "沙市区（北京路）", "纺织工业",
       "municipal_historical_building", "荆州市历史建筑候选（2024年荆棉1974工业记忆公园动议+2001年改制批复；2024-06-25荆州新闻网报道）",
       ["jingzhou_jingmian_2024"], "industrial_building", "1974年建/1979年投产",
       "荆棉厂房与生活区（省纺织局直属厂，江汉平原最大纺织工厂）；荆棉1974工业记忆公园动议",
       "1974年建厂、1979年投产——省纺织局直属厂，江汉平原最大纺织工厂",
       "荆棉职工与沙市纺织城的集体记忆；荆棉1974口袋公园动议",
       "2001年改制宣布破产；荆棉1974工业记忆公园动议待落实",
       "荆州新闻网2024-06-25报道（B级，全文核读）；荆棉1974工业记忆公园动议待落实；坐标未核验保持待核。",
        ["荆棉", "荆沙棉纺织厂"],
    ),
    _r("HBI-JZ-076", "沙市东风印染厂", "荆州市", "沙市区", "纺织印染工业",
       "municipal_historical_building", "荆州市历史建筑候选（搜狐·荆州记忆2017-12-29详细沿革报道；1999年改制）",
       ["sha_shi_yinran_2017"], "industrial_building", "1954年建/1999年改制",
       "印染厂房与八色印花机设备（1975年改装八色印花机结束只染不印）",
        "1954年由七家私营商店合并——东明漂染整厂起步；1975年改装八色印花机结束只染不印；1980年涤棉线试车成功",
       "沙市纺织印染骨干企业职工记忆",
       "荆沙合并后改荆州东风印染厂，1999年改制",
       "搜狐·荆州记忆2017-12-29详细沿革报道（B级，全文核读）；坐标未核验保持待核。",
        ["沙市东风印染厂", "东风印染厂"],
    ),
    _r("HBI-XG-033", "孝感麻糖米酒厂", "孝感市", "孝南区（城隍潭九号等）", "食品加工工业",
       "municipal_historical_building", "孝感市级工业遗产候选（1954年建立孝感县麻糖厂，1995年更名集团公司；中华老字号·神霖米酒）",
       ["xiaogan_matang_mijiu"], "industrial_building", "1954年",
       "麻糖米酒厂建筑与生产设施；酿造车间与老作坊保存状态待现场测绘",
       "孝感麻糖（源于宋代）与孝感米酒（成于孝、始于宋）的酿造工艺——中华老字号",
       "孝感麻糖米酒作为城市名片的市民记忆",
       "1995年更名孝感麻糖米酒集团有限责任公司，中华老字号企业传承70载",
       "多源交叉：孝感市文旅局孝感市第一批优秀历史建筑名录（A级）、搜狐2024-10-16报道（B级）、中国日报网转载；孝感老麻糖厂（城隍潭九号）已入孝感市第一批历史建筑名录（与孝感市第一批56处中孝感老麻糖厂可能为同一厂区不同称谓，待核）",
        ["孝感麻糖米酒集团", "神霖米酒"],
    ),
    _r("HBI-QJ-011", "园林青酒厂", "潜江市", "潜江市（园林街道）", "酿酒工业",
       "municipal_historical_building", "潜江市历史建筑候选（潜江市政府网省级非遗园林青酿酒技艺2021-09-06；前身1951年潜江县地方国营酒厂；1985/1990/1995蝉联三届国家金质奖；省非遗）",
       ["qianjiang_yuanlinqing"], "industrial_building", "1951年",
       "园林青酒厂建筑与酿造设施；窖池与酿造车间保存状态待现场测绘",
       "园林青酒的酿造技艺（省级非遗）与清香型酿酒工艺",
       "潜江园林青酒三次获国家金质奖与曹禺题词万里故乡酒的城市记忆",
       "2013年园林青酿酒技艺入选湖北省非遗",
       "潜江市政府网省级非遗园林青酿酒技艺（A级，智能体核读）+潜江新闻网园林青守正创新报道（B级）；1983年定名园林青酒厂，蝉联三届国家金质奖；坐标未核验保持待核。",
        ["园林青酒", "潜江县地方国营酒厂"],
    ),
]


def main():
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    for key, source in SOURCES.items():
        if key in sources and sources[key] != source:
            raise SystemExit(f"conflicting source: {key}")
    sources.update(SOURCES)
    added = 0
    for record in RECORDS:
        existing = next((r for r in records if r["inventory_id"] == record["inventory_id"]), None)
        if existing is not None:
            if existing != record:
                raise SystemExit(f"conflicting duplicate record: {record['inventory_id']}")
            continue
        if any(r["name"] == record["name"] for r in records):
            raise SystemExit(f"conflicting duplicate name: {record['name']}")
        records.append(record)
        added += 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_cy_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
