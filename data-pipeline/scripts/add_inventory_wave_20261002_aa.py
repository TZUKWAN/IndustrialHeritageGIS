from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "huanggang_urban_renewal_2026": {
        "source_type": "city_urban_renewal_interview_reprint",
        "title": "聚力城市更新 建设人民城市——黄冈市城市更新专班办公室负责人就城市更新工作答记者问",
        "org": "黄冈市城市更新专班办公室/黄冈市住房和城市更新局（搜狐转载）",
        "pub_date": "2026-07-26",
        "url": "https://www.sohu.com/a/1054991928_121106908",
        "authority": "C",
        "notes": "转载页面以黄冈市城市更新专班办公室负责人答记者问形式，明确原兴和铝业老旧厂房改造为兴和全明星体育公园、浠水西门山氮肥厂盘活闲置工业用地、罗田纤维板厂住宅更新等对象。因页面不是黄冈政府原站，保留为对象级线索/城市更新来源，法定遗产身份、边界和原始文件需回到市县部门核验。",
    },
    "huanggang_xinghe_reuse_2024": {
        "source_type": "provincial_media_urban_renewal_report",
        "title": "主城崛起势如虹 千年黄州焕新彩",
        "org": "湖北日报",
        "pub_date": "2024-09-29",
        "url": "https://epaper.hubeidaily.net/pad/content/202409/29/content_290112.html",
        "authority": "B",
        "notes": "湖北日报报道黄州兴和全明星体育公园前身为废弃老厂区，并明确其为黄冈兴和铝业厂区，说明通过政府支持转为体育消费和公共休闲空间；文章未给出厂区测绘、设备清单或遗产认定。",
    },
    "huanggang_xinghe_sports_2025": {
        "source_type": "national_sports_government_report",
        "title": "2025年湖北省‘百街千巷’全民健身系列赛事活动第4站走进黄冈市黄州区西湖街道",
        "org": "国家体育总局/湖北省体育局",
        "pub_date": "2025-06-12",
        "url": "https://www.sport.gov.cn/n14471/n14488/n14525/c28802560/content.html",
        "authority": "A",
        "notes": "国家体育总局转载湖北省体育局信息，确认兴和全明星体育公园作为黄州区社区体育活动场所持续运营；用于补充旧厂区再利用后的公共文化功能，不替代原厂区历史档案和建筑测绘。",
    },
    "xishui_nitrogen_factory_history_2023": {
        "source_type": "local_gazetteer_catalog",
        "title": "浠水文史资料、党史、县志、年鉴、地名志等地方资料目录",
        "org": "中国县志大全（目录线索）",
        "pub_date": "2023-10-01",
        "url": "https://xianzhi8.com/m/article.php?id=1130",
        "authority": "C",
        "notes": "目录页面列出《浠水氮肥厂志》这一地方企业志书，证明该企业有独立厂志线索；未提供志书全文、厂址坐标或建筑设备清单，需向浠水县档案馆/地方志办公室查核。",
    },
    "xishui_nitrogen_pollution_2016": {
        "source_type": "local_media_environmental_lead",
        "title": "浠水县氮肥厂污染严重",
        "org": "楚天都市网（报料页面）",
        "pub_date": "2016-01-01",
        "url": "https://www.ctdsb.net/html/baoliao/2016/0101/1750.html",
        "authority": "C",
        "notes": "地方媒体报料页标题指向浠水县氮肥厂环境问题，仅作为历史环境风险线索，不把报料内容当作污染结论；厂区土壤、地下水、修复和再开发限制必须以生态环境部门档案和环评/调查报告核验。",
    },
    "suizhou_plastic_local_2026": {
        "source_type": "municipal_official_media",
        "title": "串点成链打造‘一路繁花’一路景 以新业态新场景激活文旅新动能",
        "org": "随州日报",
        "pub_date": "2026-08-27",
        "url": "https://szrb.suiw.cn/szrb/20260827/html/content_20260827001002.htm",
        "authority": "B",
        "notes": "随州日报确认草甸子街汉东茶馆由原塑料三厂旧厂房改造而成，并将其作为随州首家工业遗存剧场式茶馆的城市更新节点；用于补充地方媒体与湖北日报来源的交叉印证。",
    },
}


SOURCE_REVISIONS: dict[str, dict[str, Any]] = {
    "shennongjia_forestry_history_2025": {
        "expected_url": "https://www.forestry.gov.cn/c/www/dfdt/638280.jhtml",
        "patch": {
            "org": "国家林业和草原局/新华每日电讯",
            "pub_date": "2025-08-15",
            "notes": "国家林草局政府网转载新华每日电讯报道，记载神农架20世纪60年代因木材建设需求形成大规模林业生产，十余年外运木材超过180万立方米；林业历史馆保存老麻绳、安全帽、刀斧锯凿等伐木时代实物，报道同时叙述停伐、保护区建立和林业转型。页面未给出单体建筑名录，故本条作为林业工业文化景观与馆藏线索记录。",
        },
    }
}


def ev(material: str, technical: str, social: str, current: str) -> dict[str, str]:
    return {
        "material_carriers": material,
        "technical_memory": technical,
        "social_memory": social,
        "current_use_or_loss": current,
    }


def rec(
    inventory_id: str,
    name: str,
    city: str,
    district: str | None,
    industry: str,
    level: str,
    status: str,
    source_keys: list[str],
    notes: str,
    cultural_evidence: dict[str, str],
    *,
    record_status: str = "source_confirmed",
    aliases: list[str] | None = None,
    asset_kind: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "inventory_id": inventory_id,
        "name": name,
        "city": city,
        "district_county": district,
        "industry_category_l1": industry,
        "recognition_level": level,
        "recognition_status": status,
        "record_status": record_status,
        "geocode_status": "pending",
        "source_keys": source_keys,
        "cultural_evidence": cultural_evidence,
        "notes": notes,
    }
    if aliases:
        row["aliases"] = aliases
    if asset_kind:
        row["asset_kind"] = asset_kind
    return row


NEW_RECORDS: list[dict[str, Any]] = [
    rec(
        "HBI-HG-009",
        "兴和铝业旧厂区—兴和全明星体育公园",
        "黄冈市",
        "黄州区",
        "有色冶金工业",
        "city_planning",
        "城市更新工业片区转型对象；未见法定工业遗产认定",
        ["huanggang_urban_renewal_2026", "huanggang_xinghe_reuse_2024", "huanggang_xinghe_sports_2025"],
        "黄冈市城市更新问答和湖北日报均确认兴和全明星体育公园前身为兴和铝业旧厂区/废弃老厂区，湖北日报称其由‘工业锈带’转为体育消费和公共休闲空间；国家体育总局来源确认其持续承载社区体育活动。与白莲铝业社区记录可能存在企业沿革或空间关联，但尚未取得厂志、地籍和厂区测绘，暂不合并。",
        ev(
            "原兴和铝业老厂区保留的建筑主体和更新后的体育公园空间；公开报道未列出车间编号、设备、烟囱或铁路等具体核心物项",
            "铝业生产、老厂区组织和由生产空间转为公共体育空间的技术与更新记忆；具体冶炼/加工工艺、设备谱系和厂志待核",
            "原厂职工、黄州居民和体育公园使用者共同形成的工业锈带转型记忆；工人社区、企业沿革和口述史待采集",
            "旧厂区已转为篮球、羽毛球、游泳、休闲游乐和社区活动空间，报道称原有建筑主体得到保留；产权、结构安全、污染风险和保护边界仍待现场与档案核验",
        ),
        aliases=["黄冈兴和铝业老厂区", "兴和全明星体育公园工业遗存"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-HG-010",
        "浠水西门山氮肥厂旧工业片区",
        "黄冈市",
        "浠水县清泉镇（西门山片区）",
        "化肥与化学工业",
        "city_planning",
        "黄冈市城市更新问答确认的低效工业片区；未见法定工业遗产认定",
        ["huanggang_urban_renewal_2026", "xishui_nitrogen_factory_history_2023", "xishui_nitrogen_pollution_2016"],
        "黄冈市城市更新专班答记者问明确浠水西门山氮肥厂通过盘活闲置工业用地导入居住、商业和科创功能；地方资料目录列出《浠水氮肥厂志》，另有地方报料页提出环境风险线索。本条只确认企业和旧工业片区的研究入口，不把再开发报道写成遗产认定或污染结论。",
        ev(
            "西门山氮肥厂旧工业用地及可能残留的厂房、生产设施和职工配套；公开来源未给出建筑、设备、铁路或储罐清单",
            "县域氮肥生产、合成氨/化肥供应和地方化学工业组织的技术记忆；《浠水氮肥厂志》全文、工艺路线和设备谱系待档案核验",
            "氮肥厂职工、浠水农业用肥供应和西门山工业片区形成的社会记忆；职工社区、人物和口述史待采集",
            "城市更新报道称闲置工业用地被导入居住、商业和科创功能；原厂边界、建筑保存、土壤地下水风险和再开发限制必须以自然资源、生态环境和档案资料核验",
        ),
        aliases=["浠水氮肥厂旧址", "西门山老旧工业片区"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-HG-011",
        "罗田纤维板厂职工住宅片区（城市更新对象）",
        "黄冈市",
        "罗田县",
        "人造板工业",
        "city_planning",
        "黄冈市城市更新问答确认的原纤维板厂住宅改造对象；未见厂址、遗产认定或完整厂区边界",
        ["huanggang_urban_renewal_2026"],
        "黄冈市城市更新专班答记者问将罗田纤维板厂列入八九十年代D级预制板危旧住房原拆原建项目。公开材料只证明企业名称与职工住宅更新关系，尚未证明厂房、设备或厂区仍存，故按工业社区文化载体和待核对象登记。",
        ev(
            "与原纤维板厂相关的八九十年代预制板职工住宅及其社区空间；公开来源未确认生产厂房、仓库、设备或具体坐标",
            "纤维板生产企业的工艺、原料、设备和质量管理记忆目前只有企业名称线索；厂志、地方志和档案目录待补",
            "原厂职工住宅、家庭生活和企业社区共同形成的工业社会记忆；居民口述、老照片和社区档案待采集",
            "城市更新问答称项目采用原拆原建路径，住宅和原厂区是否保留、拆除或异地迁建均需规划批复和现场调查核实",
        ),
        aliases=["罗田纤维板厂", "罗田纤维板厂职工社区"],
        asset_kind="industrial_residential_landscape",
    ),
]


RECORD_PATCHES: dict[str, dict[str, Any]] = {
    "HBI-SZ-001": {
        "source_keys": ["suizhou_plastic_local_2026"],
        "notes_append": "随州日报补充确认草甸子街汉东茶馆由原塑料三厂旧厂房改造，作为随州首家工业遗存剧场式茶馆持续运营；与湖北日报报道互相印证。",
        "cultural_evidence": ev(
            "原随州塑料三厂约1000平方米旧厂房、红砖墙和老梁架，现为草甸子街汉东茶馆；原厂区边界、设备清单和附属建筑待核",
            "塑料制品生产、厂房空间组织和老厂房修旧如旧更新形成的技术记忆；原工艺和设备谱系待补",
            "原厂长、老工友、草甸子街居民与非遗演艺观众共同形成的工业社区记忆；湖北日报和随州日报均记录其公共传播场景",
            "旧厂房已改造为剧场式茶馆，保留工业元素并融入工业展陈、非遗展演、本土美食和社区茶叙；产权、结构安全和保护边界待核",
        ),
    },
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    existing_by_id = {row["inventory_id"]: row for row in records}
    names = {row["name"] for row in records}
    for new_row in NEW_RECORDS:
        old = existing_by_id.get(new_row["inventory_id"])
        if old is None:
            if new_row["name"] in names:
                raise SystemExit(f"conflicting duplicate name: {new_row['name']}")
            records.append(new_row)
            existing_by_id[new_row["inventory_id"]] = new_row
            names.add(new_row["name"])
        elif old != new_row:
            raise SystemExit(f"conflicting duplicate record: {new_row['inventory_id']}")
    for key, value in NEW_SOURCES.items():
        if key in sources and sources[key] != value:
            raise SystemExit(f"conflicting source: {key}")
        sources[key] = value
    for key, revision in SOURCE_REVISIONS.items():
        if key not in sources:
            raise SystemExit(f"missing source to revise: {key}")
        if sources[key].get("url") != revision["expected_url"]:
            raise SystemExit(f"unexpected source URL for revision: {key}")
        sources[key].update(revision["patch"])
    for inventory_id, patch in RECORD_PATCHES.items():
        row = existing_by_id[inventory_id]
        old_sources = row.get("source_keys", [])
        row["source_keys"] = list(dict.fromkeys(old_sources + patch.get("source_keys", [])))
        note = patch.get("notes_append")
        if note and note not in row.get("notes", ""):
            row["notes"] = row.get("notes", "").rstrip() + " " + note
        evidence = patch.get("cultural_evidence")
        if evidence is not None:
            if "cultural_evidence" in row and row["cultural_evidence"] not in ({}, evidence):
                raise SystemExit(f"conflicting cultural evidence: {inventory_id}")
            row["cultural_evidence"] = evidence
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_aa_sources={len(NEW_SOURCES)} added_records={len(NEW_RECORDS)} "
        f"updated_records={len(RECORD_PATCHES)} revised_sources={len(SOURCE_REVISIONS)} "
        f"total_records={len(records)} total_sources={len(sources)}"
    )


if __name__ == "__main__":
    main()
