"""
Downloads 9 real, publicly accessible examination question papers across:
- Engineering: VTU (CSE/ECE/Mechanical)
- Science / Numericals: CBSE (Physics, Chemistry, Mathematics)
- Non-Engineering / Commerce: CBSE (Accountancy, Computer Science)
And creates 1 image-only (scanned) PDF to test the 422 error path.
Writes test_papers/real/SOURCES.md.
"""

import os
import urllib.request
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PIL import Image, ImageDraw

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "test_papers", "real")
os.makedirs(OUT_DIR, exist_ok=True)

TARGETS = [
    {
        "filename": "01_vtu_btech_maths_cse_2023.pdf",
        "url": "https://vtu.ac.in/pdf/QP/1BMATS101.pdf",
        "university": "Visvesvaraya Technological University (VTU)",
        "subject": "Mathematics for CSE Stream (1BMATS101)",
        "max_marks": 100,
        "category": "Engineering / Numericals & Linear Algebra"
    },
    {
        "filename": "02_vtu_btech_calculus_2023.pdf",
        "url": "https://vtu.ac.in/pdf/QP/1BMATC101.pdf",
        "university": "Visvesvaraya Technological University (VTU)",
        "subject": "Calculus and Linear Algebra (1BMATC101)",
        "max_marks": 100,
        "category": "Engineering / Calculus & Derivations"
    },
    {
        "filename": "03_vtu_btech_electronics_ece_2023.pdf",
        "url": "https://vtu.ac.in/pdf/QP/BETCK105Cset1.pdf",
        "university": "Visvesvaraya Technological University (VTU)",
        "subject": "Basics of Electronics & Communication (BETCK105C)",
        "max_marks": 100,
        "category": "Engineering / Circuits & Electronics"
    },
    {
        "filename": "04_vtu_btech_mechanical_maths_2023.pdf",
        "url": "https://vtu.ac.in/pdf/QP/BMATM101set1.pdf",
        "university": "Visvesvaraya Technological University (VTU)",
        "subject": "Applied Mathematics for Mechanical Engineering (BMATM101)",
        "max_marks": 100,
        "category": "Engineering / Mechanical & Numericals"
    },
    {
        "filename": "05_vtu_btech_analog_circuits_2024.pdf",
        "url": "https://vtu.ac.in/wp-content/uploads/2024/03/BVL302-AEC-MODEL-QUESTION-PAPER.pdf",
        "university": "Visvesvaraya Technological University (VTU)",
        "subject": "Analog Electronic Circuits (BVL302)",
        "max_marks": 100,
        "category": "Engineering / Electronics & Hardware"
    },
    {
        "filename": "06_cbse_computer_science_2024.pdf",
        "url": "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2023_24/ComputerScience-SQP.pdf",
        "university": "Central Board of Secondary Education (CBSE)",
        "subject": "Computer Science (Code 083)",
        "max_marks": 70,
        "category": "Non-Engineering / Computing & Python"
    },
    {
        "filename": "07_cbse_physics_2024.pdf",
        "url": "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2023_24/Physics-SQP.pdf",
        "university": "Central Board of Secondary Education (CBSE)",
        "subject": "Physics (Code 042)",
        "max_marks": 70,
        "category": "Science / Electrodynamics & Numericals"
    },
    {
        "filename": "08_cbse_mathematics_2024.pdf",
        "url": "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2023_24/Maths-SQP.pdf",
        "university": "Central Board of Secondary Education (CBSE)",
        "subject": "Mathematics (Code 041)",
        "max_marks": 80,
        "category": "Science / Calculus & Algebra"
    },
    {
        "filename": "09_cbse_accountancy_commerce_2024.pdf",
        "url": "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2023_24/Accountancy-SQP.pdf",
        "university": "Central Board of Secondary Education (CBSE)",
        "subject": "Accountancy (Code 055)",
        "max_marks": 80,
        "category": "Non-Engineering / Commerce & Accounting"
    }
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

downloaded_list = []

print("=== STARTING OFFICIAL QUESTION PAPER DOWNLOADS ===")
for item in TARGETS:
    dest = os.path.join(OUT_DIR, item["filename"])
    print(f"\nDownloading: {item['filename']} ...")
    try:
        req = urllib.request.Request(item["url"], headers=headers)
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read()
            if len(data) > 1000 and data.startswith(b"%PDF"):
                with open(dest, "wb") as f:
                    f.write(data)
                item["status"] = "DOWNLOADED"
                item["size_bytes"] = len(data)
                print(f"  -> SUCCESS: {len(data):,} bytes")
            else:
                item["status"] = f"INVALID_PDF (size {len(data)})"
                print(f"  -> FAILED: Invalid PDF header or small size ({len(data)} bytes)")
    except Exception as e:
        item["status"] = f"ERROR: {e}"
        print(f"  -> ERROR: {e}")
    downloaded_list.append(item)

# 10. Generate 1 purely scanned/image-only PDF to test 422 error path
scanned_filename = "10_scanned_image_only_exam_paper.pdf"
scanned_path = os.path.join(OUT_DIR, scanned_filename)
print(f"\nGenerating purely scanned/image-only PDF: {scanned_filename} ...")

# Create a temporary raster image simulating a scanned document with hand-drawn lines
img_path = os.path.join(OUT_DIR, "_temp_scan.png")
img = Image.new("RGB", (1200, 1600), color=(245, 243, 235))
d = ImageDraw.Draw(img)
# Draw lines simulating scanned handwriting / grid marks
for y in range(100, 1500, 80):
    d.line([(80, y), (1120, y)], fill=(200, 195, 185), width=2)
d.rectangle([(100, 120), (1100, 250)], outline=(100, 95, 85), width=3)
img.save(img_path)

# Embed image into a PDF with zero extractable text streams
c = canvas.Canvas(scanned_path, pagesize=A4)
c.drawImage(img_path, 0, 0, width=595.27, height=841.89)
c.showPage()
c.save()
os.remove(img_path)

scanned_size = os.path.getsize(scanned_path)
print(f"  -> SUCCESS: {scanned_size:,} bytes (Image-only canvas, 0 text streams)")

downloaded_list.append({
    "filename": scanned_filename,
    "url": "Local synthetic raster canvas (Zero text streams)",
    "university": "Simulated Physical Examination Script",
    "subject": "Handwritten Physical Assessment Paper",
    "max_marks": 50,
    "category": "Scanned / Image-Only PDF (422 Diagnostic Test)",
    "status": "GENERATED_FOR_422_TEST",
    "size_bytes": scanned_size
})

# Write test_papers/real/SOURCES.md
sources_md_path = os.path.join(OUT_DIR, "SOURCES.md")
with open(sources_md_path, "w", encoding="utf-8") as f:
    f.write("# Real Question Papers Benchmark Sources\n\n")
    f.write("Publicly accessible past question papers collected for CogniExam robustness testing.\n")
    f.write("Local testing only: git-ignored, excluded from Docker images, and unbundled.\n\n")
    f.write("| # | File Name | University / Board | Subject | Stated Max Marks | Category | Size (Bytes) | Source URL |\n")
    f.write("| :--- | :--- | :--- | :--- | :---: | :--- | :---: | :--- |\n")
    for idx, d in enumerate(downloaded_list, 1):
        f.write(f"| {idx} | `{d['filename']}` | {d['university']} | {d['subject']} | {d['max_marks']} | {d['category']} | {d.get('size_bytes', 0):,} | {d['url']} |\n")

print(f"\nSOURCES.md successfully generated at: {sources_md_path}")

