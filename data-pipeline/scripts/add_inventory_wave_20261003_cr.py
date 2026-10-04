from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "tongcheng_batches_2022_2024": {
        "source_type": "county_public_notice",
        "title": "通城县历史建筑认定公示（2022年38处+2024年52处“百日行动”批次）",
        "org": "通城县住房和城乡建设局（通城县人民政府网 www.zgtc.gov.cn）",
        "pub_date": "2022-03-22",
        "url": "http://www.zgtc.gov.cn/xxgk/zc/qtzdgkwj/202203/t20220322_2567167.shtml",
        "authority": "A",
        "notes": "2022年公示38处完整名单表已核读：北港岭源湖北省长石矿旧址（北港镇姜家垅）【矿】、关刀八燕渡槽（关刀镇八燕村，与底册省保八燕渡槽HBI-XN-002为同一对象不同批次认定）、关刀高冲公社（关刀镇高冲村）、沙堆九井峰茶场（沙堆镇沙堆村）等；2024年“百日行动”公示52处（http://www.zgtc.gov.cn/dfbmptlj/bmxxgkpt/xzjj/zc_22252/qtzdgkwj_35277/202405/t20240520_3588411.shtml，附件PDF已核读）：石家渡槽（北港镇桂家村一组，约100年以上）等。",
    },
    "jiayu_heritage_2023_2024": {
        "source_type": "county_government_notice",
        "title": "嘉鱼县人民政府关于公布嘉鱼县第一批历史建筑保护名单的通知（11处，2023-05-26成文）及省住建厅“百日行动”30处挂牌报道",
        "org": "嘉鱼县人民政府门户网站/湖北省住房和城乡建设厅",
        "pub_date": "2023-05-26",
        "url": "http://www.jiayu.gov.cn/xxgk/xxgkmls/gysyjs/cszhzf/202403/t20240312_3504246.shtml",
        "authority": "A",
        "notes": "第一批11处附件PDF已完整核读：永逸闸（鱼岳镇木鱼山东护城干堤桩号298+600）【水闸】、八斗渡槽（高铁岭镇九龙村下屋孙家至石塘村，横跨大岩畈）【渡槽】等；省住建厅2024-08-26报道（http://zjt.hubei.gov.cn/bmdt/dtyw/szsm/202408/t20240826_5315164.shtml）载明“百日行动”遴选出范家桥、朱砂桥、文庙山县委大院大门门楼等30处挂牌，湖北日报2025-12-11证实41处落实挂牌保护。",
    },
    "chongyang_liujia_2024": {
        "source_type": "county_media_report",
        "title": "崇阳县挂牌保护20处历史建筑（第一批，含刘家渡槽）",
        "org": "崇阳县（咸宁网/微信公众号转载）",
        "pub_date": None,
        "url": None,
        "authority": "B",
        "notes": "崇阳县第一批20处历史建筑挂牌（媒体核读，政府网无正式通知原文）：含刘家渡槽【渡槽】★；分布天城镇6处、金塘镇1处、路口镇4处、石城镇2处、白霓镇7处。另崇阳四普新发现公示（2025-10-24，http://www.chongyang.gov.cn/xxgk/dfbmptlj/bmxxgkpt/whhlyj/fdzdgknr_19990/gysyjs_33446/ggwhfw_33448/202510/t20251024_4089286.shtml）含大市渡槽（白霓镇大市村）、洞口渡槽（肖岭乡泉陂村）、青山水库大坝（青山镇青山村）3处水利【四普新发现线索，暂不入库】。完整名单原文未获取，仅记刘家渡槽一处。",
    },
    "jianli_30_2024": {
        "source_type": "county_public_notice",
        "title": "关于监利市白螺镇圣灵寺等历史建筑认定的公示（30处，2023-05-31至2024-06-06公示期）",
        "org": "监利市住房和城乡建设局（监利市政府信息公开）",
        "pub_date": "2024-06-06",
        "url": "http://zwgk.jianli.gov.cn/38536/106220243/t103220243064/495250.shtml",
        "authority": "A",
        "notes": "监利市30处历史建筑认定公示已核读，工业类6处：白螺镇粮站、黄歇口镇余埠粮管所、汪桥镇严场粮库、汪桥镇莲台粮库、毛市镇红瓦仓库、毛市镇砖瓦厂渡口（工业运输遗存）。佐证：湖北日报客户端2025-04-27载刘朝栋民居（公示第6项）“2024年6月被监利市人民政府公布为历史建筑”——公示已进入正式公布程序。",
    },
    "honghu_batch2_2023": {
        "source_type": "county_government_notice",
        "title": "洪湖市人民政府关于公布洪湖市第二批历史建筑的通知（洪政函〔2023〕14号，11处）",
        "org": "洪湖市人民政府门户网站（政府信息公开）",
        "pub_date": "2023-04-19",
        "url": "https://zwgk.honghu.gov.cn/30279/202304/t20230426/335943.shtml",
        "authority": "A",
        "notes": "洪政函〔2023〕14号公布11处原文+名录全表已核读，工业相关2处：乌林粮管所仓库（乌林镇黄蓬老街，1968年，1090㎡，原承担粮食收储，后为叶家门国家粮库乌林收购点，“功能特殊，具有一定标志性”）、六垸大队部（万全镇张当村，1969年，原永丰人民公社六垸大队会议楼，2层砖混约144㎡，大礼堂已拆）。第一批4处（洪政发〔2021〕6号）无工业对象。",
    },
}


def _xn(record_id: str, name: str, dc: str, cat: str, status: str, src: list, kind: str, year: str, material: str, tech: str, social: str, use: str, notes: str, aliases: list) -> dict:
    return {
        "inventory_id": record_id,
        "name": name,
        "city": "咸宁市",
        "district_county": dc,
        "industry_category_l1": cat,
        "recognition_level": "municipal_historical_building",
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


def _jl(record_id: str, name: str, dc: str, cat: str, kind: str, year: str, material: str, tech: str, social: str, use: str, notes: str, aliases: list) -> dict:
    return {
        "inventory_id": record_id,
        "name": name,
        "city": "荆州市",
        "district_county": dc,
        "industry_category_l1": cat,
        "recognition_level": "municipal_historical_building",
        "recognition_status": "监利市历史建筑（市住建局2023-05-31认定公示30处之列，2024年6月市政府公布程序生效）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["jianli_30_2024"],
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
    _xn("HBI-XN-018", "北港岭源湖北省长石矿旧址", "通城县北港镇姜家垅", "矿山采选工业",
        "通城县历史建筑（2022-03-22认定公示38处名录之列）", ["tongcheng_batches_2022_2024"], "industrial_building", "待核",
        "长石矿旧址矿区建筑与采矿设施（姜家垅）；矿洞、堆场与选矿遗迹待现场测绘",
        "湖北省属长石矿的采矿选矿工艺与县域非金属矿开发史",
        "通城长石矿职工与矿区集镇记忆",
        "以历史建筑身份纳入保护体系；停产年代与矿权现状待核",
        "直接取自通城县2022年历史建筑认定公示名单（A级，智能体核读原文）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["湖北省长石矿"],
    ),
    _xn("HBI-XN-019", "关刀高冲公社", "通城县关刀镇高冲村", "工业社区",
        "通城县历史建筑（2022-03-22认定公示38处名录之列）", ["tongcheng_batches_2022_2024"], "industrial_social_site", "待核",
        "高冲公社建筑本体（关刀镇高冲村）；公社办公与公共活动空间格局待现场测绘",
        "人民公社基层治理建筑的保存样本",
        "高冲村公社集体化治理与生产生活记忆",
        "以历史建筑身份纳入保护体系；现状用途待核",
        "直接取自通城县2022年历史建筑认定公示名单（A级，智能体核读原文）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    _xn("HBI-XN-020", "沙堆九井峰茶场", "通城县沙堆镇沙堆村", "茶业生产与工业社区",
        "通城县历史建筑（2022-03-22认定公示38处名录之列）", ["tongcheng_batches_2022_2024"], "industrial_site", "待核",
        "九井峰茶场建筑与茶园（沙堆镇沙堆村）；制茶车间与厂房保存状态待现场测绘",
        "县域国营/集体茶场的种植—采摘—制茶生产链",
        "沙堆镇茶场职工与通城茶叶产业记忆",
        "以历史建筑身份纳入保护体系；茶场经营延续状态待核",
        "直接取自通城县2022年历史建筑认定公示名单（A级，智能体核读原文）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["九井峰茶场"],
    ),
    _xn("HBI-XN-021", "石家渡槽", "通城县北港镇桂家村一组", "水利工程与泵站",
        "通城县历史建筑（2024年5月20日“百日行动”认定公示52处名录之列，名录载约100年以上）", ["tongcheng_batches_2022_2024"], "industrial_utility_site", "约100年以上",
        "石家渡槽本体（桂家村一组）；跨度、结构形式与保存状态待现场测绘",
        "山区引水灌溉渡槽工艺（名录载约100年以上，早于集体化高潮期的稀有早期渡槽）",
        "通城北港灌区农业灌溉记忆",
        "以历史建筑身份纳入保护体系；在用/停用状态待核",
        "直接取自通城县2024年“百日行动”认定公示附件PDF（A级，智能体核读）；名录载年代约100年以上；坐标未核验保持待核。",
        [],
    ),
    _xn("HBI-XN-022", "永逸闸", "嘉鱼县鱼岳镇木鱼山东护城干堤桩号298+600", "水利工程与泵站",
        "嘉鱼县第一批历史建筑保护名单（2023-05-26成文公布，11处之列）", ["jiayu_heritage_2023_2024"], "industrial_utility_site", "待核",
        "水闸建筑本体（护城干堤）；闸孔规模、启闭设施与闸体结构待现场测绘",
        "长江干堤护城水闸的排灌调蓄工艺",
        "嘉鱼县城防洪排涝与水闸值守记忆",
        "以第一批历史建筑身份正式公布保护；在用状态待水利部门核",
        "直接取自嘉鱼县政府第一批历史建筑保护名单PDF（A级，智能体完整核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    _xn("HBI-XN-023", "八斗渡槽", "嘉鱼县高铁岭镇九龙村下屋孙家至石塘村", "水利工程与泵站",
        "嘉鱼县第一批历史建筑保护名单（2023-05-26成文公布，11处之列）", ["jiayu_heritage_2023_2024"], "industrial_utility_site", "待核",
        "渡槽本体（横跨大岩畈）；跨度与结构待现场测绘",
        "丘陵灌区渡槽输水工艺，与麻城/孝感/利川/通城渡槽群同谱系",
        "嘉鱼丘陵灌区农业灌溉记忆",
        "以第一批历史建筑身份正式公布保护；在用/停用状态待核",
        "直接取自嘉鱼县政府第一批历史建筑保护名单PDF（A级，智能体完整核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    _xn("HBI-XN-024", "崇阳县刘家渡槽", "咸宁市崇阳县（路口镇或白霓镇，分布待核）", "水利工程与泵站",
        "崇阳县第一批历史建筑（2024年挂牌保护20处之一，媒体核读）", ["chongyang_liujia_2024"], "industrial_utility_site", "待核",
        "刘家渡槽本体；跨度与结构待现场测绘",
        "山区引水灌溉渡槽工艺",
        "崇阳灌区农业灌溉与水利建设记忆",
        "以第一批历史建筑身份挂牌保护（媒体核读，政府网正式通知原文未检索到）；在用/停用状态待核",
        "媒体核读（B级），崇阳县政府网无正式通知原文——政府网正式公布文件待查；坐标未核验保持待核。",
        [],
    ),
    _jl("HBI-JZ-067", "监利粮站粮库群（白螺镇粮站、余埠粮管所、严场粮库、莲台粮库、红瓦仓库）", "监利市白螺镇、黄歇口镇、汪桥镇、毛市镇", "粮食仓储工业",
        "industrial_storage_site", "待核",
        "5处粮站/粮管所/粮库/仓库：白螺镇粮站、黄歇口镇余埠粮管所、汪桥镇严场粮库、汪桥镇莲台粮库、毛市镇红瓦仓库；各处仓房型制与保存状态待现场测绘",
        "监利（全国产粮大县）县域粮站—粮管所两级粮食储运网络标本",
        "监利粮农售粮与粮站职工的统购统销记忆",
        "30处已与产权人签订保护协议并进入市政府公布程序（2024年6月）；在用/停用状态待核",
        "直接取自监利市住建局认定公示（A级，智能体核读原文）；5处合并记录以保持县域粮储网络完整；坐标未核验保持待核。",
        ["白螺镇粮站", "余埠粮管所", "严场粮库", "莲台粮库", "红瓦仓库"],
    ),
    _jl("HBI-JZ-068", "毛市镇砖瓦厂渡口", "监利市毛市镇", "工业仓储与运输",
        "industrial_transport_site", "待核",
        "砖瓦厂配套渡口设施；渡口形制与使用状态待现场测绘",
        "砖瓦厂产品水路外运的配套渡口运输节点",
        "毛市镇砖瓦生产与水路运输记忆",
        "以市级历史建筑身份纳入保护体系；渡口使用状态待核",
        "直接取自监利市住建局认定公示（A级，智能体核读原文）；工业运输配套遗存类型在底册为首例；坐标未核验保持待核。",
        [],
    ),
    {
        "inventory_id": "HBI-JZ-069",
        "name": "乌林粮管所仓库",
        "city": "荆州市",
        "district_county": "洪湖市乌林镇黄蓬老街",
        "industry_category_l1": "粮食仓储工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "洪湖市第二批历史建筑（洪政函〔2023〕14号，2023-04-19公布，11处之一；1968年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["honghu_batch2_2023"],
        "cultural_evidence": {
            "material_carriers": "粮管所仓库建筑本体（1090平方米，黄蓬老街）；仓房型制与保存状态待现场测绘",
            "technical_memory": "县域粮食收储仓库建筑，后为叶家门国家粮库乌林收购点——公社粮仓到国家粮库收购点的功能演变",
            "social_memory": "乌林镇粮储职工与黄蓬老街粮食收购记忆（名录载其“功能特殊，具有一定标志性”）",
            "current_use_or_loss": "以第二批历史建筑身份正式公布保护；在用/停用状态待核",
        },
        "notes": "直接取自洪政函〔2023〕14号名录全表（A级，智能体核读原文）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["乌林粮管所"],
        "asset_kind": "industrial_storage_site",
    },
]


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    for key, source in SOURCES.items():
        if key in sources and sources[key] != source:
            sources[key] = source
    sources.update(SOURCES)
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
    # 八燕渡槽补强（通城2022名录关刀八燕渡槽与省保八燕渡槽同一对象）
    xn002 = next((row for row in records if row["inventory_id"] == "HBI-XN-002"), None)
    if xn002 is None:
        raise SystemExit("record not found: HBI-XN-002")
    note_add = "2026-10-05通城县2022年历史建筑认定公示名单（A级）亦列“关刀八燕渡槽”（关刀镇八燕村），与本条省保八燕渡槽为同一对象的不同批次认定，县保/省保层级沿革互证。"
    if note_add not in xn002["notes"]:
        xn002["notes"] = xn002["notes"] + note_add
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_cr_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
