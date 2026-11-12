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


class AgentTraceStep(BaseModel):
    step: str
    status: str
    retries: int = 0
    engine_used: str
    details: Optional[str] = None


class NumericalVerification(BaseModel):
    is_numerical: bool = False
    formula_detected: Optional[str] = None
    computed_value: Optional[str] = None
    matches_canonical: bool = True
    note: Optional[str] = None


class DesignSuggestion(BaseModel):
    level: str
    status: str  # under_represented | over_represented | balanced
    actual_pct: float
    target_pct: float
    difference_pct: float
    recommended_stems: List[str]


class SmartDesignAudit(BaseModel):
    target_distribution: Dict[str, float]
    actual_distribution: Dict[str, float]
    compliance_status: str
    rebalance_suggestions: List[DesignSuggestion]


class AnalyzedQuestion(BaseModel):
    q_no: str
    section: Optional[str] = "PART A"
    question: str
    marks: float
    bloom_level: str
    bloom_name: str
    action_verb: str
    justification: str
    model_answer: str
    rubric: List[RubricItem]
    own_words_criteria: Optional[List[str]] = None
    numerical_verification: Optional[NumericalVerification] = None
    engine_used: str = "gemini-3.5-flash"
    faculty_verified: str = "Faculty verified: No"


class QuestionPaperAnalysisResponse(BaseModel):
    institution_header: Optional[str] = "OFFICIAL MODEL ANSWER KEY"
    institution_name: Optional[str] = None
    department: Optional[str] = None
    course_title: str
    exam_title: str
    disclaimer: Optional[str] = None
    total_questions: int
    total_marks: float
    bloom_index: float
    verdict: str
    metrics: Dict[str, Any]
    questions: List[AnalyzedQuestion]
    design_audit: Optional[SmartDesignAudit] = None
    agent_trace: List[AgentTraceStep] = []
    faculty_verified: str = "Faculty verified: No"


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
