import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://vtu.ac.in/model-question-paper/'
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, timeout=10) as r:
    html = r.read().decode('utf-8', errors='ignore')

# Find all links on the page
links = re.findall(r'href=[\'"]([^\'"]+)[\'"]', html)
for l in links:
    if any(k in l.lower() for k in ['b.e', 'btech', 'question', 'scheme', 'bmat', 'bcse', '2022', '2021', 'cse']):
        print(l)

