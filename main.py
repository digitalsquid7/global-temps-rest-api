import configparser

from flask import Flask
from flask_restx import Resource
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from werkzeug.middleware.proxy_fix import ProxyFix

from global_temps_rest_api.api_models import api, city_model
from global_temps_rest_api.config import DatabaseConfigRetriever
from global_temps_rest_api.repositories import CityRepository
from global_temps_rest_api.schemas import CitySchema
from global_temps_rest_api.sql import db
from global_temps_rest_api.util import EnvVarUtil

config = configparser.ConfigParser()
config.read(EnvVarUtil.get_required_env_var('CONFIG_FILE_PATH'))
database_config = DatabaseConfigRetriever.retrieve(config)

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.config['SQLALCHEMY_DATABASE_URI'] = database_config.connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api.init_app(app)

engine = create_engine(database_config.connection_string)

city_namespace = api.namespace('city', description=' A list of cities that have global temperature data.')


@city_namespace.route('')
class Cities(Resource):

    def __init__(self, *args, **kwargs):
        self.city_repo = CityRepository(engine)
        super().__init__(*args, **kwargs)

    @city_namespace.marshal_with(city_model)
    def get(self):
        """Test to see if it works"""
        city = self.city_repo.read()
        return CitySchema(many=True).dump(city)


@city_namespace.route('/<int:id>')
@city_namespace.response(404, 'Todo not found')
@city_namespace.param('id', 'The task identifier')
class Cities(Resource):

    def __init__(self, *args, **kwargs):
        self.city_repo = CityRepository(engine)
        super().__init__(*args, **kwargs)

    @city_namespace.marshal_with(city_model)
    def get(self, id):
        """Test to see if it works"""
        city = self.city_repo.read()
        return CitySchema(many=True).dump(city)


if __name__ == '__main__':
    app.run(debug=True)
