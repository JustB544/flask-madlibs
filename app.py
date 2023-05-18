from stories import Story, story
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)


def dir_last_updated(folder):
    return str(max(os.path.getmtime(os.path.join(root_path, f))
                   for root_path, dirs, files in os.walk(folder)
                   for f in files))
# credit: MarredCheese at https://stackoverflow.com/questions/41144565/flask-does-not-see-change-in-js-file
# is used to automatically update static files without having to hard refresh the browser for every change :D


@app.route("/")
def main_page():
    """returns main page"""
    return render_template("madlib_form.html", last_updated=dir_last_updated('static'))


@app.route("/story")
def response_page():
    """returns response page"""
    answers = {}
    answers["place"] = request.args["place"]
    answers["noun"] = request.args["noun"]
    answers["verb"] = request.args["verb"]
    answers["adjective"] = request.args["adjective"]
    answers["plural_noun"] = request.args["plural_noun"]
    return render_template("madlib.html", story=story.generate(answers))
