from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCES = {
    "qichun_batch4_2025": {
        "source_type": "county_government_notice",
        "title": "县人民政府关于公布蕲春县第四批历史建筑名录的通知（7处，2025-09-22）",
        "org": "蕲春县人民政府门户网站",
        "pub_date": "2025-09-22",
        "url": "https://www.qichun.gov.cn/zwgk/public/6636852/1602651.html",
        "authority": "A",
        "notes": "蕲春县第四批历史建筑7处正式公布：黄冈市第二人民医院生活区1号宿舍（1951年，蕲州镇）、李明祖祠（1926年，檀林镇）、康桥粮库（31-32号，1958年，彭思镇康桥村）【粮仓】、黄柏城大礼堂（1982年，彭思镇）、古龙宫（清中期，向桥乡）、闻彪祖祠（1904年，狮子镇）、林氏宗祠（1949年，狮子镇）。",
    },
    "huanggang_batch4_gongshi_2026": {
        "source_type": "county_public_notice",
        "title": "关于拟确定黄冈市市区第四批历史建筑名录的公示（5处，公示期2026-07-13至07-17，附件doc已下载解析）",
        "org": "黄州区住房和城乡建设局（黄州区人民政府网）",
        "pub_date": "2026-07-13",
        "url": "http://www.huangzhou.gov.cn/zwgk/public/6635079/1753009.html",
        "authority": "A",
        "notes": "市区第四批拟确定5处（附件doc已下载WPS COM解析）：李四光纪念馆（1988年，体育路21号）、启黄中学教学楼（1985年）、启黄中学食堂/礼堂（80年代）、禹王公社星火大礼堂（1978年，禹王汪家冲社区）【集体化时期公社礼堂】、陈策楼镇吕华山故居（2020年）。截至检索日（2026-10-05）未见市政府正式公布通知，公示层级入库待转正跟踪。背景：市区前三批共61处（13+23+25）。",
    },
    "xishui_batch2_gongshi_2023": {
        "source_type": "county_public_notice",
        "title": "关于浠水县第二批11处历史建筑的公示（公示期2023-09-26至10-02）",
        "org": "浠水县住房和城乡建设局（浠水县人民政府网）",
        "pub_date": "2023-09-26",
        "url": "https://www.xishui.gov.cn/zwgk/public/6636610/1059275.html",
        "authority": "A",
        "notes": "浠水县第二批11处公示（第85轮已入库工业3处：闫河倒虹吸/蔡河供销社/圆拱石型养猪场）另含汪岗镇前进村“大寨型”建筑村部（1974年，集体化村部）、闻一多纪念馆（1987年）、蔡河镇政府礼堂（1982年）、卷棚桥（约1500年）、青蒿港桥（1755年）、丁司垱镇分水丘村古井（1930年）、团陂镇樟树湾村古门楼（约1500年）、绿杨乡冷水井村祖家老屋（1950年）、乱石河村卷棚桥（约1500年）。",
    },
}


def _hg(record_id: str, name: str, dc: str, cat: str, status: str, src: list, kind: str, year: str, material: str, tech: str, social: str, use: str, notes: str, aliases: list) -> dict:
    return {
        "inventory_id": record_id,
        "name": name,
        "city": "黄冈市",
        "district_county": dc,
        "industry_category_l1": cat,
        "recognition_level": "municipal_historical_building",
        "recognition_status": status,
        "record_status": "source_confirmed",
        "geocode_status": "pending",
        "source_keys": src,
        "cultural_evidence": {
            "material_carriers": material,
            "technical_memory": tech,
            "social_memory": social,
            "current_use_or_loss": use,
        },
        "notes": notes,
        "aliases": aliases,
        "asset_kind": kind,
    }


RECORDS = [
    _hg("HBI-HG-041", "康桥粮库（31-32号）", "蕲春县彭思镇康桥村", "粮食仓储工业",
        "蕲春县第四批历史建筑名录（2025-09-22正式公布，7处之一；1958年建）", ["qichun_batch4_2025"], "industrial_storage_site", "1958年",
        "康桥粮库31-32号仓房两栋；仓房型制与保存状态待现场测绘",
        "1958年公社时期粮仓的仓储建筑形制，与底册蕲春链条厂（HBI-HG-014）同县域工业谱系",
        "彭思镇粮储职工与统购统销年代售粮记忆",
        "以第四批历史建筑身份正式公布保护；在用/停用状态待核",
        "直接取自蕲春县政府第四批名录通知（A级，正式公布）；历史建筑保护不等于工业遗产法定认定；坐标未核验保持待核。",
        [],
    ),
    _hg("HBI-HG-042", "禹王公社星火大礼堂", "黄冈市黄州区禹王街道汪家冲社区", "工业社区",
        "黄冈市市区第四批历史建筑名录（公示期2026-07-13至07-17，拟确定5处之一；1978年建）", ["huanggang_batch4_gongshi_2026"], "industrial_social_site", "1978年",
        "公社大礼堂建筑本体（汪家冲社区）；观众厅与舞台格局待现场测绘",
        "1978年公社礼堂的集会、文艺与放映功能空间形制",
        "禹王公社集体劳动、开会与文娱活动的年代记忆",
        "公示拟确定层级（正式公布通知截至2026-10-05未见，入库标注待转正跟踪）；现状用途待核",
        "直接取自黄州区住建局第四批公示附件doc（A级，已下载WPS COM解析）；公示层级参照浠水/麻城公示批次先例入库；坐标未核验保持待核。",
        ["星火大礼堂"],
    ),
    _hg("HBI-XG-030", "汪岗镇前进村“大寨型”建筑村部", "孝感市浠水县汪岗镇前进村", "工业社区",
        "浠水县第二批历史建筑公示（2023-09-26至10-02公示，11处之一；1974年建）", ["xishui_batch2_gongshi_2023"], "industrial_social_site", "1974年",
        "“大寨型”建筑村部本体（前进村）；形制与保存状态待现场测绘",
        "农业学大寨时期的村部建筑范式（与大寨梯田/集体劳动思潮对应的公共建筑类型）",
        "前进村集体化治理与农业学大寨运动记忆",
        "以第二批历史建筑公示层级纳入保护体系（正式公布通知未检索到，待跟踪）；现状用途待核",
        "直接取自浠水县第二批公示（A级，第85轮同源批次补录——工业/集体化3处已入库，本条为该村部类型补录）；坐标未核验保持待核。",
        ["前进村村部"],
    ),
]


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    records = data.setdefault("records", [])
    for key, source in SOURCES.items():
        if key in sources and sources[key] != source:
            sources[key] = source
    sources.update(SOURCES)
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
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_cq_sources={len(SOURCES)} added_records={added} total_records={len(records)} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
