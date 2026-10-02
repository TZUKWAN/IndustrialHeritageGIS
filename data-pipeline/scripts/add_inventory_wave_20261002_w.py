from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "shiyan_dongfeng_origin_2026": {
        "source_type": "official_media_industrial_memory",
        "title": "传承弘扬‘马灯精神’ 树立和践行正确政绩观丨从工业‘锈带’到文旅‘秀带’ 东风故里华丽蝶变",
        "org": "十堰广电网",
        "pub_date": "2026-07-01",
        "url": "https://www.syiptv.com/article/show/331299",
        "authority": "B",
        "notes": "十堰本地官方媒体报道明确花果街道原东风48厂、49厂、59厂、62厂、64厂五大原厂旧址及其东风故里城市更新关系；用于确认59厂和62厂的对象线索、三线工业社区记忆和片区利用方向，不替代单体名录或测绘档案。",
    },
    "shiyan_6264_2026": {
        "source_type": "official_media_industrial_memory",
        "title": "芦席棚里走出来的世界车都——十堰茅箭区784家东风系汽配工厂的五十六年",
        "org": "十堰日报数字报",
        "pub_date": "2026-05-07",
        "url": "https://syrb.10yan.com/html/20260507/215293.html",
        "authority": "B",
        "notes": "十堰日报报道将张湾区花果街道东风故里工业遗址小镇定位为原6264厂旧址，并说明红砖厂房、三线建设和东风城市记忆的活化语境；原厂边界、建筑清单和保护层级仍需普查档案核验。",
    },
    "shiyan_housing_dongfeng_2023": {
        "source_type": "provincial_government_urban_renewal_report",
        "title": "十堰：四措并举推进东风公司老旧小区蝶变",
        "org": "湖北省住房和城乡建设厅",
        "pub_date": "2023-09-28",
        "url": "https://zjt.hubei.gov.cn/bmdt/dtyw/szsm/202309/t20230928_4872492.shtml",
        "authority": "A",
        "notes": "省住建厅报道东风公司老旧小区改造和东风故里历史文化街区，明确修缮旧厂房、嵌入三线建设精神和东风工业文化；用于补充片区更新与工业文化利用证据，不替代具体厂号的文保认定。",
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
        "HBI-SY-018",
        "原东风公司59厂旧址",
        "十堰市",
        "张湾区花果街道",
        "汽车制造与专业零部件",
        "city_planning",
        "东风故里片区官方工业遗址对象；独立厂区边界和认定级别待核",
        ["shiyan_dongfeng_origin_2026", "shiyan_housing_dongfeng_2023", "shiyan_car_survey_2018"],
        "十堰官方媒体明确花果街道原东风48、49、59、62、64厂为东风专业厂核心发源地，并纳入东风故里工业文化更新语境；本条单列59厂以保留厂号和工业社区记忆，暂不把片区更新等同于59厂独立名录认定，厂房、设备、建成年代和权属待普查档案核验。",
        ev(
            "原东风公司59厂厂区、专业生产车间和职工社区空间；公开报道未给出59厂独立建筑清单与完整边界",
            "三线建设时期汽车专业化分工、零部件生产和整车协作形成的制造技术记忆；具体产品和设备谱系待厂志补证",
            "花果街道东风职工、家属和建设者共同形成的马灯精神、三线建设与汽车城记忆；厂号对应的口述史待采集",
            "纳入东风故里片区城市更新和工业文化展示语境；59厂现存厂房、拆改范围和开放利用状态待现场核验",
        ),
        aliases=["东风59厂旧址", "原二汽59厂"],
        asset_kind="industrial_social_site",
    ),
    rec(
        "HBI-SY-019",
        "原东风公司62厂旧址",
        "十堰市",
        "张湾区花果街道",
        "汽车制造与专业零部件",
        "city_planning",
        "东风故里片区官方工业遗址对象；独立厂区边界和认定级别待核",
        ["shiyan_dongfeng_origin_2026", "shiyan_housing_dongfeng_2023", "shiyan_car_survey_2018"],
        "十堰官方媒体明确花果街道原东风48、49、59、62、64厂为东风专业厂核心发源地，并纳入东风故里工业文化更新语境；本条单列62厂以保留厂号和工业社区记忆，暂不把片区更新等同于62厂独立名录认定，厂房、设备、建成年代和权属待普查档案核验。",
        ev(
            "原东风公司62厂厂区、专业生产车间和职工社区空间；公开报道未给出62厂独立建筑清单与完整边界",
            "三线建设时期汽车专业化分工、零部件生产和整车协作形成的制造技术记忆；具体产品和设备谱系待厂志补证",
            "花果街道东风职工、家属和建设者共同形成的马灯精神、三线建设与汽车城记忆；厂号对应的口述史待采集",
            "纳入东风故里片区城市更新和工业文化展示语境；62厂现存厂房、拆改范围和开放利用状态待现场核验",
        ),
        aliases=["东风62厂旧址", "原二汽62厂"],
        asset_kind="industrial_social_site",
    ),
    rec(
        "HBI-SY-020",
        "原东风公司6264厂旧址（东风故里工业遗址小镇）",
        "十堰市",
        "张湾区花果街道",
        "汽车制造与三线建设",
        "city_planning",
        "官方媒体确认的旧厂址活化对象；工业遗址小镇保护边界和原厂物项待核",
        ["shiyan_6264_2026", "shiyan_dongfeng_origin_2026", "shiyan_car_survey_2018"],
        "十堰日报将东风故里工业遗址小镇定位于原6264厂旧址，并记录红砖厂房、三线建设和东风城市记忆；本条与东风故里放马坪文化古巷保持片区关系，但单独保留厂址谱系，避免将街区名称代替厂区实体认定。",
        ev(
            "原6264厂红砖厂房、厂区道路和东风故里工业遗址小镇公共空间；建筑编号、设备与完整边界待测绘",
            "三线建设时期汽车工厂选址、厂房建设和专业化生产组织形成的工程与制造技术记忆；具体产品谱系待档案补证",
            "放马坪职工社区、建设者和东风后代共同形成的马灯精神、芦席棚创业和汽车城记忆；厂史口述材料待采集",
            "旧厂区已进入东风故里工业遗址小镇和文化街区活化利用；原真性、权属和保护制度待核",
        ),
        aliases=["6264厂旧址", "六二六四厂旧址", "东风故里工业遗址小镇"],
        asset_kind="industrial_cultural_landscape",
        related_inventory_ids=["HBI-SY-013"],
    ),
    rec(
        "HBI-SY-021",
        "房县恒达纺织厂旧址",
        "十堰市",
        "房县县城",
        "纺织工业",
        "city_update",
        "省级官方城市更新报道确认的原纺织厂；原址边界和保护价值待专项普查",
        ["shiyan_natural_resources_2026"],
        "湖北省自然资源厅转载十堰日报报道，明确房县县城恒达、华球两个纺织厂因工艺落后和经营困难迁入纺织产业园，原址约11.35万平方米并转为综合性商业体；报道确认企业原址与转型关系，但未给恒达厂单体建筑、设备和年代清单，暂按城市更新工业文化对象记录。",
        ev(
            "房县恒达纺织厂原厂区及其生产、仓储和职工服务空间；原址拆改范围、厂房保留情况和坐标待核",
            "县域纺织产业迁建、工艺升级和产业园转移形成的地方工业技术记忆；纺织设备、产品和厂志待补",
            "房县纺织工人、家庭和县城工业化形成的就业与社区记忆；老职工口述史和照片待采集",
            "原厂区已纳入退二进三和综合商业体开发；现存工业构件、旧厂门和档案保存状态未知",
        ),
        aliases=["房县恒达纺织厂原址", "恒达纺织厂旧厂区"],
        asset_kind="industrial_social_site",
    ),
    rec(
        "HBI-SY-022",
        "房县华球纺织厂旧址",
        "十堰市",
        "房县县城",
        "纺织工业",
        "city_update",
        "省级官方城市更新报道确认的原纺织厂；原址边界和保护价值待专项普查",
        ["shiyan_natural_resources_2026"],
        "湖北省自然资源厅转载十堰日报报道，明确房县县城恒达、华球两个纺织厂因工艺落后和经营困难迁入纺织产业园，原址约11.35万平方米并转为综合性商业体；报道确认企业原址与转型关系，但未给华球厂单体建筑、设备和年代清单，暂按城市更新工业文化对象记录。",
        ev(
            "房县华球纺织厂原厂区及其生产、仓储和职工服务空间；原址拆改范围、厂房保留情况和坐标待核",
            "县域纺织产业迁建、工艺升级和产业园转移形成的地方工业技术记忆；纺织设备、产品和厂志待补",
            "房县纺织工人、家庭和县城工业化形成的就业与社区记忆；老职工口述史和照片待采集",
            "原厂区已纳入退二进三和综合商业体开发；现存工业构件、旧厂门和档案保存状态未知",
        ),
        aliases=["房县华球纺织厂原址", "华球纺织厂旧厂区"],
        asset_kind="industrial_social_site",
    ),
    rec(
        "HBI-SY-023",
        "原东风公司54厂片区",
        "十堰市",
        None,
        "汽车制造与专业零部件",
        "city_planning",
        "官方城市更新报道确认的东风老厂片区；具体厂区和遗存边界待核",
        ["shiyan_natural_resources_2026", "shiyan_car_survey_2018"],
        "湖北省自然资源厅报道十堰规划开发原东风公司54厂片区约68.8万平方米用地，明确其属于东风老工业基地腾退和城市更新范围；公开资料暂未给出54厂核心物项清单，故按片区工业文化线索记录，不升格为独立工业遗产认定。",
        ev(
            "原东风公司54厂片区及可能保留的厂房、道路、配套设施和职工生活空间；公开资料未给出具体建筑清单",
            "二汽专业化分工、汽车零部件生产和厂区组织形成的技术记忆；厂号沿革、产品和设备档案待补",
            "东风职工和家属在54厂片区形成的三线建设、就业和社区记忆；口述史和老照片待采集",
            "片区约68.8万平方米用地进入商住开发规划；拆改进度、工业遗存保留情况和保护要求待核",
        ),
        aliases=["东风54厂片区", "原二汽54厂"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-SY-024",
        "原东风小康一工厂旧厂房",
        "十堰市",
        None,
        "汽车制造",
        "city_update",
        "省级官方城市更新报道确认的旧厂房活化对象；原厂址边界和保留构件待核",
        ["shiyan_natural_resources_2026"],
        "湖北省自然资源厅转载十堰日报报道，明确原东风小康一工厂2.6万平方米旧厂房改造为‘农耕二张烙馍村’，并以微改造盘活工业存量；报道未给出工厂建成年代、原生产线和完整坐标，暂按城市更新工业文化对象记录。",
        ev(
            "原东风小康一工厂约2.6万平方米旧厂房及生产空间；具体车间、设备和厂区边界待现场核验",
            "汽车整车及零部件生产、工厂搬迁和旧厂房再利用形成的技术与城市转型记忆；产品和设备谱系待补",
            "东风小康职工、周边居民和十堰老工业基地转型形成的就业与社区记忆；口述史和影像待采集",
            "旧厂房已改造为餐饮和体验空间，报道强调保留工业骨架；原真性、产权和开放管理待核",
        ),
        aliases=["东风小康一工厂旧址", "原东风小康一厂"],
        asset_kind="industrial_cultural_landscape",
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
        f"wave_w_sources={len(NEW_SOURCES)} added_records={len(NEW_RECORDS)} "
        f"total_records={len(records)} total_sources={len(sources)}"
    )


if __name__ == "__main__":
    main()
