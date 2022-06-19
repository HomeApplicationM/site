import os
from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import PersonOfInterest, User

from app import create_app, db


# app.config.from_object(os.environ['APP_SETTINGS'])

# app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(
        app=app,
        db=db,
        User=User,
        PersonOfInterest=PersonOfInterest
        )


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host="0.0.0.0"))

if __name__ == '__main__':
    manager.run()

