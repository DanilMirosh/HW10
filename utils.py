import json


def load_json() -> list[dict]:
    with open('candidates.json', 'r', encoding='utf-8') as f:
        candidates = json.load(f)
        return candidates


def format_candidates(candidates) -> str:
    result = '<pre>'

    for candidate in candidates:
        result += f"""
            {candidate['name']}\n
            {candidate['position']}\n
            {candidate['skills']}\n
        """
        result += "</pre>"
        return result


def get_all_candidates() -> list[dict]:
    return load_json()


def get_candidates_id(uid: int) -> dict | None:
    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate['id'] == uid:
            return candidate
    return None


def get_candidates_skills(skill: str) -> list[dict]:
    candidates = get_all_candidates()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)
        return result
