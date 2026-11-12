import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://www.brainkart.com/subject/Database-Management-Systems---CS8492_380/'
try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as r:
        html = r.read().decode('utf-8', errors='ignore')
    links = re.findall(r'href=[\'"]([^\'"]+question[^\'"]*)[\'"]', html, re.I)
    print("Found links:", len(links))
    for l in links[:5]:
        print("BrainKart:", l)
except Exception as e:
    print("BrainKart Error:", e)

