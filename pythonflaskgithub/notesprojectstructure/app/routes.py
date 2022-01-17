import flask
from werkzeug.utils import redirect

from app import app    # app.app is package_name.variable_name
from flask import flash, render_template, url_for


# @app.route("/")
# def home():
#     flash("This is a flashed message.")
#     flash("Another message bee boo.")
#     return render_template("home.html")

@app.route("/")
def home():
    flash("Error", "error")
    flash("Logged in successfully", "success")
    return render_template("home.html")


@app.route('/flask1')
def flash1():
    flash("red","color")
    flash("car", "machine" )
    return render_template('home1.html')

