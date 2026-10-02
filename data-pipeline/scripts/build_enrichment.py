# -*- coding: utf-8 -*-
"""阶段3/4: 把联网采集的结构化史实(enrichment JSON)与批次认定信息合并进数据模型。

输入:
  data-pipeline/enrichment/pilot_*.json   研究员输出的遗产史实数组
  data-pipeline/enrichment/batch_dates.json  7批认定日期/URL 核实结果

输出 (processed/model/；默认保留全国追溯模型，公开发布时由 `export_frontend.py` 切片为湖北):
  heritage_events.json     事件表(含全体遗产的“遗产认定”事件)
  heritage_relations.json  关系表
  heritage_profiles.json   可阅读档案(全部段落由事件+主表字段程序化生成, 可溯源)
  sources.json             来源总表(A/B/C/D 分级)

铁律: 档案只由事件生成; 无事件的遗产档案为空并标 insufficient; 不编造。
"""
import hashlib
import json
import os
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ENRICH = os.path.join(HERE, '..', 'enrichment')
PROCESSED = os.path.join(HERE, '..', 'processed')
MODEL = os.path.join(PROCESSED, 'model')

BATCH_TITLES = {
    1: '国家工业遗产名单（第一批）', 2: '国家工业遗产名单（第二批）',
    3: '国家工业遗产名单（第三批）', 4: '国家工业遗产名单（第四批）',
    5: '国家工业遗产名单（第五批）', 6: '第六批国家工业遗产名单',
    7: '第七批国家工业遗产名单',
}

EVENT_TYPE_RECOGNITION = '遗产认定'
PERIOD_BOUNDS = [
    ('晚清近代工业', 1840, 1911),
    ('民国时期', 1912, 1948),
    ('新中国初期', 1949, 1952),
    ('一五二五时期', 1953, 1965),
    ('三线建设时期', 1964, 1980),
    ('改革开放后', 1978, 2026),
]


def period_tags_for_years(years):
    tags = set()
    for y in years:
        if y is None:
            continue
        for name, lo, hi in PERIOD_BOUNDS:
            if lo <= y <= hi:
                tags.add(name)
    return sorted(tags, key=lambda t: PERIOD_BOUNDS[[p[0] for p in PERIOD_BOUNDS].index(t)][1])


def norm_url_key(url):
    return hashlib.md5((url or '').strip().encode('utf-8')).hexdigest()[:10]


def load_json(path):
    if not os.path.exists(path):
        return None
    return json.load(open(path, encoding='utf-8'))


def main():
    os.makedirs(MODEL, exist_ok=True)
    sites = json.load(open(os.path.join(PROCESSED, 'heritage_sites.json'),
                           encoding='utf-8'))
    site_by_id = {s['heritage_id']: s for s in sites}
    now = datetime.now(timezone.utc).isoformat(timespec='seconds')
    data_version = 'v1.1.0'

    sources = load_json(os.path.join(PROCESSED, 'sources.json')) or []
    # 就地按 source_id 去重(防御历史运行造成的重复累积)
    _seen = set()
    _dedup = []
    for _s in sources:
        if _s['source_id'] not in _seen:
            _seen.add(_s['source_id'])
            _dedup.append(_s)
    sources = _dedup
    batch_date_src = {}
    bd = load_json(os.path.join(ENRICH, 'batch_dates.json')) or {}
    for b in bd.get('batches', []):
        sid = f'src-batch{b["batch"]}'
        for s in sources:
            if s['source_id'] == sid:
                if b.get('announcement_date'):
                    s['publication_date'] = b['announcement_date']
                if b.get('url'):
                    s['url'] = b['url']
                s['accessed_at'] = b.get('accessed_at')
                s['authority_level'] = 'A'
                if b.get('doc_number'):
                    marker = '公告文号: ' + b['doc_number']
                    notes = s.get('notes') or ''
                    # 兼容历史重复运行产生的重复标记，并保持该步骤幂等。
                    prefix = notes.split(marker, 1)[0].rstrip()
                    s['notes'] = (prefix + ' ' + marker).strip()
        batch_date_src[b['batch']] = b

    # ---- 网络来源合并
    web_sources = {}
    web_sid_by_key = {}
    def src_id_for(src):
        key = norm_url_key(src.get('url'))
        if key in web_sid_by_key:
            return web_sid_by_key[key]
        sid = f"src-web-{key}"
        web_sid_by_key[key] = sid
        web_sources[sid] = {
            'source_id': sid,
            'source_type': src.get('source_type', 'web'),
            'title': src.get('title', ''),
            'organization': src.get('org', ''),
            'author': None,
            'publication_date': src.get('pub_date'),
            'url': src.get('url'),
            'accessed_at': now,
            'authority_level': src.get('authority', 'D'),
            'notes': src.get('notes', ''),
        }
        return sid

    events = []
    relations = []
    founded = {}
    production = {}
    closure = {}
    period_tags = {}
    current_use = {}
    item_people = {}

    pilots = []
    for fname in sorted(os.listdir(ENRICH)):
        if not fname.startswith('pilot') or not fname.endswith('.json'):
            continue
        data = load_json(os.path.join(ENRICH, fname))
        if isinstance(data, dict):
            data = data.get('sites', [])
        pilots.extend(data)

    # ---- 湖北全量扩展底册
    # 这部分不是国家名录主表，不混入 heritage_sites；它保存省级、市级、研究名录
    # 和来源确认候选，供公开包/Agent 分层查询。source_ids 仍由 URL 统一生成，保证
    # 与事件和文化档案使用同一来源表、重复运行幂等。
    inventory_raw = load_json(os.path.join(ENRICH, 'hubei_inventory.json')) or {}
    inventory = []
    inventory_sources = inventory_raw.get('sources') or {}
    # 注册底册声明的全部来源，而不只登记当前记录直接引用的来源。
    # 文化档案可以引用同一底册来源（例如国家主表的补充考证），若只在
    # 逐条记录循环中注册，会造成发布包中文化档案 source_ids 无法回溯。
    for src in inventory_sources.values():
        src_id_for(src)
    for rec in inventory_raw.get('records') or []:
        row = dict(rec)
        source_ids = []
        for key in rec.get('source_keys') or []:
            src = inventory_sources.get(key)
            if not src:
                raise ValueError(f'inventory source key not found: {key}')
            source_ids.append(src_id_for(src))
        row['source_ids'] = sorted(set(source_ids))
        row.pop('source_keys', None)
        inventory.append(row)

    for item in pilots:
        hid = item.get('heritage_id')
        if hid not in site_by_id:
            print('  !! unknown heritage_id, skip:', hid)
            continue
        site = site_by_id[hid]
        sid_map = {}
        for i, s in enumerate(item.get('sources', [])):
            sid_map[i] = src_id_for(s)

        for fld, store in (('founded_year', founded),
                           ('production_start_year', production),
                           ('closure_year', closure)):
            v = item.get(fld)
            if isinstance(v, dict) and v.get('value'):
                store[hid] = {'value': int(v['value']),
                              'date_precision': v.get('date_precision', 'year'),
                              'source_ids': [sid_map.get(i) for i in v.get('source_idxs', [])
                                             if sid_map.get(i)]}
        if item.get('current_use'):
            current_use[hid] = item['current_use']
        period_tags[hid] = item.get('historical_period_tags') or []

        for i, ev in enumerate(item.get('events', [])):
            # 认定事件由本脚本依批次公告统一生成(A级, 精确日期), 跳过采集方自带版本
            if ev.get('event_type') == EVENT_TYPE_RECOGNITION:
                continue
            sids = [sid_map.get(x) for x in ev.get('source_idxs', []) if sid_map.get(x)]
            if not sids:
                continue
            events.append({
                'event_id': f'EVT-{hid.split("-")[1]}-{i + 1:02d}',
                'heritage_id': hid,
                'event_date_start': str(ev.get('date_start') or ''),
                'event_date_end': str(ev.get('date_end') or '') or None,
                'date_precision': ev.get('date_precision', 'year'),
                'event_type': ev.get('event_type', ''),
                'title': ev.get('title', ''),
                'description': ev.get('description', ''),
                'place_name': ev.get('place_name') or site.get('city'),
                'related_orgs': ev.get('related_orgs', []),
                'related_people': ev.get('related_people', []),
                'source_ids': sids,
                'confidence': ev.get('confidence', 'medium'),
                'disputed': bool(ev.get('disputed')),
                'notes': ev.get('notes', ''),
            })
        for p in item.get('people', []):
            ppl = item_people.setdefault(hid, {})
            ent = ppl.setdefault(p.get('name', ''), {'name': p.get('name', ''),
                                                     'roles': set(), 'source_ids': set()})
            if p.get('role'):
                ent['roles'].add(p['role'])
            ent['source_ids'].update(sid_map.get(i) for i in p.get('source_idxs', [])
                                     if sid_map.get(i))
        for i, rel in enumerate(item.get('relations', [])):
            sids = [sid_map.get(x) for x in rel.get('source_idxs', []) if sid_map.get(x)]
            relations.append({
                'relation_id': f'REL-{hid.split("-")[1]}-{i + 1:02d}',
                'source_entity': hid,
                'relation_type': rel.get('relation_type', ''),
                'target_entity': rel.get('target_entity', ''),
                'start_date': None, 'end_date': None,
                'description': rel.get('description', ''),
                'source_ids': sids,
                'confidence': 'medium',
                'inferred': bool(rel.get('inferred')),
            })

    # ---- 认定事件(全体遗产, 来源=批次公告 A级)
    for s in sites:
        for b in s['batches']:
            info = batch_date_src.get(b, {})
            date = info.get('announcement_date') or ''
            events.append({
                'event_id': f'EVT-{s["heritage_id"].split("-")[1]}-R{b}',
                'heritage_id': s['heritage_id'],
                'event_date_start': date,
                'event_date_end': None,
                'date_precision': info.get('date_precision', 'year') if date else 'unknown',
                'event_type': EVENT_TYPE_RECOGNITION,
                'title': f'入选{BATCH_TITLES.get(b, str(b) + "批")}',
                'description': f'被工业和信息化部公布为第{b}批国家工业遗产。',
                'place_name': None,
                'related_orgs': ['中华人民共和国工业和信息化部'],
                'related_people': [],
                'source_ids': [f'src-batch{b}'],
                'confidence': 'high',
                'disputed': bool(info.get('conflict_note')),
                'notes': info.get('conflict_note', ''),
            })

    events.sort(key=lambda e: (e['heritage_id'], e['event_date_start'] or 'zzzz'))

    # ---- 档案生成(仅由事件/主表字段, 每段附来源)
    ev_by_site = {}
    for e in events:
        ev_by_site.setdefault(e['heritage_id'], []).append(e)
    profiles = {}
    for s in sites:
        hid = s['heritage_id']
        evs = ev_by_site.get(hid, [])
        hist = [e for e in evs if e['event_type'] != EVENT_TYPE_RECOGNITION]
        recog = [e for e in evs if e['event_type'] == EVENT_TYPE_RECOGNITION]

        def cite(e):
            return '［' + '；'.join(e['source_ids']) + '］' 

        overview = (f"{s['name']}位于{s['province'] or ''}{s['city'] or ''}"
                    f"{s['district_county'] or ''}，属{s['industry_category_l1']}领域，"
                    f"第{s['initial_batch']}批入选国家工业遗产名录。")

        origin = [e for e in hist if e['event_type'] in ('创建/筹建', '投产', '迁建')]
        origin_story = (''.join(
            f"{e['event_date_start'] or ''}，{e['title']}：{e['description']}{cite(e)}。"
            for e in origin)) or None

        dev = [e for e in hist if e not in origin]
        development_story = (''.join(
            f"{e['event_date_start'] or ''}，{e['title']}：{e['description']}{cite(e)}。"
            for e in dev)) or None

        transform = [e for e in hist if e['event_type'] in
                     ('停产', '搬迁', '改制', '军转民', '博物馆/园区再利用',
                      '保护启动', '合并重组', '制度变化')]
        transformation_story = (''.join(
            f"{e['event_date_start'] or ''}，{e['title']}：{e['description']}{cite(e)}。"
            for e in transform)) or None

        recognition_story = (''.join(
            f"{e['event_date_start'] or ''}，{e['title']}。{cite(e)}" for e in recog)) or None

        has_content = bool(hist)
        profiles[hid] = {
            'heritage_id': hid,
            'overview': overview,
            'origin_story': origin_story,
            'development_story': development_story,
            'transformation_story': transformation_story,
            'recognition_story': recognition_story,
            'current_use': current_use.get(hid),
            'period_tags': period_tags.get(hid) or period_tags_for_years(
                [founded[hid]['value']] if hid in founded else []),
            'research_status': ('verified' if has_content else 'insufficient_sources'),
            'generated_from_event_version': data_version,
            'note': None if has_content else '当前数据库尚无足够已核实史料, 档案待补充。',
            'people': [],
        }
        # 人物从事件与采集条目聚合
        people = {}
        for e in hist:
            for p in e.get('related_people', []):
                people.setdefault(p, {'name': p, 'roles': set(), 'source_ids': set()})
                people[p]['roles'].add(e['event_type'])
                people[p]['source_ids'].update(e['source_ids'])
        for k, v in item_people.get(hid, {}).items():
            ent = people.setdefault(k, {'name': k, 'roles': set(), 'source_ids': set()})
            ent['roles'].update(v['roles'])
            ent['source_ids'].update(v['source_ids'])
        profiles[hid]['people'] = [
            {'name': k, 'roles': sorted(v['roles']),
             'source_ids': sorted(v['source_ids'])}
            for k, v in people.items()]

    # ---- 回写主表
    for s in sites:
        hid = s['heritage_id']
        s['founded_year'] = founded.get(hid, {}).get('value')
        s['founded_year_precision'] = founded.get(hid, {}).get('date_precision')
        s['production_start_year'] = production.get(hid, {}).get('value')
        s['closure_year'] = closure.get(hid, {}).get('value')
        s['recognition_years'] = [int(str(batch_date_src.get(b, {}).get(
            'announcement_date', '0'))[:4]) for b in s['batches']
            if str(batch_date_src.get(b, {}).get('announcement_date', ''))[:4].isdigit()]
        s['historical_period'] = profiles[hid]['period_tags']
        s['current_use'] = current_use.get(hid)
        s['enrichment_status'] = ('verified'
                                  if profiles[hid]['research_status'] == 'verified'
                                  else 'not_started')
        s['data_version'] = data_version

    # Reconcile existing source rows instead of append-only merging.  The
    # inventory source registry may gain a more precise note for an existing
    # URL in a later research wave; leaving the old processed row untouched
    # would make the public provenance text lag behind the source of truth.
    existing_by_id = {x['source_id']: x for x in sources}
    for sid, src in web_sources.items():
        if sid in existing_by_id:
            existing_by_id[sid].update(src)
        else:
            sources.append(src)
    json.dump(sites, open(os.path.join(PROCESSED, 'heritage_sites.json'), 'w',
                          encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(events, open(os.path.join(MODEL, 'heritage_events.json'), 'w',
                           encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(relations, open(os.path.join(MODEL, 'heritage_relations.json'), 'w',
                              encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(profiles, open(os.path.join(MODEL, 'heritage_profiles.json'), 'w',
                             encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(sources, open(os.path.join(PROCESSED, 'sources.json'), 'w',
                            encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump({
        'schema': inventory_raw.get('schema', 'hubei-industrial-heritage-inventory-v1'),
        'scope': inventory_raw.get('scope', '湖北省'),
        'purpose': inventory_raw.get('purpose', ''),
        'research_targets': inventory_raw.get('research_targets') or {},
        'records': inventory,
    }, open(os.path.join(PROCESSED, 'hubei_inventory.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)

    print('events:', len(events), '| relations:', len(relations),
          '| web sources:', len(web_sources),
          '| enriched sites:', len(ev_by_site),
          '| hubei inventory:', len(inventory))


if __name__ == '__main__':
    sys.exit(main())
