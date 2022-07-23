import os


class EnvVarUtil:

    @staticmethod
    def get_required_env_var(name: str) -> str:
        env_var = os.getenv(name)

        if env_var is None:
            raise ValueError(f"Required environment variable '{name}' does not have a value.")

        return env_var
