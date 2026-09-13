# 🎓 EduPath AI

### Privacy-First Academic Companion & Longitudinal Career Navigator

> **EduPath AI** transforms raw academic transcripts and university syllabi into grounded four-year academic roadmaps, personalized career guidance, measurable readiness insights, and verifiable progress reports.

<p align="center">

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io/)
[![Google Gemini](https://img.shields.io/badge/AI-Google%20Gemini-4285F4?logo=google)](https://ai.google.dev/)
[![ChromaDB](https://img.shields.io/badge/RAG-ChromaDB-orange)](https://www.trychroma.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

</p>

<p align="center">
  <a href="https://edupath-ai-companion.streamlit.app/">
    <strong>🚀 Live Demo</strong>
  </a>
</p>

---

## 📌 Overview

Students often have access to grades, course outlines, and career resources, but these pieces of information are rarely connected into one continuous academic and career journey.

**EduPath AI** addresses this gap by combining:

- 📄 Academic transcript analysis
- 📚 University syllabus and catalog grounding
- 🧠 Retrieval-Augmented Generation (RAG)
- 📊 Academic and career readiness scoring
- 🛠️ Personalized skill remediation
- 🗺️ Adaptive four-year roadmaps
- 🤖 Grade-aware AI advising
- 🎯 Verified career opportunities
- 📈 Longitudinal progress tracking
- 🏆 Achievement and milestone tracking
- 📑 Downloadable PDF progress audits and portfolios

Instead of providing generic AI advice, EduPath AI maintains a student's academic context and continuously updates recommendations as the student progresses.

---

## 🎯 Problem Statement

University students commonly face several connected problems:

### 1. Syllabus Disconnect

Students know which courses they are taking, but often do not know how individual courses map to:

- Required technical skills
- Projects
- Career roles
- Industry expectations
- Future learning goals

### 2. Generic AI Advice

Traditional AI assistants can provide useful suggestions, but without grounding them in the student's actual academic record, advice can become generic or inaccurate.

### 3. No Longitudinal Tracking

Most academic tools focus on the current semester.

Students need a system that can answer:

> **"How am I progressing compared with where I started?"**

### 4. Scattered Achievements

Projects, certifications, internships, competitions, leadership activities, and other achievements are often stored separately and are difficult to connect to career readiness.

### 5. Privacy Concerns

Academic transcripts and student profiles contain sensitive personal information. A student-focused system should minimize unnecessary exposure and isolate individual profiles.

---

# 💡 Solution

EduPath AI creates a continuous student-development cycle:

```text
Academic Data
     ↓
Transcript & Syllabus Analysis
     ↓
Grounded Knowledge Retrieval
     ↓
Readiness Assessment
     ↓
Skill Gap Detection
     ↓
Personalized Recommendations
     ↓
Four-Year Roadmap
     ↓
Progress & Achievement Tracking
     ↓
Updated Readiness Assessment
     ↓
Progress Report / Portfolio
```

The key idea is simple:

> **Analyze → Recommend → Act → Track → Reassess → Improve**

---

# ✨ Key Features

## 📄 1. Academic Transcript Analysis

EduPath AI extracts academic information from student transcripts and converts it into structured data.

The system can analyze:

- Courses
- Grades
- Credit hours
- Academic performance
- Completed coursework
- Areas requiring improvement

This creates the academic foundation for the rest of the system.

---

## 📚 2. University Syllabus Grounding

University course information can be stored and indexed using **ChromaDB**.

This enables the AI advisor to retrieve relevant academic context instead of relying only on general model knowledge.

### RAG Pipeline

```text
University Catalog / Syllabus
            ↓
      Document Processing
            ↓
        Chunking
            ↓
       ChromaDB Index
            ↓
    Semantic Retrieval
            ↓
       Gemini AI
            ↓
 Grounded Recommendation
```

---

## 📊 3. 100-Point Career Readiness Score

EduPath AI evaluates student readiness using four major pillars:

| Pillar | Weight |
|---|---:|
| 🎓 Academic | 30% |
| 🧠 Skills | 25% |
| 🛠️ Projects | 25% |
| 💼 Experience | 20% |
| **Total** | **100%** |

### Readiness Formula

```text
Readiness Score =
    Academic × 0.30
  + Skills × 0.25
  + Projects × 0.25
  + Experience × 0.20
```

The score is designed to provide a high-level snapshot of career preparation rather than functioning as a formal academic evaluation.

---

# 🛠️ 4. Skill Gap & Remediation Engine

After analyzing academic and career readiness data, EduPath AI identifies areas where the student may need additional development.

Examples include:

- Programming
- Data Structures & Algorithms
- Machine Learning
- Deep Learning
- Databases
- Cloud
- Communication
- Project experience
- Industry exposure

The system can then recommend targeted learning or practical activities.

### Example

```text
Current State
     ↓
Missing Skill: Machine Learning Deployment
     ↓
Recommended Learning
     ↓
Build a Deployment Project
     ↓
Add Achievement
     ↓
Recalculate Readiness
```

---

# 🗺️ 5. Adaptive Four-Year Roadmap

EduPath AI generates a personalized roadmap based on the student's:

- Current semester
- Academic performance
- Existing skills
- Skill gaps
- Projects
- Career interests
- Experience
- Achievements

The roadmap is designed to evolve rather than remain a static four-year plan.

```text
Year 1
├── Academic Foundation
├── Programming
└── Basic Projects

Year 2
├── Core AI / CS Skills
├── Intermediate Projects
└── Technical Certifications

Year 3
├── Specialization
├── Advanced Projects
├── Research / Internship
└── Portfolio Development

Year 4
├── Capstone Project
├── Industry Preparation
├── Resume / Portfolio
└── Job / Graduate Study Preparation
```

---

# 🤖 6. Grade-Aware AI Advisor

The AI advisor uses the student's academic context to make recommendations.

Instead of asking:

> "What should an AI student learn?"

a student can receive guidance based on their actual academic progress.

Examples:

- Which skill should I learn next?
- Which project fits my current level?
- What should I improve before applying for internships?
- Which courses are related to my target career?
- What should I focus on this semester?

---

# 🎯 7. Verified Opportunities

EduPath AI can surface relevant opportunities such as:

- Internships
- Projects
- Certifications
- Competitions
- Career opportunities
- Learning opportunities

The objective is to connect readiness gaps with practical opportunities.

---

# 📈 8. Longitudinal Progress Tracking

A major part of EduPath AI is tracking how a student's profile changes over time.

The system supports a continuous cycle:

```text
Initial Analysis
      ↓
Baseline Readiness
      ↓
Student Takes Action
      ↓
Student Updates Progress
      ↓
System Recalculates
      ↓
New Readiness Score
      ↓
Progress Comparison
```

Students can manually update their progress by adding:

- New skills
- Completed projects
- Certifications
- Internships
- Competitions
- Experience
- Other academic/career milestones

The system can then compare the updated state against earlier progress.

### Example

```text
Initial Readiness      → 58/100
       ↓
Completed ML Project
       ↓
Earned Certification
       ↓
Added Internship
       ↓
Updated Readiness      → 74/100
```

This makes the platform longitudinal rather than just a one-time academic analyzer.

---

# 🏆 9. Achievements & Milestone Tracking

Students can maintain a structured record of meaningful achievements.

Examples:

- 🥇 Competition wins
- 📜 Certifications
- 💻 Projects
- 🧪 Research
- 💼 Internships
- 🎤 Presentations
- 🏅 Awards
- 👥 Leadership activities
- 📚 Completed learning milestones

Achievements can become part of the student's overall career-readiness picture.

### Achievement Flow

```text
Student Adds Achievement
          ↓
Achievement Stored
          ↓
Profile Updated
          ↓
Relevant Readiness Area Updated
          ↓
Progress Report Updated
```

---

# 📑 10. Downloadable Progress Audit & Portfolio

EduPath AI can generate a PDF containing a structured snapshot of the student's development.

A progress report can include:

- Student profile
- Academic summary
- Readiness score
- Readiness breakdown
- Skills
- Skill gaps
- Projects
- Achievements
- Experience
- Roadmap
- Progress observations
- Career recommendations

This can function as a personal academic/career audit and a structured portfolio artifact.

---

# 🧠 System Architecture

```text
┌───────────────────────────────────────────┐
│              Student Input                │
│ Transcript + Profile + Syllabus + Updates │
└─────────────────────┬─────────────────────┘
                      ↓
┌───────────────────────────────────────────┐
│          Document & Data Processing        │
│ PDF Extraction + Pandas + Validation       │
└─────────────────────┬─────────────────────┘
                      ↓
┌───────────────────────────────────────────┐
│              Knowledge Layer               │
│         ChromaDB + Semantic RAG             │
└─────────────────────┬─────────────────────┘
                      ↓
┌───────────────────────────────────────────┐
│              Analysis Layer                │
│ Academic + Skills + Projects + Experience │
└─────────────────────┬─────────────────────┘
                      ↓
┌───────────────────────────────────────────┐
│            Readiness Engine                │
│              100-Point Score               │
└─────────────────────┬─────────────────────┘
                      ↓
┌───────────────────────────────────────────┐
│            Recommendation Layer            │
│ Gaps + Remediation + Roadmap + AI Advisor │
└─────────────────────┬─────────────────────┘
                      ↓
┌───────────────────────────────────────────┐
│         Longitudinal Tracking Layer        │
│ Progress + Achievements + Milestones       │
└─────────────────────┬─────────────────────┘
                      ↓
┌───────────────────────────────────────────┐
│              Output Layer                 │
│ Dashboard + Opportunities + PDF Reports   │
└───────────────────────────────────────────┘
```

---

# 🔄 Continuous Student Progress Cycle

EduPath AI is designed around repeated evaluation rather than a one-time analysis.

```text
┌──────────────────────┐
│ 1. Student Onboards  │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ 2. Initial Analysis  │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ 3. Readiness Score   │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ 4. Recommendations   │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ 5. Student Progress  │
│    & Achievements    │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ 6. Reassessment      │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ 7. Progress Report   │
└──────────┬───────────┘
           │
           └──────────────→ Repeat
```

---

# 📊 Progress Report Generation

The reporting system converts the student's current state into a downloadable document.

```text
Student Profile
      ↓
Current Academic Data
      ↓
Skills + Projects + Experience
      ↓
Achievements
      ↓
Readiness Calculation
      ↓
Historical Progress
      ↓
AI-Generated Insights
      ↓
PDF Progress Audit
```

The report provides a point-in-time snapshot while preserving the idea of continuous progress.

---

# 🔐 Privacy & Security

EduPath AI is designed with student privacy in mind.

### Current privacy-oriented mechanisms include:

- 🔒 Secure account/profile gate
- 🔑 SHA-256 hashed passcodes
- 👤 Isolated student JSON profiles
- 🚫 Secrets excluded through `.gitignore`
- 🚫 Student profiles excluded from version control
- 🚫 Local vector databases excluded from version control
- 🚫 Cache and generated runtime data excluded from version control

### Sensitive Files

The project should not commit:

```text
.env
student_profiles/
chroma_db/
cache/
secrets/
```

API keys and other secrets should be stored through environment variables or the deployment platform's secret-management system.

---

# 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| **Python 3.10+** | Core application |
| **Streamlit** | Web application and dashboard |
| **Google Gemini API** | AI reasoning and recommendations |
| **ChromaDB** | Vector database / RAG |
| **Pandas** | Data processing |
| **NumPy** | Numerical computation |
| **PyPDF2 / pdfplumber** | PDF extraction |
| **ReportLab** | PDF report generation |
| **hashlib** | Passcode hashing |
| **Git / GitHub** | Version control |
| **Streamlit Cloud** | Deployment |

---

# 📂 Project Structure

```text
EduPath-AI/
│
├── .streamlit/
│   └── config.toml
│
├── data/
│   └── university/
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
├── .gitignore
├── LICENSE
└── README.md
```

---

# 🧩 Module Responsibilities

### `app.py`

Main Streamlit application and user interface.

### `academic_analysis.py`

Handles academic performance and transcript-related analysis.

### `achievements.py`

Manages student achievements and milestones.

### `career_analysis.py`

Evaluates career-readiness information and career-related gaps.

### `progress_tracker.py`

Handles longitudinal progress updates and comparisons.

### `rag.py`

Manages retrieval-augmented generation and ChromaDB interactions.

### `report_generator.py`

Generates downloadable PDF reports.

### `roadmap.py`

Generates and manages personalized academic/career roadmaps.

### `storage.py`

Handles student profile and local data persistence.

### `utils.py`

Contains shared helper functions and utilities.

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/mshakeelrasheed/EduPath-AI.git
cd EduPath-AI
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment Variables

Create a `.env` file or configure secrets through your deployment platform.

Example:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

> Never commit API keys or other secrets to GitHub.

## 5. Run the Application

```bash
streamlit run app.py
```

The application will become available through the local Streamlit URL shown in the terminal.

---

# 🔑 Google Gemini Configuration

EduPath AI uses Google's Gemini API for AI-powered reasoning and recommendations.

You need a valid Gemini API key.

Store the key securely rather than hard-coding it inside the source code.

For Streamlit deployment, configure the key through Streamlit Secrets.

---

# 🧭 User Workflow

```text
1. Sign In
      ↓
2. Create / Load Student Profile
      ↓
3. Upload Academic Transcript
      ↓
4. Provide University Catalog / Syllabus
      ↓
5. Analyze Academic Progress
      ↓
6. Generate Readiness Score
      ↓
7. Identify Skill Gaps
      ↓
8. Receive Remediation Recommendations
      ↓
9. Generate Four-Year Roadmap
      ↓
10. Consult AI Advisor
      ↓
11. Explore Opportunities
      ↓
12. Add Skills / Projects / Achievements
      ↓
13. Reevaluate Progress
      ↓
14. Compare Progress
      ↓
15. Download Progress Audit / Portfolio
```

---

# 📈 Example Readiness Dashboard

A student's readiness profile can be represented as:

```text
Career Readiness
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall Score        74 / 100

Academic             82 / 100
Skills               70 / 100
Projects             68 / 100
Experience           55 / 100
```

The important point is not only the score itself, but **why the score is at that level and what the student can do next**.

---

# 🔁 From Static Profile to Longitudinal Profile

Traditional academic systems often look like:

```text
Student Data → Analysis → Result
```

EduPath AI extends this into:

```text
Student Data
     ↓
Analysis
     ↓
Recommendations
     ↓
Student Action
     ↓
New Skills / Projects / Achievements
     ↓
Updated Profile
     ↓
Reassessment
     ↓
Progress Report
     ↓
Next Recommendations
```

This creates a living academic and career profile rather than a static report.

---

# 🏗️ Development Philosophy

EduPath AI follows several design principles:

### Grounded AI

AI recommendations should be connected to available academic context whenever possible.

### Student-Centered

The system is designed around the student's current state rather than generic career advice.

### Longitudinal

Progress is tracked across time instead of being evaluated only once.

### Explainable

Readiness is divided into understandable components so students can identify improvement areas.

### Privacy-Aware

Student data and application secrets should be isolated from public source control.

### Action-Oriented

Recommendations should lead toward concrete actions such as learning, building, applying, or achieving.

---

# 🧪 Example Student Journey

Consider a student beginning with:

```text
Academic Readiness: 75
Skills:             52
Projects:           40
Experience:         20
```

The system may identify:

```text
Primary Gaps:
- Practical ML projects
- Industry experience
- Portfolio development
```

The roadmap can then prioritize:

```text
1. Complete an ML project
2. Deploy the project
3. Document the project
4. Add the project to the profile
5. Apply for relevant internships
```

After the student updates their profile:

```text
New Project
      +
Deployment
      +
Internship
      +
Certification
      ↓
Updated Readiness
```

The system can reassess the student's current position and provide the next recommendations.

---

# 🌱 Future Development

Potential future improvements include:

- 📊 Advanced progress analytics
- 📅 Semester-by-semester planning
- 📈 Historical readiness charts
- 🎯 More granular career-role matching
- 🧠 Advanced multi-agent career advising
- 🔍 Improved opportunity verification
- 🧾 Enhanced portfolio generation
- 🔔 Progress reminders
- 📱 Mobile-friendly experience
- 🏫 Support for additional universities
- 📚 Larger academic knowledge bases
- 🔐 More advanced privacy and authentication controls

---

# 🌐 Live Demo

Try the deployed application:

**[🚀 EduPath AI — Live Demo](https://edupath-ai-companion.streamlit.app/)**

---

# 👥 Team & Contributions

| Team Member | Role & Contributions |
|---|---|
| **Muhammad Shakeel Rasheed** | **Co-Lead Developer & AI Engineer** — Project ideation, system architecture, core development, AI/RAG implementation, readiness engine, progress tracking, roadmap, and overall project development |
| **Muhammad Rafay** | **Co-Lead Developer & AI Engineer** — Contributed to project ideation, system design, core development, AI functionality, implementation, and overall project development |
| **Muhammad Abdullah** | **Project & Presentation Contributor** — Contributed to the project and prepared the presentation |
| **Malik Muhammad Anees** | **Project & Media Contributor** — Contributed to the project and created the project demonstration video |

### Team Links

- **Muhammad Shakeel Rasheed** — [GitHub](https://github.com/mshakeelrasheed) · [LinkedIn](https://www.linkedin.com/in/muhammad-shakeel-rasheed/)
- **Muhammad Rafay** — [LinkedIn](https://www.linkedin.com/in/muhammad-rafay-itsrafay03/)
- **Muhammad Abdullah** — LinkedIn not provided
- **Malik Muhammad Anees** — LinkedIn not provided

---

# 👨‍💻 Author

### Muhammad Shakeel Rasheed

**Co-Lead Developer & AI Engineer**  
BS Artificial Intelligence — The Islamia University of Bahawalpur

- GitHub: [@mshakeelrasheed](https://github.com/mshakeelrasheed)
- LinkedIn: [Muhammad Shakeel Rasheed](https://www.linkedin.com/in/muhammad-shakeel-rasheed/)
- Hugging Face: [@mshakeelrasheed](https://huggingface.co/mshakeelrasheed)

---

# 📄 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

---

<p align="center">

### 🎓 EduPath AI

**Analyze your journey. Track your progress. Build your future.**

</p>
**Built with Python • Streamlit • Google Gemini • ChromaDB • ReportLab**

<br>

⭐ **If you find EduPath AI helpful, consider starring the repository.**

</div>
