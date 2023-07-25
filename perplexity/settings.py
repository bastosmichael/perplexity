from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    """
    Settings class for this application.
    Utilizes the BaseSettings from pydantic for environment variables.
    """
    openai_api_key: str

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    """Function to get and cache settings.
    The settings are cached to avoid repeated disk I/O.
    """
    return Settings()
