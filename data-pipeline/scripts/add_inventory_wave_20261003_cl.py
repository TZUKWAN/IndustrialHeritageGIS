from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "djk_batch3_2024": {
        "source_type": "county_government_notice",
        "title": "市人民政府关于公布丹江口市第三批历史建筑名录的通知（丹政发〔2024〕6号，40处，红头文件扫描图识读）",
        "org": "丹江口市人民政府门户网站",
        "pub_date": "2024-05-29",
        "url": "http://www.djk.gov.cn/xxgk/zc/gfxwj/dzf/202408/t20240822_4585610.shtml",
        "authority": "A",
        "notes": "丹政发〔2024〕6号（2024-05-29成文）公布40处（官山5、大沟2、蒿坪1、浪河19、土关垭2、盐池河9、凉水河1、石鼓2，含地址/年代/现状/面积）：工业对象9处全部为三线军工生活配套建筑——国营三六一一厂电影院（2160㎡）/办公楼（3550㎡）/商场（2360㎡）（浪河镇土门沟村，70年代）、国营三六零七电影院（1260㎡）/办公楼（2870㎡）/商场（1590㎡）（浪河镇代湾村，60年代）、国营三六零二电影院（1375㎡）/百货大楼（1790㎡）/办公楼（3586㎡）（浪河镇青莫社区，70年代）——3602/3607/3611三厂集中浪河镇构成完整三线厂区生活配套建筑群。",
    },
    "zhushan_batches_2023_2024": {
        "source_type": "county_government_notice",
        "title": "竹山县第一批（11处，竹政办发〔2023〕27号）、第二批（20处，竹政办发〔2024〕19号）历史建筑保护名单",
        "org": "竹山县人民政府办公室（竹山县人民政府网）",
        "pub_date": "2023-08-09",
        "url": "http://www.zhushan.gov.cn/xxgkxi/zc/qtzdgkwj/202309/t20230925_4317319.shtml",
        "authority": "A",
        "notes": "第一批11处含霍河大坝坝沿（城关镇刘家山村，20世纪70年代，全县名录中唯一大型水利水电构筑物）；第二批20处含竹山堵河大桥（城关镇人民路，建国后，两批中唯一现代基础设施）；第二批URL http://www.zhushan.gov.cn/xxgkxi/zc/qtzdgkwj/202601/t20260120_4886986.shtml（2024-07-11发布）。两批其余为清代老屋/宗祠/古民居群。",
    },
    "shiyan_batch2025_2026": {
        "source_type": "municipal_government_notice",
        "title": "市人民政府关于公布2025年度十堰市历史建筑名录的通知（十政发〔2026〕4号，14处，全在张湾区）",
        "org": "十堰市人民政府门户网站",
        "pub_date": "2026-02-08",
        "url": "https://www.shiyan.gov.cn/xxgk/zc_67263/qt/202603/t20260312_4910349.shtml",
        "authority": "A",
        "notes": "2025年度14处全部在张湾区（智能体核读）：原64厂5栋建筑（东风设备制造厂脉络）与62厂体育馆等三线建筑；与2024年度104处（十政发〔2024〕10号，茅箭33/张湾30/郧阳41）构成十堰市级批次体系。",
    },
}


def _sy(record_id: str, name: str, dc: str, cat: str, status: str, src: list, kind: str, year: str, material: str, tech: str, social: str, use: str, notes: str, aliases: list) -> dict:
    return {
        "inventory_id": record_id,
        "name": name,
        "city": "十堰市",
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
    _sy("HBI-SY-043", "国营三六一一厂生活配套建筑群（电影院、办公楼、商场）", "丹江口市浪河镇土门沟村", "三线军工工业",
        "丹江口市第三批历史建筑（丹政发〔2024〕6号，2024-05-29公布，名录3处：电影院2160㎡、办公楼3550㎡、商场2360㎡，70年代）", ["djk_batch3_2024"], "industrial_social_site", "70年代",
        "三六一一厂生活配套建筑3处（电影院、办公楼、商场，土门沟村）；建筑形制与内部格局待现场测绘",
        "三线军工企业厂前区生活配套（文娱/办公/商业）的完整组群形制",
        "三六一厂职工与浪河镇三线厂区生活记忆",
        "以第三批历史建筑身份正式公布保护；现状用途与产权待核",
        "直接取自丹政发〔2024〕6号红头文件扫描图（A级，逐页识读）；3处合并记录以保持厂区配套完整；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["三六一一厂"],
    ),
    _sy("HBI-SY-044", "国营三六零七厂生活配套建筑群（电影院、办公楼、商场）", "丹江口市浪河镇代湾村", "三线军工工业",
        "丹江口市第三批历史建筑（丹政发〔2024〕6号，名录3处：电影院1260㎡、办公楼2870㎡、商场1590㎡，60年代）", ["djk_batch3_2024"], "industrial_social_site", "60年代",
        "三六零七厂生活配套建筑3处（电影院、办公楼、商场，代湾村）；保存状况待现场测绘",
        "三线厂厂前区建筑群（代湾村）",
        "三六零七厂职工与代湾村三线生活记忆",
        "以第三批历史建筑身份正式公布保护；现状用途与产权待核",
        "直接取自丹政发〔2024〕6号红头文件扫描图（A级，逐页识读）；3处合并记录；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["三六零七厂"],
    ),
    _sy("HBI-SY-045", "国营三六零二厂生活配套建筑群（电影院、百货大楼、办公楼）", "丹江口市浪河镇青莫社区", "三线军工工业",
        "丹江口市第三批历史建筑（丹政发〔2024〕6号，名录3处：电影院1375㎡、百货大楼1790㎡、办公楼3586㎡，70年代）", ["djk_batch3_2024"], "industrial_social_site", "70年代",
        "三六零二厂生活配套建筑3处（电影院、百货大楼、办公楼，青莫社区）；保存状况待现场测绘",
        "三线厂厂前区含百货大楼的商业配套形态",
        "三六零二厂职工与青莫社区三线生活记忆",
        "以第三批历史建筑身份正式公布保护；现状用途与产权待核",
        "直接取自丹政发〔2024〕6号红头文件扫描图（A级，逐页识读）；3处合并记录；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["三六零二厂"],
    ),
    _sy("HBI-SY-046", "原64厂建筑群（5栋）", "十堰市张湾区", "三线军工工业",
        "十堰市2025年度历史建筑名录（十政发〔2026〕4号，2026-02-08公布，14处之列，张湾区原64厂5栋建筑）", ["shiyan_batch2025_2026"], "industrial_building", "待核",
        "原64厂5栋建筑（张湾区）；64厂为东风设备制造（修造）脉络专业厂，栋型与保存状态待现场测绘",
        "二汽专业厂设备制造与修配工艺脉络",
        "64厂职工与张湾区三线厂区记忆",
        "以2025年度历史建筑身份正式公布保护；现状用途待核",
        "直接取自十政发〔2026〕4号名录（A级，智能体核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["64厂"],
    ),
    _sy("HBI-SY-047", "62厂体育馆", "十堰市张湾区", "三线军工工业",
        "十堰市2025年度历史建筑名录（十政发〔2026〕4号，2026-02-08公布，14处之列）", ["shiyan_batch2025_2026"], "industrial_social_site", "待核",
        "62厂体育馆建筑本体；规模与保存状态待现场测绘",
        "三线专业厂体育设施的建筑形制",
        "62厂职工体育文娱记忆",
        "以2025年度历史建筑身份正式公布保护；现状用途待核",
        "直接取自十政发〔2026〕4号名录（A级，智能体核读）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["62厂"],
    ),
    _sy("HBI-SY-048", "霍河大坝坝沿", "十堰市竹山县城关镇刘家山村", "水利水电工程",
        "竹山县第一批历史建筑保护名单（竹政办发〔2023〕27号，2023-08-09公布，名录第11项，20世纪70年代）", ["zhushan_batches_2023_2024"], "industrial_utility_site", "20世纪70年代",
        "霍河水库大坝坝体及相关设施（刘家山村）；坝长、坝高与砌筑形式待现场测绘",
        "70年代县域水利水电枢纽的大坝筑造工艺（竹山名录中唯一大型水利水电构筑物）",
        "霍河水库建设者与堵河流域水利开发记忆",
        "以第一批历史建筑身份正式公布保护；水库运行状态待水利部门核",
        "直接取自竹政办发〔2023〕27号名单（A级，智能体核读原文）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["霍河大坝"],
    ),
    _sy("HBI-SY-049", "竹山堵河大桥", "十堰市竹山县城关镇人民路", "公路交通工业",
        "竹山县第二批历史建筑保护名单（竹政办发〔2024〕19号，2024-07-11公布，名录第20项，建国后）", ["zhushan_batches_2023_2024"], "industrial_transport_site", "建国后",
        "堵河大桥建筑本体（人民路，跨堵河）；桥型、跨径与保存状态待现场测绘",
        "建国后堵河干流大桥的公路桥梁工艺（竹山两批31处中唯一现代基础设施）",
        "堵河两岸通行与竹山县城交通门户记忆",
        "以第二批历史建筑身份正式公布保护；通行状态待核",
        "直接取自竹政办发〔2024〕19号名单（A级，智能体核读原文）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
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
    print(f"wave_cl_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
