from flask_wtf import FlaskForm
from wtforms.validators import data_required
from wtforms import StringField, SubmitField, FloatField


class AddForm(FlaskForm):

    title = StringField('Title', validators=[data_required()])
    author = StringField('Author', validators=[data_required()])
    price = FloatField('Price', default=0)
    submit = SubmitField('Add a New Book')
