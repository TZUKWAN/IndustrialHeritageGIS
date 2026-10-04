import re
import sys
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
KW = ['安陆', '公安县', '宜都', '化肥', '冷冻', '矿山机械', '粮']

def scan(page):
    url = f'https://www.hbda.gov.cn/searchitem/207_8?page={page}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req, timeout=12, context=ctx).read().decode('utf-8', errors='replace')
    except Exception as e:
        print(f'p{page}: ERR {e}')
        return
    text = re.sub(r'<[^>]+>', '|', html)
    text = re.sub(r'\|+', '|', text)
    text = re.sub(r'\s+', ' ', text)
    for kw in KW:
        for m in re.finditer(kw, text):
            i = m.start()
            seg = text[max(0, i-120):i+150]
            print(f'p{page} [{kw}]: ...{seg}...')

for pg in [int(x) for x in sys.argv[1:]]:
    scan(pg)
