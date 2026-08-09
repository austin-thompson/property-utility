# Property Utility

Property Utility is an API-first geographic and property intelligence engine for combining real-estate, demographic, economic, and risk data into a consistent analytical system.

## Status

This repository now has an initial architecture foundation plus a first functional geographic-context slice, a small provider-boundary refinement, and a new geographic-observation endpoint. The current implementation includes a runnable FastAPI skeleton, configuration management, async database wiring, Alembic scaffolding, health endpoints, and a persisted address-to-geographic-context flow.

## State snapshot

- Current phase: Phase 5 — metrics and comparison foundation
- Current focus: preserve the architectural foundation while introducing the first reusable comparison metric built on top of geographic context
- What is working: FastAPI app skeleton, health endpoints, async database scaffolding, geographic-context resolution and retrieval, a first geographic-observation workflow, configurable provider selection between heuristic and HTTP-backed implementations, and a first comparison metric endpoint for geographic contexts
- Next milestone: refine the first metric model and capture the next cycle plan in the cycle documentation before broadening the scope
- Known gaps: no production provider integrations yet, the metric model remains intentionally lightweight, and live Postgres-backed readiness has not yet been exercised end to end

## Current capabilities

- FastAPI application skeleton
- PostgreSQL/PostGIS-ready configuration
- async SQLAlchemy database wiring
- Alembic baseline structure
- health endpoints at /health/live and /health/ready
- geographic-context resolution and retrieval endpoints
- geographic-observation creation through a lightweight observations API
- persisted geographic-context records via a lightweight repository layer
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
