from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "qiaokou_industry_history_2018": {
        "source_type": "district_government_industry_history",
        "title": "硚口区工业略谈",
        "org": "武汉市硚口区人民政府",
        "pub_date": "2018-02-05",
        "url": "https://www.qiaokou.gov.cn/qkgk/hghh/201802/t20180205_117765.shtml",
        "authority": "A",
        "notes": "硚口区政府工业史页面明确古田地区武汉柴油机厂的历史沿革、生产设备和产品，并记载1957年成功试制中国第一台小型拖拉机、1963年更名武汉柴油机厂；用于补强武汉柴油机厂旧址工业文化证据，不替代现存建筑清单和保护边界。",
    },
    "wuhan_history_hubei_diesel_2021": {
        "source_type": "municipal_history_pdf",
        "title": "武汉文史资料2021年第5/6期：构建以国营企业为主导的社会主义工业体系",
        "org": "武汉市地方志/武汉市政协文史资料",
        "pub_date": None,
        "url": "https://www.dxh.gov.cn/YXLKG_16692/wszl/202108/P020250516589252373546.pdf",
        "authority": "A",
        "notes": "官方文史资料PDF记载1949年接管湖北省机械厂和机械农垦处后成立湖北农具制造厂（现湖北省柴油机厂），置于武汉工业体系沿革中；发布日期未在页面明确，pub_date留空。用于补强湖北省柴油机厂名称与组织谱系，不替代厂址测绘。",
    },
    "shiyan_third_front_2026": {
        "source_type": "academic_secondary_with_local_chronicles",
        "title": "三线建设与湖北十堰城市的形成",
        "org": "环球社科评论",
        "pub_date": "2026-04-01",
        "url": "https://cn.sgsci.org/ssr/article/download/1104/958/6285",
        "authority": "C",
        "notes": "2026年第3卷第2期学术论文表格引用《十堰市志（1866—2008）》《丹江口市志》等地方志，明确郧县柳陂风动工具厂1967年由国家一机部投资兴建，后改为郧阳地区汽车拨叉厂，并给出职工与固定资产统计；作为二手学术交叉来源，不替代地方档案、厂志和现场核验。",
    },
}


def ev(material: str, technical: str, social: str, current: str) -> dict[str, str]:
    return {
        "material_carriers": material,
        "technical_memory": technical,
        "social_memory": social,
        "current_use_or_loss": current,
    }


UPDATES: dict[str, dict[str, Any]] = {
    "HBI-WUHAN-034": {
        "source_keys": ["wuhan_old_sites_2026", "wuhan_qiaokou_industrial_2026", "qiaokou_industry_history_2018"],
        "cultural_evidence": ev(
            "硚口古田地区原柴油机厂、床单厂厂区建筑和生产空间；区政府工业史补充柴油机设备与厂区历史，具体单体和遗存比例待普查",
            "柴油机制造、195型柴油机、手扶拖拉机和老城区工业生产组织技术记忆；设备型号与生产线档案待补",
            "硚口工人、古田工业基地、企业社区和武汉农业机械化记忆；职工口述、老照片和生活设施待采集",
            "已更新为汉江湾人工智能产业园，报道确认产业导入；原柴油机厂和床单厂遗存保留比例、产权与可展示对象待现场核验",
        ),
        "notes": "武汉市政府和硚口区政府来源共同确认汉江湾项目由原柴油机厂、床单厂旧址更新而来；硚口区工业史进一步补足武汉柴油机厂沿革、古田位置和产品技术，但厂区边界与保留单体仍待专项普查。",
    },
    "HBI-PROV-010": {
        "city": "武汉市",
        "district_county": "硚口区古田地区（具体厂界待核）",
        "recognition_level": "research_candidate",
        "recognition_status": "武汉官方文史资料确认湖北农具制造厂沿革为湖北省柴油机厂；未见法定工业遗产认定",
        "record_status": "source_confirmed",
        "source_keys": ["hubei_archive_machinery_1966", "wuhan_history_hubei_diesel_2021"],
        "cultural_evidence": ev(
            "湖北农具制造厂—湖北省柴油机厂在武汉工业体系中的厂房、设备和生产空间；具体建筑与厂界待档案及测绘核验",
            "农具制造、柴油机和农业机械动力技术记忆；官方文史资料确认企业名称沿革，产品谱系和设备清单待厂志核实",
            "湖北省柴油机厂与武汉农业机械化、技术工人和工业组织记忆相连；职工社区、口述史和老照片待采集",
            "档案和官方文史资料确认历史企业与组织沿革，现存厂区、改制、停产、更新和环境风险待核",
        ),
        "aliases": ["湖北柴油机厂", "湖北农具制造厂", "湖北省柴油机厂"],
        "asset_kind": "industrial_site",
        "notes": "湖北省档案馆设计任务书与武汉官方文史资料共同确认企业谱系；本条与‘武汉柴油机厂’记录分开保存，避免把湖北农具制造厂/湖北省柴油机厂和武汉柴油机厂名称沿革直接合并。",
    },
    "HBI-SY-029": {
        "recognition_level": "research_candidate",
        "recognition_status": "省档案馆设计任务书与学术论文引用地方志共同确认郧县柳陂风动工具厂历史实体；未见法定工业遗产认定",
        "record_status": "source_confirmed",
        "source_keys": ["hubei_archive_machinery_1966", "shiyan_third_front_2026"],
        "cultural_evidence": ev(
            "郧县柳陂风动工具厂厂房、机械设备和职工生活设施；学术论文给出柳陂地点，具体建筑、厂界和现状待测绘",
            "1967年国家一机部投资建设的风动工具及汽车零部件生产技术，后转为郧阳地区汽车拨叉生产；工艺和设备清单待厂志核验",
            "风动工具厂与十堰三线建设、汽车配套产业和郧县工人群体相连；职工社区、口述史和地方照片待采集",
            "学术论文记载后续改为郧阳地区汽车拨叉厂，现企业名称、厂区保存、搬迁和再利用状态待地方档案与现场核验",
        ),
        "aliases": ["郧县风动工具厂", "郧阳风动工具厂", "郧县柳陂风动工具厂", "郧阳地区汽车拨叉厂"],
        "notes": "省档案馆目录提供设计任务书题名，2026年学术论文引用《十堰市志》《丹江口市志》补足柳陂位置、1967年建设和后续汽车拨叉厂沿革；保留研究候选层级。",
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
    updated = 0
    for inventory_id, patch in UPDATES.items():
        if inventory_id not in by_id:
            raise SystemExit(f"missing update target: {inventory_id}")
        for key, value in patch.items():
            by_id[inventory_id][key] = value
        updated += 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_af_sources={len(NEW_SOURCES)} added_records=0 updated_records={updated} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
