from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "hubei_sbao_1098": {
        "source_type": "provincial_cultural_relic_publicity",
        "title": "湖北省文物保护单位总名录（1098处，含第1-8批；2023-06-25省文旅厅发布）",
        "org": "湖北省文化和旅游厅（省文旅厅官网，Internet Archive存档核读）",
        "pub_date": "2023-06-25",
        "url": "http://wlt.hubei.gov.cn/bsfw/bmcxfw/wwbhdwml/202306/t20230625_4721281.shtml",
        "authority": "A",
        "notes": "省文旅厅1098处省级文保单位总名录（智能体curl下载614KB解析出1110条记录），对全表做工业关键词系统筛查，底册遗漏A类6项：槐山矶驳岸（省保3-52，2013年升第七批国保，长江航运纤道驳岸）、长渠遗址（省保5-44，东周，宜城+南漳，世界灌溉工程遗产）、羊楼洞新店明清石板街（省保4-58，万里茶道源头茶贸街区）、大丰仓（省保5-156，清，郧阳区古代官仓）、石骨山人民公社办公楼（省保7-12，武汉新洲）、红旗人民公社旧址（省保5-329，孝感应城）。",
    },
    "gongan_heritage_11_2023": {
        "source_type": "county_government_notice",
        "title": "关于公布黄山头镇原粮管所粮仓等11处公安县历史建筑的通知（公政函〔2023〕1号，2023-01-03公布）",
        "org": "公安县人民政府（公安县政府信息公开网）",
        "pub_date": "2023-01-03",
        "url": "http://zwgk.gongan.gov.cn/63279/202308/t20230830/388213.shtml",
        "authority": "A",
        "notes": "公安县2023年公布11处历史建筑：黄山头镇原粮管所粮仓、章庄铺镇联兴村圆仓库等；公安县融媒体通稿确认陆续挂牌。",
    },
    "gongan_hongxing_liangcang_2024": {
        "source_type": "official_media",
        "title": "公安县历史建筑名录系列(四)：红星粮仓（1968年石砌薄壳拱顶两座，改造为村史馆和农耕馆）",
        "org": "湖北日报客户端",
        "pub_date": "2024-07-18",
        "url": "https://news.hubeidaily.net/pc/c_2877085.html",
        "authority": "B",
        "notes": "红星粮仓1968年建，石砌薄壳拱顶两座，建筑面积约500㎡，用猪毛山红色岩石砌成，2021年改造为村史馆和农耕馆——工业遗产活化利用案例（甘家厂乡红双村2组）。",
    },
    "shiyan_binggongchang_yunxi": {
        "source_type": "municipal_government_portal",
        "title": "鄂陕第四军分区兵工厂旧址（郧西县观音镇万寿寺村，县级文保，1948年建，130余人9个车间）",
        "org": "十堰市人民政府门户网站（转十堰日报2023-06-01）",
        "pub_date": "2023-06-01",
        "url": "http://zt.shiyan.gov.cn/2021ztzl/bwcxljsm/xxjy/202306/t20230601_4243187.shtml",
        "authority": "A",
        "notes": "1948年2月鄂陕第四军分区在观音镇万寿寺村建立全分区唯一兵工厂，职工130余人设9个车间，枪械修配与制炸弹；旧址一进三栋依山而建共8组房屋（清代中期、民国初年）；1985年8月公布为郧西县文物保护单位。底册郧西仅陕南军区枪械修配厂旧址1条，兵工厂旧址确属遗漏。",
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
    _r("HBI-WUHAN-073", "槐山矶驳岸", "武汉市", "江夏区金口街（长江南岸）", "港口与水运工业",
       "provincial_relic_related", "湖北省文物保护单位（省保3-52）；2013年并入第七批全国重点文物保护单位",
       ["hubei_sbao_1098"], "industrial_transport_site", "明代",
       "长江航运纤道/驳岸工程（槐山矶矶头条石砌筑驳岸），明代航运水工构筑物；驳岸长度与砌筑形式待现场测绘",
       "长江航运纤道/驳岸工程的明代水工构筑物——纤夫拉纤行船的航道整治设施",
       "金口古镇长江航运与纤夫拉纤的集体记忆",
       "以省保身份纳入保护体系（2013年升国保）；保护范围与建控地带待文物部门核",
       "直接取自1098处省级文保总名录（A级，智能体curl解析核读）；槐山矶驳岸2013年升国保——与底册长江航运谱系互补；坐标未核验保持待核。",
       [],),
    _r("HBI-XIANGYANG-072", "长渠遗址（白起渠）", "襄阳市", "宜城市、南漳县", "水利工程与泵站",
       "provincial_relic_related", "湖北省文物保护单位（省保5-44，东周）；2018年世界灌溉工程遗产",
       ["hubei_sbao_1098"], "industrial_utility_site", "东周（公元前279年）",
       "长渠（白起渠）灌溉渠系遗址（分布在宜城市和南漳县境内）；渠首、干渠与分水设施待现场测绘",
       "公元前279年白起攻鄢时所筑的军事水利工程，后转化为灌溉渠系——中国最早的大型无坝引水灌溉工程之一，2018年获世界灌溉工程遗产",
       "宜城/南漳灌区农业灌溉与白起渠的持续利用记忆",
       "以省保身份纳入保护体系；2018年获世界灌溉工程遗产（与都江堰同批）；灌溉功能延续使用",
       "直接取自1098处省级文保总名录（A级，智能体curl解析核读）；世界灌溉工程遗产为国际权威认定；坐标未核验保持待核。",
       ["白起渠", "武镇百里长渠"],
    ),
    _r("HBI-XN-025", "羊楼洞、新店明清石板街", "咸宁市", "赤壁市羊楼洞镇、新店镇", "历史水运、码头与城市商贸",
       "provincial_relic_related", "湖北省文物保护单位（省保4-58，明清）",
       ["hubei_sbao_1098"], "industrial_trade_site", "明清",
       "羊楼洞明清石板街与新店石板街（万里茶道源头茶贸街区，独轮车车辙印迹石板路面）；街区范围与建筑保存待现场测绘",
       "万里茶道源头的茶叶加工—集散—运输商贸街区形制，独轮车运茶的车辙石板路面为茶贸运输的实物见证",
       "羊楼洞茶庄帮、新店码头茶贸与万里茶道起点记忆",
       "以省保身份纳入保护体系；街区保护规划与建筑修缮待文物部门核",
       "直接取自1098处省级文保总名录（A级，智能体curl解析核读）；与底册赵李桥茶厂（HBI-XN-017）、万里茶道系列互补；坐标未核验保持待核。",
       ["羊楼洞石板街", "新店石板街"],
    ),
    _r("HBI-SY-051", "大丰仓", "十堰市", "郧阳区", "粮食仓储工业",
       "provincial_relic_related", "湖北省文物保护单位（省保5-156，清）",
       ["hubei_sbao_1098"], "industrial_storage_site", "清代",
       "大丰仓建筑本体（郧阳区古代官仓）；仓房形制、容量与保存状态待现场测绘",
       "清代官仓的储粮建筑形制与管理体制",
       "郧阳府官仓储粮与赈济记忆",
       "以省保身份纳入保护体系；保存状况待文物部门核",
       "直接取自1098处省级文保总名录（A级，智能体curl解析核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    _r("HBI-WUHAN-074", "石骨山人民公社办公楼", "武汉市", "新洲区", "工业社区",
       "provincial_relic_related", "湖北省文物保护单位（省保7-12，第七批）",
       ["hubei_sbao_1098"], "industrial_social_site", "待核",
       "人民公社办公楼建筑本体（新洲区石骨山）；建筑形制与保存状态待现场测绘",
       "人民公社基层治理的办公建筑形制",
       "公社治理与集体化生产生活记忆",
       "以省保身份纳入保护体系；现状用途待核",
       "直接取自1098处省级文保总名录（A级，智能体curl解析核读）；坐标未核验保持待核。",
        [],
    ),
    _r("HBI-XG-032", "红旗人民公社旧址", "孝感市", "应城市", "工业社区",
       "provincial_relic_related", "湖北省文物保护单位（省保5-329）",
       ["hubei_sbao_1098"], "industrial_social_site", "1958年",
       "红旗人民公社旧址建筑本体；建筑形制与保存状态待现场测绘",
       "1958年人民公社化运动的基层组织建筑标本",
       "应城红旗公社集体化治理与生产生活记忆",
       "以省保身份纳入保护体系；现状用途待核",
       "直接取自1098处省级文保总名录（A级，智能体curl解析核读）；坐标未核验保持待核。",
        [],
    ),
    _r("HBI-SY-052", "鄂陕第四军分区兵工厂旧址", "十堰市", "郧西县观音镇万寿寺村", "军工修配工业",
       "county_relic_related", "郧西县文物保护单位（1985年8月公布）",
       ["shiyan_binggongchang_yunxi"], "industrial_building", "1948年",
       "兵工厂旧址建筑群8组房屋（一进三栋依山而建，清代中期、民国初年）；9个车间分布与设备遗迹待现场测绘",
       "1948年鄂陕第四军分区兵工厂的枪械修配与制炸弹工艺，130余人的战时军工生产体系",
       "解放战争时期随县军工生产与根据地武器自给记忆",
       "以县级文保身份纳入保护体系；保存状况与展示利用待核",
       "直接取自十堰市政府门户网站国防教育栏转十堰日报2023-06-01（A级，智能体核读原文）；与底册陕南军区枪械修配厂旧址（HBI-SY 系列）同一性待核；坐标未核验保持待核。",
        [],
    ),
    _r("HBI-JZ-073", "公安县红星粮仓", "荆州市", "公安县甘家厂乡红双村2组", "粮食仓储工业",
       "municipal_historical_building", "公安县历史建筑（湖北日报客户端2024-07-18名录系列四报道；1968年建）",
       ["gongan_hongxing_liangcang_2024"], "industrial_storage_site", "1968年",
       "石砌薄壳拱顶粮仓两座（建筑面积约500㎡，猪毛山红色岩石砌筑），2021年改造为村史馆和农耕馆",
       "石砌薄壳拱顶粮仓建筑工艺（猪毛山红色岩石砌筑），1960-70年代集体储粮设施样本",
       "红星粮仓改造为村史馆和农耕馆的活化利用——工业遗产功能转型的社区样本",
       "2021年改造活化；以历史建筑身份纳入保护体系",
       "直接取自湖北日报客户端2024-07-18报道（B级，全文核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    _r("HBI-JZ-074", "公安县历史建筑工业群（黄山头镇原粮管所粮仓、章庄铺镇联兴村圆仓库等11处）", "荆州市", "公安县（各乡镇）", "粮食仓储工业",
       "municipal_historical_building", "公安县历史建筑（公政函〔2023〕1号，2023-01-03公布，11处之列）",
       ["gongan_heritage_11_2023"], "industrial_storage_site", "待核",
       "11处中工业相关：黄山头镇原粮管所粮仓、章庄铺镇联兴村圆仓库等（其余8处在PDF附件中待解析）；保存状态待现场测绘",
       "公安县县域粮站—粮管所—圆仓的三级粮食储运网络标本",
       "公安县粮农售粮与粮站职工记忆",
       "以市级历史建筑身份正式公布保护；在用/停用状态待核",
       "直接取自公政函〔2023〕1号通知（A级，正文+PDF附件名已核读）；11处中非工业对象（民居等）不计入本条；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["黄山头镇原粮管所粮仓", "联兴村圆仓库"],
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
    print(f"wave_cx_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
