# First, we are in a different file, so we need to import the app
import flask
from app import app    # app.app is package_name.variable_name
from flask import flash, render_template


@app.route("/")
def home():
    flash("This is a flashed message.")
    return render_template("notes.html")