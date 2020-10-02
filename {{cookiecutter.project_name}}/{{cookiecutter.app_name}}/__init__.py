import os

import click
from flask import Flask, jsonify

from {{cookiecutter.app_name}}.config import app_config
from {{cookiecutter.app_name}}.controllers import *
from {{cookiecutter.app_name}}.extends.error import HttpError
from {{cookiecutter.app_name}}.extensions import db, migrate, cors
from {{cookiecutter.app_name}}.middlewares import before_request
from {{cookiecutter.app_name}}.models.database import *

def create_app(config_name: str = None) -> Flask:
    """
    :param config_name: str in ['development', 'production', 'testing']
    """
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    register_errorhandler(app)
    register_blueprints(app)
    register_extensions(app)
    register_commands(app)
    register_middleware(app)

    return app


def register_errorhandler(app: Flask):
    @app.errorhandler(HttpError)
    def handle_http_error(error: HttpError):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response


def register_blueprints(app: Flask):
    app.register_blueprint(user_bp)


def register_extensions(app: Flask):
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)


def register_middleware(app: Flask):
    app.before_request(before_request)


def register_commands(app: Flask):
    @app.cli.command()
    def initdb():
        """
        初始化数据库
        """
        db.create_all()
        db.session.commit()
        click.echo('Initialized database.')

    @app.cli.command()
    def dropdb():
        """
        清空数据表
        """
        click.confirm('This operation will delete the database, do you want to continue?', abort=True)
        db.drop_all()
        click.echo('Drop tables.')
        db.create_all()
        db.session.commit()
        click.echo('Initialized database.')

    @app.cli.command()
    def forge():
        """
        向数据库中插入模拟数据
        """
        pass
