@'
<div align="center">

# 🎓 EduPath AI

### Privacy-First Academic Companion & Longitudinal Career Navigator

**Transforming raw academic transcripts and university syllabi into grounded four-year roadmaps and verifiable career readiness.**

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-ff4b4b?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Google Gemini](https://img.shields.io/badge/Google_Gemini-API-orange?style=for-the-badge&logo=google)](https://ai.google.dev/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_RAG-blueviolet?style=for-the-badge)](https://www.trychroma.com/)
[![ReportLab](https://img.shields.io/badge/ReportLab-PDF_Audits-red?style=for-the-badge)](https://www.reportlab.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<br>

### 🚀 Live Demo

**[Launch EduPath AI](https://edupath-ai-companion.streamlit.app/)**

</div>

---

# 📌 Overview

**EduPath AI** is an intelligent, privacy-focused academic and career companion engineered to bridge the disconnect between university course enrollments, dense degree catalogs, and real-world employment readiness.

Instead of generic career prompts, EduPath AI ingests verified student performance data, leverages **Retrieval-Augmented Generation (RAG)** over official institutional handbooks, and tracks longitudinal progress against an immutable day-one baseline.

Instead of asking broad questions with hallucinated answers, EduPath AI addresses a concrete problem:

> **How can a student navigate their institutional curriculum without hallucinations, remediate weak subjects, and tangibly measure four-year career readiness while maintaining strict data privacy?**

EduPath AI combines:

- 📄 Automatic transcript & coursework parsing
- 📑 Course catalog ingestion via ChromaDB vector search (RAG)
- 📊 Balanced 100-point career readiness scoring
- 💡 Targeted academic remediation workflows
- 🗺️ Adaptive 4-year dynamic roadmapping
- 💬 Grade-aware AI advisory chat companion
- 🎯 Curated and verified global opportunity tracking
- 🏆 Rule-based milestone badge progression
- 📄 Automated publication-grade PDF audit generation

---

# 🎯 Problem Statement

Higher education advising is often fragmented, reactive, and disconnected from dynamic industry benchmarks:

- **Syllabus Disconnect:** Institutional handbooks and course prerequisites are buried in multi-page static PDFs that students rarely consult.
- **Generic LLM Hallucinations:** Off-the-shelf AI models frequently fabricate university degree requirements, incorrect course codes, and dead application links.
- **Lack of Longitudinal Tracking:** Students lack a quantitative metric to measure how semester coursework, technical skills, and projects compound over time toward target careers.
- **Privacy & Security Risks:** Existing online portfolio tools frequently compromise sensitive academic records, exposing transcripts and personal data on shared cloud databases.

EduPath AI resolves this gap by providing an isolated, RAG-grounded decision engine that stays faithful to official institutional curricula while enforcing session-level security.

---

# 💡 Our Solution

EduPath AI unifies multimodal parsing, local vector retrieval, and Large Language Model reasoning into a structured, privacy-preserving workflow:

```text
Academic Transcript (PDF)       Course Catalog Handbook (PDF)
            │                                 │
            ▼                                 ▼
   Text Extraction Layer             ChromaDB Vector Store
            │                                 │
            ▼                                 ▼
 Coursework Analytics Engine             Semantic RAG
            │                                 │
            ├─────────────────────────────────┤
            │
            ▼
 Balanced Readiness Engine (100-Point Audit)
            │
      ┌─────┴────────────────┐
      ▼                      ▼
Dynamic 4-Year         Grade-Aware AI
   Roadmap            Advisory Companion
      │                      │
      └─────┬────────────────┘
            │
            ▼
 Publication-Grade PDF Progress Audits
 The system evaluates student progress across four balanced pillars:

Academic Standing (GPA/Grades) + Skills Matrix + Practical Projects + Experience/Internships

This shifts academic guidance from:

"What electives should I take?"

to:

"Based on your performance in prerequisite courses and the institutional handbook, here are the electives that bridge your skill gap for your target career—and here is your projected readiness index delta."

✨ Key Features
📄 1. Transcript Analytics & Grading Breakdown
Ingests semester result documents and extracts course titles, numerical marks, and letter grades.

Automatically categorizes academic performance into Strong, Average, and Weak subjects.

Flags academic blind spots before they cascade into downstream course failures.

💡 2. Targeted Academic Remediation
Generates tailored recovery strategies for subjects flagged as weak.

Formulates weekly conceptual revision schedules, concrete learning targets, and targeted practice problems tied directly to the student's target career goals.

📑 3. Grounded Catalog Knowledge Base (RAG)
Vectorizes official university handbooks, degree syllabi, and faculty catalogs using ChromaDB.

Performs semantic search over program requirements and prerequisite chains.

Includes a strict guardrail: if a course rule or prerequisite is not present in the uploaded catalog, the model states so directly instead of hallucinating answers.

📊 4. Quantitative 100-Point Readiness Engine
Benchmarks student progress against an immutable day-one baseline across four dimensions:

Academic Foundation: Coursework performance and overall GPA consistency.

Technical & Professional Skills: Validated competencies and tool proficiencies.

Portfolio Deliverables: Real-world projects, repository links, and production deployments.

Practical Experience: Internships, fellowships, and academic research.

Displays longitudinal trendlines to visualize continuous progress over semesters.

🗺️ 5. Dynamic 4-Year Adaptive Roadmap
Generates field-specific multi-stage milestones across Year 1 through Year 4.

Features interactive progress toggles (Not Started, In Progress, Completed) that directly update student progress ledgers and readiness scores.

💬 6. Grade-Aware AI Advisory Companion
Context-aware conversational assistant grounded in the student's real coursework marks, declared interests, and RAG catalog excerpts.

Powered by Google Gemini with dynamic multi-model fallback and exponential backoff retry handling.

🎯 7. Verified Opportunities Ledger
Surfaces verified internships, hackathons (Devpost, Lablab.ai), fellowships, and global competitions.

Filterable by academic discipline to eliminate dead ends and fake application portals.

📄 8. Automated PDF Audit & Portfolio Generation
Programmatically compiles two publication-grade PDF documents via ReportLab:

Comprehensive Career Progress Audit: Detailed metric analysis, category scores, historical deltas, and strategic directives.

Student Career Portfolio: Clean, professional CV-ready summary of skills, completed projects, verified achievements, and career goals.

🧠 Scoring & Readiness Architecture
EduPath AI calculates progress using a weighted, normalized multi-variable matrix:
Readiness Score = (Academic Metric   × 0.30)
                + (Skills Matrix     × 0.25)
                + (Project Portfolio × 0.25)
                + (Field Experience  × 0.20)
Audit Pipeline
Committed Student Records
                           │
                           ▼
                  Multi-Pillar Scoring
                           │
         ┌─────────────┬───┴─────────┬─────────────┐
         ▼             ▼             ▼             ▼
     Academic        Skills       Projects     Experience
       30%            25%           25%           20%
         │             │             │             │
         └─────────────┼─────────────┴─────────────┘
                       ▼
            Composite Readiness Score
                       │
                       ▼
           Delta Comparison vs. Baseline
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
 Action Directives            Verifiable PDF Audit

🔐 Privacy & Security Framework
EduPath AI is built on a privacy-first architecture:

Isolated Account Gate: Replaces open profile selectors with a secure authentication layer.

Cryptographic Hashing: Passcodes are hashed with SHA-256 before being written to disk; plaintext passwords are never stored.

Strict Data Segregation: Each student profile resides in an isolated schema (data/students/<sanitized_id>.json), preventing cross-user data leakage.

No Inadvertent Git Tracking: All local credentials, personal student profiles, vector database indices, and cache files are strictly excluded from version control via .gitignore.

# 🛠️ Technology Stack

| Category | Technology |
| :--- | :--- |
| **Programming Language** | Python 3.10+ |
| **Web Framework** | Streamlit |
| **AI / LLM Engine** | Google Gemini API |
| **Vector Database (RAG)** | ChromaDB |
| **Data Processing** | Pandas, NumPy |
| **PDF Extraction** | PyPDF2, pdfplumber |
| **Report Generation** | ReportLab |
| **Cryptographic Security** | Python `hashlib` (SHA-256) |
| **Deployment Platform** | Streamlit Community Cloud |
| **Version Control** | Git & GitHub |

📂 Repository Structure
EduPath-AI/
│
├── .streamlit/
│   ├── config.toml           # UI branding tokens & server parameters
│   └── secrets.toml          # API keys & local secrets (git-ignored)
│
├── data/
│   ├── credentials.json      # SHA-256 hashed credentials (git-ignored)
│   ├── opportunities.csv     # Verified global opportunities database
│   └── students/             # Isolated student JSON profiles (git-ignored)
│       └── sample_student.json
│
├── src/
│   ├── academic_analysis.py  # Transcript parsing & remediation strategy generator
│   ├── achievements.py       # Rule-based automatic milestone & badge detection
│   ├── career_analysis.py    # Career trajectory synthesis & skill gap audits
│   ├── progress_tracker.py   # 100-point longitudinal readiness evaluator
│   ├── rag.py                # ChromaDB vector indexing & catalog semantic retrieval
│   ├── report_generator.py   # Publication-grade ReportLab PDF export engine
│   ├── roadmap.py            # Adaptive 4-year milestone engine
│   ├── storage.py            # Hashed auth gates & isolated JSON data management
│   └── utils.py              # Gemini client, backoff retries, & model fallback logic
│
├── app.py                    # Main dashboard, UI layout, & navigation routing
├── requirements.txt          # Production environment dependencies
├── LICENSE                   # MIT License
└── README.md

⚙️ Local Installation & Setup
1. Clone the repository
git clone [https://github.com/mshakeelrasheed/EduPath-AI.git](https://github.com/mshakeelrasheed/EduPath-AI.git)
cd EduPath-AI
2. Create and activate a virtual environment
Windows (PowerShell)
python -m venv venv
venv\Scripts\activate
macOS / Linux
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Configure environment secrets
Create .streamlit/secrets.toml in the project root:
mkdir -p .streamlit
touch .streamlit/secrets.toml
Add your Google Gemini API key:
GEMINI_API_KEY = "AIzaSyYourGeminiApiKeyHere"
▶️ Run EduPath AI
Start the application locally:
streamlit run app.py
Access the portal at http://localhost:8501.

📊 User Workflow
1. Sign In or Create a Secure Student Account
                       ↓
2. Complete Profile & Upload Academic Transcript
                       ↓
3. Upload & Vectorize University Catalog (PDF)
                       ↓
4. Review Coursework Performance & Address Weak Subjects
                       ↓
5. Synthesize Grounded Career Recommendations
                       ↓
6. Generate / Adapt the 4-Year University Roadmap
                       ↓
7. Query the Grade-Aware AI Advisor Companion
                       ↓
8. Log Projects, Skills, and Verified Achievements
                       ↓
9. Re-Evaluate Readiness vs. Day-One Baseline
                       ↓
10. Download Official PDF Progress Audit & Portfolio

👨‍💻 Author
Muhammad Shakeel Rasheed
Lead Developer & AI Engineer

Affiliation: BS Artificial Intelligence, The Islamia University Bahawalpur

GitHub: @mshakeelrasheed

LinkedIn: muhammad-shakeel-rasheed

Hugging Face: @mshakeelrasheed

📜 License
This project is licensed under the MIT License — see the LICENSE file for details.

🎓 EduPath AI
Guiding students from enrollment to career readiness with grounded intelligence.
Built with Python • Streamlit • Google Gemini • ChromaDB • ReportLab

⭐ If you find EduPath AI helpful, consider starring the repository.
