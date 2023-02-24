from flask import Flask, render_template

import onegin_utils

app = Flask(__name__)

data = onegin_utils.load_candidates_from_json("C:/Users/Professional/Desktop/Python/skypro/candidates.json")


@app.route('/')
def main_page():
    return render_template("candidates.html", candidates=data)


@app.route('/candidate/<int:x>')
def single_page(x):
    return render_template("card.html", candidate=onegin_utils.get_candidate(x))


@app.route('/candidate/<candidate_name>')
def search_page(candidate_name):
    return render_template("search.html", candidates=onegin_utils.get_candidates_by_name(candidate_name),
                           length=len(onegin_utils.get_candidates_by_name(candidate_name)))


@app.route('/skill/<skill_name>')
def search_skill(skill_name):
    return render_template("skill.html", X=skill_name, candidates=onegin_utils.get_candidates_by_skill(skill_name),
                           length=len(onegin_utils.get_candidates_by_skill(skill_name)))


app.run()
