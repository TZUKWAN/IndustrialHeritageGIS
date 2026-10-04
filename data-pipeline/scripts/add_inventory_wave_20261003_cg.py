from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "macheng_batch2_2023": {
        "source_type": "county_city_government_notice",
        "title": "麻城市人民政府关于公布第二批历史建筑名录的通知（麻政发〔2023〕10号，9处）",
        "org": "麻城市人民政府门户网站",
        "pub_date": "2023-09-13",
        "url": "http://www.macheng.gov.cn/zwgk/public/6636847/1021480.html",
        "authority": "A",
        "notes": "第二批9处含渡槽5处：福田河镇何家坳渡槽、何家凹渡槽、土门渡槽（1972年建，长125.45米石混结构）、龟山镇驻峰山渡槽、盐田河镇安堂国渡槽；另有乘马岗镇原大河铺水库管理处办公楼、黄土岗镇细水河桥、小漆园礼堂、中馆驿镇林氏祠。麻城政府网佐证称其为“重大的民生水利工程，对研究上世纪中期水利设施建筑提供了实物资料”（http://www.mc.gov.cn/zwxw/bmdt/11730620.html）；黄冈市政府网另有土门渡槽细节报道（https://www.hg.gov.cn/zwxw/xsxw/9312032.html）。第一批（麻政发〔2018〕17号公示）2处：观音殿、傅家山渡槽。",
    },
    "macheng_batch3_2024": {
        "source_type": "county_city_government_public_notice",
        "title": "2024年麻城市历史文化建筑评审清单公示（30处，名单xls）",
        "org": "麻城市住房和城乡建设局（市政府网）",
        "pub_date": "2024-05-31",
        "url": "http://www.macheng.gov.cn/zwgk/public/6635494/1379411.html",
        "authority": "A",
        "notes": "名单xls附件（http://www.macheng.gov.cn/group2/M00/0D/FA/rBQOoGZZd_yAINBlBJyuAPrLV4g679.xls）已下载解析30处：盐田河茧站（1953年，占地5000余㎡，收贮室2间+烘干车间3间保存完好，服务周边5个乡镇十万蚕农，“鄂东近代建筑典范”）、门前垸村鲍家垸生产队仓库（1956年，两层阁楼，建国初期标语清晰）、凉亭生产队仓库（1970年，铁门岗乡）、张广河油茶籽仓库（1958年，狮子峰林场，原铁厂大办公室）、谢店古村民俗陈列馆及桥梁6座（黄泥坳大桥1965、木子店一桥1978、风雨桥1904/1964、张家湾汽车桥1958、黄土岗桥1979、燕窝地村石拱桥1970）。",
    },
    "hongan_batch3_2024": {
        "source_type": "county_government_notice",
        "title": "红安县人民政府关于公布红安县第三批历史建筑的通知（红政发〔2024〕8号，40处）",
        "org": "红安县人民政府门户网站（hazf.gov.cn）",
        "pub_date": "2024-05-29",
        "url": "https://www.hazf.gov.cn/zwgk/public/6636844/1404722.html",
        "authority": "A",
        "notes": "第三批40处正文含完整名单表：福德公社建新大队粮仓（约1963年，七里坪镇盐店河村秦罗庄，砖木14间，“人民公社时期的符号”，现改造为红色培训中心）、陡山村谢家垸粮仓（1962年，八里湾镇，立面刻“深挖洞广积粮”“备战备荒为人民”标语）、八一村老茶厂（1970年，七里坪镇，村集体茶叶加工场所）、八一村大集体仓库（1970年）、七里坪镇供销合作社（长胜街，明末清初建筑2栋砖木，曾承担农业供销职能）等；红安县文保单位479处中革命遗址233处属文物序列（黄冈日报2024-12），历史建筑为住建序列另行公布。",
    },
    "huangmei_batch3_2024": {
        "source_type": "county_government_notice",
        "title": "关于公布黄梅县第三批历史建筑名录的通知（36处）",
        "org": "黄梅县人民政府门户网站",
        "pub_date": "2024-06-01",
        "url": "http://www.hm.gov.cn/zwgk/public/6636010/1502958.html",
        "authority": "A",
        "notes": "第三批36处正文含完整名单表：骑龙庵粮库（1950年，濯港镇吴元八村）、濯港老粮库1号仓库（1953年，濯港镇）、大庙公社食品所（1954年，大河镇）、向蔡供销社老房（1960年左右，五祖镇向桥村）、苦竹供电所老办公楼（1982年，苦竹乡吕世贵村）、渔政办公楼（1954）、独山镇老银行（1954）、商务局老办公楼（1958）、林科所职工宿舍（1958）、县委老办公楼（1952）及中垏老礼堂（1979）、杨凼大礼堂（1963）、太山大礼堂（1964）、商子塆大礼堂（1962）等4处礼堂。第二批（黄梅县人民政府2023-09-10公布，http://www.hm.gov.cn/zwgk/public/6636010/1322620.html）3处含卢府老榨油坊（民国，1958年迁建，保存全套人工榨油设备，县内唯一完好店铺作坊）。",
    },
}


def _hg(record_id: str, name: str, dc: str, cat: str, status: str, kind: str, year: str, material: str, tech: str, social: str, use: str, notes: str, aliases: list, src: list) -> dict:
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
    _hg("HBI-HG-020", "傅家山渡槽", "麻城市（乡镇待测绘成果核验）", "水利工程与泵站",
        "麻城市第一批历史建筑（麻政发〔2018〕17号公示，2018年）", "industrial_utility_site", "待核",
        "傅家山渡槽本体；跨度与结构待测绘成果核验",
        "麻城渡槽序列的起点（2018年首批即收录），山区引水灌溉构筑物",
        "麻城灌区农业灌溉与水利建设记忆",
        "以第一批历史建筑身份纳入保护体系；在用/停用状态待核",
        "经搜狗新闻快照核实（麻城市城乡规划局2017.9-2018.10认定程序，多篇报道一致），政府网原文未检索到；坐标未核验保持待核。",
        [], ["macheng_batch2_2023"],
    ),
    _hg("HBI-HG-021", "麻城渡槽群（何家坳、何家凹、土门、驻峰山、安堂国渡槽）", "麻城市福田河镇、龟山镇、盐田河镇", "水利工程与泵站",
        "麻城市第二批历史建筑（麻政发〔2023〕10号，2023-09-13，名录渡槽5处）", "industrial_utility_site", "1972年（土门渡槽）等",
        "渡槽5处：福田河镇何家坳渡槽、何家凹渡槽、土门渡槽（长125.45米石混结构）、龟山镇驻峰山渡槽、盐田河镇安堂国渡槽；各渡槽跨度与保存状态待现场测绘",
        "上世纪中期山区水利设施的渡槽建筑实物资料（政府网评语），石混结构大跨度输水工艺",
        "麻城东北部山区农田灌溉与水利会战集体记忆",
        "以第二批历史建筑身份纳入保护体系；在用/停用状态待核",
        "直接取自麻政发〔2023〕10号名录（A级）；5处合并记录以保持渡槽序列完整；坐标未核验保持待核。",
        ["土门渡槽", "安堂国渡槽", "驻峰山渡槽"],
        ["macheng_batch2_2023"],
    ),
    _hg("HBI-HG-022", "盐田河茧站", "麻城市盐田河镇", "蚕桑与缫丝工业",
        "2024年麻城市历史文化建筑评审清单公示（30处之一）", "industrial_building", "1953年",
        "茧站建筑群（占地5000余平方米，收贮室2间+烘干车间3间保存完好）；烘茧设备留存待现场测绘",
        "蚕茧收贮与烘干工艺的专区级站房形制，服务周边5个乡镇十万蚕农，被誉为“鄂东近代建筑典范”",
        "麻城东部蚕桑产业带茧农与茧站职工的记忆，蚕桑经济兴衰的时代见证",
        "以评审清单公示层级纳入保护体系（正式公布待跟踪）；现状用途待核",
        "直接取自2024年评审清单xls（A级，已下载解析）；茧站类型为黄冈县域罕见；坐标未核验保持待核。",
        [],
        ["macheng_batch3_2024"],
    ),
    _hg("HBI-HG-023", "乘马岗镇原大河铺水库管理处办公楼", "麻城市乘马岗镇", "水利工程与泵站",
        "麻城市第二批历史建筑（麻政发〔2023〕10号，2023-09-13）", "industrial_utility_site", "待核",
        "水库管理处办公楼建筑本体；结构与保存状态待现场测绘",
        "水库管理设施的办公建筑形制，类型在县域历史建筑中稀有",
        "大河铺水库建设与管理者的集体记忆",
        "以第二批历史建筑身份纳入保护体系；现状用途待核",
        "直接取自麻政发〔2023〕10号名录（A级）；坐标未核验保持待核。",
        ["大河铺水库管理处"],
        ["macheng_batch2_2023"],
    ),
    _hg("HBI-HG-024", "麻城生产队仓库群（门前垸、凉亭、张广河油茶籽仓库）", "麻城市张家畈镇、铁门岗乡、狮子峰林场", "粮食仓储工业",
        "2024年麻城市历史文化建筑评审清单公示（30处之一组）", "industrial_storage_site", "1956/1958/1970年",
        "3处生产队仓库：门前垸村鲍家垸生产队仓库（1956年，两层阁楼，建国初期标语清晰）、凉亭生产队仓库（1970年）、张广河油茶籽仓库（1958年，原铁厂大办公室）；保存状况待现场测绘",
        "集体化时期生产队粮仓与油茶籽专业仓库的仓储形制，标语墙的时代印记",
        "生产队集体储粮与油茶经济记忆",
        "以评审清单公示层级纳入保护体系（正式公布待跟踪）；现状用途待核",
        "直接取自2024年评审清单xls（A级，已下载解析）；3处合并记录；坐标未核验保持待核。",
        ["鲍家垸生产队仓库", "凉亭生产队仓库", "张广河油茶籽仓库"],
        ["macheng_batch3_2024"],
    ),
    _hg("HBI-HG-025", "红安公社粮仓（建新大队粮仓、谢家垸粮仓）", "红安县七里坪镇、八里湾镇", "粮食仓储工业",
        "红安县第三批历史建筑（红政发〔2024〕8号，2024-05-29）", "industrial_storage_site", "约1963/1962年",
        "2处公社粮仓：福德公社建新大队粮仓（砖木14间，“人民公社时期的符号”，现改造为红色培训中心）、陡山村谢家垸粮仓（立面刻“深挖洞广积粮”“备战备荒为人民”标语）；保存状况待现场测绘",
        "人民公社时期大队粮仓的砖木仓储形制与备战标语墙",
        "红安老区集体储粮与战备年代记忆；建新大队粮仓已活化红色培训中心",
        "以第三批历史建筑身份正式公布保护；谢家垸粮仓现状用途待核",
        "直接取自红政发〔2024〕8号名录（A级）；2处合并记录；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["建新大队粮仓", "谢家垸粮仓"],
        ["hongan_batch3_2024"],
    ),
    _hg("HBI-HG-026", "八一村老茶厂与大集体仓库", "红安县七里坪镇八一村", "茶业生产与工业社区",
        "红安县第三批历史建筑（红政发〔2024〕8号，2024-05-29）", "industrial_building", "1970年",
        "老茶厂与大集体仓库2处建筑（均为1970年）；设备留存待现场测绘",
        "村集体茶叶加工与集体仓储的一体化生产组合",
        "七里坪镇八一村（革命老区村）集体茶业与仓储记忆",
        "以第三批历史建筑身份正式公布保护；现状用途待核",
        "直接取自红政发〔2024〕8号名录（A级）；2处合并记录；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
        ["hongan_batch3_2024"],
    ),
    _hg("HBI-HG-027", "七里坪镇长胜街供销合作社", "红安县七里坪镇长胜街", "供销商贸与基层物资供应",
        "红安县第三批历史建筑（红政发〔2024〕8号，2024-05-29）", "industrial_trade_site", "明末清初建筑",
        "供销合作社2栋砖木建筑（长胜街，曾承担农业供销职能）；与天门/襄阳/利川供销社同谱系",
        "长胜街老建筑改造供销合作社的农业物资供应功能形制",
        "红安七里坪苏区老街的商业供销记忆（长胜街为革命旧址集中街区）",
        "以第三批历史建筑身份正式公布保护；现状用途待核",
        "直接取自红政发〔2024〕8号名录（A级）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
        ["hongan_batch3_2024"],
    ),
    _hg("HBI-HG-028", "黄梅粮库（骑龙庵粮库、濯港老粮库1号仓库）", "黄梅县濯港镇", "粮食仓储工业",
        "黄梅县第三批历史建筑名录（2024-06-01，36处）", "industrial_storage_site", "1950/1953年",
        "2处粮库：骑龙庵粮库（濯港镇吴元八村，1950年）、濯港老粮库1号仓库（濯港镇，1953年）；仓房型制与保存状态待现场测绘",
        "新中国初期县域粮库建设的最早批次形制",
        "黄梅粮棉产区统购统销记忆",
        "以第三批历史建筑身份正式公布保护；在用/停用状态待核",
        "直接取自黄梅县政府第三批名录（A级）；2处合并记录；坐标未核验保持待核。",
        ["骑龙庵粮库", "濯港老粮库"],
        ["huangmei_batch3_2024"],
    ),
    _hg("HBI-HG-029", "卢府老榨油坊", "黄梅县（1958年迁建）", "油料加工工业",
        "黄梅县第二批历史建筑（黄梅县人民政府2023-09-10公布，3处之一）", "industrial_building", "民国（1958年迁建）",
        "老榨油坊建筑，保存全套人工榨油设备（县内唯一完好店铺作坊）",
        "传统木榨榨油工艺的完整设备实证",
        "黄梅油坊榨油匠与乡民打油换油记忆",
        "以第二批历史建筑身份正式公布保护；设备保存为黄梅县域唯一，活化展示价值高",
        "直接取自黄梅县政府第二批公布通知（A级）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
        ["huangmei_batch3_2024"],
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
    print(f"wave_cg_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
