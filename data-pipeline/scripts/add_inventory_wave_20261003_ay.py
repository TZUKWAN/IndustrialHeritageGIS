from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "huanggang_heritage_buildings_2024": {
        "source_type": "municipal_government_notice",
        "title": "黄冈市人民政府关于公布市区第三批历史建筑名录的通知（共25处）",
        "org": "黄冈市人民政府门户网站",
        "pub_date": "2024-08-29",
        "url": "https://www.hg.gov.cn/zwgk/public/6636765/1416680.html",
        "authority": "A",
        "notes": "市区第三批25处历史建筑名录（HGLSJZ037-061）正文附完整表：第16-25项为棉朵朵城市微度假中心2-11号楼，即原叶路洲棉花采购站轧花/剥绒车间、皮棉打包楼、籽棉/皮棉/备用品/储备仓库、储水塔与视望台、职工宿舍及办公楼（1965年至八十年代末陆续建设，名录逐栋载明原工业功能与2023年活化改造用途——游客服务中心、剧场、时光博物馆、水吧茶室观光塔、乡村餐厅、农研体验馆、亲子活动馆、美食集、酒店）；第10项原黄州区红星门市部（1974年，工商联红星商场门市部沿革，现清源门社区办公楼）。",
    },
}


RECORDS = [
    {
        "inventory_id": "HBI-HG-015",
        "name": "叶路洲棉花采购站旧址建筑群（棉朵朵城市微度假中心）",
        "city": "黄冈市",
        "district_county": "黄州区堵城镇叶路洲",
        "industry_category_l1": "棉花加工与棉产流通",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "黄冈市市区第三批历史建筑（2024年8月29日公布，名录第16-25项共10栋，编号HGLSJZ052-061）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["huanggang_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "名录逐栋载明10栋建筑：轧花生产与剥绒车间（2号楼，八十年代初）、皮棉加工打包楼（3号楼，1965年建三层砖混）、皮棉商品库（4号楼）、备用品仓库（5号楼，六十年代末红砖拱形屋面钢索拉结）、储水塔与安全保卫视望台（6号楼，局部三层）、皮棉储备仓库（7号楼）、棉籽仓库与加工维修车间及棉短绒短化车间（8号楼）、生产厂房（9号楼）、职工宿舍（10号楼）、职工宿舍及办公场所（11号楼，八十年代末三层，曾为叶路洲办事处及堵城公社会议场所）；均位于叶路洲沿江路",
            "technical_memory": "棉花采购站籽棉收购—轧花—皮棉打包—储运—棉籽深加工的完整工艺链建筑载体；名录记载大跨度桁架结构与木屋面厂房、红砖拱顶钢索拉结仓库等典型工业建造做法",
            "social_memory": "堵城棉纺产业与叶路洲棉农交售记忆；采购站职工生产生活与堵城公社时期会议场所记忆",
            "current_use_or_loss": "2023年活化改造为棉朵朵城市微度假中心：游客服务中心、剧场、时光博物馆、水吧茶室与观光瞭望塔、乡村餐厅、农研体验馆、亲子活动体验馆、乡村美食集、酒店，为黄冈工业遗存整体活化的代表性案例；改造后原工艺设备留存情况待现场核验",
        },
        "notes": "直接取自黄冈市政府市区第三批历史建筑名录正文表（A级，逐栋含原功能、年代与改造用途）；历史建筑保护不等于工业遗产法定认定；各单体坐标与改造后设备遗存待现场核验；坐标未核验保持待核。",
        "aliases": ["叶路洲棉花采购站", "棉朵朵城市微度假中心", "堵城棉花采购站"],
        "asset_kind": "industrial_site",
    },
    {
        "inventory_id": "HBI-HG-016",
        "name": "原黄州区红星门市部（现清源门社区办公楼）",
        "city": "黄冈市",
        "district_county": "黄州区沙街",
        "industry_category_l1": "商贸服务与基层文化供应",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "黄冈市市区第三批历史建筑（2024年8月29日公布，名录第10项，编号HGLSJZ046；1974年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["huanggang_heritage_buildings_2024"],
        "cultural_evidence": {
            "material_carriers": "砖混结构商业建筑一处（沙街4号，清源门老城墙前），中轴对称、平面规矩；结构与修缮状况待现场测绘",
            "technical_memory": "七十年代县城商业门市部建筑形制",
            "social_memory": "工商联红星商场红一门市部、九十年代烟草公司经营部、2005年后信访局办公用房至社区办公场所的用途更替，映射黄州老城商业与基层治理变迁",
            "current_use_or_loss": "经修缮加固后现为清源门社区办公场所，保护利用状态良好；改造中原始商业界面留存情况待核",
        },
        "notes": "直接取自黄冈市政府市区第三批历史建筑名录正文表（A级）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["红星商场红一门市部"],
        "asset_kind": "industrial_trade_site",
    },
]


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
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_ay_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
