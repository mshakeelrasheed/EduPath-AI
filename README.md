# AI Academic & Career Navigator

A persistent AI companion designed for university students across all academic disciplines (Computer Science, Business, Engineering, Life Sciences, Social Sciences, and the Arts).

---

## Key Capabilities
- **Field-Agnostic Architecture:** Recommends relevant milestones (e.g., case competitions for Business, clinical/lab fellowships for Biology, hackathons for CS).
- **Longitudinal Audit & Preservation:** Initial baseline assessments are locked. Historical assessments are never overwritten.
- **RAG Handbook Ingestion:** Embeds university course catalogs and handbooks via ChromaDB and PyMuPDF to ground course advice without hallucinations.
- **Publication-Ready PDF Reports:** Multi-page progress audits and career portfolios built with ReportLab.

---

## Local Setup

### 1. Prerequisites
- Python 3.10+ installed
- Free-tier Gemini API key from Google AI Studio

### 2. Installation
```bash
git clone https://github.com/your-username/ai-academic-career-navigator.git
cd ai-academic-career-navigator
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt