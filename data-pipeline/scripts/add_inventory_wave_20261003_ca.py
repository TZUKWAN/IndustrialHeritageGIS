from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "shishou_heritage_batch1_2022": {
        "source_type": "county_city_government_notice",
        "title": "石首市人民政府关于公布我市历史建筑的通知（石政函〔2022〕43号，11处）及市住建局认定公示附件详情",
        "org": "石首市人民政府门户网站（政府信息公开平台）",
        "pub_date": "2022-12-19",
        "url": "http://zwgk.shishou.gov.cn/32823/202212/t20221219/247410.shtml",
        "authority": "A",
        "notes": "石政函〔2022〕43号公布11处历史建筑（公示2022-12-05，http://zwgk.shishou.gov.cn/38400/202212/t20221205/244538.shtml）；附件《石首市拟公布的历史建筑详细情况》PDF（18页）已下载OCR，逐处含地址/面积/年代/沿革：调关缝纫社旧址（调关镇解放大道西段北街，房屋1930年代，缝纫社50年代创办职工32人，90年代中解散，215.84㎡）、调关粮管所旧址（希望路段西片132号，50年代建，1986年停运，529.29㎡，粮库7栋存万吨，70-80年代职工230余人）、调关三机械厂旧址（解放大道东街，1962年调关机电社起家，1972年更名石首县第三机械厂，地方国营，1995年产值340万元/职工130人）、焦山河粮站仓库（东升镇焦山河社区15组，1958年苏联援建项目，1092.25㎡砖木结构）、天鹅洲新码头粮库（天鹅洲开发区新堤村一组，1972年3月，3个圆顶仓+1平房仓，736.41㎡）、卫星大队大礼堂（高陵镇三字岗村，1971年10月，约700㎡）、拦河坝大礼堂（横沟市镇拦河坝村，70年代，643.57㎡砖混）、团山寺镇大礼堂旧址（解放路125号，约1972年，616.81㎡，现租用为美莎克服装厂厂房）。",
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


def _jz(record_id: str, name: str, dc: str, cat: str, no: str, src: list, kind: str, year: str, material: str, tech: str, social: str, use: str, notes: str, aliases: list) -> dict:
    return {
        "inventory_id": record_id,
        "name": name,
        "city": "荆州市",
        "district_county": dc,
        "industry_category_l1": cat,
        "recognition_level": "municipal_historical_building",
        "recognition_status": f"石首市历史建筑（{no}）",
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
    _jz("HBI-JZ-045", "调关缝纫社旧址", "石首市调关镇解放大道西段北街", "服装与纺织工业", "石政函〔2022〕43号名录（缝纫社50年代创办，90年代中解散）",
        ["shishou_heritage_batch1_2022"], "industrial_building", "房屋1930年代",
        "缝纫社旧址建筑（215.84平方米，职工32人）；缝纫设备无存证",
        "集体缝纫社的服装来料加工与统购统销经营形制",
        "调关镇缝纫社女职工与集镇成衣消费记忆",
        "90年代中解散后房屋留存；以市级历史建筑身份纳入保护体系，现状用途待核",
        "直接取自石政函〔2022〕43号附件详情PDF（A级，已下载OCR逐处核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    _jz("HBI-JZ-046", "调关粮管所旧址", "石首市调关镇希望路段西片132号", "粮食仓储工业", "石政函〔2022〕43号名录（50年代建，1986年停运）",
        ["shishou_heritage_batch1_2022"], "industrial_storage_site", "50年代",
        "粮管所旧址（529.29平方米），粮库7栋、仓储能力约万吨；建筑保存状况待现场测绘",
        "区乡粮管所的收购、储存、调运体系，计划经济粮食统购统销的基层节点",
        "调关镇粮管所职工230余人（70-80年代）与四乡售粮农民记忆",
        "1986年停运；以市级历史建筑身份纳入保护体系，现状用途待核",
        "直接取自石政函〔2022〕43号附件详情PDF（A级，OCR核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["调关粮管所"],
    ),
    _jz("HBI-JZ-047", "调关三机械厂旧址", "石首市调关镇解放大道东街", "机械制造工业", "石政函〔2022〕43号名录（1962年调关机电社起家，1972年更名石首县第三机械厂）",
        ["shishou_heritage_batch1_2022"], "industrial_building", "1962年（机电社起家）",
        "三机械厂旧址厂房；机床设备无存证，厂房保存状况待现场测绘",
        "从乡镇机电社到地方国营机械厂的升级脉络（1995年产值340万元、职工130人）",
        "三机械厂职工与调关镇机械工业记忆",
        "以市级历史建筑身份纳入保护体系；停产年代与现状用途待核",
        "直接取自石政函〔2022〕43号附件详情PDF（A级，OCR核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["石首县第三机械厂", "调关机电社"],
    ),
    _jz("HBI-JZ-048", "焦山河粮站仓库", "石首市东升镇焦山河社区15组", "粮食仓储工业", "石政函〔2022〕43号名录（1958年，苏联援建项目）",
        ["shishou_heritage_batch1_2022"], "industrial_storage_site", "1958年",
        "粮站仓库（1092.25平方米，砖木结构）；保存状况待现场测绘",
        "1958年苏联援建背景的粮站仓储建筑，砖木结构大跨度仓房工艺",
        "焦山河粮站统购统销时期四乡售粮记忆",
        "以市级历史建筑身份纳入保护体系；在用/停用状态待核",
        "直接取自石政函〔2022〕43号附件详情PDF（A级，OCR核读，“苏联援建项目”表述引自名录简介）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["焦山河粮站"],
    ),
    _jz("HBI-JZ-049", "天鹅洲新码头粮库（圆顶仓群）", "石首市天鹅洲开发区新堤村一组", "粮食仓储工业", "石政函〔2022〕43号名录（1972年3月建）",
        ["shishou_heritage_batch1_2022"], "industrial_storage_site", "1972年",
        "粮库3个圆顶仓+1栋平房仓（736.41平方米）；圆顶仓形制与保存状态待现场测绘",
        "圆顶仓（穹顶粮仓）仓储工艺，1970年代粮仓建设的典型形制",
        "天鹅洲垦区粮储与农场记忆",
        "以市级历史建筑身份纳入保护体系；在用/停用状态待核",
        "直接取自石政函〔2022〕43号附件详情PDF（A级，OCR核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    _jz("HBI-JZ-050", "卫星大队大礼堂", "石首市高陵镇三字岗村", "工业社区", "石政函〔2022〕43号名录（1971年10月建）",
        ["shishou_heritage_batch1_2022"], "industrial_social_site", "1971年",
        "大队大礼堂（约700平方米）；保存状况待现场测绘",
        "生产大队礼堂的集会、文艺与农副加工分配功能空间形制",
        "卫星大队集体劳动、开会与文艺活动记忆",
        "以市级历史建筑身份纳入保护体系；现状用途待核",
        "直接取自石政函〔2022〕43号附件详情PDF（A级，OCR核读）；收录角度为其大队工业社区属性；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    _jz("HBI-JZ-051", "拦河坝大礼堂", "石首市横沟市镇拦河坝村", "工业社区", "石政函〔2022〕43号名录（70年代建）",
        ["shishou_heritage_batch1_2022"], "industrial_social_site", "70年代",
        "大队/生产队礼堂（643.57平方米，砖混结构）；保存状况待现场测绘",
        "70年代砖混结构礼堂的建筑工艺",
        "拦河坝村集体集会与分配记忆",
        "以市级历史建筑身份纳入保护体系；现状用途待核",
        "直接取自石政函〔2022〕43号附件详情PDF（A级，OCR核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    _jz("HBI-JZ-052", "团山寺镇大礼堂旧址（现服装厂厂房）", "石首市团山寺镇解放路125号", "工业社区", "石政函〔2022〕43号名录（约1972年建）",
        ["shishou_heritage_batch1_2022"], "industrial_social_site", "约1972年",
        "大礼堂旧址（616.81平方米），现租用为美莎克服装厂厂房——礼堂空间活态工业利用",
        "礼堂大空间结构承接现代服装生产的空间再利用样本",
        "团山寺镇集体集会记忆与当代服装生产叠合",
        "以市级历史建筑身份纳入保护体系；租用关系与工业生产现状待核",
        "直接取自石政函〔2022〕43号附件详情PDF（A级，OCR核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    _jz("HBI-JZ-053", "新厂粮库建筑群（6栋）", "石首市新厂镇", "粮食仓储工业", "石政函〔2024〕12号名录（新厂粮库6栋）",
        ["shishou_heritage_batch2_2024"], "industrial_storage_site", "未详（名录未载）",
        "新厂粮库6栋仓房；栋型与保存状态待现场测绘",
        "新厂镇为石首江北粮棉集散重镇，粮库群体现区域仓储布局",
        "新厂镇粮储职工与江北粮棉集散记忆",
        "以市级历史建筑身份纳入保护体系；在用/停用状态待核",
        "直接取自石政函〔2024〕12号名录扫描件（A级，OCR核对）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    _jz("HBI-JZ-054", "焦山河粮库建筑群（6栋）", "石首市东升镇焦山河社区", "粮食仓储工业", "石政函〔2024〕12号名录（焦山河粮库6栋）",
        ["shishou_heritage_batch2_2024"], "industrial_storage_site", "未详（名录未载）",
        "焦山河粮库6栋仓房；与 HBI-JZ-048 焦山河粮站仓库（1958年）的组团关系待现场核验",
        "焦山河片区粮站+粮库的组合仓储体系",
        "焦山河粮储职工记忆",
        "以市级历史建筑身份纳入保护体系；在用/停用状态待核",
        "直接取自石政函〔2024〕12号名录扫描件（A级，OCR核对）；与1958年粮站仓库的先后沿革待核；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    _jz("HBI-JZ-055", "梅田湖供销社", "石首市梅田湖镇", "供销商贸与基层物资供应", "石政函〔2024〕12号名录（梅田湖供销社）",
        ["shishou_heritage_batch2_2024"], "industrial_trade_site", "未详（名录未载）",
        "供销社建筑本体；门面与柜台格局待现场测绘",
        "基层供销社的商品供应与农资回收功能形制",
        "梅田湖镇供销社购物记忆",
        "以市级历史建筑身份纳入保护体系；现状用途待核",
        "直接取自石政函〔2024〕12号名录扫描件（A级，OCR核对）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    _jz("HBI-JZ-056", "石首历史建筑水塔群（新风水塔、新厂供销社水塔、江波渡老水塔、高基庙老水厂塔）", "石首市新厂镇、江波渡、高基庙镇", "城镇供水基础设施", "石政函〔2024〕12号名录（新风水塔、新厂供销社水塔、江波渡老水塔、高基庙老水厂塔）",
        ["shishou_heritage_batch2_2024"], "industrial_utility_site", "未详（名录未载）",
        "4处水塔构筑物（新风水塔、新厂供销社水塔、江波渡老水塔、高基庙老水厂塔）；高度与保存状态待现场测绘",
        "石首乡镇供水体系的水塔群，集中供水时代的基础设施标本",
        "各集镇居民饮水与供水站值守记忆",
        "以市级历史建筑身份纳入保护体系；在用/退役状态待核",
        "直接取自石政函〔2024〕12号名录扫描件（A级，OCR核对）；4处合并记录以保持乡镇供水遗存群组完整；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["新风水塔", "新厂供销社水塔", "江波渡老水塔", "高基庙老水厂塔"],
    ),
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
    print(f"wave_ca_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
