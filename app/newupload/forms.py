# app/newupload/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField

from ..models import Imagedata

class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    startdate = DateField('Start date', format='%Y-%m-%d', validators=[DataRequired()])
    enddate = DateField('End date', format='%Y-%m-%d', validators=[DataRequired()])
    text = StringField('Comments')
    submit = SubmitField('Submit')
  