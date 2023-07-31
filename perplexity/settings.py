from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Settings class for this application.
    Utilizes the BaseSettings from pydantic for environment variables.
    """

    openai_api_key: str
    anthropic_api_key: str
    azure_openai_api_key: str
    fake_list_api_key: str
    google_palm_api_key: str
    human_input_api_key: str
    jina_api_key: str
    prompt_layer_openai_api_key: str
    vertex_ai_api_key: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    """Function to get and cache settings.
    The settings are cached to avoid repeated disk I/O.
    """
    return Settings()
