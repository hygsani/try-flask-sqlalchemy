from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import Length, DataRequired

class LoginForm(Form):
	username = StringField('username', [DataRequired(), Length(min=5, max=30)], render_kw={'placeholder': 'your username'})
	password = StringField('password', [DataRequired(), Length(min=5, max=100)], render_kw={'placeholder': 'your password'})