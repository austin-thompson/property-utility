# Property Utility

Property Utility is an API-first geographic and property intelligence engine for combining real-estate, demographic, economic, and risk data into a consistent analytical system.

## Status

This repository is in early Phase 0 development. The current focus is repository setup, architecture documentation, configuration, and a small executable API skeleton.

## Capabilities in this phase

- FastAPI application skeleton
- PostgreSQL/PostGIS-ready configuration
- SQLAlchemy async database wiring
- Alembic baseline structure
- health endpoints
- quality tooling via Ruff, mypy, and pytest

## Architecture summary

The project uses a modular monolith with clear boundaries between API, application, domain, and infrastructure layers.

## Local development

```bash
cp .env.example .env
make install
make run
```

## Quality checks

```bash
make lint
make typecheck
make test
```

## Context

The architectural source of truth lives in the [context](context/README.md) directory.

> This project is early-stage and analytical output should not be interpreted as financial advice.
