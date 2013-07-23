from flask.ext.wtf import Form, TextField, TextAreaField
from flask.ext.wtf import DataRequired, Length

class Createform(Form):
	title = TextField(
		'Title',
		validators=[DataRequired(), Length(max=100)]
		)
	content = TextAreaField('Content')
