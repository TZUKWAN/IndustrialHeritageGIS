from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "suizhou_30_draft_2025": {
        "source_type": "municipal_government_public_notice",
        "title": "关于公开征求《随州市新增历史建筑名录（征求意见稿）》意见的通知（曾都区30处，附名录docx）",
        "org": "随州市自然资源和城乡建设局",
        "pub_date": "2025-08-05",
        "url": "http://zrzyhghj.suizhou.gov.cn/fbjd_18/zwgk/zc/qtzdgkwj/gsgg/202508/t20250805_1353835.shtml",
        "authority": "A",
        "notes": "市自然资源和城乡建设局筛选曾都区辖区内30处历史建筑拟列入随州市历史建筑名录，2025年8月5日公开征求意见（公示5个工作日）；附件docx含逐栋档案表（建筑编号、保护分类、结构、年代、产权、概况、照片），已下载解析（本地存档 raw/suizhou_30/）：编号1/2/3/4/7为齐星公司打磨车间、模具车间、仓库、职工仓库、冲压车间（草甸子街东面，始建于上世纪80年代、修缮于2024年，现作非遗产品展示使用，产权齐星公司）；其余为随南县抗日民主政府旧址、淅河镇石码头街与万店镇传统民居等。",
    },
}


RECORD = {
    "inventory_id": "HBI-SZ-013",
    "name": "齐星公司草甸子街车间仓库建筑群（打磨、模具、冲压车间及仓库）",
    "city": "随州市",
    "district_county": "曾都区西城街道草甸子街",
    "industry_category_l1": "机械制造与汽车零部件工业",
    "recognition_level": "municipal_historical_building",
    "recognition_status": "拟列入随州市历史建筑名录（2025年8月5日市自然资源和城乡建设局征求意见公示，曾都区30处之编号1、2、3、4、7；公示层级，正式公布待跟踪）",
    "record_status": "source_confirmed",
    "geocode_status": "pending",
    "source_keys": ["suizhou_30_draft_2025"],
    "cultural_evidence": {
        "material_carriers": "名录档案表载明5栋砖混建筑：1号打磨车间（273平方米）、2号模具车间、3号仓库、4号职工仓库、7号冲压车间（草甸子街东面，产权齐星公司）；各栋建筑面积与设备留存待现场测绘",
        "technical_memory": "齐星集团（随州汽车车身与专用车制造企业）钣金冲压、打磨、模具加工车间组群，反映汽车零部件配套生产的工艺布局；80年代建、2024年修缮",
        "social_memory": "齐星公司职工生产记忆与草甸子街老城工业街区记忆；车间现作为非遗产品展示空间，工业遗存与非遗活化叠加",
        "current_use_or_loss": "修缮后作为非遗产品展示使用，工业骨架保存于展示空间内；拟列入名录公示后正式认定、保护范围与活化边界待跟踪核验",
    },
    "notes": "直接取自市自然资源和城乡建设局征求意见公示附件docx逐栋档案表（A级，已下载解析）；公示层级不等于正式公布，record_status 的 source_confirmed 指档案表来源确凿；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
    "aliases": ["齐星公司打磨车间", "齐星公司模具车间", "齐星公司冲压车间"],
    "asset_kind": "industrial_building",
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    existing = next((row for row in records if row["inventory_id"] == RECORD["inventory_id"]), None)
    if existing is not None:
        if existing != RECORD:
            raise SystemExit("conflicting duplicate record")
        added = 0
    else:
        if any(row["name"] == RECORD["name"] for row in records):
            raise SystemExit("conflicting duplicate name")
        records.append(RECORD)
        added = 1
    for key, source in SOURCES.items():
        if key in sources and sources[key] != source:
            raise SystemExit(f"conflicting source: {key}")
    sources.update(SOURCES)
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_bm_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
