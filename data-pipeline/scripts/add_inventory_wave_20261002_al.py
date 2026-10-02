from __future__ import annotations

import json
from pathlib import Path


PATH = Path(__file__).resolve().parents[1] / "enrichment" / "hubei_inventory.json"


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    record = next(row for row in data["records"] if row["inventory_id"] == "HBI-JM-018")
    record["aliases"] = ["京山市原机械厂生活区", "京山机械厂职工生活区", "京山机械厂生活区", "京山机械厂社区"]
    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wave_al_sources=0 added_records=0 updated_records=1 total_records={len(data['records'])} total_sources={len(data['sources'])}")


if __name__ == "__main__":
    main()
