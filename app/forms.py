from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms import DateField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ScraperForm(FlaskForm):
    test_date = DateField('Test Date', validators=[DataRequired()])
    initial_pressure = StringField('Initial Pressure', validators=[DataRequired()])
    final_pressure = StringField('Final Pressure')
    buildup_pressure = StringField('Buildup Pressure')
    water_flow = BooleanField('Water Flow')
    oil_flow = BooleanField('Oil Flow')
    comment = TextAreaField('Comment', validators=[Length(min=0, max=1000)])
    submit = SubmitField('Submit Data')


