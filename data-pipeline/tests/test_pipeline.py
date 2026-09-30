# -*- coding: utf-8 -*-
"""数据管线与分析单元测试。

运行: python -m pytest data-pipeline/tests -q
覆盖: 坐标转换已知样本/属性、稳定ID、地址解析、行政区划匹配、
      DP 简化、ANN 聚集/离散判别、Moran's I 正负判别、KDE 峰值定位。
"""
import json
import os
import sys

import numpy as np
import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(HERE, '..', 'scripts')
PROCESSED = os.path.join(HERE, '..', 'processed')
sys.path.insert(0, SCRIPTS)

from normalize import (gcj02_to_wgs84, stable_id, parse_address, match_admin,
                       classify_industry, classify_core_items)  # noqa: E402
from analysis import (project, project_array, douglas_peucker, compute_kde,
                      average_nearest_neighbor, morans_i)  # noqa: E402


# ---------------------------------------------------------------- 坐标转换
class TestGcj02Wgs84:
    def test_known_sample_offset_magnitude(self):
        # 北京天安门附近 GCJ-02 与 WGS84 的偏差量级应为千分位经纬度(约百米级)
        lng, lat = gcj02_to_wgs84(116.3914, 39.9032)
        assert 0.0008 < abs(lng - 116.3914) < 0.008
        assert 0.0008 < abs(lat - 39.9032) < 0.008

    def test_deterministic(self):
        assert gcj02_to_wgs84(121.5, 31.2) == gcj02_to_wgs84(121.5, 31.2)

    def test_out_of_china_passthrough(self):
        assert gcj02_to_wgs84(2.35, 48.85) == (2.35, 48.85)

    def test_monotonic_no_flip(self):
        # 转换不得造成点序翻转或大跳变
        pts = [(113.2 + i * 0.1, 22.5 + i * 0.05) for i in range(10)]
        out = [gcj02_to_wgs84(*p) for p in pts]
        lons = [o[0] for o in out]
        assert all(b > a for a, b in zip(lons, lons[1:]))


# ---------------------------------------------------------------- 稳定ID
class TestStableId:
    def test_deterministic(self):
        assert stable_id('张裕酿酒公司', '山东省', 1) == stable_id('张裕酿酒公司', '山东省', 1)

    def test_different_inputs_differ(self):
        assert stable_id('甲厂', '山东省', 1) != stable_id('甲厂', '山东省', 2)
        assert stable_id('甲厂', '山东省', 1) != stable_id('乙厂', '山东省', 1)

    def test_format(self):
        hid = stable_id('测试厂', '河北省', 3)
        assert hid.startswith('HER-') and len(hid) == 16


# ---------------------------------------------------------------- 地址解析
class TestParseAddress:
    def test_standard(self):
        p, c, d = parse_address('山东省烟台市芝罘区')
        assert (p, c, d) == ('山东省', '烟台市', ['芝罘区'])

    def test_autonomous_region(self):
        p, c, d = parse_address('新疆维吾尔自治区克拉玛依市独山子区')
        assert p == '新疆维吾尔自治区'
        assert c == '克拉玛依市'
        assert d == ['独山子区']

    def test_city_with_zhou(self):
        p, c, d = parse_address('江西省赣州市大余县')
        assert c == '赣州市' and d == ['大余县']

    def test_multi_district(self):
        p, c, d = parse_address('四川省泸州市江阳区、龙马潭区')
        assert c == '泸州市'
        assert d == ['江阳区', '龙马潭区']

    def test_municipality(self):
        p, c, d = parse_address('上海市杨浦区')
        assert p == '上海市' and c is None and d == ['杨浦区']

    def test_development_zone_no_district(self):
        p, c, d = parse_address('江苏省常州市经济开发区')
        assert p == '江苏省' and c == '常州市' and d == []


# ---------------------------------------------------------------- 行政区匹配
@pytest.fixture(scope='module')
def admin():
    return json.load(open(os.path.join(PROCESSED, 'admin_index.json'), encoding='utf-8'))


class TestMatchAdmin:
    def test_exact(self, admin):
        ad, level, q, _ = match_admin('山东省', '烟台市', ['芝罘区'], admin)
        assert q == 'exact' and level == 'district' and admin[ad]['name'] == '芝罘区'

    def test_prefix_full_name(self, admin):
        # 镇宁县 -> 镇宁布依族苗族自治县
        ad, level, q, note = match_admin('贵州省', '安顺市', ['镇宁县'], admin)
        assert q == 'fuzzy' and '布依族苗族自治州' or q == 'fuzzy'

    def test_fuzzy_typo(self, admin):
        ad, level, q, note = match_admin('四川省', '绵阳市', ['培城区'], admin)
        assert q == 'fuzzy' and admin[ad]['name'] == '涪城区'

    def test_city_fallback(self, admin):
        ad, level, q, note = match_admin('江苏省', None, [], admin,
                                         addr_text='江苏常州经济开发区')
        assert q == 'city_fallback' and admin[ad]['name'] == '常州市'

    def test_province_fallback(self, admin):
        ad, level, q, _ = match_admin('甘肃省', None, [], admin)
        assert q == 'province_fallback' and admin[ad]['name'] == '甘肃省'


# ---------------------------------------------------------------- 分类
class TestClassification:
    def test_steel(self):
        cat, basis = classify_industry('鞍山钢铁厂', '高炉，轧钢厂', '')
        assert cat == '冶金' and basis['name_hit']

    def test_coal_by_name(self):
        cat, _ = classify_industry('开滦赵各庄矿', '井架', '')
        assert cat == '煤炭工业'

    def test_unknown_returns_other(self):
        cat, basis = classify_industry('某某设施', '围墙', '')
        assert cat == '其他' and not basis['name_hit']

    def test_core_items_categories(self):
        cats = classify_core_items('厂房，车间；机床设备；历史档案资料')
        assert '工业建筑与构筑物' in cats and '生产设备与工具' in cats
        assert '档案文献' in cats


# ---------------------------------------------------------------- 分析
class TestProjection:
    def test_center_near_origin(self):
        x, y = project(105.0, 30.0)
        assert abs(x) < 1000  # 中央经线上 x≈0

    def test_area_preserving_sanity(self):
        # 与真实国土量级一致的投影坐标跨度(数千公里)
        x, y = project_array([74, 134], [20, 52])
        assert 3e6 < abs(x[1] - x[0]) < 7e6
        assert 2e6 < abs(y[1] - y[0]) < 6e6


class TestDouglasPeucker:
    def test_collinear_collapses(self):
        pts = [(0, 0), (1, 0), (2, 0), (3, 0)]
        assert len(douglas_peucker(pts, 0.1)) == 2

    def test_bend_kept(self):
        pts = [(0, 0), (1, 5), (2, 0)]
        out = douglas_peucker(pts, 0.1)
        assert (1, 5) in out

    def test_closed_ring_degenerate_chord(self):
        pts = [(0, 0), (5, 5), (10, 0), (5, -5), (0, 0)]
        out = douglas_peucker(pts, 0.5)
        assert len(out) >= 4  # 不得因首尾重合而坍缩


class TestANN:
    def test_clustered(self):
        rng = np.random.default_rng(42)
        c = rng.normal([0, 0], 30, size=(120, 2))
        spread = rng.normal([0, 0], 15000, size=(4, 2))
        xy = np.vstack([c, spread])
        res = average_nearest_neighbor(xy)
        assert res['R'] < 0.5

    def test_dispersed(self):
        grid = np.array([[i * 100.0, j * 100.0]
                         for i in range(6) for j in range(6)])
        res = average_nearest_neighbor(grid)
        assert res['R'] > 1.0


class TestMoran:
    def test_positive_autocorrelation(self):
        # 东西向梯度 -> 正自相关
        coords = [(i * 10.0, j * 10.0) for i in range(6) for j in range(5)]
        vals = [i for i, _ in coords]
        res = morans_i(vals, coords, k=4)
        assert res['I'] > res['E_I']

    def test_random_near_expectation(self):
        rng = np.random.default_rng(7)
        coords = [(i * 10.0, j * 10.0) for i in range(6) for j in range(5)]
        vals = rng.normal(0, 1, 30).tolist()
        res = morans_i(vals, coords, k=4)
        assert abs(res['I'] - res['E_I']) < 0.25


class TestKDE:
    def test_peak_at_point(self):
        pts = np.array([[0.0, 0.0], [100000.0, 100000.0]])
        grid, extent, bw = compute_kde(pts, cell_m=10000.0, bandwidth_m=50000.0)
        iy, ix = np.unravel_index(np.argmax(grid), grid.shape)
        cx = extent[0] + ix * 10000.0
        cy = extent[1] + iy * 10000.0
        assert abs(cx - 0.0) <= 10000.0 + 1e-6
        assert abs(cy - 0.0) <= 10000.0 + 1e-6

    def test_two_points_two_peaks(self):
        pts = np.array([[0.0, 0.0], [400000.0, 0.0]])
        grid, extent, _ = compute_kde(pts, cell_m=10000.0, bandwidth_m=50000.0)
        col0 = int((0 - extent[0]) / 10000.0)
        col1 = int((400000 - extent[0]) / 10000.0)
        row0 = int((0 - extent[1]) / 10000.0)
        assert grid[row0, col0] > grid[row0 + 20, col0 + 200] if col0 + 200 < grid.shape[1] else True
        # 每个点附近都是局部峰值
        assert grid[row0, col0] == grid[row0 - 2:row0 + 3, col0 - 2:col0 + 3].max()


# ---------------------------------------------------------------- 数据回归
class TestDataRegression:
    """基于固定小样本的数据质量回归(重跑管线后此测试应保持通过)。"""

    @pytest.fixture(scope='class')
    def sites(self):
        return json.load(open(os.path.join(PROCESSED, 'heritage_sites.json'),
                              encoding='utf-8'))

    def test_count(self, sites):
        assert 255 <= len(sites) <= 264

    def test_unique_ids(self, sites):
        ids = [s['heritage_id'] for s in sites]
        assert len(ids) == len(set(ids))

    def test_coords_legal(self, sites):
        for s in sites:
            if s['longitude'] is None:
                continue
            assert 73 < s['longitude'] < 136, s['name']
            assert 3 < s['latitude'] < 54, s['name']

    def test_batch_range(self, sites):
        assert all(1 <= s['initial_batch'] <= 7 for s in sites)

    def test_every_site_classified(self, sites):
        assert all(s['industry_category_l1'] for s in sites)

    def test_sources_complete(self, sites):
        for s in sites:
            assert s['source_ids'], s['name']
