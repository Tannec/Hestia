import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo, Email, Length


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    surname = StringField("Surname", validators=[DataRequired()])
    address = StringField("Address")
    email = StringField("Email", validators=[DataRequired(), Email()])
    shortname = StringField("Short name - login")
    password = StringField("Password", validators=[DataRequired()])
    rep_password = StringField("Repeat password", validators=[DataRequired(),
                                                              EqualTo('password',
                               message="Passwords must match")])
    submit = SubmitField("Submit")


class FinishRegistration(FlaskForm):
    code = StringField("Code", validators=[DataRequired()])
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    shortname = StringField('Short name - login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')


class DialogForm(FlaskForm):
    input_line = TextAreaField('Type your message there', validators=[DataRequired(), Length(min=1, max=500)])
    submit = SubmitField('Send')

