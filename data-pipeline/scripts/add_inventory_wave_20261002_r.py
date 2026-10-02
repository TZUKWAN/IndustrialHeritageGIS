from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "shiyan_second_auto_final_2025": {
        "source_type": "provincial_science_association_official",
        "title": "十堰市科协联合申报项目“第二汽车制造厂”成功入选省级工业遗产名录",
        "org": "湖北省科学技术协会（十堰市科协）",
        "pub_date": "2025-12-22",
        "url": "https://www.hbkx.org.cn/news/info?newsid=cc29bbbc1e99469a8a2ee9fe45c2aa82",
        "authority": "A",
        "notes": "省科协公开信息确认第二汽车制造厂项目成功入选湖北省第二批省级工业遗产名录，明确原43厂总装线为核心物项、产权归十堰市科协，并说明申报材料梳理了三线建设工业布局、生产工艺、技术创新和保护现状。",
    },
    "dfmc_museum_2025": {
        "source_type": "enterprise_official_industrial_museum",
        "title": "东风汽车博物馆在十堰盛大开馆",
        "org": "东风汽车集团有限公司",
        "pub_date": "2025-03-27",
        "url": "https://www.dfmc.com.cn/news/company/news_20250327_1025.html",
        "authority": "A",
        "notes": "东风汽车官网记录东风汽车博物馆依托第二汽车制造厂历史厂区改造，总面积2.1万余平方米、展出2000余件展品并设置三线岁月等专题展区；用于补充二汽遗产的现状展示和社会记忆，不等同于全部厂区核心物项。",
    },
    "shiyan_text605_culture_park": {
        "source_type": "central_enterprise_official_cultural_park",
        "title": "六零五文化创意产业园",
        "org": "中国文化产业发展集团有限公司/文字六零五（湖北）有限公司",
        "pub_date": "2026-06-26",
        "url": "https://www.chinawenfa.cn/zwf/ywly/whyq/605/A007003002006index_1.htm",
        "authority": "A",
        "notes": "中文发集团官网介绍文字六零五厂由上海字模二厂于1968年支援三线建设迁至湖北均县（今丹江口），主要生产字模、铅字、PS版等，现为六零五文创园；记录园区地址、面积、华文印迹三线建设展厅及500余件照片实物档案。",
    },
    "shiyan_second_archive_2026": {
        "source_type": "municipal_media_fourth_cultural_relic_survey",
        "title": "十堰“四普”新发现文物第14期｜国家第二书库：三线建设中的文化堡垒",
        "org": "十堰广电网（十堰市融媒体中心）",
        "pub_date": "2026-02-19",
        "url": "https://www.syiptv.com/article/show/319541",
        "authority": "B",
        "notes": "十堰融媒报道确认国家第二书库位于丹江口市丹赵路街道三里桥村原文字605厂内，占地641.36平方米，建筑保存较完整，1975年由兰州迁入、1984年搬离，2015年公布为丹江口市第三批市级文物保护单位，并在第四次全国文物普查中登记为新发现文物。",
    },
    "xiangyang_2025_final_industrial_heritage": {
        "source_type": "municipal_media_final_list_report",
        "title": "我市2家企业入选2025年度湖北省工业遗产名单",
        "org": "襄阳日报（长江网转载）",
        "pub_date": "2026-01-28",
        "url": "https://news.cjn.cn/hbpd_19912/yw_19915/202601/t5259070.htm",
        "authority": "B",
        "notes": "襄阳日报报道从市经信局获悉，省经信厅已发布2025年度湖北省工业遗产名单，国营石花酒厂和文字六〇三厂成功入选；报道同时补充石花155年酿造技艺、厂房遗址和文化博物馆，以及603厂房、车间、仓库和附属生活设施保护利用。",
    },
    "xiangyang_603_current_use_2025": {
        "source_type": "provincial_media_city_update",
        "title": "襄阳：工业遗存“活”起来 城市消费“潮”起来！",
        "org": "湖北日报新闻客户端",
        "pub_date": "2025-12-01",
        "url": "https://news.hubeidaily.net/pc/c_5356927.html",
        "authority": "B",
        "notes": "湖北日报报道六〇三文创园保留机修车间等工业痕迹，设三线记忆展厅，建设603印·刻非遗传承中心和603印刷博物馆，并记录园区企业、就业和运营情况。",
    },
    "yunyang_yun_gaisi_2025": {
        "source_type": "county_media_industrial_heritage_report",
        "title": "郧阳区云盖寺绿松石矿成功认定2025年度湖北省工业遗产",
        "org": "郧阳网（郧阳区融媒体中心）",
        "pub_date": "2025-12-17",
        "url": "https://www.syyunyang.cn/bumen/wenlvju/102270.html",
        "authority": "B",
        "notes": "郧阳网报道湖北省经信厅正式公示2025年度省级工业遗产名单，云盖寺绿松石矿入选；记录明代以来采掘历史、绿松石文化和矿山公园的博物馆、文创中心、游客服务及体验利用。",
    },
    "huanggang_guanyao_details_2025": {
        "source_type": "municipal_media_industrial_heritage_report",
        "title": "蕲春县管窑镇岚头矶工艺陶器厂入选省级工业遗产名单，千年陶脉再添荣光！",
        "org": "云上黄冈（黄冈日报）",
        "pub_date": "2025-12-19",
        "url": "https://pc.hgdaily.com.cn/p/481903.html",
        "authority": "B",
        "notes": "黄冈日报明确将“岚头矶工艺陶器厂（湖北管窑传统陶器生产制造基地）”作为同一入选项目，记录1958年建厂、红砖车间、推板窑、旧礼堂、老车间、产品外销和活化利用，为两种名录名称之间的组成关系提供直接证据。",
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
        "HBI-SY-017",
        "国家第二书库旧址（原文字605厂内）",
        "十堰市",
        "丹江口市",
        "出版印刷与文化备战",
        "municipal_heritage_related",
        "丹江口市第三批市级文物保护单位；第四次全国文物普查新发现文物；文字605厂工业文化组成项",
        ["shiyan_second_archive_2026", "shiyan_text605_culture_park"],
        "十堰融媒确认国家第二书库位于丹江口市丹赵路街道三里桥村原文字605厂内，占地641.36平方米，建筑保存较完整，1975年由兰州迁入、1984年搬离，2015年由丹江口市公布为第三批市级文物保护单位，并在第四次全国文物普查中登记为新发现文物。本条作为文字605厂内可独立识别的文化备战遗存组成项，不新增省级工业遗产认定。",
        ev(
            "红机瓦屋面平房、国家第二书库建筑本体、保护标志牌及原文字605厂内选址空间，占地641.36平方米；具体构件和保护范围待测绘",
            "1975年三线文化备战、图书迁移、文献保管与分散隐蔽布局；正式运行时13名工作人员、藏书33万册，体现出版物安全保存工程",
            "兰州—丹江口文化资源战略迁移、书库工作人员、文字605厂职工和三线建设文化安全记忆；与国家版本图书馆第二备战书库历史相连",
            "1984年书库搬离后改为职工活动室，2015年公布为市级文保单位，2026年报道确认第四次普查新发现文物；公开参观和修缮利用状态待核",
        ),
        aliases=["国家第二备战书库旧址", "丹江口文字605厂国家第二书库", "文字605厂书库旧址"],
        asset_kind="heritage_component",
        related_inventory_ids=["HBI-PROV-006"],
    ),
]


def merge_unique(row: dict[str, Any], key: str, values: list[str]) -> None:
    existing = row.setdefault(key, [])
    for value in values:
        if value not in existing:
            existing.append(value)


def patch_record(row: dict[str, Any], *, source_keys: list[str], aliases: list[str], evidence: dict[str, str], notes: str, level: str | None = None, status: str | None = None, district: str | None = None, related_inventory_ids: list[str] | None = None) -> None:
    merge_unique(row, "source_keys", source_keys)
    merge_unique(row, "aliases", aliases)
    row["cultural_evidence"] = evidence
    row["notes"] = notes
    if level is not None:
        row["recognition_level"] = level
    if status is not None:
        row["recognition_status"] = status
    if district is not None:
        row["district_county"] = district
    if related_inventory_ids:
        merge_unique(row, "related_inventory_ids", related_inventory_ids)
    row["record_status"] = "source_confirmed"


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    existing_by_id = {row["inventory_id"]: row for row in records}
    for new_row in NEW_RECORDS:
        old = existing_by_id.get(new_row["inventory_id"])
        if old is None:
            records.append(new_row)
            existing_by_id[new_row["inventory_id"]] = new_row
        elif old != new_row:
            raise SystemExit(f"conflicting duplicate record: {new_row['inventory_id']}")
    for key, value in NEW_SOURCES.items():
        if key in sources and sources[key] != value:
            raise SystemExit(f"conflicting source: {key}")
        sources[key] = value

    patch_record(
        existing_by_id["HBI-PROV-001"],
        source_keys=["shiyan_second_auto_final_2025", "dfmc_museum_2025"],
        aliases=["第二汽车制造厂工业遗存", "二汽", "东风汽车历史厂区"],
        level="provincial",
        status="湖北省第二批省级工业遗产（2025年度）",
        notes="湖北省科协公开信息确认第二汽车制造厂项目成功入选湖北省第二批省级工业遗产名录，原43厂总装线为核心物项且产权归十堰市科协。东风汽车官网记录原二汽历史厂区已改造为2.1万余平方米东风汽车博物馆，展出2000余件展品并设置三线岁月等专题展区；全厂区边界、其他核心物项和涉密开放范围待核。",
        evidence=ev(
            "原43厂总装一车间总装线、52厂原前梁车间、二汽总厂办公楼、工艺研究所大楼、商用车技术中心和科技图书馆等核心物项；东风汽车博物馆位于原二汽历史厂区",
            "1969年三线建设汽车基地、原43厂总装工艺、国内自主汽车制造、万吨锻压和EQ240/EQ2102/EQ140-1/EQ153车型技术记忆；官方申报重点整理生产工艺与技术创新",
            "举国支援二汽、十堰山沟建厂、东风人和三线建设者形成的汽车工业记忆；东风汽车博物馆以‘打汽车工业翻身仗’和三线岁月展区进行公共叙事",
            "2025年东风汽车博物馆依托历史厂区开馆，总面积2.1万余平方米、展出2000余件展品；省科协提出以原43厂总装线为核心系统性保护和活化，完整厂区开放边界待核",
        ),
    )
    patch_record(
        existing_by_id["HBI-PROV-004"],
        source_keys=["xiangyang_first_provincial_heritage_2024", "xiangyang_2025_final_industrial_heritage"],
        aliases=["石花酒厂", "石花酿酒股份有限公司原国营厂区", "石花街黄公顺酒馆"],
        level="provincial",
        status="湖北省第二批省级工业遗产（2025年度）",
        notes="襄阳日报报道确认国营石花酒厂入选2025年度湖北省工业遗产名单；湖北日报专题记录其由1870年石花街黄公顺酒馆发展而来、1950年代地方国营酒厂沿革、古窖池和酒精精馏塔，襄阳日报补充155年酿造技艺、厂房遗址和文化博物馆活化。具体老窖池、建筑编号和档案全宗待核。",
        evidence=ev(
            "石花镇原国营酒厂厂房、古窖池、酒精精馏塔、老厂门和现有酒文化博物馆/非遗体验中心；核心建筑与设备清单待测绘",
            "1870年石花街黄公顺酒馆延续的清香型白酒酿造、固态发酵和155年技艺传承；起窖拌料、蒸馏、摘酒、入窖发酵、勾兑储存等工序与老窖池共同构成技术链",
            "谷城石花镇酒业、酿酒工人、品牌消费和地方白酒产区身份记忆；石花酒文化博物馆和游客体验提供现行解释入口",
            "厂房遗址已改造为霸王醉古法酿造非遗体验中心、酒体设计中心、石花酒文化博物馆和酒旅综合体验馆；厂区产权、开放制度和原真性边界待核",
        ),
    )
    patch_record(
        existing_by_id["HBI-PROV-005"],
        source_keys=["yunyang_yun_gaisi_2025"],
        aliases=["云盖寺绿松石矿", "郧阳云盖寺矿山公园"],
        level="provincial",
        status="湖北省第二批省级工业遗产（2025年度）",
        notes="郧阳网报道确认云盖寺绿松石矿入选2025年度湖北省工业遗产名单，并记录明代以来开采史、绿松石文化和矿山公园的博物馆、文创中心、游客服务中心与民宿体验。工业遗产核心矿坑、巷道、选矿设施和矿权边界仍需专业测绘与安全核验。",
        evidence=ev(
            "云盖寺矿山矿脉、采掘地貌、矿坑/巷道及矿山公园博物馆、文创中心和游客服务设施；报道未给出完整核心物项清单，保留待核标记",
            "明代以来绿松石开采、矿脉识别、采掘和宝石加工技术传统；现代工业化开采设备与工艺谱系待补档案",
            "郧阳绿松石产地身份、矿工与工匠、宝石贸易和‘东方绿宝石’地方文化记忆；矿山公园以展示和体验方式对外解释",
            "矿山已转型为集工业遗产展示、生态旅游和文化体验于一体的矿山公园；开放线路、矿坑安全边界和持续保护主体待核",
        ),
    )
    patch_record(
        existing_by_id["HBI-PROV-006"],
        source_keys=["shiyan_text605_culture_park", "shiyan_second_archive_2026"],
        aliases=["文字六零五厂", "六零五厂", "丹江口文字605厂"],
        level="provincial",
        status="湖北省第二批省级工业遗产（2025年度）",
        notes="中文发集团官网介绍文字六零五厂1968年由上海字模二厂支援三线建设迁至湖北均县（今丹江口），主要生产字模、铅字和PS版，现为六零五文创园；园区约120亩、建筑4万余平方米，设华文印迹三线建设展厅，展出照片、实物和档案500余件。十堰融媒另确认原厂内国家第二书库为独立市级文保/四普新发现组成项。",
        evidence=ev(
            "六零五厂原厂区、厂房和生活设施、约120亩园区及4万余平方米建筑，华文印迹三线建设展厅和500余件照片实物档案；国家第二书库另列组成项",
            "1968年上海字模二厂支援三线迁建，字模、铅字、PS版等出版印刷材料生产，异地搬迁、荒山建厂和文字印刷技术组织",
            "六零五建设者从上海迁往丹江口、三线精神、出版文化备战和职工社区形成的社会记忆；园区展厅作为爱国主义教育基地持续传播",
            "现为六零五文创园，2017年企业变更、2018年与603园区组建文化创意园；产权、原生产设备完整性和公众开放边界待核",
        ),
        related_inventory_ids=["HBI-SY-017"],
    )
    patch_record(
        existing_by_id["HBI-PROV-007"],
        source_keys=["xiangyang_2025_final_industrial_heritage", "xiangyang_603_current_use_2025"],
        aliases=["文字六〇三厂", "603厂", "六〇三文创园"],
        level="provincial",
        status="湖北省第二批省级工业遗产（2025年度）",
        notes="襄阳日报报道确认文字六〇三厂入选2025年度湖北省工业遗产名单，湖北日报补充其为三线建设时期大型印刷企业，原厂房、车间、仓库和生活设施大部分保存；现六〇三文创园保留机修车间、三线记忆展厅，建设603印·刻非遗传承中心和603印刷博物馆。厂区逐栋清单、档案开放及涉军信息边界待核。",
        evidence=ev(
            "文字六〇三厂原厂房、印刷车间、仓库、附属生活设施、机修车间和三线记忆展厅；现园区改造仍保持部分工业空间肌理",
            "20世纪70—90年代大型文字印刷、制版和出版物生产技术，承担《毛泽东选集》、标准像和《邓小平文选》等重要出版物印制任务；具体设备型号与工艺档案待核",
            "三线建设、全国出版传播、六〇三职工和襄阳城市工业记忆；退休职工返园、展厅、非遗传承和研学活动提供代际传播渠道",
            "以修旧如旧方式改造为六〇三文创园，2025年建设603印·刻非遗传承中心和603印刷博物馆；园区已有多元文创业态，保护边界和展陈开放制度待核",
        ),
    )
    patch_record(
        existing_by_id["HBI-PROV-008"],
        source_keys=["huanggang_guanyao_details_2025"],
        aliases=["湖北管窑传统陶器生产制造基地", "岚头矶工艺陶器厂", "管窑陶器厂"],
        level="provincial",
        status="湖北省第二批省级工业遗产（2025年度）",
        notes="黄冈日报明确写作“岚头矶工艺陶器厂（湖北管窑传统陶器生产制造基地）”，确认两种名称指向同一2025年度省级工业遗产项目。报道补充1958年建厂、红砖车间、推板窑、旧礼堂、老车间、产品外销和国际艺术区活化利用；窑炉编号、产品档案和保护边界待核。",
        evidence=ev(
            "1958年红砖车间、推板窑车间、旧礼堂、老车间、美术馆/非遗展馆和工艺陶器生产空间；窑炉、窑具和厂区建筑编号待测绘",
            "管窑陶器生产、推板窑烧成、以陶土资源和水陆交通组织生产，产品出口20余个国家和地区；产品谱系、配方、窑具与工艺师档案待补",
            "万余名窑工、全国陶艺家邀请会、陶艺大师交流、国礼陶器和蕲春‘千年陶都’地方身份构成社会记忆；非遗展馆和研学活动持续传承",
            "旧礼堂改造文化小剧场，推板窑车间用于工业遗存展示，老车间改造为美术馆/非遗展馆，并建设国际艺术区、研学和文创空间；产权和开放规则待核",
        ),
        related_inventory_ids=["HBI-HG-007"],
    )
    patch_record(
        existing_by_id["HBI-PROV-009"],
        source_keys=["xiaogan_matang"],
        aliases=["孝感县麻糖厂", "孝感麻糖厂旧址", "城隍潭9号麻糖厂"],
        district="孝南区",
        notes="湖北日报目前只确认孝感市麻糖厂列入2025年度湖北省工业遗产拟认定名单，未找到可公开核验的最终认定通知，因此保留provincial_proposed层级。报道确认厂址为孝南区府前街道城隍潭9号，主体结构较完整，早期仓库、车间、捶麻工具和简易拌麻器具留存；孝感麻糖米酒产业仍在发展。",
        evidence=ev(
            "城隍潭9号麻糖厂主体建筑、早期仓库、车间、捶麻工具和简易拌麻器具；完整建筑测绘和实物目录待补",
            "1976年孝感县麻糖厂建立，标志孝感麻糖由手工作坊转向现代化生产；捶麻、拌麻和米糖食品工业流程需结合厂志补证",
            "孝感麻糖工人、城隍潭水系、地方副食品消费和几代城市居民记忆；孝感日报已补充公私合营、国营和改制沿革",
            "在孝感麻糖米酒有限责任公司维护下厂区主体仍保存；公开页面确认拟认定与现场遗存，保护责任、开放方式和最终名录状态待核",
        ),
    )
    hg = existing_by_id["HBI-HG-007"]
    merge_unique(hg, "source_keys", ["huanggang_guanyao_details_2025"])
    hg["related_inventory_ids"] = ["HBI-PROV-008"]
    hg["notes"] = "黄冈日报在2025年报道中将“岚头矶工艺陶器厂（湖北管窑传统陶器生产制造基地）”作为同一入选项目名称，已补充两条记录的明确关联；本条继续按厂址/活化利用载体表达，不新增独立省级认定。"
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_r_sources={len(NEW_SOURCES)} added_records={len(NEW_RECORDS)} "
        f"total_records={len(records)} total_sources={len(sources)} patched_records=8"
    )


if __name__ == "__main__":
    main()
