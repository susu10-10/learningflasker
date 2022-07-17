from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# create a form class
class NamerForm(FlaskForm):
    name = StringField('What is your Name?', 
                        validators=[DataRequired()])
    submit = SubmitField('Continue')


class Register(FlaskForm):
    name = StringField('What is your Name?', 
                        validators=[DataRequired()])
    email = StringField('What is your email?',
                        validators=[DataRequired()])
    submit = SubmitField('Submit')