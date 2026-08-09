# API Design

The future API namespace is /api/v1. Phase 0 implements only the health endpoints.

## Phase 0 endpoints

- GET /health/live
- GET /health/ready

## Future endpoints

- GET /api/v1/properties/{property_id}
- GET /api/v1/properties/{property_id}/analysis
- GET /api/v1/areas/{area_id}
- GET /api/v1/areas/{area_id}/metrics
- GET /api/v1/areas/{area_id}/trends
- GET /api/v1/compare
- GET /api/v1/rankings

The API should use JSON, ISO 8601 UTC timestamps, explicit error envelopes, versioned URLs, and bounded pagination.
