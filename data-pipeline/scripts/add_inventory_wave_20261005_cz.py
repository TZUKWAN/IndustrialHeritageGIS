from __future__ import annotations

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"

S = {
    "suizhou_weidong_2021": {"source_type": "official_media", "title": "湖北老旧小区改造：随州府河化工厂改造留住了李焕英情怀", "org": "网易/随州市政府网", "pub_date": "2021-06-09", "url": "https://www.163.com/news/article/GCA4V3O9000315OA.html", "authority": "B", "notes": "该厂成立于1966年，与电影《你好，李焕英》取景地襄阳卫东机械厂同属一家总公司，老厂区原貌保存较好；曾都区南郊街道涢水南路5号。"},
    "suizhou_old_station": {"source_type": "encyclopedia_media", "title": "随州站（汉丹铁路随县站，1958年始建1961年通车，2009年东迁后闲置）", "org": "百度百科/头条", "pub_date": None, "url": "https://baike.baidu.com/item/随州站", "authority": "B", "notes": "1958年始建、1961年11月5日通车，1979年前称随县站，站址在老城区交通大道与解放路交汇处旁；2009年火车站东迁后老站淡出客运，闲置未拆，承载市民记忆。"},
    "guangshui_old_station": {"source_type": "encyclopedia_media", "title": "广水站旧址（卢汉铁路广水站，1902年开站，2007年迁现址）", "org": "百度百科/头条", "pub_date": None, "url": "https://baike.baidu.com/item/广水站", "authority": "B", "notes": "1899年动工、1902年开站，卢汉铁路最早一批车站之一、进入南方省份第一站，位于武胜关镇；2007年3月26日迁现址；1958、1959年毛主席南巡专列曾两次停靠。"},
    "suizhou_zhanbei_dayuan": {"source_type": "county_government_portal", "title": "湖北省委战备大院旧址/张体学在随县纪念馆（随县洪山镇温泉村）", "org": "随县人民政府网/随州市政府网", "pub_date": "2021-05-28", "url": "http://www.zgsuixian.gov.cn/", "authority": "A", "notes": "1964年前后张体学主持修建的战时湖北省后方基地（简称省委大院），青砖瓦房和老标语极富年代感；纪念馆在原省委战备大院旧址上建设而成，系湖北省爱国主义教育基地。"},
    "xiantao_yushan_zha_2024": {"source_type": "county_government_portal", "title": "我市发现一座民国时期修建愚山闸（仙桃市政府网转仙桃日报2024-07-17，四普新发现）", "org": "仙桃市人民政府网", "pub_date": "2024-07-17", "url": "https://www.xiantao.gov.cn/zwgk/xtyw/202407/t20240717_5270113.shtml", "authority": "A", "notes": "愚山闸1938年修建、1940年建成，至今仍在沿用；位于西流河镇（何帮至消泗公路下），青石砌筑，闸北嵌愚山闸石碑（民国二十九年立），2024年6月四普实地调查新发现。"},
    "qianjiang_huarun_2024": {"source_type": "enterprise_official_site", "title": "湖北潜江金华润化肥有限公司官网（前身1970年潜江化肥厂）", "org": "湖北潜江金华润化肥有限公司", "pub_date": None, "url": "http://www.jhrhf.cn/", "authority": "B", "notes": "公司前身是始建于1970年的潜江化肥厂，2001年改制为民营企业，2009年与晋煤金石合作、2018年三宁化工托管；现处潜江经开区化工园区；老法人主体湖北省潜江市化肥厂（竹泽路6号）已注销。"},
    "qianjiang_sanqiao_liangcang_2011": {"source_type": "county_government_notice", "title": "潜江市人民政府关于公布第四批市级重点文物保护单位的通知（潜政发〔2011〕38号，103处含三桥粮仓旧址）", "org": "潜江市人民政府网", "pub_date": "2011-09-21", "url": "https://www.hbqj.gov.cn/xxgk/zc/qtwj/szfwj/2013/201109/t20110921_2136421.html", "authority": "A", "notes": "近现代重要史迹类：三桥粮仓旧址，老新镇三桥村十组，1963年，20×60m，1204㎡。"},
    "snj_wenbao_list_2022": {"source_type": "county_cultural_relic_publicity", "title": "神农架林区一般不可移动文物保护单位名录（109处，2022-11-21）", "org": "神农架林区文化和旅游局（林区政府网）", "pub_date": "2022-11-21", "url": "http://wlj.snj.gov.cn/fdzdgknr_38827/gysyjs/ggwhtyfw/202211/t20221121_4412744.shtml", "authority": "A", "notes": "109处一般不可移动文物名录已下载核读全表，近现代工业类5处：神农架林区鞋楦厂旧址（松柏镇70年代）、神农架林区家俱厂旧址（松柏镇70年代）、神农架林区印刷厂旧址（松柏镇70年代）、神农架林区木材加工厂旧址（松柏镇70年代）、黑水河糖厂旧址（木鱼镇木鱼村1950年）——全部不在底册。"},
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
    _r("HBI-SZ-015", "湖北卫东府河化工厂老厂区", "随州市", "曾都区南郊街道涢水南路5号", "化工工业", "municipal_historical_building",
       "随州市老旧小区改造对象（曾都区南郊街道2021年改造报道确认老厂区原貌保存较好）", ["suizhou_weidong_2021"],
       "industrial_building", "1966年",
       "化工厂老厂区建筑群（涢水南路5号），原貌保存较好、部分车间废弃",
       "1966年三线化工企业的军工资质与民品转型",
       "与襄阳卫东机械厂同属一家总公司；改造中保留厂区原有面貌留住李焕英情怀",
       "老旧小区改造中保留厂区原有面貌；部分车间废弃",
       "网易2021年报道+随州市政府2021-04-26改造报道（B级，全文核读）；现名随州卫东化工有限公司；坐标未核验保持待核。",
       ["卫东化工厂", "随州卫东化工"],    ),
    _r("HBI-SZ-016", "随州老火车站（汉丹铁路随县站旧址）", "随州市", "曾都区交通大道与解放路交汇处", "铁路交通工业", "municipal_historical_building",
       "随州站（1958年始建1961年通车，2009年东迁后闲置未拆）", ["suizhou_old_station"],
       "industrial_transport_site", "1958年始建/1961年通车",
       "老火车站站房与站场设施（交通大道与解放路交汇处旁）；闲置未拆",
       "汉丹铁路1958年始建、1961年通车的随州首站",
       "随州市民老火车站出行与城市铁路发展记忆",
       "2009年火车站东迁后老站淡出客运，闲置未拆",
       "百度百科+头条报道（B级，全文核读）；铁路遗产强候选；坐标未核验保持待核。",
        [],
    ),
    _r("HBI-SZ-017", "广水老火车站旧址", "随州市", "广水市武胜关镇", "铁路交通工业", "municipal_historical_building",
       "广水站旧址（卢汉铁路广水站，1899年动工1902年开站，2007年迁现址）", ["guangshui_old_station"],
       "industrial_transport_site", "1902年",
       "卢汉铁路广水站旧址站房（武胜关镇）；百年铁路建筑",
       "卢汉铁路最早一批车站之一、进入南方省份第一站",
       "1958、1959年毛主席南巡专列曾两次停靠；广水老镇因站而兴的记忆",
       "2007年迁现址后旧址闲置",
       "百度百科+头条报道（B级，全文核读）；百年铁路建筑强候选；坐标未核验保持待核。",
        [],
    ),
    _r("HBI-SZ-018", "湖北省委战备大院旧址（张体学在随县纪念馆）", "随州市", "随县洪山镇温泉村", "三线备战工业", "municipal_historical_building",
       "随州市爱国主义教育基地（随县政府2021年红色地名+随州市政府2022-03-14报道确认）", ["suizhou_zhanbei_dayuan"],
       "industrial_social_site", "1964年前后",
       "省委战备大院旧址建筑群（青砖瓦房和老标语极富年代感）；纪念馆在原址上建设",
       "1964年前后张体学主持修建的战时湖北省后方基地",
       "绝密级省委战备大院与三线备战年代记忆",
       "在原省委战备大院旧址上建设张体学在随县纪念馆，系湖北省爱国主义教育基地",
       "随县政府2021年红色地名+随州市政府2022-03-14报道（A级，全文核读）；坐标未核验保持待核。",
        [],
    ),
    _r("HBI-XT-009", "愚山闸", "仙桃市", "仙桃市西流河镇（何帮至消泗公路下）", "水利工程与泵站", "municipal_historical_building",
       "仙桃市四普新发现（仙桃市政府网2024-07-17转仙桃日报，2024年6月实地调查新发现）", ["xiantao_yushan_zha_2024"],
       "industrial_utility_site", "1938-1940年",
       "青石砌筑水闸（闸北嵌愚山闸石碑，民国二十九年立）；闸孔规模与砌筑工艺待现场测绘",
       "民国时期水利闸站建设工艺，至今仍在沿用",
       "仙桃水利事业发展史重要篇章（仙桃日报评语）",
       "至今仍在沿用；四普新发现",
       "仙桃市政府网2024-07-17报道（A级，全文核读）；坐标未核验保持待核。",
        [],
    ),
    _r("HBI-QJ-012", "潜江化肥厂旧址（金华润前身）", "潜江市", "潜江经开区化工园区（竹泽路6号）", "化肥化工", "municipal_historical_building",
       "潜江市工业遗产候选（企业官网2024年核读确认1970年建厂沿革；正式名录未公布）", ["qianjiang_huarun_2024"],
       "industrial_building", "1970年建",
       "化肥厂厂房与生产设施（竹泽路6号）；设备与建筑保存状态待现场测绘",
       "1970年县域化肥工业的合成氨/尿素生产工艺，2001年改制民营",
       "潜江化肥厂职工与县域化工产业记忆",
       "2001年改制为民营企业，2009年与晋煤金石合作、2018年三宁化工托管",
       "企业官网自述（B级，全文核读）；在产企业按在用工业遗产处理；坐标未核验保持待核。",
        ["潜江化肥厂", "金华润化肥"],    ),
    _r("HBI-QJ-013", "三桥粮仓旧址", "潜江市", "潜江市老新镇三桥村十组", "粮食仓储工业", "county_relic_related",
       "潜江市第四批市级重点文物保护单位（潜政发〔2011〕38号，2011-09-21公布，103处之一；1963年）", ["qianjiang_sanqiao_liangcang_2011"],
       "industrial_storage_site", "1963年",
       "粮仓旧址（20×60m，1204㎡）；保存状态待现场测绘",
        "1963年县域粮仓建设工艺",
       "潜江粮食产区储粮与公粮缴纳记忆",
       "以县级文物保护单位身份纳入保护体系；保存状态待文物部门核",
       "直接取自潜政发〔2011〕38号市保四批公示全表（A级，智能体核读原文）；坐标未核验保持待核。",
        [],
    ),
    _r("HBI-SNJ-006", "神农架林区木材加工厂旧址", "神农架林区", "神农架林区松柏镇", "木材加工工业", "county_relic_related",
       "神农架林区一般不可移动文物保护单位（区文旅局2022-11-21名录109处之一；70年代）", ["snj_wenbao_list_2022"],
       "industrial_building", "20世纪70年代",
       "木材加工厂旧址厂房与设备遗存（松柏镇）；保存状态待现场测绘",
       "神农架伐木时代木材加工——从原木到板材的锯切加工链条",
       "林区伐木工人与木材加工的集体记忆，与长坊运输路/断江坪伐木队互补",
       "以区级一般不可移动文物身份纳入保护体系；保存状况待核",
       "直接取自神农架林区文旅局文保名录（A级，智能体核读全表）；与在册长坊运输路/断江坪伐木队互补加工环节；坐标未核验保持待核。",
        [],
    ),
    _r("HBI-SNJ-007", "神农架林区鞋楦厂旧址", "神农架林区", "神农架林区松柏镇", "轻工业", "county_relic_related",
       "神农架林区一般不可移动文物保护单位（区文旅局2022-11-21名录109处之一；70年代）", ["snj_wenbao_list_2022"],
       "industrial_building", "20世纪70年代",
       "鞋楦厂旧址厂房与设备遗存（松柏镇）；保存状态待现场测绘",
       "林区轻工业鞋楦制造的木工车削工艺",
       "林区轻工业多样性与职工记忆",
       "以区级一般不可移动文物身份纳入保护体系；保存状况待核",
       "直接取自神农架林区文旅局文保名录（A级，智能体核读全表）；坐标未核验保持待核。",
        [],
    ),
    _r("HBI-SNJ-008", "神农架林区家俱厂旧址", "神农架林区", "神农架林区松柏镇", "木材加工工业", "county_relic_related",
       "神农架林区一般不可移动文物保护单位（区文旅局2022-11-21名录109处之一；70年代）", ["snj_wenbao_list_2022"],
       "industrial_building", "20世纪70年代",
       "家俱厂旧址厂房与木工设备遗存（松柏镇）；保存状态待现场测绘",
       "林区木材深加工（家具制造）的木工工艺",
       "林区家具生产与职工生活配套记忆",
       "以区级一般不可移动文物身份纳入保护体系；保存状况待核",
       "直接取自神农架林区文旅局文保名录（A级，智能体核读全表）；坐标未核验保持待核。",
        [],
    ),
    _r("HBI-SNJ-009", "神农架林区印刷厂旧址", "神农架林区", "神农架林区松柏镇", "印刷工业", "county_relic_related",
       "神农架林区一般不可移动文物保护单位（区文旅局2022-11-21名录109处之一；70年代）", ["snj_wenbao_list_2022"],
       "industrial_building", "20世纪70年代",
       "印刷厂旧址厂房与印刷设备遗存（松柏镇）；保存状态待现场测绘",
       "林区印刷工业的铅印/胶印工艺",
       "林区报刊文书印刷与职工记忆",
       "以区级一般不可移动文物身份纳入保护体系；保存状况待核",
       "直接取自神农架林区文旅局文保名录（A级，智能体核读全表）；坐标未核验保持待核。",
        [],
    ),
    _r("HBI-SNJ-010", "黑水河糖厂旧址", "神农架林区", "神农架林区木鱼镇木鱼村", "食品加工工业", "county_relic_related",
       "神农架林区一般不可移动文物保护单位（区文旅局2022-11-21名录109处之一；1950年建）", ["snj_wenbao_list_2022"],
       "industrial_building", "1950年",
       "糖厂旧址厂房与制糖设备遗存（木鱼镇木鱼村）；保存状态待现场测绘",
       "1950年林区制糖工业的早期地方工业样本（名录中年代最早的地方工业点）",
       "神农架早期地方工业与糖业供应记忆",
       "以区级一般不可移动文物身份纳入保护体系；保存状况待核",
       "直接取自神农架林区文旅局文保名录（A级，智能体核读全表）；名录中年代最早的地方工业点；坐标未核验保持待核。",
        [],
    ),
]


def main():
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    for key, source in S.items():
        if key in sources and sources[key] != source:
            raise SystemExit(f"conflicting source: {key}")
    sources.update(S)
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
    print(f"wave_cz_S={len(S)} added={added} total={len(records)} src={len(sources)}")


if __name__ == "__main__":
    main()
