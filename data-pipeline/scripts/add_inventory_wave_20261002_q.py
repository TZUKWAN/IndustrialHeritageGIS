from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "enrichment" / "hubei_inventory.json"
PROFILES_PATH = ROOT / "enrichment" / "hubei_cultural_profiles.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "hubei_first_provincial_heritage_2024": {
        "source_type": "central_media_provincial_list_report",
        "title": "湖北首批工业遗产出炉",
        "org": "央广网（来源：湖北日报）",
        "pub_date": "2024-03-13",
        "url": "https://www.cnr.cn/hubei/yw/20240313/t20240313_526625221.shtml",
        "authority": "B",
        "notes": "央广网转载湖北日报报道，引用湖北省经信厅消息确认湖北首批省级工业遗产共9家（单位），明确列出五峰归真集团五峰茶叶有限责任公司等项目；名单对象和详细价值仍按省级申报材料及各地补充来源拆分核验。",
    },
    "wufeng_caohua_digital_museum": {
        "source_type": "ministry_digital_museum",
        "title": "采花-老字号数字博物馆",
        "org": "中华人民共和国商务部老字号数字博物馆",
        "pub_date": "2024-02-01",
        "url": "https://lzhbwg.mofcom.gov.cn/edi_ecms_web_front/thb/detail/8fda263bf7c740b2b760a1e4b67a9737",
        "authority": "A",
        "notes": "商务部主办数字博物馆页面记录湖北采花茶业及其前身五峰中心茶站（1951年）、1990年国营茶厂、厂房与设备、采花毛尖及宜红茶工艺、非遗传承人、湖北茶博馆和现状科技园；页面是品牌/企业文化档案，不替代五峰归真集团省级工业遗产核心物项边界。",
    },
    "xiangyang_first_provincial_heritage_2024": {
        "source_type": "provincial_media_industrial_heritage_feature",
        "title": "襄阳工业遗产焕新再出发",
        "org": "湖北日报数字报",
        "pub_date": "2024-04-22",
        "url": "https://epaper.hubeidaily.net/pc/content/202404/22/content_271331.html",
        "authority": "B",
        "notes": "湖北日报专题报道引用襄阳市经信局，确认首批省级工业遗产中襄阳有老河口光化特酒业、湖北金环新材料、国营红星化工机械厂3家；分述光化特1952—1954年沿革、北京路旧厂区建筑/古窖池/酒精精馏塔，红星厂1966年及航天四十二所旧址，湖北化纤厂1972年投产和三线配套背景，并记录保护利用现状。",
    },
    "xiangyang_redstar_history_2024": {
        "source_type": "provincial_media_industrial_heritage_report",
        "title": "湖北首批工业遗产名单公布 谷城一地上榜",
        "org": "湖北日报新闻客户端",
        "pub_date": "2024-03-06",
        "url": "https://news.hubeidaily.net/pc/c_2326158.html",
        "authority": "B",
        "notes": "湖北日报报道确认谷城国营红星化工机械厂旧址位于庙滩镇郭峪村，1966年由中国科学院大连化学物理研究所建设、后由航天四院接管，形成复合固体推进剂研究和三线红色教育记忆；涉密物项和开放边界仍待核验。",
    },
    "jianmin_digital_museum": {
        "source_type": "ministry_digital_museum",
        "title": "健民-老字号数字博物馆",
        "org": "中华人民共和国商务部老字号数字博物馆",
        "pub_date": "2024-02-01",
        "url": "https://lzhbwg.mofcom.gov.cn/edi_ecms_web_front/thb/detail/a0cabda94eeb47328cb399db11f2d822",
        "authority": "A",
        "notes": "商务部主办老字号数字博物馆健民页面，用于补充武汉市健民制药厂现行品牌、老字号/非遗传承、叶开泰文化和企业展示利用的公开证据；不替代国家工业遗产核心物项清单，也不推断厂区全部开放。",
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
        "HBI-YC-016",
        "五峰归真集团五峰茶叶有限责任公司（采花茶业）",
        "宜昌市",
        "五峰土家族自治县",
        "茶叶加工工业",
        "provincial",
        "湖北省首批省级工业遗产",
        ["hubei_first_provincial_heritage_2024", "wufeng_caohua_digital_museum"],
        "央广网转载湖北日报并引用省经信厅消息，确认五峰归真集团五峰茶叶有限责任公司为湖北首批省级工业遗产项目。商务部老字号数字博物馆记录其前身五峰中心茶站1951年建立、1990年转为国营茶厂，后形成采花茶业科技园和茶博馆；本条保留‘五峰归真集团’名录名称与现企业谱系，未将采花科技园、五峰精制茶厂或采花茶园直接合并为同一遗产边界，具体核心物项、原厂址和申报单位沿革待档案核验。",
        ev(
            "1951年五峰中心茶站、1990年国营茶厂的厂房与机械设备（商务部页面记载6000平方米厂房、80余套设备），以及后续茶博馆和科技园展示空间；与现存五峰精制茶厂旧址的同址关系待核",
            "采花毛尖传统制作技艺、宜红工夫茶加工、现代自动摊青/微波杀青/智能揉捻/连续做形生产线；商务部页面记载十二道重要工艺、27道工序和传承人谱系",
            "五峰茶乡、宜红茶外销、茶工与土家族社区记忆，采花毛尖湖北省非遗制作技艺和茶博馆公共展示共同构成工业文化传播入口",
            "湖北采花茶业持续经营，科技园、湖北茶博馆、茶旅路线和2024年升级改造计划均有商务部页面记录；省级工业遗产核心物项、开放制度与保护边界待核",
        ),
        aliases=["五峰归真集团五峰茶业有限责任公司", "五峰茶叶有限责任公司", "五峰中心茶站", "采花茶业"],
        asset_kind="industrial_cultural_landscape",
    ),
    rec(
        "HBI-XIANGYANG-027",
        "老河口光化特酒业有限公司",
        "襄阳市",
        "老河口市",
        "酿酒工业",
        "provincial",
        "湖北省首批省级工业遗产",
        ["xiangyang_first_provincial_heritage_2024"],
        "湖北日报专题报道引用襄阳市经信局，确认老河口光化特酒业有限公司为湖北首批省级工业遗产项目。北京路厂区外墙记录1952年组建光化县老河口酒厂、1953—1954年定名地方国营酒厂的沿革，红砖筒子楼、烟囱、古窖池和酒精精馏塔等工业载体仍具可识别性；保护范围、设备清单和档案全宗待现场及企业资料核验。",
        ev(
            "老河口市北京路旧厂区红砖筒子楼、烟囱、古窖池、酒精精馏塔、手工酿酒工坊和酒文化博物馆等；具体建筑编号和设备年代待测绘",
            "地方国营白酒生产、古窖池固态发酵、起窖拌料—上甑蒸馏—量质摘酒—入窖发酵—勾兑储存等工艺，以及1974年省轻工局调拨年产1500吨酒精精馏塔的工程记忆",
            "光化县/老河口地方酒业、几代光化特职工和白酒消费者形成的城市产业记忆；旧厂区外墙、游客打卡和酒文化展陈提供公共记忆入口",
            "公司在2013年后对化城门厂区进行保护性改造，形成光化艺术社区、手工酿酒工坊、酒文化博物馆和展览空间；老厂区产权、开放时段和核心物项保护责任待核",
        ),
        aliases=["光化特酒业", "光化特酒厂", "老河口地方国营酒厂", "光化县老河口酒厂"],
        asset_kind="industrial_cultural_landscape",
    ),
]


def merge_unique(row: dict[str, Any], key: str, values: list[str]) -> None:
    existing = row.setdefault(key, [])
    for value in values:
        if value not in existing:
            existing.append(value)


def patch_record(row: dict[str, Any], *, source_keys: list[str], aliases: list[str], evidence: dict[str, str], notes: str, level: str | None = None, status: str | None = None) -> None:
    merge_unique(row, "source_keys", source_keys)
    merge_unique(row, "aliases", aliases)
    row["cultural_evidence"] = evidence
    row["notes"] = notes
    if level is not None:
        row["recognition_level"] = level
    if status is not None:
        row["recognition_status"] = status
    row["record_status"] = "source_confirmed"


def patch_jianmin_profile() -> None:
    data = json.loads(PROFILES_PATH.read_text(encoding="utf-8"))
    profile = data["profiles"]["HER-4c71d600d918"]
    sid = "src-web-cb5dc409c2"
    merge_unique(profile, "source_ids", [sid])
    for dim in profile["cultural_dimensions"]:
        merge_unique(dim, "source_ids", [sid])
        if dim["key"] == "technology":
            dim["text"] = "原料仓库、制剂与糖浆车间、产品药方及生产工艺资料共同构成中药生产技术和配方传承的证据链；商务部老字号数字博物馆补充健民品牌、叶开泰文化和现行传承展示。"
        elif dim["key"] == "organization":
            dim["text"] = "“叶开泰”历史人物文献、公司制度档案和三大品牌商标资料为企业组织与老字号谱系研究提供入口；商务部页面确认健民老字号、非遗传承与企业文化展示。"
        elif dim["key"] == "memory":
            dim["text"] = "叶开泰、健民和龙牡品牌及相关产品构成武汉医药工业与城市日常健康记忆的公共入口；商务部老字号页面补充企业品牌沿革和叶开泰文化，具体口述史仍待补证。"
        elif dim["key"] == "continuity":
            dim["text"] = "商务部老字号数字博物馆记录健民品牌现行传承、叶开泰文化展示和企业持续经营，为保护利用连续性提供公开证据；国家工业遗产核心物项的现状开放范围仍待企业和现场核验。"
            dim["evidence_type"] = "documented_current_use_and_brand_continuity"
            dim["evidence_level"] = "A"
    profile["current_use_status"] = "documented"
    profile["limitations"] = "商务部页面补充了现行品牌、非遗传承和文化展示证据；仍需补充叶开泰历史档案、配方与工艺授权边界、厂区核心物项现状和公众开放信息。"
    PROFILES_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


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
        existing_by_id["HBI-XIANGYANG-002"],
        source_keys=["xiangyang_first_provincial_heritage_2024", "xiangyang_redstar_history_2024"],
        aliases=["国营红星化工机械厂旧址", "航天四院四十二所旧址"],
        level="provincial",
        status="湖北省首批省级工业遗产",
        notes="湖北日报两篇报道确认谷城国营红星化工机械厂（航天四十二所旧址）为湖北首批省级工业遗产，位于庙滩镇郭峪村，1966年起由中科院大连化学物理研究所建设、后由航天四院接管；专题报道记录约7公里遗址分布、工房、红星子弟学校、干打垒旧址、烈士牺牲地、老设备展陈和红色教育利用。涉密核心物项、产权边界和公众开放范围仍待核验。",
        evidence=ev(
            "郭峪村约7公里范围内的工房、红星子弟学校、干打垒旧址、烈士牺牲地、文化墙和航天旧址展陈物；具体保护线、涉密设施和建筑编号待测绘",
            "1966年建设、复合固体推进剂研究、火箭发动机与推进剂技术组织及三线军工科研生产；专题报道还记录神舟火箭模型、大气采样器、老砝码和老式电话等展陈物",
            "三线建设工程技术人员、航天四十二所科研人员、职工家属和郭峪村红色教育形成的地方社会记忆；英雄人物与奉献精神需按公开资料边界表述",
            "郭峪村投入资金修复损毁建筑并设立旅游标志，原招待所改为教育展厅，航天四十二所与庙滩镇规划三线文化展区和科普体验馆；涉密开放边界与长期保护责任待核",
        ),
    )
    patch_record(
        existing_by_id["HBI-XIANGYANG-011"],
        source_keys=["xiangyang_first_provincial_heritage_2024"],
        aliases=["湖北化纤厂旧址", "湖北金环新材料科技有限公司原厂区", "十里化纤城"],
        level="provincial",
        status="湖北省首批省级工业遗产",
        notes="湖北日报专题报道确认湖北金环新材料科技有限公司（原湖北化纤厂）为湖北首批省级工业遗产，1968年动工、1972年投产，承担三线建设时期为东风轮胎厂配套生产工业用粘胶强力丝帘子布的任务；专题同时记录十里化纤城厂区风貌和影视取景。现存厂房、设备、档案和保护范围待企业与现场核验。",
        evidence=ev(
            "原湖北化纤厂及十里化纤城的厂房、烟囱、生产生活空间和影视取景形成的工业景观；具体保留建筑和设备目录待测绘",
            "1968年动工、1972年投产，工业用粘胶强力丝帘子布生产及为东风轮胎厂配套的化纤工程技术；完整工艺流程与设备谱系待补",
            "三线建设时期化纤工人、下班工装人流和襄阳—东风产业配套形成的城市工业记忆；职工口述史与社区档案待补",
            "现企业继续经营，旧厂区部分空间被用于城市记忆和影视拍摄；省级工业遗产核心物项、厂区开放与更新边界待核",
        ),
    )
    data.setdefault("research_targets", {})["coverage_sources"] = [
        "hubei_industrial_survey_2019",
        "hubei_industrial_management_draft_2024",
    ]
    data["research_targets"]["coverage_rule"] = (
        "每条对象至少绑定名录/普查/规划/企业史/档案遗产或来源确认资料；"
        "工业遗产实体、工业文化景观、工业金融与贸易节点、工业旅游相关场景、档案文献和待核验线索分层记录。"
        "省级摸底和管理办法征求意见稿只作为范围、字段和分级依据，不替代具体对象的名录或现场证据；"
        "古代窑业、矿冶、铸钱与史前纺织遗址仅在来源明确出现生产性证据时纳入，并保留考古候选或相关层级；"
        "文化证据字段只记录来源中明确出现的载体、技术、社会记忆和利用状态，未核实内容保持待核。"
    )
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    patch_jianmin_profile()
    print(
        f"wave_q_sources={len(NEW_SOURCES)} added_records={len(NEW_RECORDS)} "
        f"total_records={len(records)} total_sources={len(sources)} profiles_patched=1"
    )


if __name__ == "__main__":
    main()
