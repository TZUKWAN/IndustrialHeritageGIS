# -*- coding: utf-8 -*-
"""阶段6: 把 processed 数据导出为前端可打包的 src/data/heritage/ 数据包。

首屏地图只加载 sites.json(精简字段); 详情/事件/档案/关系由详情面板懒加载 details.json。
"""
import json
import os
import shutil
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..', '..')
PROCESSED = os.path.join(HERE, '..', 'processed')
MODEL = os.path.join(PROCESSED, 'model')
DEST = os.path.join(ROOT, 'src', 'data', 'heritage')
SCOPE_PROVINCE = os.environ.get('HERITAGE_PROVINCE', '湖北省').strip() or None
ANALYSIS_DIR = os.path.join(PROCESSED, 'analysis_hubei' if SCOPE_PROVINCE else 'analysis')
CONFIG = os.path.join(HERE, '..', 'config')

SITE_FIELDS = [
    'heritage_id', 'name', 'aliases', 'initial_batch', 'batches',
    'province', 'city', 'district_county', 'address_raw',
    'industry_category_l1', 'core_item_categories',
    'longitude', 'latitude', 'geocode_quality', 'geocode_precision',
    'geocode_level', 'needs_review', 'founded_year', 'founded_year_precision',
    'production_start_year', 'closure_year', 'recognition_years',
    'historical_period', 'current_use', 'enrichment_status',
    'field_completeness', 'source_ids',
]


def _load_or(path, default):
    if not os.path.exists(path):
        return default
    return json.load(open(path, encoding='utf-8'))


def _load_cultural_profiles():
    path = os.path.join(HERE, '..', 'enrichment', 'hubei_cultural_profiles.json')
    data = _load_or(path, {})
    profiles = data.get('profiles', {})
    if SCOPE_PROVINCE and data.get('scope') != SCOPE_PROVINCE:
        raise ValueError(f'cultural profile scope mismatch: {data.get("scope")}')
    return profiles


def _load_inventory():
    """湖北全量扩展底册：省/市名录和来源确认候选，不混入国家名录 sites。"""
    path = os.path.join(PROCESSED, 'hubei_inventory.json')
    data = _load_or(path, {})
    if data and data.get('scope') != '湖北省':
        raise ValueError(f'inventory scope mismatch: {data.get("scope")}')
    return data


def _apply_scope_overrides(sites):
    path = os.path.join(CONFIG, 'hubei_industry_overrides.json')
    data = _load_or(path, {})
    overrides = data.get('overrides', {})
    for site in sites:
        override = overrides.get(site.get('heritage_id'))
        if not override:
            continue
        site['industry_category_l1'] = override['industry_category_l1']
        basis = dict(site.get('classification_basis') or {})
        basis.update({'basis': 'manual_scope_override_v1', 'reason': override.get('reason', '')})
        site['classification_basis'] = basis
        site.setdefault('needs_review', {})['classification'] = False
    return sites


def main():
    os.makedirs(os.path.join(DEST, 'analysis'), exist_ok=True)
    all_sites = json.load(open(os.path.join(PROCESSED, 'heritage_sites.json'),
                               encoding='utf-8'))
    sites = [s for s in all_sites if s.get('province') == SCOPE_PROVINCE] if SCOPE_PROVINCE else all_sites
    sites = _apply_scope_overrides(sites)
    if not sites:
        raise ValueError(f'export scope has no sites: {SCOPE_PROVINCE}')
    all_events = _load_or(os.path.join(MODEL, 'heritage_events.json'), [])
    all_relations = _load_or(os.path.join(MODEL, 'heritage_relations.json'), [])
    all_profiles = _load_or(os.path.join(MODEL, 'heritage_profiles.json'), {})
    all_sources = json.load(open(os.path.join(PROCESSED, 'sources.json'),
                                 encoding='utf-8'))
    inventory = _load_inventory()
    cultural = _load_cultural_profiles()
    missing_cultural = sorted({s['heritage_id'] for s in sites} - set(cultural))
    if missing_cultural:
        raise ValueError(f'missing cultural profiles: {missing_cultural}')
    scoped_ids = {s['heritage_id'] for s in sites}
    events = [e for e in all_events if e.get('heritage_id') in scoped_ids]
    relations = [r for r in all_relations if r.get('source_entity') in scoped_ids]
    profiles = {hid: p for hid, p in all_profiles.items() if hid in scoped_ids}
    used_source_ids = set()
    for s in sites:
        used_source_ids.update(s.get('source_ids') or [])
    for row in events + relations:
        used_source_ids.update(row.get('source_ids') or [])
    for p in cultural.values():
        used_source_ids.update(p.get('source_ids') or [])
        for d in p.get('cultural_dimensions') or []:
            used_source_ids.update(d.get('source_ids') or [])
        for actor in p.get('actors') or []:
            used_source_ids.update(actor.get('source_ids') or [])
    for row in inventory.get('records') or []:
        used_source_ids.update(row.get('source_ids') or [])
    sources = [s for s in all_sources if s.get('source_id') in used_source_ids]

    minimal = [{k: s.get(k) for k in SITE_FIELDS} for s in sites]
    details = {s['heritage_id']: s for s in sites}
    json.dump(minimal, open(os.path.join(DEST, 'sites.json'), 'w',
                            encoding='utf-8'), ensure_ascii=False)
    json.dump(details, open(os.path.join(DEST, 'details.json'), 'w',
                            encoding='utf-8'), ensure_ascii=False)
    json.dump(events, open(os.path.join(DEST, 'events.json'), 'w',
                           encoding='utf-8'), ensure_ascii=False)
    json.dump(relations, open(os.path.join(DEST, 'relations.json'), 'w',
                              encoding='utf-8'), ensure_ascii=False)
    json.dump(profiles, open(os.path.join(DEST, 'profiles.json'), 'w',
                             encoding='utf-8'), ensure_ascii=False)
    json.dump(sources, open(os.path.join(DEST, 'sources.json'), 'w',
                            encoding='utf-8'), ensure_ascii=False)
    json.dump(cultural, open(os.path.join(DEST, 'cultural.json'), 'w',
                             encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(inventory, open(os.path.join(DEST, 'inventory.json'), 'w',
                              encoding='utf-8'), ensure_ascii=False, indent=1)

    # 分析产物
    adir = ANALYSIS_DIR
    for f in ['batch_stats.json', 'ann_stats.json', 'moran_stats.json',
              'province_stats.json', 'province_boundaries.geojson',
              'kde_meta.json', 'analysis_results.json']:
        if not os.path.exists(os.path.join(adir, f)):
            raise FileNotFoundError(f'analysis artifact missing: {os.path.join(adir, f)}')
        shutil.copy(os.path.join(adir, f), os.path.join(DEST, 'analysis', f))
    # 前端用 .json 扩展名(vite 原生 JSON 模块解析; .geojson 会被当作二进制资产)
    shutil.copy(os.path.join(adir, 'province_boundaries.geojson'),
                os.path.join(DEST, 'analysis', 'province_boundaries.json'))
    shutil.copy(os.path.join(adir, 'kde_raster.png'),
                os.path.join(DEST, 'analysis', 'kde_raster.png'))

    meta = {
        'data_version': sites[0].get('data_version', 'v1.1.0') if sites else None,
        'scope': SCOPE_PROVINCE or '全国',
        'scope_type': 'province' if SCOPE_PROVINCE else 'national',
        'generated_at': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'site_count': len(sites),
        'event_count': len(events),
        'relation_count': len(relations),
        'source_count': len(sources),
        'enriched_sites': sum(1 for s in sites
                              if s.get('enrichment_status') == 'verified'),
        'cultural_profile_count': len(cultural),
        'inventory_count': len(inventory.get('records') or []),
        'inventory_source_confirmed_count': sum(
            1 for r in inventory.get('records') or []
            if r.get('record_status') == 'source_confirmed'
        ),
        'inventory_recognized_count': sum(
            1 for r in inventory.get('records') or []
            if r.get('recognition_level') in (
                'national', 'provincial', 'municipal', 'county',
                'municipal_historical_building', 'provincial_heritage_related',
                'enterprise_heritage'
            )
            and r.get('recognition_status') not in ('拟认定', '候选')
        ),
        'inventory_target_minimum': (inventory.get('research_targets') or {}).get(
            'first_pass_minimum'),
        'sources_of_truth': 'data-pipeline/ (raw -> interim -> processed -> src/data)',
    }
    json.dump(meta, open(os.path.join(DEST, 'meta.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)

    # 同步一份给 Python 后端 agent 工具使用(随应用分发)。必须在 meta 写入后复制，避免残留旧范围元数据。
    backend_dir = os.path.join(ROOT, 'python-backend', 'opengis_backend', 'data', 'heritage')
    os.makedirs(backend_dir, exist_ok=True)
    for f in ['sites.json', 'details.json', 'events.json', 'relations.json',
              'profiles.json', 'sources.json', 'cultural.json', 'inventory.json', 'meta.json']:
        shutil.copy(os.path.join(DEST, f), os.path.join(backend_dir, f))

    total = 0
    for root, _, files in os.walk(DEST):
        for f in files:
            total += os.path.getsize(os.path.join(root, f))
    print('exported to src/data/heritage:', meta)
    print('bundle size:', round(total / 1024), 'KB')


if __name__ == '__main__':
    sys.exit(main())
