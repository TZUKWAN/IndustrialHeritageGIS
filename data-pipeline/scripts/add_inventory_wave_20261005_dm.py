from __future__ import annotations

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"

S = {
    "ssdejc_official": {
        "source_type": "enterprise_official_site",
        "title": "荆州市沙市帝尔机床有限公司官网（原沙市第二机床厂改制企业，1952年始建，机电部定点磨床专业厂）",
        "org": "荆州市沙市帝尔机床有限公司",
        "pub_date": None,
        "url": "http://www.ssdejc.com/",
        "authority": "B",
        "notes": "官网自述'是原荆州市沙市第二机床厂改制后的企业。原企业始建于1952年，是原机电部定点生产磨床的专业厂家'；现址湖北省荆州市开发区跃进工业园；产品MG602工具磨、M2110A/C/D、M2125内圆磨、M1432A/D、M120W外圆磨、M4214绗磨、T8014镗缸机等。直连SSL失败经r.jina.ai代理核读。",
    },
    "jc35_dier_shop": {
        "source_type": "industry_platform_profile",
        "title": "机床商务网·帝尔机床商铺简介（改制实体2007年9月29日注册，荆州开发区跃进工业园）",
        "org": "机床商务网（jc35.com）",
        "pub_date": None,
        "url": "https://m.jc35.com/st207413/",
        "authority": "B",
        "notes": "改制实体'荆州市沙市帝尔机床有限公司'成立日期2007年09月29日，注册资本100万元，法人姜伟，地址荆州开发区跃进工业园；产品33条与原厂型号一致（T8014、M2125、MG602等）。原文核读。",
    },
    "weixin_jingzhoujiyi_erjichuang_zhaiyao": {
        "source_type": "media_excerpt_unverified",
        "title": "微信公众号'荆州记忆'《回眸｜八十年代的沙市企业精神(七)》沙市第二机床厂篇（仅搜索摘录，未核读原文）",
        "org": "微信公众号'荆州记忆'（2018-02-11）",
        "pub_date": "2018-02-11",
        "url": None,
        "authority": "B",
        "notes": "摘录载：机械行业建厂最早的单位之一、机械工业部定点企业、'中南地区唯一生产磨床的厂家'，座落沙市西区南湖，职工676人，占地45000平方米，25个品种年产600台。mp.weixin.qq.com直连与r.jina.ai代理均被'环境异常'验证页拦截，原文未核读——本条仅作摘录级旁证，细节待《沙市市志》核校。",
    },
    "weixin_huazaiwuli_erjichuang_zhaiyao": {
        "source_type": "media_excerpt_unverified",
        "title": "微信公众号'花在雾里'《沙市市第二机床厂（八十年代工厂篇）》（仅搜索摘录，未核读原文）",
        "org": "微信公众号'花在雾里'（2026-06-03）",
        "pub_date": "2026-06-03",
        "url": None,
        "authority": "B",
        "notes": "摘录载（方志体例）：厂址西区金龙路6号，占地45233㎡、职工695人、设备187台；沿革1950年合营利民机器厂（新沙路12号）→1958沙市机械厂→1959沙市第二机械厂→1961迁金龙路6号→1964试制磨床→1973定名沙市第二机床厂；1970试制'054甲'雷达；1980年T8014获机械部'信得过'产品，年产670台。微信验证拦截原文未核读——厂址与细沿革均为摘录级待核。",
    },
    "sina_kangjiansu_2001": {
        "source_type": "official_media_reprint",
        "title": "《武汉抗菌素厂境遇令人深思》（湖北日报2001-03-07，新浪新闻中心转载）",
        "org": "湖北日报（王溥、余凯、杨凯、杨伟）",
        "pub_date": "2001-03-07",
        "url": None,
        "authority": "B",
        "notes": "载：1958年建成，国家大二型抗生素化学制药企业，占地7万多平方米，位于武汉江汉二桥旁；职工2270人；'黄鹤'牌盐酸土霉素1991年获国家医药行业唯一最高奖银质奖，海外称'中国黄'，销往近30国，高峰年创汇1000万美元；1997年6月停产（成本上升、产品单一、管理不善），账面8000万元、负债1.2亿余元，留27人留守。原发直链未留存，经搜狗跳转+r.jina.ai代理核读新浪转载页（dailynews.sina.com.cn 2001-03-07 14:45），按原发站+标题+检索路径完整记录。",
    },
    "qcc_wuhan_kangjiansu": {
        "source_type": "business_registry",
        "title": "企查查'武汉抗菌素厂'工商信息（硚口区建一路2号，已注销）",
        "org": "企查查",
        "pub_date": None,
        "url": "https://www.qcc.com/firm/986f9c7987ca70d9a4b3e01977196fcc.html",
        "authority": "B",
        "notes": "成立1990-02-19（重新登记），登记状态注销，注册资本2709万元，法定代表人焦家祥，地址桥口区建一路2号，企业类型联营，行业化学药品原料药制造(C2710)；曾用名'武汉市武汉抗菌素厂'（1990-02-19至1998-08-27）。注销具体日期页面未显示。经r.jina.ai代理核读。",
    },
    "whfzg_nianjian_1995_yiyao": {
        "source_type": "local_gazetteer_official",
        "title": "1995年武汉年鉴专条【武汉抗菌素厂调整产品结构】",
        "org": "武汉地方志数字方志馆",
        "pub_date": "1995",
        "url": "http://www.whfzg.org.cn/book/dfz/bookread/id/1119/category_id/440987.html",
        "authority": "A",
        "notes": "国家大二型医药企业，固定资产5600万元，职工1800人；抗生素西药原料年产700吨、年创汇500万美元；1994年盐酸土霉素月产28→40吨、转产洁霉素3.5→5吨、租赁豫南药厂生产线半年产土霉素近130吨；1994年总产值1.11亿元、销售收入8306万元，列湖北省医药行业规模效益第6位。原文核读。",
    },
    "whfzg_gongyezhi_yiyao_yange": {
        "source_type": "local_gazetteer_official",
        "title": "《武汉市志·工业志（下）》医药工业【沿革】节（至1959年建成8家主要药厂含抗菌素厂）",
        "org": "武汉地方志数字方志馆",
        "pub_date": None,
        "url": "http://www.whfzg.org.cn/book/dfz/bookread/id/1004/category_id/371571.html",
        "authority": "A",
        "notes": "至1959年建成了武汉制药厂、抗菌素厂、久安制药厂、健民制药厂、中联制药厂、生物制品研究所等8家主要生产厂；武汉抗菌素厂生产了土霉素、红霉素、卡那霉素、灰黄霉素等。同页载明武汉制药厂/久安（二药）/中联各自建厂谱系——均为独立企业，与武汉抗菌素厂无合并关系。原文核读。",
    },
    "whfzg_gongyezhi_yiyao_gaikuang": {
        "source_type": "local_gazetteer_official",
        "title": "《武汉市志·工业志（下）》医药工业【概况】节（1985年含抗菌素厂在内7家企业职工8000余人）",
        "org": "武汉地方志数字方志馆",
        "pub_date": None,
        "url": "http://www.whfzg.org.cn/book/dfz/bookread/id/1004/category_id/371570.html",
        "authority": "A",
        "notes": "1985年武汉制药厂、武汉第二制药厂、武汉第三制药厂、武汉第四制药厂、武汉抗菌素厂和中联制药厂、健民制药厂7家企业共有职工8000余人，固定资产原值4700余万元。原文核读。",
    },
    "whfzg_nianjian_1986_yiyao": {
        "source_type": "local_gazetteer_official",
        "title": "1986年武汉年鉴【医药工业】节（抗菌素厂土霉素盐酸盐获国家银质奖、L-赖氨酸工程上马）",
        "org": "武汉地方志数字方志馆",
        "pub_date": "1986",
        "url": "http://www.whfzg.org.cn/book/dfz/bookread/id/1121/category_id/443323.html",
        "authority": "A",
        "notes": "'武汉抗菌素厂的土霉素盐酸盐'获国家优质产品银质奖；'武汉抗菌素厂L—赖氨酸1,000吨/年工程上马'；1986年全市化学制药厂9家。原文核读。",
    },
    "lszyy_jituan_official": {
        "source_type": "enterprise_official_site",
        "title": "李时珍医药集团官网厂史（溯源/传奇/概况/蕲春生产基地4页核读：1958年蕲春县人民政府挂牌创办李时珍制药厂，1998年台资改制）",
        "org": "李时珍医药集团",
        "pub_date": None,
        "url": "https://www.chinabencaogangmu.com/history.html",
        "authority": "B",
        "notes": "溯源页：1952-1956蕲州'本草药坊'公私合营为蕲春县国营李时珍药酒厂；1958年4月蕲春县人民政府正式挂牌创办蕲春县李时珍制药厂，生产治咳糖浆、李时珍药酒等25个中成药品种；1985年更名蕲春县李时珍药厂；1989年迁址、更名'湖北李时珍保健药品厂'；1998年台湾舒佳康（郭文和、林朝辉）控股保健药品厂与酒厂，成立湖北李时珍医药企业有限公司；2002年组建集团。概况/基地页：蕲春基地占地1200亩、厂房15万㎡、年产能60亿元，位于本草纲目生物科技园区。history/about/10026/company/jidi五页均原文核读。",
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
    _r("HBI-JZ-079", "沙市第二机床厂旧址（帝尔机床前身）", "荆州市", "沙市区金龙路6号（方志类文章摘录，待核）", "机械工业", "research_candidate",
       "无法定遗产认定；承继企业官网与机床行业平台沿革核读（机电部定点磨床专业厂）",
       ["ssdejc_official", "jc35_dier_shop", "weixin_jingzhoujiyi_erjichuang_zhaiyao", "weixin_huazaiwuli_erjichuang_zhaiyao"], "industrial_site", "1952年（始建）/1973年（定名）",
       "沙市西区厂区（占地4.5万㎡级，金龙路6号待核）与磨床产品谱系（MG602工具磨/M2110/M2125内圆磨/M1432/M120W外圆磨/M4214绗磨/T8014镗缸机）",
       "机电部定点磨床制造工艺；T8014镗缸机1980年获机械部'信得过'产品（摘录级）",
       "'中南地区唯一生产磨床厂家'（摘录级）的行业地位与沙市机械工业记忆；'7·21'工人大学—沙市职工大学教育谱系旁证",
       "原厂改制为荆州市沙市帝尔机床有限公司（2007年注册），迁荆州开发区跃进工业园在产；金龙路6号老厂区现状空缺",
       "承继企业官网经r.jina.ai核读（B级）证实1952年始建与机电部定点磨床厂口径；厂址金龙路6号、1950年利民机器厂前身、职工695人等方志细节仅微信公众号摘录级（微信验证拦截未核读原文），待《沙市市志》核校；原厂注销时间未证（工商平台封锁）；与在册沙市第一机床厂（HBI-JZ-078）、荆州机床厂（HBI-JZ-018）为独立企业；坐标未核验保持待核。",
       ["沙市市第二机床厂", "荆州市沙市第二机床厂", "沙市机械厂", "利民机器厂", "沙市帝尔机床"]),
    _r("HBI-WUHAN-095", "武汉抗菌素厂旧址", "武汉市", "硚口区建一路2号（江汉二桥旁、水厂路片区）", "医药工业", "research_candidate",
       "无法定遗产认定；湖北日报2001年深度报道+市志/年鉴专节沿革（国家大二型抗生素企业，1997年停产）",
       ["sina_kangjiansu_2001", "qcc_wuhan_kangjiansu", "whfzg_nianjian_1995_yiyao", "whfzg_gongyezhi_yiyao_yange", "whfzg_gongyezhi_yiyao_gaikuang", "whfzg_nianjian_1986_yiyao"], "industrial_site", "1958年（建成）",
       "江汉二桥旁占地7万余㎡厂区（现状待核）与'黄鹤'牌盐酸土霉素产品谱系",
       "土霉素/红霉素/卡那霉素/灰黄霉素/洁霉素抗生素原料药制造工艺；'黄鹤'牌盐酸土霉素1991年获国家医药行业唯一最高奖银质奖、海外称'中国黄'销近30国；L-赖氨酸1000吨/年工程",
       "职工2270人的大型国企社区记忆；1997年6月停产、负债1.2亿濒临破产的国企转型教训（湖北日报深度报道）；1994年列湖北省医药行业规模效益第6位",
       "1997年6月停产，工商登记注销（注销日期未证）；老厂区现状空缺待核",
       "湖北日报2001-03-07报道经新浪转载r.jina.ai核读（B级，原发直链未留存按原发站+标题+检索路径记录）；厂址硚口区建一路2号经企查查核读；市志工业志（下）医药工业沿革/概况节与1986/1995年鉴专节核读（A级方志馆）；市志沿革节证实与武汉制药厂/二药/中联为独立企业无合并谱系；坐标未核验保持待核。",
       ["武汉市武汉抗菌素厂"]),
    _r("HBI-HG-044", "蕲春县李时珍制药厂旧址", "黄冈市", "蕲春县蕲州镇（建厂地，具体门牌待核；1989年迁出）", "医药工业", "research_candidate",
       "无法定遗产认定；企业官网厂史沿革核读（1958年县人民政府挂牌创办，1998年台资改制）",
       ["lszyy_jituan_official"], "industrial_site", "1958年4月（挂牌创办）",
       "蕲州老厂区（1989年迁出，现状待核）与25个中成药品种产品谱系（治咳糖浆、李时珍药酒等）",
       "蕲春中成药制药工艺传承（本草药坊—公私合营药酒厂—国营制药厂谱系）",
       "医圣故里中医药工业记忆：1952-1956公私合营→1958年4月国营挂牌→1985更名→1989迁址更名湖北李时珍保健药品厂→1998台湾舒佳康控股组建湖北李时珍医药企业有限公司→2002组建集团（蕲春基地现占地1200亩、厂房15万㎡）",
       "1989年迁出蕲州，集团现址蕲春本草纲目生物科技园区在产；蕲州老厂区现状空缺待核",
       "李时珍医药集团官网4页核读（B级）；建厂地蕲州为官网语境+公众号摘录互证（具体门牌待核）；存在独立注册主体'湖北省蕲春县李时珍药厂'（1992年，赤东镇走马岭——摘录级）须与集团谱系区分；'1989年更名保健药品厂'（官网）与'1998年酒厂改制'（公众号摘录）口径出入并存注明；坐标未核验保持待核。",
       ["蕲春县李时珍制药厂", "湖北李时珍保健药品厂", "湖北李时珍医药企业有限公司", "蕲春县李时珍药酒厂"]),
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
    print(f"wave_dm_S={len(S)} added={added} total={len(records)} src={len(sources)}")


if __name__ == "__main__":
    main()
