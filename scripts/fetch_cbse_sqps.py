import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://cbseacademic.nic.in/SQP_CLASSXII_2023-24.html'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=10) as r:
    html = r.read().decode('utf-8', errors='ignore')

targets = [
    'Math', 'Chemistry', 'Accountancy', 'Economics', 'Business', 'AppliedMath'
]
for t in targets:
    matches = re.findall(rf'href=[\'"]([^\'"]*{t}[^\'"]*SQP\.pdf)[\'"]', html, re.I)
    for m in matches:
        print(f"{t}: https://cbseacademic.nic.in/{m.lstrip('/')}")
