from YourArchives import app
from flask import render_template, redirect, url_for, flash
from YourArchives.model import User, Item
from YourArchives.form import RegisterForm, LoginForm
from YourArchives.controller import RegisterController, LoginController
from YourArchives import db
from flask_login import logout_user

# @app.route('/')
# This name is decorator and you can find it: https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all();
    return render_template('market.html', items=items)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if RegisterController.register(form):
        return redirect(url_for('home_page'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if LoginController.Login(form):
        return redirect(url_for('market_page'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))