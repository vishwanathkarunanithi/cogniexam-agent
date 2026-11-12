"""
Downloads 8-10 real, publicly accessible university examination question papers (PDF)
into test_papers/real/ and writes SOURCES.md.
"""

import os
import sys
import urllib.request
import urllib.error

# Ensure output directory exists
OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "test_papers", "real")
os.makedirs(OUT_DIR, exist_ok=True)

# List of target openly accessible educational question paper URLs
PAPERS_TO_FETCH = [
    {
        "filename": "01_cbse_cs_class12_2024.pdf",
        "url": "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2023_24/ComputerScience-SQP.pdf",
        "university": "CBSE (Central Board of Secondary Education)",
        "subject": "Computer Science (Code 083)",
        "max_marks": 70,
        "category": "Non-Engineering / School Board"
    },
    {
        "filename": "02_cbse_mathematics_class12_2024.pdf",
        "url": "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2023_24/Mathematics-SQP.pdf",
        "university": "CBSE (Central Board of Secondary Education)",
        "subject": "Mathematics (Code 041)",
        "max_marks": 80,
        "category": "Numericals / Derivations"
    },
    {
        "filename": "03_cbse_physics_class12_2024.pdf",
        "url": "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2023_24/Physics-SQP.pdf",
        "university": "CBSE (Central Board of Secondary Education)",
        "subject": "Physics (Code 042)",
        "max_marks": 70,
        "category": "Numericals / Physics"
    },
    {
        "filename": "04_gate_cse_2024.pdf",
        "url": "https://gate2024.iisc.ac.in/wp-content/uploads/2024/02/CS1_2024.pdf",
        "university": "IISc Bangalore / GATE (National Engineering)",
        "subject": "Computer Science & Information Technology",
        "max_marks": 100,
        "category": "Engineering / National Exam"
    },
    {
        "filename": "05_gate_ece_2024.pdf",
        "url": "https://gate2024.iisc.ac.in/wp-content/uploads/2024/02/EC_2024.pdf",
        "university": "IISc Bangalore / GATE (National Engineering)",
        "subject": "Electronics and Communication Engineering",
        "max_marks": 100,
        "category": "Engineering / Circuits & Signals"
    }
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

results = []

for item in PAPERS_TO_FETCH:
    dest_path = os.path.join(OUT_DIR, item["filename"])
    print(f"Fetching: {item['filename']} from {item['url']}...")
    try:
        req = urllib.request.Request(item["url"], headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read()
            if len(content) > 1000 and content.startswith(b"%PDF"):
                with open(dest_path, "wb") as f:
                    f.write(content)
                item["status"] = "DOWNLOADED"
                item["size_bytes"] = len(content)
                print(f"  -> SUCCESS: {len(content)} bytes")
            else:
                item["status"] = f"FAILED: Not a valid PDF (got {len(content)} bytes)"
                print(f"  -> FAILED: content size {len(content)}")
    except Exception as e:
        item["status"] = f"FAILED: {e}"
        print(f"  -> ERROR: {e}")
    results.append(item)

print("\nSummary of initial downloads completed.")

