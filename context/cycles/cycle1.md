# Cycle 1 — Geographic Foundation

## Purpose

Cycle 1 establishes the first working foundation for Property Utility by proving that the repository can support a small but meaningful geographic-intelligence slice.

## Status

Phase 0 and Phase 1 of the current planning model are now completed. The current work has moved into the first metrics-and-comparison slice, and Cycle 2 is now being sketched as the next follow-on cycle.

## Phase-Based Approach

### Phase 0 — Foundation and documentation (completed)

**Objective**

Create the initial repository structure, documentation, and developer workflow needed to support future product work.

**Scope covered**

- repository metadata and developer-facing documentation
- Python packaging and quality tooling
- initial project structure and architecture context

**Commit marker**

- 39e0035
- 89be1ae

**Outcomes**

- the repository now has a coherent baseline structure
- the project can be linted, type-checked, and tested from a consistent local workflow
- the initial architecture and planning documents are in place

### Phase 1 — Geographic context resolution (completed)

**Objective**

Add the first end-to-end slice for resolving an address into normalized geographic context and making that context retrievable.

**Scope covered**

- FastAPI application skeleton
- configuration and logging foundation
- a first geographic-context workflow with resolve and retrieval endpoints
- a lightweight repository-backed persistence path for geographic-context records

**Commit marker**

- a5c1e51

**Outcomes**

- the API can resolve and retrieve geographic-context records for a simple address-like input
- repository-backed persistence now exists for the first geographic slice

### Phase 2 — Geographic context refinement (completed)

**Objective**

Make the geographic-context flow more explicit by introducing lightweight domain structure and a clear provider boundary.

**Scope covered**

- a small domain object for geographic context
- a provider boundary for the resolution flow
- better separation between application, domain, and infrastructure concerns

**Commit marker**

- 1ade3a1

**Outcomes**

- the architecture is now clearer for future provider integrations
- the geographic-resolution flow is more structured and easier to extend

### Phase 3 — Geographic observations (completed)

**Objective**

Add the first normalized observation workflow so the system can capture data derived from an address.

**Scope covered**

- a first geographic-observation endpoint for creating normalized observations from an address
- a lightweight geographic-observation domain model
- continued refinement of the provider boundary and routing structure

**Commit marker**

- ff9a3ef

**Outcomes**

- the system can now represent and store a first observation-oriented workflow
- the repository has a verified slice that exercises more than the health endpoints

### Phase 4 — Provider integration and operational hardening (next)

**Objective**

Move the current heuristic flow toward a real provider-backed integration and strengthen local readiness and persistence behavior.

**Planned scope**

- replace the current heuristic resolution path with a real adapter-backed implementation
- validate database-backed readiness against the local container environment
- harden the local development experience around configuration and persistence

### Phase 5 — Metrics and comparison foundation (next)

**Objective**

Establish the first reusable metrics and derived signals so the platform can begin supporting comparison and screening workflows.

**Planned scope**

- introduce the first metric-oriented domain concepts
- define initial derived signals and comparative semantics
- connect those concepts to the underlying geographic context

## Problems and Gaps Identified

- live database-backed readiness has not yet been exercised against a running Postgres container
- no production provider integrations are in place yet
- the domain model remains lightweight and focused on the early slice
- scoring and derived-signal workflows are still future work

## Verification Evidence

- docker compose config succeeded for the api and postgres services
- ruff check passed
- mypy src passed with "Success: no issues found in 20 source files"
- pytest passed with 7 tests collected and 7 passed
