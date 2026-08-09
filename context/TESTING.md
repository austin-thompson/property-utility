# Testing

Phase 0 tests cover the application skeleton, configuration, /health/live, /health/ready, and the database readiness behavior through a focused unit suite.

## Test categories

- unit
- integration
- provider contract

The current repository snapshot includes unit tests for the health endpoints. Live API calls should not be required for the standard test suite. Future provider tests should use frozen fixtures rather than live external APIs.
