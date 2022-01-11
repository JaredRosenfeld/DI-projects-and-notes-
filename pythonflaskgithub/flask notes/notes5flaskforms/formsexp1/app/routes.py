# First, we are in a different file, so we need to import the app
import flask
from app import app    # app.app is package_name.variable_name



@app.route("/")
def index():
    posts = [
        {"author":"John", "body":"I love python"},
        {"author":"Fish", "body":"I love water"},
        {"author":"Herpetolog", "body":"I love pythons"},
    ]
    return flask.render_template('index.html',posts=posts)

form_template = """
<form method="POST">
{{ form.hidden_tag() }}

{{ form.firstname.label }}
{{ form.firstname(size=32) }}

{{ form.lastname.label }}
{{ form.lastname(size=32) }}

{{ form.age.label }}
{{ form.age(size=240) }}

{{ form.submit() }}
</form>
"""
@app.route('/myform')
def myform():
    from app.Forms import Form
    form = Form()
    return flask.render_template_string(form_template, form=form)

@app.route('/myform', methods=("GET","POST"))
def myform1():
    from app.Forms import Form
    form = Form()
    if form.validate_on_submit(): # Check if the form has been filled

        firstname = form.firstname.data # Get
        lastname = form.lastname.data #   The
        age      = form.age.data      #     Data

        print("Here is what I got from the form:")
        print("firstname:", firstname)
        print("Lastname:", lastname)
        print("Age:", int(age))
        # Do something with the data

        return flask.redirect('/')
    return flask.render_template_string(form_template, form=form)