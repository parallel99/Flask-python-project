from YourArchives import bcrypt
from flask_login import UserMixin
from YourArchives import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'app_users'

    id = db.Column(db.Integer(), primary_key=True, name="user_id")
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=60), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=128), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime())
    is_active = db.Column(db.Integer(), default=1)
    questions = db.relationship('Question', lazy=True)
    answers = db.relationship('Answer', lazy=True)
    roles = db.relationship('Role', secondary='app_user_roles', backref=db.backref('role', lazy='dynamic'))

    @property
    def password(self):
        return self.password

    @password.setter
    def set_password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        if bcrypt.check_password_hash(self.password_hash, attempted_password):
            return True