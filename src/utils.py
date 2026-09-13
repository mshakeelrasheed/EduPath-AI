import os
import streamlit as st
from google import genai
from google.genai import types

def get_gemini_api_key() -> str:
    key = None
    try:
        if "GEMINI_API_KEY" in st.secrets:
            key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass
    if not key:
        key = os.environ.get("GEMINI_API_KEY", "")
    return key.strip()

def get_gemini_client():
    api_key = get_gemini_api_key()
    if not api_key:
        return None
    return genai.Client(api_key=api_key)

def call_gemini(prompt: str, system_instruction: str = "", response_mime_type: str = "text/plain") -> str:
    client = get_gemini_client()
    if not client:
        return "ERROR: Gemini API Key is missing. Configure it in .streamlit/secrets.toml or set the GEMINI_API_KEY environment variable."
    try:
        config = types.GenerateContentConfig(
            response_mime_type=response_mime_type
        )
        if system_instruction:
            config.system_instruction = system_instruction
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
            config=config
        )
        return response.text or ""
    except Exception as exc:
        return f"ERROR: Gemini API execution failed: {str(exc)}"

def calculate_readiness_score(student_data: dict) -> dict:
    records = student_data.get("academic_records", [])
    total_marks = 0
    sub_count = 0
    for rec in records:
        for s in rec.get("subjects", []):
            try:
                m = float(s.get("marks", 0))
                if m > 0:
                    total_marks += m
                    sub_count += 1
            except (ValueError, TypeError):
                continue
    academic_score = round(total_marks / sub_count, 1) if sub_count > 0 else 60.0

    skills = student_data.get("skills", [])
    skill_pts = 0
    for sk in skills:
        lvl = str(sk.get("level", "")).lower()
        if "adv" in lvl:
            skill_pts += 25
        elif "int" in lvl:
            skill_pts += 15
        else:
            skill_pts += 8
    skills_score = min(round((skill_pts / 80.0) * 100, 1), 100.0) if skills else 30.0

    projects = student_data.get("projects", [])
    proj_pts = 0
    for p in projects:
        status = str(p.get("status", "")).lower()
        if status == "completed":
            proj_pts += 30
        elif status == "in progress":
            proj_pts += 15
        else:
            proj_pts += 5
    projects_score = min(round((proj_pts / 60.0) * 100, 1), 100.0) if projects else 15.0

    experiences = student_data.get("experience", [])
    exp_score = min(len(experiences) * 35.0, 100.0) if experiences else 10.0

    certifications = student_data.get("certifications", [])
    cert_score = min(len(certifications) * 30.0, 100.0) if certifications else 15.0

    activities = student_data.get("activities", [])
    act_score = min(len(activities) * 25.0, 100.0) if activities else 15.0

    achievements = student_data.get("achievements", [])
    ach_score = min(len(achievements) * 25.0, 100.0) if achievements else 15.0

    networking_score = min((len(activities) * 15.0) + (len(experiences) * 20.0), 100.0)
    if not activities and not experiences:
        networking_score = 15.0

    portfolio_score = round((projects_score * 0.5) + (skills_score * 0.3) + (ach_score * 0.2), 1)

    overall = (
        (academic_score * 0.20) +
        (skills_score * 0.20) +
        (projects_score * 0.15) +
        (exp_score * 0.15) +
        (cert_score * 0.10) +
        (act_score * 0.05) +
        (networking_score * 0.05) +
        (portfolio_score * 0.10)
    )
    overall_score = int(round(min(max(overall, 0.0), 100.0)))

    return {
        "overall_score": overall_score,
        "academic": round(academic_score, 1),
        "skills": round(skills_score, 1),
        "projects": round(projects_score, 1),
        "experience": round(exp_score, 1),
        "certifications": round(cert_score, 1),
        "activities": round(act_score, 1),
        "networking": round(networking_score, 1),
        "portfolio": round(portfolio_score, 1)
    }