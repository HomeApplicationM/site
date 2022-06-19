# from venv import create
from flask import Flask
# import config
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import Security, login_required, SQLAlchemySessionUserDatastore


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'login.login'

admin = Admin()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)
        login.init_app(app)
        admin.init_app(app)

        from app.models import User
        @login.user_loader
        def load_user(id):
            return User.query.get(id)

        db.create_all()
        admin.add_view(ModelView(User, db.session))

    from app.routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.routes.login import login_bp as login_blueprint
    app.register_blueprint(login_blueprint)

    from app.routes.birthdays import birthdays_bp as birthdays_blueprint
    app.register_blueprint(birthdays_blueprint)

    return app

if __name__ == "__main__":
    create_app().run(host='0.0.0.0')
