# ADR 0001: Modular Monolith

## Status

Accepted

## Context

Property Utility is an early-stage project with a single developer and a small team of contributors. The system will start with related domains such as geography, property, housing, employment, and education, and it should remain easy to evolve without introducing unnecessary operational complexity.

## Decision

Use a modular monolith rather than microservices.

## Consequences

- The project remains straightforward to run locally.
- Boundaries between API, application, domain, and infrastructure layers are explicit.
- The codebase can be refactored into services later if a future requirement justifies it.

## Alternatives Considered

- Microservices
- Distributed event-driven architecture
- A single unstructured package
