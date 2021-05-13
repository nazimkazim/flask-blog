from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# noinspection SpellCheckingInspection
app.config['SECRET_KEY'] = 'dd26f2b76681eb602fb0d8c3a6ddcf12'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes
