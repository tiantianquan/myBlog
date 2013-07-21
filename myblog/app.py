
from flask import Flask
from .models import db
from .views import topic
from flask.ext.bootstrap import Bootstrap

def create_app():
	app = Flask(__name__)
	
	app.config.from_pyfile('config.py')
	app.register_blueprint(topic.bp)
	Bootstrap(app)

	db.init_app(app)
	db.app = app
	
	
	return app




