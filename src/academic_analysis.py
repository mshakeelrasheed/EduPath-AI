import json
from typing import Dict, Any, List
from src.utils import call_gemini

def categorize_subject(marks: float) -> str:
    if marks >= 80.0:
        return "Strong"
    elif marks >= 60.0:
        return "Average"
    return "Weak"

def parse_transcript_text(extracted_text: str) -> List[Dict[str, Any]]:
    system_instruction = (
        "You are an academic transcript parser. Extract subject names and numerical marks or percentage grades from "
        "the raw text. Return ONLY a valid JSON array of objects. Do not include markdown code block ticks ```json. "
        "Format: [{\"name\": \"Subject Name\", \"marks\": 85, \"grade\": \"A\"}]. If a value is missing, estimate reasonably."
    )
    prompt = f"Extract all academic subjects and marks from this text:\n\n{extracted_text[:4000]}"
    res = call_gemini(prompt, system_instruction=system_instruction, response_mime_type="application/json")
    
    cleaned_res = res.replace("```json", "").replace("```", "").strip()
    try:
        parsed = json.loads(cleaned_res)
        if isinstance(parsed, list):
            for item in parsed:
                m = float(item.get("marks", 70))
                item["status"] = categorize_subject(m)
            return parsed
    except Exception:
        pass
    return []

def generate_academic_improvement_plan(weak_subjects: List[str], target_career: str, field: str) -> str:
    if not weak_subjects:
        return "No acute academic weaknesses detected. Maintain your solid foundational coursework and continue exploring advanced electives."
    
    system_prompt = (
        "You are an empathetic academic coach and domain specialist. For each weak subject, construct a concrete, "
        "constructive improvement plan connecting back to the target career. Avoid harsh or discouraging language. "
        "Address: 1. Why this subject matters for the career. 2. Conceptual remediation targets. 3. Active practice strategies. "
        "4. Suggested timeline and curated reference types. Be rigorous, grounded, and encouraging."
    )
    user_prompt = (
        f"Academic Field: {field}\n"
        f"Target Career: {target_career}\n"
        f"Weak Subjects: {', '.join(weak_subjects)}\n\n"
        "Provide a concrete academic improvement roadmap."
    )
    return call_gemini(user_prompt, system_instruction=system_prompt)