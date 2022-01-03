import flask
from flask import Flask
from flask import render_template_string, render_template
import markdown
import markdown.extensions.fenced_code

app = flask.Flask(__name__)

@app.route("/main")
def lesson():
    read_me = open('chapter.md', 'r')
    temp_string = markdown.markdown(read_me.read(), extensions=["fenced_code"])
    return temp_string

@app.route('/main/lesson')
def ex():
    read_me = open('exercises.md', 'r')
    temp_string = markdown.markdown(read_me.read(), extensions=["fenced_code"])
    return temp_string

if __name__ == "__main__":
    app.run(debug=True,port=5000)