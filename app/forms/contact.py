from flask_wtf import Form
from wtforms import StringField, TextAreaField, HiddenField
from wtforms.validators import Length, DataRequired

class ContactForm(Form):
	id = HiddenField('id')
	name = StringField('name', [DataRequired(), Length(min=5, max=50)], render_kw={'placeholder': 'input your name here...'})
	address = TextAreaField('address', [DataRequired(), Length(min=5, max=255)], render_kw={'placeholder': 'input your address here...'})