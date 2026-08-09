from __future__ import annotations

from typing import Protocol

from property_utility.core.config import Settings
from property_utility.domain.geographic_context import GeographicContext
from property_utility.domain.geographic_observation import GeographicObservation
from property_utility.infrastructure.providers.heuristic_geocoding_provider import (
    HeuristicGeocodingProvider,
)
from property_utility.infrastructure.providers.http_geocoding_provider import (
    HttpGeocodingProvider,
)


class GeographicContextRepository(Protocol):
    def save(self, record: dict[str, object]) -> None: ...

    def list(self) -> list[dict[str, object]]: ...

    def get_by_address(self, address: str) -> dict[str, object] | None: ...

    def clear(self) -> None: ...


def build_geocoding_provider(settings: Settings | None = None) -> object:
    resolved_settings = settings or Settings()
    if resolved_settings.geocoding_provider == "http":
        return HttpGeocodingProvider()
    return HeuristicGeocodingProvider()


class GeographicContextService:
    def __init__(
        self,
        repository: GeographicContextRepository,
        provider: object | None = None,
        settings: Settings | None = None,
    ) -> None:
        self._repository = repository
        self._provider = provider or build_geocoding_provider(settings)

    def resolve(self, address: str) -> dict[str, object]:
        context = self._provider.resolve(address)
        record = self._to_record(context)
        self._repository.save(record)
        return record

    def get_by_address(self, address: str) -> dict[str, object] | None:
        return self._repository.get_by_address(address)

    def resolve_observation(self, address: str) -> dict[str, object]:
        context = self._provider.resolve(address)
        observation = GeographicObservation(
            address=context.address,
            normalized_address=context.normalized_address,
            city=context.city,
            state=context.state,
            country=context.country,
            confidence=context.confidence,
            source=context.source,
        )
        record = self._to_observation_record(observation)
        self._repository.save(record)
        return record

    def _to_record(self, context: GeographicContext) -> dict[str, object]:
        return {
            "address": context.address,
            "normalized_address": context.normalized_address,
            "city": context.city,
            "state": context.state,
            "country": context.country,
            "confidence": context.confidence,
            "source": context.source,
        }

    def _to_observation_record(self, observation: GeographicObservation) -> dict[str, object]:
        return {
            "address": observation.address,
            "normalized_address": observation.normalized_address,
            "city": observation.city,
            "state": observation.state,
            "country": observation.country,
            "confidence": observation.confidence,
            "source": observation.source,
            "observation_type": observation.observation_type,
        }
