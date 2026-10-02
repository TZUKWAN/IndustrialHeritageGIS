from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "shiyan_mould_reloc_2020": {
        "source_type": "local_media_baijiahao_repost",
        "title": "今天上午开建！十堰东风这家50年历史的大工厂要搬家了！（模具分公司搬迁报道）",
        "org": "秦楚网系（云上十堰/百家号转载）",
        "pub_date": "2020-08-01",
        "url": "https://baijiahao.baidu.com/s?id=1675983777679971482",
        "authority": "B",
        "notes": "载明东风模具冲压技术有限公司模具分公司始建于上世纪60年代，位于张湾区东岳路100号（即东风模具厂、原25厂厂区）；2020年8月模具中心在张湾工业新区装备工业园开工（投资2.35亿元）、2021年5月投产；2019年5月东风公司与十堰市政府签署装备公司整体搬迁框架协议。",
    },
    "shiyan_mould_qinchu_2019": {
        "source_type": "local_media",
        "title": "东风制造彰显中国力量——东风有限装备公司自主创新发展纪略",
        "org": "秦楚网转十堰日报",
        "pub_date": "2019-03-29",
        "url": "https://m.10yan.com/m/showArt.html?contentid=608691",
        "authority": "B",
        "notes": "载明东风模具冲压技术有限公司模具分公司技术大楼研发团队开发东风日产侧围/翼子板模具，设计制造能力居国内行业前三。",
    },
    "shiyan_chassis_merger": {
        "source_type": "enterprise_registry_mirror",
        "title": "东风汽车底盘系统有限公司工商信息（原东风汽车车轮有限公司更名，下辖车轮/传动轴/悬架弹簧/泵业工厂）",
        "org": "企查查/天眼查（渲染核读）",
        "pub_date": None,
        "url": "https://www.qcc.com/",
        "authority": "C",
        "notes": "东风汽车车轮有限公司为曾用名，公司已更名为东风汽车底盘系统有限公司（存续，注册地址十堰市张湾区工业新区发展大道社区风神大道29号），下辖车轮工厂（张湾区汉江路街道广东路2号）、传动轴工厂、悬架弹簧工厂（工业新区B区）、泵业工厂（已注销）；泵业工厂工会地址同风神大道36号。另据头条新闻标题级线索（待核证）：底盘系统公司挂牌整合原42、45、54、46等老厂号资源。",
    },
    "huangpi_qianchuan_grain_2022": {
        "source_type": "district_government_portal",
        "title": "颗粒归仓！黄陂秋粮收购工作全面展开（前川五里粮库现役收储）",
        "org": "黄陂区人民政府门户网站",
        "pub_date": "2022-09-26",
        "url": "https://www.huangpi.gov.cn/ywdt/bmzc/202209/t20220926_2047954.html",
        "authority": "A",
        "notes": "官网报道载明前川街道五里粮库现役开展秋粮收购（土庙、五里、八里粮库9月14日启动），2023年报道八里粮库为市级储备粮库（计划收储24200吨）——前川街道现役粮库体系与1965年省档案馆“黄陂县储备粮仓”征地档案地点吻合，延续关系待档案终核。",
    },
}


UPGRADES = {
    "HBI-SY-026": {
        "record_status": "source_confirmed",
        "recognition_status": "东风模具冲压技术有限公司模具分公司沿革与厂址坐实：始建于上世纪60年代（即东风模具厂、原25厂），老厂区张湾区东岳路100号，2020年整体搬迁张湾工业新区装备工业园（投资2.35亿元、2021年投产），模具设计制造能力居国内行业前三",
        "district_county": "张湾区东岳路100号（老厂区）；新厂区张湾工业新区装备工业园",
        "material_carriers": "老厂区（东岳路100号，原25厂厂区）建筑遗存与新厂区现代化模具中心；老厂区建筑保留状况待现场核验",
        "notes_append": "2026-10-03复核升格：秦楚网/云上十堰系列报道（B）坐实老厂区地址（东岳路100号、原25厂）、2020年整体搬迁与在产现状，自 source_lead 升格为 source_confirmed（升格表示沿革与厂址坐实，不表示法定工业遗产认定；老厂区搬迁后建筑处置待核）。",
    },
    "HBI-SY-027": {
        "record_status": "source_confirmed",
        "recognition_status": "东风汽车车轮有限公司沿革与现址清楚：公司已更名东风汽车底盘系统有限公司（张湾区工业新区风神大道29号），下辖车轮工厂（广东路2号）、传动轴工厂、悬架弹簧工厂；车轮随州有限公司为分立主体（季梁大道16号，年产能900万只）",
        "district_county": "张湾区（车轮工厂广东路2号；底盘系统公司风神大道29号）",
        "material_carriers": "车轮工厂现址（广东路2号）与新底盘系统公司厂区；老厂号（42/45/54/46整合为标题级线索待核证）对应厂区待考",
        "notes_append": "2026-10-03复核升格：企查查/天眼查工商信息（C，渲染核读）证实车轮公司更名底盘系统公司及各工厂现址，东风车轮随州公司官网自述40年历程，自 source_lead 升格为 source_confirmed（升格表示沿革与现址坐实，不表示法定认定；老厂号整合关系待《十堰文史·三线建设专辑》等线下核证）。",
    },
    "HBI-SY-028": {
        "record_status": "source_confirmed",
        "recognition_status": "东风汽车泵业有限公司沿革与结局清楚：1999年设立（注册资本4800万元）、厂址十堰工业新区风神大道36号，已注销，主体并入东风汽车底盘系统有限公司泵业工厂；二汽时期前身老厂号未查实",
        "district_county": "张湾区十堰工业新区风神大道36号",
        "material_carriers": "泵业公司厂址（风神大道36号）厂房与泵类产品产线；注销后厂区现状待现场核验",
        "notes_append": "2026-10-03复核升格：企查查/天眼查工商信息（C，渲染核读）坐实设立、厂址、注销与并入底盘系统泵业工厂的结局，自 source_lead 升格为 source_confirmed（升格表示沿革与厂址坐实，不表示法定认定；二汽时期前身老厂号未查实，待《十堰文史·三线建设专辑》核证）。",
    },
    "HBI-WUHAN-065": {
        "record_status": "source_confirmed",
        "recognition_status": "黄陂前川街道粮库体系现役收储（五里粮库、八里粮库为市级储备库）与1965年省档案馆“黄陂县储备粮仓”征地档案地点吻合；1965年仓与现役库的延续关系待档案终核",
        "material_carriers": "前川街道五里粮库（现役收储）、八里粮库（市级储备，计划收储24200吨）；1965年仓址与现库的建筑对应待现场核验",
        "notes_append": "2026-10-03复核升格：黄陂区政府官网2022年秋粮收购报道（A）坐实前川街道五里粮库现役收储，与1965年征地档案地点吻合，自 archive_lead 升格为 source_confirmed（升格表示地点语境坐实，不表示建筑本体与法定认定）。",
    },
}


NOTES_APPENDS = {
    "HBI-XIANGYANG-029": "2026-10-03第四组复核澄清：肖湾化肥厂经博雅地名网沿革资料证实为1975年筹建、1977年投产的襄阳县化肥厂（1996年改制楚鹰化工、2000年破产），与1965年省档案馆“襄樊市化肥厂”题名非同一实体（市属与县属、年代均不符），肖湾线索的对应性排除；1965年市属化肥厂需回溯《襄樊市志》与市级档案。",
    "HBI-XIANGYANG-031": "2026-10-03第四组复核补充：八十年代襄樊商业系统史话证实市食品公司下辖两个肉联厂、一个牛羊肉加工厂和一个肉食制品加工厂（冷库应从属该系统）；肉联厂1985年注册于襄城胜利街37号、冷库西街门市部1989年襄城西门外；“襄樊市冷冻厂”专名仍未命中，维持 source_lead。",
    "HBI-XIANGYANG-033": "2026-10-03第四组复核补充：《中国财政》1958年第5期载枣阳八一拖拉机站经营管理经验（32台机车、107名职工、服务111个农业社76354市亩）——1950年代枣阳拖拉机站体系的权威一手文献，为1965年环城站设立提供制度背景；环城站本体仍未命中，维持 source_lead。另抖音影像线索显示枣阳杨垱公社拖拉机站旧址存“残屋旧墙”（杨垱与环城不同址，仅作枣阳拖拉机站遗址存留的旁证）。",
    "HBI-XIANGYANG-032": "2026-10-03第四组复核澄清（煤货场子项）：余家湖港现况为汉江中游大型煤炭储备中转专用港（年中转500万吨、7.1公里专用铁路、2座码头），其煤炭物流源头系1996年襄樊电厂与近年多式联运格局，与1965年省档案馆“襄阳县煤货场”题名非同一实体；1965年煤货场维持 archive_lead 表述，转《襄樊市志》与土地档案线索深挖。",
    "HBI-XG-013": "2026-10-03第四组复核补充：头条媒体文证实东方红粮机厂（上海内迁、全国粮食加工机械重要生产基地）已破产拆分、老厂区冷清，另有短视频影像可定位老厂区；安陆粮机产业由永祥粮机等企业延续。粮机厂老厂区现状与档案题名“粮食加工与棉花轧花设施”的同一性仍待档案比对，维持 source_lead。",
    "HBI-SZ-012": "2026-10-03第四组复核补充：湖北日报客户端证实唐县镇原砂子粮站（近10亩）2025年拍卖活化（2000万元粮机制造项目落户），随县国家粮食储备库有限公司实体与职能经政府公开文件证实；储备库具体镇村地址仍未命中，维持 source_lead，建议下轮查湖北省政府采购网合同公告。",
    "HBI-JZ-016": "2026-10-03第四组复核：9种渠道组合检索仍未命中（必应系持续将“公安”分词为公安机关），维持 source_lead；建议转线下以《公安县志》工业篇与公安县政府网（gongan.gov.cn）站内检索深挖。",
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
            "HBI-SY-026": ["shiyan_mould_reloc_2020", "shiyan_mould_qinchu_2019"],
            "HBI-SY-027": ["shiyan_chassis_merger"],
            "HBI-SY-028": ["shiyan_chassis_merger"],
            "HBI-WUHAN-065": ["huangpi_qianchuan_grain_2022"],
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
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_bw_updated={updated} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
