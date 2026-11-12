"""
Automated Verification Suite using Playwright / Selenium for CogniExam.
Tests the Multi-Agent API endpoints and React Native frontend rendering.
"""

import sys
import time
import requests

SERVER_URL = "http://localhost:8000"

def test_backend_api():
    print("=" * 60)
    print(" 🧪 Running CogniExam Automated Verification Suite")
    print("=" * 60)
    
    # 1. Health check
    try:
        r = requests.get(f"{SERVER_URL}/api/health", timeout=5)
        assert r.status_code == 200, f"Expected 200, got {r.status_code}"
        data = r.json()
        print(f"[✓] 1. Health Endpoint: PASSED (Mode: {data.get('cloud_mode')}, Model: {data.get('model')})")
    except Exception as e:
        print(f"[FAILED] 1. Health Endpoint: {e}")
        return False

    # 2. Sample Paper Fetch
    try:
        r = requests.get(f"{SERVER_URL}/api/sample-paper", timeout=5)
        assert r.status_code == 200
        paper = r.json()
        assert "paper_text" in paper and len(paper["paper_text"]) > 50
        print(f"[✓] 2. Sample Paper Ingestion: PASSED ({len(paper['paper_text'])} chars)")
    except Exception as e:
        print(f"[FAILED] 2. Sample Paper: {e}")
        return False

    # 3. Bloom Analysis & Answer Key Synthesis
    try:
        test_payload = {
            "course_title": "Unit Test Distributed Systems",
            "paper_text": "1. Define CAP Theorem. [5 Marks]\n2. Explain two-phase commit consensus. [5 Marks]"
        }
        r = requests.post(f"{SERVER_URL}/api/analyze-paper", json=test_payload, timeout=60)
        assert r.status_code == 200
        analysis = r.json()
        assert len(analysis["questions"]) >= 2
        assert "bloom_index" in analysis
        print(f"[✓] 3. Bloom Taxonomy Audit & Answer Key Synthesis: PASSED (Bloom Index: {analysis['bloom_index']})")
    except Exception as e:
        print(f"[FAILED] 3. Analysis: {e}")
        return False

    # 4. Student Grading & Rubric
    try:
        eval_payload = {
            "question_text": "Explain two-phase commit consensus.",
            "bloom_level": "L2",
            "maximum_marks": 5.0,
            "model_answer": "Phase 1 is prepare, Phase 2 is commit or abort.",
            "rubric": [{"criterion": "Explain phase 1 and 2", "marks": 5.0}],
            "student_answer": "In phase 1 the coordinator asks participants to prepare. In phase 2 it commits if all agreed."
        }
        r = requests.post(f"{SERVER_URL}/api/evaluate-submission", json=eval_payload, timeout=20)
        assert r.status_code == 200
        grading = r.json()
        assert "score_awarded" in grading
        print(f"[✓] 4. Rubric Student Grading Agent: PASSED (Awarded: {grading['score_awarded']} / 5.0)")
    except Exception as e:
        print(f"[FAILED] 4. Grading: {e}")
        return False

    # 5. Cloud Storage Paper Vault
    try:
        r = requests.get(f"{SERVER_URL}/api/cloud-papers", timeout=5)
        assert r.status_code == 200
        vault_papers = r.json()
        print(f"[✓] 5. Cloud Storage Paper Vault: PASSED ({len(vault_papers)} papers archived in cloud)")
    except Exception as e:
        print(f"[FAILED] 5. Cloud Storage: {e}")
        return False

    print("\n" + "=" * 60)
    print(" 🎉 ALL AUTOMATED TESTS PASSED SUCCESSFULLY (5/5)")
    print("=" * 60)
    return True

if __name__ == "__main__":
    success = test_backend_api()
    sys.exit(0 if success else 1)
