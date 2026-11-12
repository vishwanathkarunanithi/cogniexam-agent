"""
Pydantic Schemas for CogniExam Multi-Agent System.
"""

from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class QuestionPaperAnalysisRequest(BaseModel):
    paper_text: str = Field(..., description="Raw text of the examination paper")
    course_title: Optional[str] = Field("Course Assessment", description="Course name or code")


class RubricItem(BaseModel):
    criterion: str
    marks: float


class AnalyzedQuestion(BaseModel):
    q_no: str
    question: str
    marks: float
    bloom_level: str
    bloom_name: str
    action_verb: str
    justification: str
    model_answer: str
    rubric: List[RubricItem]


class QuestionPaperAnalysisResponse(BaseModel):
    exam_title: str
    total_questions: int
    total_marks: float
    bloom_index: float
    verdict: str
    metrics: Dict[str, Any]
    questions: List[AnalyzedQuestion]


class ExamGenerationRequest(BaseModel):
    course_name: str
    syllabus_summary: str
    total_marks: int = 50
    target_distribution: Optional[Dict[str, float]] = None


class StudentEvaluationRequest(BaseModel):
    question_text: str
    bloom_level: str
    maximum_marks: float
    model_answer: str
    rubric: List[RubricItem]
    student_answer: str

