from __future__ import annotations

from fastapi import APIRouter, HTTPException

from property_utility.core.exceptions import DatabaseUnavailableError
from property_utility.infrastructure.database.engine import check_database_ready

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/live")
async def health_live() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/ready")
async def health_ready() -> dict[str, str]:
    try:
        await check_database_ready()
    except DatabaseUnavailableError as exc:
        raise HTTPException(status_code=503, detail="database unavailable") from exc
    return {"status": "ready"}
