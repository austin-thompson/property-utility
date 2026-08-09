from __future__ import annotations

from fastapi import FastAPI

from property_utility.api.routes.health import router as health_router
from property_utility.core.config import settings
from property_utility.core.logging import configure_logging

configure_logging(settings.log_level)

app = FastAPI(title="Property Utility", version="0.1.0")
app.include_router(health_router)
