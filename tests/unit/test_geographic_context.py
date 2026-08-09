import tempfile
from pathlib import Path

from fastapi.testclient import TestClient

from property_utility.api.app import app
from property_utility.core.config import Settings
from property_utility.domain.geographic_context import GeographicContext
from property_utility.infrastructure.providers.heuristic_geocoding_provider import (
    HeuristicGeocodingProvider,
)
from property_utility.infrastructure.providers.http_geocoding_provider import (
    HttpGeocodingProvider,
)
from property_utility.infrastructure.repositories.geographic_context_repository import (
    SqliteGeographicContextRepository,
)
from property_utility.application.geographic_context_service import build_geocoding_provider

client = TestClient(app)


def test_resolve_geographic_context_returns_normalized_payload() -> None:
    response = client.post(
        "/api/v1/geographic-context/resolve",
        json={"address": "1600 Amphitheatre Parkway, Mountain View, CA"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["address"] == "1600 Amphitheatre Parkway, Mountain View, CA"
    assert payload["normalized_address"] == "1600 Amphitheatre Parkway, Mountain View, CA"
    assert payload["city"] == "Mountain View"
    assert payload["state"] == "CA"
    assert payload["country"] == "US"
    assert payload["confidence"] > 0.8
    assert payload["source"] == "heuristic"


def test_resolve_geographic_context_persists_a_record() -> None:
    repository = app.state.geographic_context_repository
    repository.clear()

    response = client.post(
        "/api/v1/geographic-context/resolve",
        json={"address": "1 Infinite Loop, Cupertino, CA"},
    )

    assert response.status_code == 200
    records = repository.list()
    assert len(records) == 1
    assert records[0]["address"] == "1 Infinite Loop, Cupertino, CA"
    assert records[0]["city"] == "Cupertino"


def test_provider_returns_domain_model() -> None:
    provider = HeuristicGeocodingProvider()
    context = provider.resolve("123 Main Street, Denver, CO")

    assert isinstance(context, GeographicContext)
    assert context.city == "Denver"
    assert context.state == "CO"
    assert context.source == "heuristic"


def test_build_geocoding_provider_returns_heuristic_provider_for_heuristic_setting() -> None:
    settings = Settings(geocoding_provider="heuristic")

    provider = build_geocoding_provider(settings)

    assert isinstance(provider, HeuristicGeocodingProvider)


def test_build_geocoding_provider_returns_http_provider_for_http_setting() -> None:
    settings = Settings(geocoding_provider="http")

    provider = build_geocoding_provider(settings)

    assert isinstance(provider, HttpGeocodingProvider)


def test_create_geographic_context_observation_returns_normalized_payload() -> None:
    response = client.post(
        "/api/v1/observations/geographic-context",
        json={"address": "456 Market Street, San Francisco, CA"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["city"] == "San Francisco"
    assert payload["state"] == "CA"
    assert payload["observation_type"] == "geographic_context"


def test_compare_geographic_contexts_returns_similarity_metric() -> None:
    response = client.post(
        "/api/v1/metrics/geographic-context/compare",
        json={
            "address_a": "1600 Amphitheatre Parkway, Mountain View, CA",
            "address_b": "1 Infinite Loop, Cupertino, CA",
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["metric_type"] == "city_state_similarity"
    assert payload["city_match"] is False
    assert payload["state_match"] is True
    assert payload["similarity_score"] == 0.75


def test_get_geographic_context_returns_saved_record() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "geographic_context.sqlite3"
        repository = SqliteGeographicContextRepository(db_path)
        app.state.geographic_context_repository = repository
        repository.clear()

        response = client.post(
            "/api/v1/geographic-context/resolve",
            json={"address": "2 Apple Park Way, Cupertino, CA"},
        )

        assert response.status_code == 200

        saved_response = client.get(
            "/api/v1/geographic-context/2%20Apple%20Park%20Way,%20Cupertino,%20CA"
        )
        assert saved_response.status_code == 200
        payload = saved_response.json()
        assert payload["city"] == "Cupertino"
        assert payload["state"] == "CA"

        app.state.geographic_context_repository = None
        repository.close()
        del repository
