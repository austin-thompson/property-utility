# ADR 0003: Provider Adapter Boundary

## Status

Accepted

## Context

External providers change over time. Licensing, payload schemas, and availability differ between data sources, especially for census, labor, education, and hazard datasets. Domain logic should not be tightly coupled to provider-specific transport formats.

## Decision

All external data providers integrate through explicit adapters and provider-specific DTOs.

## Consequences

- Provider schemas do not leak into the domain model.
- The system can swap providers without rewriting domain logic.
- The architecture stays explicit and testable.

## Alternatives Considered

- Direct HTTP calls across application services
- Embedding provider-specific schemas into domain entities
- A general-purpose adapter layer with no explicit provider DTOs
