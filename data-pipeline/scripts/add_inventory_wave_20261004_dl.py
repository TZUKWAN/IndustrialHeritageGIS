from __future__ import annotations

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"

S = {
    "toutiao_shalongda_banyun_2019": {
        "source_type": "official_media",
        "title": "原沙隆达厂最新搬迁进展（前身1958年沙市农药厂，老厂区装置拆除及土地修复）",
        "org": "荆州新闻网（头条号转载）",
        "pub_date": "2019-10-10",
        "url": "https://www.toutiao.com/article/6746124750881292808/",
        "authority": "B",
        "notes": "前身为沙市农药厂，1993年A股上市；搬迁改造总投资51.9亿元，除草剂项目搬迁完成后进入老厂区装置拆除及土地修复阶段。经r.jina.ai全文核读。",
    },
    "baike_hubei_zhiyaochang": {
        "source_type": "encyclopedia_entry",
        "title": "湖北制药有限公司（前身1968年湖北制药厂，三线医药企业）",
        "org": "百度百科",
        "pub_date": None,
        "url": "https://baike.baidu.com/item/湖北制药有限公司",
        "authority": "B",
        "notes": "前身湖北制药厂创建于1968年，国家大型二档企业，位于襄樊市，占地55万多平方米，国家精神类药品定点生产企业；2005年被宜昌三峡制药收购改制。词条核读。",
    },
    "baike_minkang_zhiyao": {
        "source_type": "encyclopedia_entry",
        "title": "湖北民康制药有限公司（1954年公私合营宜昌民康制药厂，溯源1921年兴盛祥药材号）",
        "org": "百度百科",
        "pub_date": None,
        "url": "https://baike.baidu.com/item/湖北民康制药有限公司",
        "authority": "B",
        "notes": "1954年兴盛祥与义安顺、怡安合并，组建川东鄂西地区规模最大的制药企业——公私合营宜昌民康制药厂，同年8月与内迁上海费氏药厂合并；2020年启动民康医药产业园迁建（老厂区在西陵区）。词条核读。",
    },
    "zhoudawuhan_286_wuhan_xiangjiaochang": {
        "source_type": "media_photo_essay",
        "title": "大武汉系列之286：武汉橡胶厂（化工部定点力车胎18家之一，原址三眼桥北路）",
        "org": "周国献（头条号）",
        "pub_date": "2022-12-04",
        "url": "https://www.toutiao.com/article/7172767831161864738/",
        "authority": "B",
        "notes": "化工部定点生产力车胎18家之一，1958年试制成功湖北省第一条汽车轮胎；原址江汉区三眼桥北路，厂区已拆改为住宅小区，尚存一栋武汉橡胶厂宿舍。经r.jina.ai全文核读。",
    },
    "zhoudawuhan_132_wuhan_diwuzhiyao": {
        "source_type": "media_photo_essay",
        "title": "大武汉系列之132：武汉第五制药厂（1979年建厂，1998年破产，东西湖大道7082号）",
        "org": "周国献（头条号）",
        "pub_date": None,
        "url": "https://www.toutiao.com/article/7647373582665794074/",
        "authority": "B",
        "notes": "东西湖大道7082号；2024年2月探访仍废弃，办公楼、锅炉房、质量控制中心可辨，存20世纪50年代平房宿舍与李时珍塑像。经r.jina.ai全文核读。",
    },
    "changjiangnet_wuyao_yuanda_2018": {
        "source_type": "official_media",
        "title": "从武药到远大医药：武汉首家改制国企重生（长江网）",
        "org": "长江网（头条号转载）",
        "pub_date": "2018-08-07",
        "url": "https://www.toutiao.com/article/6586902584106156558/",
        "authority": "B",
        "notes": "武汉制药厂前身八路军129师制药所随军南下扎根武汉；2003年因GMP改造缺资金被远大集团收购更名远大医药，武汉首家改制国企，2800余名职工身份置换。经r.jina.ai全文核读。",
    },
    "thepaper_wuhan_shihuachang": {
        "source_type": "official_media",
        "title": "武汉百年瞬间第41期：武汉石油化工厂的开建和发展（1971年动工、1978年正式建厂）",
        "org": "澎湃新闻（转载）",
        "pub_date": None,
        "url": "https://m.thepaper.cn/baijiahao_13460500",
        "authority": "B",
        "notes": "1971年6月一期工程（武钢炼油厂）破土动工，1975年一期建成，1978年8月正式建厂，1984年划归中国石化总公司，2013年跨入千万吨级炼化一体化。页面核读。",
    },
    "baike_guangji_yaoye": {
        "source_type": "encyclopedia_entry",
        "title": "湖北广济药业股份有限公司（前身1969年广济制药厂，世界三大核黄素生产商之一）",
        "org": "百度百科",
        "pub_date": None,
        "url": "https://baike.baidu.com/item/湖北广济药业股份有限公司",
        "authority": "B",
        "notes": "前身为1969年始建的湖北省广济制药厂，位于武穴市，1971年起生产维生素B2（核黄素），2004年成为世界三大核黄素生产商之一；证券日报2019-12-23载其获武穴市'退城进园'奖励2649万元（搜索摘录），老厂区搬迁线索明确。词条核读。",
    },
    "toutiao_hubei_1965_laolaoopian": {
        "source_type": "media_photo_essay",
        "title": "湖北省1965年老照片：黄石钙镁磷肥厂建成投产（杨礼门摄）",
        "org": "头条号历史影像",
        "pub_date": None,
        "url": "https://www.toutiao.com/article/7394016274939953702/",
        "authority": "B",
        "notes": "图注载'黄石钙镁磷肥厂自1965年5月份建成投入生产以来，到6月上旬已生产2000多吨钙镁磷肥'（杨礼门摄）。经r.jina.ai核读图注；实体存续与遗存待考。",
    },
}


def _r(rid, nm, city, dc, cat, lvl, status, src, kind, yr, mat, tech, soc, use, notes, aliases):
    return {
        "inventory_id": rid, "name": nm, "city": city, "district_county": dc,
        "industry_category_l1": cat, "recognition_level": lvl, "recognition_status": status,
        "record_status": "source_confirmed", "geocode_status": "pending", "source_keys": src,
        "cultural_evidence": {"material_carriers": mat, "technical_memory": tech, "social_memory": soc, "current_use_or_loss": use},
        "notes": notes, "aliases": aliases, "asset_kind": kind,
    }


RECORDS = [
    _r("HBI-WUHAN-091", "武汉橡胶厂", "武汉市", "江汉区三眼桥北路", "化工工业", "research_candidate",
       "无法定遗产认定；影像纪实与行业史志沿革（化工部定点力车胎18家之一）",
       ["zhoudawuhan_286_wuhan_xiangjiaochang"], "industrial_building", "1953年（公私合营起源）/1962年（合并建厂）",
       "三眼桥北路原厂区（已拆改为住宅小区）与现存一栋武汉橡胶厂宿舍",
       "1958年试制成功湖北省第一条汽车轮胎的橡胶加工工艺记忆",
       "化工部定点生产力车胎18家之一的行业地位与橡胶厂职工记忆",
       "厂区已拆改为住宅小区，仅存一栋武汉橡胶厂宿舍（现状待复核）",
       "周国献大武汉系列核读（B级）；前身谱系为1953年公私合营武汉橡胶制品厂与1958年国营新民橡胶厂；宿舍现状待复核；坐标未核验保持待核。",
       ["公私合营武汉橡胶制品厂", "国营新民橡胶厂"]),
    _r("HBI-WUHAN-092", "武汉第五制药厂旧址", "武汉市", "东西湖区东西湖大道7082号", "医药工业", "research_candidate",
       "无法定遗产认定；影像纪实探访（2024年2月仍废弃，建筑实物尚存）",
       ["zhoudawuhan_132_wuhan_diwuzhiyao"], "industrial_building", "1979年（建厂）",
       "废弃厂区建筑群：办公楼、锅炉房、质量控制中心可辨，存20世纪50年代平房宿舍与李时珍塑像",
       "东西湖制药厂时期的制药工艺与质量控制体系记忆",
       "1998年破产的国企改制记忆与平房宿舍职工社区记忆",
       "2024年2月探访仍废弃闲置，建筑实物尚存，处置去向待核",
       "周国献大武汉系列核读（B级）；原东西湖制药厂；废弃建筑处置去向需跟进；坐标未核验保持待核。",
       ["东西湖制药厂"]),
    _r("HBI-WUHAN-093", "武汉制药厂（远大医药前身）", "武汉市", "武汉市（历史厂址待专项核验）", "医药工业", "research_candidate",
       "无法定遗产认定；官方媒体企业史沿革（红色医药工业谱系）",
       ["changjiangnet_wuyao_yuanda_2018"], "industrial_site", "前身溯至八路军129师制药所（随军南下建厂）",
       "企业档案与产品谱系（老厂区遗存待核）",
       "随军制药所传承的制药工艺与GMP改造转型记忆",
       "武汉首家改制国企（2003年，2800余名职工身份置换）的国企改革记忆；红色医药工业谱系",
       "2003年被远大集团收购更名远大医药，企业在产延续",
       "长江网核读（B级）；历史厂址与遗存本体未核验；坐标未核验保持待核。",
       ["武药", "远大医药（武汉）有限公司"]),
    _r("HBI-WUHAN-094", "武汉石油化工厂", "武汉市", "青山区（厂区地址待精确核验）", "石油化工工业", "research_candidate",
       "在产企业（中石化武汉分公司），无遗产认定；官方媒体建厂史沿革",
       ["thepaper_wuhan_shihuachang"], "industrial_site", "1971年（动工）/1978年（正式建厂）",
       "青山区炼化厂区与千万吨级炼化一体化设施（在役）",
       "从武钢炼油厂一期到千万吨级炼化一体化的炼油化工技术演进",
       "1971年一期工程破土动工的武汉现代石油工业起点记忆",
       "1984年划归中国石化总公司，2013年跨入千万吨级，在产运行",
       "澎湃转载武汉百年瞬间核读（B级）；在产企业关注老厂区早期设施演变与可展示工业记忆载体；坐标未核验保持待核。",
       ["武钢炼油厂", "中石化武汉分公司"]),
    _r("HBI-JZ-077", "沙市农药厂旧址", "荆州市", "沙市区（原厂区待精确核验）", "化工工业", "research_candidate",
       "无法定遗产认定；官方媒体搬迁报道（老厂区装置拆除及土地修复阶段）",
       ["toutiao_shalongda_banyun_2019"], "industrial_site", "1958年（始建）",
       "原厂区装置与厂房（搬迁完成后进入拆除及土地修复阶段，抢救记录紧迫）",
       "国产农药（除草剂）制造工艺与1993年A股上市的行业转型记忆",
       "沙隆达与沙市化工城的工业城市记忆",
       "老厂区已关闭搬迁，拆除与土地修复推进中（2019年报道），遗存抢救紧迫",
       "荆州新闻网经头条转载核读（B级）；搬迁改造总投资51.9亿元；老厂区拆除进度需持续跟踪；坐标未核验保持待核。",
       ["沙隆达", "沙市农药厂", "安道麦荆州基地"]),
    _r("HBI-XIANGYANG-073", "湖北制药厂", "襄阳市", "襄阳市（厂区具体地址待专项核验）", "医药工业", "research_candidate",
       "无法定遗产认定；百科企业志沿革（三线医药企业）",
       ["baike_hubei_zhiyaochang"], "industrial_site", "1968年（创建）",
       "占地55万余平方米的三线厂区（遗存与现状待核）",
       "国家精神类药品定点生产的药品制造工艺记忆",
       "'三线'建设医药企业记忆与国家大型二档企业的职工社区记忆",
       "2005年被宜昌三峡制药收购改制为湖北制药有限公司，企业存续",
       "百度百科核读（B级）；创建于襄樊（今襄阳），厂址与遗存本体未核验；坐标未核验保持待核。",
       ["湖北制药有限公司"]),
    _r("HBI-YC-071", "宜昌民康制药厂", "宜昌市", "西陵区（老厂区）", "医药工业", "research_candidate",
       "无法定遗产认定；百科企业志沿革（公私合营老字号药厂）",
       ["baike_minkang_zhiyao"], "industrial_site", "1921年（兴盛祥溯源）/1954年（公私合营建厂）",
       "西陵区老厂区（2020年启动民康医药产业园迁建，遗存待核）",
       "川东鄂西最大制药企业的中药制药工艺传承",
       "1921年兴盛祥药材号老字号渊源与1954年公私合营、内迁上海费氏药厂合并的工商业社会主义改造记忆",
       "2020年启动产业园迁建，老厂区现状待核",
       "百度百科核读（B级）；老厂区边界与遗存本体未核验；坐标未核验保持待核。",
       ["兴盛祥", "湖北民康制药"]),
    _r("HBI-HS-058", "黄石钙镁磷肥厂", "黄石市", "黄石市（厂址待专项核验）", "化工工业", "research_candidate",
       "无法定遗产认定；1965年新闻影像图注证据（实体存续待考）",
       ["toutiao_hubei_1965_laolaoopian"], "industrial_site", "1965年（建成投产）",
       "1965年建成投产时的厂区影像（杨礼门摄）",
       "钙镁磷肥生产工艺（投产首月余产2000余吨）",
       "1965年湖北化肥工业建设起步的历史影像记忆",
       "实体存续与遗存待考（目前仅有1965年影像证据）",
       "头条历史影像图注核读（B级）；证据链较薄，厂址与存续待县志/厂志补考；坐标未核验保持待核。",
       []),
    _r("HBI-HG-043", "广济制药厂（广济药业前身）", "黄冈市", "武穴市（老厂区）", "医药工业", "research_candidate",
       "无法定遗产认定；百科企业志沿革与'退城进园'搬迁线索",
       ["baike_guangji_yaoye"], "industrial_site", "1969年（始建）",
       "武穴老厂区（'退城进园'搬迁线索，遗存待核）",
       "维生素B2（核黄素）发酵工艺——2004年成为世界三大核黄素生产商之一",
       "县域医药发酵工业从1969年县办药厂到上市公司的演进记忆",
       "2019年获武穴市'退城进园'奖励2649万元（证券日报摘录），老厂区搬迁线索明确，现状待核",
       "百度百科核读（B级）；老厂区边界与遗存本体未核验；坐标未核验保持待核。",
       ["湖北省广济制药厂", "广济药业"]),
]


def main():
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    for key, source in S.items():
        if key in sources and sources[key] != source:
            raise SystemExit(f"conflicting source: {key}")
    sources.update(S)
    added = 0
    for record in RECORDS:
        existing = next((r for r in records if r["inventory_id"] == record["inventory_id"]), None)
        if existing is not None:
            if existing != record:
                raise SystemExit(f"conflicting duplicate record: {record['inventory_id']}")
            continue
        if any(r["name"] == record["name"] for r in records):
            raise SystemExit(f"conflicting duplicate name: {record['name']}")
        records.append(record)
        added += 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_dl_S={len(S)} added={added} total={len(records)} src={len(sources)}")


if __name__ == "__main__":
    main()
