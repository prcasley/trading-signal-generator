"""
Database configuration and initialization
"""
import asyncio
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base, sessionmaker
from core.config import settings

# Create database engines
engine = create_engine(settings.DATABASE_URL)
async_engine = create_async_engine(settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://"))

# Create session makers
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
AsyncSessionLocal = async_sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

# Create base class for models
Base = declarative_base()

async def init_db():
    """Initialize database tables (optional for MVP)"""
    try:
        if settings.DATABASE_URL and not settings.DATABASE_URL.startswith("sqlite"):
            async with async_engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
        print("Database initialized successfully")
    except Exception as e:
        print(f"Database initialization skipped: {e}")
        # Continue without database for MVP

async def get_async_session():
    """Get async database session"""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

def get_session():
    """Get sync database session"""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()