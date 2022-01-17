
from app import app    # app.app is package_name.variable_name
from flask import flash, render_template


@app.route("/to")
def home():
    flash("This is a flashed message.")
    return render_template("templates/notes.html")