# Context Documents

This directory is the architectural source of truth for Property Utility.
It preserves product intent, architecture decisions, and stable domain concepts so future coding sessions can extend the project without reconstructing the design intent.

The roadmap is the stable, high-level guide for the project. The cycle documents in the cycles directory are the detailed execution records for the work that has been completed or is currently underway.

## Recommended reading order

1. PRODUCT.md
2. ARCHITECTURE.md
3. ROADMAP.md
4. cycles/README.md
5. DATA_MODEL.md
6. DATA_SOURCES.md
7. METRICS.md
8. API_DESIGN.md
9. Relevant ADRs
10. TESTING.md
11. OPERATIONS.md
12. SECURITY.md
13. GLOSSARY.md

The following documents are normative unless superseded by an accepted ADR: PRODUCT.md, ARCHITECTURE.md, ROADMAP.md, DATA_MODEL.md, DATA_SOURCES.md, API_DESIGN.md, METRICS.md, and ADRs.

The current repository snapshot contains the initial architecture foundation, including the FastAPI skeleton, configuration, Alembic scaffolding, health endpoints, Docker Compose setup, and the initial test harness. The detailed implementation history for the current slice is recorded in the cycle documents.
