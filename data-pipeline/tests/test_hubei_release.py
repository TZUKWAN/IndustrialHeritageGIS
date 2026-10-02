import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FRONT = ROOT / 'src' / 'data' / 'heritage'
BACK = ROOT / 'python-backend' / 'opengis_backend' / 'data' / 'heritage'


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def test_public_bundle_is_hubei_and_frontend_backend_match():
    front_sites = load(FRONT / 'sites.json')
    back_sites = load(BACK / 'sites.json')
    assert len(front_sites) == 13
    assert {s['province'] for s in front_sites} == {'湖北省'}
    assert front_sites == back_sites

    front_meta = load(FRONT / 'meta.json')
    back_meta = load(BACK / 'meta.json')
    assert front_meta == back_meta
    assert front_meta['scope'] == '湖北省'
    assert front_meta['site_count'] == 13
    assert front_meta['cultural_profile_count'] == 13


def test_cultural_profiles_are_complete_and_source_bound():
    sites = load(FRONT / 'sites.json')
    cultural = load(FRONT / 'cultural.json')
    source_ids = {s['source_id'] for s in load(FRONT / 'sources.json')}
    assert set(cultural) == {s['heritage_id'] for s in sites}
    for profile in cultural.values():
        assert profile['carrier_types']
        assert len(profile['cultural_dimensions']) >= 4
        refs = set(profile['source_ids'])
        for dimension in profile['cultural_dimensions']:
            refs.update(dimension['source_ids'])
        for actor in profile.get('actors', []):
            refs.update(actor['source_ids'])
        assert refs
        assert refs <= source_ids


def test_hubei_classification_overrides_are_in_public_bundle():
    sites = {s['name']: s for s in load(FRONT / 'sites.json')}
    assert sites['湖北5133厂']['industry_category_l1'] == '机械装备'
    assert sites['二三四八蒲纺总厂']['industry_category_l1'] == '纺织工业'
    assert sites['青山热电厂']['industry_category_l1'] == '电力能源'


def test_hubei_analysis_declares_single_province_limit():
    analysis = load(FRONT / 'analysis' / 'analysis_results.json')
    moran = load(FRONT / 'analysis' / 'moran_stats.json')
    assert analysis['scope'] == '湖北省'
    assert moran['result']['I'] is None
    assert '不计算' in moran['limitation']


def test_hubei_inventory_is_source_bound_and_frontend_backend_match():
    front = load(FRONT / 'inventory.json')
    back = load(BACK / 'inventory.json')
    assert front == back
    assert front['scope'] == '湖北省'
    # The expansion inventory is intentionally monotonic: later research waves
    # may add records, but the first-pass coverage floor must remain achieved.
    assert len(front['records']) >= front['research_targets']['first_pass_minimum']
    assert front['research_targets']['first_pass_minimum'] == 170
    meta = load(FRONT / 'meta.json')
    assert meta['inventory_count'] == len(front['records'])
    source_ids = {s['source_id'] for s in load(FRONT / 'sources.json')}
    ids = [r['inventory_id'] for r in front['records']]
    assert len(ids) == len(set(ids))
    for row in front['records']:
        assert row['source_ids']
        assert set(row['source_ids']) <= source_ids
        assert row['geocode_status'] == 'pending'
        if row.get('cultural_evidence'):
            assert set(row['cultural_evidence']) == {
                'material_carriers', 'technical_memory',
                'social_memory', 'current_use_or_loss',
            }
