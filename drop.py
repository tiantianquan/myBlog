from myblog.app import create_app
from myblog.models import db


app = create_app()

db.drop_all()