from flask_restx import Resource, Namespace
from flask_restx import Api, fields

from global_temps_rest_api.schemas import CitySchema
from global_temps_rest_api.database_models import City


city_namespace = Namespace('city', description=' A list of cities that have global temperature data.')

country_model = city_namespace.model('Country', {
    'country_name': fields.String(required=True, description='Name of the country.'),
})

city_model = city_namespace.model('City', {
    'city_name': fields.String(required=True, description='Name of the city.'),
    'latitude': fields.String(required=True, description='Latitude the temperature recording took place.'),
    'longitude': fields.String(required=True, description='Longitude the temperature recording took place.'),
    'country': fields.Nested(country_model),
})


@city_namespace.route('')
class CitiesResource(Resource):

    @city_namespace.marshal_with(city_model)
    def get(self):
        """Get a list of all cities that have global temperature data available."""
        cities = City.query.all()
        return CitySchema(many=True).dump(cities)


@city_namespace.route('/<int:id>')
@city_namespace.response(404, 'Todo not found')
@city_namespace.param('id', 'The task identifier')
class CityResource(Resource):

    @city_namespace.marshal_with(city_model)
    def get(self, city_id):
        """Get a city"""
        city = City.query.get_or_404(city_id)
        return CitySchema().dump(city)
