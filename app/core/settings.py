from pydantic_settings import SettingsConfigDict
from pydantic import BaseModel


class Settings(BaseModel):
    config = SettingsConfigDict(
        env_file=".env"
    )
    
settings = Settings()