from YourArchives import db

class UserRoles(db.Model):
    __tablename__ = 'app_user_roles'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('app_users.user_id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('app_roles.role_id', ondelete='CASCADE'))