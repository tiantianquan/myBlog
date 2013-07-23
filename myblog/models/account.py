from .base import db
from datetime import datetime

class Account(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), nullable=False, unique=True)
	password = db.Column(db.String(100), nullable=False)
	email = db.Column(db.String(100), nullable=False, unique=True)
	create_time = db.Column(db.DateTime)

	def __init__(self,username,password,email):
		self.username = username
		self.password = password
		self.email = email.lower()
		self.create_time = datetime.now()
