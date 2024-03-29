from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from YourArchives import app, db

app.config.from_object('venv')

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

# This file manages the migrations