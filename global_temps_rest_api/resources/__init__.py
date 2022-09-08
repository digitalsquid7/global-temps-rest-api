from flask_restx import Api

from .city import city_namespace

api = Api(
    version='1.0',
    title='Global Temperatures API',
    description='An API for retrieving global temperature data between the years of 1743 and 2013.'
)

api.add_namespace(city_namespace)
