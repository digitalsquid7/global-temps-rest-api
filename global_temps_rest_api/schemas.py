from flask_marshmallow import fields
from flask_marshmallow.sqla import auto_field
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested

from global_temps_rest_api.database_models import City, Country


class CountrySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Country


class CitySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = City
        include_relationships = True
        load_instance = True

    country = Nested(CountrySchema, many=False)
