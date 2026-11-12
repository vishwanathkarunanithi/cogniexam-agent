# CogniExam: AI-Driven Smart Examination Design and Bloom’s Taxonomy Assessment Agent

**Submitted for Academic Evaluation / Capstone Defense**  
**Architecture:** Autonomous Multi-Agent Pedagogical System with Cloud & Hybrid Runtimes  

---

## ⚡ Quick Start: How to Run in 1 Click

You do **not** need to manually configure complicated database servers or API keys to evaluate this project. It is packaged with self-installing launchers that configure all dependencies automatically:

### On Windows (Recommended):
> **Simply double-click:** `RUN_APP.bat`  
> *(This automatically checks Python, installs any missing packages, and opens your web browser to the dashboard)*.

### On macOS / Linux:
Open terminal in this folder and run:
```bash
bash RUN_APP.sh
```

### Manual Command (Optional):
```bash
pip install -r requirements.txt
streamlit run app.py
```
*The web portal will open at `http://localhost:8501`.*

---

## 🧭 What to Test in the Dashboard (Feature Walkthrough)

The application is structured into four intuitive tabs designed for faculty and academic evaluators:

### 1. 📚 Tab 1: Syllabus & Curriculum Ingestion (RAG Grounding)
- Pre-loaded with an Outcome-Based Education (OBE) curriculum: *"Cloud Computing & Distributed Systems"*.
- Displays breakdown into **Course Units**, **Topics**, and **Course Outcomes (CO1 to CO4)**.
- You can also upload any custom course syllabus (PDF or TXT) to test dynamic parsing.

### 2. 🎯 Tab 2: Smart Exam Blueprint & Multi-Agent Question Generator
- **Configure Exam Parameters:** Select total marks (e.g., 50 or 100) and duration.
- **Set Target Bloom's Weights:** Adjust the cognitive distribution sliders:
  - **L1 (Remember) & L2 (Understand):** Lower-order thinking skills.
  - **L3 (Apply) & L4 (Analyze):** Medium-order problem-solving skills.
  - **L5 (Evaluate) & L6 (Create):** Higher-order architectural & synthesis skills.
- Click **"🚀 Generate & Verify Exam Paper with Multi-Agent Swarm"**:
  - The system coordinates an **Item Authoring Agent**, a **Bloom's Taxonomy Auditor Agent**, and a **Rubric Synthesis Agent**.
  - Generates balanced sections (Part A, Part B, Part C) with verifiable Bloom badges, action verbs, and **step-by-step scoring rubrics**.
  - Provides instant **Markdown and JSON export** for printing.

### 3. ✍️ Tab 3: Intelligent Assessment & Grading Agent
- Demonstrates automated grading of student submissions against step-by-step rubrics.
- Grades student submissions and awards partial credit with semantic reasoning.
- Pinpoints individual student cognitive strengths and learning growth areas.

### 4. ☁️ Tab 4: Full Cloud-Native Deployment Guide
- Explains the complete production cloud architecture on **Google Cloud Platform (GCP)**.
- Details the serverless deployment to **Google Cloud Run**, **Vertex AI (Gemini 1.5 Pro)**, and **Google Cloud Storage (GCS)**.
- Includes a 1-click script (`deploy_gcp.ps1` / `deploy_gcp.sh`) to launch the entire platform onto Google Cloud.

---

## 🧠 Bloom's Revised Taxonomy Engine

The core engine maps cognitive demands across 6 pedagogical levels:

| Level | Cognitive Domain | Action Verbs Tested | Target Question Style |
| :---: | :--- | :--- | :--- |
| **L1** | **Remember** | Define, List, State, Recall | Definitions, fundamental principles |
| **L2** | **Understand** | Explain, Summarize, Differentiate | Conceptual mechanisms and trade-offs |
| **L3** | **Apply** | Calculate, Solve, Implement | Numerical calculations, quorum consensus |
| **L4** | **Analyze** | Analyze, Contrast, Deconstruct | Comparative architectural analysis |
| **L5** | **Evaluate** | Critique, Justify, Defend | Critical review of fail-stop protocols |
| **L6** | **Create** | Design, Formulate, Construct | End-to-end resilient system architecture |

---

## 📂 Repository File Structure

```
Thamil MAM/
├── RUN_APP.bat              <-- Double-click to start on Windows
├── RUN_APP.sh               <-- Double-click / execute on macOS/Linux
├── app.py                   <-- Main interactive Streamlit application
├── requirements.txt         <-- Python library dependencies
├── Dockerfile               <-- Production container for Google Cloud Run
├── cloudbuild.yaml          <-- Google Cloud Build CI/CD configuration
├── deploy_gcp.ps1           <-- Automated 1-click Google Cloud deployment (PowerShell)
├── deploy_gcp.sh            <-- Automated 1-click Google Cloud deployment (Bash)
├── core/
│   ├── bloom_engine.py      <-- Bloom's taxonomy classifier and cognitive calculator
│   ├── cloud_client.py      <-- Cloud integration (Vertex AI / Gemini API + offline fallback)
│   ├── exam_generator.py    <-- Multi-agent exam blueprint synthesizer
│   ├── assessment_agent.py  <-- Step-wise rubric assessment and diagnostic feedback
│   └── syllabus_parser.py   <-- Syllabus document and PDF parser
├── data/
│   └── sample_syllabus.json <-- Sample curriculum for immediate demonstration
└── docs/
    └── FULLY_DEVELOP_ON_CLOUD_GUIDE.md <-- Detailed cloud engineering manual
```

---
*Developed for Academic Review and Outcome-Based Education (OBE) Examination Design.*

