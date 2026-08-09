from __future__ import annotations

from collections.abc import AsyncIterator

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from property_utility.core.config import settings
from property_utility.core.exceptions import DatabaseUnavailableError


class Base(DeclarativeBase):
    pass


engine = create_async_engine(settings.database_url, echo=False)

SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_session() -> AsyncIterator[AsyncSession]:
    async with SessionLocal() as session:
        yield session


async def check_database_ready() -> bool:
    try:
        async with engine.connect() as connection:
            result = await connection.execute(text("SELECT 1"))
            return result.scalar_one() == 1
    except Exception as exc:
        raise DatabaseUnavailableError("database unavailable") from exc


