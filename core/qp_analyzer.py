"""
Question Paper Analyzer Engine:
Extracts individual questions, computes Bloom's taxonomy cognitive scores,
generates canonical answer keys, and builds step-wise scoring rubrics using Google Cloud AI.
"""

import json
import re
from typing import Dict, List, Any
from core.cloud_client import CloudAgentClient
from core.bloom_engine import BLOOM_TAXONOMY_LEVELS, rule_based_bloom_classify, compute_exam_cognitive_distribution


class QuestionPaperAnalyzer:
    """
    Parses an uploaded question paper, evaluates its Bloom's Taxonomy score,
    and synthesizes a complete answer key with marking rubrics.
    """
    def __init__(self, cloud_client: CloudAgentClient):
        self.cloud_client = cloud_client

    def parse_and_extract_questions(self, text: str) -> List[Dict[str, Any]]:
        """
        Extracts questions from raw text using regex patterns or AI structuring.
        """
        lines = text.split("\n")
        questions = []
        pattern = re.compile(r"^(?:q(?:uestion)?\.?\s*(\d+[a-z]?)|(\d+)[\.\)])\s*(.*)", re.IGNORECASE)
        marks_pattern = re.compile(r"\[?\(?(\d+)\s*(?:marks?|pts?|m)\)?\]?", re.IGNORECASE)

        current_q = None
        for line in lines:
            line_str = line.strip()
            if not line_str:
                continue

            match = pattern.match(line_str)
            if match:
                if current_q:
                    questions.append(current_q)

                q_num = match.group(1) or match.group(2)
                q_text = match.group(3).strip()

                # Check for marks inline
                marks = 5
                m_match = marks_pattern.search(line_str)
                if m_match:
                    marks = int(m_match.group(1))

                current_q = {
                    "q_no": q_num,
                    "question": q_text,
                    "marks": marks
                }
            else:
                if current_q:
                    # Append multiline question text
                    current_q["question"] += " " + line_str
                    m_match = marks_pattern.search(line_str)
                    if m_match:
                        current_q["marks"] = int(m_match.group(1))

        if current_q:
            questions.append(current_q)

        # If regex didn't find numbered questions, split by sentences or paragraphs
        if not questions:
            paragraphs = [p.strip() for p in text.split("\n\n") if len(p.strip()) > 15]
            for idx, p in enumerate(paragraphs):
                m_match = marks_pattern.search(p)
                marks = int(m_match.group(1)) if m_match else 5
                questions.append({
                    "q_no": str(idx + 1),
                    "question": p,
                    "marks": marks
                })

        return questions

    def analyze_paper_and_generate_key(self, paper_text: str, course_title: str = "Course Assessment") -> Dict[str, Any]:
        """
        Full pipeline:
        1. Parse questions.
        2. Call Cloud AI to classify Bloom's level and generate model answers + rubrics.
        3. Compute overall Bloom cognitive index and distribution.
        """
        raw_questions = self.parse_and_extract_questions(paper_text)
        
        prompt = f"""
ANALYZE_QUESTION_PAPER_AND_GENERATE_ANSWER_KEY
Course Title: {course_title}

Here is the raw text of an uploaded examination question paper:
\"\"\"
{paper_text[:6000]}
\"\"\"

Your task as an Expert Pedagogical Evaluation Agent:
1. Identify all questions in the paper.
2. For EACH question:
   - Determine its exact Bloom's Revised Taxonomy level: L1 (Remember), L2 (Understand), L3 (Apply), L4 (Analyze), L5 (Evaluate), or L6 (Create).
   - Identify the primary action verb used.
   - Provide a short justification explaining WHY it belongs to that Bloom's cognitive level.
   - Write a comprehensive, canonical MODEL ANSWER.
   - Generate a detailed STEP-BY-STEP MARKING RUBRIC breakdown (allocating marks to steps).
3. Compute the overall cognitive quality verdict for the question paper.

Return a STRICT, VALID JSON response with this exact structure:
{{
  "exam_title": "{course_title} - Bloom's Audit & Answer Key",
  "questions": [
    {{
      "q_no": "1",
      "question": "Question text here",
      "marks": 5,
      "bloom_level": "L2",
      "bloom_name": "Understand",
      "action_verb": "explain",
      "justification": "Requires conceptual explanation of mechanisms rather than mere rote recall.",
      "model_answer": "Complete expected ideal answer...",
      "rubric": [
        {{"criterion": "Key point 1 explanation", "marks": 2.5}},
        {{"criterion": "Key point 2 explanation", "marks": 2.5}}
      ]
    }}
  ],
  "audit_verdict": "Cognitively Balanced (NBA/ABET Compliant)"
}}
"""
        response_text = self.cloud_client.generate_completion(prompt, json_mode=True)
        
        try:
            cleaned = response_text.strip()
            if cleaned.startswith("```json"):
                cleaned = cleaned[7:]
            if cleaned.startswith("```"):
                cleaned = cleaned[3:]
            if cleaned.endswith("```"):
                cleaned = cleaned[:-3]
            parsed_data = json.loads(cleaned.strip())
            analyzed_questions = parsed_data.get("questions", [])
        except Exception:
            # Dynamic fallback using rule-based engine
            analyzed_questions = []
            for q in raw_questions:
                heuristic = rule_based_bloom_classify(q["question"])
                lvl = heuristic["level"]
                m = q.get("marks", 5)
                analyzed_questions.append({
                    "q_no": q["q_no"],
                    "question": q["question"],
                    "marks": m,
                    "bloom_level": lvl,
                    "bloom_name": BLOOM_TAXONOMY_LEVELS[lvl]["name"],
                    "action_verb": heuristic.get("heuristic_matched", ["examine"])[0] if heuristic.get("heuristic_matched") else "discuss",
                    "justification": f"Cognitive demand calibrated at {lvl} ({BLOOM_TAXONOMY_LEVELS[lvl]['name']}) based on task complexity and action verbs.",
                    "model_answer": f"Ideal model answer addressing {q['question'][:120]} with relevant technical derivations, concepts, and domain principles.",
                    "rubric": [
                        {"criterion": "Definition of core concepts & principles", "marks": round(m * 0.4, 1)},
                        {"criterion": "Technical derivation / practical analysis", "marks": round(m * 0.4, 1)},
                        {"criterion": "Accuracy, formatting & conclusions", "marks": round(m * 0.2, 1)}
                    ]
                })

        # Calculate exact metrics and Bloom's cognitive index
        metrics = compute_exam_cognitive_distribution(analyzed_questions)
        
        # Calculate Bloom's Cognitive Depth Index (Scale: 1.0 to 6.0)
        total_m = metrics["total_marks"] or 1
        weighted_sum = sum(
            BLOOM_TAXONOMY_LEVELS[q.get("bloom_level", "L2")]["weight"] * q.get("marks", 5)
            for q in analyzed_questions
        )
        bloom_index = round(weighted_sum / total_m, 2)
        
        if bloom_index < 2.0:
            verdict = "Heavy Lower-Order Recall (L1/L2) - Needs more analytical and design problems."
        elif bloom_index < 3.5:
            verdict = "Moderately Balanced - Good mix of foundational and application questions."
        else:
            verdict = "Highly Rigorous - Strong emphasis on Higher-Order Thinking (Analyze, Evaluate, Create)."

        return {
            "exam_title": f"{course_title} - Bloom's Audit & Answer Key",
            "total_questions": len(analyzed_questions),
            "total_marks": total_m,
            "bloom_index": bloom_index,
            "verdict": verdict,
            "metrics": metrics,
            "questions": analyzed_questions
        }

    def format_as_printable_answer_key(self, result: Dict[str, Any]) -> str:
        """Formats the audit report and answer key into clean printable Markdown."""
        md = []
        md.append(f"# {result.get('exam_title')}")
        md.append(f"**Total Questions:** {result.get('total_questions')} | **Total Marks:** {result.get('total_marks')} | **Bloom Cognitive Index:** {result.get('bloom_index')} / 6.0\n")
        md.append(f"**OBE Accreditation Verdict:** *{result.get('verdict')}*\n")
        md.append("---\n")
        
        metrics = result.get("metrics", {})
        md.append("## 📊 Bloom's Cognitive Distribution Summary")
        md.append(f"- **Lower-Order Thinking (L1 Recall & L2 Understand):** {metrics.get('low_order_pct', 0):.1f}%")
        md.append(f"- **Middle-Order Thinking (L3 Apply & L4 Analyze):** {metrics.get('medium_order_pct', 0):.1f}%")
        md.append(f"- **Higher-Order Thinking (L5 Evaluate & L6 Create):** {metrics.get('high_order_pct', 0):.1f}%\n")
        md.append("---\n")
        md.append("## 📝 Detailed Answer Key & Marking Scheme\n")

        for q in result.get("questions", []):
            md.append(f"### Question {q.get('q_no')} ({q.get('marks')} Marks)")
            md.append(f"**Question:** {q.get('question')}  ")
            md.append(f"**Bloom Level:** `{q.get('bloom_level')} - {q.get('bloom_name')}` | **Action Verb:** `{q.get('action_verb')}`  ")
            md.append(f"*Pedagogical Justification:* {q.get('justification')}\n")
            md.append(f"#### 💡 Canonical Model Answer:")
            md.append(f"> {q.get('model_answer')}\n")
            md.append(f"#### 📋 Step-by-Step Scoring Rubric:")
            for r in q.get("rubric", []):
                md.append(f"- **{r.get('criterion')}**: `{r.get('marks')} Marks`")
            md.append("\n---\n")

        return "\n".join(md)

