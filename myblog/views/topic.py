from sqlalchemy import desc
from flask import render_template, request, redirect
from flask import Blueprint
from ..models import Topic, db

bp = Blueprint('topic', __name__)

@bp.route('/')
def show():
	topics = Topic.query.order_by(desc(Topic.create_time))
	return render_template('index.html', topics=topics)

@bp.route('/create', methods=['GET','POST'])
def create():
	if request.method == 'POST':
		title = request.form['title']
		content = request.form['content']
		topic = Topic(title, content)
		db.session.add(topic)
		db.session.commit()
		return redirect('/')

	return render_template('create.html')