from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt           
from flask_login import LoginManager      

app = Flask(__name__)

# You MUST have a SECRET_KEY for login forms to work securely!
# If you don't have this line, add it now:
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# This initializes SQLAlchemy
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)                      # <-- NEW
login_manager = LoginManager(app)         # <-- NEW
login_manager.login_view = 'login'        # <-- NEW (Tells Flask where the login page is)

from flaskblog import routes