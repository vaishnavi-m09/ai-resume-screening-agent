from backend.utils.skill_dictionary import SKILLS


def extract_jd_skills(jd_text):

    found = []

    text = jd_text.lower()

    for skill in SKILLS:

        if skill in text:
            found.append(skill)

    return found