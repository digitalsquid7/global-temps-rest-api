import abc
from configparser import ConfigParser

from global_temps_rest_api.config.config_dataclasses import DatabaseConfig


class IniConfigRetriever(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def retrieve(config_parser: ConfigParser):
        pass


class DatabaseConfigRetriever(IniConfigRetriever):
    @staticmethod
    def retrieve(config_parser: ConfigParser) -> DatabaseConfig:
        return DatabaseConfig(
            config_parser.get("DATABASE", "connection_string"),
            config_parser.getboolean("DATABASE", "track_modifications"),
        )
