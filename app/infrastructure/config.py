"""
This file defines global application-level settings 
"""
import os
from pydantic_settings import BaseSettings  
class Settings(BaseSettings):
 

    # PostgreSQL connection string
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://libuser:abd123456@localhost:5432/libdb"
    )


# Instantiate global settings object
# This will be imported and used throughout the app
settings = Settings()
