from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "luotian_silk_yongxing_2022": {
        "source_type": "third_party_enterprise_directory",
        "title": "罗田县永兴茧丝有限责任公司工商信息（大河岸镇永兴街63号，经营范围首项缫丝）",
        "org": "搜了网企业目录",
        "pub_date": None,
        "url": "https://www.51sole.com/company/detail_13729436.html",
        "authority": "C",
        "notes": "载明罗田县永兴茧丝有限责任公司注册地址大河岸镇永兴街63号（2002年注册、注册资本50万元、规模175人、经营范围首项缫丝、状态吊销）；顺企网另见大河岸镇缫丝厂预制板厂（1998年，大河岸镇永兴街，行业标注缫丝厂）反证母体大河岸缫丝厂位于永兴街；罗田县缫丝有限责任公司（凤山镇义水北路383号）为县缫丝厂法人化主体。多源C级一致，厂址语境坐实。",
    },
    "yingshan_zhisi_wenquan_41": {
        "source_type": "third_party_enterprise_directory",
        "title": "湖北制丝针织厂企业信息（温泉镇温泉路41号，主营白厂丝与针织）",
        "org": "顺企网企业目录",
        "pub_date": None,
        "url": "https://11467.com/huanggang/co/4258.htm",
        "authority": "C",
        "notes": "载明湖北制丝针织厂位于英山，行业为针织品编织品及其制品厂，主营白厂丝、丝类产品生产销售、缫丝生产加工，地址温泉镇温泉路41号，状态在业——厂址候选坐标与“制丝针织”厂名完全吻合（页面限流，经搜狗搜索摘要+跳转URL双重解析核读）。",
    },
    "qichun_chain_hgdaily_2012": {
        "source_type": "official_media",
        "title": "周火明创业路上铸辉煌（蕲春县第三机械厂并入湖北链条厂设分厂、2005年破产沿革）",
        "org": "黄冈新闻网（黄冈日报社）",
        "pub_date": "2012-12-14",
        "url": "https://www.hgdaily.com.cn/w/3/m_ciye/4O1177O30326O0O1.html",
        "authority": "B",
        "notes": "载明1989年蕲春县政府、县工业局决定将蕲春县第三机械厂并入湖北链条厂成立分厂；1997年始湖北链条厂生产经营每况愈下，2005年破产倒闭、全厂职工卖断身份；原厂同事2005年租赁县漕河镇新建居委会闲置厂房再创业。",
    },
    "qichun_chain_21jingji_2012": {
        "source_type": "national_business_media_repost",
        "title": "湖北虎牌链条厂借贷生死劫（蕲阳北路319号，蕲春县早期两大老国企之一）",
        "org": "21世纪经济报道（搜狐焦点转载）",
        "pub_date": "2012-12-10",
        "url": "https://news.focus.cn/xm/2012-12-10/2622998.html",
        "authority": "C",
        "notes": "载明湖北虎牌链条制造有限责任公司位于蕲春县漕河镇蕲阳北路319号，系蕲春县早期两大老国企之一、县里排名前列税收大户；七八十年代由农具厂改为湖北链条厂，九十年代中停产，2005年资不抵债经县委县政府同意破产改制、高永友以400万元买下，2006年注册股份制私企；含厂区实景（堆料、仓库、打包待发链条）。与黄冈新闻网2012年报道及1989年省政府公报“省级先进企业”名单互证。",
    },
    "shashi_tractor_placename": {
        "source_type": "official_placename_database_repost",
        "title": "沙市市柴油机总厂（历史地名词条，数据源中国·国家地名信息库）",
        "org": "百度百科（数据源标注中国·国家地名信息库）",
        "pub_date": None,
        "url": "https://baike.baidu.com/item/%E6%B2%99%E5%B8%82%E5%B8%82%E6%9F%B4%E6%B2%B9%E6%9C%BA%E6%80%BB%E5%8E%82/61377899",
        "authority": "A",
        "notes": "词条数据源为国家地名信息库（引用日期2022-06-09），载沿革：1954年建铁木农具厂→1964年更名沙市农业机械厂→1970年更名沙市拖拉机厂→1973年扩建更名柴油机厂→1978年12月更名沙市市柴油机总厂→1997年原址修建塔桥小区（设立1954年、废止1997年）——证实沙市拖拉机厂真实存在（1970-1973），与省档案馆SZ 90-1-279（1966）“沙市三厂(拖拉机厂)”批复时间线吻合，旧址位置候选沙市区塔桥路一带。同名异厂提示：另有“沙市农业机械厂”（1979-1999，生产银锄）需区分。原始条目宜在 dmfw.mca.gov.cn 复核留档。",
    },
    "jingzhou_machine_tool_tianyancha": {
        "source_type": "enterprise_registry_mirror",
        "title": "湖北省荆州机床厂工商登记信息（荆州区安心桥38号，全民所有制，1996年登记设立，状态吊销未注销）",
        "org": "天眼查（镜像工商登记）",
        "pub_date": None,
        "url": "https://www.tianyancha.com/company/2313192265",
        "authority": "B",
        "notes": "载明湖北省荆州机床厂：全民所有制，1996-06-05登记设立，注册资本7419万元，住所荆州区安心桥38号，登记机关荆州市工商局，状态吊销未注销，英文名Hubei Jingzhou Machine Tool Factory。",
    },
    "jingzhou_hehua_machine": {
        "source_type": "third_party_enterprise_page",
        "title": "荆州荷花机床有限公司自介（原湖北省荆州机床厂改制组建，1958年建厂，荆州城东门外，产C5112/C5116立式车床）",
        "org": "51sole企业自介页（另参百度百科荆州荷花机床词条）",
        "pub_date": None,
        "url": "https://hkjum719013.51sole.com/companyabout.htm",
        "authority": "C",
        "notes": "载明荆州荷花机床有限公司系原湖北省荆州机床厂改制后组建，位于荆州城东门外，企业始建于1958年，曾生产大型立式车床C5112、C5116；百度百科词条载公司2002年5月30日成立、前身为1958年创建的湖北省荆州机床厂、“荷花牌”机床曾出口多国。与天眼查工商信息互证；并据荆州新闻网《沙市机床一厂的“巅峰岁月”》（news.jznews.com.cn/system/2022/03/16/030015496.shtml，B级）排除“荆州机床厂=沙市第一机床厂”（沙市一机1956年建于沙市北京东路）——荆州机床厂为独立厂（1958年建、荆州城东门外/安心桥38号）。",
    },
    "suizhou_juyu_renov_2017": {
        "source_type": "municipal_government_portal",
        "title": "随城启动聚玉街改造（官方确认聚玉街“避雷器厂桥梁”地标）",
        "org": "随州市人民政府门户网站",
        "pub_date": "2017-11-04",
        "url": "http://www.suizhou.gov.cn/zwgk/xxgk/shgysyjs/jtzx/202001/t20200104_619981.shtml",
        "authority": "A",
        "notes": "市政府网2017年报道聚玉街改造工程，载明“改造避雷器厂和东壕街两座桥梁”——官方确认聚玉街上有以“避雷器厂”命名的桥梁，避雷器厂为聚玉街地标，与房产网聚玉街358号地址线索互证。",
    },
    "suizhou_arrester_company_history": {
        "source_type": "enterprise_official_site",
        "title": "湖北省随州避雷器有限责任公司公司简介（1976年建厂，原名随州避雷器厂，机械部电力部定点）",
        "org": "湖北省随州避雷器有限责任公司官网",
        "pub_date": None,
        "url": "http://www.hbsszblq.com/list-67-1.html",
        "authority": "C",
        "notes": "企业官网自介：国家原机械部和电力部定点生产金属氧化物避雷器的专业公司，创建于1976年、原名随州避雷器厂（后为湖北省随州避雷器股份有限公司），1978年在国内率先生产出无间隙金属氧化物避雷器；北极星电力商务通页补充1986年水电部避质检字001号《准用证》、1990年机械部首批《金属氧化物避雷器生产许可证》；黄页载武汉博大科技集团随州避雷器有限公司地址聚玉街358号、随州避雷器有限公司（1998年注册）聚玉街十四号——两址均在聚玉街。企业自述内容以官方档案互证为准。",
    },
}


UPGRADES = {
    "HBI-HG-012": {
        "record_status": "source_confirmed",
        "recognition_status": "罗田大河岸缫丝厂厂址语境坐实：大河岸镇永兴街63号（永兴茧丝2002年注册、经营范围首项缫丝、已吊销；厂办预制板厂条目行业标注缫丝厂反证母厂）；法定遗产认定仍无",
        "district_county": "罗田县大河岸镇永兴街",
        "material_carriers": "缫丝厂厂址（大河岸镇永兴街63号及永兴街沿线原厂区）；厂房设备留存待现场核验",
        "notes_append": "2026-10-03复核升格：搜了网企业目录（C）厂址信息与顺企网预制板厂条目互证，自 research_candidate 升格为 source_confirmed（升格表示厂址语境坐实，不表示建筑本体与法定认定）；县缫丝有限责任公司（凤山镇义水北路383号）为县厂法人化主体线索。",
    },
    "HBI-HG-013": {
        "record_status": "source_confirmed",
        "recognition_status": "湖北制丝针织厂厂址候选坐实：英山县温泉镇温泉路41号（主营白厂丝+针织，与厂名完全吻合，状态在业）；法定遗产认定仍无",
        "district_county": "英山县温泉镇温泉路",
        "material_carriers": "制丝针织厂厂址（温泉镇温泉路41号）；厂房设备留存与在业状态待实地踏勘",
        "notes_append": "2026-10-03复核升格：顺企网企业目录（C，搜狗摘要+跳转URL双重解析核读）厂址与主营信息坐实，自 research_candidate 升格为 source_confirmed（升格表示厂址语境坐实，不表示建筑本体与法定认定）；建厂年代待英山县工业志核验，可顺带核查湖北桑宝集团谱系。",
    },
    "HBI-HG-014": {
        "record_status": "source_confirmed",
        "recognition_status": "湖北链条厂沿革与旧址完整闭环：农具厂改名湖北链条厂（七八十年代）→1989年三机厂并入设分厂→1997年衰败→2005年破产改制→虎牌链条延续（漕河镇蕲阳北路319号）；曾获机械工业部部优、湖北省优",
        "district_county": "蕲春县漕河镇蕲阳北路（新建居委会片区）",
        "material_carriers": "链条厂厂址（漕河镇蕲阳北路319号，厂区实景见21世纪经济报道2012年报道）；厂房设备现状待现场核验",
        "notes_append": "2026-10-03复核升格：黄冈新闻网（B）两篇与21世纪经济报道（C，含厂区实景）构成完整证据链（农具厂改名沿革、1989并入、2005破产改制、蕲阳北路319号厂址、部优省优荣誉），自 archive_lead 升格为 source_confirmed；新建居委会老厂区与蕲阳北路319号地块关系待核。",
    },
    "HBI-JZ-017": {
        "record_status": "source_confirmed",
        "recognition_status": "沙市拖拉机厂沿革获国家地名信息库实证：1954铁木农具厂→1964沙市农业机械厂→1970沙市拖拉机厂→1973柴油机厂→1978柴油机总厂→1997原址建塔桥小区；与省档案馆SZ 90-1-279（1966）“沙市三厂(拖拉机厂)”批复时间线吻合，旧址位置候选沙市区塔桥路一带",
        "district_county": "沙市区塔桥路一带（塔桥小区原址）",
        "material_carriers": "原厂址已建塔桥小区（1997年），拖拉机厂时期建筑无存证；档案图纸与设备清单待省档案馆调档",
        "notes_append": "2026-10-03复核升格：百度百科转载国家地名信息库沿革条目（A-，2026-10-03经WAP版全文核读）证实沙市拖拉机厂（1970-1973）真实存在且原址在塔桥路一带，与省档案馆1966年批复题名时间线吻合；自 archive_lead 升格为 source_confirmed（升格表示沿革与旧址位置语境坐实，“沙市三厂”称谓与农机厂/拖拉机厂的对应细节仍待调阅档案原文，建筑本体已无存）；同名异厂“沙市农业机械厂”（1979-1999，产银锄）需区分。",
    },
    "HBI-JZ-018": {
        "record_status": "source_confirmed",
        "recognition_status": "荆州机床厂名称对应解决：系1958年建、荆州城东门外（荆州区安心桥38号）的独立机床厂（产C5112/C5116立式车床、荷花牌出口），2002年改制为荆州荷花机床有限公司——非沙市第一机床厂；1989年省政府公报名单“荆州机床厂”大概率对应此厂（建议调名单原文终核）",
        "district_county": "荆州区安心桥（荆州城东门外）",
        "material_carriers": "机床厂厂址（安心桥38号）厂房与机床设备；改制后厂区现状待现场核验",
        "notes_append": "2026-10-03复核升格：天眼查工商镜像（B）+企业自介/百科（C）+荆州新闻网沙市一机报道（B，排除证据）三重证据解决名称对应问题，自 archive_lead 升格为 source_confirmed（升格表示名称对应与厂址坐实，不表示建筑本体与法定认定）。",
    },
    "HBI-SZ-009": {
        "record_status": "source_confirmed",
        "recognition_status": "随州避雷器厂厂址与厂史双固化：聚玉街358号多源一致（黄页+房产网），市政府网2017年聚玉街改造报道官方确认“避雷器厂桥梁”地标；企业官网自述1976年建厂（原名随州避雷器厂）、机械部电力部定点、1978年国内率先生产无间隙金属氧化物避雷器",
        "material_carriers": "厂址（聚玉街358号及聚玉街十四号）厂房与“避雷器厂桥梁”地标；桥梁现状与厂房留存待现场核验",
        "notes_append": "2026-10-03复核升格：随州市政府网2017年改造报道（A）+企业官网厂史（C）+黄页地址多源互证，自 research_candidate 升格为 source_confirmed（升格表示厂址与厂史语境坐实，不表示建筑本体与法定认定）；1976年建厂批文建议赴随州市档案馆补A级文件。",
    },
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    for key, source in SOURCES.items():
        if key in sources and sources[key] != source:
            raise SystemExit(f"conflicting source: {key}")
    sources.update(SOURCES)
    updated = 0
    for record_id, patch in UPGRADES.items():
        record = next((row for row in records if row["inventory_id"] == record_id), None)
        if record is None:
            raise SystemExit(f"record not found: {record_id}")
        for key in ("record_status", "recognition_status", "district_county"):
            if key in patch and record[key] != patch[key]:
                record[key] = patch[key]
                updated += 1
        if "material_carriers" in patch and record["cultural_evidence"]["material_carriers"] != patch["material_carriers"]:
            record["cultural_evidence"]["material_carriers"] = patch["material_carriers"]
            updated += 1
        new_sources = {
            "HBI-HG-012": ["luotian_silk_yongxing_2022"],
            "HBI-HG-013": ["yingshan_zhisi_wenquan_41"],
            "HBI-HG-014": ["qichun_chain_hgdaily_2012", "qichun_chain_21jingji_2012"],
            "HBI-JZ-017": ["shashi_tractor_placename"],
            "HBI-JZ-018": ["jingzhou_machine_tool_tianyancha", "jingzhou_hehua_machine"],
            "HBI-SZ-009": ["suizhou_juyu_renov_2017", "suizhou_arrester_company_history"],
        }[record_id]
        for k in new_sources:
            if k not in record["source_keys"]:
                record["source_keys"].append(k)
                updated += 1
        if patch["notes_append"] not in record["notes"]:
            record["notes"] = record["notes"] + patch["notes_append"]
            updated += 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_bv_updated={updated} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
