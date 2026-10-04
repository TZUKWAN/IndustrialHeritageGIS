from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "dangyang_batch1_2021": {
        "source_type": "county_city_government_notice",
        "title": "当阳市人民政府关于公布历史建筑名录的通知（2021-12-10，首批31处，编号DY-001~031）",
        "org": "当阳市人民政府门户网站（信息公开）",
        "pub_date": "2021-12-10",
        "url": "http://xxgk.dangyang.gov.cn/show.html?aid=1&id=216848&t=4",
        "authority": "A",
        "notes": "首批31处名录含名称/位置/编号/年代/简介（智能体经官方数据接口核读）：No.25官道河水库（玉泉办事处官道河村二组，DY-YQ-025，1974年兴建1976年竣工，总库容1559万方，粘土心墙堆石坝，坝长241米高42米，“坝体均为人力所建”，用于防洪灌溉养殖，“反映人民响应毛主席号召，兴建水利……具有典型的时代特征”）；另有河溶镇沿河街/紫云街民居群（白玉堂旧居、张炳南宅等）、淯溪镇民居14处、中共当阳地委旧址与瓦仓起义战时指挥部旧址；曹贤迪宅（侵华时期曾设榨油坊、酒作坊）与朱大润宅（粮棉布丝绸生意）为附带工商业线索。",
    },
    "dangyang_batch2024_2025": {
        "source_type": "county_city_government_notice",
        "title": "2024年当阳市新增历史建筑名录（31处，编号DY-032~062）",
        "org": "当阳市住房和城乡建设局（当阳市人民政府网，2025-01-07发布）",
        "pub_date": "2025-01-07",
        "url": "http://www.dangyang.gov.cn/zfxxgk/show.html?id=119847",
        "authority": "A",
        "notes": "2024年新增31处（编号032-062，与首批无缝衔接），工业遗产密集（智能体经官方数据接口核读）：国营草埠湖粮管所1-4号仓库（1959年）、草埠湖沮漳供销社、老榨油坊仓库、草埠湖农垦往事街区彩门、半月镇粮管所1-3号仓库、半月镇供销社1-2号仓库、半月镇电影院（1978年）、恒山大礼堂（1970年代初）、老烟厂技术加工车间/材料仓库/成品仓库（子龙路，1975年，共3处）、干河村粮管所仓库（1972年）、三桥村粮站仓库（1952年始建）、焦堤粮仓（1974年）、市公路建设养护中心办公楼（1993年）等约17处工业相关对象。",
    },
    "wuxue_front_batches_gap_2026": {
        "source_type": "county_public_notice",
        "title": "武穴市2024年新增历史建筑名录的公示（29处，编号WXLSJZ023-051）",
        "org": "武穴市住房和城乡建设局（武穴市人民政府网）",
        "pub_date": "2024-05-29",
        "url": "https://www.wuxue.gov.cn/zwgk/public/6636855/1376938.html",
        "authority": "A",
        "notes": "第八十七轮排除性核查结论：武穴门户通知公告栏34页约660条全时段扫描（2018-08至2026-09）、住建局四个信息公开栏回溯2019年、多引擎检索均无前批次（编号001-022，约22处）公示原文；2024年公示标题称“新增”与编号自023起旁证前批次已确认存在（2024年11月湖北日报客户端系列挂牌视频含市委老书记楼等前批次对象），认定大概率发生于2021-2023年线下程序。建议向武穴市住建局申请政府信息公开或查《武穴市历史文化保护传承实施方案》申报档案。",
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
        "recognition_status": ("当阳市2024年新增历史建筑（2025-01-07公布，31处之列，编号DY-032~062段）" if "dangyang_batch2024_2025" in src else "当阳市历史建筑（2021-12-10市政府公布首批名录31处之列）"),
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
    _yc("HBI-YC-051", "官道河水库", "当阳市玉泉办事处官道河村二组", "水利工程与泵站", "industrial_utility_site", "1974-1976年",
        "水库大坝（粘土心墙堆石坝，坝长241米、高42米，总库容1559万方）及溢洪、灌溉设施；名录简介载“坝体均为人力所建”",
        "1970年代人力堆石坝筑坝工艺与防洪灌溉养殖综合水利调度",
        "人民响应号召兴建水利的时代记忆（名录原文评语），当阳市最大水库之一的人力建设史诗",
        "以首批历史建筑身份正式公布保护；水库运行管理现状待水利部门核",
        "直接取自当阳市政府首批历史建筑名录（A级，官方数据接口核读，名录第25项含完整简介）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
        ["dangyang_batch1_2021"],
    ),
    _yc("HBI-YC-052", "国营草埠湖粮管所仓库群（1-4号仓库）", "当阳市草埠湖镇（国营农场区）", "粮食仓储工业", "industrial_storage_site", "1959年",
        "国营草埠湖粮管所1-4号仓库（1959年建）；仓房型制与保存状态待现场测绘",
        "国营农场粮管所的苏式/早期仓房仓储体系，草埠湖农垦区粮食统购统销核心设施",
        "草埠湖农垦场职工（军垦转业与移民背景）的粮储生产记忆",
        "以市级历史建筑身份纳入保护体系；在用/停用状态待核",
        "直接取自2024年当阳市新增历史建筑名录（A级，智能体核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["草埠湖粮管所"],
        ["dangyang_batch2024_2025"],
    ),
    _yc("HBI-YC-053", "草埠湖农垦遗产群（沮漳供销社、老榨油坊仓库、农垦往事街区彩门）", "当阳市草埠湖镇", "供销商贸与基层物资供应", "industrial_trade_site", "待核",
        "3处农垦遗产：沮漳供销社、老榨油坊仓库、草埠湖农垦往事街区彩门；保存状态待现场测绘",
        "草埠湖国营农垦区的商业供应、油料加工与农垦文化街区标识体系",
        "草埠湖农场（1950年代建立的国营农场）农工创业与“农垦往事”集体记忆",
        "以市级历史建筑身份纳入保护体系；农垦往事街区活化方向待核",
        "直接取自2024年当阳市新增历史建筑名录（A级，智能体核读）；3处合并记录以保持农垦遗产群完整；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["沮漳供销社", "老榨油坊仓库", "农垦往事街区"],
        ["dangyang_batch2024_2025"],
    ),
    _yc("HBI-YC-054", "半月镇粮管所与供销社仓库群（粮管所1-3号仓库、供销社1-2号仓库）", "当阳市半月镇", "粮食仓储工业", "industrial_storage_site", "待核",
        "5处仓储建筑：半月镇粮管所1-3号仓库、半月镇供销社1-2号仓库；仓房型制与保存状态待现场测绘",
        "粮管所与供销社双系统的仓储组合，反映计划经济粮棉油统购统销与生产资料供应的双轨布局",
        "半月镇粮储职工与供销社员记忆",
        "以市级历史建筑身份纳入保护体系；在用/停用状态待核",
        "直接取自2024年当阳市新增历史建筑名录（A级，智能体核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["半月镇粮管所", "半月镇供销社"],
        ["dangyang_batch2024_2025"],
    ),
    _yc("HBI-YC-055", "老烟厂工业建筑群（技术加工车间、材料仓库、成品仓库）", "当阳市子龙路", "烟叶复烤与烟草加工", "industrial_building", "1975年",
        "老烟厂3处工业建筑：技术加工车间、材料仓库、成品仓库（子龙路）；车间设备与建筑保存状态待现场测绘",
        "1975年县域烟草工业的烟叶发酵、卷制加工与成品储运功能分区",
        "当阳烟厂职工与县域烟草产业记忆",
        "以市级历史建筑身份纳入保护体系；停产年代与现状（闲置/改造）待核",
        "直接取自2024年当阳市新增历史建筑名录（A级，智能体核读）；3处合并记录；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["当阳老烟厂"],
        ["dangyang_batch2024_2025"],
    ),
    _yc("HBI-YC-056", "当阳乡村粮站仓库群（干河村粮管所仓库、三桥村粮站仓库、焦堤粮仓）", "当阳市（干河村、三桥村、焦堤）", "粮食仓储工业", "industrial_storage_site", "1952/1972/1974年",
        "3处乡村粮仓储设施：干河村粮管所仓库（1972年）、三桥村粮站仓库（1952年始建）、焦堤粮仓（1974年）；仓型与保存状态待现场测绘",
        "1950-70年代乡村粮站—粮管所—粮仓三级粮食储运网络的节点标本",
        "当阳产粮区售粮与乡粮站职工记忆",
        "以市级历史建筑身份纳入保护体系；在用/停用状态待核",
        "直接取自2024年当阳市新增历史建筑名录（A级，智能体核读）；3处合并记录；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["干河村粮管所仓库", "三桥村粮站仓库", "焦堤粮仓"],
        ["dangyang_batch2024_2025"],
    ),
    _yc("HBI-YC-057", "半月镇电影院与恒山大礼堂", "当阳市半月镇", "工业社区文化", "industrial_social_site", "1970年代初/1978年",
        "2处文化设施：半月镇电影院（1978年）、恒山大礼堂（1970年代初）；观众厅与舞台格局待现场测绘",
        "乡镇电影院与大礼堂的文娱功能空间形制",
        "半月镇居民观影集会记忆",
        "以市级历史建筑身份纳入保护体系；现状用途（停演/改造）待核",
        "直接取自2024年当阳市新增历史建筑名录（A级，智能体核读）；2处合并记录；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["半月镇电影院", "恒山大礼堂"],
        ["dangyang_batch2024_2025"],
    ),
    _yc("HBI-YC-058", "市公路建设养护中心办公楼", "当阳市（地址待核）", "公路交通工业", "industrial_building", "1993年",
        "公路建设养护中心办公楼建筑本体；结构与保存状态待现场测绘",
        "公路建设养护体系的行业办公建筑，当阳公路网养护管理记忆载体",
        "公路养护职工与当阳干线公路建设记忆",
        "以市级历史建筑身份纳入保护体系；现状用途待核",
        "直接取自2024年当阳市新增历史建筑名录（A级，智能体核读）；名录未载地址明细；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
        ["dangyang_batch2024_2025"],
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
    print(f"wave_ck_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
