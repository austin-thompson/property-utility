# Security

## Current posture

- Environment-based secrets
- .env excluded from Git
- .env.example committed
- validated third-party payloads
- HTTP timeouts
- bounded retries
- rate-limit awareness
- SQLAlchemy parameterization
- no credentials in logs
- minimal dependencies
- no authentication required for local MVP

Public API authentication is intentionally deferred until there is a reason to expose the service externally.
