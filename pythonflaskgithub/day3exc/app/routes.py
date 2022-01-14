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
<form method="POST">
{{ form.hidden_tag() }}

*{{ form.City_Name.label }}
{{ form.City_Name(size=32) }}

*{{ form.City_Country.label }}
{{ form.City_Country(size=32) }}

*{{ form.population.label }}
{{ form.population(size=32) }}

*{{ form.size.label }}
{{ form.size(size=32) }}

{{ form.Latitude.label}}
{{ form.Latitude(size=32)}}

{{ form.Longitude.label }}
{{ form.Longitude(size=32)}}

{{ form.Capital.label }}
{{ form.Capital(size=32)}}

{{ form.submit() }}
</form>
"""

list_of_cities = []


@app.route('/cityform', methods=("GET", "POST"))
def myform1():
    from app.Forms import Form
    form = Form()
    if form.validate_on_submit():  # Check if the form has been filled
        my_length_check(Form, form.City_Name.data)
        pop_chec(Form, form.population.data)
        name_of_city = form.City_Name.data  # Get
        city_country = form.City_Country.data  # The
        population = form.population.data  # Data
        size = form.size.data
        Latitude = form.Latitude.data
        longitude = form.Longitude.data
        capital = form.Capital.data

        print("Here is what I got from the form:")
        print("City:", name_of_city)
        print("Country:", city_country)
        print("Population:", population)
        print("Size:", size)
        print("Longitude:", longitude)
        print("Latitude:", Latitude)
        print("Capital:", capital)
        # Do something with the data
        city_dict = {
            'City': name_of_city,
            'Country': city_country,
            'Population': population,
            'Size': size,
            'Longitude': longitude,
            'Latitude': Latitude,
            'Capital': capital}
        list_of_cities.append(city_dict)
        return flask.redirect('/cityform')
    write_to_json(list_of_cities)
    return flask.render_template_string(form_template, form=form)


def my_length_check(form1, field):
    if len(field) > 15:
        raise wtforms.ValidationError('Field must be less than 15 characters')


def pop_chec(form1, field):
    if int(field) <= 0:
        raise wtforms.ValidationError('Population can not be a negative number')

def write_to_json(dict1):
    with open('cities_around_the_world.json', "r+") as cw:
            json.dump(dict1,cw)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/image', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''