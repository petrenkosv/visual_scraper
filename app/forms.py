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
    test_date = DateField('Test Date (e.g. YYYY-MM-DD)', validators=[DataRequired()])
    init_bradenhead_pressure = FloatField('Initial Bradenhead Pressure', validators=[InputRequired()], render_kw = {'autofocus':True})
    init_intermediate_1_pressure = FloatField('Initial Intermediate 1 Pressure', validators=[Optional()])
    init_intermediate_2_pressure = FloatField('Initial Intermediate 2 Pressure', validators=[Optional()])
    init_casing_pressure = FloatField('Initial Casing Pressure', validators=[Optional()])
    init_tubing_pressure = FloatField('Initial Tubing Pressure', validators=[Optional()])
    fin_bradenhead_pressure = FloatField('Final Bradenhead Pressure', validators=[Optional()])
    fin_intermediate_1_pressure = FloatField('Final Intermediate 1 Pressure', validators=[Optional()])
#    fin_intermediate_2_pressure = FloatField('Final Intermediate 2 Pressure', validators=[Optional()])
    fin_casing_pressure = FloatField('Final Casing Pressure', validators=[Optional()])
    bradenhead_buildup_pressure = FloatField('Bradenhead Buildup Pressure', validators=[Optional()])
    intermediate_1_buildup_pressure = FloatField('Intermediate 1 Buildup Pressure', validators=[Optional()])
#    intermediate_2_buildup_pressure = FloatField('Intermediate 2 Buildup Pressure', validators=[Optional()])
    shut_in = BooleanField('Shut In')
    water_flow = BooleanField('Water Flow')
    oil_flow = BooleanField('Oil Flow')
    comment = TextAreaField('Comment', validators=[Length(min=0, max=1000)])
    submit = SubmitField('Submit Data')


