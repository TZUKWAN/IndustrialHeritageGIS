from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCE_UPDATE = {
    "hubei_archive_catalog_1965": {
        "source_type": "provincial_archive_catalog",
        "title": "省直档案（老）开放档案目录（1965—1966征地档案卷，SZ 67-2全宗）",
        "org": "湖北省档案馆",
        "pub_date": None,
        "url": "https://www.hbda.gov.cn/searchitem/207_8?page=1969",
        "authority": "A",
        "notes": "2026-10-05扩页扫描（page=1968/1969，原始HTML存档 raw/hbda_scan/）新增命中：SZ 67-2-1305 宜昌市与秭归、宜都、当阳县修建公路码头、新建砖瓦厂等征用土地；SZ 67-2-1307 襄阳专署、襄阳县建煤货场、棉花储备仓库、石油库、第三新华印刷厂征用土地（1965-1966，长期）；SZ 67-2-1308 襄樊市化肥厂、棉纺织印染厂纺织厂扩大初步设计新建厂征用土地（1966）；SZ 67-2-1309 襄阳冷冻厂征用土地报告的批复、协定书、平面图；SZ 67-2-1310 随县修建鱼池、粮食储备仓库征用土地；SZ 67-2-1311 枣阳县石油公司货场油库及枣阳环城拖拉机站申请征用土地；SZ 67-2-1313 黄陂县新建储备粮仓征用土地批复及协议书；SZ 67-2-1314 安陆兴建粮食储备仓库、棉花仓库、粮食加工厂、棉花轧花厂征用土地；SZ 67-2-1315 松滋清江矿山机械厂、江汉石油勘探处及天门、石首建库建厂征用土地；SZ 67-2-1316 潜江县商业局、公安县砖瓦厂、荆州军分区后勤部征用土地——全部为批复/协定书/图纸级档案卷。",
    }
}


NOTES_APPENDS = {
    "HBI-XIANGYANG-028": "2026-10-05省档案馆目录扩页扫描档号精确化：SZ 67-2-1307（1965-1966，长期）《关于襄阳专署、襄阳县建煤货场、棉花储备仓库、石油库、第三新华印刷厂征用土地报告的批复、协定书、平面图》——批复/协定书/平面图级档案卷，线下调档可直接报档号；原始HTML存档 raw/hbda_scan/。",
    "HBI-XIANGYANG-029": "2026-10-05档号精确化：SZ 67-2-1308（1966，长期）《关于襄樊市化肥厂、棉纺织印染厂的纺织厂扩大初步设计新建厂征用土地报告、初步设计意见及议定书、图纸》——市属两厂同卷，与县属肖湾厂（1975年筹建）进一步区分，线下调档可直接报档号。",
    "HBI-XIANGYANG-030": "2026-10-05档号精确化：与化肥厂同卷 SZ 67-2-1308（1966，长期）含棉纺织印染厂扩大初步设计新建厂征用土地报告、初步设计意见及议定书、图纸，线下调档可直接报档号。",
    "HBI-XIANGYANG-031": "2026-10-05档号精确化：SZ 67-2-1309（1965-1966，长期）《湖北省人委关于襄阳冷冻厂征用土地报告的批复、协定书、平面图》——批复/协定书/平面图级档案卷，线下调档可直接报档号。",
    "HBI-XIANGYANG-032": "2026-10-05档号精确化（煤货场/棉花储备仓库子项）：SZ 67-2-1307（1965-1966，长期）《关于襄阳专署、襄阳县建煤货场、棉花储备仓库、石油库、第三新华印刷厂征用土地报告的批复、协定书、平面图》——与本条档案题名完全对应（含平面图），煤货场子项的实体线索显著增强，线下调档可直接报档号。",
    "HBI-XIANGYANG-033": "2026-10-05档号精确化：SZ 67-2-1311（1965，长期）《湖北省人委关于枣阳县石油公司兴建货场油库报告批复及枣阳环城拖拉机站申请征用土地报告》——拖拉机站征地报告与石油公司货场同卷，线下调档可直接报档号。",
    "HBI-WUHAN-065": "2026-10-05档号精确化：SZ 67-2-1313（1965，长期）《湖北省人委关于黄陂县新建储备粮仓征用土地报告的批复及协议书等》——批复及协议书级档案卷，与前川街道五里粮库现役收储语境衔接，线下调档可直接报档号。",
    "HBI-XG-013": "2026-10-05档号精确化：SZ 67-2-1314（1965，长期）《湖北省人委关于安陆兴建粮食储备仓库、棉花仓库、粮食加工厂、棉花轧花厂征用土地的报告、批复及图纸》——档案题名与本条对象名完全吻合（粮食储备仓库+棉花仓库+粮食加工厂+棉花轧花厂四项齐备），含图纸，线下调档可直接报档号。",
    "HBI-JZ-015": "2026-10-05档号补充：SZ 67-2-1315（1965-1966，长期）《湖北省人委关于松滋清江矿山机械厂、江汉石油勘探处以及天门、石首建库建厂征用土地批复、报告、图纸等》——1965年征地批复档号补入（与本条已确认的三线军工沿革互证）。",
    "HBI-JZ-016": "2026-10-05档号精确化：SZ 67-2-1316（1965-1966，长期）《潜江县商业局、公安县砖瓦厂、荆州军分区后勤部征用土地报告的批复、协议等》——公安县砖瓦厂征地批复与协议档号精确化（与2015年全县关闭方案构成首尾断代），线下调档可直接报档号。",
    "HBI-SZ-012": "2026-10-05档号补充：SZ 67-2-1310（1965-1966，长期）《湖北省人委关于随县修建鱼池、粮食储备仓库征用土地的报告、批复、图纸等》——1965年征地批复档号补入（与本条厉山镇北岗村机构地址互证）。",
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    if sources.get("hubei_archive_catalog_1965") != SOURCE_UPDATE["hubei_archive_catalog_1965"]:
        if "hubei_archive_catalog_1965" not in sources:
            raise SystemExit("source not found")
        sources["hubei_archive_catalog_1965"] = SOURCE_UPDATE["hubei_archive_catalog_1965"]
        updated = 1
    else:
        updated = 0
    for record_id, notes_append in NOTES_APPENDS.items():
        record = next((row for row in records if row["inventory_id"] == record_id), None)
        if record is None:
            raise SystemExit(f"record not found: {record_id}")
        if notes_append not in record["notes"]:
            record["notes"] = record["notes"] + notes_append
            updated += 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_cp_updated={updated} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
