from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "zhijiang_integrated_2024": {
        "source_type": "county_government_notice",
        "title": "枝江市人民政府关于整合公布历史建筑名录的通知（枝府发〔2024〕2号，79处，编号1-79）",
        "org": "枝江市人民政府门户网站",
        "pub_date": "2024-04-19",
        "url": "http://www.zgzhijiang.gov.cn/zfxxgk/show.html?aid=9&id=223150&t=4",
        "authority": "A",
        "notes": "枝府发〔2024〕2号将2019年第一批5处、2021年第二批5处、2022年第三批4处及后续新增整合公布为79处（编号1-79）。工业对象（智能体核读原文）：No.12董市供销社（已入库HBI-YC-042）、No.30张涛然纺织厂（亮瓦亭）、No.42木板屋躲水楼（下街130号，明清）、No.48胡安汉踹坊、No.57毛氏苕粉作坊、No.63焦家磨坊、No.69老百纺公司、No.70五金公司江口门市部、No.71老搬运站（江口沿江路，解放初期，码头搬运）、No.73罗家港505哨所（1973年）、No.74罗家河血防桥、No.75罗家港大桥（1979年）、No.77同意大队综合厂（1963年）、No.79襄阳铁路分局旧址（安福寺镇紫荆岭社区，70年代）等。",
    },
    "zigui_batch1_gongshi_2020": {
        "source_type": "county_public_notice",
        "title": "关于对我县首批历史建筑名录的公示（7处，2020-11-16）",
        "org": "秭归县住房和城乡建设局（秭归县人民政府网）",
        "pub_date": "2020-11-16",
        "url": "http://www.hbzg.gov.cn/zfxxgk/show.html?aid=12&id=71956",
        "authority": "A",
        "notes": "秭归县首批7处历史建筑公示（智能体核读原文）：秭归厅屋院子聂氏老屋（归州镇向家湾村）、秭归桑坪公社时期建筑（水田坝乡姜家坡村四组）【公社时期建筑】、秭归向清和老屋（归州镇周家湾村）、秭归永乐水库（归州镇周家湾村）【水利】、风华屋场（磨坪乡一篮村五组）、谭家坡白屋（磨坪乡一篮村五组）、刘家岩栈道（磨坪乡银坪村三组）【交通遗产】。2026年新增7处（归州街片区门楼/影壁等，非工业）公示中。",
    },
    "changyang_batch3_notice_2024": {
        "source_type": "county_government_notice",
        "title": "长阳土家族自治县人民政府关于公布长阳土家族自治县第三批历史建筑名录的通知（长政发〔2024〕3号，38处）",
        "org": "长阳土家族自治县人民政府门户网站",
        "pub_date": "2024-06-26",
        "url": "http://www.changyang.gov.cn/zfxxgk/show.html?aid=13&id=223932&t=4",
        "authority": "A",
        "notes": "长政发〔2024〕3号公布38处完整名单（智能体核读原文），工业对象11处：王家棚信用社、邮政所旧址（龙舟坪镇王家棚村）、原沿头溪公社旧址、原马家坪粮站仓库一/二（大堰乡钟家湾村，已并入HBI-YC-041）、都镇湾镇供销合作社杨柘坪分店旧址、原璞岭大队榨坊旧址、原麻池人民公社旧址（已并入HBI-YC-041）、原曲溪公社旧址、渔峡口镇陶器厂遗址（已并入HBI-YC-041）、渔峡口镇供销社龙池分店旧址、原武钢职工宿舍石头屋（火烧坪乡青树包村）。",
    },
}


def _yc(record_id: str, name: str, dc: str, cat: str, kind: str, year: str, material: str, tech: str, social: str, use: str, notes: str, aliases: list, src: list) -> dict:
    return {
        "inventory_id": record_id,
        "name": name,
        "city": "宜昌市",
        "district_county": dc,
        "industry_category_l1": cat,
        "recognition_level": "municipal_historical_building",
        "recognition_status": "枝江市历史建筑（枝府发〔2024〕2号整合名录79处之列）",
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
    _yc("HBI-YC-059", "老搬运站", "枝江市江口镇沿江路", "货运搬运与仓储服务", "industrial_transport_site", "解放初期",
        "老搬运站建筑本体（江口沿江路）；站房与货场格局待现场测绘",
        "解放初期码头搬运行业的基层组织建筑，江口港货运装卸的组织中枢",
        "江口港搬运工人（俗称“扁担帮”）集体劳动记忆",
        "以市级历史建筑身份纳入保护体系；现状用途待核",
        "直接取自枝府发〔2024〕2号整合名录第71项（A级，智能体核读原文）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["江口搬运站"],
        ["zhijiang_integrated_2024"],
    ),
    _yc("HBI-YC-060", "襄阳铁路分局旧址", "枝江市安福寺镇紫荆岭社区", "铁路交通工业", "industrial_transport_site", "70年代",
        "铁路分局旧址建筑本体（紫荆岭社区，70年代）；建筑规模与站场关联待现场测绘",
        "焦柳铁路沿线地区铁路管理机构旧址（襄阳铁路分局分支驻点），焦柳线1970年代建设史的地方节点",
        "铁路职工驻站工作与紫荆岭铁路社区记忆",
        "以市级历史建筑身份纳入保护体系；现状用途待核",
        "直接取自枝府发〔2024〕2号整合名录第79项（A级，智能体核读原文）；名录未载建筑明细；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["焦柳铁路紫荆岭站"],
        ["zhijiang_integrated_2024"],
    ),
    _yc("HBI-YC-061", "同意大队综合厂", "枝江市（大队属综合加工厂）", "综合工业", "industrial_building", "1963年",
        "大队综合厂厂房（1963年建）；加工门类与设备留存待现场测绘",
        "人民公社大队综合厂的多业经营模式（农副加工/五金/编织等）",
        "同意大队社员集体办厂与工分制生产记忆",
        "以市级历史建筑身份纳入保护体系；停产年代与现状用途待核",
        "直接取自枝府发〔2024〕2号整合名录（A级，智能体核读原文）；综合厂具体加工门类待地方志核验；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
        ["zhijiang_integrated_2024"],
    ),
    _yc("HBI-YC-062", "枝江纺织与踹布遗存（张涛然纺织厂亮瓦亭、胡安汉踹坊）", "枝江市（董市镇/江口镇）", "纺织工业", "industrial_building", "待核",
        "2处纺织加工遗存：张涛然纺织厂（亮瓦亭——亮瓦采光屋顶的纺织车间形制）、胡安汉踹坊（踹布整理作坊）；设备留存待现场测绘",
        "枝江棉纺织业的织布（亮瓦采光车间）与踹布整理（元宝石碾压）传统工艺",
        "枝江纺织工人与董市/江口棉布集散记忆",
        "以市级历史建筑身份纳入保护体系；现状用途待核",
        "直接取自枝府发〔2024〕2号整合名录（A级，智能体核读原文）；2处合并记录以保持纺织加工谱系；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["张涛然纺织厂", "胡安汉踹坊"],
        ["zhijiang_integrated_2024"],
    ),
    _yc("HBI-YC-063", "枝江食品加工作坊（毛氏苕粉作坊、焦家磨坊）", "枝江市", "食品加工工业", "industrial_building", "待核",
        "2处食品加工作坊：毛氏苕粉作坊（红薯淀粉粉丝制作）、焦家磨坊（粮食磨粉加工）；设备与作坊格局待现场测绘",
        "县域传统食品加工作坊的水磨/苕粉制作工艺",
        "枝江苕粉、面粉地方食品与作坊主家族经营记忆",
        "以市级历史建筑身份纳入保护体系；现状用途待核",
        "直接取自枝府发〔2024〕2号整合名录（A级，智能体核读原文）；2处合并记录；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["毛氏苕粉作坊", "焦家磨坊"],
        ["zhijiang_integrated_2024"],
    ),
    _yc("HBI-YC-064", "枝江百纺五金商贸遗存（老百纺公司、五金公司江口门市部）", "枝江市江口镇", "供销商贸与基层物资供应", "industrial_trade_site", "待核",
        "2处商贸建筑：老百纺公司、五金公司江口门市部；门面与仓储格局待现场测绘",
        "国营百纺公司与五金专业门市的商品流通业态",
        "枝江百货纺织品与五金商品供应的国营商业记忆",
        "以市级历史建筑身份纳入保护体系；现状用途待核",
        "直接取自枝府发〔2024〕2号整合名录（A级，智能体核读原文）；2处合并记录；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["老百纺公司", "五金公司江口门市部"],
        ["zhijiang_integrated_2024"],
    ),
    _yc("HBI-YC-065", "枝江木板屋躲水楼", "枝江市下街130号", "防洪水利构筑物", "industrial_utility_site", "明清",
        "木板屋躲水楼建筑（下街130号，明清）；躲水楼层构造与撤离通道形制待现场测绘",
        "长江洪泛区“躲水楼”建筑类型——洪水期居民携物上楼避洪的民居防洪智慧（枝江沿江特有建筑类型）",
        "枝江沿江居民世代避洪迁居的水患记忆",
        "以市级历史建筑身份纳入保护体系；建筑保存与展示待核",
        "直接取自枝府发〔2024〕2号整合名录（A级，智能体核读原文）；躲水楼为长江洪泛区特有建筑类型，底册首例；坐标未核验保持待核。",
        ["躲水楼"],
        ["zhijiang_integrated_2024"],
    ),
    {
        "inventory_id": "HBI-YC-066",
        "name": "秭归桑坪公社时期建筑",
        "city": "宜昌市",
        "district_county": "秭归县水田坝乡姜家坡村四组",
        "industry_category_l1": "工业社区",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "秭归县首批历史建筑（2020-11-16县住建局公示7处之一，2021年市政府汇总公布）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["zigui_batch1_gongshi_2020"],
        "cultural_evidence": {
            "material_carriers": "桑坪公社时期建筑本体（姜家坡村四组）；建筑形制与公社功能空间待现场测绘",
            "technical_memory": "人民公社时期基层治理与公共活动的建筑载体",
            "social_memory": "桑坪公社社员集体化生产生活记忆",
            "current_use_or_loss": "以首批历史建筑身份纳入保护体系（秭归县政府正式公布通知未检索到，以县住建局公示为准）；现状用途待核",
        },
        "notes": "直接取自秭归县住建局首批历史建筑公示（A级，智能体核读原文）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["桑坪公社"],
        "asset_kind": "industrial_social_site",
    },
    {
        "inventory_id": "HBI-YC-067",
        "name": "秭归永乐水库",
        "city": "宜昌市",
        "district_county": "秭归县归州镇周家湾村",
        "industry_category_l1": "水利工程与泵站",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "秭归县首批历史建筑（2020-11-16县住建局公示7处之一，2021年市政府汇总公布）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["zigui_batch1_gongshi_2020"],
        "cultural_evidence": {
            "material_carriers": "永乐水库大坝与灌溉设施（周家湾村）；坝型、库容与灌溉范围待水利部门资料核补",
            "technical_memory": "峡江山地水库蓄水灌溉工程的建设工艺",
            "social_memory": "归州镇水利建设与农田灌溉集体记忆",
            "current_use_or_loss": "以首批历史建筑身份纳入保护体系；水库运行状态待水利部门核",
        },
        "notes": "直接取自秭归县住建局首批历史建筑公示（A级，智能体核读原文）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_utility_site",
    },
    {
        "inventory_id": "HBI-YC-068",
        "name": "武钢职工宿舍石头屋",
        "city": "宜昌市",
        "district_county": "长阳土家族自治县火烧坪乡青树包村",
        "industry_category_l1": "矿山采选工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "长阳土家族自治县第三批历史建筑（长政发〔2024〕3号，2024-06-26公布，38处之列）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["changyang_batch3_notice_2024"],
        "cultural_evidence": {
            "material_carriers": "武钢职工宿舍石头屋建筑本体（青树包村）；石砌工艺与内部格局待现场测绘",
            "technical_memory": "武钢（武汉钢铁集团）在长阳火烧坪矿区开采矿石的职工生活配套建筑，石砌墙体适应高山气候的营造工艺",
            "social_memory": "武钢矿山开采期职工驻矿生活记忆；火烧坪为武钢矿石原料供应地之一",
            "current_use_or_loss": "以第三批历史建筑身份正式公布保护；现状用途待核",
        },
        "notes": "直接取自长政发〔2024〕3号第三批名录（A级，智能体核读原文）；武钢在长阳的具体矿山名称与开采年代待档案核验；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["火烧坪武钢宿舍"],
        "asset_kind": "industrial_residential_landscape",
    },
    {
        "inventory_id": "HBI-YC-069",
        "name": "长阳第三批供销金融与公社遗存（王家棚信用社邮政所、沿头溪公社、都镇湾供销社杨柘坪分店、璞岭大队榨坊、曲溪公社、渔峡口供销社龙池分店）",
        "city": "宜昌市",
        "district_county": "长阳土家族自治县（龙舟坪镇、大堰乡、都镇湾镇等）",
        "industry_category_l1": "供销商贸与基层物资供应",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "长阳土家族自治县第三批历史建筑（长政发〔2024〕3号，2024-06-26公布，38处之列）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["changyang_batch3_notice_2024"],
        "cultural_evidence": {
            "material_carriers": "6处遗存：王家棚信用社、邮政所旧址（龙舟坪镇王家棚村）、原沿头溪公社旧址、都镇湾镇供销合作社杨柘坪分店旧址、原璞岭大队榨坊旧址、原曲溪公社旧址、渔峡口镇供销社龙池分店旧址；保存状态待现场测绘",
            "technical_memory": "县域基层信用社、邮政所、供销社分店、公社治理与大队榨坊的组合遗存——长阳山区基层经济服务网络标本",
            "social_memory": "山区供销购物、邮政汇兑、信用存贷与公社榨坊生产的组合记忆",
            "current_use_or_loss": "以第三批历史建筑身份正式公布保护；现状用途待核",
        },
        "notes": "直接取自长政发〔2024〕3号第三批名录（A级，智能体核读原文）；6处合并记录以保持基层经济服务网络完整；榨坊为油料加工遗存可细究；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["王家棚信用社", "沿头溪公社", "杨柘坪分店", "璞岭大队榨坊", "曲溪公社", "龙池分店"],
        "asset_kind": "industrial_trade_site",
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
    print(f"wave_cs_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
