# ADR 0002: PostgreSQL + PostGIS

## Status

Accepted

## Context

Property Utility needs to manage relational data and future geographic relationships. The system should support spatial queries and time-series metrics without introducing multiple databases prematurely.

## Decision

Use PostgreSQL as the primary persistent store with PostGIS for geographic operations.

## Consequences

- The project can support relational and spatial data in one system.
- Time-series metrics and geographic relationships can be represented in a consistent model.
- The initial deployment remains simpler than introducing extra storage systems.

## Alternatives Considered

- MongoDB
- Neo4j
- Separate geospatial store plus relational store
