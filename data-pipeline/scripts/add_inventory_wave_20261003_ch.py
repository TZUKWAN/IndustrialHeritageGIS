from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "yidu_batch2_2024": {
        "source_type": "county_city_government_notice",
        "title": "市人民政府关于公布宜都市第二批历史建筑名录的通知（都政发〔2024〕6号，27处）",
        "org": "宜都市人民政府门户网站",
        "pub_date": "2024-08-05",
        "url": "https://www.yidu.gov.cn/zfxxgk/show.html?aid=8&id=223616&t=4",
        "authority": "A",
        "notes": "都政发〔2024〕6号公布27处，附完整名录表（智能体核读原文）：三八八厂二/三/六/七车间、科技楼、工具室、理化室（7处，中南光学仪器厂代号三八八厂，高坝洲镇中光社区，1970年代三线建设遗迹，砖混结构共约8590㎡）、枝城火车站（枝城镇沿江路，1970年，焦柳铁路二等客货运站，“唯一同时连通港口专用线和支线铁路的国家干线车站”）、候船室×2（陆城城河大道1号1980年代，宜红茶水运出口装船处；红花套老河街31号1953年，318国道进川码头）、油榨坊（姚家店镇油榨坪村一组，1980年代，墙有“工业学大庆、农业学大寨”标语，两台木制榨油机）、生产大队原址（油榨坪村一组，1950年代，原生产大队库房）、骡马行（陆城唐家巷14号，民国，为福星玉茶漆行提供运输住宿）、国营旅行社（枝城滨江路，1950年代，老码头旁）、文物楼（红花套，1966年，原考古队库房）。",
    },
    "zhijiang_batch3_2022": {
        "source_type": "county_city_government_notice",
        "title": "枝江市人民政府关于公布枝江市第三批历史建筑名录的通知（枝府发〔2022〕2号，4处）",
        "org": "枝江市人民政府门户网站",
        "pub_date": "2022-01-28",
        "url": "http://www.zgzhijiang.gov.cn/zfxxgk/show.html?id=217190&t=4",
        "authority": "A",
        "notes": "枝府发〔2022〕2号公布4处（编号11-14）：董市供销社（编号12，民国，老正街上街67号东南侧）、董市裁缝铺（编号11，五六十年代）、顾家布庄（编号13，五六十年代）、老正街63号民居（编号14，明清）。编号自11起印证前两批共10处；董市老正街2019年6月确定为湖北省历史文化街区。",
    },
    "changyang_batch3_2024": {
        "source_type": "county_media_report",
        "title": "我县第三批历史建筑完成挂牌保护（38处，含原马家坪粮站、原麻池人民公社旧址、渔峡口镇陶器厂遗址）",
        "org": "长阳土家族自治县人民政府网（长阳融媒体）",
        "pub_date": "2024-09-02",
        "url": "http://www.changyang.gov.cn/content-5086-529714-1.html",
        "authority": "A",
        "notes": "长阳第三批历史建筑38处完成挂牌保护，明确列举原马家坪粮站（粮食系统）、原麻池人民公社旧址（麻池为湘鄂西革命根据地粮油生产供给地）、渔峡口镇陶器厂遗址（厂）；长阳累计49处历史建筑建档（2021年首批8处+后续批次）。38处完整名单未检索到。",
    },
}


def _es(record_id: str, name: str, dc: str, cat: str, kind: str, year: str, material: str, tech: str, social: str, use: str, notes: str, aliases: list) -> dict:
    return {
        "inventory_id": record_id,
        "name": name,
        "city": "恩施州",
        "district_county": dc,
        "industry_category_l1": cat,
        "recognition_level": "municipal_historical_building",
        "recognition_status": "宜都市第二批历史建筑（都政发〔2024〕6号，2024-08-05公布，27处之一）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["yidu_batch2_2024"],
        "cultural_evidence": {
            "material_carriers": material,
            "technical_memory": tech,
            "social_memory": social,
            "current_use_or_loss": use,
        },
        "notes": notes,
        "aliases": aliases,
        "asset_kind": kind,
    }


ES_RECORDS = [
    _es("HBI-ES-035", "三八八厂车间与科技楼建筑群（二、三、六、七车间，科技楼、工具室、理化室）", "宜都市高坝洲镇中光社区", "三线军工工业", "industrial_building", "1970年代",
        "中南光学仪器厂（代号三八八厂）车间与科技楼建筑群7处（二、三、六、七车间，科技楼、工具室、理化室），砖混结构共约8590平方米",
        "三线建设时期光学仪器制造的精密加工车间组群（车、铣、磨、装配与理化检测功能分区）",
        "三线军工科技人员与“好人好马上三线”的建设者记忆",
        "以第二批历史建筑身份纳入保护体系；厂区停产/转型状态与设备留存待核",
        "直接取自都政发〔2024〕6号名录表（A级，智能体核读原文）；7处合并记录以保持厂区功能分区完整；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["中南光学仪器厂", "三八八厂"],
    ),
    _es("HBI-ES-036", "枝城火车站", "宜都市枝城镇沿江路", "铁路交通工业", "industrial_transport_site", "1970年",
        "焦柳铁路二等客货运站站房与站场设施（沿江路）；站房立面与站场轨道待现场测绘",
        "焦柳铁路（1970年通车）与长江港口的铁水联运枢纽——“唯一同时连通港口专用线和支线铁路的国家干线车站”，铁路-水运转运工艺节点",
        "枝城港铁水联运职工与鄂西南货物集散记忆",
        "以第二批历史建筑身份纳入保护体系；车站运营状态与保留范围待铁路部门核",
        "直接取自都政发〔2024〕6号名录表（A级，智能体核读原文）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["枝城站"],
    ),
    _es("HBI-ES-037", "宜都候船室（陆城城河大道、红花套老河街）", "宜都市陆城街道、红花套镇", "港口与水运工业", "industrial_transport_site", "1953/1980年代",
        "候船室2处：陆城城河大道1号（1980年代，宜红茶水运出口曾在此装船）、红花套老河街31号（1953年，318国道进川码头候船设施）",
        "长江客运候船建筑的班轮候船与行李托运功能形制；宜红茶水运出口与进川码头的航运节点",
        "宜红茶出口水运与川鄂往来旅客的候船记忆",
        "以第二批历史建筑身份纳入保护体系；候船功能是否延续待核",
        "直接取自都政发〔2024〕6号名录表（A级，智能体核读原文）；2处合并记录以保持长江客运候船谱系完整；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["陆城候船室", "红花套候船室"],
    ),
    _es("HBI-ES-038", "油榨坪村油榨坊与生产大队原址", "宜都市姚家店镇油榨坪村一组", "油料加工工业", "industrial_building", "1950年代/1980年代",
        "油榨坊（1980年代，墙存“工业学大庆、农业学大寨”标语，两台木制榨油机）与生产大队原址（1950年代，原生产大队库房）",
        "木制榨油机榨油工艺与生产大队库房的村办加工业组合",
        "油榨坪村地名来源的榨油产业记忆与标语墙时代印记",
        "以第二批历史建筑身份纳入保护体系；木制榨油机为稀缺实物，保护展示方案待核",
        "直接取自都政发〔2024〕6号名录表（A级，智能体核读原文）；2处合并记录；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["油榨坊"],
    ),
    _es("HBI-ES-039", "骡马行与国营旅行社（陆城·枝城）", "宜都市陆城街道唐家巷、枝城镇滨江路", "商贸服务与基层文化供应", "industrial_trade_site", "民国/1950年代",
        "骡马行（陆城唐家巷14号，民国，为福星玉茶漆行提供运输住宿）与国营旅行社（枝城滨江路，1950年代，老码头旁）",
        "茶漆贸易骡马运输住宿服务与国营旅游服务业态的建筑形制",
        "宜红茶漆骡马运输与新中国国营旅行社的业态变迁记忆",
        "以第二批历史建筑身份纳入保护体系；现状用途待核",
        "直接取自都政发〔2024〕6号名录表（A级，智能体核读原文）；2处合并记录以保持茶道运输—国营服务谱系；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        ["骡马行", "国营旅行社"],
    ),
    {
        "inventory_id": "HBI-YC-042",
        "name": "董市供销社",
        "city": "宜昌市",
        "district_county": "枝江市董市镇老正街",
        "industry_category_l1": "供销商贸与基层物资供应",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "枝江市第三批历史建筑（枝府发〔2022〕2号，2022-01-28公布，名录编号12；民国）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["zhijiang_batch3_2022"],
        "cultural_evidence": {
            "material_carriers": "供销社建筑本体（老正街上街67号东南侧，民国建筑）；门面与柜台格局待现场测绘",
            "technical_memory": "董市古镇供销合作商业的建筑形制，由民国商号到供销社的功能演变",
            "social_memory": "董市老正街商埠与供销社凭票供应记忆（董市老正街为湖北省历史文化街区）",
            "current_use_or_loss": "以第三批历史建筑身份正式公布保护；现状用途待核",
        },
        "notes": "直接取自枝府发〔2022〕2号名录（A级）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": [],
        "asset_kind": "industrial_trade_site",
    },
    {
        "inventory_id": "HBI-ES-041",
        "name": "长阳马家坪粮站与麻池人民公社旧址、渔峡口陶器厂遗址",
        "city": "宜昌市",
        "district_county": "长阳土家族自治县",
        "industry_category_l1": "粮食仓储工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "长阳土家族自治县第三批历史建筑（2024年挂牌保护，38处之一组）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["changyang_batch3_2024"],
        "cultural_evidence": {
            "material_carriers": "3处对象：原马家坪粮站（粮食系统）、原麻池人民公社旧址（麻池为革命根据地粮油生产供给地）、渔峡口镇陶器厂遗址（陶器厂）；保存状态待现场测绘",
            "technical_memory": "县域粮食购销、公社治理与陶器制造的多业态组合，麻池公社为湘鄂西根据地供给体系节点",
            "social_memory": "长阳粮站职工、公社社员与陶器工匠记忆",
            "current_use_or_loss": "第三批历史建筑已挂牌保护（38处完整名单未公开，3处经官方媒体报道明确列举）；现状与保护范围待核",
        },
        "notes": "直接取自长阳政府网第三批挂牌报道（A级，明确列举3处名称）；陶器厂遗址本体保存程度待核；坐标未核验保持待核。",
        "aliases": ["马家坪粮站", "麻池人民公社旧址", "渔峡口陶器厂"],
        "asset_kind": "industrial_storage_site",
    },
]


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    for key, source in SOURCES.items():
        if key in sources and sources[key] != source:
            sources[key] = source
    sources.update(SOURCES)
    added = 0
    for record in ES_RECORDS:
        existing = next((row for row in records if row["inventory_id"] == record["inventory_id"]), None)
        if existing is not None:
            if existing != record:
                raise SystemExit(f"conflicting duplicate record: {record['inventory_id']}")
            continue
        if any(row["name"] == record["name"] for row in records):
            raise SystemExit(f"conflicting duplicate name: {record['name']}")
        records.append(record)
        added += 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_ch_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
