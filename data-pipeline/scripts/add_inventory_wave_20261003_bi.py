from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


SOURCE_UPDATE = {
    "huangshi2019": {
        "source_type": "government_notice",
        "title": "关于公布第一批黄石市工业遗产名录的通知（黄政发〔2019〕3号）",
        "org": "黄石市人民政府",
        "pub_date": "2019-01-03",
        "url": "http://huangshi.gov.cn/xxxgk/2020_zc/2020_gfxwj/202011/t20201109_727808.html",
        "authority": "A",
        "notes": "政府规范性文件正文载明19项经市政府第71次常务会议审议通过；2026-10-03 实读现行页面并下载3张附件图片逐张视觉核读19项全表（冶金工业8项、水泥工业2项、煤炭工业4项、机械制造工业2项、其它工业3项，含编号4202022018001-19与地址），与底册 HBI-HS-001~019 逐项对应确认；本地存档 raw/huangshi_iheritage/。黄石市另有《黄石市工业遗产保护条例》地方立法（通知正文援引）。",
    }
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    sources = data.setdefault("sources", {})
    current = sources.get("huangshi2019")
    if current == SOURCE_UPDATE["huangshi2019"]:
        updated = 0
    elif current is None:
        raise SystemExit("source not found: huangshi2019")
    else:
        sources["huangshi2019"] = SOURCE_UPDATE["huangshi2019"]
        updated = 1
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_bi_updated_sources={updated} total_records={len(data.get('records', []))} total_sources={len(sources)}")


if __name__ == "__main__":
    main()
