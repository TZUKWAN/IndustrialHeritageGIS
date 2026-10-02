from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCE = {
    "renminribao_shashi_machine_1980": {
        "source_type": "newspaper_archive_machine_industry",
        "title": "湖北沙市机床工业专业化协作报道",
        "org": "人民日报历史版（新华社武汉电）",
        "pub_date": "1980-04-22",
        "url": "https://cn.govopendata.com/renminribao/1980/04/22/3/",
        "authority": "C",
        "notes": "人民日报历史版报道沙市机床一厂钻床畅销、机床三厂生产空气压缩机，并记录机床公司成立后的专业化协作和技术组织；用于补强沙市机床厂谱系，不替代厂址、设备和现状核验。",
    }
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    if "renminribao_shashi_machine_1980" in sources and sources["renminribao_shashi_machine_1980"] != SOURCE["renminribao_shashi_machine_1980"]:
        raise SystemExit("conflicting source")
    sources.update(SOURCE)
    row = next(item for item in records if item["inventory_id"] == "HBI-JZ-018")
    row["source_keys"] = ["hubei_industry_export_1989", "shashi_first_machine_history_2022", "renminribao_shashi_machine_1980"]
    row["aliases"] = ["荆州机床厂", "沙市第一机床厂", "沙市第二机床厂", "沙市第三机床厂", "沙市机床三厂", "沙市机床厂（待核）"]
    row["cultural_evidence"]["technical_memory"] = "摇臂钻床、磨床、空气压缩机和机床专业化协作技术；人民日报1980年报道补足沙市机床一厂钻床、机床三厂空压机和机床公司协作生产关系，设备档案待补"
    row["notes"] = "省政府公报提供荆州机床厂历史名单线索，区域回忆资料补足沙市第一机床厂建厂、老厂门和摇臂钻床生产记忆，人民日报1980年报道补足机床一厂/三厂专业化协作与空压机生产；名称对应关系、厂址和实体边界待档案核对。"
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_ap_sources=1 added_records=0 updated_records=1 total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
