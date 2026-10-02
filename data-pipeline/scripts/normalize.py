# -*- coding: utf-8 -*-
"""把 7 批 interim 名单清洗、统一为 heritage_sites 主表, 并完成地理编码与质量报告。

产出:
  processed/heritage_sites.json   主表记录(每遗产一行)
  processed/heritage_sites.geojson  WGS84 点位
  processed/sources.json          批次名单来源表(A 级)
  reports/normalize_report.json   清洗/查重/分类/编码统计
  reports/geocoding_report.json   地理编码明细
  reports/duplicate_candidates.json 疑似重复(不自动合并, 仅同名同省跨批自动归并)

地理编码策略: 名单地址为省/市/区县级行政区文本, 用 DataV GeoAtlas 行政区划中心点
(原始 GCJ-02)定位, 统一转换为 WGS84 后使用; 转换算法与误差在 DATA_PROVENANCE 中说明。
绝不使用伪精确坐标: precision 字段如实标注 district_centroid / city_centroid / fuzzy_match。
"""
import difflib
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
INTERIM = os.path.join(HERE, '..', 'interim')
PROCESSED = os.path.join(HERE, '..', 'processed')
REPORTS = os.path.join(HERE, '..', 'reports')
CONFIG = os.path.join(HERE, '..', 'config')

# ---------------------------------------------------------------- 坐标转换
A = 6378245.0
EE = 0.00669342162296594323


def _transform_lat(x, y):
    ret = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y + 0.2 * abs(x)
    ret += (20.0 * math_sin(6.0 * x * PI) + 20.0 * math_sin(2.0 * x * PI)) * 2.0 / 3.0
    ret += (20.0 * math_sin(y * PI) + 40.0 * math_sin(y / 3.0 * PI)) * 2.0 / 3.0
    ret += (160.0 * math_sin(y / 12.0 * PI) + 320 * math_sin(y * PI / 30.0)) * 2.0 / 3.0
    return ret


def _transform_lng(x, y):
    ret = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1 * abs(x)
    ret += (20.0 * math_sin(6.0 * x * PI) + 20.0 * math_sin(2.0 * x * PI)) * 2.0 / 3.0
    ret += (20.0 * math_sin(x * PI) + 40.0 * math_sin(x / 3.0 * PI)) * 2.0 / 3.0
    ret += (150.0 * math_sin(x / 12.0 * PI) + 300.0 * math_sin(x / 30.0 * PI)) * 2.0 / 3.0
    return ret


PI = 3.1415926535897932384626433832795
import math as _m
math_sin = _m.sin


def out_of_china(lng, lat):
    return not (73.66 < lng < 135.05 and 3.86 < lat < 53.55)


def gcj02_to_wgs84(lng, lat):
    """GCJ-02 -> WGS84 近似逆变换(公开算法, 城区误差约 1-2 米, 记录于 DATA_PROVENANCE)。"""
    if out_of_china(lng, lat):
        return lng, lat
    dlat = _transform_lat(lng - 105.0, lat - 25.0)
    dlng = _transform_lng(lng - 105.0, lat - 25.0)
    radlat = lat / 180.0 * PI
    magic = _m.sin(radlat)
    magic = 1 - EE * magic * magic
    sqrtmagic = _m.sqrt(magic)
    dlat = (dlat * 180.0) / ((A * (1 - EE)) / (magic * sqrtmagic) * PI)
    dlng = (dlng * 180.0) / (A / sqrtmagic * _m.cos(radlat) * PI)
    return lng - dlng, lat - dlat


# ---------------------------------------------------------------- 地址解析
PROVINCE_FULL = {
    '北京': '北京市', '天津': '天津市', '上海': '上海市', '重庆': '重庆市',
    '河北': '河北省', '山西': '山西省', '内蒙古': '内蒙古自治区',
    '辽宁': '辽宁省', '吉林': '吉林省', '黑龙江': '黑龙江省', '江苏': '江苏省',
    '浙江': '浙江省', '安徽': '安徽省', '福建': '福建省', '江西': '江西省',
    '山东': '山东省', '河南': '河南省', '湖北': '湖北省', '湖南': '湖南省',
    '广东': '广东省', '广西': '广西壮族自治区', '海南': '海南省', '四川': '四川省',
    '贵州': '贵州省', '云南': '云南省', '西藏': '西藏自治区', '陕西': '陕西省',
    '甘肃': '甘肃省', '青海': '青海省', '宁夏': '宁夏回族自治区',
    '新疆': '新疆维吾尔自治区',
}
MUNICIPALITIES = {'北京市', '天津市', '上海市', '重庆市'}


def parse_address(addr):
    """把名单地址解析为 (province, city, [districts])。不做地理编码, 只做文本结构化。"""
    rest = addr.strip()
    province = None
    for short, full in PROVINCE_FULL.items():
        if rest.startswith(short):
            province = full
            rest = rest[len(short):]
            if rest.startswith(full[len(short):]):
                rest = rest[len(full) - len(short):]
            break
    city = None
    m = re.match(r'([\u4e00-\u9fa5]{2,9}?(?:市|地区|自治州|盟|林区|矿区))', rest)
    if m:
        city = m.group(1)
        rest = rest[m.end():]
    # 自治州: “xx彝族苗族自治区州”等特例不再展开
    districts = re.findall(r'([^、，,;；\s]{1,12}?(?:区|县|旗|市|林区|特区))(?![^、，,;；\s]*?(?:区|县|旗|市|林区|特区))', rest)
    if not districts:
        districts = re.findall(r'([^、，,;；\s]{1,12}?(?:区|县|旗|市|林区|特区))', rest)
    # 去掉“经济开发区”等非行政区尾缀干扰
    districts = [d for d in districts if not d.endswith(('开发区', '园区', '新城'))]
    return province, city, districts


# ---------------------------------------------------------------- 行业分类
INDUSTRY_RULES = [
    # (L1, 关键词) 顺序即优先级: 命中即停
    ('煤炭工业', ['煤矿', '煤田', '煤炭', '选煤', '焦化', '煤业', '矿务局', '煤窑',
                  '开滦']),
    ('石油天然气', ['油田', '石油', '炼油', '天然气', '油井', '钻井', '油矿']),
    ('核工业军工', ['核工业', '中核', '核动力', '核潜艇', '工程物理研究院', '铀',
                    '原子能', '兵工', '军工', '枪械', '火炮', '弹药', '掷弹筒',
                    '轻机枪', '步枪', '军械', '炸药', '火工', '机器局']),
    ('冶金', ['钢铁', '钢厂', '冶', '铁厂', '高炉', '轧钢', '炼钢', '炼铁', '铝厂',
              '镁厂', '有色', '熔炼', '铜冶炼', '轻合金', '合金', '铜加工', '压延']),
    ('金属与非金属采矿', ['钨矿', '锑矿', '锡矿', '金矿', '铜矿', '铁矿', '汞矿', '铅锌',
                          '矾矿', '明矾', '井盐', '盐矿', '岩盐', '矿选厂', '淘金',
                          '采矿', '矿山', '盐场', '盐湖', '盐田', '盐化', '粘土矿']),
    ('铁路交通', ['铁路', '机车', '车辆厂', '火车站', '机务段', '桥梁', '京张', '窄轨',
                  '森林铁路', '车站', '邮务', '邮政']),
    ('船舶工业', ['船厂', '船坞', '造船', '船舶', '船政', '航修']),
    ('航空航天', ['航空', '航天', '飞机', '火箭', '卫星', '试飞', '试车台', '强度试验',
                  '总装厂房']),
    ('电子通信', ['电子', '电报', '电话', '通信', '电信', '电台', '无线电', '广播',
                  '电视', '计算机', '半导体', '集成电路', '晶体管', '电子管', '收信',
                  '发信', '微电子', '授时', '发播', '短波', '长波']),
    ('电力能源', ['电厂', '发电', '水电站', '水电', '电力', '电网', '热电', '电站',
                  '供电', '水利枢纽', '电业', '煤气', '燃气', '自来水', '水厂']),
    ('医药化工', ['制药', '化工', '化学', '橡胶', '塑料', '化肥', '农药', '医药',
                  '抗生素', '纯碱', '涂料', '试剂', '香精', '香料']),
    ('纺织工业', ['纺织', '棉纺', '纱厂', '织布', '印染', '丝绸', '毛纺', '针织',
                  '化纤', '麻纺', '织造', '绢纺']),
    ('食品酿酒', ['酒厂', '酿酒', '烧锅', '窖池', '葡萄酒', '啤酒', '白兰地', '黄酒',
                  '醋', '酿造', '卷烟', '烟厂', '烟公司', '烟叶', '复烤', '糖厂',
                  '面粉', '粮油', '罐头', '茶厂', '茶叶', '乳品', '肉联', '酱油',
                  '醋厂', '汽水', '味精', '香粉厂', '蜜饯']),
    ('机械装备', ['机械', '机床', '机器厂', '重机', '起重机', '轴承', '阀门', '风动',
                  '工具厂', '仪表', '量具', '刃具', '砂轮', '电机厂', '动力机', '内燃机',
                  '拖拉机', '农机', '水泵', '空压机', '制冷', '压缩机', '汽车', '齿轮',
                  '冷冻机', '锅炉', '重型装备', '锻造', '水压机', '电器']),
    ('建材陶瓷', ['水泥', '玻璃', '陶瓷', '瓷厂', '瓷业', '砖瓦', '耐火', '建材',
                  '琉璃', '窑']),
    ('轻工业', ['造纸', '纸厂', '印刷', '钟表', '手表', '缝纫机', '自行车', '搪瓷',
                '火柴', '电池', '灯泡', '制笔', '制革', '皮鞋', '塑料花', '照相',
                '电影机械', '乐器', '造币', '墨厂', '湖笔', '笔厂', '电影制片',
                '摄影棚']),
]
L1_ORDER = [r[0] for r in INDUSTRY_RULES]

CORE_ITEM_RULES = [
    ('工业建筑与构筑物', ['厂房', '车间', '办公楼', '仓库', '大坝', '船坞', '井架',
                          '烟囱', '水塔', '码头', '桥梁', '老门头', '大楼', '楼', '坊',
                          '作坊', '工房', '库房', '窿', '洞', '宾馆', '招待所', '俱乐部',
                          '文化宫', '学校', '医院', '住所', '故居', '纪念碑', '旧址',
                          '建筑群', '构筑']),
    ('生产设备与工具', ['机', '炉', '釜', '塔', '泵', '床', '仪器', '仪表', '设备',
                        '器具', '工具', '钻头', '车头', '发电机', '变压器', '计算机',
                        '电镐', '机车', '车辆', '秤', '仪']),
    ('基础设施', ['铁路', '专用线', '管廊', '管线', '公路', '码头', '航道', '运河',
                  '电网', '变电站']),
    ('档案文献', ['档案', '图纸', '文件', '照片', '资料', '账册', '股票', '商标',
                  '书籍', '报刊', '手稿', '证书', '奖状', '题词', '录音', '影像']),
    ('工业产品', ['产品', '样品', '手表', '汽车', '飞机', '葡萄酒', '白酒', '香烟',
                  '电报机', '胶片']),
    ('工艺与技术', ['技艺', '工艺', '技术', '配方', '方法', '流程']),
]


def classify_industry(name, core_items, applicant=''):
    text = f'{name} {core_items} {applicant}'
    for l1, kws in INDUSTRY_RULES:
        hits = [k for k in kws if k in text]
        if hits:
            name_hits = [k for k in hits if k in name]
            return l1, {'matched_keywords': hits,
                        'name_hit': bool(name_hits),
                        'basis': 'keyword_rule_v1'}
    return '其他', {'matched_keywords': [], 'name_hit': False,
                    'basis': 'no_rule_matched'}


def classify_core_items(core_items):
    cats = []
    for cat, kws in CORE_ITEM_RULES:
        if any(k in core_items for k in kws):
            cats.append(cat)
    return cats or ['其他']


def load_scope_overrides():
    """加载经过人工审计的范围内分类覆盖，避免关键词优先级误分类。"""
    path = os.path.join(CONFIG, 'hubei_industry_overrides.json')
    if not os.path.exists(path):
        return {}
    data = json.load(open(path, encoding='utf-8'))
    return data.get('overrides', {})


# ---------------------------------------------------------------- 主流程
def stable_id(name, province, batch):
    key = f'{name}|{province}|{batch}'
    return 'HER-' + hashlib.md5(key.encode('utf-8')).hexdigest()[:12]


def name_key(name):
    return re.sub(r'[\s（）()。·,，-]', '', name)


def load_admin():
    return json.load(open(os.path.join(PROCESSED, 'admin_index.json'), encoding='utf-8'))


def match_admin(province, city, districts, admin, addr_text=''):
    """返回 (adcode, level, match_quality, note)。quality: exact/fuzzy/city_fallback/none"""
    prov_name = province
    cand_districts = {}
    for ad, v in admin.items():
        if v['level'] == 'district' and (not prov_name or v['province'] == prov_name) \
                and (not city or v['city'] == city or city in v['city'] or v['city'] in city):
            cand_districts[ad] = v
    notes = []
    for d in districts or []:
        exact = [ad for ad, v in cand_districts.items() if v['name'] == d]
        if exact:
            return exact[0], 'district', 'exact', ''
        # 去后缀核心前缀匹配: “镇宁县”->“镇宁布依族苗族自治县”
        core = re.sub(r'(区|县|旗|市|林区|特区)$', '', d)
        if len(core) >= 2:
            pref = [ad for ad, v in cand_districts.items()
                    if v['name'].startswith(core) and len(v['name']) <= len(core) + 8]
            if pref:
                notes.append(f'prefix_match:{d}->{admin[pref[0]]["name"]}')
                return pref[0], 'district', 'fuzzy', ';'.join(notes)
        fuzzy = difflib.get_close_matches(d, [v['name'] for v in cand_districts.values()],
                                          n=1, cutoff=0.6)
        if fuzzy:
            ad = [a for a, v in cand_districts.items() if v['name'] == fuzzy[0]][0]
            notes.append(f'district_fuzzy:{d}->{fuzzy[0]}')
            return ad, 'district', 'fuzzy', ';'.join(notes)
    # 区县失配: 城市(显式城市或地址中出现的城市核心名)
    city_core = re.sub(r'(市|地区|盟)$', '', city or '')
    for ad, v in admin.items():
        if v['level'] == 'city' and v['province'] == prov_name:
            vcore = re.sub(r'(市|地区|盟)$', '', v['name'])
            if (city and (v['name'] == city or vcore == city_core)) \
                    or (not city and len(vcore) >= 2 and vcore in (addr_text or '')):
                notes.append(f'city_fallback:{v["name"]}')
                return ad, 'city', 'city_fallback', ';'.join(notes)
    # 直辖市: 城区中心点用市级
    if prov_name in MUNICIPALITIES and city:
        for ad, v in admin.items():
            if v['level'] == 'province' and v['name'] == prov_name:
                notes.append(f'city_fallback:{city}')
                return ad, 'city', 'city_fallback', ';'.join(notes)
    if prov_name:
        for ad, v in admin.items():
            if v['level'] == 'province' and v['name'] == prov_name:
                notes.append('province_fallback')
                return ad, 'province', 'province_fallback', ';'.join(notes)
    return None, None, 'none', ''


def main():
    os.makedirs(PROCESSED, exist_ok=True)
    os.makedirs(REPORTS, exist_ok=True)
    admin = load_admin()
    batch_meta = {
        1: ('国家工业遗产名单（第一批）', None),
        2: ('国家工业遗产名单（第二批）', None),
        3: ('国家工业遗产名单（第三批）', None),
        4: ('国家工业遗产名单（第四批）', None),
        5: ('国家工业遗产名单（第五批）', None),
        6: ('第六批国家工业遗产名单', None),
        7: ('第七批国家工业遗产名单', None),
    }
    sources = []
    for b, (title, _u) in batch_meta.items():
        interim = json.load(open(os.path.join(INTERIM, f'batch{b}.json'), encoding='utf-8'))
        sources.append({
            'source_id': f'src-batch{b}',
            'source_type': 'government_document',
            'title': title,
            'publisher': '中华人民共和国工业和信息化部',
            'authority_level': 'A',
            'origin_file': interim['source_file'],
            'sha256': interim['source_sha256'],
            'url': None,
            'accessed_at': None,
            'notes': '工作空间原始名单文件, 见 data-pipeline/raw/; url 待联网采集阶段补充',
        })

    records = []
    geo_report = {'total': 0, 'exact_district': 0, 'fuzzy_district': 0,
                  'city_fallback': 0, 'province_fallback': 0, 'failed': 0,
                  'rows': []}
    dup_auto_merged = []
    by_key = {}
    raw_records = []

    for b in range(1, 8):
        interim = json.load(open(os.path.join(INTERIM, f'batch{b}.json'), encoding='utf-8'))
        for row in interim['rows']:
            name = row['name']
            aliases = []
            if row.get('approved_name') and row['approved_name'] != name:
                aliases.append(row['approved_name'])
            if row.get('applied_name') and row['applied_name'] not in ([name] + aliases):
                aliases.append(row['applied_name'])
            province, city, districts = parse_address(row['address_raw'])
            raw_records.append({
                'batch': b, 'no': row['no'], 'name': name,
                'address_raw': row['address_raw'],
                'province': province, 'city': city, 'districts': districts,
                'applicant_unit': row.get('applicant_unit', ''),
                'core_items': row['core_items'],
            })

    # 同名同省跨批自动归并(如第四批增补行)
    merged = {}
    for rec in raw_records:
        key = (name_key(rec['name']), rec['province'])
        if key in merged:
            merged[key]['batches'].append((rec['batch'], rec['no']))
            merged[key]['extra_core_items'].append({
                'batch': rec['batch'], 'core_items': rec['core_items']})
            merged[key]['core_items'] += '；' + rec['core_items']
            dup_auto_merged.append({
                'canonical': merged[key]['name'], 'province': rec['province'],
                'merged_batch': rec['batch'], 'merged_no': rec['no'],
                'rule': 'same_normalized_name_and_province'})
        else:
            rec['batches'] = [(rec['batch'], rec['no'])]
            rec['extra_core_items'] = []
            merged[key] = rec
    records_raw = list(merged.values())

    # 疑似重复(相似名, 不合并)
    dup_cands = []
    for i, a in enumerate(records_raw):
        for c in records_raw[i + 1:]:
            if a['province'] != c['province'] or not a['province']:
                continue
            ratio = difflib.SequenceMatcher(
                None, name_key(a['name']), name_key(c['name'])).ratio()
            if ratio >= 0.82 and name_key(a['name']) != name_key(c['name']):
                dup_cands.append({
                    'a': f"b{a['batches'][0][0]}#{a['batches'][0][1]} {a['name']}",
                    'b': f"b{c['batches'][0][0]}#{c['batches'][0][1]} {c['name']}",
                    'province': a['province'], 'similarity': round(ratio, 3),
                    'action': 'flag_only_not_merged'})

    for rec in records_raw:
        b0 = min(x[0] for x in rec['batches'])
        hid = stable_id(rec['name'], rec['province'] or '', b0)
        industry, cls_basis = classify_industry(
            rec['name'], rec['core_items'], rec.get('applicant_unit', ''))
        core_cats = classify_core_items(rec['core_items'])

        adcode, level, quality, note = match_admin(
            rec['province'], rec['city'], rec['districts'], admin,
            addr_text=rec['address_raw'])
        lon = lat = None
        gcj = None
        precision = None
        needs_review_geo = False
        if adcode and admin[adcode].get('center'):
            gcj = admin[adcode]['center']
            lon, lat = gcj02_to_wgs84(gcj[0], gcj[1])
            precision = {
                'district': 'district_centroid',
                'city': 'city_centroid',
                'province': 'province_centroid',
            }.get(level, 'unknown')
            if quality == 'fuzzy':
                needs_review_geo = True
            if level != 'district':
                needs_review_geo = True
            if len(rec['districts']) > 1:
                precision += '_multi_district'
                needs_review_geo = True
        else:
            quality = 'none' if quality == 'none' else quality
            needs_review_geo = True

        first_no = min(n for bb, n in rec['batches'] if bb == b0)
        r = {
            'heritage_id': hid,
            'name': rec['name'],
            'aliases': aliases,
            'initial_batch': b0,
            'batches': sorted({x[0] for x in rec['batches']}),
            'source_no': first_no,
            'recognition_years': [],   # 官方文件未含认定年份, 保留空, 待档案阶段补
            'province': rec['province'],
            'city': rec['city'],
            'district_county': '、'.join(rec['districts']) if rec['districts'] else '',
            'address_raw': rec['address_raw'],
            'address_components': {
                'district_adcodes': [adcode] if adcode else [],
                'district_names': rec['districts'],
            },
            'applicant_unit': rec.get('applicant_unit', ''),
            'core_items_raw': rec['core_items'],
            'core_item_categories': core_cats,
            'industry_category_l1': industry,
            'classification_basis': cls_basis,
            'founded_year': None,
            'production_start_year': None,
            'historical_period': [],
            'current_use': None,
            'longitude': lon,
            'latitude': lat,
            'coordinate_system': 'WGS84' if lon is not None else None,
            'geocode_source': 'DataV_GeoAtlas_admin_center' if gcj else None,
            'geocode_source_crs': 'GCJ-02',
            'geocode_gcj02': gcj,
            'geocode_adcode': adcode,
            'geocode_level': level,
            'geocode_quality': quality,
            'geocode_note': note,
            'geocode_precision': precision,
            'needs_review': {
                'geocode': needs_review_geo,
                'classification': industry == '其他',
                'duplicate': False,
            },
            'source_ids': [f'src-batch{x}' for x in sorted({y[0] for y in rec['batches']})],
            'enrichment_status': 'not_started',
            'data_version': 'v1.0.0',
        }
        records.append(r)

    # 关键词分类完成后应用人工审计覆盖；覆盖理由写入 classification_basis，保持可追溯。
    overrides = load_scope_overrides()
    for r in records:
        override = overrides.get(r['heritage_id'])
        if not override:
            continue
        r['industry_category_l1'] = override['industry_category_l1']
        r['classification_basis'] = {
            'matched_keywords': r['classification_basis'].get('matched_keywords', []),
            'name_hit': r['classification_basis'].get('name_hit', False),
            'basis': 'manual_scope_override_v1',
            'reason': override.get('reason', ''),
        }

    # 地理编码报告
    for r in records:
        geo_report['total'] += 1
        q = r['geocode_quality']
        if q == 'exact':
            geo_report['exact_district'] += 1
        elif q == 'fuzzy':
            geo_report['fuzzy_district'] += 1
        elif q == 'city_fallback':
            geo_report['city_fallback'] += 1
        elif q == 'province_fallback':
            geo_report['province_fallback'] += 1
        else:
            geo_report['failed'] += 1
        geo_report['rows'].append({
            'heritage_id': r['heritage_id'], 'name': r['name'],
            'batch': r['initial_batch'], 'address_raw': r['address_raw'],
            'quality': q, 'level': r['geocode_level'],
            'precision': r['geocode_precision'], 'note': r['geocode_note'],
            'lon': r['longitude'], 'lat': r['latitude'],
            'needs_review': r['needs_review']['geocode'],
        })

    # 完整度
    for r in records:
        fields = ['name', 'province', 'city', 'district_county', 'address_raw',
                  'core_items_raw', 'industry_category_l1', 'longitude', 'latitude']
        filled = sum(1 for f in fields if r.get(f))
        r['field_completeness'] = round(filled / len(fields) * 100)

    # 分类频数
    freq = {}
    for r in records:
        freq[r['industry_category_l1']] = freq.get(r['industry_category_l1'], 0) + 1

    json.dump(records, open(os.path.join(PROCESSED, 'heritage_sites.json'), 'w',
                            encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(sources, open(os.path.join(PROCESSED, 'sources.json'), 'w',
                            encoding='utf-8'), ensure_ascii=False, indent=1)

    feats = []
    for r in records:
        if r['longitude'] is None:
            continue
        feats.append({
            'type': 'Feature',
            'geometry': {'type': 'Point',
                         'coordinates': [r['longitude'], r['latitude']]},
            'properties': {'heritage_id': r['heritage_id'], 'name': r['name'],
                           'initial_batch': r['initial_batch'],
                           'province': r['province'], 'city': r['city'],
                           'industry_category_l1': r['industry_category_l1'],
                           'geocode_quality': r['geocode_quality'],
                           'geocode_precision': r['geocode_precision']},
        })
    gj = {'type': 'FeatureCollection',
          'metadata': {'crs': 'EPSG:4326 (WGS84)',
                       'note': '点坐标由 DataV 行政区划中心点(GCJ-02)转换为 WGS84',
                       'count': len(feats), 'data_version': 'v1.0.0'},
          'features': feats}
    json.dump(gj, open(os.path.join(PROCESSED, 'heritage_sites.geojson'), 'w',
                       encoding='utf-8'), ensure_ascii=False, indent=1)

    report = {
        'data_version': 'v1.0.0',
        'raw_rows': len(raw_records),
        'records': len(records),
        'auto_merged': dup_auto_merged,
        'duplicate_candidates': dup_cands,
        'geocoding': {k: v for k, v in geo_report.items() if k != 'rows'},
        'industry_freq': freq,
        'needs_review_geo': sum(1 for r in records if r['needs_review']['geocode']),
        'needs_review_classification': sum(1 for r in records
                                           if r['needs_review']['classification']),
        'completeness_avg': round(sum(r['field_completeness'] for r in records)
                                  / max(len(records), 1), 1),
    }
    json.dump(report, open(os.path.join(REPORTS, 'normalize_report.json'), 'w',
                           encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(geo_report, open(os.path.join(REPORTS, 'geocoding_report.json'), 'w',
                               encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump({'generated_from': 'normalize_report.auto_merged+duplicate_candidates'},
              open(os.path.join(REPORTS, 'duplicate_candidates.json'), 'w',
                   encoding='utf-8'), ensure_ascii=False, indent=1)

    print('records:', len(records))
    print('geocoding:', report['geocoding'])
    print('industry_freq:', json.dumps(freq, ensure_ascii=False))
    print('auto_merged:', len(dup_auto_merged), 'dup_candidates:', len(dup_cands))
    print('needs_review geo/class:', report['needs_review_geo'],
          report['needs_review_classification'])
    # 打印失败与模糊明细
    for row in geo_report['rows']:
        if row['quality'] in ('none', 'fuzzy', 'city_fallback', 'province_fallback'):
            print('  REVIEW:', row['batch'], row['name'], row['quality'],
                  row['note'], row['address_raw'])


if __name__ == '__main__':
    sys.exit(main())
