import hashlib
import json
import os
from typing import Dict, Any, List

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "students")
CREDENTIALS_FILE = os.path.join(os.path.dirname(DATA_DIR), "credentials.json")

def ensure_data_directory() -> None:
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(DATA_DIR), exist_ok=True)

def get_student_file_path(student_id: str) -> str:
    ensure_data_directory()
    sanitized_id = "".join([c for c in student_id if c.isalnum() or c in ("_", "-")])
    return os.path.join(DATA_DIR, f"{sanitized_id}.json")

def load_student_data(student_id: str) -> Dict[str, Any]:
    path = get_student_file_path(student_id)
    if not os.path.exists(path):
        return get_default_student_schema(student_id)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return get_default_student_schema(student_id)

def save_student_data(student_id: str, data: Dict[str, Any]) -> bool:
    ensure_data_directory()
    path = get_student_file_path(student_id)
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception:
        return False

def list_all_students() -> List[str]:
    ensure_data_directory()
    students = []
    for fname in os.listdir(DATA_DIR):
        if fname.endswith(".json"):
            students.append(fname[:-5])
    return sorted(students)

# ----------------- CREDENTIALS & AUTHENTICATION -----------------

def hash_passcode(passcode: str) -> str:
    return hashlib.sha256(passcode.strip().encode("utf-8")).hexdigest()

def load_credentials() -> Dict[str, str]:
    ensure_data_directory()
    if not os.path.exists(CREDENTIALS_FILE):
        default_creds = {}
        save_credentials(default_creds)
        return default_creds
    try:
        with open(CREDENTIALS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_credentials(creds: Dict[str, str]) -> None:
    ensure_data_directory()
    with open(CREDENTIALS_FILE, "w", encoding="utf-8") as f:
        json.dump(creds, f, indent=2)

def register_user(student_id: str, passcode: str) -> bool:
    creds = load_credentials()
    clean_id = "".join([c for c in student_id.strip().lower() if c.isalnum() or c in ("_", "-")])
    if not clean_id or clean_id in creds:
        return False
    creds[clean_id] = hash_passcode(passcode)
    save_credentials(creds)
    return True

def verify_user(student_id: str, passcode: str) -> bool:
    creds = load_credentials()
    clean_id = student_id.strip().lower()
    return creds.get(clean_id) == hash_passcode(passcode)

# ----------------- DEFAULT SCHEMA -----------------

def get_default_student_schema(student_id: str) -> Dict[str, Any]:
    return {
        "profile": {
            "student_id": student_id,
            "name": "",
            "education_level": "Undergraduate",
            "university": "",
            "degree": "",
            "field": "General",
            "current_year": "Year 1",
            "current_semester": "Semester 1",
            "interests": [],
            "career_goals": "",
            "preferred_career": "",
            "weak_areas": []
        },
        "academic_records": [],
        "skills": [],
        "projects": [],
        "experience": [],
        "certifications": [],
        "activities": [],
        "achievements": [],
        "saved_opportunities": [],
        "baseline_assessment": None,
        "assessment_history": [],
        "roadmap": {
            "year_1": {"title": "Year 1: Foundation & Discovery", "tasks": []},
            "year_2": {"title": "Year 2: Skill Application & Exploration", "tasks": []},
            "year_3": {"title": "Year 3: Practical Specialization & Experience", "tasks": []},
            "year_4": {"title": "Year 4: Capstone & Career Transition", "tasks": []}
        }
    }