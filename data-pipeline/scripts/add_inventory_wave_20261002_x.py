from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "xiantao_low_efficiency_2026": {
        "source_type": "provincial_government_urban_renewal_report",
        "title": "向存量要空间 以盘活促发展——仙桃市攻坚低效用地激活土地发展新动能",
        "org": "湖北省自然资源厅",
        "pub_date": "2026-07-10",
        "url": "https://zrzyt.hubei.gov.cn/bmdt/sxdt/202607/t20260710_5974707.shtml",
        "authority": "A",
        "notes": "省自然资源厅报道仙桃低效工业载体再开发，明确杨林尾镇原第三服装厂、三伏潭镇废弃无纺布厂区，以及大垸子—沙湖泵站老旧水利设施的盘活、转型和产教融合用途；用于确认具体旧厂区/水利设施对象存在及现状，不替代工业遗产认定、原址边界和现场测绘。",
    },
    "pufang_archive_2019": {
        "source_type": "provincial_archive_industrial_memory",
        "title": "蒲纺：繁华落尽待重生",
        "org": "湖北档案信息网（咸宁市档案馆）",
        "pub_date": "2019-10-14",
        "url": "https://www.hbda.gov.cn/info/3234",
        "authority": "A",
        "notes": "咸宁市档案馆文章梳理二三四八—蒲纺三线建设、纺织联合企业、十里纺城、职工社区和工业园更新，记载原6500平方米老厂房改造、二三四八展览馆建成并接待参观者；用于补充工业文化载体和利用证据，不改变国家工业遗产组成项的法定边界。",
    },
    "xianning_pufang_school_2026": {
        "source_type": "official_media_industrial_memory",
        "title": "师泽如光，虽微致远——记赤壁市蒲纺一中英语教师杨欣",
        "org": "掌上咸宁",
        "pub_date": "2026-08-17",
        "url": "https://app.xnnews.com.cn/news/sh/202608/t20260817_5290775.shtml",
        "authority": "B",
        "notes": "地方官方媒体报道蒲纺一中由老厂房改建教学楼，保留老厂区空间记忆并与二三四八三线建设历史相连；用于确认教育再利用这一文化载体，不替代原厂房单体清单和保护边界。",
    },
    "xianning_baidun_bricktea_2025": {
        "source_type": "official_media_traditional_industry",
        "title": "湖北咸安：一块贡砖的百年荣光与新生",
        "org": "掌上咸宁",
        "pub_date": "2025-07-17",
        "url": "https://app.xnnews.com.cn/news/rt/202507/t20250717_4026553.shtml",
        "authority": "B",
        "notes": "地方官方媒体报道咸安区桂花镇柏墩街咸宁市柏墩生甡川砖茶厂，明确清代老厂房、省级非遗生甡川青砖茶制作技艺和当代研学利用；用于确认传统工业生产场所及文化传承关系，工业遗产认定层级和建筑年代档案仍待核。",
    },
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
    aliases: list[str] | None = None,
    asset_kind: str | None = None,
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
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": source_keys,
        "cultural_evidence": cultural_evidence,
        "notes": notes,
    }
    if aliases:
        row["aliases"] = aliases
    if asset_kind:
        row["asset_kind"] = asset_kind
    if related_inventory_ids:
        row["related_inventory_ids"] = related_inventory_ids
    return row


NEW_RECORDS: list[dict[str, Any]] = [
    rec(
        "HBI-XT-005",
        "杨林尾镇原第三服装厂旧厂房",
        "仙桃市",
        "杨林尾镇",
        "服装与纺织工业",
        "city_update",
        "官方低效用地再开发对象；非独立工业遗产认定，保护边界待核",
        ["xiantao_low_efficiency_2026"],
        "省自然资源厅报道杨林尾镇盘活原第三服装厂和广羽服饰共8600平方米闲置厂房，引入生物科技、服饰和机械加工企业；本条保留原第三服装厂的旧厂房谱系，暂按城市更新工业文化对象记录，不把再利用报道等同于法定工业遗产认定。",
        ev(
            "原第三服装厂闲置厂房及其生产、仓储和配套空间；公开报道未给出保留建筑清单、坐标和原厂边界",
            "乡镇服装生产、厂房租赁和产业转型形成的地方制造技术记忆；原设备、产品和厂志待补",
            "杨林尾镇工人、家庭和小城工业就业形成的社区记忆；老职工口述、照片和厂史待采集",
            "8600平方米闲置厂房进入租赁改造并导入新产业；原有工业构件和改造保留程度待现场核验",
        ),
        aliases=["原第三服装厂", "杨林尾镇第三服装厂旧址"],
        asset_kind="industrial_building",
    ),
    rec(
        "HBI-XT-006",
        "三伏潭镇废弃无纺布厂区",
        "仙桃市",
        "三伏潭镇",
        "无纺布与纺织工业",
        "city_update",
        "官方低效用地再开发对象；非独立工业遗产认定，原厂区边界待核",
        ["xiantao_low_efficiency_2026"],
        "省自然资源厅报道三伏潭镇废弃十余年的无纺布厂区引进纳米新材料企业，原低效地块变为现代化生产车间；本条记录其产业转型和工业文化记忆价值，厂名、建设年代、建筑设备清单及保护边界仍待补证。",
        ev(
            "废弃无纺布厂区、厂房和生产场地；报道未公开原企业名称、厂房编号和完整空间边界",
            "仙桃无纺布产业由传统厂区向纳米新材料转型的技术记忆；原生产线、工艺和人员谱系待厂志补证",
            "三伏潭镇纺织产业工人、周边社区和就业结构变化形成的工业社会记忆；口述与影像待采集",
            "厂区闲置十余年后导入纳米新材料企业并重新生产；原工业遗存保留和拆改情况待现场核验",
        ),
        aliases=["三伏潭无纺布厂区", "废弃无纺布厂旧址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-XT-007",
        "大垸子—沙湖泵站老旧水利设施群",
        "仙桃市",
        "大垸子、沙湖镇",
        "水利工程与泵站",
        "city_update",
        "官方低效用地再开发和产教融合对象；泵站单体名录、年代与保护边界待核",
        ["xiantao_low_efficiency_2026"],
        "省自然资源厅报道整合仙桃市大垸子、沙湖泵站闲置土地、老旧办公宿舍，改造老旧水利设施为水利产教融合实训课堂；本条将其作为水利工业文化景观群记录，不把项目规划直接等同于泵站文保或工业遗产认定。",
        ev(
            "大垸子、沙湖泵站的泵房、闸站、老旧办公宿舍及配套水利设施；公开报道未列单体清单和坐标",
            "泵站运行、灌排调度和水利工程维护形成的区域工程技术记忆；设备型号、建设年代和工程档案待补",
            "泵站职工、灌区村镇和水利建设者共同形成的生产生活记忆；口述史与老照片待采集",
            "老旧水利设施计划改造为水利产教融合实训课堂；具体保留、修缮和教学开放范围待核",
        ),
        aliases=["大垸子泵站", "沙湖泵站老旧设施"],
        asset_kind="industrial_utility_site",
    ),
    rec(
        "HBI-XN-014",
        "蒲纺一中旧厂房改建教学楼",
        "咸宁市",
        "赤壁市蒲纺片区",
        "纺织工业与工业社区",
        "city_update",
        "官方媒体确认的老厂房再利用文化载体；非独立工业遗产认定，原建筑单体待核",
        ["xianning_pufang_school_2026", "pufang_archive_2019"],
        "地方官方媒体报道蒲纺一中教学楼由旧厂房改建，保留老厂区空间记忆；咸宁市档案馆同时记载二三四八—蒲纺三线建设、职工社区和工业园更新。本条记录教育再利用载体，暂不把学校改建建筑直接等同于国家工业遗产组成项之外的法定认定。",
        ev(
            "蒲纺一中由旧厂房改建的教学楼、老厂区廊道和工业社区空间；原厂房编号、结构年代和边界待核",
            "二三四八—蒲纺纺织联合企业的生产、教育和职工服务体系形成的技术传播记忆；原教学和生产设备待补",
            "蒲纺职工子女教育、老厂区学校生活和三线建设社区共同记忆；师生与退休职工口述待采集",
            "旧厂房已改作学校教学楼并持续使用；改建保留程度、权属和开放展示方式待现场核验",
        ),
        aliases=["蒲纺一中旧厂房", "赤壁市蒲纺一中老厂房教学楼"],
        asset_kind="industrial_social_site",
        related_inventory_ids=["HBI-XN-005", "HBI-XN-006"],
    ),
    rec(
        "HBI-XN-015",
        "蒲纺二三四八工业文化展览馆",
        "咸宁市",
        "赤壁市蒲纺片区",
        "纺织工业与三线建设",
        "industrial_tourism_related",
        "咸宁市档案馆报道的工业文化展示设施；非独立工业遗产认定，馆舍来源和展陈档案待核",
        ["pufang_archive_2019"],
        "咸宁市档案馆文章记载蒲纺园区建成代表蒲纺军工文化的二三四八展览馆并接待参观者；本条作为工业文化展示和公众记忆载体单列，展馆所在建筑、展陈目录和开放状态仍需现场或档案资料核验。",
        ev(
            "二三四八展览馆及其展陈空间、老厂房环境和蒲纺工业园公共设施；馆舍原建筑信息待核",
            "展览内容承载二三四八三线建设、纺织联合生产、军工服装和十里纺城的技术史；展陈目录待取得",
            "蒲纺职工、家属、建设者和参观者通过展馆延续工业社区记忆；讲解词、口述史和参观记录待补",
            "展览馆已建成并接待参观者；当前开放时间、运营主体和展陈更新状态待现场核验",
        ),
        aliases=["二三四八展览馆", "蒲纺军工文化展览馆"],
        asset_kind="industrial_culture_site",
        related_inventory_ids=["HBI-XN-005", "HBI-XN-006", "HBI-XN-007", "HBI-XN-008", "HBI-XN-009", "HBI-XN-010", "HBI-XN-011"],
    ),
    rec(
        "HBI-XN-016",
        "柏墩生甡川砖茶厂清代老厂房",
        "咸宁市",
        "咸安区桂花镇柏墩街",
        "茶叶加工与传统食品工业",
        "research_candidate",
        "地方官方媒体确认的传统生产场所和清代老厂房；工业遗产认定层级待核",
        ["xianning_baidun_bricktea_2025"],
        "地方官方媒体报道咸宁市柏墩生甡川砖茶厂保有清代老厂房，并以省级非遗生甡川青砖茶制作技艺开展生产、研学和传承；本条按传统工业文化遗产候选记录，建筑本体、产权、年代档案和保护边界待文物/普查资料核验。",
        ev(
            "柏墩街清代砖茶厂老厂房、制茶场地和传统生产空间；建筑测绘、构件清单和确切年代待核",
            "生甡川青砖茶压制、加工和质量控制技艺，以及万里茶道相关茶业生产组织记忆；工艺谱系待系统整理",
            "柏墩茶工、传承人、茶商和地方社区共同形成的贡砖生产与茶乡生活记忆；传承人口述和老照片待补",
            "老厂房与现代生产线并存，已开展非遗课堂和研学活动；开放管理、设备原真性和保护制度待核",
        ),
        aliases=["生甡川砖茶厂", "柏墩砖茶厂老厂房", "长裕川砖茶厂旧址"],
        asset_kind="industrial_building",
    ),
]


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
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_x_sources={len(NEW_SOURCES)} added_records={len(NEW_RECORDS)} "
        f"total_records={len(records)} total_sources={len(sources)}"
    )


if __name__ == "__main__":
    main()
