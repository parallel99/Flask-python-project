from YourArchives import db

class Role(db.Model):
    __tablename__ = 'app_roles'

    id = db.Column(db.Integer(), primary_key=True, name="role_id")
    name = db.Column(db.String(50), unique=True)