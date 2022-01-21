from flask_wtf import FlaskForm
from wtforms.validators import data_required
from wtforms import StringField, SubmitField

class NewsForm(FlaskForm):
    title = StringField('Title', validators = [data_required()])
    description = StringField('Description', validators = [data_required()])
    source = StringField('Source', validators = [data_required()])
    submit = SubmitField('Submit News to database')