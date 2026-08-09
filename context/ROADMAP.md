# Roadmap

## Overarching Purpose

Property Utility is being built as a modular monolith for geographic intelligence and property-context analysis. The long-term objective is to turn fragmented property and area data into a consistent, traceable, and reusable model that can support analysis, comparison, and screening workflows.

This roadmap is intentionally high-level. It captures the durable direction of the work, while the detailed implementation history and execution details live in the cycle documents.

## Guiding Direction

- start with a reliable geographic foundation before expanding into richer scoring and analytics
- preserve explicit boundaries between API, application, domain, and infrastructure layers
- normalize provider-specific data into stable domain concepts
- keep analytical conclusions traceable to underlying measurements
- prefer small, verifiable increments over speculative expansion

## Current State

The repository now has a verified architectural foundation for future product work. The current focus is to preserve that foundation while expanding toward geographic and property-market intelligence in small, well-bounded increments.

## Phased Direction

The work is organized into a small number of well-defined phases. Each phase is intended to land as a coherent checkpoint before the next one begins, which fits a human-in-the-loop workflow well.

- Phase 0 — Geographic foundation (completed): established the repository foundation, the first geographic-context workflow, and the initial observation capability.
- Phase 1 — Provider-backed integration (completed): introduced a configurable geocoding-provider path and established the basis for a more durable provider-backed integration.
- Phase 2 — Analytical foundation (current): introduce the first reusable comparison metric built on top of the geographic foundation.
- Phase 3 — Product workflows: expand into richer property and area analysis experiences and broader data-source integration.
- Phase 4 — Operational hardening: validate provider-backed flows in the local environment and strengthen readiness, persistence, and developer experience.
- Phase 5 — Metrics and comparison foundation: build the first reusable metrics and comparison semantics on top of the geographic foundation.

## Current Cycle

The current cycle is Cycle 1, which documents the implementation work for the geographic foundation phase.

### Cycle 1 Summary

Cycle 1 established the repository foundation, added the first geographic-context resolution workflow, refined the architecture around provider boundaries and domain structure, and introduced the first geographic-observation capability. The detailed scope, outcomes, evidence, and follow-up items are recorded in the cycle document.

## Next Focus

The next work should move the current heuristic geographic flow toward a more durable provider-backed integration path while keeping the implementation small and testable.

## Relationship to Cycle Documents

The roadmap remains stable and directional, but it now carries a light phase structure for planning. The cycle documents record the concrete work performed in each implementation slice, including objectives, outcomes, verification evidence, and remaining gaps.
