# CogniExam: 3-Minute Live Presentation Script

**Target Audience:** Professor / Academic Evaluator ("Mam") & Department Evaluation Committee  
**Total Duration:** 3 Minutes  

---

## Timeline & Action Flow

### 0:00 - 0:45 | Introduction & The Problem Statement
* **Action:** Double-click `run_local.bat`. Show the CogniExam web interface loading at `http://localhost:8000`.
* **What to Say:**
  > *"Good morning Mam and respected committee. Today, manual question paper auditing for Outcome-Based Education (OBE) and NBA accreditation takes faculty days of repetitive work. Furthermore, grading answer sheets often leads to discrepancies when students write accurate technical explanations in their own words.*
  > *We developed **CogniExam**, an autonomous multi-agent academic system powered by Google Cloud AI and Bloom's Revised Taxonomy that takes any university question paper, audits its cognitive equilibrium, and synthesizes official answer keys with step-by-step rubrics and student own-words grading guidelines."*

---

### 0:45 - 1:30 | Live Question Paper Ingestion & Institutional Adaptation
* **Action:** 
  1. Click the **"Pre-Loaded University Question Papers"** dropdown.
  2. Select **"CS8791 - Cloud Computing (Anna University)"** (or **"Velammal Autonomous Web Technologies"**).
  3. Notice how the paper transcript and Course ID immediately populate.
  4. Click the blue button: **"Audit Bloom Score & Generate Model Answer Key"**.
* **What to Say:**
  > *"Notice how the system dynamically adapts to any institution—here extracting Anna University and Department of Computer Science without hardcoding.*
  > *Our agent loop executes a 6-phase pipeline: parsing structure, classifying Bloom levels from L1 to L6, generating canonical solutions, running a deterministic verifier to ensure marking rubrics sum exactly to the question marks, checking for boilerplate, and auditing against OBE targets."*

---

### 1:30 - 2:15 | Reviewing Bloom Audit, Rubrics & Student "Own Words" Policy
* **Action:** Scroll to the Audit Scorecard and Question 1.
* **Point out:**
  1. **Bloom Cognitive Index:** (e.g. 4.96 / 6.0) and the OBE Radar Chart.
  2. **Smart Exam Design Suggestions:** Highlight the recommended question stems for rebalancing curriculum depth.
  3. **Question 1 Box:**
     - Bloom Level: $L_1$ Remember, Directive Verb: *State*.
     - **Specific Rubric:** *Definition of Cloud Computing: 1.0 Mark | 5 NIST Characteristics: 1.0 Mark*.
     - **Student Own-Words Criteria:** Evaluator guidance explicitly instructing faculty to award partial/full credit if core concepts are met even if phrasing differs from textbook definitions.
     - **Status Banner:** *Faculty verified: No* (highlighting academic integrity).
* **What to Say:**
  > *"Here you can see the question-specific rubrics in 0.5-mark increments. Look at the Evaluator Guidance disclaimer: it protects students who explain concepts logically in their own words. The verifier checks that every rubric sums exactly to the question total."*

---

### 2:15 - 3:00 | Publication Academic PDF Export & Cloud Vault
* **Action:** 
  1. Click the **"Download Academic PDF Answer Key"** button.
  2. Open the downloaded PDF in the browser.
  3. Show the clean 3-column institutional header, running *Page X of Y* footer, and complete absence of informal emojis.
  4. Click the **"Cloud Paper Vault"** tab in the app to show that this certified paper has been versioned and indexed for digital paper-saving.
* **What to Say:**
  > *"With one click, faculty can export a formal, publication-ready academic PDF with official tables, running footers, and complete rubrics, fully formatted for university boards.*
  > *All evaluations are versioned in our Cloud Paper Vault to eliminate paper waste. If internet connectivity is ever disrupted, our offline presentation backup in `demo_backup/` guarantees zero-downtime demonstration.*
  > *Thank you, Mam. We welcome your questions."*

