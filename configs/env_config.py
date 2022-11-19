from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "Mail Watch"
    database_url: str
    database_password: str
    pushover_api_token: str
    pushover_user_key: str

    class Config:
        env_file ='.env'
        env_file_encoding ='utf-8'

@lru_cache
def env_settings():
    '''
    Allows the env setting to be load once 
    '''
    return Settings()

