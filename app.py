from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

# add routes below ...#

@app.route("/")
def show_questions():
    questions = story.prompts
    return render_template("questions.html", questions=questions)

@app.route("/story")
def result_story():
    words_picked = request.args
    story_result = story.generate(request.args)
    return render_template("story.html", response=story_result, words=words_picked)