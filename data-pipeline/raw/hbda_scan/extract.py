import re
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for page in [1968, 1969]:
    url = f'https://www.hbda.gov.cn/searchitem/207_8?page={page}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req, timeout=12, context=ctx).read().decode('utf-8', errors='replace')
    text = re.sub(r'<[^>]+>', '|', html)
    text = re.sub(r'&nbsp;', ' ', text)
    text = re.sub(r'\|+', '|', text)
    text = re.sub(r'\s+', ' ', text)
    # 提取档号-题名对
    for m in re.finditer(r'(SZ \d+-\s*\d+-\s*\d+)\s*\|\s*([^|]{6,150})\|', text):
        no, title = m.group(1).strip(), m.group(2).strip()
        print(f'p{page} | {no} | {title}')
