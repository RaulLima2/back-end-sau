from flask import Flask, SQLAlchemy
from src.routes.usuario import UsuarioRoute


def create_app(db:SQLAlchemy) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_envvar('config')
    app.config.from_object('config')
    db.init_app(app)

    app.register_blueprint(UsuarioRoute)

    return app