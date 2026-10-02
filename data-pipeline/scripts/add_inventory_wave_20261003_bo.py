from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "enshi_heritage_buildings_batch1_2023": {
        "source_type": "county_city_government_notice",
        "title": "恩施市人民政府关于公布第一批历史建筑的通知（恩市政发〔2023〕154号，13处）",
        "org": "恩施市人民政府门户网站（政策文件PDF）",
        "pub_date": "2023-12-29",
        "url": "http://www.es.gov.cn/xxgk/zc/zcwj/202412/P020241226395463833880.pdf",
        "authority": "A",
        "notes": "恩市政发〔2023〕154号公布湖北省邮电管理局旧址等第一批13处历史建筑，PDF含名录表与逐处简介（已下载文本核读，本地存档 raw/enshi_heritage/）：第4项湖北省邮电管理局旧址（六角亭街道和平街，抗战时期为国民党湖北省邮电管理局、解放后为恩施县邮电局，现房屋闲置，传统建筑与欧式风格结合）；第7项宜红茶厂旧址（芭蕉侗族乡集镇，1938年建，占地3818平方米，多层砖混结构，中国茶叶公司派范和均、冯绍裘等技士办机制厂、首开机制茶，解放前夕设备被撤后由居民购下继续作茶叶加工坊）；另有恩施地区农校分校教室/实验楼（1952-1954仿苏式）、公园街天主教堂及多处老屋祠堂。",
    },
    "enshi_heritage_buildings_batch2_2024": {
        "source_type": "county_city_government_notice",
        "title": "恩施市人民政府关于公布第二批历史建筑的通知（恩市政发〔2024〕47号，30处）",
        "org": "恩施市人民政府门户网站",
        "pub_date": "2024-08-22",
        "url": "http://www.es.gov.cn/xxgk/dfbmptlj/xz/sjb/zc_sjb/202411/t20241126_1640199.shtml",
        "url2": "http://www.es.gov.cn/xxgk/dfbmptlj/xz/sjb/zc_sjb/202411/P020241126591788011614.pdf",
        "authority": "A",
        "notes": "恩市政发〔2024〕47号公布施州古城美术馆等第二批30处历史建筑（编号14-43），PDF逐处简介已下载核读（本地存档 raw/enshi_heritage/）：全部为传统民居、吊脚楼、街屋、乡公所（红土乡公所，1944年苏式风格）、美术馆与图书馆等，无工业对象（负结果记录）。恩施市第三批名录尚未检索到官方全文，待续查。",
    },
}


RECORDS = [
    {
        "inventory_id": "HBI-ES-022",
        "name": "宜红茶厂旧址（芭蕉机制茶厂）",
        "city": "恩施州",
        "district_county": "恩施市芭蕉侗族乡集镇",
        "industry_category_l1": "茶叶加工工业",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "恩施市第一批历史建筑（恩市政发〔2023〕154号名录第7项；1938年建）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["enshi_heritage_buildings_batch1_2023"],
        "cultural_evidence": {
            "material_carriers": "机制茶厂旧址建筑群（占地3818平方米、建筑面积3275平方米，多层砖混结构、机制红瓦顶、悬山式，位于芭蕉中街桥头河沿边）；厂房内制茶设备留存待现场测绘",
            "technical_memory": "1938年中国茶叶公司派副总技士冯绍裘率技士到恩施办机制厂、在芭蕉设分厂，有史以来官办茶厂首开机制茶；1940年起芭蕉成为全县茶叶主产区，并在朱砂溪等地增设五个制茶所；解放前夕设备被撤后由8户居民买下茶厂继续作茶叶加工坊——机制茶工艺引入鄂西的完整过程记忆",
            "social_memory": "芭蕉茶农、茶厂职工与抗战时期茶叶统制经济下的生产记忆；宜红茶产制销脉络与鄂西茶区 wartime 产业史",
            "current_use_or_loss": "以第一批历史建筑身份纳入保护体系，市政府要求挂牌、测绘和建档；现状用途与保存边界待核",
        },
        "notes": "直接取自恩市政发〔2023〕154号名录表及逐处简介（A级，PDF文本核读）；与本底册宜都红茶厂（HBI-PROV-002）、赵李桥茶厂（HBI-XN-017）同属湖北茶叶加工工业谱系；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["芭蕉茶厂", "恩施宜红茶厂"],
        "asset_kind": "industrial_site",
    },
    {
        "inventory_id": "HBI-ES-023",
        "name": "湖北省邮电管理局旧址（和平街）",
        "city": "恩施州",
        "district_county": "恩施市六角亭街道和平街",
        "industry_category_l1": "通信与城市基础设施",
        "recognition_level": "municipal_historical_building",
        "recognition_status": "恩施市第一批历史建筑（恩市政发〔2023〕154号名录第4项）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": ["enshi_heritage_buildings_batch1_2023"],
        "cultural_evidence": {
            "material_carriers": "邮电管理机构旧址建筑（和平街东端高地，传统建筑与近代欧式风格结合，镂空门墙、防火马头墙、圆弧形门窗带花纹石膏线）；建筑本体保存与闲置状态待现场测绘",
            "technical_memory": "抗日战争时期国民党湖北省邮电管理局驻地、解放后为恩施县邮电局——战时省域邮电通信指挥机构西迁恩施的通信史记忆",
            "social_memory": "老城邮电职工与和平街机构驻地记忆；建筑选址文化（大圈椅地形、石级阶梯）为多文化结合样本",
            "current_use_or_loss": "名录载房屋现已闲置；以第一批历史建筑身份纳入保护体系，活化方案待属地推进",
        },
        "notes": "直接取自恩市政发〔2023〕154号名录表及逐处简介（A级，PDF文本核读）；与汉口电灯公司、永耀电灯公司同属湖北近现代通信/电力基础设施谱系的恩施节点；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        "aliases": ["恩施县邮电局"],
        "asset_kind": "industrial_building",
    },
]


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    added = 0
    for record in RECORDS:
        existing = next((row for row in records if row["inventory_id"] == record["inventory_id"]), None)
        if existing is not None:
            if existing != record:
                raise SystemExit(f"conflicting duplicate record: {record['inventory_id']}")
            continue
        if any(row["name"] == record["name"] for row in records):
            raise SystemExit(f"conflicting duplicate name: {record['name']}")
        records.append(record)
        added += 1
    for key, source in SOURCES.items():
        if key in sources and sources[key] != source:
            raise SystemExit(f"conflicting source: {key}")
    sources.update(SOURCES)
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_bo_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
