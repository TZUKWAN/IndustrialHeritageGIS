from __future__ import annotations

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"

S = {
    "whfzg_gongyezhi_xiechang_huochai_zhuanji": {
        "source_type": "local_gazetteer_official",
        "title": "《武汉市志·工业志》专记·燮昌火柴厂（1897年宋炜臣创办，武汉第一家民族资本近代工厂）",
        "org": "武汉地方志数字方志馆",
        "pub_date": None,
        "url": "https://www.whfzg.org.cn/book/dfz/bookread/id/1004/category_id/371355.html",
        "authority": "A",
        "notes": "1897年宋炜臣创办于汉口日租界（今芦沟桥路一带），占地1.7万平方米，产双狮牌火柴；1927年停业，厂房机件作价30万银元售上海大中华火柴公司。原文核读。",
    },
    "whfzg_gongyezhi_huochai": {
        "source_type": "local_gazetteer_official",
        "title": "《武汉市志·工业志》武汉火柴厂节（1917年燧华火柴公司起源，硚口仁寿路）",
        "org": "武汉地方志数字方志馆",
        "pub_date": None,
        "url": "https://www.whfzg.org.cn/book/dfz/bookread/id/1004/category_id/371315.html",
        "authority": "A",
        "notes": "1917年燧华火柴公司起源，1948年改名，1958年两厂合并国营为武汉火柴厂；硚口仁寿路；航空牌火柴1985年产51万件。原文核读。",
    },
    "zhoudawuhan_292_huochai": {
        "source_type": "media_photo_essay",
        "title": "大武汉系列之292：武汉火柴厂（厂区已拆建仁硚新村、航天星苑小区，遗存两处宿舍群）",
        "org": "周国献/黑镜头（头条号）",
        "pub_date": None,
        "url": "https://www.toutiao.com/article/7196849257440297476/",
        "authority": "B",
        "notes": "厂区已拆，改建仁硚新村、航天星苑小区；遗存宿舍：仁寿路/双厂巷7栋、汉西路汉水四村10栋（已见拆迁标记）。经r.jina.ai原文核读。",
    },
    "whfzg_gongyezhi_dianchi": {
        "source_type": "local_gazetteer_official",
        "title": "《武汉市志·工业志》武汉电池厂节（1925年大明电池厂起源，1961年迁循礼门）",
        "org": "武汉地方志数字方志馆",
        "pub_date": None,
        "url": "https://www.whfzg.org.cn/book/dfz/bookread/id/1004/category_id/371314.html",
        "authority": "A",
        "notes": "1925年大明电池厂起源；1955年公私合营，1956年13家私营厂并入；1961年迁循礼门（江汉路原宇宙烟厂厂址）；大公牌R20干电池获湖北省优质产品。原文核读。",
    },
    "whfzg_gongyezhi_dengpao": {
        "source_type": "local_gazetteer_official",
        "title": "《武汉市志·工业志》武汉灯泡厂节（1958年由第一灯泡合作工厂转国营，武昌马房山）",
        "org": "武汉地方志数字方志馆",
        "pub_date": None,
        "url": "https://www.whfzg.org.cn/book/dfz/bookread/id/1004/category_id/371334.html",
        "authority": "A",
        "notes": "1958年由第一灯泡合作工厂转国营；武昌马房山厂区；产普通灯泡/日光灯/三基色荧光灯，1985年产2933万只。原文核读。",
    },
    "whfzg_gongyezhi_boli": {
        "source_type": "local_gazetteer_official",
        "title": "《武汉市志·工业志》武汉玻璃厂节（1958年筹建纸坊八分山，1961年停建未建成；省新生玻璃厂1969年大军山投产）",
        "org": "武汉地方志数字方志馆",
        "pub_date": None,
        "url": "https://www.whfzg.org.cn/book/dfz/bookread/id/1004/category_id/371711.html",
        "authority": "A",
        "notes": "1958年筹建（'200项重点项目'），选址武昌县纸坊八分山，1961年停建未建成；实际投产者为1969年省新生玻璃厂（大军山）。原文核读；'武汉长利玻璃'承继改制关系仅见系列文章标题（摘录级待核）。",
    },
    "whfzg_gongyezhi_zhige": {
        "source_type": "local_gazetteer_official",
        "title": "《武汉市志·工业志》武汉制革厂节（溯源1903年南湖制皮厂，1965年正式设厂）",
        "org": "武汉地方志数字方志馆",
        "pub_date": None,
        "url": "https://www.whfzg.org.cn/book/dfz/bookread/id/1004/category_id/371432.html",
        "authority": "A",
        "notes": "溯源1903年南湖制皮厂；1965年一分为三正式设厂；汉口中山大道1541号；滨江牌猪皮彩色面革等，全市最大国营制革厂。原文核读。",
    },
    "whfzg_gongyezhi_yinshua_wuhan": {
        "source_type": "local_gazetteer_official",
        "title": "《武汉市志·工业志》武汉印刷厂节（1949年8月成立，1968年造国内首台塑料四色凹印机）",
        "org": "武汉地方志数字方志馆",
        "pub_date": None,
        "url": "https://www.whfzg.org.cn/book/dfz/bookread/id/1004/category_id/371277.html",
        "authority": "A",
        "notes": "1949年8月成立（市财政局供应社印刷部）；汉口民意四路101号，占地1.7万平方米；塑料包装印刷，1968年造出国内首台塑料四色凹印机。原文核读。",
    },
    "whfzg_gongyezhi_xinhua_yinshua": {
        "source_type": "local_gazetteer_official",
        "title": "《武汉市志·工业志》湖北新华印刷厂节（1949年5月华中新华印刷厂创建，1954年迁硚口解放大道79号）",
        "org": "武汉地方志数字方志馆",
        "pub_date": None,
        "url": "https://www.whfzg.org.cn/book/dfz/bookread/id/1004/category_id/371278.html",
        "authority": "A",
        "notes": "1949年5月以华中新华印刷厂起家，1954年迁硚口解放大道79号；教科书/图书印制，全国四大印刷基地之一。原文核读；现改制湖北新华印务有限公司打造'智慧工厂'为摘录级。",
    },
    "whfzg_gongyezhi_youzhi_huaxue": {
        "source_type": "local_gazetteer_official",
        "title": "《武汉市志·工业志》武汉油脂化学厂节（1909年福和油厂起源，一枝花牌洗衣粉）",
        "org": "武汉地方志数字方志馆",
        "pub_date": None,
        "url": "https://www.whfzg.org.cn/book/dfz/bookread/id/1004/category_id/371323.html",
        "authority": "A",
        "notes": "1909年福和油厂起源；1960年改名武汉油脂化学厂；汉阳月湖堤202号（志书作月湖路202号）；一枝花牌洗衣粉1985年产3.5万吨。原文核读；后改组武汉一枝花集团（汉阳区志摘录级）、月湖厂区随琴台文化区改造消失（公众号摘录级）。",
    },
    "whfzg_gongyezhi_shipin": {
        "source_type": "local_gazetteer_official",
        "title": "《武汉市志·工业志》武汉食品厂节（1951年市合作社购小苏州食品店建社，1958年改国营长江食品厂）",
        "org": "武汉地方志数字方志馆",
        "pub_date": None,
        "url": "https://www.whfzg.org.cn/book/dfz/bookread/id/1004/category_id/371281.html",
        "authority": "A",
        "notes": "1951年市合作社购小苏州食品店建社，1958年改国营长江食品厂；汉口（志书未载详址）；糖果糕点。同卷另有冠生园（1928年，中山大道永广里设厂）、英商赞育汽水厂（1921年，车站路9号）、和利汽水厂（岳飞街44号）线索。原文核读。",
    },
    "jingzhou_zaixian_gaigaiban_2021": {
        "source_type": "official_media",
        "title": "'关改搬转'后厂区到底关没关？市民受邀现场看进展（荆州日报，荆州市政府网转载）",
        "org": "荆州日报/荆州市人民政府网",
        "pub_date": "2021-09-19",
        "url": "https://www.jingzhou.gov.cn/ztzl_9/zyhbdchtk/gzjb/202109/t20210919_639426.shtml",
        "authority": "A",
        "notes": "安道麦沙隆达老厂区已于2020年12月30日全部关闭停产，生产装置已全部清洗置换，主要反应装置已经拆除；待完成国有资产审批处置手续后对土地进行修复。政府网直核全文。",
    },
    "shashi_quzhang_turang_xiufu_2023": {
        "source_type": "district_government_portal",
        "title": "沙市区区长调研沙隆达老厂区土壤修复情况（2023-07-20）",
        "org": "沙市区人民政府网",
        "pub_date": "2023-07-21",
        "url": "http://www.shashi.gov.cn/huandengshashi/202307/t20230721_856170.shtml",
        "authority": "A",
        "notes": "2023年7月20日区长秦军赴沙隆达老厂区实地察看土壤修复情况，要求优化土壤修复方案——2023年年中老厂区已入土壤修复实施期。经r.jina.ai核读。",
    },
    "hubei_sthjt_turang_minglu_2025d7": {
        "source_type": "provincial_government_notice",
        "title": "湖北省建设用地土壤污染风险管控和修复名录（2025年第七批）：安道麦老厂（西厂区-原沙市化肥厂）地块'正在实施修复'",
        "org": "湖北省生态环境厅",
        "pub_date": "2025-12-18",
        "url": "https://sthjt.hubei.gov.cn/fbjd/zc/zcwj/sthjt/tzgg/202512/t20251218_5837236.shtml",
        "authority": "A",
        "notes": "名录载'安道麦股份有限公司老厂（西厂区－原沙市化肥厂）地块'，沙市区北京东路97号，2023-12-28列入，当前阶段'正在实施修复'，截至2025-12-15未移出；同名录另列'沙隆达（荆州）农药化工（原江陵农药厂）地块'（荆州区西环路）为另一地块。表格经r.jina.ai核读。",
    },
    "toutiao_heijingtou_huangshi_zhoucheng_2019": {
        "source_type": "media_excerpt_unverified",
        "title": "《黄石市轴承厂已拆除，建了中商百货、黄石摩尔城》（头条号'黑镜头'2019-04-07，仅标题级摘要，未核读原文）",
        "org": "头条号'黑镜头'",
        "pub_date": "2019-04-07",
        "url": None,
        "authority": "B",
        "notes": "标题陈述老厂地块已拆除、原址建中商百货与黄石摩尔城（湖滨大道一带，黄石港区）；原文经头条检索命中但正文未核读，仅标题级证据，与黄石港区2024年摩尔城安置房公示互为佐证。",
    },
    "huangshigang_moecheng_anzhi_2024": {
        "source_type": "district_government_publicity",
        "title": "黄石港区政府公示：黄石摩尔城项目湖滨大道180号安置住宅解除不可售状态（2024-03-01，仅搜索摘录，未核读原文）",
        "org": "黄石港区人民政府",
        "pub_date": "2024-03-01",
        "url": None,
        "authority": "A",
        "notes": "华迅房地产申请解除黄石摩尔城项目湖滨大道180号5号楼19套安置住宅不可售状态——佐证摩尔城项目推进；原文URL未留存，仅搜索摘录级。区政府网站内核查：征收补偿栏7条均无轴承厂公示，'轴承厂2024年获拆迁补偿款'线索维持未核读。",
    },
    "xinhuanet_liuheng_2018": {
        "source_type": "official_media",
        "title": "《刘珩同志逝世》（新华网2018-07-17，讣告提及曾任沙市第二机床厂工程师）",
        "org": "新华网",
        "pub_date": "2018-07-17",
        "url": "http://www.xinhuanet.com/politics/2018/07/17/c_1123140075.htm",
        "authority": "B",
        "notes": "讣告载刘珩'先后任湖北省沙市纺织机械厂技术员，第二机床厂工程师'——沙市第二机床厂人物史旁证（摘要级，未逐句核读全文）。",
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
    _r("HBI-WUHAN-096", "燮昌火柴厂旧址", "武汉市", "汉口日租界（今芦沟桥路一带）", "轻工业", "research_candidate",
       "无本体遗存法定认定；武汉市志工业志专记沿革（武汉第一家民族资本近代工厂）",
       ["whfzg_gongyezhi_xiechang_huochai_zhuanji"], "industrial_site", "1897年（创办）/1927年（停业）",
       "占地1.7万平方米厂区旧址（地上遗存待踏勘）与双狮牌火柴产品谱系",
       "武汉民族资本机器火柴工业发端；1927年停业后厂房机件作价30万银元售上海大中华火柴公司",
       "宋炜臣实业救国谱系记忆（与扬子机器厂创办同一实业界人士，互见HBI-WUHAN-089）",
       "1927年停业，原址融入汉口城区，遗存待踏勘",
       "武汉市志工业志专记核读（A级方志馆）；遗存本体未核验；坐标未核验保持待核。",
       ["燮昌火柴公司"]),
    _r("HBI-WUHAN-097", "武汉火柴厂旧址", "武汉市", "硚口区仁寿路（厂区）；遗存宿舍：仁寿路/双厂巷7栋、汉西路汉水四村10栋", "轻工业", "research_candidate",
       "无法定遗产认定；武汉市志工业志节+影像纪实沿革（厂区已拆，宿舍群抢救紧迫）",
       ["whfzg_gongyezhi_huochai", "zhoudawuhan_292_huochai"], "industrial_site", "1917年（燧华火柴公司起源）/1958年（合并国营）",
       "仁寿路厂区（已拆建仁硚新村、航天星苑小区）；遗存职工宿舍仁寿路/双厂巷7栋与汉西路汉水四村10栋（已见拆迁标记）",
       "航空牌火柴制造（1985年产51万件）——武汉火柴工业主力厂工艺记忆",
       "从1917年燧华火柴公司到国营武汉火柴厂的民族工业—国营厂沿革与火柴厂职工社区记忆",
       "厂区已拆建住宅小区；两处宿舍群存续且已见拆迁标记，抢救记录紧迫",
       "武汉市志工业志节核读（A级）+周国献大武汉系列之292经r.jina.ai核读（B级）；宿舍群拆迁动态需持续跟踪；坐标未核验保持待核。",
       ["燧华火柴公司"]),
    _r("HBI-WUHAN-098", "武汉电池厂", "武汉市", "江汉区循礼门（1961年迁入，原宇宙烟厂厂址）；起源地汉正街", "轻工业", "research_candidate",
       "无法定遗产认定；武汉市志工业志节沿革（民族电池工业起源）",
       ["whfzg_gongyezhi_dianchi"], "industrial_site", "1925年（大明电池厂起源）/1956年（公私合营）",
       "循礼门厂区（遗存待核）与大公牌R20干电池产品谱系",
       "干电池制造工艺（大公牌获湖北省优质产品）",
       "1925年大明电池厂民族电池工业起源与1956年13家私营厂公私合营的社会主义改造记忆",
       "厂区下落待查（周国献大武汉系列之115原文已404）",
       "武汉市志工业志节核读（A级方志馆）；厂区现状与遗存未核验，后续经城市留言板/长报档案补查；坐标未核验保持待核。",
       ["大明电池厂"]),
    _r("HBI-WUHAN-099", "武汉灯泡厂", "武汉市", "武昌区马房山", "轻工业", "research_candidate",
       "无法定遗产认定；武汉市志工业志节沿革（武汉电光源工业）",
       ["whfzg_gongyezhi_dengpao"], "industrial_site", "1958年（转国营）",
       "马房山厂区（遗存待核）与灯泡产品谱系（1985年产2933万只）",
       "普通灯泡/日光灯/三基色荧光灯制造工艺演进",
       "从第一灯泡合作工厂到国营厂的武汉电光源工业记忆",
       "厂区下落待查（大武汉系列之126原文已404）",
       "武汉市志工业志节核读（A级方志馆）；遗存未核验；坐标未核验保持待核。",
       ["第一灯泡合作工厂"]),
    _r("HBI-WUHAN-100", "武汉玻璃厂（八分山停建工程）", "武汉市", "江夏区纸坊八分山（停建工程地）；实际投产者为大军山省新生玻璃厂", "建材工业", "research_candidate",
       "无法定遗产认定；武汉市志工业志节沿革（未建成工程按工业史迹沿革收录）",
       ["whfzg_gongyezhi_boli"], "industrial_site", "1958年（筹建）/1961年（停建）",
       "纸坊八分山筹建工程（1961年停建未建成，无实体遗存）；实际投产者省新生玻璃厂（1969年，大军山）",
       "平板玻璃工业布局记忆——'200项重点项目'停建与大军山迁建的工业地理调整",
       "大跃进工业布局调整的停建史与省新生玻璃厂投产记忆",
       "停建工程无实体遗存；省新生玻璃厂承继投产，与武汉长利玻璃承继改制关系为摘录级待核",
       "武汉市志工业志节核读（A级方志馆）；未建成工程按沿革条目收录；长利玻璃承继关系待核；坐标未核验保持待核。",
       ["省新生玻璃厂", "武汉长利玻璃"]),
    _r("HBI-WUHAN-101", "武汉制革厂", "武汉市", "江岸区中山大道1541号", "轻工业", "research_candidate",
       "无法定遗产认定；武汉市志工业志节沿革（全市最大国营制革厂）",
       ["whfzg_gongyezhi_zhige"], "industrial_site", "溯源1903年南湖制皮厂/1965年（正式设厂）",
       "中山大道1541号厂区（遗存待核）与滨江牌猪皮彩色面革产品谱系",
       "制革工艺（全市最大国营制革厂）",
       "1903年南湖制皮厂起源的武汉制革工业世纪记忆与1965年一分为三的工业调整",
       "厂区下落待查",
       "武汉市志工业志节核读（A级方志馆）；遗存未核验；坐标未核验保持待核。",
       ["南湖制皮厂"]),
    _r("HBI-WUHAN-102", "武汉印刷厂", "武汉市", "江汉区民意四路101号", "印刷工业", "research_candidate",
       "无法定遗产认定；武汉市志工业志节沿革（包装印刷骨干厂）",
       ["whfzg_gongyezhi_yinshua_wuhan"], "industrial_site", "1949年8月（成立）",
       "民意四路101号占地1.7万平方米厂区（遗存待核）",
       "1968年造出国内首台塑料四色凹印机的包装印刷技术记忆",
       "从市财政局供应社印刷部到包装印刷骨干厂的国营印刷工业记忆",
       "厂区下落待查（大武汉系列之38原文已404）",
       "武汉市志工业志节核读（A级方志馆）；遗存未核验；坐标未核验保持待核。",
       []),
    _r("HBI-WUHAN-103", "湖北新华印刷厂", "武汉市", "硚口区解放大道79号（1954年迁入）", "印刷工业", "research_candidate",
       "无法定遗产认定；武汉市志工业志节沿革（全国四大印刷基地之一）",
       ["whfzg_gongyezhi_xinhua_yinshua"], "industrial_site", "1949年5月（华中新华印刷厂创建）",
       "解放大道79号厂区（遗存待核）与教科书/图书印制谱系",
       "全国四大印刷基地之一的书刊印刷工艺；现改制湖北新华印务打造'智慧工厂'（摘录级）",
       "华中新华印刷厂随军进城建厂的红色印刷工业记忆",
       "企业存续转型（湖北新华印务有限公司）；老厂区建筑遗存待核",
       "武汉市志工业志节核读（A级方志馆）；转型信息为摘录级；遗存未核验；坐标未核验保持待核。",
       ["华中新华印刷厂", "湖北新华印务"]),
    _r("HBI-WUHAN-104", "武汉油脂化学厂", "武汉市", "汉阳区月湖堤202号（志书作月湖路202号）", "化工工业", "research_candidate",
       "无法定遗产认定；武汉市志工业志节沿革（一枝花牌洗衣粉）",
       ["whfzg_gongyezhi_youzhi_huaxue"], "industrial_site", "溯源1909年福和油厂/1960年（改名）",
       "月湖堤厂区（已随琴台文化区改造消失——摘录级）与一枝花牌洗衣粉产品谱系（1985年产3.5万吨）",
       "从油脂加工到合成洗涤剂的日化工艺演进",
       "一枝花品牌的大众生活记忆与后改组武汉一枝花集团（摘录级）、企业注销的国企兴衰记忆",
       "厂区随月湖—琴台文化区改造消失（摘录级），按沿革条目收录，基本无实体遗存",
       "武汉市志工业志节核读（A级方志馆）；改组与厂区消失均为摘录级（汉阳区志/公众号）；坐标未核验保持待核。",
       ["福和油厂", "武汉一枝花集团"]),
    _r("HBI-WUHAN-105", "武汉食品厂（长江食品厂）", "武汉市", "汉口（志书未载详址）", "食品工业", "research_candidate",
       "无法定遗产认定；武汉市志工业志节沿革（国营糖果糕点工业）",
       ["whfzg_gongyezhi_shipin"], "industrial_site", "1951年（建社）/1958年（改国营）",
       "糖果糕点产品谱系（详址与厂区遗存待核）",
       "武汉国营糖果糕点工业化生产记忆",
       "1951年市合作社购置'小苏州'食品店建社、1958年改国营长江食品厂的食品工业社会主义改造记忆",
       "厂区下落待查",
       "武汉市志工业志节核读（A级方志馆）；同卷冠生园（1928年）、英商赞育汽水厂（1921年车站路9号）、和利汽水厂（岳飞街44号）线索留待后续轮；坐标未核验保持待核。",
       ["长江食品厂", "小苏州食品店"]),
]

# 既有记录口径修订（幂等：与目标值一致则跳过）
UPDATES = [
    {
        "id": "HBI-HS-059",
        "fields": {
            "material_carriers": "下陆区老下陆街168号现用厂区（人本黄石园区，2008年接续经营）；原黄石港区湖滨大道一带老厂地块已于2019年前拆除、原址建中商百货与黄石摩尔城——两地块关系与遗存边界待核",
            "current_use_or_loss": "下陆区现用厂区在产；黄石港区老厂地块已拆除建商业体；此前'2024年获拆迁补偿款'公示线索经区政府网站内核查未获原文，维持未核读",
            "notes": "人本官网核读（B级）确认前身与下陆区地址；2026-10-05月度复核修正口径：头条'黑镜头'2019-04-07标题级+黄石港区2024-03摩尔城安置房公示摘要级佐证老厂地块（黄石港区湖滨大道一带）已于2019年前拆除建中商百货/摩尔城——与下陆区168号现用厂区非同一地块；区政府网征收补偿栏7条均无轴承厂公示，'2024年获拆迁补偿款'线索维持未核读待函询；建厂年代待厂志补考；坐标未核验保持待核。",
        },
    },
    {
        "id": "HBI-JZ-077",
        "fields": {
            "district_county": "沙市区北京东路97号（省土壤修复名录2025年第七批核读）",
            "current_use_or_loss": "2020年12月30日老厂区全部关闭停产、主要反应装置已拆除（荆州日报2021核读）；2023年7月土壤修复实施中（沙市区政府核读）；截至2025-12-15省级名录口径北京东路97号地块'正在实施修复'、2023-12-28列入未移出",
            "notes": "荆州新闻网经头条转载核读（B级）；2026-10-05月度跟踪补强：修复节点链全部核读原文（2019年搬迁中→2020-12-30关停并拆主要反应装置→2023年土壤修复实施→2025-12省名录'正在实施修复'）；省名录同列'沙隆达（荆州）农药化工（原江陵农药厂）地块'（荆州区西环路）为另一地块勿混同；拆除改造总投资51.9亿元；下次按月复查。",
            "source_keys": ["toutiao_shalongda_banyun_2019", "jingzhou_zaixian_gaigaiban_2021", "shashi_quzhang_turang_xiufu_2023", "hubei_sthjt_turang_minglu_2025d7"],
        },
    },
    {
        "id": "HBI-JZ-079",
        "fields": {
            "district_county": "沙市区金龙路6号（方志类文章摘录，待核；另一口径为西区南湖）",
            "notes": "承继企业官网经r.jina.ai核读（B级）证实1952年始建与机电部定点磨床厂口径；2026-10-05志书核校：武汉方志馆书库无《沙市市志》、省地方志办在线版不可达，志书原文未命中，公众号原文仍被验证拦截——两套口径并列存注（'花在雾里'2026：695人/45233㎡/金龙路6号 vs '荆州记忆'2018：676人/45000㎡/西区南湖，或系不同年份统计口径）；刘珩（后任副省级领导）曾任该厂工程师（新华网2018讣告，摘要级旁证）；与在册沙市第一机床厂（HBI-JZ-078）、荆州机床厂（HBI-JZ-018）为独立企业；坐标未核验保持待核。",
            "source_keys": ["ssdejc_official", "jc35_dier_shop", "weixin_jingzhoujiyi_erjichuang_zhaiyao", "weixin_huazaiwuli_erjichuang_zhaiyao", "xinhuanet_liuheng_2018"],
        },
    },
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
    updated = 0
    for upd in UPDATES:
        rec = next((r for r in records if r["inventory_id"] == upd["id"]), None)
        if rec is None:
            raise SystemExit(f"update target missing: {upd['id']}")
        changed = False
        for field, value in upd["fields"].items():
            if rec.get(field) != value:
                rec[field] = value
                changed = True
        if changed:
            updated += 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_dn_S={len(S)} added={added} updated={updated} total={len(records)} src={len(sources)}")


if __name__ == "__main__":
    main()
