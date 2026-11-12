"""
Syllabus and Curriculum Parser.
Extracts Course Outcomes, Units, Topics, and Pedagogical Constraints.
"""

import os
import json
from typing import Dict, List, Any

try:
    import fitz  # PyMuPDF
    HAS_PYMUPDF = True
except ImportError:
    HAS_PYMUPDF = False


class SyllabusParser:
    """
    Parses and extracts structured modules from syllabus documents.
    """
    def __init__(self):
        pass

    def parse_text(self, text: str) -> Dict[str, Any]:
        """Parses raw syllabus text into structured units and learning outcomes."""
        lines = [line.strip() for line in text.strip().split("\n") if line.strip()]
        units = []
        current_unit = {"title": "General Curriculum", "topics": []}
        
        for line in lines:
            lower = line.lower()
            if any(lower.startswith(k) for k in ["unit", "module", "chapter", "section"]):
                if current_unit["topics"]:
                    units.append(current_unit)
                current_unit = {"title": line, "topics": []}
            else:
                current_unit["topics"].append(line)
                
        if current_unit["topics"]:
            units.append(current_unit)
            
        return {
            "total_units": len(units),
            "units": units,
            "raw_text_length": len(text)
        }

    def parse_pdf(self, file_bytes: bytes) -> str:
        """Extracts text content from uploaded PDF using PyMuPDF."""
        if not HAS_PYMUPDF:
            return "PyMuPDF not available in runtime. Please paste syllabus text directly."
        
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        extracted_text = []
        for page in doc:
            extracted_text.append(page.get_text())
        doc.close()
        return "\n".join(extracted_text)

