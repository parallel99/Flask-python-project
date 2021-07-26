from YourArchives.model import Role
from YourArchives import db

class RoleConfig:

    def __init__(self):
        if not Role.query.filter(Role.name == 'Admin').first():
            db.session.add(Role(name='Admin'))
            db.session.commit()

        if not Role.query.filter(Role.name == 'User').first():
            db.session.add(Role(name='User'))
            db.session.commit()