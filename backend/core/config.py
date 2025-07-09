"""
Application configuration settings
"""
import os
from typing import List
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Database (optional for MVP)
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./trading_signals.db")
    
    # Redis (optional for MVP)
    REDIS_URL: str = os.getenv("REDIS_URL", "")
    
    # API Keys
    ALPHA_VANTAGE_API_KEY: str = os.getenv("ALPHA_VANTAGE_API_KEY", "demo")
    
    # CORS
    ALLOWED_ORIGINS: List[str] = os.getenv("ALLOWED_ORIGINS", "*").split(",") if os.getenv("ALLOWED_ORIGINS") else ["*"]
    
    # Real-time settings
    SIGNAL_UPDATE_INTERVAL: int = 30  # seconds
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    
    class Config:
        env_file = ".env"

settings = Settings()