# Data Model

The initial data model should be a hybrid between explicit domain entities and normalized metric observations.

## Foundational concepts

- geographic_areas
- properties
- addresses
- data_sources
- observations
- metrics
- metric_observations

## Direction

The project should use explicit core geographic/domain entities while also supporting normalized time-series metric observations where appropriate. PostGIS geometry and geography columns should support future spatial operations.

## Tradeoffs

A fully generic EAV model would be too flexible for the initial project and would make analysis harder to reason about. Strongly typed domain tables are better for the core entities, while a normalized metric-observation pattern is useful for repeated time-series data such as population, median income, median home price, and housing inventory.
