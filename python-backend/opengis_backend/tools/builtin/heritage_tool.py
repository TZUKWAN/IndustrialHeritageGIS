"""heritage_data tool — 工业文化遗产GIS智能体 内置数据集查询。

让 Agent 能基于本地结构化数据回答湖北工业文化遗产相关问题:
搜索/详情/时间线/统计。回答必须引用工具返回的 source_id;
数据中没有的情报必须回答"当前数据库尚无足够证据", 不得补全。
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

from opengis_backend.tools.context import ToolContext
from opengis_backend.tools.registry import tool

logger = logging.getLogger(__name__)

_MAX_RESULTS = 25

_CACHE: dict[str, Any] = {}


def _data_dir() -> Path:
    here = Path(__file__).resolve()
    # builtin/heritage_tool.py → tools/ → opengis_backend/ → data/heritage
    for cand in (
        here.parent.parent.parent / 'data' / 'heritage',
        here.parent.parent.parent.parent / 'src' / 'data' / 'heritage',
    ):
        if (cand / 'sites.json').exists():
            return cand
    return here.parent.parent.parent / 'data' / 'heritage'


def _load(name: str) -> Any:
    if name not in _CACHE:
        path = _data_dir() / name
        if not path.exists():
            _CACHE[name] = None
        else:
            with open(path, encoding='utf-8') as f:
                _CACHE[name] = json.load(f)
    return _CACHE[name]


def _site_brief(s: dict) -> dict:
    return {
        'heritage_id': s.get('heritage_id'),
        'name': s.get('name'),
        'initial_batch': s.get('initial_batch'),
        'batches': s.get('batches'),
        'province': s.get('province'),
        'city': s.get('city'),
        'district': s.get('district_county'),
        'industry': s.get('industry_category_l1'),
        'founded_year': s.get('founded_year'),
        'enrichment_status': s.get('enrichment_status'),
        'scope': '湖北省',
    }


def _iter_sites() -> list[dict]:
    return _load('sites.json') or []


def _iter_inventory() -> list[dict]:
    data = _load('inventory.json') or {}
    return data.get('records') or []


def _match_inventory(query: str, city: str | None = None,
                     recognition_level: str | None = None) -> list[dict]:
    out = []
    q = (query or '').strip().lower()
    for row in _iter_inventory():
        if city and city not in (row.get('city') or ''):
            continue
        if recognition_level and row.get('recognition_level') != recognition_level:
            continue
        if q:
            hay = ' '.join(str(x) for x in [
                row.get('name'), *(row.get('aliases') or []), row.get('city'),
                row.get('district_county'), row.get('industry_category_l1'),
                row.get('recognition_level'), row.get('recognition_status'),
                row.get('notes'),
            ] if x).lower()
            if q not in hay:
                continue
        out.append(row)
    return out


def _match_sites(query: str, batch: int | None, province: str | None,
                 industry: str | None, period: str | None) -> list[dict]:
    out = []
    q = (query or '').strip().lower()
    for s in _iter_sites():
        if batch is not None and batch not in (s.get('batches') or []):
            continue
        if province and province not in (s.get('province') or ''):
            continue
        if industry and industry not in (s.get('industry_category_l1') or ''):
            continue
        if period and period not in (s.get('historical_period') or []):
            continue
        if q:
            hay = ' '.join(str(x) for x in [
                s.get('name'), *(s.get('aliases') or []),
                s.get('province'), s.get('city'), s.get('district_county'),
                s.get('industry_category_l1'), s.get('current_use'),
            ] if x).lower()
            if q not in hay:
                continue
        out.append(s)
    return out


@tool(
    name='heritage_data',
    display_name='工业遗产数据查询',
    description=(
        '查询内置的湖北省国家工业文化遗产数据集(13处国家工业遗产,第1-7批)。'
        'actions: search=按关键词/批次/省份/行业/历史时期检索; '
        'detail=单处遗产完整档案(含事件与来源); '
        'timeline=单处遗产的时间线事件; stats=按当前筛选的统计。'
        '另有 inventory 动作查询国家名录之外的湖北省级、市级、研究名录和来源确认候选底册。'
        'detail 还返回文化载体、技术/技艺、组织与人物、社会记忆、保护利用和资料边界。'
        '回答历史问题时必须只使用本工具返回的内容并注明 source_id; '
        '数据未覆盖的内容要明确说"当前数据库尚无足够证据"。'
    ),
    category='heritage',
    params=[
        {'name': 'action', 'type': 'enum',
         'options': ['search', 'detail', 'timeline', 'stats', 'inventory'],
         'description': '查询动作。'},
        {'name': 'query', 'type': 'string',
         'description': 'search 的关键词(名称/别名/城市/行业/事件词)。'},
        {'name': 'batch', 'type': 'number',
         'description': '限定认定批次 1-7。'},
        {'name': 'province', 'type': 'string',
         'description': '限定省份(如 山东省)。'},
        {'name': 'city', 'type': 'string',
         'description': 'inventory 可限定地市(如 武汉市、黄石市)。'},
        {'name': 'industry', 'type': 'string',
         'description': '限定行业一级分类(如 煤炭工业)。'},
        {'name': 'period', 'type': 'string',
         'description': '限定历史时期(如 一五二五时期/三线建设时期)。'},
        {'name': 'heritage_id', 'type': 'string',
         'description': 'detail/timeline 需要的遗产ID(HER-开头, 先用 search 获得)。'},
        {'name': 'recognition_level', 'type': 'string',
         'description': 'inventory 可限定 national/provincial/municipal/county/provincial_proposed 等层级。'},
    ],
    returns=(
        'dict: search→results[]+total; detail→site+events+profile+sources; '
        'timeline→events[]; stats→counts(by_batch/by_province/by_industry)+total; '
        'inventory→国家名录之外的扩展对象及来源ID'
    ),
    examples=[
        "heritage_data(action='search', query='钢铁', batch=1)",
        "heritage_data(action='detail', heritage_id='HER-3318e785a779')",
        "heritage_data(action='stats', province='湖北省')",
    ],
    needs_context=False,
)
def heritage_data(
    action: str = 'search',
    query: str | None = None,
    batch: float | None = None,
    province: str | None = None,
    city: str | None = None,
    industry: str | None = None,
    period: str | None = None,
    heritage_id: str | None = None,
    recognition_level: str | None = None,
) -> dict[str, Any]:
    b = int(batch) if batch is not None else None
    if action == 'search':
        matched = _match_sites(query or '', b, province, industry, period)
        return {
            'total': len(matched),
            'truncated': len(matched) > _MAX_RESULTS,
            'results': [_site_brief(s) for s in matched[:_MAX_RESULTS]],
        }

    if action in ('detail', 'timeline'):
        site = next((s for s in _iter_sites() if s.get('heritage_id') == heritage_id), None)
        if site is None:
            return {'error': f'heritage_id {heritage_id} not found; 先用 action=search 查找'}
        events = [e for e in (_load('events.json') or [])
                  if e.get('heritage_id') == heritage_id]
        events.sort(key=lambda e: str(e.get('event_date_start') or '9999'))
        if action == 'timeline':
            return {'heritage_id': heritage_id, 'name': site.get('name'),
                    'events': [
                        {k: e.get(k) for k in (
                            'event_id', 'event_date_start', 'date_precision',
                            'event_type', 'title', 'description', 'source_ids',
                            'disputed')}
                        for e in events]}

        profile = (_load('profiles.json') or {}).get(heritage_id) or {}
        cultural = (_load('cultural.json') or {}).get(heritage_id) or None
        src_ids_set = {sid for e in events for sid in e.get('source_ids', [])}
        if cultural:
            src_ids_set.update(cultural.get('source_ids') or [])
            for dimension in cultural.get('cultural_dimensions') or []:
                src_ids_set.update(dimension.get('source_ids') or [])
            for actor in cultural.get('actors') or []:
                src_ids_set.update(actor.get('source_ids') or [])
        src_ids = sorted(src_ids_set)
        all_sources = {s['source_id']: s for s in (_load('sources.json') or [])}
        detail = _load('details.json') or {}
        full = detail.get(heritage_id) or site
        return {
            'site': {k: full.get(k) for k in (
                'heritage_id', 'name', 'aliases', 'batches', 'recognition_years',
                'province', 'city', 'district_county', 'address_raw',
                'industry_category_l1', 'core_items_raw', 'founded_year',
                'production_start_year', 'closure_year', 'historical_period',
                'current_use', 'geocode_precision', 'needs_review',
                'data_version')},
            'profile': {k: profile.get(k) for k in (
                'overview', 'origin_story', 'development_story',
                'transformation_story', 'recognition_story', 'research_status',
                'note')} if profile else None,
            'people': profile.get('people', []) if profile else [],
            'cultural_profile': cultural,
            'events': events,
            'sources': [all_sources.get(sid) for sid in src_ids if all_sources.get(sid)],
        }

    if action == 'stats':
        matched = _match_sites(query or '', b, province, industry, period)

        def count(key):
            out: dict[str, int] = {}
            for s in matched:
                v = s.get(key)
                if isinstance(v, list):
                    for item in v:
                        out[str(item)] = out.get(str(item), 0) + 1
                elif v:
                    out[str(v)] = out.get(str(v), 0) + 1
            return dict(sorted(out.items(), key=lambda kv: -kv[1]))

        return {
            'total': len(matched),
            'by_batch': count('initial_batch'),
            'by_province': count('province'),
            'by_industry': count('industry_category_l1'),
            'data_version': (_load('meta.json') or {}).get('data_version'),
            'scope': (_load('meta.json') or {}).get('scope', '湖北省'),
        }

    if action == 'inventory':
        matched = _match_inventory(query or '', city=city,
                                   recognition_level=recognition_level)
        data = _load('inventory.json') or {}
        all_sources = {s['source_id']: s for s in (_load('sources.json') or [])}
        return {
            'total': len(matched),
            'truncated': len(matched) > _MAX_RESULTS,
            'target_minimum': (data.get('research_targets') or {}).get('first_pass_minimum'),
            'results': matched[:_MAX_RESULTS],
            'sources': [all_sources[sid] for row in matched[:_MAX_RESULTS]
                        for sid in row.get('source_ids', []) if sid in all_sources],
            'scope': data.get('scope', '湖北省'),
        }

    return {'error': f'unknown action: {action}'}
