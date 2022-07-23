from flask_restx import Api, fields

api = Api(
    version='1.0',
    title='Global Temperatures API',
    description='An API for retrieving global temperature data between the years of 1743 and 2013.'
)

country_model = api.model('Country', {
    'country_name': fields.String(required=True, description='Name of the country.'),
})

city_model = api.model('City', {
    'city_name': fields.String(required=True, description='Name of the city.'),
    'latitude': fields.String(required=True, description='Latitude the temperature recording took place.'),
    'longitude': fields.String(required=True, description='Longitude the temperature recording took place.'),
    'country': fields.Nested(country_model),
})
