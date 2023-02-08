from flask_wtf import FlaskForm
from wtforms.fields import BooleanField, DateField, StringField, SelectField,  SubmitField, TextAreaField, TimeField, PasswordField, EmailField
from datetime import datetime
from wtforms.validators import DataRequired, Length, Email, ValidationError

class LoginForm(FlaskForm):

    employee_number = StringField("Employee number", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("Login")
    