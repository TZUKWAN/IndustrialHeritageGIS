from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "ezhou_relics_2021_industrial_rows": {
        "source_type": "government_register_detail",
        "title": "鄂州市文物保护单位名录（工业遗址相关条目）",
        "org": "鄂州市人民政府",
        "pub_date": "2021-11-11",
        "url": "https://www.ezhou.gov.cn/gk/zcwdpt/bm/swlj/202112/t20211202_445852.html",
        "authority": "A",
        "notes": "官方名录逐项列出铜灶矿冶遗址、徐王湾矿冶遗址、童家坝遗址、武圣宫遗址和西山矿槽遗址及行政地址；本来源用于核对名称、现行市级文保身份与地址，不把名录身份直接等同于工业遗产认定。",
    },
    "ezhou_museum_industrial_table_2010": {
        "source_type": "museum_register_detail",
        "title": "鄂州市各级文物保护单位有关情况一览表（矿冶、铸钱和冶炼条目）",
        "org": "鄂州博物馆",
        "pub_date": "2011-02-22",
        "url": "https://ezbwg.com/ReadNews.asp?NewsID=129",
        "authority": "B",
        "notes": "鄂州博物馆公开表格将童家坝记为宋代铸钱遗址、铜灶记为宋代遗址、武圣宫记为太平天国冶炼遗址、西山矿槽记为抗日战争时期矿槽；这些时代和功能信息作为交叉来源保留，正式考古报告与现状调查仍需补证。",
    },
    "ezhou_airport_archaeology_2020": {
        "source_type": "government_archaeology_news",
        "title": "鄂州机场考古再发掘出一批六朝古墓、唐宋窑址",
        "org": "鄂州市文化和旅游局",
        "pub_date": "2020-06-15",
        "url": "https://wtxgj.ezhou.gov.cn/xwdt/wlyw/202006/t20200615_341117.html",
        "authority": "A",
        "notes": "官方报道确认鄂州机场文物保护项目勘探约90万平方米、发掘20座窑址，并具体记载余家山唐代龙窑主体约45米长、约3米宽，以及朱家咀唐宋冶炼遗址的两座窑炉基底和附属柱洞；报道将其解释为可能的手工业作坊生产区域。两处尚未见独立公布的工业遗产名录名称，故分层为来源确认的考古工业遗址候选。",
    },
    "ezhou_qiyaoshan_craft_2018": {
        "source_type": "government_cultural_history",
        "title": "寻找鄂州原始先民的足迹（之二）",
        "org": "鄂州市人民政府",
        "pub_date": "2018-05-23",
        "url": "https://www.ezhou.gov.cn/zjez/ezrw/ezwy/201805/t20180523_45120.html",
        "authority": "A",
        "notes": "鄂州市政府文化史文章指出燕矶沙塘村七窑山遗址出土纺轮，并以纺轮解释史前纺线活动；文章同时讨论鄂州史前制陶和纺织技术，但未提供七窑山完整出土报告，故仅用于工业文化线索分层。",
    },
    "ezhou_qiyaoshan_protection_2019": {
        "source_type": "government_protection_notice",
        "title": "省政府公布45处文物保护单位保护范围和建设控制地带（鄂州相关）",
        "org": "鄂州市人民政府",
        "pub_date": "2019-02-27",
        "url": "https://www.ezhou.gov.cn/zjez/ezrw/ezwy/201902/t20190227_179325.html",
        "authority": "A",
        "notes": "官方报道明确七窑山遗址属于第五批湖北省文物保护单位，并列入省政府公布保护范围和建设控制地带的鄂州相关单位；具体边界应以省政府原始文件和现场测绘为准。",
    },
    "wuhan_jiang_an_factory_history_2021": {
        "source_type": "municipal_government_media",
        "title": "120年老厂新型铁路货车享誉全球",
        "org": "武汉市人民政府",
        "pub_date": "2021-06-16",
        "url": "https://www.wuhan.gov.cn/sy/whyw/202106/t20210616_1720993.shtml",
        "authority": "A",
        "notes": "武汉市政府报道记载江岸机厂始建于1901年、源于芦汉铁路建设，承担机车车辆修理并不断扩建；报道还记录林祥谦1912年进入江岸机厂及工人劳动记忆，用于补足江岸车辆厂的铁路生产、技术和社会文化证据。",
    },
    "wuhan_yuehan_rail_assets_2019": {
        "source_type": "municipal_government_response",
        "title": "市文化和旅游局关于激活粤汉铁路文化价值建议的答复",
        "org": "武汉市文化和旅游局",
        "pub_date": "2019-08-29",
        "url": "https://www.wuhan.gov.cn/ztzl/jytabl/swlj/sjytaa/202003/t20200316_950533.shtml",
        "authority": "A",
        "notes": "武汉市政府公开答复明确把芦汉铁路江岸机厂等铁路资源纳入全市工业遗产分级分类保护，并把江岸机厂、江岸车站会议室等资源纳入城市紫线；页面同时提示申报资料仍需整理，故本条补强保护制度证据而不扩大正式名录层级。",
    },
}


SOURCE_NOTE_UPDATES: dict[str, str] = {
    "ezhou_relics_2021": (
        "鄂州市政府公开名录逐项列出瓦窑咀窑址、梁子湖窑址（含华容王仓屋窑）、螃蟹山窑址、"
        "南窑嘴窑址、马嘴塝窑址、熊泗林窑址、杨家山窑址、上董古矿井、铁屎墩遗址，以及本轮补入的"
        "铜灶矿冶遗址、徐王湾矿冶遗址、童家坝遗址、武圣宫遗址和西山矿槽遗址；用于小型窑业、矿冶、"
        "铸钱和战争时期矿山遗存的名称与行政地址核验。"
    ),
    "ezhou_museum_relics_2010": (
        "鄂州博物馆公开的文保单位表列出瓦窑咀窑址、梁子湖窑址等古遗址的时代、地点和保护层级，"
        "并将童家坝记为宋代铸钱遗址、铜灶记为宋代遗址、武圣宫记为太平天国冶炼遗址、西山矿槽记为"
        "抗日战争时期矿槽；作为市政府名录之外的交叉核验来源，正式考古报告和现状仍需补证。"
    ),
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
    recognition_status: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "inventory_id": inventory_id,
        "name": name,
        "city": "鄂州市",
        "district_county": district,
        "industry_category_l1": industry,
        "recognition_level": level,
        "recognition_status": recognition_status or status,
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
    return row


NEW_RECORDS: list[dict[str, Any]] = [
    rec(
        "HBI-EZ-021",
        "铜灶矿冶遗址",
        "古代矿冶与采矿",
        "municipal_related",
        "鄂州市文物保护单位",
        ["ezhou_relics_2021_industrial_rows", "ezhou_museum_industrial_table_2010"],
        "鄂州市政府名录列出铜灶矿冶遗址，地址为鄂城区汀祖镇丁祖村石桥中学西；鄂州博物馆表称铜灶遗址为宋代、位于汀祖采矿场范围。本条确认地方文保和矿冶线索，不把矿种、炉址范围或保存状态写成已核实事实。",
        ev(
            "铜灶矿冶遗址及其所在汀祖矿区空间；具体井口、炉渣、炉体和边界待考古与现场测绘",
            "宋代矿冶和采矿活动线索；矿石来源、冶炼流程、工具与年代需考古报告复核",
            "汀祖矿工、资源开采和鄂州古代矿冶传统记忆；地方口述与产业谱系待采集",
            "列入鄂州市文物保护单位名录；现状保存、产权、开放和安全范围待核",
        ),
        district="鄂城区",
        aliases=["铜灶遗址", "铜灶古矿冶遗址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-EZ-022",
        "徐王湾矿冶遗址",
        "古代矿冶与采矿",
        "municipal_related",
        "鄂州市文物保护单位",
        ["ezhou_relics_2021_industrial_rows"],
        "鄂州市政府名录列出徐王湾矿冶遗址，地址为鄂城区汀祖镇洪山村3组徐王湾北面。本条仅据官方名录确认名称、地址与地方文保身份，矿种、年代、生产环节和遗存构成待考古与现场核验。",
        ev(
            "徐王湾矿冶遗址及其地表、地下遗存；井口、矿坑、炉渣和相关构筑物清单待核",
            "矿冶生产线索已由遗址名称确认；采矿、选矿、冶炼和运输工艺尚缺公开考古细节",
            "汀祖镇矿冶资源、矿工劳动和村落生产记忆待地方志与口述史补证",
            "列入鄂州市文物保护单位名录；保护范围、保存状态和利用方式待核",
        ),
        district="鄂城区",
        aliases=["徐王湾古矿冶遗址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-EZ-023",
        "童家坝铸钱遗址",
        "古代铸钱与金属加工",
        "municipal_related",
        "鄂州市文物保护单位名录（公布名：童家坝遗址）",
        ["ezhou_relics_2021_industrial_rows", "ezhou_museum_industrial_table_2010"],
        "鄂州市政府名录以童家坝遗址列出鄂城区沙窝乡黄山村16组童家坝湾；鄂州博物馆表进一步记为宋代童家坝铸钱遗址，并记有炼渣存放地。本条将名称差异和铸钱功能并列保存，正式考古年代、遗存范围和保护状态仍需复核。",
        ev(
            "童家坝遗址、村前及湖边炼渣存放地；铸钱模具、炉体、钱范与金属残留待考古核验",
            "宋代铸钱、熔炼和金属加工技术线索；炉料、钱范和工序关系待考古报告补证",
            "货币生产、地方市场和金属手工业者的区域记忆待地方文献与博物馆资料补充",
            "列入鄂州市文物保护单位名录；现状保存、边界和可展示性待核",
        ),
        district="鄂城区",
        aliases=["童家坝遗址", "童家坝铸钱遗址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-EZ-024",
        "西山矿槽遗址",
        "近现代采掘冶金工业",
        "municipal_related",
        "鄂州市文物保护单位",
        ["ezhou_relics_2021_industrial_rows", "ezhou_museum_industrial_table_2010"],
        "鄂州市政府名录列出西山矿槽遗址，地址为鄂城区西山街道西山社区西山东北麓山脚；鄂州博物馆表称其为抗日战争时期、位于鄂钢西山铁矿矿区。本条记录矿山战争时期工业遗存，具体矿槽、运输和防护设施待现场核验。",
        ev(
            "西山矿槽遗址、矿区山脚空间及可能的矿槽、堆场和运输设施；具体物项待测绘",
            "抗战时期铁矿采掘、矿石转运和矿山保障技术线索；设备与工艺待档案补证",
            "鄂钢西山铁矿、矿工劳动和战时资源供给记忆；人物与企业沿革待补",
            "列入鄂州市文物保护单位名录；保存状态、产权、开放和安全边界待核",
        ),
        district="鄂城区",
        aliases=["矿槽", "西山铁矿矿槽"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-EZ-025",
        "武圣宫冶炼遗址",
        "近代矿冶与冶炼工业",
        "municipal_related",
        "鄂州市文物保护单位名录（公布名：武圣宫遗址）",
        ["ezhou_relics_2021_industrial_rows", "ezhou_museum_industrial_table_2010"],
        "鄂州市政府名录以武圣宫遗址列出梁子湖区东沟镇鲊州村上鲊洲湾等地址；鄂州博物馆表将其记为太平天国时期武圣宫冶炼遗址。本条保留名称与功能差异，不把遗址范围、炉渣和冶炼品种写成已证实事实。",
        ev(
            "武圣宫遗址及公路两侧相关遗存空间；炉址、炉渣、矿料和作坊构成待考古与现场核验",
            "太平天国时期冶炼活动线索；燃料、炉型、矿料和产品谱系待考古报告补证",
            "鲊洲地区冶炼、交通和地方社会记忆待地方志与口述史补充",
            "列入鄂州市文物保护单位名录；保护范围、保存状态和开放方式待核",
        ),
        district="梁子湖区",
        aliases=["武圣宫遗址", "武圣宫冶炼遗址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-EZ-026",
        "余家山唐代龙窑",
        "古代陶瓷制造",
        "research_candidate",
        "鄂州机场文物保护项目考古发现（2020年官方报道；未见独立公布名录名称）",
        ["ezhou_airport_archaeology_2020"],
        "鄂州市文化和旅游局报道确认鄂州机场考古发现余家山唐代龙窑，主体约45米长、约3米宽，为湖北地区罕见的龙窑。报道未提供完整坐标、保护范围和后续展示信息，因此作为来源确认的考古工业遗址候选，不等同正式工业遗产认定。",
        ev(
            "余家山唐代龙窑窑体及机场考古发掘区；窑具、作坊、灰坑和保存状态需查考古档案",
            "龙窑窑炉结构与唐代陶瓷烧造技术；产品类型、燃料和窑业组织待发掘报告补证",
            "鄂州湖区交通、陶工群体与唐代区域陶瓷供给网络为待研究的社会记忆线索",
            "已由鄂州机场文物保护项目官方报道确认考古发现；后续保护、迁移、展示和建设影响待核",
        ),
        aliases=["余家山龙窑", "余家山唐代窑址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-EZ-027",
        "朱家咀唐宋冶炼遗址",
        "古代矿冶与冶炼工业",
        "research_candidate",
        "鄂州机场文物保护项目考古发现（2020年官方报道；未见独立公布名录名称）",
        ["ezhou_airport_archaeology_2020"],
        "鄂州市文化和旅游局报道确认朱家咀唐宋冶炼遗址发现2座窑炉基底及附属柱洞，并由湖北省文物考古研究所分析为可能的手工业作坊生产区域。报道未公布独立保护名录、完整坐标和现状边界，因此保持考古候选层级。",
        ev(
            "两座窑炉基底、附属柱洞及机场考古发掘区；炉渣、矿料、作坊建筑和组合关系待报告核验",
            "唐宋时期手工冶铸、窑炉组合和矿产资源利用线索；具体金属品种与工序待考古资料补证",
            "湖叉水运、矿产资源、手工业作坊和区域聚落生产记忆由官方分析提出，地方文献与口述史待补",
            "已由鄂州机场文物保护项目官方报道确认考古发现；保护、展示和建设后续影响待核",
        ),
        aliases=["朱家咀手工冶铸遗址", "朱家咀唐宋冶炼遗址"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-EZ-028",
        "七窑山遗址",
        "史前纺织与制陶手工业",
        "provincial_heritage_related",
        "第五批湖北省文物保护单位（古遗址；未单独认定工业遗产）",
        ["ezhou_relics_2021_industrial_rows", "ezhou_qiyaoshan_craft_2018", "ezhou_qiyaoshan_protection_2019"],
        "鄂州市政府名录和保护报道确认七窑山遗址位于鄂城区燕矶镇沙塘村并属于第五批湖北省文物保护单位；官方文化史文章指出遗址有纺轮，并以此说明史前纺线活动。七窑山是工业文化研究线索，不把普通古遗址身份直接升级为工业遗产，制陶与纺织生产规模及遗存组合待考古报告核验。",
        ev(
            "七窑山遗址、纺轮等生产工具线索及考古地层；出土组合、作坊和保存边界待考古资料核验",
            "纺轮反映史前纺线技术；区域制陶工艺可作关联线索，但七窑山的具体制陶流程与生产组织尚未证实",
            "史前纺织、制陶、家庭分工和鄂州地方手工业源流构成研究性文化记忆；口述传统不适用，需以考古解释为主",
            "列入第五批湖北省文物保护单位并有保护范围报道；现状保存、开放和展示利用待核",
        ),
        district="鄂城区",
        aliases=["燕矶七窑山遗址"],
        asset_kind="industrial_cultural_landscape",
    ),
]


UPDATES: dict[str, dict[str, Any]] = {
    "HBI-WUHAN-002": {
        "source_keys_add": [
            "wuhan_jiang_an_factory_history_2021",
            "wuhan_yuehan_rail_assets_2019",
        ],
        "aliases": ["江岸机厂", "江岸车辆厂旧址", "芦汉铁路江岸机厂"],
        "recognition_status": "武汉市首批工业遗产三级；市政府公开答复将芦汉铁路江岸机厂等铁路资源纳入工业遗产分级分类保护和城市紫线",
        "notes": "武汉市首批工业遗产名录中的江岸车辆厂与芦汉铁路江岸机厂为同一铁路修造工业谱系，合并为一条主档案。武汉市政府报道确认江岸机厂始建于1901年、源于芦汉铁路建设，承担机车车辆修理并不断扩建；2019年市文旅局公开答复又明确将江岸机厂、江岸车站会议室等铁路遗产纳入城市紫线和全市工业遗产分级分类保护。具体厂区边界、现存建筑/设备、产权和开放状态仍需铁路档案与现场核验。",
        "cultural_evidence": ev(
            "1901年始建的江岸机厂/江岸车辆厂铁路工业空间，以及江岸车站会议室等关联铁路遗产；现存厂房、机修设备和边界待测绘",
            "芦汉铁路贯通后机车车辆修理、扩建和铁路装备维修技术；生产线、设备谱系和法国管理档案待补",
            "林祥谦1912年进入江岸机厂、铁路工人劳动与工运记忆，以及江岸车辆厂对铁路运输的长期支撑构成核心社会价值",
            "武汉市首批工业遗产三级；2019年市政府答复称相关铁路资源纳入城市紫线和分级分类保护，现状保存、产权、展示和开放方式待核",
        ),
    }
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

    duplicate_ids = {row["inventory_id"] for row in NEW_RECORDS} & set(existing_by_id)
    if duplicate_ids:
        if not all(existing_by_id[i] == row for i, row in ((r["inventory_id"], r) for r in NEW_RECORDS if r["inventory_id"] in duplicate_ids)):
            raise SystemExit(f"conflicting duplicate records: {sorted(duplicate_ids)}")
    else:
        records.extend(NEW_RECORDS)

    for inventory_id, patch in UPDATES.items():
        row = existing_by_id.get(inventory_id)
        if row is None:
            raise SystemExit(f"update target missing: {inventory_id}")
        merge_unique(row, "source_keys", patch.get("source_keys_add") or [])
        merge_unique(row, "aliases", patch.get("aliases") or [])
        for key, value in patch.items():
            if key not in {"source_keys_add", "aliases"}:
                row[key] = value
        row["source_keys"] = sorted(set(row.get("source_keys") or []))

    sources.update({key: value for key, value in NEW_SOURCES.items() if key not in sources})
    for key, note in SOURCE_NOTE_UPDATES.items():
        if key in sources:
            sources[key]["notes"] = note
        else:
            raise SystemExit(f"source note update target missing: {key}")
    data["research_targets"]["coverage_rule"] = (
        "每条对象至少绑定名录/普查/规划/企业史/档案遗产或来源确认资料；"
        "工业遗产实体、工业文化景观、工业金融与贸易节点、工业旅游相关场景、档案文献和待核验线索分层记录。"
        "古代窑业、矿冶、铸钱与史前纺织遗址仅在来源明确出现生产性证据时纳入，并保留考古候选或相关层级；"
        "文化证据字段只记录来源中明确出现的载体、技术、社会记忆和利用状态，未核实内容保持待核。"
    )
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_o_sources={len(NEW_SOURCES)} added_records={len(NEW_RECORDS)} "
        f"patched_records={len(UPDATES)} total_records={len(records)} total_sources={len(sources)}"
    )


if __name__ == "__main__":
    main()
