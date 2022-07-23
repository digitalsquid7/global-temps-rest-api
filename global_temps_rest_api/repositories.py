from typing import List, Dict, Any

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from global_temps_rest_api.sql import City, Country


class CityRepository:
    """High level class for accessing global temperatures data."""

    def __init__(self, engine):
        self.engine = engine

    def read(self) -> Dict[str, Any]:
        # create session and add objects
        with Session(self.engine) as session:
            rows = session.query(City).join(Country)
            return rows
