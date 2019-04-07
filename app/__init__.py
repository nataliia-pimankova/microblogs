# from flask_bootstrap import Bootstrap, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from flask import Flask

from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
# bootstrap = Bootstrap()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    # bootstrap.init_app(app)

    from app import routes
    app.register_blueprint(routes.bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    return app


from app import models
