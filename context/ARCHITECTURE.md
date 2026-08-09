# Architecture

Property Utility uses a modular monolith with clear boundaries between API, application, domain, and infrastructure layers.

## Layering

```text
External Providers
      ↓
Infrastructure Adapters
      ↓
Application Services
      ↓
Domain Models / Metrics
      ↓
Persistence
```

API routes invoke application use cases. Application code coordinates domain logic and ports. Infrastructure implements database repositories, geocoding adapters, and external data-provider adapters. Domain code remains largely framework-independent.

## Dependency Rules

- Domain must not depend on FastAPI.
- Domain must not depend on SQLAlchemy.
- Domain must not depend on httpx.
- Domain must not know Census/BLS/FEMA API payload formats.
- Application may depend on domain interfaces.
- Infrastructure implements application/domain ports.
- API performs transport-level validation and response shaping.

## Provider Architecture

External datasets use explicit adapters:

```text
Census API -> CensusProvider
BLS API -> BLSProvider
FRED API -> FREDProvider
FEMA -> FEMAProvider
```

Provider adapters handle HTTP communication, retries, timeouts, provider-specific DTOs, payload validation, schema translation, rate limits, and provider-specific error handling. Domain code should receive normalized values.

## Geographic Domain Model

Geography is foundational infrastructure. In the long term, entities may include Address, Coordinate, Property, CensusBlock, CensusBlockGroup, CensusTract, ZIPCode, Municipality, County, MetroArea, State, and SchoolDistrict. A property belongs to multiple overlapping geographic contexts.

The current implementation includes a lightweight geographic-context slice that resolves an address into a normalized structure and stores the result in a repository-backed record for retrieval. It now also uses a small domain object, a provider boundary, and a lightweight geographic-observation endpoint to make that flow more explicit before introducing a richer domain model.
