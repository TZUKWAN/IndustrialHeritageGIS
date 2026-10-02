from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "miit_batch4_notice_gov_2020": {
        "source_type": "government_notice",
        "title": "工业和信息化部关于公布第四批国家工业遗产名单的通告（工信部政法函〔2020〕348号）",
        "org": "工业和信息化部（中国政府网政策文件库）",
        "pub_date": "2020-12-17",
        "url": "https://www.gov.cn/zhengce/zhengceku/2020-12/27/content_5573790.htm",
        "authority": "A",
        "notes": "通告正文载明第四批国家工业遗产名单经申报、推荐、专家评审、现场核查和网上公示程序确定，2020年12月17日公布；名单见附件doc，已下载核读。",
    },
    "miit_batch4_list_attachment_2020": {
        "source_type": "government_notice_attachment",
        "title": "国家工业遗产名单（第四批附件，doc）",
        "org": "工业和信息化部（中国政府网政策文件库附件）",
        "pub_date": "2020-12-17",
        "url": "https://www.gov.cn/zhengce/zhengceku/2020-12/27/5573790/files/549c755129574a489d5a3750f0aed3a4.doc",
        "authority": "A",
        "notes": "已下载核读附件全表：序号42为湖北省咸宁市赤壁市湖北省赵李桥茶厂，核心物项为青砖生产线厂房，推斗机、开栓机、取帽机、预压机、主压机、出砖机和斗模流转线，复制车间厂房，老复制主料生产线，烘包车间，原料第2号仓库、原料第3号仓库；同批湖北另有葛洲坝水利枢纽（序号40）与二三四八蒲纺总厂（序号41）。本地存档 raw/national_batch4/miit_batch4_list.doc。",
    },
    "zhao_liqiao_official_site": {
        "source_type": "enterprise_official_site",
        "title": "公司介绍_湖北省赵李桥茶厂有限责任公司",
        "org": "湖北省赵李桥茶厂有限责任公司官网",
        "pub_date": None,
        "url": "https://www.brick-tea.com/list_9.html",
        "authority": "B",
        "notes": "企业官网自述：前身是将建国前复兴茶厂、义兴茶行、聚兴顺茶行等接收后成立的中国茶业公司羊楼洞砖茶厂，1953年迁址赵李桥镇更名中国茶业公司赵李桥茶厂，2008年改制为湖北省赵李桥茶厂有限责任公司（湖北省茶业集团成员企业）；川字牌青砖茶与火车头牌、牌坊牌米砖茶；荣誉谱系含1993年国内贸易部中华老字号、2014年国家级非遗保护单位、2020年12月国家工业遗产、2022年11月人类非遗；地址赤壁市赵李桥镇前进街25号。企业自述内容以官方认定文件互证为准。",
    },
    "xianning_gov_zhao_liqiao_2025": {
        "source_type": "municipal_government_news",
        "title": "老技艺有了新味道 赵李桥茶厂川字牌青砖茶饮料上线",
        "org": "咸宁市人民政府门户网站",
        "pub_date": "2025-07-14",
        "url": "http://www.xianning.gov.cn/xwzx/xssm/202507/t20250714_4024286.shtml",
        "authority": "A",
        "notes": "市政府网报道2025年7月4日赵李桥茶厂新品发布会暨赤壁青砖茶产业创新研究院成立仪式在中国青砖茶博物馆举行，川字牌青砖茶饮料已有意向订单200万瓶；赤壁为万里茶道源头、青米砖茶文化发祥地；赤壁市每年财政列支青砖茶产业专项资金3000万元、设立2亿元产业基金、研发30余类360多款创新产品。",
    },
    "miit_batch6_notice_2024": {
        "source_type": "government_notice",
        "title": "工业和信息化部关于公布第六批国家工业遗产及通过复核的第一批、第二批国家工业遗产名单的通知（工信部政法函〔2024〕301号）",
        "org": "工业和信息化部产业政策与法规司",
        "pub_date": "2024-10-24",
        "url": "https://www.miit.gov.cn/zwgk/zcwj/wjfb/tz/art/2024/art_fb72ba03c3f441a28ed521c4debc492a.html",
        "authority": "A",
        "notes": "通知成文2024年10月22日、发布2024年10月24日，公布第六批国家工业遗产名单及通过复核的第一批、第二批名单；附件1第六批名单PDF已在工信部官网核读。",
    },
    "miit_batch6_list_attachment_2024": {
        "source_type": "government_notice_attachment",
        "title": "第六批国家工业遗产名单（附件1，PDF）",
        "org": "工业和信息化部",
        "pub_date": "2024-10-22",
        "url": "https://www.miit.gov.cn/cms_files/filemanager/1226211233/attach/202410/37ba3ea37aac48918132977ad3d16416.pdf",
        "authority": "A",
        "notes": "已下载核读13页名单PDF全表：序号25为湖北省武汉市青山区一米七轧机工程（申请名称武钢一米七产线），核心物项为“一米七”产线（加热炉、粗轧机、精轧机、卷取机），一次试轧成功纪念碑及首次轧制钢卷样品，历史照片、领导题词、获奖证书、厂志、通知批复、工程文件、技术手册等档案资料；申请单位武汉钢铁有限公司。同批湖北另有三线航天066导弹基地旧址（序号26）。本地存档 raw/national_batch6/miit_batch6_list.pdf。",
    },
    "hubei_daily_batch6_2024": {
        "source_type": "official_media",
        "title": "工信部公布第六批国家工业遗产名单 湖北新增2项",
        "org": "湖北日报",
        "pub_date": "2024-10-27",
        "url": "https://news.hubeidaily.net/mobile/c_3268467.html",
        "authority": "B",
        "notes": "湖北日报讯确认第六批37项中湖北新增武钢一米七产线（武汉市青山区）与三线航天066导弹基地旧址（宜昌市远安县）两项；通过复核的第一、二批名单含汉冶萍公司-大冶铁厂、铜绿山古铜矿遗址；湖北自2017年第一批大冶铁厂起持续有对象入选国家工业遗产。",
    },
    "xinhua_wisco_tourism_4a_2025": {
        "source_type": "official_media",
        "title": "武汉青山武钢文化旅游区获评国家4A级旅游景区",
        "org": "新华网湖北频道",
        "pub_date": "2025-12-23",
        "url": "http://www.hb.xinhuanet.com/20251223/4a7a0bd60cb84449a35f9efe7872acb6/c.html",
        "authority": "A",
        "notes": "新华网报道湖北省文化和旅游厅2025年12月19日公告武钢文化旅游区获评国家4A级旅游景区；景区依托一号高炉、一米七工程、中国硅钢摇篮等核心资源，红色钢城文化之旅线路依托一号高炉与一米七轧机工程；武钢一号高炉、一米七轧机工程分别于2021年、2024年获评国家工业遗产，景区2023年获评国家工业旅游示范基地、2018年6月对外开放。",
    },
}


RECORDS = [
    {
        "inventory_id": "HBI-XN-017",
        "name": "湖北省赵李桥茶厂",
        "city": "咸宁市",
        "district_county": "赤壁市",
        "industry_category_l1": "茶叶加工工业",
        "recognition_level": "national_heritage_related",
        "recognition_status": "第四批国家工业遗产（工信部政法函〔2020〕348号，2020年12月17日公布，名单序号42）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": [
            "miit_batch4_notice_gov_2020",
            "miit_batch4_list_attachment_2020",
            "zhao_liqiao_official_site",
            "xianning_gov_zhao_liqiao_2025",
        ],
        "related_heritage_ids": ["HER-61bb352b4593"],
        "cultural_evidence": {
            "material_carriers": "第四批国家工业遗产核心物项：青砖生产线厂房，推斗机、开栓机、取帽机、预压机、主压机、出砖机和斗模流转线，复制车间厂房，老复制主料生产线，烘包车间，原料第2号仓库、原料第3号仓库；厂区位于赤壁市赵李桥镇前进街25号",
            "technical_memory": "黑茶制作技艺（赵李桥砖茶制作技艺）2014年列入国家级非物质文化遗产代表性项目名录，茶厂为该技艺保护单位；2022年11月赵李桥砖茶制作技艺入选联合国教科文组织人类非物质文化遗产代表作名录；川字牌青砖茶压制技艺据企业自述跨越三个世纪",
            "social_memory": "前身为接收建国前复兴茶厂、义兴茶行、聚兴顺茶行等成立的中国茶业公司羊楼洞砖茶厂，1953年迁址赵李桥镇更名中国茶业公司赵李桥茶厂，2008年改制为湖北省赵李桥茶厂有限责任公司；川字牌青砖茶与火车头牌、牌坊牌米砖茶畅销全国并远销海外；1990年、1994年、2019年多次获全国民族团结进步荣誉，砖茶边疆贸易与民族团结记忆贯穿厂史",
            "current_use_or_loss": "改制后持续生产，据企业自述为湖北省最大单体紧压砖茶生产基地（占地12万平方米、6条砖茶生产线）；2025年联合赤壁青砖茶产业创新研究院推出川字牌青砖茶饮料；赤壁市以专项资金、产业基金和中国青砖茶博物馆支撑青砖茶产业活化；第四批核心物项建筑的本体保存、产权与开放条件待现场核验",
        },
        "notes": "全国主表与前端站点数据已含该对象（HER-61bb352b4593，第四批2020年）；本底册记录补充研究级四项文化证据与可追溯来源绑定。同批湖北入选对象葛洲坝水利枢纽、二三四八蒲纺总厂已有底册记录。核心物项建筑保存现状与产权边界待现场核验；坐标未核验保持待核。",
        "aliases": ["中国茶业公司羊楼洞砖茶厂", "中国茶业公司赵李桥茶厂", "湖北省赵李桥茶厂有限责任公司"],
        "asset_kind": "industrial_site",
    },
    {
        "inventory_id": "HBI-WUHAN-069",
        "name": "一米七轧机工程",
        "city": "武汉市",
        "district_county": "青山区",
        "industry_category_l1": "钢铁工业",
        "recognition_level": "national_heritage_related",
        "recognition_status": "第六批国家工业遗产（工信部政法函〔2024〕301号，2024年10月22日成文、10月24日发布，名单序号25；申请名称武钢“一米七”产线）",
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": [
            "miit_batch6_notice_2024",
            "miit_batch6_list_attachment_2024",
            "hubei_daily_batch6_2024",
            "xinhua_wisco_tourism_4a_2025",
        ],
        "related_heritage_ids": ["HER-7eefab99baa1"],
        "cultural_evidence": {
            "material_carriers": "第六批国家工业遗产核心物项：“一米七”产线（加热炉、粗轧机、精轧机、卷取机），一次试轧成功纪念碑及首次轧制钢卷样品，历史照片、领导题词、获奖证书、厂志、通知批复、工程文件、技术手册等档案资料；申请单位武汉钢铁有限公司",
            "technical_memory": "产线加热炉、粗轧机、精轧机、卷取机四机组连续轧制工艺；入选档案资料含工程文件、技术手册、获奖证书与通知批复，完整技术引进与建设谱系以厂志及工程档案为准，待进一步核验补充",
            "social_memory": "一次试轧成功纪念碑与首次轧制钢卷样品承载武钢建设者与技术人员集体记忆；领导题词、厂志与历史照片构成“十里钢城”职工社会记忆的档案载体；武钢素有新中国钢铁长子之称的语境下，一米七工程为青山区工业社区共同记忆组成部分",
            "current_use_or_loss": "2024年获评国家工业遗产后纳入武钢文化旅游区（2018年6月对外开放，2023年获评国家工业旅游示范基地，2025年12月武钢文化旅游区获评国家4A级旅游景区）；红色钢城文化之旅线路依托一号高炉与一米七轧机工程开展钢铁发展史展示与传统教育；产线本体位于武汉钢铁有限公司厂区内，参观边界与开放条件以景区管理方为准",
        },
        "notes": "全国主表与前端站点数据已含该对象（HER-7eefab99baa1，第六批2024年）；本底册记录补充研究级四项文化证据与可追溯来源绑定。同批湖北另一入选对象三线航天066导弹基地旧址已有底册记录（HBI-YC-018）。核心物项产线设备的在用/停用状态、保存边界与产权以武汉钢铁有限公司为准，待现场核验；坐标未核验保持待核。",
        "aliases": ["武钢“一米七”产线", "一米七产线"],
        "asset_kind": "industrial_site",
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
    print(f"wave_as_sources={len(SOURCES)} added_records={added} updated_records=0 total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
