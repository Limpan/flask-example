from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.redis import FlaskRedis
from config import config


bootstrap = Bootstrap()
redis = FlaskRedis()


def create_app(config_name):
    """Application factory, see docs_.

    .. _docs: http://flask.pocoo.org/docs/0.10/patterns/appfactories/
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    redis.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
