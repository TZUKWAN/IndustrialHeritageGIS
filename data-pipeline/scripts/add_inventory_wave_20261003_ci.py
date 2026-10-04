from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "wuxue_batch_2024": {
        "source_type": "county_public_notice",
        "title": "关于武穴市2024年新增历史建筑名录的公示（29处，编号WXLSJZ023-051，名单xlsx）",
        "org": "武穴市住房和城乡建设局（武穴市人民政府网）",
        "pub_date": "2024-05-29",
        "url": "https://www.wuxue.gov.cn/zwgk/public/6636855/1376938.html",
        "authority": "A",
        "notes": "依鄂建〔2024〕423号“百日行动”公示29处（公示期2024-05-29至06-02），名单xlsx附件（https://www.wuxue.gov.cn/group2/M00/0D/EA/rBQOoGZWglWAAaEKAABDuEbrXVw38.xlsx）已下载解析：杨二岭渡桥（1958年，花桥镇杨二岭村，上层放水渡槽解决1100亩灌溉，渡槽至今仍在承担灌溉功能）、仙人坝渡槽（1961年，花桥镇戴文义村与仙人坝水库交界处，钢筋混凝土长156米，保障花桥、石佛寺两镇灌溉）、张富记古楼（1910年，龙坪镇下街商号/绒行，解放初曾作区公所）、万寿宫门楼（1980年左右重建，龙坪镇，江西商人会所→龙坪公社会场→电影院）等。编号自023起，存在编号001-022前批次名录待查。",
    },
    "xishui_batches_2022_2023": {
        "source_type": "county_public_notice",
        "title": "浠水县历史建筑第一批（城区3处，2022-07-28）与第二批（11处，2023-09-26至10-02）公示",
        "org": "浠水县住房和城乡建设局（浠水县人民政府网）",
        "pub_date": "2022-07-28",
        "url": "https://www.xishui.gov.cn/zwgk/public/6635866/678228.html",
        "authority": "A",
        "notes": "第一批公示（https://www.xishui.gov.cn/zwgk/public/6635866/678228.html）：浠水县人民会堂（1974年，清泉镇学堂路96号）、县政府办公楼（1978年）、县政协机关大楼（1993年）；第二批公示（https://www.xishui.gov.cn/zwgk/public/6636610/1028807.html，公示期2023-09-26至10-02）11处：清泉镇闫河村倒虹吸（1964年，水利设施）、蔡河镇供销社（1972年）、兰溪镇福星村圆拱石型养猪场（1970年，农业养殖设施）、汪岗镇前进村“大寨型”建筑村部（1974年）、蔡河镇政府礼堂（1982年）、闻一多纪念馆（1987年）、卷棚桥、青蒿港桥（1755年）等。",
    },
    "tuanfeng_batch3_2024": {
        "source_type": "county_public_notice",
        "title": "关于团风县第三批历史建筑的公示（20处，编号TFLSJZ018-037）",
        "org": "团风县住房和城乡建设局（团风县人民政府网）",
        "pub_date": "2024-05-08",
        "url": "http://www.tfzf.gov.cn/zwgk/public/6635206/1367264.html",
        "authority": "A",
        "notes": "第三批20处公示（公示期2024-05-08至15），类型以寺庙、祠堂、民居为主；时代性对象：严家咀大礼堂（70年代）、坎子湾礼堂（1970年）、夕阳冲礼堂（1973年）、眺云村大戏台（1980年）、薛坳村拱门（1975年）、瓦屋湾石拱桥（1976年）、邹冲村老拱桥（清）。",
    },
}


def _hg(record_id: str, name: str, dc: str, cat: str, status: str, src: list, kind: str, year: str, material: str, tech: str, social: str, use: str, notes: str, aliases: list) -> dict:
    return {
        "inventory_id": record_id,
        "name": name,
        "city": "黄冈市",
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


RECORDS = [
    _hg("HBI-HG-030", "武穴渡槽桥复合体（杨二岭渡桥、仙人坝渡槽）", "武穴市花桥镇", "水利工程与泵站",
        "武穴市2024年新增历史建筑名录（29处公示名单之列）", ["wuxue_batch_2024"], "industrial_utility_site", "1958/1961年",
        "2处渡槽桥复合体：杨二岭渡桥（1958年，上层为放水渡槽，解决1100亩灌溉，渡槽至今仍在承担灌溉功能，兼桥、渡槽、知青石屋复合形态）、仙人坝渡槽（1961年，钢筋混凝土，长156米，保障花桥、石佛寺两镇灌溉）",
        "桥上渡槽的立体复合水工构筑物工艺，1950年代末至60年代农田水利建设的活态遗存",
        "花桥镇灌区农业灌溉与渡槽建设者的代际记忆",
        "杨二岭渡槽至今仍在承担灌溉功能（活态水利遗产）；以市级历史建筑身份纳入保护体系",
        "直接取自武穴市2024年新增名录xlsx（A级，已下载解析）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["杨二岭渡桥", "仙人坝渡槽"],
    ),
    _hg("HBI-HG-031", "万寿宫门楼", "武穴市龙坪镇", "商贸服务与基层文化供应",
        "武穴市2024年新增历史建筑名录（29处公示名单之列）", ["wuxue_batch_2024"], "industrial_social_site", "1980年左右重建",
        "万寿宫门楼建筑本体（原江西商人会所，后为龙坪公社会场、电影院）；门楼形制与装饰待现场测绘",
        "江西商帮会馆→人民公社会场→电影院的建筑功能三段演变标本",
        "龙坪镇赣商贸易、集体集会与观影的多代公共记忆叠层",
        "以市级历史建筑身份纳入保护体系；现状用途待核",
        "直接取自武穴市2024年新增名录xlsx（A级，已下载解析）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["万寿宫"],
    ),
    _hg("HBI-HG-032", "张富记古楼", "武穴市龙坪镇下街", "商贸服务与基层文化供应",
        "武穴市2024年新增历史建筑名录（29处公示名单之列）", ["wuxue_batch_2024"], "industrial_trade_site", "1910年",
        "商号/绒行建筑本体（下街）；门面与作坊格局待现场测绘",
        "民国龙坪镇绒行商号的纺织原料贸易经营形制",
        "张富记商号与龙坪镇下街商贸记忆",
        "解放初曾作区公所；以市级历史建筑身份纳入保护体系，现状用途待核",
        "直接取自武穴市2024年新增名录xlsx（A级，已下载解析）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["张富记绒行"],
    ),
    _hg("HBI-HG-033", "清泉镇闫河村倒虹吸", "浠水县清泉镇闫河村", "水利工程与泵站",
        "浠水县第二批历史建筑公示（2023-09-26至10-02，11处之列）", ["xishui_batches_2022_2023"], "industrial_utility_site", "1964年",
        "倒虹吸水利构筑物（闫河村，1964年）；管径、长度与进出口高差待现场测绘",
        "倒虹吸利用虹吸原理实现渠道跨越低地的水工技术，与渡槽互为对偶的灌溉工程类型",
        "浠水灌区水利建设与渠道管护记忆",
        "以市级历史建筑身份纳入保护体系；在用/停用状态待核",
        "直接取自浠水县第二批历史建筑公示（A级）；倒虹吸类型在底册为首例；坐标未核验保持待核。",
        [],
    ),
    _hg("HBI-HG-034", "蔡河镇供销社", "浠水县蔡河镇", "供销商贸与基层物资供应",
        "浠水县第二批历史建筑公示（2023-09-26至10-02，11处之列）", ["xishui_batches_2022_2023"], "industrial_trade_site", "1972年",
        "供销社建筑本体；门面与柜台格局待现场测绘",
        "基层供销社的商品供应与农资回收功能形制",
        "蔡河镇供销社购物与农资供应记忆",
        "以市级历史建筑身份纳入保护体系；现状用途待核",
        "直接取自浠水县第二批历史建筑公示（A级）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    _hg("HBI-HG-035", "兰溪镇福星村圆拱石型养猪场", "浠水县兰溪镇福星村", "农业养殖设施",
        "浠水县第二批历史建筑公示（2023-09-26至10-02，11处之列）", ["xishui_batches_2022_2023"], "industrial_building", "1970年",
        "圆拱石型养猪场建筑本体（福星村，1970年）；拱跨与圈舍布局待现场测绘",
        "圆拱石型（石砌拱顶）集体养猪场建筑工艺，1970年代“养猪积肥”集体养殖设施标本",
        "生产队集体养猪与积肥运动记忆",
        "以市级历史建筑身份纳入保护体系；现状用途（废弃/转用）待核",
        "直接取自浠水县第二批历史建筑公示（A级）；养殖设施类型在底册为首例；坐标未核验保持待核。",
        [],
    ),
    _hg("HBI-HG-036", "团风礼堂群（严家咀、坎子湾、夕阳冲礼堂及眺云村大戏台）", "团风县（具体乡镇名录已载）", "工业社区",
        "团风县第三批历史建筑公示（2024-05-08至15，20处之列，编号TFLSJZ018-037内）", ["tuanfeng_batch3_2024"], "industrial_social_site", "1970/1973/1980年",
        "4处礼堂戏台：严家咀大礼堂（70年代）、坎子湾礼堂（1970年）、夕阳冲礼堂（1973年）、眺云村大戏台（1980年）；保存状况待现场测绘",
        "团风县集体化时期礼堂戏台的建筑形制组群",
        "团风乡村集会、演戏与电影放映的公共文化记忆",
        "以市级历史建筑身份纳入保护体系；现状用途待核",
        "直接取自团风县第三批历史建筑公示（A级）；4处合并记录以保持礼堂戏台组群完整；第二批13处水晶坳村民居为传统民居不属工业；坐标未核验保持待核。",
        ["严家咀大礼堂", "坎子湾礼堂", "夕阳冲礼堂", "眺云村大戏台"],
    ),
    _hg("HBI-HG-037", "麻城时代桥梁群（黄泥坳大桥、木子店一桥、风雨桥、张家湾汽车桥、黄土岗桥、燕窝地石拱桥）", "麻城市（各乡镇）", "内河交通与货运服务",
        "2024年麻城市历史文化建筑评审清单公示（30处之桥梁6座）", ["macheng_batch3_2024"], "industrial_transport_site", "1904-1979年",
        "6座时代桥梁：黄泥坳大桥（1965年）、木子店一桥（1978年）、风雨桥（1904/1964年）、张家湾汽车桥（1958年）、黄土岗桥（1979年）、燕窝地村石拱桥（1970年，“水利设施建筑实物资料”）；桥型与保存状态待现场测绘",
        "从传统石拱桥到公路桥的百年桥梁技术演进序列（集体化时期交通建设标本群）",
        "麻城山区交通通达与乡村 connectivity 记忆",
        "以评审清单公示层级纳入保护体系（正式公布待跟踪）；通行状态待核",
        "直接取自2024年评审清单xls（A级，已下载解析）；6座合并记录以保持桥梁技术演进序列完整；坐标未核验保持待核。",
        ["黄泥坳大桥", "风雨桥", "燕窝地石拱桥"],
    ),
    _hg("HBI-HG-038", "大庙公社食品所", "黄梅县大河镇", "食品加工工业",
        "黄梅县第三批历史建筑名录（2024-06-01，36处）", ["huangmei_batch3_2024"], "industrial_building", "1954年",
        "公社食品所建筑本体（大河镇，1954年）；屠宰加工与售肉柜台格局待现场测绘",
        "公社食品所的生猪统购统宰与定量供肉体系形制",
        "大河镇食品所职工与计划经济肉食供应记忆",
        "以第三批历史建筑身份正式公布保护；现状用途待核",
        "直接取自黄梅县政府第三批名录（A级）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    _hg("HBI-HG-039", "向蔡供销社老房", "黄梅县五祖镇向桥村", "供销商贸与基层物资供应",
        "黄梅县第三批历史建筑名录（2024-06-01，36处）", ["huangmei_batch3_2024"], "industrial_trade_site", "1960年左右",
        "供销社老房建筑本体（向桥村，1960年左右）；保存状态待现场测绘",
        "五祖山区基层供销网点的供应形制",
        "向蔡片区供销社购物与农资供应记忆",
        "以第三批历史建筑身份正式公布保护；现状用途待核",
        "直接取自黄梅县政府第三批名录（A级）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    _hg("HBI-HG-040", "黄梅县域公用事业旧址（苦竹供电所老办公楼、独山镇老银行）", "黄梅县苦竹乡、独山镇", "电力能源",
        "黄梅县第三批历史建筑名录（2024-06-01，36处）", ["huangmei_batch3_2024"], "industrial_utility_site", "1954/1982年",
        "2处公用事业建筑：苦竹供电所老办公楼（1982年，吕世贵村）、独山镇老银行（1954年）；结构与保存状态待现场测绘",
        "县域电力供应与农村金融的基层设施建筑组合",
        "乡镇电工、农金员与县域电气化、农村信用记忆",
        "以第三批历史建筑身份正式公布保护；现状用途待核",
        "直接取自黄梅县政府第三批名录（A级，智能体核读原文）；2处合并记录（电力+农村金融公用事业）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["苦竹供电所", "独山镇老银行"],
    ),
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
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_ci_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
