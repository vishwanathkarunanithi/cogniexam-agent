import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
urls_to_try = [
    'https://stannescet.ac.in/department/cse/anna-university-question-papers/',
    'https://stannescet.ac.in/department/ece/anna-university-question-papers/',
    'https://stannescet.ac.in/department/mechanical-engineering/anna-university-question-papers/'
]
for u in urls_to_try:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
        pdfs = re.findall(r'href=[\'"]([^\'"]+\.pdf)[\'"]', html, re.I)
        print(f"{u}: {len(pdfs)} PDFs found")
        for p in pdfs[:5]:
            print("  PDF:", p)
    except Exception as e:
        print(u, e)

