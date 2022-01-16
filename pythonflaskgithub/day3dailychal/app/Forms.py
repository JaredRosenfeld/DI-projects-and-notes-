import flask_wtf
import wtforms


class Form(flask_wtf.FlaskForm):
    first_name = wtforms.StringField(" First Name", [wtforms.validators.DataRequired()])
    last_name = wtforms.StringField("Last Name", [wtforms.validators.DataRequired()])
    age = wtforms.StringField("Age", [wtforms.validators.DataRequired()])
    location = wtforms.StringField("Location", [wtforms.validators.DataRequired()])
    job = wtforms.StringField("Job", [wtforms.validators.DataRequired()])
    experience = wtforms.StringField("Experience", [wtforms.validators.DataRequired()])
    language = wtforms.StringField("Language")
    template = wtforms.StringField("Template")
    submit = wtforms.SubmitField("Submit")


my_form = Form()
