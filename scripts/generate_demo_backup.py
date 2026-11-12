"""
Pre-generates offline demo backup artifacts (JSON + PDF) for 2 sample papers.
"""

import os
import sys
import json

# Ensure project root is in python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.sample_bank import SAMPLE_QUESTION_PAPERS
from core.qp_analyzer import QuestionPaperAnalyzer
from core.cloud_client import CloudAgentClient
from core.pdf_generator import AcademicPDFGenerator

os.makedirs("demo_backup", exist_ok=True)
client = CloudAgentClient()
analyzer = QuestionPaperAnalyzer(client)
pdf_gen = AcademicPDFGenerator()

# 1. Anna University Cloud Computing
p1 = SAMPLE_QUESTION_PAPERS["anna_univ_cloud"]
title1 = f"{p1['course_code']} - {p1['course_title']}"
res1 = analyzer.analyze_paper_and_generate_key(p1["paper_text"], title1)
with open("demo_backup/anna_univ_cloud_result.json", "w", encoding="utf-8") as f:
    json.dump(res1, f, indent=2)
pdf1 = pdf_gen.generate_pdf_bytes(res1)
with open("demo_backup/anna_univ_cloud_model_answer_key.pdf", "wb") as f:
    f.write(pdf1)

# 2. Velammal Autonomous Web Technologies
p2 = SAMPLE_QUESTION_PAPERS["velammal_autonomous_web"]
title2 = f"{p2['course_code']} - {p2['course_title']}"
res2 = analyzer.analyze_paper_and_generate_key(p2["paper_text"], title2)
with open("demo_backup/velammal_web_result.json", "w", encoding="utf-8") as f:
    json.dump(res2, f, indent=2)
pdf2 = pdf_gen.generate_pdf_bytes(res2)
with open("demo_backup/velammal_web_model_answer_key.pdf", "wb") as f:
    f.write(pdf2)

print("SUCCESS: Demo backup artifacts generated in demo_backup/")
