from sqlalchemy import desc
from flask import render_template, request, redirect, session, g
from flask import Blueprint
from ..models import Account, Topic, db
from ..forms import Registerform, Createform, Loginform

bp = Blueprint('view', __name__)

def get_current_user():
	if 'username' in session and 'password' in session:
		user = Account.query.filter_by(username=session['username']).first()
		if not user:
			return None

		if user.password == session['password']:
			return user
		else:
			return None
	return None

@bp.before_request
def load_current_user():
	g.user = get_current_user()

@bp.route('/')
def show():
	topics = Topic.query.order_by(desc(Topic.create_time))
	return render_template('index.html', topics=topics)

@bp.route('/create', methods=['GET','POST'])
def create():
	if g.user :
		form = Createform()

		if request.method == 'POST':
			title = request.form['title']
			content = request.form['content']
			topic = Topic(title, content)
			db.session.add(topic)
			db.session.commit()
			return redirect('/')
		return render_template('create.html', form=form)		
	

	return redirect('/')

@bp.route('/register', methods=['GET','POST'])
def register():
	form = Registerform()
	if request.method == 'POST':
		session['username'] = request.form['username']
		session['password'] = request.form['password']
		email = request.form['email']
		account = Account(session['username'],session['password'],email)
		db.session.add(account)
		db.session.commit()

		load_current_user()
		return redirect('/')
		

	return render_template('register.html', form=form)

@bp.route('/login', methods=['GET','POST'])
def login():
	form = Loginform()
	error = ''
	if request.method == 'POST':
		session['username'] = request.form['username']
		session['password'] = request.form['password']

		user = get_current_user()
		
		if user:
			return redirect('/')

		if not user:	
			error = 'WRONG ACCOUNT'
	return render_template('login.html', form=form, error=error)

@bp.route('/logout')
def logout():
	if g.user:
		session['username'] = None
		session['password'] = None
	return redirect('/')
















