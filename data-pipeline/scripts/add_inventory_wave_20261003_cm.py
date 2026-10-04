from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "xiaochang_batch3_2024": {
        "source_type": "county_government_public_notice",
        "title": "孝昌县第三批历史建筑名录（20处，附件xlsx编号HB-XG-XC-0008~0027，2024-04-29）",
        "org": "孝昌县人民政府办公室（孝昌县人民政府网）",
        "pub_date": "2024-04-29",
        "url": "http://www.xiaochang.gov.cn/c/xcxzfhcxjsj/qtzdgkwj/346082.jhtml",
        "authority": "A",
        "notes": "第三批20处附件xlsx（省级上报详表，含地址/年代/简介）已下载核读：双峰渡槽（HB-XG-XC-0026，周巷镇双峰村下份湾，1967年始建、1974年龙卷风垮塌后重建，全长200余米、高约15米，引观音湖水灌溉周巷、丰山、邹岗三镇90%农田）、新四军第五师被服厂旧址（HB-XG-XC-0020，小悟乡项庙村大阳湾，1943年，与枪械维修所和练兵场并设）；其余为寺庙、古井、民居、宗祠、李先念旧居等。孝昌第二批7处（2023-08-01）含红山大桥。",
    },
    "dawu_wenbao_list": {
        "source_type": "county_cultural_relic_publicity",
        "title": "大悟县文物保护单位名录（含边区消费合作社旧址、兵工厂旧址两处工业类县保，芳畈镇大悟山村）",
        "org": "大悟县人民政府网（县文旅局）",
        "pub_date": None,
        "url": "http://www.hbdawu.gov.cn/c/dwx/ggwhfw/354842.jhtml",
        "authority": "A",
        "notes": "大悟县文物保护单位名录载明：No.71边区消费合作社旧址（芳畈镇大悟山村，县保，供销合作类）、No.72兵工厂旧址（芳畈镇大悟山村，县保，军工）；大悟县历史建筑沿革：2007/2011年曾公布172处、2021年公布21处（孝感市第一批56处中大悟占21处）、2023年新一批12处（寺祠民居为主，湖北日报2023-05-30挂牌报道）。",
    },
    "xiaogan_batch2_2024": {
        "source_type": "municipal_government_notice",
        "title": "孝感市第二批历史建筑名单（25处，孝感政办函〔2024〕29号，PDF原件核读）",
        "org": "孝感市人民政府（市政府网信息公开）",
        "pub_date": "2024-06-22",
        "url": "http://gkml.xiaogan.gov.cn/c/www/xgzbh/359891.jhtml",
        "authority": "A",
        "notes": "第二批25处地址全部为孝感市孝南区：南闸泵站（1960年）、三汊埠火车站（1901年）、三汊粮油公司老仓库（1960年）、孝感县三汊供销社（1970年）、孝感米酒馆（1956年）等工业/商贸类对象；第一批（2021年56处）孝感老麻糖厂（1964年，城隍潭9号）为工业遗产（与底册 HBI 系列麻糖类对象的孝南城隍潭语境相关）。",
    },
}


def _xg(record_id: str, name: str, dc: str, cat: str, level: str, status: str, src: list, kind: str, year: str, material: str, tech: str, social: str, use: str, notes: str, aliases: list) -> dict:
    return {
        "inventory_id": record_id,
        "name": name,
        "city": "孝感市",
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
    _xg("HBI-XG-022", "双峰渡槽", "孝昌县周巷镇双峰村下份湾", "水利工程与泵站", "municipal_historical_building",
        "孝昌县第三批历史建筑（2024-04-29公布，名录编号HB-XG-XC-0026）", ["xiaochang_batch3_2024"], "industrial_utility_site", "1967年始建/1974年重建",
        "渡槽本体（全长200余米、高约15米），1974年龙卷风垮塌后重建；结构形式与保存状态待现场测绘",
        "山区引水灌溉渡槽工艺与灾后重建工程史（引观音湖水灌溉周巷、丰山、邹岗三镇90%农田）",
        "三镇农业灌溉命脉与渡槽建设者的集体记忆",
        "以第三批历史建筑身份正式公布保护；在用/停用状态待核",
        "直接取自孝昌县第三批名录附件xlsx（A级，省级上报详表已核读）；与底册陡山/青山口渡槽（HBI-XG-015/016）同县域水利谱系；坐标未核验保持待核。",
        [],
    ),
    _xg("HBI-XG-023", "新四军第五师被服厂旧址（含枪械维修所）", "孝昌县小悟乡项庙村大阳湾", "军需纺织工业", "county_relic_related",
        "孝昌县第三批历史建筑（2024-04-29公布，名录编号HB-XG-XC-0020；1943年）", ["xiaochang_batch3_2024"], "industrial_building", "1943年",
        "被服厂旧址建筑本体，与枪械维修所和练兵场并设；厂房形制与设备遗迹待现场测绘",
        "新四军第五师军需被服生产与枪械维修的战时军工组合设施",
        "新四军五师（李先念部）随军军工生产与根据地支前记忆",
        "以第三批历史建筑身份正式公布保护；保存状况与展示利用待核",
        "直接取自孝昌县第三批名录附件xlsx（A级，已核读）；革命军需工业对象，记录边界含枪械维修所组合；坐标未核验保持待核。",
        ["新四军第五师枪械维修所"],
    ),
    _xg("HBI-XG-024", "边区消费合作社旧址", "大悟县芳畈镇大悟山村", "供销商贸与基层物资供应", "county_relic_related",
        "大悟县文物保护单位（文保名录No.71）", ["dawu_wenbao_list"], "industrial_trade_site", "待核",
        "消费合作社旧址建筑本体（芳畈镇大悟山村）；门面与柜面格局待现场测绘",
        "边区消费合作社的统购统销与合作社经济组织形制",
        "鄂豫边区合作社经济与根据地物资供应记忆",
        "以县保身份纳入保护体系；保存与展示状态待核",
        "直接取自大悟县文旅局文保名录（A级）；供销合作类对象与底册供销社系列同谱系；坐标未核验保持待核。",
        ["边区合作社"],
    ),
    _xg("HBI-XG-025", "兵工厂旧址", "大悟县芳畈镇大悟山村", "军工修配工业", "county_relic_related",
        "大悟县文物保护单位（文保名录No.72）", ["dawu_wenbao_list"], "industrial_building", "待核",
        "兵工厂旧址建筑本体（芳畈镇大悟山村）；厂房与设备遗迹待现场测绘",
        "地方兵工厂的修械制造工艺与隐蔽生产布局",
        "根据地军工生产与民兵武装记忆",
        "以县保身份纳入保护体系；建造年代与生产谱系待档案核验",
        "直接取自大悟县文旅局文保名录（A级）；坐标未核验保持待核。",
        [],
    ),
    _xg("HBI-XG-026", "南闸泵站", "孝感市孝南区", "水利工程与泵站", "municipal_historical_building",
        "孝感市第二批历史建筑（孝感政办函〔2024〕29号，2024-06-22公布，25处之一；1960年）", ["xiaogan_batch2_2024"], "industrial_utility_site", "1960年",
        "泵站建筑与机组设施；装机与结构待现场测绘",
        "1960年排灌泵站的机电提水工艺",
        "孝南区排涝保丰收与泵站职工值守记忆",
        "以市级历史建筑身份正式公布保护；在用/退役状态待核",
        "直接取自孝感政办函〔2024〕29号名录（A级，PDF原件已核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    _xg("HBI-XG-027", "三汊埠火车站", "孝感市孝南区三汊镇", "铁路交通工业", "municipal_historical_building",
        "孝感市第二批历史建筑（孝感政办函〔2024〕29号，2024-06-22公布，25处之一；1901年）", ["xiaogan_batch2_2024"], "industrial_transport_site", "1901年",
        "火车站站房与站场设施（三汊镇）；站房立面与轨道形制待现场测绘",
        "1901年建站的铁路车站——孝感境内最早铁路站之一（京汉铁路沿线支线或车站谱系待铁路志核验）",
        "三汊埠铁路客货运与集镇因站而兴的记忆",
        "以市级历史建筑身份正式公布保护；运营状态与保留范围待铁路部门核",
        "直接取自孝感政办函〔2024〕29号名录（A级，PDF原件已核读）；1901年建站早于京汉铁路全线通车（1906年），所属线路待核；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["三汊埠站"],
    ),
    _xg("HBI-XG-028", "三汊粮油公司老仓库与三汊供销社", "孝感市孝南区三汊镇", "粮食仓储工业", "municipal_historical_building",
        "孝感市第二批历史建筑（孝感政办函〔2024〕29号，2024-06-22公布，25处之列；1960/1970年）", ["xiaogan_batch2_2024"], "industrial_storage_site", "1960/1970年",
        "2处建筑：三汊粮油公司老仓库（1960年）与孝感县三汊供销社（1970年）；仓型与保存状态待现场测绘",
        "粮油统购统销仓库与供销社双系统的集镇布局",
        "三汊镇粮储职工与供销社员记忆",
        "以市级历史建筑身份正式公布保护；现状用途待核",
        "直接取自孝感政办函〔2024〕29号名录（A级，PDF原件已核读）；2处合并记录；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["三汊粮油公司", "三汊供销社"],
    ),
    _xg("HBI-XG-029", "孝感米酒馆", "孝感市孝南区", "食品加工工业", "municipal_historical_building",
        "孝感市第二批历史建筑（孝感政办函〔2024〕29号，2024-06-22公布，25处之一；1956年）", ["xiaogan_batch2_2024"], "industrial_trade_site", "1956年",
        "米酒馆建筑本体；门面与酿造作坊格局待现场测绘",
        "孝感米酒（糊汤酒酿）的商业酿造与堂售传统，1956年公私合营背景的米酒馆业态",
        "孝感米酒城市名片与早酒饮食习俗记忆",
        "以市级历史建筑身份正式公布保护；经营延续与建筑保存待核",
        "直接取自孝感政办函〔2024〕29号名录（A级，PDF原件已核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
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
    print(f"wave_cm_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
