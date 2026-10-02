from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "xiangyang_miantielu_2026": {
        "source_type": "official_media",
        "title": "昔日“工业锈带”变身“生活秀带” 襄棉铁路废弃专线重载人间烟火",
        "org": "荆楚网（湖北日报传媒集团）极目新闻",
        "pub_date": "2026-07-06",
        "url": "http://news.cnhubei.com/content/2026-07/06/content_20069337.html",
        "authority": "B",
        "notes": "报道载明襄棉铁路系原襄樊棉纺织印染厂的配套货运专线（上世纪60年代末铺轨），厂区位于樊城汉江路—长虹路片区；专线保护更新项目为襄阳市人大二号议案、2025年市民生实事，2025年12月29日首开段建成，坚持“不拆一根钢轨”、站台轨道原址留存。另参襄阳市政府网2024-04-22《襄阳工业遗产焕新再出发》：市经信局正起草市级工业遗产保护名录。",
    },
    "xiangyang_archive_wenzi603_2023": {
        "source_type": "government_archive_media",
        "title": "【“四史教育”专栏】文字六〇三厂：“铅与火”时代的行业顶流",
        "org": "襄阳市档案局网站（转载湖北日报客户端）",
        "pub_date": "2023-07-20",
        "url": "http://dsj.xiangyang.gov.cn/",
        "authority": "A",
        "notes": "档案局专栏文章载明：1965年经国务院批准，国家文化部筹建三线印刷企业，取名“第三新华印刷厂”，代号“文字六〇三办公室”，选点小组1965年4月赴襄阳选址定于岘山脚下，1968年建成投产，2017年改制为文字六〇三文化创意公司。经360搜索跳转核读全文（页面落款湖北日报客户端2023-07-20，作者祝兆林等）；2026-10-03复核确认原发子站 dsj.xiangyang.gov.cn 已随改版下线（404），原发直链失效，替代可访问载体为襄城区政府网六〇三街区报道（xc.xiangyang.gov.cn/news/202606/t20260618_4019626.shtml，含1965年建成沿革与省级街区认定）；档案题名“襄阳县第三新华印刷厂”（1965-1966省档案馆征地档案）与该厂筹建时间、专名吻合，两条证据互相印证。",
    },
    "xiangyang_cotton_reserve_2017": {
        "source_type": "government_information_public",
        "title": "襄阳市棉花中转储备库仓库招租（索引号011158671/2017-08527）",
        "org": "襄阳市供销合作社联合社（政府信息公开）",
        "pub_date": "2017-12-05",
        "url": "http://gxs.xiangyang.gov.cn/",
        "authority": "A",
        "notes": "招租公告载明：襄阳市棉花中转储备库（曾用名襄樊市棉花中转储备库）为国有企业，位于襄城区余家湖、紧挨207国道，现有国标仓库11栋、每栋800平方米。经360搜索跳转核读原文，站内直链未留存（复现路径：gxs.xiangyang.gov.cn 仅HTTP可访问→政府信息公开→索引号011158671/2017-08527检索，或360搜索标题取“-襄阳市供销社”首条；公告要素含国标仓库11栋、每栋800平米、层高9.5米、余家湖207国道旁、联系电话0710-3616600）。另据荆楚网消息（2009-12-16，经转载核读）：中储棉总公司2009年致函湖北省发改委拟在襄樊建中央直属棉花储备库（库容5万吨），国家发改委2016年批复建于余家湖工业园207国道东侧——沿革细节的原始报道直链待补。",
    },
    "hubei_kongyaji_address": {
        "source_type": "third_party_enterprise_directory",
        "title": "湖北压缩机有限公司企业信息（原湖北空压机厂承接体）",
        "org": "顺企网企业目录",
        "pub_date": None,
        "url": "http://xiangfan03712.11467.com/",
        "authority": "C",
        "notes": "企业目录载明：湖北压缩机有限公司地址为湖北省襄樊市大庆路56号（1993年注册，经营空压机产品设计制造、一二类压力容器），搜索快照另证其为湖北空压机厂持股的国企承接体、湖北空压机厂兴达实业公司（1989）注册于襄樊市大庆西路56号——与既有生活区POI互证，厂址坐实为樊城区大庆西路（56号），C级多源一致。",
    },
    "songzi_982_factory_2021": {
        "source_type": "official_media",
        "title": "特约记者行：我们三线建设的秘密工厂“949”",
        "org": "荆州新闻网",
        "pub_date": "2021-11-26",
        "url": "http://www.jznews.com.cn/",
        "authority": "B",
        "notes": "荆州新闻网三线建设系列报道载明：建在刘家场镇边的军工企业982厂对外称呼“清江矿山机械厂”（生产半自动步枪），另有9669厂、949厂；三线建设自1964年起、80年代初军转民、1990年松滋三家军工企业整体搬迁沙市。经360搜索跳转核读全文，原发直链未留存（站内路径待补）。注意甄别：松滋市金津矿山机械公司自述“原湖北省松滋矿山机械厂”（新江口）与982厂“清江矿山机械厂”（刘家场）是否同一未经证实，不混用。",
    },
}


# 升格条目补丁（recognition_status / record_status / district_county / cultural_evidence / notes）
UPGRADES = {
    "HBI-XIANGYANG-030": {
        "record_status": "source_confirmed",
        "recognition_status": "襄樊市棉纺织印染厂沿革经官方媒体确认：1966年省档案馆设计任务书档案题名与荆楚网2026年报道（襄棉铁路专线为该厂配套、厂区樊城汉江路—长虹路片区）互证；厂区活化项目为市人大二号议案",
        "district_county": "樊城区汉江路—长虹路片区",
        "material_carriers": "厂区（樊城汉江路—长虹路片区）与襄棉铁路货运专线（60年代末铺轨，站台轨道原址留存、不拆一根钢轨）；厂房与染整设备现状待现场测绘",
        "technical_memory": "棉纺织印染联合生产与铁路专线运输工艺；专线2025年12月29日首开段建成转型为城市公共空间",
        "social_memory": "襄棉职工与樊城纺织工业街区记忆；铁路专线重载人间烟火成为城市更新样本",
        "current_use_or_loss": "铁路专线经保护更新重载公共功能（2025年首开段），系政府主导的工业锈带变生活秀带项目；厂区建筑本体保护清单待市级工业遗产名录（起草中）公布",
        "notes_append": "2026-10-03复核升格：荆楚网极目新闻2026-07-06报道（B）与省档案馆1966年档案题名互证，自 archive_lead 升格为 source_confirmed（升格表示沿革、区位与活化语境有官方媒体来源，厂界与建筑清单仍待现场核验与市级名录公布）。",
    },
    "HBI-XIANGYANG-032": {
        "record_status": "source_confirmed",
        "recognition_status": "棉花储备仓库部分经政府公开信息确认（襄阳市棉花中转储备库，襄城区余家湖，国标仓库11栋）；煤货场部分维持档案线索",
        "district_county": "襄城区余家湖（棉花储备库）；煤货场地址待核",
        "material_carriers": "棉花储备侧：襄阳市棉花中转储备库国标仓库11栋（每栋800平方米，余家湖207国道旁）；煤货场侧设施无存证",
        "technical_memory": "棉花储备中转的仓储管理与调运体系；中储棉2009年拟建中央直属储备库（库容5万吨）、2016年批复余家湖的沿革背景",
        "social_memory": "供销社系统棉花储备职工与江汉平原棉产集散记忆",
        "current_use_or_loss": "储备库2017年仍在招租运营（政府公开信息）；煤货场部分实体无存证，维持档案线索",
        "notes_append": "2026-10-03复核升格：棉花储备仓库部分以市供销社2017年招租公告（A，索引号可复现检索）升格 source_confirmed，煤货场子项维持 archive_lead 表述于本条 notes；对象名称与实际构成按两分处理。",
    },
    "HBI-PROV-011": {
        "record_status": "source_confirmed",
        "recognition_status": "湖北空压机厂厂址坐实为樊城区大庆西路56号（企业承接体目录与生活区POI多源一致）；法定遗产认定仍无",
        "district_county": "樊城区米公街道大庆西路（厂址与生活区）",
        "material_carriers": "厂址（大庆西路56号）与生活区1栋（既有POI）；厂房设备现状待现场核验",
        "technical_memory": "空压机产品设计制造与一、二类压力容器生产脉络；1993年改制承接体湖北压缩机有限公司延续经营",
        "social_memory": "空压机厂职工与樊城大庆西路厂区生活区记忆",
        "current_use_or_loss": "承接体湖北压缩机有限公司仍在经营；老厂区建筑保存状况待现场核验",
        "notes_append": "2026-10-03复核升格：顺企网企业目录（C）厂址信息与既有生活区POI互证，自 archive_lead 升格为 source_confirmed（升格表示厂址语境坐实，不表示建筑本体与法定认定）。",
    },
    "HBI-JZ-015": {
        "record_status": "source_confirmed",
        "recognition_status": "清江矿山机械厂即三线军工982厂（刘家场镇，生产半自动步枪，1964年建/1965年投产与省档案馆1965年设计任务书吻合；1990年整体迁沙市）——荆州新闻网三线系列报道确认",
        "district_county": "松滋市刘家场镇",
        "material_carriers": "982厂厂址（刘家场镇边）军工厂房与产线；1990年迁沙市后旧址建筑留存状况待现场核验",
        "technical_memory": "三线军工半自动步枪制造工艺与军转民转型（80年代初）；1964年建设、1965年投产、1990年迁并的时间线",
        "social_memory": "三线军工职工“秘密工厂”记忆与松滋军工城（949/982/9669厂）群体叙事",
        "current_use_or_loss": "1990年整体搬迁沙市后刘家场旧址现状待核；三线旧址活化利用方向待属地规划明确",
        "notes_append": "2026-10-03复核升格：荆州新闻网三线系列报道（B，2021-11-26）厂名、地点、年代与省档案馆1965年设计任务书三重吻合，自 archive_lead 升格为 source_confirmed；松滋金津矿山机械（新江口，自述原湖北省松滋矿山机械厂）与982厂的同一性未经证实，不混用。",
    },
}


NOTES_APPENDS = {
    "HBI-XIANGYANG-028": "2026-10-03复核确认：襄阳市档案局专栏文章（A，2023-07-20）载明1965年文化部筹建的三线印刷企业即取名“第三新华印刷厂”、代号“文字六〇三办公室”——本档案线索与 HBI-PROV-007 文字六〇三厂为同一对象，不再作为独立对象升格；1965年省档案馆征地档案题名与筹建时间互证，已补入 PROV-007 语境。",
    "HBI-XIANGYANG-029": "2026-10-03复核补充：第三方公交站名“肖湾化肥厂”（襄州区，11条线路）与“襄阳县化肥厂”（1975年筹建、1977年投产、1996年改制楚鹰化学）线索指向肖湾一带，但厂名与年代同1965-1966年档案题名的对应关系存疑，维持 source_lead 待档案原件核对。",
    "HBI-XIANGYANG-031": "2026-10-03复核补充：襄阳肉联厂（商贸国企，2004年与雨润重组）冷库系统与本档案题名“襄阳冷冻厂”的同一性未能证实，仅记为存疑旁路线索，维持 source_lead。",
    "HBI-XIANGYANG-033": "2026-10-03复核补充：枣阳市环城农机站（南城街道张湾村）为该拖拉机站体系的存续机构，但原站址与建筑遗存无证据，维持 source_lead 待地方志与实地核查。",
    "HBI-XG-013": "2026-10-03复核补充：孝感市政府网2024-08报道证实1966年东方红粮机厂（上海粮机厂内迁）落户安陆、孝感党史资料载1966年上海武汉两地工厂合并迁安陆建东方红粮食机械厂——年代与1965年征地档案吻合，但档案题名“粮食加工与棉花轧花设施”与粮机制造的行业指向待档案比对，维持 source_lead。",
    "HBI-WUHAN-065": "2026-10-03复核补充：黄陂横店老粮库（1950年始建省级储备库，“亿万斤粮库”，2026年“横店记忆”城市更新保留红砖仓房）为黄陂粮仓遗产存续的旁证，但系横店粮库，与前川1965年征地档案题名的对应关系未证实，维持 source_lead。",
    "HBI-SZ-012": "2026-10-03复核补充：随县高城镇卸甲村闲置粮仓翻新活化（官媒2026-06，随县已梳理20处村级粮仓等闲置资产）与随县国家粮食储备库（2019年采购公告，机构存续）证实随县粮仓体系存续，但与1965年档案题名仓库的具体对应未证实，维持 source_lead。",
    "HBI-JZ-016": "2026-10-03复核：公安县砖瓦厂多组关键词检索未命中任何官方地址、认定或权威报道（仅1989年后乡镇砖瓦企业注册条目），维持 source_lead，转线下以省档案馆征地档案为抓手深挖。",
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    for key, source in SOURCES.items():
        if key in sources and sources[key] != source:
            sources[key] = source
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
        for key in ("material_carriers", "technical_memory", "social_memory", "current_use_or_loss"):
            if key in patch and record["cultural_evidence"][key] != patch[key]:
                record["cultural_evidence"][key] = patch[key]
                updated += 1
        src_key = next((k for k in record["source_keys"]), None)
        new_sources = {
            "HBI-XIANGYANG-030": ["xiangyang_miantielu_2026"],
            "HBI-XIANGYANG-032": ["xiangyang_cotton_reserve_2017"],
            "HBI-PROV-011": ["hubei_kongyaji_address"],
            "HBI-JZ-015": ["songzi_982_factory_2021"],
        }[record_id]
        for k in new_sources:
            if k not in record["source_keys"]:
                record["source_keys"].append(k)
                updated += 1
        if patch["notes_append"] not in record["notes"]:
            record["notes"] = record["notes"] + patch["notes_append"]
            updated += 1
    for record_id, notes_append in NOTES_APPENDS.items():
        record = next((row for row in records if row["inventory_id"] == record_id), None)
        if record is None:
            raise SystemExit(f"record not found: {record_id}")
        if notes_append not in record["notes"]:
            record["notes"] = record["notes"] + notes_append
            updated += 1
    prov007 = next((row for row in records if row["inventory_id"] == "HBI-PROV-007"), None)
    prov007_add = "2026-10-03档案互证：省档案馆1965-1966年征地档案题名“襄阳县第三新华印刷厂”经襄阳市档案局专栏文章证实即1965年文化部筹建的三线印刷企业（代号文字六〇三办公室，1968年建成投产），筹建沿革获档案题名与档案局专栏双重印证。"
    if prov007 is None:
        raise SystemExit("record not found: HBI-PROV-007")
    if prov007_add not in prov007["notes"]:
        prov007["notes"] = prov007["notes"] + prov007_add
        updated += 1
    if "xiangyang_archive_wenzi603_2023" not in prov007["source_keys"]:
        prov007["source_keys"].append("xiangyang_archive_wenzi603_2023")
        updated += 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_br_updated={updated} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
