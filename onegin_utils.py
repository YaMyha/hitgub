import json


def load_candidates_from_json(path: str) -> list:
    with open(path, encoding='utf-8') as jsn:
        return json.load(jsn)


def get_candidate(candidate_id):
    list_of_candidates = load_candidates_from_json("C:/Users/Professional/Desktop/Python/skypro/candidates.json")
    return list_of_candidates[candidate_id-1]


def get_candidates_by_name(candidate_name):
    list_of_candidates = load_candidates_from_json("C:/Users/Professional/Desktop/Python/skypro/candidates.json")
    result = []
    for candidate in list_of_candidates:
        if candidate_name.lower() == candidate["name"].lower():
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name):
    list_of_candidates = load_candidates_from_json("C:/Users/Professional/Desktop/Python/skypro/candidates.json")
    result = []
    for candidate in list_of_candidates:
        if skill_name.lower() in candidate["skills"].lower().split(", "):
            result.append(candidate)
    return result
