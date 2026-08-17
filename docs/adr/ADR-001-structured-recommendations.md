# ADR-001: Structured recommendations are the source of truth

## Status

Accepted

## Context

Keyword checks against Markdown cannot reliably distinguish selected, mentioned, and rejected technologies.

## Decision

Store saved decisions as schema-versioned JSON, validate them semantically, and render Markdown from that JSON.

## Consequences

Reports become testable and machine-readable. Chat-only answers still follow the same conceptual contract. The JSON schema and renderer must evolve together.

## Review trigger

Review when a second output format needs fields that cannot be represented by schema version 1.0.
