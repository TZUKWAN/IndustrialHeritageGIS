from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "hubei_makou_kiln_2017": {
        "source_type": "government_policy_reply",
        "title": "对省十二届人大五次会议第2017546号建议的答复",
        "org": "湖北省文化和旅游厅",
        "pub_date": "2017-07-05",
        "url": "https://wlt.hubei.gov.cn/zfxxgk/fdzdgknr/qtzdgknr/jytabl/rddbjy/202008/t20200805_2742104.shtml",
        "authority": "A",
        "notes": "省文旅厅答复确认马口窑址2008年列入第五批湖北省文物保护单位，并确认马口陶器烧制技艺2011年列入第三批湖北省非物质文化遗产名录；同时提到器物、民间工艺、商业交通和文化特色保护传承。",
    },
    "hubei_makou_craft_2022": {
        "source_type": "official_cultural_media",
        "title": "湖北非遗文创设计比赛：陶器烧制技艺",
        "org": "湖北省非物质文化遗产保护中心/湖北省文化和旅游厅",
        "pub_date": "2022-04-07",
        "url": "https://wlt.hubei.gov.cn/hbsfwzwhycw/mtgz/xwdt/202204/t20220406_4070570.shtml",
        "authority": "A",
        "notes": "省级非遗专题资料将汉川马口镇列为陶器烧制技艺分布地，介绍当地黄粘土原料、耐腐蚀不渗漏的器物特征及明清以来的历史线索；具体窑址和传承人仍需专项调查。",
    },
    "hubei_bailuo_airport_2025": {
        "source_type": "government_procuratorate",
        "title": "荆州：守护旷野中的沉默“证人”",
        "org": "湖北省人民检察院",
        "pub_date": "2025-09-15",
        "url": "https://www.hbjc.gov.cn/ejxw/gddt/202509/t20250915_1868269.shtml",
        "authority": "A",
        "notes": "省检察院实地保护监督报道确认1940年日军在监利白螺修建军用机场，记载现存碉堡、地堡、暗堡和蓄水池数量，并说明保护修缮工程已获湖北省文化和旅游厅批复同意立项。",
    },
    "hubei_salt_route_2021": {
        "source_type": "government_investment_profile",
        "title": "省文化和旅游厅关于印发2021年全省文化和旅游及康养产业招商引资工作方案的通知",
        "org": "湖北省文化和旅游厅",
        "pub_date": "2021-01-05",
        "url": "https://wlt.hubei.gov.cn/zfxxgk/fdzdgknr/zdjsxm/202201/t20220105_3952430.shtml",
        "authority": "A",
        "notes": "省文旅厅项目资料确认虎牙山盐运纤道为省级文物点，说明其与古战场景区、宜昌沿江交通和公共教育/研学利用的关系。",
    },
    "hubei_wanli_tea_2018": {
        "source_type": "government_policy_reply",
        "title": "关于湖北省政协十二届一次会议第20180358号提案的答复",
        "org": "湖北省文化和旅游厅",
        "pub_date": "2019-08-16",
        "url": "https://wlt.hubei.gov.cn/zfxxgk/fdzdgknr/qtzdgknr/jytabl/zxwyta/202008/t20200805_2742256.shtml",
        "authority": "A",
        "notes": "省文旅厅答复把五峰古茶道纳入万里茶道中国世界文化遗产预备名单项目，并确认五峰古茶道汉阳桥段、五峰采花茶园、五峰精制茶厂等申遗推荐点及档案支持。",
    },
    "hubei_wanli_tea_overview_2020": {
        "source_type": "government_feature",
        "title": "再识万里茶道（看·世界遗产）",
        "org": "湖北省文化和旅游厅",
        "pub_date": "2020-11-25",
        "url": "https://wlt.hubei.gov.cn/bmdt/xydt/202011/t20201125_3052105.shtml",
        "authority": "A",
        "notes": "省文旅厅专题介绍万里茶道中国段的工厂、古道、码头、关隘、城镇和水陆转运体系，作为湖北茶业生产、加工与贸易文化景观的宏观交叉来源。",
    },
    "hubei_8th_relics_2021": {
        "source_type": "government_register",
        "title": "湖北省人民政府关于公布第八批湖北省文物保护单位的通知",
        "org": "湖北省人民政府",
        "pub_date": "2021-12-09",
        "url": "https://www.hubei.gov.cn/xxgk/gb/202201/W020220128589044239800.pdf",
        "authority": "A",
        "notes": "省政府公报公布第八批省级文物保护单位，列出孝感城隍潭码头遗址及其明清年代和孝南区所在地；保护范围与建设控制地带另有后续公报。",
    },
    "hubei_chenghuang_boundary_2024": {
        "source_type": "government_protection_notice",
        "title": "湖北省人民政府办公厅关于公布第八批湖北省文物保护单位保护范围和建设控制地带的通知",
        "org": "湖北省人民政府办公厅",
        "pub_date": "2024-04-01",
        "url": "https://www.hubei.gov.cn/xxgk/gb/202404/W020240412574567775024.pdf",
        "authority": "A",
        "notes": "省政府公报明确城隍潭码头遗址保护范围以环城路、老码头石矶、新建观景栈道和城隍潭桥等为界，并给出建设控制地带方向，用于补足空间边界证据。",
    },
    "xiaogan_chenghuang_2022": {
        "source_type": "official_media",
        "title": "孝感老澴河畔 一批古迹重见天日焕发新的生机——城隍潭码头遗址催放新芳华",
        "org": "湖北日报/荆楚网",
        "pub_date": "2022-01-25",
        "url": "https://news.cnhubei.com/content/2022-01/25/content_14442968.html",
        "authority": "B",
        "notes": "湖北日报报道记录2020年省文物考古研究所与孝感市博物馆发掘城隍潭码头，说明其为明清交通枢纽、长江流域较早且规模较大的古码头，并记录保护利用工程与老麻糖厂等城市工业记忆的关联。",
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
        "HBI-XG-011",
        "马口窑址",
        "孝感市",
        "古代陶瓷制造与传统制陶技艺",
        "provincial_heritage_related",
        "第五批湖北省文物保护单位（2008）；马口陶器烧制技艺列入第三批湖北省非物质文化遗产（2011）",
        ["hubei_provincial_relics_1098", "hubei_makou_kiln_2017", "hubei_makou_craft_2022"],
        "省级名录和省文旅厅资料确认马口窑址位于孝感市汉川市马口镇，窑址与马口陶器烧制技艺构成同一地方生产文化系统；本条把遗址、器物、原料、技艺和商业交通分层记录，不把非遗项目等同于文物本体。",
        ev(
            "马口窑址、黄粘土原料、传统陶器和可能关联的窑炉/作坊；具体窑址边界、窑炉数量、遗物和现状保存需考古与现场测绘",
            "明清以来马口陶器烧制、黄粘土取料、成型和烧造技术；省级非遗资料确认器物耐腐蚀、不渗漏等工艺特征，完整流程和工具谱系待补",
            "马口窑器物的地域识别、民间工艺传承、跨区域商业交通和汉川社区生产记忆；传承人、作坊网络和口述史待补证",
            "省级文保身份与省级非遗身份已由官方资料确认；专题博物馆、窑址展示、产权和现存生产空间需按最新资料复核",
        ),
        district="汉川市",
        aliases=["马口窑", "系马陶窑址", "汉川马口窑址"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-ES-009",
        "箭竹坪手工榨油坊",
        "恩施州",
        "传统油料加工",
        "provincial_heritage_related",
        "湖北省省级文物保护单位名录列名（民国）",
        ["hubei_provincial_relics_1098"],
        "湖北省省级文物保护单位公布名录列出宣恩县箭竹坪手工榨油坊，年代为民国；目前仅以名录确认名称、年代和行政区，传统榨油设备、作坊布局、生产连续性与保护现状待地方档案和现场核验。",
        ev(
            "手工榨油坊建筑、榨油设备、油料仓储和作坊空间；省级名录未列具体构件，现存本体和边界待测绘",
            "民国时期传统油料破碎、蒸煮、压榨和储运技术线索；榨具、燃料、原料与产品谱系待补证",
            "宣恩山地油料加工、榨油匠人和村落交换网络的地方生产记忆；人物、组织与口述史待补",
            "省级文保名录身份和民国年代已确认；保存、产权、利用、开放与风险信息待核",
        ),
        district="宣恩县",
        aliases=["箭竹坪油坊", "箭竹坪传统榨油坊"],
        asset_kind="industrial_site",
    ),
    rec(
        "HBI-JZ-012",
        "白螺机场遗址",
        "荆州市",
        "战时航空基础设施",
        "provincial_heritage_related",
        "第五批湖北省文物保护单位（2008）；省级名录列名（1940—1945）",
        ["hubei_provincial_relics_1098", "hubei_bailuo_airport_2025"],
        "省级名录确认白螺机场为1940—1945年近现代重要史迹，省检察院2025年保护监督报道进一步确认机场遗址现存碉堡、地堡、暗堡和蓄水池，并记录保护修缮工程已获批立项；报道对机场始建和扩建年份有更细分叙述，本条保留名录年代并标注时间差异。",
        ev(
            "机场场地及残存1座碉堡、3座地堡、2座暗堡和1处蓄水池等军事工程遗存；机场跑道、机库和保护边界大部已损失或待核",
            "战时机场选址、跑道施工、飞机停泊、燃料补给和防御工事构成航空基础设施技术记忆；设备、机库和工程档案待补",
            "日军占领、强征民夫、抗日自卫队袭扰与飞虎队/中国空军活动形成抗战与地方社会记忆；受害者、见证者和口述史需规范采集",
            "省级文保身份与现存构筑物由官方资料确认；湖北省文旅厅已批复保护修缮工程立项，具体工程、开放和安全边界待跟踪",
        ),
        district="监利市",
        aliases=["白螺飞机场遗址", "白螺矶机场遗址", "监利白螺机场"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-YC-013",
        "虎牙山盐运纤道",
        "宜昌市",
        "盐运交通与水运工程",
        "provincial_heritage_related",
        "湖北省省级文物保护单位名录列名（清）",
        ["hubei_provincial_relics_1098", "hubei_salt_route_2021"],
        "省级名录列出猇亭区虎牙山盐运纤道，省文旅厅项目资料确认其为省级文物点并纳入古战场景区、研学和沿江文化旅游利用；本条按盐运、水运和人工纤运基础设施记录，具体石阶、路基和岸线范围待测绘。",
        ev(
            "沿江山体纤道、石阶、路基、岸线节点和相关碑刻；省级名录与项目资料未给出完整构筑物清单，保护范围待复核",
            "清代盐货沿长江水运并由纤夫牵引船只通过险段的交通技术与组织方式；船具、码头和运盐线路档案待补",
            "盐商、船工、纤夫、沿江村落与宜昌盐运贸易形成的劳动和商贸记忆；地方志、口述史和路线节点待补证",
            "省级文物点身份已确认，并作为景区主轴和研学资源利用；日常维护、开放强度和岸线安全需按管理资料复核",
        ),
        district="猇亭区",
        aliases=["虎牙山古盐运道", "虎牙滩盐运纤道"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-YC-014",
        "万里茶道五峰段",
        "宜昌市",
        "茶业生产与贸易交通",
        "cultural_landscape_related",
        "湖北省省级文物保护单位名录列名；万里茶道中国世界文化遗产预备名单湖北段节点",
        ["hubei_provincial_relics_1098", "hubei_wanli_tea_2018", "hubei_wanli_tea_overview_2020"],
        "省级名录列出万里茶道五峰段，省文旅厅答复确认五峰古茶道纳入中国世界文化遗产预备名单项目并列出汉阳桥段、采花茶园、五峰精制茶厂等推荐点；本条作为线路型工业文化景观，不把整条线路误称为单一工厂遗址。",
        ev(
            "古道、桥梁、茶园、村落、茶厂、码头和沿线水陆转运节点；推荐点清单和线路保护边界需按申遗文本与地方测绘复核",
            "茶叶采摘、初制、精制、包装、驮运和水陆转运构成跨区域生产链；省文旅厅专题资料确认工厂、古道、码头与转运体系，设备谱系待补",
            "茶农、茶商、挑夫、船工、村落和跨省贸易网络形成的地方社会记忆；档案馆茶麻公司档案和口述史可继续补证",
            "已纳入万里茶道预备名单项目语境并开展推荐点保护利用；线路分段产权、开放路线和现状风险需按最新规划复核",
        ),
        district="五峰土家族自治县",
        aliases=["五峰古茶道", "万里茶道湖北段五峰节点"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-YC-015",
        "五峰采花茶园",
        "宜昌市",
        "茶业种植与原料生产",
        "research_candidate",
        "万里茶道五峰段申遗推荐点（省文旅厅提案答复）",
        ["hubei_wanli_tea_2018"],
        "省文旅厅提案答复把五峰采花茶园列为万里茶道申遗推荐点；本条只确认官方推荐点身份和茶业原料生产关联，不将推荐点直接升格为文物保护单位，茶园年代、传统管理、构筑物和保护边界待专题调查。",
        ev(
            "茶园梯田、茶树群落、田间道路、水土保持和可能的初制设施；具体地块边界与历史层积待测绘",
            "采摘、萎凋、揉捻、初制及向五峰精制茶厂供料的生产链线索；设备、工艺谱系和历史产量待档案补证",
            "采花地区茶农、村落、茶商和万里茶道贸易网络的生产记忆；人物、组织和口述史待补",
            "官方资料确认其为申遗推荐点；现状茶园经营、展示、产权和保护管理需地方资料复核",
        ),
        district="五峰土家族自治县",
        aliases=["采花茶园", "五峰采花古茶园"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-ES-010",
        "伍家台贡茶园",
        "恩施州",
        "茶业种植与传统茶文化景观",
        "provincial_heritage_related",
        "湖北省省级文物保护单位名录列名（清）",
        ["hubei_provincial_relics_1098", "hubei_wanli_tea_overview_2020"],
        "湖北省省级文物保护单位名录列出宣恩县伍家台贡茶园，年代为清；本条按茶叶原料、传统园地和茶文化景观记录，现存茶树、道路、水利、加工空间和保护边界待现场及地方志核验。",
        ev(
            "清代贡茶园、茶树群落、山地道路和可能关联的制茶/仓储空间；名录未列具体本体，范围与保存状况待核",
            "贡茶采摘、初制、包装与运输的技术线索；具体品种、工艺、工具和供应组织待补",
            "宣恩茶农、贡茶贸易、土家族村落和茶叶消费形成的地方社会记忆；口述史和茶业档案待补",
            "省级文保名录身份已确认；现行茶园经营、展示利用和保护责任主体待地方资料复核",
        ),
        district="宣恩县",
        aliases=["伍家台贡茶园遗址", "伍家台古茶园"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-ES-011",
        "万里茶道鹤峰段",
        "恩施州",
        "茶业生产与贸易交通",
        "cultural_landscape_related",
        "湖北省省级文物保护单位名录列名；万里茶道湖北段节点",
        ["hubei_provincial_relics_1098", "hubei_wanli_tea_overview_2020"],
        "省级名录列出万里茶道鹤峰段，所在地为恩施州鹤峰县；省文旅厅专题资料确认万里茶道包含工厂、古道、码头、城镇和水陆转运系统。本条按线路型茶业工业文化景观记录，鹤峰段节点清单和保护边界待申遗档案核验。",
        ev(
            "古道、茶园、村落、驿运节点、码头和可能的茶叶加工空间；省级名录只确认线路名称与行政区，组成项待调查",
            "茶叶采制、山地运输、船运与长距离贸易的综合技术线索；鹤峰段具体工厂、工具和路线档案待补",
            "茶农、茶商、挑夫、船工和沿线村落共同形成的茶业社会记忆；地方志、商号档案和口述史待补",
            "省级名录身份和万里茶道文化线路语境已确认；现状经营、展示、产权与风险待地方规划复核",
        ),
        district="鹤峰县",
        aliases=["万里茶道（鹤峰段）", "鹤峰古茶道"],
        asset_kind="industrial_cultural_landscape",
    ),
]


PATCHES: dict[str, dict[str, Any]] = {
    "HBI-XG-010": {
        "industry_category_l1": "历史水运、码头与城市商贸",
        "recognition_status": "第八批湖北省文物保护单位（2021）；明清古遗址",
        "source_keys": [
            "hubei_8th_relics_2021",
            "hubei_chenghuang_boundary_2024",
            "xiaogan_chenghuang_2022",
        ],
        "aliases": [
            "城隍潭码头旧址",
            "孝感城隍潭码头",
            "城隍潭码头遗址",
            "城隍潭老码头",
            "孝感城隍潭码头遗址",
            "老澴河城隍潭码头",
        ],
        "asset_kind": "industrial_cultural_landscape",
        "notes": "省政府公报确认孝南区城隍潭码头遗址为第八批省级文物保护单位，后续公报明确保护范围和建设控制地带；湖北日报报道记录2020年考古发掘、明清交通枢纽功能和保护利用工程。本条合并名录简名与考古报道名称，作为水运基础设施与城市工业文化景观纳入底册。",
        "cultural_evidence": ev(
            "老澴河石砌码头、石矶、石阶、车辙印痕、驳岸和周边水陆衔接空间；省政府公报已给出保护范围方向，细部遗存待测绘",
            "明清船只停靠、货物装卸、驳运和河道交通组织技术；考古出土、修缮工艺和相关船厂/仓储谱系待补",
            "孝感老城商贾、船队、挑夫、麻糖米酒等地方产业与城隍潭码头相互塑造的城市记忆；商号、船队和口述史可继续补证",
            "省级文保身份、保护范围和考古发掘已确认；遗址公园、展示工程、岸线安全和开放管理需按最新资料复核",
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
    # The first draft of this wave created a second canonical row for the
    # already-tracked 城隍潭码头. Merge that draft into HBI-XG-010 before the
    # normal idempotent insertion path so reruns repair the same JSON source.
    legacy = existing_by_id.get("HBI-XG-012")
    target = existing_by_id.get("HBI-XG-010")
    if legacy is not None and target is not None:
        merge_unique(target, "source_keys", legacy.get("source_keys") or [])
        merge_unique(target, "aliases", legacy.get("aliases") or [])
        records[:] = [row for row in records if row.get("inventory_id") != "HBI-XG-012"]
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
        f"wave_k_records={len(NEW_RECORDS)} wave_k_sources={len(NEW_SOURCES)} "
        f"patched_records={len(PATCHES)} total_records={len(records)} total_sources={len(sources)}"
    )


if __name__ == "__main__":
    main()
