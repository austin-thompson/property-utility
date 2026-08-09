# Property Utility

Property Utility is an API-first geographic and property intelligence engine for combining real-estate, demographic, economic, and risk data into a consistent analytical system.

## Status

This repository is now in a completed Phase 0 state for the initial architecture bootstrap. The current implementation includes a runnable FastAPI skeleton, config management, async database wiring, Alembic scaffolding, health endpoints, and the core documentation set.

## Capabilities in this phase

- FastAPI application skeleton
- PostgreSQL/PostGIS-ready configuration
- async SQLAlchemy database wiring
- Alembic baseline structure
- health endpoints at /health/live and /health/ready
- quality tooling via Ruff, mypy, and pytest
- Docker Compose configuration for api and postgres services

## Architecture summary

The project uses a modular monolith with clear boundaries between API, application, domain, and infrastructure layers.

## Local development

```bash
cp .env.example .env
make install
make run
```

## Quality checks

The following commands have been exercised successfully in the current repository snapshot:

```bash
make lint
make typecheck
make test
```

To validate the Compose configuration locally, use:

```bash
docker compose config
```

## Context

The architectural source of truth lives in the [context](context/README.md) directory.

> This project is early-stage and analytical output should not be interpreted as financial advice.
