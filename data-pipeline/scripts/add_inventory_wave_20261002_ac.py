from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "suizhou_silk_reuse_2026": {
        "source_type": "municipal_media_urban_renewal",
        "title": "马泽江调研规委会审议项目规划和‘断头路’工作",
        "org": "随州日报",
        "pub_date": "2026-03-25",
        "url": "https://szrb.suiw.cn/szrb/20260325/html/content_20260325001002.htm",
        "authority": "B",
        "notes": "随州日报报道随州市委书记现场调研缫丝厂区改造，明确缫丝厂承载随州工业记忆和城市发展印记，要求保护与发展统一、推动厂区活化改造并植入多元业态；原页面当前抓取超时，保留搜索结果与官方报纸 URL，具体规划批复和厂区边界待核。",
    },
    "suizhou_silk_community_2016": {
        "source_type": "municipal_media_enterprise_community",
        "title": "袁善谋督办检查‘禁鞭’工作",
        "org": "随州日报",
        "pub_date": "2016-01-27",
        "url": "https://szrb.suiw.cn/shtml/szrb/20160127/134339.shtml",
        "authority": "B",
        "notes": "随州日报明确曾都区东城街道缫丝社区是典型企业社区，厂房和居民楼房老旧；用于补足缫丝厂区与职工社区的社会记忆和物质环境，不替代厂志、土地档案和建筑测绘。",
    },
}


def ev(material: str, technical: str, social: str, current: str) -> dict[str, str]:
    return {
        "material_carriers": material,
        "technical_memory": technical,
        "social_memory": social,
        "current_use_or_loss": current,
    }


NEW_RECORD = {
    "inventory_id": "HBI-SZ-011",
    "name": "随州缫丝厂区—缫丝社区工业文化景观",
    "city": "随州市",
    "district_county": "曾都区东城街道（具体厂界待核）",
    "industry_category_l1": "纺织工业",
    "recognition_level": "city_planning",
    "recognition_status": "随州日报确认的城市更新与企业社区对象；未见法定工业遗产认定",
    "record_status": "source_confirmed",
    "geocode_status": "pending",
    "source_keys": ["suizhou_silk_reuse_2026", "suizhou_silk_community_2016"],
    "cultural_evidence": ev(
        "缫丝厂区原厂房、缫丝社区居民楼及周边公共空间；2016年报道确认厂房和居民楼房老旧，具体建筑、设备和厂界待测绘",
        "缫丝生产、蚕茧加工和纺织企业组织的技术记忆；现有公开报道未列生产线、机器和工艺档案，需查厂志与企业档案",
        "缫丝社区作为典型企业社区，连接产业工人、居民生活和随州城市发展记忆；社区口述、老照片、厂史和生活服务设施待采集",
        "2026年随州日报报道市级规划现场调研缫丝厂区改造，提出保护与发展统一、推动厂区活化并植入多元业态；项目批复、产权、环境风险和开放边界待核",
    ),
    "notes": "随州日报2026年现场报道将缫丝厂区改造列为城市更新项目，并明确其承载随州工业记忆和城市发展印记；2016年报道确认缫丝社区是典型企业社区，厂房和居民楼房老旧。本条把厂区与职工社区作为一个工业文化景观登记，暂不推断原缫丝厂完整厂界、具体生产设备或法定遗产级别。",
    "aliases": ["随州缫丝厂", "缫丝厂区改造", "缫丝社区"],
    "asset_kind": "industrial_residential_landscape",
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    by_id = {row["inventory_id"]: row for row in records}
    names = {row["name"] for row in records}
    old = by_id.get(NEW_RECORD["inventory_id"])
    added = 0
    if old is None:
        if NEW_RECORD["name"] in names:
            raise SystemExit("conflicting duplicate name")
        records.append(NEW_RECORD)
        added = 1
    elif old != NEW_RECORD:
        raise SystemExit("conflicting duplicate record")
    for key, value in NEW_SOURCES.items():
        if key in sources and sources[key] != value:
            raise SystemExit(f"conflicting source: {key}")
        sources[key] = value
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_ac_sources={len(NEW_SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
