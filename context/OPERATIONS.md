# Operations

## Local workflow

```bash
cp .env.example .env
docker compose up --build
make migrate
make test
make lint
make typecheck
```

The project uses PostgreSQL with PostGIS in Docker Compose. Migrations are managed with Alembic. Logs should remain structured and lightweight, with health checks and graceful shutdown behavior in mind.

The current implementation includes the health endpoints and the initial database readiness check. The local workflow should be run from the repository root after copying .env.example to .env.

## Configuration

Configuration comes from environment variables, including DATABASE_URL, APP_ENV, and LOG_LEVEL.

## Verification notes

The current repository snapshot has verified the Compose configuration and the local quality suite via ruff, mypy, and pytest. Docker services should still be started locally before relying on the readiness endpoint.

## Future observability

The current implementation is intentionally simple; future work can add richer observability and backup practices as the system grows.
