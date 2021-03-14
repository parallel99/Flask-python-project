from SearchEngine import db
from flask import flash
from SearchEngine.model import User

class RegisterController():

    def register(form):
        if form.validate_on_submit():
            user_to_create = User(username=form.username.data,
                                  email=form.email.data,
                                  set_password=form.password1.data)
            db.session.add(user_to_create)
            db.session.commit()
            flash(f'Successful registration', category='success')
            return True
        if form.errors != {}:  # If there are not errors from validations
            for err_msg in form.errors.values():
                flash(f'There was an error with creating a user: {err_msg}', category='danger')

        return False