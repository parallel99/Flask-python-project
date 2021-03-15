from YourArchives.model import User
from flask_login import login_user
from flask import flash

class LoginController():

    def Login(form):
        if form.validate_on_submit():
            attempted_user = User.query.filter_by(username=form.username.data).first()

            if attempted_user and attempted_user.check_password_correction(
                    attempted_password=form.password.data):
                login_user(attempted_user)
                flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
                return True
            else:
                flash('Username and the password are not match! Please try again', category='danger')

        return False