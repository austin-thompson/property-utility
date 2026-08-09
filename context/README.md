# Context Documents

This directory is the architectural source of truth for Property Utility.
It preserves product intent, architecture decisions, and stable domain concepts so future coding sessions can extend the project without reconstructing the design intent.

## Recommended reading order

1. PRODUCT.md
2. ARCHITECTURE.md
3. ROADMAP.md
4. DATA_MODEL.md
5. DATA_SOURCES.md
6. METRICS.md
7. API_DESIGN.md
8. Relevant ADRs
9. TESTING.md
10. OPERATIONS.md
11. SECURITY.md
12. GLOSSARY.md

The following documents are normative unless superseded by an accepted ADR: PRODUCT.md, ARCHITECTURE.md, ROADMAP.md, DATA_MODEL.md, DATA_SOURCES.md, API_DESIGN.md, METRICS.md, and ADRs.

The current repository snapshot contains the completed Phase 0 architecture foundation, including the initial FastAPI skeleton, configuration, Alembic scaffolding, health endpoints, Docker Compose setup, and the initial test harness.

The context/cycles directory contains execution planning and historical implementation records. The stable ROADMAP should not become an implementation diary.
