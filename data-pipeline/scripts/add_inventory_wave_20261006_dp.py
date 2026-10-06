from __future__ import annotations

import json
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"

S = {
    "landscape_minglu_2013": {
        "source_type": "official_media",
        "title": "武汉市首批工业遗产名录27处全表（landscape.cn转载2013年2月报道，经r.jina.ai核读）",
        "org": "景观中国（转载2013年报道）",
        "pub_date": "2013-02",
        "url": "https://landscape.cn/news/56829.html",
        "authority": "B",
        "notes": "27处全表：一级15处（均为文保单位）——汉口既济水塔1908、邦可面包房1930、南洋大楼1917、汉口电灯公司1905、和利汽水厂1918（岳飞街44号）、赞育汽水厂1937（洞庭街）、亚细亚火油公司1924（天津路1号）、平和打包厂旧址1905、宗关水厂1908、福新面粉厂1918、汉阳铁厂矿砂码头旧址1890、第一纱厂办公楼旧址1919、武汉重型机床厂（大门）1954、武汉轻型汽车厂办公楼1953、汉钢转炉车间旧址1952（汉阳龙灯堤特1号）；二级6处——武汉肉类联合加工厂1954、武汉铜材厂1958、青山红房子1955、南洋烟厂1926、武汉重型机床厂（厂房）1954、鹦鹉磁带厂1960；三级6处——太平洋肥皂厂1914、武汉市第一棉纺织厂1951、江岸车辆厂1901、汉阳特种汽车制造厂1959、武汉锅炉厂1956、武汉电视机总厂1980。经r.jina.ai代理核读。",
    },
    "sina_cuijin_2013": {
        "source_type": "official_media",
        "title": "武汉首批工业遗产名录27处（楚天金报2013-02-26胡诚，新浪新闻转载）",
        "org": "楚天金报（新浪新闻中心转载）",
        "pub_date": "2013-02-26",
        "url": "https://news.sina.com.cn/o/2013-02-26/073926360388.shtml",
        "authority": "B",
        "notes": "2013-02-25市政府常务会原则通过；一级15处=国保3+省保3+市保9（2013年时点文保等级口径）。经r.jina.ai代理核读（直连GB2312乱码）。",
    },
    "cnhubei_fenji_2022": {
        "source_type": "official_media",
        "title": "武汉首批工业遗产27处分级名单（武汉晚报2022-01-11，长江网转载）",
        "org": "武汉晚报/长江网",
        "pub_date": "2022-01-11",
        "url": "https://cnhubei.com/content/2022-01/11/content_14397911.html",
        "authority": "B",
        "notes": "27处分级名单双源之一（与landscape版互证）。经r.jina.ai代理核读。",
    },
    "wuhan_gov_pifu_2022": {
        "source_type": "city_government_portal",
        "title": "武汉市政府2013年5月批复《武汉市工业遗产保护与利用规划》并公布实施（长江日报，市政府网转载）",
        "org": "武汉市人民政府网（长江日报稿）",
        "pub_date": "2022-01-11",
        "url": "https://wuhan.gov.cn/sy/whyw/202201/t20220111_1893271.shtml",
        "authority": "A",
        "notes": "市政府2013年5月批复规划并公布实施（局网公开页2013-05-23）；名录以规划附录形式发布，无独立名录文号。原文核读。",
    },
    "hbtv_dierpi_2017": {
        "source_type": "official_media",
        "title": "武汉第二批工业遗产名单38处（长江日报2017-11-13/15，长江云转载：平和打包厂论坛宣布）",
        "org": "长江日报/长江云",
        "pub_date": "2017-11-15",
        "url": "http://news.hbtv.com.cn/p/1028690.html",
        "authority": "B",
        "notes": "2017-11-13市国土资源和规划局在'武汉工业遗产保护与再利用名师名匠高峰论坛'（平和打包厂）宣布第二批38处（一级5/二级9/三级24），新增桥梁、火车站、码头类（武汉长江大桥、大智门火车站、江汉一桥/二桥、三北轮船公司旧址、中铁大桥局办公楼、汉口美最时电灯厂、循礼门火车站、一冶重件码头、和平公园铁轨、青山公园铁轨等）；截至2026-10未见正式公布文件，完整名单缺口。直连核读。",
    },
    "whrd_faguiku_2026": {
        "source_type": "city_peoples_congress_portal",
        "title": "武汉人大网地方性法规库全库核读（2016-2026年区间无工业遗产专项条例——《武汉市工业遗产保护与利用条例》不存在之反证）",
        "org": "武汉市人民代表大会常务委员会",
        "pub_date": None,
        "url": "https://www.whrd.gov.cn/",
        "authority": "A",
        "notes": "法规库全7页逐页核读（经r.jina.ai代理，whrd.gov.cn直连被重置）：2016-2026年区间无工业遗产专项条例；市政府规章库检索'工业遗产'零结果；2017-11-15长江日报称相关条例'正在讨论中'，此后无颁布报道——武汉市级名录唯一依据是2013年市政府批复的规划。网络流传《武汉市工业遗产保护规定》文档无官方出处与文号，不采信。",
    },
    "guihua_wenku_29chu": {
        "source_type": "planning_document_mirror",
        "title": "《武汉市工业遗产保护与利用规划》文库版（'95处遗存中确定29处推荐名单'，比正式名录多绒印厂/毛纺织厂）",
        "org": "人人文库（规划文本镜像）",
        "pub_date": None,
        "url": "https://www.renrendoc.com/paper/87020278.html",
        "authority": "B",
        "notes": "文库版载29处推荐名单（一级15/二级6/三级8），比正式名录27处多出武汉绒印厂（1956）、武汉市毛纺织厂（1958）（列三级）；文档预览截断于附表前，附表2全表未获得。经r.jina.ai代理核读（预览级）。",
    },
    "zhoudawuhan_115_dianchi": {
        "source_type": "media_photo_essay",
        "title": "大武汉系列之115：武汉电池厂（重发布版：循礼门厂房改用大润发/蓝天歌剧院，2018年空置）",
        "org": "周国献/黑镜头（头条号）",
        "pub_date": None,
        "url": "https://www.toutiao.com/article/7543606422454485545/",
        "authority": "B",
        "notes": "1961年迁江汉路循礼门原宇宙烟厂集中生产；2000年因环保原因主体迁内环线外，原址留1条生产线，后厂房改为大润发超市和蓝天歌剧院（京汉大道店）；2018年2月拍摄时蓝天歌剧院已停业多年、大楼空置；2018年下半年（军运会前）外立面整饬一新；企业2000年改制组建新有限责任公司、年产3亿节电池大部分出口。原文核读。",
    },
    "zhoudawuhan_126_dengpao": {
        "source_type": "media_photo_essay",
        "title": "大武汉系列之126：武汉灯泡厂（厂区已拆建博文花园小区，灯泡厂小区宿舍存）",
        "org": "周国献/黑镜头（头条号）",
        "pub_date": None,
        "url": "https://www.toutiao.com/article/7546300495502033471/",
        "authority": "B",
        "notes": "武汉灯泡厂位于武昌马房山，今武昌区珞狮路洪达巷；2019年3月拍摄时厂区早已拆除，灯泡厂小区尚存，原厂址兴建博文花园商品房小区。原文核读。",
    },
    "fang_jinyang_xincheng": {
        "source_type": "property_platform",
        "title": "房天下'金阳新城'小区页（江岸区中山大道1541号，2011年竣工，4栋1256户）",
        "org": "房天下",
        "pub_date": None,
        "url": "https://www.fang.com/xiaoqu/wuhan-2610587546/",
        "authority": "B",
        "notes": "小区地址江岸中山大道1541号（三阳路区域），建筑年代2011-08-01，房屋总数1256户、4栋——志载武汉制革厂厂址现况。原文核读。",
    },
    "baike_wuhan_yinshua": {
        "source_type": "encyclopedia_entry",
        "title": "百度百科'武汉印刷厂'词条（引《武汉市志·工业志(下)》《江汉区志》：已停用，载入地方志）",
        "org": "百度百科",
        "pub_date": None,
        "url": "https://baike.baidu.com/item/武汉印刷厂/61348864",
        "authority": "B",
        "notes": "自建国初期至20世纪70年代末持续运营，20世纪后期停止运营后作为产业文化遗产载入《武汉市志》工业卷，现状标注'已停用'。原文核读。",
    },
    "baike_so_wanhong": {
        "source_type": "encyclopedia_entry",
        "title": "360百科'万鸿集团'词条（长印股份1993年上市→诚成文化→万鸿集团沿革全链）",
        "org": "360百科",
        "pub_date": None,
        "url": "https://baike.so.com/doc/2217209-2346088.html",
        "authority": "B",
        "notes": "1993年10月18日'长印股份'上交所上市（600681），1998年国家股转让海南诚成，1999年更名'诚成文化'，2003年更'奥园发展'，2003年底更'万鸿集团'。原文核读；'由原武汉印刷厂、京华信托、深圳万科发起组建武汉长印集团（1992）'为多源摘录一致。",
    },
    "jc001_zhuangshicheng": {
        "source_type": "industry_platform",
        "title": "九正建材网'武汉装饰城'市场页（民意四路与利东街交汇处，诚成文化全额投资兴建）",
        "org": "九正建材网",
        "pub_date": None,
        "url": "https://shop.jc001.cn/market/1642.html",
        "authority": "B",
        "notes": "武汉装饰城由武汉诚成文化投资集团股份有限公司全额投资兴建，位于汉口民意四路和利东街交汇处，占地1.2万平方米、经营面积近3万平方米，商户200余家——武汉印刷厂民意四路101号原厂区1998年改建用途（现址同名，摘录级）。原文核读。",
    },
    "zhoudawuhan_124_xinhua": {
        "source_type": "media_photo_essay",
        "title": "大武汉系列之124：湖北省新华印刷厂（2001年改制新华印务，2014年迁长风路31号，老厂区出租）",
        "org": "周国献/黑镜头（头条号）",
        "pub_date": None,
        "url": "https://www.toutiao.com/article/7591865028505027081/",
        "authority": "B",
        "notes": "位于硚口区解放大道145号；2001年1月组建湖北新华印务有限公司；2014年底整体搬迁至硚口区长风路31号新厂区；2017年6月拍摄时厂房已出租给多家私营企业；2019年2月再访，俱乐部变身汽车服务公司、书品精装车间变身乒乓球馆。原文核读。",
    },
    "cjcb_xinhua_2023": {
        "source_type": "enterprise_official_site",
        "title": "长江出版传媒官网：新华产业园中间园区简易维修改造竞争性谈判公告（2023-12-21，原新华印刷厂生产办公区5.5万㎡）",
        "org": "湖北长江出版传媒集团",
        "pub_date": "2023-12-21",
        "url": "https://www.cjcb.com.cn/contents/219/56538.html",
        "authority": "A",
        "notes": "'新华产业园整个中间园区——原湖北省新华印刷厂生产、办公区（解放大道131号、145号），建筑面积约5.5万平方米……因房屋年代久远、消防水电不达标，须完成简易维修改造，满足已签约客商入驻运营'；采购人湖北省新华印刷产业园有限公司地址即解放大道145号。原文核读。",
    },
    "toutiao_changjiang_shipin": {
        "source_type": "media_photo_essay",
        "title": "武汉长江食品厂（头条专文：武胜路2号，1951年8月始建，1992年改办汉正街食品专业市场）",
        "org": "头条号",
        "pub_date": None,
        "url": "https://www.toutiao.com/article/7220595054795244092/",
        "authority": "B",
        "notes": "全民所有制企业，厂址武胜路2号，始建于1951年8月；1992年利用厂房开办汉正街长江食品专业市场（160摊位、临街40门点）；1997年5月划转硚口区管理；2000年企业改制组建长江食品有限责任公司（改制前资产2025.33万元、负资产3134万元）。原文核读。",
    },
    "baike_changjiang_shipin": {
        "source_type": "encyclopedia_entry",
        "title": "百度百科'武汉市长江食品厂'词条（载中国国家地名信息库：1951年合作社购小苏州食品店建，2013年原厂址旧改拆除）",
        "org": "百度百科（引中国国家地名信息库）",
        "pub_date": None,
        "url": "https://baike.baidu.com/item/武汉市长江食品厂/61343246",
        "authority": "B",
        "notes": "1951年8月武汉市合作社买下1946年创建的私营小苏州食品店成立合作社食品厂；1958年更名武汉市长江食品厂转国营；1992年厂房改建为汉正街长江食品专业市场；2013年原厂址因旧城（棚户区）改造拆除。原文核读。",
    },
    "zrzyhgh_hanzhengjie_2025": {
        "source_type": "city_government_portal",
        "title": "市自然资源和城乡建设局：秦军副局长带队前往汉正街片区开展调研（2025-02-13活动，长江食品厂A2B地块为重点项目）",
        "org": "武汉市自然资源和城乡建设局",
        "pub_date": "2025-09-12",
        "url": "https://zrzyhgh.wuhan.gov.cn/fjzrzyhcxjsj_101415/zwdt/gzdt/202509/t20250912_2646979.shtml",
        "authority": "A",
        "notes": "调研分别前往天翔灯饰城地块、新华书店片、长江食品厂A2B地块等重点项目所在地，聚焦'开工难'等问题。原文核读。",
    },
    "toutiao_changshi_zhengchai_2026": {
        "source_type": "official_media",
        "title": "盘点！武汉因缺钱而推进困难的征拆项目（转引武汉城市留言板2026-01-09官方回复：长食片花样年违约停滞、2025年三年行动计划重启）",
        "org": "头条号（转引城市留言板官方回复）",
        "pub_date": None,
        "url": "https://www.toutiao.com/article/7597627842561606184/",
        "authority": "B",
        "notes": "'长食片项目因花样年集团2021年10月4日美元债违约等资金链问题被迫停滞。2025年5月硚口区制订《汉正街转型升级三年行动计划（2025-2027年）》，责成区住更局等研究盘活路径，重启地块建设。'原文核读。",
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
    _r("HBI-WUHAN-109", "汉钢转炉车间旧址（汉阳钢铁厂）", "武汉市", "汉阳区龙灯堤特1号", "冶金工业", "municipal",
       "武汉市首批工业遗产一级（2013年市政府批复《武汉市工业遗产保护与利用规划》附名录27处之一）；名录口径为市级文物保护单位",
       ["wuhan2013", "wuhan_plan", "landscape_minglu_2013", "cnhubei_fenji_2022", "sina_cuijin_2013"], "industrial_site", "1952年（'一五'时期）",
       "汉阳龙灯堤转炉车间旧址建筑（本体保存状态待现场核验）",
       "武汉地方钢铁工业转炉炼钢工艺记忆（汉阳钢铁厂）",
       "从张之洞汉阳铁厂到新中国汉阳钢铁厂的地方钢铁工业百年传承记忆",
       "2013年名录一级身份确认；现状待核",
       "2013年第一批27处名录一级第15项（landscape.cn全表经r.jina.ai核读B+武汉晚报2022分级名单核读B+楚天金报2013经新浪核读B）；与在册汉冶萍系列（HBI-WUHAN-001、HBI-HS-001）为不同历史时期主体；市级文保等级待文保名录正式核对；遗存本体未核验；坐标未核验保持待核。",
       ["汉阳钢铁厂"]),
    _r("HBI-WUHAN-110", "武汉绒印厂", "武汉市", "武汉市（地址待规划附表核补）", "纺织工业", "research_candidate",
       "《武汉市工业遗产保护与利用规划》推荐名单（29处版三级，未列入正式公布27处名录）",
       ["guihua_wenku_29chu"], "industrial_site", "1956年",
       "绒线印花纺织厂区（遗存待核）",
       "绒线印花工艺记忆",
       "武汉轻纺工业体系记忆",
       "现状待核",
       "规划文库版载'95处遗存中确定29处推荐名单'（一级15/二级6/三级8），比正式名录27处多出绒印厂与毛纺织厂两项（列三级）；文库预览截断未得附表2全表，地址与详情待规划正式文本核对；坐标未核验保持待核。",
       []),
    _r("HBI-WUHAN-111", "武汉市毛纺织厂", "武汉市", "武汉市（地址待规划附表核补）", "纺织工业", "research_candidate",
       "《武汉市工业遗产保护与利用规划》推荐名单（29处版三级，未列入正式公布27处名录）",
       ["guihua_wenku_29chu"], "industrial_site", "1958年",
       "毛纺织厂区（遗存待核）",
       "毛纺织工艺记忆",
       "武汉轻纺工业体系记忆",
       "现状待核",
       "规划文库版29处推荐名单（三级）之一，正式名录27处未含；文库预览截断未得附表2全表，地址与详情待规划正式文本核对；坐标未核验保持待核。",
       []),
]

DELETES = ["HBI-WUHAN-107", "HBI-WUHAN-108"]

# 修订（幂等）：010/015/028合并第105轮重复条目证据；6厂补下落
UPDATES = [
    {
        "id": "HBI-WUHAN-010",
        "fields": {
            "district_county": "江岸区岳飞街44号（购厂合同与省住建厅作42号，以名录44号为主并注）",
            "asset_kind": "industrial_building",
            "aliases": ["和利冰厂", "汉口英商和利冰厂", "和利汽水厂旧址", "国营武汉饮料二厂", "汉口二厂"],
            "cultural_evidence": {
                "material_carriers": "岳飞街44号两层法国古典主义砖木建筑（2003/2005年曾租用后整栋封闭保存）；制冰与汽水生产空间（冰厂与汽水厂分址疑点：据科赛恩嫡孙考证44号实为汽水厂、冰厂在岳飞街24-26号）",
                "technical_memory": "汉口机器制冰与碳酸汽水生产发端（市志：'以和利汽水最为著名'）；滨江牌商标1975年起用，滨江牌中华猕猴桃晶1978年投产、1983年获国家银质奖",
                "social_memory": "英商柯三（科赛恩）创业与1938年售予华商刘耀堂、1945年复业并购赞育、1952年改制国营武汉饮料二厂的民族资本替代链；'汉口二厂'汽水城市记忆（2017年品牌复刻）",
                "current_use_or_loss": "1949年后改制国营武汉饮料二厂（约2000年停产于解放大道1503号）；岳飞街44号建筑整栋封闭保存，武汉市首批工业遗产一级+省保+市第四批优秀历史建筑（2007，二级保护）多重身份",
            },
            "notes": "武汉汽水工业与二厂汽水品牌记忆的重要入口。2026-10-06补强并合并第105轮重复入库条目：市志沿革节/饮料节核读（A级）——1921年开始生产碳酸汽水以和利最著名、1975年改滨江牌、猕猴桃晶1983年国家银质奖；维基汉口和利冰厂词条核读（B级）——冰厂1904年开业（一说1891年柯三克鲁奇合资20万元）、汽水厂1917年3月苏格兰人科赛恩（柯三）建、1938年售华商刘耀堂；省住建厅2017年文核读（A级）——1922年建成投产（岳飞街42号）、1945年刘耀堂返汉复业并购赞育、1952年改名国营武汉饮料二厂、约2000年解放大道1503号停产、2017年'汉口二厂'品牌复刻；网易2016核读——44号建筑整栋封闭保存；建厂年代诸说（1891/1904/1911/1917/1918/1921/1922）按来源并注，门牌42/44并存以名录44号为主；同对象省保条目另见HBI-WUHAN-028（公布名'汉口英商和利冰厂旧址'，时代1911）；坐标未核验保持待核。",
            "source_keys": ["wuhan2013", "wuhan_plan", "whfzg_gongyezhi_shipin", "whfzg_gongyezhi_yinliao", "wikipedia_heli_bingchang", "163_heli_2016", "zjt_erbanchiqishui_2017", "wikipedia_wuhan_4th_lishi"],
        },
    },
    {
        "id": "HBI-WUHAN-015",
        "fields": {
            "district_county": "江岸区洞庭街103-105号（车站路路口；市志作今车站路9号并注）",
            "aliases": ["汉口赞育药房", "汉口赞育药房旧址", "汉口赞育汽水公司", "赞育汽水厂旧址", "汉口赞育汽水厂", "Hankow Dispensary"],
            "notes": "同一处江岸区洞庭街103—105号建筑与企业谱系在不同名录中分别以'汉口赞育药房'和'赞育汽水厂'出现，合并为一条主档案避免重复计数。湖北省1098处名录确认1913年汉口赞育药房，武汉市工业遗产名录和优秀历史建筑文件确认赞育汽水厂；地方媒体与武汉地方文化出版资料进一步记录1918年收购汽水车间、机械化生产，以及药品、化工、汽水、制冰和相关设备经营范围。2012年火灾报道提示本体保存风险，建筑保护范围与控制地带以鄂政办发〔2017〕68号为准；镜像文件中的具体方向距离发布前仍需从省政府原始附件复核。2026-10-06合并第105轮重复入库条目并补强：市志沿革节核读（A级）——1921年英商柯三开办赞育汽水厂（今车站路9号门牌与本条并注）；市志饮料节核读（A级）——1975年改滨江牌商标；省住建厅2017年文核读（A级）——1918年英商收购法商碳酸汽水厂创办汉口赞育汽水厂（洞庭街103号），为武汉首家机器制汽水厂，1945年刘耀堂返汉复业后并购赞育；维基汉口赞育药房词条核读（B级）——1910年华生（屈臣氏系）汉口分店、1918年收购法商那加利汽水车间、1948年倒闭被华资和利收购、1949年底彻底停产、2012年火灾烧穿楼顶；建厂年代1918/1921两说并注，创办人'柯三'与维基赫伯特·詹姆斯·林人名口径冲突并注；2007年列武汉市第四批优秀历史建筑（序号11，1937年前，二级保护）。",
            "source_keys": ["chinanews_zanyu_fire_2012", "hubei_boundary_2017_wlt", "hubei_provincial_relics_1098", "whcbs_zanyu_economic_history_2020", "wuhan2013", "wuhan_historical_buildings_2023", "wuhan_plan", "wuhan_zanyu_boundary_2017_mirror", "wuhan_zanyu_history_2012", "whfzg_gongyezhi_shipin", "whfzg_gongyezhi_yinliao", "wikipedia_zanyu_yaofang", "zjt_erbanchiqishui_2017", "wikipedia_wuhan_4th_lishi"],
        },
    },
    {
        "id": "HBI-WUHAN-028",
        "fields": {
            "aliases": ["和利冰厂", "和利汽水厂"],
            "notes": "省级名录确认汉口英商和利冰厂旧址为1911年近现代工业建筑；省文物部门公开说明第一至六批省保保护范围已按鄂政办发〔2017〕68号划定。本条暂保留省保公布名与和利冰厂/汽水厂企业谱系疑点，冰厂与汽水厂的分址、设备、产权和现状需专项测绘与档案核验。2026-10-06补强：维基汉口和利冰厂词条核读（B级）——2007-03-09列武汉市第四批优秀历史建筑（'和利冰厂'，年代标注1918，二级保护），2013年以'和利汽水厂'列入武汉市第一批工业遗产名录（一级）；据科赛恩嫡孙考证岳飞街44号实为汽水厂、冰厂在岳飞街24-26号；44号为两层法国古典主义砖木结构、整栋封闭保存；本省保条目与市名录条目（HBI-WUHAN-010）为同一对象的双身份分立。",
            "source_keys": ["hubei_boundary_2017_wlt", "hubei_provincial_relics_1098", "wikipedia_heli_bingchang"],
        },
    },
    {
        "id": "HBI-WUHAN-098",
        "fields": {
            "current_use_or_loss": "2000年因环保原因主体迁内环线外并改制，原址仅留1条生产线；循礼门厂房后改用为大润发超市与蓝天歌剧院（京汉大道店），2018年2月探访时蓝天歌剧院已停业多年、大楼空置，同年下半年（军运会前）外立面整饬一新——建筑本体存续、空置",
            "notes": "武汉市志工业志节核读（A级方志馆）；厂区现状与遗存未核验，后续经城市留言板/长报档案补查；坐标未核验保持待核。2026-10-06下落补查：周国献大武汉系列之115（重发布版）核读（B级）证实循礼门厂房改用大润发/蓝天歌剧院、2018年空置、军运会前外立面整饬；企业2000年改制组建新有限责任公司、年产3亿节电池大部分出口（同源）。",
            "source_keys": ["whfzg_gongyezhi_dianchi", "zhoudawuhan_115_dianchi"],
        },
    },
    {
        "id": "HBI-WUHAN-099",
        "fields": {
            "district_county": "洪山区珞狮路洪达巷（志书作武昌马房山，实属珞狮路一带）；灯泡厂小区（宿舍）地名存续",
            "current_use_or_loss": "厂区早已拆除，原址兴建博文花园商品房小区；'灯泡厂小区'（宿舍）地名存续；珞狮路24号尚有同名注册主体（爱企查摘录级，经营状态未核）",
            "notes": "武汉市志工业志节核读（A级方志馆）；遗存未核验；坐标未核验保持待核。2026-10-06下落补查：周国献大武汉系列之126核读（B级）证实厂区已拆建博文花园小区、灯泡厂小区宿舍存续；志书'武昌马房山'与该文'珞狮路洪达巷'实为同一片区（洪山区），district_county已按此考订。",
            "source_keys": ["whfzg_gongyezhi_dengpao", "zhoudawuhan_126_dengpao"],
        },
    },
    {
        "id": "HBI-WUHAN-101",
        "fields": {
            "current_use_or_loss": "志载厂址中山大道1541号（三阳路轻轨站旁）现即2011年竣工的金阳新城住宅小区（4栋1256户，房天下核读），老厂建筑已不存（拆除时间无直接记载）；疑似承接体武汉皮革工业有限公司（1991年，江岸区光荣村18号，存续——企查查摘录级，承接关系无直接文本证实）",
            "notes": "武汉市志工业志节核读（A级方志馆）；遗存未核验；坐标未核验保持待核。2026-10-06下落补查：房天下金阳新城小区页核读（B级）坐实原址现为2011年住宅小区；同批核读的红星制革厂（江岸区汉黄路23号，1958年由第一/三/四/五制革社等合并，厂房基本保存完好出租——网易转载核读B级）为另一支系非本厂，已排除混淆；大武汉系列1-300总索引核读无本厂专篇。",
            "source_keys": ["whfzg_gongyezhi_zhige", "fang_jinyang_xincheng"],
        },
    },
    {
        "id": "HBI-WUHAN-102",
        "fields": {
            "current_use_or_loss": "企业1992年改组武汉长印（集团）公司→1993年'长印股份'上交所上市（600681）→1999年更名诚成文化→2003年更名万鸿集团，印刷主业退出；民意四路101号原厂区1998年改建为武汉装饰城（建材市场，占地1.2万㎡、经营面积近3万㎡，诚成文化全额投资兴建）——市场主体现存（九正建材核读）",
            "notes": "武汉市志工业志节核读（A级方志馆）；遗存未核验；坐标未核验保持待核。2026-10-06下落补查：百度百科武汉印刷厂词条核读（B级，引《武汉市志》《江汉区志》）+360百科万鸿集团词条核读（B级，上市壳沿革全链）+九正建材武汉装饰城页核读（B级）；'由原武汉印刷厂等发起组建武汉长印集团（1992）'为多源摘录一致。",
            "source_keys": ["whfzg_gongyezhi_yinshua_wuhan", "baike_wuhan_yinshua", "baike_so_wanhong", "jc001_zhuangshicheng"],
        },
    },
    {
        "id": "HBI-WUHAN-103",
        "fields": {
            "district_county": "硚口区解放大道131/145号（志书作79号，门牌考订待核；2014年迁长风路31号）",
            "current_use_or_loss": "2001年1月组建湖北新华印务有限公司（长江出版传媒旗下），2014年底整体搬迁硚口区长风路31号；解放大道131/145号老厂区约5.5万㎡建筑未拆除，整体转为'新华产业园'对外出租招商（2023年12月仍在实施简易维修改造满足客商入驻——长江出版传媒公告核读A级）；2017-2019年影像：厂房分租私营企业、俱乐部变汽车服务公司、精装车间变乒乓球馆",
            "notes": "武汉市志工业志节核读（A级方志馆）；转型信息为摘录级；遗存未核验；坐标未核验保持待核。2026-10-06下落补查：周国献大武汉系列之124核读（B级）+长江出版传媒官网新华产业园维修改造公告核读（A级，2023-12-21，载原厂区解放大道131/145号、建筑面积约5.5万㎡）；门牌考订：志书79号与现行131/145号并存待核；湖北省国资委2026-07来信称该厂为'重要工业遗产'（页面拦截仅摘录级）。",
            "source_keys": ["whfzg_gongyezhi_xinhua_yinshua", "zhoudawuhan_124_xinhua", "cjcb_xinhua_2023"],
        },
    },
    {
        "id": "HBI-WUHAN-105",
        "fields": {
            "district_county": "硚口区武胜路2号（志书未载详址，经核读补正）",
            "current_use_or_loss": "1992年利用厂房开办汉正街长江食品专业市场（160摊位、临街40门点）；1997年划转硚口区管理；2000年改制组建长江食品有限责任公司（资不抵债背景）；2013年原厂址因旧城（棚户区）改造拆除；地块分片开发——长食片项目因开发商花样年2021年美元债违约停滞，2025年5月硚口区制订《汉正街转型升级三年行动计划（2025-2027年）》重启盘活，A2B地块2025年仍由市、区两级协调（市局调研核读）",
            "notes": "武汉市志工业志节核读（A级方志馆）；同卷冠生园（1928年）、英商赞育汽水厂（1921年车站路9号）、和利汽水厂（岳飞街44号）线索已分别入库（WUHAN-106/015/010）。2026-10-06下落补查：头条武汉长江食品厂专文核读（B级，武胜路2号/1951年8月始建）+百度百科武汉市长江食品厂词条核读（B级，引中国国家地名信息库：2013年拆除）+市自然资源和城乡建设局汉正街调研报道核读（A级，2025-09-12发布）+头条征拆困难项目盘点核读（B级，转引城市留言板2026-01-09官方回复：花样年违约停滞与三年行动计划重启）；坐标未核验保持待核。",
            "source_keys": ["whfzg_gongyezhi_shipin", "toutiao_changjiang_shipin", "baike_changjiang_shipin", "zrzyhgh_hanzhengjie_2025", "toutiao_changshi_zhengchai_2026"],
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
    removed = 0
    ids = set(DELETES)
    kept = [r for r in records if r["inventory_id"] not in ids]
    removed = len(records) - len(kept)
    data["records"] = kept
    records = kept
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
    print(f"wave_dp_S={len(S)} added={added} removed={removed} updated={updated} total={len(records)} src={len(sources)}")


if __name__ == "__main__":
    main()
