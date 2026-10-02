# -*- coding: utf-8 -*-
"""阶段5: GIS 空间分析与研究指标 (可复现, 参数与版本写入元数据)。

产出 (默认 `processed/analysis_hubei/`; 设置 `ANALYSIS_PROVINCE=ALL` 可生成内部全国结果):
  kde_raster.png + kde_meta.json   核密度估计栅格(PNG, WGS84 经纬度范围, Albers 投影计算)
  ann_stats.json                   平均最近邻指数 (投影坐标, Albers 等积)
  moran_stats.json                 全局 Moran's I (省级单元, KNN k=4 空间权重)
  province_stats.json              省级遗产数量(分级统计用)
  province_boundaries.geojson      省界(GCJ-02->WGS84, DP 简化)
  batch_stats.json                 批次/行业/省份分布(图表用)
  analysis_results.json            所有分析的可追溯元数据(数据版本/CRS/参数/时间)

所有分析基于 WGS84 输入坐标; 密度/距离计算统一使用 Albers 等积圆锥投影
(中央经线105E, 标准纬线25N/47N, Krassovsky 椭球), 参数在此声明并写入输出。
"""
import json
import math
import os
import sys
from datetime import datetime, timezone

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
PROCESSED = os.path.join(HERE, '..', 'processed')
_scope_value = os.environ.get('ANALYSIS_PROVINCE', '湖北省').strip()
SCOPE_PROVINCE = None if _scope_value in ('', 'ALL', '全国') else _scope_value
OUT = os.path.join(PROCESSED, 'analysis_hubei' if SCOPE_PROVINCE else 'analysis')
REPORTS = os.path.join(HERE, '..', 'reports')

DATA_VERSION = 'v1.0.0'
ALGORITHM_VERSION = 'heritage-analysis-v1'
CRS_PROJ = 'Albers_Con Equal_Area (lon_0=105, lat_1=25, lat_2=47, Krasovsky ellipsoid)'
CRS_IN = 'EPSG:4326 (WGS84)'

# ------------------------------------------------------------- Albers 投影
A_ELL = 6378245.0
E2 = 0.00669342162296594870166
LON0, LAT1, LAT2 = 105.0, 25.0, 47.0


def _m(lat):
    return math.cos(lat / 180 * math.pi) / math.sqrt(1 - E2 * math.sin(lat / 180 * math.pi) ** 2)


def _q(lat):
    s = math.sin(lat / 180 * math.pi)
    return (1 - E2) * (s / (1 - E2 * s * s) - (1 / (2 * math.sqrt(E2))) *
                       math.log((1 - math.sqrt(E2) * s) / (1 + math.sqrt(E2) * s)))


def _q_polar(lat):
    if abs(lat) >= 90:
        lat = math.copysign(89.999, lat)
    return _q(lat)


def albers_params():
    """Snyder(1987) 14-15/14-17: n=(m1²-m2²)/(q2-q1), C=m1²+n·q1。球面极限退化为
    n=(sinφ1+sinφ2)/2。"""
    m1_2, m2_2 = _m(LAT1) ** 2, _m(LAT2) ** 2
    q1, q2 = _q(LAT1), _q(LAT2)
    n = (m1_2 - m2_2) / (q2 - q1)
    C = m1_2 + n * q1
    rho0 = A_ELL * math.sqrt(C - n * _q(0)) / n
    return n, C, rho0


N_PARAM, C_PARAM, RHO0 = albers_params()


def project(lon, lat):
    """WGS84 经纬度 -> Albers 等积平面坐标(米)。"""
    rho = A_ELL * math.sqrt(C_PARAM - N_PARAM * _q_polar(lat)) / N_PARAM
    theta = N_PARAM * (lon - LON0) * math.pi / 180
    return rho * math.sin(theta), RHO0 - rho * math.cos(theta)


def project_array(lons, lats):
    lons = np.asarray(lons, dtype=float)
    lats = np.asarray(lats, dtype=float)
    lat_rad = np.radians(lats)
    s = np.sin(lat_rad)
    q = (1 - E2) * (s / (1 - E2 * s * s) -
                    (1 / (2 * math.sqrt(E2))) *
                    np.log((1 - math.sqrt(E2) * s) / (1 + math.sqrt(E2) * s)))
    rho = A_ELL * np.sqrt(np.maximum(C_PARAM - N_PARAM * q, 0)) / N_PARAM
    theta = N_PARAM * np.radians(lons - LON0)
    x = rho * np.sin(theta)
    y = RHO0 - rho * np.cos(theta)
    return x, y


def inv_project(x, y):
    """Albers 平面坐标(米) -> WGS84 经纬度。纬度用牛顿迭代(弧度)解 q(lat)=q_val。"""
    x = float(x)
    y = float(y)
    rho = math.hypot(x, RHO0 - y)
    if N_PARAM < 0:
        rho = -rho
    theta = math.atan2(x, RHO0 - y)
    q_val = (C_PARAM - (rho * N_PARAM / A_ELL) ** 2) / N_PARAM
    lat_rad = math.asin(max(-1.0, min(1.0, q_val / 2)))
    for _ in range(40):
        s = math.sin(lat_rad)
        qf = (1 - E2) * (s / (1 - E2 * s * s) -
                         (1 / (2 * math.sqrt(E2))) *
                         math.log((1 - math.sqrt(E2) * s) / (1 + math.sqrt(E2) * s)))
        dq = 2 * (1 - E2) * math.cos(lat_rad) / (1 - E2 * s * s)
        step = (qf - q_val) / dq if abs(dq) > 1e-12 else 0.0
        lat_rad -= step
        if abs(step) < 1e-10:
            break
    lon = LON0 + (theta / N_PARAM) * 180.0 / math.pi
    return lon, lat_rad * 180.0 / math.pi


# ------------------------------------------------------------- KDE
def compute_kde(xy, cell_m=10000.0, bandwidth_m=None):
    """高斯核密度估计(2D, 等积投影坐标, 米)。带宽默认 Silverman 规则。
    返回 grid(行=纬向), extent(xmin,ymin,xmax,ymax), bandwidth。"""
    x, y = xy[:, 0], xy[:, 1]
    n = len(x)
    if bandwidth_m is None:
        sx, sy = np.std(x, ddof=1), np.std(y, ddof=1)
        bandwidth_m = 0.9 * min(sx, sy) * n ** (-1.0 / 6.0)
        bandwidth_m = max(bandwidth_m, 50000.0)  # 下限50km, 避免过小带宽
    pad = 3 * bandwidth_m
    xmin, xmax = x.min() - pad, x.max() + pad
    ymin, ymax = y.min() - pad, y.max() + pad
    nx = int((xmax - xmin) / cell_m) + 1
    ny = int((ymax - ymin) / cell_m) + 1
    gx = xmin + np.arange(nx) * cell_m
    gy = ymin + np.arange(ny) * cell_m
    grid = np.zeros((ny, nx), dtype=np.float32)
    norm = 1.0 / (n * 2 * math.pi * bandwidth_m ** 2)
    for i in range(n):
        cx = int((x[i] - xmin) / cell_m)
        cy = int((y[i] - ymin) / cell_m)
        r = int(3 * bandwidth_m / cell_m) + 1
        x0, x1 = max(0, cx - r), min(nx, cx + r + 1)
        y0, y1 = max(0, cy - r), min(ny, cy + r + 1)
        if x0 >= x1 or y0 >= y1:
            continue
        wx = gx[x0:x1] - x[i]
        wy = gy[y0:y1] - y[i]
        d2 = wx[None, :] ** 2 + wy[:, None] ** 2
        grid[y0:y1, x0:x1] += np.exp(-0.5 * d2 / bandwidth_m ** 2)
    grid *= norm
    return grid, (xmin, ymin, xmax, ymax), float(bandwidth_m)


def kde_to_png(grid, extent, path):
    """密度 -> 带透明度的 PNG(密度越高越暖)。返回 color_ramp 描述。"""
    g = grid / (grid.max() + 1e-12)
    g_img = np.flipud(g)  # PNG 行序从上到下
    rgba = np.zeros((*g_img.shape, 4), dtype=np.uint8)
    # 简易 ramp: 透明 -> 蓝 -> 青 -> 黄 -> 红
    stops = [
        (0.0, (0, 0, 0, 0)),
        (0.15, (34, 94, 168, 140)),
        (0.4, (29, 145, 192, 190)),
        (0.65, (254, 224, 144, 220)),
        (0.85, (244, 109, 67, 240)),
        (1.0, (178, 24, 43, 250)),
    ]
    for (t0, c0), (t1, c1) in zip(stops, stops[1:]):
        mask = (g_img >= t0) & (g_img <= t1)
        if t1 <= t0:
            continue
        f = np.where(mask, (g_img - t0) / (t1 - t0), 0)
        for k in range(4):
            ch = rgba[..., k]
            ch[mask] = (c0[k] + (c1[k] - c0[k]) * f[mask]).astype(np.uint8)
    Image.fromarray(rgba, 'RGBA').save(path)
    return {
        'type': 'linear_alpha_ramp',
        'stops': [{'t': t, 'rgba': list(c)} for t, c in stops],
        'value_range_note': 't 为密度值/最大密度; 最大密度见 kde_meta',
    }


# ------------------------------------------------------------- ANN / Moran
def average_nearest_neighbor(xy):
    from scipy.spatial import cKDTree
    n = len(xy)
    tree = cKDTree(xy)
    d, _ = tree.query(xy, k=2)  # k=2: 第一个是自己
    mean_obs = float(d[:, 1].mean())
    area = float((xy[:, 0].max() - xy[:, 0].min()) * (xy[:, 1].max() - xy[:, 1].min()))
    # 研究区面积用包含所有点的凸包面积更稳健
    from scipy.spatial import ConvexHull
    try:
        area = float(ConvexHull(xy).volume)  # 2D 情形 volume=面积, area=周长
    except Exception:
        pass
    density = n / area
    mean_random = 0.5 / math.sqrt(density)
    se = 0.26136 / math.sqrt(n * density)
    R = mean_obs / mean_random
    z = (mean_obs - mean_random) / se
    return {
        'n': n, 'mean_observed_m': round(mean_obs, 1),
        'mean_random_expected_m': round(mean_random, 1),
        'R': round(R, 4), 'z_score': round(z, 2),
        'area_m2': round(area, 1),
        'interpretation': ('聚集' if R < 1 else '随机/离散',),
        'interpretation_note': 'R<1 趋向聚集, R>1 趋向离散; 仅描述点格局, 不构成因果解释',
    }


def morans_i(values, coords, k=4):
    """全局 Moran's I, KNN(k) 二元权重(行标准化)。随机化近似 z 值。
    零方差(所有值相同)时返回 I=None 并注明, 不抛异常。"""
    from scipy.spatial import cKDTree
    x = np.asarray(values, dtype=float)
    n = len(x)
    tree = cKDTree(coords)
    d, idx = tree.query(coords, k=k + 1)
    W = np.zeros((n, n))
    for i in range(n):
        for j in idx[i][1:]:
            W[i, j] = 1
    W_row = W / W.sum(axis=1, keepdims=True)
    z = x - x.mean()
    denom = float((z ** 2).sum())
    if denom <= 0:
        return {
            'I': None, 'E_I': None, 'z_value': None, 'variance': None,
            'n_units': n, 'weights': f'KNN k={k} (row-standardized binary)',
            'note': 'zero variance: all values identical, index undefined',
        }
    I = (n / float(W.sum())) * float(z @ W_row @ z) / denom
    EI = -1.0 / (n - 1)
    # 随机化假设下的方差(Clift & Ord 1973)
    s0 = float(W.sum())
    s1 = sum((W[i, j] + W[j, i]) ** 2 for i in range(n) for j in range(n)) / 2.0
    s2 = float(((W.sum(axis=1) + W.sum(axis=0)) ** 2).sum())
    b2 = float((z ** 4).sum() / (denom ** 2) * n)
    var_n = (n * ((n * n - 3 * n + 3) * s1 - n * s2 + 3 * s0 * s0)
             - b2 * ((n * n - n) * s1 - 2 * n * s2 + 6 * s0 * s0)
             ) / ((n - 1) * (n - 2) * (n - 3) * s0 * s0) - EI ** 2
    z_val = (I - EI) / math.sqrt(var_n) if var_n > 0 else None
    return {
        'I': round(I, 4), 'E_I': round(EI, 4),
        'z_value': round(z_val, 3) if z_val is not None else None,
        'variance': round(var_n, 6) if var_n > 0 else None,
        'n_units': n, 'weights': f'KNN k={k} (row-standardized binary)',
    }


# ------------------------------------------------------------- DP 简化
def douglas_peucker(pts, tol):
    if len(pts) < 3:
        return pts
    keep = np.zeros(len(pts), dtype=bool)
    keep[0] = keep[-1] = True
    stack = [(0, len(pts) - 1)]
    while stack:
        i0, i1 = stack.pop()
        if i1 <= i0 + 1:
            continue
        a = np.array(pts[i0])
        seg = np.array(pts[i1]) - a
        L = float(np.hypot(seg[0], seg[1]))
        rel = np.asarray(pts[i0 + 1:i1], dtype=float) - a
        if L < 1e-9:
            # 闭合环首尾重合: 用到锚点的距离
            cross = np.hypot(rel[:, 0], rel[:, 1])
        else:
            cross = np.abs(seg[0] * rel[:, 1] - seg[1] * rel[:, 0]) / L
        imax = int(np.argmax(cross))
        if cross[imax] > tol:
            k = i0 + 1 + imax
            keep[k] = True
            stack.append((i0, k))
            stack.append((k, i1))
    return [p for p, k in zip(pts, keep) if k]


def simplify_ring(coords, tol_deg=0.008):
    ring = douglas_peucker([(float(x), float(y)) for x, y in coords], tol_deg)
    if len(ring) < 4:
        return None
    if ring[0] != ring[-1]:
        ring.append(ring[0])
    return ring


def main():
    os.makedirs(OUT, exist_ok=True)
    created = datetime.now(timezone.utc).isoformat(timespec='seconds')
    all_sites = json.load(open(os.path.join(PROCESSED, 'heritage_sites.json'), encoding='utf-8'))
    sites = [s for s in all_sites if s.get('province') == SCOPE_PROVINCE] if SCOPE_PROVINCE else all_sites
    if not sites:
        raise ValueError(f'analysis scope has no sites: {SCOPE_PROVINCE}')
    pts = [(r['longitude'], r['latitude']) for r in sites if r['longitude'] is not None]
    lons = np.array([p[0] for p in pts])
    lats = np.array([p[1] for p in pts])
    xy = np.column_stack(project_array(lons, lats))

    # ---- KDE
    grid, extent, bw = compute_kde(xy)
    png_path = os.path.join(OUT, 'kde_raster.png')
    ramp = kde_to_png(grid, extent, png_path)
    scope_label = SCOPE_PROVINCE or '全国'
    kde_meta = {
        'analysis_id': f'kde_{"hubei" if SCOPE_PROVINCE else "all"}_v1',
        'analysis_type': 'kernel_density_estimation',
        'data_version': DATA_VERSION,
        'algorithm_version': ALGORITHM_VERSION,
        'crs_input': CRS_IN, 'crs_analysis': CRS_PROJ,
        'kernel': 'gaussian', 'bandwidth_m': bw, 'bandwidth_rule': 'Silverman, min 50km',
        'cell_size_m': 10000.0,
        'grid_shape': list(grid.shape),
        'extent_proj': list(extent),
        'extent_wgs84_corners': [
            list(inv_project(extent[0], extent[3])),   # NW
            list(inv_project(extent[2], extent[3])),   # NE
            list(inv_project(extent[2], extent[1])),   # SE
            list(inv_project(extent[0], extent[1])),   # SW
        ],
        'max_density': float(grid.max()),
        'png_size': [int(grid.shape[1]), int(grid.shape[0])],
        'ramp': ramp,
        'created_at': created,
        'scope': scope_label,
        'note': '密度图仅展示空间分布强度; 不能解释成因。湖北样本量较小，仅作点位分布可视化。' if SCOPE_PROVINCE else '密度图仅展示空间分布强度; 不能解释成因',
    }
    json.dump(kde_meta, open(os.path.join(OUT, 'kde_meta.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)

    # ---- ANN
    ann = average_nearest_neighbor(xy)
    ann_stats = {'analysis_id': f'ann_{"hubei" if SCOPE_PROVINCE else "all"}_v1', 'analysis_type': 'average_nearest_neighbor',
                 'data_version': DATA_VERSION, 'algorithm_version': ALGORITHM_VERSION,
                 'crs_analysis': CRS_PROJ, 'created_at': created, 'scope': scope_label, 'result': ann,
                 'limitation': f'湖北仅{len(xy)}处点位，ANN仅作描述性参考，不用于推断因果或代表全省工业遗产总体。' if SCOPE_PROVINCE else None}
    json.dump(ann_stats, open(os.path.join(OUT, 'ann_stats.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)

    # ---- 省级统计 + Moran
    from collections import defaultdict
    prov_counts = defaultdict(int)
    for r in sites:
        if r['province']:
            prov_counts[r['province']] += 1
    prov_stats = sorted(prov_counts.items(), key=lambda kv: -kv[1])
    prov_index = json.load(open(os.path.join(PROCESSED, 'admin_index.json'),
                                encoding='utf-8'))
    prov_ad = {v['name']: ad for ad, v in prov_index.items() if v['level'] == 'province'}
    order = [p for p, _ in prov_stats]
    vals = [c for _, c in prov_stats]
    coords = np.array([prov_index[prov_ad[p]]['center'] for p in order], dtype=float)
    if len(vals) < 4:
        moran = {
            'I': None, 'E_I': None, 'z_value': None, 'variance': None,
            'n_units': len(vals), 'weights': None,
            'note': '研究范围只有一个省级单元，Moran\'s I 不适用。'
        }
    else:
        moran = morans_i(vals, coords, k=4)
    moran_stats = {
        'analysis_id': f'moran_{"hubei" if SCOPE_PROVINCE else "province"}_count_v1',
        'analysis_type': "global_morans_i",
        'data_version': DATA_VERSION, 'algorithm_version': ALGORITHM_VERSION,
        'unit': 'province', 'variable': 'heritage_count',
        'weights': moran['weights'],
        'crs_note': '邻接关系基于省会/省级中心点 KNN, 非面邻接',
        'result': moran,
        'created_at': created, 'scope': scope_label,
        'interpretation_note': ('省际遗产数量呈空间自相关(高-高或低-低聚集)'
                                if moran['z_value'] and moran['z_value'] > 1.96
                                else ('湖北范围只有一个省级单元，Moran\'s I 不适用'
                                      if len(vals) < 4 else '未发现显著空间自相关')),
        'limitation': ('湖北范围只有一个省级单元，不计算省际空间自相关。'
                       if len(vals) < 4 else '全局指数, 不能定位局部聚集区; 变量为计数, 受省域面积影响'),
    }
    json.dump(moran_stats, open(os.path.join(OUT, 'moran_stats.json'), 'w',
                                encoding='utf-8'), ensure_ascii=False, indent=1)

    json.dump({
        'analysis_id': 'province_stats_v1', 'data_version': DATA_VERSION,
        'created_at': created,
        'counts': [{'province': p, 'count': c} for p, c in prov_stats],
    }, open(os.path.join(OUT, 'province_stats.json'), 'w', encoding='utf-8'),
        ensure_ascii=False, indent=1)

    # ---- 省界 GeoJSON(GCJ-02 -> WGS84, DP 简化)
    gcj2wgs = __import__('normalize', fromlist=['gcj02_to_wgs84']).gcj02_to_wgs84
    nat = json.load(open(os.path.join(PROCESSED, 'provinces_gcj02_raw.json'),
                         encoding='utf-8'))
    feats = []
    for f in nat['features']:
        p = f['properties']
        if not p.get('adcode') or p.get('name') is None:
            continue
        if SCOPE_PROVINCE and p.get('name') != SCOPE_PROVINCE:
            continue
        g = f['geometry']
        geoms = []
        polys = [g['coordinates']] if g['type'] == 'Polygon' else g['coordinates']
        for poly in polys:
            outer = simplify_ring(poly[0])
            if outer:
                geoms.append([outer])
        for rings in geoms:
            wgs_rings = [[list(gcj2wgs(x, y)) for x, y in ring] for ring in rings]
            feats.append({'type': 'Feature',
                          'properties': {'adcode': p['adcode'], 'name': p['name'],
                                         'count': prov_counts.get(p['name'], 0)},
                          'geometry': {'type': 'Polygon', 'coordinates': wgs_rings}})
    gj = {'type': 'FeatureCollection',
          'metadata': {'crs': 'EPSG:4326 (WGS84)',
                       'note': '来源: DataV GeoAtlas 省界(GCJ-02), 已转换 WGS84 并 DP 简化(tol 0.008°)',
                       'data_version': DATA_VERSION, 'created_at': created,
                       'scope': scope_label},
          'features': feats}
    json.dump(gj, open(os.path.join(OUT, 'province_boundaries.geojson'), 'w',
                       encoding='utf-8'), ensure_ascii=False)

    # ---- 批次/行业分布
    batch_stats = {'analysis_id': f'descriptive_{"hubei" if SCOPE_PROVINCE else "all"}_v1', 'data_version': DATA_VERSION,
                   'created_at': created,
                   'scope': scope_label,
                   'by_batch': {}, 'by_industry': {}, 'by_province': {},
                   'core_item_categories': {}}
    for r in sites:
        b = f"第{r['initial_batch']}批"
        batch_stats['by_batch'][b] = batch_stats['by_batch'].get(b, 0) + 1
        ind = r['industry_category_l1']
        batch_stats['by_industry'][ind] = batch_stats['by_industry'].get(ind, 0) + 1
        pr = r['province'] or '未知'
        batch_stats['by_province'][pr] = batch_stats['by_province'].get(pr, 0) + 1
        for c in r['core_item_categories']:
            batch_stats['core_item_categories'][c] = \
                batch_stats['core_item_categories'].get(c, 0) + 1
    json.dump(batch_stats, open(os.path.join(OUT, 'batch_stats.json'), 'w',
                                encoding='utf-8'), ensure_ascii=False, indent=1)

    # ---- 总元数据
    json.dump({
        'data_version': DATA_VERSION, 'algorithm_version': ALGORITHM_VERSION,
        'scope': scope_label,
        'created_at': created,
        'crs_input': CRS_IN, 'crs_analysis': CRS_PROJ,
        'projection_params': {'lon_0': LON0, 'lat_1': LAT1, 'lat_2': LAT2,
                              'ellipsoid': 'Krassovsky 1940 (a=6378245, e2≈0.0066934)'},
        'inputs': ['processed/heritage_sites.geojson (WGS84)'],
        'outputs': ['kde_raster.png', 'ann_stats.json', 'moran_stats.json',
                    'province_stats.json', 'province_boundaries.geojson',
                    'batch_stats.json'],
        'reproducibility': ('ANALYSIS_PROVINCE=湖北省 python data-pipeline/scripts/analysis.py' if SCOPE_PROVINCE
                            else 'python data-pipeline/scripts/analysis.py'),
    }, open(os.path.join(OUT, 'analysis_results.json'), 'w', encoding='utf-8'),
        ensure_ascii=False, indent=1)

    print('KDE:', grid.shape, 'bw=', round(bw / 1000), 'km max=', round(float(grid.max()), 8))
    print('ANN:', json.dumps(ann, ensure_ascii=False))
    print("Moran's I:", json.dumps(moran, ensure_ascii=False))
    print('provinces:', len(prov_stats), 'boundaries:', len(feats))


if __name__ == '__main__':
    sys.exit(main())
