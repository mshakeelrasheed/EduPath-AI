<div align="center">

# 🎓 EduPath AI

### Privacy-First Academic Companion & Longitudinal Career Navigator

**Transforming raw academic transcripts and university syllabi into grounded four-year roadmaps and verifiable career readiness.**

<p>

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-ff4b4b?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Google Gemini](https://img.shields.io/badge/Google_Gemini-API-orange?style=for-the-badge&logo=google)](https://ai.google.dev/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_RAG-blueviolet?style=for-the-badge)](https://www.trychroma.com/)
[![ReportLab](https://img.shields.io/badge/ReportLab-PDF_Audits-red?style=for-the-badge)](https://www.reportlab.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</p>

### 🚀 Live Demo

**[Launch EduPath AI](https://edupath-ai-companion.streamlit.app/)**

</div>

---

# 📌 Overview

**EduPath AI** is an intelligent, privacy-focused academic and career companion designed to bridge the gap between university coursework, degree requirements, skill development, and real-world career readiness.

Instead of relying on generic career advice, EduPath AI analyzes verified student academic data, uses **Retrieval-Augmented Generation (RAG)** over official institutional handbooks, and tracks longitudinal progress against an immutable day-one baseline.

The platform addresses a practical question:

> **How can a student navigate their institutional curriculum without hallucinated information, remediate weak subjects, and continuously measure career readiness while maintaining strict data privacy?**

EduPath AI combines:

- 📄 Automatic transcript and coursework parsing
- 📑 Course catalog ingestion using ChromaDB-based RAG
- 📊 Balanced 100-point career readiness scoring
- 💡 Targeted academic remediation
- 🗺️ Adaptive four-year academic and career roadmapping
- 💬 Grade-aware AI advisory companion
- 🎯 Verified opportunity tracking
- 🏆 Rule-based milestone and achievement progression
- 📈 Longitudinal progress tracking
- 📄 Automated PDF progress audits and portfolio generation

---

# 🎯 Problem Statement

Higher education advising is often fragmented, reactive, and disconnected from changing industry requirements.

### Major Problems

#### 📚 Syllabus Disconnect

University handbooks, course prerequisites, degree requirements, and course descriptions are often buried inside large static PDFs that students rarely consult.

#### 🤖 Generic AI Hallucinations

General-purpose AI systems can generate incorrect university requirements, fabricated course codes, inaccurate prerequisites, or outdated application information.

#### 📉 Lack of Longitudinal Tracking

Students often lack a quantitative way to understand how their:

- Academic performance
- Technical skills
- Projects
- Internships
- Achievements

compound over time toward their desired career.

#### 🔐 Privacy & Security Risks

Academic transcripts contain sensitive student information. Uploading these records to uncontrolled platforms can create unnecessary privacy and data-leakage risks.

---

# 💡 Our Solution

EduPath AI combines document parsing, local vector retrieval, structured analytics, and Large Language Model reasoning into a unified academic and career intelligence platform.

```text
        Academic Transcript                University Catalog
                │                                │
                ▼                                ▼
       Text Extraction Layer            ChromaDB Vector Store
                │                                │
                ▼                                ▼
      Coursework Analytics Engine          Semantic RAG
                │                                │
                └──────────────┬─────────────────┘
                               │
                               ▼
                 ┌──────────────────────────┐
                 │     Readiness Engine     │
                 │      100-Point Audit     │
                 └────────────┬─────────────┘
                              │
                 ┌────────────┴────────────┐
                 ▼                         ▼
        Dynamic 4-Year Roadmap       Grade-Aware AI
                                   Advisor Companion
                 │                         │
                 └────────────┬────────────┘
                              │
                              ▼
                 Longitudinal Progress Tracking
                              │
                              ▼
                 PDF Progress Audit & Portfolio
```

The system evaluates student development across four balanced pillars:

```text
Academic Standing
       +
Skills Matrix
       +
Practical Projects
       +
Experience / Internships
       =
Career Readiness
```

This shifts academic guidance from:

> **"What electives should I take?"**

to:

> **"Based on your academic performance, prerequisite courses, institutional handbook, skills, and target career, which milestones should you complete next to improve your readiness?"**

---

# ✨ Key Features

## 📄 1. Transcript Analytics & Grading Breakdown

EduPath AI processes semester result documents and extracts:

- Course titles
- Numerical marks
- Letter grades
- Semester performance

The system automatically categorizes academic performance into:

- 🟢 Strong
- 🟡 Average
- 🔴 Weak

Weak areas are highlighted to help students identify academic blind spots before they affect downstream courses.

---

## 💡 2. Targeted Academic Remediation

For weak subjects, EduPath AI generates targeted recovery strategies.

The system can provide:

- Weekly revision plans
- Conceptual learning targets
- Practice recommendations
- Subject-specific improvement strategies
- Career-aligned learning priorities

The goal is not simply to identify a weak grade, but to convert it into an actionable improvement plan.

---

## 📑 3. Grounded Catalog Knowledge Base — RAG

Official university handbooks, degree catalogs, and course syllabi can be processed into a **ChromaDB vector store**.

The RAG system enables:

- Semantic course searching
- Degree requirement retrieval
- Prerequisite discovery
- Course relationship analysis
- Curriculum-grounded recommendations

### 🛡️ Anti-Hallucination Guardrail

If a course rule, prerequisite, or requirement is not present in the uploaded institutional catalog, EduPath AI explicitly states that the information could not be verified.

This prevents the AI from inventing university-specific requirements.

---

## 📊 4. Quantitative 100-Point Career Readiness Engine

EduPath AI calculates career readiness using four major dimensions.

### Readiness Formula

```text
Readiness Score =
    (Academic Metric    × 0.30)
  + (Skills Matrix      × 0.25)
  + (Project Portfolio  × 0.25)
  + (Field Experience   × 0.20)
```

### Scoring Breakdown

| Dimension | Weight |
|---|---:|
| 🎓 Academic Foundation | 30% |
| 🛠️ Technical & Professional Skills | 25% |
| 🚀 Portfolio & Projects | 25% |
| 💼 Experience / Internships | 20% |
| **Total** | **100%** |

### Academic Foundation

Measures:

- Coursework performance
- GPA
- Grade consistency
- Academic progression

### Technical & Professional Skills

Measures:

- Technical competencies
- Programming skills
- Tools
- Professional capabilities
- Validated skill development

### Portfolio & Projects

Measures:

- Completed projects
- GitHub repositories
- Production deployments
- Practical implementations

### Field Experience

Measures:

- Internships
- Fellowships
- Research experience
- Relevant professional exposure

---

# 📈 Longitudinal Progress Tracking

EduPath AI maintains a **day-one baseline** and compares future progress against it.

```text
                    Day-One Baseline
                           │
                           ▼
                  Initial Readiness
                           │
                           ▼
        ┌─────────────────────────────────┐
        │       Student Progress          │
        │                                 │
        │  Academic → Skills → Projects  │
        │  → Experience → Achievements   │
        └────────────────┬────────────────┘
                         │
                         ▼
                  Updated Readiness
                         │
                         ▼
                  Progress Delta
```

Students can continue updating their information over time, allowing the system to show how their career readiness changes across semesters.

The tracker can represent progress through:

- Not Started
- In Progress
- Completed

---

# 🏆 Achievements & Milestone Tracking

EduPath AI includes rule-based milestone detection to recognize meaningful student progress.

Achievements can be associated with:

- Academic milestones
- Completed roadmap milestones
- Technical skill development
- Projects
- Internships
- Research
- Competitions
- Other verified accomplishments

The achievement layer transforms individual accomplishments into a visible career-development history.

---

# 🗺️ 5. Dynamic 4-Year Adaptive Roadmap

EduPath AI generates a field-specific roadmap covering:

```text
Year 1
  ↓
Foundation & Academic Development
  ↓
Year 2
  ↓
Skill Building & Practical Projects
  ↓
Year 3
  ↓
Specialization & Experience
  ↓
Year 4
  ↓
Career Preparation & Industry Readiness
```

Roadmap milestones can be tracked using:

- ⚪ Not Started
- 🟡 In Progress
- 🟢 Completed

Completing roadmap milestones contributes to the student's overall progress ledger and readiness evaluation.

---

# 💬 6. Grade-Aware AI Advisory Companion

EduPath AI provides a conversational AI advisor that understands the student's academic context.

The assistant can use:

- Student coursework
- Grades
- Declared interests
- Career goals
- RAG-retrieved catalog information
- Current progress
- Skills
- Projects

This enables more personalized recommendations than a generic AI chatbot.

### AI Infrastructure

The advisor is powered by **Google Gemini** with:

- Dynamic model fallback
- Retry handling
- Exponential backoff
- Context-aware prompting

---

# 🎯 7. Verified Opportunities Ledger

EduPath AI provides a centralized opportunity layer for students.

Supported opportunity categories include:

- 💼 Internships
- 🏆 Hackathons
- 🔬 Research opportunities
- 🎓 Fellowships
- 🌎 Global competitions

Opportunity sources can include platforms such as:

- Devpost
- Lablab.ai
- Other verified opportunity sources

Opportunities can be filtered according to the student's academic discipline and career direction.

---

# 📄 8. Automated PDF Audit & Portfolio Generation

EduPath AI can generate publication-grade PDF documents using **ReportLab**.

## 📊 Career Progress Audit

The progress audit can contain:

- Overall readiness score
- Category scores
- Historical progress
- Baseline comparison
- Progress deltas
- Strategic recommendations
- Career readiness analysis

## 📁 Student Career Portfolio

The portfolio provides a professional summary containing:

- Student profile
- Career goals
- Technical skills
- Completed projects
- Verified achievements
- Relevant experience
- Career development progress

---

# 🧠 Scoring & Readiness Architecture

The scoring system follows a weighted, normalized multi-variable model.

```text
                    Student Records
                          │
                          ▼
                Multi-Pillar Scoring
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼                 ▼
    Academic           Skills            Projects         Experience
      30%               25%                25%               20%
        │                 │                  │                 │
        └─────────────────┴──────────────────┴─────────────────┘
                          │
                          ▼
                Composite Readiness Score
                          │
                          ▼
                 Baseline Comparison
                          │
                 ┌────────┴────────┐
                 ▼                 ▼
          Action Directives    PDF Progress Audit
```

---

# 🔐 Privacy & Security Framework

EduPath AI follows a privacy-first architecture.

## 🔑 Isolated Account Gate

The platform uses a secure authentication layer instead of open profile selectors.

## 🔒 Cryptographic Hashing

Passcodes are hashed using **SHA-256** before being written to disk.

Plaintext passwords are not stored.

## 🗂️ Strict Data Segregation

Each student profile is stored separately:

```text
data/students/<sanitized_id>.json
```

This structure helps prevent cross-user data leakage.

## 🚫 Git Tracking Protection

Sensitive files are excluded from version control through `.gitignore`, including:

```text
credentials
student profiles
vector database files
cache files
local secrets
API keys
```

---

# 🛠️ Technology Stack

| Category | Technology |
|---|---|
| **Programming Language** | Python 3.10+ |
| **Web Framework** | Streamlit |
| **AI / LLM Engine** | Google Gemini API |
| **Vector Database** | ChromaDB |
| **Data Processing** | Pandas, NumPy |
| **PDF Extraction** | PyPDF2, pdfplumber |
| **PDF Generation** | ReportLab |
| **Cryptographic Security** | Python `hashlib` — SHA-256 |
| **Deployment Platform** | Streamlit Community Cloud |
| **Version Control** | Git & GitHub |

---

# 📂 Repository Structure

```text
EduPath-AI/
│
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
│
├── data/
│   ├── credentials.json
│   ├── opportunities.csv
│   └── students/
│       └── sample_student.json
│
├── src/
│   ├── academic_analysis.py
│   ├── achievements.py
│   ├── career_analysis.py
│   ├── progress_tracker.py
│   ├── rag.py
│   ├── report_generator.py
│   ├── roadmap.py
│   ├── storage.py
│   └── utils.py
│
├── app.py
├── requirements.txt
├── LICENSE
└── README.md
```

### Module Responsibilities

| File | Responsibility |
|---|---|
| `app.py` | Main dashboard, UI layout, and navigation |
| `academic_analysis.py` | Transcript parsing and academic remediation |
| `achievements.py` | Automatic milestone and achievement detection |
| `career_analysis.py` | Career trajectory and skill-gap analysis |
| `progress_tracker.py` | Longitudinal 100-point readiness evaluation |
| `rag.py` | ChromaDB indexing and semantic catalog retrieval |
| `report_generator.py` | PDF audit and portfolio generation |
| `roadmap.py` | Adaptive four-year roadmap engine |
| `storage.py` | Authentication and isolated student data management |
| `utils.py` | Gemini client, retry handling, and model fallback logic |

---

# ⚙️ Local Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/mshakeelrasheed/EduPath-AI.git
cd EduPath-AI
```

## 2. Create a Virtual Environment

### Windows — PowerShell

```powershell
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment Secrets

Create:

```text
.streamlit/secrets.toml
```

Add your Google Gemini API key:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

> ⚠️ Never commit your API key to GitHub.

Make sure `.streamlit/secrets.toml` is included in `.gitignore`.

---

# ▶️ Run EduPath AI

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

# 📊 User Workflow

```text
1. Create or Sign In to a Secure Student Account
                         ↓
2. Complete Student Profile
                         ↓
3. Upload Academic Transcript
                         ↓
4. Upload University Course Catalog
                         ↓
5. Vectorize Catalog Using RAG
                         ↓
6. Analyze Coursework Performance
                         ↓
7. Identify Weak Subjects
                         ↓
8. Generate Targeted Remediation
                         ↓
9. Generate Grounded Career Recommendations
                         ↓
10. Generate / Adapt 4-Year Roadmap
                         ↓
11. Track Roadmap Progress
                         ↓
12. Log Skills, Projects & Experience
                         ↓
13. Add / Detect Achievements
                         ↓
14. Re-Evaluate Career Readiness
                         ↓
15. Compare Progress Against Baseline
                         ↓
16. Download PDF Progress Audit
                         ↓
17. Download Student Career Portfolio
```

---

# 🔄 Continuous Student Progress Cycle

EduPath AI is designed to be used throughout a student's degree rather than only once.

```text
          INITIAL ANALYSIS
                │
                ▼
        Day-One Baseline
                │
                ▼
        Personalized Roadmap
                │
                ▼
       Student Takes Action
                │
                ▼
      Projects / Skills / Grades
                │
                ▼
         Add Achievements
                │
                ▼
       Update Progress Tracker
                │
                ▼
       Recalculate Readiness
                │
                ▼
       Compare With Baseline
                │
                ▼
        Generate New Guidance
                │
                └───────────────┐
                                │
                                ▼
                       Continuous Tracking
```

This allows students to repeatedly update their academic and career information as they progress through university.

---

# 📈 Progress Report Generation

The system can generate a downloadable PDF report containing the student's current career-readiness state.

A typical report can include:

```text
Student Profile
      ↓
Academic Performance
      ↓
Skills Development
      ↓
Project Portfolio
      ↓
Experience
      ↓
Achievements
      ↓
Current Readiness Score
      ↓
Baseline Comparison
      ↓
Progress Delta
      ↓
Strategic Recommendations
```

This provides students with a tangible record of how their career readiness evolves over time.

---

# 🔮 Future Development

Potential future improvements include:

- 📊 Advanced progress analytics
- 📈 Semester-by-semester readiness charts
- 🏆 Expanded achievement and badge systems
- 🎯 More sophisticated career matching
- 🔎 Automated opportunity verification
- 🧠 Improved multi-model AI orchestration
- 📚 Support for multiple university catalogs
- 📱 Mobile-friendly student dashboard
- 🔔 Personalized deadline and opportunity alerts
- 📄 Enhanced professional portfolio exports

---

# 👨‍💻 Author

### Muhammad Shakeel Rasheed

**Lead Developer & AI Engineer**

🎓 **BS Artificial Intelligence**  
The Islamia University of Bahawalpur

### Profiles

- **GitHub:** [@mshakeelrasheed](https://github.com/mshakeelrasheed)
- **LinkedIn:** [muhammad-shakeel-rasheed](https://www.linkedin.com/in/muhammad-shakeel-rasheed/)
- **Hugging Face:** [@mshakeelrasheed](https://huggingface.co/mshakeelrasheed)

---

# 📜 License

This project is licensed under the **MIT License**.

See the [`LICENSE`](LICENSE) file for more information.

---

<div align="center">

# 🎓 EduPath AI

### Guiding students from enrollment to career readiness with grounded intelligence.

**Built with Python • Streamlit • Google Gemini • ChromaDB • ReportLab**

<br>

⭐ **If you find EduPath AI helpful, consider starring the repository.**

</div>
