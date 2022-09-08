from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    connection_string: str
    track_modifications: bool


@dataclass
class EnvironmentConfig:
    file_config_path: str
