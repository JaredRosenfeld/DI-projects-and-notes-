# First, we are in a different file, so we need to import the app

import os
import flask
import wtforms
import json
import bz2
from werkzeug.utils import secure_filename
from flask import flash, request, redirect, url_for
# from flask_wtf import file

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

{{form.language.label}}
{{form.language(size=32)}}
{{ form.submit() }}

</form>
"""

list_of_resumes = []


@app.route("/resume", methods=("GET", "POST"))
def resume1():
    from app.Forms import Form
    form = Form()
    if form.validate_on_submit():
        resume_dict = {
            'FirstName': form.first_name.data,
            'LastName': form.last_name.data,
            'Age': form.age.data,
            'Location': form.location.data,
            'Job': form.job.data,
            'Experience': form.experience.data,
            'Language': form.language.data
        }
        list_of_resumes.append(resume_dict)
        return flask.redirect('/resume/choice')
    return flask.render_template_string(form_template, form=form)


@app.route("/resume/red", methods=("GET", "POST"))
def redresume():
    templates = open('app/templates/redresume.html', 'r').read()
    first_name = list_of_resumes[0]['FirstName']
    last_name = list_of_resumes[0]['LastName']
    age = list_of_resumes[0]['Age']
    location = list_of_resumes[0]['Location']
    job = list_of_resumes[0]['Job']
    experience = list_of_resumes[0]['Experience']
    language = list_of_resumes[0]['Language']
    return flask.render_template_string(templates, first_name=first_name,last_name=last_name,age = age,location=location,job=job,experience=experience,language=language)


@app.route("/resume/blue", methods=("GET", "POST"))
def blueresume():
    templates = open('app/templates/blueresume.html', 'r').read()
    first_name = list_of_resumes[0]['FirstName']
    last_name = list_of_resumes[0]['LastName']
    age = list_of_resumes[0]['Age']
    location = list_of_resumes[0]['Location']
    job = list_of_resumes[0]['Job']
    experience = list_of_resumes[0]['Experience']
    language = list_of_resumes[0]['Language']
    return flask.render_template_string(templates, first_name=first_name, last_name=last_name, age=age,
                                        location=location, job=job, experience=experience, language=language)


@app.route("/resume/black", methods=("GET", "POST"))
def blackresume():
    templates = open('app/templates/blackresume.html', 'r').read()
    first_name = list_of_resumes[0]['FirstName']
    last_name = list_of_resumes[0]['LastName']
    age = list_of_resumes[0]['Age']
    location = list_of_resumes[0]['Location']
    job = list_of_resumes[0]['Job']
    experience = list_of_resumes[0]['Experience']
    language = list_of_resumes[0]['Language']
    return flask.render_template_string(templates, first_name=first_name, last_name=last_name, age=age,
                                        location=location, job=job, experience=experience, language=language)


@app.route('/resume/choice',methods=("GET", "POST"))
def choice():
    templates = open('app/templates/cvbase.html', 'r').read()
    return flask.render_template_string(templates)
