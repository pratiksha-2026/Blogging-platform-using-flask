from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# This line configures the database location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# This initializes SQLAlchemy
db = SQLAlchemy(app)

from flaskblog import routes