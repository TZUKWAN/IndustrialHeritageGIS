from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "jingshan_minglu_2022": {
        "source_type": "county_government_notice",
        "title": "市人民政府关于公布京山市历史建筑名录的通知（京政发〔2022〕9号，55处，红头PDF已逐页核读）",
        "org": "京山市人民政府（荆门市政府站群京山子站）",
        "pub_date": "2022-07-02",
        "url": "http://114.jingmen.gov.cn/art/17212_1094857.html",
        "authority": "A",
        "notes": "京政发〔2022〕9号公布55处历史建筑（红头PDF附件4页含完整名单表，已逐页核读）：惠亭水库大坝（温泉街道桂花台社区，序号06，京山最大水利枢纽1958年动工）、三步墩堤坝（新市街道荷花堰村一组，序号02）及古桥/古井/民居/祠寺/革命旧址等；2024年发布名录修改版（55处，市住建局2024-05-20征求意见无反馈后调整，微信公众号载体核读）。",
    },
    "shayang_batches": {
        "source_type": "county_government_work_summary",
        "title": "沙洋县历史建筑工作官方记录（两批41处：第一批11处含沙洋码头旧址、第二批30处龙凤亭等）",
        "org": "沙洋县住房和城乡建设局（沙洋县人民政府网）",
        "pub_date": "2026-03-30",
        "url": "https://www.shayang.gov.cn/art/2026/3/30/art_24863_1212000.html",
        "authority": "A",
        "notes": "县住建局官方总结载明：截至2025年底全县历史建筑41处（第一批11处、第二批30处“龙凤亭等”），2024-2025年完成新增30处三维扫描测绘建档并上传住建部历史建筑数据平台；2022-2023年总结载明县人民政府发布《关于公布沙洋县第一批历史建筑保护名单的通知》，“沙洋码头旧址”等11处列入，已完成沙洋码头旧址、沈集丁坪旧址、后港浙江会馆旧址3处修缮（另见 https://www.shayang.gov.cn/art/2023/2/28/art_12145_959345.html 与 https://www.shayang.gov.cn/art/2025/4/1/art_24863_1143671.html）。两批完整名单原文未上网，仅官方总结点名沙洋码头旧址/后港浙江会馆旧址/沈集丁坪旧址/龙凤亭等。",
    },
}


def _jm(record_id: str, name: str, dc: str, cat: str, status: str, kind: str, year: str, material: str, tech: str, social: str, use: str, notes: str, aliases: list) -> dict:
    return {
        "inventory_id": record_id,
        "name": name,
        "city": "荆门市",
        "district_county": dc,
        "industry_category_l1": cat,
        "recognition_level": "municipal_historical_building",
        "recognition_status": status,
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["jingshan_minglu_2022", "shayang_batches"],
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
    _jm("HBI-JM-021", "惠亭水库大坝", "京山市温泉街道桂花台社区", "水利水电工程",
        "京山市历史建筑名录（京政发〔2022〕9号，2022-07-02公布，序号06；2024年修改版保留）", "industrial_utility_site", "1958年动工",
        "惠亭水库大坝坝体（京山最大水利枢纽，1958年动工）；坝长、坝高与溢洪设施待现场测绘",
        "1958年动工的大型水库筑坝工艺与灌区渠系配套工程",
        "京山人民兴建惠亭水库的集体劳动记忆与灌区灌溉保障",
        "以历史建筑身份正式公布保护（2022版与2024修改版名录均保留）；水库运行管理现状待水利部门核",
        "直接取自京政发〔2022〕9号红头PDF名单（A级，序号06）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["惠亭水库"],
    ),
    _jm("HBI-JM-022", "沙洋码头旧址", "荆门市沙洋县（汉江沿岸）", "港口与水运工业",
        "沙洋县第一批历史建筑保护名单（11处之一，已修缮）", "industrial_transport_site", "待核",
        "沙洋码头旧址建筑与设施（汉江沿岸，已完成修缮）；码头形制与岸线范围待现场测绘",
        "沙洋为两千余年历史港口、“小汉口”商埠——汉江中游码头的水运集散与货物装卸体系",
        "沙洋港水运商埠与码头工人记忆",
        "以第一批历史建筑身份纳入保护体系并已完成修缮；使用与开放状态待核",
        "直接取自沙洋县住建局官方工作总结（A级，两批41处口径与3处修缮名单）；码头始建年代待地方志核验；坐标未核验保持待核。",
        ["沙洋港码头"],
    ),
    _jm("HBI-JM-023", "后港浙江会馆旧址", "荆门市沙洋县后港镇", "商贸服务与基层文化供应",
        "沙洋县第一批历史建筑保护名单（11处之一，已修缮）", "industrial_trade_site", "待核",
        "浙江会馆旧址建筑本体（后港镇）；会馆格局（正殿/厢房/戏楼）待现场测绘",
        "外来商帮会馆的行会组织与客居商贸服务建筑形制（后港为长湖水运商埠）",
        "浙江商帮客居后港经商与会馆联谊的商贸记忆",
        "以第一批历史建筑身份纳入保护体系并已完成修缮；使用与开放状态待核",
        "直接取自沙洋县住建局官方工作总结（A级，两批41处口径与3处修缮名单）；会馆始建年代待地方志核验；坐标未核验保持待核。",
        ["后港浙江会馆"],
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
    print(f"wave_cn_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
