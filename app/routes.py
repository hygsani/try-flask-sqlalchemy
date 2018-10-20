from app import app, db
from flask import render_template, url_for, request, redirect, session
from app.models.contact import Contact
from app.models.user import User
from app.forms.contact import ContactForm
from app.forms.login import LoginForm

@app.route('/', methods=['GET', 'POST'])
def index():
	if session.get('is_logged_in'):
		return redirect(url_for('home'))

	login_form = LoginForm(request.form)

	if request.method == 'POST' and login_form.validate():
		is_user_exist = db.session.query(User).filter_by(username=login_form.username.data, password=login_form.password.data).first()

		if is_user_exist:
			session['is_logged_in'] = True

			return redirect(url_for('home'))
		else:
			return redirect(url_for('index'))

	return render_template('login.html', title='CRUD', form=login_form)

@app.route('/logout')
def logout():
	session['is_logged_in'] = False

	return redirect(url_for('index'))

@app.route('/home')
def home():
	if not session.get('is_logged_in'):
		return redirect(url_for('index'))

	return render_template('index.html', title='home')

@app.route('/browse')
def browse():
	if not session.get('is_logged_in'):
		return redirect(url_for('index'))

	contacts = db.session.query(Contact).all()

	return render_template('browse.html', title='browse', contacts=contacts)

@app.route('/insert', methods=['GET', 'POST'])
def insert():
	if not session.get('is_logged_in'):
		return redirect(url_for('index'))

	contact_form = ContactForm(request.form)

	if request.method == 'POST' and contact_form.validate():
		contact = Contact(name=contact_form.name.data, address=contact_form.address.data)

		db.session.add(contact)
		db.session.commit()

		return redirect(url_for('index'))

	return render_template('insert.html', title='insert', form=contact_form)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
	if not session.get('is_logged_in'):
		return redirect(url_for('index'))

	contact = db.session.query(Contact).filter_by(id=id).first()
	contact_form = ContactForm(request.form)

	if request.method == 'POST' and contact_form.validate():
		contact.name = contact_form.name.data
		contact.address = contact_form.address.data

		db.session.commit()

		return redirect(url_for('browse'))

	contact_form.id.data = contact.id
	contact_form.name.data = contact.name
	contact_form.address.data = contact.address

	return render_template('update.html', title='update', contact=contact, form=contact_form)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
	if not session.get('is_logged_in'):
		return redirect(url_for('index'))

	contact = db.session.query(Contact).filter_by(id=id).first()

	if request.method == 'POST':
		db.session.delete(contact)
		db.session.commit()

		return redirect(url_for('browse'))

	return render_template('delete.html', title='delete', contact=contact)

@app.route('/show/<int:id>')
def show(id):
	if not session.get('is_logged_in'):
		return redirect(url_for('index'))

	contact = db.session.query(Contact).filter_by(id=id).first()

	return render_template('show.html', title='show', contact=contact)