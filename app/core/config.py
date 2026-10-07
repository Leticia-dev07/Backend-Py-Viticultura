from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "AgroClima Python API"
    DATABASE_URL: str
    API_PREFIX: str = "/api/v1"
    THINGSPEAK_BASE_URL: str = "https://api.thingspeak.com"
    THINGSPEAK_CHANNEL_ID: str = ""
    THINGSPEAK_READ_API_KEY: str = ""
    THINGSPEAK_RESULTS: int = 100
    MODEL_DIR: str = "./storage/models"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
