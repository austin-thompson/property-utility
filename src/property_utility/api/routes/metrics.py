from __future__ import annotations

from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/api/v1/metrics", tags=["metrics"])


class CompareGeographicContextsRequest(BaseModel):
    address_a: str = Field(min_length=1)
    address_b: str = Field(min_length=1)


class CompareGeographicContextsResponse(BaseModel):
    metric_type: str
    city_match: bool
    state_match: bool
    similarity_score: float


@router.post("/geographic-context/compare", response_model=CompareGeographicContextsResponse)
async def compare_geographic_contexts(
    payload: CompareGeographicContextsRequest,
) -> CompareGeographicContextsResponse:
    city_a = payload.address_a.split(",")[-2].strip().lower() if "," in payload.address_a else ""
    city_b = payload.address_b.split(",")[-2].strip().lower() if "," in payload.address_b else ""
    state_a = payload.address_a.split(",")[-1].strip().upper() if "," in payload.address_a else ""
    state_b = payload.address_b.split(",")[-1].strip().upper() if "," in payload.address_b else ""

    city_match = city_a == city_b
    state_match = state_a == state_b
    similarity_score = 0.75 if state_match and not city_match else 1.0 if state_match and city_match else 0.0

    return CompareGeographicContextsResponse(
        metric_type="city_state_similarity",
        city_match=city_match,
        state_match=state_match,
        similarity_score=similarity_score,
    )
