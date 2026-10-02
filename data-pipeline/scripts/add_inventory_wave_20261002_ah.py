from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "hanchuan_makou_auto_repair_2026": {
        "source_type": "provincial_media_industrial_renewal",
        "title": "老厂房‘又一春’：汉川马口镇以‘微更新’唤醒三线工业遗存",
        "org": "湖北日报客户端",
        "pub_date": "2026-06-29",
        "url": "https://news.hubeidaily.net/mobile/c_5692565.html",
        "authority": "B",
        "notes": "湖北日报客户端报道汉川市马口镇省汽修老旧厂房活化改造项目开工，明确厂区位于金马大道与S105省道之间、占地约120亩，红砖车间和钢构建筑保存较好，项目从3509厂区闲置空间更新为马口烧烤文创园；用于补强工业文化载体和现状利用，不替代原企业全称、产权与设备清单核验。",
    },
    "jingmen_jinlongquan_democratic_street_2025": {
        "source_type": "provincial_culture_tourism_media",
        "title": "民主街：历时三年修缮的古街火起来",
        "org": "湖北省文化和旅游厅/湖北日报",
        "pub_date": "2025-08-27",
        "url": "https://wlt.hubei.gov.cn/bmdt/szyw/jm/202508/t20250827_5756343.shtml",
        "authority": "A",
        "notes": "省文旅厅转载湖北日报报道，明确荆门民主街修缮后仍可见金龙泉啤酒厂旧址坚固厂房、高烟囱和工人文化宫，并将其作为荆门工业重镇记忆的一组空间载体；具体厂界、设备和产权待核。",
    },
}


UPDATES: dict[str, dict[str, Any]] = {
    "HBI-XG-002": {
        "source_keys": ["xg_hanchuan_auto_2026", "hanchuan_makou_auto_repair_2026"],
        "cultural_evidence": {
            "material_carriers": "20世纪70年代红砖车间、钢构建筑、梁柱和老式门窗；湖北日报现场报道确认省汽修老厂房与3509厂区红砖/钢构遗存保存较好",
            "technical_memory": "汽车维修、机械加工和地方工业服务；原省汽修/3509厂的生产组织、设备和产品谱系待厂志核验",
            "social_memory": "马口工业镇职工、居民和老厂房生活记忆；三线企业社区、工人名录和口述史待采集",
            "current_use_or_loss": "2026年启动马口烧烤文创园微更新，项目占地约120亩，分期建设并坚持轻干预保留原构件；产权、开放边界和后续运营待核",
        },
        "notes": "湖北日报两条报道确认马口省汽修老厂房与3509厂区的三线工业遗存语境、红砖/钢构保存状态和文创园更新方向；原企业全称、厂区构成、设备和权属仍待档案核验。",
    },
    "HBI-JM-008": {
        "source_keys": ["jingmen_jinlongquan", "jingmen_jinlongquan_democratic_street_2025"],
        "district_county": "东宝区民主街片区（具体厂界待核）",
        "cultural_evidence": {
            "material_carriers": "金龙泉啤酒厂旧址坚固厂房、烟囱及民主街工业空间；具体生产线、设备和厂界待测绘",
            "technical_memory": "啤酒酿造、食品饮料生产和荆门地方工业技术记忆；工艺、设备和厂志待补",
            "social_memory": "荆门工业重镇、工人文化宫和市民共同记忆；职工社区与企业文化资料待采集",
            "current_use_or_loss": "旧址位于修缮后的民主街历史文化空间中，报道确认与工人文化宫共同展示工业记忆；产权、开放与活化边界待核",
        },
        "notes": "省文旅厅2025年报道与既有来源共同确认金龙泉啤酒厂旧址位于民主街工业记忆空间，补足厂房、烟囱和工人文化宫的空间关系；不推断完整生产区或法定遗产级别。",
    },
    "HBI-JM-012": {
        "source_keys": ["jingmen_jinlongquan", "jingmen_jinlongquan_democratic_street_2025"],
        "notes": "省文旅厅报道明确民主街修缮后仍可见金龙泉啤酒厂旧址与工人文化宫共同记录荆门工业重镇记忆；本条作为工人文化与工业社区载体单列，建筑沿革、产权和开放方式待核。",
    },
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    by_id = {row["inventory_id"]: row for row in records}
    for key, value in NEW_SOURCES.items():
        if key in sources and sources[key] != value:
            raise SystemExit(f"conflicting source: {key}")
        sources[key] = value
    for inventory_id, patch in UPDATES.items():
        if inventory_id not in by_id:
            raise SystemExit(f"missing update target: {inventory_id}")
        for key, value in patch.items():
            by_id[inventory_id][key] = value
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_ah_sources={len(NEW_SOURCES)} added_records=0 updated_records={len(UPDATES)} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
