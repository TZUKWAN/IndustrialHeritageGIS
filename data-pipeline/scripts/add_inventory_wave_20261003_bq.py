from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCE_UPDATE = {
    "shennongjia_logging_team_2023": {
        "source_type": "national_park_official_media",
        "title": "从伐木工到护林人，守护华中屋脊的金山银山",
        "org": "神农架国家公园",
        "pub_date": "2023-09-18",
        "url": "https://www.snjnationalpark.com/hbxd/xhjs/202309/t4648451.shtml",
        "authority": "A",
        "notes": "神农架国家公园官网林二代许文操口述史（2023-09-18发布；2026-10-03经301重定向抓取成功并全文核读，本地存档 raw/snj_duanjiangping.html）：1980-1983年在木鱼林场断江坪队工作（先养路班后伐木班五班，全队5个伐木班约20人/班，林业队另有蔬菜班、后勤班、养路班，总数数百人）；断江坪即今里叉河、云盘、后河一带，入口在今木鱼小学处，主伐栎类与水青冈；全林区4林场（木鱼/温水/徐家庄/红坪）、林管局3支运输车队（兴山/木鱼/阳儿湾）；年任务两三千方，班配油锯2把；工艺为油锯采伐—打枝烧毁防虫—山上置放一冬—次年春锯断—绞盘机钢索滑轮组集材—运秭归屈原庙木材场统销；木板房营地一人一间、铝合金饭盒背壶、冬驻山同期护林；新工月薪27.5元、转正32.9元，粮票47斤/月；民兵持枪护林；每年春季义务植树（九成种日本落叶松）；2000年起天保工程退耕还林（木鱼镇一万多亩）、2017年林区大改革。",
    }
}


SNJ005_PATCH = {
    "record_status": "source_confirmed",
    "recognition_status": "神农架国家公园官网林二代口述史确认的木鱼林场断江坪伐木队（1980-1983年在队口述）；队址语境、组织与工艺有官方来源，具体队址建筑与设备实物待现场核验",
    "material_carriers": "断江坪林业队队址（今里叉河、云盘、后河一带，入口在今木鱼小学处）木板房营地（一人一间全木板钉装）、绞盘机钢索滑轮组集材设施、油锯2把/班等采伐工具；队址建筑与设施实物均无存证，待林场档案与现场核验",
    "technical_memory": "口述史完整记载伐木—集材—运销工艺链：油锯采伐（栎类、水青冈，直径14公分以下不作正规材）—打枝集中烧毁防白蚁—原木山上置放一冬—次年春锯断—绞盘机架山顶经钢索滑轮组转运山下—集中装载由林管局运输车队运秭归屈原庙木材场统销；队年任务两三千方",
    "social_memory": "断江坪林业队5个伐木班（每班约20人）加蔬菜班、后勤班、养路班共数百人；林二代接替父辈（父辈伐木受伤转采购）；木板房驻山十天半月、铝合金饭盒背壶、雪季封山回家；新工月薪27.5元/转正32.9元、粮票月47斤、翻毛皮鞋保暖大衣发放；民兵持枪护林；全家林区时代木鱼尚无正规街道",
    "current_use_or_loss": "1980年代伐木后林业队撤并，队址回归山林（口述指认今里叉河、云盘、后河一带）；2000年天保工程退耕还林（木鱼镇一万多亩，九成植日本落叶松）、2017年林区大改革，伐木时代设施无存证；由伐木转护林的转型记忆为神农架生态转型代表案例",
    "notes_append": "2026-10-03官方页面经301重定向抓取成功并全文核读，口述史细节补入四项证据并将本条自 research_candidate 升格为 source_confirmed（升格仅表示名称、沿革与队址语境有官方口述来源，不表示队址建筑与设备实物已核实）。",
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    updated = 0
    current = sources.get("shennongjia_logging_team_2023")
    if current is None:
        raise SystemExit("source not found")
    if current != SOURCE_UPDATE["shennongjia_logging_team_2023"]:
        sources["shennongjia_logging_team_2023"] = SOURCE_UPDATE["shennongjia_logging_team_2023"]
        updated += 1
    snj005 = next((row for row in records if row["inventory_id"] == "HBI-SNJ-005"), None)
    if snj005 is None:
        raise SystemExit("record not found: HBI-SNJ-005")
    for key in ("record_status", "recognition_status", "material_carriers", "technical_memory", "social_memory", "current_use_or_loss"):
        new_val = SNJ005_PATCH[key]
        if key in ("material_carriers", "technical_memory", "social_memory", "current_use_or_loss"):
            if snj005["cultural_evidence"][key] != new_val:
                snj005["cultural_evidence"][key] = new_val
                updated += 1
        elif snj005[key] != new_val:
            snj005[key] = new_val
            updated += 1
    if SNJ005_PATCH["notes_append"] not in snj005["notes"]:
        snj005["notes"] = snj005["notes"] + SNJ005_PATCH["notes_append"]
        updated += 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_bq_updated={updated} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
