from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class LoginForm(FlaskForm):
	username = StringField('username',validators=[Required()])
	password = StringField('password', validators=[Required()])
	submit = SubmitField("submit")
