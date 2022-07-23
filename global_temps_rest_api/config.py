import abc
from configparser import ConfigParser
from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    connection_string: str


class ConfigRetriever(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def retrieve(config_parser: ConfigParser):
        pass


class DatabaseConfigRetriever(ConfigRetriever):
    @staticmethod
    def retrieve(config_parser: ConfigParser) -> DatabaseConfig:
        return DatabaseConfig(
            config_parser.get("DATABASE", "connection_string")
        )
