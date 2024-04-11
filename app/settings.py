import os
from pydantic import BaseSettings

class GlobalConfig(BaseSettings):
    DB_HOST: str = 'http://dynamodb:8000'
    ENVIRONMENT: str = os.getenv('ENVIRONMENT', 'LOCAL')
    AWS_REGION: str = 'ap-northeast-1'    
    DB_ACCESS_KEY_ID: str = os.getenv('DB_ACCESS_KEY_ID', 'foo')
    DB_SECRET_ACCESS_KEY: str = os.getenv('DB_SECRET_ACCESS_KEY', 'bar')


config = GlobalConfig()