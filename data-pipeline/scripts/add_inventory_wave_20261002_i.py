from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "hubei_national_relics_1_8_2023": {
        "source_type": "government_register",
        "title": "湖北省1—8批次全国重点文物保护单位名录",
        "org": "湖北省文化和旅游厅",
        "pub_date": "2023-09-28",
        "url": "https://wlt.hubei.gov.cn/bsfw/bmcxfw/wwbhdwml/202309/t20230928_4871978.shtml",
        "authority": "A",
        "notes": "省文旅厅公开的全国重点文物保护单位名录，逐项列出汉口英商电灯公司旧址、武汉长江大桥等对象的批次、年代、行政区和并入汉口近代建筑群等关系；用于国保身份和名称交叉核验。",
    },
    "wuhan_lamp_history_2020": {
        "source_type": "government_news",
        "title": "左岸淑女 右岸侠客",
        "org": "武汉市发展和改革委员会",
        "pub_date": "2020-01-16",
        "url": "https://fgw.wuhan.gov.cn/xwzx/mtgz/202001/t20200116_864875.html",
        "authority": "A",
        "notes": "武汉市发改委报道确认1906年5月英商在汉口界限路8号创办汉口电灯公司并开始安装路灯，补足电力照明的技术、城市基础设施和社会记忆语境；旧址现状需另行核验。",
    },
    "wuhan_dazhimeng_station_2024": {
        "source_type": "government_news",
        "title": "拐个弯走进老武汉！天声街，该你上场了",
        "org": "武汉市人民政府",
        "pub_date": "2024-05-19",
        "url": "https://www.wuhan.gov.cn/sy/whyw/202405/t20240519_2404215.shtml",
        "authority": "A",
        "notes": "武汉市政府报道确认大智门火车站始建于1903年、为中国早期铁路站之一，2001年列入第五批全国重点文物保护单位，并记录铁路街、车站搬迁和周边城市记忆；用于补足铁路工业文化和现状叙事。",
    },
    "wuhan_8th_relics_2021": {
        "source_type": "government_news",
        "title": "武汉市新增6处省级文物保护单位",
        "org": "武汉市文化和旅游局",
        "pub_date": "2021-12-27",
        "url": "https://wlj.wuhan.gov.cn/zwgk_27/zwdt/xydt/202112/t20211227_1882207.shtml",
        "authority": "A",
        "notes": "武汉市文旅局逐项列出顺丰茶栈旧址等新增省级文物保护单位，并说明其属于近现代重要史迹及代表性建筑、部分为万里茶道遗产点；用于确认名称、级别和茶业文化联系。",
    },
    "wuhan_tea_trade_2019": {
        "source_type": "government_reply",
        "title": "关于市政协第十三届二次会议第20180012号提案的答复",
        "org": "武汉市供销合作总社",
        "pub_date": "2019-08-22",
        "url": "https://gxs.wuhan.gov.cn/zfxxgk/fdzdgknr/jytabl/201908/t20190822_21550.shtml",
        "authority": "A",
        "notes": "政府答复以顺丰茶栈等汉口茶建筑为再生式保护经营对象，说明汉口东方茶港、青砖茶产业和万里茶道的公共文化利用语境；不替代对全部历史设备和厂址边界的现场核验。",
    },
    "hubei_red_tea_cultural_2022": {
        "source_type": "government_news",
        "title": "宜都红茶厂（旧址）打卡点揭牌",
        "org": "湖北省文化和旅游厅",
        "pub_date": "2022-08-30",
        "url": "https://wlt.hubei.gov.cn/bmdt/mtjj/202208/t20220830_4284937.shtml",
        "authority": "A",
        "notes": "省文旅厅转载报道确认宜都红茶厂（旧址）始建于1951年，木结构茶叶生产线和风选机、平圆筛等设备保存，入选中国工业遗产保护名录第二批，并记录档案整理、茶旅展示和博物馆筹办；现状开放范围仍需复核。",
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


NEW_RECORDS: list[dict[str, Any]] = [
    rec(
        "HBI-WUHAN-049",
        "汉口电话局旧址",
        "武汉市",
        "通信与城市基础设施",
        "provincial_heritage_related",
        "湖北省省级文物保护单位（1098处名录）；武汉市近代工业与城市基础设施遗产语境",
        ["hubei_provincial_relics_1098", "wuhan_plan"],
        "湖北省省级文物保护单位名录逐项列出1915年的汉口电话局旧址，所在地为武汉市江岸区；武汉市工业遗产保护规划提供城市工业遗存普查和保护制度背景。本条把电话交换建筑作为通信工业文化遗产记录，设备、保护范围和现状使用仍需专项测绘与档案核验。",
        ev(
            "1915年汉口电话局旧址建筑、电话交换空间及可能保留的线路/机房构件；设备清单、建筑测绘和保护边界待核",
            "近代电话交换、城市通信网络运行和机房管理技术记忆；交换机、线路图、运营档案和职工谱系待补",
            "汉口城市电话服务、通信职工和近代商业生活的社会记忆；用户史料与口述史待补",
            "省级文物保护单位名录身份已确认；现状产权、开放方式、设备保存和保护工程需按最新管理资料复核",
        ),
        district="江岸区",
        aliases=["汉口电话局大楼"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-WUHAN-050",
        "大智门火车站",
        "武汉市",
        "铁路运输与城市交通",
        "national_cultural_relic_related",
        "第五批全国重点文物保护单位（2001）",
        [
            "hubei_national_relics_1_8_2023",
            "hubei_provincial_relics_1098",
            "wuhan_dazhimeng_station_2024",
        ],
        "省级名录列名为大智门火车站候车厅并注明2001年列入第五批全国重点文物保护单位；武汉市政府资料确认车站始建于1903年、承载早期铁路运输和城市变迁。本条按铁路站房及其工运/城市记忆记录，具体保护范围和构成项仍需核验。",
        ev(
            "大智门火车站站房、候车厅、石柱和雕花等建筑构件；站场边界、铁路附属设施和保存清单待测绘",
            "1903年早期铁路站房、列车组织、客货联运和站务技术记忆；时刻表、线路图、设备和铁路档案待补",
            "铁路街、铁路职工、汉口城市物流和车站搬迁形成的社区记忆；武汉市政府报道记录车站周边街区叙事",
            "第五批全国重点文物保护单位身份已确认；武汉市推进文物修缮和片区更新，当前开放、产权与修缮范围需按管理资料复核",
        ),
        district="江岸区",
        aliases=["大智门火车站候车厅", "大智门火车站旧址", "京汉火车站旧址"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-WUHAN-051",
        "顺丰茶栈旧址",
        "武汉市",
        "茶叶加工与商贸物流",
        "provincial_heritage_related",
        "第八批湖北省文物保护单位（2021）；万里茶道遗产点",
        [
            "hubei_provincial_relics_1098",
            "wuhan_8th_relics_2021",
            "wuhan_tea_trade_2019",
        ],
        "省级名录列出1901—1902年的顺丰茶栈旧址；武汉市文旅局确认其为第八批湖北省文物保护单位和万里茶道遗产点，市供销社答复补充东方茶港、青砖茶和再生式保护经营语境。本条记录茶业加工、仓储、码头物流与城市文化网络，历史设备和边界仍需核验。",
        ev(
            "顺丰茶栈旧址建筑、茶叶仓储/转运空间及与汉口码头的关系；茶砖厂房、蒸汽设备和历史码头边界待核",
            "汉口茶叶集散、青砖茶加工、仓储和水陆转运技术记忆；茶厂设备、工艺档案和产品谱系待补",
            "汉口东方茶港、俄商茶业网络、羊楼洞茶区和万里茶道共同形成的商贸与社区记忆；市级资料已确认公共文化利用语境",
            "第八批省级文保和万里茶道遗产点身份已确认；市级资料提到再生式保护经营，当前产权、开放和设备保存需复核",
        ),
        district="江岸区",
        aliases=["顺丰茶栈", "顺丰茶厂旧址", "顺丰砖茶厂旧址"],
        asset_kind="industrial_cultural_landscape",
    ),
]


PATCHES: dict[str, dict[str, Any]] = {
    "HBI-WUHAN-003": {
        "district_county": "江岸区",
        "recognition_level": "national_cultural_relic_related",
        "recognition_status": "第八批全国重点文物保护单位（并入第六批汉口近代建筑群）；武汉市首批工业遗产一级",
        "source_keys": ["hubei_national_relics_1_8_2023", "wuhan_lamp_history_2020"],
        "aliases": ["汉口英商电灯公司旧址", "汉口电灯公司旧址"],
        "asset_kind": "industrial_site",
        "notes": "汉口电灯公司与省级名录、国保名录中的汉口英商电灯公司旧址为同一近代电力照明遗存；武汉市发改委资料确认1906年英商创办公司并开始安装路灯，补足电力技术和城市照明社会记忆。旧址建筑、设备和保护范围仍需现场核验。",
        "cultural_evidence": ev(
            "汉口英商电灯公司旧址建筑、早期电力照明设施及城市路灯关联空间；发电设备、线路和建筑构件待核",
            "1906年英商电灯公司创办、路灯安装和近代城市照明系统；发电机组、配电线路、技术人员和档案待补",
            "武汉街道由油灯进入电灯时代的城市生活记忆，江岸租界居民和路灯使用者的社会经验；官方报道记录历史地点与路灯叙事",
            "国保名录确认并入汉口近代建筑群；旧址现状、开放方式、产权和保护工程需以最新管理资料复核",
        ),
    },
    "HBI-WUHAN-012": {
        "district_county": "江岸区",
        "recognition_level": "provincial_heritage_related",
        "recognition_status": "湖北省省级文物保护单位名录（1098处）；武汉市首批工业遗产一级",
        "source_keys": ["hubei_provincial_relics_1098"],
        "aliases": ["亚细亚火油公司汉口分公司旧址"],
        "asset_kind": "industrial_site",
        "notes": "省级名录逐项列出亚细亚火油公司汉口分公司旧址；本条保留武汉首批工业遗产名录中的简名并补入官方文保全名。该对象属于近代石油储运、销售和商贸建筑遗存，具体油库/码头关联、建筑构成和现状需专项核验。",
        "cultural_evidence": ev(
            "亚细亚火油公司汉口分公司旧址建筑及沿江商贸空间；储油、装卸、广告和码头设施关联待核",
            "近代煤油进口、储运、销售和城市燃料供应技术记忆；油罐、运输工具、经营档案和产品谱系待补",
            "汉口沿江油品贸易、煤油消费和近代商贸网络的城市记忆；公司职工、买办和周边社区口述史待补",
            "省级名录和武汉工业遗产语境已确认；保护范围、产权、开放方式和设备遗存需按最新资料复核",
        ),
    },
    "HBI-PROV-002": {
        "recognition_level": "provincial_heritage_related",
        "recognition_status": "湖北省省级文物保护单位名录（宜都红茶厂旧址）；中国工业遗产保护名录第二批；2025年度湖北省工业遗产拟认定对象",
        "source_keys": ["hubei_provincial_relics_1098", "hubei_red_tea_cultural_2022"],
        "aliases": ["宜都红茶厂旧址", "宜红茶厂旧址"],
        "asset_kind": "industrial_cultural_landscape",
        "notes": "省级名录和省文旅厅报道确认宜都红茶厂（旧址）为1951年建成的茶叶生产遗存，保留完整木结构生产线及风选机、平圆筛等设备，并入选中国工业遗产保护名录第二批；2025年度省级工业遗产公示为另一个认定语境，二者均保留并明确状态。档案和茶旅展示资料丰富，厂址边界与当前开放仍需复核。",
        "cultural_evidence": ev(
            "1951年宜都红茶厂完整木结构茶叶生产线、风选机、平圆筛等十余台设备，以及湖北省档案馆、宜都市档案馆相关档案；设备清单和厂区边界待测绘",
            "宜红茶收购、精制、自动化筛分和生产组织技术；完整生产线和档案可支撑工艺复原，设备运行状态与工序关系待现场核验",
            "宜红茶品牌、宜都茶港、茶叶工人和万里茶道共同构成地方产业记忆；省文旅厅报道记录档案整理、茶旅线路和宜红茶博物馆筹办",
            "中国工业遗产保护名录第二批和省级文保名录语境已确认；报道提到茶旅展示和博物馆筹办，产权、开放时段和完整保护范围需复核",
        ),
    },
    "HBI-YC-005": {
        "notes": "宜昌市政府报道确认精制茶厂精制车间、宜红茶工业遗产展示馆和非遗展示利用；省级名录另登记宜都市另一处茶厂遗产，二者为不同县市对象。",
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
        f"wave_i_records={len(NEW_RECORDS)} wave_i_sources={len(NEW_SOURCES)} "
        f"patched_records={len(PATCHES)} total_records={len(records)} total_sources={len(sources)}"
    )


if __name__ == "__main__":
    main()
