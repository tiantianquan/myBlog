from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class Topic(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	content = db.Column(db.Text)
	create_time = db.Column(db.DateTime)


	def __init__(self,title,content):
		self.title = title
		self.content = content
		self.create_time = datetime.now()