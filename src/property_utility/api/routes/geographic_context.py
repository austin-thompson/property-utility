from __future__ import annotations

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field

from property_utility.application.geographic_context_service import GeographicContextService

router = APIRouter(prefix="/api/v1/geographic-context", tags=["geographic-context"])


class ResolveGeographicContextRequest(BaseModel):
    address: str = Field(min_length=1)


class GeographicContextResponse(BaseModel):
    address: str
    normalized_address: str
    city: str
    state: str
    country: str
    confidence: float
    source: str


@router.post("/resolve", response_model=GeographicContextResponse)
async def resolve_geographic_context(
    request: Request,
    payload: ResolveGeographicContextRequest,
) -> GeographicContextResponse:
    repository = request.app.state.geographic_context_repository
    service = GeographicContextService(repository, settings=request.app.state.geocoding_settings)
    result = service.resolve(payload.address)
    return GeographicContextResponse.model_validate(result)


@router.get("/{address}", response_model=GeographicContextResponse)
async def get_geographic_context(request: Request, address: str) -> GeographicContextResponse:
    repository = request.app.state.geographic_context_repository
    service = GeographicContextService(repository, settings=request.app.state.geocoding_settings)
    result = service.get_by_address(address)
    if result is None:
        raise HTTPException(status_code=404, detail="not found")
    return GeographicContextResponse.model_validate(result)
