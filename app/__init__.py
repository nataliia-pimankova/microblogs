# from flask_bootstrap import Bootstrap, current_app


from flask import Flask

from config import Config


# bootstrap = Bootstrap()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # bootstrap.init_app(app)

    # from . import previews
    # app.register_blueprint(previews.bp)

    from app import routes
    app.register_blueprint(routes.bp)

    return app

