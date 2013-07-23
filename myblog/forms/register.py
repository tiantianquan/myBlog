from flask.ext.wtf import Form, TextField, PasswordField
from flask.ext.wtf import Email, Length, DataRequired
from flask.ext.wtf.html5 import EmailField

class Registerform(Form):
	username = TextField(
		'Username',
		validators=[DataRequired(), Length(min=3, max=20)]
		)

	password = PasswordField(
		'Password',
		validators=[DataRequired(), Length(min=6, max=16)]
		)
	email = EmailField(
		'Email',
		validators=[DataRequired(), Email()]
		)