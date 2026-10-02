# -*- coding: utf-8 -*-
"""抓取阿里云 DataV GeoAtlas 行政区划数据(省/市/县三级的中心点与边界), 建立本地索引。

来源: https://geo.datav.aliyun.com/areas_v3/bound/{adcode}_full.json
坐标: GCJ-02 (高德坐标系)。所有坐标在导出前统一转换为 WGS84, 转换记录于元数据。
结果缓存于 data-pipeline/interim/admin_cache/, 重复运行不重新下载。
"""
import json
import os
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, '..', 'interim', 'admin_cache')
PROCESSED = os.path.join(HERE, '..', 'processed')
BASE = 'https://geo.datav.aliyun.com/areas_v3/bound/{}_full.json'
DELAY = 0.25  # 尊重服务, 串行小间隔


def fetch(adcode):
    path = os.path.join(CACHE, f'{adcode}_full.json')
    if os.path.exists(path) and os.path.getsize(path) > 100:
        return json.load(open(path, encoding='utf-8'))
    url = BASE.format(adcode)
    req = urllib.request.Request(url, headers={'User-Agent': 'heritage-gis-etl/1.0 (research)'})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                data = json.load(r)
            json.dump(data, open(path, 'w', encoding='utf-8'), ensure_ascii=False)
            time.sleep(DELAY)
            return data
        except Exception as e:
            if attempt == 2:
                print(f'  FAIL {adcode}: {e}')
                return None
            time.sleep(1.5 * (attempt + 1))
    return None


def main():
    os.makedirs(CACHE, exist_ok=True)
    os.makedirs(PROCESSED, exist_ok=True)
    index = {}   # adcode -> {name, level, parent, center, province, city}
    order = []

    nat = fetch(100000)
    if not nat:
        sys.exit('cannot fetch national boundaries')
    provinces = [f for f in nat['features'] if f['properties'].get('adcode', 0)]
    for f in provinces:
        p = f['properties']
        index[p['adcode']] = {
            'name': p['name'], 'level': 'province', 'parent': 100000,
            'center': p.get('center') or p.get('centroid'),
            'province': p['name'], 'city': '',
        }
        order.append(p['adcode'])

    for pad in [p['properties']['adcode'] for p in provinces]:
        pf = fetch(pad)
        if not pf:
            continue
        for f in pf['features']:
            p = f['properties']
            if not p.get('adcode'):
                continue
            prov = index[pad]['name']
            index[p['adcode']] = {
                'name': p['name'], 'level': p.get('level'), 'parent': pad,
                'center': p.get('center') or p.get('centroid'),
                'province': prov, 'city': p['name'] if p.get('level') == 'city' else '',
            }
            order.append(p['adcode'])
            if p.get('level') == 'city' and p.get('childrenNum', 0) > 0:
                cf = fetch(p['adcode'])
                if not cf:
                    continue
                for g in cf['features']:
                    q = g['properties']
                    if not q.get('adcode'):
                        continue
                    index[q['adcode']] = {
                        'name': q['name'], 'level': q.get('level'), 'parent': p['adcode'],
                        'center': q.get('center') or q.get('centroid'),
                        'province': prov, 'city': p['name'],
                    }
                    order.append(q['adcode'])

    json.dump(index, open(os.path.join(PROCESSED, 'admin_index.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=0)
    levels = {}
    for v in index.values():
        levels[v['level']] = levels.get(v['level'], 0) + 1
    print('admin index entries:', len(index), levels)
    # 省级边界单独保存(供前端分级统计), 原始 GCJ-02 坐标
    json.dump(nat, open(os.path.join(PROCESSED, 'provinces_gcj02_raw.json'), 'w',
                        encoding='utf-8'), ensure_ascii=False)
    print('saved provinces_gcj02_raw.json')


if __name__ == '__main__':
    main()
