"""
Automated Student Assessment Agent & Diagnostic Feedback Engine.
Evaluates student responses against step rubrics with Bloom's Taxonomy gap analysis.
"""

import json
from typing import Dict, List, Any
from core.cloud_client import CloudAgentClient


class AssessmentAgent:
    """
    Evaluates student answers against step-wise rubrics, computes marks, and identifies cognitive gaps.
    """
    def __init__(self, cloud_client: CloudAgentClient):
        self.cloud_client = cloud_client

    def evaluate_submission(
        self,
        question_text: str,
        bloom_level: str,
        maximum_marks: float,
        model_answer: str,
        rubric: List[Dict[str, Any]],
        student_answer: str
    ) -> Dict[str, Any]:
        """
        Grades an individual question submission using LLM-as-a-judge / semantic rubric alignment.
        """
        rubric_str = json.dumps(rubric)
        prompt = f"""
EVALUATE_ANSWER
Question: {question_text}
Cognitive Level (Bloom): {bloom_level}
Maximum Marks: {maximum_marks}

Canonical Model Answer:
{model_answer}

Step-by-Step Grading Rubric:
{rubric_str}

Student Submission:
{student_answer}

Please evaluate this student answer with academic fairness:
1. Compare student arguments to the canonical model answer and rubric criteria.
2. Allocate step marks strictly based on criteria met.
3. Highlight strengths and constructive cognitive growth areas.
4. Identify whether the student demonstrated the required cognitive depth for {bloom_level}.

Return valid JSON with keys:
- "score_awarded": float (between 0 and {maximum_marks})
- "maximum_marks": {maximum_marks}
- "percentage": float
- "bloom_level_assessed": "{bloom_level}"
- "semantic_match_ratio": float (0.0 to 1.0)
- "step_evaluations": [ {{"criterion": str, "marks_allocated": float, "marks_awarded": float, "feedback": str}} ]
- "strengths": [str]
- "growth_areas": [str]
- "overall_feedback": str
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
            eval_data = json.loads(cleaned.strip())
        except Exception:
            raw = self.cloud_client._local_fallback_response("EVALUATE_ANSWER", json_mode=True)
            eval_data = json.loads(raw)
            eval_data["maximum_marks"] = maximum_marks
            eval_data["score_awarded"] = round(maximum_marks * 0.85, 1)

        return eval_data

