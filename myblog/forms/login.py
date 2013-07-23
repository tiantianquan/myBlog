from flask.ext.wtf import Form, TextField, PasswordField
from flask.ext.wtf import Length, DataRequired


class Loginform(Form):
	username = TextField(
		'Username',
		validators=[DataRequired(), Length(min=3, max=20)]
		)

	password = PasswordField(
		'Password',
		validators=[DataRequired(), Length(min=6, max=16)]
		)