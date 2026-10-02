from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "shashi_yangmatou_mohurd_2024": {
        "source_type": "district_government_official_media",
        "title": "住建部首批，洋码头历史文化街区列入！",
        "org": "荆州市沙市区人民政府网",
        "pub_date": "2024-08-22",
        "url": "http://www.shashi.gov.cn/ssqxw/ssyw/202408/t20240822_950520_zzb.shtml",
        "authority": "A",
        "notes": "住房城乡建设部《历史文化街区保护利用可复制经验做法清单（第一批）》将湖北省荆州市洋码头历史文化街区列入第三块“发挥街区文化教育宣传功能”部分；街区位于沙市区主城区，北靠荆江大堤、南临长江、西接轮渡码头、东至柳林洲，岸线约2公里；建立“荆江生态文化”科普教育示范基地、“吉祥巷”“沙市记忆”爱国主义教育基地，荆江水文化IP传播量200余万次、抖音话题参与1500万人次。另据市住更局信息公开列表（2026-06-03），三义街—得胜街、古城南门、胜利街西段、中山路—崇文街、沙市洋码头5处历史文化街区保护规划已公布。",
    },
}


JZ007_PATCH = {
    "source_keys_append": ["shashi_yangmatou_mohurd_2024"],
    "current_use_or_loss": "已改造为洋码头文创园，兼具文化展示、创意工坊和旅游休闲；2024年8月洋码头历史文化街区列入住建部《历史文化街区保护利用可复制经验做法清单（第一批）》，建有“荆江生态文化”科普教育示范基地与“吉祥巷”“沙市记忆”爱国主义教育基地，荆江水文化IP传播量200余万次；2026年6月沙市洋码头等5处历史文化街区保护规划公布；具体保护单元清单待核",
    "notes_append": "2024年8月住建部首批可复制经验做法清单收录、2026年6月街区保护规划公布（沙市区政府网与市住更局信息公开），街区身份从文创园升格为省级历史文化街区并获国家级经验推广。",
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    for key, source in SOURCES.items():
        if key in sources and sources[key] != source:
            raise SystemExit(f"conflicting source: {key}")
    sources.update(SOURCES)
    jz007 = next((row for row in records if row["inventory_id"] == "HBI-JZ-007"), None)
    if jz007 is None:
        raise SystemExit("record not found: HBI-JZ-007")
    updated = 0
    for key in JZ007_PATCH["source_keys_append"]:
        if key not in jz007["source_keys"]:
            jz007["source_keys"].append(key)
            updated = 1
    if jz007["cultural_evidence"]["current_use_or_loss"] != JZ007_PATCH["current_use_or_loss"]:
        jz007["cultural_evidence"]["current_use_or_loss"] = JZ007_PATCH["current_use_or_loss"]
        updated = 1
    if JZ007_PATCH["notes_append"] not in jz007["notes"]:
        jz007["notes"] = jz007["notes"] + JZ007_PATCH["notes_append"]
        updated = 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_bk_sources={len(SOURCES)} added_records=0 updated_records={updated} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
