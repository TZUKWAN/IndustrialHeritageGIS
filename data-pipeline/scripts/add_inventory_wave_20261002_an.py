from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "jingshan_light_machine_history_official": {
        "source_type": "enterprise_official_history",
        "title": "湖北京山轻工机械股份有限公司企业史",
        "org": "湖北京山轻工机械股份有限公司",
        "pub_date": None,
        "url": "https://www.jspackmach.com/about_index.html",
        "authority": "B",
        "notes": "企业官网企业史记载京山轻机1957年起航于农业机械化制造，后发展为包装机械、印刷机械和智能装备，并说明京山轻工机械厂及轻机工业园沿革；用于补强企业技术与组织谱系，不替代原宋河/新市厂区测绘和遗产认定。",
    },
    "shashi_first_machine_history_2022": {
        "source_type": "regional_media_worker_memory",
        "title": "‘热风’从这里吹过：原沙市市第一机床厂回忆",
        "org": "区域文史媒体（作者工厂回忆）",
        "pub_date": "2022-09-03",
        "url": "https://www.sohu.com/a/582268947_121124392",
        "authority": "C",
        "notes": "回忆文章记录沙市第一机床厂1956年建厂、20世纪70年代老厂门和办公楼、摇臂钻床生产及1980年国家产品质量金质奖；为工人回忆和图像线索，具体建筑保存、产权与现状待官方档案和现场核验。",
    },
}


UPDATES: dict[str, dict[str, Any]] = {
    "HBI-JM-018": {
        "source_keys": ["jingshan_mechanical_residential_2020", "hubei_industry_export_1989", "jingshan_light_machine_history_official"],
        "cultural_evidence": {
            "material_carriers": "原机械厂职工生活区住宅、道路、管网和公共空间；企业官网补充京山轻工机械厂与轻机工业园沿革，生产厂房与生活区边界待核",
            "technical_memory": "1957年起步的农业机械化制造，后发展为包装机械、印刷机械和智能装备；产品、设备与工艺谱系待厂志核验",
            "social_memory": "原机械厂职工、家属和京山市工业社区生活记忆；居民口述、老照片和公共服务设施待采集",
            "current_use_or_loss": "2019年启动原机械厂生活区老旧小区改造，企业现有轻机工业园继续运营；原老厂区产权、迁建和遗存边界待核",
        },
        "notes": "省住建厅案例确认原机械厂生活区更新，企业官网补足京山轻工机械厂1957年以来的技术与组织谱系；本条仍不推断原生产厂房完整保存或法定遗产级别。",
    },
    "HBI-JZ-018": {
        "source_keys": ["hubei_industry_export_1989", "shashi_first_machine_history_2022"],
        "cultural_evidence": {
            "material_carriers": "荆州/沙市机床厂厂房、老厂门、办公楼和机床设备待档案与现场核验；回忆资料提供第一机床厂老厂门和办公楼图像线索",
            "technical_memory": "摇臂钻床、磨床和机床加工技术；回忆资料记载1956年建厂、20世纪70年代生产和1980年金质奖，设备档案待补",
            "social_memory": "沙市机械工业、机床工人、技术培训和地方工业化记忆；职工社区与口述史待采集",
            "current_use_or_loss": "1989年省政府公报确认荆州机床厂名称，回忆资料涉及沙市第一/第二机床厂，现厂址、改制、搬迁和再利用状态待核",
        },
        "aliases": ["荆州机床厂", "沙市第一机床厂", "沙市第二机床厂", "沙市机床厂（待核）"],
        "notes": "省政府公报提供荆州机床厂历史名单线索，区域回忆资料补足沙市第一机床厂建厂、老厂门和摇臂钻床生产记忆；名称对应关系、厂址和实体边界待档案核对。",
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
    print(f"wave_an_sources={len(NEW_SOURCES)} added_records=0 updated_records={len(UPDATES)} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
