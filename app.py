import os
import pandas as pd
import streamlit as st
from datetime import datetime

from src.storage import (
    load_student_data,
    save_student_data,
    verify_user,
    register_user
)
from src.utils import calculate_readiness_score, get_gemini_api_key, call_gemini
from src.academic_analysis import categorize_subject, parse_transcript_text, generate_academic_improvement_plan
from src.career_analysis import generate_career_recommendations
from src.roadmap import generate_adaptive_roadmap
from src.progress_tracker import evaluate_progress_update
from src.achievements import detect_automatic_milestones
from src.rag import index_course_catalog, ask_catalog_rag, extract_pdf_text, retrieve_courses
from src.report_generator import generate_progress_report_pdf, generate_career_portfolio_pdf

st.set_page_config(
    page_title="EduPath AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------- SESSION STATE & AUTHENTICATION GATE -----------------
if "authenticated_student" not in st.session_state:
    st.session_state.authenticated_student = None

if not st.session_state.authenticated_student:
    # Custom CSS to style inputs, buttons, and container cards
    st.markdown("""
        <style>
        /* Form card styling */
        div[data-testid="stVerticalBlock"] > div:has(div.auth-card) {
            background: #FFFFFF;
            padding: 2.5rem 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 24px rgba(13, 31, 60, 0.08);
        }
        /* Primary button styling */
        button[kind="primary"] {
            background-color: #E65100 !important;
            border-color: #E65100 !important;
            color: #FFFFFF !important;
            font-weight: 600;
            border-radius: 8px;
            padding: 0.6rem 1rem;
            margin-top: 1rem;
        }
        button[kind="primary"]:hover {
            background-color: #CF4400 !important;
            border-color: #CF4400 !important;
        }
        /* Custom input border styling */
        div[data-baseweb="input"] {
            border-radius: 8px;
            border: 1px solid #D0D5DD;
        }
        div[data-baseweb="input"]:focus-within {
            border-color: #E65100 !important;
            box-shadow: 0 0 0 1px #E65100 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    col_brand, col_form = st.columns([1.2, 1], gap="large")

    with col_brand:
        st.markdown("""
            <div style="background-color: #0D1F3C; color: #FFFFFF; padding: 3.5rem 2.5rem; border-radius: 16px; min-height: 520px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <span style="font-weight: 800; font-size: 1.1rem; letter-spacing: 0.5px;">EDUPATH AI</span>
                    <div style="margin-top: 2rem;">
                        <span style="font-size: 0.95rem; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; color: #E65100; border-bottom: 2px solid #E65100; padding-bottom: 4px;">Student Portal</span>
                    </div>
                    <h1 style="font-size: 2.2rem; font-weight: 700; line-height: 1.25; margin-top: 1.5rem; color: #FFFFFF;">Manage your academic roadmap in one place</h1>
                    <p style="color: #94A3B8; font-size: 1rem; line-height: 1.6; margin-top: 1.2rem;">
                        Track transcripts, explore validated career paths, evaluate course requirements, and maintain verified achievement credentials securely.
                    </p>
                </div>
                <div style="display: flex; align-items: center; gap: 12px; margin-top: 2rem;">
                    <div style="width: 10px; height: 10px; border-radius: 50%; background: #E65100;"></div>
                    <div>
                        <div style="font-size: 0.85rem; font-weight: 600; color: #FFFFFF;">Real-time Progression Audits</div>
                        <div style="font-size: 0.75rem; color: #94A3B8;">Private record isolation for every enrolled student</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col_form:
        st.markdown('<div class="auth-card"></div>', unsafe_allow_html=True)
        st.markdown("<h2 style='font-size: 1.8rem; font-weight: 700; color: #101828; margin-bottom: 4px;'>Sign in to EduPath AI</h2>", unsafe_allow_html=True)
        st.caption("Enter your credentials to access your student records")

        tab_login, tab_register = st.tabs(["Sign In", "Create Account"])

        with tab_login:
            with st.form("login_form"):
                login_id = st.text_input("Student Workspace ID", placeholder="e.g. std_101")
                login_pin = st.text_input("Passcode / PIN", type="password", placeholder="Enter your secret passcode")
                
                submitted_login = st.form_submit_button("Sign In", type="primary", use_container_width=True)
                if submitted_login:
                    if verify_user(login_id, login_pin):
                        st.session_state.authenticated_student = login_id.strip().lower()
                        st.session_state.chat_history = []
                        st.rerun()
                    else:
                        st.error("Invalid Workspace ID or Passcode.")

        with tab_register:
            with st.form("register_form"):
                reg_id = st.text_input("Choose Student ID", placeholder="e.g. std_101")
                reg_name = st.text_input("Full Name", placeholder="e.g. Jane Doe")
                reg_pin = st.text_input("Create Passcode / PIN", type="password", placeholder="Choose a secure PIN")
                
                submitted_reg = st.form_submit_button("Create Student Record", type="primary", use_container_width=True)
                if submitted_reg:
                    if not reg_id.strip() or not reg_pin.strip():
                        st.error("Both ID and Passcode are required.")
                    elif register_user(reg_id, reg_pin):
                        clean_id = "".join([c for c in reg_id.strip().lower() if c.isalnum() or c in ("_", "-")])
                        fresh_data = load_student_data(clean_id)
                        fresh_data["profile"]["name"] = reg_name.strip()
                        save_student_data(clean_id, fresh_data)
                        st.session_state.authenticated_student = clean_id
                        st.session_state.chat_history = []
                        st.rerun()
                    else:
                        st.error("Student ID already exists.")

    st.stop()

# Logged-in user context
student_id = st.session_state.authenticated_student
student_data = load_student_data(student_id)

# ----------------- AUTHENTICATED SIDEBAR -----------------
st.sidebar.title("🎓 EduPath AI")
st.sidebar.caption(f"Active Account: **{student_id}**")

if st.sidebar.button("🚪 Log Out", use_container_width=True):
    st.session_state.authenticated_student = None
    st.session_state.chat_history = []
    st.rerun()

st.sidebar.markdown("---")
page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "👤 My Profile",
        "📚 Academic Analysis",
        "🧭 Career Paths",
        "🗺️ My Roadmap",
        "📈 Progress Tracker",
        "🏆 Achievements",
        "🎯 Opportunities",
        "📄 Reports"
    ]
)

st.sidebar.markdown("---")
gemini_key = get_gemini_api_key()
if not gemini_key:
    st.sidebar.warning("⚠️ Gemini API Key not detected. Configure `.streamlit/secrets.toml`.")
else:
    st.sidebar.success("⚡ Gemini Connected")

# =====================================================================
# 1. DASHBOARD
# =====================================================================
if page == "🏠 Dashboard":
    profile = student_data.get("profile", {}) or {}
    history = student_data.get("assessment_history", []) or []
    baseline = student_data.get("baseline_assessment") or {}
    
    current_assessment = (history[-1] if history else baseline) or {}
    prev_assessment = (history[-2] if len(history) >= 2 else current_assessment) or {}

    st.title(f"Welcome Back, {profile.get('name') or student_id} 👋")
    st.caption(f"{profile.get('degree', 'Undergraduate')} in {profile.get('field', 'Academic Studies')} • {profile.get('university', 'University')}")

    # Prompt user if brand-new unassessed student
    if not current_assessment:
        st.info("👋 Welcome! You have not generated your initial Career Readiness Assessment yet. You can initialize your baseline below, or complete **👤 My Profile** first.")
        if st.button("🚀 Generate Initial Baseline Assessment", type="primary"):
            with st.spinner("Calculating initial readiness score..."):
                initial_audit = evaluate_progress_update(student_data, {})
                student_data["baseline_assessment"] = initial_audit
                student_data.setdefault("assessment_history", []).append(initial_audit)
                save_student_data(student_id, student_data)
                st.success("Initial baseline assessment established!")
                st.rerun()

    curr_score = current_assessment.get("overall_score", 0)
    prev_score = prev_assessment.get("overall_score", 0)
    score_diff = curr_score - prev_score

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Career Readiness Index", f"{curr_score} / 100", delta=f"{score_diff} pts" if (score_diff != 0 and history) else None)
    with col2:
        st.metric("Target Career Goal", profile.get("preferred_career") or "Undecided")
    with col3:
        st.metric("Current Stage", f"{profile.get('current_year', 'Year 1')} ({profile.get('current_semester', 'Sem 1')})")

    st.markdown("### 📊 Readiness Breakdown")
    cat_scores = current_assessment.get("category_scores", {}) or {}
    b1, b2, b3, b4 = st.columns(4)
    b1.progress(min(max(float(cat_scores.get("academic", 0)) / 100.0, 0.0), 1.0), text=f"Academic: {cat_scores.get('academic', 0)}%")
    b2.progress(min(max(float(cat_scores.get("skills", 0)) / 100.0, 0.0), 1.0), text=f"Skills: {cat_scores.get('skills', 0)}%")
    b3.progress(min(max(float(cat_scores.get("projects", 0)) / 100.0, 0.0), 1.0), text=f"Projects: {cat_scores.get('projects', 0)}%")
    b4.progress(min(max(float(cat_scores.get("experience", 0)) / 100.0, 0.0), 1.0), text=f"Experience: {cat_scores.get('experience', 0)}%")

    st.markdown("---")
    left_col, right_col = st.columns([3, 2])
    with left_col:
        st.subheader("🔥 Current Strategic Priorities")
        recs = current_assessment.get("ai_recommendations", []) or []
        if recs:
            for r in recs:
                st.info(f"**Action:** {r}")
        else:
            st.write("Complete your initial baseline assessment to unlock personalized priorities.")

        st.subheader("🎉 Recent AI Milestones")
        milestones = detect_automatic_milestones(student_data)
        if milestones:
            for m in milestones:
                st.success(m)
        else:
            st.caption("No automatic milestones unlocked yet. Record projects and activities to trigger badges.")

        # =================================================================
        # CHAT ASSISTANT
        # =================================================================
        st.markdown("---")
        st.subheader("💬 EduPath AI Assistant")
        st.caption("Ask general career/academic questions, or ask about your transcript, skills, and university catalog.")

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        chat_container = st.container(height=320)
        with chat_container:
            if not st.session_state.chat_history:
                st.info("👋 Ask anything! E.g., *'What should I prioritize next?'*, *'What grades did I get in my courses?'*, or *'What electives align with my career?'*")
            for msg in st.session_state.chat_history:
                with st.chat_message(msg["role"]):
                    st.markdown(msg["content"])

        user_chat_input = st.chat_input("Ask EduPath AI a question...")
        if user_chat_input:
            st.session_state.chat_history.append({"role": "user", "content": user_chat_input})

            # 1. Retrieve RAG context from ChromaDB if available
            rag_docs = retrieve_courses(user_chat_input, n_results=3)
            rag_context = "\n---\n".join([d["content"] for d in rag_docs]) if rag_docs else "No university handbook uploaded yet."

            # 2. Extract full academic coursework & letter grades summary
            academic_records_summary = []
            for r in (student_data.get("academic_records", []) or []):
                sem_label = r.get("semester", "Semester")
                gpa = r.get("gpa", "N/A")
                subj_list = []
                for s in r.get("subjects", []):
                    s_name = s.get("name", "Unknown Subject")
                    s_marks = s.get("marks", "N/A")
                    s_grade = s.get("grade", "N/A")
                    s_status = s.get("status", "Average")
                    subj_list.append(f"{s_name} (Grade: {s_grade}, Marks: {s_marks}, Status: {s_status})")
                
                academic_records_summary.append(f"[{sem_label} | GPA: {gpa}]: " + "; ".join(subj_list))

            full_academic_context = "\n".join(academic_records_summary) if academic_records_summary else "No committed transcript records found."

            skills_summary = ", ".join([s.get("name", "") for s in (student_data.get("skills", []) or [])]) or "None recorded"
            opp_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "opportunities.csv")
            opp_context = ""
            if os.path.exists(opp_path):
                try:
                    df_temp = pd.read_csv(opp_path)
                    opp_context = "\n".join([f"- {row['title']} ({row['type']}): {row['url']}" for _, row in df_temp.head(8).iterrows()])
                except Exception:
                    opp_context = ""

            # 3. Construct System Prompt with Guardrails
            advisor_system_prompt = f"""
You are the dedicated Academic & Career Companion inside EduPath AI.
You answer both general career/study questions and hyper-personalized questions based on committed records.

Student Context:
- Name: {profile.get('name', 'Student')}
- Field: {profile.get('field', 'General')} ({profile.get('current_year', 'Year 1')}, {profile.get('current_semester', 'Semester 1')})
- Degree: {profile.get('degree', 'N/A')}
- Target Career: {profile.get('preferred_career', 'Undecided')}
- Readiness Score: {curr_score}/100
- Academic Coursework & Letter Grades:
{full_academic_context}
- Known Skills: {skills_summary}

University Handbook / Catalog Excerpts (RAG Context):
{rag_context}

Verified External Opportunities & Portals:
{opp_context}

Rules:
1. When asked about specific coursework grades, scores, or performance, reference the exact grades and marks provided in the Academic Coursework context.
2. If the student asks about university curriculum rules, degree requirements, or course codes, rely strictly on the Handbook Excerpts. If absent, explicitly state: "Your uploaded university handbook does not contain details on this; please verify with your department."
3. Never invent fake URLs or example domains. When recommending hackathons or competitions, refer only to verified platforms (e.g. Lablab.ai at https://lablab.ai/ai-hackathons or Devpost at https://devpost.com/hackathons).
4. For general questions, provide actionable, structured, and realistic advice.
"""
            with st.spinner("EduPath AI is thinking..."):
                bot_reply = call_gemini(user_chat_input, system_instruction=advisor_system_prompt)

            st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
            st.rerun()

    with right_col:
        st.subheader("🏆 Recent Achievements")
        achs = student_data.get("achievements", []) or []
        if achs:
            for a in achs[-3:]:
                st.markdown(f"**{a.get('title')}**  \n*{a.get('organization')} — {a.get('date')}*")
        else:
            st.caption("No achievements logged yet.")

        st.markdown("---")
        st.write("**Next Suggested Review:** Within 60 to 90 days.")
        pdf_data = generate_progress_report_pdf(student_data)
        st.download_button(
            label="📄 Download Official Progress PDF",
            data=pdf_data,
            file_name=f"{student_id}_career_progress.pdf",
            mime="application/pdf",
            use_container_width=True
        )

# =====================================================================
# 2. MY PROFILE
# =====================================================================
elif page == "👤 My Profile":
    st.title("👤 Student Profile & Academic Background")
    p = student_data.get("profile", {}) or {}

    with st.form("profile_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name", value=p.get("name", ""))
            edu_level = st.selectbox("Education Level", ["Undergraduate", "Graduate", "Doctoral"], index=0)
            university = st.text_input("University / College", value=p.get("university", ""))
            degree = st.text_input("Degree / Major Program", value=p.get("degree", ""))
            field = st.text_input("Field of Study (Generic)", value=p.get("field", "Computer Science"))
        with col2:
            current_year = st.selectbox("Current Year", ["Year 1", "Year 2", "Year 3", "Year 4", "Post-Grad"], index=2)
            current_semester = st.selectbox("Current Semester", [f"Semester {i}" for i in range(1, 9)], index=4)
            preferred_career = st.text_input("Preferred Career Path", value=p.get("preferred_career", ""))
            interests_raw = st.text_area("Key Academic & Professional Interests (comma separated)", value=", ".join(p.get("interests", [])))
            weak_raw = st.text_area("Perceived Weak Academic Subjects / Skills (comma separated)", value=", ".join(p.get("weak_areas", [])))

        career_goals = st.text_area("Comprehensive Career Objectives", value=p.get("career_goals", ""))
        submit_profile = st.form_submit_button("💾 Save Profile Details")

    if submit_profile:
        student_data.setdefault("profile", {}).update({
            "name": name,
            "education_level": edu_level,
            "university": university,
            "degree": degree,
            "field": field,
            "current_year": current_year,
            "current_semester": current_semester,
            "preferred_career": preferred_career,
            "interests": [x.strip() for x in interests_raw.split(",") if x.strip()],
            "weak_areas": [x.strip() for x in weak_raw.split(",") if x.strip()],
            "career_goals": career_goals
        })
        save_student_data(student_id, student_data)
        st.success("Profile saved successfully!")

    st.markdown("---")
    st.subheader("📑 University Course Catalog Knowledge Base (RAG)")
    st.write("Upload your official university syllabus, course catalog, or degree handbook PDF to enrich course recommendations.")
    uploaded_catalog = st.file_uploader("Upload Course Catalog (PDF)", type=["pdf"], key="catalog_pdf")
    if uploaded_catalog and st.button("Index University Handbook"):
        with st.spinner("Extracting and vectorizing catalog..."):
            chunks_indexed = index_course_catalog(uploaded_catalog.getvalue())
            if chunks_indexed > 0:
                st.success(f"Indexed {chunks_indexed} catalog sections into ChromaDB!")
            else:
                st.error("Failed to parse catalog PDF. Ensure the file contains selectable text.")

# =====================================================================
# 3. ACADEMIC ANALYSIS
# =====================================================================
elif page == "📚 Academic Analysis":
    st.title("📚 Academic Analysis & Transcript Parsing")
    tab1, tab2 = st.tabs(["📄 Transcript Extractor & Results", "💡 Academic Remediation Plan"])

    with tab1:
        st.write("Upload a semester result PDF or manually review extracted subject scores.")
        uploaded_transcript = st.file_uploader("Upload Academic Transcript / Result PDF", type=["pdf"])
        if uploaded_transcript and st.button("Parse Transcript with Gemini"):
            with st.spinner("Extracting coursework text and analyzing scores..."):
                raw_txt = extract_pdf_text(uploaded_transcript.getvalue())
                extracted_subjects = parse_transcript_text(raw_txt)
                if extracted_subjects:
                    st.session_state.temp_extracted_subjects = extracted_subjects
                    st.success(f"Successfully extracted {len(extracted_subjects)} subjects!")
                else:
                    st.error("Could not parse structured subjects. Please use the manual table below.")

        records = student_data.get("academic_records", []) or []
        current_subjects = records[-1].get("subjects", []) if records else []
        if "temp_extracted_subjects" in st.session_state:
            current_subjects = st.session_state.temp_extracted_subjects

        st.subheader("Active Coursework Record")
        df_subjects = pd.DataFrame(current_subjects) if current_subjects else pd.DataFrame(columns=["name", "marks", "grade", "status"])
        edited_df = st.data_editor(df_subjects, num_rows="dynamic", use_container_width=True)

        col_a, col_b = st.columns(2)
        with col_a:
            sem_name = st.text_input("Semester Name / Term", value="Semester 5")
        with col_b:
            sem_gpa = st.text_input("Calculated Semester GPA", value="3.70")

        if st.button("💾 Commit Academic Record to Profile"):
            parsed_list = edited_df.to_dict(orient="records")
            for item in parsed_list:
                try:
                    m = float(item.get("marks", 70))
                    item["status"] = categorize_subject(m)
                except Exception:
                    item["status"] = "Average"

            new_record = {
                "semester": sem_name,
                "gpa": sem_gpa,
                "subjects": parsed_list
            }
            student_data.setdefault("academic_records", []).append(new_record)
            save_student_data(student_id, student_data)
            st.success("Semester academic performance committed!")

    with tab2:
        st.subheader("Targeted Subject Improvement Plan")
        weak_subs = []
        for r in (student_data.get("academic_records", []) or []):
            for s in r.get("subjects", []):
                if s.get("status") == "Weak":
                    weak_subs.append(s.get("name"))
        weak_subs = list(set(weak_subs))

        if weak_subs:
            st.warning(f"Identified Weak Subjects: {', '.join(weak_subs)}")
            if st.button("Generate Remediation Strategies"):
                with st.spinner("Synthesizing learning targets and practice schedules..."):
                    plan = generate_academic_improvement_plan(
                        weak_subs,
                        student_data.get("profile", {}).get("preferred_career", "Domain Specialist"),
                        student_data.get("profile", {}).get("field", "General")
                    )
                    st.markdown(plan)
        else:
            st.info("No weak subjects flagged. Excellent work maintaining consistent academic standing!")

# =====================================================================
# 4. CAREER PATHS
# =====================================================================
elif page == "🧭 Career Paths":
    st.title("🧭 Evidence-Based Career Exploration")
    st.caption("Synthesizing academic transcript metrics, domain interests, and existing project capabilities.")

    catalog_context = ask_catalog_rag("What are recommended upper-level elective courses for career readiness?")

    if st.button("🔄 Synthesize Career Recommendations", type="primary"):
        with st.spinner("Querying Gemini with student portfolio metrics..."):
            recommendations = generate_career_recommendations(student_data, catalog_context)
            st.session_state.career_recs = recommendations

    recs = st.session_state.get("career_recs")
    if recs:
        primary = recs.get("primary_recommendation", {}) or {}
        st.subheader(f"⭐ Primary Match: {primary.get('career_name', 'Recommended Role')}")
        st.write(f"**Alignment Index:** {primary.get('match_level', 'High')}")
        st.write(primary.get("match_explanation", ""))

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Required Core Competencies:**")
            for req in primary.get("required_skills", []):
                st.write(f"• {req}")
        with c2:
            st.markdown("**Identified Gaps to Close:**")
            for gap in primary.get("current_skill_gaps", []):
                st.write(f"⚠️ {gap}")

        st.info(f"**Market Context & Risk Analysis:** {primary.get('potential_risks_and_considerations', 'Evolving industry demands continuous skill validation.')}")

        st.markdown("### 🔄 Alternative Viable Pathways")
        for alt in recs.get("alternative_recommendations", []):
            with st.expander(f"Pathway: {alt.get('career_name')} ({alt.get('match_level')} Match)"):
                st.write(alt.get("match_explanation", ""))
                st.write(f"**Key Skills Needed:** {', '.join(alt.get('required_skills', []))}")
                st.write(f"**Identified Gaps:** {', '.join(alt.get('current_skill_gaps', []))}")

        st.success(f"**Transferable Strengths:** {recs.get('transferable_strengths_summary', 'Strong baseline foundations.')}")
    else:
        st.info("Click 'Synthesize Career Recommendations' to generate your personalized career analysis.")

# =====================================================================
# 5. MY ROADMAP
# =====================================================================
elif page == "🗺️ My Roadmap":
    st.title("🗺️ Personalized 4-Year Adaptive Roadmap")
    st.caption("Field-generic multi-stage milestones configured to your academic domain.")

    if st.button("🔄 Generate / Adapt Roadmap with AI"):
        with st.spinner("Constructing progressive university milestone stages..."):
            updated_roadmap = generate_adaptive_roadmap(student_data)
            student_data["roadmap"] = updated_roadmap
            save_student_data(student_id, student_data)
            st.success("Adaptive roadmap successfully synchronized!")

    roadmap = student_data.get("roadmap", {}) or {}
    for year_key in ["year_1", "year_2", "year_3", "year_4"]:
        y_info = roadmap.get(year_key, {}) or {}
        with st.expander(f"📌 {y_info.get('title', year_key.upper())}", expanded=True):
            tasks = y_info.get("tasks", []) or []
            for idx, t in enumerate(tasks):
                col_status, col_desc = st.columns([1, 4])
                with col_status:
                    current_status = t.get("status", "Not Started")
                    status_opts = ["Not Started", "In Progress", "Completed"]
                    sel_idx = status_opts.index(current_status) if current_status in status_opts else 0
                    new_status = st.selectbox(
                        "Status",
                        status_opts,
                        index=sel_idx,
                        key=f"{year_key}_{idx}"
                    )
                    t["status"] = new_status
                with col_desc:
                    st.write(f"**{t.get('task')}**")

    if st.button("💾 Save Roadmap Status Updates"):
        save_student_data(student_id, student_data)
        st.success("Roadmap progress committed to student record!")

# =====================================================================
# 6. PROGRESS TRACKER
# =====================================================================
elif page == "📈 Progress Tracker":
    st.title("📈 Longitudinal Progress & Readiness Tracking")
    st.caption("Record periodic updates. Previous milestones are preserved and evaluated historically.")

    history = student_data.get("assessment_history", []) or []
    if history:
        dates = [h.get("date") for h in history]
        scores = [h.get("overall_score") for h in history]
        df_chart = pd.DataFrame({"Assessment Date": dates, "Readiness Score": scores})
        st.line_chart(df_chart.set_index("Assessment Date"))

    st.markdown("---")
    st.subheader("📝 Update My Current Progress")

    with st.expander("➕ Add / Update Technical & Professional Skills", expanded=False):
        skills_df = pd.DataFrame(student_data.get("skills", []) or [])
        if skills_df.empty:
            skills_df = pd.DataFrame(columns=["id", "name", "level", "target_level"])
        edited_skills = st.data_editor(skills_df, num_rows="dynamic", use_container_width=True, key="skills_ed")
        if st.button("Save Skills Matrix"):
            student_data["skills"] = edited_skills.to_dict(orient="records")
            save_student_data(student_id, student_data)
            st.success("Skills matrix updated!")

    with st.expander("➕ Log New Project Work", expanded=False):
        with st.form("new_project_form"):
            p_title = st.text_input("Project Name")
            p_desc = st.text_area("Project Overview & Deliverables")
            p_tech = st.text_input("Key Technologies / Methods (comma separated)")
            p_status = st.selectbox("Current Status", ["In Progress", "Completed", "Not Started"])
            p_url = st.text_input("Repository / Portfolio Link")
            submit_proj = st.form_submit_button("Add Project")
            if submit_proj and p_title:
                new_proj = {
                    "id": f"proj_{len(student_data.get('projects', []) or []) + 1}",
                    "title": p_title,
                    "description": p_desc,
                    "technologies": [x.strip() for x in p_tech.split(",") if x.strip()],
                    "status": p_status,
                    "completion_date": datetime.now().strftime("%Y-%m-%d") if p_status == "Completed" else "",
                    "github_url": p_url
                }
                student_data.setdefault("projects", []).append(new_proj)
                save_student_data(student_id, student_data)
                st.success("Project added successfully!")

    with st.expander("➕ Log Work Experience / Internships", expanded=False):
        with st.form("new_exp_form"):
            e_role = st.text_input("Role / Title")
            e_org = st.text_input("Organization / Laboratory")
            e_type = st.selectbox("Type", ["Internship", "Research", "Freelance", "Volunteer", "Part-time work"])
            e_desc = st.text_area("Responsibilities & Impact")
            submit_exp = st.form_submit_button("Add Experience")
            if submit_exp and e_role:
                new_exp = {
                    "id": f"exp_{len(student_data.get('experience', []) or []) + 1}",
                    "role": e_role,
                    "organization": e_org,
                    "type": e_type,
                    "description": e_desc,
                    "date": datetime.now().strftime("%Y-%m-%d")
                }
                student_data.setdefault("experience", []).append(new_exp)
                save_student_data(student_id, student_data)
                st.success("Experience record committed!")

    st.markdown("---")
    if st.button("🚀 Re-Evaluate Career Readiness & Compare with Baseline", type="primary"):
        with st.spinner("Auditing progress metrics and running delta comparison..."):
            prev_assessment = (history[-1] if history else student_data.get("baseline_assessment")) or {}
            new_audit = evaluate_progress_update(student_data, prev_assessment)
            
            if not student_data.get("baseline_assessment"):
                student_data["baseline_assessment"] = new_audit
                
            student_data.setdefault("assessment_history", []).append(new_audit)
            save_student_data(student_id, student_data)
            st.success(f"Audit Complete! New Readiness Score: {new_audit['overall_score']} / 100")
            st.rerun()

# =====================================================================
# 7. ACHIEVEMENTS
# =====================================================================
elif page == "🏆 Achievements":
    st.title("🏆 Student Achievements & Verified Honors")
    st.caption("Maintain a permanent record of awards, honors, certifications, and competition wins.")

    with st.expander("➕ Record New Achievement", expanded=True):
        with st.form("ach_form"):
            a_title = st.text_input("Achievement Title (e.g. 1st Place Datathon Winner)")
            a_type = st.selectbox("Type", ["Competition Winner", "Hackathon Finalist", "Certification", "Internship Completed", "Research Publication", "Scholarship", "Leadership Role"])
            a_org = st.text_input("Issuing Institution / Organization")
            a_date = st.date_input("Date Achieved", value=datetime.today())
            a_desc = st.text_area("Detailed Overview & Accomplishments")
            a_url = st.text_input("Credential or Project Link")
            submit_ach = st.form_submit_button("Log Official Achievement")

        if submit_ach and a_title:
            ach_item = {
                "id": f"ach_{len(student_data.get('achievements', []) or []) + 1}",
                "title": a_title,
                "type": a_type,
                "organization": a_org,
                "date": a_date.strftime("%Y-%m-%d"),
                "description": a_desc,
                "url": a_url
            }
            student_data.setdefault("achievements", []).append(ach_item)
            save_student_data(student_id, student_data)
            st.success("Achievement saved!")

    st.subheader("Verified Ledger")
    achs = student_data.get("achievements", []) or []
    if achs:
        for a in reversed(achs):
            st.markdown(f"""
            #### 🎖️ {a.get('title')}
            **{a.get('organization')}** • *{a.get('date')}*  
            {a.get('description')}  
            [Credential Link]({a.get('url', '#')})
            ---
            """)
    else:
        st.info("No recorded achievements yet.")

# =====================================================================
# 8. OPPORTUNITIES
# =====================================================================
elif page == "🎯 Opportunities":
    st.title("🎯 Curated Opportunities & External Programs")
    st.caption("Hackathons, internships, fellowships, and conferences aligned with your academic field.")

    opp_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "opportunities.csv")
    if os.path.exists(opp_file):
        df_opps = pd.read_csv(opp_file)
        
        filter_field = st.selectbox("Filter by Academic Discipline", ["All"] + list(df_opps["field"].unique()))
        display_df = df_opps if filter_field == "All" else df_opps[df_opps["field"] == filter_field]

        for _, row in display_df.iterrows():
            with st.container():
                st.markdown(f"### {row['title']} ({row['type']})")
                st.write(f"**Organization:** {row['organization']} | **Location:** {row['location']} | **Deadline:** {row['deadline']}")
                st.write(row["description"])
                st.caption(f"**Eligibility:** {row['eligibility']} | **Skills:** {row['skills']}")
                st.markdown(f"[Apply / View Official Page]({row['url']})")
                st.markdown("---")
    else:
        st.warning("Opportunities database (data/opportunities.csv) not found.")

# =====================================================================
# 9. REPORTS
# =====================================================================
elif page == "📄 Reports":
    st.title("📄 Publication-Grade PDF Reports")
    st.caption("Generate verifiable multi-page career readiness audits and student portfolio documents.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Comprehensive Career Progress Report")
        st.write("Contains full historical assessment deltas, category matrix, academic trajectories, and AI action directives.")
        progress_pdf = generate_progress_report_pdf(student_data)
        st.download_button(
            label="📥 Download Progress Audit PDF",
            data=progress_pdf,
            file_name=f"{student_id}_career_progress_audit.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    with col2:
        st.subheader("Student Career Portfolio")
        st.write("Tailored summary of skills, completed projects, verified achievements, and career objective statements.")
        portfolio_pdf = generate_career_portfolio_pdf(student_data)
        st.download_button(
            label="📥 Download Career Portfolio PDF",
            data=portfolio_pdf,
            file_name=f"{student_id}_career_portfolio.pdf",
            mime="application/pdf",
            use_container_width=True
        )