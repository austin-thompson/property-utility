from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GeographicContext:
    address: str
    normalized_address: str
    city: str
    state: str
    country: str
    confidence: float
    source: str
