"""
Formal Academic PDF Answer Key Generator using ReportLab.
Constructs publication-grade, professionally aligned PDF documents
without informal emojis or casual characters.
"""

import os
import io
from typing import Dict, Any, List
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas


class NumberedCanvas(canvas.Canvas):
    """Adds formal running headers and page numbers (Page X of Y) to each page."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#475569"))
        
        # Header (pages after page 1)
        if self._pageNumber > 1:
            inst = getattr(NumberedCanvas, 'current_institution', 'OFFICIAL EXAMINATION EVALUATION').upper()
            self.drawString(54, 800, f"{inst[:55]} - OFFICIAL MODEL ANSWER KEY")
            self.drawRightString(558, 800, "CONFIDENTIAL / FACULTY USE ONLY")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, 792, 558, 792)

        # Running Footer
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 45, 558, 45)
        self.drawString(54, 32, "Outcome-Based Education (OBE) Certified • Bloom's Revised Taxonomy Evaluation Scheme")
        self.drawRightString(558, 32, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()


class AcademicPDFGenerator:
    """
    Builds clean, publication-ready academic PDF answer keys.
    """
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self._create_custom_styles()

    def _create_custom_styles(self):
        self.styles.add(ParagraphStyle(
            name='InstTitle',
            fontName='Helvetica-Bold',
            fontSize=13,
            leading=16,
            alignment=1, # Center
            textColor=colors.HexColor("#0F172A")
        ))
        self.styles.add(ParagraphStyle(
            name='DeptSubtitle',
            fontName='Helvetica',
            fontSize=10,
            leading=13,
            alignment=1,
            textColor=colors.HexColor("#334155")
        ))
        self.styles.add(ParagraphStyle(
            name='DocTypeBanner',
            fontName='Helvetica-Bold',
            fontSize=11,
            leading=14,
            alignment=1,
            textColor=colors.HexColor("#1E3A8A"),
            spaceBefore=4,
            spaceAfter=6
        ))
        self.styles.add(ParagraphStyle(
            name='MetaLeft',
            fontName='Helvetica',
            fontSize=8.5,
            leading=11,
            alignment=0, # Left
            textColor=colors.HexColor("#334155")
        ))
        self.styles.add(ParagraphStyle(
            name='MetaCenter',
            fontName='Helvetica',
            fontSize=8.5,
            leading=11,
            alignment=1, # Center
            textColor=colors.HexColor("#334155")
        ))
        self.styles.add(ParagraphStyle(
            name='MetaRight',
            fontName='Helvetica',
            fontSize=8.5,
            leading=11,
            alignment=2, # Right
            textColor=colors.HexColor("#1D4ED8")
        ))
        self.styles.add(ParagraphStyle(
            name='MetaLine',
            fontName='Helvetica',
            fontSize=9,
            leading=12,
            alignment=1,
            textColor=colors.HexColor("#475569")
        ))
        self.styles.add(ParagraphStyle(
            name='DisclaimerHeading',
            fontName='Helvetica-Bold',
            fontSize=8.5,
            leading=11,
            textColor=colors.HexColor("#92400E")
        ))
        self.styles.add(ParagraphStyle(
            name='DisclaimerText',
            fontName='Helvetica',
            fontSize=8,
            leading=11,
            textColor=colors.HexColor("#78350F")
        ))
        self.styles.add(ParagraphStyle(
            name='QuestionHeader',
            fontName='Helvetica-Bold',
            fontSize=10,
            leading=13,
            textColor=colors.HexColor("#0F172A"),
            spaceBefore=8,
            spaceAfter=3
        ))
        self.styles.add(ParagraphStyle(
            name='QuestionMeta',
            fontName='Helvetica-Bold',
            fontSize=8.5,
            leading=11,
            textColor=colors.HexColor("#2563EB")
        ))
        self.styles.add(ParagraphStyle(
            name='AnswerLabel',
            fontName='Helvetica-Bold',
            fontSize=9,
            leading=12,
            textColor=colors.HexColor("#047857"),
            spaceBefore=4,
            spaceAfter=2
        ))
        self.styles.add(ParagraphStyle(
            name='AnswerBody',
            fontName='Helvetica',
            fontSize=8.5,
            leading=12,
            textColor=colors.HexColor("#1E293B")
        ))
        self.styles.add(ParagraphStyle(
            name='RubricLabel',
            fontName='Helvetica-Bold',
            fontSize=8.5,
            leading=11,
            textColor=colors.HexColor("#334155"),
            spaceBefore=4,
            spaceAfter=2
        ))
        self.styles.add(ParagraphStyle(
            name='RubricItem',
            fontName='Helvetica',
            fontSize=8,
            leading=10,
            textColor=colors.HexColor("#1E293B")
        ))
        self.styles.add(ParagraphStyle(
            name='OwnWordsHeading',
            fontName='Helvetica-Bold',
            fontSize=8,
            leading=10,
            textColor=colors.HexColor("#1D4ED8"),
            spaceBefore=3,
            spaceAfter=1
        ))

    def generate_pdf_bytes(self, result: Dict[str, Any]) -> bytes:
        """
        Compiles the analyzed result into a high-grade academic PDF.
        """
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=A4,
            leftMargin=54,
            rightMargin=54,
            topMargin=54,
            bottomMargin=54
        )

        story = []

        # 1. Formal Institutional Header
        inst_name = str(result.get("institution_name") or "INSTITUTION OF HIGHER EDUCATION").strip().strip('|').strip().upper()
        dept = str(result.get("department") or "DEPARTMENT OF ACADEMIC ASSESSMENT").strip().strip('|').strip().upper()
        course_title = str(result.get("course_title") or "COURSE ASSESSMENT").strip().strip('|').strip().upper()
        NumberedCanvas.current_institution = inst_name

        story.append(Paragraph(inst_name, self.styles['InstTitle']))
        story.append(Paragraph(dept, self.styles['DeptSubtitle']))
        story.append(Paragraph("OFFICIAL MODEL ANSWER KEY AND EVALUATION SCHEME", self.styles['DocTypeBanner']))
        
        # Clean 3-column metadata table (no stray pipes, perfectly balanced on A4)
        meta_left = Paragraph(f"<b>Course:</b> {course_title}", self.styles['MetaLeft'])
        meta_center = Paragraph(f"<b>Total Marks:</b> {result.get('total_marks', 50)}", self.styles['MetaCenter'])
        meta_right = Paragraph(f"<b>Bloom Index:</b> {result.get('bloom_index', 3.5)} / 6.0", self.styles['MetaRight'])
        
        meta_table = Table([[meta_left, meta_center, meta_right]], colWidths=[240, 110, 137])
        meta_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 3),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ]))
        story.append(meta_table)
        story.append(Spacer(1, 3))
        
        # Faculty verification status tag (R5)
        fac_verify_p = Paragraph("<b>Audit Status:</b> Provisional Draft &nbsp;|&nbsp; <b>Faculty Verified:</b> <font color='#DC2626'><b>No</b></font> (Autonomous Cognitive Agent Output)", self.styles['MetaCenter'])
        story.append(fac_verify_p)
        story.append(Spacer(1, 4))
        story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#CBD5E1"), spaceBefore=2, spaceAfter=8))

        # 2. Formal Evaluator Disclaimer Box (Own Words Evaluation Guidance)
        disclaimer_html = (
            "<b>EVALUATOR GUIDANCE (STUDENT OWN-WORDS EVALUATION):</b><br/>"
            "Students are encouraged to express technical explanations, derivations, and solutions in their own words. "
            "Evaluators must award full or proportional marks whenever the fundamental conceptual logic, necessary technical "
            "keywords, and core propositions are satisfied, even if phrasing differs from the canonical solution. "
            "Refer to the 'Key Semantic Criteria for Student Own Words' outlined under each question."
        )
        disclaimer_table = Table(
            [[Paragraph(disclaimer_html, self.styles['DisclaimerText'])]],
            colWidths=[490]
        )
        disclaimer_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#FEF3C7")),
            ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#F59E0B")),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
            ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ]))
        story.append(disclaimer_table)
        story.append(Spacer(1, 10))

        # 3. Bloom Summary Table
        metrics = result.get("metrics", {})
        summary_data = [
            ["Metric", "Value", "Metric", "Value"],
            [
                "Total Questions", str(result.get("total_questions", 0)),
                "Bloom Cognitive Index", f"{result.get('bloom_index', 3.5)} / 6.0"
            ],
            [
                "Lower-Order Thinking (L1-L2)", f"{metrics.get('low_order_pct', 0):.1f}%",
                "Higher-Order Thinking (L5-L6)", f"{metrics.get('high_order_pct', 0):.1f}%"
            ],
            [
                "Middle-Order Thinking (L3-L4)", f"{metrics.get('medium_order_pct', 0):.1f}%",
                "OBE Accreditation Verdict", str(result.get("verdict", "Certified"))[:30]
            ]
        ]
        summary_table = Table(summary_data, colWidths=[130, 115, 130, 115])
        summary_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F1F5F9")),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor("#0F172A")),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ]))
        story.append(summary_table)
        story.append(Spacer(1, 8))

        # 3b. Smart Exam Design Recommendations (R4 / R7)
        design_audit = result.get("design_audit")
        if design_audit and design_audit.get("rebalance_suggestions"):
            design_lines = ["<b>SMART EXAM DESIGN & OBE REBALANCE RECOMMENDATIONS:</b>"]
            for s in design_audit["rebalance_suggestions"]:
                status_color = "#DC2626" if s.get("status") == "under_represented" else "#D97706"
                lvl = s.get("level", "L1")
                diff = s.get("difference_pct", 0.0)
                diff_str = f"{diff:+.1f}%"
                design_lines.append(f"&bull; <b>{lvl} ({s.get('status').replace('_', ' ').title()})</b>: Actual {s.get('actual_pct')}% vs Target {s.get('target_pct')}% ({diff_str})")
                for stem in s.get("recommended_stems", [])[:2]:
                    design_lines.append(f"&nbsp;&nbsp;&nbsp;&nbsp;- <i>Suggested Stem:</i> {stem}")
            
            design_html = "<br/>".join(design_lines)
            design_table = Table([[Paragraph(design_html, self.styles['RubricItem'])]], colWidths=[490])
            design_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
                ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
                ('TOPPADDING', (0, 0), (-1, -1), 5),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
                ('LEFTPADDING', (0, 0), (-1, -1), 8),
                ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ]))
            story.append(design_table)
            story.append(Spacer(1, 10))
        else:
            story.append(Spacer(1, 8))

        # 4. Questions & Model Answers
        for q in result.get("questions", []):
            q_elements = []

            # Section & Question Title
            sec = q.get('section', 'PART A')
            q_num = q.get('q_no', '1')
            marks = q.get('marks', 4)
            bloom_lvl = q.get('bloom_level', 'L2')
            bloom_name = q.get('bloom_name', 'Understand')
            action_verb = q.get('action_verb', 'explain')

            header_text = f"<b>{sec} &bull; Question {q_num} [{marks} Marks]</b>"
            engine_str = q.get('engine_used', 'gemini-3.5-flash-lite')
            conf_tag = q.get('confidence_tag', 'AI Synthesized - High confidence')
            conf_color = '#B45309' if 'low confidence' in conf_tag.lower() else '#047857'
            meta_text = f"Bloom: {bloom_lvl} ({bloom_name}) &nbsp;|&nbsp; Verb: {action_verb} &nbsp;|&nbsp; Engine: {engine_str} &nbsp;|&nbsp; <font color='{conf_color}'><b>[{conf_tag}]</b></font>"
            
            q_elements.append(Paragraph(header_text, self.styles['QuestionHeader']))
            q_elements.append(Paragraph(meta_text, self.styles['QuestionMeta']))
            
            # Question Body
            q_text = f"<b>Question:</b> {q.get('question')}"
            q_elements.append(Paragraph(q_text, self.styles['AnswerBody']))
            q_elements.append(Spacer(1, 3))

            # Model Answer Box
            ans_content = f"<b>Canonical Model Answer:</b><br/>{q.get('model_answer', '')}"
            ans_table = Table([[Paragraph(ans_content, self.styles['AnswerBody'])]], colWidths=[490])
            ans_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
                ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
                ('TOPPADDING', (0, 0), (-1, -1), 5),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
                ('LEFTPADDING', (0, 0), (-1, -1), 8),
                ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ]))
            q_elements.append(ans_table)
            q_elements.append(Spacer(1, 4))

            # Numerical verification note if applicable
            num_v = q.get("numerical_verification")
            if num_v and num_v.get("is_numerical"):
                status_txt = "Code Verified: Computed result matches canonical answer." if num_v.get("matches_canonical") else "Flagged for manual review."
                num_p = Paragraph(f"<b>Numerical Verification:</b> {status_txt} &nbsp;|&nbsp; <b>Faculty Verified:</b> No", self.styles['MetaLeft'])
                q_elements.append(num_p)
                q_elements.append(Spacer(1, 2))

            # Step-by-Step Marking Rubric Table
            rubric_rows = [["Grading Criterion / Step", "Marks"]]
            for r in q.get("rubric", []):
                rubric_rows.append([r.get("criterion", ""), f"{r.get('marks', 0)} Marks"])

            rubric_table = Table(rubric_rows, colWidths=[410, 80])
            rubric_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#E2E8F0")),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 7.5),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
                ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
                ('TOPPADDING', (0, 0), (-1, -1), 3),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
                ('LEFTPADDING', (0, 0), (-1, -1), 6),
                ('RIGHTPADDING', (0, 0), (-1, -1), 6),
            ]))
            q_elements.append(rubric_table)
            q_elements.append(Spacer(1, 3))

            # Own Words Criteria
            own_words = q.get("own_words_criteria", [])
            if own_words:
                ow_lines = ["<b>Key Semantic Criteria for Student's Own Words:</b>"]
                for c in own_words:
                    ow_lines.append(f"&bull; {c}")
                ow_text = "<br/>".join(ow_lines)
                ow_table = Table([[Paragraph(ow_text, self.styles['RubricItem'])]], colWidths=[490])
                ow_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#EFF6FF")),
                    ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#BFDBFE")),
                    ('TOPPADDING', (0, 0), (-1, -1), 4),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                    ('LEFTPADDING', (0, 0), (-1, -1), 8),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 8),
                ]))
                q_elements.append(ow_table)

            q_elements.append(Spacer(1, 8))
            story.append(KeepTogether(q_elements))

        # Build document
        doc.build(story, canvasmaker=NumberedCanvas)
        buffer.seek(0)
        return buffer.getvalue()

