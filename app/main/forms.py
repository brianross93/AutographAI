# Create your forms here.

# Creating forms for the user to enter in their prompt/thesis they want to write an essay for.
# We also need to enter a user id to save the prompt/thesis in the database.

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, DateField, SelectField, SubmitField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError
from wtforms.fields.html5 import DateField
from datetime import datetime



