# First, we are in a different file, so we need to import the app
import flask
import wtforms

from app import app  # app.app is package_name.variable_name

form_template = """
<form method="POST">
{{ form.hidden_tag() }}

{{ form.City_Name.label }}
{{ form.City_Name(size=32) }}

{{ form.City_Country.label }}
{{ form.City_Country(size=32) }}

{{ form.population.label }}
{{ form.population(size=32) }}

{{ form.size.label }}
{{ form.size(size=32) }}

{{ form.submit() }}
</form>
"""


@app.route('/cityform', methods=("GET", "POST"))
def myform1():
    from app.Forms import Form
    form = Form()
    if form.validate_on_submit():  # Check if the form has been filled
        my_length_check(Form,form.City_Name.data)
        name_of_city = form.City_Name.data  # Get
        city_country = form.City_Country.data  # The
        population = form.population.data  # Data
        size = form.size.data

        print("Here is what I got from the form:")
        print("City:", name_of_city)
        print("Country:", city_country)
        print("Population:", population)
        print("Size:", size)
        # Do something with the data

        return flask.redirect('/cityform')
    return flask.render_template_string(form_template, form=form)


def my_length_check(form1, field):
    if len(field) > 15:
        raise wtforms.ValidationError('Field must be less than 15 characters')
