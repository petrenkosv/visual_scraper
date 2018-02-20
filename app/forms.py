from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import TextAreaField, FloatField
from wtforms import DateField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from wtforms.validators import NumberRange, Length, InputRequired, Optional

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ScraperForm(FlaskForm):
    test_date = DateField('Test Date (e.g. YYYY-MM-DD)',
                          validators=[DataRequired()],
                          render_kw={'autofocus':True})
    initial_pressure = FloatField('Initial Pressure', validators=[InputRequired()])
    final_pressure = FloatField('Final Pressure', validators=[Optional()])
    buildup_pressure = FloatField('Buildup Pressure', validators=[Optional()])
    water_flow = BooleanField('Water Flow')
    oil_flow = BooleanField('Oil Flow')
    comment = TextAreaField('Comment', validators=[Length(min=0, max=1000)])
    submit = SubmitField('Submit Data')


