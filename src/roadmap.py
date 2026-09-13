import json
from typing import Dict, Any
from src.utils import call_gemini

def generate_adaptive_roadmap(student_data: Dict[str, Any], catalog_context: str = "") -> Dict[str, Any]:
    profile = student_data.get("profile", {})
    existing_roadmap = student_data.get("roadmap", {})
    
    system_instruction = (
        "You are a university academic dean and career roadmapping architect. "
        "Construct a cohesive 4-Year Academic and Career Roadmap adapted specifically to the student's academic field, "
        "current stage, strengths, and career ambitions. "
        "IMPORTANT: The roadmap must NOT default to software/coding if the student is in Business, Biology, Arts, or Engineering. "
        "Adapt activities: e.g., Case competitions for Business, Lab fellowships for Biology, Design reviews for Arts. "
        "Preserve existing completed tasks if valid. Return ONLY valid JSON with keys year_1, year_2, year_3, year_4. "
        "Structure each year with: {\"title\": \"Year X: Theme\", \"tasks\": [{\"id\": \"t_...\", \"task\": \"Descriptive action\", \"status\": \"Not Started\"}]}"
    )

    user_prompt = (
        f"Field of Study: {profile.get('field')}\n"
        f"Current Academic Level: {profile.get('current_year')}, {profile.get('current_semester')}\n"
        f"Target Career: {profile.get('preferred_career') or profile.get('career_goals')}\n"
        f"Interests: {', '.join(profile.get('interests', []))}\n"
        f"Existing Roadmap State: {json.dumps(existing_roadmap)}\n"
        f"University Catalog Reference: {catalog_context[:800] if catalog_context else 'None'}"
    )

    response = call_gemini(user_prompt, system_instruction=system_instruction, response_mime_type="application/json")
    cleaned = response.replace("```json", "").replace("```", "").strip()
    try:
        parsed = json.loads(cleaned)
        if "year_1" in parsed and "year_4" in parsed:
            # Reconcile completed statuses from prior roadmap
            for yk in ["year_1", "year_2", "year_3", "year_4"]:
                if yk in existing_roadmap and yk in parsed:
                    old_tasks = {t.get("task"): t.get("status") for t in existing_roadmap[yk].get("tasks", [])}
                    for new_t in parsed[yk].get("tasks", []):
                        if new_t.get("task") in old_tasks and old_tasks[new_t.get("task")] == "Completed":
                            new_t["status"] = "Completed"
            return parsed
    except Exception:
        pass
    return existing_roadmap