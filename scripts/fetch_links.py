import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

# 1. VTU
try:
    req = urllib.request.Request('https://vtu.ac.in/model-question-paper/', headers=headers)
    with urllib.request.urlopen(req, timeout=10) as r:
        html = r.read().decode('utf-8', errors='ignore')
    pdfs = re.findall(r'href=[\'"](https?://vtu\.ac\.in/wp-content/uploads/[^\'"]+\.pdf)[\'"]', html, re.I)
    print("Found VTU PDFs:", len(pdfs))
    for p in pdfs[:8]:
        print("VTU:", p)
except Exception as e:
    print("VTU Error:", e)

# 2. CBSE Academic Class 12
try:
    req2 = urllib.request.Request('https://cbseacademic.nic.in/SQP_CLASSXII_2023_24.html', headers=headers)
    with urllib.request.urlopen(req2, timeout=10) as r:
        html2 = r.read().decode('utf-8', errors='ignore')
    cbse_pdfs = re.findall(r'href=[\'"](web_material/SQP/[^\'"]+\.pdf)[\'"]', html2, re.I)
    print("Found CBSE PDFs:", len(cbse_pdfs))
    for p in cbse_pdfs[:8]:
        print("CBSE: https://cbseacademic.nic.in/" + p)
except Exception as e:
    print("CBSE Error:", e)

