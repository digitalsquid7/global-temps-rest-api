import os


class EnvVarRetriever:

    @staticmethod
    def retrieve(name: str) -> str:
        env_var = os.getenv(name)

        if env_var is None:
            raise ValueError(f"Environment variable '{name}' does not have a value.")

        return env_var
