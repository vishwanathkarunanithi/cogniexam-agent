import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://mu.ac.in/distance-open-learning/question-papers-of-various-courses-semester-pattern'
try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as r:
        html = r.read().decode('utf-8', errors='ignore')
    pdfs = re.findall(r'href=[\'"]([^\'"]+\.pdf)[\'"]', html, re.I)
    print("Found Mumbai Univ PDFs:", len(pdfs))
    for p in pdfs[:8]:
        print("MU:", p)
except Exception as e:
    print("MU Error:", e)

