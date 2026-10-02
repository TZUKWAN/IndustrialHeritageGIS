from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "lichuan_heritage_2024": {
        "source_type": "county_city_government_public_notice",
        "title": "利川市新增历史建筑公示（32处，鄂建〔2024〕423号“百日行动”批次，含利川第一批15处累计47处）",
        "org": "利川市人民政府门户网站（市住建局）",
        "pub_date": "2024-05-21",
        "url": "http://www.lichuan.gov.cn/xxgk/dfbmptlj/sz/szjj/ldjj/zjj004_/qtgk/202405/t20240521_1579551.shtml",
        "authority": "A",
        "notes": "公示名单载明（智能体核读原文）：No.20火电厂一号烟囱（1970年）、No.21火电厂二号烟囱（1980年），均在汪营镇齐跃桥村，备注“上世纪六十年代与七十年代……州市国营水泥厂、煤厂、火电厂、钢厂、焦化厂等建筑群……记录着民族工业走过的光辉岁月”；No.7“60公社供销社”（1959年，凉雾乡诸天村，公社时期标志性建筑）；No.2天桥（1958年灌溉水渠，建南镇）；No.6容貌坪大队办公室（1966-67年，内设卫生室和加工房）。公示层级，正式公布待跟踪。",
    },
    "xuanen_heritage_2023_2024": {
        "source_type": "county_city_government_public_notice",
        "title": "宣恩县历史建筑公示（2023年拟确定18处）与2024年拟新增历史建筑统计表（30处）",
        "org": "宣恩县人民政府门户网站",
        "pub_date": "2023-06-06",
        "url": "http://www.xe.gov.cn/xxgk/gkml/qtzdgknr/tzgg/202306/t20230606_1449845.shtml",
        "authority": "A",
        "notes": "2023年公示18处附件doc已解析（智能体核读）：含上湖塘社区综合厂厂房（上世纪90年代，“我县保存最完整的厂房”）、工农街粮食局老办公楼（一楼为粮食仓库，仿苏建筑）；2024年统计表（http://www.xe.gov.cn/xxgk/gkml/qtzdgknr/tzgg/202404/t20240418_1570379.shtml）30处含沙道沟镇姚家寨仓库（60年代初生产大队粮仓，石木结构）。均为公示/统计表层级，正式公布文件未检索到，待跟踪。",
    },
    "hefeng_heritage_2023_2024": {
        "source_type": "county_city_government_notice",
        "title": "鹤峰县第一批（11处，2023-01-08）、第二批（31处，2024-05-06）历史建筑公布通知",
        "org": "鹤峰县人民政府门户网站",
        "pub_date": "2023-01-08",
        "url": "http://www.hefeng.gov.cn/xxgk/gkml/shgysy/ggwhfw/fwxxy/202405/t20240513_1576905.shtml",
        "authority": "A",
        "notes": "第一批通知正文名录（第二批通知 http://www.hefeng.gov.cn/xxgk/gkml/shgysy/ggwhfw/fwxxy/202405/t20240513_1576910.shtml，附件doc已解析）：第一批第1项关口石拱桥（清康熙十三年，太平镇，茶马古道必经）、第2项刘公桥（光绪十三年，走马镇，“万里茶道”干道）、第11项石龙街驿站（燕子镇，四合天井，客栈+运茶骡马道）——茶马古道/万里茶道交通驿运遗产；第二批31处为桥梁、民居、旧址等。",
    },
    "enshi_zjw_428_2026": {
        "source_type": "prefecture_government_information",
        "title": "恩施州住房和城市更新局政协提案会办意见（全州428处历史建筑确权挂牌）",
        "org": "恩施州住房和城市更新局",
        "pub_date": "2026-07-14",
        "url": "http://zjw.enshi.gov.cn/xxgk/fdzdgk/qtzdgk/jytablj/202607/t20260714_1819620.shtml",
        "authority": "A",
        "notes": "会办意见原文载明“完成全州428处历史建筑确权挂牌，挂牌覆盖率达到100%”；并载恩施1988街区改造老旧厂房3.2万平方米（即恩施市烟叶复烤厂厂房旧址活化）。州住建局“县市联播”另有建始老电厂改造“和美小镇”、利川原复烤仓储基地38米烟囱改造“温度计”等工业遗产再利用报道（活化项目参照线索，暂不入库）。",
    },
}


RECORDS = [
    {
        "inventory_id": "HBI-ES-024",
        "name": "汪营镇火电厂烟囱（一号、二号）",
        "city": "恩施州",
        "district_county": "利川市汪营镇齐跃桥村",
        "industry_category_l1": "火力发电",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "利川市新增历史建筑（2024年5月公示，名录No.20、21；一号1970年、二号1980年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["lichuan_heritage_2024"],
        "cultural_evidence": {
            "material_carriers": "火电厂烟囱两座（一号1970年、二号1980年，汪营镇齐跃桥村）；公示备注载同场地原有州市国营水泥厂、煤厂、火电厂、钢厂、焦化厂等建筑群；烟囱高度与保存状态待现场测绘",
            "technical_memory": "利川县域火力发电与“五小工业”建设时期的动力设施遗存，建筑群备注记录民族工业发展历程",
            "social_memory": "汪营工业区职工与县域工业化记忆",
            "current_use_or_loss": "公示拟确定为历史建筑（公示层级，正式公布待跟踪）；电厂停产年代与烟囱在用状态待核",
        },
        "notes": "直接取自利川市政府网新增历史建筑公示名单（A级，智能体核读原文）；公示层级不等于正式公布；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["利川汪营火电厂"],
        "asset_kind": "industrial_utility_site",
    },
    {
        "inventory_id": "HBI-ES-025",
        "name": "凉雾乡60公社供销社",
        "city": "恩施州",
        "district_county": "利川市凉雾乡诸天村",
        "industry_category_l1": "供销商贸与基层物资供应",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "利川市新增历史建筑（2024年5月公示，名录No.7；1959年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["lichuan_heritage_2024"],
        "cultural_evidence": {
            "material_carriers": "公社供销社建筑本体（诸天村，1959年）；公示备注称其为公社时期标志性建筑；面积与形制待现场测绘",
            "technical_memory": "人民公社时期基层供销合作商业的建筑形制与商品供应体系",
            "social_memory": "公社社员凭票供应与赶集购销的集体记忆",
            "current_use_or_loss": "公示拟确定为历史建筑（公示层级，正式公布待跟踪）；现状用途待核",
        },
        "notes": "直接取自利川市政府网新增历史建筑公示名单（A级，智能体核读原文）；与天门/襄阳供销社记录同为基层商贸遗存模式；公示层级；坐标未核验保持待核。",
        "aliases": ["60公社供销社"],
        "asset_kind": "industrial_trade_site",
    },
    {
        "inventory_id": "HBI-ES-026",
        "name": "建南天桥（灌溉水渠）",
        "city": "恩施州",
        "district_county": "利川市建南镇",
        "industry_category_l1": "水利工程与泵站",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "利川市新增历史建筑（2024年5月公示，名录No.2；1958年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["lichuan_heritage_2024"],
        "cultural_evidence": {
            "material_carriers": "灌溉水渠天桥（建南镇，1958年）；跨度、高度与结构待现场测绘",
            "technical_memory": "1958年农田水利建设高潮时期的引水灌溉渡槽/水渠工艺，与底册孝感渡槽系列同谱系",
            "social_memory": "灌区农业灌溉与水利建设集体记忆",
            "current_use_or_loss": "公示拟确定为历史建筑（公示层级，正式公布待跟踪）；在用/停用状态待核",
        },
        "notes": "直接取自利川市政府网新增历史建筑公示名单（A级，智能体核读原文）；公示层级；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_utility_site",
    },
    {
        "inventory_id": "HBI-ES-027",
        "name": "容貌坪大队办公室（含加工房）",
        "city": "恩施州",
        "district_county": "利川市建南镇",
        "industry_category_l1": "工业社区",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "利川市新增历史建筑（2024年5月公示，名录No.6；1966-67年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["lichuan_heritage_2024"],
        "cultural_evidence": {
            "material_carriers": "大队办公室建筑本体（内设卫生室和加工房）；面积与保存状态待现场测绘",
            "technical_memory": "人民公社大队综合办公与农副加工一体化的功能布局",
            "social_memory": "大队治理、合作医疗与农副加工的集体记忆",
            "current_use_or_loss": "公示拟确定为历史建筑（公示层级，正式公布待跟踪）；现状用途待核",
        },
        "notes": "直接取自利川市政府网新增历史建筑公示名单（A级，智能体核读原文）；收录角度为其加工房生产性构成与大队工业社区属性；公示层级；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_social_site",
    },
    {
        "inventory_id": "HBI-ES-028",
        "name": "宣恩上湖塘综合厂厂房",
        "city": "恩施州",
        "district_county": "宣恩县珠山镇上湖塘社区",
        "industry_category_l1": "综合工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "宣恩县历史建筑拟确定对象（2023年6月公示18处之一；公示称“我县保存最完整的厂房”；90年代建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["xuanen_heritage_2023_2024"],
        "cultural_evidence": {
            "material_carriers": "综合厂厂房建筑本体（上湖塘社区，90年代）；生产行业、面积与设备留存待现场测绘与档案核验",
            "technical_memory": "县域综合厂（多业经营集体企业）的厂房形制；宣恩保存最完整厂房的样本价值",
            "social_memory": "县城集体企业职工生产记忆",
            "current_use_or_loss": "公示拟确定为历史建筑（公示层级，正式公布文件未检索到，待跟踪）；现状用途待核",
        },
        "notes": "直接取自宣恩县政府网公示附件（A级，智能体解析doc）；综合厂生产行业未载明；公示层级；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_building",
    },
    {
        "inventory_id": "HBI-ES-029",
        "name": "宣恩工农街粮食局老办公楼（一楼粮仓）",
        "city": "恩施州",
        "district_county": "宣恩县珠山镇工农街",
        "industry_category_l1": "粮食仓储工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "宣恩县历史建筑拟确定对象（2023年6月公示18处之一；仿苏建筑，新中国成立初期）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["xuanen_heritage_2023_2024"],
        "cultural_evidence": {
            "material_carriers": "粮食局老办公楼（一楼为粮食仓库，仿苏建筑，新中国成立初期）；建筑面积与保存状态待现场测绘",
            "technical_memory": "县域粮食管理机构办公与仓储一体化的功能组合，仿苏建筑形制反映五十年代建设背景",
            "social_memory": "粮食统购统销时期县域粮政记忆",
            "current_use_or_loss": "公示拟确定为历史建筑（公示层级，正式公布文件未检索到，待跟踪）；现状用途待核",
        },
        "notes": "直接取自宣恩县政府网公示附件（A级，智能体解析doc）；公示层级；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_storage_site",
    },
    {
        "inventory_id": "HBI-ES-030",
        "name": "沙道沟镇姚家寨仓库",
        "city": "恩施州",
        "district_county": "宣恩县沙道沟镇",
        "industry_category_l1": "粮食仓储工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "宣恩县历史建筑拟新增对象（2024年4月统计表30处之No.20；60年代初建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["xuanen_heritage_2023_2024"],
        "cultural_evidence": {
            "material_carriers": "生产大队粮仓（石木结构，60年代初）；仓容与保存状态待现场测绘",
            "technical_memory": "生产大队集体储粮的石木结构粮仓营造工艺",
            "social_memory": "大队集体储粮与公粮缴纳记忆",
            "current_use_or_loss": "统计表拟新增层级（正式公布文件未检索到，待跟踪）；现状用途待核",
        },
        "notes": "直接取自宣恩县政府网2024年拟新增历史建筑统计表（A级，智能体核读）；统计表层级较公示更前置；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_storage_site",
    },
    {
        "inventory_id": "HBI-ES-031",
        "name": "燕子镇石龙街驿站",
        "city": "恩施州",
        "district_county": "鹤峰县燕子镇",
        "industry_category_l1": "盐运交通与山地贸易路线",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "鹤峰县第一批历史建筑（2023年1月8日公布，名录第11项）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["hefeng_heritage_2023_2024"],
        "cultural_evidence": {
            "material_carriers": "四合天井式驿站建筑（客栈与运茶骡马道组合）；建筑面积与保存状态待现场测绘",
            "technical_memory": "武陵山区茶马古道驿运体系的客栈—骡马道组合设施，山地商路转运节点形制",
            "social_memory": "鹤峰茶叶外运与骡马商队过往记忆，与万里茶道、容美土司贡茶历史脉络相关",
            "current_use_or_loss": "以第一批历史建筑身份正式公布保护；现状用途与活化方向待核",
        },
        "notes": "直接取自鹤峰县政府第一批历史建筑公布通知名录（A级，正式公布）；与底册川鄂古盐道神农架段（HBI-SNJ 系列）同属山地商路遗存模式；坐标未核验保持待核。",
        "aliases": ["石龙街客栈"],
        "asset_kind": "industrial_trade_site",
    },
    {
        "inventory_id": "HBI-ES-032",
        "name": "鹤峰茶马古道桥梁（关口石拱桥、刘公桥）",
        "city": "恩施州",
        "district_county": "鹤峰县太平镇、走马镇",
        "industry_category_l1": "茶业生产与贸易交通",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "鹤峰县第一批历史建筑（2023年1月8日公布，名录第1、2项）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["hefeng_heritage_2023_2024"],
        "cultural_evidence": {
            "material_carriers": "两座古石拱桥：关口石拱桥（太平镇，清康熙十三年）、刘公桥（走马镇，光绪十三年）；桥体跨度与保存状态待现场测绘",
            "technical_memory": "茶马古道与万里茶道干道上的石拱桥营建工艺，山地商路跨溪交通节点",
            "social_memory": "鹤峰茶号运茶骡马队与商旅往来记忆，见证武陵山区茶叶外销通道",
            "current_use_or_loss": "以第一批历史建筑身份正式公布保护；通行状态与保护范围待核",
        },
        "notes": "直接取自鹤峰县政府第一批历史建筑公布通知名录（A级，正式公布）；两桥合并记录以保持茶马古道交通脉络完整；与底册万里茶道系列（HBI-XN 等）同谱系；坐标未核验保持待核。",
        "aliases": ["关口石拱桥", "刘公桥"],
        "asset_kind": "industrial_transport_site",
    },
]


ES013_PATCH = {
    "source_keys_append": ["enshi_zjw_428_2026"],
    "notes_append": "2026年州住建局会办意见（A级）确认全州428处历史建筑确权挂牌覆盖率100%，并载恩施1988街区改造老旧厂房3.2万平方米（即本条烟叶复烤厂厂房旧址活化），补充官方活化规模数据。",
}


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
    es013 = next((row for row in records if row["inventory_id"] == "HBI-ES-013"), None)
    if es013 is None:
        raise SystemExit("record not found: HBI-ES-013")
    updated = 0
    for key in ES013_PATCH["source_keys_append"]:
        if key not in es013["source_keys"]:
            es013["source_keys"].append(key)
            updated = 1
    if ES013_PATCH["notes_append"] not in es013["notes"]:
        es013["notes"] = es013["notes"] + ES013_PATCH["notes_append"]
        updated = 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_bt_sources={len(SOURCES)} added_records={added} updated_records={updated} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
