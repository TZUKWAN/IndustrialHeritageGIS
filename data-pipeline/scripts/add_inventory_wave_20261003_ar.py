from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "miit_batch7_notice_jxt_2025": {
        "source_type": "government_notice_reprint",
        "title": "第七批国家工业遗产名单公布（工信部政法函〔2025〕273号，湖北省经信厅转载）",
        "org": "湖北省经济和信息化厅（转载工业和信息化部通知）",
        "pub_date": "2025-10-27",
        "url": "https://jxt.hubei.gov.cn/bmdt/rdjj/202510/t20251027_5798081.shtml",
        "authority": "A",
        "notes": "通知正文载明第七批国家工业遗产及通过复核的第三批国家工业遗产名单由工业和信息化部2025年10月17日公布；页面附件列表由脚本动态加载，正文名单经由附件PDF来源核读。",
    },
    "miit_batch7_list_attachment_2025": {
        "source_type": "government_notice_attachment_repost",
        "title": "第七批国家工业遗产名单（工信部政法函〔2025〕273号附件1，32项）",
        "org": "工业和信息化部（襄阳市中小企业公共服务平台转载PDF）",
        "pub_date": "2025-10-17",
        "url": "https://www.xy96500.cn/storage/zhengce_project/2025_11_26/%E9%99%84%E4%BB%B6%EF%BC%9A1.%E7%AC%AC%E4%B8%83%E6%89%B9%E5%9B%BD%E5%AE%B6%E5%B7%A5%E4%B8%9A%E9%81%97%E4%BA%A7%E5%90%8D%E5%8D%95%5Bsize295126%5D.pdf",
        "authority": "B",
        "notes": "已下载核读11页名单PDF全表：序号19为湖北省武汉市汉阳区武汉市健民制药厂（申请名称健民药业集团股份有限公司），核心物项含原医化分厂、原原料仓库、原固体制剂车间、原酊水糖浆车间、原外用药车间、品牌商标认定资料、厂史档案文献与历史影像、产品药方与生产工艺资料、叶开泰中医药文化；湖北省当批仅此1项。本地存档 raw/hubei_2025_gongshi/batch7_national_list.pdf。",
    },
    "hubei_daily_jianmin_award_2025": {
        "source_type": "official_media",
        "title": "第四届国家工业遗产大会在黄石开幕 武汉市健民制药厂获授第七批国家工业遗产",
        "org": "湖北日报（荆楚网）",
        "pub_date": "2025-11-15",
        "url": "http://news.cnhubei.com/content/2025-11/15/content_19661319.html",
        "authority": "B",
        "notes": "湖北日报讯确认2025年11月13日第四届国家工业遗产大会在黄石开幕，工业和信息化部现场公布第七批名单并为32个国家工业遗产项目授牌，武汉市健民制药厂为湖北省当批唯一入选项目；全国已认定7批264项国家工业遗产。",
    },
    "mofcom_lzhbwg_jianmin": {
        "source_type": "government_time_honored_brand_museum",
        "title": "中华老字号数字博物馆·健民（叶开泰）",
        "org": "商务部（老字号数字博物馆）",
        "pub_date": None,
        "url": "https://lzhbwg.mofcom.gov.cn/edi_ecms_web_front/thb/detail/a0cabda94eeb47328cb399db11f2d822",
        "authority": "A",
        "notes": "官方老字号馆专页记载：1637年叶文机于汉口大夹街创叶开泰药号，与同仁堂、陈李济并称初清三杰、跻身中国四大药号；1912年叶凤池股份制改革；1953年6月1日改造为武汉市私营健民制药厂，1955年10月1日公私合营，1958年国营；2004年在上海证券交易所上市；龙牡壮骨颗粒为国家一级中药保护品种；叶开泰中医药文化园占地47000平方米、2018年6月开园，为国家AAA级旅游景区、武汉市非遗生产性保护示范基地；叶开泰传统中药制剂方法与十三代传人谱系。",
    },
}


RECORD = {
    "inventory_id": "HBI-WUHAN-068",
    "name": "武汉市健民制药厂（叶开泰药号）",
    "city": "武汉市",
    "district_county": "汉阳区",
    "industry_category_l1": "医药工业",
    "recognition_level": "national_heritage_related",
    "recognition_status": "第七批国家工业遗产（工信部政法函〔2025〕273号，2025年10月17日公布，全国32项之一，湖北省当批唯一；2025年11月13日第四届国家工业遗产大会黄石授牌）",
    "record_status": "source_confirmed",
    "geocode_status": "pending",
    "source_keys": [
        "miit_batch7_notice_jxt_2025",
        "miit_batch7_list_attachment_2025",
        "hubei_daily_jianmin_award_2025",
        "mofcom_lzhbwg_jianmin",
    ],
    "related_heritage_ids": ["HER-4c71d600d918"],
    "cultural_evidence": {
        "material_carriers": "第七批国家工业遗产核心物项：原医化分厂、原原料仓库、原固体制剂车间、原酊水糖浆车间、原外用药车间，健民/龙牡/叶开泰品牌商标认定资料，制药厂基建、行政、文书档案与历史影像，龙牡壮骨颗粒、健民咽喉片、小金胶囊等产品药方与生产工艺资料；叶开泰中医药文化园建筑群（占地47000平方米，2018年6月开园）",
        "technical_memory": "叶开泰传统中药制剂方法：膏方选、炙、洗、泡、煎、滤、密、炼、收九道工序，手工泛丸、轻红粉炼丹等技艺；道地药材选用传统（甘肃天水五花龙骨、安徽休宁松烟墨、云南鸭嘴胆矾）；龙牡壮骨颗粒（源出龙骨牡蛎汤，国家一级中药保护品种）、小金胶囊（源出小金丹）、拔毒生肌散等名药配伍；师带徒传承谱系延续十三代",
        "social_memory": "1637年叶文机创叶开泰药号于汉口，与同仁堂、陈李济并称初清三杰、跻身中国四大药号；前店后厂经营模式与修合虽无人见、存心自有天知店训；1912年叶凤池股份制改革；1929年代表中医药界赴南京抗争废止中医议案；1937年武汉沦陷前留店支援抗战；1953年改造为武汉市健民制药厂、1955年公私合营、1958年国营的体制沿革与几代职工记忆",
        "current_use_or_loss": "叶开泰中医药文化园（汉阳）以智能制造车间、非遗传承基地、叶开泰中医药文化博物馆、国医馆、汉阳造工业文化旅游等形态活化运营，为国家AAA级旅游景区、武汉市非遗生产性保护示范基地；第七批国家工业遗产核心物项中历史车间与仓库的本体保存状况与产权边界以工信部公布名单为准，待现场核验",
    },
    "notes": "全国主表与前端站点数据已含该对象（HER-4c71d600d918，第七批序号19）；本底册记录补充研究级四项文化证据与可追溯来源绑定。核心物项历史建筑保存现状与产权边界待现场核验；坐标未核验保持待核。",
    "aliases": ["叶开泰药号", "健民药业集团", "武汉市私营健民制药厂", "武汉市公私合营健民制药厂", "国营武汉市健民制药厂"],
    "asset_kind": "industrial_site",
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
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
    for key, source in SOURCES.items():
        if key in sources and sources[key] != source:
            raise SystemExit(f"conflicting source: {key}")
    sources.update(SOURCES)
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_ar_sources={len(SOURCES)} added_records={added} updated_records=0 total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
