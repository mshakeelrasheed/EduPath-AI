from datetime import datetime
from typing import Dict, Any, List
from src.utils import calculate_readiness_score, call_gemini

def evaluate_progress_update(student_data: Dict[str, Any], previous_assessment: Dict[str, Any]) -> Dict[str, Any]:
    current_metrics = calculate_readiness_score(student_data)
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    prev_score = previous_assessment.get("overall_score", 0) if previous_assessment else 0
    score_delta = current_metrics["overall_score"] - prev_score

    system_prompt = (
        "You are an analytical university progress auditor. Compare the student's previous assessment with their "
        "current updated profile. Identify specific areas of demonstrable growth (projects, skills, academic marks) "
        "and candidly highlight remaining vulnerabilities or gaps (e.g. lack of formal internships, low networking score). "
        "Generate: 1. A succinct 3-4 sentence progress narrative. 2. 3 to 5 prioritized, high-leverage immediate action steps. "
        "Do NOT exaggerate claims. If progress is modest, state so constructively."
    )

    user_prompt = (
        f"Student Field: {student_data.get('profile', {}).get('field')}\n"
        f"Target Career: {student_data.get('profile', {}).get('preferred_career')}\n"
        f"Previous Assessment: {previous_assessment}\n"
        f"Current Computed Metrics: {current_metrics}\n"
        f"Score Delta: {score_delta}\n"
        f"Total Projects: {len(student_data.get('projects', []))}\n"
        f"Total Experiences: {len(student_data.get('experience', []))}\n"
        f"Total Achievements: {len(student_data.get('achievements', []))}"
    )

    ai_critique = call_gemini(user_prompt, system_instruction=system_prompt)

    new_assessment = {
        "date": date_str,
        "overall_score": current_metrics["overall_score"],
        "category_scores": current_metrics,
        "delta": score_delta,
        "ai_analysis": ai_critique,
        "strengths": [
            f"Active academic progression in {student_data.get('profile', {}).get('field')}",
            f"Recorded {len(student_data.get('projects', []))} portfolio projects"
        ],
        "weaknesses": [
            "Continuous hands-on practical expansion required",
            "Professional industry networking footprint requires expansion"
        ],
        "ai_recommendations": [
            "Formalize ongoing project work into public repository or portfolio artifact",
            "Target relevant field competitions or industry certifications",
            "Engage in faculty office hours or professional discipline associations"
        ]
    }
    return new_assessment