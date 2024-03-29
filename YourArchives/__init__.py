import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_assets import Environment, Bundle

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Database (ORM)
db = SQLAlchemy(app)

# Password Encrypt
bcrypt = Bcrypt(app)

# Login manager
login_manager = LoginManager(app)

# scss compiler to css
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('scss/main.scss', 'scss/ImageContainer.scss', filters='pyscss', output='css/style.css')
assets.register('scss_all', scss)

from YourArchives import routes
