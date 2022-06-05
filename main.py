from flask import Flask

from utils import get_all_candidates, format_candidates, get_candidates_id, get_candidates_skills

app = Flask(__name__)

@app.route('/')
def page_home():
    """Главная страница"""
    candidates: list[dict] = get_all_candidates()
    result:str = format_candidates(candidates)
    return result

@app.route('/candidat/<int:uid>')
def page_candidate(uid):
    """Поиск кандидата по id"""
    candidate: dict = get_candidates_id(uid)
    result = f'<img src="{candidate["picture"]}">'
    result += format_candidates([candidate])
    return result

@app.route('/skills/<skill>')
def page_skills(skill):
    """Поиск по навыку"""
    skill_lower = skill.lower()
    candidate: list[dict] = get_candidates_skills(skill_lower)
    result = format_candidates(candidate)
    return result


app.run()