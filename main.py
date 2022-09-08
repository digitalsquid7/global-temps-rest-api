import configparser

from flask import Flask
from sqlalchemy import create_engine

from global_temps_rest_api.api_models import CITY_NAMESPACE, API
from global_temps_rest_api.config.env_var_retriever import EnvVarRetriever
from global_temps_rest_api.config.ini_config_retriever import DatabaseConfigRetriever
from global_temps_rest_api.setup import FlaskAppSetupUtil

engine = create_engine(database_config.connection_string)


def main():
    app = Flask(__name__)

    config = configparser.ConfigParser()
    config.read(EnvVarRetriever.retrieve('GLOBAL_TEMPS_CONFIG_FILE_PATH'))
    database_config = DatabaseConfigRetriever.retrieve(config)

    FlaskAppSetupUtil.configure_app(app, database_config)
    FlaskAppSetupUtil.add_namespaces_to_api(API, CITY_NAMESPACE)
    app.run(debug=True)


if __name__ == '__main__':
    main()
