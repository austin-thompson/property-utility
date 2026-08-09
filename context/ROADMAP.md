# Roadmap

## Phase 0 — Architecture and Repository Foundation

Status: completed in the current repository snapshot.

Objective: create a coherent, executable project skeleton with explicit architectural boundaries.

### Scope

- repository setup
- Apache 2.0 license
- Python configuration
- context documentation
- modular-monolith package structure
- FastAPI application
- PostgreSQL/PostGIS
- SQLAlchemy wiring
- Alembic baseline
- configuration management
- logging
- health endpoints
- Docker
- testing
- linting
- typechecking

### Deliverables

- complete root README
- complete context documentation
- initial ADRs
- FastAPI app
- GET /health/live
- GET /health/ready
- PostgreSQL/PostGIS container
- async database session infrastructure
- initial Alembic migration baseline
- Ruff
- mypy
- pytest
- Makefile commands

### Acceptance Criteria

Docker Compose starts the api and postgres services, the health endpoints respond, Alembic migrations apply successfully, and make lint, make typecheck, and make test pass.

### Non-goals

- no Census ingestion
- no BLS ingestion
- no property analysis
- no geocoding provider
- no scoring
- no heatmaps
- no frontend
- no authentication
- no ML

### Exit condition

The repository provides a reliable architectural foundation for Phase 1.

## Future phases

- Phase 1: Geographic Foundation + Demographic MVP
- Phase 2: Housing Market Intelligence
- Phase 3: Employment + Education Intelligence
- Phase 4: Accessibility, Amenities, and Risk
- Phase 5: Comparative Market Intelligence
- Phase 6: Market Screening + Hotspot Detection
- Phase 7: Development and Catalyst Intelligence
- Phase 8: Rental + Ownership Economics
- Phase 9: Advanced Analysis
