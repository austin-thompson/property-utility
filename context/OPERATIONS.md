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

## Configuration

Configuration comes from environment variables, including DATABASE_URL, APP_ENV, and LOG_LEVEL.

## Future observability

The current Phase 0 implementation is intentionally simple; future work can add richer observability and backup practices as the system grows.
