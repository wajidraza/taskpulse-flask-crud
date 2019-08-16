# Configuration module for TaskPulse Distributed Task & Issue Tracker
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "TaskPulse Distributed Task & Issue Tracker"
    port: int = int(os.getenv("PORT", "8080"))
    database_url: str = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/taskpulse_flask_crud_db")
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")

settings = Settings()
