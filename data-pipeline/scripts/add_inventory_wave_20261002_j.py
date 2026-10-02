from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "ezhou_relics_2021": {
        "source_type": "government_register",
        "title": "鄂州市文物保护单位名录",
        "org": "鄂州市人民政府",
        "pub_date": "2021-11-11",
        "url": "https://www.ezhou.gov.cn/gk/zcwdpt/bm/swlj/202112/t20211202_445852.html",
        "authority": "A",
        "notes": "鄂州市政府公开名录逐项列出瓦窑咀窑址、梁子湖窑址（含华容王仓屋窑）、螃蟹山窑址、南窑嘴窑址、马嘴塝窑址、熊泗林窑址、杨家山窑址、上董古矿井和铁屎墩遗址的行政地址与市/省级层级；用于小型窑业、矿冶遗存的名称与地址核验。",
    },
    "ezhou_museum_relics_2010": {
        "source_type": "museum_register",
        "title": "鄂州市各级文物保护单位有关情况一览表",
        "org": "鄂州博物馆",
        "pub_date": "2010-01-01",
        "url": "https://ezbwg.com/ReadNews.asp?NewsID=129",
        "authority": "B",
        "notes": "鄂州博物馆公开的文保单位表列出瓦窑咀窑址、梁子湖窑址等古遗址的时代、地点和保护层级，作为市政府名录之外的交叉核验来源；具体公布日期按页面未标日期处理。",
    },
    "ezhou_wayao_2018": {
        "source_type": "government_news",
        "title": "瓦窑咀六朝馒头窑炉系我国南方地区首次发现",
        "org": "鄂州市人民政府",
        "pub_date": "2018-01-03",
        "url": "https://www.ezhou.gov.cn/zjez/ezrw/ezss/201801/t20180103_44699.html",
        "authority": "A",
        "notes": "鄂州市政府报道记录2016—2017年考古发掘、窑炉/作坊/沉泥池布局、陶瓷产品和窑具，确认瓦窑咀是六朝早期青瓷烧造大型手工业作坊遗址；用于补足陶瓷技术与生产组织证据。",
    },
    "ezhou_liangzi_history_2022": {
        "source_type": "government_news",
        "title": "梁子山史话（之三）",
        "org": "鄂州市人民政府",
        "pub_date": "2022-02-09",
        "url": "https://www.ezhou.gov.cn/zjez/ezrw/ezss/202202/t20220211_456066.html",
        "authority": "A",
        "notes": "鄂州市政府报道记录梁子湖窑址相关窑炉发掘、器物出土和从隋唐五代至明清延续的窑业历史，并说明梁子湖水系与人员货物交通；用于补足窑业技术、贸易和区域社会记忆。",
    },
    "wuhan_husi_kiln_2022": {
        "source_type": "official_media",
        "title": "武汉湖泗瓷窑址群将申报国家遗址公园",
        "org": "湖北省文化和旅游厅/湖北日报",
        "pub_date": "2022-01-06",
        "url": "https://wlt.hubei.gov.cn/bmdt/szyw/wh/202201/t20220106_3953816.shtml",
        "authority": "A",
        "notes": "省文旅厅转载湖北日报报道确认湖泗瓷窑址群为湖北地区最大的宋代制瓷窑场，分布180处窑堆、跨8个街道50个自然村，晚唐五代至元明延续，包含龙窑、原料、燃料和水运网络，并记录遗址公园规划。",
    },
    "wuhan_husi_kiln_2026": {
        "source_type": "government_news",
        "title": "中新网：武汉“湖泗瓷窑址群”：窑火曾映照古代民生百态",
        "org": "武汉市人民政府",
        "pub_date": "2026-07-06",
        "url": "https://www.wuhan.gov.cn/sy/kwh/202607/t20260706_2817332.shtml",
        "authority": "A",
        "notes": "武汉市政府转载报道补充湖泗窑产品、窑具、原料与水运、外销市场、窑工船工商贩聚居、江夏区博物馆展示和陶瓷技艺教育等工业文化证据；当前遗址开放边界仍需管理资料复核。",
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
    return row


def listed_production_evidence(kind: str, era: str, current: str) -> dict[str, str]:
    return ev(
        f"官方文保名录确认的{kind}遗址名称与行政位置；窑炉、矿井、作坊构筑物、产品和保护边界需现场核验",
        f"{era}{kind}构成工业技术线索；具体原料、工艺流程、工具、产品谱系和生产组织待考古报告或地方档案补证",
        f"{kind}与地方手工业、矿冶生产、运输贸易和社区形成的社会记忆；人物、组织和口述史待补",
        current,
    )


NEW_RECORDS: list[dict[str, Any]] = [
    rec(
        "HBI-WUHAN-052",
        "湖泗瓷窑址群",
        "武汉市",
        "古代陶瓷制造与水运贸易",
        "national_cultural_relic_related",
        "第五批全国重点文物保护单位（2001）；第一批省级文物保护单位",
        [
            "hubei_national_relics_1_8_2023",
            "hubei_provincial_relics_1098",
            "wuhan_husi_kiln_2022",
            "wuhan_husi_kiln_2026",
        ],
        "省文旅厅和武汉市政府资料共同确认湖泗瓷窑址群为晚唐五代至元明延续的古代制瓷窑场，2001年列入第五批全国重点文物保护单位；本条按古代规模化生产、原料供应、水运外销、窑工群体和当代展示的工业文化景观记录，不拆分180余处窑堆为未经核验的独立遗址。",
        ev(
            "江夏区梁子湖、斧头湖和鲁湖周边180余处窑堆、龙窑遗迹、匣钵、垫饼、窑具与出土瓷器；遗址公园保护边界和各窑堆构成待测绘",
            "晚唐五代至元明龙窑制瓷、青白瓷/青瓷烧造、高岭土取料、木材燃料和水运外销；湖北日报与武汉市政府资料记录窑业布局和产品谱系",
            "窑工、船工、商贩聚居形成的市镇社会，湖泗窑产品流向湖北及邻省，以及江夏区博物馆“湖泗风华”展和陶瓷技艺教育；人物与口述史待补",
            "国保身份、总体规划和江夏区博物馆展示已由官方资料确认；遗址公园建设、开放范围、产权和各窑堆保存状况需按最新管理资料复核",
        ),
        district="江夏区",
        aliases=["湖泗窑址群", "湖泗瓷窑址群遗址", "下浮山湾窑址"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-EZ-012",
        "瓦窑咀窑址",
        "鄂州市",
        "古代陶瓷制造",
        "provincial_heritage_related",
        "湖北省文物保护单位；东汉至六朝古遗址",
        ["hubei_provincial_relics_1098", "ezhou_relics_2021", "ezhou_wayao_2018"],
        "省级名录和鄂州市政府资料确认瓦窑咀窑址位于鄂城区凤凰街道司徒村；2016—2017年考古发掘发现密集窑址、作坊区、沉泥池、窑炉和窑具。本条记录六朝早期青瓷烧造手工业遗址，不把周边同名窑点未经核验地合并。",
        ev(
            "瓦窑咀窑址超过百座窑址的分布范围、8座已发掘窑炉、房址、灰坑、灰沟、水井、窑具和陶瓷产品；保护范围需按文保资料复核",
            "东汉至六朝馒头窑/龙窑烧造、陶土淘洗、沉泥池和作坊分区；鄂州市政府报道记录窑炉结构、青瓷和窑具，工艺复原仍需考古报告",
            "吴王城城市功能、窑工与长江中游瓷业发展的地方记忆；陶瓷生产与城市供给关系需结合出土和地方文献补证",
            "省级文保名录、主动性考古发掘和鄂州市政府报道已确认；展陈、开放、产权和遗址公园衔接情况待管理资料复核",
        ),
        district="鄂城区",
        aliases=["瓦窑咀六朝窑址", "瓦窑咀陶瓷窑址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-EZ-013",
        "梁子湖窑址",
        "鄂州市",
        "古代陶瓷制造",
        "provincial_heritage_related",
        "湖北省文物保护单位；五代古遗址（含华容王仓屋窑、柯坟山窑合并关系）",
        ["hubei_provincial_relics_1098", "ezhou_relics_2021", "ezhou_museum_relics_2010", "ezhou_liangzi_history_2022"],
        "省级名录、鄂州市政府和鄂州博物馆资料确认梁子湖窑址位于梁子镇及梁子湖周边，王仓屋窑、柯坟山窑按名录合并关系作为组成/关联项记录。地方报道记录窑炉、器物和从隋唐五代至明清延续的窑业，具体窑点边界仍需考古资料核验。",
        ev(
            "梁子湖窑址及王仓屋、柯坟山等关联窑点、窑炉、陶瓷器物和窑具；各组成项边界和保存状态待测绘",
            "五代至明清窑业生产、陶土处理、烧造和湖区水运；鄂州市政府报道记录窑炉发掘、器物和延续年代，详细工艺谱系待补",
            "梁子湖水系人员往来、货物贸易和窑工聚居形成的地方工业文化记忆；地方文献与口述史待补",
            "省级文保身份和名录合并关系已确认；遗址保护范围、展示利用和各窑点管理责任需复核",
        ),
        district="梁子湖区",
        aliases=["梁子湖瓦窑澥遗址", "王仓屋窑址", "柯坟山窑址"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-EZ-014",
        "螃蟹山窑址",
        "鄂州市",
        "古代陶瓷制造",
        "municipal_related",
        "鄂州市文物保护单位",
        ["ezhou_relics_2021", "ezhou_museum_relics_2010"],
        "鄂州市政府公开文保名录逐项列出螃蟹山窑址及其位于梁子湖区涂家垴镇涂镇村的地址。本条作为地方窑业遗存进入扩展底册，窑炉年代、产品、工艺、保护级别和现状利用均保持待核。",
        listed_production_evidence("螃蟹山窑址", "时代与窑业类型待考古核定；", "鄂州市文物保护单位名录身份已确认；窑址保存、保护范围、产权和开放利用待地方资料复核"),
        district="梁子湖区",
        aliases=["螃蟹山古窑址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-EZ-015",
        "南窑嘴窑址",
        "鄂州市",
        "古代陶瓷制造",
        "municipal_related",
        "鄂州市文物保护单位",
        ["ezhou_relics_2021"],
        "鄂州市政府公开文保名录逐项列出南窑嘴窑址及其位于梁子湖区涂家垴镇南阳村的地址。本条作为地方窑业遗存进入扩展底册，年代、窑炉构成、产品和保存状态待考古与现场资料核验。",
        listed_production_evidence("南窑嘴窑址", "时代与窑业类型待考古核定；", "鄂州市文物保护单位名录身份已确认；窑址保存、保护范围、产权和开放利用待地方资料复核"),
        district="梁子湖区",
        aliases=["南窑嘴古窑址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-EZ-016",
        "马嘴塝窑址",
        "鄂州市",
        "古代陶瓷制造",
        "municipal_related",
        "鄂州市文物保护单位",
        ["ezhou_relics_2021"],
        "鄂州市政府公开文保名录逐项列出马嘴塝窑址及其位于梁子湖区涂家垴镇王桥村的地址。本条作为地方窑业遗存进入扩展底册，年代、窑炉构成、产品和保存状态待考古与现场资料核验。",
        listed_production_evidence("马嘴塝窑址", "时代与窑业类型待考古核定；", "鄂州市文物保护单位名录身份已确认；窑址保存、保护范围、产权和开放利用待地方资料复核"),
        district="梁子湖区",
        aliases=["马嘴塝古窑址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-EZ-017",
        "熊泗林窑址",
        "鄂州市",
        "古代陶瓷制造",
        "municipal_related",
        "鄂州市文物保护单位",
        ["ezhou_relics_2021"],
        "鄂州市政府公开文保名录逐项列出熊泗林窑址及其位于梁子湖区涂家垴镇万秀村的地址。本条作为地方窑业遗存进入扩展底册，年代、窑炉构成、产品和保存状态待考古与现场资料核验。",
        listed_production_evidence("熊泗林窑址", "时代与窑业类型待考古核定；", "鄂州市文物保护单位名录身份已确认；窑址保存、保护范围、产权和开放利用待地方资料复核"),
        district="梁子湖区",
        aliases=["熊泗林古窑址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-EZ-018",
        "杨家山窑址",
        "鄂州市",
        "古代陶瓷制造",
        "municipal_related",
        "鄂州市文物保护单位",
        ["ezhou_relics_2021"],
        "鄂州市政府公开文保名录逐项列出杨家山窑址及其位于梁子湖区涂家垴镇公友村的地址。本条作为地方窑业遗存进入扩展底册，年代、窑炉构成、产品和保存状态待考古与现场资料核验。",
        listed_production_evidence("杨家山窑址", "时代与窑业类型待考古核定；", "鄂州市文物保护单位名录身份已确认；窑址保存、保护范围、产权和开放利用待地方资料复核"),
        district="梁子湖区",
        aliases=["杨家山古窑址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-EZ-019",
        "上董古矿井",
        "鄂州市",
        "古代矿冶与采矿",
        "municipal_related",
        "鄂州市文物保护单位",
        ["ezhou_relics_2021"],
        "鄂州市政府公开文保名录列出上董古矿井及其位于鄂城区汀祖镇吴垴村的地址。本条仅确认地方文保名录身份和矿井名称，不把矿种、开采年代、巷道构成或冶炼关系写成已证实事实，待地方考古与矿冶史资料补证。",
        ev(
            "上董古矿井遗址及其井口、巷道、采矿构筑物和矿石遗存；官方名录仅给出名称与地址，具体构成待现场核验",
            "古代采矿与可能的矿冶生产技术线索；矿种、年代、采掘工具、运输和冶炼关系当前证据不足，保持待核",
            "鄂城区汀祖矿冶传统、矿工群体和地方资源记忆；人物、组织和口述史待补",
            "鄂州市文物保护单位名录身份已确认；保存状态、保护范围、产权、开放和安全管理待复核",
        ),
        district="鄂城区",
        aliases=["上董古矿井遗址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-EZ-020",
        "铁屎墩遗址",
        "鄂州市",
        "古代矿冶线索",
        "municipal_related",
        "鄂州市文物保护单位",
        ["ezhou_relics_2021"],
        "鄂州市政府公开文保名录列出铁屎墩遗址及其位于梁子湖区涂家垴镇涂镇村的地址。名称提示可能存在铁屑或冶炼相关遗存，但当前公开名录未说明年代、矿种和功能，本条作为矿冶研究线索记录并保持待核。",
        ev(
            "铁屎墩遗址及可能的炉渣、矿冶堆积、窑炉或采矿构筑物；当前仅有名录名称和地址，遗存构成待考古核验",
            "可能涉及铁矿采冶或相关手工业生产；年代、工艺、工具、产品和生产组织没有公开直接证据，保持待核",
            "梁子湖区域资源开发、矿冶地名和地方生产记忆；社会记忆与口述史待补",
            "鄂州市文物保护单位名录身份已确认；是否为工业遗址、保存状态和保护利用方式待专项调查",
        ),
        district="梁子湖区",
        aliases=["铁屎墩古冶炼遗址（功能待核）"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-JM-016",
        "钟祥市谢家湾古冶铜遗址",
        "荆门市",
        "古代铜冶炼与矿冶",
        "provincial_heritage_related",
        "第三批湖北省文物保护单位；东周古文化遗址",
        ["hubei_provincial_relics_1098", "hubei_industrial_heritage_reply_2018"],
        "省级文保名录列出东周谢家湾古冶铜遗址，所在地为荆门市钟祥市；省文旅厅工业遗产答复把湖北远古铜冶炼纳入工业遗产历史序列。本条记录古代矿冶生产遗址，矿坑、炉址、炉渣、产品和保护范围需地方考古资料核验。",
        listed_production_evidence("谢家湾古冶铜", "东周；", "省级文保名录身份已确认；遗址保存、展示、产权和保护工程待复核"),
        district="钟祥市",
        aliases=["谢家湾古冶铜遗址", "谢家湾古矿冶遗址"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-SY-015",
        "郧阳区安城古铜矿遗址",
        "十堰市",
        "古代铜矿采冶",
        "provincial_heritage_related",
        "第三批湖北省文物保护单位；东周古文化遗址",
        ["hubei_provincial_relics_1098", "hubei_industrial_heritage_reply_2018"],
        "省级文保名录列出东周安城古铜矿遗址，所在地为十堰市郧阳区；省文旅厅工业遗产答复把湖北远古铜冶炼纳入工业遗产历史序列。本条记录古代铜矿采冶遗址，具体矿坑、冶炼遗存、产品与保护范围需地方考古资料核验。",
        listed_production_evidence("安城古铜矿", "东周；", "省级文保名录身份已确认；遗址保存、展示、产权和保护工程待复核"),
        district="郧阳区",
        aliases=["安城古铜矿遗址", "安城古矿冶遗址"],
        asset_kind="industrial_site",
    ),
]


PATCHES: dict[str, dict[str, Any]] = {
    "HBI-WUHAN-006": {
        "district_county": "硚口区",
        "recognition_status": "第一批中国工业遗产保护名录；湖北省省级文物保护单位名录；武汉市首批工业遗产一级",
        "source_keys": ["hubei_industrial_heritage_reply_2018"],
        "aliases": ["既济水电公司宗关水厂旧址", "汉口既济水电公司宗关水厂旧址", "宗关水厂旧址"],
        "asset_kind": "industrial_site",
        "notes": "官方省文旅厅答复把汉口既济水电公司宗关水厂列入第一批中国工业遗产保护名录语境；省级文保名录登记为既济水电公司宗关水厂旧址，武汉首批工业遗产名录使用宗关水厂简名。本条合并同一对象，补足水源、供水技术、职工和城市公共基础设施文化证据，仍需核验建筑/设备清单与保护边界。",
        "cultural_evidence": ev(
            "宗关水厂取水、净水、泵房、水塔、管网和厂区建筑；现存设备、建筑年代和保护范围待测绘",
            "既济水电公司供水与供电合营、汉江取水、净水处理和城市管网运行技术；设备谱系与档案待补",
            "近代武汉公共供水、城市卫生、供水职工和居民用水的社会记忆；口述史和用户档案待补",
            "第一批中国工业遗产保护名录、湖北省文保名录和武汉市工业遗产语境已确认；现状使用、开放、产权和修缮需按最新资料复核",
        ),
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
    existing_names = {row["name"] for row in records}
    duplicate_ids = {row["inventory_id"] for row in NEW_RECORDS} & set(existing_by_id)
    duplicate_names = {row["name"] for row in NEW_RECORDS} & existing_names
    if duplicate_ids or duplicate_names:
        all_new_present = all(
            row["inventory_id"] in existing_by_id
            and existing_by_id[row["inventory_id"]]["name"] == row["name"]
            for row in NEW_RECORDS
        )
        if not all_new_present:
            raise SystemExit(
                "partial or conflicting prior application: "
                f"ids={sorted(duplicate_ids)} names={sorted(duplicate_names)}"
            )
    else:
        sources.update({key: value for key, value in NEW_SOURCES.items() if key not in sources})
        records.extend(NEW_RECORDS)

    for inventory_id, patch in PATCHES.items():
        row = existing_by_id.get(inventory_id)
        if row is None:
            raise SystemExit(f"patch target missing: {inventory_id}")
        for key in ("source_keys", "aliases"):
            values = patch.get(key)
            if values:
                merge_unique(row, key, values)
        for key, value in patch.items():
            if key not in {"source_keys", "aliases"}:
                row[key] = value

    data["research_targets"]["coverage_rule"] = (
        "每条对象至少绑定名录/普查/规划/企业史/档案遗产或来源确认资料；"
        "工业遗产实体、工业文化景观、工业旅游相关场景、档案文献和待核验线索分层记录。"
        "文化证据字段只记录来源中明确出现的载体、技术、社会记忆和利用状态，未核实内容保持待核。"
    )
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"wave_j_records={len(NEW_RECORDS)} wave_j_sources={len(NEW_SOURCES)} "
        f"patched_records={len(PATCHES)} total_records={len(records)} total_sources={len(sources)}"
    )


if __name__ == "__main__":
    main()
