from YourArchives import db
from flask import flash
from YourArchives.model import User, Role, UserRoles
from datetime import datetime

class RegisterController():

    def register(form):
        if form.validate_on_submit():
            user_role = Role.query.filter_by(name='User').first()
            user_to_create = User(username=form.username.data,
                                  email=form.email.data,
                                  set_password=form.password1.data,
                                  created_at=datetime.now())
            user_to_create.roles.append(user_role)

            db.session.add(user_to_create)
            db.session.commit()
            flash(f'Successful registration', category='success')
            return True
        if form.errors != {}:  # If there are not errors from validations
            for err_msg in form.errors.values():
                flash(f'There was an error with creating a user: {err_msg}', category='danger')

        return False