from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "suizhou_bai_ri_action_2024": {
        "source_type": "municipal_government_portal",
        "title": "我市开展历史建筑普查认定工作（随县新增31处、广水新增20处，市本级约30多处拟待公布）",
        "org": "随州市人民政府门户网站（来源随州日报）",
        "pub_date": "2024-10-10",
        "url": "http://www.suizhou.gov.cn/xwdt/bmdt/202410/t20241010_1260730.shtml",
        "authority": "A",
        "notes": "2024-10-10报道载明全省历史建筑确定挂牌“百日行动”中随州累计公布新增历史建筑51处（随县新增31处、广水市新增20处），以所在地区人民政府名义公布挂牌；强调新中国成立以后、改革开放以来有代表性建筑物和构筑物；市本级（含曾都区）约有30多处拟待公布——与齐星5栋征求意见状态互证。",
    },
    "guangshui_survey_contract_2025": {
        "source_type": "government_procurement_contract",
        "title": "广水市2024历史建筑挂牌及测绘建档项目（项目编号421381202506000211，中标78.52万元，合同附件列明20处名单）",
        "org": "中国政府采购网/湖北省政府采购网（采购人：广水市住房和城乡建设局）",
        "pub_date": "2025-07-04",
        "url": "http://www.ccgp.gov.cn/cggg/dfgg/zbgg/202506/t20250625_24841716.htm",
        "authority": "A",
        "notes": "中标成交公告（2025-06-25，中标单位广水市应山房地产测绘中心，金额78.52万元，评分92.89）；竞争性磋商公告 http://www.ccgp.gov.cn/cggg/dfgg/jzxcs/202506/t20250609_24740351.htm；合同2025-06-25签订、2025-07-04公告（湖北省政府采购网），成果按《湖北省历史建筑测绘建档操作规程（试行）》汇交住建部“历史文化街区和历史建筑数据信息平台”。合同书依据载明广水市人民政府《关于同意新增20处历史建筑单位的批复》（广政函〔2024〕6号），并按测绘类型列明20处：全面测绘2处（方家湾革命旧址、麻堰鱼抗日碉堡）、典型测绘16处（平林市老街古民居一至四、应山县第一个中国共产党组织成立旧址、太平国共停战谈判旧址、应办八一渡槽、麻市老豆腐作坊、麻市老手工面条铺、江家桃园古民居一至三、田埔古建筑私塾、武胜关玄天观、余店赖家老屋、三潭毓秀牌坊）、简略测绘2处（左家河左德生旧居、田埔古建筑旧居）。名单源自政采合同附件（政府门户暂无名录公布文件，广政函〔2024〕6号未见主动公开版本）；广水市政府网“市政府文件”栏目2021-2025已核验无名录文件。",
    },
}


RECORD = {
    "inventory_id": "HBI-SZ-014",
    "name": "应办八一渡槽",
    "city": "随州市",
    "district_county": "广水市应山街道",
    "industry_category_l1": "水利工程与泵站",
    "recognition_level": "municipal_historical_building",
    "recognition_status": "广水市新增历史建筑（2024年，广政函〔2024〕6号批复新增20处之一，政采合同附件按典型测绘列名；正式名录文件政府门户未公开）",
    "record_status": "source_confirmed",
    "geocode_status": "pending",
    "source_keys": ["guangshui_survey_contract_2025", "suizhou_bai_ri_action_2024"],
    "cultural_evidence": {
        "material_carriers": "八一渡槽渡槽本体（应山街道）；长度、跨径、结构形式与保存状态待测绘建档成果核验",
        "technical_memory": "1970年代农田水利建设高潮时期的引水渡槽构筑物工艺，与孝感八燕渡槽（HBI-XN-002）、英山茶场村渡槽（HBI-HG-017）、利川建南天桥（HBI-ES-026）同谱系",
        "social_memory": "广水灌区农业灌溉与水利建设集体记忆",
        "current_use_or_loss": "2024年经广政函〔2024〕6号批复新增为历史建筑（以所在地区人民政府名义公布挂牌），2025年完成测绘建档（应山房地产测绘中心承做，成果已汇交部级平台）；在用/停用状态待核",
    },
    "notes": "名单源自政采合同附件（政府门户暂无名录公布文件，批复广政函〔2024〕6号未见主动公开版本）；广水20处中其余为革命旧址、古民居、老街铺面及麻市豆腐作坊/手工面条铺两处传统作坊（传统食品手工业，暂不单独入库可后续议定）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
    "aliases": [],
    "asset_kind": "industrial_utility_site",
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    for key, source in SOURCES.items():
        if key in sources and sources[key] != source:
            sources[key] = source
    sources.update(SOURCES)
    existing = next((row for row in records if row["inventory_id"] == RECORD["inventory_id"]), None)
    if existing is not None:
        if existing != RECORD:
            raise SystemExit("conflicting duplicate record")
        added = 0
    else:
        if any(row["name"] == RECORD["name"] for row in records):
            raise SystemExit("conflicting duplicate name")
        records.append(RECORD)
        added = 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_ce_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
