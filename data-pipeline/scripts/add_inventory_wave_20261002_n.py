from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "wuhan_zanyu_history_2012": {
        "source_type": "official_media",
        "title": "老汉口最大制冰厂风光不再 曾是本地冷饮市场龙头",
        "org": "长江商报/长江网",
        "pub_date": "2012-11-27",
        "url": "https://news.cjn.cn/sywh/201211/t2159383.htm",
        "authority": "B",
        "notes": "地方官方媒体报道赞育药房在1918年收购小型汽水车间、投资扩建并添置机器，形成汉口赞育汽水厂和机制汽水生产；报道还记载其与和利等企业共同参与武汉冷饮市场。生产规模、设备清单和厂区范围仍需档案核验。",
    },
    "whcbs_zanyu_economic_history_2020": {
        "source_type": "local_cultural_publishing",
        "title": "汉口赞育药房有限公司备忘录与章程（《武汉民国初期史料》）",
        "org": "武汉出版社/武汉文化出版网站",
        "pub_date": None,
        "url": "https://www.whcbs.com/Upload/BookReadFile/202002/3342c36349d14537a274a048f0fe2a8b/ops/chapter007.html",
        "authority": "B",
        "notes": "武汉地方文化出版资料摘录1920年公司备忘录和章程，明确赞育药房经营药品、化工制剂、医疗器械、矿泉汽水、液体充气/矿化/罐装、制冰及相关设备，并注明材料摘自档案原件；本来源用于支撑企业技术范围和组织谱系，原件馆藏目录与完整档案仍待核验。",
    },
    "wuhan_zanyu_boundary_2017_mirror": {
        "source_type": "government_protection_notice_mirror",
        "title": "省人民政府办公厅关于公布湖北省文物保护单位保护范围和建设控制地带的通知（鄂政办发〔2017〕68号）",
        "org": "湖北省人民政府办公厅（公开文件镜像）",
        "pub_date": "2017-12-04",
        "url": "https://upload.wikimedia.org/wikipedia/commons/e/e6/%E7%9C%81%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%8E%85%E5%85%B3%E4%BA%8E%E5%85%AC%E5%B8%83%E6%B9%96%E5%8C%97%E7%9C%81%E6%96%87%E7%89%A9%E4%BF%9D%E6%8A%A4%E8%8C%83%E5%9B%B4%E5%92%8C%E5%BB%BA%E8%AE%BE%E6%8E%A7%E5%88%B6%E5%9C%B0%E5%B8%A6%E7%9A%84%E9%80%9A%E7%9F%A5%EF%BC%88%E9%84%82%E6%94%BF%E5%8A%9E%E5%8F%91%E3%80%942017%E3%80%9568%E5%8F%B7%EF%BC%89.pdf",
        "authority": "B",
        "notes": "公开电子镜像中的省政府原文列出汉口赞育药房（江岸区洞庭街103—105号）的保护范围和建设控制地带，具体方向与距离已转写到档案备注；因当前链接为公开镜像，发布前应再从湖北省政府原始附件复核文件版本。",
    },
    "chinanews_zanyu_fire_2012": {
        "source_type": "national_media",
        "title": "建筑凌晨失火 三年轻人挨家敲门救出16户居民",
        "org": "中国新闻网",
        "pub_date": "2012-02-13",
        "url": "https://www.chinanews.com/sh/2012/02-13/3664385.shtml",
        "authority": "B",
        "notes": "报道洞庭街103号建筑火灾、居民疏散和屋顶受损，并将其描述为1918年英商赞育药房附属工厂、后改为汉口机制汽水厂；用于记录建筑风险与社会记忆，不替代现状测绘和修缮评估。",
    },
    "wuhan_historical_buildings_2023": {
        "source_type": "municipal_government_register",
        "title": "武汉市第四批优秀历史建筑名录（公布文件）",
        "org": "武汉市人民政府",
        "pub_date": "2023-06-26",
        "url": "https://www.wuhan.gov.cn/zwgk/xxgk/zfgb/202306/P020230626396464516850.pdf",
        "authority": "A",
        "notes": "武汉市政府公布文件列出原名赞育汽水厂、现地址江岸区洞庭街103—105号、建造年代1937年前及‘近代工业建筑遗址’保留理由，补足市级历史建筑名录与地址核对。",
    },
}


def ev(material: str, technical: str, social: str, current: str) -> dict[str, str]:
    return {
        "material_carriers": material,
        "technical_memory": technical,
        "social_memory": social,
        "current_use_or_loss": current,
    }


PATCHES: dict[str, dict[str, Any]] = {
    "HBI-WUHAN-015": {
        "source_keys_add": [
            "hubei_provincial_relics_1098",
            "hubei_boundary_2017_wlt",
            "wuhan_zanyu_history_2012",
            "whcbs_zanyu_economic_history_2020",
            "wuhan_zanyu_boundary_2017_mirror",
            "chinanews_zanyu_fire_2012",
            "wuhan_historical_buildings_2023",
        ],
        "aliases": ["汉口赞育药房", "汉口赞育药房旧址", "汉口赞育汽水公司", "赞育汽水厂旧址"],
        "district_county": "江岸区",
        "recognition_level": "provincial",
        "recognition_status": "第五批湖北省文物保护单位（公布名：汉口赞育药房）；武汉市首批工业遗产一级（保护名：赞育汽水厂）",
        "asset_kind": "industrial_cultural_landscape",
        "notes": "同一处江岸区洞庭街103—105号建筑与企业谱系在不同名录中分别以‘汉口赞育药房’和‘赞育汽水厂’出现，合并为一条主档案避免重复计数。湖北省1098处名录确认1913年汉口赞育药房，武汉市工业遗产名录和优秀历史建筑文件确认赞育汽水厂；地方媒体与武汉地方文化出版资料进一步记录1918年收购汽水车间、机械化生产，以及药品、化工、汽水、制冰和相关设备经营范围。2012年火灾报道提示本体保存风险，建筑保护范围与控制地带以鄂政办发〔2017〕68号为准；镜像文件中的具体方向距离发布前仍需从省政府原始附件复核。",
        "cultural_evidence_updates": {
            "material_carriers": "1913年汉口赞育药房营业部/现存历史建筑，以及1918年并入企业谱系的汽水生产空间；洞庭街103—105号地址、近代工业建筑遗址身份和省级文保保护边界已有名录或公报证据，现存设备、楼内分区、厂房是否完整需测绘",
            "technical_memory": "药品与化工制剂、医疗器械、矿泉汽水的充气/矿化/罐装、制冰及相关机器设备构成企业技术谱系；1918年添置机器后形成汉口机制汽水生产的报道可核，设备型号、工艺参数和产品档案待补",
            "social_memory": "药房提供药品与医疗用品、汽水和冰块进入汉口城市消费，药房职员、制冰/汽水工人、商贸网络和居民共同形成公共生活记忆；2012年火灾中居民互救事件已见媒体记录，企业职工与社区口述史待规范采集",
            "current_use_or_loss": "第五批省级文保名录、武汉市工业遗产与优秀历史建筑名录均已确认；2012年火灾造成屋顶和部分住户受损，当前产权、修缮、开放、设备留存和是否仍有生产展示功能需以最新现场资料复核",
        },
    },
}


def merge_unique(row: dict[str, Any], key: str, values: list[str]) -> None:
    existing = row.setdefault(key, [])
    for value in values:
        if value not in existing:
            existing.append(value)


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    existing_by_id = {row["inventory_id"]: row for row in records}
    for inventory_id, patch in PATCHES.items():
        row = existing_by_id.get(inventory_id)
        if row is None:
            raise SystemExit(f"patch target missing: {inventory_id}")
        merge_unique(row, "source_keys", patch.get("source_keys_add") or [])
        merge_unique(row, "aliases", patch.get("aliases") or [])
        updates = patch.get("cultural_evidence_updates") or {}
        if updates:
            row.setdefault("cultural_evidence", {}).update(updates)
        for key, value in patch.items():
            if key not in {"source_keys_add", "aliases", "cultural_evidence_updates"}:
                row[key] = value
        row["source_keys"] = sorted(set(row.get("source_keys") or []))
    sources.update({key: value for key, value in NEW_SOURCES.items() if key not in sources})
    data["research_targets"]["coverage_rule"] = (
        "每条对象至少绑定名录/普查/规划/企业史/档案遗产或来源确认资料；"
        "工业遗产实体、工业文化景观、工业金融与贸易节点、工业旅游相关场景、档案文献和待核验线索分层记录。"
        "文化证据字段只记录来源中明确出现的载体、技术、社会记忆和利用状态，未核实内容保持待核。"
    )
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_n_sources={len(NEW_SOURCES)} patched_records={len(PATCHES)} "
        f"total_records={len(records)} total_sources={len(sources)}"
    )


if __name__ == "__main__":
    main()
