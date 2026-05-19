import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

# --- THE SMART DATABASE LOGIC ---
# This line looks to see if Render gave us an internet database
database_url = os.environ.get('DATABASE_URL')

if database_url:
    # If Render DID give us a database, we fix the name and use it
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    # If we are on your PC, it uses your local file
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# --------------------------------------

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from flaskblog import routes