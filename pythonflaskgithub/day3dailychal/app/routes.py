# First, we are in a different file, so we need to import the app

import os
import flask
import wtforms
import json
import bz2
from werkzeug.utils import secure_filename
from flask import flash, request, redirect, url_for
from flask_wtf import file

from app import app  # app.app is package_name.variable_name
UPLOAD_FOLDER = 'images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

form_template = """
<form method= "POST">
{{form.hidden_tag()}}

{{ form.first_name.label}}
{{form.first_name(size = 32)}}

{{form.last_name.label}}
{{form.last_name(size=32)}}

{{form.age.label}}
{{form.age(size=32)}}

{{form.location.label}}
{{form.location(size=32)}}

{{form.job.label}}
{{form.job(size=32)}}

{{form.experience.label}}
{{form.experience(size=32)}}

{{form.language.label)}}
{{form.language(size=32)}}


</form>
"""
# {{ form.submit() }}
list_of_resumes = []

@app.route("/resume",METHODS = ("GET","POST"))
def resume1():
    templates = open('cvbase.html', 'r').read()
    from app.Forms import Form
    form = Form()
    if form.validate_on_submit():
        resume_dict = {
            'FirstName' : form.first_name.data,
            'LastName' : form.last_name.data,
            'Age' : form.age.data,
            'Location' : form.location.data,
            'Job' : form.job.data,
            'Experience' : form.experience.data,
            'Language' : form.language.data
        }
        list_of_resumes.append(resume_dict)
    return flask.render_template_string(templates, form_template = form_template, form = form)

@app.route("/resume/red", METHODS = ("GET","POST"))
def redresume():
    templates = open('redresume.html','r').read()
    from app.Forms import Form
    form = Form()
    red_resume_dict = {
        'FirstName': form.first_name.data,
        'LastName': form.last_name.data,
        'Age': form.age.data,
        'Location': form.location.data,
        'Job': form.job.data,
        'Experience': form.experience.data,
        'Language': form.language.data
    }
    return flask.render_template_string(templates,dict1 = red_resume_dict)

@app.route("/resume/blue", METHODS = ("GET","POST"))
def blueresume():
    templates = open('blueresume.html','r').read()
    from app.Forms import Form
    form = Form()
    blue_resume_dict = {
        'FirstName': form.first_name.data,
        'LastName': form.last_name.data,
        'Age': form.age.data,
        'Location': form.location.data,
        'Job': form.job.data,
        'Experience': form.experience.data,
        'Language': form.language.data
    }
    return flask.render_template_string(templates,dict1 = blue_resume_dict)

@app.route("/resume/black", METHODS = ("GET","POST"))
def blackresume():
    templates = open('blackresume.html','r').read()
    from app.Forms import Form
    form = Form()
    black_resume_dict = {
        'FirstName': form.first_name.data,
        'LastName': form.last_name.data,
        'Age': form.age.data,
        'Location': form.location.data,
        'Job': form.job.data,
        'Experience': form.experience.data,
        'Language': form.language.data
    }
    return flask.render_template_string(templates,dict1 = black_resume_dict)