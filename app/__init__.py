from flask import Flask
from flasgger import Swagger
from .config import Config
from .extensions import db, migrate


def create_app():
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static"
    )
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    swagger = Swagger(app)

    from .views import main
    app.register_blueprint(main)

    return app
