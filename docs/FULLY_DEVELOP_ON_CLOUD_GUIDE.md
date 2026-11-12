# Production Manual: Fully Developing & Hosting on Google Cloud Platform

**Project Title:** AI-Driven Smart Examination Design and Bloom's Taxonomy Assessment Agent  
**System Name:** CogniExam Cloud Agentic Platform  
**Target Architecture:** Google Cloud Platform (GCP) Serverless Multi-Agent System  

---

## 1. System Architecture Overview

This platform is architected as a **Cloud-Native Pedagogical Assistant**. It does not rely on local compute; instead, every stage of syllabus processing, multi-agent reasoning, Bloom's cognitive auditing, and student assessment is orchestrated via serverless cloud primitives:

```
[User Browser: Faculty / Student]
               │ HTTPS (Port 443)
               ▼
[Google Cloud Run (Serverless Container)]
  ├── Frontend: Streamlit Interactive UI
  ├── Backend: Multi-Agent Orchestrator
  │
  ├── 1. Knowledge Layer ────► Google Cloud Storage (PDFs, Exam Papers)
  ├── 2. Vector Grounding ───► Vertex AI Vector Search / Cloud SQL (pgvector)
  ├── 3. Cognitive Engine ───► Vertex AI (Gemini 1.5 Pro & Flash)
  └── 4. Assessment OCR ─────► Google Cloud Vision API
```

---

## 2. Cloud Components & Responsibilities

| Cloud Service | Purpose in this Project | Why It Was Chosen |
| :--- | :--- | :--- |
| **Google Cloud Run** | Hosts the containerized application (`app.py`, agent pipelines) | Serverless, scales to 0 when idle (zero wasted compute cost), provides free HTTPS domain |
| **Vertex AI Studio (Gemini 1.5)** | Powers item authoring, Bloom's cognitive audit, and rubric evaluation | Native long-context window (up to 1M tokens) to ingest complete textbooks and multi-unit curricula |
| **Google Cloud Storage (GCS)** | Persists syllabus documents, generated exam papers, and scanned answer sheets | Encrypted, durable, provides time-limited signed URLs for downloads |
| **Google Cloud Build** | Builds Docker images and deploys them to Cloud Run automatically | Eliminates need for local Docker desktop; builds directly inside Google's cloud infrastructure |
| **Google Cloud Vision API** | Handwritten answer sheet OCR (for handwritten student assessments) | High-accuracy transcription of handwritten mathematical and scientific prose |

---

## 3. Step-by-Step Guide to Deploy on Google Cloud

### Prerequisites
1. A Google Cloud account with an active project (e.g., `antolin-dashboard`).
2. Google Cloud SDK (`gcloud` CLI) installed or access to [Google Cloud Shell](https://shell.cloud.google.com).

---

### Step 1: Open Terminal & Set Project
If using your local terminal or Cloud Shell:
```bash
# 1. Login to your Google Cloud account
gcloud auth login

# 2. Set your target project ID
gcloud config set project antolin-dashboard
```

---

### Step 2: Enable Required Cloud Services
Run the following single command to activate all necessary Google Cloud APIs:
```bash
gcloud services enable \
    run.googleapis.com \
    cloudbuild.googleapis.com \
    artifactregistry.googleapis.com \
    aiplatform.googleapis.com \
    vision.googleapis.com \
    storage.googleapis.com
```

---

### Step 3: Create a Cloud Storage Bucket (For Syllabi & Papers)
```bash
# Create bucket in us-central1 region
gcloud storage buckets create gs://antolin-dashboard-cogniexam --location=us-central1
```

---

### Step 4: Execute 1-Click Deployment to Cloud Run
From inside the project directory (`c:\Users\vishwanath\Desktop\Thamil MAM`):

#### On Windows (PowerShell):
```powershell
.\deploy_gcp.ps1
```

#### On Linux / Mac / Google Cloud Shell:
```bash
chmod +x deploy_gcp.sh
./deploy_gcp.sh
```

#### Or Run the Raw gcloud Command Directly:
```bash
gcloud run deploy cogniexam-agent \
    --source . \
    --region us-central1 \
    --platform managed \
    --allow-unauthenticated \
    --memory 2Gi \
    --cpu 2 \
    --timeout 300
```

> **Note on Build Process:** Google Cloud will automatically upload your code to **Cloud Build**, package it with the provided `Dockerfile`, register it in **Artifact Registry**, and assign you a secure, live production HTTPS URL such as:  
> `https://cogniexam-agent-xxxx-uc.a.run.app`

---

## 4. How to Verify & Test Your Live Cloud Deployment

1. Once the deployment finishes, the terminal will print your **Service URL**.
2. Open the URL in any web browser.
3. Test the workflows:
   - **Tab 1:** Load the sample syllabus or upload a course syllabus PDF.
   - **Tab 2:** Click **"Generate & Verify Exam Paper"** to trigger the Bloom's Taxonomy multi-agent swarm.
   - **Tab 3:** Test automated grading on a sample student answer against the generated step-by-step rubric.

---

## 5. Defense & Viva Talking Points (For Final Review)

When presenting this project to your examiners or guide:
1. **Explain the Pedagogical Innovation:**
   *"Manual examination setting suffers from Bloom's cognitive imbalance—typically concentrating 80% on lower-order recall (L1/L2). Our system enforces an algorithmic constraint solver to balance question papers according to Outcome-Based Education (OBE) accreditation standards (NBA/ABET)."*
2. **Explain the Multi-Agent Verification:**
   *"Rather than a single prompt, we deploy a collaborative agent swarm: an Item Authoring Agent, a Bloom's Taxonomy Auditor Agent that detects verb-gaming, and a Rubric Synthesis Agent that produces fine-grained mark breakdowns."*
3. **Explain the Cloud Architecture:**
   *"The solution is 100% cloud-native, deployed on Google Cloud Run with Vertex AI foundation models, serverless container auto-scaling, and Cloud Storage for pedagogical document persistence."*

