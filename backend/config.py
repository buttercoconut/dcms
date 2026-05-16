from pydantic import BaseSettings

class Settings(BaseSettings):
    app_title: str = "Server Status API"
    app_version: str = "0.1.0"
    app_description: str = "API to collect and expose server status information."

    class Config:
        env_file = ".env"
