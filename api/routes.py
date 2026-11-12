"""
FastAPI Routes for CogniExam Multi-Agent System.
"""

import os
from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from typing import Optional

from api.schemas import (
    QuestionPaperAnalysisRequest,
    QuestionPaperAnalysisResponse,
    ExamGenerationRequest,
    StudentEvaluationRequest
)
from core.cloud_client import CloudAgentClient
from core.qp_analyzer import QuestionPaperAnalyzer
from core.exam_generator import SmartExamGenerator
from core.assessment_agent import AssessmentAgent
from core.syllabus_parser import SyllabusParser

router = APIRouter(prefix="/api")
cloud_client = CloudAgentClient()
qp_analyzer = QuestionPaperAnalyzer(cloud_client)
exam_generator = SmartExamGenerator(cloud_client)
assessment_agent = AssessmentAgent(cloud_client)
syllabus_parser = SyllabusParser()


@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "cloud_mode": cloud_client.mode,
        "cloud_connected": cloud_client.is_cloud_connected(),
        "model": "gemini-3.5-flash-lite (Google Cloud AI)"
    }


@router.get("/sample-paper")
def get_sample_paper():
    sample_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "sample_question_paper.txt")
    if os.path.exists(sample_path):
        with open(sample_path, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = "1. Define CAP theorem. [5 Marks]\n2. Explain two-phase commit protocol. [5 Marks]"
    return {
        "course_title": "CS8401 - Cloud Computing & Distributed Systems",
        "paper_text": content
    }


@router.post("/analyze-paper", response_model=QuestionPaperAnalysisResponse)
def analyze_question_paper(req: QuestionPaperAnalysisRequest):
    if not req.paper_text or len(req.paper_text.strip()) < 10:
        raise HTTPException(status_code=400, detail="Question paper text is empty or too short.")
    result = qp_analyzer.analyze_paper_and_generate_key(
        paper_text=req.paper_text,
        course_title=req.course_title or "Course Assessment"
    )
    return result


@router.post("/upload-paper")
async def upload_question_paper(file: UploadFile = File(...), course_title: str = Form("Course Assessment")):
    content = await file.read()
    if file.filename.endswith(".pdf"):
        text = syllabus_parser.parse_pdf(content)
    else:
        text = content.decode("utf-8", errors="ignore")
        
    result = qp_analyzer.analyze_paper_and_generate_key(
        paper_text=text,
        course_title=course_title
    )
    return result


@router.post("/generate-exam")
def generate_balanced_exam(req: ExamGenerationRequest):
    exam = exam_generator.generate_exam_paper(
        course_name=req.course_name,
        syllabus_summary=req.syllabus_summary,
        total_marks=req.total_marks,
        target_distribution=req.target_distribution
    )
    return exam


@router.post("/evaluate-submission")
def evaluate_student_submission(req: StudentEvaluationRequest):
    eval_res = assessment_agent.evaluate_submission(
        question_text=req.question_text,
        bloom_level=req.bloom_level,
        maximum_marks=req.maximum_marks,
        model_answer=req.model_answer,
        rubric=[r.model_dump() for r in req.rubric],
        student_answer=req.student_answer
    )
    return eval_res

