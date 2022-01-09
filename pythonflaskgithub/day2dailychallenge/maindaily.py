import flask
from flask import request
from flask import render_template_string, render_template



app = flask.Flask(__name__)

@app.route('/homepage')
def main():
    return render_template('main.html')

@app.route('/homepage/blue')
def blue():
    return render_template('blue.html')

@app.route('/homepage/yellow')
def yellow():
    css1 = open('static/yellow.css', 'r').read()
    temp1 = open('templates/yellow.html','r').read()
    return flask.render_template_string(temp1, css1 = css1)

@app.route('/homepage/red')
def red():
    css1 = open('static/red.css', 'r').read()
    temp1 = open('templates/red.html','r').read()
    return flask.render_template_string(temp1, css1 = css1)

@app.route('/homepage/green')
def green():
    css1 = open('static/green.css', 'r').read()
    temp1 = open('templates/green.html','r').read()
    return flask.render_template_string(temp1, css1 = css1)


if __name__ == "__main__":
    app.run(debug=True,port=5000)