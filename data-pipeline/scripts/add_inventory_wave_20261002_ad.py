from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "enrichment" / "hubei_inventory.json"


NEW_SOURCES: dict[str, dict[str, Any]] = {
    "yangxin_futu_industry_2024": {
        "source_type": "provincial_industry_government_media",
        "title": "盘活闲置用地和厂房 浮屠镇建起新材料产业园",
        "org": "湖北省经济和信息化厅/湖北日报",
        "pub_date": "2024-07-16",
        "url": "https://jxt.hubei.gov.cn/bmdt/cyfz/202407/t20240716_5269412.shtml",
        "authority": "A",
        "notes": "省经信厅转载湖北日报报道，明确阳新县浮屠镇20世纪60年代以铝材、纺织等传统工业起家，老工业园区曾聚集老铝厂、山下工业园、麻纺厂等厂房，后因产业迁移闲置；现原老铝厂部分用地改造为新材料项目。用于确认工业文化景观和再利用沿革，不替代厂区测绘、产权和法定遗产认定。",
    },
    "yangxin_futu_gov_2024": {
        "source_type": "county_government_media",
        "title": "浮屠镇：工农融合新发展 乡村振兴有‘出路’",
        "org": "阳新县人民政府/黄石日报",
        "pub_date": "2024-11-12",
        "url": "https://www.yx.gov.cn/xwdt/tpxw/202412/t20241227_1178819.html",
        "authority": "A",
        "notes": "阳新县政府转载黄石日报，明确浮屠镇整合老铝厂、山下工业园、麻纺厂等老工业园区闲置用地和厂房，原老铝厂约200亩用地承接瓷釉新材料项目；用于与省经信厅报道交叉印证。",
    },
    "huangshi_steel_textile_2023": {
        "source_type": "municipal_government_media",
        "title": "3处入选国家工业遗产名录——黄石让老厂区活起来潮起来",
        "org": "黄石市住房和城市更新局/湖北日报",
        "pub_date": "2023-05-17",
        "url": "https://zjj.huangshi.gov.cn/index2019/zjdt/xydt/202305/t20230517_1014936.html",
        "authority": "A",
        "notes": "黄石市住房和城市更新局转载湖北日报，具体记载下陆区东方钢铁厂（东钢）焦化、炼铁、炼钢连铸厂房保存情况，并记载黄石纺织机械厂、湖北省拖拉机厂老厂区现状；用于补强既有对象的工业建筑、职工和城市更新证据。",
    },
    "shennongjia_logging_team_2023": {
        "source_type": "national_park_industrial_memory",
        "title": "从伐木工到护林人，守护华中屋脊的金山银山",
        "org": "神农架国家公园",
        "pub_date": "2023-09-18",
        "url": "https://www.snjnationalpark.com/hbxd/xhjs/202309/t4648451.shtml",
        "authority": "A",
        "notes": "神农架国家公园官网报道林二代许文操1980—1983年在木鱼林场断江坪队工作并参与伐木，记录林场、养路班、伐木班及工人家庭生活；当前页面抓取超时，保留官方 URL，具体队址、建筑和设备待林场档案与现场核验。",
    },
    "shennongjia_wood_mill_2022": {
        "source_type": "central_government_industrial_memory",
        "title": "湖北省神农架林区神农顶民兵接力守护北纬31度的‘绿色奇迹’",
        "org": "中华人民共和国国防部",
        "pub_date": "2022-11-02",
        "url": "https://www.mod.gov.cn/gfbw/gfdy/jt_214159/16155965.html",
        "authority": "A",
        "notes": "国防部转载《解放军报》2022年11月2日报道，明确王大志曾是林区木材厂工人，并记录神农架由开山伐木转向生态保护的历史；用于木材工业社会记忆交叉核验，不替代具体木材厂厂址和设备清单。",
    },
    "hubei_archive_catalog_1965": {
        "source_type": "provincial_archive_catalog",
        "title": "省直档案（老）开放档案目录（1965—1966）",
        "org": "湖北省档案馆",
        "pub_date": None,
        "url": "https://www.hbda.gov.cn/searchitem/207_8?page=1969",
        "authority": "A",
        "notes": "湖北省档案馆开放目录检出1965—1966年形成的多个工业和生产设施档案题名：安陆粮食储备仓库、棉花仓库、粮食加工厂、棉花轧花厂；松滋清江矿山机械厂；襄阳县建煤货场、棉花储备仓库、石油库、第三新华印刷厂；襄樊市化肥厂、棉纺织印染厂、襄阳冷冻厂；枣阳环城拖拉机站；公安县砖瓦厂等。pub_date留空以区分档案形成年度与网页发布日期；目录页面当前抓取超时，题名可核，实体存续、位置和是否纳入四普均待档案调阅与现场核验。",
    },
}


def ev(material: str, technical: str, social: str, current: str) -> dict[str, str]:
    return {
        "material_carriers": material,
        "technical_memory": technical,
        "social_memory": social,
        "current_use_or_loss": current,
    }


NEW_RECORDS: list[dict[str, Any]] = [
    {
        "inventory_id": "HBI-HS-038",
        "name": "阳新县浮屠镇老铝厂旧厂区",
        "city": "黄石市",
        "district_county": "阳新县浮屠镇（具体厂界待核）",
        "industry_category_l1": "有色金属与材料工业",
        "recognition_level": "research_candidate",
        "recognition_status": "县政府和省经信厅报道确认的三线老工业厂区；未见法定工业遗产认定",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["yangxin_futu_industry_2024", "yangxin_futu_gov_2024"],
        "cultural_evidence": ev(
            "原老铝厂厂房、闲置工业用地及老工业园区空间；公开报道确认原老铝厂约200亩用地承接新材料项目，具体建筑和设备待测绘",
            "铝材生产及三线建设时期乡镇工业组织记忆；产品、工艺、设备和生产年代待厂志、企业档案核实",
            "浮屠镇以铝材、纺织等工业起家，老铝厂与镇域就业、产业迁移和老工业镇记忆相连；工人名录、口述史和老照片待采集",
            "原厂区部分用地已改造承接瓷釉新材料项目，老厂房保留范围、产权、环境风险和剩余工业构筑物待核",
        ),
        "notes": "两篇政府来源均明确浮屠镇原老铝厂及其再利用，但没有给出完整厂界和遗产级别。本条作为工业文化景观登记，不把现有新材料企业等同于历史遗产。",
        "aliases": ["浮屠老铝厂", "阳新老铝厂", "浮屠镇原老铝厂"],
        "asset_kind": "industrial_landscape",
    },
    {
        "inventory_id": "HBI-HS-039",
        "name": "阳新县浮屠镇山下工业园旧工业片区",
        "city": "黄石市",
        "district_county": "阳新县浮屠镇（具体片区待核）",
        "industry_category_l1": "综合工业",
        "recognition_level": "research_candidate",
        "recognition_status": "政府报道确认的三线老工业园区组成片区；未见法定工业遗产认定",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["yangxin_futu_industry_2024", "yangxin_futu_gov_2024"],
        "cultural_evidence": ev(
            "山下工业园旧厂房、道路和工业用地构成的老工业片区；公开来源未给出单体清单和现存状态",
            "三线建设时期多类乡镇工业生产和厂区组织记忆；具体行业、工艺、设备及企业沿革待核",
            "老工业园区曾支撑浮屠镇工业繁荣，承载工人、家属和地方产业迁移记忆；社区口述和厂史待补",
            "现纳入浮屠镇闲置厂房盘活和新材料产业招商，具体保留建筑、权属和更新范围待规划资料核验",
        ),
        "notes": "来源明确将山下工业园列入浮屠镇老工业园区厂房资源，但没有证明其为单一工厂或法定遗产；以片区候选记录保留，待四普和规划档案拆分。",
        "aliases": ["浮屠山下工业园", "浮屠镇老工业园区山下片区"],
        "asset_kind": "industrial_landscape",
    },
    {
        "inventory_id": "HBI-HS-040",
        "name": "阳新县浮屠镇麻纺厂旧厂区",
        "city": "黄石市",
        "district_county": "阳新县浮屠镇（具体厂界待核）",
        "industry_category_l1": "纺织工业",
        "recognition_level": "research_candidate",
        "recognition_status": "政府报道确认的三线老工业厂区；未见法定工业遗产认定",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["yangxin_futu_industry_2024", "yangxin_futu_gov_2024"],
        "cultural_evidence": ev(
            "麻纺厂老厂房、闲置工业用地及老工业园区空间；公开来源未给出建筑、设备和厂界清单",
            "麻纺及纺织生产技术、原料处理和乡镇工业组织记忆；具体工艺、机器和产品待厂志核验",
            "麻纺厂与浮屠镇传统工业、就业和产业迁移相连；工人家庭、职工社区和地方产业记忆待口述采集",
            "现纳入老工业园区闲置厂房盘活和鞋纺等产业招商，原厂区保留情况、产权和更新边界待核",
        ),
        "notes": "两篇政府来源均点名浮屠镇麻纺厂，但没有提供独立厂址、建厂年代和现存设施；保留为来源确认的工业文化对象，法定级别和实体边界待核。",
        "aliases": ["浮屠麻纺厂", "阳新麻纺厂"],
        "asset_kind": "industrial_site",
    },
    {
        "inventory_id": "HBI-SNJ-005",
        "name": "神农架木鱼林场断江坪伐木队工业文化景观",
        "city": "神农架林区",
        "district_county": "木鱼镇断江坪（具体队址待核）",
        "industry_category_l1": "林业生产与木材加工",
        "recognition_level": "research_candidate",
        "recognition_status": "神农架国家公园和国防部报道确认的伐木队、林场和木材工业社会记忆；未见法定工业遗产认定",
        "record_status": "source_lead",
        "geocode_status": "pending",
        "source_keys": ["shennongjia_logging_team_2023", "shennongjia_wood_mill_2022", "shennongjia_forestry_history_2025"],
        "cultural_evidence": ev(
            "木鱼林场断江坪队、林场道路、养路班和伐木班可能遗留的工棚、工具、绞盘或木材集运节点；公开报道未给出建筑和设备清单",
            "山地伐木、修路、木材集运和林场作业组织技术；1980—1983年伐木班经历有官方报道，具体工法和设备待档案核验",
            "林二代、伐木工、养路工及其家庭生活构成神农架由木头经济转向生态保护的社会记忆；口述史、影像和职工名册待补",
            "神农架2000年全面停止天然林采伐后生产体系转向护林和生态管理；断江坪队址、木材厂关联和现状边界待现场核验",
        ),
        "notes": "国家公园官网报道明确到木鱼林场断江坪队和1980—1983年伐木班经历，国防部来源补充林区木材厂工人记忆；页面抓取存在超时，暂保留为来源线索，不推断具体厂房仍存。",
        "aliases": ["断江坪伐木队", "木鱼林场断江坪队", "神农架木材厂工人记忆"],
        "asset_kind": "industrial_cultural_landscape",
        "related_inventory_ids": ["HBI-SNJ-001", "HBI-SNJ-003", "HBI-SNJ-004"],
    },
    {
        "inventory_id": "HBI-XG-013",
        "name": "安陆县粮食加工与棉花轧花设施旧址群（档案线索）",
        "city": "孝感市",
        "district_county": "安陆市（具体县域地址待核）",
        "industry_category_l1": "粮食与棉花加工",
        "recognition_level": "archive_lead",
        "recognition_status": "湖北省档案馆1965年征地档案题名线索；未见实体和法定工业遗产认定",
        "record_status": "source_lead",
        "geocode_status": "pending",
        "source_keys": ["hubei_archive_catalog_1965"],
        "cultural_evidence": ev(
            "档案题名涉及粮食储备仓库、棉花仓库、粮食加工厂和棉花轧花厂，具体建筑和设备待档案调阅、地方志及现场核验",
            "粮食储运、粮食加工、棉花仓储和轧花技术的县域生产体系；工艺流程与设备清单待补",
            "安陆县域粮棉生产、供销和劳动组织记忆；职工、合作社和地方粮食系统口述史待采集",
            "1965年征地建设档案可确认项目曾被规划或建设，实体是否存续、后续改制和现状用途待核",
        ),
        "notes": "省档案馆目录将四类设施列在同一征地档案题名中，本条先以旧址群登记，避免把未调阅的档案题名拆成四个已确认实体。",
        "aliases": ["安陆粮食加工厂", "安陆棉花轧花厂", "安陆粮棉加工设施"],
        "asset_kind": "industrial_agricultural_processing",
    },
    {
        "inventory_id": "HBI-JZ-015",
        "name": "松滋市清江矿山机械厂旧址（档案线索）",
        "city": "荆州市",
        "district_county": "松滋市（具体厂址待核）",
        "industry_category_l1": "机械制造工业",
        "recognition_level": "archive_lead",
        "recognition_status": "湖北省档案馆1965年征地档案题名线索；未见实体和法定工业遗产认定",
        "record_status": "source_lead",
        "geocode_status": "pending",
        "source_keys": ["hubei_archive_catalog_1965"],
        "cultural_evidence": ev(
            "档案题名明确出现清江矿山机械厂，厂房、机修车间和设备等实体待档案调阅和现场核验",
            "矿山机械制造、维修和服务地方矿业生产的技术记忆；产品、工艺和设备型号待厂志核验",
            "清江矿山机械厂与松滋工业化、矿山生产和职工群体相连；职工生活区和地方工业记忆待采集",
            "1965年征地档案可确认项目线索，厂址、存续状态、改制和现用途待核",
        ),
        "notes": "档案目录可核对厂名和年度，但页面未给出地址与实体现状，保持来源线索层级。",
        "aliases": ["清江矿山机械厂", "松滋矿山机械厂"],
        "asset_kind": "industrial_site",
    },
    {
        "inventory_id": "HBI-JZ-016",
        "name": "公安县砖瓦厂旧址（档案线索）",
        "city": "荆州市",
        "district_county": "公安县（具体厂址待核）",
        "industry_category_l1": "建材工业",
        "recognition_level": "archive_lead",
        "recognition_status": "湖北省档案馆1965年征地档案题名线索；未见实体和法定工业遗产认定",
        "record_status": "source_lead",
        "geocode_status": "pending",
        "source_keys": ["hubei_archive_catalog_1965"],
        "cultural_evidence": ev(
            "档案题名明确出现公安县砖瓦厂，窑炉、厂房、取土和堆场等实体待档案与现场核验",
            "砖瓦烧制、窑炉生产和地方建材供应技术记忆；窑型、燃料和产品规格待核",
            "砖瓦厂与县域城镇建设、工人就业和地方建材供给相连；职工和周边社区记忆待采集",
            "1965年征地批复档案确认建设线索，厂址、停产时间、窑体保存与现用途待核",
        ),
        "notes": "来源为省档案馆开放目录中的征地批复题名，尚不能证明厂址完整保存或属于文物。",
        "aliases": ["公安县砖瓦厂", "公安砖瓦厂"],
        "asset_kind": "industrial_site",
    },
    {
        "inventory_id": "HBI-XIANGYANG-028",
        "name": "襄阳县第三新华印刷厂旧址（档案线索）",
        "city": "襄阳市",
        "district_county": "襄阳市（原襄阳县，具体厂址待核）",
        "industry_category_l1": "印刷工业",
        "recognition_level": "archive_lead",
        "recognition_status": "湖北省档案馆1965年征地档案题名线索；未见实体和法定工业遗产认定",
        "record_status": "source_lead",
        "geocode_status": "pending",
        "source_keys": ["hubei_archive_catalog_1965"],
        "cultural_evidence": ev(
            "档案题名明确出现第三新华印刷厂，印刷车间、排版设备和办公生活设施待档案与现场核验",
            "铅印、制版、装订或地方出版印刷的技术记忆待厂史、设备档案核实",
            "印刷厂与襄阳县公共文化、教育传播和职工群体相连；产品、职工和社区记忆待采集",
            "1965年征地档案确认建设线索，厂址、设备、改制和现用途待核",
        ),
        "notes": "档案目录给出‘第三新华印刷厂’的具体题名，但未提供地址，暂作为来源线索。",
        "aliases": ["第三新华印刷厂", "襄阳县新华印刷厂"],
        "asset_kind": "industrial_site",
    },
    {
        "inventory_id": "HBI-XIANGYANG-029",
        "name": "襄樊市化肥厂旧址（档案线索）",
        "city": "襄阳市",
        "district_county": "襄阳市（原襄樊市，具体厂址待核）",
        "industry_category_l1": "化工工业",
        "recognition_level": "archive_lead",
        "recognition_status": "湖北省档案馆1966年征地与初步设计档案题名线索；未见实体和法定工业遗产认定",
        "record_status": "source_lead",
        "geocode_status": "pending",
        "source_keys": ["hubei_archive_catalog_1965"],
        "cultural_evidence": ev(
            "档案题名涉及化肥厂新建厂征地、初步设计和图纸，生产装置、厂房和管线待档案调阅与现场核验",
            "化肥生产、化工装置和农业生产资料供应技术记忆待厂志与行业档案核实",
            "化肥厂与襄樊城市工业化、农业供给和职工群体相连；工人和周边社区记忆待采集",
            "档案可确认建设和设计活动，投产、迁建、停产、环境风险与现用途待核",
        ),
        "notes": "省档案馆目录将其列入新建厂征地与设计档案，不能据此推断厂房仍存，保持来源线索。",
        "aliases": ["襄阳化肥厂", "襄樊化肥厂"],
        "asset_kind": "industrial_site",
    },
    {
        "inventory_id": "HBI-XIANGYANG-030",
        "name": "襄樊市棉纺织印染厂旧址（档案线索）",
        "city": "襄阳市",
        "district_county": "襄阳市（原襄樊市，具体厂址待核）",
        "industry_category_l1": "纺织工业",
        "recognition_level": "archive_lead",
        "recognition_status": "湖北省档案馆1966年征地与初步设计档案题名线索；未见实体和法定工业遗产认定",
        "record_status": "source_lead",
        "geocode_status": "pending",
        "source_keys": ["hubei_archive_catalog_1965"],
        "cultural_evidence": ev(
            "档案题名涉及棉纺织印染厂扩建初步设计、新建厂征地和图纸，厂房、染整设备和附属设施待核",
            "棉纺、织造、印染和纺织品生产技术记忆待厂志、设备档案核实",
            "棉纺织印染厂与襄樊纺织工业、就业和职工社区相连；职工与地方产业记忆待采集",
            "档案可确认扩建和设计活动，厂址、生产线迁移、停产和现用途待核；与既有襄阳棉纺厂记录暂不合并",
        ),
        "notes": "为避免与‘襄阳棉纺厂旧址’混同，单独保留档案题名中的棉纺织印染厂，待档案核对历史名称和地址后再去重。",
        "aliases": ["襄阳棉纺织印染厂", "襄樊棉纺织印染厂"],
        "asset_kind": "industrial_site",
    },
    {
        "inventory_id": "HBI-XIANGYANG-031",
        "name": "襄阳冷冻厂旧址（档案线索）",
        "city": "襄阳市",
        "district_county": "襄阳市（具体厂址待核）",
        "industry_category_l1": "食品冷藏与加工",
        "recognition_level": "archive_lead",
        "recognition_status": "湖北省档案馆1965—1966年征地档案题名线索；未见实体和法定工业遗产认定",
        "record_status": "source_lead",
        "geocode_status": "pending",
        "source_keys": ["hubei_archive_catalog_1965"],
        "cultural_evidence": ev(
            "档案题名明确出现襄阳冷冻厂，冷库、制冷机房和物流设施待档案、地方志与现场核验",
            "食品冷藏、制冷和城市供应链技术记忆待厂史与设备档案核实",
            "冷冻厂与襄阳城市食品供给、商贸流通和职工群体相连；社区记忆待采集",
            "1965—1966年征地档案确认建设线索，厂址、设备、停产和现用途待核",
        ),
        "notes": "档案目录未提供地址和存续信息，暂列来源线索。",
        "aliases": ["襄樊冷冻厂", "襄阳冷库厂"],
        "asset_kind": "industrial_site",
    },
    {
        "inventory_id": "HBI-XIANGYANG-032",
        "name": "襄阳县煤货场与棉花储备仓库旧址群（档案线索）",
        "city": "襄阳市",
        "district_county": "襄阳市（原襄阳县，具体地址待核）",
        "industry_category_l1": "工业仓储与运输",
        "recognition_level": "archive_lead",
        "recognition_status": "湖北省档案馆1965—1966年征地档案题名线索；未见实体和法定工业遗产认定",
        "record_status": "source_lead",
        "geocode_status": "pending",
        "source_keys": ["hubei_archive_catalog_1965"],
        "cultural_evidence": ev(
            "档案题名涉及煤货场、棉花储备仓库、石油库及相关平面图，具体仓储设施、铁路/码头连接待核",
            "煤炭、棉花和石油储运、装卸与城市工业供应链技术记忆待档案核实",
            "仓储设施与襄阳县工业、农业物资供应和运输工人群体相连；口述和老地图待采集",
            "1965—1966年征地批复确认建设线索，实体存续、污染风险和现用途待核",
        ),
        "notes": "档案题名将多个储运设施列在同一组文件中，先按旧址群登记，不将未核验的单体拆成确定遗产。",
        "aliases": ["襄阳煤货场", "襄阳棉花储备仓库", "襄阳石油库"],
        "asset_kind": "industrial_transport_site",
    },
    {
        "inventory_id": "HBI-XIANGYANG-033",
        "name": "枣阳县环城拖拉机站旧址（档案线索）",
        "city": "襄阳市",
        "district_county": "枣阳市（原枣阳县环城区域，具体地址待核）",
        "industry_category_l1": "农业机械服务",
        "recognition_level": "archive_lead",
        "recognition_status": "湖北省档案馆1965年征地档案题名线索；未见实体和法定工业遗产认定",
        "record_status": "source_lead",
        "geocode_status": "pending",
        "source_keys": ["hubei_archive_catalog_1965"],
        "cultural_evidence": ev(
            "拖拉机站机库、维修间、油料设施和场站空间待档案、地方志与现场核验",
            "农业机械维修、机耕服务和油料保障技术记忆待档案核实",
            "拖拉机站与枣阳县农业机械化、农忙服务和基层技术人员群体相连；口述和照片待采集",
            "1965年征地档案确认站点建设线索，站址、设备、改制和现用途待核",
        ),
        "notes": "档案目录明确写出枣阳环城拖拉机站申请征地，暂列为农业工业服务设施线索。",
        "aliases": ["枣阳环城拖拉机站", "枣阳县拖拉机站"],
        "asset_kind": "industrial_service_site",
    },
    {
        "inventory_id": "HBI-WUHAN-065",
        "name": "黄陂县储备粮仓旧址（档案线索）",
        "city": "武汉市",
        "district_county": "黄陂区（具体仓址待核）",
        "industry_category_l1": "粮食仓储",
        "recognition_level": "archive_lead",
        "recognition_status": "湖北省档案馆1965年征地档案题名线索；未见实体和法定工业遗产认定",
        "record_status": "source_lead",
        "geocode_status": "pending",
        "source_keys": ["hubei_archive_catalog_1965"],
        "cultural_evidence": ev(
            "档案题名明确出现黄陂县新建储备粮仓征地报告和协议，仓房、晒场、运输设施待档案与现场核验",
            "粮食储藏、调运和基层物资保障技术记忆待地方志和粮食系统档案核实",
            "储备粮仓与黄陂县粮食供给、灾年保障和仓储工人群体相连；口述和老照片待采集",
            "1965年征地档案确认建设线索，仓址、建筑保存、改制和现用途待核",
        ),
        "notes": "档案目录只确认新建储备粮仓的行政文件，不证明仓房现存；保留来源线索层级。",
        "aliases": ["黄陂储备粮仓", "黄陂县粮仓"],
        "asset_kind": "industrial_storage_site",
    },
    {
        "inventory_id": "HBI-SZ-012",
        "name": "随县粮食储备仓库旧址（档案线索）",
        "city": "随州市",
        "district_county": "随县（具体仓址待核）",
        "industry_category_l1": "粮食仓储",
        "recognition_level": "archive_lead",
        "recognition_status": "湖北省档案馆1965—1966年征地档案题名线索；未见实体和法定工业遗产认定",
        "record_status": "source_lead",
        "geocode_status": "pending",
        "source_keys": ["hubei_archive_catalog_1965"],
        "cultural_evidence": ev(
            "档案题名涉及随县粮食储备仓库建设，仓房、场地和运输设施待档案与现场核验",
            "粮食仓储、调运和基层粮食管理技术记忆待地方志与粮食系统档案核实",
            "粮仓与随县农业生产、粮食统购统销和仓储工人群体相连；口述和老照片待采集",
            "1965—1966年征地档案确认建设线索，仓址、建筑保存和现用途待核",
        ),
        "notes": "档案题名还涉及鱼池等配套设施，本条只登记其中具有工业仓储属性的粮食储备仓库，具体单体待核。",
        "aliases": ["随县粮库", "随县粮食储备库"],
        "asset_kind": "industrial_storage_site",
    },
]


UPDATES: dict[str, dict[str, Any]] = {
    "HBI-HS-004": {
        "source_keys": ["huangshi2019", "huangshi_steel_textile_2023"],
        "notes": "黄石市首批工业遗产中的下陆钢铁厂旧址连铸厂房；黄石市住房和城市更新局报道进一步确认其与东方钢铁厂（东钢）焦化、炼铁、炼钢连铸厂房群的关系，厂区建筑清单、停产沿革和保护边界待核。",
        "aliases": ["下陆钢铁厂", "东方钢铁厂", "东钢", "东钢连铸厂房"],
        "cultural_evidence": ev(
            "连铸厂房及东钢焦化、炼铁、炼钢生产建筑群；公开报道称部分厂房保存完好，具体单体和设备清单待测绘",
            "新中国首批钢铁厂的焦化、炼铁、炼钢连铸工艺和国产化工业技术记忆；设备型号与生产线档案待补",
            "东钢作为三线建设历史印迹，与下陆区工人、家属和城市工业化记忆相连；职工社区和口述史待采集",
            "老厂区纳入城市更新和工业遗产活化讨论，现状权属、环境风险、开放条件和保护规划待核",
        ),
    },
    "HBI-HS-016": {
        "source_keys": ["huangshi2019", "huangshi_steel_textile_2023"],
        "notes": "黄石市首批工业遗产中的湖北省拖拉机厂旧址；黄石市住房和城市更新局报道确认老厂区仍存在产权、资产和保护利用问题，厂房、设备、职工生活设施和现状边界待核。",
        "aliases": ["黄石拖拉机厂", "湖北拖拉机厂老厂区"],
        "cultural_evidence": ev(
            "湖北省拖拉机厂老厂区厂房、设备和配套生活设施；公开报道确认厂区被隔离并涉及资产处置，具体单体待测绘",
            "拖拉机制造、农业机械化和维修服务技术记忆；产品谱系和设备清单待厂志与档案核验",
            "拖拉机厂与黄石工业化、农业机械推广和职工家庭生活相连；职工名录、社区和口述史待补",
            "老厂区面临产权和保护利用问题，部分土地经历法拍，现状使用、环境风险和保护边界待核",
        ),
    },
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    by_id = {row["inventory_id"]: row for row in records}
    names = {row["name"] for row in records}
    added = 0
    updated = 0
    for row in NEW_RECORDS:
        if row["inventory_id"] in by_id:
            if by_id[row["inventory_id"]] != row:
                raise SystemExit(f"conflicting duplicate record: {row['inventory_id']}")
            continue
        if row["name"] in names:
            raise SystemExit(f"conflicting duplicate name: {row['name']}")
        records.append(row)
        by_id[row["inventory_id"]] = row
        names.add(row["name"])
        added += 1
    for key, value in NEW_SOURCES.items():
        if key in sources and sources[key] != value:
            raise SystemExit(f"conflicting source: {key}")
        sources[key] = value
    for inventory_id, patch in UPDATES.items():
        if inventory_id not in by_id:
            raise SystemExit(f"missing update target: {inventory_id}")
        row = by_id[inventory_id]
        for key, value in patch.items():
            row[key] = value
        updated += 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_ad_sources={len(NEW_SOURCES)} added_records={added} updated_records={updated} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
