# Testing

Phase 0 tests cover application startup, configuration, /health/live, /health/ready, and database readiness behavior.

## Test categories

- unit
- integration
- provider contract

Live API calls should not be required for the standard test suite. Future provider tests should use frozen fixtures rather than live external APIs.
