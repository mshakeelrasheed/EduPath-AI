from typing import Dict, Any, List

def detect_automatic_milestones(student_data: Dict[str, Any]) -> List[str]:
    milestones = []
    projects = student_data.get("projects", [])
    completed_projects = [p for p in projects if str(p.get("status", "")).lower() == "completed"]
    
    if len(completed_projects) >= 5:
        milestones.append("🎉 Milestone Unlocked: Completed 5+ career-aligned projects!")
    elif len(completed_projects) >= 1:
        milestones.append("🚀 First Step: Successfully delivered your first completed practical project!")

    experiences = student_data.get("experience", [])
    internships = [e for e in experiences if "intern" in str(e.get("type", "")).lower() or "intern" in str(e.get("role", "")).lower()]
    if internships:
        milestones.append("💼 Professional Milestone: Recorded first industrial or research internship!")

    achievements = student_data.get("achievements", [])
    competitions = [a for a in achievements if "winner" in str(a.get("type", "")).lower() or "finalist" in str(a.get("title", "")).lower()]
    if competitions:
        milestones.append("🏆 Competitive Excellence: Secured recognition in a verified academic/domain competition!")

    history = student_data.get("assessment_history", [])
    if len(history) >= 2:
        last_score = history[-1].get("overall_score", 0)
        first_score = history[0].get("overall_score", 0)
        if last_score > first_score:
            milestones.append(f"📈 Sustained Growth: Improved overall Career Readiness score by +{last_score - first_score} points since baseline!")

    return milestones