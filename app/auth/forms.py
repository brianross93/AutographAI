# Create your forms here.

#Create signup form
# The signup form will have a username, password, and email.
# The username will be unique and the email will be unique.
# The password will be required and the email will be required.

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, DateField, SelectField, SubmitField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError
from wtforms.fields.html5 import DateField
from datetime import datetime

