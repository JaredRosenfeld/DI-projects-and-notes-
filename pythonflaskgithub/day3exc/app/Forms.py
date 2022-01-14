import flask_wtf
import wtforms

class Form(flask_wtf.FlaskForm):
    City_Name     = wtforms.StringField("City Name",[wtforms.validators.DataRequired()])
    City_Country = wtforms.StringField("City Country",[wtforms.validators.DataRequired()])
    population      = wtforms.StringField("Population",[wtforms.validators.DataRequired()])
    size      = wtforms.StringField("Size",[wtforms.validators.DataRequired()])
    Latitude = wtforms.StringField("Latitude")
    Longitude = wtforms.StringField("Longitude")
    Capital = wtforms.BooleanField("Capital")
    submit   = wtforms.SubmitField("Submit")



my_form = Form()
