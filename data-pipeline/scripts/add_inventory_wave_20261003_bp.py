from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCE_UPDATE = {
    "enshi_heritage_buildings_batch1_2023": {
        "source_type": "county_city_government_notice",
        "title": "恩施市人民政府关于公布第一批历史建筑的通知（恩市政发〔2023〕54号，13处）",
        "org": "恩施市人民政府门户网站（政策文件PDF）",
        "pub_date": "2023-06-19",
        "url": "http://www.es.gov.cn/xxgk/zc/zcwj/202412/P020241226395463833880.pdf",
        "authority": "A",
        "notes": "恩市政发〔2023〕54号（2023年6月19日成文；2024年12月重新挂网PDF，其文本层将文号连读为“2023154”，现据市政府其他主动公开文件列表权威显示校正为〔2023〕54号）公布湖北省邮电管理局旧址等第一批13处历史建筑，PDF含名录表与逐处简介（已下载文本核读，本地存档 raw/enshi_heritage/）：第4项湖北省邮电管理局旧址（六角亭街道和平街，抗战时期为国民党湖北省邮电管理局、解放后为恩施县邮电局，现房屋闲置）；第7项宜红茶厂旧址（芭蕉侗族乡集镇，1938年建，中国茶叶公司技士办机制厂首开机制茶，占地3818平方米，多层砖混结构）；另有恩施地区农校分校教室/实验楼（1952-1954仿苏式）、公园街天主教堂及多处老屋祠堂。",
    }
}


RECORD_UPDATES = {
    "HBI-ES-022": {
        "recognition_status": "恩施市第一批历史建筑（恩市政发〔2023〕54号名录第7项；1938年建）",
    },
    "HBI-ES-023": {
        "recognition_status": "恩施市第一批历史建筑（恩市政发〔2023〕54号名录第4项）",
    },
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    updated = 0
    current = sources.get("enshi_heritage_buildings_batch1_2023")
    if current is None:
        raise SystemExit("source not found")
    if current != SOURCE_UPDATE["enshi_heritage_buildings_batch1_2023"]:
        sources["enshi_heritage_buildings_batch1_2023"] = SOURCE_UPDATE["enshi_heritage_buildings_batch1_2023"]
        updated += 1
    for record_id, patch in RECORD_UPDATES.items():
        record = next((row for row in records if row["inventory_id"] == record_id), None)
        if record is None:
            raise SystemExit(f"record not found: {record_id}")
        if record["recognition_status"] != patch["recognition_status"]:
            record["recognition_status"] = patch["recognition_status"]
            updated += 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_bp_updated={updated} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
