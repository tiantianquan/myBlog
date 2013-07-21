from myblog.app import create_app
from myblog.models import db


app = create_app()

db.create_all()

if __name__ == '__main__':


	app.run(port=1234,debug=True)