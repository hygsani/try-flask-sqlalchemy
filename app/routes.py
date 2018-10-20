from app import app, db
from flask import render_template, url_for, request, redirect
from app.models.contact import Contact

@app.route('/')
def index():
	return render_template('index.html', data='test')

@app.route('/browse')
def browse():
	contacts = db.session.query(Contact).all()

	return render_template('browse.html', title='browse', contacts=contacts)

@app.route('/insert', methods=['GET', 'POST'])
def insert():
	if request.method == 'POST':
		contact = Contact(name=request.form['name'], address=request.form['address'])

		db.session.add(contact)
		db.session.commit()

		return redirect(url_for('index'))

	return render_template('insert.html', title='insert')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
	contact = db.session.query(Contact).filter_by(id=id).first()

	if request.method == 'POST':
		contact.name = request.form['name']
		contact.address = request.form['address']

		db.session.commit()

		return redirect(url_for('browse'))

	return render_template('update.html', title='update', contact=contact)

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