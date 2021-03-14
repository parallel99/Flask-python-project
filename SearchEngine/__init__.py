from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_assets import Environment, Bundle

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '23e11ad5d944bb0f0ec7c01c'

# Database
db = SQLAlchemy(app)

# Password Encrypt
bcrypt = Bcrypt(app)

# Login manager
login_manager = LoginManager(app)

# scss compiler to css
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('scss/main.scss', 'scss/secondary.scss', filters='pyscss', output='css/style.css')
assets.register('scss_all', scss)

from SearchEngine import routes