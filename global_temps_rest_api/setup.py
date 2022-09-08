from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from global_temps_rest_api.config.ini_config_retriever import DatabaseConfig
from main import database_config


class FlaskAppSetupUtil:

    @staticmethod
    def configure_app(app, database_config: DatabaseConfig):
        app.config['SQLALCHEMY_DATABASE_URI'] = database_config.connection_string
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = database_config.track_modifications

    @staticmethod
    def add_namespaces_to_api(api, *name_spaces):
        for name_space in name_spaces:
            api.add_namespace(name_space)

    @staticmethod
    def initiate_app_components(app, db, api):
        db.init_app(app)
        api.init_app(app)


class DatabaseSetupUtil:

    @staticmethod
    def create_engine():
        return create_engine(database_config.connection_string)

    @staticmethod
    def create_database(engine):
        if not database_exists(engine.url):
            create_database(engine.url)

    @staticmethod
    def create_tables(app: Flask, db: SQLAlchemy):
        with app.app_context():
            db.create_all()
            db.session.commit()
