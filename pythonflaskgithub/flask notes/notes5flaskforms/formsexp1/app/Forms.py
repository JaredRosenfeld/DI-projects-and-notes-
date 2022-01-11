import flask_wtf
import wtforms

class Form(flask_wtf.FlaskForm):
    firstname     = wtforms.StringField("Firstname",[wtforms.validators.DataRequired()])
    lastname = wtforms.StringField("Lastname",[wtforms.validators.DataRequired()])
    age      = wtforms.StringField("Age",[wtforms.validators.DataRequired()])
    submit   = wtforms.SubmitField("Submit")



my_form = Form()
