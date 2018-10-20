from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e8be6c76f90f01893eedc58ee07c65fcc1e4339b1a854dc1edc9969402a84bc2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost/contact'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app import routes