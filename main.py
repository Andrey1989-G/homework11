from flask import Flask, render_template

from utils import *


if __name__ == '__main__':

    app = Flask(__name__)

    @app.route('/')
    def page_with_candidates():
        """
        выводим список всех кандидатов
        :return: страницу с ссылками на кандидатов
        """
        candidates = load_candidates()
        return render_template('list.html', candidates=candidates)


    @app.route('/candidate/<int:x>/')
    def page_candidate(x):
        candidate = get_by_pk(x)
        return render_template('single.html', candidate=candidate)


    @app.route('/search/<name>/')
    def search_by_name(name):
        candidates = get_by_name(name)
        return render_template('search.html', candidates=candidates)


    @app.route('/skill/<skill>/')
    def search_by_skill(skill):
        candidates = get_by_skill(skill)
        return render_template('skill.html', candidates=candidates)


    app.run(debug=True)