from app import app, db
from flask import render_template, url_for, request, redirect
from app.models.contact import Contact
from app.forms.contact import ContactForm

@app.route('/')
def index():
	return render_template('index.html', title='CRUD')

@app.route('/browse')
def browse():
	contacts = db.session.query(Contact).all()

	return render_template('browse.html', title='browse', contacts=contacts)

@app.route('/insert', methods=['GET', 'POST'])
def insert():
	contact_form = ContactForm(request.form)

	if request.method == 'POST' and contact_form.validate():
		contact = Contact(name=contact_form.name.data, address=contact_form.address.data)

		db.session.add(contact)
		db.session.commit()

		return redirect(url_for('index'))

	return render_template('insert.html', title='insert', form=contact_form)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
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
	contact = db.session.query(Contact).filter_by(id=id).first()

	if request.method == 'POST':
		db.session.delete(contact)
		db.session.commit()

		return redirect(url_for('browse'))

	return render_template('delete.html', title='delete', contact=contact)

@app.route('/show/<int:id>')
def show(id):
	contact = db.session.query(Contact).filter_by(id=id).first()

	return render_template('show.html', title='show', contact=contact)