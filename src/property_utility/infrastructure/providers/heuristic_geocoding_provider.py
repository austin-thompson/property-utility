from __future__ import annotations

from property_utility.domain.geographic_context import GeographicContext


class HeuristicGeocodingProvider:
    def resolve(self, address: str) -> GeographicContext:
        normalized_address = address.strip()
        parts = [part.strip() for part in normalized_address.split(",") if part.strip()]

        if len(parts) >= 3:
            city = parts[-2]
            state = parts[-1].upper()
        elif len(parts) == 2:
            city = parts[0]
            state = parts[1].upper()
        elif parts:
            city = parts[0]
            state = "UNKNOWN"
        else:
            city = "UNKNOWN"
            state = "UNKNOWN"

        return GeographicContext(
            address=address,
            normalized_address=normalized_address,
            city=city,
            state=state,
            country="US",
            confidence=0.91,
            source="heuristic",
        )
