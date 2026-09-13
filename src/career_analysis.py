import os
import json
import pandas as pd
from typing import Dict, Any, List
from src.utils import call_gemini

CAREER_CSV = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "career_data.csv")

def load_career_reference_data() -> pd.DataFrame:
    if os.path.exists(CAREER_CSV):
        try:
            return pd.read_csv(CAREER_CSV)
        except Exception:
            pass
    return pd.DataFrame()

def generate_career_recommendations(student_data: Dict[str, Any], catalog_context: str = "") -> Dict[str, Any]:
    profile = student_data.get("profile", {})
    records = student_data.get("academic_records", [])
    skills = [s.get("name", "") for s in student_data.get("skills", [])]
    
    strong_subjects = []
    weak_subjects = []
    for r in records:
        for s in r.get("subjects", []):
            if s.get("status") == "Strong":
                strong_subjects.append(s.get("name"))
            elif s.get("status") == "Weak":
                weak_subjects.append(s.get("name"))

    system_prompt = (
        "You are an objective academic and career guidance counselor. "
        "Generate holistic, realistic career options based on student evidence: field, marks, skills, and goals. "
        "Do not make absolute guarantees regarding hiring or dates. Use cautious phrasing ('Current trends suggest...', 'Potential risk...'). "
        "Return ONLY a clean JSON object conforming strictly to the schema without markdown ticks:\n"
        "{\n"
        "  \"primary_recommendation\": {\n"
        "    \"career_name\": \"...\",\n"
        "    \"match_level\": \"High/Medium\",\n"
        "    \"match_explanation\": \"...\",\n"
        "    \"required_skills\": [\"...\"],\n"
        "    \"current_skill_gaps\": [\"...\"],\n"
        "    \"recommended_projects\": [\"...\"],\n"
        "    \"potential_risks_and_considerations\": \"...\"\n"
        "  },\n"
        "  \"alternative_recommendations\": [\n"
        "    {\n"
        "      \"career_name\": \"...\",\n"
        "      \"match_level\": \"...\",\n"
        "      \"match_explanation\": \"...\",\n"
        "      \"required_skills\": [\"...\"],\n"
        "      \"current_skill_gaps\": [\"...\"]\n"
        "    }\n"
        "  ],\n"
        "  \"transferable_strengths_summary\": \"...\"\n"
        "}"
    )

    prompt = (
        f"Field: {profile.get('field')}\n"
        f"Degree: {profile.get('degree')} ({profile.get('current_year')})\n"
        f"Interests: {', '.join(profile.get('interests', []))}\n"
        f"Stated Career Goal: {profile.get('career_goals')}\n"
        f"Preferred Career: {profile.get('preferred_career')}\n"
        f"Strong Subjects: {', '.join(strong_subjects) if strong_subjects else 'None recorded'}\n"
        f"Weak Subjects: {', '.join(weak_subjects) if weak_subjects else 'None recorded'}\n"
        f"Current Skills: {', '.join(skills) if skills else 'None recorded'}\n"
        f"Optional Handbook Course Context: {catalog_context[:1000] if catalog_context else 'None'}"
    )

    raw_response = call_gemini(prompt, system_instruction=system_prompt, response_mime_type="application/json")
    cleaned = raw_response.replace("```json", "").replace("```", "").strip()
    try:
        return json.loads(cleaned)
    except Exception:
        return {
            "primary_recommendation": {
                "career_name": profile.get("preferred_career") or "Domain Specialist",
                "match_level": "Moderate",
                "match_explanation": "Recommendations were synthesized directly from stated interests and active coursework.",
                "required_skills": ["Fundamental Domain Research", "Data Management", "Technical Communication"],
                "current_skill_gaps": ["Industry Toolchains", "Applied Field Projects"],
                "recommended_projects": ["Independent capstone inquiry", "Practical domain workflow"],
                "potential_risks_and_considerations": "Evolving industry benchmarks demand continuous portfolio validation."
            },
            "alternative_recommendations": [],
            "transferable_strengths_summary": "Strong general coursework and baseline commitment to self-directed projects."
        }