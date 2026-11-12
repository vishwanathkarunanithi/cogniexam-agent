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
from core.cloud_storage import CloudPaperVault
from core.sample_bank import SAMPLE_QUESTION_PAPERS
from core.pdf_generator import AcademicPDFGenerator
from fastapi.responses import Response

router = APIRouter(prefix="/api")
cloud_client = CloudAgentClient()
qp_analyzer = QuestionPaperAnalyzer(cloud_client)
exam_generator = SmartExamGenerator(cloud_client)
assessment_agent = AssessmentAgent(cloud_client)
syllabus_parser = SyllabusParser()
cloud_vault = CloudPaperVault()
pdf_generator = AcademicPDFGenerator()


@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "cloud_mode": cloud_client.mode,
        "cloud_connected": cloud_client.is_cloud_connected(),
        "model": "gemini-3.5-flash-lite (Google Cloud AI)"
    }


@router.get("/sample-papers")
def list_sample_papers():
    """Returns list of 10 pre-loaded university examination question papers."""
    return [
        {
            "key": k,
            "id": v["id"],
            "institution": v["institution"],
            "course_code": v["course_code"],
            "course_title": v["course_title"],
            "display_name": f"{v['course_code']} - {v['course_title']} ({v['institution']})"
        }
        for k, v in SAMPLE_QUESTION_PAPERS.items()
    ]


@router.get("/sample-papers/{paper_key}")
def get_sample_paper_by_key(paper_key: str):
    """Retrieves full question paper text for a specific university sample."""
    if paper_key not in SAMPLE_QUESTION_PAPERS:
        raise HTTPException(status_code=404, detail="Sample paper not found.")
    data = SAMPLE_QUESTION_PAPERS[paper_key]
    return {
        "course_title": f"{data['course_code']} - {data['course_title']}",
        "paper_text": data["paper_text"],
        "metadata": data
    }


@router.get("/sample-paper")
def get_default_sample_paper():
    """Default fallback sample paper (Velammal Cloud Computing)."""
    data = SAMPLE_QUESTION_PAPERS.get("velammal_cloud")
    return {
        "course_title": f"{data['course_code']} - {data['course_title']}",
        "paper_text": data["paper_text"]
    }


@router.post("/analyze-paper", response_model=QuestionPaperAnalysisResponse)
def analyze_question_paper(req: QuestionPaperAnalysisRequest):
    if not req.paper_text or len(req.paper_text.strip()) < 10:
        raise HTTPException(status_code=400, detail="Question paper text is empty or too short.")
    result = qp_analyzer.analyze_paper_and_generate_key(
        paper_text=req.paper_text,
        course_title=req.course_title or "Course Assessment"
    )
    # Automatically archive to cloud paper vault
    try:
        cloud_vault.save_paper_to_cloud(
            course_title=req.course_title or "Course Assessment",
            paper_text=req.paper_text,
            analysis_result=result
        )
    except Exception as e:
        print(f"[Notice] Cloud vault save note: {e}")

    return result


@router.post("/upload-paper")
async def upload_question_paper(file: UploadFile = File(...), course_title: str = Form("Course Assessment")):
    content = await file.read()
    if not content:
        raise HTTPException(status_code=400, detail="Uploaded file is empty (0 bytes).")

    if file.filename.lower().endswith(".pdf"):
        text = syllabus_parser.parse_pdf(content)
        if not text or len(text.strip()) < 20:
            raise HTTPException(
                status_code=422,
                detail="Unable to extract text from PDF. The document appears to be scanned, image-only, or encrypted. Please provide a searchable text PDF or paste the question paper transcript directly."
            )
    else:
        text = content.decode("utf-8", errors="ignore")
        if not text or len(text.strip()) < 10:
            raise HTTPException(status_code=400, detail="Text file contains insufficient content.")

    result = qp_analyzer.analyze_paper_and_generate_key(
        paper_text=text,
        course_title=course_title
    )
    # Automatically archive to cloud paper vault
    try:
        cloud_vault.save_paper_to_cloud(
            course_title=course_title,
            paper_text=text,
            analysis_result=result
        )
    except Exception as e:
        print(f"[Notice] Cloud vault save note: {e}")

    return result


@router.post("/download-answer-key-pdf")
def download_answer_key_pdf(payload: dict):
    """Generates a formal, publication-grade academic PDF answer key."""
    try:
        pdf_bytes = pdf_generator.generate_pdf_bytes(payload)
        safe_name = payload.get("course_title", "Assessment").replace(" ", "_").replace("/", "_")
        return Response(
            content=pdf_bytes,
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename=Official_Model_Answer_Key_{safe_name}.pdf"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PDF Generation failed: {str(e)}")


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


@router.get("/cloud-papers")
def list_cloud_papers():
    """Returns all question papers archived in cloud storage."""
    return cloud_vault.list_saved_cloud_papers()


@router.get("/cloud-papers/{paper_id}")
def get_cloud_paper(paper_id: str):
    """Retrieves a specific question paper and answer key from cloud storage."""
    record = cloud_vault.get_paper_by_id(paper_id)
    if not record:
        raise HTTPException(status_code=404, detail="Paper not found in cloud storage.")
    return record


@router.post("/save-to-cloud")
def save_paper_to_cloud_storage(payload: dict):
    course_title = payload.get("course_title", "Course Assessment")
    paper_text = payload.get("paper_text", "")
    analysis_result = payload.get("analysis_result", {})
    save_info = cloud_vault.save_paper_to_cloud(course_title, paper_text, analysis_result)
    return save_info


