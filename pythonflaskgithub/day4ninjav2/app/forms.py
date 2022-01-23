from flask_wtf import FlaskForm
from wtforms.validators import data_required
from wtforms import StringField, SubmitField, BooleanField


class Todolist1(FlaskForm):
    todo = StringField('Item to do', validators=[data_required()])
    submit1 = SubmitField('Add the item')
