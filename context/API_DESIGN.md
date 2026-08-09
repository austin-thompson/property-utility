# API Design

The API namespace is /api/v1, and the current implementation exposes health endpoints plus a first geographic-context slice with a lightweight provider-backed domain model and a geographic-observations endpoint.

## Current endpoints

- GET /health/live
- GET /health/ready
- POST /api/v1/geographic-context/resolve
- GET /api/v1/geographic-context/{address}
- POST /api/v1/observations/geographic-context

## Future endpoints

- GET /api/v1/properties/{property_id}
- GET /api/v1/properties/{property_id}/analysis
- GET /api/v1/areas/{area_id}
- GET /api/v1/areas/{area_id}/metrics
- GET /api/v1/areas/{area_id}/trends
- GET /api/v1/compare
- GET /api/v1/rankings

The API should use JSON, ISO 8601 UTC timestamps, explicit error envelopes, versioned URLs, and bounded pagination.
