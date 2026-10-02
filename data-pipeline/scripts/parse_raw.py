# -*- coding: utf-8 -*-
"""解析国家工业遗产名单第 1-7 批原始文件 (xls/pdf/docx) 为统一的 interim JSON。

输出: data-pipeline/interim/batch{1..7}.json
  { batch, source_file, source_sha256, layout, row_count, rows: [...] }

解析策略:
- xls/docx: 直接读表格
- pdf: 无可用表格线, 按表头词的 x 坐标聚类得到列边界, 按“序号”列数字锚定行,
  其余词按 x 中心分列、按行区间归属, 支持跨行单元格与竖排(逐字)文本。
"""
import hashlib
import json
import os
import re
import sys

import pdfplumber
import xlrd
from docx import Document

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, '..', 'raw')
INTERIM = os.path.join(HERE, '..', 'interim')

SRC = {
    1: '7799881.xls',
    2: '7799405.pdf',
    3: '7576103.pdf',
    4: '国家工业遗产名单（第四批）.docx',
    5: 'ec7698fcea41463885cd22e31943d9db.pdf',
    6: '907087582fcb435c9f2ab3e828162f61.pdf',
    7: 'e3061bbc941c419c9413f8ac35678a8f.pdf',
}

TITLE_RE = re.compile(r'第[一二三四五六七八九十]+批国家工业遗产名单|^附件')


def clean_text(s):
    """单元格文本规范化: 去换行/多余空白(中文文本安全), 保留内部标点。"""
    if s is None:
        return ''
    s = str(s)
    s = s.replace('\r', '\n')
    s = re.sub(r'\s+', '', s)
    return s.strip()


def sha256_of(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


# ---------------------------------------------------------------- xls (batch 1)

def parse_batch1(path):
    wb = xlrd.open_workbook(path)
    sh = wb.sheet_by_index(0)
    rows = []
    # The original first-batch workbook uses a blank sequence cell for
    # continuation rows (for example 大冶铁厂 and 安源煤矿).  Treating the
    # sequence cell as mandatory silently dropped those official entries.
    # Keep explicit numbers when present and assign the next sequence number
    # to a complete continuation row.
    next_no = 1
    for r in range(sh.nrows):
        vals = [clean_text(sh.cell_value(r, c)) for c in range(sh.ncols)]
        if not any(vals):
            continue
        joined = ''.join(vals)
        if '附件' in joined or '国家工业遗产名单' in joined or vals[0] == '序号':
            continue
        if re.fullmatch(r'\d+(\.0)?', vals[0]):
            no = int(float(vals[0]))
            next_no = no + 1
            rows.append({
                'no': no,
                'name': vals[1],
                'address_raw': vals[2],
                'core_items': vals[3],
            })
        elif vals[1] and vals[2] and vals[3]:
            rows.append({
                'no': next_no,
                'name': vals[1],
                'address_raw': vals[2],
                'core_items': vals[3],
            })
            next_no += 1
    return rows


# --------------------------------------------------------------- docx (batch 4)

def parse_batch4(path):
    doc = Document(path)
    rows = []
    for tbl in doc.tables:
        header = [clean_text(c.text) for c in tbl.rows[0].cells]
        key_of = {}
        for i, h in enumerate(header):
            k = classify_header(h)
            if k:
                key_of[i] = k
        for tr in tbl.rows[1:]:
            cells = [clean_text(c.text) for c in tr.cells]
            if not any(cells):
                continue
            if not re.fullmatch(r'\d+', cells[0]):
                continue
            row = {'no': int(cells[0])}
            for i, k in key_of.items():
                if k != 'no' and i < len(cells):
                    row[k] = cells[i]
            rows.append(row)
    return rows


# ---------------------------------------------------------------- pdf (2,3,5,6,7)

def cluster_header_words(words, y_tol=4):
    """把表头行附近的词按 (行, x 接近度) 聚类成列组。单字残片(如 '序'+'号')与相邻组合并。"""
    lines = []
    for w in sorted(words, key=lambda w: w['top']):
        for ln in lines:
            if abs(ln['top'] - w['top']) <= y_tol:
                ln['words'].append(w)
                break
        else:
            lines.append({'top': w['top'], 'words': [w]})
    groups = []
    for ln in lines:
        ws = sorted(ln['words'], key=lambda w: w['x0'])
        cur = [ws[0]]
        for w in ws[1:]:
            prev = cur[-1]
            single = len(prev['text']) == 1 or len(w['text']) == 1
            if single and w['x0'] - prev['x1'] < 30:
                cur.append(w)
            else:
                groups.append(cur)
                cur = [w]
        groups.append(cur)
    out = []
    for g in groups:
        out.append({
            'text': ''.join(w['text'] for w in g),
            'x0': min(w['x0'] for w in g),
            'x1': max(w['x1'] for w in g),
            'bottom': max(w['bottom'] for w in g),
        })
    return out


HEADER_EXACT = {
    '序号': 'no',
    '地址': 'address',
    '申请名称': 'applied_name',
    '核准名称': 'approved_name',
    '名称': 'name',
    '核心物项': 'core_items',
    '申报单位': 'unit',
    '申请单位': 'unit',
}


def classify_header(text):
    """表头词全串精确匹配, 避免把含“单位”等字样的正文长句误判为表头。"""
    return HEADER_EXACT.get(text.replace(' ', ''), None)


def detect_columns(pdf_path):
    """取所有页的表头组, 投票得到每列的表头 x 区间。返回 {key: (x0, x1)} (按 x 排序)。"""
    votes = {}
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            words = page.extract_words()
            heads = [w for w in words if classify_header(w['text']) or len(w['text']) <= 2]
            heads = [w for w in heads if not TITLE_RE.search(w['text'])]
            for g in cluster_header_words(heads):
                key = classify_header(g['text'])
                if key:
                    votes.setdefault(key, []).append((g['x0'], g['x1']))
    if not votes:
        raise RuntimeError('no header detected in ' + pdf_path)
    cols = {}
    for key, spans in votes.items():
        xs0 = sorted(s[0] for s in spans)
        xs1 = sorted(s[1] for s in spans)
        cols[key] = (xs0[len(xs0) // 2], xs1[len(xs1) // 2])
    return dict(sorted(cols.items(), key=lambda kv: kv[1][0]))


def x_clusters(centers, gap=8.0):
    """把一页正文字符的 x 中心聚成簇(相邻间隔<=gap 视为同簇), 返回 [(x0,x1)] 按 x 排序。"""
    cs = sorted(centers)
    clusters = []
    start = prev = cs[0]
    for c in cs[1:]:
        if c - prev > gap:
            clusters.append((start, prev))
            start = c
        prev = c
    clusters.append((start, prev))
    return clusters


def assign_clusters(clusters, header_cols):
    """把内容 x 簇映射到表头列。
    簇数多于列数: 反复合并间隔最小的相邻簇, 直到簇数=列数, 再按 x 序一一对应;
    簇数少于列数: 退回表头中点边界。返回 {key: (left, right)}。"""
    keys = list(header_cols)
    cl = sorted(clusters)
    if len(cl) > len(keys):
        while len(cl) > len(keys):
            best_i, best_gap = 0, None
            for i in range(len(cl) - 1):
                gap = cl[i + 1][0] - cl[i][1]
                if best_gap is None or gap < best_gap:
                    best_i, best_gap = i, gap
            merged = (cl[best_i][0], cl[best_i + 1][1])
            cl = cl[:best_i] + [merged] + cl[best_i + 2:]
    if len(cl) == len(keys):
        return {k: (c[0] - 0.1, c[1] + 0.1) for k, c in zip(keys, cl)}
    # 少于列数: 用表头区间中点作边界
    bounds = {}
    ordered = keys
    for i, k in enumerate(ordered):
        left = 0.0 if i == 0 else (header_cols[ordered[i - 1]][1] + header_cols[k][0]) / 2
        right = 10000.0 if i == len(ordered) - 1 \
            else (header_cols[k][1] + header_cols[ordered[i + 1]][0]) / 2
        bounds[k] = (left, right)
    return bounds


def group_lines(chars):
    """按垂直 span 重叠聚成视觉行(兼容上下标/中西文混排的字形高度差), 行内按 x 排序。"""
    def yc(c):
        return c['top'] + (c['bottom'] - c['top']) / 2
    lines = []
    for ch in sorted(chars, key=lambda c: (c['top'], c['x0'])):
        h = ch['bottom'] - ch['top']
        placed = False
        for ln in lines:
            ov = min(ln['bottom'], ch['bottom']) - max(ln['top'], ch['top'])
            if ov > 0.45 * max(min(h, ln['bottom'] - ln['top']), 0.5):
                ln['chars'].append(ch)
                ln['top'] = min(ln['top'], ch['top'])
                ln['bottom'] = max(ln['bottom'], ch['bottom'])
                placed = True
                break
        if not placed:
            lines.append({'top': ch['top'], 'bottom': ch['bottom'], 'chars': [ch]})
    for ln in lines:
        ln['chars'].sort(key=lambda c: c['x0'])
    lines.sort(key=lambda l: yc(ln['chars'][0]))
    lines.sort(key=lambda l: min(yc(c) for c in ln['chars']))
    return lines


def get_grid(page, expect_cols):
    """若页面有完整表格线(V>=列数+1 且 H>=2), 返回 (vxs, hys); 否则 None。"""
    vs = sorted({round(l['x0'], 1) for l in page.lines if abs(l['x0'] - l['x1']) < 1})
    hs = sorted({round(l['top'], 1) for l in page.lines if abs(l['top'] - l['bottom']) < 1})
    # 聚类去重(±2pt)
    def dedup(vals):
        out = []
        for v in vals:
            if not out or v - out[-1] > 2:
                out.append(v)
        return out
    vxs, hys = dedup(vs), dedup(hs)
    if len(vxs) >= expect_cols + 1 and len(hys) >= 2:
        return vxs, hys
    return None


def parse_pdf(path):
    """优先用页面表格线做精确网格解析(跨页续行自动并入前一序号行),
    无表格线的页面退回字符聚类解析。字符带 page 标签保证跨页顺序正确。"""
    header_cols = detect_columns(path)
    n_keys = len(header_cols)
    rows_acc = {}   # no -> {key: [char,...]}
    last_no = None
    page_no = 0
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_no += 1
            words = page.extract_words()
            # 标题词与表头词的字符都要剔除(表头可能落在首行数据带内)
            drop_spans = [(w['x0'], w['x1'], w['top'], w['bottom'])
                          for w in words
                          if TITLE_RE.search(w['text']) or classify_header(w['text'])]

            def in_drop(ch):
                return any(x0 - 1 <= ch['x0'] and ch['x1'] <= x1 + 1
                           and top - 1 <= ch['top'] and ch['bottom'] <= bottom + 1
                           for x0, x1, top, bottom in drop_spans)

            chars = []
            for c in page.chars:
                if in_drop(c):
                    continue
                c = dict(c)
                c['page'] = page_no
                chars.append(c)
            if not chars:
                continue
            grid = get_grid(page, n_keys - 1)
            if grid:
                vxs, hys = grid
                keys = list(header_cols)  # 已按 x 排序
                # 列区间: 相邻 V 线之间
                col_ranges = list(zip(vxs, vxs[1:]))
                for yi in range(len(hys) - 1):
                    top, bottom = hys[yi], hys[yi + 1]
                    cells = {i: [] for i in range(len(col_ranges))}
                    for c in chars:
                        yc = c['top'] + (c['bottom'] - c['top']) / 2
                        xc = c['x0'] + (c['x1'] - c['x0']) / 2
                        if not (top <= yc < bottom):
                            continue
                        for i, (l, r) in enumerate(col_ranges):
                            if l <= xc < r:
                                cells[i].append(c)
                                break
                    # 该行带的序号
                    no_txt = ''.join(c['text'] for c in
                                     sorted(cells[0], key=lambda c: c['x0']))
                    m = re.fullmatch(r'\d{1,3}', no_txt.strip())
                    if m:
                        no = int(m.group())
                        last_no = no
                    elif last_no is None:
                        continue  # 表头/标题带
                    target = rows_acc.setdefault(last_no, {k: [] for k in keys})
                    for i, cs in cells.items():
                        key = keys[i] if i < len(keys) else None
                        if key and key != 'no':
                            target[key].extend(cs)
            else:
                # 退回: 字符聚类解析
                content = chars
                heads = [w for w in words if classify_header(w['text'])]
                header_bottom = max((w['bottom'] for w in heads), default=0.0)
                content = [c for c in content if c['top'] > header_bottom - 2]
                if not content:
                    continue
                clusters = x_clusters([c['x0'] + (c['x1'] - c['x0']) / 2 for c in content])
                pbounds = assign_clusters(clusters, header_cols)
                no_col = pbounds['no']
                no_chars = [c for c in content
                            if no_col[0] <= c['x0'] + (c['x1'] - c['x0']) / 2 < no_col[1]
                            and re.fullmatch(r'\d', c['text'])]
                anchors = []
                for ln in group_lines(no_chars):
                    num = ''.join(c['text'] for c in ln['chars'])
                    if re.fullmatch(r'\d{1,3}', num):
                        c = ln['chars'][0]
                        anchors.append({'no': int(num),
                                        'center': (c['top'] + c['bottom']) / 2})
                if not anchors:
                    continue
                anchors.sort(key=lambda a: a['center'])
                spans = []
                for i, a in enumerate(anchors):
                    top = 0.0 if i == 0 else (anchors[i - 1]['center'] + a['center']) / 2
                    bottom = page.height if i == len(anchors) - 1 \
                        else (a['center'] + anchors[i + 1]['center']) / 2
                    spans.append({'no': a['no'], 'top': top, 'bottom': bottom,
                                  'cells': {k: [] for k in pbounds}})
                for c in content:
                    yc = c['top'] + (c['bottom'] - c['top']) / 2
                    xc = c['x0'] + (c['x1'] - c['x0']) / 2
                    for sp in spans:
                        if sp['top'] <= yc < sp['bottom']:
                            for k, (l, r) in pbounds.items():
                                if l <= xc < r:
                                    sp['cells'][k].append(c)
                                    break
                            break
                for sp in spans:
                    last_no = sp['no']
                    row = rows_acc.setdefault(sp['no'], {k: [] for k in pbounds})
                    for k, cs in sp['cells'].items():
                        row[k].extend(cs)
        # 页首续行落在锚点之前的情况由网格分支处理; 聚类分支无法处理跨页续行
    out_rows = []
    for no in sorted(rows_acc):
        row = {'no': no}
        for k, cs in rows_acc[no].items():
            if k == 'no':
                continue
            # 按 (页码 -> 页内行 -> x) 层级拼接, 保证跨页续行顺序正确
            text_parts = []
            for p in sorted({c.get('page', 0) for c in cs}):
                page_chars = [c for c in cs if c.get('page', 0) == p]
                for ln in group_lines(page_chars):
                    text_parts.append(''.join(c['text'] for c in ln['chars']))
            row[k] = clean_text('\n'.join(text_parts))
        out_rows.append(row)
    return out_rows, list(header_cols)


def normalize_row(batch, row, layout):
    out = {
        'no': row['no'],
        'name': row.get('name', ''),
        'address_raw': row.get('address', row.get('address_raw', '')),
        'core_items': row.get('core_items', ''),
    }
    if 'approved_name' in row:
        out['applied_name'] = row.get('applied_name', '')
        out['approved_name'] = row.get('approved_name', '')
        out['name'] = row.get('approved_name', '') or row.get('applied_name', '')
    if 'unit' in row:
        out['applicant_unit'] = row.get('unit', '')
    return out


PROVINCES = [
    '北京', '天津', '上海', '重庆', '河北', '山西', '内蒙古', '辽宁', '吉林',
    '黑龙江', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北',
    '湖南', '广东', '广西', '海南', '四川', '贵州', '云南', '西藏', '陕西',
    '甘肃', '青海', '宁夏', '新疆',
]


def semantic_checks(rows):
    """语义校验: 地址以省级行政区开头; 名称不含地址片段。返回问题列表。"""
    problems = []
    for r in rows:
        addr = r['address_raw']
        if not any(addr.startswith(p) for p in PROVINCES):
            problems.append({'no': r['no'], 'field': 'address_raw',
                             'issue': 'not_starting_with_province', 'value': addr[:30]})
        name = r['name']
        # 以省名开头可能是名称本身(如“山东省邮电管理局旧址”), 仅作提示不作错误
        if any(name.startswith(p) and ('省' in name[:4] or '市' in name[:5])
               for p in PROVINCES):
            problems.append({'no': r['no'], 'field': 'name',
                             'issue': 'info_name_starts_with_province', 'value': name[:30]})
        if len(name) < 3:
            problems.append({'no': r['no'], 'field': 'name',
                             'issue': 'name_too_short', 'value': name})
    return problems


def main():
    summary = []
    for batch, fname in SRC.items():
        path = os.path.join(RAW, fname)
        if fname.endswith('.xls'):
            rows = parse_batch1(path)
            layout = 'xls-4col'
        elif fname.endswith('.docx'):
            rows = parse_batch4(path)
            layout = 'docx-4col'
        else:
            rows, layout_cols = parse_pdf(path)
            layout = 'pdf:' + '+'.join(layout_cols)
        rows = [normalize_row(batch, r, layout) for r in rows]
        # 校验序号连续 1..N
        nos = [r['no'] for r in rows]
        ok_seq = nos == list(range(1, len(nos) + 1))
        # 校验关键字段非空
        empty_name = [r['no'] for r in rows if not r['name']]
        empty_addr = [r['no'] for r in rows if not r['address_raw']]
        empty_core = [r['no'] for r in rows if not r['core_items']]
        problems = semantic_checks(rows)
        out = {
            'batch': batch,
            'source_file': fname,
            'source_sha256': sha256_of(path),
            'layout': layout,
            'row_count': len(rows),
            'sequence_ok': ok_seq,
            'empty_name_nos': empty_name,
            'empty_address_nos': empty_addr,
            'empty_core_items_nos': empty_core,
            'semantic_problems': problems,
            'rows': rows,
        }
        outp = os.path.join(INTERIM, f'batch{batch}.json')
        json.dump(out, open(outp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        summary.append(f"batch{batch}: {len(rows)} rows, seq_ok={ok_seq}, "
                       f"empty={len(empty_name)}/{len(empty_addr)}/{len(empty_core)}, "
                       f"semantic_problems={len(problems)} -> {os.path.basename(outp)}")
        for p in problems:
            summary.append(f"   !! batch{batch} #{p['no']} {p['field']} {p['issue']}: {p['value']}")
    print('\n'.join(summary))


if __name__ == '__main__':
    sys.exit(main())
