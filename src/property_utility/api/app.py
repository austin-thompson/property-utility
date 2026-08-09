from __future__ import annotations

from fastapi import FastAPI

from property_utility.api.routes.geographic_context import router as geographic_context_router
from property_utility.api.routes.health import router as health_router
from property_utility.api.routes.metrics import router as metrics_router
from property_utility.api.routes.observations import router as observations_router
from property_utility.core.config import settings
from property_utility.core.logging import configure_logging
from property_utility.infrastructure.repositories.geographic_context_repository import (
    InMemoryGeographicContextRepository,
)

configure_logging(settings.log_level)

app = FastAPI(title="Property Utility", version="0.1.0")
app.state.geocoding_settings = settings
app.state.geographic_context_repository = InMemoryGeographicContextRepository()
app.include_router(health_router)
app.include_router(geographic_context_router)
app.include_router(metrics_router)
app.include_router(observations_router)
