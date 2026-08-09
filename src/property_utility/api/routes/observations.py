from __future__ import annotations

from fastapi import APIRouter, Request
from pydantic import BaseModel, Field

from property_utility.application.geographic_context_service import GeographicContextService

router = APIRouter(prefix="/api/v1/observations", tags=["observations"])


class ObservationRequest(BaseModel):
    address: str = Field(min_length=1)


class ObservationResponse(BaseModel):
    address: str
    normalized_address: str
    city: str
    state: str
    country: str
    confidence: float
    source: str
    observation_type: str


@router.post("/geographic-context", response_model=ObservationResponse)
async def create_geographic_context_observation(
    request: Request,
    payload: ObservationRequest,
) -> ObservationResponse:
    repository = request.app.state.geographic_context_repository
    service = GeographicContextService(repository, settings=request.app.state.geocoding_settings)
    result = service.resolve_observation(payload.address)
    return ObservationResponse.model_validate(result)
