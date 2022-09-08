from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Float, create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship, declarative_base


db = SQLAlchemy()


class Country(db.Model):
    __tablename__ = "country"
    id = Column(Integer, primary_key=True)
    country_name = Column(String(1000))
    cities = relationship("City", back_populates="country")


class City(db.Model):
    __tablename__ = "city"
    id = Column(Integer, primary_key=True)
    country_id = Column(Integer, ForeignKey("country.id"), nullable=False)
    city_name = Column(String(1000))
    latitude = Column(Float())
    longitude = Column(Float())
    country = relationship("Country", back_populates="cities")
