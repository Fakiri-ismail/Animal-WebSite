from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class SingUpForm(FlaskForm):
    fullName = StringField('Full Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password1 = PasswordField('Password', validators=[InputRequired()])
    password2 = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password1', message='Passwords must match')])
    submit = SubmitField('SingUP')