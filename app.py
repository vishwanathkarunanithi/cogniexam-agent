"""
Streamlit Web Interface for AI-Driven Smart Examination Design
and Bloom's Taxonomy Assessment Agent.
Focused on Question Paper Bloom's Scoring and Automated Answer Key Synthesis.
"""

import os
import json
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from core.bloom_engine import BLOOM_TAXONOMY_LEVELS, compute_exam_cognitive_distribution
from core.cloud_client import CloudAgentClient
from core.syllabus_parser import SyllabusParser
from core.exam_generator import SmartExamGenerator
from core.assessment_agent import AssessmentAgent
from core.qp_analyzer import QuestionPaperAnalyzer

# Page Configuration
st.set_page_config(
    page_title="AI Smart Exam & Bloom's Assessment Agent",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .badge-l1 { background-color: #DBEAFE; color: #1E40AF; padding: 4px 10px; border-radius: 4px; font-weight: 600; font-size: 0.85rem; }
    .badge-l2 { background-color: #DCFCE7; color: #166534; padding: 4px 10px; border-radius: 4px; font-weight: 600; font-size: 0.85rem; }
    .badge-l3 { background-color: #FEF9C3; color: #854D0E; padding: 4px 10px; border-radius: 4px; font-weight: 600; font-size: 0.85rem; }
    .badge-l4 { background-color: #FFEDD5; color: #9A3412; padding: 4px 10px; border-radius: 4px; font-weight: 600; font-size: 0.85rem; }
    .badge-l5 { background-color: #FCE7F3; color: #9D174D; padding: 4px 10px; border-radius: 4px; font-weight: 600; font-size: 0.85rem; }
    .badge-l6 { background-color: #F3E8FF; color: #6B21A8; padding: 4px 10px; border-radius: 4px; font-weight: 600; font-size: 0.85rem; }
    .card-box {
        background: #F9FAFB;
        border: 1px solid #E5E7EB;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)


# Initialize Session State
if "cloud_client" not in st.session_state:
    st.session_state.cloud_client = CloudAgentClient()
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None
if "current_exam" not in st.session_state:
    st.session_state.current_exam = None


# --- SIDEBAR: Cloud Settings & Health ---
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/exam.png", width=100)
    st.title("System Controls")
    
    st.markdown("### ☁️ Cloud AI Connection")
    mode = st.session_state.cloud_client.mode
    if mode == "gemini_api":
        st.success("🟢 Google Gemini Cloud AI: Connected")
    elif mode == "vertex_ai":
        st.success("🟢 Google Vertex AI: Connected")
    else:
        st.info("🟡 Autonomous Simulation Engine")

    with st.expander("⚙️ Configure API Key"):
        key_val = st.text_input("Gemini API Key", type="password", value=st.session_state.cloud_client.api_key)
        if st.button("Save & Reconnect"):
            st.session_state.cloud_client = CloudAgentClient(api_key=key_val)
            st.rerun()

    st.markdown("---")
    st.markdown("### 📊 Bloom's Cognitive Levels")
    for lvl, info in BLOOM_TAXONOMY_LEVELS.items():
        st.markdown(f"**{lvl} - {info['name']}**: *{info['verbs'][0].capitalize()}, {info['verbs'][1]}...*")


# --- MAIN HEADER ---
st.markdown('<div class="main-title">CogniExam: Smart Examination Design & Bloom’s Assessment Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Outcome-Based Education (OBE) • Question Paper Bloom Auditing • Canonical Answer Keys & Rubrics</div>', unsafe_allow_html=True)

# Navigation Tabs (Primary Problem Statement is Tab 1)
tab_analyze, tab_generate, tab_assess, tab_cloud = st.tabs([
    "📄 1. Upload Question Paper ➔ Bloom Score & Answer Key",
    "🎯 2. Author & Synthesize New Exam Paper",
    "✍️ 3. Student Assessment & Partial Grading Agent",
    "☁️ 4. Full Cloud-Native Deployment Architecture"
])


# ==============================================================================
# TAB 1: UPLOAD QUESTION PAPER ➔ BLOOM SCORE & ANSWER KEY (PRIMARY PROBLEM)
# ==============================================================================
with tab_analyze:
    st.subheader("Question Paper Bloom's Scoring & Answer Key Generator")
    st.write("Upload or paste any university/college question paper to automatically evaluate its Bloom's cognitive distribution, audit question levels, and synthesize canonical model answers with step-by-step grading rubrics.")

    col_input, col_preview = st.columns([1, 1])

    with col_input:
        st.markdown("#### 1. Input Question Paper")
        
        # Load Sample Button
        if st.button("📋 Load Sample University Question Paper (Cloud & Distributed Systems)"):
            try:
                with open(os.path.join("data", "sample_question_paper.txt"), "r") as f:
                    st.session_state.paper_text = f.read()
            except Exception:
                pass
            st.success("Loaded university question paper into editor!")

        qp_course_title = st.text_input("Course Name / Code", value="CS8401 - Cloud Computing & Distributed Systems")
        
        # File Uploader
        uploaded_qp = st.file_uploader("Upload Question Paper (PDF or TXT)", type=["pdf", "txt"])
        if uploaded_qp is not None:
            if uploaded_qp.name.endswith(".pdf"):
                parser = SyllabusParser()
                st.session_state.paper_text = parser.parse_pdf(uploaded_qp.read())
            else:
                st.session_state.paper_text = uploaded_qp.read().decode("utf-8")
            st.success("File uploaded successfully!")

        default_text = st.session_state.get("paper_text", "")
        if not default_text:
            try:
                with open(os.path.join("data", "sample_question_paper.txt"), "r") as f:
                    default_text = f.read()
            except Exception:
                default_text = "1. Define CAP theorem. [5 Marks]\n2. Explain two-phase commit protocol. [5 Marks]"

        paper_content = st.text_area("Question Paper Content (Editable):", value=default_text, height=220)

    with col_preview:
        st.markdown("#### 2. Action")
        st.info("The AI Agent Swarm will:\n- Extract and isolate each individual question and allocated marks.\n- Classify each question according to Bloom's Revised Taxonomy (L1 to L6).\n- Compute the overall Paper Cognitive Score (Bloom Index / 6.0) and OBE balance.\n- Synthesize a comprehensive canonical Answer Key and step-by-step marking rubrics.")
        
        analyze_btn = st.button("🚀 Analyze Question Paper & Generate Answer Key", type="primary", use_container_width=True)

    if analyze_btn and paper_content:
        with st.spinner("Analyzing Question Paper with Google Cloud AI: Extracting Questions ➔ Calibrating Bloom Levels ➔ Synthesizing Answer Keys & Step Rubrics..."):
            analyzer = QuestionPaperAnalyzer(st.session_state.cloud_client)
            result = analyzer.analyze_paper_and_generate_key(paper_content, course_title=qp_course_title)
            st.session_state.analysis_result = result
            st.success("Question Paper Successfully Audited & Answer Key Generated!")

    # Display Results
    if st.session_state.analysis_result:
        res = st.session_state.analysis_result
        metrics = res.get("metrics", {})
        
        st.markdown("---")
        st.markdown(f"### 📋 Audit Report: {res.get('exam_title')}")
        
        # High-level Metrics Row
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total Marks", f"{res.get('total_marks')} pts")
        m2.metric("Questions Audited", res.get("total_questions"))
        m3.metric("Bloom Cognitive Depth", f"{res.get('bloom_index', 3.0)} / 6.0")
        m4.metric("OBE Accreditation Verdict", "Certified" if res.get('bloom_index', 0) >= 2.5 else "Needs Revision")

        st.info(f"**Cognitive Balance Assessment:** {res.get('verdict')}")

        # Visualizations (Bar chart & Category Breakdown)
        c_chart, c_cats = st.columns([1, 1])
        with c_chart:
            dist = metrics.get("distribution", {})
            if dist:
                df_bar = pd.DataFrame([
                    {"Cognitive Level": f"{k} ({v['name']})", "Marks": v["marks"], "Percentage": v["percentage"]}
                    for k, v in dist.items()
                ])
                fig = px.bar(df_bar, x="Cognitive Level", y="Marks", color="Cognitive Level", text="Marks", title="Marks Allocated by Bloom's Taxonomy Level")
                fig.update_layout(showlegend=False, height=280)
                st.plotly_chart(fig, use_container_width=True)

        with c_cats:
            st.markdown("#### Cognitive Tier Distribution")
            st.write(f"- **Lower-Order Thinking (L1 Remember & L2 Understand):** `{metrics.get('low_order_pct', 0):.1f}%`")
            st.write(f"- **Middle-Order Thinking (L3 Apply & L4 Analyze):** `{metrics.get('medium_order_pct', 0):.1f}%`")
            st.write(f"- **Higher-Order Thinking (L5 Evaluate & L6 Create):** `{metrics.get('high_order_pct', 0):.1f}%`")
            
            # Progress bar visualization
            lo = metrics.get('low_order_pct', 0) / 100
            mo = metrics.get('medium_order_pct', 0) / 100
            ho = metrics.get('high_order_pct', 0) / 100
            st.progress(min(1.0, lo + mo + ho))

        # Detailed Questions + Model Answers + Rubric Schemes
        st.markdown("### 📝 Certified Answer Key & Step-by-Step Marking Rubrics")
        
        for q in res.get("questions", []):
            lvl = q.get("bloom_level", "L2")
            badge_class = f"badge-{lvl.lower()}"
            
            st.markdown(f"""
            <div class="card-box">
                <h4>Question {q.get('q_no')} &nbsp;•&nbsp; {q.get('marks')} Marks &nbsp;•&nbsp; <span class="{badge_class}">{lvl} - {q.get('bloom_name')}</span></h4>
                <p><strong>Question Text:</strong> {q.get('question')}</p>
                <p><em>Action Verb Identified:</em> <code>{q.get('action_verb', 'N/A')}</code> &nbsp;|&nbsp; <em>Justification:</em> {q.get('justification', '')}</p>
            </div>
            """, unsafe_allow_html=True)

            with st.expander(f"👁️ View Canonical Answer Key & Step Rubric for Question {q.get('q_no')}"):
                st.markdown(f"**Canonical Model Answer:**\n> {q.get('model_answer')}")
                st.markdown("**Step-by-Step Marking Rubric:**")
                for r in q.get("rubric", []):
                    st.markdown(f"- **{r.get('criterion')}**: `{r.get('marks')} Marks`")
            st.write("")

        # Export Report & Answer Key
        st.markdown("#### 📥 Download Official Answer Key & Bloom Audit Report")
        analyzer = QuestionPaperAnalyzer(st.session_state.cloud_client)
        md_answer_key = analyzer.format_as_printable_answer_key(res)
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            st.download_button(
                "📄 Download Official Answer Key & Report (Markdown / Print-Ready)",
                data=md_answer_key,
                file_name="Bloom_Audit_and_Answer_Key.md",
                mime="text/markdown",
                use_container_width=True
            )
        with col_d2:
            st.download_button(
                "💾 Download Full Schema (JSON)",
                data=json.dumps(res, indent=2),
                file_name="Bloom_Answer_Key_Schema.json",
                mime="application/json",
                use_container_width=True
            )


# ==============================================================================
# TAB 2: SYNTHESIZE NEW EXAM PAPER FROM SCRATCH
# ==============================================================================
with tab_generate:
    st.subheader("Autonomous Blueprint & Cognitive Balancing Loop")
    st.write("Generate a brand new, balanced question paper from course syllabus specifications with strict Bloom weight constraints.")
    
    col_settings, col_bloom = st.columns([1, 1])
    with col_settings:
        exam_course = st.text_input("Target Course Title", value="Cloud Computing & Distributed Systems", key="gen_cname")
        total_marks = st.number_input("Total Examination Marks", min_value=20, max_value=100, value=50, step=10, key="gen_marks")
        exam_duration = st.number_input("Duration (Minutes)", min_value=30, max_value=180, value=90, step=15, key="gen_dur")

    with col_bloom:
        st.markdown("#### Target Bloom Cognitive Weightage (%)")
        col_b1, col_b2, col_b3 = st.columns(3)
        with col_b1:
            l1_target = st.slider("L1: Remember", 0, 50, 10, key="s_l1")
            l2_target = st.slider("L2: Understand", 0, 50, 15, key="s_l2")
        with col_b2:
            l3_target = st.slider("L3: Apply", 0, 50, 25, key="s_l3")
            l4_target = st.slider("L4: Analyze", 0, 50, 20, key="s_l4")
        with col_b3:
            l5_target = st.slider("L5: Evaluate", 0, 50, 15, key="s_l5")
            l6_target = st.slider("L6: Create", 0, 50, 15, key="s_l6")

    gen_btn = st.button("🚀 Synthesize Balanced Question Paper", type="primary")
    if gen_btn:
        with st.spinner("Multi-Agent Swarm Active..."):
            generator = SmartExamGenerator(st.session_state.cloud_client)
            exam = generator.generate_exam_paper(
                course_name=exam_course,
                syllabus_summary="Distributed consensus, virtualization, storage pipelines, and disaster recovery.",
                total_marks=total_marks,
                target_distribution={"L1": l1_target, "L2": l2_target, "L3": l3_target, "L4": l4_target, "L5": l5_target, "L6": l6_target}
            )
            st.session_state.current_exam = exam
            st.success("New Question Paper Synthesized!")

    if st.session_state.current_exam:
        e = st.session_state.current_exam
        st.markdown(f"### {e.get('exam_title')}")
        for sec in e.get("sections", []):
            st.markdown(f"#### {sec.get('section_name')}")
            for q in sec.get("questions", []):
                st.markdown(f"**Q{q.get('q_no')}. {q.get('question')}** *[{q.get('marks')} Marks | {q.get('bloom_level')} - {q.get('bloom_name')}]*")


# ==============================================================================
# TAB 3: STUDENT ASSESSMENT AGENT
# ==============================================================================
with tab_assess:
    st.subheader("Student Answer Grading & Partial Marks Agent")
    st.write("Evaluate student answer submissions against step-wise rubrics.")

    q_text = st.text_input("Question:", value="Differentiate between Chubby and ZooKeeper consensus implementations.")
    m_marks = st.number_input("Max Marks:", value=10)
    m_ans = st.text_area("Model Answer:", value="Chubby uses Paxos for coarse-grained locks. ZooKeeper uses ZAB for fine-grained high-throughput updates.")
    std_ans = st.text_area("Student Answer:", value="Chubby is for coarse-grained locks like master election. ZooKeeper uses ZAB protocol with an in-memory tree for fast updates.")

    if st.button("⚖️ Grade Submission with Rubric Agent", type="primary"):
        with st.spinner("Grading..."):
            agent = AssessmentAgent(st.session_state.cloud_client)
            eval_res = agent.evaluate_submission(
                question_text=q_text,
                bloom_level="L4",
                maximum_marks=float(m_marks),
                model_answer=m_ans,
                rubric=[{"criterion": "Key comparison", "marks": m_marks}],
                student_answer=std_ans
            )
            st.success(f"Score Awarded: {eval_res.get('score_awarded')} / {m_marks}")
            st.info(f"Feedback: {eval_res.get('overall_feedback')}")


# ==============================================================================
# TAB 4: CLOUD DEPLOYMENT
# ==============================================================================
with tab_cloud:
    st.subheader("☁️ Google Cloud Platform Deployment")
    st.markdown("""
    - **Google Cloud Run:** Hosts the web app container with auto-scaling to 0.
    - **Vertex AI / Gemini API:** Powering Bloom taxonomy classification and canonical answer key generation.
    - **1-Click Scripts:** `deploy_gcp.ps1` (Windows) and `deploy_gcp.sh` (Linux/Mac).
    """)
