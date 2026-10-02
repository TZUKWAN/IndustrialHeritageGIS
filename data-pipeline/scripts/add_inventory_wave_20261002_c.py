from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "hubei_industrial_tourism_2026": {
        "source_type": "government_media",
        "title": "从青铜炉到智能臂——湖北工业的5万亿“进化论”",
        "org": "湖北省文化和旅游厅",
        "pub_date": "2026-09-07",
        "url": "https://wlt.hubei.gov.cn/bmdt/ztzl/wltztwhlvj/wltztwhlvjtp/202609/t20260907_6008532.shtml",
        "authority": "A",
        "notes": "省文旅厅工业指南列出大冶铁矿矿区机车存放区、鄂钢工业旅游景区、羊楼洞茶文化生态产业园、汉阳造文化创意园、青山红坊等工业旅游或工业文化场景；记录为来源确认对象，正式遗产层级按各自名录/规划另行核验。",
    },
    "wuhan_dazhi_2026": {
        "source_type": "government_media",
        "title": "大智无界·空中小镇文创产业园",
        "org": "湖北省文化和旅游厅",
        "pub_date": "2026-07-16",
        "url": "https://wlt.hubei.gov.cn/bmdt/ztzl/wltztwhlvj/wltztalzs/wltztwljcz/202607/t20260716_5978742.shtml",
        "authority": "A",
        "notes": "官方页面确认大智无界前身为武汉无线电厂，位于江岸区大智路50号，由7栋老厂房组成，约5万平方米，已进行文商旅体融合活化利用。",
    },
    "hubei_definition_2024": {
        "source_type": "government_policy_draft",
        "title": "湖北省工业遗产管理办法（征求意见稿）",
        "org": "湖北省经济和信息化厅",
        "pub_date": "2024-12-13",
        "url": "https://jxt.hubei.gov.cn/fbjd/zc/qtzdgkwj/gsgg/202412/t20241213_5461585.shtml",
        "authority": "A",
        "notes": "省经信厅公开征求意见稿把工业遗产核心物项明确为物质遗存与非物质遗存，包含厂房/矿区、生活服务设施、机器设备、产品、档案，以及生产工艺、规章制度、企业文化和工业精神；本项目用作概念和字段边界依据，文件本身不是对象认定。",
    },
    "wuhan_qiaokou_yuedong_2026": {
        "source_type": "government_news",
        "title": "老厂区建起运动场和景观绿地，硚口悦动公园本月底开放",
        "org": "武汉市人民政府/长江日报",
        "pub_date": "2026-08-08",
        "url": "https://www.wuhan.gov.cn/whyw/gqdt/202608/t20260808_2831394.shtml",
        "authority": "A",
        "notes": "武汉市政府报道确认悦动公园保留原武汉轻工业机械厂3栋主体老厂房，并将其纳入古田片城市更新公共空间；旧厂区精确边界和建筑清单待普查。",
    },
    "wuhan_nanyang1916_2026": {
        "source_type": "government_news",
        "title": "央视网：武汉城市更新进行时——硚口区从“工业锈带”到“发展秀带”",
        "org": "武汉市人民政府/央视网",
        "pub_date": "2026-04-15",
        "url": "https://www.wuhan.gov.cn/sy/kwh/202604/t20260415_2753343.shtml",
        "authority": "A",
        "notes": "官方报道确认南洋1916园区前身为武汉床单总厂区域，保留部分老厂房并开展保护性修缮、文商旅活化；与汉江湾床单厂片区保持组成关系待核。",
    },
    "wuhan_nantaizihu_2026": {
        "source_type": "government_media",
        "title": "城市更新进行时：“工业锈带”变身“科创谷”",
        "org": "武汉市住房和城市更新局/中华建设网",
        "pub_date": "2026-07-13",
        "url": "https://zgj.wuhan.gov.cn/zwdt/jdxw/202607/t20260713_2819986.shtml",
        "authority": "A",
        "notes": "官方城市更新报道确认武汉经开区南太子湖创新谷由连片老工业区更新而来，保留机械制造、汽车零部件和电子电器制造厂房主体并导入文创、档案馆、音乐厅等功能。",
    },
    "wuhan_binhushuanghe_2026": {
        "source_type": "government_news",
        "title": "光谷黄龙山城市更新项目启动，老厂房将变超级全感剧场",
        "org": "武汉市人民政府/长江日报",
        "pub_date": "2026-08-29",
        "url": "https://3g.wuhan.gov.cn/sy/whyw/202608/t20260829_2840571.shtml",
        "authority": "A",
        "notes": "武汉市政府报道确认黄龙山南侧12栋老厂房为原滨湖双鹤药业遗存，列出约6.2万平方米用地和更新为剧场、文创工坊等功能；原企业厂区边界待专项测绘。",
    },
}


def rec(
    inventory_id: str,
    name: str,
    city: str,
    industry: str,
    level: str,
    status: str,
    source_keys: list[str],
    notes: str,
    cultural_evidence: dict[str, str],
    *,
    district: str | None = None,
    aliases: list[str] | None = None,
    asset_kind: str | None = None,
    record_status: str = "source_confirmed",
    related_heritage_ids: list[str] | None = None,
    related_inventory_ids: list[str] | None = None,
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
    if related_heritage_ids:
        row["related_heritage_ids"] = related_heritage_ids
    if related_inventory_ids:
        row["related_inventory_ids"] = related_inventory_ids
    return row


def ev(material: str, technical: str, social: str, current: str) -> dict[str, str]:
    return {
        "material_carriers": material,
        "technical_memory": technical,
        "social_memory": social,
        "current_use_or_loss": current,
    }


NEW_RECORDS: list[dict[str, Any]] = [
    rec(
        "HBI-HS-033",
        "大冶铁矿矿区机车存放区",
        "黄石市",
        "采掘冶金与铁路运输工业",
        "industrial_tourism_related",
        "省文旅厅工业指南图注确认的工业文化场景（正式层级待核）",
        ["hubei_industrial_tourism_2026"],
        "省文旅厅工业指南图注明确标出大冶铁矿矿区机车存放区，并以CKD6E型内燃机车说明矿业运输记忆；本条不把图注直接升格为独立名录认定。",
        ev(
            "矿区机车存放区、CKD6E型内燃机车、矿山铁路/机车设施（数量和位置待测绘）",
            "露天矿山矿石运输、机车调度和矿区物流技术",
            "矿山运输工人、铁山矿区和黄石采掘工业记忆",
            "作为大冶铁矿工业旅游场景出现，具体保存状态、开放线路和管理主体待核",
        ),
        district="铁山区",
        asset_kind="heritage_component",
        related_inventory_ids=["HBI-HS-005"],
    ),
    rec(
        "HBI-XN-012",
        "咸宁羊楼洞茶文化生态产业园",
        "咸宁市",
        "茶叶加工与茶文化产业",
        "industrial_tourism_related",
        "省文旅厅工业指南列举的国家级工业旅游场景（不等同工业遗产认定）",
        ["hubei_industrial_tourism_2026"],
        "省文旅厅工业指南把羊楼洞茶文化生态产业园列为工业旅游样本，说明其覆盖茶叶种植、研发加工、品牌营销、文化传播和生态旅游；本条记录工业文化场景，不替代工业遗产名录。",
        ev(
            "茶园、茶叶研发加工设施、中国青砖茶未来实践展示馆和“天下第一砖”等产品展示",
            "青砖茶种植、加工、产品开发和茶文化传播链条",
            "羊楼洞茶区、茶工、青砖茶贸易和地方茶产业记忆",
            "官方指南称其兼具生产、展示和旅游功能；园区边界、具体企业和遗产分级待核",
        ),
        district="赤壁市",
        aliases=["羊楼洞茶文化生态产业园（青砖茶）"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-EZ-011",
        "鄂钢工业旅游景区（复兴广场—花溪湿地公园）",
        "鄂州市",
        "钢铁工业文化景观",
        "industrial_tourism_related",
        "来源确认的钢铁工业旅游景区（不等同独立工业遗产认定）",
        ["ezhou_steel", "hubei_industrial_tourism_2026"],
        "鄂城区文旅局官方简介确认鄂城钢铁厂形成工业旅游景区，省文旅厅工业指南进一步列出复兴广场、花溪湿地公园和钢厂变公园的利用场景；作为景区尺度对象入库。",
        ev(
            "复兴广场、花溪湿地公园、钢厂厂区和可展示工业设施（具体清单待核）",
            "钢铁生产、厂区能源物流和工业景观组织",
            "鄂钢工人、鄂州钢城和钢铁城市记忆",
            "官方资料确认已建成工业旅游景区；现役生产区、开放边界和保护单元待核",
        ),
        district="鄂城区",
        aliases=["鄂城钢铁工业旅游景区", "鄂钢工业旅游"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-WUHAN-035",
        "大智无界·空中小镇（武汉无线电厂旧址活化）",
        "武汉市",
        "电子工业与工业文创",
        "provincial_heritage_related",
        "武汉市无线电厂省级工业遗产活化利用对象",
        ["wuhan_dazhi_2026", "hubei_definition_2024"],
        "省文旅厅确认大智无界前身为武汉无线电厂，江岸区大智路50号，保留7栋老厂房并改造为文商旅体融合园区；与省级工业遗产HBI-PROV-003建立组成/利用关系。",
        ev(
            "7栋包豪斯风格老厂房、原厂区空间格局和约5万平方米建筑",
            "收录机等无线电产品制造、电子工业厂区组织和老厂房改造技术",
            "“长江”牌音响、无线电厂职工和江岸工业社区记忆",
            "已改造为文创办公、艺术展览、演艺娱乐和体育休闲园区；具体原厂房编号待核",
        ),
        district="江岸区",
        aliases=["武汉市无线电厂旧址活化", "大智路50号老厂房"],
        asset_kind="industrial_cultural_landscape",
        related_inventory_ids=["HBI-PROV-003"],
    ),
    rec(
        "HBI-WUHAN-036",
        "汉阳造文化创意园",
        "武汉市",
        "近代工业建筑与文创产业",
        "industrial_tourism_related",
        "省文旅厅工业指南列举的工业遗产文创园（具体名录层级待核）",
        ["hubei_industrial_tourism_2026", "hubei_definition_2024"],
        "省文旅厅工业指南将汉阳造文化创意园列为工业遗产与文创园，提到百年工业厂房、老机床和艺术空间；具体产权、原企业谱系和保护名录需进一步核验。",
        ev(
            "百年工业厂房、老机床、红砖建筑和文创空间（具体单体待测绘）",
            "近代机械/冶金生产空间和工业建筑再利用",
            "汉阳工业区、工人和“汉阳造”城市品牌记忆",
            "官方指南确认已转为艺术/文创空间；遗存边界和开放管理主体待核",
        ),
        district="汉阳区",
        aliases=["汉阳造文创园"],
        asset_kind="industrial_cultural_landscape",
        record_status="source_confirmed",
    ),
    rec(
        "HBI-WUHAN-037",
        "青山红坊工业文创集群",
        "武汉市",
        "钢铁工业文化景观",
        "industrial_tourism_related",
        "省文旅厅工业指南列举的工业文创集群（具体名录层级待核）",
        ["hubei_industrial_tourism_2026", "hubei_definition_2024"],
        "省文旅厅工业指南把青山红坊列为工业遗产与文创园，说明其依托老工业区形成文创集群；具体旧厂名、建筑清单和保护层级待武汉市更新/文保资料核验。",
        ev(
            "老工业区厂房、工业构筑物和文创公共空间（具体单体待核）",
            "钢铁工业社区空间和老厂房适应性再利用",
            "武钢职工、青山社区和钢铁城市生活记忆",
            "官方指南确认形成工业文创集群；运营范围、产权和保护责任待核",
        ),
        district="青山区",
        aliases=["青山红坊"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-WUHAN-038",
        "硚口悦动公园（原武汉轻工业机械厂旧址）",
        "武汉市",
        "轻工业机械制造",
        "city_planning",
        "武汉市政府报道确认的老厂房更新对象",
        ["wuhan_qiaokou_yuedong_2026", "hubei_definition_2024"],
        "武汉市政府报道确认悦动公园保留原武汉轻工业机械厂3栋主体老厂房，并将其纳入古田片城市更新；正式工业遗产层级和完整厂区边界待专项普查。",
        ev(
            "原武汉轻工业机械厂3栋主体老厂房及其厂区空间",
            "轻工业机械制造、厂房结构和城市更新中的工业建筑再利用",
            "古田片区工人、居民和轻工业机械厂记忆",
            "按官方报道将开放为运动、亲子、休闲公园；保留建筑清单和产权管理待核",
        ),
        district="硚口区",
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-WUHAN-039",
        "南洋1916园区（原武汉床单总厂老厂房）",
        "武汉市",
        "纺织工业与城市更新",
        "city_planning",
        "武汉市政府报道确认的老厂房活化对象",
        ["wuhan_nanyang1916_2026", "hubei_definition_2024"],
        "武汉市政府报道确认南洋1916园区前身为武汉床单总厂区域，保留部分老厂房并实施保护性修缮；与汉江湾床单厂片区可能存在组成关系，待专项普查确认。",
        ev(
            "武汉床单总厂区域残存老厂房、红砖墙面和拱券顶等工业肌理",
            "纺织生产、工厂社区和老厂房保护性修缮",
            "硚口纺织职工、床单产品和老工业城区记忆",
            "官方报道确认导入文创、商业和公共服务业态；完整边界和保留比例待核",
        ),
        district="硚口区",
        aliases=["南洋1916工业园", "武汉床单总厂旧址"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-WUHAN-040",
        "南太子湖创新谷（连片老工业区更新）",
        "武汉市",
        "机械制造与汽车零部件工业文化景观",
        "city_planning",
        "武汉经开区城市更新报道确认的工业遗存片区",
        ["wuhan_nantaizihu_2026", "hubei_definition_2024"],
        "武汉市住房和城市更新局报道确认南太子湖创新谷由20世纪90年代连片老工业区更新而来，涉及机械制造、汽车零部件、电子电器制造厂房，保留主体并导入文创、档案馆和音乐厅。",
        ev(
            "连片老厂房主体、工业区道路绿化和公共文化空间（原企业单体待核）",
            "机械制造、汽车零部件和电子电器生产空间及适应性再利用",
            "经开区产业工人、老工业区居民和城市转型记忆",
            "已更新为生产—生活—生态融合的科创园区；原企业名单和保护单元待核",
        ),
        district="武汉经济技术开发区",
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-WUHAN-041",
        "滨湖双鹤药业老厂房区（黄龙山更新项目）",
        "武汉市",
        "医药工业",
        "city_planning",
        "武汉市政府报道确认的工业遗存更新对象",
        ["wuhan_binhushuanghe_2026", "hubei_definition_2024"],
        "武汉市政府报道确认黄龙山南侧12栋老厂房为原滨湖双鹤药业遗存，约6.2万平方米用地、约3600平方米建筑，并启动剧场、文创工坊等更新；原企业厂区边界待核。",
        ev(
            "原滨湖双鹤药业12栋老厂房及约3600平方米建筑（具体编号待核）",
            "医药生产厂房、企业技术空间和旧厂房结构加固再利用",
            "双鹤药业职工、东湖高新区企业社区和医药工业记忆",
            "官方报道显示正在更新为剧场、文创工坊、餐饮和零售等文化业态；施工完成度和开放时间待核",
        ),
        district="东湖高新区",
        asset_kind="industrial_cultural_landscape",
    ),
]


UPDATES: dict[str, dict[str, Any]] = {
    "HBI-PROV-003": {
        "source_keys_add": ["wuhan_dazhi_2026", "hubei_definition_2024"],
        "cultural_evidence": ev(
            "武汉无线电厂7栋包豪斯风格老厂房、原厂区空间格局和“长江”牌音响产品档案/实物线索",
            "收录机、音响等无线电产品制造和电子工业生产组织",
            "无线电厂职工、长江牌音响和江岸工业社区记忆",
            "已活化为大智无界·空中小镇；产权、开放和7栋厂房逐栋清单待核",
        ),
    },
    "HBI-YC-004": {
        "source_keys_add": ["hubei_industrial_tourism_2026"],
        "cultural_evidence": ev(
            "809厂老厂房、三线标语、艺术空间和度假小镇公共设施",
            "三线军工生产、转产和旧厂房文旅再利用",
            "809厂职工、三线建设者和宜昌山区工业记忆",
            "省文旅厅工业指南称809文化小镇已整体转产并运营；原厂区边界与开放状况待管理方核验",
        ),
    },
    "HBI-SY-001": {
        "source_keys_add": ["hubei_industrial_tourism_2026"],
        "cultural_evidence": ev(
            "东风汽车老厂房、车辆工厂、品牌体验中心和车城公园",
            "整车制造、汽车生产线和工业旅游展示组织",
            "东风职工、十堰车城和汽车工业城市记忆",
            "省文旅厅工业指南确认东风汽车工业旅游区包含车辆工厂、品牌体验中心和车城公园；具体开放线路待核",
        ),
    },
}


def merge_update(row: dict[str, Any], patch: dict[str, Any]) -> None:
    for key in patch.get("source_keys_add", []):
        if key not in row.setdefault("source_keys", []):
            row["source_keys"].append(key)
    if "cultural_evidence" in patch:
        existing = row.get("cultural_evidence")
        if existing is None:
            row["cultural_evidence"] = patch["cultural_evidence"]
        elif existing != patch["cultural_evidence"]:
            raise SystemExit(f"conflicting cultural_evidence for {row['inventory_id']}")
    row["source_keys"] = sorted(set(row.get("source_keys") or []))


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    existing_by_id = {row["inventory_id"]: row for row in records}
    existing_names = {row["name"] for row in records}
    duplicate_sources = set(NEW_SOURCES) & set(sources)
    duplicate_ids = {row["inventory_id"] for row in NEW_RECORDS} & set(existing_by_id)
    duplicate_names = {row["name"] for row in NEW_RECORDS} & existing_names
    if duplicate_sources or duplicate_ids or duplicate_names:
        all_new_present = (
            set(NEW_SOURCES) <= set(sources)
            and all(sources[key] == value for key, value in NEW_SOURCES.items())
            and all(row["inventory_id"] in existing_by_id and existing_by_id[row["inventory_id"]] == row for row in NEW_RECORDS)
        )
        if not all_new_present:
            raise SystemExit(
                "partial or conflicting prior application: "
                f"sources={sorted(duplicate_sources)} ids={sorted(duplicate_ids)} names={sorted(duplicate_names)}"
            )
    else:
        missing = sorted({key for row in NEW_RECORDS for key in row["source_keys"] if key not in sources and key not in NEW_SOURCES})
        if missing:
            raise SystemExit(f"missing source keys: {missing}")
        sources.update(NEW_SOURCES)
        records.extend(NEW_RECORDS)
        existing_by_id = {row["inventory_id"]: row for row in records}

    for inventory_id, patch in UPDATES.items():
        row = existing_by_id.get(inventory_id)
        if row is None:
            raise SystemExit(f"update target missing: {inventory_id}")
        merge_update(row, patch)

    data["research_targets"]["coverage_rule"] = (
        "每条对象至少绑定名录/普查/规划/企业史/档案遗产或来源确认资料；"
        "工业遗产实体、工业文化景观、工业旅游相关场景、档案文献和待核验线索分层记录。"
        "文化证据字段只记录来源中明确出现的载体、技术、社会记忆和利用状态，未核实内容保持待核。"
    )
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_c_records={len(NEW_RECORDS)} wave_c_sources={len(NEW_SOURCES)} "
        f"total_records={len(records)} total_sources={len(sources)} updates={len(UPDATES)}"
    )


if __name__ == "__main__":
    main()

