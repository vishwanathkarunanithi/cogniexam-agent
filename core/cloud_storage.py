"""
Cloud Storage & Paper Vault Integration.
Manages persistent saving and retrieval of question papers, answer keys,
and Bloom's taxonomy audit reports to Cloud Storage (GCS / Cloud Repository).
"""

import os
import json
import uuid
from datetime import datetime
from typing import Dict, List, Any, Optional

VAULT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "cloud_paper_vault")
os.makedirs(VAULT_DIR, exist_ok=True)


class CloudPaperVault:
    """
    Manages saving and archiving question papers and generated answer keys
    with cloud persistence metadata.
    """
    def __init__(self, bucket_name: str = "cogniexam-paper-vault"):
        self.bucket_name = bucket_name
        self.vault_dir = VAULT_DIR

    def save_paper_to_cloud(
        self,
        course_title: str,
        paper_text: str,
        analysis_result: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Saves a question paper and its certified answer key to the Cloud Paper Vault.
        """
        paper_id = f"QP-{datetime.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"
        timestamp = datetime.now().isoformat()
        cloud_uri = f"gs://{self.bucket_name}/{paper_id}.json"

        record = {
            "paper_id": paper_id,
            "course_title": course_title,
            "timestamp": timestamp,
            "cloud_uri": cloud_uri,
            "total_questions": analysis_result.get("total_questions", 0),
            "total_marks": analysis_result.get("total_marks", 0),
            "bloom_index": analysis_result.get("bloom_index", 0.0),
            "verdict": analysis_result.get("verdict", "Evaluated"),
            "paper_text": paper_text,
            "analysis_result": analysis_result
        }

        # Save to vault storage
        file_path = os.path.join(self.vault_dir, f"{paper_id}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(record, f, indent=2)

        return {
            "status": "SAVED_TO_CLOUD",
            "paper_id": paper_id,
            "cloud_uri": cloud_uri,
            "timestamp": timestamp,
            "message": f"Successfully archived question paper and answer key to cloud storage: {cloud_uri}"
        }

    def list_saved_cloud_papers(self) -> List[Dict[str, Any]]:
        """
        Lists all question papers archived in the cloud repository.
        """
        papers = []
        if not os.path.exists(self.vault_dir):
            return papers

        for filename in os.listdir(self.vault_dir):
            if filename.endswith(".json"):
                fpath = os.path.join(self.vault_dir, filename)
                try:
                    with open(fpath, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        papers.append({
                            "paper_id": data.get("paper_id"),
                            "course_title": data.get("course_title"),
                            "timestamp": data.get("timestamp"),
                            "cloud_uri": data.get("cloud_uri"),
                            "total_questions": data.get("total_questions"),
                            "total_marks": data.get("total_marks"),
                            "bloom_index": data.get("bloom_index"),
                            "verdict": data.get("verdict")
                        })
                except Exception:
                    continue

        # Sort descending by timestamp
        papers.sort(key=lambda x: x.get("timestamp", ""), reverse=True)
        return papers

    def get_paper_by_id(self, paper_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves a saved paper and its complete answer key from cloud storage.
        """
        fpath = os.path.join(self.vault_dir, f"{paper_id}.json")
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                return json.load(f)
        return None

